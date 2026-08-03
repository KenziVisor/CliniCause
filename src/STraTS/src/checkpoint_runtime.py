"""Runtime glue for metadata-bound STraTS checkpoint roles."""

from __future__ import annotations

from pathlib import Path
import shutil
from typing import Any, Mapping, Sequence

from artifact_metadata import (
    build_artifact_metadata,
    cohort_descriptor,
    file_descriptor,
    validate_artifact_metadata,
    write_metadata,
)
from runtime_contract import model_config_from_args, training_config_from_args


PREPROCESSING_STATE_FILENAME = "pt_saved_variables.pkl"
CHECKPOINT_SCHEMA = {
    "format": "pytorch_state_dict",
    "version": 1,
}


def architecture_mode(args: Any) -> str:
    if bool(args.pretrain):
        return "pretrain"
    return "finetune" if bool(args.finetune) else "scratch"


def input_descriptors(args: Any, *, pretrain: bool | None = None) -> dict[str, dict[str, Any]]:
    if pretrain is None:
        pretrain = bool(args.pretrain)
    inputs = {"processed_data": file_descriptor(args.processed_data_path)}
    if not pretrain:
        inputs["latent_tags"] = file_descriptor(args.latent_csv_path)
        init_checkpoint = getattr(args, "init_ckpt_path", None)
        if init_checkpoint:
            inputs["initialization_checkpoint"] = file_descriptor(init_checkpoint)
    return inputs


def _base_expected(args: Any, architecture: str) -> dict[str, Any]:
    return {
        "artifact_kind": "checkpoint",
        "schema": CHECKPOINT_SCHEMA,
        "pipeline_run_id": str(args.pipeline_run_id),
        "dataset": str(args.dataset),
        "model": str(args.model_type),
        "architecture_mode": architecture,
        "config_fingerprint": str(args.config_fingerprint),
        "base_seed": int(args.base_seed),
        "dataset_seed": int(args.dataset_seed),
        "model_seed": int(args.seed),
        "effective_seed": int(args.effective_seed),
    }


def _validated_preprocessing_state(
    checkpoint_path: str,
    metadata: Mapping[str, Any],
) -> Path:
    descriptor = metadata.get("preprocessing_state")
    if not isinstance(descriptor, Mapping):
        raise ValueError(
            f"Fine-tune/pretrain checkpoint lacks preprocessing_state metadata: {checkpoint_path}"
        )
    state_path = Path(checkpoint_path).parent / PREPROCESSING_STATE_FILENAME
    actual = file_descriptor(state_path)
    for field in ("name", "size", "sha256"):
        if actual[field] != descriptor.get(field):
            raise ValueError(
                f"Preprocessing-state {field} does not match checkpoint metadata: {state_path}"
            )
    return state_path


def _copy_preprocessing_state(source: Path, output_dir: str) -> Path:
    destination = Path(output_dir) / PREPROCESSING_STATE_FILENAME
    if source.resolve() == destination.resolve():
        return destination
    if destination.exists():
        if file_descriptor(destination) != file_descriptor(source):
            raise FileExistsError(
                f"Refusing to overwrite mismatched preprocessing state: {destination}"
            )
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination


def prepare_checkpoint_roles(args: Any) -> None:
    """Resolve architecture before constructing Dataset or the torch model."""

    if args.pretrain and (args.init_ckpt_path or args.restore_ckpt_path):
        raise ValueError("Pretraining cannot initialize or restore a supervised checkpoint.")

    if args.init_ckpt_path:
        if args.model_type not in {"strats", "istrats"}:
            raise ValueError("Pretraining initialization is only valid for strats/istrats.")
        expected = _base_expected(args, "pretrain")
        expected["inputs"] = input_descriptors(args, pretrain=True)
        expected["ordered_targets"] = []
        expected["model_config"] = model_config_from_args(args, "pretrain")
        metadata = validate_artifact_metadata(args.init_ckpt_path, expected=expected)
        args.init_metadata = metadata
        source = _validated_preprocessing_state(args.init_ckpt_path, metadata)
        args.preprocessing_state_path = str(_copy_preprocessing_state(source, args.output_dir))
        args.finetune = True
        return

    if args.restore_ckpt_path:
        metadata = validate_artifact_metadata(
            args.restore_ckpt_path,
            expected={
                "artifact_kind": "checkpoint",
                "schema": CHECKPOINT_SCHEMA,
                "pipeline_run_id": str(args.pipeline_run_id),
                "dataset": str(args.dataset),
                "model": str(args.model_type),
                "config_fingerprint": str(args.config_fingerprint),
                "base_seed": int(args.base_seed),
                "dataset_seed": int(args.dataset_seed),
                "model_seed": int(args.seed),
                "effective_seed": int(args.effective_seed),
            },
        )
        restored_architecture = metadata.get("architecture_mode")
        if restored_architecture not in {"scratch", "finetune"}:
            raise ValueError(
                "Supervised restore requires scratch or finetune architecture metadata; "
                f"got {restored_architecture!r}."
            )
        args.finetune = restored_architecture == "finetune"
        expected = _base_expected(args, restored_architecture)
        expected["inputs"] = input_descriptors(args, pretrain=False)
        expected["model_config"] = model_config_from_args(args, restored_architecture)
        metadata = validate_artifact_metadata(args.restore_ckpt_path, expected=expected)
        if args.finetune:
            args.preprocessing_state_path = str(
                _validated_preprocessing_state(args.restore_ckpt_path, metadata)
            )
        args.restore_metadata = metadata


def validate_restored_dataset(args: Any, dataset: Any) -> None:
    """Bind checkpoint target/cohort metadata after canonical dataset loading."""

    if args.init_ckpt_path:
        authoritative = getattr(dataset, "authoritative_splits", None)
        if not isinstance(authoritative, Mapping):
            raise ValueError(
                "Pretraining initialization requires authoritative supervised splits."
            )
        missing_keys = {"train", "val"} - set(authoritative)
        if missing_keys:
            raise ValueError(
                f"Authoritative splits are missing keys required for initialization: {sorted(missing_keys)}"
            )
        pretrain_ids = list(authoritative["train"])
        pretrain_ids += list(authoritative["val"])
        validate_artifact_metadata(
            args.init_ckpt_path,
            expected={
                "ordered_targets": [],
                "cohort": cohort_descriptor(pretrain_ids),
            },
        )

    if not args.restore_ckpt_path:
        return
    validate_artifact_metadata(
        args.restore_ckpt_path,
        expected={
            "ordered_targets": list(dataset.target_columns),
            "cohort": cohort_descriptor(dataset.metadata_cohort_ids),
        },
    )


def build_runtime_metadata(
    args: Any,
    dataset: Any,
    artifact_path: str,
    *,
    artifact_kind: str,
    schema: Mapping[str, Any],
    producing_command: Sequence[object],
    cohort_ids: Sequence[object] | None = None,
) -> dict[str, Any]:
    preprocessing_state = None
    candidate = Path(args.output_dir) / PREPROCESSING_STATE_FILENAME
    if candidate.is_file():
        preprocessing_state = file_descriptor(candidate)
    inputs = input_descriptors(args)
    if artifact_kind == "prediction":
        checkpoint_path = args.restore_ckpt_path
        if checkpoint_path is None:
            checkpoint_path = str(Path(args.output_dir) / "checkpoint_best.bin")
        inputs["checkpoint"] = file_descriptor(checkpoint_path)
    model_config = model_config_from_args(args, architecture_mode(args))
    if artifact_kind == "prediction" and isinstance(
        getattr(args, "restore_metadata", None), Mapping
    ):
        training_config = dict(args.restore_metadata["training_config"])
    else:
        training_config = training_config_from_args(args)
    return build_artifact_metadata(
        artifact_path,
        artifact_kind=artifact_kind,
        pipeline_run_id=args.pipeline_run_id,
        dataset=args.dataset,
        model=args.model_type,
        architecture_mode=architecture_mode(args),
        ordered_targets=list(dataset.target_columns),
        config_fingerprint=args.config_fingerprint,
        base_seed=args.base_seed,
        dataset_seed=args.dataset_seed,
        model_seed=args.seed,
        effective_seed=args.effective_seed,
        producing_command=producing_command,
        schema=schema,
        cohort_ids=(
            dataset.metadata_cohort_ids if cohort_ids is None else cohort_ids
        ),
        model_config=model_config,
        training_config=training_config,
        inputs=inputs,
        preprocessing_state=preprocessing_state,
    )


def write_runtime_metadata(
    args: Any,
    dataset: Any,
    artifact_path: str,
    *,
    artifact_kind: str,
    schema: Mapping[str, Any],
    producing_command: Sequence[object],
    cohort_ids: Sequence[object] | None = None,
) -> Path:
    metadata = build_runtime_metadata(
        args,
        dataset,
        artifact_path,
        artifact_kind=artifact_kind,
        schema=schema,
        producing_command=producing_command,
        cohort_ids=cohort_ids,
    )
    return write_metadata(artifact_path, metadata)

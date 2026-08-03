"""Pure artifact provenance helpers used by STraTS checkpoints and predictions."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any, Iterable, Mapping, Sequence

from runtime_contract import (
    scientific_config_fingerprint,
    validate_training_config,
)


METADATA_SCHEMA_VERSION = 2
REQUIRED_METADATA_FIELDS = {
    "metadata_schema_version",
    "artifact_kind",
    "artifact_name",
    "artifact_sha256",
    "artifact_size",
    "pipeline_run_id",
    "dataset",
    "model",
    "architecture_mode",
    "ordered_targets",
    "config_fingerprint",
    "base_seed",
    "dataset_seed",
    "model_seed",
    "effective_seed",
    "producing_command",
    "schema",
    "cohort",
    "model_config",
    "training_config",
    "scientific_config_fingerprint",
    "inputs",
}


def metadata_path_for(artifact_path: str | os.PathLike[str]) -> Path:
    return Path(str(Path(artifact_path)) + ".metadata.json")


def sha256_file(path: str | os.PathLike[str], chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def cohort_descriptor(ids: Iterable[object]) -> dict[str, Any]:
    canonical_ids = [str(value) for value in ids]
    if len(canonical_ids) != len(set(canonical_ids)):
        raise ValueError("Cannot describe a cohort containing duplicate canonical IDs.")
    ordered_ids = sorted(canonical_ids)
    return {
        "count": len(ordered_ids),
        "sha256": canonical_json_sha256(ordered_ids),
    }


def file_descriptor(path: str | os.PathLike[str]) -> dict[str, Any]:
    artifact = Path(path)
    if not artifact.is_file():
        raise FileNotFoundError(f"Artifact input is missing or not a file: {artifact}")
    return {
        "name": artifact.name,
        "size": artifact.stat().st_size,
        "sha256": sha256_file(artifact),
    }


def sanitize_command(command: Sequence[object]) -> list[str]:
    """Return a command suitable for metadata without obvious secret values."""

    redacted: list[str] = []
    redact_next = False
    secret_markers = ("password", "passwd", "secret", "token", "api-key", "api_key")
    for raw_part in command:
        part = str(raw_part)
        lowered = part.lower()
        if redact_next:
            redacted.append("<redacted>")
            redact_next = False
            continue
        if any(marker in lowered for marker in secret_markers):
            if "=" in part:
                redacted.append(part.split("=", 1)[0] + "=<redacted>")
            else:
                redacted.append(part)
                redact_next = True
            continue
        redacted.append(part)
    return redacted


def build_artifact_metadata(
    artifact_path: str | os.PathLike[str],
    *,
    artifact_kind: str,
    pipeline_run_id: str,
    dataset: str,
    model: str,
    architecture_mode: str,
    ordered_targets: Sequence[str],
    config_fingerprint: str,
    base_seed: int,
    dataset_seed: int,
    model_seed: int,
    effective_seed: int,
    producing_command: Sequence[object],
    schema: Mapping[str, Any],
    cohort_ids: Iterable[object],
    model_config: Mapping[str, Any],
    training_config: Mapping[str, Any],
    inputs: Mapping[str, Mapping[str, Any]],
    preprocessing_state: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = Path(artifact_path)
    descriptor = file_descriptor(artifact)
    model_config_value = dict(model_config)
    training_config_value = validate_training_config(dict(training_config))
    metadata: dict[str, Any] = {
        "metadata_schema_version": METADATA_SCHEMA_VERSION,
        "artifact_kind": artifact_kind,
        "artifact_name": artifact.name,
        "artifact_sha256": descriptor["sha256"],
        "artifact_size": descriptor["size"],
        "pipeline_run_id": str(pipeline_run_id),
        "dataset": str(dataset),
        "model": str(model),
        "architecture_mode": str(architecture_mode),
        "ordered_targets": [str(target) for target in ordered_targets],
        "config_fingerprint": str(config_fingerprint),
        "base_seed": int(base_seed),
        "dataset_seed": int(dataset_seed),
        "model_seed": int(model_seed),
        "effective_seed": int(effective_seed),
        "producing_command": sanitize_command(producing_command),
        "schema": dict(schema),
        "cohort": cohort_descriptor(cohort_ids),
        "model_config": model_config_value,
        "training_config": training_config_value,
        "scientific_config_fingerprint": scientific_config_fingerprint(
            model_config_value, training_config_value
        ),
        "inputs": {name: dict(value) for name, value in sorted(inputs.items())},
    }
    if preprocessing_state is not None:
        metadata["preprocessing_state"] = dict(preprocessing_state)
    return metadata


def write_metadata(
    artifact_path: str | os.PathLike[str],
    metadata: Mapping[str, Any],
) -> Path:
    destination = metadata_path_for(artifact_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        prefix=destination.name + ".",
        suffix=".tmp",
        dir=str(destination.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(dict(metadata), handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, destination)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise
    return destination


def load_metadata(artifact_path: str | os.PathLike[str]) -> dict[str, Any]:
    path = metadata_path_for(artifact_path)
    if not path.is_file():
        raise FileNotFoundError(f"Artifact metadata is missing: {path}")
    with path.open("r", encoding="utf-8") as handle:
        metadata = json.load(handle)
    if not isinstance(metadata, dict):
        raise ValueError(f"Artifact metadata must be a JSON object: {path}")
    return metadata


def _compare_expected(actual: Any, expected: Any, field_path: str) -> None:
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping):
            raise ValueError(f"Metadata field {field_path} must be an object.")
        for key, expected_value in expected.items():
            if key not in actual:
                raise ValueError(f"Metadata field {field_path}.{key} is missing.")
            _compare_expected(actual[key], expected_value, f"{field_path}.{key}")
        return
    if actual != expected:
        raise ValueError(
            f"Metadata mismatch for {field_path}: expected {expected!r}, got {actual!r}."
        )


def validate_artifact_metadata(
    artifact_path: str | os.PathLike[str],
    *,
    expected: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = Path(artifact_path)
    if not artifact.is_file():
        raise FileNotFoundError(f"Artifact is missing: {artifact}")
    metadata = load_metadata(artifact)
    missing_fields = sorted(REQUIRED_METADATA_FIELDS - set(metadata))
    if missing_fields:
        raise ValueError(f"Artifact metadata is missing required fields: {missing_fields}")
    if metadata["metadata_schema_version"] != METADATA_SCHEMA_VERSION:
        raise ValueError(
            "Unsupported artifact metadata schema version: "
            f"{metadata['metadata_schema_version']!r}"
        )
    descriptor = file_descriptor(artifact)
    if metadata["artifact_name"] != artifact.name:
        raise ValueError(
            f"Metadata artifact_name does not match {artifact.name!r}: "
            f"{metadata['artifact_name']!r}"
        )
    if metadata["artifact_sha256"] != descriptor["sha256"]:
        raise ValueError(f"Artifact digest does not match metadata: {artifact}")
    if metadata["artifact_size"] != descriptor["size"]:
        raise ValueError(f"Artifact size does not match metadata: {artifact}")
    validate_training_config(dict(metadata["training_config"]))
    expected_scientific_fingerprint = scientific_config_fingerprint(
        metadata["model_config"], metadata["training_config"]
    )
    if (
        metadata["scientific_config_fingerprint"]
        != expected_scientific_fingerprint
    ):
        raise ValueError(
            "Artifact scientific configuration fingerprint is inconsistent: "
            f"{artifact}"
        )
    if expected:
        for key, expected_value in expected.items():
            if key not in metadata:
                raise ValueError(f"Metadata field {key} is missing.")
            _compare_expected(metadata[key], expected_value, key)
    return metadata

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import pickle
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
import traceback
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


WORKSPACE_ROOT = Path(__file__).resolve().parent
THESIS_REPO_CANDIDATES = [WORKSPACE_ROOT / "causal-irregular-time-series", WORKSPACE_ROOT]
STRATS_REPO_CANDIDATES = [WORKSPACE_ROOT / "STraTS", WORKSPACE_ROOT.parent / "STraTS"]

STAGE_ORDER = [
    "preprocessing",
    "tagging",
    "trees",
    "prepare-strats",
    "run-strats",
    "collect-strats",
    "normalize-predictions",
    "thesis-main",
]
SUPPORTED_STAGES = set(STAGE_ORDER) | {"all"}
DATASETS = ("physionet", "mimic")
MODELS = ("strats", "gru", "grud", "tcn", "sand")
RUN_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
ID_TEXT_RE = re.compile(r"(?:0|[1-9][0-9]*)(?:[.]0+)?\Z")
ROUTER_PRODUCER_VERSION = "clinicause-router-static-contract-v3"
SENSITIVE_OPTIONS = {
    "--token",
    "--api-key",
    "--password",
    "--secret",
    "--coordinator-token",
}


@dataclass
class DatasetPaths:
    dataset: str
    thesis_dataset: str
    strats_dataset: str
    raw_data_path: Path | None
    run_dir: Path
    config_csv: Path
    resolved_config_csv: Path
    thesis_processed_pkl: Path
    thesis_input_pkl: Path
    rule_latent_tags_csv: Path
    rule_input_csv: Path
    rule_decision_trees_pkl: Path
    decision_trees_input_pkl: Path
    tree_plots_dir: Path
    strats_input_root: Path
    strats_processed_pkl: Path
    strats_latent_tags_csv: Path
    strats_output_root: Path
    strats_predictions_dir: Path
    predicted_raw_dir: Path
    voters_dir: Path
    voters_input_dir: Path
    thesis_main_output_dir: Path
    temporary_dir: Path
    logs_dir: Path
    config_dir: Path
    manifest_path: Path


@dataclass
class GPUAssignment:
    dataset: str
    requested: str | None
    physical: str | None
    child_visible: str | None
    lock_path: Path
    max_concurrent: int


@dataclass
class GPUPolicy:
    visible_devices: list[str] | None
    max_concurrent: int
    assignments: dict[str, GPUAssignment]


@dataclass
class RouterContext:
    run_id: str
    run_root: Path
    run_dir: Path
    thesis_repo_root: Path
    strats_repo_root: Path
    logs_dir: Path
    datasets: dict[str, DatasetPaths]
    args: argparse.Namespace
    manifest_path: Path
    config_dir: Path
    configs: dict[str, dict[str, Any]]
    config_fingerprints: dict[str, str]
    plan_fingerprint: str
    gpu_assignment: GPUAssignment | None = None


@dataclass
class StageResult:
    status: str = "completed"
    details: dict[str, Any] = field(default_factory=dict)


class CommandExecutionError(RuntimeError):
    def __init__(self, command: Sequence[str], returncode: int, log_path: Path):
        self.command = list(command)
        self.returncode = int(returncode)
        self.log_path = Path(log_path)
        super().__init__(
            f"Command failed with exit code {returncode}: {shlex.join(command)}; "
            f"log={log_path}"
        )


class CoordinatorInterrupted(RuntimeError):
    def __init__(self, signum: int):
        self.signum = int(signum)
        super().__init__(f"Coordinator received signal {signum}")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sanitize_command(command: Sequence[str]) -> list[str]:
    sanitized: list[str] = []
    redact_next = False
    for value in command:
        text = str(value)
        if redact_next:
            sanitized.append("<redacted>")
            redact_next = False
            continue
        option = text.split("=", 1)[0].lower()
        if option in SENSITIVE_OPTIONS:
            if "=" in text:
                sanitized.append(option + "=<redacted>")
            else:
                sanitized.append(text)
                redact_next = True
            continue
        sanitized.append(text)
    return sanitized


def parse_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "f", "no", "n", "off"}:
        return False
    raise argparse.ArgumentTypeError(f"Invalid boolean value: {value!r}")


def normalize_stage_list(stages: str | Iterable[str]) -> list[str]:
    if isinstance(stages, str):
        raw_parts = [part.strip().lower() for part in stages.split(",") if part.strip()]
    else:
        raw_parts = [str(part).strip().lower() for part in stages if str(part).strip()]
    if not raw_parts:
        raise ValueError("No stages were selected.")
    unknown = sorted(set(raw_parts) - SUPPORTED_STAGES)
    if unknown:
        raise ValueError(f"Unsupported stages {unknown}; expected one of {sorted(SUPPORTED_STAGES)}")
    if "all" in raw_parts:
        if len(raw_parts) != 1:
            raise ValueError("Stage selector 'all' cannot be combined with explicit stage names.")
        return list(STAGE_ORDER)
    selected = set(raw_parts)
    return [stage for stage in STAGE_ORDER if stage in selected]


def validate_run_id(run_id: str) -> str:
    value = str(run_id)
    if not RUN_ID_RE.fullmatch(value) or value in {".", ".."}:
        raise ValueError(
            "run-id must be one safe path component containing only letters, numbers, "
            "periods, underscores, and hyphens."
        )
    return value


def resolve_python_executable(value: str) -> str:
    """Return an absolute executable path before any child changes cwd."""

    candidate = Path(value).expanduser()
    if candidate.is_absolute() or candidate.parent != Path("."):
        resolved = candidate.resolve()
        if not resolved.is_file():
            raise FileNotFoundError(f"Python executable does not exist: {resolved}")
        return str(resolved)
    located = shutil.which(str(value))
    if located is None:
        raise FileNotFoundError(f"Python executable is not available on PATH: {value}")
    return str(Path(located).resolve())


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Orchestrate the thesis and STraTS pipeline.")
    parser.add_argument("--dataset", choices=["physionet", "mimic", "both"], default="both")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output-root", default="runs")
    parser.add_argument("--thesis-repo-root", default=None)
    parser.add_argument("--strats-repo-root", default=None)
    parser.add_argument("--strats-script-path", default="run_full_main.sh")
    parser.add_argument("--stages", default="all")
    parser.add_argument("--physionet-raw-data-path", default=None)
    parser.add_argument("--mimic-raw-data-path", default=None)
    parser.add_argument("--physionet-config-csv", default=None)
    parser.add_argument("--mimic-config-csv", default=None)
    parser.add_argument("--cate-model", choices=["CausalForest", "LinearDML", "CausalPFN"], default=None)
    parser.add_argument("--down-sample", default=None)
    parser.add_argument("--trials", type=int, default=None)
    parser.add_argument("--use-expanded-safe-confounders", default=None)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--fail-fast", action="store_true")
    parser.add_argument("--python-executable", default=sys.executable)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--allow-existing-strats-inputs", action="store_true")
    parser.add_argument("--run-strats", default=None, type=parse_bool)
    parser.add_argument("--preprocess-chunksize", type=int, default=500000)
    parser.add_argument("--tmp-dir", default=None)
    parser.add_argument("--strats-max-concurrent", type=int, default=None)
    parser.add_argument("--strats-train-frac", type=float, default=0.5)
    parser.add_argument("--strats-model-run", default="1o10")
    parser.add_argument("--physionet-gpu", default=None)
    parser.add_argument("--mimic-gpu", default=None)

    for dataset in DATASETS:
        parser.add_argument(f"--{dataset}-thesis-pkl", default=None)
        parser.add_argument(f"--{dataset}-rule-tags-csv", default=None)
        parser.add_argument(f"--{dataset}-decision-trees-pkl", default=None)
        parser.add_argument(f"--{dataset}-strats-input-dir", default=None)
        parser.add_argument(f"--{dataset}-strats-output-dir", default=None)
        parser.add_argument(f"--{dataset}-voters-dir", default=None)

    parser.add_argument("--dataset-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--dataset-run-dir", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--coordinator-run-root", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--parent-plan-fingerprint", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--assigned-gpu", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--gpu-lock-path", default=None, help=argparse.SUPPRESS)

    args = parser.parse_args(list(argv) if argv is not None else None)
    args.run_id = validate_run_id(args.run_id)
    args.stages = normalize_stage_list(args.stages)
    args.python_executable = resolve_python_executable(args.python_executable)
    if args.run_strats is None:
        args.run_strats = "run-strats" in args.stages
    if args.overwrite and args.resume:
        raise ValueError("--overwrite and --resume are mutually exclusive.")
    if args.skip_existing and not args.resume:
        raise ValueError("--skip-existing requires --resume so reuse is provenance-bound.")
    if args.resume and not args.skip_existing:
        raise ValueError("--resume requires --skip-existing to preserve immutable completed artifacts.")
    if args.dataset_child and args.dataset == "both":
        raise ValueError("An internal dataset child cannot coordinate dataset=both.")
    if not 0 <= args.seed < 2**31 - 1:
        raise ValueError("--seed must satisfy 0 <= seed < 2147483647.")
    if args.preprocess_chunksize <= 0:
        raise ValueError("--preprocess-chunksize must be positive.")
    if args.strats_max_concurrent is not None and args.strats_max_concurrent <= 0:
        raise ValueError("--strats-max-concurrent must be positive.")
    if not 0 < args.strats_train_frac <= 1:
        raise ValueError("--strats-train-frac must be in (0, 1].")
    run_match = re.fullmatch(r"([1-9][0-9]*)o([1-9][0-9]*)", args.strats_model_run)
    if run_match is None or int(run_match.group(1)) > int(run_match.group(2)):
        raise ValueError(
            "--strats-model-run must have form <run>o<total> with run <= total."
        )
    return args


def selected_datasets(args: argparse.Namespace) -> list[str]:
    return list(DATASETS) if args.dataset == "both" else [args.dataset]


def resolve_repo_root(explicit: str | None, candidates: Iterable[Path], expected_marker: str) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        if not (path / expected_marker).exists():
            raise FileNotFoundError(f"Expected {expected_marker} below repository root: {path}")
        return path
    for candidate in candidates:
        if (candidate / expected_marker).exists():
            return candidate.resolve()
    raise FileNotFoundError(f"Could not locate repository root containing {expected_marker!r}")


def resolve_optional_path(value: str | None) -> Path | None:
    if value is None or str(value).strip() == "":
        return None
    return Path(value).expanduser().resolve()


def resolve_dataset_raw_data_path(dataset: str, context: RouterContext) -> Path:
    paths = getattr(context, "datasets", {}).get(dataset)
    if paths is not None and hasattr(paths, "raw_data_path"):
        return paths.raw_data_path if paths.raw_data_path is not None else Path("")

    raw_value = getattr(context.args, f"{dataset}_raw_data_path", None)
    if raw_value in (None, "", ".", "./", ".\\"):
        return Path("")
    return Path(raw_value).expanduser().resolve()


def _stringify_value(value: Any) -> Any:
    if isinstance(value, (list, tuple, set)):
        return json.dumps(list(value))
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


CONFIG_FIELDS = [
    "PREFERRED_ENV_NAME",
    "SEED",
    "DATASET_NAME",
    "ID_COL",
    "ALT_ID_COL",
    "OUTCOME_COL",
    "GRAPH_OUTCOME_NODE",
    "TREATMENTS",
    "LATENT_ORDER",
    "BACKGROUND_FEATURE_COLUMNS",
    "EFFECT_MODIFIER_COLUMNS",
    "MODEL_TYPE",
    "TRIALS",
    "DOWN_SAMPLE",
    "USE_EXPANDED_SAFE_CONFOUNDERS",
    "SAVE_CONTOUR_PLOT",
    "MATCH_WITH_REPLACEMENT",
    "REQUIRE_BINARY_CONF",
]


def build_resolved_config_row(
    config: dict[str, Any],
    args: argparse.Namespace,
    dataset: str | None = None,
) -> dict[str, Any]:
    row = {key: config[key] for key in CONFIG_FIELDS if key in config}
    if args.cate_model is not None:
        row["MODEL_TYPE"] = args.cate_model
    if args.down_sample is not None:
        parsed = parse_bool(args.down_sample)
        row["DOWN_SAMPLE"] = parsed
    if args.trials is not None:
        row["TRIALS"] = args.trials
    if args.use_expanded_safe_confounders is not None:
        row["USE_EXPANDED_SAFE_CONFOUNDERS"] = parse_bool(args.use_expanded_safe_confounders)
    row["SEED"] = (
        derive_seed(args.seed, dataset, "causal") if dataset is not None else args.seed
    )
    return row


def write_resolved_config(
    path: Path,
    dataset: str,
    config: dict[str, Any],
    args: argparse.Namespace,
) -> None:
    row = build_resolved_config_row(config, args, dataset)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CONFIG_FIELDS)
        writer.writeheader()
        writer.writerow({key: _stringify_value(row.get(key)) for key in CONFIG_FIELDS})


def _load_dataset_config(
    thesis_repo_root: Path,
    dataset: str,
    explicit_path: str | None,
) -> tuple[Path, dict[str, Any]]:
    if str(thesis_repo_root) not in sys.path:
        sys.path.insert(0, str(thesis_repo_root))
    from src.dataset_config import default_config_path, load_dataset_config

    source = Path(explicit_path or default_config_path(dataset)).expanduser()
    if not source.is_absolute():
        source = (thesis_repo_root / source).resolve()
    else:
        source = source.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Dataset config not found for {dataset}: {source}")
    config = load_dataset_config(dataset, str(source))
    return source, config


def derive_seed(base_seed: int, dataset: str, component: str) -> int:
    payload = f"{int(base_seed)}|{dataset}|{component}".encode("utf-8")
    value = int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")
    return value % (2**31 - 1)


def build_context(args: argparse.Namespace, dataset: str) -> RouterContext:
    if dataset not in DATASETS:
        raise ValueError(f"Unsupported dataset {dataset!r}")
    thesis_root = resolve_repo_root(args.thesis_repo_root, THESIS_REPO_CANDIDATES, "main.py")
    strats_root = resolve_repo_root(args.strats_repo_root, STRATS_REPO_CANDIDATES, "run_full_main.sh")
    output_root = Path(args.output_root).expanduser().resolve()
    run_root = (output_root / args.run_id).resolve()
    if run_root.parent != output_root:
        raise ValueError(f"run-id escapes output-root: {run_root}")

    if args.dataset_child:
        if args.dataset_run_dir is None or args.coordinator_run_root is None:
            raise ValueError("Internal child requires explicit dataset and coordinator run roots.")
        coordinator_root = Path(args.coordinator_run_root).expanduser().resolve()
        run_dir = Path(args.dataset_run_dir).expanduser().resolve()
        if coordinator_root != run_root:
            raise ValueError("Internal coordinator root does not match output-root/run-id.")
        if run_dir.parent != run_root or run_dir.name != dataset:
            raise ValueError("Internal dataset run directory is outside its dataset subtree.")
    else:
        run_dir = run_root / dataset

    config_path, config = _load_dataset_config(
        thesis_root, dataset, getattr(args, f"{dataset}_config_csv", None)
    )
    config_row = build_resolved_config_row(config, args, dataset)
    config_fingerprint = stable_hash(config_row)

    raw_value = getattr(args, f"{dataset}_raw_data_path", None)
    resolved_raw = (
        None
        if raw_value in (None, "", ".", "./", ".\\")
        else Path(raw_value).expanduser().resolve()
    )

    local_thesis = run_dir / "preprocessing" / f"{dataset}_ts_oc_ids.pkl"
    explicit_thesis = resolve_optional_path(getattr(args, f"{dataset}_thesis_pkl", None))
    thesis_input = local_thesis if "preprocessing" in args.stages else (explicit_thesis or local_thesis)

    local_rule = run_dir / "tagging" / "rules" / "latent_tags.csv"
    explicit_rule = resolve_optional_path(getattr(args, f"{dataset}_rule_tags_csv", None))
    rule_input = local_rule if "tagging" in args.stages else (explicit_rule or local_rule)

    local_trees = run_dir / "tagging" / "rules" / "latent_decision_trees.pkl"
    explicit_trees = resolve_optional_path(getattr(args, f"{dataset}_decision_trees_pkl", None))
    trees_input = local_trees if "tagging" in args.stages else (explicit_trees or local_trees)

    local_strats_input = run_dir / "strats" / "inputs"
    explicit_strats_input = resolve_optional_path(getattr(args, f"{dataset}_strats_input_dir", None))
    strats_input = local_strats_input if "prepare-strats" in args.stages else (
        explicit_strats_input or local_strats_input
    )
    local_strats_output = run_dir / "strats" / "outputs"
    explicit_strats_output = resolve_optional_path(getattr(args, f"{dataset}_strats_output_dir", None))
    strats_output = local_strats_output if "run-strats" in args.stages else (
        explicit_strats_output or local_strats_output
    )
    local_voters = run_dir / "predictions" / "voters"
    explicit_voters = resolve_optional_path(getattr(args, f"{dataset}_voters_dir", None))
    voters_input = local_voters if "normalize-predictions" in args.stages else (
        explicit_voters or local_voters
    )

    strats_dataset = {"physionet": "physionet_2012", "mimic": "mimic_iii"}[dataset]
    paths = DatasetPaths(
        dataset=dataset,
        thesis_dataset=dataset,
        strats_dataset=strats_dataset,
        raw_data_path=resolved_raw,
        run_dir=run_dir,
        config_csv=config_path,
        resolved_config_csv=run_dir / "config" / "resolved_config.csv",
        thesis_processed_pkl=local_thesis,
        thesis_input_pkl=thesis_input,
        rule_latent_tags_csv=local_rule,
        rule_input_csv=rule_input,
        rule_decision_trees_pkl=local_trees,
        decision_trees_input_pkl=trees_input,
        tree_plots_dir=run_dir / "trees",
        strats_input_root=strats_input,
        strats_processed_pkl=strats_input / "processed" / f"{strats_dataset}.pkl",
        strats_latent_tags_csv=strats_input / f"{dataset}_latent_tags.csv",
        strats_output_root=strats_output,
        strats_predictions_dir=strats_output / "predictions",
        predicted_raw_dir=run_dir / "predictions" / "raw",
        voters_dir=local_voters,
        voters_input_dir=voters_input,
        thesis_main_output_dir=run_dir / "causal",
        temporary_dir=run_dir / "temporary",
        logs_dir=run_dir / "logs",
        config_dir=run_dir / "config",
        manifest_path=run_dir / "manifest.json",
    )

    plan_payload = {
        "contract": ROUTER_PRODUCER_VERSION,
        "run_id": args.run_id,
        "dataset": dataset,
            "strats_train_frac": args.strats_train_frac,
            "strats_model_run": args.strats_model_run,
        "stages": args.stages,
        "config_fingerprint": config_fingerprint,
        "seed": args.seed,
        "scientific_overrides": {
            "cate_model": args.cate_model,
            "down_sample": args.down_sample,
            "trials": args.trials,
            "expanded": args.use_expanded_safe_confounders,
            "run_strats": args.run_strats,
        },
        "source_paths": {
            "config": str(config_path),
            "raw": str(resolved_raw),
            "thesis": str(thesis_input),
            "rules": str(rule_input),
            "strats_input": str(strats_input),
            "strats_output": str(strats_output),
            "voters": str(voters_input),
        },
    }
    return RouterContext(
        run_id=args.run_id,
        run_root=run_root,
        run_dir=run_dir,
        thesis_repo_root=thesis_root,
        strats_repo_root=strats_root,
        logs_dir=paths.logs_dir,
        datasets={dataset: paths},
        args=args,
        manifest_path=paths.manifest_path,
        config_dir=paths.config_dir,
        configs={dataset: config},
        config_fingerprints={dataset: config_fingerprint},
        plan_fingerprint=stable_hash(plan_payload),
    )


def initialize_context(args: argparse.Namespace) -> RouterContext:
    datasets = selected_datasets(args)
    if len(datasets) != 1:
        raise ValueError("dataset=both is coordinator-only; build one context per child.")
    return build_context(args, datasets[0])


def _parse_visible_devices(environ: dict[str, str]) -> list[str] | None:
    if "CUDA_VISIBLE_DEVICES" not in environ:
        return None
    raw = environ.get("CUDA_VISIBLE_DEVICES", "")
    if raw.strip() in {"", "-1", "NoDevFiles"}:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def _validate_gpu_token(value: str | None, option: str) -> str | None:
    if value is None:
        return None
    token = str(value).strip()
    if not token or "," in token or any(char.isspace() for char in token):
        raise ValueError(f"{option} must identify exactly one GPU device.")
    if not re.fullmatch(r"[A-Za-z0-9_.:-]+", token):
        raise ValueError(f"{option} contains unsupported characters: {token!r}")
    return token


def resolve_gpu_policy(
    args: argparse.Namespace,
    datasets: Sequence[str],
    environ: dict[str, str] | None = None,
    run_root: Path | None = None,
) -> GPUPolicy:
    environ = dict(os.environ if environ is None else environ)
    visible = _parse_visible_devices(environ)
    requested = {
        dataset: _validate_gpu_token(getattr(args, f"{dataset}_gpu", None), f"--{dataset}-gpu")
        for dataset in datasets
    }
    explicit = [requested[dataset] is not None for dataset in datasets]
    if len(datasets) == 2 and any(explicit) and not all(explicit):
        raise ValueError("Both dataset GPU assignments must be explicit when either is provided.")
    if len(datasets) == 2 and all(explicit) and requested[datasets[0]] == requested[datasets[1]]:
        raise ValueError("PhysioNet and MIMIC cannot be assigned the same explicit GPU.")

    physical: dict[str, str | None] = {}
    if all(explicit):
        for dataset in datasets:
            physical[dataset] = requested[dataset]
    elif visible:
        if len(datasets) == 2 and len(visible) >= 2:
            physical = {datasets[0]: visible[0], datasets[1]: visible[1]}
        else:
            physical = {dataset: visible[0] for dataset in datasets}
    else:
        physical = {dataset: None for dataset in datasets}

    if visible is not None:
        unavailable = [
            device for device in physical.values()
            if device is not None and device not in visible
        ]
        if unavailable:
            raise ValueError(
                f"Requested GPU assignments are not visible: {sorted(set(unavailable))}; "
                f"visible={visible}"
            )

    env_max = environ.get("STRATS_MAX_CONCURRENT")
    if args.strats_max_concurrent is not None:
        max_concurrent = args.strats_max_concurrent
    elif env_max is not None:
        try:
            max_concurrent = int(env_max)
        except ValueError as exc:
            raise ValueError("STRATS_MAX_CONCURRENT must be an integer.") from exc
    elif len(set(physical.values())) == len(datasets) and None not in physical.values():
        max_concurrent = len(datasets)
    else:
        max_concurrent = 1
    if max_concurrent <= 0:
        raise ValueError("STRATS_MAX_CONCURRENT must be positive.")
    if max_concurrent > 1 and len(datasets) > 1:
        assigned = list(physical.values())
        if None in assigned or len(set(assigned)) != len(assigned):
            raise ValueError(
                "Concurrent STraTS stages require unique explicit or visible GPU assignments."
            )

    run_root = run_root or (Path(args.output_root).expanduser().resolve() / args.run_id)
    lock_root = run_root / "coordinator" / "gpu_locks"
    assignments: dict[str, GPUAssignment] = {}
    for dataset in datasets:
        lock_name = "global.lock" if max_concurrent == 1 else (
            "gpu-" + re.sub(r"[^A-Za-z0-9_.-]", "_", str(physical[dataset])) + ".lock"
        )
        assignments[dataset] = GPUAssignment(
            dataset=dataset,
            requested=requested[dataset],
            physical=physical[dataset],
            child_visible="0" if physical[dataset] is not None else None,
            lock_path=lock_root / lock_name,
            max_concurrent=max_concurrent,
        )
    return GPUPolicy(visible_devices=visible, max_concurrent=max_concurrent, assignments=assignments)


def _explicit_or_resume(args: argparse.Namespace, value: str | None, local_path: Path) -> bool:
    return value is not None or (args.resume and local_path.exists())


def _require_existing(path: Path, description: str, kind: str = "file") -> None:
    if kind == "file" and not path.is_file():
        raise FileNotFoundError(f"{description} is missing or not a file: {path}")
    if kind == "dir" and not path.is_dir():
        raise FileNotFoundError(f"{description} is missing or not a directory: {path}")


def validate_stage_dependencies(context: RouterContext) -> None:
    args = context.args
    dataset, paths = next(iter(context.datasets.items()))
    selected = set(args.stages)

    if "preprocessing" in selected:
        raw = resolve_dataset_raw_data_path(dataset, context)
        if raw == Path("") or not raw.is_dir():
            raise FileNotFoundError(
                f"Raw data path for {dataset} is required and must exist for preprocessing: {raw}"
            )

    has_thesis = "preprocessing" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_thesis_pkl"), paths.thesis_input_pkl
    )
    has_rules = "tagging" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_rule_tags_csv"), paths.rule_input_csv
    )
    has_trees = "tagging" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_decision_trees_pkl"), paths.decision_trees_input_pkl
    )
    has_strats_input = "prepare-strats" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_strats_input_dir"), paths.strats_input_root
    )
    has_strats_output = "run-strats" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_strats_output_dir"), paths.strats_output_root
    )
    has_voters = "normalize-predictions" in selected or _explicit_or_resume(
        args, getattr(args, f"{dataset}_voters_dir"), paths.voters_input_dir
    )

    failures: list[str] = []
    if "tagging" in selected and not has_thesis:
        failures.append("tagging requires preprocessing or an explicit thesis pickle")
    if "trees" in selected and not has_trees:
        failures.append("trees requires tagging or an explicit decision-tree pickle")
    if "prepare-strats" in selected and not (has_thesis and has_rules):
        failures.append("prepare-strats requires canonical data and rule tags")
    if "run-strats" in selected and not has_strats_input:
        failures.append("run-strats requires prepare-strats or an explicit STraTS input directory")
    if "run-strats" in selected and args.run_strats is False:
        failures.append("run-strats was selected while --run-strats false was requested")
    if "collect-strats" in selected and not has_strats_output:
        failures.append(
            "collect-strats requires run-strats or an explicit STraTS output directory"
        )
    if "collect-strats" in selected and not (has_thesis or has_strats_input):
        failures.append(
            "collect-strats requires an explicit trusted thesis or STraTS input cohort"
        )
    if "normalize-predictions" in selected and not (has_thesis and has_rules and has_strats_output):
        failures.append("normalize-predictions requires canonical data, rule tags, and STraTS predictions")
    if "thesis-main" in selected and not (has_thesis and has_voters):
        failures.append("thesis-main requires canonical data and normalized voters")
    if failures:
        raise ValueError("Invalid stage subset: " + "; ".join(failures))

    explicit_file_checks = [
        (getattr(args, f"{dataset}_thesis_pkl"), paths.thesis_input_pkl, "thesis pickle"),
        (getattr(args, f"{dataset}_rule_tags_csv"), paths.rule_input_csv, "rule tags"),
        (
            getattr(args, f"{dataset}_decision_trees_pkl"),
            paths.decision_trees_input_pkl,
            "decision-tree pickle",
        ),
    ]
    for raw_value, path, description in explicit_file_checks:
        if raw_value is not None:
            _require_existing(path, f"Explicit {description}")
    for raw_value, path, description in [
        (getattr(args, f"{dataset}_strats_input_dir"), paths.strats_input_root, "STraTS input"),
        (getattr(args, f"{dataset}_strats_output_dir"), paths.strats_output_root, "STraTS output"),
        (getattr(args, f"{dataset}_voters_dir"), paths.voters_input_dir, "voters"),
    ]:
        if raw_value is not None:
            _require_existing(path, f"Explicit {description} directory", kind="dir")


def validate_thesis_input(context: RouterContext) -> list[str]:
    dataset, paths = next(iter(context.datasets.items()))
    valid, reason = validate_thesis_pickle(
        paths.thesis_input_pkl, dataset, paths.resolved_config_csv
    )
    if not valid:
        raise ValueError(f"Invalid canonical thesis input: {reason}")
    cohort = _expected_cohort_from_thesis(paths.thesis_input_pkl)
    validate_artifact_record(
        paths.thesis_input_pkl,
        {
            **_reuse_expected(context, "preprocessing"),
            "schema": ["ts", "oc", "ts_ids"],
            "cohort_size": len(cohort),
            "cohort_fingerprint": stable_hash(sorted(cohort)),
        },
    )
    return cohort


def _require_exact_columns(frame: Any, expected: Sequence[str], source: str) -> None:
    actual = [str(column) for column in frame.columns]
    expected_list = list(expected)
    if actual != expected_list:
        raise ValueError(
            f"Exact column order mismatch in {source}: "
            f"expected={expected_list!r} actual={actual!r}"
        )


def validate_rule_input(
    context: RouterContext, expected_ids: Sequence[str] | None = None
) -> list[str]:
    import pandas as pd

    dataset, paths = next(iter(context.datasets.items()))
    cohort = list(expected_ids) if expected_ids is not None else validate_thesis_input(context)
    if not cohort:
        raise ValueError("Rule inputs require a nonempty trusted thesis cohort.")
    latent_order = _latent_order(context, dataset)
    expected_columns = ["ts_id", *latent_order]
    frame = pd.read_csv(paths.rule_input_csv, dtype={"ts_id": "string"})
    _require_exact_columns(frame, expected_columns, str(paths.rule_input_csv))
    validated = validate_prediction_frame(
        frame,
        latent_order,
        cohort,
        str(paths.rule_input_csv),
        require_probabilities=False,
    )
    validate_artifact_record(
        paths.rule_input_csv,
        {
            **_reuse_expected(context, "tagging"),
            "schema": expected_columns,
            "input_fingerprints": {
                "thesis": file_sha256(paths.thesis_input_pkl)
            },
            "cohort_size": len(cohort),
            "cohort_fingerprint": stable_hash(sorted(cohort)),
        },
    )
    return validated["ts_id"].tolist()


def _available_tree_cohort(
    context: RouterContext, expected_ids: Sequence[str] | None
) -> list[str] | None:
    if expected_ids is not None:
        return list(expected_ids)
    dataset, paths = next(iter(context.datasets.items()))
    thesis_is_explicit = getattr(context.args, f"{dataset}_thesis_pkl", None) is not None
    thesis_is_produced = bool(
        {"preprocessing", "tagging"} & set(context.args.stages)
    )
    if thesis_is_explicit or (thesis_is_produced and paths.thesis_input_pkl.is_file()):
        return validate_thesis_input(context)
    return None


def validate_tree_input(
    context: RouterContext, expected_ids: Sequence[str] | None = None
) -> None:
    paths = next(iter(context.datasets.values()))
    cohort = _available_tree_cohort(context, expected_ids)
    expected: dict[str, Any] = {
        **_reuse_expected(context, "tagging"),
        "schema": ["latent_decision_trees"],
    }
    if cohort is not None:
        if not cohort:
            raise ValueError("Decision-tree inputs require a nonempty trusted cohort.")
        expected.update(
            {
                "cohort_size": len(cohort),
                "cohort_fingerprint": stable_hash(sorted(cohort)),
            }
        )
    metadata = validate_artifact_record(paths.decision_trees_input_pkl, expected)
    cohort_size = metadata.get("cohort_size")
    if isinstance(cohort_size, bool) or not isinstance(cohort_size, int) or cohort_size <= 0:
        raise ValueError("Decision-tree metadata must bind a nonempty cohort.")
    cohort_fingerprint = metadata.get("cohort_fingerprint")
    if not isinstance(cohort_fingerprint, str) or re.fullmatch(
        r"[0-9a-f]{64}", cohort_fingerprint
    ) is None:
        raise ValueError("Decision-tree metadata has an invalid cohort fingerprint.")
    input_fingerprints = metadata.get("input_fingerprints")
    if not isinstance(input_fingerprints, dict) or not input_fingerprints:
        raise ValueError("Decision-tree metadata has no bound upstream input.")
    invalid_inputs = {
        name: digest
        for name, digest in input_fingerprints.items()
        if not isinstance(name, str)
        or not name
        or not isinstance(digest, str)
        or re.fullmatch(r"[0-9a-f]{64}", digest) is None
    }
    if invalid_inputs:
        raise ValueError(
            f"Decision-tree metadata has invalid input fingerprints: {invalid_inputs}"
        )


def validate_voter_inputs(context: RouterContext) -> list[str]:
    import pandas as pd

    dataset, paths = next(iter(context.datasets.items()))
    expected_ids = validate_thesis_input(context)
    if not expected_ids:
        raise ValueError("Voter inputs require a nonempty trusted thesis cohort.")
    latent_order = _latent_order(context, dataset)
    expected_columns = ["ts_id", *latent_order]
    models = ("rules", *MODELS)
    expected_names = {
        name
        for model in models
        for name in (
            f"{model}.csv",
            f"{model}.csv.provenance.json",
        )
    }
    downstream_output = (
        paths.thesis_main_output_dir
        / "majority_vote"
        / "latent_tags_majority_vote.csv"
    ).resolve()
    actual_names: set[str] = set()
    for child in paths.voters_input_dir.iterdir():
        if not child.is_file() or child.name.startswith("."):
            continue
        if child.resolve() == downstream_output:
            continue
        if child.suffix.lower() == ".csv" or child.name.endswith(
            ".csv.provenance.json"
        ):
            actual_names.add(child.name)
    if actual_names != expected_names:
        raise ValueError(
            "Voter artifact set mismatch: "
            f"missing={sorted(expected_names - actual_names)} "
            f"extra={sorted(actual_names - expected_names)}"
        )
    for model in models:
        voter = paths.voters_input_dir / f"{model}.csv"
        frame = pd.read_csv(voter, dtype={"ts_id": "string"})
        _require_exact_columns(frame, expected_columns, str(voter))
        validate_prediction_frame(
            frame,
            latent_order,
            expected_ids,
            str(voter),
            require_probabilities=False,
        )
        metadata = validate_artifact_record(
            voter,
            {
                **_reuse_expected(context, "normalize-predictions"),
                "schema": expected_columns,
                "model": model,
                "targets": list(latent_order),
                "cohort_size": len(expected_ids),
                "cohort_fingerprint": stable_hash(sorted(expected_ids)),
            },
        )
        if not metadata["input_fingerprints"]:
            raise ValueError(f"Voter metadata has no bound source input: {voter}")
    return expected_ids

def validate_context(context: RouterContext) -> None:
    dataset, paths = next(iter(context.datasets.items()))
    if not paths.config_csv.is_file():
        raise FileNotFoundError(f"Source config missing: {paths.config_csv}")
    selected = set(context.args.stages)
    if "preprocessing" in selected:
        script = (
            "preprocess_physionet_2012.py"
            if dataset == "physionet"
            else "preprocess_mimic_iii_large.py"
        )
        _require_existing(
            context.thesis_repo_root / "src" / script,
            "Preprocessing script",
        )
    if "tagging" in selected:
        script = (
            "tagging_latent_variables_physionet.py"
            if dataset == "physionet"
            else "tagging_latent_variables_mimiciii.py"
        )
        _require_existing(
            context.thesis_repo_root / "src" / script,
            "Tagging script",
        )
    if "trees" in selected:
        _require_existing(
            context.thesis_repo_root / "src" / "decision_trees_plot.py",
            "Decision-tree plotting script",
        )
    if "thesis-main" in selected:
        _require_existing(context.thesis_repo_root / "main.py", "Causal repository main")
    if "run-strats" in selected:
        script_path = Path(context.args.strats_script_path)
        if not script_path.is_absolute():
            script_path = context.strats_repo_root / script_path
        _require_existing(script_path.resolve(), "STraTS runner")

    validate_stage_dependencies(context)

    trusted_thesis_ids: list[str] | None = None
    needs_existing_thesis = (
        "preprocessing" not in selected
        and bool(
            selected
            & {
                "tagging",
                "prepare-strats",
                "normalize-predictions",
                "thesis-main",
            }
        )
    )
    collect_uses_thesis = (
        "collect-strats" in selected
        and "run-strats" not in selected
        and not paths.strats_processed_pkl.is_file()
    )
    if needs_existing_thesis or collect_uses_thesis:
        trusted_thesis_ids = validate_thesis_input(context)

    if (
        selected & {"prepare-strats", "normalize-predictions"}
        and "tagging" not in selected
    ):
        validate_rule_input(context, trusted_thesis_ids)
    if "trees" in selected and "tagging" not in selected:
        validate_tree_input(context, trusted_thesis_ids)

    external_strats_input = should_validate_existing_strats_inputs(context) or (
        "collect-strats" in selected
        and "run-strats" not in selected
        and paths.strats_processed_pkl.is_file()
    )
    if external_strats_input:
        validate_strats_inputs(context)

    if (
        selected & {"collect-strats", "normalize-predictions"}
        and "run-strats" not in selected
    ):
        for model in MODELS:
            validate_strats_prediction_metadata(
                paths.strats_predictions_dir / f"{model}.csv",
                context,
                model,
            )

    if "thesis-main" in selected and "normalize-predictions" not in selected:
        validate_voter_inputs(context)


def coordinator_fingerprint(
    contexts: dict[str, RouterContext],
    policy: GPUPolicy,
) -> str:
    return stable_hash(
        {
            "contract": ROUTER_PRODUCER_VERSION,
            "children": {
                dataset: context.plan_fingerprint
                for dataset, context in sorted(contexts.items())
            },
            "gpu": {
                "max_concurrent": policy.max_concurrent,
                "assignments": {
                    dataset: assignment.physical
                    for dataset, assignment in sorted(policy.assignments.items())
                },
            },
        }
    )


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Invalid JSON evidence at {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object at {path}")
    return payload


def validate_run_collision(
    args: argparse.Namespace,
    contexts: dict[str, RouterContext],
    fingerprint: str,
) -> None:
    run_root = next(iter(contexts.values())).run_root
    if args.dataset_child:
        if os.environ.get("CLINICAUSE_DATASET_CHILD") != "1":
            raise ValueError("Internal child marker is not authorized by a coordinator environment.")
        if args.parent_plan_fingerprint != next(iter(contexts.values())).plan_fingerprint:
            raise ValueError("Internal child plan fingerprint does not match its coordinator command.")
        context = next(iter(contexts.values()))
        if context.run_dir.exists() and not args.resume:
            raise FileExistsError(f"Dataset run directory already exists: {context.run_dir}")
        if args.resume:
            manifest = _load_json(context.manifest_path)
            if manifest.get("plan_fingerprint") != context.plan_fingerprint:
                raise ValueError("Resume refused: dataset plan fingerprint mismatch.")
        return

    if not run_root.exists():
        if args.resume:
            raise FileNotFoundError(f"Cannot resume missing run root: {run_root}")
        return
    if args.overwrite:
        return
    if not args.resume:
        raise FileExistsError(
            f"Run ID already exists and is immutable by default: {run_root}. "
            "Use a new run ID, or explicit --resume/--overwrite."
        )

    if args.dataset == "both":
        manifest_path = run_root / "coordinator" / "manifest.json"
        manifest = _load_json(manifest_path)
        if manifest.get("plan_fingerprint") != fingerprint:
            raise ValueError("Resume refused: coordinator plan fingerprint mismatch.")
        for dataset, context in contexts.items():
            child_manifest = _load_json(context.manifest_path)
            if child_manifest.get("plan_fingerprint") != context.plan_fingerprint:
                raise ValueError(
                    "Resume refused before child launch: "
                    f"{dataset} plan fingerprint mismatch."
                )
    else:
        context = next(iter(contexts.values()))
        manifest = _load_json(context.manifest_path)
        if manifest.get("plan_fingerprint") != context.plan_fingerprint:
            raise ValueError("Resume refused: dataset plan fingerprint mismatch.")


def preflight(args: argparse.Namespace) -> tuple[dict[str, RouterContext], GPUPolicy, str]:
    contexts = {dataset: build_context(args, dataset) for dataset in selected_datasets(args)}
    for context in contexts.values():
        validate_context(context)
    run_root = next(iter(contexts.values())).run_root
    policy = resolve_gpu_policy(args, list(contexts), run_root=run_root)
    if args.dataset_child:
        dataset = next(iter(contexts))
        assignment = policy.assignments[dataset]
        if args.assigned_gpu is not None:
            if assignment.physical != args.assigned_gpu:
                raise ValueError("Child GPU environment does not match coordinator assignment.")
            assignment.requested = args.assigned_gpu
            assignment.child_visible = "0"
        if args.gpu_lock_path is not None:
            expected_lock = Path(args.gpu_lock_path).expanduser().resolve()
            if expected_lock != assignment.lock_path.resolve():
                raise ValueError("Child GPU lock path does not match coordinator policy.")
            assignment.lock_path = expected_lock
    for dataset, context in contexts.items():
        context.gpu_assignment = policy.assignments[dataset]
    fingerprint = coordinator_fingerprint(contexts, policy)
    validate_run_collision(args, contexts, fingerprint)
    return contexts, policy, fingerprint


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def maybe_remove(path: Path) -> None:
    if path.exists():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, default=str)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def build_stage_log_path(run_dir: Path, stage_name: str, dataset: str | None = None) -> Path:
    suffix = f"_{dataset}" if dataset else ""
    return run_dir / "logs" / f"{stage_name}{suffix}.log"


def _manifest_args(args: argparse.Namespace) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in vars(args).items():
        if "token" in key or "password" in key or "secret" in key:
            result[key] = "<redacted>"
        else:
            result[key] = value
    return result


def _gpu_payload(assignment: GPUAssignment | None) -> dict[str, Any]:
    if assignment is None:
        return {}
    return {
        "requested_gpu": assignment.requested,
        "assigned_physical_gpu": assignment.physical,
        "child_visible_gpu": assignment.child_visible,
        "max_concurrent": assignment.max_concurrent,
        "lock_path": str(assignment.lock_path),
        "permit_wait_start": None,
        "permit_acquired_at": None,
        "strats_start": None,
        "strats_finish": None,
        "permit_released_at": None,
        "strats_exit_code": None,
        "failure_reason": None,
    }


def reserve_top_level_root(args: argparse.Namespace, run_root: Path) -> None:
    if args.overwrite and run_root.exists():
        maybe_remove(run_root)
    if args.resume:
        return
    run_root.parent.mkdir(parents=True, exist_ok=True)
    run_root.mkdir(exist_ok=False)


def create_run_dirs(context: RouterContext) -> None:
    paths = next(iter(context.datasets.values()))
    if not context.args.resume:
        context.run_dir.mkdir(exist_ok=False)
    for directory in [
        paths.config_dir,
        paths.logs_dir,
        paths.thesis_processed_pkl.parent,
        paths.rule_latent_tags_csv.parent,
        paths.tree_plots_dir,
        context.run_dir / "strats" / "inputs" / "processed",
        context.run_dir / "strats" / "outputs" / "models",
        context.run_dir / "strats" / "outputs" / "predictions",
        paths.predicted_raw_dir,
        paths.voters_dir,
        paths.thesis_main_output_dir,
        paths.temporary_dir,
    ]:
        ensure_directory(directory)


def initialize_dataset_run(context: RouterContext) -> None:
    dataset, paths = next(iter(context.datasets.items()))
    create_run_dirs(context)
    if not context.args.resume:
        write_resolved_config(
            paths.resolved_config_csv,
            dataset,
            context.configs[dataset],
            context.args,
        )
        write_json(paths.config_dir / "router_args.json", _manifest_args(context.args))
        manifest = {
            "kind": "dataset",
            "dataset": dataset,
            "run_id": context.run_id,
            "pid": os.getpid(),
            "plan_fingerprint": context.plan_fingerprint,
            "config_fingerprint": context.config_fingerprints[dataset],
            "base_seed": context.args.seed,
            "derived_seeds": {
                "adapter": derive_seed(context.args.seed, dataset, "adapter"),
                "causal": derive_seed(context.args.seed, dataset, "causal"),
                "strats_dataset": derive_strats_dataset_seed(
                    context.args.seed, dataset
                ),
                **{
                    f"strats_{model}": derive_strats_model_seed(
                        context.args.seed, dataset, model
                    )
                    for model in MODELS
                },
            },
            "status": "running",
            "start_time": utc_now(),
            "finish_time": None,
            "run_path": str(context.run_dir),
            "manifest_path": str(context.manifest_path),
            "logs_path": str(context.logs_dir),
            "gpu": _gpu_payload(context.gpu_assignment),
            "stages": {
                stage: {
                    "status": "pending",
                    "command": None,
                    "inputs": [],
                    "outputs": [],
                    "start_time": None,
                    "finish_time": None,
                    "failure_summary": None,
                }
                for stage in context.args.stages
            },
            "failure_summary": None,
        }
        write_json(context.manifest_path, manifest)


def update_dataset_manifest(
    context: RouterContext,
    *,
    stage: str | None = None,
    status: str | None = None,
    details: dict[str, Any] | None = None,
    overall_status: str | None = None,
    failure_summary: str | None = None,
) -> None:
    manifest = _load_json(context.manifest_path)
    if stage is not None:
        record = manifest.setdefault("stages", {}).setdefault(stage, {})
        if status is not None:
            record["status"] = status
        if details:
            record.update(details)
        if status == "running" and record.get("start_time") is None:
            record["start_time"] = utc_now()
        if status in {"completed", "failed", "skipped", "cancelled"}:
            record["finish_time"] = utc_now()
    if overall_status is not None:
        manifest["status"] = overall_status
        if overall_status in {"completed", "failed", "cancelled"}:
            manifest["finish_time"] = utc_now()
    if failure_summary is not None:
        manifest["failure_summary"] = failure_summary
    write_json(context.manifest_path, manifest)


def update_gpu_manifest(context: RouterContext, **fields: Any) -> None:
    manifest = _load_json(context.manifest_path)
    manifest.setdefault("gpu", {}).update(fields)
    write_json(context.manifest_path, manifest)


def initialize_coordinator(
    args: argparse.Namespace,
    contexts: dict[str, RouterContext],
    policy: GPUPolicy,
    fingerprint: str,
) -> Path:
    run_root = next(iter(contexts.values())).run_root
    coordinator_dir = run_root / "coordinator"
    ensure_directory(coordinator_dir / "logs")
    manifest_path = coordinator_dir / "manifest.json"
    if args.resume:
        manifest = _load_json(manifest_path)
        manifest["overall_status"] = "running"
        manifest["finish_time"] = None
    else:
        manifest = {
            "kind": "coordinator",
            "run_id": args.run_id,
            "mode": "parallel-dataset-processes",
            "requested_datasets": list(contexts),
            "coordinator_pid": os.getpid(),
            "plan_fingerprint": fingerprint,
            "base_seed": args.seed,
            "start_time": utc_now(),
            "finish_time": None,
            "overall_status": "running",
            "gpu_policy": {
                "visible_devices": policy.visible_devices,
                "max_concurrent": policy.max_concurrent,
                "assignments": {
                    dataset: _gpu_payload(policy.assignments[dataset])
                    for dataset in contexts
                },
            },
            "children": {
                dataset: {
                    "dataset": dataset,
                    "pid": None,
                    "command": None,
                    "start_time": None,
                    "finish_time": None,
                    "exit_code": None,
                    "status": "pending",
                    "run_path": str(context.run_dir),
                    "manifest_path": str(context.manifest_path),
                    "log_paths": {
                        "coordinator": str(coordinator_dir / "logs" / f"{dataset}.log"),
                        "dataset": str(context.logs_dir),
                    },
                    "stage_statuses": {},
                    "gpu": _gpu_payload(policy.assignments[dataset]),
                    "failure_summary": None,
                }
                for dataset, context in contexts.items()
            },
        }
    write_json(manifest_path, manifest)
    return manifest_path


def update_coordinator_child(
    manifest_path: Path,
    dataset: str,
    status: str,
    **fields: Any,
) -> None:
    manifest = _load_json(manifest_path)
    child = manifest["children"][dataset]
    child["status"] = status
    child.update(fields)
    if status in {"completed", "failed", "cancelled"}:
        child["finish_time"] = utc_now()
    write_json(manifest_path, manifest)


def finalize_coordinator(manifest_path: Path, status: str) -> None:
    manifest = _load_json(manifest_path)
    manifest["overall_status"] = status
    manifest["finish_time"] = utc_now()
    write_json(manifest_path, manifest)


def artifact_metadata_path(path: Path) -> Path:
    return Path(str(path) + ".provenance.json")


def write_artifact_record(
    path: Path,
    context: RouterContext,
    stage: str,
    *,
    schema: Any,
    inputs: dict[str, str] | None = None,
    model: str | None = None,
    targets: list[str] | None = None,
    cohort: Sequence[str] | None = None,
    seed: int | None = None,
    command: Sequence[str] | None = None,
) -> Path:
    dataset = next(iter(context.datasets))
    cohort_list = list(cohort or [])
    metadata = {
        "artifact": str(path.resolve()),
        "artifact_sha256": file_sha256(path),
        "run_id": context.run_id,
        "dataset": dataset,
        "producing_stage": stage,
        "producer_version": ROUTER_PRODUCER_VERSION,
        "config_fingerprint": context.config_fingerprints[dataset],
        "input_fingerprints": inputs or {},
        "schema": schema,
        "model": model,
        "targets": targets or [],
        "seed": context.args.seed if seed is None else seed,
        "producing_command": sanitize_command(command or []),
        "cohort_size": len(cohort_list),
        "cohort_fingerprint": stable_hash(sorted(cohort_list)),
        "created_at": utc_now(),
    }
    metadata_path = artifact_metadata_path(path)
    write_json(metadata_path, metadata)
    return metadata_path


def validate_artifact_record(
    path: Path,
    expected: dict[str, Any],
    metadata_path: Path | None = None,
) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Artifact is missing: {path}")
    metadata_path = metadata_path or artifact_metadata_path(path)
    metadata = _load_json(metadata_path)
    required = {
        "artifact_sha256",
        "run_id",
        "dataset",
        "producing_stage",
        "producer_version",
        "config_fingerprint",
        "input_fingerprints",
        "schema",
        "model",
        "targets",
        "seed",
        "cohort_size",
        "cohort_fingerprint",
    }
    missing = sorted(required - set(metadata))
    if missing:
        raise ValueError(f"Artifact metadata missing required fields {missing}: {metadata_path}")
    actual_digest = file_sha256(path)
    if metadata["artifact_sha256"] != actual_digest:
        raise ValueError(f"Artifact digest mismatch: {path}")
    mismatches = {
        key: (metadata.get(key), value)
        for key, value in expected.items()
        if value is not None and metadata.get(key) != value
    }
    if mismatches:
        raise ValueError(f"Artifact provenance mismatch for {path}: {mismatches}")
    return metadata


def _canonicalize_identifier(value: Any, label: str = "identifier") -> str:
    if isinstance(value, bool):
        raise ValueError(f"{label} cannot be boolean: {value!r}")
    if value is None:
        raise ValueError(f"{label} cannot be missing.")
    try:
        import pandas as pd

        if pd.isna(value):
            raise ValueError(f"{label} cannot be missing.")
    except TypeError:
        pass
    if isinstance(value, int):
        if value < 0:
            raise ValueError(f"{label} cannot be negative: {value!r}")
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value) or not value.is_integer() or abs(value) > 2**53 - 1:
            raise ValueError(f"{label} must be a finite exact integer: {value!r}")
        if value < 0:
            raise ValueError(f"{label} cannot be negative: {value!r}")
        if value == 0 and math.copysign(1.0, value) < 0:
            raise ValueError(f"{label} cannot be negative zero: {value!r}")
        return str(int(value))
    text = str(value)
    if text != text.strip():
        raise ValueError(f"{label} cannot contain surrounding whitespace: {value!r}")
    if not ID_TEXT_RE.fullmatch(text):
        raise ValueError(f"{label} is not an unambiguous integer representation: {value!r}")
    try:
        decimal = Decimal(text)
    except InvalidOperation as exc:
        raise ValueError(f"{label} is malformed: {value!r}") from exc
    if decimal != decimal.to_integral_value() or decimal < 0:
        raise ValueError(f"{label} must be a nonnegative exact integer: {value!r}")
    return str(int(decimal))


def canonicalize_id_list(values: Iterable[Any], label: str) -> list[str]:
    result = [_canonicalize_identifier(value, label) for value in values]
    if len(result) != len(set(result)):
        duplicates = sorted({value for value in result if result.count(value) > 1})
        raise ValueError(f"{label} contains duplicate identifiers: {duplicates[:10]}")
    return result


def _id_sort_key(value: str) -> tuple[int, int | str]:
    return (0, int(value)) if value.isdigit() else (1, value)


def validate_split_integrity(
    canonical_ids: Sequence[Any],
    train_ids: Sequence[Any],
    val_ids: Sequence[Any],
    test_ids: Sequence[Any],
) -> tuple[list[str], list[str], list[str], list[str]]:
    canonical = canonicalize_id_list(canonical_ids, "canonical_ids")
    train = canonicalize_id_list(train_ids, "train_ids")
    val = canonicalize_id_list(val_ids, "val_ids")
    test = canonicalize_id_list(test_ids, "test_ids")
    canonical_set = set(canonical)
    split_sets = {"train": set(train), "val": set(val), "test": set(test)}
    if not train or not val or not test:
        raise ValueError("Train, validation, and test splits must all be nonempty.")
    overlap = (
        (split_sets["train"] & split_sets["val"])
        | (split_sets["train"] & split_sets["test"])
        | (split_sets["val"] & split_sets["test"])
    )
    if overlap:
        raise ValueError(f"Split identifiers overlap: {sorted(overlap, key=_id_sort_key)[:10]}")
    union = set().union(*split_sets.values())
    missing = canonical_set - union
    unknown = union - canonical_set
    if missing or unknown:
        raise ValueError(
            f"Split union mismatch: missing={len(missing)} unknown={len(unknown)}"
        )
    ordered = sorted(canonical_set, key=_id_sort_key)
    return ordered, train, val, test


def validate_thesis_pickle(
    path: Path,
    dataset: str,
    config_path: Path,
) -> tuple[bool, str]:
    del dataset, config_path
    if not path.exists():
        return False, f"missing thesis pickle: {path}"
    try:
        with path.open("rb") as handle:
            payload = pickle.load(handle)
        if not isinstance(payload, (list, tuple)) or len(payload) != 3:
            return False, "expected exactly [ts, oc, ts_ids]"
        ts, oc, ts_ids = payload
        required_ts = {"ts_id", "minute", "variable", "value"}
        if not required_ts.issubset(set(getattr(ts, "columns", []))):
            return False, f"missing ts columns: {sorted(required_ts - set(ts.columns))}"
        if "ts_id" not in getattr(oc, "columns", []) or "in_hospital_mortality" not in oc.columns:
            return False, "invalid outcomes schema"
        canonical = canonicalize_id_list(ts_ids, "ts_ids")
        ts_set = {
            _canonicalize_identifier(value, "ts.ts_id") for value in ts["ts_id"].tolist()
        }
        oc_values = canonicalize_id_list(oc["ts_id"].tolist(), "oc.ts_id")
        if set(canonical) != ts_set or set(canonical) != set(oc_values):
            return False, "ts, oc, and ts_ids cohorts differ"
        if not canonical:
            return False, "empty canonical cohort"
    except Exception as exc:
        return False, f"failed thesis pickle validation: {exc}"
    return True, "ok"


def validate_latent_tags_csv(path: Path, latent_order: list[str]) -> tuple[bool, str]:
    if not path.exists():
        return False, f"missing latent tags csv: {path}"
    try:
        import pandas as pd

        df = pd.read_csv(path, dtype={"ts_id": "string"})
        validate_prediction_frame(df, latent_order, expected_ids=None, source=str(path))
    except Exception as exc:
        return False, str(exc)
    return True, "ok"


def validate_strats_pickle(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"missing STraTS pickle: {path}"
    try:
        with path.open("rb") as handle:
            payload = pickle.load(handle)
        if not isinstance(payload, (list, tuple)) or len(payload) != 5:
            return False, "expected five-item STraTS payload"
        data, oc, train, val, test = payload
        data_ids = {
            _canonicalize_identifier(value, "data.ts_id")
            for value in data["ts_id"].tolist()
        }
        oc_ids = canonicalize_id_list(oc["ts_id"].tolist(), "oc.ts_id")
        if data_ids != set(oc_ids):
            return False, "event and outcome cohorts differ"
        validate_split_integrity(sorted(data_ids, key=_id_sort_key), train, val, test)
    except Exception as exc:
        return False, str(exc)
    return True, "ok"


def build_strats_pickle(
    dataset: str,
    thesis_pickle_path: Path,
    strats_pickle_path: Path,
    seed: int,
) -> None:
    with thesis_pickle_path.open("rb") as handle:
        payload = pickle.load(handle)
    if not isinstance(payload, (list, tuple)) or len(payload) not in {3, 5}:
        raise ValueError("Canonical/STraTS pickle must contain three or five objects.")
    data, oc = payload[0], payload[1]
    data_ids = {
        _canonicalize_identifier(value, "data.ts_id")
        for value in data["ts_id"].tolist()
    }
    oc_ids = canonicalize_id_list(oc["ts_id"].tolist(), "oc.ts_id")
    if data_ids != set(oc_ids):
        raise ValueError("Event and outcome cohorts must be identical before splitting.")

    if len(payload) == 5:
        canonical, train, val, test = validate_split_integrity(
            sorted(data_ids, key=_id_sort_key), payload[2], payload[3], payload[4]
        )
    else:
        authoritative = canonicalize_id_list(payload[2], "ts_ids")
        if set(authoritative) != data_ids:
            raise ValueError("Authoritative ts_ids must equal event and outcome cohorts.")
        canonical = sorted(authoritative, key=_id_sort_key)
        if len(canonical) < 3:
            raise ValueError(f"At least three canonical IDs are required for dataset {dataset}.")
        import random

        shuffled = list(canonical)
        random.Random(seed).shuffle(shuffled)
        count = len(shuffled)
        train_count = max(1, int(round(count * 0.64)))
        val_count = max(1, int(round(count * 0.16)))
        if train_count + val_count >= count:
            train_count = max(1, count - 2)
            val_count = 1
        train = shuffled[:train_count]
        val = shuffled[train_count : train_count + val_count]
        test = shuffled[train_count + val_count :]
        _, train, val, test = validate_split_integrity(canonical, train, val, test)

    strats_pickle_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = strats_pickle_path.with_name(f".{strats_pickle_path.name}.{os.getpid()}.tmp")
    with temporary.open("wb") as handle:
        pickle.dump([data, oc, train, val, test], handle)
    os.replace(temporary, strats_pickle_path)


def link_or_copy(src: Path, dst: Path, overwrite: bool = False) -> None:
    if not src.is_file():
        raise FileNotFoundError(f"Source artifact is missing: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file: {dst}")
    if dst.exists():
        maybe_remove(dst)
    shutil.copy2(src, dst)


def run_command(
    command: list[str],
    cwd: Path,
    log_path: Path,
    dry_run: bool = False,
    env: dict[str, str] | None = None,
) -> int:
    compact = shlex.join(command)
    if dry_run:
        print(f"[router] DRY RUN: would run command: {compact}")
        return 0
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"# cwd={cwd}\n# command={compact}\n")
        process = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            start_new_session=False,
        )
        assert process.stdout is not None
        for line in process.stdout:
            handle.write(line)
            if not line.endswith("\n"):
                handle.write("\n")
        return_code = process.wait()
    if return_code != 0:
        raise CommandExecutionError(command, return_code, log_path)
    return return_code


def build_preprocessing_command(dataset: str, context: RouterContext) -> list[str]:
    paths = context.datasets[dataset]
    script_name = (
        "src/preprocess_physionet_2012.py"
        if dataset == "physionet"
        else "src/preprocess_mimic_iii_large.py"
    )
    command = [
        context.args.python_executable,
        str(context.thesis_repo_root / script_name),
        "--dataset-config-csv",
        str(paths.resolved_config_csv),
        "--raw-data-path",
        str(resolve_dataset_raw_data_path(dataset, context)),
        "--output-path",
        str(paths.thesis_processed_pkl),
    ]
    if dataset == "physionet":
        command.extend(["--processed-dir", str(paths.thesis_processed_pkl.parent)])
    else:
        command.extend(
            [
                "--chunksize",
                str(context.args.preprocess_chunksize),
                "--tmp-dir",
                str(getattr(paths, "temporary_dir", Path(context.args.tmp_dir or ".").expanduser().resolve()) / "preprocessing"),
            ]
        )
    return command


def _latent_order(context: RouterContext, dataset: str) -> list[str]:
    value = build_resolved_config_row(
        context.configs[dataset], context.args, dataset
    ).get(
        "LATENT_ORDER", []
    )
    if isinstance(value, str):
        value = json.loads(value)
    return [str(item) for item in value]


def _reuse_expected(context: RouterContext, stage: str) -> dict[str, Any]:
    dataset = next(iter(context.datasets))
    return {
        "run_id": context.run_id,
        "dataset": dataset,
        "producing_stage": stage,
        "producer_version": ROUTER_PRODUCER_VERSION,
        "config_fingerprint": context.config_fingerprints[dataset],
        "seed": context.args.seed,
    }


def run_preprocessing(dataset: str, context: RouterContext) -> StageResult:
    paths = context.datasets[dataset]
    command = build_preprocessing_command(dataset, context)
    if context.args.skip_existing and paths.thesis_processed_pkl.exists():
        validate_artifact_record(paths.thesis_processed_pkl, _reuse_expected(context, "preprocessing"))
        return StageResult("skipped", {"reason": "matching provenance", "command": sanitize_command(command)})
    run_command(
        command,
        context.thesis_repo_root,
        build_stage_log_path(context.run_dir, "preprocessing", dataset),
    )
    valid, reason = validate_thesis_pickle(
        paths.thesis_processed_pkl, dataset, paths.resolved_config_csv
    )
    if not valid:
        raise ValueError(reason)
    with paths.thesis_processed_pkl.open("rb") as handle:
        _, _, ids = pickle.load(handle)
    metadata = write_artifact_record(
        paths.thesis_processed_pkl,
        context,
        "preprocessing",
        schema=["ts", "oc", "ts_ids"],
        cohort=[_canonicalize_identifier(value) for value in ids],
        command=command,
    )
    return StageResult(details={"command": sanitize_command(command), "outputs": [str(paths.thesis_processed_pkl), str(metadata)]})


def run_tagging(dataset: str, context: RouterContext) -> StageResult:
    paths = context.datasets[dataset]
    expected_ids = validate_thesis_input(context)
    if not expected_ids:
        raise ValueError("Tagging requires a nonempty trusted thesis cohort.")
    latent_order = _latent_order(context, dataset)
    expected_columns = ["ts_id", *latent_order]
    if dataset == "physionet":
        command = [
            context.args.python_executable,
            str(context.thesis_repo_root / "src" / "tagging_latent_variables_physionet.py"),
            "--dataset-config-csv",
            str(paths.resolved_config_csv),
            "--pkl-path",
            str(paths.thesis_input_pkl),
            "--output-csv-path",
            str(paths.rule_latent_tags_csv),
        ]
    else:
        command = [
            context.args.python_executable,
            str(context.thesis_repo_root / "src" / "tagging_latent_variables_mimiciii.py"),
            "--dataset-config-csv",
            str(paths.resolved_config_csv),
            "--pkl_path",
            str(paths.thesis_input_pkl),
            "--output_dir",
            str(paths.rule_latent_tags_csv.parent),
        ]

    rule_metadata = artifact_metadata_path(paths.rule_latent_tags_csv)
    tree_metadata = artifact_metadata_path(paths.rule_decision_trees_pkl)
    if context.args.skip_existing and (
        paths.rule_latent_tags_csv.exists() or paths.rule_decision_trees_pkl.exists()
    ):
        _require_existing(paths.rule_latent_tags_csv, "Existing rule tags")
        _require_existing(paths.rule_decision_trees_pkl, "Existing decision-tree pickle")
        validate_rule_input(context, expected_ids)
        validate_tree_input(context, expected_ids)
        return StageResult(
            "skipped",
            {
                "reason": "matching provenance",
                "command": sanitize_command(command),
                "outputs": [
                    str(paths.rule_latent_tags_csv),
                    str(rule_metadata),
                    str(paths.rule_decision_trees_pkl),
                    str(tree_metadata),
                ],
            },
        )

    run_command(
        command,
        context.thesis_repo_root,
        build_stage_log_path(context.run_dir, "tagging", dataset),
    )
    valid, reason = validate_latent_tags_csv(
        paths.rule_latent_tags_csv, latent_order
    )
    if not valid:
        raise ValueError(reason)
    _require_existing(paths.rule_decision_trees_pkl, "Tagging decision-tree pickle")

    import pandas as pd

    frame = pd.read_csv(paths.rule_latent_tags_csv, dtype={"ts_id": "string"})
    _require_exact_columns(frame, expected_columns, str(paths.rule_latent_tags_csv))
    validated = validate_prediction_frame(
        frame,
        latent_order,
        expected_ids,
        str(paths.rule_latent_tags_csv),
        require_probabilities=False,
    )
    ids = validated["ts_id"].tolist()
    shared_inputs = {"thesis": file_sha256(paths.thesis_input_pkl)}
    rule_metadata = write_artifact_record(
        paths.rule_latent_tags_csv,
        context,
        "tagging",
        schema=expected_columns,
        cohort=ids,
        command=command,
        inputs=shared_inputs,
    )
    tree_metadata = write_artifact_record(
        paths.rule_decision_trees_pkl,
        context,
        "tagging",
        schema=["latent_decision_trees"],
        cohort=ids,
        command=command,
        inputs={
            **shared_inputs,
            "rules": file_sha256(paths.rule_latent_tags_csv),
        },
    )
    validate_rule_input(context, expected_ids)
    validate_tree_input(context, expected_ids)
    return StageResult(
        details={
            "command": sanitize_command(command),
            "outputs": [
                str(paths.rule_latent_tags_csv),
                str(rule_metadata),
                str(paths.rule_decision_trees_pkl),
                str(tree_metadata),
            ],
        }
    )

def run_tree_plots(dataset: str, context: RouterContext) -> StageResult:
    paths = context.datasets[dataset]
    validate_tree_input(context)
    command = [
        context.args.python_executable,
        str(context.thesis_repo_root / "src" / "decision_trees_plot.py"),
        "--dataset",
        dataset,
        "--dataset-config-csv",
        str(paths.resolved_config_csv),
        "--pickle-path",
        str(paths.decision_trees_input_pkl),
        "--output-dir",
        str(paths.tree_plots_dir),
        "--format",
        "png",
        "--overwrite",
    ]
    run_command(command, context.thesis_repo_root, build_stage_log_path(context.run_dir, "trees", dataset))
    return StageResult(details={"command": sanitize_command(command), "outputs": [str(paths.tree_plots_dir)]})


def prepare_strats_filesystem(context: RouterContext) -> StageResult:
    import pandas as pd

    dataset, paths = next(iter(context.datasets.items()))
    latent_order = _latent_order(context, dataset)
    validate_artifact_record(
        paths.thesis_input_pkl, _reuse_expected(context, "preprocessing")
    )
    validate_artifact_record(
        paths.rule_input_csv, _reuse_expected(context, "tagging")
    )
    paths.strats_processed_pkl.parent.mkdir(parents=True, exist_ok=True)
    paths.strats_latent_tags_csv.parent.mkdir(parents=True, exist_ok=True)
    adapter_seed = derive_seed(context.args.seed, dataset, "adapter")
    build_strats_pickle(
        dataset, paths.thesis_input_pkl, paths.strats_processed_pkl, adapter_seed
    )
    valid, reason = validate_strats_pickle(paths.strats_processed_pkl)
    if not valid:
        raise ValueError(reason)
    with paths.strats_processed_pkl.open("rb") as handle:
        data, _, train, val, test = pickle.load(handle)
    data_ids = sorted(
        {
            _canonicalize_identifier(value, "STraTS data.ts_id")
            for value in data["ts_id"].tolist()
        },
        key=_id_sort_key,
    )
    _, train, val, test = validate_split_integrity(
        data_ids, train, val, test
    )
    cohort = [*train, *val, *test]

    source_labels = pd.read_csv(
        paths.rule_input_csv, dtype={"ts_id": "string"}
    )
    normalized_labels = validate_prediction_frame(
        source_labels,
        latent_order,
        cohort,
        str(paths.rule_input_csv),
        require_probabilities=False,
    )
    temporary = paths.strats_latent_tags_csv.with_name(
        f".{paths.strats_latent_tags_csv.name}.{os.getpid()}.tmp"
    )
    normalized_labels.to_csv(temporary, index=False)
    os.replace(temporary, paths.strats_latent_tags_csv)

    processed_meta = write_artifact_record(
        paths.strats_processed_pkl,
        context,
        "prepare-strats",
        schema=["data", "oc", "train_ids", "val_ids", "test_ids"],
        inputs={"thesis": file_sha256(paths.thesis_input_pkl)},
        cohort=cohort,
        seed=adapter_seed,
    )
    label_meta = write_artifact_record(
        paths.strats_latent_tags_csv,
        context,
        "prepare-strats",
        schema=["ts_id", *latent_order],
        inputs={"rules": file_sha256(paths.rule_input_csv)},
        cohort=cohort,
        seed=adapter_seed,
    )
    bundle = paths.strats_input_root / "artifact_manifest.json"
    write_json(
        bundle,
        {
            "run_id": context.run_id,
            "dataset": dataset,
            "config_fingerprint": context.config_fingerprints[dataset],
            "seed": context.args.seed,
            "adapter_seed": adapter_seed,
            "processed": str(paths.strats_processed_pkl.resolve()),
            "labels": str(paths.strats_latent_tags_csv.resolve()),
            "processed_sha256": file_sha256(paths.strats_processed_pkl),
            "labels_sha256": file_sha256(paths.strats_latent_tags_csv),
            "cohort_size": len(cohort),
            "cohort_fingerprint": stable_hash(sorted(cohort)),
            "producer_version": ROUTER_PRODUCER_VERSION,
        },
    )
    return StageResult(
        details={
            "outputs": [
                str(paths.strats_processed_pkl),
                str(processed_meta),
                str(paths.strats_latent_tags_csv),
                str(label_meta),
                str(bundle),
            ]
        }
    )


def validate_strats_inputs(context: RouterContext) -> None:
    import pandas as pd

    dataset, paths = next(iter(context.datasets.items()))
    latent_order = _latent_order(context, dataset)
    _require_existing(paths.strats_processed_pkl, "STraTS processed input")
    _require_existing(paths.strats_latent_tags_csv, "STraTS labels")
    _require_existing(
        paths.strats_input_root / "artifact_manifest.json",
        "STraTS input bundle manifest",
    )

    valid, reason = validate_strats_pickle(paths.strats_processed_pkl)
    if not valid:
        raise ValueError(f"Invalid STraTS processed input: {reason}")
    with paths.strats_processed_pkl.open("rb") as handle:
        data, _, train, val, test = pickle.load(handle)
    data_ids = sorted(
        {
            _canonicalize_identifier(value, "STraTS data.ts_id")
            for value in data["ts_id"].tolist()
        },
        key=_id_sort_key,
    )
    _, train, val, test = validate_split_integrity(
        data_ids, train, val, test
    )
    cohort = [*train, *val, *test]

    labels = pd.read_csv(
        paths.strats_latent_tags_csv, dtype={"ts_id": "string"}
    )
    validate_prediction_frame(
        labels,
        latent_order,
        cohort,
        str(paths.strats_latent_tags_csv),
        require_probabilities=False,
    )

    adapter_seed = derive_seed(context.args.seed, dataset, "adapter")
    common_expected = {
        "run_id": context.run_id,
        "dataset": dataset,
        "producing_stage": "prepare-strats",
        "producer_version": ROUTER_PRODUCER_VERSION,
        "config_fingerprint": context.config_fingerprints[dataset],
        "seed": adapter_seed,
        "cohort_size": len(cohort),
        "cohort_fingerprint": stable_hash(sorted(cohort)),
    }
    validate_artifact_record(
        paths.strats_processed_pkl,
        {
            **common_expected,
            "schema": [
                "data",
                "oc",
                "train_ids",
                "val_ids",
                "test_ids",
            ],
        },
    )
    validate_artifact_record(
        paths.strats_latent_tags_csv,
        {
            **common_expected,
            "schema": ["ts_id", *latent_order],
        },
    )

    bundle = _load_json(paths.strats_input_root / "artifact_manifest.json")
    expected = {
        "run_id": context.run_id,
        "dataset": dataset,
        "config_fingerprint": context.config_fingerprints[dataset],
        "seed": context.args.seed,
        "adapter_seed": adapter_seed,
        "processed": str(paths.strats_processed_pkl.resolve()),
        "labels": str(paths.strats_latent_tags_csv.resolve()),
        "processed_sha256": file_sha256(paths.strats_processed_pkl),
        "labels_sha256": file_sha256(paths.strats_latent_tags_csv),
        "cohort_size": len(cohort),
        "cohort_fingerprint": stable_hash(sorted(cohort)),
        "producer_version": ROUTER_PRODUCER_VERSION,
    }
    mismatches = {
        key: (bundle.get(key), value)
        for key, value in expected.items()
        if bundle.get(key) != value
    }
    if mismatches:
        raise ValueError(f"STraTS input bundle provenance mismatch: {mismatches}")


class GPUFilePermit:
    def __init__(
        self,
        lock_path: Path,
        event_callback: Callable[[str, str], None] | None = None,
    ):
        self.lock_path = Path(lock_path)
        self.event_callback = event_callback
        self.handle: Any = None
        self.acquired = False

    def _event(self, name: str) -> None:
        if self.event_callback:
            self.event_callback(name, utc_now())

    def _release(self) -> None:
        handle = self.handle
        acquired = self.acquired
        if handle is None:
            return
        try:
            if acquired:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            try:
                handle.close()
            finally:
                self.handle = None
                self.acquired = False
                if acquired:
                    self._event("permit_released_at")

    def __enter__(self) -> "GPUFilePermit":
        self._event("permit_wait_start")
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.lock_path.open("a+", encoding="utf-8")
        try:
            import fcntl
        except ImportError as exc:
            self.handle.close()
            self.handle = None
            raise RuntimeError("Process-safe GPU locking requires fcntl on this platform.") from exc
        try:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX)
        except BaseException:
            self.handle.close()
            self.handle = None
            raise
        self.acquired = True
        try:
            self.handle.seek(0)
            self.handle.truncate()
            self.handle.write(json.dumps({"pid": os.getpid(), "acquired_at": utc_now()}) + "\n")
            self.handle.flush()
            self._event("permit_acquired_at")
        except BaseException:
            try:
                self._release()
            except BaseException:
                pass
            raise
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> bool:
        try:
            self._release()
        except BaseException:
            if exc_type is None:
                raise
        return False


def run_strats_script(context: RouterContext) -> StageResult:
    dataset, paths = next(iter(context.datasets.items()))
    if context.args.run_strats is False:
        return StageResult("skipped", {"reason": "--run-strats false"})
    validate_strats_inputs(context)
    script = Path(context.args.strats_script_path)
    if not script.is_absolute():
        script = (context.strats_repo_root / script).resolve()
    command = ["bash", str(script)]
    assignment = context.gpu_assignment
    env = dict(os.environ)
    env.update(
        {
            "PYTHON": str(context.args.python_executable),
            "DATASET_SCOPE": dataset,
            "STRATS_INPUT_ROOT": str(paths.strats_input_root),
            "STRATS_OUTPUT_ROOT": str(paths.strats_output_root),
            "CLINICAUSE_RUN_ID": context.run_id,
            "STRATS_CONFIG_FINGERPRINT": context.config_fingerprints[dataset],
            "STRATS_BASE_SEED": str(context.args.seed),
            "STRATS_MAX_CONCURRENT": str(assignment.max_concurrent if assignment else 1),
            "STRATS_TRAIN_FRAC": str(context.args.strats_train_frac),
            "STRATS_MODEL_RUN": context.args.strats_model_run,
        }
    )
    if assignment and assignment.physical is not None:
        env["CUDA_VISIBLE_DEVICES"] = assignment.physical

    def record_event(name: str, timestamp: str) -> None:
        update_gpu_manifest(context, **{name: timestamp})

    lock_path = assignment.lock_path if assignment else (
        context.run_root / "coordinator" / "gpu_locks" / "global.lock"
    )
    verified_outputs: list[str] = []
    terminal_recorded = False
    try:
        with GPUFilePermit(lock_path, record_event):
            update_gpu_manifest(context, strats_start=utc_now())
            try:
                return_code = run_command(
                    command,
                    context.strats_repo_root,
                    build_stage_log_path(context.run_dir, "run_strats", dataset),
                    env=env,
                )
                for model in MODELS:
                    prediction = paths.strats_predictions_dir / f"{model}.csv"
                    validate_strats_prediction_metadata(prediction, context, model)
                    verified_outputs.extend(
                        [str(prediction), str(_find_strats_metadata(prediction))]
                    )
            except BaseException as exc:
                return_code = (
                    exc.returncode
                    if isinstance(exc, CommandExecutionError)
                    else return_code
                )
                update_gpu_manifest(
                    context,
                    strats_finish=utc_now(),
                    strats_exit_code=return_code,
                    failure_reason=f"{type(exc).__name__}: {exc}",
                )
                terminal_recorded = True
                raise
            update_gpu_manifest(
                context,
                strats_finish=utc_now(),
                strats_exit_code=return_code,
                failure_reason=None,
            )
            terminal_recorded = True
    except BaseException as exc:
        if not terminal_recorded:
            return_code = (
                exc.returncode if isinstance(exc, CommandExecutionError) else None
            )
            update_gpu_manifest(
                context,
                strats_finish=utc_now(),
                strats_exit_code=return_code,
                failure_reason=f"{type(exc).__name__}: {exc}",
            )
        raise
    return StageResult(details={
        "command": sanitize_command(command),
        "environment": {
            "DATASET_SCOPE": dataset,
            "CUDA_VISIBLE_DEVICES": env.get("CUDA_VISIBLE_DEVICES"),
            "STRATS_INPUT_ROOT": str(paths.strats_input_root),
            "STRATS_OUTPUT_ROOT": str(paths.strats_output_root),
            "STRATS_BASE_SEED": str(context.args.seed),
        },
        "outputs": verified_outputs,
    })


def _find_strats_metadata(path: Path) -> Path:
    for candidate in [Path(str(path) + ".metadata.json"), artifact_metadata_path(path)]:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"Prediction provenance metadata is missing for {path}")


def derive_strats_dataset_seed(base_seed: int, dataset: str) -> int:
    offsets = {"physionet": 100_000, "mimic": 200_000}
    return (int(base_seed) + offsets[dataset]) % (2**31 - 1)


def derive_strats_model_seed(base_seed: int, dataset: str, model: str) -> int:
    offsets = {"strats": 1, "gru": 3, "grud": 4, "tcn": 5, "sand": 6}
    return (derive_strats_dataset_seed(base_seed, dataset) + offsets[model]) % (2**31 - 1)


def derive_strats_effective_seed(model_seed: int, run_spec: str) -> int:
    match = re.fullmatch(r"([1-9][0-9]*)o([1-9][0-9]*)", str(run_spec))
    if match is None or int(match.group(1)) > int(match.group(2)):
        raise ValueError(f"Invalid STraTS model-run specification: {run_spec!r}")
    return (int(model_seed) + int(match.group(1))) % (2**31 - 1)


def _expected_strats_scientific_config(
    context: RouterContext, model: str
) -> tuple[dict[str, Any], dict[str, Any], str]:
    dataset, paths = next(iter(context.datasets.items()))
    with paths.strats_processed_pkl.open("rb") as handle:
        payload = pickle.load(handle)
    if not isinstance(payload, (list, tuple)) or len(payload) != 5:
        raise ValueError(
            f"Invalid STraTS input while deriving training schedule: {paths.strats_processed_pkl}"
        )
    full_train_count = len(payload[2])
    selected_train_count = math.ceil(
        context.args.strats_train_frac * full_train_count
    )
    model_config = {
        "model_type": model,
        "hid_dim": (
            128
            if model == "tcn" and dataset == "mimic"
            else 64
        ),
        "num_layers": (
            6
            if model == "tcn" and dataset == "physionet"
            else 4
            if model in {"tcn", "sand"}
            else 2
        ),
        "num_heads": 16 if model == "strats" else 4,
        "dropout": 0.2,
        "attention_dropout": 0.2,
        "kernel_size": 4,
        "r": 24,
        "M": 12,
        "max_obs": 880,
        "max_timesteps": 880,
        "hours_look_ahead": 24,
        "ref_points": 24,
        "train_frac": context.args.strats_train_frac,
        "run": context.args.strats_model_run,
        "architecture_mode": "finetune" if model == "strats" else "scratch",
    }
    batches_per_epoch = selected_train_count / 16
    training_config = {
        "max_epochs": 50,
        "max_steps": int(round(batches_per_epoch) * 50),
        "patience": 10,
        "lr": 5e-5 if model == "strats" else 5e-4,
        "train_batch_size": 16,
        "gradient_accumulation_steps": 1,
        "eval_batch_size": 32,
        "validate_after": -1,
        "validate_every": math.ceil(batches_per_epoch),
    }
    scientific_fingerprint = stable_hash(
        {
            "model_config": model_config,
            "training_config": training_config,
        }
    )
    return model_config, training_config, scientific_fingerprint

def _expected_strats_prediction_cohort(context: RouterContext) -> list[str]:
    paths = next(iter(context.datasets.values()))
    if paths.strats_processed_pkl.is_file():
        with paths.strats_processed_pkl.open("rb") as handle:
            payload = pickle.load(handle)
        if not isinstance(payload, (list, tuple)) or len(payload) != 5:
            raise ValueError(
                f"Invalid STraTS input while deriving prediction cohort: {paths.strats_processed_pkl}"
            )
        data_ids = canonicalize_id_list(
            sorted(
                {
                    _canonicalize_identifier(value, "STraTS data.ts_id")
                    for value in payload[0]["ts_id"].tolist()
                },
                key=_id_sort_key,
            ),
            "STraTS data cohort",
        )
        _, train, val, test = validate_split_integrity(
            data_ids, payload[2], payload[3], payload[4]
        )
        return [*train, *val, *test]
    return _expected_cohort_from_thesis(paths.thesis_input_pkl)


def validate_strats_prediction_metadata(
    path: Path,
    context: RouterContext,
    model: str,
) -> dict[str, Any]:
    dataset = next(iter(context.datasets))
    metadata_path = _find_strats_metadata(path)
    metadata = _load_json(metadata_path)
    model_seed = derive_strats_model_seed(context.args.seed, dataset, model)
    expected_architecture = "finetune" if model == "strats" else "scratch"
    expected_model_config, expected_training_config, expected_scientific_fingerprint = (
        _expected_strats_scientific_config(context, model)
    )
    required_values = {
        "metadata_schema_version": 2,
        "artifact_kind": "prediction",
        "artifact_name": path.name,
        "architecture_mode": expected_architecture,
        "pipeline_run_id": context.run_id,
        "dataset": context.datasets[dataset].strats_dataset,
        "model": model,
        "ordered_targets": _latent_order(context, dataset),
        "config_fingerprint": context.config_fingerprints[dataset],
        "base_seed": context.args.seed,
        "dataset_seed": derive_strats_dataset_seed(context.args.seed, dataset),
        "model_seed": model_seed,
        "effective_seed": derive_strats_effective_seed(model_seed, context.args.strats_model_run),
    }
    mismatches = {
        key: (metadata.get(key), expected)
        for key, expected in required_values.items()
        if metadata.get(key) != expected
    }
    actual_digest = file_sha256(path)
    if metadata.get("artifact_sha256") != actual_digest:
        mismatches["artifact_sha256"] = (
            metadata.get("artifact_sha256"),
            actual_digest,
        )
    if metadata.get("artifact_size") != path.stat().st_size:
        mismatches["artifact_size"] = (
            metadata.get("artifact_size"),
            path.stat().st_size,
        )
    required = {
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
    missing = sorted(required - set(metadata))
    cohort = metadata.get("cohort")
    if not isinstance(cohort, dict) or set(cohort) != {"count", "sha256"}:
        mismatches["cohort"] = (cohort, "count and sha256 descriptor")
    targets = _latent_order(context, dataset)
    expected_columns = [
        "ts_id",
        *[f"{target}_prob" for target in targets],
        *targets,
    ]
    schema = metadata.get("schema")
    if not isinstance(schema, dict) or schema.get("columns") != expected_columns:
        mismatches["schema.columns"] = (
            schema.get("columns") if isinstance(schema, dict) else None,
            expected_columns,
        )
    elif schema.get("probability_range") != [0.0, 1.0]:
        mismatches["schema.probability_range"] = (
            schema.get("probability_range"),
            [0.0, 1.0],
        )
    elif schema.get("binary_values") != [0, 1]:
        mismatches["schema.binary_values"] = (
            schema.get("binary_values"),
            [0, 1],
        )
    producing_command = metadata.get("producing_command")
    if not isinstance(producing_command, list) or not producing_command:
        mismatches["producing_command"] = (
            producing_command,
            "nonempty sanitized command list",
        )
    model_config = metadata.get("model_config")
    if model_config != expected_model_config:
        mismatches["model_config"] = (model_config, expected_model_config)
    training_config = metadata.get("training_config")
    if training_config != expected_training_config:
        mismatches["training_config"] = (
            training_config,
            expected_training_config,
        )
    if metadata.get("scientific_config_fingerprint") != expected_scientific_fingerprint:
        mismatches["scientific_config_fingerprint"] = (
            metadata.get("scientific_config_fingerprint"),
            expected_scientific_fingerprint,
        )
    inputs = metadata.get("inputs")
    required_inputs = {"processed_data", "latent_tags", "checkpoint"}
    if not isinstance(inputs, dict) or not required_inputs.issubset(inputs):
        mismatches["inputs"] = (
            sorted(inputs) if isinstance(inputs, dict) else inputs,
            sorted(required_inputs),
        )
    else:
        for input_name in sorted(required_inputs):
            descriptor = inputs[input_name]
            if not isinstance(descriptor, dict) or not {
                "name",
                "size",
                "sha256",
            }.issubset(descriptor):
                mismatches[f"inputs.{input_name}"] = (
                    descriptor,
                    "name/size/sha256 descriptor",
                )

    import pandas as pd

    expected_ids = _expected_strats_prediction_cohort(context)
    prediction_frame = pd.read_csv(path, dtype={"ts_id": "string"})
    validated_frame = validate_prediction_frame(
        prediction_frame,
        targets,
        expected_ids,
        str(path),
        require_probabilities=True,
    )
    actual_ids = validated_frame["ts_id"].tolist()
    actual_cohort = {
        "count": len(actual_ids),
        "sha256": stable_hash(sorted(actual_ids)),
    }
    if cohort != actual_cohort:
        mismatches["cohort"] = (cohort, actual_cohort)

    if missing or mismatches:
        raise ValueError(
            f"Invalid STraTS prediction provenance for {path}: missing={missing}, "
            f"mismatches={mismatches}"
        )
    return metadata


def collect_strats_outputs(context: RouterContext) -> StageResult:
    dataset, paths = next(iter(context.datasets.items()))
    paths.predicted_raw_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    for model in MODELS:
        source = paths.strats_predictions_dir / f"{model}.csv"
        metadata = validate_strats_prediction_metadata(source, context, model)
        target = paths.predicted_raw_dir / f"{model}.csv"
        if target.exists():
            raise FileExistsError(f"Refusing to overwrite collected prediction: {target}")
        shutil.copy2(source, target)
        sidecar = write_artifact_record(
            target,
            context,
            "collect-strats",
            schema=metadata["schema"],
            model=model,
            targets=list(metadata["ordered_targets"]),
            cohort=_expected_strats_prediction_cohort(context),
            seed=int(metadata["effective_seed"]),
            command=metadata.get("producing_command", []),
            inputs={"source": file_sha256(source)},
        )
        upstream_metadata = Path(str(target) + ".metadata.json")
        shutil.copy2(_find_strats_metadata(source), upstream_metadata)
        outputs.extend([str(target), str(sidecar), str(upstream_metadata)])
    return StageResult(details={"outputs": outputs})


def _validate_probabilities(series: Any, source: str, column: str) -> Any:
    import numpy as np
    import pandas as pd

    try:
        values = pd.to_numeric(series, errors="raise")
    except Exception as exc:
        raise ValueError(f"Malformed probability in {source}, column {column}") from exc
    array = values.to_numpy(dtype=float)
    if np.isnan(array).any() or np.isinf(array).any():
        raise ValueError(f"Non-finite probability in {source}, column {column}")
    if ((array < 0) | (array > 1)).any():
        raise ValueError(f"Out-of-range probability in {source}, column {column}")
    return values.astype(float)


def validate_prediction_frame(
    frame: Any,
    latent_order: Sequence[str],
    expected_ids: Sequence[Any] | None,
    source: str,
    *,
    require_probabilities: bool = False,
) -> Any:
    import numpy as np
    import pandas as pd

    if "ts_id" not in frame.columns:
        raise ValueError(f"Missing ts_id in {source}")
    normalized_ids = [
        _canonicalize_identifier(value, f"{source}.ts_id")
        for value in frame["ts_id"].tolist()
    ]
    if len(normalized_ids) != len(set(normalized_ids)):
        raise ValueError(f"Duplicate normalized ts_id values in {source}")
    missing_targets = [column for column in latent_order if column not in frame.columns]
    if missing_targets:
        raise ValueError(f"Missing latent columns {missing_targets} in {source}")
    if require_probabilities:
        missing_probabilities = [
            f"{column}_prob"
            for column in latent_order
            if f"{column}_prob" not in frame.columns
        ]
        if missing_probabilities:
            raise ValueError(
                f"Missing probability columns {missing_probabilities} in {source}"
            )
    allowed = {"ts_id", *latent_order, *(f"{column}_prob" for column in latent_order)}
    extras = sorted(set(frame.columns) - allowed)
    if extras:
        raise ValueError(f"Unexpected prediction columns {extras} in {source}")

    output = pd.DataFrame({"ts_id": normalized_ids})
    for column in latent_order:
        try:
            numeric = pd.to_numeric(frame[column], errors="raise")
        except Exception as exc:
            raise ValueError(f"Malformed binary value in {source}, column {column}") from exc
        values = numeric.to_numpy(dtype=float)
        if np.isnan(values).any() or np.isinf(values).any() or not np.isin(values, [0, 1]).all():
            raise ValueError(f"Invalid binary value in {source}, column {column}")
        output[column] = numeric.astype(int)
        probability_column = f"{column}_prob"
        if probability_column in frame.columns:
            probabilities = _validate_probabilities(
                frame[probability_column], source, probability_column
            )
            expected_tags = (probabilities.to_numpy() >= 0.5).astype(int)
            if not np.array_equal(expected_tags, output[column].to_numpy()):
                raise ValueError(
                    f"Probability/tag inconsistency in {source}, target {column}"
                )

    if expected_ids is not None:
        expected = canonicalize_id_list(expected_ids, "expected cohort")
        actual_set = set(normalized_ids)
        expected_set = set(expected)
        if actual_set != expected_set:
            raise ValueError(
                f"Prediction cohort mismatch in {source}: "
                f"missing={len(expected_set - actual_set)} extra={len(actual_set - expected_set)}"
            )
        order = {identifier: index for index, identifier in enumerate(expected)}
        output["_order"] = output["ts_id"].map(order)
        output = output.sort_values("_order").drop(columns="_order").reset_index(drop=True)
    return output[["ts_id", *latent_order]]


def _expected_cohort_from_thesis(path: Path) -> list[str]:
    with path.open("rb") as handle:
        payload = pickle.load(handle)
    if not isinstance(payload, (list, tuple)) or len(payload) != 3:
        raise ValueError(f"Invalid canonical pickle for cohort extraction: {path}")
    return canonicalize_id_list(payload[2], "canonical ts_ids")


def normalize_prediction_csvs(context: RouterContext) -> StageResult:
    import pandas as pd

    dataset, paths = next(iter(context.datasets.items()))
    latent_order = _latent_order(context, dataset)
    expected_ids = _expected_cohort_from_thesis(paths.thesis_input_pkl)
    source_paths = {"rules": paths.rule_input_csv}
    source_base = (
        paths.predicted_raw_dir
        if "collect-strats" in context.args.stages
        else paths.strats_predictions_dir
    )
    source_paths.update({model: source_base / f"{model}.csv" for model in MODELS})

    validated: dict[str, Any] = {}
    for model, source in source_paths.items():
        if model == "rules":
            validate_artifact_record(
                source,
                _reuse_expected(context, "tagging"),
            )
        else:
            validate_strats_prediction_metadata(source, context, model)
        frame = pd.read_csv(source, dtype={"ts_id": "string"})
        validated[model] = validate_prediction_frame(
            frame,
            latent_order,
            expected_ids,
            str(source),
            require_probabilities=model != "rules",
        )

    paths.voters_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    for model, frame in validated.items():
        destination = paths.voters_dir / f"{model}.csv"
        if destination.exists():
            raise FileExistsError(f"Refusing to overwrite normalized voter: {destination}")
        temporary = destination.with_name(f".{destination.name}.{os.getpid()}.tmp")
        frame.to_csv(temporary, index=False)
        os.replace(temporary, destination)
        metadata = write_artifact_record(
            destination,
            context,
            "normalize-predictions",
            schema=["ts_id", *latent_order],
            model=model,
            targets=list(latent_order),
            cohort=expected_ids,
            inputs={"source": file_sha256(source_paths[model])},
        )
        outputs.extend([str(destination), str(metadata)])
    return StageResult(details={"outputs": outputs, "cohort_size": len(expected_ids)})


def run_thesis_main(dataset: str, context: RouterContext) -> StageResult:
    paths = context.datasets[dataset]
    command = [
        context.args.python_executable,
        str(context.thesis_repo_root / "main.py"),
        "--dataset",
        dataset,
        "--dataset-config-csv",
        str(paths.resolved_config_csv),
        "--latent-tags-dir",
        str(paths.voters_input_dir),
        "--dataset-pkl-path",
        str(paths.thesis_input_pkl),
        "--output-dir",
        str(paths.thesis_main_output_dir),
    ]
    if context.args.cate_model is not None:
        command.extend(["--model-type", context.args.cate_model])
    if context.args.cate_model == "CausalPFN":
        command.extend(["--mortality-device", "cpu"])

    assignment = context.gpu_assignment
    lock_path = assignment.lock_path if assignment else (
        context.run_root / "coordinator" / "gpu_locks" / "global.lock"
    )
    event_names = {
        "permit_wait_start": "causal_permit_wait_start",
        "permit_acquired_at": "causal_permit_acquired_at",
        "permit_released_at": "causal_permit_released_at",
    }

    def record_event(name: str, timestamp: str) -> None:
        update_gpu_manifest(context, **{event_names[name]: timestamp})

    summary = paths.thesis_main_output_dir / "run_summary.json"
    return_code: int | None = None
    terminal_recorded = False
    try:
        with GPUFilePermit(lock_path, record_event):
            update_gpu_manifest(context, causal_start=utc_now())
            try:
                return_code = run_command(
                    command,
                    context.thesis_repo_root,
                    build_stage_log_path(context.run_dir, "thesis_main", dataset),
                )
                if not summary.is_file():
                    raise FileNotFoundError(
                        f"Expected thesis main summary not found: {summary}"
                    )
            except BaseException as exc:
                return_code = (
                    exc.returncode
                    if isinstance(exc, CommandExecutionError)
                    else return_code
                )
                update_gpu_manifest(
                    context,
                    causal_finish=utc_now(),
                    causal_exit_code=return_code,
                    causal_failure_reason=f"{type(exc).__name__}: {exc}",
                )
                terminal_recorded = True
                raise
            update_gpu_manifest(
                context,
                causal_finish=utc_now(),
                causal_exit_code=return_code,
                causal_failure_reason=None,
            )
            terminal_recorded = True
    except BaseException as exc:
        if not terminal_recorded:
            return_code = (
                exc.returncode
                if isinstance(exc, CommandExecutionError)
                else return_code
            )
            update_gpu_manifest(
                context,
                causal_finish=utc_now(),
                causal_exit_code=return_code,
                causal_failure_reason=f"{type(exc).__name__}: {exc}",
            )
        raise
    return StageResult(
        details={
            "command": sanitize_command(command),
            "outputs": [str(paths.thesis_main_output_dir)],
        }
    )

def should_validate_existing_strats_inputs(context: RouterContext) -> bool:
    stages = set(context.args.stages)
    return "run-strats" in stages and "prepare-strats" not in stages


def print_stage(stage_index: int, total: int, stage_name: str) -> None:
    print(f"[router] === Stage {stage_index}/{total}: {stage_name} ===")


def _execute_stage(context: RouterContext, stage: str) -> StageResult:
    dataset = next(iter(context.datasets))
    if stage == "preprocessing":
        return run_preprocessing(dataset, context)
    if stage == "tagging":
        return run_tagging(dataset, context)
    if stage == "trees":
        return run_tree_plots(dataset, context)
    if stage == "prepare-strats":
        return prepare_strats_filesystem(context)
    if stage == "run-strats":
        return run_strats_script(context)
    if stage == "collect-strats":
        return collect_strats_outputs(context)
    if stage == "normalize-predictions":
        return normalize_prediction_csvs(context)
    if stage == "thesis-main":
        return run_thesis_main(dataset, context)
    raise ValueError(f"Unsupported stage: {stage}")


def _fingerprint_output(path_like: str) -> dict[str, Any]:
    path = Path(path_like)
    if path.is_file():
        return {
            "kind": "file",
            "path": str(path.resolve()),
            "sha256": file_sha256(path),
            "size": path.stat().st_size,
        }
    if path.is_dir():
        entries = []
        for child in sorted(item for item in path.rglob("*") if item.is_file()):
            entries.append(
                {
                    "relative_path": str(child.relative_to(path)),
                    "sha256": file_sha256(child),
                    "size": child.stat().st_size,
                }
            )
        return {
            "kind": "directory",
            "path": str(path.resolve()),
            "fingerprint": stable_hash(entries),
            "entries": len(entries),
        }
    raise FileNotFoundError(f"Stage output is missing: {path}")


def _fingerprint_input(path_like: str | Path) -> dict[str, Any]:
    """Fingerprint stage inputs without rereading large directory contents."""

    path = Path(path_like)
    if path.is_file():
        return _fingerprint_output(str(path))
    if path.is_dir():
        entries = [
            {
                "relative_path": str(child.relative_to(path)),
                "size": child.stat().st_size,
                "mtime_ns": child.stat().st_mtime_ns,
            }
            for child in sorted(item for item in path.rglob("*") if item.is_file())
        ]
        return {
            "kind": "input-directory",
            "path": str(path.resolve()),
            "fingerprint": stable_hash(entries),
            "entries": len(entries),
        }
    raise FileNotFoundError(f"Stage input is missing: {path}")


def _stage_input_paths(context: RouterContext, stage: str) -> list[Path]:
    dataset, paths = next(iter(context.datasets.items()))
    if stage == "preprocessing":
        return [resolve_dataset_raw_data_path(dataset, context)]
    if stage == "tagging":
        return [
            paths.thesis_input_pkl,
            artifact_metadata_path(paths.thesis_input_pkl),
        ]
    if stage == "trees":
        return [
            paths.decision_trees_input_pkl,
            artifact_metadata_path(paths.decision_trees_input_pkl),
        ]
    if stage == "prepare-strats":
        return [
            paths.thesis_input_pkl,
            artifact_metadata_path(paths.thesis_input_pkl),
            paths.rule_input_csv,
            artifact_metadata_path(paths.rule_input_csv),
        ]
    if stage == "run-strats":
        return [
            paths.strats_processed_pkl,
            artifact_metadata_path(paths.strats_processed_pkl),
            paths.strats_latent_tags_csv,
            artifact_metadata_path(paths.strats_latent_tags_csv),
            paths.strats_input_root / "artifact_manifest.json",
        ]
    if stage == "collect-strats":
        inputs: list[Path] = []
        for model in MODELS:
            prediction = paths.strats_predictions_dir / f"{model}.csv"
            inputs.extend([prediction, _find_strats_metadata(prediction)])
        return inputs
    if stage == "normalize-predictions":
        inputs = [
            paths.thesis_input_pkl,
            artifact_metadata_path(paths.thesis_input_pkl),
            paths.rule_input_csv,
            artifact_metadata_path(paths.rule_input_csv),
        ]
        source_base = (
            paths.predicted_raw_dir
            if "collect-strats" in context.args.stages
            else paths.strats_predictions_dir
        )
        for model in MODELS:
            prediction = source_base / f"{model}.csv"
            inputs.extend([prediction, _find_strats_metadata(prediction)])
        return inputs
    if stage == "thesis-main":
        inputs = [
            paths.thesis_input_pkl,
            artifact_metadata_path(paths.thesis_input_pkl),
        ]
        for model in ("rules", *MODELS):
            voter = paths.voters_input_dir / f"{model}.csv"
            inputs.extend([voter, artifact_metadata_path(voter)])
        return inputs
    raise ValueError(f"Unsupported stage input contract: {stage}")


def _stage_input_descriptors(context: RouterContext, stage: str) -> list[dict[str, Any]]:
    return [_fingerprint_input(path) for path in _stage_input_paths(context, stage)]


def _planned_stage_command(context: RouterContext, stage: str) -> list[str]:
    dataset = next(iter(context.datasets))
    if stage == "preprocessing":
        return build_preprocessing_command(dataset, context)
    if stage == "run-strats":
        script = Path(context.args.strats_script_path)
        if not script.is_absolute():
            script = (context.strats_repo_root / script).resolve()
        return ["bash", str(script)]
    return [
        str(Path(__file__).resolve()),
        f"<internal-stage:{stage}>",
        f"--dataset={dataset}",
    ]


def _expected_stage_output_paths(
    context: RouterContext, stage: str
) -> list[Path]:
    dataset, paths = next(iter(context.datasets.items()))
    if stage == "preprocessing":
        return [
            paths.thesis_processed_pkl,
            artifact_metadata_path(paths.thesis_processed_pkl),
        ]
    if stage == "tagging":
        return [
            paths.rule_latent_tags_csv,
            artifact_metadata_path(paths.rule_latent_tags_csv),
            paths.rule_decision_trees_pkl,
            artifact_metadata_path(paths.rule_decision_trees_pkl),
        ]
    if stage == "trees":
        return [paths.tree_plots_dir]
    if stage == "prepare-strats":
        return [
            paths.strats_processed_pkl,
            artifact_metadata_path(paths.strats_processed_pkl),
            paths.strats_latent_tags_csv,
            artifact_metadata_path(paths.strats_latent_tags_csv),
            paths.strats_input_root / "artifact_manifest.json",
        ]
    if stage == "run-strats":
        return [
            item
            for model in MODELS
            for item in (
                paths.strats_predictions_dir / f"{model}.csv",
                Path(str(paths.strats_predictions_dir / f"{model}.csv") + ".metadata.json"),
            )
        ]
    if stage == "collect-strats":
        return [
            item
            for model in MODELS
            for item in (
                paths.predicted_raw_dir / f"{model}.csv",
                artifact_metadata_path(paths.predicted_raw_dir / f"{model}.csv"),
                Path(str(paths.predicted_raw_dir / f"{model}.csv") + ".metadata.json"),
            )
        ]
    if stage == "normalize-predictions":
        return [
            item
            for model in ("rules", *MODELS)
            for item in (
                paths.voters_dir / f"{model}.csv",
                artifact_metadata_path(paths.voters_dir / f"{model}.csv"),
            )
        ]
    if stage == "thesis-main":
        return [paths.thesis_main_output_dir]
    raise ValueError(f"Unsupported stage output contract: {stage}")



def _stage_receipt_path(context: RouterContext, stage: str) -> Path:
    return context.config_dir / "stage_receipts" / f"{stage}.json"


def write_stage_receipt(
    context: RouterContext,
    stage: str,
    result: StageResult,
) -> Path:
    output_paths = list(result.details.get("outputs", []))
    if not output_paths:
        raise ValueError(f"Stage {stage} produced no receipt-bound outputs.")
    expected_paths = {
        str(path.resolve()) for path in _expected_stage_output_paths(context, stage)
    }
    actual_paths = [str(Path(path).resolve()) for path in output_paths]
    if len(actual_paths) != len(set(actual_paths)) or set(actual_paths) != expected_paths:
        raise ValueError(
            f"Stage {stage} output contract mismatch: "
            f"missing={sorted(expected_paths - set(actual_paths))} "
            f"extra={sorted(set(actual_paths) - expected_paths)}"
        )
    receipt = {
        "stage": stage,
        "status": result.status,
        "run_id": context.run_id,
        "dataset": next(iter(context.datasets)),
        "plan_fingerprint": context.plan_fingerprint,
        "producer_version": ROUTER_PRODUCER_VERSION,
        "inputs": _stage_input_descriptors(context, stage),
        "outputs": [_fingerprint_output(value) for value in output_paths],
        "created_at": utc_now(),
    }
    path = _stage_receipt_path(context, stage)
    write_json(path, receipt)
    return path


def validate_stage_receipt(context: RouterContext, stage: str) -> dict[str, Any]:
    path = _stage_receipt_path(context, stage)
    receipt = _load_json(path)
    expected = {
        "stage": stage,
        "run_id": context.run_id,
        "dataset": next(iter(context.datasets)),
        "plan_fingerprint": context.plan_fingerprint,
        "producer_version": ROUTER_PRODUCER_VERSION,
    }
    mismatches = {
        key: (receipt.get(key), value)
        for key, value in expected.items()
        if receipt.get(key) != value
    }
    if mismatches:
        raise ValueError(f"Stage reuse receipt mismatch for {stage}: {mismatches}")
    receipt_inputs = receipt.get("inputs")
    receipt_outputs = receipt.get("outputs")
    if not isinstance(receipt_inputs, list) or not receipt_inputs:
        raise ValueError(f"Stage reuse receipt has no bound inputs for {stage}.")
    if not isinstance(receipt_outputs, list) or not receipt_outputs:
        raise ValueError(f"Stage reuse receipt has no bound outputs for {stage}.")
    current_inputs = _stage_input_descriptors(context, stage)
    if receipt_inputs != current_inputs:
        raise ValueError(f"Stage reuse input mismatch for {stage}.")
    expected_paths = {
        str(path.resolve()) for path in _expected_stage_output_paths(context, stage)
    }
    receipt_paths = [descriptor.get("path") for descriptor in receipt_outputs]
    if (
        len(receipt_paths) != len(set(receipt_paths))
        or set(receipt_paths) != expected_paths
    ):
        raise ValueError(f"Stage reuse output set mismatch for {stage}.")
    for descriptor in receipt_outputs:
        current = _fingerprint_output(descriptor["path"])
        if current != descriptor:
            raise ValueError(
                f"Stage reuse output mismatch for {stage}: {descriptor['path']}"
            )
    return receipt


def execute_plan(context: RouterContext) -> None:
    total = len(context.args.stages)
    for index, stage in enumerate(context.args.stages, start=1):
        print_stage(index, total, stage)
        if context.args.resume:
            manifest = _load_json(context.manifest_path)
            prior_status = manifest.get("stages", {}).get(stage, {}).get("status")
            if prior_status in {"completed", "skipped"}:
                receipt = validate_stage_receipt(context, stage)
                update_dataset_manifest(
                    context,
                    stage=stage,
                    status="skipped",
                    details={
                        "reason": "resume receipt and output fingerprints matched",
                        "reused_receipt": str(_stage_receipt_path(context, stage)),
                        "original_status": receipt.get("status"),
                    },
                )
                continue
        planned_command = sanitize_command(_planned_stage_command(context, stage))
        attempted_inputs: list[str] = []
        try:
            input_paths = _stage_input_paths(context, stage)
            attempted_inputs = [str(path) for path in input_paths]
            stage_inputs = [_fingerprint_input(path) for path in input_paths]
            update_dataset_manifest(
                context,
                stage=stage,
                status="running",
                details={
                    "command": planned_command,
                    "inputs": stage_inputs,
                },
            )
            result = _execute_stage(context, stage)
            receipt = write_stage_receipt(context, stage, result)
            result.details.setdefault("command", planned_command)
            result.details.setdefault("inputs", stage_inputs)
            result.details["receipt"] = str(receipt)
        except BaseException as exc:
            summary = f"{type(exc).__name__}: {exc}"
            failure_details: dict[str, Any] = {
                "failure_summary": summary,
                "command": planned_command,
                "inputs": attempted_inputs,
            }
            if isinstance(exc, CommandExecutionError):
                failure_details.update(
                    {
                        "command": sanitize_command(exc.command),
                        "exit_code": exc.returncode,
                        "log_path": str(exc.log_path),
                    }
                )
            update_dataset_manifest(
                context,
                stage=stage,
                status="failed",
                details=failure_details,
                overall_status="failed",
                failure_summary=summary,
            )
            raise
        update_dataset_manifest(
            context,
            stage=stage,
            status=result.status,
            details=result.details,
        )
    update_dataset_manifest(context, overall_status="completed")


def run_single_dataset(context: RouterContext) -> int:
    if not context.args.resume:
        initialize_dataset_run(context)
    else:
        initialize_dataset_run(context)
    try:
        execute_plan(context)
    except BaseException:
        if context.manifest_path.exists():
            manifest = _load_json(context.manifest_path)
            if manifest.get("status") not in {"failed", "cancelled"}:
                update_dataset_manifest(
                    context,
                    overall_status="failed",
                    failure_summary=traceback.format_exc(limit=8),
                )
        raise
    return 0


def _append_option(command: list[str], option: str, value: Any) -> None:
    if value is not None:
        command.extend([option, str(value)])


def build_child_command(
    args: argparse.Namespace,
    dataset: str,
    context: RouterContext,
    assignment: GPUAssignment,
) -> list[str]:
    paths = context.datasets[dataset]
    command = [
        str(args.python_executable),
        str((WORKSPACE_ROOT / "router.py").resolve()),
        "--dataset",
        dataset,
        "--run-id",
        args.run_id,
        "--output-root",
        str(context.run_root.parent),
        "--thesis-repo-root",
        str(context.thesis_repo_root),
        "--strats-repo-root",
        str(context.strats_repo_root),
        "--strats-script-path",
        str(args.strats_script_path),
        "--stages",
        ",".join(args.stages),
        "--seed",
        str(args.seed),
        "--python-executable",
        str(args.python_executable),
        "--preprocess-chunksize",
        str(args.preprocess_chunksize),
        "--strats-max-concurrent",
        str(assignment.max_concurrent),
        "--run-strats",
        "true" if args.run_strats else "false",
        "--strats-train-frac",
        str(args.strats_train_frac),
        "--strats-model-run",
        args.strats_model_run,
        "--dataset-child",
        "--dataset-run-dir",
        str(context.run_dir),
        "--coordinator-run-root",
        str(context.run_root),
        "--parent-plan-fingerprint",
        context.plan_fingerprint,
        "--gpu-lock-path",
        str(assignment.lock_path),
    ]
    if assignment.physical is not None:
        command.extend(["--assigned-gpu", assignment.physical])
    for flag, enabled in [
        ("--resume", args.resume),
        ("--skip-existing", args.skip_existing),
        ("--fail-fast", args.fail_fast),
        ("--verbose", args.verbose),
        ("--allow-existing-strats-inputs", args.allow_existing_strats_inputs),
    ]:
        if enabled:
            command.append(flag)
    for option, value in [
        ("--cate-model", args.cate_model),
        ("--down-sample", args.down_sample),
        ("--trials", args.trials),
        ("--use-expanded-safe-confounders", args.use_expanded_safe_confounders),
        (f"--{dataset}-raw-data-path", paths.raw_data_path if getattr(args, f"{dataset}_raw_data_path") is not None else None),
        (f"--{dataset}-config-csv", paths.config_csv),
        (f"--{dataset}-thesis-pkl", paths.thesis_input_pkl if getattr(args, f"{dataset}_thesis_pkl") is not None else None),
        (f"--{dataset}-rule-tags-csv", paths.rule_input_csv if getattr(args, f"{dataset}_rule_tags_csv") is not None else None),
        (
            f"--{dataset}-decision-trees-pkl",
            paths.decision_trees_input_pkl if getattr(args, f"{dataset}_decision_trees_pkl") is not None else None,
        ),
        (
            f"--{dataset}-strats-input-dir",
            paths.strats_input_root if getattr(args, f"{dataset}_strats_input_dir") is not None else None,
        ),
        (
            f"--{dataset}-strats-output-dir",
            paths.strats_output_root if getattr(args, f"{dataset}_strats_output_dir") is not None else None,
        ),
        (f"--{dataset}-voters-dir", paths.voters_input_dir if getattr(args, f"{dataset}_voters_dir") is not None else None),
    ]:
        if value is not None:
            command.extend([option, str(value)])
    return command


def _process_running(process: Any) -> bool:
    try:
        return process.poll() is None
    except Exception:
        return True


def terminate_children(
    processes: dict[str, Any], *, kill_after: float = 5.0
) -> dict[str, int | None]:
    """Terminate live children, wait for every child, and return observed exit codes."""

    for process in processes.values():
        if not _process_running(process):
            continue
        try:
            if hasattr(os, "killpg"):
                os.killpg(process.pid, signal.SIGTERM)
            else:
                process.terminate()
        except (ProcessLookupError, OSError, AttributeError):
            try:
                process.terminate()
            except Exception:
                pass

    deadline = time.monotonic() + kill_after
    exit_codes: dict[str, int | None] = {}
    for dataset, process in processes.items():
        timeout = max(0.0, deadline - time.monotonic())
        try:
            return_code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            try:
                if hasattr(os, "killpg"):
                    os.killpg(process.pid, signal.SIGKILL)
                else:
                    process.kill()
            except (ProcessLookupError, OSError, AttributeError):
                try:
                    process.kill()
                except Exception:
                    pass
            try:
                return_code = process.wait(timeout=kill_after)
            except Exception:
                return_code = process.poll()
        except Exception:
            return_code = process.poll()
        exit_codes[dataset] = (
            int(return_code) if return_code is not None else None
        )
    return exit_codes


@contextmanager
def coordinator_signal_handlers(processes: dict[str, Any]):
    previous: dict[int, Any] = {}

    def handler(signum: int, frame: Any) -> None:
        del frame
        terminate_children(processes)
        raise CoordinatorInterrupted(signum)

    try:
        for signum in (signal.SIGINT, signal.SIGTERM):
            previous[signum] = signal.getsignal(signum)
            signal.signal(signum, handler)
        yield
    finally:
        for signum, old_handler in previous.items():
            signal.signal(signum, old_handler)


def _load_child_manifest(context: RouterContext) -> dict[str, Any] | None:
    if not context.manifest_path.is_file():
        return None
    try:
        return _load_json(context.manifest_path)
    except Exception:
        return None


def _write_terminal_child_manifest(
    context: RouterContext,
    status: str,
    exit_code: int | None,
    summary: str,
    *,
    pid: int | None = None,
) -> dict[str, Any]:
    if status not in {"failed", "cancelled"}:
        raise ValueError(f"Unsupported fallback child status: {status}")
    dataset = next(iter(context.datasets))
    manifest = _load_child_manifest(context)
    if manifest is None:
        context.run_dir.mkdir(parents=True, exist_ok=True)
        manifest = {
            "kind": "dataset",
            "dataset": dataset,
            "run_id": context.run_id,
            "pid": pid,
            "plan_fingerprint": context.plan_fingerprint,
            "config_fingerprint": context.config_fingerprints[dataset],
            "base_seed": context.args.seed,
            "start_time": None,
            "run_path": str(context.run_dir),
            "manifest_path": str(context.manifest_path),
            "logs_path": str(context.logs_dir),
            "gpu": _gpu_payload(context.gpu_assignment),
            "stages": {},
        }
    elif pid is not None and manifest.get("pid") is None:
        manifest["pid"] = pid

    terminal_stage_statuses = {"completed", "failed", "skipped", "cancelled"}
    stages = manifest.setdefault("stages", {})
    for stage in context.args.stages:
        record = stages.setdefault(
            stage,
            {
                "status": "pending",
                "command": None,
                "inputs": [],
                "outputs": [],
                "start_time": None,
                "finish_time": None,
                "failure_summary": None,
            },
        )
        if not isinstance(record, dict):
            record = {"status": "pending"}
            stages[stage] = record
        if record.get("status") not in terminal_stage_statuses:
            record["status"] = status
            record["finish_time"] = utc_now()
            record["failure_summary"] = summary

    manifest["status"] = status
    manifest["finish_time"] = utc_now()
    manifest["failure_summary"] = summary
    manifest["exit_code"] = exit_code
    manifest.setdefault("gpu", _gpu_payload(context.gpu_assignment))
    write_json(context.manifest_path, manifest)
    return manifest


def _write_fallback_child_failure(
    context: RouterContext,
    exit_code: int | None,
    summary: str,
) -> None:
    _write_terminal_child_manifest(context, "failed", exit_code, summary)


def _reconcile_child_result(
    manifest_path: Path,
    dataset: str,
    context: RouterContext,
    return_code: int | None,
    *,
    forced_status: str | None = None,
    forced_summary: str | None = None,
    pid: int | None = None,
) -> str:
    child_manifest = _load_child_manifest(context)
    completed = (
        return_code == 0
        and child_manifest is not None
        and child_manifest.get("status") == "completed"
    )
    if completed:
        status = "completed"
        child_manifest["exit_code"] = 0
        write_json(context.manifest_path, child_manifest)
    else:
        status = forced_status or "failed"
        if forced_summary is not None:
            failure_summary = forced_summary
        elif return_code == 0:
            manifest_status = (
                child_manifest.get("status") if child_manifest is not None else None
            )
            failure_summary = (
                "Child exited zero without a completed dataset manifest; "
                f"manifest status={manifest_status!r}."
            )
        elif return_code is None:
            failure_summary = "Child exit code is unavailable before manifest finalization."
        else:
            failure_summary = f"Child exited with code {return_code}."
        child_manifest = _write_terminal_child_manifest(
            context,
            status,
            return_code,
            failure_summary,
            pid=pid,
        )

    child_gpu = child_manifest.get("gpu", _gpu_payload(context.gpu_assignment))
    stage_statuses = {
        name: record.get("status")
        for name, record in child_manifest.get("stages", {}).items()
        if isinstance(record, dict)
    }
    update_coordinator_child(
        manifest_path,
        dataset,
        status,
        gpu=child_gpu,
        exit_code=return_code,
        stage_statuses=stage_statuses,
        failure_summary=child_manifest.get("failure_summary"),
    )
    return status


def coordinate_both(
    args: argparse.Namespace,
    contexts: dict[str, RouterContext],
    policy: GPUPolicy,
    fingerprint: str,
) -> int:
    run_root = next(iter(contexts.values())).run_root
    reserve_top_level_root(args, run_root)
    manifest_path = initialize_coordinator(args, contexts, policy, fingerprint)
    processes: dict[str, Any] = {}
    log_handles: dict[str, Any] = {}
    recorded: dict[str, str] = {}
    try:
        with coordinator_signal_handlers(processes):
            for dataset in DATASETS:
                context = contexts[dataset]
                assignment = policy.assignments[dataset]
                command = build_child_command(args, dataset, context, assignment)
                update_coordinator_child(
                    manifest_path,
                    dataset,
                    "starting",
                    command=sanitize_command(command),
                    start_time=utc_now(),
                )
                log_path = run_root / "coordinator" / "logs" / f"{dataset}.log"
                handle = log_path.open("a", encoding="utf-8")
                log_handles[dataset] = handle
                child_env = dict(os.environ)
                child_env["CLINICAUSE_DATASET_CHILD"] = "1"
                if assignment.physical is not None:
                    child_env["CUDA_VISIBLE_DEVICES"] = assignment.physical
                process = subprocess.Popen(
                    command,
                    cwd=str(WORKSPACE_ROOT),
                    stdout=handle,
                    stderr=subprocess.STDOUT,
                    text=True,
                    env=child_env,
                    start_new_session=True,
                )
                processes[dataset] = process
                update_coordinator_child(
                    manifest_path,
                    dataset,
                    "running",
                    pid=process.pid,
                )

            pending = set(processes)
            while pending:
                ready: list[tuple[str, int]] = []
                for dataset in DATASETS:
                    if dataset not in pending:
                        continue
                    return_code = processes[dataset].poll()
                    if return_code is not None:
                        ready.append((dataset, int(return_code)))
                if not ready:
                    time.sleep(0.05)
                    continue

                failed_dataset: str | None = None
                for dataset, polled_code in ready:
                    waited_code = processes[dataset].wait()
                    return_code = (
                        int(waited_code) if waited_code is not None else polled_code
                    )
                    status = _reconcile_child_result(
                        manifest_path,
                        dataset,
                        contexts[dataset],
                        return_code,
                        pid=processes[dataset].pid,
                    )
                    recorded[dataset] = status
                    pending.remove(dataset)
                    if status == "failed" and failed_dataset is None:
                        failed_dataset = dataset

                if failed_dataset is not None and args.fail_fast:
                    raced: list[tuple[str, int]] = []
                    for dataset in DATASETS:
                        if dataset not in pending:
                            continue
                        return_code = processes[dataset].poll()
                        if return_code is not None:
                            raced.append((dataset, int(return_code)))
                    for dataset, polled_code in raced:
                        waited_code = processes[dataset].wait()
                        return_code = (
                            int(waited_code) if waited_code is not None else polled_code
                        )
                        status = _reconcile_child_result(
                            manifest_path,
                            dataset,
                            contexts[dataset],
                            return_code,
                            pid=processes[dataset].pid,
                        )
                        recorded[dataset] = status
                        pending.remove(dataset)

                    live = {
                        dataset: processes[dataset]
                        for dataset in DATASETS
                        if dataset in pending
                    }
                    exit_codes = terminate_children(live)
                    for dataset in DATASETS:
                        if dataset not in pending:
                            continue
                        status = _reconcile_child_result(
                            manifest_path,
                            dataset,
                            contexts[dataset],
                            exit_codes.get(dataset),
                            forced_status="cancelled",
                            forced_summary=(
                                f"Cancelled after sibling {failed_dataset} failed."
                            ),
                            pid=processes[dataset].pid,
                        )
                        recorded[dataset] = status
                    pending.clear()
                    break
    except CoordinatorInterrupted as exc:
        exit_codes = terminate_children(processes)
        for dataset in DATASETS:
            if dataset in recorded:
                continue
            process = processes.get(dataset)
            status = _reconcile_child_result(
                manifest_path,
                dataset,
                contexts[dataset],
                exit_codes.get(dataset),
                forced_status="cancelled",
                forced_summary=str(exc),
                pid=process.pid if process is not None else None,
            )
            recorded[dataset] = status
        finalize_coordinator(manifest_path, "cancelled")
        return 128 + exc.signum
    except BaseException as exc:
        exit_codes = terminate_children(processes)
        for dataset in DATASETS:
            if dataset in recorded:
                continue
            process = processes.get(dataset)
            launched = process is not None
            status = _reconcile_child_result(
                manifest_path,
                dataset,
                contexts[dataset],
                exit_codes.get(dataset),
                forced_status="cancelled" if launched else "failed",
                forced_summary=(
                    f"Coordinator failure: {type(exc).__name__}: {exc}"
                    if launched
                    else f"Failed before launch: {type(exc).__name__}: {exc}"
                ),
                pid=process.pid if process is not None else None,
            )
            recorded[dataset] = status
        finalize_coordinator(manifest_path, "failed")
        raise
    finally:
        for handle in log_handles.values():
            handle.close()

    manifest = _load_json(manifest_path)
    statuses = [child["status"] for child in manifest["children"].values()]
    success = all(status == "completed" for status in statuses)
    finalize_coordinator(manifest_path, "completed" if success else "failed")
    return 0 if success else 1

def print_preview(
    args: argparse.Namespace,
    contexts: dict[str, RouterContext],
    policy: GPUPolicy,
) -> None:
    print("[router] Read-only plan validation passed.")
    if args.dataset == "both":
        for dataset in DATASETS:
            command = build_child_command(
                args, dataset, contexts[dataset], policy.assignments[dataset]
            )
            print(f"[router] child {dataset}: {shlex.join(sanitize_command(command))}")
    else:
        context = next(iter(contexts.values()))
        print(
            f"[router] dataset={next(iter(context.datasets))} "
            f"run_dir={context.run_dir} stages={','.join(args.stages)}"
        )


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    contexts, policy, fingerprint = preflight(args)
    if args.validate_only or args.dry_run:
        print_preview(args, contexts, policy)
        return 0
    run_root = next(iter(contexts.values())).run_root
    if args.dataset == "both":
        return coordinate_both(args, contexts, policy, fingerprint)

    context = next(iter(contexts.values()))
    if not args.dataset_child:
        reserve_top_level_root(args, run_root)
    return run_single_dataset(context)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - command-line failure reporting
        print(f"[router] ERROR: {exc}")
        traceback.print_exc()
        raise

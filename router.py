from __future__ import annotations

import argparse
import csv
import json
import os
import pickle
import shlex
import shutil
import subprocess
import sys
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


WORKSPACE_ROOT = Path(__file__).resolve().parent
THESIS_REPO_CANDIDATES = [
    WORKSPACE_ROOT / "causal-irregular-time-series",
    WORKSPACE_ROOT,
]
STRATS_REPO_CANDIDATES = [
    WORKSPACE_ROOT / "STraTS",
    WORKSPACE_ROOT.parent / "STraTS",
]


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


@dataclass
class DatasetPaths:
    dataset: str
    thesis_dataset: str
    strats_dataset: str
    config_csv: Path
    resolved_config_csv: Path
    thesis_processed_pkl: Path
    strats_processed_pkl: Path
    rule_latent_tags_csv: Path
    rule_decision_trees_pkl: Path
    tree_plots_dir: Path
    predicted_raw_dir: Path
    voters_dir: Path
    thesis_main_output_dir: Path


@dataclass
class RouterContext:
    run_id: str
    run_dir: Path
    thesis_repo_root: Path
    strats_repo_root: Path
    logs_dir: Path
    datasets: dict[str, DatasetPaths]
    args: argparse.Namespace
    manifest_path: Path
    config_dir: Path


def parse_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "f", "no", "n", "off"}:
        return False
    raise argparse.ArgumentTypeError(f"Invalid boolean value: {value!r}")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Orchestrate the thesis + STraTS unified pipeline.")
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
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--python-executable", default=sys.executable)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--allow-existing-strats-inputs", action="store_true")
    parser.add_argument("--run-strats", default=None, type=parse_bool)
    args = parser.parse_args(list(argv) if argv is not None else None)

    stages = normalize_stage_list(args.stages)
    args.stages = stages
    if args.run_strats is None:
        args.run_strats = "run-strats" in stages or stages == STAGE_ORDER
    return args


def normalize_stage_list(stages: str | Iterable[str]) -> list[str]:
    if isinstance(stages, str):
        raw_parts = [part.strip() for part in stages.split(",") if part.strip()]
    else:
        raw_parts = [str(part).strip() for part in stages if str(part).strip()]
    if not raw_parts:
        raise ValueError("No stages were selected.")
    if len(raw_parts) == 1 and raw_parts[0].lower() == "all":
        return list(STAGE_ORDER)
    normalized: list[str] = []
    for part in raw_parts:
        if part.lower() == "all":
            return list(STAGE_ORDER)
        if part.lower() not in SUPPORTED_STAGES:
            raise ValueError(f"Unsupported stage {part!r}; expected one of {sorted(SUPPORTED_STAGES)}")
        normalized.append(part.lower())
    return normalized


def resolve_repo_root(explicit: str | None, candidates: Iterable[Path], expected_marker: str) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
    else:
        for candidate in candidates:
            if (candidate / expected_marker).exists():
                return candidate.resolve()
        for candidate in candidates:
            if candidate.exists():
                return candidate.resolve()
        raise FileNotFoundError(f"Could not locate repository root for {expected_marker!r}")
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    return path.resolve()


def selected_datasets(args: argparse.Namespace) -> list[str]:
    if args.dataset == "both":
        return ["physionet", "mimic"]
    return [args.dataset]


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def maybe_remove(path: Path) -> None:
    if path.exists():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()


def build_stage_log_path(run_dir: Path, stage_name: str, dataset: str | None = None) -> Path:
    log_dir = run_dir / "logs"
    ensure_directory(log_dir)
    if dataset is None:
        return log_dir / f"{stage_name}.log"
    return log_dir / f"{stage_name}_{dataset}.log"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_directory(path.parent)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def write_resolved_config(path: Path, dataset: str, config: dict[str, Any], args: argparse.Namespace) -> None:
    ensure_directory(path.parent)
    rows: list[dict[str, Any]] = []
    row: dict[str, Any] = {}

    for key in [
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
    ]:
        if key in config:
            row[key] = config[key]

    if args.cate_model is not None:
        row["MODEL_TYPE"] = args.cate_model
    if args.down_sample is not None:
        row["DOWN_SAMPLE"] = args.down_sample.lower() == "true"
    if args.trials is not None:
        row["TRIALS"] = args.trials
    if args.use_expanded_safe_confounders is not None:
        row["USE_EXPANDED_SAFE_CONFOUNDERS"] = parse_bool(args.use_expanded_safe_confounders)
    if args.seed is not None:
        row["SEED"] = args.seed
    elif "SEED" not in row:
        row["SEED"] = 42

    rows.append(row)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
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
        ])
        writer.writeheader()
        writer.writerow({key: _stringify_value(row.get(key)) for key in writer.fieldnames})


def _stringify_value(value: Any) -> Any:
    if isinstance(value, (list, tuple, set)):
        return json.dumps(list(value))
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


def initialize_context(args: argparse.Namespace) -> RouterContext:
    thesis_repo_root = resolve_repo_root(args.thesis_repo_root, THESIS_REPO_CANDIDATES, "main.py")
    strats_repo_root = resolve_repo_root(args.strats_repo_root, STRATS_REPO_CANDIDATES, "run_full_main.sh")
    run_dir = (Path(args.output_root).expanduser().resolve() / args.run_id).resolve()
    logs_dir = run_dir / "logs"
    config_dir = run_dir / "config"
    manifest_path = config_dir / "manifest.json"
    ensure_directory(logs_dir)
    ensure_directory(config_dir)

    if not str(thesis_repo_root).endswith("causal-irregular-time-series") and (thesis_repo_root / "main.py").exists():
        pass

    sys.path.insert(0, str(thesis_repo_root))
    from src.dataset_config import load_dataset_config, default_config_path

    datasets: dict[str, DatasetPaths] = {}
    for dataset in selected_datasets(args):
        source_config_path = Path(args.__dict__.get(f"{dataset}_config_csv") or default_config_path(dataset))
        if not source_config_path.is_absolute():
            source_config_path = (thesis_repo_root / source_config_path).resolve()
        if not source_config_path.exists():
            raise FileNotFoundError(f"Dataset config not found for {dataset}: {source_config_path}")
        config = load_dataset_config(dataset, str(source_config_path))
        resolved_config_csv = config_dir / f"{dataset}_resolved_config.csv"
        write_resolved_config(resolved_config_csv, dataset, config, args)

        datasets[dataset] = DatasetPaths(
            dataset=dataset,
            thesis_dataset=dataset,
            strats_dataset={"physionet": "physionet_2012", "mimic": "mimic_iii"}[dataset],
            config_csv=source_config_path,
            resolved_config_csv=resolved_config_csv,
            thesis_processed_pkl=run_dir / "preprocessing" / f"{dataset}_ts_oc_ids.pkl",
            strats_processed_pkl=run_dir / "preprocessing" / "strats" / f"{ {'physionet': 'physionet_2012', 'mimic': 'mimic_iii'}[dataset] }.pkl",
            rule_latent_tags_csv=run_dir / "latent_tags" / "rules" / dataset / "latent_tags.csv",
            rule_decision_trees_pkl=run_dir / "latent_tags" / "rules" / dataset / "latent_decision_trees.pkl",
            tree_plots_dir=run_dir / "decision_tree_plots" / dataset,
            predicted_raw_dir=run_dir / "latent_tags" / "predicted_raw" / dataset,
            voters_dir=run_dir / "latent_tags" / "voters" / dataset,
            thesis_main_output_dir=run_dir / "thesis_main" / dataset,
        )

    return RouterContext(
        run_id=args.run_id,
        run_dir=run_dir,
        thesis_repo_root=thesis_repo_root,
        strats_repo_root=strats_repo_root,
        logs_dir=logs_dir,
        datasets=datasets,
        args=args,
        manifest_path=manifest_path,
        config_dir=config_dir,
    )


def update_manifest(context: RouterContext, stage: str, status: str, details: dict[str, Any] | None = None) -> None:
    manifest_path = context.manifest_path
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "run_id": context.run_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "thesis_repo_root": str(context.thesis_repo_root),
            "strats_repo_root": str(context.strats_repo_root),
            "datasets": list(context.datasets.keys()),
            "stage_statuses": {},
            "commands_run": [],
            "important_paths": {},
            "failure_details": {},
        }
    manifest["stage_statuses"][stage] = {
        "status": status,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        **(details or {}),
    }
    manifest["important_paths"] = {
        "run_dir": str(context.run_dir),
        "config_dir": str(context.config_dir),
        "logs_dir": str(context.logs_dir),
        **manifest.get("important_paths", {}),
    }
    write_json(manifest_path, manifest)


def print_stage(stage_index: int, total: int, stage_name: str) -> None:
    print(f"[router] === Stage {stage_index}/{total}: {stage_name} ===")


def validate_thesis_pickle(path: Path, dataset: str, config_path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"missing thesis pickle: {path}"
    try:
        with path.open("rb") as handle:
            payload = pickle.load(handle)
    except Exception as exc:  # pragma: no cover - runtime path validation
        return False, f"failed to load thesis pickle {path}: {exc}"

    if not isinstance(payload, (list, tuple)) or len(payload) != 3:
        return False, f"thesis pickle {path} did not contain exactly 3 objects"

    ts, oc, ts_ids = payload
    missing_ts_cols = {"ts_id", "minute", "variable", "value"} - set(getattr(ts, "columns", []))
    if missing_ts_cols:
        return False, f"thesis pickle {path} is missing ts columns: {sorted(missing_ts_cols)}"
    if not hasattr(oc, "columns"):
        return False, f"thesis pickle {path} has invalid outcomes payload"
    outcome_col = "in_hospital_mortality"
    if outcome_col not in oc.columns:
        return False, f"thesis pickle {path} is missing outcome column {outcome_col!r}"
    if not ts_ids:
        return False, f"thesis pickle {path} had an empty ts_ids list"
    return True, "ok"


def validate_latent_tags_csv(path: Path, latent_order: list[str]) -> tuple[bool, str]:
    if not path.exists():
        return False, f"missing latent tags csv: {path}"
    try:
        import pandas as pd

        df = pd.read_csv(path)
    except Exception as exc:  # pragma: no cover - runtime path validation
        return False, f"failed to load latent tags csv {path}: {exc}"

    if "ts_id" not in df.columns:
        return False, f"latent tags csv {path} missing ts_id column"
    if df.duplicated("ts_id").any():
        return False, f"latent tags csv {path} has duplicate ts_id values"
    available = [col for col in latent_order if col in df.columns]
    if not available:
        return False, f"latent tags csv {path} did not contain any configured latent columns"
    return True, "ok"


def validate_strats_pickle(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"missing STraTS processed pickle: {path}"
    try:
        with path.open("rb") as handle:
            payload = pickle.load(handle)
    except Exception as exc:  # pragma: no cover - runtime path validation
        return False, f"failed to load STraTS pickle {path}: {exc}"
    if isinstance(payload, dict):
        return False, f"STraTS pickle {path} used unsupported dict format; expected a 5-item list/tuple"
    if not isinstance(payload, (list, tuple)) or len(payload) != 5:
        return False, f"STraTS pickle {path} had unsupported payload shape: expected 5 items"
    data, oc, train_ids, val_ids, test_ids = payload
    if data is None or oc is None:
        return False, f"STraTS pickle {path} has missing data/oc payloads"
    if not isinstance(train_ids, (list, tuple)) or not isinstance(val_ids, (list, tuple)) or not isinstance(test_ids, (list, tuple)):
        return False, f"STraTS pickle {path} has non-list train/val/test ids"
    return True, "ok"


def build_strats_pickle(dataset: str, thesis_pickle_path: Path, strats_pickle_path: Path, seed: int) -> None:
    ensure_directory(strats_pickle_path.parent)
    with thesis_pickle_path.open("rb") as handle:
        ts, oc, ts_ids = pickle.load(handle)

    ids = [str(value) for value in ts.ts_id.unique().tolist()]
    if not ids:
        raise ValueError(f"No ts_ids available for dataset {dataset}")
    import random

    rng = random.Random(seed)
    shuffled = list(ids)
    rng.shuffle(shuffled)
    n = len(shuffled)
    train_n = max(1, int(round(n * 0.64)))
    val_n = max(1, int(round(n * 0.16)))
    test_n = max(1, n - train_n - val_n)
    if train_n + val_n + test_n != n:
        train_n = n - val_n - test_n
    train_ids = shuffled[:train_n]
    val_ids = shuffled[train_n:train_n + val_n]
    test_ids = shuffled[train_n + val_n:train_n + val_n + test_n]
    if not train_ids or not val_ids or not test_ids:
        raise ValueError(f"Generated empty split for dataset {dataset}")
    payload = [ts, oc, train_ids, val_ids, test_ids]
    with strats_pickle_path.open("wb") as handle:
        pickle.dump(payload, handle)


def link_or_copy(src: Path, dst: Path, overwrite: bool = False) -> None:
    ensure_directory(dst.parent)
    if dst.exists() and not overwrite:
        if dst.resolve() == src.resolve():
            return
        raise FileExistsError(f"Refusing to overwrite existing file: {dst}")
    if dst.exists() and overwrite:
        maybe_remove(dst)
    if os.name == "nt":
        shutil.copy2(src, dst)
    else:
        try:
            os.symlink(src, dst)
        except OSError:
            shutil.copy2(src, dst)


def run_command(command: list[str], cwd: Path, log_path: Path, dry_run: bool = False, env: dict[str, str] | None = None) -> None:
    compact = shlex.join(command)
    print(f"[router] DRY RUN: would run command: {compact}") if dry_run else print(f"[router] Running: {compact}")
    ensure_directory(log_path.parent)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"# cwd={cwd}\n")
        handle.write(f"# command={compact}\n")
        if dry_run:
            handle.write("# dry-run; command not executed\n")
            return
        process = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
        )
        assert process.stdout is not None
        for line in process.stdout:
            handle.write(line)
            if not line.endswith("\n"):
                handle.write("\n")
        return_code = process.wait()
        if return_code != 0:
            raise RuntimeError(f"Command failed with exit code {return_code}: {compact}")


def run_preprocessing(dataset: str, context: RouterContext) -> None:
    dataset_paths = context.datasets[dataset]
    script_name = "src/preprocess_physionet_2012.py" if dataset == "physionet" else "src/preprocess_mimic_iii_large.py"
    script_path = context.thesis_repo_root / script_name
    log_path = build_stage_log_path(context.run_dir, "preprocessing", dataset)
    raw_data_path = Path(getattr(context.args, f"{dataset}_raw_data_path") or "")
    if raw_data_path == Path("."):
        raise FileNotFoundError(f"Raw data path for {dataset} is missing: {raw_data_path}")
    if not context.args.dry_run and not raw_data_path.exists():
        raise FileNotFoundError(f"Raw data path for {dataset} is missing: {raw_data_path}")
    command = [
        context.args.python_executable,
        str(script_path),
        "--dataset-config-csv",
        str(dataset_paths.resolved_config_csv),
        "--raw-data-path",
        str(raw_data_path),
        "--output-path",
        str(dataset_paths.thesis_processed_pkl),
    ]
    if dataset == "physionet":
        command.extend(["--processed-dir", str(dataset_paths.thesis_processed_pkl.parent)])
    if context.args.dry_run:
        run_command(command, context.thesis_repo_root, log_path, dry_run=True)
        return
    if context.args.skip_existing and validate_thesis_pickle(dataset_paths.thesis_processed_pkl, dataset, dataset_paths.resolved_config_csv)[0]:
        print(f"[router] Skipping preprocessing for {dataset} because output already exists and passed validation.")
        return
    run_command(command, context.thesis_repo_root, log_path)


def run_tagging(dataset: str, context: RouterContext) -> None:
    dataset_paths = context.datasets[dataset]
    if dataset == "physionet":
        script_path = context.thesis_repo_root / "src" / "tagging_latent_variables_physionet.py"
        command = [
            context.args.python_executable,
            str(script_path),
            "--dataset-config-csv",
            str(dataset_paths.resolved_config_csv),
            "--pkl-path",
            str(dataset_paths.thesis_processed_pkl),
            "--output-csv-path",
            str(dataset_paths.rule_latent_tags_csv),
        ]
    else:
        script_path = context.thesis_repo_root / "src" / "tagging_latent_variables_mimiciii.py"
        command = [
            context.args.python_executable,
            str(script_path),
            "--dataset-config-csv",
            str(dataset_paths.resolved_config_csv),
            "--pkl_path",
            str(dataset_paths.thesis_processed_pkl),
            "--output_dir",
            str(dataset_paths.rule_latent_tags_csv.parent),
        ]
    log_path = build_stage_log_path(context.run_dir, "tagging", dataset)
    with dataset_paths.resolved_config_csv.open("r", encoding="utf-8") as handle:
        config_row = next(csv.DictReader(handle))
    latent_order = [item for item in json.loads(config_row.get("LATENT_ORDER", "[]")) if item]
    if context.args.dry_run:
        run_command(command, context.thesis_repo_root, log_path, dry_run=True)
        return
    if context.args.skip_existing and validate_latent_tags_csv(dataset_paths.rule_latent_tags_csv, latent_order)[0]:
        print(f"[router] Skipping tagging for {dataset} because output already exists and passed validation.")
        update_manifest(context, "tagging", "skipped", {"dataset": dataset, "reason": "skip-existing validation passed", "path": str(dataset_paths.rule_latent_tags_csv)})
        return
    run_command(command, context.thesis_repo_root, log_path)


def run_tree_plots(dataset: str, context: RouterContext) -> None:
    dataset_paths = context.datasets[dataset]
    script_path = context.thesis_repo_root / "src" / "decision_trees_plot.py"
    log_path = build_stage_log_path(context.run_dir, "trees", dataset)
    command = [
        context.args.python_executable,
        str(script_path),
        "--dataset",
        dataset,
        "--dataset-config-csv",
        str(dataset_paths.resolved_config_csv),
        "--pickle-path",
        str(dataset_paths.rule_decision_trees_pkl),
        "--output-dir",
        str(dataset_paths.tree_plots_dir),
        "--format",
        "png",
        "--overwrite",
    ]
    if context.args.dry_run:
        run_command(command, context.thesis_repo_root, log_path, dry_run=True)
        return
    run_command(command, context.thesis_repo_root, log_path)


def prepare_strats_filesystem(context: RouterContext) -> None:
    if context.args.dry_run:
        print("[router] DRY RUN: would prepare STraTS filesystem.")
        return
    print("[router] Preparing STraTS filesystem.")
    ensure_directory(context.strats_repo_root / "data" / "processed")
    ensure_directory(context.strats_repo_root / "outputs")
    for dataset in context.datasets:
        dataset_paths = context.datasets[dataset]
        strats_dataset_name = dataset_paths.strats_dataset
        rule_src = dataset_paths.rule_latent_tags_csv
        rule_dst = context.strats_repo_root / "data" / f"{dataset}_latent_tags.csv"
        link_or_copy(rule_src, rule_dst, overwrite=context.args.overwrite)

        strats_pickle_dst = context.strats_repo_root / "data" / "processed" / f"{strats_dataset_name}.pkl"
        build_strats_pickle(dataset, dataset_paths.thesis_processed_pkl, dataset_paths.strats_processed_pkl, context.args.seed or 42)
        link_or_copy(dataset_paths.strats_processed_pkl, strats_pickle_dst, overwrite=context.args.overwrite)


def validate_strats_inputs(context: RouterContext) -> None:
    if not context.args.run_strats:
        return
    for dataset in context.datasets:
        rule_target = context.strats_repo_root / "data" / f"{dataset}_latent_tags.csv"
        processed_target = context.strats_repo_root / "data" / "processed" / f"{context.datasets[dataset].strats_dataset}.pkl"
        if not rule_target.exists() or not processed_target.exists():
            if context.args.allow_existing_strats_inputs:
                if rule_target.exists() and processed_target.exists():
                    continue
            raise FileNotFoundError(f"Validation failed: missing STraTS input file for {dataset}: {rule_target} or {processed_target}")


def run_strats_script(context: RouterContext) -> None:
    if context.args.run_strats is False:
        print("[router] Skipping STraTS execution because --run-strats false was provided.")
        update_manifest(context, "run-strats", "skipped", {"reason": "--run-strats false"})
        return
    if not context.args.dry_run:
        validate_strats_inputs(context)
    script_path = Path(context.args.strats_script_path)
    if not script_path.is_absolute():
        script_path = (context.strats_repo_root / script_path).resolve()
    if not script_path.exists():
        raise FileNotFoundError(f"STraTS script not found: {script_path}")
    log_path = build_stage_log_path(context.run_dir, "run_strats")
    command = ["bash", str(script_path)]
    env = {**os.environ, "PYTHON": str(context.args.python_executable), "DATASET_SCOPE": ",".join(sorted(context.datasets.keys()))}
    if context.args.dry_run:
        run_command(command, context.strats_repo_root, log_path, dry_run=True, env=env)
        return
    run_command(command, context.strats_repo_root, log_path, env=env)


def collect_strats_outputs(context: RouterContext) -> None:
    if context.args.dry_run:
        print("[router] DRY RUN: would collect raw prediction CSVs.")
        return
    print("[router] Collecting raw prediction CSVs.")
    predictions = {
        "physionet": [
            ("strats", "predicted_physionet_latent_tags_strats.csv"),
            ("gru", "predicted_physionet_latent_tags_gru.csv"),
            ("grud", "predicted_physionet_latent_tags_grud.csv"),
            ("tcn", "predicted_physionet_latent_tags_tcn.csv"),
            ("sand", "predicted_physionet_latent_tags_sand.csv"),
        ],
        "mimic": [
            ("strats", "predicted_latent_tags_strats_mimic.csv"),
            ("gru", "predicted_latent_tags_gru_mimic.csv"),
            ("grud", "predicted_latent_tags_grud_mimic.csv"),
            ("tcn", "predicted_latent_tags_tcn_mimic.csv"),
            ("sand", "predicted_latent_tags_sand_mimic.csv"),
        ],
    }
    for dataset in context.datasets:
        pairs = predictions[dataset]
        for model_name, filename in pairs:
            src = context.strats_repo_root / "outputs" / filename
            dst = context.datasets[dataset].predicted_raw_dir / f"{model_name}.csv"
            if src.exists():
                link_or_copy(src, dst, overwrite=context.args.overwrite)
            else:
                raise FileNotFoundError(f"Expected STraTS prediction file not found: {src}")


def normalize_prediction_csvs(context: RouterContext) -> None:
    if context.args.dry_run:
        print("[router] DRY RUN: would normalize prediction CSVs.")
        return
    import pandas as pd

    for dataset in context.datasets:
        dataset_paths = context.datasets[dataset]
        dataset_paths.voters_dir.mkdir(parents=True, exist_ok=True)
        latent_order = []
        config = {}
        with dataset_paths.resolved_config_csv.open("r", encoding="utf-8") as handle:
            row = next(csv.DictReader(handle))
            latent_order = [item for item in json.loads(row.get("LATENT_ORDER", "[]")) if item]
            config = row
        for model_name in ["rules", "strats", "gru", "grud", "tcn", "sand"]:
            if model_name == "rules":
                src_path = dataset_paths.rule_latent_tags_csv
            else:
                src_path = dataset_paths.predicted_raw_dir / f"{model_name}.csv"
            if not src_path.exists():
                raise FileNotFoundError(f"Missing raw prediction CSV for normalization: {src_path}")
            df = pd.read_csv(src_path)
            if "ts_id" not in df.columns:
                raise ValueError(f"Missing ts_id in {src_path}")
            if df["ts_id"].duplicated().any():
                raise ValueError(f"Duplicate ts_id values found in {src_path}")
            df = df[["ts_id"] + [col for col in df.columns if col != "ts_id" and not col.endswith("_prob")]]
            for col in [c for c in df.columns if c != "ts_id"]:
                values = pd.to_numeric(df[col], errors="coerce")
                unique_values = sorted({value for value in values.dropna().unique().tolist() if value in {0, 1}})
                if len(unique_values) > 2 or any(value not in {0, 1} for value in values.dropna().unique().tolist()):
                    raise ValueError(f"Column {col} in {src_path} is not binary")
                df[col] = values.fillna(0).astype(int)
            missing = [col for col in latent_order if col not in df.columns]
            if missing:
                raise ValueError(f"Missing latent columns {missing} while normalizing {src_path}")
            df = df[["ts_id"] + [col for col in latent_order if col in df.columns]]
            dst_path = dataset_paths.voters_dir / f"{model_name}.csv"
            df.to_csv(dst_path, index=False)


def run_thesis_main(dataset: str, context: RouterContext) -> None:
    dataset_paths = context.datasets[dataset]
    command = [
        context.args.python_executable,
        str(context.thesis_repo_root / "main.py"),
        "--dataset",
        dataset,
        "--dataset-config-csv",
        str(dataset_paths.resolved_config_csv),
        "--latent-tags-dir",
        str(dataset_paths.voters_dir),
        "--dataset-pkl-path",
        str(dataset_paths.thesis_processed_pkl),
        "--output-dir",
        str(dataset_paths.thesis_main_output_dir),
    ]
    if context.args.cate_model is not None:
        command.extend(["--model-type", context.args.cate_model])
    log_path = build_stage_log_path(context.run_dir, "thesis_main", dataset)
    if context.args.dry_run:
        run_command(command, context.thesis_repo_root, log_path, dry_run=True)
        return
    run_command(command, context.thesis_repo_root, log_path)
    summary_path = dataset_paths.thesis_main_output_dir / "run_summary.json"
    if not summary_path.exists():
        raise FileNotFoundError(f"Expected thesis main summary not found: {summary_path}")


def create_run_dirs(context: RouterContext) -> None:
    ensure_directory(context.run_dir)
    ensure_directory(context.run_dir / "config")
    ensure_directory(context.run_dir / "logs")
    ensure_directory(context.run_dir / "preprocessing" / "strats")
    ensure_directory(context.run_dir / "latent_tags" / "rules")
    ensure_directory(context.run_dir / "latent_tags" / "predicted_raw")
    ensure_directory(context.run_dir / "latent_tags" / "voters")
    ensure_directory(context.run_dir / "decision_tree_plots")
    ensure_directory(context.run_dir / "thesis_main")
    for dataset_path in context.datasets.values():
        ensure_directory(dataset_path.rule_latent_tags_csv.parent)
        ensure_directory(dataset_path.tree_plots_dir)
        ensure_directory(dataset_path.predicted_raw_dir)
        ensure_directory(dataset_path.voters_dir)
        ensure_directory(dataset_path.thesis_main_output_dir)


def stage_index(stages: Iterable[str], name: str) -> int | None:
    stage_names = list(stages)
    try:
        return stage_names.index(name)
    except ValueError:
        return None


def stage_is_before(stages: Iterable[str], earlier: str, later: str) -> bool:
    earlier_index = stage_index(stages, earlier)
    later_index = stage_index(stages, later)
    return earlier_index is not None and later_index is not None and earlier_index < later_index


def should_validate_existing_strats_inputs(context: RouterContext) -> bool:
    preview_mode = context.args.dry_run or context.args.validate_only
    if preview_mode:
        return False
    stages = list(getattr(context.args, "stages", []))
    needs_strats_execution = any(stage in stages for stage in {"run-strats", "collect-strats"})
    if not needs_strats_execution:
        return False
    if stage_is_before(stages, "prepare-strats", "run-strats") or stage_is_before(stages, "prepare-strats", "collect-strats"):
        return False
    return True


def validate_context(context: RouterContext) -> None:
    preview_mode = context.args.dry_run or context.args.validate_only
    for dataset in context.datasets:
        dataset_paths = context.datasets[dataset]
        if not dataset_paths.resolved_config_csv.exists():
            raise FileNotFoundError(f"Resolved config missing: {dataset_paths.resolved_config_csv}")
        if not dataset_paths.config_csv.exists():
            raise FileNotFoundError(f"Source config missing: {dataset_paths.config_csv}")
        if "preprocessing" in context.args.stages:
            raw_value = getattr(context.args, f"{dataset}_raw_data_path", None)
            if raw_value in (None, "", ".", "./", ".\\"):
                raise FileNotFoundError(f"Raw data path for {dataset} is required when preprocessing is selected; received {raw_value!r}")
            raw_path = Path(raw_value).expanduser().resolve()
            if not preview_mode and (not raw_path.exists() or not raw_path.is_dir()):
                raise FileNotFoundError(f"Raw data path for {dataset} is required when preprocessing is selected, but was missing or invalid: {raw_path}")
        if not (context.thesis_repo_root / "main.py").exists():
            raise FileNotFoundError(f"Thesis main.py not found at {context.thesis_repo_root / 'main.py'}")
        if not (context.thesis_repo_root / "src" / "preprocess_physionet_2012.py").exists():
            raise FileNotFoundError(f"PhysioNet preprocessing script not found at {context.thesis_repo_root / 'src' / 'preprocess_physionet_2012.py'}")
        if not (context.thesis_repo_root / "src" / "preprocess_mimic_iii_large.py").exists():
            raise FileNotFoundError(f"MIMIC preprocessing script not found at {context.thesis_repo_root / 'src' / 'preprocess_mimic_iii_large.py'}")
    if not (context.strats_repo_root / "run_full_main.sh").exists():
        raise FileNotFoundError(f"STraTS runner not found at {context.strats_repo_root / 'run_full_main.sh'}")
    if should_validate_existing_strats_inputs(context):
        validate_strats_inputs(context)


def execute_plan(context: RouterContext) -> None:
    create_run_dirs(context)
    write_json(context.run_dir / "config" / "router_args.json", vars(context.args))
    update_manifest(context, "router", "started", {"datasets": list(context.datasets.keys())})
    stage_total = len(context.args.stages)
    for index, stage_name in enumerate(context.args.stages, start=1):
        print_stage(index, stage_total, stage_name)
        if stage_name == "preprocessing":
            for dataset in context.datasets:
                run_preprocessing(dataset, context)
        elif stage_name == "tagging":
            for dataset in context.datasets:
                run_tagging(dataset, context)
        elif stage_name == "trees":
            for dataset in context.datasets:
                run_tree_plots(dataset, context)
        elif stage_name == "prepare-strats":
            prepare_strats_filesystem(context)
        elif stage_name == "run-strats":
            run_strats_script(context)
        elif stage_name == "collect-strats":
            collect_strats_outputs(context)
        elif stage_name == "normalize-predictions":
            normalize_prediction_csvs(context)
        elif stage_name == "thesis-main":
            for dataset in context.datasets:
                run_thesis_main(dataset, context)
        update_manifest(context, stage_name, "completed", {"run_dir": str(context.run_dir)})
    print("[router] Unified run completed successfully.")
    print(f"[router] Manifest: {context.manifest_path}")
    print(f"[router] Outputs: {context.run_dir}")


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if args.dataset not in {"physionet", "mimic", "both"}:
        raise ValueError(f"Unsupported dataset {args.dataset!r}")
    if args.run_strats is None:
        args.run_strats = "run-strats" in args.stages or args.stages == STAGE_ORDER
    context = initialize_context(args)
    validate_context(context)
    if args.validate_only:
        print("[router] Validation only requested; no commands were executed.")
        return 0
    execute_plan(context)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - runtime execution path
        print(f"[router] ERROR: {exc}")
        traceback.print_exc()
        raise

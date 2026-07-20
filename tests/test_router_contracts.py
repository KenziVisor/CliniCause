from __future__ import annotations

import json
import os
import pickle
import signal
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

import router
runtime = router


ROOT = Path(__file__).resolve().parents[1]
THESIS = ROOT / "causal-irregular-time-series"
STRATS = ROOT / "STraTS"


def write_tree_receipt(tree: Path, args, dataset: str) -> None:
    context = runtime.build_context(args, dataset)
    runtime.write_json(
        runtime.artifact_metadata_path(tree),
        {
            "artifact": str(tree.resolve()),
            "artifact_sha256": runtime.file_sha256(tree),
            "run_id": args.run_id,
            "dataset": dataset,
            "producing_stage": "tagging",
            "producer_version": runtime.ROUTER_PRODUCER_VERSION,
            "config_fingerprint": context.config_fingerprints[dataset],
            "input_fingerprints": {"thesis": "0" * 64},
            "schema": ["latent_decision_trees"],
            "model": None,
            "targets": [],
            "seed": args.seed,
            "cohort_size": 1,
            "cohort_fingerprint": runtime.stable_hash(["synthetic"]),
        },
    )


def parse_base(
    tmp_path: Path,
    *,
    dataset: str = "physionet",
    stages: str = "trees",
    extra: list[str] | None = None,
):
    tree = tmp_path / f"{dataset}-trees.pkl"
    tree.write_bytes(b"synthetic")
    argv = [
        "--dataset",
        dataset,
        "--run-id",
        "contract_run",
        "--output-root",
        str(tmp_path / "runs"),
        "--thesis-repo-root",
        str(THESIS),
        "--strats-repo-root",
        str(STRATS),
        "--stages",
        stages,
    ]
    if stages == "trees":
        argv.extend([f"--{dataset}-decision-trees-pkl", str(tree)])
    argv.extend(extra or [])
    args = router.parse_args(argv)
    if stages == "trees":
        write_tree_receipt(tree, args, dataset)
    return args


def parse_both(tmp_path: Path, extra: list[str] | None = None):
    phys = tmp_path / "phys-trees.pkl"
    mimic = tmp_path / "mimic-trees.pkl"
    phys.write_bytes(b"p")
    mimic.write_bytes(b"m")
    argv = [
        "--dataset",
        "both",
        "--run-id",
        "parallel_run",
        "--output-root",
        str(tmp_path / "runs"),
        "--thesis-repo-root",
        str(THESIS),
        "--strats-repo-root",
        str(STRATS),
        "--stages",
        "trees",
        "--physionet-decision-trees-pkl",
        str(phys),
        "--mimic-decision-trees-pkl",
        str(mimic),
    ]
    argv.extend(extra or [])
    args = router.parse_args(argv)
    write_tree_receipt(phys, args, "physionet")
    write_tree_receipt(mimic, args, "mimic")
    return args


class FakeProcess:
    def __init__(self, command, events, returncode=0, pid=1000):
        self.command = list(command)
        self.events = events
        self.returncode = returncode
        self.pid = pid
        self.done = False

    def wait(self, timeout=None):
        del timeout
        self.events.append(("wait", self.dataset))
        self.done = True
        if self.returncode == 0:
            run_dir = Path(
                self.command[self.command.index("--dataset-run-dir") + 1]
            )
            run_dir.mkdir(parents=True, exist_ok=True)
            (run_dir / "manifest.json").write_text(
                json.dumps(
                    {
                        "status": "completed",
                        "failure_summary": None,
                        "stages": {"trees": {"status": "completed"}},
                    }
                ),
                encoding="utf-8",
            )
        return self.returncode

    @property
    def dataset(self):
        return self.command[self.command.index("--dataset") + 1]

    def poll(self):
        return self.returncode

    def terminate(self):
        self.events.append(("terminate", self.dataset))
        self.done = True
        self.returncode = -signal.SIGTERM

    def kill(self):
        self.events.append(("kill", self.dataset))
        self.done = True
        self.returncode = -signal.SIGKILL


def fake_popen_factory(events, codes=None, captured=None):
    codes = codes or {}
    captured = captured if captured is not None else []

    def factory(command, **kwargs):
        dataset = command[command.index("--dataset") + 1]
        events.append(("launch", dataset))
        captured.append((list(command), kwargs))
        return FakeProcess(
            command,
            events,
            returncode=codes.get(dataset, 0),
            pid=1200 + len(captured),
        )

    return factory


def test_stage_names_are_deduplicated_and_canonicalized():
    assert router.normalize_stage_list(
        "thesis-main,tagging,tagging,preprocessing"
    ) == ["preprocessing", "tagging", "thesis-main"]


def test_dataset_extraction_fingerprint_and_child_selector_are_distinct(tmp_path: Path):
    common = [
        "--dataset", "both",
        "--run-id", "semantic_scope",
        "--output-root", str(tmp_path / "runs"),
        "--thesis-repo-root", str(THESIS),
        "--strats-repo-root", str(STRATS),
    ]
    all_args = router.parse_args([*common, "--stages", "all"])
    extraction_args = router.parse_args(
        [*common, "--stages", "dataset-extraction"]
    )
    all_context = runtime.build_context(all_args, "physionet")
    extraction_context = runtime.build_context(extraction_args, "physionet")
    assert all_context.plan_fingerprint != extraction_context.plan_fingerprint

    policy = runtime.resolve_gpu_policy(
        extraction_args,
        ["physionet"],
        environ={"CUDA_VISIBLE_DEVICES": ""},
        run_root=extraction_context.run_root,
    )
    command = runtime.build_child_command(
        extraction_args,
        "physionet",
        extraction_context,
        policy.assignments["physionet"],
    )
    assert command[command.index("--stages") + 1] == "dataset-extraction"
    child_args = router.parse_args(command[2:])
    assert child_args.stage_mode == "dataset-extraction"
    assert child_args.causal_stages == "graph,majority_vote"


@pytest.mark.parametrize("dataset", ["physionet", "mimic"])
def test_dataset_extraction_thesis_contract_is_dataset_local(
    tmp_path: Path, dataset: str
):
    args = router.parse_args([
        "--dataset", dataset,
        "--run-id", "extract_contract",
        "--output-root", str(tmp_path / "runs"),
        "--thesis-repo-root", str(THESIS),
        "--strats-repo-root", str(STRATS),
        "--stages", "dataset-extraction",
    ])
    context = runtime.build_context(args, dataset)
    command = runtime.build_thesis_main_command(dataset, context)
    assert command[command.index("--causal-stages") + 1] == "graph,majority_vote"
    assert command[command.index("--output-dir") + 1] == str(
        context.run_dir / "causal"
    )
    outputs = runtime._expected_stage_output_paths(context, "thesis-main")
    assert outputs == [
        context.run_dir / "causal" / "run_summary.json",
        context.run_dir / "causal" / "majority_vote" / "latent_tags_majority_vote.csv",
        context.run_dir / "causal" / "graph" / f"{dataset}_causal_graph.pkl",
        context.run_dir / "causal" / "graph" / f"{dataset}_causal_dag.png",
    ]


@pytest.mark.parametrize("selector", ["all,tagging", "tagging,unknown", "", ",,"])
def test_invalid_stage_selectors_fail(selector):
    with pytest.raises(ValueError):
        router.normalize_stage_list(selector)


@pytest.mark.parametrize("run_id", ["../escape", "/absolute", "a/b", ".", "..", ""])
def test_unsafe_run_ids_fail(run_id):
    with pytest.raises(ValueError):
        router.validate_run_id(run_id)


def test_seed_zero_is_preserved_in_args_config_and_child_command(tmp_path: Path):
    args = parse_both(tmp_path, ["--seed", "0"])
    contexts = {
        dataset: runtime.build_context(args, dataset)
        for dataset in runtime.selected_datasets(args)
    }
    policy = runtime.resolve_gpu_policy(
        args, list(contexts), environ={"CUDA_VISIBLE_DEVICES": "0"}
    )
    command = runtime.build_child_command(
        args, "physionet", contexts["physionet"], policy.assignments["physionet"]
    )
    assert args.seed == 0
    assert command[command.index("--seed") + 1] == "0"
    row = runtime.build_resolved_config_row(
        contexts["physionet"].configs["physionet"], args
    )
    assert row["SEED"] == 0


def test_parallel_coordinator_launches_both_before_wait_and_never_runs_dataset_plan(
    tmp_path: Path, monkeypatch
):
    args = parse_both(tmp_path)
    events = []
    captured = []
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        fake_popen_factory(events, captured=captured),
    )
    monkeypatch.setattr(
        runtime,
        "run_single_dataset",
        lambda context: pytest.fail("coordinator executed a dataset plan"),
    )

    assert runtime.main(vars_to_argv(args)) == 0

    assert events[:2] == [("launch", "physionet"), ("launch", "mimic")]
    assert [event for event in events if event[0] == "wait"] == [
        ("wait", "physionet"),
        ("wait", "mimic"),
    ]
    assert len(captured) == 2
    commands = [item[0] for item in captured]
    assert {command[command.index("--dataset") + 1] for command in commands} == {
        "physionet",
        "mimic",
    }
    assert all(
        command[command.index("--dataset") + 1] != "both" for command in commands
    )
    assert all("--dataset-child" in command for command in commands)


def vars_to_argv(args) -> list[str]:
    argv = [
        "--dataset",
        args.dataset,
        "--run-id",
        args.run_id,
        "--output-root",
        args.output_root,
        "--thesis-repo-root",
        args.thesis_repo_root,
        "--strats-repo-root",
        args.strats_repo_root,
        "--stages",
        ",".join(args.stages),
        "--seed",
        str(args.seed),
    ]
    for dataset in runtime.DATASETS:
        for suffix in [
            "raw_data_path",
            "config_csv",
            "thesis_pkl",
            "rule_tags_csv",
            "decision_trees_pkl",
            "strats_input_dir",
            "strats_output_dir",
            "voters_dir",
        ]:
            value = getattr(args, f"{dataset}_{suffix}", None)
            if value is not None:
                argv.extend([f"--{dataset}-{suffix.replace('_', '-')}", str(value)])
    if args.run_strats is not None:
        argv.extend(["--run-strats", "true" if args.run_strats else "false"])
    return argv


def test_child_commands_only_receive_their_dataset_arguments(tmp_path: Path):
    args = parse_both(tmp_path)
    contexts, policy, _ = runtime.preflight(args)
    phys = runtime.build_child_command(
        args, "physionet", contexts["physionet"], policy.assignments["physionet"]
    )
    mimic = runtime.build_child_command(
        args, "mimic", contexts["mimic"], policy.assignments["mimic"]
    )
    assert "--mimic-config-csv" not in phys
    assert "--mimic-decision-trees-pkl" not in phys
    assert "--physionet-config-csv" not in mimic
    assert "--physionet-decision-trees-pkl" not in mimic
    assert phys[phys.index("--stages") + 1] == mimic[mimic.index("--stages") + 1]


def test_child_command_round_trips_resolved_scientific_options(tmp_path: Path):
    args = parse_both(
        tmp_path,
        ["--strats-train-frac", "0.25", "--strats-model-run", "2o10"],
    )
    contexts, policy, _ = runtime.preflight(args)
    context = contexts["physionet"]
    command = runtime.build_child_command(
        args, "physionet", context, policy.assignments["physionet"]
    )
    child_args = router.parse_args(command[2:])
    assert child_args.dataset == "physionet"
    assert child_args.run_strats is args.run_strats
    assert child_args.strats_train_frac == 0.25
    assert child_args.strats_model_run == "2o10"
    assert Path(child_args.python_executable).is_absolute()
    assert child_args.physionet_decision_trees_pkl == str(
        context.datasets["physionet"].decision_trees_input_pkl
    )



def test_parallel_failure_is_aggregated_without_deleting_successful_evidence(
    tmp_path: Path, monkeypatch
):
    args = parse_both(tmp_path)
    events = []
    marker = tmp_path / "success.marker"
    marker.write_text("preserve", encoding="utf-8")
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        fake_popen_factory(events, codes={"mimic": 7}),
    )

    assert runtime.main(vars_to_argv(args)) == 1
    assert marker.read_text(encoding="utf-8") == "preserve"
    manifest = json.loads(
        (tmp_path / "runs" / "parallel_run" / "coordinator" / "manifest.json").read_text()
    )
    assert manifest["overall_status"] == "failed"
    assert manifest["children"]["physionet"]["status"] == "completed"
    assert manifest["children"]["mimic"]["status"] == "failed"
    assert manifest["children"]["mimic"]["exit_code"] == 7
    child_manifest = json.loads(
        (tmp_path / "runs" / "parallel_run" / "mimic" / "manifest.json").read_text()
    )
    assert child_manifest["status"] == "failed"


def test_fail_fast_detects_later_child_failure_and_cancels_running_sibling(
    tmp_path: Path, monkeypatch
):
    args = parse_both(tmp_path, ["--fail-fast"])
    events: list[tuple[str, str]] = []

    class ReverseFailureProcess(FakeProcess):
        def __init__(self, command, returncode, pid):
            super().__init__(command, events, returncode=returncode, pid=pid)
            self.running = returncode is None

        def poll(self):
            return None if self.running else self.returncode

        def terminate(self):
            events.append(("terminate", self.dataset))
            self.running = False
            self.returncode = -signal.SIGTERM

    def factory(command, **kwargs):
        del kwargs
        dataset = command[command.index("--dataset") + 1]
        events.append(("launch", dataset))
        return ReverseFailureProcess(
            command, None if dataset == "physionet" else 7, 1400 + len(events)
        )

    monkeypatch.setattr(runtime.subprocess, "Popen", factory)
    assert runtime.main(vars_to_argv(args) + ["--fail-fast"]) == 1
    assert events[:2] == [("launch", "physionet"), ("launch", "mimic")]
    assert ("terminate", "physionet") in events
    manifest = json.loads(
        (tmp_path / "runs" / "parallel_run" / "coordinator" / "manifest.json").read_text()
    )
    assert manifest["children"]["mimic"]["status"] == "failed"
    assert manifest["children"]["physionet"]["status"] == "cancelled"



def test_single_dataset_validation_does_not_spawn_or_mutate(tmp_path: Path, monkeypatch):
    args = parse_base(tmp_path)
    output_root = tmp_path / "runs"
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        lambda *a, **k: pytest.fail("validation spawned a process"),
    )
    argv = vars_to_argv(args) + ["--validate-only"]
    assert runtime.main(argv) == 0
    assert not output_root.exists()


def test_single_dataset_execution_uses_direct_path_without_child_popen(
    tmp_path: Path, monkeypatch
):
    args = parse_base(tmp_path)
    called = []
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        lambda *a, **k: pytest.fail("single dataset spawned a router child"),
    )
    monkeypatch.setattr(
        runtime,
        "run_single_dataset",
        lambda context: called.append(context.run_dir) or 0,
    )
    assert runtime.main(vars_to_argv(args)) == 0
    assert called == [tmp_path / "runs" / "contract_run" / "physionet"]


def test_internal_child_cannot_coordinate_both():
    with pytest.raises(ValueError, match="cannot coordinate"):
        router.parse_args(
            ["--dataset", "both", "--run-id", "x", "--dataset-child"]
        )


def test_dataset_path_hierarchies_are_disjoint_and_contained(tmp_path: Path):
    args = parse_both(tmp_path)
    contexts, _, _ = runtime.preflight(args)
    left = contexts["physionet"].datasets["physionet"]
    right = contexts["mimic"].datasets["mimic"]
    assert left.run_dir != right.run_dir
    writable_names = [
        "resolved_config_csv",
        "thesis_processed_pkl",
        "rule_latent_tags_csv",
        "rule_decision_trees_pkl",
        "tree_plots_dir",
        "strats_processed_pkl",
        "strats_latent_tags_csv",
        "strats_output_root",
        "strats_predictions_dir",
        "predicted_raw_dir",
        "voters_dir",
        "thesis_main_output_dir",
        "temporary_dir",
        "manifest_path",
        "logs_dir",
    ]
    left_paths = {Path(getattr(left, name)).resolve() for name in writable_names}
    right_paths = {Path(getattr(right, name)).resolve() for name in writable_names}
    assert left_paths.isdisjoint(right_paths)
    assert all(left.run_dir.resolve() in [path, *path.parents] for path in left_paths)
    assert all(right.run_dir.resolve() in [path, *path.parents] for path in right_paths)


def test_dry_run_is_filesystem_pure_and_spawns_no_child(tmp_path: Path, monkeypatch):
    raw = tmp_path / "raw"
    raw.mkdir()
    output = tmp_path / "new-runs"
    argv = [
        "--dataset",
        "physionet",
        "--run-id",
        "pure",
        "--output-root",
        str(output),
        "--thesis-repo-root",
        str(THESIS),
        "--strats-repo-root",
        str(STRATS),
        "--stages",
        "preprocessing",
        "--physionet-raw-data-path",
        str(raw),
        "--dry-run",
    ]
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        lambda *a, **k: pytest.fail("dry-run spawned a process"),
    )
    assert runtime.main(argv) == 0
    assert not output.exists()


def test_invalid_preview_input_fails_with_zero_filesystem_delta(tmp_path: Path):
    output = tmp_path / "new-runs"
    argv = [
        "--dataset",
        "physionet",
        "--run-id",
        "invalid",
        "--output-root",
        str(output),
        "--thesis-repo-root",
        str(THESIS),
        "--strats-repo-root",
        str(STRATS),
        "--stages",
        "preprocessing",
        "--physionet-raw-data-path",
        str(tmp_path / "missing"),
        "--validate-only",
    ]
    with pytest.raises(FileNotFoundError):
        runtime.main(argv)
    assert not output.exists()


def test_existing_run_collision_happens_before_spawn(tmp_path: Path, monkeypatch):
    args = parse_both(tmp_path)
    run_root = tmp_path / "runs" / "parallel_run"
    run_root.mkdir(parents=True)
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        lambda *a, **k: pytest.fail("collision spawned a child"),
    )
    with pytest.raises(FileExistsError):
        runtime.main(vars_to_argv(args))


def test_resume_requires_matching_plan_fingerprint(tmp_path: Path):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    context.run_dir.mkdir(parents=True)
    runtime.write_json(
        context.manifest_path,
        {"plan_fingerprint": context.plan_fingerprint},
    )
    resume_args = parse_base(tmp_path, extra=["--resume", "--skip-existing"])
    resume_context = runtime.build_context(resume_args, "physionet")
    runtime.validate_run_collision(
        resume_args,
        {"physionet": resume_context},
        "unused",
    )
    runtime.write_json(
        resume_context.manifest_path,
        {"plan_fingerprint": "different"},
    )
    with pytest.raises(ValueError, match="fingerprint"):
        runtime.validate_run_collision(
            resume_args,
            {"physionet": resume_context},
            "unused",
        )


def test_one_visible_gpu_uses_one_shared_lock(tmp_path: Path):
    args = parse_both(tmp_path)
    policy = runtime.resolve_gpu_policy(
        args,
        ["physionet", "mimic"],
        environ={"CUDA_VISIBLE_DEVICES": "0"},
        run_root=tmp_path / "run",
    )
    assert policy.max_concurrent == 1
    assert policy.assignments["physionet"].physical == "0"
    assert policy.assignments["mimic"].physical == "0"
    assert (
        policy.assignments["physionet"].lock_path
        == policy.assignments["mimic"].lock_path
    )


def test_two_visible_gpus_get_stable_distinct_assignments(tmp_path: Path):
    args = parse_both(tmp_path)
    policy = runtime.resolve_gpu_policy(
        args,
        ["physionet", "mimic"],
        environ={"CUDA_VISIBLE_DEVICES": "3,7"},
        run_root=tmp_path / "run",
    )
    assert policy.max_concurrent == 2
    assert policy.assignments["physionet"].physical == "3"
    assert policy.assignments["mimic"].physical == "7"
    assert policy.assignments["physionet"].child_visible == "0"
    assert policy.assignments["mimic"].child_visible == "0"
    assert (
        policy.assignments["physionet"].lock_path
        != policy.assignments["mimic"].lock_path
    )


@pytest.mark.parametrize(
    "extra,environ,match",
    [
        (
            ["--physionet-gpu", "0", "--mimic-gpu", "0"],
            {"CUDA_VISIBLE_DEVICES": "0,1"},
            "same explicit GPU",
        ),
        (
            ["--physionet-gpu", "2", "--mimic-gpu", "1"],
            {"CUDA_VISIBLE_DEVICES": "0,1"},
            "not visible",
        ),
        (
            ["--strats-max-concurrent", "2"],
            {"CUDA_VISIBLE_DEVICES": "0"},
            "unique",
        ),
    ],
)
def test_invalid_gpu_policy_fails_before_execution(tmp_path: Path, extra, environ, match):
    args = parse_both(tmp_path, extra)
    with pytest.raises(ValueError, match=match):
        runtime.resolve_gpu_policy(
            args,
            ["physionet", "mimic"],
            environ=environ,
            run_root=tmp_path / "run",
        )
    assert not (tmp_path / "run").exists()


def test_gpu_permit_records_wait_acquire_release_and_releases_on_exception(
    tmp_path: Path,
):
    events = []
    lock = tmp_path / "gpu.lock"
    with pytest.raises(RuntimeError, match="synthetic"):
        with runtime.GPUFilePermit(
            lock, lambda name, timestamp: events.append((name, timestamp))
        ):
            raise RuntimeError("synthetic")
    assert [name for name, _ in events] == [
        "permit_wait_start",
        "permit_acquired_at",
        "permit_released_at",
    ]
    with runtime.GPUFilePermit(lock):
        pass


def test_cpu_only_stage_does_not_acquire_gpu_permit(tmp_path: Path, monkeypatch):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)
    tree_output = context.datasets["physionet"].tree_plots_dir
    tree_output.mkdir(parents=True, exist_ok=True)
    (tree_output / "synthetic.png").write_bytes(b"png")
    monkeypatch.setattr(
        runtime,
        "GPUFilePermit",
        lambda *a, **k: pytest.fail("CPU stage acquired GPU"),
    )
    monkeypatch.setattr(
        runtime,
        "_execute_stage",
        lambda context, stage: runtime.StageResult(
            details={"outputs": [str(tree_output)]}
        ),
    )
    runtime.execute_plan(context)
    manifest = json.loads(context.manifest_path.read_text())
    assert manifest["stages"]["trees"]["status"] == "completed"


def test_stage_skip_is_not_overwritten_as_completed(tmp_path: Path, monkeypatch):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)
    tree_output = context.datasets["physionet"].tree_plots_dir
    tree_output.mkdir(parents=True, exist_ok=True)
    (tree_output / "synthetic.png").write_bytes(b"png")
    monkeypatch.setattr(
        runtime,
        "_execute_stage",
        lambda context, stage: runtime.StageResult(
            "skipped",
            {
                "reason": "matching provenance",
                "outputs": [str(tree_output)],
            },
        ),
    )
    runtime.execute_plan(context)
    manifest = json.loads(context.manifest_path.read_text())
    assert manifest["stages"]["trees"]["status"] == "skipped"


def test_resume_receipt_rejects_nonempty_output_subset(tmp_path: Path):
    raw = tmp_path / "raw"
    raw.mkdir()
    args = parse_base(
        tmp_path,
        stages="preprocessing",
        extra=["--physionet-raw-data-path", str(raw)],
    )
    context = runtime.build_context(args, "physionet")
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)
    paths = context.datasets["physionet"]
    paths.thesis_processed_pkl.write_bytes(b"synthetic")
    metadata = runtime.artifact_metadata_path(paths.thesis_processed_pkl)
    metadata.write_text("{}", encoding="utf-8")
    receipt_path = runtime.write_stage_receipt(
        context,
        "preprocessing",
        runtime.StageResult(
            details={
                "outputs": [str(paths.thesis_processed_pkl), str(metadata)]
            }
        ),
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    receipt["outputs"] = receipt["outputs"][:1]
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(ValueError, match="output set mismatch"):
        runtime.validate_stage_receipt(context, "preprocessing")



def test_stage_exception_is_manifested_before_propagation(tmp_path: Path, monkeypatch):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)

    def fail(context, stage):
        raise RuntimeError("synthetic stage failure")

    monkeypatch.setattr(runtime, "_execute_stage", fail)
    with pytest.raises(RuntimeError, match="synthetic stage failure"):
        runtime.execute_plan(context)
    manifest = json.loads(context.manifest_path.read_text())
    assert manifest["status"] == "failed"
    assert manifest["stages"]["trees"]["status"] == "failed"
    assert "synthetic stage failure" in manifest["failure_summary"]


def synthetic_frames(ids=("1", "2", "3", "4", "5", "6")):
    ts = pd.DataFrame(
        {
            "ts_id": list(ids),
            "minute": [0] * len(ids),
            "variable": ["HR"] * len(ids),
            "value": [80.0] * len(ids),
        }
    )
    oc = pd.DataFrame(
        {
            "ts_id": list(ids),
            "in_hospital_mortality": [0, 1] * (len(ids) // 2)
            + ([0] if len(ids) % 2 else []),
        }
    )
    return ts, oc


def test_split_generation_is_order_independent_and_seed_zero_valid(tmp_path: Path):
    ts, oc = synthetic_frames()
    first = tmp_path / "first.pkl"
    second = tmp_path / "second.pkl"
    source_a = tmp_path / "source-a.pkl"
    source_b = tmp_path / "source-b.pkl"
    with source_a.open("wb") as handle:
        pickle.dump([ts, oc, list(ts["ts_id"])], handle)
    with source_b.open("wb") as handle:
        pickle.dump(
            [
                ts.iloc[::-1].reset_index(drop=True),
                oc.iloc[::-1].reset_index(drop=True),
                list(reversed(list(ts["ts_id"]))),
            ],
            handle,
        )
    runtime.build_strats_pickle("physionet", source_a, first, 0)
    runtime.build_strats_pickle("physionet", source_b, second, 0)
    with first.open("rb") as handle:
        first_payload = pickle.load(handle)
    with second.open("rb") as handle:
        second_payload = pickle.load(handle)
    assert first_payload[2:] == second_payload[2:]
    canonical = list(ts["ts_id"])
    runtime.validate_split_integrity(canonical, *first_payload[2:])


@pytest.mark.parametrize(
    "train,val,test,match",
    [
        (["1", "1"], ["2"], ["3"], "duplicate"),
        (["1"], ["1"], ["2", "3"], "overlap"),
        (["1"], ["2"], ["4"], "mismatch"),
        (["1"], ["2"], [], "nonempty"),
    ],
)
def test_split_integrity_rejects_invalid_partitions(train, val, test, match):
    with pytest.raises(ValueError, match=match):
        runtime.validate_split_integrity(["1", "2", "3"], train, val, test)


def test_authoritative_splits_are_preserved(tmp_path: Path):
    ts, oc = synthetic_frames()
    source = tmp_path / "authoritative.pkl"
    output = tmp_path / "output.pkl"
    expected = [["6", "1", "2"], ["4"], ["3", "5"]]
    with source.open("wb") as handle:
        pickle.dump([ts, oc, *expected], handle)
    runtime.build_strats_pickle("physionet", source, output, 999)
    with output.open("rb") as handle:
        payload = pickle.load(handle)
    assert payload[2:] == expected


@pytest.mark.parametrize(
    "bad_value",
    [None, float("nan"), float("inf"), float(2**53), 10.5, "bad", "1e1", True, "010"],
)
def test_prediction_identifier_rejects_malformed_values(bad_value):
    frame = pd.DataFrame({"ts_id": [bad_value], "LAT_A": [1]})
    with pytest.raises(ValueError):
        runtime.validate_prediction_frame(frame, ["LAT_A"], None, "synthetic")


@pytest.mark.parametrize("bad_value", [None, float("nan"), float("inf"), -0.1, 1.1, "bad"])
def test_prediction_probability_rejects_malformed_values(bad_value):
    frame = pd.DataFrame(
        {"ts_id": ["1"], "LAT_A": [1], "LAT_A_prob": [bad_value]}
    )
    with pytest.raises(ValueError):
        runtime.validate_prediction_frame(frame, ["LAT_A"], ["1"], "synthetic")


def test_prediction_cohort_reorders_equal_ids_and_rejects_missing_extra():
    frame = pd.DataFrame({"ts_id": ["2", "1"], "LAT_A": [0, 1]})
    result = runtime.validate_prediction_frame(
        frame, ["LAT_A"], ["1", "2"], "synthetic"
    )
    assert result["ts_id"].tolist() == ["1", "2"]
    with pytest.raises(ValueError, match="missing=1 extra=1"):
        runtime.validate_prediction_frame(
            frame, ["LAT_A"], ["1", "3"], "synthetic"
        )


def test_probability_tag_inconsistency_fails():
    frame = pd.DataFrame(
        {"ts_id": ["1"], "LAT_A": [0], "LAT_A_prob": [0.9]}
    )
    with pytest.raises(ValueError, match="inconsistency"):
        runtime.validate_prediction_frame(frame, ["LAT_A"], ["1"], "synthetic")


def test_model_prediction_requires_probability_columns():
    frame = pd.DataFrame({"ts_id": ["1"], "LAT_A": [1]})
    with pytest.raises(ValueError, match="Missing probability columns"):
        runtime.validate_prediction_frame(
            frame,
            ["LAT_A"],
            ["1"],
            "synthetic",
            require_probabilities=True,
        )

def test_artifact_provenance_rejects_mutation_and_field_mismatch(tmp_path: Path):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)
    artifact = context.run_dir / "synthetic.csv"
    artifact.write_text("ts_id,LAT_A\n1,1\n", encoding="utf-8")
    metadata = runtime.write_artifact_record(
        artifact,
        context,
        "synthetic-stage",
        schema=["ts_id", "LAT_A"],
        model="rules",
        targets=["LAT_A"],
        cohort=["1"],
    )
    expected = {
        "run_id": context.run_id,
        "dataset": "physionet",
        "producing_stage": "synthetic-stage",
        "config_fingerprint": context.config_fingerprints["physionet"],
    }
    runtime.validate_artifact_record(artifact, expected, metadata)
    with pytest.raises(ValueError, match="provenance mismatch"):
        runtime.validate_artifact_record(
            artifact, {**expected, "dataset": "mimic"}, metadata
        )
    artifact.write_text("ts_id,LAT_A\n1,0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="digest mismatch"):
        runtime.validate_artifact_record(artifact, expected, metadata)


def test_build_stage_log_path_is_pure(tmp_path: Path):
    path = runtime.build_stage_log_path(tmp_path / "run", "stage", "mimic")
    assert path == tmp_path / "run" / "logs" / "stage_mimic.log"
    assert not (tmp_path / "run").exists()


def test_relative_and_tilde_raw_paths_are_normalized_before_child_cwd(
    tmp_path: Path, monkeypatch
):
    home = tmp_path / "home"
    raw = home / "raw"
    raw.mkdir(parents=True)
    monkeypatch.setenv("HOME", str(home))
    args = parse_base(
        tmp_path,
        stages="preprocessing",
        extra=["--physionet-raw-data-path", "~/raw"],
    )
    context = runtime.build_context(args, "physionet")
    assert runtime.resolve_dataset_raw_data_path("physionet", context) == raw.resolve()
    command = runtime.build_preprocessing_command("physionet", context)
    assert command[command.index("--raw-data-path") + 1] == str(raw.resolve())

def write_synthetic_strats_input(context: runtime.RouterContext) -> list[str]:
    dataset = next(iter(context.datasets))
    paths = context.datasets[dataset]
    cohort = ["1", "2", "3", "4", "5", "6"]
    ts, oc = synthetic_frames(cohort)
    train, val, test = cohort[:4], cohort[4:5], cohort[5:]
    paths.strats_processed_pkl.parent.mkdir(parents=True, exist_ok=True)
    with paths.strats_processed_pkl.open("wb") as handle:
        pickle.dump([ts, oc, train, val, test], handle)
    latent_order = runtime._latent_order(context, dataset)
    labels = pd.DataFrame(
        {
            "ts_id": cohort,
            **{target: [0] * len(cohort) for target in latent_order},
        }
    )
    paths.strats_latent_tags_csv.parent.mkdir(parents=True, exist_ok=True)
    labels.to_csv(paths.strats_latent_tags_csv, index=False)
    adapter_seed = runtime.derive_seed(context.args.seed, dataset, "adapter")
    runtime.write_artifact_record(
        paths.strats_processed_pkl,
        context,
        "prepare-strats",
        schema=["data", "oc", "train_ids", "val_ids", "test_ids"],
        inputs={"thesis": "0" * 64},
        cohort=cohort,
        seed=adapter_seed,
    )
    runtime.write_artifact_record(
        paths.strats_latent_tags_csv,
        context,
        "prepare-strats",
        schema=["ts_id", *latent_order],
        inputs={"rules": "1" * 64},
        cohort=cohort,
        seed=adapter_seed,
    )
    runtime.write_json(
        paths.strats_input_root / "artifact_manifest.json",
        {
            "run_id": context.run_id,
            "dataset": dataset,
            "config_fingerprint": context.config_fingerprints[dataset],
            "seed": context.args.seed,
            "adapter_seed": adapter_seed,
            "processed": str(paths.strats_processed_pkl.resolve()),
            "labels": str(paths.strats_latent_tags_csv.resolve()),
            "processed_sha256": runtime.file_sha256(paths.strats_processed_pkl),
            "labels_sha256": runtime.file_sha256(paths.strats_latent_tags_csv),
            "cohort_size": len(cohort),
            "cohort_fingerprint": runtime.stable_hash(sorted(cohort)),
            "producer_version": runtime.ROUTER_PRODUCER_VERSION,
        },
    )
    return cohort


def write_synthetic_strats_prediction(
    context: runtime.RouterContext,
    model: str,
    cohort: list[str] | None = None,
) -> Path:
    dataset = next(iter(context.datasets))
    paths = context.datasets[dataset]
    path = paths.strats_predictions_dir / f"{model}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    targets = runtime._latent_order(context, dataset)
    columns = ["ts_id", *[f"{target}_prob" for target in targets], *targets]
    cohort = cohort or []
    frame = pd.DataFrame(
        {
            "ts_id": cohort,
            **{f"{target}_prob": [0.8] * len(cohort) for target in targets},
            **{target: [1] * len(cohort) for target in targets},
        },
        columns=columns,
    )
    frame.to_csv(path, index=False)
    model_seed = runtime.derive_strats_model_seed(context.args.seed, dataset, model)
    model_config, training_config, scientific_fingerprint = (
        runtime._expected_strats_scientific_config(context, model)
    )
    metadata = {
        "metadata_schema_version": 2,
        "artifact_kind": "prediction",
        "artifact_name": path.name,
        "artifact_sha256": runtime.file_sha256(path),
        "artifact_size": path.stat().st_size,
        "pipeline_run_id": context.run_id,
        "dataset": paths.strats_dataset,
        "model": model,
        "architecture_mode": "finetune" if model == "strats" else "scratch",
        "ordered_targets": targets,
        "config_fingerprint": context.config_fingerprints[dataset],
        "base_seed": context.args.seed,
        "dataset_seed": runtime.derive_strats_dataset_seed(context.args.seed, dataset),
        "model_seed": model_seed,
        "effective_seed": runtime.derive_strats_effective_seed(
            model_seed, context.args.strats_model_run
        ),
        "producing_command": ["python", "main.py"],
        "schema": {
            "columns": columns,
            "probability_range": [0.0, 1.0],
            "binary_values": [0, 1],
        },
        "cohort": {
            "count": len(cohort),
            "sha256": runtime.stable_hash(sorted(cohort)),
        },
        "model_config": model_config,
        "training_config": training_config,
        "scientific_config_fingerprint": scientific_fingerprint,
        "inputs": {
            name: {"name": name, "size": 1, "sha256": value * 64}
            for name, value in {
                "processed_data": "0",
                "latent_tags": "1",
                "checkpoint": "2",
            }.items()
        },
    }
    runtime.write_json(Path(str(path) + ".metadata.json"), metadata)
    return path

def test_router_validates_exact_strats_metadata_contract(tmp_path: Path):
    args = parse_base(tmp_path)
    context = runtime.build_context(args, "physionet")
    cohort = write_synthetic_strats_input(context)
    prediction = write_synthetic_strats_prediction(context, "gru", cohort)
    metadata = runtime.validate_strats_prediction_metadata(
        prediction, context, "gru"
    )
    assert metadata["base_seed"] == 42
    metadata["ordered_targets"] = list(reversed(metadata["ordered_targets"]))
    runtime.write_json(Path(str(prediction) + ".metadata.json"), metadata)
    with pytest.raises(ValueError, match="ordered_targets"):
        runtime.validate_strats_prediction_metadata(prediction, context, "gru")


def test_run_strats_uses_only_child_scoped_paths_and_gpu_environment(
    tmp_path: Path, monkeypatch
):
    input_root = tmp_path / "external-input"
    args = parse_base(
        tmp_path,
        stages="run-strats",
        extra=[
            "--physionet-strats-input-dir",
            str(input_root),
            "--physionet-gpu",
            "7",
        ],
    )
    context = runtime.build_context(args, "physionet")
    context.gpu_assignment = runtime.resolve_gpu_policy(
        args,
        ["physionet"],
        environ={"CUDA_VISIBLE_DEVICES": "7"},
        run_root=context.run_root,
    ).assignments["physionet"]
    runtime.reserve_top_level_root(args, context.run_root)
    runtime.initialize_dataset_run(context)
    paths = context.datasets["physionet"]
    cohort = write_synthetic_strats_input(context)
    for model in runtime.MODELS:
        write_synthetic_strats_prediction(context, model, cohort)

    captured = {}

    def fake_run(command, cwd, log_path, dry_run=False, env=None):
        captured.update(
            {
                "command": command,
                "cwd": cwd,
                "log_path": log_path,
                "dry_run": dry_run,
                "env": env,
            }
        )
        return 0

    monkeypatch.setattr(runtime, "run_command", fake_run)
    result = runtime.run_strats_script(context)
    assert result.status == "completed"
    assert captured["env"]["DATASET_SCOPE"] == "physionet"
    assert captured["env"]["CUDA_VISIBLE_DEVICES"] == "7"
    assert captured["env"]["STRATS_INPUT_ROOT"] == str(paths.strats_input_root)
    assert captured["env"]["STRATS_OUTPUT_ROOT"] == str(paths.strats_output_root)
    assert str(STRATS / "data") not in captured["env"]["STRATS_INPUT_ROOT"]
    assert str(STRATS / "outputs") not in captured["env"]["STRATS_OUTPUT_ROOT"]
    manifest = json.loads(context.manifest_path.read_text(encoding="utf-8"))
    gpu = manifest["gpu"]
    assert gpu["strats_start"] <= gpu["strats_finish"]
    assert gpu["strats_finish"] <= gpu["permit_released_at"]
    assert gpu["strats_exit_code"] == 0


def test_missing_stage_producer_fails_before_filesystem_mutation(tmp_path: Path):
    output = tmp_path / "runs"
    args = parse_base(tmp_path, stages="tagging")
    context = runtime.build_context(args, "physionet")
    with pytest.raises(ValueError, match="tagging requires preprocessing"):
        runtime.validate_context(context)
    assert not output.exists()


def test_both_validate_only_is_pure_and_has_no_child_process(
    tmp_path: Path, monkeypatch
):
    args = parse_both(tmp_path)
    monkeypatch.setattr(
        runtime.subprocess,
        "Popen",
        lambda *a, **k: pytest.fail("validate-only spawned a child"),
    )
    assert runtime.main(vars_to_argv(args) + ["--validate-only"]) == 0
    assert not (tmp_path / "runs").exists()


def test_coordinator_signal_handler_targets_every_child_process_group(monkeypatch):
    installed = {}
    signalled = []

    class SignalProcess:
        def __init__(self, pid):
            self.pid = pid
            self.finished = False

        def poll(self):
            return 0 if self.finished else None

        def wait(self, timeout=None):
            del timeout
            self.finished = True
            return -signal.SIGTERM

        def terminate(self):
            self.finished = True

        def kill(self):
            self.finished = True

    monkeypatch.setattr(
        runtime.signal,
        "signal",
        lambda signum, handler: installed.__setitem__(signum, handler),
    )
    monkeypatch.setattr(runtime.signal, "getsignal", lambda signum: None)
    monkeypatch.setattr(
        runtime.os,
        "killpg",
        lambda pid, signum: signalled.append((pid, signum)),
    )
    processes = {
        "physionet": SignalProcess(101),
        "mimic": SignalProcess(202),
    }
    with pytest.raises(runtime.CoordinatorInterrupted):
        with runtime.coordinator_signal_handlers(processes):
            installed[signal.SIGTERM](signal.SIGTERM, None)
    assert signalled == [
        (101, signal.SIGTERM),
        (202, signal.SIGTERM),
    ]

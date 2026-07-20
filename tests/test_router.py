import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


spec = importlib.util.spec_from_file_location("router", Path(__file__).resolve().parents[1] / "router.py")
router = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = router
spec.loader.exec_module(router)


class RouterParsingTests(unittest.TestCase):
    def test_default_stages_expand_to_full_order(self):
        args = router.parse_args([
            "--dataset", "both",
            "--run-id", "exp_test",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
        ])
        self.assertEqual(args.stages, router.STAGE_ORDER)
        self.assertEqual(args.stage_mode, "all")
        self.assertEqual(args.causal_stages, "all")

    def test_dataset_extraction_is_a_distinct_full_router_preset(self):
        args = router.parse_args([
            "--dataset", "physionet",
            "--run-id", "extract_test",
            "--stages", "dataset-extraction",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
        ])
        self.assertEqual(args.stages, router.STAGE_ORDER)
        self.assertEqual(args.stage_mode, "dataset-extraction")
        self.assertEqual(args.stage_selector, "dataset-extraction")
        self.assertEqual(args.causal_stages, "graph,majority_vote")

    def test_dataset_extraction_rejects_combinations(self):
        for selector in (
            "dataset-extraction,tagging",
            "all,dataset-extraction",
        ):
            with self.subTest(selector=selector), self.assertRaises(ValueError):
                router.normalize_stage_list(selector)

    def test_explicit_subset_retains_explicit_mode(self):
        args = router.parse_args([
            "--dataset", "physionet",
            "--run-id", "explicit_test",
            "--stages", "thesis-main,tagging",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
        ])
        self.assertEqual(args.stages, ["tagging", "thesis-main"])
        self.assertEqual(args.stage_mode, "explicit")
        self.assertEqual(args.causal_stages, "all")

    def test_dataset_extraction_fingerprint_child_and_causal_contract(self):
        root = Path(__file__).resolve().parents[1]
        thesis = root / "causal-irregular-time-series"
        strats = root / "STraTS"
        with tempfile.TemporaryDirectory() as temp_dir:
            common = [
                "--dataset", "both",
                "--run-id", "semantic_test",
                "--output-root", str(Path(temp_dir) / "runs"),
                "--thesis-repo-root", str(thesis),
                "--strats-repo-root", str(strats),
            ]
            all_args = router.parse_args([*common, "--stages", "all"])
            extraction_args = router.parse_args(
                [*common, "--stages", "dataset-extraction"]
            )
            all_context = router.build_context(all_args, "physionet")
            extraction_context = router.build_context(
                extraction_args, "physionet"
            )
            self.assertNotEqual(
                all_context.plan_fingerprint,
                extraction_context.plan_fingerprint,
            )
            all_causal = router.build_thesis_main_command(
                "physionet", all_context
            )
            self.assertEqual(
                all_causal[all_causal.index("--causal-stages") + 1], "all"
            )
            policy = router.resolve_gpu_policy(
                extraction_args,
                ["physionet"],
                environ={"CUDA_VISIBLE_DEVICES": ""},
                run_root=extraction_context.run_root,
            )
            child = router.build_child_command(
                extraction_args,
                "physionet",
                extraction_context,
                policy.assignments["physionet"],
            )
            self.assertEqual(
                child[child.index("--stages") + 1], "dataset-extraction"
            )
            causal = router.build_thesis_main_command(
                "physionet", extraction_context
            )
            self.assertEqual(
                causal[causal.index("--causal-stages") + 1],
                "graph,majority_vote",
            )
            self.assertEqual(
                router._expected_stage_output_paths(
                    extraction_context, "thesis-main"
                )[1],
                extraction_context.run_dir
                / "causal"
                / "majority_vote"
                / "latent_tags_majority_vote.csv",
            )

    def test_run_strats_flag_defaults_to_true_when_stage_requested(self):
        args = router.parse_args([
            "--dataset", "physionet",
            "--run-id", "exp_test",
            "--stages", "run-strats",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
        ])
        self.assertTrue(args.run_strats)

    def test_validate_stage_names(self):
        normalized = router.normalize_stage_list("preprocessing,tagging")
        self.assertEqual(normalized, ["preprocessing", "tagging"])

    def test_dry_run_flag_is_parsed(self):
        args = router.parse_args([
            "--dataset", "physionet",
            "--run-id", "dryrun_test",
            "--stages", "preprocessing",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
            "--dry-run",
        ])
        self.assertTrue(args.dry_run)
        self.assertFalse(args.validate_only)

    def test_validate_only_flag_is_parsed(self):
        args = router.parse_args([
            "--dataset", "mimic",
            "--run-id", "validate_test",
            "--stages", "preprocessing",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
            "--validate-only",
        ])
        self.assertTrue(args.validate_only)
        self.assertFalse(args.dry_run)

    def test_preprocess_chunk_size_and_tmp_dir_are_parsed(self):
        args = router.parse_args([
            "--dataset", "mimic",
            "--run-id", "chunk_test",
            "--stages", "preprocessing",
            "--thesis-repo-root", str(Path(".").resolve()),
            "--strats-repo-root", str(Path(".").resolve()),
            "--preprocess-chunksize", "12345",
            "--tmp-dir", "/tmp/mimic-preprocess",
        ])
        self.assertEqual(args.preprocess_chunksize, 12345)
        self.assertEqual(args.tmp_dir, "/tmp/mimic-preprocess")

    def test_build_preprocessing_command_for_physionet_does_not_pass_chunksize(self):
        context = SimpleNamespace(
            args=SimpleNamespace(
                python_executable="python",
                preprocess_chunksize=500000,
                tmp_dir="/tmp/preprocess",
                dry_run=False,
                skip_existing=False,
            ),
            thesis_repo_root=Path("."),
            datasets={
                "physionet": SimpleNamespace(
                    resolved_config_csv=Path("config.csv"),
                    thesis_processed_pkl=Path("out.pkl"),
                )
            },
        )
        command = router.build_preprocessing_command("physionet", context)
        self.assertIn("--processed-dir", command)
        self.assertNotIn("--chunksize", command)

    def test_build_preprocessing_command_for_mimic_passes_chunksize(self):
        context = SimpleNamespace(
            args=SimpleNamespace(
                python_executable="python",
                preprocess_chunksize=500000,
                tmp_dir="/tmp/preprocess",
                dry_run=False,
                skip_existing=False,
            ),
            thesis_repo_root=Path("."),
            datasets={
                "mimic": SimpleNamespace(
                    resolved_config_csv=Path("config.csv"),
                    thesis_processed_pkl=Path("out.pkl"),
                )
            },
        )
        command = router.build_preprocessing_command("mimic", context)
        self.assertIn("--chunksize", command)
        self.assertIn("500000", command)
        self.assertIn("--tmp-dir", command)

    def test_build_preprocessing_command_normalizes_relative_raw_path_before_child_cwd_changes(self):
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            caller_cwd = temp_root / "caller"
            caller_cwd.mkdir()
            raw_dir = caller_cwd / "raw"
            raw_dir.mkdir()
            thesis_repo_root = temp_root / "thesis"
            thesis_repo_root.mkdir()
            context = SimpleNamespace(
                args=SimpleNamespace(
                    python_executable="python",
                    physionet_raw_data_path="raw",
                    preprocess_chunksize=500000,
                    tmp_dir=None,
                ),
                thesis_repo_root=thesis_repo_root,
                datasets={
                    "physionet": SimpleNamespace(
                        resolved_config_csv=temp_root / "config.csv",
                        thesis_processed_pkl=temp_root / "out.pkl",
                    )
                },
            )

            try:
                os.chdir(caller_cwd)
                command = router.build_preprocessing_command("physionet", context)
            finally:
                os.chdir(original_cwd)

            raw_path_arg = command[command.index("--raw-data-path") + 1]
            self.assertEqual(raw_path_arg, str(raw_dir.resolve()))
            self.assertTrue(Path(raw_path_arg).is_absolute())

    def test_should_validate_existing_strats_inputs_when_prepare_runs_before_run_strats(self):
        context = SimpleNamespace(args=SimpleNamespace(
            stages=["preprocessing", "tagging", "trees", "prepare-strats", "run-strats"],
            dry_run=False,
            validate_only=False,
        ))
        self.assertFalse(router.should_validate_existing_strats_inputs(context))

    def test_should_validate_existing_strats_inputs_when_prepare_is_absent(self):
        context = SimpleNamespace(args=SimpleNamespace(
            stages=["run-strats"],
            dry_run=False,
            validate_only=False,
        ))
        self.assertTrue(router.should_validate_existing_strats_inputs(context))

    def test_should_validate_existing_strats_inputs_remains_read_only_in_dry_run(self):
        context = SimpleNamespace(args=SimpleNamespace(
            stages=["run-strats"],
            dry_run=True,
            validate_only=False,
        ))
        self.assertTrue(router.should_validate_existing_strats_inputs(context))


if __name__ == "__main__":
    unittest.main()

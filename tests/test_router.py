import importlib.util
import sys
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

    def test_should_validate_existing_strats_inputs_skips_dry_run(self):
        context = SimpleNamespace(args=SimpleNamespace(
            stages=["run-strats"],
            dry_run=True,
            validate_only=False,
        ))
        self.assertFalse(router.should_validate_existing_strats_inputs(context))


if __name__ == "__main__":
    unittest.main()

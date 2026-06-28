import importlib.util
import sys
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()

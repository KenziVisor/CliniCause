from __future__ import annotations

import importlib.util
import argparse
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
SPEC = importlib.util.spec_from_file_location("causal_main_stage_scope", REPO / "main.py")
causal_main = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = causal_main
assert SPEC.loader is not None
SPEC.loader.exec_module(causal_main)


def parse(*extra: str):
    return causal_main.parse_args(["--dataset", "physionet", *extra])


def extraction_context(temp_root: Path):
    voters = temp_root / "voters"
    voters.mkdir()
    args = parse(
        "--causal-stages",
        "graph,majority_vote",
        "--latent-tags-dir",
        str(voters),
        "--output-dir",
        str(temp_root / "output"),
    )
    return causal_main.build_run_context(args)


class CausalStageScopeTests(unittest.TestCase):
    def test_causal_selector_defaults_to_all(self):
        args = parse("--validate-config-only")
        self.assertEqual(args.causal_stage_selector, "all")
        self.assertEqual(args.selected_causal_stages, causal_main.STAGE_SEQUENCE)

    def test_causal_prefix_is_canonicalized(self):
        args = parse(
            "--causal-stages",
            " graph , majority_vote ",
            "--validate-config-only",
        )
        self.assertEqual(args.causal_stage_selector, "graph,majority_vote")
        self.assertEqual(args.selected_causal_stages, ["graph", "majority_vote"])

    def test_invalid_causal_selectors_are_rejected(self):
        for selector in (
            "unknown",
            "majority_vote",
            "graph,matching",
            "majority_vote,graph",
            "graph,graph",
        ):
            with self.subTest(selector=selector), self.assertRaises(
                argparse_error_types()
            ):
                parse("--causal-stages", selector)

    def test_extraction_does_not_require_pickle_or_downstream_scripts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            context = extraction_context(root)
            self.assertIsNone(context.dataset_pkl_path)
            for stage_name in causal_main.STAGE_SEQUENCE[2:]:
                context.stages[stage_name].script_path = str(root / "missing.py")
            causal_main.prepare_output_directories(context)
            causal_main.validate_context(context)
            self.assertFalse(context.stage_dirs["mortality_prediction"].exists())
            self.assertFalse(context.stage_dirs["cate_estimation"].exists())

    def test_extraction_runs_only_selected_stages_and_writes_summary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            context = extraction_context(root)
            causal_main.prepare_output_directories(context)
            causal_main.validate_context(context)
            launched: list[str] = []

            def fake_run(stage, command, cwd, env, lock):
                del command, cwd, env, lock
                launched.append(stage.name)
                for key in stage.required_output_keys:
                    output = Path(stage.output_paths[key])
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text("synthetic", encoding="utf-8")
                stage.status = causal_main.STATUS_SUCCESS
                return True

            with mock.patch.object(causal_main, "run_stage_subprocess", fake_run), mock.patch.object(
                causal_main.threading,
                "Thread",
                side_effect=AssertionError("extraction started a background thread"),
            ):
                success, error = causal_main.orchestrate(context)

            self.assertTrue(success)
            self.assertIsNone(error)
            self.assertEqual(launched, ["graph", "majority_vote"])
            self.assertFalse(context.stage_dirs["mortality_prediction"].exists())
            self.assertFalse(context.stage_dirs["matching"].exists())

            causal_main.write_run_summary(context, "success", None)
            summary = json.loads(context.summary_path.read_text(encoding="utf-8"))
            self.assertEqual(summary["overall_status"], "success")
            self.assertEqual(summary["causal_stage_selector"], "graph,majority_vote")
            self.assertEqual(
                summary["selected_causal_stages"], ["graph", "majority_vote"]
            )
            self.assertTrue(
                summary["terminal_artifact"].endswith(
                    "majority_vote/latent_tags_majority_vote.csv"
                )
            )
            for stage_name in causal_main.STAGE_SEQUENCE[2:]:
                stage = summary["stages"][stage_name]
                self.assertEqual(stage["status"], "skipped")
                self.assertIn("Not selected by causal stage scope", stage["skip_reason"])

    def test_missing_majority_vote_output_fails_selected_stage(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            context = extraction_context(Path(temp_dir))
            causal_main.prepare_output_directories(context)
            completed = mock.Mock(returncode=0)
            with mock.patch.object(causal_main.subprocess, "run", return_value=completed):
                stage = context.stages["majority_vote"]
                success = causal_main.run_stage_subprocess(
                    stage,
                    causal_main.build_majority_vote_command(context),
                    context.repo_root,
                    causal_main.build_env(),
                    causal_main.threading.Lock(),
                )
            self.assertFalse(success)
            self.assertEqual(stage.status, "failed")
            self.assertIn("was not created", stage.error)

    def test_validate_only_reports_selected_commands_and_omissions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            voters = root / "voters"
            voters.mkdir()
            args = parse(
                "--causal-stages",
                "graph,majority_vote",
                "--latent-tags-dir",
                str(voters),
                "--output-dir",
                str(root / "output"),
                "--validate-config-only",
            )
            context = causal_main.build_run_context(args)
            output = io.StringIO()
            with redirect_stdout(output):
                causal_main.validate_config_only(args, context)
            text = output.getvalue()
            self.assertIn("graph:", text)
            self.assertIn("majority_vote:", text)
            self.assertIn("mortality_prediction: SKIPPED - Not selected", text)
            self.assertNotIn("mortality_prediction_using_latents.py", text)


def argparse_error_types():
    return (SystemExit, argparse.ArgumentTypeError, ValueError, TypeError)


if __name__ == "__main__":
    unittest.main()

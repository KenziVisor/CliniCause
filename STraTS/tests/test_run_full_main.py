import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "run_full_main.sh"


def option_value(command, option):
    return command[command.index(option) + 1]


class RunFullMainContractTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.log_path = self.root / "commands.jsonl"
        self.fake_python = self.root / "fake_python"
        self.fake_python.write_text(
            "#!/usr/bin/env python3\n"
            "import json, os, sys\n"
            "with open(os.environ['COMMAND_LOG'], 'a', encoding='utf-8') as handle:\n"
            "    handle.write(json.dumps(sys.argv[1:]) + '\\n')\n",
            encoding="utf-8",
        )
        self.fake_python.chmod(0o755)

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_wrapper(self, scope, **overrides):
        if self.log_path.exists():
            self.log_path.unlink()
        env = os.environ.copy()
        env.update({
            "PYTHON": str(self.fake_python),
            "COMMAND_LOG": str(self.log_path),
            "STRATS_INPUT_ROOT": str(self.root / "run" / "strats" / "inputs"),
            "STRATS_OUTPUT_ROOT": str(self.root / "run" / "strats" / "outputs"),
            "CLINICAUSE_RUN_ID": "synthetic-run",
            "STRATS_CONFIG_FINGERPRINT": "config-sha256",
            "STRATS_BASE_SEED": "0",
        })
        env.update({key: str(value) for key, value in overrides.items()})
        if scope is None:
            env.pop("DATASET_SCOPE", None)
        else:
            env["DATASET_SCOPE"] = scope
        result = subprocess.run(
            ["bash", str(SCRIPT_PATH)],
            cwd=self.root,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        commands = []
        if self.log_path.exists():
            commands = [json.loads(line) for line in self.log_path.read_text().splitlines()]
        return result, commands

    def test_each_supported_scope_selects_exact_datasets(self):
        cases = {
            "physionet": (11, {"physionet_2012"}),
            "mimic": (11, {"mimic_iii"}),
            "both": (22, {"physionet_2012", "mimic_iii"}),
            "physionet,mimic": (22, {"physionet_2012", "mimic_iii"}),
            "mimic,physionet": (22, {"physionet_2012", "mimic_iii"}),
            None: (22, {"physionet_2012", "mimic_iii"}),
        }
        for scope, (expected_count, expected_datasets) in cases.items():
            with self.subTest(scope=scope):
                result, commands = self.run_wrapper(scope)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(len(commands), expected_count)
                self.assertEqual(
                    {option_value(command, "--dataset") for command in commands},
                    expected_datasets,
                )

    def test_empty_unknown_and_substring_scopes_fail_before_model_calls(self):
        for scope in ("", "unknown", "notphysionet", "mimic-extra"):
            with self.subTest(scope=scope):
                result, commands = self.run_wrapper(scope)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(commands, [])
                self.assertIn("DATASET_SCOPE", result.stderr)

    def test_singular_child_uses_explicit_roots_and_provenance(self):
        result, commands = self.run_wrapper("physionet")
        self.assertEqual(result.returncode, 0, result.stderr)
        input_root = self.root / "run" / "strats" / "inputs"
        output_root = self.root / "run" / "strats" / "outputs"

        for command in commands:
            self.assertEqual(
                option_value(command, "--processed_data_path"),
                str(input_root / "processed" / "physionet_2012.pkl"),
            )
            self.assertEqual(
                option_value(command, "--latent_csv_path"),
                str(input_root / "physionet_latent_tags.csv"),
            )
            self.assertEqual(option_value(command, "--pipeline_run_id"), "synthetic-run")
            self.assertEqual(option_value(command, "--config_fingerprint"), "config-sha256")
            self.assertEqual(option_value(command, "--base_seed"), "0")
            self.assertEqual(option_value(command, "--dataset_seed"), "100000")
            self.assertTrue(Path(option_value(command, "--output_dir")).is_relative_to(output_root))
            self.assertEqual(command[0], str(REPO_ROOT / "src" / "main.py"))

        output_directories = {
            Path(option_value(command, "--output_dir"))
            .relative_to(output_root)
            .as_posix()
            for command in commands
        }
        self.assertEqual(
            output_directories,
            {
                "models/strats_pretrain",
                "models/strats",
                "models/gru",
                "models/grud",
                "models/tcn",
                "models/sand",
            },
        )

        init_commands = [command for command in commands if "--init_ckpt_path" in command]
        restore_commands = [command for command in commands if "--restore_ckpt_path" in command]
        self.assertEqual(len(init_commands), 1)
        self.assertEqual(len(restore_commands), 5)
        self.assertNotIn("--restore_ckpt_path", init_commands[0])
        prediction_paths = {
            Path(option_value(command, "--save_pred_csv_path")).relative_to(output_root).as_posix()
            for command in restore_commands
        }
        self.assertEqual(
            prediction_paths,
            {
                "predictions/strats.csv",
                "predictions/gru.csv",
                "predictions/grud.csv",
                "predictions/tcn.csv",
                "predictions/sand.csv",
            },
        )

    def test_model_seeds_are_explicit_stable_and_match_training_to_export(self):
        first_result, first_commands = self.run_wrapper("mimic")
        second_result, second_commands = self.run_wrapper("mimic")
        self.assertEqual(first_result.returncode, 0, first_result.stderr)
        self.assertEqual(second_result.returncode, 0, second_result.stderr)
        first_seeds = [option_value(command, "--seed") for command in first_commands]
        second_seeds = [option_value(command, "--seed") for command in second_commands]
        self.assertEqual(first_seeds, second_seeds)
        self.assertTrue(all(option_value(command, "--dataset_seed") == "200000" for command in first_commands))

        seeds_by_model = {}
        for command in first_commands:
            model = option_value(command, "--model_type")
            seeds_by_model.setdefault(model, set()).add(option_value(command, "--seed"))
        self.assertTrue(all(len(seeds) == 1 for seeds in seeds_by_model.values()))
        self.assertEqual(len({next(iter(seeds)) for seeds in seeds_by_model.values()}), 5)

    def test_explicitly_empty_roots_and_provenance_fail_before_model_calls(self):
        cases = {
            "CLINICAUSE_RUN_ID": "CLINICAUSE_RUN_ID",
            "STRATS_CONFIG_FINGERPRINT": "STRATS_CONFIG_FINGERPRINT",
            "STRATS_INPUT_ROOT": "STRATS_INPUT_ROOT",
            "STRATS_OUTPUT_ROOT": "STRATS_OUTPUT_ROOT",
        }
        for variable, expected_error in cases.items():
            with self.subTest(variable=variable):
                result, commands = self.run_wrapper(
                    "physionet", **{variable: ""}
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(commands, [])
                self.assertIn(expected_error, result.stderr)

    def test_empty_seed_fails_before_model_calls(self):
        result, commands = self.run_wrapper("physionet", STRATS_BASE_SEED="")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(commands, [])
        self.assertIn("STRATS_BASE_SEED", result.stderr)


if __name__ == "__main__":
    unittest.main()

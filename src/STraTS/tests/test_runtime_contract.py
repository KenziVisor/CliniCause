import sys
import unittest
from pathlib import Path
from types import SimpleNamespace


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from runtime_contract import (
    SEED_MODULUS,
    derive_dataset_seed,
    derive_effective_seed,
    derive_model_seed,
    model_config_from_args,
    parse_model_run,
    scientific_config_fingerprint,
    training_config_from_args,
    validate_base_seed,
)


class RuntimeContractTests(unittest.TestCase):
    def test_seed_zero_is_valid_and_derives_stably(self):
        self.assertEqual(validate_base_seed(0), 0)
        self.assertEqual(derive_dataset_seed(0, "physionet_2012"), 100000)
        self.assertEqual(derive_dataset_seed(0, "mimic_iii"), 200000)
        self.assertEqual(derive_model_seed(0, "physionet_2012", "strats"), 100001)
        self.assertEqual(derive_effective_seed(100001, "1o10"), 100002)

    def test_dataset_and_model_seeds_are_distinct_and_order_independent(self):
        first = {
            (dataset, model): derive_model_seed(42, dataset, model)
            for dataset in ("physionet_2012", "mimic_iii")
            for model in ("strats", "gru", "tcn")
        }
        second = {
            (dataset, model): derive_model_seed(42, dataset, model)
            for model in ("tcn", "gru", "strats")
            for dataset in ("mimic_iii", "physionet_2012")
        }
        self.assertEqual(first, second)
        self.assertEqual(len(set(first.values())), len(first))

    def test_seed_range_is_enforced(self):
        for invalid in (-1, SEED_MODULUS, 1.5, True):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    validate_base_seed(invalid)

    def test_model_run_is_validated(self):
        self.assertEqual(parse_model_run("2o10"), (2, 10))
        for invalid in ("0o10", "11o10", "1/10", "one"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    parse_model_run(invalid)

    def test_model_config_records_architecture_and_scientific_arguments(self):
        args = SimpleNamespace(
            model_type="gru",
            hid_dim=64,
            dropout=0.2,
            train_frac=0.5,
            run="1o10",
            max_epochs=100,
            max_steps=200,
            patience=10,
            lr=5e-4,
            train_batch_size=16,
            gradient_accumulation_steps=1,
            eval_batch_size=32,
            validate_after=-1,
            validate_every=4,
            save_pred_csv_path="operational.csv",
        )
        config = model_config_from_args(args, "scratch")

        self.assertEqual(config["architecture_mode"], "scratch")
        self.assertEqual(config["model_type"], "gru")
        self.assertEqual(config["train_frac"], 0.5)
        self.assertNotIn("max_epochs", config)
        self.assertNotIn("save_pred_csv_path", config)

        training = training_config_from_args(args)
        self.assertEqual(training["max_epochs"], 100)
        self.assertEqual(training["max_steps"], 200)
        self.assertEqual(training["lr"], 5e-4)
        first = scientific_config_fingerprint(config, training)
        second = scientific_config_fingerprint(dict(reversed(list(config.items()))), training)
        self.assertEqual(first, second)
        changed = dict(training)
        changed["lr"] = 0.9
        self.assertNotEqual(first, scientific_config_fingerprint(config, changed))


if __name__ == "__main__":
    unittest.main()

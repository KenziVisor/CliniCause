import json
import sys
import tempfile
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from runtime_contract import scientific_config_fingerprint

from artifact_metadata import (
    build_artifact_metadata,
    cohort_descriptor,
    file_descriptor,
    metadata_path_for,
    sanitize_command,
    validate_artifact_metadata,
    write_metadata,
)


class ArtifactMetadataTests(unittest.TestCase):
    def _create_artifact_and_metadata(self, root: Path):
        artifact = root / "predictions" / "strats.csv"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("ts_id,a_prob,a\n1,0.75,1\n", encoding="utf-8")
        processed = root / "inputs" / "processed.pkl"
        processed.parent.mkdir(parents=True)
        processed.write_bytes(b"synthetic-processed")
        labels = root / "inputs" / "labels.csv"
        labels.write_text("ts_id,a\n1,1\n", encoding="utf-8")
        metadata = build_artifact_metadata(
            artifact,
            artifact_kind="prediction",
            pipeline_run_id="run-001",
            dataset="physionet_2012",
            model="strats",
            architecture_mode="finetune",
            ordered_targets=["a"],
            config_fingerprint="cfg-sha256",
            base_seed=0,
            dataset_seed=100000,
            model_seed=100001,
            effective_seed=100002,
            producing_command=["python", "main.py", "--token", "private-value"],
            schema={"columns": ["ts_id", "a_prob", "a"]},
            cohort_ids=["1"],
            model_config={"hid_dim": 64, "num_layers": 2},
            training_config={
                "max_epochs": 50,
                "max_steps": 100,
                "patience": 10,
                "lr": 5e-5,
                "train_batch_size": 16,
                "gradient_accumulation_steps": 1,
                "eval_batch_size": 32,
                "validate_after": -1,
                "validate_every": 2,
            },
            inputs={
                "processed_data": file_descriptor(processed),
                "latent_tags": file_descriptor(labels),
            },
        )
        write_metadata(artifact, metadata)
        return artifact, metadata

    def test_exact_metadata_and_seed_zero_validate(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, metadata = self._create_artifact_and_metadata(Path(temp_dir))

            loaded = validate_artifact_metadata(
                artifact,
                expected={
                    "pipeline_run_id": "run-001",
                    "dataset": "physionet_2012",
                    "model": "strats",
                    "ordered_targets": ["a"],
                    "config_fingerprint": "cfg-sha256",
                    "base_seed": 0,
                    "cohort": cohort_descriptor(["1"]),
                },
            )

            self.assertEqual(loaded, metadata)
            self.assertEqual(loaded["base_seed"], 0)
            self.assertEqual(loaded["producing_command"][-1], "<redacted>")
            self.assertEqual(
                metadata_path_for(artifact),
                Path(str(artifact) + ".metadata.json"),
            )

    def test_artifact_digest_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, _ = self._create_artifact_and_metadata(Path(temp_dir))
            artifact.write_text("tampered", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "digest does not match"):
                validate_artifact_metadata(artifact)

    def test_each_provenance_identity_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, _ = self._create_artifact_and_metadata(Path(temp_dir))
            mismatches = {
                "pipeline_run_id": "other-run",
                "dataset": "mimic_iii",
                "model": "gru",
                "ordered_targets": ["b"],
                "config_fingerprint": "other-config",
                "base_seed": 1,
                "model_seed": 7,
                "schema": {"columns": ["wrong"]},
                "cohort": cohort_descriptor(["9"]),
            }
            for field, wrong_value in mismatches.items():
                with self.subTest(field=field):
                    with self.assertRaisesRegex(ValueError, "Metadata mismatch"):
                        validate_artifact_metadata(
                            artifact,
                            expected={field: wrong_value},
                        )

    def test_scientific_config_fingerprint_tamper_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, metadata = self._create_artifact_and_metadata(Path(temp_dir))
            metadata["training_config"]["lr"] = 0.9
            metadata_path_for(artifact).write_text(
                json.dumps(metadata), encoding="utf-8"
            )

            with self.assertRaisesRegex(
                ValueError, "scientific configuration fingerprint"
            ):
                validate_artifact_metadata(artifact)

    def test_incomplete_training_config_fails_even_with_matching_fingerprint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, metadata = self._create_artifact_and_metadata(Path(temp_dir))
            metadata["training_config"].pop("max_epochs")
            metadata["scientific_config_fingerprint"] = scientific_config_fingerprint(
                metadata["model_config"], metadata["training_config"]
            )
            metadata_path_for(artifact).write_text(
                json.dumps(metadata), encoding="utf-8"
            )

            with self.assertRaisesRegex(ValueError, "Training configuration fields"):
                validate_artifact_metadata(artifact)

    def test_missing_required_field_fails(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact, metadata = self._create_artifact_and_metadata(Path(temp_dir))
            metadata.pop("ordered_targets")
            metadata_path_for(artifact).write_text(json.dumps(metadata), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "missing required fields"):
                validate_artifact_metadata(artifact)

    def test_duplicate_cohort_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate canonical IDs"):
            cohort_descriptor(["1", "1"])

    def test_sanitize_command_redacts_inline_secret(self):
        self.assertEqual(
            sanitize_command(["python", "--api-key=value"]),
            ["python", "--api-key=<redacted>"],
        )


if __name__ == "__main__":
    unittest.main()

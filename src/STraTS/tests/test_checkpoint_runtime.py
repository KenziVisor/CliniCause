import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from artifact_metadata import (
    build_artifact_metadata,
    cohort_descriptor,
    file_descriptor,
    write_metadata,
)
from checkpoint_runtime import (
    PREPROCESSING_STATE_FILENAME,
    build_runtime_metadata,
    input_descriptors,
    prepare_checkpoint_roles,
    validate_restored_dataset,
)
from runtime_contract import model_config_from_args, training_config_from_args


class CheckpointRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.processed = self.root / "inputs" / "processed" / "physionet_2012.pkl"
        self.labels = self.root / "inputs" / "physionet_latent_tags.csv"
        self.processed.parent.mkdir(parents=True)
        self.processed.write_bytes(b"synthetic processed artifact")
        self.labels.write_text("ts_id,a\n1,1\n2,0\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_args(self, output_name="restore"):
        return SimpleNamespace(
            pretrain=0,
            init_ckpt_path=None,
            restore_ckpt_path=None,
            model_type="strats",
            dataset="physionet_2012",
            pipeline_run_id="run-1",
            config_fingerprint="config-fingerprint",
            base_seed=0,
            dataset_seed=100000,
            seed=100001,
            effective_seed=100002,
            processed_data_path=str(self.processed),
            latent_csv_path=str(self.labels),
            output_dir=str(self.root / output_name),
            train_frac=0.5,
            run="1o10",
            hid_dim=64,
            num_layers=2,
            num_heads=16,
            dropout=0.2,
            attention_dropout=0.2,
            kernel_size=4,
            r=24,
            M=12,
            max_obs=880,
            max_timesteps=880,
            hours_look_ahead=24,
            ref_points=24,
            max_epochs=50,
            max_steps=150,
            patience=10,
            lr=5e-5,
            train_batch_size=16,
            gradient_accumulation_steps=1,
            eval_batch_size=32,
            validate_after=-1,
            validate_every=3,
            finetune=False,
            preprocessing_state_path=None,
            restore_metadata=None,
        )

    def write_checkpoint_metadata(self, checkpoint, args, architecture, preprocessing=None, schema=None):
        checkpoint.parent.mkdir(parents=True, exist_ok=True)
        checkpoint.write_bytes(b"synthetic checkpoint")
        metadata = build_artifact_metadata(
            checkpoint,
            artifact_kind="checkpoint",
            pipeline_run_id=args.pipeline_run_id,
            dataset=args.dataset,
            model=args.model_type,
            architecture_mode=architecture,
            ordered_targets=[] if architecture == "pretrain" else ["a"],
            config_fingerprint=args.config_fingerprint,
            base_seed=args.base_seed,
            dataset_seed=args.dataset_seed,
            model_seed=args.seed,
            effective_seed=args.effective_seed,
            producing_command=["python", "main.py"],
            schema=schema or {"format": "pytorch_state_dict", "version": 1},
            cohort_ids=["1", "2"],
            model_config=model_config_from_args(args, architecture),
            training_config=training_config_from_args(args),
            inputs=input_descriptors(args, pretrain=architecture == "pretrain"),
            preprocessing_state=preprocessing,
        )
        write_metadata(checkpoint, metadata)

    def test_pretrain_init_copies_verified_state_and_selects_finetune_architecture(self):
        args = self.make_args("finetune")
        checkpoint = self.root / "pretrain" / "checkpoint_best.bin"
        state = checkpoint.parent / PREPROCESSING_STATE_FILENAME
        state.parent.mkdir(parents=True)
        state.write_bytes(b"variables and normalization")
        self.write_checkpoint_metadata(
            checkpoint,
            args,
            "pretrain",
            preprocessing=file_descriptor(state),
        )
        args.init_ckpt_path = str(checkpoint)

        prepare_checkpoint_roles(args)
        dataset = SimpleNamespace(
            authoritative_splits={"train": ["1"], "val": ["2"], "test": []}
        )
        validate_restored_dataset(args, dataset)

        copied = Path(args.preprocessing_state_path)
        self.assertTrue(args.finetune)
        self.assertEqual(copied.parent, Path(args.output_dir))
        self.assertEqual(copied.read_bytes(), state.read_bytes())
        self.assertEqual(
            input_descriptors(args)["initialization_checkpoint"],
            file_descriptor(checkpoint),
        )

    def test_scratch_restore_reconstructs_scratch_and_validates_target_cohort(self):
        args = self.make_args("scratch")
        checkpoint = Path(args.output_dir) / "checkpoint_best.bin"
        self.write_checkpoint_metadata(checkpoint, args, "scratch")
        args.restore_ckpt_path = str(checkpoint)

        prepare_checkpoint_roles(args)
        dataset = SimpleNamespace(target_columns=["a"], metadata_cohort_ids=["1", "2"])
        validate_restored_dataset(args, dataset)

        self.assertFalse(args.finetune)
        self.assertIsNotNone(args.restore_metadata)
        self.assertIsNone(args.preprocessing_state_path)

    def test_restore_rejects_reordered_or_changed_targets(self):
        args = self.make_args("scratch")
        checkpoint = Path(args.output_dir) / "checkpoint_best.bin"
        self.write_checkpoint_metadata(checkpoint, args, "scratch")
        args.restore_ckpt_path = str(checkpoint)
        prepare_checkpoint_roles(args)

        with self.assertRaisesRegex(ValueError, "ordered_targets"):
            validate_restored_dataset(
                args,
                SimpleNamespace(target_columns=["b"], metadata_cohort_ids=["1", "2"]),
            )

    def test_pretrain_init_rejects_wrong_authoritative_cohort(self):
        args = self.make_args("wrong-init-cohort")
        checkpoint = self.root / "pretrain-wrong-cohort" / "checkpoint_best.bin"
        state = checkpoint.parent / PREPROCESSING_STATE_FILENAME
        state.parent.mkdir(parents=True)
        state.write_bytes(b"variables and normalization")
        self.write_checkpoint_metadata(
            checkpoint,
            args,
            "pretrain",
            preprocessing=file_descriptor(state),
        )
        args.init_ckpt_path = str(checkpoint)
        prepare_checkpoint_roles(args)

        with self.assertRaisesRegex(ValueError, "cohort"):
            validate_restored_dataset(
                args,
                SimpleNamespace(
                    authoritative_splits={
                        "train": ["1"],
                        "val": ["3"],
                        "test": [],
                    }
                ),
            )

    def test_restore_rejects_wrong_checkpoint_schema(self):
        args = self.make_args("wrong-schema")
        checkpoint = Path(args.output_dir) / "checkpoint_best.bin"
        self.write_checkpoint_metadata(
            checkpoint,
            args,
            "scratch",
            schema={"format": "pytorch_state_dict", "version": 2},
        )
        args.restore_ckpt_path = str(checkpoint)

        with self.assertRaisesRegex(ValueError, "schema.version"):
            prepare_checkpoint_roles(args)

    def test_prediction_metadata_binds_exact_checkpoint_descriptor(self):
        args = self.make_args("prediction")
        checkpoint = Path(args.output_dir) / "checkpoint_best.bin"
        self.write_checkpoint_metadata(checkpoint, args, "scratch")
        args.restore_ckpt_path = str(checkpoint)
        prepare_checkpoint_roles(args)
        dataset = SimpleNamespace(
            target_columns=["a"],
            metadata_cohort_ids=["1", "2"],
        )
        prediction = Path(args.output_dir) / "prediction.csv"
        prediction.write_text(
            "ts_id,a_prob,a\n2,0.1,0\n",
            encoding="utf-8",
        )

        metadata = build_runtime_metadata(
            args,
            dataset,
            str(prediction),
            artifact_kind="prediction",
            schema={
                "columns": ["ts_id", "a_prob", "a"],
                "probability_range": [0.0, 1.0],
                "binary_values": [0, 1],
            },
            producing_command=["python", "main.py"],
            cohort_ids=["2"],
        )

        self.assertEqual(
            metadata["inputs"]["checkpoint"],
            file_descriptor(checkpoint),
        )
        self.assertEqual(
            metadata["training_config"],
            args.restore_metadata["training_config"],
        )
        self.assertEqual(metadata["cohort"], cohort_descriptor(["2"]))

    def test_finetune_restore_requires_bound_preprocessing_state(self):
        args = self.make_args("finetune")
        checkpoint = Path(args.output_dir) / "checkpoint_best.bin"
        self.write_checkpoint_metadata(checkpoint, args, "finetune", preprocessing=None)
        args.restore_ckpt_path = str(checkpoint)

        with self.assertRaisesRegex(ValueError, "preprocessing_state"):
            prepare_checkpoint_roles(args)


if __name__ == "__main__":
    unittest.main()

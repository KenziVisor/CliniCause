import sys
import unittest
from pathlib import Path
import pandas as pd
import numpy as np


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from split_contract import (
    require_ids_present,
    require_no_excluded_indices,
    restrict_frames_to_split_cohort,
    validate_split_contract,
)


class SplitContractTests(unittest.TestCase):
    def test_valid_partition_preserves_authoritative_order_and_full_cohort(self):
        result = validate_split_contract(
            event_ids=["4", "1", "2", "3", "4"],
            outcome_ids=["1", "2", "3", "4"],
            train_ids=["2", "1"],
            val_ids=["4"],
            test_ids=["3"],
        )

        self.assertEqual(result.train, ("2", "1"))
        self.assertEqual(result.val, ("4",))
        self.assertEqual(result.test, ("3",))
        self.assertEqual(result.full_cohort, ("2", "1", "4", "3"))

    def test_duplicate_within_split_fails(self):
        with self.assertRaisesRegex(ValueError, "duplicate canonical IDs"):
            validate_split_contract(
                ["1", "2", "3"],
                ["1", "2", "3"],
                ["1", "1"],
                ["2"],
                ["3"],
            )

    def test_pairwise_overlap_fails(self):
        with self.assertRaisesRegex(ValueError, "train and val splits overlap"):
            validate_split_contract(
                ["1", "2", "3"],
                ["1", "2", "3"],
                ["1"],
                ["1", "2"],
                ["3"],
            )

    def test_unknown_and_missing_split_ids_fail(self):
        with self.assertRaisesRegex(ValueError, "unknown IDs=1.*missing IDs=1"):
            validate_split_contract(
                ["1", "2", "3"],
                ["1", "2", "3"],
                ["1", "9"],
                ["2"],
                [],
            )

    def test_event_outcome_cohort_mismatch_fails(self):
        with self.assertRaisesRegex(ValueError, "Event/outcome canonical cohorts differ"):
            validate_split_contract(
                ["1", "2", "3"],
                ["1", "2", "4"],
                ["1"],
                ["2"],
                ["3"],
            )

    def test_duplicate_outcome_id_fails(self):
        with self.assertRaisesRegex(ValueError, "outcome_ids contains duplicate"):
            validate_split_contract(
                ["1", "2", "3"],
                ["1", "2", "2", "3"],
                ["1"],
                ["2"],
                ["3"],
            )

    def test_post_transform_missing_id_fails_instead_of_intersecting(self):
        with self.assertRaisesRegex(ValueError, "removed 1 canonical cohort IDs"):
            require_ids_present(["1", "2", "3"], ["1", "3"], "synthetic transform")

    def test_empty_canonical_cohort_fails(self):
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            validate_split_contract([], [], [], [], [])

    def test_pandas_na_identifier_fails(self):
        with self.assertRaisesRegex(ValueError, "missing canonical IDs"):
            validate_split_contract(
                ["1", pd.NA],
                ["1", "2"],
                ["1"],
                ["2"],
                [],
            )

    def test_native_frames_are_restricted_to_authoritative_split_union(self):
        events = pd.DataFrame(
            {
                "ts_id": ["extra", "2", "1", "2"],
                "value": [0.0, 2.0, 1.0, 3.0],
            }
        )
        outcomes = pd.DataFrame(
            {
                "ts_id": ["extra", "1", "2"],
                "mortality": [0, 0, 1],
            }
        )
        train = np.asarray(["2"], dtype=object)
        val = np.asarray(["1"], dtype=object)
        test = np.asarray([], dtype=object)

        filtered_events, filtered_outcomes = restrict_frames_to_split_cohort(
            events, outcomes, train, val, test
        )

        self.assertEqual(filtered_events["ts_id"].tolist(), ["2", "1", "2"])
        self.assertEqual(filtered_outcomes["ts_id"].tolist(), ["1", "2"])
        validated = validate_split_contract(
            filtered_events["ts_id"],
            filtered_outcomes["ts_id"],
            train,
            val,
            test,
        )
        self.assertEqual(validated.full_cohort, ("2", "1"))

    def test_pretrain_eligibility_cannot_silently_shrink_cohort(self):
        with self.assertRaisesRegex(
            ValueError, "removed 1 canonical cohort IDs.*2"
        ):
            require_no_excluded_indices(
                ["1", "2", "3"],
                [1],
                "Pretraining forecast-window eligibility",
            )

    def test_training_subset_does_not_change_authoritative_export_cohort(self):
        result = validate_split_contract(
            event_ids=["1", "2", "3", "4", "5"],
            outcome_ids=["1", "2", "3", "4", "5"],
            train_ids=["1", "2", "3"],
            val_ids=["4"],
            test_ids=["5"],
        )
        selected_training_ids = result.train[:2]

        self.assertEqual(selected_training_ids, ("1", "2"))
        self.assertEqual(set(result.full_cohort), {"1", "2", "3", "4", "5"})


if __name__ == "__main__":
    unittest.main()

"""Pure validation helpers for split-aware STraTS artifacts."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import math
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ValidatedSplits:
    """Validated split values, preserving their authoritative order."""

    train: tuple[object, ...]
    val: tuple[object, ...]
    test: tuple[object, ...]

    @property
    def full_cohort(self) -> tuple[object, ...]:
        return self.train + self.val + self.test


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, float):
        return math.isnan(value)
    try:
        result = value != value
        if result is True:
            return True
        try:
            return bool(result)
        except (TypeError, ValueError):
            return True
    except Exception:
        return False


def _materialize(values: Iterable[object], name: str) -> tuple[object, ...]:
    materialized = tuple(values)
    missing_positions = [index for index, value in enumerate(materialized) if _is_missing(value)]
    if missing_positions:
        raise ValueError(
            f"{name} contains missing canonical IDs at positions {missing_positions[:10]}."
        )
    return materialized


def _duplicates(values: Sequence[object]) -> list[object]:
    return [value for value, count in Counter(values).items() if count > 1]


def _sample(values: Iterable[object], limit: int = 10) -> list[str]:
    return sorted((str(value) for value in values))[:limit]


def validate_split_contract(
    event_ids: Iterable[object],
    outcome_ids: Iterable[object],
    train_ids: Iterable[object],
    val_ids: Iterable[object],
    test_ids: Iterable[object],
) -> ValidatedSplits:
    """Validate an exact, pairwise-disjoint partition of the canonical cohort.

    Event IDs may repeat because the event table has multiple rows per stay.
    Outcome IDs and every split must contain each stay at most once.
    """

    events = _materialize(event_ids, "event_ids")
    outcomes = _materialize(outcome_ids, "outcome_ids")
    train = _materialize(train_ids, "train_ids")
    val = _materialize(val_ids, "val_ids")
    test = _materialize(test_ids, "test_ids")

    if not events or not outcomes:
        raise ValueError(
            "The canonical event/outcome cohort must not be empty."
        )

    duplicate_outcomes = _duplicates(outcomes)
    if duplicate_outcomes:
        raise ValueError(
            "outcome_ids contains duplicate canonical IDs: "
            f"{_sample(duplicate_outcomes)}"
        )

    named_splits = {"train": train, "val": val, "test": test}
    for split_name, split_values in named_splits.items():
        duplicate_ids = _duplicates(split_values)
        if duplicate_ids:
            raise ValueError(
                f"{split_name} split contains duplicate canonical IDs: "
                f"{_sample(duplicate_ids)}"
            )

    split_sets = {name: set(values) for name, values in named_splits.items()}
    for left_name, right_name in (("train", "val"), ("train", "test"), ("val", "test")):
        overlap = split_sets[left_name] & split_sets[right_name]
        if overlap:
            raise ValueError(
                f"{left_name} and {right_name} splits overlap on "
                f"{len(overlap)} canonical IDs: {_sample(overlap)}"
            )

    event_set = set(events)
    outcome_set = set(outcomes)
    if event_set != outcome_set:
        missing_outcomes = event_set - outcome_set
        outcomes_without_events = outcome_set - event_set
        raise ValueError(
            "Event/outcome canonical cohorts differ: "
            f"missing outcomes={len(missing_outcomes)} {_sample(missing_outcomes)}; "
            f"outcomes without events={len(outcomes_without_events)} "
            f"{_sample(outcomes_without_events)}"
        )

    split_union = split_sets["train"] | split_sets["val"] | split_sets["test"]
    unknown_ids = split_union - event_set
    missing_ids = event_set - split_union
    if unknown_ids or missing_ids:
        raise ValueError(
            "Split union does not equal the canonical cohort: "
            f"unknown IDs={len(unknown_ids)} {_sample(unknown_ids)}; "
            f"missing IDs={len(missing_ids)} {_sample(missing_ids)}"
        )

    return ValidatedSplits(train=train, val=val, test=test)


def require_ids_present(
    expected_ids: Iterable[object],
    available_ids: Iterable[object],
    context: str,
) -> None:
    """Fail instead of silently intersecting a split after a transformation."""

    missing = set(expected_ids) - set(available_ids)
    if missing:
        raise ValueError(
            f"{context} removed {len(missing)} canonical cohort IDs: {_sample(missing)}"
        )


def require_no_excluded_indices(
    canonical_ids: Sequence[object],
    excluded_indices: Iterable[int],
    context: str,
) -> None:
    """Fail when a transformation would silently remove canonical participants."""

    identifiers = tuple(canonical_ids)
    indices = tuple(int(index) for index in excluded_indices)
    invalid = [index for index in indices if index < 0 or index >= len(identifiers)]
    if invalid:
        raise ValueError(
            f"{context} reported invalid cohort indices: {invalid[:10]}"
        )
    removed_ids = [identifiers[index] for index in indices]
    if removed_ids:
        raise ValueError(
            f"{context} removed {len(removed_ids)} canonical cohort IDs: "
            f"{_sample(removed_ids)}"
        )


def restrict_frames_to_split_cohort(
    events: object,
    outcomes: object,
    train_ids: Iterable[object],
    val_ids: Iterable[object],
    test_ids: Iterable[object],
    *,
    id_column: str = "ts_id",
) -> tuple[object, object]:
    """Restrict native preprocessing frames to the declared supervised cohort."""

    for name, frame in (("events", events), ("outcomes", outcomes)):
        if id_column not in getattr(frame, "columns", ()):
            raise KeyError(f"{name} must contain canonical {id_column!r} values.")
    cohort = (
        _materialize(train_ids, "train_ids")
        + _materialize(val_ids, "val_ids")
        + _materialize(test_ids, "test_ids")
    )
    if not cohort:
        raise ValueError("The authoritative supervised split cohort must not be empty.")
    cohort_set = set(cohort)
    filtered_events = events.loc[events[id_column].isin(cohort_set)].copy()
    filtered_outcomes = outcomes.loc[outcomes[id_column].isin(cohort_set)].copy()
    return filtered_events, filtered_outcomes

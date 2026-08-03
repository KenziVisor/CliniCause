"""Strict, lossless canonicalization for STraTS stay identifiers."""

from __future__ import annotations

import math
import numbers
import re

import numpy as np
import pandas as pd


_CANONICAL_INTEGER_TEXT = re.compile(r"^(?:0|[1-9][0-9]*)(?:[.]0+)?$")


def canonicalize_stay_id_scalar(
    value: object,
    *,
    field_name: str = "stay identifier",
) -> str:
    """Return one lossless decimal representation for a stay identifier."""

    if value is None or value is pd.NA:
        raise ValueError(f"{field_name} contains a missing value.")
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{field_name} must not contain booleans.")

    if isinstance(value, numbers.Integral):
        integer = int(value)
        if integer < 0:
            raise ValueError(f"{field_name} must be a non-negative integer identifier.")
        return str(integer)

    if isinstance(value, numbers.Real):
        numeric = float(value)
        if not math.isfinite(numeric):
            raise ValueError(f"{field_name} must be finite.")
        if numeric < 0 or (numeric == 0 and math.copysign(1.0, numeric) < 0):
            raise ValueError(f"{field_name} must be a non-negative integer identifier.")
        if not numeric.is_integer():
            raise ValueError(f"{field_name} must not contain fractional identifiers.")
        if numeric > 2**53 - 1:
            raise ValueError(
                f"{field_name} exceeds the exact IEEE-754 integer range."
            )
        return str(int(numeric))

    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            raise ValueError(f"{field_name} contains a missing value.")
        if stripped != value:
            raise ValueError(f"{field_name} contains surrounding whitespace.")
        if _CANONICAL_INTEGER_TEXT.fullmatch(stripped) is None:
            raise ValueError(
                f"{field_name} must use plain, unpadded non-negative integer text "
                "with only an optional .0 suffix."
            )
        return stripped.split(".", maxsplit=1)[0]

    try:
        is_missing = bool(pd.isna(value))
    except (TypeError, ValueError):
        is_missing = False
    if is_missing:
        raise ValueError(f"{field_name} contains a missing value.")
    raise TypeError(
        f"{field_name} contains an unsupported value type: {type(value).__name__}."
    )


def canonicalize_stay_id_series(
    series: pd.Series,
    *,
    field_name: str | None = None,
) -> pd.Series:
    """Strictly canonicalize every value while retaining its original row index."""

    label = field_name or str(series.name or "stay identifier")
    normalized: list[str] = []
    for row_index, value in series.items():
        try:
            normalized.append(
                canonicalize_stay_id_scalar(value, field_name=label)
            )
        except (TypeError, ValueError) as error:
            raise type(error)(
                f"{error} Invalid row index: {row_index!r}."
            ) from error
    return pd.Series(
        normalized,
        index=series.index,
        dtype="object",
        name=series.name,
    )

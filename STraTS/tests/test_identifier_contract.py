import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from identifier_contract import canonicalize_stay_id_series


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (10, "10"),
        (np.int64(10), "10"),
        (10.0, "10"),
        ("10", "10"),
        ("10.0", "10"),
        (str(2**53), str(2**53)),
    ],
)
def test_exact_integer_representations_are_canonicalized(value, expected):
    result = canonicalize_stay_id_series(pd.Series([value], dtype="object"))
    assert result.tolist() == [expected]


def test_nonnull_nullable_integer_series_is_supported():
    values = pd.Series([10, 11], dtype="Int64", name="ts_id")
    assert canonicalize_stay_id_series(values).tolist() == ["10", "11"]


@pytest.mark.parametrize(
    "value",
    [
        None,
        pd.NA,
        np.nan,
        True,
        np.bool_(False),
        10.5,
        float(2**53),
        float(2**53 + 2),
        " 10.00 ",
        np.inf,
        -1,
        -0.0,
        "",
        "abc",
        "10.5",
        "1e1",
        "010",
        "+10",
        "-1",
        "NaN",
        "inf",
    ],
)
def test_missing_fractional_and_ambiguous_values_are_rejected(value):
    with pytest.raises((TypeError, ValueError)):
        canonicalize_stay_id_series(pd.Series([value], dtype="object"))

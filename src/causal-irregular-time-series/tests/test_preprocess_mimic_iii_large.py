from __future__ import annotations

import ast
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
WORKSPACE_ROOT = ROOT.parents[1]
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import preprocess_mimic_iii_large as preprocess


HISTORICAL_VARIABLES = {
    "ALP",
    "ALT",
    "AST",
    "Age",
    "Albumin",
    "Albumin 25%",
    "Albumin 5%",
    "Amiodarone",
    "Anion Gap",
    "BUN",
    "Base Excess",
    "Basophils",
    "Bicarbonate",
    "Bilirubin (Direct)",
    "Bilirubin (Indirect)",
    "Bilirubin (Total)",
    "CRR",
    "Calcium Free",
    "Calcium Gluconate",
    "Calcium Total",
    "Cefazolin",
    "Chest Tube",
    "Chloride",
    "Colloid",
    "Creatinine Blood",
    "Creatinine Urine",
    "D5W",
    "DBP",
    "Dextrose Other",
    "Dopamine",
    "EBL",
    "Emesis",
    "Eoisinophils",
    "Epinephrine",
    "Famotidine",
    "Fentanyl",
    "FiO2",
    "Fiber",
    "Free Water",
    "Fresh Frozen Plasma",
    "Furosemide",
    "GCS_eye",
    "GCS_motor",
    "GCS_verbal",
    "GT Flush",
    "Gastric",
    "Gastric Meds",
    "Gender",
    "Glucose (Blood)",
    "Glucose (Serum)",
    "Glucose (Whole Blood)",
    "HR",
    "Half Normal Saline",
    "Hct",
    "Height",
    "Heparin",
    "Hgb",
    "Hydralazine",
    "Hydromorphone",
    "INR",
    "Insulin Humalog",
    "Insulin NPH",
    "Insulin Regular",
    "Insulin largine",
    "Intubated",
    "Jackson-Pratt",
    "KCl",
    "KCl (Bolus)",
    "LDH",
    "Lactate",
    "Lactated Ringers",
    "Lorazepam",
    "Lymphocytes",
    "Lymphocytes (Absolute)",
    "MBP",
    "MCH",
    "MCHC",
    "MCV",
    "Magnesium",
    "Magnesium Sulfate (Bolus)",
    "Magnesium Sulphate",
    "Metoprolol",
    "Midazolam",
    "Milrinone",
    "Monocytes",
    "Morphine Sulfate",
    "Neosynephrine",
    "Neutrophils",
    "Nitroglycerine",
    "Nitroprusside",
    "Norepinephrine",
    "Normal Saline",
    "O2 Saturation",
    "OR/PACU Crystalloid",
    "PCO2",
    "PO intake",
    "PO2",
    "PT",
    "PTT",
    "Packed RBC",
    "Pantoprazole",
    "Phosphate",
    "Piggyback",
    "Piperacillin",
    "Platelet Count",
    "Potassium",
    "Pre-admission Intake",
    "Pre-admission Output",
    "Propofol",
    "RBC",
    "RDW",
    "RR",
    "Residual",
    "SBP",
    "SG Urine",
    "Sodium",
    "Solution",
    "Sterile Water",
    "Stool",
    "TPN",
    "Temperature",
    "Total CO2",
    "Ultrafiltrate",
    "Unknown",
    "Urine",
    "Vacomycin",
    "Vasopressin",
    "WBC",
    "Weight",
    "pH Blood",
    "pH Urine",
}


def _declared_variable_names() -> set[str]:
    tree = ast.parse((SRC / "preprocess_mimic_iii_large.py").read_text())
    variables = {"Age", "Gender"}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            if any("NAME" in ast.unparse(target) for target in node.targets):
                variables.add(node.value.value)
        for target in node.targets:
            if (
                isinstance(target, ast.Name)
                and target.id == "features"
                and isinstance(node.value, ast.Dict)
            ):
                variables.update(
                    key.value
                    for key in node.value.keys
                    if isinstance(key, ast.Constant) and isinstance(key.value, str)
                )
    return variables


def _synthetic_tables() -> dict[str, pd.DataFrame]:
    chart_rows: list[dict[str, object]] = []

    def add_chart(
        itemid: int,
        charttime: str,
        valuenum: float | None,
        value: object | None = None,
    ) -> None:
        chart_rows.append(
            {
                "SUBJECT_ID": "1",
                "HADM_ID": "10",
                "ICUSTAY_ID": "100",
                "ITEMID": itemid,
                "CHARTTIME": charttime,
                "VALUE": str(valuenum) if value is None and valuenum is not None else value,
                "VALUENUM": valuenum,
                "VALUEUOM": None,
                "ERROR": 0,
            }
        )

    add_chart(8368, "2020-01-01 01:00:00", 60)
    add_chart(220051, "2020-01-01 01:01:00", 65)
    add_chart(51, "2020-01-01 01:02:00", 120)
    add_chart(52, "2020-01-01 01:03:00", 80)
    add_chart(184, "2020-01-01 01:04:00", 4)
    add_chart(454, "2020-01-01 01:05:00", 6)
    add_chart(723, "2020-01-01 01:06:00", 5)
    add_chart(223761, "2020-01-01 01:07:00", 98.6)
    add_chart(226531, "2020-01-01 01:08:00", 220.462262)
    add_chart(3420, "2020-01-01 01:09:00", 50)
    add_chart(211, "2020-01-01 06:00:00", 80)
    add_chart(211, "2020-01-01 06:00:00", 100)
    add_chart(211, "2020-01-01 06:01:00", 500)
    add_chart(211, "2020-01-02 06:00:00", 75)
    add_chart(3348, "2020-01-01 01:10:00", None, "Normal <3 Seconds")
    add_chart(3348, "2020-01-01 01:11:00", None, "Abnormal >3 Seconds")

    labs = pd.DataFrame(
        [
            ["10", 50983, "2020-01-01 02:00:00", "140", 140.0, "mEq/L"],
            ["10", 50912, "2020-01-01 02:01:00", "1.2", 1.2, "mg/dL"],
            ["10", 50813, "2020-01-01 02:02:00", "2", 2.0, "mmol/L"],
            ["10", 50885, "2020-01-01 02:03:00", "0.8", 0.8, "mg/dL"],
            ["10", 50818, "2020-01-01 02:04:00", "40", 40.0, "mmHg"],
            ["10", 50812, "2020-01-01 02:05:00", "INTUBATED", np.nan, None],
        ],
        columns=["HADM_ID", "ITEMID", "CHARTTIME", "VALUE", "VALUENUM", "VALUEUOM"],
    )

    output = pd.DataFrame(
        [
            ["100", 40286, "2020-01-01 03:00:00", 100.0, "mL"],
            ["100", 40286, "2020-01-01 03:01:00", 8000.0, "mL"],
            ["100", 40055, "2020-01-01 03:02:00", 500.0, "mL"],
            ["100", 226593, "2020-01-01 03:03:00", 50.0, "mL"],
        ],
        columns=["ICUSTAY_ID", "ITEMID", "CHARTTIME", "VALUE", "VALUEUOM"],
    )
    items = pd.DataFrame(
        [
            [40286, "Ultrafiltrate", "UF", "mL", "Numeric"],
            [40055, "Foley urine", "Urine", "mL", "Numeric"],
            [226593, "Chest tube", "CT", "mL", "Numeric"],
        ],
        columns=["ITEMID", "LABEL", "ABBREVIATION", "UNITNAME", "PARAM_TYPE"],
    )

    input_cv = pd.DataFrame(
        [
            ["100", 30124, "2020-01-01 04:00:00", 10.0, "mg"],
            ["100", 30124, "2020-01-01 04:01:00", 600.0, "mg"],
            ["100", 30018, "2020-01-01 04:02:00", 1.0, "L"],
            ["100", 30047, "2020-01-01 04:03:00", 2000.0, "mcg"],
            ["100", 30045, "2020-01-01 04:04:00", 5.0, "units"],
            ["100", 30001, "2020-01-01 04:05:00", 300.0, "ml"],
            ["100", 30032, "2020-01-01 04:06:00", 500.0, "ml"],
            ["100", 30026, "2020-01-01 04:07:00", 20.0, "mEq"],
            ["100", 30051, "2020-01-01 04:08:00", 2.0, "units"],
        ],
        columns=["ICUSTAY_ID", "ITEMID", "CHARTTIME", "AMOUNT", "AMOUNTUOM"],
    )
    input_mv = pd.DataFrame(
        [
            [
                "100",
                221906,
                "2020-01-01 05:00:00",
                "2020-01-01 07:30:00",
                30.0,
                "mg",
                82.0,
            ],
            [
                "100",
                223262,
                "2020-01-01 08:00:00",
                "2020-01-01 08:30:00",
                4.0,
                "units",
                82.0,
            ],
        ],
        columns=[
            "ICUSTAY_ID",
            "ITEMID",
            "STARTTIME",
            "ENDTIME",
            "AMOUNT",
            "AMOUNTUOM",
            "PATIENTWEIGHT",
        ],
    )

    return {
        "ICUSTAYS.csv": pd.DataFrame(
            [["1", "10", "100", "2020-01-01 00:00:00", "2020-01-03 00:00:00"]],
            columns=["SUBJECT_ID", "HADM_ID", "ICUSTAY_ID", "INTIME", "OUTTIME"],
        ),
        "PATIENTS.csv": pd.DataFrame(
            [["1", "1980-06-01", pd.NaT, "M"]],
            columns=["SUBJECT_ID", "DOB", "DOD", "GENDER"],
        ),
        "CHARTEVENTS.csv": pd.DataFrame(chart_rows),
        "LABEVENTS.csv": labs,
        "OUTPUTEVENTS.csv": output,
        "D_ITEMS.csv": items,
        "INPUTEVENTS_CV.csv": input_cv,
        "INPUTEVENTS_MV.csv": input_mv,
        "ADMISSIONS.csv": pd.DataFrame(
            [["10", pd.NaT, 1]],
            columns=["HADM_ID", "DEATHTIME", "HOSPITAL_EXPIRE_FLAG"],
        ),
    }


@pytest.fixture()
def synthetic_payload(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    tables = _synthetic_tables()

    def fake_read_csv(
        path: str | Path,
        *args: object,
        usecols: list[str] | None = None,
        chunksize: int | None = None,
        dtype: dict[str, str] | None = None,
        **kwargs: object,
    ):
        frame = tables[Path(path).name].copy()
        if usecols is not None:
            frame = frame.loc[:, usecols].copy()
        if dtype is not None:
            for column, column_dtype in dtype.items():
                if column in frame.columns:
                    frame[column] = frame[column].astype(column_dtype)
        if chunksize is not None:
            return iter([frame])
        return frame

    monkeypatch.setattr(preprocess.pd, "read_csv", fake_read_csv)
    output_path = tmp_path / "nested" / "processed" / "mimic.pkl"
    ts, oc, ts_ids = preprocess.run_preprocessing(tmp_path / "raw", output_path)
    with output_path.open("rb") as file:
        artifact = pickle.load(file)
    return ts, oc, ts_ids, artifact, output_path


def _values(ts: pd.DataFrame, variable: str) -> list[float]:
    return ts.loc[ts["variable"] == variable, "value"].tolist()


def test_historical_variable_vocabulary_is_fully_restored() -> None:
    assert len(HISTORICAL_VARIABLES) == 131
    assert _declared_variable_names() == HISTORICAL_VARIABLES
    assert {"BP", "Input", "Output"}.isdisjoint(HISTORICAL_VARIABLES)


def test_full_historical_extraction_families_and_names(synthetic_payload) -> None:
    ts, _, _, _, _ = synthetic_payload
    variables = set(ts["variable"])

    assert {"DBP", "SBP", "MBP"} <= variables
    assert {"GCS_eye", "GCS_motor", "GCS_verbal"} <= variables
    assert {"Sodium", "Creatinine Blood", "Lactate", "Bilirubin (Total)", "PCO2"} <= variables
    assert {"Midazolam", "KCl"} <= variables
    assert {"Normal Saline"} <= variables
    assert {"Norepinephrine", "Vasopressin"} <= variables
    assert {"Insulin Regular", "Insulin Humalog"} <= variables
    assert {"Urine", "Ultrafiltrate", "Chest Tube"} <= variables
    assert {"Packed RBC", "TPN"} <= variables
    assert {"BP", "Input", "Output"}.isdisjoint(variables)

    assert _values(ts, "GCS_eye") == [4.0]
    assert _values(ts, "GCS_motor") == [6.0]
    assert _values(ts, "GCS_verbal") == [5.0]
    assert _values(ts, "Intubated") == [1.0]
    assert _values(ts, "CRR") == [0.0, 1.0]


def test_historical_units_bounds_medians_and_itemids(synthetic_payload) -> None:
    ts, _, _, _, _ = synthetic_payload

    assert _values(ts, "Temperature") == pytest.approx([37.0])
    assert any(
        value == pytest.approx(100.0, rel=1e-5)
        for value in _values(ts, "Weight")
    )
    assert _values(ts, "FiO2") == pytest.approx([0.5])
    assert _values(ts, "Normal Saline") == pytest.approx([1000.0])
    assert 2.0 in _values(ts, "Norepinephrine")
    assert {12.0, 6.0} <= set(_values(ts, "Norepinephrine"))

    assert _values(ts, "Midazolam") == [10.0, 10.0]
    assert _values(ts, "Ultrafiltrate") == [100.0, 100.0]
    assert 500.0 not in _values(ts, "HR")

    dbp = ts.loc[ts["variable"] == "DBP", ["minute", "value"]]
    assert dict(dbp.itertuples(index=False, name=None)) == {60: 60.0, 61: 65.0}


def test_historical_cohort_demographics_mortality_and_artifact(synthetic_payload) -> None:
    ts, oc, ts_ids, artifact, output_path = synthetic_payload

    assert output_path.exists()
    assert isinstance(artifact, list)
    assert len(artifact) == 3
    assert artifact[2] == ["100"]
    assert ts_ids == ["100"]
    assert set(ts["ts_id"]) == set(oc["ts_id"]) == set(ts_ids)
    assert list(ts.columns) == ["ts_id", "minute", "variable", "value"]
    assert list(oc.columns) == [
        "ts_id",
        "length_of_stay",
        "in_hospital_mortality",
        "subset",
    ]

    static = ts.loc[ts["variable"].isin(["Age", "Gender"])]
    assert set(static["minute"]) == {0}
    assert dict(zip(static["variable"], static["value"], strict=True)) == {
        "Age": 40.0,
        "Gender": 0.0,
    }
    assert oc.loc[0, "in_hospital_mortality"] == 1
    assert ts["minute"].max() == 30 * 60

    hr_at_six_hours = ts.loc[
        (ts["variable"] == "HR") & (ts["minute"] == 6 * 60), "value"
    ]
    assert hr_at_six_hours.tolist() == [90.0]


def _icu_rows() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "SUBJECT_ID": ["1"],
            "HADM_ID": ["10"],
            "ICUSTAY_ID": ["100"],
            "INTIME": pd.to_datetime(["2020-01-01 00:00:00"]),
            "OUTTIME": pd.to_datetime(["2020-01-02 12:00:00"]),
            "DOB": pd.to_datetime(["1980-01-01"]),
            "DOD": [pd.NaT],
            "GENDER": ["F"],
            "AGE": [40],
        }
    )


def test_admission_level_event_is_assigned_to_the_unique_icu_stay() -> None:
    events = pd.DataFrame(
        {
            "HADM_ID": ["10"],
            "ICUSTAY_ID": [pd.NA],
            "CHARTTIME": pd.to_datetime(["2020-01-01 05:00:00"]),
            "VALUENUM": [140.0],
            "TABLE": ["lab"],
            "NAME": ["Sodium"],
        }
    )

    assigned = preprocess.assign_missing_icustays(events, _icu_rows())

    assert assigned.loc[0, "ICUSTAY_ID"] == "100"
    assert assigned.loc[0, "HADM_ID"] == "10"


def test_ambiguous_admission_level_event_fails_explicitly() -> None:
    icu = pd.concat(
        [
            _icu_rows(),
            _icu_rows().assign(
                ICUSTAY_ID="101",
                INTIME=pd.Timestamp("2020-01-01 04:00:00"),
                OUTTIME=pd.Timestamp("2020-01-02 16:00:00"),
            ),
        ],
        ignore_index=True,
    )
    events = pd.DataFrame(
        {
            "HADM_ID": ["10"],
            "ICUSTAY_ID": [pd.NA],
            "CHARTTIME": pd.to_datetime(["2020-01-01 05:00:00"]),
            "VALUENUM": [1.0],
            "TABLE": ["lab"],
            "NAME": ["Creatinine Blood"],
        }
    )

    with pytest.raises(ValueError, match="matching multiple ICU stays"):
        preprocess.assign_missing_icustays(events, icu)


def test_conflicting_icustay_to_admission_mapping_fails() -> None:
    mapping = pd.DataFrame(
        {
            "ICUSTAY_ID": ["100", "100.0"],
            "HADM_ID": ["10", "11"],
            "SUBJECT_ID": ["1", "1"],
        }
    )

    with pytest.raises(ValueError, match="conflicting duplicate ICUSTAY_ID"):
        preprocess.validate_icustay_hadm_mapping(mapping)


def test_source_hadm_repair_requires_subject_consistency() -> None:
    source = pd.DataFrame(
        {
            "SUBJECT_ID": ["1"],
            "HADM_ID": ["999"],
            "ICUSTAY_ID": ["100"],
        }
    )

    repaired = preprocess.link_fragment_hadm_ids(source, _icu_rows(), "CHARTEVENTS")
    assert repaired.loc[0, "HADM_ID"] == "10"

    conflicting_subject = source.assign(SUBJECT_ID="2")
    with pytest.raises(ValueError, match="SUBJECT_ID conflicts"):
        preprocess.link_fragment_hadm_ids(
            conflicting_subject,
            _icu_rows(),
            "CHARTEVENTS",
        )


def test_unassignable_admission_event_is_excluded_with_diagnostic(capsys) -> None:
    events = pd.DataFrame(
        {
            "HADM_ID": ["10", "10"],
            "ICUSTAY_ID": ["100", pd.NA],
            "CHARTTIME": pd.to_datetime(
                ["2020-01-01 05:00:00", "2019-12-20 05:00:00"]
            ),
            "VALUENUM": [1.0, 2.0],
            "TABLE": ["chart", "lab"],
            "NAME": ["HR", "Sodium"],
        }
    )

    assigned = preprocess.assign_missing_icustays(events, _icu_rows())

    assert assigned["ICUSTAY_ID"].tolist() == ["100"]
    assert "excluded 1 row" in capsys.readouterr().out


def test_current_cli_paths_and_router_compatibility_flags_are_retained(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    args = preprocess.parse_args(
        [
            "--dataset-config-csv",
            "config.csv",
            "--raw-data-path",
            "raw",
            "--output-path",
            "out.pkl",
            "--chunksize",
            "500000",
            "--tmp-dir",
            "scratch",
        ]
    )
    assert args.dataset_config_csv == "config.csv"
    assert args.raw_data_path == "raw"
    assert args.output_path == "out.pkl"
    assert args.chunksize == 500000
    assert args.tmp_dir == "scratch"
    assert not hasattr(args, "keep_intermediates")
    assert not hasattr(args, "max_debug_chunks")

    called: dict[str, object] = {}

    def fake_run(raw_data_path: str | Path, output_path: str | Path):
        called["raw"] = raw_data_path
        called["output"] = output_path
        return pd.DataFrame(), pd.DataFrame(), []

    monkeypatch.setattr(preprocess, "run_preprocessing", fake_run)
    preprocess.main(
        [
            "--raw-data-path",
            str(tmp_path / "raw"),
            "--output-path",
            str(tmp_path / "out.pkl"),
        ]
    )
    assert called == {
        "raw": str(tmp_path / "raw"),
        "output": str(tmp_path / "out.pkl"),
    }


def test_validate_only_does_not_load_mimic_data(
    monkeypatch: pytest.MonkeyPatch,
    capsys,
) -> None:
    def forbidden_read_csv(*args: object, **kwargs: object):
        raise AssertionError("validation-only mode must not load MIMIC CSV files")

    monkeypatch.setattr(preprocess.pd, "read_csv", forbidden_read_csv)
    config_path = WORKSPACE_ROOT / "configs" / "mimic-global-variables.csv"

    with pytest.raises(SystemExit) as exit_info:
        preprocess.main(
            [
                "--dataset-config-csv",
                str(config_path),
                "--validate-config-only",
            ]
        )

    assert exit_info.value.code == 0
    assert "VALIDATE-CONFIG-ONLY PASS" in capsys.readouterr().out

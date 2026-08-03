
"""
tagging_latent_variables_mimiciii.py

Rule-based latent variable tagging for MIMIC-III ICU stays.

What this script does
---------------------
1. Loads either:
   - a pre-aggregated patient/ICU-stay summary CSV, or
   - raw concept-level CSVs/tables exported from MIMIC-III SQL queries.
   - a PhysioNet-compatible MIMIC pickle: [ts, oc, ts_ids]
2. Computes clinically motivated summary features.
3. Applies pickle-safe rule-based decision trees for latent physiologic states.
4. Saves:
   - latent_tags.csv
   - latent_tags_with_features.csv
   - latent_decision_trees.pkl
   - validation_summary.json
   - prevalence.csv
   - mortality_by_tag.csv
   - cooccurrence_phi.csv

Important note
--------------
This script intentionally stays rule-based and interpretable.
It does NOT train a model for labeling.

Recommended workflow
--------------------
Best practical use is:
A. extract concept-level tables from MIMIC-III using SQL (labs, vitals, urine, vent, vasopressors, etc.)
B. export those as CSVs
C. run this script to aggregate + tag

The script also supports a simpler path:
- pass a prebuilt summary CSV with columns such as MAP_min, Lactate_max, GCS_min, etc.

Authoring note
--------------
Some raw MIMIC-III extraction details depend on your local SQL pipeline / ITEMID mappings.
Therefore this file includes:
- fully implemented decision trees
- a complete summary/tagging/validation pipeline
- hooks for raw concept CSV inputs
"""

from __future__ import annotations

import argparse
import json
import math
import os
import pickle
import sys
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple

if "--validate-config-only" in sys.argv:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from dataset_config import maybe_run_validate_config_only

    maybe_run_validate_config_only(
        "src/tagging_latent_variables_mimiciii.py",
        fixed_dataset="mimic",
    )

import numpy as np
import pandas as pd

from dataset_config import (
    get_config_list,
    load_dataset_config,
)
from preprocess_mimic_iii_large_contract import canonicalize_stay_id_series


# ============================================================
# Configuration
# ============================================================

DEFAULT_PKL_PATH = "../data/processed/mimic_iii_ts_oc_ids.pkl"
DEFAULT_OUTPUT_DIR = "mimiciii_latent_tags_output"

LATENT_ORDER = [
    "LAT_CHRONIC_BURDEN",
    "LAT_INFLAMMATION_SEPSIS",
    "LAT_GLOBAL_SEVERITY",
    "LAT_SHOCK",
    "LAT_RESPIRATORY_FAILURE",
    "LAT_RENAL_DYSFUNCTION",
    "LAT_HEPATIC_COAG_DYSFUNCTION",
    "LAT_NEUROLOGIC_DYSFUNCTION",
    "LAT_METABOLIC_DERANGEMENT",
    "LAT_CARDIAC_STRAIN",
]

DEFAULT_THRESHOLDS = {
    # Chronic burden
    "chronic_age": 75,
    "chronic_elixhauser": 5,
    "chronic_comorbidity_count": 2,

    # Inflammation / suspected infection / sepsis burden
    "sepsis_temp_hi": 38.3,
    "sepsis_temp_lo": 36.0,
    "sepsis_wbc_hi": 12.0,
    "sepsis_wbc_lo": 4.0,
    "sepsis_lactate": 2.0,

    # SIRS helper thresholds retained for existing summary feature construction
    "sirs_temp_hi": 38.3,
    "sirs_temp_lo": 36.0,
    "sirs_hr": 90,
    "sirs_rr": 20,
    "sirs_paco2": 32,
    "sirs_wbc_hi": 12.0,
    "sirs_wbc_lo": 4.0,
    "sirs_min_count": 2,

    # Global severity domains
    "global_map": 70,
    "global_sbp": 100,
    "global_spo2": 92,
    "global_pf": 300.0,
    "global_gcs": 15,
    "global_rass_low": -3,
    "global_rass_high": 2,
    "global_creatinine": 2.0,
    "global_urine_24h_ml": 500.0,
    "global_lactate": 2.0,
    "global_ph": 7.30,
    "global_hco3": 18.0,
    "global_bilirubin": 2.0,
    "global_platelets": 100.0,
    "global_inr": 1.5,
    "global_min_domains": 3,

    # Shock
    "shock_map": 65,
    "shock_sbp": 90,
    "shock_sustained_map": 70,
    "shock_lactate": 2.0,
    "shock_urine_24h_ml": 500.0,
    "shock_urine_6h_mlkg": 0.5,
    "shock_ph": 7.30,
    "shock_base_excess": -5.0,

    # Respiratory failure
    "resp_spo2": 92.0,
    "resp_pf": 300.0,
    "resp_fio2": 0.5,
    "resp_rr_hi": 30.0,
    "resp_rr_lo": 8.0,
    "resp_paco2": 50.0,
    "resp_ph": 7.30,

    # Renal dysfunction
    "renal_creatinine_delta": 0.3,
    "renal_creatinine_abs": 2.0,
    "renal_bun": 40.0,
    "renal_urine_24h_ml": 500.0,
    "renal_urine_6h_mlkg": 0.5,
    "renal_potassium_hi": 5.5,
    "renal_hco3": 18.0,

    # Hepatic / coagulation dysfunction
    "hepcoag_bilirubin": 2.0,
    "hepcoag_ast": 120.0,
    "hepcoag_alt": 120.0,
    "hepcoag_platelets": 100.0,
    "hepcoag_inr": 1.5,
    "hepcoag_albumin": 2.5,

    # Neurologic dysfunction
    "neuro_gcs_moderate": 13,
    "neuro_gcs_severe": 8,
    "neuro_rass_low": -3,
    "neuro_rass_high": 2,

    # Metabolic derangement
    "metab_ph_low": 7.30,
    "metab_ph_high": 7.55,
    "metab_hco3_low": 18.0,
    "metab_hco3_high": 35.0,
    "metab_base_excess": -5.0,
    "metab_lactate": 2.0,
    "metab_potassium_lo": 3.0,
    "metab_potassium_hi": 5.5,
    "metab_sodium_lo": 130.0,
    "metab_sodium_hi": 150.0,
    "metab_glucose_lo": 70.0,
    "metab_glucose_hi": 250.0,

    # Cardiac strain / injury
    "cardiac_troponin_t_fallback": 0.1,
    "cardiac_troponin_i_fallback": 0.4,
    "cardiac_hr_hi": 150.0,
    "cardiac_hr_lo": 40.0,
    "cardiac_stress_hr_hi": 130.0,
    "cardiac_context_units": {"CSRU", "CCU"},
}

CHRONIC_ICD_KEYWORDS = [
    "CHF", "HEART FAILURE", "COPD", "CHRONIC KIDNEY", "CKD", "CIRRHOSIS",
    "MALIGNANC", "CANCER", "DIABETES", "DEMENTIA", "CAD", "CORONARY",
    "ATRIAL FIB", "HYPERTENSION", "LIVER DISEASE", "ESRD",
]

ACUTE_ICD_KEYWORDS = [
    "SEPSIS", "SEPTIC", "PNEUMONIA", "RESPIRATORY FAILURE", "ARDS",
    "MYOCARDIAL INFARCTION", "STEMI", "NSTEMI", "STROKE", "INTRACRANIAL",
    "TRAUMA", "HEMORRHAGE", "SHOCK", "PANCREATITIS", "GI BLEED",
]


PICKLE_TS_SUMMARY_SPECS = {
    "Age": {"aliases": ["Age"], "stats": {"first": "Age"}},
    "Albumin": {"aliases": ["Albumin"], "stats": {"first": "Albumin_first", "min": "Albumin_min"}},
    "Lactate": {"aliases": ["Lactate"], "stats": {"max": "Lactate_max"}},
    "pH": {"aliases": ["pH", "pH Blood"], "stats": {"min": "pH_min", "max": "pH_max"}},
    "Platelets": {"aliases": ["Platelets", "Platelet Count"], "stats": {"min": "Platelets_min"}},
    "Creatinine": {
        "aliases": ["Creatinine", "Creatinine Blood"],
        "stats": {"first": "Creatinine_first", "max": "Creatinine_max"},
    },
    "BUN": {"aliases": ["BUN", "Blood Urea Nitrogen"], "stats": {"max": "BUN_max"}},
    "Bilirubin": {"aliases": ["Bilirubin", "Bilirubin (Total)"], "stats": {"max": "Bilirubin_max"}},
    "Temperature": {"aliases": ["Temperature"], "stats": {"min": "Temperature_min", "max": "Temperature_max"}},
    "HR": {"aliases": ["HR", "Heart Rate"], "stats": {"min": "HR_min", "max": "HR_max"}},
    "RR": {"aliases": ["RR", "Respiratory Rate"], "stats": {"min": "RR_min", "max": "RR_max"}},
    "RASS": {"aliases": ["RASS"], "stats": {"min": "RASS_min", "max": "RASS_max"}},
    "PaCO2": {"aliases": ["PaCO2", "PCO2"], "stats": {"min": "PaCO2_min", "max": "PaCO2_max"}},
    "WBC": {"aliases": ["WBC", "White Blood Cell Count"], "stats": {"min": "WBC_min", "max": "WBC_max"}},
    "MAP": {"aliases": ["MAP", "MBP"], "stats": {"min": "MAP_min"}},
    "SBP": {"aliases": ["SBP"], "stats": {"min": "SBP_min"}},
    "PaO2": {"aliases": ["PaO2", "PO2"], "stats": {"min": "PaO2_min"}},
    "FiO2": {"aliases": ["FiO2"], "stats": {"max": "FiO2_max"}},
    "SpO2": {"aliases": ["SpO2", "O2 Saturation"], "stats": {"min": "SpO2_min"}},
    "INR": {"aliases": ["INR"], "stats": {"max": "INR_max"}},
    "PT": {"aliases": ["PT", "Prothrombin Time"], "stats": {"max": "PT_max"}},
    "PTT": {"aliases": ["PTT", "Partial Thromboplastin Time"], "stats": {"max": "PTT_max"}},
    "TroponinT": {"aliases": ["TroponinT", "Troponin T"], "stats": {"max": "TroponinT_max"}},
    "TroponinI": {"aliases": ["TroponinI", "Troponin I"], "stats": {"max": "TroponinI_max"}},
    "CKMB": {"aliases": ["CKMB", "CK-MB", "CK MB"], "stats": {"max": "CKMB_max"}},
    "Bicarbonate": {"aliases": ["Bicarbonate"], "stats": {"min": "Bicarbonate_min", "max": "Bicarbonate_max"}},
    "BaseExcess": {"aliases": ["BaseExcess", "Base Excess"], "stats": {"min": "BaseExcess_min"}},
    "AnionGap": {"aliases": ["AnionGap", "Anion Gap"], "stats": {"max": "AnionGap_max"}},
    "Glucose": {
        "aliases": ["Glucose", "Glucose (Blood)", "Glucose (Whole Blood)", "Glucose (Serum)"],
        "stats": {"min": "Glucose_min", "max": "Glucose_max"},
    },
    "Sodium": {"aliases": ["Sodium"], "stats": {"min": "Sodium_min", "max": "Sodium_max"}},
    "Potassium": {"aliases": ["Potassium"], "stats": {"min": "Potassium_min", "max": "Potassium_max"}},
    "AST": {"aliases": ["AST"], "stats": {"max": "AST_max"}},
    "ALT": {"aliases": ["ALT"], "stats": {"max": "ALT_max"}},
}

PICKLE_GCS_COMPONENTS = ["GCS_eye", "GCS_motor", "GCS_verbal"]
PICKLE_URINE_VARIABLE = "Urine"
PICKLE_WEIGHT_VARIABLE = "Weight"
PICKLE_TS_BINARY_HELPERS = {
    "MechanicalVentilation_any": ["MechanicalVentilation", "Intubated"],
    "NonInvasiveVentilation_any": ["NonInvasiveVentilation", "NIV", "BiPAP", "CPAP"],
    "Vasopressors_any": ["Vasopressin", "Norepinephrine", "Epinephrine", "Dopamine", "Neosynephrine", "Phenylephrine", "Dobutamine"],
    "DialysisOrCRRT_any": ["Dialysis", "CRRT", "RenalReplacementTherapy"],
    "SedationOrIntubation_any": ["Sedation", "SedativeInfusion", "Intubated", "MechanicalVentilation"],
    "Arrhythmia_any": ["Arrhythmia", "AtrialFibrillation", "VentricularTachycardia"],
}
PICKLE_OC_OPTIONAL_FIELDS = {
    "InHospitalMortality": ["InHospitalMortality", "in_hospital_mortality"],
    "AdmissionType": ["AdmissionType", "admission_type", "ADMISSION_TYPE"],
    "FirstCareUnit": ["FirstCareUnit", "first_careunit", "FIRST_CAREUNIT"],
    "ComorbidityCount": ["ComorbidityCount", "comorbidity_count", "COMORBIDITY_COUNT"],
    "ElixhauserScore": ["ElixhauserScore", "elixhauser_score", "ELIXHAUSER_SCORE"],
    "ChronicICD_any": ["ChronicICD_any"],
    "ChronicOrganDisease_any": ["ChronicOrganDisease_any", "chronic_organ_disease"],
    "MalignancyImmunosuppression_any": ["MalignancyImmunosuppression_any", "malignancy_immunosuppression"],
    "AcuteICD_any": ["AcuteICD_any"],
    "SuspectedInfection_any": ["SuspectedInfection_any"],
    "CultureOrdered_any": ["CultureOrdered_any", "culture_ordered"],
    "CulturePositive_any": ["CulturePositive_any", "culture_positive"],
    "AntibioticStarted_any": ["AntibioticStarted_any", "antibiotic_started"],
    "MAP_sustained_lt70_any": ["MAP_sustained_lt70_any", "map_sustained_lt70"],
    "DialysisOrCRRT_any": ["DialysisOrCRRT_any", "dialysis_or_crrt"],
    "NonInvasiveVentilation_any": ["NonInvasiveVentilation_any", "noninvasive_ventilation"],
    "TroponinPositive_any": ["TroponinPositive_any"],
    "TroponinAboveULN_any": ["TroponinAboveULN_any", "troponin_above_uln"],
    "CKMBAboveULN_any": ["CKMBAboveULN_any", "ckmb_above_uln"],
    "Arrhythmia_any": ["Arrhythmia_any", "arrhythmia_documented"],
    "CardiacSurgeryContext_any": ["CardiacSurgeryContext_any", "cardiac_surgery_context"],
    "GCSComponentAbnormal_any": ["GCSComponentAbnormal_any", "gcs_component_abnormal"],
    "PupilOrFocalNeuroAbnormal_any": ["PupilOrFocalNeuroAbnormal_any", "pupil_or_focal_neuro_abnormal"],
    "SedationOrIntubation_any": ["SedationOrIntubation_any", "sedation_or_intubation"],
    "PTProlonged_any": ["PTProlonged_any", "pt_prolonged"],
    "PTTProlonged_any": ["PTTProlonged_any", "ptt_prolonged"],
}
PICKLE_EXPECTED_SUMMARY_COLUMNS = [
    "Age",
    "AgeIsDeidentifiedOld",
    "AdmissionType",
    "FirstCareUnit",
    "ComorbidityCount",
    "ElixhauserScore",
    "ChronicICD_any",
    "ChronicOrganDisease_any",
    "MalignancyImmunosuppression_any",
    "AcuteICD_any",
    "MechanicalVentilation_any",
    "NonInvasiveVentilation_any",
    "Vasopressors_any",
    "DialysisOrCRRT_any",
    "Lactate_max",
    "pH_min",
    "pH_max",
    "BaseExcess_min",
    "GCS_min",
    "GCSComponentAbnormal_any",
    "RASS_min",
    "RASS_max",
    "PupilOrFocalNeuroAbnormal_any",
    "SedationOrIntubation_any",
    "Platelets_min",
    "Creatinine_first",
    "Creatinine_max",
    "Creatinine_delta",
    "BUN_max",
    "Bilirubin_max",
    "Temperature_min",
    "Temperature_max",
    "HR_min",
    "HR_max",
    "RR_min",
    "RR_max",
    "PaCO2_min",
    "PaCO2_max",
    "WBC_min",
    "WBC_max",
    "SIRS_count_max",
    "MAP_min",
    "MAP_sustained_lt70_any",
    "SBP_min",
    "UrineOutput_sum_24h",
    "UrineOutput_mlkg_6h_min",
    "PaO2_min",
    "FiO2_max",
    "PF_ratio_min",
    "SF_ratio_min",
    "SpO2_min",
    "INR_max",
    "PT_max",
    "PTT_max",
    "PTProlonged_any",
    "PTTProlonged_any",
    "TroponinPositive_any",
    "TroponinAboveULN_any",
    "TroponinT_max",
    "TroponinI_max",
    "CKMB_max",
    "CKMBAboveULN_any",
    "Arrhythmia_any",
    "CardiacSurgeryContext_any",
    "Bicarbonate_min",
    "Bicarbonate_max",
    "AnionGap_max",
    "Glucose_min",
    "Glucose_max",
    "Sodium_min",
    "Sodium_max",
    "Potassium_min",
    "Potassium_max",
    "AST_max",
    "ALT_max",
    "Albumin_min",
    "Albumin_first",
    "SuspectedInfection_any",
    "CultureOrdered_any",
    "CulturePositive_any",
    "AntibioticStarted_any",
    "InHospitalMortality",
]
PROGRESS_EVERY = 500


# ============================================================
# Utilities
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def print_progress(label: str, current: int, total: int) -> None:
    if total <= 0:
        return
    if current == total or current % PROGRESS_EVERY == 0:
        print(f"      {label}: {current:,} / {total:,}")


def safe_float(x) -> float:
    if x is None:
        return np.nan
    try:
        return float(x)
    except (TypeError, ValueError):
        return np.nan


def is_notna(x) -> bool:
    return pd.notna(x)


def safe_div(a, b):
    if pd.isna(a) or pd.isna(b) or b == 0:
        return np.nan
    return a / b


def normalize_fio2_value(x):
    """
    Converts FiO2 to fraction when values are given as percentages.
    Examples:
        0.40 -> 0.40
        40 -> 0.40
        100 -> 1.0
    """
    if pd.isna(x):
        return np.nan
    x = float(x)
    if x <= 0:
        return np.nan
    if x > 1.5:
        return x / 100.0
    return x


def binary_phi(a: pd.Series, b: pd.Series) -> float:
    """
    Phi coefficient for two binary vectors.
    Returns np.nan when undefined.
    """
    a = a.fillna(0).astype(int)
    b = b.fillna(0).astype(int)

    n11 = int(((a == 1) & (b == 1)).sum())
    n10 = int(((a == 1) & (b == 0)).sum())
    n01 = int(((a == 0) & (b == 1)).sum())
    n00 = int(((a == 0) & (b == 0)).sum())

    denom = math.sqrt((n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00))
    if denom == 0:
        return np.nan
    return (n11 * n00 - n10 * n01) / denom


def first_non_null(series: pd.Series):
    s = series.dropna()
    return s.iloc[0] if len(s) else np.nan


def last_non_null(series: pd.Series):
    s = series.dropna()
    return s.iloc[-1] if len(s) else np.nan


def standard_stats(series: pd.Series) -> Dict[str, float]:
    s = series.dropna()
    if len(s) == 0:
        return {
            "min": np.nan,
            "max": np.nan,
            "mean": np.nan,
            "first": np.nan,
            "last": np.nan,
        }
    return {
        "min": s.min(),
        "max": s.max(),
        "mean": s.mean(),
        "first": s.iloc[0],
        "last": s.iloc[-1],
    }


def require_columns(df: pd.DataFrame, required_columns: Iterable[str], df_name: str) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"{df_name} is missing required columns: {missing}")


# ============================================================
# Decision tree functions (pickle-safe)
# ============================================================


def _first_available(row: pd.Series, *names):
    """Return the first non-missing value across several possible column names."""
    for name in names:
        val = row.get(name)
        if is_notna(val):
            return val
    return np.nan


def _flag_any(row: pd.Series, *names) -> bool:
    """Return True if any named binary/categorical helper column is positive/truthy."""
    for name in names:
        val = row.get(name)
        if pd.isna(val):
            continue
        if isinstance(val, str):
            if val.strip().upper() in {"1", "TRUE", "YES", "Y", "POSITIVE", "PRESENT"}:
                return True
            continue
        try:
            if float(val) > 0:
                return True
        except (TypeError, ValueError):
            if bool(val):
                return True
    return False


def _admission_type_upper(row: pd.Series) -> str:
    return str(row.get("AdmissionType", row.get("ADMISSION_TYPE", ""))).strip().upper()


def _first_careunit_upper(row: pd.Series) -> str:
    return str(row.get("FirstCareUnit", row.get("FIRST_CAREUNIT", ""))).strip().upper()


def _hypotension_for_cardiac(row: pd.Series, thr: dict) -> bool:
    map_min = _first_available(row, "MAP_min")
    sbp_min = _first_available(row, "SBP_min")
    return (
        (is_notna(map_min) and map_min < thr["global_map"]) or
        (is_notna(sbp_min) and sbp_min <= thr["global_sbp"])
    )


def tag_chronic_burden(row: pd.Series, thr: dict = None) -> int:
    """LAT_CHRONIC_BURDEN: score >= 2 across baseline vulnerability domains."""
    thr = thr or DEFAULT_THRESHOLDS
    age = _first_available(row, "Age", "AGE")
    comorbidity_count = _first_available(row, "ComorbidityCount", "COMORBIDITY_COUNT", "comorbidity_count")
    elixhauser_score = _first_available(row, "ElixhauserScore", "ELIXHAUSER_SCORE", "elixhauser_score")
    admission_type = _admission_type_upper(row)

    age_burden = (
        (is_notna(age) and age >= thr["chronic_age"]) or
        _flag_any(row, "AgeIsDeidentifiedOld", "AGE_IS_DEIDENTIFIED_OLD")
    )
    comorbidity_burden = (
        (is_notna(comorbidity_count) and comorbidity_count >= thr["chronic_comorbidity_count"]) or
        (is_notna(elixhauser_score) and elixhauser_score >= thr["chronic_elixhauser"])
    )
    chronic_organ_disease = _flag_any(
        row,
        "ChronicOrganDisease_any",
        "ChronicICD_any",
        "ChronicHeartDisease_any",
        "ChronicLungDisease_any",
        "ChronicKidneyDisease_any",
        "ChronicLiverDisease_any",
        "ChronicNeurologicDisease_any",
    )
    malignancy_or_immunosuppression = _flag_any(
        row,
        "MalignancyImmunosuppression_any",
        "Malignancy_any",
        "Immunosuppression_any",
        "Transplant_any",
    )
    high_risk_admission = admission_type in {"EMERGENCY", "URGENT"}

    score = sum(map(int, [
        age_burden,
        comorbidity_burden,
        chronic_organ_disease,
        malignancy_or_immunosuppression,
        high_risk_admission,
    ]))
    return int(score >= 2)


def tag_inflammation_sepsis(row: pd.Series, thr: dict = None) -> int:
    """LAT_INFLAMMATION_SEPSIS: score >= 2 with infection/inflammation evidence."""
    thr = thr or DEFAULT_THRESHOLDS
    temp_max = _first_available(row, "Temperature_max", "TEMP_MAX_C", "Temp_max")
    temp_min = _first_available(row, "Temperature_min", "TEMP_MIN_C", "Temp_min")
    wbc_max = _first_available(row, "WBC_max")
    wbc_min = _first_available(row, "WBC_min")
    lactate_max = _first_available(row, "Lactate_max")

    temperature_abnormal = (
        (is_notna(temp_max) and temp_max >= thr["sepsis_temp_hi"]) or
        (is_notna(temp_min) and temp_min < thr["sepsis_temp_lo"])
    )
    wbc_abnormal = (
        (is_notna(wbc_max) and wbc_max > thr["sepsis_wbc_hi"]) or
        (is_notna(wbc_min) and wbc_min < thr["sepsis_wbc_lo"])
    )
    lactate_elevated = is_notna(lactate_max) and lactate_max > thr["sepsis_lactate"]
    culture_evidence = _flag_any(row, "CultureOrdered_any", "CulturePositive_any", "SuspectedInfection_any")
    antibiotic_evidence = _flag_any(row, "AntibioticStarted_any", "Antibiotics_any", "SuspectedInfection_any")

    score = sum(map(int, [
        temperature_abnormal,
        wbc_abnormal,
        lactate_elevated,
        culture_evidence,
        antibiotic_evidence,
    ]))
    return int(score >= 2 and (culture_evidence or antibiotic_evidence or temperature_abnormal or wbc_abnormal))


def tag_global_severity(row: pd.Series, thr: dict = None) -> int:
    """LAT_GLOBAL_SEVERITY: score >= 3 abnormal organ/severity domains."""
    thr = thr or DEFAULT_THRESHOLDS
    map_min = _first_available(row, "MAP_min")
    sbp_min = _first_available(row, "SBP_min")
    spo2_min = _first_available(row, "SpO2_min", "SPO2_MIN")
    pf_ratio_min = _first_available(row, "PF_ratio_min", "PAO2_FIO2_MIN")
    gcs_min = _first_available(row, "GCS_min")
    rass_min = _first_available(row, "RASS_min")
    rass_max = _first_available(row, "RASS_max")
    creatinine_max = _first_available(row, "Creatinine_max")
    urine_24h = _first_available(row, "UrineOutput_sum_24h", "UrineOutput_24h", "URINE_OUTPUT_24H")
    lactate_max = _first_available(row, "Lactate_max")
    ph_min = _first_available(row, "pH_min", "PH_min")
    bicarbonate_min = _first_available(row, "Bicarbonate_min")
    temp_max = _first_available(row, "Temperature_max", "TEMP_MAX_C")
    temp_min = _first_available(row, "Temperature_min", "TEMP_MIN_C")
    wbc_max = _first_available(row, "WBC_max")
    wbc_min = _first_available(row, "WBC_min")
    bilirubin_max = _first_available(row, "Bilirubin_max")
    platelets_min = _first_available(row, "Platelets_min")
    inr_max = _first_available(row, "INR_max")

    circulatory = (
        (is_notna(map_min) and map_min < thr["global_map"]) or
        (is_notna(sbp_min) and sbp_min <= thr["global_sbp"]) or
        _flag_any(row, "Vasopressors_any")
    )
    respiratory = (
        (is_notna(spo2_min) and spo2_min < thr["global_spo2"]) or
        (is_notna(pf_ratio_min) and pf_ratio_min <= thr["global_pf"]) or
        _flag_any(row, "MechanicalVentilation_any")
    )
    neurologic = (
        (is_notna(gcs_min) and gcs_min < thr["global_gcs"]) or
        (is_notna(rass_min) and rass_min <= thr["global_rass_low"]) or
        (is_notna(rass_max) and rass_max >= thr["global_rass_high"])
    )
    renal = (
        (is_notna(creatinine_max) and creatinine_max >= thr["global_creatinine"]) or
        (is_notna(urine_24h) and urine_24h < thr["global_urine_24h_ml"])
    )
    metabolic = (
        (is_notna(lactate_max) and lactate_max > thr["global_lactate"]) or
        (is_notna(ph_min) and ph_min < thr["global_ph"]) or
        (is_notna(bicarbonate_min) and bicarbonate_min < thr["global_hco3"])
    )
    inflammatory = (
        (is_notna(temp_max) and temp_max >= thr["sepsis_temp_hi"]) or
        (is_notna(temp_min) and temp_min < thr["sepsis_temp_lo"]) or
        (is_notna(wbc_max) and wbc_max > thr["sepsis_wbc_hi"]) or
        (is_notna(wbc_min) and wbc_min < thr["sepsis_wbc_lo"])
    )
    hepatic_coag = (
        (is_notna(bilirubin_max) and bilirubin_max >= thr["global_bilirubin"]) or
        (is_notna(platelets_min) and platelets_min < thr["global_platelets"]) or
        (is_notna(inr_max) and inr_max >= thr["global_inr"])
    )

    score = sum(map(int, [circulatory, respiratory, neurologic, renal, metabolic, inflammatory, hepatic_coag]))
    return int(score >= thr["global_min_domains"])


def tag_shock(row: pd.Series, thr: dict = None) -> int:
    """LAT_SHOCK: score >= 2, or vasopressor plus hypoperfusion/acidosis/hypotension."""
    thr = thr or DEFAULT_THRESHOLDS
    map_min = _first_available(row, "MAP_min")
    sbp_min = _first_available(row, "SBP_min")
    lactate_max = _first_available(row, "Lactate_max")
    urine_24h = _first_available(row, "UrineOutput_sum_24h", "UrineOutput_24h", "URINE_OUTPUT_24H")
    urine_6h = _first_available(row, "UrineOutput_mlkg_6h_min", "UrineOutput_6h_mlkg", "URINE_OUTPUT_6H_ML_PER_KG_HR")
    ph_min = _first_available(row, "pH_min", "PH_min")
    base_excess_min = _first_available(row, "BaseExcess_min", "BASE_EXCESS_MIN")

    hypotension = (
        (is_notna(map_min) and map_min < thr["shock_map"]) or
        (is_notna(sbp_min) and sbp_min <= thr["shock_sbp"]) or
        _flag_any(row, "MAP_sustained_lt70_any")
    )
    vasopressor = _flag_any(row, "Vasopressors_any")
    tissue_hypoperfusion = is_notna(lactate_max) and lactate_max > thr["shock_lactate"]
    oliguria = (
        (is_notna(urine_6h) and urine_6h < thr["shock_urine_6h_mlkg"]) or
        (is_notna(urine_24h) and urine_24h < thr["shock_urine_24h_ml"])
    )
    acidosis = (
        (is_notna(ph_min) and ph_min < thr["shock_ph"]) or
        (is_notna(base_excess_min) and base_excess_min <= thr["shock_base_excess"])
    )

    score = sum(map(int, [hypotension, vasopressor, tissue_hypoperfusion, oliguria, acidosis]))
    return int(score >= 2 or (vasopressor and (tissue_hypoperfusion or acidosis or hypotension)))


def tag_respiratory_failure(row: pd.Series, thr: dict = None) -> int:
    """LAT_RESPIRATORY_FAILURE: score >= 2, or support plus gas-exchange abnormality."""
    thr = thr or DEFAULT_THRESHOLDS
    spo2_min = _first_available(row, "SpO2_min", "SPO2_MIN")
    pf_ratio_min = _first_available(row, "PF_ratio_min", "PAO2_FIO2_MIN")
    fio2_max = _first_available(row, "FiO2_max", "FIO2_MAX")
    rr_max = _first_available(row, "RR_max", "RespRate_max", "RESP_RATE_MAX")
    rr_min = _first_available(row, "RR_min", "RespRate_min", "RESP_RATE_MIN")
    paco2_max = _first_available(row, "PaCO2_max", "PACO2_MAX")
    ph_min = _first_available(row, "pH_min", "PH_min")

    hypoxemia = is_notna(spo2_min) and spo2_min < thr["resp_spo2"]
    oxygenation_failure = is_notna(pf_ratio_min) and pf_ratio_min <= thr["resp_pf"]
    respiratory_support = (
        _flag_any(row, "MechanicalVentilation_any") or
        _flag_any(row, "NonInvasiveVentilation_any") or
        (is_notna(fio2_max) and fio2_max >= thr["resp_fio2"])
    )
    respiratory_rate_abnormal = (
        (is_notna(rr_max) and rr_max >= thr["resp_rr_hi"]) or
        (is_notna(rr_min) and rr_min <= thr["resp_rr_lo"])
    )
    ventilatory_failure = (
        is_notna(paco2_max) and is_notna(ph_min) and
        paco2_max >= thr["resp_paco2"] and ph_min < thr["resp_ph"]
    )

    score = sum(map(int, [hypoxemia, oxygenation_failure, respiratory_support, respiratory_rate_abnormal, ventilatory_failure]))
    return int(score >= 2 or (respiratory_support and (hypoxemia or oxygenation_failure or ventilatory_failure)))


def tag_renal_dysfunction(row: pd.Series, thr: dict = None) -> int:
    """LAT_RENAL_DYSFUNCTION: score >= 2, or dialysis/CRRT present."""
    thr = thr or DEFAULT_THRESHOLDS
    creatinine_max = _first_available(row, "Creatinine_max")
    creatinine_delta = _first_available(row, "Creatinine_delta")
    bun_max = _first_available(row, "BUN_max")
    urine_24h = _first_available(row, "UrineOutput_sum_24h", "UrineOutput_24h", "URINE_OUTPUT_24H")
    urine_6h = _first_available(row, "UrineOutput_mlkg_6h_min", "UrineOutput_6h_mlkg", "URINE_OUTPUT_6H_ML_PER_KG_HR")
    potassium_max = _first_available(row, "Potassium_max")
    bicarbonate_min = _first_available(row, "Bicarbonate_min")

    creatinine_abnormal = (
        (is_notna(creatinine_max) and creatinine_max >= thr["renal_creatinine_abs"]) or
        (is_notna(creatinine_delta) and creatinine_delta >= thr["renal_creatinine_delta"])
    )
    azotemia = is_notna(bun_max) and bun_max >= thr["renal_bun"]
    oliguria = (
        (is_notna(urine_6h) and urine_6h < thr["renal_urine_6h_mlkg"]) or
        (is_notna(urine_24h) and urine_24h < thr["renal_urine_24h_ml"])
    )
    renal_metabolic_consequence = (
        (is_notna(potassium_max) and potassium_max >= thr["renal_potassium_hi"]) or
        (is_notna(bicarbonate_min) and bicarbonate_min < thr["renal_hco3"])
    )
    dialysis = _flag_any(row, "DialysisOrCRRT_any")

    score = sum(map(int, [creatinine_abnormal, azotemia, oliguria, renal_metabolic_consequence, dialysis]))
    return int(score >= 2 or dialysis)


def tag_hepatic_coag_dysfunction(row: pd.Series, thr: dict = None) -> int:
    """LAT_HEPATIC_COAG_DYSFUNCTION: score >= 2 across liver/coagulation domains."""
    thr = thr or DEFAULT_THRESHOLDS
    bilirubin_max = _first_available(row, "Bilirubin_max")
    ast_max = _first_available(row, "AST_max")
    alt_max = _first_available(row, "ALT_max")
    platelets_min = _first_available(row, "Platelets_min")
    inr_max = _first_available(row, "INR_max")
    albumin_min = _first_available(row, "Albumin_min", "Albumin_first")

    bilirubin_elevation = is_notna(bilirubin_max) and bilirubin_max >= thr["hepcoag_bilirubin"]
    hepatocellular_injury = (
        (is_notna(ast_max) and ast_max >= thr["hepcoag_ast"]) or
        (is_notna(alt_max) and alt_max >= thr["hepcoag_alt"])
    )
    thrombocytopenia = is_notna(platelets_min) and platelets_min < thr["hepcoag_platelets"]
    coagulopathy = (
        (is_notna(inr_max) and inr_max >= thr["hepcoag_inr"]) or
        _flag_any(row, "PTProlonged_any") or
        _flag_any(row, "PTTProlonged_any")
    )
    low_albumin = is_notna(albumin_min) and albumin_min < thr["hepcoag_albumin"]

    score = sum(map(int, [bilirubin_elevation, hepatocellular_injury, thrombocytopenia, coagulopathy, low_albumin]))
    return int(score >= 2)


def tag_neurologic_dysfunction(row: pd.Series, thr: dict = None) -> int:
    """LAT_NEUROLOGIC_DYSFUNCTION: neuro score >= 2; isolated sedation-confounded score is not positive."""
    thr = thr or DEFAULT_THRESHOLDS
    gcs_min = _first_available(row, "GCS_min")
    rass_min = _first_available(row, "RASS_min")
    rass_max = _first_available(row, "RASS_max")

    score = 0
    if is_notna(gcs_min) and gcs_min <= thr["neuro_gcs_severe"]:
        score += 2
    elif is_notna(gcs_min) and gcs_min <= thr["neuro_gcs_moderate"]:
        score += 1

    score += int(_flag_any(row, "GCSComponentAbnormal_any"))
    score += int(
        (is_notna(rass_min) and rass_min <= thr["neuro_rass_low"]) or
        (is_notna(rass_max) and rass_max >= thr["neuro_rass_high"])
    )
    score += int(_flag_any(row, "PupilOrFocalNeuroAbnormal_any"))

    if _flag_any(row, "SedationOrIntubation_any") and score == 1:
        return 0
    return int(score >= 2)


def tag_metabolic_derangement(row: pd.Series, thr: dict = None) -> int:
    """LAT_METABOLIC_DERANGEMENT: score >= 2 across acid-base/electrolyte/glucose domains."""
    thr = thr or DEFAULT_THRESHOLDS
    ph_min = _first_available(row, "pH_min", "PH_min")
    ph_max = _first_available(row, "pH_max", "PH_max")
    bicarbonate_min = _first_available(row, "Bicarbonate_min")
    bicarbonate_max = _first_available(row, "Bicarbonate_max")
    base_excess_min = _first_available(row, "BaseExcess_min", "BASE_EXCESS_MIN")
    lactate_max = _first_available(row, "Lactate_max")
    potassium_min = _first_available(row, "Potassium_min")
    potassium_max = _first_available(row, "Potassium_max")
    sodium_min = _first_available(row, "Sodium_min")
    sodium_max = _first_available(row, "Sodium_max")
    glucose_min = _first_available(row, "Glucose_min")
    glucose_max = _first_available(row, "Glucose_max")

    ph_abnormal = (
        (is_notna(ph_min) and ph_min < thr["metab_ph_low"]) or
        (is_notna(ph_max) and ph_max > thr["metab_ph_high"])
    )
    bicarbonate_or_base_abnormal = (
        (is_notna(bicarbonate_min) and bicarbonate_min < thr["metab_hco3_low"]) or
        (is_notna(bicarbonate_max) and bicarbonate_max > thr["metab_hco3_high"]) or
        (is_notna(base_excess_min) and base_excess_min <= thr["metab_base_excess"])
    )
    lactate_elevated = is_notna(lactate_max) and lactate_max > thr["metab_lactate"]
    potassium_abnormal = (
        (is_notna(potassium_min) and potassium_min < thr["metab_potassium_lo"]) or
        (is_notna(potassium_max) and potassium_max >= thr["metab_potassium_hi"])
    )
    sodium_abnormal = (
        (is_notna(sodium_min) and sodium_min < thr["metab_sodium_lo"]) or
        (is_notna(sodium_max) and sodium_max > thr["metab_sodium_hi"])
    )
    glucose_abnormal = (
        (is_notna(glucose_min) and glucose_min < thr["metab_glucose_lo"]) or
        (is_notna(glucose_max) and glucose_max > thr["metab_glucose_hi"])
    )

    score = sum(map(int, [
        ph_abnormal,
        bicarbonate_or_base_abnormal,
        lactate_elevated,
        potassium_abnormal,
        sodium_abnormal,
        glucose_abnormal,
    ]))
    return int(score >= 2)


def tag_cardiac_strain(row: pd.Series, thr: dict = None) -> int:
    """LAT_CARDIAC_STRAIN: score >= 2 with biomarker or rhythm evidence required."""
    thr = thr or DEFAULT_THRESHOLDS
    tropt = _first_available(row, "TroponinT_max")
    tropi = _first_available(row, "TroponinI_max")
    ckmb = _first_available(row, "CKMB_max")
    hr_max = _first_available(row, "HR_max")
    hr_min = _first_available(row, "HR_min")
    first_careunit = _first_careunit_upper(row)

    biomarker = (
        _flag_any(row, "TroponinPositive_any", "TroponinAboveULN_any", "TroponinFlagAbnormal_any") or
        (is_notna(tropt) and tropt >= thr["cardiac_troponin_t_fallback"]) or
        (is_notna(tropi) and tropi >= thr["cardiac_troponin_i_fallback"])
    )
    ckmb_abnormal = _flag_any(row, "CKMBAboveULN_any") or (is_notna(ckmb) and ckmb > 0)
    rhythm_instability = (
        _flag_any(row, "Arrhythmia_any") or
        (is_notna(hr_max) and hr_max > thr["cardiac_hr_hi"]) or
        (is_notna(hr_min) and hr_min < thr["cardiac_hr_lo"])
    )
    hypotension = _hypotension_for_cardiac(row, thr)
    hemodynamic_cardiac_stress = (
        (is_notna(hr_max) and hr_max > thr["cardiac_stress_hr_hi"] and hypotension) or
        (is_notna(hr_min) and hr_min < thr["cardiac_hr_lo"] and hypotension)
    )
    cardiac_care_context = (
        first_careunit in thr["cardiac_context_units"] or
        _flag_any(row, "CardiacSurgeryContext_any")
    )

    score = sum(map(int, [biomarker, ckmb_abnormal, rhythm_instability, hemodynamic_cardiac_stress, cardiac_care_context]))
    return int(score >= 2 and (biomarker or rhythm_instability))


def get_latent_decision_trees(thr: dict = None) -> Dict[str, Callable[[pd.Series], int]]:
    thr = thr or DEFAULT_THRESHOLDS
    return {
        "LAT_CHRONIC_BURDEN": partial(tag_chronic_burden, thr=thr),
        "LAT_INFLAMMATION_SEPSIS": partial(tag_inflammation_sepsis, thr=thr),
        "LAT_GLOBAL_SEVERITY": partial(tag_global_severity, thr=thr),
        "LAT_SHOCK": partial(tag_shock, thr=thr),
        "LAT_RESPIRATORY_FAILURE": partial(tag_respiratory_failure, thr=thr),
        "LAT_RENAL_DYSFUNCTION": partial(tag_renal_dysfunction, thr=thr),
        "LAT_HEPATIC_COAG_DYSFUNCTION": partial(tag_hepatic_coag_dysfunction, thr=thr),
        "LAT_NEUROLOGIC_DYSFUNCTION": partial(tag_neurologic_dysfunction, thr=thr),
        "LAT_METABOLIC_DERANGEMENT": partial(tag_metabolic_derangement, thr=thr),
        "LAT_CARDIAC_STRAIN": partial(tag_cardiac_strain, thr=thr),
    }


# ============================================================
# Raw concept table loading
# ============================================================

@dataclass
class RawConceptTables:
    admissions: Optional[pd.DataFrame] = None
    diagnoses: Optional[pd.DataFrame] = None
    vitals: Optional[pd.DataFrame] = None
    labs: Optional[pd.DataFrame] = None
    urine: Optional[pd.DataFrame] = None
    vaso: Optional[pd.DataFrame] = None
    vent: Optional[pd.DataFrame] = None
    cultures_antibiotics: Optional[pd.DataFrame] = None
    troponin_map: Optional[pd.DataFrame] = None


def maybe_read_csv(path: Optional[str]) -> Optional[pd.DataFrame]:
    if path is None or not os.path.exists(path):
        return None
    return pd.read_csv(path)


def load_raw_concept_tables(args) -> RawConceptTables:
    return RawConceptTables(
        admissions=maybe_read_csv(args.admissions_csv),
        diagnoses=maybe_read_csv(args.diagnoses_csv),
        vitals=maybe_read_csv(args.vitals_csv),
        labs=maybe_read_csv(args.labs_csv),
        urine=maybe_read_csv(args.urine_csv),
        vaso=maybe_read_csv(args.vaso_csv),
        vent=maybe_read_csv(args.vent_csv),
        cultures_antibiotics=maybe_read_csv(args.infection_csv),
        troponin_map=maybe_read_csv(args.troponin_map_csv),
    )


def load_mimic_pickle_payload(pkl_path: str) -> Tuple[pd.DataFrame, pd.DataFrame, List[str]]:
    print(f"      Loading canonical MIMIC pickle payload from: {os.path.abspath(pkl_path)}")
    with open(pkl_path, "rb") as f:
        payload = pickle.load(f)

    if not isinstance(payload, (list, tuple)) or len(payload) != 3:
        raise ValueError(
            "Expected pickle payload [ts, oc, ts_ids]; got an object with a different structure."
        )

    ts, oc, ts_ids = payload
    if not isinstance(ts, pd.DataFrame) or not isinstance(oc, pd.DataFrame):
        raise ValueError("Pickle payload must contain pandas DataFrames for ts and oc.")
    if not isinstance(ts_ids, (list, tuple)):
        raise ValueError("Pickle payload must contain ts_ids as a list or tuple.")

    require_columns(ts, ["ts_id", "minute", "variable", "value"], "ts")
    require_columns(oc, ["ts_id"], "oc")

    ts = ts.loc[:, ["ts_id", "minute", "variable", "value"]].copy()
    ts["ts_id"] = canonicalize_stay_id_series(ts["ts_id"])
    if ts["ts_id"].isna().any():
        raise ValueError("Pickle ts contains missing ts_id values after canonicalization.")
    ts["minute"] = pd.to_numeric(ts["minute"], errors="raise").astype(int)
    ts["variable"] = ts["variable"].astype(str)
    ts["value"] = pd.to_numeric(ts["value"], errors="coerce")
    ts = ts.sort_values(["ts_id", "minute", "variable"]).reset_index(drop=True)

    oc = oc.copy()
    oc["ts_id"] = canonicalize_stay_id_series(oc["ts_id"])
    if oc["ts_id"].isna().any():
        raise ValueError("Pickle oc contains missing ts_id values after canonicalization.")

    ts_ids_series = canonicalize_stay_id_series(pd.Series(list(ts_ids), dtype="object"))
    if ts_ids_series.isna().any():
        raise ValueError("Pickle ts_ids contains missing values after canonicalization.")
    ts_ids = ts_ids_series.tolist()
    if ts_ids != sorted(ts_ids):
        raise ValueError("ts_ids in the pickle must be sorted.")

    ts_ids_from_ts = sorted(ts["ts_id"].unique().tolist())
    if ts_ids != ts_ids_from_ts:
        raise ValueError("ts_ids in the pickle must match sorted(ts.ts_id.unique()).")

    oc_ids = set(oc["ts_id"].astype(str))
    if not oc_ids.issubset(set(ts_ids)):
        raise ValueError("All oc.ts_id values must be contained in ts_ids.")

    print(
        f"      Loaded canonical payload: ts rows={len(ts):,}, oc rows={len(oc):,}, "
        f"stays={len(ts_ids):,}"
    )
    return ts, oc, ts_ids


def validate_mimic_pickle_summary(summary_df: pd.DataFrame) -> None:
    if "InHospitalMortality" not in summary_df.columns:
        raise ValueError(
            "Processed MIMIC pickle is broken: summary construction could not recover "
            "InHospitalMortality from oc. Regenerate the processed MIMIC pickle and "
            "then regenerate the MIMIC latent tags."
        )

    outcome = pd.to_numeric(summary_df["InHospitalMortality"], errors="coerce")
    if int(outcome.notna().sum()) == 0:
        raise ValueError(
            "Processed MIMIC pickle is broken: merged InHospitalMortality is entirely "
            "missing after aligning ts_ids with oc. A known cause is misaligned stay "
            "identifiers such as '12345.0' versus '12345'. Regenerate the processed "
            "MIMIC pickle and then regenerate the MIMIC latent tags."
        )


def _aggregate_minimal_summary_stats_from_ts(ts: pd.DataFrame) -> pd.DataFrame:
    alias_to_target = {}
    for target_name, spec in PICKLE_TS_SUMMARY_SPECS.items():
        for alias in spec["aliases"]:
            alias_to_target[alias] = target_name

    work = ts.loc[ts["variable"].isin(alias_to_target), ["ts_id", "minute", "variable", "value"]].copy()
    if work.empty:
        return pd.DataFrame(columns=["icustay_id"])

    work["target_name"] = work["variable"].map(alias_to_target)
    rows = []
    total_stays = int(work["ts_id"].nunique())
    print(f"      Aggregating canonical summary stats for {total_stays:,} stays")
    for stay_index, (stay_id, g_stay) in enumerate(work.groupby("ts_id", sort=False), start=1):
        row = {"icustay_id": stay_id}
        for target_name, g_var in g_stay.groupby("target_name", sort=False):
            stats = standard_stats(g_var.sort_values("minute")["value"])
            for stat_name, out_col in PICKLE_TS_SUMMARY_SPECS[target_name]["stats"].items():
                row[out_col] = stats[stat_name]
        rows.append(row)
        print_progress("Canonical summary stats aggregated", stay_index, total_stays)

    return pd.DataFrame(rows)


def _aggregate_gcs_min_from_ts(ts: pd.DataFrame) -> pd.DataFrame:
    available_variables = set(ts["variable"].unique())
    missing_components = [col for col in PICKLE_GCS_COMPONENTS if col not in available_variables]
    if missing_components:
        raise ValueError(
            "Pickle mode requires GCS_eye, GCS_motor, and GCS_verbal in ts to build GCS_min. "
            f"Missing: {missing_components}"
        )

    gcs = ts.loc[ts["variable"].isin(PICKLE_GCS_COMPONENTS), ["ts_id", "minute", "variable", "value"]].copy()
    if gcs.empty:
        raise ValueError("Pickle mode could not find any GCS component rows in ts.")

    gcs_wide = gcs.pivot_table(
        index=["ts_id", "minute"],
        columns="variable",
        values="value",
        aggfunc="mean",
    )
    gcs_wide = gcs_wide.dropna(subset=PICKLE_GCS_COMPONENTS)
    if gcs_wide.empty:
        return pd.DataFrame(columns=["icustay_id", "GCS_min"])

    gcs_wide["GCS_total"] = (
        gcs_wide["GCS_eye"] + gcs_wide["GCS_motor"] + gcs_wide["GCS_verbal"]
    )
    out = (
        gcs_wide.reset_index()
        .groupby("ts_id", as_index=False)["GCS_total"]
        .min()
        .rename(columns={"ts_id": "icustay_id", "GCS_total": "GCS_min"})
    )
    return out


def _get_first_weight_by_stay(ts: pd.DataFrame) -> pd.Series:
    weights = ts.loc[ts["variable"] == PICKLE_WEIGHT_VARIABLE, ["ts_id", "minute", "value"]].copy()
    if weights.empty:
        return pd.Series(dtype=float)

    weights = weights.dropna(subset=["value"]).sort_values(["ts_id", "minute"])
    if weights.empty:
        return pd.Series(dtype=float)

    return weights.groupby("ts_id")["value"].first()


def _aggregate_urine_from_ts(ts: pd.DataFrame) -> pd.DataFrame:
    urine = ts.loc[ts["variable"] == PICKLE_URINE_VARIABLE, ["ts_id", "minute", "value"]].copy()
    if urine.empty:
        return pd.DataFrame(columns=["icustay_id", "UrineOutput_sum_24h", "UrineOutput_mlkg_6h_min"])

    urine = urine.dropna(subset=["minute", "value"]).sort_values(["ts_id", "minute"])
    if urine.empty:
        return pd.DataFrame(columns=["icustay_id", "UrineOutput_sum_24h", "UrineOutput_mlkg_6h_min"])

    first_weight = _get_first_weight_by_stay(ts)
    rows = []
    total_stays = int(urine["ts_id"].nunique())
    print(f"      Aggregating urine features for {total_stays:,} stays")
    for stay_index, (stay_id, g) in enumerate(urine.groupby("ts_id", sort=False), start=1):
        row = {"icustay_id": stay_id}

        first_day = g.loc[(g["minute"] >= 0) & (g["minute"] <= 24 * 60), "value"].dropna()
        row["UrineOutput_sum_24h"] = float(first_day.sum()) if len(first_day) else np.nan

        weight = first_weight.get(stay_id, np.nan)
        if is_notna(weight) and weight > 0:
            minutes = g["minute"].to_numpy(dtype=float)
            values = g["value"].to_numpy(dtype=float)
            cumsum = np.cumsum(values)
            window_starts = np.searchsorted(minutes, minutes - 360, side="left")
            window_sums = cumsum.copy()
            mask = window_starts > 0
            window_sums[mask] = window_sums[mask] - cumsum[window_starts[mask] - 1]
            urine_rates = window_sums / weight / 6.0
            row["UrineOutput_mlkg_6h_min"] = float(np.nanmin(urine_rates)) if len(urine_rates) else np.nan
        else:
            row["UrineOutput_mlkg_6h_min"] = np.nan

        rows.append(row)
        print_progress("Urine features aggregated", stay_index, total_stays)

    return pd.DataFrame(rows)


def _aggregate_binary_any_from_ts(
    ts: pd.DataFrame,
    source_variables: Iterable[str],
    out_name: str,
) -> Tuple[pd.DataFrame, bool]:
    source_variables = [var for var in source_variables if var in set(ts["variable"].unique())]
    if not source_variables:
        return pd.DataFrame(columns=["icustay_id", out_name]), False

    work = ts.loc[ts["variable"].isin(source_variables), ["ts_id", "value"]].copy()
    if work.empty:
        return pd.DataFrame(columns=["icustay_id", out_name]), True

    work[out_name] = (work["value"].fillna(0) > 0).astype(int)
    out = (
        work.groupby("ts_id", as_index=False)[out_name]
        .max()
        .rename(columns={"ts_id": "icustay_id"})
    )
    return out, True


def _merge_optional_oc_fields(summary_df: pd.DataFrame, oc: pd.DataFrame) -> pd.DataFrame:
    rename_map = {}
    for out_col, aliases in PICKLE_OC_OPTIONAL_FIELDS.items():
        for alias in aliases:
            if alias in oc.columns:
                rename_map[alias] = out_col
                break

    if not rename_map:
        return summary_df

    oc_small = oc.loc[:, ["ts_id", *rename_map.keys()]].copy()
    oc_small = oc_small.rename(columns={"ts_id": "icustay_id", **rename_map})
    if "InHospitalMortality" in oc_small.columns:
        oc_small["InHospitalMortality"] = pd.to_numeric(
            oc_small["InHospitalMortality"], errors="coerce"
        )

    oc_small = oc_small.drop_duplicates(subset=["icustay_id"])
    return summary_df.merge(oc_small, on="icustay_id", how="left")


def build_summary_df_from_ts_oc(
    ts: pd.DataFrame,
    oc: pd.DataFrame,
    ts_ids: List[str],
) -> pd.DataFrame:
    print(f"      Building canonical summary dataframe for {len(ts_ids):,} stays")
    summary = pd.DataFrame({"icustay_id": ts_ids})

    print("      Stage A: summary statistics from canonical time-series")
    summary = summary.merge(_aggregate_minimal_summary_stats_from_ts(ts), on="icustay_id", how="left")
    print("      Stage B: deriving GCS minima from canonical time-series")
    summary = summary.merge(_aggregate_gcs_min_from_ts(ts), on="icustay_id", how="left")
    print("      Stage C: aggregating urine output features")
    summary = summary.merge(_aggregate_urine_from_ts(ts), on="icustay_id", how="left")
    print("      Stage D: merging optional outcome/context columns from oc")
    summary = _merge_optional_oc_fields(summary, oc)

    for out_name, source_variables in PICKLE_TS_BINARY_HELPERS.items():
        print(f"      Stage E: deriving helper flag '{out_name}'")
        helper_df, available = _aggregate_binary_any_from_ts(ts, source_variables, out_name)
        if available:
            summary = summary.merge(helper_df, on="icustay_id", how="left")
        elif out_name not in summary.columns:
            summary[out_name] = np.nan

    summary = _compute_sirs_features(summary)
    sirs_inputs = [
        "Temperature_min", "Temperature_max", "HR_max", "RR_max", "PaCO2_min", "WBC_min", "WBC_max"
    ]
    sirs_available = [col for col in sirs_inputs if col in summary.columns]
    if sirs_available:
        missing_all_sirs_inputs = summary[sirs_available].isna().all(axis=1)
        summary.loc[missing_all_sirs_inputs, "SIRS_count_max"] = np.nan

    summary = _compute_derived_features(summary)

    for col in PICKLE_EXPECTED_SUMMARY_COLUMNS:
        if col not in summary.columns:
            summary[col] = np.nan

    validate_mimic_pickle_summary(summary)
    print(f"      Canonical summary dataframe ready: {summary.shape}")
    return summary


def load_summary_from_mimic_pickle(pkl_path: str) -> pd.DataFrame:
    ts, oc, ts_ids = load_mimic_pickle_payload(pkl_path)
    return build_summary_df_from_ts_oc(ts, oc, ts_ids)


# ============================================================
# ICD helper flags
# ============================================================

def add_icd_flags(
    admissions_df: pd.DataFrame,
    diagnoses_df: Optional[pd.DataFrame],
) -> pd.DataFrame:
    df = admissions_df.copy()

    if diagnoses_df is None or diagnoses_df.empty:
        df["ChronicICD_any"] = 0
        df["AcuteICD_any"] = 0
        return df

    dx = diagnoses_df.copy()
    for col in ["long_title", "SHORT_TITLE", "short_title", "diagnosis"]:
        if col in dx.columns:
            dx["dx_text"] = dx[col].astype(str)
            break
    else:
        dx["dx_text"] = ""

    dx["dx_text_u"] = dx["dx_text"].str.upper()

    chronic = (
        dx.groupby("icustay_id")["dx_text_u"]
        .apply(lambda s: int(any(any(k in text for k in CHRONIC_ICD_KEYWORDS) for text in s)))
        .rename("ChronicICD_any")
        .reset_index()
    )

    acute = (
        dx.groupby("icustay_id")["dx_text_u"]
        .apply(lambda s: int(any(any(k in text for k in ACUTE_ICD_KEYWORDS) for text in s)))
        .rename("AcuteICD_any")
        .reset_index()
    )

    df = df.merge(chronic, on="icustay_id", how="left")
    df = df.merge(acute, on="icustay_id", how="left")
    df["ChronicICD_any"] = df["ChronicICD_any"].fillna(0).astype(int)
    df["AcuteICD_any"] = df["AcuteICD_any"].fillna(0).astype(int)
    return df


# ============================================================
# Summary building from concept-level data
# ============================================================

def _aggregate_named_variable_events(
    df: pd.DataFrame,
    id_col: str,
    time_col: str,
    variable_col: str,
    value_col: str,
    variables: Iterable[str],
) -> pd.DataFrame:
    """
    Aggregates long-format events into summary columns:
    Variable_min, Variable_max, Variable_mean, Variable_first, Variable_last
    """
    if df is None or df.empty:
        return pd.DataFrame({id_col: []})

    variables = list(variables)
    work = df.copy()
    work = work[work[variable_col].isin(variables)].copy()
    if work.empty:
        return pd.DataFrame({id_col: []})

    work[time_col] = pd.to_datetime(work[time_col], errors="coerce")
    work[value_col] = pd.to_numeric(work[value_col], errors="coerce")
    work = work.dropna(subset=[id_col, time_col])

    rows = []
    total_stays = int(work[id_col].nunique())
    print(
        f"      Aggregating {len(variables)} variables from '{variable_col}' "
        f"for {total_stays:,} stays"
    )
    for stay_index, (stay_id, g) in enumerate(work.groupby(id_col), start=1):
        g = g.sort_values(time_col)
        row = {id_col: stay_id}

        for var, sub in g.groupby(variable_col):
            stats = standard_stats(sub[value_col])
            for stat_name, stat_val in stats.items():
                row[f"{var}_{stat_name}"] = stat_val

        rows.append(row)
        print_progress("Raw-table summary aggregation", stay_index, total_stays)

    return pd.DataFrame(rows)


def _aggregate_binary_any(
    df: pd.DataFrame,
    id_col: str,
    binary_col: str,
    out_name: str,
) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame({id_col: []})
    tmp = df.groupby(id_col)[binary_col].max().reset_index()
    tmp = tmp.rename(columns={binary_col: out_name})
    return tmp


def _aggregate_urine(
    urine_df: Optional[pd.DataFrame],
    id_col: str = "icustay_id",
    time_col: str = "charttime",
    value_col: str = "value",
    weight_col: str = "weight_kg",
) -> pd.DataFrame:
    if urine_df is None or urine_df.empty:
        return pd.DataFrame({id_col: []})

    u = urine_df.copy()
    u[time_col] = pd.to_datetime(u[time_col], errors="coerce")
    u[value_col] = pd.to_numeric(u[value_col], errors="coerce")
    if weight_col in u.columns:
        u[weight_col] = pd.to_numeric(u[weight_col], errors="coerce")

    rows = []
    for stay_id, g in u.groupby(id_col):
        g = g.sort_values(time_col).dropna(subset=[time_col])
        row = {id_col: stay_id}

        if len(g) == 0:
            rows.append(row)
            continue

        # 24h sum from available rows
        row["UrineOutput_sum_24h"] = g[value_col].sum(skipna=True)

        # Approximate 6h rolling normalized urine output if weight exists
        if weight_col in g.columns and g[weight_col].notna().any():
            weight = g[weight_col].dropna().iloc[0]
        else:
            weight = np.nan

        if len(g) >= 1 and is_notna(weight) and weight > 0:
            gg = g[[time_col, value_col]].dropna().copy()
            if len(gg):
                gg = gg.set_index(time_col).sort_index()
                # Rolling 6h total / weight / 6
                roll = gg[value_col].rolling("6H").sum() / weight / 6.0
                row["UrineOutput_mlkg_6h_min"] = roll.min() if len(roll) else np.nan
            else:
                row["UrineOutput_mlkg_6h_min"] = np.nan
        else:
            row["UrineOutput_mlkg_6h_min"] = np.nan

        rows.append(row)

    return pd.DataFrame(rows)


def _aggregate_infection(
    inf_df: Optional[pd.DataFrame],
    id_col: str = "icustay_id",
    suspicion_col: str = "suspected_infection",
) -> pd.DataFrame:
    if inf_df is None or inf_df.empty:
        return pd.DataFrame({id_col: []})

    if suspicion_col not in inf_df.columns:
        tmp = inf_df.copy()
        tmp[suspicion_col] = 1
    else:
        tmp = inf_df.copy()

    out = tmp.groupby(id_col)[suspicion_col].max().reset_index()
    out = out.rename(columns={suspicion_col: "SuspectedInfection_any"})
    return out


def _compute_sirs_features(summary_df: pd.DataFrame) -> pd.DataFrame:
    df = summary_df.copy()

    def sirs_count(row):
        count = 0
        if is_notna(row.get("Temperature_max")) and row["Temperature_max"] > DEFAULT_THRESHOLDS["sirs_temp_hi"]:
            count += 1
        elif is_notna(row.get("Temperature_min")) and row["Temperature_min"] < DEFAULT_THRESHOLDS["sirs_temp_lo"]:
            count += 1

        if is_notna(row.get("HR_max")) and row["HR_max"] > DEFAULT_THRESHOLDS["sirs_hr"]:
            count += 1

        rr_flag = (
            is_notna(row.get("RR_max")) and row["RR_max"] > DEFAULT_THRESHOLDS["sirs_rr"]
        )
        paco2_flag = (
            is_notna(row.get("PaCO2_min")) and row["PaCO2_min"] < DEFAULT_THRESHOLDS["sirs_paco2"]
        )
        if rr_flag or paco2_flag:
            count += 1

        wbc_hi = is_notna(row.get("WBC_max")) and row["WBC_max"] > DEFAULT_THRESHOLDS["sirs_wbc_hi"]
        wbc_lo = is_notna(row.get("WBC_min")) and row["WBC_min"] < DEFAULT_THRESHOLDS["sirs_wbc_lo"]
        if wbc_hi or wbc_lo:
            count += 1

        return count

    df["SIRS_count_max"] = df.apply(sirs_count, axis=1)
    return df


def _compute_derived_features(summary_df: pd.DataFrame) -> pd.DataFrame:
    df = summary_df.copy()

    # FiO2 normalization
    for col in [c for c in df.columns if c.startswith("FiO2_")]:
        df[col] = df[col].apply(normalize_fio2_value)

    # PF ratio: prefer worst oxygenation proxy using PaO2_min and FiO2_max
    df["PF_ratio_min"] = [
        safe_div(a, b)
        for a, b in zip(df.get("PaO2_min", pd.Series(np.nan, index=df.index)),
                        df.get("FiO2_max", pd.Series(np.nan, index=df.index)))
    ]

    # SF ratio
    fio2_for_sf = df["FiO2_max"] if "FiO2_max" in df.columns else pd.Series(np.nan, index=df.index)
    spo2_min = df["SpO2_min"] if "SpO2_min" in df.columns else pd.Series(np.nan, index=df.index)
    df["SF_ratio_min"] = [safe_div(a, b) for a, b in zip(spo2_min, fio2_for_sf)]

    # Creatinine KDIGO helper
    if "Creatinine_max" in df.columns and "Creatinine_first" in df.columns:
        df["Creatinine_delta"] = df["Creatinine_max"] - df["Creatinine_first"]
        df["Creatinine_ratio"] = [
            safe_div(a, b) for a, b in zip(df["Creatinine_max"], df["Creatinine_first"])
        ]
    else:
        df["Creatinine_delta"] = np.nan
        df["Creatinine_ratio"] = np.nan

    return df


def build_summary_from_raw_tables(raw: RawConceptTables) -> pd.DataFrame:
    if raw.admissions is None or raw.admissions.empty:
        raise ValueError(
            "Raw-table mode requires at least admissions_csv with one row per ICU stay "
            "and columns including icustay_id. "
            "You can also skip raw mode and pass --summary_csv."
        )

    admissions = raw.admissions.copy()
    required_id = "icustay_id"
    if required_id not in admissions.columns:
        raise ValueError("admissions_csv must include column 'icustay_id'.")

    summary = admissions.copy()
    print(f"      Admissions rows loaded: {len(summary):,}")

    # ICD-based helper flags
    print("      Stage A: adding ICD-derived helper flags")
    summary = add_icd_flags(summary, raw.diagnoses)

    # Vitals aggregation
    if raw.vitals is not None and not raw.vitals.empty:
        print(f"      Stage B: aggregating vitals rows={len(raw.vitals):,}")
        vitals_summary = _aggregate_named_variable_events(
            raw.vitals,
            id_col="icustay_id",
            time_col="charttime",
            variable_col="variable",
            value_col="value",
            variables=[
                "HR", "SBP", "DBP", "MAP", "RR", "SpO2", "Temperature", "GCS", "RASS", "FiO2"
            ],
        )
        summary = summary.merge(vitals_summary, on="icustay_id", how="left")
        print(f"      Summary shape after vitals merge: {summary.shape}")

    # Labs aggregation
    if raw.labs is not None and not raw.labs.empty:
        print(f"      Stage C: aggregating labs rows={len(raw.labs):,}")
        labs_summary = _aggregate_named_variable_events(
            raw.labs,
            id_col="icustay_id",
            time_col="charttime",
            variable_col="variable",
            value_col="value",
            variables=[
                "Lactate", "PaO2", "PaCO2", "pH", "Bicarbonate", "Creatinine",
                "BUN", "Sodium", "Potassium", "AST", "ALT", "Bilirubin",
                "Albumin", "Platelets", "WBC", "Glucose", "AnionGap",
                "BaseExcess", "TroponinT", "TroponinI", "CKMB", "INR", "PT", "PTT",
            ],
        )
        summary = summary.merge(labs_summary, on="icustay_id", how="left")
        print(f"      Summary shape after labs merge: {summary.shape}")

    # Urine aggregation
    print("      Stage D: aggregating urine features")
    urine_summary = _aggregate_urine(raw.urine)
    summary = summary.merge(urine_summary, on="icustay_id", how="left")
    print(f"      Summary shape after urine merge: {summary.shape}")

    # Vasopressors
    if raw.vaso is not None and not raw.vaso.empty:
        print(f"      Stage E: aggregating vasopressor flags from {len(raw.vaso):,} rows")
        vaso = raw.vaso.copy()
        if "vasopressor" not in vaso.columns:
            vaso["vasopressor"] = 1
        vaso_summary = _aggregate_binary_any(vaso, "icustay_id", "vasopressor", "Vasopressors_any")
        summary = summary.merge(vaso_summary, on="icustay_id", how="left")

    # Mechanical ventilation
    if raw.vent is not None and not raw.vent.empty:
        print(f"      Stage F: aggregating ventilation flags from {len(raw.vent):,} rows")
        vent = raw.vent.copy()
        if "mechanical_ventilation" not in vent.columns:
            vent["mechanical_ventilation"] = 1
        vent_summary = _aggregate_binary_any(vent, "icustay_id", "mechanical_ventilation", "MechanicalVentilation_any")
        summary = summary.merge(vent_summary, on="icustay_id", how="left")

    # Infection flag
    print("      Stage G: aggregating infection suspicion flags")
    infection_summary = _aggregate_infection(raw.cultures_antibiotics)
    summary = summary.merge(infection_summary, on="icustay_id", how="left")

    # Troponin positivity map
    if raw.troponin_map is not None and not raw.troponin_map.empty:
        print(f"      Stage H: aggregating troponin positivity from {len(raw.troponin_map):,} rows")
        tmap = raw.troponin_map.copy()
        cols_needed = {"icustay_id", "troponin_positive"}
        if cols_needed.issubset(set(tmap.columns)):
            tpos = (
                tmap.groupby("icustay_id")["troponin_positive"]
                .max()
                .reset_index()
                .rename(columns={"troponin_positive": "TroponinPositive_any"})
            )
            summary = summary.merge(tpos, on="icustay_id", how="left")

    # Fill absent binary helpers
    for col in [
        "Vasopressors_any", "MechanicalVentilation_any", "NonInvasiveVentilation_any",
        "SuspectedInfection_any", "CultureOrdered_any", "CulturePositive_any",
        "AntibioticStarted_any", "TroponinPositive_any", "TroponinAboveULN_any",
        "CKMBAboveULN_any", "DialysisOrCRRT_any", "Arrhythmia_any",
        "CardiacSurgeryContext_any", "GCSComponentAbnormal_any",
        "PupilOrFocalNeuroAbnormal_any", "SedationOrIntubation_any",
        "PTProlonged_any", "PTTProlonged_any", "MAP_sustained_lt70_any",
    ]:
        if col not in summary.columns:
            summary[col] = 0
        summary[col] = summary[col].fillna(0).astype(int)

    summary = _compute_sirs_features(summary)
    summary = _compute_derived_features(summary)
    print(f"      Raw-table summary dataframe ready: {summary.shape}")
    return summary


# ============================================================
# Summary CSV mode
# ============================================================

def load_summary_csv(summary_csv: str) -> pd.DataFrame:
    df = pd.read_csv(summary_csv)
    if "icustay_id" not in df.columns:
        if "patient_id" in df.columns:
            df = df.rename(columns={"patient_id": "icustay_id"})
        elif "stay_id" in df.columns:
            df = df.rename(columns={"stay_id": "icustay_id"})
        else:
            raise ValueError(
                "summary_csv must contain one of: icustay_id, patient_id, stay_id"
            )

    # Normalize binary helpers if present
    for col in [
        "Vasopressors_any", "MechanicalVentilation_any", "NonInvasiveVentilation_any",
        "SuspectedInfection_any", "CultureOrdered_any", "CulturePositive_any",
        "AntibioticStarted_any", "TroponinPositive_any", "TroponinAboveULN_any",
        "CKMBAboveULN_any", "DialysisOrCRRT_any", "Arrhythmia_any",
        "CardiacSurgeryContext_any", "GCSComponentAbnormal_any",
        "PupilOrFocalNeuroAbnormal_any", "SedationOrIntubation_any",
        "PTProlonged_any", "PTTProlonged_any", "MAP_sustained_lt70_any",
        "ChronicICD_any", "ChronicOrganDisease_any", "MalignancyImmunosuppression_any", "AcuteICD_any",
    ]:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    df = _compute_sirs_features(df) if "SIRS_count_max" not in df.columns else df
    df = _compute_derived_features(df)
    return df


# ============================================================
# Tagging pipeline
# ============================================================

def apply_decision_trees(
    summary_df: pd.DataFrame,
    decision_trees: Dict[str, Callable[[pd.Series], int]],
) -> pd.DataFrame:
    rows = []
    total_rows = len(summary_df)
    print(f"      Applying latent decision trees to {total_rows:,} ICU stays")
    for row_index, (_, row) in enumerate(summary_df.iterrows(), start=1):
        out = {"icustay_id": row["icustay_id"]}
        for latent_name, fn in decision_trees.items():
            out[latent_name] = int(fn(row))
        rows.append(out)
        print_progress("Latent tags applied", row_index, total_rows)
    return pd.DataFrame(rows)


# ============================================================
# Validation
# ============================================================

def prevalence_table(latent_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    n = len(latent_df)
    for latent in LATENT_ORDER:
        if latent not in latent_df.columns:
            continue
        s = latent_df[latent].fillna(0).astype(int)
        rows.append({
            "latent": latent,
            "n_positive": int(s.sum()),
            "prevalence": float(s.mean()) if n > 0 else np.nan,
        })
    return pd.DataFrame(rows)


def mortality_by_tag_table(
    latent_df: pd.DataFrame,
    summary_df: pd.DataFrame,
) -> pd.DataFrame:
    if "InHospitalMortality" not in summary_df.columns:
        return pd.DataFrame(columns=["latent", "mortality_tag0", "mortality_tag1", "risk_ratio"])

    merged = latent_df.merge(
        summary_df[["icustay_id", "InHospitalMortality"]],
        on="icustay_id",
        how="left",
    )

    rows = []
    for latent in LATENT_ORDER:
        if latent not in merged.columns:
            continue

        g0 = merged.loc[merged[latent] == 0, "InHospitalMortality"]
        g1 = merged.loc[merged[latent] == 1, "InHospitalMortality"]

        m0 = float(g0.mean()) if len(g0) else np.nan
        m1 = float(g1.mean()) if len(g1) else np.nan
        rr = safe_div(m1, m0)

        rows.append({
            "latent": latent,
            "n_tag0": int((merged[latent] == 0).sum()),
            "n_tag1": int((merged[latent] == 1).sum()),
            "mortality_tag0": m0,
            "mortality_tag1": m1,
            "risk_ratio": rr,
        })

    return pd.DataFrame(rows)


def cooccurrence_phi_table(latent_df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in LATENT_ORDER if c in latent_df.columns]
    mat = pd.DataFrame(index=cols, columns=cols, dtype=float)

    for c1 in cols:
        for c2 in cols:
            mat.loc[c1, c2] = binary_phi(latent_df[c1], latent_df[c2])

    return mat


def sanity_checks(latent_df: pd.DataFrame) -> Dict[str, dict]:
    results = {}
    for latent in LATENT_ORDER:
        if latent not in latent_df.columns:
            continue
        s = latent_df[latent].fillna(0).astype(int)
        p = float(s.mean()) if len(s) else np.nan
        results[latent] = {
            "all_zero": bool((s == 0).all()),
            "all_one": bool((s == 1).all()),
            "prevalence": p,
            "flag_too_rare_lt_0_5pct": bool(is_notna(p) and p < 0.005),
            "flag_too_common_gt_95pct": bool(is_notna(p) and p > 0.95),
        }
    return results


def build_validation_summary(
    latent_df: pd.DataFrame,
    summary_df: pd.DataFrame,
) -> dict:
    prevalence = prevalence_table(latent_df)
    mortality = mortality_by_tag_table(latent_df, summary_df)
    checks = sanity_checks(latent_df)

    return {
        "n_stays": int(len(latent_df)),
        "available_latents": [c for c in LATENT_ORDER if c in latent_df.columns],
        "prevalence": prevalence.to_dict(orient="records"),
        "mortality_by_tag": mortality.to_dict(orient="records"),
        "sanity_checks": checks,
        "notes": [
            "High-prevalence tags may indicate too-soft thresholds or cohort-specific severity.",
            "Very low-prevalence tags may indicate too-harsh thresholds or missing concept extraction.",
            "Interpret cardiac injury carefully if TroponinPositive_any is unavailable and fallback thresholds are used.",
            "RespFail is more robust when PaO2/FiO2 and SpO2/FiO2 are both available.",
            "RenalDysfunction is more robust when urine output and weight are available.",
        ],
    }


# ============================================================
# Saving
# ============================================================

def _prepare_output_df_with_ts_id(df: pd.DataFrame, df_name: str) -> pd.DataFrame:
    if "icustay_id" not in df.columns:
        raise ValueError(f"{df_name} must contain icustay_id before saving outputs.")

    output_df = df.copy()
    if "ts_id" in output_df.columns:
        existing_ts_id = canonicalize_stay_id_series(output_df["ts_id"])
        internal_ids = canonicalize_stay_id_series(output_df["icustay_id"])
        mismatch = existing_ts_id.notna() & internal_ids.notna() & (existing_ts_id != internal_ids)
        if bool(mismatch.any()):
            raise ValueError(
                f"{df_name} contains both ts_id and icustay_id with conflicting values; "
                "cannot standardize output schema safely."
            )
        output_df = output_df.drop(columns=["ts_id"])

    return output_df.rename(columns={"icustay_id": "ts_id"})


def save_outputs(
    output_dir: str,
    summary_df: pd.DataFrame,
    latent_df: pd.DataFrame,
    decision_trees: dict,
    validation_summary: dict,
) -> None:
    ensure_dir(output_dir)

    tags_path = os.path.join(output_dir, "latent_tags.csv")
    merged_path = os.path.join(output_dir, "latent_tags_with_features.csv")
    trees_path = os.path.join(output_dir, "latent_decision_trees.pkl")
    prevalence_path = os.path.join(output_dir, "prevalence.csv")
    mortality_path = os.path.join(output_dir, "mortality_by_tag.csv")
    cooccur_path = os.path.join(output_dir, "cooccurrence_phi.csv")
    validation_path = os.path.join(output_dir, "validation_summary.json")

    print(f"      Saving output files under: {os.path.abspath(output_dir)}")
    output_summary_df = _prepare_output_df_with_ts_id(summary_df, "summary_df")
    output_latent_df = _prepare_output_df_with_ts_id(latent_df, "latent_df")

    output_latent_df.to_csv(tags_path, index=False)
    output_summary_df.merge(output_latent_df, on="ts_id", how="left").to_csv(merged_path, index=False)
    prevalence_table(latent_df).to_csv(prevalence_path, index=False)
    mortality_by_tag_table(latent_df, summary_df).to_csv(mortality_path, index=False)
    cooccurrence_phi_table(latent_df).to_csv(cooccur_path)

    with open(trees_path, "wb") as f:
        pickle.dump(decision_trees, f)

    with open(validation_path, "w", encoding="utf-8") as f:
        json.dump(validation_summary, f, indent=2)
    print("      Finished saving latent tags, merged features, validation tables, and decision trees")


# ============================================================
# Main
# ============================================================

def parse_args():
    p = argparse.ArgumentParser(description="Rule-based latent variable tagging for MIMIC-III ICU stays.")
    p.add_argument(
        "--dataset-config-csv",
        default=None,
        help=(
            "Path to the dataset global-variables CSV. If omitted, use the default "
            "MIMIC config."
        ),
    )

    # Input modes
    p.add_argument("--summary_csv", type=str, default=None,
                   help="Pre-aggregated summary CSV with one row per ICU stay.")
    p.add_argument("--pkl_path", type=str, default=None,
                   help="PhysioNet-compatible MIMIC pickle storing [ts, oc, ts_ids].")

    # Raw concept CSVs
    p.add_argument("--admissions_csv", type=str, default=None)
    p.add_argument("--diagnoses_csv", type=str, default=None)
    p.add_argument("--vitals_csv", type=str, default=None)
    p.add_argument("--labs_csv", type=str, default=None)
    p.add_argument("--urine_csv", type=str, default=None)
    p.add_argument("--vaso_csv", type=str, default=None)
    p.add_argument("--vent_csv", type=str, default=None)
    p.add_argument("--infection_csv", type=str, default=None)
    p.add_argument("--troponin_map_csv", type=str, default=None)

    # Output
    p.add_argument("--output_dir", type=str, default=None)
    p.add_argument(
        "--validate-config-only",
        action="store_true",
        help="Resolve dataset config values and exit without loading data.",
    )

    return p.parse_args()


def main():
    global LATENT_ORDER
    global DEFAULT_THRESHOLDS
    global CHRONIC_ICD_KEYWORDS
    global ACUTE_ICD_KEYWORDS
    global PICKLE_TS_SUMMARY_SPECS
    global PICKLE_GCS_COMPONENTS
    global PICKLE_URINE_VARIABLE
    global PICKLE_WEIGHT_VARIABLE
    global PICKLE_TS_BINARY_HELPERS
    global PICKLE_OC_OPTIONAL_FIELDS
    global PICKLE_EXPECTED_SUMMARY_COLUMNS
    global PROGRESS_EVERY

    args = parse_args()
    config = load_dataset_config("mimic", args.dataset_config_csv)
    LATENT_ORDER = list(get_config_list(config, "LATENT_ORDER", LATENT_ORDER) or [])
    if isinstance(DEFAULT_THRESHOLDS.get("acute_emergency_types"), list):
        DEFAULT_THRESHOLDS["acute_emergency_types"] = set(
            DEFAULT_THRESHOLDS["acute_emergency_types"]
        )

    if args.pkl_path is None and not args.summary_csv and not any([
        args.admissions_csv,
        args.diagnoses_csv,
        args.vitals_csv,
        args.labs_csv,
        args.urine_csv,
        args.vaso_csv,
        args.vent_csv,
        args.infection_csv,
        args.troponin_map_csv,
    ]):
        args.pkl_path = DEFAULT_PKL_PATH

    output_dir = args.output_dir
    if output_dir is None:
        output_dir = DEFAULT_OUTPUT_DIR

    ensure_dir(output_dir)
    print("=== Starting MIMIC-III latent tagging ===")
    print(f"Output directory: {os.path.abspath(output_dir)}")

    summary_mode = args.summary_csv is not None
    pkl_mode = args.pkl_path is not None
    raw_mode = any([
        args.admissions_csv,
        args.diagnoses_csv,
        args.vitals_csv,
        args.labs_csv,
        args.urine_csv,
        args.vaso_csv,
        args.vent_csv,
        args.infection_csv,
        args.troponin_map_csv,
    ])

    num_modes = int(summary_mode) + int(pkl_mode) + int(raw_mode)
    if num_modes != 1:
        raise ValueError(
            "Provide exactly one input mode: --summary_csv, --pkl_path, "
            "or raw concept CSV inputs (at minimum --admissions_csv for raw mode)."
        )

    if summary_mode:
        print("[1/5] Loading summary CSV...")
        summary_df = load_summary_csv(args.summary_csv)
    elif pkl_mode:
        print("[1/5] Loading MIMIC pickle...")
        print("[2/5] Building summary dataframe from canonical ts/oc...")
        summary_df = load_summary_from_mimic_pickle(args.pkl_path)
    else:
        print("[1/5] Loading raw concept CSVs...")
        raw = load_raw_concept_tables(args)
        print(
            "      Raw table availability: "
            f"admissions={0 if raw.admissions is None else len(raw.admissions):,}, "
            f"diagnoses={0 if raw.diagnoses is None else len(raw.diagnoses):,}, "
            f"vitals={0 if raw.vitals is None else len(raw.vitals):,}, "
            f"labs={0 if raw.labs is None else len(raw.labs):,}, "
            f"urine={0 if raw.urine is None else len(raw.urine):,}, "
            f"vaso={0 if raw.vaso is None else len(raw.vaso):,}, "
            f"vent={0 if raw.vent is None else len(raw.vent):,}, "
            f"infection={0 if raw.cultures_antibiotics is None else len(raw.cultures_antibiotics):,}, "
            f"troponin_map={0 if raw.troponin_map is None else len(raw.troponin_map):,}"
        )
        print("[2/5] Building summary dataframe from raw concept tables...")
        summary_df = build_summary_from_raw_tables(raw)

    if "icustay_id" not in summary_df.columns:
        raise ValueError("Summary dataframe must contain icustay_id.")

    print(f"[3/5] Summary dataframe shape: {summary_df.shape}")

    decision_trees = get_latent_decision_trees()
    print(f"      Latent definitions loaded: {len(decision_trees)}")

    print("[4/5] Applying decision trees...")
    latent_df = apply_decision_trees(summary_df, decision_trees)
    print(f"      Latent tag dataframe shape: {latent_df.shape}")

    print("[5/5] Running validation and saving outputs...")
    validation_summary = build_validation_summary(latent_df, summary_df)
    save_outputs(output_dir, summary_df, latent_df, decision_trees, validation_summary)

    print("\nDone.")
    print(f"Saved outputs to: {os.path.abspath(output_dir)}")
    print("Files:")
    for fname in [
        "latent_tags.csv",
        "latent_tags_with_features.csv",
        "latent_decision_trees.pkl",
        "validation_summary.json",
        "prevalence.csv",
        "mortality_by_tag.csv",
        "cooccurrence_phi.csv",
    ]:
        print(f"  - {fname}")


if __name__ == "__main__":
    main()

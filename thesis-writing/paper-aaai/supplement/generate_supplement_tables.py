#!/usr/bin/env python3
"""Generate technical-appendix tables from checked aggregate evidence only.

The generator never opens patient-level artifacts.  It validates the exact P8
selection predicates and writes deterministic LaTeX fragments under generated/.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


SUPPLEMENT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SUPPLEMENT_DIR.parents[1] / "results"
OUTPUT_DIR = SUPPLEMENT_DIR / "generated"

ESTIMATORS = ("CausalForestDML", "LinearDML", "CausalPFN")
MAIN_STATUS = {
    "CausalForestDML": "PRIMARY_MAIN_TEXT",
    "LinearDML": "SECONDARY_MAIN_TEXT",
    "CausalPFN": "EXPLORATORY_MAIN_TEXT",
}
DATASET_ORDER = ("mimic", "physionet")
DATASET_LABEL = {"mimic": "MIMIC-III", "physionet": "PhysioNet 2012"}
LABELS = {
    "LAT_CARDIAC_STRAIN": "Cardiac strain",
    "LAT_CARDIAC_INJURY_STRAIN": "Cardiac injury/strain",
    "LAT_GLOBAL_SEVERITY": "Global severity",
    "LAT_HEPATIC_COAG_DYSFUNCTION": "Hepatic/coag. dysfunction",
    "LAT_HEPATIC_DYSFUNCTION": "Hepatic dysfunction",
    "LAT_COAG_HEME_DYSFUNCTION": "Coag./heme dysfunction",
    "LAT_INFLAMMATION_SEPSIS": "Inflammation/sepsis",
    "LAT_INFLAMMATION_SEPSIS_BURDEN": "Inflammation/sepsis burden",
    "LAT_METABOLIC_DERANGEMENT": "Metabolic derangement",
    "LAT_NEUROLOGIC_DYSFUNCTION": "Neurologic dysfunction",
    "LAT_RENAL_DYSFUNCTION": "Renal dysfunction",
    "LAT_RESPIRATORY_FAILURE": "Respiratory failure",
    "LAT_SHOCK": "Shock",
}


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS_DIR / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def tex(value: str) -> str:
    return value.replace("_", r"\_").replace("&", r"\&")


def label(treatment: str) -> str:
    return LABELS.get(treatment, treatment.replace("LAT_", "").replace("_", " ").title())


def signed(value: str) -> str:
    return f"{float(value):+.6f}"


def sign(value: str) -> str:
    parsed = float(value)
    return "+" if parsed > 0 else "-" if parsed < 0 else "0"


def write(name: str, content: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / name).write_text(content.rstrip() + "\n", encoding="utf-8")


def selected_cate() -> dict[tuple[str, str, str], dict[str, str]]:
    selected: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows("checked_cate_candidates.csv"):
        estimator = row["estimator"]
        if row["sampling_condition"] != "original" or estimator not in MAIN_STATUS:
            continue
        if row["selection_status"] != MAIN_STATUS[estimator]:
            continue
        key = (row["dataset"], row["treatment"], estimator)
        if key in selected:
            raise ValueError(f"duplicate original selected CATE row: {key}")
        selected[key] = row
    if len(selected) != 57:
        raise ValueError(f"expected 57 original selected CATE rows; got {len(selected)}")
    combinations = {(dataset, treatment) for dataset, treatment, _ in selected}
    expected_counts = {"mimic": 9, "physionet": 10}
    if len(combinations) != 19 or Counter(dataset for dataset, _ in combinations) != expected_counts:
        raise ValueError("original CATE dataset/exposure count mismatch")
    for dataset, treatment in combinations:
        present = {estimator for ds, trt, estimator in selected if (ds, trt) == (dataset, treatment)}
        if present != set(ESTIMATORS):
            raise ValueError(f"missing estimator for {dataset}/{treatment}: {present}")
    return selected


def original_table(selected: dict[tuple[str, str, str], dict[str, str]]) -> None:
    lines = [
        r"\begin{longtable}{@{}p{0.84in}p{1.42in}rrrp{0.68in}@{}}",
        r"\caption{Complete original-cohort estimator summaries (CF-DML denotes CausalForestDML). Values are mean model-estimated CATE summaries over the analyzed samples; display precision is six decimal places.}\label{tab:supp-original-cate}\\",
        r"\toprule Dataset & Exposure & CF-DML & LinearDML & CausalPFN & Sign agreement\\",
        r"\midrule \endfirsthead",
        r"\toprule Dataset & Exposure & CF-DML & LinearDML & CausalPFN & Sign agreement\\",
        r"\midrule \endhead",
    ]
    for dataset in DATASET_ORDER:
        treatments = sorted(
            {treatment for ds, treatment, _ in selected if ds == dataset},
            key=lambda treatment: -float(selected[(dataset, treatment, "CausalForestDML")]["mean_cate"]),
        )
        for treatment in treatments:
            values = [selected[(dataset, treatment, estimator)]["mean_cate"] for estimator in ESTIMATORS]
            agreement = "all three" if len({sign(value) for value in values}) == 1 else "disagreement"
            lines.append(
                f"{DATASET_LABEL[dataset]} & {tex(label(treatment))} & "
                f"{signed(values[0])} & {signed(values[1])} & {signed(values[2])} & {agreement}\\\\"
            )
    lines.append(r"\bottomrule \end{longtable}")
    write("original_estimator_table.tex", "\n".join(lines))


def downsampling_table(selected: dict[tuple[str, str, str], dict[str, str]]) -> None:
    downsampled: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows("checked_cate_candidates.csv"):
        if row["sampling_condition"] != "outcome-downsampled" or row["estimator"] not in MAIN_STATUS:
            continue
        if row["selection_status"] != "ROBUSTNESS_APPENDIX":
            continue
        key = (row["dataset"], row["treatment"], row["estimator"])
        if key in downsampled:
            raise ValueError(f"duplicate downsampled CATE row: {key}")
        downsampled[key] = row
    if len(downsampled) != 57 or set(downsampled) != set(selected):
        raise ValueError("expected exactly one downsampled counterpart for each of 57 original rows")
    lines = [
        r"\begin{longtable}{@{}p{0.78in}p{1.18in}p{0.56in}rrlp{0.62in}@{}}",
        r"\caption{Original versus outcome-downsampled estimator summaries (CF-DML, Linear, and PFN denote CausalForestDML, LinearDML, and CausalPFN). Direction compares signs only; the changed population means magnitudes are not transported between conditions.}\label{tab:supp-downsampling}\\",
        r"\toprule Dataset & Exposure & Estimator & Original & Downsampled & Original sign & Direction\\",
        r"\midrule \endfirsthead",
        r"\toprule Dataset & Exposure & Estimator & Original & Downsampled & Original sign & Direction\\",
        r"\midrule \endhead",
    ]
    changed = 0
    for dataset in DATASET_ORDER:
        keys = sorted((key for key in selected if key[0] == dataset), key=lambda key: (label(key[1]), ESTIMATORS.index(key[2])))
        for key in keys:
            original = selected[key]["mean_cate"]
            down = downsampled[key]["mean_cate"]
            preserved = sign(original) == sign(down)
            changed += not preserved
            lines.append(
                f"{DATASET_LABEL[key[0]]} & {tex(label(key[1]))} & { {'CausalForestDML': 'CF-DML', 'LinearDML': 'Linear', 'CausalPFN': 'PFN'}[key[2]] } & {signed(original)} & {signed(down)} & {sign(original)} & {'preserved' if preserved else 'changed'}\\\\"
            )
    if changed != 2:
        raise ValueError(f"expected two direction changes; got {changed}")
    lines.append(r"\bottomrule \end{longtable}")
    write("downsampling_table.tex", "\n".join(lines))


def matching_table(selected: dict[tuple[str, str, str], dict[str, str]]) -> None:
    successes: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows("checked_matching_results.csv"):
        if row["sampling_condition"] == "original" and "SUPPORTING_MAIN_TEXT[CausalForestDML]" in row["selection_status"]:
            key = (row["dataset"], row["treatment"])
            if key in successes:
                raise ValueError(f"duplicate original matching success: {key}")
            successes[key] = row
    failures: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows("checked_matching_failures.csv"):
        if row["sampling_condition"] == "original" and row["selection_status"] == "SUPPORTING_APPENDIX":
            key = (row["dataset"], row["treatment"])
            if key in failures:
                raise ValueError(f"duplicate original matching failure: {key}")
            failures[key] = row
    combinations = {(dataset, treatment) for dataset, treatment, _ in selected}
    if set(successes) | set(failures) != combinations or set(successes) & set(failures):
        raise ValueError("matching rows do not cover the 19 original CATE exposures exactly")
    if len(successes) != 15 or len(failures) != 4:
        raise ValueError("expected 15 matching successes and 4 failures")
    lines = [
        r"\begin{longtable}{@{}p{0.78in}p{1.10in}p{0.44in}p{0.48in}p{0.54in}p{0.48in}p{1.02in}@{}}",
        r"\caption{Original-cohort matching availability. Failures are retained as failures, not zero effects.}\label{tab:supp-matching}\\",
        r"\toprule Dataset & Exposure & Status & Pairs & Match rate & Final distance & Result / reason\\",
        r"\midrule \endfirsthead",
        r"\toprule Dataset & Exposure & Status & Pairs & Match rate & Final distance & Result / reason\\",
        r"\midrule \endhead",
    ]
    for dataset in DATASET_ORDER:
        for treatment in sorted(treatment for ds, treatment in combinations if ds == dataset):
            key = (dataset, treatment)
            if key in successes:
                row = successes[key]
                result = signed(row["mean_pair_effect"])
                lines.append(f"{DATASET_LABEL[dataset]} & {tex(label(treatment))} & success & {row['n_pairs']} & {float(row['match_rate']):.3f} & {row['final_allowed_distance']} & {result}\\\\")
            else:
                reason = "No binary matching columns after preprocessing"
                lines.append(f"{DATASET_LABEL[dataset]} & {tex(label(treatment))} & failure & -- & -- & -- & {reason}\\\\")
    lines.append(r"\bottomrule \end{longtable}")
    write("matching_table.tex", "\n".join(lines))


def predictive_table() -> None:
    primary = [row for row in rows("checked_predictive_metrics.csv") if row["metric_split"] == "test" and row["selection_status"] == "PRIMARY_MAIN_TEXT"]
    if len(primary) != 8:
        raise ValueError(f"expected eight primary predictive rows; got {len(primary)}")
    rows_by_dataset = Counter(row["dataset"] for row in primary)
    if rows_by_dataset != {"mimic_iii": 4, "physionet_2012": 4}:
        raise ValueError("predictive table dataset counts mismatch")
    lines = [
        r"\begin{table}[H] \centering \small",
        r"\caption{Complete selected archived held-out predictive results. Loss is minimized; the other metrics are maximized. Degenerate target columns are excluded from macro AUROC, AUPRC, and minRP.}\label{tab:supp-predictive}",
        r"\begin{tabular}{llrrrr} \toprule Dataset & Model & Loss & AUROC & AUPRC & minRP\\ \midrule",
    ]
    for dataset, dataset_label in (("mimic_iii", "MIMIC-III"), ("physionet_2012", "PhysioNet 2012")):
        selected_rows = sorted((row for row in primary if row["dataset"] == dataset), key=lambda row: ("strats", "gru", "grud", "tcn").index(row["model"]))
        for index, row in enumerate(selected_rows):
            prefix = dataset_label if index == 0 else ""
            lines.append(f"{prefix} & {row['model'].upper().replace('GRUD', 'GRU-D')} & {float(row['loss']):.6f} & {float(row['auroc']):.6f} & {float(row['auprc']):.6f} & {float(row['minrp']):.6f}\\\\")
    lines.extend([r"\bottomrule \end{tabular}", r"\end{table}"])
    write("predictive_table.tex", "\n".join(lines))


def coverage_table() -> None:
    sensitivity = [row for row in rows("checked_sensitivity_candidates.csv") if row["sampling_condition"] == "original" and row["selection_status"] == "SUPPORTING_APPENDIX"]
    permutations = [row for row in rows("checked_permutation_candidates.csv") if row["sampling_condition"] == "original" and row["selection_status"] == "SUPPORTING_APPENDIX"]
    if not sensitivity or not permutations:
        raise ValueError("missing selected diagnostic evidence")
    sens = Counter((row["estimator"], row["analysis_status"]) for row in sensitivity)
    perm = Counter((row["estimator"], row.get("permutation_type", row.get("diagnostic_name", "recorded"))) for row in permutations)
    sens_text = "; ".join(f"{estimator}: {status}={count}" for (estimator, status), count in sorted(sens.items()))
    perm_text = "; ".join(f"{estimator}: {kind}={count}" for (estimator, kind), count in sorted(perm.items()))
    content = "\n".join([
        r"\begin{table}[H] \centering \small",
        r"\caption{Diagnostic coverage and provenance. Counts are generated from checked aggregate diagnostic records, not inferred from estimator names.}\label{tab:supp-diagnostic-coverage}",
        r"\begin{tabular}{p{0.22\linewidth}p{0.68\linewidth}} \toprule Coverage family & Checked status / boundary\\ \midrule",
        r"Estimator-native sensitivity & Archived DML records distinguish saved-training direct, recomputed/reconstructed, partial, and failed diagnostics; they are not collapsed.\\",
        r"CausalPFN sensitivity & No equivalent archived CausalPFN sensitivity stage; unavailable by archived-stage design.\\",
        rf"Original-cohort sensitivity rows & {tex(sens_text)}.\\",
        r"Treatment permutations & Available only for archived non-PFN estimator stages; disruption diagnostic, not identification proof.\\",
        r"Outcome permutations & Available only for archived non-PFN estimator stages; disruption diagnostic, not identification proof.\\",
        rf"Original-cohort permutation rows & {tex(perm_text)}.\\",
        r"\bottomrule \end{tabular}",
        r"\end{table}",
    ])
    write("diagnostic_coverage_table.tex", content)


def main() -> None:
    selected = selected_cate()
    predictive_table()
    original_table(selected)
    downsampling_table(selected)
    matching_table(selected)
    coverage_table()


if __name__ == "__main__":
    main()

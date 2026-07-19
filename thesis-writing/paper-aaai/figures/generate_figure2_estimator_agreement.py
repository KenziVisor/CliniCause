#!/usr/bin/env python3
"""Generate Figure 2 from the checked original-cohort CATE table.

Input authority: thesis-writing/results/checked_cate_candidates.csv
Selection rule: sampling_condition == "original" and selection_status is the
estimator-specific main-text status. The script requires exactly 19 unique
dataset--exposure combinations, exactly three expected estimators per
combination, and no duplicate estimator rows. Rows are ordered within each
dataset by decreasing CausalForestDML mean_cate.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib as mpl

mpl.use("pdf")
mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 10,
        "legend.fontsize": 9,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)
import matplotlib.pyplot as plt


SCRIPT_PATH = Path(__file__).resolve()
PAPER_DIR = SCRIPT_PATH.parents[1]
INPUT_PATH = PAPER_DIR.parent / "results" / "checked_cate_candidates.csv"
OUTPUT_PATH = SCRIPT_PATH.with_name("figure2_estimator_agreement.pdf")

EXPECTED_ESTIMATORS = ("CausalForestDML", "LinearDML", "CausalPFN")
MAIN_SELECTIONS = {
    "CausalForestDML": "PRIMARY_MAIN_TEXT",
    "LinearDML": "SECONDARY_MAIN_TEXT",
    "CausalPFN": "EXPLORATORY_MAIN_TEXT",
}
EXPECTED_DATASET_COUNTS = {"mimic": 9, "physionet": 10}

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


def load_checked_values() -> dict[str, dict[str, dict[str, float]]]:
    selected: dict[str, dict[str, dict[str, float]]] = {
        dataset: {} for dataset in EXPECTED_DATASET_COUNTS
    }
    with INPUT_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            estimator = row["estimator"]
            if row["sampling_condition"] != "original":
                continue
            if estimator not in MAIN_SELECTIONS:
                continue
            if row["selection_status"] != MAIN_SELECTIONS[estimator]:
                continue
            dataset = row["dataset"]
            if dataset not in selected:
                raise ValueError(f"Unexpected selected dataset: {dataset}")
            treatment = row["treatment"]
            values = selected[dataset].setdefault(treatment, {})
            if estimator in values:
                raise ValueError(
                    f"Duplicate selected row: {dataset}/{treatment}/{estimator}"
                )
            values[estimator] = float(row["mean_cate"])

    combination_count = sum(len(rows) for rows in selected.values())
    if combination_count != 19:
        raise ValueError(f"Expected 19 dataset--exposure combinations; got {combination_count}")
    for dataset, expected_count in EXPECTED_DATASET_COUNTS.items():
        if len(selected[dataset]) != expected_count:
            raise ValueError(
                f"Expected {expected_count} {dataset} exposures; got {len(selected[dataset])}"
            )
        for treatment, values in selected[dataset].items():
            if set(values) != set(EXPECTED_ESTIMATORS):
                raise ValueError(
                    f"Missing/unexpected estimator for {dataset}/{treatment}: "
                    f"{sorted(values)}"
                )
    return selected


def main() -> None:
    selected = load_checked_values()
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.65), constrained_layout=True)
    styles = {
        "CausalForestDML": dict(marker="o", color="#000000", label="CausalForestDML"),
        "LinearDML": dict(marker="s", color="#4D4D4D", label="LinearDML"),
        "CausalPFN": dict(marker="^", color="#8C510A", label="CausalPFN"),
    }
    offsets = {"CausalForestDML": 0.20, "LinearDML": 0.0, "CausalPFN": -0.20}

    for axis, dataset, title in zip(
        axes, ("mimic", "physionet"), ("MIMIC-III", "PhysioNet 2012")
    ):
        rows = sorted(
            selected[dataset].items(),
            key=lambda item: item[1]["CausalForestDML"],
            reverse=True,
        )
        base_y = list(range(len(rows)))[::-1]
        for estimator in EXPECTED_ESTIMATORS:
            axis.scatter(
                [values[estimator] for _, values in rows],
                [y + offsets[estimator] for y in base_y],
                s=27,
                linewidth=0.8,
                edgecolor="white" if estimator == "CausalPFN" else styles[estimator]["color"],
                zorder=3,
                **styles[estimator],
            )
        axis.axvline(0.0, color="#666666", linewidth=0.8, linestyle="--", zorder=1)
        axis.grid(axis="x", color="#D0D0D0", linewidth=0.45, zorder=0)
        axis.set_yticks(base_y, [LABELS[treatment] for treatment, _ in rows])
        axis.set_title(title, fontweight="bold", pad=5)
        axis.set_xlabel("Mean model-estimated CATE")
        axis.tick_params(axis="y", length=0, pad=3)
        axis.spines[["top", "right", "left"]].set_visible(False)
        axis.spines["bottom"].set_linewidth(0.7)
        axis.margins(y=0.08)

    axes[0].set_xlim(-0.035, 0.275)
    axes[1].set_xlim(-0.035, 0.135)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="outside upper center",
        ncol=3,
        frameon=False,
        handletextpad=0.4,
        columnspacing=1.2,
    )
    fig.savefig(
        OUTPUT_PATH,
        format="pdf",
        bbox_inches="tight",
        pad_inches=0.02,
        metadata={
            "Creator": "CliniCause Figure 2 generation script",
            "Producer": "Matplotlib PDF backend",
            "CreationDate": None,
            "ModDate": None,
        },
    )
    plt.close(fig)


if __name__ == "__main__":
    main()

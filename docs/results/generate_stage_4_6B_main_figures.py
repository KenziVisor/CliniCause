#!/usr/bin/env python3
"""Generate the three Stage 4.6B-R main-results figures from checked CATE rows."""

from __future__ import annotations

import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = REPOSITORY_ROOT / "thesis-writing/results/checked_cate_candidates.csv"
OUTPUT_DIR = REPOSITORY_ROOT / "thesis-writing/thesis/figures"

REQUIRED_COLUMNS = {
    "dataset",
    "estimator",
    "sampling_condition",
    "treatment",
    "mean_cate",
    "selection_status",
}
KEY_COLUMNS = ("dataset", "estimator", "sampling_condition", "treatment")
ESTIMATORS = ("CausalForestDML", "LinearDML", "CausalPFN")

RANKING_CONFIGS = (
    {
        "dataset": "mimic",
        "dataset_title": "MIMIC-III",
        "expected_rows": 9,
        "output": "results_mimic_forest_original_cate_ranking.png",
        "color": "#35689A",
    },
    {
        "dataset": "physionet",
        "dataset_title": "PhysioNet 2012",
        "expected_rows": 10,
        "output": "results_physionet_forest_original_cate_ranking.png",
        "color": "#2A7F62",
    },
)


def fail(message: str) -> "NoReturn":
    raise ValueError(message)


def read_checked_rows() -> list[dict[str, str]]:
    if not INPUT_PATH.is_file():
        fail(f"Missing checked input: {INPUT_PATH}")
    with INPUT_PATH.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - columns)
        if missing:
            fail(f"Checked input is missing required columns: {missing}")
        rows = list(reader)
    if not rows:
        fail("Checked input contains no data rows")

    seen: set[tuple[str, ...]] = set()
    for csv_line, row in enumerate(rows, start=2):
        key = tuple(row[column] for column in KEY_COLUMNS)
        if key in seen:
            fail(f"Duplicate dataset-estimator-sampling-exposure row at CSV line {csv_line}: {key}")
        seen.add(key)
    return rows


def exact_mean(row: dict[str, str]) -> float:
    raw = row["mean_cate"].strip()
    if not raw:
        fail(f"Missing mean_cate for {tuple(row[column] for column in KEY_COLUMNS)}")
    try:
        value = float(raw)
    except ValueError as error:
        fail(f"Non-numeric mean_cate {raw!r}: {error}")
    if not math.isfinite(value):
        fail(f"Non-finite mean_cate {raw!r}")
    return value


def display_value(value: float) -> str:
    decimals = 4 if value != 0.0 and round(value, 3) == 0.0 else 3
    return f"{value:.{decimals}f}"


def human_label(identifier: str) -> str:
    prefix = "LAT_"
    if not identifier.startswith(prefix):
        fail(f"Unexpected proxy-state identifier: {identifier}")
    friendly = identifier[len(prefix) :].replace("_", " ").title()
    return f"{friendly}\n({identifier})"


def select_ranking_rows(rows: list[dict[str, str]], dataset: str, expected_rows: int) -> list[dict[str, str]]:
    selected = [
        row
        for row in rows
        if row["dataset"] == dataset
        and row["estimator"] == "CausalForestDML"
        and row["sampling_condition"] == "original"
        and row["selection_status"] == "PRIMARY_MAIN_TEXT"
    ]
    if len(selected) != expected_rows:
        fail(f"{dataset}: expected {expected_rows} primary original Forest rows, found {len(selected)}")
    treatments = [row["treatment"] for row in selected]
    if len(set(treatments)) != expected_rows:
        fail(f"{dataset}: expected {expected_rows} unique exposures, found {len(set(treatments))}")
    for row in selected:
        exact_mean(row)
    return sorted(selected, key=lambda row: (-exact_mean(row), row["treatment"]))


def configure_matplotlib() -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 15,
            "axes.labelsize": 11,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 10,
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "savefig.facecolor": "white",
            "axes.facecolor": "white",
        }
    )


def save_ranking_figure(config: dict[str, object], selected: list[dict[str, str]]) -> Path:
    values = [exact_mean(row) for row in selected]
    labels = [human_label(row["treatment"]) for row in selected]
    height = 7.4 if len(selected) == 9 else 8.1
    fig, ax = plt.subplots(figsize=(11.2, height), constrained_layout=True)
    positions = list(range(len(selected)))
    bars = ax.barh(positions, values, color=str(config["color"]), edgecolor="white", linewidth=0.6)
    ax.set_yticks(positions, labels)
    ax.invert_yaxis()
    ax.axvline(0.0, color="#333333", linewidth=1.0)
    ax.set_xlabel("Mean model-estimated CATE")
    ax.set_title(f"{config['dataset_title']} — CausalForestDML\nOriginal cohort", pad=12)
    ax.xaxis.grid(True, linestyle="--", alpha=0.30)
    ax.set_axisbelow(True)

    span = max(values) - min(0.0, min(values))
    padding = max(span * 0.025, 0.0025)
    for bar, value in zip(bars, values):
        if value >= 0:
            x = value + padding
            alignment = "left"
        else:
            x = value - padding
            alignment = "right"
        ax.text(x, bar.get_y() + bar.get_height() / 2, display_value(value), va="center", ha=alignment, fontsize=9)

    left = min(0.0, min(values)) - max(span * 0.12, 0.008)
    right = max(values) + max(span * 0.13, 0.012)
    ax.set_xlim(left, right)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    output_path = OUTPUT_DIR / str(config["output"])
    fig.savefig(output_path, metadata={"Software": "CliniCause Stage 4.6B-R checked-CSV generator"})
    plt.close(fig)
    return output_path


def build_direction_counts(rows: list[dict[str, str]]) -> tuple[dict[str, dict[str, int]], list[tuple[str, str, dict[str, int]]]]:
    original = [
        row
        for row in rows
        if row["sampling_condition"] == "original" and row["estimator"] in ESTIMATORS
    ]
    joined: dict[tuple[str, str], dict[str, dict[str, str]]] = defaultdict(dict)
    for row in original:
        joined[(row["dataset"], row["treatment"])][row["estimator"]] = row

    counts: dict[str, dict[str, int]] = defaultdict(lambda: {"concordant": 0, "discordant": 0})
    comparisons: list[tuple[str, str, dict[str, int]]] = []
    for (dataset, treatment), estimator_rows in sorted(joined.items()):
        if set(estimator_rows) != set(ESTIMATORS):
            fail(
                f"{dataset} {treatment}: expected exactly one original row for each estimator; "
                f"found {sorted(estimator_rows)}"
            )
        signs = {
            estimator: (1 if exact_mean(estimator_rows[estimator]) > 0 else -1 if exact_mean(estimator_rows[estimator]) < 0 else 0)
            for estimator in ESTIMATORS
        }
        status = "concordant" if len(set(signs.values())) == 1 else "discordant"
        counts[dataset][status] += 1
        comparisons.append((dataset, treatment, signs))

    expected = {
        "mimic": {"concordant": 9, "discordant": 0},
        "physionet": {"concordant": 9, "discordant": 1},
    }
    if dict(counts) != expected:
        fail(f"Unexpected direction counts: {dict(counts)}")
    discordant = [(dataset, treatment, signs) for dataset, treatment, signs in comparisons if len(set(signs.values())) != 1]
    if len(discordant) != 1:
        fail(f"Expected one discordant comparison, found {discordant}")
    dataset, treatment, signs = discordant[0]
    expected_signs = {"CausalForestDML": -1, "LinearDML": -1, "CausalPFN": 1}
    if (dataset, treatment) != ("physionet", "LAT_SHOCK") or signs != expected_signs:
        fail(f"Unexpected sole direction exception: {discordant[0]}")
    return dict(counts), comparisons


def save_direction_figure(counts: dict[str, dict[str, int]]) -> Path:
    datasets = ("mimic", "physionet")
    labels = ("MIMIC-III", "PhysioNet 2012")
    concordant = [counts[dataset]["concordant"] for dataset in datasets]
    discordant = [counts[dataset]["discordant"] for dataset in datasets]
    totals = [a + b for a, b in zip(concordant, discordant)]

    fig, ax = plt.subplots(figsize=(10.2, 5.8), constrained_layout=True)
    positions = list(range(len(datasets)))
    ax.barh(positions, concordant, color="#2A7F62", label="Concordant across all three")
    ax.barh(positions, discordant, left=concordant, color="#D18A2E", label="Not concordant across all three")
    ax.set_yticks(positions, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, max(totals) + 0.8)
    ax.set_xlabel("Dataset–exposure comparisons (count)")
    ax.set_title(
        "Original-cohort direction agreement across three estimators\n"
        "18/19 overall\n"
        "Exception: PhysioNet LAT_SHOCK (Forest/Linear negative; CausalPFN positive)",
        pad=12,
        fontsize=13,
    )
    ax.xaxis.grid(True, linestyle="--", alpha=0.25)
    ax.set_axisbelow(True)

    for position, (same, total) in enumerate(zip(concordant, totals)):
        ax.text(same / 2, position, f"{same}/{total}", ha="center", va="center", color="white", fontweight="bold", fontsize=11)
        if total > same:
            ax.text(same + (total - same) / 2, position, str(total - same), ha="center", va="center", color="white", fontweight="bold")

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    output_path = OUTPUT_DIR / "results_original_three_estimator_direction_agreement.png"
    fig.savefig(output_path, metadata={"Software": "CliniCause Stage 4.6B-R checked-CSV generator"})
    plt.close(fig)
    return output_path


def main() -> int:
    rows = read_checked_rows()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    configure_matplotlib()

    print(f"INPUT {INPUT_PATH.relative_to(REPOSITORY_ROOT)} rows={len(rows)}")
    for config in RANKING_CONFIGS:
        selected = select_ranking_rows(rows, str(config["dataset"]), int(config["expected_rows"]))
        print(
            "FILTER "
            f"dataset={config['dataset']} estimator=CausalForestDML sampling_condition=original "
            f"selection_status=PRIMARY_MAIN_TEXT rows={len(selected)}"
        )
        for rank, row in enumerate(selected, start=1):
            print(
                f"RANK {rank} dataset={row['dataset']} treatment={row['treatment']} "
                f"mean_cate_exact={row['mean_cate']} display={display_value(exact_mean(row))}"
            )
        output = save_ranking_figure(config, selected)
        print(f"WROTE {output.relative_to(REPOSITORY_ROOT)}")

    counts, comparisons = build_direction_counts(rows)
    for dataset, treatment, signs in comparisons:
        print(
            f"DIRECTION dataset={dataset} treatment={treatment} "
            + " ".join(f"{estimator}={signs[estimator]:+d}" for estimator in ESTIMATORS)
        )
    overall_concordant = sum(item["concordant"] for item in counts.values())
    overall_total = sum(item["concordant"] + item["discordant"] for item in counts.values())
    print(
        "COUNTS "
        f"mimic={counts['mimic']['concordant']}/{sum(counts['mimic'].values())} "
        f"physionet={counts['physionet']['concordant']}/{sum(counts['physionet'].values())} "
        f"overall={overall_concordant}/{overall_total}"
    )
    output = save_direction_figure(counts)
    print(f"WROTE {output.relative_to(REPOSITORY_ROOT)}")
    print("VALIDATION PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"VALIDATION ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)

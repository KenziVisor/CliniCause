#!/usr/bin/env python3
"""Generate the paper-native Figure 1 construction-pipeline diagram.

This script contains workflow labels only.  It reads no data, is deterministic,
and writes a vector PDF with stable metadata.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("pdf")
mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT_PATH = Path(__file__).with_name("figure1_pipeline.pdf")


def box(ax, x, y, w, h, text, *, face="#F2F2F2", edge="#333333", bold=False):
    patch = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=0.8, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=7.2, fontweight=("bold" if bold else "normal"), wrap=True)
    return (x, y, w, h)


def arrow(ax, start, end, *, style="->", color="#3F3F3F", dashed=False):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle=style, mutation_scale=8, linewidth=0.85,
        color=color, linestyle="--" if dashed else "-", shrinkA=2, shrinkB=2,
        connectionstyle="arc3,rad=0.0",
    ))


def right(rect):
    x, y, w, h = rect
    return (x + w, y + h / 2)


def left(rect):
    x, y, w, h = rect
    return (x, y + h / 2)


def top(rect):
    x, y, w, h = rect
    return (x + w / 2, y + h)


def bottom(rect):
    x, y, w, h = rect
    return (x + w / 2, y)


def stage(ax, separator, label, subtitle, header_y):
    ax.text(0.012, header_y - 0.04, label, rotation=90, ha="center", va="center",
            fontsize=7.8, fontweight="bold", color="#222222")
    ax.plot([0.035, 0.985], [separator, separator], color="#767676", lw=0.65)
    ax.text(0.045, header_y, subtitle, ha="left", va="top", fontsize=7.8,
            fontweight="bold", color="#222222")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.05, 2.45))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")

    # Design-time lane: intentionally isolated from runtime records.
    stage(ax, 0.71, "1", "Design time", 0.98)
    design = box(ax, 0.05, 0.78, 0.15, 0.095, "Dataset\ndescriptions", face="#FFFFFF")
    llm = box(ax, 0.25, 0.78, 0.20, 0.095, "Structured LLM\nproposals", face="#E8E8E8")
    selection = box(ax, 0.50, 0.78, 0.15, 0.095, "Project / human\nselection", face="#FFFFFF")
    source = box(ax, 0.70, 0.78, 0.25, 0.095, "Deterministic rule /\nDAG source artifacts", face="#D9D9D9", bold=True)
    arrow(ax, right(design), left(llm)); arrow(ax, right(llm), left(selection)); arrow(ax, right(selection), left(source))
    ax.text(0.50, 0.745, "LLM: design-time only; no patient rows; not an estimator",
            ha="center", va="top", fontsize=6.6, style="italic", color="#444444")

    # Dataset construction lane, with clearly separate data lanes.
    stage(ax, 0.285, "2", "Construction: separate source lanes (not pooled)", 0.69)
    ax.text(0.09, 0.555, "MIMIC-III", ha="center", va="center", fontsize=7.1, fontweight="bold")
    ax.text(0.09, 0.425, "PhysioNet 2012", ha="center", va="center", fontsize=7.1, fontweight="bold")
    mimic = box(ax, 0.16, 0.515, 0.14, 0.075, "Irregular\nrecords", face="#FFFFFF")
    phys = box(ax, 0.16, 0.385, 0.14, 0.075, "Irregular\nrecords", face="#FFFFFF")
    prep_m = box(ax, 0.34, 0.515, 0.16, 0.075, "Preprocess +\ncanonical IDs", face="#F6F6F6")
    prep_p = box(ax, 0.34, 0.385, 0.16, 0.075, "Preprocess +\ncanonical IDs", face="#F6F6F6")
    rules_m = box(ax, 0.54, 0.515, 0.14, 0.075, "Deterministic\nrules", face="#F6F6F6")
    rules_p = box(ax, 0.54, 0.385, 0.14, 0.075, "Deterministic\nrules", face="#F6F6F6")
    models_m = box(ax, 0.73, 0.515, 0.20, 0.075, "STraTS / GRU /\nGRU-D / TCN", face="#F6F6F6")
    models_p = box(ax, 0.73, 0.385, 0.20, 0.075, "STraTS / GRU /\nGRU-D / TCN", face="#F6F6F6")
    for a, b, c, d in ((mimic, prep_m, rules_m, models_m), (phys, prep_p, rules_p, models_p)):
        arrow(ax, right(a), left(b)); arrow(ax, right(b), left(c)); arrow(ax, right(c), left(d))
    ax.text(0.83, 0.655, "encoded source governs runtime", ha="center", va="center", fontsize=5.7, color="#555555")
    ax.text(0.42, 0.485, "schema / ID gate", ha="center", va="center", fontsize=5.6, color="#444444")
    ax.text(0.83, 0.485, "prediction-export gate", ha="center", va="center", fontsize=5.6, color="#444444")

    exports = box(ax, 0.06, 0.305, 0.20, 0.052, "Normalized probability\n+ binary exports", face="#F6F6F6")
    aggregate = box(ax, 0.34, 0.305, 0.18, 0.052, "Five-source\naggregation", face="#D9D9D9", bold=True)
    resource_m = box(ax, 0.60, 0.32, 0.32, 0.042, "MIMIC-III estimator-ready resource", face="#E1E1E1", bold=True)
    resource_p = box(ax, 0.60, 0.255, 0.32, 0.042, "PhysioNet estimator-ready resource", face="#E1E1E1", bold=True)
    arrow(ax, bottom(models_m), (0.16, 0.357)); arrow(ax, bottom(models_p), (0.16, 0.357))
    arrow(ax, right(exports), left(aggregate)); arrow(ax, right(aggregate), left(resource_m)); arrow(ax, right(aggregate), left(resource_p))
    ax.text(0.43, 0.295, "aggregation + cohort-alignment gate", ha="center", va="top", fontsize=5.6, color="#444444")
    ax.text(0.76, 0.238, "outcome + covariates + DAG/adjustment + provenance", ha="center", va="top", fontsize=5.5, color="#333333")

    # Downstream characterization is source-specific but method-shared.
    stage(ax, 0.075, "3", "Downstream characterization", 0.18)
    downstream = box(ax, 0.07, 0.005, 0.84, 0.055,
                     "CausalForestDML  |  LinearDML  |  CausalPFN  |  matching\nsensitivity/permutation diagnostics  |  outcome-downsampling robustness",
                     face="#F2F2F2")
    arrow(ax, bottom(resource_m), (0.38, 0.06)); arrow(ax, bottom(resource_p), (0.62, 0.06))
    ax.text(0.91, 0.075, "provenance / manifest gate", ha="right", va="bottom", fontsize=5.7, color="#444444")

    fig.savefig(OUTPUT_PATH, format="pdf", bbox_inches="tight", pad_inches=0.02,
                metadata={"Creator": "CliniCause Figure 1 generation script", "Producer": "Matplotlib PDF backend", "CreationDate": None, "ModDate": None})
    plt.close(fig)


if __name__ == "__main__":
    main()

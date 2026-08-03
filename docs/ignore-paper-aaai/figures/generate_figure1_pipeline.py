#!/usr/bin/env python3
"""Generate the data-free, deterministic Figure 1 construction diagram."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("pdf")
mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT_PATH = Path(__file__).with_name("figure1_pipeline.pdf")

# The PDF is placed at 0.99\textwidth.  These source sizes retain roughly
# 9 pt primary type after that modest final-width scaling.
PRIMARY_SIZE = 10.0
HEADING_SIZE = 10.2
SECONDARY_SIZE = 9.3


def box(ax, x, y, w, h, text, *, face="#F4F4F4", bold=False, size=PRIMARY_SIZE):
    """Draw one compact, grayscale-safe workflow box."""
    rect = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.07",
        linewidth=0.85, edgecolor="#333333", facecolor=face,
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size,
        fontweight="bold" if bold else "normal", color="#202020",
    )
    return (x, y, w, h)


def arrow(ax, start, end, *, dashed=False, rad=0.0):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="->", mutation_scale=9, linewidth=0.9,
        color="#3E3E3E", linestyle="--" if dashed else "-",
        shrinkA=3, shrinkB=3, connectionstyle=f"arc3,rad={rad}",
    ))


def left(rect):
    x, y, _, h = rect
    return x, y + h / 2


def right(rect):
    x, y, w, h = rect
    return x + w, y + h / 2


def top(rect):
    x, y, w, h = rect
    return x + w / 2, y + h


def bottom(rect):
    x, y, w, _ = rect
    return x + w / 2, y


def band(ax, y, title, number):
    ax.plot([0.35, 13.7], [y, y], color="#737373", linewidth=0.7)
    ax.text(0.08, y + 0.12, number, ha="center", va="bottom", fontsize=HEADING_SIZE,
            fontweight="bold", color="#202020")
    ax.text(0.42, y + 0.12, title, ha="left", va="bottom", fontsize=HEADING_SIZE,
            fontweight="bold", color="#202020")


def lane_label(ax, y, text):
    ax.text(0.55, y, text, ha="left", va="center", fontsize=HEADING_SIZE,
            fontweight="bold", color="#202020")


def route_to_downstream(ax, rect, *, route_x, entry_x):
    """Route a completed resource around, rather than through, the other lane."""
    start = left(rect)
    entry_y = 1.97
    ax.plot([start[0], route_x, route_x, entry_x - 0.22],
            [start[1], start[1], entry_y, entry_y],
            color="#3E3E3E", linewidth=0.9)
    arrow(ax, (entry_x - 0.22, entry_y), (entry_x, entry_y))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.12, 4.50))
    fig.subplots_adjust(left=0.01, right=0.995, bottom=0.015, top=0.99)
    ax.set(xlim=(0, 14), ylim=(0, 10))
    ax.axis("off")

    # 1. The LLM belongs only to the design-time band, never the record lanes.
    band(ax, 8.25, "Design time", "1")
    descriptions = box(ax, 0.65, 9.05, 2.0, 0.58, "Dataset\ndescriptions", face="#FFFFFF")
    proposals = box(ax, 3.15, 9.05, 2.25, 0.58, "Structured LLM\nproposals", face="#E7E7E7")
    selection = box(ax, 5.90, 9.05, 2.15, 0.58, "Project / human\nselection", face="#FFFFFF")
    source = box(ax, 8.55, 9.05, 3.45, 0.58, "Deterministic rule and\nDAG source", face="#D9D9D9", bold=True)
    arrow(ax, right(descriptions), left(proposals))
    arrow(ax, right(proposals), left(selection))
    arrow(ax, right(selection), left(source))
    ax.text(6.9, 8.67, "Design time only; no patient rows; not an estimator",
            ha="center", va="center", fontsize=SECONDARY_SIZE, style="italic", color="#3F3F3F")

    # 2. Parallel runtime lanes.  No construction box is shared between sources.
    band(ax, 7.68, "Construction: independent dataset lanes", "2")
    ax.text(6.00, 7.18,
            "Gates per lane: schema/ID | prediction export\n"
            "voter/cohort | output/provenance",
            ha="left", va="center", fontsize=SECONDARY_SIZE, color="#444444")
    top_columns = [
        (0.78, 2.20, "Irregular\nrecords"),
        (3.60, 2.20, "Preprocess\n+ IDs"),
        (6.42, 2.20, "Rule\nlabels"),
        (9.24, 2.45, "4 model\nannotations"),
    ]
    # The lower row runs right-to-left, making each lane a legible continuous
    # path without forcing shared exports, aggregation, or causal resources.
    lower_columns = [
        (0.78, 2.20, "Estimator-ready\nresource", "#DEDEDE", True),
        (3.60, 2.20, "DAG + adjustment\n+ provenance", "#F4F4F4", False),
        (6.42, 2.20, "Outcome +\ncovariates", "#F4F4F4", False),
        (9.24, 2.45, "5-source vote", "#D9D9D9", True),
        (12.02, 1.55, "Normalize\nexports", "#F4F4F4", False),
    ]
    mimic_top_y, mimic_bottom_y = 6.18, 5.17
    phys_top_y, phys_bottom_y = 3.93, 2.92
    height = 0.64
    lane_label(ax, 6.96, "MIMIC-III lane")
    lane_label(ax, 4.71, "PhysioNet 2012 lane")
    lanes = []
    for top_y, lower_y in ((mimic_top_y, mimic_bottom_y), (phys_top_y, phys_bottom_y)):
        upper = [box(ax, x, top_y, w, height, label, face="#F4F4F4")
                 for x, w, label in top_columns]
        lower = [box(ax, x, lower_y, w, height, label, face=face, bold=bold)
                 for x, w, label, face, bold in lower_columns]
        for current, following in zip(upper, upper[1:]):
            arrow(ax, right(current), left(following))
        arrow(ax, right(upper[-1]), top(lower[-1]))
        for current, following in zip(reversed(lower), reversed(lower[:-1])):
            arrow(ax, left(current), right(following))
        lanes.append((upper, lower))
    mimic, phys = lanes

    # 3. Only completed resources meet the shared method family.
    band(ax, 2.32, "Downstream characterization", "3")
    downstream = box(
        ax, 2.00, 0.85, 10.45, 1.12,
        "Shared method interface; separate execution and results\n"
        "CausalForestDML  |  LinearDML  |  CausalPFN  |  matching\n"
        "sensitivity / permutations  |  outcome downsampling",
        face="#EFEFEF", bold=True,
    )
    route_to_downstream(ax, mimic[1][0], route_x=0.22, entry_x=4.25)
    route_to_downstream(ax, phys[1][0], route_x=0.46, entry_x=5.25)
    ax.text(7.22, 0.30, "Resources are not pooled; similarly named proxies retain source-specific meaning.",
            ha="center", va="center", fontsize=SECONDARY_SIZE, color="#3F3F3F")

    fig.savefig(
        OUTPUT_PATH, format="pdf", metadata={
            "Creator": "CliniCause Figure 1 generation script",
            "Producer": "Matplotlib PDF backend",
            "CreationDate": None,
            "ModDate": None,
        },
    )
    plt.close(fig)


if __name__ == "__main__":
    main()


import argparse
import os
import pickle
import sys
from pathlib import Path

if "--validate-config-only" in sys.argv:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from dataset_config import maybe_run_validate_config_only

    maybe_run_validate_config_only(
        "src/mimiciii_causal_graph.py",
        fixed_dataset="mimic",
    )

import matplotlib.pyplot as plt
import networkx as nx


DEFAULT_GRAPH_PKL_PATH = "../data/mimiciii_causal_graph.pkl"
DEFAULT_GRAPH_PNG_PATH = "../data/mimiciii_causal_dag.png"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the MIMIC-III causal DAG and save the graph artifacts."
    )
    parser.add_argument(
        "--dataset-config-csv",
        default=None,
        help=(
            "Path to the dataset global-variables CSV. If omitted, use the default "
            "MIMIC config."
        ),
    )
    parser.add_argument(
        "--graph-pkl-path",
        default=None,
        help=f"Output path for the graph pickle. Default: {DEFAULT_GRAPH_PKL_PATH}",
    )
    parser.add_argument(
        "--graph-png-path",
        default=None,
        help=f"Output path for the rendered graph PNG. Default: {DEFAULT_GRAPH_PNG_PATH}",
    )
    parser.add_argument(
        "--validate-config-only",
        action="store_true",
        help="Resolve dataset config values and exit without creating graph outputs.",
    )
    return parser.parse_args()


def resolve_output_path(path_like: str) -> str:
    raw_path = path_like.strip()
    if not raw_path:
        raise ValueError("Output path must be a non-empty string.")
    return os.path.abspath(os.path.expanduser(raw_path))


def create_mimiciii_causal_graph(
    save=0,
    graph_pkl_path: str | None = None,
) -> nx.DiGraph:
    """
    Research-ready causal DAG for a clinically aggregated subset of MIMIC-III.
    This graph models background variables, latent physiologic states, observed
    vitals/labs/interventions, and mortality.

    Notes
    -----
    - This is not a DAG over all raw MIMIC-III ITEMIDs.
    - It is a compact causal abstraction over commonly used aggregated variables.
    - Edges encode clinically plausible causal directions for causal-inference work.
    """
    G = nx.DiGraph()

    # ------------------------------------------------------------------
    # Background variables from the approved latent causal DAG
    # ------------------------------------------------------------------
    background_vars = [
        "BG_AGE",
        "BG_SEX",
        "BG_ETHNICITY_INSURANCE_LANGUAGE",
        "BG_ADMISSION_CONTEXT",
        "BG_ICU_UNIT",
    ]

    # ------------------------------------------------------------------
    # Approved latent clinical-state variables from the causal DAG
    # ------------------------------------------------------------------
    latent_vars = [
        "LAT_CHRONIC_BURDEN",
        "LAT_INFLAMMATION_SEPSIS",
        "LAT_GLOBAL_SEVERITY",
        "LAT_CARDIAC_STRAIN",
        "LAT_SHOCK",
        "LAT_RESPIRATORY_FAILURE",
        "LAT_RENAL_DYSFUNCTION",
        "LAT_HEPATIC_COAG_DYSFUNCTION",
        "LAT_NEUROLOGIC_DYSFUNCTION",
        "LAT_METABOLIC_DERANGEMENT",
    ]

    # ------------------------------------------------------------------
    # Observed, treatment, outcome, and measurement-process nodes
    # ------------------------------------------------------------------
    observed_vars = [
        "OBS_BLOOD_PRESSURE",
        "OBS_LACTATE",
        "OBS_OXYGENATION",
        "OBS_VENTILATOR_SETTINGS",
        "OBS_CREATININE_BUN_URINE",
        "OBS_BILIRUBIN_PLATELETS_INR",
        "OBS_GCS_RASS",
        "OBS_PH_ELECTROLYTES_GLUCOSE",
        "OBS_TEMP_WBC_CULTURES",
        "OBS_TROPONIN_ECG",
        "OBS_CULTURES_MEDICATIONS",
        "OBS_CREATININE_BUN_ELECTROLYTES",
        "OBS_AVAILABILITY",
        "OBS_LAB_COUNTS",
        "OBS_VITAL_COUNTS",
        "TRT_ANTIBIOTICS",
        "TRT_VASOPRESSORS",
        "TRT_MECH_VENT",
        "TRT_DIALYSIS",
        "MISS_MEASUREMENT_INTENSITY",
        "OUT_MORTALITY",
    ]

    G.add_nodes_from(background_vars, node_type="background")
    G.add_nodes_from(latent_vars, node_type="latent")
    G.add_nodes_from(observed_vars, node_type="observed")

    # ------------------------------------------------------------------
    # Final DAG edges from the approved causal graph specification
    # ------------------------------------------------------------------
    edges = [
        ("BG_AGE", "LAT_CHRONIC_BURDEN"),
        ("BG_AGE", "OUT_MORTALITY"),
        ("BG_SEX", "LAT_CHRONIC_BURDEN"),
        ("BG_ETHNICITY_INSURANCE_LANGUAGE", "MISS_MEASUREMENT_INTENSITY"),
        ("BG_ETHNICITY_INSURANCE_LANGUAGE", "OUT_MORTALITY"),
        ("BG_ADMISSION_CONTEXT", "LAT_INFLAMMATION_SEPSIS"),
        ("BG_ADMISSION_CONTEXT", "LAT_GLOBAL_SEVERITY"),
        ("BG_ADMISSION_CONTEXT", "MISS_MEASUREMENT_INTENSITY"),
        ("BG_ICU_UNIT", "LAT_GLOBAL_SEVERITY"),
        ("BG_ICU_UNIT", "MISS_MEASUREMENT_INTENSITY"),

        ("LAT_CHRONIC_BURDEN", "LAT_GLOBAL_SEVERITY"),
        ("LAT_CHRONIC_BURDEN", "LAT_RENAL_DYSFUNCTION"),
        ("LAT_CHRONIC_BURDEN", "LAT_CARDIAC_STRAIN"),
        ("LAT_CHRONIC_BURDEN", "OUT_MORTALITY"),

        ("LAT_INFLAMMATION_SEPSIS", "LAT_GLOBAL_SEVERITY"),
        ("LAT_INFLAMMATION_SEPSIS", "LAT_SHOCK"),
        ("LAT_INFLAMMATION_SEPSIS", "LAT_HEPATIC_COAG_DYSFUNCTION"),
        ("LAT_INFLAMMATION_SEPSIS", "TRT_ANTIBIOTICS"),
        ("LAT_INFLAMMATION_SEPSIS", "OUT_MORTALITY"),

        ("LAT_GLOBAL_SEVERITY", "LAT_RESPIRATORY_FAILURE"),
        ("LAT_GLOBAL_SEVERITY", "LAT_NEUROLOGIC_DYSFUNCTION"),
        ("LAT_GLOBAL_SEVERITY", "LAT_METABOLIC_DERANGEMENT"),
        ("LAT_GLOBAL_SEVERITY", "MISS_MEASUREMENT_INTENSITY"),
        ("LAT_GLOBAL_SEVERITY", "OUT_MORTALITY"),

        ("LAT_CARDIAC_STRAIN", "LAT_SHOCK"),
        ("LAT_CARDIAC_STRAIN", "OUT_MORTALITY"),

        ("LAT_SHOCK", "LAT_RENAL_DYSFUNCTION"),
        ("LAT_SHOCK", "LAT_HEPATIC_COAG_DYSFUNCTION"),
        ("LAT_SHOCK", "LAT_METABOLIC_DERANGEMENT"),
        ("LAT_SHOCK", "TRT_VASOPRESSORS"),
        ("LAT_SHOCK", "OUT_MORTALITY"),

        ("LAT_RESPIRATORY_FAILURE", "LAT_METABOLIC_DERANGEMENT"),
        ("LAT_RESPIRATORY_FAILURE", "TRT_MECH_VENT"),
        ("LAT_RESPIRATORY_FAILURE", "OUT_MORTALITY"),

        ("LAT_RENAL_DYSFUNCTION", "LAT_METABOLIC_DERANGEMENT"),
        ("LAT_RENAL_DYSFUNCTION", "TRT_DIALYSIS"),
        ("LAT_RENAL_DYSFUNCTION", "OUT_MORTALITY"),

        ("LAT_HEPATIC_COAG_DYSFUNCTION", "OUT_MORTALITY"),
        ("LAT_NEUROLOGIC_DYSFUNCTION", "OUT_MORTALITY"),
        ("LAT_METABOLIC_DERANGEMENT", "OUT_MORTALITY"),

        ("LAT_SHOCK", "OBS_BLOOD_PRESSURE"),
        ("LAT_SHOCK", "OBS_LACTATE"),
        ("LAT_RESPIRATORY_FAILURE", "OBS_OXYGENATION"),
        ("LAT_RENAL_DYSFUNCTION", "OBS_CREATININE_BUN_URINE"),
        ("LAT_HEPATIC_COAG_DYSFUNCTION", "OBS_BILIRUBIN_PLATELETS_INR"),
        ("LAT_NEUROLOGIC_DYSFUNCTION", "OBS_GCS_RASS"),
        ("LAT_METABOLIC_DERANGEMENT", "OBS_PH_ELECTROLYTES_GLUCOSE"),
        ("LAT_INFLAMMATION_SEPSIS", "OBS_TEMP_WBC_CULTURES"),
        ("LAT_CARDIAC_STRAIN", "OBS_TROPONIN_ECG"),

        ("TRT_ANTIBIOTICS", "OBS_CULTURES_MEDICATIONS"),
        ("TRT_VASOPRESSORS", "OBS_BLOOD_PRESSURE"),
        ("TRT_MECH_VENT", "OBS_OXYGENATION"),
        ("TRT_MECH_VENT", "OBS_VENTILATOR_SETTINGS"),
        ("TRT_DIALYSIS", "OBS_CREATININE_BUN_ELECTROLYTES"),

        ("MISS_MEASUREMENT_INTENSITY", "OBS_AVAILABILITY"),
        ("MISS_MEASUREMENT_INTENSITY", "OBS_LAB_COUNTS"),
        ("MISS_MEASUREMENT_INTENSITY", "OBS_VITAL_COUNTS"),
    ]
    G.add_edges_from(edges)

    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Constructed graph is not a DAG")

    print(
        f"      Built MIMIC-III DAG with {G.number_of_nodes()} nodes and "
        f"{G.number_of_edges()} edges."
    )

    if save:
        output_path = resolve_output_path(graph_pkl_path or DEFAULT_GRAPH_PKL_PATH)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print(f"      Saving graph pickle to: {output_path}")
        with open(output_path, "wb") as f:
            pickle.dump(G, f)

    return G


def draw_graph(
    G: nx.DiGraph,
    save=0,
    graph_png_path: str | None = None,
    figsize=(24, 18),
    node_size=1500,
    font_size=8,
):
    color_map = {
        "background": "#9ecae1",
        "latent": "#fdae6b",
        "observed": "#a1d99b",
    }

    background_nodes = [n for n, d in G.nodes(data=True) if d.get("node_type") == "background"]
    latent_nodes = [n for n, d in G.nodes(data=True) if d.get("node_type") == "latent"]
    observed_nodes = [n for n, d in G.nodes(data=True) if d.get("node_type") == "observed"]

    pos = {}

    def assign_layer(nodes, y, x_spacing):
        x_offset = -(len(nodes) - 1) * x_spacing / 2
        for i, node in enumerate(nodes):
            pos[node] = (x_offset + i * x_spacing, y)

    assign_layer(background_nodes, y=3.1, x_spacing=2.0)
    assign_layer(latent_nodes, y=2.0, x_spacing=1.7)
    assign_layer(observed_nodes, y=0.9, x_spacing=0.8)

    plt.figure(figsize=figsize)

    nx.draw_networkx_edges(
        G,
        pos,
        arrowstyle="-|>",
        arrowsize=15,
        edge_color="gray",
        width=1.1,
        alpha=0.65,
        connectionstyle="arc3,rad=0.04",
        min_source_margin=10,
        min_target_margin=15,
    )

    for group, nodes in [
        ("background", background_nodes),
        ("latent", latent_nodes),
        ("observed", observed_nodes),
    ]:
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=nodes,
            node_color=color_map[group],
            node_size=node_size,
            edgecolors="black",
        )

    nx.draw_networkx_labels(G, pos, font_size=font_size)

    legend_handles = [
        plt.Line2D(
            [0], [0],
            marker="o",
            color="w",
            label=label,
            markerfacecolor=color,
            markeredgecolor="black",
            markersize=11,
        )
        for label, color in color_map.items()
    ]

    plt.legend(handles=legend_handles, loc="upper center", ncol=3, frameon=False)
    plt.title("MIMIC-III – Clinically Aggregated Causal DAG", fontsize=16)
    plt.axis("off")
    plt.tight_layout()

    if save:
        output_path = resolve_output_path(graph_png_path or DEFAULT_GRAPH_PNG_PATH)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print(f"      Saving DAG figure to: {output_path}")
        plt.savefig(output_path, dpi=220, bbox_inches="tight")
    else:
        plt.show()


if __name__ == "__main__":
    args = parse_args()
    graph_pkl_path = args.graph_pkl_path or DEFAULT_GRAPH_PKL_PATH
    graph_png_path = args.graph_png_path or DEFAULT_GRAPH_PNG_PATH
    print("=== Building MIMIC-III causal DAG ===")
    print("[1/2] Creating graph structure")
    g = create_mimiciii_causal_graph(
        save=1,
        graph_pkl_path=graph_pkl_path,
    )
    print("[2/2] Rendering graph figure")
    draw_graph(
        g,
        save=1,
        graph_png_path=graph_png_path,
    )
    print("MIMIC-III causal DAG build completed.")

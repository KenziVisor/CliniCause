# Thesis Figure Directory

Store thesis-local figure copies here only after a later stage approves the source artifact, caption, and provenance.

Do not copy assets from `thesis-writing/example-omri-thesis/`. The example thesis is formatting reference only.

Current planned source paths are tracked in `thesis-writing/planning/figure_plan.md`; chapter files contain `[FIGURE REQUIRED]` comments where later drafting may attach approved figures.

## Stage 4.4 Approved Thesis-Local Copies

| thesis file | figure id | source artifact | source SHA-256 | destination SHA-256 | inserted label | provenance status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `physionet_causal_dag.png` | F-DAG-PHY-01 | `final-results/causal-outputs/outputs-physionet-forest/graph/physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | `fig:physionet-causal-dag` | Verified duplicate graph artifact; active source matches graph pickle; exact producing command/commit still needs manifest. | Orientation figure for the project-specified DAG, not clinical validation. |
| `mimic_causal_dag.png` | F-DAG-MIMIC-01 | `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | `fig:mimic-causal-dag` | Verified duplicate graph artifact; active source matches graph pickle; exact producing command/commit still needs manifest. | Orientation figure for the project-specified DAG, not clinical validation; dense labels limit readability. |

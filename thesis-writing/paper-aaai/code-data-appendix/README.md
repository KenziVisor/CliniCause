# Anonymous code/data appendix preparation

This directory records the intended contents of a future anonymous review package. It is preparatory and release-neutral: it does not assert that code, data, or a public URL is currently available.

## Intended package layout

```text
code-data-package/
├── README.md
├── construction/                 # deterministic preprocessing, proxy, DAG, and assembly code
├── prediction/                   # STraTS and baseline training/export interfaces
├── causal-analysis/              # CATE, matching, diagnostic, and orchestration interfaces
├── configs-and-schemas/          # relative configuration, schema, DAG, and contract artifacts
├── checked-results/              # licensing-permitted aggregate paper inputs only
├── paper-artifacts/              # deterministic figure and supplement generators
└── manifests/                    # package inventory, checksums, and provenance notes
```

## Pipeline entry points

All paths below are relative to the repository root and must be revalidated before packaging.

- `causal-irregular-time-series/src/preprocess_physionet_2012.py` and `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`: source-specific preprocessing contracts.
- `causal-irregular-time-series/src/clinically_sufficient_tagging_latent_variables.py` and `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`: deterministic proxy-state construction.
- `causal-irregular-time-series/src/physionet2012_causal_graph.py`, `causal-irregular-time-series/src/mimiciii_causal_graph.py`, and `causal-irregular-time-series/src/cate_estimation.py`: DAG and causal-analysis interfaces.
- `causal-irregular-time-series/src/matching_causal_effect.py` and `causal-irregular-time-series/src/permutations_test.py`: matching and diagnostic interfaces.
- `STraTS/src/main.py`: STraTS/GRU/GRU-D/TCN training and prediction-export interface.
- `thesis-writing/paper-aaai/figures/generate_figure1_pipeline.py`, `thesis-writing/paper-aaai/figures/generate_figure2_estimator_agreement.py`, and `thesis-writing/paper-aaai/supplement/generate_supplement_tables.py`: paper-artifact generators.

## Source-data access and safe artifacts

MIMIC-III must be obtained through its applicable credentialed-access and data-use process. PhysioNet 2012 source material must be obtained under its applicable access and licensing terms. Do not include raw source records, processed patient-level tables, identifiers, credentials, or private paths in the review package.

Subject to source-data licenses and a final privacy review, safe candidate inclusions are source code, relative schemas, configuration templates, deterministic rule/DAG definitions, aggregate checked results used by the paper, aggregate manifests/checksums, and regeneration scripts. Inclusion decisions remain open until a license and package audit is complete.

## Checked aggregate inputs

The paper uses checked aggregate files under `thesis-writing/results/`, especially:

- `checked_cohort_candidates.csv`
- `checked_predictive_metrics.csv`
- `checked_cate_candidates.csv`
- `checked_matching_results.csv` and `checked_matching_failures.csv`
- `checked_sensitivity_candidates.csv` and `checked_permutation_candidates.csv`
- `results_source_packet.md`, `results_manifest.csv`, and `results_checksums.sha256`

These files support paper artifacts but do not close historical producing-lineage gaps.

## Regeneration commands

Run from the repository root:

```bash
MPLCONFIGDIR=/tmp/matplotlib-p8 python3 thesis-writing/paper-aaai/figures/generate_figure1_pipeline.py
MPLCONFIGDIR=/tmp/matplotlib-p8 python3 thesis-writing/paper-aaai/figures/generate_figure2_estimator_agreement.py
python3 thesis-writing/paper-aaai/supplement/generate_supplement_tables.py
cd thesis-writing/paper-aaai/supplement && latexmk -pdf -interaction=nonstopmode -halt-on-error technical_appendix.tex
cd thesis-writing/paper-aaai && env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The commands regenerate paper artifacts only; they do not run models or experiments.

## Known boundaries and release gates

Historical producing revisions/configurations, predictive split IDs, checkpoint-to-export linkage, raw/processed-data lineage, producing environments, and CausalPFN package/version alignment remain incomplete. Current repaired contracts must not be represented as the historical producer without lineage evidence. A release decision still requires package scoping, license compatibility, source-data access wording, a runtime validation plan, checksums, and an anonymity audit.

## Anonymity checklist

- Remove authors, institutions, usernames, repository-owner information, private URLs, server paths, tokens, and credentials.
- Use relative paths and neutral package names only.
- Inspect PDF and archive metadata, file names, documentation, scripts, manifests, and generated logs.
- Include no patient-level data or derived identifiers.
- Do not make “publicly available,” exact-reproduction, or current-test-pass claims until independently verified.

# Thesis Literature Corpus

This directory is the canonical literature corpus for the CliniCause thesis work on causal analysis of irregular clinical time-series data. It keeps the PDFs, BibTeX, metadata catalog, and checksums in one reproducible structure.

## Structure

```text
thesis-writing/literature/
├── README.md
├── papers/        # core PDF files only
├── optional/      # optional/background PDF files only
└── metadata/
    ├── references.bib
    ├── catalog.csv
    └── checksums.sha256
```

## Policy and Counts

Core papers are directly used to support the implemented pipeline, clinical proxy definitions, datasets, estimators, sensitivity workflow, weak supervision, or software tooling. Optional papers are retained because they are useful background, but they are not the primary citation for the implemented method.

- Core catalog entries: 38
- Optional catalog entries: 5
- Catalog entries with valid local PDFs: 41
- Missing PDFs: 2

See `metadata/catalog.csv` for the complete source-of-truth metadata and `metadata/references.bib` for citations.

## Topic Summary

The core corpus covers irregular clinical time-series models, datasets and benchmarks, clinical proxy phenotyping, causal identification and DAGs, DML and causal forests, overlap and sensitivity analysis, programmatic labeling and weak supervision, LLM clinical knowledge, LLM-assisted causal-graph construction, and software tooling.

Clinical tags in this project should be described as derived proxy states, proxy phenotypes, clinically inspired proxy labels, or weak clinical labels. They are not verified diagnoses and should not be described as formal latent variables unless a separate validation argument is made.

The E-value papers are retained as optional background. Cinelli-Hazlett and Chernozhukov et al. are the primary sensitivity references for the implemented robustness-value and omitted-variable-bias workflow.

The early InterpNet workshop paper is optional because the ICLR 2019 Interpolation-Prediction Networks paper is the canonical core citation. Marginal structural models are retained for longitudinal causal-inference background, but they are not the estimator implemented in the current point/binary exposure workflow.

The inspected prompt artifacts and author clarification establish that an LLM was used at design time to propose the proxy-variable ontology, dataset-specific causal DAGs, and decision-tree rules. Accepted proposals were subsequently encoded in deterministic project source code; the LLM was not a runtime estimator in the executed preprocessing, prediction, or causal-effect pipeline. The core corpus now includes literature on clinical knowledge encoded by LLMs and on LLM-derived soft priors for causal-graph construction, together with foundational data-programming and Snorkel references for programmatic labeling and weak supervision.

These references provide methodological context rather than project-specific validation. They do not establish that the LLM was a clinically validated medical expert, that it discovered the true causal graph, that the local DAGs or decision rules received clinical validation, or that the proxy states are diagnoses or ground-truth latent variables. Deterministic source code remains the authority for what was implemented, while `llm_methodology_candidate_additions.md` records the remaining reporting and validation gaps.

## Adding a Future Paper

Place the PDF in `papers/` for a core paper or `optional/` for background. Add exactly one BibTeX entry to `metadata/references.bib`, add exactly one row to `metadata/catalog.csv`, regenerate `metadata/checksums.sha256`, and rerun duplicate, path, and PDF validity checks. Do not add duplicate metadata files in the literature root.

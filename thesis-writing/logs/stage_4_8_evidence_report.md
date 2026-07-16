# Stage 4.8 Evidence Report — Chapter 1: Introduction

## 20.1 Git state

- Verified approved commit 12acb9a47f750c18c4152a9adfb3b548846dbed7 with subject step 4.7; its immediate predecessor is 94d91e8 step 4.6B repair.
- Branch: main. The initial worktree was dirty with pre-existing unrelated changes; none was reset, staged, committed, or discarded.
- Stage 4.8 changed chapters/01_introduction.tex, logs/unresolved_placeholders.md, logs/deferred_fixes.md, and this report. The final build regenerated thesis-writing/thesis/main.pdf.
- Later chapters, results artifacts, checked CSVs, bibliography, figures, code, configurations, planning, and audit files were not modified by this stage.

## 20.2 Baseline build

Ran latexmk -C, latexmk -xelatex main.tex, test -f main.pdf, and pdfinfo main.pdf from thesis-writing/thesis. The baseline succeeded at 101 pages. After Biber and subsequent XeLaTeX passes, citations and references resolved; existing layout warnings remained.

## 20.3 Files inspected

- Thesis: complete Chapters 1 and 3--12, with Chapters 3, 10, and 11 authoritative for questions, hierarchy, findings, and boundaries.
- Planning: story, outline, evidence map, citation/table/terminology plans, writing order, and Stage 4 prompt queue.
- Audit: claim ledger, evidence inventory, unresolved questions, and terminology map.
- Results: manifest, source packet, and decision register.
- Reports/tracking: Stage 4.6A, repair, 4.6B, figure repair, Stage 4.7, placeholders, and deferred fixes.
- Literature metadata: references.bib and catalog.csv.

## 20.4 Introduction structure

| Section | Approximate words | Purpose |
| --- | ---: | --- |
| Motivation: Irregular ICU Time-Series Analysis | 948 | Irregularity, informative measurement, proxy terminology, task distinction, and dataset context. |
| Thesis Gap and Objective | 710 | Integration gap, exact objective, sequence, LLM role, and scope. |
| Research Questions and Contributions | 954 | RQs, hierarchy, six-row contribution table, and bounded findings preview. |
| Thesis Organization | 172 | Logical roadmap for Chapters 2--12. |

The prose count excluding the table is approximately 2,508 words (2,668 including it).

## 20.5 Main research question

Chapter 1 states exactly: “How can irregular ICU time-series data be converted into clinically interpretable proxy-state representations and used, under explicit causal assumptions, to support DAG-guided adjusted effect estimation for in-hospital mortality?”

It matches Chapters 3 and 11. **Consistency: pass.**

## 20.6 Secondary questions

| Identifier | Chapter 1 / Chapter 11 correspondence | Status |
| --- | --- | --- |
| SRQ-1 | Data contracts / normalized links between causal and split-aware predictive artifacts. | pass |
| SRQ-2 | Rule-based proxy inputs / consistent pipeline use but no clinical validation. | pass |
| SRQ-3 | STraTS and baselines / leading family differs by dataset. | pass |
| SRQ-4 | Prediction normalization and aggregation / paired outputs and deterministic voting. | pass |
| SRQ-5 | DAG-selected adjustment sets / source-coded, assumption-conditional sets. | pass |
| SRQ-6 | Matching, CATE, sensitivity, and permutations / qualified triangulation. | pass |
| SRQ-7 | Construct, causal, support, model, provenance, and confounding limits / all findings bounded. | pass |

## 20.7 Contributions

| Contribution-table row | Supporting evidence | Boundary |
| --- | --- | --- |
| End-to-end framework | Chapters 3--9 and completed workflow | Retrospective research workflow, not clinical validation. |
| Shared proxy-state interface | Chapters 4--6 | Rule-derived proxies, not diagnoses or ground truth. |
| Cross-dataset predictive evaluation | Chapter 10 checked table | Dataset-specific rankings and qualified lineage. |
| DAG-guided multi-estimator analysis | Chapters 7 and 10 | DAG, intervention, overlap, and confounding assumptions remain unresolved. |
| Robustness and diagnostics | Chapters 8 and 10 | Do not confirm causal identification. |
| Evidence tracking/reproducibility | Results packet and Chapters 10--11 | Numerical traceability exceeds clean-checkout rerun reproducibility. |

## 20.8 Findings preview

| Chapter 1 statement | Value | Source and boundary |
| --- | ---: | --- |
| Predictive leaders | STraTS in MIMIC-III; GRU-D in PhysioNet | Chapter 10; four archived metrics, dataset-specific only. |
| Forest--Linear agreement | 19 of 19 original-cohort comparisons | Chapters 10--11; not causal confirmation or estimator equivalence. |
| All-three agreement | 18 of 19 original-cohort comparisons | Chapters 10--11; CausalPFN remains exploratory. |
| CausalPFN wording | Nearly every original-cohort comparison | Chapters 10--11; promising complement without a primary citation or complete DML diagnostics. |
| Downsampling wording | Separate robustness population | Chapters 9--11; no pooling with original cohorts. |

## 20.9 Citations

Inserted and verified bibliography keys:

- sun_2026_review_irregular_medical_timeseries and lipton_kale_wetzel_2016_missingness_rnns: irregularity/missingness context only.
- tipirneni2022strats and che2018grud: representation-method context only.
- banda_2018_electronic_phenotyping and ratner_et_al_2020_snorkel: phenotyping/weak-supervision context only.
- pearl_1995_causal_diagrams, hernan_robins_2016_target_trial, and hernan_taubman_2008_well_defined_interventions: causal and intervention-definition boundaries only.
- silva2012physionet and johnson2016mimiciii: dataset context only.
- chernozhukov2018dml, wager2018causalforest, and athey2019grf: method context only.
- smit_2023_causal_inference_icu_scoping_review and bica_2021_individualized_treatment_effects_ehr_ml: ICU observational-causal context only.

No CausalPFN citation was invented.

## 20.10 Terminology validation

- Proxy-language scan finds diagnosis, ground truth, and validated phenotype only in explicit statements of what proxy states are not.
- Causal-language scan finds no unqualified ATE, ATT, risk-ratio, superiority, significance, or clinical-recommendation claim.
- LLM language states that prompts supplied candidate design material only; no execution, learned DAG, or clinical validation role is claimed.
- Full-thesis InterpNet/interpnet scan returned no matches.

## 20.11 Placeholders and deferred fixes

- Removed four generic Chapter 1 draft placeholders and two generic supervisor-decision placeholders.
- Retained the thesis-wide supervisor, clinical-review, CausalPFN-citation, predictive-lineage, producer/archive-provenance, and ethics/governance gates in the tracking log.
- Added DF-4.8-001 through DF-4.8-003 for title/abstract alignment, whole-thesis editorial consistency, and final reader-facing visual/copy-edit review. Equivalent earlier issues were cross-referenced rather than duplicated.

## 20.12 Final build

Ran latexmk -C, latexmk -xelatex main.tex, test -f main.pdf, and pdfinfo main.pdf. The final build succeeded and produced thesis-writing/thesis/main.pdf with 107 pages.

Final scan: 0 unresolved citations/references, 0 duplicate labels, 0 Biber errors, and 0 fatal errors. It retains 99 overfull and 1,108 underfull box warnings, predominantly from existing narrow/long tables in later chapters; no warning prevented PDF generation.

## 20.13 Readiness

**READY WITH NON-BLOCKING WARNINGS**

Chapter 1 is complete, evidence-bounded, citation-valid, and builds successfully. Supervisor, clinical-review, provenance, CausalPFN-citation, ethics, title/abstract, and final whole-thesis consistency gates remain visible in the logs. They do not block the separately authorized Stage 4.9A, but they constrain final submission and stronger clinical or causal language.


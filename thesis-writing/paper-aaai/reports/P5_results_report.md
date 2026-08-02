# P5 Results Report

## Execution identity and repository baseline

| Field | Value |
|---|---|
| Stage | P5 -- Results Draft |
| Model | GPT-5.6 |
| Reasoning effort | High |
| Current HEAD before work | `b604d68fdf85aa278d80c3f8916c9fd1ef837bcc` (`AAAI p4`) |
| Branch | `main` |
| Last two commits inspected | `b604d68` (`AAAI p4`); `14337a2` (`AAAI P3`) |
| Accepted P4 commit | `b604d68fdf85aa278d80c3f8916c9fd1ef837bcc` |
| Accepted P3 content commit | `60504040c86721782e6fdf8a29971c8b1e0ab9e4` |
| Worktree before work | Modified `prompt.txt` only; protected, pre-existing user work with no overlap with P5 files |
| STraTS nested revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal nested revision | `379ed9b75107b52007957ba5908e507b719c9247` |

The mandatory status, branch, HEAD, recent-log, submodule, last-two-commit,
two-commit name-status, and accepted-P4 manuscript-diff inspections were
completed before editing. HEAD was exactly the accepted P4 commit. The P4 commit
changed the permitted manuscript/report/build artifacts plus tracked LaTeX
auxiliaries and the protected prompt; there were no post-P4 changes and no user
change overlapped a permitted P5 file.

The canonical operational plan was read completely. The complete current
`paper.tex`, `paper_evidence_map.md`, `aaai_structure_notes.md`,
`paper_build_report.md`, P3 report, and P4 report were inspected before editing.
The checked sources inspected were:

- `results_source_packet.md`, `results_decision_register.md`, result manifest,
  checksum record, and the checked cohort, predictive, CATE, matching,
  matching-failure, sensitivity, and permutation CSVs;
- reproducibility README and provenance-gap register;
- thesis Chapters 10 and 11; and
- the existing evidence-map numerical matrix and decision boundaries.

No patient-level values were accessed. No experiment, model, sensitivity,
permutation, or matching run was performed. Read-only arithmetic checks were
performed over checked aggregate CSV rows.

## Files changed

P5 changed or created only the permitted source/artifact paths below; compilation
also regenerated the pre-existing tracked LaTeX auxiliaries as explicitly
allowed by the user policy.

1. `thesis-writing/paper-aaai/paper.tex`
2. `thesis-writing/paper-aaai/paper.pdf`
3. `thesis-writing/paper-aaai/paper_build_report.md`
4. `thesis-writing/paper-aaai/paper_evidence_map.md`
5. `thesis-writing/paper-aaai/reports/P5_results_report.md`
6. `thesis-writing/paper-aaai/figures/figure2_estimator_agreement.pdf`
7. `thesis-writing/paper-aaai/figures/generate_figure2_estimator_agreement.py`

No Section 3 or Section 4 prose was revised. The only non-Results manuscript
addition is `\FloatBarrier` immediately before Section 6 so Table 2 and Figure 2
remain attached to Results rather than passing later placeholder sections.

## Section, table, and figure outcome

Section 5 now contains the required opening plus:

1. `Predictive Characterization`
2. `Effect Patterns and Estimator Agreement`
3. `Robustness and Cross-Dataset Findings`

It contains nine substantive paragraphs and approximately 533 prose words
excluding Table 2 and Figure 2 (713 words including headings, table text, and
captions under `detex`). Its measured layout is approximately 1.7 physical pages:
the prose occupies the remaining Results portion of page 4 and the full-width
table/figure occupy the top of page 5 before Section 6 begins on that page. This
is within the requested 1.45--1.75-page target to measurement precision.

Table 2 is a full-width, 9-point (`\small`) table with eight dataset--model rows
and 32 metric cells: loss, AUROC, AUPRC, and minRP. It uses no `\resizebox`.
Within each dataset, minimum loss and maximum AUROC/AUPRC/minRP are bolded. Its
numerical source is `checked_predictive_metrics.csv` filtered by
`selection_status == PRIMARY_MAIN_TEXT` (exactly eight rows). The caption states
that these are selected archived held-out point results and makes no uncertainty
or significance claim.

Figure 2 is a deterministic two-panel horizontal dot plot generated from
`checked_cate_candidates.csv`. The script explicitly selects original sampling
and the estimator-specific `PRIMARY_MAIN_TEXT`, `SECONDARY_MAIN_TEXT`, and
`EXPLORATORY_MAIN_TEXT` rows. It validates exactly 19 unique dataset--exposure
combinations, 9 MIMIC and 10 PhysioNet exposures, exactly three named estimators
per combination, and no duplicates or missing rows. It plots full-precision
values and orders each panel by decreasing CausalForestDML value. The output is
a vector PDF with embedded CID TrueType fonts and no Type 3 fonts. Creation and
modification dates are suppressed; two consecutive regenerations produced the
same SHA-256. The plotted matrix is the complete prespecified set, not a
favorable subset.

Separate inspection of Figure 2 at 200 dpi and inspection at its final embedded
size confirmed readable labels and legend, grayscale-safe marker-shape
differences, visible zero references, visible magnitude differences, a visible
PhysioNet-shock exception, and no clipping. Input and output SHA-256 values at
the final build are recorded in the build section below.

## Scientific result checks

- Primary CausalForestDML: all 9 MIMIC summaries are positive; 9 of 10 PhysioNet
  summaries are positive, with shock negative. The largest checked values are
  those stated in the manuscript and audited below.
- LinearDML: signs agree with CausalForestDML in 19/19 joined original-cohort
  comparisons.
- CausalPFN: all three estimators agree in 18/19 complete original-cohort
  comparisons. CausalPFN is a headline paragraph and full figure series, not a
  footnote. No unsupported CausalPFN methodological citation was added.
- PhysioNet shock: CausalForestDML and LinearDML are negative, CausalPFN is
  slightly positive, and matching is positive. It is retained as the sole
  three-estimator sign exception and is not called clinically protective.
- Matching: 8/9 MIMIC and 7/10 PhysioNet comparisons produced summaries, 15/19
  overall; 14/15 successful summaries share the primary direction. The 4 failed
  rows have no usable binary matching columns after preprocessing and are not
  interpreted as zero effects.
- Downsampling: 55/57 signs are preserved. The two explicit changes are
  PhysioNet LinearDML coagulation/hematologic dysfunction and PhysioNet
  CausalPFN shock. Downsampled magnitudes are not interpreted as original-
  population estimates.
- Sensitivity/permutation: the text reports nonuniform DML provenance/coverage,
  disruption-based permutation checks, and the lack of equivalent archived
  CausalPFN stages without enumerating unsupported diagnostic magnitudes.
- Cross-dataset: workflow portability is stated positively, while prediction
  leaders, effect rankings, proxy semantics, and at least one sign remain
  dataset specific and unpooled.

Citation keys used remain those already activated in Sections 3--4:
`johnson2016mimiciii`, `silva2012physionet`, `tipirneni2022strats`,
`cho2014gru`, `bai2018tcn`, `che2018grud`, `chernozhukov2018dml`,
`wager2018causalforest`, `athey2019grf`, and
`oprescu_et_al_2019_econml`. P5 activates no new citation.

The evidence map now records the P5 baseline, claims C56--C70, exact manuscript
locations, source files, full predicates, support status, local qualifications,
and Table 2/Figure 2 connections. Existing TODO gates are preserved.

## Numerical audit conventions

Every rendered P5 scientific number was traced to a checked source; no number
was copied from `prompt.txt` without verification. The audit covers the 32 Table
2 cells, all prose values/counts, all 57 plotted values, agreement denominators,
matching counts, downsampling counts, and named exceptions. Section/table/figure
ordinal numbers and automatic axis ticks are layout identifiers/scales rather
than reported scientific results; Figure 2's axis ranges and ticks are specified
in the generation script and were visually checked.

Abbreviations used in the audit:

- `CPM`: `thesis-writing/results/checked_predictive_metrics.csv`.
- `CCC`: `thesis-writing/results/checked_cate_candidates.csv`.
- `CCO`: `thesis-writing/results/checked_cohort_candidates.csv`.
- `CMR`: `thesis-writing/results/checked_matching_results.csv`.
- `CMF`: `thesis-writing/results/checked_matching_failures.csv`.
- `AWQ`: admissible with qualifications under the decision/source packet.
- `Q-P`: archived point metric against rule targets; no uncertainty,
  significance, or clinical-label-validity claim.
- `Q-C`: mean model-estimated CATE over the analyzed sample; not a risk ratio,
  odds ratio, treatment recommendation, or unqualified population ATE.
- `Q-D`: full-precision sign comparison only; no magnitude equality or causal
  identification claim.
- `Q-M`: descriptive matched-pair/support evidence; failures are not zero.
- `Q-S`: robustness population differs from original; no magnitude transport.

All decimal displays use nearest-value rounding to three decimals except the
matching value 0.010, also three decimals, and plotted values, which retain
binary floating-point/full CSV precision without display rounding.

### Context, prose, caption, and derived-count audit

| Audit ID | Manuscript location | Rendered value | Full-precision source value | Unit/scale | Dataset | Estimator/model | Exposure | Sampling | Source | Source row/selection predicate | Source status | Rounding | Cross-check | Qualification |
|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
| P5-C01 | Sec. 5 opening | 26,845 | 26845 | analysis records | MIMIC-III | all | all admitted | original | CCO | dataset=mimic; pipeline_stage=majority_vote; sampling_condition=original; count_value=26845 (three hash-identical estimator families) | AWQ | thousands separator | CCC original `model_n` | analysis records, not raw cohort |
| P5-C02 | Sec. 5 opening | 9 | 9 unique treatments | admitted exposures | MIMIC-III | all 3 | all | original | CCC | original main-text statuses; unique dataset/treatment | AWQ/execution-supported | exact integer | Evidence map N02 | no subset selection |
| P5-C03 | Sec. 5 opening | 7,993 | 7993 | analysis records | PhysioNet 2012 | all | all admitted | original | CCO | dataset=physionet; pipeline_stage=majority_vote; sampling_condition=original; count_value=7993 | AWQ | thousands separator | CCC original `model_n` | analysis records, not raw cohort |
| P5-C04 | Sec. 5 opening | 10 | 10 unique treatments | admitted exposures | PhysioNet 2012 | all 3 | all | original | CCC | original main-text statuses; unique dataset/treatment | AWQ/execution-supported | exact integer | Evidence map N02 | no subset selection |
| P5-C05 | Sec. 5.1 paragraph 1 | all 4 | 4 checked metrics | metrics led | MIMIC-III/PhysioNet | STraTS/GRU-D | -- | archived test | CPM | 8 PRIMARY_MAIN_TEXT rows; per-dataset min loss/max other metrics | AWQ/artifact-supported | exact integer | Table 2 | Q-P |
| P5-C06 | Sec. 5.1 paragraph 2 | 0.905 | 0.905411 | AUROC | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | P5-P02 | Q-P |
| P5-C07 | Sec. 5.1 paragraph 2 | 0.869 | 0.869417 | AUPRC | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | P5-P03 | Q-P |
| P5-C08 | Sec. 5.1 paragraph 2 | 0.918 | 0.918478 | AUROC | PhysioNet | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | P5-P26 | Q-P |
| P5-C09 | Sec. 5.1 paragraph 2 | 0.905 | 0.905105 | AUPRC | PhysioNet | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | P5-P27 | Q-P |
| P5-C10 | Sec. 5.1 paragraph 2 | all 4 | 4 checked metrics | metrics led | both | STraTS/GRU-D | -- | archived test | CPM | same as P5-C05 | AWQ/artifact-supported | exact integer | Table 2 | Q-P |
| P5-C11 | Sec. 5.2 paragraph 1 | all 9 | 9 positive of 9 | sign count | MIMIC-III | CausalForestDML | all | original | CCC | PRIMARY_MAIN_TEXT Forest rows, dataset=mimic; sign(mean_cate)>0 | AWQ/execution-supported | exact integer | Figure 2/P5-F01--F27 | Q-D |
| P5-C12 | Sec. 5.2 paragraph 1 | 9 of 10 | 9 positive of 10 | sign count | PhysioNet | CausalForestDML | all | original | CCC | PRIMARY_MAIN_TEXT Forest rows, dataset=physionet; sign(mean_cate)>0 | AWQ/execution-supported | exact integers | Figure 2/P5-F28--F57 | Q-D |
| P5-C13 | Sec. 5.2 paragraph 1 | 0.220 | 0.22035603834514436 | mean model-estimated CATE | MIMIC | CausalForestDML | LAT_CARDIAC_STRAIN | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F01 | Q-C |
| P5-C14 | Sec. 5.2 paragraph 1 | 0.161 | 0.16117863078031663 | mean model-estimated CATE | MIMIC | CausalForestDML | LAT_INFLAMMATION_SEPSIS | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F04 | Q-C |
| P5-C15 | Sec. 5.2 paragraph 1 | 0.120 | 0.1200268544489593 | mean model-estimated CATE | PhysioNet | CausalForestDML | LAT_RENAL_DYSFUNCTION | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F28 | Q-C |
| P5-C16 | Sec. 5.2 paragraph 1 | 0.112 | 0.1118307526053288 | mean model-estimated CATE | PhysioNet | CausalForestDML | LAT_CARDIAC_INJURY_STRAIN | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F31 | Q-C |
| P5-C17 | Sec. 5.2 paragraph 1 | 0.108 | 0.10798789990231876 | mean model-estimated CATE | PhysioNet | CausalForestDML | LAT_GLOBAL_SEVERITY | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F34 | Q-C |
| P5-C18 | Sec. 5.2 paragraph 1 | -0.014 | -0.013849200594340203 | mean model-estimated CATE | PhysioNet | CausalForestDML | LAT_SHOCK | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ/execution-supported | 3 decimals | P5-F55 | Q-C |
| P5-C19 | Sec. 5.2 paragraph 2 | 19 | 19 of 19 | joined direction count | both | Forest/Linear | all | original | CCC | join PRIMARY/SECONDARY rows on dataset/treatment; same sign | AWQ/execution-supported | exact integer | Figure 2 caption/P5-C25 | Q-D |
| P5-C20 | Sec. 5.2 paragraph 3 | 18 of 19 | 18 of 19 | joined direction count | both | all 3 | all | original | CCC | join all estimator-specific main-text rows; common sign | AWQ/execution-supported | exact integers | Figure 2 caption/P5-C26 | Q-D |
| P5-C21 | Sec. 5.2 paragraph 4 | -0.014 | -0.013849200594340203 | mean model-estimated CATE | PhysioNet | CausalForestDML | LAT_SHOCK | original | CCC | named PRIMARY_MAIN_TEXT row | AWQ | 3 decimals | P5-F55 | Q-C |
| P5-C22 | Sec. 5.2 paragraph 4 | -0.027 | -0.02694439466909599 | mean model-estimated CATE | PhysioNet | LinearDML | LAT_SHOCK | original | CCC | named SECONDARY_MAIN_TEXT row | AWQ | 3 decimals | P5-F56 | Q-C |
| P5-C23 | Sec. 5.2 paragraph 4 | 0.004 | 0.00412193359964432 | mean model-estimated CATE | PhysioNet | CausalPFN | LAT_SHOCK | original | CCC | named EXPLORATORY_MAIN_TEXT row | AWQ | 3 decimals | P5-F57 | Q-C |
| P5-C24 | Sec. 5.2 paragraph 4 | 0.010 | 0.010275380189066995 | descriptive matched-pair difference | PhysioNet | matching | LAT_SHOCK | original | CMR | dataset=physionet; treatment=LAT_SHOCK; original | AWQ | 3 decimals | thesis Ch. 10 matching | Q-M |
| P5-C25a | Figure 2 caption | 19 | 19 combinations | combination count | both | all 3 | all | original | CCC | complete estimator-specific main-text join | AWQ/execution-supported | exact integer | script validation | Q-D |
| P5-C25b | Figure 2 caption | 19/19 | 19 same DML signs of 19 | agreement | both | Forest/Linear | all | original | CCC | complete join and sign comparison | AWQ/execution-supported | exact integers | C63 | Q-D |
| P5-C26 | Figure 2 caption | 18/19 | 18 common signs of 19 | agreement | both | all 3 | all | original | CCC | complete three-estimator join/sign comparison | AWQ/execution-supported | exact integers | C64 and script validation | Q-D |
| P5-C27 | Sec. 5.3 paragraph 1 | 8 of 9 | 8 success/1 failure | matching availability | MIMIC | cross-run matching | all | original | CMR; CMF | all MIMIC original success/failure rows | AWQ | exact integers | thesis Ch. 10 matching | Q-M |
| P5-C28 | Sec. 5.3 paragraph 1 | 7 of 10 | 7 success/3 failures | matching availability | PhysioNet | cross-run matching | all | original | CMR; CMF | all PhysioNet original success/failure rows | AWQ | exact integers | thesis Ch. 10 matching | Q-M |
| P5-C29 | Sec. 5.3 paragraph 1 | 15 of 19 | 15 success/19 prespecified | matching availability | both | cross-run matching | all | original | CMR; CMF | all original success/failure rows | AWQ | exact integers | evidence C67 | Q-M |
| P5-C30 | Sec. 5.3 paragraph 1 | 4 | 4 failure rows | failure count | both | cross-run matching | four named rows | original | CMF | all original rows | AWQ | exact integer | thesis Ch. 10 matching | Q-M |
| P5-C31 | Sec. 5.3 paragraph 1 | 14 of 15 | 14 same signs/15 success | direction agreement | both | matching/Forest | successful rows | original | CMR; CCC | sign join original successes to PRIMARY_MAIN_TEXT Forest | AWQ | exact integers | evidence C67 | Q-M/Q-D |
| P5-C32 | Sec. 5.3 paragraph 2 | 55 of 57 | 55 same signs/57 joins | robustness agreement | both | all 3 | all | original vs outcome-downsampled | CCC | join original main-text to ROBUSTNESS_APPENDIX; sign compare | AWQ/execution-supported | exact integers | evidence C68 | Q-S |
| P5-C33 | Sec. 5.3 paragraph 2 | 2 | 2 sign flips | exception count | PhysioNet | LinearDML; CausalPFN | coagulation; shock | original vs outcome-downsampled | CCC | mismatching signs in the 57-row join | AWQ/execution-supported | exact integer | thesis Ch. 10 robustness | Q-S |
| P5-C34 | Sec. 5.3 paragraph 2 | one primary sign | 1 negative Forest row among 19 | cross-dataset sign difference | PhysioNet | CausalForestDML | LAT_SHOCK | original | CCC | PRIMARY_MAIN_TEXT Forest rows; dataset comparison | AWQ/execution-supported | exact integer | P5-F55 | Q-C/Q-D |

### Table 2 audit: all 32 metric cells

| Audit ID | Manuscript location | Rendered | Full precision | Unit/scale | Dataset | Model | Exposure | Sampling | Source | Predicate | Status | Rounding | Cross-check | Qualification |
|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
| P5-P01 | Table 2, MIMIC/STraTS/loss | 0.348 | 0.348136 | loss | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P02 | Table 2, MIMIC/STraTS/AUROC | 0.905 | 0.905411 | AUROC | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P03 | Table 2, MIMIC/STraTS/AUPRC | 0.869 | 0.869417 | AUPRC | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P04 | Table 2, MIMIC/STraTS/minRP | 0.795 | 0.795399 | minRP | MIMIC-III | STraTS | -- | archived test | CPM | dataset=mimic_iii; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P05 | Table 2, MIMIC/GRU/loss | 0.386 | 0.385757 | loss | MIMIC-III | GRU | -- | archived test | CPM | dataset=mimic_iii; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P06 | Table 2, MIMIC/GRU/AUROC | 0.881 | 0.881119 | AUROC | MIMIC-III | GRU | -- | archived test | CPM | dataset=mimic_iii; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P07 | Table 2, MIMIC/GRU/AUPRC | 0.840 | 0.839559 | AUPRC | MIMIC-III | GRU | -- | archived test | CPM | dataset=mimic_iii; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P08 | Table 2, MIMIC/GRU/minRP | 0.770 | 0.770421 | minRP | MIMIC-III | GRU | -- | archived test | CPM | dataset=mimic_iii; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P09 | Table 2, MIMIC/GRU-D/loss | 0.404 | 0.404448 | loss | MIMIC-III | GRU-D | -- | archived test | CPM | dataset=mimic_iii; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P10 | Table 2, MIMIC/GRU-D/AUROC | 0.884 | 0.884277 | AUROC | MIMIC-III | GRU-D | -- | archived test | CPM | dataset=mimic_iii; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P11 | Table 2, MIMIC/GRU-D/AUPRC | 0.841 | 0.841273 | AUPRC | MIMIC-III | GRU-D | -- | archived test | CPM | dataset=mimic_iii; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P12 | Table 2, MIMIC/GRU-D/minRP | 0.773 | 0.772533 | minRP | MIMIC-III | GRU-D | -- | archived test | CPM | dataset=mimic_iii; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P13 | Table 2, MIMIC/TCN/loss | 0.414 | 0.414456 | loss | MIMIC-III | TCN | -- | archived test | CPM | dataset=mimic_iii; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P14 | Table 2, MIMIC/TCN/AUROC | 0.867 | 0.866914 | AUROC | MIMIC-III | TCN | -- | archived test | CPM | dataset=mimic_iii; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P15 | Table 2, MIMIC/TCN/AUPRC | 0.823 | 0.822642 | AUPRC | MIMIC-III | TCN | -- | archived test | CPM | dataset=mimic_iii; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P16 | Table 2, MIMIC/TCN/minRP | 0.758 | 0.757798 | minRP | MIMIC-III | TCN | -- | archived test | CPM | dataset=mimic_iii; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P17 | Table 2, PhysioNet/STraTS/loss | 0.341 | 0.340692 | loss | PhysioNet 2012 | STraTS | -- | archived test | CPM | dataset=physionet_2012; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P18 | Table 2, PhysioNet/STraTS/AUROC | 0.915 | 0.914761 | AUROC | PhysioNet 2012 | STraTS | -- | archived test | CPM | dataset=physionet_2012; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P19 | Table 2, PhysioNet/STraTS/AUPRC | 0.877 | 0.877456 | AUPRC | PhysioNet 2012 | STraTS | -- | archived test | CPM | dataset=physionet_2012; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P20 | Table 2, PhysioNet/STraTS/minRP | 0.818 | 0.818228 | minRP | PhysioNet 2012 | STraTS | -- | archived test | CPM | dataset=physionet_2012; model=strats; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P21 | Table 2, PhysioNet/GRU/loss | 0.397 | 0.396819 | loss | PhysioNet 2012 | GRU | -- | archived test | CPM | dataset=physionet_2012; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P22 | Table 2, PhysioNet/GRU/AUROC | 0.915 | 0.914616 | AUROC | PhysioNet 2012 | GRU | -- | archived test | CPM | dataset=physionet_2012; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P23 | Table 2, PhysioNet/GRU/AUPRC | 0.897 | 0.897493 | AUPRC | PhysioNet 2012 | GRU | -- | archived test | CPM | dataset=physionet_2012; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P24 | Table 2, PhysioNet/GRU/minRP | 0.831 | 0.831044 | minRP | PhysioNet 2012 | GRU | -- | archived test | CPM | dataset=physionet_2012; model=gru; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P25 | Table 2, PhysioNet/GRU-D/loss | 0.331 | 0.330593 | loss | PhysioNet 2012 | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P26 | Table 2, PhysioNet/GRU-D/AUROC | 0.918 | 0.918478 | AUROC | PhysioNet 2012 | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P27 | Table 2, PhysioNet/GRU-D/AUPRC | 0.905 | 0.905105 | AUPRC | PhysioNet 2012 | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P28 | Table 2, PhysioNet/GRU-D/minRP | 0.835 | 0.834958 | minRP | PhysioNet 2012 | GRU-D | -- | archived test | CPM | dataset=physionet_2012; model=grud; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P29 | Table 2, PhysioNet/TCN/loss | 0.477 | 0.476513 | loss | PhysioNet 2012 | TCN | -- | archived test | CPM | dataset=physionet_2012; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P30 | Table 2, PhysioNet/TCN/AUROC | 0.899 | 0.899103 | AUROC | PhysioNet 2012 | TCN | -- | archived test | CPM | dataset=physionet_2012; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P31 | Table 2, PhysioNet/TCN/AUPRC | 0.875 | 0.875091 | AUPRC | PhysioNet 2012 | TCN | -- | archived test | CPM | dataset=physionet_2012; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |
| P5-P32 | Table 2, PhysioNet/TCN/minRP | 0.811 | 0.811184 | minRP | PhysioNet 2012 | TCN | -- | archived test | CPM | dataset=physionet_2012; model=tcn; PRIMARY_MAIN_TEXT | AWQ/artifact-supported | 3 decimals | Evidence map §3 | Q-P |

### Figure 2 audit: all 57 plotted values

All figure rows use the same unit (`mean model-estimated CATE`), sampling
condition (`original`), source (`CCC`), status (`AWQ/execution-supported`),
rounding rule (`none; full-precision float input`), cross-check (`evidence map
§3 CATE matrix`), and qualification (`Q-C`). These shared fields apply to every
row and, together with the row-specific fields below, provide the complete audit
record required for each plotted number.

| Audit ID | Location | Rendered value | Full precision | Dataset | Estimator | Exposure | Source row/selection predicate |
|---|---|---|---:|---|---|---|---|
| P5-F01 | Figure 2 marker | plotted full precision | 0.22035603834514436 | MIMIC | CausalForestDML | LAT_CARDIAC_STRAIN | dataset=mimic; treatment=LAT_CARDIAC_STRAIN; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F02 | Figure 2 marker | plotted full precision | 0.1876338252286513 | MIMIC | LinearDML | LAT_CARDIAC_STRAIN | dataset=mimic; treatment=LAT_CARDIAC_STRAIN; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F03 | Figure 2 marker | plotted full precision | 0.259327498577642 | MIMIC | CausalPFN | LAT_CARDIAC_STRAIN | dataset=mimic; treatment=LAT_CARDIAC_STRAIN; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F04 | Figure 2 marker | plotted full precision | 0.16117863078031663 | MIMIC | CausalForestDML | LAT_INFLAMMATION_SEPSIS | dataset=mimic; treatment=LAT_INFLAMMATION_SEPSIS; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F05 | Figure 2 marker | plotted full precision | 0.1613343714629977 | MIMIC | LinearDML | LAT_INFLAMMATION_SEPSIS | dataset=mimic; treatment=LAT_INFLAMMATION_SEPSIS; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F06 | Figure 2 marker | plotted full precision | 0.14854354851917861 | MIMIC | CausalPFN | LAT_INFLAMMATION_SEPSIS | dataset=mimic; treatment=LAT_INFLAMMATION_SEPSIS; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F07 | Figure 2 marker | plotted full precision | 0.09759849060449512 | MIMIC | CausalForestDML | LAT_HEPATIC_COAG_DYSFUNCTION | dataset=mimic; treatment=LAT_HEPATIC_COAG_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F08 | Figure 2 marker | plotted full precision | 0.08301684982922239 | MIMIC | LinearDML | LAT_HEPATIC_COAG_DYSFUNCTION | dataset=mimic; treatment=LAT_HEPATIC_COAG_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F09 | Figure 2 marker | plotted full precision | 0.0968462757091129 | MIMIC | CausalPFN | LAT_HEPATIC_COAG_DYSFUNCTION | dataset=mimic; treatment=LAT_HEPATIC_COAG_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F10 | Figure 2 marker | plotted full precision | 0.09129044441831921 | MIMIC | CausalForestDML | LAT_RENAL_DYSFUNCTION | dataset=mimic; treatment=LAT_RENAL_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F11 | Figure 2 marker | plotted full precision | 0.08859517453837928 | MIMIC | LinearDML | LAT_RENAL_DYSFUNCTION | dataset=mimic; treatment=LAT_RENAL_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F12 | Figure 2 marker | plotted full precision | 0.08697155012811061 | MIMIC | CausalPFN | LAT_RENAL_DYSFUNCTION | dataset=mimic; treatment=LAT_RENAL_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F13 | Figure 2 marker | plotted full precision | 0.06210061818008489 | MIMIC | CausalForestDML | LAT_GLOBAL_SEVERITY | dataset=mimic; treatment=LAT_GLOBAL_SEVERITY; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F14 | Figure 2 marker | plotted full precision | 0.08015308816889209 | MIMIC | LinearDML | LAT_GLOBAL_SEVERITY | dataset=mimic; treatment=LAT_GLOBAL_SEVERITY; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F15 | Figure 2 marker | plotted full precision | 0.07304968889618824 | MIMIC | CausalPFN | LAT_GLOBAL_SEVERITY | dataset=mimic; treatment=LAT_GLOBAL_SEVERITY; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F16 | Figure 2 marker | plotted full precision | 0.036133320420856 | MIMIC | CausalForestDML | LAT_RESPIRATORY_FAILURE | dataset=mimic; treatment=LAT_RESPIRATORY_FAILURE; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F17 | Figure 2 marker | plotted full precision | 0.03909791554254309 | MIMIC | LinearDML | LAT_RESPIRATORY_FAILURE | dataset=mimic; treatment=LAT_RESPIRATORY_FAILURE; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F18 | Figure 2 marker | plotted full precision | 0.04976550012196902 | MIMIC | CausalPFN | LAT_RESPIRATORY_FAILURE | dataset=mimic; treatment=LAT_RESPIRATORY_FAILURE; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F19 | Figure 2 marker | plotted full precision | 0.034252711518043336 | MIMIC | CausalForestDML | LAT_NEUROLOGIC_DYSFUNCTION | dataset=mimic; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F20 | Figure 2 marker | plotted full precision | 0.03154960397072449 | MIMIC | LinearDML | LAT_NEUROLOGIC_DYSFUNCTION | dataset=mimic; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F21 | Figure 2 marker | plotted full precision | 0.034993031034570465 | MIMIC | CausalPFN | LAT_NEUROLOGIC_DYSFUNCTION | dataset=mimic; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F22 | Figure 2 marker | plotted full precision | 0.020994326819048455 | MIMIC | CausalForestDML | LAT_SHOCK | dataset=mimic; treatment=LAT_SHOCK; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F23 | Figure 2 marker | plotted full precision | 0.021245787889811386 | MIMIC | LinearDML | LAT_SHOCK | dataset=mimic; treatment=LAT_SHOCK; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F24 | Figure 2 marker | plotted full precision | 0.031644985158239956 | MIMIC | CausalPFN | LAT_SHOCK | dataset=mimic; treatment=LAT_SHOCK; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F25 | Figure 2 marker | plotted full precision | 0.01974295345435545 | MIMIC | CausalForestDML | LAT_METABOLIC_DERANGEMENT | dataset=mimic; treatment=LAT_METABOLIC_DERANGEMENT; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F26 | Figure 2 marker | plotted full precision | 0.017989452868950796 | MIMIC | LinearDML | LAT_METABOLIC_DERANGEMENT | dataset=mimic; treatment=LAT_METABOLIC_DERANGEMENT; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F27 | Figure 2 marker | plotted full precision | 0.03132348239996354 | MIMIC | CausalPFN | LAT_METABOLIC_DERANGEMENT | dataset=mimic; treatment=LAT_METABOLIC_DERANGEMENT; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F28 | Figure 2 marker | plotted full precision | 0.1200268544489593 | PhysioNet | CausalForestDML | LAT_RENAL_DYSFUNCTION | dataset=physionet; treatment=LAT_RENAL_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F29 | Figure 2 marker | plotted full precision | 0.0906219401807068 | PhysioNet | LinearDML | LAT_RENAL_DYSFUNCTION | dataset=physionet; treatment=LAT_RENAL_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F30 | Figure 2 marker | plotted full precision | 0.11066853776658027 | PhysioNet | CausalPFN | LAT_RENAL_DYSFUNCTION | dataset=physionet; treatment=LAT_RENAL_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F31 | Figure 2 marker | plotted full precision | 0.1118307526053288 | PhysioNet | CausalForestDML | LAT_CARDIAC_INJURY_STRAIN | dataset=physionet; treatment=LAT_CARDIAC_INJURY_STRAIN; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F32 | Figure 2 marker | plotted full precision | 0.12203313682540579 | PhysioNet | LinearDML | LAT_CARDIAC_INJURY_STRAIN | dataset=physionet; treatment=LAT_CARDIAC_INJURY_STRAIN; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F33 | Figure 2 marker | plotted full precision | 0.11941345027314323 | PhysioNet | CausalPFN | LAT_CARDIAC_INJURY_STRAIN | dataset=physionet; treatment=LAT_CARDIAC_INJURY_STRAIN; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F34 | Figure 2 marker | plotted full precision | 0.10798789990231876 | PhysioNet | CausalForestDML | LAT_GLOBAL_SEVERITY | dataset=physionet; treatment=LAT_GLOBAL_SEVERITY; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F35 | Figure 2 marker | plotted full precision | 0.10674017610435634 | PhysioNet | LinearDML | LAT_GLOBAL_SEVERITY | dataset=physionet; treatment=LAT_GLOBAL_SEVERITY; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F36 | Figure 2 marker | plotted full precision | 0.10503878126970247 | PhysioNet | CausalPFN | LAT_GLOBAL_SEVERITY | dataset=physionet; treatment=LAT_GLOBAL_SEVERITY; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F37 | Figure 2 marker | plotted full precision | 0.09052704652421123 | PhysioNet | CausalForestDML | LAT_HEPATIC_DYSFUNCTION | dataset=physionet; treatment=LAT_HEPATIC_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F38 | Figure 2 marker | plotted full precision | 0.06018403931880851 | PhysioNet | LinearDML | LAT_HEPATIC_DYSFUNCTION | dataset=physionet; treatment=LAT_HEPATIC_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F39 | Figure 2 marker | plotted full precision | 0.10684272691739839 | PhysioNet | CausalPFN | LAT_HEPATIC_DYSFUNCTION | dataset=physionet; treatment=LAT_HEPATIC_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F40 | Figure 2 marker | plotted full precision | 0.08163578213590206 | PhysioNet | CausalForestDML | LAT_NEUROLOGIC_DYSFUNCTION | dataset=physionet; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F41 | Figure 2 marker | plotted full precision | 0.07572758184655413 | PhysioNet | LinearDML | LAT_NEUROLOGIC_DYSFUNCTION | dataset=physionet; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F42 | Figure 2 marker | plotted full precision | 0.07704883483275221 | PhysioNet | CausalPFN | LAT_NEUROLOGIC_DYSFUNCTION | dataset=physionet; treatment=LAT_NEUROLOGIC_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F43 | Figure 2 marker | plotted full precision | 0.07770406267721523 | PhysioNet | CausalForestDML | LAT_METABOLIC_DERANGEMENT | dataset=physionet; treatment=LAT_METABOLIC_DERANGEMENT; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F44 | Figure 2 marker | plotted full precision | 0.07973829165462494 | PhysioNet | LinearDML | LAT_METABOLIC_DERANGEMENT | dataset=physionet; treatment=LAT_METABOLIC_DERANGEMENT; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F45 | Figure 2 marker | plotted full precision | 0.0907344995137599 | PhysioNet | CausalPFN | LAT_METABOLIC_DERANGEMENT | dataset=physionet; treatment=LAT_METABOLIC_DERANGEMENT; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F46 | Figure 2 marker | plotted full precision | 0.07180004977331886 | PhysioNet | CausalForestDML | LAT_INFLAMMATION_SEPSIS_BURDEN | dataset=physionet; treatment=LAT_INFLAMMATION_SEPSIS_BURDEN; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F47 | Figure 2 marker | plotted full precision | 0.07087168486512074 | PhysioNet | LinearDML | LAT_INFLAMMATION_SEPSIS_BURDEN | dataset=physionet; treatment=LAT_INFLAMMATION_SEPSIS_BURDEN; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F48 | Figure 2 marker | plotted full precision | 0.0674804416051104 | PhysioNet | CausalPFN | LAT_INFLAMMATION_SEPSIS_BURDEN | dataset=physionet; treatment=LAT_INFLAMMATION_SEPSIS_BURDEN; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F49 | Figure 2 marker | plotted full precision | 0.06475009736198116 | PhysioNet | CausalForestDML | LAT_RESPIRATORY_FAILURE | dataset=physionet; treatment=LAT_RESPIRATORY_FAILURE; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F50 | Figure 2 marker | plotted full precision | 0.06266009635207058 | PhysioNet | LinearDML | LAT_RESPIRATORY_FAILURE | dataset=physionet; treatment=LAT_RESPIRATORY_FAILURE; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F51 | Figure 2 marker | plotted full precision | 0.06298443986654997 | PhysioNet | CausalPFN | LAT_RESPIRATORY_FAILURE | dataset=physionet; treatment=LAT_RESPIRATORY_FAILURE; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F52 | Figure 2 marker | plotted full precision | 0.01079355815492156 | PhysioNet | CausalForestDML | LAT_COAG_HEME_DYSFUNCTION | dataset=physionet; treatment=LAT_COAG_HEME_DYSFUNCTION; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F53 | Figure 2 marker | plotted full precision | 0.004135693132290908 | PhysioNet | LinearDML | LAT_COAG_HEME_DYSFUNCTION | dataset=physionet; treatment=LAT_COAG_HEME_DYSFUNCTION; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F54 | Figure 2 marker | plotted full precision | 0.025428398451365294 | PhysioNet | CausalPFN | LAT_COAG_HEME_DYSFUNCTION | dataset=physionet; treatment=LAT_COAG_HEME_DYSFUNCTION; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |
| P5-F55 | Figure 2 marker | plotted full precision | -0.013849200594340203 | PhysioNet | CausalForestDML | LAT_SHOCK | dataset=physionet; treatment=LAT_SHOCK; estimator=CausalForestDML; PRIMARY_MAIN_TEXT |
| P5-F56 | Figure 2 marker | plotted full precision | -0.02694439466909599 | PhysioNet | LinearDML | LAT_SHOCK | dataset=physionet; treatment=LAT_SHOCK; estimator=LinearDML; SECONDARY_MAIN_TEXT |
| P5-F57 | Figure 2 marker | plotted full precision | 0.00412193359964432 | PhysioNet | CausalPFN | LAT_SHOCK | dataset=physionet; treatment=LAT_SHOCK; estimator=CausalPFN; EXPLORATORY_MAIN_TEXT |

## Source conflicts, gates, and readiness boundaries

No authoritative numerical conflict was found. Every protected headline value
in the requested stage reconciled with the checked CSVs. The historical thesis
labels CausalPFN exploratory, while the operational plan requires prominent,
positive complementary positioning. P5 follows the authoritative paper plan:
the complete 18/19 result is prominent, while the smaller archived diagnostic
package remains a single local boundary.

Open items retained from earlier stages:

- `TODO-EVIDENCE G-EVD-01`: a verified primary CausalPFN reference remains
  absent. P5 adds no architecture, training, novelty, theory, or primary-source
  attribution, so this does not block the checked empirical result.
- `TODO-EVIDENCE G-EVD-02`: producing revisions/configurations and predictive
  split/checkpoint lineage remain incomplete; P5 reports checked archived
  outputs, not an exact rerun.
- `TODO-RUNTIME G-RUN-01/G-RUN-02`: no current test-pass or integrated-rerun
  claim is made.
- `TODO-RELEASE G-REL-01`: no public/release claim is made.
- `TODO-HUMAN G-HUM-01/G-HUM-02` and `TODO-AAAI G-AAAI-01` remain for later
  manuscript/submission stages.

## Build and validation

| Field | Result |
|---|---|
| Figure command | `env MPLCONFIGDIR=/tmp/clinicause-mpl python3 figures/generate_figure2_estimator_agreement.py` |
| Manuscript build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; citations and references resolved |
| PDF page count | 6 |
| PDF page size | 612 x 792 pt, US Letter |
| Layout | Official anonymous AAAI two-column submission layout |
| `paper.pdf` SHA-256 | `d5b4c8870224584069ff98e656a897ce8991529c0e564f4f7156b3737d955d41` |
| Figure PDF SHA-256 | `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423` |
| Figure script SHA-256 | `cd365937f326ee32e458e9c27fd1bc7b7b9db7c90251bf3e1ea302bb34c58c31` |
| Font validation | All manuscript fonts embedded/subset; Type 1 or CID TrueType; no Type 3 font |
| Anonymous block | Intact; rendered as anonymous submission; no identity added |

The final log has no undefined citation, undefined reference, multiply defined
label, missing file, horizontal overfull box, or fatal LaTeX warning. The known
33.21437 pt first-page overfull vertical-box diagnostic from P3/P4 persists; the
full-page inspection again shows no clipping, overlap, gutter/margin breach, or
readability defect. Underfull diagnostics are ordinary paragraph/table
justification plus a final-page column-balance diagnostic. They do not create a
visible defect.

All six pages were rendered at 120 dpi and inspected together, with Results
pages re-inspected at full resolution. Table 2 is legible and within the text
block. Figure 2 is legible at final size, preserves all 57 magnitudes, shows both
zero lines and the PhysioNet-shock sign split, and has no clipped label. No text
crosses a margin or gutter. Captions remain below their artifacts. The anonymous
author block, page-number suppression, and official two-column format remain
intact.

`git diff --check`, status, diff-stat, per-file diffs, allowed-path checks, and
protected-file hashes are run again after the final report/build-report edits.
Repository cleanup remains deferred by explicit user decision: tracked LaTeX
auxiliaries were not removed and `.gitignore` was not changed. No file was
staged, committed, pushed, reset, restored, reverted, or cleaned.

Every rendered P5 scientific number is mapped above to a checked repository
source. No favorable exposure or estimator subset was selected; all 19
original-cohort comparisons appear in Figure 2. CausalPFN is presented
prominently, no unsupported CausalPFN methodological citation was added,
matching failures are not interpreted as zero effects, no experiment or model
run was performed, and no commit or push was performed.

READY FOR STAGE P6 — RESULTS DRAFTED AND NUMERICALLY MAPPED

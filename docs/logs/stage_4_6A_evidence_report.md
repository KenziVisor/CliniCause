# Stage 4.6A Evidence Report

## Git State

- Verified approved commit: `7f5206a step 4.5`; parent is `a96d475 step 4.4S`.
- Parent branch: `main`. Initial worktree was already dirty outside the authorized scope; no reset, checkout, stage, commit, or push was performed.
- Causal nested repository: `main` at `417bb32`, with pre-existing modification to `src/preprocess_mimic_iii_large.py`. STraTS: `main` at `4d2a752`.
- `final-results/` is ignored/untracked (`.gitignore`), so its archived copies have partial provenance.

## Baseline and Final Build

- Command: `latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.
- Result: success; `thesis-writing/thesis/main.pdf`, 79 pages.
- Warnings: existing undefined-citation/reference and layout warnings were emitted; no fatal build error.

## Artifact Inventory

- Manifested source artifacts: 1369.
- Families: cate=587, graph=24, majority_vote_proxy=24, matching=308, mortality_prediction=24, permutation=24, predictive=94, proxy=9, run_summary=12, sensitivity=236, supporting_archive=27.
- SHA-256 was computed for every manifest source and every generated checked CSV/Markdown result file; no binary artifact was deserialized.

## Predictive Validation

- Eight completed final training summaries were parsed, with separate validation/test rows and paired-log numerical comparison.
- InterpNet is retained as `BLOCKED_MISSING_RESULT` for both datasets.
- Eight archived exports were schema checked; their split and checkpoint provenance remain unverified.

## Proxy Validation

- Existing MIMIC rule-based prevalence, co-occurrence, and unadjusted mortality-association tables were copied with provenance. PhysioNet counterpart tables remain explicitly missing and were not generated.
- Majority-vote duplicates are grouped in the manifest by SHA-256; voter composition is not inferred.

## Causal Run Matrix

| Dataset | Estimator | Sampling | Run | Overall | Stage statuses | Configuration |
|---|---|---|---|---|---|---|
| mimic | CausalForestDML | original | `outputs-mimic-forest` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| mimic | CausalForestDML | outcome-downsampled | `outputs-mimic-forest-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| mimic | LinearDML | original | `outputs-mimic-linear` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| mimic | LinearDML | outcome-downsampled | `outputs-mimic-linear-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| mimic | CausalPFN | original | `outputs-mimic-pfn` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=skipped; permutations_test=skipped | numbered config not archived |
| mimic | CausalPFN | outcome-downsampled | `outputs-mimic-pfn-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=skipped; permutations_test=skipped | numbered config not archived |
| physionet | CausalForestDML | original | `outputs-physionet-forest` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| physionet | CausalForestDML | outcome-downsampled | `outputs-physionet-forest-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| physionet | LinearDML | original | `outputs-physionet-linear` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| physionet | LinearDML | outcome-downsampled | `outputs-physionet-linear-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=success; permutations_test=success | numbered config not archived |
| physionet | CausalPFN | original | `outputs-physionet-pfn` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=skipped; permutations_test=skipped | numbered config not archived |
| physionet | CausalPFN | outcome-downsampled | `outputs-physionet-pfn-downsample` | success | graph=success; majority_vote=success; mortality_prediction=success; matching=success; cate_estimation=success; analyze_cate_results=skipped; permutations_test=skipped | numbered config not archived |

## Canonical and Conflict Audit

- Full per-run CATE summaries were selected over reduced manager summaries.
- Hash-equivalent copies are excluded from canonical use.
- `outputs-mimic-linear/cate_estimation/physionet_manager_global_summary.csv` is excluded as mislabeled.
- Exact numbered causal configs are referenced by run summaries but absent locally; they were not silently replaced by compact configs.

## Checked Table Inventory

| Path | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `thesis-writing/results/checked_cohort_candidates.csv` | 22 | 13 | `e8ca0a6d3290f4135f56e2ba07e69b70c9856e4d6442620f891860223a3a9210` |
| `thesis-writing/results/checked_proxy_prevalence.csv` | 10 | 12 | `6a7fcf2231bf97f98eab69ddc4252217f74f0e591854a737a1a922486969a8e3` |
| `thesis-writing/results/checked_proxy_cooccurrence.csv` | 82 | 12 | `9dc78a5fd04289808a6127d8b260deefc08ff11189888a3380de52e24788dd3b` |
| `thesis-writing/results/checked_proxy_mortality_association.csv` | 10 | 15 | `e9bf1000904c2ff0dbb0c076e44c2e9994fc47f47811874894aa2baf887bb3ab` |
| `thesis-writing/results/checked_predictive_metrics.csv` | 22 | 19 | `f2764315c8a97bcc5ea2611e45091f1d41aa5ea0a706bcbc3fec20f9c58f6119` |
| `thesis-writing/results/checked_predictive_exports.csv` | 10 | 17 | `95e8b132ecc7804897d6a298e0e0e41b2f19db3488782b1debd92eb3354ac9f7` |
| `thesis-writing/results/checked_mortality_prediction.csv` | 6 | 11 | `f33db389a446c7fea690fc0acb53249dc3de65631d62179772c3240badbbd496` |
| `thesis-writing/results/checked_matching_results.csv` | 30 | 20 | `c09958954b0ae1d74249b14ccb9d2d5de18887a703b81950836a5fcd7cc91988` |
| `thesis-writing/results/checked_matching_failures.csv` | 8 | 9 | `cc1438b8c3607a966d8e5660eb125e13978c3b07bc10b0264ed7f21802ce0b60` |
| `thesis-writing/results/checked_cate_candidates.csv` | 114 | 28 | `656cc09a777d6f7856d1b17082ab78b598a83b956960ddfae3230574a85028b3` |
| `thesis-writing/results/checked_heterogeneity_candidates.csv` | 190 | 15 | `470bfd1bca46fc3b5e4c8c5b0a75a6b7bbacb78dc6e4f9ff75b52bc4bd5e77c7` |
| `thesis-writing/results/checked_sensitivity_candidates.csv` | 80 | 26 | `5b9a71346e6d40cacd24d0be972c99340f43cccafe86ed5e3ae4955598878db2` |
| `thesis-writing/results/checked_permutation_candidates.csv` | 160 | 22 | `844ce3e6f75577ff8a661332b464905276eebf72b3736fa6ac1eb12af0095438` |
| `thesis-writing/results/checked_figure_candidates.csv` | 107 | 16 | `2c13b2a679955875471e084a4b04f6fc941a46c7c41c371653feaf3532241f17` |

## Source Packet and Decisions

- Source packet: `thesis-writing/results/results_source_packet.md`.
- Decision register: `thesis-writing/results/results_decision_register.md`; all 16 required decisions remain open.
- Nonbinding hierarchy: original population for population interpretation; an estimator with complete archived diagnostics only after human selection; PFN exploratory; diagnostics generally appendix candidates.

## Placeholders and Deferred Fixes

- No existing placeholder is resolved merely by this audit.
- New deferred issues: `DF-4.6A-001` through `DF-4.6A-006`, covering missing numbered configs, predictive split/checkpoint lineage, archive-copy/source-commit provenance, missing PhysioNet proxy tables, treatment-level diagnostic source/status, and result-hierarchy approval.

## Scope Validation

- No thesis chapter, research code, configuration, planning/audit file, source result artifact, or source figure was edited. The only thesis build output is `thesis-writing/thesis/main.pdf`.

## Readiness

READY FOR HUMAN RESULT-SELECTION DECISIONS

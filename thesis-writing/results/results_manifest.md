# Stage 4.6A Results Manifest

This manifest inventories archived sources only. `final-results/` is ignored/untracked, and recorded producing-machine paths are not treated as local sources.

## Scope

- Source artifacts inventoried: 1369
- Result-family counts: cate=587, graph=24, majority_vote_proxy=24, matching=308, mortality_prediction=24, permutation=24, predictive=94, proxy=9, run_summary=12, sensitivity=236, supporting_archive=27
- Predictive final summaries: 10 completed families (five models × two datasets); InterpNet has no final summary/export.
- Causal runs: 12 archived run summaries; numbered producing configs are referenced but absent locally.

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

## Canonical-source rule

Full per-run CATE summaries are the canonical CATE summaries. Reduced manager summaries are excluded; `physionet_manager_global_summary.csv` under the MIMIC LinearDML run is excluded as mislabeled. SHA-256-equivalent copies are grouped in `results_manifest.csv`.

## Readiness

READY FOR HUMAN RESULT-SELECTION DECISIONS

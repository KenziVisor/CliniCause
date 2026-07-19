# P8 figure, table, and appendix value checks

All checks use checked aggregate files only; no patient-level artifact was opened.

| Artifact | Marks/cells | Checked source and predicate | Display rule | Outcome |
| --- | ---: | --- | --- | --- |
| Table 1 | 2 resource rows | `checked_cohort_candidates.csv` plus original selected `checked_cate_candidates.csv`; MIMIC=26,845/9 and PhysioNet=7,993/10 | Integer counts | PASS |
| Table 2 | 32 | `checked_predictive_metrics.csv`; `metric_split=test`, `selection_status=PRIMARY_MAIN_TEXT` | Three decimals in main table; full precision retained in source | PASS: 8 rows x 4 metrics, leaders checked by loss-minimum and score-maximum direction |
| Figure 2 | 57 | `checked_cate_candidates.csv`; `sampling_condition=original`, estimator-specific main-text status | Full floating-point values passed to Matplotlib | PASS: 19 combinations, 9 MIMIC + 10 PhysioNet, 3 estimators each; no duplicate/missing mark |
| Original estimator appendix table | 57 | Same original Figure 2 predicate | Signed six decimals | PASS: 19 rows x 3 estimators; 18 all-three agreements, PhysioNet shock exception |
| Downsampling appendix table | 114 values | Original predicate joined exactly to `sampling_condition=outcome-downsampled`, `selection_status=ROBUSTNESS_APPENDIX` | Signed six decimals and sign state | PASS: 57 pairs, 55 preserved and 2 changed directions |
| Matching appendix table | 19 rows | `checked_matching_results.csv` original CausalForest supporting selection plus original `checked_matching_failures.csv` supporting appendix | Signed six-decimal successful effects; failures explicit | PASS: 15 successes + 4 failures; failures are never rendered as zero |
| Diagnostic coverage | aggregate availability | original supporting rows in `checked_sensitivity_candidates.csv` and `checked_permutation_candidates.csv` | Recorded status classes, not magnitudes | PASS: source/provenance classes retained; CausalPFN unavailable stages distinct |

The deterministic supplement generator validates every stated row count and aborts on missing or duplicate selections. It retains source precision internally and emits only documented display rounding. Figure 2 was regenerated twice with SHA-256 `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423`; Figure 1 was regenerated twice with SHA-256 `e194745a0e36e1edaba5ba2f8127680ef33e3aecebdd5b13e0c06afb2bda1e44`.

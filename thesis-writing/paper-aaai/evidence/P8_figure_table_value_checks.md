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

The deterministic supplement generator validates every stated row count and aborts on missing or duplicate selections. It retains source precision internally and emits only documented display rounding. Figure 2 was regenerated twice with SHA-256 `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423`; the current repaired Figure 1 was regenerated twice with SHA-256 `3c1c0c63e04dfdba9d7aada3245948f3de59add7e6eb2bd4db1ded99d814c836`.

## P8 Figure 1 narrow-repair checks

| Check | Result |
| --- | --- |
| Separate per-dataset exports | PASS: each MIMIC-III/PhysioNet lane has its own `Normalize exports` box. |
| Separate per-dataset aggregation | PASS: each lane has its own `5-source vote`; no arrow connects either vote to the other lane. |
| No pooling implication | PASS: each path ends in its own estimator-ready resource; only completed resources connect to the shared, explicitly separate-execution method interface. |
| Final-size readability | PASS: source primary labels are 10.0 pt, headings 10.2 pt, and gate/note labels 9.3 pt; at the 0.99-text-width embedding these remain approximately 9.5 pt, 9.7 pt, and 8.9 pt. |
| Vector/font check | PASS: the repaired PDF contains embedded CID TrueType fonts and no Type 3 font. |

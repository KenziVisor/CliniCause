# Stage 4.6B-R Results Source Packet

This packet carries the frozen hierarchy forward after the Stage 4.6B-R figure repair. Use the checked CSVs; do not use historical InterpNet references in audit or literature files.

## Frozen hierarchy and population boundary

- Primary original causal-analysis populations: MIMIC 26,845 records; PhysioNet 7,993 records; difference 18,852; MIMIC is approximately 3.36 times larger. These are original causal-analysis population counts, not raw cohort totals.
- Original and outcome-downsampled results must never be pooled. Downsampled material is robustness/supplementary only.
- CausalForestDML is primary, LinearDML secondary, and CausalPFN exploratory. Report every prespecified original-cohort proxy-state exposure.
- Use **descriptive matched-pair outcome difference** and **mean model-estimated CATE over the analyzed sample**. Do not use normalized CATE in Chapter 10.

## Approved Chapter 10 order

1. Analysis-population counts (`checked_cohort_candidates.csv`)
2. Predictive performance (`checked_predictive_metrics.csv`)
3. Primary CausalForestDML (`checked_cate_candidates.csv`)
4. Matching and empirical support (`checked_matching_results.csv`, `checked_matching_failures.csv`)
5. LinearDML comparison (`checked_cate_candidates.csv`)
6. CausalPFN exploratory results (`checked_cate_candidates.csv`)
7. Cross-dataset comparison (`checked_cate_candidates.csv`)
8. Robustness and sensitivity (`checked_sensitivity_candidates.csv`, `checked_permutation_candidates.csv`)

## Direction agreement

Original-cohort rows support 18 of 19 directionally concordant dataset--exposure comparisons (MIMIC 9/9; PhysioNet 9/10). PhysioNet `LAT_SHOCK` is the exception: CausalForestDML and LinearDML negative; CausalPFN slightly positive. This does not establish estimator equivalence, superiority, causal validity, or interchangeable uncertainty quantification. CausalPFN has no archived downstream sensitivity/permutation diagnostics.

## Figure gate

Use `figure_selection_register.md`. The two archived original-cohort ranking figures remain `BLOCKED_VALUE_CONFLICT` and `EXCLUDED_FROM_THESIS` because their labels are two-DML averages rather than the image-labelled median across all three estimators. The archived `cross_model_direction_counts.png` also remains blocked and excluded because it aggregates both sampling modes.

The three `SOURCE_EXACT_GENERATED` replacements are approved for `MAIN_RESULTS` use with qualifications: MIMIC and PhysioNet original-cohort CausalForestDML rankings, plus the original-cohort three-estimator direction count. They were generated only from `checked_cate_candidates.csv`; the agreement figure uses no outcome-downsampled row and reports 18/19 with PhysioNet shock as the sole exception. Appendix selections retain their stated diagnostic or illustrative boundaries.

## Persisting limitations

Missing numbered configs, ignored archive-copy history, missing producing commits, predictive split/checkpoint lineage, raw cohort totals, missing PhysioNet proxy tables, overlap diagnostics, proxy clinical validation, and LLM prompt-execution provenance remain open.

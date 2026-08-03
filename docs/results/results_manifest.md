# Stage 4.6B-R Results Manifest

The package inventories 1,353 archived result artifacts, 16 optional PNGs, three generated checked result figures, and one contextual seminar presentation. All have repository-relative paths and SHA-256 entries in `results_checksums.sha256`.

## Author decision freeze

**AUTHOR DECISION RECORDED; supervisor ratification remains pending.** Original cohorts are primary; outcome-downsampled analyses are robustness/supplementary only and are never pooled. CausalForestDML is primary, LinearDML secondary, and CausalPFN exploratory. Every prespecified original-cohort dataset-specific exposure is reported. Normalized CATE is omitted from Chapter 10.

## Predictive scope

The thesis predictive comparison contains exactly four learned models: STraTS, GRU, GRU-D, and TCN. The final aggregate contains their four predicted-label sources plus one Rule-Based Trees source.


## Direction agreement

Original-cohort checked CATE rows yield 18/19 concordant dataset--exposure comparisons: MIMIC 9/9 and PhysioNet 9/10. PhysioNet `LAT_SHOCK` is the exception (CausalForestDML and LinearDML negative; CausalPFN slightly positive). This is bounded directional agreement only; it does not establish equivalence, superiority, causal validity, or interchangeable uncertainty quantification.

## Optional figures

`figure_selection_register.md` retains the 16 optional PNGs and classifies the three generated replacements. The two archived ranking plots remain `BLOCKED_VALUE_CONFLICT` and `EXCLUDED_FROM_THESIS` because their displayed labels conflict with their stated three-estimator median scale. The archived `cross_model_direction_counts.png` remains blocked and excluded because it mixes sampling modes. Their source-exact replacements were generated from `checked_cate_candidates.csv`, selected as `MAIN_RESULTS`, and admitted with qualifications. The seminar PowerPoint is contextual provenance only, never numerical authority.

## Generated main-result figures

- `results_mimic_forest_original_cate_ranking.png`: exact MIMIC original-cohort CausalForestDML `PRIMARY_MAIN_TEXT` rows (9 rows), Chapter 10 primary-results placement.
- `results_physionet_forest_original_cate_ranking.png`: exact PhysioNet original-cohort CausalForestDML `PRIMARY_MAIN_TEXT` rows (10 rows), including negative shock, Chapter 10 primary-results placement.
- `results_original_three_estimator_direction_agreement.png`: 57 original-cohort estimator rows joined into 19 dataset--exposure comparisons; MIMIC 9/9, PhysioNet 9/10, overall 18/19, with PhysioNet shock the sole exception; Chapter 10 exploratory-PFN placement.

All three have artifact role `generated checked result figure`, validation `SOURCE_EXACT_GENERATED`, selection `MAIN_RESULTS`, and admission `ADMISSIBLE_WITH_QUALIFICATIONS`. They were produced by `generate_stage_4_6B_main_figures.py`; dimensions, hashes, filters, caption boundaries, and provenance notes are recorded in the CSV manifest and figure register.

## Readiness

**READY FOR STAGE 4.7.** The figure-source blocker is repaired: all three replacements passed source-exact numerical validation, Chapter 10 contains exactly those three generated figures, the eight validated table environments are unchanged, and the clean 90-page thesis build and rendered-page inspection passed. Supervisor ratification of the results hierarchy remains pending but is non-blocking for drafting Stage 4.7.

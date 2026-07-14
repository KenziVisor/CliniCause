# Stage 4.6A-R Results Manifest

The package inventories 1,369 archived result artifacts plus the 16 optional PNGs and one contextual seminar presentation. All have repository-relative paths and SHA-256 entries in `results_checksums.sha256`.

## Author decision freeze

**AUTHOR DECISION RECORDED; supervisor ratification remains pending.** Original cohorts are primary; outcome-downsampled analyses are robustness/supplementary only and are never pooled. CausalForestDML is primary, LinearDML secondary, and CausalPFN exploratory. Every prespecified original-cohort dataset-specific exposure is reported. Normalized CATE is omitted from Chapter 10.

## Predictive scope

The thesis predictive comparison contains exactly STraTS, GRU, GRU-D, TCN, and SAnD. **InterpNet is not part of the thesis pipeline and is excluded from the thesis.** Historical audit/literature records are not source-packet instructions.

## Direction agreement

Original-cohort checked CATE rows yield 18/19 concordant dataset--exposure comparisons: MIMIC 9/9 and PhysioNet 9/10. PhysioNet `LAT_SHOCK` is the exception (CausalForestDML and LinearDML negative; CausalPFN slightly positive). This is bounded directional agreement only; it does not establish equivalence, superiority, causal validity, or interchangeable uncertainty quantification.

## Optional figures

`figure_selection_register.md` classifies all 16 PNGs. Both original-cohort ranking figures are blocked because their labels conflict with their stated three-estimator median scale. `cross_model_direction_counts.png` is blocked because it mixes sampling modes; no replacement was generated. The seminar PowerPoint is contextual provenance only, never numerical authority.

## Readiness

BLOCKED: ALL THREE AUTHOR-SELECTED MAIN NUMERICAL FIGURES HAVE SOURCE-VALUE OR SAMPLING CONFLICTS. SUPERVISOR RATIFICATION OF THE RESULTS HIERARCHY REMAINS PENDING.

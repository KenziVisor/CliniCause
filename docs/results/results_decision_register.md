# Stage 4.6A-R Results Decision Register

## Decision freeze

**AUTHOR DECISION RECORDED.** Supervisor ratification remains pending. These choices were not made from effect magnitude, direction, apparent significance, estimator agreement, or post-hoc clinical interest.

- Primary population: original causal-analysis cohorts. Outcome-downsampled analyses are robustness/sensitivity material only, belong in supplementary material, and are never pooled with original analyses.
- Estimator hierarchy: CausalForestDML primary; LinearDML secondary; CausalPFN exploratory and included after LinearDML.
- Exposure policy: report every prespecified dataset-specific proxy-state exposure from original-cohort runs.
- Required wording: **descriptive matched-pair outcome difference** and **mean model-estimated CATE over the analyzed sample**. Omit normalized CATE from Chapter 10.
- Cross-dataset policy: qualitative/aligned-concept comparison only; no pooling. Original causal-analysis populations are MIMIC 26,845 and PhysioNet 7,993 records (difference 18,852; MIMIC approximately 3.36 times larger). These are not raw cohort totals.

## Frozen Chapter 10 order

1. Analysis-population counts
2. Predictive performance
3. Primary CausalForestDML results
4. Matching and empirical support
5. LinearDML comparison
6. CausalPFN exploratory results
7. Cross-dataset comparison
8. Robustness and sensitivity

Downsampling is addressed only within the final robustness section.

## Estimator agreement

The three estimators agree in mean-effect direction for 18 of 19 dataset--exposure comparisons: MIMIC 9 of 9 and PhysioNet 9 of 10. The exception is PhysioNet `LAT_SHOCK`: CausalForestDML and LinearDML are negative and CausalPFN is slightly positive.

CausalPFN reproduced the prevailing direction in nearly every comparison, supporting its promise as a complementary estimator within this pipeline. This broad agreement is not complete agreement and does not establish estimator equivalence, superiority, causal validity, or interchangeable uncertainty quantification. CausalPFN lacks the archived downstream sensitivity and permutation diagnostics available for the DML estimators.

## InterpNet

**NOT PART OF THE THESIS PIPELINE — EXCLUDED FROM THESIS.** Stage 4.6B must ignore historical audit and literature references to InterpNet.

## Former decision records

DEC-RESULT-001 through DEC-RESULT-016 are superseded by this author decision freeze where applicable; their evidence limitations remain in the manifest, source packet, and deferred-fix register.

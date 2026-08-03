# Stage 4.6A-R Repair Report

## Repository verification

- Verified `da200b7 adding figures` with parent `b4b1212 step 4.6A`.
- Confirmed the Stage 4.6A checked package exists, `thesis-writing/figures-options/` contains 16 PNGs, Chapter 10 remains undrafted, and the prior decision-freeze had not been applied.

## Author decisions recorded

- Original population primary; outcome-downsampled analyses robustness/supplementary only.
- CausalForestDML primary; LinearDML secondary; CausalPFN exploratory.
- All prespecified original-cohort exposures retained; no post-hoc exposure selection.
- Approved effect wording and normalized-CATE omission recorded.
- Cross-dataset comparison is qualitative/aligned only. Original causal-analysis populations: MIMIC 26,845; PhysioNet 7,993; difference 18,852; MIMIC approximately 3.36 times larger.

## CATE direction validation

- Directly reproduced original-cohort concordance: 18/19 overall, MIMIC 9/9, PhysioNet 9/10.
- PhysioNet `LAT_SHOCK` is the exception: CausalForestDML and LinearDML negative; CausalPFN slightly positive.
- CausalPFN remains exploratory, not failed; its missing archived downstream sensitivity/permutation diagnostics remain explicit.

## InterpNet removal


## Figure audit

- Inspected and hashed all 16 optional PNGs; see `figure_selection_register.md`.
- Both original-cohort ranking figures are `BLOCKED_VALUE_CONFLICT`: their labels equal two-DML averages rather than their stated three-estimator median scale, although all prespecified exposures are present.
- `cross_model_direction_counts.png` is `BLOCKED_VALUE_CONFLICT`: it visibly aggregates original and downsampled rows and does not support the required 18-of-19 original-cohort statement. No blocked figure was altered or replaced.

## Checked-table and checksum validation

- Added selection-status metadata only; no existing numerical field, source path/hash, row count, or row order was changed.
- Updated manifest/checksum coverage for the 16 PNGs and contextual seminar presentation.

## Build

- Ran `latexmk -C && latexmk -xelatex main.tex`; `main.pdf` was produced successfully (79 A4 pages). Existing citation and layout warnings remain non-blocking and are not treated as new evidence.

## Readiness

BLOCKED: ALL THREE AUTHOR-SELECTED MAIN NUMERICAL FIGURES HAVE SOURCE-VALUE OR SAMPLING CONFLICTS.

SUPERVISOR RATIFICATION OF THE RESULTS HIERARCHY REMAINS PENDING.

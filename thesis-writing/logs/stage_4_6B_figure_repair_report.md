# Stage 4.6B-R Figure Repair Evidence Report

## 1. Commit and worktree

- Verified commit: `fb40839 step 4.6B`.
- Verified parent: `5e6477a step 4.6A repair`.
- Branch: `main`.
- The verified Stage 4.6B thesis had eight major Chapter 10 result sections, an 87-page PDF, no inserted main-result figure, no InterpNet occurrence, and readiness blocked only by the three figure conflicts.
- No reset, clean, checkout, staging, amend, commit, or push was performed. `latexmk -C` and the final auxiliary-file cleanup affected only generated build products; `main.pdf` was retained.

The initial worktree was already dirty. Its recorded status comprised the following pre-existing paths:

```text
M README.md
M SCRIPTS.md
m causal-irregular-time-series
M fix_preprocessor.py
M prompt.txt
M requirements-full.txt
M requirements-router.txt
M requirements.txt
M router.py
M runs/validate_demo/config/physionet_resolved_config.csv
M tests/test_router.py
M thesis-writing/important-md-copies/clinicause_root_project_overview.md
M thesis-writing/important-md-copies/clinicause_root_router_usage.md
M thesis-writing/important-md-copies/strats_project_overview.md
M thesis-writing/literature/metadata/catalog.csv
M thesis-writing/results/checked_cate_candidates.csv
M thesis-writing/results/checked_cohort_candidates.csv
M thesis-writing/results/checked_figure_candidates.csv
M thesis-writing/results/checked_heterogeneity_candidates.csv
M thesis-writing/results/checked_matching_failures.csv
M thesis-writing/results/checked_matching_results.csv
M thesis-writing/results/checked_mortality_prediction.csv
M thesis-writing/results/checked_permutation_candidates.csv
M thesis-writing/results/checked_predictive_exports.csv
M thesis-writing/results/checked_predictive_metrics.csv
M thesis-writing/results/checked_proxy_cooccurrence.csv
M thesis-writing/results/checked_proxy_mortality_association.csv
M thesis-writing/results/checked_proxy_prevalence.csv
M thesis-writing/results/checked_sensitivity_candidates.csv
M thesis-writing/results/results_manifest.csv
M tmp_verify_router.py
```

The checked numerical CSV modifications above were pre-existing line-ending-only changes. A semantic CSV comparison against `HEAD` passed for every numerical `checked_*.csv`; `checked_figure_candidates.csv` is the sole intentionally edited checked register. The final worktree retains every pre-existing path and adds only the authorized repair paths listed below. Build auxiliaries were removed after validation.

Repair-created or repair-edited files:

```text
thesis-writing/results/generate_stage_4_6B_main_figures.py
thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png
thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png
thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png
thesis-writing/thesis/chapters/10_results.tex
thesis-writing/results/figure_selection_register.md
thesis-writing/results/checked_figure_candidates.csv
thesis-writing/results/results_manifest.csv
thesis-writing/results/results_manifest.md
thesis-writing/results/results_source_packet.md
thesis-writing/results/results_checksums.sha256
thesis-writing/logs/unresolved_placeholders.md
thesis-writing/logs/deferred_fixes.md
thesis-writing/logs/stage_4_6B_figure_repair_report.md
thesis-writing/thesis/main.pdf
```

## 2. Blocking issue

The archived MIMIC and PhysioNet ranking PNGs contain displayed values equal to a two-DML average while their labels describe a different three-estimator aggregation. They therefore cannot support the approved primary CausalForestDML tables. The archived direction-count PNG combines original and outcome-downsampled analyses, whereas the approved 18-of-19 statement is an original-cohort comparison only.

The three original PNGs were not read as numerical sources, modified, overwritten, renamed, or deleted. They remain excluded provenance with their original hashes:

| Archived figure | SHA-256 | Status |
|---|---|---|
| `mimic_non_downsampled_cate_ranking.png` | `e54ad1cf1d268135def7312f69065b49221a505d04d885720eb2d984e8e0428a` | `BLOCKED_VALUE_CONFLICT`; `EXCLUDED_FROM_THESIS` |
| `physionet_non_downsampled_cate_ranking.png` | `890db4d998ca1c4d8fe8b31024291f508ab01c5a418db280a3c1ebf793bfdf2c` | `BLOCKED_VALUE_CONFLICT`; `EXCLUDED_FROM_THESIS` |
| `cross_model_direction_counts.png` | `3fe798a320b6c96f1c106f0b81b4d856aef902976c84f10df40a30a4947ba32b` | `BLOCKED_VALUE_CONFLICT`; `EXCLUDED_FROM_THESIS` |

## 3. Generation script

- Script: `thesis-writing/results/generate_stage_4_6B_main_figures.py`.
- Sole numerical input: `thesis-writing/results/checked_cate_candidates.csv`.
- Frozen input SHA-256 before and after: `594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835`.
- Required columns: `dataset`, `estimator`, `sampling_condition`, `treatment`, `mean_cate`, and `selection_status`.
- Duplicate key: `(dataset, estimator, sampling_condition, treatment)`; any duplicate exits nonzero.
- Missing, non-numeric, or non-finite plotted `mean_cate` values exit nonzero.
- Ranking filters are exact and include `selection_status=PRIMARY_MAIN_TEXT`; agreement uses only `sampling_condition=original` and the three named estimators.
- Matplotlib uses a fixed backend, fixed dimensions, fixed typography/colors, stable sorting, fixed resolution, and deterministic metadata. Two consecutive runs produced identical hashes.
- The script prints every selected ranking row, all 19 joined direction comparisons, derived counts, output paths, and `VALIDATION PASS`.
- No numerical value is embedded in the plotting code and no normalized-CATE field is read.

## 4. MIMIC ranking figure

Filter: `dataset=mimic`, `estimator=CausalForestDML`, `sampling_condition=original`, `selection_status=PRIMARY_MAIN_TEXT`.

| Rank | Display label / exact identifier | Exact mean CATE | Display |
|---:|---|---:|---:|
| 1 | Cardiac Strain (`LAT_CARDIAC_STRAIN`) | 0.22035603834514436 | 0.220 |
| 2 | Inflammation Sepsis (`LAT_INFLAMMATION_SEPSIS`) | 0.16117863078031663 | 0.161 |
| 3 | Hepatic Coag Dysfunction (`LAT_HEPATIC_COAG_DYSFUNCTION`) | 0.09759849060449512 | 0.098 |
| 4 | Renal Dysfunction (`LAT_RENAL_DYSFUNCTION`) | 0.09129044441831921 | 0.091 |
| 5 | Global Severity (`LAT_GLOBAL_SEVERITY`) | 0.06210061818008489 | 0.062 |
| 6 | Respiratory Failure (`LAT_RESPIRATORY_FAILURE`) | 0.036133320420856 | 0.036 |
| 7 | Neurologic Dysfunction (`LAT_NEUROLOGIC_DYSFUNCTION`) | 0.034252711518043336 | 0.034 |
| 8 | Shock (`LAT_SHOCK`) | 0.020994326819048455 | 0.021 |
| 9 | Metabolic Derangement (`LAT_METABOLIC_DERANGEMENT`) | 0.01974295345435545 | 0.020 |

- Validation: exactly 9 rows, 9 unique exposures, 9 bars, exact descending source order, exact means before three-decimal display rounding, no interval or normalized-CATE use.
- Output: `thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png`.
- Dimensions: 3360 x 2220; file size: 271,094 bytes.
- SHA-256: `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969`.
- Chapter label: `fig:results-mimic-forest-ranking`.

## 5. PhysioNet ranking figure

Filter: `dataset=physionet`, `estimator=CausalForestDML`, `sampling_condition=original`, `selection_status=PRIMARY_MAIN_TEXT`.

| Rank | Display label / exact identifier | Exact mean CATE | Display |
|---:|---|---:|---:|
| 1 | Renal Dysfunction (`LAT_RENAL_DYSFUNCTION`) | 0.1200268544489593 | 0.120 |
| 2 | Cardiac Injury Strain (`LAT_CARDIAC_INJURY_STRAIN`) | 0.1118307526053288 | 0.112 |
| 3 | Global Severity (`LAT_GLOBAL_SEVERITY`) | 0.10798789990231876 | 0.108 |
| 4 | Hepatic Dysfunction (`LAT_HEPATIC_DYSFUNCTION`) | 0.09052704652421123 | 0.091 |
| 5 | Neurologic Dysfunction (`LAT_NEUROLOGIC_DYSFUNCTION`) | 0.08163578213590206 | 0.082 |
| 6 | Metabolic Derangement (`LAT_METABOLIC_DERANGEMENT`) | 0.07770406267721523 | 0.078 |
| 7 | Inflammation Sepsis Burden (`LAT_INFLAMMATION_SEPSIS_BURDEN`) | 0.07180004977331886 | 0.072 |
| 8 | Respiratory Failure (`LAT_RESPIRATORY_FAILURE`) | 0.06475009736198116 | 0.065 |
| 9 | Coag Heme Dysfunction (`LAT_COAG_HEME_DYSFUNCTION`) | 0.01079355815492156 | 0.011 |
| 10 | Shock (`LAT_SHOCK`) | -0.013849200594340203 | -0.014 |

- Validation: exactly 10 rows, 10 unique exposures, 10 bars, exact descending source order, exact means before display rounding, and negative shock retained to the left of zero.
- Output: `thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png`.
- Dimensions: 3360 x 2430; file size: 318,483 bytes.
- SHA-256: `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87`.
- Chapter label: `fig:results-physionet-forest-ranking`.

## 6. Direction-agreement figure

The figure uses 57 exact original-cohort rows joined into 19 dataset--exposure comparisons, requiring one row per estimator for every pair.

| Dataset | Exposure | Forest exact | Linear exact | PFN exact | All three concordant |
|---|---|---:|---:|---:|---|
| mimic | `LAT_CARDIAC_STRAIN` | 0.22035603834514436 | 0.1876338252286513 | 0.259327498577642 | yes |
| mimic | `LAT_GLOBAL_SEVERITY` | 0.06210061818008489 | 0.08015308816889209 | 0.07304968889618824 | yes |
| mimic | `LAT_HEPATIC_COAG_DYSFUNCTION` | 0.09759849060449512 | 0.08301684982922239 | 0.0968462757091129 | yes |
| mimic | `LAT_INFLAMMATION_SEPSIS` | 0.16117863078031663 | 0.1613343714629977 | 0.14854354851917861 | yes |
| mimic | `LAT_METABOLIC_DERANGEMENT` | 0.01974295345435545 | 0.017989452868950796 | 0.03132348239996354 | yes |
| mimic | `LAT_NEUROLOGIC_DYSFUNCTION` | 0.034252711518043336 | 0.03154960397072449 | 0.034993031034570465 | yes |
| mimic | `LAT_RENAL_DYSFUNCTION` | 0.09129044441831921 | 0.08859517453837928 | 0.08697155012811061 | yes |
| mimic | `LAT_RESPIRATORY_FAILURE` | 0.036133320420856 | 0.03909791554254309 | 0.04976550012196902 | yes |
| mimic | `LAT_SHOCK` | 0.020994326819048455 | 0.021245787889811386 | 0.031644985158239956 | yes |
| physionet | `LAT_CARDIAC_INJURY_STRAIN` | 0.1118307526053288 | 0.12203313682540579 | 0.11941345027314323 | yes |
| physionet | `LAT_COAG_HEME_DYSFUNCTION` | 0.01079355815492156 | 0.004135693132290908 | 0.025428398451365294 | yes |
| physionet | `LAT_GLOBAL_SEVERITY` | 0.10798789990231876 | 0.10674017610435634 | 0.10503878126970247 | yes |
| physionet | `LAT_HEPATIC_DYSFUNCTION` | 0.09052704652421123 | 0.06018403931880851 | 0.10684272691739839 | yes |
| physionet | `LAT_INFLAMMATION_SEPSIS_BURDEN` | 0.07180004977331886 | 0.07087168486512074 | 0.0674804416051104 | yes |
| physionet | `LAT_METABOLIC_DERANGEMENT` | 0.07770406267721523 | 0.07973829165462494 | 0.0907344995137599 | yes |
| physionet | `LAT_NEUROLOGIC_DYSFUNCTION` | 0.08163578213590206 | 0.07572758184655413 | 0.07704883483275221 | yes |
| physionet | `LAT_RENAL_DYSFUNCTION` | 0.1200268544489593 | 0.0906219401807068 | 0.11066853776658027 | yes |
| physionet | `LAT_RESPIRATORY_FAILURE` | 0.06475009736198116 | 0.06266009635207058 | 0.06298443986654997 | yes |
| physionet | `LAT_SHOCK` | -0.013849200594340203 | -0.02694439466909599 | 0.00412193359964432 | no |

- Counts: MIMIC 9 concordant, 0 discordant, total 9; PhysioNet 9 concordant, 1 discordant, total 10; overall 18 concordant, 1 discordant, total 19.
- Sole exception: PhysioNet `LAT_SHOCK`; CausalForestDML negative, LinearDML negative, CausalPFN positive.
- No outcome-downsampled row was selected and no magnitude comparison or equivalence claim is made.
- Output: `thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png`.
- Dimensions: 3060 x 1740; file size: 149,880 bytes.
- SHA-256: `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea`.
- Chapter label: `fig:results-three-estimator-direction`.

## 7. Chapter changes

- Removed the paragraph stating that the selected figures were blocked and not inserted.
- Inserted the MIMIC ranking after the MIMIC primary table, the PhysioNet ranking after the PhysioNet primary table, and the direction-agreement figure in the CausalPFN exploratory section.
- Added surrounding cross-references and the required bounded captions.
- Chapter 10 contains exactly three `includegraphics` commands, all for the generated replacement filenames; none references an archived conflicting PNG.
- The section order, estimator/population hierarchy, 18-of-19 conclusion, shock exception, downsampling interpretation, predictive results, matching values, and robustness counts were preserved.

## 8. Manifest updates

- Added generated-figure register records and result-manifest rows `ART-01387` through `ART-01389`.
- Every replacement records the relative path, SHA-256, dimensions, generating script, exact filter, source-row count, Chapter 10 placement, caption boundary, and provenance notes.
- Every replacement is recorded with artifact role `generated checked result figure`, source `checked_cate_candidates.csv`, validation/provenance `SOURCE_EXACT_GENERATED`, selection `MAIN_RESULTS`, and admission `ADMISSIBLE_WITH_QUALIFICATIONS`.
- The three original conflicting records retain their original hashes, `BLOCKED_VALUE_CONFLICT`, and `EXCLUDED_FROM_THESIS`, with links to their replacements.
- `results_manifest.md`, `results_source_packet.md`, figure/deferred registers, and placeholder log now describe the repaired gate without resolving unrelated limitations.
- `results_checksums.sha256` was regenerated after the report and manifest contents were finalized; it does not hash itself.

## 9. Numerical integrity

`checked_cate_candidates.csv` is byte-for-byte unchanged. All other numerical checked CSVs are semantically unchanged. The eight table-environment hashes before and after the repair are identical:

| Chapter 10 table | Before and after SHA-256 |
|---|---|
| `tab:results-analysis-populations` | `38e93c76580d8bb375e4e953301d0c8f96d317e8b6ed1f869c6df90378b8f1e9` |
| `tab:results-predictive-performance` | `371105a1c29281b31821a2410ca9ec2adbc5aadb4e31e69d3c8462601d7c014a` |
| `tab:results-forest-mimic` | `5cb715a555efd9e3253642ca2e8d30e6e86689292bdbe79c11ecb00f4e19b2d6` |
| `tab:results-forest-physionet` | `135b794f96763699d98cb08d13b830cf42f1d81b6f70c2bf9816a37bc748dad6` |
| `tab:results-matching-support` | `34fa487fbef1f0bb1a27ff550f74a5366b2cc5df3b36e9d887cbb9b92651bb51` |
| `tab:results-linear-comparison` | `a020e7480e931f6a007d5d85dcb5eef2f5e02851f5a0f394c3e741f7cd3205cb` |
| `tab:results-pfn-comparison` | `284029548f582d96c2d95daa35b90674a82083f171e03b77c799cd31d27e7710` |
| `tab:results-robustness-summary` | `37086290d33c5623709920ab1a0f0d8f6e8402ed879107d8b58bf2f22798837c` |

Result: **0 numerical table changes**.

## 10. Final build and readiness

- Command sequence: `latexmk -C`, then `latexmk -xelatex main.tex`.
- Result: success; `main.pdf` exists, A4, 90 pages, 2,710,115 bytes.
- Final-pass scan: no LaTeX error, undefined control sequence, undefined citation/reference, multiply-defined label, Biber error, emergency stop, or fatal error.
- Non-fatal layout warnings remain across the thesis (95 overfull and 988 underfull boxes in the final log before auxiliary cleanup). The PDF conversion also reported two duplicate internal page-label object warnings caused by the existing front-matter page-label structure. None is specific to the repaired figures or prevents rendering.
- Rendered inspection: physical PDF pages 70, 71, and 77 (thesis-numbered pages 56, 57, and 63) contain the three figures. All labels and values are readable; no crop, text overflow, distortion, or caption separation was observed.
- Causal-language scan: the only prohibited-term hit is `risk ratio` in the explicit qualification that the reported mean model-estimated CATE is not a risk ratio. No inappropriate causal claim remains.
- InterpNet scan across thesis `.tex` files: zero occurrences.
- Supervisor ratification, the CausalPFN primary-citation limitation, missing numbered causal configs, predictive split/checkpoint lineage, raw cohort-total limitations, appendix placement, and the final supervisor/clinical causal-language review remain open and were not marked resolved.

**READY FOR STAGE 4.7.** Stage 4.7 was not begun.

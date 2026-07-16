# Stage 4.6B Evidence Report

## 23.1 Git state

- Verified commit: `5e6477a step 4.6A repair` on branch `main`.
- Verified immediate history: `5e6477a` follows `da200b7 adding figures`, which follows `b4b1212 step 4.6A`.
- `git show --stat --oneline 5e6477a` and `git diff --stat da200b7..5e6477a` were inspected before editing.
- The initial worktree was dirty.  No reset, clean, checkout, stage, amend, commit, or push was performed.
- The checked CSVs and `results_manifest.csv` appeared modified because of line-ending normalization: `git diff --numstat` showed equal deleted/added line counts, while `git diff --ignore-space-at-eol --stat` was empty.  Stage 4.6B did not edit any checked source.
- Initial worktree:

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

- Authorized Stage 4.6B changes: `thesis-writing/thesis/chapters/10_results.tex`, `thesis-writing/logs/unresolved_placeholders.md`, `thesis-writing/logs/deferred_fixes.md`, this evidence report, and the build-produced `thesis-writing/thesis/main.pdf`.
- Final worktree retained every initial entry and added only the authorized Stage 4.6B paths shown below.  A post-build `latexmk -c` removed auxiliary files while preserving `main.pdf`.

```text
 M thesis-writing/logs/deferred_fixes.md
 M thesis-writing/logs/unresolved_placeholders.md
 M thesis-writing/thesis/chapters/10_results.tex
 M thesis-writing/thesis/main.pdf
?? thesis-writing/logs/stage_4_6B_evidence_report.md
```

All initial unrelated paths listed above remained present and were not discarded.
- Checked CSVs, result manifests, decision/source packets, source optional figures, research code, configurations, and bibliography files were not modified by Stage 4.6B.

## 23.2 Baseline build

- Command: `cd thesis-writing/thesis && latexmk -xelatex main.tex && pdfinfo main.pdf`.
- Return status: 0.
- Baseline PDF: `thesis-writing/thesis/main.pdf`, 79 A4 pages.
- Warnings: pre-existing undefined citation/reference messages on the first clean pass, layout underfull/overfull boxes, and duplicate page-object warnings from `xdvipdfmx`; no fatal error.

## 23.3 Numerical source inventory

| Chapter section | Table/figure label | Checked source | Selection filter/source rows | Displayed fields | Rounding/derivation | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| 10.1 | `tab:results-analysis-populations` | `checked_cohort_candidates.csv`; `checked_cate_candidates.csv` | Cohort lines 12 and 18 corroborate row counts; original CATE lines 2--10 and 56--65 establish causal model rows | dataset, population, sampling, count, scope | integer counts; difference and ratio derived below | causal-analysis counts, not raw totals |
| 10.2 | `tab:results-predictive-performance` | `checked_predictive_metrics.csv` | `metric_split=test`, `selection_status=PRIMARY_MAIN_TEXT`; lines 3,5,7,9,11,13,15,17,19,21 | loss, AUROC, AUPRC, minRP | three decimals | split/checkpoint lineage incomplete |
| 10.3 | `tab:results-forest-mimic` | `checked_cate_candidates.csv` | Forest/original/primary; lines 2--10 | treatment rate, mean CATE, observed adjustment variables, status | three decimals | identifiability unresolved; numbered configs missing |
| 10.3 | `tab:results-forest-physionet` | `checked_cate_candidates.csv` | Forest/original/primary; lines 56--65 | same | three decimals | same |
| 10.3 | requested ranking figures | `figure_selection_register.md` | two ranking entries | none inserted | N/A | both `BLOCKED_VALUE_CONFLICT` |
| 10.4 | `tab:results-matching-support` | `checked_matching_results.csv`; `checked_matching_failures.csv` | original supporting rows: results lines 10--17 and 25--31; failures lines 3 and 7--9 | pairs, rate, distance, matched-pair difference, status | rates/effects three decimals except 0.0017 retained at four | treated/control counts unavailable; greedy indirect support |
| 10.5 | `tab:results-linear-comparison` | `checked_cate_candidates.csv` | original Forest and Linear rows: 2--10, 20--28, 56--65, 76--85 | two mean CATEs, direction | three decimals | direction agreement is not equivalence |
| 10.6 | `tab:results-pfn-comparison` | `checked_cate_candidates.csv` | original PFN rows 38--46 and 96--105, paired with DML rows | PFN mean, DML signs, agreement | three decimals; PhysioNet shock four decimals | exploratory; later diagnostics intentionally skipped |
| 10.6 | requested direction figure | `figure_selection_register.md` | `cross_model_direction_counts.png` entry | none inserted | N/A | `BLOCKED_VALUE_CONFLICT`; mixes sampling modes |
| 10.7 | prose | checked CATE original rows | all original rows | counts, rates, conceptual comparison | counts/ratio; rates three decimals | no pooling or construct-equivalence claim |
| 10.8 | `tab:results-robustness-summary` | checked CATE, matching, sensitivity, and permutation CSVs | all outcome-downsampled robustness rows plus original status rows | status counts | integer status counts | downsampled population differs; no diagnostic magnitude |

No normalized CATE, interval bound, new p-value, pooled effect, cross-estimator average, cross-dataset average, or new subgroup effect was displayed.

## 23.4 Analysis populations

| Dataset | Checked input rows | Exact source count | Display | Exact source outcome rate used in prose | Display |
| --- | --- | ---: | ---: | ---: | ---: |
| MIMIC | `checked_cate_candidates.csv` lines 2--10; cohort line 12 corroborates | 26845 | 26,845 | 0.12080461910970386 | 0.121 |
| PhysioNet | CATE lines 56--65; cohort line 18 corroborates | 7993 | 7,993 | 0.14237457775553608 | 0.142 |

Derived comparisons:

- Difference formula: `26845 - 7993`; inputs: checked original model-row counts above; output: `18852`, displayed `18,852`.
- Ratio formula: `26845 / 7993`; inputs: same rows; output: `3.358563743275366`, displayed `approximately 3.36`.
- Scope wording: original causal-analysis population/model rows, explicitly not raw cohort totals.

## 23.5 Predictive results

Every source summary agreed with its paired log within the packet's checked tolerance.  Every row carries the `PREDICTIVE_SPLIT_MANIFEST_MISSING` and `CHECKPOINT_EXPORT_MAPPING_MISSING` caveats.

| CSV line | Dataset | Model | Exact loss | Display | Exact AUROC | Display | Exact AUPRC | Display | Exact minRP | Display |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | MIMIC | GRU | 0.385757 | 0.386 | 0.881119 | 0.881 | 0.839559 | 0.840 | 0.770421 | 0.770 |
| 5 | MIMIC | GRU-D | 0.404448 | 0.404 | 0.884277 | 0.884 | 0.841273 | 0.841 | 0.772533 | 0.773 |
| 9 | MIMIC | STraTS | 0.348136 | 0.348 | 0.905411 | 0.905 | 0.869417 | 0.869 | 0.795399 | 0.795 |
| 11 | MIMIC | TCN | 0.414456 | 0.414 | 0.866914 | 0.867 | 0.822642 | 0.823 | 0.757798 | 0.758 |
| 13 | PhysioNet | GRU | 0.396819 | 0.397 | 0.914616 | 0.915 | 0.897493 | 0.897 | 0.831044 | 0.831 |
| 15 | PhysioNet | GRU-D | 0.330593 | 0.331 | 0.918478 | 0.918 | 0.905105 | 0.905 | 0.834958 | 0.835 |
| 19 | PhysioNet | STraTS | 0.340692 | 0.341 | 0.914761 | 0.915 | 0.877456 | 0.877 | 0.818228 | 0.818 |
| 21 | PhysioNet | TCN | 0.476513 | 0.477 | 0.899103 | 0.899 | 0.875091 | 0.875 | 0.811184 | 0.811 |

Summary statements were computed only by sorting the checked displayed metrics: STraTS leads all four MIMIC metrics; GRU-D leads all four PhysioNet metrics.  Validation rows were not displayed.

## 23.6 Primary CausalForestDML results

All rows use `sampling_condition=original`, `selection_status=PRIMARY_MAIN_TEXT`; adjustment variables are exact checked `observed_confounders` values.  Every row has `identifiable_with_available_nodes=UNRESOLVED` and the caveats `NUMBERED_CONFIG_MISSING;ESTIMAND_WORDING_UNRESOLVED;ARCHIVE_COPY_PROVENANCE_PARTIAL`.

### MIMIC

| CSV line | Exposure | Exact prevalence | Display | Exact mean CATE | Display | Adjustment code / exact observed variables |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 2 | `LAT_CARDIAC_STRAIN` | 0.1776494691748929 | 0.178 | 0.22035603834514436 | 0.220 | M1: Age, Gender, LAT_CHRONIC_BURDEN |
| 3 | `LAT_INFLAMMATION_SEPSIS` | 0.4718197057180108 | 0.472 | 0.16117863078031663 | 0.161 | M0: empty |
| 4 | `LAT_HEPATIC_COAG_DYSFUNCTION` | 0.2413112311417396 | 0.241 | 0.09759849060449512 | 0.098 | M2: LAT_INFLAMMATION_SEPSIS, LAT_SHOCK |
| 5 | `LAT_RENAL_DYSFUNCTION` | 0.3630843732538648 | 0.363 | 0.09129044441831921 | 0.091 | M3: LAT_CHRONIC_BURDEN, LAT_SHOCK |
| 6 | `LAT_GLOBAL_SEVERITY` | 0.7192400819519463 | 0.719 | 0.06210061818008489 | 0.062 | M4: Age, Gender, LAT_CHRONIC_BURDEN, LAT_INFLAMMATION_SEPSIS |
| 7 | `LAT_RESPIRATORY_FAILURE` | 0.5903147699757869 | 0.590 | 0.036133320420856 | 0.036 | M5: Age, Gender, LAT_CHRONIC_BURDEN, LAT_GLOBAL_SEVERITY, LAT_INFLAMMATION_SEPSIS |
| 8 | `LAT_NEUROLOGIC_DYSFUNCTION` | 0.43389830508474575 | 0.434 | 0.034252711518043336 | 0.034 | M5: same |
| 9 | `LAT_SHOCK` | 0.5396163158875024 | 0.540 | 0.020994326819048455 | 0.021 | M6: Age, Gender, LAT_CARDIAC_STRAIN, LAT_CHRONIC_BURDEN, LAT_INFLAMMATION_SEPSIS |
| 10 | `LAT_METABOLIC_DERANGEMENT` | 0.3729186068169119 | 0.373 | 0.01974295345435545 | 0.020 | M7: LAT_GLOBAL_SEVERITY, LAT_RENAL_DYSFUNCTION, LAT_RESPIRATORY_FAILURE, LAT_SHOCK |

### PhysioNet

| CSV line | Exposure | Exact prevalence | Display | Exact mean CATE | Display | Adjustment code / exact observed variables |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 56 | `LAT_RENAL_DYSFUNCTION` | 0.23032653571875392 | 0.230 | 0.1200268544489593 | 0.120 | P1: ICUType_1--4, LAT_CARDIAC_INJURY_STRAIN, LAT_INFLAMMATION_SEPSIS_BURDEN, LAT_SHOCK |
| 57 | `LAT_CARDIAC_INJURY_STRAIN` | 0.35531089703490554 | 0.355 | 0.1118307526053288 | 0.112 | P2: ICUType_1--4 |
| 58 | `LAT_GLOBAL_SEVERITY` | 0.7770549230576754 | 0.777 | 0.10798789990231876 | 0.108 | P3: Age, Gender, ICUType_1--4, LAT_CHRONIC_BASELINE_RISK, LAT_INFLAMMATION_SEPSIS_BURDEN, Weight |
| 59 | `LAT_HEPATIC_DYSFUNCTION` | 0.1417490304016014 | 0.142 | 0.09052704652421123 | 0.091 | P1: same |
| 60 | `LAT_NEUROLOGIC_DYSFUNCTION` | 0.6588264731640185 | 0.659 | 0.08163578213590206 | 0.082 | P0: empty |
| 61 | `LAT_METABOLIC_DERANGEMENT` | 0.558113349180533 | 0.558 | 0.07770406267721523 | 0.078 | P4: LAT_RENAL_DYSFUNCTION, LAT_RESPIRATORY_FAILURE, LAT_SHOCK |
| 62 | `LAT_INFLAMMATION_SEPSIS_BURDEN` | 0.5626172901288627 | 0.563 | 0.07180004977331886 | 0.072 | P0: empty |
| 63 | `LAT_RESPIRATORY_FAILURE` | 0.6144126110346553 | 0.614 | 0.06475009736198116 | 0.065 | P0: empty |
| 64 | `LAT_COAG_HEME_DYSFUNCTION` | 0.395095708745152 | 0.395 | 0.01079355815492156 | 0.011 | P5: LAT_INFLAMMATION_SEPSIS_BURDEN, LAT_SHOCK |
| 65 | `LAT_SHOCK` | 0.6956086575753785 | 0.696 | -0.013849200594340203 | -0.014 | P6: ICUType_1--4, LAT_CARDIAC_INJURY_STRAIN, LAT_INFLAMMATION_SEPSIS_BURDEN |

Exposure completeness: 9/9 MIMIC and 10/10 PhysioNet original Forest exposures appear once; no result-based omission or duplicate occurred.  Normalized CATE and interval bounds are absent.

## 23.7 Matching

Wording used: **descriptive matched-pair outcome difference**.  The checked rows have empty `n_treated` and `n_control`; those fields were not inferred.

| CSV line | Dataset/exposure | Exact pairs | Exact match rate -> display | Exact difference -> display | Distance | Status/warning |
| ---: | --- | ---: | --- | --- | ---: | --- |
| 10 | MIMIC `LAT_CARDIAC_STRAIN` | 4769 | 1.0 -> 1.000 | 0.3447263577269868 -> 0.345 | 0 | sufficient |
| 11 | MIMIC `LAT_GLOBAL_SEVERITY` | 7537 | 0.39035632898280503 -> 0.390 | 0.07483083454955552 -> 0.075 | 1 | insufficient-pair flag |
| 12 | MIMIC `LAT_HEPATIC_COAG_DYSFUNCTION` | 6478 | 1.0 -> 1.000 | 0.13337449830194503 -> 0.133 | 0 | sufficient |
| 13 | MIMIC `LAT_METABOLIC_DERANGEMENT` | 5061 | 0.505543901708121 -> 0.506 | 0.03694921952183363 -> 0.037 | 0 | sufficient |
| 14 | MIMIC `LAT_NEUROLOGIC_DYSFUNCTION` | 6275 | 0.5387190934065934 -> 0.539 | 0.026932270916334662 -> 0.027 | 0 | sufficient |
| 15 | MIMIC `LAT_RENAL_DYSFUNCTION` | 8915 | 0.9146404021750282 -> 0.915 | 0.13359506449803701 -> 0.134 | 0 | sufficient |
| 16 | MIMIC `LAT_RESPIRATORY_FAILURE` | 10998 | 0.694011484823626 -> 0.694 | 0.10565557374068012 -> 0.106 | 2 | sufficient; larger distance |
| 17 | MIMIC `LAT_SHOCK` | 10380 | 0.7165539141239817 -> 0.717 | 0.03863198458574181 -> 0.039 | 1 | sufficient |
| failure 3 | MIMIC `LAT_INFLAMMATION_SEPSIS` | missing | missing | missing | missing | no binary matching columns |
| 25 | PhysioNet `LAT_CARDIAC_INJURY_STRAIN` | 2840 | 1.0 -> 1.000 | 0.13380281690140844 -> 0.134 | 0 | sufficient |
| 26 | PhysioNet `LAT_COAG_HEME_DYSFUNCTION` | 1763 | 0.5582647245091831 -> 0.558 | 0.0017016449234259785 -> 0.0017 | 0 | sufficient |
| 27 | PhysioNet `LAT_GLOBAL_SEVERITY` | 1782 | 0.2869103203992916 -> 0.287 | 0.09539842873176206 -> 0.095 | 1 | insufficient-pair flag |
| 28 | PhysioNet `LAT_HEPATIC_DYSFUNCTION` | 1133 | 1.0 -> 1.000 | 0.13680494263018536 -> 0.137 | 0 | sufficient |
| 29 | PhysioNet `LAT_METABOLIC_DERANGEMENT` | 3378 | 0.7572293207800942 -> 0.757 | 0.07341622261693309 -> 0.073 | 2 | sufficient; larger distance |
| 30 | PhysioNet `LAT_RENAL_DYSFUNCTION` | 1841 | 1.0 -> 1.000 | 0.15426398696360674 -> 0.154 | 0 | sufficient |
| 31 | PhysioNet `LAT_SHOCK` | 2433 | 0.437589928057554 -> 0.438 | 0.010275380189066995 -> 0.010 | 1 | insufficient-pair flag |
| failures 7--9 | PhysioNet inflammation/sepsis burden, neurologic dysfunction, respiratory failure | missing | missing | missing | missing | no binary matching columns |

Derived direction comparison: among the 15 successful original matching rows, 14 share the Forest sign.  Formula: compare `sign(mean_pair_effect)` with the matched original Forest `sign(mean_cate)`; the only mismatch is PhysioNet shock (0.010275380189066995 versus -0.013849200594340203).

## 23.8 LinearDML comparison

Formula: inner join original Forest and Linear rows on `(dataset,treatment)`, then compare the sign of exact `mean_cate`.  Result: MIMIC 9/9, PhysioNet 10/10, total 19/19.

| Dataset/exposure | Forest exact -> display | Linear exact -> display | Agreement |
| --- | --- | --- | --- |
| MIMIC cardiac strain | 0.22035603834514436 -> 0.220 | 0.1876338252286513 -> 0.188 | yes |
| MIMIC inflammation/sepsis | 0.16117863078031663 -> 0.161 | 0.1613343714629977 -> 0.161 | yes |
| MIMIC hepatic/coagulation | 0.09759849060449512 -> 0.098 | 0.08301684982922239 -> 0.083 | yes |
| MIMIC renal | 0.09129044441831921 -> 0.091 | 0.08859517453837928 -> 0.089 | yes |
| MIMIC global severity | 0.06210061818008489 -> 0.062 | 0.08015308816889209 -> 0.080 | yes |
| MIMIC respiratory | 0.036133320420856 -> 0.036 | 0.03909791554254309 -> 0.039 | yes |
| MIMIC neurologic | 0.034252711518043336 -> 0.034 | 0.03154960397072449 -> 0.032 | yes |
| MIMIC shock | 0.020994326819048455 -> 0.021 | 0.021245787889811386 -> 0.021 | yes |
| MIMIC metabolic | 0.01974295345435545 -> 0.020 | 0.017989452868950796 -> 0.018 | yes |
| PhysioNet renal | 0.1200268544489593 -> 0.120 | 0.0906219401807068 -> 0.091 | yes |
| PhysioNet cardiac injury/strain | 0.1118307526053288 -> 0.112 | 0.12203313682540579 -> 0.122 | yes |
| PhysioNet global severity | 0.10798789990231876 -> 0.108 | 0.10674017610435634 -> 0.107 | yes |
| PhysioNet hepatic | 0.09052704652421123 -> 0.091 | 0.06018403931880851 -> 0.060 | yes |
| PhysioNet neurologic | 0.08163578213590206 -> 0.082 | 0.07572758184655413 -> 0.076 | yes |
| PhysioNet metabolic | 0.07770406267721523 -> 0.078 | 0.07973829165462494 -> 0.080 | yes |
| PhysioNet inflammation/sepsis | 0.07180004977331886 -> 0.072 | 0.07087168486512074 -> 0.071 | yes |
| PhysioNet respiratory | 0.06475009736198116 -> 0.065 | 0.06266009635207058 -> 0.063 | yes |
| PhysioNet coagulation/hematologic | 0.01079355815492156 -> 0.011 | 0.004135693132290908 -> 0.004 | yes |
| PhysioNet shock | -0.013849200594340203 -> -0.014 | -0.02694439466909599 -> -0.027 | yes |

Magnitude statements use direct subtraction only: MIMIC cardiac absolute difference 0.032722213116493065 (approximately 0.033); MIMIC global severity 0.018052469988807204 (approximately 0.018); PhysioNet hepatic 0.03034300720540272 (approximately 0.030); PhysioNet renal 0.029404914268252508 (approximately 0.029).  Rankings were obtained by sorting exact within-estimator means; no correlation was calculated.

## 23.9 CausalPFN comparison

All original PFN rows were selected with `selection_status=EXPLORATORY_MAIN_TEXT`.

| Dataset/exposure | Exact PFN -> display | Forest sign | Linear sign | All-three direction |
| --- | --- | ---: | ---: | --- |
| MIMIC cardiac strain | 0.259327498577642 -> 0.259 | + | + | agree |
| MIMIC inflammation/sepsis | 0.14854354851917861 -> 0.149 | + | + | agree |
| MIMIC hepatic/coagulation | 0.0968462757091129 -> 0.097 | + | + | agree |
| MIMIC renal | 0.08697155012811061 -> 0.087 | + | + | agree |
| MIMIC global severity | 0.07304968889618824 -> 0.073 | + | + | agree |
| MIMIC respiratory | 0.04976550012196902 -> 0.050 | + | + | agree |
| MIMIC neurologic | 0.034993031034570465 -> 0.035 | + | + | agree |
| MIMIC shock | 0.031644985158239956 -> 0.032 | + | + | agree |
| MIMIC metabolic | 0.03132348239996354 -> 0.031 | + | + | agree |
| PhysioNet cardiac injury/strain | 0.11941345027314323 -> 0.119 | + | + | agree |
| PhysioNet renal | 0.11066853776658027 -> 0.111 | + | + | agree |
| PhysioNet hepatic | 0.10684272691739839 -> 0.107 | + | + | agree |
| PhysioNet global severity | 0.10503878126970247 -> 0.105 | + | + | agree |
| PhysioNet metabolic | 0.0907344995137599 -> 0.091 | + | + | agree |
| PhysioNet neurologic | 0.07704883483275221 -> 0.077 | + | + | agree |
| PhysioNet inflammation/sepsis | 0.0674804416051104 -> 0.067 | + | + | agree |
| PhysioNet respiratory | 0.06298443986654997 -> 0.063 | + | + | agree |
| PhysioNet coagulation/hematologic | 0.025428398451365294 -> 0.025 | + | + | agree |
| PhysioNet shock | 0.00412193359964432 -> 0.0041 | - | - | disagree |

Agreement formula: inner join exact original Forest, Linear, and PFN rows on `(dataset,treatment)` and count rows where all three signs are equal.  Outputs: MIMIC 9/9; PhysioNet 9/10; total 18/19.  Exact PhysioNet shock values: Forest -0.013849200594340203, Linear -0.02694439466909599, PFN 0.00412193359964432.

Bounded conclusion used verbatim in substance: CausalPFN reproduced the prevailing direction in nearly every comparison and may be promising as a complementary estimator; this does not establish equivalence, superiority, validity, or interchangeable uncertainty.  Diagnostic limitation: saved-CATE sensitivity and permutation stages were intentional skips, not execution failures; the primary citation remains unresolved.

## 23.10 Downsampling

Source rows: `checked_cate_candidates.csv` MIMIC Forest 11--19, Linear 29--37, PFN 47--55; PhysioNet Forest 66--75, Linear 86--95, PFN 106--115.  Matching uses all `ROBUSTNESS_APPENDIX` rows in `checked_matching_results.csv` and `checked_matching_failures.csv`.

- MIMIC downsample model rows: exact 6486; outcome rate 0.5; display 6,486 and 0.500.
- PhysioNet downsample model rows: exact 2276; outcome rate 0.5; display 2,276 and 0.500.
- Direction calculation: join original and downsampled rows on `(dataset,estimator,treatment)` and compare exact signs.
  - MIMIC Forest 9/9; Linear 9/9; PFN 9/9.
  - PhysioNet Forest 10/10; Linear 9/10; PFN 9/10.
  - Total: `(9+9+9+10+9+9)/(9+9+9+10+10+10) = 55/57`.
- Sign changes:
  - PhysioNet Linear `LAT_COAG_HEME_DYSFUNCTION`: 0.004135693132290908 -> -0.01740576478180357; displays 0.0041 -> -0.0174.
  - PhysioNet PFN `LAT_SHOCK`: 0.00412193359964432 -> -0.04128668318471506; displays 0.0041 -> -0.0413.
- Magnitude comparison: exact inequality test over the 57 joined means found 57/57 numerically different original/downsampled values.  No thresholded ``material change'' metric was invented.
- Matching availability: MIMIC 8 successes/1 failure in both conditions; PhysioNet 7 successes/3 failures in both.  Population separation and no-pooling wording is explicit.

## 23.11 Sensitivity and permutation

Sensitivity source: all 80 rows of `checked_sensitivity_candidates.csv`.

| Dataset/estimator/sampling family | Checked status |
| --- | --- |
| MIMIC Forest, original and downsampled | 8 partial; 1 failed in each condition |
| MIMIC Linear, original and downsampled | 8 partial; 1 failed in each condition |
| PhysioNet Forest, original and downsampled | 7 partial; 3 failed in each condition |
| PhysioNet Linear, original and downsampled | 7 partial; 3 failed in each condition |
| PFN, both datasets and conditions | intentional skip / not applicable to PFN pipeline |

Partial-row source classification: `saved_training_direct;saved_training_direct;custom_reconstructed_from_residual_params`; residual status `saved_training_direct`; benchmark status `unimplemented_by_design`.  Failed rows are MIMIC inflammation/sepsis and PhysioNet inflammation/sepsis burden, neurologic dysfunction, and respiratory failure.  No sensitivity value is displayed in Chapter 10, so no source class is detached from a numerical value.

Permutation source: all 160 rows of `checked_permutation_candidates.csv`.  The 152 non-PFN aggregate rows each record 10 trials and seed 42; treatment and outcome types are present for every DML dataset--exposure--sampling row.  Eight PFN dataset/sampling/type status rows are `INTENTIONAL_SKIP`.  No new p-value was computed or displayed.  Empty checked `subprocess_status` and warning fields for ordinary rows were not upgraded into an unrecorded success claim.

## 23.12 Figures

No figure was copied or inserted because the frozen selection register excludes all three requested files from the relevant chapter role.

| Requested figure | Source SHA-256 | Dimensions | Destination | Figure label | Frozen validation |
| --- | --- | ---: | --- | --- | --- |
| `mimic_non_downsampled_cate_ranking.png` | `e54ad1cf1d268135def7312f69065b49221a505d04d885720eb2d984e8e0428a` | 1461x831 | not copied | none | `BLOCKED_VALUE_CONFLICT`: labels match a two-DML average, not stated three-estimator median |
| `physionet_non_downsampled_cate_ranking.png` | `890db4d998ca1c4d8fe8b31024291f508ab01c5a418db280a3c1ebf793bfdf2c` | 1460x899 | not copied | none | same conflict |
| `cross_model_direction_counts.png` | `3fe798a320b6c96f1c106f0b81b4d856aef902976c84f10df40a30a4947ba32b` | 1739x978 | not copied | none | `BLOCKED_VALUE_CONFLICT`: combines original and downsampled rows |

Numerical validation status: the text/tables validate the checked original-cohort values; the blocked images do not.  No source PNG was edited or redrawn, and no excluded figure was referenced in the thesis.

## 23.13 Citations

No new bibliography citation was added.  Chapter 10 relies on cross-references to Chapters 7--9 and the checked repository evidence.

## 23.14 Placeholders and deferred fixes

- Resolved: all generic Chapter 10 result, validation, figure, and supervisor-decision skeleton placeholders were removed and replaced with checked prose/tables or an explicit frozen figure-block statement.
- Retained: supervisor ratification, raw cohort totals, exact configs, predictive split/checkpoint lineage, overlap figure, clinical validation, CausalPFN citation/diagnostics, and appendix placement.
- Added deferred fixes: `DF-4.6B-001` ranking-figure conflicts; `DF-4.6B-002` appendix result placement; `DF-4.6B-003` final causal-language review; `DF-4.6B-004` final rounded-value reverification.
- Existing equivalent issues were referenced rather than duplicated.

## 23.15 Final build

- Command: `cd thesis-writing/thesis && latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.
- Return status: 0 for clean, build, file test, and `pdfinfo`.
- PDF: `thesis-writing/thesis/main.pdf`, 87 A4 pages, 2,048,751 bytes.
- Final `main.log`: 0 unresolved citations, 0 unresolved references, 0 duplicate labels, 0 Biber errors, and 0 fatal errors.
- Layout: pre-existing thesis-wide warnings remain.  Chapter 10 contributed three small overfull prose lines (maximum reported excess 4.64316 pt) and underfull cells in the compact matching/robustness tables.  Rendered Chapter 10 pages were inspected and remained within the page bounds and readable.
- `xdvipdfmx` emitted the existing two duplicate page-object warnings (`Object @page.i already defined`).
- Post-build auxiliary cleanup: `latexmk -c`; return status 0; `main.pdf` preserved.

Programmatic transcription validation parsed the Chapter 10 tables and compared them with the selected checked CSV rows.  Result: 0 errors; 10 predictive rows; 19/19 primary Forest exposures (MIMIC 9, PhysioNet 10); Forest--Linear direction 19/19; all-three direction 18/19; original/downsampled direction 55/57 with exactly the two recorded changes; 57/57 paired means numerically different.  `git diff --check` passed.

Final scans:

- Thesis-wide InterpNet scan: no occurrence.
- Chapter 10 generic placeholder scan: no occurrence.
- Chapter 10 figure scan: no `\includegraphics` and no excluded-figure reference.
- Causal-language scan: the only target-term hit was the explicit boundary that mean model-estimated CATE is not a risk ratio.  No unqualified ATE/ATT, significance, causation-proof, clinical-actionability, positivity, confounding-elimination, or estimator-superiority claim was found.
- Checked-source semantic diff: `git diff --ignore-space-at-eol --stat -- thesis-writing/results/checked_*.csv thesis-writing/results/results_manifest.csv` remained empty.

## 23.16 Readiness

**BLOCKED BEFORE STAGE 4.7**

Reason: the frozen Stage 4.6A packet marks all three mandated main-result figures `BLOCKED_VALUE_CONFLICT`.  The numerical chapter, tables, and diagnostics can be validated and built, but inserting those images would violate the same prompt's frozen-packet admission rule.  Supervisor ratification also remains pending.

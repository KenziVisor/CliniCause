# Stage 5.2 Evidence Report

## 24.1 Repository baseline

- Branch: `main`.
- HEAD: `11a2cb46a87a979677602556611a704cfbd1074a` (`step 5.1`).
- Parent: `4f69df9a8e42154576b9526a500f8b687bda3715` (`step 4.10C`).
- Stage 5.1 conclusion: `READY FOR STAGE 5.2 WITH NON-BLOCKING WARNINGS`.
- Stage 5.1 commit inspection found only auxiliary-file cleanup and narrow ignore changes; no checked CSV, figure, generator, or protected result-record changes.
- The worktree was already dirty. All listed baseline modifications except the user-supplied `prompt.txt` content were CRLF-only when compared with `--ignore-cr-at-eol`; they were preserved.

Initial `git status --short`:

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

Protected baseline and final hashes:

| Path | Initial SHA-256 | Final SHA-256 | Status |
|---|---|---|---|
| `thesis-writing/results/checked_cate_candidates.csv` | `594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835` | `594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_cohort_candidates.csv` | `e8ca0a6d3290f4135f56e2ba07e69b70c9856e4d6442620f891860223a3a9210` | `e8ca0a6d3290f4135f56e2ba07e69b70c9856e4d6442620f891860223a3a9210` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_figure_candidates.csv` | `5145242aac10fe896a79a8331f400c0bc1cdc2db5f218cdfba2c1394f0866042` | `5145242aac10fe896a79a8331f400c0bc1cdc2db5f218cdfba2c1394f0866042` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_heterogeneity_candidates.csv` | `470bfd1bca46fc3b5e4c8c5b0a75a6b7bbacb78dc6e4f9ff75b52bc4bd5e77c7` | `470bfd1bca46fc3b5e4c8c5b0a75a6b7bbacb78dc6e4f9ff75b52bc4bd5e77c7` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_matching_failures.csv` | `50109696273da6e006ae88e54f179e462d731a3c788f354cfe2e8d0f195fc3ae` | `50109696273da6e006ae88e54f179e462d731a3c788f354cfe2e8d0f195fc3ae` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_matching_results.csv` | `8b8d1a992a2419db24a351404d211fac79bbc277b9bdd5c2cbb554057da03b0b` | `8b8d1a992a2419db24a351404d211fac79bbc277b9bdd5c2cbb554057da03b0b` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_mortality_prediction.csv` | `398fa90d6fc38a422e5dbf567b06a6a9a14806a30bea64c352cbca86803d97fb` | `398fa90d6fc38a422e5dbf567b06a6a9a14806a30bea64c352cbca86803d97fb` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_permutation_candidates.csv` | `ca2e7239b6a9f96c2001f78452496c5047201972f8b4382137301b65308a163f` | `ca2e7239b6a9f96c2001f78452496c5047201972f8b4382137301b65308a163f` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_predictive_exports.csv` | `2c89d339419a017bd576ca360b6f0fe4f6d295a6c8934e386b5f5c5de2f4572a` | `2c89d339419a017bd576ca360b6f0fe4f6d295a6c8934e386b5f5c5de2f4572a` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_predictive_metrics.csv` | `6bd59e26d617b8728ef9bd5d3bebd0862148ef7bd3975c6e28eea243c3848c3d` | `6bd59e26d617b8728ef9bd5d3bebd0862148ef7bd3975c6e28eea243c3848c3d` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_proxy_cooccurrence.csv` | `91e7a13b767569654082fa55f94aa16cf40ce765b548cde29852e304932f182a` | `91e7a13b767569654082fa55f94aa16cf40ce765b548cde29852e304932f182a` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_proxy_mortality_association.csv` | `f7a596e11b70cd5a6d59a2f916d199f6e4c150c7a61c7ddacc15e2a268de8d98` | `f7a596e11b70cd5a6d59a2f916d199f6e4c150c7a61c7ddacc15e2a268de8d98` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_proxy_prevalence.csv` | `f8f8c0f566683df20679478f092fca9a5d588cd347d60b8e7bb3a985a9257a70` | `f8f8c0f566683df20679478f092fca9a5d588cd347d60b8e7bb3a985a9257a70` | BYTE_IDENTICAL |
| `thesis-writing/results/checked_sensitivity_candidates.csv` | `2bc2d88a6a0b63e6461c1886428f3d979209504c73008c95fb55026d11094a4a` | `2bc2d88a6a0b63e6461c1886428f3d979209504c73008c95fb55026d11094a4a` | BYTE_IDENTICAL |
| `thesis-writing/results/results_manifest.csv` | `e39f3fcb2a927aa1e41942d97466b1ddf790684cf9eaecf9e094777a66a76bbf` | `e39f3fcb2a927aa1e41942d97466b1ddf790684cf9eaecf9e094777a66a76bbf` | BYTE_IDENTICAL |
| `thesis-writing/results/results_manifest.md` | `2fe6018ee7909e75b55c3f5a4e15c95f18f034024afa127ab7bd913686e59554` | `2fe6018ee7909e75b55c3f5a4e15c95f18f034024afa127ab7bd913686e59554` | BYTE_IDENTICAL |
| `thesis-writing/results/results_source_packet.md` | `1209cd85c04dae9a562f8db710a0f6bbb19db82db29e85aafeecb82298eb36e8` | `1209cd85c04dae9a562f8db710a0f6bbb19db82db29e85aafeecb82298eb36e8` | BYTE_IDENTICAL |
| `thesis-writing/results/results_decision_register.md` | `d8d0d4dc68b5b4f4e0a2e28c48f27d6e749bd3d9614656e73d3ebad7300cacf0` | `d8d0d4dc68b5b4f4e0a2e28c48f27d6e749bd3d9614656e73d3ebad7300cacf0` | BYTE_IDENTICAL |
| `thesis-writing/results/results_checksums.sha256` | `dde9daf1ad59f8983a3f64a4453969aa4e5966cff56adfd2f6890d3e78426fde` | `dde9daf1ad59f8983a3f64a4453969aa4e5966cff56adfd2f6890d3e78426fde` | BYTE_IDENTICAL |
| `thesis-writing/results/figure_selection_register.md` | `6e9690c3867cd2809b3c94ba01842974b96997d20a687dd68b524bfb7e72eee1` | `febc6c848ec2732673be38ae8849b9ec02a2f5b3cc3ec660f23592c1a9548e4f` | AUTHORIZED_REGISTER_CLARIFICATION |
| `thesis-writing/literature/metadata/references.bib` | `7759a3b5b40ebe8cd0017698b8f562b1d0e41758299a7d5ce10d85e28b5757f0` | `7759a3b5b40ebe8cd0017698b8f562b1d0e41758299a7d5ce10d85e28b5757f0` | BYTE_IDENTICAL |
| `thesis-writing/literature/metadata/catalog.csv` | `616b58f4ce7c6412ebba79b553ac8086a08aeef6d91ff9c00fec729ecffda3b9` | `616b58f4ce7c6412ebba79b553ac8086a08aeef6d91ff9c00fec729ecffda3b9` | BYTE_IDENTICAL |
| `thesis-writing/thesis/figures/mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | BYTE_IDENTICAL |
| `thesis-writing/thesis/figures/physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | BYTE_IDENTICAL |
| `thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` | BYTE_IDENTICAL |
| `thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` | BYTE_IDENTICAL |
| `thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` | BYTE_IDENTICAL |
| `thesis-writing/results/generate_stage_4_6B_main_figures.py` | `f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af` | `f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af` | BYTE_IDENTICAL |
| `causal-irregular-time-series/src/physionet2012_causal_graph.py` | `825705e5d4a433cd5e0b7717e3ad316b3b17a4ba98b09d18cdbb7dcafe8060ce` | `825705e5d4a433cd5e0b7717e3ad316b3b17a4ba98b09d18cdbb7dcafe8060ce` | BYTE_IDENTICAL |
| `causal-irregular-time-series/src/mimiciii_causal_graph.py` | `4d5e61a59a0d867d578dde014dce42b2cc8f5b2a03aa169fc6354532b02e2490` | `4d5e61a59a0d867d578dde014dce42b2cc8f5b2a03aa169fc6354532b02e2490` | BYTE_IDENTICAL |

## 24.2 Build baseline

- Commands: `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, `pdfinfo main.pdf`.
- Baseline clean build succeeded: 113 A4 pages, 2,845,816 bytes, SHA-256 `da7fe47fe3d61a00a6f58ecb4c6dc5cce22a062f83bf1223c3cabf126d1cc246`.
- Baseline warning profile: 103 overfull hboxes, 1,159 underfull hboxes, 26 nonfatal duplicate longtable destination warnings, and one `biblatex` Hebrew-language support warning. There were no fatal errors, unresolved citations/references, duplicate labels, or missing glyphs.

## 24.3 Included figure inventory

| Figure | Path | SHA-256 | Dimensions | Chapter / label |
|---|---|---|---:|---|
| F-DAG-PHYSIONET | `thesis-writing/thesis/figures/physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | 2200×1800 RGBA | Chapter 7 / `fig:physionet-causal-dag` |
| F-DAG-MIMIC | `thesis-writing/thesis/figures/mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | 5258×3940 RGBA | Chapter 7 / `fig:mimic-causal-dag` |
| F-RESULT-MIMIC-CATE | `thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` | 3360×2220 RGBA | Chapter 10 / `fig:results-mimic-forest-ranking` |
| F-RESULT-PHYSIONET-CATE | `thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` | 3360×2430 RGBA | Chapter 10 / `fig:results-physionet-forest-ranking` |
| F-RESULT-DIRECTION-AGREEMENT | `thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` | 3060×1740 RGBA | Chapter 10 / `fig:results-three-estimator-direction` |

Exactly five `\includegraphics` calls compile, and all are the expected files.

## 24.4 Result-figure generator audit

- Generator: `thesis-writing/results/generate_stage_4_6B_main_figures.py`; SHA-256 `f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af`.
- Authoritative input: `checked_cate_candidates.csv`; SHA-256 `594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835`.
- The complete script was inspected: it enforces required columns, unique `(dataset, estimator, sampling_condition, treatment)` keys, nonempty finite `mean_cate`, expected row counts, complete three-estimator joins, asserted direction counts, and the sole shock exception.
- Ranking filter: dataset-specific, `CausalForestDML`, `original`, `PRIMARY_MAIN_TEXT`; 9 MIMIC and 10 PhysioNet rows.
- Sorting: descending exact `mean_cate`, then treatment identifier as tie-break. Friendly labels remove `LAT_`, title-case words, and retain the identifier on a second line.
- Values use three decimals except a nonzero value rounding to zero at three decimals uses four. A zero line is drawn and negative values are placed left of zero.
- Axis limits use generator padding from the observed exact span; the direction figure uses 0–10.8. Missing/nonfinite/incomplete inputs fail generation.
- Isolated environment: Python 3.12.3, Matplotlib 3.11.0, NumPy 2.5.0, Pillow 12.2.0, DejaVu Sans. Generation occurred under `/tmp/clinicause-stage-5-2`; no thesis PNG was overwritten.

## 24.5 Result-figure source validation

### MIMIC ranking

- Exact display order: `LAT_CARDIAC_STRAIN` 0.220; `LAT_INFLAMMATION_SEPSIS` 0.161; `LAT_HEPATIC_COAG_DYSFUNCTION` 0.098; `LAT_RENAL_DYSFUNCTION` 0.091; `LAT_GLOBAL_SEVERITY` 0.062; `LAT_RESPIRATORY_FAILURE` 0.036; `LAT_NEUROLOGIC_DYSFUNCTION` 0.034; `LAT_SHOCK` 0.021; `LAT_METABOLIC_DERANGEMENT` 0.020.
- 9/9 labels, values, signs, and ranks match the checked rows. Isolated regeneration was byte-identical and pixel-identical: zero differing pixels, maximum channel delta 0.

### PhysioNet ranking

- Exact display order: `LAT_RENAL_DYSFUNCTION` 0.120; `LAT_CARDIAC_INJURY_STRAIN` 0.112; `LAT_GLOBAL_SEVERITY` 0.108; `LAT_HEPATIC_DYSFUNCTION` 0.091; `LAT_NEUROLOGIC_DYSFUNCTION` 0.082; `LAT_METABOLIC_DERANGEMENT` 0.078; `LAT_INFLAMMATION_SEPSIS_BURDEN` 0.072; `LAT_RESPIRATORY_FAILURE` 0.065; `LAT_COAG_HEME_DYSFUNCTION` 0.011; `LAT_SHOCK` -0.014.
- 10/10 labels, values, signs, and ranks match. The negative shock bar and zero line are visible. Isolated regeneration was byte-identical and pixel-identical: zero differing pixels, maximum channel delta 0.

### Direction agreement

- 57 exact original-cohort rows join into 19 dataset–exposure comparisons. MIMIC is 9 concordant / 0 discordant; PhysioNet is 9 / 1; overall 18/19.
- The sole exception is PhysioNet `LAT_SHOCK`: Forest negative, Linear negative, exploratory CausalPFN positive.
- Counts, title, groups, colors, labels, axis, and legend match. Isolated regeneration was byte-identical and pixel-identical: zero differing pixels, maximum channel delta 0.

Conclusion: all three numerical figures are source-exact and remain pending external review.

## 24.6 DAG source and copy validation

- PhysioNet canonical PNG: `final-results/causal-outputs/outputs-physionet-forest/graph/physionet_causal_dag.png`; all six archived PNGs and the thesis copy share SHA-256 `67d545...e7c2`. All six pickles share `b742015668ee0def7d0cd7140faa56bfbd40c4be259ddcdd9194ef08de320351`.
- MIMIC canonical PNG: `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_dag.png`; all six archived PNGs and the thesis copy share SHA-256 `79fa7209...04d8`. All six pickles share `33e4531c971746f7374177c17c97ad1d06163f310bb77faf7d7c09dada6de19a`.
- Active sources: PhysioNet `825705e5...060ce`; MIMIC `4d5e61a5...e2490`. Under Python 3.10.20 / Matplotlib 3.8.4 / NumPy 1.26.4 / NetworkX 3.2.1 / Pillow 12.1.1, active rendering reproduced each canonical PNG byte-for-byte and pixel-for-pixel.
- PhysioNet: 30 nodes, 45 directed edges, acyclic. MIMIC: 36 nodes, 57 directed edges, acyclic. Node sets, edge sets, graph attributes, node types, and outcome endpoints exactly match the archived pickles.
- Exact node and edge CSVs are in `stage_5_2_figure_values/`. Thesis copies are exact canonical copies.
- DAG captions were minimally repaired: current reproducibility is distinguished from the unrecovered historical producing command; arrows remain explicitly assumed, not learned or validated.

## 24.7 MIMIC hash-name collision

- Exactly eight repository PNGs share SHA-256 `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8`:

  - `final-results/causal-outputs/outputs-mimic-forest-downsample/graph/mimic_causal_dag.png`
  - `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_dag.png`
  - `final-results/causal-outputs/outputs-mimic-linear-downsample/graph/mimic_causal_dag.png`
  - `final-results/causal-outputs/outputs-mimic-linear/graph/mimic_causal_dag.png`
  - `final-results/causal-outputs/outputs-mimic-pfn-downsample/graph/mimic_causal_dag.png`
  - `final-results/causal-outputs/outputs-mimic-pfn/graph/mimic_causal_dag.png`
  - `thesis-writing/figures-options/causal_dag_overview.png`
  - `thesis-writing/thesis/figures/mimic_causal_dag.png`
- Each is 5258×3940 RGBA with the same Matplotlib 3.8.4 metadata. The canonical PNG corresponds structurally and by active byte-identical rendering to the MIMIC graph pickle and expected title `MIMIC-III – Clinically Aggregated Causal DAG`.
- Supported explanation: **A**. `causal_dag_overview.png` is a duplicate copy/rename of the valid archived MIMIC DAG, not an independent optional design.
- The thesis MIMIC figure is valid. The optional-figure register note was minimally clarified; its `EXCLUDED_FROM_THESIS` status did not change. No blocking identity ambiguity remains.

## 24.8 Figure captions and references

- 110 LaTeX labels are present and all 110 are unique. There are zero unresolved references and zero duplicate labels.
- All five figures have unique labels and list-of-figures entries. The three result figures have one explicit prose reference each, at Chapter 10 lines 67, 105, and 237. The two DAGs have no separate prose `\ref`; they are placed immediately after the Chapter 7 graph introduction and resolve through their labels/list entries.
- Dataset, cohort, estimator, and evidence-role wording matches every figure. DAG captions state assumptions and current byte reproduction while preserving the historical-command limitation.
- Ranking captions remain descriptive/model-estimated and make no significance, clinical-importance, or population-average-effect claim.
- The direction caption was minimally repaired to identify CausalPFN as exploratory and retains the no-magnitude/no-equivalence/no-causal-validity boundary.

## 24.9 Visual readability

| Figure | Physical PDF page | PDF-to-XML image box (892×1262 canvas) | Readability and clipping | Limitation |
|---|---:|---|---|---|
| F-DAG-PHYSIONET | 57 (printed 43) | x103 y278 w687 h562 | Title/legend/arrows/caption visible; no clipping/overflow; grayscale node families distinguishable | Dense node labels limit normal-zoom use to orientation |
| F-DAG-MIMIC | 58 (printed 44) | x103 y302 w687 h515 | Title/legend/arrows/caption visible; no clipping/overflow; grayscale node families distinguishable | Higher density; orientation only, inventories/source are authority |
| F-RESULT-MIMIC-CATE | 84 (printed 70) | x92 y347 w708 h468 | Title, axis, 9 labels, values, zero line, caption readable; no clipping/collision | No uncertainty display |
| F-RESULT-PHYSIONET-CATE | 85 (printed 71) | x92 y323 w708 h512 | Title, axis, 10 labels, values, negative bar, zero line, caption readable; no clipping/collision | No uncertainty display |
| F-RESULT-DIRECTION-AGREEMENT | 91 (printed 77) | x92 y367 w708 h403 | Title, axis, groups, 9/9, 9/10, orange `1`, legend, caption readable; no clipping/collision | Direction only |

All captions are attached to the correct figure; page numbers are clear; blank area is float-page whitespace rather than missing content. Visual readability is not scientific validation.

## 24.10 Table inventory

- 33 compiled environments: 31 labelled tables plus 2 front-matter longtables.
- 8 numerical result tables and 25 non-numerical method/design/evidence/front-matter tables.
- All 31 labelled tables have list-of-tables entries; both front-matter nomenclature tables intentionally have no numbered caption.

## 24.11 Numerical tables

- Reconstructed eight Chapter 10 tables from checked sources. Machine comparison files contain 367 field-level comparisons: 6 population, 40 predictive, 36 MIMIC Forest, 40 PhysioNet Forest, 95 matching, 57 Linear, 57 PFN, and 36 robustness/status comparisons.
- 239 displayed numerical result cells/counts were checked, including caption cohort sizes; discrepancies: 0.
- Dataset, estimator, sampling, exposure, sign, rounding, ordering, status, and row counts match. Failed matching remains `--`/failed, missing intervals are not zero, PFN diagnostic skips remain intentional, robustness rows remain non-primary, datasets are not pooled, and normalized CATE is not substituted.
- No numerical table transcription repair was required.

## 24.12 Non-numerical tables

- All 25 non-numerical tables were checked row-by-row against active source, completed methods, approved literature, tracking logs, the result packet, or institutional-evidence boundaries named in the ledger.
- No cell represents planned work as completed, defaults as producing settings, DAGs as validated, estimates as unqualified causal facts, exact unarchived hardware/software, complete provenance, or current faculty-form approval.
- Discrepancies: 0. Content edits made during layout repair only replace slash/hyphen compounds with semantically identical breakable wording.

## 24.13 Table layout

- Rendered and inspected 44 physical PDF pages covering every table and longtable continuation. Captions, repeated headers, numbering, continuation, page breaks, minus signs, and significant digits are correct.
- Material overlap was found and repaired in Tables 5.3, 5.4, 7.4, 8.1, 8.2, 8.3, 9.2, and 9.3 through column allocation, scoped type/spacing, breakable paths/compounds, and two explicit long-identifier line breaks.
- Final rendered inspection shows no material table clipping or text overlap. Remaining TeX overfull warnings are nonfatal prose or narrow-cell box diagnostics without a rendered readability defect; no table was shrunk solely to silence warnings.

## 24.14 Appendix

- 16 materially distinct claims were audited. All are supported or explicitly bounded by the manifest, source packet, decision register, checksums, figure register, Stage 5.1 report, deferred fixes, or unresolved placeholders.
- The appendix does not imply clean-checkout rerun, recovered exact commands/configurations, complete raw/processed hashes, complete checkpoint/export or source-version lineage, governance approval, or clinical review.
- It contains no credentials, protected raw-data contents, obsolete stage chronology, or duplicated methods chapter. Overclaims: 0; repairs: 0.

## 24.15 Reproducibility artifacts

- `results_manifest.csv`: 1,389/1,389 referenced files exist and 1,389/1,389 hashes match.
- `results_checksums.sha256`: 1,418 paths exist; 1,413 current hashes match. Five post-snapshot differences are reconciled, not unexplained: `deferred_fixes.md`, `unresolved_placeholders.md`, and Chapter 10 evolved in authorized later stages; `main.pdf` is a mutable build output; `figure_selection_register.md` has the explicitly authorized Stage 5.2 duplicate-name clarification.
- The 1,421-row audit contains 1,415 `PASS`, 5 `EXPLAINED_POST_SNAPSHOT_EVOLUTION`, and 1 `PASS_WITH_DOCUMENTED_GAP`; blocking issues: 0.
- Generated figures are current and main-results roles agree; blocked/excluded legacy figures remain excluded; DAG source copies are documented; seminar slides are not numerical authority; failed paths and missing configurations retain explicit status.
- Exact producing configurations, some source versions/copy history, and predictive split/checkpoint/export lineage remain unresolved but consistently described as missing.

## 24.16 Files changed

- `thesis-writing/results/figure_selection_register.md`
- `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`
- `thesis-writing/thesis/chapters/07_causal_methodology.tex`
- `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex`
- `thesis-writing/thesis/chapters/09_experimental_design.tex`
- `thesis-writing/thesis/chapters/10_results.tex`
- `thesis-writing/thesis/main.pdf`
- `thesis-writing/logs/stage_5_2_appendix_audit.csv`
- `thesis-writing/logs/stage_5_2_figure_validation.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-edges.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-nodes.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-edges.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-nodes.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT-summary.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-MIMIC-CATE.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-PHYSIONET-CATE.csv`
- `thesis-writing/logs/stage_5_2_reproducibility_artifact_audit.csv`
- `thesis-writing/logs/stage_5_2_table_audit.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-analysis-populations.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-forest-mimic.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-forest-physionet.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-linear-comparison.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-matching-support.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-pfn-comparison.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-predictive-performance.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-robustness-summary.csv`
- `thesis-writing/logs/stage_5_2_external_review_summary.md`
- `thesis-writing/logs/stage_5_2_evidence_report.md`

Pre-existing user/worktree changes listed in Section 24.1 were preserved. No commit or push was performed.

## 24.17 Protected-file validation

- Protected files audited: 30.
- Byte-identical to initial Stage 5.2 baseline: 29.
- Authorized protected register clarification: 1 (`figure_selection_register.md`); selection status and artifact hashes unchanged.
- Unauthorized/prohibited protected changes: 0.
- All 14 checked CSVs, both literature metadata files, five thesis PNGs, result manifest/source/decision/checksum records, result generator, and both active graph sources retain baseline hashes.
- Figure hashes: PhysioNet DAG `67d545...e7c2`; MIMIC DAG `79fa72...04d8`; MIMIC result `e87b0d...b969`; PhysioNet result `1a64ad...4c87`; direction result `0f2b89...9ea`.

## 24.18 Final build

- Final commands: `latexmk -C`; `latexmk -xelatex main.tex`; `test -f main.pdf`; `pdfinfo main.pdf`.
- Final PDF: 111 A4 pages, 2,846,271 bytes, SHA-256 `192167724bba77199c19fbf0d11d3e14550a83aa79d80575b7880b41bf1cf34b`.
- Compilation: fatal errors 0; undefined citations 0; undefined references 0; duplicate labels 0; missing glyphs 0; Biber errors/warnings 0/0.
- Warning profile: 48 overfull hboxes, 1,157 underfull hboxes, 26 nonfatal duplicate longtable-destination warnings, one known `biblatex` warning that Hebrew is not a supported bibliography language, and no missing-character/bidi failure.
- Figure pages and every table page/continuation were rendered after repairs. All material readability defects found in this stage were repaired and re-rendered.
- `latexmk -c` is run after this report is written; `main.pdf` is retained.

## 24.19 Remaining gates

- Independent assistant figure approval.
- Supervisor ratification.
- Qualified clinical review of proxy rules and DAGs.
- CausalPFN primary source/version resolution.
- Exact producing configurations and complete source/archive-copy lineage.
- Raw/processed data provenance and authorized access records.
- Predictive split/checkpoint/export lineage.
- Dedicated overlap and balance diagnostics.
- Fairness/subgroup evaluation.
- External/prospective validation and deployment evaluation.
- LLM prompt-run and human-review provenance.
- Ethics, governance, consent, and institutional documentation.
- Title/English authorization, official administrative details, acknowledgements, and current faculty forms.

These gates remain outside Stage 5.2 and are not silently approved.

## 24.20 Readiness decision

`READY FOR EXTERNAL FIGURE VALIDATION`

This decision authorizes only the external figure-validation handoff. It does not declare readiness for Stage 5.3 or confer academic, clinical, supervisor, or institutional approval. All five ledger rows remain `external_review_status=PENDING_ASSISTANT_REVIEW`.

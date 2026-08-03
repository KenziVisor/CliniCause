# Stage 5.2 External Review Summary

This packet is for independent review. Codex completed a reproducibility and layout self-check only; it did **not** grant academic approval. Every included figure remains `external_review_status=PENDING_ASSISTANT_REVIEW`.

## Figures

### F-DAG-PHYSIONET

- **Thesis path:** `thesis-writing/thesis/figures/physionet_causal_dag.png`
- **Chapter and label:** Chapter 7; `fig:physionet-causal-dag`
- **PDF page and bounding box:** 57 (printed 43); x=103, y=278, w=687, h=562 on 892×1262 audit canvas
- **Current hash and dimensions:** `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2`; 2200×1800 RGBA
- **Exact source:** `final-results/causal-outputs/outputs-physionet-forest/graph/physionet_causal_dag.png` (`67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2`)
- **Generator or archived-artifact provenance:** `causal-irregular-time-series/src/physionet2012_causal_graph.py` (`825705e5d4a433cd5e0b7717e3ad316b3b17a4ba98b09d18cdbb7dcafe8060ce`); BYTE_IDENTICAL
- **Input hash:** `final-results/causal-outputs/outputs-physionet-forest/graph/physionet_causal_graph.pkl` (`b742015668ee0def7d0cd7140faa56bfbd40c4be259ddcdd9194ef08de320351`)
- **Filters:** N/A
- **Expected displayed values:** 30 exact node labels and 45 directed arrows; graph inventory files are authoritative. Full exact inventory: `F-DAG-PHYSIONET-nodes.csv; F-DAG-PHYSIONET-edges.csv`.
- **Expected labels:** 30 exact graph node identifiers; see node inventory
- **Expected title:** PhysioNet 2012 – Causal DAG
- **Expected axis and legend:** axis `none`; legend `background; latent; observed`; axis rule `axes hidden; renderer layout bounds`
- **Regeneration result:** BYTE_IDENTICAL_ACTIVE_RENDER
- **Byte/pixel comparison:** BYTE_IDENTICAL; 0 differing pixels
- **Caption boundary:** Assumed directions; source-code definitions; historical producing command unrecovered.
- **Known limitation:** Dense node labels; interpretable at normal zoom as an orientation figure, not as the exact node/edge authority or scientific validation. No prose cross-reference beyond placement/list-of-figures entry.
- **Codex self-check:** PASS_WITH_PROVENANCE_QUALIFICATION; final-PDF title/caption attachment, clipping, page number, overflow, and grayscale interpretation inspected.
- **External review status:** `PENDING_ASSISTANT_REVIEW`
- **Blocking question:** No Stage 5.2 self-check blocker. Independently confirm the displayed values/structure, evidence boundary, and orientation-only acceptability of dense DAGs.

### F-DAG-MIMIC

- **Thesis path:** `thesis-writing/thesis/figures/mimic_causal_dag.png`
- **Chapter and label:** Chapter 7; `fig:mimic-causal-dag`
- **PDF page and bounding box:** 58 (printed 44); x=103, y=302, w=687, h=515 on 892×1262 audit canvas
- **Current hash and dimensions:** `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8`; 5258×3940 RGBA
- **Exact source:** `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_dag.png` (`79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8`)
- **Generator or archived-artifact provenance:** `causal-irregular-time-series/src/mimiciii_causal_graph.py` (`4d5e61a59a0d867d578dde014dce42b2cc8f5b2a03aa169fc6354532b02e2490`); BYTE_IDENTICAL
- **Input hash:** `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_graph.pkl` (`33e4531c971746f7374177c17c97ad1d06163f310bb77faf7d7c09dada6de19a`)
- **Filters:** N/A
- **Expected displayed values:** 36 exact node labels and 57 directed arrows; graph inventory files are authoritative. Full exact inventory: `F-DAG-MIMIC-nodes.csv; F-DAG-MIMIC-edges.csv`.
- **Expected labels:** 36 exact graph node identifiers; see node inventory
- **Expected title:** MIMIC-III – Clinically Aggregated Causal DAG
- **Expected axis and legend:** axis `none`; legend `background; latent; observed`; axis rule `axes hidden; renderer layout bounds`
- **Regeneration result:** BYTE_IDENTICAL_ACTIVE_RENDER
- **Byte/pixel comparison:** BYTE_IDENTICAL; 0 differing pixels
- **Caption boundary:** Assumed directions; source-code definitions; historical producing command unrecovered.
- **Known limitation:** Dense node labels and arrows; usable only as an orientation figure. Exact historical producing command remains unrecovered. No prose cross-reference beyond placement/list-of-figures entry.
- **Codex self-check:** PASS_WITH_PROVENANCE_QUALIFICATION; final-PDF title/caption attachment, clipping, page number, overflow, and grayscale interpretation inspected.
- **External review status:** `PENDING_ASSISTANT_REVIEW`
- **Blocking question:** No Stage 5.2 self-check blocker. Independently confirm the displayed values/structure, evidence boundary, and orientation-only acceptability of dense DAGs.

### F-RESULT-MIMIC-CATE

- **Thesis path:** `thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png`
- **Chapter and label:** Chapter 10; `fig:results-mimic-forest-ranking`
- **PDF page and bounding box:** 84 (printed 70); x=92, y=347, w=708, h=468 on 892×1262 audit canvas
- **Current hash and dimensions:** `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969`; 3360×2220 RGBA
- **Exact source:** `thesis-writing/thesis/figures/results_mimic_forest_original_cate_ranking.png` (`e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969`)
- **Generator or archived-artifact provenance:** `thesis-writing/results/generate_stage_4_6B_main_figures.py` (`f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af`); SELF_CANONICAL_CHECKED_OUTPUT
- **Input hash:** `thesis-writing/results/checked_cate_candidates.csv` (`594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835`)
- **Filters:** dataset=mimic; estimator=CausalForestDML; sampling_condition=original; selection_status=PRIMARY_MAIN_TEXT
- **Expected displayed values:** 0.220, 0.161, 0.098, 0.091, 0.062, 0.036, 0.034, 0.021, 0.020 in descending source order. Full exact inventory: `F-RESULT-MIMIC-CATE.csv`.
- **Expected labels:** Cardiac Strain / (LAT_CARDIAC_STRAIN); Inflammation Sepsis / (LAT_INFLAMMATION_SEPSIS); Hepatic Coag Dysfunction / (LAT_HEPATIC_COAG_DYSFUNCTION); Renal Dysfunction / (LAT_RENAL_DYSFUNCTION); Global Severity / (LAT_GLOBAL_SEVERITY); Respiratory Failure / (LAT_RESPIRATORY_FAILURE); Neurologic Dysfunction / (LAT_NEUROLOGIC_DYSFUNCTION); Shock / (LAT_SHOCK); Metabolic Derangement / (LAT_METABOLIC_DERANGEMENT)
- **Expected title:** MIMIC-III — CausalForestDML / Original cohort
- **Expected axis and legend:** axis `Mean model-estimated CATE`; legend `none`; axis rule `left=-0.026443; right=0.249002 by generator padding rule`
- **Regeneration result:** BYTE_IDENTICAL_ISOLATED_REGENERATION
- **Byte/pixel comparison:** BYTE_IDENTICAL; 0 differing pixels; max channel delta 0
- **Caption boundary:** Mean model-estimated CATE; no significance, clinical-importance, or population-average-effect claim.
- **Known limitation:** No intervals or significance display; descriptive model-estimated ordering only.
- **Codex self-check:** PASS_WITH_CAUSAL_QUALIFICATION; final-PDF title/caption attachment, clipping, page number, overflow, and grayscale interpretation inspected.
- **External review status:** `PENDING_ASSISTANT_REVIEW`
- **Blocking question:** No Stage 5.2 self-check blocker. Independently confirm the displayed values/structure, evidence boundary, and orientation-only acceptability of dense DAGs.

### F-RESULT-PHYSIONET-CATE

- **Thesis path:** `thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png`
- **Chapter and label:** Chapter 10; `fig:results-physionet-forest-ranking`
- **PDF page and bounding box:** 85 (printed 71); x=92, y=323, w=708, h=512 on 892×1262 audit canvas
- **Current hash and dimensions:** `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87`; 3360×2430 RGBA
- **Exact source:** `thesis-writing/thesis/figures/results_physionet_forest_original_cate_ranking.png` (`1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87`)
- **Generator or archived-artifact provenance:** `thesis-writing/results/generate_stage_4_6B_main_figures.py` (`f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af`); SELF_CANONICAL_CHECKED_OUTPUT
- **Input hash:** `thesis-writing/results/checked_cate_candidates.csv` (`594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835`)
- **Filters:** dataset=physionet; estimator=CausalForestDML; sampling_condition=original; selection_status=PRIMARY_MAIN_TEXT
- **Expected displayed values:** 0.120, 0.112, 0.108, 0.091, 0.082, 0.078, 0.072, 0.065, 0.011, -0.014 in descending source order. Full exact inventory: `F-RESULT-PHYSIONET-CATE.csv`.
- **Expected labels:** Renal Dysfunction / (LAT_RENAL_DYSFUNCTION); Cardiac Injury Strain / (LAT_CARDIAC_INJURY_STRAIN); Global Severity / (LAT_GLOBAL_SEVERITY); Hepatic Dysfunction / (LAT_HEPATIC_DYSFUNCTION); Neurologic Dysfunction / (LAT_NEUROLOGIC_DYSFUNCTION); Metabolic Derangement / (LAT_METABOLIC_DERANGEMENT); Inflammation Sepsis Burden / (LAT_INFLAMMATION_SEPSIS_BURDEN); Respiratory Failure / (LAT_RESPIRATORY_FAILURE); Coag Heme Dysfunction / (LAT_COAG_HEME_DYSFUNCTION); Shock / (LAT_SHOCK)
- **Expected title:** PhysioNet 2012 — CausalForestDML / Original cohort
- **Expected axis and legend:** axis `Mean model-estimated CATE`; legend `none`; axis rule `left=-0.029914; right=0.137431 by generator padding rule`
- **Regeneration result:** BYTE_IDENTICAL_ISOLATED_REGENERATION
- **Byte/pixel comparison:** BYTE_IDENTICAL; 0 differing pixels; max channel delta 0
- **Caption boundary:** Mean model-estimated CATE; no significance, clinical-importance, or population-average-effect claim.
- **Known limitation:** No intervals or significance display; negative shock bar and zero line must remain visible.
- **Codex self-check:** PASS_WITH_CAUSAL_QUALIFICATION; final-PDF title/caption attachment, clipping, page number, overflow, and grayscale interpretation inspected.
- **External review status:** `PENDING_ASSISTANT_REVIEW`
- **Blocking question:** No Stage 5.2 self-check blocker. Independently confirm the displayed values/structure, evidence boundary, and orientation-only acceptability of dense DAGs.

### F-RESULT-DIRECTION-AGREEMENT

- **Thesis path:** `thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png`
- **Chapter and label:** Chapter 10; `fig:results-three-estimator-direction`
- **PDF page and bounding box:** 91 (printed 77); x=92, y=367, w=708, h=403 on 892×1262 audit canvas
- **Current hash and dimensions:** `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea`; 3060×1740 RGBA
- **Exact source:** `thesis-writing/thesis/figures/results_original_three_estimator_direction_agreement.png` (`0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea`)
- **Generator or archived-artifact provenance:** `thesis-writing/results/generate_stage_4_6B_main_figures.py` (`f5bc6fc877a87d8ac757c3c4085035e9dc96d68b5d27488c6f4f8ac2984717af`); SELF_CANONICAL_CHECKED_OUTPUT
- **Input hash:** `thesis-writing/results/checked_cate_candidates.csv` (`594795869ece8d6c32ddc6b48c21b26c7073cdb472bd1e813352446b24ec5835`)
- **Filters:** sampling_condition=original; estimators=CausalForestDML+LinearDML+CausalPFN; exact join dataset+treatment
- **Expected displayed values:** MIMIC 9/9 concordant; PhysioNet 9/10 concordant plus 1 discordant; overall 18/19; exception LAT_SHOCK with Forest/Linear negative and PFN positive. Full exact inventory: `F-RESULT-DIRECTION-AGREEMENT.csv; F-RESULT-DIRECTION-AGREEMENT-summary.csv`.
- **Expected labels:** MIMIC-III; PhysioNet 2012
- **Expected title:** Original-cohort direction agreement across three estimators / 18/19 overall / Exception: PhysioNet LAT_SHOCK (Forest/Linear negative; CausalPFN positive)
- **Expected axis and legend:** axis `Dataset–exposure comparisons (count)`; legend `Concordant across all three; Not concordant across all three`; axis rule `x=0 to 10.8; y categorical`
- **Regeneration result:** BYTE_IDENTICAL_ISOLATED_REGENERATION
- **Byte/pixel comparison:** BYTE_IDENTICAL; 0 differing pixels; max channel delta 0
- **Caption boundary:** Direction only; no magnitude, uncertainty, estimator-equivalence, or causal-validity claim.
- **Known limitation:** Direction-only aggregation; no magnitude, uncertainty, equivalence, or causal-validity claim.
- **Codex self-check:** PASS_WITH_DIRECTION_ONLY_QUALIFICATION; final-PDF title/caption attachment, clipping, page number, overflow, and grayscale interpretation inspected.
- **External review status:** `PENDING_ASSISTANT_REVIEW`
- **Blocking question:** No Stage 5.2 self-check blocker. Independently confirm the displayed values/structure, evidence boundary, and orientation-only acceptability of dense DAGs.

## Tables

Each compiled `table` or `longtable` is listed; “match” refers to its exact named source, not a general assertion. Numerical comparison CSVs are under `stage_5_2_table_values/`.

| Table ID | Exact source | Row/value match | Layout | Repair |
|---|---|---|---|---|
| `tab:introduction-contributions` | thesis-writing/planning/chapter_evidence_map.md; thesis chapters; checked result packet; Stage 5.1 report | 6 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:background-datasets` | thesis-writing/literature/metadata/catalog.csv; official dataset citations in references.bib; preprocessing contracts | 2 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:background-model-families` | approved literature in references.bib; active predictive source; archived training artifacts | 5 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:data-contracts` | causal-irregular-time-series/src/preprocess_*.py; causal-irregular-time-series/src/cate_estimation.py; STraTS data loaders | 5 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:llm-prompt-artifact-provenance` | design prompt/document artifacts named in the table; stage_4_3_llm_prompt_repair_report.md | 5 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:proxy-source-types` | active proxy taggers; prediction export code; majority-vote implementation | 3 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:physionet-proxy-definitions` | causal-irregular-time-series/src/tagging_latent_variables_physionet.py | 11 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Column allocation and long identifier wrap repaired. |
| `tab:mimic-proxy-definitions` | causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py | 10 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Column allocation and long identifier wrap repaired. |
| `tab:predictive-model-comparison` | STraTS and causal-router active model sources; checked_predictive_exports.csv | 5 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:prediction-export-schema` | STraTS prediction export code; split_predicted_latent_tags.py; router.py | 3 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:dag-node-families` | causal-irregular-time-series/src/physionet2012_causal_graph.py; causal-irregular-time-series/src/mimiciii_causal_graph.py; archived graph pickles | 6 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:adjustment-set-logic` | causal-irregular-time-series/src/cate_estimation.py; project DAG helper implementation | 7 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:causal-assumptions` | implemented DAG/matching/CATE methods; approved causal-method literature | 10 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:causal-estimator-methods` | matching_causal_effect.py; cate_estimation.py; causal_pfn.py; orchestrator records | 4 rows; N/A; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | First-column allocation repaired. |
| `tab:overlap-support-design` | matching_causal_effect.py; checked_matching_results.csv; checked_matching_failures.csv | 5 rows; N/A; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Breakable paths and compound wording, smaller type, and column spacing repaired. |
| `tab:sensitivity-diagnostic-design` | cate_estimation.py; saved-CATE analysis source; checked_sensitivity_candidates.csv | 7 rows; N/A; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Breakable compound wording, smaller type, and spacing repaired. |
| `tab:permutation-reproducibility-design` | permutation source; config validators; archived run_summary.json; results_manifest.csv | 5 rows; N/A; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Breakable path/compound wording, column allocation, smaller type, and spacing repaired. |
| `tab:predictive-experimental-matrix` | checked_predictive_exports.csv; checked_predictive_metrics.csv; archived training summaries | 2 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:causal-experimental-matrix` | experiment_inventory.csv and 12 archived run_summary.json records; active orchestrator | 4 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Column allocation and break opportunity in CausalForestDML repaired. |
| `tab:reproducibility-status` | results_manifest.csv; results_source_packet.md; results_decision_register.md | 8 rows; N/A; textual cells PASS_SOURCE_CHECKED | REPAIRED_PASS | Breakable provenance and hardware wording, smaller type, and spacing repaired. |
| `tab:result-admission-policy` | results_decision_register.md; checked result selection/admission fields | 4 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-analysis-populations` | thesis-writing/results/checked_cate_candidates.csv | 2 rows; 2/2 result-value cells; 6 total machine comparisons in stage_5_2_table_values/T-results-analysis-populations.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-predictive-performance` | thesis-writing/results/checked_predictive_metrics.csv | 10 rows; 40/40 result-value cells; 40 total machine comparisons in stage_5_2_table_values/T-results-predictive-performance.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-forest-mimic` | thesis-writing/results/checked_cate_candidates.csv | 9 rows; 19/19 result-value cells; 36 total machine comparisons in stage_5_2_table_values/T-results-forest-mimic.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-forest-physionet` | thesis-writing/results/checked_cate_candidates.csv | 10 rows; 21/21 result-value cells; 40 total machine comparisons in stage_5_2_table_values/T-results-forest-physionet.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-matching-support` | checked_matching_results.csv; checked_matching_failures.csv | 19 rows; 60/60 result-value cells; 95 total machine comparisons in stage_5_2_table_values/T-results-matching-support.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-linear-comparison` | thesis-writing/results/checked_cate_candidates.csv | 19 rows; 38/38 result-value cells; 57 total machine comparisons in stage_5_2_table_values/T-results-linear-comparison.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-pfn-comparison` | thesis-writing/results/checked_cate_candidates.csv | 19 rows; 19/19 result-value cells; 57 total machine comparisons in stage_5_2_table_values/T-results-pfn-comparison.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:results-robustness-summary` | checked_matching_results.csv; checked_matching_failures.csv; checked_sensitivity_candidates.csv; checked_permutation_candidates.csv | 12 rows; 40/40 result-value cells; 36 total machine comparisons in stage_5_2_table_values/T-results-robustness-summary.csv; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:discussion-rq-answers` | Chapter 10 checked tables; Stage 5.1 RQ/contribution matrix; chapter_evidence_map.md | 8 rows; ALL numeric thresholds/count-like cells checked against named source; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `tab:discussion-limitations` | results_source_packet.md; results_decision_register.md; Stage 5.1 audit; methods/results evidence | 17 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `T-FRONT-ABBREVIATIONS` | thesis chapters and definitions; active source; approved evidence records | 17 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |
| `T-FRONT-NOTATION` | thesis chapters and definitions; active source; approved evidence records | 15 rows; N/A; textual cells PASS_SOURCE_CHECKED | PASS | No unreconciled cell or layout issue. |

## Handoff decision

`READY FOR EXTERNAL FIGURE VALIDATION`

This is not readiness for Stage 5.3 and is not assistant, supervisor, clinical, or institutional approval.

# Stage 4.1 Evidence Report

Date: 2026-07-14

Scope: implement `prompt.txt` Stage 4.1 by drafting Chapter 3 and Chapter 4 from audited repository evidence, updating placeholder/deferred-fix logs, compiling the thesis, and recording evidence.

## 11.1 Git State

Current branch at start of work: `main`.

Inspected commit:

```text
a1e7634 step 4.0
```

Recent history inspected:

```text
a1e7634 step 4.0
6c83048 stage 3 completion
350c30a stage 2 completion
```

Initial `git status --short` before Stage 4.1 edits already contained unrelated local changes:

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
 M tmp_verify_router.py
```

Stage 4.1 source/log edits:

```text
thesis-writing/thesis/chapters/03_problem_definition_study_design.tex
thesis-writing/thesis/chapters/04_data_preprocessing.tex
thesis-writing/logs/unresolved_placeholders.md
thesis-writing/logs/deferred_fixes.md
thesis-writing/logs/stage_4_1_evidence_report.md
```

Generated build artifact kept for review:

```text
thesis-writing/thesis/main.pdf
```

Expected final `git status --short` after report creation and LaTeX auxiliary cleanup:

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
 M thesis-writing/logs/deferred_fixes.md
 M thesis-writing/logs/unresolved_placeholders.md
 M thesis-writing/thesis/chapters/03_problem_definition_study_design.tex
 M thesis-writing/thesis/chapters/04_data_preprocessing.tex
 M tmp_verify_router.py
?? thesis-writing/logs/stage_4_1_evidence_report.md
?? thesis-writing/thesis/main.pdf
```

## 11.2 Toolchain

Verified tool paths:

```text
/usr/bin/pdfinfo
/usr/bin/pdftotext
/usr/bin/latexmk
/usr/bin/xelatex
/usr/bin/biber
```

Verified versions:

```text
pdfinfo version 24.02.0
pdftotext version 24.02.0
Latexmk, John Collins, 31 Jan. 2024. Version 4.83
XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian)
biber version: 2.19
```

No package or font warning blocks were present in the final `main.log` scan. The PDF conversion step emitted nonfatal `xdvipdfmx:warning: Object @page.i already defined.` messages and still wrote `main.pdf` successfully.

## 11.3 Baseline Compilation

Baseline build working directory:

```text
thesis-writing/thesis
```

Baseline commands:

```bash
latexmk -C
latexmk -xelatex main.tex
```

Baseline status: successful. `latexmk` ran XeLaTeX and Biber and generated `main.pdf`.

Baseline `pdfinfo main.pdf` summary:

```text
Pages: 33
Page size: 595.28 x 841.89 pts (A4)
File size: 50225 bytes
CreationDate: Tue Jul 14 08:38:29 2026 IDT
```

Baseline log scan found no fatal errors. The notable nonfatal warning was an empty bibliography because Chapter 3 and Chapter 4 had not yet introduced citations.

No compile repair was required before drafting.

## 11.4 Files Inspected

BGU/faculty requirements:

- `thesis-writing/general-instructions.pdf`
- `thesis-writing/bgu-requirements-map.md`

Stage 4.0 thesis skeleton and logs:

- `thesis-writing/logs/stage_4_0_setup_report.md`
- `thesis-writing/logs/unresolved_placeholders.md`
- `thesis-writing/logs/deferred_fixes.md`
- `thesis-writing/thesis/main.tex`
- `thesis-writing/thesis/latexmkrc`
- `thesis-writing/thesis/README.md`
- `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex`
- `thesis-writing/thesis/chapters/04_data_preprocessing.tex`

Planning files:

- `thesis-writing/planning/thesis_story.md`
- `thesis-writing/planning/thesis_outline.md`
- `thesis-writing/planning/chapter_evidence_map.md`
- `thesis-writing/planning/terminology_and_notation.md`
- `thesis-writing/planning/citation_plan.md`
- `thesis-writing/planning/table_plan.md`
- `thesis-writing/planning/figure_plan.md`
- `thesis-writing/planning/writing_order.md`
- `thesis-writing/planning/stage4_prompt_queue.md`

Audit/evidence files:

- `thesis-writing/audit/repository_map.md`
- `thesis-writing/audit/evidence_inventory.md`
- `thesis-writing/audit/experiment_inventory.csv`
- `thesis-writing/audit/terminology_map.md`
- `thesis-writing/audit/unresolved_questions.md`
- `thesis-writing/audit/claim_evidence_ledger.csv`

Literature metadata:

- `thesis-writing/literature/README.md`
- `thesis-writing/literature/metadata/catalog.csv`
- `thesis-writing/literature/metadata/references.bib`

Root and orchestration files:

- `README.md`
- `SCRIPTS.md`
- `router.py`

Causal repository files:

- `causal-irregular-time-series/README.md`
- `causal-irregular-time-series/SCRIPTS.md`
- `causal-irregular-time-series/src/preprocess_physionet_2012.py`
- `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`
- `causal-irregular-time-series/src/preprocess_mimic_iii_large_contract.py`
- `causal-irregular-time-series/src/majority_vote_latents.py`
- `causal-irregular-time-series/src/split_predicted_latent_tags.py`
- `causal-irregular-time-series/src/mortality_prediction_using_latents.py`
- `causal-irregular-time-series/src/matching_causal_effect.py`
- `causal-irregular-time-series/src/cate_estimation.py`
- `causal-irregular-time-series/configs/physionet-global-variables.csv`
- `causal-irregular-time-series/configs/mimic-global-variables.csv`

STraTS files:

- `STraTS/SCRIPTS.md`
- `STraTS/src/dataset.py`
- `STraTS/src/dataset_pretrain.py`
- `STraTS/src/main.py`
- `STraTS/src/preprocess_physionet_2012.py`
- `STraTS/src/preprocess_mimic_iii.py`
- inspected wrapper/run scripts found through `rg --files STraTS`

## 11.5 Claims and Evidence by Drafted Section

C3.1, Units, Time Horizons, and Data Objects:

- Claim drafted: the analysis unit is a time-series record or ICU stay normalized to `ts_id`, not a guaranteed person identifier.
- Evidence: PhysioNet preprocessing renames `RecordID` to `ts_id`; MIMIC preprocessing normalizes ICU-stay identifiers to `ts_id`; STraTS loader accepts `ts_id`, `icustay_id`, and `ICUSTAY_ID` and canonicalizes to `ts_id`.
- Claim drafted: irregular observations are long-format events with `ts_id`, `minute`, `variable`, and `value`.
- Evidence: causal preprocessing contract and router validation require those columns.
- Claim drafted: missingness and measurement frequency are interpretive risks, not causal conclusions.
- Evidence: repository uses irregular clinical events without a complete measurement grid.

C3.2, Prediction Task:

- Claim drafted: prediction is multi-label proxy-state prediction.
- Evidence: STraTS supervised loader reads a latent-label CSV, treats all non-`ts_id` columns as targets, and exports probability plus binary proxy-state columns.
- Claim drafted: proxy labels are weak/rule-derived labels, not chart-adjudicated diagnoses.
- Evidence: planning terminology and audit warnings require conservative proxy-state wording; no manual adjudication artifact was found.
- Claim drafted: mortality in `oc` is not the supervised proxy-label target.
- Evidence: STraTS loader joins a separate latent CSV for labels; causal `oc` stores `in_hospital_mortality`.

C3.3, Causal Question, Exposures, Outcome, Estimands, Assumptions:

- Claim drafted: the causal setting is retrospective and observational.
- Evidence: no randomized assignment or intervention-generation code exists in the inspected repository.
- Claim drafted: `LAT_*` columns are proxy-state exposures or modeled treatment variables unless later defined as manipulable interventions.
- Evidence: configs and causal scripts use `treatment` terminology for selected binary latent/proxy columns; planning files require conservative exposure wording.
- Claim drafted: causal interpretation requires graph, consistency, exchangeability, positivity/overlap, measurement, and unmeasured-confounding assumptions.
- Evidence: DAG-guided matching/CATE scripts and literature plan support assumption-based causal framing, not automatic identification.

C4.1, PhysioNet 2012 Pipeline:

- Claim drafted: PhysioNet 2012 is used as an ICU mortality-prediction challenge dataset.
- Evidence: `silva2012physionet` citation and preprocessing source.
- Claim drafted: preprocessing traverses `set-a`, `set-b`, and `set-c`, filters missing parameters, skips very small records, removes negative values, converts `HH:MM` to minutes, maps `In-hospital_death` to `in_hospital_mortality`, deduplicates, and one-hot-style encodes ICU type.
- Evidence: `causal-irregular-time-series/src/preprocess_physionet_2012.py`.
- Claim drafted: final cohort count is not asserted.
- Evidence: raw data and processed pickles are not tracked in the repository.

C4.2, MIMIC-III Pipeline:

- Claim drafted: MIMIC-III is used as the second ICU data source and is transformed into stay-level time-series examples.
- Evidence: `johnson2016mimiciii`, `harutyunyan_2019_mimiciii_benchmark`, MIMIC preprocessing source.
- Claim drafted: source tables include `ICUSTAYS`, `PATIENTS`, `ADMISSIONS`, `CHARTEVENTS`, `LABEVENTS`, `OUTPUTEVENTS`, `INPUTEVENTS_CV`, and `INPUTEVENTS_MV`.
- Evidence: `preprocess_mimic_iii_large.py`.
- Claim drafted: canonical export uses `ts_id`, `minute`, `variable`, `value` in `ts` and `ts_id`, `length_of_stay`, `in_hospital_mortality`, `subset` in `oc`.
- Evidence: `preprocess_mimic_iii_large_contract.py`.
- Claim drafted: active source has an outcome-column reproducibility issue.
- Evidence: active script reads `ADMISSIONS.csv` with `DEATHTIME`, while `build_canonical_oc` requires `HOSPITAL_EXPIRE_FLAG`.

C4.3, STraTS Split-Aware Artifacts Versus Causal Artifacts:

- Claim drafted: STraTS and causal repositories use different processed-pickle contracts.
- Evidence: STraTS loader expects five objects; causal preprocessing and router validation expect three objects.
- Claim drafted: supervised STraTS joins latent-label CSVs after ID normalization and validates missing/duplicate labels.
- Evidence: `STraTS/src/dataset.py`.
- Claim drafted: prediction export writes `ts_id`, probability columns, and thresholded binary columns.
- Evidence: `STraTS/src/main.py`.
- Claim drafted: the parent router can synthesize STraTS split payloads from causal artifacts, but this does not prove final archived provenance.
- Evidence: `router.py` bridge code and audit unresolved provenance questions.

## 11.6 Artifact Contracts

Causal processed artifact:

```text
[ts, oc, ts_ids]
```

- `ts`: long event table requiring `ts_id`, `minute`, `variable`, and `value`.
- `oc`: outcome/covariate table keyed by `ts_id`; expected mortality outcome is `in_hospital_mortality`.
- `ts_ids`: identifier collection derived from normalized IDs represented in `ts`.
- Main use in this thesis: rule-based tagging, mortality/proxy analysis, matching, and CATE estimation.

STraTS processed artifact:

```text
[events, oc, train_ids, val_ids, test_ids]
```

- `events`: event table with identifiers normalized by the loader to `ts_id`.
- `oc`: outcome/covariate table carried with split-aware data.
- `train_ids`, `val_ids`, `test_ids`: explicit split identifier arrays.
- Main use in this thesis: predictive training, pretraining, and prediction export.

Latent-label CSV:

- keyed by `ts_id` after normalization;
- all non-`ts_id` columns become supervised proxy-label targets in STraTS;
- mortality in `oc` is not the supervised proxy-label target;
- prediction export includes `ts_id`, one probability column per proxy state, and one thresholded binary column per proxy state;
- downstream causal scripts require binary latent/proxy columns and align them to `oc` by `ts_id`.

Split representation:

- causal artifacts are unsplit and carry a single ID collection;
- STraTS artifacts are split-aware and carry train/validation/test ID arrays;
- router bridging can synthesize split arrays by seeded shuffle, but final archive-copy provenance remains unresolved.

## 11.7 Citations Used

- `pearl_1995_causal_diagrams`: supports DAG/causal-graph framing and the need for assumptions.
- `hernan_robins_2016_target_trial`: supports conservative target-trial/observational causal framing.
- `hernan_taubman_2008_well_defined_interventions`: supports caution around ill-defined interventions.
- `silva2012physionet`: supports the PhysioNet 2012 dataset description.
- `johnson2016mimiciii`: supports the MIMIC-III dataset description.
- `harutyunyan_2019_mimiciii_benchmark`: supports benchmark-style ICU time-series preprocessing context.

Citation validation:

- `references.bib` contains all six keys.
- Final `main.log` scan found no undefined citation warnings.

## 11.8 Placeholders

Resolved/replaced in Stage 4.1:

- C3.1 `[STAGE 4 DRAFT REQUIRED]`
- C3.2 `[STAGE 4 DRAFT REQUIRED]`
- C3.3 `[STAGE 4 DRAFT REQUIRED]`
- C4.1 `[STAGE 4 DRAFT REQUIRED]`
- C4.2 `[STAGE 4 DRAFT REQUIRED]`
- C4.3 `[STAGE 4 DRAFT REQUIRED]`
- generic C4 result/validation/figure placeholders replaced with precise, evidence-tied placeholders

Remaining in Chapter 3 and Chapter 4:

- `[SUPERVISOR DECISION REQUIRED: final estimand wording for proxy-state exposures and aggregated CATE summaries]`
- `[RESULT REQUIRED: final number of included PhysioNet records after preprocessing]`
- `[RESULT REQUIRED: final number of included MIMIC-III ICU stays after preprocessing]`
- `[FIGURE REQUIRED: audited dataflow diagram linking raw data, causal artifacts, STraTS artifacts, proxy labels, and causal analysis]`
- `[VALIDATION REQUIRED: checksums for processed PhysioNet and MIMIC-III dataset artifacts]`
- `[VALIDATION REQUIRED: provenance of train/validation/test split generation for final STraTS artifacts]`

The unresolved placeholder register was updated with these resolutions and remaining gates.

## 11.9 Deferred Fixes

Resolved:

- `DF-4.0-001`: TeX/PDF tooling blocker is resolved. `latexmk`, `xelatex`, `biber`, `pdfinfo`, and `pdftotext` are installed and working.

New Stage 4.1 deferred fixes:

- `DF-4.1-001`: MIMIC preprocessing outcome-column mismatch between active source and canonical helper.
- `DF-4.1-002`: final STraTS split-aware artifact and prediction-archive provenance remains incomplete.
- `DF-4.1-003`: `thesis-writing/thesis/README.md` still contains stale Stage 4.0 text saying TeX tools are unavailable.

Previously known unresolved issues still relevant:

- `DF-4.0-002`: final BGU/faculty forms and thesis-language approval still required.
- `DF-4.0-003`: CausalPFN citation unresolved if it becomes central.
- `DF-4.0-004`: final result archive lacks tracked manifest.
- `DF-4.0-005`: exact numbered config mapping unresolved.
- `DF-4.0-006`: raw/processed data artifacts are external or absent.
- `DF-4.0-007`: dedicated overlap/support diagnostics not found.
- `DF-4.0-008`: unrelated pre-existing worktree modifications remain.

## 11.10 Final Compilation

Final build working directory:

```text
thesis-writing/thesis
```

Final build commands:

```bash
latexmk -C
latexmk -xelatex main.tex
```

Auxiliary cleanup after recording final diagnostics:

```bash
latexmk -c
```

Final build status: successful. XeLaTeX, Biber, additional XeLaTeX reruns, and `xdvipdfmx` completed.

Final PDF:

```text
thesis-writing/thesis/main.pdf
Pages: 38
Page size: 595.28 x 841.89 pts (A4)
File size: 100915 bytes
CreationDate: Tue Jul 14 08:49:53 2026 IDT
```

Final validation scans:

- no fatal errors;
- no undefined citations;
- no undefined references;
- no duplicate labels;
- `\label{tab:data-contracts}` is unique;
- no risky banned wording matches in edited chapters for `ground truth`, `verified diagnosis`, `true diagnosis`, `causes mortality`, `clinically actionable`, `randomized`, `intervention effect`, `treatment recommendation`, `learned causal graph`, `complete-case guarantee`, or `no leakage`.

Remaining nonfatal layout warnings from final `main.log` scan:

```text
Underfull \hbox (badness 10000) in paragraph at lines 55--56
Underfull \hbox (badness 10000) in paragraph at lines 58--58
Underfull \hbox (badness 4072) in paragraph at lines 59--59
Overfull \hbox (5.34378pt too wide) in paragraph at lines 83--83
Overfull \hbox (20.22945pt too wide) in paragraph at lines 83--83
```

The underfull warnings are from narrow table cells in Chapter 4. The overfull warnings are bibliography line breaks. They do not block PDF generation.

## 11.11 Readiness

Status: ready with non-blocking warnings.

Chapter 3 and Chapter 4 are now drafted at Stage 4.1 scope with conservative causal and clinical wording, explicit artifact contracts, citations, and retained evidence-gated placeholders. The thesis compiles successfully to a 38-page A4 PDF. Remaining blockers are evidence/provenance or supervisor-decision gates, not LaTeX build failures.

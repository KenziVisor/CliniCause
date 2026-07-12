# Stage 2 Validation Report

## 1. Scope and Method

| Field | Value |
| --- | --- |
| Repository root | `/mnt/c/Users/kobik/Desktop/הנדסת מערכות תקשורת/תואר שני/תזה/code/CliniCause` |
| Branch | `main` |
| Parent commit inspected | `88568e4bf42c8d717fd12e2238aa90b6467cfc0d` |
| Working-tree state | Dirty before Stage 2 deliverable edits. Pre-existing changes were not reverted. |
| Nested repository state | `causal-irregular-time-series` at `417bb322fd43ddc4caea1e83529b3462b25eaaf5` with local modification in `src/preprocess_mimic_iii_large.py`; `STraTS` at `4d2a7520b565425eed00462cee570e139b5392db`; `git submodule status` fails because `.gitmodules` lacks a mapping for `STraTS`. |
| Inspection date | 2026-07-12 |
| Directories/files inspected | `prompt.txt`, `.gitignore`, `README.md`, `SCRIPTS.md`, `router.py`, `STraTS/`, `causal-irregular-time-series/`, `final-results/AGENTS.md`, `final-results/causal-outputs/AGENTS.md`, `final-results/causal-outputs/scripts/compare_cate_runs.py`, final cross-run CSVs, run summaries, logs, predictive summaries, prediction export headers/row counts, proxy tag tables, literature metadata paths, existing audit files. |
| Inspection methods | `find`, `rg`, `sed`, `git`, `wc`, `head`/CSV header reads, JSON/CSV metadata extraction, representative log reads, source-code searches. |
| Deliberately not executed/opened | No preprocessing, training, causal estimation, sensitivity analysis, permutation test, result regeneration, notebook execution, or expensive pipeline rerun. No pickle/checkpoint/model artifacts were deserialized. Binary PDFs/DOCX files were inventoried but not read for claims. |
| `final-results/AGENTS.md` correction | No factual error requiring correction was found; it was not edited. |

## 2. Deliverable Validation

| File | Exists | Nonempty | Schema or structure valid | Internally consistent | Cross-referenced correctly | Remaining issues | Validation status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/audit/repository_map.md` | yes | yes | Markdown sections and functional component table | yes | References final archive, nested repos, configs, code paths | Final archive untracked; configs missing | PASS WITH LIMITATIONS |
| `thesis-writing/audit/evidence_inventory.md` | yes | yes | Requested evidence families present | yes | Paths link to repository/result archive patterns | Some provenance marked unresolved | PASS WITH LIMITATIONS |
| `thesis-writing/audit/experiment_inventory.csv` | yes | yes | Single CSV header, one row per predictive/causal run family | yes | Summaries/logs/run folders referenced | InterpNet missing; configs missing | PASS WITH LIMITATIONS |
| `thesis-writing/audit/figure_table_inventory.md` | yes | yes | Requested figure/table categories present | yes | Ties artifacts to generators and validations | Image content not exhaustively visually checked | PASS WITH LIMITATIONS |
| `thesis-writing/audit/terminology_map.md` | yes | yes | Canonical terminology table present | yes | Connects terms to code/results | Advisor wording decisions remain | PASS WITH LIMITATIONS |
| `thesis-writing/audit/unresolved_questions.md` | yes | yes | Grouped by requested urgency categories | yes | Issues point to actual inspected paths | Blocking Stage 3 decisions remain | PASS |
| `thesis-writing/audit/claim_evidence_ledger.csv` | yes | yes | Required header and candidate claim rows present | yes | Claims point to exact artifacts where available | Some claims partial/blocked by design | PASS WITH LIMITATIONS |

## 3. Stage 2 Checklist

| Checklist item | Status | Evidence |
| --- | --- | --- |
| Repository map completed | PASS WITH LIMITATIONS | `repository_map.md` covers parent router, nested repos, final results, thesis/literature directories, obsolete areas, and portability risks. |
| Data pipeline documented | PASS WITH LIMITATIONS | Preprocessing code and missing raw/processed data are mapped; exact final processed pickles are external. |
| All implemented models documented | PASS WITH LIMITATIONS | STraTS, GRU, GRU-D, TCN, SAnD, InterpNet implementation status recorded; InterpNet final output missing. |
| All executed experiments identified | PASS WITH LIMITATIONS | Ten predictive archived runs and twelve causal run families inventoried; archive copy provenance incomplete for STraTS. |
| All available results inventoried | PASS WITH LIMITATIONS | Main result families, cross-run tables, proxy tables, logs, diagnostics, binary support artifacts listed. |
| Proxy-state definitions documented | PASS WITH LIMITATIONS | Rule/predicted/majority-vote distinctions and terminology documented; full clinical review remains. |
| Causal estimands and estimators documented | PASS WITH LIMITATIONS | CATE, matching, forest, linear, PFN, downsampling, and estimand wording risks documented. |
| Sensitivity and overlap workflows documented | PASS WITH LIMITATIONS | Sensitivity/permutation present for non-PFN; overlap evidence is indirect and missing dedicated plots. |
| Figures and tables mapped to source files | PASS WITH LIMITATIONS | Figure/table inventory maps artifacts to scripts and validation needs. |
| Missing and contradictory evidence listed | PASS | `unresolved_questions.md` records missing configs, InterpNet, conflicting summary names, missing overlap diagnostics, and provenance gaps. |
| Claim-to-evidence ledger started | PASS | `claim_evidence_ledger.csv` contains candidate claims across methods, results, limitations, and future work. |

## 4. Coverage Validation

| Area | Coverage | Gaps |
| --- | --- | --- |
| Datasets | PhysioNet 2012 and MIMIC-III covered across predictive, proxy, and causal outputs. | Raw data and final processed pickle artifacts are external/missing locally. |
| Predictive models | STraTS, GRU, GRU-D, TCN, SAnD have archived summaries and exports for both datasets. | InterpNet implemented but final output missing. |
| Proxy-state methods | Rule-based, predicted, and majority-vote proxy states distinguished. | Exact voter input directories for majority vote are absolute and not archived. |
| Causal estimators | CausalForest, LinearDML, and CausalPFN covered for both datasets and both sampling conditions. | Primary estimator not selected; PFN lacks downstream diagnostics. |
| Sampling conditions | Original/no-downsample and downsampled runs inventoried. | Numbered config CSVs proving exact `DOWN_SAMPLE` values are missing. |
| Causal pipeline stages | Graph, majority vote, mortality prediction, matching, CATE, sensitivity, and permutation stages covered. | PFN sensitivity/permutation intentionally skipped. |
| Result families | Predictive, proxy, matching, CATE, sensitivity, permutation, cross-run comparison covered. | Some binary artifacts not opened by design. |
| Figures | Learning curves, DAGs, sensitivity contours, workflow image inventoried. | Image content not fully visually validated; proposed overlap plots missing. |
| Tables | Predictive summaries, proxy prevalence/mortality, matching, CATE, sensitivity, permutations, cross-run tables mapped. | Final thesis-formatted tables not generated in Stage 2. |
| Configurations | Local unnumbered configs and final run-summary config paths identified. | Numbered final configs missing. |
| Logs | Representative predictive and causal logs inspected; run-summary log paths inventoried. | Not every log line was exhaustively reviewed. |
| Thesis-relevant claims | Candidate claim ledger started with risk and wording constraints. | Advisor decisions required before final wording. |

Excluded areas: no external raw data locations outside the repository were searched; no binary artifact was deserialized; no generated result was recomputed.

## 5. Internal Consistency Validation

| Check | Status | Evidence |
| --- | --- | --- |
| Paths in audit files exist where expected | PASS WITH LIMITATIONS | Main repo-relative paths exist; absolute `/truenas` and `/workspace` paths are recorded as provenance facts and not locally expected. |
| Dataset names normalized | PASS | Predictive uses `physionet_2012`/`mimic_iii`; causal uses `physionet`/`mimic`; terminology map documents mapping. |
| Model/estimator names normalized | PASS | Predictive model names and causal estimator names are consistent across inventories. |
| Sampling labels normalized | PASS WITH LIMITATIONS | CSV uses `original`/`downsampled`; cross-run source uses `no-downsample`/`downsample`; mapping documented. |
| Status values used consistently | PASS WITH LIMITATIONS | CSV status fields use `yes`, `no`, `partial`, `missing`; unresolved markers used where needed. |
| Evidence classes consistent | PASS | Evidence inventory uses the controlled classes from the prompt. |
| Experiment inventory agrees with evidence inventory | PASS | Predictive/causal run counts and missing InterpNet/PFN skip statuses match. |
| Claim ledger points to valid artifacts | PASS WITH LIMITATIONS | Artifact paths exist or are explicitly marked `[RESULT MISSING]`; exact numerical claims still require Stage 3 table extraction. |
| Unresolved issues correspond to actual ambiguities | PASS | Each issue cites inspected paths/evidence. |
| Proxy states never called verified diagnoses | PASS | Terminology and claim ledger use proxy-state wording. |
| Predictive evidence not presented as causal evidence | PASS | Prediction exports and performance summaries separated from causal outputs. |
| Association evidence not presented as causal evidence | PASS | Mortality-by-tag and mortality prediction marked association/predictive support only. |
| CATE not automatically presented as ATE | PASS | Terminology and unresolved questions explicitly block that wording. |
| Missing PFN diagnostics not described as negative results | PASS | PFN sensitivity/permutation stages marked intentionally skipped. |

## 6. Evidence-Chain Spot Checks

### PhysioNet Predictive Result

Claim: PhysioNet STraTS predictive metrics are available.
Exact artifact: `final-results/strats-outputs/physionet_2012/strats/finetune_strats/training_summary.txt`.
Schema and aggregation: one model run; validation/test metric blocks.
Run/configuration evidence: `run=1o10`, `train_frac=0.500000`, checkpoint metric `auprc + auroc`.
Generating source: `STraTS/src/main.py::write_training_summary`.
Execution evidence: `log.txt` final val/test lines and saved summary line.
Limitation: archive copy provenance and split construction need manifest.

### MIMIC Predictive Result

Claim: MIMIC STraTS predictive metrics are available.
Exact artifact: `final-results/strats-outputs/mimic_iii/strats/finetune_strats/training_summary.txt`.
Schema and aggregation: one model run; validation/test metric blocks.
Run/configuration evidence: `run=1o10`, `train_frac=0.500000`, checkpoint metric `auprc + auroc`.
Generating source: `STraTS/src/main.py::write_training_summary`.
Execution evidence: `log.txt` final val/test lines and saved summary line.
Limitation: `LAT_CHRONIC_BURDEN` has one-class warnings in representative log; interpret metrics as proxy-label prediction.

### Proxy-State Result

Claim: MIMIC rule-based proxy tags are available.
Exact artifact: `final-results/trees/mimic-tags/latent_tags.csv`.
Schema and aggregation: patient-level `ts_id` plus 10 `LAT_*` binary columns; 44,812 data rows.
Run/configuration evidence: generator source `tagging_latent_variables_mimiciii.py::save_outputs`.
Execution evidence: files `prevalence.csv`, `mortality_by_tag.csv`, `validation_summary.json` are co-produced.
Limitation: proxy states are not verified diagnoses.

### Majority-Vote Result

Claim: Majority-vote tags were used by causal runs.
Exact artifact: `final-results/causal-outputs/outputs-physionet-forest/majority_vote/latent_tags_majority_vote.csv`.
Schema and aggregation: patient-level `ts_id` plus 11 PhysioNet `LAT_*` binary columns; 7,993 data rows.
Run/configuration evidence: `outputs-physionet-forest/run_summary.json` stage `majority_vote`.
Generating source: `src/majority_vote_latents.py`.
Execution evidence: stage status success with return code 0.
Limitation: voter input directory is absolute and not archived.

### Matching Result

Claim: Matching baseline summaries are available.
Exact artifact: `final-results/causal-outputs/cate_cross_run_matching_table.csv`.
Schema and aggregation: dataset/sampling/treatment rows with matched-pair effect fields and support fields.
Run/configuration evidence: per-run `matching/global_summary.csv` and run summaries.
Generating source: `src/matching_causal_effect.py`; deduped by `compare_cate_runs.py`.
Execution evidence: all run summaries report matching success.
Limitation: `mean_pair_effect` should not be called ATE without further justification.

### Forest CATE Result

Claim: Forest CATE summaries are available.
Exact artifact: `final-results/causal-outputs/outputs-mimic-forest/cate_estimation/global_summary.csv`.
Schema and aggregation: treatment-level rows with `mean_cate`, normalized CATE, confounder counts, and saved diagnostics.
Run/configuration evidence: `outputs-mimic-forest/run_summary.json` with `--model-type CausalForest`.
Generating source: `src/cate_estimation.py`.
Execution evidence: `logs/05_cate_estimation.log` reports successful summaries 9/9.
Limitation: numbered config missing; CATE is not automatically ATE.

### Linear CATE Result

Claim: LinearDML CATE summaries are available.
Exact artifact: `final-results/causal-outputs/outputs-physionet-linear/cate_estimation/global_summary.csv`.
Schema and aggregation: treatment-level rows with CATE summary statistics.
Run/configuration evidence: `outputs-physionet-linear/run_summary.json` with `--model-type LinearDML`.
Generating source: `src/cate_estimation.py`.
Execution evidence: stage status success in `run_summary.json`.
Limitation: exact numbered config missing.

### PFN CATE Result

Claim: PFN CATE summaries are available but diagnostics are limited.
Exact artifact: `final-results/causal-outputs/outputs-mimic-pfn/cate_estimation/global_summary.csv`.
Schema and aggregation: treatment-level CATE summary rows.
Run/configuration evidence: `outputs-mimic-pfn/run_summary.json` with `--model-type CausalPFN`.
Generating source: `src/cate_estimation.py` PFN branch.
Execution evidence: representative PFN log reports successful summaries 9/9.
Limitation: sensitivity and permutations skipped by run summary because PFN does not use those diagnostics in this pipeline.

### Sensitivity Result

Claim: Non-PFN sensitivity summaries are available.
Exact artifact: `final-results/causal-outputs/outputs-mimic-forest/analyze_cate_results/benchmark_summary.csv`.
Schema and aggregation: treatment-level robustness/sensitivity fields.
Run/configuration evidence: `outputs-mimic-forest/run_summary.json` stage `analyze_cate_results`.
Generating source: `src/analyze_cate_results.py`.
Execution evidence: stage exit code 0 and summary/control-message CSVs.
Limitation: representative log reports partial statuses for most treatments; inspect per-treatment reports before numerical claims.

### Permutation Result

Claim: Non-PFN permutation summaries are available.
Exact artifact: `final-results/causal-outputs/outputs-mimic-forest/permutations_test/treatment_permutation_results.csv`.
Schema and aggregation: treatment-level permutation diagnostic rows with real/permuted mean fields and trial count.
Run/configuration evidence: `outputs-mimic-forest/run_summary.json` stage `permutations_test`.
Generating source: `src/permutations_test.py`.
Execution evidence: representative log shows 10 treatment/outcome permutation trials and saved aggregate CSVs.
Limitation: diagnostic only; temporary trial outputs are deleted by the script.

### Blocked Claim

Claim: InterpNet final performance can be compared with other predictive models.
Exact artifact: `[RESULT MISSING]`.
Schema and aggregation: not available.
Run/configuration evidence: implementation and wrapper commands exist.
Generating source: `STraTS/src/main.py` includes model support.
Execution evidence: none found in `final-results/`.
Limitation: must be marked missing or recovered externally before Stage 3 comparison.

## 7. Readiness for Stage 3

Final status: **READY FOR STAGE 3 WITH EXPLICIT LIMITATIONS**

Resolved in Stage 2:

- Functional repository map completed.
- Final archive result families mapped.
- Twelve causal run families inventoried.
- Ten predictive archived runs inventoried.
- Missing InterpNet output documented.
- PFN diagnostic skips classified as intentional.
- Matching duplicates and failures documented.
- Conflicting summary filenames documented.
- Claim-evidence ledger started.

Blocking issues before unqualified Stage 3 result writing:

- Advisor/user must choose how to handle original versus downsampled runs.
- Advisor/user must define forest/linear/PFN roles and primary estimator status.
- `final-results/` needs a manifest/checksum/archive decision because it is ignored and untracked.
- Numbered final-run configuration CSVs should be recovered or explicitly documented as missing.
- Proxy-state clinical wording needs review.

Non-blocking limitations:

- Binary artifacts were not opened.
- Image content was not exhaustively visually validated.
- Raw and processed datasets are external.
- STraTS archive-copy provenance is incomplete.
- Dedicated overlap diagnostics were not found.

Evidence Stage 3 may safely use with caveats:

- Predictive `training_summary.txt` files for supported models after approved-run confirmation.
- Rule/proxy tag tables as proxy-state evidence, not diagnoses.
- Majority-vote tags as causal pipeline inputs.
- Causal run summaries/logs as execution provenance.
- CATE and matching CSVs with careful estimand wording.
- Sensitivity and permutation CSVs as diagnostics for forest/linear only.

Evidence Stage 3 must not yet use as primary claims:

- InterpNet final results.
- Binary checkpoints, model pickles, and tree pickles directly.
- PFN sensitivity/permutation diagnostics.
- Any ATE claim based only on `mean_cate` or `mean_pair_effect`.
- Any causal clinical conclusion without assumptions, overlap/support limits, and advisor-approved wording.

# Thesis Compression Scientific Repair

Repair date: 2026-07-16 (Asia/Jerusalem).

## Baseline

- Current branch and HEAD: `main` at `26b639cf3da6551e0e2aee388c8b2bfd7368d238` (`aaai authors kit`).
- Thesis-manuscript baseline: `ddbf52b489bc7bffc0b17f39d54aca5d766fe8e3` (`thesis compression`).
- Pre-compression presentation reference: `d77fada7b63c2b0b37746302fcda1c6351fa3e9b` (`SAnD removal`).
- Commit classification: the only commit after the thesis baseline changes 17 files, all below `thesis-writing/paper-aaai/AuthorKit27/`. It changes no active thesis source and remained untouched.
- Initial worktree: dirty with 59 status entries. The pre-existing entries comprised 12 root/runtime/test/config entries (`README.md`, `SCRIPTS.md`, the dirty `causal-irregular-time-series` nested repository, `fix_preprocessor.py`, `prompt.txt`, the three requirements files, `router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `tests/test_router.py`, and `tmp_verify_router.py`); three `thesis-writing/important-md-copies/` files; `thesis-writing/literature/metadata/catalog.csv`; 28 pre-existing Stage 5.2/5.5 log, table-value, and figure-value files; and 15 pre-existing checked-result/manifest files below `thesis-writing/results/`. These bytes were preserved.
- Nested repositories: `causal-irregular-time-series` remained at `417bb322fd43ddc4caea1e83529b3462b25eaaf5` with only its pre-existing modification to `src/preprocess_mimic_iii_large.py`; `STraTS` remained clean at `4d2a7520b565425eed00462cee570e139b5392db`.
- Initial PDF: 94 A4 pages.
- Existing build: `latexmk -C` followed by `latexmk -xelatex main.tex` from `thesis-writing/thesis/`.
- Body spacing: `main.tex` lines 8--9 retain `\usepackage{setspace}` and `\onehalfspacing` unchanged.
- Protected snapshot: SHA-256 manifests covered 30 checked-result/result-manifest/result-figure/abstract files, nine front-matter/Results files, and all 17 AAAI-kit files. Diff hashes separately covered every unrelated outer-worktree change and the pre-existing nested-repository diff.
- Authorized repair paths: Chapter 5, merged Chapter 8, deletion of the inactive Chapter 9 stub, rebuilt `main.pdf`, and this single report. `main.tex` was not changed.

The required baseline commands were run before editing. They confirmed the expected three-commit sequence (`26b639c`, `ddbf52b`, `d77fada`) and that the post-compression diff is confined to the AAAI AuthorKit.

## Review findings addressed

1. The compressed Chapter 5 identified proxy families but did not independently communicate the operational meaning of every prediction target and causal exposure.
2. The merged experimental/validation chapter lacked one compact distinction between execution-supported settings, current source behavior, and unresolved producing lineage.
3. `chapters/09_experimental_design.tex` was an inactive two-line compatibility stub with no active dependency.

The repair did not reopen the broader compression stage. It retained the compressed narrative, the predicted/aggregated-label section, the four-model scope, the five-source aggregate, the estimator hierarchy, the population hierarchy, and all Results material.

## Proxy-definition repair

### Source hierarchy and table design

The reconciliation order was: active tagger source; validated schema/evidence records; the `d77fada7` pre-compression presentation; design prompts for provenance only; and clinical literature for bounded conceptual grounding only. The active authorities were:

- `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`, `LATENT_ORDER` and the eleven `tag_lat_*` functions at source lines 400--710;
- `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`, `LATENT_ORDER` and the ten `tag_*` functions at source lines 543--908;
- `thesis-writing/logs/stage_4_9B_proxy_rule_citation_matrix.csv` and existing evidence reports;
- the current bibliography, without adding or changing citation keys.

Chapter 5 now contains Table 5.1 for all eleven PhysioNet states and Table 5.2 for all ten MIMIC-III states. Both use the requested four fields: proxy state/construct, operational evidence, decision form, and principal boundary. Shared missingness, aggregation, input-mode, active-code-authority, and validation qualifications stay in prose. The tables use local single spacing and standard `\footnotesize`/`\small` text inside landscape `longtable`s; body prose and margins are unchanged.

### Row-level source validation ledger

`Thesis row` refers to Table 5.1 or 5.2. Every active identifier occurs exactly once as a table row; no extra or obsolete identifier occurs.

| Proxy identifier | Source function or rule | Thesis row | Main thresholds/conditions checked | Status | Discrepancy |
|---|---|---|---|---|---|
| `LAT_CHRONIC_BASELINE_RISK` | `tag_lat_chronic_baseline_risk` | 5.1 | Score at least 2: age >=75, BMI <18.5 or >=40, albumin <3.0, ICU type 1/3; BMI input dependency | PASS | None |
| `LAT_GLOBAL_SEVERITY` (PhysioNet) | `tag_lat_global_severity` | 5.1 | Seven domains; score >=3 or score >=2 plus a critical marker; MAP, SBP, PF, SaO2, RR, GCS, renal, hepatic, platelet, lactate, and HR cutoffs | PASS | None |
| `LAT_SHOCK` (PhysioNet) | `tag_lat_shock` | 5.1 | Score >=2 across pressure, lactate, HR, urine, acidosis; low MAP plus lactate >=4 sufficient; no vasopressor input | PASS | None |
| `LAT_RESPIRATORY_FAILURE` (PhysioNet) | `tag_lat_respiratory_failure` | 5.1 | Score >=2 across ventilation, PF <300, oxygenation, RR, PaCO2/pH; ventilation plus low PF sufficient; PF approximation qualified | PASS | None |
| `LAT_RENAL_DYSFUNCTION` (PhysioNet) | `tag_lat_renal_dysfunction` | 5.1 | Score >=2 across creatinine >=2.0/delta >=0.3, BUN >=40, urine, potassium/bicarbonate; creatinine >=3.5 sufficient | PASS | None |
| `LAT_HEPATIC_DYSFUNCTION` | `tag_lat_hepatic_dysfunction` | 5.1 | Weighted score >=2; bilirubin contributes 2; AST/ALT, ALP, albumin, platelet contributions | PASS | None |
| `LAT_COAG_HEME_DYSFUNCTION` | `tag_lat_coag_heme_dysfunction` | 5.1 | Weighted score >=2; platelet <100 contributes 2; platelet <150, HCT, WBC, and platelet-drop contributions | PASS | None |
| `LAT_INFLAMMATION_SEPSIS_BURDEN` | `tag_lat_inflammation_sepsis_burden` | 5.1 | Score >=3 across temperature/WBC/HR/RR-or-PaCO2/lactate/platelets; inflammatory anchor plus lactate condition; no infection anchor | PASS | None |
| `LAT_NEUROLOGIC_DYSFUNCTION` (PhysioNet) | `tag_lat_neurologic_dysfunction` | 5.1 | Weighted score >=2; GCS <=12 contributes 2; sodium, glucose, PaCO2/SaO2/pH evidence; sedation limitation | PASS | None |
| `LAT_CARDIAC_INJURY_STRAIN` | `tag_lat_cardiac_injury_strain` | 5.1 | Weighted score >=2; troponin I >0.1 or T >0.01 contributes 2; ICU type, HR, pressure, lactate contributions | PASS | None |
| `LAT_METABOLIC_DERANGEMENT` (PhysioNet) | `tag_lat_metabolic_derangement` | 5.1 | At least 2 acid-base/lactate/electrolyte/glucose/PaCO2 domains; pH <7.20, lactate >=4, or potassium >=6 sufficient | PASS | None |
| `LAT_CHRONIC_BURDEN` | `tag_chronic_burden` | 5.2 | Score >=2 across age/old flag, comorbidity or Elixhauser, chronic helpers, malignancy/immunosuppression, urgent admission | PASS | None |
| `LAT_INFLAMMATION_SEPSIS` | `tag_inflammation_sepsis` | 5.2 | Score >=2 across temperature, WBC, lactate, culture, antibiotics; at least one infection/inflammation anchor | PASS | None |
| `LAT_GLOBAL_SEVERITY` (MIMIC) | `tag_global_severity` | 5.2 | Seven domains and score >=3; pressure/support, GCS/RASS, renal, acid-base, inflammatory, hepatic/coagulation cutoffs; no single-marker sufficient rule | PASS | None |
| `LAT_SHOCK` (MIMIC) | `tag_shock` | 5.2 | Score >=2 across MAP/SBP/sustained MAP, vasopressor, lactate, 24-hour/rolling urine, pH/base excess; vasopressor conjunction sufficient | PASS | None |
| `LAT_RESPIRATORY_FAILURE` (MIMIC) | `tag_respiratory_failure` | 5.2 | Score >=2 across SpO2, PF, FiO2/support, RR, PaCO2/pH; support conjunction sufficient | PASS | None |
| `LAT_RENAL_DYSFUNCTION` (MIMIC) | `tag_renal_dysfunction` | 5.2 | Score >=2 across creatinine/delta, BUN, urine, potassium/bicarbonate, dialysis; dialysis/CRRT sufficient | PASS | None |
| `LAT_HEPATIC_COAG_DYSFUNCTION` | `tag_hepatic_coag_dysfunction` | 5.2 | Score >=2 across bilirubin, AST/ALT, platelets, INR/prolonged PT/PTT, albumin | PASS | None |
| `LAT_NEUROLOGIC_DYSFUNCTION` (MIMIC) | `tag_neurologic_dysfunction` | 5.2 | GCS <=8 contributes 2; GCS <=13, components, RASS, pupil/focal evidence contribute 1; score >=2; sedation/intubation caveat | PASS | None |
| `LAT_METABOLIC_DERANGEMENT` (MIMIC) | `tag_metabolic_derangement` | 5.2 | At least 2 pH, bicarbonate/base-excess, lactate, potassium, sodium, or glucose domains; no single-marker sufficient rule | PASS | None |
| `LAT_CARDIAC_STRAIN` | `tag_cardiac_strain` | 5.2 | Score >=2 across troponin fallback, CK-MB, rhythm/HR, HR-hypotension, cardiac context; final troponin-or-rhythm anchor; CK-MB alone insufficient | PASS | None |

No unresolved rule discrepancy remains. The restored rows do not present proxies as diagnoses, clinical gold standards, SOFA/KDIGO/DIC reproductions, or chart-adjudicated outcomes. Exact clause-by-clause source paths, hashes, prompt-to-code lineage, and detailed citation-status matrices deliberately remain in the repository evidence package rather than returning to the main text.

## Experimental-setting repair

Chapter 8 now contains Section 8.2, “Executed Settings and Provenance Status,” and one compact two-page longtable. Its vocabulary explicitly separates `artifact-supported`, `log-supported`, `source-defined`, `unresolved`, and `not applicable` evidence.

### Setting-to-evidence ledger

| Table component | Reported setting/status | Evidence class | Principal source checked |
|---|---|---|---|
| Prediction scope and artifacts | Two datasets x STraTS/GRU/GRU-D/TCN; eight checked combinations; multi-label rule-proxy targets | Artifact-supported | `results/checked_predictive_metrics.csv`, `results/checked_predictive_exports.csv`, `reproducibility/predictive_run_lineage.csv` |
| Archived predictive settings | Run `1o10`, training fraction 0.5, validation/test evaluation, AUPRC+AUROC checkpoint selection | Artifact-supported | Checked training-summary fields represented in `checked_predictive_metrics.csv` and `predictive_run_lineage.csv` |
| Seed/export split | Seed 2023 and `predict_split=all` | Log-supported | Archived Namespace/log records catalogued by `reproducibility/predictive_run_lineage.csv`; explicitly not a split manifest |
| Export contract | Unique `ts_id`, paired `<label>_prob` and binary `<label>` fields, valid ranges | Artifact-supported | `results/checked_predictive_exports.csv` |
| Binary threshold | 0.5 | Source-defined | Prediction/export implementation and Chapter 6 source audit; not represented as recovered producing history |
| STraTS pretraining | Separate self-supervised path for STraTS only | Source-defined, with archived artifacts | STraTS training/checkpoint records and `predictive_run_lineage.csv`; exact checkpoint lineage remains unresolved |
| Causal matrix/hierarchy | Two datasets x three estimators x two sampling conditions = 12 run families; original primary; downsampled robustness; forest/linear/PFN hierarchy | Artifact-supported | `audit/experiment_inventory.csv`, `reproducibility/causal_run_lineage.csv`, `results/results_manifest.csv` |
| Exposure/aggregate/support | Exact five-source lineage; exposure-specific graph/column admission; matching as descriptive support diagnostics | Artifact-supported plus source-defined behavior | Causal run summaries/lineage and active aggregation/matching source; voter bytes/hashes remain unresolved |
| Sensitivity evidence | Direct, later artifact, labelled fallback, benchmark, partial/failure classes; no equivalent archived CausalPFN family | Artifact-supported / not applicable | `results/checked_sensitivity_candidates.csv`, reproducibility records |
| Permutations | Ten trials, seed 42, treatment-column versus copied-outcome disruption; CausalPFN skipped | Artifact-supported / not applicable | `results/checked_permutation_candidates.csv` and causal run records |
| Producing lineage | Stage argv/status/return codes, limited interpreter/device fields, hashes/schemas | Artifact-supported but incomplete | `reproducibility/causal_run_lineage.csv`, `predictive_run_lineage.csv`, `artifact_index.csv`, `provenance_gaps.csv` |

The table keeps all required gaps visible: processed-pickle hashes, split IDs/manifests, checkpoint-to-export mapping, raw producing commands/configurations, numbered final causal configurations, source versions, producing environment, and archive-copy direction. Current defaults are never called historical producing values; archived paths are not called portable commands; requirements are not called producing-environment proof; original and downsampled populations remain separate; and permutation parameters are reported only for validated DML records.

Full artifact-path matrices, hardware wish lists, environment-field inventories, configuration-precedence detail, and result-admission checklists deliberately remain outside the main chapter.

## Stub resolution

Repository searches covered the exact path/name across active thesis source, `main.tex`, Python/shell/build/validation files, and planning/history. No active source, build script, or validation tool requires `thesis-writing/thesis/chapters/09_experimental_design.tex`; `main.tex` already omitted it. Remaining mentions are historical logs/audits or old planning entries, including two planning paths that use the different obsolete spelling `chapters/ch09_experimental_design.tex`.

The inactive two-comment stub was therefore deleted. The active content remains solely in `08_robustness_sensitivity_validation.tex`; no chapter was re-enabled or split, and deletion changes no label or chapter number.

## Scientific preservation

- Checked numerical Results, result manifests/checksums, result-table values, and `chapters/10_results.tex`: unchanged byte-for-byte within the protected manifests.
- Result figures, figure data, and DAG images: unchanged byte-for-byte.
- Abstracts, title pages, administrative metadata, Hebrew cover, keywords, nomenclature, and acknowledgements: unchanged byte-for-byte.
- Active research code: no repair edit. The outer unrelated-diff SHA-256 remained `54105cbcdb773335dacd8176692a417f2034e55fb72bdf556ce5f1f87713a26f`; the nested causal diff remained `897be9dfe89113fecb768a4eb6dc9a3eae6d04f70acb8409b92d532abd156201`.
- AAAI AuthorKit: all 17 protected hashes matched and the post-compression commit remained intact.
- SAnD: exact word-boundary search of active thesis `.tex` files returned zero matches.
- Predictive scope: PhysioNet 2012 and MIMIC-III with STraTS, GRU, GRU-D, and TCN remains unchanged.
- Aggregate: exactly one rule-derived source plus four predicted sources remains unchanged.
- Estimator hierarchy: CausalForestDML primary, LinearDML secondary, CausalPFN exploratory remains unchanged.
- Population hierarchy: original cohorts primary; outcome-downsampled cohorts separate robustness analyses remains unchanged.
- Spacing: `setspace` plus `\onehalfspacing` remains unchanged; only the three dense new longtables use local single spacing.

Citation, label, reference, and numeric-token accounting:

- Citation keys: none added, removed, or changed. The existing clinical-grounding citation group moved with its paragraph to follow Table 5.1.
- Labels: the compressed `tab:proxy-family-summary` label was removed; `tab:physionet-proxy-definitions`, `tab:mimic-proxy-definitions`, `sec:experimental-design:executed-settings-provenance`, and `tab:executed-settings-provenance` were added. The deleted stub defined no labels.
- References: three new in-text table references point to the two proxy tables and the settings table; the final build resolves them.
- Numeric tokens: additions are source-checked proxy thresholds/score rules and evidence-backed settings (`0.5`, `1o10`, `2023`, 12 run families, 10 trials, seed 42, and five-source lineage). No checked result value or Results-chapter token changed.

## Validation

### Build and static checks

- Clean command sequence: `latexmk -C` then `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`.
- Exit status: 0. XeLaTeX converged after Biber; Biber found and wrote all 36 cited keys.
- Final log: no undefined citation, undefined reference, multiply defined label, missing character, missing input file, LaTeX error, emergency stop, or fatal error.
- `git diff --check`: clean for all repaired/deleted source files.
- Table overflow: no overfull box originates in either restored proxy table or the compact settings table. Final log contains 12 small non-table overfull boxes (maximum 9.519 pt) and one bibliography underfull box; the two Chapter 5 warnings are in pre-existing prose/path text, and Chapter 8 has none.
- Non-blocking inherited/toolchain notes: `biblatex` reports unsupported Hebrew localization and falls back to dummy definitions; `xdvipdfmx` reports duplicate named table objects associated with longtables. Neither produces an undefined reference, visible corruption, or qpdf failure.
- PDF syntax: `qpdf --check main.pdf` reports no syntax or stream-encoding errors.
- Final PDF: 101 A4 pages, 3,001,531 bytes.

### Scientific and protected checks

- `^\nolinkurl{LAT_` row count: 21, split exactly 11 PhysioNet and 10 MIMIC rows.
- Active `LATENT_ORDER` lists and all 21 source functions were reconciled; the ledger above has 21 PASS rows and zero discrepancies.
- No obsolete or extra state, diagnostic upgrade, SAnD term, or changed model/estimator/population hierarchy was found.
- All 30 primary protected hashes, all nine thesis front-matter/Results hashes, and all 17 AuthorKit hashes matched the pre-edit snapshot.
- Unrelated outer diff and nested causal diff hashes matched the pre-edit snapshot exactly. `STraTS` remained clean.

### Complete visual review

All 101 pages were rendered at 100 dpi and inspected in nine ordered contact sheets. Contents, Lists, every Chapter 5 page, Tables 5.1 and 5.2, every Chapter 8 page, Table 8.2, chapter transitions, Results opening, bibliography, and final Hebrew cover were additionally checked at adequate resolution where needed.

The review found readable table text at normal zoom; repeated headers on continuation pages; correct table numbering and List-of-Tables entries; no clipping, overlap, broken identifiers, detached headings, blank/nearly blank pages, or excessive whitespace; consistent body spacing; and intact RTL cover layout. An intermediate 103-page build had a sparse pre-table page and a one-row continuation page; moving the existing explanatory paragraph after Table 5.1 and using standard local `\footnotesize` for that table removed both without deleting scientific content or changing global typography.

## Length outcome

- Starting PDF: 94 pages.
- Final PDF: 101 pages.
- Net restoration: 7 pages.
- Pagination location: the expanded List of Tables accounts for one front-matter page; Chapter 5 grows by three pages; Chapter 8 grows by three pages. Later chapters shift but do not grow from repair content.

The added pages make all 21 downstream constructs operationally understandable and distinguish confirmed execution evidence from unresolved lineage. No compensating prose cuts, figure shrinking, margin changes, body-font changes, or global spacing manipulation were used.

## Unresolved issues

The scientific repair has no unresolved proxy-rule discrepancy or document-integrity blocker. The following are deliberately visible, non-blocking limitations of the underlying archive or toolchain:

- predictive split membership, processed-input hashes, exact checkpoint-to-export mapping, numbered final causal configurations, producing commands/source versions/environments, and archive-copy direction remain incomplete;
- proxy constructs remain rule-derived and lack chart-adjudicated clinical validation;
- existing small overfull/underfull boxes, Hebrew `biblatex` fallback, and nonfatal `xdvipdfmx` duplicate table-object warnings remain presentation/toolchain notes.

## Readiness decision

READY FOR AUTHOR REVIEW WITH NON-BLOCKING PRESENTATION NOTES

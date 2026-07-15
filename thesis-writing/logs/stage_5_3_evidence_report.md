# Stage 5.3 evidence report

## 23.1 Repository baseline

- Head: `f71c9bab70c8fb6347c7692236cd2cfd03e84fa1` (`step 5.2`); immediate parent: `11a2cb46a87a979677602556611a704cfbd1074a` (`step 5.1`).
- Branch: `main`.
- The Stage 5.2 diff adds audit ledgers/evidence reports and changes no thesis PNG, checked CSV, result/graph generator, or research graph source. Its only protected evidence-record modification is the authorized duplicate-name clarification in `figure_selection_register.md`.
- Stage 5.2 records five included figures, zero figure-value discrepancies, 239 checked numerical table cells with zero discrepancies, 1,389/1,389 manifest files present with matching hashes, and `READY FOR EXTERNAL FIGURE VALIDATION`.
- Initial parent worktree (preserved, including pre-existing CRLF-only and user changes):
```
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
 M thesis-writing/logs/stage_5_2_appendix_audit.csv
 M thesis-writing/logs/stage_5_2_figure_validation.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-edges.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-nodes.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-edges.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-nodes.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT-summary.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-MIMIC-CATE.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-PHYSIONET-CATE.csv
 M thesis-writing/logs/stage_5_2_reproducibility_artifact_audit.csv
 M thesis-writing/logs/stage_5_2_table_audit.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-analysis-populations.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-forest-mimic.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-forest-physionet.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-linear-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-matching-support.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-pfn-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-predictive-performance.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-robustness-summary.csv
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
- Initial nested causal worktree:
```
M src/preprocess_mimic_iii_large.py
```
- Initial nested STraTS worktree:
```
CLEAN
```

## 23.2 External figure-decision record

`stage_5_3_external_figure_decision.csv` and its Markdown companion transcribe the five independent assistant decisions supplied in the Stage 5.3 authorization prompt. Codex did not approve the figures. The review found no figure hallucination, fabricated value, hidden sign, unauthorized aggregation, invented graph element, or estimator substitution. DAG readability remains a non-blocking limitation; direction agreement remains direction-only evidence. No clinical, causal-identification, or statistical-significance approval follows.

| Figure | SHA-256 at Stage 5.3 baseline |
| --- | --- |
| `F-DAG-MIMIC` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` |
| `F-DAG-PHYSIONET` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` |
| `F-RESULT-MIMIC-CATE` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` |
| `F-RESULT-PHYSIONET-CATE` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` |
| `F-RESULT-DIRECTION-AGREEMENT` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` |

## 23.3 Search methodology

Read-only local searches covered tracked and non-sensitive untracked project files; parent, causal, and STraTS reachable histories; git trees and objects; `git fsck --full --no-reflogs --unreachable --no-progress`; archived run summaries/logs/config basenames; manifests; copied output directories; training summaries; prediction exports; checkpoints; and environment/path metadata. No web access, fetch, submodule update, raw protected clinical data, shell history, credentials, tokens, `.env` files, or SSH files were inspected. `stage_5_3_recovery_search_log.csv` records repositories, objects, paths, relevance, and recovery status.

## 23.4 Recovered evidence

| Item | Exact source | Evidence class | Previous status | New status | Impact |
| --- | --- | --- | --- | --- | --- |
| Causal stage argv/CWD/status/return codes | 12 archived `run_summary.json` files | `RUN_SUMMARY_RECORDED` | commands treated as incomplete at high level | recorded command metadata available | Commands are auditable, while configs/inputs/source versions remain incomplete. |
| Predictive export arguments, split argument, and seed | 10 archived `log.txt` Namespace records | `LOG_RECORDED` | split/seed unavailable at high level | `predict_split=all`, `seed=2023` recorded | Does not provide split IDs or checkpoint-to-export proof. |
| Predictive checkpoint files | 10 `checkpoint_best.bin` files | `EXACT_ARCHIVED_ARTIFACT` | checkpoint provenance incomplete | files and hashes available | Artifact existence is distinct from exporter linkage. |
| Current/historical config search | causal reachable history and object scan | `EXACT_GIT_HISTORY_RECOVERY` | numbered config unresolved | only unnumbered configs recovered | Similar/current config remains non-proof. |
| DAG copy groups | archived and thesis PNG SHA-256 groups | `EXACT_HASH_IDENTICAL_COPY` | partial copy provenance | byte identity explicit | Direction/timing remains unknown. |

## 23.5 Causal-run lineage

All 12 required causal families have a row in `reproducibility/causal_run_lineage.csv`. Every archived summary reports overall success, explicit stage statuses, commands, return codes, and timestamps. Forest and Linear runs report successful matching, CATE, saved-CATE analysis, and permutations. CausalPFN runs report matching/CATE success and intentional skips for the non-EconML analysis/permutation stages. The numbered producing configurations, processed-pickle hashes, producing source versions, package environments, and archive-copy direction remain unresolved.

## 23.6 Predictive-run lineage

All 10 dataset--model families have a row in `reproducibility/predictive_run_lineage.csv`. Training summaries, logs, prediction exports, and checkpoint files are archived and hashed. Logs record `predict_split=all` and `seed=2023`; they do not archive split IDs, processed-pickle hashes, an immutable checkpoint-to-export map, the exact shell executable, or a producing STraTS revision.

## 23.7 Data lineage

`reproducibility/data_lineage.csv` separates raw source data, authorized access, raw version/hashes, extraction/cohort construction, processed pickles, identifier contracts, prediction inputs, proxy labels, majority-vote inputs, causal inputs, and mortality construction. It relies only on schemas, manifests, code contracts, and available hashes. No protected raw data was opened or copied. Similar mortality field names are not treated as cross-dataset equivalence.

## 23.8 Environment lineage

Causal summaries preserve a historical `thesis310` interpreter path and timestamps; predictive logs preserve CUDA device type and timestamps. Neither is a complete producing software/hardware environment. Requirements are classified as `INTENDED_REQUIREMENTS_ONLY`. Stage 5.2 figure/DAG recreation is `CURRENT_SOURCE_REPRODUCTION`, not historical-production proof. Full rows are in `reproducibility/environment_lineage.csv`.

## 23.9 Source-version lineage

Current parent/nested gitlinks and heads are recorded in `reproducibility/source_version_lineage.csv`: parent `f71c9bab70c8fb6347c7692236cd2cfd03e84fa1`, causal `417bb322fd43ddc4caea1e83529b3462b25eaaf5`, and STraTS `4d2a7520b565425eed00462cee570e139b5392db`. These are not substituted for producing versions. No per-run producing causal or STraTS revision was recovered. The causal worktree was already modified at baseline.

## 23.10 Archive-copy lineage

The MIMIC DAG group has eight hash-identical paths (six archived run copies, `causal_dag_overview.png`, and the thesis copy); the PhysioNet DAG group has seven (six archived run copies and the thesis copy). Hash equality proves bytes, not historical origin, direction, actor, or timestamp. The MIMIC `causal_dag_overview.png` remains excluded solely to avoid duplicate inclusion.

## 23.11 Provenance gaps

`reproducibility/provenance_gaps.csv` contains 18 dispositions: 3 `RECOVERED`, 5 `PARTIALLY_RECOVERED`, 5 `NOT_FOUND_AFTER_EXHAUSTIVE_LOCAL_SEARCH`, and 5 `EXTERNAL_RECORD_REQUIRED`. It retains all required categories, owners, external-input flags, likely-irrecoverable assessments, thesis wording, and next actions.

## 23.12 Thesis repairs

Only evidence-supported provenance wording changed.

- `chapters/06_predictive_modeling.tex`: logs record `predict_split=all` and `seed=2023`, while archived checkpoints are hashable; split IDs, processed-input hash, checkpoint-to-export proof, and copy manifest remain absent.
- `chapters/09_experimental_design.tex`: the compact package is identified as indexing exact causal argv arrays and log-recorded predictive arguments without claiming historical rerun lineage.
- `appendices/appendices.tex`: adds a precise package reference.
- `logs/unresolved_placeholders.md` and `logs/deferred_fixes.md`: replace materially false absence wording with the recovered partial evidence and retain the remaining gaps.

No value, figure, caption, citation, interpretation, or administrative fact changed.

## 23.13 Reproducibility package

The package has 10 files: `README.md`; `artifact_index.csv` (9 rows); `causal_run_lineage.csv` (12); `predictive_run_lineage.csv` (10); `data_lineage.csv` (9); `environment_lineage.csv` (10); `source_version_lineage.csv` (5); `archive_copy_lineage.csv` (15 unique copy-instance rows); `provenance_gaps.csv` (18); and `checksums.sha256` (9 package files, excluding itself).

Programmatic validation passed: required columns and unique row IDs are present; status fields are populated; referenced run/export/checkpoint/copy hashes match; inferred checkpoint/export links are not marked recovered; no copy direction is asserted; and every gap has an owner and next action. All package checksums verify.

## 23.14 Files changed

- `thesis-writing/reproducibility/` (all 10 package files)
- `thesis-writing/logs/stage_5_3_external_figure_decision.csv`
- `thesis-writing/logs/stage_5_3_external_figure_decision.md`
- `thesis-writing/logs/stage_5_3_recovery_search_log.csv`
- `thesis-writing/logs/stage_5_3_reproducibility_claim_matrix.csv`
- `thesis-writing/logs/stage_5_3_evidence_report.md`
- `thesis-writing/thesis/chapters/06_predictive_modeling.tex`
- `thesis-writing/thesis/chapters/09_experimental_design.tex`
- `thesis-writing/thesis/appendices/appendices.tex`
- `thesis-writing/logs/unresolved_placeholders.md`
- `thesis-writing/logs/deferred_fixes.md`
- `thesis-writing/thesis/main.pdf`

## 23.15 Protected-file validation

All 30 protected baseline files are byte-identical at completion: 14 checked CSVs, five protected result records, the result generator, five thesis PNGs, both literature metadata files, and both causal graph sources. Protected changed count: `0`.

The five externally reviewed PNG hashes remain MIMIC DAG `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8`; PhysioNet DAG `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2`; MIMIC CATE `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969`; PhysioNet CATE `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87`; and direction agreement `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea`.

The aggregate source digest for `causal-irregular-time-series/src/` remains `2b33b9da97bb07debe102e1b91d5c304546c285a6d4c55644de94cfa54a6274d`; the STraTS non-Git working-tree digest remains `8df73f0e1a905d7b3bb83febfb565b25e6a589e8b7d48538c001eff0c63b74bb`. Research source is unchanged.

Before editing, all 21 thesis source-file hashes were captured:

```
22acfca2b17898d1ac176dc86818bac03183ea06cd6ffcfa48ddbdf5e0e2617f  appendices/appendices.tex
43789ea8f2dcde6175261f97a1318943edfb5be349ebf9feaf5c59cbac940c2e  chapters/01_introduction.tex
8496165c6d8be218bd7e47c97786dcf04adbb9076ef90a2f363f36af051a72b0  chapters/02_background_related_work.tex
5744346026f39d67d8646538a8f5325e6482854b5b9ffeda6e46bd1a55068f54  chapters/03_problem_definition_study_design.tex
b0190a26a194a698daa099f32a361a696c17a04bb974aa1bba5d2edae6ab922a  chapters/04_data_preprocessing.tex
5e5f77b1d4c119ab2432eadeb0e537b784c96fe18f0b3a1c10e5cfdffe662f1f  chapters/05_proxy_state_construction.tex
11344f15cba152cf3768da5e08c832162ae63d3d4acc7cc7f7410460a5089460  chapters/06_predictive_modeling.tex
6ac793a8d86f4426ac6a470f24afa95f56fc4c3469b448f60756cc93381d361a  chapters/07_causal_methodology.tex
939107b6f983dd4bf5b3d8d8a966f5d88cc9f95ee48017ec796ba87ae9234054  chapters/08_robustness_sensitivity_validation.tex
b350bd5087d825408e570ea69dd295d819f6ee5448fb5748c25bad2d646a58a6  chapters/09_experimental_design.tex
f831b65a48333edde4138869bbeae73f3b843b3d07618238ed65d8c1b0e61de8  chapters/10_results.tex
b5d2ba64b912a40f452487e2a3c6423bb60bec79132d4b7b3590ee8bd341b53b  chapters/11_discussion.tex
11c2d93cce5c2df0a9db3dc66615cf71e25a8338468d1c91c3c3f7fa61441d4e  chapters/12_conclusions_future_work.tex
968415da17f5be0926f690c056e2471d9b0b3397fddb9ffe6f5577ba2de31769  frontmatter/abstract_primary.tex
10e11b6c1279e8e7cfd912e4f83b160888ec651e9aec1b3e72b89f054591f079  frontmatter/abstract_secondary.tex
7ba7d8feb4394f33cfaeb124e2685fea725f91cf3ae7d216f11b973f2029f9fb  frontmatter/acknowledgements.tex
d8bb14e93b49e2448cc4810bc7294eeef78699fd1395b5ecdbbaecc8974875d4  frontmatter/administrative_metadata.tex
3a7f72ab68c9e94338a0a77b6526f39871f7551cb37c9ace34485b45ebfbdf15  frontmatter/keywords.tex
73af128086476e8a2d2386abbf4597eb48233dc0e17dd49220c2862acedf993a  frontmatter/nomenclature.tex
46194db1cc88d8d8fe80963506bf2e58533a44932d77f026350759e308f7cad5  frontmatter/title_pages.tex
e8bd08acd05176e2fad605b0bcfba18983898ee7df36787346f02ee6b3918b6a  main.tex
```

The only allowed source changes are `chapters/06_predictive_modeling.tex` (now `0226251a71d2b5e19b8098381449876c5a58fac910139275a14c5ae803b22196`), `chapters/09_experimental_design.tex` (now `9d1359f8d7865888871307e98edca73e18beb852ed66de4746fa98eabfdb8b31`), and `appendices/appendices.tex` (now `fdbbe0f6cd878c41573c80019d71a0390a6f7bf8e2f1e0e7c09c236f07ac72e2`). The remaining 18 source-file hashes are unchanged.

## 23.16 Final build

From `thesis-writing/thesis/`, `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf` all returned 0. `latexmk -c` was then run, leaving `main.pdf` and no LaTeX auxiliary files.

- Pages: 111; PDF SHA-256: `70db7414b4363f64faab597c313ae85d3ec9b388c6a4bfa9f11cc7e56d1df855`.
- Unresolved citations: 0; unresolved references: 0; duplicate labels: 0; fatal errors: 0; Biber errors/warnings: 0/0; missing glyphs: 0; bidi warnings: 0; `xdvipdfmx` warnings: 0.
- Existing layout diagnostics: 48 overfull and 1,157 underfull boxes; none is introduced as a Stage 5.3 blocker.
- Render inspection: pages 54, 77, 78, and 107 (all pages touched by the reader-facing repairs, including the Chapter 9 sentence continuation) were rendered and visually inspected. The new text is legible and no figure changed.

## 23.17 Remaining gates

The remaining non-blocking gates are numbered causal configurations; raw-data access/version/hashes and cohort extraction lineage; processed-pickle hashes; predictive split IDs; checkpoint-to-export proof; full predictive shell commands; producing source versions, package environments, and hardware; archive-copy direction; CausalPFN source/version; LLM prompt-run settings; and the human clinical-review record.

## 23.18 Readiness decision

READY FOR STAGE 5.4 WITH NON-BLOCKING PROVENANCE GAPS

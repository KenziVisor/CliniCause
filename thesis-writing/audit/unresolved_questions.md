# Stage 2 Unresolved Questions

This file records repository-specific uncertainty. Do not silently resolve these during Stage 3.

## Blocking Stage 3

### UQ-BLOCK-001

| Field | Value |
| --- | --- |
| Question | Which runs are thesis-approved when original and downsampled versions both exist? |
| Relevant paths | `final-results/causal-outputs/outputs-*`, `cate_cross_run_unified_table.csv`, `cate_cross_run_summary.csv` |
| Why it matters | Downsampled runs have different sample sizes and outcome rates, and the cross-run report says they should not be treated as the same estimand/population as no-downsample runs. |
| Evidence already inspected | Twelve run folders, cross-run script/report/tables, per-run `run_summary.json`. |
| Current best-supported interpretation | Both original and downsampled runs executed; neither is marked thesis-primary. |
| Risk if unresolved | Stage 3 may mix non-comparable estimates or select a result without authorization. |
| Recommended resolution | Advisor/user must designate primary sampling design or require parallel presentation. |
| Owner | advisor/user |
| Stage blocked | Stage 3 result selection |

### UQ-BLOCK-002

| Field | Value |
| --- | --- |
| Question | Are forest, linear, and PFN comparisons, alternatives, or candidates for primary analysis? |
| Relevant paths | `outputs-*-forest*`, `outputs-*-linear*`, `outputs-*-pfn*`, `cate_cross_run_summary.csv` |
| Why it matters | Estimator choice changes interpretation; PFN lacks sensitivity and permutation diagnostics by design. |
| Evidence already inspected | CATE summaries, run summaries, logs, cross-run report. |
| Current best-supported interpretation | All three estimators executed for CATE; forest/linear have additional robustness diagnostics; PFN is diagnostic/alternative unless approved otherwise. |
| Risk if unresolved | Thesis may imply a primary estimator or average estimators without justification. |
| Recommended resolution | Record advisor decision on primary estimator and comparison role of alternatives. |
| Owner | advisor/user |
| Stage blocked | Stage 3 causal-results framing |

### UQ-BLOCK-003

| Field | Value |
| --- | --- |
| Question | Can thesis claims rely on an ignored and untracked `final-results/` archive without a manifest? |
| Relevant paths | `.gitignore`, `final-results/`, `final-results/AGENTS.md`, `git status --ignored --short` |
| Why it matters | The main evidence archive is not committed and may not be reproducible from a clean checkout. |
| Evidence already inspected | `.gitignore` ignores `final-results/`; `git status` reports `!! final-results/`; `git ls-files final-results` is zero per archive guide. |
| Current best-supported interpretation | Results are locally present and execution-supported but not repository-tracked. |
| Risk if unresolved | External reviewers cannot verify exact artifacts cited in thesis. |
| Recommended resolution | Create a results manifest with checksums, archival location, and commit/source state before Stage 3 final writing. |
| Owner | user |
| Stage blocked | Stage 3 evidence citation |

### UQ-BLOCK-004

| Field | Value |
| --- | --- |
| Question | Are the numbered final-run configuration CSV files recoverable? |
| Relevant paths | `run_summary.json` paths like `/truenas/home/kenzikob/causal-irregular-time-series/configs/mimic-global-variables-1.csv` |
| Why it matters | Exact `MODEL_TYPE`, `DOWN_SAMPLE`, trials, treatment list, and confounder settings for final runs cannot be fully verified from local files alone. |
| Evidence already inspected | Local `configs/*global-variables.csv`, `runs/validate_demo/config/physionet_resolved_config.csv`, all final `run_summary.json` files. |
| Current best-supported interpretation | Only unnumbered local defaults are present; numbered configs referenced by final runs are [CONFIGURATION MISSING]. |
| Risk if unresolved | Stage 3 may cite exact configuration-dependent claims without exact configuration evidence. |
| Recommended resolution | Copy numbered configs into an archived manifest or verify they match reconstructed settings. |
| Owner | user |
| Stage blocked | Stage 3 reproducibility and methods |

## High-Risk Interpretation Issue

### UQ-HR-001

| Field | Value |
| --- | --- |
| Question | Should any runs be excluded because of partial execution or missing diagnostics? |
| Relevant paths | `outputs-*-pfn*/run_summary.json`, `outputs-*/analyze_cate_results/`, `outputs-*/permutations_test/` |
| Why it matters | PFN CATE ran successfully, but sensitivity/permutation stages were skipped; some non-PFN sensitivity reports are partial. |
| Evidence already inspected | Run summaries, representative logs, benchmark summaries, cross-run inventory. |
| Current best-supported interpretation | PFN should not be excluded as failed, but it has diagnostic limitations; non-PFN sensitivity outputs need per-treatment validation before quoting. |
| Risk if unresolved | Missing PFN diagnostics could be misreported as negative results or silently ignored. |
| Recommended resolution | Decide whether PFN is exploratory/secondary and state missing diagnostics explicitly. |
| Owner | advisor/user |
| Stage blocked | Stage 3 causal robustness interpretation |

### UQ-HR-002

| Field | Value |
| --- | --- |
| Question | Are proxy-state thresholds and definitions sufficiently documented for thesis use? |
| Relevant paths | `tagging_latent_variables_mimiciii.py`, `tagging_latent_variables_physionet.py`, `final-results/trees/*` |
| Why it matters | Proxy states are central treatments/exposures; definitions must be clinically and methodologically transparent. |
| Evidence already inspected | Tagger source, MIMIC validation outputs, PhysioNet tag CSV, tree pickle paths. |
| Current best-supported interpretation | Rules are implemented, but tree pickles were not deserialized and PhysioNet validation tables are limited in final archive. |
| Risk if unresolved | Stage 3 may overstate clinical validity or fail to explain proxy construction. |
| Recommended resolution | Produce a proxy-definition table from source and have clinical/advisor review. |
| Owner | advisor/user |
| Stage blocked | Stage 3 methods and clinical interpretation |

### UQ-HR-003

| Field | Value |
| --- | --- |
| Question | Can `mean_cate` and `mean_pair_effect` be interpreted as ATE or ATT? |
| Relevant paths | `src/cate_estimation.py`, `src/matching_causal_effect.py`, CATE/matching global summaries |
| Why it matters | Mislabeling estimands would materially overstate the causal interpretation. |
| Evidence already inspected | Source references, CATE and matching schemas, terminology map. |
| Current best-supported interpretation | `mean_cate` is an aggregate of estimated patient-level CATE values; `mean_pair_effect` is a matched-pair summary closer to ATT-style support. Neither should be called ATE without further proof. |
| Risk if unresolved | Incorrect estimand wording in thesis results. |
| Recommended resolution | Formalize estimand wording with advisor before result prose. |
| Owner | advisor/user |
| Stage blocked | Stage 3 causal claims |

### UQ-HR-004

| Field | Value |
| --- | --- |
| Question | Are forest/linear/PFN treatment-effect outputs comparable despite different diagnostics and model behavior? |
| Relevant paths | `cate_cross_run_summary.csv`, `cate_cross_run_comparison_report.md`, PFN run summaries |
| Why it matters | Cross-estimator comparisons are informative but can be overread as interchangeable estimates. |
| Evidence already inspected | Cross-run tables/report and PFN logs. |
| Current best-supported interpretation | Comparisons are useful robustness/triangulation evidence; PFN lacks downstream sensitivity/permutation. |
| Risk if unresolved | Stage 3 may average or rank estimators without a methodological decision. |
| Recommended resolution | Decide whether estimator comparison is sensitivity analysis, model comparison, or primary selection. |
| Owner | advisor/user |
| Stage blocked | Stage 3 results organization |

## Missing Provenance

### UQ-PROV-001

| Field | Value |
| --- | --- |
| Question | What is the full archival provenance for STraTS outputs copied into `final-results/`? |
| Relevant paths | `final-results/strats-outputs/`, `STraTS/run_full_main.sh`, `STraTS/run_main_mimic.sh`, `router.py` |
| Why it matters | Predictive outputs have summaries/logs but no causal-style run manifest or copy manifest. |
| Evidence already inspected | Training summaries, representative logs, shell wrappers, export filenames. |
| Current best-supported interpretation | Outputs match STraTS source/wrapper conventions and logs, but copy into `final-results/` is [PROVENANCE UNCLEAR]. |
| Risk if unresolved | Predictive result reproducibility chain remains incomplete. |
| Recommended resolution | Add manifest recording source output directories, commands, commit, and checksums. |
| Owner | user |
| Stage blocked | Stage 3 predictive evidence citation |

### UQ-PROV-002

| Field | Value |
| --- | --- |
| Question | Is the exported prediction split known for each latent-prediction CSV? |
| Relevant paths | `final-results/strats-outputs/predicted*_latent_tags*.csv`, `STraTS/run_full_main.sh`, `STraTS/run_main_mimic.sh` |
| Why it matters | Prediction exports can represent train, validation, test, or all splits; causal input interpretation depends on this. |
| Evidence already inspected | Wrapper lines show `--predict_split all` for matching export names; CSV row counts inspected. |
| Current best-supported interpretation | Likely `all` split for archived exports, but final copy provenance is incomplete. |
| Risk if unresolved | Stage 3 may misstate whether predictions are out-of-sample. |
| Recommended resolution | Confirm archived export commands or add manifest; avoid claiming out-of-sample export unless verified. |
| Owner | user |
| Stage blocked | Stage 3 predictive-to-causal provenance |

### UQ-PROV-003

| Field | Value |
| --- | --- |
| Question | Are result-generating commits and nested-repository commits recoverable? |
| Relevant paths | parent Git, `causal-irregular-time-series/`, `STraTS/`, final `run_summary.json` source paths |
| Why it matters | Current local nested commits may not equal producing-machine code states. |
| Evidence already inspected | Parent and nested `rev-parse HEAD`, run-summary absolute repo paths, dirty nested status. |
| Current best-supported interpretation | Local commits are known, but final run summaries do not record producing commit hashes. |
| Risk if unresolved | Exact code provenance for final results remains incomplete. |
| Recommended resolution | Recover producing commits from `/truenas`/`/workspace` logs, shell history, or result manifests. |
| Owner | user |
| Stage blocked | Stage 3 reproducibility |

## Missing Configuration

### UQ-CONFIG-001

| Field | Value |
| --- | --- |
| Question | Are local copies of configuration CSV files referenced through absolute paths available? |
| Relevant paths | `/truenas/home/kenzikob/.../configs/*-global-variables-[1-6].csv` |
| Why it matters | Exact run configuration cannot be independently checked. |
| Evidence already inspected | `find` found only unnumbered local config CSVs and one demo resolved config. |
| Current best-supported interpretation | Numbered final configs are missing locally. |
| Risk if unresolved | Causal run settings remain partially unverifiable. |
| Recommended resolution | Archive all final resolved config CSVs. |
| Owner | user |
| Stage blocked | Stage 3 methods |

### UQ-CONFIG-002

| Field | Value |
| --- | --- |
| Question | Does the folder suffix `-downsample` exactly correspond to config `DOWN_SAMPLE=True` in every final run? |
| Relevant paths | `outputs-*-downsample/run_summary.json`, `cate_cross_run_inventory.csv`, missing numbered configs |
| Why it matters | Sampling condition is parsed from folder names and reflected in outcome rates, but exact config files are absent. |
| Evidence already inspected | Cross-run parser, CATE outcome rates, run summaries. |
| Current best-supported interpretation | Strongly supported by folder names and outcome rates; exact config value still [CONFIGURATION MISSING]. |
| Risk if unresolved | Sampling labels could be challenged. |
| Recommended resolution | Verify numbered configs or add a derived-sampling validation note. |
| Owner | user |
| Stage blocked | Stage 3 sampling claims |

## Conflicting Result

### UQ-CONFLICT-001

| Field | Value |
| --- | --- |
| Question | Why does `outputs-physionet-forest/cate_estimation/` use `physionet_global_summary.csv` instead of `global_summary.csv`? |
| Relevant paths | `final-results/causal-outputs/outputs-physionet-forest/cate_estimation/physionet_global_summary.csv`, `cate_cross_run_inventory.csv` |
| Why it matters | Automated tools may miss or rank this differently; may indicate older output naming. |
| Evidence already inspected | Cross-run script selects `*_global_summary.csv` when richer than manager summary; inventory selected this file. |
| Current best-supported interpretation | The table is loadable and selected as primary for that run, but naming provenance is [PROVENANCE UNCLEAR]. |
| Risk if unresolved | Stage 3 may cite wrong or duplicate summary file. |
| Recommended resolution | Confirm whether file was renamed manually or produced by an older script version. |
| Owner | user |
| Stage blocked | Stage 3 exact artifact citation |

### UQ-CONFLICT-002

| Field | Value |
| --- | --- |
| Question | Why is `physionet_manager_global_summary.csv` inside a MIMIC run? |
| Relevant paths | `final-results/causal-outputs/outputs-mimic-linear/cate_estimation/physionet_manager_global_summary.csv` |
| Why it matters | The filename conflicts with the run dataset and could confuse provenance. |
| Evidence already inspected | File inventory and `compare_cate_runs.py` candidate scoring. |
| Current best-supported interpretation | It is a reduced manager-style duplicate in a MIMIC run; not selected as primary. |
| Risk if unresolved | Incorrect dataset attribution if cited directly. |
| Recommended resolution | Treat as duplicate/obsolete unless source history proves otherwise. |
| Owner | user |
| Stage blocked | Stage 3 artifact selection |

### UQ-CONFLICT-003

| Field | Value |
| --- | --- |
| Question | Do competing or duplicate summary files contain identical values? |
| Relevant paths | `cate_estimation/global_summary.csv`, `manager_global_summary.csv`, `physionet_global_summary.csv`, `*_manager_global_summary.csv` |
| Why it matters | Duplicate summaries differ in schema richness and may omit fields. |
| Evidence already inspected | Headers and row counts; cross-run script candidate scoring. |
| Current best-supported interpretation | Manager summaries are reduced duplicates; full global summaries should be preferred when available. |
| Risk if unresolved | Stage 3 may cite reduced or misleading duplicate artifacts. |
| Recommended resolution | Compare value equality for any exact artifact selected for thesis tables. |
| Owner | Codex/user |
| Stage blocked | Stage 3 table generation |

## Potentially Obsolete Artifact

### UQ-OBS-001

| Field | Value |
| --- | --- |
| Question | Are `causal-irregular-time-series/src/draft/` scripts retained only for history, and were any used in final results? |
| Relevant paths | `causal-irregular-time-series/src/draft/`, final run summaries |
| Why it matters | Draft scripts include older workflows and could be mistaken for active methods. |
| Evidence already inspected | `SCRIPTS.md`, `AGENTS.md`, run summaries stage script paths. |
| Current best-supported interpretation | Final causal runs use active scripts under `src/`, not `src/draft/`. |
| Risk if unresolved | Thesis methods may cite obsolete code. |
| Recommended resolution | Mark draft folder as legacy unless a result specifically references it. |
| Owner | user |
| Stage blocked | none if documented |

### UQ-OBS-002

| Field | Value |
| --- | --- |
| Question | Is `fix_preprocessor.py` obsolete after nested preprocessing changes? |
| Relevant paths | `fix_preprocessor.py`, `causal-irregular-time-series/src/preprocess_mimic_iii_large.py` |
| Why it matters | It edits source via an absolute local path and may represent a scratch fix rather than maintained workflow. |
| Evidence already inspected | Existing repository map, Git status. |
| Current best-supported interpretation | It is ad hoc; not part of final result generation evidence. |
| Risk if unresolved | Reproducibility docs may include unsafe scratch tooling. |
| Recommended resolution | Decide separately whether to remove, document, or commit it. |
| Owner | user |
| Stage blocked | none |

### UQ-OBS-003

| Field | Value |
| --- | --- |
| Question | Is `tmp_verify_router.py` still needed? |
| Relevant paths | `tmp_verify_router.py`, `tests/test_router.py` |
| Why it matters | Temporary verification scripts can confuse audit inventories. |
| Evidence already inspected | Git status and previous structural audit. |
| Current best-supported interpretation | It is scratch/temporary; not final evidence. |
| Risk if unresolved | Low; documentation clutter. |
| Recommended resolution | Convert useful checks into tests or remove in separate cleanup. |
| Owner | user |
| Stage blocked | none |

## Reproducibility Limitation

### UQ-REPRO-001

| Field | Value |
| --- | --- |
| Question | Can binary artifacts be used safely for thesis-relevant values? |
| Relevant paths | `checkpoint_best.bin`, `pt_saved_variables.pkl`, `*_model.pkl`, `*_trees.pkl` |
| Why it matters | Binary artifacts may require exact code/environment and may be unsafe/unportable to deserialize. |
| Evidence already inspected | File inventory and source writers/readers. |
| Current best-supported interpretation | Binary artifacts are support/intermediate evidence, not direct thesis tables. |
| Risk if unresolved | Stage 3 may depend on values unavailable from text/CSV summaries. |
| Recommended resolution | Prefer text/CSV summaries; use trusted loaders only if essential. |
| Owner | Codex/user |
| Stage blocked | Stage 3 only if a claim requires binary-only evidence |

### UQ-REPRO-002

| Field | Value |
| --- | --- |
| Question | Are raw data and processed pickles available with hashes/contracts? |
| Relevant paths | `/truenas/.../data/processed/*.pkl`, STraTS data paths, preprocessing scripts |
| Why it matters | Reproduction requires the raw/processed cohorts used to produce final outputs. |
| Evidence already inspected | Run summaries, local file inventory, preprocessing source. |
| Current best-supported interpretation | Processed pickles are referenced by absolute paths but not archived locally. |
| Risk if unresolved | Results cannot be reproduced from repository and `final-results/` alone. |
| Recommended resolution | Archive processed-data contracts, hashes, and access instructions without exposing restricted data. |
| Owner | user |
| Stage blocked | Stage 3 reproducibility limitations |

### UQ-REPRO-003

| Field | Value |
| --- | --- |
| Question | Does absolute-path usage reduce portability? |
| Relevant paths | `run_summary.json`, STraTS `training_summary.txt`, logs, scripts with relative defaults |
| Why it matters | Absolute `/truenas` and `/workspace` paths prevent direct reruns on another machine. |
| Evidence already inspected | Run summaries and training summaries. |
| Current best-supported interpretation | Yes; paths are valuable provenance facts but not portable instructions. |
| Risk if unresolved | Stage 3 reproduction section may overstate portability. |
| Recommended resolution | Document path remapping and repository-relative alternatives. |
| Owner | user |
| Stage blocked | Stage 3 reproducibility writing |

## Advisor Decision

### UQ-ADV-001

| Field | Value |
| --- | --- |
| Question | Which causal treatment concepts should be highlighted or tabled in the thesis? |
| Relevant paths | `cate_cross_run_summary.csv`, `cate_cross_run_cate_vs_matching.csv`, proxy definitions |
| Why it matters | Some concepts are direction-stable; others are near-zero, negative, or dataset-specific. |
| Evidence already inspected | Cross-run summary and report. |
| Current best-supported interpretation | Treatment-specific presentation is safer than one global conclusion. |
| Risk if unresolved | Thesis may overemphasize cherry-picked or clinically ambiguous concepts. |
| Recommended resolution | Advisor selects primary concepts and clinical framing. |
| Owner | advisor/user |
| Stage blocked | Stage 3 results narrative |

### UQ-ADV-002

| Field | Value |
| --- | --- |
| Question | Should MIMIC and PhysioNet dataset-specific latent names be harmonized in the main text? |
| Relevant paths | `terminology_map.md`, `compare_cate_runs.py` `CONCEPT_MAP`, tagger outputs |
| Why it matters | Some constructs align approximately, while MIMIC hepatic/coag is combined and PhysioNet has separate hepatic and coag/heme states. |
| Evidence already inspected | Cross-run concept map and tag headers. |
| Current best-supported interpretation | Harmonize only obvious concept variants; keep dataset-specific constructs distinct. |
| Risk if unresolved | Invalid cross-dataset replication claims. |
| Recommended resolution | Advisor approves concept grouping. |
| Owner | advisor/user |
| Stage blocked | Stage 3 cross-dataset comparison |

### UQ-ADV-003

| Field | Value |
| --- | --- |
| Question | Can clinical proxy-state claims be stated without external validation or chart review? |
| Relevant paths | `final-results/trees/`, tagger source, literature corpus |
| Why it matters | The tags are clinically inspired proxies, not verified diagnoses. |
| Evidence already inspected | Tagger outputs and literature guidance. |
| Current best-supported interpretation | Wording must remain proxy/weak-label language. |
| Risk if unresolved | Overstated clinical claims. |
| Recommended resolution | Advisor approves wording and limitations. |
| Owner | advisor/user |
| Stage blocked | Stage 3 clinical interpretation |

## Non-Blocking Cleanup

### UQ-CLEAN-001

| Field | Value |
| --- | --- |
| Question | Should generated bytecode and local scratch artifacts be cleaned from the repository? |
| Relevant paths | `__pycache__/`, `tmp_verify_router.py`, ignored/generated folders |
| Why it matters | Cleanup improves repository clarity but does not change Stage 2 evidence. |
| Evidence already inspected | File inventory and `.gitignore`. |
| Current best-supported interpretation | Cleanup is useful but outside allowed Stage 2 scope. |
| Risk if unresolved | Low; audit noise. |
| Recommended resolution | Separate cleanup PR/task after thesis evidence is stabilized. |
| Owner | user |
| Stage blocked | none |

### UQ-CLEAN-002

| Field | Value |
| --- | --- |
| Question | Should duplicate cross-run report formats both be retained? |
| Relevant paths | `cate_cross_run_comparison_report.md`, `cate_cross_run_comparison_report.docx` |
| Why it matters | Duplicates can drift if regenerated manually. |
| Evidence already inspected | Both files present; script writes both. |
| Current best-supported interpretation | They are intended duplicate formats from `compare_cate_runs.py`. |
| Risk if unresolved | Low; cite CSVs and `.md` for audit. |
| Recommended resolution | Keep both if script-generated; cite one canonical format in Stage 3. |
| Owner | user |
| Stage blocked | none |

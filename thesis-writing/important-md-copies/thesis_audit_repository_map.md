# CliniCause Repository Map

## Audit Metadata

- Repository root: `/mnt/c/Users/kobik/Desktop/הנדסת מערכות תקשורת/תואר שני/תזה/code/CliniCause`
- Current branch: `main`
- Audit date: 2026-07-12
- Working-tree state: dirty before audit. Pre-existing parent-repo changes were reported for `README.md`, `SCRIPTS.md`, `causal-irregular-time-series`, `fix_preprocessor.py`, `prompt.txt`, `requirements-full.txt`, `requirements-router.txt`, `requirements.txt`, `router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `tests/test_router.py`, `thesis-writing/literature/metadata/catalog.csv`, and `tmp_verify_router.py`; `thesis-writing/THESIS_PLAN.md` was untracked.
- Audit scope: structural repository audit only. Source code, configs, data, notebooks, outputs, figures, tables, literature files, and thesis prose were not modified.
- Commands or inspection methods used: `pwd`, `git rev-parse --show-toplevel`, `git branch --show-current`, `git status --short`, `git status --ignored --short`, `git ls-files --stage`, `git ls-files --others --exclude-standard`, `git submodule status`, selected `git log --oneline`, selected `git show --stat --name-only`, selected nested-repo `git status` and `git diff --stat`, `find` directory/file inventory, `rg --files`, targeted `rg` searches for entry points and artifact names, and small text reads of README, script index, requirement, config, test, and documentation files.

## Executive Structural Summary

`CliniCause` is a parent Git repository that combines a top-level router with two nested Git repositories: `causal-irregular-time-series` for preprocessing, clinical proxy-state tagging, DAG construction, and causal analysis, and `STraTS` for time-series model training and prediction export. The parent README and router documentation describe an intended end-to-end pipeline that writes run artifacts under `runs/`, but this audit did not execute any pipeline and did not treat file existence as proof of execution.

The repository also contains thesis-writing resources, a curated literature corpus, a previous thesis example, tests for router behavior, tracked generated-looking Python bytecode, tracked decision-tree PNGs, and a small `runs/validate_demo` artifact. No `.ipynb` notebooks were found by filename search.

## Top-Level Repository Map

| Path | Type | Apparent purpose | Evidence for classification | Thesis relevance | Status/uncertainty |
| --- | --- | --- | --- | --- | --- |
| `README.md` | Markdown | Parent overview of the unified CliniCause pipeline. | Describes causal irregular time-series pipeline, router, `causal-irregular-time-series`, and `STraTS`. | High; states intended architecture. | Modified before audit. |
| `SCRIPTS.md` | Markdown | Parent router usage and flag reference. | Lists `router.py` examples and important flags. | High; entry-point evidence. | Modified before audit. |
| `router.py` | Python source | Unified orchestration CLI for preprocessing, tagging, tree plotting, STraTS preparation/execution, prediction normalization, and thesis main pipeline. | `argparse` CLI, `STAGE_ORDER`, command builders, README references. | High; apparent top-level workflow coordinator. | Modified before audit; execution not confirmed. |
| `tests/` | Directory | Parent router tests. | `tests/test_router.py` imports `router.py` and tests stage parsing and command construction. | Medium; validates orchestration logic. | Modified before audit; `tests/__pycache__` is generated-looking and tracked. |
| `requirements.txt` | Dependency file | Project-wide Python dependencies for router and downstream scripts. | Header and package list. | Medium; environment evidence. | Modified before audit. |
| `requirements-router.txt` | Dependency file | Lightweight router-side dependency list. | Header and package list. | Medium; setup evidence. | Modified before audit. |
| `requirements-full.txt` | Dependency file | Aggregates router, causal repo, and STraTS requirements. | Contains `-r requirements-router.txt`, `-r causal-irregular-time-series/requirements.txt`, `-r STraTS/requirements.txt`. | Medium; setup evidence. | Modified before audit. |
| `causal-irregular-time-series/` | Nested Git repo/gitlink | Thesis research code for preprocessing, proxy-state tagging, DAGs, and causal analysis. | Parent `git ls-files --stage` shows mode `160000`; nested README/SCRIPTS describe active and legacy entry points. | High; core analysis implementation. | Parent marks modified; nested repo has a one-line local diff in `src/preprocess_mimic_iii_large.py`. |
| `STraTS/` | Nested Git repo/gitlink | Time-series model training, evaluation, and prediction-export workflow. | Parent `git ls-files --stage` shows mode `160000`; nested `SCRIPTS.md` describes training scripts and outputs. | High; predictive-model implementation. | Clean nested status at audit time; parent has gitlink but no `.gitmodules` mapping. |
| `runs/` | Directory | Stored run/output area for router executions. | Router default `--output-root runs`; contains `validate_demo/config/physionet_resolved_config.csv`. | Medium; may hold execution evidence. | Only small demo config observed; provenance unresolved. |
| `thesis-writing/` | Directory | Thesis planning, instructions, literature corpus, and example thesis resources. | Contains `literature/`, `general-instructions.pdf`, `context-dump.txt`, `example-omri-thesis/`, and untracked `THESIS_PLAN.md`. | High for thesis prose and citations. | `THESIS_PLAN.md` untracked before audit; literature catalog modified before audit. |
| `fix_preprocessor.py` | Python utility | One-off source editing helper for MIMIC preprocessing. | Reads and writes an absolute Windows path to `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`. | Low-to-medium; may explain local preprocessing edits. | Modified before audit; likely ad hoc, but status unresolved. |
| `tmp_verify_router.py` | Python utility | Temporary/ad hoc router command-construction verifier. | Imports `router.py`, builds SimpleNamespace contexts, prints command checks. | Low; overlaps with tests. | Modified before audit; temporary status unresolved. |
| `prompt.txt` | Text | Current Stage 2.1 audit instructions. | Contains the required procedure and deliverable templates. | High for this audit only. | Modified before audit. |
| `LICENSE` | License | Parent repository license. | Tracked top-level license file. | Administrative. | No uncertainty noted. |
| `__pycache__/` | Directory | Python bytecode cache. | Contains `router.cpython-39.pyc`; tracked in parent. | Low; generated-looking artifact. | Generated-looking and tracked; likely not thesis evidence. |

## Data and Preprocessing Areas

- `causal-irregular-time-series/src/preprocess_physionet_2012.py`: PhysioNet preprocessing entry point. `SCRIPTS.md` says it converts raw PhysioNet folders and outcomes into a processed `[ts, oc, ts_ids]` pickle. Source exposes `--raw-data-path`, `--output-path`, `--processed-dir`, and `--validate-config-only`.
- `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`: MIMIC-III preprocessing entry point. `SCRIPTS.md` says it converts raw MIMIC-III ICU tables into a PhysioNet-compatible processed pickle. Source exposes `--raw-data-path`, `--output-path`, `--chunksize`, `--tmp-dir`, and `--validate-config-only`; nested Git status shows a local line-ending-like change at the `main()` call.
- `STraTS/src/preprocess_physionet_2012.py` and `STraTS/src/preprocess_mimic_iii_large.py`: STraTS-side preprocessing scripts. `STraTS/SCRIPTS.md` says they build split-aware processed pickles under `STraTS/data/processed/`, using hardcoded relative raw-data locations.
- `causal-irregular-time-series/configs/physionet-global-variables.csv` and `causal-irregular-time-series/configs/mimic-global-variables.csv`: compact dataset config CSVs with dataset names, ID/outcome columns, treatment lists, latent ordering, covariates, model type, trial count, and run defaults.
- Raw clinical data directories were not present in the tracked inventory. Documentation says raw datasets must be available externally.

## Predictive-Model Areas

- `STraTS/src/main.py`: main predictive-model CLI for STraTS, iSTraTS, GRU, TCN, SAND, GRUD, and InterpNet. Source exposes model, pretraining, checkpoint, split, output, and prediction-export arguments.
- `STraTS/src/modeling_strats.py`, `modeling_gru.py`, `modeling_tcn.py`, `modeling_sand.py`, `modeling_grud.py`, `modeling_interpnet.py`: model implementations named by `STraTS/src/main.py`.
- `STraTS/src/dataset.py`, `dataset_pretrain.py`, `evaluator.py`, `evaluator_pretrain.py`, `models.py`, `learning_curves.py`, `utils.py`: training/evaluation support modules.
- `STraTS/run_main.sh`, `run_main_rest.sh`, `run_main_mimic.sh`, `run_full_main.sh`, and `run_strats_job.sbatch`: orchestration scripts for training and prediction export. Outputs are documented as `STraTS/outputs/...`, but no tracked `STraTS/outputs/` directory was found.

## Clinical Proxy-State Areas

- `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`: active PhysioNet rule-based proxy-state tagger according to `SCRIPTS.md`; outputs latent tag CSV and a decision-tree pickle.
- `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`: active MIMIC-III rule-based proxy-state tagger according to `SCRIPTS.md`; supports summary CSV, canonical pickle, or raw concept CSV inputs.
- `causal-irregular-time-series/src/majority_vote_latents.py`: combines voter CSVs into a majority-vote latent CSV.
- `causal-irregular-time-series/src/split_predicted_latent_tags.py`: splits combined predicted latent tags into probabilities and absolute tags.
- `causal-irregular-time-series/trees/`: tracked decision-tree PNGs for MIMIC and PhysioNet proxy-state rules. These appear generated from tagging/tree plotting workflows, but execution provenance was not confirmed.
- `thesis-writing/literature/README.md`: explicitly cautions that clinical tags should be described as derived proxy states/proxy phenotypes/weak clinical labels, not verified diagnoses.

## Causal-Inference Areas

- `causal-irregular-time-series/src/physionet2012_causal_graph.py` and `src/mimiciii_causal_graph.py`: active DAG builders/renderers, with dataset config and graph pickle/PNG output arguments.
- `causal-irregular-time-series/src/matching_causal_effect.py`: matched-pair causal effect summaries using DAG-guided confounders.
- `causal-irregular-time-series/src/cate_estimation.py`: CATE estimation with `CausalForestDML`, `LinearDML`, or `CausalPFN`, per `SCRIPTS.md` and CLI choices.
- `causal-irregular-time-series/src/analyze_cate_results.py`: analysis of saved CATE artifacts and sensitivity/benchmark outputs.
- `causal-irregular-time-series/src/permutations_test.py`: permutation sanity checks that call `cate_estimation.py`.
- `causal-irregular-time-series/src/draft/`: legacy causal/tagging scripts with old or hard-coded assumptions, according to `SCRIPTS.md`.

## Experiment and Evaluation Areas

- `router.py`: parent-level experiment orchestration across preprocessing, tagging, trees, STraTS, prediction normalization, and thesis main.
- `causal-irregular-time-series/main.py`: post-preprocessing causal pipeline orchestrator with stage sequence `graph`, `majority_vote`, `mortality_prediction`, `matching`, `cate_estimation`, `analyze_cate_results`, and `permutations_test`.
- `causal-irregular-time-series/scripts/run_main.sh`: wrapper around `main.py`.
- `causal-irregular-time-series/scripts/validate_global_variables_config.py` and `.sh`: config contract validation utilities; the shell script references active scripts with `--validate-config-only`.
- `STraTS/SCRIPTS.md` lists training scripts and outputs, but this audit did not run them.
- `tests/test_router.py` covers parent router argument parsing and command construction.
- `causal-irregular-time-series/tests/` contains tests for dataset config and MIMIC preprocessing contract.

## Results and Output Areas

- `runs/validate_demo/config/physionet_resolved_config.csv`: tracked resolved config artifact under the router's documented output root. It appears generated by a validation/demo run, but this is tentative because no manifest/log content was found under `runs/validate_demo/logs/` in the shallow inventory and no run was executed during audit.
- `causal-irregular-time-series/trees/`: tracked tree plots, likely generated outputs from decision-tree plotting. This is tentative because no command log or source artifact link was confirmed in this structural pass.
- `STraTS/.gitignore` excludes `outputs/`, `checkpoint_best.bin`, `log.txt`, `training_summary.txt`, and `pt_saved_variables.pkl`, indicating expected generated model artifacts are usually untracked.
- `causal-irregular-time-series/.gitignore` excludes stage output folders such as `graph/`, `majority_vote/`, `matching/`, `cate_estimation/`, `analyze_cate_results/`, `permutations_test/`, and standalone latent/mortality artifacts.

## Figures and Tables

- `causal-irregular-time-series/Thesis code Workflow.png`: workflow image referenced by the causal repo README.
- `causal-irregular-time-series/trees/mimic-trees/*.png`: 10 tracked MIMIC decision-tree figures.
- `causal-irregular-time-series/trees/physionet-trees/*.png`: 11 tracked PhysioNet decision-tree figures.
- `thesis-writing/example-omri-thesis/Figs/`: example thesis figures and an `.xlsx` file. These appear to belong to an example thesis, not necessarily to CliniCause results.
- No dedicated CliniCause result tables directory was found in the structural inventory.

## Configuration and Environment Files

- Parent environment files: `requirements.txt`, `requirements-router.txt`, and `requirements-full.txt`.
- Causal repo environment file: `causal-irregular-time-series/requirements.txt`, pinning the causal inference stack including `econml==0.16.0`, `scikit-learn==1.5.2`, `torch==2.3.1`, `causalpfn==0.1.4`, `faiss-cpu==1.9.0`, and `huggingface_hub==0.32.4`.
- STraTS environment file: `STraTS/requirements.txt`, listing PyTorch, scientific Python, Optuna, NetworkX, Matplotlib, Transformers, and `pytz`.
- Causal dataset configs: `causal-irregular-time-series/configs/physionet-global-variables.csv` and `mimic-global-variables.csv`.
- Config documentation: `causal-irregular-time-series/docs/global-variables-parameters.txt`.
- Ignore files exist in the two nested repos, but no top-level `.gitignore` was found.

## Documentation and Thesis Resources

- `README.md` and `SCRIPTS.md`: parent documentation for unified router setup and usage.
- `causal-irregular-time-series/README.md` and `SCRIPTS.md`: causal repo workflow and active/legacy script index.
- `STraTS/README.md`: placeholder-level README; `STraTS/SCRIPTS.md` contains the useful script inventory.
- `AGENTS.md` files in nested repos: development guidance files, not inspected in detail for this structural audit.
- `thesis-writing/literature/`: canonical literature corpus per its README, with `papers/`, `optional/`, and `metadata/`.
- `thesis-writing/context-dump.txt`: thesis context resource; not deeply audited.
- `thesis-writing/general-instructions.pdf`: thesis instructions PDF; not read because binary/PDF content is outside this structural pass.
- `thesis-writing/example-omri-thesis/`: example thesis LaTeX/PDF/resources, apparently reference material rather than CliniCause output.
- `thesis-writing/THESIS_PLAN.md`: untracked thesis planning file present before audit.

## Tests and Validation Utilities

- `tests/test_router.py`: parent router unit tests.
- `tmp_verify_router.py`: ad hoc command-building verifier; overlaps conceptually with router tests and prints results directly.
- `causal-irregular-time-series/tests/test_dataset_config.py`: dataset config tests.
- `causal-irregular-time-series/tests/test_preprocess_mimic_iii_large_contract.py`: MIMIC preprocessing contract tests.
- `causal-irregular-time-series/scripts/validate_global_variables_config.py`: config validation implementation.
- `causal-irregular-time-series/scripts/validate_global_variables_config.sh`: shell validation runner that expects the `econml310` conda environment.

## Generated, Archived, Duplicate, or Potentially Obsolete Material

- `__pycache__/` and nested `__pycache__/` directories: Python bytecode caches. They are generated-looking because of `.pyc` filenames and interpreter-version suffixes; some are tracked in the parent or nested inventories.
- `tests/__pycache__/`: generated-looking router test bytecode.
- `STraTS/src/__pycache__/`: generated-looking STraTS bytecode for multiple Python versions.
- `causal-irregular-time-series/src/__pycache__/`, `src/draft/__pycache__/`, and `tests/__pycache__/`: generated-looking causal repo bytecode.
- `causal-irregular-time-series/src/draft/`: described by `SCRIPTS.md` as legacy draft entry points with older path assumptions or older implementations. Do not delete based on this audit.
- `causal-irregular-time-series/trees/`: generated-looking decision-tree PNG outputs. They may be important thesis figures, but provenance and source command are unresolved.
- `runs/validate_demo/`: generated-looking router output area. It contains a resolved config but no confirmed execution evidence from this audit.
- `tmp_verify_router.py`: temporary-looking verifier because of its name and overlap with `tests/test_router.py`; its intended status is unresolved.
- `fix_preprocessor.py`: ad hoc source-modification helper using an absolute local path; its intended status is unresolved.
- `thesis-writing/example-omri-thesis/`: archived/reference example material for thesis formatting, not CliniCause evidence unless explicitly cited as such.

## Apparent Workflow Entry Points

| Entry point | Apparent role | Inputs | Outputs | Evidence | Execution status |
| --- | --- | --- | --- | --- | --- |
| `router.py` | Unified parent pipeline router. | Dataset selection, run ID, output root, raw data paths, config CSVs, stage list, nested repo roots. | Run directory under `runs/`, logs, resolved configs, processed pickles, latent tags, tree plots, STraTS predictions, thesis-main outputs. | Parent README/SCRIPTS and `argparse`/`STAGE_ORDER` in source. | implementation present, execution not confirmed |
| `causal-irregular-time-series/main.py` | Post-preprocessing causal pipeline orchestrator. | Dataset, config CSV, latent-tag voter directory, processed dataset pickle, output directory, model type. | Stage subdirectories, logs, `run_summary.json`, graph, majority vote, mortality, matching, CATE, analysis, permutation outputs. | Causal `SCRIPTS.md` and source `STAGE_SEQUENCE`. | implementation present, execution not confirmed |
| `causal-irregular-time-series/scripts/run_main.sh` | Shell wrapper for causal `main.py`. | Dataset, latent tags directory, dataset pickle, output directory, optional config CSV. | Same as `main.py`. | Causal `SCRIPTS.md` and shell argument parsing. | implementation present, execution not confirmed |
| `causal-irregular-time-series/scripts/validate_global_variables_config.py` | Validate compact dataset configs and script contracts. | Causal config CSVs and docs. | PASS/FAIL stdout and nonzero exit on validation errors. | Causal `SCRIPTS.md` and source. | implementation present, execution not confirmed |
| `causal-irregular-time-series/scripts/validate_global_variables_config.sh` | Shell wrapper for config and script `--validate-config-only` checks. | Config CSVs, active scripts, `econml310` environment. | PASS/FAIL stdout. | Causal `SCRIPTS.md` and shell content. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/preprocess_physionet_2012.py` | Build processed PhysioNet pickle. | Raw PhysioNet root, dataset config, output path. | Processed `[ts, oc, ts_ids]` pickle. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/preprocess_mimic_iii_large.py` | Build processed MIMIC-III pickle. | Raw MIMIC-III CSV root, dataset config, chunk/tmp options, output path. | Processed `[ts, oc, ts_ids]` pickle. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/tagging_latent_variables_physionet.py` | Generate PhysioNet proxy-state tags and trees. | Processed pickle, dataset config, optional thresholds. | Latent tag CSV and tree pickle. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py` | Generate MIMIC-III proxy-state tags and summaries. | Summary CSV, processed pickle, or raw concept CSVs; dataset config; output directory. | Latent tags, feature tags, summaries, co-occurrence CSV, tree pickle. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/decision_trees_plot.py` | Render decision-tree pickles. | Dataset name, tree pickle, output directory, format flags. | Rule diagrams under output directory. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/physionet2012_causal_graph.py` | Build/render PhysioNet DAG. | Dataset config and graph output paths. | Graph pickle and PNG. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/mimiciii_causal_graph.py` | Build/render MIMIC-III DAG. | Dataset config and graph output paths. | Graph pickle and PNG. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/matching_causal_effect.py` | DAG-guided matching estimates. | Latent tags, dataset pickle, graph pickle, config. | Matching folders and `global_summary.csv`. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/cate_estimation.py` | Treatment-effect estimation. | Latent tags, dataset pickle, graph pickle, estimator/model config. | Per-treatment CATE outputs, model pickles, summaries/control CSVs. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/analyze_cate_results.py` | Analyze saved CATE artifacts. | CATE results dir, latent tags, dataset pickle. | Benchmark reports/scores/contours and summary CSVs. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `causal-irregular-time-series/src/permutations_test.py` | Permutation sanity checks. | Latent tags, dataset pickle, graph pickle, trials, estimator type. | Treatment and outcome permutation CSVs. | Causal `SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `STraTS/src/main.py` | STraTS/baseline model training, validation, checkpointing, and prediction export. | Processed pickle, latent CSV, model/training/checkpoint flags. | Output directory with checkpoint/log/learning curves/summary and optional prediction CSV. | `STraTS/SCRIPTS.md` and parser flags. | implementation present, execution not confirmed |
| `STraTS/run_main.sh` | Compact PhysioNet STraTS workflow. | `data/processed/physionet_2012.pkl`, `data/latent_tags.csv`, generated checkpoint. | `outputs/physionet_2012/` and predicted latent tags CSV. | `STraTS/SCRIPTS.md` and shell content. | implementation present, execution not confirmed |
| `STraTS/run_main_rest.sh` | PhysioNet baseline workflow. | Processed PhysioNet pickle, latent CSV, checkpoints. | Baseline output dirs and per-model prediction CSVs. | `STraTS/SCRIPTS.md` and shell content. | implementation present, execution not confirmed |
| `STraTS/run_main_mimic.sh` | MIMIC STraTS/baseline workflow. | Processed MIMIC pickle, latent CSV, checkpoints. | MIMIC output dirs and prediction CSVs. | `STraTS/SCRIPTS.md` and shell content. | implementation present, execution not confirmed |
| `STraTS/run_full_main.sh` | Combined PhysioNet and MIMIC model workflow. | Processed pickles, latent tag CSVs, checkpoints created in script. | Dataset-specific outputs and prediction CSVs. | `STraTS/SCRIPTS.md` and shell content. | implementation present, execution not confirmed |
| `STraTS/run_strats_job.sbatch` | Slurm batch wrapper for STraTS job. | Cluster environment and script options. | Slurm output `strats_%j.out`. | File content and filename. | implementation present, execution not confirmed |

## Structural Risks and Ambiguities

- The parent repository tracks `STraTS` and `causal-irregular-time-series` as gitlinks, but `git submodule status` failed because no `.gitmodules` mapping was found for `STraTS`.
- The parent working tree was dirty before audit, so thesis evidence should distinguish committed baseline content from local modifications.
- `causal-irregular-time-series` was locally modified before audit; the nested diff showed a one-line change in `src/preprocess_mimic_iii_large.py`.
- Multiple orchestration layers exist: parent `router.py`, causal `main.py`, causal shell wrappers, and STraTS shell wrappers.
- `causal-irregular-time-series/src/draft/` preserves older implementations that could be mistaken for active methods.
- The repository includes generated-looking artifacts (`__pycache__`, decision-tree PNGs, `runs/validate_demo`) without full provenance in this structural pass.
- Top-level `.gitignore` was not found, while nested repos have their own ignore policies.
- Raw data, processed pickles, STraTS `data/`, STraTS `outputs/`, model checkpoints, and most run outputs are absent or ignored; later audits will need external provenance.
- `fix_preprocessor.py` and `tmp_verify_router.py` appear ad hoc and need status clarification.
- No notebooks were found, but the absence of notebooks does not establish that no external notebooks were used.

## Recommended Next Audit Targets

1. Clarify Git/submodule structure and local modifications before using the repository as thesis evidence.
2. Audit the parent `router.py` stage graph and its generated manifest/log conventions.
3. Audit causal preprocessing scripts and their processed-pickle contract for PhysioNet and MIMIC.
4. Audit proxy-state tagging scripts and the provenance of `causal-irregular-time-series/trees/`.
5. Audit causal DAG scripts and treatment/confounder configuration.
6. Audit CATE, matching, sensitivity, and permutation output contracts.
7. Audit STraTS data expectations, model scripts, checkpoint/prediction export behavior, and ignored output locations.
8. Audit `runs/validate_demo` and any external run directories for execution evidence.
9. Audit thesis-writing literature metadata after resolving the pre-existing modified `catalog.csv`.

## Limitations of This Structural Audit

- No training, preprocessing, evaluation, notebook, or analysis pipeline was executed.
- Binary/PDF contents were not read beyond filenames and metadata-level inventory.
- Large datasets, checkpoints, and untracked external artifacts were not searched outside the repository tree.
- Source files were read only selectively to identify purpose and entry-point structure.
- File existence was not treated as proof that a pipeline stage was executed.
- Methodology, clinical definitions, causal assumptions, and numerical results were intentionally not audited in this stage.

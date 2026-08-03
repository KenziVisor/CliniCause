# CliniCause script reference

This is the authoritative script reference for the integrated CliniCause repository. It brings together the root router, repository-wide launch helpers, the causal component, and STraTS. It documents locations and interfaces only; none of the commands below were run during the repository cleanup.

## Repository layout

- `router.py`: root-level integrated pipeline orchestrator.
- `scripts/`: repository-level launch helpers.
- `src/causal-irregular-time-series/`: causal preprocessing, tagging, graph, prediction, and causal-estimation component.
- `src/STraTS/`: time-series predictive-model component.
- `configs/`: protected configuration files. Do not generate or edit files here through these commands without a separate task.
- `results/`: protected result artifacts. Select an explicit external or run-specific output path instead of treating it as a scratch directory.
- `docs/`: local working documentation. Only the two final PDFs are tracked.

The component-local indexes, [causal SCRIPTS](src/causal-irregular-time-series/SCRIPTS.md) and [STraTS SCRIPTS](src/STraTS/SCRIPTS.md), remain in place because they document those folders. This document is the complete cross-repository index.

## Environment and execution prerequisites

- The router requires Python 3.9 or newer and the dependencies in `requirements.txt`.
- Commands that import the causal analysis stack normally use the `econml310` WSL Conda environment.
- Raw PhysioNet and MIMIC data must be available to the machine executing a real pipeline run.
- Relative defaults in both source components are fragile. Prefer explicit input and output paths for real runs.
- Training, preprocessing, inference, Slurm submission, containers, and causal estimation are operational commands, not cleanup validation commands.

## Root orchestration

### `router.py`

`router.py` is the public integrated entry point. It coordinates preprocessing, rule-based latent tagging, decision-tree plotting, STraTS input preparation and execution, prediction normalization, and the causal component's main pipeline.

The main arguments are:

- `--dataset {physionet,mimic,both}`
- `--run-id <name>`
- `--output-root <path>`
- `--thesis-repo-root <path>` and `--strats-repo-root <path>`
- `--strats-script-path <path>`
- `--stages <comma-separated-list>`
- `--physionet-raw-data-path <path>` and `--mimic-raw-data-path <path>`
- `--physionet-config-csv <path>` and `--mimic-config-csv <path>`
- `--cate-model {CausalForest,LinearDML,CausalPFN}`, `--down-sample`, `--trials`, and `--use-expanded-safe-confounders`
- `--seed`, `--overwrite`, `--resume`, `--dry-run`, `--validate-only`, `--skip-existing`, and `--fail-fast`
- `--python-executable`, `--verbose`, `--allow-existing-strats-inputs`, and `--run-strats {true,false}`
- `--preprocess-chunksize`, `--tmp-dir`, `--strats-max-concurrent`, `--strats-train-frac`, `--strats-model-run`, `--physionet-gpu`, and `--mimic-gpu`

The router discovers `src/causal-irregular-time-series/` and `src/STraTS/` by default. Explicit repository-root options remain available when an alternate checkout is intentional.

Example validation-only invocation:

```bash
python router.py --dataset both --run-id demo_run --strats-repo-root ./src/STraTS --validate-only
```

Example plan preview:

```bash
python router.py --dataset both --run-id demo_run --strats-repo-root ./src/STraTS --stages all --dry-run
```

Example full invocation:

```bash
python router.py \
  --dataset both \
  --run-id full_001 \
  --output-root runs \
  --thesis-repo-root ./src/causal-irregular-time-series \
  --strats-repo-root ./src/STraTS \
  --physionet-raw-data-path /path/to/physionet2012 \
  --mimic-raw-data-path /path/to/mimiciii \
  --stages all \
  --overwrite
```

## Project-level launch helpers

### `scripts/run_clinicause.sh`

This shell wrapper resolves paths from the repository root and invokes `router.py` using the active Python environment. It accepts environment variables including `DATASET`, `OUTPUT_ROOT`, `PHYSIONET_RAW_DATA_PATH`, `MIMIC_RAW_DATA_PATH`, `STAGES`, `STRATS_MAX_CONCURRENT`, `PYTHON_BIN`, and `RUN_ID` (or `CLINICAUSE_RUN_ID`).

```bash
STAGES=all bash scripts/run_clinicause.sh
```

`STAGES=dataset-extraction bash scripts/run_clinicause.sh` selects the dataset-construction-through-majority-vote preset. The wrapper requires the root `router.py` and both source-component directories to exist.

### `scripts/run_clinicause.sbatch`

This is the cluster submission wrapper for the complete pipeline. It requires `DATASET=physionet`, `DATASET=mimic`, or `DATASET=both`; it recognizes `OUTPUT_ROOT` and `CLINICAUSE_RUN_ID`. It contains site-specific Slurm, Apptainer, project-root, image, and Conda-environment settings, and invokes the root router against `src/causal-irregular-time-series/` and `src/STraTS/`.

Treat this as a maintained project-level launcher, but review its cluster-specific paths before submitting it on another system.

## Causal-pipeline entry points

All entries in this section live below `src/causal-irregular-time-series/`. Run their examples from that component root unless an example explicitly changes directory.

### Primary component orchestration

- `main.py` orchestrates graph construction, majority-vote latents, mortality, matching, CATE, saved-model analysis, and permutations. It accepts `--dataset`, `--dataset-config-csv`, latent-voter inputs, a processed `[ts, oc, ts_ids]` pickle, `--output-dir`, and optional `--model-type`; it writes stage directories, `logs/`, and `run_summary.json` below `--output-dir`.
- `scripts/run_main.sh` resolves and passes `--dataset`, `--latent-tags-dir`, `--dataset-pkl-path`, `--output-dir`, and optional `--dataset-config-csv` to `main.py`.
- `scripts/validate_global_variables_config.py` validates the compact dataset config CSVs and required config fields, reporting PASS/FAIL and using a nonzero exit status for validation errors.
- `scripts/validate_global_variables_config.sh` runs configuration and active-script validation checks through `econml310`.

The component's config-validation documentation names `configs/physionet-global-variables.csv` and `configs/mimic-global-variables.csv`; from the integrated repository root those protected files remain at exactly those paths.

### Preprocessing, graph construction, and proxy tags

- `src/preprocess_physionet_2012.py` accepts `--raw-data-path`, `--processed-dir`, or `--output-path` and writes the canonical PhysioNet `[ts, oc, ts_ids]` pickle.
- `src/preprocess_mimic_iii_large.py` accepts `--raw-data-path` and `--output-path` and writes a PhysioNet-compatible MIMIC `[ts, oc, ts_ids]` pickle.
- `src/physionet2012_causal_graph.py` and `src/mimiciii_causal_graph.py` accept optional dataset config, `--graph-pkl-path`, and `--graph-png-path` arguments and write a graph pickle plus rendered PNG.
- `src/tagging_latent_variables_physionet.py` accepts `--pkl-path`, `--output-csv-path`, `--optimized`, and `--thresholds-path`, producing a latent-tag CSV and matching decision-tree pickle.
- `src/tagging_latent_variables_mimiciii.py` accepts one of `--summary_csv`, `--pkl_path`, or raw-concept CSV inputs, plus optional `--output_dir`; it produces latent tags, feature-merged tags, validation/prevalence summaries, a co-occurrence CSV, and a decision-tree pickle.
- `src/majority_vote_latents.py` accepts `--input-dir` and `--output-path` for binary latent-tag voter CSVs and writes the majority-vote latent CSV.
- `src/split_predicted_latent_tags.py` accepts `--input-csv` and writes probability and absolute-tag CSVs beside it.
- `src/decision_trees_plot.py` accepts a dataset, decision-tree pickle, output directory, and optional format/overwrite flags and renders one figure per latent rule.

### Prediction and causal-estimation scripts

- `src/mortality_prediction_using_latents.py` takes latent tags, a processed dataset pickle, an optional dataset config, and writes a mortality report; the documented example uses `--model`, `--latent-tags-path`, `--dataset-pkl-path`, and `--results-txt-path`.
- `src/matching_causal_effect.py` takes latent tags, a processed dataset pickle, a graph pickle, an optional dataset config, and an `--output-dir`; the documented example uses `--model`, `--latent-tags-path`, `--dataset-pkl-path`, and `--graph-pkl-path`.
- `src/cate_estimation.py` accepts the same core inputs and `--model-type {CausalForest,LinearDML,CausalPFN}`; it produces per-treatment output plus run-level summary/control CSVs.
- `src/analyze_cate_results.py` accepts `--model`, `--results-dir`, `--latent-tags-path`, `--dataset-pkl-path`, and `--output-dir` to analyze saved CATE artifacts.
- `src/permutations_test.py` accepts `--model`, `--trials`, latent tags, dataset and graph paths, plus `--experiment-dir` for treatment- and outcome-permutation outputs.

### Legacy causal scripts

The runnable historical scripts remain under `src/draft/` and preserve their older path assumptions:

- `clinically_sufficient_tagging_latent_variables.py`: an older clinical/windowed PhysioNet tagger with a hard-coded processed-pickle input; it writes clinical tags, a tree pickle, and optional stage details.
- `optimize_latent_thresholds.py`: an Optuna threshold search for the older summary-statistics tagger; it uses a hard-coded processed-pickle input and `N_TRIALS`, writing optimized mortality results and thresholds.
- `causal_inference_on_latent_variables.py`: legacy PhysioNet stratification estimation labeled as CATE; it uses hard-coded latent tags, processed-pickle, and graph inputs and writes `cate_results.txt`.
- `causal_inference_on_latent_variables_updated.py`: conservative legacy PhysioNet ATE stratification; it uses the same class of hard-coded inputs and writes `ate_results_fixed.txt`.
- `physionet2012_causal_graph_old.py` and `mimiciii_causal_graph_old.py`: older graph builders with optional graph pickle/PNG output arguments.
- `tagging_latent_variables_physionet_old.py`: older PhysioNet rule tags from a processed pickle, with optional output CSV, optimization flag, and thresholds path.
- `tagging_latent_variables_mimiciii_old.py`: older MIMIC tags from summary CSV, canonical pickle, or raw-concept inputs, with optional output directory.
- `treatment_split.py`: a demonstration of treatment/control splits from hard-coded PhysioNet measurement and spacing rules; it prints split-size summaries.

They are preserved for comparison; inspect their hard-coded constants before using them. The component-local [causal script index](src/causal-irregular-time-series/SCRIPTS.md) retains the complete per-script examples and output descriptions.

### Component maintenance helper

`src/causal-irregular-time-series/scripts/fix_preprocessor.py` is a component-specific maintenance helper retained with the causal project. It targets that component's `src/preprocess_mimic_iii_large.py`; it is not an integrated public runner and must not be executed as part of a normal pipeline.

## STraTS predictive entry points

All entries in this section live below `src/STraTS/`.

- `src/main.py` is the main STraTS, iSTraTS, baseline-supervised, validation, checkpointing, prediction-export, and `--pretrain 1` CLI. It consumes `data/processed/{dataset}.pkl`, needs `--latent_csv_path` for supervised runs, and supports checkpoint, model-hyperparameter, split-control, and `--save_pred_csv_path` options. It writes `checkpoint_best.bin`, `log.txt`, learning curves, optional `training_summary.txt`, and optional prediction CSVs below `output_dir`.
- `src/preprocess_physionet_2012.py` builds the split-aware PhysioNet 2012 pickle consumed by `src/main.py`, from the component's documented hard-coded raw-data location, writing `data/processed/physionet_2012.pkl`.
- `src/preprocess_mimic_iii_large.py` builds the split-aware MIMIC-III pickle consumed by `src/main.py`, from the component's documented hard-coded raw-data location, writing `data/processed/mimic_iii.pkl`.
- `run_main.sh` is the compact PhysioNet pretrain, fine-tune, and prediction-export workflow. It uses the processed PhysioNet pickle and latent tags and writes PhysioNet model outputs plus predicted latent tags.
- `run_main_rest.sh` is the PhysioNet TCN, GRUD, GRU, SAND, and InterpNet baseline workflow. It uses the processed PhysioNet pickle, latent tags, and relevant checkpoints and writes per-model prediction CSVs.
- `run_main_mimic.sh` is the MIMIC STraTS/baseline training and prediction-export workflow. It uses the processed MIMIC pickle, latent tags, and its checkpoints and writes per-model prediction CSVs.
- `run_full_main.sh` combines the PhysioNet and MIMIC workflows, requiring both processed pickles, both latent-tag CSVs, and generated checkpoints.
- `run_strats_job.sbatch` is the component-specific Slurm submission script.

The documented STraTS paths are relative to the STraTS component root: processed pickles are expected below `data/processed/`, latent CSVs below `data/`, and outputs below `outputs/` unless overridden. Use the integrated router for cross-component handoffs. The component-local [STraTS script index](src/STraTS/SCRIPTS.md) remains the detailed reference for its runners.

## Internal helpers and local scratch files

The `src/` modules, component tests, and helper modules are implementation support rather than repository-wide launch commands. `scripts/tmp_verify_router.py` is an ignored local router-verification scratch file, not part of the tracked public project interface.

## Warnings and limitations

- The router and source scripts can create artifacts, use raw clinical data, and invoke expensive jobs. Select explicit output paths and do not assume a dry run validates scientific behavior.
- Do not assume source-component relative defaults resolve from the repository root.
- The two `configs/` files and all `results/` contents are protected by repository policy; this script index does not authorize changes to them.
- No command in this document was executed to validate behavior during the structural cleanup.

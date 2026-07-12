# Stage 2 Unresolved Questions

## Instructions

Questions in this file must arise from repository uncertainty. Do not invent generic questions.

## Repository Structure

- [ ] Are `STraTS` and `causal-irregular-time-series` intended to be managed as Git submodules, nested repositories, or vendored snapshots?
  - Relevant path(s): `STraTS/`, `causal-irregular-time-series/`, `.gitmodules`
  - Why it matters: The parent repository records both paths as gitlinks, but submodule metadata is missing; this affects reproducibility and checkout instructions.
  - Evidence inspected: `git ls-files --stage` showed mode `160000` for both paths; `git submodule status` failed with no `.gitmodules` mapping for `STraTS`; each nested path contains its own `.git` directory.
  - Suggested way to resolve: Inspect repository setup history and decide whether to restore `.gitmodules`, document manual clone steps, or convert these paths to regular tracked directories.

- [ ] Which pre-existing working-tree changes are part of the intended thesis evidence baseline?
  - Relevant path(s): `README.md`, `SCRIPTS.md`, `router.py`, `requirements*.txt`, `tests/test_router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `thesis-writing/literature/metadata/catalog.csv`, `tmp_verify_router.py`, `fix_preprocessor.py`, `prompt.txt`, `thesis-writing/THESIS_PLAN.md`
  - Why it matters: The audit must distinguish committed evidence from local edits when later stages cite repository state.
  - Evidence inspected: `git status --short` in the parent repository before creating audit deliverables.
  - Suggested way to resolve: Review each modified/untracked path, either commit intentional changes or document them as local-only before detailed evidence audits.

- [ ] Should generated Python bytecode remain tracked?
  - Relevant path(s): `__pycache__/`, `tests/__pycache__/`, `STraTS/src/__pycache__/`, `causal-irregular-time-series/src/__pycache__/`, `causal-irregular-time-series/tests/__pycache__/`
  - Why it matters: Bytecode is generated and may confuse structural inventories or reproducibility claims.
  - Evidence inspected: `find` inventory found many `.pyc` files; parent `git ls-files --stage` includes top-level bytecode entries; nested `.gitignore` files ignore `__pycache__/` and `*.py[cod]`.
  - Suggested way to resolve: Check whether these files are intentionally tracked or should be removed in a separate cleanup task.

## Data and Preprocessing

- [ ] What is the authoritative version of `causal-irregular-time-series/src/preprocess_mimic_iii_large.py` for future audits?
  - Relevant path(s): `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`, `fix_preprocessor.py`
  - Why it matters: The nested causal repo has a local modification, and the top-level helper appears capable of rewriting this preprocessing source file.
  - Evidence inspected: `git -C causal-irregular-time-series status --short`; `git -C causal-irregular-time-series diff --stat`; small read of `fix_preprocessor.py`.
  - Suggested way to resolve: Review the nested diff and decide whether to commit, discard, or document it before auditing preprocessing logic.

- [ ] Where are the raw and processed clinical datasets expected to live for reproducible runs?
  - Relevant path(s): `router.py`, `SCRIPTS.md`, `causal-irregular-time-series/src/preprocess_*.py`, `STraTS/src/preprocess_*.py`, `STraTS/data/`
  - Why it matters: Raw data and processed pickles are not present in the repository, but many entry points depend on them.
  - Evidence inspected: README/SCRIPTS files, parser flags, and directory inventories; no tracked raw data or STraTS `data/` directory was found.
  - Suggested way to resolve: Document external dataset locations, expected hashes/contracts, and which preprocessing path produces each downstream artifact.

## Predictive Modeling

- [ ] Which STraTS workflow is the current source of prediction CSVs used by the causal pipeline?
  - Relevant path(s): `STraTS/src/main.py`, `STraTS/run_main.sh`, `STraTS/run_main_rest.sh`, `STraTS/run_main_mimic.sh`, `STraTS/run_full_main.sh`, `router.py`
  - Why it matters: Several STraTS scripts export predictions, and the parent router can call STraTS; later audits need the actual workflow used.
  - Evidence inspected: `STraTS/SCRIPTS.md`, shell script inventory, and `router.py` stage names.
  - Suggested way to resolve: Locate run manifests/logs or command history showing which STraTS scripts produced the prediction CSVs used for thesis analysis.

- [ ] Are any model checkpoints or STraTS outputs available outside Git for audit?
  - Relevant path(s): `STraTS/outputs/`, `STraTS/.gitignore`, `runs/`
  - Why it matters: The repository ignores checkpoints and outputs, so predictive-model evidence may live outside the tracked tree.
  - Evidence inspected: `STraTS/.gitignore` and file/directory inventory; no tracked checkpoints or `STraTS/outputs/` directory were found.
  - Suggested way to resolve: Identify external output directories, checkpoint files, and prediction CSVs, then map them to generation commands.

## Clinical Proxy States

- [ ] What is the provenance of the tracked decision-tree PNGs?
  - Relevant path(s): `causal-irregular-time-series/trees/mimic-trees/`, `causal-irregular-time-series/trees/physionet-trees/`, `causal-irregular-time-series/src/decision_trees_plot.py`, tagger scripts
  - Why it matters: The PNGs may be thesis figures or generated diagnostics, but file existence alone does not prove how or when they were generated.
  - Evidence inspected: Tree file inventory, causal `SCRIPTS.md`, and entry-point parser search.
  - Suggested way to resolve: Locate matching tree pickle artifacts, run logs, or commit history showing the generation workflow.

- [ ] Which proxy-state/tagging implementation should be treated as current for PhysioNet and MIMIC?
  - Relevant path(s): `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`, `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`, `causal-irregular-time-series/src/draft/*tagging*`
  - Why it matters: Active and draft/old implementations coexist and could support different thesis claims.
  - Evidence inspected: Causal `SCRIPTS.md` labels active versus legacy draft entry points; directory inventory found both current and old taggers.
  - Suggested way to resolve: In the clinical proxy-state audit, compare active scripts to any run evidence and exclude draft scripts unless there is explicit use evidence.

## Causal Analysis

- [ ] Which causal estimator outputs, if any, are the thesis results based on?
  - Relevant path(s): `causal-irregular-time-series/src/cate_estimation.py`, `src/matching_causal_effect.py`, `src/analyze_cate_results.py`, `src/permutations_test.py`, ignored output directories
  - Why it matters: The implementation supports multiple estimators and output areas, but tracked result artifacts are not present.
  - Evidence inspected: Causal `SCRIPTS.md`, source parser search, `.gitignore`, and top-level file inventory.
  - Suggested way to resolve: Locate run directories, summaries, saved models, and logs; map each reported thesis result to the exact command and input artifacts.

- [ ] Which DAG versions are current versus legacy?
  - Relevant path(s): `causal-irregular-time-series/src/physionet2012_causal_graph.py`, `src/mimiciii_causal_graph.py`, `src/draft/physionet2012_causal_graph_old.py`, `src/draft/mimiciii_causal_graph_old.py`
  - Why it matters: Current and old DAG builders coexist, and downstream causal claims depend on the selected graph.
  - Evidence inspected: Causal `SCRIPTS.md` and source inventory.
  - Suggested way to resolve: Audit graph-generation logs/artifacts and compare active versus draft DAG outputs only if needed.

## Experiments and Results

- [ ] What produced `runs/validate_demo/config/physionet_resolved_config.csv`?
  - Relevant path(s): `runs/validate_demo/`, `router.py`
  - Why it matters: It is a tracked output-like artifact under the router output root, but this structural audit did not find enough provenance to classify it as confirmed execution evidence.
  - Evidence inspected: `find runs -maxdepth 4`, parent README/SCRIPTS, and router default output-root documentation.
  - Suggested way to resolve: Inspect file history and any logs/manifests; decide whether it is a demo fixture, validation artifact, or stale output.

- [ ] Is `tmp_verify_router.py` still needed?
  - Relevant path(s): `tmp_verify_router.py`, `tests/test_router.py`
  - Why it matters: It appears to duplicate router command-construction checks in a temporary script, which could confuse test/provenance inventories.
  - Evidence inspected: Small read of `tmp_verify_router.py` and `tests/test_router.py`.
  - Suggested way to resolve: Ask whether it is a scratch helper, convert useful checks into tests, or document it as obsolete in a separate cleanup task.

## Figures and Tables

- [ ] Which figure/table assets are thesis evidence versus formatting examples?
  - Relevant path(s): `causal-irregular-time-series/Thesis code Workflow.png`, `causal-irregular-time-series/trees/`, `thesis-writing/example-omri-thesis/Figs/`, `thesis-writing/example-omri-thesis/`
  - Why it matters: The repository contains both project-related figures and example-thesis assets that should not be conflated.
  - Evidence inspected: README references, directory names, and file inventory.
  - Suggested way to resolve: During the thesis resources audit, tag each figure/table as CliniCause evidence, workflow illustration, or external formatting example.

## Versioning and Obsolete Material

- [ ] Which files in `causal-irregular-time-series/src/draft/` are retained only for history, and were any used in reported results?
  - Relevant path(s): `causal-irregular-time-series/src/draft/`
  - Why it matters: The draft directory contains runnable old scripts with hard-coded path assumptions, and later audits need to avoid citing obsolete methods as active.
  - Evidence inspected: Causal `SCRIPTS.md` legacy section and draft directory inventory.
  - Suggested way to resolve: Use run evidence and commit history to determine whether any draft script participated in a result; otherwise document as archived/legacy.

- [ ] Is `fix_preprocessor.py` obsolete after the nested preprocessing changes?
  - Relevant path(s): `fix_preprocessor.py`, `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`
  - Why it matters: It edits source using an absolute local path and could represent a one-off repair rather than a maintained utility.
  - Evidence inspected: Small read of `fix_preprocessor.py`; parent and nested Git status.
  - Suggested way to resolve: Review commit history around MIMIC preprocessing fixes and decide whether to keep, document, or remove it in a separate non-audit cleanup.

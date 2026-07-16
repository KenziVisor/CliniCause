# Stage 4.2 Evidence Report

## 15.1 Git State

- Branch inspected: `main`.
- Inspected commit: `d7edc78 step 4.1`.
- Verification: `d7edc78` exists, follows `a1e7634 step 4.0`, and includes the Stage 4.1 Chapter 3/4 drafts, Stage 4.1 evidence report, placeholder/deferred-fix updates, and generated `thesis-writing/thesis/main.pdf`.
- Initial status was dirty before Stage 4.2.  Pre-existing unrelated changes included root files such as `README.md`, `SCRIPTS.md`, requirements files, router/tests, `prompt.txt`, copied thesis notes, literature catalog metadata, temporary verification code, and a modified nested `causal-irregular-time-series` checkout.
- Files changed by Stage 4.2: `thesis-writing/thesis/chapters/06_predictive_modeling.tex`, `thesis-writing/logs/unresolved_placeholders.md`, `thesis-writing/logs/deferred_fixes.md`, `thesis-writing/logs/stage_4_2_evidence_report.md`, and generated `thesis-writing/thesis/main.pdf` after final build.
- Final status after Stage 4.2 validation remained dirty, as expected, with the same unrelated pre-existing modifications plus Stage 4.2 edits to Chapter 6, the placeholder log, the deferred-fix log, generated `main.pdf`, and the new untracked evidence report.  No build intermediates remained after `latexmk -c`.

## 15.2 Toolchain and Baseline Build

- Tool paths verified: `/usr/bin/pdfinfo`, `/usr/bin/pdftotext`, `/usr/bin/latexmk`, `/usr/bin/xelatex`, `/usr/bin/biber`.
- Baseline command:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

- Baseline result: successful XeLaTeX/Biber build, generated `main.pdf`.
- Baseline page count: 38.
- Baseline warnings: nonfatal underfull hboxes in Chapter 4 and one nonfatal overfull hbox in the bibliography; no fatal error, undefined citation, or undefined reference was detected in the final baseline log scan.

## 15.3 Files Inspected

- Thesis and logs: `prompt.txt`, `thesis-writing/thesis/main.tex`, Chapter 3, Chapter 4, Chapter 6 skeleton, `stage_4_0_setup_report.md`, `stage_4_1_evidence_report.md`, `unresolved_placeholders.md`, `deferred_fixes.md`.
- Planning: `thesis_story.md`, `thesis_outline.md`, `chapter_evidence_map.md`, `terminology_and_notation.md`, `citation_plan.md`, `table_plan.md`, `figure_plan.md`, `writing_order.md`, `stage4_prompt_queue.md`.
- Audit: `repository_map.md`, `evidence_inventory.md`, `experiment_inventory.csv`, `claim_evidence_ledger.csv`, `terminology_map.md`, `unresolved_questions.md`.
- Literature: `literature/README.md`, `metadata/catalog.csv`, `metadata/references.bib`.
- STraTS data loaders: `STraTS/src/dataset_pretrain.py`, `STraTS/src/dataset.py`.
- STraTS evaluators and curves: `evaluator_pretrain.py`, `evaluator.py`, `learning_curves.py`.
- STraTS wrappers and metadata: `STraTS/SCRIPTS.md`, `STraTS/requirements.txt`, `run_main.sh`, `run_main_rest.sh`, `run_main_mimic.sh`, `run_full_main.sh`, `run_strats_job.sbatch`, `STraTS/AGENTS.md`.
- Parent router: `router.py`, root `SCRIPTS.md`.
- Downstream export-normalization scripts: `causal-irregular-time-series/src/split_predicted_latent_tags.py`, `causal-irregular-time-series/src/majority_vote_latents.py`, `causal-irregular-time-series/main.py`, `causal-irregular-time-series/AGENTS.md`.
- Predictive artifacts: `final-results/AGENTS.md`, `final-results/causal-outputs/AGENTS.md`, `final-results/strats-outputs/**/training_summary.txt`, `log.txt`, `checkpoint_best.bin`, `pt_saved_variables.pkl`, and `predicted*_latent_tags*.csv`; `STraTS/outputs` was absent.

## 15.4 Model Implementation Matrix

| model name | source file | input representation | irregularity/missingness handling | static-feature handling | pretraining support | supervised head | primary citation | implementation status | execution evidence | approved final-result status | limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STraTS | `modeling_strats.py`, `models.py` | irregular time/value/variable triplets | padding mask, variable dropout, train or pretraining normalization | learned demographic embedding | supported | scratch: combined embedding to binary head; checkpoint-loaded: forecasting head then binary head | `tipirneni2022strats` | IMPLEMENTATION-CONFIRMED | CONFIGURATION-CONFIRMED and EXECUTION-SUPPORTED by wrappers/logs | RESULT-ARTIFACT-PRESENT for CSVs | PROVENANCE-INCOMPLETE for checkpoint-to-export mapping |
| iSTraTS | `modeling_strats.py`, `models.py` | same initial triplets, pooled before contextualized representation | same loader/mask path as STraTS | raw static vector concatenation | supported | same shared head path | `tipirneni2022strats` | IMPLEMENTATION-CONFIRMED | wrapper support present through CLI choices | no approved final export found | unclear final experiment status |
| GRU | `modeling_gru.py` | dense hourly value/mask/delta grid | mean-fill, mask channels, elapsed-time channels | learned demographic embedding | not supported by pretraining guard | shared binary head | `cho2014gru` | IMPLEMENTATION-CONFIRMED | wrappers/logs and archived CSVs present | RESULT-ARTIFACT-PRESENT for CSVs | export provenance incomplete |
| GRU-D | `modeling_grud.py` | value, mask, delta tensors with sequence length | learned decays and masks in recurrent gates | learned demographic embedding | not supported by pretraining guard | shared binary head | `che2018grud` | IMPLEMENTATION-CONFIRMED | wrappers/logs and archived CSVs present | RESULT-ARTIFACT-PRESENT for CSVs | export provenance incomplete |
| TCN | `modeling_tcn.py` | dense hourly value/mask/delta grid | mask/delta channels on dense grid | learned demographic embedding | not supported by pretraining guard | shared binary head | `bai2018tcn` | IMPLEMENTATION-CONFIRMED | wrappers/logs and archived CSVs present | RESULT-ARTIFACT-PRESENT for CSVs | export provenance incomplete |
| InterpNet | `modeling_interpnet.py` | irregular times, values, masks, holdout masks | single-channel and cross-channel interpolation plus auxiliary reconstruction loss | learned demographic embedding | not supported by pretraining guard | shared binary head plus auxiliary loss in training | `shukla2019interpolation` | IMPLEMENTATION-CONFIRMED | wrapper entries present | no approved final export/training artifact found | must not be included in final numerical comparison until recovered |

## 15.5 Pretraining Contract

- Input fields: normalized values, scaled times, variable indices, observation mask, static covariates, forecast values, and forecast mask.
- Forecast-anchor logic: anchors are sampled from non-final observed timestamps and restricted to timestamps at least 720 minutes after record start.
- Context window: observations up to the anchor, limited by `max_obs`; MIMIC-III additionally uses at most a 24-hour context window.
- Target window: two hours after the anchor.
- Target construction: the last normalized future value per variable inside the target window is used.
- Masks: variables without future observations are masked out of the forecasting loss.
- Normalization: variable means and standard deviations are derived from pretraining train identifiers.
- Variable vocabulary: variables are restricted to those observed in the pretraining train split.
- Objective: masked squared error over forecasted variables.
- Evaluator behavior: materializes and caches three sampled batches per evaluation chunk for each split; returns `loss_neg`.
- Saved metadata: `pt_saved_variables.pkl` contains variables, means/stds, and maximum time; `checkpoint_best.bin` contains the best model state by validation `loss_neg`.
- Checkpoint-selection rule: pretraining uses validation `loss_neg`.

## 15.6 Supervised Contract

- Latent CSV schema: accepted identifier plus one column per proxy-label target.
- Accepted ID names: `ts_id`, `icustay_id`, `ICUSTAY_ID`.
- ID normalization: canonicalizes numeric-looking identifiers, drops alternate ID columns after consistency checks, and uses `ts_id`.
- Target-column derivation: all non-`ts_id` columns become target columns in CSV order.
- Loss: binary cross-entropy with logits.
- Class weighting: per-target positive-class weights are computed from the train split.
- Output shape: one probability or logit per target; number of targets is runtime-derived from the CSV.
- Metric calculations: per-target AUROC, AUPRC, and minRP; degenerate target columns are skipped; remaining per-target metrics are averaged.
- Checkpoint-selection rule: supervised training uses validation `auprc + auroc`.

## 15.7 Checkpoint-Loading Audit

- Intended warm-start flow: run STraTS/iSTraTS pretraining, save `checkpoint_best.bin` and `pt_saved_variables.pkl`, then run supervised checkpoint-loaded training with `--load_ckpt_path`.
- Actual active code flow: when `--load_ckpt_path` is supplied, the supervised model is constructed, the current state dictionary is read, the checkpoint state is loaded, overlapping keys are copied into the current state dictionary, and `model.load_state_dict(curr_state_dict)` is called.
- State dictionaries loaded: current supervised model state and checkpoint state from `args.load_ckpt_path`.
- Ignored or overwritten state dictionary: no ignored constructed state dictionary was found in the active code; stale local documentation still suggests a likely warm-start issue, but current `main.py` passes the merged state dictionary to `load_state_dict`.
- Supported model types: the pretraining guard permits only `strats` and `istrats`.
- Wrapper assumptions: wrappers configure pretraining and fine-tuning/export flows, but `run_full_main.sh` contains checkpoint/export patterns that differ from the archived export logs and from the baseline export wrappers.
- Artifact evidence: pretraining checkpoint/metadata artifacts and supervised checkpoints are present in the final archive for STraTS; archived prediction CSVs are present for four learned models per dataset, but export logs do not fully map each CSV to the intended supervised checkpoint.
- Conclusion: source-level warm-start loading is verified for compatible overlapping tensors, but successful pretrained initialization of every final exported prediction remains PROVENANCE-INCOMPLETE.

## 15.8 Export Contract

- Export flag: `--save_pred_csv_path`.
- Split selection: `--predict_split` with `train`, `val`, `test`, and `all`; `all` exports all supervised identifiers.
- Checkpoint reload behavior: immediately before export, the script reloads `checkpoint_best.bin` from the current output directory only if that file exists.
- Probability columns: one `<target>_prob` column per target.
- Binary columns: one target-named binary column per target.
- Threshold: probabilities are thresholded at `>= 0.5`.
- Normalization/splitting scripts: `split_predicted_latent_tags.py` separates probability and binary halves; `router.py` can collect and normalize STraTS prediction CSVs by dropping probabilities and enforcing latent ordering.
- Downstream voter requirements: voter CSVs must contain `ts_id` plus binary-only proxy columns with consistent latent columns across voters.
- Provenance limitations: final processed-pickle hashes, split-generation seed or identifier lists, checkpoint-to-export mapping, and archive-copy provenance remain incomplete.

## 15.9 Citations Used

- `tipirneni2022strats`: STraTS and iSTraTS irregular observation representation and self-supervised method context.
- `cho2014gru`: GRU recurrent baseline.
- `che2018grud`: GRU-D decay and missingness-aware recurrent baseline.
- `bai2018tcn`: TCN temporal convolution baseline.
- `shukla2019interpolation`: InterpNet interpolation-prediction baseline.

## 15.10 Placeholders

- Resolved Chapter 6 placeholders: generic `[STAGE 4 DRAFT REQUIRED]` placeholders in C6.1, C6.2, and C6.3; generic `[RESULT REQUIRED]` in C6.2; generic `[VALIDATION REQUIRED]` in C6.3.
- Newly added placeholders:
  - `[VALIDATION REQUIRED: recover a predictive manifest linking each final STraTS-family supervised checkpoint, pretraining checkpoint, export command, and exported CSV]`
  - `[RESULT REQUIRED: approved final InterpNet evaluation artifact before inclusion in the predictive performance comparison]`
  - `[VALIDATION REQUIRED: record the final export split, source processed-pickle hash, split-generation seed or ID manifest, source checkpoint, and archive-copy provenance for each prediction CSV]`
- Resolution stage: predictive result-manifest preparation before final Chapter 6 polishing and Chapter 10 numerical result writing.

## 15.11 Deferred Fixes

- Existing predictive issue confirmed: `DF-4.1-002` remains open.  Stage 4.2 found export logs supporting `predict_split=all`, but did not find the complete predictive manifest needed to resolve split/checkpoint/archive provenance.
- Issues resolved through evidence: the active warm-start code no longer matches the stale suspected issue in `STraTS/AGENTS.md`; no source repair was made because source loading is currently implemented.
- New Stage 4.2 deferred issues: `DF-4.2-001` through `DF-4.2-005` in `deferred_fixes.md`.
- Generated-PDF tracking-policy status: unresolved and recorded as `DF-4.2-005`.

## 15.12 Final Build

Final build command run from `thesis-writing/thesis`:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

- Return status: success (`0`).
- PDF path: `thesis-writing/thesis/main.pdf`.
- Page count: 44.
- Citation status: no unresolved citation warnings in the final `main.log` scan; `main.blg` scan found no Biber warnings or errors.
- Reference status: no undefined-reference warnings in the final `main.log` scan.
- Duplicate-label status: duplicate-label scan returned no duplicates.
- Fatal errors: none; no `LaTeX Error`, undefined control sequence, emergency stop, or fatal error was found.
- Remaining nonfatal warnings: 76 underfull hbox warnings, primarily from narrow methods/schema tables in Chapters 4 and 6; one overfull hbox warning in the bibliography at line 83 for the PhysioNet reference title.  Build intermediates were removed afterward with `latexmk -c`, retaining `main.pdf`.

## 15.13 Readiness

READY WITH NON-BLOCKING WARNINGS

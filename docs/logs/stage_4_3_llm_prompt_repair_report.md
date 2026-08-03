# Stage 4.3R LLM Prompt-Provenance Repair Report

## Git State

- Branch: `main`.
- Starting point for this repair: `0009d91 step 4.3 + prompts`.
- The worktree was already dirty before Stage 4.3R. Pre-existing unrelated changes included root documentation, router/test/requirements files, `prompt.txt`, important-md copies, literature catalog metadata, a modified nested `causal-irregular-time-series` checkout, generated thesis PDF state, and temporary verification files.
- No commit, reset, checkout, clean, staging, or push was performed.
- Prompt/document artifacts under `thesis-writing/prompts-and-documents/` were inspected read-only and not edited.

## Baseline Build

- Command sequence: `cd thesis-writing/thesis && latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.
- Baseline return status: `0`.
- Baseline PDF path: `thesis-writing/thesis/main.pdf`.
- Baseline page count observed before Stage 4.3R edits: `53`.
- Baseline warnings: the build completed with existing nonfatal layout warnings and no fatal LaTeX error.

## Artifact Inventory

The prompt/document archive contains 16 files:

- 5 prompt text files: generic final prompt, final PhysioNet prompt, final MIMIC prompt, old PhysioNet prompt, old MIMIC prompt.
- 5 exported prompt or deep-research PDFs: final PhysioNet prompt run, final MIMIC prompt run, old PhysioNet prompt result, old MIMIC prompt result, and a ChatGPT Deep Research CATE/proxy-validation report.
- 2 manager-summary PDFs and their 2 DOCX sources.
- 2 internal DOCX documents for thesis research question and clinical-CATE validation reference.

Artifact hashes and sizes are recorded in `thesis-writing/audit/llm_prompt_provenance_audit.md`.

## Prompt Architecture

The final prompt protocol is a staged clinical-causal elicitation template. It asks for dataset audit, candidate latent/proxy state identification, rule-based binary decision-tree proposals, missingness and measurement-process reasoning, DAG construction, iterative validation, and final structured representation.

The prompt contains strong elicitation language such as "true hidden clinical states", "causal correctness", and "clinically and causally justified latent DAG". Stage 4.3R marks these as prompt objectives, not thesis claims.

## Version Comparison

- `general-purpose-latent-causal-model-prompt.txt` and the final dataset prompts differ only in the two global variable assignments.
- `physionet-prompt.txt` sets `DATASET-NAME = PhysioNet 2012 Challenge` and the PhysioNet Challenge URL.
- `mimic-prompt.txt` sets `DATASET-NAME = MIMIC-III` and the MIMIC-III URL.
- The final PhysioNet and MIMIC prompts differ only in those dataset-specific global variables.
- Old-to-final prompt changes mainly introduce the reusable global-variable block and replace hard-coded dataset references with global variables.

## LLM Execution Metadata

- Final PhysioNet prompt run PDF: `physionet-prompt-running.pdf`, 45 pages, browser-export metadata created 2026-05-01 16:34:29 IDT.
- Final MIMIC prompt run PDF: `mimic-prompt-running.pdf`, 44 pages, browser-export metadata created 2026-05-01 16:33:37 IDT.
- User-supplied model metadata for final runs: ChatGPT 5.4 with extended reasoning.
- The PDF metadata records browser/export details but not the model-version field.
- Open execution-provenance gaps: exact research/browsing mode, settings, follow-up prompts, and output-export procedure.

## Output-Document Relationships

The prompt outputs and manager summaries are classified as design-provenance artifacts. They support a process claim that proxy ontology and DAG design were developed with LLM-assisted elicitation and later encoded in project source code.

They do not support claims that:

- The LLM executed the pipeline.
- The LLM learned causal graphs from patient-level records.
- The LLM outputs are clinical validation.
- The LLM outputs are the authoritative implemented proxy-state or DAG definitions.
- The LLM outputs prove identification or causal effects.

## Prompt-to-Code Traceability

The final PhysioNet prompt output aligns at a high level with the 11 active PhysioNet `LAT_*` proxy states. The final MIMIC prompt output aligns at a high level with the 10 active MIMIC `LAT_*` proxy states. Both final outputs include missingness or measurement-process concepts that are also represented in the graph design.

The authoritative implementation remains:

- `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`
- `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`
- `causal-irregular-time-series/src/physionet2012_causal_graph.py`
- `causal-irregular-time-series/src/mimiciii_causal_graph.py`

## Scientific Interpretation

Allowed thesis role: LLM-assisted design provenance for candidate clinical proxy ontology, rule families, missingness reasoning, and dataset-specific DAG design.

Disallowed thesis role: clinical validation, causal discovery, source-code execution, or proof of causal identification.

Preferred wording:

- "LLM-assisted clinical and causal elicitation protocol."
- "Candidate proxy-state ontology and DAG design proposals."
- "Project-specified DAGs subsequently encoded in source code."
- "Design-provenance artifacts."

Avoid:

- "LLM-discovered causal graph."
- "AI-validated clinical states."
- "Ground-truth latent states."
- "Clinically validated DAG."

## Planning Changes

Updated:

- `thesis-writing/planning/thesis_story.md`
- `thesis-writing/planning/citation_plan.md`
- `thesis-writing/planning/figure_plan.md`
- `thesis-writing/planning/terminology_and_notation.md`
- `thesis-writing/planning/table_plan.md`
- `thesis-writing/planning/writing_order.md`
- `thesis-writing/planning/stage4_prompt_queue.md`
- `thesis-writing/planning/chapter_evidence_map.md`

The planning files now describe prompt artifacts as design provenance, add `T-LLM-PROMPT-01`, and remove or qualify the older DAG-origin wording.

## Audit and Literature Changes

Added:

- `thesis-writing/audit/llm_prompt_provenance_audit.md`
- `thesis-writing/literature/llm_methodology_candidate_additions.md`

Updated:

- `thesis-writing/audit/repository_map.md`
- `thesis-writing/audit/evidence_inventory.md`
- `thesis-writing/audit/terminology_map.md`
- `thesis-writing/audit/unresolved_questions.md`
- `thesis-writing/audit/claim_evidence_ledger.csv`
- `thesis-writing/literature/README.md`

## Thesis Changes

Updated:

- `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex`
- `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`

Chapter 3 now says adjustment variables are selected from a project-specified DAG and clarifies that LLM-assisted elicitation was design provenance, while source graph scripts define the implemented artifacts.

Chapter 5 now includes `\subsection{LLM-Assisted Ontology and Rule Elicitation}` and Table `tab:llm-prompt-artifact-provenance`, separating prompt artifacts from source-code authority, executed artifacts, and clinical validation.

## Citation Gaps

Added `CIT-GAP-004` for prompt-engineering, transparent AI-assisted-research reporting, or exact ChatGPT 5.4 extended-reasoning documentation if LLM-assisted elicitation is framed as a formal methodology.

No bibliography entries were added during this repair.

## Placeholders

Added precise Chapter 5 placeholders:

- `[VALIDATION REQUIRED: record the final prompt execution settings, research or browsing mode, follow-up prompts, and output-export procedure for the ChatGPT 5.4 extended-reasoning runs]`
- `[SUPERVISOR DECISION REQUIRED: document the human and clinical review applied to the LLM-generated proxy-state and DAG design proposals]`

The model detail itself was not left as a placeholder because the user supplied it during the repair.

## Deferred Fixes

Added:

- `DF-4.3R-001` prompt execution provenance.
- `DF-4.3R-002` human and clinical review record.
- `DF-4.3R-003` LLM methodology citations.

## Validation Commands

Final validation commands included:

```bash
git diff -- thesis-writing/prompts-and-documents
rg -n "<unsafe and guardrail wording patterns>" thesis-writing/thesis thesis-writing/audit thesis-writing/planning thesis-writing/literature thesis-writing/logs
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

## Final Build

- Command sequence: `cd thesis-writing/thesis && latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.
- Return status: `0`.
- PDF path: `thesis-writing/thesis/main.pdf`.
- Final page count: `54`.
- Prompt artifact diff: empty; no files under `thesis-writing/prompts-and-documents/` were changed.
- Fatal/error scan: no `LaTeX Error`, `Undefined control sequence`, `Emergency stop`, `Fatal error`, `Biber error`, undefined citation, undefined reference, or multiply-defined label messages were found in the final `main.log`/`main.blg` scan.
- Wording scan: remaining matches are guardrail, limitation, or "wording to avoid" contexts in audit/planning/log files. No unsupported LLM-validation, learned-DAG, or clinical-validation claim was found in the thesis body.
- Nonfatal layout warnings: final `main.log` contains 23 overfull and 274 underfull hbox warnings. The largest overfull warning remains 35.53642 pt in a dense Chapter 5 proxy-definition table; the new prompt-provenance table contributes a small 9.29594 pt overfull warning after shortening file labels.

## Readiness

READY WITH NON-BLOCKING WARNINGS.

Stage 4.3R repaired the LLM/prompt-provenance framing, incorporated the user-supplied ChatGPT 5.4 extended-reasoning model metadata, kept prompt artifacts read-only, and produced a clean 54-page PDF build.

# Testbed Story Alignment — Step 2 Report

## 1. Baseline

- Branch: `main`.
- Step 2 baseline commit: `ea77b982d0ecd0ce99af63cd0315f71525e3a84b` (`ea77b98 edit thesis step 1`).
- The worktree was already dirty at the start of the step. The following pre-existing user changes were preserved and not edited as part of Step 2:
  - `prompt.txt`
  - `thesis-writing/advisor/clinical-evidence-supplement/dag_edge_evidence.csv`
  - `thesis-writing/advisor/clinical-evidence-supplement/proxy_evidence.csv`
  - `thesis-writing/advisor/clinical-evidence-supplement/source_registry.csv`
  - `thesis-writing/paper-aaai/mimic-mortality-voters.csv`
  - `thesis-writing/paper-aaai/physionet-mortality-voters.csv`
- No files were staged, committed, pushed, deleted, or reset during this step.

## 2. Scope

Step 2 implemented the intellectual reframe specified in `THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md`. The thesis is now introduced as a causal-estimator evaluation framework built around two distinct, clinically grounded observational testbeds. ICU data integration remains essential enabling infrastructure, but it is no longer the thesis's primary intellectual claim.

The step was intentionally limited to:

- the English and Hebrew administrative titles;
- Chapter 1 (Introduction);
- Chapter 2 (Background and Related Work);
- Chapter 3 (Problem Definition and Study Design);
- the bibliography entries required by the new evaluation-spectrum discussion; and
- the approved pipeline figure copied from the validated root source asset.

Chapters 4–10, abstracts, keywords, numerical result narratives, result tables, and the dataset-specific shock figure remain outside Step 2. The user's instruction that every paper result may be treated as checked and validated is recorded for later result-alignment work; no Step 4 numerical result was imported in this step.

## 3. Source Authority

The sources were applied in this order:

1. `prompt.txt` for the requested workflow and stop boundary.
2. `thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md` for the approved intellectual hierarchy and step scope.
3. `thesis-writing/logs/testbed_story_alignment_step_1_audit.md` for the Step 1 source map, freeze contract, and figure-source decision.
4. Existing thesis source for established terminology, design details, and frozen numerical content.
5. The validated paper and supplement as protected reference material. Per the user's clarification, their reported results may be assumed checked and validated even where a working-directory derivation is unavailable.

The Step 1 audit designates `thesis-writing/true-figure-1.png` as the authoritative pipeline image and explicitly supersedes the stale `paper-aaai/figures/figure1_pipeline.pdf`. The authoritative image was copied byte-for-byte to `thesis-writing/thesis/figures/clinicause_testbed_pipeline.png`; both files have SHA-256 `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`.

## 4. Work Performed

### Intellectual hierarchy

| Layer | Before Step 2 | After Step 2 |
|---|---|---|
| Primary claim | A reproducible integration-first ICU workflow | A framework for constructing two clinically grounded observational testbeds for causal-estimator analysis |
| Enabling contribution | Dataset harmonization was foregrounded as the main contribution | Explicit interfaces, deterministic processing, provenance, and cross-source harmonization enable the testbeds |
| Evaluation contribution | Estimator results appeared downstream of the integration story | Converging evidence and estimator agreement are central evaluation evidence, while omitted-confounding fragility remains explicit |
| Boundary | The distinction between observational evaluation and causal truth was less prominent | The testbeds do not manufacture ground-truth treatment effects or replace clinical validation |

### Chapter 1

Chapter 1 now:

- opens with the causal-estimator evaluation problem and the control-versus-realism tension;
- positions source-observed ICU cohorts as high-fidelity observational evaluation environments whose limitations must remain visible;
- frames CliniCause as a representation-layer intervention rather than a truth-generating mechanism;
- limits the language model's role to schema-level assistance, with deterministic execution and provenance retained in code;
- states that MIMIC-IV and PhysioNet 2012 form two distinct testbeds and are not pooled;
- introduces the approved pipeline figure and a matching caption and label;
- makes the testbed framework the primary objective and recasts integration as enabling infrastructure;
- preserves the frozen estimator hierarchy: CausalForestDML is primary, LinearDML is secondary, and CausalPFN is exploratory;
- preserves the frozen agreement summary: `19/19` primary comparisons and `18/19` secondary comparisons, with the PhysioNet shock exception retained; and
- updates the contribution hierarchy and chapter roadmap without importing later-step result prose.

The revised main research question is: How can irregular, heterogeneous ICU time series be transformed into clinically grounded observational testbeds that support transparent, reproducible, and appropriately bounded evaluation of causal estimators across distinct source environments?

The seven previous subquestions were consolidated into five:

1. Which causal-estimator evaluation setting is supported by source-observed ICU data, and what claims remain out of scope?
2. Which representation, exposure, outcome, and covariate contracts are required to construct comparable dataset-specific testbeds?
3. How can schema-level assistance, deterministic processing, provenance, and validation make construction reproducible and auditable?
4. How consistently do the estimators behave across tasks, models, horizons, and the two distinct testbeds?
5. Which conclusions are robust, and where do omitted confounding, overlap, measurement, or transportability limit interpretation?

### Chapter 2

Chapter 2 adds an explicit causal-estimator evaluation spectrum covering fully synthetic, semi-synthetic, experimentally anchored, empirically anchored generated, and source-observed testbeds. It explains why these settings provide complementary rather than interchangeable evidence and closes by locating CliniCause at the source-observed end of that spectrum.

### Chapter 3

Chapter 3 now defines a dataset-specific testbed contract and distinguishes source-observed, representation-defined, model-generated, derived, and project-specified elements. It formalizes the representation intervention, states that it does not create causal truth, keeps the two datasets separate, and aligns the study questions and the language-model boundary with the testbed-first framing.

### Title, figure, and bibliography

- English title: `CliniCause: Constructing Clinically Grounded Observational Testbeds for Causal Analysis from Irregular ICU Time Series`.
- Hebrew title: `CliniCause:` followed by the Hebrew translation of the new testbed-centered title.
- Added `fig:clinicause-testbed-pipeline` using the validated `true-figure-1.png` source.
- Added five bibliography records required by the evaluation-spectrum discussion: `shalit2017ite`, `shi2019dragonnet`, `alaa2019validating`, `gentzel2021experimental`, and `parikh2022validating`.

## 5. Frozen-Content Verification

The Step 1 inventories were compared with the post-edit source:

- Labels increased from 98 to 103. No pre-existing label was removed. The five additions are:
  - `fig:clinicause-testbed-pipeline`
  - `sec:background-related-work:causal-estimator-evaluation-spectrum`
  - `sec:introduction:causal-estimator-evaluation-problem`
  - `sec:introduction:representation-centered-observational-testbeds`
  - `sec:problem-definition-study-design:testbed-contract`
- Active citation keys increased from 36 to 41. No pre-existing active citation key was removed; the five additions are the five evaluation references listed above.
- Bibliography keys increased from 43 to 48. No pre-existing bibliography key was removed, and searches found one definition for each new key.
- Existing table bodies, figure filenames and captions, cohort definitions, exposure definitions, model definitions, estimator definitions, and numerical results were not changed.
- The intentional numeric/textual differences are limited to consolidating seven subquestions into five, section/list numbering, and bibliographic metadata for the five new references.
- The estimator hierarchy remains CausalForestDML primary, LinearDML secondary, and CausalPFN exploratory.
- The one rule voter plus four model voters and the five-source aggregate remain unchanged.
- The `19/19` primary, `18/19` secondary, MIMIC `9/9`, PhysioNet `9/10`, and PhysioNet shock-exception statements remain unchanged.
- The two source environments remain separate; no pooled cohort or pooled causal estimate was introduced.

## 6. Paper Protection

The protected paper source was checked before and after the work:

- `thesis-writing/paper-aaai/` contained 65 files before and after.
- The sorted file-manifest hash was identical before and after: `8d4255c108c4417d6b21fd3e788f1582e81b6f5e27519d3a115571acf27ca008`.
- The before/after manifests were byte-identical.
- Protected artifact hashes were unchanged:
  - `CausalDataGeneration.pdf`: `9c7a3473301fcab7a652985ed7f4fbf765a4de197eec53cc7ffe89a5996193f1`
  - root `aaai27.sty`: `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6`
  - supplement artifact: `a0fa0eca32b043877dbcdb98a357cb8eb4844416c856fe8a748781ac456d72b3`
- The root and paper copies of the protected source compared byte-for-byte equal.
- `ignore-paper-aaai` remained untouched.
- The two already-modified voter CSVs under `paper-aaai/` remained byte-identical to the Step 2 baseline. No paper file was changed by this task.

## 7. Validation

### Clean build

A fresh build was produced in `/tmp/clinicause_thesis_step2_clean_validation.KRfglb` from `thesis-writing/thesis` using:

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step2_clean_validation.KRfglb main.tex
biber --input-directory=/tmp/clinicause_thesis_step2_clean_validation.KRfglb --output-directory=/tmp/clinicause_thesis_step2_clean_validation.KRfglb main
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step2_clean_validation.KRfglb main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step2_clean_validation.KRfglb main.tex
```

The initial preferred `latexmk -xelatex` invocation did not run Biber because the repository's `latexmkrc` sets `$bibtex_use=2`; this was a build-driver configuration issue rather than a LaTeX source failure. The explicit XeLaTeX/Biber sequence above completed successfully.

The final artifact is `/tmp/clinicause_thesis_step2_clean_validation.KRfglb/main.pdf`:

- 108 A4 pages;
- SHA-256 `2c9bc021a3c333bedb2fb5b7de90a4b65809fe54c60bf469a31af5604373a229`;
- passed `qpdf --check`;
- no undefined citations or references;
- no duplicate labels;
- no missing-glyph warnings;
- no Biber warnings or errors; and
- one pre-existing `biblatex` language warning for Hebrew dummy-language handling.

There are nine small overfull-box warnings and one underfull bibliography-entry warning, all in source-unchanged list-of-tables, Chapters 5, 7, 9, 10, or bibliography content. None originates in the Step 2 edits to Chapters 1–3.

### Visual review

All 108 pages were rendered at 200 DPI to `/tmp/clinicause_thesis_step2_pages_clean_validation/` and individually inspected. The clean renders were also byte-compared with the previously reviewed render set and matched exactly at the pixel-file level.

Page-by-page review notes for source-induced or pagination-affected pages:

- Physical page 1: the new English title is centered, legible, and unclipped.
- Pages 5–8: every contents page was checked; entries, leaders, page numbers, and the new chapter pagination are sound.
- Page 11: the pipeline figure appears correctly in the list of figures.
- Pages 12–13: both list-of-tables pages were checked; page 13 remains a valid sparse tail page.
- Pages 14–21: every Chapter 1 page was checked. The revised hierarchy, main question, five subquestions, contribution ordering, and roadmap render cleanly. The pipeline figure on page 18 is sharp and readable, its labels remain visible, its caption is accurate, and the first in-text reference precedes it. Chapter 1 now closes on page 21 without an orphaned spill page.
- Pages 22–37: every Chapter 2 page was checked. The evaluation-spectrum section and citations render correctly; page 37 is a valid short chapter-ending page.
- Pages 38–42: every Chapter 3 page was checked. The testbed contract and provenance categories render cleanly; page 42 is a valid short chapter-ending page.
- Pages 43–102: every downstream page was individually inspected after the four-page pagination shift. No clipping, broken cross-reference, missing figure, degraded table, unintended blank page, or new layout defect was found. Sparse pages 28, 73, and 102 in the full document are intentional class/float or chapter-ending layouts. The integration-first main-question wording on physical page 86 and conclusion wording on pages 96–98 are expected temporary cross-step mismatches and are explicitly deferred to Step 4.
- Pages 103–107: every bibliography page was checked. All entries are legible; the five newly cited records appear as entries [20]–[24] on page 105.
- Page 108: the Hebrew cover renders right-to-left without clipping. A final language-quality review by a fluent Hebrew domain reader remains a release gate.

## 8. Git Diff Summary

The tracked Step 2 source diff, before adding this report, was:

```text
 thesis-writing/literature/metadata/references.bib   | 61 ++++++++++++++++++++
 thesis-writing/thesis/chapters/01_introduction.tex | 67 +++++++++++++++-------
 .../02_background_related_work.tex                 | 33 ++++++++++-
 .../03_problem_definition_study_design.tex         | 19 ++++--
 .../frontmatter/administrative_metadata.tex         |  4 +-
 5 files changed, 154 insertions(+), 30 deletions(-)
```

The new binary asset `thesis-writing/thesis/figures/clinicause_testbed_pipeline.png` and this report are untracked additions. The scoped Step 2 diff passes `git diff --check`.

The repository-wide `git diff --check` still reports pre-existing trailing-whitespace/CRLF findings in dirty CSV files listed in the baseline. Those files were not edited by Step 2 and their findings are not part of this change.

## 9. Remaining Issues

- Step 3 must align Chapters 4–8 and replace or reconcile the designated shock figure under the plan's source rules.
- Step 4 must align the abstracts, keywords, result interpretation, discussion, and conclusions. This includes the expected temporary integration-first wording still visible on the abstract pages and on physical pages 86 and 96–98.
- Any validated numerical result imported from the paper under the user's authorization belongs to Step 4, not this step.
- The Hebrew title should receive a final fluency review by a Hebrew-speaking domain expert before release.
- The repository's `latexmkrc` does not currently invoke Biber in the tested out-of-tree command; explicit Biber works and was used for validation.
- Existing downstream layout warnings may be revisited during the relevant chapter steps, but no warning introduced by Step 2 blocks progress.

## 10. Readiness

The Step 2 intellectual reframe is implemented within its approved scope. The title and Chapters 1–3 now establish the testbed-first story, the frozen numerical and design content remains intact, the protected paper is unchanged, and the full 108-page thesis builds and renders successfully. No Step 3 work has been started.

READY FOR STEP 3

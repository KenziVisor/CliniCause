# P4 Empirical Evaluation Report

## Execution identity

| Field | Value |
|---|---|
| Stage | P4 — Empirical Evaluation |
| Model | GPT-5.6 |
| Reasoning effort | High |
| Current HEAD before work | `14337a293eee03a24216c299c312ad5c7d61b3a7` (`AAAI P3`) |
| Branch | `main` |
| Last two commits inspected | `14337a2` (`AAAI P3`) and `a851e38` (`docs: record P3 commit evidence`) |
| Accepted P3 content commit | `60504040c86721782e6fdf8a29971c8b1e0ab9e4` (`paper: draft dataset construction and validation`) |
| STraTS nested revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal nested revision | `379ed9b75107b52007957ba5908e507b719c9247` |

## Repository state before work

The worktree contained one pre-existing modification: `prompt.txt`. It was user work, did not overlap the permitted P4 manuscript paths, and was treated as protected. The current HEAD was two commits after the accepted P3 content commit. Full inspection showed that the later commits changed the P3 report, `prompt.txt`, and tracked LaTeX auxiliary files; no manuscript source, evidence map, or build report changed after the P3 content commit.

Tracked LaTeX build artifacts (`paper.aux`, `paper.bbl`, `paper.blg`, `paper.fdb_latexmk`, and `paper.fls`) already existed. Repository cleanup was intentionally deferred by user decision. They were not removed, ignored, normalized, or treated as blockers; compilation regenerated the tracked artifacts it required.

No reset, restore, clean, deletion, staging, commit, or push was performed.

## Canonical plan and sources inspected

The canonical operational plan `clinicause_aaai27_paper_operational_plan.md` was read completely before editing. Its primary resource contribution, secondary evidence-tracked pipeline contribution, estimator hierarchy, positive CausalPFN positioning, original-versus-downsampled population hierarchy, no-pooling policy, page budget, and evidence gates governed the draft.

Sources inspected included:

- the complete current `paper.tex`, `paper_evidence_map.md`, `aaai_structure_notes.md`, `paper_build_report.md`, and P3 report;
- the complete results source packet, decision register, and manifest, plus checked predictive metrics/exports, CATE, matching, matching-failure, sensitivity, permutation, and cohort records;
- reproducibility lineage and provenance-gap records;
- thesis Chapters 3, 6, 7, and 8, with relevant implemented-protocol and interpretation passages from Chapters 10 and 11;
- the approved bibliography and exact DML/forest/EconML citation entries;
- current STraTS evaluator/model contracts and current causal matching, DML/PFN, downsampling, sensitivity, and permutation contracts, after reading both nested `AGENTS.md` files.

Current implementation was used only to verify method contracts. It was not attributed retroactively to the archived result production.

## Files changed

The intended P4 content is limited to:

1. `thesis-writing/paper-aaai/paper.tex`
2. `thesis-writing/paper-aaai/paper.pdf`
3. `thesis-writing/paper-aaai/paper_build_report.md`
4. `thesis-writing/paper-aaai/paper_evidence_map.md`
5. `thesis-writing/paper-aaai/reports/P4_empirical_evaluation_report.md`

Compilation regenerated pre-existing tracked LaTeX auxiliaries as permitted. No protected scientific evidence, thesis prose, bibliography, code, test, nested repository, result, planning, audit, log, data, or run file was edited.

## Manuscript structure and size

Section 4 is now titled `Empirical Evaluation` and contains:

1. `Prediction Tasks and Metrics`
2. `Effect Estimators and Cross-Estimator Evaluation`
3. `Matching and Robustness Diagnostics`

The section has eight substantive paragraphs. A LaTeX-stripped count is approximately 715 prose words (732 words including headings), within the requested range. The measured PDF footprint is approximately 0.86 physical page, from the Section 4 heading at page 3, y=254.54 pt, to the Section 5 heading at page 4, y=144.39 pt. This is within the requested 0.85–1.10-page range.

The former predictive/causal Results placeholders were moved into a distinct Section 5, `Results`, with three planned subsections. No numerical Results prose was written. Section 3 scientific prose was not edited; its existing final paragraph already provides a natural transition into empirical evaluation.

## Evaluation protocol drafted

### Prediction-task definition and verified metrics

Each dataset is evaluated as a separate multi-label task against its dataset-specific deterministic proxy-state vector. STraTS, GRU, GRU-D, and TCN are compared using the selected archived held-out test outputs; targets and scores are not pooled across datasets. The prose states once that this evaluates learnability and reproducibility of rule-derived constructs, not clinical-label validity or statistical superiority.

The verified metrics are:

- sample-mean multi-label binary cross-entropy test loss;
- macro AUROC;
- macro area under the precision–recall curve (AUPRC);
- macro minRP, defined per target as the maximum across thresholds of `min(precision, recall)`.

AUROC, AUPRC, and minRP are averaged over non-degenerate proxy targets; a target containing only one observed class on the evaluated split is skipped. The archive supplies point metrics without repeated-run uncertainty, confidence intervals, or significance tests, and the manuscript makes no such claim.

### Estimator roles and reported effect quantity

- `CausalForestDML` is the primary nonlinear heterogeneous-effect estimator, using DML adjustment, flexible nuisance models, and a causal-forest final stage.
- `LinearDML` is the main structured comparator, retaining the DML/nuisance framework with a linear final effect model for cross-model-form triangulation.
- `CausalPFN` is a meaningful complementary estimator from a distinct modeling perspective, evaluated over the same prespecified dataset–exposure comparisons to test whether directions are specific to the DML estimators.

For every dataset–exposure analysis, the reported quantity is the `mean model-estimated CATE over the analyzed sample`: the arithmetic sample mean of record-level fitted conditional-effect estimates. It is not described as a risk ratio, odds ratio, unqualified population ATE, or validated treatment effect.

### Cross-estimator comparison protocol and CausalPFN treatment

Directional triangulation compares CausalForestDML with LinearDML and then all three estimators across all prespecified dataset–exposure pairs. Disagreements remain explicit. The manuscript states that agreement does not require equal magnitudes and does not prove identification. It does not report the archived numerical agreement count, which remains reserved for Results.

CausalPFN is visible in the central estimator paragraph and in the triangulation protocol, rather than being reduced to a footnote. One precise boundary is stated: the archive contains less complete estimator-specific sensitivity and permutation support for CausalPFN than for the DML estimators. No unsupported CausalPFN methodological citation, architecture, training-corpus, novelty, or theory claim was invented.

### Matching protocol

The section describes the implemented binary matching representation: existing binary adjustment variables are retained, usable non-binary numeric variables are median-binarized, and exposed records are greedily matched one-to-one to available unexposed records by Hamming distance. Matching begins at distance zero and progressively relaxes the allowed distance until the configured maximum or sufficient pair-count/match-rate criteria. The outcome is named a `descriptive matched-pair outcome difference`; availability, final distance, and sufficient-pair warnings are retained. If no usable binary matching columns remain, the comparison fails explicitly rather than being assigned a zero effect.

### Sensitivity and permutation protocols

DML sensitivity support is described by provenance class: estimator-native saved output, later recomputation or labeled reconstruction, partial coverage, and unavailable/failed diagnostics are not conflated. No uniform exposure coverage is implied.

Treatment permutation disrupts the analyzed proxy-exposure column, while outcome permutation disrupts mortality and preserves the remaining run structure. Both are disruption-based sanity checks, not automatically formal randomization tests or identification proof. Equivalent stages were not archived for CausalPFN; the text presents this as a difference in the diagnostic package.

### Downsampling and cross-dataset policy

Outcome-downsampled analyses retain all mortality-positive records and sample mortality-negative records according to the implementation. They change the empirical population and outcome prevalence, test qualitative robustness to a major class-balance perturbation, remain robustness-only, and are not co-primary. Their magnitudes are not treated as directly interchangeable with original-population estimates.

The full analytical sequence is shared across both datasets to evaluate workflow portability under heterogeneous data contracts. Definitions and results remain dataset specific; cross-dataset evidence is compared without numerical pooling.

## Citations and evidence-map changes

Citation keys activated in P4:

- `chernozhukov2018dml`
- `wager2018causalforest`
- `athey2019grf`
- `oprescu_et_al_2019_econml`

All four exist in the approved bibliography and are used only for the supported DML, causal-forest, and EconML method-family statements. No CausalPFN citation was added.

The evidence map now records the P4 repository baseline and claims C41–C55, covering prediction-task scope, archived test-evaluation scope, metric definitions and degenerate-target handling, primary populations, exposure retention, all three estimator roles, the mean fitted-CATE summary, directional comparison, matching, sensitivity, permutations, downsampling, and no pooling. Each entry names its manuscript location, authoritative source, support status, qualification, and gate.

## Open gates and source conflicts

### TODO-EVIDENCE

- `G-EVD-01`: a verified primary CausalPFN bibliographic entry remains absent. P4 therefore makes no architecture, theory, novelty, or training-source attribution.
- `G-EVD-02`: exact producing revisions/configurations, processed-input hashes, predictive split identifiers, checkpoint-to-export linkage, and archive-copy lineage remain incomplete. P4 describes checked archived outputs, not an exact clean rerun.

### TODO-RUNTIME

- `G-RUN-01`: no current test-pass claim was added.
- `G-RUN-02`: no integrated rerun at the current revisions was performed or claimed.

No experiments or model runs were performed.

### TODO-RELEASE

- `G-REL-01`: no anonymous package/URL, license, or release instructions are evidenced. P4 adds no public-availability claim.

### Source conflicts

The thesis/results hierarchy calls CausalPFN exploratory, while the canonical paper plan requires it to be a meaningful complementary estimator. P4 follows the paper authority: CausalPFN is presented positively as complementary empirical triangulation, with one bounded statement about its smaller archived diagnostic envelope. Current repaired implementation contains stronger contracts than the archive; P4 uses it only for method-contract verification and does not identify it as producing code. The archive contains several sensitivity provenance classes; P4 explicitly preserves rather than merges them.

## Build and validation

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0 after BibTeX and three PDFLaTeX passes |
| PDF page count | 5 |
| PDF page size | 612 × 792 pt, US Letter |
| PDF SHA-256 | `13b28f0396fcb91baa830f9aaa57c96da1d65e4cb10d1748b249e1150da1f228` |
| Fonts | Four embedded/subset Type 1 fonts; no Type 3 fonts |
| Anonymity | Submission mode and `Anonymous submission` remain intact; no identity, affiliation, URL, or acknowledgment introduced |

No undefined citation, undefined reference, multiply defined label, missing file, horizontal overfull box, or fatal LaTeX warning remains. The pre-existing 33.21437 pt first-page overfull vertical-box diagnostic remains; full-resolution inspection shows no clipping, overlap, margin breach, or gutter collision. Underfull horizontal-box diagnostics are limited to ordinary paragraph/table justification and do not impair readability.

All five pages were rendered at 144 dpi and visually inspected. Section 3 flows directly into Section 4 on page 3. All three Section 4 subsection headings are correctly placed and readable; CausalPFN is clearly visible in the central estimator paragraph; the section continues naturally onto page 4 and ends before the separate Results heading. Columns, margins, and gutter are clear. Figure/Table placeholders remain inside bounds, captions remain below artifacts, references render correctly, and the whitespace on pages 4–5 is expected from the still-unwritten manuscript stages and deferred P5 floats.

## Protected-file verification and readiness

The canonical-plan SHA-256 remains `e70a485146631a3edf3f5358ec5e047e97db0967cd12a50a0388eed745f31b25`. `aaai2027.sty` remains `391bce82815bf698b8e382dd3ae7e30c75d7ab46df140cb295b1266016bc8623`, and `aaai2027.bst` remains `5db7765ba99de5c1e4686f9b3940a0add9c5e702f2164514462bec130ccb6e3c`. The protected prompt, operational plan, structure notes, P3 report, Author Kit, thesis, results, reproducibility, literature, logs, planning, audit, code, tests, data, logs, processed artifacts, and runs were not edited.

The Abstract was not written. No numerical Results prose was written. P3’s scientific contribution hierarchy was preserved, and Section 3 scientific prose was unchanged. CausalPFN was presented as a meaningful complementary estimator, and no unsupported CausalPFN methodological citation was invented. Repository cleanup was intentionally deferred by user decision. No experiments or model runs were performed. No commit or push was performed.

READY FOR STAGE P5 — EMPIRICAL EVALUATION DRAFTED

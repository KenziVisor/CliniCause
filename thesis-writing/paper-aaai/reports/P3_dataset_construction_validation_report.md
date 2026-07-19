# P3 Dataset Construction and Validation Report

## Execution identity

| Field | Value |
|---|---|
| Stage | P3 — Dataset Construction and Validation Draft |
| Model | GPT-5.6 |
| Reasoning effort | High |
| Current HEAD before work | `884ff8e4d112ff732e43a6aea33ab9bddcf8ed5e` (`AAAI skeleton`) |
| Task baseline | `884ff8e4d112ff732e43a6aea33ab9bddcf8ed5e` |
| Branch | `main` |
| Worktree state before work | Modified `prompt.txt` only. It was treated as pre-existing user work and was not edited, staged, restored, normalized, or committed. |
| STraTS nested revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal nested revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Commit SHA | `60504040c86721782e6fdf8a29971c8b1e0ab9e4` (`paper: draft dataset construction and validation`); this is the five-file P3 content commit. |

## Canonical plan and sources inspected

The canonical plan `thesis-writing/paper-aaai/clinicause_aaai27_paper_operational_plan.md` was read completely before editing. Its SHA-256 remained `e70a485146631a3edf3f5358ec5e047e97db0967cd12a50a0388eed745f31b25` after work.

Sources inspected for P3 included:

- `prompt.txt` in full; root `README.md`; both nested `AGENTS.md` files and nested repository summaries.
- `clinicause_aaai27_paper_operational_plan.md`, `paper_evidence_map.md`, `aaai_structure_notes.md`, `paper_build_report.md`, and the complete pre-P3 `paper.tex`.
- Thesis Chapters 3--8, with targeted results/discussion validation language from Chapters 10--11.
- `results_source_packet.md`, `results_decision_register.md`, checked cohort, predictive-export, CATE, matching, sensitivity, and permutation records, plus result manifests and checksums.
- Reproducibility README, artifact/data/predictive/causal lineage tables, and `provenance_gaps.csv`.
- Root `router.py` and router contract tests; relevant STraTS identifier, split, artifact, checkpoint, seed, and full-run source/tests; relevant causal repository orchestration, aggregation, preprocessing, determinism, and contract source/tests.
- Approved `references.bib` entries for the two datasets and four model families. No bibliography file was edited.

## Files changed

The P3 content commit is scoped to exactly these five permitted paths:

1. `thesis-writing/paper-aaai/paper.tex`
2. `thesis-writing/paper-aaai/paper.pdf`
3. `thesis-writing/paper-aaai/paper_build_report.md`
4. `thesis-writing/paper-aaai/paper_evidence_map.md`
5. `thesis-writing/paper-aaai/reports/P3_dataset_construction_validation_report.md`

LaTeX auxiliary files were generated locally for validation but are not intended for staging or commit.

## Section structure written

Section 3 is now titled `Constructing the CliniCause Datasets` and contains all five required scientific functions:

1. Source Cohorts and Analysis Units
2. Proxy-State Design and Deterministic Construction
3. Predictive Annotations from Irregular Time Series
4. Causal-Analysis Schema and DAG Metadata
5. Dataset Validation and Provenance

The section has 12 substantive paragraphs. A LaTeX-stripped count is approximately 1,214 words including headings, Table 1, and the Figure 1 caption; manuscript prose alone is correspondingly smaller. The PDF footprint is approximately 1.88 physical pages, measured from the Section 3 heading at page-1 y=350.95 pt to the Evaluation heading at page-3 y=253.98 pt. This is within the requested 1.80--2.10-page range.

## Table 1 values and authority

| Dataset | Primary analysis records | Admitted non-chronic proxy exposures | Outcome | Predictive annotation sources | Estimators |
|---|---:|---:|---|---|---|
| MIMIC-III | 26,845 | 9 | In-hospital mortality | One rule-derived source plus STraTS, GRU, GRU-D, and TCN | CausalForestDML, LinearDML, CausalPFN |
| PhysioNet 2012 | 7,993 | 10 | In-hospital mortality | One rule-derived source plus STraTS, GRU, GRU-D, and TCN | CausalForestDML, LinearDML, CausalPFN |

The record counts are authoritative in `checked_cohort_candidates.csv`. Exposure counts are the original-sampling unique exposure rows in `checked_cate_candidates.csv`. The five annotation sources and three estimator families are supported by the checked results source packet and archived run-family records. The caption states that these are analysis records and admitted non-chronic exposures, not raw source-cohort counts. No `Validation: Pass` field was added.

## Figure 1 specification

Figure 1 remains a correctly sized two-column layout placeholder rather than a fabricated scientific figure. Its final-quality caption centers resource construction and validation. The LaTeX production comment specifies three bands:

- design time: dataset descriptions and structured LLM proposals, project/human selection, deterministic tagger and graph source;
- construction/runtime: separate dataset lanes, preprocessing and canonical identifiers, deterministic rule labels, four predictive models, normalized exports, five-source proxy aggregation, outcome/covariates/DAG metadata, and validation gates;
- downstream characterization: CausalForestDML, LinearDML, CausalPFN, matching, and robustness diagnostics.

The central visual object is the pair of reusable estimator-ready causal-analysis datasets. The specification prohibits a patient-level runtime LLM interpretation and pooled dataset semantics and requires grayscale-safe, directly labeled, at-least-9-point vector artwork.

## Claims and evidence-map changes

Claims C26--C40 were added for analysis units, source-specific interfaces, LLM authority, deterministic proxy behavior, predictive representations and export contracts, five-source aggregation, resource/DAG schema, reuse, structural/cohort validation, provenance validation, archive/current-code separation, analytical execution, and the exact definition of `validated causal-analysis datasets`.

C17 was updated from a generic gated statement to `SUPPORTED WITH QUALIFICATION`: current source and tests support the existence of the repaired contracts, while `TODO-RUNTIME G-RUN-01` still blocks test-pass wording and archived attribution. Existing C02--C05, C08, C17, and C25 are connected to exact Section 3, Table 1, and Figure 1 locations. A dedicated Table/Figure evidence block and P3 citation-key register were added.

## Citation keys used

- `johnson2016mimiciii`
- `silva2012physionet`
- `tipirneni2022strats`
- `cho2014gru`
- `bai2018tcn`
- `che2018grud`

All keys exist in the approved bibliography. No CausalPFN citation or theory/novelty attribution was added because its primary citation remains gated.

## Open TODOs and evidence boundaries

### TODO-EVIDENCE

- `G-EVD-01`: verified primary CausalPFN bibliographic entry remains absent. P3 names the estimator only as a represented downstream workflow and makes no unsupported method-attribution claim.
- `G-EVD-02`: exact producing revisions/configurations, processed-input hashes, predictive split identifiers, checkpoint-to-export linkage, voter byte/hash manifests, and archive-copy direction remain incomplete. P3 explicitly separates checked archived artifacts from repaired current code.

### TODO-RUNTIME

- `G-RUN-01`: `python` is unavailable; `python3 -m pytest` cannot start because `pytest` is not installed. No current test-pass claim is made.
- `G-RUN-02`: no integrated rerun at the current frozen revisions was performed or claimed; experiments and models were not run.

### TODO-RELEASE

- `G-REL-01`: no anonymous release URL, license, source-data access instructions, or submission package is evidenced. P3 makes a design-level reuse claim but no public-availability or release claim.

### Other retained gates

- `TODO-HUMAN G-HUM-01`: final Figure 1 artwork/emphasis and contribution ratification remain for the authors/supervisor.
- `TODO-AAAI G-AAAI-01`: mutable submission rules must be rechecked immediately before submission.

## Source conflicts and resolutions

- Archived aggregation code aligned shared intersections, while repaired current contracts reject silent cohort intersections. P3 describes the archived five-source aggregate as an archived artifact fact and attributes strict equality/rejection behavior only to current validation contracts.
- Current repaired router/STraTS contracts postdate portions of the archive. P3 does not retroactively identify them as producing code.
- The checked archive validates schemas, counts, manifests, checksums, and recorded stage completion but lacks complete production lineage. The prose presents both facts together without converting artifact integrity into exact rerun reproducibility.
- The operational plan promotes a positive CausalPFN role, but the approved bibliography lacks its primary reference. P3 lists the estimator in the resource schema/table without adding method claims.

## Build and PDF validation

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success, exit code 0; BibTeX and cross-references resolved |
| PDF page count | 4 |
| PDF page size | 612 x 792 pt, US Letter |
| PDF SHA-256 | `f37022cb5a45e54ba113b1eb3e84b8d6aa0534fa2bb627efe8e707b774952510` |
| Layout | Official anonymous AAAI two-column submission format |
| Fonts | Embedded/subset Type 1; no Type 3 fonts |

LaTeX warnings: no undefined citation/reference, duplicate-label, missing-file, or fatal warning remains. One 33.21437 pt overfull vertical-box diagnostic occurs during the partially populated first-page skeleton composition; full-resolution inspection shows no clipping, overlap, gutter/margin breach, or readability effect. Underfull horizontal-box diagnostics are limited to ordinary paragraph/table justification. The first-page vertical diagnostic must be rechecked after later placeholders and the empty Abstract are replaced.

Every PDF page was rendered and visually inspected. Section 3 is readable without code or thesis access. Figure 1 and Table 1 remain inside margins; both captions are below their artifacts. The table is readable at the permitted 9-point size. The anonymous block, US-Letter page size, two columns, title, margins, and page-number suppression remain intact. Pages 3--4 retain expected skeleton whitespace and placeholders for later stages.

## Protected-file verification

- No Author Kit, thesis, result, reproducibility, literature, bibliography, planning, audit, log, code, test, nested repository, data, run, or prompt file was modified by P3.
- The canonical-plan hash remains the frozen value.
- `aaai2027.sty` and `aaai2027.bst` remain at their frozen hashes.
- The only pre-existing dirty file, `prompt.txt`, remains modified and unstaged.
- Generated LaTeX auxiliaries are excluded from the intended staged list.

## Staged-file list

Confirmed before the content commit with `git diff --cached --name-only`: exactly the five paths in `Files changed` were staged. `git diff --cached --check` passed. Pre-existing `prompt.txt` and generated LaTeX auxiliaries were not staged.

## Readiness decision

The complete resource section, validation definition, Table 1, Figure 1 specification, claim evidence, build record, and visual audit satisfy the P3 completion standard. Remaining evidence/runtime/release items are explicitly bounded and do not block the P3 manuscript draft.

READY FOR STAGE P4 — RESOURCE CONTRIBUTION DRAFTED

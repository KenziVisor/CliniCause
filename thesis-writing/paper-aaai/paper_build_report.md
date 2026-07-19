# CliniCause AAAI-27 baseline and skeleton build report

Date: 2026-07-19

Task scope: P0, P0A, P1, and P2 mechanical/evidence foundation only.

## Execution identity

| Field | Value |
|---|---|
| Model used | GPT-5.6 |
| Reasoning effort | High |
| Current parent HEAD | `c335d327b3ca63045d362f180518a2bfa7005e6e` on `main` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` (clean detached nested worktree) |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` (clean detached nested worktree) |
| Full-run pointer commit noted | `d3195458` (`Complete run pipeline`); no root archived run manifest found |

## Files inspected

- Canonical operational plan and `prompt.txt`, both completely.
- Parent/nested Git status and histories; root and nested repository guidance.
- Complete AAAI-27 Author Kit: anonymous/camera-ready sources and PDFs, checklist source/PDF, style, bibliography style, and kit bibliography.
- Official current AAAI-27 call, submission, supplement, conference, and publication-policy pages.
- Three official AAAI proceedings examples selected for resource/pipeline and causal-paper genre structure.
- Thesis main source/PDF, abstracts, Chapters 1–8 and 10–12, figure/table guidance, and build guidance.
- Results source packet, manifest/checksums, decision/figure registers, and all checked result families used by the evidence map.
- Reproducibility README, artifact/data/environment/source/run/copy lineage tables, checksums, and provenance gaps.
- Approved literature metadata/bibliography and its CausalPFN coverage.
- Historical `final-results` guidance and causal-output guidance.
- Current router validation implementation and router-contract tests.

## Files created or updated

| File | Function |
|---|---|
| `paper_evidence_map.md` | Frozen revisions/hashes, authority hierarchy, protected numerical baseline, result-family register, claim lock, conflicts, and evidence/runtime/release/human/AAAI gates |
| `aaai_structure_notes.md` | Official constraints, kit contract, genre study, exact architecture, seven-page budget, visual plan, supplement boundary, and checklist preparation ledger |
| `paper.tex` | Anonymous AAAI-27 structural skeleton with an intentionally empty abstract, exact section hierarchy, labeled float placeholders, evidence comments, gates, and approved bibliography path |
| `paper.pdf` | Compiled, visually audited skeleton |
| `paper_build_report.md` | This verification report |

No scientific manuscript paragraphs were drafted. Rendered text is limited to the approved working title, headings, anonymous marker, structural planning labels, and planned-placeholder captions.

## Author Kit findings

- Required base is `\documentclass[letterpaper]{article}` plus `\usepackage[submission]{aaai2027}` and the kit's URL, graphics, Natbib, caption, spacing, and PDF-template metadata settings.
- PDFLaTeX is enforced/supported; submission mode provides anonymous-review rendering, US-letter page size, two columns, and suppressed page numbers.
- The style/bibliography files resolve from `AuthorKit27` without modification.
- `booktabs` is the only added package; no forbidden layout, font, hyperlink, navigation, or spacing package/command was added.
- Captions are below their planned figures/tables. The checklist is not included in `paper.pdf`.
- Anonymous and camera-ready kit examples each render as 10 US-letter pages; the checklist example renders as two pages.

## AAAI structure findings

- Current official limit: 7 technical pages and at most 9 pages total, with pages beyond 7 restricted to references.
- The reproducibility checklist is a separate upload, resolving the generic kit sample's input/standalone ambiguity.
- Main paper must be self-contained; supplement is optional to reviewers and has document, media, and code/data channels.
- Evidence intended for review must be available at submission rather than promised only after acceptance.
- Genre examples support a first-page problem/resource/contribution frame, early pipeline orientation, compact related work, result-led figures/tables, and explicit consolidated limitations.
- Locked architecture: Introduction; Related Work; CliniCause Resource and Pipeline (three subsections); Evaluation (three subsections); Discussion and Limitations; Conclusion.

## Evidence sources and protected claims

Primary numerical authority is the checked results package and its manifest/checksums. Thesis chapters supply definitions and bounded interpretation; reproducibility tables supply lineage and gaps; current code/tests support only statements about the current static validation contract.

Verified protected facts include:

- 26,845 MIMIC-III and 7,993 PhysioNet majority-vote causal analysis records.
- 9 and 10 original-sampling proxy exposures, respectively; 57 estimator-exposure rows.
- STraTS is the checked MIMIC-III archived leader and GRU-D the checked PhysioNet archived leader on all four reported predictive metrics, without a significance claim.
- ForestDML/LinearDML direction agrees in 19/19 combinations; all three estimators agree in 18/19, with PhysioNet shock as the exception.
- Original/outcome-downsampled direction agrees in 55/57 rows; the two exact exceptions are recorded.
- Sensitivity and permutation/matching evidence is explicitly partial/diagnostic, with skipped, failed, and insufficient-support states kept distinct.

The evidence map preserves the complete eight-row predictive metric table and 19×3 original-sampling CATE matrix, with full-precision files named as authority.

## Source conflicts found and resolved

- Official AAAI-27 instructions override the generic kit's checklist ambiguity: separate upload, not manuscript input.
- Historical `final-results` revisions are audit-snapshot facts, not the current baseline or automatically the producing revisions.
- Current validation code is newer than portions of the archive and is not retroactively attributed to result production.
- The thesis's cautious CausalPFN position and the paper plan's central concordance result are reconciled by treating CausalPFN as complementary empirical triangulation, still gated on a primary citation and bounded limitations.
- Current official pages resolve the operational plan's tentative page-limit and checklist questions.

## Unresolved gates

| Gate | State and consequence |
|---|---|
| TODO-EVIDENCE | Primary CausalPFN citation missing; complete producing revisions/numbered configurations and predictive split/checkpoint linkage remain incomplete. Drafting can proceed only with gated/bounded language. |
| TODO-RUNTIME | `pytest -q` could not start because `pytest` is unavailable; no current test pass or integrated rerun is claimed. |
| TODO-RELEASE | No evidenced anonymous URL/package, license, access instructions, or final supplement contents; public-availability/checklist claims are blocked. |
| TODO-HUMAN | Contribution hierarchy, main visuals, authorship/track, ethics/privacy language, identity metadata, and final anonymization require author/supervisor decisions. |
| TODO-AAAI | Recheck mutable official rules immediately before submission. |

These gates do not block the evidence baseline or structural skeleton. They block only the corresponding scientific, runtime, release, checklist, or submission claims recorded in the evidence map.

## Build and PDF verification

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Engine | pdfTeX/PDFLaTeX `1.40.25` (TeX Live 2023/Debian) |
| Bibliography command | `bibtex paper`; style resolved as `aaai2027.bst`; database resolved as `../literature/metadata/references.bib` |
| Build result | Success; `latexmk` exit code 0, target up to date after three PDFLaTeX passes and BibTeX |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `11d6e66f41dceb5d11b397eb67ca61fcd85d55842377f13e37735b94d164553f` |
| Page size | `612 × 792 pt` (US letter) |
| Page count | 3 skeleton pages |
| Layout | Official AAAI two-column layout; verified from style, extracted text, and rendered-page inspection |
| Anonymity | Submission mode and rendered `Anonymous submission`; no author identity, affiliation, URL, acknowledgment, or title/author PDF metadata |
| Fonts | TeX Gyre Termes Type 1 fonts, embedded and subset |
| Visual audit | Every page rendered and inspected; no clipping, overflow, layout collision, or unexpected identity content |

### Warnings

- Expected skeleton-only BibTeX diagnostic: no `\citation` commands.
- Expected Natbib warning: empty `thebibliography` environment. This produces the placeholder References heading on page 3 and will disappear once verified citations are drafted.
- No overfull/underfull box, undefined-reference, missing-file, or fatal LaTeX warning was found.
- Runtime warning: the repository test suite was not executable in the current environment because `pytest` is absent.

## Protected-path verification

- Canonical plan SHA-256 remains `e70a485146631a3edf3f5358ec5e047e97db0967cd12a50a0388eed745f31b25`.
- Author-kit hashes remain the frozen values in `paper_evidence_map.md`; no kit file was changed.
- Key results/reproducibility/bibliography hashes remain the frozen values in `paper_evidence_map.md`; no checked evidence, thesis prose, code, data, manifest, literature, or bibliography file was edited.
- Pre-existing user changes (`prompt.txt`, `clinicause_debug_operational_plan.md`, and the untracked canonical plan) were preserved.
- No pre-existing file was staged, committed, pushed, reset, reverted, reorganized, or deleted; temporary LaTeX intermediates created by the build were cleaned while `paper.pdf` was retained.

## Readiness decisions

- P0A is ready: the workspace/revision/kit baseline is recorded and protected.
- P1 is ready: current official rules, kit behavior, genre structure, page budget, and visual/supplement boundary are evidenced.
- P2 is ready: numerical claims, sources, qualifications, conflicts, and gates are locked.
- P3 is ready: the anonymous author-kit skeleton compiles, resolves its bibliography path, and passes page-size/layout/anonymity/visual checks. Empty-bibliography warnings are expected before scientific citation drafting.

READY FOR STAGE P0A — PAPER BASELINE FROZEN

READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED

READY FOR STAGE P2 — CLAIMS AND EVIDENCE LOCKED

READY FOR STAGE P3 — AAAI SKELETON COMPILES

---

## P3 dataset-construction draft build update

Date: 2026-07-19

Stage P3 replaced the Section 3 planning placeholders with the complete five-subsection resource-construction and validation draft, a reader-facing resource summary table, and a sized Figure 1 layout placeholder with a final-quality caption and implementable production specification. Introduction, Related Work, Evaluation, Discussion, Conclusion, the approved title, and the anonymous author block remain structurally unchanged apart from removing the obsolete predictive Table 1 placeholder and renumbering its planning reference.

### P3 build identity

| Field | Result |
|---|---|
| Parent HEAD before P3 | `884ff8e4d112ff732e43a6aea33ab9bddcf8ed5e` on `main` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; BibTeX and cross-references resolved |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `f37022cb5a45e54ba113b1eb3e84b8d6aa0534fa2bb627efe8e707b774952510` |
| Page count and size | 4 pages; `612 x 792 pt` US Letter |
| Section 3 footprint | Approximately 1.88 physical pages, measured from the Section 3 heading at page-1 y=350.95 pt to the Evaluation heading at page-3 y=253.98 pt |
| Section 3 size | 12 substantive paragraphs; approximately 1,214 words including headings, captions, and table text after LaTeX stripping |
| Fonts | Four embedded, subset Type 1 fonts; no Type 3 fonts |
| Anonymity | Submission mode and rendered `Anonymous submission`; no author identity, affiliation, URL, or acknowledgment introduced |

### P3 warnings and visual audit

- No undefined citation, undefined reference, multiply-defined label, missing file, or fatal LaTeX warning remains.
- One 33.21437 pt overfull vertical-box diagnostic occurs during first-page output. Full-resolution inspection shows no clipping, overlap, margin breach, gutter collision, or readability defect; it arises in the partially populated skeleton's first-page composition. It must be rechecked when the empty Abstract and remaining section placeholders are replaced.
- Underfull horizontal-box diagnostics are limited to normal justification in the Section 3 opening and compact Table 1 cells. Table 1 remains readable at its permitted 9-point size.
- Every PDF page was rendered and inspected. Figure 1 and Table 1 remain within the two-column text block; captions appear below both artifacts; Section 3 columns are balanced and readable. Pages 3--4 retain expected whitespace because later manuscript stages remain placeholders.
- Figure 1 is deliberately a layout placeholder rather than a fabricated scientific figure. Its source comment specifies design-time, runtime, validation-gate, central-resource, and downstream-characterization bands.

### P3 protection and runtime boundary

- The operational-plan SHA-256 remains `e70a485146631a3edf3f5358ec5e047e97db0967cd12a50a0388eed745f31b25`; Author Kit style/BST hashes remain the frozen values in the evidence map.
- No thesis, checked-result, reproducibility, literature, bibliography, code, test, nested-repository, data, or Author Kit file was edited.
- `python` is unavailable and `python3 -m pytest` cannot start because the `pytest` module is absent. The manuscript therefore describes inspected current validation contracts but makes no current test-pass claim and does not attribute repaired current code to archived production.

---

## P4 empirical-evaluation build update

Date: 2026-07-19

Stage P4 replaced the Evaluation placeholders with a complete `Empirical Evaluation` section covering prediction tasks and metrics, effect estimators and directional triangulation, and matching/robustness diagnostics. The pre-existing future-results placeholders now occupy a separate Section 5. No numerical Results prose or Abstract text was written, and Section 3 scientific prose was unchanged.

### P4 build identity

| Field | Result |
|---|---|
| Parent HEAD before P4 | `14337a293eee03a24216c299c312ad5c7d61b3a7` on `main` |
| Accepted P3 content commit | `60504040c86721782e6fdf8a29971c8b1e0ab9e4` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; BibTeX and cross-references resolved |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `13b28f0396fcb91baa830f9aaa57c96da1d65e4cb10d1748b249e1150da1f228` |
| Page count and size | 5 pages; `612 × 792 pt` US Letter |
| Section 4 footprint | Approximately 0.86 physical page, from page-3 y=254.54 pt to page-4 y=144.39 pt |
| Section 4 size | 8 substantive paragraphs; approximately 715 prose words (732 including headings) |
| Fonts | Four embedded/subset Type 1 fonts; no Type 3 fonts |
| Anonymity | Submission mode and anonymous author block intact |

### P4 warnings and visual audit

- No undefined citation/reference, multiply defined label, missing file, horizontal overfull box, or fatal warning remains.
- The existing 33.21437 pt first-page overfull vertical-box diagnostic persists. Full-resolution inspection again found no clipping, overlap, gutter/margin breach, or readability defect.
- Underfull horizontal-box diagnostics are confined to ordinary paragraph and compact-table justification.
- All five pages were rendered at 144 dpi and inspected. The Section 3–4 transition, Section 4 headings, cross-column flow, separate Section 5 heading, placeholders, bibliography, margins, and gutter are visually sound. Remaining whitespace reflects intentionally unwritten stages and deferred P5 floats.

### P4 protection and scientific boundaries

- The operational-plan, AAAI style, and bibliography-style hashes remain unchanged.
- No protected thesis, evidence, result, reproducibility, literature, bibliography, code, test, nested-repository, data, or run file was edited.
- Pre-existing `prompt.txt` and tracked LaTeX auxiliaries were preserved; cleanup remains intentionally deferred by user decision.
- CausalPFN is presented as a meaningful complementary estimator without an invented citation or unsupported architecture/theory claim.
- No experiment, model run, test-pass claim, commit, or push occurred.

READY FOR STAGE P5 — EMPIRICAL EVALUATION DRAFTED

---

## P5 results build update

Date: 2026-07-19

Stage P5 replaced every Results placeholder with the complete three-subsection
Results draft, full predictive-results Table 2, and source-generated
cross-estimator Figure 2. Sections 3 and 4 were not revised. A `\FloatBarrier`
immediately before Section 6 keeps both P5 full-width floats attached to Results.

### P5 build identity and content

| Field | Result |
|---|---|
| Parent HEAD before P5 | `b604d68fdf85aa278d80c3f8916c9fd1ef837bcc` (`AAAI p4`) on `main` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Section 5 structure | Opening plus Predictive Characterization; Effect Patterns and Estimator Agreement; Robustness and Cross-Dataset Findings |
| Paragraph/word count | 9 substantive paragraphs; approximately 533 prose words excluding floats, 713 words including headings/table/captions |
| Measured footprint | Approximately 1.7 physical pages: page-4 Results prose plus page-5 top full-width floats before Section 6 |
| Table 2 | 8 rows x 4 metrics = 32 checked values; full width, 9-point text, no resize; complete selected held-out test results |
| Figure 2 | Two-panel vector PDF; 19 combinations x 3 estimators = 57 checked values; decreasing Forest order within dataset |
| Numerical audit | Complete in `reports/P5_results_report.md` |

Figure 2 is regenerated by
`figures/generate_figure2_estimator_agreement.py` directly from
`../results/checked_cate_candidates.csv`. The script filters original sampling
and the three estimator-specific main-text statuses, requires 9 MIMIC and 10
PhysioNet exposures, requires all three estimators per combination, rejects
duplicates/missing rows, and plots full precision. Visual inspection at 200 dpi
and at final embedded size confirmed readable labels, distinct grayscale-safe
markers, visible zero lines, preserved magnitudes, and the visible PhysioNet
shock disagreement. PDF creation/modification dates are suppressed; two
consecutive regenerations produced the same SHA-256.

### P5 final build and visual audit

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; references/citations resolved |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `d5b4c8870224584069ff98e656a897ce8991529c0e564f4f7156b3737d955d41` |
| Figure PDF SHA-256 | `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423` |
| Figure script SHA-256 | `cd365937f326ee32e458e9c27fd1bc7b7b9db7c90251bf3e1ea302bb34c58c31` |
| Page count/size | 6 pages; 612 x 792 pt US Letter |
| Layout/anonymity | Official AAAI two-column submission layout; anonymous block intact |
| Fonts | Embedded/subset Type 1 and CID TrueType; no Type 3 font |

All six pages were rendered at 120 dpi and inspected as a contact sheet; pages
4--5 and Figure 2 were additionally inspected at full resolution. Table 2 and
Figure 2 fit the two-column text block, remain readable, use captions below the
artifacts, and have no clipped labels or gutter/margin overflow. All 19
comparisons and three estimator series are present, and the shock exception is
visible.

No undefined citation/reference, duplicate label, missing file, horizontal
overfull box, or fatal warning remains. The known 33.21437 pt first-page
overfull vertical diagnostic from P3/P4 persists without visible clipping,
overlap, margin/gutter breach, or readability impact. Underfull diagnostics are
ordinary paragraph/table justification and final-page column balancing.

No protected thesis, result, reproducibility, literature, bibliography,
planning, audit, log, code, test, data, run, Author Kit, prompt, operational-plan,
structure-note, or earlier-stage report file was edited. Repository cleanup
remains deferred: tracked auxiliaries were preserved and `.gitignore` was not
changed. No experiment/model run, stage, commit, push, reset, restore, revert,
or clean operation occurred.

READY FOR STAGE P6 — RESULTS DRAFTED AND NUMERICALLY MAPPED

---

## P6 Discussion, limitations, and conclusion build update

Date: 2026-07-19

Stage P6 replaced the Discussion and Conclusion planning boxes with five
substantive Discussion paragraphs under four compact subsections and exactly one
Conclusion paragraph. The draft centers resource reuse, workflow-level
cross-dataset portability, prominent DML/CausalPFN triangulation, the design-time
LLM boundary, future research, and one centralized limitations passage. No
earlier scientific section, float, result table, citation, or bibliography entry
was revised.

### P6 build identity and content

| Field | Result |
|---|---|
| Parent HEAD before P6 | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` (`AAAI P5`) on `main` |
| Canonical plan | Version 1.1 at `clinicause_aaai27_paper_operational_plan_v1.1.md`; SHA-256 `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |
| Discussion structure | Resource Utility and Cross-Dataset Portability; Estimator Triangulation and CausalPFN; LLM-Assisted Design and Future Research; Limitations |
| Paragraph/word count | 5 Discussion paragraphs / 561 prose words; 1 Conclusion paragraph / 79 prose words; 640 combined |
| Measured footprint | Approximately 0.94 physical AAAI page by equivalent two-column occupancy, from page-5 y=536.22 pt through the page-6 Conclusion before References at y=259.55 pt |
| New citations/results | None; accepted P5 mappings only |

### P6 final build and visual audit

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; citations and references resolved |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `3c1d90db329e51cce2c8b4d9b32d1c63ecb5bf7b7e0965ecd479eb894acb6c0c` |
| Page count/size | 7 pages; 612 x 792 pt US Letter |
| Technical-content boundary | Discussion and Conclusion end on page 6; page 7 contains only final reference continuation |
| Layout/anonymity | Official AAAI two-column submission layout; anonymous block intact |
| Fonts | All embedded/subset; Type 1 or CID TrueType; no Type 3 font |

All seven pages were rendered and inspected. Table 2 and Figure 2 remain before
Section 6, with no float crossing into Discussion. Discussion, Limitations,
Conclusion, and References flow cleanly across pages 5--7 with no clipping,
margin breach, gutter collision, or readability defect. The known 33.21437 pt
first-page overfull vertical diagnostic persists without a visible defect;
underfull diagnostics remain ordinary justification/column-fill warnings. No
undefined citation/reference, duplicate label, missing file, horizontal
overfull box, or fatal warning remains.

The manuscript retains a viable path to the seven-page technical-content limit,
although P7 will replace the Abstract/Introduction/Related Work placeholders and
P9 must reassess global compression. P6 made no global compression or formatting
change.

No protected plan, prompt, thesis, result, reproducibility, literature,
bibliography, code, test, data, run, Author Kit, figure, table, or earlier-stage
report was edited. Repository cleanup remains deferred. No experiment, model
run, test-pass claim, staging, commit, or push occurred.

READY FOR STAGE P7 — INTERPRETATION AND CONCLUSION DRAFTED

---

## P7 Introduction and Related Work build update

Date: 2026-07-19

Stage P7 replaced the Introduction and Related Work placeholders with a
resource-led, result-aware five-paragraph Introduction and a four-paragraph,
gap-led literature synthesis. The working title was retained. The Abstract
remains intentionally empty, and Sections 3--7, Table 1, Table 2, and both
figures were not changed.

### P7 build identity and content

| Field | Result |
|---|---|
| Parent HEAD before P7 | `ae8b1ef39222ba41c3dc702be931505940f5d7c8` (`AAAI P6`) on `main` |
| Accepted numerical baseline | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` (`AAAI P5`) |
| Canonical plan | Version 1.1 at `clinicause_aaai27_paper_operational_plan_v1.1.md`; SHA-256 `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |
| Introduction | 5 substantive paragraphs; 564 prose words; approximately 0.78 physical AAAI page |
| Related Work | 4 thematic paragraphs; 376 prose words; approximately 0.52 physical AAAI page |
| New evidence-map entries | C84--C103: framing, gap, resource answer, validation boundary, LLM role, four contributions, four headline-result groups, literature claims, title, and CausalPFN gate |
| CausalPFN literature status | User-added primary PDF verified, but method-level attribution remains gated because the approved bibliography/catalog has no entry or citation key |

### P7 final build and visual audit

| Field | Result |
|---|---|
| Build command | `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` |
| Build result | Success; `latexmk` exit code 0; citations and references resolved |
| Output | `thesis-writing/paper-aaai/paper.pdf` |
| PDF SHA-256 | `88d256db48b9c4242fba4e950eb414a5f06fbe7ff952d52955679d970226821a` |
| Page count/size | 8 pages; 612 x 792 pt US Letter |
| Technical-content boundary | Conclusion ends on page 7 at y=386.06 pt; References begins on page 7 at y=397.71 pt; page 8 is reference continuation |
| Layout/anonymity | Official AAAI two-column submission layout; `Anonymous submission` block intact |
| Fonts | All embedded/subset; Type 1 or CID TrueType; no Type 3 font |

All eight pages were rendered and inspected as a contact sheet; pages 1 and 2
were additionally inspected at full resolution after the final prose pass.
Introduction, Related Work, their transition into Section 3, floats, references,
margins, gutters, and column flow are readable and free of clipping, collisions,
or overflow. No undefined citation/reference, duplicate label, overfull box,
missing-file, or fatal warning remains. Underfull diagnostics are limited to
ordinary paragraph/table justification.

The empty Abstract leaves the exact P9 footprint unresolved. Based on the
current page-7 technical endpoint, P9 should reserve approximately 0.20 physical
AAAI page of scientific compression (about 150 prose-equivalent words or an
equivalent float/text saving) after the Abstract is drafted. This is a safety
margin to be remeasured in P9, not evidence of a present seven-page technical
overflow. No formatting trick or global compression was used in P7.

The user-added `literature/papers/causalPFN.pdf` and pre-existing `prompt.txt`
change were preserved. Compilation regenerated tracked LaTeX auxiliaries under
the deferred-cleanup policy. No bibliography, plan, thesis, checked evidence,
code, test, nested repository, Author Kit file, protected scientific section,
table, or figure was edited; no staging, commit, or push occurred.

READY FOR STAGE P8 — COMPLETE MAIN-PAPER BODY DRAFTED

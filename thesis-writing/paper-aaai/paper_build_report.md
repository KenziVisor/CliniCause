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

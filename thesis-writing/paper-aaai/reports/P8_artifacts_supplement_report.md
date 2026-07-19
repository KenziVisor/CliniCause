# P8 artifacts, supplement, and CausalPFN ingestion report

## Stage and baseline

Stage P8 used the canonical plan `thesis-writing/paper-aaai/clinicause_aaai27_paper_operational_plan_v1.1.md` (SHA-256 `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1`). HEAD before work was `e7edfc3a7d74240c73afa7cf3d1fcfd1678ca4cb` on `main`; accepted P7 was that same commit and accepted numerical P5 was `47f487c84a92f0a0b6a8271b370ff9d7afcace23`. The only initial dirty path was user-owned `prompt.txt`. Nested revisions remained STraTS `c37cf381b971af4a4a29ef09b93884a4afe61060` and causal repository `379ed9b75107b52007957ba5908e507b719c9247`.

## Figures and tables

Figure 1 is a deterministic, data-free, grayscale-safe vector pipeline graphic. It separates design-time LLM proposals from deterministic source artifacts and runtime data lanes; shows separate MIMIC-III and PhysioNet lanes, aggregation, two estimator-ready resources, validation gates, and downstream estimators/diagnostics. It makes no test-pass claim and does not depict the LLM as a runtime estimator. Two regenerations produced SHA-256 `e194745a0e36e1edaba5ba2f8127680ef33e3aecebdd5b13e0c06afb2bda1e44`.

Figure 2 was independently re-run without modification. Its input is `checked_cate_candidates.csv`; predicate is original sampling plus the estimator-specific main-text status. It validates 19 combinations (9 MIMIC and 10 PhysioNet), exactly three estimators per combination, exactly 57 values, no duplicates, full-precision plotting, visible zero lines, and the PhysioNet-shock exception. Two regenerations produced SHA-256 `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423`.

Table 1 resource counts, exposure counts, annotation/estimator families, and terminology agree with the checked cohort/CATE sources and Sections 3--7. Table 2 retains all 8 rows and 32 values from `checked_predictive_metrics.csv`, with three-decimal main-paper display, correct loss/score directions, and dataset-specific leaders. The detailed cell/mark audit is `evidence/P8_figure_table_value_checks.md`.

## Supplement and package preparation

`supplement/technical_appendix.tex` and its PDF are separate and anonymous. The deterministic table generator reads aggregate checked CSVs only, asserts expected row counts/uniqueness, retains full precision before documented display rounding, and creates predictive, 19x3 original-estimator, 57-row downsampling, 19-row matching, and diagnostic-coverage tables. Matching failures remain explicit failures, not zeros; original and downsampled magnitudes are not treated as interchangeable. The supplement documents resource contracts, proxy boundaries, DAG/adjustment metadata, validation layers, provenance boundaries, predictive metrics, diagnostic coverage, and restricted source-data access.

`code-data-appendix/README.md` describes an intended anonymous package, relative entry points, checked aggregate inputs, safe-candidate artifact boundaries, regeneration commands, historical-lineage gaps, no-patient-data policy, and remaining release/anonymity gates. It contains no release announcement or exact-reproduction claim.

## CausalPFN ingestion

The supplied PDF passed `file`, `pdfinfo`, text extraction, `qpdf --check`, SHA-256, and first/last page visual checks. It is arXiv:2506.07918v2, 40 pages, SHA-256 `cd3dcd6017745e31db617503f77fa31f6bac454b3be5b3748c4e51d8f5ab3950`. Official NeurIPS metadata verified the final proceedings title, author reconciliation, venue, and volume 38. The PDF was normalized, cataloged as core, checksummed, and assigned `balazadeh2025causalpfn`; the README corpus counts were recomputed. `CIT-GAP-001` and paper gate `G-EVD-01` are resolved only for the missing primary citation. Source/version, runtime, diagnostic, observational-identification, and release gaps remain open.

The AAAI paper now cites CausalPFN in Related Work and at its first Evaluation method mention. The citation supports bounded prior-data-fitted/in-context method framing; it is not used as evidence for local effects, 18/19 agreement, proxy validity, or identification. Future thesis use is planned in `planning/causalpfn_thesis_integration_plan.md`.

## Build and inspection

Main build: `env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex`. Supplement build: `latexmk -pdf -interaction=nonstopmode -halt-on-error technical_appendix.tex` after running the table generator. Both succeeded. The main PDF has 8 US-Letter pages, technical content through page 7 and references on page 8; the supplement has 6 US-Letter pages. Visual contact-sheet inspection found no clipping, overlap, margin/gutter breach, or Type 3 font. The main Abstract remains empty. P9 should retain the pre-existing compression task before adding the Abstract.

No patient-level data was accessed, no model/experiment was run, no checked source was modified, and no large matrix was manually transcribed without source validation. Current code and archived results remain distinct. No unsupported CausalPFN citation, public-release claim, global scientific compression, staging, commit, push, reset, restore, clean, or repository-cleanup action occurred. The PDF rename used an equivalent filesystem operation because `.git/index` was read-only in the sandbox; the PDF bytes were unchanged.

READY FOR STAGE P9 — PAPER AND SUPPLEMENT ARTIFACTS COMPLETE

---

## P8 narrow repair — Figure 1 dataset separation and readability

| Field | Result |
| --- | --- |
| Repair baseline HEAD | `0c1fd3c7b14d3694d7140efe9f4a72cb143df3ac` (`AAAI P8`) on `main` |
| Exact defects repaired | The prior topology visually shared normalized exports and aggregation; prior Figure 1 text was below the requested final-size threshold. |
| Previous / repaired script SHA-256 | `ce207415a1d9e59b92d40f9180d48b8f2ecb5541ccf9e5cb3446b130251174bb` / `a925afed159fff112f241f63ede53b2644ba165d071e00e0a2c3588aa492fdab` |
| Previous / repaired Figure 1 SHA-256 | `6a7a78cb89e17f901b77549bdf5719eb30cdba3e8dda2c5e3933663b26775948` / `3c1c0c63e04dfdba9d7aada3245948f3de59add7e6eb2bd4db1ded99d814c836` |
| Dataset-lane topology | PASS: MIMIC-III and PhysioNet 2012 independently traverse records, preprocessing/IDs, rule labels, four-model annotations, normalized exports, five-source votes, outcome/covariate plus DAG/provenance packaging, and their own estimator-ready resources. Only the completed resources connect to a shared method-family interface marked as separate execution and results. |
| Minimum font sizes | Primary boxes 10.0 pt; stage/lane headings 10.2 pt; gates and bounded notes 9.3 pt. With the 0.99-text-width embedding, these are approximately 9.5 pt, 9.7 pt, and 8.9 pt. |
| Deterministic regeneration | PASS: two invocations of `MPLCONFIGDIR=/tmp/matplotlib-p8-repair python3 thesis-writing/paper-aaai/figures/generate_figure1_pipeline.py` produced the repaired Figure 1 hash above. |
| Standalone inspection | PASS: rendered at full-page scale and at a high-resolution reading scale; all labels, paths, arrows, and bounds are visible, with no clipping or overlap. |
| Embedded inspection | PASS: rendered paper page 3 confirms the full-width figure and caption are readable at their final placement; no float collision, gutter breach, or clipped label appears. |
| Type 3 check | PASS: `pdffonts` reports embedded CID TrueType fonts for Figure 1 and no Type 3 font; the rebuilt main PDF also has no Type 3 font. |
| Caption changes | Minimal alignment change only: it now states `per-dataset` five-source aggregation and `separate dataset-specific` estimator-ready resources. |
| Main build | PASS: the required `latexmk` command completed with resolved citations/references, anonymous US-Letter AAAI layout, and no horizontal overfull box. |
| Main PDF/page footprint | 9 US-Letter pages (previously 8). Technical content and the start of references occur on page 8; references continue on page 9. |
| P9 compression estimate | At least approximately one technical AAAI page, plus Abstract space, must be recovered to restore a seven-page technical body; remeasure in P9 without using formatting compression. |
| Files changed | `figures/generate_figure1_pipeline.py`, `figures/figure1_pipeline.pdf`, `paper.tex`, `paper.pdf`, `paper_build_report.md`, `evidence/P8_figure_table_value_checks.md`, and this report; LaTeX auxiliaries were regenerated by the permitted main build. |
| Protected-file verification | PASS: Figure 2, Tables 1--2, supplement artifacts, CausalPFN metadata, scientific Sections 1--7, checked results, and `prompt.txt` were not edited by this repair. |
| No-commit/no-push verification | PASS: no staging, commit, push, reset, restore, or clean operation occurred. |

READY FOR STAGE P9 — PAPER AND SUPPLEMENT ARTIFACTS COMPLETE

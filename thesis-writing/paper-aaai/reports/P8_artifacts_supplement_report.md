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

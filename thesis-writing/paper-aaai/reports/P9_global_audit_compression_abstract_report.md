# P9 Whole-Paper Audit, Scientific Compression, and Abstract Report

## Stage, model, and authority

| Field | Value |
|---|---|
| Stage | P9 -- whole-paper audit, scientific compression, human-feedback check, title/keywords, and Abstract |
| Model and reasoning | GPT-5.6 Sol; extra-high reasoning |
| Canonical plan | `thesis-writing/paper-aaai/clinicause_aaai27_paper_operational_plan_v1.1.md` |
| Canonical plan SHA-256 | `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |
| Baseline HEAD | `414b8a46c9533ff410fddc739bcc385318860881` (`AAAI P8 repair`) on `main` |
| Accepted numerical baseline | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` (`AAAI P5`) |
| Nested revisions | STraTS `c37cf381b971af4a4a29ef09b93884a4afe61060`; causal repository `379ed9b75107b52007957ba5908e507b719c9247` |
| Pre-existing worktree change | Modified root `prompt.txt`; preserved and not edited by P9 |

The accepted P8 repair, P8, P7, P6, and P5 commits and their durable reports
were inspected. Required complete inputs were read: `paper.tex`,
`paper_evidence_map.md`, `paper_build_report.md`, `aaai_structure_notes.md`, the
P5--P8 reports, P8 value checks, technical appendix, code/data appendix README,
CausalPFN ingestion/integration records, and the approved bibliography. P3--P8
scientific results were treated as accepted; no experiment or numerical
extraction was reopened.

## Feedback search and approval state

No consolidated author or supervisor feedback artifact was found under
`thesis-writing/`. The filename/content search covered `feedback`, `review`,
`supervisor`, `advisor`, `comments`, and `revision requests`.

The closest review-named files are not human paper feedback:

- `logs/stage_5_2_external_review_summary.md` is a thesis artifact packet that
  explicitly marks review pending and denies academic/supervisor approval.
- `logs/stage_5_5_full_pdf_review.csv` and
  `logs/stage_5_5A_full_resolution_pdf_review.csv` are mechanical thesis PDF
  inspections.

No comment was implemented as human feedback, and no author or supervisor
approval is inferred from absence. Human review remains required before P10.

## Files changed

Primary P9 changes:

1. `thesis-writing/paper-aaai/paper.tex`
2. `thesis-writing/paper-aaai/paper.pdf`
3. `thesis-writing/paper-aaai/paper_build_report.md`
4. `thesis-writing/paper-aaai/paper_evidence_map.md`
5. `thesis-writing/paper-aaai/reports/P9_global_audit_compression_abstract_report.md`

Compilation regenerated the already tracked `paper.aux` and
`paper.fdb_latexmk`. No figure generator, figure PDF, supplement, code/data
appendix, checked result, bibliography, literature PDF, source/test file,
submodule, thesis chapter, plan, prior report, or Author Kit file was edited.

## Claim and evidence audit

Every material manuscript statement was checked against the evidence-map claim
register and the accepted reports. The final contribution hierarchy remains:

1. two reusable, validated causal-analysis datasets;
2. their evidence-tracked construction and validation pipeline;
3. predictive and multi-estimator characterization;
4. the design-time LLM proposal layer.

The resource definition, validation boundary, explicit contribution list,
Table 1, Table 2, Figure 1, Figure 2, CausalPFN result, PhysioNet-shock
exception, matching summary, downsampling summary, centralized limitations, and
resource-focused Conclusion all remain in the main paper.

No unsupported clinical, causal, LLM, runtime, reproducibility, or release claim
remains. In particular:

- `validated` refers to construction integrity, cohort consistency, provenance,
  and analytical reuse, not clinical construct validation or identification;
- proxy states are not chart-adjudicated diagnoses;
- reported effects are mean model-estimated CATE over the analyzed sample;
- estimates are observational, proxy based, and not treatment recommendations;
- directional agreement is not magnitude equality, uncertainty, or causal
  identification;
- the LLM is a design-time proposal aid and never a runtime patient-level
  estimator;
- public availability, current test success, and exact clean-checkout
  reproduction are not claimed.

### Claims removed, narrowed, or merged

- The predictive layer no longer claims that one archived run demonstrates
  construct `reproducibility`; it characterizes prediction/recovery of rule
  targets.
- `Strongest representation`/architecture-selection language was narrowed to
  dataset-specific archived point-metric leadership without significance.
- The Results phrase `systematic mortality-related variation` was removed;
  fitted summaries are reported descriptively under the implemented proxy and
  adjustment design.
- Repeated causal, clinical, lineage, runtime, and release qualifications were
  merged into the centralized Limitations subsection; local captions retain only
  the qualification needed to interpret their artifact.
- Duplicated Introduction/Related Work integration-gap language, repeated
  validation/reuse explanations, supplement-level method detail, diagnostic
  narration, captions, and transitions were shortened or merged.

No central contribution was compressed away.

## Numerical and displayed-artifact audit

Read-only recomputation from checked aggregate CSVs confirmed:

| Item | Final check |
|---|---|
| Resource counts | MIMIC-III 26,845 records/9 admitted exposures; PhysioNet 7,993/10 |
| Table 2 | 8 selected rows and all 32 cells; STraTS leads all four MIMIC-III point metrics and GRU-D all four PhysioNet metrics |
| Figure 2 | 57 values = 19 dataset--exposure combinations x 3 estimators; 9 MIMIC-III and 10 PhysioNet combinations |
| DML directions | 19/19 agreement |
| All three estimators | 18/19 agreement; sole exception PhysioNet shock |
| Original/downsampled | 55/57 direction preservation |
| Matching | 15/19 successful; 14/15 agree with the primary direction |

The checked predictive and CATE files retain SHA-256 values
`506f9367f7af0946a9adb77970ae78a8a0e8578fce64a5c4a5cd3ec519ad601c`
and `2f550cf95e2acb9c1c7febf74735f0b36dfc2bd8592baf8e3d6dab5459252bff`.
Figure 1 and Figure 2 retain accepted hashes
`3c1c0c63e04dfdba9d7aada3245948f3de59add7e6eb2bd4db1ded99d814c836`
and `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423`.

No protected number, denominator, sign, sampling condition, table cell, or
figure value changed.

## Citation and CausalPFN audit

The final manuscript cites 19 unique approved keys. Every key exists in
`literature/metadata/references.bib`; BibTeX resolves all citations, and the
final log contains no undefined citation or reference. No new literature was
added.

`balazadeh2025causalpfn` supports only the external method description of a
prior-data-fitted, in-context estimator trained on simulated data-generating
processes. The local 18/19 agreement and PhysioNet-shock exception remain
supported only by checked CliniCause outputs. CausalPFN remains prominent in the
Abstract, Introduction, Evaluation, Results/Figure 2, Discussion, and
Conclusion, while its smaller archived diagnostic envelope remains explicit.

## Current-code versus archive-language audit

The manuscript keeps three evidence layers distinct:

- checked archives support selected prediction exports, aggregate tables,
  manifests/checksums, and archived analysis-stage records;
- current repaired source/test artifacts support descriptions of stricter
  validation contracts;
- missing producing revisions/configurations and checkpoint-to-export links
  prevent historical-producer, current-test-pass, integrated-rerun, and exact
  reproduction claims.

No current implementation is retroactively attributed to archived production.

## Scientific compression

Counts below use `detex | wc -w` on each LaTeX section block, including headings,
table text, and captions within that block. The pre-P9 Abstract contained no
prose. The final Discussion is intentionally the single expanded section: P9
centralized the resource-reuse interpretation and all limitations there while
compressing their repetitions elsewhere.

| Section | Before | After | Change |
|---|---:|---:|---:|
| Abstract | 0 | 182 | +182 |
| Introduction | 565 | 452 | -113 |
| Related Work | 388 | 353 | -35 |
| Dataset construction | 1,220 | 1,136 | -84 |
| Empirical Evaluation | 731 | 653 | -78 |
| Results | 713 | 611 | -102 |
| Discussion and Limitations | 579 | 787 | +208 |
| Conclusion | 81 | 120 | +39 |

Compression was scientific/editorial. No document-class, margin, style, base
font, line-spacing, column-spacing, heading-spacing, caption-spacing,
bibliography-font, page-dimension, `resizebox`, negative-spacing, manual-break,
or new float-placement workaround was used. Captions were shortened without
changing artifact meaning. Figure 1 was not resized or regenerated.

### Page boundary

| State | Total pages | Technical endpoint | Reference placement |
|---|---:|---|---|
| Before P9 | 9 | Technical content and References both on page 8 | Pages 8--9 |
| After P9 | 8 | Conclusion ends on page 7 | References begins on page 8; page 8 is references only |

The exact seven-page technical-content requirement is satisfied, including the
Abstract. The total PDF remains below the nine-page maximum.

## Final Abstract and evidence mapping

> Reusable causal analysis of heterogeneous, irregular intensive-care records requires explicit constructs, cohort boundaries, adjustment assumptions, and provenance that prediction-ready sequences do not provide. We present CliniCause, two validated causal-analysis datasets built from MIMIC-III and PhysioNet 2012. The resources contain 26,845 and 7,993 analysis records with nine and ten admitted proxy-state exposures, respectively, linked to in-hospital mortality, observed covariates, dataset-specific causal-graph metadata, and provenance. An evidence-tracked pipeline combines deterministic proxy rules with annotations from four irregular-time-series models and enforces schema, cohort, artifact, and provenance contracts; a design-time LLM proposes candidates but does not process patient records or estimate effects. On archived predictive point metrics, STraTS led all four MIMIC-III metrics and GRU-D led all four PhysioNet metrics. Across 19 prespecified dataset--exposure comparisons, the two double-machine-learning estimators agreed in direction for 19/19, while CausalPFN joined them in 18/19; PhysioNet shock was the sole all-estimator exception. These observational, proxy-based results do not establish clinical effects or causal identification. They show that CliniCause supports reusable, inspectable analysis and that estimator triangulation can expose both stable directional patterns and informative disagreements across heterogeneous ICU resources.

Evidence by sentence/function:

1. problem/interface need: C84--C86;
2. resource and two-dataset scope: C02, C03, C08, C87, C94;
3. construction/validation and LLM boundary: C04, C05, C29--C40, C89;
4. predictive characterization: C58--C60, C95;
5. estimator agreement/exception: C63--C65, C96;
6. bounded reuse conclusion: C40, C51--C54, C71--C83.

The Abstract is one paragraph, 182 words, citation free, release neutral, and
was written from the final stabilized body. It contains no recommendation,
significance, availability, or identification claim.

## Title and proposed keywords

Final working-title decision: retain
`CliniCause: Constructing Reusable Causal-Analysis Datasets from Irregular ICU
Records`. The complete paper matches its resource-first scope; no material
mismatch justified stylistic replacement. Human approval is still required.

Proposed OpenReview keywords:

1. causal machine learning
2. irregular clinical time series
3. clinical data resources
4. heterogeneous treatment effects
5. weak supervision
6. foundation models for causal inference

## Build, PDF, fonts, and visual inspection

Build command from `thesis-writing/paper-aaai/`:

```bash
env TEXINPUTS=AuthorKit27: \
    BSTINPUTS=AuthorKit27: \
    BIBINPUTS=../literature/metadata: \
    latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

| Check | Result |
|---|---|
| Build | PASS; `latexmk` exit 0 |
| Main PDF SHA-256 | `ffa4be53aab2bcc3f606cc1a4409441e5f003307311df3eaa1bb78d1515efda2` |
| Page count/size | 8 pages; 612 x 792 pt US Letter |
| Layout/anonymity | Official anonymous AAAI two-column submission layout retained |
| Abstract | Present, readable, one paragraph, 182 words |
| Citations/references | No undefined citation/reference; all 19 keys resolve |
| Labels | No duplicate-label warning |
| PDF integrity | `qpdf --check` PASS |
| Fonts | All embedded/subset Type 1 or CID TrueType; no Type 3 font |
| Overfull/fatal diagnostics | None |
| Remaining log diagnostics | Ordinary underfull paragraph/table justification only |

All eight pages were rendered at 120 dpi and visually inspected. Pages 1--8
were checked for clipping, overlap, margin/gutter intrusion, column flow,
caption attachment, and readable tables/figures. The Abstract is readable;
Figure 1 retains separate dataset lanes and design-time/runtime separation;
Table 1 and Table 2 are legible; Figure 2 retains all series, zero references,
magnitude differences, and the shock exception; page 7 contains technical
content only; page 8 contains references only. No visual defect was found.

## Open gates

- `G-EVD-02`: historical producing commits/configurations and predictive
  split/checkpoint/export lineage remain incomplete.
- `G-RUN-01`: current root/nested test execution remains unevidenced.
- `G-RUN-02`: no complete current-revision integrated rerun manifest exists.
- `G-REL-01`: anonymous package/URL, license, access instructions, and final
  release contents remain undecided.
- `G-HUM-01`: title, contribution hierarchy, claim strength, visuals, and exact
  scientific PDF require author/supervisor approval.
- `G-HUM-02`: author/track/conflict, privacy/ethics/governance, and final
  anonymity decisions remain human owned.
- `G-AAAI-01`: mutable AAAI-27 requirements and generative-AI policy must be
  rechecked in P10.

These gates are explicit and do not invalidate the bounded audited draft. They
block only the corresponding runtime, reproduction, release, governance, or
submission claims.

## Human-review decision list

The exact decisions requiring human approval are:

1. title;
2. contribution hierarchy;
3. validation terminology;
4. CausalPFN framing;
5. causal and clinical language;
6. LLM positioning;
7. limitations;
8. final Abstract;
9. exact seven-page technical PDF;
10. release commitment and ethics/governance language deferred to P10.

No author or supervisor approval is claimed for any item.

## Protection and repository verification

The canonical plan, Author Kit, checked results, figure PDFs/generators,
supplement, code/data appendix, bibliography/literature corpus, source code,
tests, submodules, thesis chapters, prior reports, and user-owned `prompt.txt`
were not modified by P9. Compilation changed only the permitted tracked LaTeX
auxiliaries. Repository cleanup remained deferred.

No file was staged, committed, pushed, reset, restored, reverted, cleaned, or
deleted. HEAD remains the P8 repair baseline. No protected number changed; no
central contribution was compressed away; CausalPFN remains prominent but
bounded; the Abstract was written from the stabilized body; no formatting trick
was used; and the human-approval state is reported without inference.

HUMAN REVIEW REQUIRED BEFORE STAGE P10 — AUDITED COMPRESSED DRAFT AND ABSTRACT READY

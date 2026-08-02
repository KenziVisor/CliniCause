# P7 Introduction and Related Work Report

## Execution identity and repository baseline

| Field | Value |
|---|---|
| Stage | P7 -- Introduction and Related Work |
| Model | Sol-extra high |
| Reasoning effort | Extra high |
| Canonical plan | `thesis-writing/paper-aaai/clinicause_aaai27_paper_operational_plan_v1.1.md` |
| Canonical plan version/hash | Version 1.1; `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |
| Current HEAD before work | `ae8b1ef39222ba41c3dc702be931505940f5d7c8` (`AAAI P6`) |
| Accepted P6 commit | `ae8b1ef39222ba41c3dc702be931505940f5d7c8` |
| Accepted P5 numerical commit | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` (`AAAI P5`) |
| Branch | `main` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` |

The seven recent commits inspected were `ae8b1ef` (`AAAI P6`), `47f487c`
(`AAAI P5`), `b604d68` (`AAAI p4`), `14337a2` (`AAAI P3`), `a851e38`
(`docs: record P3 commit evidence`), `6050404` (`paper: draft dataset
construction and validation`), and `884ff8e` (`AAAI skeleton`). `HEAD` and
`HEAD~1` statistics and both nested-repository revisions were inspected.

At entry, the only dirty item was the user's modified `prompt.txt`; it did not
overlap the permitted P7 manuscript files. During P7 the user added the
untracked `thesis-writing/literature/papers/causalPFN.pdf`. That PDF was read and
verified but not modified. No reset, restore, clean, staging, commit, or push was
performed.

## Complete-body and literature inspection

The following complete-body sources were inspected before drafting:

- the complete Version 1.1 operational plan and current `paper.tex`;
- `paper_evidence_map.md`, `aaai_structure_notes.md`, and
  `paper_build_report.md`;
- `reports/P5_results_report.md` and
  `reports/P6_discussion_conclusion_report.md`; and
- thesis Chapters 1, 2, 11, and 12, including the available conclusions/future
  work source.

The approved literature README, inclusion/role material,
`llm_methodology_candidate_additions.md`, `metadata/catalog.csv`, and
`metadata/references.bib` were inspected. Primary PDFs were checked for the
irregular-time-series review; MIMIC-III, PhysioNet 2012, and the MIMIC-III
benchmark; STraTS, GRU-D, GRU, TCN, and missingness-aware RNN work; electronic
phenotyping, data programming, and Snorkel; double machine learning, causal
forests, and generalized random forests; and the two approved LLM sources used
for medical capability/reliability and causal-graph priors. No broad literature
search was performed.

The user-added CausalPFN PDF was verified as Balazadeh et al., *CausalPFN:
Amortized Causal Effect Estimation via In-Context Learning*, NeurIPS 2025,
arXiv:2506.07918v2; its SHA-256 is
`cd3dcd6017745e31db617503f77fa31f6bac454b3be5b3748c4e51d8f5ab3950`.
The approved `references.bib` (SHA-256
`8ffcee89e8d3ff617d88725ca4625c55d84d53bc6aa5cffdda5525fe26b3fb0e`) and
catalog (SHA-256
`dea6b72196ede8cddb66dc0ba5d9650f57e7efe5338794a4d2f4b5fd157181b8`)
contain no corresponding entry or existing key. Consequently G-EVD-01 is
partially resolved at the source-verification layer but remains open at the
approved-metadata/citation-key layer. No CausalPFN architecture, training,
theory, novelty, or method citation was added.

## Citations and Related Work

The approved citation keys used in Sections 1--2 are:

`sun_2026_review_irregular_medical_timeseries`,
`lipton_kale_wetzel_2016_missingness_rnns`, `johnson2016mimiciii`,
`silva2012physionet`, `harutyunyan_2019_mimiciii_benchmark`,
`tipirneni2022strats`, `che2018grud`, `banda_2018_electronic_phenotyping`,
`ratner_et_al_2016_data_programming`, `chernozhukov2018dml`,
`wager2018causalforest`, `cho2014gru`, `bai2018tcn`,
`ratner_et_al_2020_snorkel`, `athey2019grf`,
`singhal_et_al_2023_llm_clinical_knowledge`, and
`darvariu_et_al_2024_llm_causal_graph_priors`.

Every key exists in the approved bibliography and each primary source was
checked against the rendered statement. Surveys and adjacent thesis citations
were not used to launder method attribution. Candidate additions lacking an
approved role/key, unrelated literature, and method-level CausalPFN positioning
were excluded or gated.

Related Work contains four compact paragraphs and 376 LaTeX-stripped prose
words (headings excluded), occupying approximately 0.52 physical AAAI page:

1. clinical source resources, prediction benchmarks, and irregular temporal
   modeling;
2. proxy states, electronic phenotyping, programmatic labeling, and the fixed
   deterministic aggregation distinction;
3. double machine learning and heterogeneous-effect estimators versus the
   missing reusable analysis-table interfaces; and
4. bounded design-time LLM assistance followed by the integrated resource gap.

The synthesis establishes the same gap the Introduction answers: existing
strands provide necessary components, but leave an integration gap in reusable
resources that connect heterogeneous irregular ICU records, replaceable proxy
constructs, predictive annotations, dataset-specific graph metadata,
estimator-ready tables, validation/provenance, and cross-estimator
characterization across two datasets. It makes no categorical universal-absence
claim.

## Introduction outcome

The Introduction contains the requested five substantive paragraphs and 564
LaTeX-stripped prose words (heading excluded), occupying approximately 0.78
physical AAAI page. Its sequence is problem/opportunity, integrated gap,
CliniCause resource answer, headline empirical findings, and explicit
contributions.

The exact contribution list is:

1. two reusable, validated causal-analysis datasets spanning MIMIC-III and
   PhysioNet 2012;
2. an evidence-tracked construction pipeline integrating design-time
   LLM-assisted proposals, deterministic proxy definitions, temporal
   prediction, DAG metadata, validation, and provenance while preserving source
   semantics;
3. full predictive and multi-estimator characterization, including 19/19 DML
   and 18/19 all-estimator directional agreement; and
4. explicit interfaces for replacing proxy definitions, temporal models, DAGs,
   adjustment sets, estimators, and robustness analyses without rebuilding
   every upstream integration stage.

This hierarchy keeps the resource contribution first, the construction pipeline
second, and empirical analyses as demonstrations. The LLM remains inside the
construction contribution and is not promoted to a primary contribution.

The rendered headline results and accepted P5 mappings are:

| Introduction statement | Accepted numerical source |
|---|---|
| 26,845 MIMIC-III records / 9 admitted exposures; 7,993 PhysioNet records / 10 admitted exposures | P5-C01--P5-C04 |
| STraTS leads all four archived MIMIC-III metrics; GRU-D leads all four corresponding PhysioNet metrics | P5-C05 and P5-C10; full values P5-P01--P5-P32 |
| CausalForestDML and LinearDML agree in direction for 19/19 prespecified comparisons | P5-C19 and P5-C25b |
| All three estimators, including CausalPFN, agree in 18/19 | P5-C20 and P5-C26 |
| Original-versus-outcome-downsampled direction is preserved in 55/57 estimator comparisons | P5-C32 |

No accepted denominator was recomputed or reinterpreted. CausalPFN remains
prominent in the headline empirical result despite the method-citation gate.

The validation boundary is rendered as: “validated denotes construction and
analytical integrity---including aligned schemas, cohorts, artifacts,
provenance, and successful analytical use---not clinical construct validation
or causal identification.” The LLM boundary is rendered as structured
design-time proposal assistance whose project-selected proposals are encoded
into deterministic source artifacts before patient-level execution; project
selection and deterministic source govern runtime behavior.

## Title, evidence map, and protection

The title remains *CliniCause: Constructing Reusable Causal-Analysis Datasets
from Irregular ICU Records*. It matches the completed resource-first story,
preserves “causal-analysis” rather than claiming validated causality, and does
not overemphasize the LLM. No material mismatch justified a change; final title
approval remains a P9 human decision.

The evidence map now records the P7 repository/source baseline, the verified
but uncataloged CausalPFN PDF, updated G-EVD-01 wording, and claim entries
C84--C103 for problem framing, gap, resource answer, validation definition, LLM
role, four contributions, headline results, literature-dependent statements,
title consistency, and the remaining CausalPFN citation gate. Claims are marked
SUPPORTED, SUPPORTED WITH QUALIFICATION, or GATED as appropriate.

P7 changed or created only:

1. `thesis-writing/paper-aaai/paper.tex`;
2. `thesis-writing/paper-aaai/paper.pdf`;
3. `thesis-writing/paper-aaai/paper_build_report.md`;
4. `thesis-writing/paper-aaai/paper_evidence_map.md`; and
5. `thesis-writing/paper-aaai/reports/P7_introduction_related_work_report.md`.

Compilation regenerated the already tracked `paper.aux`, `paper.bbl`,
`paper.blg`, `paper.fdb_latexmk`, and `paper.fls` under the deferred-cleanup
policy. The user-added CausalPFN PDF and modified `prompt.txt` are not P7 edits
and remain preserved. Section-by-section comparison against the accepted P6
commit confirms Sections 3--7 and the bibliography tail are byte-identical.
Tables 1--2, Figures 1--2, their source/generation assets, the empty Abstract,
the anonymous author block, plans, prior reports, thesis, literature,
bibliography, checked evidence, code, tests, submodules, and Author Kit were not
changed.

## Build, page pressure, and readiness

The exact build command, run from `thesis-writing/paper-aaai/`, was:

```bash
env TEXINPUTS=AuthorKit27: BSTINPUTS=AuthorKit27: BIBINPUTS=../literature/metadata: latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

`latexmk` exited 0. The final PDF SHA-256 is
`88d256db48b9c4242fba4e950eb414a5f06fbe7ff952d52955679d970226821a`.
It has 8 pages at 612 x 792 pt (US Letter) in the official anonymous AAAI
two-column format. Technical content ends with the Conclusion on page 7 at
y=386.06 pt; References begins at y=397.71 pt and continues through page 8.

There are no undefined citations, undefined references, duplicate labels,
overfull boxes, missing files, or fatal warnings. All fonts are embedded and
subset Type 1 or CID TrueType; no Type 3 font appears. Underfull box messages are
ordinary paragraph/table justification. The anonymous author block remains
intact, and PDF metadata exposes no title or author identity.

All eight pages were visually inspected as a contact sheet. Pages 1 and 2 were
also inspected at full resolution after the final prose pass. The Introduction,
Related Work, Section 3 transition, floats, references, margins, gutters, and
column flow have no clipping, collision, text crossing, or readability defect.

Because the Abstract is still empty, P9 should reserve approximately 0.20
physical AAAI page of scientific compression, about 150 prose-equivalent words
or an equivalent float/text saving, and remeasure after drafting the Abstract.
The estimate provides safety margin under the seven-page technical limit; the
current manuscript does not overflow that limit. No global compression, smaller
font, margin change, spacing hack, or float manipulation was attempted.

The complete revised P6--P10 workflow was followed; the obsolete workflow was
not combined with it. No Abstract was written. No public-release,
clinical-deployment, statistical-significance, randomized-effect,
clinical-label-validity, equal-estimator-magnitude, or causal-identification
claim was added. Every headline number maps to the accepted P5 audit. No
unsupported novelty or CausalPFN method citation was invented. Repository
cleanup remains deferred, and no staging, commit, or push occurred.

P7 is complete: Related Work establishes the gap answered by the Introduction,
the contribution hierarchy remains resource first, all citations and numerical
claims are evidenced within their stated boundaries, and the complete main-paper
body is ready for the next stage.

READY FOR STAGE P8 — COMPLETE MAIN-PAPER BODY DRAFTED

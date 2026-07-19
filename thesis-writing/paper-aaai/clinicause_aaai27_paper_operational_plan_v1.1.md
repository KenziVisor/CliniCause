# CliniCause — Complete AAAI-27 Paper Writing Operational Plan

**Document status:** Canonical paper-writing plan  
**Version:** 1.1  
**Date:** 2026-07-19  
**Last workflow revision:** 2026-07-19  
**Target venue:** AAAI-27 Main Technical Track  
**Repository:** `KenziVisor/CliniCause`  
**Paper workspace:** `thesis-writing/paper-aaai/`  
**Workflow coordinator and stage reviewer:** ChatGPT  
**Bounded manuscript and artifact implementation:** Codex  
**Submission authors and scientific authorities:** the human author team and supervisor  
**Model-routing principle:** use the least expensive model that preserves the required scientific or technical quality

---

## 1. Purpose

This document defines the complete and stable workflow for producing a full AAAI-27 paper from the CliniCause thesis, repository, checked results, repaired pipeline, and AAAI 2027 Author Kit.

The immediate objective is to produce a complete first manuscript draft in AAAI format, then refine it through evidence verification, scientific compression, reproducibility preparation, anonymity checks, and final PDF validation.

The paper will not be a shortened thesis. It will present one focused research story:

> **CliniCause constructs reusable, validated causal-analysis datasets from heterogeneous irregular ICU records and demonstrates their analytical utility through irregular-time-series prediction, DAG-guided analysis, and cross-estimator agreement.**

The paper will be confident and constructive. It will present the achieved contributions directly and positively. Qualifications will be used where they protect scientific accuracy, not as a substitute for stating the contribution.

The central writing rule is:

> State demonstrated contributions with confidence; qualify only the boundary that is genuinely unresolved; do not weaken a valid result merely because a stronger result was not established.

### 1.1 Workflow revision record

Version 1.1 records the author-approved token-efficiency revision:

- Codex is authorized to perform bounded manuscript drafting under explicit prompts;
- every stage writes a durable repository report;
- every “move to the next part” request triggers an independent full-context review;
- P6–P15 are consolidated into P6–P10 where tasks genuinely share context;
- model selection is based on required context and task type rather than using maximum reasoning for every task.

---

## 2. Frozen strategic decisions

These decisions are approved and should not be silently changed during drafting.

### 2.1 Primary contribution

The primary contribution is the construction of **validated, reusable causal-analysis datasets** derived from MIMIC-III and PhysioNet 2012.

The dataset packages are intended to support reproducible follow-up research without requiring every researcher to reconstruct the entire integration pipeline from raw irregular ICU records.

The paper should use the term:

> **validated causal-analysis datasets**

rather than implying that causal identification itself has been validated.

“Validated” refers to the construction and analytical integrity of the resources, including, subject to final evidence confirmation:

- explicit analysis units and canonical identifiers;
- deterministic source-to-analysis transformations;
- documented exposure, outcome, and covariate schemas;
- deterministic proxy-state construction;
- prediction artifact schemas and metadata;
- cohort-alignment and exact-equality contracts;
- duplicate-conflict detection;
- rejection of malformed or incomplete inputs;
- dataset-specific DAG and adjustment metadata;
- estimator-ready outputs;
- provenance, manifests, receipts, and checksums;
- empirical characterization with predictive and causal-analysis models.

The term does **not** need to be followed by a defensive paragraph every time it appears. Its scope will be defined clearly once in the Introduction or Dataset Validation section and then used normally.

### 2.2 Secondary contribution

The second contribution is an **evidence-tracked dataset-construction pipeline** that turns irregular ICU records into reusable causal-analysis resources while preserving construct lineage and dataset-specific semantics.

This contribution includes:

- source-specific preprocessing;
- LLM-assisted design proposals;
- human/project selection;
- deterministic proxy-state rules;
- irregular-time-series predictive annotations;
- normalized aggregation;
- explicit outcomes and covariates;
- source-coded DAG adjustment structures;
- estimator-ready exports;
- validation and provenance artifacts.

### 2.3 CausalPFN positioning

CausalPFN will be presented as a meaningful positive empirical result, not buried as an incidental exploratory model.

The core result is:

> Despite using a different modeling paradigm, CausalPFN agreed in direction with the two DML estimators in 18 of 19 prespecified dataset–exposure comparisons.

The paper will emphasize this as **cross-estimator triangulation** and evidence that the principal directional patterns were not unique to one estimator family.

CausalPFN may still be described as complementary or exploratory when discussing its smaller diagnostic and provenance envelope. That qualification must not obscure the positive result.

### 2.4 LLM positioning

The LLM-assisted design component remains important but is not the primary paper claim.

The paper will state confidently that the project used a structured design-time LLM protocol to propose:

- proxy-state ontologies;
- decision-rule families;
- missingness considerations;
- dataset-specific DAG structures.

It will also make clear that:

- project-selected proposals were encoded as deterministic source artifacts;
- the LLM was not used as a runtime patient-level estimator;
- the paper evaluates the complete constructed resources and workflow, not the isolated causal value of the LLM.

### 2.5 Writing order and consolidated stage structure

The paper body will be written before the abstract.

Completed foundation and drafting stages:

1. P0 — baseline and source freeze;
2. P0A — AAAI structure and genre study;
3. P1 — scientific story and claim map;
4. P2 — anonymous AAAI manuscript skeleton;
5. P3 — dataset construction and validation;
6. P4 — empirical evaluation.

Current stage:

7. P5 — Results, predictive table, estimator-agreement figure, and complete numerical audit.

The remaining work is consolidated into five stages that share context and therefore should be executed together:

8. P6 — Discussion, limitations, and conclusion;
9. P7 — Introduction and Related Work;
10. P8 — final figures, tables, supplement, and code/data appendix content;
11. P9 — whole-paper evidence audit, scientific compression, author/supervisor feedback integration, and abstract;
12. P10 — AAAI compliance, anonymity, reproducibility checklist, final package, and submission handoff.

This consolidation replaces the older P6–P15 sequence. It reduces repeated context loading without merging tasks whose evidentiary order must remain separate. In particular, Results must be frozen before Discussion, and the scientific paper must be approved before final submission packaging.

### 2.6 Tone

The article must be optimistic, forward-looking, and confident.

It should communicate that CliniCause provides a useful research resource and a productive foundation for future causal AI research.

It must avoid two opposite errors:

- **overclaiming:** presenting adjusted observational estimates as proven intervention effects or proxy states as validated diagnoses;
- **underclaiming:** describing a substantial integrated dataset and consistent empirical findings as merely tentative engineering artifacts.

---

## 3. AAAI-27 deadlines and submission assumptions

The official AAAI-27 timetable states:

- **Abstract deadline:** July 21, 2026, 23:59 UTC-12;
- **Full paper deadline:** July 28, 2026, 23:59 UTC-12;
- **Supplementary material and code deadline:** July 31, 2026, 23:59 UTC-12.

All deadlines are Anywhere on Earth.

The AAAI-27 Author Kit is present under:

```text
thesis-writing/paper-aaai/
```

and includes:

```text
AnonymousSubmission2027.tex
AnonymousSubmission2027.pdf
CameraReady2027.tex
CameraReady2027.pdf
ReproducibilityChecklist.tex
ReproducibilityChecklist.pdf
aaai2027.sty
aaai2027.bst
aaai2027.bib
```

The current working page architecture assumes the established AAAI Main Technical Track limit of:

- **7 pages of technical content**;
- additional pages for references;
- supplementary technical appendix and code/data package submitted separately or as instructed.

The AAAI-27 event page currently supplies the 2027 kit and deadlines but may later publish additional track-specific details. Therefore Stage P0 includes one final verification of:

- exact AAAI-27 Main Track page limit;
- whether the checklist is included in the main PDF or submitted separately;
- precise supplementary-material instructions;
- title/author modification policy;
- available tracks and keywords.

If the official page limit differs, the page budget changes, but the scientific hierarchy and section order remain the same.

### 3.1 Generative-AI authoring-policy gate

Before manuscript text is submitted, verify the exact AAAI-27 policy governing generative-AI assistance in scholarly writing. The most recent Main Track policy available during planning permits judicious assistance but also contains restrictive language distinguishing editing/polishing from submitting machine-generated prose. Because the AAAI-27 wording may be clarified or updated, it is a mandatory compliance gate rather than an assumption.

Operational rule:

- ChatGPT may produce the complete working manuscript draft requested by the author;
- the human authors remain solely responsible for every statement, citation, interpretation, and submitted word;
- the author must read, verify, revise, and adopt the manuscript as their own scholarly work;
- no AI system may be listed as an author or cited as a scholarly authority;
- no fabricated reference, quote, result, or unsupported claim may enter the draft;
- if AAAI-27 retains a rule limiting LLM use to editing or polishing author-written prose, the author must perform the substantive human rewrite needed for compliance before submission;
- the final submission record should follow any disclosure requirement published by AAAI-27.

This gate does not change today’s objective of producing a full draft. It controls what human review and revision are required before that draft becomes a submission artifact.

---

## 4. Mandatory study of the AAAI paper structure and genre

Before drafting prose, the AAAI format must be learned as a scientific communication structure, not only as a LaTeX template.

### 4.1 Author Kit study

The writer must inspect in full:

- `AnonymousSubmission2027.tex`;
- `aaai2027.sty` where necessary to understand behavior;
- `ReproducibilityChecklist.tex`;
- the rendered sample manuscript for page rhythm and visual density;
- current official AAAI-27 instructions;
- recent Main Track submission and supplementary policies where AAAI-27 details are not yet separately published.

### 4.2 Formatting facts to internalize

The paper must use:

```latex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai2027}
% Fonts are loaded automatically by aaai2027.sty.
% Do not load times, helvet, courier, or another text-font package.
\usepackage[hyphens]{url}
\usepackage{graphicx}
\urlstyle{rm}
\def\UrlFont{\rm}
\usepackage{natbib}
\usepackage{caption}
\frenchspacing
```

However, the precise preamble must be copied from the 2027 sample and not reconstructed from memory. The Author Kit’s current comments about automatically managed fonts must be followed exactly.

Mandatory structural requirements include:

- US Letter paper;
- two-column AAAI layout;
- submission mode and anonymous author block;
- no `hyperref`, `navigator`, or packages that embed links/bookmarks;
- no `geometry` or margin-changing packages;
- no page numbers, headers, or footers;
- no modification of `aaai2027.sty`;
- no font, line-spacing, margin, float-spacing, or section-spacing tricks;
- no manual page breaks in the final manuscript;
- all fonts embedded, including figure fonts;
- no Type 3 fonts;
- no margin or gutter overflow;
- one principal `.tex` source containing the paper text and macros;
- bibliography through `aaai2027.bst` and `natbib`;
- figure captions below figures;
- table captions below tables, following the 2027 kit even if this differs from common conventions;
- tables normally in 10-point text, reducible only to 9 point where necessary;
- figures and tables designed for one or two columns rather than resized blindly;
- title in Chicago-style Title Case;
- PDF metadata cleaned for anonymous review;
- no acknowledgments in the anonymous submission;
- anonymization of self-references and links.

### 4.3 AAAI genre study

The writer will extract the communication pattern expected from a strong AAAI paper:

- the research problem is stated immediately;
- novelty is explicit by the end of the Introduction;
- contributions are few, concrete, and independently evaluable;
- the method is described conceptually before implementation detail;
- experiments map directly to claims;
- results sections answer research questions rather than list logs;
- the discussion interprets findings positively while identifying exact limits;
- the main paper is self-contained;
- the supplement adds depth but is not required to understand or accept the contribution;
- figures and tables perform substantial explanatory work;
- every paragraph earns scarce two-column space.

### 4.4 Reference-paper structure sampling

Before finalizing the section design, inspect a small, purposeful sample of recent AAAI papers with one or more of these traits:

- novel dataset/resource contribution;
- healthcare or clinical AI application;
- causal inference or heterogeneous treatment-effect estimation;
- integrative framework contribution;
- code/data release and reproducibility emphasis.

The goal is not to copy language. The goal is to learn:

- common Introduction length;
- contribution-list style;
- balance between resource description and empirical evaluation;
- number and placement of figures/tables;
- how dataset papers define validation;
- how limitations are concentrated rather than repeated;
- how supplementary material is referenced;
- how a seven-page narrative remains complete.

A brief internal genre note should record:

```text
paper
primary claim
section order
page allocation
figures/tables
contribution wording
resource-validation wording
what remains in supplement
```

This note is a working aid and need not become a permanent repository file unless it has clear future value.

### 4.5 Exit criterion

Stage P0A is complete when the writer can state:

- the final section order;
- the expected function of each section;
- the permitted LaTeX structure;
- the page budget;
- the main-paper versus supplement boundary;
- the visual plan;
- the checklist obligations.

Readiness wording:

```text
READY FOR PAPER ARCHITECTURE — AAAI GENRE AND FORMAT STUDIED
```

---

## 5. Evidence hierarchy and source policy

The paper will be based on an explicit evidence hierarchy.

### 5.1 Evidence priority

1. checked numerical result tables and manifests;
2. current repository source and runtime records;
3. thesis evidence maps and reproducibility ledgers;
4. archived logs tied to known runs;
5. approved literature PDFs and metadata;
6. thesis prose, used as a draft source rather than independent proof;
7. supervisor decisions;
8. author decisions and historical knowledge;
9. clearly labeled inference.

### 5.2 Thesis use

The thesis is the main conceptual and textual source, but it will not be copied mechanically.

For every paper section:

1. identify the relevant thesis chapters;
2. identify the checked evidence behind those chapters;
3. extract only material needed for the paper’s central story;
4. rewrite it for the AAAI audience and page budget;
5. update it against the current repository state;
6. remove thesis-specific chapter navigation, audit narration, and administrative detail.

### 5.3 Protected numerical claims

The following categories are frozen unless a higher-authority evidence source changes them:

- cohort sizes;
- proxy-state counts;
- predictive metrics;
- effect estimates;
- estimator direction-agreement counts;
- matching availability and warning counts;
- downsampling agreement counts;
- dataset/model names;
- estimator hierarchy;
- primary versus robustness population definitions.

Any numerical change requires:

```text
old value
new value
source of old value
source of new value
reason for change
affected claims, tables, and figures
```

### 5.4 Current key results

The initial evidence map includes:

- MIMIC-III causal-analysis population: **26,845**;
- PhysioNet causal-analysis population: **7,993**;
- MIMIC-III proxy-state exposures: **9** in the admitted causal analysis;
- PhysioNet proxy-state exposures: **10**;
- predictive models: **STraTS, GRU, GRU-D, TCN**;
- MIMIC-III predictive leader across the four archived test metrics: **STraTS**;
- PhysioNet predictive leader across those metrics: **GRU-D**;
- CausalForestDML–LinearDML directional agreement: **19/19**;
- all-three-estimator directional agreement including CausalPFN: **18/19**;
- central estimator-disagreement case: **PhysioNet shock**;
- outcome-downsampled directional preservation: **55/57** matched comparisons, subject to final source verification before inclusion.

### 5.5 Evidence gates

Unverified details are marked in the draft with standardized comments:

```latex
% TODO-EVIDENCE: exact missing fact and expected source
% TODO-RUNTIME: statement depends on final runtime validation
% TODO-RELEASE: statement depends on anonymized release package
% TODO-AAAI: statement depends on final AAAI-27 instruction
% TODO-HUMAN: author/supervisor decision required
```

No vague `TODO` is allowed. Each marker must state exactly what is missing.

---

## 6. Claim and tone policy

### 6.1 Claims to make confidently

The paper can and should state directly that:

- CliniCause constructs two reusable causal-analysis datasets from heterogeneous ICU sources;
- the resources preserve explicit exposures, outcomes, covariates, adjustment metadata, and provenance;
- the pipeline integrates deterministic proxy construction, predictive annotation, and estimator-ready causal analysis;
- the construction is dataset specific while exposing a common analytical interface;
- the resources were empirically exercised with four prediction models and three causal estimators;
- the best archived predictive model differed by dataset;
- the two DML estimators agreed in direction for all 19 comparisons;
- CausalPFN joined that directional agreement in 18 of 19 comparisons;
- this agreement supplies useful estimator triangulation;
- the resource supports reproducible follow-up evaluation of representations, proxy definitions, graph choices, and estimators;
- preserving construct and cohort lineage is a substantive scientific contribution, not merely software hygiene.

### 6.2 Claims requiring precise qualification

Use specific bounded language for:

- clinical meaning of proxy states;
- causal interpretation of adjusted estimates;
- identifiability;
- graph validity;
- unmeasured confounding;
- statistical superiority among prediction models;
- effect magnitude comparison across estimators;
- external generalization;
- public release status;
- historical producing-code provenance;
- complete rerun reproducibility.

### 6.3 Avoid repeated disclaimers

The manuscript will not repeat the full limitation set after every result.

Instead:

- define the scope of “validated causal-analysis dataset” once;
- define the estimand and interpretation once in Methods;
- add short result-specific qualifications only when needed;
- provide a focused Limitations subsection;
- use captions for local interpretation boundaries;
- avoid apologetic phrases such as “only,” “merely,” and “just” when describing genuine contributions.

### 6.4 Preferred confident language

Use:

- `constructs`;
- `provides`;
- `validates` with an explicit object;
- `demonstrates`;
- `enables`;
- `supports`;
- `preserves`;
- `exposes`;
- `characterizes`;
- `agrees in direction`;
- `shows promise`;
- `offers a reusable foundation`.

Avoid unsupported uses of:

- `proves`;
- `causes`;
- `clinically validated`;
- `state of the art`;
- `significantly outperforms`;
- `ground truth`;
- `unbiased`;
- `fully reproducible`;
- `generalizable` without evidence.

### 6.5 Core positioning sentence

The provisional central sentence is:

> CliniCause converts heterogeneous irregular ICU records into two validated causal-analysis datasets that preserve construct, cohort, and provenance information from proxy-state design through predictive annotation and DAG-guided estimator-ready analysis.

---

## 7. Paper title strategy

Working title candidates:

1. **CliniCause: Constructing Reusable Causal-Analysis Datasets from Irregular ICU Records**
2. **CliniCause: Validated Causal-Analysis Datasets from Irregular ICU Time Series**
3. **CliniCause: Evidence-Tracked Causal-Analysis Resources for Irregular ICU Data**

Default working title:

> **CliniCause: Constructing Reusable Causal-Analysis Datasets from Irregular ICU Records**

Reasons:

- states the primary contribution;
- sounds constructive and confident;
- avoids implying that causal identification itself was validated;
- leaves room for prediction, DAGs, LLM assistance, and estimator evaluation in the paper;
- fits an integrative AAAI contribution.

The title will be revisited only after the full manuscript and abstract exist.

---

## 8. Target paper architecture

The main manuscript will be a self-contained AAAI paper of approximately seven technical-content pages.

### 8.1 Section order

```text
Title
Abstract
1 Introduction
2 Related Work
3 Constructing the CliniCause Datasets
  3.1 Source Cohorts and Analysis Units
  3.2 Proxy-State Design and Deterministic Construction
  3.3 Predictive Annotations from Irregular Time Series
  3.4 Causal-Analysis Schema and DAG Metadata
  3.5 Dataset Validation and Provenance
4 Empirical Evaluation
  4.1 Prediction Tasks and Metrics
  4.2 Effect Estimators and Cross-Estimator Evaluation
  4.3 Matching and Robustness Diagnostics
5 Results
  5.1 Resource Summary and Predictive Characterization
  5.2 Effect Patterns and Estimator Agreement
  5.3 Robustness and Cross-Dataset Findings
6 Discussion
  6.1 Research Utility and Reuse
  6.2 CausalPFN and Estimator Triangulation
  6.3 Limitations and Appropriate Interpretation
7 Conclusion
References
```

The exact number of subsections may be reduced during compression, but the scientific functions must remain.

### 8.2 Page budget

Working budget:

| Component | Target pages |
|---|---:|
| Title + abstract | 0.35–0.45 |
| Introduction | 0.75–0.90 |
| Related Work | 0.45–0.60 |
| Dataset Construction | 1.80–2.10 |
| Empirical Evaluation | 0.85–1.05 |
| Results | 1.45–1.75 |
| Discussion | 0.65–0.85 |
| Conclusion | 0.15–0.25 |
| Total technical content | approximately 7.0 |

This budget is a design constraint, not a reason to squeeze typography.

### 8.3 Paragraph budget

A likely first-pass paragraph plan:

- Introduction: 5–6 paragraphs;
- Related Work: 3 compact paragraphs;
- Dataset Construction: 9–12 paragraphs plus Figure 1 and Table 1;
- Evaluation: 5–7 paragraphs;
- Results: 7–9 paragraphs plus Table 2 and Figure 2 or Table 3;
- Discussion: 5–6 paragraphs;
- Conclusion: 1 paragraph.

### 8.4 Main-paper self-containment

The main manuscript must contain enough information to understand:

- what each dataset resource represents;
- what one row represents;
- how exposures are produced;
- what outcomes and covariates are present;
- how predictions enter the resource;
- what the DAG metadata means;
- what “validated” means;
- what each reported estimator quantity represents;
- what the headline empirical findings are;
- how the resource can be reused;
- where causal and clinical interpretation stops.

A reviewer must not need to inspect Python code or the thesis to understand the contribution.

---

## 9. Detailed section plan

## 9.1 Introduction

### Purpose

Establish the need for reusable causal-analysis datasets from irregular clinical records and position CliniCause as the solution.

### Logical sequence

1. Public ICU datasets are rich but not immediately usable as transparent causal-analysis resources for complex proxy-state questions.
2. Building such resources requires decisions about irregular observations, missingness, analytical constructs, cohort identity, predictive annotations, causal adjustment, and provenance.
3. Silent changes across these interfaces undermine reuse and interpretation.
4. CliniCause constructs two validated causal-analysis datasets with explicit and traceable interfaces.
5. Summarize the empirical evaluation and strongest results.
6. State contributions.

### Contribution list

The Introduction should present three or four contributions, with the first dominant:

1. **Resources:** two reusable validated causal-analysis datasets for MIMIC-III and PhysioNet 2012.
2. **Construction and validation:** an evidence-tracked pipeline preserving construct, cohort, schema, and provenance integrity.
3. **Empirical characterization:** four irregular-time-series prediction models and three effect estimators, with broad cross-estimator directional agreement.
4. **Traceable design:** an LLM-assisted proposal layer separated from deterministic implementation authority.

### Required results in Introduction

- 26,845 and 7,993 analysis records;
- STraTS leads archived MIMIC metrics, GRU-D leads PhysioNet;
- 19/19 DML directional agreement;
- 18/19 all-three agreement including CausalPFN.

### Tone

The Introduction should end with the opportunity created by the resource, not with a list of deficiencies.

---

## 9.2 Related Work

### Purpose

Locate the contribution at the intersection of resource construction, irregular clinical modeling, programmatic phenotyping, and causal ML.

### Three clusters

1. **Clinical datasets, phenotyping, and weak supervision**
   - MIMIC-III and PhysioNet;
   - rule-based electronic phenotyping;
   - programmatic labeling and weak supervision;
   - LLM-assisted medical knowledge elicitation.

2. **Irregular medical time-series prediction**
   - STraTS;
   - GRU-D;
   - GRU and TCN as included baselines;
   - missingness and sampling-process representation.

3. **Causal ML and heterogeneous-effect estimation**
   - DAG-guided adjustment;
   - DML and CausalForestDML;
   - LinearDML;
   - CausalPFN and foundation-model-based causal estimation;
   - matching, overlap, sensitivity, and robustness.

### Gap statement

The novelty is not that these components individually exist. It is that CliniCause packages their interfaces into reusable, validated causal-analysis resources and empirically characterizes them across datasets and estimator families.

### Citation policy

- use only approved and verified bibliography entries;
- prefer primary method papers;
- include dataset citations;
- add a primary CausalPFN citation if absent from the current approved corpus;
- avoid citation dumping;
- every citation should explain a component, contrast, or gap.

---

## 9.3 Constructing the CliniCause Datasets

This is the core methods section and should receive the largest page allocation.

### 9.3.1 Source cohorts and analysis units

For each dataset, define:

- source dataset;
- source access conditions;
- unit of analysis;
- outcome definition;
- temporal window, if confirmed;
- source-specific covariates;
- final primary causal-analysis population;
- why results are kept separate rather than pooled.

State confidently that the common framework preserves source-specific semantics.

### 9.3.2 Proxy-state design and deterministic construction

Explain:

- design-time LLM-assisted proposal process;
- proposal categories;
- human/project selection;
- deterministic source-coded rules;
- dataset-specific ontologies;
- handling of missing or unavailable measurements;
- canonical proxy-state columns;
- distinction between proxy states and chart-adjudicated diagnoses.

Do not over-expand prompt history. The main paper needs the role and authority boundary; full prompt artifacts can appear in the supplement.

### 9.3.3 Predictive annotations

Explain:

- multi-label prediction task;
- four models;
- irregular-time-series inputs;
- train/validation/test concept;
- prediction probabilities and thresholded fields;
- normalized export;
- aggregation of one deterministic rule-derived source and four model-derived sources in the archived causal runs;
- how aggregated proxy-state fields become analytical exposures.

The wording should treat the predictive layer as an annotation and construct-transport mechanism, not as clinical diagnosis.

### 9.3.4 Causal-analysis schema and DAG metadata

Define the resource contents:

- record identifier;
- proxy-state exposure fields;
- in-hospital mortality outcome;
- observed covariates;
- dataset-specific DAG or graph provenance;
- exposure-specific adjustment-set metadata;
- estimator-ready representation;
- sampling condition;
- run and provenance identifiers.

Explain that source-coded DAGs operationalize the project’s adjustment assumptions and make them inspectable.

### 9.3.5 Dataset validation and provenance

This subsection justifies the main contribution and the word “validated.”

It should distinguish validation dimensions:

#### Structural validation

- expected files and schemas;
- column names and types;
- canonical identifiers;
- allowed values;
- complete output sets.

#### Cohort validation

- identifier preservation;
- exact cohort equality at required handoffs;
- no silent intersections;
- no silent inner-join shrinkage;
- explicit failure for mismatches.

#### Artifact validation

- fingerprints and hashes;
- checkpoint and prediction metadata;
- voter sidecars;
- manifests and receipts;
- run-scoped outputs;
- stale-artifact and reuse protection.

#### Determinism and execution validation

- seed policy;
- deterministic split behavior where supported;
- dataset isolation;
- GPU coordination where relevant;
- independent component and integrated execution evidence.

#### Empirical validation

- predictive characterization;
- estimator triangulation;
- matching and robustness diagnostics;
- cross-dataset execution of the shared workflow.

The subsection will conclude with a single precise scope sentence:

> Validation establishes the integrity and analytical reuse of the constructed resources; clinical construct validity and causal identification remain separate scientific questions.

After that sentence, the manuscript should use “validated causal-analysis datasets” without repeatedly re-explaining the full qualification.

---

## 9.4 Empirical Evaluation

### 9.4.1 Predictive evaluation

Specify:

- evaluated models;
- target labels;
- datasets;
- test metrics: loss, AUROC, AUPRC, minRP;
- macro-averaging and handling of degenerate labels, if verified;
- run count;
- seed policy;
- model-selection and hyperparameter source;
- absence or presence of confidence intervals and statistical tests.

The evaluation question is:

> Do the constructed proxy-state targets support meaningful prediction from irregular ICU time series, and how does model behavior vary across datasets?

### 9.4.2 Effect-estimator evaluation

Specify:

- original cohorts as primary;
- outcome-downsampled cohorts as robustness;
- CausalForestDML;
- LinearDML;
- CausalPFN;
- reported mean model-estimated CATE summaries;
- exposure prevalence;
- estimator-direction comparison;
- no post-hoc exposure selection.

The evaluation question is:

> Are the principal dataset–exposure sign patterns stable across distinct estimator families?

This formulation permits a strong CausalPFN result without implying equal estimands or magnitudes.

### 9.4.3 Matching and robustness

Summarize:

- descriptive matched-pair comparisons;
- matching availability and failure conditions;
- support warnings;
- sensitivity diagnostics for DML estimators;
- treatment and outcome permutations;
- outcome-downsampling comparison;
- the role of these analyses as robustness evidence rather than separate primary claims.

### 9.4.4 Reproducibility details

The main paper should include a compact experimental settings statement. Full settings belong in the supplement.

Required main-text facts, when available:

- producing commit or validated current commit;
- environment summary;
- main hardware;
- random-seed policy;
- number of runs;
- software frameworks;
- data-access restrictions;
- release plan.

---

## 9.5 Results

### 9.5.1 Resource summary

Lead with the resources rather than immediately with model metrics.

Report:

- two datasets;
- cohort sizes;
- exposure counts;
- outcome;
- predictive annotation sources;
- estimators;
- validation components;
- separation of dataset-specific semantics.

### 9.5.2 Predictive characterization

Report the full eight model–dataset combinations in a compact table or a selected metric table with the full version in the supplement.

Confident headline:

> STraTS led all four archived MIMIC-III test metrics, whereas GRU-D led the corresponding PhysioNet metrics, demonstrating that the strongest representation was dataset dependent.

Do not claim statistical superiority without uncertainty evidence.

### 9.5.3 Primary effect patterns

Summarize:

- nine positive CausalForestDML means for MIMIC-III;
- nine positive and one negative mean for PhysioNet;
- key largest values if space permits;
- separate dataset interpretation;
- no numerical pooling.

### 9.5.4 Cross-estimator agreement and CausalPFN

This is a headline subsection.

Required text:

- CausalForestDML and LinearDML agree in direction for 19/19 comparisons;
- CausalPFN joins the prevailing direction for 18/19 comparisons;
- this is strong cross-model triangulation across distinct estimation paradigms;
- the PhysioNet shock comparison is the informative exception;
- magnitude differences remain visible and should not be collapsed into a vote.

Preferred positive framing:

> CausalPFN reproduced the dominant directional pattern in nearly every prespecified comparison, supporting its promise as a complementary estimator for these constructed resources.

Then state the bounded diagnostic difference in one sentence.

### 9.5.5 Robustness

Subject to page space and final verification, report:

- matching direction agreement;
- matching failures as support information;
- outcome-downsampled direction preservation;
- sensitivity/permutation coverage;
- no need to enumerate every diagnostic in the main paper.

### 9.5.6 Result interpretation order

Every Results paragraph should follow:

```text
finding → quantitative evidence → scientific meaning → local boundary if needed
```

Do not begin result paragraphs with a limitation.

---

## 9.6 Discussion

### 9.6.1 Resource contribution and reuse

Discuss how researchers can use the resources to:

- compare alternative causal estimators;
- test new irregular-time-series representations;
- replace or refine proxy definitions;
- evaluate alternative DAGs and adjustment sets;
- study cohort and support sensitivity;
- audit construct lineage;
- reproduce selected analyses without rebuilding all integration stages.

The discussion should present this as a practical research opportunity.

### 9.6.2 Cross-dataset insight

State that:

- the same overall construction pattern operated across two heterogeneous datasets;
- model leadership differed by dataset;
- similarly named proxy states need not be semantically identical;
- portability is demonstrated at the workflow/interface level;
- preserving dataset-specific definitions is a design strength.

### 9.6.3 CausalPFN and estimator triangulation

Discuss:

- why agreement across DML and CausalPFN is meaningful;
- why it supports further evaluation of foundation-model-based causal estimators;
- what the single disagreement teaches;
- why complementary estimators can reveal model sensitivity;
- future work needed for richer diagnostics and uncertainty.

### 9.6.4 LLM-assisted design

Present the LLM layer as:

- a structured design aid;
- a way to convert clinical and causal reasoning into inspectable proposals;
- separated from deterministic execution authority;
- a foundation for future clinician and multi-LLM evaluation.

### 9.6.5 Limitations

Use one concentrated subsection, prioritized by impact:

1. proxy-state clinical construct validity;
2. graph and intervention assumptions;
3. unmeasured confounding and unresolved identification;
4. incomplete uncertainty or repeated-run evidence for some comparisons;
5. incomplete historical provenance where still applicable;
6. dataset-access restrictions and external validation;
7. absence of isolated LLM ablation.

Each limitation should be paired, where appropriate, with the resource feature or future experiment that addresses it.

Example:

> Although the current proxy states are not chart-adjudicated phenotypes, their deterministic definitions and preserved lineage make them directly replaceable and testable in future clinical validation studies.

This maintains an optimistic tone without hiding the limitation.

---

## 9.7 Conclusion

One compact paragraph should state:

- what CliniCause provides;
- the two datasets;
- the validation and reuse value;
- the cross-estimator finding including CausalPFN;
- the research agenda enabled by the release.

Provisional closing sentence:

> By releasing transparent, estimator-ready resources rather than only final effect tables, CliniCause provides a reusable foundation for testing new proxy definitions, temporal representations, graph assumptions, and causal estimators in irregular clinical data.

The exact release verb must match the final release status.

---

## 10. Visual and table plan

The main paper should use a small number of high-value visuals.

## 10.1 Figure 1 — CliniCause resource-construction pipeline

### Purpose

Show that the primary output is the validated dataset resource.

### Required elements

```text
Raw irregular ICU records
        ↓
Dataset-specific preprocessing and canonical IDs
        ↓
Deterministic proxy-state labels
        ↑
Selected LLM-assisted design proposals
        ↓
Four predictive annotation models
        ↓
Normalized and validated exposure construction
        ↓
Outcome + observed covariates + DAG/adjustment metadata
        ↓
Reusable causal-analysis dataset
        ↓
CausalForestDML | LinearDML | CausalPFN | matching | diagnostics
```

### Design requirements

- resource output visually central;
- design-time and runtime paths distinguished;
- human/project selection visible;
- no implication that the LLM processes patient records at runtime;
- validation gates indicated compactly;
- readable in grayscale;
- font size at least 9 point in final placement;
- vector PDF preferred;
- all fonts embedded;
- likely two-column width near the top of page 2 or 3.

## 10.2 Table 1 — Resource summary

Candidate columns:

| Dataset | Records | Proxy exposures | Outcome | Predictive sources | Estimators | Validation/provenance |

Keep entries compact. Use footnotes or abbreviated validation categories if necessary.

## 10.3 Table 2 — Predictive results

Possible options:

### Option A: full metrics

Eight rows and four metrics.

### Option B: compact main table

AUROC and AUPRC in main paper; loss and minRP in supplement.

Decision rule:

- use full metrics if the table fits legibly in two columns;
- otherwise preserve the most interpretable metrics in the main paper and cite the complete supplement table.

## 10.4 Figure 2 — Cross-estimator agreement

Preferred design:

- one row per dataset–exposure comparison;
- three markers for CausalForestDML, LinearDML, CausalPFN;
- split panels or grouping for MIMIC-III and PhysioNet;
- zero reference line;
- the PhysioNet shock disagreement clearly visible;
- magnitude differences preserved;
- perhaps placed across two columns.

If 19 rows are unreadable in the main paper:

- main paper: agreement summary matrix or compact sign heatmap;
- supplement: full dot plot and numeric table.

## 10.5 Table 3 — Validation contract or estimator agreement

Only include if it adds more value than Figure 2.

Possible validation rows:

- schema validation;
- canonical IDs;
- exact cohort equality;
- conflict rejection;
- artifact metadata;
- run-scoped provenance;
- deterministic exports;
- integrated execution.

Alternative compact estimator table:

| Comparison | Direction agreement |
| CausalForestDML vs. LinearDML | 19/19 |
| All three estimators | 18/19 |
| Original vs. downsampled matched comparisons | 55/57 |

The final page architecture should use either a third table or more discussion space, not automatically both.

## 10.6 Visual validation

For every final figure and table:

- reconstruct values from checked sources;
- compare labels and order;
- verify signs and negative values;
- inspect at final printed size;
- inspect grayscale;
- inspect accessibility and contrast;
- check margin and gutter fit;
- check embedded fonts;
- verify caption claims;
- ensure no identifying paths or metadata.

---

## 11. Main paper versus supplementary material

## 11.1 Main paper must contain

- full central contribution;
- resource definition;
- validation definition;
- essential construction sequence;
- LLM role and authority boundary;
- cohort sizes and proxy counts;
- predictive models and headline results;
- estimators and headline agreement;
- CausalPFN result;
- main limitations;
- reuse value.

## 11.2 Technical appendix should contain

- complete proxy-state definitions;
- full decision-rule tables;
- complete DAGs or graph descriptions;
- all exposure-specific adjustment sets;
- detailed preprocessing and data-contract schemas;
- exact split and cohort manifests where available;
- full predictive result tables;
- all 19 × 3 estimator values;
- matching details;
- sensitivity and permutation details;
- outcome-downsampled results;
- complete settings and hyperparameters;
- runtime environment;
- additional validation contract details;
- reproducibility-checklist explanations;
- release and licensing notes.

## 11.3 Code and data appendix

Prepare an anonymized package containing, subject to access and licensing restrictions:

- source code needed to construct and analyze the resources;
- preprocessing scripts;
- configuration files;
- schema definitions;
- tests and validation scripts;
- manifests or representative safe examples;
- environment specification;
- exact run commands;
- README with construction and reuse instructions;
- license information;
- instructions for obtaining MIMIC-III and PhysioNet data;
- no raw restricted patient-level source data;
- no author-identifying repository history or paths.

## 11.4 Supplement rule

The supplement may deepen the evidence but may not carry a fact essential to evaluating the primary contribution.

---

## 12. Reproducibility checklist plan

The AAAI checklist is a design input from the beginning, not an administrative task at the end.

### 12.1 Checklist categories relevant to this paper

#### General structure

- conceptual outline of the method;
- clear separation of fact from interpretation;
- pedagogical references.

#### Dataset usage

- motivation for MIMIC-III and PhysioNet;
- inclusion or description of the novel derived resources;
- public-availability and licensing plan;
- citations and access conditions for source datasets.

#### Computational experiments

- hyperparameter search ranges and selection criterion;
- preprocessing code;
- full experiment code;
- public release plan;
- code comments and paper mapping;
- random seed policy;
- hardware and software infrastructure;
- metric definitions;
- number of runs;
- variation/confidence analysis;
- statistical tests;
- final hyperparameters.

### 12.2 Checklist gap register

Create an internal table:

```text
question
planned answer
supporting section or appendix
missing evidence
owner
blocking status
```

### 12.3 Honest but strategic answers

A `partial` or `no` answer is not automatically fatal. It must be consistent with the paper’s claims.

For example:

- no significance test means the paper must not claim statistical superiority;
- restricted source data can still support a public construction pipeline and derived schema, subject to licenses;
- one archived run can still support a resource paper if run count is stated clearly and not presented as uncertainty analysis;
- missing LLM ablation is acceptable because LLM superiority is not the central claim.

### 12.4 Checklist completion gate

Before submission, every question must have:

- a final answer;
- a location in the paper or supplement;
- a truthful explanation where needed;
- no contradiction with manuscript claims.

---

## 13. Repository and file organization

The active workspace is:

```text
thesis-writing/paper-aaai/
```

Recommended working layout:

```text
paper-aaai/
  AnonymousSubmission2027.tex       # retained Author Kit reference
  aaai2027.sty
  aaai2027.bst
  ReproducibilityChecklist.tex
  paper.tex                          # single main manuscript source
  references.bib                    # paper-only or curated bibliography
  figures/
    pipeline.pdf
    estimator_agreement.pdf
  supplement/
    technical_appendix.tex
    technical_appendix.pdf
  code-data-appendix/
    README.md
    ...
  evidence/
    claim_evidence_map.md
    checklist_gap_register.md
    figure_value_checks.md
  builds/                            # generated, normally ignored
```

Before creating these paths, inspect the existing `paper-aaai/` folder and preserve the Author Kit files. Do not duplicate files that already serve the role.

### 13.1 Single-source requirement

The submitted main manuscript should use one principal `.tex` source containing all paper prose. Custom macros may be kept in that source. Avoid `\input` for the paper body unless the final AAAI instructions explicitly allow it and the source package remains compliant.

### 13.2 Bibliography

Options:

- use a curated paper-specific `.bib` extracted from the thesis corpus;
- avoid importing the entire thesis bibliography if it contains unused entries or sensitive metadata;
- validate every key;
- use `natbib` commands supported by the Author Kit;
- do not add `biblatex`.

### 13.3 Generated artifacts

Generated PDFs, auxiliary files, and compilation caches should not be confused with source. Establish a clear ignore policy before repeated builds.

---

## 14. Roles, transition review, and model-routing policy

## 14.1 ChatGPT — coordinator and independent stage reviewer

ChatGPT will:

- maintain the canonical plan and contribution hierarchy;
- inspect the latest repository commits and durable stage reports;
- compare the actual diff against the authorized scope;
- verify scientific, numerical, build, and formatting evidence;
- decide whether the next action is a narrow repair or advancement;
- choose the model and reasoning level for the next bounded Codex task;
- write the next Codex prompt;
- perform whole-paper scientific review and final claim calibration;
- never accept a stage solely because Codex says it is complete.

Whenever the author writes **“move to the next part”**, ChatGPT must:

1. inspect the current HEAD and at least the most relevant latest commit or commits;
2. read the durable report from the completed stage;
3. inspect the manuscript and artifact diff relevant to that stage;
4. validate the required build, numerical, visual, and protected-file evidence;
5. decide explicitly between:
   - `NARROW REPAIR REQUIRED`, or
   - `READY TO ADVANCE`;
6. write the next Codex prompt with an explicit model and reasoning assignment.

This transition review uses **Sol-extra high** because it requires the full accumulated project and manuscript context.

## 14.2 Codex — bounded implementation agent

Codex will execute one explicitly authorized stage at a time. Depending on the prompt, it may:

- inspect repository evidence;
- write or revise bounded manuscript sections;
- construct tables and figures from checked sources;
- update the claim–evidence map;
- compile and visually inspect the manuscript;
- prepare supplement and submission artifacts;
- perform narrow technical or numerical audits.

Codex must not independently redesign the contribution hierarchy, broaden scope, overwrite protected evidence, or silently reinterpret checked results.

Every Codex stage from P3 onward must write a durable report under:

```text
thesis-writing/paper-aaai/reports/
```

The report replaces manual copying of Codex chat output. It must record, as applicable:

```text
stage
model and reasoning effort
baseline HEAD and inspected commits
sources inspected
files changed
claims and numbers added
numerical source mapping
build command and result
PDF page count and visual checks
open evidence/runtime/release gates
protected-file verification
readiness decision
```

## 14.3 Author

The author will:

- confirm scientific intent and priorities;
- provide authoritative historical experiment knowledge;
- decide repository-cleanup timing;
- provide author list, order, metadata, conflicts, and release commitments;
- read, verify, revise, and adopt the manuscript as human scholarly work;
- coordinate supervisor feedback;
- approve the exact final submission artifacts;
- submit the paper.

## 14.4 Supervisor

The supervisor will:

- confirm the central dataset contribution;
- review causal and clinical language;
- confirm CausalPFN positioning;
- assess novelty and AAAI relevance;
- approve the final scientific narrative.

## 14.5 Model quality and token-efficiency policy

The following rankings are project-specific operational judgments, not external benchmark claims.

### Comparable-task quality ranking

For the four bounded options explicitly considered:

```text
Sol-medium
> Terra-extra high
> Terra-high
> Terra-medium
```

### Raw token-efficiency ranking

```text
Terra-medium
> Sol-medium
> Terra-high
> Terra-extra high
```

### Effective quality-per-token ranking for this paper

```text
Sol-medium
> Terra-high
> Terra-extra high
> Terra-medium
```

Terra-medium is inexpensive but is not trusted for manuscript prose, evidence interpretation, numerical auditing, or stage-level decisions. It should be avoided except for trivial housekeeping.

### Routing rules

#### Sol-extra high

Use when the model must understand or judge the entire accumulated context:

- every “move to the next part” transition review;
- Introduction and Related Work after the body is known;
- whole-paper claim/evidence audit;
- global page-limit compression;
- abstract writing from the final manuscript;
- integration of author and supervisor feedback;
- final scientific readiness decision.

#### Sol-high

Use for truly difficult but bounded scientific tasks:

- Results interpretation and result-led writing;
- Discussion and limitations;
- resolving conflicts among checked sources;
- calibrating CausalPFN against the DML results;
- deciding main-paper versus supplement scientific priority.

#### Sol-medium

Use as the default for bounded scientific writing when the evidence and structure are already frozen:

- concise section rewrites;
- transitions and captions;
- supplement prose derived from approved content;
- localized supervisor-comment responses;
- conclusion-only revisions;
- shortening without changing the argument.

#### Terra-high

Use for bounded technical implementation where scientific interpretation is already specified:

- figure generation from checked tables;
- LaTeX integration and build repair;
- table construction;
- supplement assembly;
- reproducibility checklist preparation;
- anonymity and package audits;
- exact file and artifact validation.

#### Terra-extra high

Use rarely, as an independent deep technical audit when a difficult technical artifact warrants a second model family:

- independent numerical audit of Results;
- adversarial validation of a figure-generation script;
- difficult LaTeX/layout diagnosis;
- checking that no checked row was omitted, duplicated, or misrounded.

Do not use Terra-extra high as the normal drafting model.

#### Terra-medium

Use only for trivial, fully specified housekeeping such as:

- listing files;
- checking whether exact paths exist;
- running a predefined build command;
- confirming an exact changed-file list.

It is not assigned to any substantive paper stage.

## 15. End-to-end stage plan

### 15.1 Common execution protocol

Every stage must:

1. inspect the current HEAD, recent relevant commits, branch, submodules, and dirty work;
2. read the canonical plan and prior-stage report;
3. preserve unrelated work and protected evidence;
4. use only the authorized source hierarchy;
5. write or update the required manuscript/artifact files;
6. update the claim–evidence map when claims or numbers change;
7. compile and visually inspect the PDF when LaTeX changes;
8. create a durable stage report;
9. end with one explicit readiness line;
10. leave the advance/repair decision to the subsequent Sol-extra-high transition review.

Repository cleanup is currently deferred by author decision. Tracked generated files are not a scientific-stage blocker unless the author changes this policy.

---

## Stage P0 — Baseline and source freeze — COMPLETE

### Purpose

Freeze repository revisions, Author Kit files, checked results, literature, runtime evidence, protected numerical claims, and unresolved source gaps.

### Durable output

- baseline and source records;
- protected numerical claim list;
- unresolved evidence register.

### Exit

```text
READY FOR STAGE P0A — PAPER BASELINE FROZEN
```

---

## Stage P0A — AAAI structure and genre study — COMPLETE

### Purpose

Learn the AAAI-27 scientific structure, format, page budget, visual conventions, checklist obligations, and main-paper/supplement boundary.

### Exit

```text
READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED
```

---

## Stage P1 — Scientific story and claim map — COMPLETE

### Purpose

Lock the contribution hierarchy, supported claims, evidence sources, qualifications, protected numbers, and unresolved gates.

### Exit

```text
READY FOR STAGE P2 — CLAIMS AND EVIDENCE LOCKED
```

---

## Stage P2 — AAAI manuscript skeleton — COMPLETE

### Purpose

Create and compile the anonymous AAAI-27 manuscript skeleton with the approved title, section architecture, bibliography, and placeholders.

### Exit

```text
READY FOR STAGE P3 — AAAI SKELETON COMPILES
```

---

## Stage P3 — Dataset construction and validation — COMPLETE

### Purpose

Write the primary resource-contribution section, Table 1, Figure 1 specification, validation definition, provenance boundaries, and reuse claims.

### Exit

```text
READY FOR STAGE P4 — RESOURCE CONTRIBUTION DRAFTED
```

---

## Stage P4 — Empirical Evaluation — COMPLETE

### Purpose

Define prediction tasks and metrics, estimator roles, directional triangulation, matching, sensitivity, permutations, downsampling, and the no-pooling policy.

### Exit

```text
READY FOR STAGE P5 — EMPIRICAL EVALUATION DRAFTED
```

---

## Stage P5 — Results, visuals, and numerical audit — CURRENT

### Primary model

```text
Sol-high
```

Use Terra-high only for a separate bounded figure/table implementation task when this avoids loading the complete scientific context into a technical model. Use Terra-extra high only if an independent numerical or plotting audit is justified by complexity or conflict.

### Objective

Write the complete result-led section and trace every rendered number to checked evidence.

### Required work

- complete predictive-results table;
- primary CausalForestDML patterns;
- 19/19 CausalForestDML–LinearDML agreement;
- prominent 18/19 all-three-estimator result including CausalPFN;
- explicit PhysioNet-shock disagreement;
- matching availability and directional agreement;
- 55/57 original-versus-downsampled directional stability;
- cross-dataset synthesis without pooling;
- Figure 2 or a complete justified fallback;
- complete numerical audit and evidence-map update.

### Durable report

```text
thesis-writing/paper-aaai/reports/P5_results_report.md
```

### Exit

```text
READY FOR STAGE P6 — RESULTS DRAFTED AND NUMERICALLY MAPPED
```

---

## Stage P6 — Discussion, Limitations, and Conclusion

### Model

```text
Sol-high
```

### Why these tasks are combined

Discussion, limitations, future work, and conclusion use the same frozen Results context and claim boundaries. Writing them together prevents duplicated context loading and keeps the conclusion aligned with the exact interpretation.

### Objective

Interpret the completed evidence positively and responsibly, then close the paper without adding new claims.

### Required content

- research utility and reuse;
- portability across heterogeneous ICU resources;
- interpretation of predictive dataset dependence;
- 19/19 DML triangulation;
- 18/19 CausalPFN triangulation and the PhysioNet-shock exception;
- LLM-assisted design implications;
- concise centralized limitations:
  - proxy construct validity;
  - observational identification;
  - diagnostic-coverage differences;
  - incomplete historical producing lineage;
  - runtime and release state;
- prioritized future research;
- concise resource-focused conclusion.

### Durable report

```text
thesis-writing/paper-aaai/reports/P6_discussion_conclusion_report.md
```

### Exit

```text
READY FOR STAGE P7 — INTERPRETATION AND CONCLUSION DRAFTED
```

---

## Stage P7 — Introduction and Related Work

### Model

```text
Sol-extra high
```

### Why these tasks are combined

The Introduction defines the gap and contribution; Related Work must prove that gap and distinguish CliniCause from prior work. Both require the complete manuscript and approved literature context.

### Internal order

1. inspect the completed body and evidence map;
2. draft the gap-led Related Work synthesis;
3. draft the Introduction around the proven paper contribution;
4. write the contribution list and headline findings;
5. review the title for consistency.

### Required content

- motivation and problem;
- gap in reusable causal-analysis resources for irregular ICU data;
- concise CliniCause approach;
- dataset and validation contribution;
- headline predictive and estimator-agreement findings;
- three or four explicit contributions;
- compact Related Work covering only literature needed to establish the gap:
  - irregular clinical time-series modeling;
  - proxy/weak-label construction;
  - causal ML and heterogeneous-effect estimation;
  - clinical dataset/resource construction;
  - LLM-assisted domain design;
  - CausalPFN only when a verified source is available.

### Durable report

```text
thesis-writing/paper-aaai/reports/P7_introduction_related_work_report.md
```

### Exit

```text
READY FOR STAGE P8 — COMPLETE MAIN-PAPER BODY DRAFTED
```

---

## Stage P8 — Final Figures, Tables, Supplement, and Code/Data Appendix

### Primary model

```text
Terra-high
```

Use Sol-medium only for a short bounded scientific prose subtask that cannot be derived mechanically from approved manuscript text.

### Why these tasks are combined

They share the same numerical sources, artifact layout, cross-reference structure, and main-paper/supplement boundary.

### Required work

- finalize Figure 1;
- audit and finalize Figure 2;
- optimize Tables 1 and 2;
- prepare complete estimator tables;
- prepare matching, sensitivity, permutation, and downsampling details;
- document proxy definitions, DAG metadata, settings, and provenance;
- prepare technical appendix and code/data appendix content;
- verify all visual numbers and labels;
- maintain anonymous and license-safe artifacts.

### Durable report

```text
thesis-writing/paper-aaai/reports/P8_artifacts_supplement_report.md
```

### Exit

```text
READY FOR STAGE P9 — PAPER AND SUPPLEMENT ARTIFACTS COMPLETE
```

---

## Stage P9 — Whole-Paper Audit, Scientific Compression, Human Feedback, and Abstract

### Model

```text
Sol-extra high
```

### Why these tasks are combined

All tasks require the same complete manuscript, evidence map, literature, page architecture, and supplement context. The abstract must be written only after the audited and compressed paper stabilizes.

### Ordered workflow

1. audit every material claim, citation, number, and qualification;
2. verify current-code versus historical-run language;
3. resolve or retain exact evidence gates;
4. audit literature coverage and citation validity;
5. remove repetition and compress to the AAAI technical-content limit;
6. preserve the resource contribution and headline results during compression;
7. integrate consolidated author and supervisor feedback;
8. re-audit the final scientific narrative;
9. finalize title and keywords;
10. write the abstract last from the stabilized manuscript.

### Compression priority

1. repeated limitations;
2. redundant explanations;
3. low-value background;
4. settings and secondary diagnostics that belong in the supplement;
5. low-priority LLM process detail;
6. verbose captions and transitions.

Never compress using font, margin, spacing, or float hacks.

### Human checkpoint

Before the stage exits, the author and supervisor must review the scientific claims, contribution hierarchy, CausalPFN framing, limitations, title, and exact compressed PDF. Their comments should be consolidated before one final revision pass.

### Durable report

```text
thesis-writing/paper-aaai/reports/P9_global_audit_compression_abstract_report.md
```

### Exit

```text
READY FOR STAGE P10 — SCIENTIFIC CONTENT APPROVED AND WITHIN BUDGET
```

---

## Stage P10 — Submission Readiness, Compliance, and Final Package

### Primary model

```text
Terra-high
```

The subsequent final transition review uses Sol-extra high. If a substantive scientific defect is found, return to a bounded P9 repair rather than rewriting science inside P10.

### Required work

- verify current AAAI-27 rules and generative-AI policy;
- complete the reproducibility checklist truthfully;
- validate anonymous main PDF and supplement;
- validate source-package structure;
- validate page size, columns, fonts, references, captions, figures, tables, and metadata;
- search all review artifacts for identifying names, institutions, paths, URLs, usernames, commit metadata, and acknowledgments;
- validate release statement, license, source-data access instructions, and anonymous code/data package;
- perform a clean final build;
- inspect every page visually;
- generate checksums and a submission inventory;
- cross-check OpenReview metadata against the manuscript;
- preserve the exact author-approved artifacts.

### Durable report

```text
thesis-writing/paper-aaai/reports/P10_submission_readiness_report.md
```

### Exit

```text
READY FOR AAAI-27 SUBMISSION
```

---

## 16. Immediate remaining plan

The paper is currently at Stage P5.

### Remaining sequence

1. **P5 — Sol-high:** complete Results, Table 2, Figure 2, and numerical audit;
2. **P6 — Sol-high:** write Discussion, Limitations, and Conclusion together;
3. **P7 — Sol-extra high:** write Related Work and Introduction from the complete body;
4. **P8 — Terra-high:** finalize visuals, tables, supplement, and code/data appendix;
5. **P9 — Sol-extra high:** perform the whole-paper audit, compression, human-feedback integration, and abstract;
6. **P10 — Terra-high:** complete compliance, anonymity, checklist, packaging, and final build.

Each transition is reviewed with **Sol-extra high** after the author writes “move to the next part.”

### Current completion standard

P5 is complete only when the Results prose, predictive table, estimator-comparison visual or justified fallback, numerical audit, evidence-map updates, successful build, and durable P5 report all pass independent transition review.

---

## 17. Missing inputs and decision register

## 17.1 Required for submission metadata

- final author list;
- author order;
- contact author;
- track selection;
- OpenReview subject areas/keywords;
- conflicts of interest;
- concurrent-submission status;
- release commitment;
- code/data license;
- approved title.

## 17.2 Required for final reproducibility claims

- exact producing commits for archived results;
- current validated commits;
- exact runtime commands;
- environment/container identity;
- Python and major library versions;
- hardware and memory;
- seed policy;
- number of runs;
- model-selection and hyperparameter process;
- final hyperparameters;
- split lineage;
- checkpoint-to-prediction lineage;
- data-resource build outputs and hashes;
- public-release packaging decision.

## 17.3 Desirable but not necessarily blocking experiments

- repeated predictive runs and confidence intervals;
- formal paired model-comparison tests;
- additional CausalPFN diagnostics;
- clinician evaluation of proxy states and DAGs;
- LLM ablation or manual-design baseline;
- prompt sensitivity;
- alternate-LLM replication;
- external clinical validation;
- prospective validation.

These are not blockers unless the manuscript makes a claim that requires them.

---

## 18. Risk register and mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Dataset contribution sounds like ordinary preprocessing | Novelty weakened | Make resource schema, validation contracts, and reuse central in title, Figure 1, contributions, and Results |
| “Validated causal dataset” is misread as validated causality | Reviewer skepticism | Define “validated causal-analysis dataset” precisely once; retain strong resource language thereafter |
| Paper contains too many stories | Diluted contribution | Primary resource story; pipeline second; empirical characterization third; LLM fourth |
| CausalPFN is underemphasized | Supervisor priority missed | Headline 18/19 result in Introduction, Results, Figure/Table, Discussion, and abstract |
| CausalPFN is overclaimed | Scientific weakness | Emphasize directional triangulation, not equal magnitude, identification, or diagnostic parity |
| Seven pages cannot fit full thesis scope | Incomplete narrative | Page architecture, high-value visuals, technical appendix, scientific compression |
| Repeated disclaimers make paper pessimistic | Contribution appears weak | Centralize boundaries; lead paragraphs with findings and opportunity |
| Missing uncertainty/statistical tests | Predictive ranking challenged | Avoid superiority claim; report archived leaders and dataset dependence; state run evidence exactly |
| Runtime/code provenance changes during writing | Paper becomes inconsistent | Frozen evidence map; post-debug verification pass; exact TODO markers |
| Resource cannot be fully public due source-data licenses | Checklist/release issue | Release construction code, schemas, manifests, safe derived artifacts as permitted; document source access process |
| Anonymous package leaks identity | Desk rejection | Dedicated source/PDF/ZIP anonymity audit and metadata cleaning |
| Author Kit violation during compression | Rejection or return | No style hacks; compress content; validate fonts, pages, overflow, captions, and source structure |
| Abstract written too early misstates paper | Misalignment | Abstract written after full body |
| Main contribution remains only in supplement | Reviewers miss it | Main paper includes resource definition, validation, core results, and reuse claim |

---

## 19. Quality standards for the final paper

The final paper should satisfy all of the following.

### Scientific

- primary claim is explicit and supported;
- datasets are defined sufficiently for reuse;
- validation scope is clear;
- all headline results trace to checked evidence;
- CausalPFN result is visible and accurately framed;
- no causal or clinical overclaim;
- no unnecessary self-diminishment;
- limitations are precise and constructive;
- discussion explains research value beyond the current experiments.

### Narrative

- the first page communicates the problem, solution, contribution, and headline findings;
- the paper reads as one story;
- each experiment evaluates a stated claim;
- figures and tables carry major explanatory load;
- the abstract matches the final paper;
- the conclusion points toward reuse and follow-up research.

### AAAI

- valid 2027 anonymous format;
- correct paper size and columns;
- content within official page limit;
- self-contained main paper;
- reproducibility checklist complete;
- supplement organized;
- code/data package compliant;
- source and PDF anonymous;
- no forbidden formatting;
- all pages visually inspected.

### Reproducibility and release

- source-dataset access conditions documented;
- exact construction instructions available;
- schemas and resource contents documented;
- environment and commands recorded;
- code and safe data artifacts packaged as permitted;
- release statement matches actual availability;
- final artifacts versioned and checksummed.

---

## 20. Definition of done

The AAAI paper project is complete when:

- the full article is written in the AAAI-27 format;
- the primary contribution is the reusable validated causal-analysis datasets;
- the dataset construction and validation are clear and self-contained;
- CausalPFN’s 18/19 directional agreement is prominently and accurately presented;
- the LLM-assisted design layer is integrated without displacing the primary story;
- all important numerical statements are evidence-verified;
- the manuscript is confident and optimistic while scientifically bounded;
- the technical content fits the official page limit without formatting manipulation;
- the abstract was written from and matches the complete paper;
- the reproducibility checklist is complete and truthful;
- the technical appendix and code/data package are prepared;
- author identities and metadata are absent from review artifacts;
- all fonts, figures, tables, citations, and pages pass validation;
- the author and supervisor approve the exact final PDF;
- the submitted artifact is the same artifact that was approved.

---

## 21. Canonical status block

```text
PLAN VERSION: 1.1
TARGET: AAAI-27 Main Technical Track
PRIMARY CONTRIBUTION: Reusable validated causal-analysis datasets
SECONDARY CONTRIBUTION: Evidence-tracked construction pipeline
KEY EMPIRICAL EMPHASIS: CausalPFN joins directional agreement in 18/19 comparisons
LLM ROLE: Traceable design-time assistance, not runtime estimation
COORDINATOR AND TRANSITION REVIEWER: ChatGPT
IMPLEMENTATION AGENT: Codex under bounded prompts
TRANSITION REVIEW MODEL: Sol-extra high
CURRENT STAGE: P5 — Results, visuals, and numerical audit
COMPLETED STAGES: P0, P0A, P1, P2, P3, P4
REMAINING CONSOLIDATED STAGES: P5, P6, P7, P8, P9, P10
ABSTRACT ORDER: Written in P9 after full-paper audit and compression
REPOSITORY CLEANUP: Deferred by author decision; not a current scientific blocker
NEXT ACTION: Execute P5 with Sol-high, then validate the commit and P5 report with Sol-extra high
```

---

## 22. Final operating rule

> Build the paper around the resource we created, present its value confidently, and make every qualification proportionate to the exact claim. The manuscript should show that CliniCause already provides a substantial, reusable research foundation—and that its transparent boundaries make the next generation of clinical causal-AI studies easier to perform, compare, and improve.

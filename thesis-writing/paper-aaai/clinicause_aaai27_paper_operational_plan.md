# CliniCause — Complete AAAI-27 Paper Writing Operational Plan

**Document status:** Canonical paper-writing plan  
**Version:** 1.0  
**Date:** 2026-07-19  
**Target venue:** AAAI-27 Main Technical Track  
**Repository:** `KenziVisor/CliniCause`  
**Paper workspace:** `thesis-writing/paper-aaai/`  
**Working-draft writer and coordinator:** ChatGPT  
**Submission authors and scientific authorities:** the human author team and supervisor  
**Codex role:** no scientific writing; at most narrowly authorized mechanical build or repository checks if later requested

---

## 1. Purpose

This document defines the complete and stable workflow for producing a full AAAI-27 paper from the CliniCause thesis, repository, checked results, repaired pipeline, and AAAI 2027 Author Kit.

The immediate objective is to produce a complete first manuscript draft in AAAI format, then refine it through evidence verification, scientific compression, reproducibility preparation, anonymity checks, and final PDF validation.

The paper will not be a shortened thesis. It will present one focused research story:

> **CliniCause constructs reusable, validated causal-analysis datasets from heterogeneous irregular ICU records and demonstrates their analytical utility through irregular-time-series prediction, DAG-guided analysis, and cross-estimator agreement.**

The paper will be confident and constructive. It will present the achieved contributions directly and positively. Qualifications will be used where they protect scientific accuracy, not as a substitute for stating the contribution.

The central writing rule is:

> State demonstrated contributions with confidence; qualify only the boundary that is genuinely unresolved; do not weaken a valid result merely because a stronger result was not established.

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

### 2.5 Writing order

The paper body will be written before the abstract.

The drafting order is:

1. AAAI structure and genre study;
2. claims and evidence map;
3. paper skeleton and page architecture;
4. dataset construction and validation;
5. empirical setup;
6. results;
7. introduction;
8. related work;
9. discussion and conclusion;
10. abstract;
11. full-paper compression and compliance.

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

## 14. Roles and responsibility boundaries

## 14.1 ChatGPT

ChatGPT will:

- inspect the thesis and repository evidence;
- study the AAAI Author Kit and paper genre;
- design the article architecture;
- draft all manuscript sections for human scientific review and adoption;
- formulate claims and qualifications;
- produce the abstract last;
- design figures and tables conceptually;
- create or revise LaTeX source;
- audit evidence and citations;
- perform scientific compression;
- conduct anonymity and compliance checks;
- produce the final writing and validation plan.

## 14.2 Author

The author will:

- confirm scientific intent;
- provide author list and ordering;
- provide authoritative historical experiment knowledge;
- resolve uncertain run settings where possible;
- approve title, contribution hierarchy, and release commitment;
- review the full draft for accuracy and defendability;
- coordinate supervisor feedback;
- submit the paper.

## 14.3 Supervisor

The supervisor will:

- confirm the central contribution;
- validate the positioning of the datasets;
- confirm the desired emphasis on CausalPFN;
- review the causal and clinical claims;
- approve the paper’s scientific narrative.

## 14.4 Codex

Codex will not write or rewrite the scientific paper.

If later authorized, it may perform bounded mechanical tasks such as:

- running LaTeX build commands;
- reporting compilation warnings;
- locating broken citations or references;
- checking file paths;
- performing exact static searches;
- regenerating a known figure from an approved script.

Codex may not independently change claims, interpretations, structure, or scientific prose.

---

## 15. End-to-end stage plan

## Stage P0 — Baseline and source freeze

### Objective

Record the exact writing baseline and authoritative sources.

### Required work

- record current parent repository HEAD;
- record relevant submodule commits;
- inspect current `thesis-writing/paper-aaai/` state;
- record thesis baseline commit;
- identify checked result tables and manifests;
- identify current runtime validation records;
- identify literature metadata and PDFs;
- identify protected files and unrelated work;
- record Author Kit files and hashes if practical.

### Deliverables

- baseline block in the evidence map;
- authoritative source list;
- protected numerical claim list;
- unresolved source list.

### Exit

```text
READY FOR STAGE P0A — PAPER BASELINE FROZEN
```

---

## Stage P0A — AAAI structure and genre study

Defined in Section 4.

### Deliverables

- section-function map;
- page architecture;
- visual budget;
- formatting constraints;
- checklist obligations;
- reference-paper structure notes.

### Exit

```text
READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED
```

---

## Stage P1 — Scientific story and claim map

### Objective

Translate the approved strategy into a closed set of manuscript claims.

### Required work

Create a claim-evidence map with fields:

```text
claim ID
claim text
claim role: primary / secondary / supporting
supporting evidence
confidence
required qualification
paper location
figure/table
unresolved gate
```

### Primary claims

- construction of two reusable validated causal-analysis datasets;
- evidence-tracked resource construction;
- dataset-specific but structurally aligned interfaces;
- four-model predictive characterization;
- DML agreement 19/19;
- CausalPFN all-three agreement 18/19;
- value for follow-up research.

### Exit

```text
READY FOR STAGE P2 — CLAIMS AND EVIDENCE LOCKED
```

---

## Stage P2 — AAAI manuscript skeleton

### Objective

Create a compilable anonymous manuscript before filling prose.

### Required work

- copy the correct 2027 anonymous preamble;
- create the working title;
- set anonymous author information;
- create section headings;
- add figure/table placeholders;
- connect paper bibliography;
- integrate or prepare checklist according to current instructions;
- compile a blank structural PDF;
- confirm US Letter and two columns.

### Deliverables

- `paper.tex`;
- initial PDF;
- build command;
- initial warning report.

### Exit

```text
READY FOR STAGE P3 — AAAI SKELETON COMPILES
```

---

## Stage P3 — Dataset construction and validation draft

### Objective

Write the paper’s central method/resource section first.

### Source chapters

Use material from thesis chapters covering:

- data and preprocessing;
- proxy-state construction;
- prediction;
- causal methodology;
- experimental and validation design;
- reproducibility.

### Required content

All subsections in Section 9.3.

### Deliverables

- complete Section 3;
- draft Figure 1 caption and content specification;
- draft Table 1;
- exact definition of “validated causal-analysis datasets.”

### Quality gate

A technical reader should understand what the released resource contains and how it was produced without reading the code.

### Exit

```text
READY FOR STAGE P4 — RESOURCE CONTRIBUTION DRAFTED
```

---

## Stage P4 — Empirical evaluation draft

### Objective

Define experiments as tests of the paper’s claims.

### Required work

- predictive tasks and metrics;
- estimator setup;
- matching and robustness;
- run and environment details;
- resource-validation tests;
- primary versus robustness hierarchy.

### Deliverables

- complete Section 4;
- settings table or supplement plan;
- checklist updates.

### Exit

```text
READY FOR STAGE P5 — EMPIRICAL DESIGN DRAFTED
```

---

## Stage P5 — Results draft

### Objective

Write a full, result-led section with all approved numerical findings.

### Required work

- resource summary;
- predictive table;
- primary causal patterns;
- cross-estimator agreement;
- strong CausalPFN paragraph;
- robustness summary;
- cross-dataset findings;
- figure/table placeholders or initial visuals.

### Deliverables

- complete Section 5;
- Table 2;
- Figure 2 design or draft;
- numerical audit list.

### Exit

```text
READY FOR STAGE P6 — RESULTS DRAFTED AND NUMERICALLY MAPPED
```

---

## Stage P6 — Introduction and related work

### Objective

Write the opening only after the paper has proven what it can deliver.

### Required work

- Introduction narrative;
- contribution bullets;
- headline results;
- Related Work;
- gap statement;
- AAAI relevance.

### Deliverables

- Sections 1 and 2;
- title review;
- claim-evidence alignment check.

### Exit

```text
READY FOR STAGE P7 — PAPER NARRATIVE ESTABLISHED
```

---

## Stage P7 — Discussion and conclusion

### Objective

Interpret the resource and empirical findings positively and responsibly.

### Required work

- research utility;
- dataset portability;
- CausalPFN implications;
- LLM-assisted design implications;
- focused limitations;
- conclusion and future use.

### Deliverables

- Sections 6 and 7;
- no repeated qualification clutter;
- final future-work hierarchy.

### Exit

```text
READY FOR STAGE P8 — COMPLETE PAPER BODY DRAFTED
```

---

## Stage P8 — Abstract, keywords, and submission metadata

### Objective

Write the abstract from the completed manuscript.

### Abstract structure

1. problem and gap;
2. CliniCause resource contribution;
3. construction approach;
4. datasets and scale;
5. predictive result;
6. estimator and CausalPFN result;
7. reuse implication;
8. one concise interpretation boundary.

### Abstract tone

The abstract should lead with the resource and finish with opportunity, not limitations.

### Metadata

Prepare:

- final title;
- abstract;
- keywords;
- subject areas;
- author list and order for OpenReview;
- contact author;
- conflicts;
- track selection;
- code/data availability statement.

Author information stays outside the anonymous manuscript.

### Exit

```text
READY FOR STAGE P9 — COMPLETE FIRST DRAFT INCLUDING ABSTRACT
```

---

## Stage P9 — First-draft completion gate

A first draft is complete when:

- all main sections contain substantive prose;
- no section is only an outline;
- the abstract exists;
- contributions are explicit;
- all headline numbers are present;
- Figure 1 and Tables 1–2 exist at least in draft form;
- CausalPFN is visible in Results and Discussion;
- citations are inserted;
- all evidence gaps use exact standardized markers;
- the manuscript compiles in AAAI format;
- a readable PDF exists;
- page count is known;
- no author identity appears in the PDF.

The first draft may still be overlength and may still contain evidence markers.

Readiness wording:

```text
COMPLETE FIRST AAAI MANUSCRIPT DRAFT
```

---

## Stage P10 — Evidence and literature audit

### Objective

Verify every material claim before scientific compression.

### Required work

- numerical transcription checks;
- result-source checks;
- current-code versus historical-run distinction;
- literature citation validation;
- CausalPFN primary citation acquisition;
- dataset citation and license review;
- environment and run-setting audit;
- checklist gap update;
- release feasibility assessment.

### Exit states

```text
READY FOR STAGE P11 — CLAIMS VERIFIED
```

or

```text
NARROW EVIDENCE REPAIR REQUIRED — <EXACT GAP>
```

---

## Stage P11 — Scientific compression to AAAI length

### Objective

Fit the full contribution into the technical-content limit without weakening it.

### Compression order

1. delete repeated limitations;
2. merge overlapping explanations;
3. shorten background;
4. move full definitions and settings to supplement;
5. consolidate tables;
6. shorten captions without removing interpretation;
7. replace path/provenance narration with precise resource schema statements;
8. remove secondary robustness details;
9. tighten transitions;
10. remove low-priority LLM process detail before removing dataset validation detail.

### Material that must survive compression

- primary resource contribution;
- validation definition;
- dataset contents;
- cohort sizes;
- proxy construction;
- predictive annotations;
- DAG/adjustment metadata;
- STraTS versus GRU-D result;
- 19/19 DML agreement;
- 18/19 CausalPFN agreement;
- resource reuse value;
- central limitations.

### Forbidden compression methods

- font-size reduction below allowed levels;
- spacing hacks;
- margin changes;
- negative `vspace` around structure or floats;
- unreadable tables;
- removing essential operational definitions;
- moving the main contribution entirely to supplement.

### Exit

```text
READY FOR STAGE P12 — MAIN PAPER WITHIN AAAI PAGE BUDGET
```

---

## Stage P12 — Supplement and code/data package

### Objective

Provide full technical depth and reproducibility support.

### Required work

- technical appendix prose;
- complete tables and figures;
- proxy definitions and DAG details;
- settings and hyperparameters;
- runtime and environment detail;
- checklist explanations;
- anonymized code/data package;
- access and license instructions;
- representative safe artifacts.

### Exit

```text
READY FOR STAGE P13 — SUPPLEMENTARY PACKAGE COMPLETE
```

---

## Stage P13 — AAAI compliance and anonymity audit

### Source audit

Check:

- 2027 style unmodified;
- correct `submission` option;
- no forbidden packages;
- no `hyperref` or embedded links;
- no margin/spacing/font hacks;
- one main source file;
- correct bibliography mechanism;
- no manual final page breaks;
- table and figure caption placement;
- valid figure paths;
- no non-Roman fonts in text.

### PDF audit

Check:

- US Letter;
- two columns;
- no page numbers or headers;
- no overflow;
- no clipping or overlap;
- all fonts embedded;
- no Type 3 fonts;
- no bookmarks or links;
- grayscale-readable figures;
- readable final-size labels;
- correct page count;
- references after main text;
- clean metadata;
- all pages inspected individually.

### Anonymity audit

Search source, PDF, supplement, and code package for:

- author names;
- supervisor names;
- institution;
- usernames;
- emails;
- local/server paths;
- GitHub owner or repository URL if identifying;
- commit authors;
- acknowledgments;
- grant numbers;
- PDF creator/author metadata;
- comments or filenames revealing identity;
- self-citations written non-anonymously.

### Exit

```text
READY FOR STAGE P14 — ANONYMOUS AAAI SUBMISSION ARTIFACT VALIDATED
```

---

## Stage P14 — Author and supervisor review

### Author review

Check:

- accuracy of project description;
- contribution emphasis;
- defendability of claims;
- title;
- dataset release commitment;
- terminology;
- omissions;
- CausalPFN emphasis;
- optimistic tone.

### Supervisor review

Check:

- central contribution is the datasets;
- causal framing;
- validity language;
- CausalPFN interpretation;
- novelty and AAAI relevance;
- main-paper completeness;
- whether any additional result deserves priority.

### Comment handling

Consolidate feedback into one versioned list classified as:

```text
scientific
numerical
structural
interpretive
wording
citation
formatting
submission metadata
```

### Exit

```text
READY FOR STAGE P15 — CONTENT APPROVED FOR FINAL BUILD
```

---

## Stage P15 — Final build and submission handoff

### Required work

- clean source build;
- BibTeX build and repeated LaTeX passes;
- zero unresolved references/citations;
- zero material overfull boxes;
- final page-level visual review;
- final font check;
- final metadata cleaning;
- checksum generation;
- final checklist validation;
- exact final PDF preserved;
- supplementary ZIPs preserved;
- submission metadata cross-checked with manuscript.

### Submission artifacts

```text
main anonymous PDF
technical appendix PDF
code/data ZIP
optional multimedia ZIP, likely not needed
final source snapshot for archive
checksums
submission metadata record
```

### Final readiness wording

```text
READY FOR AAAI-27 SUBMISSION
```

---

## 16. Immediate plan for the first full draft

The target for the current working day is a complete manuscript draft, not a perfect final submission.

### Drafting sequence

1. confirm baseline and open `paper.tex`;
2. study Author Kit structure and extract preamble;
3. create AAAI skeleton;
4. write Section 3, Dataset Construction and Validation;
5. write Section 4, Empirical Evaluation;
6. write Section 5, Results;
7. write Introduction and contributions;
8. write Related Work;
9. write Discussion and Conclusion;
10. add provisional Figure 1 and core tables;
11. write abstract last;
12. compile and record page count;
13. mark exact evidence gaps;
14. conduct a first claim and anonymity scan.

### Today’s completion standard

The draft must be a readable paper from beginning to end. It may be overlength and some visuals may be provisional, but it must not be a collection of notes.

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
PLAN VERSION: 1.0
TARGET: AAAI-27 Main Technical Track
PRIMARY CONTRIBUTION: Reusable validated causal-analysis datasets
SECONDARY CONTRIBUTION: Evidence-tracked construction pipeline
KEY EMPIRICAL EMPHASIS: CausalPFN joins directional agreement in 18/19 comparisons
LLM ROLE: Traceable design-time assistance, not runtime estimation
WRITING OWNER: ChatGPT
ABSTRACT ORDER: Written after the full paper body
CURRENT STAGE: P0
TODAY'S TARGET: Complete first AAAI manuscript draft
NEXT ACTION: Freeze baseline, study AAAI structure, create paper skeleton, and draft the resource-construction section
```

---

## 22. Final operating rule

> Build the paper around the resource we created, present its value confidently, and make every qualification proportionate to the exact claim. The manuscript should show that CliniCause already provides a substantial, reusable research foundation—and that its transparent boundaries make the next generation of clinical causal-AI studies easier to perform, compare, and improve.

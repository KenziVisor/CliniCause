# CliniCause Thesis–Paper Story Alignment Plan

**Canonical filename:** `THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md`  
**Recommended repository location:** `thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md`  
**Status:** Approved high-level workflow; implementation has not started  
**Planning baseline inspected:** `KenziVisor/CliniCause` at commit `1b444d9fdd29efa9dfaf74db001fa4915f5cba66` (`paper sync`)  
**Primary objective:** Reframe the thesis so that its principal scientific idea matches the finished paper, while preserving the thesis’s existing technical depth, evidence discipline, detailed methods, results, limitations, and chapter structure.

---

## 1. Mission

The finished paper and the current thesis describe the same project but assign primary importance to different contributions.

The paper’s main idea is:

> CliniCause constructs clinically grounded observational causal-analysis testbeds from source-observed longitudinal ICU records without generating patient records, proxy-exposure assignments, or mortality outcomes. It moves researcher intervention from the data-generating process to the representation layer, makes proxy definitions and causal assumptions explicit, and evaluates the resulting resources through converging evidence rather than known causal ground truth.

The current thesis’s main idea is:

> CliniCause is an evidence-tracked end-to-end integration workflow connecting LLM-assisted design, deterministic proxy construction, irregular-time-series prediction, aggregation, DAG-guided adjustment, observational estimation, and provenance.

The thesis is already detailed, scientifically cautious, and structurally strong. It must **not** be rewritten from scratch. The required change is a change in contribution hierarchy:

1. **Primary contribution after revision:** construction and evaluation of clinically grounded observational causal-analysis testbeds.
2. **Enabling methodological contribution:** the detailed integrated workflow, data contracts, source-coded rules, prediction pipeline, aggregation, DAG adjustment, diagnostics, and provenance that make the testbeds inspectable and reusable.
3. **Empirical contribution:** evidence from proxy recoverability, mortality prediction, cross-estimator stability, clinical-literature corroboration, permutation checks, empirical-support diagnostics, and omitted-variable sensitivity.
4. **Boundary:** the resources do not provide known causal ground truth, clinically validated diagnoses, validated DAGs, or treatment recommendations.

The revision must preserve the thesis’s strongest current property: it explains exactly what was implemented, what each artifact supports, and where the claims stop.

---

## 2. Frozen target thesis statement

All five stages must converge on the following scientific story:

> CliniCause is an evidence-tracked framework for constructing observational causal-analysis testbeds from source-observed irregular ICU records. Instead of simulating patients, proxy exposures, treatment assignments, or mortality outcomes, it shifts researcher intervention to an explicit representation layer consisting of clinically motivated proxy states, operational rules, cohorts, causal graphs, adjustment assumptions, and provenance. The representation is instantiated deterministically and separately on MIMIC-III and PhysioNet 2012, producing two dataset-specific resources that preserve source-observed measurement, missingness, support, care-process, and outcome patterns. Because these resources have no known causal answer, they are evaluated through converging evidence: construct plausibility, proxy recoverability, mortality prediction, cross-estimator agreement, clinical-literature corroboration, permutation checks, support diagnostics, and omitted-variable sensitivity. Broad predictive and cross-estimator consistency, together with retained discrepancies and sensitivity to modest unobserved confounding, demonstrates the value of realistic observational testbeds for exposing estimator behavior and fragility that controlled benchmarks may not reveal.

The following sentence should govern the relationship between the old and new thesis stories:

> Integration and evidence tracking are not removed from the contribution; they become the machinery that makes representation-centered observational testbed construction explicit, auditable, and reusable.

---

## 3. Repository findings that control this plan

The following facts were established by a fresh repository inspection and must guide Codex.

### 3.1 Current thesis workspace

The active thesis is under:

```text
thesis-writing/thesis/
```

Its build entry point is:

```text
thesis-writing/thesis/main.tex
```

The active chapter order is:

```text
chapters/01_introduction.tex
chapters/02_background_related_work.tex
chapters/03_problem_definition_study_design.tex
chapters/04_data_preprocessing.tex
chapters/05_proxy_state_construction.tex
chapters/06_predictive_modeling.tex
chapters/07_causal_methodology.tex
chapters/08_robustness_sensitivity_validation.tex
chapters/10_results.tex
chapters/11_discussion.tex
chapters/12_conclusions_future_work.tex
```

The thesis already uses:

```text
thesis-writing/thesis/figures/
```

through `\graphicspath{{figures/}}`, and its bibliography authority is:

```text
thesis-writing/literature/metadata/references.bib
```

The current thesis title and central prose are integration-oriented. In particular:

- the title foregrounds LLM guidance, deep proxy-state prediction, and causal-effect estimation;
- Chapter 1 explicitly describes the gap as an “integration gap”;
- Chapter 1 says the integrated framework is primary;
- Chapter 11 answers the main question as a feasibility and integration result;
- Chapter 12 says the strongest contribution is the integrated connection;
- the English and Hebrew abstracts foreground methodological integration and traceability.

These statements are scientifically defensible but must become secondary to the paper’s testbed-construction story.

### 3.2 Finished paper authorities at `thesis-writing/`

The finished paper is:

```text
thesis-writing/CausalDataGeneration.pdf
```

The matching root paper source is:

```text
thesis-writing/aaai27-submission.tex
```

The finished supplementary PDF is:

```text
thesis-writing/supp.pdf
```

At the inspected baseline, the root `aaai27-submission.tex` and the Overleaf-copy file below had the same Git blob SHA, but Codex must verify current local equality rather than assume it:

```text
thesis-writing/paper-aaai/aaai27-submission.tex
```

The finished paper PDF is the principal authority for the paper’s final visible scientific story. The matching final source is the authority for reusable prose structure, labels, equations, figure references, and bibliography keys.

### 3.3 `paper-aaai/` is useful but must be handled cautiously

The Overleaf project copy is:

```text
thesis-writing/paper-aaai/
```

Use only the following as focused supporting material:

```text
paper-aaai/aaai27-submission.tex
paper-aaai/references.bib
paper-aaai/supplementary1.tex
paper-aaai/figures/
paper-aaai/paper_evidence_map.md
paper-aaai/reports/
paper-aaai/evidence/
```

Important caution:

```text
paper-aaai/paper.tex
paper-aaai/paper.pdf
```

are older artifacts with an earlier integration/resource-level paper story. They are **not** the authority for the final paper’s main idea and must not override `CausalDataGeneration.pdf` or `aaai27-submission.tex`.

The directory:

```text
thesis-writing/ignore-paper-aaai/
```

is a superseded duplicate/archive and must be ignored completely during this mission.

The AAAI author-kit files under:

```text
paper-aaai/AuthorKit27/
```

are formatting references, not scientific evidence.

### 3.4 Paper figures relevant to the thesis

The final paper’s two most important new explanatory figures are available as:

```text
thesis-writing/paper-aaai/figures/figure1_pipeline.pdf
thesis-writing/paper-aaai/figures/figure3_shock_proxy_example.png
```

They should be copied, without modifying the originals, into the thesis figure directory under clear thesis-specific filenames, for example:

```text
thesis-writing/thesis/figures/clinicause_testbed_pipeline.pdf
thesis-writing/thesis/figures/clinicause_shock_proxy_example.png
```

The paper directory also contains:

```text
paper-aaai/figures/figure2_estimator_agreement.pdf
paper-aaai/figures/mimic_causal_dag.png
paper-aaai/figures/physionet_causal_dag.png
```

The thesis already contains result-ranking/agreement figures and both dataset DAGs. Stage 1 must determine whether the paper’s estimator-agreement figure should replace an existing thesis figure or remain unused to avoid duplication. The DAG images must not be duplicated unless the audit finds that the paper copies materially improve or correct the active thesis versions.

Minimum figure requirement for this mission:

1. add the paper’s three-stage CliniCause pipeline figure;
2. add the paper’s deterministic shock-proxy example.

### 3.5 Existing thesis strengths that must survive

The current thesis already contains detailed and valuable material on:

- irregular ICU measurements and missingness;
- dataset-specific source and artifact contracts;
- design-time versus executed-layer separation;
- proxy-state operational definitions;
- four predictive models;
- probability and binary prediction exports;
- five-source aggregation;
- source-coded DAGs and adjustment logic;
- estimator hierarchy;
- matching and support diagnostics;
- original and outcome-downsampled populations;
- permutation and omitted-variable sensitivity evidence;
- result-admission policy;
- numerical traceability versus clean-checkout reproducibility;
- extensive causal, clinical, and deployment limitations.

This content is not obsolete. The revision should mostly change chapter openings, transitions, contribution hierarchy, interpretation, and synthesis, with only the additions required by the paper’s evaluation story.

---

## 4. Source and evidence hierarchy

When sources differ, Codex must use the following order.

### 4.1 Scientific narrative authority

1. `thesis-writing/CausalDataGeneration.pdf`
2. `thesis-writing/aaai27-submission.tex`
3. `thesis-writing/supp.pdf`
4. `thesis-writing/paper-aaai/aaai27-submission.tex`
5. `thesis-writing/paper-aaai/supplementary1.tex`
6. relevant final-paper reports and evidence maps under `paper-aaai/`

The finished paper defines the target contribution hierarchy, but it must not be edited.

### 4.2 Thesis implementation and detail authority

1. active source under `thesis-writing/thesis/`
2. current rendered thesis PDF at `thesis-writing/thesis/main.pdf`
3. existing thesis evidence and audit records under `thesis-writing/logs/`, `results/`, `reproducibility/`, `planning/`, and `audit/`

The thesis remains the authority for its detailed implementation account and bounded historical provenance.

### 4.3 Numerical authority

For any numerical value, use this order:

1. checked thesis result CSVs, manifests, and checksums;
2. finished paper and supplementary numerical tables;
3. approved result-source packets and decision registers;
4. current thesis tables;
5. paper reports only when they point to an approved numerical source.

Do not introduce a number only because it appears in a draft, comment, unused table, old `paper.tex`, or generated auxiliary file.

### 4.4 Bibliography authority

The active thesis bibliography remains:

```text
thesis-writing/literature/metadata/references.bib
```

The paper bibliography:

```text
thesis-writing/paper-aaai/references.bib
```

may be used to identify missing citation entries required for the new benchmark/testbed framing or clinical-evidence comparison. Before copying an entry:

- search the thesis bibliography for an existing equivalent;
- preserve the thesis’s key if already present;
- avoid duplicate DOI/title entries;
- copy only verified entries actually cited in the revised thesis;
- do not alter the paper bibliography.

No new internet research is part of this mission unless explicitly authorized later.

---

## 5. Protected material

### 5.1 Absolutely read-only

Codex must not modify, regenerate, reformat, or “clean”:

```text
thesis-writing/CausalDataGeneration.pdf
thesis-writing/aaai27-submission.tex
thesis-writing/supp.pdf
thesis-writing/paper-aaai/**
thesis-writing/ignore-paper-aaai/**
```

Copying an exact figure file from `paper-aaai/figures/` into `thesis/figures/` is allowed. The source file must remain byte-identical.

### 5.2 Scientifically frozen unless a later prompt explicitly authorizes a checked change

- all admitted cohort counts;
- all predictive metrics;
- all proxy definitions and thresholds;
- all model names and the four-model scope;
- the one-rule-plus-four-prediction aggregation description;
- the nine MIMIC and ten PhysioNet exposure counts;
- all CausalForestDML, LinearDML, and CausalPFN values;
- estimator hierarchy;
- matching values and failure statuses;
- sampling-condition definitions;
- permutation and sensitivity values and statuses;
- graph edge sets and adjustment sets;
- existing provenance limitations;
- the no-pooling policy.

### 5.3 Out of scope

Do not:

- run new experiments;
- retrain models;
- rerun the causal pipeline;
- change code outside the thesis-writing task;
- edit the paper;
- redesign the proxy rules or DAGs;
- add a new estimator;
- change results to improve agreement with literature;
- remove discrepancies;
- claim known causal ground truth;
- claim clinical validation;
- compress the thesis merely to resemble the paper;
- restructure the thesis chapter by chapter from scratch;
- conduct broad repository cleanup;
- stage, commit, or push unless the stage prompt explicitly authorizes it.

---

## 6. Terminology and claim policy

The revised thesis must consistently use these distinctions.

### 6.1 Preferred terms

Use:

- “observational causal-analysis testbed”;
- “observational resource for evaluating estimator behavior”;
- “representation-centered construction”;
- “source-observed records, measurements, missingness, support, and mortality”;
- “proxy-state exposure”;
- “rule-derived proxy label”;
- “construct plausibility”;
- “proxy recoverability”;
- “cross-estimator stability/agreement”;
- “clinical-evidence corroboration” or “contextual clinical comparison”;
- “model-estimated mean CATE summary”;
- “omitted-variable sensitivity”;
- “diagnostic value”;
- “known causal answer” or “causal answer key” only when contrasting with synthetic or experimentally anchored benchmarks.

### 6.2 Terms requiring qualification

“Benchmark” is allowed only with an explicit qualifier such as:

> observational testbed without known causal ground truth

or:

> complementary to synthetic and semi-synthetic benchmarks that provide constructed answer keys.

Do not call the CliniCause resources “ground-truth causal benchmarks.”

“Validated” may refer only to a named validation dimension, such as schema validation, artifact validation, numerical checking, or construction integrity. It must not imply clinical construct validation or causal identification.

### 6.3 Prohibited implication chains

The thesis must never imply:

```text
predictive recoverability -> clinical correctness
cross-estimator agreement -> estimator accuracy
clinical-literature similarity -> causal validation
permutation success -> identification
matching availability -> positivity
DAG encoding -> graph correctness
literature-grounded proxy -> validated diagnosis
LLM proposal -> expert consensus
numerical traceability -> full reproducibility
```

### 6.4 Central interpretation

The final discussion should make this contrast explicit:

> Agreement shows that a pattern is not unique to one fitted estimator under one fixed representation. Sensitivity and discrepancies show why agreement alone is insufficient. This combination is precisely what makes the resources useful as diagnostic observational testbeds.

---

## 7. Five-stage implementation workflow

The mission uses exactly five Codex prompts after this plan is installed. Each stage is bounded, produces a durable report, and stops for independent review before the next stage.

---

# Step 1 — Focused read-only alignment audit

**Model:** GPT-5.6  
**Reasoning:** Extra High  
**Primary mode:** inspection and report only  
**Thesis prose edits:** forbidden  
**Permitted new file:** the Step 1 report only

## Objective

Produce a surgical map from the current thesis to the finished paper’s contribution hierarchy before any thesis prose is changed.

## Required focused inspection

Start at repository root and inspect:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git log -10 --oneline
```

Then inspect only the mission-critical material first:

```text
thesis-writing/thesis/
thesis-writing/CausalDataGeneration.pdf
thesis-writing/aaai27-submission.tex
thesis-writing/supp.pdf
thesis-writing/paper-aaai/aaai27-submission.tex
thesis-writing/paper-aaai/supplementary1.tex
thesis-writing/paper-aaai/references.bib
thesis-writing/paper-aaai/figures/
thesis-writing/paper-aaai/paper_evidence_map.md
thesis-writing/paper-aaai/reports/
thesis-writing/literature/metadata/references.bib
```

Do not recursively inspect the entire repository unless a specific thesis claim cannot be resolved from these sources.

Explicitly ignore:

```text
thesis-writing/ignore-paper-aaai/
thesis-writing/paper-aaai/paper.tex
thesis-writing/paper-aaai/paper.pdf
thesis-writing/paper-aaai/AuthorKit27/
```

except that `paper.tex` may be mentioned in the report as a superseded artifact that must not control the edit.

## Required audit products

The report must include:

1. **Source authority check**
   - verify that root and `paper-aaai` final submission sources match or explain any difference;
   - record current SHA-256 hashes for the final paper, root source, supplement, and protected paper tree;
   - identify all superseded paper artifacts.

2. **Thesis story map**
   - locate every passage that makes integration, pipeline feasibility, traceability, or engineering the primary contribution;
   - classify each passage as:
     - retain unchanged;
     - retain but subordinate;
     - reframe;
     - add paper-derived context;
     - remove only if redundant.

3. **Chapter-by-chapter intervention map**
   - exact files and sections to edit;
   - intended conceptual change;
   - material to preserve;
   - expected scale: small, medium, or major-but-localized.

4. **Benchmark/testbed literature gap**
   - identify paper citations needed to explain synthetic, semi-synthetic, RCT-derived, empirically anchored, and observational evaluation;
   - check which keys already exist in the thesis bibliography;
   - list only missing entries that will be needed.

5. **Evaluation-axis gap**
   - map current thesis coverage of:
     - construct plausibility;
     - proxy recoverability;
     - mortality prediction;
     - estimator sign/rank/magnitude agreement;
     - clinical-evidence corroboration;
     - permutation checks;
     - omitted-variable sensitivity;
     - support and matching.
   - identify what is absent or currently too secondary.

6. **Figure integration map**
   - verify the paper figure files against the finished PDF;
   - propose exact thesis filenames, chapter locations, captions, labels, and cross-references;
   - assess whether `figure2_estimator_agreement.pdf` should replace an existing thesis figure or be excluded as redundant;
   - confirm that DAG figures should not be duplicated.

7. **Frozen-content inventory**
   - capture the current title, abstracts, main research question, contribution statements, key numerical claims, table counts, figure list, bibliography keys, and chapter labels needed for later comparison.

8. **Risk register**
   - duplicate paper copies;
   - superseded `paper.tex`;
   - paper-edit risk;
   - bibliography duplication;
   - overclaim risk;
   - Hebrew/English mismatch risk;
   - figure-resolution/layout risk;
   - accidental numerical drift;
   - excessive rewriting.

## Required report

Create:

```text
thesis-writing/logs/testbed_story_alignment_step_1_audit.md
```

End the report with one of:

```text
READY FOR STEP 2
```

or:

```text
BLOCKED BEFORE STEP 2
```

with exact blocking reasons.

---

# Step 2 — Reframe the intellectual proposition

**Model:** GPT-5.6  
**Reasoning:** Extra High  
**Primary scope:** title, Chapter 1, relevant Chapter 2 framing, Chapter 3 resource definition, first paper figure

## Objective

Make the thesis’s opening intellectual proposition match the finished paper while preserving the thesis’s richer detail.

## Expected files

The exact list must come from Step 1, but likely permitted files are:

```text
thesis-writing/thesis/frontmatter/administrative_metadata.tex
thesis-writing/thesis/chapters/01_introduction.tex
thesis-writing/thesis/chapters/02_background_related_work.tex
thesis-writing/thesis/chapters/03_problem_definition_study_design.tex
thesis-writing/thesis/figures/clinicause_testbed_pipeline.pdf
thesis-writing/literature/metadata/references.bib
```

Do not edit abstracts yet unless a small temporary consistency fix is required for a successful build; full abstract alignment belongs to Step 4.

## Required conceptual changes

### A. Title

The working English title should be aligned with the paper, with thesis-specific detail only if it improves precision. Preferred form:

> **CliniCause: Constructing Clinically Grounded Observational Testbeds for Causal Analysis from Irregular ICU Time Series**

A scientifically equivalent Hebrew title must ultimately be provided. If Step 2 changes the English title but the Hebrew title requires careful final language review, record that as a mandatory Step 4 item rather than inventing a weak translation.

### B. Introduction order

The opening should move from:

```text
irregular ICU data -> integration challenge
```

to:

```text
causal-estimator evaluation problem
-> missing counterfactual answer
-> controlled benchmark spectrum
-> control/fidelity trade-off
-> representation-layer intervention
-> CliniCause instantiation on irregular ICU records
```

Irregularity remains important because it supplies realistic measurement, missingness, support, and care-process conditions; it no longer needs to carry the entire opening motivation.

### C. Contribution hierarchy

Chapter 1 must state:

1. primary: two clinically grounded observational causal-analysis testbeds and a general construction framework;
2. enabling: evidence-tracked integration, explicit interfaces, deterministic instantiation, and provenance;
3. empirical: converging-evidence evaluation and the finding that agreement can coexist with omitted-confounding fragility;
4. boundary: no known causal truth and no clinical validation.

### D. Main research question

Replace the current integration-first main question with a testbed-first question, for example:

> How can clinically grounded observational causal-analysis testbeds be constructed from source-observed irregular ICU records without generating exposures or outcomes, and what converging evidence can characterize their usefulness and limitations for evaluating causal estimators?

Retain the existing integration questions as secondary questions about how the testbeds are implemented and made auditable.

### E. Related work

Add a bounded section or subsection explaining the evaluation spectrum:

- fully synthetic;
- semi-synthetic;
- experimentally anchored or RCT-derived;
- empirically anchored;
- source-observed observational testbeds without known causal truth.

Use the paper’s cited examples and wording as a basis, but adapt them to thesis depth. Do not copy long paper passages verbatim. Explain the trade-off:

> greater experimental control makes accuracy measurable, while greater observational fidelity makes the causal target less knowable.

The thesis must present CliniCause as complementary, not superior in every respect.

### F. Formal resource framing

Chapter 3 should define each dataset-specific resource as a constructed analytical object that includes:

- record identifiers;
- source-observed irregular measurements as inputs;
- instantiated proxy exposures;
- source-observed mortality;
- observed covariates;
- project-specified DAG;
- exposure-specific adjustment sets;
- provenance.

Preserve the thesis’s existing data-contract detail. The new formalism should explain what the contracts construct.

### G. Pipeline figure

Copy:

```text
paper-aaai/figures/figure1_pipeline.pdf
```

to the thesis figure directory without changing the original. Insert it near the main contribution statement or resource-definition transition. The caption must explain:

- Design;
- Instantiate;
- Evaluate;
- schema-only LLM access;
- deterministic patient-level instantiation;
- converging-evidence evaluation.

Do not present the figure as proof of execution or clinical validity.

## Step 2 report

Create:

```text
thesis-writing/logs/testbed_story_alignment_step_2_intellectual_reframe.md
```

The report must contain:

- baseline commit and pre-existing worktree state;
- exact sources consulted;
- exact files changed;
- before/after contribution hierarchy;
- title decision;
- main and secondary research-question changes;
- citations added and bibliography changes;
- copied figure source and SHA-256 equality;
- protected paper-tree pre/post hash comparison;
- numerical/frozen-content comparison;
- build command and result;
- changed PDF page ranges;
- visual review notes for every changed page;
- unresolved Step 3/4 dependencies;
- readiness statement.

---

# Step 3 — Reframe construction and evaluation methodology

**Model:** GPT-5.6  
**Reasoning:** High  
**Primary scope:** Chapters 4–8, chapter transitions, deterministic shock example

## Objective

Preserve the detailed methods but make clear that they construct and evaluate the two observational testbeds.

## Expected files

Likely permitted files:

```text
thesis-writing/thesis/chapters/04_data_preprocessing.tex
thesis-writing/thesis/chapters/05_proxy_state_construction.tex
thesis-writing/thesis/chapters/06_predictive_modeling.tex
thesis-writing/thesis/chapters/07_causal_methodology.tex
thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex
thesis-writing/thesis/figures/clinicause_shock_proxy_example.png
```

Edits should concentrate on chapter openings, conceptual transitions, section framing, and the explanation of evaluation roles. Do not rewrite technical implementation that is already correct.

## Required changes

### A. Data and preprocessing

Frame preprocessing as preservation and normalization of source-observed processes for resource construction, not merely as a bridge between repositories.

Emphasize:

- records and mortality are not generated;
- MIMIC and PhysioNet remain separate;
- observed support, missingness, and measurement practices remain part of the resource;
- deterministic choices about cohorts and transformations are representation-layer interventions and must be explicit.

### B. Proxy construction

Explain the separation:

```text
schema and literature -> candidate representation
accepted definitions -> deterministic code
patient record -> instantiated proxy
```

Insert the paper’s shock figure by copying:

```text
paper-aaai/figures/figure3_shock_proxy_example.png
```

to the thesis figure directory without changing the source.

The accompanying prose must retain the important missingness interpretation:

- an unobserved clause does not fire;
- proxy value 0 means the implemented rule was not satisfied by observed evidence;
- 0 does not prove absence of the underlying clinical state.

### C. Predictive modeling

Reframe four-model prediction as **proxy recoverability**, one component of converging-evidence evaluation.

Retain:

- architecture detail;
- multi-label adaptation;
- splits and export contracts;
- dataset-specific model comparison.

Add the explicit boundary:

> recoverability shows that rule-derived constructs correspond to learnable patterns in the source time series; it does not validate the constructs clinically.

### D. Aggregation

Keep the five-source aggregate description, but do not allow aggregation to become the testbed’s defining scientific contribution. It is one implemented exposure interface used in the archived causal analyses.

Maintain:

- one rule-derived source;
- STraTS, GRU, GRU-D, and TCN binary sources;
- deterministic voting;
- cohort/schema alignment;
- no claim of clinical consensus or independent labels.

### E. Causal graph and estimation

Frame the DAG and adjustment sets as explicit representation-layer assumptions included in each testbed.

Maintain:

- project-specified, source-coded authority;
- not learned from the data;
- not validated edge by edge;
- exposure-specific adjustment;
- estimator hierarchy;
- intervention-definition limitations.

### F. Evaluation design

Chapter 8 should present a clear converging-evidence framework. It may be organized as:

1. construct plausibility;
2. proxy recoverability;
3. mortality-relevant information;
4. cross-estimator stability;
5. clinical-evidence corroboration;
6. permutation/disruption checks;
7. matching and empirical support;
8. omitted-variable sensitivity;
9. population perturbation and provenance.

Do not claim that all axes have equal evidential strength. State what each tests and what it cannot establish.

Clinical-evidence methodology may be introduced here using the finished paper and supplement, but the numerical comparisons belong in Step 4.

## Step 3 report

Create:

```text
thesis-writing/logs/testbed_story_alignment_step_3_methodology_reframe.md
```

Include all standard report fields plus:

- section-by-section method-role changes;
- exact shock-figure provenance and hash equality;
- list of technical paragraphs deliberately preserved;
- evaluation-axis coverage matrix before/after;
- confirmation that no proxy rule, threshold, DAG edge, adjustment set, model, estimator, or result changed;
- build and visual review results;
- protected paper hash comparison;
- readiness statement.

---

# Step 4 — Reframe evidence, discussion, conclusions, and front matter

**Model:** GPT-5.6  
**Reasoning:** Extra High  
**Primary scope:** Results, Discussion, Conclusions, abstracts, keywords, final title equivalence

## Objective

Make the empirical and concluding story answer the same question as the paper while retaining the thesis’s more detailed result and limitation hierarchy.

## Expected files

Likely permitted files:

```text
thesis-writing/thesis/chapters/10_results.tex
thesis-writing/thesis/chapters/11_discussion.tex
thesis-writing/thesis/chapters/12_conclusions_future_work.tex
thesis-writing/thesis/frontmatter/abstract_primary.tex
thesis-writing/thesis/frontmatter/abstract_secondary.tex
thesis-writing/thesis/frontmatter/keywords.tex
thesis-writing/thesis/frontmatter/administrative_metadata.tex
thesis-writing/literature/metadata/references.bib
```

A narrow edit to Chapter 8 is allowed only if required to match a newly added Results subsection.

## Required empirical hierarchy

The Results and Discussion should synthesize the evidence in this order:

1. **Resource construction**
   - two separate resources;
   - 26,845 MIMIC-III analysis records and nine exposures;
   - 7,993 PhysioNet analysis records and ten exposures;
   - no pooling.

2. **Construct plausibility**
   - informal consultation is limited evidence;
   - no formal ratings or chart adjudication.

3. **Proxy recoverability**
   - four model families;
   - archived dataset-specific performance;
   - STraTS leading MIMIC and GRU-D leading PhysioNet;
   - learnability, not validation.

4. **Mortality-relevant information**
   - include mortality-prediction results from the proxy representation only if Step 1 verifies the exact values and authoritative source;
   - distinguish rule-defined versus majority-vote representation exactly as supported;
   - prediction is not causal evidence.

5. **Cross-estimator stability**
   - DML sign agreement 19/19;
   - all-three sign agreement 18/19;
   - rank and magnitude agreement where supported;
   - agreement is not error against ground truth.

6. **Clinical-evidence corroboration**
   - add a concise thesis subsection and, if appropriate, a compact table based on the finished supplement;
   - report closest comparisons and major discrepancies symmetrically;
   - retain shock, respiratory, coagulation, neurologic, and metabolic discrepancies;
   - state differences in construct, severity, population, adjustment, and mortality horizon;
   - no study is a fully commensurate ground-truth effect for the CliniCause proxy.

7. **Permutation and support diagnostics**
   - retain their current bounded role.

8. **Omitted-variable sensitivity**
   - elevate the main paper conclusion:
     broad agreement can coexist with fragility to modest unobserved confounding;
   - explain why this is evidence for the diagnostic usefulness of an observational testbed;
   - do not turn sensitivity analysis into proof that an estimate is false or true.

9. **Central exception**
   - PhysioNet shock remains visible and is treated as a representation/estimator/support warning, not averaged away.

## Discussion hierarchy after revision

The Discussion must answer:

> What does CliniCause contribute as an observational testbed, and what can such a testbed reveal without known causal truth?

The answer should be:

- it preserves real observational processes;
- it makes representation choices explicit and replaceable;
- it exposes stable patterns, discrepancies, and sensitivity;
- it complements answer-key benchmarks;
- it does not score estimator accuracy against causal truth;
- it is useful for stress testing, diagnosis, and method comparison under realistic observational conditions.

The existing integration and provenance discussion remains as the explanation of why the testbeds are auditable.

## Conclusions hierarchy after revision

The first conclusion paragraph and “strongest contribution” statement must become testbed-first.

The closing perspective should state that:

- source-observed observational resources can add a different evaluation dimension from synthetic and semi-synthetic benchmarks;
- estimator agreement alone is insufficient;
- realistic sensitivity and disagreement are valuable findings;
- clinical validation, stronger causal designs, graph review, external cohorts, and complete provenance remain necessary.

The paper’s longer-term idea of expanding to additional held-out observational resources may be included as future work, but only as a proposal.

## Abstracts and title

The English and Hebrew abstracts must become scientifically equivalent and follow the paper-first hierarchy:

1. problem of causal-estimator evaluation;
2. CliniCause as complementary observational testbed construction;
3. schema-only LLM design and deterministic instantiation;
4. two resources and converging-evidence evaluation;
5. agreement plus fragility;
6. no causal ground truth or clinical validation.

The abstracts must remain citation-free and should not overfill with implementation detail.

Update keywords to include concepts such as:

- observational causal-analysis testbeds;
- causal estimator evaluation;
- representation-layer construction;
- causal machine learning;
- proxy exposures;
- irregular ICU time series;
- omitted-variable sensitivity.

Keep relevant existing keywords.

## Step 4 report

Create:

```text
thesis-writing/logs/testbed_story_alignment_step_4_evidence_synthesis.md
```

Include all standard fields plus:

- empirical-story before/after map;
- every newly added numerical claim with exact source;
- clinical-evidence source table and qualification;
- abstract equivalence check;
- title equivalence check;
- keyword changes;
- list of old integration-first phrases removed or subordinated;
- list of integration/provenance material preserved;
- numeric freeze comparison;
- citation and reference check;
- build and changed-page visual review;
- protected paper hash comparison;
- readiness statement.

---

# Step 5 — Independent thesis-wide audit and narrow repair

**Model:** GPT-5.6 in a new Codex thread  
**Reasoning:** Extra High  
**Primary scope:** independent review; only narrow repairs  
**Requirement:** the reviewing thread must not be the same thread that performed Steps 2–4

## Objective

Verify independently that the thesis now tells the paper’s main story without losing technical depth, introducing unsupported claims, altering frozen evidence, or modifying the paper.

## Mandatory independent checks

### A. Repository and scope

- identify the baseline before Step 2 and current HEAD/worktree;
- list all changed files;
- confirm no code or unrelated subtree changed;
- confirm all paper files are byte-identical to their pre-edit hashes;
- confirm `ignore-paper-aaai/` was untouched;
- confirm copied figures match their paper sources.

### B. Global story consistency

Read the rendered thesis and source, not only search results. Verify consistency across:

- English title;
- Hebrew title;
- English abstract;
- Hebrew abstract;
- Chapter 1 objective and research questions;
- Chapter 2 positioning;
- Chapter 3 resource contract;
- Chapters 4–8 method roles;
- Results synthesis;
- Discussion;
- Conclusions and future work;
- figure captions;
- keywords.

The primary contribution should be testbed construction everywhere. Integration must remain a major enabling contribution, not disappear.

### C. Claim safety

Search and inspect every use of:

```text
benchmark
testbed
ground truth
causal truth
validated
validation
clinical validation
causal effect
treatment effect
CATE
agreement
corroboration
recoverability
robust
sensitivity
LLM
expert
diagnosis
```

Verify the distinctions in Section 6 of this plan.

### D. Numerical freeze

Compare before/after:

- all integers;
- decimals;
- percentages;
- fractions;
- cohort counts;
- exposure counts;
- model counts;
- estimator counts;
- table values;
- figure filenames and captions;
- bibliography keys;
- labels and references.

Every changed number must be listed and justified by an authoritative source. Unexplained numerical drift is blocking.

### E. Figure audit

For each imported or replaced paper figure:

- exact source path;
- SHA-256 source and thesis copy;
- visible resolution;
- readable labels at thesis page size;
- no clipping;
- caption accuracy;
- first in-text reference before or near placement;
- list-of-figures entry;
- no duplicate figure with the same scientific purpose.

### F. Bibliography audit

- every citation key resolves;
- no duplicate bibliographic entries were introduced;
- final benchmark/testbed claims are supported;
- paper bibliography was not edited;
- raw URLs are avoided when a bibliography entry exists.

### G. Build and visual audit

Run a clean thesis build:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Then:

- inspect the build log for errors, missing references, missing citations, overfull boxes, and font problems;
- render every changed page individually at adequate resolution;
- inspect title pages, both abstracts, contents/list-of-figures changes, Chapters 1–3, imported figures, new clinical-evidence material, Discussion, Conclusions, bibliography, and Hebrew cover;
- use a contact sheet only for navigation, never as the sole visual review;
- keep temporary page renders outside tracked source unless explicitly needed.

### H. Narrow repair rule

Step 5 may edit only defects found by the audit. It must not perform another broad rewrite. Every repair must be mapped to an audit finding.

## Step 5 report

Create:

```text
thesis-writing/logs/testbed_story_alignment_step_5_independent_audit.md
```

Required final status:

```text
READY FOR AUTHOR REVIEW
```

or:

```text
BLOCKED — NARROW REPAIR REQUIRED
```

If blocked, list exact files and exact defects. Do not claim readiness conditionally.

---

## 8. Mandatory report template for every step

Every Codex step must save its report under `thesis-writing/logs/`. Reports are durable evidence for independent evaluation by ChatGPT and the author.

Each report must contain the following headings.

```markdown
# Testbed Story Alignment — Step N Report

## 1. Baseline
- current HEAD
- task baseline
- branch
- pre-existing dirty/untracked files
- local instructions read

## 2. Scope
- objective
- allowed files
- protected files
- files actually inspected

## 3. Source Authority
- finished-paper sources used
- thesis sources used
- numerical sources used
- superseded sources explicitly excluded

## 4. Work Performed
- exact conceptual changes
- exact file changes
- figures copied/replaced
- citations added/removed

## 5. Frozen-Content Verification
- numerical comparison
- proxy/model/estimator scope comparison
- label/reference comparison
- unexplained differences, if any

## 6. Paper Protection
- pre-edit hashes
- post-edit hashes
- changed protected-file count
- source/copy figure hash comparison

## 7. Validation
- commands
- build result
- warnings
- citation/reference result
- changed PDF pages
- visual inspection notes

## 8. Git Diff Summary
- git diff --stat
- changed file list
- unexpected changes
- diff-check result

## 9. Remaining Issues
- unresolved scientific issues
- unresolved layout issues
- items deferred to later steps

## 10. Readiness
READY FOR STEP N+1
```

Step 5 uses `READY FOR AUTHOR REVIEW` instead.

Reports must be specific enough that a reviewer can reproduce the checks. “Reviewed and looks good” is not sufficient.

---

## 9. Independent review gate after every step

Codex must stop after writing each report. It must not begin the next step automatically.

After each step, ChatGPT and the author will independently inspect:

1. repository status and the actual diff;
2. the report;
3. every changed source file;
4. protected-file hashes;
5. the rebuilt PDF;
6. the changed pages at readable resolution;
7. numerical and citation changes;
8. whether the new text follows this plan’s contribution hierarchy.

A Codex statement that a stage passed is not acceptance. Acceptance occurs only after the independent review.

The author or ChatGPT may request a narrow repair before authorizing the next prompt.

No step should be committed merely because Codex finished. Commit only after review, and only if the user explicitly requests or performs the commit. A recommended commit sequence is:

```text
thesis: audit testbed-story alignment
thesis: reframe contribution as observational testbeds
thesis: align construction and evaluation methodology
thesis: align evidence synthesis and conclusions
thesis: complete independent testbed-story audit
```

---

## 10. Protected-hash procedure

At the beginning and end of every editing step, record hashes for:

```text
thesis-writing/CausalDataGeneration.pdf
thesis-writing/aaai27-submission.tex
thesis-writing/supp.pdf
```

Also produce a deterministic paper-tree manifest, excluding no tracked scientific source:

```bash
find thesis-writing/paper-aaai -type f -print0 \
  | sort -z \
  | xargs -0 sha256sum \
  > /tmp/paper_aaai_hashes_before.txt
```

Repeat afterward and compare:

```bash
diff -u /tmp/paper_aaai_hashes_before.txt /tmp/paper_aaai_hashes_after.txt
```

Any paper-tree difference is blocking unless it is proven to be a pre-existing user change made outside the task. This mission never authorizes paper edits.

For copied figures, record both source and destination hashes:

```bash
sha256sum \
  thesis-writing/paper-aaai/figures/figure1_pipeline.pdf \
  thesis-writing/thesis/figures/clinicause_testbed_pipeline.pdf

sha256sum \
  thesis-writing/paper-aaai/figures/figure3_shock_proxy_example.png \
  thesis-writing/thesis/figures/clinicause_shock_proxy_example.png
```

The corresponding pairs must match exactly unless a later human-approved thesis-specific regeneration is explicitly authorized.

---

## 11. Git and worktree discipline

At the beginning of every prompt:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git log -10 --oneline
```

Do not:

```bash
git reset --hard
git clean -fd
git add .
git add -A
git commit
git push
```

unless the prompt explicitly authorizes the operation.

Preserve pre-existing dirty files. Do not normalize unrelated line endings or rebuild unrelated PDFs.

At the end:

```bash
git diff --check
git diff --stat
git diff --name-only
git status --short
```

The report must distinguish:

- files changed by the current step;
- pre-existing changes;
- generated build artifacts;
- unexpected changes.

---

## 12. Quality criteria for the completed thesis

The mission is complete only when all of the following are true.

### Story

- The title is testbed-centered.
- The abstract begins from causal-estimator evaluation, not only irregular ICU integration.
- Chapter 1 explains the answer-key versus observational-fidelity trade-off.
- Representation-layer intervention is explicit.
- The main research question is testbed-first.
- Integration and evidence tracking are enabling contributions.
- Results are organized as converging evidence.
- Agreement plus omitted-confounding fragility is a central finding.
- Discussion positions CliniCause as complementary to controlled benchmarks.
- Conclusion states the diagnostic value and the absence of known causal truth.

### Scientific safety

- No causal ground truth is claimed.
- No proxy is upgraded to a diagnosis.
- No graph is described as learned or validated.
- No clinical-literature comparison is described as calibration against truth.
- No estimator agreement is described as accuracy.
- No sensitivity result is overstated.
- PhysioNet shock remains visible.
- Dataset results remain separate and unpooled.
- Estimator hierarchy remains unchanged.
- Provenance limitations remain explicit.

### Preservation

- Existing detailed methods remain.
- Existing data-contract explanations remain.
- Existing implementation and artifact distinctions remain.
- Existing limitations remain or become stronger.
- Existing checked numbers remain frozen.
- The paper and its Overleaf copy remain unchanged.

### Figures

- The pipeline figure is added.
- The shock-proxy figure is added.
- No redundant DAG or agreement figure is introduced.
- All imported figures are readable and correctly captioned.

### Validation

- Clean XeLaTeX/biber build passes.
- No missing citations or references.
- Changed pages are inspected at readable resolution.
- Hebrew and English front matter are scientifically equivalent.
- All five reports exist.
- Step 5 concludes `READY FOR AUTHOR REVIEW`.

---

## 13. Decision rule when the paper and thesis differ

The paper controls the **main scientific story**. The thesis controls the **level of detail and evidence qualification**.

Therefore:

- adopt the paper’s testbed-construction hierarchy;
- retain the thesis’s more conservative estimator hierarchy where it is better supported;
- retain the thesis’s detailed provenance boundaries;
- retain the thesis’s implementation specifics;
- do not weaken the thesis to imitate conference brevity;
- do not import paper wording that is less qualified than the thesis evidence permits;
- do not import a paper claim without verifying its exact source;
- do not make the thesis identical to the paper in structure or length.

The goal is not a long version of the paper. The goal is a detailed thesis whose central intellectual proposition is the same as the finished paper.

---

## 14. Final handoff

After this plan is placed at:

```text
thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md
```

the next action is to prepare **Step 1 only** as a read-only Codex prompt using GPT-5.6 with Extra High reasoning.

No thesis prose should be edited until the Step 1 report has been independently reviewed and approved.

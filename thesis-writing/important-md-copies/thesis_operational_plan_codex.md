# CliniCause Thesis Writing with Codex — Complete Operational Plan

## 1. Purpose of This Plan

This document explains the complete workflow for writing the CliniCause thesis with Codex while working inside the `CliniCause` repository.

The central idea is simple: **Codex should not start by writing the thesis**. It should first understand the repository, validate the available evidence, organize the literature, map the Ben-Gurion University thesis template, and only then write the thesis section by section.

The thesis must be built from verified sources only:

- repository code;
- experiment configurations;
- stored results;
- generated figures and tables;
- curated literature;
- approved thesis template requirements;
- advisor-approved assumptions;
- explicitly marked unresolved gaps.

The workflow is designed to prevent three common failures in AI-assisted academic writing:

1. **invented results** — writing numbers, claims, or findings that are not present in the repository;
2. **unsupported citations** — citing papers for claims they do not support;
3. **overclaiming** — especially around clinical meaning and causal interpretation.

The plan therefore treats the thesis as an evidence-driven engineering artifact, not as a free-form writing task.

---

## 2. Guiding Principles

### 2.1 Repository First

The repository is the primary source of truth. Codex should inspect code, notebooks, scripts, outputs, plots, tables, metadata, and LaTeX files before writing or editing any thesis text.

### 2.2 Inspect Before Editing

Every Codex task must begin with inspection. A good Codex task should specify:

- what Codex may inspect;
- what Codex may edit;
- what Codex must not change;
- what output is expected;
- how the output should be validated.

### 2.3 No Invented Evidence

Codex must not invent:

- numerical results;
- experiment outcomes;
- model performance values;
- clinical interpretations;
- treatment effects;
- sensitivity-analysis conclusions;
- citations;
- figure or table descriptions.

If something is missing, Codex should write a visible placeholder such as:

```text
[NEEDS RESULT]
[NEEDS EVIDENCE]
[NEEDS CITATION]
[ADVISOR CHECK]
[VALIDATION REQUIRED]
```

### 2.4 Separate Facts from Interpretation

The thesis should distinguish clearly between:

- what was implemented;
- what was executed;
- what results were observed;
- what can be concluded;
- what remains uncertain;
- what is future work.

This is especially important for the causal-inference parts of the thesis.

### 2.5 Causal Language Must Be Conservative

The thesis must not imply causality merely because a causal estimator was used. Causal claims require explicit assumptions, including treatment definition, outcome definition, confounder set, adjustment logic, overlap/positivity, and sensitivity to unmeasured confounding.

The thesis should distinguish:

- prediction;
- association;
- adjustment;
- CATE estimation;
- clinical interpretation;
- clinical actionability.

### 2.6 Write Incrementally

The thesis should be written in small, reviewable units. Codex should not be asked to write the full thesis in one prompt.

A safe writing loop is:

```text
inspect → plan → draft → validate → report gaps → human review → revise
```

---

## 3. Expected Repository Context

The work should be performed from the root of the repository:

```text
CliniCause/
```

Do not open only:

```text
CliniCause/thesis-writing/
```

Codex needs access to both the thesis material and the research pipeline, including code and outputs.

A useful thesis-working structure is:

```text
thesis-writing/
├── THESIS_PLAN.md
├── literature/
│   ├── README.md
│   ├── papers/
│   ├── optional/
│   └── metadata/
│       ├── references.bib
│       ├── catalog.csv
│       └── checksums.sha256
├── audit/
├── planning/
├── thesis/
├── figures/
├── tables/
├── prompts/
└── logs/
```

The exact names may change if the repository already has a better structure, but the functions should remain:

- `literature/` — curated papers, metadata, BibTeX, optional/background sources;
- `audit/` — repository maps, result inventories, claim ledgers;
- `planning/` — thesis outline, chapter maps, terminology, figure/table plans;
- `thesis/` — actual LaTeX source;
- `figures/` — approved thesis figures or links to source figures;
- `tables/` — approved thesis tables or links to generated tables;
- `prompts/` — prompts used for each Codex stage;
- `logs/` — validation notes, unresolved questions, advisor feedback.

---

## 4. Stage Overview

The full workflow is divided into six major stages:

| Stage | Name | Main Question | Main Output |
|---|---|---|---|
| 0 | Environment and workspace preparation | Can Codex safely work in this repo? | validated VS Code/WSL/LaTeX/Codex setup |
| 1 | Literature corpus construction and validation | Which papers belong in the thesis evidence base? | curated literature matrix and BibTeX status |
| 2 | Repository and evidence audit | What was actually implemented, executed, and produced? | repository map and evidence inventory |
| 3 | Thesis structure and construction plan | What should the thesis structure be? | approved outline and chapter evidence map |
| 4 | Incremental thesis writing | How do we draft safely from evidence? | chapter and section drafts |
| 5 | Final validation and thesis hardening | Is the thesis correct, traceable, and compilable? | final checked thesis and advisor-ready package |

Each stage should end with a human approval checkpoint before moving to the next one.

---

# Stage 0 — Environment and Workspace Preparation

## Objective

Prepare a reproducible VS Code workspace for repository inspection, Python work, LaTeX editing, literature validation, and Codex-assisted thesis writing.

This stage does not write thesis content.

## 0.1 Open the Correct Workspace

Open the repository root:

```text
CliniCause/
```

Codex should be able to see:

- source code;
- notebooks;
- results;
- figures;
- thesis files;
- literature files;
- metadata files.

## 0.2 Required VS Code Extensions

Install at least:

```text
openai.chatgpt
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
james-yu.latex-workshop
```

Recommended full set:

```text
openai.chatgpt
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
james-yu.latex-workshop
eamodio.gitlens
mechatroner.rainbow-csv
redhat.vscode-yaml
DavidAnson.vscode-markdownlint
charliermarsh.ruff
```

If working through WSL, also install:

```text
ms-vscode-remote.remote-wsl
```

## 0.3 External Tools

The following command-line tools should be available:

```bash
git
python
latexmk
pdflatex
biber
```

A LaTeX distribution is required:

- Windows: MiKTeX or TeX Live;
- Linux/WSL: TeX Live;
- macOS: MacTeX.

## 0.4 Validation Commands

Run from the repository root:

```bash
git rev-parse --show-toplevel
git status --short
python --version
code --version
code --list-extensions --show-versions
latexmk --version
pdflatex --version
biber --version
```

If working inside WSL, also check:

```bash
pwd
uname -a
```

A good WSL path looks like:

```text
/home/<user>/projects/CliniCause
```

Avoid working directly inside:

```text
/mnt/c/Users/...
```

## 0.5 Recommended `.vscode/extensions.json`

Create:

```text
.vscode/extensions.json
```

Suggested contents:

```json
{
  "recommendations": [
    "openai.chatgpt",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "james-yu.latex-workshop",
    "eamodio.gitlens",
    "mechatroner.rainbow-csv",
    "redhat.vscode-yaml",
    "davidanson.vscode-markdownlint",
    "charliermarsh.ruff"
  ]
}
```

If WSL is used, add:

```json
"ms-vscode-remote.remote-wsl"
```

## 0.6 Stage 0 Deliverables

Codex should produce or update:

```text
docs/thesis/environment_setup.md
docs/thesis/thesis_workflow.md
docs/thesis/repo_map.md
AGENTS.md                 # only if useful and kept minimal
.vscode/extensions.json   # only with approval
```

## 0.7 Minimal `AGENTS.md` Policy

If an `AGENTS.md` file is created, it should be short. It should include only stable instructions:

- how to compile or validate the thesis;
- where thesis files live;
- where literature metadata lives;
- evidence policy;
- citation policy;
- no invented results;
- no unsupported causal claims;
- preserve LaTeX labels and citation keys;
- do not commit or push unless explicitly instructed.

It should not contain a long thesis summary.

## 0.8 Stage 0 Completion Checklist

- [ ] Repository root opens correctly in VS Code
- [ ] Codex is installed and signed in
- [ ] Python and Pylance are installed
- [ ] Jupyter is installed and detects the project environment
- [ ] LaTeX Workshop is installed
- [ ] A TeX distribution is installed
- [ ] Git is available
- [ ] LaTeX commands are available
- [ ] Recommended optional extensions are reviewed
- [ ] No conflicting formatters or AI writing extensions are active
- [ ] `.vscode/extensions.json` is created or approved
- [ ] Codex can inspect the repo without editing

## 0.9 First Codex Prompt for Stage 0

```text
Stage 0 — Thesis workflow setup.

Goal:
Create minimal repository instructions for using Codex to help write this thesis from a code+results repository.

Important:
Do not write thesis content yet.
Do not modify code.
Do not invent results, citations, or claims.
Do not commit or push changes.

Tasks:
1. Inspect the repository structure.
2. Identify where the thesis template/main LaTeX files are.
3. Identify where code, results, plots, tables, papers, and bibliography files are.
4. Identify the likely thesis compile command, but do not assume it works unless you verify it.
5. Create or update:
   - docs/thesis/environment_setup.md
   - docs/thesis/thesis_workflow.md
   - docs/thesis/repo_map.md
6. If appropriate, create a minimal AGENTS.md at the repository root.

Rules for AGENTS.md:
- Keep it short.
- Include only stable rules:
  - compile/check commands
  - repository structure
  - evidence policy
  - citation policy
  - no invented results
  - no unsupported causal claims
  - preserve LaTeX labels and bibliography keys
- Do not include a huge thesis summary.

Evidence policy:
Every thesis claim must be supported by one of:
- repository code
- result file
- figure/table
- paper/citation
- advisor-approved assumption

If support is missing, mark it as:
[NEEDS EVIDENCE]
[NEEDS CITATION]
[ADVISOR CHECK]

Output:
After editing, report:
1. Files changed.
2. What you inferred from the repository.
3. The compile command you recommend.
4. Open issues before moving to Stage 1.
```

---

# Stage 1 — Literature Corpus Construction and Validation

## Objective

Build a compact, thesis-specific literature corpus in which every paper has a clear role.

The literature corpus is not the Related Work chapter. It is the evidence base that will later support the Background, Related Work, Methodology, and Discussion chapters.

## 1.1 Literature Scope

The corpus should cover the following areas.

### Implemented Time-Series Models

- STraTS;
- TCN;
- InterpNet;
- SAnD;
- GRU;
- GRU-D.

### Causal Estimation

- generalized random forests;
- causal forests;
- double/debiased machine learning;
- EconML-related estimators;
- heterogeneous treatment-effect estimation.

### Data and Benchmarks

- MIMIC-III;
- PhysioNet Challenge 2012;
- clinical time-series benchmarks;
- ICU EHR modeling.

### Causal Identification

- causal diagrams;
- backdoor adjustment;
- target-trial emulation;
- overlap and positivity;
- sensitivity to unmeasured confounding;
- well-defined interventions.

### Clinical and Labeling Context

- clinical proxy states;
- proxy phenotypes;
- weak supervision;
- rule-based phenotyping;
- limitations of unvalidated clinical proxies.

## 1.2 Literature Corpus Structure

Recommended structure:

```text
thesis-writing/literature/
├── README.md
├── papers/
├── optional/
└── metadata/
    ├── references.bib
    ├── catalog.csv
    └── checksums.sha256
```

## 1.3 Literature Roles

Each paper should be classified as one of:

- **core method** — directly explains a method used in the thesis;
- **data/benchmark** — explains the dataset or benchmark setup;
- **causal foundation** — supports identification or estimation logic;
- **clinical context** — supports clinical proxy definitions or interpretation;
- **related work** — useful comparison but not central;
- **optional/background** — retained but not required for the main thesis argument;
- **remove candidate** — duplicate, weakly related, or unsupported.

## 1.4 Stage 1 Deliverables

Codex should produce:

```text
thesis-writing/literature/README.md
thesis-writing/literature/metadata/catalog.csv
thesis-writing/literature/metadata/references.bib
thesis-writing/literature/metadata/checksums.sha256
thesis-writing/literature/literature_matrix.md
thesis-writing/literature/literature_gaps.md
thesis-writing/literature/candidate_additions.md
thesis-writing/literature/candidate_removals.md
```

If BibTeX changes are risky, candidate additions should be written to a separate file first, not directly inserted into the main bibliography.

## 1.5 Stage 1 Completion Checklist

- [ ] Every core paper has a clear thesis role
- [ ] Every implemented model has a primary citation
- [ ] Every causal estimator has a primary citation
- [ ] Data/benchmark papers are present
- [ ] Clinical proxy/phenotyping literature is present
- [ ] BibTeX keys are unique
- [ ] PDF paths in `catalog.csv` are valid
- [ ] Duplicate papers are resolved
- [ ] Missing PDFs are listed
- [ ] Optional papers are separated from core papers
- [ ] No paper is cited for a method that was not implemented

## 1.6 Codex Prompt for Stage 1

```text
Stage 1 — Literature corpus validation.

Goal:
Validate and organize the thesis literature corpus.

Allowed scope:
- thesis-writing/literature/
- bibliography files
- literature metadata files
- existing paper PDFs

Forbidden scope:
- Do not edit model code.
- Do not edit thesis prose.
- Do not delete papers unless explicitly instructed.
- Do not invent paper metadata.
- Do not add citations directly to the thesis.
- Do not commit or push changes.

Tasks:
1. Inspect the existing literature directory.
2. Build a literature matrix listing citation key, title, year, venue, role, local PDF status, and thesis relevance.
3. Classify papers as core, supporting, optional/background, duplicate, or removal candidate.
4. Identify missing papers required by implemented methods.
5. Identify papers that appear weakly related or redundant.
6. Check for duplicate titles, duplicate DOIs, missing PDFs, missing BibTeX fields, and broken PDF paths.
7. Produce a concise literature gap report.

Deliverables:
- literature_matrix.md
- literature_gaps.md
- candidate_additions.md
- candidate_removals.md

Validation:
- Do not claim that a paper supports a method unless the connection is clear.
- Mark uncertain entries as [VERIFY].
- Report all unresolved questions.
```

---

# Stage 2 — Repository and Evidence Audit

## Objective

Create a factual map of the research project before writing thesis prose.

This is one of the most important stages. It prevents Codex from writing an elegant thesis that is disconnected from the actual repository.

## 2.1 What Codex Should Audit

Codex should inspect and document:

- repository structure;
- datasets and data assumptions;
- preprocessing pipeline;
- cohort construction;
- time-series representation;
- predictive models;
- clinical proxy-state construction;
- causal estimators;
- sensitivity analysis;
- overlap analysis;
- experiments;
- generated outputs;
- figures;
- tables;
- missing evidence;
- inconsistencies;
- obsolete or archived artifacts.

## 2.2 Required Audit Categories

### Repository Structure

Identify:

- main source directories;
- scripts;
- notebooks;
- configuration files;
- experiment directories;
- output directories;
- model checkpoints;
- figure directories;
- LaTeX files;
- archived or obsolete files.

### Data Provenance

Document:

- source datasets;
- data access assumptions;
- preprocessing pipelines;
- filtering criteria;
- inclusion/exclusion rules;
- variable definitions;
- missing-data handling;
- train/validation/test splits;
- leakage protections.

### Predictive Modeling

For each model, document:

- implementation file;
- input format;
- output;
- training objective;
- hyperparameters;
- missingness handling;
- evaluation metrics;
- executed experiments;
- stored results.

### Clinical Proxy-State Construction

Document:

- definitions of proxy states such as Shock, Respiratory Failure, Renal Failure, or other states;
- variables and thresholds used;
- temporal windows;
- aggregation logic;
- clinical rationale;
- validation status;
- why these are proxies rather than verified diagnoses.

### Causal Analysis

Document:

- treatment/exposure definition;
- outcome definition;
- confounder set;
- adjustment strategy;
- DAG assumptions;
- estimator choice;
- nuisance models;
- cross-fitting;
- treatment-effect target;
- subgroup or heterogeneous-effect analysis;
- uncertainty estimates;
- overlap diagnostics;
- sensitivity analysis.

### Experimental Evidence

Classify each result into one of:

1. implemented and executed;
2. implemented but not clearly executed;
3. described but not implemented;
4. result present but provenance unclear;
5. expected but missing.

## 2.3 Stage 2 Deliverables

Recommended outputs:

```text
thesis-writing/audit/
├── repository_map.md
├── evidence_inventory.md
├── experiment_inventory.csv
├── figure_table_inventory.md
├── terminology_map.md
├── unresolved_questions.md
└── claim_evidence_ledger.csv
```

## 2.4 Claim-Evidence Ledger

The claim-evidence ledger is the backbone of the thesis.

Suggested fields:

```text
claim_id
chapter_or_section
claim
claim_type
repository_source
result_source
figure_or_table
literature_source
status
risk_level
notes
```

Claim types may include:

- implementation claim;
- data claim;
- numerical result claim;
- methodological claim;
- causal claim;
- clinical interpretation;
- limitation;
- future work.

Risk levels may include:

- low — directly supported by code or results;
- medium — supported but requires careful wording;
- high — causal or clinical claim requiring assumptions;
- blocked — missing evidence.

## 2.5 Stage 2 Completion Checklist

- [ ] Repository map completed
- [ ] Data pipeline documented
- [ ] All implemented models documented
- [ ] All executed experiments identified
- [ ] All available results inventoried
- [ ] Proxy-state definitions documented
- [ ] Causal estimands and estimators documented
- [ ] Sensitivity and overlap workflows documented
- [ ] Figures and tables mapped to source files
- [ ] Missing and contradictory evidence listed
- [ ] Claim-to-evidence ledger started

## 2.6 Codex Prompt for Stage 2

```text
Stage 2 — Repository and evidence audit.

Goal:
Create a factual evidence map of the repository before thesis writing begins.

Allowed scope:
- Inspect the full repository.
- Write audit files under thesis-writing/audit/.

Forbidden scope:
- Do not edit code.
- Do not edit data.
- Do not rerun expensive experiments.
- Do not write thesis prose.
- Do not modify existing results.
- Do not commit or push changes.

Required procedure:
1. Inspect the repository structure.
2. Identify code, notebooks, configs, data-processing scripts, results, figures, tables, and thesis files.
3. Distinguish implemented workflows from executed workflows.
4. Map each available result to its apparent source.
5. Identify missing, ambiguous, duplicated, or obsolete evidence.
6. Start a claim-evidence ledger.
7. Record uncertainty explicitly.

Deliverables:
- thesis-writing/audit/repository_map.md
- thesis-writing/audit/evidence_inventory.md
- thesis-writing/audit/experiment_inventory.csv
- thesis-writing/audit/figure_table_inventory.md
- thesis-writing/audit/terminology_map.md
- thesis-writing/audit/unresolved_questions.md
- thesis-writing/audit/claim_evidence_ledger.csv

Validation:
- Do not infer that a script was executed merely because it exists.
- Do not infer that a result is final unless there is evidence.
- Mark uncertain items as [UNCLEAR].

Report:
At the end, summarize files inspected, files created/changed, key findings, and open questions.
```

---

# Stage 3 — Thesis Structure and Construction Plan

## Objective

Design the thesis structure around the actual research contribution, available evidence, and Ben-Gurion University engineering thesis requirements.

This stage defines what the thesis will say, but still does not draft full prose.

## 3.1 Proposed High-Level Thesis Structure

### Front Matter

- title page;
- approval pages;
- acknowledgments;
- abstract;
- Hebrew abstract, if required;
- table of contents;
- list of figures;
- list of tables;
- list of abbreviations.

### Chapter 1 — Introduction

- clinical and methodological motivation;
- problem statement;
- research gap;
- thesis objectives;
- contributions;
- chapter overview.

### Chapter 2 — Background and Related Work

- irregular clinical time-series modeling;
- missingness-aware modeling;
- clinical proxy phenotyping;
- causal inference from observational ICU data;
- heterogeneous treatment effects;
- sensitivity and overlap;
- relationship between prior work and the present study.

### Chapter 3 — Problem Formulation

- notation;
- data structure;
- prediction tasks;
- proxy-state definitions;
- exposure and outcome definitions;
- causal estimand;
- assumptions.

### Chapter 4 — Data and Preprocessing

- datasets;
- cohort construction;
- variables;
- preprocessing;
- temporal representation;
- missing-data handling;
- splitting and leakage prevention.

### Chapter 5 — Predictive Modeling

- baselines;
- STraTS;
- TCN;
- InterpNet;
- SAnD;
- GRU;
- GRU-D;
- training protocol;
- evaluation metrics.

### Chapter 6 — Clinical Proxy-State Construction

- clinical rationale;
- operational definitions;
- temporal logic;
- implementation;
- limitations and validation status.

### Chapter 7 — Causal-Inference Methodology

- causal graph and assumptions;
- treatment/exposure definition;
- confounder selection;
- DML;
- causal forests;
- nuisance estimation;
- uncertainty;
- heterogeneous effects;
- overlap;
- sensitivity analysis.

### Chapter 8 — Experimental Design

- research questions;
- experimental matrix;
- hyperparameters;
- computational setup;
- evaluation procedure;
- statistical testing;
- ablations and robustness checks.

### Chapter 9 — Results

- predictive performance;
- proxy-state characteristics;
- causal-effect estimates;
- heterogeneity;
- overlap diagnostics;
- sensitivity analysis;
- key figures and tables.

### Chapter 10 — Discussion

- interpretation;
- relationship to prior work;
- clinical meaning;
- methodological implications;
- limitations;
- threats to validity;
- generalizability;
- ethical considerations.

### Chapter 11 — Conclusion and Future Work

- summary of findings;
- main contributions;
- practical implications;
- recommended future research.

### Back Matter

- references;
- appendices;
- supplementary methods;
- additional figures and tables;
- configuration and reproducibility details.

## 3.2 Section Planning Requirements

Before drafting each section, define:

- purpose;
- key claims;
- repository evidence;
- citations;
- figures;
- tables;
- unresolved questions;
- maximum scope;
- dependencies on other sections.

## 3.3 Stage 3 Deliverables

Recommended outputs:

```text
thesis-writing/planning/
├── thesis_outline.md
├── chapter_evidence_map.md
├── figure_plan.md
├── table_plan.md
├── citation_plan.md
├── terminology_and_notation.md
└── writing_order.md
```

## 3.4 Stage 3 Completion Checklist

- [ ] BGU template requirements reviewed
- [ ] Final chapter outline approved
- [ ] Every chapter mapped to repository evidence
- [ ] Every planned figure mapped to a source
- [ ] Every planned table mapped to a source
- [ ] Literature assigned to relevant sections
- [ ] Terminology standardized
- [ ] Notation standardized
- [ ] Unsupported planned claims removed
- [ ] Writing order approved

## 3.5 Codex Prompt for Stage 3

```text
Stage 3 — Thesis structure and construction plan.

Goal:
Create a detailed thesis outline and construction plan based on the BGU template, repository evidence, and validated literature corpus.

Allowed scope:
- thesis-writing/audit/
- thesis-writing/literature/
- thesis-writing/planning/
- thesis LaTeX template files, read-only unless explicitly approved

Forbidden scope:
- Do not write full thesis prose.
- Do not modify code.
- Do not modify results.
- Do not invent claims.
- Do not commit or push changes.

Tasks:
1. Inspect the BGU thesis template and existing thesis files.
2. Inspect the audit outputs and literature matrix.
3. Propose a detailed chapter and section outline.
4. Map each planned section to evidence, citations, figures, and tables.
5. Identify unsupported or risky planned claims.
6. Define terminology and notation conventions.
7. Recommend a writing order.

Deliverables:
- thesis-writing/planning/thesis_outline.md
- thesis-writing/planning/chapter_evidence_map.md
- thesis-writing/planning/figure_plan.md
- thesis-writing/planning/table_plan.md
- thesis-writing/planning/citation_plan.md
- thesis-writing/planning/terminology_and_notation.md
- thesis-writing/planning/writing_order.md

Validation:
- Every planned chapter must have evidence or a clear purpose.
- Every planned causal claim must include assumptions or be marked [ADVISOR CHECK].
- Unsupported planned claims should be removed or marked explicitly.
```

---

# Stage 4 — Incremental Thesis Writing

## Objective

Draft the thesis in controlled, reviewable sections using only approved evidence.

This is the first stage where Codex writes thesis prose.

## 4.1 Recommended Writing Order

Do not start with the Introduction. The Introduction should reflect the actual methods and results, so it should be written later.

Recommended order:

1. Data and preprocessing;
2. Predictive modeling;
3. Clinical proxy-state construction;
4. Causal-inference methodology;
5. Experimental design;
6. Results;
7. Discussion and limitations;
8. Related work;
9. Introduction and contributions;
10. Conclusion;
11. Abstracts;
12. Appendices.

## 4.2 Prompt Structure for Every Writing Task

Each writing prompt should include:

### Context

Explain where Codex is operating and what has already been approved.

### Objective

State exactly which section should be drafted or revised.

### Allowed Scope

List files Codex may inspect and edit.

### Forbidden Scope

List files and actions that are not allowed.

### Evidence

List approved:

- repository files;
- result files;
- figures;
- tables;
- literature entries;
- prior planning documents.

### Restrictions

Include rules such as:

- no invented values;
- no new experiments;
- no unsupported clinical claims;
- no unsupported causal language;
- no citations outside the approved literature corpus;
- preserve LaTeX labels and citation keys.

### Required Output

Codex should produce:

- complete section draft;
- list of cited sources;
- list of repository evidence used;
- list of unresolved placeholders;
- self-check against the prompt.

## 4.3 Drafting Convention

When evidence is missing, use explicit placeholders:

```text
[RESULT REQUIRED]
[CITATION REQUIRED]
[FIGURE REQUIRED]
[VALIDATION REQUIRED]
[SUPERVISOR DECISION REQUIRED]
```

Do not hide missing evidence with vague language.

## 4.4 Chapter-Level Review

After every chapter, Codex should verify:

- citations;
- numerical values;
- terminology;
- notation;
- figure references;
- table references;
- consistency with earlier chapters;
- unresolved placeholders.

## 4.5 Stage 4 Completion Checklist

- [ ] Methods chapters drafted
- [ ] Experimental design drafted
- [ ] Results drafted from verified outputs
- [ ] Discussion separates evidence from interpretation
- [ ] Related work uses only approved literature
- [ ] Introduction reflects actual contributions
- [ ] Conclusion does not introduce new claims
- [ ] Abstract matches final thesis
- [ ] Placeholders are tracked centrally
- [ ] Supervisor feedback is incorporated through explicit revisions

## 4.6 Generic Codex Prompt for a Thesis Section

```text
Stage 4 — Incremental thesis writing.

Section:
[Specify exact chapter/section/subsection]

Goal:
Draft or revise only this section using approved evidence.

Allowed scope:
- [List files Codex may inspect]
- [List files Codex may edit]

Forbidden scope:
- Do not edit code.
- Do not edit results.
- Do not add new experiments.
- Do not edit unrelated thesis sections.
- Do not add citations outside the approved bibliography without marking them as [CITATION REQUIRED].
- Do not commit or push changes.

Evidence to use:
- [Approved audit files]
- [Approved result files]
- [Approved figures/tables]
- [Approved literature keys]

Writing rules:
- Use precise academic English.
- Do not invent numerical values.
- Do not overclaim causality.
- Distinguish prediction, association, causal estimation, and clinical interpretation.
- Use placeholders for missing evidence.
- Preserve LaTeX labels and citation keys.

Deliverable:
- A complete draft of the requested section.
- A short evidence report listing which files, figures, tables, and citations support the section.
- A list of unresolved placeholders or advisor questions.

Validation:
- Re-read the edited section.
- Check terminology and notation consistency.
- Check that every technical claim is supported or explicitly marked.
- If possible, compile the thesis or relevant LaTeX target.
```

---

# Stage 5 — Final Validation and Thesis Hardening

## Objective

Validate the complete thesis for factual accuracy, reproducibility, formatting, citation integrity, and internal consistency.

## 5.1 Claim Validation

For every major claim, verify:

- supporting repository evidence;
- supporting citation;
- numerical consistency;
- wording strength;
- causal interpretation;
- clinical interpretation.

Maintain or complete the claim ledger:

```text
claim_id
chapter
claim
claim_type
repository_source
literature_source
validation_status
notes
```

## 5.2 Numerical Validation

Check:

- sample sizes;
- cohort counts;
- split sizes;
- metric values;
- confidence intervals;
- treatment-effect estimates;
- sensitivity values;
- figure labels;
- table values;
- units;
- rounding.

The same result must not appear differently in different chapters.

## 5.3 Citation Validation

Check:

- every citation key exists;
- every cited source appears in the bibliography;
- every bibliography entry is cited or intentionally retained;
- duplicate entries are resolved;
- titles, authors, venues, years, and DOIs are correct;
- optional literature is not presented as a primary methodological basis;
- preprints and final publications are clearly distinguished.

## 5.4 Figure and Table Validation

For every figure and table, check:

- source file;
- generation script or notebook;
- data provenance;
- caption accuracy;
- labels and units;
- references in text;
- consistent numbering;
- readability;
- no unsupported interpretation in captions.

## 5.5 Terminology Validation

Standardize terms such as:

- proxy state;
- proxy phenotype;
- clinically inspired proxy label;
- treatment;
- exposure;
- outcome;
- confounder;
- causal effect;
- association;
- heterogeneous treatment effect;
- sensitivity analysis;
- robustness value;
- overlap;
- positivity.

Avoid describing proxy labels as verified diagnoses unless separately validated.

## 5.6 Causal-Language Validation

Confirm that the thesis does not:

- claim causality without assumptions;
- imply that a derived clinical state is necessarily manipulable;
- ignore unmeasured confounding;
- ignore overlap violations;
- interpret heterogeneous effects beyond supported subgroups;
- confuse prediction with causal estimation.

## 5.7 Reproducibility Validation

Confirm that:

- code paths exist;
- configurations are identifiable;
- environments are documented;
- random seeds are documented where available;
- result provenance is recorded;
- thesis figures and tables can be regenerated or traced;
- external data access requirements are explained.

## 5.8 LaTeX and Formatting Validation

Run the approved compile command, usually involving:

```bash
latexmk
biber
```

Resolve:

- compilation errors;
- undefined references;
- missing citations;
- overfull boxes;
- duplicate labels;
- broken figure paths;
- incorrect table placement;
- inconsistent capitalization;
- page-numbering issues;
- front-matter requirements.

## 5.9 Stage 5 Deliverables

Recommended outputs:

```text
thesis-writing/logs/final_validation_report.md
thesis-writing/logs/citation_validation_report.md
thesis-writing/logs/figure_table_validation_report.md
thesis-writing/logs/unresolved_final_placeholders.md
thesis-writing/logs/advisor_review_packet.md
```

The final advisor review packet should include:

- what changed;
- what still needs review;
- which claims are sensitive;
- which figures/tables need approval;
- which assumptions require advisor confirmation.

## 5.10 Stage 5 Completion Checklist

- [ ] All major claims validated
- [ ] All numerical values cross-checked
- [ ] All citations compile
- [ ] All figures and tables have provenance
- [ ] Terminology is consistent
- [ ] Causal language is appropriately qualified
- [ ] Clinical claims are appropriately limited
- [ ] Reproducibility details are documented
- [ ] LaTeX compiles cleanly
- [ ] BGU formatting requirements are satisfied
- [ ] Final placeholders are resolved or explicitly documented
- [ ] Final supervisor review completed

## 5.11 Codex Prompt for Stage 5

```text
Stage 5 — Final validation and thesis hardening.

Goal:
Validate the complete thesis for evidence, citations, numerical consistency, causal wording, clinical wording, reproducibility, and LaTeX compilation.

Allowed scope:
- Thesis LaTeX files
- Bibliography files
- thesis-writing/audit/
- thesis-writing/planning/
- thesis-writing/logs/
- figure/table directories

Forbidden scope:
- Do not change research code unless explicitly instructed.
- Do not rerun expensive experiments.
- Do not invent missing values.
- Do not silently remove unresolved placeholders.
- Do not commit or push changes.

Tasks:
1. Compile the thesis using the approved command.
2. Check citations and references.
3. Check all figure and table references.
4. Cross-check major numerical claims against evidence sources.
5. Check causal and clinical wording.
6. Check terminology and notation consistency.
7. Produce a final validation report.

Deliverables:
- final_validation_report.md
- citation_validation_report.md
- figure_table_validation_report.md
- unresolved_final_placeholders.md
- advisor_review_packet.md

Validation:
- Every major claim must be supported or flagged.
- Every unresolved issue must remain visible.
- The final report must clearly distinguish fixed issues from remaining issues.
```

---

# 6. Standard Codex Prompt Template

Every Codex prompt in this project should follow this structure.

```text
Context:
[Where Codex is operating and what has already been approved]

Objective:
[One specific goal]

Allowed scope:
[Files/directories Codex may inspect or edit]

Forbidden scope:
[Files/directories/actions Codex must not touch]

Required procedure:
[Inspection, validation, editing, and reporting steps]

Deliverables:
[Exact files or outputs expected]

Validation:
[Checks Codex must perform]

Reporting:
At the end, report:
1. files inspected;
2. files changed;
3. key findings;
4. unresolved issues;
5. validation performed.

Safety:
Do not commit or push changes unless explicitly instructed.
```

---

# 7. Human Approval Gates

Codex should not move freely from one stage to the next. Each stage should end with a human approval gate.

| Gate | Approval Question |
|---|---|
| After Stage 0 | Is the workspace safe and correctly configured? |
| After Stage 1 | Is the literature corpus complete and focused enough? |
| After Stage 2 | Do we agree what evidence exists and what is missing? |
| After Stage 3 | Do we approve the thesis structure and story? |
| During Stage 4 | Is each chapter section accurate and appropriately scoped? |
| After Stage 5 | Is the thesis ready for supervisor review or submission? |

If a gate fails, revise the relevant stage rather than continuing forward.

---

# 8. What Codex Should Never Do Without Approval

Codex should not:

- commit changes;
- push changes;
- delete papers;
- delete results;
- overwrite generated figures;
- rerun expensive experiments;
- rewrite the full thesis at once;
- modify code while writing thesis prose;
- add unsupported citations;
- hide unresolved uncertainty;
- convert proxy labels into verified diagnoses;
- claim clinical actionability without support;
- claim causality without assumptions and sensitivity discussion.

---

# 9. Current Status Tracking

A useful project status section should be maintained in `THESIS_PLAN.md` or a separate `THESIS_STATUS.md` file.

Suggested format:

```markdown
# Thesis Status

## Completed

- [ ] Stage 0 environment validated
- [ ] Literature corpus structured
- [ ] Repository evidence audited
- [ ] Thesis outline approved
- [ ] Claim ledger approved

## In Progress

- [ ] Current active task

## Blocked

- [ ] Missing result
- [ ] Missing citation
- [ ] Advisor decision needed

## Next Action

- [ ] Next Codex prompt to run
```

---

# 10. Definition of Done

The thesis-writing project is complete only when:

1. the repository has been fully audited;
2. every thesis chapter is mapped to evidence;
3. all numerical results are verified;
4. all citations are validated;
5. all figures and tables are traceable;
6. causal and clinical claims are appropriately qualified;
7. proxy states are described as proxies unless separately validated;
8. the thesis compiles using the approved BGU template;
9. unresolved limitations are explicitly documented;
10. the final thesis is internally consistent;
11. the final draft is supervisor-ready.

---

# 11. Immediate Next Step

If starting from the beginning, do **Stage 0 only**.

The immediate objective is:

```text
Validate the workspace and create minimal repository instructions.
```

Do not start the literature audit, evidence audit, outline, or writing stages until Stage 0 is complete and approved.

The first practical action is to open `CliniCause/` in VS Code, verify the required extensions and command-line tools, then run the Stage 0 Codex prompt included above.

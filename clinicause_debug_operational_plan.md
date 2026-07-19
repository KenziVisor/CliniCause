# CliniCause — Complete Debugging and Integration Validation Plan

**Document status:** Canonical operational plan  
**Version:** 1.2  
**Frozen on:** 2026-07-17  
**Project:** `KenziVisor/CliniCause`  
**Primary purpose:** Debug the merged CliniCause repository before updating the thesis and conference paper  
**Intended users:** The author, ChatGPT as coordinator/reviewer, and Codex agents in VS Code  
**Canonical filename:** `clinicause_debug_operational_plan.md`

---

## 1. Purpose of this document

This document defines the complete and stable debugging process for the merged `CliniCause` project.

`CliniCause` was created by combining two projects that had previously worked separately:

- `STraTS/`
- `causal-irregular-time-series/`

The top-level merged project, including `router.py` and shared configuration or orchestration, may have introduced regressions at the integration boundaries. The working assumption is therefore:

> The two original subprojects were operational before the merge, so integration regressions are the first debugging target. However, this is a prioritization rule rather than proof that the subprojects contain no latent bugs.

The process uses **Codex in VS Code on the remote server for every stage**. Laptop Codex is unavailable because the VPN prevents practical repository work.

Separation of duties is preserved on the server through:

- one active writer thread for a bounded task;
- fresh Codex threads for independent review;
- separate Git worktrees or read-only scopes when parallel investigation is useful;
- explicit handoff packets between implementing and reviewing threads;
- ChatGPT as the external coordinator and evidence reviewer.

The server has the repository, real data, run artifacts, and logs. This access does not make execution the default diagnostic method. Because a complete pipeline run is expensive, the workflow prioritizes static analysis, Git-history inspection, contract validation, existing-artifact analysis, synthetic tests, and narrow component checks before authorizing progressively larger runtime tests.

The plan is intentionally evidence-gated. A stage is not complete because an agent says it is complete. It is complete only after the required evidence, tests, diffs, and runtime observations have been checked.

This document is designed to be added to the project sources and used at the beginning of future conversations. Future sessions must treat it as the canonical plan rather than inventing a new debugging methodology.

---

## 2. Change-control rule

This plan is frozen unless the author explicitly approves a change.

### 2.0 Approved operational changes — 2026-07-17

The author explicitly approved these changes:

1. **Server-only Codex operation**
   - All Codex stages run on the remote server.
   - Laptop Codex is not used because VPN constraints prevent practical work.
   - Independent review is preserved through fresh server Codex threads, explicit writer ownership, and separate worktrees or read-only scopes when needed.

2. **Execution Budget Gate**
   - Expensive execution is prohibited by default.
   - Correctness should be established as far as possible through static inspection, history analysis, contract tests, synthetic fixtures, existing logs and artifacts, and narrow component checks.
   - A representative or full pipeline run requires explicit author approval after cheaper evidence has been exhausted or shown insufficient.
   - The requirement to reproduce before repair remains, but reproduction must use the smallest and cheapest test capable of demonstrating the defect; it does not imply reproducing the complete pipeline.

3. **Slurm/container runtime isolation and three independent execution tracks**
   - The interactive VS Code shell on the compute node is not assumed to be the producing runtime environment.
   - Current evidence indicates that the project Conda environment is activated inside an Apptainer container launched by Slurm rather than in the host-node shell. D1 must verify the exact container image, activation command, and environment name before runtime work.
   - Codex may perform static analysis and cheap wire checks interactively, but environment-authoritative or pipeline execution must run as an isolated `sbatch` job with its own logs, run ID, output root, and resource request.
   - Runtime validation is divided into three independently schedulable tracks: preprocessing; STraTS using precomputed validated PKL inputs; and the causal pipeline using explicitly selected validated handoff artifacts.
   - No track may implicitly rerun an earlier track. Inputs must be named, hashed where practical, and recorded in a manifest.
   - A monolithic `--stages all` run is not the default validation method and remains an optional final integration gate requiring explicit author approval.

These changes replace the original laptop/server division of responsibilities, strengthen the progressive-execution policy, and define the authoritative runtime boundary. All other evidence, privacy, review, regression-test, and thesis/paper gates remain in force.

### 2.1 What future conversations may change

Future conversations may:

- record the current repository commit;
- fill in previously unknown paths or commands;
- add discovered facts to the status and decision records;
- mark stages as completed;
- add narrow repair stages;
- update the current model-name snapshot when OpenAI changes model availability;
- refine test commands after the repository has been inspected;
- add confirmed integration contracts;
- add confirmed failure IDs and root causes.

### 2.2 What future conversations must not change without explicit approval

Future conversations must not silently change:

- the server-only thread/worktree division of responsibilities;
- the assumption that integration boundaries are investigated first;
- the requirement for reproducible failures before repair;
- the small-commit policy;
- the requirement for regression tests;
- the independent-review gate;
- the execution-budget hierarchy from non-execution evidence through narrow tests to any approved full run;
- the rule that the thesis and paper are updated only after code validation;
- the evidence hierarchy;
- the data-privacy rules;
- the prohibition on broad refactoring during root-cause investigation;
- the prohibition on treating successful execution as scientific equivalence;
- the requirement to compare against pre-merge or previously accepted behavior where evidence exists.

If a future session proposes a materially different process, it must state:

1. the exact proposed change;
2. the evidence motivating it;
3. the risks;
4. the parts of this plan that would be replaced;
5. that author approval is required.

---

## 3. High-level objective

The debugging program must establish, with auditable evidence:

1. which failures are caused by the merger;
2. which failures are environment, data, artifact, or dependency mismatches;
3. whether any latent subproject bugs are exposed;
4. whether the top-level orchestration passes the correct inputs, paths, configuration, and state;
5. whether each subproject still works independently inside the merged repository;
6. whether the complete pipeline works on the smallest controlled sample required to validate the relevant contracts;
7. whether a representative or full run succeeds on the server **only when such a run is necessary for the intended claims and explicitly approved**;
8. whether important outputs remain equivalent to the accepted baseline within an explicitly defined tolerance;
9. how a new user or agent can reproduce the validated pipeline;
10. what exact statements can safely be written in the thesis and paper.

---

## 4. Scope

### 4.1 In scope

The initial debugging scope includes:

- `router.py`;
- top-level orchestration;
- entry points and command-line arguments;
- configuration loading and propagation;
- imports and Python path behavior;
- current working directory assumptions;
- relative and absolute path handling;
- environment variables;
- dependency and package-version collisions;
- model selection and model-name mapping;
- device and accelerator selection;
- random seed propagation;
- preprocessing order;
- data schemas;
- identifiers and split consistency;
- time units, time ordering, padding, and masks;
- serialization and deserialization;
- checkpoint loading;
- filenames and output-directory conventions;
- handoff artifacts between the predictive and causal components;
- stale caches and stale generated artifacts;
- component-level and end-to-end execution;
- validation of outputs against previous accepted evidence;
- documentation necessary for reliable execution.

### 4.2 Initially out of scope

The following are out of scope until the relevant debug gate is passed:

- broad architecture redesign;
- performance optimization unrelated to the failure;
- stylistic refactoring;
- migration to a different framework;
- replacing models or estimators;
- changing the scientific design;
- changing target definitions or causal exposures;
- recomputing thesis results merely because the pipeline can run;
- rewriting thesis chapters;
- writing the conference paper;
- changing checked result packets;
- altering figures or archived results;
- changing unrelated `thesis-writing/` material;
- upgrading all dependencies without a failure-specific justification.

A narrowly necessary refactor may be approved only when a minimal fix cannot safely restore the contract. The evidence report must explain why.

---

## 5. Core working assumptions

The following assumptions guide prioritization but must be tested where possible.

### 5.1 Strong initial assumption

Both original projects worked separately before the merge.

Implication:

- investigate merge-related differences and integration contracts before assuming a deep algorithmic defect.

### 5.2 Non-guarantee

Previous success does not prove that:

- every code path worked;
- the original environment is still reproducible;
- all artifacts match the current data;
- the subprojects were free of latent bugs;
- the previous outputs were scientifically correct;
- the merged repository preserves the same defaults;
- the old runs used the current requirements files.

### 5.3 Runtime authority

The server is authoritative for:

- real runtime behavior;
- real data schemas;
- actual logs;
- resource behavior;
- environment-dependent failures;
- any approved sample, representative, or full-pipeline execution.

Runtime authority does not imply that runtime execution should be used early or broadly. Static repository evidence, version history, configuration contracts, existing artifacts, and narrow tests should answer as much as possible before a costly execution is considered.

### 5.4 Execution-cost assumption

A complete CliniCause pipeline run is expensive in time and possibly compute. Therefore:

- no stage may use a full run merely as a general diagnostic;
- every runtime test must answer a named question or falsify a named hypothesis;
- the smallest sufficient execution scope must be used;
- representative and full runs require explicit author approval;
- absence of a full run is not a defect when the intended claim can be validated with cheaper, stronger, or already available evidence.

### 5.5 Containerized runtime assumption

The interactive server shell and the Slurm/Apptainer runtime are distinct environments.

Until D1 verifies the exact setup, use this operating assumption:

- the host-node shell is suitable for Git inspection, static analysis, file-contract checks, and other cheap wire checks;
- it is not authoritative for the packages, Conda environment, paths, mounts, or GPU configuration used by the pipeline;
- pipeline-dependent checks must use the same `sbatch` → Apptainer → environment-activation path intended for actual execution;
- the exact container image, environment name, mount map, working directory, and package fingerprint must be captured in every runtime evidence packet;
- a direct interactive failure does not prove that the containerized job fails, and a containerized success does not validate host-shell behavior.

### 5.6 Code-review authority

A successful server run does not prove that:

- the patch is minimal;
- the patch is maintainable;
- unrelated behavior was not changed;
- hidden fallbacks are masking a defect;
- the implementation matches the intended contract.

A separate review of the diff is required.

---

## 6. Actors and responsibilities

## 6.1 Author

The author:

- confirms priorities and intended behavior;
- supplies historical knowledge not present in Git or logs;
- confirms which pre-merge runs were accepted as working;
- decides whether behavior differences are intended;
- approves any scope expansion;
- approves scientific changes;
- decides when validated code is ready to be reflected in the thesis and paper;
- does not need to perform mechanical checks that Codex can perform reliably.

## 6.2 ChatGPT coordinator and reviewer

ChatGPT:

- maintains the overall plan;
- determines the next bounded stage;
- converts the plan into precise Codex prompts;
- reviews stage evidence, diffs, test output, and sanitized logs;
- separates verified facts from hypotheses;
- prevents premature thesis or paper updates;
- selects the appropriate model capability and reasoning effort;
- decides whether the next state is ready, ready with gates, narrow repair, or blocked;
- does not claim runtime validation unless server evidence was inspected;
- does not invent missing commands, paths, versions, or historical behavior.

## 6.3 Server Codex — implementing thread

The active implementing thread is primarily responsible for:

- repository and history inspection;
- architecture and dependency mapping;
- pre-merge versus post-merge differential analysis;
- identifying and documenting integration contracts;
- collecting the runtime and environment baseline;
- designing synthetic fixtures and contract tests;
- reproducing failures at the smallest practical scope;
- inspecting full logs and real data locally when necessary;
- preparing and reviewing isolated Slurm job scripts for environment-authoritative checks;
- using the interactive shell only for static work and cheap wire checks unless a task explicitly authorizes more;
- applying only explicitly authorized patches;
- running narrow tests before broader tests;
- generating sanitized evidence;
- not exposing data or sensitive paths unnecessarily;
- not submitting representative, full, or monolithic jobs without explicit author approval.

## 6.4 Server Codex — independent reviewing thread

A fresh reviewing thread is responsible for:

- inspecting the baseline and exact diff independently;
- checking whether the failure was demonstrated with sufficient evidence;
- reviewing regression tests and contract coverage;
- detecting hidden fallbacks, broad changes, or unsupported assumptions;
- inspecting relevant server-only evidence without modifying the implementation;
- deciding whether broader execution is justified;
- producing an independent readiness or repair decision.

The reviewing thread should use a separate worktree when file isolation is useful. It should remain read-only unless a later narrow repair task explicitly transfers writer ownership.

## 6.5 Independent reviewer

The independent reviewer should normally be:

- a fresh Codex thread on the server; and/or
- ChatGPT reviewing committed diffs, evidence reports, sanitized command output, and author decisions.

The same agent thread that proposed and implemented a fix must not be the only approver of that fix. Server access does not remove this separation requirement.

---

## 7. Server-only operating model and execution budget

## 7.1 Server capabilities

The server may perform:

- Git and static-code inspection;
- dependency and environment comparison;
- test discovery;
- architecture and contract mapping;
- analysis of existing logs and run artifacts;
- synthetic and mocked tests;
- controlled sample loading;
- narrow runtime reproduction;
- component and boundary tests;
- representative or full execution only after explicit approval;
- generation of sanitized evidence;
- patching in the authorized branch by the active writer thread.

The server must not:

- commit raw private data;
- copy raw logs containing sensitive information into the repository;
- treat access to data as permission to run expensive experiments;
- run a representative or full experiment before cheaper gates pass and author approval is recorded;
- overwrite accepted result archives;
- delete old artifacts while debugging;
- modify the thesis or paper during code debugging;
- make broad environment changes without capturing the baseline;
- let an implementing thread self-approve a material fix.

## 7.1A Authoritative runtime boundary: Slurm and Apptainer

The interactive VS Code session is attached to a compute node, but the project runtime is expected to live inside an Apptainer container launched by Slurm. The absence of an active Conda environment in the host shell is therefore not, by itself, an installation defect.

The exact runtime path must be verified before execution:

```text
sbatch script
→ Slurm allocation
→ Apptainer image
→ bind mounts and working directory
→ environment activation inside the container
→ stage-specific command
→ unique logs and output root
```

Rules:

- Codex may run E0 and safe E1 wire checks interactively.
- Pure E2 tests may run interactively only when they do not depend on project-specific binary packages, GPU behavior, container mounts, or the producing environment.
- Environment-sensitive E1/E2 checks and all E3–E6 execution must use a dedicated `sbatch` job unless the author explicitly approves another mechanism.
- The job script must fail fast, print the commit and nested-repository commits, fingerprint the container runtime, and never reuse an accepted run ID.
- Job submission is a distinct authorized action. Codex may prepare and inspect a script without being authorized to submit it.
- Slurm jobs must not edit source files. They may write only to their declared unique log and debug-output roots.
- The node shell, the container, and any named Conda environment must be documented separately; do not merge their package inventories into one environment claim.

## 7.1B Three independent runtime tracks

Runtime validation is split into three independently schedulable Slurm tracks.

### Track P — Preprocessing

Purpose:

- validate raw-data path resolution, dataset-specific preprocessing, schema construction, identifier preservation, and PKL production;
- produce or validate preprocessing artifacts without invoking STraTS or the causal estimators.

Required outputs:

- unique run ID and output root;
- input-data identifiers or safe hashes;
- dataset/config manifest;
- output PKL paths, sizes, hashes where practical, and schema summaries;
- warnings, runtime, peak-memory information, and exit status.

Track P may be split by dataset when this reduces cost or isolates failures. A preprocessing job must not launch STraTS or the causal pipeline.

### Track S — STraTS from precomputed PKL inputs

Purpose:

- validate the predictive project independently using precomputed, contract-checked PKL files;
- avoid paying the preprocessing cost during STraTS debugging and validation.

Required inputs:

- explicitly selected PKL files;
- their provenance status, paths, sizes, hashes where practical, and schema-contract result;
- model/config/seed/checkpoint settings.

Required outputs:

- prediction or checkpoint artifacts required by the active contract;
- identifier/order manifest;
- configuration and environment fingerprint;
- warnings, runtime, resource use, and exit status.

Track S must not regenerate preprocessing artifacts or silently select a different PKL file.

### Track C — Causal pipeline

Purpose:

- validate causal preprocessing, graph/tagging, matching, estimators, and result export independently of preprocessing and STraTS execution;
- consume only explicitly selected, contract-checked preprocessing and prediction artifacts required by the active causal configuration.

Required inputs and outputs must be determined by the D1 contract map. Track C must not invoke preprocessing or STraTS implicitly.

### Cross-track rules

- Each track has its own `sbatch` script or clearly parameterized stage-specific script.
- Each track writes to a unique debug output root and unique Slurm logs.
- Handoffs are explicit artifacts with manifests; directory discovery alone is not sufficient.
- An existing precomputed artifact may be used only after provenance and schema are classified. Unknown provenance may be acceptable for a narrow contract check but not for final scientific equivalence.
- Tracks may be validated independently and need not be run in one job.
- A final orchestration check, if ever needed, should first chain the already validated tracks without recomputing accepted artifacts.
- A monolithic router `--stages all` job is an optional E6 gate, not the normal debugging path.

## 7.2 Execution Budget Gate

Execution follows a cost-aware evidence ladder. Each level is attempted only when the preceding levels cannot answer the relevant question.

### E0 — No-execution evidence

Use:

- Git history and pre/post-merge diffs;
- code-path and import analysis;
- configuration and CLI propagation analysis;
- schema and serialization contracts from source;
- checkpoint and cache metadata;
- existing sanitized logs;
- existing run summaries, manifests, hashes, and artifacts;
- static searches for path, naming, ordering, seed, and default mismatches.

### E1 — Side-effect-free wire checks

Use:

- path, mount, executable, and container-image existence checks;
- `sbatch` script parsing and shell syntax validation;
- configuration loading and CLI parsing that are proven not to create run directories;
- test collection;
- schema validators that do not load private data;
- linting or type checks already supported by the repository.

Run these interactively only when they do not depend on the containerized project environment. Otherwise package them as a minimal Slurm probe.

### E2 — Synthetic or mocked contract tests

Use tiny synthetic fixtures to validate:

- paths;
- config propagation;
- identifiers;
- ordering;
- temporal units;
- shapes and dtypes;
- serialization;
- handoff adapters;
- artifact names;
- cache invalidation behavior.

### E3 — Narrow Slurm probe with real data or artifacts

Use the smallest safe input that can decide a specific hypothesis. Prefer one loader, function, component, checkpoint, or producer-consumer boundary. Run it through an isolated `sbatch` job when it depends on the project container, real mounts, GPU, or producing environment.

### E4 — Fixed micro-run within one runtime track

Run the smallest deterministic slice of Track P, S, or C capable of validating the active contract. This level requires a written execution justification and a stage-specific Slurm job. It does not authorize a monolithic router run.

### E5 — Representative track run

Requires explicit author approval. It must be limited to one of Tracks P, S, or C unless a cross-track question truly cannot be answered independently. It must be justified as necessary to expose scale, resource, worker, batching, artifact-collision, or stochastic behavior that E0–E4 cannot validate.

### E6 — Cross-track or monolithic integration run

Requires explicit author approval and is the final optional execution gate. Prefer chaining validated track artifacts over recomputing everything. A monolithic `--stages all` job is authorized only when a thesis/paper, equivalence, or reproducibility claim specifically requires proof of one-command orchestration and cannot be established from the three independent validated tracks.

## 7.3 Required execution-justification record

Before E4, E5, or E6, record:

```text
Execution ID
Runtime track: P / S / C / cross-track
Current parent and nested-repository commits
Question being answered
Hypothesis being tested
Why cheaper evidence is insufficient
SBATCH script path or immutable script content
Container image and bind-mount plan
Environment activation command and expected environment name
Exact stage-specific command
Container working directory
Input artifact paths and provenance status
Expected runtime/resource scale
Unique run ID, output root, and Slurm log paths
Overwrite protection
Stopping conditions
Expected success signal
Expected failure signal
Ambiguous-result handling
Submission owner
Approval owner
```

For E5 and E6, the approval owner must be the author.

## 7.4 Single-writer rule

At any given time, only one server Codex thread is the writer for a specific bug or stage.

- Other threads must be read-only reviewers or work in separate, non-overlapping worktrees.
- If ownership moves, the current state must first be committed or intentionally preserved with an explicit handoff.
- Do not let two threads independently edit the same branch or files.

## 7.5 Git as the synchronization and review mechanism

Use Git commits, branches, and worktrees to separate implementation and review.

Do not synchronize code by:

- copying loose files between threads;
- manually replacing individual files without a base commit;
- pasting a large uncommitted patch without recording its base state;
- using an unclear shared worktree for parallel writers.

Exceptions require explicit documentation.

---

## 8. Repository and Git policy

## 8.1 Branching

Use a dedicated debugging branch, for example:

```text
debug/merge-integration
```

If repository policy requires another naming convention, follow the local policy.

Do not assume the branch name. Inspect the repository first.

## 8.2 Baseline terminology

Every task must distinguish:

- **current HEAD** — the commit currently checked out;
- **task baseline** — the commit from which the current debug task is evaluated;
- **pre-merge reference** — the last known relevant state of a subproject before integration;
- **accepted runtime baseline** — a historical run, artifact, or commit that the author considers working;
- **intervening commits** — commits after the task baseline classified as relevant, unrelated, or conflicting.

Do not reset unrelated later work merely to recreate an older state.

## 8.3 Initial Git inspection

At the start of every stage:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git log -15 --oneline --decorate
```

If subprojects are nested repositories or submodules, inspect them separately.

Also inspect local instruction files such as:

```text
AGENTS.md
README.md
CONTRIBUTING.md
WORKFLOW.md
```

## 8.4 Commit policy

Use one commit per meaningful unit.

Recommended patterns:

```text
debug: record baseline for <failure-id>
test: reproduce <failure-id>
fix: restore <named-contract>
test: cover <named-edge-case>
docs: record validated run contract
```

A fix commit should normally contain:

- the minimal implementation change;
- its regression test;
- only necessary fixture or documentation changes.

Avoid mixing:

- multiple unrelated failures;
- cleanup;
- formatting churn;
- thesis edits;
- generated results;
- dependency upgrades unrelated to the root cause.

## 8.5 Prohibited Git operations unless explicitly approved

Do not:

- `git reset --hard`;
- clean the worktree;
- delete untracked artifacts;
- rewrite shared history;
- force push;
- revert unrelated commits;
- remove accepted result archives;
- commit secrets or data;
- commit or push merely because a Codex task completed.

## 8.6 Worktrees for parallel work

Parallel agents are allowed only when the work can be separated into independent scopes.

Use separate Git worktrees and branches for:

- environment analysis;
- history and merge-diff analysis;
- data-contract investigation;
- independent patch review.

Do not run parallel writers against the same branch and files.

---

## 9. Evidence hierarchy

Use this hierarchy when claims conflict:

1. **Reproducible current execution** with exact command, commit, environment, and input.
2. **Versioned source code** at the relevant commit.
3. **Historical execution records** tied to a commit and environment.
4. **Stored artifacts** with known provenance and hashes.
5. **Derived validation records** such as checked schemas or reconstructed metrics.
6. **Documentation and requirements files**.
7. **Human recollection**.
8. **Inference**.

Human recollection can define intended behavior, but it must be labeled as a human decision rather than execution evidence.

Important distinctions:

- A requirements file is an intended environment, not proof of the historical environment.
- A filename is not proof that a stage completed.
- A log is not useful unless its commit, command, and context are known.
- A successful run does not establish output equivalence.
- Output equivalence does not establish scientific validity.
- A regression test proves only the contract represented by that test.

---

## 10. Data, privacy, logs, and secrets

## 10.1 Server-local evidence

Raw data and raw logs remain on the server unless explicitly approved for export.

## 10.2 Sanitized evidence

Evidence returned across server threads, sent to ChatGPT, or committed may include:

- command;
- commit hash;
- environment fingerprint;
- schema without sensitive values;
- dimensions;
- dtypes;
- aggregate missingness;
- sanitized exception;
- stack frame locations;
- hashes;
- timings;
- test results;
- aggregate metric comparisons;
- artifact identifiers that are safe to expose.

## 10.3 Do not commit

Never commit:

- raw patient-level data;
- identifying fields;
- access tokens;
- credentials;
- private storage URLs;
- environment secrets;
- full logs with sensitive records;
- absolute paths that reveal credentials or protected mount names when avoidable;
- model artifacts that repository policy excludes.

## 10.4 Log excerpts

A log excerpt should contain the smallest evidence required to explain the failure.

Prefer:

```text
exception type
first meaningful failing frame
relevant shape/schema summary
effective configuration key
```

Avoid dumping entire logs into prompts.

---

## 11. Failure taxonomy

Every reproduced failure receives one primary classification.

### A. Integration regression

The subprojects work independently, but their merged handoff fails.

Examples:

- wrong path;
- renamed file;
- missing argument;
- changed default;
- schema mismatch;
- identifier mismatch;
- serialization mismatch;
- execution-order defect.

### B. Latent subproject bug

A subproject contains a defect that was not observed in the accepted prior runs but is now triggered.

Examples:

- unhandled empty group;
- non-deterministic ordering assumption;
- edge-case timestamp;
- unsupported missingness pattern;
- type assumption.

### C. Environment divergence

The code relies on an environment different from the current server environment.

Examples:

- Python version;
- package version;
- CUDA or driver mismatch;
- compiled extension;
- device visibility;
- locale;
- environment variable;
- shell behavior.

### D. Data or artifact mismatch

The code and environment may be correct, but the supplied data, checkpoint, cache, or generated artifact is incompatible.

Examples:

- stale cache;
- checkpoint from a different architecture;
- different column names;
- incomplete preprocessing output;
- mismatched split;
- old serialized object.

### E. Intended behavior change mistaken for a bug

The merger intentionally changed behavior, but the change is undocumented or the caller expects old behavior.

This requires an explicit author decision.

### F. Non-determinism or resource defect

Examples:

- race condition;
- data-loader worker issue;
- random seed omission;
- GPU memory behavior;
- unstable ordering;
- timeout;
- file-lock conflict.

### G. Scientific mismatch without runtime failure

The pipeline runs, but:

- outputs differ materially from the accepted baseline;
- labels, exposures, or populations changed;
- aggregation is different;
- evaluation logic changed;
- the result cannot support the intended thesis claim.

This category is high priority even when no exception occurs.

### Default investigation order

Use this prioritization:

```text
A → C/D → B/F → E → G
```

Category G is checked at validation gates even when the runtime problem appears resolved.

---

## 12. Integration-contract map

The project must eventually have a verified contract map for every major boundary.

Each contract entry should contain:

```text
Contract ID
Producer
Consumer
Input/output artifact
Required schema or type
Required ordering
Required units
Required identifiers
Path convention
Configuration keys
Version assumptions
Validation test
Current status
Evidence
```

At minimum, inspect these contract families:

### 12.1 Path and filesystem contract

- repository root;
- current working directory;
- paths relative to `__file__`;
- data roots;
- output roots;
- checkpoint roots;
- temporary directories;
- directory creation;
- overwrite behavior;
- filename conventions.

### 12.2 Configuration contract

- required keys;
- default values;
- environment overrides;
- CLI argument names;
- booleans and string parsing;
- model identifiers;
- dataset identifiers;
- stage enablement;
- seed;
- device;
- batch sizes;
- run IDs.

### 12.3 Data schema contract

- columns;
- dtypes;
- shapes;
- nullability;
- permitted categories;
- key uniqueness;
- identifier formats;
- index behavior;
- sort order;
- units;
- value ranges.

### 12.4 Temporal contract

- timestamp units;
- absolute versus relative time;
- sorting;
- duplicated times;
- padding;
- masks;
- observation windows;
- prediction horizons;
- train/validation/test boundaries.

### 12.5 Prediction-output contract

- model output type;
- logits versus probabilities;
- tensor/array/dataframe format;
- row order;
- patient/stay mapping;
- label ordering;
- checkpoint version;
- output filename;
- serialization method.

### 12.6 Causal-input contract

- exposure definition;
- outcome definition;
- covariates;
- identifiers;
- matching or split metadata;
- missing-value handling;
- expected prediction columns;
- estimator-specific fields.

### 12.7 Environment contract

- Python;
- package versions;
- OS assumptions;
- CUDA;
- driver;
- GPU;
- CPU and memory;
- shell;
- locale;
- compiled libraries.

### 12.8 Randomness contract

- Python seed;
- NumPy seed;
- framework seed;
- data-loader worker seed;
- deterministic settings;
- split seed;
- estimator seed.

### 12.9 Artifact and cache contract

- expected producing code;
- code version;
- configuration;
- checksum;
- invalidation rule;
- whether a missing artifact is generated or treated as blocking;
- whether stale artifacts can be detected.

---

## 13. Stage overview

The complete process is divided into these stages:

```text
Stage D0 — Establish the debugging baseline
Stage D1 — Map architecture, history, and integration boundaries
Stage D2 — Reproduce and classify failures on the server
Stage D3 — Build contract and regression-test infrastructure
Stage D4 — Repair failures one at a time
Stage D5 — Validate components and integration progressively
Stage D6 — Validate output equivalence and scientific contracts
Stage D7 — Harden reproducibility and execution documentation
Stage D8 — Final independent audit
Stage D9 — Update thesis and paper
```

A narrow repair stage uses a suffix:

```text
D4.2A
D5.3A
D6.1A
```

---

# 14. Stage D0 — Establish the debugging baseline

## 14.1 Objective

Create an immutable record of the starting state before modifying code or environment.

## 14.2 Server read-only tasks

Inspect the repository without changing code or environment:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git log -15 --oneline --decorate
```

Then identify:

- repository structure;
- nested repositories or submodules;
- instruction files;
- current tests;
- dependency files;
- top-level entry points;
- known pre-merge commits or branches;
- current dirty files;
- protected thesis, paper, results, data, checkpoint, and artifact subtrees.

Record the active environment without changing it:

```bash
python --version
which python
pip --version
pip freeze
```

Where relevant:

```bash
nvidia-smi
nvcc --version
uname -a
```

Also record:

- active virtual environment;
- data-root existence;
- key artifact-root existence;
- available disk space;
- available GPU memory;
- relevant environment variables with secrets redacted;
- current working directory;
- exact command believed to fail, if supported by repository evidence or existing logs;
- location and date of relevant logs.

Do not upgrade, reinstall, reproduce, or repair anything in D0. The D0 report may identify the cheapest next reproduction candidate, but execution waits for coordinator review.

## 14.3 Server-only review separation

Because laptop Codex is unavailable:

- D0 collection runs in one server Codex thread;
- ChatGPT reviews the returned report;
- any independent repository audit that requires Codex runs in a fresh server thread;
- later implementation and review work use separate threads and, when useful, separate worktrees.

## 14.4 Pre-merge baseline discovery

Identify, where possible:

- last accepted commit for `STraTS`;
- last accepted commit for `causal-irregular-time-series`;
- first merge or integration commit;
- commits that altered entry points;
- commits that changed configuration;
- commits that changed data schemas;
- historical commands;
- historical output artifacts;
- historical environments or dependency snapshots.

Unknown items remain unknown; do not invent them.

## 14.5 Deliverables

Create or update a durable debug record containing:

- server parent-repository commit;
- nested-repository commits, where applicable;
- branch;
- dirty state;
- environment fingerprint;
- protected paths;
- pre-merge references;
- known commands;
- known failures;
- unresolved baseline questions.

Suggested repository location, subject to local instructions:

```text
debugging/baseline.md
```

If an existing canonical audit or debug location exists, update it instead of creating a duplicate.

## 14.6 Exit criteria

D0 is complete when:

- the server parent and nested repository commits and worktree states are known;
- the server environment is fingerprinted;
- protected material is identified;
- at least one suspected failing command is documented;
- pre-merge references are identified or explicitly marked unavailable;
- no code or environment repair has been made.

Readiness wording:

```text
READY FOR STAGE D1 — BASELINE RECORDED
```

---

# 15. Stage D1 — Map architecture, history, and integration boundaries

## 15.1 Objective

Understand exactly how the two projects were combined before attempting repairs.

## 15.2 Primary environment

Server Codex, primarily in a read-only architecture-analysis thread. Real data and expensive runtime execution remain out of scope for D1 unless a separate narrow check is explicitly authorized.

## 15.3 Required inspections

Map:

- root-level orchestration;
- `router.py`;
- all callable entry points;
- CLI scripts;
- configuration files;
- environment files;
- dataset loaders;
- preprocessing;
- model training and inference;
- output exports;
- causal ingestion;
- result writing;
- caches;
- checkpoints;
- logs.

## 15.4 Historical differential analysis

Compare:

- each pre-merge subproject state;
- the merge commit;
- current HEAD.

Prioritize changes in:

1. imports;
2. module paths;
3. current working directory;
4. relative paths;
5. renamed files;
6. configuration keys;
7. CLI signatures;
8. defaults;
9. model-name mapping;
10. dataset-name mapping;
11. schema transformations;
12. serialization;
13. output names;
14. execution order;
15. environment files;
16. seeds and devices;
17. cache behavior.

## 15.5 Required output

Produce:

1. repository execution map;
2. integration-boundary map;
3. contract inventory;
4. ranked hypothesis list;
5. list of tests possible without runtime execution or private-data access;
6. list of narrow server-local checks that may later be required;
7. verified or provisional map of the Slurm → Apptainer → environment-activation runtime path;
8. a feasibility map for independently invoking preprocessing, STraTS from precomputed PKLs, and the causal pipeline without implicit earlier stages;
9. list of ambiguous intended behaviors requiring author input.

Each hypothesis should use this template:

```text
Hypothesis ID:
Confidence: high / medium / low
Suspected boundary:
Evidence:
Expected failure signature:
Smallest falsifying test:
Files involved:
Server evidence required:
```

## 15.6 No-edit boundary

D1 is primarily inspection.

Allowed edits:

- durable architecture or contract documentation;
- non-invasive test inventory;
- no behavior-changing implementation edit.

## 15.7 Exit criteria

D1 is complete when:

- the integration path is mapped end to end;
- major contracts have IDs;
- the likely merge-sensitive changes are ranked;
- the cheapest next reproduction or falsification task is precise;
- the containerized runtime path and three-track stage boundaries are mapped or explicitly marked as requiring a narrow follow-up;
- no broad speculative fix has been applied.

Readiness wording:

```text
READY FOR STAGE D2 — INTEGRATION MAP COMPLETE
```

---

# 16. Stage D2 — Reproduce and classify failures on the server

## 16.1 Objective

Turn vague symptoms into deterministic failure records.

## 16.2 Primary environment

Server. Static and wire checks may run in the interactive Codex shell. Environment-authoritative reproduction runs as an isolated Slurm job inside the intended Apptainer/container environment.

## 16.3 Failure-record format

Every failure receives an ID, for example:

```text
F-001
F-002
```

Required fields:

```text
Failure ID
Current commit
Branch
Exact command
Working directory
Environment
Input or sample identifier
Expected behavior
Observed behavior
Exit code
First meaningful error
Relevant stack frames
Relevant sanitized schema/shape
Log path
Reproduction rate
Failure category
Open hypotheses
```

## 16.4 Reproduction ladder

Do not begin with runtime execution when static or existing evidence can establish the failure. Apply the Execution Budget Gate from Section 7 and stop at the cheapest level that answers the active question.

### L-1 — Static and historical reproduction

Demonstrate the violated contract without execution where possible, using:

- pre/post-merge diffs;
- incompatible function signatures or defaults;
- provable path-resolution errors;
- schema producer-consumer mismatch;
- configuration keys that cannot propagate correctly;
- artifact metadata incompatible with the current consumer;
- existing logs tied to a known command and commit.

A strong L-1 demonstration may justify writing a failing contract test before any real-data runtime attempt.

### L0 — Runtime wiring and environment

First inspect the Slurm wrapper, container image, binds, working directory, and environment activation. Use an isolated probe job for package imports or GPU checks that depend on the producing environment.

Check:

- modules import;
- expected Python is used;
- packages resolve from expected locations;
- GPU/device is visible;
- no local package shadows another package;
- environment variables are effective.

### L1 — Configuration only

Load configuration without running the pipeline.

Record a sanitized effective configuration:

- model;
- dataset;
- paths;
- enabled stages;
- seed;
- device;
- checkpoint;
- output directory;
- important defaults.

### L2 — Data load and schema only

Load the smallest representative sample.

Record:

- shape;
- columns;
- dtypes;
- identifier uniqueness;
- ordering;
- timestamp range and units;
- missingness;
- target/exposure availability;
- split membership.

### L3 — Independent track/component smoke tests

Run only the relevant independent track or component through a stage-specific Slurm job. The runtime tracks are preprocessing (P), STraTS from precomputed PKLs (S), and the causal pipeline (C).

Important comparison:

```text
Direct subproject execution succeeds
Router-mediated execution fails
```

This is strong evidence of an integration defect.

If direct execution also fails, determine whether the problem is:

- current environment;
- current data/artifact;
- a post-merge internal modification;
- a latent bug.

### L4 — Boundary test

Run the producer only, validate its output, then run the consumer only.

Examples:

- predictive preprocessing → predictive model;
- predictive inference → exported prediction artifact;
- exported predictions → causal preprocessing;
- causal preprocessing → estimator;
- estimator → result export.

### L5 — Cross-track micro-sample

Use only when separate Track P, S, and C checks plus handoff validation cannot establish the active integration claim. Prefer chaining named artifacts over recomputation. Record an execution justification first.

### L6 — Representative run

Requires explicit author approval after L-1 through L5 have passed or have been shown insufficient.

### L7 — Monolithic full pipeline run

Requires explicit author approval. Use only when a final scientific, equivalence, reproducibility, or one-command orchestration claim cannot be validated from the three independent tracks and their explicit handoffs.

## 16.5 Instrumentation policy

Instrumentation must be minimal and removable or deliberately retained as structured logging.

Allowed temporary evidence:

- assertions;
- shape/schema logging;
- effective path logging;
- configuration logging;
- artifact hash logging;
- timing.

Do not print sensitive rows or complete records.

## 16.6 Exit criteria

D2 is complete when:

- at least one failure is reproducible at the cheapest sufficient level, including a valid static/contract reproduction where appropriate;
- the smallest known reproduction is recorded;
- direct-versus-router behavior is known for the relevant component;
- the failure has a primary category;
- at least one hypothesis has a falsifying test;
- no fix is accepted merely because an untracked experiment happened to pass.

Readiness wording:

```text
READY FOR STAGE D3 — FAILURE REPRODUCED AND CLASSIFIED
```

---

# 17. Stage D3 — Build contract and regression-test infrastructure

## 17.1 Objective

Convert the identified failure and integration assumptions into executable tests.

## 17.2 No-execution and synthetic tests

Prefer tests that can run without private data:

- import tests;
- CLI parsing tests;
- configuration propagation tests;
- relative-path tests;
- execution-from-non-root-CWD tests;
- serialization round trips;
- model-name mapping;
- synthetic schema tests;
- identifier alignment;
- timestamp ordering;
- tensor/array shape contracts;
- empty or single-row edge cases;
- mocked orchestration;
- artifact-name tests.

## 17.3 Narrow server-local and Slurm probe tests

Use sanitized, tiny fixtures or locally generated fixtures for:

- real data schema;
- real checkpoint compatibility;
- actual prediction export;
- actual causal ingestion;
- GPU-specific behavior;
- package/driver interactions;
- representative sample behavior.

A private-data test may stay server-local if committing the fixture is unsafe. If it depends on project packages, container mounts, GPU behavior, or the producing environment, execute it as a minimal Slurm probe rather than directly in the Codex shell. Its command, script, environment fingerprint, and result must still be recorded.

## 17.4 Test requirements

A regression test must:

- fail on the defective state;
- pass after the intended fix;
- represent the named contract;
- avoid asserting irrelevant implementation details;
- be deterministic where possible;
- not depend on a full expensive run unless no smaller test exists.

## 17.5 Fixture policy

Fixture priority:

1. synthetic fixture;
2. generated schema-equivalent fixture;
3. tiny de-identified fixture approved for repository use;
4. server-local private fixture.

## 17.6 Exit criteria

D3 is complete when:

- the active failure has an automated or precisely scripted reproduction;
- important contracts have tests or a documented reason why they cannot;
- the failing test is tied to the failure ID;
- the test scope is narrow enough to identify regressions.

Readiness wording:

```text
READY FOR STAGE D4 — REGRESSION TEST ESTABLISHED
```

---

# 18. Stage D4 — Repair failures one at a time

## 18.1 Objective

Apply the smallest evidence-supported patch that restores the violated contract.

## 18.2 Bug loop

For each failure:

1. reproduce;
2. minimize;
3. classify;
4. define expected behavior;
5. add or confirm a failing regression test;
6. patch minimally;
7. run the narrow test;
8. run adjacent tests;
9. validate at the cheapest sufficient server execution level;
10. inspect the diff independently;
11. commit;
12. update the failure record;
13. advance only one validation level.

## 18.3 Root-cause requirement

The evidence report must distinguish:

- observed symptom;
- proximate cause;
- root cause;
- violated contract;
- why the patch restores that contract;
- what alternative hypotheses were rejected.

## 18.4 Minimality rule

A patch is suspicious if it:

- changes many unrelated files;
- changes both subprojects unnecessarily;
- adds silent exception handling;
- adds a fallback that hides invalid input;
- hardcodes a server path;
- removes validation;
- disables a pipeline stage;
- changes data silently;
- accepts multiple incompatible schemas without explicit normalization;
- upgrades many dependencies at once.

## 18.5 Acceptable repair patterns

Examples:

- resolve paths from a stable repository root;
- restore an omitted argument;
- preserve an old default explicitly;
- normalize one documented schema;
- sort by the required key before handoff;
- preserve identifiers through serialization;
- validate checkpoint metadata;
- invalidate stale caches;
- seed all relevant libraries;
- use an explicit adapter at the integration boundary.

## 18.6 Unacceptable repair patterns

Examples:

- broad rewrite before reproduction;
- catch-all exception and continue;
- replace missing values without scientific approval;
- drop rows silently;
- rename columns by guessing;
- change target or exposure semantics;
- regenerate accepted results before provenance is established;
- declare success because the exception disappeared.

## 18.7 Exit criteria for one bug

A bug is closed when:

- its regression test failed before and passes after;
- the relevant static, contract, or server-local reproduction passes;
- adjacent contracts pass;
- the diff is independently reviewed;
- no protected artifact changed unexpectedly;
- the failure record includes root cause and evidence;
- any behavior change is explicitly approved.

Readiness wording:

```text
FAILURE <ID> CLOSED — READY FOR NEXT FAILURE OR STAGE D5
```

---

# 19. Stage D5 — Validate three independent runtime tracks and integration boundaries

## 19.1 Objective

Demonstrate that the repaired repository works beyond narrow regression tests while avoiding an expensive monolithic run. Runtime validation is performed through three independently schedulable Slurm tracks and explicit artifact handoffs.

## 19.2 Validation sequence

### D5.1 Static, wire, and unit validation

- import-path and packaging analysis;
- unit and contract tests;
- config and CLI tests;
- path and mount tests;
- serialization tests;
- `sbatch`/shell syntax validation;
- container-image and required-path existence checks;
- lint/type checks if already part of the project.

Environment-sensitive imports or tests must run as a minimal Slurm probe inside the intended container.

### D5.2 Track P — Preprocessing validation

Validate preprocessing independently of STraTS and the causal pipeline.

Prefer this escalation:

1. static producer/consumer schema analysis;
2. synthetic preprocessing contracts;
3. narrow loader or fragment checks;
4. dataset-specific micro-run;
5. representative preprocessing job only with author approval.

Track P must:

- use a unique Slurm job, run ID, output root, and log paths;
- record raw-input identity safely;
- validate dataset-specific identifiers, time fields, ordering, missingness, and output schemas;
- produce PKLs and manifests without launching Track S or C;
- avoid overwriting the existing `processed/**` artifacts unless a later explicit promotion decision is made.

PhysioNet and MIMIC preprocessing may be separate jobs when this improves fault isolation or resource control.

### D5.3 Track S — STraTS validation from precomputed PKLs

Validate STraTS independently using explicitly selected precomputed PKL inputs.

Before submission:

- verify each PKL path and provenance status;
- perform the cheapest safe schema/metadata validation available;
- record hashes where practical;
- pin model, dataset, seed, checkpoint, and output settings;
- confirm that the job cannot invoke preprocessing.

Track S must record prediction/checkpoint artifacts, identifier order, configuration, environment, warnings, resource use, and exit status. It must not discover or replace input PKLs silently.

### D5.4 Track C — Causal-pipeline validation

Validate the causal project independently using explicitly selected, contract-checked preprocessing and predictive artifacts.

Before submission:

- identify the exact required PKL, prediction, configuration, and graph/tagging inputs;
- verify identifier, ordering, exposure, outcome, and covariate contracts;
- confirm that the job cannot invoke preprocessing or STraTS;
- select the narrowest causal component or estimator scope that answers the current question.

Track C must use a unique Slurm job and output root and must not overwrite checked thesis results or historical causal outputs.

### D5.5 Explicit handoff validation

Validate each cross-track boundary independently:

- Track P artifact → Track S input;
- Track P artifact → Track C input, where required;
- Track S predictions → Track C input;
- Track C outputs → result/manifest consumers.

For each handoff:

- name the producer artifact;
- record its path, size, hash where practical, and provenance status;
- validate schema, identifiers, ordering, units, and configuration compatibility;
- reject ambiguous directory-based artifact selection;
- confirm stale artifacts cannot be substituted silently.

### D5.6 Optional staged cross-track micro-integration

Use only when independent tracks and handoff validation cannot establish a required orchestration claim. The job should chain already validated artifacts and skip recomputation wherever supported.

Complete the execution-justification record and use one exact command, unique run ID, and isolated output root.

### D5.7 Representative track run — author approval required

Use only when cheaper validation cannot reveal scale, memory, worker, batching, artifact-collision, or stochastic defects. Approve and run one track at a time unless the defect is specifically cross-track.

### D5.8 Monolithic full run — final optional gate

A complete `--stages all` run requires explicit author approval. It is authorized only when the final thesis/paper or reproducibility claim requires demonstration of one-command orchestration and cannot be supported by the three independent validated tracks plus their handoff evidence.

## 19.3 Slurm execution matrix

Maintain a table:

| Execution ID | Track | Commit(s) | Container/env | Input scope | SBATCH script | Output root | Expected | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|

## 19.4 Exit criteria

D5 is complete when:

- static, wire, unit, and contract checks required by the active scope pass;
- Track P is validated to the level required by the preprocessing claims;
- Track S is validated independently from named precomputed PKLs to the level required by the predictive claims;
- Track C is validated independently from named artifacts to the level required by the causal claims;
- all active handoff contracts pass;
- every executed job records commits, container/environment, inputs, unique outputs, logs, and status;
- no track implicitly reruns another track;
- representative runs pass only if justified and approved;
- a monolithic full run passes only if it was separately required and approved;
- no unresolved failure is hidden by retries, stale artifacts, or fallbacks.

Readiness wording:

```text
READY FOR STAGE D6 — INDEPENDENT RUNTIME TRACKS AND HANDOFFS VALIDATED
```


# 20. Stage D6 — Validate output equivalence and scientific contracts

## 20.1 Objective

Confirm that runtime success did not silently change the scientific computation.

## 20.2 Baseline sources

Use, in priority order:

1. previously checked result packets;
2. historical artifacts tied to a known commit/configuration;
3. accepted run summaries;
4. reproducible pre-merge execution;
5. author-confirmed expected behavior.

## 20.3 Comparison levels

### Structural equivalence

Compare:

- artifact presence;
- filenames;
- schemas;
- shapes;
- identifiers;
- ordering;
- sample counts;
- split counts.

### Configuration equivalence

Compare:

- model;
- estimator;
- dataset;
- feature set;
- target;
- exposure;
- seed;
- checkpoint;
- hyperparameters;
- sampling condition.

### Numerical equivalence

Compare:

- exact values where deterministic;
- tolerance-based values where floating-point or stochastic variation is expected;
- distributional summaries where exact order is not meaningful.

### Scientific equivalence

Confirm:

- target meaning unchanged;
- exposure meaning unchanged;
- population unchanged;
- outcome unchanged;
- estimator hierarchy unchanged;
- exclusions unchanged;
- aggregation unchanged;
- sign conventions unchanged;
- interpretation boundary unchanged.

## 20.4 Tolerance policy

Do not invent a tolerance.

For each comparison, record:

```text
Metric
Baseline value
Current value
Absolute difference
Relative difference
Tolerance
Why this tolerance is valid
Pass/fail
```

Tolerance may come from:

- deterministic expectation;
- numerical precision;
- repeated-run variability;
- prior accepted validation policy;
- domain-approved threshold.

If no valid tolerance exists, mark the comparison unresolved.

## 20.5 Stochastic validation

For stochastic components:

- fix seeds where feasible;
- repeat runs when needed;
- record variability;
- compare distributions or confidence ranges;
- do not require exact byte equality unless the pipeline is designed to be deterministic.

## 20.6 Exit criteria

D6 is complete when:

- structural and configuration equivalence are established;
- important numerical differences are within justified tolerances;
- scientific constructs are unchanged or explicitly approved;
- checked result packets remain protected;
- unresolved differences are visible rather than hidden.

Readiness wording:

```text
READY FOR STAGE D7 — OUTPUT AND SCIENTIFIC CONTRACTS VALIDATED
```

---

# 21. Stage D7 — Reproducibility and execution hardening

## 21.1 Objective

Make the validated pipeline understandable and repeatable by a future user or agent.

## 21.2 Required durable documentation

Document:

- supported environment;
- setup;
- exact entry point;
- required data roots;
- required artifact roots;
- configuration;
- execution order;
- sample smoke-test command;
- representative/full command;
- expected outputs;
- failure diagnostics;
- cache invalidation;
- checkpoint requirements;
- known non-determinism;
- resource expectations;
- privacy restrictions.

## 21.3 Documentation placement

Before creating files:

1. inspect existing `README.md`, `AGENTS.md`, and workflow docs;
2. update canonical files;
3. create a new file only when it has a distinct durable role.

Possible structure:

```text
debugging/
  baseline.md
  integration_contracts.md
  failure_register.md
  validation_matrix.md
  final_debug_report.md
```

Do not create this exact structure if the repository already has a canonical alternative.

## 21.4 Environment record

Record actual producing environment separately from intended dependencies.

Do not claim that `requirements.txt` proves the environment used for a successful run.

## 21.5 Clean-checkout validation

Where practical:

- create a fresh worktree or clone;
- install or activate the documented environment;
- run the cheapest documented smoke or contract test sufficient to detect undocumented local state;
- verify that undocumented local state is unnecessary.

If a clean-checkout test is impossible because of data access or infrastructure, record the precise limitation.

## 21.6 Exit criteria

D7 is complete when:

- a future agent can identify the correct execution path;
- commands and configuration are explicit;
- environment provenance is recorded;
- hidden local assumptions are minimized;
- known gates are documented.

Readiness wording:

```text
READY FOR STAGE D8 — REPRODUCIBILITY PACKAGE COMPLETE
```

---

# 22. Stage D8 — Final independent audit

## 22.1 Objective

Perform an independent, repository-wide review before scientific writing resumes.

## 22.2 Reviewer requirements

Use a fresh server Codex thread or reviewer that did not implement the main fixes. Prefer a read-only review worktree for material audits. ChatGPT additionally reviews the returned evidence and readiness decision.

## 22.3 Audit checklist

The reviewer verifies:

- current HEAD and task baseline;
- complete diff from the debugging baseline;
- commit sequence;
- failure register;
- regression tests;
- static, unit, synthetic, and contract tests;
- any justified component smoke tests;
- boundary tests;
- any justified end-to-end micro-sample;
- representative/full execution only if approved and required;
- output equivalence;
- environment record;
- protected files;
- documentation;
- unresolved warnings and gates.

## 22.4 Required questions

The audit must answer:

1. Were the failures actually reproduced?
2. Were root causes identified rather than symptoms hidden?
3. Are fixes minimal?
4. Does every fix have regression coverage?
5. Are both subprojects independently validated to the level required by the active contracts?
6. Is the merged path validated at the cheapest sufficient level?
7. Are data and artifact contracts explicit?
8. Did accepted results remain protected?
9. Are numerical differences justified?
10. Can the execution be described unambiguously?
11. Are any claims still dependent on undocumented local state?
12. Is it safe to update the thesis and paper?

## 22.5 Readiness states

### Ready

```text
READY TO UPDATE THESIS AND PAPER
```

### Ready with non-blocking operational gates

```text
READY TO UPDATE THESIS AND PAPER WITH NON-BLOCKING OPERATIONAL GATES
```

Use only if the remaining gates do not affect the claims that will be written.

### Narrow repair

```text
NARROW REPAIR REQUIRED — <EXACT DEFECT>
```

### Blocked

```text
BLOCKED BEFORE THESIS/PAPER UPDATE — <REASON>
```

---

# 23. Stage D9 — Update thesis and paper

## 23.1 Entry condition

Do not begin D9 before D8 explicitly authorizes it.

## 23.2 Thesis updates

Update only evidence-supported statements about:

- repository architecture;
- execution order;
- entry points;
- configuration;
- environment;
- preprocessing;
- predictive-to-causal handoff;
- reproducibility;
- limitations;
- exact commands where academically appropriate.

Do not retroactively claim that a repaired implementation was the historical producing implementation unless provenance proves it.

Distinguish:

- historical code;
- repaired current code;
- producing code for archived results;
- validated reproduction code.

## 23.3 Paper updates

The paper requires stricter concision but the same evidence boundaries.

Do not claim:

- full reproducibility if only sample execution was validated;
- unchanged results without equivalence evidence;
- clinical validation;
- causal validity beyond the supported design;
- historical environment certainty when unavailable.

## 23.4 Final writing gate

Before accepting thesis or paper edits, verify:

- code commit referenced;
- commands referenced;
- environment provenance;
- result provenance;
- no contradiction with checked results;
- no claim stronger than the debug evidence.

---

## 24. Model and reasoning-effort policy

Model names and availability change. The stable rule is to select by task complexity, ambiguity, and risk.

### 24.1 Current snapshot

As of the freeze date, official Codex documentation recommends the current frontier coding model for most Codex tasks and supports configurable reasoning effort. The exact model shown in the VS Code picker may differ by plan, rollout, or later product changes.

Therefore:

- inspect the available model picker at the beginning of a stage;
- select the strongest generally available coding model for cross-project reasoning;
- use a faster/lower-cost available coding model for mechanical tasks;
- do not block the workflow because an old model name is unavailable;
- record the actual model and reasoning effort in each stage report.

Official reference points at the freeze date:

- Codex CLI features: `https://developers.openai.com/codex/cli/features`
- Codex configuration: `https://developers.openai.com/codex/config-sample`
- Codex changelog: `https://developers.openai.com/codex/changelog`

### 24.2 Capability classes

Use the following stable capability classes.

#### Class F — Fast coding model

Use for:

- file inventory;
- targeted search;
- mechanical formatting;
- simple test implementation after expected behavior is known;
- small renames;
- updating ledgers;
- running known commands;
- summarizing deterministic output.

Default reasoning:

```text
low or medium
```

#### Class S — Strong coding and reasoning model

Use for:

- architecture mapping;
- multi-file analysis;
- Git history comparison;
- root-cause analysis;
- integration-contract design;
- patch design;
- complex test design;
- scientific-output equivalence review;
- independent audit.

Default reasoning:

```text
high
```

#### Class P — Parallel or multi-agent mode

Use only for genuinely separable investigations, such as:

- environment investigation;
- history investigation;
- schema investigation;
- independent review.

Requirements:

- separate worktrees or read-only scopes;
- no overlapping file ownership;
- one coordinator consolidates findings;
- results are hypotheses until independently verified.

### 24.3 Reasoning-effort selection

#### Low

Use only when:

- the task is mechanical;
- expected output is unambiguous;
- risk is low;
- no architecture decision is involved.

Examples:

- list paths;
- update a status table;
- apply a known one-line rename;
- run an existing test.

#### Medium

Use for:

- focused code reading;
- implementing a known test;
- simple patch review;
- deterministic config inspection;
- straightforward error localization.

#### High

Use for:

- architecture and history analysis;
- multiple plausible hypotheses;
- integration root-cause analysis;
- patch design across boundaries;
- test strategy;
- output-equivalence analysis;
- final audit.

#### Maximum available

Use only when:

- high effort leaves multiple materially different explanations;
- the defect crosses both projects and runtime layers;
- behavior is intermittent;
- logs are incomplete;
- scientific meaning may have changed;
- a wrong fix would invalidate results;
- the final audit detects an unresolved contradiction.

### 24.4 Escalation rule

Start with the lowest effort appropriate for the risk, then escalate:

```text
Focused task at medium
    ↓ unresolved material ambiguity
Strong model at high
    ↓ cross-project, non-deterministic, or scientific-risk problem
Strongest available model at maximum effort
```

Do not use maximum effort to compensate for:

- an overly broad prompt;
- missing reproduction;
- unfiltered logs;
- unclear scope;
- absent expected behavior.

### 24.5 Recommended task mapping

| Task | Capability | Effort |
|---|---|---|
| Inventory and grep | F | Low/Medium |
| Baseline collection | F | Medium |
| Architecture map | S | High |
| Pre/post-merge comparison | S | High |
| Reproduce a known command | F or S | Medium |
| Analyze ambiguous logs | S | High |
| Design contract tests | S | High |
| Implement a known small test | F | Medium |
| Root cause spanning both projects | S | High/Maximum |
| Environment mismatch | S | High |
| Non-deterministic failure | S | Maximum |
| Minimal patch review | S | Medium/High |
| Scientific output equivalence | S | High/Maximum |
| Final independent audit | S in fresh thread | High/Maximum |

---

## 25. Thread and context policy

## 25.1 One primary objective per Codex thread

Use separate threads for:

- baseline and architecture;
- one specific failure;
- independent patch review in a fresh server thread;
- final audit in a fresh server thread.

Do not keep using one enormous thread for every failure.

## 25.2 Starting a new thread

Every new thread receives:

- this canonical plan;
- current HEAD;
- task baseline;
- branch;
- current stage;
- failure ID if applicable;
- exact objective;
- allowed files;
- forbidden files;
- commands already run;
- evidence already known;
- expected readiness wording.

## 25.3 Avoid context contamination

A repair thread must not be asked to simultaneously:

- redesign the project;
- update the thesis;
- investigate unrelated warnings;
- optimize performance;
- clean the repository.

## 25.4 Fresh independent review

Use a fresh thread for review so that it does not inherit the implementer's assumptions.

---

## 26. Handoff protocol between server threads

## 26.1 Coordinator-to-implementing-thread packet

```text
Task ID:
Stage:
Current commit:
Branch/worktree:
Failure ID:
Objective:
Hypothesis:
Known evidence:
Cheapest authorized evidence level:
Exact commands authorized:
Explicitly prohibited execution levels:
Working directory:
Expected observation:
Observation that would falsify the hypothesis:
Allowed files:
Forbidden files:
Data/privacy restrictions:
Required return evidence:
Commit/push policy:
```

## 26.2 Implementing-thread-to-reviewer packet

```text
Task ID:
Base commit:
Patch commit or uncommitted diff state:
Branch/worktree:
Environment fingerprint:
Commands run:
Execution levels used:
Execution justification, if applicable:
Observed result:
Sanitized failure or output:
Hypothesis confirmed/refuted:
Regression test result:
Files changed:
Protected-file status:
Remaining uncertainty:
Recommended next action:
```

## 26.3 Reviewer-to-coordinator packet

```text
Task ID:
Commit reviewed:
Review worktree/thread:
Diff scope:
Evidence independently inspected:
Tests independently inspected or rerun:
Execution-budget compliance:
Minimality assessment:
Protected-file assessment:
Unresolved risks:
Readiness decision:
Exact narrow repair, if required:
```

## 26.4 Writer-ownership handoff

A writer handoff must include:

- base commit;
- current branch/worktree;
- patch commit or exact preserved diff state;
- file ownership scope;
- test command;
- server result;
- known limitations;
- confirmation that the previous thread is no longer editing the same scope.

---

## 27. Standard Codex prompt contract

Every substantial Codex prompt should contain:

```text
Task identity
Canonical plan reference
Current HEAD
Task baseline
Pre-merge/reference baseline
Intervening-commit classification
Current stage
Objective
Known evidence
Hypotheses
Allowed tools and execution
Cheapest authorized evidence level
Execution-justification requirement
Forbidden execution
Data/privacy boundary
Protected paths
Required inspection
Required changes
Allowed files
Forbidden files
Validation commands
Evidence report requirements
Readiness wording
Commit/push policy
```

A prompt must be narrow enough that Codex cannot reasonably interpret it as permission to rewrite the project.

---

## 28. Standard failure report template

````markdown
# Failure F-XXX

## Summary

## Current state
- Commit:
- Branch:
- Environment:
- Working directory:

## Reproduction
```bash
<exact command>
```

## Input
- Sample/artifact:
- Data scale:
- Hash or safe identifier:

## Expected behavior

## Observed behavior

## Sanitized evidence

## Classification

## Hypotheses

## Minimal falsifying test

## Root cause

## Violated contract

## Repair

## Regression test

## Server validation

## Output-equivalence impact

## Files changed

## Protected files

## Remaining uncertainty

## Status
````

---

## 29. Standard stage evidence report

```markdown
# Stage D<X> Evidence Report

## Objective

## Current HEAD

## Task baseline

## Reference baselines

## Intervening commits

## Worktree state

## Sources inspected

## Commands run

## Execution-budget compliance

## Findings

## Files changed

## Tests and results

## Server execution evidence

## Protected-file verification

## Data/privacy confirmation

## Unresolved items

## Readiness decision
```

---

## 30. Decision register

Use a durable decision register for decisions that affect future debugging.

Fields:

```text
Decision ID
Date
Question
Options considered
Decision
Evidence
Owner
Affected files/contracts
Reversal condition
```

Approved decisions already in force:

```text
Decision ID: DEC-RUNTIME-001
Date: 2026-07-17
Question: Which environment is authoritative for pipeline execution?
Decision: Use isolated Slurm jobs that launch the intended Apptainer/container environment; treat the interactive node shell as non-authoritative for pipeline runtime until proven otherwise.
Owner: Author
Reversal condition: Explicit author approval supported by verified equivalent environment evidence.

Decision ID: DEC-RUNTIME-002
Date: 2026-07-17
Question: How should expensive validation be partitioned?
Decision: Split runtime work into independent preprocessing, STraTS-from-precomputed-PKL, and causal-pipeline tracks with explicit artifact manifests and no implicit earlier stages.
Owner: Author
Reversal condition: Explicit author approval supported by evidence that a different partition is safer or necessary.
```

Examples requiring a decision entry:

- old or new default is authoritative;
- a renamed schema is accepted;
- a tolerance is approved;
- historical artifact cannot be reproduced;
- a dependency version is pinned;
- a cache invalidation rule is adopted;
- a scientific behavior change is accepted;
- a representative or full run is approved and why cheaper evidence is insufficient.

---

## 31. Protected material

Before debugging begins, identify and protect at least:

- checked result packets;
- result manifests and checksums;
- thesis figures;
- archived run outputs;
- current thesis source;
- paper subtree;
- literature corpus;
- reproducibility records;
- prior audit logs;
- raw data;
- known historical checkpoints.

Protection may use:

- Git status;
- path allowlists;
- hashes;
- read-only permissions;
- separate output directories;
- fresh run IDs.

A debug run must not overwrite a historical artifact. Use a new debug output root.

---

## 32. Warnings and non-fatal anomalies

Warnings are evidence, not background noise.

Classify each material warning as:

- blocking defect;
- correctness risk;
- reproducibility risk;
- performance issue;
- benign;
- unresolved.

Do not silence warnings globally before understanding them.

Examples requiring investigation:

- missing checkpoint keys;
- unexpected checkpoint keys;
- implicit dtype conversion;
- unsorted index;
- dropped rows;
- convergence warning;
- deterministic-mode warning;
- cache mismatch;
- deprecated API affecting defaults;
- worker failure;
- NaN or infinite values.

---

## 33. Stopping rules

Stop the current execution and investigate when:

- data or artifacts may be overwritten;
- sensitive data may be exposed;
- the command is operating on an unexpected path;
- configuration does not match the task;
- sample size is unexpectedly large;
- the wrong environment is active;
- the run uses a different commit;
- output contains NaN/Inf unexpectedly;
- labels, exposure, outcome, or splits differ from expectation;
- an E5 representative or E6 full run was reached without explicit author approval;
- any execution is broader than the named question requires;
- the patch requires a broad scientific change;
- the agent cannot state the expected behavior.

---

## 34. Anti-patterns

Do not:

- fix before reproducing;
- use broad runtime execution when static, artifact, synthetic, or narrow checks can answer the question;
- use full runs as a general diagnostic;
- trust only the last stack-trace line;
- treat every failure as an integration bug;
- treat prior success as proof of current compatibility;
- update all dependencies at once;
- add broad fallbacks;
- suppress validation;
- drop invalid records silently;
- hardcode the server's absolute paths;
- let one server thread both implement and independently approve a material fix;
- let server execution success certify code quality;
- accept a self-authored evidence report as independent review;
- mix unrelated bugs in one commit;
- rewrite thesis text while the implementation is unsettled;
- claim historical reproducibility from a newly repaired implementation;
- optimize page or paper content before code truth is established.

---

## 35. Completion criteria for the entire debugging program

The debugging program is complete only when:

1. the baseline is recorded;
2. pre-merge references are known or explicitly unavailable;
3. the integration map is complete;
4. all material failures are in the failure register;
5. every closed bug has a regression test or documented equivalent;
6. preprocessing, STraTS from named precomputed PKLs, and the causal pipeline are independently validated to the level required by the active contracts;
7. all major handoff and integration boundaries pass contract validation;
8. every runtime job uses the verified Slurm/Apptainer path and records the parent and nested commits, container, environment, inputs, unique outputs, and logs;
9. a cross-track micro-integration passes only if it is required by the active integration claim;
10. a representative track run passes only if it was explicitly approved and necessary;
11. a monolithic full run passes only if it was explicitly approved and required for the intended thesis/paper or one-command reproducibility claims;
12. configuration and environment are recorded;
13. accepted artifacts were not overwritten;
14. output equivalence is validated with justified tolerances;
15. scientific constructs remain unchanged or changes are explicitly approved;
16. the repository has a reproducible execution guide;
17. an independent audit has passed;
18. only then is the thesis and paper update authorized.

---

## 36. Immediate next action

The current operational task is **Stage D1 static integration mapping on the server**. The D1 thread already running does not need to be restarted.

Coordinator review of the D1 report must additionally determine:

1. the exact `sbatch` → Apptainer → environment-activation path;
2. whether `clinicause`, `econml310`, or another environment is actually used inside the container;
3. which checks are safe as interactive wire checks and which require a Slurm probe;
4. how to invoke preprocessing alone;
5. how to invoke STraTS alone from explicitly selected precomputed PKLs;
6. how to invoke the causal pipeline alone from explicitly selected validated artifacts;
7. whether the current router supports those stage boundaries cleanly or needs a narrow orchestration repair;
8. the cheapest E0–E2 test before any job submission.

Do not submit a job merely because D1 finishes. After review, prepare the smallest relevant test or Slurm probe. The historical `--stages all` command remains prohibited unless it later receives explicit E6 approval.


## 37. New-conversation startup checklist

At the start of every new conversation about debugging, the coordinator must read this document and establish:

```text
Current date:
Current repository HEAD:
Current branch:
Server thread/worktree involved:
Current debugging stage:
Last completed stage:
Open failure IDs:
Latest accepted evidence report:
Protected material:
Cheapest authorized evidence level:
Authoritative runtime path and container/env status:
Active runtime track: none / P / S / C / cross-track
Next authorized action:
```

Then:

1. do not redesign the workflow;
2. inspect the latest committed state;
3. classify any intervening commits;
4. continue from the current stage;
5. issue one bounded Codex prompt;
6. require the stage's evidence report and readiness wording.

---

## 38. Canonical status block

This block should be updated as work progresses without rewriting the plan.

```text
PLAN VERSION: 1.2
CURRENT STAGE: D1
LAST COMPLETED STAGE: D0 — server baseline recorded and coordinator-reviewed on 2026-07-17
ACTIVE BRANCH: main
CURRENT HEAD: 1d838562ac7599423f0e8fd5c466caee757a8844
PRE-MERGE STRATS REFERENCE: Candidate initial integration gitlink 37478daee6d9a5140abc39df5af2e93f5209f682; last accepted standalone runtime baseline remains unknown
PRE-MERGE CAUSAL REFERENCE: Candidate initial integration gitlink d88f325c4c787235957e611c82d8f3d8f259aee5; last accepted standalone runtime baseline remains unknown
ACTIVE FAILURE IDS: None assigned; historical HADM_ID failure is a D1 investigation candidate
LAST ACCEPTED SERVER RUN: Unknown
LAST INDEPENDENT REVIEW: D0 baseline reviewed by ChatGPT on 2026-07-17; no repair audit yet
THESIS/PAPER UPDATE AUTHORIZED: No
EXECUTION BUDGET: E0–E3 preferred; E5/E6 require explicit author approval
AUTHORITATIVE RUNTIME: Provisional sbatch → Apptainer → internal environment; exact image, binds, activation, and env name pending D1 verification
RUNTIME TRACKS: P preprocessing; S STraTS from precomputed PKLs; C causal pipeline from explicit validated artifacts
MONOLITHIC PIPELINE: Prohibited by default; optional E6 only with explicit author approval
NEXT ACTION: Complete and review D1; map the container runtime and three independent track commands; submit no job yet
```

---

## 39. Final rule

> Restore and validate the implementation before describing it academically.  
> Reproduce before repairing, using the cheapest sufficient evidence.  
> Test the contract, not only the symptom.  
> Prefer static, artifact, and synthetic validation before runtime execution.  
> Run environment-authoritative checks through isolated Slurm/Apptainer jobs.  
> Validate preprocessing, STraTS from precomputed PKLs, and the causal pipeline as independent tracks before any monolithic run.  
> Run progressively, and use representative or full execution only when explicitly approved and scientifically necessary.  
> Preserve accepted evidence.  
> Require independent review.  
> Update the thesis and paper only after the code and its provenance are sufficiently clear.

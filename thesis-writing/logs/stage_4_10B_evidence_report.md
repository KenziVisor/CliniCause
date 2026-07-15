# Stage 4.10B Evidence Report — Independent Chapter 12 and Whole-Thesis Conclusion Consistency Audit

## 13.1 Repository baseline

- Current head: `46c3c87e7fad6c6f3ea01710640a3d62c238f1e7 step 4.10A`.
- Substantive Stage 4.10A commit: `212ded22e96449f944d64de364a7f57d0bfc2d6c step 4.10A`.
- Parent relationship: `46c3c87^` resolves exactly to `212ded22`; `212ded22` follows `57398329e3c0b8c681d66179e75f2bf16508529a step 4.9B`.
- Prompt-only verification: `git show --stat --oneline 46c3c87` and `git diff --stat 212ded22..46c3c87` identify only `prompt.txt`. The duplicate commit messages do not represent two substantive Chapter 12 drafts.
- Substantive-change verification: `git show --stat --oneline 212ded22` and `git diff --stat 5739832..212ded22` identify only Chapter 12, the Stage 4.10A conclusion evidence brief, the Stage 4.10A evidence report, and `main.pdf`.
- Branch: `main`.
- The Stage 4.10A report states `READY FOR STAGE 4.10B WITH NON-BLOCKING WARNINGS` and records a successful 122-page build.
- A 31-file SHA-256 baseline was created at `/tmp/stage_4_10B_protected_before.sha256` before editing.

Complete initial `git status --short`:

```text
 M README.md
 M SCRIPTS.md
 m causal-irregular-time-series
 M fix_preprocessor.py
 M prompt.txt
 M requirements-full.txt
 M requirements-router.txt
 M requirements.txt
 M router.py
 M runs/validate_demo/config/physionet_resolved_config.csv
 M tests/test_router.py
 M thesis-writing/important-md-copies/clinicause_root_project_overview.md
 M thesis-writing/important-md-copies/clinicause_root_router_usage.md
 M thesis-writing/important-md-copies/strats_project_overview.md
 M thesis-writing/literature/metadata/catalog.csv
 M thesis-writing/results/checked_cate_candidates.csv
 M thesis-writing/results/checked_cohort_candidates.csv
 M thesis-writing/results/checked_figure_candidates.csv
 M thesis-writing/results/checked_heterogeneity_candidates.csv
 M thesis-writing/results/checked_matching_failures.csv
 M thesis-writing/results/checked_matching_results.csv
 M thesis-writing/results/checked_mortality_prediction.csv
 M thesis-writing/results/checked_permutation_candidates.csv
 M thesis-writing/results/checked_predictive_exports.csv
 M thesis-writing/results/checked_predictive_metrics.csv
 M thesis-writing/results/checked_proxy_cooccurrence.csv
 M thesis-writing/results/checked_proxy_mortality_association.csv
 M thesis-writing/results/checked_proxy_prevalence.csv
 M thesis-writing/results/checked_sensitivity_candidates.csv
 M thesis-writing/results/results_manifest.csv
 M tmp_verify_router.py
```

The checked-result CSV and literature-catalog modifications are line-ending-only under `git diff --ignore-space-at-eol`; they predate this stage and were preserved byte-for-byte from the Stage 4.10B baseline snapshot. No reset, clean, branch switch, staging, commit, amend, or push operation was performed.

## 13.2 Baseline build

Commands run from `thesis-writing/thesis/`:

```bash
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

All four commands returned 0. The PDF existed at `thesis-writing/thesis/main.pdf` and contained 122 pages. The final-pass `main.log` and `main.blg`, rather than transient first-pass messages in the multi-pass transcript, showed:

- unresolved citations: 0;
- unresolved references: 0;
- duplicate labels: 0;
- Biber warnings: 0;
- Biber errors: 0;
- fatal LaTeX errors: 0;
- rerun requests: 0;
- overfull boxes: 99;
- underfull boxes: 1,149;
- nonfatal `xdvipdfmx` duplicate `@page.i` object warnings: 2.

The successful build established formatting integrity only; it was not used as evidence of scientific correctness.

## 13.3 Independent sources inspected

The conclusion set was reconstructed from the authoritative thesis and frozen result sources before the Stage 4.10A brief was used as a comparison object.

Thesis sources:

- `thesis-writing/thesis/chapters/01_introduction.tex` — objective, main RQ, SRQ-1 through SRQ-7, contribution hierarchy, and bounded findings preview;
- `thesis-writing/thesis/chapters/02_background_related_work.tex` — targeted terminology, novelty, method-boundary, proxy, and causal-language consistency inspection;
- `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex` through `09_experimental_design.tex` — targeted workflow, data-contract, proxy, prediction, DAG, matching, estimator, diagnostic, population, and provenance verification;
- `thesis-writing/thesis/chapters/10_results.tex` — complete numerical and result-hierarchy authority;
- `thesis-writing/thesis/chapters/11_discussion.tex` — complete interpretation, RQ-answer, limitation, clinical-use, ethics, and provenance authority;
- `thesis-writing/thesis/chapters/12_conclusions_future_work.tex` — audited object.

Frozen result-packet sources:

- `thesis-writing/results/results_manifest.md`;
- `thesis-writing/results/results_source_packet.md`;
- `thesis-writing/results/results_decision_register.md`;
- `thesis-writing/results/results_checksums.sha256`;
- `thesis-writing/results/checked_predictive_metrics.csv`;
- `thesis-writing/results/checked_cate_candidates.csv`;
- `thesis-writing/results/checked_matching_results.csv`;
- `thesis-writing/results/checked_matching_failures.csv`;
- `thesis-writing/results/checked_sensitivity_candidates.csv`;
- `thesis-writing/results/checked_permutation_candidates.csv`.

Audit and tracking sources:

- `thesis-writing/audit/claim_evidence_ledger.csv`;
- `thesis-writing/audit/evidence_inventory.md`;
- `thesis-writing/audit/experiment_inventory.csv`;
- `thesis-writing/audit/unresolved_questions.md`;
- `thesis-writing/audit/terminology_map.md`;
- `thesis-writing/logs/unresolved_placeholders.md`;
- `thesis-writing/logs/deferred_fixes.md`.

Comparison objects inspected after independent reconstruction:

- `thesis-writing/logs/stage_4_10A_conclusion_evidence_brief.md`;
- `thesis-writing/logs/stage_4_10A_evidence_report.md`.

No web browsing, paper download, bibliography edit, research-code inspection, or new research was needed.

## 13.4 Independent conclusion reconstruction

Before comparison with Stage 4.10A, the authoritative sources supported this conclusion set:

1. The addressed problem is an integration and evidence-boundary problem: irregular ICU records must be transformed across prediction and retrospective observational-analysis interfaces without concealing changing objects or assumptions.
2. The empirically exercised workflow comprises dataset-specific preprocessing, rule-derived proxy states, multi-label prediction, export normalization, deterministic aggregation, project-specified DAG-guided adjustment, descriptive matching, model-estimated CATE, diagnostics, and provenance tracking across PhysioNet 2012 and MIMIC-III.
3. The contribution hierarchy is integrated evidence-tracked workflow first; shared proxy/data-contract interfaces next; qualified empirical predictive and multi-estimator evaluation after them; evidence infrastructure alongside every layer. The thesis does not invent the component methods.
4. The predictive conclusion is dataset specific: STraTS led the four archived MIMIC-III test metrics and GRU-D led the four PhysioNet test metrics. No universal superiority, significance, clinical validity, or complete export lineage follows.
5. The primary model-estimated conclusion is the original-cohort CausalForestDML sign pattern: 9/9 positive in MIMIC-III and 9/10 positive in PhysioNet, with PhysioNet shock negative. These are mean model-estimated CATE summaries over analyzed samples, conditional on project assumptions.
6. LinearDML supplies secondary directional triangulation; matching is a descriptive empirical-support baseline with failures and weak-support flags; neither validates identification or positivity.
7. CausalPFN is exploratory. Its 18/19 all-three directional agreement is bounded by the PhysioNet shock disagreement, unresolved primary method source/version alignment, and absent comparable sensitivity/permutation support.
8. Interpretation-changing limitations include construct and clinical validity, cross-dataset differences, measurement and handoff error, intervention definition, graph and temporal uncertainty, possible unmeasured confounding, incomplete overlap/balance and uncertainty, estimator dependence, external/fairness/prospective/deployment limits, incomplete producing provenance, incomplete human-governed LLM records, and missing authoritative ethics/governance documentation.
9. Permitted future work follows those limitations: clinical construct validation; target-trial-aligned design; support, balance, uncertainty, and sensitivity work; handoff ablations; signed provenance manifests; external, temporal, subgroup, and prospective validation; CausalPFN verification; LLM review records; and ethics/governance completion.
10. Prohibited conclusions include diagnosis/ground-truth language, learned or validated DAG claims, unconditional causal or treatment-priority claims, estimator correctness/equivalence, clinical deployment or recommendation claims, LLM expertise/causal-discovery claims, proven positivity, and clean-checkout reproducibility.

The Stage 4.10A brief and Chapter 12 agreed with items 1-7, most of item 8, and most of item 9. The independent audit found two discrepancies:

- Stage 4.10A omitted the explicit institutional ethics/data-governance documentation limitation and its directly derived future-work action from Chapter 12, even though Chapter 11 and `DF-4.7-012` keep that gate open.
- Chapter 12 used reader-facing `commits` wording twice in provenance prose, contrary to Stage 4.10B's explicit process-language rule.

Both discrepancies were repairable within Chapter 12 and required no earlier-chapter, result-packet, code, configuration, or bibliography change.

## 13.5 Claim-audit summary

`stage_4_10B_conclusion_claim_audit.csv` contains 53 materially distinct claims with the required 15-column schema and unique claim IDs.

| Classification | Count |
| --- | ---: |
| Supported | 9 |
| Supported with qualification | 19 |
| Exploratory and correctly bounded | 2 |
| Limitations supported | 11 |
| Future work derived | 12 |
| Inconsistent | 0 |
| Unsupported | 0 |
| Repaired | 4 |

The four repaired rows are a subset of the supported limitation/future-work rows. All 53 final actions are `RETAIN` or `REPAIRED`; no unsupported or inconsistent claim remains.

## 13.6 Research-question coverage

| Research question | Authoritative answer | Chapter 12 coverage | Assessment | Action |
| --- | --- | --- | --- | --- |
| Main RQ | An evidence-tracked workflow links irregular measurements, proxy construction/prediction, aggregation, project DAGs, and adjusted analyses across both datasets, conditional on clinical and causal assumptions. | Summary, contribution synthesis, limitations, and closing perspective. | Adequate | Retain. |
| SRQ-1 | Separate causal and split-aware predictive contracts are bridged through normalized identifiers and explicit export schemas; producing lineage is incomplete. | Separate contracts and inspectable identifier/cohort/export boundaries in the contribution section; provenance gap in limitations. | Adequate | Retain. |
| SRQ-2 | Deterministic proxy states serve as labels, voter inputs, and exposures, but clinical validity remains unresolved. | Shared-interface contribution plus rule-derived, non-verified construct limitation and clinical-validation priority. | Adequate | Retain. |
| SRQ-3 | Five model families completed the archived task; the leading family differed by dataset without statistical or clinical superiority. | Explicit five-family and dataset-leader paragraph with boundaries. | Adequate | Retain. |
| SRQ-4 | Prediction outputs are normalized and may be aggregated deterministically; aggregation is not clinical consensus and can preserve error. | Workflow/shared-interface synthesis and error-propagation limitation; exact schema/tie mechanics are omitted. | Partial | Acceptable concise synthesis; no expansion needed. |
| SRQ-5 | Project-specified DAGs yield exposure-specific observed adjustment sets conditional on unresolved graph, timing, and identification assumptions. | Project-authored DAG workflow and explicit graph/temporal/unmeasured-confounding limitations; individual sets are omitted. | Partial | Acceptable concise synthesis; no result catalogue needed. |
| SRQ-6 | Primary, secondary, exploratory, matching, and diagnostic analyses show bounded directional triangulation with PhysioNet shock as the key exception. | Explicit primary forest pattern, 19/19 DML comparison, 18/19 all-three comparison, shock exception, matching role, and PFN boundary. | Adequate | Retain. |
| SRQ-7 | Construct, identification, support, modeling, transport, provenance, clinical-use, fairness, ethics, and governance limits materially bound the findings. | Limitations and all directly derived future-work priorities after repair. | Adequate | Retain repaired ethics/governance sentences. |

No misleading RQ answer or material omission remains. The two partial entries are subordinate implementation details whose full restatement would turn Chapter 12 into a second Discussion chapter.

## 13.7 Contribution consistency

Chapter 12 preserves the Introduction's hierarchy: integrated workflow first, shared proxy/data-contract interfaces next, empirical predictive and estimator evaluation after them, and evidence infrastructure as traceability support. It claims no invention of STraTS, GRU, GRU-D, TCN, SAnD, weak supervision, proxy phenotyping, DAG methods, matching, DML, causal forests, HTE estimation, sensitivity methods, or permutation testing.

The audit CSV records 27 claims as `ALREADY_ESTABLISHED` and 26 as `NOT_APPLICABLE`; it records zero `NEW_UNSUPPORTED_CLAIM` rows. Evidence infrastructure is described as improving numerical traceability, not proving clean-checkout reproduction. Hierarchy status is either `CONSISTENT` or `NOT_APPLICABLE`; no `DRIFTED` row exists.

## 13.8 Numerical validation

Every numerical or count expression in Chapter 12 is represented in the audit CSV. This includes non-result expressions such as the comment-only section ID, the dataset year, editorial priority ordinals, and the target-trial term `time zero`.

| Chapter 12 expression | Exact authority | Validation |
| --- | --- | --- |
| `C12.1` | Chapter 12 comment-only section ID. | Non-rendered identifier; no result meaning. |
| `PhysioNet 2012`; two named datasets | Dataset designation and scope in Introduction lines 19 and 30-32; Chapter 10 throughout. | Correct; not a result aggregate. |
| Five named predictive families | Chapter 10 lines 26-60, Table `tab:results-predictive-performance`; `checked_predictive_metrics.csv`, test/`PRIMARY_MAIN_TEXT` rows. | Exactly STraTS, GRU, GRU-D, TCN, and SAnD. |
| Four archived test metrics per dataset, implicit in the leader statement | Chapter 10 lines 29-31 and Table `tab:results-predictive-performance`; checked columns `loss`, `auroc`, `auprc`, `minrp`. | Programmatic comparison gives STraTS as MIMIC-III leader and GRU-D as PhysioNet leader for all four. |
| All nine MIMIC-III primary summaries positive | Chapter 10 lines 65-91 and Table `tab:results-forest-mimic`; `checked_cate_candidates.csv`, MIMIC/original/CausalForestDML. | 9/9 positive. |
| Nine of ten PhysioNet primary summaries positive; shock negative | Chapter 10 lines 103-130 and Table `tab:results-forest-physionet`; checked PhysioNet/original/CausalForestDML rows. | 9/10 positive; shock is `-0.013849200594340203`. |
| All 19 Forest/Linear original-cohort comparisons share direction | Chapter 10 lines 191-230 and Table `tab:results-linear-comparison`; joined original checked CATE rows. | 19/19. |
| All three estimators agree in 18 of 19; PhysioNet shock is the exception | Chapter 10 lines 234-281, Figure `fig:results-three-estimator-direction`, and Table `tab:results-pfn-comparison`; joined original checked CATE rows. | 18/19; shock signs are Forest negative, Linear negative, PFN positive. |
| `two datasets` in the transport limitation | Chapter 10 lines 286-291; Chapter 11 lines 65-72 and 142-147. | Correct and explicitly not pooled. |
| first/second/third priorities; `time zero` | Chapter 11 limitations and `DF-4.7-002`, `DF-4.7-008`, `DF-4.7-012`. | Editorial ordering/design terminology; not empirical result values. |

No new aggregate or value was calculated for Chapter 12. Programmatic revalidation of the frozen checked rows exactly reproduced the four required sign/count statements.

## 13.9 Result hierarchy validation

- Original cohorts: primary and explicitly named in the main adjusted-result paragraph.
- Outcome downsampling: remains robustness-only; it is not pooled with or substituted for the primary conclusion.
- CausalForestDML: primary model-estimated estimator.
- LinearDML: secondary directional comparator; no equivalence or superiority claim.
- CausalPFN: exploratory only; source/version, uncertainty, and diagnostic gaps remain explicit.
- Matching: descriptive empirical-support baseline, not independent confirmation, ATE/ATT proof, or positivity proof.
- Normalized CATE: absent from Chapter 12 and the main thesis conclusion.
- Cross-dataset pooling: explicitly rejected; similarly named constructs are not treated as automatically equivalent.
- Exposure policy: the repeated 9 MIMIC-III and 10 PhysioNet counts retain every prespecified dataset-specific exposure.

The hierarchy is unchanged. Directional agreement is never represented as a vote, equivalence, estimator correctness, interchangeable uncertainty, or causal validation. PhysioNet shock remains the visible disagreement.

## 13.10 Causal, clinical, and LLM-language validation

The thesis-wide `InterpNet|interpnet` scan across reader-facing `.tex` files returned zero matches.

The required Chapter 12 risk scan matched only manually acceptable contexts:

- `diagnos` appears within `diagnostics`/`diagnostic`, not as a claim that proxy states are diagnoses;
- `caused mortality` appears only inside the explicit negation that the estimates do not establish causation;
- causal/identification language appears only as an assumption or limitation;
- `approved corpus` and diagnostic wording do not assert proof, superiority, or validation.

Chapter 12 contains no claim of ground truth, validated phenotype, learned/discovered DAG, protective effect, treatment recommendation, deployment readiness, clinical decision support, eliminated confounding, established positivity, superior estimator, medical expertise, or LLM causal discovery. The LLM role is limited to incomplete, human-governed design provenance.

After repair, exact scans for `Stage [0-9]`, `Codex`, and `commit` return zero Chapter 12 matches. There are zero external citation commands, zero `\StagePlaceholder` commands, and zero unresolved bracketed requirement markers in Chapter 12. Its six labels are unique, all five internal references are defined, and the clean final build reports no reference problem.

## 13.11 Limitations and future-work derivation

Every future-work item maps to an established limitation:

| Future-work item | Existing limitation authority |
| --- | --- |
| Clinical review, frozen rules, and reference-label validation | Chapter 11 lines 117-124; `DF-4.7-002`. |
| Target-trial-aligned question and time-varying-confounding plan | Chapter 11 lines 126-133; `DF-4.7-008`. |
| Overlap, balance, support-aware estimands, uncertainty, multiplicity, and sensitivity | Chapter 11 lines 129-140; `DF-4.7-007`. |
| Pipeline-handoff/error-propagation ablations | Chapter 11 lines 117-124; proxy/predictive/majority-vote error and lineage records. |
| Signed data/configuration/model/artifact provenance manifests | Chapter 11 lines 149-154; `DF-4.7-004` through `DF-4.7-006`. |
| External, temporal, subgroup, prospective, safety, and impact evaluation | Chapter 11 lines 142-147 and 166-176; `DF-4.7-009` and `DF-4.7-010`. |
| CausalPFN source/version and diagnostic/uncertainty verification | Chapter 11 lines 57 and 138-140; `DF-4.7-003`. |
| Human-governed LLM prompt and review record | Chapter 11 lines 159-164; `DF-4.7-011`. |
| Authoritative institutional ethics/data-governance wording | Chapter 11 lines 166-174; `DF-4.7-012`. |

No future work is presented as completed, no unrelated speculative program is introduced, and clinical deployment is not promised.

## 13.12 Repairs performed

Four smallest-sufficient claim repairs were made in Chapter 12:

1. Added `Authoritative institutional ethics and data-governance documentation also remains required.` to the limitations paragraph. Authority: Chapter 11, Ethical and Clinical-Deployment Considerations, lines 166-174; `DF-4.7-012`.
2. Added `Authoritative ethics and data-governance wording should also be completed before prospective or deployment-related evaluation.` to Future Work. This is directly derived from repair 1 and the same authority.
3. Replaced `producing commits` with `producing source versions` in the provenance limitation.
4. Replaced `source commits` with `source versions` in the provenance-manifest future work.

Repairs 3-4 preserve the unresolved source-state/provenance meaning while removing reader-facing commit terminology required by the Stage 4.10B validation rule. No number, finding, estimator role, contribution, citation, or earlier chapter changed.

No tracking-log update was needed: the ethics/governance, provenance, clinical, and human-review issues already have precise existing entries, and their status did not change.

## 13.13 Protected-file validation

The final `sha256sum -c /tmp/stage_4_10B_protected_before.sha256` returned 0 with 31 `OK` entries and zero failures. Therefore these files remained byte-for-byte unchanged from the Stage 4.10B baseline:

- Chapters 1-11;
- all `thesis-writing/results/checked_*.csv` files;
- `results_manifest.md`, `results_source_packet.md`, `results_decision_register.md`, and `results_checksums.sha256`;
- `references.bib` and `catalog.csv`.

This validation is against the recorded initial worktree bytes, so it also proves that pre-existing line-ending-only changes in protected result/catalog files were not absorbed or altered by this task.

## 13.14 Files changed

Stage 4.10B files:

- `thesis-writing/thesis/chapters/12_conclusions_future_work.tex`;
- `thesis-writing/logs/stage_4_10B_conclusion_claim_audit.csv`;
- `thesis-writing/logs/stage_4_10B_evidence_report.md`;
- `thesis-writing/thesis/main.pdf` (generated clean-build output).

All other modified paths in the worktree were present in the complete initial status and remain unrelated. Temporary LaTeX auxiliaries were removed with `latexmk -c` after validation while retaining `main.pdf`. `prompt.txt` was not edited by this stage.

## 13.15 Final build

After all Chapter 12 repairs, the required clean-build sequence returned 0 for `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`.

- page count: 122;
- PDF SHA-256: `4e0c5dc012e696caa91188f3c74d182234fdd8b92cca913df76d61869f72060d`;
- unresolved citations: 0;
- unresolved references: 0;
- duplicate labels: 0;
- fatal errors: 0;
- Biber warnings/errors: 0/0;
- rerun requests: 0;
- overfull boxes: 99;
- underfull boxes: 1,149;
- nonfatal `xdvipdfmx` duplicate `@page.i` object warnings: 2.

The page count and layout-warning counts are unchanged from the Stage 4.10B baseline. No Chapter 12 label, reference, citation, placeholder, or process-language defect remains.

## 13.16 Remaining warnings

The following external or human-review gates remain open and were not claimed as resolved:

- supervisor ratification of the contribution/result hierarchy and final causal language;
- qualified clinical review, chart adjudication, and construct validation of proxy states and project DAGs;
- verified primary CausalPFN source, implementation-version alignment, theory, uncertainty, and diagnostics;
- exact numbered causal configurations;
- predictive split, checkpoint, export-command, and archive-copy lineage;
- raw/processed artifact hashes, producing source versions, environments, and archive history;
- dedicated overlap, support, and balance evidence;
- target-trial-aligned intervention and estimand definition;
- subgroup fairness analysis;
- external, temporal, prospective, safety, impact, and transport validation;
- complete LLM prompt-run settings and accepted/rejected human-review record;
- authoritative institutional ethics and data-governance wording;
- current administrative/title-page details and final title, abstract, keyword, and front/back-matter alignment;
- final submission-time numerical, causal-language, citation, and layout review.

These gates bound interpretation or final submission but do not require an earlier-chapter repair before the authorized front/back-matter stage.

## 13.17 Readiness decision

**READY FOR STAGE 4.10C WITH NON-BLOCKING WARNINGS**

Chapter 12 is fully supported after the four narrow repairs; every number matches the frozen checked evidence; the contribution and result hierarchies are unchanged; no unsupported conclusion remains; no earlier chapter or frozen source requires repair; the final clean build succeeds; and all protected files are unchanged. The exact next authorized task is Stage 4.10C — Final Title, Abstracts, Keywords, and Front/Back Matter Completion.

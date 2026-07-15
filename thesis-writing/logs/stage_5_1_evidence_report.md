# Stage 5.1 Evidence Report — Whole-Thesis Claim, Number, Citation, Terminology, and Front-Matter Audit

## 24.1 Repository baseline

- Verified branch `main` at `4f69df9 step 4.10C`; its immediate parent is `405f907 step 4.10B`.
- `4f69df9` changed only the authorized front matter, appendix, logs, prompt, PDF, and generated LaTeX paths. It changed no body chapter, checked result source, figure, figure register, figure generator, or graph generator.
- The Stage 4.10C report records 115 pages, zero unresolved citations/references/duplicate labels/fatal errors/Biber errors, no figure change, and `READY FOR STAGE 5.1 WITH NON-BLOCKING ADMINISTRATIVE WARNINGS`.
- The initial worktree was already dirty. Pre-existing changes comprised `README.md`, `SCRIPTS.md`, the nested `causal-irregular-time-series` repository, `fix_preprocessor.py`, `prompt.txt`, `requirements-full.txt`, `requirements-router.txt`, `requirements.txt`, `router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `tests/test_router.py`, `tmp_verify_router.py`, three files in `thesis-writing/important-md-copies/`, `thesis-writing/literature/metadata/catalog.csv`, all checked result CSVs, and `thesis-writing/results/results_manifest.csv`. Their initial bytes were preserved.
- Initial SHA-256 baselines were recorded for 30 protected evidence, literature, figure, figure-generator, and graph-generator files. Stage 4.10C and Stage 5.1 inserted or changed no figure reference; the final thesis still includes exactly five figures.
- No reset, branch switch, staging, commit, amend, push, web browsing, literature addition, experiment, result regeneration, or figure generation was performed.

## 24.2 Generated-file cleanup

The Stage 4.10C commit contained generated `main.aux`, `main.bbl`, `main.bcf`, `main.blg`, `main.fdb_latexmk`, `main.fls`, `main.lof`, `main.lot`, `main.out`, `main.run.xml`, `main.toc`, and `main.xdv`. They were used only as compiler intermediates and were removed after the final validation. Narrow thesis-local ignore rules were added for precisely those extensions. `main.pdf` remains tracked and present.

The required final `find` scan returned no auxiliary file. The files remain visible as deletions relative to the unmodified Git index because this task neither stages nor commits changes; none is retained in the working tree.

## 24.3 Baseline build

Before repairs, the mandated `latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf` sequence returned zero and produced a 115-page A4 PDF with SHA-256 `8ba56e26c745879697f15c23aba36de6a2502afe7049bd4daa98f712951d7d3f`. Citations, references, labels, Biber, glyphs, bidi processing, and fatal-error checks resolved. The baseline was warning-bearing: inherited overfull/underfull layout diagnostics, one non-fatal `biblatex` Hebrew-language fallback, and duplicate `xdvipdfmx` destination warnings were visible. Final authoritative warning counts are recorded in Section 24.18.

## 24.4 Evidence hierarchy and sources inspected

The audit used the following authorities, in decreasing order of claim-specific relevance:

- checked numerical sources: `checked_cate_candidates.csv`, `checked_cohort_candidates.csv`, `checked_figure_candidates.csv`, `checked_heterogeneity_candidates.csv`, `checked_matching_failures.csv`, `checked_matching_results.csv`, `checked_mortality_prediction.csv`, `checked_permutation_candidates.csv`, `checked_predictive_exports.csv`, `checked_predictive_metrics.csv`, `checked_proxy_cooccurrence.csv`, `checked_proxy_mortality_association.csv`, `checked_proxy_prevalence.csv`, and `checked_sensitivity_candidates.csv`;
- frozen evidence records: `results_manifest.csv`, `results_manifest.md`, `results_source_packet.md`, `results_decision_register.md`, `results_checksums.sha256`, and `figure_selection_register.md`;
- approved literature: `thesis-writing/literature/metadata/references.bib`, `catalog.csv`, and `thesis-writing/literature/README.md`;
- terminology authorities: `thesis-writing/planning/terminology_and_notation.md` and `thesis-writing/audit/terminology_map.md`;
- implementation evidence: the inspected prediction/preprocessing wrappers, `causal-irregular-time-series/src/physionet2012_causal_graph.py`, `mimiciii_causal_graph.py`, and the active causal-analysis source referenced by the source packet;
- prior audit records: Stage 4.9B literature/citation logs, Stage 4.10C evidence report, unresolved-placeholder/deferred-fix logs, and figure-validation records;
- all compiled reader-facing sources: `main.tex`, the included front matter, Chapters 1--12, and `appendices/appendices.tex`.

No web search or new literature was used.

## 24.5 Master claim audit

`stage_5_1_master_claim_audit.csv` contains 644 materially distinct reader-facing claims across 20 controlled claim types.

| Support status | Count | Required action |
| --- | ---: | --- |
| `SUPPORTED` | 224 | Retain |
| `SUPPORTED_WITH_QUALIFICATION` | 364 | Retain |
| `EXPLORATORY_CORRECTLY_BOUNDED` | 7 | Retain |
| `LIMITATION_SUPPORTED` | 35 | Retain |
| `ADMINISTRATIVE_GATE` | 14 | Blocked external input |

There are 630 `RETAIN` actions and 14 `BLOCKED_EXTERNAL_INPUT` actions. There are zero `UNSUPPORTED`, `INCONSISTENT`, `SOURCE_AMBIGUOUS`, `REPAIR`, `REMOVE`, or `MOVE_TO_TRACKING` dispositions after repair. The administrative rows concern only author/faculty/institutional facts that the repository cannot establish.

Minimal repairs removed obsolete reader-facing stage placeholders and process vocabulary, aligned Chapter 3 subquestions to the main question plus SRQ-1--SRQ-7, made the result-source language current, and stated the already-prespecified estimator/population hierarchy where it was previously implicit. No empirical value was changed.

## 24.6 Numerical audit

`stage_5_1_numeric_audit.csv` contains 963 extracted numerical expressions: 261 `RESULT_VALUE`, 64 `RESULT_COUNT`, 39 `DATASET_YEAR`, 133 `METHOD_PARAMETER`, 235 `EQUATION_OR_SYMBOL`, 80 `SECTION_IDENTIFIER`, 93 `CITATION_YEAR`, 34 `ADMINISTRATIVE_TEXT`, and 24 `EDITORIAL_ORDERING` rows. All 325 result values/counts are `MATCHED`; the other 638 rows are source-supported. No row requires repair.

Independent validation found:

- all 10 predictive model rows match the checked AUROC/AUPRC/minRP source at displayed precision;
- primary causal populations are 26,845 MIMIC-III rows and 7,993 PhysioNet rows;
- all 19 primary CausalForestDML values, all 19 LinearDML values, all 19 CausalPFN values, exposure prevalences, and signs match their checked rows;
- primary signs are positive for 9/9 MIMIC exposures and 9/10 PhysioNet exposures; PhysioNet shock is the sole negative primary value;
- CausalForestDML and LinearDML agree in direction for 19/19 original-cohort comparisons; all three estimators agree for 18/19, with PhysioNet shock retained as the disagreement;
- all 15 successful matching summaries match their pair count, rate, distance, difference, warning, and dataset/exposure row; the five failures and three weak warnings match;
- all sensitivity/permutation statements match availability/status, including ten DML permutation trials with seed 42 and intentional CausalPFN skips;
- outcome-downsampling uses 6,486 MIMIC and 2,276 PhysioNet rows at a 0.5 outcome rate; 55/57 estimator-exposure comparisons preserve direction, with exactly the two reported PhysioNet changes;
- repeated abstract, introduction, discussion, and conclusion counts match Chapter 10 and the checked grid.

No new aggregate entered reader-facing prose, and no numeric repair was needed.

## 24.7 Result hierarchy

The whole-thesis audit confirms every frozen item:

- original cohorts are primary;
- outcome-downsampled cohorts are robustness only;
- CausalForestDML is primary;
- LinearDML is the secondary comparator;
- CausalPFN is exploratory;
- matching is a descriptive empirical-support baseline;
- normalized CATE is not a main result;
- no numerical pooling occurs across datasets;
- every prespecified dataset-specific exposure is retained;
- InterpNet is excluded.

Directional agreement is never used to establish estimator equivalence, correctness, superiority, interchangeable uncertainty, valid causal identification, or treatment priority. PhysioNet shock remains visible wherever all-three agreement is summarized.

## 24.8 Research questions and contributions

`stage_5_1_rq_contribution_matrix.csv` has 14 rows: the main research question, SRQ-1--SRQ-7, and the six Chapter 1 contributions. Every row has methods coverage, checked results evidence, an evidence-bounded Chapter 11 answer, Chapter 12 coverage, and appropriate abstract coverage. All are `SUPPORTED_WITH_QUALIFICATION` / `RETAIN`.

The contributions remain integration/application/evidence-tracking contributions: end-to-end framework, shared proxy interface, cross-dataset prediction, DAG-guided multi-estimator analysis, robustness/diagnostics, and evidence infrastructure. No component method is claimed as invented, absence from the literature is not used as novelty evidence, and numerical traceability is not equated with full reproducibility.

## 24.9 Citation audit

`stage_5_1_citation_audit.csv` records 91 commands, 133 key uses, and 34 unique cited keys. All 34 are core-corpus keys, exist exactly once in the 40-entry bibliography and catalog, and are placed defensibly. There are zero undefined or malformed keys, optional/excluded citations, duplicate bibliography/catalog keys, duplicate nonempty DOI/title pairs, unresolved citations, raw bibliography keys exposed to readers, stranded citations, or unbounded uncited factual literature claims.

The cited missing-PDF entries `vincent_et_al_1996_sofa` and `ranieri_et_al_2012_berlin_ards` remain non-blocking metadata warnings; their claims are limited to conceptual grounding and do not validate local rules. Dataset papers support dataset context, model papers support canonical methods rather than local execution, causal papers support methods/assumptions rather than the project DAG or estimates, and clinical sources do not validate project-specific proxy thresholds. No citation was added or changed.

## 24.10 Terminology audit

Required spelling/capitalization is consistent for MIMIC-III, PhysioNet 2012, STraTS, GRU, GRU-D, TCN, SAnD, CausalForestDML, LinearDML, CausalPFN, DAG, DML, CATE, AUROC, AUPRC, and minRP. Proxy-state, rule-derived-label, predicted-proxy, aggregation, exposure, outcome, adjustment-variable, effect-modifier, project-specified DAG, matching-contrast, mean-model-estimated-CATE, observational-analysis, exploratory-estimator, evidence-provenance, and clean-checkout-reproducibility distinctions are retained.

Repairs standardized `CausalForestDML` where two method passages used a spaced variant; replaced stale “planned,” “frozen stage,” and “checked packet” wording with prespecified/validated scholarly language; and removed the unused `StagePlaceholder` macro and every reader-facing placeholder invocation. `LAT_*` remains only as stable implementation vocabulary. The exact required InterpNet scan returns zero.

Restricted terms such as diagnosis, ground truth, validated phenotype, ATE, ATT, latent variable, unbiased, clinical actionability, and protective effect appear only in explicit negative boundaries, implementation-name explanations, cited background, or qualified estimand language.

## 24.11 Causal and clinical language audit

The whole-source high-risk scan produced the following exact case-insensitive counts: cause 3; causal effect 2; effect 97; treatment 78; intervention 22; diagnosis 8; phenotype 6; ground truth 4; validated 28; clinical 163; actionable 4; protective 1; recommendation 4; deployment 11; positivity 16; exchangeability 8; confounding 30; proof 11; prove 14; superior 0; expert 6; discovery 3.

Every material match was reviewed. Cause/causal-effect language is attached to questions or explicit non-causal boundaries. Effect/treatment/intervention vocabulary is methodological or explicitly conditional. Diagnosis/phenotype/ground-truth/validated language either describes cited literature or denies those statuses for project proxies and DAGs. Actionability/recommendation/deployment matches deny readiness. The single protective match says the negative shock estimate must not be called protective. Positivity/exchangeability/confounding matches state assumptions, diagnostic limits, or unresolved risks. Proof/prove/unbiased/expert/discovery matches deny proof, unbiasedness, LLM medical expertise, or data-driven DAG discovery. No language-risk repair remains outstanding.

The required repository-process scan has one benign lexical match: “evidence reported” in Chapter 11 contains the search substring “evidence report” but is ordinary scholarly prose. There is no Stage number, Codex, prompt filename, claim-audit, author-freeze, repository-head, or worktree language in the thesis.

## 24.12 Abstract equivalence

`stage_5_1_abstract_equivalence.csv` contains 20 component/formal checks. The English abstract has 347 tokens and the Hebrew abstract 302 under the same source-text tokenizer; both are below 500. Neither contains a citation or footnote.

Objective, datasets, workflow, five model families, proxy boundary, DAG boundary, 9/9, 9/10, negative shock, 19/19, 18/19, exploratory CausalPFN, descriptive matching, no pooling, contribution, causal limits, clinical/deployment limits, reproducibility boundary, and future needs are semantically equivalent. Neither language adds a claim or strengthens causal/clinical meaning. Render inspection confirms intact Hebrew right-to-left flow and readable embedded MIMIC-III, PhysioNet 2012, CausalForestDML, LinearDML, CausalPFN, and checkout terms. No abstract repair was required.

## 24.13 Front matter

The English title is centralized and renders identically as `A DAG-Guided Framework for Proxy-State Effect Estimation in Irregular ICU Time Series`; its status remains provisional in tracking. No Hebrew title, author, supervisor, department, degree, approval text, date, ethics identifier, or governance statement was inferred. The administrative gates remain explicit.

The English and Hebrew keyword lists contain 15 aligned concepts each. Every abbreviation and notation entry is used in the thesis. TOC, nomenclature, list of figures, and list of tables render. Acknowledgements remain deliberately omitted because no author-approved text exists.

## 24.14 Appendix

Appendix A remains a concise scholarly statement of reproducibility and evidence boundaries. Its checked-table/manifest/checksum/source-packet/decision-register claims are supported, it does not expose raw absolute paths or repository-stage chronology, it does not imply complete clean-checkout reproduction, and it carries external data-access, governance, clinical-review, and administrative limits. No appendix repair was needed.

## 24.15 Existing figures

Exactly five pre-existing figures remain included and unchanged:

| Figure file | SHA-256 |
| --- | --- |
| `mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` |
| `physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` |
| `results_mimic_forest_original_cate_ranking.png` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` |
| `results_physionet_forest_original_cate_ranking.png` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` |
| `results_original_three_estimator_direction_agreement.png` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` |

No figure, caption, reference, selection-register row, figure generator, or graph generator changed. No excluded figure entered the thesis.

## 24.16 Files changed

Stage 5.1 changed only:

- `.gitignore`;
- `thesis-writing/thesis/main.tex`;
- Chapters `03_problem_definition_study_design.tex` through `11_discussion.tex` except no change to Chapters 1, 2, or 12;
- `thesis-writing/thesis/main.pdf`;
- the five Stage 5.1 CSV ledgers and this evidence report;
- deletion of the twelve generated auxiliary files listed in Section 24.2.

No front-matter source, appendix source, figure, literature, planning, audit, checked result, manifest, source packet, decision register, checksum, code, configuration, requirement, router, test, prompt, or nested-repository file was changed by this stage. Pre-existing unrelated dirty files were not normalized or repaired.

## 24.17 Protected-file validation

Final SHA-256 comparison passed for all 30 protected files: 14 checked CSVs, the six frozen evidence/figure-register records, bibliography, catalog, five included figures, the main-figure generator, and both causal-graph generators. Result: `protected_files=30`, `changed=0`. The nested repository's pre-existing unrelated modification remained outside the graph scripts.

## 24.18 Final build and render

The final clean command sequence returned zero: `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`. It produced a 113-page A4 PDF with SHA-256 `4c5577ecfc5465818ed025519b9535949c1731f31b27bed344032fa801381bc2`.

Final checks: unresolved citations 0; unresolved references 0; duplicate source labels 0 among 110 labels; fatal errors 0; Biber errors 0; Biber warnings 0; missing-glyph/font warnings 0; bidi warnings/errors 0; rerun warnings 0. Non-blocking diagnostics are 103 overfull boxes, 1,159 underfull boxes, one `biblatex` warning that Hebrew language definitions are unavailable and dummy definitions are used, and 26 `xdvipdfmx` duplicate-destination warnings. The latter are PDF destination-name warnings (`page` and table destinations), not duplicate LaTeX labels or unresolved cross-references.

Rendered inspection covered both title pages, Hebrew abstract, English abstract, keywords, TOC, abbreviations, notation, lists, Chapter 1 opening, Chapter 10 opening/predictive/primary/matching/comparator pages, Chapter 11 research-question and limitations pages, Chapter 12, appendix, and bibliography transition. Text is present and legible, tables remain within the intended evidence hierarchy, Hebrew/Latin direction is intact, and no blank, clipped, or malformed audited page was found. After inspection, `latexmk -c` removed all auxiliaries while retaining the validated PDF and its hash.

## 24.19 Remaining gates

The following external or later-stage gates remain: supervisor ratification; clinical review; CausalPFN source/version; raw/configuration/split/checkpoint/source/archive provenance; overlap/balance; fairness; external/prospective validation; LLM human-review provenance; ethics/governance wording; title and English-thesis approval; official administrative details; acknowledgements; current faculty forms; and detailed external figure correctness review in Stage 5.2.

## 24.20 Readiness decision

READY FOR STAGE 5.2 WITH NON-BLOCKING WARNINGS

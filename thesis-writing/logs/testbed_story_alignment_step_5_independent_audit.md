# Testbed Story Alignment — Step 5 Independent Audit and Final Repair

This is an intentional early-stop report. On 2026-08-03, after the baseline audit and mandatory lead planning were complete but before thesis-source editing began, the user requested that Step 5 finish early with a report of what remains. Accordingly, this report records verified findings, completed planning, and every material unfinished gate. It does **not** claim that Step 5 repairs or final validation were completed.

## 1. Baseline

- Expected HEAD: `eba841dbcb7fc63f89f903e6b94a5be0f46f0f65`.
- Actual HEAD: `eba841dbcb7fc63f89f903e6b94a5be0f46f0f65` — pass.
- Branch: `main`.
- Initial and pre-report worktree status contained six pre-existing user-owned modifications: `prompt.txt`, three clinical-evidence-supplement CSV files, and the two mortality-voter CSV files. They were not modified by Step 5.
- The 22-file active-thesis-source baseline manifest and 65-file paper-tree baseline manifest both pass `sha256sum -c` at early stop.
- Key protected hashes remain:
  - tracked thesis PDF: `6f25ac51acdcc091518371dcf46d73b43d0e2e4634f3da19e9458ba133c88020`;
  - root paper source: `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6`;
  - pipeline figure: `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`;
  - thesis shock figure: `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`;
  - Step 4 derived statistics: `c2efb00f64d901fe1635221ee032155900b7f7ac369ecf0facb56358d88c7aea`.
- A clean baseline was built at `/tmp/clinicause-step5-baseline.3bg3zw` using XeLaTeX, Biber, XeLaTeX, XeLaTeX. All four commands exited successfully.
- Clean baseline PDF: 120 A4 pages; SHA-256 `d91a3bce7e7aee5a6701cfbc5b2d640dd3f12e851abd1f49ed9a012c5f776b70`.
- The clean and tracked PDFs differ in metadata/font-subset bytes, but their extracted layout text and all 120 rendered 200-dpi pages are identical. Extracted-text SHA-256: `0424cc7bcc98bf60afc27543180f9d92e65efcd0f19716f59f944a48af445866`.
- Baseline page budget: front matter 14; Chapters 1--11 respectively 8, 16, 5, 4, 9, 5, 11, 8, 16, 10, and 3; Appendix 4; bibliography 6; Hebrew cover 1.
- Baseline citations: 55 unique emitted keys, 94 citation commands, 137 cited-key appearances, and 62 raw bibliography entries.
- Baseline warnings: one expected `biblatex` Hebrew-localization warning; nine bounded overfull boxes, maximum 9.51868 pt; one visually harmless bibliography underfull box, badness 1019. There are no undefined citations/references or rerun warnings.

## 2. Ultra and Subagent Execution

Six independent first-wave roles completed before any thesis-source edit:

- A — scientific story, RQ/SRQ alignment, terminology, causal language: `/tmp/step5_wave1_A_science.md`.
- B — numerical and evidence integrity: `/tmp/step5_wave1_B_numbers.md`.
- C — redundancy and page budget: `/tmp/step5_wave1_C_redundancy.md`.
- D — LaTeX/layout audit and individual inspection of all 120 baseline pages: `/tmp/step5_wave1_D_layout.md`.
- E — Hebrew and administrative audit: `/tmp/step5_wave1_E_hebrew_admin.md`.
- F — citation minimization, bibliography, and source authority: `/tmp/step5_wave1_F_citations.md`.

The roles ran in batches under the four-slot concurrency limit. After all six reports returned, the lead created the four required pre-edit documents:

- `/tmp/step5_unified_issue_matrix.md`;
- `/tmp/step5_chapter_page_budget.md`;
- `/tmp/step5_citation_retention_matrix.md`;
- `/tmp/step5_two_pass_compression_plan.md`.

Lead resolutions included retaining all three Results figures despite a compression proposal, enlarging rather than compressing the DAGs, selecting the preferred 38-key bibliography rather than the 35-key minimum, and pruning clinical evidence only when its inseparable number/range would also be removed. A supplemental backup citation audit was stopped when the primary F report completed and then became unnecessary under the user's early-stop instruction.

No second-wave verifier was started. That entire wave remains missing. No unavailable utility affected the baseline: XeLaTeX, Biber, qpdf, PDF text/font inspection, and 200-dpi rendering were available.

## 3. Independent Findings

Blocking if left unresolved in a final author-review artifact:

- CausalPFN is implemented but its primary key `balazadeh2025causalpfn` is not cited. The primary source is locally available; only exact producing implementation/version lineage remains unresolved.
- Chapter 2 line 31 requires the mandated phrase `source-observed mechanisms` and the thesis more broadly must stop classifying representation-induced cohort, proxy prevalence, and support as source-observed.
- Citation pruning, final build, all-page final rendering, three independent verifier audits, and equality between the validated build and tracked `main.pdf` were not performed.

Major findings:

- The Introduction, Background, Results synthesis, Discussion, and Conclusions repeat substantial material.
- The bibliography can defensibly move from 55 to 38 emitted keys while retaining all essential primary authorities and balanced clinical evidence.
- Several claims overstate internal checks as validation, replication, or causal evidence.
- LoF/LoT spills, two orphan chapter tails, one isolated Results float, and an Appendix spill account for approximately six high-confidence pages.

Moderate findings:

- DAG labels are too small in portrait placement and should be placed landscape at readable width.
- Hebrew terminology needs several high-confidence repairs and the keyword heading needs explicit RTL treatment.
- Nine local overfull boxes should be repaired without global typography changes.

Minor findings include publication-irrelevant acquisition notes printed in bibliography entries and inconsistent uses of `validated`, `effect`, and `reusable`.

False alarms or rejected proposals:

- All three Results figures are readable and scientifically useful; they should not all be deleted merely because values also appear in tables.
- Existing landscape longtables, chapter-start spacing, institutional leaves, and baseline font sizes are acceptable.
- The expected Hebrew-localization warning is non-fatal.

Deliberately deferred issues require human authority: official title/degree/department wording, names, supervisor approval, dates, signatures, forms, English-thesis authorization, required final page order, acknowledgements, native academic-Hebrew review, and institutional deposit rules.

## 4. Scientific Coherence Audit

The baseline contribution hierarchy passes: two dataset-specific observational testbeds are primary; the representation-centered framework is enabling; checked numerical/provenance artifacts are supporting. The main RQ and all five SRQs are present verbatim and aligned with the chapter structure. Chapter 1 contains zero occurrences of `MIMIC-IV`, as required.

Controlled-benchmark complementarity is scientifically sound: controlled benchmarks supply a measurable answer under specified mechanisms, while these observational testbeds expose estimator behavior and fragility under realistic but causally unresolved records. The required repair is terminological precision: source-recorded measurements, availability, covariates, care traces, and outcome must be separated from representation-defined cohort, proxy labels, cutoffs, prevalence, and support.

The five SRQs remain correctly scoped. SRQ-3 needs one explicit asymmetric answer: proxy recoverability is assessed in both corpora, but mortality relevance is reported only for MIMIC; PhysioNet mortality performance remains withheld. The phrase `five analytical tasks` should be renamed so it is not confused with the five SRQs.

The unimplemented Chapter 2 correction is to use `source-observed mechanisms` at line 31 and revise surrounding sentences that overextend `source-observed`. Causal language still needs narrowing from effects/validation/reproducibility to adjusted or model-estimated contrasts, checked artifacts, workflow portability, and the exact evidence class available.

Remaining repetition is concentrated in Chapter 1's background/method/limitation recaps, Chapter 2's catalogs and duplicate tables, Chapter 3 and Chapter 6 orphan tails, Results overview tables, the first half of Discussion, and Conclusions. None was edited because of the early stop.

## 5. Numerical and Evidence Audit

The independent numerical audit passed without unexplained drift. The frozen cohort/exposure counts remain MIMIC 26,845 with 9 exposures and PhysioNet 7,993 with 10 exposures. Four predictive model families and the one-rule-plus-four-predicted label contract remain unchanged. The MIMIC predictive metrics were checked against Step 4 artifacts; PhysioNet mortality AUROC remains withheld.

The estimator hierarchy remains Forest primary, Linear secondary, PFN exploratory. All 19/19 Forest--Linear directions agree; all three estimators agree for 18/19, with PhysioNet shock retained as the sole exception. Rank, RMSE, Spearman-correlation, matching, outcome-downsampling, permutation, and sensitivity statements were independently recomputed or traced to admitted Step 4 artifacts. The `|z|>2` permutation rule remains a heuristic flag, not a p-value or formal randomization test. Datasets remain separate; no pooled estimate was introduced. No unified omitted-variable-sensitivity number was inserted.

The clinical-comparison table retains direct citations for every external number in the unchanged baseline. The planned pruning would remove exactly 17.9, 9.1, 8.9, 15.3, and 10.2--21.0 together with their sources, while retaining one cited comparator for renal, hepatic, cardiac, inflammation, shock, coagulation, respiratory, neurologic, and metabolic constructs; global severity would retain no numerical comparator. That pruning was not executed.

All tables, formulas, thresholds, DAG counts, adjustment sets, figures, abstracts, conclusions, and appendix claims remain at their baseline values because no active thesis source was changed.

## 6. Compression Plan and Execution

The unified matrix accepted, but did not execute, these candidates:

| Matrix IDs | Planned action | Planned saving | Citation consequence | Risk | Final action |
|---|---|---:|---:|---|---|
| U-01, U-05--U-08 | Repair evidence taxonomy, causal language, SRQ-3 wording, reuse qualification, and CausalPFN authority | 0--1 page | +1 PFN before pruning | Low--medium | Not executed; early stop |
| U-02--U-04 | Compress Introduction, Background, and Discussion around canonical locations | 7--10 pages | remove repeated appearances and overlapping keys | Medium | Not executed; early stop |
| U-09--U-11, U-13 | Merge two orphan tails, repair Appendix spill, shorten list captions, and place the direction figure normally | about 6 pages | none | Low | Not executed; early stop |
| U-14, U-27 | Enlarge DAGs landscape and clear local overfull boxes | 0 pages | none | Low | Not executed; early stop |
| U-15--U-17, U-19--U-20 | Remove duplicate Background/robustness overviews and compact Results/Chapter 7 repetition | 4--7 pages | fewer repeated appearances | Low--medium | Not executed; early stop |
| U-21--U-23 | Apply 38-key plan, balanced clinical pruning, and bibliography-note cleanup | 1--2 bibliography pages | net -17 unique keys | Medium | Not executed; early stop |
| U-24 | High-confidence Hebrew and RTL repairs | 0 pages | none | Medium | Not executed; early stop |

Rejected candidates remain rejected: U-12 deleting all three Results figures; U-18 merging/deleting estimator tables; U-28 global typography or institutional-page compression. U-25, U-26, and the associated administrative questions remain deferred to humans.

The planned first pass targeted approximately 104 pages. A second pass was authorized only if a validated first-pass PDF remained above 108 pages, and would have removed three optional benchmark-context passages/keys before any more aggressive prose reduction. Neither pass occurred.

## 7. Page Budget

Because no thesis source changed and no final build was performed, there is no after-build page budget. The tracked baseline remains 120 pages.

| Component | Before | Planned target | Validated after |
|---|---:|---:|---:|
| Front matter | 14 | 12 | Not produced |
| Chapter 1 | 8 | 7 | Not produced |
| Chapter 2 | 16 | 12 | Not produced |
| Chapter 3 | 5 | 4 | Not produced |
| Chapter 4 | 4 | 4 | Not produced |
| Chapter 5 | 9 | 9 | Not produced |
| Chapter 6 | 5 | 4 | Not produced |
| Chapter 7 | 11 | 11 | Not produced |
| Chapter 8 | 8 | 7 | Not produced |
| Results | 16 | 14 | Not produced |
| Discussion | 10 | 8 | Not produced |
| Conclusions | 3 | 3 | Not produced |
| Appendix | 4 | 3 | Not produced |
| Bibliography | 6 | 5 | Not produced |
| Hebrew cover | 1 | 1 | Not produced |
| **Total** | **120** | **104** | **Not produced** |

The preferred 96--108-page band was not reached. No quality override is asserted because there is no post-edit PDF to evaluate.

## 8. Citation Reduction

- Baseline/current unique emitted entries: 55.
- Planned final unique entries: 38.
- Actual validated final unique entries: not produced; current source remains 55.
- Planned reduction: 17/55 = 30.9%; actual reduction: 0%.
- Baseline/current citation commands: 94; planned 60--64; final not measured.
- Baseline bibliography: 6 pages; planned 4--5; final not produced.
- Planned retained roles: two dataset primaries; four predictive-model primaries; DML, forest, EconML, DAG, target-trial, intervention, overlap, and sensitivity authorities; bounded LLM/proxy authorities; three direct benchmark examples; nine direct numerical clinical comparators; one primary CausalPFN source.
- Planned removed keys: `alaa2019validating`, `anthon2023ploticu`, `arbous2024sepsis`, `athey2019grf`, `bica_2021_individualized_treatment_effects_ehr_ml`, `curth_2024_ml_individualized_treatment_effects`, `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`, `iwashyna_2015_hte_critical_care`, `jia2023sepsisaki`, `lipkovich_2024_modern_hte_methods`, `lipton_kale_wetzel_2016_missingness_rnns`, `lorenteros2020myocardial`, `parikh2022validating`, `ratner_et_al_2020_snorkel`, `saha2023ards`, `sharma_kiciman_2020_dowhy`, `shi2019dragonnet`, and `vincent_et_al_1996_sofa`. Each has a claim-level or number-level co-edit in the temporary retention matrix.
- Planned added key: `balazadeh2025causalpfn`.
- No three-key cluster is scientifically required after clause-level citation placement, but baseline clusters remain unchanged.
- Baseline contains 19 keys cited once and seven raw uncited entries. The planned final bibliography would remove six never-used entries and activate CausalPFN, leaving no raw uncited entry.
- Baseline duplicate-title and duplicate-DOI checks pass.

No claim-support confirmation can be issued for a final 38-key thesis because the pruning and final citation audit remain missing.

## 9. Clinical-Comparison Citation Decisions

The current table is unchanged. The reviewed but unexecuted plan was:

| Construct | Original comparator(s) | Planned final comparator | Planned removed value/source | Balance and qualification |
|---|---|---|---|---|
| Renal | 8.1 Jiang | unchanged | none | Broadly compatible; definitions/horizon differ |
| Hepatic | 7.4 Yang | unchanged | none | Overlapping but same MIMIC source and narrower threshold |
| Cardiac | 17.0 Babuin; 17.9 Lorente-Ros | 17.0 Babuin | 17.9/Lorente-Ros | Population/definition caveat retained |
| Inflammation | 5.0 Shankar-Hari; 9.1 Jia; 8.9 Arbous | 5.0 Shankar-Hari | 9.1/Jia and 8.9/Arbous | MIMIC remains larger/discrepant; horizons differ |
| Global severity | no defensible comparator | unchanged | none | No corroboration claim |
| Shock | 11.1 Lamontagne | unchanged | none | Discrepant; different intervention, population, and 90-day horizon |
| Coagulation | 19.5 Stephan; 15.3 Anthon | 19.5 Stephan | 15.3/Anthon | Strong discrepancy retained |
| Respiratory | 15.0 Torres; 10.2--21.0 Saha | 15.0 Torres | 10.2--21.0/Saha | Strong discrepancy and noncommensurability retained |
| Neurologic | 0.9 Klein Klouwenberg | unchanged | none | Delirium/proxy and horizon mismatch retained |
| Metabolic | 31.0 Gunnerson | unchanged | none | Unadjusted, more severe construct; discrepancy retained |

The plan removes both broadly compatible extras and discrepant extras while retaining every construct and all interpretation-changing discrepancies. It therefore does not selectively curate corroboration. Because it was not implemented, every original number still has its original direct citation.

## 10. Source Changes

The only repository file created by this early-stop turn is this report. No file under `thesis-writing/thesis/main.tex`, `frontmatter/**`, `chapters/**`, `appendices/**`, or `thesis-writing/literature/metadata/references.bib` was changed. No table, figure, cross-reference, citation, abstract, or conclusion was edited. No repetition was removed. No material was lost.

The missing source changes are exactly those summarized in Sections 3, 4, 6, 8, 9, and 11.

## 11. Hebrew and Administrative Audit

Scientific equivalence between the English and Hebrew abstracts passes. Both are under the 500-word limit and their 12 keyword concepts align. Baseline RTL rendering is sound, including mixed Hebrew/Latin/numeric content.

Unimplemented high-confidence repairs include: standardizing the Hebrew observational-testbed term; replacing a literal counterfactual sentence; improving the terms for omitted confounding, diagnostics, provenance, proxy exposures, contextual clinical-literature comparison, and secondary comparator; and placing the Hebrew keyword heading in explicit RTL context.

Native academic-Hebrew review remains required. Unresolved institutional actions include authoritative title/name/supervisor/degree/department/date fields, signatures and forms, approval for an English thesis, official page order, acknowledgements requirements, ethics/governance wording, and deposit-format checks. No value was invented.

## 12. Bibliography and Source-Authority Audit

The current bibliography remains at 55 emitted keys. Dataset primaries for MIMIC-III and PhysioNet 2012 resolve. Primary or appropriate authorities resolve for the four predictive families, DML, causal forest, EconML, DAG/backdoor reasoning, target-trial reasoning, overlap, and sensitivity. Direct construct sources and every retained clinical number resolve.

The unresolved final-gate issue is that the implemented exploratory CausalPFN family lacks its active primary citation even though `balazadeh2025causalpfn` already exists as a valid raw entry. The correct repair is to cite it while keeping exact producing implementation/version/checkpoint lineage unresolved.

No exact normalized-title duplicate, near-title duplicate at the audited threshold, or duplicate DOI was found. Seven raw entries are currently uncited. Several rendered `note` fields contain local acquisition/download prose inappropriate for a publication bibliography. The planned 38-key bibliography cleanup and source-to-Biber equality check remain missing.

## 13. Frozen-Content Verification

At early stop, all 22 active thesis sources and the bibliography match their pre-Step-5 manifest. The 65-file paper tree also matches its manifest. Consequently, frozen tables, formulas, thresholds, DAGs, adjustment sets, estimator hierarchy, figures, labels, citations, abstracts, conclusions, and appendices have no Step 5 drift. The six pre-existing user-modified files remain outside Step 5's edit scope and were preserved.

This is a preservation result, not a verification of proposed edits: after implementing the repairs, every frozen-content check would need to be repeated.

## 14. Final Build

No final build exists. Only the clean baseline build was completed, using:

1. `xelatex -interaction=nonstopmode -halt-on-error main.tex`
2. `biber main`
3. `xelatex -interaction=nonstopmode -halt-on-error main.tex`
4. `xelatex -interaction=nonstopmode -halt-on-error main.tex`

Baseline results were 120 A4 pages, qpdf pass, Biber pass with 55 entries, embedded fonts with no Type 3 fonts, and no unresolved citations/references. A post-edit build path, page count, PDF hash, extracted-text hash, qpdf result, Biber count, final citation/reference result, final font result, and final warning inventory are all missing.

## 15. Visual Review

Every baseline page was rendered at 200 dpi and inspected individually. Baseline front matter, Hebrew, figures, tables, clinical comparison, bibliography, and cover are readable. The known defects are LoF/LoT spill pages, two orphan chapter tails, one isolated Results float, the Appendix spill, and small DAG labels; no page is clipped or blank.

No changed-page review or final all-page render exists because no source changed and no final PDF was built. The planned DAG, caption, float, table, bibliography, and Hebrew repairs therefore have no visual acceptance evidence.

## 16. Independent Verification Wave

- Verifier 1 (scientific/numerical/frozen-content): not run.
- Verifier 2 (citations/source authority/clinical balance): not run.
- Verifier 3 (clean build/all-page visual/administrative structure): not run.
- Repairs made after verification: none.
- Unresolved concerns: all proposed source edits and all final gates.
- Final acceptance decision: not accepted because the user requested an early stop before implementation and verification.

## 17. Tracked Main PDF

- Previous/current hash: `6f25ac51acdcc091518371dcf46d73b43d0e2e4634f3da19e9458ba133c88020`.
- Previous/current pages: 120.
- Validated final hash/pages: not produced.
- Equality with a validated final build: impossible to establish.
- No PDF or auxiliary file was copied into the thesis tree.

## 18. Protection and Git Status

The active-source and paper-tree manifests pass. The paper tree, evidence sources, Step 4 derived-statistics file, and protected figures were not changed by Step 5. Before creation of this report, `git status --short` showed only the six pre-existing user modifications listed in Section 1.

The only task-scoped change after this report is one new file: `thesis-writing/logs/testbed_story_alignment_step_5_independent_audit.md`. The post-write task-scoped whitespace check, status check, and both protected-manifest checks pass; no thesis source or tracked PDF appears. The global worktree remains intentionally dirty because of the six user-owned modifications. Nothing was staged, committed, or pushed.

One transient helper artifact, `references.bib.blg`, was accidentally created during read-only baseline work and immediately deleted; it is absent from the final worktree.

## 19. Human Actions Before Submission

Independent of the unfinished Step 5 implementation, the following human actions remain:

- supervisor scientific approval;
- native academic-Hebrew review;
- authoritative administrative fields and institutional page order;
- ethics and governance wording review;
- signatures and required forms;
- English-thesis authorization and final deposit-format checks;
- resolution or explicit acceptance of incomplete PhysioNet mortality lineage;
- resolution or explicit acceptance of missing unified omitted-variable-sensitivity lineage;
- confirmation of the exact producing CausalPFN package/checkpoint/version and diagnostic lineage, if recoverable.

These are submission gates. They do not authorize invention of data or metadata.

## 20. Readiness

Step 5 stopped after baseline audit and lead planning. The thesis-source repairs, 38-key citation consolidation, page reduction, final build, final all-page inspection, three independent verifier audits, and tracked-PDF replacement are missing. In addition, the implemented CausalPFN method still lacks its active primary citation. These conditions meet explicit author-review blocker criteria.

BLOCKED BEFORE AUTHOR REVIEW

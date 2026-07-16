# LLM methodology integration evidence report

## 1. Repository baseline

- Repository root: `/mnt/c/Users/kobik/Desktop/הנדסת מערכות תקשורת/תואר שני/תזה/code/CliniCause`
- Branch: `main`
- Pre-edit `HEAD`: `4de62a8 adding front and back pages`
- Earlier four commits: `69041e4 step 5.6`, `8367195 step 5.5`, `3e29da1 step 5.4`, and `ad52c76 step 5.3`.
- The applicable repository, thesis, literature, reproducibility, table, and figure instructions were inspected before editing. The thesis entry point is `thesis-writing/thesis/main.tex`; the canonical bibliography and catalog are under `thesis-writing/literature/metadata/`.
- A source snapshot and a frozen pre-edit claim inventory were made before prose changes. The inventory contains 2,264 unique repository hits and has SHA-256 `315dd09f475aaddd798df34d653c9b9152a448103b3f3a4fc77a43261dda1f01`.

## 2. Pre-existing dirty state

The pre-edit short status contained 61 entries, a dirty `causal-irregular-time-series` submodule, the four untracked input PDFs under `thesis-writing/literature/new/`, and 15 ignored entries. No reset, clean, normalization, staging, commit, or push was performed.

The pre-existing changes included:

- root/router work: `README.md`, `SCRIPTS.md`, `fix_preprocessor.py`, `prompt.txt`, the three requirements files, `router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `tests/test_router.py`, and `tmp_verify_router.py`;
- the dirty `causal-irregular-time-series` submodule and existing copied project guides under `thesis-writing/important-md-copies/`;
- protected stage-5.2 and stage-5.5 audit, table-value, figure-value, and PDF-review records under `thesis-writing/logs/`;
- every already-modified checked-results CSV and `thesis-writing/results/results_manifest.csv`;
- pre-existing thesis changes to `frontmatter/administrative_metadata.tex`, `frontmatter/title_pages.tex`, and `main.pdf`.

The existing `title_pages.tex` spacing change was retained as user work. `administrative_metadata.tex` was necessarily updated for the approved Hebrew title, and `main.pdf` was necessarily rebuilt; both overlaps are distinguished from the untouched pre-existing files above. Historical `stage_*` reports were not rewritten.

## 3. Authoritative author clarification used

The integration treats the author-supplied clarification as a project fact:

1. an LLM was used at design time to propose the proxy ontology, dataset-specific DAGs, and decision-tree rules;
2. project-selected designs were encoded in deterministic source code;
3. the deterministic trees generated rule-derived proxy labels;
4. deep irregular-time-series models learned to predict those labels;
5. normalized or aggregated proxy-label representations entered the downstream causal workflow; and
6. the LLM was not a runtime estimator in the executed preprocessing, prediction, or causal pipeline.

The clarification was not used as evidence of medical-expert validation, chart adjudication, graph discovery from patient data, proved identification, unchanged implementation of every proposal, or clinical actionability.

## 4. Papers inspected and methodological roles

| Citation key | Retained paper and version | Narrow role in the thesis |
| --- | --- | --- |
| `singhal_et_al_2023_llm_clinical_knowledge` | Singhal et al., corrected 2023 Nature publisher PDF | Bounded precedent that evaluated LLMs can encode and express substantial clinical knowledge; not validation of this project's rules or outputs. |
| `darvariu_et_al_2024_llm_causal_graph_priors` | Darvariu, Hailes, and Musolesi, arXiv v1, 2024 | Precedent for LLM semantic judgments as causal-graph priors or proposals; not validation of the project DAGs. |
| `ratner_et_al_2016_data_programming` | Ratner et al., extended arXiv v3 copy of the NIPS 2016 paper | Foundational context for expressing domain heuristics as programmatic labeling functions. |
| `ratner_et_al_2020_snorkel` | Existing expanded 2020 VLDB Journal publisher version | Weak-supervision and downstream discriminative-training context; CliniCause does not implement Snorkel's learned generative label model. |

Exact input identity, size, page count, version status, source link, disposition, path, and SHA-256 are recorded in `llm_literature_ingestion_report.md`.

## 5. Files changed by this task

Literature corpus and metadata:

- `thesis-writing/literature/README.md`
- `thesis-writing/literature/llm_methodology_candidate_additions.md`
- `thesis-writing/literature/metadata/references.bib`
- `thesis-writing/literature/metadata/catalog.csv`
- `thesis-writing/literature/metadata/checksums.sha256`
- `thesis-writing/literature/papers/llm_clinical_knowledge_singhal_et_al_2023.pdf`
- `thesis-writing/literature/papers/llm_causal_graph_priors_darvariu_et_al_2024.pdf`
- `thesis-writing/literature/papers/weak_supervision_data_programming_ratner_et_al_2016.pdf`
- the four input files were removed from `thesis-writing/literature/new/`, and the empty `new` directory was deleted after validation.

Current canonical audit, planning, terminology, and reproducibility records:

- `thesis-writing/audit/llm_prompt_provenance_audit.md`
- `thesis-writing/audit/claim_evidence_ledger.csv`
- `thesis-writing/audit/terminology_map.md`
- `thesis-writing/planning/citation_plan.md`
- `thesis-writing/planning/chapter_evidence_map.md`
- `thesis-writing/planning/thesis_story.md`
- `thesis-writing/planning/terminology_and_notation.md`
- `thesis-writing/reproducibility/provenance_gaps.csv`

Thesis sources and generated PDF:

- `thesis-writing/thesis/frontmatter/administrative_metadata.tex`
- `thesis-writing/thesis/frontmatter/abstract_primary.tex`
- `thesis-writing/thesis/frontmatter/abstract_secondary.tex`
- `thesis-writing/thesis/frontmatter/keywords.tex`
- `thesis-writing/thesis/frontmatter/nomenclature.tex`
- `thesis-writing/thesis/chapters/01_introduction.tex`
- `thesis-writing/thesis/chapters/02_background_related_work.tex`
- `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex`
- `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`
- `thesis-writing/thesis/chapters/06_predictive_modeling.tex`
- `thesis-writing/thesis/chapters/07_causal_methodology.tex`
- `thesis-writing/thesis/chapters/09_experimental_design.tex`
- `thesis-writing/thesis/chapters/10_results.tex`
- `thesis-writing/thesis/chapters/11_discussion.tex`
- `thesis-writing/thesis/chapters/12_conclusions_future_work.tex`
- `thesis-writing/thesis/main.pdf`

New task reports:

- `thesis-writing/logs/llm_literature_ingestion_report.md`
- `thesis-writing/logs/llm_methodology_integration_claim_audit.csv`
- `thesis-writing/logs/llm_methodology_integration_evidence_report.md`

No Chapter 4, Chapter 8, appendix source, research-code file, result CSV, checked number, estimator output, or result figure was edited.

## 6. Thesis sections changed

- The approved English title was retained exactly; the Hebrew title was corrected to the approved wording while keeping `CliniCause:` in an English-direction span.
- Both abstracts now state the same design-to-execution chain and limitations, contain no citations or footnotes, and remain under 500 words (`detex` counts: English 342, Hebrew 360).
- The keywords contain 15 English and 15 Hebrew entries; the nomenclature now defines LLM and the aggregated proxy-label notation.
- Chapter 1 makes LLM-assisted design a substantive framework stage, updates the objective, research questions, contribution hierarchy, and contribution table, and preserves the prediction/causal distinction.
- Chapter 2 adds `LLM-Assisted Clinical and Causal Knowledge Elicitation` and gives each of the four references a separate, bounded role.
- Chapter 3 separates the design-time knowledge-construction layer from the executed patient-level layer.
- Chapter 5 is the authoritative account of prompt versions, final runs, user-reported model metadata, partial output-to-source traceability, source-code authority, six design-element mappings, and validation limits.
- Chapter 6 states the supervision chain from LLM-assisted rule design to rule labels to predictive targets and distinguishes learnability from construct validity.
- Chapter 7 describes source-encoded, non-data-learned DAGs, static adjustment logic, measurement-error propagation, and the exact archived five-source voter lineage.
- Chapter 9 corrects the experimental-design matrix and provenance boundary; Chapter 10 makes terminology-only lineage corrections without changing numerical content.
- Chapter 11 adds a dedicated advantages/limitations analysis and the required non-validation statements.
- Chapter 12 concludes with the four-stage framework and concrete clinical review, chart validation, design-comparison, LLM replication, prompt sensitivity, label-noise, graph-review, measurement-error, and external-validation work.

## 7. Old claims corrected

- “No implemented LLM role” and “LLM literature is out of scope” were replaced in current canonical sources with a substantive design-time role and an explicit no-runtime-LLM boundary.
- Sole clinician authorship was not asserted. The text now says project-selected and source-encoded, while formal human/clinical-review provenance remains incomplete.
- DAGs are described as LLM-assisted and project-specified, not discovered from patient data or dynamically selected by an LLM.
- Deterministic outputs are rule-derived proxy labels, not diagnoses or ground-truth latent states; deep models predict those targets rather than create authoritative clinical labels.
- The final causal input is no longer generalized as prediction-only. All 12 archived final vote logs enumerate one rule-derived table plus GRU, GRU-D, STraTS, and TCN predicted-label tables; SAnD is not a voter. The aggregate is then passed downstream.
- Majority voting is described as algorithmic aggregation, not clinician or expert consensus and not the Snorkel generative label model.

The exhaustive audit has 2,265 rows: the 2,264 frozen search hits plus one supplemental Chapter 9 target-lineage line missed by the original hyphen-sensitive expression. Classification totals are 1,166 protected historical, 815 implementation/artifact documentation, 222 correct retained, 57 obsolete, 4 unsafe, and 1 citation-required. Its SHA-256 is `149968e1af566848ff94f7bbc3c9375c20a36c93e71a4cacdaa0fea1ee10756a`.

## 8. Claims deliberately retained

- The LLM is a design-time component, not a runtime patient-level estimator.
- Active deterministic tagger and graph source files are authoritative for implemented behavior; prompts are design-provenance artifacts rather than execution logs.
- Prompt-to-code mapping is partial, exact hosted-model and decoding metadata are incomplete, and the model/version remains project reported rather than independently encoded in the PDFs.
- Proxy states are not chart-adjudicated diagnoses; DAG correctness, measured-confounding adequacy, overlap, temporal ordering, and model assumptions remain conditions rather than established facts.
- No LLM ablation, clinician comparison, prompt-sensitivity study, alternative-LLM replication, graph-correctness experiment, prospective validation, or clinical deployment evidence exists.
- Clean-checkout computational reproducibility and external voter/checkpoint provenance remain incomplete.

Protected historical reports retain their time-specific wording. The noncanonical copied guide `important-md-copies/thesis_literature_corpus_guide.md` also retains one obsolete scope statement and is explicitly classified as superseded artifact documentation in claim-audit row 2,092.

## 9. Citations added and exact supporting role

- `singhal_et_al_2023_llm_clinical_knowledge`: evaluated medical-knowledge capability with reliability and validation limitations.
- `darvariu_et_al_2024_llm_causal_graph_priors`: LLM knowledge as graph-prior/proposal information, not local graph validation.
- `ratner_et_al_2016_data_programming`: programmatic construction of training labels from domain heuristics.
- `ratner_et_al_2020_snorkel`: weak-supervision and discriminative-training context with an explicit non-equivalence statement.

The references are placed beside their supported claims rather than cited as an undifferentiated group. All thesis citation keys resolve, all four methodology references are cited, and the final Biber log contains zero warnings and zero errors.

## 10. Duplicate-resolution decision

Incoming `1711.10160v1.pdf` was the earlier 2017 arXiv/PVLDB version of the existing Snorkel work. The retained `ratner_et_al_2020_snorkel` file is the expanded 2020 VLDB Journal publisher version, so its established key and path were preserved. The redundant input was deleted only after normalized-title, author, DOI/publication-lineage, retained-PDF, and checksum checks. The incoming duplicate SHA-256 was `ca0a8c147e8fc157c3600539a247140c1921a009e8814a6ebb715cc61a344737`; the retained file SHA-256 is `9c611b904d4e2ad2af11d1fe497120706fb4763d1657dba70fb08426baa456c6`.

## 11. Protected-artifact comparison

The same sorted aggregate-hash procedure was run before editing and after the final build. Every protected aggregate is byte-identical:

| Protected scope | Files | Baseline and final aggregate SHA-256 |
| --- | ---: | --- |
| `thesis-writing/results/` | 24 | `95b403f18a0f357e548ef0d21fed36868e75cb6beca9a09eae6ac3f682a1ad36` |
| `thesis-writing/thesis/figures/` | 6 | `66da51c26741bd06b610a49e2b8b7b70063a4a6ae478bd14ff6dcd1b1fbdc875` |
| `causal-irregular-time-series/` | 83 | `b1752b905209e4fe13e547feca157a0ccc5b63b597bc83f80ce6e45160ba911b` |
| `STraTS/` | 55 | `8df73f0e1a905d7b3bb83febfb565b25e6a589e8b7d48538c001eff0c63b74bb` |

The 128 numeric-bearing lines in Chapter 10 are byte-identical to the pre-edit snapshot. Across changed thesis sources, the only newly introduced numeric tokens are citation years, table-width parameters, documented prompt dates/model metadata, and notation; no pre-existing result token was removed from Chapter 10. No figure filename or protected figure byte changed.

## 12. Literature validation results

- Catalog: 43 total records = 38 core + 5 optional.
- PDF status: 41 available local PDFs (`present` or `downloaded`) + 2 intentionally missing.
- All 41 available files begin with the PDF signature and pass `pdfinfo`; all available catalog paths exist and their SHA-256 fields match.
- The 43 BibTeX keys are unique and exactly equal the 43 catalog keys. Normalized titles, nonempty DOI values, and canonical PDF paths are unique.
- `metadata/checksums.sha256` has 41 stably sorted records, and `sha256sum -c metadata/checksums.sha256` passes every record.
- The catalog retains 44/44 CRLF-terminated lines with no space or tab before an end of line.
- Every new BibTeX `file` path and every available catalog `pdf_path` exists.
- `thesis-writing/literature/new/` no longer exists.

## 13. LaTeX build results

The canonical clean build was run from `thesis-writing/thesis/`:

```text
latexmk -C
latexmk -xelatex main.tex
```

Final result:

- exit status 0; `latexmk` reports all targets up to date;
- 118 A4 pages, 3,066,539 bytes;
- PDF SHA-256 `4d66ba3dfa4abf9790fa26b6c3ca1ed7ceeb3dfe6458021f9575ae27c1e27902`;
- `qpdf --check main.pdf`: no syntax or stream-encoding errors;
- zero undefined citations, undefined references, missing files, LaTeX errors, Biber warnings, or Biber errors;
- final log counts: 58 overfull `hbox` notices, 1,242 underfull `hbox` notices, and no overfull/underfull `vbox` notices. Visual inspection found no material overflow; the notices are concentrated in the thesis's dense, narrow-column tables. The existing Hebrew-language fallback and duplicate destination/object warnings remain nonfatal template/toolchain behavior.

The repository-wide `git diff --check` was run and returned the pre-existing dirty-worktree CRLF/trailing-whitespace findings in unrelated root, result, stage-log, and temporary files. A task-scoped check passes for every changed tracked text file except `catalog.csv`, whose intentionally preserved CRLF endings Git reports as trailing whitespace; a byte-level check confirms no actual spaces or tabs precede any catalog line ending. The three new reports also contain no trailing whitespace.

## 14. Complete PDF page review

Every page of the final 118-page PDF was rendered at 120 DPI and individually inspected. The review explicitly covered the English and Hebrew covers, Hebrew and English abstracts, keywords, contents/list pages, the contribution table, the new related-work subsection, Chapter 5 traceability table, causal method, results, discussion limitations, conclusions, appendix, and all bibliography pages.

Two task-introduced pagination problems were found and repaired before the final review:

- the expanded English abstract originally left a few lines on a second page; redundant wording was tightened without changing any checked result or methodological condition, and the final abstract fits completely on page 3;
- a deferred contribution-table float originally appeared between the two page-separated halves of “follow”; a float boundary now keeps the table and subsequent prose in a valid order.

The final page-by-page pass found no task-introduced material clipping, overlap, missing element, unexpected blank page, bad margin, header/footer collision, broken bibliography, or Hebrew/RTL defect. Several tables remain dense but are zoom-readable and within their margins.

One material visual issue predates and is outside this task's permitted repair scope: the causal-DAG figures on final PDF pages 60--61 contain very small, overlapping node labels in the source PNGs themselves. The figures-directory aggregate hash is exactly equal to baseline, proving this task did not introduce the collisions. The issue is recorded for a future figure-specific stage rather than altering protected figure bytes here.

## 15. Unresolved provenance, validation, and reproducibility gaps

- Exact hosted-model build metadata, system prompt, decoding parameters, browsing/tool state, and complete interaction/export procedure are not independently preserved.
- The accepted/rejected proposal record, human selection chain, formal clinician review, and line-by-line prompt-output-to-source mapping are incomplete.
- There is no clinician-panel adjudication, chart-level proxy validation, external clinical validation, or prospective validation.
- There is no clinician-only/hybrid comparison, alternative-LLM replication, prompt perturbation, model-version sensitivity, or formal LLM robustness experiment.
- The archived final vote logs identify five source filenames, but the external voter bytes, per-voter hashes, exact checkpoint-to-export mappings, and complete split lineage are unavailable locally.
- Clean-checkout reproduction of every historical run is not established.
- Proxy validity, graph correctness/completeness, temporal ordering, overlap, measured-confounding adequacy, model assumptions, and possible unmeasured confounding remain substantive conditions.
- The protected DAG PNG labels remain visually crowded/overlapping and should be regenerated in a separately authorized figure-repair stage.

## 16. Final readiness decision

All requested literature, metadata, current canonical records, thesis framing, claim audit, protected-scope checks, clean build, and final page review are complete. Remaining gaps are explicitly bounded and do not prevent author review; they do prevent claims of clinical validation, proved causal identification, or complete computational reproducibility.

READY FOR AUTHOR REVIEW OF LLM METHODOLOGY INTEGRATION

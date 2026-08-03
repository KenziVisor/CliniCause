# Stage 4.10C Evidence Report

## 25.1 Repository baseline

| item | result |
| --- | --- |
| Head | 405f907 step 4.10B |
| Parent | 46c3c87 step 4.10A |
| Branch | main |
| Stage 4.10B | Verified expected commit, parent, five changed paths, and no figure change. Its report records 122 pages, zero unresolved citations/references/duplicate labels/fatal errors, and readiness for this stage with non-blocking warnings. |
| Initial worktree | Dirty before this stage. Pre-existing unrelated modifications included root documentation/code, the nested causal repository, prompt.txt, requirements/router/test files, copied notes, literature catalog, checked result CSVs, results_manifest.csv, and tmp_verify_router.py. They were preserved. |

No reset, worktree clean, branch switch, staging, commit, amend, or push was performed.

## 25.2 Baseline build and visual state

The pre-existing Stage 4.10B PDF was 122 pages. Its clean rebuild was started with latexmk clean and XeLaTeX; XeLaTeX reached a 122-page XDV, while the baseline capture did not complete final PDF conversion before front-matter work began. The Stage 4.10B report supplies the corresponding successful baseline record.

The pre-edit front matter contained generic draft placeholders in both abstracts, keywords, acknowledgements, nomenclature, and all seven appendix chapters. Title and approval pages contained generic administrative placeholders. Acknowledgements created a placeholder-only page; every appendix was placeholder-only.

## 25.3 Institutional requirements applied

| requirement | implementation | status | remaining authority needed |
| --- | --- | --- | --- |
| A4, 1.5--2 spacing, margins | A4 report/12pt, 1.5 spacing, 2 cm margins retained. | Implemented. | None for draft layout. |
| Numbering | Unnumbered title pages; Roman top-centred front matter begins at Hebrew abstract; Arabic top-centred body begins at Chapter 1. | Implemented and rendered. | Faculty form may add requirements. |
| Bilingual abstracts | Same hierarchy and qualifications; English 347 words; Hebrew 320 letter-token words. | Implemented. | English-thesis authorization. |
| TOC through subsection | Report tocdepth=2 retained; compiled TOC contains chapters, sections, and subsections. | Implemented. | None. |
| Nomenclature/lists/bibliography | Reader-facing nomenclature completed; both lists retained; bibliography after appendices. | Implemented. | Human format approval. |
| Current title/approval forms | Centralized metadata and structurally prepared pages. | Administratively blocked. | Current faculty form and official metadata. |

## 25.4 Title audit

The title remains “A DAG-Guided Framework for Proxy-State Effect Estimation in Irregular ICU Time Series.” It aligns with Chapters 1 and 10--12 when effect estimation is read as observational and conditional. It was not changed. It is provisional pending author/supervisor approval; the official Hebrew title remains unavailable.

## 25.5--25.7 Abstracts

The abstract claim set is in stage_4_10C_front_back_matter_brief.md. Sources are Chapter 1 for objective/workflow, Chapter 10 and Chapter 12 for the four numerical findings, and Chapters 11--12 for limitations.

| component | English | Hebrew | equivalent |
| --- | --- | --- | --- |
| Motivation/objective | Irregular ICU data and evidence-tracked proxy-state framework. | Same. | Yes |
| Workflow/datasets | Separate PhysioNet 2012 and MIMIC-III analysis with prediction and DAG-guided adjusted analysis. | Same. | Yes |
| Findings | 9/9, 9/10 with negative shock, 19/19, and 18/19. | Same values and exception. | Yes |
| Estimator boundaries | CausalPFN exploratory; matching descriptive; no pooling. | Same. | Yes |
| Limitations | Conditional estimates; no causal/clinical/deployment claim; incomplete clean-checkout reproducibility. | Same. | Yes |

Both abstracts contain no citations or footnotes. They add no unsupported model family, aggregate, clinical conclusion, treatment recommendation, clean-checkout claim, or LLM-expertise/discovery claim. Polyglossia Hebrew support uses installed FreeSerif; the rendered Hebrew, Latin terms, punctuation, and direction were inspected.

## 25.8 Keywords

There are 15 English and 15 corresponding Hebrew keywords: irregular clinical time series, intensive care, electronic health records, proxy states, multi-label prediction, missingness-aware modeling, directed acyclic graphs, observational causal inference, double machine learning, causal forests, heterogeneous effect estimation, sensitivity analysis, evidence provenance, MIMIC-III, and PhysioNet 2012. InterpNet, diagnosis, clinical decision support, and treatment recommendation are absent.

## 25.9 Administrative and acknowledgements status

| field | status | rendered placeholder or omitted | required authority | impact |
| --- | --- | --- | --- | --- |
| Author name/identification | Missing | Precise title-page placeholder | Author/current form | Blocks final title page. |
| Department/faculty/degree wording | Missing | Precise title-page placeholder | Department/current form | Blocks final title page. |
| Supervisor/co-supervisor | Missing | Precise title-page placeholder | Supervisor/current form | Blocks title/approval pages. |
| Submission date | Missing | Precise title-page placeholder | Author/submission record | Blocks final title page. |
| Approval/signature wording | Missing | Precise approval-page gate | Current faculty form | Structurally prepared, administratively blocked. |
| Ethics/data governance wording | Missing | Precise approval-page gate; no compliance claimed | Institutional/dataset records | Required for submission/prospective use. |
| English authorization | Not established | Precise title-page gate | Department | English thesis remains conditional. |
| Official Hebrew title | Missing | Not fabricated | Author/supervisor/form | Blocks final bilingual package. |
| Acknowledgements | No approved text | Page omitted | Author | No placeholder-only page. |

Full administrative inventory: stage_4_10C_administrative_inputs_required.md.

## 25.10 Abbreviations and notation


Included notation is directly verified in Chapters 3 and 7: i, n_i, t_ij, v_ij, x_ij, mathcal V, mathcal O_i, L-rule, predicted p, predicted L, A_i, Y_i, W_i, X_i, and Y_i(a). Unused planning-only symbols were excluded.

## 25.11--25.13 Appendix, tables, and figures

| appendix | disposition | evidence/content | limitation |
| --- | --- | --- | --- |
| APP-A | OMIT | Complete rules are already in Chapter 5. | Avoid duplicate methods; clinical grounding gaps remain. |
| APP-B | OMIT | Chapter 7 already provides active graph/node material. | A full inventory would duplicate methods and is not a validated graph. |
| APP-C | MERGE into APP-F | Configuration recoverability boundary. | Exact numbered configurations unavailable. |
| APP-D | MERGE into APP-F | Implemented-versus-executed distinction. | No verified producing command/checkpoint lineage. |
| APP-E | OMIT | No additional display is needed. | Supporting figures duplicate evidence and would trigger external review. |
| APP-F | KEEP | Concise reproducibility/evidence-boundary appendix. | No clean-checkout or governance claim. |
| APP-G | OMIT | Legacy material remains in audit records. | No scholarly reader benefit. |

No appendix table was added. The appendix evidence map records the source-checked narrative appendix and no displayed numerical values. No new appendix figure entered the compiled thesis. The figure packet has its required header and no rows; supporting candidates were not inserted and blocked figures remain excluded. No new external figure review is required.

## 25.14--25.15 Placeholders and structure

Generic front/back-matter placeholders were replaced with supported content, omitted (acknowledgements), or converted to centralized precise administrative gates. Remaining placeholder scan matches occur only in protected body chapters and are inherited precise review/provenance/validation gates. No retained appendix is placeholder-only.

Document order is title pages, Hebrew abstract, English abstract, bilingual keywords, TOC, nomenclature, figure/table lists, body, appendix, bibliography. Render inspection covered title/approval pages, abstracts, keyword page, TOC, nomenclature, lists, Chapter 1 opening, Appendix A, and bibliography transition. No broken Hebrew glyphs, reversed punctuation, clipped changed content, blank placeholder page, detached caption, or unreadable new table/figure was found.

## 25.16 Protected-file validation

SHA-256 was recalculated for 34 protected files: Chapters 1--12, checked CSVs, frozen result records, figure register, bibliography, and literature catalog. Comparison with the pre-edit protected-hash baseline passed byte-for-byte: protected_hash_cmp=0.

## 25.17 Files changed

Stage source/log paths: main.tex; administrative_metadata.tex; all seven allowed frontmatter files; appendices.tex; stage_4_10C_front_back_matter_brief.md; stage_4_10C_administrative_inputs_required.md; stage_4_10C_appendix_evidence_map.csv; stage_4_10C_figure_validation_packet.csv; this report; and main.pdf.

Generated untracked build files: main.aux, main.bbl, main.bcf, main.blg, main.fdb_latexmk, main.fls, main.lof, main.lot, main.out, main.run.xml, main.toc, and main.xdv. No figure file or generator was added. Pre-existing unrelated modifications remain separate.

## 25.18 Final build

| check | result |
| --- | --- |
| latexmk clean and XeLaTeX build | Success, return code 0. |
| PDF | Present, A4, 115 pages. |
| SHA-256 | 7765c7c35b6bdecf6329d97937279eb7f57e89ea34b615616493d4b800df4fc8 |
| Citations/references/duplicate labels/fatal errors/Biber errors | 0 / 0 / 0 / 0 / 0 |
| Missing glyph, bidi, xdvipdfmx warnings | 0 / 0 / 0 |
| Box warnings | Existing body layout: 100 overfull and 1,150 underfull entries; changed front/back matter rendered cleanly. |

## 25.19 Remaining gates

Final title approval; English-thesis authorization; current faculty forms; author/supervisor/department/degree/date details; approval/signature text; acknowledgements; authoritative ethics/data-governance wording; supervisor causal-language ratification; clinical review; CausalPFN primary source; raw/configuration/split/checkpoint/source-version/archive provenance; and external human review of existing thesis figures remain open.

## 25.20 Readiness decision

READY FOR STAGE 5.1 WITH NON-BLOCKING ADMINISTRATIVE WARNINGS

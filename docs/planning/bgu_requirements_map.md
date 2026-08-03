# BGU Requirements Map

Source: `thesis-writing/general-instructions.pdf`, extracted with `pypdf` because no system `pdftotext` utility was available.

## Official Requirements From PDF

| requirement_id | requirement | source_location | planned_thesis_location | example_thesis_pattern | implementation_status | advisor_check | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BGU-OFF-001 | Thesis must demonstrate suitable scientific level, command of research methods, independent analysis, and scientific-engineering writing with original character. | PDF p.1, sec. 12.a.1 | Entire thesis; especially Chapters 1, 3, 7-12 | Example has original contribution section in Chapter 1. | Planned in outline | yes | Originality should be framed as pipeline/method integration, not clinical discovery. |
| BGU-OFF-002 | Default final thesis language is Hebrew with English abstract; English submission requires departmental approval and then Hebrew abstract. | PDF p.1, sec. 12.a.2(a) | Front/back matter | Example main text is English with Hebrew and English abstracts. | Needs later LaTeX decision | yes | Writing language for final thesis is [ADVISOR CHECK]. |
| BGU-OFF-003 | Thesis must include introduction/problem definition. | PDF p.2, sec. 4(a) | Chapter 1 | Example Chapter 1 introduces motivation and question. | Planned | no | Chapter 1 should avoid numerical claims. |
| BGU-OFF-004 | Thesis must include comprehensive literature review and source index/bibliography. | PDF p.2, sec. 4(a), p.3 sec. 16-17 | Chapter 2 and bibliography | Example uses bibliography at end via `biblatex`/`Bibliography.bib`. | Planned | yes | Citation style must be uniform and approved by advisor/committee. |
| BGU-OFF-005 | Prior work must be evaluated for relevance and relative value. | PDF p.2, sec. 4(b) | Chapter 2 synthesis sections | Example related-background chapters are broad. | Planned | no | Related work should be conceptual, not paper-by-paper. |
| BGU-OFF-006 | Research objective must be defined. | PDF p.2, sec. 4(c) | Chapter 1 and Chapter 3 | Example states research question/contribution. | Planned | no | Use main RQ and SRQs from `thesis_story.md`. |
| BGU-OFF-007 | Research method must be detailed. | PDF p.2, sec. 4(d) | Chapters 3-9 | Example has methods/evaluation chapters. | Planned | no | Methods should be evidence-grounded and avoid results prose. |
| BGU-OFF-008 | Results must be presented. | PDF p.2, sec. 4(e) | Chapter 10 | Example has results chapter. | Blocked for full drafting | yes | Numerical result prose waits for approved artifacts and manifest. |
| BGU-OFF-009 | Reliability, errors, and measurement limitations must be evaluated. | PDF p.2, sec. 4(e) | Chapters 8 and 11 | Example has evaluation/results discussion. | Planned | no | Include proxy-label error, measurement irregularity, missingness, overlap, confounding. |
| BGU-OFF-010 | Conclusions and possible applications must be justified from obtained results. | PDF p.2, sec. 4(f) | Chapter 12 | Example conclusion/future work. | Planned; delayed | yes | Do not introduce new evidence in conclusion. |
| BGU-OFF-011 | A4 white paper and good print quality. | PDF p.2, sec. 5(1,3) | LaTeX class/page setup | Example uses `a4paper,12pt`. | Later LaTeX implementation | no | Stage 3 does not edit final LaTeX. |
| BGU-OFF-012 | Line spacing 1.5-2. | PDF p.2, sec. 5(2) | LaTeX preamble | Example uses `\renewcommand{\baselinestretch}{2}`. | Later LaTeX implementation | no | Prefer template-consistent spacing. |
| BGU-OFF-013 | Margins at least 1 cm on all sides. | PDF p.2, sec. 5(4) | LaTeX geometry | Example uses `margin=2cm`. | Later LaTeX implementation | no | Verify department template before final. |
| BGU-OFF-014 | Page numbers appear centered at top; abstract numbered Roman or Hebrew letters; body numbered Arabic. | PDF p.2, sec. 5(5) | Front matter and main matter page numbering | Example uses roman front matter and Arabic main matter, but plain style may place numbers differently. | Needs LaTeX check | yes | Top-center numbering may need `fancyhdr`; example may not fully satisfy. |
| BGU-OFF-015 | Chapters/subchapters must use a numbering system where first number identifies the chapter. | PDF p.2, sec. 5(6) | All numbered chapters | Example uses report class chapter/section numbering. | Planned | no | TOC must reach third level. |
| BGU-OFF-016 | Figures must be high quality. | PDF p.2, sec. 5(7) | Figure plan; later LaTeX figures | Example embeds PNGs under `Figs/`. | Planned | no | Existing project images need visual validation. |
| BGU-OFF-017 | Cover pages and internal title pages must follow faculty form examples. | PDF p.2, sec. 5(8-9), p.3 sec. 19 | Front/back matter | Example hard-codes BGU title/approval pages. | Later LaTeX implementation | yes | Official form examples not included locally; must obtain current faculty forms. |
| BGU-OFF-018 | Tables and figures must follow accepted standards and be numbered separately. | PDF p.2, sec. 5(10) | Lists of figures/tables; all captions | Example has list of figures; no list of tables visible in inspected section. | Planned | no | Add separate list of tables. |
| BGU-OFF-019 | Equations, signs, and symbols must follow accepted international standards. | PDF p.2, sec. 5(11) | Notation and methods chapters | Example has notation section. | Planned | no | Use notation file as final source. |
| BGU-OFF-020 | Hebrew and English abstracts must use the same format. | PDF p.2, sec. 5(12a) | Abstract pages | Example has Hebrew then English abstract. | Planned | yes | Order depends on final language and official sequence. |
| BGU-OFF-021 | Abstract length must not exceed 500 words. | PDF p.2, sec. 5(12b) | Abstracts | Example abstracts appear short. | Later drafting validation | no | Validate word count separately. |
| BGU-OFF-022 | Table of contents must list to third-level headings. | PDF p.2, sec. 5(13) | TOC | Example uses `\tableofcontents`. | Later LaTeX implementation | no | Set `tocdepth=3`. |
| BGU-OFF-023 | Terminology/symbol list appears when needed. | PDF p.2, sec. 5(14) | Abbreviations and notation | Example has Abbreviations and Notation. | Planned | no | This thesis needs both. |
| BGU-OFF-024 | 10-15 keywords or phrases must appear after the abstract. | PDF p.3, sec. 5(15) | Keywords page after abstract | Example does not show a keyword page in inspected front matter. | New LaTeX implementation needed | no | Must add in final thesis. |
| BGU-OFF-025 | Bibliography must be systematic and citation numbering/style uniform. | PDF p.3, sec. 16-17 | Bibliography | Example uses `biblatex` and `\addbibresource`. | Planned | yes | Current project source of truth is `thesis-writing/literature/metadata/references.bib`. |
| BGU-OFF-026 | If thesis is in Hebrew, use Hebrew terms where possible. | PDF p.3, sec. 18 | Terminology policy | Example uses bilingual handling. | Depends on language | yes | If English thesis approved, still provide Hebrew abstract and title pages. |
| BGU-OFF-027 | Required document order is cover, title, abstract, keywords, acknowledgements, TOC, terminology/list of symbols, lists of tables/figures, body, appendices, notes, bibliography, English abstract, English title, English cover. | PDF p.3, sec. 19 | Final document sequence below | Example has title/approval, abstracts, acknowledgements, TOC, list of figures, abbreviations, notation, body. | Planned with corrections | yes | PDF order is Hebrew-oriented; adapt for English submission only after confirmation. |
| BGU-OFF-028 | Binding direction differs for Hebrew/main material and English back matter. | PDF p.3, sec. 20 | Final PDF/printing instructions | Example not sufficient as official binding proof. | Outside Stage 3 | yes | Important for final submission package, not drafting files. |

## Example Thesis Patterns

| pattern_id | observed pattern | use for CliniCause? | notes |
| --- | --- | --- | --- |
| EX-001 | `report` class with `a4paper,12pt`. | yes, as starting point | Later use a cleaner modular structure if possible. |
| EX-002 | Title page and approval page hard-coded in `main.tex`. | yes, with current BGU forms | Do not copy subject text. |
| EX-003 | Hebrew abstract then English abstract. | yes, if language/order confirmed | Official order depends on thesis language. |
| EX-004 | Roman front matter and Arabic main matter. | yes | Need top-center page numbers per PDF. |
| EX-005 | Abbreviations and notation are unnumbered chapters added to TOC. | yes | This thesis needs both. |
| EX-006 | Bibliography uses `biblatex` with `backend=bibtex`. | maybe | Project should use `references.bib`; confirm `biblatex` vs BibTeX/Biber later. |
| EX-007 | Single large `main.tex`. | no | Recommend modular chapters in Stage 4/5 to reduce risk. |
| EX-008 | Duplicate package imports (`graphicx`, `subcaption`, math packages) and many unused macros. | no | Avoid copying clutter. |
| EX-009 | Figure directory `Figs/` contains example assets. | formatting only | Exclude from CliniCause evidence. |

## Recommended Project-Specific Choices

| choice_id | recommendation | rationale | status |
| --- | --- | --- | --- |
| CLINI-BGU-001 | Write the main thesis in English only if departmental approval exists. | Official PDF defaults to Hebrew; English submission requires approval. | [ADVISOR CHECK] |
| CLINI-BGU-002 | Use a modular LaTeX architecture: `main.tex`, `frontmatter/`, `chapters/`, `appendices/`, `figures/`, `tables/`, `macros.tex`. | Easier Stage 4 drafting and validation. | Later implementation |
| CLINI-BGU-003 | Keep final thesis bibliography linked to `thesis-writing/literature/metadata/references.bib` or a copied approved derivative. | Avoid drift from curated corpus. | Later implementation |
| CLINI-BGU-004 | Provide both abbreviations and notation lists. | Required by thesis complexity and supported by official terminology/symbol requirement. | Planned |
| CLINI-BGU-005 | Use separate list of figures and list of tables. | Official separate numbering requirement and expected thesis usability. | Planned |
| CLINI-BGU-006 | Include a reproducibility appendix. | Repository provenance gaps are central limitations. | Planned |

## Proposed Final Document Sequence

Assuming English main text is approved [ADVISOR CHECK]:

1. External English cover page using current BGU engineering form [ADVISOR CHECK].
2. English internal title page.
3. Approval/signature page.
4. Hebrew abstract, matching English abstract format and <= 500 words.
5. Hebrew keywords or bilingual keyword list, 10-15 items [ADVISOR CHECK].
6. English abstract, matching Hebrew format and <= 500 words.
7. English keywords, 10-15 items.
8. Acknowledgements.
9. Table of contents through third-level headings.
10. Abbreviations.
11. Notation and symbols.
12. List of figures.
13. List of tables.
14. Main body: Chapters 1-12.
15. Appendices.
16. Notes, if used.
17. Bibliography.
18. Required Hebrew/English back-cover/title pages if mandated by current faculty form [ADVISOR CHECK].

If the final thesis must be Hebrew, follow PDF sec. 19 literally and place the English abstract/title/cover at the end.


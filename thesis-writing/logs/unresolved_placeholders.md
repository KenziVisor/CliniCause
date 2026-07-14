# Stage 4.0 Unresolved Placeholders

This inventory covers placeholders present in the Stage 4.0 LaTeX skeleton under `thesis-writing/thesis/`.

## Placeholder Classes

| placeholder | meaning | resolution gate |
| --- | --- | --- |
| `[STAGE 4 DRAFT REQUIRED]` | A later Stage 4 drafting prompt must write this section from the approved evidence packet. | Matching Stage 4 prompt and review gate. |
| `[RESULT REQUIRED]` | Numerical, tabular, figure, or result-specific material is unavailable or not yet approved. | Checked result artifact/table/figure package. |
| `[CITATION REQUIRED]` | Citation coverage must be added or verified before drafting this section. | Citation-plan validation; CausalPFN gap if applicable. |
| `[FIGURE REQUIRED]` | A planned figure slot exists, but the figure source/provenance/caption is not yet approved. | Figure plan validation. |
| `[TABLE REQUIRED]` | A planned table slot exists, but the table source/provenance/content is not yet approved. | Table plan validation. |
| `[VALIDATION REQUIRED]` | Source, result, wording, visual, or schema validation is required before final prose. | Stage-specific validation. |
| `[SUPERVISOR DECISION REQUIRED]` | Advisor or supervisor decision is required before drafting or final wording. | Human approval gate. |
| `[ADMINISTRATIVE DETAILS REQUIRED]` | Thesis administrative details are missing. | Current BGU/faculty forms and user details. |
| `[AUTHOR DETAILS REQUIRED]` | Author information is missing. | User/admin input. |
| `[SUPERVISOR DETAILS REQUIRED]` | Supervisor information is missing. | User/admin input. |
| `[DEPARTMENT DETAILS REQUIRED]` | Department/faculty wording is missing. | User/admin input and BGU forms. |
| `[APPROVAL TEXT REQUIRED]` | Approval/signature wording is missing. | Current BGU/faculty forms. |

## Inventory Summary

Generated with:

```bash
rg -o '\[[A-Z0-9 -]+ REQUIRED\]' thesis-writing/thesis/main.tex thesis-writing/thesis/frontmatter thesis-writing/thesis/chapters thesis-writing/thesis/appendices | sed 's/^.*://' | sort | uniq -c
```

| placeholder | count |
| --- | ---: |
| `[ADMINISTRATIVE DETAILS REQUIRED]` | 3 |
| `[APPROVAL TEXT REQUIRED]` | 1 |
| `[AUTHOR DETAILS REQUIRED]` | 2 |
| `[CITATION REQUIRED]` | 2 |
| `[DEPARTMENT DETAILS REQUIRED]` | 2 |
| `[FIGURE REQUIRED]` | 7 |
| `[RESULT REQUIRED]` | 19 |
| `[STAGE 4 DRAFT REQUIRED]` | 46 |
| `[SUPERVISOR DECISION REQUIRED]` | 12 |
| `[SUPERVISOR DETAILS REQUIRED]` | 2 |
| `[TABLE REQUIRED]` | 3 |
| `[VALIDATION REQUIRED]` | 32 |

## Main Locations

| area | files | placeholder focus |
| --- | --- | --- |
| Front matter | `frontmatter/title_pages.tex`, `abstract_primary.tex`, `abstract_secondary.tex`, `keywords.tex`, `acknowledgements.tex`, `nomenclature.tex` | Administrative details, language/order decisions, abstracts, keywords, acknowledgements, abbreviations, notation. |
| Chapters 1-9 | `chapters/01_*.tex` through `chapters/09_*.tex` | Drafting placeholders plus targeted result, citation, figure, table, validation, and supervisor-decision placeholders. |
| Chapter 10 | `chapters/10_results.tex` | Result and validation placeholders for every approved result slot. |
| Chapters 11-12 | `chapters/11_discussion.tex`, `chapters/12_conclusions_future_work.tex` | Result-dependent synthesis and final conclusion placeholders. |
| Appendices | `appendices/appendices.tex` | Appendix drafting, validation, figure/table slots, and supervisor-decision placeholders. |

No generic task-marker text, dummy Latin text, or filler thesis prose was found in `thesis-writing/thesis/` during Stage 4.0 validation.

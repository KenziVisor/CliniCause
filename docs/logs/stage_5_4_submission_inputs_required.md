# Stage 5.4 submission inputs required

This checklist records only inputs that must be supplied by an authoritative person or office. It does not treat their absence from the repository as evidence that no oversight occurred. The current PDF intentionally omits official title and approval pages until the necessary forms and values are supplied.

## Required from author

| required | why required | where inserted | authoritative provider | acceptable evidence | current status | submission blocking |
| --- | --- | --- | --- | --- | --- | --- |
| Full legal name and any required identification number | Official form metadata cannot be inferred from Git or repository identity. | Current title and approval forms; `administrative_metadata.tex` | Author | Author-confirmed details matching the faculty record | Missing | Yes |
| Final English title confirmation | The stored title is a working value, not a ratified official title. | Current title page and metadata | Author with supervisor ratification | Written confirmation | Pending | Yes |
| Approved Hebrew title | A Hebrew title must not be translated or inferred by the repository. | Current Hebrew/English submission forms and metadata | Author with supervisor/department approval | Written approved title | Missing | Yes |
| Submission month and year | Dates must reflect the real submission. | Current title/approval form | Author and department | Submission instruction or confirmed date | Missing | Yes |
| Acknowledgements text or decision to omit | Acknowledgements are author content, not repository metadata. | `frontmatter/acknowledgements.tex` if included | Author | Author-approved wording or instruction to omit | No text supplied; omitted | No, unless current form requires it |

## Required from supervisor or department

| required | why required | where inserted | authoritative provider | acceptable evidence | current status | submission blocking |
| --- | --- | --- | --- | --- | --- | --- |
| Final title ratification | Confirms scholarly and administrative title wording. | Official title page and final PDF metadata | Supervisor/department | Written approval | Missing | Yes |
| English-thesis authorization | Local BGU instructions require departmental approval for an English thesis. | Submission packet and any required front matter | Departmental teaching committee/department | Written authorization or official record | Not present locally | Yes |
| Supervisor name and official title | Official form text must be current and accurate. | Current title/approval forms | Supervisor/department | Official departmental confirmation | Missing | Yes |
| Co-supervisor status and wording, if applicable | A blank or invented field is not acceptable. | Current title/approval forms | Department | Current appointment/form record | Unknown | Yes if applicable |
| Exact degree, department, and faculty wording | Current faculty forms control the required wording. | Official title and approval pages | Department/faculty | Current form or official written wording | Missing | Yes |
| Final thesis sequence confirmation | Local instructions are Hebrew-default and do not establish the exact current English-thesis sequence. | Main front/back matter order | Department/faculty | Current thesis-submission instructions or form package | Missing | Yes |
| Current title-page and approval-page forms | The local PDF refers to forms not included in the repository. | `title_pages.tex` replacement and final PDF | Faculty/department | Current official forms | Missing | Yes |
| Committee, signature, and approval requirements | Required wording and signatories cannot be reconstructed. | Official approval page and submission packet | Department/faculty | Current form and committee instruction | Missing | Yes |

## Required from institution or data-governance authority

| required | why required | where inserted | authoritative provider | acceptable evidence | current status | submission blocking |
| --- | --- | --- | --- | --- | --- | --- |
| Ethics approval, exemption, or other determination wording | The repository cannot establish the project-specific determination. | Required ethics statement and official forms, if applicable | Institutional ethics/IRB authority | Official determination text | Missing | Yes |
| Approval/exemption identifier, if applicable | Numbers must never be invented. | Required ethics statement/form | Institutional ethics/IRB authority | Official record | Missing | Yes if applicable |
| Consent or waiver wording | Dataset availability does not establish participant-consent status for this project. | Required ethics statement/form | Institutional ethics/IRB authority | Official determination | Missing | Yes if applicable |
| Data-use agreement wording | Dataset-level access context is not a project-level agreement record. | Required governance statement/form | Dataset/data-governance authority | Applicable agreement or institutional confirmation | Missing | Yes if applicable |
| Governance and privacy wording | Required wording must state only what the authority has determined. | Required governance statement/form | Institutional data-governance authority | Approved statement | Missing | Yes if required |
| Retention/security or other institutional privacy requirements | No policy may be inferred from repository files. | Submission packet or institutional appendix, if required | Institutional data-governance authority | Current written instruction | Unknown | Yes if required |

## Required from qualified clinical reviewer

| required | why required | where inserted | authoritative provider | acceptable evidence | current status | submission blocking |
| --- | --- | --- | --- | --- | --- | --- |
| Proxy-rule review | Project-specific proxy thresholds and construct mapping are not clinically validated. | Clinical-methods wording, limitations, and decision record | Qualified clinical reviewer | Signed or dated decision record with scope and rationale | Missing | Yes for any stronger clinical claim; otherwise a documented submission gate |
| DAG review | Project DAGs are source-coded assumptions, not clinical approval. | DAG interpretation and limitations; decision record | Qualified clinical/causal reviewer | Arrow/rule-level accepted/rejected record | Missing | Yes for any claim of qualified clinical approval |
| Clinical-language review | Prevents proxy labels, estimates, and model results from being presented as diagnoses or recommendations. | Abstracts, Chapters 5, 7, 11, and 12 | Qualified clinical reviewer | Dated review record | Missing | Yes for final clinical-language sign-off |
| Accepted/rejected decision record | Review must distinguish a suggestion from approval and record any changes. | Project governance archive and submission packet | Qualified reviewer with supervisor | Dated, scoped decision log | Missing | Yes for an approval claim; otherwise retained as an explicit gate |

## Dataset-specific boundary

The approved MIMIC-III citation supports dataset-level de-identification and controlled-access context. The approved PhysioNet 2012 citation supports challenge-dataset context. Neither citation, dataset access, de-identification statement, nor repository record establishes the project's ethics determination, consent/waiver procedure, data-use agreement, or institutional governance decision.

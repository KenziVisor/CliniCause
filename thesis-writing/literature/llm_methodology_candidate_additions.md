# LLM Methodology Literature Decision

Stage 4.3R found LLM-assisted prompt-engineering artifacts relevant to design provenance. The author subsequently clarified that the LLM was used at design time to propose the proxy-variable ontology, dataset-specific causal DAGs, and decision-tree rules; accepted proposals were encoded in deterministic source code, and the LLM was not a runtime estimator.

## Current Decision

The literature-ingestion stage added three core references and retained the existing canonical Snorkel reference. Together they support bounded framing of LLM clinical knowledge, LLM-derived soft priors for causal-graph construction, and programmatic weak supervision. They do not validate the project-specific proxy states, decision rules, DAGs, or causal identification. Source code remains the authority for the implemented proxy-state rules and DAGs.

## Ingested References

| citation key | role | version decision |
| --- | --- | --- |
| `singhal_et_al_2023_llm_clinical_knowledge` | Evidence that medical LLMs can encode and express substantial clinical knowledge, subject to important reliability, safety, and validation limitations. | Corrected 2023 Nature publisher version retained. |
| `darvariu_et_al_2024_llm_causal_graph_priors` | Methodological precedent for treating LLM semantic judgments as soft prior information in causal-graph construction. | arXiv v1 preprint retained; no journal version was identified. |
| `ratner_et_al_2016_data_programming` | Foundational reference for expressing domain heuristics as programmatic labeling functions. | Published as NIPS 2016; the extended arXiv v3 copy is retained locally. |
| `ratner_et_al_2020_snorkel` | Context for combining noisy and correlated labeling sources and training downstream discriminative models. | Existing expanded 2020 VLDB Journal publisher version retained; incoming arXiv/PVLDB 2017 version removed as a duplicate. |

## Remaining Citation and Validation Needs

| need | why it matters | status |
| --- | --- | --- |
| Prompt engineering or structured LLM elicitation | Supports the methodological framing of the staged prompt used to elicit candidate proxy-state ontologies, rule families, missingness reasoning, and DAG proposals. | partially addressed by the LLM-prior paper; no general prompt-elicitation or reporting reference was added |
| Transparent reporting of AI-assisted research or writing | Supports disclosure of LLM role, model, date, human review, and limits. | citation gap |
| Model or system documentation for ChatGPT 5.4 with extended reasoning | Supports the exact model/version description supplied by the user. | citation gap; metadata is user-reported |
| Clinical expert review of LLM-generated proposals | Needed before strengthening claims from "design proposal" to "clinically reviewed design". | not a literature citation by itself; requires project record |

## Wording Boundary

Use language such as "LLM-assisted clinical and causal knowledge elicitation," "LLM-guided proxy-state, decision-rule, and DAG construction," or "LLM-generated design proposals subsequently selected and encoded in deterministic project source code."

Do not describe the LLM as a validated medical domain expert, claim that it discovered the true causal graph, call the proxy states AI-validated clinical states, or imply that the cited papers validate this project's design choices. In particular, `darvariu_et_al_2024_llm_causal_graph_priors` evaluates soft priors on nonclinical benchmark graphs, and CliniCause does not implement the learned Snorkel generative label model described by `ratner_et_al_2020_snorkel`.

# LLM Prompt Provenance Audit

## Scope

This audit covers the artifacts under `thesis-writing/prompts-and-documents/` and their relationship to the proxy-state and DAG methodology drafted in Chapter 5. The goal is to distinguish:

- LLM-assisted design proposals and prompt-engineering artifacts.
- Human/project review documents.
- Source-code implementations.
- Executed pipeline artifacts.
- Clinical or chart-review validation evidence.

The directory was inspected read-only. No prompt, PDF, DOCX, or exported conversation artifact was edited.

## Artifact Inventory

| artifact | size | sha256 | role in thesis evidence |
| --- | ---: | --- | --- |
| `general-purpose-latent-causal-model-prompt.txt` | 35580 | `34b77c2cf5688af6aba54f07fcc21a3e5ef0001883963d0427e2e7569898013f` | Generic prompt-engineering template for latent/proxy ontology, rule, missingness, and DAG elicitation. |
| `physionet-prompt.txt` | 35589 | `0bf72593261298a8b1c8370a42e5601e651d2db8608f9282b9c912a415c7524e` | Final PhysioNet 2012 dataset-specific prompt. |
| `mimic-prompt.txt` | 35566 | `da4abd8c3ed1775d02aa300668542d68c83997d6d42cdabf7ad5b3bdd6468804` | Final MIMIC-III dataset-specific prompt. |
| `old-physionet-prompt.txt` | 35345 | `03cb08ee378fab17ec369f64b26ef7650d60e8ca11b2e0a7dde4bf92d5986060` | Earlier PhysioNet prompt version. |
| `old-mimic-prompt.txt` | 35209 | `053ab09501c911cfe0c8cce3afd689da010f8dd4dbad3a99703865412454be8f` | Earlier MIMIC prompt version. |
| `physionet-prompt-running.pdf` | 1827973 | `933c864a5c0679764d579d4617f5192c7f1db0a53cd74e5b0906b7297d98cb67` | Browser-exported final PhysioNet prompt run; 45 pages; created 2026-05-01 16:34:29 IDT. |
| `mimic-prompt-running.pdf` | 1705405 | `56271465a73f624151ba36b1b4c4a07ad0e4271a9bb7304256ede4155afbf79a` | Browser-exported final MIMIC prompt run; 44 pages; created 2026-05-01 16:33:37 IDT. |
| `old-physionet-prompt-results.pdf` | 1255602 | `a91cfb36e37d9b4d96ca89dceeae609f614b77967ee6db9de27c449c3cce406f` | Earlier PhysioNet output; 26 pages; created 2026-04-29 10:47:13 IDT. |
| `old-mimic-prompt-results.pdf` | 1440606 | `178da26831bb8052d1b19fb77c01028d60cd1e868353e74668a526b927e2c8fd` | Earlier MIMIC output; 28 pages; created 2026-04-29 11:07:49 IDT. |
| `Deep research report on CATE, latent tags, and validation signals in your causal-irregular-time-seri.pdf` | 85488 | `892a973bf8866832fbedc5c330d2c75a555db1cdbc2a3e15adcf8bd3b7aa4275` | ChatGPT Deep Research report; CATE/proxy-validation context; 11 pages. |
| `latent-causal-manager-summary.pdf` | 246407 | `d1c7383626182bdc4401067d2ec23d5cf1c80be158beb151e0cbdb7e02869409` | Word-exported management summary of latent/proxy causal design; 7 pages; created 2026-05-02 15:29:01 IDT. |
| `clinical_cate_manager_summary.pdf` | 169491 | `eb72ff78e6a8e7bf9a333f51c7e85ca17712af5a3e277c2208ba03861d78be16` | Word-exported management summary for clinical CATE review; 3 pages; created 2026-05-02 16:18:55 IDT. |
| `latent-causal-manager-summary.docx` | 53516 | `b23942dd6315ebab3ab090ccbf91bc4116b82ccc341d5aef6a2bac391816ae6e` | Editable source for latent/proxy causal management summary. |
| `clinical_cate_manager_summary.docx` | 42343 | `fcddf72342d8e97c8d3b81093a6cb235b583a9822a72c0a521066f4499c1106c` | Editable source for clinical CATE management summary. |
| `Thesis research question - internal document.docx` | 18902 | `09189ea46e07b6de10b00414af59df11d29744a4d1278ab0d8a08026f751e514` | Human/internal thesis-question document. |
| `reference-clinical_cate_ground_truth_validation - internal document.docx` | 195192 | `c0bf5b5b7566235e0e6f28cac30ddeade196813ed969355d1ad225f368e827d1` | Internal clinical-CATE validation reference document; not an implemented pipeline artifact. |

## Prompt Version Comparison

The final generic prompt and the two final dataset prompts are structurally identical except for the dataset global variables:

- PhysioNet final variables: `DATASET-NAME = PhysioNet 2012 Challenge`; `DATASET-DESCRIPTION-LINK = https://physionet.org/content/challenge-2012/1.0.0/`.
- MIMIC final variables: `DATASET-NAME = MIMIC-III`; `DATASET-DESCRIPTION-LINK = https://physionet.org/content/mimiciii/1.4/`.

The old-to-final prompt changes mainly introduce the reusable global-variable block and replace hard-coded dataset names/URLs with `DATASET-NAME` and `DATASET-DESCRIPTION-LINK`. The final PhysioNet and MIMIC prompts differ only in those two variable assignments.

## Prompt Protocol

The final prompts ask an LLM to act as an expert clinical causal inference, medical machine learning, and causal representation learning researcher. The staged protocol requests:

- Dataset audit from the official dataset description URL.
- Clinical and causal ontology proposal.
- Latent/proxy variable selection and definition.
- Rule-based binary decision-tree proposals.
- Missingness and measurement-process reasoning.
- Dataset-specific DAG construction.
- Iterative validation and final structured answer.

The prompts use language such as "true hidden clinical states", "causal correctness", and "clinically and causally justified latent DAG". Thesis prose must not carry those phrases forward as claims. They are prompt objectives for eliciting candidate designs, not evidence that hidden states, clinical truth, or causal identification were established.

## Execution Metadata

- Final prompt PDFs were exported from ChatGPT browser sessions using Chrome/Skia PDF metadata on 2026-05-01.
- User-supplied model metadata for the final prompt runs: ChatGPT 5.4 with extended reasoning.
- The PDF metadata records browser/export details and conversation titles, but it does not independently encode the model/version field.
- The exact research/browsing mode, system instructions, temperature/settings, follow-up prompts, and export procedure remain incompletely documented.
- Earlier prompt-result PDFs from 2026-04-29 do not contain exact model/version metadata in the PDF fields inspected.

## Output-Document Relationships

The prompt outputs and management summaries are best classified as design-provenance documents. They can support a methods-history statement such as "the proxy ontology and DAG design were developed with an LLM-assisted elicitation protocol and then encoded in source code." They cannot, by themselves, support:

- A claim that the implemented proxy labels are clinically validated phenotypes.
- A claim that the DAG was learned from data.
- A claim that the LLM executed the pipeline.
- A claim that the LLM output is the authoritative source of implemented labels or adjustment sets.
- A claim that the outputs prove causal identification or treatment effects.

## Prompt-Output-to-Code Traceability

The source-code authority for implemented proxy states and DAGs remains:

- `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`
- `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`
- `causal-irregular-time-series/src/physionet2012_causal_graph.py`
- `causal-irregular-time-series/src/mimiciii_causal_graph.py`

The final prompt reports align at a high level with the active source:

- PhysioNet final prompt output proposes 11 active `LAT_*` proxy states matching the active PhysioNet tagger schema.
- MIMIC final prompt output proposes 10 active `LAT_*` proxy states matching the active MIMIC tagger schema.
- Both final outputs discuss measurement/missingness process nodes, and the active graph layer contains measurement/missingness-oriented nodes.
- Rule families and graph structure are only partially traceable from the exported reports because the active source is more precise than the narrative prompt output.

Therefore, the thesis should cite source code and run artifacts for implementation, and use prompt artifacts only for design provenance.

## Scientific Role

Allowed wording:

- "LLM-assisted clinical and causal elicitation protocol."
- "Candidate proxy-state ontology, rule families, missingness considerations, and DAG design proposals."
- "Project-specified DAGs subsequently encoded in source code."
- "Design-provenance evidence."

Avoided wording:

- "LLM-discovered causal graph."
- "AI-validated clinical states."
- "Ground-truth latent variables."
- "Clinically validated DAG."
- "Causal discovery from patient-level data."

## Limitations

- Prompt artifacts are not source-code execution logs.
- Prompt artifacts are not clinical chart-review validation.
- Prompt artifacts do not prove that every proposed rule was implemented unchanged.
- Prompt artifacts do not provide patient-level performance, association, or causal-effect results.
- Model metadata is user-reported for the final runs and should be marked as such unless additional export metadata is recovered.
- Human/advisor/clinical review status of the LLM proposals is not fully documented in the inspected artifacts.

## Citation Needs

The current literature corpus supports EHR phenotyping, weak supervision, DAGs, causal inference, sensitivity analysis, datasets, and implemented models. It does not yet contain dedicated citations for:

- Prompt engineering or structured LLM elicitation protocols.
- Transparent reporting of AI-assisted scientific writing or design support.
- Model/system documentation for the exact ChatGPT 5.4 extended-reasoning product used here.

Until those citations are added, the thesis should keep LLM prompt provenance as a documented project process, not a literature-supported methodological contribution.

## Recommended Thesis Wording

Use:

> The proxy-state ontology and dataset-specific DAGs were developed through an LLM-assisted clinical and causal elicitation process and then reviewed, selected, and encoded as deterministic project source code. The LLM outputs are treated as design-provenance artifacts; the implemented proxy labels and graph artifacts are defined by the active tagger and graph scripts, and neither the prompt outputs nor the generated summaries constitute chart-adjudicated clinical validation.


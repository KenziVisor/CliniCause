# LLM methodology literature ingestion report

## Scope and disposition

Four PDFs were found under `thesis-writing/literature/new/`. Each was inspected with file-type, PDF-structure, metadata, page-count, text-extraction, title-page, abstract, methods, limitations, and conclusion checks before any disposition decision. Bibliographic fields were checked against the publisher or primary repository records linked below. Three papers were added as core corpus entries. The fourth was an earlier semantic/version duplicate of the existing canonical Snorkel paper and was removed only after the retained publisher PDF and its metadata were revalidated.

| original file | verified paper and copy type | size; pages; SHA-256 | authoritative bibliographic check | final disposition |
| --- | --- | --- | --- | --- |
| `s41586-023-06291-2.pdf` | Karan Singhal et al., “Large language models encode clinical knowledge,” corrected open-access Nature publisher version, 2023, 620(7972):172--180, DOI `10.1038/s41586-023-06291-2` | 4,867,390 bytes; 28 pages; `969d7f5ae18a244a4fc156914e6200c4962fac11132ac6a9a2518ae58e4741d4` | [Nature article record](https://www.nature.com/articles/s41586-023-06291-2); PDF footer identifies the corrected 2023 publication | Added as `singhal_et_al_2023_llm_clinical_knowledge` at `papers/llm_clinical_knowledge_singhal_et_al_2023.pdf` |
| `2405.13551v1.pdf` | Victor-Alexandru Darvariu, Stephen Hailes, and Mirco Musolesi, “Large Language Models are Effective Priors for Causal Graph Discovery,” arXiv v1 preprint marked “Under review,” 2024, arXiv `2405.13551`, DOI `10.48550/arXiv.2405.13551` | 725,536 bytes; 15 pages; `2062af1fb064ec8fb08ce3cae6117bdd80e148989fad2eeb151c70eccd3ddf97` | [arXiv record](https://arxiv.org/abs/2405.13551); submitted 22 May 2024 with no journal reference | Added as `darvariu_et_al_2024_llm_causal_graph_priors` at `papers/llm_causal_graph_priors_darvariu_et_al_2024.pdf` |
| `1605.07723v3.pdf` | Alexander J. Ratner, Christopher M. De Sa, Sen Wu, Daniel Selsam, and Christopher Ré, “Data Programming: Creating Large Training Sets, Quickly,” extended arXiv v3 copy of the NIPS 2016 paper, volume 29, pages 3567--3575 | 362,152 bytes; 27 pages; `2b5cb4ec06201e35bad7fd3e1a0d297eb1a2d832588bf140d983c5350b78b9e2` | [NeurIPS proceedings record](https://proceedings.neurips.cc/paper/2016/hash/6709e8d64a5f47269ed5cea9f625f7ab-Abstract.html) and [arXiv version record](https://arxiv.org/abs/1605.07723); the proceedings paper has no DOI, while `10.48550/arXiv.1605.07723` is the arXiv-issued DOI | Added as `ratner_et_al_2016_data_programming` at `papers/weak_supervision_data_programming_ratner_et_al_2016.pdf` |
| `1711.10160v1.pdf` | Alexander Ratner et al., “Snorkel: Rapid Training Data Creation with Weak Supervision,” arXiv v1 / PVLDB 11(3):269--282, 2017, DOI `10.14778/3157794.3157797` | 1,966,800 bytes; 17 pages; `ca0a8c147e8fc157c3600539a247140c1921a009e8814a6ebb715cc61a344737` | PDF identifiers and DOI were compared with the retained [Springer journal record](https://link.springer.com/article/10.1007/s00778-019-00552-1) | Confirmed as the earlier version of existing key `ratner_et_al_2020_snorkel`; removed. The retained canonical file is the expanded 22-page VLDB Journal publisher version at `papers/phenotyping_weak_supervision_snorkel_ratner_et_al_2020.pdf`, DOI `10.1007/s00778-019-00552-1`, SHA-256 `9c611b904d4e2ad2af11d1fe497120706fb4763d1657dba70fb08426baa456c6` |

The complete Nature author list and the exact author order for every new entry are transcribed in `metadata/references.bib` and `metadata/catalog.csv`. No venue or proceedings DOI was inferred. The Nature correction is recorded but not treated as a separate paper; it changed reference ordering rather than the article's methodological identity.

## Duplicate-resolution rationale

The incoming Snorkel PDF was not an exact-byte duplicate, but normalized title, authors, eprint, publication lineage, and DOI checks established that it was the earlier conference/arXiv version of the work already represented by `ratner_et_al_2020_snorkel`. The existing file is the expanded final journal version and remained fully readable through all 22 pages. Its non-fatal PDF linearization-hint warnings do not affect parsing or text extraction. The established citation key and canonical path were therefore preserved, and the catalog note records the removed file's identity and checksum.

## Corpus changes and validation

| measure | before | after |
| --- | ---: | ---: |
| Core catalog records | 35 | 38 |
| Optional catalog records | 5 | 5 |
| Total catalog records | 40 | 43 |
| Valid local PDFs | 38 | 41 |
| Intentionally missing PDFs | 2 | 2 |
| Checksum records | 38 | 41 |

The three new citation keys, normalized titles, DOI/eprint identifiers, canonical PDF paths, and SHA-256 values are unique. All 41 retained PDFs are recognizable, unencrypted PDFs with readable metadata and extractable content; all checksum records validate from the literature root. Every new BibTeX `file` path and catalog `pdf_path` resolves to the retained file. The catalog retains its pre-existing CRLF line endings. `thesis-writing/literature/new/` was deleted after all three moves, the duplicate decision, metadata updates, and checksum verification were complete.

## Methodological-use boundary

Singhal et al. support a bounded statement that evaluated LLMs can encode substantial medical knowledge while retaining important reliability and human-evaluation limitations. Darvariu et al. provide nonclinical methodological precedent for LLM judgments as causal-graph priors, not validation of the CliniCause DAGs. Ratner et al. provide the foundational programmatic-labeling reference, and the retained Snorkel paper supplies weak-supervision and discriminative-training context. CliniCause does not implement the full Data Programming framework or Snorkel's learned generative label model, and none of these papers validates the local proxy ontology, rules, graphs, or effect estimates.

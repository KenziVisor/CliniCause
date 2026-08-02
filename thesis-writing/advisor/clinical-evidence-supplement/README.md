# CliniCause clinical-evidence supplement

This directory is a standalone, anonymous source package for the supplementary document **Clinical Evidence for the Construction of the CliniCause Representation**.

## Source and audit layers

- `main.tex` — reader-facing standalone document.
- `references.bib` — references actually cited in the PDF.
- `source_registry.csv` — source provenance, local availability, Phase 2 status, verification status, and limitations.
- `proxy_evidence.csv` — the 19-row proxy evidence audit layer.
- `dag_edge_evidence.csv` — the 102-row DAG evidence audit layer.
- `generate_supplement_data.py` — deterministic generator/validator for the three CSVs and LaTeX table rows.
- `proxy_definition_rows.tex` — generated reader-facing proxy rows.
- `dag_edge_rows_mimic.tex` — generated MIMIC-III edge rows.
- `dag_edge_rows_physionet.tex` — generated PhysioNet edge rows.
- `main.pdf` — compiled deliverable.

The generator reads the authoritative edge inventories from:

- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-edges.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-edges.csv`

It does not copy clinical source PDFs into this directory.

## Rebuild

From this directory:

```bash
python3 generate_supplement_data.py
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated row files and CSVs are intentionally retained so that the rendered tables can be audited without parsing the PDF.

## Expected structural counts

- `proxy_evidence.csv`: 19 data rows
  - MIMIC-III: 9
  - PhysioNet 2012: 10
- `dag_edge_evidence.csv`: 102 data rows
  - MIMIC-III: 57
  - PhysioNet 2012: 45

Chronic/baseline constructs occur in the graphs but are not counted among the 19 admitted proxy exposures.

## Provenance rules

An `O_` source identifier is used only when a preserved final ChatGPT export contains the source. Exact, family-level, generally present, and missing mappings remain distinct.

A `V_` source identifier means:

> NEW INDEPENDENT-VERIFICATION SOURCE — NOT PART OF THE ORIGINAL CHATGPT ELICITATION

Later verification sources never repair missing original provenance. Historical proposal sources are not silently merged into final rows. Post-construction mortality-direction corroboration is excluded from construction evidence.

The PhysioNet active specification uses the default threshold dictionary.

## Unresolved evidence

Missing paper mappings, unavailable local full text, unsupported exact cutoffs, association-only evidence, and unverified directed causality are represented explicitly in the CSVs and PDF. Empty or negative evidence fields must not be inferentially filled.

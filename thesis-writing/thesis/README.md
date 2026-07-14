# CliniCause Thesis LaTeX Workspace

This directory contains the Stage 4.0 structural thesis skeleton. It intentionally contains headings, labels, front matter, appendices, placeholders, and build wiring only.

## Toolchain

- Engine: XeLaTeX through `latexmk`.
- Bibliography backend: `biblatex` with `biber`.
- Bibliography source: `../literature/metadata/references.bib`.
- Expected output: `thesis-writing/thesis/main.pdf`.

## Commands

Run commands from `thesis-writing/thesis/`.

Clean build:

```bash
latexmk -C
latexmk -xelatex main.tex
```

Incremental build:

```bash
latexmk -xelatex main.tex
```

Cleanup:

```bash
latexmk -C
```

## Required System Packages

Install a LaTeX distribution that includes `latexmk`, `xelatex`, `biber`, `biblatex`, `fontspec`, `polyglossia`, `geometry`, `setspace`, `fancyhdr`, `hyperref`, `booktabs`, and `longtable`.

## Known Current Blocker

The local environment used for Stage 4.0 did not have `latexmk`, `xelatex`, `pdflatex`, `lualatex`, `bibtex`, `biber`, or `tectonic` on `PATH`, so a PDF could not be generated here. The skeleton is configured for the commands above once the TeX toolchain is installed.

## Placeholder Policy

Do not replace placeholders with prose until the corresponding Stage 4 task is authorized. Placeholder inventory is tracked in `../logs/unresolved_placeholders.md`.

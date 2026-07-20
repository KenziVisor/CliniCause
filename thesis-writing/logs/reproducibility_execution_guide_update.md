# Reproducibility execution guide update

## Baseline and scope

- Branch: `main`
- Conversion-validation HEAD: `0fe0649f9abc2959eb9653a57379e555d7143b37`
- Task baseline: `0fe0649f9abc2959eb9653a57379e555d7143b37`
- Baseline comparison: HEAD exactly matched the prepared task baseline, so there were no intervening commits to classify.
- Worktree status before editing: ` M prompt.txt`
- The pre-existing `prompt.txt` modification was preserved and was not edited by this task.
- The prompt contains a legacy block that says not to create or rename requirements files, but its earlier dedicated Phase 1 expressly requires consolidation and says that phase must pass before scientific-document edits. The mandatory Phase 1 was treated as authoritative. No file inside either component directory was changed.
- Follow-up author direction established that `STraTS/` and `causal-irregular-time-series/` are regular tracked directories in the intended repository layout. The final guides therefore assume that an ordinary clone contains both directories and requires no secondary repository-initialization command.

The mandatory Git baseline commands were run before editing: `git status --short`, `git branch --show-current`, `git rev-parse HEAD`, and `git log -10 --oneline --decorate`.

## Instructions and implementation evidence inspected

The inspection covered the root `README.md`, `SCRIPTS.md`, the then-current `.gitmodules`, `run_clinicause.sh`, `router.py`, every root requirements file, both component `AGENTS.md` files, both component READMEs and requirements files, both source-specific preprocessing entry points, the thesis main/build files, the thesis appendix, the AAAI manuscript, the technical appendix, the Author Kit reproducibility checklist, paper build instructions and reports, and the existing records under `thesis-writing/reproducibility/` and `thesis-writing/logs/`.

Current source contracts confirmed the following:

- The intended final checkout contains `STraTS/` and `causal-irregular-time-series/` as ordinary directories; no secondary repository initialization is part of the supported reproduction workflow.
- `run_clinicause.sh` is the canonical launcher. Its defaults are `DATASET=both`, `OUTPUT_ROOT=runs`, `PHYSIONET_RAW_DATA_PATH=data/physionet2012`, `MIMIC_RAW_DATA_PATH=data/mimiciii`, `STAGES=all`, `STRATS_MAX_CONCURRENT=1`, and `PYTHON_BIN=python`.
- The launcher accepts absolute raw-data paths and resolves relative paths from the repository root.
- Both raw paths are passed as raw dataset roots to the source-specific causal-repository preprocessors. The guide does not invent an extracted hierarchy or download command.
- `dataset-extraction` runs the router's implemented stage sequence and changes the causal-program selector to `graph,majority_vote`. Its required terminal resource outputs are the dataset-specific graph artifacts, `latent_tags_majority_vote.csv`, and `run_summary.json`; it stops before the later causal estimators.
- Default output is `runs/<run-id>/<dataset>/`, with coordinator metadata at the common run root. Dataset manifests, resolved configuration, stage logs, provenance sidecars, hashes, cohort fingerprints, and stage receipts are current router contracts.
- `all` retains the complete integrated predictive and causal workflow.

Official PhysioNet project pages were checked to avoid treating unlike access policies as identical. [MIMIC-III v1.4](https://physionet.org/content/mimiciii/1.4/) is credentialed access and currently requires the specified training and data-use agreement. The [PhysioNet/CinC Challenge 2012 v1.0.0](https://physionet.org/content/challenge-2012/1.0.0/) is currently labeled open access under its displayed license. Both guides therefore direct users through PhysioNet and require compliance with the applicable current terms, while correctly reserving the restricted-data wording for MIMIC-III.

## Requirements consolidation

The actual supported umbrella filename is now the root `requirements.txt`. It directly declares the six existing parent/router packages and recursively includes:

```text
-r causal-irregular-time-series/requirements.txt
-r STraTS/requirements.txt
```

The superseded parent-owned `requirements-full.txt` and `requirements-router.txt` were removed. The active root README now directs users to `python -m pip install -r requirements.txt`. The old filenames remain only in copied audit snapshots, historical worktree records, provenance records, and earlier evidence reports; those occurrences were intentionally preserved as historical or archival facts.

Static parsing with pip's requirements-file parser resolved 32 entries without installation. The parent lower bounds are compatible with the causal component's exact pins, and the overlapping STraTS declarations are unpinned; no unresolved constraint conflict was found. Both recursive include targets exist.

## Repository layout conversion

At the author's follow-up request, the two clean component checkouts were converted from gitlinks to ordinary parent-repository directories. The conversion removed `.gitmodules`, both component `.git` marker files, and the two corresponding parent `.git/modules/` metadata directories. It then staged the regular directory contents without committing.

The staged parent index was compared against read-only copies of the original component revisions. All 152 originally tracked paths have identical blob hashes and modes; the two original executable scripts retain mode `100755`; 26 ignored cache files that were present on disk but absent from the original component indexes were left on disk and excluded from the parent index. The converted project tree has zero mode-`160000` gitlinks for the two former component submodules. At validation time, HEAD was still `0fe0649f9abc2959eb9653a57379e555d7143b37`; publication was requested afterward.

`git diff --cached --check` reports historical trailing whitespace because the structural conversion presents the byte-identical component files as additions. Those component bytes were intentionally not normalized. The ordinary unstaged `git diff --check` for the reproducibility and dependency edits passes.

## Files changed by this task

- `README.md`
- `requirements.txt`
- `requirements-full.txt` (deleted)
- `requirements-router.txt` (deleted)
- `.gitmodules` (deleted and staged as part of the regular-directory conversion)
- `STraTS/` (gitlink replaced in the index by its 67 regular tracked files)
- `causal-irregular-time-series/` (gitlink replaced in the index by its 85 regular tracked files)
- `thesis-writing/thesis/appendices/appendices.tex`
- `thesis-writing/paper-aaai/paper.tex`
- `thesis-writing/paper-aaai/supplement/technical_appendix.tex`
- `thesis-writing/logs/reproducibility_execution_guide_update.md` (new)

No research-code bytes, launcher, router, result, figure, table, unrelated caption, bibliography entry, author field, submission-mode setting, or style file was changed. The component-file entries changed only in parent-repository ownership: their blobs and modes match the former component indexes exactly.

## Documented commands

The detailed thesis and anonymous supplement guides contain the ordinary fresh-clone command, Python 3.10 Conda setup, root dependency installation, default and external raw-data locations, and the two canonical launcher commands:

```bash
git clone <repository-url>
conda create -n clinicause python=3.10 -y
conda activate clinicause
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
STAGES=dataset-extraction bash run_clinicause.sh
STAGES=all bash run_clinicause.sh
```

The thesis uses the exact public repository URL. The anonymous paper and supplement do not expose it.

## Paper anonymity decision

No approved anonymized repository or artifact URL was found. Existing paper planning and build reports explicitly keep that release input gated. The main paper therefore uses non-identifying prose, and the technical appendix uses the visible `<ANONYMIZED_REPOSITORY_URL>` token while explaining that it is a release gate. No author-identifying URL, name, affiliation, or anonymity-setting change was introduced. Author insertion of an approved anonymized repository URL remains the only unresolved human gate for these guides.

## Validation results

- Root requirements file exists; both obsolete parent files are absent: pass.
- Recursive requirements includes exist and parse statically: pass, 32 entries.
- Component conversion: pass, 152 exact blob/mode matches, two preserved executable files, and zero component gitlinks.
- Required command/path/variable coverage in both detailed guides: pass.
- Ordinary clone is the only documented repository setup; no secondary initialization command or nested-repository claim remains: pass.
- `bash -n run_clinicause.sh`: pass.
- Changed documents recommend no `run_clinicause_shell.sh`: pass.
- Paper anonymity scan for `github.com/KenziVisor` and `KenziVisor/CliniCause`: pass, no matches.
- Exact-historical-rerun claim boundary retained: pass.
- `git diff --check`: pass.
- Protected numerical/scientific content review: pass; no numerical result, count, metric, estimator finding, figure, table, or causal/clinical interpretation was changed.

## Build and PDF inspection

Builds were performed on clean copies under `/tmp` so tracked PDFs and auxiliary files in the working repository were not overwritten.

- Thesis: `latexmk -C` followed by `latexmk -xelatex main.tex` succeeded. Output: 104 pages, A4. The task-introduced appendix overflow warnings were repaired; remaining warnings are pre-existing elsewhere in the thesis. No fatal error occurred.
- AAAI paper: the existing `TEXINPUTS`, `BSTINPUTS`, and `BIBINPUTS` environment procedure with `latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` succeeded. Output: 8 pages, US letter, matching the tracked PDF's page count after the compact reproducibility text was integrated into the existing validation boundary. No overfull box was reported.
- Technical appendix: `latexmk -pdf -interaction=nonstopmode -halt-on-error technical_appendix.tex` succeeded. Output: 7 pages, US letter. The three small overfull warnings originate in pre-existing generated tables; the new workflow prose and command blocks introduced no overfull warning.
- Rendered inspection covered all six thesis appendix pages, the changed main-paper page, and both new supplement workflow pages. Commands and URLs were readable and unclipped; references were intact; no undesirable float movement was observed. The supplement grew from 6 to 7 pages. The thesis grew from 101 to 104 pages, reflecting the expanded self-contained appendix.

## Final worktree note

During validation, an untracked nested `CliniCause/` checkout appeared in the workspace. No command in this task created or modified that checkout. It was used read-only to verify the original component revisions after their nested metadata was removed, and it remains excluded from the published project tree and does not affect the static or isolated-copy build results.

## Readiness

READY FOR AUTHOR REVIEW WITH ANONYMOUS-REPOSITORY URL GATE

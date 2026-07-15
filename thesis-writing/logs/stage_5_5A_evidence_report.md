# Stage 5.5A Evidence Report

## Identity and scope

Verified repository head: `8367195905fca00a4d6611cdaee242086132c834` (`step 5.5`).

Verified immediate parent: `3e29da1d8c6b91ddc00d44b9637218ed0047e6a6` (`step 5.4`).

Before the Stage 5.5A repair, the Stage 5.5 commit introduced no thesis `.tex` change relative to its parent: its thesis-related additions were validation ledgers and the rebuilt PDF.  The five thesis figures were unchanged.

The worktree was already dirty on entry.  Its recorded user-controlled baseline included root documentation and router files, `prompt.txt`, dependency files, the nested `causal-irregular-time-series` worktree, test/config files, thesis literature metadata, Stage 5.2 and Stage 5.5 ledgers, checked-results CSVs, and project-overview copies.  Those entries were neither reset, staged, normalized, nor edited by this stage.  The Stage 5.5A protected snapshot covered 64 named path records and 396 recursive files before inspection.

## Commands and execution boundary

The following document/static commands were used (with paths resolved from the repository root unless noted):

```text
git rev-parse HEAD
git rev-parse HEAD^
git log -1 --format='%H%n%P%n%s' HEAD
git status --short
git show --stat 8367195905fca00a4d6611cdaee242086132c834
python3 /tmp/stage_5_5a_static_audit.py snapshot --root . --out /tmp/stage_5_5a_protected_initial.json
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
qpdf --check main.pdf
pdftotext -layout main.pdf
pdftoppm -png -r 300 -f <page> -l <page> main.pdf <output-prefix>
rg, sed, awk, sha256sum, and git diff --check (static inspection only)
python3 /tmp/stage_5_5a_static_audit.py snapshot --root . --out /tmp/stage_5_5a_protected_final_allowbreak.json
python3 /tmp/stage_5_5a_static_audit.py compare --root . --before /tmp/stage_5_5a_protected_initial.json --after /tmp/stage_5_5a_protected_final_allowbreak.json
```

The two temporary `python3` helpers used only the standard library to hash static files and parse LaTeX/PDF text and CSV data.  No research code, data loader, preprocessing, training, prediction, matching, CATE, sensitivity, permutation, figure-generation, test, router, or nested-project code was run or imported.

## Clean-build result

The clean baseline build produced 109 A4 pages, 48 overfull boxes, and 1,157 underfull boxes.  It had 0 unresolved citations, 0 unresolved references, 0 duplicate destinations, 0 Biber errors, 0 missing-glyph errors, 0 bidi errors, and 0 fatal errors.

After the one local layout repair, the final build has 109 A4 pages, 47 overfull boxes, and 1,157 underfull boxes.  The same zero-error checks remain true.  `qpdf --check` reported no syntax or stream-encoding errors.

## High-resolution review and warning localization

Every physical page, 1--109, was rendered as an individual PNG and inspected at 300 DPI.  This exceeds the 200-DPI requirement and covers all pages requiring 300 DPI: tables/longtables, figures, Hebrew and mixed RTL/LTR text, equations, long identifiers, bibliography entries, and every warning above 5 pt.  After the repair, physical pages 67--69 were regenerated and rechecked individually at 300 DPI; pagination remained 109 pages.

The 48 clean-baseline warnings are all localized with source file, line range, physical PDF page, visual disposition, root cause, and post-repair state in [stage_5_5A_overfull_localization.csv](stage_5_5A_overfull_localization.csv).  The individual-page evidence is in [stage_5_5A_full_resolution_pdf_review.csv](stage_5_5A_full_resolution_pdf_review.csv).  The warning-page distribution is: 1 (2), 2, 12, 39 (2), 41 (5), 46, 54, 64 (2), 67, 68 (5), 70, 72 (5), 73, 74 (7), 76 (6), 86 (3), 92, 94 (2), and 107.

The reported approximately 267.4-pt warning did not occur in the clean 48-warning build.  The largest observed baseline warning was 88.74751 pt at `chapters/08_robustness_sensitivity_validation.tex:44-45`, physical page 68.  It visibly crossed the right margin and is documented as `OVERFULL-17`.  The largest remaining final-build diagnostic is 83.23866 pt at `chapters/05_proxy_state_construction.tex:180-181`, physical page 46; its fixed-width table content was inspected at 300 DPI and is fully within the rendered crop, without clipping or overlap.

## Defects and repair

One material defect and one minor defect were found, both in the same Chapter 8 API-availability paragraph on physical page 68.  The 88.74751-pt line visibly extended beyond the right margin; the 14.20638-pt continuation extended slightly beyond it.

The only thesis source edit is in `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex:44`.  Four local `\allowbreak` points were added immediately after identifier underscores in the existing `\texttt{}` runs.  This preserves the exact prose and API identifiers while permitting legal line breaks.  The baseline two warnings at that paragraph became one 36.04349-pt TeX diagnostic; the final 300-DPI page inspection confirms that it has no visible margin intrusion, clipping, or overlap.  The adjacent pages remain clean.

No global spacing, margin, font-size, line-spacing, or suppression setting was changed.

## Content and integrity comparison

The scoped source diff contains only the four inserted `\allowbreak` controls.  Consequently, numerical tokens, citation keys, labels, table values, figure files, figure captions, and prose meaning are unchanged.  The figure directory hash is unchanged.  The final protected-hash comparison found exactly one delta: the authorized Chapter 8 `.tex` file.  It found zero deltas in results, reproducibility records, literature, figures, audit/planning material, all Stage 5.1--5.5 logs, `causal-irregular-time-series`, and `STraTS`.

Final PDF: `thesis-writing/thesis/main.pdf`  
SHA-256: `67e62c94bf5da78318b2094515897568ea6dea7723678903288f2256c472013f`  
Page count: 109

## Readiness decision

READY FOR AUTHOR FIRST-DRAFT REVIEW

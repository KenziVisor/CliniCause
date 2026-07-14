# Stage 4.6A Results Decision Register

All recommendations are nonbinding; no recommendation is enacted in checked tables.

## DEC-RESULT-001
- Question: primary causal sampling condition
- Available options: original; outcome-downsampled
- Verified evidence: Both exist; original retains population outcome rate while downsampled is a distinct analysis population.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: original for population interpretation; retain downsampled as separate sensitivity population
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-002
- Question: primary causal estimator
- Available options: CausalForestDML; LinearDML; CausalPFN
- Verified evidence: All twelve summaries exist; PFN skips downstream diagnostics.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: choose an estimator with complete archived diagnostics after human review
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-003
- Question: role of CausalPFN
- Available options: exploratory; supplementary; primary
- Verified evidence: PFN CATE summaries exist but diagnostic stages are intentionally skipped.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: exploratory/supplementary
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-004
- Question: matching estimand wording
- Available options: descriptive matched-pair difference; ATT-like; exclude
- Verified evidence: Archive reports mean_pair_effect only.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: descriptive matched-pair difference
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-005
- Question: mean_cate wording
- Available options: mean model-estimated CATE; other approved wording
- Verified evidence: Arithmetic summary of patient-level modeled CATE values.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: mean model-estimated CATE
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-006
- Question: normalized_CATE inclusion and wording
- Available options: omit; include with explicit normalization wording
- Verified evidence: Value divides by sample outcome rate.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: omit from main text pending wording approval
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-007
- Question: thesis-primary proxy-state exposures
- Available options: select subset; show all; none
- Verified evidence: Archived treatment sets differ by dataset.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: human selection based on construct review
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-008
- Question: original versus downsampled presentation
- Available options: original primary; downsampled primary; parallel
- Verified evidence: Both populations have distinct n/outcome rates.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: original primary, downsampled sensitivity
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-009
- Question: cross-dataset comparison scope
- Available options: qualitative; aligned proxy concepts; pooled
- Verified evidence: Schemas and proxy concepts differ.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: qualitative/aligned only; no pooling
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-010
- Question: sensitivity-contour selection
- Available options: choose one; appendix all; omit
- Verified evidence: Non-PFN contours are archived.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: appendix all pending selection
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-011
- Question: permutation main-text versus appendix role
- Available options: main; appendix; omit
- Verified evidence: Aggregate archived rows exist for non-PFN only.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: appendix pending source-interpretation review
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-012
- Question: overlap figure omission or generation requirement
- Available options: omit; create later
- Verified evidence: No dedicated overlap plot archived.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: omit with support limitations stated
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-013
- Question: InterpNet exclusion
- Available options: exclude; rerun later
- Verified evidence: No final summary or export archived.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: exclude numerical comparison
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-014
- Question: learning-curve figure selection
- Available options: select archived curve; appendix all
- Verified evidence: Archived PNGs exist.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: appendix candidate pending selection
- Recommendation confidence: medium
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-015
- Question: cohort-count source
- Available options: run summary; export; labels; recover manifest
- Verified evidence: Counts describe different contracts.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: report source-specific counts only
- Recommendation confidence: high
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

## DEC-RESULT-016
- Question: primary versus supplementary tables
- Available options: select hierarchy
- Verified evidence: All candidate tables are checked but no approved hierarchy is recorded.
- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.
- Provenance consequences: does not remove the archive, configuration, or split limitations.
- Recommended option: main predictive + qualified CATE candidate; appendices for diagnostics
- Recommendation confidence: low
- Human owner: thesis author and supervisor
- Current status: OPEN
- Required before Stage 4.6B: yes

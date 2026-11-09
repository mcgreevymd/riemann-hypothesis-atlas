# atlas2060: research bundle for RH Atlas v1.21

Prepared 8 Nov 2026, about 10 PM CST (America/Chicago).

This bundle organizes the work done after the v1.20 release:
- 23 scratch directories, from matching1989 through inertia2057;
- the follow-up conclusions on the boundary model and the arithmetic class map.

**The Riemann Hypothesis is not proved. No all-window positivity is claimed.**

## Read in this order

1. `SYNTHESIS.md`: themes and status tags.
2. `AUDIT.md`: binding corrections, re-derivations and the number cross-check.
3. `delta/DELTA_v121.md`: the concepts and relations to add.
4. `RELEASE_NOTES_v121.md`: changelog draft.
5. `FIGURE_STORYBOARD.md`: figure captions.

Integration steps for the repo agent are in `OVERVIEW_PROMPT.md`.

## Headline

- E0 positivity of the window Weil form is established up to width A = 1.1:
  - analytic for A ≤ 0.1;
  - interval-certified for A ≤ 0.694;
  - computer-assisted with an IEEE-754 error model for A ≤ 1 and A ≤ 1.1.
- Exactly one negative direction off E0 is certified at A = 1 and 1.1. It is absorbed by the two moment constraints.
- Beyond A = 1.1 there are numerics only.
- The missing object is an arithmetic class map Φ with a computed intersection pairing.

## Reproduce

- Quick checks: `python3 SMOKE_TEST.py`.
- Full rerun of all 47 scripts: `OPENBLAS_NUM_THREADS=1 python3 rerun_all.py`, about 10 minutes. It writes `checks/rerun_results.json`, and `checks/RERUN_REPORT.md` summarizes it.
- Requires python3, numpy, scipy, mpmath, sympy and matplotlib.
- `ref/` holds the v1.20 atlas.json and CHANGELOG, used for collision checks. It is not part of the proposal.

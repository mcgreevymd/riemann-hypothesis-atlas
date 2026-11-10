# atlas2105: research bundle for RH Atlas v1.22

Prepared 10 Nov 2026, about 12:30 AM CST (America/Chicago).

This bundle organizes the work done after v1.21 (merge `deaaf83`):
- the scratch directories evec2064, gammau2068, cutoff2072, framing2073, route22078, vary2083, prime2087, r2trop2097 and ccrr2098;
- the conversation conclusions t2068–t2104;
- the new-connections pass night2105.

**RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.**

Read in this order: SYNTHESIS.md, AUDIT.md (binding), delta/atlas_delta_v122.json, RELEASE_NOTES_v122.md, FIGURE_STORYBOARD.md.

Reproduce: `python3 SMOKE_TEST.py` (about 20 s). The full night2105 scripts are in `scripts/night2105/`; n3_weyl.py takes about 7 minutes. Requires python3, numpy, scipy, sympy and matplotlib.

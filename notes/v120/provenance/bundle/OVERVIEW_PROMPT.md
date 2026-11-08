# atlas1987 — OVERVIEW PROMPT for the cloud integration agent and the manuscript writer
Authorization context: user message pt1987u (Nov 7 2026): "finish up our current tests. Write and push a new atlas revision, with figures and animation.
Use this as a way to refine ideas for the manuscript. Then write and push a new manuscript to ai.vixra … I'm giving you permission."
Order: Atlas revision (v1.20 proposed) FIRST, then manuscript "Arithmetic Unification VI", then ai.viXra submission (by the coordinator, not by this bundle).

## Inputs (this bundle, /workspace/taa/atlas1987/ or research_bundle.zip)
PUBLICATION_AUDIT_matching1983.md (parent math audit; cite OVER raw notes) · SYNTHESIS.md (ranked front section + concept/relation names + next theorem) · AUDIT.md (binding overrides A1–A24, contradictions D1–D5) ·
SOURCE_MANIFEST.md (sha256 of every file, citations) · FIGURE_STORYBOARD.md · figures/ (3 figs + supplementary + GIF + generator scripts) ·
scripts/ (existing checks per directory) · data/ (json/npy outputs) · notes/ (verbatim scratch notes, archived unedited — AUDIT overrides them).

## Cloud agent (repo mcgreevymd/riemann-hypothesis-atlas, baseline release v1.19)
1. Verify baseline commit/counts from the live repo (parent-reported main 65153b7…, 1025 concepts / 1990 relations; not verified locally).
2. Add a front section "Since v1.19" built from SYNTHESIS ranked items 1–9 in that order; central aim paragraph first (thermodynamic / RH-unitarity, not conic).
3. Add the proposed concepts/relations; check for name collisions; every node carries its status tag (EXACT/THEOREM/NUM/SKETCH/CONJ/MODEL/CLOSED).
4. Add figures/animation with the storyboard captions; copy scripts/data needed to regenerate into the repo's reproducibility area.
5. Apply every AUDIT override verbatim in spirit; do not quote notes/ text that AUDIT marks WRONG without the correction.
6. Mark the closed routes list and the "next missing matching theorem" box. Keep "RH is not proved" on the landing page and in every figure.
7. Do not include credentials, private paths, or chat text in the repo.

## Manuscript writer (Arithmetic Unification VI)
Thesis framing: an exact arithmetic energy ledger for the Weil form on log-windows, with every term given an independent local/thermodynamic meaning, a reduction of
window positivity to a bordered-inertia (count + sign) criterion, and a precisely stated missing matching theorem; conic/Hodge polarity as a model of the target sign pattern.
Sections: 1 Intro & aim (no proof claim) · 2 Ledger (W=P+B, E0, M_A) · 3 Local product-state reading · 4 Semilocal trace identity (twisted star; time delay) and the two-Hankel obstruction ·
5 Bordered inertia and moments (hypotheses; numerics as uncertified tables) · 6 Matching test: two candidates fail; prime-edge kink · 7 One-form polarity model and Künneth signs;
dimension caveat (A21) · 8 Calibrations (Rankin–Selberg, Ramanujan system, Iwasawa regularity) · 9 Closed routes · 10 Open problem (next theorem). Appendix: reproducibility.
Hard rules: abstract and conclusion state RH is not proved and no positivity result is claimed; numerics labelled uncertified; cite Connes 1999, Connes–Consani 2020, Weil,
Haynsworth, Hartshorne V.1, Tate, Rankin/Selberg, Ramanujan; no claim that a universal no-go or a Hodge structure exists.

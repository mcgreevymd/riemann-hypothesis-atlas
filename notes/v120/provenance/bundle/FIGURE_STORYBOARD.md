# atlas1987 — FIGURE STORYBOARD (3 figures + 1 animation; prototypes already rendered in figures/)
All script-generated (matplotlib), vector SVG + PNG, every panel footed "The Riemann Hypothesis is not proved." Regenerate:
`cd figures && python3 make_figures.py && python3 make_fig3_candidates.py` (needs numpy, scipy, matplotlib, pillow; ~30 s). Cloud may restyle; may not change numbers or labels' status tags.

## Fig 1 — "The exact ledger and where the sign is missing" (fig1_ledger.svg)
Purpose: central TAA aim first. Left: the identities W = P + B, P = 2ev+ev− = 2(C²−S²), B = H_A − M_A‖F‖² = (1/2π)∫m_A|F̂|², M_A, K0; "E0 kills P only".
Right: per-place contributions at A=2, F=(∂²−1/4)G, G=sin⁸ (covariance1956): arch +0.090, p=2 +9.092, p=3 −9.001, p=5 −0.0016, total W = 0.1788 [NUM]
(rounded parts sum to 0.1794; caption must say rounded). Message: massive cancellation, per-place indefinite; covariances enter subtracted.
Option for cloud: add subtraction arrow "white − colored" per prime.

## Fig 2 — "One form, two jobs" (fig2_polarity.svg)
Left: model discriminant conic q = t²/4 (null, Δ=0; neutral label — not the Hasse wall itself), shaded timelike interior, Legendre tangent family, focus h=(0:1:1) with Q(h)=−4, polar = directrix with
Q|_{h⊥} = v_T²+4v_Z² > 0, axis span(h,x∞) signature (1,1), x∞ null with self-containing polar. Right: H¹ alternating → H¹⊗H¹ symmetric, −8 mixed (1,1) primitive vs +8 (2,0)+(0,2).
Caption must carry A14, A16, A19, A21: model only; conic smooth at ∞, not a cusp; no finite target can carry W faithfully.

## Fig 3 — "Testing the missing matching theorem: two explicit candidates fail" (fig3_candidates.svg) [replaces uncertain A=2 spectrum per parent]
(3a) h1 = cosh·1_win: r_{h1}/cosh vs edge distance d (log axis), slope ½ log(1/d) — EXACT mechanism, NUM curve.
(3b) h2 Dirichlet cosh, A=1: residual r_{h2} − κcosh shows kinks at ±(log 2 − A/2) = ±0.193; derivative jump a_2 sinh(A/4)/2 = 0.06191 EXACT.
Caption: "only these two candidates fail; no general no-go (A20)."
Supplementary (optional, appendix only): figS_moment_spectrum.svg — λ1(B_e), λ2(B_e), E0 estimates (not certified brackets) for A=0.6, 1.0; A=2 marked UNRESOLVED; Ritz = upper bounds.

## Animation — "Interior polarization degenerating to the null boundary" (anim_polarity.gif, 48 frames, 8 fps, ~0.3 MB)
Frames: s from 1 → 0.05 then hold. Left: Legendre tangents (fixed, grey) of the same conic; point h_s=(0:1:s) at q=1/s rising; its polar q=−1/s falling;
title Q(h_s) = −4s (homogeneous gauge; affine-normalized (0,1/s,1) gives −4/s — state both). Right: unit set of Q on the complement v_Z = −s v_Q, Q = v_T² + 4s v_Q² — ellipse stretching to a strip as s → 0.
Footer states schematic algebra, not a physical recording. Narrative: Legendre tangents → same conic's polarity → interior definite complement → degeneration at x∞.

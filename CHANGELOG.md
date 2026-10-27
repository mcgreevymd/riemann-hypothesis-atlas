# Changelog — The RH Atlas

## v1.1 — 27 Oct 2026

- 183 concepts (+52) and 529 typed relations (+250).
- Folds TAA Lemmas 148–153: where positivity comes from (the definite cup square; definition vs source; formal lattice vs geometric surface), Laguerre's formula and the Cayley–Klein absolute, the conic type at infinity (ellipse = Hasse), half turns as sign flips; Legendre strata (support functions, dual conics, the Maxwell construction); the blockwise Weil-form diagnostic, which detects the Davenport–Heilbronn off-line zeros from the coefficient side alone; limiting mixed Hodge structures, Consani's archimedean cohomology, weight–monodromy and the Connes–Consani log 2 window; Legendre ↔ Fourier (Maslov) and the critical line as the unitary spectrum of scaling; the Poincaré disk and adelic gluing; the cusp as the tying section (Eisenstein resonances at ρ/2, Selberg's eigenvalue conjecture, CM points and Epstein zeta, the Maass–Selberg intercept); Connes's cokernel (the positive space sees only the critical zeros; "quotient positivity" withdrawn as a positivity statement).
- The distortionless cusp (TAA Lemma 153 §7.5): Birman–Krein and the Lorentzian splitting of −φ′/φ, S(T) as the fluctuating remainder, Heaviside's condition, Lax–Phillips scattering, Wigner time delay, purity as distortionless transmission.
- New: Verschiebung as the positive adjoint of Frobenius (FV = q is ghost-blind; V = F† for a positive form is the RH-type statement); the Morse picture of lobes, wedges and hyperbolic windows.
- TAA Lemma 154: Γ, the width of a zero (the FWHM of its Breit–Wigner line; RH ⇔ all widths vanish); zeros as Breit–Wigner resonances with cusp doublets; width → area → the zero-counting 2-form; why the area is π (the circle). The refined Davenport–Heilbronn zero list of TAA Lemma 154 is now the standard list.
- Wording fixes: the positivity-inventory line and the Hasse = Cauchy–Schwarz entry.
- TAA Lemma 155: the ghost map. Davenport–Heilbronn's off-line zeros are detected from the prime side (coefficients, Γ-factor and functional equation), without a zero list; β̂ = 0.80852, 0.65083 [Numerical].
- TAA Lemma 156: certified zero lists (ball arithmetic). The standard Davenport–Heilbronn list for 2 < t < 135 is complete: 79 zeros, 75 on the line plus 4 off it. Certified Γ₁ = 0.617034364913274771106 ± 9·10⁻²² and Γ₂ = 0.30166016121947416481 ± 3·10⁻²¹. Two further off-line pairs near t ≈ 166.48 and 176.70 are recorded separately. Corrected cusp widths for ghost 2 [Numerical, rigorous; Theorem given the certificates].
- Figures: two equivalent labelled figure sets, the concept-colour set (`figures/animation_labelled/`, one colour per concept) and the detailed-annotation set (`figures/animation_detailed/`). They show the same content with different emphasis. Also new: the Kramers–Kronig absorption-vs-gain figure (`figures/kk/`).
- README: leads with the figures, then "Where RH is likely to live"; the top-15 table has been regenerated from the current ranking.
- License: CC BY 4.0 (`LICENSE`).

## v1.0 — 26 Oct 2026

First public edition.

- 131 concepts, each with a plain-language summary, a precise core statement, a label (Theorem / Restatement / Analogy / Conjecture / Open / Numerical / Heuristic / Cited), axes, corrections and cautions, and references to the TAA lemma series.
- 279 typed relations between concepts.
- The organizing split: phase/unitarity structure is ghost-blind; the sign of a spectral weight is ghost-sensitive, and for ζ that sign is RH.
- Ten missing pieces, each stated precisely with what is proved around it and the tests it must pass.
- The Connes–Consani Riemann–Roch analysis on the square of the scaling site (TAA Lemma 147), and the distinction between the two different χ’s (Euler characteristic vs class-group character in the 691 story).
- New entries on the quadratic character and the prime 2: Gauss’s half and the (p + 1)/4 square-root formula, 2 as the wild prime, Gauss-sum unitarity, the primary sign rule for a_p, the elliptic-curve Chebyshev bias, and Hilbert reciprocity at 2. These are planned for development in a later TAA lemma; citations still to be checked are marked “to verify”.
- A Heuristic scoring layer (gap significance, sensitivity, specificity, tractability, evidence) and a diagnostic 2×2 quadrant view. All lists are presented in descending priority, with `#rank · priority` in each header.

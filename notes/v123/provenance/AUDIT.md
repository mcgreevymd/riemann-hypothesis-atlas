# AUDIT v1.23 (binding; overrides SYNTHESIS and notes)

1. **Priority.** t* = 0.28119957, a ≤ t*/2, the Perron theorem for the pole-free part (all windows), the rank-two parity split and the even-sector scalar reduction are de Andrade Silva's (Zenodo 20682833, 13 Jun 2026). v1.23 claims only the closed form t* = log P (plastic number), as far as checked; Suzuki's paper was not checked for it.
2. **Galerkin.** Every eigenvalue for A > log P is a Rayleigh–Ritz value. Positive minima are not certificates of W ≥ 0 on the window, and "one negative eigenvalue" means one in each Galerkin space tested. For A ≥ 2.5 the tiny eigenvalues are not converged in the basis size.
3. **Precision.** Only runs stable under digit doubling are reported. 60-digit runs at A ≥ 3 were wrong (spurious sign changes and negatives) and are excluded.
4. **Basis attribution.** Q ground states −1.98747, −4.30591, −7.23122, −11.2308 (A = 1–4) are Legendre-basis values (M = 220, 160 digits). The sine basis at N = 200 gives −1.9839, −4.2959, −7.2115, −11.1942, still drifting.
5. **Scope.** CCM even-simplicity is a diagnostic of the approximants. It does not produce Φ, ω or J, and it does not touch (D). L192 (Hilbert J) is a closed route, not progress.
6. **Corrections to the manuscript are recorded, not applied.** TARGET.md is unchanged; proposed rows await J.W.'s OK.
7. **Literature reading depth.** de Andrade Silva ×2: abstract and TeX read. Mehennaoui: abstract and theorem statements read, proofs not checked. Suzuki: Theorem 1.4 read in t2252.

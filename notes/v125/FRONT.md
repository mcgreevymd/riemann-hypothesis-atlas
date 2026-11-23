## Since v1.24

Links are relative to the repository root (this file is included in README.md).

> **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.** Nothing in v1.25 touches the compatibility condition (D) ([J, Θ] = 0 on ℋ). The certified E0 gaps are still the v1.21 ones (A ≤ 1.1). Every statement for larger windows is numerical (Galerkin: minima are upper bounds, negative counts lower bounds). Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

**New in v1.25.** Work of 20–22 Nov 2026 (America/Chicago). Counts: 1115 concepts (+2) and 2278 typed relations (+12). Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. Two additions only, approved by J. W. McGreevy.

Tags: **[Exact]** an identity or a literature fact; **[Closed]** a restatement or closed route.

### Einstein / Hagedorn on the Bost–Connes row
- **[Exact]** Einstein's 1917 derivation of B₁₂ = B₂₁ (hence Planck's law from A/B coefficients plus Boltzmann statistics) uses the high-temperature limit ρ → ∞. The primon gas's thermal description ends at the Hagedorn point β_H = 1 (the pole of ζ), and the Weil form lives beyond it, on Re β = ½ (complex β). So the step that forces detailed balance in physics is unavailable for ζ; continuation past β = 1 runs through the functional equation, which Davenport–Heilbronn and Epstein zetas (e.g. Z_{x²+5y²}) share. Recorded on the Bost–Connes / KMS-primon entry, on the Theorem 3.2 table row, and as `einstein_hagedorn_bc`.

### Constraint / Dirac framing
- **[Exact + Closed route]** In the Lagrange/Dirac-constraint picture of Q (norm constraint ‖f‖² = 1, pole constraints f̂(0) = f̂(1) = 0 or ⟨f, cosh⟩ = 0, the pencil Q − λ·norm, Poisson brackets such as {xy, x²+y²} = 2(y²−x²)), every element is built from Q alone and is sign-neutral: Davenport–Heilbronn and Epstein zetas share it. Relative to Q the pole plane is already nondegenerate (1,1), i.e. a second-class pair, with no Euler product used; Q-orthogonal reduction of that plane gives index 1 only, not Q ≥ 0 on E0 (TAA Lemma 194). The Hamiltonian J (rotation of the (x, y) plane) is not TARGET's J (a complex structure on ℋ compatible with ω); brackets with respect to TARGET's ω are undefined until piece (B) exists. The only multiplicativity-using constraint expressible here is simultaneous eigen-constraints for the commuting Hecke / scaling-by-p family; it rejects Z_{x²+5y²} = ½(ζ_K + L(s,χ)), K = ℚ(√−5), only because it is a sum of two Euler products, so it is the Euler-product filter (`prime_torus_nonresonance`, #884: selects pure modes) and supplies no sign (cf. TAA Lemma 196: 𝔽_q fakes with Euler products fail Hodge index). Any sign-giving, prime-dependent constraint beyond this would have to encode finite-place intersection data, i.e. the missing square Spec ℤ × Spec ℤ. Recorded as `constraint_dirac_framing_route`.

**Open, in order of bearing on Φ.** Unchanged from v1.24.

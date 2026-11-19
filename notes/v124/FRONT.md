## Since v1.23

Links are relative to the repository root (this file is included in README.md).

> **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.** Nothing in v1.24 touches the compatibility condition (D) ([J, Θ] = 0 on ℋ). The certified E0 gaps are still the v1.21 ones (A ≤ 1.1). Every statement for larger windows is numerical (Galerkin: minima are upper bounds, negative counts lower bounds). Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

Work of 17–18 Nov 2026 (America/Chicago). Counts: 1113 concepts (+12) and 2266 typed relations (+49). Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. [AUDIT.md](notes/v124/provenance/AUDIT.md) overrides the synthesis and the notes. Full text: [SYNTHESIS.md](notes/v124/SYNTHESIS.md). Lemmas: [L194](notes/v124/provenance/notes/LEMMA_194.md), [L195 draft](notes/v124/provenance/notes/LEMMA_195_draft.md), [L196](notes/v124/provenance/notes/LEMMA_196.md), [L197](notes/v124/provenance/notes/LEMMA_197.md); checks: [CHECKS_t2271_2286.md](notes/v124/provenance/notes/CHECKS_t2271_2286.md).

Tags: **[Proved]** hand proof or exact algebra; **[Numerical]** Galerkin or exact-integer computation without a positivity certificate; **[Framing]** an analogy; **[Closed]** a restatement or closed route.

Window r = length of [−r/2, r/2]; C± = ∫F e^{±u/2}; P = 2C₊C₋; W = Q + P; E0 = ker C₊ ∩ ker C₋; cosh^⊥ = L² complement of cosh(u/2).

### TAA Lemma 194: the ample direction
- **[Proved]** Translation acts on the pole plane as a boost, maps E0 of a window onto E0 of the shifted window, and leaves Q and W invariant. P has eigenvalues r ± 2sinh(r/2) with eigenvectors cosh(u/2) and sinh(u/2).
- **[Closed: Restatement]** Over all windows, RH ⇔ Q ≥ 0 on E0 for every r (Weil) ⇔ Q ≥ 0 on cosh(u/2)^⊥ for every r. The one-way statement is about Q's ground state: RH ⇒ λ₁(Q_r) ≥ 0 (index 1), not conversely. On a single window, W ≥ 0 ⇒ Q ≥ 0 on cosh^⊥ ⇒ Q ≥ 0 on E0. In the function-field dictionary the ample class f₁ + f₂ is cosh, not h_r.
- **[Proved]** Q is Markov on every window (Λ ≥ 0), so its ground state h_r is positive and even for all r. **[Numerical]** corr(h_r, cosh) ≥ 0.993 for r = 1–10.

### TAA Lemma 195 (draft): onset law and a matched entire control
- **[Numerical]** The proposed law σ′·r* = const fails. Over 15 Davenport–Heilbronn quartets σ′r* = 0.09–1.58 and R² = 0.02 against log γ. The ledger law r* ≈ A·log(qγ/2π) + B − (0.1–0.3)·ln σ′ stands (R² = 0.90–0.98).
- **[Numerical]** Z₂ (2x² + 2xy + 3y²) starts failing early because its lowest zero 2.079 + 7.629i lies outside the critical strip.
- **[Numerical]** L(s, χ mod 5) with χ(2) = i is positive on W, E0 and cosh^⊥ up to r = 8, while DH (same Γ factor, q = 5, entire) fails at 3.58 (fine basis). Both have signed coefficients. The separator is prime-power support together with the FE, not the sign of Λ.
- **[Closed]** The σ-pencil test is already TAA L165 and the d = −20 pencil is already L173. The claim that on-line zeros carry opposite signs is false: they contribute |F̂|² ≥ 0, and the apparent sign changes are phase crossings. T4 was dropped.

### TAA Lemma 196: anatomy of the sign over F_q (genus 2)
- **[Numerical, exact integers]** Ablation ladder for q = 3–13: FE shape; integrality; N_n ≥ 0; nonnegative closed-point counts (a genuine Euler product); the hyperelliptic twist; Jacobian orders. After all count rungs, 12/172/586/2555/4322 off-circle fakes survive at q = 3/5/7/11/13. Rung (iv) reproduces L166 and is now certified for all degrees.
- **[Proved]**
  - Thm 196.1: N_n ≥ 0 for all n ⇒ every |α| ≤ q (the enumerated box is complete).
  - Hodge index on ⟨f₁, f₂, Δ, Γ_n⟩ at one n ⇔ the Weil bound at n.
  - **[Numerical]** The depth needed to kill every fake is N*(q) = 4/5/7/9/12, so it grows with q.
- **[Proved]** Thm 196.4: the function-field window form W has rank ≤ 2g, and the pole term is a real off-circle FE pair β = q^{±½} entering with multiplicity −1. So n−(Q) = n−(W) + 1, and every fake fails by window 2g − 1, independent of its distance from the circle.
- **[Proved + Numerical]** 196.6: changing one closed-point count breaks the FE. Adding a point fails at once. Removing one keeps W > 0, but the object is not pure. So the FE is needed for "positivity ⇒ purity".
- **[Closed]** (B) restates TARGET T-D2: the sign comes from Frobenius being a morphism (effective graphs, Riemann–Roch, an ample class). **[Framing]** (D) as stated is framing. Naming: TARGET's Q_ff is L194's W.

### TAA Lemma 197: Euler × FE ablation with failure localization
- **[Numerical]** The matched families are ζ; ζ_K for d = −20 together with L(χ₋₄)L(χ₅) and the pencil (ζ_K + λ·L(χ₋₄)L(χ₅))/(1 + λ), which includes Z₁ (λ = 1) and Z₂ (λ = −1); and L(χ mod 5) against DH. Results to r ≤ 8:
  - The 4 true members stay positive.
  - All 36 single-ingredient fakes fail: FE-only at r* = 0.85–5.7, Euler-only at 0.78–4.6.
  - The pencil's λ < 0 branch fails early: λ = −0.3 → 2.0, λ = −0.7 → 1.15 (E0).
- **[Proved]** For a one-prime perturbation, the negative direction lies on that prime by construction, so the "p₀ share" test proposed in ledger §351 is vacuous.
- **[Numerical]** The detection lag r* − log p₀ is the informative quantity:
  - It grows with the analytic conductor: 0.08–0.43 for ζ, 1.8–3.8 for ζ_K.
  - It grows by ≈ 0.03–0.06 per e-fold of 1/|ε|.
  - Truncations restate ledger §304.
  - For the FE-only fakes, composites carry 0–87% of the defect (DH 74%, Z₁ 47%).
- **[Numerical]** The prime-free ("flat") background of the ζ class is positive only up to r ≈ 0.78. So the prime 2 is load-bearing almost immediately.
- **[Proved]** Deleting a local factor and restoring its diagonal term (log p·‖F‖²) adds a positive Poisson form. An Euler product without the FE can therefore be window-positive. This is the ζ-side twin of L196.6, and as in L196.6 it is not pure.
- **[Closed: Restatement] Reconciliation with L196.** The ζ/DH separation by Euler × FE (ledger §351) is a diagnostic pattern. It is not evidence that these ingredients carry the sign: over F_q, thousands of fakes have both and still fail. In both settings the true forms are rigidly, marginally positive (the Galerkin minima fall to 10⁻⁸–10⁻¹⁰ by r = 8), so ablation measures fragility, not the source of the sign.

### Filter sort and closed routes (t2271–t2286)
- **[Closed]** About 75 ledger lemmas were binned by whether their proof step uses the Euler product: E 12, S 16, D 24, C 9, P 10, N 4. No Euler-using step produces the sign. The filter itself is the ledger's standing control (`euler_fe_conjunction`).
- **[Closed]**
  - Maass–Selberg/Witten positivity holds for DH too. Its unitary axis sits half a unit off ζ's line (the ½ offset, TARGET C16).
  - Ruppeiner curvature is flat for an Euler field, and real-β positivity is ghost-blind (L116).
  - ζ's zeros are Fisher zeros, not Lee–Yang zeros (L124).
  - Hodge star on 2-forms: on a Riemannian 4-manifold, ∫F∧*F = ‖F‖² ≥ 0 and *² = +1. The intersection pairing ∫F∧F can be indefinite. The earlier statement that ∫F∧*F is indefinite was wrong. The supplied Riemannian metric is not the missing arithmetic sign.
  - f∗f̃ is positive-definite but not an effective class.
- **[Framing]**
  - Gravity reading of E0: P is the invariant mass², E0 has zero 2-momentum, Q is internal energy.
  - Quartet language: degree sets the zero density N(T) ≈ (T/2π)·log(qT^d/(2πe)^d); the conductor sets the resolution scale.
  - Equivalence-principle reading of the window: primes enter one at a time at r = log n.
- **Corrections to that last reading:**
  - Short-window agreement holds only inside a class with the same Γ factor and the same poles.
  - Z₂ has a₁ = 0. Its prime side lives at frequencies log(m/2^k), and the first is log(3/2) ≈ 0.405. An earlier check said log 2; that was wrong.
  - 0.2812 = log P is the Markov threshold, not a positivity threshold. Positivity on E0 is certified for A ≤ 1.1.
- **[Framing + Closed]** Kepler perpendicularity dictionary: cosh ↔ angular momentum, sinh ↔ Runge–Lenz vector, cosh^⊥ ↔ the orbital plane, J = L̂×.
  - Kustaanheimo–Stiefel: fixed negative-energy Kepler motion becomes, after a time change and a constraint, an oscillator on ℂ² with a compatible positive metric. It is an analogue of (D), not an arithmetic realization.
  - With ω = dx∧dy and J multiplication by i, ½ω(z, Jz) > 0. The flow is e^{−it} under the convention i_Xω = dH, up to frequency normalization.
  - It does not transfer, for three reasons:
    1. There is no canonical J on a complement in infinite dimensions.
    2. Q is indefinite (the pole plane), so nothing is inherited.
    3. ζ's flow is a boost, so a hidden rotation with positive generator is Hilbert–Pólya.
  - The RH-equivalent statement uses the L² complement ⟨F, cosh(u/2)⟩ = 0, i.e. f̂(0) = −f̂(1) with f̂(s) = ∫F e^{(s−½)u}du. When Q(cosh) < 0 and the restriction is nondegenerate, the Q-orthogonal complement gives only index 1.
  - KS, Moser and Runge–Lenz are already in the atlas (`ks_quaternion_lift`, `moser_orbit_space_s2xs2`, `lrl_hidden_symmetry_trichotomy`). Rotating-frame/Lagrange is closed (L161, C14).

**Open, in order of bearing on Φ.** Unchanged from v1.23. L196 (B) sharpens the requirement: the ℚ side must supply effective classes against an ample class with a Riemann–Roch-type theorem. No condition on prime counts, the Euler product or the FE can suffice by itself.

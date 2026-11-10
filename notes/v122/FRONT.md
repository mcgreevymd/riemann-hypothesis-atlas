## Since v1.21

Links are relative to the repository root (this file is included in README.md).

> **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.** The certified E0 gaps are still the v1.21 ones (A ≤ 1.1). Every statement for A > 1.1 is numerical. Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

Work of 9 Nov 2026 (America/Chicago). Counts: 1088 concepts (+22) and 2173 typed relations (+65). Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. [AUDIT.md](notes/v122/provenance/AUDIT.md) overrides the synthesis and the archived notes. The full text is in [SYNTHESIS.md](notes/v122/SYNTHESIS.md).

**Status tags.**
- **[Exact]** an identity or hand proof; **[Cited]** literature.
- **[Numerical]** no error certificate.
- **[Obstruction]** a no-go in the stated scope only.
- **[Cooked]** a match only because the answer was inserted.
- **[Analogy]** no arithmetic map.
- **[Open]** missing.

<p align="center"><a href="figures/v122/fig1_two_walls_shioda_tate.png"><img src="figures/v122/fig1_two_walls_shioda_tate.png" width="900" alt="Two walls and a finite-window Shioda–Tate split"></a><br><sub><b>Two walls, one missing H¹.</b> (a) The chart determinant pᵏ − 1 is carried by the primes ℓ | pᵏ − 1, never by p (product formula) [Exact]. (b) n₋(W|E0) = n₋(Q) − n₋(S): only the true prime weights keep the counts equal at A ≥ 1.5; failures add bound states [identity Exact; counts Numerical; s ≠ 1 is a control, not Euler data]. (c) The Riesz lifts of C± behave like the fibre classes f₁, f₂ [Numerical, mesh-dependent]. (d) Over F_q, near-null = numerically trivial (Cayley–Hamilton) [Exact]; for ζ no window has an exact kernel. <b>RH is not proved; Φ is not constructed.</b></sub></p>

### The class map Φ: what was built
- **[Exact, semilocal]** Graphs of scaling [Γ_u] exist for every real u, with ⟨[Γ_u], K⟩ = e^{−u/2}∫K(λ_u x, x)dx. Their fixed-point loci give k∞ (x∞ = 0, all u) and Λ(n)/√n (x_p = 0). This is a trace pairing, not an intersection of currents.
- **[Exact]** The renormalized fixed-point pairing is lim[Tr − 2⟨F,G⟩ log Λ] = M_A − H_A = −(W − P). On E0 it equals −W. The divergence is subtracted, not cancelled, and P is not produced. Residual 1.3e−40.
- **[Exact + Numerical]** (h_sym, h_asym) = (2cosh(u/2), 2sinh(u/2)) has I-signature (1,1). The negative Q-mode is even, with cosine 0.995 to h_sym at A = 1. "W(H_lift) < 0" is the wrong test, and that lock is dropped.
- **[Exact, function field]** Φ_ff = Σ c_k q^{−k/2} Γ_{Frob^k} has bidegree (C₋, C₊). Toeplitz invariance forces the half-density, and the primitive pairing is −W_ff.
- **[Open]** Requirements on Φ:
  - **R1:** bidegree (1, e^u).
  - **R2:** the min-composition law.
  - **R3:** a log p fibre component over p.
  - **R4:** ζ, not cusp forms, in the primitive part.
  - **R5 (new):** no window kernel.

### Closed or narrowed routes
- **[Obstruction]** Green currents on P¹×P¹ give 6 − 4 log|e^u − e^v|, a log height, not k∞.
- **[Cooked]** First variations give weight-0 and weight-1 traces. k∞ appears only when inserted.
- **[Obstruction]** Hecke squares X₀(N)² carry L(f,s), not ζ.
- **[Obstruction]** On Arakelov P¹_Z×P¹_Z, Γ̂_n = Δ̂ + div̂(f_n), so all intersections are independent of n.
- **[Exact + Obstruction]** In the tropical Cartier model, R2 is a theorem, but the model is genus 0: Ψ(e^a)·Δ = e^a + 1 gives P only.
- **[Obstruction]** Connes–Consani Riemann–Roch on the square has no n² term: dimensions are additive and Pic⁰(C_p) = ℤ/(p−1).
- **[Obstruction]** R2 and R3 cannot both hold in one real PL chart. That would need a chart Jacobian (p^k − 1)/log p, which depends on k.

### Two walls and the missing H¹
- **Determinant wall.** Intersections give |det(1 − dψ)|, while the explicit formula needs its inverse times a length (the trace shape).
- **n² wall.** No continuous fibre Picard object exists on the scaling site.
- **Both crossed classically.** The Jacobian / H¹ crosses both, through Lefschetz: #Fix = 1 − Tr(Frob | H¹) + q^k.
- **[Cited]** Connes' cokernel H¹ is zeros-free and gives the trace after a cutoff, but it has no polarization.
  - The Fréchet quotient has a trace and no inner product.
  - The L² quotient has positivity, but sees only on-line zeros.
  - "Positivity + isometry + convergence to W" is Weil's criterion, not a no-go.
- **[Open]** The live lead is the semilocal prolate boundary condition.

### New connections
1. **The determinant wall is the product formula [Exact].**
   - pᵏ − 1 = #G_m(F_pᵏ) and pᵏ + 1 = #P¹(F_pᵏ). With the half-density these are h_asym and h_sym.
   - log(pᵏ − 1) = Σ_{ℓ | pᵏ−1} v_ℓ log ℓ with ℓ ≠ p, and |1 − pᵏ|_p = 1.
   - So the graph meets Δ over other primes, never over p. A log p atom must be a vertical fibre degree.
   - This unifies three no-gos: the real chart, P¹_Z, and the p-adic determinant.
2. **A finite-window Shioda–Tate split [identity Exact; counts Numerical].**
   - With Triv = span{Q⁻¹r±}: E0 = Triv^{⊥_I}, I|Triv = −S, and **n₋(W|E0) = n₋(Q) − n₋(S)**.
   - The Hodge index for I = −Q is "H_A has one bound state below M_A."
   - For ζ both counts are 1 at A = 0.694–2.5.
   - Under prime-weight controls, failures add bound states while the trivial lattice stays rigid.
   - The Riesz lifts' Gram tends to J, like the fibres f₁, f₂ (mesh-dependent).
3. **The pole plane is a boundary condition [Exact].**
   - In the family Q + BΘBᵀ: Θ = 0 gives Q, Θ = J gives W, and Θ → ∞ gives W|E0.
   - Krein: spec W|E0 = zeros of det M(λ), with M(λ) = Bᵀ(Q − λ)⁻¹B.
   - When n₋(Q) = 1, E0-positivity ⇔ det M(0) < 0. For ζ the penalty threshold is c* ≈ 0.99999 (≤ 1, as W ≥ 0 requires).
   - The prolate lead becomes a membership question: a zeros-free Θ_A in a cone.
4. **Near-null = numerically trivial; genus ∞ [Exact over F_q; contrast exact for ζ; rest Analogy].**
   - Over F_q the Weil Toeplitz form has rank 2g, with kernel the multiples of L̃ (Cayley–Hamilton).
   - For ζ, completeness of {e^{iγu}} on every interval means no window has an exact kernel.

**[Numerical]** The 1e−5 E0 plateau above A = 1.1 is a mesh floor, falling like about h^1.8. The near-null eigenvector's transform vanishes at γ₁…γ₈, the known ζ-cycle phenomenon.

**Open, in order of bearing on Φ.**
1. A space in which Ψ(pᵏ) ∩ Δ has a vertical component over p of degree log p.
2. A geometric one-bound-state theorem for H_A below M_A.
3. The prolate boundary condition written as Θ_A, and whether it is admissible.
4. A zeros-free effective genus 2g(A).
5. Intersection theory on the Connes–Consani square.

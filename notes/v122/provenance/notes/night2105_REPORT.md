# night2105: new connections after tonight's work (scratch, nothing pushed)

Mon 9 Nov 2026, about 11:50 PM CST through 10 Nov 00:30 CST. **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity. Open ~1.8 is unchanged.**
Tags: [Exact] identity or hand proof · [Numerical] computation without an error certificate · [Analogy] structural reading with no arithmetic map · [Open] missing.
Scripts and outputs in this directory: common2105.py (the inertia2057 cell model plus controls), n1_*, n2_*, n2b_*, n2c_*, n3_*, n3b_*, n4_*, make_figures_v122.py, figs/.

## N1. The determinant wall is the product formula
- **Analogy.** A real chart's intersection number |det(1 − dψ)| = p^k − 1 is a point count of the torus G_m over F_{p^k}. Compactified, 1 + p^k is the count for P¹. Either way the chart is genus 0. It sees only the Tate part (weights 0 and 2) and never a weight-1 H¹. That is why the tropical, P¹_Z and real-chart models all reproduce P and nothing else.
- **Precise version.**
  - [Exact] R1 forces dψ = μ, so each transversal fixed point carries |1 − μ|. At μ = p^k this is the Lefschetz number on H*_c(G_m), with eigenvalues 1 and p^k.
  - [Exact] With the half-density, e^{−u/2}(e^u + 1) = 2cosh(u/2) = h_sym and e^{−u/2}(e^u − 1) = 2sinh(u/2) = h_asym. So the t2073 signature-(1,1) pair is literally (P¹ count, G_m count).
  - [Exact] Product formula: log(p^k − 1) = Σ_{ℓ | p^k−1} v_ℓ log ℓ with ℓ ≠ p, and |1 − p^k|_p = 1. The graph of ×p^k meets Δ over the primes ℓ with p^k ≡ 1 (mod ℓ), and never over p.
  - This is the same cancellation as t2087 §3 (finite 2 log(n−1) against archimedean −2 log(n−1)). It is also why the p-adic determinant gives 1 rather than log p.
  - Checked for every p^k ≤ 10⁶ with p < 60: maximum error 1.8e−15 (n1_product_formula.json).
- **Verdict.** Exact and elementary. It merges three no-gos into one statement: the real PL chart, Arakelov P¹_Z, and the p-adic determinant. A log p atom at p cannot be a determinant of a horizontal graph. It has to be a vertical fibre degree, deg(Spec F_p) = log p. That is R3 restated. It does not build Φ.
- **Question for the other LLM.** "Let Ψ(μ) be a family of correspondences on a 2-dimensional arithmetic space T with bidegree (1, μ). In every model tested so far (real PL charts, tropical P¹×P¹, P¹_Z×P¹_Z), the fixed locus of Ψ(p^k) is horizontal: torsion points of G_m. By the product formula, its degree is carried by the primes ℓ | p^k − 1 and never by p. Construct T, or prove none exists, in which Ψ(p^k) ∩ Δ has a vertical component over p of Arakelov degree exactly log p and multiplicity 1, which rational equivalence does not cancel against the archimedean place. Say which axiom of an arithmetic surface (properness over Spec Z, the product formula, or finite rank of NS) must fail. Mark the step you are least sure of."

## N2. A finite-window Shioda–Tate split: Hodge index as a single bound state
- **Analogy (the t2081–82 rank/BSD thread).** For an elliptic surface, NS = Triv ⊕ (Triv)^⊥. The height pairing is minus the intersection form projected away from Triv (Shioda). The Hodge index theorem says Triv is hyperbolic and the complement is definite. Faltings–Hriljac is the arithmetic version, with Néron–Tate heights.
- **Precise version.**
  - [Exact, finite dimension] Let Q = H_A − M_A be invertible, I := −Q (the zeros-blind renormalized pairing of t2072), H_± := Q⁻¹ r_± (the Riesz lifts of C±) and Triv := span{H_±}. Then:
    - E0 = ker C± is exactly the I-orthogonal complement of Triv;
    - I|Triv has Gram −S, with S = Bᵀ Q⁻¹ B;
    - I|E0 = −W.
  - Hence In(I) = In(−S) ⊕ In(−W|E0), and **n₋(W|E0) = n₋(Q) − n₋(S)**.
  - "Hodge index for I", meaning exactly one positive direction, is n₋(Q) = 1. In words: **H_A has exactly one eigenvalue below M_A, a single bound state.**
  - E0-positivity ⇔ n₋(Q) = n₋(S).
  - [Numerical] For ζ, n₋(Q) = n₋(S) = 1 at A = 0.694 to 2.5. The identity holds in all 84 runs (n2_shioda_tate.json).
  - [Numerical, mesh-dependent] The lifts behave like the fibre classes f₁, f₂ (f_i² = 0, f₁·f₂ = 1). At A = 3, n = 1024: I(H₊,H₊) = 1.4e−5 and I(H₊,H₋) = 0.99999. The defect shrinks under refinement, which ties it to the t2064 mesh floor (n2b_fibres.json).
  - [Numerical controls; not Euler data] Scale every prime weight by s:
    - At A = 1.5 and 2, only s = 1 keeps E0-positivity at a resolution of 0.01.
    - Every failure adds bound states: n₋(Q) rises to 2–10 while n₋(S) stays at 1.
    - Deleting n = 2 at A = 1 or 1.1 raises n₋(Q) to 2, but n₋(S) also rises to 2, so E0 stays positive there. At A ≥ 1.5 the trivial lattice no longer absorbs the extra bound state (n2c_scale_sweep.json).
- **Verdict.** The identity is exact. The counts are numerical. Certified n₋(Q) = 1 exists only at A = 1 and 1.1, from v1.21. The new content:
  - the trivial lattice is rigid (it looks like U = ⟨f₁, f₂⟩);
  - the sign sits in the bound-state count of the zeros-blind pairing I;
  - that count is saturated at the true Euler coefficients.

  This sharpens the target for Φ: a geometric reason that H_A has one bound state below M_A for every A. It does not prove RH, because both counts are needed.
- **Question.** "On L²[−A/2, A/2] let H_A be the window jump-energy operator, with the archimedean kernel k∞(a) = e^{−a/2}/(1 − e^{−2a}) and prime atoms Λ(n)/√n at ±log n. Let M_A = −K₀ + 2Σ_{log n<A} Λ(n)/√n be its regularized mass, so that I = M_A − H_A is the renormalized fixed-point trace pairing. Numerically H_A has exactly one eigenvalue below M_A for A ≤ 3, and a 1% change in all prime weights adds bound states. On C×C over F_q the corresponding statement is the Hodge index theorem, proved from an ample class H with H² > 0 plus Riemann–Roch: D·H = 0 and D² > 0 force nD or −nD effective. Give the window analogue of that ampleness-plus-effectivity argument, or explain why a one-bound-state theorem must use the exact Euler coefficients and so cannot be variational. Mark the step you are least sure of."

## N3. The pole plane is a boundary condition (Krein–Weyl function): a home for the prolate lead
- **Analogy.** Self-adjoint extensions of a symmetric operator correspond to boundary conditions Θ. Their spectra are read off a Weyl function M(λ) by Krein's resolvent formula. The open t2104 lead says the semilocal prolate extension is fixed by a boundary condition at |x| = λ.
- **Precise version.**
  - [Exact, finite dimension] Define Q_Θ = Q + BΘBᵀ, with Θ a symmetric 2×2 matrix.
    - Θ = 0 gives Q.
    - Θ = J gives W, since P = BJBᵀ.
    - Θ → ∞ gives the compression to E0, the "Dirichlet" condition C± = 0.
  - Krein's formula: det(Q_Θ − λ)/det(Q − λ) = det(I + ΘM(λ)), with M(λ) = Bᵀ(Q − λ)⁻¹B. M is Herglotz: M′ = Bᵀ(Q − λ)⁻²B ≥ 0.
  - So spec(W|E0) = the zeros of det M.
  - When n₋(Q) = 1: E0-positivity ⇔ det M(0) < 0 ⇔ some positive-definite Θ makes Q_Θ ≥ 0.
  - For Θ = cI the threshold is c* = 1/|λ_min M(0)|. Because |C₊|² + |C₋|² − P = |C₊ − C₋|² ≥ 0, positivity of W on the whole window forces c* ≤ 1.
  - [Numerical] At every eigenvalue of W|E0, M(λ) is singular: relative σ_min is 1e−6 to 1e−15, against 0.02–1 at the midpoints.
  - c* = 0.99997 at A = 1.1 and 0.99999 at A = 1.5 and 2.
  - The controls with n₋(Q) ≥ 2 admit no c (n3_weyl.json, n3b_krein_direct.json).
- **Verdict.** An exact reformulation plus a computed check. It is not a sign source. It turns "a sign from a boundary condition" into a checkable membership: a zeros-free Θ_A in the cone {Θ > 0 : det(Θ⁻¹ + M_A(0)) < 0}.
- **Question.** "Connes–Consani's semilocal prolate operator W_λ commutes with the Sonine projection, and its self-adjoint realization is fixed by a boundary condition at |x| = λ. Restricted to a log-window of width A, with boundary map F ↦ (C₊(F), C₋(F)), C± = ∫F e^{±u/2}, write that condition as a symmetric 2×2 parameter Θ_A in Q_Θ = Q + BΘBᵀ. If the boundary space is not 2-dimensional, say what it is. Then decide whether Θ_A lies in the cone det(Θ_A⁻¹ + M_A(0)) < 0, where M_A(0) = Bᵀ Q_A⁻¹ B and Q_A = H_A − M_A, for a reason independent of the zeros and of W. Mark the step you are least sure of. A Θ_A defined through ξ or ĝ(γ_ρ) is circular."

## N4. Near-null = numerical equivalence (Cayley–Hamilton), and "genus ∞ on every window"
- **Analogy.** Over F_q, the Frobenius graphs satisfy the characteristic polynomial of Frobenius on H¹ modulo numerical equivalence. The near-null eigenvector of t2064 has f̂(γ_k) ≈ 0, which looks like an approximate "ξ-Cayley–Hamilton relation".
- **Precise version.**
  - [Exact, checked on genus 1 and genus 2; residuals ≤ 1e−12 (n4_cayley_hamilton.json)] On the window k = 0..K, the Weil Toeplitz form has rank min(K+1, 2g). Its kernel is spanned by the coefficient vectors of the multiples of L̃(x) = ∏(x − β_i). Also G − P = −W_ff. Hodge index makes the primitive form definite, so a null vector c gives a numerically trivial class Σ c_k q^{−k/2} Γ_k.
  - [Exact, cited] For ζ, W(F) = Σ_ρ ĝ(γ_ρ). Under RH, W(F) = 0 forces F̂(γ) = 0 for every ordinate γ. The ordinates have infinite density (N(T) ~ (T/2π) log T). By the Beurling–Malliavin/Levinson completeness theorem, {e^{iγu}} is complete in L²(I_A) for every A, so W has no exact kernel on any window.
  - So the function-field kernel of dimension K + 1 − 2g has no ζ analogue: **every window has "genus ∞"**. The near-null cluster seen in t2064 is the shadow of that, not a finite-genus relation.
  - [Analogy] The Fréchet cokernel H¹ is like homological equivalence: the trace holds and all zeros are seen. The L² quotient is like the numerical quotient: positive, with off-line hyperbolic planes (e_ρ paired with e_{1−ρ̄}) annihilated. RH then reads as "Hodge standard conjecture on the numerical quotient plus no off-line hyperbolic planes". That is a restatement of Weil's criterion, not a mechanism.
- **Verdict.** Exact over F_q. Exact "no kernel" for ζ (conditional on RH only to place the zeros; completeness needs only the density). The rest is analogy. It adds requirement R5: Φ's numerical-equivalence kernel must be trivial on every window. NS must have infinite rank already window by window, which strengthens R3. The finite rank of CH¹(P¹_Z×P¹_Z) (t2087) and the finiteness of Pic⁰(C_p) (t2098) both fail R5 for the same reason.
- **Question.** "Over F_q, rank W_ff = 2g on any window longer than 2g, by Cayley–Hamilton for Frobenius on H¹. For ζ, W has trivial kernel on every window, by completeness of {e^{iγu}}. Give a zeros-free asymptotic for n_A(ε) = #{eigenvalues of W|E0 on L²(I_A) above ε} as A → ∞ with ε fixed. Is it governed by A·log(A)/2π (Riemann–von Mangoldt), by the prolate count (Landau–Pollak), or by neither? Say which object plays '2g(A)', the effective genus of the window. Mark the step you are least sure of."

## What changed and what did not
- New: one exact unification (N1), one exact split with a new numerical diagnosis (N2), one exact boundary-condition calculus (N3), and one exact function-field fact with a clean ζ contrast (N4).
- Unchanged: rank 1 (`kahler_triple_polarization`), Open ~1.8, the v1.21 certificates (A ≤ 1.1). No statement for A > 1.1 is more than numerical.

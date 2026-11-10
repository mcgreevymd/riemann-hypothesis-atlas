# Since v1.21: the class map Φ, two walls, and a finite-window Shioda–Tate split

Work of 9 Nov 2026 (America/Chicago), after RH Atlas v1.21 (published 8 Nov 2026, 10:40 PM CST; merge `deaaf83`).

> **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.** The certified E0 gaps are still only the v1.21 ones (A ≤ 1.1). Every statement for A > 1.1 is numerical. Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

**Status tags.**
- **[Exact]** an identity or hand proof; **[Cited]** literature.
- **[Numerical]** a computation without an error certificate.
- **[Obstruction]** a no-go in the stated scope only.
- **[Cooked]** a construction that matches only because the answer was inserted.
- **[Analogy]** a structural reading with no arithmetic map.
- **[Open]** missing.

**Sources.**
- Scratch directories: evec2064, gammau2068, cutoff2072, framing2073, route22078, vary2083, prime2087, r2trop2097, ccrr2098, night2105.
- Conversation conclusions t2068–t2104. Items with no scratch file are marked *(conversation)*.
- AUDIT.md overrides this file and the archived notes.

**Notation (as in v1.21).**
- I_A = [−A/2, A/2]; C± = ∫F e^{±u/2}; E0 = ker C₊ ∩ ker C₋.
- W = P + H_A − M_A‖F‖², with P = 2 Re C₊ conj C₋.
- Q = W − P = H_A − M_A; B = [r₊, r₋], r± = e^{±u/2}; S = Bᵀ Q⁻¹ B.
- I := −Q, the renormalized fixed-point trace pairing.
- k∞(a) = e^{−a/2}/(1 − e^{−2a}); a_n = Λ(n)/√n.

## 1. The class-map programme: what was built

1. **[Exact, semilocal] Graphs of scaling for every real u (t2068).**
   - ⟨[Γ_u], K⟩ = e^{−u/2} ∫_A K(λ_u x, x) dx on the adèle class space. This is the Schwartz kernel of the unitary scaling θ_u. It uses no zeros and no ξ′/ξ.
   - Φ(F) = ∫ F(u)[Γ_u] du is a distribution kernel, the kernel of θ(F).
   - The fixed-point loci produce the explicit-formula pieces:
     - x_∞ = 0 is present for every u, and its index averaged over ±1 is k∞(a);
     - x_p = 0 is present only for u ∈ ℤ log p, and gives the atoms Λ(n)/√n.
   - k∞ comes from the x_∞ = 0 locus, not from the diagonal self-intersection.
   - X carries no intersection product, so this is a trace pairing, not an intersection of (1,1)-currents.
2. **[Exact] Renormalized pairing = −(W − P) (t2072).**
   - Subtract the 2 log Λ divergence; it is subtracted, not cancelled.
   - What remains is M_A − H_A = −(W − P) exactly, so on E0 it equals −W. The pole term P is not produced, because no fixed point gives it.
   - Checks:
     - window A = 1.1 with F ≠ G, log 2 and log 3 active: residual 1.3e−40;
     - nested quadrature: residual 1.4e−16.
   - This repeats counterterm1995 in the t2068 convention.
3. **[Exact + Numerical] The (h_sym, h_asym) frame (t2073).**
   - h_sym = 2cosh(u/2) and h_asym = 2sinh(u/2) are I-orthogonal by parity.
   - I has signature (1,1) on their span: I(h_sym) > 0 and I(h_asym) < 0 at every tested A.
   - The unique negative Q-mode is even, with cosine 0.9949 to h_sym at A = 1 (0.9937 at A = 1.1, 0.9996 at A = 3). This is numerical; only the index count is certified.
   - Riesz-lift signs: I(H_sym) ≈ +2 and I(H_asym) ≈ −2.
   - E0 is not I-orthogonal to h_sym.
4. **[Correction] "W(H) < 0" is the wrong test, and the lock is dropped (t2084, conversation; t2073 §6).**
   - Finite W has n₋(W) = 0, and under RH W ≥ 0 on the whole window.
   - The coherent ample-type tests are Q(h) < 0 for functions and −⟨v, Q⁻¹v⟩ > 0 for Riesz lifts.
   - Neither is independent of the v1.21 inertia certificate.
5. **[Exact, function field] The template that forces the half-density (t2087 §1).**
   - Φ_ff(c) = Σ c_k q^{−k/2} Γ_{Frob^k} has bidegree (C₋, C₊). E0 = Φ⁻¹(primitive).
   - The Gram is Toeplitz, and Toeplitz invariance forces the weight q^{−k/2}.
   - Full pairing = P − W_ff; primitive pairing = −W_ff.
   - The prime block is Γ_k·Δ, a transversal count, giving Λ_ff(n)/√n. The log q is the Jacobian of k ↦ u.
   - Hodge index gives W_ff ≥ 0.
   - Checked on genus 1 and genus 2 point counts.
6. **[Open] Requirements R1–R4 on Φ (t2087).**
   - R1: Γ_u has bidegree (1, e^u) for real u, so C± are the two degrees and E0 is the primitive part.
   - R2: Γ_λ·Γ_μ = min(λ, μ) (Γ_{λ/μ}·Δ), which forces e^{−u/2}.
   - R3: Γ_{p^k}·Δ contains a multiplicity-1 component of Arakelov degree log p over p, not killed by rational equivalence. So NS has infinite rank.
   - R4: the primitive sector carries ζ, not cusp forms.

## 2. Closed or narrowed routes (tonight)

| route | result | tag |
|---|---|---|
| Green currents on P¹×P¹ (t2078) | T = 6 − 4 log\|e^u − e^v\| exactly, for any fixed metric; a log height, not k∞ | [Obstruction] |
| First variation of [Γ_u] (t2083) | variations give weight-0 and weight-1 local traces (1/(1−q), −1/sinh²(a/2)); k∞ needs weight ½ plus the ±1 projection, and matches only when inserted by hand | [Cooked] |
| Hecke squares X₀(N)² (t2087 §2) | the primitive part is the prime block of L(f,s), the wrong target; ζ appears only in the rank-2 trivial lattice and the cusp | [Obstruction] |
| Arakelov P¹_Z×P¹_Z (t2087 §3) | Γ̂_n = Δ̂ + div̂(f_n), so every intersection is independent of n; finite 2 log(n−1) cancels archimedean −2 log(n−1); CH¹_R is 3-dimensional; no log p | [Obstruction] |
| Tropical Cartier model (t2097) | R2 is a theorem there (G_μ*Ψ(μ) = μΔ), but the model is genus 0: Ψ(e^a)·Δ = e^a + 1 gives only P (kernel 2cosh(a/2)), with no atoms and no k∞; the min-kernel is positive definite, an ample-type sign on the trivial part only | [Exact] + [Obstruction] |
| Connes–Consani Riemann–Roch on the square (t2098) | CC23 dimensions are additive, so χ(nD) is linear in n; CC17 has finite Pic⁰(C_p) = ℤ/(p−1); no n² term. The classical n² is the Jacobian with Rosati, a closed route | [Obstruction] |
| One real PL chart with R1–R3 (t2099–t2101, conversation) | \|det(n_{p^k}, n₁)\| = p^k − 1; a chart change multiplies by one fixed \|det J\|⁻¹; matching log p for all k would need \|det J\| = (p^k − 1)/log p, which depends on k. **R2 and R3 cannot both hold in one real PL chart** | [Obstruction] |
| Dreamer constructions (t2092–t2101, conversation) | Construction A is cooked. Construction B is the Guillemin–Sternberg flow trace (orbit length × \|det(1−dψ)\|⁻¹), a trace shape and not an intersection. A p-adic determinant at p gives 1, not log p | [Cooked] / [Exact] |

## 3. Two walls (t2101–t2102, conversation)
- **Determinant wall.** An intersection number gives |det(1 − dψ)| (p^k − 1, or e^a ± 1). The explicit formula needs the inverse times a length (log p, k∞), which is the trace shape. Every model tested lands on one side.
- **n² wall.** The sign needs a continuous fibre Picard object. The scaling site has none (t2098).
- **[Exact, classical]** In Weil's proof the Jacobian crosses both walls. Lefschetz turns det(1 − Frob) on H¹ into fixed-point counts, #Fix(Frob^k) = 1 − Tr(Frob^k | H¹) + q^k, and the same H¹ supplies the n² term in Riemann–Roch on C×C. The target is an H¹-type object attached to the scaling site, not a better chart.
- **[New, N1 below]** The determinant wall is the product formula.

## 4. H¹ candidates and the polarization problem (t2102–t2104, conversation)
- **[Cited]** Connes' cokernel H¹ = L²(C_ℚ)/closure(ℰ(𝒮₀)) is defined without zeros. It reproduces the explicit formula as a trace after a cutoff (requirement (a)). It does not meet (b): no fibre-class map lands in it and there is no n² term.
- **[Exact]** Fréchet versus L² dichotomy:
  - the Fréchet quotient has an unconditional trace and no positive inner product;
  - the L² quotient has automatic positivity, and its trace sees only on-line zeros, so (a) there is equivalent to RH.
- **[Correction]** "Positivity + (1) + (2)" is Weil's criterion. It is not a no-go: any successful polarization proves RH, which is the goal. The dreamer's Bochner step overreaches. A positive scaling-invariant limit only forces off-line eigenclasses to have norm zero; it says nothing about whether they exist.
- **[Correction]** The dreamer's fibre-class map x ↦ [Σ c_i ψ_{μ_i}(x)] ∈ H¹ is not defined. Its n² term is W inserted by hand.
- **[Cited]** As defined, Sonine/prolate spaces are archimedean-only. They model k∞ with a cutoff, not the primes.
- **[Open, live lead]** Connes–Consani's semilocal prolate operator, whose self-adjoint extension is fixed by a boundary condition at |x| = λ. N3 below gives this lead an exact finite-window home.

## 5. The near-null floor (t2064)
- **[Numerical]** The "1e−5 plateau" for A ≥ 1.5 is a mesh floor. It falls like about h^1.8, from 1.5e−4 to 1.0e−6 at A = 2 as n goes from 512 to 8192. At A ≤ 1.1 the minimum converges (A = 1: 0.01186; A = 1.1: 9.2e−4).
- **[Numerical]** The eigenvector is smooth, even and has two nodes. Grid overlaps are 0.998–0.9999. Its Fourier transform vanishes at γ₁…γ₈ to about 1e−6.
- **[Cited]** This is the Connes–Consani ζ-cycle phenomenon, a consequence of the explicit formula and not evidence for RH (see also atlas #374).

## 6. Conversation analogies recorded (no scratch file)
- **Rank/BSD (t2081–t2082).** Shioda–Tate (NS = trivial lattice ⊕ Mordell–Weil lattice, with the height as projected intersection) and Néron–Tate / Faltings–Hriljac as the template where a positive height on a Jacobian supplies the sign. [Analogy] N2 makes the finite-window part precise.
- **Telegrapher (t2085).** Recorded by title only, as an analogy next to the existing `telegrapher_distortionless` entry. Its details live in the conversation and are not reconstructed here. It supplies no sign mechanism. [Analogy]
- **Graded shadow H⁰ ⊕ H¹ ⊕ H² (t2091, as summarized).** Γ·Δ = 1 + μ − Tr(H¹): the pole part P is the H⁰ ⊕ H² shadow, and W is the H¹ part. [Analogy; exact over F_q]

## 7. New connections (night2105)

### N1. The determinant wall is the product formula
- **[Exact]** R1 forces dψ = μ, so each transversal fixed point carries |1 − μ|.
- At μ = p^k: p^k − 1 = #G_m(F_{p^k}) (affine) and p^k + 1 = #P¹(F_{p^k}) (compact). The Lefschetz eigenvalues are 1 and p^k only, with no weight-1 part.
- With the half-density these are 2sinh(u/2) = h_asym and 2cosh(u/2) = h_sym, the t2073 pair.
- Product formula: log(p^k − 1) = Σ_{ℓ | p^k−1} v_ℓ log ℓ with ℓ ≠ p, and |1 − p^k|_p = 1. Checked for p^k ≤ 10⁶, error 1.8e−15.
- The graph of ×p^k meets Δ over the primes ℓ, never over p. One statement explains three no-gos: the real chart, P¹_Z, and the p-adic determinant.
- A log p atom at p must be a vertical fibre degree, which is R3 restated. **Verdict: exact; no Φ.**

### N2. A finite-window Shioda–Tate split
- **[Exact, finite dimension]** With Triv = span{Q⁻¹r±}:
  - E0 is the I-orthogonal complement of Triv;
  - I|Triv = −S and I|E0 = −W;
  - **n₋(W|E0) = n₋(Q) − n₋(S)**.
- Hodge index for I, meaning exactly one positive direction, is n₋(Q) = 1: H_A has exactly one eigenvalue below M_A.
- **[Numerical]** For ζ, both counts equal 1 at A = 0.694 to 2.5. The identity holds in 84 runs.
- **[Numerical, mesh-dependent]** The lifts' Gram tends to J, like the fibres f₁, f₂: at A = 3, n = 1024, I(H₊,H₊) = 1.4e−5 and I(H₊,H₋) = 0.99999.
- **[Numerical control]** Scaling the prime weights by s ≠ 1 (not Euler data):
  - at A ≥ 1.5 only s = 1 is E0-positive at a resolution of 0.01;
  - failures add bound states while n₋(S) stays at 1;
  - deleting n = 2 at A ≤ 1.1 is absorbed by n₋(S) = 2.
- **Verdict:** the identity is exact; the diagnosis is numerical. The sign sits in the bound-state count, and the trivial lattice is rigid.

### N3. The pole plane is a boundary condition
- **[Exact]** For Q_Θ = Q + BΘBᵀ:
  - Θ = 0 gives Q; Θ = J gives W; Θ → ∞ gives W|E0.
  - Krein: det(Q_Θ − λ)/det(Q − λ) = det(I + ΘM(λ)), with M(λ) = Bᵀ(Q − λ)⁻¹B, which is Herglotz.
  - spec W|E0 = the zeros of det M.
  - When n₋(Q) = 1: E0-positivity ⇔ det M(0) < 0 ⇔ some Θ > 0 makes Q_Θ ≥ 0.
  - For Θ = cI the threshold is c* = 1/|λ_min M(0)|, and W ≥ 0 on the window forces c* ≤ 1.
- **[Numerical]** c* = 0.99997 (A = 1.1) and 0.99999 (A = 1.5, 2). M is singular at every W|E0 eigenvalue: relative σ_min is 1e−6 to 1e−15, against 0.02–1 at the midpoints.
- **Verdict:** an exact reformulation, not a sign source. It gives the prolate lead a checkable form: a zeros-free Θ_A in the cone det(Θ⁻¹ + M_A(0)) < 0.

### N4. Near-null = numerical equivalence; "genus ∞" on every window
- **[Exact, function field]** The Weil Toeplitz form on k = 0..K has rank min(K+1, 2g). Its kernel is the multiples of L̃(x) = ∏(x − β_i), by Cayley–Hamilton for Frobenius on H¹. Also G − P = −W_ff. Checked on genus 1 and 2, residual ≤ 1e−12.
- **[Exact, cited]** For ζ under RH, W(F) = Σ|F̂(γ)|². The zero ordinates have infinite density, so {e^{iγu}} is complete on every window (Beurling–Malliavin/Levinson) and W has no exact kernel. The near-null cluster is the shadow of genus ∞.
- **[Analogy]** Fréchet / L² corresponds to homological / numerical equivalence.
- **[Open] R5:** Φ must be numerically injective on every window. Finite-rank CH¹ (t2087) and finite Pic⁰(C_p) (t2098) fail R5.
- **Verdict:** exact over F_q; exact contrast for ζ; the rest is analogy.

## 8. Open problems (ordered by how directly they bear on Φ or a sign)
1. A space where Ψ(p^k) ∩ Δ has a vertical component over p of degree log p (N1 / R3).
2. A geometric reason that H_A has one bound state below M_A for every A (N2).
3. Connes–Consani's prolate boundary condition written as Θ_A, and whether it lies in the admissible cone (N3).
4. A zeros-free count for the effective genus 2g(A) of a window (N4).
5. Intersection theory on the Connes–Consani square, with Ψ(e^u)·Ψ(e^v) = τ(u − v) (t2068, t2087).

# Lemma 194 — positivity package (t2262/t2263, Grok Bot as checker, 17 Nov 2026)

Scratch, lem194/. **RH is not proved; Φ is not constructed; no sign is found.** Nothing touches TARGET.md or the atlas. Parts: (a) PROVED, (b) RESTATEMENT, (c) PROVED bound + CONJECTURE (sharp form refuted numerically), (d) EXACT on 𝔽_q side / ANALOGY across, (e) PROVED linear algebra (addendum). Does not touch TARGET (D).

## Lemma 194 (positivity package)

**Setting / conventions** (TARGET §1.1, hp2251, LEMMAS_2253). u = log x; window I_r = [−r/2, r/2]; F real, supported in I_r; F̂(t) = ∫F(u)e^{itu}du; g = F∗F̃ (F̃(u) = F(−u)).
Q(F) = K₀‖F‖² + ½∬(F(u)−F(v))²J(u−v)du dv (F extended by 0) − Σ_{n≥2} a_n [g(log n)+g(−log n)], a_n = Λ(n)n^{−1/2};
C±(F) = ∫F e^{±u/2}; P = 2C₊C₋; W = Q + P (= QW, CCM's form incl. pole terms); E₀ = ker C₊ ∩ ker C₋.
Explicit formula (checked numerically, §T0): W(F) = Σ_ρ F̂(t_ρ)F̂(−t_ρ), t_ρ = −i(ρ − ½), sum over nontrivial zeros of ζ (symmetric summation).
For an entire L-function L(s) = Σ b_n n^{−s} with real b_n and self-dual FE Λ(s) = (q/π)^{s/2}Γ((s+a)/2)L(s) = Λ(1−s): same Q with K₀ = ψ(¼ + a/2) + log(q/π), J(w) = Σ_{n≥0} e^{−(2n+½+a)|w|}, a_n = c(n)n^{−1/2} where −L′/L(s) = Σ c(n)n^{−s} (Re s ≫ 1), and no pole terms: Q(F) = Σ_ρ F̂(t_ρ)F̂(−t_ρ).

### (a) Translation covariance — PROVED (elementary)
Let (τ_a F)(u) = F(u − a). Then
1. g is unchanged (τ_aF ∗ (τ_aF)~ = F ∗ F̃), and Q depends on F only through g (the archimedean part is ½∬(F(u)−F(v))²J(u−v) + K₀∫F², both shift-invariant integrals over ℝ²/ℝ; the prime part is Σa_n(g(log n)+g(−log n))). Hence Q(τ_aF) = Q(F).
2. C±(τ_aF) = ∫F(u−a)e^{±u/2}du = e^{±a/2}C±(F). Hence τ_a maps E₀ (of I_r) onto E₀ (of I_r + a), and P(τ_aF) = 2e^{a/2}e^{−a/2}C₊C₋ = P(F), so W is shift-invariant too.
3. Consequences: (i) spectra of Q, W, Q|E₀, Q|ker C± on a window depend only on r; (ii) **monotonicity**: if r′ < r, L²(I_{r′}) ⊂ L²(I_r) (after a shift) and the form is the same, so n−(Q|I_{r′}) ≤ n−(Q|I_r) and min Q|I_r ≤ min Q|I_{r′} (same for W, Q|E₀); (iii) **Galerkin**: the sine basis spaces V_N ⊂ V_{N′} are nested in L²(I_r) and Rayleigh–Ritz values are upper bounds, so a Galerkin negative count is a lower bound for the true index, nondecreasing in N; a positive Galerkin minimum certifies nothing.
On the hyperbolic plane spanned by e^{±u/2} the flow acts by diag(e^{a/2}, e^{−a/2}) in the null basis — a boost; P is the boost-invariant Lorentzian form of signature (1,1). ∎

### (b) Weil's criterion on E₀ — RESTATEMENT (Weil 1952; Bombieri 2000, Yoshida 1992; TARGET §1.1; Lemma 189)
RH ⇔ for every r, Q ≥ 0 on E₀ ∩ L²(I_r) ⇔ (L189) for every r, Q ≥ 0 on ker C₊ ∩ L²(I_r). Equivalently W ≥ 0 on all of L²(I_r) for every r.
For an entire L as above (no poles, E₀ not needed): all zeros on the line ⇔ Q ≥ 0 on L²(I_r) for every r. (⇒: Q = Σ_γ|F̂(γ)|² ≥ 0. ⇐: Weil's argument — the zero distribution Σ_ρ δ_{t_ρ} is then a positive-definite distribution, so by Bochner–Schwartz a positive measure on ℝ, so every t_ρ is real.) Nothing new is proved here.

### (c) Index count — PROVED upper bound + CONJECTURE (diagnostic)
Group off-line zeros of a real self-dual L into quadruples {ρ, 1−ρ̄, ρ̄, 1−ρ}, ρ = ½ + δ + iγ, δ > 0, γ > 0; they give t ∈ {±γ ± iδ}.
**Proved (finite algebra on the spectral side).** Write a = F̂(γ − iδ), b = F̂(γ + iδ). For real F, F̂(−z̄) = conj F̂(z), and the quadruple contributes q_ρ(F) = 4 Re(a b̄) (real form, rank ≤ 4, signature ≤ (2,2)). On even real F, b = ā and q_ρ = 4 Re(a²) = 4(A² − B²), A = ∫F cos(γu)cosh(δu), B = ∫F sin(γu)sinh(δu): signature ≤ (1,1). On odd real F, b = −ā and q_ρ = −4 Re(a²): signature ≤ (1,1). The on-line part Σ_γ 2|F̂(γ)|² is ≥ 0. Hence, by subadditivity of the negative index, **if there are m off-line quadruples, n−(Q | parity sector of any window) ≤ m**, and with the pole plane n−(Q|E₀ ∩ sector) ≤ m, n−(Q|sector) ≤ m + [even sector]. In particular RH ⇒ n−(Q|E₀) = 0 and n−(Q) ≤ 1 on every window. (For DH, m = ∞, so no bound.)
**Size bound.** For normalized even F, |B|² ≤ ∫_{I_r} sin²(γu)sinh²(δu)du ≈ ½(sinh(δr)/(2δ) − r/2), so a single quadruple can push an even eigenvalue at most to ≈ −2(sinh(δr)/(2δ) − r/2) (less the on-line positive part).
**Conjecture 194c (diagnostic, not a theorem).** In each parity sector, n−(Q|I_r) equals the number of off-line quadruples "resolved" by I_r, where resolved means: the basis reaches frequency γ (N ≳ γr/π) and r exceeds a threshold r*(ρ) of order log(qγ/2π) (the window must be long enough for F̂, of exponential type r/2, to be small at the on-line zeros near height γ, whose density is (1/2π)log(qγ/2π)). For ζ the conjecture is equivalent to RH and predicts 0 at every r.

### (d) 𝔽_q dictionary — EXACT on the 𝔽_q side; ANALOGY (framing) across
| C/𝔽_q, surface X = C × C | ζ, CCM/Weil form |
|---|---|
| NS(X)_ℝ with intersection pairing (·) | test functions with −Q (Weil: W = −(intersection) up to normalization) |
| fibre classes f₁ = [pt×C], f₂ = [C×pt]: f₁² = f₂² = 0, f₁·f₂ = 1 (hyperbolic plane) | null functionals C₊, C₋ (e^{±u/2}); P = 2C₊C₋, signature (1,1) |
| ample h = f₁ + f₂, h² = 2 | cosh(u/2) = ½(e^{u/2}+e^{−u/2}): the P-positive direction, P(cosh)/‖cosh‖² = r + 2sinh(r/2) = λ_max(P) (exact, see (e)) |
| primitive part ⟨f₁,f₂⟩^⊥ | E₀ = ker C₊ ∩ ker C₋ |
| (id×Frob)^* acts on ⟨f₁,f₂⟩ by 1, q; normalized q^{∓½} | translation τ_{log q} scales C± by q^{±½} (part (a)) |
| Hodge index: (·) negative definite on primitive part of NS | Q ≥ 0 on E₀ (= RH, part (b)) |
| Castelnuovo–Severi applied to Δ, Γ_Frob ⇒ |#C(𝔽_q) − q − 1| ≤ 2g√q (Weil's RH) | Weil's criterion |
Status: the left column is a theorem (Weil; Grothendieck's proof of Hodge index for surfaces). In the right column, every row except the Hodge-index row is proved (parts (a), (e)); the Hodge-index row is RH. The dictionary supplies no mechanism (what replaces Riemann–Roch + ampleness on our side is exactly the missing index theorem, TARGET (D)).

### (e) Pole-plane linear algebra; index-1 vs Weil — PROVED (exact, finite-dimensional; addendum t2263 (ii), (v))
1. On L²(I_r): ‖e^{±u/2}‖² = 2sinh(r/2), ⟨e^{u/2}, e^{−u/2}⟩ = r. So P has exactly two nonzero eigenvalues r ± 2sinh(r/2), with eigenvectors cosh(u/2) (top, +) and sinh(u/2) (−). ∫cosh(u/2)e^{±u/2} = r/2 + sinh(r/2) = ‖cosh(u/2)‖² (exact). Hence λ_max(P) = r + 2sinh(r/2) = P(ĉ), ĉ = cosh/‖cosh‖.
2. **Sandwich.** Q = W − P ⇒ e₀(W) − (r + 2sinh(r/2)) ≤ λ₀(Q) ≤ W(ĉ) − (r + 2sinh(r/2)). So Claude's "λ₀ ≈ −(r + 2sinh(r/2))" is the statement that W is small on cosh; ε(r) := λ₀ + r + 2sinh(r/2) ∈ [e₀(W), W(ĉ)].
3. **Haynsworth.** For a nondegenerate symmetric Q and independent functionals L = (ℓ₁..ℓ_k): n−(Q|ker L) = n−(Q) − n−(LᵀQ^{−1}L).
4. Parity split: c := C₊|even = C₋|even (↔ cosh), s := C₊|odd = −C₋|odd (↔ sinh); W_e = Q_e + 2ccᵀ, W_o = Q_o − 2ssᵀ. Put G_e = cᵀQ_e^{−1}c, G_o = sᵀQ_o^{−1}s. Then det W_e = det Q_e·(1 + 2G_e), det W_o = det Q_o·(1 − 2G_o), and:
   - n−(W_e) = n−(Q_e) − [1 + 2G_e < 0]; n−(W_o) = n−(Q_o) + [1 − 2G_o < 0];
   - n−(Q|E₀) = n−(Q_e) − [G_e < 0] + n−(Q_o) − [G_o < 0];
   - n−(Q|ker C₊) = n−(Q) − [G_e + G_o < 0].
   So, when n−(Q) = 1 with even ground state ("index 1", λ₁ > 0): **W > 0 on the window ⇔ G_e < −½ and G_o < ½; Q > 0 on E₀ ⇔ G_e < 0; Q > 0 on ker C₊ ⇔ G_e + G_o < 0.**
5. **Answer to (v).** "Q ≥ 0 on h_r^⊥" (λ₁(Q) ≥ 0) is n−(Q) ≤ 1. It is *implied* by W ≥ 0 (n−(Q) = n−(W − P) ≤ n−(W) + 1, P having one positive eigenvalue), hence by RH, but it is **not equivalent** to Weil positivity on E₀ or on ker C₊ on a given window: those need in addition the sign conditions on G_e (and G_o). Concretely, if a resolved off-line quadruple gives W_e one negative direction while 1 + 2G_e > 0, then n−(Q_e) = 1 still and λ₁(Q) > 0: the index-1 test is blind to it. Conversely Q|E₀ > 0 is compatible with n−(Q) = 2 (n−(Q_e) = 1, G_e < 0, n−(Q_o) = 1, G_o < 0). E₀ meets the negative cone of an index-1 Q exactly when G_e > 0 (codim-2 version: when n−(LᵀQ^{−1}L) = 0). Over all windows: RH ⇒ index 1 on every window; the converse is not implied by this algebra.
6′. **The Hodge-index analogue relative to the ample direction cosh(u/2) *is* equivalent to RH; relative to h_r it is not.** cosh(u/2)^⊥ = (even ∩ ker c) ⊕ odd. n−(Q|cosh^⊥) = n−(Q_e) − [G_e < 0] + n−(Q_o). On each window W ≥ 0 ⇒ Q ≥ 0 on cosh^⊥ (Q_e = W_e on ker c; Q_o = W_o + 2ssᵀ ≥ W_o) ⇒ Q ≥ 0 on E₀ ⊂ cosh^⊥. Hence, over all windows, **RH ⇔ Q ≥ 0 on cosh(u/2)^⊥ for every r** (⇐ by (b)). "Q ≥ 0 on h_r^⊥ for every r" is only implied by RH. So in the 𝔽_q dictionary the Kähler class must be read as cosh (= f₁ + f₂, P's positive direction), not as Q's Perron vector h_r; the two are close numerically (T3) but play different logical roles.
7. **Perron property of Q (for ζ, every r).** The off-diagonal kernel of Q is −J(u−v) − Σ a_n δ(|u−v| − log n) ≤ 0 with a_n = Λ(n)/√n ≥ 0 and J > 0, so Q is a Beurling–Deny form plus a potential bounded below on every window; as in Lemma 188 its lowest eigenvalue is simple with a strictly positive even eigenfunction h_r, for **every** r (not only r ≤ log P, which is the threshold for W because P adds the positive kernel 2cosh((u−v)/2)). Consequently Q(h_r, f) = λ₀⟨h_r, f⟩ < 0 for every f ≥ 0, f ≠ 0 ("ample" in Claude's sense) — trivially. This uses only Λ(n) ≥ 0; it fails for DH (c(n) of both signs), and holds for χ₄ only for r ≤ log 3 (Lemma 193).

---

## Numerical tests (scratch; all times America/Chicago, 17 Nov 2026)

**Setup.** Sine basis φ_n = √(2/r) sin(nπ(u+r/2)/r), n = 1..N on [−r/2, r/2]. The assembly is `build.py`, which is lem2253/build.py (= hp2251/sine.py) plus a generic option (α, q, c(n)) for DH. The driver is `t194.py`. All restrictions are explicit: E₀ via a Householder complement in each parity block, ker C₊ via the exact secular equation, and the Haynsworth counts from G_e and G_o. mpmath with the gmpy2 backend (in a venv). **Galerkin caveat:** Rayleigh–Ritz eigenvalues are upper bounds. A positive Galerkin minimum certifies nothing. A Galerkin negative count is a lower bound for the true index, and it is nondecreasing in N and in r (part (a)).

**Precision.** Every precision duplicate (2× dps for ζ/χ₄; 1.6–2× for DH) agreed in every printed digit: ζ r = 0.25–10, χ₄ r = 4, DH r = 3, 3.5, 4, 5, 6. Small eigenvalues of ζ are not converged in N for r ≥ 2: they fall by many orders per +50 in N, as in hp2251.

### T0. Explicit-formula cross-checks (arithmetic side vs zeros)
- **ζ** (r = 1, N = 8, 341 zeros up to T = 600 plus a smooth tail): the Galerkin matrix of W built from zeros, W = Σ_ρ F̂(t_ρ)F̂(−t_ρ), matches the arithmetic QW to **8.7·10⁻⁸** with the tail (6·10⁻⁶ without it). Largest entry 1.46. `out/spec_zeta_r1.json`.
- **DH explicit formula.** The form uses c(n), where −f′/f = Σ c(n)n^{−s}. These are not von Mangoldt values; c(n) ≠ 0 for many non-prime-powers, and |c(n)|/√n ≤ 0.79 for n ≤ 3000. Justification: shift the contour on Re s = c ≫ 1, term by term. Each term is entire, and only n ≤ e^r survive because g has compact support.
  - Γ-factor confirmed numerically: Λ(s) = (5/π)^{s/2}Γ((s+1)/2)f(s) = Λ(1−s) to 1e−30. The even Γ(s/2) fails.
  - Σ c(n)n^{−3} reproduces −f′/f(3).
  - Zeros up to T = 400: 287 sign changes on the line, plus **8 off-line zeros with Re > ½**, found where Backlund's N(T) exceeds the sign-change count and confirmed by box winding numbers: 0.808517+85.699348i, 0.650830+114.163343i, 0.574356+166.479306i, 0.724258+176.702461i, 0.869531+240.404672i, 0.819550+320.876490i, 0.768223+331.050259i, 0.628508+366.640908i. These match the literature values in the brief (`out/zeros_dh_400.json`).
  - **Rayleigh check on the large negative DH directions**, arithmetic eigenvalue vs zero-side sum:

| r, N | vector | arithmetic | zero side total | on-line part | off-line part | tail |
|---|---|---|---|---|---|---|
| 4.5, 220 | even #0 | −1.316958115 | −1.316958074 | +0.0576 | **−1.3746** | 1.6e−5 |
| 4.5, 220 | odd #0 | −1.336475826 | −1.336475473 | +0.0612 | **−1.3977** | 7.7e−5 |
| 6, 216 | even #0 | −3.657416962 | −3.657417887 | +0.1564 | **−3.8139** | 9.0e−5 |
| 6, 216 | odd #0 | −3.602503144 | −3.602502729 | +0.1417 | **−3.7442** | 2.3e−5 |

  So the DH negativity is caused by the off-line zeros, and the DH build is validated. The size bound in (c) for the first quadruple at r = 6 is −2(sinh(δr)/(2δ) − r/2) ≈ −4.1; observed −3.66.
- **Not completed:** full-matrix zero-side checks at N = 30, and spec2 vectors #1/#5/#20. Their tail quadratures were too slow (> 80 min) and were killed. Labelled not done.

### T1. ζ: Q on E₀. Expected index 0. **Result: index 0 at every r and N.**
| r | N | dps | λ₀(Q) | λ₁(Q) = min Q on h_r^⊥ | min Q on E₀ | min Q on cosh^⊥ | min Q on ker C₊ | e₀(W) | n−(Q) | n−(Q\|E₀) (direct = Haynsworth) | n−(W) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 200 | 60 | -0.160536 | 1.1094e+00 | 1.5707e+00 | 1.1094e+00 | 1.1079e+00 | 3.1838e-01 | 1 | 0 = 0 | 0 |
| 0.5 | 200 | 60 | -0.912534 | 4.1510e-01 | 8.7658e-01 | 4.1510e-01 | 4.0873e-01 | 3.3718e-02 | 1 | 0 = 0 | 0 |
| 1 | 100 | 60 | -1.980368 | 1.2763e-02 | 1.2719e-02 | 1.2719e-02 | 2.0778e-04 | 1.0055e-06 | 1 | 0 = 0 | 0 |
| 1 | 100 | 120 | -1.980368 | 1.2763e-02 | 1.2719e-02 | 1.2719e-02 | 2.0778e-04 | 1.0055e-06 | 1 | 0 = 0 | 0 |
| 1 | 200 | 60 | -1.983891 | 1.2343e-02 | 1.2302e-02 | 1.2302e-02 | 1.9983e-04 | 9.7314e-07 | 1 | 0 = 0 | 0 |
| 2 | 100 | 80 | -4.285486 | 1.8036e-23 | 1.8036e-23 | 1.8036e-23 | 1.8400e-26 | 7.6622e-30 | 1 | 0 = 0 | 0 |
| 2 | 200 | 80 | -4.295908 | 1.4981e-23 | 1.4981e-23 | 1.4981e-23 | 1.5884e-26 | 6.5335e-30 | 1 | 0 = 0 | 0 |
| 3 | 100 | 160 | -7.192448 | 9.6919e-69 | 9.6919e-69 | 9.6919e-69 | 2.1276e-72 | 1.2395e-75 | 1 | 0 = 0 | 0 |
| 3 | 100 | 320 | -7.192448 | 9.6919e-69 | 9.6919e-69 | 9.6919e-69 | 2.1276e-72 | 1.2395e-75 | 1 | 0 = 0 | 0 |
| 3 | 200 | 160 | -7.211459 | 1.9589e-87 | 1.9589e-87 | 1.9589e-87 | 2.3239e-91 | 2.2000e-95 | 1 | 0 = 0 | 0 |
| 4 | 100 | 250 | -11.156033 | 8.2416e-99 | 8.2416e-99 | 8.2416e-99 | 1.4528e-102 | 8.2416e-106 | 1 | 0 = 0 | 0 |
| 4 | 100 | 500 | -11.156033 | 8.2416e-99 | 8.2416e-99 | 8.2416e-99 | 1.4528e-102 | 8.2416e-106 | 1 | 0 = 0 | 0 |
| 4 | 200 | 250 | -11.194247 | 3.3944e-154 | 3.3944e-154 | 3.3944e-154 | 2.1665e-158 | 6.2886e-162 | 1 | 0 = 0 | 0 |
| 5 | 100 | 300 | -16.935416 | 9.2563e-120 | 9.2563e-120 | 9.2563e-120 | 8.5050e-124 | 9.7606e-127 | 1 | 0 = 0 | 0 |
| 5 | 100 | 600 | -16.935416 | 9.2563e-120 | 9.2563e-120 | 9.2563e-120 | 8.5050e-124 | 9.7606e-127 | 1 | 0 = 0 | 0 |
| 5 | 200 | 300 | -17.002554 | 2.3193e-199 | 2.3193e-199 | 2.3193e-199 | 6.7537e-204 | 5.5459e-207 | 1 | 0 = 0 | 0 |
| 6 | 100 | 350 | -25.738978 | 1.5305e-136 | 1.5305e-136 | 1.5305e-136 | 8.6643e-141 | 1.9777e-143 | 1 | 0 = 0 | 0 |
| 6 | 100 | 700 | -25.738978 | 1.5305e-136 | 1.5305e-136 | 1.5305e-136 | 8.6643e-141 | 1.9777e-143 | 1 | 0 = 0 | 0 |
| 6 | 200 | 350 | -25.870182 | 4.0918e-234 | 4.0918e-234 | 4.0918e-234 | 1.0559e-238 | 6.8646e-242 | 1 | 0 = 0 | 0 |
| 7 | 100 | 420 | -39.554266 | 1.9780e-150 | 1.9780e-150 | 1.9780e-150 | 8.1072e-155 | 1.3245e-157 | 1 | 0 = 0 | 0 |
| 7 | 100 | 840 | -39.554266 | 1.9780e-150 | 1.9780e-150 | 1.9780e-150 | 8.1072e-155 | 1.3245e-157 | 1 | 0 = 0 | 0 |
| 7 | 150 | 420 | -39.717043 | 9.6264e-209 | 9.6264e-209 | 9.6264e-209 | 1.8075e-213 | 3.0686e-216 | 1 | 0 = 0 | 0 |
| 8 | 100 | 500 | -61.631888 | 1.7564e-162 | 1.7564e-162 | 1.7564e-162 | 4.0862e-167 | 9.4123e-170 | 1 | 0 = 0 | 0 |
| 8 | 200 | 500 | -62.097513 | 6.3112e-287 | 6.3112e-287 | 6.3112e-287 | 9.3943e-292 | 8.8145e-295 | 1 | 0 = 0 | 0 |
| 10 | 100 | 650 | -155.320942 | 9.7820e-182 | 9.7820e-182 | 9.7820e-182 | 9.8317e-187 | 3.0676e-189 | 1 | 0 = 0 | 0 |
| 10 | 100 | 1000 | -155.320942 | 9.7820e-182 | 9.7820e-182 | 9.7820e-182 | 9.8317e-187 | 3.0676e-189 | 1 | 0 = 0 | 0 |
| 10 | 150 | 650 | -156.329954 | 1.2033e-256 | 1.2033e-256 | 1.2033e-256 | 1.7364e-261 | 1.6551e-264 | 1 | 0 = 0 | 0 |

- In every run, n−(Q) = 1 (even), n−(Q|E₀) = 0, n−(W) = 0, and G_e < −½, G_o < ½ (−0.5/+0.5 to 8 digits for r ≥ 2).
- For r ≥ 1, λ₁(Q) = min Q|E₀ = min Q|cosh^⊥ in all printed digits: the second eigenvector is already in E₀ (TARGET §1.3).
- min Q|ker C₊ sits 10³–10⁵ below them, near o₀(W) (Lemma 189).
- The minima are **not converged in N** for r ≥ 2. They are upper bounds, so this is no certificate of positivity.
- Full N = 50/150 rows: TABLES_194.md.

### Control: L(χ₄)
- No negative Galerkin eigenvalue at r = 1–8 and 10 (N = 100/150).
- The ground state is even and nodeless.
- λ₀ falls to 4.7e−81 (r = 5), 1.5e−126 (r = 8) and 6.0e−147 (r = 10).
- The 2×dps duplicate at r = 4 is identical.
- **Verdict:** behaves like ζ on E₀, κ = 0.

### T2. Davenport–Heilbronn: index vs window. **Result: index 0 up to r = 3.25, then negatives appear and multiply.**
Full table: DH_TABLE.md. Frequency ≈ π·(sign changes)/r is accurate to about π/r. "Reach" means Nπ/r.

| r | best N (reach) | n−(Q) e/o | negative eigenvalues with \|λ\| > 10⁻³ (frequency) | tiny negatives |
|---|---|---|---|---|
| 1, 2, 2.5 | 100 | 0/0 | — | — |
| 3 | 168 (176) | 0/0 | — | — (dps 160 = 320) |
| 3.25 | 182 (176) | 0/0 | — | — |
| 3.5 | 196 (176) | 1/1 | — | −2.1e−23 e, −7.0e−21 o at low frequency (dps 200 = 400; N-stable) |
| 3.75 | 210 (176) | 1/1 | −0.169 e @83.8, −0.097 o @84.6 | — |
| 4 | 224 (176) | 2/2 | −0.68 e @84.8, −0.76 o @84.0 | −3.9e−17 e, −1.6e−18 o |
| 4.5 | 252 (176) | 4/4 | −1.32 e @85.2, −0.27 e @114.5; −1.34 o @84.5, −0.27 o @113.8 | 2 e, 2 o |
| 5 | 280 (176) | 4/4 | 85: −1.85 e/−1.87 o; 114: −0.38/−0.38; 166: −0.083 e @164.6, −0.087 o @166.5 | 1 e, 1 o |
| 5.5 | 308 (176) | 5/4 | 85, 114, 165 in both parities; −0.0113 o @168.5 | … |
| 6 | 336 (176) | 5/4 | 85: −3.68 e/−3.63 o; 113: −0.74/−0.74; 165–167: −0.147/−0.147; −0.132 o @174.4 | … |
| 7 | 252 (113) | 2/2 | 85: −6.15 e/−6.31 o | 2 |
| 8 | 288 (113) | 3/5 | 85: −10.6 e/−10.6 o; −0.036 e @110.7 | 4 |

- **Onset of O(10⁻¹) negatives, one per parity, at each off-line ordinate:**
  - 85.70: r ∈ (3.5, 3.75]
  - 114.16: r ∈ (4, 4.5], once N > γr/π (r = 4.5 with N = 162, reach 113, misses it; N = 220 finds it)
  - 166.48: r ∈ (4.5, 5]
  - 176.70: odd sector at r ∈ (5, 5.5]; even sector not seen by r = 6
- For comparison, the heuristic r* ≈ log(5γ/2π) gives 4.22, 4.51, 4.89, 4.95. It is the right order, but the first onset comes about 0.5 earlier.
- **Verdict T2:** as expected, the index is 0 at small r and becomes ≥ 1 once the window resolves the 85.7 zero. In fact it becomes ≥ 1 in each parity sector, because a quadruple has signature (1,1) per parity. The negative eigenvectors oscillate at the off-line ordinates, and the zero-side check attributes the negativity to the off-line terms.
- **Conjecture 194c in its sharp form ("index = number of resolved quadruples") is refuted.** There are extra precision-stable tiny negatives (10⁻¹⁴ to 10⁻²³⁸) at r = 3.5 and later. At r = 8, N = 288, the odd index is 5 while only two quadruples lie within the basis reach.
  - What survives: the proved bound n− ≤ m per parity (vacuous for DH, m = ∞), and an empirical rule. **Negatives with |λ| > 10⁻³ correspond one-to-one, per parity, to off-line quadruples that are within reach and past their onset r\*.**
  - Tiny negatives with |λ| < 10⁻¹⁴ whose dps duplicate was not run (N = 252/280/300/308/336 and r = 8) are labelled unverified for precision. All the O(10⁻¹) ones are far above any rounding level.
- The formal C± restrictions for DH (E₀, ker C₊) are all negative and carry no information, since DH has no pole plane.

### T3 + addendum (t2263): h_r, the Perron vector of W, and cosh(u/2)
Notation:
- h_r = ground state of Q (Claude's object), taken positive.
- p_r = ground state of W = Q + P (the Perron vector of Lemma 188 for r ≤ log P).
- "true" correlation = ⟨h, cosh⟩/(‖h‖‖cosh‖_{L²(I_r)}), which is exact.
- "in-span" correlation = the same quantity using only the Galerkin projection of cosh (cosh capture 0.98–0.998).
| r | N | corr(h,cosh) true / in-span | ‖h_{E₀}‖ | sign changes of h | corr(p,cosh) | ‖p_{E₀}‖ | corr(p,h) | ε_N = λ₀+r+2sinh(r/2) | W(ĉ_N) |
|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 200 | 0.98301 / 0.98401 | 0.1836 | 0 | 0.9715 | 0.2370 | 0.9983 | 0.3401 | 0.4100 |
| 0.5 | 200 | 0.98353 / 0.98453 | 0.1808 | 0 | 0.9451 | 0.3268 | 0.9875 | 0.0927 | 0.1612 |
| 1 | 200 | 0.99398 / 0.99503 | 0.1095 | 0 | 0.7879 | 0.6158 | 0.8062 | 0.0583 | 0.0901 |
| 2 | 200 | 0.99745 / 0.99863 | 0.0714 | 0 | 0.5812 | 0.8138 | 0.5871 | 0.0545 | 0.0615 |
| 3 | 200 | 0.99816 / 0.99956 | 0.0607 | 0 | 0.4593 | 0.8883 | 0.4614 | 0.0471 | 0.0355 |
| 4 | 200 | 0.99806 / 0.99977 | 0.0623 | 0 | 0.3751 | 0.9270 | 0.3764 | 0.0595 | 0.0278 |
| 5 | 200 | 0.99772 / 0.99983 | 0.0676 | 0 | 0.3110 | 0.9504 | 0.3121 | 0.0979 | 0.0332 |
| 6 | 200 | 0.99731 / 0.99989 | 0.0733 | 0 | 0.2584 | 0.9660 | 0.2594 | 0.1656 | 0.0378 |
| 7 | 150 | 0.99579 / 0.99994 | 0.0917 | 0 | 0.2196 | 0.9756 | 0.2207 | 0.3682 | 0.0414 |
| 8 | 200 | 0.99631 / 0.99998 | 0.0858 | 0 | 0.1761 | 0.9844 | 0.1768 | 0.4823 | 0.0258 |
| 10 | 150 | 0.99356 / 0.99999 | 0.1133 | 0 | 0.1223 | 0.9925 | 0.1231 | 2.0765 | 0.0472 |
### Addendum (t2263): Claude's h_r table vs ours (zeta; Galerkin values are upper bounds for λ0)

| r | Claude λ0 / ε / corr | ours λ0 at N=100,150,200 | extrapolated λ0 (fit N^-p) | p | −(r+2sinh(r/2)) | ε_N (N=200) | W(ĉ_N) (upper bd for ε, N=200) | corr(h,cosh) in-span / true (N=200) | ‖h_E0‖ (N=200) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | -1.9875 / 0.055 / 0.9953 | -1.980368, -1.982729, -1.983891 | -1.98720 | 1.05 | -2.04219 | 0.058299308 | 0.090098637 | 0.9950330568 / 0.9939821545 | 0.10954212 |
| 2 | -4.306 / 0.044 / 0.9987 | -4.285486, -4.292914, -4.295908 | -4.30101 | 1.61 | -4.35040 | 0.054494145 | 0.061480125 | 0.9986331872 / 0.9974495461 | 0.071375087 |
| 3 | -7.231 / 0.028 / 0.9996 | -7.192448, -7.204438, -7.211459 | -7.25235 | 0.55 | -7.25856 | 0.047099586 | 0.035454714 | 0.9995614799 / 0.998157252 | 0.060680312 |
| 4 | -11.231 / 0.023 / 0.9998 | -11.156033, -11.180859, -11.194247 | -11.24703 | 0.79 | -11.25372 | 0.059474034 | 0.027756083 | 0.9997749507 / 0.9980588612 | 0.06227768 |
| 5 | — / — / — | -16.935416, -16.980939, -17.002554 | -17.05790 | 1.15 | -17.10041 | 0.097854937 | 0.033175845 | 0.9998303169 / 0.9977155117 | 0.067555589 |
| 6 | — / — / — | -25.738978, -25.826202, -25.870182 | -26.00583 | 0.98 | -26.03575 | 0.16556748 | 0.037753497 | 0.9998942606 / 0.9973069808 | 0.073340208 |

**Addendum items:**
- **(i) Claude's table.**
  - Our N = 100/150/200 λ₀ are Galerkin upper bounds still falling with N. Crude N^{−p} extrapolations: −1.9872, −4.3010, −7.2524, −11.2470.
  - Claude's −1.9875, −4.306, −7.231, −11.231 lie between our N = 200 values and those extrapolations. **They are consistent but not confirmed to the stated digits.**
  - Claude's correlations 0.9953/0.9987/0.9996/0.9998 match our **in-span** correlations (0.99503/0.99863/0.99956/0.99977). The true L² correlations are lower (0.99398/0.99745/0.99816/0.99806 at N = 200) and still rising with N.
  - The ε values (0.055/0.044/0.028/0.023) are consistent with our bounds ε ∈ [e₀(W), W(ĉ)]: e₀(W) ≈ 0, and W(ĉ_N) = 0.090/0.061/0.035/0.028.
- **(ii) Exact.** ∫cosh(u/2)e^{±u/2} = r/2 + sinh(r/2) = ‖cosh(u/2)‖², checked by quadrature to 15 digits in every run. Therefore P(ĉ) = r + 2sinh(r/2) = λ_max(P) and λ₀ ≥ e₀(W) − λ_max(P).
  - Claude's "−2‖h‖² = −(r+2sinh(r/2))" is −λ_max(P), and the near-equality λ₀ ≈ −λ_max(P) only says that W is small on cosh.
  - This follows from (e)2. It is a consequence of W ≈ 0 on smooth low modes, not evidence of an index mechanism.
- **(iii) E₀ component of h_r.** 0.110 (r = 1), 0.071 (2), 0.061 (3), 0.062 (4), 0.068 (5), 0.073 (6) at N = 200. It is decreasing in N and not converged. The in-span values suggest a limit of about 0.01–0.03 for r ≥ 3.
- **(iv) "Ample".** Q(h,f) < 0 for all 5 random nonnegative f in every ζ run with N ≤ 100 (0 violations). This is trivial, because Q(h,f) = λ₀⟨h,f⟩, h > 0 and λ₀ < 0.
  - h_r has 0 sign changes in every run, r = 0.25–10.
  - Positivity of h_r for every r is **proved** by (e)7, the Markov property of Q, which uses Λ(n) ≥ 0. The window restriction r ≤ log P applies to W, not to Q.
  - λ₀ < 0 is observed at every r tested (it equals −0.16 at r = 0.25 and −156 at r = 10) but is **not proved** for all r. The upper bound λ₀ ≤ W(ĉ) − λ_max(P) needs a bound on W(cosh).
  - "Effective cone = nonnegative functions" is Claude's definition. The proved property is just Perron–Frobenius.
- **(v) Equivalence.** **"λ₁ ≥ 0 (Q ≥ 0 on h_r^⊥)" is NOT equivalent to Weil positivity.** See (e)3–6′.
  - On each window: W ≥ 0 ⇒ Q ≥ 0 on cosh^⊥ ⇒ Q ≥ 0 on E₀. Also, W ≥ 0 ⇒ n−(Q) ≤ 1 (λ₁ ≥ 0).
  - Index 1 misses the G-conditions (G_e < 0 for E₀; G_e < −½ and G_o < ½ for W).
  - Over all windows, **RH ⇔ Q ≥ 0 on cosh(u/2)^⊥ ∀r** (an equivalence), while **RH ⇒ λ₁(Q_r) ≥ 0 ∀r** is only one-way.
  - Numerically for ζ, all four minima are positive (Galerkin) and, for r ≥ 1, λ₁ = min E₀ = min cosh^⊥, so the distinction is invisible in the data. It is a logical distinction, not a numerical one.
  - For DH, λ₁ < 0 from r = 3.5 on, because negatives arrive in both parities at once. The index-1 test therefore happens to detect DH, but it would miss a single negative direction.

**Verdict T3.**
- *Claude's h_r (the Perron vector of Q) tracks cosh(u/2):* L² correlation ≥ 0.993 for r = 1–10 at N = 150–200 (limited by N: it is not monotone in r at fixed N), and the in-span correlation rises toward 1 (0.99999 at r = 10). It is by definition Q's negative direction.
  - The reason is the sandwich Q = W − P with W ≪ P on smooth modes, so h_r is ≈ the top eigenvector of P, which is cosh exactly.
  - So "Kähler class = h_r ≈ cosh" is numerically right, and the parent's earlier claim that "the Perron mode is not cosh" was about a different vector, p_r (the Perron vector of W).
  - Where the claim goes wrong is logic: "Hodge index relative to h_r is RH" is false as an equivalence. The correct ample direction is cosh itself, and relative to cosh the Hodge-index statement is RH.
- *The Perron vector of W (Lemma 188's object) does NOT track cosh:* corr(p,cosh) = 0.97 (r = 0.25), 0.94 (0.5), 0.79 (1), 0.58 (2), 0.46 (3), 0.38 (4), 0.31 (5), 0.26 (6), 0.18 (8), 0.12 (10). These are N-stable, with ‖p_{E₀}‖ rising to 0.99. Nor does it track Q's negative direction: corr(p,h) has the same decay. Under the |Q| inner product, p and h look close (0.99+) only because |Q| gives near-zero weight to the near-null directions where p lives, so that metric is not informative.

### Errors / corrections to prior work found
1. **Parent's t2261 review:** "The Perron mode is not cosh(u/2) … the sign roles don't match" is correct for p_r (W's ground state, Lemma 188) but does not apply to Claude's h_r (Q's ground state).
   - Q is Markov on every window, so h_r is a Perron vector for all r; it is Q's negative direction, and it is ≈ cosh.
   - The parent's conclusion still holds in substance: it is not a mechanism, and "Hodge index rel. h_r ⇔ RH" is false.
2. **Claude t2263:**
   - Item 4, "Hodge index relative to h_r ⇔ λ₁ ≥ 0 … RH is the statement for every r," is one-way only. The equivalence needs cosh^⊥ (or E₀), not h_r^⊥.
   - The table's correlations are in-span values, not L² values, and its λ₀ are not reproduced to the stated digits.
   - "Simple, positive for every r" is correct (it is the Markov property of Q, not Half 1/Lemma 188, which concerns W).
3. **Lemma 189/Table Z column "cos(Q-ground, cosh)" (lem2253)** is the in-span overlap |⟨u,c⟩|/|c|. It should be labelled as such; the true L² overlap is lower by about 10⁻³ at N = 100–200.
4. **Conjecture 194c (sharp index count)** is refuted by the DH data, as stated in T2.

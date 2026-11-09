# atlas2060: SYNTHESIS for RH Atlas v1.21 (work since v1.20)

Prepared 8 Nov 2026, about 9:50 PM CST (America/Chicago). This file brings together scratch work done after the v1.20 release (v1.20 was published 7 Nov 2026, 11:19 PM CST). It also includes the conclusions of the follow-up discussion on the boundary model and the class map. It is written for an independent reader. **AUDIT.md overrides any statement here or in `notes/`.**

> **The Riemann Hypothesis is not proved.** Nothing here proves it. Nothing here proves positivity of the Weil form W for all windows.
> W ≥ c‖F‖² on E0 is established only for windows of width A ≤ 1.1. It is analytic for A ≤ 1/10, interval-certified for A ≤ 0.694, and computer-assisted for A ≤ 1 and A ≤ 1.1.
> Every statement for A > 1.1 is numerical. Grid bias at that scale is about the same size as the gap.

## Status tags

| Tag | Meaning |
|---|---|
| **[Exact]** | An identity or theorem proved by hand algebra and/or symbolic or high-precision checks. Literature results are marked **[Cited]**. |
| **[Certificate]** | A computer-assisted bound. It uses mpmath interval arithmetic for scalar data. Finite matrices use floating point with a stated IEEE-754 binary64 rounding model: dot-product error γ_n = nu/(1−nu), u = 2⁻⁵³, plus explicit residual and orthogonality bounds. **This is not a formally verified proof.** |
| **[Numerical]** | A double- or high-precision computation without an error certificate. |
| **[Obstruction]** | A proved no-go for a stated route, in the stated scope only. |
| **[Analogy]** | A structural or physics reading. It has no arithmetic map. |
| **[Open]** | Missing. |

Notation:
- I_A = [−A/2, A/2] is the window. Tests F are supported there.
- C± = ∫F e^{±u/2} are the two moments. E0 = ker C₊ ∩ ker C₋.
- W = P + H_A − M_A‖F‖², with P = 2Re C₊C̄₋.
- a_n = Λ(n)/√n, and M_A = −K₀ + 2Σ_{log n<A} a_n.
- K₀ = ψ(1/4) − log π = −γ − π/2 − 3 log 2 − log π = −5.372183.
- k∞(a) = e^{−a/2}/(1−e^{−2a}) is the archimedean (Gamma) jump kernel.

---

## 1. Ledger and operator

1.1 **[Exact]** *Signed self-adjoint window operator* (operator2023). K_A = L_A − M_A + P_A is the operator of the closed semibounded form W on L²(I_A). L_A is the Gamma and prime jump operator, M_A is the constant mass, and P_A is the rank-2 pole part. The Gamma symbol grows like log|t|, so the form domain is a log-Sobolev space.
- H_A ≥ 0 is "kinetic". M_A is a constant "potential" threshold.
- Missing: ‖J_A F‖² ≥ M_A‖F‖² on E0 with no zeros used. **[Open]**

1.2 **[Exact]** *Pole-cancelled identity* (sos2010, realization2033).
- W = K₅‖F‖² + J₅ − 2∫x^{−1/2}⟨F, T_{log x}F⟩ dE(x), where E = ψ_Cheb − x and K₅(0) = K₀ + 4.
- The unconstrained form has residual mass M̃_A = M_A − 4e^{A/2}. Its values are −0.2424 (A=1), 0.3515 (A=2) and 0.4611 (A=3). **[Numerical]**
- "Lemma A" of sos2010 is only a Ritz value. **[Correction]**

1.3 **[Exact]** *Moment parametrization* (parabola2019, poincare2024).
- 𝒟 = ∂² − 1/4 is a bijection from H²₀(I_A) onto the L² tests in E0. Every E0 test is 𝒟G for a unique G supported in the window.
- In the unitary chart r = e^{−u}, 𝒟 becomes ∂_r(r²∂_r). The constant 1/4 is the Hardy constant and also the bottom of the continuous spectrum at the cusp.

1.4 **[Exact]** *M_A as a regularized prime sum* (eisenstein1990, counterterm1995).
- M_A = 2(S_A − S_reg), where S_reg = −ζ′/ζ(½) = K₀/2.
- −K₀ = γ + log 8π + π/2. The finite-part integral is FP∫k∞ = π/2 + 2 log 2.
- Under Connes' semilocal trace (Connes 1999, Thm VII.4) **[Cited]**, M_A is the total α-normalized degree mass in degree form.
- K₀ is fixed by the adelic character class (α = e^{−2πix}, self-dual measure).
- The "RG family" reading in matching1989 is corrected: there is no free renormalization parameter. **[Correction]**

1.5 **[Numerical, diagnostic only]** The explicit-formula table with 400 zeros (eisenstein1990) uses zeros. It is a diagnostic and cannot be part of any positivity argument (atlas: `tautology_boundary`).

## 2. Positivity certificates on small windows (the honest frontier)

2.1 **[Exact]** *No-prime windows* (poincare2024). For A ≤ 1/10, W ≥ c*‖F‖² on E0 with c* = log(5√2/π) − γ − 3/80 ≈ 0.19657 > 7/240.
- Moment-blind chain bounds fail early. At A = 1 the bound gives 3.7528 against the 6.3524 needed. **[Numerical]**

2.2 **[Certificate, interval]** *One prime, n = 2* (logpoincare2044). For A ≤ 347/500 (0.694), W ≥ 0.0045‖F‖² on E0.
- Proof route: a constrained log-Jensen lemma. The numbers are certified with mpmath.iv (combined margin ≈ 0.005275; k_low > 9.0258; K(9) > 0.358; θ = 3/16).
- The bound fails to close at 0.695. That is inconclusive. It is not a counterexample.

2.3 **[Certificate, IEEE model]** *A ≤ 1, prime n = 2* (multiprime2047).
- Setup: N = 48 Gamma terms, κ = 2, 815 cells.
- Finite compressed eigenvalue > 0.0069963; high-block lower h* > 2.2304; cross bound B* < 0.07587; Schur margin > 0.000314.
- Conclusion: **W ≥ (1/250)‖F‖² on E0.**
- Rerun time 5.9 s (archived run 5.2 s).

2.4 **[Certificate, IEEE model]** *A ≤ 1.1, primes n = 2, 3* (multiprime2047).
- Setup: N = 192, κ = 4, 1838 cells.
- Verified effective eigenvalue > 0.00066384; h* > 3.20786; derivative and moment Schur coefficients 1/40000000 and 1/4000000.
- Conclusion: **W ≥ 0.0005‖F‖² on E0.** Rerun time about 89 s.

2.5 **[Numerical]** Beyond 1.1 (inertia2057), the constrained E0 minima are:

| A | 0.5 | 0.694 | 1 | 1.1 | 1.5 | 2 | 2.5 | 3 |
|---|---|---|---|---|---|---|---|---|
| min W/‖F‖² on E0 | 0.8749 | 0.5455 | 0.011872 | 0.00093187 | 1.72e−5 | 1.278e−5 | 1.30e−5 | 1.2786e−5 |

- These are upper estimates only.
- The 128-cell and 2048-cell values differ by about 100× beyond A ≈ 1.1. **There is no all-window statement.**

2.6 **[Numerical]** *Ghost control* (polarity2021, multiprime2047, sos2010). The test is G = (1−u²)⁴ on [−1, 1] (A = 2), F = 𝒟G, ‖F‖² = 40.77466.
- True coefficients: W = 0.0951580, so W/N = 0.0023338.
- With only n = 2 deleted: W/N = −0.63923.
- Any proof must therefore see the actual prime coefficients. The ghost is a sensitivity control. It is not admissible Euler data.

2.7 **[Exact framework + Numerical]** *Ground-state / Birman–Schwinger reformulation* (geometry2006). The table superseded by the certificates above is n−(Q) = 1 at A = 1–4 (hat basis).
- Correct criterion (from §3.1): with Q invertible, W ≥ 0 on E0 iff n−(Q) + n+(S) = 2. The observed case is n−(Q) = 1 and S of signature (1,1).
- The S ≈ ±400 eigenvalues were basis artifacts (corrected in sos2010). **[Correction]**

## 3. Finite inertia and the signature of the boundary plane

3.1 **[Exact]** *Bordered inertia* (matching1989, inertia2057). Let Q = W − P (the full-window form) and S = B*Q⁻¹B (the 2×2 moment Schur complement).
- Then n−(Q|E0) = n−(Q) + n+(S) − 2.
- n+(J) = 1 + n−(W) for the extended form J. q_e ≈ −0.50404 (A = 0.6) and −0.5000004 (A = 1). **[Numerical]**

3.2 **[Certificate, IEEE model]** *Exactly one negative direction off E0* (inertia2057).
- A = 1: n−(Q) = 1 and the rest of the spectrum is ≥ 0.004. The constant trial gives Q ∈ [−1.95450, −1.95400]. Schur margin 0.000513.
- A = 1.1: n−(Q) = 1 and the rest of the spectrum is ≥ 0.0005. Q(const) ∈ [−2.1351, −2.1346]. Schur margin 0.000164.
- The signature of S, one positive and one negative, **is derived using the constrained certificate**. It is not an independent check.
- The finite minorant W_J alone has 2 negative directions. Only the constrained certificate removes them.

3.3 **[Numerical]** *Scan* (inertia2057). In every finite model from A = 0.5 to 3, Q has n− = 1. At 2048 cells, Q has inertia (1, 0, 2047), W has (0, 0, 2048), and S_Q has signature (−, +).
- The squared overlap of the negative Q-mode with span{e^{±u/2}} is 0.969–0.999. It is close to the span, but the mode is not in it.
- "The negative mode *is* the hyperbolic plane" is an analogy, not a theorem. **[Analogy]**
- The earlier "two negative directions" sketch is wrong: there is **one**. **[Correction]**

3.4 **[Exact]** *Boundary plane* (polarity2021; discussion).
- U = span{h, v} with J(h,h) = J(v,v) = 0 and J(h,v) = 1, so its signature is (1,1).
- The functional equation swaps h and v (B_U R = I).
- The fixed class e = h + v has J(e,e) = 2. Its normalizing residues are −1 and +1, those of the **completed zeta** Λ(s) = π^{−s/2}Γ(s/2)ζ(s) at s = 0 and s = 1. (ξ itself is entire. "Residues of ξ" was a misstatement.) **[Correction]**
- e^⊥ = R(h − v) ⊕ π(A), and J(h−v, h−v) = −2. So E0 ≠ e^⊥: e^⊥ also contains the negative line.

3.5 **[Exact, tautological]** *The formal boundary model only restates W.* Put πF = F − C₋(F)h − C₊(F)v. Then −J(πF, πG) = W(F, G) holds on all window tests (matching1989).
- J on tests is *defined* from W, so this identity is a bookkeeping device. It is not a sign theorem.
- A genuine Hodge-index argument needs a J built independently from geometry, with W = −(intersection) on the primitive sector **computed**, not defined.

3.6 **[Obstruction]** *Finite rank.* A fixed finite-rank "Néron–Severi" lattice cannot carry W. High frequencies make the form positive definite on an infinite-dimensional subspace of smooth E0. The atlas already records this argument in v1.20 (`bulk_form_B_off_E0`).

3.7 **[Exact + Numerical]** *Pencil discriminant / conic geometry* (parabolic1998).
- W(F) = ½·min over the pencil of Δ_e through e.
- disc(Q|ℓ) = −4 det M · Q(pole ℓ). There is one conic in a moving chart, with det = −1/4.
- Window lines are near-parabolic. The separation is 0.128, 1.46e−3 and 1.6e−7 as A grows. **[Numerical]**
- A dimension-4 counterexample shows that the conic picture alone does not force positivity. **[Obstruction]**

## 4. What the missing arithmetic class map Φ must satisfy (discussion; [Open])

4.1 **[Open]** A class map Φ from window tests to an arithmetic intersection space must be **built from geometry first**. Then W = −⟨Φ F, Φ F⟩ on the primitive sector must be **computed** as an intersection number. One concrete shape is Φ(F) = ∫F(u)[Γ_u] du, a superposition of graphs of the scaling action, with these properties:
- **(i)** Primes appear as fixed-point contributions with weight Λ(n)/√n (Lefschetz).
- **(ii)** The Gamma term appears as an archimedean Green term (k∞).
- **(iii)** M_A appears as the diagonal self-intersection.
- **(iv)** A Hodge-index theorem applies, with ampleness (A), effectivity (E) or a relative version (R), and a quadratic Riemann–Roch.

4.2 **[Exact / Obstruction]** *Ingredients audited* (effectivity2001, intersection2002, diagonal2003).
- (A) holds for the cone of positive functions. (E) fails for the pointwise cone.
- Relative lemma (GRR-type): (A) + (R) ⇒ n+(J) = 1.
- Derived self-intersection: Δ² = 2 − 2g. The arithmetic degree of the Tate dimension-1 diagonal is 0 (|d| = 1).
- Hecke ratios are 2cos(mθ_p). These do not collapse to Λ(n)/√n, so weight-12 data is a calibration only. **[Obstruction]**
- K₀ is a Mellin derivative (K₀ = 2E[log|x|] under the Tate weight). It is **not** an Arakelov degree. On P¹_Z, ω̂² = 2 − 4a ≠ −K₀ under every canonical metric tried; the gaps are 3.3722, 5.3722, 1.0827 and −0.3036. **[Obstruction]**
- The spin, Wu and Rokhlin structures give parity only. **[Obstruction]**

4.3 **[Exact calibration]** *Function-field check* (matching1989).
- A genus-2 curve over F₃ with N = 5, 19, 23, 75 reproduces the Weil sign through Δ² = 2 − 2g = −2 and Castelnuovo.
- The window covariance cocycle makes the completion unique up to κ.

4.4 **[Open]** *The test any Φ must pass.* It must reproduce the finite certificates: exactly one negative direction off E0, with gap ≥ 0.004 at A = 1 and ≥ 0.0005 at A = 1.1. Its intersection numbers must see the n = 2 coefficient (§2.6).

## 5. Response, passivity, storage (dispersion, KYP, blocks)

5.1 **[Exact]** *Probe identity* (dispersion2030).
- B_W(F_z, F_w) = K_q(z,w) = (q(z) + q̄(w))/(z + w̄), with q = ξ′/ξ(½ + z) and F_z = e^{−zu}1_{u≥0}, for Re z, Re w > ½.
- The pole, Gamma, K₀ and every prime term match. The independent check reproduces it at three pairs to ≤ 1e−13.
- RH ⇔ q is positive-real on Re z > 0 (Lagarias 1999; Hinkkanen) **[Cited]**.
- The step "PSD on one vertical line ⇒ W ≥ 0 on compact tests" uses inverse superposition. It is a sketched proof, not checked in full. **[Correction]**

5.2 **[Exact falsifiers / Analogy]** *Anomalous dispersion is not loss.* These are causal and stable but not passive: q = −1/(z+1), the ghost transfer q_a, and z + z³.
- Herglotz/positive-real is the needed property. Causality plus dispersion relations are not enough.
- Heaviside's distortionless line (LG = RC) is distortion-free and still lossy. Distortionless ≠ lossless (atlas `telegrapher_distortionless`). **[Analogy]**

5.3 **[Exact]** *Delay-line realization and signed KYP* (realization2033).
- The state evolution realizes q. Its storage identity is 2Re(ū y_B) = d/dt(S_∂ + S_jump) + D_jump − M_B|u|².
- The boundary storage S_∂ = 2Re(x₊x̄₋) is indefinite.
- **[Obstruction]**: a finite prime cutoff leaves a pole at z = ½, and independent prime-line storage diverges.
- The pole-cancelled transfer is q = g₅ − ∫x^{−z−½} dE.
- q′(0) = 0.0462099862 > 0 follows from a positive Φ-type (theta) representation. This is not passivity: z + z³ also has positive derivative.

5.4 **[Obstruction]** *Block positivity* (blocks2038).
- Fixed-diagonal PSD coupling diverges; it needs ≥ (√P_B − √G)².
- The exact-match 2×2 block fails at cutoff B = 2, s₀ = 49/25: g = 0.003012, d = 0.107651, w = −0.104639, det = −0.0112645. The required ratio is ρ_req = 5.978.
- **New in this audit [Numerical]**: w_B < 0 on four intervals at B = 2, directly after log 2, log 3, log 5 and log 7: (0.693, 0.766), (1.099, 1.183), (1.609, 1.707) and (1.946, 2). See fig2.
- At s = 0.5, w = +0.20412, while the ghost gives −0.28601. q_{E2}(0) = −0.17576.

5.5 **[Exact + Obstruction]** *KMS / primon gas* (kms2040).
- The boson gas has Z = ζ(β). The fermion gas has Z = ζ(β)/ζ(2β), with the wrong sign at n = 4 and 9.
- The Bost–Connes KMS state at β = ½ gives vectors with ‖v_n‖² = Λ(n)/√n exactly. **[Exact + Cited]**
- Their kernel is −ζ′/ζ(½ + z + w̄). That is **not** K_q: the Gamma, pole and mass terms are missing. The all-prime vector has infinite norm. **[Obstruction]**
- Sample values: C₂ = 0.63038, J = 0.100396, K_q(1,2) = 0.045990.

5.6 **[Exact / Analogy]** *Planck ladder.*
- k∞(a) = Σ_m e^{−(2m+½)a}. This is an Ornstein–Uhlenbeck / Planck tower with rates 2m + ½. **[Exact]**
- Reading the Gamma term as blackbody radiation and the primes as a primon gas is suggestive. They are not the same Hamiltonian. **[Analogy]**
- The kinetic-vs-potential reading: H_A ≥ 0 is kinetic, M_A is a potential threshold, and positivity is a spectral-gap question. That reading is accurate as bookkeeping. It is not a sign mechanism.

## 6. Modular and boundary calibrations (cusp, Eisenstein, 691)

6.1 **[Exact]** *Serre derivative* (eisenstein1990, modular2026).
- D E_k has a cusp correction a₁(f_k), and f_k = 0 iff S_{k+2} = 0, i.e. k ∈ {4, 6, 8, 12}. The proof uses a Bernoulli-number bound, with an exact check for 14 ≤ k ≤ 398.
- D E₁₀ carries the coefficient 38016/691. Checks: D₄E₄ = −E₆/3 and D₆E₆ = −E₄²/2.
- −φ′/φ(½ + it) = 4Re Λ′/Λ(1 + 2it).

6.2 **[Exact]** *Half-density.* The radial cusp operator −y²∂_y² is unitarily −∂_t² + 1/4, the same 1/4 as in §1.3. This is not the W operator. Also, the parallel E₂ = θ log Δ vs K₀ = 2(log Γ_R)′(½) is not one identified connection, because E₂ has divisor-sum coefficients and W needs prime-power weights. **[Obstruction to naive identification]**

6.3 **[Exact]** *691 at the boundary* (hodge1991, boundary1994).
- In M₁₂(Z), the index of 691E₁₂ ⊕ ZΔ is 691. T₂ = [[2049, 0], [−1296000, −24]], and 2049 ≡ −24 mod 691. So mod 691 the Hecke algebra Z[T₂] has a nilpotent N = T₂ + 24 with ker N = im N = the line of Δ (a unipotent-monodromy shadow).
- The fibre form has signature (5, 6). Sym² has signature (1, 2), and ⟨Δ, Δ⟩ = 1.0353620568e−6.
- X¹⁰ − 1 = δ(1) is a **boundary class in H¹_c**. It is not "the Eisenstein class" as hodge1991 said. **[Correction]**
- Eis₁ has denominator 691 (3617 at k = 16). D(δ₁, ψ) = 6·res ψ.
- One cusp supplies one moment. A two-moment dictionary needs Γ₀(N) with two cusps. M_A has no modular counterpart. **[Open]**

6.4 **[Exact + Obstruction]** *SL₂(Z) cusp mismatch* (counterterm1995). K₀ − K₀^{(1)} = −π/2 − log 2. The cusp outputs σ = 1 data, not σ = ½ data.

## 7. Open problems (front of v1.21)

1. **[Open]** Construct Φ from geometry (§4.1), with the pairing computed, so that W = −(intersection) on the primitive sector, and prove a Hodge index theorem that applies.
2. **[Open]** Extend certified positivity beyond A = 1.1 with grid bias controlled. Next target: A = 1.5 (primes 2, 3, 4) with a gap of about 1.7e−5. The current certificate method needs about 100× more resolution.
3. **[Open]** An independently positive coupled storage that reproduces K_q exactly (§5).
4. **[Open]** A two-cusp (Γ₀(N)) dictionary that carries both moments and a modular origin for M_A (§6.3).

## 8. Closed or narrowed routes (in scope stated)

- Fixed-diagonal PSD block storage (§5.4).
- Exact-match prime-gap blocks (§5.4).
- KMS kernel as K_q (§5.5).
- Fermion primon (wrong signs).
- Finite-rank NS (§3.6).
- K₀ as an Arakelov degree on P¹_Z (§4.2).
- Hecke weight-12 collapse to Λ(n)/√n.
- Spin/Wu parity.
- Elementary moment-blind chain bounds at A = 1 (§2.1).
- "Causal + dispersive ⇒ passive".

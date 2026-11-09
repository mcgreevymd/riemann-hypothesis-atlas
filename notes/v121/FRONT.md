## Since v1.20

> **RH is not proved; no all-window positivity.** The Riemann Hypothesis is not proved. Nothing here proves it. Nothing here proves positivity of the Weil form W for all windows. W ≥ c‖F‖² on E0 is established only for windows of width A ≤ 1.1. It is analytic for A ≤ 1/10, interval-certified for A ≤ 0.694, and computer-assisted for A ≤ 1 and A ≤ 1.1. Every statement for A > 1.1 is numerical. Grid bias at that scale is about the same size as the gap. Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

Work of 8 Nov 2026 (America/Chicago), integrated 9 Nov 2026 (UTC). Counts: 1066 concepts (+22) and 2108 typed relations (+57). Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. [AUDIT.md](notes/v121/provenance/AUDIT.md) overrides the synthesis and the archived notes. Raw notes are archived and are not quoted here.

**Status tags.** **[Exact]** an identity or hand proof, with literature marked **[Cited]**. **[Certificate]** a computer-assisted bound: mpmath intervals for scalars, and IEEE-754 binary64 for finite matrices (dot-product error γ_n = nu/(1−nu), u = 2⁻⁵³, plus residual and orthogonality bounds). **This is not a formally verified proof.** **[Numerical]** a computation without an error certificate. **[Obstruction]** a proved no-go in the stated scope only. **[Analogy]** a structural or physics reading with no arithmetic map. **[Open]** missing.

**Notation.** The operator ledger (§1 of the synthesis) is recorded after the closed routes, so the frontier and the one-negative-direction certificate lead. I_A = [−A/2, A/2]. C± = ∫ F e^{±u/2}. E0 = ker C₊ ∩ ker C₋. W = P + H_A − M_A‖F‖², with P = 2 Re C₊ conjugate C₋. a_n = Λ(n)/√n and M_A = −K₀ + 2 Σ_{log n<A} a_n. K₀ = ψ(1/4) − log π = −γ − π/2 − 3 log 2 − log π = −5.372183. k∞(a) = e^{−a/2}/(1−e^{−2a}).

### The honest frontier

**[Exact]** *No-prime windows.* For A ≤ 1/10, W ≥ c*‖F‖² on E0 with c* = log(5√2/π) − γ − 3/80 ≈ 0.19657 > 7/240. Moment-blind chain bounds fail early. At A = 1 the bound gives 3.7528 against the 6.3524 needed. **[Numerical]**

**[Certificate, interval]** *One prime, n = 2.* For A ≤ 347/500 (0.694), W ≥ 0.0045‖F‖² on E0, by a constrained log-Jensen lemma. The numbers are certified with mpmath.iv (combined margin ≈ 0.005275; k_low > 9.0258; K(9) > 0.358; θ = 3/16). The bound fails to close at 0.695. That is inconclusive. It is not a counterexample.

**[Certificate, IEEE model]** *A ≤ 1, prime n = 2.* N = 48 Gamma terms, κ = 2, 815 cells. Finite compressed eigenvalue > 0.0069963; high-block lower h* > 2.2304; cross bound B* < 0.07587; Schur margin > 0.000314. Conclusion: **W ≥ (1/250)‖F‖² on E0.**

**[Certificate, IEEE model]** *A ≤ 1.1, primes n = 2, 3.* N = 192, κ = 4, 1838 cells. Verified effective eigenvalue > 0.00066384; h* > 3.20786; derivative and moment Schur coefficients 1/40000000 and 1/4000000. Conclusion: **W ≥ 0.0005‖F‖² on E0.**

**[Numerical]** Beyond 1.1, constrained E0 minima (upper estimates only):

| A | 0.5 | 0.694 | 1 | 1.1 | 1.5 | 2 | 2.5 | 3 |
|---|---|---|---|---|---|---|---|---|
| min W/‖F‖² on E0 | 0.8749 | 0.5455 | 0.011872 | 0.00093187 | 1.72e−5 | 1.278e−5 | 1.30e−5 | 1.2786e−5 |

The 128-cell and 2048-cell values differ by about 100× beyond A ≈ 1.1. **There is no all-window statement.**

**[Numerical]** *Ghost control.* The test is G = (1−u²)⁴ on [−1, 1] (A = 2), F = (∂² − 1/4)G, ‖F‖² = 40.77466. True coefficients: W = 0.0951580, so W/N = 0.0023338. With only n = 2 deleted: W/N = −0.63923. Any proof must see the actual prime coefficients. The ghost is a quadrature sensitivity control. It is not admissible Euler data and not a counterexample.

**[Exact framework + Numerical]** *Ground-state / Birman–Schwinger.* The table superseded by the certificates above is n−(Q) = 1 at A = 1–4 (hat basis). With Q invertible, W ≥ 0 on E0 if and only if n−(Q) + n+(S) = 2. The observed case is n−(Q) = 1 and S of signature (1,1). The S ≈ ±400 eigenvalues were basis artifacts. **[Correction]**

### One negative direction

**[Exact]** *Bordered inertia.* Let Q = W − P and S = B* Q⁻¹ B, the 2×2 moment Schur complement. Then n−(Q|E0) = n−(Q) + n+(S) − 2. n+(J) = 1 + n−(W) for the extended form J. q_e ≈ −0.50404 (A = 0.6) and −0.5000004 (A = 1). **[Numerical]**

**[Certificate, IEEE model]** *Exactly one negative direction off E0.* At A = 1, n−(Q) = 1 and the rest of the spectrum is ≥ 0.004. The constant trial gives Q ∈ [−1.95450, −1.95400]. Schur margin 0.000513. At A = 1.1, n−(Q) = 1 and the rest of the spectrum is ≥ 0.0005. Q(const) ∈ [−2.1351, −2.1346]. Schur margin 0.000164. The signature of S, one positive and one negative, **is derived using the constrained certificate**. It is not independent evidence. The finite minorant W_J alone has 2 negative directions. Only the constrained certificate removes them. Statements for A > 1.1 are numerical only. **[Correction]**

**[Numerical]** *Scan.* In every finite model from A = 0.5 to 3, Q has n− = 1. At 2048 cells, Q has inertia (1, 0, 2047), W has (0, 0, 2048), and S_Q has signature (−, +). The squared overlap of the negative Q-mode with span{e^{±u/2}} is 0.969–0.999. The mode is close to that span and is not in it. “The negative mode is the hyperbolic plane” is an analogy, not a theorem. **[Analogy]** The earlier “two negative directions” sketch is wrong: there is **one**. **[Correction]**

**[Exact]** *Boundary plane.* U = span{h, v} with J(h,h) = J(v,v) = 0 and J(h,v) = 1, so its signature is (1,1). The functional equation swaps h and v. The fixed class e = h + v has J(e,e) = 2. Its normalizing residues are −1 and +1, those of the **completed zeta** Λ(s) = π^{−s/2}Γ(s/2)ζ(s) at s = 0 and s = 1. ξ is entire. “Residues of ξ” was a misstatement. **[Correction]** e^⊥ = R(h − v) ⊕ π(A), and J(h−v, h−v) = −2. So E0 ≠ e^⊥: e^⊥ also contains the negative line h − v.

**[Exact, tautological]** *The formal boundary model only restates W.* Put πF = F − C₋(F)h − C₊(F)v. Then −J(πF, πG) = W(F, G) on all window tests. J on tests is defined from W, so this identity is bookkeeping. It is not a sign theorem and not evidence for a Hodge index theorem. A genuine Hodge-index argument needs a J built independently from geometry, with W = −(intersection) on the primitive sector computed, not defined.

**[Obstruction]** *Finite rank.* A fixed finite-rank Néron–Severi lattice cannot carry W. High frequencies make the form positive definite on an infinite-dimensional subspace of smooth E0. The atlas already records this in v1.20 (`bulk_form_B_off_E0`).

**[Exact + Numerical]** *Pencil discriminant.* W(F) = ½ min over the pencil of Δ_e through e. disc(Q|ℓ) = −4 det M · Q(pole ℓ). There is one conic in a moving chart, with det = −1/4. Window lines are near-parabolic. The separation is 0.128, 1.46e−3 and 1.6e−7 as A grows. **[Numerical]** A dimension-4 counterexample shows that the conic picture alone does not force positivity. **[Obstruction]**

### The missing arithmetic class map Φ

**[Open]** A class map Φ from window tests to an arithmetic intersection space must be built from geometry first. Then W = −⟨ΦF, ΦF⟩ on the primitive sector must be computed as an intersection number. One concrete shape is Φ(F) = ∫ F(u)[Γ_u] du, with these properties: **(i)** primes appear as fixed-point contributions with weight Λ(n)/√n (Lefschetz); **(ii)** the Gamma term appears as an archimedean Green term (k∞); **(iii)** M_A appears as the diagonal self-intersection; **(iv)** a Hodge-index theorem applies, with ampleness (A), effectivity (E) or a relative version (R), and a quadratic Riemann–Roch.

**[Exact / Obstruction]** *Ingredients audited.* (A) holds for the cone of positive functions. (E) fails for the pointwise cone. Relative lemma (GRR-type): (A) + (R) ⇒ n+(J) = 1. Derived self-intersection: Δ² = 2 − 2g. The arithmetic degree of the Tate dimension-1 diagonal is 0. Hecke ratios are 2 cos(m θ_p). These do not collapse to Λ(n)/√n, so weight-12 data is a calibration only. **[Obstruction]** K₀ is a Mellin derivative (K₀ = 2 E[log|x|] under the Tate weight). It is not an Arakelov degree. On P¹_Z, ω̂² = 2 − 4a ≠ −K₀ under every canonical metric tried; the gaps are 3.3722, 5.3722, 1.0827 and −0.3036. **[Obstruction]** The spin, Wu and Rokhlin structures give parity only. **[Obstruction]**

**[Exact calibration]** *Function-field check.* A genus-2 curve over F₃ with N = 5, 19, 23, 75 reproduces the Weil sign through Δ² = 2 − 2g = −2 and Castelnuovo. The window covariance cocycle makes the completion unique up to κ.

**[Open]** *The test any Φ must pass.* It must reproduce the finite certificates: exactly one negative direction off E0, with gap ≥ 0.004 at A = 1 and ≥ 0.0005 at A = 1.1. Its intersection numbers must see the n = 2 coefficient.

### Response, passivity, storage

**[Exact]** *Probe identity.* B_W(F_z, F_w) = K_q(z, w) = (q(z) + conjugate q(w))/(z + conjugate w), with q = ξ′/ξ(½ + z) and F_z = e^{−zu} 1_{u≥0}, for Re z, Re w > ½. The pole, Gamma, K₀ and every prime term match. The independent check reproduces it at three pairs to ≤ 1e−13. RH ⇔ q is positive-real on Re z > 0 (Lagarias 1999; Hinkkanen) **[Cited]**. The step “PSD on one vertical line ⇒ W ≥ 0 on compact tests” uses inverse superposition. It is a sketched proof, not checked in full. **[Correction]**

**[Exact falsifiers / Analogy]** *Anomalous dispersion is not loss.* These are causal and stable but not passive: q = −1/(z+1), the ghost transfer q_a, and z + z³. Herglotz/positive-real is the needed property. Causality plus dispersion relations are not enough. Heaviside’s distortionless line (LG = RC) is distortion-free and still lossy. Distortionless is not lossless. **[Analogy]**

**[Exact]** *Delay-line realization and signed KYP.* The state evolution realizes q. Its storage identity is 2 Re(ū y_B) = d/dt(S_∂ + S_jump) + D_jump − M_B|u|². The boundary storage S_∂ = 2 Re(x₊ conjugate x₋) is indefinite. **[Obstruction]**: a finite prime cutoff leaves a pole at z = ½, and independent prime-line storage diverges. The pole-cancelled transfer is q = g₅ − ∫ x^{−z−½} dE. q′(0) = 0.0462099862 > 0 follows from a positive Φ-type (theta) representation. This is not passivity: z + z³ also has positive derivative.

**[Obstruction]** *Block positivity.* Fixed-diagonal PSD coupling diverges; it needs ≥ (√P_B − √G)². The exact-match 2×2 block fails at cutoff B = 2, s₀ = 49/25: g = 0.003012, d = 0.107651, w = −0.104639, det = −0.0112645. The required ratio is ρ_req = 5.978. **[Numerical]** w_B < 0 on four intervals at B = 2, directly after log 2, log 3, log 5 and log 7: (0.693, 0.766), (1.099, 1.183), (1.609, 1.707) and (1.946, 2). At s = 0.5, w = +0.20412, while the ghost gives −0.28601. q_{E2}(0) = −0.17576.

**[Exact + Obstruction]** *KMS / primon gas.* The boson gas has Z = ζ(β). The fermion gas has Z = ζ(β)/ζ(2β), with the wrong sign at n = 4 and 9. The Bost–Connes KMS state at β = ½ gives vectors with ‖v_n‖² = Λ(n)/√n exactly. **[Exact + Cited]** Their kernel is −ζ′/ζ(½ + z + conjugate w). That is not K_q: the Gamma, pole and mass terms are missing. The all-prime vector has infinite norm. **[Obstruction]** Sample values: C₂ = 0.63038, J = 0.100396, K_q(1, 2) = 0.045990.

**[Exact / Analogy]** *Planck ladder.* k∞(a) = Σ_m e^{−(2m+½)a}. This is an Ornstein–Uhlenbeck / Planck tower with rates 2m + ½. **[Exact]** Reading the Gamma term as blackbody radiation and the primes as a primon gas is suggestive. They are not the same Hamiltonian. **[Analogy]** The kinetic-versus-potential reading is accurate as bookkeeping. It is not a sign mechanism. **[Analogy]**

### Modular and boundary calibrations

**[Exact]** *Serre derivative.* D E_k has a cusp correction a₁(f_k), and f_k = 0 if and only if S_{k+2} = 0, that is k ∈ {4, 6, 8, 12}. The proof uses a Bernoulli-number bound, with an exact check for 14 ≤ k ≤ 398. D E₁₀ carries the coefficient 38016/691. Checks: D₄ E₄ = −E₆/3 and D₆ E₆ = −E₄²/2. −φ′/φ(½ + it) = 4 Re Λ′/Λ(1 + 2it).

**[Exact]** *Half-density.* The radial cusp operator −y² ∂_y² is unitarily −∂_t² + 1/4, the same 1/4 as in the moment parametrization. This is not the W operator. The parallel E₂ = θ log Δ versus K₀ = 2 (log Γ_R)′(½) is not one identified connection, because E₂ has divisor-sum coefficients and W needs prime-power weights. **[Obstruction to naive identification]**

**[Exact]** *691 at the boundary.* In M₁₂(Z), the index of 691 E₁₂ ⊕ Z Δ is 691. T₂ = [[2049, 0], [−1296000, −24]], and 2049 ≡ −24 (mod 691). So mod 691 the Hecke algebra Z[T₂] has a nilpotent N = T₂ + 24 with ker N = im N = the line of Δ. “T₂ nilpotent mod 691” is imprecise. **[Correction]** The fibre form has signature (5, 6). Sym² has signature (1, 2), and ⟨Δ, Δ⟩ = 1.0353620568e−6. X¹⁰ − 1 = δ(1) is a **boundary class in H¹_c**. It is not the Eisenstein class. **[Correction]** Eis₁ has denominator 691 (3617 at k = 16). D(δ₁, ψ) = 6 · res ψ. One cusp supplies one moment. A two-moment dictionary needs Γ₀(N) with two cusps. M_A has no modular counterpart. **[Open]**

**[Exact + Obstruction]** *SL₂(Z) cusp mismatch.* K₀ − K₀^{(1)} = −π/2 − log 2. The cusp outputs σ = 1 data, not σ = ½ data.

### Open problems

1. **[Open]** Construct Φ from geometry, with the pairing computed, so that W = −(intersection) on the primitive sector, and prove a Hodge index theorem that applies.
2. **[Open]** Extend certified positivity beyond A = 1.1 with grid bias controlled. Next target: A = 1.5 (primes 2, 3, 4) with a gap of about 1.7e−5. The current certificate method needs about 100× more resolution.
3. **[Open]** An independently positive coupled storage that reproduces K_q exactly.
4. **[Open]** A two-cusp (Γ₀(N)) dictionary that carries both moments and a modular origin for M_A.

### Closed or narrowed routes

Fixed-diagonal PSD block storage. Exact-match prime-gap blocks. The KMS kernel as K_q. The fermion primon gas (wrong signs). Finite-rank Néron–Severi. K₀ as an Arakelov degree on P¹_Z. A Hecke weight-12 collapse to Λ(n)/√n. Spin/Wu parity. Elementary moment-blind chain bounds at A = 1. “Causal + dispersive ⇒ passive.”

### Ledger and operator

**[Exact]** *Signed self-adjoint window operator.* K_A = L_A − M_A + P_A is the operator of the closed semibounded form W on L²(I_A). L_A is the Gamma and prime jump operator, M_A is the constant mass, and P_A is the rank-2 pole part. The Gamma symbol grows like log|t|, so the form domain is a log-Sobolev space. H_A ≥ 0 is the kinetic bookkeeping term. M_A is a constant potential threshold. That reading is not a sign mechanism. **[Analogy]** Missing: ‖J_A F‖² ≥ M_A‖F‖² on E0 with no zeros used. **[Open]**

**[Exact]** *Pole-cancelled identity.* W = K₅‖F‖² + J₅ − 2∫ x^{−1/2}⟨F, T_{log x} F⟩ dE(x), where E = ψ_Cheb − x and K₅(0) = K₀ + 4. The unconstrained residual mass is M̃_A = M_A − 4e^{A/2}: −0.2424 (A=1), 0.3515 (A=2) and 0.4611 (A=3). **[Numerical]** “Lemma A” of the source note is only a Ritz value. **[Correction]**

**[Exact]** *Moment parametrization.* 𝒟 = ∂² − 1/4 is a bijection from H²₀(I_A) onto the L² tests in E0. In the unitary chart r = e^{−u}, 𝒟 becomes ∂_r(r² ∂_r). The constant 1/4 is the Hardy constant and also the bottom of the continuous spectrum at the cusp. The operators are not identified.

**[Exact]** *M_A as a regularized prime sum.* M_A = 2(S_A − S_reg), where S_reg = −ζ′/ζ(½) = K₀/2. −K₀ = γ + log 8π + π/2. The finite-part integral is FP∫ k∞ = π/2 + 2 log 2. Under Connes’ semilocal trace (Connes 1999, Thm VII.4) **[Cited]**, M_A is the total α-normalized degree mass in degree form. K₀ is fixed by the adelic character class. There is no free renormalization parameter. **[Correction]**

**[Numerical, diagnostic only]** The explicit-formula table with 400 zeros uses zeros. It is a diagnostic and cannot be part of any positivity argument (atlas: `tautology_boundary`). The zero-based table is never used for a sign.

**Read next.** Corrected narrative: [notes/v121/SYNTHESIS.md](notes/v121/SYNTHESIS.md). Binding audit: [notes/v121/provenance/AUDIT.md](notes/v121/provenance/AUDIT.md). Raw notes are historical: [notes/v121/provenance/SUPERSEDED.md](notes/v121/provenance/SUPERSEDED.md).

<p align="center"><a href="figures/v121/fig1_frontier.svg"><img src="figures/v121/fig1_frontier.png" width="720" alt="Certified lower bounds on W over E0 stop at window width 1.1. The missing piece is an arithmetic class map."></a><br><sub>Figure 1. What is proved, what is only computed, and what is missing. Certified bars: A ≤ 0.1, 0.1966 [Exact]; A ≤ 0.694, 0.0045 [Interval certificate]; A ≤ 1, 0.004 [Computer-assisted]; A ≤ 1.1, 0.0005 [Computer-assisted]. The grey curve and the dots are 128-cell and 2048-cell minima [Numerical, upper estimates]. For A &gt; 1.1 the computed gap is about the size of the discretization error. Deleting only n = 2 gives −0.639 at A = 2, against +0.0023 with the true coefficients. The sign pattern is one negative direction absorbed by two moments. The arithmetic class map that would make that a theorem is missing. <b>The Riemann Hypothesis is not proved. No all-window positivity is claimed.</b> <a href="figures/v121/fig1_frontier.svg">SVG</a>.</sub></p>

<p align="center"><a href="figures/v121/fig2_response_storage.svg"><img src="figures/v121/fig2_response_storage.png" width="720" alt="Signed storage weight at cutoff 2 is negative just after log 2, 3, 5 and 7"></a><br><sub>Figure 2. The response reading of W, and where storage fails. The signed storage weight w_B(s) at cutoff B = 2 is negative just after log 2, 3, 5 and 7 [Numerical]. At s = 1.96 the failure is proved: det = −0.01126 [Obstruction]. The probe identity B_W = K_q is [Exact]. Lagarias/Hinkkanen is [Cited]. Signed KYP is [Exact]. The KMS kernel at β = ½ is not K_q. Coupled positive storage is [Open]. <b>The Riemann Hypothesis is not proved. No all-window positivity is claimed.</b> <a href="figures/v121/fig2_response_storage.svg">SVG</a>.</sub></p>

<p align="center"><a href="figures/v121/fig3_inertia_scan.svg"><img src="figures/v121/fig3_inertia_scan.png" width="720" alt="Finite models show one negative direction of Q, with squared overlap 0.969 to 0.999"></a><br><sub>Figure 3. Finite inertia scan. Eigenvalues of S_Q, with n−(Q) = 1 and n−(Q|E0) = 0 on the 128-cell models, A = 0.5 to 3. The squared overlap of the negative Q-mode with span{e^{±u/2}} is 0.969 to 0.999: close to the moment span, and not inside it. All of this figure is [Numerical]. Only A = 1 and A = 1.1 are certified. <b>The Riemann Hypothesis is not proved. No all-window positivity is claimed.</b> <a href="figures/v121/fig3_inertia_scan.svg">SVG</a>.</sub></p>

Entries: [window operator](ATLAS.md#signed-window-operator), [pole-cancelled ledger](ATLAS.md#pole-cancelled-chebyshev-ledger), [moment parametrization](ATLAS.md#moment-parametrization-hardy-quarter), [character-class mass](ATLAS.md#mass-counterterm-character-class), [no-prime bound](ATLAS.md#small-window-poincare-bound), [prime-window certificates](ATLAS.md#prime-window-certificates), [grid bias](ATLAS.md#e0-minima-grid-bias), [n = 2 ghost](ATLAS.md#n2-deletion-ghost-control), [one negative direction](ATLAS.md#one-negative-direction-certificate), [FE-fixed class](ATLAS.md#fe-fixed-boundary-class), [projection restates W](ATLAS.md#formal-projection-restates-w), [requirements on Φ](ATLAS.md#arithmetic-class-map-requirements), [pencil conic](ATLAS.md#pencil-discriminant-window-conic), [K₀ is not a degree](ATLAS.md#k0-not-arakelov-degree), [probe identity](ATLAS.md#probe-response-identity), [dispersion is not passivity](ATLAS.md#dispersion-not-passivity), [signed KYP](ATLAS.md#signed-kyp-delay-line), [prime-gap blocks](ATLAS.md#prime-gap-block-obstruction), [KMS kernel](ATLAS.md#kms-half-kernel-not-response), [Planck ladder](ATLAS.md#gamma-kernel-planck-ladder), [Serre derivative](ATLAS.md#serre-derivative-cusp-correction), [boundary class 691](ATLAS.md#boundary-class-691).

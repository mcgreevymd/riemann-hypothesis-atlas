# geometry2006 (t2006; Nov 8 2026 ~2:10–2:45 PM CST). Scratch only; no Page/repo/manuscript edits. RH NOT proved.
Files: osc2006.py/json (quartic oscillator geometry; xp count), gs2006.txt/json (ground-state + inertia test; reuses
interactions1890/check1890.py kernel unchanged, h=0.05 hat basis, finite windows = calibration only).
Recovery: transcript search for prior sessions returned no readable record from this run; recovered from local notes instead:
oscillator1927, ground1896, momentum1929, interactions1890, restframe1928, kepler1925, heis1921, geometry1897, quadratic1938,
bridge1285, bridge1842, bridge1783/s6, walls1960, synthesis1953, parabolic1998, effectivity2001, intersection2002, diagonal2003.

## A. Already-defined geometric objects (recovered; exact unless marked)
1. Mediator / spring geometry (interactions1890, spring1891): on a window, W = P + ∫k_∞(a)‖F−T_aF‖²da + Σa_n‖F−T_{log n}F‖² − M_N‖F‖²,
   M_N = −K0 + 2Σa_n. Φ_N with quartic springs U = z²/2 + λz⁴/4 has Hess Φ_N(0) = W [EXACT]. A nonlocal Dirichlet (jump) form minus a mass.
2. Vacuum/score geometry (heis1921): W(F) = d/dσ|_{½}‖U_σF‖², Gram family of positive local vacua (Γ_R, L_p) [EXACT on E0].
3. Boundary/observer geometry (restframe1928): pole form P = 2Re(a b̄) on (ev0, ev1) = hyperbolic plane U, and the FE swap σ is its
   Cartan involution. The boundary "rest frame" is already fixed [EXACT]. E0 = primitive part, still lacking an independent form.
4. Genus-1 / Frobenius chamber geometry (bridge1285, bridge1842, bridge1783 S6): Q = m² − tmn + qn², with lobe = CM elliptic curve,
   wall = Hasse, wedge = NC torus. Over F_q, (ω, J) gives g = 2·trace form; occupancy-blind (Waterhouse fakes) [THM+NUM]. Over Q the analogue polarizes the wrong space.
5. Pencil/discriminant geometry (parabolic1998, kepler1925): disc(Q|ℓ) = −4 det M·Q(pole ℓ); W = ½ min of a pencil discriminant;
   pencil W_t = H − tB with real threshold μ_max ≤ 1 vs Neumann (Laplace-limit) radius [EXACT/NUM].
6. Derived diagonal (diagonal2003): ω̂²(P¹_Z) = 2 − 4a, anomaly −4; K0 = 2(log Γ_R)'(½) is a Mellin derivative, not a degree [EXACT].
Closed and not reopened: Rosati/finite Jacobian wrong-space routes, wall incidence as a certificate.

## B. Minimal components of "a geometry" (standard, no universal notion)
 Layers (choose by the observables you need; this is not a catalogue):
 - point-set: set + topology (opens / continuity);
 - smooth: charts with smooth transition maps (tangent vectors, flows, forms; de Rham d² = 0);
 - algebraic: locally ringed space (structure sheaf; local rings = germs; points = primes/valuations);
 - noncommutative/derived: algebra (+ Hilbert rep, Dirac / spectral triple) or dg/derived structure when quotients are bad (adele class space).
 For a TRACE-FORMULA geometry the operational minimum is: (1) an algebra of observables/test functions with convolution;
 (2) points/states/representation and locality; (3) cycles/correspondences with a trace (Lefschetz), and cohomology (d² = 0) where available;
 (4) boundary/duality (PD/FE); (5) a polarization: an independently defined positive * (Hodge/Rosati/ample).
 "Geometry" is not defined by a positive pairing, nor is a metric automatically canonical. Items (1)–(4) exist already over Q
 (Connes adele class space / scaling groupoid, Connes trace formula with weights Λ(n)/√n, Tate FE, pole form).
 The missing item is (5) together with its compatibility/identification with (1)–(4). It is not "absence of any space".
 Also: the "need Φ: E0 → H^{1,1}" was a chosen Hodge route, not a logical necessity; flow/operator/spectral routes are equally legitimate.
 Circularity guards: GNS from W presupposes W ≥ 0; a spectral triple exists without giving the zeta sign; ω + compatible J have many
 choices, none forced to match W; "axioms packaging RH" is not a construction. A construction must be falsifiable by local compatibility,
 functoriality, window enlargement and Beurling/ghost fakes.

## C. The oscillator as a generator-first template (computed, osc2006.json)
 H = p²/2 + q²/2 + λq⁴/4 (λ > 0).
 - Energy curve p² = 2E − q² − λq⁴/2. disc_q = −16Eλ(4Eλ+1)² [EXACT, sympy], so for λ > 0 every E > 0 gives a smooth genus-1 curve
   (two points at infinity).
 - j = 16(12Eλ−1)³ / (Eλ(4Eλ+1)²): it depends only on Eλ (scaling symmetry). The singular fibre E = 0 is the minimum.
   All of this is fixed by H, not by the spectrum.
 - Positivity is natural because H is bounded below: ground state u0 > 0, φ = −u0'/u0, H − E0 = ½(−∂+φ)(∂+φ) = ½A*A (Riccati checked
   to FD accuracy 2e−2). E0 = 0.620916 (λ = 1). Spectrum 0.6209, 2.0259, 3.6982, 5.5571, 7.5675.
 - Bohr–Sommerfeld ∮p dq = 2π(n+½) on the energy curve gives 0.573, 2.003, 3.682, 5.544, 7.557 (rel. err 7.7%, 1.1%, 0.44%, 0.23%, 0.14%).
   The ½ is the Maslov index of the turning points [THM].
 Arithmetic counterpart of the generator: the scaling (dilation) generator H = xp. Its level sets are hyperbolas (genus 0, no turning
 points, not bounded below; quantum spectrum all of R, heis1921). With a cutoff, the phase-space count gives
 N_smooth(T) = θ(T)/π + 1 = (T/2π)(log(T/2π) − 1) + 7/8 + O(1/T): checked at T = 50, 200, 1000, with differences 1.3e−4, 3.3e−5, 6.6e−6 [EXACT asymptotic].
 Lesson [EXACT]: the oscillator's positivity comes from bounded-below H via its ground state. xp lacks it, so the positivity must be built
 elsewhere. The natural place is the window jump form (item A1), which IS bounded below relative to a mass term.

## D. One targeted construction (executed round 1): ground-state transform of the window jump form
 Q_A := W − P on the full window = D_A − M_N, where D_A = Lévy jump + prime jump Dirichlet form (zero outside the window).
 Exact (continuum, standard Beurling–Deny + Perron–Frobenius, irreducible jump kernel): e^{−tD_A} is positivity improving, so the lowest
 eigenfunction u0 > 0 is simple, and
   Q_A(F) = λ0‖F‖² + ½∬ J(u,v) u0(u)u0(v) |F/u0(u) − F/u0(v)|² du dv   (ground-state representation; the oscillator's A*A).
 Bordered-inertia (Haynsworth) on E0 = ker(ev+, ev−) with C = [e^{u/2}, e^{−u/2}] and S = Cᵀ Q⁻¹ C:
   n₋(W|E0) = n₋(Q) + n₊(S) − 2. So W ≥ 0 on E0 ⇔ (n₋(Q) = 1 and n₊(S) = 1) or (n₋(Q) = 2 and S ≤ 0).
 Birman–Schwinger [EXACT]: n₋(Q_A) = #{eigenvalues of D_A below M_N}, a zeros-blind spectral count for an explicit operator.
 Computed (gs2006.json; NUM, hat basis):
| A | λ0(Q) | λ1, λ2 | n₋(Q) | u0 min/max | S eigs | n₋ on E0 (Haynsworth / direct) |
|---|---|---|---|---|---|---|
| 1 | −1.938 | 1.7e−2, 2.0e−2 | 1 | 0.84 | −400.0, +394.1 | 0 / 0 |
| 2 | −4.230 | 1.8e−5, 4.6e−5 | 1 | 0.79 | −400.0, +399.9 | 0 / 0 |
| 3 | −7.131 | 4.6e−6, 1.0e−5 | 1 | 0.63 | −400.0, +400.0 | 0 / 0 |
| 4 | −11.10 | 1.1e−6, 2.9e−6 | 1 | 0.52 | −400.0, +400.0 | 0 / 0 |
 Reading: exactly ONE bound state below 0, with a positive ground state (natural, zeros-blind), and the 2×2 boundary matrix S of signature (1,1).
 The second eigenvalue of D_A sits only 1e−6 above M_N: the whole difficulty is concentrated in that single gap.
 This localizes the sign problem to two zeros-blind, certifiable statements per window:
   (G1) λ2(D_A) ≥ M_N (one bound state), and (G2) n₊(S_A) = 1.
 Not a proof; for all windows this is equivalent to the RH-type positivity (no claim of proving it). Prior art: same Haynsworth
 bookkeeping as n₊(J) = 1 + n₋(W) (matching1989; r861). The NEW pieces are the positive ground state / ground-state representation and the
 Birman–Schwinger reformulation as a spectral count of an explicit "prime Laplacian".
 Locality check: D_A is nonlocal (jumps of length a and log n), while M_N is local. No pointwise Hardy weight exists (momentum1929), so any
 factorization must be nonlocal; u0 supplies exactly a nonlocal A*A. The spectral-measure factorization (Bochner) is tautological with zeros.
 Round 2 (proposed): certify (G1) at A = 1, 2 with Lehmann–Goerisch / Temple lower bounds for λ2(D_A) (interval arithmetic), and
 measure λ2(D_A) − M_N vs A. Falsification: the Beurling/ghost fakes (modified weights) must violate G1 or G2 on some window; if fakes pass
 both, the construction is blind.

## Sources (only those needed)
- Connes, Trace formula in noncommutative geometry and the zeros of ζ: https://arxiv.org/abs/math/9811068
- Berry–Keating, H = xp and the Riemann zeros (SIAM Rev. 41, 1999): https://doi.org/10.1137/S0036144598347497 (cited, not opened this run)
- Fukushima–Oshima–Takeda, Dirichlet Forms (Beurling–Deny, irreducibility ⇒ positivity improving): standard; not opened this run.
- Haynsworth inertia additivity: Linear Algebra Appl. 1 (1968) 73–81 (cited, not opened this run).

# factororbit1941 (t1941; Nov 7 2026 CST; RH not proved). fock1941.py/json, zv1941.py/json.
Recovered: pairs1904 (S_p isometries, [H,S_p]=log p S_p, no CCR); Lemma 44 §53, Lemma 45 §54 (primon Z_B=Z_F ζ(2β));
 Lemma 47 §56 (BC μ_n, unitary dilation on ℓ²(Q+*) = ⊗'ℓ²(Z)); Lemma 38 §47 (Bost–Connes); Lemma 79 §88 (n! twice, Lerch);
 ground1896 (E0 contains no f ≥ 0; ground-state transform needs u0 > 0); interactions1890 (window split, M_A).
## Orbit (sympy, unit mass): U_eff = l²/2r² − μ/r; ṙ² = 2(E−U_eff) (deficit = radial speed square); r̈ = −U_eff'.
 r_c = l²/μ, U_eff''(r_c) = μ⁴/l⁶ > 0. Ellipse μ=l=1, E=−0.3: apsides 0.6126, 2.7208; at peri r̈ = 1.685 ≠ 0;
 gravity μ/r² = 2.665 vs v²/r = 4.350 (equal only circular; at apsis gravity = v²/κ, κ = radius of curvature);
 tangential accel = 0 at apsis (radial force ⟂ velocity).
## NEW exact: M_A = −m_A(0) = −min_x m_A(x), m_A(x) = Reψ(¼+ix/2) − log π − 2Σ_{log n<A} Λ(n)n^{−1/2}cos(x log n).
 Proof: Reψ(¼+ix/2) increasing in |x| and cos ≤ 1, both extremal at x = 0 (trivial character). So
 H_A has symbol T(x) = m_A(x) − m_A(0) ≥ 0 ("kinetic", zero only at x = 0 = zero velocity) and W = P + T(D) − M_A‖F‖².
 Zero-velocity curve {m_A = 0}: A=2: x = 1.35, 2.96, 4.50, 6.02…; A=1: 3.30, 6.94…; A=3: 0.85, 1.97, 3.03…
 Positivity on E0 = window + E0 forbid enough spectral mass in the "forbidden" bands {m_A < 0} (band1923).
 Prime self-energy as truncated Bose occupation at β=½: 2Σ_{p^k<e^A} log p·p^{−k/2} = 5.852468; + (−K0) = 11.224652 = M_A.
## Prime-exponent Fock (known: primon gas, Julia/Spector; HLS Bohr lift): b_p|n⟩ = √v_p(n)|n/p⟩, b_p† = S_p√(N_p+1).
 Checks (n ≤ 3000, p ≤ 7): [b_p,b_p†] = 1 to 2e−15 away from truncation (1500–2572 boundary states defective);
 [b_p,b_q†] = 0 in deep interior; b_p†b_p = N_p; H = Σ log p N_p = log n on 7-smooth; |360⟩ = (b2†)³(b3†)²b5†|1⟩/√(3!2!1!)
 unit norm; ‖(b2†)^k|1⟩‖² = k! (k ≤ 7). Σ log p/(p²−1) = −ζ'/ζ(2) (0.56996).
 n! = Bargmann vs Szegő normalization: coherent ‖z‖² = exp(Σ p^{−2s}) (prime zeta, 1.52428 both) vs isometry vector
 Σ n^{−2s} = Π(1−p^{−2s})^{−1} (Hardy/HLS kernel ζ). Weil weights Λ(n) come from log of the Szegő kernel
 (Σ_k (zw̄)^k/k, cycle index; 1/(1−x) = exp Σ x^k/k); Fock kernel exp(zw̄) sees only k = 1 (misses n=4: 2a_4 = 0.347).
## Intertwiner: J_F c = Σ c_n T_{log n}F satisfies J S_n = T_{log n} J (HLS/Beurling dilation systems) — isometries, not
 CCR; N_p has no meaning on L²(window) (needs u ∈ log N). Shift-built squares Σ_j‖Σ_n v_{jn}T_{log n}F‖² = Tr(V G_F),
 G_F_{mn} = ⟨T_{log m}F,T_{log n}F⟩, V ⪰ 0: so D from shifts ⇔ a positive-definite decomposition of the Weil
 distribution (Bochner) — needs an independent reason for V, not supplied by CCR.

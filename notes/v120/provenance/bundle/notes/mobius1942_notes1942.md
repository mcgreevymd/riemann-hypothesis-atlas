# mobius1942 (t1942; Nov 7 2026 CST; RH not proved). mob1942.py/json (+ moment_check_wide).
Recovered: Lemma 53 §62 (Nyman–Beurling/Burnol: RH ⇔ W_ζ = H₊, restatement); Lemma 62 §71 (Spector μ=(−1)^F, Möbius
 inversion = sdim, Mertens); Lemma 45 §54; pairs1904; factororbit1941.
## ℓ²(N) (exact; checked n ≤ 4000, s = 1.3)
 Unique factorization: |n⟩ = ⊗_p |v_p(n)⟩ (occupations). μ = (−1)^{ΣN_p}·Q_sf, Q_sf = Π_p (I − P_{N_p≥2}) (0 mismatches).
 |p²⟩ is an ordinary unit vector (occupation 2); S_p² = S_{p²} (doubling exponent/energy), S_p*S_p = I (z̄z analogue).
 Z_s = Σ n^{−s}S_n, Z_s^{−1} = Σ μ(n)n^{−s}S_n = Π(I − p^{−s}S_p) (err 1e−17); Z_s^{−1}[H,Z_s] = Σ Λ(n)n^{−s}S_n
 (err 2e−17) — operator form of Λ = μ * log; this LINEAR log-derivative is what carries the Weil coefficients.
## Log line, critical filter D_p = I − p^{−1/2}T_{log p} (T_aF(u)=F(u−a))
 ev_s(T_aF) = e^{(s−½)a} ev_s(F) ⇒ ev_1(D_pF) = 0, ev_0(D_pF) = (1 − 1/p)ev_0(F); D_p* kills ev_0 (checked 1e−10).
 D_p = M⁻¹(I − T_{log p})M with M = e^{u/2} (ground-state/Doob transform by the boundary mode).
 Square cost: c‖(I − λT)F‖² with fixed off-diagonal cλ = a_n has diagonal c(1+λ²) ≥ 2a_n, equality λ = 1 (AM–GM,
 "z² vs |z|²"). Möbius-critical choice (λ = n^{−1/2}, c = Λ(n)): ΣΛ(n)(1+1/n) = 7.526 vs optimal 5.852 (A=2).
 Product filter (I−2^{−½}T₂)(I−3^{−½}T₃): D*D coefficients by ratio: 1: 2.000, 2: −0.943, 3: −0.866, 3/2: +0.408,
 6: +0.408. W has −0.490 (2), −0.634 (3), −0.347 (4), −0.720 (5), 0 at 6 and 3/2: squares create cross-prime ratios
 W lacks (and log(3/2) = 0.405 lies inside every window A > 0.405).
## Exact SOS certificate (independent of W's sign): window-invisible far ratios
 Tr(V G_F) ≥ 0 for V ⪰ 0 on monomials of primes, G_F(m,n) = g(log m/n), g = 0 for |log r| ≥ A. Match near prime-power
 coefficients, set other near ratios (p/q, pq…) to 0, leave far ratios free ⇒ −2Σa_n Re⟨F,T_{log n}F⟩ ≥ −c0‖F‖².
 One prime: c0 = a/cos(π/(K+2)) (Fejér–Egerváry; K=3 → 0.6058 = SDP) → a as K → ∞ = sharp (floor1934 A=1: 0.490).
 SDP (CLARABEL): A=1: c0 0.606 → prime floor ≥ 0.374 (Ritz 0.490); A=1.6 (2,3; 15 mons): ≥ 1.494 (Ritz 1.725);
 A=2 (2,3,5,7; 180 mons): ≥ 3.632 (Ritz 4.022). Rigorous-type lower bounds (modulo SDP tolerance), decoupled from arch.
 Unresolved: decoupled certificates sum below M_A (ghostfloor1934 shortfall ~2 at A=2); closing needs a JOINT
 certificate in which arch shifts (continuous) and E0 enter the same V.

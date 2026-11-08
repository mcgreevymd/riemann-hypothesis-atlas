# jointmatrix1944 (t1944; Nov 7 2026 CST; RH not proved). krein1944.py/json, coef_A*.npy. scan1944.py interrupted (not run to end).
Ansatz (exact, all-F): on a fixed window, E0∩L²[0,A] = L(L²-type G, supp G ⊂ [0,A]), L = ∂²−¼ (compat1907; CC21 Lemma 3):
 F = LG ⇔ ev0=ev1=0 for compactly supported F (Green's function, two conditions). So
 W(F) = (1/2π)∫ m_A(x)(x²+¼)²|Ĝ(x)|²dx, m_A = Ω − 2Σ_{log n<A}Λ(n)n^{−½}cos(x log n), cutoff exact, M_A = −m_A(0).
 Certificate: any h(x) = Σ c_k cos(a_k x), a_k ≥ A, is invisible (∫h|Ĝ|² = 0); if m_A + h/(x²+¼)² ≥ t ∀x then W ≥ t‖F‖² on
 ALL of E0∩window (whole sector, not a subset). Mixed prime/arch terms enter only through the joint pointwise inequality:
 one far kernel h serves both. By Krein's extension theorem (positive-definite functions on an interval), existence of
 such h (as a distribution) is EQUIVALENT to window positivity, so this is a reformulation with an explicit dual object,
 not an independent source of sign.
Numerical LP (HiGHS; a_k ∈ [A, A+16], K=160, |c_k| ≤ 50, x-grid [0,60], validated on 4×-range 10×-finer grid):
 A    joint t   arch-only t  prime-only t  separated sum  (min residual on validation grid)
 0.6  −0.162    −0.162       —             −0.162         (−1e−5)
 1.0  −0.509    −0.430       −0.980        −1.410         (−3e−5)
 1.6  −1.486    −0.750       −2.865        −3.615         (−0.017)
 2.0  −2.556    −0.930       −4.284        −5.213         (−0.031)
 Joint beats separated at every A (by 0.90, 2.13, 2.66): the shared far kernel captures arch/prime alignment.
 But ALL t < 0, including A = 0.6 where positivity is known (CC21, support ≤ log 2): the ansatz is too narrow
 (coefficient bound active: ℓ1 ≈ 6700–7700 ≈ bound; finite span). Negative t = failure of this ansatz, NOT evidence of
 negativity. A richer scan (K=400–800, span 40–80, C=1e4–1e5) was started and interrupted before completing.
Status: no certificate obtained; nothing rigorous (LP floats, grid validation only). Next: unbounded/weighted coefficients
 (Krein extensions typically need far kernels decaying like the Γ kernel), or a rational-function far kernel; start at A=0.6.

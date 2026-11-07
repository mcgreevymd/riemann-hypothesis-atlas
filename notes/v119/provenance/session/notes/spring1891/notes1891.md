# spring1891 — what controls spring domination (scratch; RH is not proved)
J. W. McGreevy; work by Grok Bot. Read-only atlas/STATE/lemmas. Code: spring_mp.py (exact rational overlaps + 50-digit), controls.py, polecheck.py, fig.py.
Basis: F_k = L g_k, g_k=(1−x²)^6 P_k(x) on window [−A/2,A/2] ⇒ ker P exact. Arch via Lévy springs (Fourier check 8.288429296280 vs 8.288429296283).
Bug fixed: C_kj(b) ≠ C_jk(−b) as polynomial (valid only b≥0) — computed both orientations.
Exact (cutoff-free): W(f)/‖f‖² = K(0) + ∫_0^∞ k_∞(a)(2−2ρ_f(a))da − 2Σ_n a_n ρ_f(log n), ρ_f(b)=<f,T_bf>/‖f‖² (= Weil on g=f*f̃).
 dμ/da_n = −2ρ_f(log n); δμ/δk(a) = 2−2ρ_f(a) ≥ 0; μ_min concave in (K0,k,a) (inf of affine) ⇒ positivity region convex in weights.
Galerkin K=12 (upper bounds; negatives = explicit-vector certificates):
 A=1: μ 3.86e-2; arch-only 0.246; p=2 contrib −0.217; drop 2 → +0.208.
 A=3/2: μ 1.42e-7; arch-only −0.166; drop 2 → −0.456, 3 → −0.082.
 A=2: μ 4.32e-10; arch-only −0.464; contrib 2:+0.198, 3:−0.118; drop any n≤5 → −0.22..−0.65.
 A=3: μ 1.38e-14 (μ2 8.3e-13); arch springs 5.2228 vs −K0 5.3722; contrib 2:+0.442, 3:−0.342, 5:+0.056, 4:−0.021, 7:+0.012; drops n≤13 → −0.24..−0.85.
 HF vs finite difference agree (≤1e-3 rel at A=3 near-degenerate). Free basis A=2 K=10: no pole −3.50 (one negative, r329), with pole 6.5e-14.
 Hat h=0.05 minima (A=2 1.8e-5) are not converged; smooth basis far lower; float64 = 50-digit at K≤10.

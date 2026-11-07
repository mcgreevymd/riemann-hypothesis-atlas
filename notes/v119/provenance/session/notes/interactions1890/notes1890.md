# interactions1890 — arithmetic interaction functional with Hess = W (scratch; RH is not proved)
J. W. McGreevy; work by Grok Bot. Read-only on atlas/STATE/lemmas. check1890.py (kernel from num/lemma103_weil.py).
Normalization (STATE §26 L17; NOTATION L17 table): W = P + <F,K(D)F> − Σ a_n 2Re<F,T_{log n}F>, a_n = Λ(n)n^{-1/2}, K = Reψ(¼+ir/2) − log π,
 P = 2ab (a,b = ∫F e^{∓u/2}), <F,K(D)F> = (1/2π)∫K|F̂|². Real F.
THM (exact): K(r) = K(0) + 2∫_0^∞ k_∞(a)(1−cos ra)da  [quad check to 1e-9; = atlas r341/r423]
THM (exact, window-cutoff N ≥ e^A): on supp F ⊂ window length A,
 W(F) = P(F) + ∫_0^∞ k_∞(a)‖F−T_aF‖²da + Σ_{n≤N} a_n‖F−T_{log n}F‖² − M_N‖F‖²,  M_N = −K(0) + 2Σ_{n≤N} a_n  (tails cancel exactly).
 Mediator form: W = P + K(D) + 2Σa_n − Σ a_n (I+T_n)*(I+T_n)  (Schur complement of unit-stiffness mediators y_n coupled √a_n(I+T_n)F).
Φ_N[F] = ½P(F) − ½M_N‖F‖² + ∫k_∞(a)∫U(F(u)−F(u−a))du da + Σ_{n≤N} a_n ∫U(F(u)−F(u−log n))du,  U(z)=z²/2+λz⁴/4.
 Hess Φ_N(0) = W exactly; Hess Φ_N(F0) = W + 3λ[∫k∫(ΔaF0)²(Δah)² + Σa_n∫(ΔnF0)²(Δnh)²] ≥ W, ≠ W for F0≠0.
NUM (h=0.05 hat basis, ker P ∩ window): λmin(W/L²) vs M_A: L=1 1.7e-2 vs 6.35; L=2 1.8e-5 vs 11.2; L=4 1.1e-6 vs 29.8; L=6 2.7e-7 vs 80.6.
 Relative to G0: L=1 12.6, L=2 1.3e-3, L=4 5.5e-6, L=6 2.8e-7. Basis-dependent scratch; finite windows only.
Prior art: r341 arch_levy_khintchine_sos, r423 kinetic_mass_metric, r307, r402, r321 (per-prime allocations indefinite), r861 haynsworth, r165 Maxwell.

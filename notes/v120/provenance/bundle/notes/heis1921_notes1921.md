# t1921 — Heisenberg/Tate audit + Euler-factor modulation-lattice bridge. Nov 7 2026 CST. RH not proved.
Files: checks1921.py/json, euler_resolvent.py/json, q0split.py/json. Window A=2, N=7 (≥e^A), F=LG, G=(1−u²)^8.

## 1. Audit of the pasted inference (exact checks)
- Group law: M(x1,p1,z1)M(x2,p2,z2) has z = z1+z2+x1p2 (sympy). The symmetric cocycle ½(x1p2−p1x2) holds for t=z−xp/2 (residual 0).
- SvN fixes the irreducible rep for a fixed nonzero central character; it fixes no Hamiltonian spectrum. Same rep:
  P²+X² ≥ 1 but P²−X² = YZ+ZY with Y=(X+P)/√2, Z=(P−X)/√2, [Y,Z]=i (sympy residual 0): dilation-type, spectrum all of R.
  Metaplectic covers linear symplectic, center-fixing automorphisms (not all of Aut H). Gaussian min-RS = chosen polarization.
- "Lattice-invariant admissible window": vacuous. No nonzero L² (a fortiori compact-support) function is invariant under a
  nonzero translation; E0 is not stable under modulations (below). Lattice restriction decomposes over UNITARY Bloch
  characters, while E0 lives off them (below). So the inference "SvN ⇒ no negative W eigenvalues" is false; W's sign is not
  rep-theoretic data. (Known in substance; corrected here concretely.)
- "WL" is our Weil-window form (not a Weil–Lindelöf metric).

## 2. Exact E0 geometry under Heisenberg/affine operations (log variable u; F(u)=e^{u/2}f(e^u))
ev_∓(F)=∫F e^{∓u/2}du; in the Tate additive variable ev_− = ∫f d*x (multiplicative mean), ev_+ = ∫f dx = f̂(0).
- Translations T_c (= dilations x→e^c x): ev_∓ scale by e^{±c/2} ⇒ E0 stable; the window moves. Reflection u→−u swaps ev±: stable.
- Modulations M_ξ: ev_∓(M_ξ LG) = ((∓½+iξ)²−¼)·∫G e^{(∓½+iξ)u}du = (−ξ² ∓ iξ)·Ĝ-value ≠ 0 (numeric = formula, e.g. ξ=2: −2.22497−0.96840i).
- Dilations u→λu (λ≠±1) break E0 (λ=1.3: ev = −0.04722). Fixed window: only identity, reflection (symmetric window), phases.
- Zak: ev_∓(F) = ∫_0^1 e^{∓u/2} Z_F(u, e^{∓1/2}) du, Z_F(u,z)=Σ_k F(u+k)z^k (finite sum for windows). The two boundary
  conditions are evaluations at NON-unitary Bloch multipliers |z|=e^{∓1/2}, outside what unitary lattice/SvN theory sees.

## 3. Constructive bridge (exact): W on E0 = σ-score of the adelic vacuum; primes = modulation lattice of the critical resolvent
(a) Local vacua (Weil-rep spherical vectors) under dilations, checked numerically:
  ∞: ⟨π(e^u)γ,γ⟩ = (2cosh u)^{−1/2}, Fourier = |Γ(¼+ix/2)|²/(2√π) (0.298605 both, x=1.3).
  p: ⟨π(p^k)1_{Zp},1_{Zp}⟩ = p^{−|k|/2}, Fourier series = (1−1/p)|L_p(½+ix)|² (1.480923 both).
  Scores: 2∂_σ log|Γ_R(σ+ix)|_{σ=½} = Reψ(¼+ix/2)−log π;  2∂_σ log|L_p(σ+ix)|_{σ=½} = −2Σ_k a_{p^k}cos(kx log p).
(b) Hence for F∈E0 (A, N≥e^A):  W(F) = (1/2π)∫|F̂|² m_N,  m_N = 2∂_σ log|Γ_R Z_N|(½+ix), Z_N = exp Σ_{n≤N}Λ(n)n^{−s}/log n.
  Check: spring 0.0631177 vs score 0.0630657 against terms of size M_N‖F‖² ≈ 1.09e3 (M_N=11.2247=−min m_N).
  Equivalently W(F) = d/dσ|_{½} ‖U_σF‖², U_σ = Λ_N(σ+iD)/Λ_N(½+iD), D=−i∂_u: derivative of a family of POSITIVE vacuum Grams.
  Sign not supplied: m_N(0) = −M_N < 0, so pointwise σ-monotonicity fails; only E0-averaged monotonicity could hold.
  Known analogue: for full ξ, |ξ(σ+it)| increasing on σ>½ for all t ⇔ RH (Sondow–Dumitrescu 2010, Cor. 1, opened via arXiv 1005.1104).
  (On the line ∂_σ log|ξ| = 0 off zeros; m_N is a window-equivalent smooth representative.)
(c) Euler factor = Heisenberg modulation lattice (exact Mittag-Leffler): with x_{p,m} = 2πm/log p,
  2∂_σ log|L_p(½+ix)| = log p − Σ_{m∈Z} 1/(¼+(x−x_{p,m})²)   (checked to 1e−15, p=2,3,7).
  So W(F) = arch(F) + Σ_{p≤N}[ log p·‖F‖² − Σ_m Q0(M_{−x_{p,m}}F) ],  Q0(H) = ⟨H,(¼−∂²)^{-1}H⟩ (kernel e^{−|u−v|/2}).
  Window check: per-prime direct spring vs symbol agree to 2e−9 (p=2: 23.302652; p=3: −13.416513; p=5: −0.013466).
  (Naive truncation of the m-sum has an O(1/M) Lorentzian tail; use the closed Fourier form.)
  The resolvent (¼−∂²)^{-1} is the n=0 tower mode of bulk1919; Γ_R's pole at s=0 gives the same −1/(¼+x²) term.
(d) E0 enters exactly through boundary leakage of each modulated copy (verified, q0split.json):
  Q0(H) = ∫_window(|G_H'|²+¼|G_H|²) + ½e^{−A/2}(|ev_+(H)|²+|ev_−(H)|²),  G_H = −(¼−∂²)^{-1}H.
  m=0 on E0: boundary = 0, Q0(LG) = ‖G'‖²+¼‖G‖² = 3.919150 (same for every p). ξ=2: 7.93063+2.16619 = 10.09681 ✓.
  For m≠0 the boundary energy is the explicit modulation residual |(−ξ²∓iξ)Ĝ(∓½+iξ)|²-type term.
Known vs new-to-us: (a),(b) are Tate/Weil local theory (explicit formula as log-derivative of local factors) — known.
 New to us: the window/E0 form; (c) as a modulation-lattice resolvent sum tied to the bulk1919 n=0 mode; (d) exact
 interior/boundary split with E0 residuals. Hecke check: degree of SL2(Z)diag(p,1/p)SL2(Z) = |P¹(Z/p²)| = p(p+1)
 (6,12,30) — does not produce a_p = Λ(p)/√p; the a_n arise from the σ-score, not from lattice commensurability counts.

## 4. Status / minimal missing step
Independently positive data: vacuum Grams ‖U_σF‖² (all σ), constants log p, each Q0 ≥ 0 split into bulk + boundary.
W on E0 = Σ_p log p‖F‖² + arch − Σ_{p,m}Q0(M_{x_{p,m}}F): positive minus positive; NO sign obtained.
Missing step (one inequality): on E0 windows, Σ_{p≤N}Σ_m Q0(M_{x_{p,m}}F) ≤ arch(F) + θ(N)‖F‖² — equivalently E0-averaged
 σ-monotonicity of the vacuum Gram at σ=½. This is the target restated in Heisenberg language, not proved; no
 independent source for it was found. The counterterm on E0 is identified exactly (the leakage terms), not controlled.

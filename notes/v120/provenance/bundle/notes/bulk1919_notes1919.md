# t1919 — Bulk/boundary (DtN, ground state, BF/Hardy) analogy for the spring form. Nov 7 2026 CST. RH not proved.
Conventions as spring1891/sign1918: on E0 (ev0=ev1=0, P=0), W = E_∞ + E_p − M_N‖F‖²,
 E_∞ = ∫_0^∞ k∞(a)‖F−T_aF‖²da,  E_p = Σ_{n≤N} a_n‖F−T_{log n}F‖²,  M_N = −K0 + 2Σ a_n,  K0 = ψ(¼)−log π = −5.37218.
Analogy: bulk positive energy (E_∞+E_p) vs negative boundary mass M_N; stability ⇔ BF/Hardy-type bound on the
normalizable sector E0. Subtraction/counterterms alone carry no sign; positivity must come from the bulk.

## Exact prototype 1: archimedean springs = DtN energy of a positive Kaluza–Klein tower (independent measure: Γ)
(i) ∫_0^∞ k∞(a)(2−2cos xa)da = Reψ(¼+ix/2) − ψ(¼) = Σ_{n≥0} c_n x²/(x²+d_n),  c_n = 1/(n+¼), d_n = (2n+½)².
 (series ψ(z) = −γ+Σ[1/(n+1)−1/(n+z)]; so λ=x² ↦ Σ c_n λ/(λ+d_n) is a Stieltjes / complete Bernstein function.)
 Checked (kk_tower.json): x=0.3: 1.0735863326532 all three; x=1: 3.3470372261222; x=2.5: 4.4425042660374.
(ii) Since min_w(λ|1−w|²+d|w|²) = λd/(λ+d):
 E_∞(F) = Σ_n (c_n/d_n) · min_{w_n∈H¹(R)} [ ‖(F−w_n)'‖² + d_n‖w_n‖² ],  optimal w_n = F − d_n(d_n−∂²)^{-1}F.
 A positive local bulk: tower of fields with masses² d_n = (½+2n)² — the squared distances from s=½ to the Γ poles
 s=−2n (equivalently AdS2 labels ν=2n+½, Δ± = {2n+1, −2n}). Genuinely independent of W's sign (pure Γ data).
(iii) Boundary conditions = confinement of the lowest mode (exact): (¼−∂²)^{-1}F (kernel e^{−|u−v|/2}) has compact support
 iff ∫F e^{±v/2}=0, i.e. iff F∈E0. The homogeneous solutions of the n=0 field are exactly the two boundary modes e^{±u/2}.
 On E0, F = LG (L=∂²−¼, G∈C_c): w_0 = F + G/4 (stays in the window) and the n=0 term is local:
  (c_0/d_0)·min = ‖G'‖² + 4‖F+G/4‖² = 4‖G''‖² + ‖G'‖²   (symbol 4x²(x²+¼)|Ĝ|²; sympy check n0_check.txt).
 Higher modes n≥1 still leak outside the window on E0 (their confinement would need ∫F e^{±(2n+½)v}=0, not imposed).
Status: exact identity, known ingredients (digamma partial fractions; Krein-string/complete-Bernstein extension technique,
 e.g. Kwaśnicki–Mucha 2018 — not re-opened this turn). New to us: E0 ⇔ n=0 tower confinement; the local E0 form of n=0.
 It gives positivity of E_∞ only; it says nothing about M_N, and the prime springs E_p have symbol Σa_n(2−2cos(x log n)),
 not Stieltjes/CBF — no analogous tower is constructed for them.

## Exact diagnostic 2: ground-state (Hardy) transform and why a pointwise Hardy weight cannot equal M_N
Ground-state representation (standard; cf. Frank–Lieb–Seiringer 2008 for jump kernels): for symmetric J≥0, ψ>0, F=ψv,
 ½∫∫J|F(x)−F(y)|² = ∫(Lψ/ψ)|F|² + ½∫∫J(x,y)ψ(x)ψ(y)|v(x)−v(y)|²,  Lψ(x)=∫J(x,y)(ψ(x)−ψ(y))dy.
 (Algebra: |ψxvx−ψyvy|² = ψxψy|vx−vy|² + (ψx−ψy)(ψx|vx|²−ψy|vy|²); verified by expansion.)
 Translation-invariant springs + ψ=e^{cu}: Lψ/ψ = −2∫w(a)(cosh(ca)−1)da < 0 (no help); for k∞, c=½ it diverges
 (k∞(a)e^{a/2}→1): the boundary modes are exactly critical for the archimedean kernel.
No-go (exact given Test2): a Hardy certificate E_N(F) ≥ ∫V|F|² on window functions with ∫V|F|² ≥ M_N‖F‖² on E0
 forces V ≥ M_N a.e. (localize F at a point, remove the two moments by a correction of relative size O(√ε)), hence
 E_N − M_N ≥ 0 on ALL window functions — contradicted by Test2 (night1916): E_N − M_N = W − P has eigenvalue
 −1.5237 (A=1), −3.2803 (A=2) on the free K=8 basis. So no multiplicative (pointwise) Hardy weight, from any ψ, can be M_N;
 the certificate must be E0-dependent (boundary flux / nonlocal remainder), as in BF where the boundary term
 vanishes only for normalizable falloffs. Rewriting E_N−M_N = Q_+ + R with R vanishing on E0 is equivalent to the target
 (Finsler/Schur complement) — counterterm freedom, no sign.

## Analogy map (structural only)
RS/Gram positivity ↔ positivity of a bulk Gram form (tower fields are the "operators"; Gram of (F, w_n) is ≥0).
Bulk/boundary DtN ↔ prototype 1 (exact for E_∞). Two falloffs ↔ e^{±u/2} = homogeneous solutions of the n=0 field
 (exact), NOT a CFT: boundary data here are 2 numbers, not an infinite-dimensional operator algebra; Tate is not a CFT.
BF/Hardy ↔ need "gradient ≥ negative mass" on E0; diagnostic 2 shows it cannot be pointwise.

## Open / hoped-for arithmetic property
Wanted: an arithmetic bulk extension of the PRIME springs (e.g. on the multiplicative semigroup, using Euler factors as
 the independent measure) whose DtN energy is E_p, together with a boundary-flux identity in which the mass M_N appears
 only as a term controlled on E0 (i.e. a non-pointwise Hardy inequality whose remainder vanishes exactly under ev0=ev1=0).
 Not constructed; no sign source for M_N obtained. Not done: any test of this (deliberately; no open-ended runs).

# synthesis1953 (t1953; Nov 7 2026 ~4:40 PM CST; RH NOT proved). Scratch only; no repo/push/Page.
Files: proto1953.py/json (24-boson/Petersson toy, ξ Euclidean slice, qubit Bogoliubov), xi_sigma_check.txt, k0_weight.txt.

## Reviewed (read this turn)
rs1901 (RS template; L103 pure Gaussian ⇔ compatible J), heis1921 (W(F)=∂_σ‖U_σF‖²|½, σ-score of vacuum Grams), sampling1923, kepler1925,
oscillator1927, factororbit1941 (M_A=−m_A(0)), pqr1947 (Var L0=(E4−E2²)/12), transv1949, jacobian1950; STATE: L124 §135 (RH ⇔ Φ Lee–Yang;
Fisher vs LY), §1825 (anomaly = 1/area), line 2825 (Poincaré–Lelong), bernoulli1945 (E0 ≈ cuspidal), ferromagnetic_phi pin.
"Bernoulli 19": no source in notes/STATE; B_19 = 0. Not guessed. (Nearby facts: B_18 num 43867 irregular @18; 691 irregular @12,200.)

## New exact facts (this turn)
T1 (toy theorem, proved): Φ(y)=−log(y^6Δ(iy)). Φ(1/y)=Φ(y); Φ'(y)=2πE2*(iy); Φ''=(π²/3)(E4−E2²)+6/y² >0 (Var>0 + curvature).
   ⇒ sign E2*(iy)=sign(y−1). Uncorrected E2 vanishes at y0=0.5235217 (not self-dual). Numerics: duality resid 4e−17.
T2 Hessian split (numeric FD = formula to 1e−8): Hess Φ at iy = diag(−V, V+6/y²), V=(π²/3)(E4−E2²).
   J-invariant part = (3/y²)·I (Petersson curvature, k/4y²·... with k=12); J-anti part traceless diag(−(V+3/y²), V+3/y²): signature (1,1).
   J = Cauchy–Riemann rotation = Wick rotation (β ↔ real time): Euclidean +Var, Lorentzian −Var.
T3 radial score R=Re(2πiτE2*) <0 at 36/36 grid points of F outside |τ|=1, =0 on |τ|=1 (NUMERICAL off-axis; proved on axis).
T4 ξ Euclidean slice: ξ(½+x)=∫_R Φ_RP(u)cosh(xu)du, Φ_RP>0 ⇒ log ξ(½+x) is a CGF, convex; κ2=0.046210 = ∫u²Φ/∫Φ (both computed).
T5 counter-check: at t=γ1, ∂_σ log|ξ| = 20.0 > 0 but ∂²_σ = −399.9 (σ=.55): σ-convexity fails at on-line zeros even under RH.
   ⇒ the transferable mechanism is first-order (score/Herglotz), not Hessian convexity; T1's convexity needs a ZERO-FREE potential.
T6 counterterm = Euclidean-slice score defect (exact from known formulas): M_A = −2 (log Γ_R Z_N)'(½) on real σ; full ξ has 0 there by FE.
T7 weight check: 2(ψ(k/2)−log2π) (archimedean counterterm, weight k) vs k/12 (toy vacuum/curvature): 12: −0.2635 vs 1 — not equal ⇒ counterterm ≠ curvature naively.
T8 Bogoliubov: qubit p=1/5, KM 0.8656 ≤ symmetrized 1 (log mean ≤ arith mean).
Calibration: Δ has full positive geometry (Petersson, curvature, self-adjoint Hecke, Deligne local RH) yet GRH for L(Δ,s) open ⇒ positive geometry on the parameter/moduli space is not enough; needs the product/correspondence space (ATLAS D8).

## Candidates (ranked) and next test: see chat answer.

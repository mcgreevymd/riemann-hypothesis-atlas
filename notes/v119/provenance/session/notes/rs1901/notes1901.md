# rs1901 — Robertson–Schrödinger loop-back: ambient positive state vs signed E0 fluctuations (t1901, synthesis; RH not proved)
Read-only; builds on scan1885, paired1888, ground1896, geometry1897. Prior art: L103 two-point THM (g=ReH, ω=ImH, J=i; positivity ⇔ RH = restatement), L103 Q1 (pure Gaussian ⇔ compatible J; mixed ⇒ g ≥ g_J, J non-unique; ghosts admit no invariant state).

## Template (template1901.py, verified)
K=R^{2n}, fixed σ, compatible J (σ(J·,J·)=σ), g=σ(·,J·)>0. Φ: K→operators, [Φ(x),Φ(y)]=iħσ(x,y).
w(x,y)=φ(Φ(x)Φ(y)) = V(x,y)+(iħ/2)σ(x,y) ≥ 0 on K_C  (RS). Pure quasifree: V=(ħ/2)g, rank w = n (null space = J-antiholomorphic), symplectic eigs = ħ/2.
Mixed V=1.5V: RS holds, full rank, J not determined. Complex doubling of a Hermitian h≥0 gives J=i free -> RS restatement.
RS threshold: given (V,σ), RS ⇔ ħ ≤ ħ*(V,σ)=2ν_min (Williamson). scan1885 ħ*(L) decays 1.5e-2 → 5.2e-7 (L=1..6, basis-dependent): falsifies that fixed (σ,ħ) normalization, not W.

## Readings of W
(i) W as covariance: W = V = Re w for an INDEPENDENT positive state φ ⇒ W ≥ 0 on E0. Needs φ, Φ computed from primes/Γ/poles, equality exact.
(ii) W as stiffness: Gibbs e^{-βH}, H=½W: needs W>0 to be normalizable (presupposes the sign). Classical V=β^{-1}W^{-1}; quantum V=(ħ/2)coth(βħν/2) per Williamson mode.
Real vs complex: on real E0 (F=F^♯ sector) W real symmetric = Re part; skew part must be an independent σ. Existing Q0, D are operators, not automatic σ axes.

## Requirements for a positive arithmetic state
*-algebra A (e.g. scaling convolution algebra / adele-class crossed product), observable map Φ:E0→A, adjoint law Φ(F)*=Φ(F^♯) (arith. adjoint), state φ positive by construction (vector/density state, not GNS of W),
φ(Φ(F)*Φ(G)) = W(F,G) exactly on E0. Faithfulness: null vectors ↔ ker W; GNS quotient fine if ker trivial. Must fail for DH (no Euler product).
Nearest source: CC21 Tr(ϑ(g)Sϑ(g)*) (archimedean, inequality, small support).

## Ampleness analogy
Abelian varieties (Appell–Humbert / Riemann relations): H>0 Hermitian with E=Im H integral on lattice Λ ⇔ ample line bundle; prequantization [ω/2πħ]∈H²(Z).
Pure Gaussian = positive compatible metric only; ample = that + lattice integrality. Arithmetic lattice is absent (analogy only).

## Next tasks (not launched)
1 arithmetic adjoint law Φ(F)* for scaling/Frobenius observables; 2 independent 2-point Gram on low windows vs W; 3 DH exclusion test for any candidate φ.

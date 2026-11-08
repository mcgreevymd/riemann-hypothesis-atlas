# localization1970 (t1970; Nov 7 2026 ~9:30 PM CST; RH NOT proved). Scratch. loc1970.py, orient1970.py/json, ledger1970.py/json.
## 0. Dictionary repair (exact)
 Unitary picture: L^2(C_S)^ur ≅ L^2(R,du) (u = log|g|), V(f)=convolution, standard star f^*(u)=conj f(-u); phi := f*f^* is
 positive type (phi^ = |f^|^2) and V(phi)=V(f)V(f)^* >= 0.  Connes' non-unitary U(h) on L^2(X_S): h = chi*phi, chi(u)=e^{-u/2}.
 chi is a convolution automorphism but (chi g)^* = chi^{-1} g^*, hence h = g * g^#, g = chi f, g^#(u) = e^{-u} conj g(-u) (TWISTED star),
 NOT g*g^*. classes1966 "I_S(h1,h2)=tau_S(h1*h2^*)" is wrong as stated; correct: I_S(f1,f2) = tau_S(chi (f1*f2^*)).
 (Numbers in classes1966 used h=e^{-s/2} r(s), i.e. the correct h, and stand.)
## 1. Explicit semilocal model (derived: Tate local FE + Mellin-Plancherel on E_S image; not quoted from Connes)
 xi^(y) := ∫xi(u)e^{-iyu}du = Z_S(f,1/2-iy) for xi = E_S f.  Fourier on A_S becomes  F_S = M_c J,  (Jxi)(u)=xi(-u),
   c_S(y) = prod_{v in S} L_v(1/2-iy)/L_v(1/2+iy),  L_inf=Gamma_R, L_2=(1-2^{-s})^{-1};  |c|=1, c(y)c(-y)=1 => F_S^2=1.
 P_Λ = 1_{u<=L}, L=log Λ;  Phat_Λ = F P F = M_c H M_cbar, H = 1_{u>=-L};  S_Λ = 1_{|u|<=L};  Connes R_Λ = Phat P.
 Semilocal Poisson defect: J F_S = M_{cbar}; globally (formal) c = Λ(1/2-iy)/Λ(1/2+iy) = 1 (FE) => F = J (Poisson (22)).
 EXACT phase identity: -i d/dy log c_S(y) = -m_S(y), m_S = Re psi(1/4+iy/2) - log pi - 2 sum_{p in S,k} log p p^{-k/2} cos(k y log p).
   The W symbol is (minus) the Wigner time delay of the semilocal Fourier scattering phase.
## 2. Validation (numerical; grid h=.025/.0175, L=8/12, box margin 20)
 tau_num = Tr(R_Λ V(phi)) - Tr(S_Λ V(phi)) vs -(W-P) (symbol, all powers of p in S):
  A=1, S={inf,2}: sin8 -0.69762 vs -0.69761; poly6 -0.41337 vs -0.41335; skew -0.53728 vs -0.53727.
  A=0.6, S={inf}: -1.21111 vs -1.21111;  S={inf,2}: -1.21112 vs -1.21111.  (Connes Thm VII.4 reproduced incl. Gamma, 2, diagonal.)
  Wrong orientation (Phat = M_cbar H M_c) flips the sign: model is orientation-sensitive => convention check passed.
 Spring ledger H_A - M_A||F||^2 = W on same tests: diff <= 8e-6 (ledger1970.json). Window: supp F ⊂ [0,A], A=1 ∈ (log2,log3);
  log4 > 1 so only n=2 enters W; A=0.6 < log2: arch only.
## 3. Candidate Q_Λ = S_Λ Phat_Λ S_Λ (no threshold, no W input; cutoffs = Connes' own)
 Positivity (algebraic): S - Q = S(1-Phat)S >= 0, V(phi) >= 0 => D_Λ := Tr((S-Q)V(phi)) >= 0. Counterterm Tr(S V(phi)) = 2L phi(0) (paired).
 Results (L-stable 1e-6, h-stable 1e-5):         D        W(=W-P on E0)   residual W-D
  A=1 {inf,2} sin8                               0.87903   0.69761          -0.18142   FAIL (D > W)
  A=1 {inf,2} poly6                              0.67476   0.41335          -0.26140   FAIL
  A=1 {inf,2} skew                               0.76105   0.53727          -0.22378   FAIL
  A=0.6 {inf} sin8 (arch control)                1.20368   1.21111          +0.00744
  A=0.6 {inf,2} sin8 (2 invisible to W)          1.31797   1.21111          -0.10686   D depends on S, W does not.
 Semiclassical: D ≈ ∫ m_+ |F^|^2/2pi (0.920, 0.703, 0.795, 1.212, 1.356).
## 4. Exact obstruction (operator order)
 With U=M_c (commutes with V), K = U H U^* - H: Connes' finite part = Tr(K V) = -(W-P). Split by H:
   W - P = D_c - D_cbar - X,   D_c = Tr(H U(1-H)U^* H V) = D (forward leakage, >=0),
   D_cbar = Tr((1-H)U H U^*(1-H) V) = Tr(H M_cbar (1-H) M_c H V) (by J-symmetry; = deficit of the inversion-conjugate projection, >=0),
   X = 2 Re Tr(H U H U^* (1-H) V)  (edge-straddling, from nonlocality of V).
 Numerics: D_cbar = 0.19457, 0.25492, 0.22871, 0.00762, 0.11506; X = D - D_cbar - (W-P) = -0.0131, +0.0065, -0.0049, -0.0150, -0.0083.
 Semiclassically D_c ≈ ∫m_+, D_cbar ≈ ∫m_- : a single positive compression sees only positive time delay; the negative
 delay (K0 and the low-frequency -2a_2 cos) is a SECOND positive deficit entering with a minus sign. Linear trace (Connes) vs
 quadratic deficits (HS norms of Hankel-type operators) is the order-structure obstruction.
## 5. Missing estimate (precise; equivalent to W >= 0 on E0∩window, no gain claimed)
   D_cbar(f) + X(f) <= D_c(f)   for f = (d^2-1/4)G, supp G ⊂ [0,A]:  backward leakage of c_S across the edge is dominated by
   forward leakage. Both sides are explicit, W-free functionals of c_S = Γ_R and 2-adic ratio.
## Relation to R26/R27: those tested Sonin-space lower bounds (W - Tr(ϑΠϑ*)); this is the Connes pair (P,Phat) with a positive
 symmetric compression Q=SPhatS and an exact two-Hankel decomposition — different object; same conclusion type (no free sign).

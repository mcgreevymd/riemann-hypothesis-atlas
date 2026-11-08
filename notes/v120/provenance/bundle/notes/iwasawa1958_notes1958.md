# iwasawa1958 (t1958; Nov 7 2026 ~6:40 PM CST; RH/BSD not proved). iw1958.py, out1958.txt (sympy, exact, p=3).
Prior: STATE §10 Lemma 4 (Iwasawa pillar, 691/37 numerics), §46 Rem 7.6 (p-adic: no positivity), §47 Lemma 38 (Gamma in compact
Galois factor; "Iwasawa generator = p-adic rapidity" corrected).
## Exact toy facts (e_n = v_p|X/omega_n X|, omega_n=(1+T)^{p^n}-1)
 Lambda/(p): e_n=p^n (mu=1), Delta e_n=(p-1)p^n.   Lambda/(T-a): e_n=n+v_p(a): lambda=1, nu=v_p(a).
 T-3 and T+3 (roots +-p): IDENTICAL e_n -> growth sees only root valuation, not position/sign.  T-9: nu shifts by 1.
 Lambda/(T^2-3), Lambda/(T^2-27): both lambda=2 (Delta=2), nu differ (1 vs 3).
 Adding finite F_p (pseudo-null): nu+1, mu,lambda unchanged -> nu depends on more than char series.
## Regularity bridge (exact): Lambda=Z_p[[T]] regular local, dim 2, m=(p,T), dim m/m^2=2.
 Lambda/(f) regular <=> f not in m^2 <=> class of f in m/m^2 ("gradient" (f(0)/p, f'(0)) mod p) nonzero.
 T-3 (2,1) reg; T^2-3 (2,0) reg (Eisenstein, Z_3[sqrt3]); T^2-27 (0,0) SINGULAR = arithmetic cusp T^2=p^3 (cf y^2=x^3);
 3T, T^2, 9: singular/nonreduced. Same (mu,lambda) can be regular or singular: invariants != Jacobian rank.
## Verdict: partial yes (discrete growth/slopes, Newton polygon, regularity of base); no sign, no ample class from (mu,lambda,nu).

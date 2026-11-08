# covariance1956 (t1956; Nov 7 2026 ~6:30 PM CST; RH NOT proved). cov1956.py/json, out1956.txt. Scratch only.
Read: synthesis1953, ghostfloor1934, jointmatrix1944, mobius1942, heis1921 (resolvent bridge already known: (1/4-d^2)^-1 positive, subtracted).
Window A=2 (n=2,3,4,5,7), MA=11.22465, K0=-5.37218. Trials F=LG, L=d^2-1/4: G=(u(A-u))^6 (F in C^3, compact) and G=sin^8(pi u/A).
## Candidate: independent product of local stationary Gaussian fields (one per place), built from local factors only
 prime p: AR(1) on lattice (log p)Z, correlation rho_p=p^{-1/2} (= geometric/bosonic KMS state at beta=1/2:
   P(N_p>=k)=p^{-k/2}), covariance P_p = sum_k p^{-|k|/2} T_{k log p} >= 0 (Poisson kernel), level log p.
 arch: Ornstein-Uhlenbeck tower, rates lambda_j = 2j+1/2 (= distance from s=1/2 to the poles s=-2j of Gamma_R), kernels e^{-lambda_j|a|}.
## EXACT ledger (identities; numerically checked)
 W_p(F) = log p (||F||^2 - <F,P_p F>)  [white minus colored, equal marginal variance] = -2 sum_k a_{p^k} Re<F,T_{k log p}F>.
   a_{p^k} = log p * P(N_p >= k) (tail prob. of critical boson). Diagonal cancels internally: no prime "M_A" needed.
 W_arch = (-gamma - log pi)||F||^2 + sum_j [ ||F||^2/(j+1) - <F, OU_{lambda_j} F> ]  (= E_inf + K0||F||^2).
 Diagonal subtraction re-read as MEANS (first cumulants), not covariances:
   -K0 = -2 E_inf[log|x|], x ~ e^{-pi x^2}|x|^{1/2}d*x (Tate Gaussian at critical tilt): -2.686091692 = K0/2 (checked 1e-8).
   2 sum_{p^k<e^A} a = 2 E_p[min(L_p, cap_p(A))], L_p = -log|x|_p, cap = largest multiple of log p below A (checked to 1e-15).
   => M_A = -2 sum_v E_v[log|x|_v^{(A)}]: twice the expected product-formula defect of the independent local product state.
 Per prime: PSD-completion deficit of (white - AR) = sup symbol gap = 2 log p/(sqrt p - 1) = 2E_p[L_p] (uncapped) = spring diagonal.
## Numerical (A=2, not certified): three ledgers agree
  poly: W_spring 3.55e-4, Fourier 3.45e-4, covariance 5.8e-4 (||F||^2=66.6; W/||F||^2 ~ 5e-6: near-extremal trial)
        places: arch -15.972, p=2 +29.972, p=3 -13.712, p=5 -0.287, p=7 ~0. Massive cancellation; per-place indefinite.
  sin8: W 0.1788 (all three), arch +0.090, p=2 +9.092, p=3 -9.001, p=5 -0.0016.
## E0 test (exact + numerical)
 E0 <=> the rate-1/2 OU response of F is window-supported: OU_{1/2}F = -G (rel err 3e-8; outside leak 7e-12). [known: heis1921]
 NEW: per-prime AR response leaks outside the window (0.23-0.58 of max|F|) on E0; leak = e^{-u/2}/log p * sum_{m!=0} ghat(2 pi m/log p)
   e^{2 pi i m u/log p}, g=e^{u/2}F (Poisson summation; matches to 1e-7). E0 kills only m=0 (=ev_+): the SHARED pole s=1;
   the local poles s=1+2 pi i m/log p remain per prime (they cancel only globally: zeta has no other poles on Re s=1).
## g/J audit (exact)
 Every K_v is translation-invariant => Hilbert transform J commutes with all K_v, J^2=-1, g-orthogonal: compatible J exists for
 free whenever g>=0 -- but J does not preserve compact support or E0 (Fhat(+-i/2)=0 not preserved by -i sgn x). So no
 translation-invariant J on the window/E0 sector: J must be non-stationary (window-adapted). Ordinary covariance vs BKM moot: commuting (classical Gaussian) fields.
## Verdict
 Matches: every Lambda(n)/sqrt n (as AR(1) correlations), Gamma kernel (OU tower), diagonal (as marginal variance/means), log pi & gamma
 (as Tate Gaussian mean). Mismatch: sign. Covariances enter SUBTRACTED (W = white - colored); positivity on E0 is a covariance UPPER
 bound (contraction/Bessel type), opposite to weight-12 calibration (Var + curvature both +). Not a sign mechanism; RH-equivalent.

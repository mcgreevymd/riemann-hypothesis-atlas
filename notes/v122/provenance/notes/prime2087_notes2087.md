# t2087: can the PRIME block of W be a zeros-blind intersection of algebraic correspondences?
Nov 9 2026 (CST). Scratch only. No Atlas/repo/Page edits. RH NOT proved. Phi NOT constructed. No Hodge-type sign theorem.
Labels: [THM]=classical theorem, cited; [DER]=derived here (elementary); [NUM]=checked in prime2087.py (prime2087.json).

## 0. Conventions (from inertia2057.py, cutoff2072)
W = P + H_A - M_A||F||^2 = Q + P (inertia2057: W = Q + B J B^T). Prime atoms enter Q (hence W) with MINUS:
  col -= a_n [hat(u - log n) + hat(u + log n)],  a_n = Lambda(n)/sqrt n,  i.e. W ⊃ - sum_n a_n [g(log n)+g(-log n)], g = F*F~.
C± = ∫F e^{±u/2}, P = C+ conj C- + C- conj C+. W = +sum_rho ghat(gamma_rho). t2072 ledger: fixed-point trace = P - W, prime atoms +sum a_n there.

## 1. Function-field template (X/F_q, genus g; Gamma_k := graph of Frob^k, Gamma_{-k} = transpose, Gamma_0 = Delta)
- f1 = {pt}xX, f2 = Xx{pt}: Gamma_k.f1 = 1, Gamma_k.f2 = q^k, f1.f2 = 1, f_i^2 = 0. [THM]
- Gamma_k.Delta = N_k = #X(F_{q^k}); each fixed point multiplicity 1 (d Frob = 0 => transversal). [THM]
- Gamma_k.Gamma_l = q^{min(k,l)} N_{|k-l|} (projection formula; (1xF^l)^*Gamma_k = q^l Gamma_{k-l}, F^l purely inseparable). [THM]
- Phi_ff(c) := sum_k c_k q^{-k/2} Gamma_k.  [DER]
  * Phi.f1 = sum c_k q^{-k/2} = C_-,  Phi.f2 = sum c_k q^{k/2} = C_+   (u = k log q; C± are literally the BIDEGREE of Phi).
  * Trivial-lattice part of Phi.Phi' = C+ C'- + C- C'+ = P_ff.  E0 = {bidegree 0} = Phi^{-1}(primitive).
  * q^{-(k+l)/2} Gamma_k.Gamma_l = q^{-|k-l|/2} N_{|k-l|}: Toeplitz. The weight w_k with w_k w_l q^{min(k,l)} = f(k-l) is forced to be
    w_k = const * q^{-k/2}. The half-density is FORCED by translation invariance, not inserted.
  * Full: Phi.Phi' = P_ff - W_ff;  primitive: Phi^0.Phi'^0 = -W_ff, W_ff(m) = (q^{m/2}+q^{-m/2}) - N_m q^{-m/2} = sum_i beta_i^m.
  * Prime block: N_m = sum_{d|m} d a_d (a_d = #closed points of degree d). In the u-measure du = log q dk:
      log q * N_m * q^{-m/2} = sum_{v, j: Nv^j = q^m} log Nv * (Nv^j)^{-1/2}  = exact Lambda_ff(n)/sqrt(n) at u = log n.
    The log q is the Jacobian of k -> u (one common time unit), the deg v is an intersection count. [DER]
  * SIGN: prime block +N_m q^{-m/2} in the intersection, -N_m q^{-m/2} in W_ff. Same as t2072 ledger (+ in trace, - in W). MATCH.
  * Castelnuovo–Severi / Hodge index [THM, Weil 1948]: primitive Gram NSD => W_ff Toeplitz >= 0 => |beta_i| = 1.
  [NUM] y^2=x^3+x+1/F5 (N=9,27,108,675), y^2=x^5+2x+1/F3 (N=7,15,19,83,232,795; brute force, zeros-blind; checked against
  the genus-2 L-polynomial, |alpha| = sqrt3): Toeplitz identity residual <3e-15; Gram NSD; rank = 2g.
  Dictionary consequence: in the template I = P - W is the FULL intersection, -W the primitive one, H ~ f1+f2.

## 2. Hecke correspondences on X_0(N) x X_0(N), (n,N)=1
- T_n bidegree (sigma1(n), sigma1(n)). Lefschetz: T_n.Delta = 2 sigma1(n) - Tr(T_n | H^1(X_0(N))) for n non-square [THM; Hurwitz 1885
  fixed-point count; Eichler–Selberg is the TRACE-formula form]. Fixed points = CM points (Hurwitz class numbers) + cusps.
  [NUM] Kronecker–Hurwitz on X(1): sum_t H(4n - t^2) = 2 sigma1(n) - sum_{d|n} min(d, n/d), all n < 60 (H(0) = -1/12).
- Frobenius-type combination Phi_{p^k} := T_{p^k} - p T_{p^{k-2}} (Eichler–Shimura: T_p ≡ F + V mod p, so Phi_{p^k} ≡ F^k + V^k) [THM].
  [NUM/DER] bidegree exactly 1 + p^k; cusp contribution exactly 2 for every k (p = 2,3,5,7; k <= 5).
  Normalized by p^{-k/2} (inserted: sqrt of bidegree is sqrt(1+p^k), NOT p^{k/2}; p^{k/2} is deg F^k from Eichler–Shimura):
    trivial lattice: 2(p^{k/2} + p^{-k/2})  = P-type term of zeta(s)zeta(s-1) (Eisenstein), finite rank;
    primitive: -sum_f (alpha_f^k + beta_f^k) p^{-k/2} = prime block of L(f,s) for weight-2 newforms.
- With log p inserted, the primitive part is the prime block of L(f,s): its zeros, NOT zeta's. CIRCULARITY/WRONG-TARGET FLAG:
  the Hodge-index (primitive) sector of a modular-curve square only carries cusp forms. zeta appears only in the rank-2 trivial lattice
  and at the cusp (the cusp count 2 x p^{-k/2} has the shape of the zeta atom, but log p must be inserted and it has no primitive content).
  zeta's zeros live in the continuous Eisenstein spectrum (scattering term of Selberg's TRACE formula), not in any intersection here.

## 3. Arakelov: P^1_Z x P^1_Z, Mobius graphs Gamma_n: w = n z, Green currents of t2078
- g_n - g_1 = -log|f_n|^2 with f_n = (w1 z0 - n w0 z1)/(w1 z0 - w0 z1). Hence hat Gamma_n = hat Delta + div^(f_n) EXACTLY. [DER]
  Gillet–Soulé: div^(f) = 0 in CH^1 [THM] => every arithmetic intersection number of hat Gamma_n is INDEPENDENT of n.
  Explicitly: finite part = vertical components Delta_{F_l}, l | n-1: 2 log(n-1); archimedean (1/2)(-4 log(n-1)) = -2 log(n-1);
  total 0 by the product formula. [NUM n<40, residual 9e-16]. No log p, no Lambda(n). (t2078's log heights are exactly the
  archimedean half of a principal divisor.)
- CH^1(P^1_Z x P^1_Z)_R = R^2 (bidegree) + R (constants): 3-dimensional, i.e. finite rank again; cannot host infinitely many
  independent prime atoms log p.
- Power map w = z^p: fixed points 0, inf, mu_{p-1}; disc(z^p - z) = ±(p-1)^{p-1}; transversal mod p; no log p. [DER]
- The only canonical source of log p: deg^(Spec F_p) = log p. Then
    Lambda(p^k)/p^{k/2} = deg^(Spec F_p) * #Fix(Frob_p^k on Spec F_p) * (#F_{p^k})^{-1/2}
  exactly, zeros-blind — but it is a sum over 0-dimensional fibers (Euler product), not a pairing of correspondences on one surface,
  and a point has no H^1: zero Hodge content. Spec Z x_{F1} Spec Z is not available; the needed global object is a single family of
  correspondences Psi(lambda), lambda in R_+^*, whose restriction "over p" at lambda = p^k is Frob_p^k with fixed locus of degree log p.
  The only existing candidate is the Connes–Consani square of the arithmetic site (Psi(lambda), composition Psi(l)Psi(l') = Psi(ll'),
  tangential correction when ll' in Q; periodic orbits C_p of length log p in the scaling site). No intersection theory exists there yet.

## 4. Sign check
Template: prime block + in intersection, - in W; t2072: + in trace, - in W. MATCH. Hecke: same sign, but for L(f,s). Arakelov P^1_Z: n/a (zero).

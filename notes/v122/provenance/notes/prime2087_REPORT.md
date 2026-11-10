# t2087 REPORT: prime block as a zeros-blind intersection (scratch)
Verdict: (c) for the number-field geometries actually available, with a sharp template result.
1. Function field [THM+DER, NUM]: Phi_ff(c) = sum c_k q^{-k/2} Gamma_{Frob^k}. Bidegree(Phi) = (C_-, C_+); trivial-lattice part = P;
   Gram is Toeplitz and the half-density q^{-k/2} is FORCED by that; full pairing = P - W_ff, primitive = -W_ff; prime block
   = Gamma_k.Delta (genuine transversal intersection) giving exactly Lambda_ff(n)/sqrt n (log q = Jacobian of k -> u); sign matches
   the t2072 ledger; Hodge index => W_ff >= 0. Verified numerically on genus 1 and genus 2 point counts.
2. Hecke on X_0(N)^2 [THM, NUM]: T_n.Delta = 2 sigma1(n) - Tr(T_n|H^1) (Hurwitz count; Eichler–Selberg is the trace form).
   Phi_{p^k} = T_{p^k} - p T_{p^{k-2}} has bidegree 1 + p^k and cusp count 2 for all k. Primitive part = prime block of L(f,s),
   not zeta (wrong target). zeta only in the rank-2 trivial lattice and cusp; log p and p^{-k/2} must be inserted. FAIL for zeta.
3. Arakelov P^1_Z x P^1_Z [DER, THM]: hat Gamma_n = hat Delta + div^(f_n) exactly; arithmetic intersections independent of n;
   finite 2 log(n-1) cancels archimedean -2 log(n-1). CH^1_R is 3-dim. Power map: no log p. FAIL.
   Only canonical log p: deg^(Spec F_p); prime atom = fiberwise Lefschetz count x log p x (#F_{p^k})^{-1/2}: exact but an Euler-product
   sum over points, no surface, no Hodge content.
Implication for Phi (derived requirements from the template): the target must (R1) give Gamma_u bidegree (1, e^u) for real u so that
C± are the two degrees and E0 = primitive; (R2) satisfy Gamma_l.Gamma_m = min(l,m)(Gamma_{l/m}.Delta) so that e^{-u/2} is forced;
(R3) have Gamma_{p^k}.Delta contain a multiplicity-1 component of Arakelov degree log p over p only, NOT killed by rational
equivalence (so Gamma_n not rationally equivalent to Delta; infinite-rank NS); (R4) primitive sector carrying zeta, not cusp forms.
Ruled out: P^1_Z x P^1_Z (arithmetic), modular-curve squares / Hecke algebra, power-map graphs. Ruled in only as candidate (untested,
no intersection theory yet): Connes–Consani square of the arithmetic/scaling site with Psi(lambda).
Phi not constructed; no sign; nothing on RH. Files: notes2087.md, prime2087.py, prime2087.json.

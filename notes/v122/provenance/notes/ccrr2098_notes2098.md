# t2098 notes — Connes–Consani-type h^1 on the square (SCRATCH ONLY; nothing pushed)
Focus question: can a CC-style h^1 on the scaling-site square carry the Hodge-type sign independently of W?

## 1. CC definitions used (quoted; local copies cc2205.pdf/.txt, cc1603.pdf/.txt)
[CC23] Connes–Consani, "Riemann-Roch for Spec Z-bar", arXiv:2205.01391v2, Bull. Sci. Math. 187 (2023).
- Divisor D = sum_j a_j{p_j} + a{inf}, a_j in Z, a in R. O(D) = {(a_v) in A_Q : |a_v|_v <= exp(D)(v)} (compact, adelic), arch. factor [-e^a, e^a] encoded as ||HR||_{e^a}.
- psi : HQ x HO(D) -> HA_Q, psi(q,a)=q+a (eq. 1.2/2.3). H^0(D) = ker psi = ||HZ||_{e^a} after linear equivalence (Prop 2.2(i)); H^1(D) = coker psi = (HA_Q, R) tolerant S[±1]-module, R_k = {(x,y): x-y in Im psi} (Prop 2.2(ii)).
- dim_{S[±1]} = minimal number of generators over coefficients {-1,0,1} with the bound sum|alpha f| <= e^a (Def A.2).
- dim H^0 = ceil(log(2n+1)/log 3), n = floor(e^a) (eq 1.3, Prop 3.3); for deg D >= -log2: = ceil((deg D+log2)/log3) - 1_L(deg D) (Thm 3.4), L exceptional set, |L|=1.14099...
- dim H^1(a{inf}) = dim U(1)_lambda, lambda=e^deg D: = ceil((-log lambda - log2)/log3) if lambda<1/2, else 0 (Prop 4.1).
- RR (Thm 1.1/4.3): dim H^0(D) - dim H^1(D) = ceil'((deg D + log 2)/log 3) - 1_L, ceil' = odd extension of ceiling. Serre duality (Thm 1.2): H^0(K-D) ≅ Hom(H^1(D), U(1)_{1/4}), K = -2{2}.
- NB: dim is integer-valued and is essentially log_3 of a cardinality (a covering count). It is one-dimensional; no surface theory in the paper.
[CC17] Connes–Consani, "Geometry of the scaling site", arXiv:1603.03191, Selecta Math. 23 (2017).
- C_p = R_+^*/p^Z with sheaf O_p of convex PL periodic functions, slopes in H_p = Z[1/p] (Lemma 5.1); affine structure is in lambda (not log lambda).
- Divisor at point H = lambda H_p has order D(H) in H itself; deg D = sum_H D(H) in R (Prop 5.4) — real degrees.
- Div(C_p)/P ≅ R x Z/(p-1)Z via (deg, chi) (Thm 5.6). So Pic^0(C_p) is FINITE.
- Arithmetic Frobenius Fr^a_mu (mu in R_+^*): D=sum(H_j,h_j) -> sum(mu H_j, mu h_j); multiplies degree by mu (Lemma 5.7). Relative Frobenius Fr^r_h (h in H_p^+ mod p^Z ≅ N^x_(p)) preserves degree (Lemma 5.8).
- Filtration H^0(D)^rho = {f : ||f||_p <= rho}; Dim_R H^0(D) := lim_n p^{-n} dim_top(H^0(D)^{p^n}) (eq 28, Lebesgue covering dim).
- RR (Thm 5.17): deg D >= 0 => Dim_R H^0(D) = deg D; Dim_R H^0(D) - Dim_R H^0(-D) = deg D. (genus-1 shape; no H^1 defined — H^0(-D) plays its role.)
- Positive for TAA: Lemma 5.7 gives a genuine, non-inserted source of bidegree (1, mu) for Psi(mu) (graph of Fr^a_mu) — consistent with R1.

## 2. Corrections to the dreamer's reduction (t2096u)
- h^2(nD) = h^0(K - nD). D.H = 0 does NOT make K - nD non-effective (K.H > 0 for g>=2). Standard fix (Hartshorne V.1.8–1.9): replace H by H' = D + mH or choose sign of n. For g = 1 (K = 0) it is fine.
- The non-effectivity "h^0(nD)=0 on E0" is only meaningful with a nontrivial linear equivalence; with too few principal divisors (R3) it is vacuous and all weight sits on RR.
- D_eps^2 = D^2 + 2 eps^2 (not minus) — t2096 arithmetic slip.

## 3. Classical target (function field, C x C over F_q) — [THM, NUM]
D = sum c_k Gamma_k, Gamma_k.Gamma_l = q^min (q^|k-l| + 1 - sum beta^|k-l| q^{|k-l|/2}), bidegree (sum c, sum c q^k).
On primitive D: K.D = (2g-2)(C_- + C_+) = 0, so chi(nD) = (1/2) D^2 n^2 + (1-g)^2 EXACTLY, and D^2 = -W_ff(F,F), F_k = c_k q^{k/2}.
Genus 1 (y^2=x^3+x+1/F5, N=9,27,108): h^0=h^2=0, h^1(nD) = deg(n psi) = n^2 deg psi with psi = sum c_k phi^k in End(E),
deg psi = Norm(sum c_k alpha^k). Numbers: c=(5,-6,1,0): D^2=-810, W=810, deg psi=405=W/2. c=(30,-31,0,1): 9315 = W/2. c=(65,-68,1,2): 44955 = W/2.
Genus 2 (y^2=x^5+2x+1/F3, N=7,15,19): D^2 = -378, -4254 = -W exactly; chi(nD) = -189 n^2 + 1, -2127 n^2 + 1.
MECHANISM of the n^2: Leray along pi_1. Fiber restriction of nD has degree 0; the class map x -> [O(nD)|F_x] in Pic^0(fiber) = Jac has degree
n^2 * (positive quadratic form); h^1 counts the jumping fibers (g=1: #ker(n psi)). The sign comes from deg >= 0 of an isogeny-type map
= Rosati positivity. NOTE: this is exactly the Jacobian/Rosati route already CLOSED as a stand-in under the Phi locks; classical, no new content.

## 4. CC23 adelic model, product (Künneth-Cartesian) — [NUM]
Box [-N,N]^2 with coordinatewise bounds (product S-module, CC23 §2): brute-force minimal generating sets:
N=1:2, N=2:4, N=3:4, N=4:4 = exactly dim1+dim1 (1D dims 1,2,2,2 match eq. 1.3). dim is log-cardinality => ADDITIVE.
chi_cart(n(F1+F2)) = 4,6,10,16,32,60 for n=1,2,4,8,16,32 (≈ 2n/log 3, linear), vs (1/2)D^2 n^2 = n^2. Quadratic coefficient 0.
Getting n^2 needs dim(A ⊗ B) = dim A · dim B, i.e. a tensor product over a base over which H^0's are "vector spaces" with
log-cardinality multiplicative. Over Z: Q ⊗ Q = Q, Z ⊗ Z = Z — the arithmetic square collapses on functions; over S, pi_0(HZ ∧_S HZ) = Z
(higher homotopy torsion). Postulating multiplicativity = inserting F1.F2 = 1 by hand (COOKED).
Correspondences: no graph-type divisor exists in CC23 (no square at all); O(Psi(mu)) not definable there.

## 5. Scaling-site square C_p x C_p — [DER, NUM]
- Psi(mu) := graph of Fr^a_mu: support = radial line lambda2 = mu lambda1. Cartier (corner locus of max(m lambda2, n lambda1) with slopes in H_p)
  ONLY for mu = n/m in Q_{>0}; irrational mu (= e^u generic) is not a CC divisor. Real weights 1/m needed for bidegree (1,mu).
- Radial lines on (R_+^*)^2/(p^Z)^2 are disjoint unless mu/mu' in p^Z (then coincide; that is R3's excess). So Gram off-diagonal = 0.
  Example p=3, mu={1,2,4}, primitive F=(0.392,-0.832,0.392): W needs off-diagonal k_inf(log2)=0.943, k_inf(log4)=0.533 AND p=2 prime atoms;
  C_3 x C_3 gives 0 for all. Single-orbit square sees one prime only and no k_inf.
- Leray along pi_1 with CC's Dim_R: fiber divisor of nD has degree n*C_- = 0; CC Thm 5.17(i) and Lemma 5.13 => Dim_R H^0 = Dim_R H^0(-.) = 0
  on every fiber, every n. Pic^0(C_p)=Z/(p-1)Z finite (Thm 5.6) => fiber-class map locally constant => no jumping-fiber count.
  Quadratic coefficient from the lift = 0 identically. (Also: the multiplicity of Psi at a CC point is an element of H=lambda H_p, so
  "multiplicity 1 on every fiber" is not canonical — a choice; either natural choice gives degree 0 on primitive D.)

## 6. Verdict: (b), sharpened
What works: CC's Fr^a_mu supplies bidegree (1,mu) honestly (R1 support). Product classes on C_p x C_p are fine tropically.
What is missing, exactly:
 (M1) an H^1 at all on C_p (CC17 has only H^0(D), H^0(-D)); CC23's H^1 is for Spec Z-bar, 1-dimensional, log-cardinality dim.
 (M2) a dimension that is multiplicative under products (CC23 dim is additive => no n^2 even for F1+F2).
 (M3) a continuous Pic^0 of the fiber (the classical n^2 = degree of fiber-class map into Jac); CC: Pic^0(C_p) finite. Supplying a
      Jacobian is the closed Jacobian/Rosati stand-in route.
 (M4) a square carrying all primes and inf simultaneously ([0,inf) x| N^x squared) with Psi(mu) Cartier for real mu; C_p x C_p sees one prime,
      rational mu only, no k_inf.
Not (a): no W-independent n^2 coefficient was obtained. Not (c) per se: no circular definition was written; the only way to get n^2 is to
postulate it (= cooked). No Phi, no Hodge sign, nothing on RH.

# counterterm1995: a geometric counterpart of the diagonal counterterm K0
Nov 8 2026 (CST). Scratch only. No repo, manuscript, or submission edits. No RH proof, no new sign theorem.
Labels: [EXACT] proved/computed here in closed form; [THM] cited; [NUM] mpmath/scipy, uncertified; [ANALOGY]; [CONJ].
Scripts: connes_arch1995.py(.json), connes_arch_fft1995.py(.json), maass1995.py(.json), det_scale1995.py(.json).

## 0. Ledger conventions (re-verified, not assumed)
W = P + B_A, B_A = H_A - M_A||F||^2, M_A = -K0 + 2 sum_{log n<A} Lambda(n)/sqrt n, K0 = psi(1/4) - log pi = -5.37218341922567.
Archimedean ledger term for even g, with K(u) = 2e^{-u/2}/(1-e^{-2u}) = e^{u/2}/sinh u:
  W_inf(g) = K0 g(0) + int_0^inf K(u)(g(0)-g(u)) du                                 [EXACT; NUM 5e-13, connes_arch_fft]
  FP_H int_0^inf K = -psi(1/4) - gamma - log 2 = pi/2 + 2 log 2 = 2.95709068791...    [EXACT, new closed form; NUM 1e-16]
  -K0 = (gamma + log 2pi) + FP_H int K = gamma + log 8pi + pi/2                       [EXACT; this confirms matching1989 l.65]

## 1. Chosen object: Connes' phase-space-cutoff trace of the scaling action (independently specified)
Source: Connes, Selecta Math. 5 (1999) 29-106, arXiv math/9811068 (Thm 3 local, Thm 4 semilocal, eqs (10)-(12)).
Object: R_Lambda = Phat_Lambda P_Lambda on L^2(K), with Phat defined by the Fourier transform for an additive character alpha.
  Tr(R_Lambda U(h)) = 2h(1) log'Lambda + int' h(u^{-1})/|1-u| d*u + o(1).                                               [THM]
  int' = the unique extension of rho^{-1}du/|1-u| whose alpha-Fourier transform vanishes at 1.
Here the u=1 identity fixed point is not transverse when h(1) != 0 (Connes Sec. V). The 2 log'Lambda divergence plus the finite
delta_1 coefficient form the excess-intersection contribution. This object is defined by an operator trace, not by the target.

Computation over R, with alpha = e^{-2pi i x}, self-dual dx, and the symmetric map h(x) = |x|^{-1/2} g(log|x|):
 (a) Independent route (Connes eq. (31)): F := lim[Tr - 2h(1)log Lambda] = -int ghat(u) log|u| du, with g(l) = h(1/(l+1))/|l+1|.
     Evaluated by FFT, F agrees with -W_inf(g) to 9e-4 and 6e-4 for two Gaussian widths; the residual is quadrature at the log singularity.   [NUM]
 (b) Distribution form: int'_R = 1/2 Pf_1 int g(l) dl/|l| + (gamma + log 2pi) g(0) gives exactly -W_inf(g), with error 5e-13.
     Dropping the constant misses by -2.41509 = -(gamma + log 2pi).                                                     [EXACT+NUM]
     (Fourier transform of Pf_1(1/|x|) at y is -2gamma - 2log 2pi - 2log|y|, so the FT-vanishing condition at y=1 forces gamma + log 2pi.)
     The map a=+1/2 instead of -1/2 breaks the s <-> 1-s symmetry and misses by 0.164. So the critical normalization sigma=1/2 is
     forced by the symmetric map.
 (c) p-adic places, unramified alpha_p (the standard global character of Q): int' over units is 0, from Connes eq. (10) with f_v=0.
     So the p-adic diagonal vanishes. The off-diagonal orbits p^m give log p * p^{-m/2} at u = +-m log p, i.e. exactly Lambda(n)/sqrt n.   [THM]
 RESULT [EXACT given THM]:  Tr_ren := sum_{v in S} int'_v = -(W - P) restricted to the window = M_A g(0) - H_A(g).
 Reading the counterterm in degree (Laplacian) form, i.e. Laplacian = degree - adjacency on the weighted "spring graph" on R:
   M_A = [alpha constant gamma + log 2pi] + [Hadamard mass of the transverse archimedean kernel, pi/2 + 2log2]
         + [mass of the transverse p-adic atoms, 2 sum Lambda(n)/sqrt n].
 So M_A is the total alpha-normalized mass (degree) of the Connes-Weil Lefschetz distribution.
 The prime part of M_A has NO local diagonal: it comes only from rewriting the off-diagonal fixed points in degree form.

## 2. Cutoff/scheme cocycles and what fixes K0 (correction to matching1989 Sec. 5)
 - Lambda -> lambda Lambda: shift 2h(1) log lambda in the divergent term only; int' is unchanged.                       [EXACT]
 - Hadamard eps -> eps/lambda: FP shifts by -log lambda and the delta coefficient by +log lambda; only this pair moves.
   The Laplacian form int K(g(0)-g) is convergent and scale-free.                                                     [EXACT]
   ==> CORRECTION: matching1989 l.66-67 ("NF delta_0 coefficient is an RG-family") is true for the Hadamard split only.
   Given Connes' int', the Laplacian-form delta_0 coefficient K0 is a single scheme-free number.
 - Character alpha -> alpha(a.) at place v: int'_v shifts by log|a|_v h(1) (FT vanishing moves from 1 to a).             [EXACT]
   For a in Q^*, the product formula gives zero total shift, so sum_v diag_v is invariant.
   Example: a = 2 moves log 2 of diagonal from infinity to the 2-adic place (whose conductor becomes nontrivial).       [EXACT]
 - Equivalent determinant form [EXACT; NUM 1e-30]: det_zeta((s+2n)/c)^{-1} = 2^{-1/2} Gamma_R(s) at c = 2pi, and
   K0 = -2 d/ds log det_zeta((s-Theta)/2pi)|_{s=1/2}. The scale cocycle c -> c' shifts K0 by -log(c'/2pi), checked for c = 1, pi, 4pi.
   The 2pi is the same 2pi as in alpha. Sources: Deninger, Invent. Math. 104 (1991) 245-261; 107 (1992) 135-150
   (https://eudml.org/doc/143961).
 ANSWER [EXACT]: the residual scalar K0 is fixed by a geometrically forced datum, the adelic character class
 (alpha trivial on Q, unique up to Q^*). That is the analogue of deg K_C forcing Delta^2 in the function-field case.
 What remains [ANALOGY, not a theorem]: calling it a SELF-INTERSECTION. In function fields, Delta^2 = 2-2g = log|d|/log q-type term
 (Connes eq. (12), Hartshorne V) is a global intersection number. For Q, |d| = 1, so the global "differental idele" term is 0, and the
 whole invariant is the archimedean local constant. Exact obstruction: the number-field counterterm is local-archimedean, not log|d|.

## 3. Secondary object: modular cusp (Maass-Selberg / Selberg trace formula), sigma=1 vs critical
Sources:
 - Iwaniec, Spectral Methods of Automorphic Forms, Ch. 10.
 - The parabolic term in the form of arXiv:1108.5659 eq. (2.130) (k=1, c=0): P(h) = -g(0)log2 - (1/2pi) int psi(1+ir)h(r)dr + h(0)/4.
 Checks:
 - -phi'/phi(1/2+it) = -2log pi + 2Re psi(1/2+it) + 4Re zeta'/zeta(1+2it), error 4e-31 at four values of t.                 [NUM]
 - -phi'/phi(1/2) = 2(gamma - log 4pi) = -3.90762.                                                                       [NUM]
 - phi(1/2) = -1.                                                                                                       [NUM]
 Continuous term, degree form [EXACT; NUM error < 1e-15 after the correction below]:
   (1/4pi) int h (-phi'/phi) = (psi(1/2) - log pi) g(0) + int_0^inf e^{-x/2}/(1-e^{-x}) (g(0)-g(x)) dx
                               - 2 sum Lambda(n)/n g(2 log n) + h(0)/2.
   The h(0)/2 is the zeta(1) pole: a boundary-value delta at r=0, i.e. a P-type pole term, not diagonal.
   CORRECTION: my earlier summary omitted this term. The numerical residual was exactly h(0)/2 for both widths.
 sigma-shift identity [EXACT]: with G(u) = g(2u), the non-h(0) part equals W_loc(e^{-|u|/2} G). This is a non-unitary shift:
   primes Lambda/n at 2 log n vs Lambda/sqrt n at log n; kernel 1/sinh u vs e^{u/2}/sinh u.
 Diagonal constants (degree form), each as -[alpha const] - FP_H int kernel:
   sigma=1/2 (Weil):         K0       = psi(1/4) - log pi = -(gamma + log 2pi) - (pi/2 + 2log2) = -5.37218
   sigma=1 (scattering):     K0^(1)   = psi(1/2) - log pi = -(gamma + log 2pi) - log 2          = -3.10824
   parabolic:                         gamma - log 2 = -0.11593, kernel e^{-x}/(1-e^{-x}), FP_H = 0
   P - Cont (T-free pair):            2gamma + log 2pi = 2.99231, combined kernel 1/(e^{x/2}-1); NUM error 8e-18
 K0 - K0^(1) = psi(1/4) - psi(1/2) = -pi/2 - log 2 exactly (duplication -log 2, reflection -pi/2).                    [EXACT]
 Scheme: the Maass-Selberg 2 log T and the truncated parabolic orbital integral g(0) log T cancel in the trace formula.
   The SAME T is forced on both sides, so only the pair P - Cont is canonical. y -> lambda y shifts each piece by log lambda g(0).
 Degree growth: M^(1)_A = 2A + log 4pi - gamma + o(1) (Mertens) is log-type, matching 2 log T.
   The critical M_A ~ 4 e^{A/2} is exponential.                                                                       [EXACT]
 Mismatch mechanism [EXACT]: phi(s) = xi(2s-1)/xi(2s) samples xi at two points one unit apart, so no s makes both critical.
   At s = 1/4, -phi'/phi = 2xi'/xi(3/2) (since xi'(1/2) = 0); its archimedean part is psi(3/4) - log pi = K0 + pi.
   The SL2(Z) cusp therefore cannot output K0. It outputs K0^(1), K0 + pi, or 2gamma + log 2pi, depending on sigma.
   For Gamma0(N)/Fricke, the constants change by log N-type terms (not computed).

## 4. Matching table
| piece | ledger (critical) | Connes adelic trace (Sec. 1) | SL2(Z) cusp (Sec. 3) |
|---|---|---|---|
| P (C+, C-) | 2Re C+ conj C- | poles h-hat(0), h-hat(1): outside int' [THM] | h(0)/4, h(0)/2 pole terms (zeta(1)) [EXACT] |
| Gamma | Re psi(1/4+ix/2) - log pi | int'_R, alpha = e^{-2pi ix}: EXACT match (5e-13) | psi(1/2+ir): sigma=1 shift [EXACT mismatch] |
| primes | Lambda(n)/sqrt n at log n | p^m orbits, same weights [THM] | Lambda(n)/n at 2 log n |
| subtraction M_A | -K0 + 2 sum Lambda/sqrt n | total alpha-normalized mass: EXACT | 2A + log 4pi - gamma (log-type) |
| diagonal const | K0 | forced by character class: EXACT | K0^(1) = K0 + pi/2 + log 2; pair 2gamma + log 2pi |
| status | - | computed + cited, no sign | computed, mismatched, no sign |

## 5. The "B(h,h) < 0" complement criterion: independence and index assumptions
Bordered inertia [EXACT]: suppose h has B(h,h) < 0 and B(h,.) lies in span(C+,C-). Then B >= 0 on h^{perp_B} iff n_-(B) = 1. It needs:
 (i) h specified independently of B. Choosing h = B^{-1}c is tautological.
 (ii) The B-orthogonal complement, not the L^2 one.
 (iii) n_-(B) finite on the window. This holds after Galerkin, but full W has infinite rank.
Modular case: <Eis,Eis> is undefined. Its renormalized value 2 log T - phi'/phi has a T-dependent, hence scheme-dependent, sign,
and the truncated norm is >= 0. So no intrinsic negative vector comes from the cusp.

## 6. Function-field prototype (kept; not recomputed)
Delta^2 = 2-2g; the FF M_L = Delta^2 + 2 sum q^{-k/2} N_k has the same degree form as Sec. 1.
matching1989 brute-forced this for g=2 over F_3. It shows no sign can be read off the diagonal (g=0 gives +2, g=2 gives -2, and both are positive-definite).

## 7. Kept from boundary1994 (unchanged)
- W = H^1_c = H^1(G, G_inf; V), dimension 3. delta(1) = X^10 - 1 is boundary, not Eisenstein.
- p10 = i Lambda(f,1), p0 = -i Lambda(f,11); S swaps them; the odd sector gives P = -2|p10|^2.
- C+ / C- are the invariant/coinvariant boundary functionals. One cusp gives one independent moment.
- H_c vs H duality D(delta1, psi) = 6 res psi. Eis_1 denominator 691.
Sec. 3 here is the analytic (Maass) side of the same cusp. It is sigma=1 data and is not identified with the critical Gamma term.

## 8. Next compatibility theorem (concrete)
(C1995) "Degree-form Lefschetz identity on windows": for S_A = {inf} ∪ {p < e^A} and F in D(I_A),
  lim_Lambda [Tr(R_Lambda U(F*F~)) - 2||F||^2 log'Lambda] = M_A||F||^2 - H_A(F)        (= -(W - P), the Sec. 1 identity),
  where M_A = sum_v (alpha-normalized local mass), invariant under alpha -> alpha(a.) for a in Q^*.
  Status: provable from Connes Thm 4 plus Sec. 1. Window compatibility holds because the new places p >= e^A do not meet the support.
Sign theorem it would feed [CONJ; RH-equivalent, NOT proved]:
  on E0 ∩ D(I_A), the regularized adjacency of the spring graph is bounded by the total mass M_A.
  Equivalently, in matching1989 Sec. 7, n_+(J_I) = 1, with deficit exactly M_A.
  This is a Hodge-index statement. The diagonal supplies only its calibration, never its sign.
Plausible geometric normalization, not imposed: read -K0 as -2 d/ds log det_inf((s-Theta)/2pi) at s=1/2, the archimedean "self-intersection"
of Deninger's Frobenius flow, with the scale 2pi tied to the character class.
Proving that this is an intersection number on an actual space is open.

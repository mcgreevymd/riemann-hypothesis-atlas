# matching1983 — can an independently specified h satisfy B(h,F) = kappa*C(F) for all window F?
Labels: [EXACT] hand-derived, checked numerically; [NUM] double precision, uncertified but refinement-stable; [DERIVED-SKETCH] argument outlined, not written out in full; [CONJ] heuristic/conjectural.

## Setup (same conventions as moment1975)
Window = [-A/2, A/2] (centered, total width A), zero extension, L^2(window) with the usual mass; C(F)=∫F cosh(u/2), S(F)=∫F sinh(u/2).
B = W - P = H_A - M_A||F||^2 (valid off E0); all prime powers with log n < A; M_A = -K0 + 2Σ Λ(n)n^{-1/2}; K0 = psi(1/4) - log pi; k(a)=e^{-a/2}/(1-e^{-2a}).
Weak response: B(h,F) = ∫ r_h F, r_h(v) = ∫_0^∞ k(a)[2h(v)-h(v+a)-h(v-a)]da + Σ a_n[2h(v)-h(v+log n)-h(v-log n)] - M_A h(v). Finite paired Gamma integrand; no separate infinities.
Identity B(h,·)=kappa C(·) on the window  <=>  r_h = kappa cosh(v/2) a.e. on the window (h even => sinh part is automatic).
Exact arch split for h1=cosh·1_win [EXACT]: r = cosh(v/2)[Jc(d+)+Jc(d-)] - sinh(v/2)[Js(d+)-Js(d-)] + primes - M_A h,
  d± = A/2 ∓ v, Jc(d)=∫_0^d k(1-cosh(a/2)) + ∫_d^∞ k, Js(d)=∫_0^d k sinh(a/2). All are real-analytic for d>0.
The trivial representer h* = B^{-1}cosh satisfies the identity by definition. It is NOT an independent construction and is used only as a reference.

## Candidates (specified before computing B; no tuning)
h1 = cosh(u/2)·1_win (the windowed kernel vector of ∂²-1/4).
h2 = (cosh(u/2) - cosh(A/4))·1_win: the Dirichlet boundary-value solution of (∂²-1/4)h = cosh(A/4)/4, with h(±A/2)=0.

## Results
1. h1 fails [EXACT]: k(a) ~ 1/(2a) gives ∫_d^∞ k ~ (1/2)log(1/d), so r/cosh -> +∞ at both edges while finite at the center.
   [NUM] r/cosh at the edge rises by 0.689 to 0.691 each time d drops 4×; (1/2)ln 4 = 0.693.
   Least-squares residual: 37.9% (A=0.6), 19.1% (A=1.0). Explicit E0 tests F=(∂²-1/4)G with G=(1-t²)²t^k (moments ~1e-12):
   B(h1,F) = 9.13 and 3.62 (A=0.6); 3.21 and 3.00 (A=1.0). Response and matrix routes agree to ≤0.6% (jump-limited).
2. h2 removes the edge logarithm but still fails.
   A=0.6 (arch only) [NUM]: residual 6.92% (stable to 1e-7 for N=60/120/240); E0 tests B(h2,F)=0.009385 and 0.008732,
     routes agree to ~2e-10. Robust nonzero => identity false (uncertified).
   A=1.0 (prime 2) [EXACT]: the prime term -a_2 h2(v±log 2) moves h2's edge kink to the interior points v0=±(log2 - A/2)=±0.193,
     so r_h2 has derivative jump a_2 sinh(A/4)/2 = 0.06191 there. The arch part and kappa·cosh are smooth there, so the identity is impossible.
     [NUM] finite-difference jump 0.06172 (eps=1e-3), 0.06189 (eps=1e-4). Residual 3.0%; E0 tests 0.00847 and 0.00994.
3. Structural consequence [DERIVED-SKETCH]: the arch symbol ~ log|x| is elliptic at high frequency, so any exact representer
   must have interior singularities equal to the prime-translated edge singularities: {±(A/2 - log n)} ∩ window, then iterated
   while inside. A representer built only from moment, Gamma and boundary data (smooth inside) cannot work once log 2 < A.
   Window edges (truncation) and adelic places (shifts by log p) are different objects. The identity couples them: each place p carries the window edge inward by log p.
   Expected edge behavior of h*: h* -> 0 like ~2·kappa·cosh(A/4)/log(1/d), the only way a log-order operator gives a bounded nonzero edge response [CONJ, heuristic].

## Mapping vs orthogonality
Even an independent h with B(h,·)=kappa·C, B(h,h)<0, and n_-(B_even)=1 would only give the quadratic-form shape of the Hodge index pattern on the window
(ample-like vector plus B-orthogonal complement E0). With moment1975, B>=0 on E0_A <=> n_-(B_e)<=1 & q_e<=0, and the count condition is the fragile one (λ2 -> 0).
A geometric map would also need, all absent: an integral/rational lattice, a real (1,1)/primitive identification via a Hodge structure (J),
and a map Φ: E0 -> H^{1,1}_prim with -I(ΦF,ΦF)=W(F) defined independently of W. Orthogonality is necessary, not constructive.

## Sharp next question
Is h*_A = B_A^{-1}cosh equal to cosh(u/2) minus a finite, prime-indexed sum of edge-layer profiles located on the edge orbit
{±A/2 ∓ Σ log n_i}, with one universal Gamma-determined layer profile? If such an "edge-orbit ansatz" can be written independently and gives zero residual,
it is the first independent candidate for the class. Its orbit structure is a concrete arithmetic object to compare with a geometric correspondence.

## Files
match1983.py / match1983.json / match.txt — h1, h2 responses, residuals, two-route E0 tests. kink1983.py / kink1983.json — prime-kink check.
mom1975.py — shared matrix code (copied from ../moment1975). No zeros, sqrt W, spectral clipping, or tuning used.

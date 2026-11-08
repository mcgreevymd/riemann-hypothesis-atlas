# moment1975 — do the two exponential moments control the dangerous directions of the actual bulk form?
Status labels: [HAND-EXACT] algebra checked by hand; [THEOREM] standard result, cited not reproved; [NUM] double-precision, uncertified.

## Setup [HAND-EXACT]
- Window: centered, support width A: F in L^2[-A/2,A/2], extended by zero (translation-invariance of B makes centering WLOG; prime lags log n < A, all prime powers included).
- B(F) = H_A - M_A||F||^2 = (1/2pi)∫ m(x)|F^(x)|^2 dx,  m(x) = Re psi(1/4+ix/2) - log pi - 2 Σ_{log n<A} Λ(n)n^{-1/2} cos(x log n);
  M_A = -K0 + 2Σ a_n, K0 = psi(1/4) - log pi. Valid for ALL window F (off E0 too). Full W = B + P, P = 2 ev+ ev-, ev± = ∫F e^{±u/2}.
- C = ∫F cosh(u/2), S = ∫F sinh(u/2): ev± = C ± S, so P = 2(C^2 - S^2). Reflection J commutes with B and P.
  => even sector: W_e = B_e + 2 c c^T (rank-one POSITIVE); odd: W_o = B_o - 2 s s^T (rank-one NEGATIVE).
  => E0_A = (even ∩ cosh⊥) ⊕ (odd ∩ sinh⊥): each sector carries exactly ONE constraint.
  => P vanishes on ker ev+ alone: B = W on ker ev+ (one moment already kills P; second moment is extra codimension).
- Domain: window space closed in L^2; moment functionals bounded (cosh,sinh in L^2) so E0_A is closed codim 2 in L^2(window) [HAND-EXACT] (unlike global E0, dense). [UNPROVED SKETCH — publication: restrict all spectral statements to the computed Galerkin matrices] m >= min m and m ~ log|x| suggest the compressed operator is self-adjoint, bounded below, with compact resolvent/discrete spectrum; not proved or cited here. Re psi(1/4+iy) increasing in y>=0 (termwise from series) [HAND-EXACT].

## Exact criterion (bordered inertia / Haynsworth) [THEOREM + HAND-EXACT specialization]
For one sector with constraint vector c, B invertible, q := <c, B^{-1} c>:
  n_-(B|c⊥) = n_-(B) - 1 + [q > 0],  n_0(B|c⊥) = [q = 0].
Hence (finite-dim, B invertible, c≠0)  B >= 0 on c⊥  <=>  n_-(B) = 0 (then q>0 automatically), or ( n_-(B) = 1 and q <= 0 ).  n_-(B) >= 2 => failure regardless of c. Proof: matching1983/PUBLICATION_AUDIT.md Lemma 1. Infinite-dim use requires invertibility/domain assumptions not verified here.
Spectral form: q = Σ_k <c,v_k>^2/λ_k ; with λ_1<0<λ_2: condition is ρ := Σ_{k>=2} c_k^2/λ_k  /  (c_1^2/|λ_1|) <= 1.
Constrained minimum μ solves the secular equation Σ c_k^2/(λ_k-μ)=0, μ in (λ_1, λ_2]: margin is CAPPED by λ_2(B_e).
E0_A bulk positivity (Galerkin, sector blocks invertible) <=> [even: n_-(B_e)=0, or n_-(B_e)=1 & q_e<=0] AND [odd: n_-(B_o)=0, or n_-(B_o)=1 & q_o<=0]. The odd condition is separate and necessary.
Separate job (full W on whole window, not E0): Sherman–Morrison inertia gives
  assuming n_-(B_e)=1 and B_e invertible: W_e>=0 <=> q_e <= -1/2 ;  assuming B_o positive definite: W_o>=0 <=> q_o <= +1/2.   (Strictly stronger than E0 job.)
Single moment (B invertible, reflection-commuting): B>=0 on ker ev+ <=> n_-(B)=0, or n_-(B)=1 & q_e+q_o <= 0 (rows add since e^{u/2}=cosh+sinh, sectors orthogonal).

## Numbers [NUM] (mom1975.json, diag1975.json, lower1975.json)
A=0.6 (no primes), A=1.0 (p=2 only), A=2.0 (2,3,4,5,7). Sine basis J=24/40/64 (orthonormal mass), plus independent
E0 encoding F=(d^2-1/4)G, G=(1-t^2)^2 t^k (moments ~1e-13: exact E0). Lower bound: m>=m_lb for |x|>X =>
B >= m_lb||F||^2 - <F,K_X F> on E0_A, λmax(PK_XP) by Nystrom (X up to 1500).
| A | λ1(B_e) | λ2(B_e) | λ1(B_o) | align(c,v1) | ρ_e | q_e | q_o | E0 min bracket | full W min |
| 0.6 | -1.114 | 0.732 | 0.235 | 0.970 | 0.037 | -0.5039 | 0.0165 | [0.6918, 0.6920] | 0.008 |
| 1.0 | -1.977(≥-1.988) | 0.0132-0.0136 | 0.0198 | 0.991 | 0.016 | -0.5000004 | 0.4947 | [0.01182, 0.01197] | ~1.0e-6 |
| 2.0 | -4.28 | ~1e-15 | ~1e-15 | 0.997 | 0.007 | -0.5 | 0.5 | UNRESOLVED (LG Ritz 1e-11..1e-7 >0; sine ±1e-14) | ±1e-14 |
No moment: negative (−1.11, −1.98, −4.28). C+ only = C− only (exact reflection symmetry): 0.226, 2.2e-4, ±1e-14. Both: as bracket.
Even constraint (cosh) does all the sign work; odd sector is already positive at A=0.6,1.0 (sinh constraint inert for sign).
A=2.0: eigenvalues of size 1e-15 = near-null cluster; double precision cannot decide sign; hypothesis "B invertible, n_-=1" unverifiable there.

## Non-arithmetic controls (A=1.0 unless noted) [NUM]; NOT counterexamples to anything
- Moment weight e^{±αu}: two-moment min ~flat (0.0136→0.0131 over α∈[0.3,0.8]); capped by λ2(B_e)=0.01362 which is α-independent.
  Single moment: positive for α<=0.5 (2.2e-4 at α=1/2), negative for α>=0.55. Exact α=1/2 matters only in the single-moment
  problem, because there B coincides with full W (P vanishes) and full W is near-singular (q_e = -1/2 - 4e-7).
- Prime-2 spring scaled by λ (consistently in H and M): E0 min 0.184, 0.104, 0.032, 0.0136, −0.0055, −0.085, −0.19 for
  λ=0,0.5,0.9,1,1.1,1.5,2. Failure at λ≈1.07 is by λ2(B_e) crossing 0 (n_-(B_e)=2) — a COUNT failure, not misalignment (ρ stays ~0.01).
  For λ<=0.5 B_o gets a negative mode and sinh constraint becomes active (q_o<0, so still fine).
  Full W fails for every λ≠1 tried (both sides) — confirms full-W and E0-bulk are different jobs.
- Counterterm: shifting K0 by δ shifts B by δ||F||^2 exactly, so E0 min = admissible increase of M_A: ~0.69 (A=0.6), ~0.0118 (A=1.0, 0.19% of M_A).

## Verdict
- Moments do control the FIRST dangerous direction: B_e's negative mode is 97–99.7% the cosh representer, residual coupling ρ<=0.04, so q_e<=0 holds with large slack. Mechanism is not mysterious: B_e = W_e − 2cc^T.
- They do nothing for the SECOND danger: λ2(B_e) (and λ1(B_o)) shrink toward 0 as A grows (0.73 → 0.013 → ~1e-15). That is where E0-bulk positivity actually lives, and a 7% boost of the prime-2 spring already flips it at A=1.
- Missing inequality (no proof claimed): for every A>0,  n_-(B_A^even) <= 1 and B_A^odd|_{sinh⊥} >= 0, i.e. λ2(B_A^even) >= 0 in the window. Moment alignment (q_e<=0) is the easy half.
- Rigour: A=0.6 and A=1.0 brackets are numeric; lower-bound scheme is rigorizable (interval Nystrom + quadrature tail bounds), not done.


## Publication audit note (added 2026-11-07, 10:25 PM CST)
Criteria corrected to include the index-0 case. See ../matching1983/PUBLICATION_AUDIT.md for proofs and domain caveats. Raw data unchanged.

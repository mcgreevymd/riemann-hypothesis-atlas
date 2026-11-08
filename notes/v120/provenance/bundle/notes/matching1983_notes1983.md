# matching1983 — two explicit candidate representers for B(h,F) = kappa*C(F) (CORRECTED for publication, 2026-11-07, 10:25 PM CST)
Superseded first draft kept verbatim in notes1983_raw_superseded.md (do not cite it). Proofs and caveats are in PUBLICATION_AUDIT.md.
Labels: [EXACT] proved here under the stated hypotheses; [NUM] double precision, uncertified, refinement-stable; [CONJ] conjecture/heuristic, no proof.

## Setup
Window [-A/2,A/2] (centered, total width A), zero extension. B = W - P = H_A - M_A||F||^2, with all prime powers log n < A,
M_A = -K0 + 2ΣΛ(n)n^{-1/2}, K0 = psi(1/4) - log pi, k(a)=e^{-a/2}/(1-e^{-2a}). The Gamma term is one finite paired integral.
Form domain used here: D_A = {F in L^2(window): ∫_0^1 ||F - T_aF||^2 a^{-1} da < ∞} (contains bounded functions with finitely many jumps).
Weak response: for h in D_A and test φ in C_c^∞(interior), B(h,φ) = ∫ r_h φ with
  r_h(v) = ∫_0^∞ k(a)[2h(v)-h(v+a)-h(v-a)]da + Σ a_n[2h(v)-h(v+log n)-h(v-log n)] - M_A h(v)  (Fubini; integrable for the h below).
Identity tested: B(h,F) = kappa*C(F) for all F in E0_A ∩ C_c^∞(interior) (the weakest version). By Lemma 3 of the audit, this holds iff
  r_h = kappa*cosh(v/2) + lambda*sinh(v/2) as distributions on the open window (lambda=0 automatic for even h).
h* = B^{-1}cosh satisfies the identity by definition (Galerkin, assuming invertibility). It is not independent and is used only for reference.

## Candidates (fixed in advance, no tuning)
h1 = cosh(u/2)·1_win.   h2 = (cosh(u/2)-cosh(A/4))·1_win = the Dirichlet solution of (∂²-1/4)h = cosh(A/4)/4.

## Results
1. h1 fails, A=0.6 and A=1.0 [EXACT, audit Prop. 4]: r_h1/cosh -> +∞ like (1/2)log(1/d) at the edges. An element of span{cosh,sinh} divided by cosh stays bounded.
   [NUM] rise per 4× decrease of d: 0.689–0.691 (theory (1/2)ln4=0.693). LS residual 37.9% (A=0.6), 19.1% (A=1.0).
2. h2 at A=1.0 fails [EXACT, audit Prop. 5; hypotheses: log2 < A < log3 so only n=2 contributes, A=1]: r_h2 is continuous with slope jump
   a_2 sinh(A/4)/2 = 0.06191 at v0 = ±(log2 - A/2) = ±0.193, and it is real-analytic elsewhere near v0. span{cosh,sinh} is analytic.
   [NUM] finite-difference jump 0.06172 (eps 1e-3), 0.06189 (eps 1e-4). LS residual 3.0%.
3. h2 at A=0.6 (Gamma only) fails NUMERICALLY ONLY [NUM, not a proof]: LS residual 6.92%, stable to 1e-7 for N=60/120/240.
4. Explicit E0 test pairings [NUM] with F=(∂²-1/4)G, G=(1-t²)²t^k (k=0,2), zero-extended. F has jumps at the edges and lies in D_A, not C_c^∞ (audit §Domain).
   Moments are exactly 0 by integration by parts (G=G'=0 at edges); numerically ~1e-12.
   A=0.6: B(h1,F)=9.13, 3.62; B(h2,F)=0.009385, 0.008732 (two routes agree to ~2e-10 for h2, ≤0.6% for h1).
   A=1.0: B(h1,F)=3.21, 3.00; B(h2,F)=0.00847, 0.00994.
   These use the identity on D_A ∩ E0. For the C_c^∞-only version, rely on items 1–2 (exact) or on a density argument not given here.

## Conjectural remarks (NOT results)
[CONJ] An exact representer may need singularities on the edge orbit ±(A/2 - Σ log n_i) ∩ window.
  This would need a boundary-regularity and propagation analysis that is not done here. Ellipticity alone does not imply it, and coincident shifts could cancel for general A.
[CONJ] h* may vanish at the edges like 1/log(1/d) (heuristic only).
[CONJ / question] Is there an independent "edge-orbit ansatz" (cosh minus prime-indexed edge layers with one Gamma-determined profile) with zero residual? Untested.
We do NOT claim that every Gamma-only or moment-only construction fails. Only the two explicit candidates are shown to fail.

## Mapping vs orthogonality
An independent h with the identity, B(h,h)<0, and the correct sector conditions (audit Lemma 1–2, both sectors) would give only the
signature pattern of a Hodge index statement on a finite Galerkin model. A geometric realization would still need a lattice/rational structure,
a real (1,1)/primitive identification (Hodge structure, J), and a map Φ with -I(ΦF,ΦF)=W(F) defined independently of W.
Dimension: on E0_A, W = B is an unbounded form (symbol m -> ∞), hence not of finite rank. A linear map from an infinite-dimensional E0 into a fixed finite-dimensional H^{1,1}
pulls back a form of rank <= dim H^{1,1}, so it cannot reproduce W. The size/limit structure of a target is undetermined.
Files: match1983.py/json, match.txt (raw run), kink1983.py/json, mom1975.py (copy). Raw data unchanged.

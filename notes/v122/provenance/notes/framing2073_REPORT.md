# t2073: 2x2 pairings of h_sym = 2cosh(u/2), h_asym = 2sinh(u/2) under Q, P, W, I = -Q (scratch only)
Mon Nov 9 2026 (CST). Nothing was pushed. RH is NOT proved, no Hodge index is proved, and Phi is NOT constructed. No positivity claim goes beyond the numbers below.
Labels: [EXACT] = closed form; [NUM] = double-precision Galerkin (inertia2057.matrix, exact-form cells, scipy quad, k via expm1);
[CONT-NUM] = continuum quadrature of Q(h,h) using closed-form overlaps <Eh,T_aEh> (independent of the cell basis).

## Conventions (project, unchanged)
I_A=[-A/2,A/2]; r±=e^{±u/2}; C±(F)=∫F r±; E0=ker B*, B=[r+,r-]; P=BJB*, J=[[0,1],[1,0]];
Q=W-P=H_A-M_A I (inertia2057 §1, cutoff2072 §0); I := -Q = renormalized t2072 trace pairing = P-W.
Discrete: orthonormal cell basis e_i=1_{cell}/sqrt h; B[:,0]=<r+,e_i>, B[:,1]=<r-,e_i> (inertia2057.matrix). The cell projection of h_sym
is B(1,1)^T, and the projection of h_asym is B(1,-1)^T. These are the same vectors that represent the functionals C++C- and C+-C-, so in this basis the
"function" and the "Riesz functional" vectors coincide. The two cases differ only in using Q and Q^{-1}.

## Exact facts [EXACT]
- C+(h_sym)=C-(h_sym)=2sinh(A/2)+A; C+(h_asym)=2sinh(A/2)-A=-C-(h_asym).
- Even F: C+=C-; odd F: C-=-C+ (u->-u swaps r+ and r-). P(even F)=2|C+|^2, P(odd F)=-2|C+|^2.
- P(h_sym,h_sym)=2(2sinh(A/2)+A)^2, P(h_asym,h_asym)=-2(2sinh(A/2)-A)^2, P(h_sym,h_asym)=0.
- ||h_sym||^2=4(sinh(A/2)+A/2), ||h_asym||^2=4(sinh(A/2)-A/2).
- <Eh,T_aEh> = 4[sinh(L-a/2) ± (L-a/2)cosh(a/2)] for 0<=a<2L, L=A/2 (+ for cosh, - for sinh); 0 for a>=2L.
- Parity: the cell grid is symmetric and Q is symmetric Toeplitz, so the exchange matrix commutes with Q (commutator 0 in floating point).
  The 2x2 matrices of Q, P, W, and I in the (sym,asym) basis are therefore diagonal (off-diagonal entries <3e-15 [NUM]). The same holds for S.
- Woodbury: if W is invertible and R:=B^T W^{-1} B, then S:=B^T Q^{-1} B = -(I-J R^{-1})^{-1} J. To first order in R^{-1}, S ≈ -J - J R^{-1} J.
  This gives I(H_t,H_t) = -t^T S t ≈ t^T J t + (Jt)^T R^{-1}(Jt). It is checked to 1e-13 [NUM].
- Riesz: H_t := Q^{-1}Bt gives I(F,H_t) = -(Bt)^T F = -(C+(F)t1 + C-(F)t2). This is a tautology, and the check returned 3e-13.

## Numbers (n=1024 unless stated; stable to ≤1e-6 relative across n=256/512/1024 for function pairings)
Function pairings, raw (diag of 2x2 in sym/asym basis; off-diag ≈0):
| A | Q(hs,hs) | Q(ha,ha) | P(hs) | P(ha) | W(hs) | W(ha) | I(hs)=-Q | unit Q(hs) | cos(negvec,hs) | eig resid | max_E0 I(F,hs^) |
| 0.5 | -1.694449 | 0.006378 | 2.020953 | -5.5e-5 | 0.326504 | 0.006323 | +1.694449 | -0.8428 | 0.98444 | 0.451 | 0.426 |
| 0.694 | -3.410002 | 0.007977 | 3.931272 | -3.93e-4 | 0.521270 | 0.007585 | +3.410002 | -1.2161 | 0.98471 | 0.329 | 0.424 |
| 1.0 | -7.965134 | 0.026683 | 8.341085 | -0.003560 | 0.375951 | 0.023123 | +7.965134 | -1.9501 | 0.99493 | 0.190 | 0.378 |
| 1.1 | -9.606923 | 0.022538 | 10.181808 | -0.006340 | 0.574885 | 0.016198 | +9.606923 | -2.1289 | 0.99371 | 0.186 | 0.403 |
| 1.386 | -16.22559 | 0.069106 | 16.66113 | -0.025857 | 0.435536 | 0.043249 | +16.22559 | -2.8108 | 0.99735 | 0.122 | 0.345 |
| 2.0 | -37.31148 | 0.332207 | 37.85200 | -0.245563 | 0.540519 | 0.086644 | +37.31148 | -4.2883 | 0.99862 | 0.079 | 0.340 |
| 3.0 | -104.8480 | 3.459890 | 105.3733 | -3.167935 | 0.525334 | 0.291956 | +104.8480 | -7.2224 | 0.99955 | 0.042 | 0.305 |
The continuum check [CONT-NUM] of Q(hs,hs) and Q(ha,ha) agrees with Galerkin to ≤2e-6 relative. Example: A=1 gives -7.9651338 and 0.0266830.
The unique negative Q eigenvalue (n=1024) is -1.98746 at A=1 and -2.17343 at A=1.1. The unit Rayleigh quotient of h_sym is -1.9501 at A=1 and -2.1289 at A=1.1.
The negative eigenvector is even. Its cosine with h_asym is ~1e-15, and its cosine with the constant function is 0.995.
max_E0 I(F,ha^) over unit F in E0, with ha^ the unit h_asym: 0.537, 0.555, 0.463, 0.459, 0.507, 0.548, 0.613. The vector h_asym is also not an eigenvector (residual 0.4–0.9).
For both modes, the discrete <F,h> is 0 on E0 (<1e-12). The nonzero I(F,h) is therefore entirely -H_A(F,h).

Riesz lifts, from S=B^T Q^{-1} B (n=1024):
| A | S (r+,r-) | S_sym=t^TSt | S_asym | eig S | I(H_sym) | I(H_asym) | W(H_sym) | W(H_asym) | cos(negvec,H_sym) |
| 0.5 | [[-0.5136,-0.5248],[.,-0.5136]] | -2.0768 | +0.02244 | -1.0384,+0.01122 | +2.0768 | -0.02244 | 0.0797 | 0.0222 | 0.989 |
| 0.694 | [[-0.4291,-0.5721],..] | -2.0024 | +0.2859 | -1.0012,+0.1430 | +2.0024 | -0.2859 | 0.0024 | 0.245 | 0.953 |
| 1.0 | [[-0.005242,-0.994766],..] | -2.000015 | +1.979048 | -1.000008,+0.989524 | +2.000015 | -1.979048 | 1.5e-5 | 0.0207 | 0.806 |
| 1.1 | [[-0.000960,-0.999048],..] | -2.000015 | +1.996175 | -1.000008,+0.998088 | +2.000015 | -1.996175 | 1.5e-5 | 0.0038 | 0.793 |
| 1.386 | | -2.000008 | +1.998866 | | +2.000008 | -1.998866 | 7.6e-6 | 1.1e-3 | 0.853 |
| 2.0 | | -2.000003 | +1.999766 | | +2.000003 | -1.999766 | 3.5e-6 | 2.3e-4 | 0.888 |
| 3.0 | | -2.000002 | +1.999944 | | +2.000002 | -1.999944 | 1.8e-6 | 5.6e-5 | 0.881 |
The inertia of S is one negative and one positive at every A and n tested. This matches the t2057 Haynsworth count n_-(Q)+n_+(S)-2 = n_-(Q|E0) = 0.
The direction is now also identified: -S>0 on sym and -S<0 on asym.
The lift-level entries are not converged in n. As n=256→512→1024, S+J shrinks and the smallest eigenvalue of W falls by about 3.4× per doubling
(A=1: W_min = 1.1e-4, 3.3e-5, 9.8e-6; R=B^TW^{-1}B has eigenvalues 39, 73, 94 and 1.1e4, 3.8e4, 1.3e5). Over the same refinements, W(H_sym) = 1.8e-4, 5.2e-5, 1.5e-5.
Galerkin on these dyadic cells is nested, so continuum inf W ≤ the finite W_min. The continuum values are not determined here.
The sign pattern is the only robust lift result: I(H_sym) ≈ +2 and I(H_asym) < 0. At A=0.5 the negative value is small (-0.022) and stable in n.

## Answers
1. Q(h_sym,h_sym) < 0 at every tested A [NUM + CONT-NUM]. So I(h_sym,h_sym) = -Q(h_sym,h_sym) > 0 for the function.
   Q(h_asym,h_asym) > 0 and I(h_asym,h_asym) < 0. On span{h_sym,h_asym}, I has signature (1,1), and the plane is I-orthogonal (by parity).
2. The unique negative eigenvector of Q is even and nearly aligned with h_sym: cos = 0.9949 at A=1 and 0.9937 at A=1.1, rising to 0.9996 at A=3.
   It is even more aligned with the constant function (0.995). This alignment is numerical, and only the index count is certified.
3. h_sym is NOT a Q-eigenvector: the relative residual is 0.19 at A=1 and 0.186 at A=1.1, and it decreases with A (0.04 at A=3).
   So I(F,h_sym) is NOT proportional to C+(F)+C-(F).
4. E0 is NOT I-orthogonal to h_sym or h_asym. For unit h and unit F in E0, max |I(F,h_sym)| = 0.378 (A=1) and 0.403 (A=1.1).
   For h_asym the values are 0.463 and 0.459. This is all -H_A(F,h).
5. Riesz lifts: I(H_sym,H_sym) ≈ +2.00002 > 0 and I(H_asym,H_asym) ≈ -1.98 (A=1) and -1.996 (A=1.1). S has signature (1,1).
   The C± lifts are nearly I-null: I(H_+,H_+) = -S_11 = 0.0052 at A=1. That is near the P-hyperbolic structure, with S ≈ -J. Woodbury explains this through the
   large R = B^T W^{-1} B in finite models. It is not a proof.
6. W(H_lift) is POSITIVE (and small) in every finite model, because finite W has n_-(W)=0. The outside test "W(H_lift) < 0" therefore fails for all lifts
   and is the wrong test, since H is not in E0 and W ≠ Q off E0. Under RH, W ≥ 0 on the full window (Weil sum over zeros on the line), so
   "W(H_lift)<0" would be impossible. The coherent ample-type tests are Q(h)<0 (function) and -<v,Q^{-1}v> > 0 (Riesz lift). Both hold numerically for the
   symmetric mode.
   Neither is independent of the certified facts: the Riesz sign is equivalent, by Haynsworth, to the inertia already in t2057, together with the parity
   placement computed here.
7. A single symmetric class cuts out only the hyperplane C+ + C- = 0, which contains E0 in codimension one. The odd sector lies in that hyperplane,
   but the odd part of E0 needs C+(F)=0 in addition. For example, h_asym is odd, satisfies C++C-=0, and has C+(h_asym)=2sinh(A/2)-A ≠ 0.

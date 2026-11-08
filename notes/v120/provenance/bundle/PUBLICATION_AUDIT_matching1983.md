# PUBLICATION_AUDIT — matching1983 (+ criterion corrections in moment1975). 2026-11-07, 10:25 PM CST.
Scope: correct overclaims only. No new tests. Raw data/json/logs unchanged; notes1983.md rewritten; first draft kept as notes1983_raw_superseded.md.

## Corrections made
1. WRONG (old notes1983 l.36, moment1975 sector line): "B>=0 on E0_A <=> n_-(B_e)<=1 & q_e<=0". This fails at index 0: B positive definite gives q>0, yet the restriction is PSD.
   Replaced by Lemma 1 (both files). The even condition alone does not give E0 positivity, so the odd sector is now stated separately (Lemma 2).
2. Spectral/operator claims (self-adjointness, compact resolvent, discrete spectrum, existence of B^{-1}cosh in infinite dimensions) were only sketched.
   Publication status: UNPROVED. All criteria are stated for the computed finite Galerkin matrices (or under explicit invertibility hypotheses).
3. h2 failure at A=0.6 relabeled NUM (was implicitly a disproof). The h2 failure at A=1 is EXACT only under the stated hypotheses (A=1, only n=2).
4. The universal-representer singularity claim, the finite edge-orbit sum, and the Gamma-only no-go were downgraded to CONJ.
   Ellipticity without a boundary-regularity/propagation proof does not give them, and several shifts could cancel for general A.
5. Added the dimension remark: a fixed finite H^{1,1} cannot carry W on infinite-dimensional E0.
6. Added domain/admissibility statements for h1, h2 and the E0 test functions (below).

## Lemma 1 (bordered inertia; finite dimension) [EXACT]
Let B be a real symmetric invertible n×n matrix (mass-orthonormal coordinates), c ≠ 0, W = ker c^T, q = c^T B^{-1} c. Then
  n_-(B|_W) = n_-(B) - 1 + [q>0],   n_0(B|_W) = [q=0],   n_+(B|_W) = n_+(B) - 1 + [q<0].
Consequently B|_W >= 0  <=>  n_-(B)=0, or (n_-(B)=1 and q<=0). In the latter case B|_W is positive definite iff q<0 and has a one-dimensional kernel iff q=0.
If n_-(B)=0 then q>0 automatically. If n_-(B)>=2 then B|_W has a negative direction.
Proof. Let K = [[B, c],[c^T, 0]]. Schur congruence with [[I, -B^{-1}c],[0,1]] gives K ≅ diag(B, -q), so In(K) = In(B) + In(-q).
Choose a basis Z of W and e with c^T e = 1; T = [[Z, e, 0],[0, 0, 1]] is invertible and
T^T K T = [[Z^T B Z, Z^T B e, 0],[e^T B Z, e^T B e, 1],[0, 1, 0]].
Adding multiples of the last coordinate (whose diagonal entry is 0 and which pairs only with e) clears the e-row/column entries Z^T B e and e^T B e.
This gives the congruence diag(Z^T B Z, [[0,1],[1,0]]), so In(K) = In(B|_W) + (1,1,0). Comparing the two expressions proves the formulas. ∎
Infinite-dimensional use needs: B self-adjoint and invertible on a stated domain, c in the domain of B^{-1} (or the form-sense analogue). These are NOT verified here.

## Lemma 2 (sector split) [EXACT, Galerkin]
On a centered window, the reflection R F(u)=F(-u) commutes with B (even symbol m) and with P. cosh is even, sinh is odd.
Hence, for any R-invariant Galerkin space, E0_A = (even ∩ cosh^⊥) ⊕ (odd ∩ sinh^⊥), orthogonal for both L^2 and B. So
  B >= 0 on E0_A  <=>  [Lemma 1 condition for (B_e, cosh)] AND [Lemma 1 condition for (B_o, sinh)],
given that each sector block is invertible. Both conditions are needed. In the A=0.6 and 1.0 runs the odd block had n_-=0 [NUM]; this is not a general fact.
Full-window W (a separate question): P = 2(C^2 - S^2), so W_e = B_e + 2cc^T and W_o = B_o - 2ss^T.
If n_-(B_e)=1 and B_e is invertible: W_e >= 0 <=> q_e <= -1/2. If B_o is positive definite: W_o >= 0 <=> q_o <= 1/2 (matrix determinant lemma plus rank-one interlacing).

## Lemma 3 (annihilator) [EXACT]
For a distribution r on the open window I: ∫ r φ = 0 for all φ in C_c^∞(I) with ∫φ e^{u/2} = ∫φ e^{-u/2} = 0  <=>  r ∈ span{e^{u/2}, e^{-u/2}} on I.
(The identity B(h,·) = kappa·C + mu·S on smooth E0-type tests is a special case.)
(Standard: two linearly independent functionals; pick ψ± in C_c^∞(I) with a nonsingular moment matrix and project any φ.) So the identity on smooth E0 tests is equivalent to r_h ∈ span{cosh, sinh} on I.

## Prop. 4 (h1 fails) [EXACT]
h1 = cosh(u/2)1_I is in D_A: its two jumps give ||h1 - T_a h1||^2 = O(a) as a -> 0, so ∫_0^1 ||h1 - T_a h1||^2 a^{-1} da < ∞ (equivalently ∫ k(a)||h1 - T_a h1||^2 da converges near 0, since k(a) ~ 1/(2a)).
r_h1(v) = cosh(v/2)[Jc(d+)+Jc(d-)] - sinh(v/2)[Js(d+)-Js(d-)] + prime terms - M_A cosh(v/2),
where Jc(d) = ∫_0^d k(1-cosh(a/2)) + ∫_d^∞ k and Js(d) = ∫_0^d k sinh(a/2).
As v -> A/2, ∫_{d+}^∞ k -> +∞ (k(a) ~ 1/(2a)); every other term stays bounded (the prime terms are bounded indicator combinations).
So r_h1/cosh is unbounded on I, while (kappa cosh + lambda sinh)/cosh is bounded. By Lemma 3 the identity fails, for A=0.6 and A=1.0. ∎

## Prop. 5 (h2 fails at A=1) [EXACT under: A=1, so only n=2 has log n < A]
h2 is Lipschitz on R (kink at ±A/2), so h2 ∈ D_A. Write r_h2 = (Gamma part) + a_2[2h2(v) - h2(v+log2) - h2(v-log2)] - M_A h2(v).
On I the Gamma part is real-analytic: the integrals are analytic in d± > 0, and h2 is analytic on I.
h2(v+log2) is supported on v <= A/2 - log2 =: -v0 (here v0 = log2 - 1/2 ∈ I). It is continuous there, with one-sided slopes h2'(A/2^-) = sinh(A/4)/2 and 0.
So r_h2 has slope jump a_2 sinh(A/4)/2 at -v0 (and symmetrically at +v0, from h2(v - log2)).
No other term is non-analytic there: h2(v - log2) vanishes identically for v < v0 (so near -v0); 2a_2 h2(v) and M_A h2(v) are analytic on I; the Gamma part is analytic on I. Since log 3 > A, no other shift enters.
A function in span{cosh,sinh} has no slope jump, so by Lemma 3 the identity fails. [NUM] jump 0.06189 vs 0.06191 predicted. ∎
For general A, several shifts and edges can coincide and cancel slope jumps; no claim is made.

## Domain / admissibility of the tests
- F = (∂²-1/4)G with G = (1-t²)²t^k, t=2u/A, zero-extended. G and G' vanish at ±A/2, so G ∈ C^1(R) with G'' piecewise polynomial.
  F is piecewise polynomial with jumps at ±A/2 (G'' ≠ 0 there). F is NOT smooth and NOT C_c^∞.
- E0 membership is exact: ∫_I (G''-G/4)e^{±u/2} = [G' e^{±u/2} - G (e^{±u/2})']_{∂I} = 0. This needs only G ∈ C^1 with G=G'=0 at the edges.
- F ∈ D_A (finitely many jumps). The pairings B(h,F) are well defined, and the physical-space spring integrals converge (||F-T_aF||^2 = O(a)).
- These tests disprove the identity posed on D_A ∩ E0. For the C_c^∞ version, use Props. 4–5 (via Lemma 3), or a density argument
  (C_c^∞(I) ∩ E0 dense in D_A ∩ E0 for the form norm), which is plausible but NOT proved here. h2 at A=0.6 has only NUM evidence either way.

## Status table for publication
| Claim | Status |
|---|---|
| Lemma 1, 2, 3 (finite / Galerkin; distribution annihilator) | EXACT |
| Operator-level discrete spectrum, B^{-1}cosh in infinite dim | UNPROVED (assumption) |
| h1 fails (A=0.6, 1.0) | EXACT |
| h2 fails at A=1 | EXACT under stated hypotheses |
| h2 fails at A=0.6 | NUM only |
| E0 test pairings, residual %, kink value | NUM |
| moment1975 brackets [0.6918,0.6920], [0.01182,0.01197]; λ2 trend; A=2 unresolved | NUM |
| Edge-orbit singular support / 1/log edge law / Gamma-only no-go | CONJ |
| Map into primitive (1,1) | NOT CONSTRUCTED; finite H^{1,1} excluded: W = B on E0_A, and B is unbounded there (symbol m -> ∞; high-frequency F in E0_A), so it is not of finite rank [EXACT modulo the form-domain setup]; target size undetermined |

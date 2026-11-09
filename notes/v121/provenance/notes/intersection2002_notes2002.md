# intersection2002: audit of the "Euler zero-set / Serre Tor" proposal (t2002), with repairs
Nov 8 2026 ~1:20–2:05 PM CST. Scratch only; no repo/manuscript edits. RH NOT proved.
Labels: [EXACT] [THM] [NUM] [MODEL] [OPEN].
Scripts: tor2002.py/.json, hecke2002.py/.json, lefschetz2002.py/.json.
Also corrected effectivity2001 (notes + relrr2001.py; tagged "CORRECTED 2002").

## 1. Claim-by-claim (what is right, what needs repair)
1. "Euler class = zero set of a generic section" is TRUE in the smooth, oriented, transverse setting, as a SIGNED count, and it needs
   rank E = dim B for points (Hutchings, cup.pdf Thm 5.2; MathWorld "algebraic intersection number").
   It is NOT a count of holomorphic sections.
   - On a surface, the zero set of a section of a LINE bundle is a curve, not points.
   - c1 is defined with no sections at all: O(−1) on P¹ has c1 = −1 and h⁰ = h¹ = 0 [EXACT, tor2002].
2. "H·C counts zeros" holds for an EFFECTIVE C. Effectivity requires an existing nonzero regular section (h⁰ ≥ 1).
   The Hodge-index proof (Hartshorne V.1.9; Block, IntersectionTheory.pdf Lemma 52) uses ample·effective > 0 together with RR to get sections.
3. HRR / Dolbeault index gives χ = Σ(−1)^i h^i, not h⁰. Kähler alone gives no vanishing.
   P¹×P¹ examples [EXACT, Künneth]:
   - O(1,−3): χ = −4, cohomology concentrated in h¹ = 4.
   - O(−1,−1): D² = 2 > 0, yet h⁰ = h¹ = h² = 0.
   - O(−3,−3): D² = 18, h⁰ = 0, h² = 4. Effectivity comes from −D, via h² = h⁰(K−D).
   So "positive square ⇒ sections" needs the dual side and large n. This is exactly the (E)/(R) gap.
4. Serre's Tor formula needs:
   - a regular ambient (or finite projective dimension);
   - finite length / proper intersection (complementary dimension);
   - for the "exact integer invariance", proper flat families. It does not survive arbitrary "warping".
   Counterexample [EXACT]: A = k[x,y]/(xy), M = A/(x), N = A/(y). Then length Tor_i = 1, 0, 1, 0, … forever, so χ is undefined.
   Rational equivalence (families over P¹; Block Prop. 10) is not smooth homotopy. Intersection multiplicity is not the number of sections.
5. Lefschetz: the local sign is sign det(1 − Df) (Hutchings Thm 2.1). det Df = 1 does NOT give the count [EXACT, lefschetz2002]:
   - hyperbolic diag(2, ½): det Df = 1, det(1−Df) = −½, index −1;
   - elliptic rotation by π/3: det(1−Df) = 1, index +1;
   - shear, and the oscillator's time-2π map (= I): det(1−Df) = 0, so the fixed points are non-isolated and the formula needs a Bott-clean version.
   Flows: periodic orbits come in families, and the distributional trace uses 1/|det(1 − P_γ)| (Atiyah–Bott / Guillemin–Sternberg).
   Connes' p-adic orbits carry exactly this |1−u|_p^{-1} normal factor, which gives log p·p^{−m/2} [THM, Connes 1999 Thm 4].
   Morse counts need compactness, Morse nondegeneracy and properness.
   For Kähler: X_H = J∇H relates the two flows pointwise. Imaginary-time continuation is NOT automatic.
6. Δ and the boundary:
   - Δ vanishes at the cusp to order 1 (q-coefficient τ(1) = 1). The τ(n) do not vanish.
   - τ(n) ≡ σ11(n) (mod 691) holds (checked for n ≤ 60). A congruence cannot give real positivity or a collapse to Λ(n)/√n.

## 2. The key test: does weight-12 data collapse to Λ(n)/√n?  [EXACT + NUM, hecke2002]
−L'/L(Δ,s) has coefficient (α_p^m + β_p^m) log p at n = p^m, where α+β = τ(p) and αβ = p¹¹.
Normalize to the critical centre (α/p^{11/2} = e^{iθ_p}) and divide by √n. The Δ weight is then 2cos(mθ_p)·log p·p^{−m/2}.
The target is log p·p^{−m/2}, so the ratio is EXACTLY 2cos(mθ_p):

| n | 2 | 4 | 3 | 9 | 5 | 25 | 7 | 49 |
|---|---|---|---|---|---|---|---|---|
| ratio | −0.530 | −1.719 | 0.599 | −1.642 | 0.691 | −1.522 | −0.377 | −1.858 |

The ratios have no fixed sign and are not 1. For example, at p = 2 the p² coefficient is (τ(2)² − 2·2¹¹) log 2 = −3520 log 2.
Eisenstein: ζ(s)ζ(s−11) has (1 + p^{11m}) log p. Normalized, that is (p^{−11m/2} + p^{11m/2}) log p·p^{−m/2}, which is non-unitary and off by up to 10⁹ by p = 7.
What DOES produce the target from Δ: Rankin–Selberg L(Δ×Δ̄) = ζ·L(Sym²Δ), so the normalized weights are (2 + 2cos 2mθ_p)·target
= target (ζ part) + (1 + 2cos 2mθ_p)·target (Sym² part), verified to 1e−16.
So ζ's weights sit inside Δ⊗Δ̄ as the trivial (Tate / Petersson-diagonal) constituent. Extracting them means dividing out L(Sym²Δ), and the Tate
class only returns ζ itself [ANALOGY: no new information about ζ's zeros].
Verdict: Hecke/weight-12 = calibration only. Trace formula = term-by-term normalization control (already Connes; no new proof).

## 3. Repair that does advance: derived self-intersection of the diagonal (Tor), exact  [EXACT, tor2002]
For a regular Cartier divisor D ⊂ X (D a smooth curve of genus g_D on a surface), Koszul gives:
- Tor_0(O_D,O_D) = O_D, Tor_1 = O_D(−D) = N^∨, Tor_{≥2} = 0;
- [O_D ⊗^L O_D] = [O_D] − [N^∨] in K_0(D);
- χ = χ(O_D) − χ(N^∨) = D² (RR on the curve, any genus).
Diagonal of C×C: N_Δ = T_C, so Δ·Δ = χ(O_C) − χ(Ω_C) = 2 − 2g. This is a NEGATIVE Euler number from Tor, and it ties directly to the diagonal counterterm.
No automatic sign:
- Δ in P¹×P¹: +2; Δ in E×E: 0; Δ in C×C with g = 2: −2;
- a fibre: 0; a (−1)-curve: −1; the ample (1,1) curve: +2;
- transverse h·v: Tor lengths [1, 0], giving 1.
Arithmetic translation:
- For Spec Z̄, the conormal of the "diagonal" corresponds to the canonical Arakelov divisor κ, with deg κ = log|d_Q| = 0 (vdG–S).
- So the naive derived self-intersection χ(O) − χ(κ) is 0, not K0. This is counterterm1995's |d| = 1 obstruction restated in Tor/K-theory.
- K0 must come from an archimedean correction to the conormal: a metrized/equivariant conormal (analytic torsion, or the arithmetic-GRR
  R-genus applied to the diagonal embedding).
- MODEL: K0 = 2E[log|x|] under the Tate weight (effectivity2001) is the candidate "log-norm of the metrized conormal". [OPEN as an intersection.]

## 4. Usable, non-circular section-counting condition for (R)
Replace "h⁰>0" with Minkowski [THM]: a lattice of rank r and covolume V has a nonzero vector with ‖v‖² ≤ (4/π)Γ(r/2+1)^{2/r}V^{2/r}.
Condition (R_M). There is a construction x ↦ E_x (Arakelov bundle on Spec Z̄), built WITHOUT using J's sign, such that:
 (i) rk E_{nx} = n·C−(x) + O(1) and deg E_{nx} = ½n²J(x,x) + O(n).
     Then slope = deg/rk ≈ nJ/(2C−) → ∞ when C− > 0 and J > 0, so Minkowski gives nonzero vectors of norm → 0.
 (ii) every nonzero vector of norm ≤ 1 in E_{nx} yields an effective object Y in a cone 𝒦 with class nx (up to bounded error), and
 (iii) (A): J(e, 𝒦∖0) > 0. This holds for positive functions (parabolic1998).
Then (A) + (R_M) ⇒ n+(J) = 1 (effectivity2001 §2). Missing: the functor x ↦ E_x and (ii), i.e. "sections are effective cycles".
The ordinary Spec Z×Spec Z = Spec Z does not provide it. Full W has infinite rank per window, so finite models are calibration only.

## 5. Recommendation (the user's two options)
- Trace formula with vector–covector: use it for term-by-term normalization control.
  The off-diagonal prime weights are already fixed by 1/|det(1−Df)|-type normal factors [THM].
  The new item is the diagonal written as a derived self-intersection.
- Hecke in weight 12: calibration only (exact 2cos mθ mismatch).
- Clearest next object: a metrized derived diagonal, i.e. compute [O_Δ ⊗^L O_Δ] with an archimedean metric on N^∨, and test whether its
  arithmetic degree equals −K0 = γ + log 8π + π/2 = 5.37218 exactly, without inserting K0.

## Sources (fetched/opened)
- Hutchings, cup.pdf: https://math.berkeley.edu/~hutching/teach/215b-2011/cup.pdf (Thm 2.1 Lefschetz sign det(1−df); Thm 5.2 Euler class = zero set of a generic section).
- MathWorld: https://mathworld.wolfram.com/AlgebraicIntersectionNumber.html (signed, transverse, complementary dimensions).
- Block, IntersectionTheory.pdf: http://www.columbia.edu/~abb2190/IntersectionTheory.pdf (smooth varieties; Prop. 10 rational equivalence via P¹; Lemma 52 Hodge index).
- nLab intersection pairing: https://ncatlab.org/nlab/show/intersection+pairing (user link; not needed beyond the above).
- Hartshorne V.1.9.
- Connes 1999: https://arxiv.org/abs/math/9811068
- van der Geer–Schoof: https://arxiv.org/abs/math/9802121
- YouTube links not watched (not needed).

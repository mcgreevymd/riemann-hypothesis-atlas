# effectivity2001 — relative (GRR/fibred) effectivity: what it adds to RR, and the exact remaining construction
Nov 8 2026 ~12:05–12:50 PM CST. Scratch only; no repo/manuscript edits. RH NOT proved. Labels [EXACT] [THM] [NUM] [MODEL] [OPEN].
Scripts: relrr2001.py/.json (sympy), arith2001.py/.json, p1asym2001.py/.json, selfdual2001.py/.json. counterterm1995 scheme claims NOT used.
"Relative" = families/maps f: X→B with base change (GRR), not physical relativity; the Lorentz/conic picture is the signature (1,n) structure only.

## 0. GRR as used [THM, assumptions stated]
f: X→B proper, X,B smooth quasi-projective (or f proper lci), E coherent: ch(Rf_*E)·td(T_B) = f_*(ch(E)·td(T_X)), i.e. relative td(T_f).
For a family of curves (f smooth proper of relative dim 1, B a curve) and L on X, Deligne/Mumford form of the degree-1 part:
  c1(det Rf_*L) = ½ f_*(c1(L)²) − ½ f_*(c1(L)·c1(ω_{X/B})) + c1(det Rf_*O_X)    (Deligne, "Le déterminant de la cohomologie", Contemp. Math. 67 (1987)).
GRR gives CLASS identities (χ, det lines). It gives no positivity and no h⁰ by itself. What it adds is the relative slot and base change.

## 1. Calibration: C×C over F_q, absolute vs relative effectivity [EXACT, relrr2001]
Gram(h,v,Δ,Γ_F): h=C×pt, v=pt×C, h·v=1, Δ²=2−2g, Γ²=q(2−2g), Δ·Γ=q+1−a, Γ·h=q, Γ·v=1.
Primitive Gram on (Δ',Γ') = [[−2g,−a],[−a,−2gq]]. For g=1, det = 4q−a², so Hodge index ⇔ |a| ≤ 2√q (Hasse). Falsifier: fake (q,a)=(5,5)
gives D ⊥ h,v with D² = (34√41−164)/25 ≈ 2.15 > 0.
Absolute RR route (Hartshorne V.1.9) needs h⁰(nD)+h⁰(K−nD) ≥ χ(nD), i.e. control of h² via Serre duality on the surface.
RELATIVE route (new formulation here, exact):
 (i) For f=pr1 (fibre v), L=O(nD): if fibre degree n·D·v > 2g−2, then R¹f_*L=0, so f_*L is a vector bundle of rank n·D·v + 1 − g [CORRECTED 2002; earlier 'n·D·v' was exact only for g=1] and
     h⁰(X,L) = h⁰(C,f_*L) ≥ χ(C,f_*L) = χ(X,L). Only base RR h⁰≥χ on the curve C is used, with no h² control on X.
 (ii) GRR: deg det f_*O(nD) = χ(X,nD) − rk·(1−g), and its n² coefficient is exactly D²/2 (sympy, all g).
 (iii) Tilt using BOTH fibrations: for D ⊥ H=h+v with D·h=D·v=0 (the E0 case, both moments 0), set D' = D+ε(h−v). Then D'·H = 0,
     fibre degrees D'·v=+ε and D'·h=−ε, and D'² = D² − 2ε² > 0 for small ε. By (i)+(ii), nD' is effective for n≫0, so D'·H>0: contradiction.
     The fake data violate exactly this, which makes it a falsifiable test.
 (iv) Section adjunction: Δ is a section of pr2, and Δ² = −deg σ*ω_{X/B} = 2−2g (verified). This is the diagonal counterterm in relative form.
WHAT GRR ADDS (precise): higher cohomology is controlled FIBREWISE by positive fibre degree, and the fibre degree of a class is its MOMENT
(J(v,·)=C−, J(h,·)=C+). Hodge index then follows from (A) ampleness plus a HALF-SPACE effectivity statement, instead of (E) on all of {J>0}.

## 2. The relative lemma on the actual extended space V = D(I)⊕U [EXACT logic]
Hypotheses, with cone 𝒦 ⊂ V independent of J's sign:
 (A) J(e,y) > 0 for y ∈ 𝒦∖0. For pointwise-positive functions plus α,β≥0 this holds exactly (parabolic1998).
 (R) relative effectivity: J(v,x) > 0 and J(x,x) > 0 ⇒ x ∈ 𝒦.
Conclusion: n+(J)=1, hence W ≥ 0 on the window.
 Proof: a second positive direction gives x ⊥ e with J(x,x)>0. If C−(x)≠0, then (R) applies to ±x. If C−(x)=0, then x ∈ E0, and the tilt
 x+ε(h−v) gives J(e,·)=0, C−=ε>0, J>0, so (R) applies again. Either way this contradicts (A).
Pointwise cone fails (R) as well: x = e+δF with F sign-changing has C−>0 and J>0 but is not in 𝒦₊. (R) is weaker than (E) (a half-space
of {J>0}) but still needs a sections-defined cone.

## 3. Candidate (most promising): fibred square over Spec Z-bar, with direct images as Arakelov bundles
Object needed (the exact construction, [OPEN]):
 a functor x ↦ E_x, an Arakelov (Hermitian) bundle on Spec Z̄ = "f_*O(x)" for the projection of the hypothetical square onto one factor, with
  rk E_{nx} = n·C−(x) + O(1) (the O(1) is the fibre '1−g' term),  deg E_{nx} = ½n²J(x,x) + O(n)  [GRR slot: the quadratic term is J, which is zeros-free],
  ampleness: a nonzero small section of E_x gives J(e,x) > 0.
Then (R) follows from base RR alone, which EXISTS:
 - theta-h⁰ (van der Geer–Schoof): h⁰(L) − h⁰(L^∨) = deg L by Poisson, hence h⁰ ≥ deg. CAVEAT [CORRECTED 2002]: theta-h⁰ is ALWAYS > 0
   (log of a theta sum ≥ log 1), so 'h⁰ > 0' is NOT a nonzero small section; an actual nonzero lattice vector needs Minkowski
   (λ1 ≤ √r·covol^{1/r}) or an effectivity threshold, so (R) must be phrased with a quantitative h⁰ threshold, not h⁰>0. Verified for rank 1 (error 2e−16) and rank 2 (3e−16).
 - Connes–Consani's RR for Spec Z̄ with integer dimensions (rank-1 divisors).
 Both are 1-dimensional, which is exactly the BASE slot that the relative formulation requires (not the square).
Where it is unconstructed:
 (a) the ordinary fibre product Spec Z ×_Z Spec Z = Spec(Z⊗Z) = Spec Z EXISTS but is the diagonal again (wrong, 1-dimensional); the needed
     2-dimensional 'absolute' square with an intersection theory is not available [CORRECTED 2002];
 (b) ranks C−(x) are real for test functions, so one needs a continuous (Murray–von Neumann/type II) rank and a theta-h⁰ for Hilbert modules.
     I know of no such construction (not verified either way) [CORRECTED 2002: earlier 'no such h⁰ exists' was unsupported]; vdG–S note h¹ has no definition without duality;
 (c) the GRR identity deg E_{nx} = ½n²J must reproduce primes, Gamma and M_A. This is not available beyond the trace-formula identity.
Full W has infinite rank on each window, so any finite-rank E_x construction is calibration only.

## 4. Archimedean/Gamma normalization in this frame [EXACT + MODEL]
 - K0 = 2·E[log|x|] under the Tate/theta archimedean weight e^{−πx²}|x|^{−1/2}dx (the critical twist s=1/2). NUM agrees to 1e−15.
   Equivalently K0 = 2(log Γ_R)'(½), where Γ_R = Mellin of the vdG–S archimedean effectivity e^{−π‖1‖²}.
 - Weight e^{−πcx²} shifts it by −log c (NUM: −0.693147 at c=2).
 - Theta-RR with the SAME weight on L and L^∨ is exact only at c=1. For c=2 and c=½ the defect is non-constant (±0.319, ∓0.343, ∓0.347 at deg −0.5, 0.7, 1.5),
   so it cannot be absorbed into a degree shift.
 ⇒ the self-duality of the base RR (Poisson) forces c=1, and hence forces K0. This is a new independent geometric datum fixing the residual
   scalar, independent of counterterm1995's scheme claims [MODEL: it is the theta-h⁰ normalization, not yet an intersection].
 Arithmetic-RR torsion slot, computed (P¹_Z, Fubini–Study, L² metric), verified to 3e−11 at n=10⁴ [EXACT]:
   χ̂(O(n)) = N²/4 + (N/4)log N − (N/4)log 2π + (1/12)log N + 1/24 − ζ'(−1) + o(1),  with N=n+1.
   The n² coefficient is ½ĉ1(Ō(1))² = ¼ (arithmetic Hilbert–Samuel). The N log N term is the L²-vs-Quillen anomaly (Bismut–Vasserot).
   The constant ζ'(−1) is the torsion/R-genus type (Gillet–Soulé).
 Mismatch: the P¹ torsion constants are of type ζ'(−1), log 2π. K0 is of type ψ(¼), log π. Both are zeta-regularized-determinant slots, and K0 IS one:
 K0 = −2∂_s log det_ζ((s−Θ)/2π) at s=½ (Deninger; verified in counterterm1995/det_scale1995). So the torsion slot is the right TYPE.
 P¹ is the wrong fibre; the needed fibre is the archimedean Frobenius flow.

## 5. Matching table for the candidate
| piece | FF relative (C×C→C) | candidate (square→Spec Z̄) | status |
| fibre degree | D·v, D·h | C−, C+ (Laplace moments at ±½) | EXACT identification of the slot |
| vanishing | deg > 2g−2 ⇒ R¹=0 | large C− ⇒ "R¹=0" | OPEN (no fibre cohomology) |
| base RR | h⁰ ≥ χ on C | theta-RR h⁰ ≥ deg (verified) / Connes–Consani | EXISTS (rank 1/lattices) |
| quadratic term | GRR: D²/2 | ½J (zeros-free) | needs E_x construction |
| diagonal | Δ² = −deg σ*ω_rel | K0 = 2E[log|x|], forced by Poisson self-duality | MODEL |
| primes | Γ_{F^k}·Δ = N_k | Λ(n)/√n atoms | via trace formula only |
| ample | h+v | e=h+v, (A) exact on positive functions | half done |

## 6. What does not follow
 GRR alone gives no sign. Direct-image positivity (Griffiths/Berndtsson) presupposes a positive bundle upstairs, which would be circular here.
 Faltings–Hriljac/Pic-hat (X over Spec Z) is the relative square of a curve over Z, not the absolute square; it stays closed.
 J ≠ J_a: the relative lemma needs no complex structure. J_a/g_a would enter only via a weight-1 sector (parabolic1998/hodge1981 Künneth); not used.
 The Lorentz picture: (A)+(R) is exactly "no ellipse-type line through e" from parabolic1998, now with the tilt along the null pair h−v
 (the two asymptotic directions).

Sources:
 - Hartshorne, Algebraic Geometry, V.1.9.
 - Deligne, Contemp. Math. 67 (1987).
 - Gillet–Soulé, Invent. Math. 110 (1992) 473–543, https://doi.org/10.1007/BF01231343
 - van der Geer–Schoof, Selecta 6 (2000) 377–398, https://arxiv.org/abs/math/9802121
 - Connes–Consani, https://arxiv.org/abs/2205.01391
 - Deninger, Invent. Math. 104 (1991) 245–261
 - Connes, https://arxiv.org/abs/math/9811068
 - local: parabolic1998, matching1989, counterterm1995 (det_scale only)

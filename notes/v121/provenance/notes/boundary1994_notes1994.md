# boundary1994: explicit modular boundary, cup signs, and the two-moment dictionary
Scratch only, unpublished. No RH claim and no new sign. Weight k = 12 (w = 10), with k = 16 as a control.
Labels: [V] = computed here, exact unless marked numeric; [C] = cited, source checked; [H] = analogy; [O] = open / missing.
Scripts: boundary1994.py, duality1994.py, hecke_test.py and eis_cocycle_test.py, with outputs in *.json.

## 0. Conventions
- G = PSL2(Z) = <S> * <U>, with U = TS. On V = V_10 = Q[X]_{≤10}, −I acts trivially. Right action: (P|g)(X) = (cX+d)^w P((aX+b)/(cX+d)).
- Cocycles: φ(gh) = φ(g)|h + φ(h). Coboundaries: (δv)(g) = v|g − v.
- Z¹ = ker(1+S) × ker(1+U+U²), in coordinates (φ(S), φ(U)). φ(T) = φ(U)|S − φ(S)|S.
- Fibre form: ⟨P,Q⟩ = Σ (−1)^a a!b!/w! p_a q_b. It is symmetric, invariant, of signature (5,6).
  - ⟨(X−z)^w, (X−z')^w⟩ = (z−z')^w [V].
  - V^T = Q·1 (the cusp's null vector). V_T = V/(T−1)V, detected by the top coefficient p_w = ⟨1,·⟩.
- Haberland form on W: B(P,Q) = ⟨P|(T−T⁻¹), Q⟩. (T−T⁻¹) is anti-self-adjoint for ⟨,⟩, so B is alternating.

## 1. Spaces and maps [V, dims; C, Hodge types]
- Dimensions: dim Z¹ = 14, dim B¹ = 11 and dim H¹(G,V) = 3. For k = 16: 18, 15 and 3.
- The period space is W = {φ ∈ Z¹ : φ(T) = 0} = ker(1+S) ∩ ker(1+U+U²) (via φ(S) = φ(U)), with dim 3.
  W ≅ H¹(G, G_∞; V) ≅ H¹_c [V for the relative-cocycle normalization]:
  a relative cocycle (φ, v) with φ(T) = v|(T−1) normalizes uniquely to v = 0.
- Two exact sequences, which must not be conflated:
  - (c) 0 → V^T --δ--> W = H¹_c → H¹_! → 0. Here δ(1) = 1|S − 1 = X^10 − 1 = e.
    - e is a COBOUNDARY in Z¹(G,V): δ(1)(T) = 0, and its class in H¹ is [0,0,0] [V].
    - e is nonzero in H¹_c. Weight 0, type (0,0): the invariant (lowest) step of the limiting MHS.
  - (h) 0 → H¹_! → H¹(G,V) --res--> V_T → 0, with res[φ] = p_w(φ(T)).
    - res is well defined (it vanishes on (T−1)V) and surjective on the integral lattice H¹_Z/torsion [V].
    - The quotient V_T is Q(−11): weight 22, type (11,11).
- Reconciliation: H¹_! = ker(res) = im(H¹_c → H¹) is pure of weight 11, types (11,0)+(0,11) [C Zucker]. Its dimension is 2.
  - H¹_c (dim 3) = weight 0 + weight 11.
  - H¹ (dim 3) = weight 11 + weight 22.
  - The two are dual under H¹_c × H¹ → H²_c = Q(−11).
- Parity (ε = diag(−1,1)): W⁺ = ⟨e, c1⟩ and W⁻ = ⟨m1⟩. Here c1 = X²(X²−1)³ and m1 = 4X⁹−25X⁷+42X⁵−25X³+4X.
  The Eisenstein cocycle below has odd φ(S), and it glues to the odd cusp class. So the e-side is ε-even and the Eis-side is ε-odd.
- **Correction to hodge1991.** Calling X^10 − 1 "the Eisenstein class" was wrong.
  - It is δ(1): the weight-0 boundary class of H¹_c, zero in H¹.
  - "Radical of the Haberland pairing" is a true statement on W = H¹_c: the radical is ker(H¹_c → H¹) = δ(V^T). It does not transfer to H¹.
  - "Mod 691 the cusp class lands on the Eisenstein line" should read "on the boundary line δ(V^T) in H¹_c".
  - The real Eisenstein class (weight 22) is computed in §3.
  - hodge1991's dim-3 W with W⁺ of dim 2 is H¹_c. H¹ itself has the opposite parity split. That is inferred from the duality and the odd Eis cocycle; ε was not computed directly on H¹.

## 2. H¹_c side: boundary sub and even cusp line; Hecke without periods [V]
- Hecke element for n = 2: {[[1,0],[0,2]], [[1,1],[0,2]], [[2,0],[0,1]], [[2,0],[1,1]]}.
  This is a Zagier-type element; I did not transcribe Zagier 1990 Thm 2 exactly. It was VERIFIED to preserve W and to give −24 = τ(2) on m1.
- T2 on W_Z = Ze ⊕ Zc1 ⊕ Zm1 (columns are images):
      T2 = [[2049, 108, 0], [0, −24, 0], [0, 0, −24]],   with 2049 = 1 + 2^11.
  - Boundary eigenvalue from cosets: T_p(1) = 1 + p^11. The two terms are the two boundary characters 1 and p^11.
  - Eigenvector for −24: 36e − 691c1, primitive. Index [W⁺_Z : Ze ⊕ Z(36e − 691c1)] = 691.
  - This independently reproduces the Kohnen–Zagier r⁺ ∝ (36/691)e − c1 with no period integrals.
  - k = 16 control: T2 = [[32769, −3240], [0, 216]], with index 3617 = num ζ(−15).
- Splitting:
  - As abelian groups, (c) splits over Z (H¹_!,Z ≅ W_Z/Ze is free).
  - Hecke-equivariantly it splits only over Z[1/691]. The section is c̄1 ↦ c1 − (36/691)e, from x·2073 = −108.
  - Mod 691, T2 + 24 is nilpotent with kernel = image.

## 3. H¹ side: the actual Eisenstein cocycle and its residue [V]
- From L(G12, s) = ζ(s)ζ(s−11), take r_n = Λ(G, n+1).
  - Odd n: rational values. Even n: only n = 0, 10 survive, with r_0 = r_10.
  - The even part is i·r_0·e, a coboundary.
- Ansatz φ(S) = ρ⁻_G = −(5/1584)X⁹ − X⁷/480 − X⁵/504 − X³/480 − (5/1584)X and φ(T) = c((X+1)^11 − X^11).
  This is a cocycle iff c = 691/720720 = a0/11, where a0 = −B12/24 = 691/65520.
  - Boundary identity: res[φ_G] = a0(G12), i.e. φ(T) = a0∫_X^{X+1} t^w dt.
  - The same holds at k = 16 (c = a0/15).
- Eis_1 := φ_G / a0, so res = 1. In the integral coordinates of H¹_Z/torsion (Z³, the coordinate map is onto, SNF [1,1,1]):
  - Eis_1 = (−1, −22680/691, −33736/691). Both fractions are ≡ 123/691 mod 1.
  - The fractional part is parallel to [m1] = (0, 630, 630), the odd cusp class.
  - Denominator: exactly 691 at k = 12 and exactly 3617 at k = 16, i.e. num ζ(1−k). This is Harder's denominator, recomputed from scratch [V; C Harder–Pink].
- Gluing: [H¹_Z : H¹_!,Z ⊕ Z·691Eis_1] = 691. The two 691s are dual, not the same statement:
  - (c) boundary sub with the even cusp line;
  - (h) Eis quotient with the odd cusp line.
- Integral comparison W_Z/Ze → H¹_!,Z: c1 ↦ (0,0,−120) and m1 ↦ (0,630,630). The index is 75600 = 2⁴3³5²7, which is 691-free.

## 4. The boundary duality at cochain level [V]
- I solved for the general bilinear D(P,ψ) = Σ x_{g,h}⟨P|g, ψ(h)⟩, for g in 10 group elements and h ∈ {S,T}, subject to two conditions:
  D vanishes on coboundaries, and D(P, Q) = B(P, Q) on W × W.
- Every solution gives:
      D(e, Eis_1) = 6,   D(c1, Eis_1) = 216/691,   D(m1, Eis_1) = 0.
- Hence D(δ1, ψ) = 6⟨1, ψ(T)⟩ = 6·res ψ. This is the fibre invariant × coinvariant pairing ⟨1, X^10⟩ = 1, times the Haberland 6.
- Hecke orthogonality check: D(36e − 691c1, Eis_1) = 216 − 216 = 0. The Eisenstein class sees the eigen cusp class as orthogonal, which gives the 36/691 a THIRD time.
- Bordered matrix H¹_c × H¹ in the bases (e, c1, m1) × (Eis_1, [c1], [m1]):
      [[6, 0, 0], [216/691, 0, −6], [0, 6, 0]]
  The border entry is computed, not defined. 691 appears only off-diagonal, and Hecke orthogonalization removes it at the cost of index 691.

## 5. Cup signs into a symmetric weight-22 pairing [V numeric; C theorem]
- Q on H¹_! in the basis (c̄1, m1) is [[0,−6],[6,0]].
- Sym²: Q₂(ab, cd) = ½(Q(a,c)Q(b,d) + Q(a,d)Q(b,c)). Gram on (c1², c1m1, m1²) = [[0,0,36],[0,−18,0],[36,0,0]]. Signature (1,2), det 23328 = 2⁵3⁶.
  On the Hecke-split lattice the entries scale by 691².
- Actual Hodge vector ρ = −iω₊c1 + ω₋m1 (mod e), with ω₊ = 0.114379… and ω₋ = 0.0092693… (numeric):
  - Q(ρ, ρ̄) = 0.0127225 i, so i^11·Q(ρ, ρ̄) = +0.0127225 > 0. This is Hodge–Riemann for the (11,0) class.
  - Q₂(ρ², ρ²) = 0, i.e. F^22 is isotropic.
  - Q₂(ρρ̄) = +8.09e−5 > 0 on the real (11,11) line.
  - Q₂(Re ρ²) = Q₂(Im ρ²) = −8.09e−5 < 0 on (22,0)+(0,22).
  - ⟨Δ,Δ⟩ = ω₊ω₋/2^10 = 1.0353620568043210e−6, matching the literature value.
- Sign entry: (2i)^11 = (2i)^10 · 2i.
  - The fibre part is ⟨(X−z)^10, (X−z̄)^10⟩ = (2iy)^10 = −2^10 y^10, a sign (−1)^{w/2}.
  - The base part comes from dz∧dz̄ = −2i dx∧dy.
- Theorem used [C]: Zucker (1979) gives H¹_!(Y, V_w) ≅ H¹_(2), a pure Hodge structure of weight w+1, polarized by Q.
  The tensor square of a polarized Hodge structure is polarized, so Sym² is polarized of weight 2(w+1):
  - positive on the real (11,11) part;
  - negative on Re/Im of the (22,0) part.
  Sign control holds ONLY on the Hodge-typed vectors. The full 3-dimensional space is indefinite (1,2).

## 6. One cusp, two moments: the exact dictionary and where it breaks
- Fibre boundary plane span{1, X^10}: these are the null vectors of the cusps ∞ and 0, the endpoints of the torus axis.
  - ⟨p0 + p10X^10, same⟩ = 2p0p10 = 2(α² − β²), with p0 = α+β and p10 = α−β [V].
  - S swaps p0 ↔ p10 [V].
- Ledger (sections/02_functional.tex): C₊ = L_F(1), C₋ = L_F(0), P = 2Re(C₊ C̄₋), signature (1,1).
  - Even sector: W = B_A + 2|C|². Odd sector: W = B_A − 2|S|².
- Exact modular counterpart:
  - The period polynomial is the Mellin transform of f along the axis 0 → i∞: r_n = ∫ f(it)t^n dt.
  - S acts as t ↦ 1/t, i.e. s ↔ k−s.
  - The boundary coefficients of ρ_f are p10 = iΛ(f,1) and p0 = −iΛ(f,11): the edge values at s = 1 and s = k−1.
- On cocycles, P|(1+S) = 0 forces p0 = −p10 (α = 0). So Hermitian P = 2Re(p0 p̄10) = −2|p10|² ≤ 0.
  Modular cocycles automatically sit in the "odd sector", and the boundary vector e has fibre norm −2 [V].
- Why C± are two functionals but only one survives here:
  - Level 1 has ONE cusp. The boundary gives dim V^T = 1 (invariant, weight 0, in H¹_c) and dim V_T = 1 (coinvariant, weight 22, in H¹). These are dual, of different weights and on different spaces.
  - The two endpoint null vectors are G-equivalent (S ∈ G), so S-gluing ties them together and only their difference e survives.
  - Two independent endpoint moments need two inequivalent cusps, e.g. Γ0(N), where the Fricke involution plays s ↔ 1−s.
    Expected boundary dimensions there are 2 + 2 [C: dim Eis = #cusps]; this was not computed here.
  - The ledger's F has no such built-in symmetry, so P stays indefinite. That is the paper's two-sector split, nothing new.

## 7. Term-by-term against the complete W
- **P (hyperbolic):** = the fibre form on the two endpoint null vectors. Exact [V]. Cohomologically, the cup pairing annihilates δ(V^T) (radical), while the fibre form gives −2.
  The cohomological shadow of P is the H¹_c × H¹ duality D(δ1, ψ) = 6·res ψ: a hyperbolic pairing between DIFFERENT weights (0 and 22).
- **Γ (normalized kernel):** r_n = (2π)^{−n−1}Γ(n+1)L(n+1), and the fibre reproducing kernel is (z−z')^w [V]. The match to the ledger's Γ-controlled H_A kernel is only [H].
- **Prime powers:** these are Hecke operators. On the boundary, T_p = 1 + p^11 (characters 1 and p^11); on the cusp, τ(p). Mod 691 these merge into a Jordan block [V].
  This is exact for Hecke, but the ledger's Λ(n)/√n weights only correspond [H]. Hecke preserves the sequences; it supplies no sign.
- **M_A (diagonal):** no counterpart [O]. The natural diagonal candidate ⟨Eis, Eis⟩ is undefined, because H¹ × H¹ needs one compact factor; it needs Zagier-type renormalization.
  This is exactly the "independent h with B(h,h) < 0" gap: the border vector h = Eis is constructed independently (§3–4), but its self-pairing is not defined without a counterterm.
- **Does the natural quotient pairing realize the full W?** No. H¹_! with Q or Sym² Q realizes only the cuspidal calibration ⟨f,f⟩ = ω₊ω₋/2^10 (rank 2 or 3, fixed and finite). The full W is infinite-rank on a fixed window, so no fixed finite target matches.
- **E0:** the analogue is ker(res) = H¹_! (a kernel description), equivalently W/δ(V^T) (a quotient description).
  Integrally they differ by small primes (75600). Against the Hecke splitting they differ by 691.

## 8. Concrete advancement (falsifiable, verified at k = 12 and k = 16)
1. res_∞[φ_{G_k}] = a0(G_k), i.e. φ(T) = a0∫_X^{X+1} t^w dt.
2. The residue-1 Eisenstein class has denominator num ζ(1−k), and D(δ1, Eis_1) = 6.
3. The Hecke T2 lattice index equals the same prime.
Together: the boundary map recovers the constant term (the C-type moment) and Harder's prime independently of the period integrals.
This is no sign statement, and the special congruence does not extrapolate to Hodge signs.

## 9. Precise remaining theorem [O]
Needed: on the complete-W test space, a mixed structure with all of the following.
- (i) A sequence 0 → B_inv → H_c → H_! → 0 and its dual 0 → H_! → H → B_coinv → 0.
- (ii) C₊, C₋ realized as the invariant and coinvariant boundary functionals, i.e. D(δv, ψ) = ⟨v, res ψ⟩, rather than as two endpoint values.
- (iii) W restricted to E0 = the polarization on H_!, satisfying Hodge–Riemann with respect to a Weil operator, plus a renormalized diagonal equal to M_A.
None of (i)–(iii) is constructed here for W. The modular case shows (i)–(ii) are natural only when the cusp or symmetry structure is present, and (iii) is the entire RH difficulty.

## Sources
- Kohnen–Zagier 1984: https://people.mpim-bonn.mpg.de/zagier/files/scanned/ModFormsRatPeriods/fulltext.pdf
- Zagier, Hecke operators and periods (1990): https://people.mpim-bonn.mpg.de/zagier/files/scanned/HeckeOperatorsAndPeriodsModForms/fulltext.pdf
- Pasol–Popa 2013: https://arxiv.org/abs/1202.5802 ; Pasol–Popa (Hecke property): https://arxiv.org/abs/1207.5766
- Haberland 1983: https://doi.org/10.1002/mana.19831120113
- Zucker 1979, Ann. Math. 109: https://doi.org/10.2307/1971221
- Harder's denominator problem (cites Harder–Pink 1992 Satz 2; Harder 2023 Thm 5.1.2): https://doi.org/10.2140/ent.2025.4.251
- Mazur 1977: https://www.numdam.org/item/PMIHES_1977__47__33_0/
- Schmid 1973: https://doi.org/10.1007/bf01389674

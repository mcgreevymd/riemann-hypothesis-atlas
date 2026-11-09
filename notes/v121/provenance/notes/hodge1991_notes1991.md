# hodge1991: the 691 "tangent at infinity" question (scratch, unpublished; no RH claim, no new sign)

Labels: [V] = verified by computation in this directory (exact unless stated otherwise); [C] = cited, with the source checked to exist (URL below);
[H] = heuristic or analogy. Scripts: m12_lattice1991.py, periods1991.py and conic1991.py, with outputs in the matching *.json.
The unaudited eisenstein1990 claims (universal f_k, Krein, zero-sum, gauge) are NOT used here.

## 0. Answer in one line
There is a genuine "tangent line at infinity", but it does not live at 691. It is the cusp's null vector, its polar and the monodromy weight flag
in the coefficient system Sym^10. That structure is prime-independent and comes with an honest symmetric form.
691 is something different: it is the integral gluing between that boundary (Eisenstein) line and the cusp line. It is an index,
congruence module and extension order. It is not a degeneration of any real or complex pairing.
The one place where 691 looks like a "point on its own polar" is mod 691. There:
(a) the cusp class falls onto the Eisenstein/radical line;
(b) T2 becomes a Jordan block with N^2 = 0 and ker N = im N.

## 1. The integral M12 lattice [V] (m12_lattice1991)
- Relations: 691E12 = 691E4^3 − 432000Δ, and E6^2 = E4^3 − 1728Δ. Also G12 = 691/65520 + Σσ11(n)q^n.
- Index: M12(Z) = ZE4^3 ⊕ ZΔ, and [M12(Z) : Z·691E12 ⊕ ZΔ] = 691. The vector 691E12 is primitive because gcd(691, 432000) = 1.
- The residue (constant-term) map a0 : M12(Z) → Z is surjective, with kernel S12(Z) = ZΔ. On the Hecke-Eisenstein line, however, its image is 691Z.
- Mod 691: 691E12 ≡ 566·Δ (checked coefficientwise for n ≤ 400; 566 = 65520 mod 691). So the Eisenstein eigenvector falls into the kernel of its own residue functional.
- Coefficient gcd: gcd_{n≤400}(σ11(n) − τ(n)) = 691.
- Hecke T2 on the basis (E4^3, Δ): T2 = [[2049, 0], [−1296000, −24]], with eigenvalues 2049 = σ11(2) and −24 = τ(2).
  Their difference is 2073 = 3·691. Mod 691, (T2 + 24) ≡ [[0,0],[316,0]] ≠ 0 and its square is 0. [V, conic1991]
  So mod 691 the Hecke algebra T = Z[T2] has a nilpotent N with ker N = im N = the line of Δ. This is the arithmetic shadow of a unipotent monodromy.
- Exact sequence: 0 → S12 → M12 → (boundary) Z → 0. Over Q it is split by the Hecke operators. Over Z the Hecke splitting has cokernel Z/691.
  That is Mazur's Eisenstein ideal picture in level 1 [C Mazur].

## 2. Hodge realization [C + V]
- Local system: V_10 = Sym^10(std) on Y = SL2(Z)\H. For the full group, H^1(SL2(Z), V_10) ≅ W := {P ∈ Q[X]_{≤10} : P|(1+S) = 0, P|(1+U+U^2) = 0} [C Kohnen–Zagier §1].
- Dimensions [V periods1991]: dim W = 3, with W+ of dimension 2 and W− of dimension 1.
  - The coboundary is X^10 − 1 = 1|S − 1. Here 1 is the T-invariant vector of V_10, i.e. the cusp's null vector.
  - Eichler–Shimura: W ⊗ C ≅ S12 ⊕ conj(S12) ⊕ M12/S12.
- Mixed Hodge structure: 0 → H^1_!(V_10) → H^1(Y, V_10) → Q(−11) → 0.
  - H^1_! is pure of weight 11, of types (11,0) + (0,11), and has dimension 2.
  - The boundary (Eisenstein) piece Q(−11) is pure of weight 22, of type (11,11).
  These are different weights and different objects. The cusp part and the Eisenstein part are NOT one pure Hodge sector.
  Over Q the sequence splits via Hecke (Harder's rational Eisenstein splitting).
  Over Z the denominator of the Eisenstein class is num ζ(−11) = num(691/32760) = 691 [C Harder–Pink 1992 Satz 2; Harder 2023 Thm 5.1.2, as cited in ENT 2025].
- Period polynomial of Δ [V numeric, 30 digits]:
  - r+ / ω+ = (36/691)(X^10 − 1) − X^2(X^2 − 1)^3, with error 5e−19.
  - r− / ω− = 4X^9 − 25X^7 + 42X^5 − 25X^3 + 4X, with error 7e−40.
  - ω+ = 0.114379…, ω− = 0.00926927…
  This matches Kohnen–Zagier.
- Integral lattice W_Z = W ∩ Z[X] has basis {X^10 − 1, X^2(X^2 − 1)^3, m1}; all Smith invariants are 1 [V].
  The Eisenstein line Z(X^10 − 1) together with the saturated cusp line Z(36(X^10 − 1) − 691X^2(X^2 − 1)^3) has index 691 in W+_Z [V].
  This is the same 691 as in §1, now seen in Betti cohomology.

## 3. The pairings: alternating vs symmetric, and the sign bookkeeping
- On V_10: ⟨P, Q⟩ = Σ_{a+b=10} (−1)^a a! b!/10! · p_a q_b [V periods1991].
  - It is symmetric, because Sym^w of an alternating form is (−1)^w-symmetric and w = 10 is even.
  - It is SL2(Z)-invariant (checked on S and T).
  - Its signature is (5,6), so it is indefinite.
  - The cusp vector 1 is isotropic, and its polar is {q_10 = 0}.
  - The rational normal curve (X − z)^10 is isotropic.
  - The degree (monodromy weight) flag is self-dual: deg ≤ j is orthogonal to deg ≤ 9 − j.
  - Polarized-limit sign: ⟨X^10, N^10 X^10⟩ = 10! > 0, where N = d/dX = log T.
- On H^1: cup product followed by ⟨,⟩_{V_10} lands in H^2_c(Q(−10)) = Q(−11).
  It is alternating, because the alternating cup product is tensored with a symmetric form.
  Haberland realization: B(P, Q) = ⟨P|(T − T^{-1}), Q⟩. Its integral Gram matrix on (X^10 − 1, X^2(X^2 − 1)^3, m1) is [V]:
      B(e, ·) = 0 (the Eisenstein line is the RADICAL),   B(c1, m1) = −6 = −B(m1, c1),   W+ ⊥ W+.
  Numerically, ⟨ρ_Δ|(T − T^{-1}), conj ρ_Δ⟩ = −6(2i)^11 ⟨Δ, Δ⟩, i.e. ratio −1.000000000000000 [V].
  This is Haberland's formula up to my global orientation sign [C Pasol–Popa].
  The real/complex Petersson form is positive on H^1_! (Hodge–Riemann with the Weil operator). It does NOT degenerate at 691.
- Where 691 does sit in the pairing [V]:
  - On W_Z/Ze, the pairing has discriminant 6^2.
  - On the Hecke-split cusp lattice Z r+_Z ⊕ Z m1, with r+_Z = 36e − 691c1, B(r+_Z, m1) = 691·6.
  So 691 shows up as the relative discriminant/index of the eigen-split sublattice. This is the congruence module, i.e. extension torsion.
  It is not a null direction of the form.
- From alternating to symmetric, done properly:
  - Fibre level: Sym^2 of (H^1(E), alternating) carries ⟨ab, cd⟩ = ½(⟨a,c⟩⟨b,d⟩ + ⟨a,d⟩⟨b,c⟩).
    This is symmetric, of rank 3, with signature (1,2), i.e. (2,1) up to the overall sign.
    That is exactly the binary-quadratic-form discriminant conic used in polarity1980/hodge1981.
  - Global level: Sym^2 H^1_!(V_10) has dimension 3 and weight 22, with types (22,0), (11,11), (0,22).
    Its (11,11) real line is ω_Δ·ω̄_Δ, i.e. the Petersson norm.
    Same Hodge TYPE as the Eisenstein boundary Q(−11), but a different object. Do not identify them.

## 4. The conic is the actual geometry [V conic1991]
- Setup: f = QX^2 + TXY + ZY^2, with B(f, f) = 2(T^2 − 4QZ), which is SL2-invariant (disc(f|g) = det(g)^2 disc f).
- For z = x + iy:
  - v_z = (X − zY)^2 is isotropic (F^2).
  - x_z = (X − zY)(X − z̄Y)/y has B = −8 and lies on the polar of v_z (F^1 = tangent line). B(v, v̄) = 16y^2.
  - B(ℓ^2, x_z) = −(4/y)|az + b|^2.
- Cusp ∞ ↔ null vector Y^2, with B(Y^2, x_z) = −4/y. So horocycle height = pairing with the cusp null vector.
- Hence E(z, s) = ½ Σ_{primitive null n} (−B(n, x_z)/4)^{−s}: the Eisenstein series is a sum over rational points of the null conic.
- Monodromy at the cusp:
  - T: X ↦ X + Y fixes Y^2; (T − 1)^2 X^2 = 2Y^2 and (T − 1)^3 = 0.
  - ker N = Y^2 (the null point), and im N = span{XY, Y^2} = Y^2⊥ (the tangent line).
  So the weight filtration W(N) at the modular cusp is precisely "null point ⊂ tangent line at infinity".
  For Sym^10, this is the osculating flag of §3.
- Terminology: "cusp" here means the boundary point of X(1). That is a rational point on the boundary conic, NOT the singular-point cusp of boundary1982.

## 5. Verdict on the user's guess
- The geometric tangent at infinity = (cusp null vector 1 ∈ V_10, its polar, W(N)). It exists, is canonical and is the same for every weight and prime.
  Its cohomological image is the Eisenstein class X^10 − 1 = 1|(S − 1), which is the radical of the Haberland pairing.
  The Eisenstein boundary IS the transported tangent-at-infinity direction.
- 691 measures how far the cusp eigenline is from being integrally orthogonal-split from that radical line.
  Mod 691 the cusp class lands on it (691·r+ ≡ 36(X^10 − 1)), and Hecke becomes unipotent.
  The best reading is: 691 is an arithmetic (p-adic) incidence of the null line with the cuspidal line. It is not a real degeneration [V+H].
  Other irregular pairs behave the same way, with the denominator num ζ(1 − k) [C].
- Tie-back to complete W [H]: the honest lesson is bookkeeping, not a sign.
  - Primitive/sign statements live on the quotient by the boundary radical (W_Z/Ze ~ H^1_!), the analogue of primitive cohomology.
  - Integrally, the quotient does not split back. So any arithmetic version of the W = P + B ledger must use the quotient lattice; otherwise spurious 691-type denominators appear.
  - This adds no positivity in a fixed finite space and no sign for W. The target stays a sign-controlled primitive intersection for complete W.

## Sources (checked to exist on 2026-11-07)
- Kohnen–Zagier, Modular forms with rational periods (1984): https://people.mpim-bonn.mpg.de/zagier/files/scanned/ModFormsRatPeriods/fulltext.pdf
- Pasol–Popa, Modular forms and period polynomials, PLMS 107 (2013): https://arxiv.org/abs/1202.5802 (Haberland, Math. Nachr. 112 (1983): https://doi.org/10.1002/mana.19831120113)
- Mazur, Modular curves and the Eisenstein ideal, IHES 47 (1977): https://www.numdam.org/item/PMIHES_1977__47__33_0/
- Harder's denominator problem for SL2(Z) (Ent. Nat. Th. 2025), citing Harder–Pink 1992 and Harder 2023 Thm 5.1.2: https://doi.org/10.2140/ent.2025.4.251
- Ramanujan's congruence primes (691 as an Eisenstein-class denominator in H^1(SL2(Z), Sym^10)): https://arxiv.org/abs/2403.03345
- Schmid, Variation of Hodge structure: the singularities of the period mapping, Invent. 22 (1973): https://doi.org/10.1007/bf01389674

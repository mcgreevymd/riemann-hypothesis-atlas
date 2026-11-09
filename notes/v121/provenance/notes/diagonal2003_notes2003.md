# diagonal2003 (t2003) + spin2004 (t2004). Nov 8 2026, CST. Scratch only; no repo/manuscript edits; RH NOT proved.
Scripts: arak2003.py/.json (metrized diagonal), spin2004.py/.json (spin/spin^c). Labels [EXACT][THM][NUM][MODEL][OPEN].

## t2003: an actual arithmetic derived diagonal, and its comparison with -K0
Ambient: X = P^1_Z (regular arithmetic surface), with X x_Z X = P^1 x P^1 over Z (regular arithmetic 3-fold).
Diagonal: Δ ⊂ X x_Z X is a regular immersion of codimension 1, with conormal N^∨ = Ω_{X/Z} = O(-2).
In K_0: [O_Δ ⊗^L O_Δ] = [O_Δ] - [Ω] [EXACT].
Arithmetic Chow group: Gillet–Soulé CH^_Z, with c1^(L) = (div s, -log||s||^2) and deg(0,g) = ½∫g c1.
Arithmetic adjunction: c1^(O(Δ))|_Δ = c1^(N̂) with the residue metric.
The resulting number is deg c1^(N̂)^2 = ω̂^2 on X [THM, Arakelov/Gillet–Soulé].

Metric: U(2)-invariant (Fubini–Study), so the metric is fixed up to ONE constant: ||·||_ω = e^{-a}||·||_{FS^{-2}}. Exact pieces:
- c1^(O(1)_FS)^2 = 1/2. Computed numerically, and it equals the BGS formula h(P^n) = (n+1)/2 Σ_{j=2}^{n+1} 1/j at n = 1.
- ω̂^2(a) = 4·(1/2) + 2a·deg ω = 2 - 4a.
  Anomaly coefficient under rescaling: d/da = 2 deg ω = 2(2g-2) = -4. This is the arithmetic shadow of Euler number 2-2g = 2.
- Arakelov normalization: ∫g μ_FS = 0. This needs the average of log chordal distance, which is -1/2, so c = 1/2.
  The residue metric is then ||dz|| = (1+|z|^2)e^{-1/2}, giving a = 1/2.

| canonical choice (not fitted) | a | ω̂^2 = Δ̂^3 | −K0 − value |
|---|---|---|---|
| FS^{-2}, Green −log chordal^2 | 0 | 2 | 3.3722 |
| Arakelov (∫gμ = 0, residue metric) | 1/2 | 0 | 5.3722 |
| Kähler vol 1, ω = (i/2)h dz∧dz̄ | −½ log π | 2 + 2log π = 4.2895 | 1.0827 |
| Kähler vol 1, ω = i h dz∧dz̄ | −½ log 2π | 2 + 2log 2π = 5.6758 | −0.3036 |

−K0 = 5.37218 would require a = −0.84305 (e^{-a} = 2.3234), which is a fit and is NOT taken.
Structure [EXACT]: invariant-metric degrees here lie in Q + Q·a. −K0 = γ + log 8π + π/2 contains γ and π/2, so those would have to sit in the metric constant (fitting).
Section self-intersection: for P = 0, (P,P)_Ar = −deg ω̂|_P = −a. The algebraic (integral) part is 0 and everything else is real archimedean.

Tate (dimension-1) model [EXACT]: Spec Z → Spec Z ×_Z Spec Z is an isomorphism, so the conormal is 0 and the derived-diagonal degree is 0 for every metric.
Self-duality of e^{2πixy} fixes dx and ||1|| = 1, i.e. a metric, not only a measure, and it gives deg 0. The character fixes the metric, and the value is 0, not −K0.

What K0 IS [EXACT]: K0 = 2 (log Γ_R)'(1/2) with Γ_R = π^{-s/2}Γ(s/2) (checked to 1e-30). That is a Mellin derivative, a log-det derivative (Deninger det_∞, done in 1995), and a regularized resolvent trace (ψ).
Key mismatch:
- An arithmetic degree shifts linearly, by deg·a, under a constant metric rescale.
- d/ds log(C·det) is invariant under constant C. Only an s-dependent scale λ^s shifts it, by log λ; the −log π in K0 is exactly the π^{-s/2} piece.
- So K0 is a derivative in the spectral variable, not a degree. An intersection interpretation needs a family over the s-line, a metrized determinant whose degree is differentiated: Deninger/arithmetic-RR type. That object is unconstructed.
Arithmetic RR on P^1_Z (t2001) produces ζ'(-1), log 2π and harmonic numbers, not ψ(1/4).

Verdict: an actual intersection was computed on a genuine arithmetic geometry. It fails to give −K0 under every canonical metric, with exact mismatches as in the table, and the anomaly coefficient is −4.
P^1_Z is calibration only; the target W has infinite rank per window. Prime weights stay Connes', not modular τ.
Missing [OPEN]: an s-family / derived archimedean equivariant correction whose degree derivative is the Γ_R log-derivative. A Deninger fibre is NOT constructed.

## t2004: spin / ample-regularity claims (audit)
- c1(X) means c1(TX), not c1 of the polarization. Ample ≠ K-trivial. P^2 has c1 = 3H, odd, so w2 ≠ 0 and it is non-spin with H ample. K3 is spin because K = 0, not because it is ample.
- Wu (x^2 = x·w2 on all of H^2(Z/2), closed oriented 4-manifold): spin ⇒ the free intersection form is even. The converse needs no 2-torsion in H_1, e.g. simply connected.
  Enriques: the free H^2 is U ⊕ E8(-1), even unimodular, sig (1,9), σ = −8, yet w2 = K mod 2 ≠ 0 (2-torsion). Rokhlin confirms non-spin, since 16 ∤ −8. Divisor classes over Z/torsion miss w2.
- Spin^c [THM; Tsiamis arXiv:2605.20178 §4, eqs. (33)-(34), which supports exactly this and NOT "ample ⇒ w2 = 0"]:
  - Every almost-complex manifold has a canonical spin^c structure with determinant K^{-1}.
  - ind(D ⊗ L) = ∫ ch L · e^{c1/2} Â = ∫ ch L · Td = χ(L). Checked symbolically: e^{c1/2}Â = Td in degree 4.
  - P^2: ind O(n) = (n+1)(n+2)/2 although P^2 is non-spin.
  - Spin case: ind D = χ(K^{1/2}) = Â = −σ/8. P^1×P^1: χ(O(-1,-1)) = 0 = −0/8 (this is the t2002 O(−1,−1) example). K3: χ(O) = 2 = 16/8.
- Lattices: P^1×P^1 is U, sig (1,1). K3 is 3U ⊕ 2E8(−1), sig (3,19); H^⊥ has sig (2,19) for H^2 = 2.
  The real primitive (1,1) part is negative definite, sig (0,19), by Hodge–Riemann (Hodge type), not spin.
- Parity [EXACT]: Wu gives D^2 ≡ D·K, so RR χ = D(D−K)/2 + χ(O) is an integer and adjunction D^2 + D·K = 2g − 2 is even. Δ^2 = 2 − 2g is even.
  Parity only; no sign: Δ^2 = 2, 0, −2, −4 for g = 0, 1, 2, 3.
- Δ (weight 12): there is no identified manifold whose tangent bundle carries the coefficients; an even Sym^2 Gram matrix does not prove w2 = 0. The formal J is not a compatible J_a.
- Metric degeneration does not change w2 of a fixed bundle; changing it needs a real singular transition, i.e. new topology. Boundary spin obstructions cannot be read off the tangent at infinity.
- Rokhlin: closed smooth spin 4-manifold ⇒ 16 | σ. The Rokhlin invariant of a spin 3-manifold (σ of a spin filling mod 16) needs a specified manifold.
  w2 is ALWAYS characteristic (Wu), so "when characteristic" is vacuous. Quadratic refinements need extra spin/Pin^- data. Not pursued without a manifold.
Recommendation: use spin^c index = χ(L) as a bookkeeping check on the intersection test (the RR/derived-diagonal integrality). It is not a positivity fix. Spinor/Rokhlin give mod-2/mod-16 constraints, never real signs.

## Sources
- Bost–Gillet–Soulé, JAMS 7 (1994): https://doi.org/10.1090/s0894-0347-1994-1260106-x (height of P^n with FS; Green forms).
- Gillet–Soulé, Arithmetic intersection theory, Publ. IHÉS 72 (1990): https://www.numdam.org/item/PMIHES_1990__72__93_0/
- Arakelov 1974 (Izv.) and Faltings, Calculus on arithmetic surfaces, Ann. Math. 119 (1984): https://doi.org/10.2307/2007043 (adjunction / residue metric). Cited, not re-fetched.
- Deninger, local L-factors / regularized determinants (via counterterm1995).
- Tsiamis, arXiv:2605.20178: https://arxiv.org/abs/2605.20178 (fetched).
- Enriques NS = U ⊕ E8(−1) ⊕ Z/2 (Hulek slides): https://cims.nyu.edu/~tschinke/.conferences/symposium15/talks/HulekRevised.pdf
- MathOverflow 193777: https://mathoverflow.net/questions/193777
- Rokhlin / intersection forms: https://www.geotop-bielefeld.de/node/832
- Huybrechts, Lectures on K3 (user link): https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf (not re-fetched; standard facts).

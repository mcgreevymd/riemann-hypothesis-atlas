# Filter 2271: ledger lemmas sorted against Claude's Euler / Epstein filter

J. W. McGreevy program. Sorted by Grok Bot, read-only (STATE.md and TARGET.md were not edited, nothing was pushed). Source: the owner message t2271u, relaying Claude.

> **RH is not proved.** Claude's claims are unverified. Every bin below is either a restatement, a structural fact, or a negative result.

## 0. The filter, and what is wrong with its framing

Claude's filter: ζ_K, the genus L, Z₁ and Z₂ (d = −20, x²+5y²) "share Γ, conductor, FE and pole plane". Two of them have Euler products and pass, two do not and fail. So "any rotation-vs-boost lemma that also holds for Z₁/Z₂ cannot be the mechanism; it must use multiplicativity somewhere."

The idea is right, and the ledger already holds it: L64 (§73), atlas `euler_fe_conjunction`, L164 (§184). The framing has these errors:

1. **The genus L = L(χ₋₄)L(χ₅) is entire, so it has no pole plane.** Only ζ_K, Z₁ and Z₂ have poles at s = 0, 1. DH mod 5 (the other standing control) is entire as well. So the four functions do not share a pole plane.
2. **The two "passes" are numerical, not proved.** ζ_K and the genus L pass only under GRH, checked by computation: L60 census at T = 60, 54/0 and 52/0 off-line. The only theorem in the test is that Z₁ and Z₂ fail (Davenport–Heilbronn 1936; also h(−20) = 2 > 1 ⇒ zeros in σ > 1, L60).
3. **The test is not new.** It is the ledger's standing control, run before:
   - L60 (§69) d = −20 census;
   - L83 (§92);
   - L135 / L164 (§148, §184): 46 and 52 off-line zeros;
   - L169 (§192): Epstein is the standing ghost #2;
   - §193(b) / t812u: the controls are DH + Epstein;
   - atlas `euler_fe_conjunction`: ½L(χ)L(χ̄) vs DH vs random Euler products vs sign-flipped.

   Claude should cite these and not re-run them as a discovery.
4. **"Uses multiplicativity" is necessary, not sufficient.** The ledger has the counterexamples:
   - Beurling / Diamond–Montgomery–Vorhauer (L64 M4; §304, ζ·ζ_C crosses both walls);
   - B* refuted (§205);
   - over F_q, count-positive Euler products are still off-circle (L166, §189);
   - an Euler product without the FE fails at 1.68–2.48 (atlas #36).

   The filter is a **necessary** sieve. To pass it, a proof step must use the Euler product **and** the FE together. In practice that means the product used as geometry (the composition of correspondences, TARGET Prop 1), not as counting data. MP4 was reworded this way in t812u.
5. **Λ ≥ 0 is not multiplicativity, and it is not necessary.**
   - L194(e)7's Markov ground state uses only Λ(n) ≥ 0.
   - L(χ₋₄) and the genus L have signed Λ_χ and still pass (L193: χ₄ is Markov only to log 3).
   - Z₁ has positive Dirichlet coefficients a_n but signed Λ_Z (L159: 40 negative Lévy coefficients for n ≤ 2000). So "positive coefficients" does not separate either: Z₁ passes KMS/Bochner (L164).
6. **"Compact quarter-turn on E₀" repeats TARGET error C6.** A J commuting with Θ_t on E₀ is free (L192: the Hilbert J). The J has to live on ℋ (C6/C7/C12).
7. **The filter is stronger than "holds for Z₁ ⇒ irrelevant".** Restatement lemmas (RH ⇔ X) hold for Z₁ as equivalences, while X fails for Z₁. They are correct and may be needed ingredients; they are only *insufficient*. So "holds for Z₁" should read "its *sign* step holds for Z₁".
8. **N-L already does the pole-plane part.** TARGET §5 N-L requires the mechanism to work for entire L(χ). So any sign source that lives on the pole plane / H⁰⊕H² is excluded already, with or without Epstein.

## 1. Bins

| Code | Bin | Meaning |
|---|---|---|
| **E** | Passes Euler filter | A proof step really uses the Euler product / Hecke multiplicativity. *None of these produces the sign*; several are negative results showing the Euler product is insufficient. |
| **S** | Holds for Epstein/DH = structure | The proof never uses the Euler product (Γ, poles, FE, translation, Λ-sign, or lattice positivity only). It holds verbatim for Z₁ and/or DH. Restatements are included. |
| **D** | Covered by Deligne torus | Boost on the weight / pole plane, compact U(1) needed on the primitive part, or an obstruction to it. Cite in Claude's §11. Also structure. |
| **C** | Closed-route background | Rotating-frame / Lagrange / Krein-L4 (C14), OS (C13), Lax–Phillips, Hilbert J, local sums, de Branges. |
| **P** | p-adic | Newton/Hodge polygons, Dieudonné, unit-root, Iwasawa. |
| **N** | Euler-sensitive numerics *(extra bin)* | Separate ζ from DH/Epstein numerically, but the readout follows the zero locations. Diagnostics, not mechanisms. |

"§" means a section of `the ledger (STATE.md)`. Secondary tags are in parentheses.

## 2. Table

| # | Lemma | STATE § / file | One-line content | Bin | Reason (the proof step that does or does not use the Euler product) |
|---|---|---|---|---|---|
| 1 | L1 | §4 | T_t is a Q-isometry; RH ⇔ Q ≥ 0 ⇔ unitary Hilbert realization; κ = N₊ | D (S) | Explicit-formula Hermitian structure + translation only. For Z₁/DH the equivalence holds and the realization fails. |
| 2 | L14 (g,h) | §22 | Γ_Frob/√q is a boost of rapidity ½ log q on the hyperbolic plane H+V; the complement is negative definite (Hodge index); obstruction: no surface over ℚ | D | The F_q sign comes from the Frobenius *graph* (geometry). The ζ side keeps only the pole-plane boost, which Z₁ shares. |
| 3 | L15 | §23 | Thm 15.1: T_t boosts the pole pair (a,b) with rapidity t/2. Thm 15.2: sup n₊ = 1 + N₊, so RH ⇔ Lorentzian index ≤ 1 | D (S) | Explicit formula + poles only. True for Z₁, with N₊ > 0. |
| 4 | L19 | §28 | RH ⇔ ∃ Hilbert J with JT_t = U_tJ unitary; inside the cone = rotation, outside = boost = ghost; finite traces are shadows | D | A restatement; no Euler step. |
| 5 | L20 | §29 | T_p/√p = boost of ⟨H,V⟩ × rotation of W (Eichler–Shimura); for ζ only the boost transfers | D (E-local) | Uses Hecke multiplicativity, but on X₀(N)² at a single p. The rotation factor is exactly what is missing for ζ (GL₁). |
| 6 | L27 | §36 | Thm 1.3: RH ⇔ [U_u, J_FE] = 0 ⇔ no boost; ghost birth = Krein collision (L4/L5 picture) | D (C) | A restatement. The Krein-collision / L4 part is the closed C14 neighbourhood. |
| 7 | **L42** | §51 | Thm 4.4 orthogonality pincer: a J commuting with scaling gives c_∞ ⇒ Bochner = Q ⇔ RH; a J reversing scaling gives ♯, Hankel ≠ Q. Thm 6.8: elliptic ⇔ compact ⇔ invariant positive form. Rem 7.6: missing rung = linear quarter-turn J commuting with scaling | D | Claude's §11 statement plus its obstruction. No Euler step; the positive content is RH. |
| 8 | L98 | §109 | One-boost lemma for O(1,n). F_q: Hodge index + one boost ⇒ Hasse. ζ: pole boost of rapidity ½ log λ. Positive involution ⇔ compact unitary group | D | Verdict RESTATEMENT. The missing input is an ample class over ℚ. |
| 9 | **L99** | §110 | Deligne criterion (Milne Prop 1.20): polarizable ⇔ ad h(i) Cartan. Abelian scaling has only an outer Cartan. The missing compact circle is the Deligne-torus U(1) at a complex place; ℚ's archimedean place is real | D (obstruction) | *The* Deligne-torus lemma. The obstruction is archimedean and independent of the Euler product. |
| 10 | **L100** | §111 | thm:intertwine: a polarizing J commuting with F ⇔ Frobenius torus compact. prop:WR: the U(1) of W_ℝ dies on ζ. prop:novortex: no continuous U(1) preserving the zeros. Verdict: no RH-independent J | D (obstruction) | Shows the §11 dictionary has no source for the compact factor over ℚ. |
| 11 | L102 | §113 | Spin(2) Hodge circle (elliptic) vs Spin(1,1) ghost (hyperbolic); over F_q h(i) is the unique compatible J with [J,F] = 0; ghosts admit no invariant state | D | A restatement over ζ. |
| 12 | L106 | §117 | Rosati PD ⇔ ∃ compatible J, [J,F] = 0. No ℚ candidate is positive + count + ghost-sensitive. Degree / Hecke / BC traces are ghost-blind; CC20 Sonin is ghost-blind | D (S) | Positivity over F_q is geometric (Milne 1.27). The Hecke traces *use* multiplicativity and are still blind. |
| 13 | **L110** | §121 | Classification of commuting J: a compatible J exists ⇔ k_r = k_c = 0; for ζ, ⇔ k_c = 0 ⇔ RH | D | A restatement. By the same theorem Z₁ has none. |
| 14 | L113 Thm 2.1–2.2, §3 | §124 | Rosati ⇒ Hodge flat ⇒ Newton flat ⇒ RH; min-boost over Sp metrics; three Hodges (H1 index Lorentz, H2 Rosati definite, H3 Mazur) | D (P) | "Lorentz on U, definite on U^⊥" for curves; geometric input. |
| 15 | L133 | §146 | Castelnuovo–Severi = Rosati; RH for curves ⇔ π/√q unitary for Tr(xy†); indefinite forms allow boosts | D | F_q geometric. |
| 16 | L137 | §151 | \|α\| = √q ⇔ Ax2 (positive †) ∧ Ax3 (ππ† = q); each alone is ghost-blind; no Spec ℤ item qualifies | D | Ax3 alone is FE-level, and Z₁/DH have it. |
| 17 | L157 | §171 | Θ† = Θ^∨ ⇔ [∗,Θ] = 0 ⇒ Θ = ½ + A skew; Γ = dual/adjoint gap; Kähler triple | D | This is TARGET (D) in group form. Θ^∨ = 1 − Θ is the FE (DH has it); the sign step is the adjoint, which is the open part. |
| 18 | L158 | §172 | Kähler identities ⇒ Θ = nα/2 + skew; ℤ⊗ℤ = ℤ collapse; defect requirements R1–R5 ("Euler-product built"); DH not multiplicative | D (E-req) | R1 *requires* the Euler product, but no proof step uses it. |
| 19 | L163 | §183 | Compact on all blocks ⇔ RH (U(n₀+m, m)); "boost frames cannot produce ghosts" is false | D | A restatement. |
| 20 | **§369 (bridge1739)** | §369 | Log-translation = O(1,1) boost of the pole plane; RH ⇔ only the pole plane is boosted (Restatement 3.4); arch symbol is DH-blind | D (S) | Literally Claude's §11 sentence. Circular as a mechanism. |
| 21 | L194 (a,d,e6′) | lem194/LEMMA_194.md | Flow = diag(e^{a/2}, e^{−a/2}) on span{e^{±u/2}}; F_q dictionary; RH ⇔ Q ≥ 0 on cosh^⊥ for all r | D (S) | Linear algebra on the pole plane. Holds verbatim for Z₁; positivity fails there. |
| 22 | **TARGET Prop 4b** | target2162/TARGET.md §2 | A compatible J commuting with T exists ⇔ T is elliptic semisimple (compact closure); for T = q^{−½}F ⇔ RH(C) | D (headline) | Cite first in §11. *Existence* of J is RH-equivalent. |
| 23 | L65 | §74 | Local triple J_p = (2π − a)/√(4p − a²); RH(E/F_p) ⇔ (ω, J_p, g_p), proved by deg > 0. Fock factorization: EP ⇔ restricted ⊗. Multiplicativity + duality + trace formula ⇒ rationality + FE only | E (D-local) | The EP step (Fock) is genuine but yields no sign: "a third input g" is needed. For ζ the local factor is GL₁, so there is no J_p. |
| 24 | L71 | §80 | (3,1) = Hodge index on E×E; F/√p = exp(θ_pJ_p); orbit closure ⇔ supersingular; principalization Pic⁰ = Γ·Δ | D (local) | Local and geometric. |
| 25 | L40 | §49 | Rosati = mirror ♯; positivity ⇔ Rosati = c_∞ on the spectrum ⇔ RH | D | A restatement. |
| 26 | L46 | §55 | FV = q gives only Krein unitarity (true for fakes); the Hilbert upgrade is the single inequality Tr(αα†) > 0 from an ample class | D (P) | The Krein step is FE-level, so it holds for DH. |
| 27 | L30 | §39 | ζ has ♯ with δ_λ∗δ_λ♯ = λ (the FF† = q analogue); all content is (iii) = Weil positivity | S | ♯ comes from x ↦ 1/x + FE; DH and Z₁ carry it. |
| 28 | L152 | §166 | Krein one-liner; the bilinear cup pairs ρ with 1−ρ only; composition law Γ_m·Γ_n; DH consistent but indefinite | S | Conformality + FE only. |
| 29 | L151 | §165 | Tate split: DH has the split with zero boundary terms; ghost-blind in the split, ghost-sensitive in the cup | S | Poisson / FE only. |
| 30 | **L164** | §184 | Modular / KMS compact J (Tomita); KMS ⇔ a_n ∈ ℤ≥0, Bochner; DH fails but Z_{x²+5y²} *passes* with 52 certified off-line zeros ⇒ B2 negative; remaining separator = Euler product | S | **Claude's filter already applied** with Z₁ as the killer. Positive coefficients are not multiplicativity. |
| 31 | L188 | lem2253/LEMMAS_2253.md | Plastic threshold log P for Beurling–Deny of W | S | Γ + poles only; ghost-blind. |
| 32 | L189 | lem2253 | Single-hyperplane Weil criterion | S | A restatement. |
| 33 | L190 | lem2253 | J-kernel exponents = Γ poles | S | Γ-factor only. |
| 34 | L192 | lem2253 | Hilbert J commutes with Θ on the u-line; (C) + (D) are free; content = symbol positivity | S (C) | Holds for any translation-invariant form, Z₁/DH included. TARGET §4 closed route. |
| 35 | L193 + L194(e)7 | lem2253; lem194 | Markov / Perron ground state: χ₄ only for r ≤ log 3; ζ's Q for every r | S\* | Uses only Λ(n) ≥ 0. It separates ζ from DH, but is not necessary (L(χ₄) and the genus L pass with signed Λ) and Z₁ has signed Λ_Z. Not multiplicativity. |
| 36 | L194 (b,c) | lem194 | Weil criterion; index ≤ #off-line quadruples per parity; DH index 0 to r = 3.25, then negatives | S | Spectral-side algebra valid for any real self-dual L. |
| 37 | L145 | §159 | ½ as unitary twist; linear h⁰; missing quadratic RR; a ghost passes everything but discreteness | S (C) | Built from ℤ ⊂ 𝔸 only. |
| 38 | L147 | §161 | CC RR: all H⁰-side objects are ghost-blind; "RR on the square must FAIL for DH ⇒ must use EP" | S (E-necessary) | The proved items use ℤ ⊂ 𝔸 only. The EP clause is a heuristic necessary condition, i.e. Claude's filter. |
| 39 | **L60** | §69, lemma60_progress.md | d = −20 census at T = 60: ζ_K 54/0, genus L 52/0, Z₁ 7 ghosts, Z₂ 6; forms = integral positive polarizations J_Q (Hecke-equivariance, not positivity); h(d) = 1 ⇔ all Z_Q are zero-free in σ > 1 | S (N) | **The four-function test, run 23 Oct.** Lattice positivity of J_Q is free and does not see ghosts. |
| 40 | L83 | §92 | Z_{x²+5y²} = ζ·L(χ₋₂₀) + L(χ₋₄)L(χ₅); 7 ghosts for t < 60; closed orbits see only det Φ | S (N) | Control definition. |
| 41 | L82 | §91 | Connes cutoff detects DH; small-support and archimedean positivity are blind | S (N) | The positivity parts hold for DH. |
| 42 | L189–L190 → see 32–33 | | | | |
| 43 | L32 | §41 | OS: Weil form = degenerate OS form; the archimedean place is RP-negative | C | Closed C13. |
| 44 | §328 (bridge1571) | §328 | OS reflection: ζ and DH are both about half negative | C (S) | Blind to the Euler product. |
| 45 | L7 | §15 | Lax–Phillips scattering | C | Closed. |
| 46 | **L64** | §73 | Each prime term is indefinite; positivity is collective. M1 pole and M2 ARCH are RH-blind; M4 EP is necessary, not sufficient (DMV); M5 FE alone fails at the first ghost; M9 geometric positivity is the only non-circular mechanism, absent over ℚ. Convexity ⇒ positivity is not characteristic of L-functions. Local Hasse everywhere ⇏ global | E (meta) | Claude's filter *is* this synthesis. It sharpens it: Euler product necessary, not sufficient. |
| 47 | **atlas `euler_fe_conjunction`** (#36) | atlas2253/repo/ATLAS.md | Window test: ½L(χ)L(χ̄) positive to ℓ = 12; DH fails at 4.80; random EP without FE fails at 1.68–2.48; sign-flipped fails at 1.60 | E (meta, numerical) | "Neither alone; a proof step must use both at once." This is the earlier four-function test. |
| 48 | L165 | §185 | Support of −F′/F on prime powers ⇔ Euler product; DH σ-pencil keeps the FE; composite leakage; Saias–Weingartner: every λ has infinitely many off-line zeros | E | Multiplicativity used as a characterization; no sign. |
| 49 | **L166** | §189 | F_q: counts + FE + positive integer closed-point counts (Euler product, ℤ≥0) do NOT force the Hodge sign: 675 / 2935 / 4961 off-circle at q = 7 / 11 / 13, degrees ≤ 40 | E (negative) | **Multiplicativity as counting data fails even over F_q.** MP4 survives only geometrically. |
| 50 | **§304 (bridge1419)** | §304 | UF ⇔ ℓ²(ℕ) ≅ ⊗_p ℓ²(ℕ₀); Euler product NOT sufficient: Beurling ζ·ζ_C crosses both walls; Routh / KS L4 | E (negative; C) | The Euler product is used (tensor factorization), and the sign still fails. |
| 51 | L174 B* / §205 | §200, §205 | B*: Beurling + EP + θ < ½ ⇒ RH, refuted numerically | E (negative) | Same lesson as 49–50. |
| 52 | §368 (bridge1736) | §368 | Comb free energy additive ⇔ Euler product (Thm 3.6); positivity = band-limited non-concentration (restatement) | E | The EP step is real; the sign is a restatement. |
| 53 | L187 Thm 3.5 | §370 | Euler ⇔ Hecke eigen; DH is a combination | E | A characterization. Z₁ = ζ_K + L_genus is the same kind of combination. |
| 54 | L39 Prop 3.2 | §48 | BC = tensor product over primes twisted by Galois | E | Yields no sign. |
| 55 | L37 | §46 | Euler factor = feedback loop, stable but not passive (no Euler factor is Schur); must use EP (ζ(s)ζ(s+a) class) | E (check 3) | The EP is used per prime, and the result is a no-go for local passivity. |
| 56 | **TARGET Prop 1** | target2162/TARGET.md §2 | F_q: tr Φ(c)Φ(c)^∨ = Q_ff from FV = q and the min-law Γ_λ·Γ_μ | E (geometric) | The one place multiplicativity enters *as a composition of correspondences*. The sign still comes from Rosati, not from Prop 1. |
| 57 | L57 | §66 | Weil ladder: DH indefinite for A ≥ 3.43 (certified); collective | N | |
| 58 | L142, L149 | §156, §163 | Relative Gram from the prime side; DH onset 3.85; tautology boundary | N | |
| 59 | L167–L169, L171, L172 | §190–§196 | Primitive spectrometer; ζ truncations track log q of the next prime; DH locks (3.85 / 1.90); Epstein onset 3.0, stable; next-prime gain ζ 401/401, Epstein prime powers 400/0 but 15× weaker, smooth a coin toss | N | Uses the actual coefficients, but zero-slaved. |
| 60 | §365 (bridge1730) | §365 | Semilocal edges 0.748 / 1.121 / 1.629 / 2.416 track log p_next; DH has no tower | N (check 3) | |
| 61 | **§329 (bridge1574)** | §329 | Place by place: each W_p is traceless ⇒ indefinite; positivity is collective; DH's first negatives are non-archimedean (composites) | S (check 3) | The local sign is indefinite for ζ as well. |
| 62 | §297 (bridge1393) | §297 | Local terms indefinite; Krein+ only at completion; L4 Krein | C (check 3) | |
| 63 | **L174 Thm I + §202 CC13′** | §200, §202 | The explicit formula sees only ε = +1 and \|det A_p\| = p; local ellipticity is invisible; per-prime SO₂ data is stronger than RH ⇒ (B) must be global | S (check 3, key) | Proves that local rotation data cannot be read by the trace formula. |
| 64 | TARGET §4 "Local sums" | target2162/TARGET.md §4 | Local sums: wrong sign even over F_q | C (check 3) | |
| 65 | L23 | §32 | p-adic slopes are identical for curves and fakes | P | |
| 66 | L38 | §47 | The Iwasawa generator is not a p-adic rapidity inside C_Q (archimedean −log n, p-adic −log_p n); no continuous hom ℝ ↔ ℤ_p; no p-adic positivity | P | |
| 67 | L39 Thm 6.1 | §48 | p-adic rapidity step = scaling + Frobenius | P | |
| 68 | **L42 §8** | §51 | Newton-above-Hodge ⇔ a_p ∈ ℤ_p (integrality; fakes pass); boost slopes ½ ± η/ln p; RH = purity (Prop 8.8) | P | "Boost p-adically" is a restatement of the zero's real part. |
| 69 | L46 Prop 6.9 | §55 | Fake a = p = 13 with slopes ½, ½ but \|α\|/√13 = 3.303 / 0.303 | P | p-adic rotation without archimedean rotation. |
| 70 | L49 | §58 | Fil¹ / unit-root splitting (Katz); Mazur = integrality | P | |
| 71 | **L113 Thm 5.1** | §124 | Ghosts are invisible at ℓ, at p (T² − 33T + 11 has slopes ½, ½) and to the product formula; only the individual \|α\|_v at ∞ breaks | P (central) | Settles check 4 negatively. |
| 72 | L134 | §147 | HR ⇒ Rosati ⇒ π/√q unitary ⇒ flat archimedean Newton ½; Mazur is p-adic | P (D) | |
| 73 | L170 | §199 | Newton ≥ Hodge polygons; local polygon gap 0 | P | |
| 74 | L186 add-on 3 | §345–§347 | F/V = p-adic slope split (0, 11) for Δ at ordinary p; Deligne at ∞; "p-adic locates / archimedean signs" | P | This *is* "same eigenvalue, boost p-adically, rotation archimedeanly", already written. |
| 75 | L60 Prop 5.2, L66, L126 | §69, §75, §137 | ℓ-adic λ, ν are ghost-blind; Iwasawa main conjecture has free unitarity and no positivity; ℚ_p is not formally real | P | |
| 76 | §290 (bridge1333) | §290 | The Legendre Newton polygon breaks for all ghosts but also for 37.6 / 35.1 / 37.3 % of genuine curves | P (N) | Not a detector. |
| 77 | **L161** | §179 | Apsides / Lagrange L4; the gyroscopic, work-free J is ghost-blind | **C (Lagrange)** | The rotating-frame route; background only. |
| 78 | §299, §302 syn-b, §312 | §299 (b1402), §302, §312 (b1455) | Lagrange / Trojans / Routh | **C (Lagrange)** | Background only. |
| 79 | L30 Addendum B | §39 | Lagrange dictionary | C (Lagrange) | Background only. |
| 80 | bridge1848 | bridge1848/ | Principalization writes U (the pole plane, weights 0, 2), not A; curve-level Arakelov classes are ghost-blind | C (D) | Principalization / UF only reaches the boosted plane. |

(Row 42 is a duplicate pointer. It is excluded from the counts.)

**Counts (primary bin, 79 rows):**

| Bin | Rows |
|---|---|
| D | 25 |
| S | 17 |
| E | 12 |
| C | 9 |
| P | 12 |
| N | 4 |

The check-3 local results are spread across S, E and C.

**Flagged rotating-frame / Lagrange (closed, background only):**
- L27 (Krein-collision part);
- L161;
- §297, §299, §302, §312;
- §304 (Routh / KS part);
- L30 Addendum B.

**Genuinely use multiplicativity:**
- TARGET Prop 1 (as geometry);
- L65 Fock;
- §304 UF;
- §368 Thm 3.6;
- L165;
- L187 Thm 3.5;
- L39 Prop 3.2;
- L20 / L71 (Hecke / E×E, local);
- L37;
- L106 (Hecke traces).

**None** of these yields the sign, and three of them are explicit proofs that the Euler product is insufficient: L166, §304 and §205.

## 3. Checks 1–4

1. **Epstein.** Yes, it is the right test, and it is already the standing control: §193(b) / t812u, L60, L83, L164, L169, atlas #36. Use it in the form "the *sign step* holds for Z₁". Note that the genus L has no pole plane (it is entire), and that the ζ_K / genus-L passes are GRH-numerical. L164 is the cleanest kill: KMS/Bochner compact J passes Z₁.
2. **Deligne torus.** Already in the ledger:
   - TARGET Prop 4b;
   - L42 Thm 4.4 / 6.8 / Rem 7.6;
   - L99, L100, L110, L98, L157, L163;
   - L14(g), L15, L27;
   - §369 Restatement 3.4;
   - L194(a).

   The §11 dictionary is a restatement and should cite these. L99 and L100 give the obstruction: ℚ's archimedean place is real, so the W_ℝ U(1) dies on ζ and no continuous U(1) preserves the zeros. A compact factor has to come from a weight-1 / U^⊥ object (bridge1848), not from scaling.
3. **Local data.** Ruled out:
   - L64: collective; local Hasse ⇏ global.
   - §329: every W_p is indefinite.
   - L37: no Euler factor is Schur.
   - L174 Thm I and §202 CC13′: local ellipticity is invisible to the explicit formula and stronger than RH.
   - TARGET §4: local sums.
   - L20: only the boost transfers.

   For ζ the local factors are GL₁, so there is no local J_p. Multiplicativity must enter globally, as a composition of correspondences (TARGET Prop 1).
4. **p-adic.** Explored, with a negative verdict:
   - L113 Thm 5.1: ghosts are invisible at p and to the product formula.
   - L42 §8: Newton-above-Hodge = integrality, which fakes pass.
   - L46 Prop 6.9: a fake with slopes ½, ½.
   - L23, L49, L38, L66, L126, L134, L170.
   - §347 already says "p-adic locates / archimedean signs".

   For ζ there is no p-adic H¹, and the degree-1 slope split is vacuous. "Boost p-adically" is purity, i.e. a restatement.


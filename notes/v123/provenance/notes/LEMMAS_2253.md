# TAA Lemmas 188–193 (t2253, 16–17 Nov 2026, America/Chicago)

Scratch, written by Grok Bot as checker. Previous highest lemma number on disk: **Lemma 187** (build187). Nothing here touches TARGET.md.
**RH is not proved. Φ is not constructed. No sign has been found.** None of these lemmas touches TARGET (D) ([J, Θ] = 0 on ℋ); four are diagnostics of the CCM truncated form, one is an exact restatement, one closes a question by reducing it to Weil's criterion.

Conventions (TARGET §1.1): u = log x, window [−r/2, r/2], C±(f) = ∫ f e^{±u/2}, P = 2C₊C₋, W = Q + P, E₀ = ker C₊ ∩ ker C₋.
QW := W (CCM's truncated form = Q + pole terms). J(w) = e^{|w|/2}/(2 sinh|w|) = Σ_{n≥0} e^{−(2n+½)|w|} = k_∞(|w|).
Numerics: `lemtest.py` (this folder) reuses the hp2251 sine-basis assembly (`build.py` = hp2251/sine.py with the eigen-step removed and an optional odd-character Γ-factor). All eigen-data come from parity eigendecompositions of Q plus exact secular equations for the rank-one / codimension-one problems. Every run was repeated at 2× digits at N = 100 and agreed in all printed digits. **Galerkin caveat (applies to every numerical row):** Rayleigh–Ritz eigenvalues are upper bounds for the true ones; a positive Galerkin minimum does not certify positivity on the window, and a Galerkin negative count is only a lower bound for the true index. For r ≥ 2.5 the tiny eigenvalues still fall with N (not converged).

---

## Lemma 188 (PROVED). The plastic-number threshold for CCM's form

**Statement.** Let K(w) = −J(w) + 2cosh(w/2) (w ≠ 0), the smooth off-diagonal kernel of QW on a window. Then
K(w) = e^{|w|/2} − Σ_{n≥1} e^{−(2n+½)|w|} = e^{|w|/2} − e^{−5|w|/2}/(1 − e^{−2|w|}),
and K(w) ≤ 0 ⇔ |w| ≤ w₀ := log P, where P = 1.32471795724… is the plastic number (the unique real root of y³ = y + 1). w₀ = 0.28119957432296…
Consequently, for window length r ≤ log P (CCM λ = e^{r/2} ≤ √P = 1.15096…, Suzuki a = r/2 ≤ 0.14060…), QW is a Beurling–Deny (pure-jump Dirichlet) form plus a potential **bounded below**, its lowest eigenvalue is simple, and the ground state is strictly positive and even (no primes enter before log 2).

**Proof.** 2cosh(w/2) = e^{|w|/2} + e^{−|w|/2}; the n = 0 term of J cancels e^{−|w|/2}. With y = e^{|w|} > 1, K ≤ 0 ⇔ e^{|w|/2} ≤ e^{−5|w|/2}/(1 − e^{−2|w|}) ⇔ y³(1 − y^{−2}) ≤ 1 ⇔ y³ − y − 1 ≤ 0. The cubic has discriminant −23 < 0, so one real root, P; it is increasing for y > 1/√3, so on y > 1 it is ≤ 0 exactly on (1, P]. (The form y² = (y+1)²(y−1) is the same cubic: (y+1)²(y−1) − y² = y³ − y − 1; P⁵ − P⁴ = 1 is equivalent.) For the form: QW(f) = ½∬_{W²}(f(u)−f(v))² j(u−v) + ∫_W V f², with j = J − 2cosh(·/2) ≥ 0 (and > 0 for 0 < |w| < log P), V = K₀ + κ + m, κ(u) = ∫_{|v|>r/2} J(u−v)dv ≥ 0 (log-divergent at the edges), m(u) = ∫_W 2cosh((u−v)/2)dv bounded. So V ≥ K₀: bounded below, not bounded. Beurling–Deny + irreducibility (j > 0 on the window) + Perron–Frobenius–Faris (Reed–Simon IV, XIII.43–44) give a simple lowest eigenvalue with a strictly positive eigenfunction; reflection symmetry makes it even. A positive function is not odd, so the lowest eigenvalue is even and simple (CCM's even-simplicity) on these windows. Positivity of the eigenvalue is not claimed (Suzuki proves it for small a). ∎ (Functional-analytic details as in de Andrade Silva, Zenodo 20682833, Thm "Unconditional Perron structure", which handles the same log-divergent potential.)
**Check.** `plastic.py`: K(log P) = 0 to 50 digits; closed form agrees with K to 1e−48; exactly one sign change of K on (0, 5], at 0.2811.
**Priority.** The value t* = 0.28119957… and the restriction a ≤ t*/2 ≈ 0.1406 are already in de Andrade Silva (Zenodo 20682833, 13 Jun 2026, §2, with the defining equation 2cosh(t*/2) = e^{−t*/2}/(1 − e^{−2t*})). His tex has no closed form. **The identification t* = log P (plastic number) appears to be the only new item.** Not checked: whether Suzuki's paper states it.
**Bearing.** Diagnostic for the CCM approximants only. Ghost-blind (depends only on Γ_ℝ and the poles). Does not touch (D).

## Lemma 189 (PROVED, elementary; restatement). Single-null-hyperplane form of Weil's criterion

**Statement.** RH ⇔ for every window, Q ≥ 0 on ker C₊ ⇔ for every window, Q ≥ 0 on ker C₋. For a fixed window: W ≥ 0 on L²(window) ⇒ Q|ker C₊ ≥ 0 ⇒ Q|E₀ ≥ 0. The two hyperplane problems are unitarily equivalent (u ↦ −u swaps C₊ and C₋ and fixes Q), so their spectra coincide exactly.
**Proof.** P = 2C₊C₋ vanishes on ker C₊, so Q = W there. E₀ ⊂ ker C₊ ⊂ L²(window). Weil: RH ⇔ W ≥ 0 on all windows ⇔ Q ≥ 0 on E₀ for all windows (TARGET §1.1). Sandwich. ∎ No index formula is needed (the manuscript's "sketch using the index formula" is unnecessary).
**Quantitative (Cauchy interlacing, exact):** e₀(W) ≤ min(Q|ker C₊) ≤ (second eigenvalue of W) = o₀(W) (numerically the lowest odd eigenvalue of W is the second one), and min(Q|ker C₊) ≤ min(Q|E₀).
**Test (Table Z).** min(Q|ker C₊) = (0.96–0.999)·o₀(W) at every r = 0.28–5, stable in N to 4 digits for r ≤ 2; it sits below min(Q|E₀) by a factor 1.5 (r = 0.28), ≈ 60 (r = 1), ≈ 10⁴ (r = 3–5); for r ≥ 1 min(Q|E₀) equals the second eigenvalue of Q to all printed digits (pole constraints inactive, TARGET §1.3). So the single hyperplane removes W's even Perron direction but not its odd one: as a numerical diagnostic it has a smaller margin than E₀, and as a criterion it is equivalent, not stronger.
**Classification.** Restatement (exact). Not a mechanism. Does not touch (D).

## Lemma 190 (EXACT correction + framing). Exponent bookkeeping of the archimedean jump kernel

**Statement.** The exponents of J are 2n + ½ = ½ − s_n with s_n = −2n, n ≥ 0: the poles of Γ(s/2). The n = 0 term (s = 0) is **not a trivial zero** (ζ(0) = −½); it is the pole of Λ(s) = π^{−s/2}Γ(s/2)ζ(s) at s = 0, the same pole that P records. The trivial zeros are n ≥ 1. Lemma 188's cancellation is therefore pole-against-pole (the Γ-pole term e^{−|w|/2} against the e^{−|w|/2} part of P's kernel), and the obstruction is P's growing branch e^{|w|/2} against the genuine trivial zeros n ≥ 1.
**Coadjoint reading.** Matching Casimirs E = s(1 − s) = ¼ − k², k = ½ − s: s = −2n corresponds to the discrete series D_m of weight m = 2(1 − s) = 4n + 2 (weights 2, 6, 10, …); n = 0 is weight 2 (Casimir 0, shared with the trivial representation). This is a Casimir (numerological) match, not a representation-theoretic derivation of the kernel. The positivity of J is complete monotonicity of the Γ-factor (Lévy–Khintchine for log Γ; atlas `arch_levy_khintchine_sos`; de Andrade Silva Prop. 1). For an odd character the same construction gives exponents 2n + 3/2 (Γ_ℝ(s+1)). The kernel depends only on the Γ-factor, so it is ghost-blind (Davenport–Heilbronn has the same kind of kernel).
**Classification.** Manuscript §8.1 "the exponents are the trivial zeros" is wrong at n = 0 (and inconsistent with its own §8.2 and Fig. 4, where k = ½ is the pole). "Inside-cone orbits [Ours, exact]" should be [Framing]. Does not touch (D).

## Lemma 191 (PROVED reduction + NUMERICAL). Odd-sector scalar criterion for even-simplicity

**Statement.** Write QW_even = Q_e + 2|c⟩⟨c| (c = C₊ = C₋ on even functions, c ↔ cosh(u/2)) and QW_odd = Q_o − 2|s⟩⟨s| (s ↔ sinh(u/2)). Let e₀ be the lowest even eigenvalue of QW. If e₀ < min spec Q_o, then
e₀ < o₀ := min spec QW_odd ⇔ S(r) := 1 − 2⟨s, (Q_o − e₀)^{−1} s⟩ > 0.
**Proof.** On (−∞, min spec Q_o), h(μ) = 1 − 2⟨s,(Q_o − μ)^{−1}s⟩ is strictly decreasing from 1 to −∞ (provided ⟨s, ground of Q_o⟩ ≠ 0), and its unique zero there is o₀ (rank-one secular equation). ∎ This is the odd-sector counterpart of de Andrade Silva's even-sector Krein reduction (Zenodo 20682833, Cor. "krein": eigenvalues of the even sector solve 1 + 2⟨C,(Ã−λ)^{−1}C⟩ = 0, plus a nodal condition on (Ã−λ₀)^{−1}C). The nodal part is already observed (0 sign changes, hp2251); S(r) > 0 is the remaining ordering condition.
**Test (Table Z).** S(r) > 0 at every r = 0.28, 0.6, 1, 1.2, 1.5, 2, 2.5, 3, 4, 5 and every N = 50/100/150; e₀ < min spec Q_o holds in every run; S(r) agrees between dps and 2·dps in all digits. S(0.28) ≈ 0.9989, S(1) ≈ 0.0098–0.0108, then S falls with o₀ (S/o₀ ≈ 20–50). o₀/e₀ ≈ 3.9 (r = 0.28), 29 (0.6), ~210 (1), ~370 (1.2), ~920 (1.5), ~2.5·10³ (2), 3·10³–1.2·10³ (r = 3–5, N-dependent).
**Classification.** Numerical diagnostic for the CCM approximants. Not a proof for any r > log P. Does not touch (D).

## Lemma 192 (PROVED; closes the manuscript's §11 "to check"). The Hilbert-transform J does not empty (D)

**Statement.** On L²(ℝ) (u-line) let H = −i sgn(D). Then H² = −1, H is orthogonal, and [H, Θ_t] = 0 for all t. For a translation-invariant form B(f, g) = (1/2π)∫ b(ξ) f̂ ḡ̂ dξ, ω_B(f, g) := −B(f, Hg) is antisymmetric (B(Hf, g) = −B(f, Hg) because b is real and even) and ω_B(f, Hg) = B(f, g), so B is the metric g of the pair (ω_B, H); **g > 0 ⇔ b ≥ 0**. For the Weil distribution on the full line, b is the zero distribution of ζ (Σ_ρ δ_{γ_ρ} in the sense of the explicit formula), and b ≥ 0 as a measure on ℝ ⇔ all γ_ρ real ⇔ RH (Bochner / Weil). So with J = H, (C) and (D) hold for free and all content moves to positivity of the symbol, which is Weil's criterion verbatim.
**Proof.** H is the Fourier multiplier −i sgn ξ; translations are multipliers e^{−itξ}; multipliers commute. Antisymmetry and compatibility follow because b is even and real; positivity of a translation-invariant form is positivity of its symbol. ∎
**Why this is not (D).** (i) H acts on the test space (E₀-level), not on ℋ; TARGET C6/C7/C12 relocated J to ℋ, and Q is the Level-2 trace form tr(Φ(F)Φ(F)^∨). (ii) ω := W(·, H·) is built from W, the circular case (t2154). (iii) On windows H leaks out of the support and does not preserve E₀ (atlas `nonstationary_J_obstruction`, #518). Closed route: TARGET §4 row "Hilbert J on E₀".
**Bearing.** Answers the manuscript's open note; negative.

## Lemma 193 (EXACT + NUMERICAL). L(s, χ₄): Markov range log 3 and the pole-free ground state

**Statement.** For χ₄ (odd, conductor 4) the Weil form has no pole terms; its archimedean part has K₀^χ = ψ(¾) + log(4/π) = 0.1562… and jump kernel J_χ(w) = Σ_{n≥0} e^{−(2n+3/2)|w|} > 0 (Γ_ℝ(s+1)); prime atoms −χ(n)Λ(n)n^{−1/2}(δ_{log n} + δ_{−log n}). Off-diagonal entries are ≤ 0 except at n with χ(n)Λ(n) < 0, the first being n = 3. So the form is Beurling–Deny (+ potential bounded below) exactly for r ≤ log 3 = 1.0986…, and its ground state is simple, strictly positive and even there. (Proof as in Lemma 188.)
**Test (Table C).** Galerkin minima (N = 100): 0.3179 (r = 0.8), 0.1427 (1), 0.0780 (1.09), 0.0354 (1.2), 2.143·10⁻³ (1.5), 6.83·10⁻⁷ (2); and 4.70·10⁻¹³ (2.5), 2.12·10⁻²³ (3), 1.34·10⁻⁵⁶ (4; N = 150 gives 8.1·10⁻⁶⁶, not converged); ground even and nodeless at every r, no negative Galerkin eigenvalue, lowest odd 10²–10⁴ times above the even ground state (2 × digits identical at N = 100). So the even-below-odd pattern of ζ's QW also holds without any pole plane. The manuscript's numbers (0.322, 0.145, 0.080, 0.036, 2.2·10⁻³, 7.2·10⁻⁷) match our N = 50 values (0.3206, 0.1453, 0.0805, 0.0364, 2.27·10⁻³, 7.27·10⁻⁷), i.e. they are small-basis upper bounds 1–6% above N = 100. This confirms they used the correct odd Γ-factor.
**Bearing.** Consistent with TARGET's N-L necessary condition (κ = 0 without a pole plane). Diagnostic only; does not touch (D).

---

## Proposed atlas/TARGET handling
- Lemmas 188–193 go into atlas v1.23 as new concepts (staged, see atlas2253).
- TARGET rows are proposed in REVIEW_ms2253v2.md §C and are **not applied**.
### Table Z: zeta, sine basis (hp2251 assembly), parity eigendecompositions + secular equations

| r | N | dps | Q q0 | min Q on E0 (= Q q1 for r ≥ 1) | n-(Q) | QW e0 | QW o0 | o0/e0 | S(r) | min Q on ker C+ | ratio to o0 | cos(Q-ground, cosh) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.28 | 50 | 60 | -0.27548188 | 1.4619263 | 1 | 0.25752301 | 0.99995881 | 3.88 | 0.9989052684 | 0.99880579 | 0.99885 | 0.984424 |
| 0.28 | 100 | 60 | -0.27912456 | 1.4588817 | 1 | 0.25574915 | 0.99689 | 3.9 | 0.9988922255 | 0.9957314 | 0.99884 | 0.984193 |
| 0.28 | 100 | 120 | -0.27912456 | 1.4588817 | 1 | 0.25574915 | 0.99689 | 3.9 | 0.9988922255 | 0.9957314 | 0.99884 | 0.984193 |
| 0.28 | 150 | 60 | -0.28036407 | 1.4578174 | 1 | 0.25514088 | 0.99581102 | 3.9 | 0.9988877019 | 0.99465052 | 0.99883 | 0.984122 |
| 0.6 | 50 | 60 | -1.1121133 | 0.69836654 | 1 | 0.0081099017 | 0.22916614 | 28.3 | 0.9661792308 | 0.22746517 | 0.99258 | 0.984987 |
| 0.6 | 100 | 60 | -1.1160146 | 0.69531187 | 1 | 0.0078517318 | 0.22601638 | 28.8 | 0.9654270746 | 0.22432527 | 0.99252 | 0.984759 |
| 0.6 | 100 | 120 | -1.1160146 | 0.69531187 | 1 | 0.0078517318 | 0.22601638 | 28.8 | 0.9654270746 | 0.22432527 | 0.99252 | 0.984759 |
| 0.6 | 150 | 60 | -1.1173411 | 0.69424417 | 1 | 0.0077615573 | 0.22490929 | 29 | 0.9651601816 | 0.22322182 | 0.99250 | 0.984688 |
| 1 | 50 | 60 | -1.9734707 | 0.0134952 | 1 | 1.05001e-6 | 0.00022503942 | 214 | 0.01077478257 | 0.00022144305 | 0.98402 | 0.995360 |
| 1 | 100 | 60 | -1.980368 | 0.012719209 | 1 | 1.0055094e-6 | 0.0002111613 | 210 | 0.01009123015 | 0.0002077806 | 0.98399 | 0.995138 |
| 1 | 100 | 120 | -1.980368 | 0.012719209 | 1 | 1.0055094e-6 | 0.0002111613 | 210 | 0.01009123015 | 0.0002077806 | 0.98399 | 0.995138 |
| 1 | 150 | 60 | -1.9827294 | 0.012440427 | 1 | 9.8444541e-7 | 0.00020592612 | 209 | 0.009834596634 | 0.00020262716 | 0.98398 | 0.995071 |
| 1.2 | 50 | 60 | -2.3961403 | 7.7896632e-5 | 1 | 1.8143238e-9 | 6.9509155e-7 | 383 | 2.886014433e-5 | 6.8278094e-7 | 0.98229 | 0.997614 |
| 1.2 | 100 | 60 | -2.4063325 | 7.3248188e-5 | 1 | 1.7670687e-9 | 6.6038171e-7 | 374 | 2.738136821e-5 | 6.4867366e-7 | 0.98227 | 0.997531 |
| 1.2 | 100 | 120 | -2.4063325 | 7.3248188e-5 | 1 | 1.7670687e-9 | 6.6038171e-7 | 374 | 2.738136821e-5 | 6.4867366e-7 | 0.98227 | 0.997531 |
| 1.2 | 150 | 60 | -2.4097889 | 7.1194489e-5 | 1 | 1.729889e-9 | 6.4304502e-7 | 372 | 2.66469914e-5 | 6.3163968e-7 | 0.98226 | 0.997503 |
| 1.5 | 50 | 60 | -3.0766033 | 8.4574583e-10 | 1 | 4.8379269e-15 | 4.0050962e-12 | 828 | 1.434442261e-10 | 3.9269131e-12 | 0.98048 | 0.998137 |
| 1.5 | 100 | 60 | -3.0886363 | 8.1768075e-10 | 1 | 4.01479e-15 | 3.7151677e-12 | 925 | 1.33060495e-10 | 3.642642e-12 | 0.98048 | 0.997992 |
| 1.5 | 100 | 120 | -3.0886363 | 8.1768075e-10 | 1 | 4.01479e-15 | 3.7151677e-12 | 925 | 1.33060495e-10 | 3.642642e-12 | 0.98048 | 0.997992 |
| 1.5 | 150 | 60 | -3.0926921 | 8.0628977e-10 | 1 | 3.9863972e-15 | 3.6799282e-12 | 923 | 1.317804559e-10 | 3.6080819e-12 | 0.98048 | 0.997945 |
| 2 | 50 | 80 | -4.2653264 | 3.283445e-23 | 1 | 2.110141e-29 | 5.0866213e-26 | 2.41e+03 | 1.583884661e-24 | 4.9778982e-26 | 0.97863 | 0.998668 |
| 2 | 100 | 80 | -4.2854859 | 1.8035798e-23 | 1 | 7.6622035e-30 | 1.880113e-26 | 2.45e+03 | 5.859166546e-25 | 1.8399526e-26 | 0.97864 | 0.998619 |
| 2 | 100 | 160 | -4.2854859 | 1.8035798e-23 | 1 | 7.6622035e-30 | 1.880113e-26 | 2.45e+03 | 5.859166546e-25 | 1.8399526e-26 | 0.97864 | 0.998619 |
| 2 | 150 | 80 | -4.292914 | 1.6287592e-23 | 1 | 6.8154811e-30 | 1.7595001e-26 | 2.58e+03 | 5.483416738e-25 | 1.7219162e-26 | 0.97864 | 0.998653 |
| 2.5 | 50 | 120 | -5.6176474 | 2.1080307e-36 | 1 | 1.6656548e-42 | 2.0894739e-39 | 1.25e+03 | 5.734586959e-38 | 2.0411939e-39 | 0.97689 | 0.999347 |
| 2.5 | 100 | 120 | -5.6424399 | 8.9229729e-47 | 1 | 7.9392482e-54 | 3.3314493e-50 | 4.2e+03 | 9.629085386e-49 | 3.2568045e-50 | 0.97759 | 0.999256 |
| 2.5 | 100 | 240 | -5.6424399 | 8.9229729e-47 | 1 | 7.9392482e-54 | 3.3314493e-50 | 4.2e+03 | 9.629085386e-49 | 3.2568045e-50 | 0.97759 | 0.999256 |
| 2.5 | 150 | 120 | -5.6509609 | 1.4932594e-47 | 1 | 7.2599189e-55 | 5.5051964e-51 | 7.58e+03 | 1.593181484e-49 | 5.3818997e-51 | 0.97760 | 0.999218 |
| 3 | 50 | 160 | -7.1462461 | 8.3471551e-46 | 1 | 7.6614035e-52 | 1.840245e-49 | 240 | 4.333269427e-48 | 1.7937761e-49 | 0.97475 | 0.999506 |
| 3 | 100 | 160 | -7.1924479 | 9.6919155e-69 | 1 | 1.239493e-75 | 2.1787376e-72 | 1.76e+03 | 5.845967646e-71 | 2.1276307e-72 | 0.97654 | 0.999582 |
| 3 | 100 | 320 | -7.1924479 | 9.6919155e-69 | 1 | 1.239493e-75 | 2.1787376e-72 | 1.76e+03 | 5.845967646e-71 | 2.1276307e-72 | 0.97654 | 0.999582 |
| 3 | 150 | 160 | -7.204438 | 2.7558125e-81 | 1 | 7.8746312e-89 | 2.9550092e-85 | 3.75e+03 | 8.14014391e-84 | 2.8867681e-85 | 0.97691 | 0.999552 |
| 4 | 50 | 250 | -11.082314 | 1.3536302e-59 | 1 | 6.3094421e-66 | 2.8790693e-63 | 456 | 4.801118866e-62 | 2.7883995e-63 | 0.96851 | 0.999843 |
| 4 | 100 | 250 | -11.156033 | 8.2416133e-99 | 1 | 8.2415979e-106 | 1.4922808e-102 | 1.81e+03 | 3.305757607e-101 | 1.4527789e-102 | 0.97353 | 0.999783 |
| 4 | 100 | 500 | -11.156033 | 8.2416133e-99 | 1 | 8.2415979e-106 | 1.4922808e-102 | 1.81e+03 | 3.305757607e-101 | 1.4527789e-102 | 0.97353 | 0.999783 |
| 4 | 150 | 250 | -11.180859 | 8.3695574e-129 | 1 | 3.1733528e-136 | 6.7167019e-133 | 2.12e+03 | 1.625889628e-131 | 6.5484968e-133 | 0.97496 | 0.999769 |
| 5 | 50 | 300 | -16.792376 | 8.080544e-70 | 1 | 5.1189202e-76 | 1.270656e-73 | 248 | 1.472681832e-72 | 1.2205487e-73 | 0.96057 | 0.999897 |
| 5 | 100 | 300 | -16.935416 | 9.2563074e-120 | 1 | 9.7605962e-127 | 8.7723965e-124 | 899 | 1.550980453e-122 | 8.505035e-124 | 0.96952 | 0.999874 |
| 5 | 100 | 600 | -16.935416 | 9.2563074e-120 | 1 | 9.7605962e-127 | 8.7723965e-124 | 899 | 1.550980453e-122 | 8.505035e-124 | 0.96952 | 0.999874 |
| 5 | 150 | 300 | -16.980939 | 9.289017e-162 | 1 | 3.3883444e-169 | 3.9934028e-166 | 1.18e+03 | 8.237923922e-165 | 3.8828658e-166 | 0.97232 | 0.999852 |

### Table C: L(s, chi_4) pole-free form (Gamma_R(s+1), conductor 4), sine basis

| r | N | dps | lowest (parity) | 2nd | n- | ground sign changes |
|---|---|---|---|---|---|---|
| 0.8 | 50 | 60 | 0.32062312e | 1.3372761o | 0 | 0 |
| 0.8 | 100 | 60 | 0.31790418e | 1.3342221o | 0 | 0 |
| 0.8 | 100 | 120 | 0.31790418e | 1.3342221o | 0 | 0 |
| 1 | 50 | 60 | 0.14527776e | 1.1147424o | 0 | 0 |
| 1 | 100 | 60 | 0.1427212e | 1.1116981o | 0 | 0 |
| 1 | 100 | 120 | 0.1427212e | 1.1116981o | 0 | 0 |
| 1.09 | 50 | 60 | 0.080454076e | 1.0290257o | 0 | 0 |
| 1.09 | 100 | 60 | 0.07796855e | 1.0259877o | 0 | 0 |
| 1.09 | 100 | 120 | 0.07796855e | 1.0259877o | 0 | 0 |
| 1.2 | 50 | 60 | 0.036432735e | 0.81684504o | 0 | 0 |
| 1.2 | 100 | 60 | 0.03542695e | 0.80714444o | 0 | 0 |
| 1.2 | 100 | 120 | 0.03542695e | 0.80714444o | 0 | 0 |
| 1.5 | 50 | 60 | 0.0022710796e | 0.20640418o | 0 | 0 |
| 1.5 | 100 | 60 | 0.0021431631e | 0.20031478o | 0 | 0 |
| 1.5 | 100 | 120 | 0.0021431631e | 0.20031478o | 0 | 0 |
| 2 | 50 | 60 | 7.2669434e-7e | 0.00037731664o | 0 | 0 |
| 2 | 100 | 60 | 6.8261954e-7e | 0.00034437828o | 0 | 0 |
| 2 | 100 | 120 | 6.8261954e-7e | 0.00034437828o | 0 | 0 |
| 2.5 | 100 | 120 | 4.7041219e-13e | 9.0857997e-10o | 0 | 0 |
| 2.5 | 100 | 240 | 4.7041219e-13e | 9.0857997e-10o | 0 | 0 |
| 2.5 | 150 | 120 | 4.6480825e-13e | 8.896018e-10o | 0 | 0 |
| 3 | 100 | 120 | 2.1245685e-23e | 1.1161266e-19o | 0 | 0 |
| 3 | 100 | 240 | 2.1245685e-23e | 1.1161266e-19o | 0 | 0 |
| 3 | 150 | 120 | 1.8813883e-23e | 9.7067467e-20o | 0 | 0 |
| 4 | 100 | 120 | 1.3438754e-56e | 5.5670014e-53o | 0 | 0 |
| 4 | 100 | 240 | 1.3438754e-56e | 5.5670014e-53o | 0 | 0 |
| 4 | 150 | 120 | 8.144554e-66e | 1.0271888e-61o | 0 | 0 |

## Since v1.22

Links are relative to the repository root (this file is included in README.md).

> **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity.** Nothing in v1.23 touches the compatibility condition (D) ([J, Θ] = 0 on ℋ). The certified E0 gaps are still the v1.21 ones (A ≤ 1.1). Every statement for A > log P is numerical (Galerkin upper bounds). Rank 1 is unchanged: `kahler_triple_polarization`. Open ~1.8 is unchanged.

Work of 14–17 Nov 2026 (America/Chicago). Counts: 1101 concepts (+13) and 2217 typed relations (+44). Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. [AUDIT.md](notes/v123/provenance/AUDIT.md) overrides the synthesis and the notes. Full text: [SYNTHESIS.md](notes/v123/SYNTHESIS.md). Lemmas with proofs and tables: [LEMMAS_2253.md](notes/v123/provenance/notes/LEMMAS_2253.md). Manuscript review: [REVIEW_ms2253v2.md](notes/v123/provenance/notes/REVIEW_ms2253v2.md).

A = window length in u = log x (window [−A/2, A/2]); C± = ∫F e^{±u/2}; W = Q + 2C₊C₋; E0 = ker C₊ ∩ ker C₋; QW = W is the truncated form of Connes–Consani–Moscovici (CCM).

### TAA Lemmas 188–193
- **L188 [Exact] Plastic-number threshold.** −J(w) + 2cosh(w/2) = e^{|w|/2} − e^{−5|w|/2}/(1 − e^{−2|w|}) ≤ 0 ⇔ e^{3|w|} − e^{|w|} ≤ 1 ⇔ |w| ≤ log P, P³ = P + 1 (plastic number), log P = 0.28119957. For A ≤ log P, QW is a jump Dirichlet form plus a potential bounded below, so its ground state is simple, positive and even. The value 0.28119957 and the bound a ≤ 0.1406 are due to de Andrade Silva (Zenodo, June 2026); the closed form is new as far as we checked.
- **L189 [Exact; Restatement] Single null hyperplane.** RH ⇔ Q ≥ 0 on ker C₊ for every window (Q = W there; E0 ⊂ ker C₊). Numerically min Q|ker C₊ ≈ 0.97 × the lowest odd eigenvalue of W, about 60× (A = 1) to 10⁴× (A = 3–5) below min Q|E0. Equivalent, not stronger.
- **L190 [Exact correction] Exponent bookkeeping.** The jump-kernel exponents 2n + ½ are the poles of Γ(s/2). n = 0 is the pole s = 0 of Λ, not a trivial zero. The discrete-series reading is a Casimir match (weights 4n + 2) [Analogy].
- **L191 [Exact reduction + Numerical] Odd-sector scalar.** Even-simplicity of QW ⇔ S(A) = 1 − 2⟨s,(Q_odd − e₀)⁻¹s⟩ > 0. S > 0 at every tested A = 0.28–5.
- **L192 [Exact; closed route] Hilbert-transform J.** On the full u-line it commutes with scaling for free; compatibility makes the metric the Weil symbol, so positivity is Weil's criterion. It lives on the test space, not on ℋ. It does not empty (D).
- **L193 [Exact + Numerical] L(s, χ₄).** No pole terms; Markov exactly for A ≤ log 3. The ground state stays even and nodeless through A = 4 (Galerkin), with the odd level 10²–10⁴ above: the even-below-odd pattern is not caused by the pole.

### CCM even-simplicity at high precision (hp2251) [Numerical]
- Sine basis up to 200 functions, 60–600 digits; every reported run is stable under digit doubling (60 digits fails at A ≥ 3).
- For A = 1–6: QW's lowest eigenvalue is even and simple with a nodeless ground state; the lowest odd eigenvalue is next, 2·10² to 1.1·10⁴ times larger; Q has one negative Galerkin eigenvalue. The eigenvalues run from about 1e−6 (A = 1) to 1e−242 (A = 6).
- **Caveats.** For A ≥ 2.5 the tiny eigenvalues still fall with the basis size: upper bounds, ordering stable. Galerkin minima are upper bounds and Galerkin negative counts are lower bounds, so nothing here is a certificate. κ = 1 cannot see off-line zeros above the verified heights.

### Literature (CCM even-simplicity)
- **[Cited]** Suzuki, arXiv:2606.09096, Thm 1.4: simple, even, positive bottom eigenvalue for sufficiently small windows; no explicit threshold.
- **[Cited]** de Andrade Silva, Zenodo 10.5281/zenodo.20682833 (13 Jun 2026): the pole term is the only obstruction to Perron structure; t* = 0.28119957; Perron for the pole-free part for all windows; even-simplicity reduced to a scalar Krein/nodal question, left open.
- **[Cited]** de Andrade Silva, Zenodo 10.5281/zenodo.20737110 (17 Jun 2026): Loewner/operator-monotone framework; the arithmetic case is the "remaining open core".
- **[Cited, proofs not checked]** Mehennaoui, Zenodo 10.5281/zenodo.23441945 (17 Oct 2026): simplicity ⇒ evenness under the reflection normalization; a windowed determinant (Hurwitz) criterion, conditional.

### Manuscript review: "Nested Hyperbolae, Null Poles, and the Missing H¹" (J.W. with Claude, v2, 16 Nov 2026)
- (i) the closed form log P is right; (ii) the single-null-hyperplane criterion is right but elementary; (iii) the "trivial-zero orbits" reading is wrong at n = 0.
- Its restatement of (D) puts J on E0 with Q as the metric. TARGET retired that reading (C6/C7/C12).
- Several "new" rows are prior work: the Perron half (de Andrade Silva; TAA L180), the κ formula, the Rindler/boost picture, Lévy–Khintchine.
- Verdict: hold as is; publishable as Arithmetic Unification VIII after the listed revisions.

### Target commentary carried into the atlas (TARGET C16, t2245)
**[Restatement]** (D) asks for a space where the ½ is a normalization, not an offset: the unitarity involution † and the functional-equation involution ∨ share a centre. Over F_q, dividing by √q does this. For GL(2) Eisenstein series the centres differ by ½, so ζ's zeros are resonances. The frozen target text is unchanged.

**Open, in order of bearing on Φ.** Unchanged from v1.22. The even-simplicity thread is a diagnostic of the CCM approximants, not a route to Φ or (D).

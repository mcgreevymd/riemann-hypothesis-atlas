# Atlas v1.20 — corrected synthesis

The Riemann Hypothesis is not proved. This note is the public reading of the 7 Nov 2026 bundle. Raw scratch notes remain in `provenance/bundle/notes/` and are historical. The parent math audit overrides them.

Rank 1 is `kahler_triple_polarization`. Open ~1.8 is unchanged. No new theorem is claimed beyond identities, citations, and two explicit counterexamples to representers.

## Aim

The programme asks for an energy, or a free energy, whose quadratic form is the Weil form W on log-window tests, with the positive part constructed independently of the zeros. Window by window, W ≥ 0 on E0 is the RH statement for that window. The aim is that this inequality should follow from a sign mechanism. It does not, yet. Calling the programme thermodynamic, or an RH-unitarity principle, names the goal. It does not establish a physical theory.

## 1. Ledger

For a window test F,

W(F) = P(F) + B(F).

P = 2(|C|² − |S|²) = 2 Re(C₊ conjugate C₋). For real F this agrees with 2 ev₊ ev₋ = 2(C² − S²). That reduction is not claimed for a general complex test.

B = H_A − M_A ‖F‖² = (1/2π) ∫ m_A |F̂|².

H_A is the sum of archimedean Lévy springs and prime springs for log n < A. Each spring is nonnegative. M_A = −K₀ + 2 Σ a_n, a_n = Λ(n) n^{−1/2}, K₀ = ψ(1/4) − log π = −5.37218.

B is defined off E0 as well as on it. W equals B on the joint kernel of the two moments, which contains E0. E0 kills P. It does not remove the diagonal. Globally E0 is dense, because the moments are unbounded on L². On one window the kernel is closed of codimension 2.

Reflection splits the pole update: the even block of W is the even block of B plus 2 c cᵀ, and the odd block of W is the odd block of B minus 2 s sᵀ.

## 2. Local product states

Each prime term is log p times (‖F‖² − ⟨F, P_p F⟩), and P_p = Σ_k p^{−|k|/2} T_{k log p} is positive semidefinite. The archimedean place is an Ornstein–Uhlenbeck tower. M_A is a sum of local means of log |x|_v, one place at a time. There is no coupling on principal ideles, so this is not a proved product-formula defect. Written over all prime powers with k log p < A, the prime contribution is 2 Σ_{p < e^A} of the local capped mean, not a single-prime expression. An observation, not a theorem: the rate (2j+1)/2 is the distance from 1/2 to the pole s = −2j of the archimedean factor. For j ≥ 1 those poles are cancelled in ξ by the trivial zeros. The pole at s = 0 survives in Λ and is the moment E0 removes.

The positive covariances are subtracted. They match the lines of the ledger. They are not a sign. That route is closed as a sign source. A positive compression that was compared with W on a few tests did not match W. The comparison is numerical. It is not a theorem that every compression fails.

One uncertified window, A = 2, G = sin⁸: arch about +0.090, p = 2 about +9.092, p = 3 about −9.001, p = 5 about −0.0016, spring total 0.1788. Rounded parts sum to 0.1794.

## 3. Semilocal trace

Connes 1999, Theorem VII.4, is the semilocal trace formula. With S containing infinity and every prime p < e^A, the twisted pairing satisfies −I_S(F, F) = W(F) − P(F) on window tests.

The weight is χ(u) = e^{−u/2}. The pairing uses χ · (f ∗ f*). The involution identity is (χ f)* = χ^{−1} f*. The ordinary star of (χ f) with itself is a different formula. The session numbers used the corrected weight. No global Euler phase c ≡ 1 is claimed.

The logarithmic derivative of the semilocal phase is the negative of the bulk symbol: a Wigner time delay. That dictionary is not Hodge positivity. A formal graph built from the bulk pairing is not a cycle class.

Under a trace-class assumption, W − P = D_c − D_{c̄} − X. The assumption is flagged. The remainder, where a number is quoted, is numerical.

## 4. Bordered inertia

Let B be a finite real symmetric invertible matrix, c ≠ 0, and q = cᵀ B^{−1} c. Then

n₋(B on c⊥) = n₋(B) − 1 + [q > 0].

The restriction is positive semidefinite if and only if n₋(B) = 0, or n₋(B) = 1 and q ≤ 0. If the index is 0, q is positive and the restriction is already positive semidefinite. The slogan “index at most 1 and q ≤ 0” is false in that case. If the index is at least 2, one constraint is not enough.

On a centered window both sectors are required: even against cosh, and odd against sinh. An even test is not E0. In the runs at A = 0.6 and A = 1 the odd block had index 0. That is numerical, not a general fact.

On a reflection-invariant finite Galerkin space with invertible blocks, B ≥ 0 on E0 if and only if both sectors pass: negative index 0, or negative index 1 with q ≤ 0.

The congruence is finite-dimensional. Self-adjointness, discrete spectrum, and the existence of B^{−1} cosh for the window operator are not proved. The vector B^{−1} c is computed from B. It is not an independent constructor.

Do not infer that B has infinite rank merely because it is unbounded. A finite-rank form built from unbounded functionals can be unbounded. High frequency is the reason a finite target fails. Re ψ(1/4 + ix/2) tends to infinity and the cosine sum is bounded, so m_A is at least 1 outside some frequency X. The time-band-limiting operator K_X is compact on the window. On a finite-codimension subspace where that compression is small, B is positive definite, and that subspace still meets smooth E0 in an infinite-dimensional set. A map into a finite-dimensional V cannot reproduce W. The same estimate yields only finitely many negative directions on one window. That is not Weil positivity and not a proximity claim.

Session numbers, uncertified. The absolute cosine of the angle between cosh and a computed even mode is about 0.970 at A = 0.6, 0.991 at A = 1, and 0.997 at A = 2. These are not squared overlaps. The width-2 cosine sits in the unresolved cluster and is not an eigenvalue. E0 minima are estimates, not certified brackets: Ritz upper estimates about 0.697 and 0.01315, and lower-bound-inspired values about 0.6919 and 0.0119. At A = 2 one basis shows a cluster near 10^{−3} and another near 10^{−15}. Neither is quoted as an eigenvalue. There is no certified gap.

## 5. Two representers

The identity B(h, ·) = κ C on smooth E0 tests holds if and only if the response lies in span{cosh, sinh} on the open window.

h₁ = cosh(u/2) on the window fails at A = 0.6 and at A = 1. The proof splits the integral at a fixed small a₀. The untruncated comparison with the smooth continuation of cosh diverges, because the integrand tends to −cosh(v/2) at infinity. From a₀ outward, h₁ is bounded and compactly supported, so that piece stays bounded. On the short interval the missing translate produces (cosh(L/2)/2) log(1/d) plus a bounded term. A multiple of cosh stays bounded. The recorded rise is about 0.689 to 0.691 per factor of four in d, against (1/2) log 4 = 0.693.

h₂, the Dirichlet cosh, is in the form domain. At A = 1 the only prime power inside the window is 2, and the response has slope jump a₂ sinh(A/4)/2 = 0.06191 at ±(log 2 − A/2). A combination of cosh and sinh has no jump. A finite difference at spacing 10^{−4} gives 0.06189. At a general width, shifts may cancel. No claim is made. At A = 0.6 the residual is 6.92 percent, numerical only.

The polynomial tests F = (∂² − 1/4)G with G = (1 − t²)² t^k are piecewise polynomial. They are not smooth. They lie in E0 because G and G′ vanish at the edges. They disprove the identity on the form domain. The smooth disproof of h₁, and of h₂ at A = 1, uses the annihilator lemma. Density of smooth E0 tests in the form domain is not proved.

Only these two candidates fail. A finite singular orbit for every representer, a universal 1/log law, and a Gamma-only no-go are conjectures.

## 6. One form, as a model

On coordinates (T, Q, Z), the form T² − 4 Q Z has signature with one negative square. The null set is a smooth conic. In the affine chart it is q = t²/4. That curve is a discriminant boundary of the model. It is not the parabolic wall, not the Routh wall, not the Beurling-pencil Hasse wall, and not a sheet of Σ. Those four stay separate nodes.

h = (0:1:1) has Q(h) = −4. On its polar, the form is v_T² + 4 v_Z², positive definite. x_∞ = (0:1:0) is null, and its polar is Z = 0, which does not meet the affine chart. The conic is smooth there. It is not a modular cusp. Focus and directrix are extra Euclidean structure of the parabola.

The family h_s = (0, 1, s) has homogeneous value Q = −4s. The affine point at height q = 1/s has value Q = −4/s. For s = 0.05 those numbers are −0.2 and −80. The sign is negative in both gauges, and the projective limit is x_∞. The magnitudes are not a single measurement.

On the polar v_Z = −s v_Q the form is v_T² + 4 s v_Q². The level set equal to 1 is an ellipse and tends to the lines v_T = ±1. The filled sublevel, the set where the form is at most 1, tends to the strip |v_T| ≤ 1. The level set does not become the strip.

On a curve, E is alternating. On the product, I(a⊗b, c⊗d) = −E(a, c) E(b, d). For area 1, the mixed real primitive vector of type (1,1) squares to −8, and the real vector in types (2,0) and (0,2) squares to +8. Not every class is negative.

Sylvester’s law on this finite matrix is the shape the missing theorem asks for. The conic does not construct h. A fixed finite H^{1,1} cannot carry W, by the high-frequency argument in §4, not because every unbounded form has infinite rank. The Hodge index used as a cited pattern is Hartshorne, Algebraic Geometry, GTM 52, Chapter V, Theorem 1.9. The harmonic-form sign is the Hodge–Riemann bilinear relations; Huybrechts, Complex Geometry, or Griffiths and Harris, Chapter 0, are chapter-level pointers. Those pages were not re-opened here. Wikipedia is not the source.

## 7. Calibrations

A translation-invariant compatible J exists for a nonnegative symbol: the Hilbert transform. It does not preserve compact support or E0, so a window J would have to be non-stationary. None is built.

The Ramanujan system, the Serre and Maass operators, E₁₀ = E₄ E₆, B₁₀ = 5/66, and the Wronskian identity were checked symbolically in the session. The weight formula 2(ψ(k/2) − log 2π) is not k/12. Weight 12 does not select K₀. Sigma-convexity of log |ξ| fails near the zeros. Both routes stay closed.

Λ = ℤ_p[[T]] is regular local of dimension 2, and the quotient by f is regular exactly when f is nonzero in m/m². The Iwasawa numbers μ, λ, ν are growth invariants, not that class, and not a sign. A regular local ring is a UFD. ℤ[√−5] is Noetherian and not a UFD, since no element has norm 2 and 6 has two irreducible factorizations. Noetherian is not a Noether charge. This toy does not reopen a Jacobian, Rosati, or Picard path.

Rankin–Selberg unfolding writes ∫ y¹² |Δ|² E(z, s) as a Gamma factor times Σ τ(n)² n^{−(s+11)}. The Petersson norm of Δ is finite and positive. Cusp decay makes the integral converge. Square coefficients are not W.

## 8. Missing theorem

On one window, with the form domain and an invertibility hypothesis stated, construct h_A from Gamma data, prime data, and the boundary, independently of B^{−1}, such that:

1. B(h_A, F) equals the moment constraint for every window F, including M_A and the prime-translated edge layers;
2. B(h_A, h_A) < 0;
3. the even sector has negative index 1 and q_even ≤ 0, or index 0, and the odd sector satisfies the same alternative.

(1) and (2) and (3) give B ≥ 0 on that finite model of E0 by the bordered count. (3) is the RH-strength half. The sharp question left open is whether, when B^{−1} cosh exists, it equals cosh minus a finite sum of edge profiles. That remains a conjecture. Any geometric home for W has to be infinite-dimensional, or an ind-limit with a stated domain. It is not built.

The Riemann Hypothesis is not proved.

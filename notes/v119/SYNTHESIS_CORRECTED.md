# Springs, a hyperbolic boundary, and a missing independent sign

Night of 6 Nov 2026, integrated 7 Nov 2026. J. W. McGreevy; formalization by Grok Bot.

**The Riemann Hypothesis is not proved.** What follows is a structural refinement of a target the atlas already states, together with consistency tests. It is not a new independent positivity theorem. No ample class, no compatible complex structure J, and no metric that reproduces the Weil form W were constructed.

Labels: **exact** (an identity checked here, or a cited theorem), **numerical** (finite, with the certificate rule below), **analogy**, **prior**, **open**.

## How to read the numbers

A positive value of a finite Galerkin minimum is an upper bound on the smallest eigenvalue of that matrix. It is not a certificate that the form is positive, and a run at K = 8 does not control the limit as the basis grows.

A negative Rayleigh quotient on an explicit vector is a strong numerical witness that the matrix is indefinite, inside the arithmetic and quadrature error of that run. Call it certified only when a rigorous error bound is attached. This integration does not attach one.

Do not put K = 12 and K = 14 on the same legend. In the spring scripts, A is the full width of the interval [−A/2, A/2]. In the boundary checks, L is the half-width of [−L, L]. Read the interval, not the letter.

## Analogy

Think of W as the energy of many springs, minus a counterterm. Each spring is a squared difference of a test function and a translate, weighted by a nonnegative density: the archimedean Lévy density, or a prime weight a_n = Λ(n) n^{−1/2}. The counterterm M ‖F‖² collects the diagonal of those squares, with M = −K(0) + 2 Σ a_n and K(0) = Re ψ(1/4) − log π.

On the pole annihilator the pole term is off, so W ≥ 0 for every test function if and only if the spring energy dominates the counterterm. That global comparison is the target. It is Weil positivity rewritten. A margin that shrinks toward zero, as the windows in the Galerkin runs do, is a picture of how tight the balance is. It is not a proof, and it is not a disproof.

The same quadratic form can be grouped another way. After the diagonal has gone into M, each prime leaves a term −2 a_n ρ(log n), where ρ is the autocorrelation. That term helps or hurts with the sign of ρ. The spring energy itself stays nonnegative. Those are two statements. They must not be collapsed into “the primes have a sign” or into “there is no domination.”

Famous positivity machines — a quantum covariance, a Bogomolny bound, the Hodge index over a finite field, the no-ghost theorem — are related architectures. They are not the single identity “every mechanism is a square plus an indefinite boundary.”

## 1. The spring identity (exact, and prior in pieces)

For real F supported in a window of full width A, and N ≥ e^A,

W(F) = P(F) + ∫₀^∞ k_∞(a) ‖F − T_a F‖² da + Σ_{n≤N} a_n ‖F − T_{log n} F‖² − M_N ‖F‖²,

with k_∞(a) = e^{−a/2} / (1 − e^{−2a}), M_N = −K(0) + 2 Σ_{n≤N} a_n, and P the pole term. The tails cancel on that window. Each summand of the spring energy is ≥ 0.

The archimedean Lévy representation K(r) = K(0) + 2 ∫ k_∞(a) (1 − cos r a) da is prior (atlas entries on the Lévy kernel and the jump-minus-mass split). Completing the square for the prime translations is the same quadratic form, not a new inequality.

Equivalently, as a Rayleigh quotient,

W(F)/‖F‖² = K(0) + ∫ k_∞(a) (2 − 2ρ(F, a)) da − 2 Σ a_n ρ(F, log n).

The weight (2 − 2ρ) is nonnegative. The coefficient −2 a_n ρ is the signed net prime contribution. The map from weights (K(0), k_∞, a_n) to the bottom of the spectrum is concave, so the set of weights that stay nonnegative is convex. That is a fact about this family of forms. It does not decide membership for the arithmetic weights.

An explicit anharmonic functional, a quadratic spring potential plus a quartic, has Hessian at the origin equal to W. Away from the origin the Hessian is W plus a nonnegative quartic term. A Hessian identity restates W.

**Numerical, K = 8, exact-E0 basis, reproduced in this integration.** Smallest Rayleigh quotient of W: full width A = 1 gives 0.0673395762411; A = 2 gives 1.65055568024×10⁻⁸. Both are positive upper bounds. The mass M is about 6.35 and 11.22. The same script’s session notes at other K show the minimum still falling. Those notes are not a controlled limit, and they are not this K = 8 series.

Session notes at A = 3, K = 12, record that dropping any single prime n ≤ 13 produced a negative direction on that basis. Treat that as a strong numerical witness of those matrices, not as a certified eigenvalue.

Hat-basis runs (spacing 0.05) give different minima, for example about 1.7×10⁻² at full width 1. They are a third legend. Do not mix them with K = 8 or K = 12.

The older atlas sentence that “no domination argument can work” remains true of a uniform spectral gap: the margin closes, and a surplus independent of the test function is not on offer. It is not a ban on the identity W = E_springs − M ‖F‖². That identity is the domination target, and it is open.

## 2. Boundary, density, and a prior bijection (exact)

Let b(f) = (f(0), ∫ f). Fourier transform swaps the two coordinates. Unitary scaling U_a multiplies them by |a|^{−1/2} and |a|^{1/2}. The only Hermitian forms invariant under all of these scalings and under the swap are real multiples of [[0, 1], [1, 0]]. Signature (1, 1), or the zero form, which is degenerate. The Weil pole term is of this hyperbolic type. The boundary cannot be the source of a positive sign.

E0, the kernel of the two Mellin moments at s = 0 and s = 1, is a convolution ideal and is stable under the sharp involution. The moment functionals are unbounded on L², so E0 is dense. Smooth functions in E0 are not an L²-closed subspace. There is no global orthogonal projection onto a pole-free subspace of L².

On one fixed window the exponentials e^{±u/2} lie in L², so the kernel is closed and has codimension 2. The orthogonal projection exists and depends on the window. “Removing the poles” globally is the moment map b, or that window projection. It is not one L²-orthogonal projection for the whole line.

The operator L = ∂² − 1/4 bijects compactly supported smooth functions onto E0 in that class and preserves support hulls, and positivity of W on the window intersection with the ideal is equivalent to positivity of the transported form. That is Connes–Consani 2021, Lemma 3.3 and Proposition 3.5 (**prior**). This integration does not claim it as a new theorem.

On the core with the reference form G0, the pair (Q0, D) with Q0 = L Q L^{−1} is the Schrödinger representation relabelled, and the commutator identities hold there. A fixed window still needs a boundary condition before an operator is self-adjoint. A real convolution by F is self-adjoint only when F^♯ = F. Translations commute with each other. A noncommutative enlargement is needed if one wants a nonzero Robertson–Schrödinger commutator. It is not needed for an independent positive functional.

Finite-field Frobenius graphs, normalized by q^{−n/2}, have boundary pairings (q^{−n/2}, q^{n/2}). That is the same diagonal law. They are discrete samples. They are not the continuous Mellin moments.

## 3. What the cousins actually use (analogy, with exact pieces)

**Robertson–Schrödinger.** A positive state gives a positive matrix of covariances. Reading W as such a covariance asks for a state or a weight whose two-point function is W. A commutative positive functional can be independent of the zeros: a positive-definite distribution is the Fourier transform of a positive tempered measure (Bochner–Schwartz). The old “Bochner trap,” that commutativity would forbid an independent functional, is withdrawn. Noncommutativity is needed only for a nonzero commutator term. W is unbounded, so it is not a normalized state on the algebra of bounded translations. The object, if it exists, is a positive weight on the test-function algebra, with domains. Neither that weight nor the reference form G0 is selected by positivity alone. A positive representation does not pick W.

**Heisenberg’s 1925 termination.** The ladder stops where a squared amplitude would become negative. The sign is the Hilbert-space norm of the amplitudes, not a property of the ladder symbols. This is background, as read in the session against Aitchison, MacManus, and Snyder, American Journal of Physics 72 (2004) 1370. It is not re-opened here, and it is not a construction for W.

**Bogomolny.** Pointwise, |F|² ∓ (F ∧ F)/vol = 2 |F^∓|². The topological charge labels a sector; its Hessian vanishes for compactly supported variations. At a Bogomolny point the Hessian of the completed functional is twice a square. Non-Bogomolny critical points in the same sector can be unstable. The norm comes from the metric.

**Hodge, two geometries.** On a Kähler surface, a primitive real (1, 1) form is anti-self-dual, so α ∧ α = −|α|² vol. That is Riemannian geometry of a complex surface. Integrality of a Chern class does not give ampleness (the blow-up of the plane at a point, with D = 2H + E, has D² = 3 and D · E = −1). On an algebraic surface over a finite field the sign is the Hodge index theorem for the intersection form. Those are related. They are not the same theorem, and neither is “the” unique source of a sign. Positive representations, metrics, and positive states also produce signs.

**Finite-field control (exact).** On E × E, with b(D) = (D · v, D · h), one has D² = 2 b₀ b₁ + D_⊥². The perpendicular Gram in the usual basis is [[−2, −a], [−a, −2q]]. It is negative semidefinite if and only if a² ≤ 4q (151 trace values in the reproduced scan). The determinant 4q − a² is positive for negative-definite examples. Inertia decides the sign; the determinant sees degeneracy. This reproduces the Hodge-index sign already in the atlas (TAA Lemma 162). It detects nothing about ζ.

**No-ghost and Virasoro.** The level-2 Gram determinant 2h (16h² + 2(c − 5)h + c) is an algebraic identity. At h = −1 the vector L_{−2} + (3/2) L_{−1}² has norm squared (c − 26)/2, hence is null at c = 26. That calculation is not a unitarity proof. Here c is the Virasoro central charge. It is not a speed of light and not a topological charge. The no-ghost theorem (Goddard–Thorn, Physics Letters B 40 (1972) 235–238; Brower, Physical Review D 6 (1972) 1655–1662) transports positivity from a transverse space that is already positive. The pole plane as an II_{1,1} lattice is an **analogy**. No arithmetic lattice is constructed.

**Connes 1999.** In characteristic p, the projection order Q′_{Λ,0} ≤ S_Λ makes the subtracted trace of positive type (Theorem 5, as recorded in the atlas: characteristic p). The global number-field trace formula is equivalent to RH. Subtraction by itself is not a sign. A negative sign in front of a term does not make a quotient positive.

**Connes–Consani 2021.** At the archimedean place, for small support and the vanishing conditions of their Theorem 1, the archimedean Weil form dominates a trace on Sonin space. The support restriction matters. This is prior.

**Deninger.** A positive leafwise Hodge star commuting with the flow, up to the conformal factor, would force the critical line. Existence of that star is the conjecture already in the atlas.

**Sonin.** The semilocal Sonin inequality is one candidate for an energy condition. It is not the unique arithmetic dominant-energy condition. The naive two-place difference already fails in the atlas (R26, smallest eigenvalue −log 2 / √2).

**Clifford.** The relation c(v)c(w) + c(w)c(v) = 2g(v, w) exists for an indefinite g, for example Cl(1, 1) by real 2×2 matrices, and also for a Euclidean metric. Clifford multiplication does not choose the signature.

**Torsion.** A Lichnerowicz formula with skew torsion has a sign that depends on the formula and the convention. This note does not say that every torsion correction has the wrong sign.

**Phase.** The local archimedean phase delay is the kernel K, prior in the atlas. The full ratio Λ(1/2 − it) / Λ(1/2 + it) equals 1 by the functional equation Λ(s) = Λ(1 − s), wherever both values are finite and nonzero. No group-delay positivity is drawn from that ratio. A vacuum spectral density proportional to |Λ|² is not asserted. A theta functional is not asserted to change sign at the zeros.

## 4. The target, stated at the right strength (open)

Weil positivity on E0 asks for the quadratic form W to be positive semidefinite. Equivalently, there exists a map from those test functions into a Hilbert space, or a semidefinite quotient of one, whose squared norm equals W(g ∗ g^♯) exactly, with the divergent counterterm handled as in a cutoff of Connes’ type. A semidefinite quotient is allowed. That existence statement is Weil positivity, hence the Riemann Hypothesis. It is a restatement.

Four further demands make a construction useful, and they are not theorems that the Riemann Hypothesis hands you for free:

1. The target space is positive for a reason that does not use the zeros. A Cholesky factor of a window matrix is circular.
2. The map intertwines scaling and is consistent under restriction of the window.
3. The map is built by a global coupling of Euler factors and gamma data. Place-local squares cannot equal the signed local terms one place at a time, because each local term is indefinite. A global coupled construction may still use primes, Euler factors, and gamma data. Those are legitimate zeros-blind inputs. There is no blanket ban on them.
4. The construction fails for Davenport–Heilbronn, which has a functional equation and no Euler product.

A positive representation does not pick W. The reference form G0 does not pick W. Rank 1 of the atlas is unchanged: the missing object over ℚ is still a compatible J whose metric g(u, v) = ω(u, Jv) reproduces W on the pole annihilator. The sought arithmetic correspondence geometry — a surface, in the sense of a cohomology carrying that polarization — is not built. Connes–Consani have a square of sites. It does not yet carry this Hodge package. Saying “Spec ℤ × Spec ℤ is absent” would overstate that fact.

The pole plane remains signature (1, 1). Calling it the II_{1,1} summand of a lattice is an analogy.

## 5. Tests, and a test that was not run

| Test | What it is | What it is not |
|---|---|---|
| Finite-field split, reproduced | Exact identity and inertia on E×E | A sign for ζ |
| Free-basis signature, K = 8, A = 1 and A = 2 | W − P has one negative Rayleigh quotient (about −1.524 and −3.280) on an explicit vector; W’s Galerkin minimum is positive (about 1.4×10⁻⁴ and 4.4×10⁻¹²) | A certificate. No integral error bound is attached. Uses W itself, so not an independent sign. Same pattern as atlas entry on the free basis with one negative direction |
| Spring K = 8, exact E0, reproduced | Minima 0.06734 and 1.65×10⁻⁸ | A certificate or a limit in K |
| Audit script | Boundary inertia, Clifford for both signatures, spring completion, finite-field inertia versus determinant, nonnegativity of a trace norm beside a signed remainder, a BPS toy Hessian, the completed-zeta ratio, the h = −1 Virasoro norm | An independent positivity theorem |
| Trace-norm leakage at S = {∞, 2} | Not run | A well-posed falsifier in the form “leakage of negative sign.” A trace norm is nonnegative. A future test would have to bound that norm and, separately, a signed quadratic remainder, and only then talk about decay |

## 6. Where this sits in the atlas

Cross-links, not new missing pieces: the Kähler triple (rank 1); the v1.15 transverse space H₊ and its four construction criteria, with the logical correction in §4; the free-basis one-negative entry; TAA Lemma 162 and the Hodge index; Connes’ trace formula; Connes–Consani 2021; Deninger’s program. Raw session folders are under `provenance/` and are superseded by this note and by `LIMITATIONS.json`.

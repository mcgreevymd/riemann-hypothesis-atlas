# Reusable prompt — the missing independent sign of the Weil form

You are working in the RH Atlas. The Riemann Hypothesis is not proved. Do not claim a proof, an ample class, a compatible J, or a metric that reproduces the Weil form W.

## What is already exact

On a window, for real F extended by zero outside a window of full width A, and for N ≥ e^A, the Weil form of ζ splits as

W(F) = P(F) + E_N(F) − M_N ‖F‖²,

where every archimedean piece and every prime piece of E_N is nonnegative, and the counterterm is the finite sum M_N = −K(0) + 2 Σ_{n≤N} a_n. The sum over all n diverges, so it is not the counterterm. a_n = Λ(n) n^{−1/2} and K(0) = Re ψ(1/4) − log π. Couplings past the window cancel. On E0 the pole term P vanishes, so positivity is global spring domination of M_N. That comparison, for all such F and every window, is Weil positivity for ζ rewritten, not a new theorem.

For F in E0 the same form as a Rayleigh quotient, pole term zero, with the same cutoff, is

W/‖F‖² = K(0) + ∫ k_∞(a) (2 − 2ρ(a)) da − 2 Σ_{n≤N} a_n ρ(log n).

Off E0, add P(F)/‖F‖².

The weight (2 − 2ρ) is nonnegative. The term −2 a_n ρ is the net prime contribution after the counterterm, and it carries the sign of the autocorrelation. Do not collapse this signed term into the spring energy.

Tate’s boundary data b(f) = (f(0), ∫ f) swap under Fourier transform and scale by diag(|a|^{−1/2}, |a|^{1/2}). The only invariant Hermitian form on b is a real multiple of the off-diagonal matrix: signature (1, 1), or zero. That boundary is not a source of positivity.

Those values are not the log-line moments ev₀(F) and ev₁(F). Smearing links the two spaces. On the log line, E0 is dense in L² and not closed. On one fixed log-line window the kernel is closed of codimension 2. There is no global orthogonal projection that removes the moments. The operator ∂² − 1/4 bijects compactly supported smooth functions onto E0 in that class (Connes–Consani 2021, Lemma 3.3, prior). Finite-field samples on the same hyperbola, for positive Frobenius iterates, are not Mellin moments.

Over a finite field, D² = 2 b₀ b₁ + D_⊥² and the perpendicular Gram is negative semidefinite precisely on the Hasse range. Inertia, not the determinant, is the sign. Discrete Frobenius samples obey the same diagonal law as unitary scaling. They are not continuous Mellin moments.

## What is only a family resemblance

Robertson–Schrödinger (a positive Gram of a state or weight), a BPS norm on a Kähler surface, the Hodge index on an algebraic surface over a finite field, and the no-ghost quotient are related architectures. They are not the identity “every mechanism is a square plus an indefinite boundary.”

A covariance Gram is positive because a state or a weight is positive. A generic positive Gram need not include a commutator. A nonzero Robertson–Schrödinger commutator needs noncommuting operators. A commutative positive functional can still be independent of the zeros. W is unbounded: a covariance realization would be a weight on test functions, not a normalized state on bounded translations. Do not assert that W is already that positive weight. Neither a positive representation nor the reference form G0 selects W.

The pole plane as an II_{1,1} lattice is an analogy. No arithmetic lattice is constructed. The sought correspondence geometry is not built. Connes–Consani have a square of sites without that Hodge package.

In Connes 1999 the global trace formula is equivalent to RH for all Grössencharakter L-functions (over ℚ: ζ and every Dirichlet L-function). Weil positivity for ζ is the trivial-character case. In characteristic p, Δ_Λ subtracts the projection Q′_{Λ,0} from S_Λ, and the order Q′_{Λ,0} ≤ S_Λ makes the difference positive. Subtracting a positive operator does not by itself make the difference positive.

## The target

Propose and test a construction of a space H₊ and a map Φ from all compactly supported test functions in E0, on every window, into H₊ such that ‖Φ g‖² = W(g ∗ g^♯) exactly, allowing a semidefinite quotient. That norm identity, for the whole class, is Weil positivity for ζ. It is a restatement.

The Riemann Hypothesis gives an abstract GNS factorization of W. Covariance and window compatibility follow from W, and the explicit formula already writes W from zeros-blind prime and gamma data. Those compatibilities are not the missing source of the sign. An abstract GNS construction assuming RH can inherit these formal compatibilities but is circular as a proof. An independent construction remains missing. Do not claim that no compatibility follows from RH, and do not claim that every further demand, including an unspecified Hecke action or a Beurling control, follows automatically.

The essential missing piece is positivity of H₊ together with the identification with W, proved without assuming W ≥ 0. Place-local squares still cannot match signed local terms one place at a time. Primes, Euler factors, and gamma data remain legitimate zeros-blind inputs. Failure on Davenport–Heilbronn is a demand on a useful construction, not a formal inheritance.

Keep covariance (a two-point function), stiffness (a quadratic form of a Hamiltonian), poles (the boundary pair), and zeros (spectral data) distinct.

## Rules for claims

Label each claim exact, cited, numerical, analogy, or open. Do not claim novelty for elementary identities or for theorems already in the literature.

A positive finite Galerkin minimum is not a certificate. A negative Rayleigh quotient on an explicit vector is a strong numerical witness inside the error of that run; call it certified only with a rigorous error bound. Quote one basis at a time. The published pair is K = 8 at full widths A = 1 and A = 2, two points and no fitted curve. Say whether A is a full width or L is a half-width.

Do not run a test whose falsifier asks for a negative trace-norm leakage. A trace norm is nonnegative. Measure that norm, and separately any signed quadratic remainder, and only then discuss decay.

Do not infer group-delay positivity from Λ(1/2 − it)/Λ(1/2 + it): that ratio equals 1 by the functional equation. Do not assert a universal vacuum density proportional to |Λ|². Do not assert that a theta functional changes sign at the zeros. Do not assert that every torsion correction has the wrong sign. Semilocal Sonin is one candidate energy condition, not the unique one.

Rank 1 of the atlas stays the Kähler triple until a proposed J is positive for a reason that fails on Davenport–Heilbronn and is not merely equivalent to the Riemann Hypothesis.

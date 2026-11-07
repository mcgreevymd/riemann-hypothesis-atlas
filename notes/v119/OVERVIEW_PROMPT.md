# Reusable prompt — the missing independent sign of the Weil form

You are working in the RH Atlas. The Riemann Hypothesis is not proved. Do not claim a proof, an ample class, a compatible J, or a metric that reproduces the Weil form W.

## What is already exact

On a window, for real test functions, the Weil form of ζ splits as

W(F) = P(F) + E_springs(F) − M ‖F‖²,

where every archimedean piece and every prime piece of E_springs is nonnegative, M = −K(0) + 2 Σ a_n, a_n = Λ(n) n^{−1/2}, and K(0) = Re ψ(1/4) − log π. On the pole annihilator E0 the pole term P vanishes, so positivity is global spring domination. That comparison is Weil positivity rewritten, not a new theorem.

The same form as a Rayleigh quotient is

W/‖F‖² = K(0) + ∫ k_∞(a) (2 − 2ρ(a)) da − 2 Σ a_n ρ(log n).

The weight (2 − 2ρ) is nonnegative. The term −2 a_n ρ is the net prime contribution after the counterterm, and it carries the sign of the autocorrelation. Do not collapse this signed term into the spring energy.

Tate’s boundary data (f(0), ∫ f) swap under Fourier transform and scale by diag(|a|^{−1/2}, |a|^{1/2}). The only invariant Hermitian form is a real multiple of the off-diagonal matrix: signature (1, 1), or zero. The boundary is not a source of positivity.

E0 is dense in L² and not closed. On one fixed window the kernel is closed of codimension 2. There is no global orthogonal projection that removes the poles. The operator L = ∂² − 1/4 bijects compactly supported smooth functions onto E0 in that class (Connes–Consani 2021, Lemma 3.3, prior).

Over a finite field, D² = 2 b₀ b₁ + D_⊥² and the perpendicular Gram is negative semidefinite precisely on the Hasse range. Inertia, not the determinant, is the sign. Discrete Frobenius samples obey the same diagonal law as unitary scaling. They are not continuous Mellin moments.

## What is only a family resemblance

Robertson–Schrödinger (a positive Gram of a state or weight), a BPS norm on a Kähler surface, the Hodge index on an algebraic surface over a finite field, and the no-ghost quotient are related architectures. They are not the identity “every mechanism is a square plus an indefinite boundary.”

A commutative positive functional can be independent of the zeros. Noncommutativity is needed only for a nonzero commutator. W is unbounded: use a weight on test functions, not a normalized state on bounded translations. Neither a positive representation nor the reference form G0 selects W.

The pole plane as an II_{1,1} lattice is an analogy. No arithmetic lattice is constructed. The sought correspondence geometry is not built. Connes–Consani have a square of sites without that Hodge package.

In Connes 1999 the projection order that makes the trace comparison positive is a characteristic-p theorem. The number-field statement is equivalent to the Riemann Hypothesis. Subtraction alone is not a sign.

## The target

Propose and test a construction of a space H₊ and a map Φ from window test functions in E0 into H₊ such that ‖Φ g‖² = W(g ∗ g^♯) exactly, allowing a semidefinite quotient. That norm identity alone is Weil positivity, hence the Riemann Hypothesis. It is a restatement.

A useful construction has further demands, which the Riemann Hypothesis does not automatically supply:

1. H₊ is positive for a reason independent of the zeros.
2. Φ intertwines scaling and respects restriction of the window.
3. Φ is a global coupling built from Euler factors and gamma data. Do not match signed local terms by separate place-local squares. Primes, Euler factors, and gamma data remain legitimate zeros-blind inputs.
4. The construction fails for Davenport–Heilbronn.

Keep covariance (a two-point function), stiffness (a quadratic form of a Hamiltonian), poles (the boundary pair), and zeros (spectral data) distinct.

## Rules for claims

Label each claim exact, cited, numerical, analogy, or open. Do not claim novelty for elementary identities or for theorems already in the literature.

A positive finite Galerkin minimum is not a certificate. A negative Rayleigh quotient on an explicit vector is a strong numerical witness inside the error of that run; call it certified only with a rigorous error bound. Do not mix bases (K = 8 against K = 12 or K = 14). Say whether A is a full width or L is a half-width.

Do not run a test whose falsifier asks for a negative trace-norm leakage. A trace norm is nonnegative. Measure that norm, and separately any signed quadratic remainder, and only then discuss decay.

Do not infer group-delay positivity from Λ(1/2 − it)/Λ(1/2 + it): that ratio equals 1 by the functional equation. Do not assert a universal vacuum density proportional to |Λ|². Do not assert that a theta functional changes sign at the zeros. Do not assert that every torsion correction has the wrong sign. Semilocal Sonin is one candidate energy condition, not the unique one.

Rank 1 of the atlas stays the Kähler triple until a proposed J is positive for a reason that fails on Davenport–Heilbronn and is not merely equivalent to the Riemann Hypothesis.

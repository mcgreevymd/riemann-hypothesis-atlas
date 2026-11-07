#!/usr/bin/env python3
"""Insert the v1.19 concepts into atlas.json.

Existing priorities, ranking components, and the relative order of existing
concepts are left unchanged. New concepts are placed after the existing block
of the same priority. Gap significance of a new concept is the distance in the
relation graph to one of the ten missing pieces, using the published rule.
"""
import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "atlas.json"

NEW = [
    dict(
        id="spring_energy_counterterm_split",
        name="Window Weil form as nonnegative spring energy minus a counterterm",
        aliases=["spring domination", "E_springs", "anharmonic Hessian of W"],
        plain="On a window the Weil form is the pole term plus a sum of nonnegative archimedean and prime spring energies, minus a counterterm M times the norm squared. On the pole annihilator, positivity is exactly whether the springs dominate the counterterm. The identity restates W; it does not prove the inequality.",
        label="Theorem",
        core="For real F supported in a window of full width A, and N at least e^A: W(F) = P(F) + integral k_infinity(a) ||F - T_a F||^2 da + sum a_n ||F - T_log n F||^2 - M_N ||F||^2, with a_n = Lambda(n) n^(-1/2), k_infinity(a) = e^(-a/2)/(1-e^(-2a)), and M_N = -K(0) + 2 sum a_n, K(0) = Re psi(1/4) - log pi. Each spring is nonnegative. Tails cancel on the window. The archimedean Levy representation is prior. An explicit quartic functional has Hessian at 0 equal to W, and away from 0 the Hessian is W plus a nonnegative quartic term: a Hessian identity, not a sign.",
        formula="W = P + E_springs - M ||F||^2 on a window; on E0, P = 0",
        numbers=[
            "K = 8 exact-E0 reproduction: full width A = 1, smallest Rayleigh quotient 0.0673395762411; A = 2, 1.65055568024e-8. Upper bounds, not certificates.",
            "Mass M about 6.352 and 11.225 at those two widths.",
            "Research-note score: the identity is exact; the inequality is open and is Weil positivity on E0.",
        ],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="The splitting is an algebraic completion of the square for translation isometries, on top of the prior archimedean Levy representation.",
        tests="A uniform gap is not expected. Domination for every test function is the open comparison.",
        pitfalls=[
            "Positive Galerkin minima are not certificates, and K = 8 does not control K to infinity.",
            "Do not read this identity as a ban on domination. Domination of the counterterm by the springs is the target. A uniform surplus, independent of the test function, is a different and unavailable argument.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "levy_khintchine_mass_gap", "note": "completed-square form of the jump-minus-mass split; the archimedean Levy piece is prior"},
            {"type": "refines", "to": "arch_levy_khintchine_sos", "note": "the constant shift is the diagonal absorbed into M"},
            {"type": "uses", "to": "weil_kernel_is_levy_measure", "note": "same archimedean density"},
            {"type": "distinguishes", "to": "margins_force_identity", "note": "no uniform gap; the remaining target is spring energy against the counterterm"},
            {"type": "refines", "to": "weil_positivity", "note": "on E0 the inequality is Weil positivity rewritten; the identity does not prove it"},
        ],
    ),
    dict(
        id="signed_prime_autocorrelation",
        name="After the counterterm, the net prime contribution has the sign of the autocorrelation",
        aliases=["signed autocorrelation", "rho of the Weil form"],
        plain="Grouped as a Rayleigh quotient, the archimedean density contributes through a nonnegative weight 2 - 2 rho, while each prime leaves -2 a_n rho(log n). That signed term is what remains after the counterterm has taken the diagonal. It is not the prime spring energy, which stays nonnegative.",
        label="Theorem",
        core="W(F)/||F||^2 = K(0) + integral k_infinity(a) (2 - 2 rho(F, a)) da - 2 sum a_n rho(F, log n), rho(b) = <F, T_b F> / ||F||^2. The weight 2 - 2 rho is nonnegative for a real isometry. The coefficient of a_n is minus twice the autocorrelation, so a prime helps or hurts that mode according to the sign of rho. The bottom of the spectrum is concave in the weights (K(0), k_infinity, a_n), so the nonnegative set is convex. Elementary reorganization of the same quadratic form, not a new inequality.",
        formula="W/||F||^2 = K(0) + integral k (2-2 rho) - 2 sum a_n rho(log n)",
        numbers=["Convexity of the positivity region in the weights is exact and does not decide the arithmetic point."],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Algebraic identity for a real translation isometry: a ||F - TF||^2 - 2 a ||F||^2 = -2 a <F, TF>.",
        tests="",
        pitfalls=["Do not describe the prime springs as signed. The springs are nonnegative. The signed object is the net term after the counterterm."],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "distinguishes", "to": "spring_energy_counterterm_split", "note": "same quadratic form, two groupings"},
            {"type": "uses", "to": "weil_kernel_is_levy_measure", "note": ""},
            {"type": "refines", "to": "weil_positivity", "note": "Rayleigh form of the same criterion"},
        ],
    ),
    dict(
        id="spring_galerkin_near_cancellation",
        name="Exact-E0 Galerkin minima shrink with the window and are not certificates",
        aliases=["K=8 spring reproduction"],
        plain="On the exact-E0 basis at K = 8 the smallest Rayleigh quotient of W is about 0.067 at full width A = 1 and about 1.7e-8 at A = 2. These positive values are upper bounds. They diagnose a near cancellation between spring energy and the counterterm. They do not certify positivity and they do not control the limit in K.",
        label="Numerical",
        core="Reproduced from spring_mp.py with 50-digit arithmetic: A = 1, mu = 0.0673395762411, second 0.433319, M = 6.3524416; A = 2, mu = 1.65055568024e-8, second 9.30914e-8, M = 11.224652. A is the full width of [-A/2, A/2]. Session notes at other K, including a K = 12 run at A = 3 in which dropping one prime n <= 13 gave a negative direction, are a different legend: strong numerical witnesses of those matrices, not certified eigenvalues, because no rigorous integral error bound is attached.",
        formula="",
        numbers=[
            "K = 8, A = 1: 0.0673395762411",
            "K = 8, A = 2: 1.65055568024e-8",
            "Hat basis h = 0.05 is a third legend (about 1.7e-2 at width 1) and is not these values.",
        ],
        axes=["numerics/certificate", "sign/positivity (Ax2)"],
        uncertain="",
        proved="",
        tests="Must not be quoted as a proof of positivity, nor as a limit.",
        pitfalls=[
            "Upper bounds only.",
            "Do not mix K = 8 with K = 12 or K = 14.",
            "A negative direction in a session note is a strong numerical witness inside that run, not a certified eigenvalue.",
        ],
        lemmas=[],
        spec=0.5,
        rels=[
            {"type": "illustrates", "to": "spring_energy_counterterm_split", "note": "near cancellation of E_springs against M"},
            {"type": "illustrates", "to": "signed_prime_autocorrelation", "note": ""},
            {"type": "contrasts-with", "to": "crude_domination_fails", "note": "different comparison; still not a certificate"},
        ],
    ),
    dict(
        id="tate_boundary_only_hyperbolic",
        name="The only scaling-and-Fourier invariant Hermitian form on Tate’s two boundary numbers is hyperbolic or zero",
        aliases=["boundary signature (1,1)", "invariant form on b(f)"],
        plain="Fourier transform swaps f(0) and the integral of f. Unitary scaling multiplies them by opposite powers of |a|. The only Hermitian forms invariant under both are real multiples of the off-diagonal matrix. A nonzero multiple has signature (1, 1). The zero multiple is degenerate. The boundary does not supply a positive sign.",
        label="Theorem",
        core="b(f) = (f(0), integral f). b(Ff) = sigma b(f), b(U_a f) = diag(|a|^(-1/2), |a|^(1/2)) b(f), and F U_a = U_(1/a) F. Smearing by F on the log line multiplies b by diag(ev_0 F, ev_1 F), so Theta_F maps the entire Schwartz-Bruhat space into ker b if and only if F is in E0. Checked symbolically: invariance under all positive scalings and under sigma forces the diagonal entries to vanish and the off-diagonal entry to be real. The Weil pole term is of this hyperbolic type. Finite-field graph pairings (q^(-n/2), q^(n/2)) obey the same diagonal law as discrete samples, not as Mellin moments.",
        formula="H = z [[0, 1], [1, 0]], z real",
        numbers=["Eigenvalues of the generator are +z and -z.", "Audit script: the zero solution is degenerate, eigenvalues 0, 0."],
        axes=["reference/pole/cusp", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Elementary representation fact on C^2, re-checked in notes/v119/tests/audit_v119.py.",
        tests="",
        pitfalls=[
            "This is not an arithmetic lattice. The II_1,1 reading of the pole plane stays an analogy.",
            "Do not identify the finite-field sample points with continuous Mellin integrals.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "same-mechanism-as", "to": "pole_block_hyperbolic_plane", "note": "the pole block is this hyperbolic form"},
            {"type": "illustrates", "to": "pole_plane", "note": ""},
            {"type": "analogue-of", "to": "ii11_pole_pair", "note": "exact form on two scalars; the lattice is not constructed"},
            {"type": "contrasts-with", "to": "boundary_signature_neutral", "note": "the boundary pair itself is indefinite; neutrality is a statement about a graded piece"},
        ],
    ),
    dict(
        id="e0_dense_window_kernel_closed",
        name="E0 is dense in L² and not closed; on one window the kernel is closed of codimension 2",
        aliases=["no global pole projection", "window kernel of the moments"],
        plain="The two moment functionals are unbounded on L², so their common kernel E0 is dense, and smooth functions in E0 are not an L²-closed set. On one finite window both exponentials are square-integrable, so the kernel is closed and has codimension 2. There is no single orthogonal projection that removes the poles on the whole line.",
        label="Theorem",
        core="E0 = {ev_0 = ev_1 = 0} is a convolution ideal and is stable under the sharp involution. Globally, P means the moment map b, or a window-dependent projection. The operator L = d^2/du^2 - 1/4 bijects compactly supported smooth functions onto E0 in that class and preserves support hulls; positivity transports across it. That bijection is Connes-Consani 2021, Lemma 3.3, and the transport is their Proposition 3.5, prior. On the core with the reference form G0, Q0 = L Q L^(-1) and the dilation commute as a relabeling of the Schrödinger representation. A fixed window still needs boundary conditions before the operator is self-adjoint. A real convolution by F is self-adjoint only when F sharp equals F.",
        formula="L = ∂² − 1/4 : C_c^∞ → E0 ∩ C_c^∞, prior",
        numbers=[
            "Session density checks: L² distance to a Schwartz function with vanishing boundary data falls like the square root of the shrinking scale.",
            "On windows of half-width L = 2, 4, 8 the distance from a fixed test function to the closed kernel is about 0.820, 0.346, 0.050.",
        ],
        axes=["reference/pole/cusp", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Unboundedness of point evaluation and of integration against a non-square-integrable exponential. The bijection across L is cited, not re-proved.",
        tests="",
        pitfalls=[
            "Do not call E0 a closed codimension-2 subspace of L².",
            "L in the boundary logs is a half-width. A in the spring logs is a full width.",
            "Translations are abelian. A noncommutative enlargement is for a Robertson-Schrödinger commutator, not a requirement for an independent positive functional.",
        ],
        lemmas=["L153"],
        spec=0.05,
        rels=[
            {"type": "lives-in", "to": "primitive_part", "note": "E0 is the annihilator of the pole functionals"},
            {"type": "uses", "to": "cc21_archimedean_positivity", "note": "Lemma 3.3 and Proposition 3.5, prior"},
            {"type": "refines", "to": "pole_plane", "note": "global versus window topology of the same two functionals"},
            {"type": "distinguishes", "to": "tate_boundary_only_hyperbolic", "note": "the form is hyperbolic; the projection that cuts it out is not global"},
        ],
    ),
    dict(
        id="positive_weight_not_normalized_state",
        name="An independent positive functional may be commutative; W is a weight, not a normalized state on bounded translations",
        aliases=["Robertson-Schrödinger versus stiffness", "Bochner correction"],
        plain="A positive covariance is the Gram of a state or a weight. A commutative positive functional can be independent of the zeros. Noncommutativity is needed only for a nonzero commutator. Because W is unbounded, the object is a weight on the test-function algebra, not a normalized state on bounded translations. Positivity of a representation does not select W, and neither does the reference form G0.",
        label="Theorem",
        core="Withdrawn: the claim that a commutative functional cannot be an independent sign (the so-called Bochner trap). A positive-definite distribution is the Fourier transform of a positive tempered measure. Stiffness is the quadratic form of a Hamiltonian; covariance is a two-point function; poles are the boundary pair; zeros are spectral data. The local archimedean phase delay is the kernel K, prior. The ratio of completed zeta values Lambda(1/2 - it) / Lambda(1/2 + it) equals 1 by the functional equation, so no group-delay positivity is drawn from it. Real F defines a self-adjoint convolution only when F sharp equals F. Q0 and the dilation commute on the core with G0; a window realization still depends on boundary conditions of the domain.",
        formula="",
        numbers=["Audit: Lambda(1/2 - it) / Lambda(1/2 + it) agrees with 1 to 1e-8 at t = 1 and t = 5, as the functional equation requires."],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)"],
        uncertain="",
        proved="The functional equation gives the ratio 1. The Bochner-Schwartz correspondence is classical and is not re-proved here; the correction is that it does not forbid an independent functional.",
        tests="Must not be used to claim a state whose two-point function is W. No such state is constructed.",
        pitfalls=[
            "RS in this entry is Robertson-Schrödinger, not Rankin-Selberg.",
            "A vacuum spectral density proportional to |Lambda|^2 is not asserted.",
            "A theta functional is not asserted to change sign at the zeros.",
        ],
        lemmas=[],
        spec=0.5,
        rels=[
            {"type": "refines", "to": "no_ghost_missing_piece", "note": "a positive functional can be the independent input; it does not pick W"},
            {"type": "contrasts-with", "to": "supercharge_laplacian_restates_positivity", "note": "a square root restates positivity; commutativity does not forbid an independent functional"},
            {"type": "uses", "to": "archimedean_weyl_kernel", "note": "local phase delay is K; the completed ratio is identically 1"},
        ],
    ),
    dict(
        id="quadratic_architectures_related",
        name="Robertson–Schrödinger, BPS, Hodge index, and no-ghost are related architectures, not one identity",
        aliases=["not a universal square-plus-boundary identity"],
        plain="A positive Gram, a metric square on a Kähler surface, the Hodge index on an algebraic surface over a finite field, and a no-ghost quotient are cousins. They are not the single formula “every mechanism is a square plus an indefinite boundary.” Clifford multiplication exists for an indefinite metric, so it is not a source of positivity. The arithmetic polarization that would match W is not built.",
        label="Analogy",
        core="Checked pieces, each in its own setting: Cl(1,1) and a Euclidean Clifford relation both exist; primitive real (1,1) forms on a Kähler surface are anti-self-dual, which is Riemannian geometry of a complex surface; the finite-field sign is the intersection form, a different theorem; a Bogomolny charge has vanishing Hessian and the norm is the metric square; the level-2 Virasoro norm at h = -1 equals (c - 26)/2, algebra only, and c is a central charge, not a speed and not a topological charge. Goddard-Thorn and Brower transport positivity from an already positive transverse space. Semilocal Sonin is one candidate energy condition, not the unique one. Torsion corrections in a Lichnerowicz formula are convention-dependent. Connes 1999: characteristic-p projection order is a theorem; the number-field comparison is equivalent to RH; subtraction alone is not a sign. The pole plane as an II_1,1 lattice is an analogy. Rank 1, the missing compatible J, is unchanged.",
        formula="",
        numbers=[
            "Audit: Clifford relations for signature (1,1) and for the Euclidean plane; Virasoro norm (c-26)/2 at h = -1; BPS toy Hessian of a constant charge is 0.",
            "Analogy score on the 0-4 research-note scale: 2.4 (structural resemblance, no load-bearing map).",
        ],
        axes=["physics analogue", "sign/positivity (Ax2)"],
        uncertain="",
        proved="",
        tests="Must not be quoted as a construction of H_+.",
        pitfalls=[
            "Do not say that only the Hodge pair produces a sign. Positive representations, metrics, and positive states also do.",
            "Do not identify the Kähler anti-self-dual equation with the finite-field Hodge index.",
            "Do not say Spec Z times Spec Z is absent. The sought correspondence geometry, a polarization matching W, is not built. Connes-Consani have a square of sites without that package.",
        ],
        lemmas=[],
        spec=0.5,
        rels=[
            {"type": "analogue-of", "to": "no_ghost_template", "note": "transports positivity; does not create it"},
            {"type": "analogue-of", "to": "hodge_index", "note": "finite-field intersection form, not the Kähler ASD equation"},
            {"type": "analogue-of", "to": "kahler_triple_polarization", "note": "rank 1 asks for the missing J; this entry does not construct it"},
            {"type": "distinguishes", "to": "ii11_pole_pair", "note": "analogy of lattices, not a construction"},
            {"type": "analogue-of", "to": "deninger", "note": "a positive leafwise star would force the line; the star is conjectural"},
            {"type": "contrasts-with", "to": "cc21_archimedean_positivity", "note": "Sonin compression is one archimedean candidate"},
            {"type": "uses", "to": "connes_trace", "note": "characteristic-p order versus the number-field target"},
        ],
    ),
    dict(
        id="norm_identity_iff_weil_not_four_criteria",
        name="The norm identity is Weil positivity; the four construction criteria are not automatic",
        aliases=["H+ norm identity versus construction criteria"],
        plain="Existence of a map from window test functions in E0 into a Hilbert space, or a semidefinite quotient, with squared norm exactly equal to W, is Weil positivity. The four demands that make a construction useful — an independent reason for the norm, scaling and window consistency, a global coupling of Euler and gamma data, and failure on Davenport-Heilbronn — are not theorems that follow from the Riemann Hypothesis for free.",
        label="Restatement",
        core="A semidefinite quotient is allowed. A Cholesky factor of a window matrix meets the norm identity and is circular. Place-local squares cannot equal the signed local terms one place at a time, because each local term is indefinite. A global coupled construction may still use primes, Euler factors, and gamma data; those are legitimate zeros-blind inputs. There is no blanket ban on them. A positive representation does not select W. The reference form G0 does not select W. No such map, and no compatible J whose metric reproduces W, is constructed. This corrects an over-strong reading of the v1.15 four conditions: they remain the right shape of a useful proof, and they are construction criteria.",
        formula="||Phi g||^2 = W(g * g sharp) on E0, semidefinite quotient allowed",
        numbers=["Research-note score of the equivalence: restatement. Score of the four criteria as a construction brief: open, unchanged in kind from v1.15."],
        axes=["restatement ⇔ RH", "open target", "sign/positivity (Ax2)"],
        uncertain="",
        proved="GNS / Kolmogorov: a positive semidefinite kernel is a Gram matrix. The arithmetic construction is not proved.",
        tests="A proposed Phi that is also positive for Davenport-Heilbronn, or that is assembled as a sum of place-local squares, or that is only shown to restate RH, does not meet the construction brief. Rank 1 would be demoted by a J that fails in one of those ways.",
        pitfalls=[
            "Do not say that RH automatically provides all four construction criteria.",
            "Do not ban Euler factors or gamma data as inputs. Ban only the place-by-place square that tries to match an indefinite local term by itself.",
        ],
        lemmas=[],
        spec=1.0,
        rels=[
            {"type": "restates", "to": "weil_positivity", "note": "norm identity, semidefinite quotient allowed"},
            {"type": "refines", "to": "no_ghost_missing_piece", "note": "four conditions stay the construction brief; they are not automatic"},
            {"type": "constrains", "to": "kahler_triple_polarization", "note": "no J whose g reproduces W is constructed; rank 1 unchanged"},
            {"type": "contrasts-with", "to": "fock_gram_realization_target", "note": "existence of some factorization is the norm identity; G0 does not select it"},
            {"type": "uses", "to": "connes_trace", "note": "cutoff bookkeeping for the counterterm, as in the characteristic-p comparison"},
            {"type": "uses", "to": "cc21_archimedean_positivity", "note": "archimedean small-support comparison is prior, not the global map"},
        ],
    ),
    dict(
        id="fq_split_inertia_not_determinant",
        name="On E×E the intersection form splits as a hyperbolic boundary term plus a perpendicular Gram whose sign is inertia, not the determinant",
        aliases=["E x E boundary split", "Test 1"],
        plain="For a divisor on E×E, the self-intersection is twice the product of the two boundary pairings plus the perpendicular square. The perpendicular Gram is negative semidefinite exactly on the Hasse range. The determinant 4q - a^2 is positive for negative-definite examples, so the determinant does not decide the sign. The normalized Frobenius graphs sit on the same scaling hyperbola as Tate’s boundary data, as discrete samples.",
        label="Theorem",
        core="Basis h, v, Delta, Gamma. b = (D·v, D·h). D^2 = 2 b0 b1 + D_perp^2, and the cross term vanishes. Perpendicular Gram [[-2, -a], [-a, -2q]], determinant 4q - a^2. Reproduced scan: 151 trace values, negative semidefinite if and only if a^2 <= 4q. Boundary eigenvalues of [[0,1],[1,0]] are -1 and +1. This re-checks the Gram of TAA Lemma 162 and the Hodge index already in the atlas. It is a finite-field control. It is not a sign for zeta. Mattuck-Tate (Hamburg Abh. 22 (1958) 295) and Grothendieck (J. Reine Angew. Math. 200 (1958) 208-215) are the literature for the curve case via the surface; not re-proved here.",
        formula="D^2 = 2 b0 b1 + D_perp^2; perp Gram [[-2, -a], [-a, -2q]]",
        numbers=["151/151 traces: negative semidefinite iff a^2 <= 4q.", "Examples with positive determinant and two negative eigenvalues, including (q, a) = (2, 0)."],
        axes=["geometry over F_q", "sign/positivity (Ax2)", "numerics/certificate"],
        uncertain="",
        proved="Exact linear algebra on the standard intersection matrix, reproduced in test1.",
        tests="Ghost traces with a^2 > 4q must leave the negative-semidefinite range. They do, in the scan.",
        pitfalls=[
            "Do not call the finite-field points Mellin moments.",
            "Do not treat determinant positivity as form positivity.",
            "This does not construct a polarization for zeta.",
        ],
        lemmas=["L162"],
        spec=0.5,
        rels=[
            {"type": "reconfirms", "to": "hodge_index", "note": "inertia of the E×E Gram"},
            {"type": "illustrates", "to": "kahler_triple_polarization", "note": "finite-field side of rank 1; the J over Q is still missing"},
            {"type": "uses", "to": "ff_weil_form_is_h1_gram", "note": ""},
            {"type": "distinguishes", "to": "det_sign_parity_blind", "note": "determinant versus inertia, now on the perpendicular block"},
            {"type": "contrasts-with", "to": "tate_boundary_only_hyperbolic", "note": "same diagonal law, discrete samples versus continuous moments"},
        ],
    ),
    dict(
        id="window_signature_numerical_witness",
        name="Free-basis windows: one negative direction for W minus the pole term, Galerkin-positive for W, not a certificate",
        aliases=["K=8 signature dictionary", "Test 2"],
        plain="On a free basis at K = 8, full widths A = 1 and A = 2, W minus the pole term has one negative Rayleigh quotient, about -1.524 and -3.280, on an explicit vector. W itself has no negative Galerkin eigenvalue at this K, with minima about 1.4e-4 and 4.4e-12. The negative values are strong numerical witnesses without a rigorous error bound. The positive minima are not certificates. The test uses W, so it is not an independent sign.",
        label="Numerical",
        core="Finite-field side of the same dictionary: W_q = -D^2 + 2 b0 b1 equals -D_perp^2 and is positive semidefinite on a Hasse example (q = 5, a = 2), while -D^2 is indefinite. Zeta side: free basis, not the exact-E0 spring basis. Pole term polarized as 2ab. The pattern matches the atlas entry that zeta without the pole has one negative direction. It does not improve that entry to a certified count.",
        formula="",
        numbers=[
            "A = 1: W-P leading eigenvalues about -1.52372, 0.0251095, 0.258915; W leading about 0.000137191.",
            "A = 2: W-P leading about -3.28031; W leading about 4.42209e-12.",
            "Explicit-vector check agrees with the leading W-P eigenvalue to the printed digits. Still not a certified enclosure.",
        ],
        axes=["numerics/certificate", "sign/positivity (Ax2)"],
        uncertain="",
        proved="",
        tests="Must not be cited as an independent positivity proof.",
        pitfalls=[
            "Strong numerical witness, not a certified eigenvalue: no rigorous integral error bound is attached.",
            "Positive Galerkin minima are upper bounds.",
            "K = 8 only. Not a limit.",
        ],
        lemmas=[],
        spec=0.5,
        rels=[
            {"type": "illustrates", "to": "fq_split_inertia_not_determinant", "note": "same dictionary, zeta side uses W itself"},
            {"type": "reconfirms", "to": "pole_plane_hyperbolic_complement_positive", "note": "one negative direction for W minus the pole, on this free basis"},
            {"type": "illustrates", "to": "spring_galerkin_near_cancellation", "note": "different basis: free here, exact-E0 there"},
        ],
    ),
]


def sensitivity(label):
    return {"Theorem": 1.0, "Cited": 1.0, "Numerical": 1.0, "Restatement": 1.0,
            "Open": 1.0, "Heuristic": 0.7, "Analogy": 0.6, "Conjecture": 1.0}[label]


def tractability(label):
    return {"Numerical": 0.7, "Theorem": 0.6, "Cited": 0.6, "Heuristic": 0.5,
            "Analogy": 0.4, "Restatement": 0.3, "Conjecture": 0.2, "Open": 0.2}[label]


def evidence(label):
    return {"Theorem": 1.0, "Cited": 1.0, "Restatement": 1.0, "Numerical": 0.8,
            "Heuristic": 0.6, "Analogy": 0.5, "Open": 0.5, "Conjecture": 0.5}[label]


def quadrant(sens, spec):
    if sens >= 0.8 and spec >= 0.8:
        return "RH-sharp"
    if sens >= 0.8:
        return "true but ghost-blind/untested"
    if spec >= 0.8:
        return "sharp but interpretive"
    return "background"


def priority(gap, sens, spec, tract):
    sig = gap * (sens * spec) ** 0.5
    return round(0.6 * sig + 0.4 * tract + 1e-12, 3)


def graph_distance(concepts):
    mp = {c["id"] for c in concepts if "missing piece" in c["axes"]}
    g = {}
    for c in concepts:
        g.setdefault(c["id"], set())
        for r in c["rels"]:
            g.setdefault(c["id"], set()).add(r["to"])
            g.setdefault(r["to"], set()).add(c["id"])

    def nearest(src):
        if src in mp:
            return 0, src
        seen = {src}
        q = deque([(src, 0)])
        while q:
            u, d = q.popleft()
            if d >= 4:
                continue
            for v in g.get(u, ()):
                if v in seen:
                    continue
                seen.add(v)
                if v in mp:
                    return d + 1, v
                q.append((v, d + 1))
        return 99, ""

    return nearest


def gap_from_dist(d):
    if d <= 1:
        return 0.8
    if d == 2:
        return 0.5
    return 0.2


def main():
    raw = ATLAS.read_text(encoding="utf-8")
    data = json.loads(raw)
    concepts = data["concepts"]
    ids = {c["id"] for c in concepts}
    adding = [c for c in NEW if c["id"] not in ids]
    if not adding:
        print("concepts already present")
        return

    # pitfalls on existing entries
    extra = {
        "no_ghost_missing_piece": (
            "v1.19 correction. A map into a semidefinite quotient with squared norm exactly W is Weil positivity. "
            "The four construction criteria are extra demands on a useful proof; they are not automatic consequences of that equivalence. "
            "Place-local squares cannot match the signed local terms one place at a time. A global coupling may still be built from primes, Euler factors, and gamma data. "
            "Neither a positive representation nor G0 selects W. The pole pair as an II₁,₁ lattice is an analogy; no arithmetic lattice is constructed. "
            "No ample class or compatible J matching W is constructed."
        ),
        "margins_force_identity": (
            "v1.19. A uniform gap is still unavailable: the margin closes. The spring target is nevertheless global domination, "
            "W = E_springs − M‖F‖² on E0, with every spring nonnegative. Near cancellation is the diagnostic of that balance, not a certificate and not a ban on the identity."
        ),
        "ii11_pole_pair": (
            "v1.19. Analogy only. No arithmetic II₁,₁ lattice is constructed. The exact (1, 1) statement is the invariant Hermitian form on the two boundary scalars."
        ),
        "einstein_cartan_torsion_spin": (
            "v1.19. The sign of a torsion correction in a Lichnerowicz formula depends on the formula and the convention. This entry does not claim that every torsion term has the wrong sign for positivity."
        ),
        "needed_semilocal_sonin_inequality": (
            "v1.19. One candidate energy condition, not the unique arithmetic dominant-energy condition. "
            "A trace-norm leakage is nonnegative, so a falsifier that asks for leakage of negative sign is ill-posed. The 6 Nov 2026 draft test at S = {∞, 2} was not run."
        ),
    }
    by = {c["id"]: c for c in concepts}
    for i, text in extra.items():
        if text not in by[i]["pitfalls"]:
            by[i]["pitfalls"].append(text)

    built = []
    for spec in adding:
        sens = sensitivity(spec["label"])
        tract = tractability(spec["label"])
        ev = evidence(spec["label"])
        c = {
            "id": spec["id"],
            "name": spec["name"],
            "aliases": spec["aliases"],
            "plain": spec["plain"],
            "label": spec["label"],
            "core": spec["core"],
            "formula": spec["formula"],
            "numbers": spec["numbers"],
            "axes": spec["axes"],
            "uncertain": spec["uncertain"],
            "proved": spec["proved"],
            "tests": spec["tests"],
            "pitfalls": spec["pitfalls"],
            "lemmas": spec["lemmas"],
            "rels": spec["rels"],
            "priority": 0.0,
            "ranking": {
                "gap_significance": 0.2,
                "gap": "",
                "sensitivity": sens,
                "specificity": spec["spec"],
                "tractability": tract,
                "evidence": ev,
                "quadrant": quadrant(sens, spec["spec"]),
            },
            "rank": 10**9,
        }
        built.append(c)
        concepts.append(c)

    nearest = graph_distance(concepts)
    for c in built:
        dist, gap_id = nearest(c["id"])
        gsig = gap_from_dist(dist)
        r = c["ranking"]
        r["gap_significance"] = gsig
        r["gap"] = gap_id if gsig >= 0.5 else ""
        c["priority"] = priority(gsig, r["sensitivity"], r["specificity"], r["tractability"])
        print(f"{c['id']}: dist {dist} -> {gap_id or '-'} gap {gsig} priority {c['priority']} {r['quadrant']}")

    # stable insertion: existing relative order kept; new concepts follow the existing block of equal priority
    existing = [c for c in concepts if c not in built]
    existing.sort(key=lambda c: c["rank"])
    from collections import defaultdict
    ex_b = defaultdict(list)
    nu_b = defaultdict(list)
    for c in existing:
        ex_b[c["priority"]].append(c)
    for c in built:
        nu_b[c["priority"]].append(c)
    pris = sorted(set(ex_b) | set(nu_b), reverse=True)
    order = []
    for p in pris:
        order.extend(ex_b.get(p, []))
        order.extend(sorted(nu_b.get(p, []), key=lambda c: c["id"]))
    for i, c in enumerate(order, 1):
        c["rank"] = i
    # keep file in rank order
    data["concepts"] = order
    data["counts"] = {
        "concepts": len(order),
        "relations": sum(len(c["rels"]) for c in order),
    }
    for c in built:
        blob = json.dumps(c, ensure_ascii=False)
        if "\\" in blob:
            raise SystemExit("backslash in new concept " + c["id"])
    text = json.dumps(data, indent=1, ensure_ascii=False)
    if not text.endswith("\n"):
        text += "\n"
    ATLAS.write_text(text, encoding="utf-8")
    print("counts", data["counts"])
    print("rank1", order[0]["id"], order[0]["rank"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Insert the v1.20 concepts into atlas.json.

Wording corrected after insertion by apply_audit_wording.py:
local means rather than a product-formula defect, E0 estimates rather than
certified brackets, the h1 edge split at a fixed a0, the band-limit reason
a finite H^{1,1} cannot carry W, and the two-sector criterion. Re-running
this script exits once the ids exist.

Existing priorities and the relative order of existing concepts stay as they are.
New concepts are placed after the existing block of the same priority.
No concept is marked as one of the ten missing pieces. Rank 1 is not edited.
"""
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "atlas.json"

NEW = [
    dict(
        id="window_energy_ledger",
        name="Exact window ledger: the Weil form is the pole term plus a bulk form",
        aliases=["W = P + B", "window energy ledger"],
        plain="On a log window the Weil form splits as a pole term P plus a bulk form B. The bulk form is nonnegative spring energy minus a diagonal counterterm. Killing the poles removes P and leaves the counterterm in place. The split is an identity. It does not sign W.",
        label="Theorem",
        core="For a window test F, W(F) = P(F) + B(F). For a general complex test, P = 2(|C|^2 - |S|^2) = 2 Re(C+ conjugate C-). For real F, P = 2 ev+ ev- = 2(C^2 - S^2). B = H_A - M_A times the norm squared, and the same B is (1/2 pi) times the integral of m_A |Fourier F|^2. H_A adds the archimedean Levy springs and the prime springs for log n < A; each spring is nonnegative. M_A = -K0 + 2 sum Lambda(n) n^(-1/2), with K0 = psi(1/4) - log pi = -5.37218. The formula for B is valid off E0 as well as on it. W equals B on the joint kernel of the two moment functionals, which contains E0. This restates the v1.19 spring identity with the pole term kept visible off E0.",
        formula="W = P + B, B = H_A - M_A ||F||^2, E0 kills P only",
        numbers=["K0 = psi(1/4) - log pi = -5.3721834192256654, from the session ledger."],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Algebraic completion of the square for real translations, on the prior archimedean Levy kernel. Checked again in notes/v120/tests/audit_v120.py for K0 and for P vanishing on E0.",
        tests="A sign for B on every window test in E0 would be Weil positivity. The identity does not supply it.",
        pitfalls=[
            "Do not write W = B off E0. Full W is B + P.",
            "Do not say that E0 removes the counterterm. E0 kills P. The diagonal M_A ||F||^2 remains inside B.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "weil_positivity", "note": "on E0 the inequality is Weil positivity rewritten; the ledger does not prove it"},
            {"type": "refines", "to": "spring_energy_counterterm_split", "note": "same completed square, with P kept visible off E0"},
            {"type": "distinguishes", "to": "pole_plane", "note": "P is the pole term; B is the bulk, including the diagonal counterterm"},
        ],
    ),
    dict(
        id="pole_form_P_2ReCplusCminus",
        name="The pole term is 2(|C| squared minus |S| squared)",
        aliases=["P = 2 Re(C+ conjugate C-)"],
        plain="For a general complex test, P = 2(|C| squared minus |S| squared), which equals 2 Re(C+ times the conjugate of C-). For real F that agrees with 2 ev+ ev- = 2(C squared minus S squared). That real reduction is not claimed for a general complex test. P is the term E0 is built to kill.",
        label="Theorem",
        core="ev±(F) = integral F(u) exp(±u/2) du. For general complex F, P(F) = 2(|C|^2 - |S|^2) = 2 Re(C+ conjugate C-). For real F, P(F) = 2 ev+ ev- = 2(C^2 - S^2). On a centered window, reflection splits this into a rank-one positive update on the even sector and a rank-one negative update on the odd sector: W_even = B_even + 2 c c^T and W_odd = B_odd - 2 s s^T. Globally the moment functionals are unbounded, so E0 is dense among square-integrable functions. On one finite window both exponentials are square-integrable, so the kernel is closed of codimension 2. That topological distinction is already in v1.19.",
        formula="P = 2(|C|^2 - |S|^2) = 2 Re(C+ conjugate C-); real F: 2 ev+ ev- = 2(C^2 - S^2)",
        numbers=[],
        axes=["reference/pole/cusp", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Definition of the pole term in the explicit formula, rewritten in even-odd and complex coordinates.",
        tests="",
        pitfalls=["The even formula alone is not E0. The odd sector has its own constraint."],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "pole_plane", "note": "same pole term, written as a product of moments"},
            {"type": "distinguishes", "to": "e0_dense_window_kernel_closed", "note": "E0 kills P; density is global and closed codimension 2 is one window"},
            {"type": "refines", "to": "window_energy_ledger", "note": "P is the first summand"},
        ],
    ),
    dict(
        id="bulk_form_B_off_E0",
        name="The bulk form B keeps the diagonal counterterm, on E0 and off it",
        aliases=["B = H_A - M_A norm squared"],
        plain="B is the spring energy minus M_A times the norm squared. It is defined for every window test, not only for E0. On E0 it coincides with W, because P has been killed. Off E0, W and B differ by P.",
        label="Theorem",
        core="B(F) = H_A(F) - M_A ||F||^2 = (1/2 pi) integral m_A(x) |Fourier F(x)|^2 dx, with m_A the archimedean symbol minus the cosine sum over log n < A. The symbol tends to infinity with |x|, so on E0 the form B is unbounded and not of finite rank. A finite-dimensional target, a finite conic or a finite primitive H^{1,1}, cannot reproduce it. The right size of a geometric target is not constructed.",
        formula="B = H_A - M_A ||F||^2 = (1/2 pi) integral m_A |F-hat|^2",
        numbers=[],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="Self-adjointness, compact resolvent, and discrete spectrum of the infinite-dimensional operator B are not proved. Finite Galerkin matrices are the setting of the inertia counts.",
        proved="The quadratic-form identity is the ledger. Unboundedness of the symbol is the reason a finite-rank pullback cannot match B on E0.",
        tests="Do not promote a finite positive Galerkin matrix to analytic positivity.",
        pitfalls=[
            "Finite H^{1,1} cannot automatically represent infinite-dimensional E0.",
            "B inverse applied to the constraint vector is not an independent constructor, and the infinite-dimensional domain is unproved.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "window_energy_ledger", "note": "B survives on E0, diagonal included"},
            {"type": "contrasts-with", "to": "pole_form_P_2ReCplusCminus", "note": "off E0, W is B plus P"},
            {"type": "constrains", "to": "mp_d8", "note": "a finite ample class cannot carry this unbounded form; nothing here constructs a replacement"},
        ],
    ),
    dict(
        id="local_product_state_covariance",
        name="Each local term is a product-state covariance, and that covariance is subtracted",
        aliases=["AR(1) prime covariance", "OU tower"],
        plain="Every local piece of the ledger has a product-state reading. A prime contributes log p times the norm squared minus a positive AR(1) covariance. The archimedean place is an Ornstein-Uhlenbeck tower. The positive covariances enter with a minus sign. They account for the terms. They do not make B positive.",
        label="Theorem",
        core="W_p(F) = log p ( ||F||^2 - <F, P_p F> ), where P_p = sum_k p^(-|k|/2) T_{k log p} is positive semidefinite, the covariance of a critical boson, or an AR(1) process. The archimedean symbol is the OU tower with rates (2j+1)/2. E0 is the statement that the rate-1/2 OU response is supported in the window. The individual prime responses leak: their local poles cancel only when all places are kept together. This is an exact term-by-term reading. As a source of the sign it is closed.",
        formula="W_p = log p (||F||^2 - <F, P_p F>), P_p positive semidefinite",
        numbers=[
            "Session, A = 2, G = sin^8, uncertified: arch +0.090, p = 2 about +9.092, p = 3 about -9.001, p = 5 about -0.0016, spring total 0.1788.",
            "Rounded displayed parts sum to 0.1794. The cancellation is the point of the figure, not a certificate.",
        ],
        axes=["sign/positivity (Ax2)", "physics analogue", "ghost-blind"],
        uncertain="",
        proved="The prime identity is completion of the square against a positive Toeplitz covariance. Positivity of a finite section is linear algebra and is rechecked for a short AR(1) block in the v1.20 audit.",
        tests="Must not be quoted as a sign mechanism. The covariance is subtracted.",
        pitfalls=[
            "Closed as a sign source, on this reading: a subtracted positive form does not dominate the diagonal by itself.",
            "Not a universal theorem that no positive compression can ever match W. The tested compressions mismatched W. That is a smaller statement.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "window_energy_ledger", "note": "place-by-place reading of the same ledger"},
            {"type": "contrasts-with", "to": "weil_positivity", "note": "closed as a sign source; covariances are subtracted"},
            {"type": "contrasts-with", "to": "positive_weight_not_normalized_state", "note": "a positive weight for W is still only a target; these local covariances are already signed into the explicit formula"},
        ],
    ),
    dict(
        id="product_formula_defect_mean",
        name="The counterterm is the expected, truncated, product-formula defect",
        aliases=["M_A as a mean of log |x|_v"],
        plain="The diagonal coefficient M_A is what the product formula would contribute if each place were replaced by its truncated expectation of log |x|_v. It is bookkeeping for the constant term. It is not a proof that the bulk form is positive.",
        label="Theorem",
        core="The session identity is M_A = -2 sum_v E_v[ log |x|_v truncated to the window ]. The sum runs over the archimedean place and the primes with log p inside the cutoff that defines A. This is why M_A = -K0 + 2 sum a_n with a_n = Lambda(n) n^(-1/2). The product formula itself, product over places of |x|_v = 1, is classical. The expectation is a reading of the constant that the ledger already isolates.",
        formula="M_A = -2 sum_v E_v[log |x|_v ^(A)] = -K0 + 2 sum_{log n < A} a_n",
        numbers=["At A = 2 the session records M_A = 11.22465. At A = 1, M_A = 6.35244. At A = 0.6, with no prime inside, M_A = -K0 = 5.37218."],
        axes=["reference/pole/cusp", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="The second expression is the definition of M_A used throughout the ledger. The expectation form is the audited reading of that constant.",
        tests="",
        pitfalls=["A product formula fixes the constant. It does not sign the quadratic form."],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "local_product_state_covariance", "note": "the diagonal is the sum of the local expectations"},
            {"type": "illustrates", "to": "window_energy_ledger", "note": "M_A is the counterterm in B"},
            {"type": "uses", "to": "weil_positivity", "note": "bookkeeping only"},
        ],
    ),
    dict(
        id="twisted_star_convolution",
        name="The semilocal pairing uses a twisted involution, not the naive star of chi f",
        aliases=["(chi f) star = chi inverse f star"],
        plain="The weight chi(u) = exp(-u/2) has to sit inside the convolution in a definite way. The corrected involution satisfies (chi f) star = chi inverse times f star. Pairing two functions by the ordinary star of (chi f) with itself is a different, wrong, formula. No global phase c = 1 is claimed.",
        label="Theorem",
        core="With f star (u) = conjugate f(-u) and chi(u) = exp(-u/2), the identity (chi f) star = chi^(-1) f star is a one-line calculation, rechecked in the v1.20 audit. The semilocal distribution is h = chi times (f convolved with f star). Equivalently h = g convolved with g sharp, where g = chi f and g sharp (u) = exp(-u) conjugate g(-u). That sharp is not the ordinary star of g. The numbers computed in the session used the corrected h. A formal graph of a flow, built from the bulk pairing, is not a cycle class, not a numerical group, and not a Hodge structure.",
        formula="(chi f)* = chi^(-1) f*, chi(u) = exp(-u/2); h = chi · (f * f*)",
        numbers=[],
        axes=["structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="The involution identity is elementary and is rechecked by the audit script. The semilocal normalization is the correction recorded against the earlier scratch formula.",
        tests="",
        pitfalls=[
            "Do not replace the twisted sharp by (chi f) star (chi f) star.",
            "Do not claim a global Euler phase c = 1. That statement is formal only.",
            "A formal graph integral is not a cycle.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "corrects", "to": "connes_trace", "note": "semilocal pairing is tau of chi times (f1 convolved with f2 star), not the naive star"},
            {"type": "distinguishes", "to": "connes_trace", "note": "no claimed global factor c = 1"},
        ],
    ),
    dict(
        id="semilocal_scattering_phase_time_delay",
        name="Semilocal trace: the bulk symbol is a scattering time delay, not a Hodge theorem",
        aliases=["Connes cutoff phase", "Wigner delay of m_S"],
        plain="With finitely many places, enough to cover the window, the Connes trace identity says that a twisted pairing equals W minus P. The phase of that cutoff turns into the symbol of the bulk form by a logarithmic derivative. That is a scattering dictionary. It is not a sign theorem and it is not Hodge positivity.",
        label="Theorem",
        core="Connes 1999, Theorem VII.4, is the semilocal trace formula. The dictionary used here: for S containing the archimedean place and every prime p < exp(A), -I_S(F, F) = W(F) - P(F) on window tests. The semilocal Fourier transform factors as M_c times J, with a phase c_S, and -i d/dy log c_S = -m_S, so the symbol of W is the negative of that Wigner time delay. The identity is semilocal. A global Gamma-Euler product with phase identically 1 is not claimed. The trace is not the Hodge index.",
        formula="-I_S(F,F) = W(F) - P(F) for S covering the window; -i d/dy log c_S = -m_S",
        numbers=[],
        axes=["structure/frame (Ax1)", "ghost-blind"],
        uncertain="Convergence of the limiting traces is an assumption, flagged for any signed-leakage reading. X in the Hankel decomposition is numerical where a number is quoted.",
        proved="The trace formula is cited, not reproved. The phase-to-symbol step is the audited dictionary, exact inside that semilocal normalization.",
        tests="Must not be quoted as RH, and must not be quoted as a Hodge-index theorem.",
        pitfalls=[
            "Semilocal only. Finite S containing infinity and every p < exp(A).",
            "Not Hodge positivity.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "uses", "to": "connes_trace", "note": "Connes 1999, Theorem VII.4, semilocal"},
            {"type": "refines", "to": "bulk_form_B_off_E0", "note": "the bulk symbol is the negative Wigner delay of the semilocal phase"},
            {"type": "contrasts-with", "to": "hodge_index", "note": "a trace identity is not the Hodge index"},
            {"type": "uses", "to": "twisted_star_convolution", "note": "the pairing in I_S uses the twisted star"},
        ],
    ),
    dict(
        id="connes_cutoff_pair_two_hankel",
        name="Under trace-class assumptions the cutoff splits into two Hankel pieces minus a remainder",
        aliases=["D_c - D_cbar - X"],
        plain="Once the semilocal traces are assumed to exist, W minus P splits as a difference of two cutoff operators minus a remainder X. A positive compression of a cutoff was compared with W on a few tests and did not match. That mismatch is numerical. It is not a theorem that every compression fails.",
        label="Theorem",
        core="The audited identity, assuming the limiting traces exist for the test class: W - P = D_c - D_cbar - X. The positive compression Q = S P-hat S was larger than or equal to W on three tests at A = 1, and at A = 0.6 the compression still depended on the set S while W did not. Those comparisons are double precision and uncertified. They close the tested compressions. They are not a universal no-go.",
        formula="W - P = D_c - D_cbar - X, assuming the traces exist",
        numbers=["Tested compressions: D depends on S at A = 0.6 while W does not; D is at least W on three tests at A = 1. Numerical, uncertified."],
        axes=["structure/frame (Ax1)", "numerics/certificate", "ghost-blind"],
        uncertain="The trace-class limit is assumed, not proved, for the signed-leakage reading.",
        proved="The splitting is exact inside that assumption. The comparison with W is numerical.",
        tests="Do not promote the mismatch to a theorem that no positive operator compression can equal W.",
        pitfalls=["Positive on a finite compression is not analytic positivity, and it is not automatically W."],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "semilocal_scattering_phase_time_delay", "note": "Hankel form of the same semilocal trace, under a limit assumption"},
            {"type": "contrasts-with", "to": "weil_positivity", "note": "tested positive compressions mismatched W; not a universal impossibility"},
            {"type": "contrasts-with", "to": "norm_identity_iff_weil_not_four_criteria", "note": "a compression that is positive and unequal to W does not meet the norm identity"},
        ],
    ),
    dict(
        id="bordered_inertia_moment_criterion",
        name="Finite bordered inertia: index 0, or index 1 with q at most 0",
        aliases=["Haynsworth on one constraint", "q = c^T B inverse c"],
        plain="For a finite invertible symmetric matrix B and one nonzero constraint c, positivity on the hyperplane c perpendicular holds in exactly two cases. Either B is already positive semidefinite, or B has exactly one negative direction and the scalar q = c^T B inverse c is less than or equal to zero. Two or more negative directions cannot be removed by one constraint. This is linear algebra. It is not yet a theorem about the infinite-dimensional bulk form.",
        label="Theorem",
        core="Let B be real symmetric and invertible, c nonzero, q = c^T B inverse c. The negative index of B on the kernel of c is n-(B) - 1 + 1 when q > 0, and n-(B) - 1 when q <= 0. The nullity of the restriction is 1 when q = 0 and 0 otherwise. The restriction is therefore positive semidefinite if and only if n-(B) = 0, in which case q is necessarily positive, or n-(B) = 1 and q <= 0. If n-(B) >= 2 the restriction still has a negative direction. The parent audit gives the congruence proof. Infinite-dimensional use needs B invertible on a stated domain and c in the domain of B inverse. Those hypotheses are not verified for the window operator. The vector B inverse c is defined from B. It is not an independent constructor.",
        formula="n-(B on c-perp) = n-(B) - 1 + [q > 0], q = c^T B^{-1} c",
        numbers=[
            "Session, uncertified, even sector: one negative mode, alignment of cosh with it 0.970 at A = 0.6 and 0.991 at A = 1.",
            "E0 brackets, Ritz upper bounds against a Nystrom tail, uncertified: [0.6918, 0.6920] at A = 0.6 and [0.01182, 0.01197] at A = 1.",
            "A = 2 is unresolved. Do not quote a second eigenvalue as certified.",
        ],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="Operator invertibility and the existence of B inverse applied to cosh, in infinite dimensions, are unproved.",
        proved="The finite-dimensional inertia count is Haynsworth's congruence, specialized in the parent audit and rechecked on sample matrices by the v1.20 audit, including the index-0 case where q is positive and the restriction is still positive semidefinite.",
        tests="Both parity sectors are required. An even-only condition is not E0.",
        pitfalls=[
            "The blanket slogan n- <= 1 and q <= 0 is wrong at index 0: a positive definite B has q > 0 and the restriction is positive semidefinite.",
            "q is not a free parameter. If the index is 0, q is positive automatically.",
            "Do not quote an apparent second eigenvalue at A = 2, from either basis, as a verified eigenvalue. The two session pictures disagree and neither is certified.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "uses", "to": "haynsworth_pole_plane_split_windows", "note": "inertia additivity for a bordered symmetric matrix; here one constraint and an invertible finite B"},
            {"type": "constrains", "to": "weil_positivity", "note": "finite-matrix shape of the comparison; not an infinite-dimensional theorem"},
            {"type": "constrains", "to": "bulk_form_B_off_E0", "note": "B inverse c requires an invertibility hypothesis that is unproved for the operator"},
        ],
    ),
    dict(
        id="even_odd_sector_constraints",
        name="Both parity sectors carry a constraint; the even test is not E0",
        aliases=["even cosh and odd sinh"],
        plain="On a centered window, reflection preserves the bulk form. Cosh is even and sinh is odd, so E0 splits into an even constraint and an odd constraint. Positivity on E0 is the bordered criterion in the even block and the bordered criterion in the odd block. One of them is not enough.",
        label="Theorem",
        core="The reflection RF(u) = F(-u) commutes with B, because the symbol is even, and it commutes with P. For a reflection-invariant Galerkin space, E0_A is the orthogonal sum of (even functions perpendicular to cosh) and (odd functions perpendicular to sinh). Each block needs the finite bordered criterion, assuming that block is invertible. In the A = 0.6 and A = 1 runs the odd block had negative index 0. That is numerical, not a general fact. Full-window W, a different question: if the even block has index 1 and is invertible, then W_even is positive semidefinite if and only if q_even <= -1/2. If the odd block is positive definite, W_odd is positive semidefinite if and only if q_odd <= 1/2.",
        formula="E0 = (even ∩ cosh-perp) ⊕ (odd ∩ sinh-perp), both required",
        numbers=["Odd-sector negative index 0 at A = 0.6 and A = 1 is numerical, uncertified, and not claimed in general."],
        axes=["sign/positivity (Ax2)", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="The splitting is symmetry of an even symbol. The inertia conditions are the finite bordered lemma applied twice. Rechecked as linear algebra in the audit, not as an operator theorem.",
        tests="An estimate that uses only even tests does not see E0.",
        pitfalls=[
            "q_even near -1/2 sits at the Sherman-Morrison threshold for full W. No claim about positivity of full W is made from that numerical proximity.",
            "Full W near a threshold is not a statement that W is positive.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "bordered_inertia_moment_criterion", "note": "one application in each parity sector"},
            {"type": "illustrates", "to": "pole_form_P_2ReCplusCminus", "note": "even update +2cc^T, odd update -2ss^T"},
            {"type": "distinguishes", "to": "e0_dense_window_kernel_closed", "note": "two constraints on one window; not one even condition"},
        ],
    ),
    dict(
        id="near_null_cluster_A2",
        name="At width 2 the near-null cluster is unresolved across bases",
        aliases=["A = 2 spectrum not certified"],
        plain="Two numerical pictures of the same width disagree about a cluster of tiny values. One basis shows several eigenvalues near 10^(-3). Another shows values near 10^(-15). Both are uncertified. Neither number is an eigenvalue of the bulk form.",
        label="Numerical",
        core="map1965, sine Galerkin, reports a cluster of small positive values around 8·10^(-4), and that picture moves when prime couplings are scaled by 1.002. moment1975 reports a near-null scale around 10^(-15). Different bases, different quadrature. The audit leaves both unresolved. A second even value that seems to cross through zero under a prime-2 scaling is a count in one matrix, not a certified gap. Finite positive Galerkin values remain upper bounds on minima when they come from a Rayleigh-Ritz projection. They are not analytic positivity.",
        formula="",
        numbers=[
            "Do not quote either cluster as spec(B).",
            "Alignment figures 0.970 and 0.991, and the E0 brackets at A = 0.6 and A = 1, are the same uncertified class.",
        ],
        axes=["numerics/certificate", "sign/positivity (Ax2)"],
        uncertain="No certified spectral gap at A = 2, and no certified second eigenvalue.",
        proved="",
        tests="A later certified enclosure would have to name its basis, its quadrature error, and an interval that both present pictures can meet. Nothing here does that.",
        pitfalls=[
            "Apparent lambda_2 is not a verified eigenvalue.",
            "A positive finite matrix does not prove positivity of the form.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "obstructs", "to": "bordered_inertia_moment_criterion", "note": "the index count at A = 2 is not certified, so the criterion cannot be evaluated there"},
            {"type": "contrasts-with", "to": "spring_galerkin_near_cancellation", "note": "another finite positive minimum; still an upper bound, still not analytic positivity"},
        ],
    ),
    dict(
        id="independent_representer_test",
        name="Two explicit representers fail; an independent matching map is still missing",
        aliases=["h1 and h2", "missing matching theorem"],
        plain="The bordered criterion would become a construction if a vector h were built from Gamma data, prime data, and the boundary, without inverting B, and if that vector carried the constraint and a negative square. Two candidates were written down in advance. Both fail. The failure of those two is proved, on the stated domain. A general no-go is not.",
        label="Theorem",
        core="The identity asked for is B(h, F) = kappa C(F) on the window, equivalently a response equal to kappa cosh(v/2) almost everywhere, for even h. h1 = cosh(u/2) times the window indicator fails at A = 0.6 and at A = 1 because the response over cosh blows up at the edge like (1/2) log(1/d). That mechanism is exact. h2, the Dirichlet cosh, removes the edge logarithm. At A = 1, where the only prime power inside the window is 2, h2 fails because the response has a slope jump a_2 sinh(A/4)/2 = 0.06191 at ±(log 2 - A/2). That jump is exact under those hypotheses. At A = 0.6 the h2 residual is 6.92 percent, numerical only. Polynomial tests F = (d^2/du^2 - 1/4)G with G = (1-t^2)^2 t^k are piecewise polynomial, not smooth; they lie in the form domain, and they lie in E0 by integration by parts using G = G' = 0 at the edges. They disprove the identity on that domain. The smooth case of h1 and of h2 at A = 1 goes through the annihilator lemma. Density of smooth E0 tests in the form domain is plausible and not proved. The missing theorem is a vector h_A, built independently of B inverse, with the full response including M_A and every prime edge, with B(h_A, h_A) < 0, and with both sector conditions. The sector count is the RH-strength half. No such vector is constructed.",
        formula="B(h, ·) = kappa C on E0 tests iff the response lies in span{cosh, sinh}",
        numbers=[
            "h1 least-squares residuals, numerical: 37.9 percent at A = 0.6, 19.1 percent at A = 1.",
            "h2 at A = 1, numerical residual about 3.0 percent, on top of the exact jump.",
            "h2 at A = 0.6: residual 6.92 percent, stable across three grids, still only numerical.",
            "Finite-difference jump at eps = 10^(-4): 0.06189, against 0.06191.",
        ],
        axes=["open target", "sign/positivity (Ax2)", "ghost-blind"],
        uncertain="Missing theorem, not a result: construct h_A from Gamma, prime, and boundary data, independently of B inverse, so that B(h_A, F) = kappa C(F) + kappa' S(F) for every window F, including the diagonal M_A and the prime-translated edge layers; B(h_A, h_A) < 0; and both sector conditions hold. A finite singular orbit, a 1/log edge law, and a Gamma-only no-go are conjectural. Whether B inverse cosh equals cosh minus a finite edge-layer sum is a conjecture, and only when the inverse exists.",
        proved="Failure of h1 at both widths, and failure of h2 at A = 1 under log 2 < A < log 3, on the form domain and on smooth tests via the annihilator lemma. Parent audit, Propositions 4 and 5.",
        tests="A proposed h that is defined as B inverse c, or that is checked only on even tests, or that drops the prime shifts, does not meet the missing theorem.",
        pitfalls=[
            "Only these two candidates are excluded. There is no universal Gamma-only no-go.",
            "B inverse c is not an independent constructor.",
            "Infinite-dimensional invertibility is unproved.",
            "The Riemann Hypothesis is not proved.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "illustrates", "to": "bordered_inertia_moment_criterion", "note": "the Sylvester shape the missing h would have to meet; not a construction"},
            {"type": "constrains", "to": "mp_castelnuovo", "note": "still missing; this entry does not construct a positive involution"},
            {"type": "constrains", "to": "no_ghost_missing_piece", "note": "H+ identified with W, without assuming the sign, is not built; Open ~1.8 unchanged"},
            {"type": "constrains", "to": "kahler_triple_polarization", "note": "no compatible J; rank 1 unchanged"},
            {"type": "uses", "to": "bulk_form_B_off_E0", "note": "the response must include the diagonal M_A and the prime shifts"},
        ],
    ),
    dict(
        id="prime_edge_kink_orbit",
        name="At width 1 the second candidate fails by a prime-2 kink of slope 0.06191",
        aliases=["edge kink", "a_2 sinh(A/4)/2"],
        plain="The Dirichlet candidate is smooth inside the window, so the archimedean part of its response is smooth there. The shift by log 2 brings a kink of the window edge into the interior. The slope jumps by a_2 sinh(A/4)/2. A combination of cosh and sinh has no jump, so the candidate is not a representer. The same sentence for every representer, at every width, is a conjecture.",
        label="Theorem",
        core="Hypotheses: A = 1, so log 2 < A < log 3 and the only prime power in the sum is n = 2. h2 is Lipschitz, with kinks at the two window edges, hence in the form domain. On the open window the archimedean integrals are analytic in the edge distances, and h2 itself is analytic. The translate by log 2 is supported up to A/2 - log 2 and contributes a slope jump a_2 sinh(A/4)/2 = 0.06191, with a_2 = log(2)/sqrt(2). The opposite edge gives the symmetric jump. No other shift enters. The annihilator lemma then excludes span{cosh, sinh}. For a general width, several shifts can land on the same point and cancel. No claim is made. The guess that every representer carries a finite singular orbit, or that the edge profile is a universal 1/log law, needs a propagation argument that is not given.",
        formula="jump = a_2 sinh(A/4)/2 = 0.06191 at A = 1, n = 2 only",
        numbers=["Finite difference at spacing 10^(-4): 0.06189. At spacing 10^(-3): 0.06172. Prediction 0.06190632."],
        axes=["sign/positivity (Ax2)", "numerics/certificate", "ghost-blind"],
        uncertain="A finite edge-orbit ansatz, a universal 1/log law, and a Gamma-only no-go are conjectures.",
        proved="The jump computation and the annihilator step, under the hypotheses above. The audit script recomputes the exact jump and one finite difference.",
        tests="",
        pitfalls=[
            "Exact only for this width, where a single prime power enters.",
            "The numerical residual of h2 at A = 0.6 is not this exact jump.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "obstructs", "to": "independent_representer_test", "note": "h2 fails at A = 1 by this jump; h1 fails by the log edge; h2 at A = 0.6 is numerical only"},
            {"type": "contrasts-with", "to": "independent_representer_test", "note": "the universal orbit, the 1/log law, and a Gamma-only no-go stay conjectural"},
        ],
    ),
    dict(
        id="conic_polarity_one_form",
        name="One model form: a null conic, a timelike point, and a positive polar",
        aliases=["model null conic Q = 0", "polarity model"],
        plain="A single quadratic form on a plane can be indefinite, negative on one vector, and positive on the polar of that vector. The zero set is a conic. Drawn in an affine chart it is the parabola q = t squared over 4. That curve is a discriminant boundary of the model. It is not a Hasse wall, not the parabolic wall, not the Routh wall, and not a sheet of Sigma. Focus and directrix are extra Euclidean structure on the chart.",
        label="Analogy",
        core="B(v, v) = v_T^2 - 4 v_Q v_Z. The null set Q = 0 is a smooth conic. The point h = (0:1:1) has Q(h) = -4. On its polar, Q = v_T^2 + 4 v_Z^2, which is positive definite. The axis span(h, x_infinity) has signature (1, 1), and x_infinity = (0:1:0) is null. Its polar is Z = 0, which contains x_infinity, so the complement is degenerate. Sylvester's law in this finite dimension: one negative square and Q(h, h) < 0 imply positivity on the polar. This is the shape the bordered criterion asks for. It constructs neither h nor a sign for W. The point-counting ellipse that the atlas already identifies with the Hasse bound is a different form.",
        formula="Q = T^2 - 4 Q Z; Q(h) = -4; Q on h-perp = v_T^2 + 4 v_Z^2",
        numbers=["Hand algebra, rechecked by the v1.20 audit. Not a numerical fit."],
        axes=["physics analogue", "sign/positivity (Ax2)", "ghost-blind"],
        uncertain="",
        proved="The three-by-three algebra and Sylvester's law on that matrix. Nothing about zeta.",
        tests="Must not be read as a construction of a polarization for W.",
        pitfalls=[
            "Do not call this null conic a Hasse wall.",
            "Do not call it the parabolic wall or the Routh wall.",
            "Interior focus and polar directrix are extra Euclidean structure of the affine parabola.",
            "Smooth at infinity. Not a modular cusp. The polar of x_infinity has no affine intercept.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "analogue-of", "to": "hodge_index", "note": "model of a sign pattern: one negative direction, positive complement; not a constructor"},
            {"type": "distinguishes", "to": "two_walls_parabolic_routh", "note": "parabolic wall and Routh wall stay separate from this model curve"},
            {"type": "distinguishes", "to": "parabolic_edge", "note": "the Jordan edge |trace| = 2 is not this picture"},
            {"type": "distinguishes", "to": "conic_type_at_infinity", "note": "the point-counting ellipse is the Hasse bound for that form; it is not this null conic"},
            {"type": "distinguishes", "to": "weil_discriminant_wall_S2_23", "note": "primary and secondary sheets of Sigma stay separate"},
            {"type": "distinguishes", "to": "beurling_incidence_no_toy_certificate", "note": "the Beurling-pencil Hasse wall is that pencil, not this model"},
            {"type": "constrains", "to": "mp_d8", "note": "finite-dimensional model only; it cannot carry full-rank W"},
        ],
    ),
    dict(
        id="polar_family_h_s_degeneration",
        name="A polar family shrinks to the null point at infinity, in two gauges",
        aliases=["h_s = (0, 1, s)", "gauge of Q"],
        plain="Move the interior point from h = (0:1:1) toward x_infinity by h_s = (0:1:s), with s from 1 down toward 0. On that homogeneous representative, Q = -4s, which tends to 0. The same projective point, normalized to affine height q = 1/s, has Q = -4/s, which tends to minus infinity. Both statements are right. They are different normalizations. The sign stays negative for s > 0, and the projective limit is the null point x_infinity either way.",
        label="Analogy",
        core="Q(0, 1, s) = -4s. The affine representative (0, 1/s, 1) has Q = -4/s. The ratio of the two numbers is the square of the scaling factor 1/s. On the polar v_Z = -s v_Q the form is v_T^2 + 4 s v_Q^2. Its level set equal to 1 is an ellipse. As s tends to 0 that ellipse lengthens toward the pair of lines v_T = ±1. The filled sublevel, the set where the form is at most 1, lengthens toward the strip |v_T| <= 1. The level set does not become the strip. At s = 0 the polar of x_infinity is the line Z = 0, which does not meet the affine chart. The conic is smooth at x_infinity: in the chart Q = 1 it is the parabola T^2 = 4Z. That point is not a cusp of the modular curve.",
        formula="Q(0,1,s) = -4s; Q(0, 1/s, 1) = -4/s; level set tends to lines, sublevel tends to a strip",
        numbers=["At s = 1 the two gauges agree at -4. At s = 0.05 they read -0.2 and -80. Same point, same sign, different scale."],
        axes=["physics analogue", "structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Homogeneous scaling of a quadratic form, Q(lambda v) = lambda^2 Q(v), and the elementary limit of the ellipse. Rechecked in the audit.",
        tests="",
        pitfalls=[
            "Do not treat -4s and -4/s as the same measurement.",
            "Do not say the level set becomes a strip. The filled sublevel does.",
            "Not a physical recording. Schematic algebra.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "refines", "to": "conic_polarity_one_form", "note": "the same model, with the gauge of h_s written twice"},
            {"type": "distinguishes", "to": "conic_type_at_infinity", "note": "x_infinity of this model is a smooth point; its polar has no affine intercept; not a modular cusp"},
        ],
    ),
    dict(
        id="kunneth_skew_to_symmetric",
        name="A skew pairing on H1 becomes symmetric on the product, with both signs",
        aliases=["I = -E tensor E", "mixed (1,1) versus (2,0)+(0,2)"],
        plain="On a curve the intersection of 1-forms is alternating. On the product of the curve with itself, the Kunneth rule turns that into a symmetric form, minus the product of the two pairings. For an elliptic curve of area 1 the mixed real primitive class of type (1,1) squares to -8. The real class in types (2,0) and (0,2) squares to +8. One sign pattern, two signs. Not every class is negative.",
        label="Theorem",
        core="E(u, v) = integral u wedge v. Holomorphic and antiholomorphic forms are isotropic, and i times the integral of alpha wedge its conjugate is positive on H^{1,0}. The product pairing is I(a tensor b, c tensor d) = -E(a, c) E(b, d). With E(dz, d z-bar) = -2i, the mixed vector dz tensor d z-bar plus d z-bar tensor dz has square -8. The vector dz tensor dz plus d z-bar tensor d z-bar has square +8. The mixed sector is not the whole primitive H^{1,1}. This is hand algebra for one normalization. It is not a map from E0.",
        formula="I = -E ⊗ E; mixed real primitive square -8; (2,0)+(0,2) square +8",
        numbers=["Area-1 normalization. Exact, rechecked symbolically in the v1.20 audit."],
        axes=["geometry over F_q", "sign/positivity (Ax2)", "ghost-blind"],
        uncertain="",
        proved="Bilinear expansion of the Kunneth rule on the two real vectors. Finite dimensional. Not a theorem about W.",
        tests="",
        pitfalls=[
            "Do not say that all of H^{1,0} tensor H^{0,1} is negative.",
            "Do not identify this calculation with a polarization for zeta.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "illustrates", "to": "hodge_index", "note": "a finite sign pattern with both a negative and a positive direction"},
            {"type": "contrasts-with", "to": "hodge_index", "note": "the mixed vector is not the whole primitive lattice"},
            {"type": "analogue-of", "to": "conic_polarity_one_form", "note": "same moral, different model: one form, two signs, no constructor"},
        ],
    ),
    dict(
        id="nonstationary_J_obstruction",
        name="A translation-invariant complex structure does not preserve the window kernel",
        aliases=["Hilbert-transform J", "non-stationary J"],
        plain="If the metric is translation-invariant and nonnegative, the Hilbert transform supplies a complex structure compatible with it. That operator does not preserve compact support, and it does not preserve E0. A complex structure for the window form has to move with the window. None has been built. Rank 1 and the open score near 1.8 are unchanged.",
        label="Theorem",
        core="On the line, a nonnegative translation-invariant symbol has the Hilbert transform as a compatible J: the Hamiltonian vector field is minus J times the gradient, and real and imaginary time differ by that J. The Hilbert transform of a compactly supported function is not compactly supported. The two moment constraints that cut out E0 are not preserved. So a J for the window sector, if it exists, is not a convolution operator. Robertson-Schrödinger positivity is positivity of a covariance, diagonals plus a determinant of a 2 by 2 block, once an observable is chosen. There is no canonical time operator in that identity. Weight-12 modular calibrations, including E10 = E4 E6, B10 = 5/66, and the Wronskian of Q^3 and R^2, were rechecked symbolically in the session. They do not select the archimedean counterterm: 2(psi(k/2) - log 2 pi) is not k/12.",
        formula="X_H = -J grad H; Hilbert J does not preserve C_c or E0",
        numbers=["B10 = 5/66. The weight identity 2(psi(k/2) - log 2 pi) versus k/12 fails at the weights checked in k0_weight.txt."],
        axes=["structure/frame (Ax1)", "sign/positivity (Ax2)", "ghost-blind"],
        uncertain="",
        proved="The support obstruction for the Hilbert transform is classical Fourier analysis and is the exact finite-dimensional-versus-window point recorded here. The modular identities are symbolic and were already checked in the session script fam1954_exact.py; the weight mismatch is an inequality of special values.",
        tests="A proposed J that is a convolution, or that is positive for a Beurling system as well, does not answer rank 1.",
        pitfalls=[
            "This obstruction does not construct a non-stationary J.",
            "Open ~1.8 is unchanged. Rank 1, kahler_triple_polarization, is unchanged.",
            "Weight 12 is a calibration, not the counterterm K0.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "constrains", "to": "kahler_triple_polarization", "note": "translation-invariant J is obstructed on E0; no replacement is built; rank 1 unchanged"},
            {"type": "contrasts-with", "to": "mp_castelnuovo", "note": "no progress on the missing positive involution"},
            {"type": "contrasts-with", "to": "positive_weight_not_normalized_state", "note": "a covariance identity still needs a chosen observable; it does not time the flow"},
        ],
    ),
    dict(
        id="iwasawa_regularity_class",
        name="Regularity of a local ring is not a global principal generator, and not a sign",
        aliases=["Jacobian class in m/m^2", "Noetherian is not Noether"],
        plain="A power-series ring over the p-adic integers is regular of dimension 2. Quotienting by one equation leaves a regular ring exactly when that equation is nonzero in m/m squared. That is a Jacobian condition. The Iwasawa numbers mu, lambda, and nu measure growth. They are not this Jacobian class, and they do not carry a sign. A regular local ring is a unique factorization domain. A global ring of integers need not be. Noetherian is a finiteness condition on ideals, not a Noether charge in mechanics.",
        label="Theorem",
        core="Lambda = Z_p[[T]] is regular local of dimension 2. Lambda/(f) is regular if and only if f is not in m squared. The element T squared - 27 is a singular example, an arithmetic cusp in that local model. Auslander-Buchsbaum says a regular local ring is a UFD. Z[sqrt(-5)] is Noetherian and not a UFD: 6 = 2·3 = (1+sqrt(-5))(1-sqrt(-5)), and 2 and 1+sqrt(-5) are irreducible because no element has norm 2. This does not reopen a global Jacobian, a Rosati involution, or a Picard lattice. Those routes stay at whatever status the atlas already gave them. The toy separates a growth invariant from a rank in m/m squared. It supplies no positivity.",
        formula="regular local <=> f not in m^2; regular local => UFD; not conversely for global rings",
        numbers=["Norm form a^2 + 5 b^2 never equals 2. Class number 2 for Q(sqrt(-5)) is the classical citation, not recomputed here."],
        axes=["structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="The norm obstruction in Z[sqrt(-5)] is rechecked by the audit. Auslander-Buchsbaum and the Iwasawa growth formula are cited.",
        tests="",
        pitfalls=[
            "Do not translate Noetherian into a Noether charge.",
            "Do not promote a local UFD to a global principal generator.",
            "Closed Jacobian, Rosati, and Picard paths are not reopened.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "distinguishes", "to": "reverse_substitution_dictionary", "note": "mu, lambda, nu are growth; the Jacobian condition is a class in m/m^2; neither signs W"},
            {"type": "illustrates", "to": "capitulation_keeps_pole", "note": "principalization can trivialize divisibility and still leave the pole; local factoriality is not global principality"},
            {"type": "contrasts-with", "to": "herbrand_ribet_spectral_no_positivity", "note": "Iwasawa data without a polarization still do not give the sign"},
        ],
    ),
    dict(
        id="rankin_selberg_square_calibration",
        name="Rankin-Selberg unfolding produces square coefficients, not the Weil form",
        aliases=["tau(n) squared", "Petersson norm stays positive"],
        plain="The integral of y to the 12, times |Delta| squared, times an Eisenstein series, unfolds to a Gamma factor times the Dirichlet series of tau(n) squared. The coefficients are squares because the interior pairing is positive and the unfolding is honest. Self-adjointness of Hecke operators makes tau(p) real. None of this is an identity for W. The Petersson norm of Delta is a finite positive number. Decay of the cusp integrand is why that integral converges. It is not a degeneration of the pairing.",
        label="Cited",
        core="Rankin (1939) and Selberg (1940): the integral of y^12 |Delta|^2 E(z, s) d mu equals Gamma(s+11) (4 pi)^(-(s+11)) times sum tau(n)^2 n^(-(s+11)). The atlas already records a positive Petersson norm, about 1.035·10^(-6). Congruences such as the one at 691 are arithmetic. They are not real positivity of W. A positive-definite lattice extracted from a Rankin-Selberg explicit formula is a different theorem and is not a formula for the Weil form on log-window tests.",
        formula="integral y^12 |Delta|^2 E(z,s) = Gamma(s+11) (4 pi)^(-(s+11)) sum tau(n)^2 n^(-(s+11))",
        numbers=["<Delta, Delta> about 1.03536205680432e-6, already in the atlas, finite and positive."],
        axes=["structure/frame (Ax1)", "ghost-blind"],
        uncertain="",
        proved="Cited unfolding. Not reproved here. The negative statement is that the identity does not mention W.",
        tests="Must not be used as a bridge from square coefficients to Weil positivity.",
        pitfalls=[
            "Square coefficients are not W.",
            "Cusp decay is convergence of the integral, not degeneration of the norm.",
            "The weight-12 calibration is not the archimedean counterterm.",
        ],
        lemmas=[],
        spec=0.05,
        rels=[
            {"type": "illustrates", "to": "cusp_forms_petersson", "note": "positive interior pairing, square coefficients, no information about zeta zeros"},
            {"type": "contrasts-with", "to": "weil_positivity", "note": "no identity with W"},
            {"type": "distinguishes", "to": "petersson_delta_value", "note": "a finite positive norm of Delta; cusp decay is not a degeneration"},
            {"type": "distinguishes", "to": "rs_explicit_formula_positive_lattice_form", "note": "a positive Rankin-Selberg lattice is not the Weil form"},
        ],
    ),
]


def sensitivity(label):
    return {
        "Theorem": 1.0,
        "Cited": 1.0,
        "Numerical": 1.0,
        "Restatement": 1.0,
        "Open": 1.0,
        "Heuristic": 0.7,
        "Analogy": 0.6,
        "Conjecture": 1.0,
    }[label]


def tractability(label):
    return {
        "Numerical": 0.7,
        "Theorem": 0.6,
        "Cited": 0.6,
        "Heuristic": 0.5,
        "Analogy": 0.4,
        "Restatement": 0.3,
        "Conjecture": 0.2,
        "Open": 0.2,
    }[label]


def evidence(label):
    return {
        "Theorem": 1.0,
        "Cited": 1.0,
        "Restatement": 1.0,
        "Numerical": 0.8,
        "Heuristic": 0.6,
        "Analogy": 0.5,
        "Open": 0.5,
        "Conjecture": 0.5,
    }[label]


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
    data = json.loads(ATLAS.read_text(encoding="utf-8"))
    concepts = data["concepts"]
    ids = {c["id"] for c in concepts}
    old_ids = list(ids)
    old_order = [c["id"] for c in sorted(concepts, key=lambda c: c["rank"])]
    old_priority = {c["id"]: c["priority"] for c in concepts}
    old_open = sum(json.dumps(c).count("Open ~1.8") for c in concepts)
    adding = [c for c in NEW if c["id"] not in ids]
    if len(adding) != len(NEW):
        raise SystemExit("some v1.20 ids already exist")
    missing_targets = sorted({r["to"] for spec in adding for r in spec["rels"] if r["to"] not in ids and r["to"] not in {s["id"] for s in adding}})
    if missing_targets:
        raise SystemExit("missing targets " + " ".join(missing_targets))

    extra = {
        "kahler_triple_polarization": (
            "v1.20. No compatible J on E0 is constructed. A translation-invariant Hilbert-transform J does not preserve compact support or E0. "
            "Open ~1.8 is unchanged. Rank 1 is unchanged. The Riemann Hypothesis is not proved."
        ),
        "two_walls_parabolic_routh": (
            "v1.20. This parabolic wall and the Routh wall stay distinct from each other, from the Beurling-pencil Hasse wall, and from the primary and secondary sheets of Sigma. "
            "The model null conic in the v1.20 polarity figure is a discriminant boundary of that model. It is not captioned as either of these walls."
        ),
        "conic_type_at_infinity": (
            "v1.20. This entry is the point-counting form, an ellipse because the form counts points, which is the Hasse bound for that form. "
            "It is not the null conic Q = 0 of the polarity model, and that model point at infinity is not a modular cusp."
        ),
        "petersson_delta_value": (
            "v1.20. This norm is finite and positive. Decay of the cusp integrand is the reason the integral converges. It is not a degeneration of the pairing, and it is not W."
        ),
        "no_ghost_missing_piece": (
            "v1.20. The window ledger, the bordered count, and the two failed representers do not construct H+. "
            "Open ~1.8 is unchanged. The Riemann Hypothesis is not proved."
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
        if "missing piece" in c["axes"]:
            raise SystemExit("new concept must not join the ten missing pieces")
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

    for c in concepts:
        if c["id"] in old_priority and c["priority"] != old_priority[c["id"]]:
            raise SystemExit("priority changed for " + c["id"])

    existing = [c for c in concepts if c["id"] in old_priority]
    existing.sort(key=lambda c: c["rank"])
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
    if order[0]["id"] != "kahler_triple_polarization":
        raise SystemExit("rank 1 moved: " + order[0]["id"])
    filtered = [c["id"] for c in order if c["id"] in old_priority]
    if filtered != old_order:
        raise SystemExit("relative order of existing concepts changed")
    new_open = sum(json.dumps(c).count("Open ~1.8") for c in order)
    if new_open < old_open:
        raise SystemExit("Open ~1.8 text was dropped")
    n_missing = sum(1 for c in order if "missing piece" in c["axes"])
    if n_missing != 10:
        raise SystemExit(f"missing-piece count {n_missing}")

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
    print("counts", data["counts"], "was", len(old_ids))
    print("rank1", order[0]["id"], order[0]["priority"])
    print("added", len(built), "relations now", data["counts"]["relations"])


if __name__ == "__main__":
    main()

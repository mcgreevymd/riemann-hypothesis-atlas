"""Build the proposed v1.21 concept/relation delta in the atlas.json concept schema and validate it against ref/atlas.json (v1.20).
Fields 'priority' and 'ranking' are copied from a named template concept of the same label/quadrant; 'rank' is left null for the repo build to assign
(v1.20 rule: existing priorities and relative order unchanged; new concepts follow the existing block of the same priority)."""
import json, os, collections
H = os.path.dirname(os.path.abspath(__file__))
ref = json.load(open(os.path.join(H, '..', 'ref', 'atlas.json')))
by = {c['id']: c for c in ref['concepts']}
TYPES = {r['type'] for c in ref['concepts'] for r in c['rels']}
A_SIGN, A_STRUCT, A_NUM, A_NOGO, A_OPEN, A_PHYS, A_POLE, A_MISS, A_GB, A_GS, A_PHASE, A_RESTATE = (
    'sign/positivity (Ax2)', 'structure/frame (Ax1)', 'numerics/certificate', 'no-go / refuted', 'open target', 'physics analogue',
    'reference/pole/cusp', 'missing piece', 'ghost-blind', 'ghost-sensitive', 'phase/unitarity (Ax3)', 'restatement ⇔ RH')
CERT = ('Computer-assisted: scalar data in mpmath interval arithmetic; finite matrices in IEEE-754 binary64 with dot-product error '
        'gamma_n = n u/(1 - n u), u = 2^-53, and explicit residual/orthogonality bounds. Not a formally verified proof.')
def C(id, name, label, tmpl, plain, core, formula, numbers, axes, uncertain, proved, tests, pitfalls, rels, aliases=()):
    return dict(id=id, name=name, aliases=list(aliases), plain=plain, label=label, core=core, formula=formula, numbers=numbers, axes=axes,
                uncertain=uncertain, proved=proved, tests=tests, pitfalls=pitfalls, lemmas=[],
                rels=[dict(type=t, to=to, note=n) for t, to, n in rels], priority=by[tmpl]['priority'], ranking=by[tmpl]['ranking'],
                rank=None, _template=tmpl)
N = []
N.append(C('signed_window_operator', 'Signed self-adjoint window operator K_A = L_A - M_A + P_A', 'Theorem', 'window_energy_ledger',
  'The window Weil form is the form of one closed, semibounded self-adjoint operator: a positive jump (Gamma plus primes) operator, minus a constant mass, plus a rank-two pole part. The Gamma part grows like log|t| in frequency. The operator exists; its sign on E0 is exactly what is missing.',
  'On L2(I_A), I_A = [-A/2, A/2], the form W = P + H_A - M_A||F||^2 is closed and bounded below on a log-Sobolev domain; the associated operator is K_A = L_A - M_A + P_A with L_A >= 0 the Gamma and prime jump operator and P_A of rank 2. The Gamma symbol is asymptotic to log|t|. The missing inequality is ||J_A F||^2 >= M_A ||F||^2 on E0 (J_A the square root of L_A) proved without zeros.',
  'K_A = L_A - M_A + P_A,  W(F) = <K_A F, F>', ['Gamma symbol ~ log|t| (operator2023).'], [A_STRUCT, A_SIGN, A_GB],
  'Positivity of K_A on E0 for any window beyond A = 1.1.', 'Closedness and semiboundedness from the positive jump form plus bounded perturbations (operator2023).',
  'Any proposed sign mechanism must reproduce the certified gaps on A <= 1.1.',
  ['Existence of a self-adjoint operator is not a sign statement.', 'Do not identify K_A with the cusp Laplacian: same 1/4, different operator.'],
  [('refines', 'window_energy_ledger', 'operator form of the ledger'), ('refines', 'weil_operator', 'window realization'), ('lives-in', 'bulk_form_B_off_E0', 'B is the L_A - M_A part')],
  ['K_A', 'window Weil operator']))
N.append(C('pole_cancelled_chebyshev_ledger', 'Pole-cancelled ledger with Chebyshev remainder', 'Theorem', 'window_energy_ledger',
  'Subtracting the pole against the main term of the prime sum rewrites W with a constant K5 = K0 + 4 and an integral against the Chebyshev remainder E = psi - x. The unconstrained residual mass changes sign between A = 1 and A = 2.',
  'W(F) = K5||F||^2 + J5(F) - 2 int x^{-1/2} <F, T_{log x}F> dE(x), E = psi_Cheb - x, K5(0) = K0 + 4. Unconstrained residual mass M~_A = M_A - 4e^{A/2}.',
  'W = K5||F||^2 + J5 - 2∫x^{-1/2}<F,T_{log x}F> dE(x)', ['M~_A: -0.2424 (A=1), 0.3515 (A=2), 0.4611 (A=3) [Numerical].'], [A_STRUCT, A_GS],
  'Sign control of the dE integral on E0.', 'Exact algebra; reproduced numerically (sos2010, realization2033).', 'Ghost n=2 deletion changes the dE term.',
  ['sos2010 "Lemma A" is a Ritz value, not a lower bound.'],
  [('refines', 'window_energy_ledger', 'pole/main-term cancellation'), ('related', 'pole_plane', 'pole absorbed into K5')]))
N.append(C('moment_parametrization_hardy_quarter', 'E0 = (d^2 - 1/4) H^2_0: moment constraints as a Hardy-1/4 operator', 'Theorem', 'bulk_form_B_off_E0',
  'Every window test with both moments zero is (d^2 - 1/4)G for a unique G supported in the window, and conversely. In the chart r = e^{-u} the operator is d_r(r^2 d_r); 1/4 is the Hardy constant and also the bottom of the continuous spectrum at the modular cusp.',
  'D = d^2 - 1/4 maps H^2_0(I_A) bijectively onto L2(I_A) ∩ ker C+ ∩ ker C-, C± = ∫F e^{±u/2}. Under r = e^{-u} with the unitary half-density, D becomes d_r(r^2 d_r). The radial cusp operator -y^2 d_y^2 is unitarily -d_t^2 + 1/4.',
  'E0 = D H^2_0,  D = d^2 - 1/4', [], [A_STRUCT, A_POLE, A_GB], 'Whether the shared 1/4 is more than coincidence of half-densities.',
  'Elementary ODE with compact support iff both moments vanish (parabola2019, poincare2024, modular2026).', '',
  ['Same constant 1/4 does not make the cusp Laplacian the W operator.'],
  [('refines', 'bulk_form_B_off_E0', 'explicit parametrization of E0'), ('related', 'hardy_constant_window_weil', 'Hardy 1/4 in the unitary chart'), ('analogue-of', 'one_cusp_three_readings', 'cusp continuous spectrum starts at 1/4')]))
N.append(C('mass_counterterm_character_class', 'M_A as a regularized prime sum fixed by the character class', 'Theorem', 'spring_energy_counterterm_split',
  'The mass M_A is twice the window prime sum minus its regularized value -zeta\'/zeta(1/2) = K0/2. The constant K0 has the closed form -(gamma + log 8 pi + pi/2) and is fixed by the adelic character class; there is no free renormalization parameter. The SL2(Z) cusp produces the sigma = 1 version of the constant instead.',
  'M_A = 2(S_A - S_reg), S_reg = -zeta\'/zeta(1/2) = K0/2; -K0 = gamma + log 8pi + pi/2; FP∫k = pi/2 + 2log2; in Connes semilocal trace degree form M_A is the total alpha-normalized mass. K0 - K0^(1) = -pi/2 - log 2.',
  'M_A = -K0 + 2Σ_{log n<A} Λ(n)/√n,  K0 = ψ(1/4) - log π = -5.372183', ['K0 = -5.3721834', 'K0 - K0^(1) = -2.2639', 'S_reg = -2.68609'], [A_POLE, A_STRUCT, A_GB],
  '', 'Closed forms checked to 30 digits (audit2060); Connes 1999 Thm VII.4 cited for the trace form.', '',
  ['The earlier "RG family" reading (free scheme parameter) is wrong.', 'Explicit-formula tables of M_A that use zeros are diagnostics only.'],
  [('refines', 'spring_energy_counterterm_split', 'closed form of the counterterm'), ('uses', 'connes_trace', 'degree form'), ('contrasts-with', 'tautology_boundary', 'zero-based tables are diagnostic only')]))
N.append(C('small_window_poincare_bound', 'No-prime windows: W >= 0.1965||F||^2 on E0 for A <= 1/10', 'Theorem', 'certified_windows',
  'For windows shorter than log 2 no prime enters, and a Poincare-type argument using both moment constraints proves a uniform positive lower bound for A <= 1/10.',
  'For A <= 1/10, W(F) >= c*||F||^2 on E0 with c* = log(5√2/π) - γ - 3/80 ≈ 0.19657 > 7/240. Elementary chain bounds without moments fail at A = 1 (3.7528 vs 6.3524 needed).',
  'c* = log(5√2/π) - γ - 3/80', ['c* ≈ 0.19657'], [A_SIGN, A_GB], '', 'Hand proof (poincare2024), constant rechecked in audit2060.', '', ['No prime is involved; this says nothing about arithmetic.'],
  [('refines', 'certified_windows', 'analytic smallest-window case'), ('tests', 'weil_positivity', 'window instance only')]))
N.append(C('prime_window_certificates', 'Certified E0 gaps through A = 1.1 (primes 2 and 3)', 'Theorem', 'certified_windows',
  'Three computer-assisted bounds: W >= 0.0045||F||^2 on E0 up to width 0.694 (interval arithmetic), W >= 0.004||F||^2 up to width 1 (prime 2), and W >= 0.0005||F||^2 up to width 1.1 (primes 2 and 3). Beyond 1.1 nothing is certified.',
  'A <= 347/500: constrained log-Jensen lemma, mpmath.iv. A <= 1: 815 cells, N=48, κ=2; finite eigenvalue > 0.0069963, h* > 2.2304, B* < 0.07587, Schur margin > 0.000314 ⇒ W >= ||F||^2/250. A <= 1.1: 1838 cells, N=192, κ=4; effective eigenvalue > 0.00066384, h* > 3.20786 ⇒ W >= 0.0005||F||^2. ' + CERT,
  'W ≥ c_A ||F||^2 on E0: c = 0.0045 (A≤0.694), 0.004 (A≤1), 0.0005 (A≤1.1)', ['Schur margins 0.000314 (A=1), effective eigen 0.00066384 (A=1.1)'], [A_NUM, A_SIGN, A_GS],
  'Extension past 1.1; formal verification of the floating-point layer.', CERT + ' Re-executed with single-thread BLAS; all assertions passed.', 'Same pipeline with n=2 deleted must fail (ghost control).',
  ['Not a formal proof.', 'Window positivity on A <= 1.1 is not RH and is not all-window positivity.', 'Failure of the interval bound at 0.695 is inconclusive, not a counterexample.'],
  [('refines', 'certified_windows', 'prime-carrying windows'), ('extends', 'small_window_poincare_bound', 'adds primes 2, 3'), ('tests', 'weil_positivity', 'window instances only')]))
N.append(C('e0_minima_grid_bias', 'E0 minima beyond A = 1.1 are numerical and grid-biased', 'Numerical', 'window_signature_numerical_witness',
  'Constrained minima of W/||F||^2 fall from about 0.012 at A = 1 to about 1.3e-5 for A between 2 and 3 on 2048-cell models; 128-cell models give about 2e-3, roughly 100 times larger. The gap and the discretization error are the same size.',
  'Ritz/finite-model minima on E0 (inertia2057): 0.8749 (0.5), 0.5455 (0.694), 0.011872 (1), 0.00093187 (1.1), 1.72e-5 (1.5), 1.278e-5 (2), 1.30e-5 (2.5), 1.2786e-5 (3).',
  '', ['2048 cells vs 128 cells differ ~100x beyond A ≈ 1.1'], [A_NUM, A_GS], 'Everything beyond 1.1.', 'Not certified.', '',
  ['Upper estimates only; do not draw as brackets.', 'A tiny positive minimum is not evidence of positivity at that scale.'],
  [('refines', 'window_signature_numerical_witness', 'E0-constrained minima'), ('contrasts-with', 'prime_window_certificates', 'uncertified region')]))
N.append(C('n2_deletion_ghost_control', 'Deleting n = 2 alone makes W negative on an explicit E0 test', 'Numerical', 'explicit_ghost_window',
  'On the test (d^2 - 1/4)(1-u^2)^4 at width 2, the true W/||F||^2 is +0.0023; deleting only the n = 2 term gives -0.639. Any positivity proof must see the actual prime coefficients.',
  'G = (1-u^2)^4 on [-1,1], F = DG, ||F||^2 = 40.77466; W = 0.0951580, W/N = 0.0023338; drop-2 W/N = -0.63923 (two routes: physical quadrature and Fourier side).',
  '', ['W/N = 0.0023338', 'drop-2 W/N = -0.63923'], [A_GS, A_NUM], '', 'Quadrature in two independent routes agree.', '',
  ['The deleted-coefficient form is not admissible Euler data; it is a sensitivity control, not a counterexample.'],
  [('instance', 'explicit_ghost_window', 'coefficient-deletion ghost'), ('constrains', 'weil_positivity', 'proof must be coefficient-sensitive')]))
N.append(C('one_negative_direction_certificate', 'Exactly one negative direction off E0 (certified at A = 1, 1.1)', 'Theorem', 'bordered_inertia_moment_criterion',
  'With Q = W - P on the full window, n-(Q|E0) = n-(Q) + n+(S) - 2 where S is the 2x2 moment Schur complement. At A = 1 and 1.1 the certificate shows Q has exactly one negative direction and the rest of its spectrum is at least 0.004 and 0.0005. The sign pattern of S follows from the constrained certificate, not independently.',
  'A=1: Q(const) ∈ [-1.95450, -1.95400], second spectral lower 0.004, Schur margin 0.000513. A=1.1: Q(const) ∈ [-2.1351, -2.1346], gap 0.0005, margin 0.000164. Finite minorant W_J alone has 2 negative directions. Scans to A=3: n-(Q)=1 in every finite model; squared overlap of the negative mode with span{e^{±u/2}} 0.969–0.999. ' + CERT,
  'n-(Q|E0) = n-(Q) + n+(S) - 2', ['gap ≥ 0.004 (A=1), ≥ 0.0005 (A=1.1)'], [A_NUM, A_SIGN, A_STRUCT],
  'Index count beyond 1.1.', CERT, 'A class map Φ must reproduce this count and gap.',
  ['One negative direction, not two.', 'Overlap 0.97–0.999 is closeness, not identity with the hyperbolic plane.', 'S signature is derived from, not independent of, the E0 certificate.'],
  [('instance', 'bordered_inertia_moment_criterion', 'certified case n-(Q)=1, S signature (1,1)'), ('refines', 'pole_block_hyperbolic_plane', 'negative mode near the pole plane'), ('refines', 'haynsworth_pole_plane_split_windows', 'certified inertia')]))
N.append(C('fe_fixed_boundary_class', 'Boundary plane (1,1) and the FE-fixed class e = h + v', 'Theorem', 'pole_block_hyperbolic_plane',
  'The two boundary classes h, v are isotropic with J(h,v) = 1, so they span a hyperbolic plane of signature (1,1). The functional equation swaps them; the fixed class e = h + v has J(e,e) = 2, normalized by the residues -1, +1 of the completed zeta at s = 0, 1. Its orthogonal complement contains the negative line h - v as well as the projected tests, so it is not E0.',
  'J(h,h)=J(v,v)=0, J(h,v)=1, B_U R = I, e^⊥ = R(h - v) ⊕ π(A), J(h-v,h-v) = -2.', 'J(e,e) = 2', [], [A_POLE, A_STRUCT, A_GB], '',
  'Exact (polarity2021); residues checked in audit2060.', '',
  ['Residues are those of the completed zeta Λ(s), not of ξ (ξ is entire).', 'e^⊥ ≠ E0.'],
  [('refines', 'pole_block_hyperbolic_plane', 'normalized boundary plane'), ('uses', 'functional_equation', 'FE swap h ↔ v')]))
N.append(C('formal_projection_restates_w', 'Formal boundary model: -J(πF, πG) = W is a restatement', 'Restatement', 'tautology_boundary',
  'Adding the two boundary classes and projecting, πF = F - C-(F)h - C+(F)v, gives -J(πF, πG) = W(F, G) on every window test. Because J on tests is defined from W, this reproduces the Hodge-index layout but proves nothing about the sign.',
  'With J defined on tests by J|tests = -W - (pole correction), the projection identity holds on all of D(I). A sign theorem needs J constructed independently, with W = -(intersection) on the primitive sector computed.',
  '-J(πF, πG) = W(F, G)', [], [A_RESTATE, A_STRUCT, A_MISS], '', 'Exact (matching1989).', '',
  ['Do not cite this identity as evidence for a Hodge index theorem.'],
  [('restates', 'weil_positivity', 'tautological on tests'), ('related', 'tautology_boundary', 'defined, not computed'), ('contrasts-with', 'hodge_index', 'layout without the theorem')]))
N.append(C('arithmetic_class_map_requirements', 'Requirements on the missing arithmetic class map Φ', 'Open', 'thermodynamic_J_direction',
  'A real Hodge-index route needs a map Φ from window tests to an intersection space built from geometry first, for example Φ(F) = ∫F(u)[Γ_u]du over graphs of the scaling action. The pairing must be computed: primes as fixed points with weight Λ(n)/√n, the Gamma term as an archimedean Green term, M_A as the diagonal self-intersection, and a Hodge-index theorem that applies. A fixed finite-rank lattice cannot work.',
  'Tests for any candidate: reproduce exactly one negative direction off E0 with gaps ≥ 0.004 (A=1) and ≥ 0.0005 (A=1.1); see the n=2 coefficient (ghost control). Ingredient status: ampleness holds on the positive-function cone; effectivity fails for the pointwise cone; a relative (GRR-type) lemma gives (A)+(R) ⇒ n+(J)=1; quadratic Riemann–Roch missing.',
  'Φ(F) = ∫ F(u) [Γ_u] du,  W = -⟨ΦF, ΦF⟩ on the primitive sector', [], [A_OPEN, A_MISS, A_SIGN], 'All of it.', '', 'Finite certificates (A ≤ 1.1) and the n=2 ghost.',
  ['A pairing defined from W is circular.', 'Finite-rank NS obstruction (bulk_form_B_off_E0).'],
  [('refines', 'no_ghost_missing_piece', 'concrete shape of the missing object'), ('uses', 'hodge_index', 'needed theorem'), ('related', 'mp_quadratic_rr', 'missing quadratic RR'), ('related', 'mp_castelnuovo', 'function-field model'), ('tested_by', 'one_negative_direction_certificate', 'index and gap')]))
N.append(C('pencil_discriminant_window_conic', 'W = half the minimal pencil discriminant through e', 'Theorem', 'pole_block_hyperbolic_plane',
  'Every window test spans with the boundary classes a pencil of conics; W(F) is half the minimum of its discriminant through e. Window lines become nearly parabolic as A grows, and a four-dimensional example shows the conic picture alone does not force positivity.',
  'W(F) = ½ min Δ_e; disc(Q|ℓ) = -4 det M · Q(pole ℓ); one conic in a moving chart, det = -1/4. Separation 0.128, 1.46e-3, 1.6e-7 [Numerical].',
  'W(F) = ½ min Δ_e', ['separation 0.128 → 1.6e-7'], [A_STRUCT, A_NOGO], '', 'sympy (parabolic1998, audit2060).', '', ['Geometry of the pencil does not supply a sign.'],
  [('refines', 'pole_block_hyperbolic_plane', 'pencil form'), ('related', 'kahler_triple_polarization', 'conic polarity model')]))
N.append(C('k0_not_arakelov_degree', 'K0 is a Mellin derivative, not an Arakelov degree on P^1_Z', 'Theorem', 'arakelov',
  'The arithmetic self-intersection of the diagonal on P^1 over Z is 2 - 4a for the canonical metric family, never -K0. K0 is the derivative 2(log Γ_R)\'(1/2) (= 2E[log|x|] under the Tate weight). The Tate dimension-one diagonal has degree 0. Hecke ratios at weight 12 are 2cos(mθ_p), which do not collapse to Λ(n)/√n.',
  'ω̂^2(P^1_Z) = 2 - 4a; -K0 - (2-4a) = 3.3722, 5.3722, 1.0827, -0.3036 for the canonical choices tested. Derived Δ^2 = 2 - 2g.',
  'K0 = 2(log Γ_R)\'(1/2)', ['gaps 3.3722, 5.3722, 1.0827, -0.3036'], [A_NOGO, A_POLE], 'Other arithmetic surfaces.', 'diagonal2003, intersection2002; rechecked in audit2060.', '',
  ['Scope: P^1_Z and the metrics tested.', 'Spin/Wu/Rokhlin structures give parity only.'],
  [('fails-for', 'arakelov', 'P^1_Z diagonal does not produce K0'), ('contrasts-with', 'mass_counterterm_character_class', 'Mellin derivative vs degree')]))
N.append(C('probe_response_identity', 'B_W(F_z, F_w) = K_q(z, w): W on exponential probes is the ξ response kernel', 'Theorem', 'passive_network_positive_real',
  'On truncated exponentials F_z = e^{-zu}1_{u≥0}, the complete Weil form, including pole, Gamma, K0 and every prime, equals the kernel (q(z) + conj q(w))/(z + conj w) with q = ξ\'/ξ(1/2 + z). RH is equivalent to q being positive-real (Lagarias, Hinkkanen); the passage from probes back to compact tests is only sketched.',
  'For Re z, Re w > 1/2: B_W(F_z, F_w) = K_q(z, w). Inverse superposition to compact tests: sketched.', 'K_q(z,w) = (q(z) + \\bar q(w))/(z + \\bar w)',
  ['K_q(1,2) = 0.045990', "q'(0) = 0.0462099862"], [A_PHASE, A_RESTATE, A_GB], 'Full proof of "PSD on one vertical line ⇒ W ≥ 0 on compact tests".',
  'Exact algebra (dispersion2030); three probe pairs rechecked by independent quadrature in audit2060.', '',
  ["q'(0) > 0 is not passivity (z + z^3 is a falsifier)."],
  [('refines', 'passive_network_positive_real', 'window form = response kernel'), ('uses', 'lagarias', 'positive-real ⇔ RH'), ('related', 'passivity', 'storage reading')]))
N.append(C('dispersion_not_passivity', 'Causal and dispersive is not passive', 'Theorem', 'anomalous_dispersion',
  'Explicit causal, stable transfer functions such as -1/(z+1), the ghost transfer, and z + z^3 fail positive-realness. Anomalous dispersion is not loss, and Heaviside\'s distortionless line is still lossy. The needed property is Herglotz positivity, not causality.',
  'Falsifiers: q = -1/(z+1); q_a (ghost); z + z^3.', '', [], [A_PHYS, A_NOGO], '', 'Elementary (dispersion2030).', '',
  ['Distortionless ≠ lossless.'],
  [('refines', 'anomalous_dispersion', 'explicit falsifiers'), ('analogy', 'telegrapher_distortionless', 'distortionless but lossy'), ('fails-for', 'passivity', 'causality alone')]))
N.append(C('signed_kyp_delay_line', 'Delay-line realization with signed KYP storage', 'Theorem', 'passivity',
  'The ξ response has a delay-line state realization whose storage identity is exact but signed: the boundary storage 2Re(x+ conj x-) is indefinite. A finite prime cutoff leaves a pole at z = 1/2, and independent per-prime storage diverges.',
  '2Re(ū y_B) = d/dt(S_∂ + S_jump) + D_jump - M_B|u|^2; pole-cancelled transfer q = g5 - ∫x^{-z-1/2} dE.', '', [], [A_PHASE, A_NOGO, A_STRUCT], 'A positive coupled storage.', 'realization2033.', '',
  ['A signed storage identity is not a passivity proof.'],
  [('refines', 'passivity', 'explicit realization'), ('uses', 'pole_cancelled_chebyshev_ledger', 'pole-cancelled transfer')]))
N.append(C('prime_gap_block_obstruction', 'Prime-gap 2x2 storage blocks fail', 'Theorem', 'passivity',
  'Coupling the storage blocks with a fixed PSD diagonal diverges, and the exact-match block is not PSD inside prime gaps: at cutoff B = 2 the weight w_B is negative just after log 2, 3, 5 and 7, proved at s = 49/25.',
  'B=2, s0=49/25: g=0.003012, d=0.107651, w=-0.104639, det=-0.0112645, ρ_req=5.978. Fixed-diagonal coupling needs ≥ (√P_B - √G)^2.',
  '', ['det = -0.0112645 at s0 = 1.96', 'w_B<0 on (0.693,0.766), (1.099,1.183), (1.609,1.707), (1.946,2) [Numerical]'], [A_NOGO, A_SIGN, A_GS], '', 'blocks2038; rechecked in audit2060.', '',
  ['Scope: these block shapes only.'],
  [('fails-for', 'passivity', 'blockwise PSD storage'), ('refines', 'signed_kyp_delay_line', 'blockwise attempt')]))
N.append(C('kms_half_kernel_not_response', 'Bost–Connes KMS at β = 1/2 gives the prime weights but not K_q', 'Theorem', 'kms_bost_connes',
  'At β = 1/2 the Bost–Connes KMS state produces vectors with squared norm Λ(n)/√n exactly, but their Gram kernel is -ζ\'/ζ(1/2 + z + conj w), which lacks the Gamma, pole and mass terms of K_q; the all-prime vector has infinite norm. The fermion primon gas has the wrong sign at n = 4 and 9.',
  '||v_n||^2 = Λ(n)/√n; kernel -ζ\'/ζ(1/2 + z + w̄) ≠ K_q; boson Z = ζ(β), fermion Z = ζ(β)/ζ(2β).', '', ['C_2 = 0.63038', 'J = 0.100396'], [A_PHYS, A_NOGO], '', 'kms2040; KMS theory cited.', '',
  ['Positive weights are not positive W.'],
  [('refines', 'kms_bost_connes', 'β = 1/2 vectors'), ('contrasts-with', 'probe_response_identity', 'missing Gamma, pole, mass'), ('related', 'graded_primon_gas', 'boson/fermion signs')]))
N.append(C('gamma_kernel_planck_ladder', 'Gamma jump kernel as a Planck/OU ladder', 'Analogy', 'planck_ott_landsberg_reading',
  'The archimedean jump kernel e^{-a/2}/(1 - e^{-2a}) is the sum of exponentials with rates 2m + 1/2, a Planck-type ladder. Reading Gamma as radiation and primes as a primon gas is suggestive; they are not one Hamiltonian, and kinetic (H_A) versus potential (M_A) is bookkeeping, not a sign mechanism.',
  'k∞(a) = Σ_m e^{-(2m+1/2)a} (exact).', 'k∞(a) = e^{-a/2}/(1-e^{-2a})', [], [A_PHYS, A_GB], '', 'Geometric series (exact).', '', ['Not a thermodynamic proof of positivity.'],
  [('refines', 'local_product_state_covariance', 'OU rates 2m+1/2'), ('analogue-of', 'planck_ott_landsberg_reading', 'ladder reading')]))
N.append(C('serre_derivative_cusp_correction', 'Serre derivative of E_k closes only at k = 4, 6, 8, 12', 'Theorem', 'e2_anomaly',
  'Differentiating E_k and restoring covariance with E_2 leaves a cusp correction f_k in S_{k+2}; it vanishes exactly when S_{k+2} = 0. For E_10 the correction carries 38016/691. This is a calibration of the derivative anomaly, not a W mechanism.',
  'D E_k = (k/12)(E_2 E_k - E_{k+2}) + f_k, f_k = 0 ⇔ k ∈ {4,6,8,12}; a_1(f_10) = 38016/691; D_4E_4 = -E_6/3, D_6E_6 = -E_4^2/2.', '', ['38016/691'], [A_POLE, A_STRUCT], '',
  'Bernoulli bound plus exact check 14 ≤ k ≤ 398 (eisenstein1990); 38016/691 rechecked in audit2060.', '', ['E_2 = θ log Δ vs K0 = 2(log Γ_R)\'(1/2) is a parallel, not an identification.'],
  [('refines', 'e2_anomaly', 'general weight'), ('analogue-of', 'serre_derivative_analogy', 'made exact')]))
N.append(C('boundary_class_691', 'X^10 - 1 is the boundary class δ(1) in H^1_c; Eisenstein denominator 691', 'Theorem', 'index_691_weight12',
  'In weight 12 the period polynomial X^10 - 1 is the boundary class δ(1) in compactly supported cohomology, not the Eisenstein class. The Eisenstein lift has denominator 691 (3617 at weight 16), and mod 691 the Hecke operator T2 + 24 is nilpotent on the Δ line. One cusp supplies only one moment; two moments need Γ0(N).',
  'T2 = [[2049,0],[-1296000,-24]], 2049 ≡ -24 mod 691; D(δ1, ψ) = 6 res ψ; Sym^2 signature (1,2); <Δ,Δ> = 1.0353620568e-6.', '', ['<Δ,Δ> = 1.0353620568e-6'], [A_POLE, A_STRUCT], 'Modular origin of M_A.', 'boundary1994, hodge1991.', '',
  ['hodge1991 called X^10 - 1 "the Eisenstein class": corrected.'],
  [('refines', 'index_691_weight12', 'boundary reading'), ('related', 'one_cusp_three_readings', 'one cusp, one moment'), ('related', 'adjoint_691_eisenstein_not_cuspidal', '691 denominator')]))
# validation
ids = [c['id'] for c in N]
assert len(ids) == len(set(ids)), 'dup'
coll = [i for i in ids if i in by]; assert not coll, coll
allid = set(by) | set(ids)
bad = [(c['id'], r['to']) for c in N for r in c['rels'] if r['to'] not in allid]; assert not bad, bad
badt = [(c['id'], r['type']) for c in N for r in c['rels'] if r['type'] not in TYPES]; assert not badt, badt
LAB = {c['label'] for c in ref['concepts']}; assert all(c['label'] in LAB for c in N)
AX = {a for c in ref['concepts'] for a in c['axes']}; assert all(a in AX for c in N for a in c['axes'])
nrel = sum(len(c['rels']) for c in N)
out = dict(base=dict(version='v1.20', concepts=len(by), relations=ref['counts']['relations']), proposed=dict(version='v1.21', concepts=len(by) + len(N), relations=ref['counts']['relations'] + nrel),
           added_concepts=len(N), added_relations=nrel, concepts=N)
json.dump(out, open(os.path.join(H, 'atlas_delta_v121.json'), 'w'), indent=1, ensure_ascii=False)
with open(os.path.join(H, 'DELTA_v121.md'), 'w') as f:
    f.write(f'# Proposed v1.21 concept/relation delta\n\nBase v1.20: {len(by)} concepts / {ref["counts"]["relations"]} relations. Added: **{len(N)} concepts, {nrel} relations** → {len(by)+len(N)} / {ref["counts"]["relations"]+nrel}.\n')
    f.write('No collisions with existing ids; every relation target exists; types, labels and axes are from the v1.20 vocabulary. `rank` is null: the build assigns it (existing order unchanged; new concepts follow their priority block). `_template` names the concept whose priority/ranking were copied; drop it on merge.\n\n')
    f.write('| id | label | template (priority) | relations |\n|---|---|---|---|\n')
    for c in N: f.write(f"| `{c['id']}` | {c['label']} | `{c['_template']}` ({c['priority']}) | " + '; '.join(f"{r['type']} → `{r['to']}`" for r in c['rels']) + ' |\n')
print(len(N), nrel, collections.Counter(c['label'] for c in N))

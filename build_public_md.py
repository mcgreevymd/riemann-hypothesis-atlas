#!/usr/bin/env python3
"""Generate ATLAS.md (the human-readable public atlas) from atlas.json.

Usage:  python3 build_public_md.py      (reads ./atlas.json, writes ./ATLAS.md)
Every section lists entries in descending priority (rank 1 = highest).
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'atlas.json'), encoding='utf-8'))
C = sorted(D['concepts'], key=lambda c: c['rank'])
BY = {c['id']: c for c in C}
VERSION, VDATE = '1.10', '31 Oct 2026'

REL = {'same-mechanism-as': 'same mechanism as', 'special-case-of': 'special case of',
       'analogue-of': 'analogue of', 'implies': 'implies', 'equivalent-to-RH': 'equivalent to RH',
       'corrects': 'corrects', 'lives-in': 'lives in', 'fails-for': 'fails for',
       'refines': 'refines', 'restates': 'restates', 'feeds': 'feeds', 'illustrates': 'illustrates',
       'mirror-of': 'mirror of', 'extends': 'extends', 'obstructs': 'obstructs',
       'contrasts-with': 'contrasts with', 'tested_by': 'tested by', 'constrains': 'constrains',
       'explains': 'explains', 'candidate_setting': 'candidate setting for',
       'analogous_to': 'analogous to', 'heuristically_points_to': 'heuristically points to',
       'localises': 'localises', 'analogy': 'analogy of', 'tests': 'tests',
       'related': 'related to', 'compared_with': 'compared with', 'quantifies': 'quantifies',
       'density_form_of': 'density form of', 'supplies_sign_for': 'supplies the sign for',
       'sharpens': 'sharpens', 'uses': 'uses', 'strengthens': 'strengthens',
       'worked_example_E2star': 'worked example of',
       'instance': 'instance of', 'counterexample_to_sufficiency': 'counterexample to sufficiency of'}
QUAD = [('RH-sharp', 'RH-sharp: true for ζ and fails for the fakes'),
        ('true but ghost-blind/untested', 'True for ζ but ghost-blind or untested against the fakes'),
        ('sharp but interpretive', 'Separates ζ from the fakes, but the claim itself is interpretive (Analogy/Heuristic)'),
        ('background', 'Background: interpretive and not separating')]

def lem(x):
    """'L147' -> 'TAA Lemma 147'; also inside free text '(L78)'."""
    return re.sub(r'\bL(\d{1,3})\b', r'TAA Lemma \1', x)

def short_mp(i):
    n = BY[i]['name'] if i in BY else i
    return n[len('Missing: '):] if n.startswith('Missing: ') else n

def anchor(c):
    return c['id'].lower().replace('_', '-')

def link(i):
    return f"[{BY[i]['name']}](#{anchor(BY[i])})" if i in BY else i

def header(c, level='###'):
    return f"{level} #{c['rank']} · {c['priority']:.3f} · {c['name']} <a id=\"{anchor(c)}\"></a>"

def entry(c, full=True):
    r = c['ranking']
    out = [header(c), '',
           f"**Label:** {c['label']} · **id:** `{c['id']}` · **quadrant:** {r['quadrant']}", '',
           f"*In plain words:* {lem(c['plain'])}", '']
    if c['core']: out += [f"**Core.** {lem(c['core'])}", '']
    if c['formula']: out += [f"**Formula.** {c['formula']}", '']
    if c['numbers']: out += ['**Numbers.** ' + ' · '.join(lem(n) for n in c['numbers']), '']
    if c.get('proved'): out += [f"**What is proved around it.** {lem(c['proved'])}", '']
    if c.get('tests'): out += [f"**Tests it must pass.** {lem(c['tests'])}", '']
    if c['aliases']: out += ['**Also known as:** ' + '; '.join(c['aliases']), '']
    out += ['**Axes:** ' + ', '.join(c['axes']), '']
    if c['lemmas']: out += ['**TAA lemmas:** ' + ', '.join(l[1:] if l.startswith('L') else l for l in c['lemmas']), '']
    g = f"nearest gap: {short_mp(r['gap'])}" if r.get('gap') else 'no gap within distance 2'
    out += [f"**Scores (Heuristic):** gap significance {r['gap_significance']} ({g}) · sensitivity {r['sensitivity']} · "
            f"specificity {r['specificity']} · tractability {r['tractability']} · evidence {r['evidence']} → priority {c['priority']:.3f}", '']
    for p in c['pitfalls']: out += [f"> ⚠ **Correction / caution.** {lem(p)}", '']
    if c['uncertain']: out += [f"> ❓ **Not verified / open.** {lem(c['uncertain'])}", '']
    if c['rels']:
        out += ['**Relations (outgoing):**', '']
        for x in c['rels']:
            note = f" — {lem(x['note'])}" if x.get('note') else ''
            out.append(f"- {REL.get(x['type'], x['type'])} → {link(x['to'])}{note}")
        out.append('')
    inn = [(d, x) for d in C for x in d['rels'] if x['to'] == c['id']]
    if inn:
        out += ['**Relations (incoming):** ' + '; '.join(f"{link(d['id'])} ({REL.get(x['type'], x['type'])})" for d, x in inn), '']
    return out

L = ['# The RH Atlas — full public edition', '',
     f"Version {VERSION} · {VDATE} · J. W. McGreevy; formalization by Grok Bot", '',
     '> **The Riemann Hypothesis is NOT proved here.** This atlas is a classification of known structures, criteria and open problems, not a proof.', '',
     '## The missing piece (refined in v1.10)',
     '',
     '> **The Riemann Hypothesis is not proved.** This section states what is missing as precisely as the current evidence allows. Labels in brackets.',
     '',
     '**Statement [Open].** What is missing over ℤ is an *a-priori Krein grading* Γ for ζ: a Rosati-type involution that acts as time reversal for the scaling flow and turns the Weil energy form Z into a positive invariant metric P = ZΓ for every support length L at once, defined before the zeros and built from the primes and the archimedean place together. Such a Γ would write the Weil form as a sum of squares at every L (item 8); in finite dimension a grading of this kind exists exactly while the flow is elliptic, and ceases to exist at the walls of item 10 [Theorem]. Over 𝔽_q the grading is supplied by the polarization: the Rosati involution on H¹ (Castelnuovo–Severi, the Hodge index theorem, Hodge–Riemann on C × C), which comes from geometry, and its existence is the same statement as Hasse, |α| = √q: the Frobenius pair never reaches the parabolic wall a² = 4q [Theorem]. Over ℤ it would presumably live on Deninger’s conjectured cohomology, with the sign supplied by an arithmetic Hodge–Riemann theorem on Spec ℤ × Spec ℤ assembled as in Faltings–Hriljac (local sign-definite pieces plus a global height) [Conjecture]. It has to act on the prime side: the archimedean (kinetic) cushion already carries ζ’s positivity on every plane tested, while Davenport–Heilbronn’s ghosts come from its prime terms (items 4–5) [Numerical], so the grading must come from the global prime sum and not from any single local factor. Any exact version is equivalent to RH, and none of the analogies below constructs it.',
     '',
     '**What is now settled about it.**',
     '',
     '1. **Frame, not definiteness [Theorem].** The product formula (the pole plane) gives the Weil form Z = Pole + W_∞ − Σ_p W_p its Lorentzian (1,1) frame. On span{pole, g} positivity is the reverse Cauchy–Schwarz inequality of timelike vectors, the inequality behind the twin paradox. The frame does not make the form definite.',
     '2. **Trichotomy and Weil radius [Restatement].** Along the support filtration each Levinson/Schur step has discriminant 1 − k²; over 𝔽_q exactly 1 − k₁² = (4q − a²)/4q, so elliptic / parabolic / hyperbolic ⇔ a² <, =, > 4q. The Weil radius L* is the first support length at which a direction turns negative, and **RH ⇔ L* = ∞ for ζ**. Under RH ζ is strictly elliptic at every finite L and meets the parabolic wall only as L → ∞; Davenport–Heilbronn crosses at L* ≈ 3.82 [Numerical].',
     '3. **Special-relativity dictionary [Theorem; circular as a criterion].** Each step is an SU(1,1) boost with velocity k: 1 − k² = 1/γ², the Lorentz factors multiply and the rapidities add. Positivity ⇔ every step is subluminal (Schur). ζ’s largest step up to L = 8 is |k| = 0.384; Davenport–Heilbronn reaches |k| ≥ 1 at L = 3.85, exactly at its wall [Numerical].',
     '4. **No local positivity [Numerical].** Every local term W_∞, W_p is indefinite, and partial products over places stay negative until every prime power ≤ e^L is present. The repair is collective: the earlier “edge primes do it” reading was an ordering effect and is refuted.',
     '5. **Where the ghost lives [Numerical].** On Davenport–Heilbronn’s ghost 2-plane span{g, Dg} (taken at its wall) the archimedean (“kinetic”, mass) part is positive definite. ζ’s prime terms keep that 2×2 positive at every partial sum, in either order and at both resolutions; Davenport–Heilbronn’s own terms break it only late, first after 73–100% of the terms (79% / 95% at h = 0.025 and 73% / 100% at h = 0.0125, adding terms in increasing / decreasing n), and the 2×2 is positive semidefinite at 77–97% of the partial sums. The ghost comes from the prime (“spring”) side. This is the first separation of ζ from Davenport–Heilbronn on a fixed low-dimensional plane.',
     '6. **One global polarization [Numerical; equivalent to n₋ = 0].** In the gyroscopic Weil pencil every ζ mode is imaginary with Krein sign +, and one fixed positive-frequency (Hardy) polarization, a Dirac sea, fills for ζ at every L ≤ 8; Davenport–Heilbronn leaves n₋/2 unfillable holes. The missing object reads as one polarization valid for every prime at once.',
     '7. **Shear, not curvature [Theorem + Numerical; equivalent to Laguerre].** The curvature of log|Ξ| is the Riesz measure 2πΣδ_ρ ≥ 0, the same for every function; the separating part is the trace-free shear (ζ keeps u_tt < 0 on the line at 3900/3900 samples with t ≤ 200, Davenport–Heilbronn flips at its ghost heights). A pointwise Witten-type curvature condition fails, so positivity must be an operator inequality.',
     '8. **The sum of squares, explicitly, and where it breaks [Theorem + Numerical; circular as a criterion].** Toeplitz Cholesky is the Levinson recursion: Z(g) = Σ_k E_k |⟨a_k, g⟩|² with the Szegő predictor polynomials a_k. Positivity ⇔ every pivot E_k > 0 ⇔ (Schur–Cohn) no predictor root inside the unit disk; the number of inside roots equals n₋ at every L tested. For ζ the roots lie on the circle at the zeta zeros (29/29 below 100 to 0.002). For Davenport–Heilbronn the root that enters the disk at the wall converges to the off-line zero itself, (γ, δ) = (85.700, 0.3085) against 0.80852 + 85.69935i, then 114.16, 176.7, 240.4. The best Witten-type constant in −R ≤ c·T is 1 − O(10⁻¹⁰) for ζ and > 1 for Davenport–Heilbronn past its wall.',
     '9. **Count versus stability [Theorem].** Morse counts are topologically forced: the co-rotating potential has 2 − 3 = −1 = χ critical points for every mass ratio, with or without the gyroscopic term, while stability (Krein signs at L4) needs that term and fails past Routh. On the arithmetic side the signed counts are equal for ζ and Davenport–Heilbronn; only the positivity data separate them (extra on-line saddles of log|Ξ|: ζ 0, Davenport–Heilbronn 2 per off-line pair).',
     '10. **Two walls [Theorem + Numerical; the converse is open].** Positivity can fail at two kinds of wall. The *parabolic (signature) wall* is a one-mode collision of a conjugate pair on the real axis: a² = 4q over 𝔽_q, Kepler’s E = 0, a Levinson step with |k| = 1, a Hodge–Riemann signature flip; along the support filtration it is the Weil radius, and RH ⇔ ζ never reaches it [Restatement]. The *Routh (Krein-collision) wall* is a collision of two modes of opposite Krein sign off the real axis (Hamiltonian–Hopf; at L4, μ_R = 0.0385209). It needs a Krein-negative mode first, so it lies downstream: RH ⇒ ζ never reaches any Routh wall [Theorem]. The converse fails at finite L: Davenport–Heilbronn crosses the parabolic wall at L* ≈ 3.6–3.9 (depending on the resolution), then sits in an L4-like window (energy indefinite, every pencil mode still elliptic, one Krein-negative pair), and from L_H ≈ 4.3–4.8 shows Hamiltonian–Hopf quartets again and again; ζ shows none of this for L ≤ 8 [Numerical]. Whether every Krein-negative mode must reach a Routh wall as L → ∞ is open [Conjecture]. In the de Bruijn–Newman (ferromagnetic Φ) direction, by contrast, ζ sits exactly on its wall: Λ ≥ 0 (Rodgers–Tao) and RH ⇔ Λ ≤ 0, so RH ⇔ Λ = 0 [Theorem, cited]; forward heat flow plays the role of the Coriolis stiffness that holds L4 below μ_R [Analogy].',
     '',
     '**Closest literal version, and the gap.** Over 𝔽_q every item above is literal: Rosati positivity = Hasse = a positive 2×2 coherency matrix = a subluminal first step = an elliptic Kepler orbit. Over ℤ each item is either a restatement of RH or a finite-cutoff observation. In its most localized form the gap is a reason why the Levinson/Szegő factor of the ζ Weil form never acquires a root inside the unit disk, an input that Davenport–Heilbronn lacks (the Euler product is the only candidate in sight). The gap is exactly the a-priori Krein grading (the polarization): a non-circular construction, from the primes and ∞, of the positive structure whose presence the numerics show for ζ and whose absence they show for Davenport–Heilbronn. Rank 1 in the ranking below remains the author’s pinned statement of this gap.',
     '',
     '## Latest results (v1.10)', '', 'Figures from the research notes folded into v1.10 (see README.md for the gallery and CHANGELOG.md for details). The Riemann Hypothesis is not proved.', '',
     '![Two walls, not one](figures/two_walls/two_walls_dictionary.png)', '', '*Two walls, not one: the parabolic (signature) wall, where a conjugate pair collides on the real axis (Hasse a² = 4q, Kepler E = 0, Levinson |k| = 1, Hodge index change; RH ⇔ ζ never reaches it), and the downstream Routh (Krein-collision) wall at μ_R = 0.0385209; Davenport–Heilbronn passes the first at L*, sits in an indefinite-but-elliptic window, then shows Hamiltonian–Hopf quartets; in the de Bruijn–Newman direction ζ sits exactly on its wall.* [Theorem + Numerical · 3.52 (0.6·sig + 0.4·prob, 0–4)]', '',
     '![Positivity concepts (Weil, Rosati, Laguerre–Pólya, Hodge–Riemann, product formula, ferromagnetic Φ, Routh wall) against the mechanics pictures (Kepler/KS, shear/Raychaudhuri, Lagrange/Krein, special relativity, Routh wall)](figures/two_walls/positivity_crosstable.png)', '', '*Positivity concepts (Weil, Rosati, Laguerre–Pólya, Hodge–Riemann, product formula, ferromagnetic Φ, Routh wall) against the mechanics pictures (Kepler/KS, shear/Raychaudhuri, Lagrange/Krein, special relativity, Routh wall): the most exact correspondence in each cell, with its label and score; every cell at 3.4 or above is a finite-dimensional theorem or an RH-equivalent restatement.* [Theorem / Restatement / Analogy · cells 2.0–3.6 (0.6·sig + 0.4·prob, 0–4)]', '',
     '![Davenport–Heilbronn’s ghost 2-plane](figures/relativity_shear/dh_ghost_plane_2x2.png)', '', '*Davenport–Heilbronn’s ghost 2-plane: the archimedean part is positive there; ζ’s prime terms never break the 2×2 (100% of partial sums, in either order), while Davenport–Heilbronn’s own terms break it late. The ghost comes from the prime side.* [Numerical · 3.2 (scores 0–4)]', '',
     '![Levinson/Schur steps are SU(1,1) boosts](figures/relativity_shear/levinson_boosts_rapidity.png)', '', '*Levinson/Schur steps are SU(1,1) boosts: ζ stays subluminal (max |k| = 0.384 up to L = 8), Davenport–Heilbronn’s first |k| ≥ 1 is its light-cone crossing at L = 3.85, Lorentz factors multiply, and over 𝔽_q k₁ = −a/(2√q).* [Theorem + Numerical · 3.5, circular as a criterion (scores 0–4)]', '',
     '![The positivity cup at E = 0](figures/positivity_cup/positivity_bowl_flat_peak.png)', '', '*The positivity cup at E = 0: bowl, flat and peak are definite, semidefinite and indefinite (null set a point, a line, an X); ζ’s smallest Weil eigenvalue flattens but stays positive, while Davenport–Heilbronn flips to a peak at L* ≈ 3.82.* [Theorem + Numerical · 3.0 (scores 0–4)]', '',
     '![KS trichotomy](figures/positivity_cup/ks_trichotomy_sundman.png)', '', '*KS trichotomy: oscillator (E < 0), free particle (E = 0, the null line is the wall) and inverted oscillator = xp (E > 0, the null X); Sundman time makes Kepler’s radial motion linear; the e^{t/2} normalization turns the decaying Mellin spiral into the unit circle.* [Theorem · 3.4; normalization panel 2.8 (scores 0–4)]', '',
     '![Shear, not curvature](figures/relativity_shear/raychaudhuri_shear.png)', '', '*Shear, not curvature: σ² − ω² = E/2 for the KS oscillator; Routh stability at L4 in tidal and rotation variables; the trace-free Hessian of log|Ξ| keeps its sign on the line for ζ and flips at Davenport–Heilbronn’s ghost heights, while the curvature is blind off the zeros.* [Theorem + Numerical · 3.5, equivalent to Laguerre (scores 0–4)]', '',
     '![Dirac sea and curvature density](figures/relativity_shear/dirac_sea_curvature_density.png)', '', '*Dirac sea and curvature density: one global positive-frequency sea fills for ζ, Davenport–Heilbronn leaves n₋/2 holes; curvature per unit kinetic energy sits on the edge −1 for ζ and below it for Davenport–Heilbronn; the Riesz curvature density is ≥ 0 for both.* [Numerical + Theorem · 3.3 / 3.4, circular as a criterion (scores 0–4)]', '',
     '![Twin paradox at the Lagrange points](figures/relativity_shear/lagrange_point_clocks.png)', '', '*Twin paradox at the Lagrange points: the co-rotating clock rate is the Jacobi constant, so the Lagrange points are its critical points and L4/L5 clocks run fastest; L4 and L5 split only when time reversal is broken.* [Theorem + Numerical · 3.6 / 3.2 (scores 0–4)]', '',
     '![Single orbit vs ensemble](figures/positivity_cup/single_orbit_vs_ensemble.png)', '', '*Single orbit vs ensemble: over 𝔽_q the ensemble inertia is the per-pair Hasse data aggregated (122/122); in the restricted three-body problem a planet clears a chaotic band but the co-orbital Trojan and horseshoe ring survives completely.* [Theorem + Numerical · 3.4 / 3.2 (scores 0–4)]', '',
     '![Frame dependence](figures/positivity_cup/frame_dependence_krein.png)', '', '*Frame dependence: rotating and inertial frames give the same Floquet multipliers and Krein signs (to 5e−12); only the picture changes. For ζ the Weil pencil is Hamiltonian only in the e^{t/2}-normalized frame (100% against 6.7% imaginary).* [Theorem + Numerical · 3.4 / 3.0 (scores 0–4)]', '',
     '![Librations and polarization](figures/librations_krein/polarization_coherency_local_global.png)', '', '*Librations and polarization: the genus-1 Hasse bound is a positive coherency (Stokes) matrix (1800/1800 curves); Levinson steps as 2×2 coherencies; L4 modes as polarization ellipses whose Krein collision is a polarization collision; place-by-place and pole-plane filtrations (the edge-prime reading is refuted in v1.10).* [Theorem + Numerical · 3.4 / 3.3; pole plane 1.6 (scores 0–4)]', '',
     '![L4/L5 and the Weil form](figures/librations_krein/l4_routh_krein_rosati_ks.png)', '', '*L4/L5 and the Weil form: Krein signs and the Routh wall at μ_R = 0.0385; a Rosati-like involution is a Krein-signed complex structure; the gyroscopic Weil pencil is all-imaginary with Krein + for ζ and L4-like for Davenport–Heilbronn; the KS lift reads the Kepler trichotomy as the sign of b² − ac, with xp on the hyperbolic side.* [Theorem + Numerical · 3.4 / 3.4 / 3.3 (scores 0–4)]', '',
     '![Hill regions and the prime-threshold filtration](figures/librations_krein/hill_regions_thresholds_krein.png)', '', '*Hill regions and the prime-threshold filtration: every ζ threshold L = log n is regular; Krein spectroscopy; the equator crossing at a wall; the Bernoulli numbers fix the archimedean sign change r* = 2π + 0.0067; the Möbius light cone.* [Numerical + Theorem · 3.3 / 3.2 / 2.9; Hill-region dictionary 1.5 (scores 0–4)]', '',
     '![Apsides, escape directions, hodograph and the Levi-Civita map](figures/librations_krein/apsides_escape_directions.png)', '', '*Apsides, escape directions, hodograph and the Levi-Civita map: the escape directions are a conjugate pair that collides on the apsidal line at e = 1 and splits into two real null asymptotes for e > 1; the Frobenius quadratic is the focal quadratic of the conic.* [Theorem · 3.0 (scores 0–4)]', '',
     '![Place-by-place and support filtrations of the Weil form](figures/weil_trichotomy/support_filtration_trichotomy.png)', '', '*Place-by-place and support filtrations of the Weil form: partial products over places stay negative until every prime power ≤ e^L is present; Levinson steps; the literal light cone; Laguerre log-concavity on the line; the elliptic / parabolic / hyperbolic trichotomy with Weil radius L* ≈ 3.82 for Davenport–Heilbronn; over 𝔽_q 4q − a² = q·det T₂.* [Restatement + Numerical · trichotomy 3.92; local definiteness falsified 3.60 (0.6·sig (0–10) + 0.4·prob (0–1))]', '',
     '![The missing piece, refined](figures/sos_morse/missing_piece.png)', '', '*The missing piece, refined: the Levinson/Szegő sum-of-squares factor of the Weil form. ζ: roots on the circle at the zeros. Davenport–Heilbronn: the root that enters the disk is the off-line zero.* [Numerical · 3.6]', '',
     '![Witten-type best constant c(L) for several cushions](figures/sos_morse/sos_constants.png)', '', '*Witten-type best constant c(L) for several cushions: same sign in every variant (circular), ζ at 1 − O(1e-10).* [Restatement · 3.0]', '',
     '![The negative direction of the Davenport–Heilbronn Weil form lives at the frequency of its off-line zero](figures/sos_morse/soft_profiles.png)', '', '*The negative direction of the Davenport–Heilbronn Weil form lives at the frequency of its off-line zero.* [Numerical · 3.2]', '',
     '![Morse count of the co-rotating potential](figures/sos_morse/cr3bp_morse.png)', '', '*Morse count of the co-rotating potential: 2 − 3 = −1 = χ for every mass ratio.* [Theorem · 3.8]', '',
     '![Morse counting of log|Ξ|](figures/sos_morse/xi_morse.png)', '', '*Morse counting of log|Ξ|: off-line zeros force two extra saddles each on the critical line.* [Theorem · 3.4]', '',
     '![Spectral flow](figures/sos_morse/spectral_flow.png)', '', '*Spectral flow: the Morse index of the window Weil form along L.* [Numerical · 3.3]', '',
     '![Count versus stability](figures/sos_morse/count_vs_stability.png)', '', '*Count versus stability: topology fixes the count, the gyroscopic term (positivity) decides stability.* [Theorem · 3.5]', '',
     '## Previous results (v1.9)', '', 'Figures from the research notes folded into v1.9. The Riemann Hypothesis is not proved.', '',
     '![Two-degree-of-freedom chaotic regularized xp](figures/regularized_xp/chaotic_two_dof_xp_orbit_lengths.png)', '', '*Two-degree-of-freedom chaotic regularized xp: periodic-orbit periods drift with energy and do not lock onto k·log p; modular-surface lengths count like the primes but are logs of quadratic units; the explicit-formula sign is cohomological, not a Maslov phase; ζ’s orbit sum improves with the prime cutoff while Davenport–Heilbronn’s degrades.* [Numerical + Theorem + Cited · 3.9 / 4.4 / 4.4 / 3.9 (as a route to RH 2.9; adelic orbit space 3.4)]', '',
     '![Regularized xp](figures/regularized_xp/regularized_xp_legendre_liouville_counting.png)', '', '*Regularized xp: a Poincaré time change with ∂f/∂p ≠ 0 makes xp Legendre-regular; the regularized xp is the hyperbolic Sundman clock of the F/V pair; in a Deninger-type toy the Liouville law gives only ρ ↔ 1 − ρ and a positive metric gives the line; counting matches only the two leading Riemann–von Mangoldt terms.* [Theorem + Numerical · 4.1 / 4.4 / 4.7 / 3.8 (as a route to RH 3.1)]', '',
     '## Previous results (v1.8)', '', 'Figures from the research notes folded into v1.8. The Riemann Hypothesis is not proved.', '',
     '![Central-charge positivity is the Weil form](figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png)', '', '*Central-charge positivity is the Weil form: from the prime side ζ stays ≥ 0 up to L = 8, while Davenport–Heilbronn turns negative near L = 4, with no zeros used.* [Restatement + Numerical · route score 4.7 (as a route to RH 2.8)]', '',
     '![Zero-free signed energy of the heat-flowed Ξ](figures/heat_flow_energy/zero_free_signed_energy_trace.png)', '', '*Zero-free signed energy of the heat-flowed Ξ: every ghost goes negative before it lands, ζ windows stay positive, and the Hermite form counts off-line pairs exactly.* [Theorem + Numerical · 4.4 (as a route to RH 3.3)]', '',
     '![Hofstadter gap widths are log-linear in |n| and close like (distance to the wall)^½ on the lobe side](figures/nc_torus_fv/gap_widths_and_nonnormal_residue.png)', '', '*Hofstadter gap widths are log-linear in |n| and close like (distance to the wall)^½ on the lobe side; ‖P − P&#42;‖ is a gauge quantity that spikes at every collision, not a ghost test.* [Numerical + Theorem · 3.6 / 3.4 / 4.4 (as a ghost detector 1.6)]', '',
     '![F/V on the noncommutative torus](figures/nc_torus_fv/nc_torus_gap_labels_ghost_blind.png)', '', '*F/V on the noncommutative torus: Manin’s lobe / wall / wedge, and gap labels that hold for every zero set, so the K-theory order is ghost-blind.* [Theorem + Numerical · 4.7 (as a route to ζ positivity 2.8)]', '',
     '![The Rodgers–Tao energy is an exact Sundman clock with speed limit 4, but monotone for every real configuration](figures/heat_flow_energy/rodgers_tao_sundman_clock.png)', '', '*The Rodgers–Tao energy is an exact Sundman clock with speed limit 4, but monotone for every real configuration; the near-collision law separates Davenport–Heilbronn from ζ.* [Theorem + Numerical · 4.4]', '',
     '![A Hardy constant for the primes is window positivity restated](figures/hardy_constant/hardy_constant_primes.png)', '', '*A Hardy constant for the primes is window positivity restated: ζ’s margin closes (critical), Davenport–Heilbronn crosses 1 near ℓ = 4–5, and local constants do not glue.* [Theorem + Numerical · 3.9]', '',
     '![Sundman/Levi-Civita clock](figures/sundman_clock/sundman_levi_civita_clock.png)', '', '*Sundman/Levi-Civita clock: the F/V collision becomes a turning point and real τ bounces; positivity is the clock staying real, i.e. RH restated.* [Theorem · 4.7 (circular as a proof route, Restatement 4.4)]', '',
     '![Two Kepler degenerations](figures/sundman_clock/two_kepler_degenerations.png)', '', '*Two Kepler degenerations: F = V is the circular orbit (e = 0), not the Levi-Civita centre collision (e = 1); both share the square-root map.* [Theorem · 4.4]', '',
     f"{D['counts']['concepts']} concepts · {D['counts']['relations']} typed relations · "
     f"{sum('missing piece' in c['axes'] for c in C)} missing pieces. Generated from `atlas.json` by `build_public_md.py`.", '',
     '**Order.** Every section lists its entries in descending priority. Headers read `#rank · priority · name`. '
     'Priority comes from the Heuristic scoring layer described in [scores.md](scores.md): '
     'priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability. The scores are judgment calls, '
     'shown component by component so any reader can disagree with them.', '',
     '**Organizing split.** Phase/unitarity structure (functional equations, |φ| = 1, cocycles, Hecke operators, cusp positivity) is '
     '*ghost-blind*: it holds equally for functions with zeros off the critical line, such as the Davenport–Heilbronn function. '
     'The *sign* of a spectral weight is *ghost-sensitive*, and for ζ that sign is RH.', '',
     '**Labels.** Theorem · Restatement (equivalent to RH or to a known result) · Analogy · Conjecture · Open · Numerical · Heuristic · Cited (taken from the literature). '
     'References of the form “TAA Lemma N” point to the lemma series of the Thermodynamics of Arithmetic Action programme (see README.md for the published volumes). '
     'Citations marked “to verify” have not yet been checked against the source.', '',
     '## Contents', '', '- [Missing pieces](#missing-pieces)', '- [Diagnostic quadrants](#diagnostic-quadrants)', '- [Concepts by primary axis](#concepts-by-primary-axis)']
groups = {}
for c in C: groups.setdefault(c['axes'][0], []).append(c)
order = sorted(groups, key=lambda a: groups[a][0]['rank'])
for a in order:
    if a == 'missing piece': continue
    L.append(f"  - [{a}](#axis-{re.sub(r'[^a-z0-9]+', '-', a.lower()).strip('-')}) ({len(groups[a])})")
L += ['- [Index by rank](#index-by-rank)', '']

MP = [c for c in C if 'missing piece' in c['axes']]
L += ['## Missing pieces', '',
      'These are the objects that, as far as this atlas can tell, would have to exist for a positivity proof of RH along the lines of the function-field case. '
      'Each is labelled Open. Listed in priority order.', '']
for c in MP: L += entry(c)

L += ['## Diagnostic quadrants', '',
      'Sensitivity asks whether a statement holds for ζ (is necessary for, or implied by, RH). Specificity asks whether it fails for the fakes '
      '(the Davenport–Heilbronn function and the ghost zero models). A concept can only detect RH if it scores high on both.', '',
      '| | specificity ≥ 0.8 (fails for the fakes) | specificity < 0.8 (ghost-blind or untested) |', '|---|---|---|']
cnt = {q: sum(c['ranking']['quadrant'] == q for c in C) for q, _ in QUAD}
L += [f"| **sensitivity ≥ 0.8** (true for ζ) | RH-sharp: {cnt['RH-sharp']} | true but ghost-blind/untested: {cnt['true but ghost-blind/untested']} |",
      f"| **sensitivity < 0.8** (interpretive) | sharp but interpretive: {cnt['sharp but interpretive']} | background: {cnt['background']} |", '']
for q, desc in QUAD:
    L += [f"### {desc} ({cnt[q]})", '']
    L += [f"- #{c['rank']} · {c['priority']:.3f} · {link(c['id'])} [{c['label']}]" for c in C if c['ranking']['quadrant'] == q]
    L.append('')

L += ['## Concepts by primary axis', '', 'Sections are ordered by their highest-ranked entry; entries within each section by descending priority. '
      'Missing pieces are listed above and not repeated.', '']
for a in order:
    if a == 'missing piece': continue
    L += [f"## Axis: {a} <a id=\"axis-{re.sub(r'[^a-z0-9]+', '-', a.lower()).strip('-')}\"></a>", '']
    for c in groups[a]: L += entry(c)

L += ['## Index by rank', '', '| # | priority | concept | label | quadrant |', '|---|---|---|---|---|']
L += [f"| {c['rank']} | {c['priority']:.3f} | {link(c['id'])} | {c['label']} | {c['ranking']['quadrant']} |" for c in C]
L.append('')
txt = '\n'.join(L)
assert '\\' not in txt.replace('\\|', ''), 'backslash found'
open(os.path.join(HERE, 'ATLAS.md'), 'w', encoding='utf-8').write(txt)
print('ATLAS.md written:', len(C), 'concepts,', len(MP), 'missing pieces,', len(txt.encode()), 'bytes')

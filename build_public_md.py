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
VERSION, VDATE = '1.9', '30 Oct 2026'

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
     '## Latest results (v1.9)', '', 'Figures from the research notes folded into v1.9 (see README.md for the gallery and CHANGELOG.md for details). The Riemann Hypothesis is not proved.', '',
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

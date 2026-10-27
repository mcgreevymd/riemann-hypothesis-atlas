#!/usr/bin/env python3
"""Query The RH Atlas (public edition, ./atlas.json).

  python3 q.py rosati                 one entry, with outgoing and incoming relations (fuzzy match on id, name, aliases)
  python3 q.py --axis ghost-blind     every concept carrying that axis, by rank
  python3 q.py --list [--by name|label|priority]   all concepts (default: descending priority)
  python3 q.py --quadrant RH-sharp    every concept in a diagnostic quadrant, by rank
  python3 q.py --missing              the missing pieces, by rank
"""
import json, os, sys, difflib
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atlas.json'), encoding='utf-8'))['concepts']
by = {c['id']: c for c in D}
def keys(c): return [c['id'], c['name'].lower()] + [a.lower() for a in c['aliases']]
def find(q):
    q = q.lower()
    hits = [c for c in D if any(q == k for k in keys(c))] or [c for c in D if any(q in k for k in keys(c))]
    if hits: return sorted(hits, key=lambda c: c['rank'])
    allk = {k: c for c in D for k in keys(c)}
    return [allk[k] for k in difflib.get_close_matches(q, allk, n=3, cutoff=0.5)]
def line(c): return f"#{c['rank']:<4}{c['priority']:.3f}  {c['id']:26} {c['label']:12} {c['name']}"
def show(c):
    print(f"■ #{c['rank']} · priority {c['priority']:.3f} · {c['name']}  [{c['id']}]  ({c['label']})")
    print('  scores (Heuristic):', ', '.join(f"{k}={v}" for k, v in c.get('ranking', {}).items()))
    if c['aliases']: print('  aka:', ', '.join(c['aliases']))
    print('  plain:', c['plain']); print('  core :', c['core'])
    if c['formula']: print('  formula:', c['formula'])
    if c['numbers']: print('  numbers:', ' | '.join(c['numbers']))
    if c.get('proved'): print('  proved around it:', c['proved'])
    if c.get('tests'): print('  tests:', c['tests'])
    print('  TAA lemmas:', ', '.join(c['lemmas']) or '—')
    print('  axes :', ', '.join(c['axes']))
    for p in c['pitfalls']: print('  ⚠', p)
    if c['uncertain']: print('  ? not verified / open:', c['uncertain'])
    print('  → out:')
    for r in c['rels']:
        print(f"     {r['type']:18} {r['to']:26} {by[r['to']]['name']}" + (f"  — {r['note']}" if r.get('note') else ''))
    inn = [(d, r) for d in D for r in d['rels'] if r['to'] == c['id']]
    if inn:
        print('  ← in:')
        for d, r in inn: print(f"     {d['id']:26} {r['type']:18} {d['name']}")
a = sys.argv[1:]
if a and a[0] in ('-h', '--help'): print(__doc__)
elif not a or a[0] == '--list':
    k = a[a.index('--by') + 1] if '--by' in a and a.index('--by') + 1 < len(a) else 'priority'
    key = {'priority': lambda c: (-c['priority'], c['rank']), 'name': lambda c: c['name'].lower(),
           'label': lambda c: (c['label'], c['rank'])}.get(k, lambda c: c['rank'])
    for c in sorted(D, key=key): print(line(c))
elif a[0] == '--axis':
    q = ' '.join(a[1:]).lower()
    for c in sorted(D, key=lambda c: c['rank']):
        if any(q in x.lower() for x in c['axes']): print(line(c))
elif a[0] == '--quadrant':
    q = ' '.join(a[1:]).lower()
    for c in sorted(D, key=lambda c: c['rank']):
        if q in c['ranking']['quadrant'].lower(): print(line(c))
elif a[0] == '--missing':
    for c in sorted(D, key=lambda c: c['rank']):
        if 'missing piece' in c['axes']: print(line(c))
else:
    h = find(' '.join(a))
    if not h: print('no match'); sys.exit(1)
    show(h[0])
    if len(h) > 1: print('\n  also matched:', ', '.join(x['id'] for x in h[1:8]))

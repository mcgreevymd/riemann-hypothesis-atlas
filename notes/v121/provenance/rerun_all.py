#!/usr/bin/env python3
"""Rerun harness for atlas2060 (bundle-relative). Rebuilds each source directory in a scratch tree from scripts/<dir>/ plus the
archived inputs data/<dir>_*.json (so archived outputs stay pristine); scripts use sibling-relative paths '../<dir>/'.
runs the listed scripts with OPENBLAS_NUM_THREADS=1, records exit code, wall time,
and compares regenerated JSON numbers against the archived JSON (max relative diff)."""
import os, sys, json, shutil, subprocess, time, pathlib, re, math
HERE = pathlib.Path(__file__).resolve().parent
SCR = HERE / 'scripts'; DATA = HERE / 'data'
ROOT = pathlib.Path(os.environ.get('RERUN_ROOT', HERE / 'rerun_tree')).resolve()
JOBS = [l.split() for l in """
matching1989 ff1989.py inertia1989.py e0tol1989.py nyq1989.py
eisenstein1990 analytic1990.py ma_explicit1990.py eis1990.py
hodge1991 m12_lattice1991.py periods1991.py conic1991.py
boundary1994 boundary1994.py duality1994.py
counterterm1995 connes_arch1995.py connes_arch_fft1995.py det_scale1995.py maass1995.py
parabolic1998 conic1998.py pencilW1998.py anchor1998.py hess1998.py
effectivity2001 relrr2001.py arith2001.py p1asym2001.py selfdual2001.py
intersection2002 tor2002.py hecke2002.py lefschetz2002.py
diagonal2003 arak2003.py spin2004.py
geometry2006 osc2006.py
sos2010 ident2010.py unconstrained2010.py buckling2010.py
polarity2021 check2021.py
poincare2024 check2024.py
modular2026 check2026.py
realization2033 check2033.py
blocks2038 check2038.py
kms2040 check2040.py
logpoincare2044 certify2044.py ghost2044.py buckling_edge2044.py
multiprime2047 certify2047.py certify_two2047.py ghost2047.py
inertia2057 certify_inertia2057.py check2057.py
""".strip().splitlines()]
SKIP_EXT = {'.pdf', '.html', '.png', '.zip'}
def nums(x, path=''):
    if isinstance(x, bool): return
    if isinstance(x, (int, float)): yield path, float(x); return
    if isinstance(x, str):
        try:
            v = float(x); yield path, v
        except ValueError: pass
        return
    if isinstance(x, dict):
        for k, v in x.items(): yield from nums(v, path + '/' + str(k))
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from nums(v, path + f'[{i}]')
def strs(x, path=''):
    if isinstance(x, str): yield path, x
    elif isinstance(x, dict):
        for k, v in x.items(): yield from strs(v, path + '/' + str(k))
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from strs(v, path + f'[{i}]')
def compare(a, b):
    """numeric fields: max relative diff; non-numeric string fields (e.g. interval enclosures): exact equality, mismatches reported."""
    A = dict(nums(a)); B = dict(nums(b)); worst = 0.0; wk = None; n = 0
    for k, v in A.items():
        if k in B and math.isfinite(v) and math.isfinite(B[k]):
            n += 1; d = abs(v - B[k]) / max(1e-300, abs(v), abs(B[k])) if (v or B[k]) else 0.0
            if d > worst: worst, wk = d, k
    SA = {k: v for k, v in strs(a) if k not in A}; SB = dict(strs(b))
    same = sum(1 for k, v in SA.items() if SB.get(k) == v); diff = [k for k, v in SA.items() if k in SB and SB[k] != v]
    return n, worst, wk, same, diff[:5]
def main(only=None):
    if ROOT.exists(): shutil.rmtree(ROOT)
    results = []
    for job in JOBS:
        d, scripts = job[0], job[1:]
        if only and d not in only: continue
        dst = ROOT / d; shutil.copytree(SCR / d, dst, ignore=lambda p, names: [n for n in names if pathlib.Path(n).suffix in SKIP_EXT or n == '__pycache__'])
        for f in DATA.glob(d + '_*.json'): shutil.copy(f, dst / f.name[len(d) + 1:])
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    for job in JOBS:
        d, scripts = job[0], job[1:]
        if only and d not in only: continue
        for s in scripts:
            out_json = None
            t0 = time.time()
            r = subprocess.run([sys.executable, s], cwd=ROOT / d, env=env, capture_output=True, text=True, timeout=1500)
            dt = time.time() - t0
            (ROOT / d / (s + '.log')).write_text(r.stdout[-20000:] + '\n--stderr--\n' + r.stderr[-5000:])
            stem = s[:-3]; cmp = None
            for cand in [stem + '.json'] + ([ 'certify_inertia2057.json', 'certify_two_inertia2057.json'] if s == 'certify_inertia2057.py' else []):
                o, n = DATA / f'{d}_{cand}', ROOT / d / cand
                if o.exists() and n.exists() and n.stat().st_mtime < t0:
                    results.append(dict(dir=d, script=s, exit=r.returncode, seconds=round(dt, 1), json=cand, compared_numbers=0, max_rel_diff=None, worst_key='NOT REGENERATED')); cmp = (cand,); continue
                if o.exists() and n.exists():
                    try: cmp = (cand,) + compare(json.load(open(o)), json.load(open(n)))
                    except Exception as e: cmp = (cand, 'cmp-error', str(e))
                    results.append(dict(dir=d, script=s, exit=r.returncode, seconds=round(dt, 1), json=cand,
                                        compared_numbers=cmp[1], max_rel_diff=cmp[2], worst_key=cmp[3] if len(cmp) > 3 else None,
                                        strings_equal=cmp[4] if len(cmp) > 4 else None, strings_differ=cmp[5] if len(cmp) > 5 else None))
            if cmp is None:
                results.append(dict(dir=d, script=s, exit=r.returncode, seconds=round(dt, 1), json=None))
            print(results[-1], flush=True)
    return results
if __name__ == '__main__':
    only = set(sys.argv[1:]) or None
    res = main(only)
    out = pathlib.Path(os.environ.get('RERUN_OUT', HERE / 'checks' / 'rerun_results.json'))
    out.parent.mkdir(exist_ok=True); json.dump(res, open(out, 'w'), indent=1)

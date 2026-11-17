#!/usr/bin/env python3
"""v1.23 smoke test (about 30 s). Run from anywhere:  python3 notes/v123/provenance/SMOKE_TEST.py
Checks: atlas counts/rank/ordering invariants, delta merged, no backslashes, no machine-local paths, and quick
re-derivations (plastic threshold to 40 digits; one zeta window and one chi_4 window against the stored outputs).
Numerical checks are not certificates."""
import json, os, sys, re, pathlib, subprocess
H=pathlib.Path(__file__).resolve().parent
ROOT=H.parents[2] if (H.parents[2]/'atlas.json').exists() else None
ok=True
def hasbs(o):
    if isinstance(o,str): return '\\' in o
    if isinstance(o,dict): return any(hasbs(v) for v in o.values())
    if isinstance(o,list): return any(hasbs(v) for v in o)
    return False
def check(name,cond,info=''):
    global ok; ok&=bool(cond); print(('PASS ' if cond else 'FAIL ')+name+(' — '+str(info) if info else ''))
delta=json.load(open(H/'delta'/'atlas_delta_v123.json',encoding='utf-8'))
check('delta size',len(delta['concepts'])==13 and sum(len(c['rels']) for c in delta['concepts'])==44)
check('delta has no backslash',not hasbs(delta))
if ROOT:
    A=json.load(open(ROOT/'atlas.json',encoding='utf-8')); C=A['concepts']; by={c['id']:c for c in C}
    check('counts 1101/2217',A['counts']=={'concepts':1101,'relations':2217} and len(C)==1101 and sum(len(c['rels']) for c in C)==2217,A['counts'])
    r1=min(C,key=lambda c:c['rank']); check('rank 1 unchanged',r1['id']=='kahler_triple_polarization')
    check('ranks 1..N',sorted(c['rank'] for c in C)==list(range(1,len(C)+1)))
    check('all delta ids merged',all(c['id'] in by for c in delta['concepts']))
    check('all relation targets exist',all(r['to'] in by for c in C for r in c['rels']))
    check('Open ~1.8 present',sum(json.dumps(c,ensure_ascii=False).count('Open ~1.8') for c in C)>=1)
    check('no backslash in atlas',not hasbs(A))
import mpmath as mp
mp.mp.dps=45
P=mp.findroot(lambda y:y**3-y-1,1.3); w0=mp.log(P)
K=lambda w: -mp.exp(w/2)/(2*mp.sinh(w))+2*mp.cosh(w/2)
check('K(log P) = 0',abs(K(w0))<mp.mpf(10)**-40,mp.nstr(K(w0),3))
check('log P = 0.2811995743',abs(w0-mp.mpf('0.28119957432296184651'))<mp.mpf(10)**-18)
S=H/'scripts'/'lem2253'
for args,stored in [(['1','50','60'],'z_1_50_60.json'),(['1.2','50','60','chi4'],'c_1.2_50_60.json')]:
    r=subprocess.run([sys.executable,str(S/'lemtest.py')]+args,cwd=S,capture_output=True,text=True)
    if r.returncode: check('rerun '+' '.join(args),False,r.stderr[-200:]); continue
    new=json.loads(r.stdout); old=json.load(open(H/'data'/'lem2253'/stored))
    keys=[k for k in old if k not in ('time',)]
    check('rerun matches stored '+stored,all(new[k]==old[k] for k in keys))
    if 'even_lt_odd' in new: check('zeta A=1: even below odd, S>0, one negative',new['even_lt_odd'] and float(new['S_scalar'])>0 and new['Q_nneg']==1)
bad=[str(p.relative_to(H)) for p in H.rglob('*') if p.is_file() and p.suffix in {'.md','.py','.json','.txt','.out'} and p.name!='SMOKE_TEST.py' and re.search(r'/(workspace|home)/',p.read_text(errors='ignore'))]
check('no machine-local paths in provenance',not bad,bad[:5])
print('SMOKE', 'OK' if ok else 'FAILED'); sys.exit(0 if ok else 1)

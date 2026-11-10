#!/usr/bin/env python3
"""v1.22 smoke test (about 20 s). Run from anywhere:  python3 notes/v122/provenance/SMOKE_TEST.py
Checks: atlas counts/rank/ordering invariants, delta merged, no backslashes, and quick re-derivations
(product formula, function-field Cayley-Hamilton, Shioda-Tate identity on 2 windows). Numerical checks are not certificates."""
import json, os, sys, subprocess, tempfile, pathlib
os.environ['OPENBLAS_NUM_THREADS']='1'
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
delta=json.load(open(H/'delta'/'atlas_delta_v122.json',encoding='utf-8'))
check('delta size',len(delta['concepts'])==22 and sum(len(c['rels']) for c in delta['concepts'])==65)
check('delta has no backslash',not hasbs(delta))
if ROOT:
    A=json.load(open(ROOT/'atlas.json',encoding='utf-8')); C=A['concepts']; by={c['id']:c for c in C}
    check('counts 1088/2173',A['counts']=={'concepts':1088,'relations':2173} and len(C)==1088 and sum(len(c['rels']) for c in C)==2173,A['counts'])
    r1=min(C,key=lambda c:c['rank']); check('rank 1 unchanged',r1['id']=='kahler_triple_polarization')
    check('ranks 1..N',sorted(c['rank'] for c in C)==list(range(1,len(C)+1)))
    check('all delta ids merged',all(c['id'] in by for c in delta['concepts']))
    check('all relation targets exist',all(r['to'] in by for c in C for r in c['rels']))
    check('Open ~1.8 present',sum(json.dumps(c,ensure_ascii=False).count('Open ~1.8') for c in C)>=1)
    check('no backslash in atlas',not hasbs(A))
S=H/'scripts'/'night2105'
with tempfile.TemporaryDirectory() as t:
    for s in ['n1_product_formula.py','n4_cayley_hamilton.py']:
        r=subprocess.run([sys.executable,str(S/s)],cwd=t,capture_output=True,text=True); check('rerun '+s,r.returncode==0,r.stderr[-200:])
    n1=json.load(open(pathlib.Path(t)/'n1_product_formula.json')); check('product formula error < 1e-12',n1['max_abs_err_product_formula']<1e-12)
    n4=json.load(open(pathlib.Path(t)/'n4_cayley_hamilton.json'))['rows']
    check('FF rank = min(K+1,2g) and kernel = L-tilde multiples',all(r['rank']==r['expected'] and r['max_resid_Ltilde_shifts']<1e-10 and r['G_minus_P_plus_T']<1e-9 for r in n4))
sys.path.insert(0,str(S))
import numpy as np, scipy.linalg as la, common2105 as c
for A,drop in [(1.1,()),(2.0,()),(2.0,(2,))]:
    Q,B=c.matrix(A,256,drop=drop); nQ=c.inertia(la.eigvalsh(Q))[0]; S_=B.T@la.solve(Q,B,assume_a='sym'); nS=c.inertia(la.eigvalsh(S_))[0]
    V=la.qr(B,mode='full')[0];Z=V[:,2:];nE=c.inertia(la.eigvalsh(Z.T@Q@Z))[0]
    check(f'Shioda-Tate identity A={A} drop={drop}',nE==nQ-nS,(nQ,nS,nE))
    if not drop: check(f'zeta counts A={A}',(nQ,nS,nE)==(1,1,0))
import re
bad=[str(p.relative_to(H)) for p in H.rglob('*') if p.is_file() and p.suffix in {'.md','.py','.json','.txt','.out'} and p.name!='SMOKE_TEST.py' and re.search(r'/(workspace|home)/',p.read_text(errors='ignore'))]
check('no machine-local paths in provenance',not bad,bad[:5])
print('SMOKE', 'OK' if ok else 'FAILED'); sys.exit(0 if ok else 1)

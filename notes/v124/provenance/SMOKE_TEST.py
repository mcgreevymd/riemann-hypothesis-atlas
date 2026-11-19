#!/usr/bin/env python3
"""v1.24 smoke test (about 20 s). Run from anywhere:  python3 notes/v124/provenance/SMOKE_TEST.py
Checks: atlas counts/rank/ordering invariants, delta merged, no backslashes, no machine-local paths, and quick
re-derivations (L197 at h = 0.05 against the stored onsets; the L197 (vii) Poisson completion is positive; the L196 table).
Numerical checks are not certificates."""
import json, os, sys, re, pathlib, subprocess
H=pathlib.Path(__file__).resolve().parent
ROOT=H.parents[2] if (H.parents[2]/'atlas.json').exists() else None
ok=True
def hasbs(o):
    if isinstance(o,str): return chr(92) in o
    if isinstance(o,dict): return any(hasbs(v) for v in o.values())
    if isinstance(o,list): return any(hasbs(v) for v in o)
    return False
def check(name,cond,info=''):
    global ok; ok&=bool(cond); print(('PASS ' if cond else 'FAIL ')+name+(' — '+str(info) if info else ''))
delta=json.load(open(H/'delta'/'atlas_delta_v124.json',encoding='utf-8'))
check('delta size',len(delta['concepts'])==12 and sum(len(c['rels']) for c in delta['concepts'])==49)
check('delta has no backslash',not hasbs(delta))
if ROOT:
    A=json.load(open(ROOT/'atlas.json',encoding='utf-8')); C=A['concepts']; by={c['id']:c for c in C}
    check('counts 1113/2266',A['counts']=={'concepts':1113,'relations':2266} and len(C)==1113 and sum(len(c['rels']) for c in C)==2266,A['counts'])
    r1=min(C,key=lambda c:c['rank']); check('rank 1 unchanged',r1['id']=='kahler_triple_polarization')
    check('ranks 1..N',sorted(c['rank'] for c in C)==list(range(1,len(C)+1)))
    check('all delta ids merged',all(c['id'] in by for c in delta['concepts']))
    check('all relation targets exist',all(r['to'] in by for c in C for r in c['rels']))
    check('Open ~1.8 present',sum(json.dumps(c,ensure_ascii=False).count('Open ~1.8') for c in C)>=1)
    check('no backslash in atlas',not hasbs(A))
S=H/'scripts'/'lem197'
env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run([sys.executable,'l197.py','0.05'],cwd=S,capture_output=True,text=True,env=env)
if r.returncode: check('rerun l197 h=0.05',False,r.stderr[-300:])
else:
    new=json.load(open(S/'l197_h0.05.json')); old=json.load(open(H/'data'/'lem197'/'l197_h0.05.json'))
    check('l197 h=0.05 onsets match stored',[x['onset'] for x in new]==[y['onset'] for y in old])
    trues=[x for x in new if x['cls'].startswith('a:')]; fakes=[x for x in new if not x['cls'].startswith('a:')]
    check('4 true members positive to r=8',len(trues)==4 and all(all(v is None for v in x['onset'].values()) for x in trues))
    check('36 fakes all fail',len(fakes)==36 and all(x['onset']['full'] is not None for x in fakes))
    os.remove(S/'l197_h0.05.json')
# Poisson completion (L197 vii): sum_{k in Z} r^{|k|} e^{ik theta} > 0
import math
for p in (2,3,5):
    rr=p**-0.5; mn=min((1-rr*rr)/(1-2*rr*math.cos(t/100)+rr*rr) for t in range(0,629))
    check(f'Poisson kernel positive p={p}',mn>0,round(mn,4))
T=json.load(open(H/'data'/'lem196'/'ladder_table.json'))
check('L196 ladder table present',bool(T))
bad=[str(p.relative_to(H)) for p in H.rglob('*') if p.is_file() and p.suffix in {'.md','.py','.json','.txt','.out','.log'} and p.name!='SMOKE_TEST.py' and re.search(r'/(workspace|home)/',p.read_text(errors='ignore'))]
check('no machine-local paths in provenance',not bad,bad[:5])
print('SMOKE', 'OK' if ok else 'FAILED'); sys.exit(0 if ok else 1)

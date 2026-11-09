"""Independent rerun of representative exact-cell counts and stored certificate conclusions."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from inertia2057 import *
from certify_inertia2057 import run
# Re-execute the key interval+continuum proof at width one, not only inspect JSON.
cert=run(False)
old=json.load(open(OUT/'inertia2057.json'))['rows']
for A in [1.,1.1,3.]:
 r=analyze(A,512);ref=next(x for x in old if x['A']==A and x['n']==512)
 assert abs(r['constrained_min']-ref['constrained_min'])<1e-10
 assert r['Q_inertia']==[1,0,511] and r['W_inertia']==[0,0,512]
 assert r['constrained_inertia']==[0,0,510] and r['identity_rhs']==0
for fn in ['certify_inertia2057.json','certify_two_inertia2057.json']:
 c=json.load(open(OUT/fn));assert c['all_assertions_passed'] and c['continuum_Q_index']==1
scan=json.load(open(OUT/'scan2057.json'))
for r in scan['coarse_scan']+scan['refined']:
 assert r['Q_inertia'][0]==1 and r['W_inertia'][0]==0
 assert r['constrained_inertia'][0]==0 and r['identity_rhs']==0
json.dump(dict(all_assertions_passed=True,width_one_certificate_reexecuted=True,representative_spectra_recomputed=[1,1.1,3],scan_rows_checked=len(scan['coarse_scan'])+len(scan['refined'])),open(OUT/'check2057.json','w'),indent=2)
print('INDEPENDENT RERUN PASSED')

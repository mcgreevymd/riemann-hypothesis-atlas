# RR/effectivity probe: is the unique positive-I class (bulk-negative eigvec) effective (F>=0) modulo the near-null cluster?
import numpy as np, runpy, json
from scipy.optimize import linprog
ns=runpy.run_path('map1965.py')
Bq=ns['K0']*ns['M0']+ns['Earch']+ns['Wp']; ev,V=np.linalg.eigh(Bq); Phi=ns['Phi']; u=ns['u']
v0=V[:,0]@Phi; v0=v0*np.sign(v0[len(u)//2])
r={'v0_min/max':float(v0.min()/v0.max()),'v0_nonneg_frac':float((v0>=0).mean())}
for nnull in [0,3,9,10]:
    N=(V[:,1:1+nnull].T@Phi) if nnull else np.zeros((0,len(u)))
    idx=np.arange(1,len(u)-1,10)                 # interior grid
    # maximize t s.t. v0 + N^T y >= t*max|v0| on interior, |y|<=5
    c=np.zeros(nnull+1); c[-1]=-1
    Aub=np.hstack([-N[:,idx].T, np.full((len(idx),1),np.abs(v0).max())]) if nnull else np.full((len(idx),1),np.abs(v0).max())
    res=linprog(c,A_ub=Aub,b_ub=v0[idx],bounds=[(-5,5)]*nnull+[(None,None)])
    r['best_min_ratio_with_%d_null'%nnull]=float(-res.fun) if res.success else None
json.dump(r,open('rr1965.json','w'),indent=1); print(json.dumps(r,indent=1))

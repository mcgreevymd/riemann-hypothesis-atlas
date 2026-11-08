import json, numpy as np, math
exec(open('krein1944.py').read().split("out={}; t0")[0])
from scipy.special import psi
res={}
for A in [0.6,1.0]:
    ns,an,Om,Pr=parts(A); joint=lambda x: Om(x)+Pr(x)
    for K,span,C,X in [(400,40,1e4,80),(800,80,1e5,120)]:
        r,c,a=solve(A,joint,K=K,amax=A+span,X=X,nx=int(X*120),C=C)
        res[f'A={A},K={K},span={span},C={C}']=r; print(A,K,span,C,r,flush=True)
json.dump(res,open('scan1944.json','w'),indent=1)

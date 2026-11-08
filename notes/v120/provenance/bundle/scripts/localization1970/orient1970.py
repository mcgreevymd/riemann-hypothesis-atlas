import json, numpy as np
from loc1970 import run
import loc1970, mpmath as mp
out=[]
for conj in [True, False]:
    for args in [(1.0,'sin8',[2],12,0.025),(1.0,'poly6',[2],12,0.025),(1.0,'skew',[2],12,0.025),(0.6,'sin8',[],12,0.025),(0.6,'sin8',[2],12,0.025)]:
        r=run(*args,conj=conj); r['orientation']='Phat=M_c H M_cbar (correct F)' if conj else 'Phat=M_cbar H M_c (inversion-conjugate J F H F J)'
        out.append(r)
        print(r['orientation'][:22],args[:3],'tau_num %.5f  -bulk %.5f  D %.5f  W-P %.5f  resid %.5f  semi_m+ %.5f'%(r['tau_num'],r['minus_bulk'],r['D'],r['W_minus_P'],r['residual_W_minus_D'],r['semiclassical_m_plus']),flush=True)
json.dump(out,open('orient1970.json','w'),indent=1,default=float)

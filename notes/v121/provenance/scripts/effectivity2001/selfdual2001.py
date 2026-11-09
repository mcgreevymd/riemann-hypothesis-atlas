# Theta-RR on Spec Z-bar with weight exp(-pi c x^2): exact RR (same weight on L and L^dual) holds only at c=1 (Poisson self-duality).
import numpy as np, json
def h0(scale,c): x=np.arange(-60,61); return np.log(np.sum(np.exp(-np.pi*c*(x*scale)**2)))
out={}
for c in (1.0,2.0,0.5):
    out[f'c={c}']=[dict(deg=d,RR_defect=float(h0(np.exp(-d),c)-h0(np.exp(d),c)-d)) for d in (-0.5,0.0,0.7,1.5)]
json.dump(out,open('selfdual2001.json','w'),indent=1); print(json.dumps(out,indent=1))

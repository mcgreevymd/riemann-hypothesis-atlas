"""N2c: sweep a common prime-weight scale s (s=1 is zeta) and record which count moves: n_-(Q) (Hodge index / bound states) or n_-(S) (trivial lattice).
Sensitivity control only; s != 1 is not Euler data."""
import json, numpy as np, scipy.linalg as la, common2105 as c
rows=[]
for A in [1.1,1.5,2.0]:
    for s in np.round(np.linspace(0.8,1.2,41),3):
        Q,B=c.matrix(A,256,scale=float(s)); ev=la.eigvalsh(Q)
        S=B.T@la.solve(Q,B,assume_a='sym'); sS=la.eigvalsh(S)
        V=la.qr(B,mode='full')[0];Z=V[:,2:];ec=la.eigvalsh(Z.T@Q@Z)
        rows.append(dict(A=A,s=float(s),nQ=c.inertia(ev)[0],nS=c.inertia(sS)[0],nE=c.inertia(ec)[0],Q_low=ev[:6].tolist(),S=sS.tolist(),minE=float(ec[0])))
    print(A,[ (r['s'],r['nQ'],r['nS'],r['nE']) for r in rows if r['A']==A and abs((r['s']*40)%2)<1e-6 ])
json.dump(dict(note='numerical, n=256 cells; s scales every prime weight; control only',rows=rows),open('n2c_scale_sweep.json','w'),indent=1)

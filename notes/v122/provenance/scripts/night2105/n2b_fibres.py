"""N2b: Riesz lifts H_pm = Q^{-1} r_pm of the bidegree functionals as 'fibre classes'.
Template (C x C): f1.f1 = f2.f2 = 0, f1.f2 = 1, Gram = J. Here I = -Q, I(H_i,H_j) = -S_ij."""
import json, numpy as np, scipy.linalg as la, common2105 as c
rows=[]
for A in [0.5,0.694,1.0,1.1,1.386,1.5,2.0,2.5,3.0]:
    for n in [256,512,1024]:
        Q,B=c.matrix(A,n); S=B.T@la.solve(Q,B,assume_a='sym'); G=-S
        r=dict(A=A,n=n,I_HpHp=G[0,0],I_HmHm=G[1,1],I_HpHm=G[0,1],eig=la.eigvalsh(S).tolist(),det=float(np.linalg.det(S)))
        rows.append(r); print(f"A={A:5} n={n:4} I(H+,H+)={G[0,0]:+.6f} I(H-,H-)={G[1,1]:+.6f} I(H+,H-)={G[0,1]:+.6f} detS={r['det']:+.6f}",flush=True)
json.dump(dict(note='numerical only',rows=rows),open('n2b_fibres.json','w'),indent=1)

"""N3b: direct Krein check: at each eigenvalue lam_j of W|E0, M(lam_j) = B^T (Q - lam_j)^{-1} B is singular (relative smallest singular value)."""
import json, numpy as np, scipy.linalg as la, common2105 as c
out=[]
for A,case,drop in [(1.1,'full',()),(1.5,'full',()),(2.0,'full',()),(1.5,'drop2',(2,))]:
    Q,B=c.matrix(A,512,drop=drop); V=la.qr(B,mode='full')[0];Z=V[:,2:];ec=la.eigvalsh(Z.T@Q@Z)
    rel=[]
    for lam in ec[:6]:
        Mm=B.T@la.solve(Q-lam*np.eye(len(Q)),B); s=la.svdvals(Mm); rel.append(float(s[-1]/s[0]))
    # control: midpoints between eigenvalues are not singular
    ctrl=[]
    for lam in (ec[:5]+ec[1:6])/2:
        Mm=B.T@la.solve(Q-lam*np.eye(len(Q)),B); s=la.svdvals(Mm); ctrl.append(float(s[-1]/s[0]))
    out.append(dict(A=A,case=case,eig_WE0=ec[:6].tolist(),rel_sigma_min_at_eigs=rel,rel_sigma_min_at_midpoints=ctrl))
    print(A,case,['%.1e'%x for x in rel],'| midpoints',['%.1e'%x for x in ctrl])
json.dump(dict(note='numerical, n=512',rows=out),open('n3b_krein_direct.json','w'),indent=1)

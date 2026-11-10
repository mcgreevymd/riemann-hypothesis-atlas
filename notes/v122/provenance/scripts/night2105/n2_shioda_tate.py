"""N2: finite-window Shioda-Tate split. I = -Q (zeros-blind renormalized trace pairing, t2072).
Trivial lattice T = span{Q^{-1} B} (Riesz lifts of C+-), Gram of I on T = -S, S = B^T Q^{-1} B. E0 = ker B^T is I-orthogonal to T.
Exact: In(I) = In(-S) + In(-W|E0)  =>  n_-(W|E0) = n_-(Q) - n_-(S)   (Q, S nondegenerate).
'Hodge index' for I  <=>  n_+(I) = n_-(Q) = 1  ('one bound state of H_A below M_A').
Controls: delete atoms / rescale prime weights, and record WHICH of the two counts moves."""
import json, numpy as np, scipy.linalg as la, common2105 as c
rows=[]
cases=[('full',(),1.0),('drop2',(2,),1.0),('drop3',(3,),1.0),('drop4',(4,),1.0),('primes x0.9',(),0.9),('primes x1.1',(),1.1),('primes x0',(),0.0)]
for A in [0.694,1.0,1.1,1.5,2.0,2.5]:
    for n in [256,512]:
        for name,drop,sc in cases:
            Q,B=c.matrix(A,n,drop=drop,scale=sc)
            evQ=la.eigvalsh(Q)
            S=B.T@la.solve(Q,B,assume_a='sym'); sS=la.eigvalsh(S)
            V=la.qr(B,mode='full')[0];Z=V[:,2:];ec=la.eigvalsh(Z.T@Q@Z)
            nQ=c.inertia(evQ)[0]; nS=c.inertia(sS)[0]; nE=c.inertia(ec)[0]
            r=dict(A=A,n=n,case=name,n_minus_Q=nQ,S_eig=sS.tolist(),n_minus_S=nS,det_S=float(np.linalg.det(S)),n_minus_WE0=nE,minWE0=float(ec[0]),
                   identity_ok=(nE==nQ-nS),Q_low=evQ[:3].tolist())
            rows.append(r)
            print(f"A={A:5} n={n} {name:12s} n-(Q)={nQ} S_eig=({sS[0]:+.5f},{sS[1]:+.5f}) n-(S)={nS} n-(W|E0)={nE} min={ec[0]:+.3e} id={'ok' if r['identity_ok'] else 'FAIL'}",flush=True)
json.dump(dict(note='numerical only (double precision Galerkin, inertia2057 cell model); controls are sensitivity tests, not Euler data',rows=rows),open('n2_shioda_tate.json','w'),indent=1)

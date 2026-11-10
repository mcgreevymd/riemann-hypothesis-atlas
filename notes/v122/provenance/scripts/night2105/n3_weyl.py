"""N3: the pole plane as a boundary condition. M(lam) = B^T (Q - lam)^{-1} B (2x2 Weyl/Krein function, Herglotz: M' = B^T (Q-lam)^{-2} B >= 0).
Krein formula (exact, finite dim): Q_Theta := Q + B Theta B^T has det(Q_Theta - lam)/det(Q - lam) = det(I + Theta M(lam)).
 Theta = 0 -> Q ; Theta = J -> W = Q + P ; Theta -> infinity -> compression to E0 = ker B^T, spectrum = zeros of det M(lam).
Penalty threshold: with n_-(Q) = 1, Q + c B B^T >= 0  <=>  c >= c* = 1/|lambda_min(M(0))|  (when lambda_max(M(0)) > 0)."""
import json, numpy as np, scipy.linalg as la, common2105 as c
from scipy.optimize import brentq
out=[]
def M(Q,B,lam): return B.T@la.solve(Q-lam*np.eye(len(Q)),B)
for A,case,drop,n in [(1.1,'full',(),512),(1.5,'full',(),512),(1.5,'drop2',(2,),512),(2.0,'full',(),512),(2.0,'primes x1.1',(),512)]:
    sc=1.1 if 'x1.1' in case else 1.0
    Q,B=c.matrix(A,n,drop=drop,scale=sc)
    evQ=la.eigvalsh(Q); V=la.qr(B,mode='full')[0];Z=V[:,2:];ec=la.eigvalsh(Z.T@Q@Z); ew=la.eigvalsh(Q+B@c.J@B.T)
    # zeros of det M on (-inf, ec[2]) avoiding poles of Q: scan
    grid=np.sort(np.concatenate([np.linspace(min(evQ[0],ec[0])-0.5,ec[min(3,len(ec)-1)]+1e-3,4001)]))
    def f(l): return np.linalg.det(M(Q,B,l))
    def g(l): return np.linalg.det(np.eye(2)+c.J@M(Q,B,l))
    zM=[];zW=[]
    for a,b in zip(grid[:-1],grid[1:]):
        if np.any((evQ>a)&(evQ<b)): continue
        fa,fb=f(a),f(b)
        if fa*fb<0: zM.append(brentq(f,a,b,xtol=1e-14))
        ga,gb=g(a),g(b)
        if ga*gb<0: zW.append(brentq(g,a,b,xtol=1e-14))
    # Herglotz check: M' psd at sample points
    herg=min(la.eigvalsh(B.T@np.linalg.matrix_power(la.inv(Q-l*np.eye(n)),2)@B)[0] for l in [-3.,-0.5,-1e-3] if not np.any(abs(evQ-l)<1e-6))
    M0=M(Q,B,0.0); m0=la.eigvalsh(M0)
    cstar=1/abs(m0[0]) if m0[1]>0 and m0[0]<0 else float('nan')
    pen=[float(la.eigvalsh(Q+cc*B@B.T)[0]) for cc in ([cstar*0.99,cstar*1.01] if np.isfinite(cstar) else [1.,10.,100.])]
    r=dict(A=A,case=case,n=n,compression_low=ec[:3].tolist(),zeros_detM=zM[:3],W_low=ew[:3].tolist(),zeros_det_I_plus_JM=zW[:3],
           herglotz_min_eig=float(herg),M0_eig=m0.tolist(),c_star=cstar,lowest_eig_Q_plus_cBBt_at_099_101_cstar=pen)
    out.append(r)
    print(json.dumps(r),flush=True)
json.dump(dict(note='numerical only; Krein formula is exact linear algebra, checked here',rows=out),open('n3_weyl.json','w'),indent=1)

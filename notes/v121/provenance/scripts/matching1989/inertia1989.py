# Two-moment bordered inertia for FULL W and for B|E0 (Galerkin, uncertified NUM; formulas EXACT in finite dim).
#  J = [[-B, c+, c-],[c+^T,0,1],[c-^T,1,0]] (extended Lefschetz form on window + hyperbolic plane U)
#  (a) n_+(J) = 1 + n_-(W),  W = B + c+c-^T + c-c+^T      (Schur on U)
#  (b) n_-(W) = n_-(B) - 1 + n_+(Q+sigma), Q_ab = c_a^T B^{-1} c_b, sigma=[[0,1],[1,0]]   (Schur on -B)
#  (c) n_-(B|E0) = n_-(B) - 2 + n_+(Q)                      (two-constraint Haynsworth)
#  (d) symmetric window: eig(Q+sigma) = {2q_e+1, 2q_o-1}, eig(Q) = {2q_e, 2q_o}, q_e=ch^T B^-1 ch, q_o=sh^T B^-1 sh
import numpy as np, json, runpy
ns=runpy.run_path('mom1975.py')
res={}
for A in [0.6,1.0,2.0]:
  for J in [24,40]:
    ev,par=ns['basis_sine'](A,J); M=ns['matrices'](A,ev)
    B,G,cp,cm=M['B'],M['G'],M['cp'],M['cm']
    Lc=np.linalg.cholesky(G); Li=np.linalg.inv(Lc)
    Bt=Li@B@Li.T; Bt=(Bt+Bt.T)/2; ap=Li@cp; am=Li@cm      # orthonormal coordinates
    inn=lambda X,t=1e-10:(int((np.linalg.eigvalsh(X)>t).sum()),int((np.linalg.eigvalsh(X)<-t).sum()))
    Wt=Bt+np.outer(ap,am)+np.outer(am,ap)
    n=len(ap); X=np.zeros((n+2,n+2)); X[:n,:n]=-Bt; X[:n,n]=X[n,:n]=ap; X[:n,n+1]=X[n+1,:n]=am; X[n,n+1]=X[n+1,n]=1
    Bi=np.linalg.inv(Bt); C=np.vstack([ap,am]).T; Q=C.T@Bi@C; sig=np.array([[0,1.],[1,0]])
    Z=np.linalg.svd(C.T)[2][2:].T; BE0=Z.T@Bt@Z
    ch=(ap+am)/2; sh=(ap-am)/2; qe=ch@Bi@ch; qo=sh@Bi@sh
    nB=inn(Bt)[1]; nW=inn(Wt)[1]; pJ=inn(X)[0]; pQs=inn(Q+sig)[0]; pQ=inn(Q)[0]; nE0=inn(BE0)[1]
    r=dict(nneg_B=nB,nneg_W=nW,npos_J=pJ,npos_Q=pQ,npos_Qsig=pQs,nneg_BE0=nE0,
           check_a=pJ==1+nW, check_b=nW==nB-1+pQs, check_c=nE0==nB-2+pQ,
           eig_Qsig=np.linalg.eigvalsh(Q+sig).tolist(), pred_d=sorted([2*qe+1,2*qo-1]),
           q_e=qe,q_o=qo, minW=float(np.linalg.eigvalsh(Wt)[0]), minBE0=float(np.linalg.eigvalsh(BE0)[0]))
    res[f'A{A}_J{J}']=r; print(A,J,json.dumps(r,default=float),flush=True)
json.dump(res,open('inertia1989.json','w'),indent=1,default=float)

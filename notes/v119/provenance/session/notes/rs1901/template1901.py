"""rs1901 finite-mode template: fix (σ, g, J) on K=R^{2n}; pure quasifree state; check factors, rank, thermal mixing, RS threshold."""
import numpy as np, scipy.linalg as sl
rng=np.random.default_rng(1); n=3; hb=0.7
S=np.block([[np.zeros((n,n)),np.eye(n)],[-np.eye(n),np.zeros((n,n))]])           # σ(x,y)=x^T S y
M=rng.normal(size=(2*n,2*n)); A=(M-M.T)/2; Ssp=sl.expm(S@ (A@S - S@A.T)/4)        # random symplectic? enforce below
# build compatible J via symplectic T: J=T J0 T^{-1}, g=σ(·,J·)
H=rng.normal(size=(2*n,2*n)); H=H+H.T; T=sl.expm(S@H*0.3)                          # exp(S·sym) is symplectic
assert np.allclose(T.T@S@T,S)
J0=-S                                                                              # with x^T S (J0 y): S J0 = -S S = I -> g0=I
J=T@J0@np.linalg.inv(T); g=S@J; g=(g+g.T)/2
print('g>0',np.linalg.eigvalsh(g).min()>0,' J^2=-1',np.allclose(J@J,-np.eye(2*n)),' σ(Jx,Jy)=σ',np.allclose(J.T@S@J,S))
# Field operators Φ(x)=x^T R, [Φ(x),Φ(y)]=iħσ(x,y). Two-point w(x,y)=<Φ(x)Φ(y)> = V(x,y)+ (iħ/2)σ(x,y)
V=(hb/2)*g; w=V+1j*(hb/2)*S
ev=np.linalg.eigvalsh(w); print('pure: w eig min %.2e, rank %d (=n)'%(ev.min(),(ev>1e-10).sum()))
print('  w(x,y)-w(y,x)=iħσ:',np.allclose(w-w.T,1j*hb*S))
# RS threshold: hbar*(V)=2*nu_min, Williamson eigenvalues nu = |eig(i S^{-1}... )| of V relative to σ
nu=np.sort(np.abs(np.linalg.eigvals(np.linalg.inv(S)@V)).real)[::2]; print('  symplectic eigs of V:',np.round(nu,6),' = ħ/2 →saturated')
# thermal mixed: V_beta = (ħ/2) T diag(coth) T^T-type; mixed with g'>=g_J for any J? show two different J give same mixed V allowed
V2=1.5*V; print('mixed V=1.5V: RS ok',np.linalg.eigvalsh(V2+1j*hb/2*S).min()>-1e-12,' full rank',np.linalg.matrix_rank(V2+1j*hb/2*S))
# complex doubling: any Hermitian h>=0 on C^n gives g=Re h, ω=Im h with J=i automatically
B=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); h=B@B.conj().T
gR=np.block([[h.real,-h.imag],[h.imag,h.real]]); print('doubling: realified g=Re h >=0',np.linalg.eigvalsh(gR).min()>0,'-> J=i free, RS = restatement')

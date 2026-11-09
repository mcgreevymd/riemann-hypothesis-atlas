import numpy as np, numpy.linalg as L
rng=np.random.default_rng(1); J2=np.array([[0,1],[1,0.]])
def inert(M): e=L.eigvalsh(M); return (e<-1e-9).sum(),(e>1e-9).sum()
ok=[0,0];N=0;pd_fail=0
for _ in range(20000):
  n=rng.integers(3,9); A=rng.standard_normal((n,n)); Q=A+A.T+rng.normal()*3*np.eye(n)
  C=rng.standard_normal((n,2)); W=Q+C@J2@C.T
  S=C.T@L.solve(Q,C)
  if min(abs(L.eigvalsh(Q)).min(),abs(L.eigvalsh(S)).min(),abs(L.eigvalsh(J2+S)).min())<1e-6: continue
  N+=1
  ok[0]+= inert(W)[0]==inert(Q)[0]+inert(J2+S)[1]-1
  Z=L.svd(C.T)[2][2:].T; ok[1]+= inert(Z.T@W@Z)[0]==inert(Q)[0]+inert(S)[1]-2
print("inertia formulas",ok,"of",N)
# (3) counterexample to S->-J2: W large-positive (not small inverse) on pole plane
n=4;C=np.eye(n)[:,:2];W=np.diag([5,5,1,1.]);Q=W-C@J2@C.T;S=C.T@L.solve(Q,C);print("S",S.round(3),"eig",L.eigvalsh(S).round(3))
# (2) Levinson: PSD singular Toeplitz -> s hits 0, |kappa|=1
t=np.array([1,1,1,1.]) # rank1 PSD
from scipy.linalg import toeplitz;print("rank1 PSD eig",L.eigvalsh(toeplitz(t)).round(6))
a=[1.];s=t[0];k=-t[1]/s;print("kappa1",k,"s1",s*(1-k*k))

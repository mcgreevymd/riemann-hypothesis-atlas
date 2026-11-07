"""ground1896 scratch: (1) Heisenberg ladder: |a(n,n-1)|^2 = beta^2 (n + c) ≥ 0 forces termination (c fixed) — positivity of norms, not labels.
(2) finite matrices cannot satisfy [X,P]=i (trace). (3) Schrödinger double well: bounded below though V''(0)<0; ground-state transform identity.
(4) nonlocal/graph ground-state representation needs J ≥ 0 and h > 0."""
import numpy as np, sympy as sp
from scipy.linalg import eigh
# (1) descending ladder from top state with |a|^2 = n + c: for non-integer c some norm-square goes negative
for c in (0.0, 0.3, -0.7):
    n=np.arange(10,-6,-1); ns=n+c
    print(f'(1) c={c}: first n with negative norm^2 going down:', n[np.argmax(ns<0)] if (ns<0).any() else None,
          ' → consistent only if ladder stops where n+c=0 (c integer, relabel ⇒ c=0)')
# (2) trace obstruction
X=np.random.default_rng(0).normal(size=(5,5)); P=np.random.default_rng(1).normal(size=(5,5))
print('(2) tr[X,P] =',np.trace(X@P-P@X).round(12),' vs tr(i I)= 5i ⇒ no finite CCR; truncated a,a†: [a,a†] =',np.diag((lambda a: a@a.T-a.T@a)(np.diag(np.sqrt(np.arange(1,6)),1))).round(6))
# (3) double well H=-d²+x⁴-4x²
x=np.linspace(-6,6,3001); dx=x[1]-x[0]; V=x**4-4*x**2
H=np.diag(2/dx**2+V)+np.diag(-np.ones(len(x)-1)/dx**2,1)+np.diag(-np.ones(len(x)-1)/dx**2,-1)
E,U=eigh(H,subset_by_index=[0,1]); u0=np.abs(U[:,0])
print(f"(3) V''(0) = -8 (classically unstable at 0); E0 = {E[0]:.6f}, E1 = {E[1]:.6f}; u0>0: {bool((u0[1:-1]>0).all())}")
f=np.exp(-4*(x-0.3)**2)*np.cos(2*x)*(np.abs(x)<2.5)
fd=np.gradient(f,dx); lhs=np.sum(fd**2+(V-E[0])*f**2)*dx
w=f/u0; m=np.abs(x)<4; rhs=np.sum((u0**2*np.gradient(w,dx)**2)[m])*dx
print(f'    ∫|f′|²+(V−E0)|f|² = {lhs:.6f}   ∫u0²|(f/u0)′|² = {rhs:.6f}')
print('    constant shift H+C: E0→E0+C, eigenvectors/commutators/Hessian unchanged (trivial)')
# (4) graph: H = L_J + V, J≥0 symmetric, h>0 with H h = λ h ⇒ <f,Hf> − λ|f|² = ½Σ J_xy h_x h_y (f_x/h_x − f_y/h_y)²
rng=np.random.default_rng(3); N=12; J=np.abs(rng.normal(size=(N,N))); J=(J+J.T)/2; np.fill_diagonal(J,0)
Lj=np.diag(J.sum(1))-J; Vv=np.diag(rng.normal(size=N)*3); Hm=Lj+Vv
lam,Q=eigh(Hm); h=Q[:,0]*np.sign(Q[0,0]); fv=rng.normal(size=N)
lhs=fv@Hm@fv-lam[0]*fv@fv; rhs=0.5*sum(J[i,j]*h[i]*h[j]*(fv[i]/h[i]-fv[j]/h[j])**2 for i in range(N) for j in range(N))
print(f'(4) h>0: {bool((h>0).all())}; <f,Hf>−λ0|f|² = {lhs:.10f}  ground-state rep = {rhs:.10f}')
Jm=J.copy(); Jm[0,1]=Jm[1,0]=-5.0; Hm2=np.diag(Jm.sum(1))-Jm+Vv; l2,Q2=eigh(Hm2)
print('    with one negative jump weight: ground vector sign-definite?',bool((Q2[:,0]>0).all() or (Q2[:,0]<0).all()))
print('(5) E0 has no nonzero f ≥ 0: ∫ f e^{u/2} = 0 with f ≥ 0 ⇒ f = 0 (trivial); positive vacuum must lie outside E0')

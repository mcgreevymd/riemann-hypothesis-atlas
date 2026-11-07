"""geometry1897 scratch: Deninger-type finite toy. V=R^{2n}, ω=cup (standard symplectic), H^2 trace with Θ|H^2 = 1 ⇒ ω(Θx,y)+ω(x,Θy)=ω(x,y).
(a) Θ conformal-symplectic & commuting with a compatible J (g=ω(·,J·)>0) ⇒ Θ+Θ^{*g}=I ⇒ Re spec Θ = 1/2.
(b) ghost Θ=diag(β,1−β) is conformal-symplectic but admits no commuting compatible J; it does admit an invariant INDEFINITE (Krein) form."""
import numpy as np, sympy as sp
rng=np.random.default_rng(0); n=3
Om=np.block([[np.zeros((n,n)),np.eye(n)],[-np.eye(n),np.zeros((n,n))]]); J=Om.copy()   # J0 compatible: g=Om^T? use g=ω(x,Jy)
g=Om@J*-1                                                    # ω(x,Jy)=x^T Om J y, Om J = -I ⇒ g = -Om J = I
B=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H=(B-B.conj().T)/2           # u(n) ∋ skew-Hermitian
A=np.block([[H.real,-H.imag],[H.imag,H.real]])                                    # real form, commutes with J0
Th=0.5*np.eye(2*n)+A
conf=Th.T@Om+Om@Th-Om; comm=Th@J-J@Th
print('(a) conformal-symplectic residual',np.abs(conf).max(),' [Θ,J]',np.abs(comm).max(),' Θ+Θ^T−I',np.abs(Th+Th.T-np.eye(2*n)).max(),
      ' Re eig',np.round(np.linalg.eigvals(Th).real,12))
b,x11,x12,x21,x22=sp.symbols('beta x11 x12 x21 x22'); Tg=sp.diag(b,1-b); O2=sp.Matrix([[0,1],[-1,0]])
print('(b) ghost conformal-symplectic:',sp.simplify(Tg.T*O2+O2*Tg-O2))
X=sp.Matrix([[x11,x12],[x21,x22]]); sol=sp.solve(list(Tg*X-X*Tg),[x12,x21],dict=True)[0]; Xc=X.subs(sol)
print('    commutant of Θ_ghost (β≠1/2):',Xc,'  J^2=-1 solvable?',sp.solve(list(Xc*Xc+sp.eye(2)),[x11,x22]))
Kf=sp.Matrix([[0,1],[1,0]]); print('    invariant Krein form h (signature (1,1)) with Θ^T h + h Θ = h:',sp.simplify(Tg.T*Kf+Kf*Tg-Kf))

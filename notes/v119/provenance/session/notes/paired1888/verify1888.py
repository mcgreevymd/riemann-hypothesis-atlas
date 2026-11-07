"""paired1888: verify L = d^2/du^2 - 1/4 : C_c^inf -> ker P, transported CCR pair, G0 geometry, Kahler triple. Scratch only."""
import sympy as sp, numpy as np
u,v,xi,hb,a=sp.symbols('u v xi hbar a',real=True); s=sp.Symbol('s')
Lop=lambda F: sp.diff(F,u,2)-F/4
print('1 L e^{±u/2}:',[sp.simplify(Lop(sp.exp(k*u/2))) for k in (1,-1)])
print('  L(u e^{u/2}), L(u e^{-u/2}):',[sp.simplify(Lop(u*sp.exp(k*u/2))/sp.exp(k*u/2)) for k in (1,-1)])
print('  symbol: -(xi^2+1/4) at s=1/2+i xi equals s(s-1)?',sp.simplify((-(xi**2)-sp.Rational(1,4))-(s*(s-1)).subs(s,sp.Rational(1,2)+sp.I*xi)))
F=sp.Function('F')(u)
print('2 [L,Q]-2d:',sp.simplify(Lop(u*F)-u*Lop(F)-2*sp.diff(F,u)))
print('  pole kernel killed: L_x cosh((x-y)/2)=',sp.simplify(Lop(sp.cosh((u-v)/2))))
# Fourier side: Q0 = (xi^2+1/4) i d/dxi (xi^2+1/4)^{-1}
H=sp.Function('H')(xi); m=xi**2+sp.Rational(1,4)
print('3 Fourier Q0 on m*H minus m*i*H\':',sp.simplify(sp.I*sp.diff(m*H,xi)-sp.I*sp.diff(m,xi)/m*m*H - m*sp.I*sp.diff(H,xi)))
# ---- numerics on a grid
N=6001; U=np.linspace(-6,6,N); du=U[1]-U[0]
bump=lambda x,c,r: np.where(np.abs(x-c)<r,np.exp(-1/np.maximum(1e-300,1-((x-c)/r)**2)),0.0)
f=bump(U,-1,2)*np.sin(3*U)+0.7*bump(U,1.2,1.5)
B=np.vstack([bump(U,-0.5,1.0),bump(U,0.8,1.0)])
Mo=lambda h: np.array([np.sum(h*np.exp(U/2))*du,np.sum(h*np.exp(-U/2))*du])
c=np.linalg.solve(np.array([Mo(b) for b in B]).T,Mo(f)); f=f-c@B   # f in ker P, supp in [-3,2.7]
print('4 moments f:',Mo(f))
K=-np.exp(-np.abs(U[:,None]-U[None,:])/2)*du; g=K@f
supp=lambda h: (U[np.abs(h)>1e-9*np.abs(h).max()][[0,-1]])
print('  supp f',supp(f),' supp g=L^-1 f',supp(g),' max|g| outside [-3.05,2.75]:',np.abs(g[(U<-3.05)|(U>2.75)]).max())
d2=lambda h: np.gradient(np.gradient(h,du),du)
print('  ||L g - f||/||f|| =',np.linalg.norm(d2(g)-g/4-f)/np.linalg.norm(f))
Q0f=U*f+2*np.gradient(g,du)
print('5 moments Q0 f:',Mo(Q0f),' vs moments Q f:',Mo(U*f))
D=lambda h: -1j*np.gradient(h,du)          # hbar=1
Kinv=lambda h: K@h
Q0=lambda h: U*h+2*np.gradient(Kinv(h),du)
comm=Q0(D(f))-D(Q0(f)); inner=np.abs(U)<4.5
print('  ||[Q0,D]f - i f||/||f|| (interior):',np.linalg.norm((comm-1j*f)[inner])/np.linalg.norm(f[inner]))
# G0 symmetry
f2=np.roll(f,300); f2=f2-np.linalg.solve(np.array([Mo(b) for b in B]).T,Mo(f2))@B
G0=lambda p,q: np.sum(Kinv(p)*Kinv(q))*du; L2=lambda p,q: np.sum(p*q)*du
print('6 G0(Q0f,f2)-G0(f,Q0f2):',G0(Q0(f),f2)-G0(f,Q0(f2)),' scale',abs(G0(Q0(f),f2)))
print('  L2(Q0f,f2)-L2(f,Q0f2):',L2(Q0(f),f2)-L2(f,Q0(f2)),' scale',abs(L2(Q0(f),f2)))
# translation acts on E0 and is G0-isometric (Toeplitz kernel)
# Kahler triple on X+X*: omega(v,w)=<q,p'>-<q',p>, J(q,p)=(-G^-1 p, G q), g=G+G^-1
rng=np.random.default_rng(0); n=5; A=rng.normal(size=(n,n)); Gm=A@A.T+n*np.eye(n); Gi=np.linalg.inv(Gm)
Om=np.block([[np.zeros((n,n)),np.eye(n)],[-np.eye(n),np.zeros((n,n))]])
J=np.block([[np.zeros((n,n)),-Gi],[Gm,np.zeros((n,n))]])
gm=np.block([[Gm,np.zeros((n,n))],[np.zeros((n,n)),Gi]])
print('7 J^2+1:',np.abs(J@J+np.eye(2*n)).max(),' omega(.,J.)-g:',np.abs(Om@J-gm).max(),' J^T Om J - Om:',np.abs(J.T@Om@J-Om).max())
C=gm/2+0.5j*Om          # covariance V+i(hbar/2)Omega with V=g/2, hbar=1
ev=np.linalg.eigvalsh(C); print('  pure Gaussian: eig(V+iΩ/2) min',ev.min(),' #zero',int((np.abs(ev)<1e-10).sum()),'of',2*n)
q=rng.normal(size=n); p=Gm@q
print('  RS saturation on Riesz pair (q,Gq): VarQ*VarP=',(q@Gm@q/2)*(p@Gi@p/2),' (1/4)<q,p>^2=',0.25*(q@p)**2)

"""compat1907: Fourier / scaling / two Poisson boundary functionals. R model (archimedean), psi(x)=e^{-2πixy}."""
import numpy as np, sympy as sp
from scipy.integrate import quad
x,y,a,t,u=sp.symbols('x y a t u',real=True); A=sp.symbols('A',positive=True)
FT=lambda h,var=x,out=y: sp.simplify(sp.integrate(h*sp.exp(-2*sp.pi*sp.I*var*out),(var,-sp.oo,sp.oo)))
f=(1+x+3*x**2)*sp.exp(-sp.pi*(x-sp.Rational(1,3))**2)            # generic Schwartz, f(0)≠0, ∫f≠0
b=lambda h,v=x:(sp.simplify(h.subs(v,0)),sp.simplify(sp.integrate(h,(v,-sp.oo,sp.oo))))
fh=FT(f); b_f=b(f); b_fh=b(fh,y)
print('(1) b(Ff) = swap b(f):',[sp.N(z,12) for z in b_fh],[sp.N(z,12) for z in b_f[::-1]])
Rf=f.subs(x,x/A); b_R=b(Rf)
print('(2) b(R_A f)=diag(1,A)b(f):',sp.simplify(b_R[0]-b_f[0])==0, sp.simplify(b_R[1]-A*b_f[1])==0)
Uf=A**sp.Rational(-1,2)*Rf
lhs=FT(Uf); rhs=(A**sp.Rational(1,2)*fh.subs(y,A*y))            # U_{A^-1} Ff = A^{1/2} (Ff)(A y)
print('(3) F U_A = U_{A^-1} F :',sp.simplify(lhs-rhs)==0)
# (4) smearing Θ_F f = ∫F(t) U_{e^t} f dt ; b(Θ_F f)=diag(ev0,ev1) b(f), ev_s(F)=∫F e^{(s-1/2)t}dt
fn=sp.lambdify(x,f,'numpy'); f0=float(b_f[0]); f1=float(b_f[1])
Fgen=lambda s: np.exp(-(s-0.2)**2)*(1+s)
G=lambda s: np.exp(-s*s/(1-s*s)) if abs(s)<1 else 0.0               # C_c bump
def LG(s,h=1e-3): return (G(s+h)-2*G(s)+G(s-h))/h**2-0.25*G(s)    # F=L G ∈ E0
for name,F,lim in [('generic',Fgen,(-12,12)),('LG (E0)',LG,(-1,1))]:
    ev=[quad(lambda s:F(s)*np.exp((k-0.5)*s),*lim,limit=400)[0] for k in (0,1)]
    th0=quad(lambda s:F(s)*np.exp(-s/2)*fn(0),*lim,limit=400)[0]
    thI=quad(lambda s:F(s)*np.exp(-s/2)*quad(lambda z:fn(z*np.exp(-s)),-40,40,limit=200)[0],*lim,limit=200)[0]
    print('(4)',name,' ev0,ev1=',np.round(ev,8),' b(Θf)=',np.round([th0,thI],8),' diag·b=',np.round([ev[0]*f0,ev[1]*f1],8))
# (5) Fourier conjugation: F Θ_F F^{-1} = Θ_{F(-·)} (linear, no conjugation); adjoint Θ_F* = Θ_{F#}
#     check at a point y0 with F generic real-asym: (FΘ_F f)(y0) vs (Θ_{F(-)} Ff)(y0)
fhn=sp.lambdify(y,fh,'numpy'); y0=0.37
Thf=lambda z: quad(lambda s:Fgen(s)*np.exp(-s/2)*fn(z*np.exp(-s)),-12,12,limit=200)[0]
lhs5=quad(lambda z:Thf(z)*np.cos(2*np.pi*z*y0),-30,30,limit=200)[0]-1j*quad(lambda z:Thf(z)*np.sin(2*np.pi*z*y0),-30,30,limit=200)[0]
rhs5=quad(lambda s:Fgen(-s)*np.exp(-s/2)*complex(fhn(y0*np.exp(-s))).real,-12,12,limit=200)[0]+1j*quad(lambda s:Fgen(-s)*np.exp(-s/2)*complex(fhn(y0*np.exp(-s))).imag,-12,12,limit=200)[0]
print('(5) FΘ_F = Θ_{F(-u)}F at y0:',np.round(lhs5,7),np.round(rhs5,7))
# (6) invariant Hermitian forms on boundary C^2 under D_a=diag(a^-1/2,a^1/2) (a>0) and swap σ
h11,h22=sp.symbols('h11 h22',real=True); z=sp.symbols('z'); H=sp.Matrix([[h11,z],[sp.conjugate(z),h22]])
D=sp.diag(A**sp.Rational(-1,2),A**sp.Rational(1,2)); S=sp.Matrix([[0,1],[1,0]])
eqD=sp.simplify(D.H*H*D-H); eqS=sp.simplify(S.H*H*S-H)
print('(6) D†HD-H =',eqD.tolist(),'  σ†Hσ-H =',eqS.tolist(),' => h11=h22=0, z real: H=z[[0,1],[1,0]], eigen ±z (signature (1,1))')
# (7) density: R model, φ with φ(0)=c0, ∫φ=c1 ; ψ=φ - c0 n_δ - (c1 - c0 δ∫η) w_R
eta=lambda s: np.exp(-s*s); Ieta=np.sqrt(np.pi)                    # η(0)=1
kap=lambda s: s*s*np.exp(-s*s)/(np.sqrt(np.pi)/2)                  # κ(0)=0, ∫κ=1
phi=lambda s: (1+s)*np.exp(-(s-0.5)**2); c0=phi(0); c1=quad(phi,-np.inf,np.inf)[0]
for d,R in [(1e-1,1e1),(1e-2,1e2),(1e-3,1e3),(1e-4,1e4)]:
    al=c1-c0*d*Ieta
    corr=lambda s: c0*eta(s/d)+al*kap(s/R)/R
    psi=lambda s: phi(s)-corr(s)
    n2=np.sqrt(quad(lambda s:corr(s)**2,-50*R,50*R,points=[0],limit=500)[0])
    Ipsi=c1-c0*quad(lambda s:eta(s/d),-20*d,20*d)[0]-al*quad(lambda s:kap(s/R)/R,-20*R,20*R,limit=400)[0]
    print('(7) δ=%g R=%g  ψ(0)=%.1e ∫ψ=%.1e  ‖ψ-φ‖₂=%.4f'%(d,R,psi(0),Ipsi,n2))
# (8) log line E0: far bumps at ±R fix ev0,ev1 with L2-small corrections; fixed window: bounded functionals
k=lambda s: np.exp(-s*s)
ev=lambda F,sk,lo,hi: quad(lambda s:F(s)*np.exp((sk-0.5)*s),lo,hi,limit=400)[0]
Phi=lambda s: np.exp(-(s-0.3)**2)
e0,e1=ev(Phi,0,-30,30),ev(Phi,1,-30,30)
for R in [4,8,12,16]:
    kp=lambda s,R=R:k(s-R); km=lambda s,R=R:k(s+R)
    M=np.array([[ev(kp,0,R-10,R+10),ev(km,0,-R-10,-R+10)],[ev(kp,1,R-10,R+10),ev(km,1,-R-10,-R+10)]])
    cp,cm=np.linalg.solve(M,[e0,e1]); nrm=np.sqrt(np.pi/2)**0.5*np.hypot(cp,cm)
    print('(8) R=%d corr coeffs (%.2e, %.2e)  ‖corr‖₂≈%.2e'%(R,cp,cm,nrm))
for Lw in [2,4,8]:   # window [-Lw,Lw]: dist(Phi, E0∩window) = norm of projection onto span{e^{±u/2}}
    sgrid=np.linspace(-Lw,Lw,20001); w=np.vstack([np.exp(-sgrid/2),np.exp(sgrid/2)]); ds=sgrid[1]-sgrid[0]
    Gm=w@w.T*ds; v=w@Phi(sgrid)*ds; print('(8) window L=%g: dist(Φ,E0_L)=%.4f (>0: E0_L closed codim 2)'%(Lw,np.sqrt(v@np.linalg.solve(Gm,v))))

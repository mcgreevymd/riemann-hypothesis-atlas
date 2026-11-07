"""interactions1890 scratch (not a lemma). Kernel construction copied from num/lemma103_weil.py (prime side; validated there vs zeros).
Checks: (1) Levy form K(r)=K(0)+2∫k_inf(a)(1-cos ra)da; (2) -2aRe<F,T_bF> = a||F-T_bF||^2 - 2a||F||^2 on a grid;
(3) on ker P ∩ window: lambda_min(W) vs tachyonic counterterm M_A = -K(0)+2Σ_{n<=e^A}Λ(n)n^{-1/2}; ratio to L2 and to G0."""
import numpy as np, json
from scipy.special import psi, digamma
from scipy.integrate import quad
from scipy.linalg import toeplitz, eigh, null_space
K=lambda r: np.real(psi(0.25+0.5j*r))-np.log(np.pi)
kinf=lambda a: np.exp(-a/2)/(-np.expm1(-2*a))
K0=K(0.0); print('K(0)=',K0,' closed form psi(1/4)-log pi =',digamma(0.25)-np.log(np.pi))
for r in (0.5,3.0,10.0):
    I=quad(lambda a: kinf(a)*(1-np.cos(r*a)),0,np.inf,limit=500)[0]
    print(f'(1) r={r}: K(r)={K(r):.10f}  K(0)+2∫k(1-cos)={K0+2*I:.10f}')
# (2) grid check of the difference identity
x=np.linspace(-8,8,16001); dx=x[1]-x[0]; F=np.exp(-x**2)*(1+np.sin(2*x)); b=np.log(3); Fb=np.interp(x-b,x,F)
lhs=-2*np.sum(F*Fb)*dx; rhs=np.sum((F-Fb)**2)*dx-2*np.sum(F**2)*dx; print('(2) -2<F,TF>=',lhs,' ||F-TF||^2-2||F||^2=',rhs)
# (3) window matrices
h=0.05; Ls=[0.6,1.0,2.0,3.0,4.0,6.0]; Lmax=max(Ls); Mmax=int(round(Lmax/h))
def B3(z):
    z=np.abs(z); return np.where(z<1,2/3-z**2+z**3/2,np.where(z<2,(2-z)**3/6,0.0))
X=int(np.exp(Lmax))+2; sv=np.ones(X+1,bool); sv[:2]=False
for p in range(2,int(X**.5)+1):
    if sv[p]: sv[p*p::p]=False
ln=[];lam=[]
for p in np.nonzero(sv)[0]:
    q=p
    while q<=X: ln.append(np.log(q)); lam.append(np.log(p)); q*=p
ln=np.array(ln); w=np.array(lam)/np.sqrt(np.exp(ln)); o=np.argsort(ln); ln,w=ln[o],w[o]
ms=np.arange(-Mmax,Mmax+1); d=ms*h
P=np.zeros(len(ms))
for i,dd in enumerate(d):
    for s in (1,-1):
        lo,hi=np.searchsorted(ln,s*dd-2*h),np.searchsorted(ln,s*dd+2*h)
        if hi>lo: P[i]-=np.sum(w[lo:hi]*h*B3((ln[lo:hi]-s*dd)/h))
G=h*B3(ms.astype(float)); c=h*(np.sinh(h/4)/(h/4))**2; POLE=2*c*c*np.cosh(d/2)
R=80/h; dr=min(0.004,np.pi/(Lmax*25)); r=np.arange(0,R,dr)+dr/2
sinc=lambda z: np.where(np.abs(z)<1e-12,1.0,np.sin(z)/np.where(np.abs(z)<1e-12,1,z))
base=h*h*sinc(r*h/2)**4
A=np.array([np.cos(dd*r)@(base*np.real(psi(0.25+0.5j*r)))*dr/np.pi for dd in d])
G0row=np.array([np.cos(dd*r)@(base/(r**2+0.25)**2)*dr/np.pi for dd in d])
Wrow=POLE+A-np.log(np.pi)*G+P
mid=Mmax; T=lambda row,M: toeplitz(row[mid:mid+M])
out={}
for L in Ls:
    M=int(round(L/h))-1; u=-L/2+h*np.arange(1,M+1)
    N=null_space(np.vstack([np.exp(u/2),np.exp(-u/2)]))
    W=N.T@T(Wrow,M)@N; Gm=N.T@T(G,M)@N; G0=N.T@T(G0row,M)@N
    l2=eigh(W,Gm,eigvals_only=True).min(); lg0=eigh(W,G0,eigvals_only=True).min()
    MA=-K0+2*w[ln<L].sum()          # shifts with log n < L overlap the window; tails cancel exactly
    out[L]=dict(lmin_L2=float(l2),lmin_G0=float(lg0),M_A=float(MA),Dirichlet_floor_L2=float(l2+MA),cancel_ratio=float(l2/MA))
    print(f'(3) L={L}: λmin(W/L2)={l2:.3e}  λmin(W/G0)={lg0:.3e}  M_A={MA:.3f}  λmin(Dir)=λmin+M_A={l2+MA:.4f}  ratio λmin/M_A={l2/MA:.2e}')
json.dump({str(k):v for k,v in out.items()},open('check1890.json','w'),indent=1)

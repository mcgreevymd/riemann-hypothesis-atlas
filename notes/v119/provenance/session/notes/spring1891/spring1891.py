"""spring1891 scratch (not a lemma). Exact-constraint Galerkin: F_k = L g_k, L = d²/du² − 1/4, g_k = (1−x²)^6 P_k(x), u = A x/2.
F_k polynomial on window ⇒ moments ∫F e^{±u/2} = 0 exactly (integration by parts), overlaps C(b)=∫F_j(u)F_k(u−b)du exact by Gauss.
W = K(0)G + ∫_0^∞ k(a)[2G − C(a) − C(a)^T]da − Σ_{log n<A} a_n [C(log n)+C(log n)^T]   (pole term ≡ 0 on ker P)
springs E = archDir + Σ a_n[2G − C − C^T],  mass M = −K(0) + 2Σ a_n,  W = E − M G."""
import numpy as np, json, sys
from numpy.polynomial import polynomial as Pl, legendre as Lg
from scipy.special import psi, roots_legendre
from scipy.integrate import quad
from scipy.linalg import eigh
K0=float(np.real(psi(0.25))-np.log(np.pi)); kinf=lambda a: np.exp(-a/2)/(-np.expm1(-2*a))
def primes_pw(X):
    out=[]
    for n in range(2,int(X)+1):
        m=n; p=None
        for q in range(2,n+1):
            if m%q==0: p=q; break
        while m%p==0: m//=p
        if m==1: out.append((n,np.log(p)/np.sqrt(n)))
    return out
def basis(A,K,pw=6,constrained=True):
    s=2/A; Fs=[]
    for k in range(K):
        g=Pl.polymul(Pl.polypow([1,0,-1],pw),Lg.leg2poly(np.eye(K)[k]))   # in x
        F=Pl.polysub(s*s*Pl.polyder(g,2),g/4) if constrained else g
        Fs.append(F)
    return Fs,[Pl.polymul(Pl.polypow([1,0,-1],pw),Lg.leg2poly(np.eye(K)[k])) for k in range(K)]
def overlap(Fs,A,b,nq=80):
    """C_jk(b)=∫F_j(u)F_k(u−b)du, u∈[−A/2+b,A/2]; polynomials in x=2u/A."""
    K=len(Fs)
    if b>=A: return np.zeros((K,K))
    lo,hi=-A/2+b,A/2; t,w=roots_legendre(nq); u=(hi-lo)/2*t+(hi+lo)/2; w=w*(hi-lo)/2
    V1=np.array([Pl.polyval(2*u/A,F) for F in Fs]); V2=np.array([Pl.polyval(2*(u-b)/A,F) for F in Fs])
    return (V1*w)@V2.T
def forms(A,K,pna=None,na=200,constrained=True,pw=6):
    Fs,gs=basis(A,K,pw,constrained); G=overlap(Fs,A,0.0); G0=overlap(gs,A,0.0)
    t,w=roots_legendre(na); a=(t+1)*A/2; w=w*A/2
    D=sum(wi*kinf(ai)*(2*G-overlap(Fs,A,ai)-overlap(Fs,A,ai).T) for ai,wi in zip(a,w))
    D+=2*G*quad(kinf,A,np.inf)[0]
    pw_=[x for x in primes_pw(np.exp(A)) if np.log(x[0])<A] if pna is None else pna
    Pr=[(n,an,overlap(Fs,A,np.log(n))) for n,an in pw_]
    return dict(Fs=Fs,G=G,G0=G0,D=D,Pr=Pr)
def Wmat(f,drop=(),pole=False,A=None):
    W=K0*f['G']+f['D']
    for n,an,C in f['Pr']:
        if n not in drop: W=W-an*(C+C.T)
    if pole:   # pole term 2ab for unconstrained basis
        t,wq=roots_legendre(80); u=A/2*t; wq=wq*A/2
        V=np.array([Pl.polyval(2*u/A,F) for F in f['Fs']]); a=V@(wq*np.exp(-u/2)); b=V@(wq*np.exp(u/2))
        W=W+np.outer(a,b)+np.outer(b,a)
    return W
def gen(W,G):
    mu,V=eigh((W+W.T)/2,(G+G.T)/2); return mu,V
if __name__=='__main__':
    res={}
    # (i) Levy-vs-Fourier check of arch term on F_0, A=1.5
    A=1.5; f=forms(A,4); F=f['Fs'][0]
    t,w=roots_legendre(400); u=A/2*t; w=w*A/2; Fu=Pl.polyval(2*u/A,F)
    r=np.linspace(1e-6,600,120001); Fh=np.array([np.sum(w*Fu*np.cos(rr*u)) for rr in r[::1]]) if False else None
    rr=np.linspace(0,600,60001); Fh=(np.cos(np.outer(rr,u))@(w*Fu))   # F_0 even ⇒ real transform
    four=np.trapezoid((np.real(psi(0.25+0.5j*rr))-np.log(np.pi))*Fh**2,rr)/np.pi
    levy=(K0*f['G']+f['D'])[0,0]; print('(i) arch Fourier vs Levy:',four,levy); res['levy_check']=[float(four),float(levy)]
    # (ii) basis convergence of μmin (Rayleigh–Ritz upper bounds) on ker P
    for A in (0.6,1.0,1.5,2.0,3.0):
        row={}
        for K in (6,10,14,18):
            f=forms(A,K); W=Wmat(f); mu,_=gen(W,f['G']); mu0,_=gen(W,f['G0'])
            M=-K0+2*sum(an for _,an,_ in f['Pr']); row[K]=dict(mu_L2=float(mu[0]),mu_G0=float(mu0[0]),M=float(M),condG=float(np.linalg.cond(f['G'])))
        res[f'A={A}']=row; print('(ii)',A,{k:(f"{v['mu_L2']:.3e}",f"{v['mu_G0']:.3e}",f"M={v['M']:.2f}",f"cond={v['condG']:.1e}") for k,v in row.items()})
    json.dump(res,open('spring1891_conv.json','w'),indent=1)

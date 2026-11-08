# Candidate representers h for the necessary identity  B(h,F) = kappa*C(F) for all window F (centered window width A, zero extension).
# Exact decomposition [HAND-EXACT], v in (-A/2,A/2), d± = A/2 ∓ v:
#   arch part of (B h1)(v), h1=cosh(u/2)1_win:  cosh(v/2)[Jc(d+)+Jc(d-)] - sinh(v/2)[Js(d+)-Js(d-)]
#   Jc(d)=∫_0^d k(1-cosh(a/2))da + ∫_d^∞ k da ,  Js(d)=∫_0^d k sinh(a/2) da ;  indicator response: K(d+)+K(d-), K(d)=∫_d^∞ k.
import numpy as np, json
from scipy.integrate import quad
from mom1975 import K0, k, primes_win, gl, matrices
Kt=lambda d: quad(k,d,np.inf,limit=400)[0]
Jc=lambda d: quad(lambda a:k(a)*(1-np.cosh(a/2)),0,d,limit=400)[0]+Kt(d)
Js=lambda d: quad(lambda a:k(a)*np.sinh(a/2),0,d,limit=400)[0]
def win(A): return lambda u: np.where(np.abs(u)<=A/2,1.0,0.0)
def resp(A,v,which):
    an=primes_win(A); MA=-K0+2*sum(an.values()); I=win(A); dp,dm=A/2-v,A/2+v
    h1=lambda u: np.cosh(np.clip(u,-50,50)/2)*I(u)
    r1=np.cosh(v/2)*(Jc(dp)+Jc(dm))-np.sinh(v/2)*(Js(dp)-Js(dm))+sum(c*(2*h1(v)-h1(v+np.log(n))-h1(v-np.log(n))) for n,c in an.items())-MA*h1(v)
    if which=='h1': return r1
    r0=Kt(dp)+Kt(dm)+sum(c*(2-I(v+np.log(n))-I(v-np.log(n))) for n,c in an.items())-MA
    return r1-np.cosh(A/4)*r0
if __name__=='__main__':
    out={}
    for A in [0.6,1.0]:
        I=win(A)
        H={'h1':lambda u: np.cosh(np.clip(u,-50,50)/2)*I(u),'h2':lambda u:(np.cosh(np.clip(u,-50,50)/2)-np.cosh(A/4))*I(u)}
        for name,hf in H.items():
            for N in [60,120,240]:
                v,w=gl(-A/2,A/2,N); r=np.array([resp(A,x,name) for x in v]); c=np.cosh(v/2)
                kap=(w*r*c).sum()/(w*c*c).sum(); R=r-kap*c; phi=r/c
                out[f'A{A}_{name}_N{N}']=dict(kappa=float(kap),res_rel=float(np.sqrt((w*R*R).sum()/(w*r*r).sum())),res_norm=float(np.sqrt((w*R*R).sum())),
                     phi_center=float(phi[N//2]),phi_edge=float(phi[-1]),edge_dist=float(A/2-v[-1]),B_hh=float((w*r*hf(v)).sum()))
                print(A,name,N,out[f'A{A}_{name}_N{N}'],flush=True)
            v,w=gl(-A/2,A/2,240); r=np.array([resp(A,x,name) for x in v])
            for kk in [0,2]:
                def Ff(u,kk=kk):
                    u=np.asarray(u); t=2*u/A; P=np.polynomial.Polynomial([1,0,-1])**2*np.polynomial.Polynomial([0]*kk+[1])
                    return (P.deriv(2)(t)*(2/A)**2-P(t)/4)*(np.abs(u)<=A/2)
                M=matrices(A,lambda u: np.array([hf(np.asarray(u)),Ff(u)]),nq=400)
                out[f'A{A}_{name}_E0test_k{kk}']=dict(via_response=float((w*r*Ff(v)).sum()),via_matrix=float(M['B'][0,1]),moments=[float(M['cp'][1]),float(M['cm'][1])])
                print(A,name,'E0 k',kk,out[f'A{A}_{name}_E0test_k{kk}'],flush=True)
    json.dump(out,open('match1983.json','w'),indent=1)

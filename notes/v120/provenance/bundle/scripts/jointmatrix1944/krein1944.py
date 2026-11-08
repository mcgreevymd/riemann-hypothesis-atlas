# Joint window certificate via F = L G (exact E0 parametrization) + window-invisible far kernel h.
# W(F) = (1/2pi) ∫ m_A(x)|F^(x)|^2 dx (P=0 on E0), F^ = -(x^2+1/4) G^, supp G ⊂ [0,A]  <=>  F ∈ E0 ∩ L^2[0,A].
# Certificate: h(x)=Σ c_k cos(a_k x), a_k ≥ A  ⇒ ∫ h |G^|^2 = 0 for all G in window. If m_A(x) + h(x)/w(x) ≥ t ∀x,
# w=(x^2+1/4)^2, then W(F) ≥ t ||F||^2 on E0∩window.  (Krein extension: existence of such h ⇔ window positivity.)
import numpy as np, math, json, time, sympy as sp
from scipy.special import psi
from scipy.optimize import linprog
def Lam(n):
    f=sp.factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
def parts(A):
    ns=[n for n in range(2,int(math.exp(A))+2) if Lam(n)>0 and math.log(n)<A]
    an=np.array([Lam(n)/math.sqrt(n) for n in ns]); ln=np.array([math.log(n) for n in ns])
    Om=lambda x: psi(0.25+0.5j*np.asarray(x)).real-math.log(math.pi)
    Pr=lambda x: -2*(an[None,:]*np.cos(np.outer(np.asarray(x),ln))).sum(1) if len(ns) else 0*np.asarray(x)
    return ns,an,Om,Pr
def solve(A,sym,K=160,amax=None,X=60.0,nx=6001,C=50.0):
    amax=amax or A+16.0
    a=np.linspace(A,amax,K); x=np.linspace(0,X,nx); w=(x**2+0.25)**2
    Cm=np.cos(np.outer(x,a))/w[:,None]
    # maximize t : -Cm c + t <= sym(x)
    nv=K+1; cobj=np.zeros(nv); cobj[-1]=-1
    Aub=np.hstack([-Cm,np.ones((nx,1))]); bub=sym(x)
    bounds=[(-C,C)]*K+[(None,None)]
    r=linprog(cobj,A_ub=Aub,b_ub=bub,bounds=bounds,method='highs')
    c=r.x[:K]; t=r.x[-1]
    # validation on 10x finer grid to Xv and analytic tail
    xv=np.linspace(0,4*X,40*nx); wv=(xv**2+0.25)**2
    hv=(np.cos(np.outer(xv,a))@c)/wv; res=sym(xv)+hv-t
    return dict(t=float(t),status=r.status,K=K,amax=amax,X=X,l1=float(np.abs(c).sum()),
                val_min_residual=float(res.min()),val_grid_step=float(xv[1]-xv[0])),c,a
out={}; t0=time.time()
for A in [0.6,1.0,1.6,2.0]:
    ns,an,Om,Pr=parts(A); MA=-(psi(0.25)-math.log(math.pi))+2*an.sum()
    joint=lambda x: Om(x)+Pr(x)
    rj,cj,aj=solve(A,joint)
    # separated: arch alone and prime alone, each certified separately, then added
    ra,_,_=solve(A,Om); rp,_,_=solve(A,Pr) if len(ns) else (dict(t=0.0),None,None)
    out[f'A={A}']=dict(primes=ns,M_A=float(MA),joint=rj,arch_only=ra,prime_only=rp,
        separated_sum_t=float(ra['t']+rp['t']))
    np.save(f'coef_A{A}.npy',np.vstack([aj,cj]))
    print(A,json.dumps(out[f'A={A}']),round(time.time()-t0,1),flush=True)
json.dump(out,open('krein1944.json','w'),indent=1)

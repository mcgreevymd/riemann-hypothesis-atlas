# covariance1956: place-by-place covariance ledger for W on E0 (t1956). Scratch; numerics not certified.
import numpy as np, mpmath as mp, json
from scipy.integrate import quad
A=2.0; pi=np.pi
K0=float(mp.digamma(0.25)-mp.log(mp.pi))
def Lam(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return (np.log(p),p) if m==1 else (0,None)
    return (0,None)
ns=[n for n in range(2,int(np.exp(A))+1) if np.log(n)<A and Lam(n)[0]>0]
a={n:Lam(n)[0]/np.sqrt(n) for n in ns}
MA=-K0+2*sum(a.values())
# trial: F = L G, L=d^2-1/4, G=(u(A-u))^m  (F vanishes to order m-2 at ends; m=6 -> F in C^3, compact)
u=np.linspace(0,A,20001); du=u[1]-u[0]
def trial(kind):
    if kind=='poly':
        m=6; G=(u*(A-u))**m
    else:
        G=np.sin(pi*u/A)**8
    G1=np.gradient(G,du,edge_order=2); G2=np.gradient(G1,du,edge_order=2)
    return G, G2-G/4
def trap(f): return np.trapezoid(f,dx=du)
res={'A':A,'K0':K0,'MA':MA,'a_n':a}
for kind in ['poly','sin8']:
    G,F=trial(kind); nF2=trap(F*F)
    r=lambda s: trap(F*np.interp(u-s,u,F,left=0,right=0)) if s<A else 0.0
    ev_m=trap(F*np.exp(-u/2)); ev_p=trap(F*np.exp(u/2))
    # spring ledger
    Einf=quad(lambda s: np.exp(-s/2)/(1-np.exp(-2*s))*2*(nF2-r(s)),0,A,limit=200)[0]+ quad(lambda s: np.exp(-s/2)/(1-np.exp(-2*s))*2*nF2,A,np.inf)[0]
    Hp=sum(a[n]*2*(nF2-r(np.log(n))) for n in ns)
    W_spring=Einf+Hp-MA*nF2
    # Fourier ledger W=(1/2pi) int m_A |Fhat|^2
    xs=np.linspace(0,120,6001)
    Fh=np.array([trap(F*np.exp(-1j*x*u)) for x in xs])
    mA=np.array([float(mp.re(mp.digamma(0.25+0.5j*x)))-np.log(pi)-2*sum(a[n]*np.cos(x*np.log(n)) for n in ns) for x in xs])
    W_four=2*np.trapezoid(mA*abs(Fh)**2,xs)/(2*pi)
    # covariance ledger: primes = log p (white - AR(1), rho=p^-1/2); arch = OU tower rates 2j+1/2
    primes=sorted({Lam(n)[1] for n in ns})
    Wp={}
    for p in primes:
        l=np.log(p); q=p**-0.5; K=int(A/l)+1
        ar=nF2+2*sum(q**k*r(k*l) for k in range(1,K+1))
        Wp[p]=l*(nF2-ar)
    J=4000; lam=2*np.arange(J)+0.5
    F1=np.gradient(F,du,edge_order=2); nF1=trap(F1*F1)
    ou=np.array([2*quad(lambda s: np.exp(-L*s)*r(s),0,A,limit=400)[0] if j<150 else 2*nF2/L-2*nF1/L**3 for j,L in enumerate(lam)])
    ou_exact150=ou[149]; ou_asym150=2*nF2/lam[149]-2*nF1/lam[149]**3
    # (for large lambda, OU response -> (2/lambda) F locally; tail error O(1/lambda^3))
    W_arch=(-np.euler_gamma-np.log(pi))*nF2+np.sum(nF2/(np.arange(J)+1)-ou)
    tail=nF2*(np.log(J+0.25)-np.log(J+1))*-1  # sum_{j>=J}(1/(j+1)-1/(j+1/4)) approx
    W_arch+= -nF2*(sum(1/(j+0.25)-1/(j+1) for j in range(J,J+200000)))
    W_cov=W_arch+sum(Wp.values())
    # E0 localisation: OU_{1/2} response outside window (should equal -G inside, 0 outside)
    U=np.linspace(-3,A+3,1201)
    resp=np.array([trap(F*np.exp(-abs(x-u)/2)) for x in U])
    inside=(U>=0)&(U<=A)
    ou_out=np.max(abs(resp[~inside])); ou_in_err=np.max(abs(resp[inside]+np.interp(U[inside],u,G)))/np.max(abs(G))
    # prime AR leak to the right of window and its aliasing prediction (Poisson summation)
    leak={}
    for p in primes:
        l=np.log(p); q=p**-0.5
        X=np.linspace(A+0.01,A+3,300)
        direct=np.array([sum(q**k*np.interp(x-k*l,u,F,left=0,right=0) for k in range(1,60)) for x in X])
        gh=lambda xi: trap(np.exp(u/2)*F*np.exp(-1j*xi*u))
        ms=np.array([m for m in range(-400,401) if m!=0]); gv=np.array([gh(2*pi*m/l) for m in ms])
        pred=np.array([ (np.exp(-x/2)/l*np.sum(gv*np.exp(2j*pi*ms*x/l))).real for x in X])
        leak[p]={'max_leak/maxF':float(np.max(abs(direct))/np.max(abs(F))),'alias_formula_err':float(np.max(abs(direct-pred))/np.max(abs(direct))),
                 'm0_term_ev+':float(gh(0).real)}
    res[kind]=dict(normF2=nF2,ev_minus=ev_m,ev_plus=ev_p,W_spring=W_spring,W_fourier=W_four,W_cov=W_cov,
        ratio_W=W_spring/nF2,ou_check_j149=(ou_exact150,ou_asym150),Einf=Einf,Hp=Hp,MA_norm=MA*nF2,W_arch_cov=W_arch,W_prime_cov=Wp,
        arch_check=Einf+K0*nF2, OU_half_out=ou_out/np.max(abs(F)),OU_half_in_relerr=ou_in_err,AR_leak=leak)
# exact local-mean identities
EL_inf=float(mp.quad(lambda x: mp.log(x)*x**(-0.5)*mp.e**(-mp.pi*x*x),[0,1,mp.inf])/mp.quad(lambda x: x**(-0.5)*mp.e**(-mp.pi*x*x),[0,1,mp.inf]))
res['E_inf_log|x|']=EL_inf; res['K0/2']=K0/2
cap={}
for p in [2,3,5,7]:
    l=np.log(p); q=p**-0.5; kmax=int(np.floor((A-1e-12)/l))
    capmean=sum((1-q)*q**k*min(k,kmax)*l for k in range(0,400))
    cap[p]=(capmean, sum(a[n] for n in ns if Lam(n)[1]==p))
res['capped_mean_vs_sum_a']=cap
# per-prime symbol range of log p(1-Poisson_q): min=-2 log p/(sqrt p-1) (= -2 E[L_p] uncapped)
res['prime_symbol_min']={p:(-2*np.log(p)/(np.sqrt(p)-1)) for p in [2,3,5,7]}
json.dump(res,open('cov1956.json','w'),indent=1,default=float)
print(json.dumps(res,indent=1,default=float))

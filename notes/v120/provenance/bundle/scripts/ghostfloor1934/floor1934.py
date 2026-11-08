# Kinetic floor on E0 windows: kappa = inf H/||F||^2, H = E_inf + sum_{n<e^A} a_n||F-T_{log n}F||^2; compare M_A.
import numpy as np, mpmath as mp, json, scipy.linalg as sl
from scipy.special import digamma
def vm(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
psi14=float(mp.digamma(0.25)); K0=psi14-np.log(np.pi)
xs=np.linspace(-600,600,240001); dx=xs[1]-xs[0]
fsym=np.array([float(mp.re(mp.digamma(0.25+0.5j*x))) for x in np.linspace(0,600,3001)])-psi14
fx=np.interp(np.abs(xs),np.linspace(0,600,3001),fsym)
out={}
for A in [1.0,1.6,2.0,3.0]:
    J=36; u=np.linspace(0,A,3001); du=u[1]-u[0]
    B=np.array([np.sin((j+1)*np.pi*u/A) for j in range(J)])
    # Fourier transforms analytic: FT of sin(k u) on [0,A]
    def ft(k):
        x=xs; e=np.exp(-1j*x*A)
        with np.errstate(divide='ignore',invalid='ignore'):
            v=0.5j*((e*np.exp(1j*k*A)-1)/(1j*(k-x))*0+0)  # placeholder
        # direct: int_0^A sin(ku)e^{-ixu}du = [k - e^{-ixA}(k cos kA + i x sin kA)]/(k^2-x^2)
        num=k-np.exp(-1j*x*A)*(k*np.cos(k*A)+1j*x*np.sin(k*A)); den=k*k-x*x
        r=np.where(np.abs(den)<1e-9,np.nan,num/np.where(np.abs(den)<1e-9,1,den))
        bad=np.isnan(r); r[bad]=np.interp(x[bad],x[~bad],r[~bad].real)+1j*np.interp(x[bad],x[~bad],r[~bad].imag)
        return r
    Fh=np.array([ft((j+1)*np.pi/A) for j in range(J)])
    G=B@B.T*du
    Einf=np.real((Fh*fx)@Fh.conj().T)*dx/(2*np.pi)
    ns=[n for n in range(2,int(np.exp(A))+1) if vm(n)>0 and np.log(n)<A]
    an={n:vm(n)/np.sqrt(n) for n in ns}
    def shiftG(s):
        j=int(round(s/du)); S=np.zeros((J,J))
        if j<len(u): S=B[:,j:]@B[:,:len(u)-j].T*du
        return 0.5*(S+S.T)
    Ep=sum(an[n]*2*(G-shiftG(np.log(n))) for n in ns)
    M=-K0+2*sum(an.values())
    ev=np.array([[np.sum(b*np.exp(-u/2))*du for b in B],[np.sum(b*np.exp(u/2))*du for b in B]])
    Z=sl.null_space(ev)
    gen=lambda H,Q: float(sl.eigh(Q.T@H@Q,Q.T@G@Q,eigvals_only=True)[0])
    I=np.eye(J)
    r=dict(M_A=M,K0=K0,primes=ns,
      floor_Einf_full=gen(Einf,I),floor_Einf_E0=gen(Einf,Z),
      floor_Ep_full=gen(Ep,I),floor_Ep_E0=gen(Ep,Z),
      floor_joint_full=gen(Einf+Ep,I),floor_joint_E0=gen(Einf+Ep,Z))
    r['sum_of_separate_floors_E0']=r['floor_Einf_E0']+r['floor_Ep_E0']
    r['shortfall_separate']=M-r['sum_of_separate_floors_E0']
    r['joint_minus_M_E0(=Ritz lam_min W)']=r['floor_joint_E0']-M
    # rigorous-type uncertainty cushion: E_inf >= f(X)(1-lambda0(A X/2)) ||F||^2  (Landau-Pollak/Slepian, any F supported in length A)
    vv=np.linspace(0,A,801); dv=vv[1]-vv[0]; best=(0,0)
    for X in np.linspace(0.5,200,400):
        D=vv[:,None]-vv[None,:]; Kb=np.where(D==0,X/np.pi,np.sin(X*D)/(np.pi*np.where(D==0,1,D)))*dv
        lam0=np.linalg.eigvalsh(Kb)[-1]; fX=float(np.interp(X,np.linspace(0,600,3001),fsym))
        if fX*(1-lam0)>best[0]: best=(fX*(1-lam0),X)
    r['slepian_cushion_Einf']=dict(value=best[0],X=best[1])
    out[f'A={A}']=r; print(A,json.dumps(r),flush=True)
json.dump(out,open('floor1934.json','w'),indent=1)

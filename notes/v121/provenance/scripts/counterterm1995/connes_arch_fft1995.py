# Refined (FFT) version of connes_arch1995.py; a=-1/2 is the symmetric map h(x)=|x|^{-1/2}G(log|x|).
import numpy as np, mpmath as mp, json
from scipy.integrate import quad
gam=float(mp.euler); K0=float(mp.digamma(0.25)-mp.log(mp.pi)); C=gam+float(mp.log(2*mp.pi))
out={}
for s2 in (0.5,0.2):
    G=lambda u: np.exp(-u*u/s2)
    K=lambda u: 2*np.exp(-u/2)/(-np.expm1(-2*u))
    Winf=K0+quad(lambda u: K(u)*(1-G(u)),0,80,limit=500)[0]
    N=2**23; dl=5e-5; lam=(np.arange(N)-N//2)*dl
    y=lam+1.0; y[y==0]=1e-300
    x=1/y; hx=np.abs(x)**-0.5*np.exp(-np.log(np.abs(x))**2/s2); gv=hx/np.abs(y); gv[~np.isfinite(gv)]=0
    gh=np.fft.fftshift(np.fft.fft(np.fft.ifftshift(gv)))*dl; u=np.fft.fftshift(np.fft.fftfreq(N,dl))
    du=u[1]-u[0]; gh=gh.real; i0=N//2
    w=np.log(np.abs(u)); w[i0]=0
    F=-np.sum(gh*w)*du - gh[i0]*du*(np.log(du/2)-1)
    # Parseval/distribution form (Weil-Connes constant C=gamma+log 2pi) computed by direct quadrature in lambda
    gf=lambda l: (abs(1/(l+1))**-0.5*np.exp(-np.log(abs(1/(l+1)))**2/s2))/abs(l+1)
    pv=0.5*(quad(lambda l:(gf(l)+gf(-l)-2)/l,0,1,limit=400,points=[0.5])[0]+quad(lambda l:(gf(l)+gf(-l))/l,1,400,limit=800)[0])
    out[f's2={s2}']=dict(F_fft=float(F),Parseval_form=float(pv+C),minus_Winf=float(-Winf),
        F_plus_Winf=float(F+Winf),pv_plus_C_plus_Winf=float(pv+C+Winf),pv_plus_Winf_if_C_omitted=float(pv+Winf))
json.dump(out,open('connes_arch_fft1995.json','w'),indent=1);print(json.dumps(out,indent=1))

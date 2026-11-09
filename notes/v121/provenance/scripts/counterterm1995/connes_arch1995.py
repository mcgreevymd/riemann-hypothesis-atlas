# Independent check of Connes (Selecta 1999, Thm V.3) archimedean cutoff-trace finite part vs ledger W_infinity.
# Trace(R_L U(h)) = int_{|u|<=L^2} ghat(u)(2 log L - log|u|) du ; finite part F = -int ghat(u) log|u| du,
# g(l) = h((l+1)^{-1}) |l+1|^{-1}, ghat(u)=int g(l) e^{-2 pi i l u} dl (alpha=e^{-2pi i x}, selfdual dx).
import numpy as np, mpmath as mp, json
from scipy.integrate import quad
G=lambda u: np.exp(-u*u/0.5)          # even test function on log scale (ledger g)
gam=float(mp.euler); K0=float(mp.digamma(0.25)-mp.log(mp.pi))
def Winf(Gf):  # ledger archimedean: K0 G(0) + int_0^inf K(u)(G(0)-G(u)) du, K = 2e^{-u/2}/(1-e^{-2u})
    K=lambda u: 2*np.exp(-u/2)/(-np.expm1(-2*u))
    val,_=quad(lambda u: K(u)*(Gf(0)-Gf(u)),0,60,limit=400)
    return K0*Gf(0)+val
res={'K0':K0,'W_inf(G)':Winf(G)}
for a in (0.5,-0.5):
    h=lambda x: abs(x)**a*G(np.log(abs(x)))
    def g(l):
        y=l+1.0
        if y==0: return 0.0
        return h(1.0/y)/abs(y)
    # ghat via direct quadrature on fine grid (g smooth, rapidly decaying)
    lam=np.linspace(-40,40,400001); dl=lam[1]-lam[0]
    gv=np.array([g(l) for l in lam])
    us=np.linspace(-60,60,24001); du=us[1]-us[0]
    # FFT-free: compute ghat by chunked matrix product (cos/sin)
    gh=np.empty_like(us)
    for i in range(0,len(us),500):
        U=us[i:i+500][:,None]
        gh[i:i+500]=(np.cos(2*np.pi*U*lam[None,:])@gv)*dl   # g real; imaginary part integrates against odd? keep real part (log|u| even)
    w=np.log(np.abs(us)+1e-300); w[np.abs(us)<1e-12]=0
    # integrable log singularity at 0: refine by subtracting ghat(0) near 0
    F=-np.sum(gh*w)*du
    # correction for log singularity at u=0 (trapezoid misses int_{-du/2}^{du/2} log|u|): add -gh(0)*du*(log(du/2)-1)
    i0=np.argmin(np.abs(us)); F+= -gh[i0]*du*(np.log(du/2)-1)
    res[f'a={a}: h(1)=g(0)']=float(gv[np.argmin(np.abs(lam))]); res[f'a={a}: int ghat']=float(np.sum(gh)*du)
    res[f'a={a}: Connes finite part F=-int ghat log|u|']=float(F)
    res[f'a={a}: F + W_inf(G)']=float(F+Winf(G))
    res[f'a={a}: F + W_inf(G) - (gamma+log2pi)G(0) [if constant omitted]']=float(F+Winf(G))
json.dump(res,open('connes_arch1995.json','w'),indent=1); print(json.dumps(res,indent=1))

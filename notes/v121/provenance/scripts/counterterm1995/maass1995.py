# SL2(Z) cusp: continuous (Maass-Selberg / scattering) and parabolic terms of the Selberg trace formula,
# degree/Laplacian split, diagonal constants, sigma-shift identity, and scheme cocycle.  mpmath, uncertified.
import mpmath as mp, json
mp.mp.dps=30
xi=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
logphi=lambda s: mp.log(xi(2*s-1))-mp.log(xi(2*s))
out={}
# (i) -phi'/phi(1/2+it) = -2 log pi + 2 Re psi(1/2+it) + 4 Re zeta'/zeta(1+2it)
chk=[]
for t in (0.3,1.7,5.0,11.0):
    s=mp.mpf(1)/2+1j*t
    lhs=-mp.diff(logphi,s)
    rhs=-2*mp.log(mp.pi)+2*mp.re(mp.digamma(s))+4*mp.re(mp.zeta(1+2j*t,derivative=1)/mp.zeta(1+2j*t))
    chk.append([t,float(mp.re(lhs)),float(mp.im(lhs)),float(abs(lhs-rhs))])
out['(i) -phi\'/phi expansion [t, Re, Im, |err|]']=chk
s=mp.mpf(1)/2; out['-phi\'/phi(1/2) limit']=[float(mp.re(-mp.diff(logphi,s+mp.mpf('1e-8')))), float(2*(mp.euler-mp.log(4*mp.pi)))]
out['phi(1/2+1e-10)']=float(mp.re(xi(2*(s+mp.mpf('1e-10'))-1)/xi(2*(s+mp.mpf('1e-10')))))
# (ii) continuous term (1/4pi) int h(r)(-phi'/phi)(1/2+ir) dr vs local degree form, g(x)=exp(-x^2/s2), h(r)=int g e^{irx}
def g(x,s2): return mp.e**(-x*x/s2)
def h(r,s2): return mp.sqrt(mp.pi*s2)*mp.e**(-s2*r*r/4)
def cont_spec(s2):
    f=lambda r: h(r,s2)*mp.re(-mp.diff(logphi,mp.mpf(1)/2+1j*r))
    return 2*mp.quad(f,[0,2,5,10,20,40])/(4*mp.pi)
def primes_sum(s2,w):  # sum Lambda(n) w(n) g(2 log n)
    S=0
    for n in range(2,5000):
        f=mp.factor if False else None
        # von Mangoldt
        m=n;p=None
        for q in range(2,int(n**0.5)+1):
            if m%q==0: p=q;break
        if p is None: p=n
        while m%p==0: m//=p
        if m!=1: continue
        S+=mp.log(p)*w(n)*g(2*mp.log(n),s2)
    return S
def cont_local(s2):
    lap=mp.quad(lambda x: mp.e**(-x/2)/(-mp.expm1(-x))*(1-g(x,s2)),[0,1,10,80])
    diag=mp.digamma(0.5)-mp.log(mp.pi)
    return diag+lap-2*primes_sum(s2,lambda n:1/mp.mpf(n)), diag
def parab(s2):  # Iwaniec/Hejhal: P(h) = -g(0)log2 - (1/2pi) int psi(1+ir)h(r)dr + h(0)/4
    direct=-mp.log(2)-2*mp.quad(lambda r: mp.re(mp.digamma(1+1j*r))*h(r,s2),[0,2,5,10,20,40])/(2*mp.pi)+h(0,s2)/4
    lap=mp.quad(lambda x: mp.e**(-x)/(-mp.expm1(-x))*(1-g(x,s2)),[0,1,10,80])
    degree=(mp.euler-mp.log(2))-lap+h(0,s2)/4
    return direct,degree
for s2 in (0.5,2.0):
    cs=cont_spec(s2); cl,d=cont_local(s2); pd,pg=parab(s2)
    # combined kernel check: k_par+k_cont = 1/(e^{x/2}-1)
    comb=(pg-h(0,s2)/4)-(cl+2*primes_sum(s2,lambda n:1/mp.mpf(n)))
    comb_form=(2*mp.euler+mp.log(2*mp.pi))-mp.quad(lambda x:(1-g(x,s2))/mp.expm1(x/2),[0,1,10,160])
    out[f'(ii) s2={s2}']=dict(cont_spectral=float(cs),cont_local=float(cl),err=float(abs(cs-cl)),
        parab_direct=float(pd),parab_degree=float(pg),parab_err=float(abs(pd-pg)),
        PminusCont_nonprime=float(comb),closed_form=float(comb_form),comb_err=float(abs(comb-comb_form)))
# (v) constants
g_=mp.euler
out['constants']=dict(
 K0=float(mp.digamma(0.25)-mp.log(mp.pi)), minusK0_closed=float(g_+mp.log(8*mp.pi)+mp.pi/2),
 FP_H_int_K=float(mp.limit(lambda e: mp.quad(lambda u:2*mp.e**(-u/2)/(-mp.expm1(-2*u)),[e,1,80])+mp.log(e),0)),
 pi_over2_plus_2log2=float(mp.pi/2+2*mp.log(2)),
 FP_H_int_Kcont_x=float(mp.limit(lambda e: mp.quad(lambda x:mp.e**(-x/2)/(-mp.expm1(-x)),[e,1,80])+mp.log(e),0)),
 log2=float(mp.log(2)),
 alpha_const=float(g_+mp.log(2*mp.pi)),
 cont_diag=float(mp.digamma(0.5)-mp.log(mp.pi)), parab_diag=float(g_-mp.log(2)),
 PminusCont_diag=float(2*g_+mp.log(2*mp.pi)),
 K0_minus_contdiag=float(mp.digamma(0.25)-mp.digamma(0.5)), minus_pi2_minus_log2=float(-mp.pi/2-mp.log(2)))
json.dump(out,open('maass1995.json','w'),indent=1);print(json.dumps(out,indent=1))

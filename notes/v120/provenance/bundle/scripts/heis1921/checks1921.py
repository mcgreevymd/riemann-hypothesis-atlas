import sympy as sp, numpy as np, mpmath as mp, json, sys
sys.path.insert(0,'/workspace/taa/sign1918'); from screened import Window
out={}
# T1a group law
x1,p1,z1,x2,p2,z2=sp.symbols('x1 p1 z1 x2 p2 z2')
M=lambda x,p,z: sp.Matrix([[1,x,z],[0,1,p],[0,0,1]])
prod=M(x1,p1,z1)*M(x2,p2,z2); out['upper_tri_z']=str(sp.expand(prod[0,2]))
t1,t2=z1-x1*p1/2, z2-x2*p2/2; t12=prod[0,2]-(x1+x2)*(p1+p2)/2
out['sym_cocycle_resid']=str(sp.simplify(t12-(t1+t2+sp.Rational(1,2)*(x1*p2-p1*x2))))
# T1b inverted oscillator: P^2-X^2 = YZ+ZY, Y=(X+P)/sqrt2, Z=(P-X)/sqrt2 (P=-i d/dx) on test f
X_,f=sp.symbols('x'),sp.Function('f')(sp.Symbol('x'))
x=sp.Symbol('x'); P=lambda g:-sp.I*sp.diff(g,x); X=lambda g:x*g
Y=lambda g:(X(g)+P(g))/sp.sqrt(2); Z=lambda g:(P(g)-X(g))/sp.sqrt(2)
out['invosc_resid']=str(sp.simplify(P(P(f))-X(X(f))-(Y(Z(f))+Z(Y(f)))))
out['YZ_comm']=str(sp.simplify(Y(Z(f))-Z(Y(f))))   # = i f  (CCR, same rep)
# T2 E0 stability, F=LG, G=(1-(2u/A)^2)^8 on [-1,1]
Wd=Window(2.0,8001); u=Wd.u; s=u; G=(1-s**2)**8
Gpp=np.gradient(np.gradient(G,u),u); F=Gpp-G/4
ev=lambda H,k: np.trapezoid(H*np.exp(k*u),u)    # k=-1/2 -> ev0 , +1/2 -> ev1
rows={}
rows['F']=[ev(F,-.5),ev(F,.5)]
rows['reflect']=[ev(F[::-1],-.5),ev(F[::-1],.5)]
for xi in [0.5,2.0]:
    Fm=np.exp(1j*xi*u)*F; pred=[(-xi**2+1j*xi*(-1)*(-1))*0,0]
    num=[ev(Fm,-.5),ev(Fm,.5)]
    predf=[(( -0.5+1j*xi)**2-0.25)*ev(G,-0.5+1j*xi),((0.5+1j*xi)**2-0.25)*ev(G,0.5+1j*xi)]
    rows[f'mod_xi={xi}']=dict(num=[str(complex(z)) for z in num],formula=[str(complex(z)) for z in predf])
lam=1.3; Fd=np.interp(lam*u,u,F,left=0,right=0)   # dilation u->lam u
rows['dilate_1.3']=[ev(Fd,-.5),ev(Fd,.5)]
rows['translate_c=0.4: ev ratios (exact e^{-+c/2})']='analytic'
out['E0']={k:(v if isinstance(v,(dict,str)) else [float(np.real(z)) for z in v]) for k,v in rows.items()}
# T3 local vacua
mp.mp.dps=25; p=3; th=0.7
lhs=mp.nsum(lambda k: p**(-abs(k)/2.)*mp.cos(k*th),[-mp.inf,mp.inf]); rhs=(1-1/mp.mpf(p))/abs(1-p**-0.5*mp.e**(1j*th))**2
out['padic_vacuum']=[float(lhs),float(rhs)]
xx=1.7; Lp=lambda sig: abs(1/(1-mp.mpf(p)**(-(sig+1j*xx))))
dl=2*mp.diff(lambda sg: mp.log(Lp(sg)),0.5); ser=-2*mp.nsum(lambda k: mp.log(p)*p**(-k/2.)*mp.cos(k*xx*mp.log(p)),[1,mp.inf])
out['padic_score']=[float(dl),float(ser)]
gx=1.3; ft=mp.quad(lambda t:(2*mp.cosh(t))**-0.5*mp.cos(gx*t),[-mp.inf,0,mp.inf]); out['gauss_vacuum']=[float(ft),float(abs(mp.gamma(0.25+1j*gx/2))**2/(2*mp.sqrt(mp.pi)))]
GR=lambda sg: abs(mp.pi**(-(sg+1j*gx)/2)*mp.gamma((sg+1j*gx)/2))
out['gauss_score']=[float(2*mp.diff(lambda sg: mp.log(GR(sg)),0.5)),float(mp.re(mp.digamma(0.25+1j*gx/2))-mp.log(mp.pi))]
# T4 exact E0 identity W = (1/2pi) int |Fhat|^2 m_N, m_N = 2 d_sigma log|Gamma_R Z_N| at 1/2, N=7 (A=2)
from screened import vonM
def mN(x): return float(mp.re(mp.digamma(0.25+1j*x/2))-mp.log(mp.pi))-2*sum(vonM(n)/np.sqrt(n)*np.cos(x*np.log(n)) for n in range(2,8))
Fa=(np.polynomial.polynomial.polyval(s,np.polynomial.polynomial.polyder(np.polynomial.polynomial.polypow([1,0,-1],8),2))-G/4)
xs=np.linspace(0,150,3001); Fh=np.array([np.trapezoid(Fa*np.exp(-1j*q*u),u) for q in xs])
mult=2*np.trapezoid(np.abs(Fh)**2*np.array([mN(q) for q in xs]),xs)/(2*np.pi)
out['T4']=dict(spring=float(Wd.form(Fa,Fa,0.0)),vacuum_score=float(mult),min_mN=float(min(mN(q) for q in xs)))
# T5 Hecke degree: |P^1(Z/p^2)| = index of Gamma0(p^2) = p(p+1)
def p1count(m):
    import math
    pts=set()
    for a in range(m):
        for b in range(m):
            if math.gcd(math.gcd(a,b),m)!=1: continue
            # normalize by units
            best=min(((a*l)%m,(b*l)%m) for l in range(1,m) if math.gcd(l,m)==1); pts.add(best)
    return len(pts)
out['T5']={p:dict(deg=p1count(p*p),p_p1=p*(p+1),a_p=float(np.log(p)/np.sqrt(p))) for p in [2,3,5]}
json.dump(out,open('checks1921.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))

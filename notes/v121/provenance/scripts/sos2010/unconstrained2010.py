# Check: for ANY F supported in window (no E0 constraint), with E(x)=psi_Cheb(x)-x,
#  W(F) = P(F) + K0||F||^2 + ∫k_inf||F-T_aF||^2 - 2Σ_{log n<A} a_n <F,T_{log n}F>
#       = K5(0)||F||^2 + ∫k5||F-T_aF||^2 - 2∫_{[1,e^A]} x^{-1/2} <F,T_{log x}F> dE(x)
import sympy as sp, mpmath as mp, json
mp.mp.dps=30; x,b=sp.symbols('x b'); out={}
for A,Fx in [(2,(1-x**2)**4),(2,(1-x**2)**4*(1+x+x**3)),(3,(1-x**2)**5*(2-x))]:
    s=sp.Rational(A,2); Fp=sp.expand(Fx)
    c=sp.Poly(sp.expand(s*sp.integrate(sp.expand(Fp*Fp.subs(x,x-b)),(x,b-1,1))),b)  # <F,T_{s b}F>
    cf=lambda bb: mp.mpf(c.eval(sp.Rational(mp.nstr(bb,40)))) if bb<2 else mp.mpf(0)
    n2=cf(0); Am=mp.mpf(A)
    Cp=mp.mpf(sp.N(s*sp.integrate(Fp*sp.exp(s*x/2),(x,-1,1)),40)); Cm=mp.mpf(sp.N(s*sp.integrate(Fp*sp.exp(-s*x/2),(x,-1,1)),40))
    P=2*Cp*Cm
    kinf=lambda a: mp.e**(-a/2)/(1-mp.e**(-2*a)); k5=lambda a: mp.e**(-2.5*a)/(1-mp.e**(-2*a))
    jump=lambda k: mp.quad(lambda a: k(a)*(2*n2-2*cf(a/s)),[0,Am/4,Am/2,Am])+2*n2*mp.quad(k,[Am,mp.inf])
    K0=mp.digamma(0.25)-mp.log(mp.pi); K5=mp.digamma(1.25)-mp.log(mp.pi)
    pp=[(n,mp.log(list(sp.factorint(n))[0])/mp.sqrt(n)) for n in range(2,int(mp.e**Am)+2) if len(sp.factorint(n))==1 and mp.log(n)<Am]
    lhs=P+K0*n2+jump(kinf)-2*sum(w*cf(mp.log(n)/s) for n,w in pp)
    # dE = dpsi - dx on [1,X]: prime part minus smooth part
    smooth=mp.quad(lambda xx: xx**-0.5*cf(mp.log(xx)/s),[1,mp.e**(Am/2),mp.e**Am])
    rhs=K5*n2+jump(k5)-2*(sum(w*cf(mp.log(n)/s) for n,w in pp)-smooth)
    out[f'A={A},F={Fx}']=dict(lhs=float(lhs),rhs=float(rhs),diff=float(lhs-rhs),P=float(P))
json.dump(out,open('unconstrained2010.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))

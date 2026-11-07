"""deform1894 scratch. (A) convolution-unit deformation with polar normalization; trace-pairing laws. (C) F_q Frobenius-graph identity."""
import sympy as sp, numpy as np
u,s=sp.symbols('u s'); eps=sp.Symbol('epsilon')
ev=lambda F,s_: sp.integrate(F*sp.exp((s_-sp.Rational(1,2))*u),(u,-sp.oo,sp.oo))
F=sp.exp(-u**2)*(1+u+u**3)
lhs=ev(sp.diff(F,u,2)-F/4,s); rhs=s*(s-1)*ev(F,s)
print('A1 ev_s(L F) - s(s-1) ev_s(F) =',sp.simplify(lhs-rhs))
print('A2 polar chars of translate delta_a: ev_0, ev_1 =',[sp.exp((k-sp.Rational(1,2))*sp.Symbol('a')) for k in (0,1)],'(boost on E/E0)')
# A3 numeric: ev multiplicative under convolution; sharp swaps ev_0/ev_1; ideal property
x=np.linspace(-12,12,4801); dx=x[1]-x[0]
f=np.exp(-(x-1)**2)*(1+np.sin(3*x)); g=np.exp(-2*(x+0.5)**2)*(x**2-0.3)
conv=np.convolve(f,g,mode='same')*dx
evn=lambda h,sv: np.sum(h*np.exp((sv-0.5)*x))*dx
for sv in (0,1,0.3):
    print(f'A3 s={sv}: ev(f*g)={evn(conv,sv):.8f}  ev(f)ev(g)={evn(f,sv)*evn(g,sv):.8f}')
print('A4 sharp: ev_0(f(-u))=',evn(f[::-1],0),' ev_1(f)=',evn(f,1))
# A5 dual numbers: (δ+εF)(δ+εG)=δ+ε(F+G) mod ε²; ev(δ+εF)=1+ε ev(F) ⇒ polar normalized ⇔ F∈E0
d0,F1,G1=sp.symbols('delta F G',commutative=True)
print('A5 (1+eF)(1+eG) mod e^2 =',sp.expand((1+eps*F1)*(1+eps*G1)).subs(eps**2,0))
# A6 trace pairing invariance on a finite cyclic group algebra (toy for convolution + sharp): B(k*f,g)=B(f,k#*g)
rng=np.random.default_rng(1); N=17
cc=lambda a,b: np.real(np.fft.ifft(np.fft.fft(a)*np.fft.fft(b)))
sharp=lambda a: np.roll(a[::-1],1)
tau=rng.normal(size=N); tau=(tau+sharp(tau))/2           # arbitrary even functional
B=lambda a,b: tau@cc(a,sharp(b))
k,f_,g_=rng.normal(size=(3,N)); print('A6 B(k*f,g)-B(f,k#*g)=',B(cc(k,f_),g_)-B(f_,cc(sharp(k),g_)),'  B sym:',B(f_,g_)-B(g_,f_))
# (C) E×E over F_q: D=Σ_{n=0}^N c_n Γ_{F^n}; Γ_m·Γ_n=(a^m−a^n)(b^m−b^n), Γ·v=1, Γ_n·h=q^n=(ab)^n
a,b=sp.symbols('a b'); Nn=4; c=sp.symbols('c0:%d'%(Nn+1))
D2=sum(c[m]*c[n]*(a**m-a**n)*(b**m-b**n) for m in range(Nn+1) for n in range(Nn+1))
d1=sum(c); d2=sum(c[n]*(a*b)**n for n in range(Nn+1)); A_=sum(c[n]*a**n for n in range(Nn+1)); B_=sum(c[n]*b**n for n in range(Nn+1))
print('C1 D^2 - 2 d1 d2 + 2 A B =',sp.expand(D2-2*d1*d2+2*A_*B_))
# C2: genuine Weil numbers vs real "ghost" pair with same product q (FE-level identical), on degree-(0,0) D
def prim_test(av,bv,trials=2000):
    worst=-np.inf
    for _ in range(trials):
        cv=rng.normal(size=Nn+1); M=np.array([np.ones(Nn+1),[(av*bv)**n for n in range(Nn+1)]]).real
        Q,_=np.linalg.qr(M.T); cv=cv-Q@(Q.T@cv)                         # impose d1=d2=0
        val=complex(D2.subs(dict(zip(c,cv))).subs({a:av,b:bv}).evalf())
        worst=max(worst,val.real)
    return worst
print('C2 q=5 genuine a=1+2i,b=1-2i: max D^2 on degree-0 =',prim_test(1+2j,1-2j,300))
print('   q=5 ghost a=3,b=5/3 (ab=q, a+b=14/3 not integer-Hasse): max D^2 on degree-0 =',prim_test(3.0,5/3,300))

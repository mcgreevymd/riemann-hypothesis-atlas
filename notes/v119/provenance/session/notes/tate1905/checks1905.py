import sympy as sp, numpy as np
from scipy.integrate import quad
x,a,b,y=sp.symbols('x a b y',real=True); f=sp.Function('f')
psi=lambda t: sp.exp(2*sp.pi*sp.I*t)               # real-place character (convention-dependent sign)
U=lambda c,h: h.subs(x,x-c); V=lambda c,h: psi(c*x)*h
F=f(x)
print('U_a V_b - psi(-ab) V_b U_a =',sp.simplify(U(a,V(b,F))-psi(-a*b)*V(b,U(a,F))))
# finite model Z/N: clock-shift Heisenberg, DFT swaps
N=7; w=np.exp(2j*np.pi/N); S=np.roll(np.eye(N),1,axis=0); C=np.diag(w**np.arange(N))
print('finite S C = w^-1 C S:',np.allclose(S@C,w**-1*C@S))
Fm=np.array([[w**(j*k) for k in range(N)] for j in range(N)])/np.sqrt(N)
print('DFT: F S F^-1 = C^{+-1}:',np.allclose(Fm@S@np.linalg.inv(Fm),C) or np.allclose(Fm@S@np.linalg.inv(Fm),np.conj(C)))
# smeared dilation at archimedean place: (θ(g)f)(x)=∫g(λ) f(x/λ) d*λ ; f=Gaussian e^{-πx²} (self-dual), check value at 0 and FT at 0
g=lambda l: np.exp(-(np.log(l)-0.3)**2)*(1+np.log(l))       # arbitrary test on R+*
fg=lambda t: np.exp(-np.pi*t*t)
th0=quad(lambda l: g(l)*fg(0/l)/l,0,np.inf)[0]
thhat0=quad(lambda t: quad(lambda l: g(l)*fg(t/l)/l,0,np.inf)[0],-np.inf,np.inf)[0]
m0=quad(lambda l: g(l)/l,0,np.inf)[0]; m1=quad(lambda l: g(l),0,np.inf)[0]   # ∫g d*λ, ∫g λ d*λ
print('(θ(g)f)(0) = f(0) ev_0 :',th0, m0*1.0)
print('(θ(g)f)^(0) = fhat(0) ev_1 :',thhat0, m1*1.0)

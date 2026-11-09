import mpmath as mp, json
from sympy import bernoulli, factorint, Matrix, Poly, symbols
mp.mp.dps=30
out={}
# (a) E2 quasimodular anomaly and E2* modularity at z=0.1+0.9i
def E2(z,N=400):
    q=mp.e**(2j*mp.pi*z); return 1-24*mp.fsum(n*q**n/(1-q**n) for n in range(1,N))
z=mp.mpc(0.1,0.9); w=-1/z
an=E2(w)-(z**2*E2(z)+12*z/(2j*mp.pi))
E2s=lambda z: E2(z)-3/(mp.pi*z.imag)
out['E2_anomaly_residual']=str(abs(an)); out['E2star_modular_residual']=str(abs(E2s(w)-z**2*E2s(z)))
# (b) Kronecker limit: E(z,s) near s=1 vs 3/(pi(s-1)) + 6/pi(gamma - log2 - log(sqrt(y)|eta|^2))
xi=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Eis(z,s,N=60):
    x,y=z.real,z.imag; phi=xi(2*s-1)/xi(2*s)
    tail=mp.fsum(2*abs(n)**(s-0.5)*mp.fsum(mp.mpf(d)**(1-2*s) for d in range(1,abs(n)+1) if abs(n)%d==0)*mp.besselk(s-0.5,2*mp.pi*abs(n)*y)*mp.cos(2*mp.pi*n*x) for n in range(1,N))*2
    return y**s+phi*y**(1-s)+mp.sqrt(y)/xi(2*s)*tail
def eta(z,N=400):
    q=mp.e**(2j*mp.pi*z); return mp.e**(2j*mp.pi*z/24)*mp.fprod(1-q**n for n in range(1,N))
eps=mp.mpf('1e-8')
kron=3/(mp.pi*eps)+6/mp.pi*(mp.euler-mp.log(2)-mp.log(mp.sqrt(z.imag)*abs(eta(z))**2))
out['kronecker_residual_at_s=1+1e-8']=str(abs(Eis(z,1+eps)-kron))
# (c) M_A = 2(S_A - S_reg), S_reg = -zeta'/zeta(1/2) = Gamma_R'/Gamma_R(1/2) = K0/2
K0=mp.digamma(0.25)-mp.log(mp.pi)
Sreg=-mp.zeta(0.5,derivative=1)/mp.zeta(0.5)
out['K0']=str(K0); out['-zeta_prime_over_zeta(1/2)']=str(Sreg); out['K0/2 - Sreg']=str(K0/2-Sreg)
def a(n):
    f=factorint(n)
    return mp.log(list(f)[0])/mp.sqrt(n) if len(f)==1 else 0
for A in (0.6,1,2,3):
    SA=mp.fsum(a(n) for n in range(2,int(mp.floor(mp.e**A))+1) if mp.log(n)<A)
    out[f'M_A(A={A})']=[str(-K0+2*SA),str(2*(SA-Sreg))]
# (d) Eisenstein scattering time delay vs Weil symbol on the edge line
Lam=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
dlog=lambda f,s: mp.diff(lambda u: mp.log(f(u)),s)
phi=lambda s: Lam(2*s-1)/Lam(2*s)
res=[]
for t in (0.7,3.1,14.1347,20):
    s=mp.mpf(0.5)+1j*t
    lhs=-dlog(phi,s); rhs=4*mp.re(dlog(Lam,1+2j*t))
    res.append([t,str(mp.chop(lhs)),str(rhs)])
out['-phi_prime_over_phi(1/2+it)_vs_4ReLam_prime_over_Lam(1+2it)']=res
# (e) a1(f_k) bound: |k(k-12)/(6B_k)|+|k(k+2)/(6B_{k+2})| < 2k
B=lambda k: mp.mpf(int(bernoulli(k).p))/int(bernoulli(k).q)
bad=[k for k in range(14,400,2) if abs(k*(k-12)/(6*B(k)))+abs(k*(k+2)/(6*B(k+2)))>=2*k]
out['a1_bound_fails_for_k_in_14..398']=bad
out['a1_bound_k=10']=str(abs(10*(-2)/(6*B(10)))+abs(10*12/(6*B(12))))
json.dump(out,open('analytic1990.json','w'),indent=1)
print(json.dumps(out,indent=1))

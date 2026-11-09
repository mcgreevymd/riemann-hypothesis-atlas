# t2006: quartic oscillator as a generator-first geometry; and the xp (scaling) analogue. Exact (sympy) + numerics.
import sympy as sp, numpy as np, mpmath as mp, json
r={}
q,p,E,lam,Y=sp.symbols('q p E lambda Y')
# (1) energy curve  p^2 = f(q) := 2E - q^2 - lam q^4/2  (H = p^2/2 + q^2/2 + lam q^4/4)
f=2*E-q**2-lam*q**4/2
d=sp.factor(sp.discriminant(f,q)); r['disc_q']=str(d)
r['singular_fibres']='disc=0 <=> E=0 or 1+4*lam*E=0 (E=-1/(4lam): only relevant for lam<0 double well)'
# genus: y^2 = quartic with distinct roots -> genus 1 (smooth model has 2 points at infinity, lam>0 leading coeff -lam/2)
r['genus_generic']=1
# j-invariant of y^2 = quartic via invariants I,J of binary quartic a q^4+b q^3+c q^2+dq+e
a,b,c,dd,e=-lam/2,0,-1,0,2*E
I=12*a*e-3*b*dd+c**2; J=72*a*c*e+9*b*c*dd-27*a*dd**2-27*e*b**2-2*c**3
jinv=sp.simplify(6912*I**3/(4*I**3-J**2)); r['j_invariant']=str(sp.factor(jinv))
# (2) quantum: ground state of -1/2 d^2 + q^2/2 + lam q^4/4, lam=1; factorization H - E0 = A*A/2? Here H-E0 = (1/2) A^dag A, A = d/dq + phi, phi=-u0'/u0
lv=1.0; N=1200; L=8.0; x=np.linspace(-L,L,N); h=x[1]-x[0]
V=x**2/2+lv*x**4/4
Hm=(np.diag(1/h**2+V)+np.diag(-0.5/h**2*np.ones(N-1),1)+np.diag(-0.5/h**2*np.ones(N-1),-1))
w,v=np.linalg.eigh(Hm); u0=np.abs(v[:,0]); E0=w[0]; r['E0_quartic_lam1']=float(E0); r['E_low']=[float(t) for t in w[:5]]
phi=-np.gradient(np.log(u0),h)
# check Riccati: phi^2 - phi' = 2(V-E0)  (so H-E0 = 1/2 (-d+phi)(d+phi) )
ric=phi**2-np.gradient(phi,h)-2*(V-E0); m=np.abs(x)<3; r['riccati_max_resid_|q|<3']=float(np.max(np.abs(ric[m])))
# (3) Bohr-Sommerfeld with Maslov 1/2: oint p dq = 2pi(n+1/2) from the energy curve
def action(Ev):
    qt=float(mp.sqrt((-1+mp.sqrt(1+4*lv*Ev))/lv))
    return 2*float(mp.quad(lambda s: mp.sqrt(max(0,2*Ev-s**2-lv*s**4/2)),[-qt,qt]))
BS=[]
for n in range(5):
    BS.append(float(mp.findroot(lambda Ev: action(float(Ev))-2*mp.pi*(n+0.5),w[n])))
r['BohrSommerfeld_n0..4']=BS; r['BS_rel_err']=[float(abs(BS[i]-w[i])/w[i]) for i in range(5)]
# (4) xp analogue (Berry-Keating/Connes): region {x,p>0, xp<=E, x>=1? cutoff} area -> smooth zero count
# Riemann-Siegel theta: N_smooth(T)=theta(T)/pi+1 ~ (T/2pi)(log(T/2pi)-1)+7/8
for T in [50,200,1000]:
    th=float(mp.siegeltheta(T)/mp.pi+1); bk=T/(2*np.pi)*(np.log(T/(2*np.pi))-1)+7/8
    r[f'Nsmooth_T{T}']=[th,bk,th-bk]
# xp symmetrized: spectrum of (xp+px)/2 on L2(R+) is all of R (dilation generator): no ground state, no A*A
r['xp_note']='H=xp: level sets hyperbolas (noncompact, genus 0, no turning points); quantum dilation generator spectrum R; not bounded below'
json.dump(r,open('osc2006.json','w'),indent=1); print(json.dumps(r,indent=1))

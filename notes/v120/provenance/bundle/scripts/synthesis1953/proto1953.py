# synthesis1953 prototype: 24-boson / Petersson calibration + xi Euclidean slice + Bogoliubov ordering
import mpmath as mp, json, sympy as sp
mp.mp.dps=30
N=400
sig1=[0]+[sum(d for d in range(1,n+1) if n%d==0) for n in range(1,N)]
sig3=[0]+[sum(d**3 for d in range(1,n+1) if n%d==0) for n in range(1,N)]
def E2(t): q=mp.e**(2j*mp.pi*t); return 1-24*mp.fsum(sig1[n]*q**n for n in range(1,N))
def E4(t): q=mp.e**(2j*mp.pi*t); return 1+240*mp.fsum(sig3[n]*q**n for n in range(1,N))
def E2s(t): return E2(t)-3/(mp.pi*mp.im(t))
out={}
# (1) imaginary axis: E2 zero y0 vs E2* zero (=1); variance positivity
y0=mp.findroot(lambda y: mp.re(E2(1j*y)),(0.5,1),solver='anderson'); out['E2_zero_y0']=str(y0)
out['E2star_at_i']=str(mp.re(E2s(1j)))
out['axis']=[[y,float(mp.re(E2(1j*y))),float(mp.re(E2s(1j*y))),float(mp.re((E4(1j*y)-E2(1j*y)**2)/12))] for y in [0.4,0.6,0.8,1,1.25,1.6,2.5]]
# duality check E2*(i/y) = -y^2 E2*(iy)
out['duality_resid']=float(abs(E2s(1j/1.7)+1.7**2*E2s(1.7j)))
# (2) Hessian split of Phi=-log(y^6|Delta|) at tau=iy (x,y coords): numeric second derivatives
def logD(t): # log|Delta| via eta product
    q=mp.e**(2j*mp.pi*t); return mp.re(mp.log(q)+24*mp.fsum(mp.log(1-q**n) for n in range(1,120)))
def Phi(x,y): return -(6*mp.log(y)+logD(x+1j*y))
hs=[]
for y in [0.8,1.0,1.5]:
    h=mp.mpf('1e-4')
    fxx=(Phi(h,y)-2*Phi(0,y)+Phi(-h,y))/h**2
    fyy=(Phi(0,y+h)-2*Phi(0,y)+Phi(0,y-h))/h**2
    V=(mp.pi**2/3)*mp.re(E4(1j*y)-E2(1j*y)**2)
    hs.append(dict(y=y,Phi_xx=float(fxx),Phi_yy=float(fyy),pred_xx=float(-V),pred_yy=float(V+6/y**2),
                   Jinv_half_trace=float((fxx+fyy)/2),curv_3_over_y2=float(3/y**2)))
out['hessian_split']=hs
# (3) radial score R=Re(2*pi*i*tau*E2*) in fundamental domain outside |tau|=1 (should be <0 if Petersson norm decreases outward)
grid=[];neg=0;pos=0
for x in [0,0.1,0.2,0.3,0.4,0.49]:
    for r in [1.02,1.1,1.3,1.6,2.2,3.0]:
        y=mp.sqrt(max(r**2-x**2,1e-9)); t=x+1j*y
        R=float(mp.re(2j*mp.pi*t*E2s(t))); grid.append([x,r,R]); neg+=R<0; pos+=R>=0
out['radial_grid']=grid; out['radial_neg_pos']=[neg,pos]
# on-circle check
out['radial_on_circle']=[float(mp.re(2j*mp.pi*mp.e**(1j*a)*E2s(mp.e**(1j*a)))) for a in [mp.pi/2,mp.pi/2-0.3,mp.pi/3+0.01]]
# (4) xi Euclidean slice: xi(1/2+x)=2∫_0^∞Phi(u)cosh(xu)du ; kappa2 = (log xi)'' at x=0
def PhiRP(u):
    return mp.fsum((2*mp.pi**2*n**4*mp.e**(9*u/2)-3*mp.pi*n**2*mp.e**(5*u/2))*mp.e**(-mp.pi*n**2*mp.e**(2*u)) for n in range(1,8))
def xi(s): return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
xs=[]
for x in [0,0.3,1.0]:
    I=2*mp.quad(lambda u: PhiRP(u)*mp.cosh(x*u),[0,0.5,1,2,4])
    xs.append([x,float(I),float(xi(mp.mpf(0.5)+x))])
out['xi_slice']=xs
k2=mp.diff(lambda x: mp.log(xi(mp.mpf(0.5)+x)),0,2); out['xi_kappa2']=float(k2)
m2=2*mp.quad(lambda u: PhiRP(u)*u**2,[0,0.5,1,2,4])/xi(mp.mpf(0.5)); out['xi_m2_from_Phi']=float(m2)
out['Phi_min_on_grid']=float(min(PhiRP(mp.mpf(u)/10) for u in range(0,40)))
# (5) Bogoliubov/Kubo-Mori <= symmetrized covariance on a qubit (exact formula check)
b,a=sp.symbols('b a',positive=True)
# rho=diag(p,1-p), A=[[0,1],[1,0]]: sym var = 1 (mean 0); KM = (p-(1-p))/(log p - log(1-p))*2 ... use generic formula
p=sp.Rational(1,5); lam=[p,1-p]
km=sum(abs(1)**2*((lam[i]-lam[j])/(sp.log(lam[i])-sp.log(lam[j]))) for i,j in [(0,1),(1,0)])
sym=sum(sp.Rational(1,2)*(lam[i]+lam[j]) for i,j in [(0,1),(1,0)])
out['qubit_KM_vs_sym']=[float(km),float(sym)]
json.dump(out,open('proto1953.json','w'),indent=1,default=str)
for k,v in out.items(): print(k,v)

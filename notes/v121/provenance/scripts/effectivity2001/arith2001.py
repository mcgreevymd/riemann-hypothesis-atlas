# Base and archimedean calibrations for a RELATIVE (fibred) arithmetic RR:
#  (1) Spec Z-bar base: theta-h0 (van der Geer-Schoof) RR h0(L)-h0(L^dual)=deg L (Poisson), hence h0 >= chi  (rank 1 and rank 2).
#  (2) P^1_Z -> Spec Z with Fubini-Study O(1): chi-hat(O(n)) exact, arithmetic Hilbert-Samuel n^2 coefficient, torsion-type constants.
#  (3) K0 as twice the mean log-norm under the Tate/theta archimedean weight at the critical twist.
import mpmath as mp, numpy as np, json
mp.mp.dps=30; out={}
def h0_lattice(Bm):  # Bm: basis rows of lattice in R^r with standard metric; h0 = log sum exp(-pi |x|^2)
    Bm=np.array(Bm,float); r=len(Bm); R=12; s=0.0
    import itertools
    for c in itertools.product(range(-R,R+1),repeat=r):
        v=np.array(c)@Bm; s+=np.exp(-np.pi*v@v)
    return np.log(s)
rows=[]
for d in (-1.0,-0.3,0.0,0.4,1.2):
    L=[[np.exp(-d)]]; Ld=[[np.exp(d)]]
    rows.append(dict(deg=d,h0=float(h0_lattice(L)),h0_dual=float(h0_lattice(Ld)),RR_err=float(h0_lattice(L)-h0_lattice(Ld)-d)))
out['(1) rank1 theta RR']=rows
Bm=np.array([[0.7,0.0],[0.31,0.9]]); Bd=np.linalg.inv(Bm).T; deg=-np.log(abs(np.linalg.det(Bm)))
out['(1) rank2 theta RR']=dict(deg=float(deg),h0=float(h0_lattice(Bm)),h0_dual=float(h0_lattice(Bd)),err=float(h0_lattice(Bm)-h0_lattice(Bd)-deg),
     note='h0(L) >= deg L since h0(L^dual) >= 0 : base inequality h0 >= chi holds with no H^1 control')
# (2) P^1_Z, O(n), FS L2 norms ||x^k y^(n-k)||^2 = k!(n-k)!/(n+1)!   (normalized FS volume)
def chihat(n): return 0.5*sum(mp.log(mp.factorial(n+1)/(mp.factorial(k)*mp.factorial(n-k))) for k in range(n+1))
tab=[]
for n in (50,100,200,400,800):
    c=chihat(n); tab.append([n,float(c),float(c/n**2)])
out['(2) chihat(O(n)) and chihat/n^2']=tab
# exact closed form via Barnes G: sum_{k=0}^n log k! = log G(n+2)
def closed(n): return 0.5*((n+1)*mp.log(mp.factorial(n+1))-2*mp.log(mp.barnesg(n+2)))
out['(2) closed form check n=200']=float(chihat(200)-closed(200))
# asymptotic: subtract n^2/4 + (n/2)log n ... fit residual to a n log n + b n + c log n + d
ns=[400,800,1600,3200,6400]; Y=[closed(n)-mp.mpf(n)**2/4 for n in ns]
A=np.array([[float(n*mp.log(n)),n,float(mp.log(n)),1] for n in ns]); coef=np.linalg.lstsq(A,np.array([float(y) for y in Y]),rcond=None)[0]
out['(2) fit chihat - n^2/4 = a n log n + b n + c log n + d']=dict(a=coef[0],b=coef[1],c=coef[2],d=coef[3],
     zeta_prime_m1=float(mp.zeta(-1,derivative=1)),half_log2pi=float(mp.log(2*mp.pi)/2))
out['(2) reading']='n^2/4 = (1/2) hat c1(O(1))^2 n^2 with hat c1^2=1/2 (arith. Hilbert-Samuel); lower terms carry L2-vs-Quillen/torsion constants (zeta\'(-1), log 2pi): a ZETA-REGULARIZED slot, not K0'
# (3) K0 = 2 d/ds log Gamma_R(s) at 1/2 = 2 E[log|x|] under e^{-pi x^2}|x|^{-1/2} dx
num=mp.quad(lambda x: mp.log(x)*mp.e**(-mp.pi*x*x)*x**(-0.5),[0,1,mp.inf]); den=mp.quad(lambda x: mp.e**(-mp.pi*x*x)*x**(-0.5),[0,1,mp.inf])
out['(3) 2E[log|x|] (critical Tate weight)']=float(2*num/den); out['(3) K0']=float(mp.digamma(0.25)-mp.log(mp.pi))
out['(3) scale: Gaussian e^{-pi c x^2} shifts 2E[log|x|] by']=float(2*(mp.quad(lambda x: mp.log(x)*mp.e**(-mp.pi*2*x*x)*x**(-0.5),[0,1,mp.inf])/mp.quad(lambda x: mp.e**(-mp.pi*2*x*x)*x**(-0.5),[0,1,mp.inf]))-2*num/den)
out['(3) predicted -log c (c=2)']=float(-mp.log(2))
json.dump(out,open('arith2001.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))

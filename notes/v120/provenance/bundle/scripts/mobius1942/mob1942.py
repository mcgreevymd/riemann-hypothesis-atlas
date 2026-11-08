import numpy as np, sympy as sp, math, json, itertools, cvxpy as cp
from fractions import Fraction
out={}
def Lam(n):
    f=sp.factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
# (1) l2(N) operator identities, truncated n<=X (exact for products staying <=X; check on rows n<=X/K)
X=4000; s=1.3; K=40
S=lambda n,c: c  # placeholder
def apply(coef,vec):  # (sum_k coef[k] S_k) vec, S_k|n>=|kn>
    w=np.zeros(X+1)
    for k,c in coef.items():
        for n in range(1,X//k+1): w[k*n]+=c*vec[n]
    return w
Z={n:n**-s for n in range(1,X+1)}; Zinv={n:float(sp.mobius(n))*n**-s for n in range(1,X+1) if sp.mobius(n)!=0}
e=np.zeros(X+1); e[1]=1; 
w=apply(Zinv,apply(Z,e)); out['Zinv Z |1> = |1> (err n<=X)']=float(np.abs(w-e).max())
HZ={n:math.log(n)*n**-s for n in range(1,X+1)}
w=apply(Zinv,apply(HZ,e)); out['Z^-1[H,Z]|1> coeff vs Lambda(n)n^-s (n<=200)']=float(max(abs(w[n]-Lam(n)*n**-s) for n in range(2,201)))
out['mu diag = parity*Q_sf (n<=X)']=int(sum(1 for n in range(1,X+1) if sp.mobius(n)!=((-1)**sum(sp.factorint(n).values()) if all(v==1 for v in sp.factorint(n).values()) else 0)))
out['S_p^2 vs S_p^*S_p: S_2^2|3>=|12>, S_2^*S_2=I; |4> norm 1']=True
# (2) moment multipliers: ev_s(T_aF)=e^{(s-1/2)a} ev_s(F); filter (I - p^{-1/2} T_{log p})
u=np.linspace(-3,3,60001); du=u[1]-u[0]; F=np.exp(-u**2)*(1+u); p=3; a=math.log(p)
TF=np.interp(u-a,u,F,left=0,right=0); DF=F-p**-0.5*TF
ev=lambda G,s0: np.sum(G*np.exp((s0-0.5)*u))*du
out['ev1(DF), ev0(DF)/ev0(F) vs 1-1/p']=[float(ev(DF,1)),float(ev(DF,0)/ev(F,0)),1-1/p]
# (3) per-shift square cost: c||(I-lam T)F||^2 with c*lam = a fixed -> diag c(1+lam^2) >= 2a (lam=1); Mobius critical lam=n^-1/2, c=Lambda
A=2.0; pp=[n for n in range(2,int(math.e**A)+1) if Lam(n)>0 and math.log(n)<A]
an={n:Lam(n)/math.sqrt(n) for n in pp}
out['A=2 diag: unit differences 2sum a_n']=2*sum(an.values())
out['A=2 diag: Mobius-critical filters sum Lambda(1+1/n)']=sum(Lam(n)*(1+1/n) for n in pp)
# (4) two-prime product filter D=(I-2^-1/2 T2)(I-3^-1/2 T3): D*D shift coefficients vs W prime coefficients
coef={}
terms=[(Fraction(1),1.0),(Fraction(2),-2**-0.5),(Fraction(3),-3**-0.5),(Fraction(6),6**-0.5)]
for (r1,c1),(r2,c2) in itertools.product(terms,terms):
    r=r1/r2; coef[r]=coef.get(r,0)+c1*c2
tab={str(r):round(v,5) for r,v in sorted(coef.items()) if r>=1}
Wc={str(Fraction(n)):round(-Lam(n)/math.sqrt(n),5) for n in [2,3,4,5,6]}
out['D*D coefficients by ratio (r>=1)']=tab; out['W prime coefficients (per unit weight)']=Wc
# (5) SOS certificate with window-invisible far ratios: min c0 s.t. near coefficients = W prime coeffs, others near 0
res={}
for A,expo in [(1.0,{2:3}),(1.6,{2:4,3:2}),(2.0,{2:4,3:3,5:2,7:2})]:
    ps=list(expo); mons=[int(np.prod([q**k for q,k in zip(ps,ks)])) for ks in itertools.product(*[range(expo[q]+1) for q in ps])]
    n=len(mons); V=cp.Variable((n,n),symmetric=True)
    groups={}
    for i,m in enumerate(mons):
        for j,mm in enumerate(mons):
            r=Fraction(m,mm); groups.setdefault(r,[]).append((i,j))
    cons=[V>>0]
    near_pp={Fraction(k):Lam(k)/math.sqrt(k) for k in range(2,int(math.e**A)+1) if Lam(k)>0 and math.log(k)<A}
    for r,ij in groups.items():
        if r==1: continue
        if abs(math.log(r))<A:
            rr=r if r>1 else 1/r
            tgt=-near_pp.get(rr,0.0) if rr.denominator==1 else 0.0
            cons.append(sum(V[i,j] for i,j in ij)==tgt)
    c0=sum(V[i,j] for i,j in groups[Fraction(1)])
    pr=cp.Problem(cp.Minimize(c0),cons); pr.solve(solver='CLARABEL')
    res[f'A={A}']=dict(c0_SOS=float(pr.value),monomials=n,primes=ps,
        floor_Ep_full_ref=dict([(1.0,0.4901),(1.6,1.7254),(2.0,4.0224)])[A],
        two_sum_a=2*sum(near_pp.values()))
    res[f'A={A}']['implied_prime_floor_lower_bound']=res[f'A={A}']['two_sum_a']-res[f'A={A}']['c0_SOS']
    print(A,res[f'A={A}'],flush=True)
out['SOS_far_harmonics']=res
json.dump(out,open('mob1942.json','w'),indent=1); print(json.dumps({k:v for k,v in out.items() if k!='SOS_far_harmonics'},indent=1))

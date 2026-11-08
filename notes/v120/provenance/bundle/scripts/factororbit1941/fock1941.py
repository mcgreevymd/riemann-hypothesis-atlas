import numpy as np, sympy as sp, mpmath as mp, json, math
out={}
# ---- (A) Kepler/apsis exact (sympy)
r,l,mu,E=sp.symbols('r l mu E',positive=True)
U=l**2/(2*r**2)-mu/r; rc=sp.solve(sp.diff(U,r),r)[0]
out['r_circ']=str(rc); out['Ueff2_at_rc']=str(sp.simplify(sp.diff(U,r,2).subs(r,rc)))
# apsis of ellipse (mu=1,l=1,E=-0.3): rdot=0, rddot=-U'(r_a) !=0 ; normal accel mu/r^2 = v^2/kappa, v^2/r only if circular
Un=U.subs({l:1,mu:1}); aps=sp.solve(sp.Eq(Un,-sp.Rational(3,10)),r); rp=min(aps); 
v2=lambda rr: 2*(-sp.Rational(3,10)+1/rr); 
out['apsides']=[float(a) for a in aps]; out['rddot_at_peri']=float(-sp.diff(Un,r).subs(r,rp))
out['g_vs_v2_over_r_at_peri']=[float(1/rp**2),float(v2(rp)/rp)]
# ---- (B) prime-exponent Fock space on l2({1..X}), primes <= P
X=3000; P=[2,3,5,7]; ns=list(range(1,X+1)); idx={n:i for i,n in enumerate(ns)}; D=len(ns)
def v(n,p):
    k=0
    while n%p==0: n//=p; k+=1
    return k
def bdag(p):
    B=np.zeros((D,D))
    for n in ns:
        if p*n<=X: B[idx[p*n],idx[n]]=math.sqrt(v(n,p)+1)
    return B
Bd={p:bdag(p) for p in P}; Bm={p:Bd[p].T for p in P}
Sp={p:(Bd[p]>0).astype(float) for p in P}             # Bost-Connes/pairs1904 isometry S_p|n>=|pn>
Np={p:np.diag([v(n,p) for n in ns]) for p in P}
# interior = states n with p*n<=X for all p in P (away from truncation boundary)
inter=np.array([all(p*n<=X for p in P) for n in ns])
res={}
for p in P:
    C=Bm[p]@Bd[p]-Bd[p]@Bm[p]
    res[f'CCR_p{p}_interior_err']=float(np.abs((C-np.eye(D))[np.ix_(inter,inter)]).max())
    res[f'CCR_p{p}_boundary_states_with_defect']=int(np.sum(np.abs(np.diag(C)-1)>1e-12))
    res[f'BdagB=N_p{p}']=float(np.abs(Bd[p]@Bm[p]-Np[p]).max())
    res[f'bdag=S_sqrt(N+1)_p{p}']=float(np.abs(Bd[p]-Sp[p]@np.diag(np.sqrt(np.diag(Np[p])+1))).max())
    res[f'S*S-I_interior_p{p}']=float(np.abs((Sp[p].T@Sp[p]-np.eye(D))[np.ix_(inter,inter)]).max())
for p,q in [(2,3),(3,7)]:
    res[f'[b{p},b{q}dag]']=float(np.abs(Bm[p]@Bd[q]-Bd[q]@Bm[p]).max())
smooth=[n for n in ns if all(n%1==0 for _ in [0]) and sp.factorint(n) and max(sp.factorint(n))<=7] if True else []
H=sum(math.log(p)*Np[p] for p in P)
sm=np.array([n==1 or max(sp.factorint(n))<=7 for n in ns])
res['H=log n on 7-smooth']=float(np.abs(np.diag(H)[sm]-np.log(np.array(ns))[sm]).max())
# normalized creation: |n> = prod (b_p^dag)^k / sqrt(k!) |1>, test n=360=2^3 3^2 5
vac=np.zeros(D); vac[0]=1; w=vac.copy()
for p,k in [(2,3),(3,2),(5,1)]:
    for _ in range(k): w=Bd[p]@w
w=w/math.sqrt(math.factorial(3)*math.factorial(2)*math.factorial(1))
res['|360> norm & position']=[float(w@w),int(np.argmax(w))+1]
res['unnormalized ||(b2dag)^k|1>||^2 = k!']=[float(np.linalg.norm(np.linalg.matrix_power(Bd[2],k)@vac)**2) for k in range(1,8)]
out['fock']=res
# ---- (C) coherent (Poisson, n!) vs thermal (geometric, Euler) : z_p = p^{-s}
s=1.0  # real
coh=sum(np.prod([ (p**(-s))**v(n,p)/math.sqrt(math.factorial(v(n,p))) for p in P])**2 for n in ns if sm[idx[n]])
out['coherent ||z||^2 vs exp(sum p^-2s)']=[coh,math.exp(sum(p**(-2*s) for p in P))]
geo=sum(n**(-2*s) for n in ns if sm[idx[n]]); out['isometry vector sum n^-2s vs prod 1/(1-p^-2s)']=[geo,float(np.prod([1/(1-p**(-2*s)) for p in P]))]
# thermal occupation: <N_p>_beta = 1/(p^beta-1) = sum_k p^{-k beta}; Sum_p log p <N_p> = sum Lambda(n) n^-beta
b=2.0; out['sum logp/(p^b-1) vs -zeta\'/zeta(2)']=[float(sum(math.log(p)/(p**b-1) for p in sp.primerange(2,10**6))),float(-mp.diff(mp.zeta,2)/mp.zeta(2))]
# ---- (D) Weil self-energy as truncated occupation at beta=1/2: 2 sum_{p^k<e^A} log p p^{-k/2}
A=2.0; Mp=2*sum(math.log(p)*sum(p**(-k/2) for k in range(1,40) if k*math.log(p)<A) for p in sp.primerange(2,int(math.e**A)+1))
out['A=2: 2 sum Lambda(n)/sqrt n (n<e^A) as truncated occupation']=Mp
out['A=2: M_A = -K0 + that']=float(-(mp.digamma(0.25)-mp.log(mp.pi))+Mp)
print(json.dumps(out,indent=1)); json.dump(out,open('fock1941.json','w'),indent=1)
# cross-prime commutator restricted to deep interior (n*p*q <= X)
deep=np.array([all(p*q*n<=X for p in P for q in P) for n in ns])
cc={f'[b{p},b{q}dag]_deep':float(np.abs((Bm[p]@Bd[q]-Bd[q]@Bm[p])[np.ix_(deep,deep)]).max()) for p,q in [(2,3),(3,7),(2,5)]}
print(cc); out['fock'].update(cc); json.dump(out,open('fock1941.json','w'),indent=1)

# Test of the claim "tau(n), sigma_11(n) collapse to Lambda(n)/sqrt n": explicit Euler log-derivative coefficients at p and p^2.
import sympy as sp, mpmath as mp, json
N=60; q=sp.symbols('q')
# tau(n) from Delta = q prod (1-q^n)^24
P=sp.Poly(sp.prod([(1-q**n)**24 for n in range(1,N)]).series(q,0,N).removeO(),q) if False else None
coef=[0]*(N+1); coef[0]=1
for n in range(1,N):
    for _ in range(24):
        new=coef[:]
        for k in range(n,N+1): new[k]-=coef[k-n]
        coef=new
tau={n:coef[n-1] for n in range(1,N+1)}
sig=lambda n,k: sum(d**k for d in range(1,n+1) if n%d==0)
out={'tau(1..12)':[tau[n] for n in range(1,13)],
     'Delta q-expansion vanishing order at cusp':1,
     'mod 691 check tau(n)-sigma11(n) for n<=60':all((tau[n]-sig(n,11))%691==0 for n in range(1,N+1))}
rows=[]
for p in (2,3,5,7):
    t=tau[p]; s1=t; s2=t*t-2*p**11                                # alpha^m+beta^m
    assert tau[p*p]==t*t-p**11
    a=t/mp.mpf(p)**5.5; th=mp.acos(a/2)                             # normalized alpha = e^{i th}
    for m,sm in ((1,s1),(2,s2)):
        LamDelta=sm*mp.log(p)                                       # coefficient of p^{-ms} in -L'/L(Delta,s)
        normed=sm/mp.mpf(p)**(5.5*m)*mp.log(p)/mp.mpf(p)**(m/2)      # shift to critical centre, then /sqrt(n)
        target=mp.log(p)/mp.mpf(p)**(m/2)                            # Lambda(n)/sqrt(n) for zeta
        eis=(1+mp.mpf(p)**(11*m))*mp.log(p)                         # -L'/L of zeta(s)zeta(s-11)
        eisn=(mp.mpf(p)**(-5.5*m)+mp.mpf(p)**(5.5*m))*mp.log(p)/mp.mpf(p)**(m/2)
        rs=(2+2*mp.cos(2*m*th))*target                               # Rankin-Selberg Delta x Delta-bar, normalized
        rows.append(dict(n=f'{p}^{m}',tau_p=t,alpha_m_plus_beta_m=sm,Lambda_Delta=float(LamDelta),
            Delta_normalized_over_sqrtn=float(normed),target_Lambda_over_sqrtn=float(target),ratio=float(normed/target),
            two_cos_m_theta=float(2*mp.cos(m*th)),Eis_coeff=float(eis),Eis_normalized_over_sqrtn=float(eisn),
            RS_normalized=float(rs),RS_minus_target_equals_Sym2=float(rs-target),Sym2_pred=float((1+2*mp.cos(2*m*th))*target)))
out['p, p^2 table']=rows
json.dump(out,open('hecke2002.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))

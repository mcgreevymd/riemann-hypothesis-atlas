import sympy as sp, json
from sympy import bernoulli, zeta, Rational, divisor_sigma, symbols
out={}
B12=bernoulli(12); out['B12']=str(B12); out['zeta(-11)']=str(zeta(-11)); out['-B12/12']=str(-B12/12)
out['zeta(-2),zeta(-4)']=[str(zeta(-2)),str(zeta(-4))]
out['E12 const 65520/691 = -24/B12']=str(-24/B12); out['G12 const -B12/24']=str(-B12/24)
# Delta = q prod (1-q^n)^24 to q^N
N=60; q=symbols('q'); D=sp.Poly(1,q)
P=[0]*(N+1); P[0]=1
for n in range(1,N+1):
    for _ in range(24):
        P=[P[i]-(P[i-n] if i>=n else 0) for i in range(N+1)]
tau=[0]+P[:N]   # tau(n)=coeff of q^n = P[n-1]
out['tau(1..5)']=tau[1:6]
out['tau(2)-sigma11(2), /691']=[tau[2]-int(divisor_sigma(2,11)), (tau[2]-int(divisor_sigma(2,11)))//691]
out['tau=sigma11 mod 691 for n<=60']=all((tau[n]-int(divisor_sigma(n,11)))%691==0 for n in range(1,N+1))
out['691 | num(B12); 2<=12<=691-3']=[sp.numer(B12)%691==0, 2<=12<=688]
out['irregular check: k even 2..688 with 691 | num(B_k)']=[k for k in range(2,689,2) if sp.numer(bernoulli(k))%691==0]
# Mellin multipliers of D_p = I - p^{-1/2}T_{log p}, h(s)=∫F e^{(s-1/2)u}
s,p=symbols('s p',positive=True)
mD=1-p**Rational(-1,2)*p**(s-Rational(1,2)); mDs=1-p**Rational(-1,2)*p**(-(s-Rational(1,2)))
out['mult D_p, D_p*']=[str(sp.simplify(mD)),str(sp.simplify(mDs))]
out['D D* = -p^{s-1}(1-p^-s)(1-p^{1-s})']=str(sp.simplify(sp.expand(mD*mDs+p**(s-1)*(1-p**-s)*(1-p**(1-s)))))
x=symbols('x',real=True)
crit=sp.simplify((mD*mDs).subs(s,Rational(1,2)+sp.I*x).rewrite(sp.exp))
out['on s=1/2+ix: D D* multiplier = |1-p^{-1/2}p^{ix}|^2 check (p=3,x=0.7)']=[complex(crit.subs({p:3,x:0.7}).evalf()), abs(1-3**-0.5*3**(0.7j))**2]
print(json.dumps(out,indent=1,default=str)); json.dump(out,open('b1945.json','w'),indent=1,default=str)

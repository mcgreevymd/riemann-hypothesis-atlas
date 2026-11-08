import sympy as sp, mpmath as mp, json
out={}
# (1) derivation ring: theta on P,Q,R,Y (Y=1/y). theta y = -1/(4 pi) => theta Y = Y^2/(4 pi)
P,Q,R,Y=sp.symbols('P Q R Y'); pi=sp.pi
d={P:(P**2-Q)/12, Q:(P*Q-R)/3, R:(P*R-Q**2)/2, Y:Y**2/(4*pi)}
th=lambda f: sp.expand(sum(sp.diff(f,v)*d[v] for v in d))
E2s=P-3*Y/pi
Dk=lambda f,k: th(f)-sp.Rational(k,12)*P*f          # Serre
Rk=lambda f,k: th(f)-k*Y/(4*pi)*f                     # Maass raising (theta normalization)
out['raise2_E2s']=sp.simplify(Rk(E2s,2)-(E2s**2-Q)/12)==0
out['raise4_Q']=sp.simplify(Rk(Q,4)-(E2s*Q-R)/3)==0
out['raise6_R']=sp.simplify(Rk(R,6)-(E2s*R-Q**2)/2)==0
out['raise_minus_serre_is_kE2s/12']=all(sp.simplify(Rk(f,k)-Dk(f,k)-sp.Rational(k,12)*E2s*f)==0 for f,k in [(Q,4),(R,6),(Q**3-R**2,12)])
D=(Q**3-R**2)/1728
out['serre12_Delta']=sp.simplify(Dk(D,12))==0
out['raise12_Delta=E2s*Delta']=sp.simplify(Rk(D,12)-E2s*D)==0
# Wronskians of same-weight sections: P cancels
W12=sp.factor(Q**3*th(R**2)-R**2*th(Q**3)); out['wronskian_Q3_R2']=str(W12)
W24=sp.factor((Q**3)**2*th(Q**3*R**2)-Q**3*R**2*th((Q**3)**2)); out['wronskian_Q6_Q3R2']=str(W24)
out['wronskian_P_free']=(sp.diff(W12,P)==0)
# (2) q-series: E10=E4E6, B10/20
N=30
s=lambda n,k: sum(d**k for d in range(1,n+1) if n%d==0)
E4=[1]+[240*s(n,3) for n in range(1,N)]; E6=[1]+[-504*s(n,5) for n in range(1,N)]
E10=[1]+[-264*s(n,9) for n in range(1,N)]
prod=[sum(E4[i]*E6[n-i] for i in range(n+1)) for n in range(N)]
out['E10_eq_E4E6']=prod==E10
B10=sp.bernoulli(10); out['B10']=str(B10); out['B10_over_20']=str(B10/20); out['-2k/B_k k=10']=str(-20/B10)
out['dimM_k (k=10,12)']=[1,2]
for k,v in out.items(): print(k,':',v)

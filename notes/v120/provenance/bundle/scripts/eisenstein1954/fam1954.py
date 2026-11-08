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
# (3) degrees: Petersson c1(lambda^k) over F = k/12 ; FS pullback of [E4^3:E6^2] over F ~ 1
out['petersson_deg_lambda12']=str(sp.Rational(12,4)/pi*pi/3)
mp.mp.dps=15
M=60
c4=[0]+[240*s(n,3) for n in range(1,M)]; c6=[0]+[-504*s(n,5) for n in range(1,M)]
def f(t):
    q=mp.e**(2j*mp.pi*t)
    e4=1+mp.fsum(c4[n]*q**n for n in range(1,M)); e6=1+mp.fsum(c6[n]*q**n for n in range(1,M))
    de4=2j*mp.pi*mp.fsum(n*c4[n]*q**n for n in range(1,M)); de6=2j*mp.pi*mp.fsum(n*c6[n]*q**n for n in range(1,M))
    a=e4**3; b=e6**2; da=3*e4**2*de4; db=2*e6*de6
    return abs(a*db-b*da)**2/(abs(a)**2+abs(b)**2)**2/mp.pi
def inner(x):
    y0=mp.sqrt(1-x*x)
    return mp.quad(lambda y: f(x+1j*y),[y0,1.2,2,4,8])
deg=mp.quad(inner,[-0.5,0,0.5]); out['FS_degree_numeric']=float(deg)
# (4) arithmetic pair Wronskian on the line: m_N(x) = -Wr/|Lam_N|^2, Wr = L(s)*d/ds[L(1-s)] - L(1-s)*L'(s)
A=1.0; ns=[n for n in range(2,int(mp.e**A)+1) if sp.factorint(n) and len(sp.factorint(n))==1]
Lam=lambda n: mp.log(list(sp.factorint(n).keys())[0])
def logL(s): return -s/2*mp.log(mp.pi)+mp.loggamma(s/2)+mp.fsum(Lam(n)*mp.mpf(n)**(-s)/mp.log(n) for n in ns)
L=lambda s: mp.e**logL(s)
chk=[]
for x in [0,0.7,3.0,12.0]:
    s0=mp.mpf(0.5)+1j*x
    Wr=L(s0)*mp.diff(lambda z: L(1-z),s0)-L(1-s0)*mp.diff(L,s0)
    lhs=-Wr/abs(L(s0))**2
    m=mp.re(mp.digamma(0.25+0.5j*x))-mp.log(mp.pi)-2*mp.fsum(Lam(n)/mp.sqrt(n)*mp.cos(x*mp.log(n)) for n in ns)
    chk.append([x,str(mp.chop(lhs,1e-12)),float(m)])
out['pair_wronskian_vs_mN_A1']=chk
json.dump(out,open('fam1954.json','w'),indent=1,default=str)
for k,v in out.items(): print(k,':',v)

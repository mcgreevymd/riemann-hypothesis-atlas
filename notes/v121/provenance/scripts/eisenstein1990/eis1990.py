# eisenstein1990: exact level-1 Eisenstein / Serre / cusp-correction computations. RH is NOT proved.
from fractions import Fraction as Fr
from sympy import bernoulli, factorint, Matrix, Poly, symbols, GF, divisor_sigma, isprime
import json
N=60
def sig(n,r): return int(divisor_sigma(n,r))
def B(k): return Fr(int(bernoulli(k).p),int(bernoulli(k).q))
def E(k):  # E_k = 1 - (2k/B_k) sum sigma_{k-1}(n) q^n
    c=-Fr(2*k)/B(k); return [Fr(1)]+[c*sig(n,k-1) for n in range(1,N+1)]
def mul(a,b): return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(N+1)]
def add(*fs): return [sum(x) for x in zip(*fs)]
def sc(c,a): return [c*x for x in a]
def D(a): return [n*a[n] for n in range(N+1)]
E2=E(2)
def serre(f,k): return add(D(f),sc(-Fr(k,12),mul(E2,f)))
Delta=[Fr(0)]+[Fr(0)]*N
# Delta via (E4^3-E6^2)/1728
E4,E6=E(4),E(6)
Delta=sc(Fr(1,1728),add(mul(mul(E4,E4),E4),sc(-1,mul(E6,E6))))
assert Delta[1]==1 and Delta[2]==-24 and Delta[3]==252
def pw(a,e):
    r=[Fr(1)]+[Fr(0)]*N
    for _ in range(e): r=mul(r,a)
    return r
def Mbasis(K):  # Miller-free basis: E4^a E6^b Delta^j ... use E_{K-12j}*Delta^j with E0=1
    bas=[]
    for j in range(K//12+1):
        w=K-12*j
        if w==0: g=[Fr(1)]+[Fr(0)]*N
        elif w==2: continue
        elif w in (4,6,8,10,14): g=E(w)
        else: g=E(w)
        bas.append(mul(g,pw(Delta,j)))
    return bas
def dimM(K): return len(Mbasis(K))
def solve_in(f,bas):
    m=len(bas); A=Matrix([[bas[j][n] for j in range(m)] for n in range(m)]); b=Matrix([f[n] for n in range(m)])
    x=A.LUsolve(b); x=[Fr(int(v.p),int(v.q)) for v in x]
    res=add(f,*[sc(-x[j],bas[j]) for j in range(m)])
    return x,max(abs(r) for r in res)  # residual up to q^N (Sturm bound is floor(K/12)+1 << N)
out={}
# 0. Ramanujan & weight-2 quasimodularity
r=add(D(E2),sc(-Fr(1,12),add(mul(E2,E2),sc(-1,E4))))
out['ramanujan_DE2_residual']=str(max(abs(x) for x in r))
# 1. f_k = theta_k E_k + (k/12) E_{k+2} in S_{k+2}
def a1formula(k): return 2*k+Fr(k*(k-12),6)/B(k)-Fr(k*(k+2),6)/B(k+2)
fk={}
for k in range(4,62,2):
    K=k+2
    f=add(serre(E(k),k),sc(Fr(k,12),E(K)))
    bas=Mbasis(K)
    x,res=solve_in(f,bas)
    dimS=len(bas)-1
    assert f[0]==0 and res==0, (k,res)
    assert f[1]==a1formula(k)
    fk[k]=f
    out.setdefault('fk',{})[k]={'dimS':dimS,'a1':str(f[1]),'zero':all(v==0 for v in f),
        'a1_den_primes':sorted(factorint(f[1].denominator)) if f[1]!=0 else [],
        'numB_Kover_K_primes':sorted(factorint(abs((B(K)/K).numerator)))}
# 2. Hecke T2 on S_K (basis Delta^j E_{K-12j}, j>=1) and Krylov rank of f_k
def T(p,f,K,M):
    return [ (f[p*n] if p*n<=N else None) if n%p else (f[p*n] if p*n<=N else None) for n in range(M)]
def T2(f,K):
    M=N//2+1; g=[]
    for n in range(M):
        v=f[2*n] + (Fr(2)**(K-1)*f[n//2] if n%2==0 else 0)
        g.append(v)
    return g
def Sbasis(K): return Mbasis(K)[1:]
def coords(f,bas):
    m=len(bas)
    # use rows n=1..m (cusp basis Delta^j... is upper triangular from q^j)
    A=Matrix([[bas[j][n] for j in range(m)] for n in range(1,m+1)]); b=Matrix([f[n] for n in range(1,m+1)])
    return list(A.LUsolve(b))
kry={}
for k,f in fk.items():
    K=k+2; S=Sbasis(K); m=len(S)
    if m<2: continue
    Tm=Matrix([coords(T2(s,K),S) for s in S]).T
    v=Matrix(coords(f,S)); cols=[v]
    for i in range(m-1): cols.append(Tm*cols[-1])
    rk=Matrix.hstack(*cols).rank()
    kry[K]={'dimS':m,'krylov_rank_under_T2':rk,'charpoly_T2':str(Tm.charpoly().as_expr())}
out['krylov']=kry
# 3. Eisenstein-cusp congruences, dim-1 weights: Delta_K normalized, compare to sigma_{K-1} mod p for p | num(B_K/K)
cong={}
for K in (12,16,18,20,22,26):
    S=Sbasis(K); g=S[0]; assert g[1]==1
    ps=sorted(factorint(abs((B(K)/K).numerator)))
    cong[K]={p: all((int(g[n])-sig(n,K-1))%p==0 for n in range(1,N+1)) for p in ps}
    cong[K]['tau_K(2)']=int(g[2])
out['dim1_congruences_n_le_60']=cong
# dim-2 weights: does charpoly of T2 have root 1+2^{K-1} mod p for p | num(B_K/K)?
c2={}
x=symbols('x')
for K in (24,28,30,32,34,38):
    S=Sbasis(K); m=len(S)
    Tm=Matrix([coords(T2(s,K),S) for s in S]).T
    cp=Tm.charpoly(x).as_expr()
    ps=sorted(factorint(abs((B(K)/K).numerator)))
    c2[K]={'dimS':m,'primes':ps,
           'root_1+2^(K-1)_mod_p':{p: int(Poly(cp,x).eval(1+2**(K-1)))%p==0 for p in ps if p>K}}
out['higher_dim_congruences']=c2
# 4. denominators: E_{p-1} == 1 mod p (Hasse) for p>=5
has={}
for p in (5,7,11,13,17,19,23):
    e=E(p-1); has[p]=all((v.numerator*pow(v.denominator,-1,p))%p==0 for v in e[1:])
out['E_{p-1}=1_mod_p']=has
json.dump(out,open('eis1990.json','w'),indent=1,default=str)
print(json.dumps({k:v for k,v in out.items() if k!='fk'},indent=1,default=str)[:6000])
for k in sorted(fk): print(k,out['fk'][k])

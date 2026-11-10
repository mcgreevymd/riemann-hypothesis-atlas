# t2087 scratch: prime block of W as intersection numbers. Zeros never used.
import itertools, math, json, numpy as np
from fractions import Fraction
OUT={}
# ---------- A. function field template ----------
def polymulmod(a,b,mod,p):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    d=len(mod)-1
    for i in range(len(r)-1,d-1,-1):
        c=r[i]
        if c:
            for j in range(d+1): r[i-d+j]=(r[i-d+j]-c*mod[j])%p
    r=r[:d]+[0]*(d-len(r[:d])); return r
def irreducible(p,k):
    if k==1: return [0,1]
    for coeffs in itertools.product(range(p),repeat=k):
        mod=list(coeffs)+[1]
        if coeffs[0]==0: continue
        # irreducible iff no roots in subfields: test x^(p^k)=x and gcd conditions crudely by brute factor check over deg<=k/2
        ok=True
        for d in range(1,k//2+1):
            for c2 in itertools.product(range(p),repeat=d):
                f=list(c2)+[1]
                # polynomial remainder mod f
                r=mod[:]
                for i in range(len(r)-1,d-1,-1):
                    c=r[i]
                    if c:
                        for j in range(d+1): r[i-d+j]=(r[i-d+j]-c*f[j])%p
                if all(v==0 for v in r[:d]): ok=False;break
            if not ok:break
        if ok: return mod
def count_points(p,k,fcoef):
    """projective smooth model of y^2=f(x), deg f odd => one point at infinity. fcoef low->high over F_p."""
    mod=irreducible(p,k); q=p**k
    elems=[list(c) for c in itertools.product(range(p),repeat=k)]
    def power(a,e):
        r=[1]+[0]*(k-1); b=a[:]
        while e:
            if e&1: r=polymulmod(r,b,mod,p)
            b=polymulmod(b,b,mod,p); e>>=1
        return r
    N=1
    for x in elems:
        # f(x)
        val=[0]*k; xp=[1]+[0]*(k-1)
        for c in fcoef:
            val=[(v+c*w)%p for v,w in zip(val,xp)]; xp=polymulmod(xp,x,mod,p)
        if all(v==0 for v in val): N+=1
        else:
            chi=power(val,(q-1)//2)
            N+= 2 if chi==[1]+[0]*(k-1) else 0
    return N
def mobius(n):
    m,res,d=n,1,2
    while d*d<=m:
        if m%d==0:
            m//=d
            if m%d==0: return 0
            res=-res
        d+=1
    return -res if m>1 else res
def ff_case(name,p,fcoef,K,g):
    q=p; N={0:None}
    for k in range(1,K+1): N[k]=count_points(p,k,fcoef)
    # closed points of degree d (Mobius inversion), Lambda identity
    a={d:sum(mobius(d//e)*N[e] for e in range(1,d+1) if d%e==0)//d for d in range(1,K+1)}
    lam_ok=all(N[k]==sum(d*a[d] for d in range(1,k+1) if k%d==0) for k in range(1,K+1))
    # intersection numbers on C x C: f1=C x pt? use Gamma_k.f1=1, Gamma_k.f2=q^k, Delta=Gamma_0, Gamma_k.Gamma_l=q^l N_{k-l} (k>=l), Gamma_0^2=Delta^2=2-2g
    def NN(m): return (2-2*g) if m==0 else N[m]
    def I(k,l):
        k,l=max(k,l),min(k,l); return q**l*NN(k-l)
    def deg(k): return (1,q**k)
    def Iprim(k,l):
        (a1,b1),(a2,b2)=deg(k),deg(l); return I(k,l)-a1*b2-b1*a2
    Kmax=K+1
    G=np.array([[Iprim(k,l)/q**((k+l)/2) for l in range(Kmax)] for k in range(Kmax)])
    Wff=lambda m: (q**(m/2)+q**(-m/2)) - NN(m)/q**(m/2)   # P_ff - prime block (Weil zero side sum beta^m, m>=1; m=0 -> 2g)
    T=np.array([[-Wff(abs(k-l)) for l in range(Kmax)] for k in range(Kmax)])
    ev=np.linalg.eigvalsh(G)
    res=dict(curve=name,q=q,genus=g,N=[N[k] for k in range(1,K+1)],closed_points=a,lambda_identity=lam_ok,
             toeplitz_residual=float(abs(G-T).max()),primitive_gram_eigs=ev.tolist(),hodge_index_NSD=bool(ev.max()<1e-9),
             W_ff=[Wff(m) for m in range(0,K+1)],
             note="G_kl = q^{-(k+l)/2} Gamma_k^0.Gamma_l^0 = -W_ff(k-l); NSD by Castelnuovo-Severi/Hodge index")
    return res
OUT['A_elliptic_F5']=ff_case('y^2=x^3+x+1 /F5',5,[1,1,0,1],4,1)
OUT['A_genus2_F3']=ff_case('y^2=x^5+2x+1 /F3 (squarefree, genus 2)',3,[1,2,0,0,0,1],6,2)
# smoothness check for genus-2: f squarefree over F3
# ---------- B. Hecke / Hurwitz ----------
def hurwitz(N):
    if N==0: return Fraction(-1,12)
    if N%4 in (1,2): return Fraction(0)
    D=-N; h=Fraction(0)
    b=N%2
    while b*b<=N//3:
        if (b*b+N)%4==0:
            ac=(b*b+N)//4
            a=max(b,1)
            while a*a<=ac:
                if ac%a==0:
                    c=ac//a
                    if a==b or a==c or b==0: w=Fraction(1)
                    else: w=Fraction(2)
                    if a==b==c: w=Fraction(1,3)
                    elif a==c and b==0: w=Fraction(1,2)
                    h+= w
                a+=1
        b+=2
    return h
def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)
KH=[]
for n in range(1,60):
    lhs=sum(hurwitz(4*n-t*t) for t in range(-int(2*math.isqrt(n))-1,int(2*math.isqrt(n))+2) if 4*n-t*t>=0)
    rhs=2*sigma(n)-sum(min(d,n//d) for d in range(1,n+1) if n%d==0)
    KH.append((n,str(lhs),rhs,lhs==rhs))
OUT['B_kronecker_hurwitz_all_ok']=all(x[3] for x in KH); OUT['B_kh_sample']=KH[:12]
def T_deg(n): return sigma(n)
def cusp(n): return sum(min(d,n//d) for d in range(1,n+1) if n%d==0)
rows=[]
for p in [2,3,5,7]:
    for k in range(1,6):
        n=p**k; m=p**(k-2) if k>=2 else None
        deg=T_deg(n)-(p*T_deg(m) if m else 0)
        cu=cusp(n)-(p*cusp(m) if m else 0)
        rows.append(dict(p=p,k=k,deg_Phi=deg,one_plus_pk=1+p**k,cusp_part=cu,
                         normalized_trivial=2*deg/p**(k/2),zeta_atom_coeff=1/p**(k/2)))
OUT['B_Phi_pk']=rows
# ---------- C. P^1_Z x P^1_Z, Mobius graphs w = n z ----------
def factor(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
C=[]
for n in range(2,40):
    fin=2*sum(e*math.log(l) for l,e in factor(n-1).items()) if n>2 else 0.0
    arch=-0.5*4*math.log(n-1)   # t2078 Green term -4log|e^u-e^v| at (log n, 0), Gillet-Soule factor 1/2
    lam=math.log(list(factor(n))[0]) if len(factor(n))==1 else 0.0
    C.append(dict(n=n,finite=fin,arch=arch,total=fin+arch,Lambda=lam))
OUT['C_mobius']=C; OUT['C_max_abs_total']=max(abs(r['total']) for r in C)
json.dump(OUT,open('prime2087.json','w'),indent=1,default=str)
for k in ['A_elliptic_F5','A_genus2_F3']:
    r=OUT[k]; print(k,r['N'],r['closed_points'],r['lambda_identity'],r['toeplitz_residual'],r['hodge_index_NSD'],np.round(r['primitive_gram_eigs'],4))
print('KH',OUT['B_kronecker_hurwitz_all_ok']); 
for r in rows[:10]: print(r)
print('C max|total|',OUT['C_max_abs_total'])

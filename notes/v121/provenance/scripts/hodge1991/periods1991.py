# hodge1991 part B: weight-12 Eichler-Shimura period polynomials, integral lattice, pairings. RH not proved.
import sympy as sp, mpmath as mp, json
from sympy import Matrix, binomial, factorial, divisor_sigma
X=sp.symbols('X'); w=10
def act(P,g):
    (a,b),(c,d)=g
    return sp.expand(sp.cancel((c*X+d)**w*sp.sympify(P).subs(X,(a*X+b)/(c*X+d))))
S=[[0,-1],[1,0]]; T=[[1,1],[0,1]]; Ti=[[1,-1],[0,1]]; U=[[1,-1],[1,0]]; U2=[[0,-1],[1,-1]]
def vec(P): P=sp.Poly(sp.expand(P),X); return [P.coeff_monomial(X**i) for i in range(w+1)]
mons=[X**i for i in range(w+1)]
def mat(fn): return Matrix([vec(fn(m)) for m in mons]).T
Ms=mat(lambda P: P+act(P,S)); Mu=mat(lambda P: P+act(P,U)+act(P,U2))
K=Matrix.vstack(Ms,Mu).nullspace()
out={'dim W (Eichler-Shimura-Manin, k=12)':len(K)}
def inW(P): return all(x==0 for x in vec(P+act(P,S))) and all(x==0 for x in vec(P+act(P,U)+act(P,U2)))
e=X**10-1; c1=X**2*(X**2-1)**3; m1=4*X**9-25*X**7+42*X**5-25*X**3+4*X
out.update({'X^10-1 in W':inW(e),'X^2(X^2-1)^3 in W':inW(c1),'4X^9-25X^7+42X^5-25X^3+4X in W':inW(m1),
            'X^10-1 == 1|S - 1':sp.expand(act(1,S)-1-e)==0, '1|T == 1 (T-invariant)':act(1,T)==1})
# W ∩ Z[X] lattice: is {X^10-1, X^2(X^2-1)^3, m1} a Z-basis of W_Z = W_Q ∩ Z[X]_{<=10}?
A=Matrix([vec(e),vec(c1),vec(m1)])
from sympy.matrices.normalforms import smith_normal_form
snf=smith_normal_form(A,domain=sp.ZZ)
out['Smith invariants of [e,c1,m1] (all 1 => saturated Z-basis)']=[snf[i,i] for i in range(3)]
# ---- numerical periods r_n = int_0^inf Delta(it) t^n dt = Lambda(Delta,n+1)
mp.mp.dps=40
NT=80
def tau(n): # from E4^3-E6^2
    return taus[n]
from fractions import Fraction
Nq=NT+1
def sig(n,r): return int(divisor_sigma(n,r))
def mul(a,b): return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(Nq)]
E4=[1]+[240*sig(n,3) for n in range(1,Nq)]; E6=[1]+[-504*sig(n,5) for n in range(1,Nq)]
taus=[(x-y)//1728 for x,y in zip(mul(mul(E4,E4),E4),mul(E6,E6))]
def Lam(s):  # completed L, root number +1, Lambda(s)=Lambda(12-s)
    return mp.fsum(taus[m]*(mp.gammainc(s,2*mp.pi*m)/(2*mp.pi*m)**s+mp.gammainc(12-s,2*mp.pi*m)/(2*mp.pi*m)**(12-s)) for m in range(1,Nq))
r=[Lam(n+1) for n in range(w+1)]
# rho(X) = int_0^{i inf} Delta(z)(X-z)^10 dz = sum_n C(10,n) X^{10-n} (-1)^n i^{n+1} r_n
coef={}
for n in range(w+1):
    coef[w-n]=int(binomial(w,n))*(-1)**n*mp.mpc(0,1)**(n+1)*r[n]
# even part: X^{10-n} with n even -> i^{n+1} imaginary; odd part n odd -> real
rp=[ (coef[j].imag if j%2==0 else 0) for j in range(w+1)]
rm=[ (coef[j].real if j%2==1 else 0) for j in range(w+1)]
# normalize
op=-rp[8]   # coefficient pattern -X^2(X^2-1)^3 has X^8 coeff -1
om=rm[9]/4
out['r+/omega+ coefficients (X^0..X^10)']=[mp.nstr(x/op,15) for x in rp]
out['r-/omega- coefficients']=[mp.nstr(x/om,15) for x in rm]
target_p=vec(sp.Rational(36,691)*e - c1); target_m=vec(m1)
out['max|r+/w+ - [(36/691)(X^10-1) - X^2(X^2-1)^3]|']=mp.nstr(max(abs(rp[j]/op-float(target_p[j])) for j in range(w+1)),5)
out['max|r-/w- - m1|']=mp.nstr(max(abs(rm[j]/om-float(target_m[j])) for j in range(w+1)),5)
out['omega+']=mp.nstr(op,20); out['omega-']=mp.nstr(om,20)
# integral lattice in W+: lines Eis=Z e, cusp = Z(36 e - 691 c1); index in W+_Z=Ze+Zc1
out['index [W+_Z : Z(X^10-1) + Z(36(X^10-1)-691 X^2(X^2-1)^3)]']=abs(Matrix([[1,0],[36,-691]]).det())
# ---- Sym^10 invariant symmetric pairing <P,Q> = sum_{a+b=w} (-1)^a a! b!/w! p_a q_b
def pair(P,Q):
    p,q=vec(P),vec(Q); return sp.nsimplify(sum((-1)**a*factorial(a)*factorial(w-a)/factorial(w)*p[a]*q[w-a] for a in range(w+1)))
G=Matrix(w+1,w+1,lambda i,j: pair(X**i,X**j))
out['pairing symmetric']=G==G.T
ev=[sp.re(x) for x in G.eigenvals(multiple=True)]
out['signature (pos,neg)']=(sum(1 for x in ev if x>0),sum(1 for x in ev if x<0))
# invariance under SL2(Z) generators
inv=all(pair(act(X**i,g),act(X**j,g))==pair(X**i,X**j) for g in (S,T) for i in range(w+1) for j in range(w+1))
out['pairing SL2(Z)-invariant']=inv
out['<1,1> (cusp T-invariant vector isotropic)']=str(pair(1,1))
out['polar of 1 = {q_10=0}: <1,X^j> for j']=[str(pair(1,X**j)) for j in range(w+1)]
# rational normal curve isotropy: (X - zY)^10 with Y=1
z=sp.symbols('z')
out['<(X-z)^10,(X-z)^10>']=str(sp.simplify(pair((X-z)**10,(X-z)**10)))
# nilpotent N = d/dX = log T ; weight filtration = degree filtration; isotropic/self-dual flag check
selfdual=all(all(pair(X**i,X**j)==0 for i in range(j0+1) for j in range(10-j0)) for j0 in range(10))
out['deg<=j  orthogonal to deg<=9-j (osculating flag self-dual)']=selfdual
out['polarized limit sign <X^10, N^10 X^10>']=str(pair(X**10,sp.diff(X**10,X,10)))
# ---- Haberland-type pairing test: 6(2i)^{11} <Delta,Delta> vs <rho|(T - T^{-1}), conj rho>
pet=mp.mpf('1.03536205680432092234e-6')
rho=sum(coef[j]*X**j for j in range(w+1))
def actnum(cvec,g):
    P=sum(sp.Float(0)+0*X for _ in [0]); 
    return None
# numeric polynomial action
import numpy as np
def polyact(cf,g):
    (a,b),(c,d)=g; res=[mp.mpc(0)]*(w+1)
    for j,cj in enumerate(cf):
        # (aX+b)^j (cX+d)^{w-j}
        P=sp.Poly(sp.expand((a*X+b)**j*(c*X+d)**(w-j)),X)
        for i in range(w+1): res[i]+=cj*int(P.coeff_monomial(X**i))
    return res
cf=[coef[j] for j in range(w+1)]
d=[x-y for x,y in zip(polyact(cf,T),polyact(cf,Ti))]
def npair(p,q): return mp.fsum((-1)**a*mp.factorial(a)*mp.factorial(w-a)/mp.factorial(w)*p[a]*q[w-a] for a in range(w+1))
hab=npair(d,[mp.conj(x) for x in cf])
out['<rho|(T-T^-1), conj rho>']=mp.nstr(hab,20)
out['6(2i)^11 <Delta,Delta>']=mp.nstr(6*(2j)**11*pet,20)
out['ratio']=mp.nstr(hab/(6*(2j)**11*pet),15)
# integral pairing on W via B(P,Q)=<P|(T-T^-1),Q> : Gram on basis e,c1,m1
def Bint(P,Q): return pair(sp.expand(act(P,T)-act(P,Ti)),Q)
basis={'e':e,'c1':c1,'m1':m1}
out['B(P,Q)=<P|(T-T^-1),Q> Gram on (e,c1,m1)']={p+','+q:str(Bint(basis[p],basis[q])) for p in basis for q in basis}
json.dump(out,open('periods1991.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))

# H^1_c x H^1 duality at cochain level (ansatz solve), Sym^2 Hodge-Riemann, fibre kernels, boundary-plane identity.
import sympy as sp, mpmath as mp, json, itertools
X,z,zp=sp.symbols('X z zp'); w=10
def act(P,g):
    (a,b),(c,d)=g
    return sp.expand(sp.cancel((c*X+d)**w*sp.sympify(P).subs(X,(a*X+b)/(c*X+d))))
def vec(P): P=sp.Poly(sp.expand(P),X); return [P.coeff_monomial(X**i) for i in range(w+1)]
def pair(P,Q):
    p,q=vec(P),vec(Q); return sum((-1)**a*sp.factorial(a)*sp.factorial(w-a)/sp.factorial(w)*p[a]*q[w-a] for a in range(w+1))
def mul(g,h): return [[g[0][0]*h[0][0]+g[0][1]*h[1][0],g[0][0]*h[0][1]+g[0][1]*h[1][1]],[g[1][0]*h[0][0]+g[1][1]*h[1][0],g[1][0]*h[0][1]+g[1][1]*h[1][1]]]
I=[[1,0],[0,1]];S=[[0,-1],[1,0]]; T=[[1,1],[0,1]]; Ti=[[1,-1],[0,1]]; U=[[1,-1],[1,0]]; U2=[[0,-1],[1,-1]]
out={}
e=X**10-1; c1=X**2*(X**2-1)**3; m1=4*X**9-25*X**7+42*X**5-25*X**3+4*X; Wb=[e,c1,m1]
hab=lambda P,Q: pair(act(P,T)-act(P,Ti),Q)
# Eisenstein cocycle (residue-1 normalized) from boundary1994
a0=sp.Rational(691,65520)
rodd=-sp.Rational(5,1584)*X**9-X**7/480-X**5/504-X**3/480-sp.Rational(5,1584)*X
Eis={'S':sp.expand(rodd/a0),'T':sp.expand(((X+1)**11-X**11)/11)}
# ansatz D(P,psi)=sum_{g,h} x_{g,h} <P|g, psi(h)>
G={'1':I,'S':S,'T':T,'Ti':Ti,'U':U,'U2':U2,'TS':mul(T,S),'ST':mul(S,T),'TiS':mul(Ti,S),'STi':mul(S,Ti)}
H=['S','T']
keys=list(itertools.product(G.keys(),H)); xs=sp.symbols('x0:%d'%len(keys))
def cob(v): return {'S':sp.expand(act(v,S)-v),'T':sp.expand(act(v,T)-v)}
def D(P,psi,xx=xs): return sp.expand(sum(x*pair(act(P,G[g]),psi[h]) for x,(g,h) in zip(xx,keys)))
eqs=[]
for P in Wb:
    for j in range(w+1): eqs.append(D(P,cob(X**j)))
for P in Wb:
    for Q in Wb: eqs.append(D(P,{'S':Q,'T':0})-hab(P,Q))
sol=sp.solve(eqs,xs,dict=True)
out['ansatz solutions exist']=len(sol)>0
if sol:
    s=sol[0]; free=[x for x in xs if x not in s]
    val=sp.simplify(D(e,Eis).subs(s)); out['D(X^10-1, Eis_1) (general solution)']=str(val)
    out['free params']=str(free)
    out['D(c1,Eis_1)']=str(sp.simplify(D(c1,Eis).subs(s))); out['D(m1,Eis_1)']=str(sp.simplify(D(m1,Eis).subs(s)))
    out['<1, X^10> fibre (invariant x coinvariant)']=str(pair(1,X**10))
# ---- Sym^2 of H^1_! with alternating Q (Haberland on W/Ze), Hodge-Riemann with actual periods
Q=sp.Matrix([[hab(a,b) for b in (c1,m1)] for a in (c1,m1)]); out['Q on H1_! basis (c1,m1)']=str(Q.tolist())
def Q2(u,v):  # u,v symmetric tensors as dict {(i,j):coef}, i<=j over basis 0=c1,1=m1 ; use polarization of products
    tot=0
    for (i,j),a in u.items():
        for (k,l),b in v.items():
            tot+=a*b*sp.Rational(1,2)*(Q[i,k]*Q[j,l]+Q[i,l]*Q[j,k])
    return sp.expand(tot)
basis2={'c1^2':{(0,0):1},'c1m1':{(0,1):1},'m1^2':{(1,1):1}}
G2=sp.Matrix([[Q2(basis2[a],basis2[b]) for b in basis2] for a in basis2]); out['Sym2 Gram (c1^2,c1m1,m1^2)']=str(G2.tolist())
ev=list(G2.eigenvals(multiple=True)); out['Sym2 signature']=(sum(1 for x in ev if x>0),sum(1 for x in ev if x<0)); out['Sym2 det']=str(G2.det())
# actual Hodge vector: rho_Delta = A*c1 + B*m1 mod e with A = -i*omega+ (since r+ = (36/691)e - c1), B = omega-
wp=mp.mpf('0.11437902243884895436'); wm=mp.mpf('0.0092692761623701632363')
A=-1j*wp; B=wm
def sq(a,b,c,d): return {(0,0):a*c,(0,1):a*d+b*c,(1,1):b*d}   # (a c1+b m1)(c c1+d m1)
def Q2n(u,v): return complex(sum(complex(a)*complex(b)*0.5*(float(Q[i,k])*float(Q[j,l])+float(Q[i,l])*float(Q[j,k])) for (i,j),a in u.items() for (k,l),b in v.items()))
rr=sq(A,B,A,B); rb=sq(A,B,A.conjugate(),B); rbb=sq(A.conjugate(),B,A.conjugate(),B)
out['Q2(rho^2,rho^2) [F^22 isotropic]']=str(Q2n(rr,rr)); out['Q2(rho rhobar, rho rhobar) [(11,11) real]']=str(Q2n(rb,rb))
re2={k_:complex(v).real for k_,v in rr.items()}; im2={k_:complex(v).imag for k_,v in rr.items()}
out['Q2(Re rho^2), Q2(Im rho^2) [(22,0)+(0,22) real]']=[str(Q2n(re2,re2)),str(Q2n(im2,im2))]
qrr=complex(sum(A_*B_*complex(float(Q[i,j])) for (i,A_),(j,B_) in itertools.product(enumerate([A,B]),enumerate([A.conjugate(),B]))))
out['Q(rho,rhobar)']=str(qrr); out['i^11 * Q(rho,rhobar) = -i Q']=str(-1j*qrr)
pet=mp.mpf('1.03536205680432092234e-6')
out['omega+ omega- / 2^10']=mp.nstr(wp*wm/1024,18); out['<Delta,Delta> (Haberland, hodge1991)']=mp.nstr(pet,18)
# ---- fibre kernel
out['<(X-z)^10,(X-zp)^10>']=str(sp.factor(sp.expand(pair((X-z)**10,(X-zp)**10))))
# ---- boundary plane identity: <P,P> restricted to span(1,X^10) = 2 p0 p10 ; S swaps p0<->p10
p0,p10,al,be=sp.symbols('p0 p10 alpha beta')
out['<p0+p10 X^10, same>']=str(sp.expand(pair(p0+p10*X**10,p0+p10*X**10)))
out['S swaps p0,p10: (p0+p10X^10)|S']=str(act(p0+p10*X**10,S))
out['with p0=a+b,p10=a-b']=str(sp.expand(pair((al+be)+(al-be)*X**10,(al+be)+(al-be)*X**10)))
out['W elements: (p0,p10) of e,c1,m1']=[(str(vec(P)[0]),str(vec(P)[10])) for P in Wb]
out['fibre norm <e,e>, <X^10+1,X^10+1>']=[str(pair(e,e)),str(pair(X**10+1,X**10+1))]
# 691 fractional-part check for Eis_1 coordinates from boundary1994
out['-22680 mod 691, -33736 mod 691']=[(-22680)%691,(-33736)%691]
json.dump(out,open('duality1994.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))

# boundary1994: explicit boundary sequences, integral gluing, Eisenstein cocycle, for SL2(Z), weight k (w=k-2).
# Group: PSL2(Z) = <S> * <U>, U=TS (−I acts trivially for even w). Right action (P|g)(X)=(cX+d)^w P((aX+b)/(cX+d)).
# Cocycles: phi(gh)=phi(g)|h+phi(h); determined by (phi(S),phi(U)) in ker(1+S) x ker(1+U+U^2).
import sympy as sp, json, sys
from cypari2 import Pari
pari=Pari()
X=sp.symbols('X'); pi=sp.pi
S=[[0,-1],[1,0]]; U=[[1,-1],[1,0]]; U2=[[0,-1],[1,-1]]; T=[[1,1],[0,1]]
def run(k):
    w=k-2; out={'k':k,'w':w}
    def act(P,g):
        (a,b),(c,d)=g
        return sp.expand(sp.cancel((c*X+d)**w*sp.sympify(P).subs(X,(a*X+b)/(c*X+d))))
    def vec(P): P=sp.Poly(sp.expand(P),X); return [P.coeff_monomial(X**i) for i in range(w+1)]
    mons=[X**i for i in range(w+1)]
    def mat(fn): return sp.Matrix([vec(fn(m)) for m in mons]).T
    MS=mat(lambda P:P+act(P,S)); MU=mat(lambda P:P+act(P,U)+act(P,U2))
    AS=mat(lambda P:act(P,S)-P); AU=mat(lambda P:act(P,U)-P); AT=mat(lambda P:act(P,T)-P)
    def pm(M): return pari.matrix(M.rows,M.cols,[int(x) for x in M])
    KS=pari.matkerint(pm(MS)); KU=pari.matkerint(pm(MU))   # saturated Z-bases (columns)
    nS,nU=int(pari.matsize(KS)[1]),int(pari.matsize(KU)[1])
    n=w+1
    # Z1 basis in Q^{2n}: block diag
    Z=pari.matconcat(pari.matrix(2,2,[KS,pari.matrix(n,nU),pari.matrix(n,nS),KU]))
    B=pari.matconcat(pari.matrix(2,1,[pm(AS),pm(AU)]))  # coboundaries of monomials, columns
    C=pari.matsolve(pari.matconcat(pari.matrix(1,1,[Z])) if False else Z, B) if False else None
    # express B in Z-coordinates: solve Z*C=B (Z has full column rank)
    C=pari.matinverseimage(Z,B)
    out['dim Z1']=nS+nU; out['dim B1']=int(pari.matrank(B)); out['dim H1']=nS+nU-int(pari.matrank(B))
    K=pari.matkerint(pari.mattranspose(C)); K=pari.mattranspose(K)   # rows annihilate B: coordinates on H1 free part
    out['SNF of H1-coordinate map (all 1 => onto Z^3)']=str(pari.matsnf(K))
    def coords(phiS,phiT):
        phiU=sp.expand(act(phiT,S)+phiS)      # U=TS: phi(U)=phi(T)|S+phi(S)
        assert all(x==0 for x in vec(phiS+act(phiS,S))), 'S relation'
        assert all(x==0 for x in vec(phiU+act(phiU,U)+act(phiU,U2))), 'U relation'
        v=pari.matrix(2*n,1,[pari(str(x)) for x in vec(phiS)+vec(phiU)])
        y=pari.matinverseimage(Z,v); m=K*y; return [m[i,0] for i in range(3)]
    def res(phiT): return vec(phiT)[w]   # top coefficient: V_T free part
    # --- W = cocycles with phi(T)=0  (= relative cohomology H^1(G,G_inf;V) ~ H^1_c)
    Wb=MS.col_join(MU).nullspace()
    out['dim W=Z1_T']=len(Wb)
    e=X**w-1
    out['delta(1)=1|S-1 equals X^w-1']=sp.expand(act(1,S)-1-e)==0
    out['delta(1)(T)=1|T-1']=str(sp.expand(act(1,T)-1))
    out['class of delta(1) in H1 (coords)']=str(coords(e,0))
    # Hecke T2 on W via Zagier's element (verified preserves W): {[[1,0],[0,2]],[[1,1],[0,2]],[[2,0],[0,1]],[[2,0],[1,1]]}
    T2el=[[[1,0],[0,2]],[[1,1],[0,2]],[[2,0],[0,1]],[[2,0],[1,1]]]
    T3el=None
    def hecke(P,els): return sp.expand(sum(act(P,g) for g in els))
    # saturated Z-basis of W
    MW=sp.Matrix.vstack(MS,MU)
    def satW(parity):
        rows=[[1 if j==i else 0 for j in range(n)] for i in range(n) if i%2!=parity]
        M=sp.Matrix.vstack(MW,sp.Matrix(rows)); KW=pari.matkerint(pm(M))
        return [sp.expand(sum(sp.Integer(int(KW[j,i]))*mons[j] for j in range(n))) for i in range(int(pari.matsize(KW)[1]))]
    ev=satW(0); od=satW(1)
    out['W_Z basis even']=[str(p) for p in ev]; out['W_Z basis odd']=[str(p) for p in od]
    # T2 matrix on even part
    a_=sp.symbols('a0:%d'%len(ev))
    def coordsE(P):
        sol=sp.solve(sp.Poly(sp.expand(P-sum(ai*b for ai,b in zip(a_,ev))),X).coeffs(),a_); return [sol[ai] for ai in a_]
    M2=sp.Matrix([coordsE(hecke(p,T2el)) for p in ev]).T
    out['T2 on W+_Z (columns = images of basis)']=str(M2.tolist())
    evs=M2.eigenvects(); out['T2 eigen on W+']=str([(ev_[0],[list(v) for v in ev_[2]]) for ev_ in evs])
    sig=sp.divisor_sigma(2,k-1)
    # eigenvector for sigma (should be X^w-1) and for cusp eigenvalue
    for val,mult,vs in evs:
        v=vs[0]; v=v/sp.gcd(list(v)) if all(x.is_integer for x in v) else v
        den=sp.ilcm(*[sp.fraction(sp.nsimplify(x))[1] for x in v]); v=v*den; g=sp.gcd(list(v)); v=v/g
        out[f'primitive eigvec in W+_Z coords (eig {val})']=str(list(v)); out[f'  poly']=None
    vecs=[]
    for val,mult,vs in evs:
        v=vs[0]; den=sp.ilcm(*[sp.fraction(sp.nsimplify(x))[1] for x in v]); v=v*den; v=v/sp.gcd(list(v)); vecs.append(v)
    out['index [W+_Z : eigenlines]']=abs(sp.Matrix.hstack(*vecs).det())
    out['sigma_{k-1}(2) - tau-like eigen']=str([sig-ev_[0] for ev_ in evs])
    del out['  poly']
    # --- Eisenstein cocycle from L(G_k,s)=zeta(s)zeta(s-k+1): odd periods exact; even part = coboundary multiple of X^w-1
    def r(nn): return sp.nsimplify(sp.simplify((2*pi)**(-(nn+1))*sp.factorial(nn)*sp.zeta(nn+1)*sp.zeta(nn+2-k)))
    rodd=sp.expand(sum(sp.binomial(w,nn)*(-1)**nn*sp.I**(nn+1)*r(nn)*X**(w-nn) for nn in range(1,w,2)))
    c=sp.symbols('c'); phiT=c*sp.expand((X+1)**(w+1)-X**(w+1)); phiU=sp.expand(act(phiT,S)+rodd)
    eqs=sp.Poly(sp.expand(rodd+act(rodd,S)),X).coeffs()+sp.Poly(sp.expand(phiU+act(phiU,U)+act(phiU,U2)),X).coeffs()
    cs=sp.solve(eqs,c)[c]; a0=-sp.bernoulli(k)/(2*k)
    out['odd Eisenstein period rho_G^-']=str(rodd)
    out['solved c']=str(cs); out['a0(G_k)=-B_k/2k']=str(a0); out['c == a0/(w+1)  [res_inf phi_G = a0]']=sp.simplify(cs-a0/(w+1))==0
    # normalized Eisenstein class with residue 1
    phiT1=sp.expand(phiT.subs(c,cs)/a0); phiS1=sp.expand(rodd/a0)
    out['res(Eis_1)']=str(res(phiT1))
    ce=coords(phiS1,phiT1); out['coords Eis_1 in H1_Z-free (Z^3)']=str(ce)
    # cusp classes from W (phi(T)=0)
    cc=[(str(p),str(coords(p,0))) for p in ev+od]; out['coords of W_Z basis classes']=cc
    # residue on integral lattice generators: find integral classes with residue: use coordinates map inverse
    # Integral generators of H1 free: preimages of unit vectors under K: compute res of each via a cocycle representative
    # representative cocycle for unit vector j: y = K-preimage
    Yinv=pari.matinverseimage(K,pari.matid(3))
    reslist=[]
    for j in range(3):
        y=Yinv[j]; phi=[sum(Z[i,t]*y[t] for t in range(nS+nU)) for i in range(2*n)]
        phiS=sum(sp.Rational(str(phi[i]))*mons[i] for i in range(n)); phiU_=sum(sp.Rational(str(phi[n+i]))*mons[i] for i in range(n))
        phiT_=sp.expand(act(phiU_,S)-act(phiS,S))   # phi(T)=phi(U S^{-1})=phi(U)|S^{-1}+phi(S^{-1}); phi(S^{-1})=-phi(S)|S^{-1}, S^{-1}=S in PSL
        reslist.append(str(res(phiT_)))
    out['res on H1_Z-free unit generators']=reslist
    den=sp.ilcm(*[sp.fraction(sp.Rational(str(x)))[1] for x in ce]); out['lcm denominators of Eis_1 coords']=str(den)
    out['factor']=str(sp.factorint(den)); out['num zeta(1-k)']=str(sp.fraction(sp.zeta(1-k))[0])
    return out
res_all=[run(k) for k in (12,16)]
json.dump(res_all,open('boundary1994.json','w'),indent=1,default=str); print(json.dumps(res_all,indent=1,default=str))

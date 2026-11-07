"""High-precision exact-constraint Galerkin (scratch). Exact rational polynomial overlaps C(b) (sympy), 50-digit mpmath for
K(0), Levy moments ∫_0^A k(a) a^m da, a_n, Cholesky + eigsy. F_k = L g_k, g_k=(1−x²)^6 P_k(x), x=2u/A (or F_k=g_k if 'free')."""
import sympy as sp, mpmath as mp, sys, time
mp.mp.dps=50
u,b,x=sp.symbols('u b x')
R2M=lambda r: mp.mpf(sp.Rational(r).p)/sp.Rational(r).q
def build(A,K,pw=6,constrained=True):
    A=sp.Rational(A)
    gs=[sp.expand((1-x**2)**pw*sp.legendre(k,x)) for k in range(K)]
    Fs=[sp.expand(sp.Rational(4)/A**2*sp.diff(g,x,2)-g/4) for g in gs] if constrained else gs
    Fu=[sp.expand(F.subs(x,2*u/A)) for F in Fs]; gu=[sp.expand(g.subs(x,2*u/A)) for g in gs]
    C={}
    for j in range(K):
        for k in range(j,K):
            I=sp.expand(sp.integrate(sp.expand(Fu[j]*Fu[k].subs(u,u-b)),(u,-A/2+b,A/2)))
            C[(j,k)]=sp.Poly(I,b)
            if j!=k: C[(k,j)]=sp.Poly(sp.expand(sp.integrate(sp.expand(Fu[k]*Fu[j].subs(u,u-b)),(u,-A/2+b,A/2))),b)   # valid for 0<=b<=A
    G0=[[sp.integrate(sp.expand(gu[j]*gu[k]),(u,-A/2,A/2)) for k in range(K)] for j in range(K)]
    return dict(A=A,K=K,C=C,G0=G0,Fu=Fu)
kinf=lambda a: mp.e**(-a/2)/(1-mp.e**(-2*a))
K0=mp.re(mp.digamma(mp.mpf(1)/4))-mp.log(mp.pi)
def pp(X):
    out=[]
    for n in range(2,X+1):
        m=n;p=next(q for q in range(2,n+1) if m%q==0)
        while m%p==0:m//=p
        if m==1: out.append((n,mp.log(p)/mp.sqrt(n)))
    return out
def mats(B):
    A=R2M(B['A']); K=B['K']; C=B['C']
    co={key:[R2M(c) for c in C[key].all_coeffs()[::-1]] for key in C}       # ascending
    Cev=lambda bv: mp.matrix([[sum(c*bv**m for m,c in enumerate(co[(j,k)])) for k in range(K)] for j in range(K)])
    G=Cev(mp.mpf(0)); deg=max(len(v) for v in co.values())
    mom=[None]+[mp.quad(lambda a,m=m: kinf(a)*a**m,[0,A]) for m in range(1,deg)]
    tail=mp.quad(kinf,[A,mp.inf]); D=mp.matrix(K,K)
    for j in range(K):
        for k in range(K):
            cj,ck=co[(j,k)],co[(k,j)]
            assert abs(2*G[j,k]-cj[0]-ck[0])<mp.mpf(10)**-40
            D[j,k]=sum(-(cj[m] if m<len(cj) else 0)*mom[m]-(ck[m] if m<len(ck) else 0)*mom[m] for m in range(1,deg))+2*G[j,k]*tail
    prim=[(n,an,Cev(mp.log(n))) for n,an in pp(int(mp.floor(mp.e**A))) if mp.log(n)<A]
    G0=mp.matrix([[R2M(B['G0'][j][k]) for k in range(K)] for j in range(K)])
    return dict(G=G,D=D,prim=prim,G0=G0,Cev=Cev,A=A,K=K)
def W(m,drop=(),scale=None,arch=True):
    Wm=K0*m['G']+(m['D'] if arch else 0*m['G'])
    for n,an,Cn in m['prim']:
        if n in drop: continue
        Wm=Wm-(1 if scale is None else scale.get(n,1))*an*(Cn+Cn.T)
    return Wm
def geneig(Wm,G):
    L=mp.cholesky(G); Li=mp.inverse(L); S=Li*Wm*Li.T; S=(S+S.T)/2
    E,Q=mp.eigsy(S); idx=sorted(range(len(E)),key=lambda i:E[i]); V=Li.T*Q
    return [E[i] for i in idx],[V[:,i] for i in idx]
if __name__=='__main__':
    t0=time.time(); A=sys.argv[1]; K=int(sys.argv[2])
    m=mats(build(A,K)); E,V=geneig(W(m),m['G']); E0,_=geneig(W(m),m['G0'])
    print(A,K,'mu_min L2=',mp.nstr(E[0],12),' 2nd',mp.nstr(E[1],6),' mu_min G0=',mp.nstr(E0[0],8),
          ' M=',mp.nstr(-K0+2*sum(an for _,an,_ in m['prim']),8),' t=%.0fs'%(time.time()-t0),flush=True)

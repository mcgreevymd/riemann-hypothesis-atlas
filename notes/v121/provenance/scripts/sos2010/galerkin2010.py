# sos2010: W on E0 via F=(d^2-1/4)G, G=(1-x^2)^m x^k on window [-A/2,A/2]. E0 exact (no constraint inversion).
# Q = K0||F||^2 + ∫k_inf ||F-T_aF||^2 da - Σ_{log n<A} a_n 2<F,T_{log n}F>   (= W on E0; P=0 exactly)
# Split: ∫k_inf||ΔF||^2 = ∫k5||ΔF||^2 + 4||F||^2 - R(F),  R(F)=<G,(1/4-d^2)G>  (exact on E0)
import sympy as sp, mpmath as mp, json, sys, time
mp.mp.dps=40
x,b=sp.symbols('x b')
def primes_pw(X):
    out=[]
    for n in range(2,X+1):
        f=sp.factorint(n)
        if len(f)==1:
            p=list(f)[0]; out.append((n,mp.log(p)/mp.sqrt(n)))
    return out
def run(A,K,m=4):
    Ar=sp.Rational(A); s=Ar/2           # u = s x
    Gs=[(1-x**2)**m*x**k for k in range(K)]
    Fs=[sp.expand(sp.diff(g,x,2)/s**2-g/4) for g in Gs]
    # c_ij(beta) = ∫ F_i(u) F_j(u - b) du, b = s*beta, beta in [0,2]: s∫_{beta-1}^{1} F_i(x)F_j(x-beta)dx
    C={}
    for i in range(K):
        for j in range(K):
            pr=sp.expand(Fs[i]*Fs[j].subs(x,x-b))
            C[(i,j)]=sp.Poly(sp.expand(s*sp.integrate(pr,(x,b-1,1))),b)
    Gram=mp.matrix(K,K); R=mp.matrix(K,K)
    for i in range(K):
        for j in range(K):
            Gram[i,j]=mp.mpf(sp.Rational(C[(i,j)].eval(0)))
            R[i,j]=mp.mpf(sp.Rational(s*sp.integrate((sp.diff(Gs[i],x)*sp.diff(Gs[j],x)/s**2+Gs[i]*Gs[j]/4),(x,-1,1))))
    deg=max(C[k].degree() for k in C)
    kinf=lambda a: mp.e**(-a/2)/(1-mp.e**(-2*a)); k5=lambda a: mp.e**(-2.5*a)/(1-mp.e**(-2*a))
    Am=mp.mpf(A)
    def moms(k):  # ∫_0^A k(a)(a/s)^r da ,  r=0..deg (r=0,1 only used to check cancellation)
        return [mp.quad(lambda a: k(a)*(a/(Am/2))**r if r>0 else 0,[0,Am]) for r in range(deg+1)]
    def tail(k): return mp.quad(k,[Am,mp.inf])
    def jump(k):
        mo=moms(k); tl=tail(k); J=mp.matrix(K,K)
        for i in range(K):
            for j in range(K):
                cij=C[(i,j)].all_coeffs()[::-1]; cji=C[(j,i)].all_coeffs()[::-1]
                d=[0]*(deg+1); 
                for r,cv in enumerate(cij): d[r]-=cv
                for r,cv in enumerate(cji): d[r]-=cv
                d[0]+=2*Gram_r[(i,j)]
                assert d[0]==0 and d[1]==0, (d[0],d[1])
                J[i,j]=sum(mp.mpf(sp.Rational(d[r]))*mo[r] for r in range(2,deg+1))+2*Gram[i,j]*tl
        return J
    Gram_r={(i,j):sp.Rational(C[(i,j)].eval(0)) for i in range(K) for j in range(K)}
    Jinf=jump(kinf); J5=jump(k5)
    pp=[(n,w) for (n,w) in primes_pw(int(mp.floor(mp.e**Am))+1) if mp.log(n)<Am]
    Pr=mp.matrix(K,K); Pjump=mp.matrix(K,K); M=-(mp.digamma(0.25)-mp.log(mp.pi))
    for (n,w) in pp:
        beta=sp.Rational(mp.nstr(2*mp.log(n)/Am,45)) 
        M+=2*w
        for i in range(K):
            for j in range(K):
                v=mp.mpf(C[(i,j)].eval(beta))+mp.mpf(C[(j,i)].eval(beta))
                Pr[i,j]+=w*v; Pjump[i,j]+=w*(2*Gram[i,j]-v)
    K0=mp.digamma(0.25)-mp.log(mp.pi)
    Q=K0*Gram+Jinf-Pr
    Qsplit=J5+Pjump-(M-4)*Gram-R
    ident=max(abs(Q[i,j]-Qsplit[i,j]) for i in range(K) for j in range(K))
    def gen_min(Amat,Bmat):
        L=mp.cholesky(Bmat); Li=L**-1; Cm=Li*Amat*Li.T; Cm=(Cm+Cm.T)/2
        E,_=mp.eigsy(Cm); return sorted([E[i] for i in range(len(E))])
    eW=gen_min(Q,Gram); eJ=gen_min(J5+Pjump,Gram); eR=gen_min(R,Gram)
    # buckling: mu1 = min <G,L^2G>/<G,LG> ; <G,L^2 G> = ||F||^2 = Gram
    eB=gen_min(Gram,R)
    return dict(A=A,K=K,M_A=float(M),split_identity_maxerr=float(ident),
        W_E0_lowest=[mp.nstr(v,12) for v in eW[:3]],
        Jreg_lowest=float(eJ[0]), Meff_Ritz=float(M-4+1/eB[0]), mu1_Ritz=float(eB[0]),
        R_over_F_max=float(eR[-1]), primes=[n for n,_ in pp])
if __name__=='__main__':
    A=float(sys.argv[1]); K=int(sys.argv[2]); t0=time.time()
    out=run(A,K); out['sec']=round(time.time()-t0,1); print(json.dumps(out))

# t2098 scratch: can a Connes-Consani-style h^1 on the square carry the Hodge sign independently of W?
# Zeros never used as input except in the explicitly labelled comparison column W_ff (computed from point counts).
import itertools, math, json
import numpy as np, sympy as sp
src=open('../prime2087/prime2087.py').read()
exec(src[:src.index("def ff_case")])          # polymulmod, irreducible, count_points, mobius
OUT={}
# ---------------- A. function-field sanity case (classical) ----------------
def prim_basis(q,K):
    M=sp.Matrix([[1]*(K+1),[q**k for k in range(K+1)]])
    B=M.nullspace(); out=[]
    for v in B:
        den=sp.ilcm(*[sp.fraction(x)[1] for x in v]); out.append([int(x*den) for x in v])
    return out
def ff_rr(name,p,fcoef,K,g,cs):
    q=p; N={m:count_points(p,m,fcoef) for m in range(1,K+1)}
    NN=lambda m:(2-2*g) if m==0 else N[m]
    I=lambda k,l: q**min(k,l)*NN(abs(k-l))                    # Gamma_k.Gamma_l (Gamma_0=Delta)
    sumbeta=lambda m: 2*g if m==0 else (q**m+1-N[m])/q**(m/2)   # sum_i beta_i^m from point counts (Lefschetz), |beta|=1
    res=dict(curve=name,q=q,genus=g,N=N,cases=[])
    for c in cs:
        D2=sum(c[k]*c[l]*I(k,l) for k in range(K) for l in range(K) if k<len(c) and l<len(c))
        L=len(c); D2=sum(c[k]*c[l]*I(k,l) for k in range(L) for l in range(L))
        degs=(sum(c),sum(c[k]*q**k for k in range(L)))
        KD=(2*g-2)*(degs[0]+degs[1])
        F=[c[k]*q**(k/2) for k in range(L)]
        W=sum(F[k]*F[l]*sumbeta(abs(k-l)) for k in range(L) for l in range(L))
        row=dict(c=c,bidegree=degs,D2=D2,KD=KD,W_ff=W,D2_plus_W=D2+W,
                 chi_nD="chi(nD) = %s*n^2 + %d (exact: K.D=0 on primitive)"%(sp.Rational(D2,2),(1-g)**2))
        if g==1:
            a=q+1-N[1]   # alpha^2 = a alpha - q ; element x+y*alpha
            x,y=0,0; px,py=1,0
            for k in range(L):
                x+=c[k]*px; y+=c[k]*py
                px,py=-q*py, px+a*py
            degpsi=x*x+a*x*y+q*y*y
            row.update(deg_psi=degpsi, h1_nD_formula="h^1(nD) = deg(n psi) = n^2*deg psi = %d n^2"%degpsi,
                       check_halfW=abs(W/2-degpsi)<1e-6, h0=0,h2=0)
        res['cases'].append(row)
    return res
q=5; B=prim_basis(q,3)
OUT['A_g1']=ff_rr('y^2=x^3+x+1 /F5',5,[1,1,0,1],3,1,[B[0],B[1],[B[0][i]+2*B[1][i] for i in range(4)]])
q=3; B2=prim_basis(q,3)
OUT['A_g2']=ff_rr('y^2=x^5+2x+1 /F3',3,[1,2,0,0,0,1],3,2,[B2[0],B2[1]])

# ---------------- B. CC 2023 (Spec Zbar) dimension: 1D and Cartesian-product (Kunneth) model ----------------
def reach(gens,N,dim):
    S=set()
    for al in itertools.product((-1,0,1),repeat=len(gens)):
        ok=True; v=[0]*dim
        for d in range(dim):
            tot=sum(a*g[d] for a,g in zip(al,gens)); bnd=sum(abs(a*g[d]) for a,g in zip(al,gens))
            if bnd>N: ok=False;break
            v[d]=tot
        if ok: S.add(tuple(v))
    return S
def ccdim(N,dim):
    full=set(itertools.product(range(-N,N+1),repeat=dim))
    cands=[v for v in full if v>tuple([0]*dim)]  # one of +-v
    k=math.ceil(math.log(len(full))/math.log(3)-1e-12)
    while True:
        for gens in itertools.combinations(cands,k):
            if reach(gens,N,dim)==full: return k,gens
        k+=1
B={}
for N in [1,2,3,4,5,13]:
    d1=ccdim(N,1)[0]; B[N]=dict(dim1=d1,formula13=math.ceil(math.log(2*N+1)/math.log(3)-1e-12))
for N in [1,2,3,4]:
    d2,g2=ccdim(N,2); B[N].update(dim_box=d2,gens=g2,sum_of_1D=2*B[N]['dim1'],log3_card=2*math.log(2*N+1)/math.log(3))
OUT['B_CC_product']=B
# chi in Kunneth-Cartesian model for D=a{inf} x b{inf}, n-scaled: ~ n(a+b)/log3 : no n^2 term
def chi1(a): # CC Thm 4.3 without exceptional set
    x=(a+math.log(2))/math.log(3); return math.ceil(x) if x>=0 else -math.ceil(-x)
OUT['B_chi_growth']={n:dict(chi_cartesian=chi1(n*1.0)+chi1(n*1.0), half_D2_n2=n*n*1.0) for n in [1,2,4,8,16,32]}

# ---------------- C. scaling-site square C_p x C_p ----------------
p=3; us=[0.0,math.log(2),math.log(4)]          # mu in {1,2,4}: Cartier (rational), distinct mod 3^Z
E=np.array([[math.exp(-u/2) for u in us],[math.exp(u/2) for u in us]])
F=sp.Matrix(E.tolist()).nullspace()[0] if False else np.linalg.svd(E)[2][-1]
c=F*np.exp(-np.array(us)/2)                    # coefficients of Psi(mu_i)
# Gram on C_p x C_p: Psi(mu).Psi(mu')=0 for mu/mu' not in p^Z (disjoint radial lines); diagonal = unknown s_i (excess)
kinf=lambda a: math.exp(-a/2)/(1-math.exp(-2*a))
offdiag_needed={f"{i}{j}":dict(du=us[j]-us[i],k_inf=kinf(abs(us[j]-us[i])),
                prime_atom=("Lambda=log2 atom present in W (p=2)" ) ) for i in range(3) for j in range(3) if i<j}
# Leray: fiber restriction of D over lambda1 has degree D.F1 = C_- = 0 ; CC Thm 5.17(i): Dim H^0 = deg = 0 ; Dim H^0(-D)=0
fib=[dict(n=n,fiber_deg=float(n*(E[0]@F)),Dim_H0=0.0,Dim_H0_minus=0.0) for n in [1,2,4,8]]
OUT['C_scaling_square']=dict(p=p,mu=[1,2,4],F=F.tolist(),c=c.tolist(),Cminus=float(E[0]@F),Cplus=float(E[1]@F),
    gram_offdiag_CpxCp=0.0,offdiag_W_needs=offdiag_needed,leray_fibers=fib,
    quadratic_coeff_from_Leray=0.0,
    reason="Pic^0(C_p)=Z/(p-1)Z finite (CC Thm 5.6) -> fiber-class map locally constant -> no jumping-fiber count; degree-0 Dim_R=0")
json.dump(OUT,open('ccrr2098.json','w'),indent=1,default=str)
print(json.dumps(OUT,indent=1,default=str))

"""Test 2 (finite control + zeta Galerkin; RH NOT addressed).
Dictionary from Test 1: in E x E / F_q, Weil-type form  W_q(D) := -D^2 + 2 b0 b1 = -D_perp^2  (b=(D.v,D.h)),
so  W_q - (hyperbolic pole term 2 b0 b1) = -D^2  has EXACTLY ONE negative direction (Hodge index), while W_q >= 0.
Zeta analogue on a FREE window basis (no E0 constraint): W - P (P=2ab pole term) vs W.
Prediction of the dictionary: inertia(W-P) = (n-1, 1); W >= 0 (RH-conditional; Galerkin cannot certify >=0).
Negative eigenvalues WITH explicit vectors are certificates; positive minima are only Galerkin upper bounds."""
import sys, json, sympy as sp, mpmath as mp
sys.path.insert(0,'/workspace/taa/spring1891'); import spring_mp as S
res={}
# F_q side (q=5, a=2, genuine-like): basis h,v,Delta,Gamma
q,a=5,2; G=sp.Matrix([[0,1,1,q],[1,0,1,1],[1,1,0,q+1-a],[q,1,q+1-a,0]])
import numpy as np
e=lambda M:[round(float(x),6) for x in np.linalg.eigvalsh(np.array(M,dtype=float))]
bv=sp.Matrix([[0,1,0,0],[1,0,0,0]])*G      # rows: D.v, D.h
Hyp=bv.T*sp.Matrix([[0,1],[1,0]])*bv       # 2 b0 b1 as Gram
res['Fq_minusD2_eigs']=e(-G); res['Fq_W_eigs']=e(-G+Hyp)
for A in ['1','2']:
    B=S.build(A,8,constrained=False); m=S.mats(B); u=sp.Symbol('u'); Ar=sp.Rational(A)
    mom=lambda s: [mp.mpf(sp.N(sp.integrate(F*sp.exp(s*u/2),(u,-Ar/2,Ar/2)),60)) for F in B['Fu']]
    am,bp=mom(-1),mom(1)
    Pm=mp.matrix(8,8)
    for j in range(8):
        for k in range(8): Pm[j,k]=am[j]*bp[k]+bp[j]*am[k]        # P(F)=2ab polarized
    Wm=S.W(m); E1,V1=S.geneig(Wm,m['G']); E2,V2=S.geneig(Wm+Pm,m['G'])
    v=V1[0]; nv=(v.T*m['G']*v)[0]
    res['zeta_A='+A]=dict(W_minus_P_eigs=[mp.nstr(x,6) for x in E1[:3]],n_neg_W_minus_P=sum(1 for x in E1 if x<0),
        W_eigs=[mp.nstr(x,6) for x in E2[:3]],n_neg_W=sum(1 for x in E2 if x<0),
        cert_vector_check=mp.nstr((v.T*Wm*v)[0]/nv,8), P_on_that_vector=mp.nstr((v.T*Pm*v)[0]/nv,8))
json.dump(res,open('test2_result.json','w'),indent=1); print(json.dumps(res,indent=1))

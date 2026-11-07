"""Test 1 (exact, finite control; RH-for-zeta NOT addressed).
Question: in the finite-field model E x E / F_q, does the Weil/intersection form split as
   D^2 = C_top(b(D)) + D_perp^2,  b(D) = (D.v, D.h),  C_top(b) = 2 b0 b1  (hyperbolic, compat1907 Lemma),
with (i) b of the normalized Frobenius graphs q^{-n/2} Gamma_{F^n} transforming by the SAME diagonal law
D_a = diag(|a|^{-1/2},|a|^{1/2}) as Tate's (f(0), int f) under U_a (compat1907 §1), and (ii) the sign living
entirely on <h,v>^perp, with Sylvester inertia (not det) deciding it?
Basis h=E x pt, v=pt x E, Delta, Gamma_{F^n}. Standard intersection numbers for genus 1:
 h.v=1, h^2=v^2=0, Delta^2=0, Gamma_n^2=0 (2-2g=0), Gamma_n.v=1, Gamma_n.h=q^n, Delta.h=Delta.v=1,
 Gamma_n.Delta = N_n = q^n+1-(alpha^n+beta^n), Gamma_m.Gamma_n = N_{|m-n|}-type is NOT needed here (we use span{h,v,Delta,Gamma_1}).
"""
import sympy as sp, itertools, json
a,q=sp.symbols('a q',real=True)
def gram(q_,a_):
    return sp.Matrix([[0,1,1,q_],[1,0,1,1],[1,1,0,q_+1-a_],[q_,1,q_+1-a_,0]])
out={}
# (i) boundary law for normalized Frobenius graph: b(q^{-n/2} Gamma_n) = (q^{-n/2}*1, q^{-n/2}*q^n)
n=sp.symbols('n',integer=True,positive=True)
b=(q**(-n/2)*1, q**(-n/2)*q**n); Da=(q**(-n/2), q**(n/2))
out['i_boundary_law']=[bool(z) for z in [sp.simplify(b[0]-Da[0])==0, sp.simplify(b[1]-Da[1])==0]]
# (ii) exact split D^2 = 2 b0 b1 + D_perp^2 for general D
x=sp.symbols('x1:5'); G=gram(q,a); D=sp.Matrix(x)
b0=(sp.Matrix([0,1,0,0]).T*G*D)[0]; b1=(sp.Matrix([1,0,0,0]).T*G*D)[0]   # D.v, D.h
Dhv=b0*sp.Matrix([1,0,0,0])+b1*sp.Matrix([0,1,0,0])                        # projection onto <h,v> (h.v=1)
Dp=D-Dhv
out['ii_split_identity']=bool(sp.expand((D.T*G*D)[0]-2*b0*b1-(Dp.T*G*Dp)[0])==0)
out['ii_cross_term_zero']=bool(sp.expand((Dhv.T*G*Dp)[0])==0)
# perp Gram in basis Delta_perp, Gamma_perp
P=[sp.Matrix([0,0,1,0]),sp.Matrix([0,0,0,1])]
Pp=[p-((sp.Matrix([0,1,0,0]).T*G*p)[0])*sp.Matrix([1,0,0,0])-((sp.Matrix([1,0,0,0]).T*G*p)[0])*sp.Matrix([0,1,0,0]) for p in P]
Gp=sp.Matrix(2,2,lambda i,j:sp.expand((Pp[i].T*G*Pp[j])[0])); out['perp_gram']=str(Gp); out['perp_det']=str(sp.factor(Gp.det()))
# (iii) scan: genuine traces |a|<=2sqrt(q) vs fakes; inertia via eigenvalue signs; det sign alone
rows=[]
for qq in [2,3,4,5,7,8,9,11,13]:
    for aa in range(-qq-1,qq+2):
        M=Gp.subs({q:qq,a:aa}); ev=[float(e) for e in M.eigenvals(multiple=True)]
        rows.append(dict(q=qq,a=aa,hasse=aa*aa<=4*qq,det=int(M.det()),npos=sum(e>1e-12 for e in ev),nneg=sum(e<-1e-12 for e in ev),nzero=sum(abs(e)<=1e-12 for e in ev)))
ok=all((r['npos']==0)==r['hasse'] for r in rows)
out['iii_neg_semidef_iff_hasse_all_rows']=ok
out['iii_rows']=len(rows)
out['iii_det_positive_but_negative_definite_examples']=[ (r['q'],r['a']) for r in rows if r['det']>0 and r['nneg']==2][:5]
out['iii_det_alone_cannot_tell_sign']='det(-I2)=det(+I2)=1; here det=4q-a^2>0 occurs with signature (0,2); positivity needs inertia/principal minors'
out['iii_boundary_signature']=[int(e) for e in sp.Matrix([[0,1],[1,0]]).eigenvals(multiple=True)]
json.dump(out,open('test1_result.json','w'),indent=1); print(json.dumps(out,indent=1))

"""Scratch reruns of original interval certificates, then verified index/gap of Q=W-P.
Uses the same IEEE double forward-error model and scalar interval arithmetic as t2047.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib, numpy as np, scipy.linalg as la, json, math, mpmath as mp
OUT=pathlib.Path(__file__).parent

def verify(M,construction_error):
 vals,V=la.eigh(M,driver='evd');n=len(vals);u=np.finfo(float).eps/2;gn=n*u/(1-n*u)
 qF=np.linalg.norm(V,'fro')*(1+1e-7);mF=np.linalg.norm(M,'fro')*(1+1e-7)
 G=V.T@V-np.eye(n);Res=M@V-V*vals
 eta=np.linalg.norm(G,'fro')*(1+1e-7)+1e-14+gn*qF*qF+10*u*(qF*qF+n)+1e-12
 rho=np.linalg.norm(Res,'fro')*(1+1e-7)+1e-14+gn*mF*qF+10*u*(mF*qF+qF*np.max(np.abs(vals)))+1e-12
 # Congruence V^T M V = diag(vals) + perturbation; bound needed at threshold c.
 err=eta*np.max(abs(vals))+math.sqrt(1+eta)*rho+construction_error*(1+eta)
 return vals,eta,rho,err

def trial(Aiv,iv,I):
 J=1000;cs=[2*I(j)+I(1,2) for j in range(J)]
 gam=sum((2*(1-iv.exp(-c*Aiv))/(Aiv*c*c) for c in cs),I(0))
 c=2*I(J)+I(1,2);tail=2/Aiv*(1/(c*c)+1/(2*c))
 Ng=1000;hh=sum((I(1,j) for j in range(1,Ng+1)),I(0));g0=hh-iv.log(I(Ng))-I(1,2*Ng)
 gamma=iv.mpf([g0.a,(g0+I(1,12*Ng**2)).b]);K0=-gamma-iv.pi/2-3*iv.log(I(2))-iv.log(iv.pi)
 p=I(0)
 for n,pr in [(2,2),(3,3)]:
  if (iv.log(I(n))).b<Aiv.a:p+=2*iv.log(I(pr))/iv.sqrt(I(n))*(1-iv.log(I(n))/Aiv)
 return K0+gam+iv.mpf([0,tail.b])-p

def run(two=False):
 src=pathlib.Path('../multiprime2047')/('certify_two2047.py' if two else 'certify2047.py')
 oldjson=str(src.with_suffix('.json'));newjson=str(OUT/('base_two_certificate2057.json' if two else 'base_certificate2057.json'))
 g={};exec(compile(src.read_text().replace(oldjson,newjson),str(src),'exec'),g)
 M=g['M'];B=g['Rvec'];kap=float(g['midpoint'](g['kappa']));Q=M-kap*(B@B.T)
 iv=g['iv'];I=g['I'];hI=g['hI'];high=g['high'];c=I(1,2000) if two else I(1,250)
 if two:
  # (h/pi)^2 D/(high-c) is enough for Q cross-block: no penalty moment term.
  alph=1/40000000
  need=(hI/iv.pi)**2/(high-c);assert need.b<I(1,40000000).a
  E=Q-alph*g['Dmat'];construction=1e-6+alph*100+1e-7
 else:
  E=Q;construction=1.1e-6
 vals,eta,rho,err=verify(E,construction)
 cf=float(c.b)
 # Congruence inertia E-cI: all except first positive despite all accounted errors.
 second_lower=(vals[1]-err)/(1+eta)
 assert eta<1e-6
 if two:
  assert vals[1]-cf*(1+eta)-err>0
  margin=second_lower-cf
 else:
  # Norm cross bound for Q: Gamma only. Prime translations preserve partition.
  cross2=g['sc']*g['epsC'];marginI=I(str(second_lower))-c-cross2/(high-c)
  assert marginI.a>I(0).b
  margin=float(marginI.a)
 assert high.a>c.b
 trialI=trial(g['A'],iv,I);assert trialI.b<I(-19,10).a
 # finite Q, full W and constrained inertia, as numerical summaries only
 def sig(v):return [int(sum(v< -1e-9)),int(sum(abs(v)<=1e-9)),int(sum(v>1e-9))]
 Qvals=la.eigvalsh(Q);P=B[:,[0]]@B[:,[1]].T+B[:,[1]]@B[:,[0]].T;wv=la.eigvalsh(Q+P)
 Z=la.qr(B,mode='full')[0][:,2:];cv=la.eigvalsh(Z.T@Q@Z);S=B.T@la.solve(Q,B,assume_a='sym')
 out=dict(A='1.1' if two else '1',cells=len(Q),Gamma_terms=g['J'],finite_minorant_Q_inertia=sig(Qvals),finite_minorant_W_inertia=sig(wv),finite_minorant_constrained_inertia=sig(cv),finite_minorant_Q_first=Qvals[:4].tolist(),finite_minorant_S=la.eigvalsh(S).tolist(),finite_minorant_constrained_min=float(cv[0]),verified_effective_second_lower=second_lower,verified_diagonalization_error=err,verified_eta=eta,verified_rho=rho,construction_error=construction,continuum_Q_index=1,continuum_Q_spectrum_gap_about_zero=cf,constant_trial_Q_interval=str(trialI),continuum_Q_second_spectral_lower=cf,Schur_margin=margin,continuum_S_signature='one positive, one negative; follows exactly from invertibility and constrained coercivity',continuum_E0_lower=cf,all_assertions_passed=True)
 json.dump(out,open(OUT/('certify_two_inertia2057.json' if two else 'certify_inertia2057.json'),'w'),indent=2);print(json.dumps(out,indent=2),flush=True)
 return out
if __name__=='__main__':run(False);run(True)

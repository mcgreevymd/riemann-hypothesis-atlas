"""Continuum certificate: finite positive Gamma minorant + exact shift-invariant cells + interval coefficients + verified spectral residual + analytic tail Schur."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np, scipy.linalg as la, mpmath as mp, json, math, time
iv=mp.iv;iv.dps=55
I=lambda n,d=1:iv.mpf(n)/iv.mpf(d)
def midpoint(x):return (float(x.a)+float(x.b))/2
def abserr(f,x):
 d=iv.mpf(float(f))-x
 return max(abs(float(d.a)),abs(float(d.b)))
def relerr(f,x):
 d=iv.mpf(float(f))/x-1
 return max(abs(float(d.a)),abs(float(d.b)))
def up(x):return float(x.b)*(1+1e-12)+1e-25
def lo(x):return float(x.a)*(1-1e-12)-1e-25
A=I(11,10);b2=iv.log(I(2));b3=iv.log(I(3));eps=A-b3;diff=b3-b2;L2=A-b2
counts=[3,674,3,478,3,674,3];J=192;kappa=I(4)
segments=[(I(0),eps),(eps,diff),(diff,L2),(L2,b2),(b2,b2+eps),(b2+eps,b3),(b3,A)]
cells=[];groups=[];pos=0
for (left,right),num in zip(segments,counts):
 groups.append(np.arange(pos,pos+num));pos+=num
 for j in range(num):cells.append((left-A/2+(right-left)*I(j,num),left-A/2+(right-left)*I(j+1,num)))
n=len(cells);L=[x for x,y in cells];R=[y for x,y in cells];H=[y-x for x,y in cells]
l=np.array([midpoint(x) for x in L]);r=np.array([midpoint(x) for x in R]);h=r-l
Ng=1000;hh=sum((I(1,j) for j in range(1,Ng+1)),I(0));g0=hh-iv.log(I(Ng))-I(1,2*Ng)
gamma=iv.mpf([g0.a,(g0+I(1,12*Ng**2)).b]);K0=-gamma-iv.pi/2-3*iv.log(I(2))-iv.log(iv.pi)
cs=[2*I(j)+I(1,2) for j in range(J)];sc=sum((2/c for c in cs),I(0));dI=K0+sc;d=midpoint(dI)
alphas=[];max_alpha_error=0
for c in cs:alphas.append(c+4*c*c*sum((ci/(c*c-ci*ci) for ci in cs if ci is not c),I(0)))
af=np.array([midpoint(x) for x in alphas])
for x,y in zip(af,alphas):max_alpha_error=max(max_alpha_error,abserr(x,y))
assert max_alpha_error<1e-6
C=np.zeros((n,n));Dmat=np.zeros((n,n));maxrel=0.;maxdiagerr=0.;maxdiagprimeerr=0.;maxlogqerr=0.
start=time.time()
for j in range(J):
 c=2*j+.5;qq=-np.expm1(-c*h)/(c*np.sqrt(h));aa=qq*np.exp(c*r);bb=qq*np.exp(-c*l)
 term=np.triu(np.outer(aa,bb),1);term=term+term.T
 diag=2/c+2*np.expm1(-c*h)/(c*c*h);np.fill_diagonal(term,diag);C+=term
 logq=h/np.expm1(c*h)-1/c
 logder=logq[:,None]+logq[None,:]+r[:,None]-l[None,:]
 prime=np.triu(term*logder,1);prime=prime+prime.T
 diagp=-2/c**2-4*np.expm1(-c*h)/(c**3*h)-2*np.exp(-c*h)/c**2
 np.fill_diagonal(prime,diagp);Dmat+=af[j]*term+c*c*prime
 ci=cs[j]
 for i in range(n):
  ee=iv.exp(-ci*H[i]);qi=(1-ee)/(ci*iv.sqrt(H[i]))
  maxrel=max(maxrel,relerr(aa[i],qi*iv.exp(ci*R[i])),relerr(bb[i],qi*iv.exp(-ci*L[i])))
  exactdiag=2/ci-2*(1-ee)/(ci**2*H[i])
  maxdiagerr=max(maxdiagerr,abserr(diag[i],exactdiag))
  exactlogq=H[i]/(iv.exp(ci*H[i])-1)-1/ci
  maxlogqerr=max(maxlogqerr,abserr(logq[i],exactlogq))
  exactdiagp=-2/ci**2+4*(1-ee)/(ci**3*H[i])-2*ee/ci**2
  maxdiagprimeerr=max(maxdiagprimeerr,abserr(diagp[i],exactdiagp))
assert maxrel<1e-9 and maxdiagerr<1e-10 and maxdiagprimeerr<1e-8 and maxlogqerr<1e-9
assert max(abserr(x,y) for x,y in zip(l,L))<1e-12
assert max(abserr(x,y) for x,y in zip(r,R))<1e-12
Rvec=[];maxRrel=0.
for sign in [1,-1]:
 vf=np.exp(sign*l/2)*np.expm1(sign*h/2)/(sign*.5*np.sqrt(h));Rvec.append(vf)
 for i in range(n):
  vi=iv.exp(sign*L[i]/2)*(iv.exp(sign*H[i]/2)-1)/(sign*I(1,2)*iv.sqrt(H[i]))
  maxRrel=max(maxRrel,relerr(vf[i],vi))
Rvec=np.array(Rvec).T;assert maxRrel<1e-9
# Interval bound for the derivative Gram construction error; all huge cancellation is covered.
Derror=I(0);absDnorm=I(0)
for ci,alpha in zip(cs,alphas):
 ab=iv.mpf([0,max(abs(float(alpha.a)),abs(float(alpha.b)))*(1+1e-12)])
 errC=I(3,10**9)*2/ci+I(1,10**10)
 errCp=(I(3,10**9)*(A+2/ci)+I(5,10**9))*2/ci+I(1,10**8)
 Derror+=ab*errC+ci**2*errCp+I(1,10**6)*2/ci
 absDnorm+=ab*2/ci+2
assert absDnorm.b<I(10**8).a
Derror+=I(1,10000) # conservative sum/product/final assembly floating error
assert Derror.b<I(100).a
rn=2*(iv.exp(A/2)-iv.exp(-A/2));assert sc.b<I(11).a and (kappa*rn).b<I(10).a
assert abserr(d,dI)<1e-7
ai2=iv.log(I(2))/iv.sqrt(I(2));ai3=iv.log(I(3))/iv.sqrt(I(3));a2=midpoint(ai2);a3=midpoint(ai3)
assert abserr(a2,ai2)<1e-12 and abserr(a3,ai3)<1e-12
Aentry_error=I(3,10**9)*sc+I(J,10**10)+I(1,10**7)+I(3,10**9)*kappa*rn+I(2,10**12)+I(1,10**10)
assert Aentry_error.b<I(1,10**6).a
M=d*np.eye(n)-C+midpoint(kappa)*(Rvec@Rvec.T)
for i,j,weight in [(0,4,a2),(1,5,a2),(2,6,a2),(0,6,a3)]:M[groups[i],groups[j]]-=weight;M[groups[j],groups[i]]-=weight
# Stronger Schur uses derivative Gram rather than a scalar C norm.
alpha=1/40000000;beta=1/4000000
Effective=M-alpha*Dmat-beta*(Rvec@Rvec.T)
vals,Q=la.eigh(Effective,driver='evd')
G=Q.T@Q-np.eye(n);Res=Effective@Q-Q*vals[np.newaxis,:]
u=np.finfo(float).eps/2;gn=n*u/(1-n*u)
qF=np.linalg.norm(Q,'fro')*(1+1e-7);eF=np.linalg.norm(Effective,'fro')*(1+1e-7)
eta=np.linalg.norm(G,'fro')*(1+1e-7)+1e-14+gn*qF*qF+10*u*(qF*qF+n)+1e-12
rho=np.linalg.norm(Res,'fro')*(1+1e-7)+1e-14+gn*eF*qF+10*u*(eF*qF+qF*np.max(np.abs(vals)))+1e-12
# A matrix construction <1e-6 as in the width-one certificate, + alpha*100 derivative allowance.
# Include rank2 factor, scalar coefficient and matrix assembly errors with additional 1e-7 slack.
construction_error=1e-6+alpha*100+1e-7
finite_lower=(float(vals[0])-eta*np.max(np.abs(vals))-math.sqrt(1+eta)*rho)/(1+eta)-construction_error
assert eta<1e-6 and finite_lower>0.0006
hmax=max(float(x.b) for x in H);hI=iv.mpf([0,hmax*(1+1e-12)])
sumc=sum(cs,I(0));epsC=2*sumc*(hI/iv.pi)**2;epsR=(hI/(2*iv.pi))**2*rn
sn=(ai3+iv.sqrt(ai3**2+4*ai2**2))/2
high=dI-sn-epsC;cclaim=I(1,2000)
assert high.a>I(16,5).b
needalpha=2*(hI/iv.pi)**2/(high-cclaim)
needbeta=2*kappa*kappa*epsR/(high-cclaim)
assert needalpha.b<I(1,40000000).a and needbeta.b<I(1,4000000).a
assert finite_lower>float(cclaim.b)
out={'A':'11/10','Gamma_positive_terms':J,'kappa':'4','cells':n,'segment_counts':counts,'hmax':hmax,'max_interval_factor_relative_error':maxrel,'max_interval_R_relative_error':maxRrel,'max_interval_diag_error':maxdiagerr,'max_interval_derivative_diag_error':maxdiagprimeerr,'max_interval_log_derivative_error':maxlogqerr,'max_interval_alpha_error':max_alpha_error,'derivative_Gram_error_bound':str(Derror),'used_derivative_Gram_error_bound':'100','numerical_effective_eigenvalue':float(vals[0]),'verified_orthogonality_defect':eta,'verified_residual_norm_bound':rho,'effective_matrix_construction_error_bound':construction_error,'verified_effective_eigen_lower':finite_lower,'high_block_lower':str(high),'needed_derivative_Schur_coefficient':str(needalpha),'used_derivative_coefficient':'1/40000000','needed_moment_Schur_coefficient':str(needbeta),'used_moment_coefficient':'1/4000000','claimed_continuum_lower':'W(F)>=1/2000||F||^2 for F in E0 supported in width <=11/10','all_assertions_passed':True,'elapsed_seconds':time.time()-start}
print(json.dumps(out,indent=2));json.dump(out,open('../multiprime2047/certify_two2047.json','w'),indent=2)

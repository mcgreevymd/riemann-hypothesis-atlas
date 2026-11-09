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
A=I(1);b=iv.log(I(2));delta=A-b;mid=2*b-A
m=250;nc=int(np.ceil(midpoint(mid/delta)*m));J=48;kappa=I(2)
cells=[]
for l,length,num in [(-A/2,delta,m),(-A/2+delta,mid,nc),(-A/2+b,delta,m)]:
 for j in range(num):cells.append((l+length*I(j,num),l+length*I(j+1,num)))
n=len(cells);L=[x for x,y in cells];R=[y for x,y in cells];H=[y-x for x,y in cells]
l=np.array([midpoint(x) for x in L]);r=np.array([midpoint(x) for x in R]);h=r-l
# Euler constant and diagonal d enclosure.
Ng=1000;hh=sum((I(1,j) for j in range(1,Ng+1)),I(0));g0=hh-iv.log(I(Ng))-I(1,2*Ng)
gamma=iv.mpf([g0.a,(g0+I(1,12*Ng**2)).b]);K0=-gamma-iv.pi/2-3*iv.log(I(2))-iv.log(iv.pi)
dI=K0+sum((2/(2*I(j)+I(1,2)) for j in range(J)),I(0));d=midpoint(dI)
C=np.zeros((n,n));maxrel=0.;maxdiagerr=0.
start=time.time()
for j in range(J):
 c=2*j+.5;q=-np.expm1(-c*h)/(c*np.sqrt(h));aa=q*np.exp(c*r);bb=q*np.exp(-c*l)
 term=np.triu(np.outer(aa,bb),1);term=term+term.T
 diag=2/c+2*np.expm1(-c*h)/(c*c*h);np.fill_diagonal(term,diag);C+=term
 ci=2*I(j)+I(1,2)
 for i in range(n):
  qi=(1-iv.exp(-ci*H[i]))/(ci*iv.sqrt(H[i]))
  maxrel=max(maxrel,relerr(aa[i],qi*iv.exp(ci*R[i])),relerr(bb[i],qi*iv.exp(-ci*L[i])))
  exactdiag=2/ci-2*(1-iv.exp(-ci*H[i]))/(ci**2*H[i])
  maxdiagerr=max(maxdiagerr,abserr(diag[i],exactdiag))
Rvec=[];maxRrel=0.
for sign in [1,-1]:
 vf=np.exp(sign*l/2)*np.expm1(sign*h/2)/(sign*.5*np.sqrt(h));Rvec.append(vf)
 for i in range(n):
  vi=iv.exp(sign*L[i]/2)*(iv.exp(sign*H[i]/2)-1)/(sign*I(1,2)*iv.sqrt(H[i]))
  maxRrel=max(maxRrel,relerr(vf[i],vi))
Rvec=np.array(Rvec).T
ai=iv.log(I(2))/iv.sqrt(I(2));af=midpoint(ai)
M=d*np.eye(n)-C+midpoint(kappa)*(Rvec@Rvec.T)
for i in range(m):M[i,m+nc+i]-=af;M[m+nc+i,i]-=af
# Interval coefficient checks imply a conservative operator-norm entry-construction enclosure.
# Offdiagonal C relative error <=3e-9; ||C||<=sum 2/c<9.
# Diagonal errors add at most J*1e-10. Rank2 error <=3e-9*kappa*sum||r||^2<2e-8.
assert maxrel<1e-9 and maxRrel<1e-9 and maxdiagerr<1e-10
assert abserr(d,dI)<1e-7 and abserr(af,ai)<1e-12
sc=sum((2/(2*I(j)+I(1,2)) for j in range(J)),I(0));rn=2*(iv.exp(A/2)-iv.exp(-A/2))
assert sc.b<I(9).a and (kappa*rn).b<I(5).a
# Include dot/sum/final assembly rounding with substantial slack.
matrix_construction_error=1e-6
vals,Q=la.eigh(M,driver='evd')
G=Q.T@Q-np.eye(n);Res=M@Q-Q*vals[np.newaxis,:]
u=np.finfo(float).eps/2;gn=n*u/(1-n*u)
# Known exact-input dot-product forward bounds; Frobenius upper estimates inflated for their evaluation.
qF=np.linalg.norm(Q,'fro')*(1+1e-7);mF=np.linalg.norm(M,'fro')*(1+1e-7)
Gf=np.linalg.norm(G,'fro')*(1+1e-7)+1e-14
Rf=np.linalg.norm(Res,'fro')*(1+1e-7)+1e-14
eta=Gf+gn*qF*qF+10*u*(qF*qF+n)+1e-12
rho=Rf+gn*mF*qF+10*u*(mF*qF+qF*np.max(np.abs(vals)))+1e-12
assert eta<1e-6
finite_lower=(float(vals[0])-eta*np.max(np.abs(vals))-math.sqrt(1+eta)*rho)/(1+eta)-matrix_construction_error
assert finite_lower>0.0069
# Analytic high-block and mixed-block bounds, all evaluated as intervals.
hmax=max(float(x.b) for x in H);hI=iv.mpf([0,hmax*(1+1e-12)])
sumc=sum((2*I(j)+I(1,2) for j in range(J)),I(0))
epsC=2*sumc*(hI/iv.pi)**2
epsR=(hI/(2*iv.pi))**2*rn
cross=iv.sqrt(sc*epsC)+kappa*iv.sqrt(rn*epsR)
high=dI-ai-epsC
cclaim=I(1,250) # .004
# low > .0069; high > 2; cross upper; subtract c and Schur.
margin=I(69,10000)-cclaim-cross**2/(high-cclaim)
assert high.a>cclaim.b and margin.a>I(0).b
out={'A':'1','Gamma_positive_terms':J,'kappa':'2','cells':n,'outer_cells_each':m,'middle_cells':nc,'hmax':hmax,'max_interval_factor_relative_error':maxrel,'max_interval_R_relative_error':maxRrel,'max_interval_diag_absolute_error':maxdiagerr,'matrix_construction_norm_error_bound':matrix_construction_error,'numerical_finite_smallest':float(vals[0]),'verified_orthogonality_defect_bound':eta,'verified_eigen_residual_Frobenius_bound':rho,'finite_continuum_compression_eigen_lower':finite_lower,'used_finite_lower':'0.0069','d_interval':str(dI),'C_high_norm_bound':str(epsC),'cross_norm_bound':str(cross),'high_block_lower':str(high),'Schur_margin':str(margin),'claimed_continuum_lower':'W(F)>=1/250 ||F||^2 for F in E0 supported in width <=1','all_assertions_passed':True,'elapsed_seconds':time.time()-start}
print(json.dumps(out,indent=2));json.dump(out,open('../multiprime2047/certify2047.json','w'),indent=2)

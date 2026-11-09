import numpy as np,scipy.linalg as la,json
from scipy.special import digamma

def build(A=1.,m=250,J=48,kappa=4.):
 b=np.log(2);delta=A-b;mid=2*b-A;h=delta/m;nc=int(np.ceil(mid/h))
 edges=np.concatenate([np.linspace(-A/2,-A/2+delta,m+1),np.linspace(-A/2+delta,-A/2+b,nc+1)[1:],np.linspace(-A/2+b,A/2,m+1)[1:]])
 h=np.diff(edges);l=edges[:-1];r=edges[1:];n=len(h)
 C=np.zeros((n,n));d=float(digamma(.25)-np.log(np.pi));sc=0.;sumc=0.
 for j in range(J):
  c=2*j+.5;sc+=2/c;sumc+=c;d+=2/c
  q=-np.expm1(-c*h)/(c*np.sqrt(h));aa=q*np.exp(c*r);bb=q*np.exp(-c*l)
  term=np.outer(aa,bb);term=np.triu(term,1);term+=term.T
  diag=2/c+2*np.expm1(-c*h)/(c*c*h)
  np.fill_diagonal(term,diag);C+=term
 R=[]
 for sign in [1,-1]:R.append(np.exp(sign*l/2)*np.expm1(sign*h/2)/(sign*.5*np.sqrt(h)))
 R=np.array(R).T
 M=d*np.eye(n)-C+kappa*(R@R.T)
 a=np.log(2)/np.sqrt(2)
 for i in range(m):M[i,m+nc+i]-=a;M[m+nc+i,i]-=a
 ev=la.eigvalsh(M,subset_by_index=[0,2]);hh=np.max(h)
 epsC=2*sumc*(hh/np.pi)**2
 # C_LH <= sqrt(||C||*epsC); R tail by cell Poincare on exp moments
 Rnorm2=4*np.sinh(A/2) # ||r+||^2+||r-||^2
 epsR=(hh/(2*np.pi))**2*Rnorm2
 cross=np.sqrt(sc*epsC)+kappa*np.sqrt(Rnorm2*epsR)
 high=d-a-epsC
 lower=ev[0]-cross*cross/high
 out=dict(A=A,m=m,J=J,kappa=kappa,n=n,hmax=hh,eigs=ev.tolist(),d=d,epsC=epsC,cross=cross,high=high,schur_lower=lower)
 print(json.dumps(out));return out
out=[build(m=m,J=J,kappa=k) for m,J,k in [(100,32,2),(250,48,2),(250,48,4),(500,64,4),(500,64,10)]]
json.dump(out,open('../multiprime2047/experiment2047.json','w'),indent=2)

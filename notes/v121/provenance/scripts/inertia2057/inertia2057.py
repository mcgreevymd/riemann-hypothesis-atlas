import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np, scipy.linalg as la
from scipy.integrate import quad
from scipy.special import digamma
import json, math, pathlib, time
OUT=pathlib.Path(__file__).parent
K0=float(digamma(.25)-np.log(np.pi))
def k(a): return np.exp(-a/2)/(-np.expm1(-2*a))
def ak(a): return .5 if a==0 else a*k(a)
def atoms(A):
 out=[]
 for n in range(2,int(np.exp(A))+1):
  for p in range(2,n+1):
   if any(p%d==0 for d in range(2,int(np.sqrt(p))+1)):continue
   m=n
   while m%p==0:m//=p
   if m==1:
    if np.log(n)<A:out.append((np.log(n),np.log(p)/np.sqrt(n),n))
    break
 return out
def matrix(A,n):
 h=A/n
 diag=K0+2*quad(ak,0,h,epsabs=2e-13)[0]/h+2*quad(k,h,np.inf,epsabs=2e-13)[0]
 col=np.zeros(n);col[0]=diag
 for m in range(1,n):
  a=m*h
  f=lambda x: k(x)*(h-abs(x-a))/h if x>0 else (.5/h if m==1 else 0.)
  col[m]=-quad(f,a-h,a,epsabs=2e-13)[0]-quad(f,a,a+h,epsabs=2e-13)[0]
 for a,w,_ in atoms(A):
  col-=w*(np.maximum(0,1-abs(np.arange(n)*h-a)/h)+np.maximum(0,1-abs(np.arange(n)*h+a)/h))
 Q=la.toeplitz(col);l=-A/2+np.arange(n)*h
 B=np.array([np.exp(s*l/2)*np.expm1(s*h/2)/(s*.5*np.sqrt(h)) for s in [1,-1]]).T
 return Q,B

def inertia(v,tol=1e-9):return [int(sum(v < -tol)),int(sum(abs(v)<=tol)),int(sum(v>tol))]
def analyze(A,n):
 Q,B=matrix(A,n);W=Q+B[:,[0]]@B[:,[1]].T+B[:,[1]]@B[:,[0]].T
 ev,U=la.eigh(Q);ew=la.eigvalsh(W)
 V=la.qr(B,mode='full')[0];Z=V[:,2:];ec=la.eigvalsh(Z.T@Q@Z)
 S=B.T@la.solve(Q,B,assume_a='sym'); sw=B.T@la.solve(W,B,assume_a='sym')
 sb=la.eigvalsh(S);swe=la.eigvalsh(sw)
 overlaps=np.sum((V[:,:2].T@U[:,ev< -1e-9])**2,axis=0)
 return dict(A=A,n=n,active=[x[2] for x in atoms(A)],Q_inertia=inertia(ev),W_inertia=inertia(ew),S_eigenvalues=sb.tolist(),S_W_eigenvalues=swe.tolist(),constrained_inertia=inertia(ec),Q_first=ev[:4].tolist(),W_first=ew[:4].tolist(),constrained_min=float(ec[0]),negative_mode_moment_overlap_squared=overlaps.tolist(),S_inertia=inertia(sb),identity_rhs=int(sum(ev < -1e-9)+sum(sb>1e-9)-2),boundary_compression_eigenvalues=la.eigvalsh(V[:,:2].T@Q@V[:,:2]).tolist())
def main():
 windows=[.5,np.log(2)-1e-5,np.log(2),.694,1.,np.log(3)-1e-5,np.log(3)+1e-5,1.1,np.log(4)-1e-5,np.log(4)+1e-5,1.5,np.log(5)-1e-5,np.log(5)+1e-5,2.,2.5,3.]
 rows=[]
 for n in [128,256,512]:
  for A in windows:
   row=analyze(float(A),n);rows.append(row)
   print(A,n,row['Q_inertia'],row['W_inertia'],row['S_eigenvalues'],row['constrained_min'],flush=True)
 json.dump(dict(method='Exact cell-integral formulas, noninterval scipy quadrature and double eigensolver; numerical only. Inertia tolerance 1e-9; order negative, zero/tolerance, positive.',rows=rows),open(OUT/'inertia2057.json','w'),indent=2)
if __name__=='__main__':main()

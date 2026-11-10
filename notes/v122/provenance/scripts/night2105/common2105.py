"""Shared window model (copied from inertia2057.matrix, with an atom filter and a prime-weight scale for controls)."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np, scipy.linalg as la
from scipy.integrate import quad
from scipy.special import digamma
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
_cache={}
def arch_col(A,n):
    key=(round(A,12),n)
    if key in _cache: return _cache[key].copy()
    h=A/n
    diag=K0+2*quad(ak,0,h,epsabs=2e-13)[0]/h+2*quad(k,h,np.inf,epsabs=2e-13)[0]
    col=np.zeros(n);col[0]=diag
    for m in range(1,n):
        a=m*h
        f=lambda x: k(x)*(h-abs(x-a))/h if x>0 else (.5/h if m==1 else 0.)
        col[m]=-quad(f,a-h,a,epsabs=2e-13)[0]-quad(f,a,a+h,epsabs=2e-13)[0]
    _cache[key]=col.copy()
    return col
def matrix(A,n,drop=(),scale=1.0,M_shift=0.0):
    """Q = H_A - M_A (cell basis). drop: atoms n to delete; scale: multiply every prime weight.
    Deleted atoms are removed from BOTH the off-diagonal atom and (implicitly) M_A, as in the v1.21 sensitivity control."""
    h=A/n
    col=arch_col(A,n)
    for a,w,nn in atoms(A):
        if nn in drop: continue
        col-=scale*w*(np.maximum(0,1-abs(np.arange(n)*h-a)/h)+np.maximum(0,1-abs(np.arange(n)*h+a)/h))
    col[0]+=M_shift
    Q=la.toeplitz(col);l=-A/2+np.arange(n)*h
    B=np.array([np.exp(s*l/2)*np.expm1(s*h/2)/(s*.5*np.sqrt(h)) for s in [1,-1]]).T
    return Q,B
J=np.array([[0.,1.],[1.,0.]])
def inertia(v,tol=1e-9):return [int(sum(v< -tol)),int(sum(abs(v)<=tol)),int(sum(v>tol))]

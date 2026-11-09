import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import simpson
import sympy as sp,json

def run(A,drop=False):
 # Gram in even/odd moment basis cosh(u/2),sinh(u/2)
 gc=A/2+np.sinh(A/2);gs=-A/2+np.sinh(A/2)
 t=np.linspace(0,2000/A,150001);z=.5+1j*t
 # integral cosh and sinh against exp(i t u) via exponentials; stable enough at A>=.5
 C=np.real(2*np.sinh(z*A/2)/z)
 S=np.imag(2*np.sinh(z*A/2)/z)
 cap=(A-C*C/gc-S*S/gs)/np.pi # positive-frequency density cap
 cap=np.maximum(cap,0)
 pp=[]
 for n in range(2,int(np.exp(A))+1):
  if len(sp.factorint(n))==1 and not(drop and n==2):pp.append((n,np.log(next(iter(sp.factorint(n))))/np.sqrt(n)))
 K=np.real(digamma(.25+.5j*t))-np.log(np.pi)
 m=K.copy()
 for n,w in pp:m-=2*w*np.cos(t*np.log(n))
 def bound(lam):return lam-simpson(np.maximum(lam-m,0)*cap,x=t)
 opt=minimize_scalar(lambda l:-bound(l),bounds=(-2,8),method='bounded')
 out={'A':A,'drop2':drop,'lower_bathtub_grid':-opt.fun,'threshold':opt.x,'tail_m_min':float(np.min(m[-1000:])),'prime_atoms':pp}
 print(json.dumps(out));return out
out=[run(A,d) for A in [.5,.7,.75,.8,1,1.25,1.5,2] for d in ([False,True] if A>=.7 else [False])]
json.dump(out,open('../logpoincare2044/probe2044.json','w'),indent=2)

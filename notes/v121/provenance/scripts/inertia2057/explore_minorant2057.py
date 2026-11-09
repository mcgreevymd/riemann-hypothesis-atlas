import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib, numpy as np, scipy.linalg as la
p=pathlib.Path('../multiprime2047/certify2047.py')
s=p.read_text().replace("'../multiprime2047/certify2047.json'","'../inertia2057/base_certificate2057.json'")
exec(compile(s,str(p),'exec'))
Q0=M-2*Rvec@Rvec.T
# Reflection is exact on these symmetric partition cells.
N=n//2; Zodd=np.zeros((n,N));Zeven=np.zeros((n,n-N))
for i in range(N):
 Zodd[i,i]=1/np.sqrt(2);Zodd[n-1-i,i]=-1/np.sqrt(2)
 Zeven[i,i]=Zeven[n-1-i,i]=1/np.sqrt(2)
if n%2:Zeven[N,N]=1
for name,Z in [('odd',Zodd),('even',Zeven)]:
 v=la.eigvalsh(Z.T@Q0@Z)
 print('minorant parity',name,v[:5])
print('base d cross high',d,midpoint(cross),midpoint(high))

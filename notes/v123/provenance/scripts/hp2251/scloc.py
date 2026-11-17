# locate sign changes of the QW even ground state (Legendre/Arb basis)
import sys
from hp import *
rs,M,dps=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
mp.mp.dps=dps; r=mp.mpf(rs); c=cvec(rs,M)
AL,GL,_=cert3.build_L(rs,M,0); n=AL.nrows(); idx=list(range(0,M,2))
A=mp.matrix(n,n)
for i in range(n):
    for j in range(n): A[i,j]=mp.mpf(AL[i,j].mid().str(dps+20,radius=False))+2*c[idx[i]]*c[idx[j]]
E,U=mp.eigsy(A); q=min(range(n),key=lambda i:E[i]); v=[U[a,q] for a in range(n)]
us=[-r/2+r*mp.mpf(i)/4000 for i in range(4001)]; f=legvals(v,idx,r,us)
mx=max(abs(x) for x in f); s=1 if f[2000]>0 else -1
print('lam0',mp.nstr(E[q],8),'f(0)/max',mp.nstr(s*f[2000]/mx,5),'f(edge)/max',mp.nstr(s*f[0]/mx,5))
for i in range(4000):
    if (f[i]>0)!=(f[i+1]>0): print(' sign change at u=',mp.nstr(us[i],6),' |f| nearby/max=',mp.nstr(max(abs(f[max(i-3,0)]),abs(f[min(i+4,4000)]))/mx,3))
print('min f/max (signed)',mp.nstr(min(s*x for x in f)/mx,5))

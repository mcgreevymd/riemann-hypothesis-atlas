import sys, mpmath as mp, sympy as sp
from spring_mp import *
A=sys.argv[1]; K=int(sys.argv[2]); B=build(A,K,constrained=False); m=mats(B); Af=m['A']
Fu=B['Fu']; mom=lambda s: mp.matrix([mp.quad(lambda uu: mp.polyval([R2M(c) for c in sp.Poly(F,u).all_coeffs()],uu)*mp.e**(s*uu/2),[-Af/2,Af/2]) for F in Fu])
a=mom(-1); bb=mom(1); Pm=a*bb.T+bb*a.T
Wn=W(m); E1,_=geneig(Wn,m['G']); E2,_=geneig(Wn+Pm,m['G'])
print(A,K,'free basis: no-pole lowest',[mp.nstr(e,6) for e in E1[:3]],' with pole lowest',[mp.nstr(e,6) for e in E2[:3]])

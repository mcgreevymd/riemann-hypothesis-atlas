# hodge1991 part A: integral structure of M12, residue/boundary map, Eisenstein ideal. RH not proved.
from fractions import Fraction as Fr
from sympy import divisor_sigma, Matrix, gcd, factorint
import json
N=400
def sig(n,r): return int(divisor_sigma(n,r))
def mul(a,b): return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(N+1)]
E4=[1]+[240*sig(n,3) for n in range(1,N+1)]
E6=[1]+[-504*sig(n,5) for n in range(1,N+1)]
E43=mul(mul(E4,E4),E4); E62=mul(E6,E6)
D=[Fr(a-b,1728) for a,b in zip(E43,E62)]; assert all(x.denominator==1 for x in D); D=[int(x) for x in D]
E12=[Fr(1)]+[Fr(65520,691)*sig(n,11) for n in range(1,N+1)]
G12=[Fr(691,65520)]+[Fr(sig(n,11)) for n in range(1,N+1)]   # -B12/24 = 691/65520
out={}
# basis of M12(Z): {E4^3, Delta} (unimodular: constant/q^1 triangular)
# 691 E12 = 691 E4^3 + c Delta
c=65520-691*720
assert all(691*E12[n]==691*E43[n]+c*D[n] for n in range(N+1))
out['691E12 = 691E4^3 + c*Delta, c']=c
out['E6^2 = E4^3 - 1728 Delta']=all(E62[n]==E43[n]-1728*D[n] for n in range(N+1))
# saturated Hecke lines: Eis = Z*(691E12) primitive (coords (691,c)), cusp = Z*Delta (0,1)
out['gcd(691,c)']=int(gcd(691,c))
out['index [M12(Z): Z(691E12)+Z Delta]']=abs(Matrix([[691,0],[c,1]]).det())
# residue (constant term) map a0: M12(Z)->Z surjective (a0(E4^3)=1); restricted to Eisenstein line image 691Z
out['a0 on primitive Eisenstein vector']=691
# mod 691 reduction of the primitive Eisenstein vector is a cusp form: 691E12 = c*Delta mod 691
out['c mod 691']=c%691; out['65520 mod 691']=65520%691
out['691E12 == c Delta (mod 691) coefficientwise n<=400']=all((691*E12[n]-c*D[n])%691==0 for n in range(N+1))
# Eisenstein ideal: gcd_n (tau(n)-sigma11(n))
g=0
for n in range(1,N+1): g=gcd(g,D[n]-sig(n,11))
out['gcd_{n<=400}(tau(n)-sigma11(n))']=int(g)
# normalized integral G12: G12 = (691/65520)E12 ; G12 - Delta has constant 691/65520 and coefficients sigma11-tau == 0 mod 691
out['G12-Delta: all n>=1 coeffs divisible by 691']=all((sig(n,11)-D[n])%691==0 for n in range(1,N+1))
# Hecke T2 on basis (E4^3, Delta): integral matrix; Hecke algebra on M12(Z) = {(a,b): a==b mod 691}
def T2(f): return [f[2*n]+(2**11*f[n//2] if n%2==0 else 0) for n in range(N//2)]
def coords(f): # in basis E43, D
    a=Fr(f[0]); b=Fr(f[1])-a*720; return a,b
t1=coords(T2(E43)); t2=coords(T2(D))
out['T2 matrix on (E4^3,Delta) columns']=[[str(t1[0]),str(t2[0])],[str(t1[1]),str(t2[1])]]
out['T2 eigen: sigma11(2), tau(2)']=[sig(2,11),D[2]]
out['sigma11(2)-tau(2) factor']=str(factorint(sig(2,11)-D[2]))
json.dump(out,open('m12_lattice1991.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))

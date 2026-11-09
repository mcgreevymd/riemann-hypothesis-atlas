# Explicit-formula decomposition of the diagonal counterterm M_A (RH not assumed in the identity; zero sum symmetric).
import mpmath as mp, json
from sympy import factorint
mp.mp.dps=20
K0=mp.digamma(0.25)-mp.log(mp.pi)
def a(n):
    f=factorint(n); return mp.log(list(f)[0])/mp.sqrt(n) if len(f)==1 else 0
def M(A): return -K0+2*mp.fsum(a(n) for n in range(2,int(mp.e**A)+1) if mp.log(n)<A)
def pole(A): return 4*mp.e**(A/2)
def gam(A): return 2*mp.nsum(lambda k: mp.e**(-(2*k+0.5)*A)/(2*k+0.5),[1,mp.inf])
NZ=400
import os
if os.path.exists("zeros400.json"): gs=[mp.mpf(x) for x in json.load(open("zeros400.json"))]
else:
    gs=[mp.im(mp.zetazero(n)) for n in range(1,NZ+1)]; json.dump([str(g) for g in gs],open("zeros400.json","w"))
def zer(A,N): return -4*mp.fsum(mp.sin(g*A)/g for g in gs[:N])
out={'identity':'M_A = 2(S_A - S_reg) = 4e^{A/2} - 2 sum_rho e^{A(rho-1/2)}/(rho-1/2) + 2 sum_{k>=1} e^{-(2k+1/2)A}/(2k+1/2); on-line zeros give -4 sum_{gamma>0} sin(gamma A)/gamma',
     'zeros_used':NZ,'rows':[]}
for A in (0.6,1.0,1.5,2.0,2.5,3.0):
    m=M(A); p=pole(A); g=gam(A); resid=m-p-g
    z1,z2=zer(A,NZ//2),zer(A,NZ)
    out['rows'].append({'A':A,'M_A':str(m),'pole_4e^{A/2}':str(p),'gamma_tail':str(g),
        'zero_part_required=M-pole-gamma':str(resid),'zero_sum_200':str(z1),'zero_sum_400':str(z2)})
json.dump(out,open('ma_explicit1990.json','w'),indent=1); print(json.dumps(out,indent=1))

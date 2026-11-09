# Derived (Tor) self-intersection of a regular Cartier divisor and calibration examples. EXACT (sympy rationals).
import sympy as sp, json
g,d=sp.symbols('g d',integer=True); out={}
chi_curve=lambda deg,genus: deg+1-genus          # RR on a smooth projective curve
# D smooth curve of genus gD on a surface; Koszul 0->O(-D)->O->O_D->0 tensored with O_D:
#   Tor_0 = O_D,  Tor_1 = O_D(-D) = N^dual (deg -D^2),  Tor_i = 0 for i>=2 ;  [O_D (x)^L O_D] = [O_D] - [N^dual] in K_0(D)
def derived_self(D2,gD): return sp.simplify(chi_curve(0,gD)-chi_curve(-D2,gD))
out['chi(O_D (x)^L O_D) = chi(O_D) - chi(N^dual)']=str(derived_self(d,g))+'  (= D^2 for any genus)'
# diagonal of C x C: N_Delta = T_C, deg 2-2g ; conormal = Omega_C
out['diagonal: chi(O_C) - chi(Omega_C)']=str(sp.expand(chi_curve(0,g)-chi_curve(2*g-2,g)))
ex={}
ex['Delta in P1xP1 (g=0)']=chi_curve(0,0)-chi_curve(-2,0)
ex['Delta in ExE (g=1)']=chi_curve(0,1)-chi_curve(0,1)
ex['Delta in CxC, g=2']=chi_curve(0,2)-chi_curve(2,2)
ex['fibre h=pt x P1 in P1xP1 (N^dual=O)']=chi_curve(0,0)-chi_curve(0,0)
ex['(-1)-curve E on Bl_p P2 (N^dual=O(1))']=chi_curve(0,0)-chi_curve(1,0)
ex['ample (1,1) curve (= Delta class) in P1xP1']=chi_curve(0,0)-chi_curve(-2,0)
out['derived self-intersections']={k:int(v) for k,v in ex.items()}
# transverse h.v in P1xP1, local ring k[x,y]: Tor_0(k[x,y]/(x),k[x,y]/(y)) = k, Tor_1 = ker(x on k[y]) = 0 -> 1
out['h.v local Tor lengths']=[1,0]
# Non-regular ambient: A=k[x,y]/(xy), M=A/(x), N=A/(y)=k[x]; periodic resolution ...A -y-> A -x-> A -> M ; tensor N: maps x (injective on k[x]), 0, x, 0, ...
# Tor_0 = k[x]/x = k ; Tor_odd = ker x / im 0 = 0 ; Tor_even>=2 = ker 0 / im x = k  -> infinitely many nonzero Tor: Serre chi undefined
tor=[]
for i in range(8):
    if i==0: tor.append(1)
    elif i%2==1: tor.append(0)
    else: tor.append(1)
out['A=k[x,y]/(xy): length Tor_i(A/x,A/y), i=0..7']=tor
# sections vs c1: O(-1) on P1 ; P1xP1 bundles O(a,b): h^i by Kunneth
def h_P1(a): return (a+1 if a>=0 else 0, -a-1 if a<=-2 else 0)
def h_P1xP1(a,b):
    A=h_P1(a);B=h_P1(b); return (A[0]*B[0], A[0]*B[1]+A[1]*B[0], A[1]*B[1])
out['O(-1) on P1: c1, h0, h1, chi']=[-1,*h_P1(-1),h_P1(-1)[0]-h_P1(-1)[1]]
tab={}
for (a,b) in [(1,-3),(-1,-1),(-2,-2),(-3,-3),(2,2),(1,0)]:
    h=h_P1xP1(a,b); tab[f'O({a},{b})']=dict(D2=2*a*b,h=h,chi=h[0]-h[1]+h[2],chi_RR=(a+1)*(b+1))
out['P1xP1 cohomology (Kunneth)']=tab
out['note']='O(-3,-3): D^2=18>0, h0=0, h2=4: effectivity comes from -D (h2=h0(K-D)); chi alone never gives h0.'
json.dump(out,open('tor2002.json','w'),indent=1); print(json.dumps(out,indent=1))

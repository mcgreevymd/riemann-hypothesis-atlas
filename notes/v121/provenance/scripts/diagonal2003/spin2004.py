# t2004: spin / spin^c bookkeeping on concrete surfaces. Exact integer/symbolic checks.
import sympy as sp, numpy as np, json
c1,c2,x=sp.symbols('c1 c2 x'); r={}
# (1) e^{c1/2} Ahat = Td in degree<=4 on a surface: Ahat=1-p1/24, p1=c1^2-2c2
expo=1+c1/2+c1**2/8; Ah=1-(c1**2-2*c2)/24
t=sp.symbols('t'); deg4=sp.expand((expo*Ah).subs({c1:t*c1,c2:t**2*c2},simultaneous=True)).coeff(t,2)
r['deg4_e^{c1/2}Ahat']=str(sp.simplify(deg4)); r['Td2']=str((c1**2+c2)/12)
r['spinc_equals_Todd']=bool(sp.simplify(deg4-(c1**2+c2)/12)==0)
# (2) P2: c1=3H, c2=3, H^2=1. index(spin^c canonical twisted O(n)) = int e^{nH} Td = chi(O(n))
n=sp.symbols('n')
idx=sp.expand(n**2/2+n*sp.Rational(3,2)+(9+3)/sp.Integer(12))
r['P2_index_O(n)']=str(sp.factor(idx)); r['P2_matches_(n+1)(n+2)/2']=bool(sp.simplify(idx-(n+1)*(n+2)/2)==0)
r['P2_w2']='c1=3H odd -> w2=H mod 2 !=0 (Wu: H.H=1 odd); non-spin although H ample'
# (3) lattices
U=np.array([[0,1],[1,0]])
E8=np.array([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],[0,0,-1,2,-1,0,0,0],
             [0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]])
def bd(*Ms):
    N=sum(M.shape[0] for M in Ms); A=np.zeros((N,N),int); i=0
    for M in Ms: k=M.shape[0]; A[i:i+k,i:i+k]=M; i+=k
    return A
def info(A):
    ev=np.linalg.eigvalsh(A.astype(float)); return dict(rank=len(A),sig=(int((ev>0).sum()),int((ev<0).sum())),
        det=int(round(np.linalg.det(A.astype(float)))),even=bool(all(A[i,i]%2==0 for i in range(len(A)))),
        sigma=int((ev>0).sum()-(ev<0).sum()))
K3=bd(U,U,U,-E8,-E8); Enr=bd(U,-E8); P1P1=U; P2=np.array([[1]])
r['P1xP1']=info(P1P1); r['K3']=info(K3); r['Enriques_free']=info(Enr); r['P2']=info(P2); r['E8']=info(E8)
# Rokhlin: closed smooth spin 4-manifold => 16 | sigma
r['Rokhlin_K3_sigma_mod16']=r['K3']['sigma']%16
r['Enriques_sigma']=r['Enriques_free']['sigma']; r['Enriques_not_spin_by_Rokhlin']=r['Enriques_free']['sigma']%16!=0
# K3 primitive complement of ample H=e+f (H^2=2) in first U
H=np.zeros(22); H[0]=H[1]=1
B=np.linalg.svd(np.array([H@K3]))[2][1:]          # basis of H^perp (real)
G=B@K3@B.T; ev=np.linalg.eigvalsh(G); r['K3_Hperp_sig']=(int((ev>1e-9).sum()),int((ev<-1e-9).sum()))
r['K3_note']='H^perp sig (2,19); real primitive (1,1) part sig (0,19) negative by Hodge-Riemann (Hodge type), not by spin'
# (4) spin Dirac index = chi(K^{1/2}) = -sigma/8 (Ahat genus)
r['P1xP1_chi_O(-1,-1)']=0; r['P1xP1_Ahat=-sigma/8']=-r['P1xP1']['sigma']/8
r['K3_chi_O']=2; r['K3_Ahat=-sigma/8']=-r['K3']['sigma']/8
# (5) Wu / RR integrality / adjunction parity on P1xP1 and P2
rows=[]
for a in range(-3,4):
  for b in range(-3,4):
    D2=2*a*b; DK=-2*a-2*b; rows.append((a,b,D2,(D2-DK)//2,(D2+DK)%2,(D2-DK)%2==0))
r['P1xP1_RR_integral_all']=all(t[5] for t in rows); r['P1xP1_D2+DK_even_all']=all(t[4]==0 for t in rows)
r['P2_Wu']=[(d, (d*d-d*(-3))%2) for d in range(-3,4)]   # D^2-D.K = d^2+3d even always
# (6) diagonal parity: Delta^2 = 2-2g even; sign by genus
r['Delta2_by_g']={g:2-2*g for g in range(4)}
# (7) the w2-mod-2 vs free lattice: Enriques K is 2-torsion, invisible to the free lattice U+E8(-1) (even)
r['Enriques_note']='free H^2 even unimodular (1,9) yet w2=K mod 2 !=0 (torsion); sigma=-8 not div by 16 confirms non-spin'
json.dump(r,open('spin2004.json','w'),indent=1,default=str); print(json.dumps(r,indent=1,default=str))

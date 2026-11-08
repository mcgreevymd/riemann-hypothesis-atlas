# map1965: graph-of-flow (Lefschetz/Castelnuovo) map, ledger checks, FF calibration, Hodge-index signature test. Scratch, uncertified.
import numpy as np, mpmath as mp, json
from scipy.integrate import quad
out={}
# ---- 1. archimedean transverse fixed-point weight on R*: u=eps*e^a, |u|^{1/2}/|1-u| summed over eps=+-1  vs 2k(|a|)
k=lambda a: np.exp(-a/2)/(1-np.exp(-2*a))
chk=[]
for a in [-2.3,-0.4,0.1,0.7,3.0]:
    lhs=sum(np.exp(a/2)/abs(1-e*np.exp(a)) for e in [1,-1]); chk.append(lhs-2*k(abs(a)))
out['arch_lefschetz_resid']=max(map(abs,chk))
# ---- 2. counterterm as finite part of identity (non-transverse) component: K0 = -(log 2pi + gamma + FP int_0^inf 2k)
eps=1e-7
I=quad(lambda a: 2*k(a)-np.exp(-2*a)/a,eps,np.inf,limit=400)[0]+float(mp.e1(2*eps))
FP=I-(-np.log(2*eps)-np.euler_gamma)   # drop the log(1/eps) divergence: E1(2eps)= -gamma-log(2eps)+O(eps)
FP=I+np.log(eps)                        # Hadamard finite part w.r.t. log(1/eps)
K0=float(mp.digamma(0.25)-mp.log(mp.pi))
out['K0']=K0; out['FP_int_2k']=FP; out['-(log2pi+gamma+FP)']=-(np.log(2*np.pi)+np.euler_gamma+FP)
# ---- 3. function-field calibration: E: y^2=x^3+x+1 over F_5 (genus 1)
q=5; pts=1+sum(1+ (0 if (x**3+x+1)%q==0 else (1 if pow((x**3+x+1)%q,(q-1)//2,q)==1 else -1)) for x in range(q))
t=q+1-pts; al=(t+np.sqrt(complex(t*t-4*q)))/2; alphas=[al,np.conj(al)]; g=1
N=lambda kk: q**kk+1-sum(a**kk for a in alphas).real
K=12
G=np.array([[ (2-2*g) if m==n else q**(-abs(m-n)/2)*N(abs(m-n)) for n in range(K)] for m in range(K)])  # gamma_m.gamma_n
Wff=-G
ev=np.linalg.eigvalsh(Wff)
hvec=np.array([q**(n/2) for n in range(K)]); vvec=np.array([q**(-n/2) for n in range(K)])
B=np.linalg.qr(np.stack([hvec,vvec],1),mode='complete')[0][:,2:]   # orthonormal basis of primitive sector
evp=np.linalg.eigvalsh(B.T@Wff@B)
# check -I = sum_i |sum c beta_i^n|^2 on random primitive c
c=B@np.random.default_rng(0).standard_normal(K-2)
beta=[a/np.sqrt(q) for a in alphas]
out['FF']=dict(q=q,points=pts,trace=t,alpha_abs=abs(al),N=[N(j) for j in range(1,6)],
  n_neg_full=int((ev<-1e-9).sum()),n_pos_full=int((ev>1e-9).sum()),n_zero_full=int((abs(ev)<=1e-9).sum()),
  rank=int(np.linalg.matrix_rank(G,1e-8)),prim_min=float(evp.min()),prim_max=float(evp.max()),
  hodge_identity_resid=float(c@Wff@c-sum(abs(np.sum(c*b**np.arange(K)))**2 for b in beta)),
  M_FF=-(2-2*g)+2*sum(q**(-j/2)*N(j) for j in range(1,K)))
# ---- 4. Q window Gram: full window W (pole form included) and E0 compression; Hodge-index signature
A=2.0; ns={2:np.log(2)/np.sqrt(2),3:np.log(3)/np.sqrt(3),4:np.log(2)/2,5:np.log(5)/np.sqrt(5),7:np.log(7)/np.sqrt(7)}
J=40; Nu=4001; u=np.linspace(0,A,Nu); du=u[1]-u[0]; w=np.full(Nu,du); w[0]=w[-1]=du/2
Phi=np.array([np.sqrt(2/A)*np.sin(j*np.pi*u/A) for j in range(1,J+1)])
def Tmat(a):   # <phi_i, T_a phi_j>, T_aF(u)=F(u-a)
    S=np.array([np.interp(u-a,u,p,left=0,right=0) for p in Phi]); M=(Phi*w)@S.T; return (M+M.T)/2
M0=(Phi*w)@Phi.T
ag=np.linspace(0,A,801)[1:]; da=ag[1]-ag[0]
Earch=np.zeros((J,J))
for a in ag: Earch+=2*k(a)*(M0-Tmat(a))*da    # midpoint-ish; integrand O(a) near 0
Earch+=2*quad(k,A,np.inf)[0]*M0
Wp=-2*sum(c_*Tmat(np.log(n)) for n,c_ in ns.items())
evm=(Phi*w)@np.exp(-u/2); evp_=(Phi*w)@np.exp(u/2)
P=np.outer(evm,evp_)+np.outer(evp_,evm)          # 2ab symmetrized
Wq=P+K0*M0+Earch+Wp
e=np.linalg.eigh(Wq); Bq=np.linalg.qr(np.stack([evm,evp_],1),mode='complete')[0][:,2:]
e0=np.linalg.eigvalsh(Bq.T@Wq@Bq)
vneg=e[1][:,0]; Ub=np.linalg.qr(np.stack([evm,evp_],1))[0]
out['Q']=dict(A=A,J=J,eig_full_lowest=e[0][:4].tolist(),n_neg_full=int((e[0]<0).sum()),
  E0_min=float(e0.min()),E0_next=float(np.sort(e0)[1]),
  neg_vec_overlap_with_pole_plane=float(np.linalg.norm(Ub.T@vneg)),
  neg_vec_FE_parity=float(vneg@ (np.array([(-1)**(j+1) for j in range(1,J+1)])*vneg)))  # sine basis: u->A-u parity (-1)^(j+1)
json.dump(out,open('map1965.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))

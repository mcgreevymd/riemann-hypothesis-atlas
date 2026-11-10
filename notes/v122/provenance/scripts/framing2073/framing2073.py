"""t2073 scratch: 2x2 pairings of h_sym=2cosh(u/2), h_asym=2sinh(u/2) under Q, P, W, I=-Q,
as L2 functions (cell projection) and as Q-Riesz lifts. Reuses inertia2057.matrix (exact-form Galerkin Q, B).
NUMERICAL (double precision Galerkin) unless labelled EXACT/closed form."""
import os, sys, json, pathlib
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'../inertia2057')
import numpy as np, scipy.linalg as la
from scipy.integrate import quad
from inertia2057 import matrix, atoms, K0, k
OUT=pathlib.Path(__file__).parent
T=np.array([[1.,1.],[1.,-1.]])   # columns: sym=(1,1), asym=(1,-1) in (r+,r-) coords
J=np.array([[0.,1.],[1.,0.]])

def closed(A):
    L=A/2; s=2*np.sinh(L)
    Cp_sym=s+A; Cm_sym=s+A; Cp_asym=s-A; Cm_asym=A-s
    return dict(C_plus_sym=Cp_sym,C_minus_sym=Cm_sym,C_plus_asym=Cp_asym,C_minus_asym=Cm_asym,
        P_sym_sym=2*Cp_sym*Cm_sym, P_asym_asym=2*Cp_asym*Cm_asym, P_sym_asym=Cp_sym*Cm_asym+Cm_sym*Cp_asym,
        norm2_sym=4*(np.sinh(L)+L), norm2_asym=4*(np.sinh(L)-L))

def overlap(par,a,L):
    """<E h, T_a E h> for h=2cosh(u/2) (par=+1) or 2sinh(u/2) (par=-1) on [-L,L], 0<=a. EXACT closed form."""
    if a>=2*L: return 0.
    return 4*(np.sinh(L-a/2)+par*(L-a/2)*np.cosh(a/2))

def Q_continuum(A,par):
    """Q(h,h)=K0||h||^2+int_0^inf k(a)||(I-T_a)Eh||^2 da - 2 sum a_n <h,T_{log n}h>; Gamma integral by quad."""
    L=A/2; n2=overlap(par,0,L)
    f=lambda a: k(a)*2*(n2-overlap(par,a,L))
    g=quad(f,0,2*L,limit=400,epsabs=1e-13,points=[min(1e-6,L)])[0]+2*n2*quad(k,2*L,np.inf,epsabs=1e-14)[0]
    pr=sum(2*w*overlap(par,a,L) for a,w,_ in atoms(A))
    return K0*n2+g-pr

def analyze(A,n,rng):
    Q,B=matrix(A,n); P=B@J@B.T; W=Q+P; I=-Q
    # (i) L2 projection of h onto orthonormal cell basis: coeffs = B @ coords  (B[:,0]=<r+,e_i>, B[:,1]=<r-,e_i>)
    H=B@T                      # columns: projected h_sym, h_asym (also = discrete Riesz functional vectors v_sym,v_asym)
    Hn=H/np.linalg.norm(H,axis=0)
    M=lambda X,Y: X.T@Y
    out=dict(A=A,n=n,active=[x[2] for x in atoms(A)])
    for name,Mat in [('Q',Q),('P',P),('W',W),('I',I)]:
        out[name+'_raw']=(H.T@Mat@H).tolist(); out[name+'_unit']=(Hn.T@Mat@Hn).tolist()
    out['proj_norm2']=(np.linalg.norm(H,axis=0)**2).tolist()
    # parity: exchange matrix commutes with Q?
    R=np.eye(n)[::-1]; out['parity_commutator']=float(np.abs(R@Q-Q@R).max())
    out['parity_of_h']=[float(np.abs(R@H[:,0]-H[:,0]).max()),float(np.abs(R@H[:,1]+H[:,1]).max())]
    ev,U=la.eigh(Q); out['Q_first3']=ev[:3].tolist(); out['Q_neg_count']=int((ev<-1e-9).sum())
    u0=U[:,0]; out['neg_vec_parity_even_resid']=float(np.abs(R@u0-u0).max()*np.sign(1))
    out['cos_negvec_hsym']=float(abs(u0@Hn[:,0])); out['cos_negvec_hasym']=float(abs(u0@Hn[:,1]))
    out['cos_negvec_constant']=float(abs(u0.sum())/np.sqrt(n))
    out['rayleigh_unit']=[float(Hn[:,j]@Q@Hn[:,j]) for j in (0,1)]
    # (2) eigenvector test
    res=[]
    for j in (0,1):
        h=Hn[:,j]; Qh=Q@h; lam=h@Qh; res.append(dict(rayleigh=float(lam),rel_resid=float(np.linalg.norm(Qh-lam*h)/np.linalg.norm(Qh))))
    out['eigvec_test']=res
    # (3) I-orthogonality to E0 (discrete), unit h
    V=la.qr(B,mode='full')[0]; Z=V[:,2:]
    out['E0_L2_orth_of_h']=float(np.abs(Z.T@H).max())
    out['max_I_E0_hsym_unit']=float(np.linalg.norm(Z.T@(I@Hn[:,0])))
    out['max_I_E0_hasym_unit']=float(np.linalg.norm(Z.T@(I@Hn[:,1])))
    # (4) Riesz lifts
    Qi_B=la.solve(Q,B,assume_a='sym'); S=B.T@Qi_B; Ssa=T.T@S@T
    out['S_rpm']=S.tolist(); out['S_symasym']=Ssa.tolist()
    sv=la.eigvalsh(S); out['S_eig']=sv.tolist(); out['S_inertia']=[int((sv<0).sum()),int((sv>0).sum())]
    out['I_Hsym_Hsym']=float(-Ssa[0,0]); out['I_Hasym_Hasym']=float(-Ssa[1,1]); out['I_Hsym_Hasym']=float(-Ssa[0,1])
    Hs=Qi_B@T
    out['W_Hsym_Hsym']=float(Hs[:,0]@W@Hs[:,0]); out['W_Hasym_Hasym']=float(Hs[:,1]@W@Hs[:,1])
    out['P_Hsym_Hsym']=float(Hs[:,0]@P@Hs[:,0]); out['P_Hasym_Hasym']=float(Hs[:,1]@P@Hs[:,1])
    out['cos_negvec_Hsym']=float(abs(u0@Hs[:,0])/np.linalg.norm(Hs[:,0]))
    # tautology I(F,H_sym) = -(C+(F)+C-(F))
    F=rng.standard_normal((n,5)); lhs=-(F.T@Q@Hs[:,0]); rhs=-(F.T@B).sum(1)
    out['riesz_identity_relerr']=float(np.abs(lhs-rhs).max()/np.abs(rhs).max())
    # constrained inertia
    out['Q_E0_min']=float(la.eigvalsh(Z.T@Q@Z)[0])
    return out

def main(windows,ns,tag):
    rng=np.random.default_rng(2073); rows=[]
    for A in windows:
        c=closed(A); cq=[Q_continuum(A,+1),Q_continuum(A,-1)]
        for n in ns:
            r=analyze(A,n,rng); r['closed']=c; r['Q_continuum_diag_raw']=cq
            rows.append(r)
            print(f"A={A:.4f} n={n} Qraw diag={np.diag(r['Q_raw'])} (cont {cq}) off={r['Q_raw'][0][1]:.2e} "
                  f"cosneg={r['cos_negvec_hsym']:.5f} eigres={r['eigvec_test'][0]['rel_resid']:.3f} "
                  f"E0I={r['max_I_E0_hsym_unit']:.3f} S_eig={r['S_eig']} IHs={r['I_Hsym_Hsym']:.4g} IHa={r['I_Hasym_Hasym']:.4g} Wneg?{r['W_Hsym_Hsym']:.3g}",flush=True)
    json.dump(dict(notice='NUMERICAL Galerkin (inertia2057.matrix) except closed forms; no RH/Hodge/positivity claim',rows=rows),
              open(OUT/f'framing2073{tag}.json','w'),indent=1,default=float)
if __name__=='__main__':
    main([0.5,0.694,1.0,1.1,np.log(4)-1e-5,1.386,2.0,3.0],[256,512,1024],'')

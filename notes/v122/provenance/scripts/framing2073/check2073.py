"""Independent rerun/checks for t2073: closed forms vs Galerkin, Woodbury identity S=-(I-J R^{-1})^{-1} J with R=B^T W^{-1} B,
W spectrum, Riesz-lift norms vs n, and the JSON from framing2073.py recomputed at A=1,1.1."""
import os,sys,json,pathlib
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'../inertia2057'); sys.path.insert(0,str(pathlib.Path(__file__).parent))
import numpy as np, scipy.linalg as la
from inertia2057 import matrix
from framing2073 import closed, Q_continuum, analyze, T, J
OUT=pathlib.Path(__file__).parent
old={(r['A'],r['n']):r for r in json.load(open(OUT/'framing2073.json'))['rows']}
rows=[]; rng=np.random.default_rng(7)
for A in [0.5,1.0,1.1,2.0,3.0]:
  for n in [256,512,1024]:
    Q,B=matrix(A,n); P=B@J@B.T; W=Q+P; H=B@T; c=closed(A)
    # closed forms: C+-(h) = (B^T H) rows; P 2x2
    CB=B.T@H; Cex=np.array([[c['C_plus_sym'],c['C_plus_asym']],[c['C_minus_sym'],c['C_minus_asym']]])
    Pex=np.array([[c['P_sym_sym'],c['P_sym_asym']],[c['P_sym_asym'],c['P_asym_asym']]])
    # note: cell projection preserves C+- exactly (r+- lie in span? no) -> report discrepancy
    wv,WU=la.eigh(W); R=B.T@la.solve(W,B,assume_a='sym'); S=B.T@la.solve(Q,B,assume_a='sym')
    Spred=-la.solve(np.eye(2)-J@la.inv(R),J)
    Hs=la.solve(Q,H,assume_a='sym')
    row=dict(A=A,n=n,C_rel_err_proj_vs_exact=float(np.abs(CB-Cex).max()/np.abs(Cex).max()),
      norm2_proj_vs_exact=[float(H[:,0]@H[:,0]/c['norm2_sym']-1),float(H[:,1]@H[:,1]/c['norm2_asym']-1)],
      P_rel_err=float(np.abs(H.T@P@H-Pex).max()/np.abs(Pex).max()),
      W_min3=wv[:3].tolist(),R_eig=la.eigvalsh(R).tolist(),woodbury_relerr=float(np.abs(S-Spred).max()),
      S_plus_J=(S+J).tolist(),
      I_Hsym_pred=float(2+(J@[1,1])@la.solve(R,J@[1,1])),I_Hasym_pred=float(-2+(J@[1,-1])@la.solve(R,J@[1,-1])),
      L2norm_Hsym=float(np.linalg.norm(Hs[:,0])),L2norm_Hasym=float(np.linalg.norm(Hs[:,1])),
      Hsym_boundary_mass_frac=float((Hs[:n//16,0]**2).sum()+(Hs[-n//16:,0]**2).sum())/float(Hs[:,0]@Hs[:,0]),
      W_Hsym=float(Hs[:,0]@W@Hs[:,0]),W_Hasym=float(Hs[:,1]@W@Hs[:,1]))
    if (A,n) in old and A in (1.0,1.1) and n in (512,1024):
      r=analyze(A,n,rng); o=old[(A,n)]
      for key in ['Q_raw','P_raw','S_eig','I_Hsym_Hsym','I_Hasym_Hasym','cos_negvec_hsym','max_I_E0_hsym_unit']:
        assert np.allclose(r[key],o[key],rtol=1e-9,atol=1e-12),key
      assert r['parity_commutator']<1e-12 and r['riesz_identity_relerr']<1e-8 and r['Q_neg_count']==1
      assert r['E0_L2_orth_of_h']<1e-12
      row['rerun_matches_json']=True
    rows.append(row); print(json.dumps(row),flush=True)
json.dump(dict(notice='NUMERICAL',rows=rows),open(OUT/'check2073.json','w'),indent=1)
print('CHECK DONE')

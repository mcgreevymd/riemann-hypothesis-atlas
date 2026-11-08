import numpy as np, runpy, json, mpmath as mp
ns=runpy.run_path('map1965.py')
Bq=ns['K0']*ns['M0']+ns['Earch']+ns['Wp']; eb=np.linalg.eigvalsh(Bq)
J=ns['J']; A=ns['A']
# zeros of zeta up to band edge ~ J*pi/A
T=J*np.pi/A; nz=int(mp.nzeros(T))
# W-predicted (RH form) for the bulk-null cluster: W(F)=sum_gamma |Fhat(gamma)|^2 (normalization 1/(2pi)*2pi?) -> compute for eigvecs
gam=[float(mp.zetazero(k).imag) for k in range(1,nz+8)]
u=ns['u']; w=ns['w']; Phi=ns['Phi']
E=np.linalg.eigh(Bq)
def zero_side(c):
    F=c@Phi; return sum(2*abs(np.sum(w*F*np.exp(-1j*g*u)))**2 for g in gam)  # +-gamma
zs=[zero_side(E[1][:,i]) for i in range(12)]
r=dict(eigs=eb[:16].tolist(),n_small=int((abs(eb)<5e-3).sum()),band_T=T,N_T=nz,zero_side_first12=zs)
json.dump(r,open('cluster1965.json','w'),indent=1); print(json.dumps(r,indent=1))

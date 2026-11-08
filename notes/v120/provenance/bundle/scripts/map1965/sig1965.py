# Hodge-index signature test: extended form I_ext on span{Phi(F)} (+) U=span(h,v), h^2=v^2=0, h.v=1, h.Phi(F)=ev+, v.Phi(F)=ev-,
# Phi(F)^2 = -bulk(F), bulk = W - P. Hodge index <=> I_ext has exactly ONE positive direction.
import numpy as np, json, runpy
ns=runpy.run_path('map1965.py')   # reuses matrices (prints again)
def ext(Bulk, ep, em):
    n=Bulk.shape[0]; X=np.zeros((n+2,n+2)); X[:n,:n]=-Bulk; X[:n,n]=X[n,:n]=ep; X[:n,n+1]=X[n+1,:n]=em; X[n,n+1]=X[n+1,n]=1; return X
r={}
# FF: Phi(c)=sum c_n gamma_n; bulk_FF = -I on graphs; ep=gamma.h=q^{n/2}, em=gamma.v=q^{-n/2}
G=ns['G']; q=ns['q']; K=ns['K']
X=ext(-G, ns['hvec'], ns['vvec']); ev=np.linalg.eigvalsh(X)
r['FF']=dict(npos=int((ev>1e-9).sum()),nneg=int((ev<-1e-9).sum()),nzero=int((abs(ev)<=1e-9).sum()),
            bulk_nneg=int((np.linalg.eigvalsh(-G)<-1e-9).sum()))
# Q window A=2: bulk = K0 M0 + Earch + Wp  (P excluded); moments in sine basis
Bq=ns['K0']*ns['M0']+ns['Earch']+ns['Wp']
eb=np.linalg.eigvalsh(Bq)
X=ext(Bq, ns['evp_'], ns['evm']); ev=np.linalg.eigvalsh(X)
r['Q']=dict(bulk_lowest=eb[:3].tolist(),bulk_nneg=int((eb<0).sum()),Iext_npos=int((ev>0).sum()),Iext_top=sorted(ev)[-3:])
# perturbation sensitivity: scale prime couplings by (1+t); when does Hodge-index signature break?
for t in [0.002,0.005,0.01,0.03]:
    Bt=ns['K0']*ns['M0']+ns['Earch']+(1+t)*ns['Wp']; e=np.linalg.eigvalsh(ext(Bt,ns['evp_'],ns['evm']))
    r['Q']['npos_primes_x(1+%g)'%t]=int((e>0).sum())
json.dump(r,open('sig1965.json','w'),indent=1,default=float); print(json.dumps(r,indent=1,default=float))

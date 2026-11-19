"""T1 for Z1 = x^2+5y^2 and Z2 = 2x^2+2xy+3y^2 (d=-20), prime-side window form in the L149/L167 B-spline basis.
Z1/2 = sum a_n n^{-s}, a_1=1, conductor 20 (arch AZ+AD+log4*G2, as L169).  Z2/2 = 2^{-s} G(s), G = 1 + sum_{m>=3} b_m (m/2)^{-s}:
Lambda = 20^{s/2} Gamma_R(s)Gamma_R(s+1) Z2 = 5^{s/2} Gamma_R Gamma_R G  => arch AZ+AD (conductor 5), generalized frequencies
lambda = log(n/2^k), -G'/G = sum lambda [log G]_lambda e^{-lambda s}.  Pole row = zeta's (completed function has simple poles at 0,1).
Validation: the generalized code applied to Z1 reproduces lemma167_lib.log_deriv_coeffs.  Scratch. RH NOT proved."""
import os, sys, math, json, time
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.path.dirname(os.path.abspath(__file__)))
import lemma167_lib as L
from scipy.linalg import eigh, toeplitz, null_space
def gen_logderiv(b, X, den2):
    """b: dict int m -> coefficient, series G = 1 + sum b_m (m/2^den2)^{-s}  (den2 = 0 or 1). returns dict (n,k)-> c_lambda with
    lambda = log(n/2^{k}) <= log X (reduced so n odd or k=0)."""
    terms={}  # level k power B^k as dict n->coef (value n / 2^{den2*k})
    Bk={1:1.0}; logG={}
    ms=sorted(b)
    for k in range(1,200):
        new={}
        lim=X*(2**(den2*k))
        for n,v in Bk.items():
            for mm in ms:
                nn=n*mm
                if nn>lim: break
                new[nn]=new.get(nn,0.0)+v*b[mm]
        Bk=new
        if not Bk: break
        for n,v in Bk.items():
            kk=den2*k; nr=n
            while kk>0 and nr%2==0: nr//=2; kk-=1
            key=(nr,kk); logG[key]=logG.get(key,0.0)+((-1)**(k+1))*v/k
    c={}
    for (n,k),v in logG.items():
        lam=math.log(n)-k*math.log(2)
        if abs(v)>0 and lam>1e-12: c[lam]=c.get(lam,0.0)+lam*v
    return c
def prow_gen(c, d, h):
    lam=np.array(sorted(c)); w=np.array([c[x] for x in lam])*np.exp(-lam/2)
    PR=np.zeros(len(d))
    for i,v in enumerate(d):
        lo,hi=np.searchsorted(lam,v-2*h),np.searchsorted(lam,v+2*h)
        if hi>lo: PR[i]-=np.sum(w[lo:hi]*h*L.B3((lam[lo:hi]-v)/h))
    return PR
def eigs(rw,G2,N,mode,h,W=None):
    M=toeplitz(rw[:N]).real; B=toeplitz(G2[:N]).astype(float); a=np.arange(N)*h
    if mode=='E0': K=null_space(np.vstack([np.exp(a/2),np.exp(-a/2)]))
    elif mode=='coshperp':
        c=(N-1)*h/2; K=null_space(np.vstack([np.exp((a-c)/2)+np.exp(-(a-c)/2)]))
    else: K=None
    if K is not None: M=K.T@M@K; B=K.T@B@K
    return eigh(M,B)
def onset(rw,G2,h,Nmax,mode,thr=-1e-9,Nlo=3):
    f=lambda N: eigs(rw,G2,N,mode,h)[0][0]<thr
    if not f(Nmax): return None
    lo,hi=Nlo,Nmax
    if f(lo): return round((lo+1)*h,6)
    while hi-lo>1:
        mm=(lo+hi)//2
        if f(mm): hi=mm
        else: lo=mm
    return round((hi+1)*h,6)
def peakfreq(rw,G2,h,N,mode):
    ev,V=eigs(rw,G2,N,mode,h)
    a=np.arange(N)*h
    if mode!='full':
        if mode=='E0': K=null_space(np.vstack([np.exp(a/2),np.exp(-a/2)]))
        else: c=(N-1)*h/2; K=null_space(np.vstack([np.exp((a-c)/2)+np.exp(-(a-c)/2)]))
        v=K@V[:,0]
    else: v=V[:,0]
    ts=np.linspace(0.,min(120,np.pi/h),6001); F=np.abs(np.exp(1j*np.outer(ts,a))@v)
    return float(ev[0]), float(ts[np.argmax(F)])
if __name__=='__main__':
    t0=time.time(); h=float(sys.argv[1]); LMAX=float(sys.argv[2]); NMAX=int(round(LMAX/h))-1
    R=L.rows(h); d=R['d']; G2=R['G2']; X=math.exp(LMAX+0.1)
    nmax=int(X)+2
    rQ=L.epstein_coeffs(nmax,((1,0,5),)); a1=rQ/2
    cZ1=L.log_deriv_coeffs(a1,nmax)
    # validation of generalized code on Z1
    b1={n:float(a1[n]) for n in range(2,nmax+1) if a1[n]!=0}
    g1=gen_logderiv(b1,X,0)
    val=max(abs(g1.get(math.log(n),0.0)-cZ1[n]) for n in range(2,int(X)+1) if abs(cZ1[n])>0)
    # Z2
    nm2=int(2*X)+4; rQ2=L.epstein_coeffs(nm2,((2,2,3),)); a2=rQ2/2
    assert a2[1]==0 and a2[2]==1.0, (a2[1],a2[2])
    b2={n:float(a2[n]) for n in range(3,nm2+1) if a2[n]!=0}
    g2=gen_logderiv(b2,X,1)
    AE20=R['AZ']+R['AD']+math.log(4)*G2; AE5=R['AZ']+R['AD']
    rows={'Z1':R['POLE']+AE20+L.prow(cZ1,d,h,None,nmax).real,
          'Z2':R['POLE']+AE5+prow_gen(g2,d,h)}
    # zeta_K control (Euler) at same h
    rQ2i=L.epstein_coeffs(nmax,((2,2,3),)); aK=(rQ+rQ2i)/2; cK=L.log_deriv_coeffs(aK,nmax)
    rows['zetaK']=R['POLE']+AE20+L.prow(cK,d,h,None,nmax).real
    out={'h':h,'LMAX':LMAX,'validation_Z1_gen_vs_lib':val,'n_freq_Z2':len(g2),'onsets':{},'peaks':{}}
    for w,rw in rows.items():
        for mode in ('full','E0','coshperp'):
            rr=rw if mode!='coshperp' else rw-R['POLE']   # cosh-perp test is for Q = W - P
            o=onset(rr,G2,h,NMAX,mode); out['onsets'][f'{w}_{mode}']=o
            if o: 
                N=int(round(o/h))-1; out['peaks'][f'{w}_{mode}']=[peakfreq(rr,G2,h,min(N+4,NMAX),mode)]
    # index profile
    prof={}
    for w in ('Z1','Z2'):
        prof[w]=[]
        for N in range(4,NMAX+1,max(1,int(0.25/h))):
            ev=eigs(rows[w],G2,N,'E0',h)[0]; evq=eigs(rows[w]-R['POLE'],G2,N,'coshperp',h)[0]
            prof[w].append([round((N+1)*h,4),int((ev<-1e-9).sum()),float(ev[0]),int((evq<-1e-9).sum()),float(evq[0])])
    out['profile']=prof; out['sec']=time.time()-t0
    json.dump(out,open(f'epstein12_h{h}.json','w'),indent=1); print(json.dumps({k:out[k] for k in ('validation_Z1_gen_vs_lib','n_freq_Z2','onsets','peaks','sec')},indent=1))

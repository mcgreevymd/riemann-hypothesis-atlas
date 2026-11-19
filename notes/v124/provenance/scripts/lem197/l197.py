# Run from this directory. Needs numpy + scipy. Data: l149_small/ (L149 rows and coefficient tables truncated to n <= 6000; enough for r <= 8).
"""Lemma 197: Euler x FE ablation with failure localization (STATE §351 design). Scratch. RH NOT proved.
L149/L167 B-spline basis (h, N <= 319, window W=(N+1)h <= 8). Modes: W full, W|E0, Q|cosh^perp (Q = W - POLE).
Families: deg-2 q=20 (zeta_K, LL, F_lam = zeta_K + lam LL incl. Z1 lam=1, Z2 lam=-1), deg-1 q=1 (zeta), deg-1 q=5 entire (L(chi), DH).
(c) Euler kept / FE lost: one-prime local factor (1 - eps p0^-s)^-1 multiplied in, prime deleted, Beurling jitter, chi(2) rotated, wrong conductor.
Attribution: Q(v) = arch(v) + pole(v) + sum_lambda term_lambda(v); term contributions from autocorrelation of v."""
import os, sys, math, json, time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import lemma167_lib as L
from epstein12 import gen_logderiv
from scipy.linalg import eigh, toeplitz, null_space
h=float(sys.argv[1]) if len(sys.argv)>1 else 0.025
LMAX=8.0; NMAX=int(round(LMAX/h))-1
R=L.rows(h); d=R['d']; G2=R['G2']; POLE=R['POLE']; AZ=R['AZ']; AD=R['AD']
X=math.exp(LMAX+0.1); nX=int(X)+2
rng=np.random.default_rng(197)
def terms_from_c(c):  # c indexed by n
    n=np.nonzero(np.abs(c[2:nX+1])>1e-15)[0]+2
    return {math.log(k):complex(c[k]) for k in n}
def row_terms(T):
    lam=np.array(sorted(T)); w=np.array([T[x] for x in lam])*np.exp(-lam/2)
    PR=np.zeros(len(d),complex)
    for i,v in enumerate(d):
        lo,hi=np.searchsorted(lam,v-2*h),np.searchsorted(lam,v+2*h)
        if hi>lo: PR[i]-=np.sum(w[lo:hi]*h*L.B3((lam[lo:hi]-v)/h))
    return PR
def Kmat(N,mode):
    a=np.arange(N)*h
    if mode=='E0': return null_space(np.vstack([np.exp(a/2),np.exp(-a/2)]))
    if mode=='coshperp': c=(N-1)*h/2; return null_space(np.vstack([np.cosh((a-c)/2)]))
    return None
def eig(rw,N,mode,vecs=False):
    M=toeplitz(rw[:N],np.conj(rw[:N])); B=toeplitz(G2[:N]).astype(float)
    if np.max(np.abs(M.imag))<1e-14: M=M.real
    K=Kmat(N,mode)
    if K is not None: M=K.T@M@K; B=K.T@B@K
    if vecs:
        ev,V=eigh(M,B); v=V[:,0] if K is None else K@V[:,0]; return ev,v
    return eigh(M,B,eigvals_only=True)
def modrow(m,mode): return m['row']-POLE if (mode=='coshperp' and m['pole']) else m['row']
def onset(m,mode,thr=-1e-9):
    rw=modrow(m,mode); f=lambda N: eig(rw,N,mode)[0]<thr
    if not f(NMAX): return None
    lo,hi=4,NMAX
    if f(lo): return (lo+1)*h
    while hi-lo>1:
        mm=(lo+hi)//2
        if f(mm): hi=mm
        else: lo=mm
    return round((hi+1)*h,6)
def autoc(v):
    N=len(v); return np.array([np.sum(np.conj(v[k:])*v[:N-k]) for k in range(N)])
def quad(rw,A):  # v^H toeplitz(rw, conj rw) v
    return float(np.real(rw[0]*A[0]+2*np.sum(rw[1:len(A)]*A[1:])))
def attribute(m,mode,N):
    rw=modrow(m,mode); ev,v=eig(rw,N,mode,vecs=True); A=autoc(v)
    Bn=float(np.real(quad(G2.astype(complex),A))); v=v/math.sqrt(Bn); A=A/Bn
    out={'lam_min':float(ev[0]),'n_minus':int((ev<-1e-9).sum()),'arch':quad(m['arch'].astype(complex),A),
         'pole':quad(POLE.astype(complex),A) if (m['pole'] and mode!='coshperp') else 0.0}
    per={}
    for lam,c in m['T'].items():
        if lam>N*h+2*h: continue
        k=np.arange(max(0,int((lam-2*h)/h)),min(len(A),int((lam+2*h)/h)+2))
        wt=-c*math.exp(-lam/2)*h*L.B3((lam-d[k])/h); fac=np.where(k==0,1.0,2.0)
        q=float(np.real(np.sum(fac*wt*A[k])))
        if abs(q)>1e-14: per[lam]=q
    out['prime_total']=sum(per.values())
    # group by base prime (ideal norm): nearest integer exp(lam), its smallest prime factor power
    grp={}
    for lam,q in per.items():
        n=int(round(math.exp(lam))); key=n
        if abs(math.exp(lam)-n)<1e-6:
            p=next(pp for pp in range(2,n+1) if n%pp==0); key=p
        else: key=f'lam{lam:.4f}'
        grp[key]=grp.get(key,0.0)+q
    neg={k:v for k,v in grp.items() if v<0}; tot=sum(neg.values())
    srt=sorted(grp.items(),key=lambda kv:kv[1])
    out['most_negative_groups']=[[str(k),round(v,5)] for k,v in srt[:5]]
    out['neg_share']={str(k):round(v/tot,4) for k,v in sorted(neg.items(),key=lambda kv:kv[1])[:8]} if tot<0 else {}
    lams=sorted(per); below=[l for l in lams if l<=N*h]
    out['last_freq_entered']=[round(below[-1],4),int(round(math.exp(below[-1])))] if below else None
    # zero attribution: peak of |F^(t)|
    a=np.arange(N)*h; ts=np.linspace(0,min(200,np.pi/h),8001); F=np.abs(np.exp(1j*np.outer(ts,a))@v)
    out['peak_t']=float(ts[np.argmax(F)]); out['_v']=v
    return out
def member(name,T,arch,pole,cls,note=''):
    return dict(name=name,T=T,arch=arch,pole=pole,row=arch+(POLE if pole else 0)+row_terms(T),cls=cls,note=note)
def perturb(T,p,eps,kmax=40):
    T=dict(T)
    for k in range(1,kmax):
        lam=k*math.log(p)
        if lam>LMAX+0.2: break
        key=min(T,key=lambda x:abs(x-lam)) if T else None
        if key is not None and abs(key-lam)<1e-9: T[key]=T[key]+eps**k*math.log(p)
        else: T[lam]=eps**k*math.log(p)
    return T
def delete(T,p): return {l:c for l,c in T.items() if not (abs(round(l/math.log(p))*math.log(p)-l)<1e-9)}
# ---- coefficients
LAM=np.array(L.LAM[:nX+1],float); Tz=terms_from_c(LAM)
r1=L.epstein_coeffs(nX,((1,0,5),)); r2=L.epstein_coeffs(nX,((2,2,3),))
aK=(r1+r2)/2; aLL=(r1-r2)/2; assert aK[1]==1 and aLL[1]==1
TK=terms_from_c(L.log_deriv_coeffs(aK,nX)); TLL=terms_from_c(L.log_deriv_coeffs(aLL,nX))
A20=AZ+AD+math.log(4)*G2; A5=AZ+AD
n=np.arange(nX+1); chi=L.chi5(n); Tchi=terms_from_c(chi*LAM); TDH=terms_from_c(L.CDH[:nX+1].astype(complex))
def chi_rot(th):  # completely multiplicative, chi'(2)=e^{i th}, other p as chi mod 5: still Euler, |a_p|=1, FE lost
    c=chi*LAM; c=c.astype(complex); k=1
    while 2**k<=nX: c[2**k]=np.exp(1j*th*k)*math.log(2); k+=1
    return terms_from_c(c)
M=[]
M.append(member('zeta_K (d=-20)',TK,A20,True,'a: Euler+FE'))
M.append(member('LL=L(chi_-4)L(chi_5)',TLL,A20,False,'a: Euler+FE (entire)'))
for lam in (0.02,0.1,0.3,1.0,3.0,-0.3,-0.7):
    a=(aK+lam*aLL)/(1+lam); T=terms_from_c(L.log_deriv_coeffs(a,nX))
    M.append(member(f'F_lam={lam}'+(' (Z1)' if lam==1 else ''),T,A20,True,'b: FE, no Euler'))
# Z2 (lam=-1): G with half-integer frequencies, conductor 5 arch (epstein12)
nm2=int(2*X)+4; a2=L.epstein_coeffs(nm2,((2,2,3),))/2
g2=gen_logderiv({k:float(a2[k]) for k in range(3,nm2+1) if a2[k]!=0},X,1)
M.append(member('F_lam=-1 (Z2)',{l:complex(c) for l,c in g2.items()},A5,True,'b: FE, no Euler'))
for p in (2,3,5,7):
    for eps in (0.2,-0.2):
        M.append(member(f'zeta_K x (1-{eps}·{p}^-s)^-1',perturb(TK,p,eps),A20,True,'c: Euler, FE lost'))
for p in (2,3):
    M.append(member(f'zeta_K minus p={p}',delete(TK,p),A20,True,'c: Euler, FE lost'))
M.append(member('zeta_K arch q=5 (wrong conductor)',TK,A5,True,'c: Euler, FE lost (q)'))
# degree 1, zeta
M.append(member('zeta',Tz,AZ,True,'a: Euler+FE'))
for p in (2,3,5):
    for eps in (0.2,-0.2,0.05):
        M.append(member(f'zeta x (1-{eps}·{p}^-s)^-1',perturb(Tz,p,eps),AZ,True,'c: Euler, FE lost'))
for p in (2,3): M.append(member(f'zeta minus p={p}',delete(Tz,p),AZ,True,'c: Euler, FE lost'))
# Beurling: primes p -> p*exp(delta_p), delta uniform +-0.02, all powers
TB={}
for lam,c in Tz.items():
    nn=int(round(math.exp(lam))); p=next(pp for pp in range(2,nn+1) if nn%pp==0); k=round(lam/math.log(p))
    TB.setdefault(p,rng.uniform(-0.02,0.02))
TBe={}
for lam,c in Tz.items():
    nn=int(round(math.exp(lam))); p=next(pp for pp in range(2,nn+1) if nn%pp==0); k=round(lam/math.log(p))
    TBe[k*(math.log(p)+TB[p])]=k*(math.log(p)+TB[p])/k  # Lambda = log p'
M.append(member('Beurling zeta (log p jitter 0.02)',TBe,AZ,True,'c: Euler, FE lost'))
# degree 1, q=5 entire
M.append(member('L(chi mod 5, chi(2)=i)',Tchi,AD,False,'a: Euler+FE'))
M.append(member('DH',TDH,AD,False,'b: FE, no Euler'))
for th in (math.pi/2+0.3,math.pi/2+1.0):
    M.append(member(f'L(chi) with chi(2)=e^(i{th:.3f})',chi_rot(th),AD,False,'c: Euler, FE lost'))
for p in (2,3):
    M.append(member(f'L(chi) x (1-0.2·{p}^-s)^-1 [real eps]',perturb(Tchi,p,0.2),AD,False,'c: Euler, FE lost'))
def run(i):
        m=M[i]
        r={'name':m['name'],'cls':m['cls'],'onset':{},'attr':{},'profile':[]}
        for mode in ('full','E0','coshperp'): r['onset'][mode]=onset(m,mode)
        for N in range(9,NMAX+1,20):
            r['profile'].append([round((N+1)*h,3)]+[int((eig(modrow(m,mo),N,mo)<-1e-9).sum()) for mo in ('full','E0','coshperp')])
        for mode in ('E0','coshperp'):
            o=r['onset'][mode]
            if o:
                N=min(int(round(o/h))-1+2,NMAX); a=attribute(m,mode,N); a.pop('_v'); a['N']=N; r['attr'][mode]=a
        print(m['name'],r['onset'],{k:(v['last_freq_entered'],v['most_negative_groups'][:2],round(v['peak_t'],2)) for k,v in r['attr'].items()},flush=True)
        return r
if __name__=='__main__':
    from multiprocessing import Pool
    t0=time.time()
    with Pool(8) as P: res=P.map(run,range(len(M)),chunksize=1)
    json.dump(res,open(f'l197_h{h}.json','w'),indent=1); print('sec',time.time()-t0)

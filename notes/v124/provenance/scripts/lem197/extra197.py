"""L197 extras: (1) eps-scan at p0=2,3 for zeta and zeta_K; (2) flat-part (arch+pole only, no primes) onsets; (3) Delta-attribution of
(b) fakes against the matched Euler member (same arch): Delta(v)=Q_fake(v)-Q_euler(v) per frequency, prime-power vs composite share;
(4) lambda_min profiles of the true members. Scratch. RH NOT proved."""
import sys; sys.argv=['x','0.025']
exec(open('l197.py').read().split("if __name__=='__main__':")[0])
import json
from lemma167_lib import factor_sets
maxp,npf=factor_sets(nX)
out={}
def on(m): return {mo:onset(m,mo) for mo in ('full','E0','coshperp')}
# (1)
sc=[]
for base,T,A in (('zeta',Tz,AZ),('zeta_K',TK,A20)):
    for p in (2,3):
        for eps in (0.2,0.05,0.01,1e-3,1e-4,-1e-4,-1e-3,-0.01,-0.05,-0.2):
            m=member('x',perturb(T,p,eps),A,True,''); o=on(m); sc.append([base,p,eps,o]); print(base,p,eps,o,flush=True)
out['eps_scan']=sc
# (2) flat part
fl={}
for nm,A,pole in (('zeta arch+pole',AZ,True),('zeta_K arch+pole (q=20)',A20,True),('q=5 odd arch (entire)',AD,False)):
    m=member(nm,{},A,pole,''); fl[nm]=on(m); print(nm,fl[nm],flush=True)
# zeta with primes truncated at P: onset vs log(next prime power)
tr=[]
for P in (2,3,4,5,7,8,9,11,13):
    T={l:c for l,c in Tz.items() if math.exp(l)<=P+0.5}; m=member('t',T,AZ,True,''); o=on(m); tr.append([P,o]); print('trunc',P,o,flush=True)
out['flat']=fl; out['trunc']=tr
# (3) Delta attribution
def delta_attr(fake,eul,mode):
    o=onset(fake,mode)
    if not o: return None
    N=min(int(round(o/h))-1+2,NMAX); rw=modrow(fake,mode); ev,v=eig(rw,N,mode,vecs=True); A=autoc(v)
    Bn=float(np.real(quad(G2.astype(complex),A))); A=A/Bn
    Qe=quad(modrow(eul,mode),A); Qf=float(ev[0]); keys=set(fake['T'])|set(eul['T'])
    per={}
    for lam in keys:
        if lam>N*h+2*h: continue
        c=fake['T'].get(lam,0)-eul['T'].get(lam,0)
        if abs(c)<1e-14: continue
        k=np.arange(max(0,int((lam-2*h)/h)),min(len(A),int((lam+2*h)/h)+2))
        wt=-c*math.exp(-lam/2)*h*L.B3((lam-d[k])/h); fac=np.where(k==0,1.0,2.0); per[lam]=float(np.real(np.sum(fac*wt*A[k])))
    darch=quad((fake['arch']-eul['arch']).astype(complex),A)
    def isint(l): n=int(round(math.exp(l))); return n if abs(math.exp(l)-n)<1e-6 else None
    neg=sum(q for q in per.values() if q<0)
    comp=sum(q for l,q in per.items() if q<0 and isint(l) and npf[isint(l)]>1)
    nonint=sum(q for l,q in per.items() if q<0 and not isint(l))
    srt=sorted(per.items(),key=lambda kv:kv[1])[:6]
    first=min((l for l,q in per.items() if q<-0.01*abs(neg)),default=None)
    return dict(onset=o,N=N,Q_fake=Qf,Q_euler_on_v=Qe,Delta_arch=darch,Delta_primes=sum(per.values()),neg_total=neg,
        composite_share=comp/neg if neg else None,nonint_share=nonint/neg if neg else None,
        top=[[ (isint(l) or round(l,4)), round(q,4), ('pp' if isint(l) and npf[isint(l)]==1 else 'comp' if isint(l) else 'gen')] for l,q in srt],
        first_carrier=[round(first,4), isint(first)] if first else None)
byname={m['name']:m for m in M}
da={}
pairs=[(k,'zeta_K (d=-20)') for k in byname if k.startswith('F_lam') and 'Z2' not in k]+[('DH','L(chi mod 5, chi(2)=i)'),('F_lam=-1 (Z2)','zeta_K (d=-20)')]
for f,e in pairs:
    fake=byname[f]; eul=byname[e]
    if f.startswith('F_lam=-1'): eul=member('zetaK q5arch',TK,A5,True,'')  # Z2 row uses conductor-5 arch with half-integer freqs
    da[f]={mo:delta_attr(fake,eul,mo) for mo in ('E0','coshperp')}; print(f,json.dumps(da[f]['E0'])[:400],flush=True)
out['delta_attr']=da
# (4) lambda_min profiles of true members
pr={}
for nm in ('zeta','zeta_K (d=-20)','LL=L(chi_-4)L(chi_5)','L(chi mod 5, chi(2)=i)'):
    m=byname[nm]; pr[nm]=[[round((N+1)*h,3)]+[float(eig(modrow(m,mo),N,mo)[0]) for mo in ('full','E0','coshperp')] for N in range(9,NMAX+1,20)]
out['true_profiles']=pr
json.dump(out,open('extra197.json','w'),indent=1)

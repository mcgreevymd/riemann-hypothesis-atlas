import sys, json, time, mpmath as mp, sympy as sp
from spring_mp import *
A=sys.argv[1]; K=int(sys.argv[2]); t0=time.time()
m=mats(build(A,K)); Wm=W(m); E,V=geneig(Wm,m['G']); f=V[0]; G=m['G']
nrm=(f.T*G*f)[0]; Af=m['A']
rho=lambda bv: ((f.T*(m['Cev'](bv)+m['Cev'](bv).T)*f)[0]/2)/nrm
out=dict(A=A,K=K,mu=[float(e) for e in E[:4]],M=float(-K0+2*sum(an for _,an,_ in m['prim'])))
archdir=(f.T*m['D']*f)[0]/nrm; out['decomp']=dict(K0=float(K0),arch_springs=float(archdir))
pr=[]
for n,an,Cn in m['prim']:
    r=rho(mp.log(n)); s=-2*r
    # finite-difference Hellmann–Feynman check
    eps=mp.mpf(10)**-12; Ep,_=geneig(W(m,scale={n:1+eps}),G); fd=(Ep[0]-E[0])/(eps*an)
    Ed,_=geneig(W(m,drop=(n,)),G)
    pr.append(dict(n=n,a=float(an),logn=float(mp.log(n)),rho=float(r),dmu_da=float(s),fd=float(fd),contrib=float(-2*an*r),drop_dmu=float(Ed[0]-E[0])))
out['primes']=pr
Ea,_=geneig(W(m,drop=tuple(n for n,_,_ in m['prim'])),G); out['arch_only_mu']=[float(e) for e in Ea[:3]]
out['rho_curve']=[[float(bv),float(rho(bv))] for bv in [Af*i/120 for i in range(121)]]
out['check_sum']=float(K0+archdir+sum(p['contrib'] for p in pr)-E[0])
json.dump(out,open(f'controls_{A.replace("/","_")}_{K}.json','w'),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='rho_curve'},indent=0)[:4000]); print('t=%.0f'%(time.time()-t0))

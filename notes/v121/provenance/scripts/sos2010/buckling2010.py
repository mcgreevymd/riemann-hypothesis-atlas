# exact clamped "buckling" constant mu1(A)=min <G,L^2G>/<G,LG>, L=1/4-d^2, G in H^2_0(-A/2,A/2)
# Euler-Lagrange L(L-mu)G=0: G = α cosh(u/2)+γ cos(ku) (even) or β sinh(u/2)+δ sin(ku) (odd), mu=1/4+k^2
import mpmath as mp, json, sys
mp.mp.dps=30
def mu1(A):
    A=mp.mpf(A)
    fe=lambda k: k*mp.sin(k*A/2)*mp.cosh(A/4)+mp.mpf(1)/2*mp.sinh(A/4)*mp.cos(k*A/2)   # even clamped det
    fo=lambda k: k*mp.sinh(A/4)*mp.cos(k*A/2)-mp.mpf(1)/2*mp.cosh(A/4)*mp.sin(k*A/2)   # odd clamped det
    roots=[]
    for f,lab in ((fe,'even'),(fo,'odd')):
        ks=mp.linspace(mp.mpf('1e-6'),40/A,4000); prev=f(ks[0])
        for k0,k1 in zip(ks[:-1],ks[1:]):
            v=f(k1)
            if prev*v<0: roots.append((mp.findroot(f,(k0,k1),solver='bisect'),lab)); break
            prev=v
    k,lab=min(roots); return dict(A=float(A),k=float(k),mode=lab,mu1=float(mp.mpf(1)/4+k**2),inv_mu1=float(1/(mp.mpf(1)/4+k**2)),
                                   dirichlet_bound_inv=float(1/(mp.mpf(1)/4+mp.pi**2/A**2)))
if __name__=='__main__':
    out=[mu1(A) for A in (0.5,1,1.5,2,3,4,6,10)]
    json.dump(out,open('buckling2010.json','w'),indent=1); print(json.dumps(out,indent=1))

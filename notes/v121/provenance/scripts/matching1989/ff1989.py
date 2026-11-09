# FF calibration (exact model): Castelnuovo/Weil ledger on C x C for a genus-2 curve y^2=f(x) over F_p.
# Brute-force N_k (k=1..4) in F_{p^k}; Gram of normalized Frobenius graphs gamma_n=q^{-n/2}Gamma_n:
#   gamma_n.gamma_m = q^{-|n-m|/2} N_{|n-m|} (n!=m),  gamma_n^2 = 2-2g (adjunction);  gamma_n.h=q^{n/2}, gamma_n.v=q^{-n/2}.
# Checks: (1) Toeplitz law G(k)=q^{k/2}+q^{-k/2}-S_k holds INCLUDING k=0 (diagonal = Euler char = 2 - #zeros)
#         (2) primitive projection: -I(pi D_c, pi D_d) = W(c,d) for ALL c,d (bilinear, not only E0)
#         (3) spring ledger: B=W-P = sum_{k>=1} G(k)||c-T_k c||^2 - M_L||c||^2, M_L = (2-2g) + 2 sum_{1<=k<L} G(k)
#         (4) Haynsworth: n_+(J) = 1 + n_-(W)  ; sign source = Hodge index (|beta|=1), not sign of Delta^2.
import itertools, numpy as np, json
p=3; fco=[1,1,0,0,2,1]   # f(x)=x^5+2x^4+x+1 ? coefficients low->high: 1 + x + 2x^4 + x^5
def irreducible(k):
    for c in itertools.product(range(p),repeat=k):
        poly=list(c)+[1]
        # test: no roots in subfields is not enough for k=4; brute check via no factor of degree<=k/2
        ok=True
        for d in range(1,k//2+1):
            for g in itertools.product(range(p),repeat=d):
                gp=list(g)+[1]
                # poly mod gp
                r=poly[:]
                while len(r)>=len(gp):
                    lc=r[-1]; sh=len(r)-len(gp)
                    for i in range(len(gp)): r[sh+i]=(r[sh+i]-lc*gp[i])%p
                    r.pop()
                if not any(r): ok=False;break
            if not ok:break
        if ok: return poly
def field(k):
    mod=irreducible(k) if k>1 else [0,1]
    els=list(itertools.product(range(p),repeat=k))
    def mul(a,b):
        r=[0]*(2*k-1)
        for i in range(k):
            for j in range(k): r[i+j]=(r[i+j]+a[i]*b[j])%p
        for t in range(2*k-2,k-1,-1):
            lc=r[t]
            if lc:
                for i in range(k+1): r[t-k+i]=(r[t-k+i]-lc*mod[i])%p
        return tuple(r[:k])
    def add(a,b): return tuple((x+y)%p for x,y in zip(a,b))
    return els,mul,add
def count(k):
    els,mul,add=field(k)
    sq={}
    for y in els: s=mul(y,y); sq[s]=sq.get(s,0)+1
    one=tuple([1]+[0]*(k-1)); N=0
    for x in els:
        val=tuple([0]*k); xp=one
        for c in fco:
            val=add(val,tuple((c*t)%p for t in xp)); xp=mul(xp,x)
        N+=sq.get(val,0)
    return N+1   # one point at infinity (odd degree model)
g=2; N={k:count(k) for k in range(1,5)}
q=p; s={k:q**k+1-N[k] for k in N}
# L-poly from s1,s2: e1=s1, e2=(s1^2-s2)/2 ; char poly of Frobenius on H^1: T^4 - e1 T^3 + e2 T^2 - q e1 T + q^2
e1=s[1]; e2=(s[1]**2-s[2])//2
alph=np.roots([1,-e1,e2,-q*e1,q*q]); beta=alph/np.sqrt(q)
pred={k:q**k+1-np.sum(alph**k).real for k in (3,4)}
out=dict(p=p,N=N,abs_beta=np.abs(beta).tolist(),N3_N4_pred_from_L=pred)
L=7; n=np.arange(L)
def Ncount(k): return q**k+1-np.sum(alph**k).real if k>0 else None
G=np.zeros((L,L))
for i in range(L):
    for j in range(L):
        k=abs(i-j); G[i,j]=(2-2*g) if k==0 else q**(-k/2)*Ncount(k)
S=lambda k: np.sum(beta**k)
out['toeplitz_k0']=float(2-2*g - (2-S(0).real))
hv=q**(n/2); vv=q**(-n/2.)
# W(c,d) = sum_i chat(beta_i) conj dhat(beta_i), chat(b)=sum c_n b^n ; since |beta|=1, conj(b^m)=b^{-m}
Wm=np.real(sum(np.outer(beta_i**n, np.conj(beta_i**n)) for beta_i in beta))
Pm=np.outer(hv,vv)+np.outer(vv,hv)
out['D2_equals_P_minus_W']=float(np.abs(G-(Pm-Wm)).max())
# extended space span(gamma_n) + U ; projection pi D = D - (D.v)h - (D.h)v
Jx=np.zeros((L+2,L+2)); Jx[:L,:L]=G; Jx[:L,L]=Jx[L,:L]=hv; Jx[:L,L+1]=Jx[L+1,:L]=vv; Jx[L,L+1]=Jx[L+1,L]=1
Pi=np.zeros((L+2,L)); Pi[:L,:]=np.eye(L); Pi[L,:]=-vv; Pi[L+1,:]=-hv
out['primitive_proj_full_W_err']=float(np.abs(-(Pi.T@Jx@Pi)-Wm).max())
out['proj_is_primitive']=float(np.abs(np.vstack([Jx[L]@Pi,Jx[L+1]@Pi])).max())
# spring ledger
B=Wm-Pm
ML=(2-2*g)+2*sum(q**(-k/2)*Ncount(k) for k in range(1,L))
c=np.random.default_rng(0).normal(size=L)
def shift(c,k):
    out=np.zeros(L+k); out[:L]=c; t=np.zeros(L+k); t[k:]=c; return out-t
spr=sum(q**(-k/2)*Ncount(k)*np.sum(shift(c,k)**2) for k in range(1,L))
out['spring_ledger_err']=float(c@B@c-(spr-ML*c@c)); out['M_L']=ML
ev=np.linalg.eigvalsh(Jx); ew=np.linalg.eigvalsh(Wm)
out['npos_J']=int((ev>1e-9).sum()); out['nneg_W']=int((ew<-1e-9).sum()); out['rank_W']=int((abs(ew)>1e-9).sum())
out['Delta2']=2-2*g
print(json.dumps(out,indent=1,default=lambda x: float(np.real(x)) if np.isscalar(x) else str(x)))
json.dump(out,open('ff1989.json','w'),indent=1,default=lambda x: float(np.real(x)) if np.isscalar(x) else str(x))

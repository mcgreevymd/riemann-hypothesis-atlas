# moment1975: bulk B = H_A - M_A||F||^2 (= W - P) on centered window [-A/2,A/2], zero extension, L^2 window (closed).
# Exact finite-window criteria: bordered/Schur (Haynsworth) per parity sector. Numerics uncertified (Ritz).
import numpy as np, json, mpmath as mp, sys
from numpy.polynomial.legendre import leggauss
K0=float(mp.digamma(0.25)-mp.log(mp.pi))
k=lambda a: np.exp(-a/2)/(1-np.exp(-2*a))
def vM(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
def primes_win(A): return {n:vM(n)/np.sqrt(n) for n in range(2,int(np.exp(A))+2) if np.log(n)<A and vM(n)>0}
def gl(a,b,n):
    x,w=leggauss(n); return (b-a)/2*x+(a+b)/2,(b-a)/2*w
def basis_sine(A,J):
    def ev(u):
        u=np.asarray(u); out=np.array([np.sqrt(2/A)*np.sin(j*np.pi*(u+A/2)/A) for j in range(1,J+1)])
        return out*((u>=-A/2)&(u<=A/2))
    par=np.array([1 if j%2==1 else -1 for j in range(1,J+1)])   # +1 even, -1 odd
    return ev,par
def basis_LG(A,J):   # F = (d^2-1/4)G, G=(1-t^2)^2 t^k, t=2u/A  -> exact E0 (G=G'=0 at ends)
    def ev(u):
        u=np.asarray(u); t=2*u/A; out=[]
        for kk in range(J):
            P=np.polynomial.Polynomial([1,0,-1])**2*np.polynomial.Polynomial([0]*kk+[1])
            G=P(t); G2=P.deriv(2)(t)*(2/A)**2
            out.append((G2-G/4)*((u>=-A/2)&(u<=A/2)))
        return np.array(out)
    par=np.array([1 if kk%2==0 else -1 for kk in range(J)])
    return ev,par
def matrices(A,ev,nq=240,na=400,lam2=1.0):
    an=primes_win(A)
    if 2 in an: an[2]*=lam2
    MA=-K0+2*sum(an.values())
    uq,wq=gl(-A/2,A/2,nq); Pq=ev(uq)
    Gm=(Pq*wq)@Pq.T
    def R(a):
        if a>=A: return 0*Gm
        x,w=gl(-A/2+a,A/2,nq); M=(ev(x)*w)@ev(x-a).T; return (M+M.T)/2
    # graded composite GL in a
    edges=np.concatenate([[0],A*np.geomspace(1e-4,1,12)])
    E=np.zeros_like(Gm)
    for lo,hi in zip(edges[:-1],edges[1:]):
        xs,ws=gl(lo,hi,na//12+8)
        for a,w in zip(xs,ws): E+=w*k(a)*2*(Gm-R(a))
    from scipy.integrate import quad
    E+=2*Gm*quad(k,A,np.inf)[0]
    Hp=sum(c*2*(Gm-R(np.log(n))) for n,c in an.items())
    B=E+Hp-MA*Gm
    cp=(Pq*wq)@np.exp(uq/2); cm=(Pq*wq)@np.exp(-uq/2)
    return dict(B=B,G=Gm,cp=cp,cm=cm,MA=MA,an=an)
def gen_eig(B,G):
    L=np.linalg.cholesky(G); Li=np.linalg.inv(L); S=Li@B@Li.T; w,V=np.linalg.eigh((S+S.T)/2); return w,Li.T@V
def constrained_min(B,G,rows):
    if len(rows)==0: return gen_eig(B,G)[0][0]
    C=np.array(rows); Q=np.linalg.svd(C)[2][len(rows):].T   # null space basis of rows (coefficient space)
    return gen_eig(Q.T@B@Q,Q.T@G@Q)[0][0]
def sector(B,G,c,par,s):
    idx=np.where(par==s)[0]; Bs=B[np.ix_(idx,idx)]; Gs=G[np.ix_(idx,idx)]; cs=c[idx]
    w,V=gen_eig(Bs,Gs)
    # q = c^T B^-1 c in coefficient space (c is the moment row, i.e. functional), via eigen-decomposition (V^T G V = I)
    coef=V.T@cs; terms=coef**2/w
    q=terms.sum(); neg=terms[w<0].sum(); pos=terms[w>0].sum()
    return dict(nneg=int((w<0).sum()),lam=w[:3].tolist(),q=float(q),q_neg=float(neg),q_pos=float(pos),
                rho=float(pos/(-neg)) if neg<0 else None,
                align=float(coef[0]**2/(coef**2).sum()),  # overlap of moment functional with lowest mode (B-orthonormal frame)
                cmin=float(constrained_min(Bs,Gs,[cs])))
if __name__=='__main__':
    out={}
    for A in [0.6,1.0,2.0]:
        for J in [24,40,64]:
            ev,par=basis_sine(A,J); M=matrices(A,ev)
            B,G,cp,cm=M['B'],M['G'],M['cp'],M['cm']; ch=(cp+cm)/2; sh=(cp-cm)/2
            r=dict(MA=M['MA'],J=J,full_nneg=int((gen_eig(B,G)[0]<0).sum()),
                   min_none=float(constrained_min(B,G,[])),min_Cplus=float(constrained_min(B,G,[cp])),
                   min_Cminus=float(constrained_min(B,G,[cm])),min_both=float(constrained_min(B,G,[cp,cm])),
                   even=sector(B,G,ch,par,1),odd=sector(B,G,sh,par,-1))
            # full W = B + P, P = 2 ev- ev+ = 2(ch^2 - sh^2): even +2cc^T, odd -2ss^T  (reported separately, not compared to E0 bulk)
            Pm=np.outer(cm,cp)+np.outer(cp,cm); r['W_full_min']=float(gen_eig(B+Pm,G)[0][0])
            out[f'A{A}_J{J}']=r; print(A,J,json.dumps(r,default=float),flush=True)
        # independent E0 encoding: F=(d^2-1/4)G polynomial basis (no constraint rows needed); verify moments
        for J in [12,18,24]:
            ev,par=basis_LG(A,J); M=matrices(A,ev)
            out[f'A{A}_LG{J}']=dict(min=float(gen_eig(M['B'],M['G'])[0][0]),max_moment=float(max(abs(M['cp']).max(),abs(M['cm']).max())),
                                    cond_G=float(np.linalg.cond(M['G'])))
            print(A,'LG',J,out[f'A{A}_LG{J}'],flush=True)
    json.dump(out,open('mom1975.json','w'),indent=1,default=float)

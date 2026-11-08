# localization1970: semilocal (unramified) pair-of-projections model in the unitary log-module picture.
# L^2(C_S)^ur = L^2(R,du). Fourier on A_S transported by E_S:  (F xi)^(y) = c_S(1/2+iy) xi^(-y),
#   c_S(1/2+iy) = prod_v L_v(1/2-iy)/L_v(1/2+iy)  (Tate local FE; L_inf=Gamma_R, L_2=(1-2^-s)^-1).  P = 1_{u<=L},
#   Phat = F P F^-1 = M_cbar 1_{u>=-L} M_c,  S_Lambda = 1_{|u|<=L},  V(f) = convolution (unitary rep), phi = f*f^* (autocorr.).
# Connes R = Phat P (not positive).  Candidate Q = S Phat S: 0 <= Q <= S (algebraic). Deficit D = Tr(S(1-Phat)S V(phi)) >= 0.
import numpy as np, mpmath as mp, json, sys
def cS(y, primes):
    out=np.empty(len(y),complex)
    for i,t in enumerate(y):
        s=mp.mpf(0.5)+1j*mp.mpf(t)
        lg=lambda z: -z/2*mp.log(mp.pi)+mp.loggamma(z/2)
        val=mp.e**(lg(1-s)-lg(s))           # Gamma_R(1/2-iy)/Gamma_R(1/2+iy)
        for p in primes: val*= (1-mp.mpf(p)**(-s))/(1-mp.mpf(p)**(-(1-s)))
        out[i]=complex(val)
    return out
def run(A, Gkind, primes, L, h, margin=20.0, conj=False):
    T=2*L+2*margin; N=int(round(T/h)); h=T/N
    u=(np.arange(N)-N//2)*h
    y=2*np.pi*np.fft.fftfreq(N,d=h)
    c=cS(y,primes);  c=np.conj(c) if conj else c
    kc=np.fft.ifft(c)                       # circulant kernel: (C xi) = ifft(c*fft(xi)); C[k,j]=kc[(k-j)%N]
    idx=(np.arange(N)[:,None]-np.arange(N)[None,:])%N
    C=kc[idx]
    Hm=(u>=-L)&(u<=T/2-margin/2)           # half-line projection, far artificial edge
    Ph=C.conj().T@(C*Hm[:,None])           # Phat = C^* H C
    # test function F = (d^2-1/4)G on [0,A], placed at u in [-A/2, A/2] (translation-invariant quantities)
    uu=np.linspace(0,A,4001); du=uu[1]-uu[0]
    G={'sin8':np.sin(np.pi*uu/A)**8,'poly6':(uu*(A-uu))**6,'skew':uu**6*(A-uu)**8}[Gkind]
    F=np.gradient(np.gradient(G,du,edge_order=2),du,edge_order=2)-G/4; F/=np.sqrt(np.trapezoid(F*F,dx=du))
    ev=(np.trapezoid(F*np.exp(-uu/2),dx=du),np.trapezoid(F*np.exp(uu/2),dx=du))
    lag=np.arange(-int(A/h)-2,int(A/h)+3)*h
    phi=np.array([np.trapezoid(F*np.interp(uu-s,uu,F,left=0,right=0),dx=du) for s in lag])
    phiF=lambda s: np.interp(s,lag,phi,left=0,right=0)
    Vt=phiF(u[None,:]-u[:,None])*h          # Vt[i,j] = V_ji = phi(u_j-u_i) h
    Sm=np.abs(u)<=L; Pm=u<=L
    trSV=Sm.sum()*phiF(0)*h
    trR=np.real(np.sum(Ph*Pm[None,:]*Vt))
    trQ=np.real(np.sum(Ph*(Sm[:,None]&Sm[None,:])*Vt))
    # reference symbol: bulk = W-P = (1/2pi) int m_S |Fhat|^2, m_S = Re psi(1/4+ix/2)-log pi - 2 sum_{p,k} log p p^{-k/2} cos(k x log p)
    xs=np.linspace(0,160,8001); Fh=np.array([np.trapezoid(F*np.exp(-1j*x*uu),dx=du) for x in xs])
    mS=np.array([float(mp.re(mp.digamma(0.25+0.5j*x)))-np.log(np.pi) for x in xs])
    for p in primes:
        k=np.arange(1,60); mS=mS-2*np.sum(np.log(p)*p**(-k[:,None]/2)*np.cos(np.outer(k,xs)*np.log(p)),0)
    bulk=2*np.trapezoid(mS*abs(Fh)**2,xs)/(2*np.pi)
    semi=2*np.trapezoid(np.maximum(mS,0)*abs(Fh)**2,xs)/(2*np.pi)
    return dict(A=A,G=Gkind,primes=primes,L=L,h=h,N=N,ev=ev,tau_num=trR-trSV,minus_bulk=-bulk,
                D=trSV-trQ,W_minus_P=bulk,residual_W_minus_D=bulk-trSV+trQ,semiclassical_m_plus=semi)
if __name__=='__main__':
    out=[]
    for args in [(1.0,'sin8',[2],8,0.025),(1.0,'sin8',[2],12,0.025),(1.0,'sin8',[2],12,0.0175),
                 (1.0,'poly6',[2],12,0.025),(1.0,'skew',[2],12,0.025),
                 (0.6,'sin8',[],12,0.025),(0.6,'sin8',[2],12,0.025),(0.6,'poly6',[],12,0.025)]:
        r=run(*args); out.append(r); print({k:(round(v,6) if isinstance(v,float) else v) for k,v in r.items()},flush=True)
    json.dump(out,open('loc1970.json','w'),indent=1,default=float)

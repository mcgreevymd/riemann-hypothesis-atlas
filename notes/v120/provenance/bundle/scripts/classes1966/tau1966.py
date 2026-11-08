# Independent evaluation of Connes' geometric side sum_v int' h(u^-1)/|1-u| d*u (Thm VII.4; principal value fixed by
# alpha-normalisation: unique extension of du/|1-u| whose Fourier transform vanishes at 1), for h(e^s)=e^{-s/2} r(s),
# r = autocorrelation of window F.  Compare with -(W-P) = -int m_A |Fhat|^2/2pi (Fourier symbol, our W).
import numpy as np, mpmath as mp, json
from scipy.integrate import quad
A=2.0; u=np.linspace(0,A,8001); du=u[1]-u[0]; tr=lambda y: np.trapezoid(y,dx=du)
lam={2:np.log(2),3:np.log(3),4:np.log(2),5:np.log(5),7:np.log(7)}
def trial(kind):
    if kind=='E0_sin8':
        G=np.sin(np.pi*u/A)**8; G1=np.gradient(G,du,edge_order=2); return np.gradient(G1,du,edge_order=2)-G/4
    if kind=='nonE0_poly': return (u*(A-u))**4
    if kind=='nonE0_skew': return u**2*(A-u)**5*np.exp(u)
res={}
for kind in ['E0_sin8','nonE0_poly','nonE0_skew']:
    F=trial(kind); F=F/np.sqrt(tr(F*F))
    sg=np.linspace(-A,A,4001); rv=np.array([tr(F*np.interp(u-s,u,F,left=0,right=0)) for s in sg])
    r=lambda s: np.interp(s,sg,rv,left=0,right=0)
    h=lambda x: x**-0.5*r(np.log(x))                     # h on R+*, h(e^s)=e^{-s/2} r(s)
    phi=lambda x: h(1/abs(x))/abs(x)                      # integrand against du/|1-u| (d*u = du/|u|), unramified: h(|u|^-1)
    # <T0(.-1),phi> with unit cutoff + 2(gamma+log 2pi) phi(1)
    eps=np.exp(-A)
    I1=quad(lambda x:(phi(1+x)-phi(1))/abs(x),-1,1,points=[0,-1+eps,np.exp(A)-1 if np.exp(A)-1<1 else 0.5],limit=800)[0]
    I2=quad(lambda x: phi(1+x)/abs(x),1,np.exp(A)-1+1e-9,limit=800)[0] if np.exp(A)-1>1 else 0.0
    I3=quad(lambda x: phi(1+x)/abs(x),-1-np.exp(A),-1-eps,limit=800)[0]     # u<0 sheet
    arch=0.5*(I1+I2+I3+2*(np.euler_gamma+np.log(2*np.pi))*phi(1))   # d*u on R^* = du/(2|u|): mass{|u| in [1,L]} = log L (C_S normalisation)
    prime=sum(c*(np.exp(-0.5*np.log(n))*r(np.log(n))*2) for n,c in lam.items())   # log p [h(p^k)+p^-k h(p^-k)]
    tau=arch+prime
    # Fourier bulk
    xs=np.linspace(0,150,7501); Fh=np.array([tr(F*np.exp(-1j*x*u)) for x in xs])
    m=np.array([float(mp.re(mp.digamma(0.25+0.5j*x)))-np.log(np.pi)-2*sum(np.log(Lam_p)/np.sqrt(n)*np.cos(x*np.log(n)) for n,Lam_p in [(2,2),(3,3),(4,2),(5,5),(7,7)]) for x in xs])
    bulk=2*np.trapezoid(m*abs(Fh)**2,xs)/(2*np.pi)
    a=tr(F*np.exp(-u/2)); b=tr(F*np.exp(u/2))
    res[kind]=dict(tau_connes=tau,arch=arch,prime=prime,minus_bulk=-bulk,diff=tau+bulk,rel=(tau+bulk)/max(abs(bulk),1e-12),P=2*a*b,W=bulk+2*a*b,ev_minus=a,ev_plus=b)
json.dump(res,open('tau1966.json','w'),indent=1); print(json.dumps(res,indent=1))

# Exact check: per-prime score 2 d_sigma log|L_p(1/2+ix)| = log p - sum_m 1/(1/4+(x-2 pi m/log p)^2)
# and E0 window decomposition W = arch + sum_{p<=N}[log p ||F||^2 - sum_m Q_{p,m}],  Q_{p,0}(LG)=||G'||^2+||G||^2/4
import numpy as np, mpmath as mp, json, sys
sys.path.insert(0,'/workspace/taa/sign1918'); from screened import Window
out={}
for p in [2,3,7]:
    for x in [0.0,1.3]:
        lhs=-2*float(mp.nsum(lambda k: mp.log(p)*p**(-k/2.)*mp.cos(k*x*mp.log(p)),[1,mp.inf]))
        L=np.log(p); rhs=L-float(mp.nsum(lambda m:1/(0.25+(x-2*mp.pi*m/L)**2),[-mp.inf,mp.inf]))
        out[f'p{p}_x{x}']=[lhs,rhs]
Wd=Window(2.0,8001); u=Wd.u; P=np.polynomial.polynomial
gp=P.polypow([1,0,-1],8); G=P.polyval(u,gp); Gp=P.polyval(u,P.polyder(gp)); F=P.polyval(u,P.polyder(gp,2))-G/4
xs=np.linspace(-200,200,8001); Fh=np.array([np.trapezoid(F*np.exp(-1j*q*u),u) for q in xs]); A2=np.abs(Fh)**2
I=lambda m: np.trapezoid(A2*m,xs)/(2*np.pi)
nF=np.trapezoid(F**2,u)
arch=I(np.array([float(mp.re(mp.digamma(0.25+1j*q/2))-mp.log(mp.pi)) for q in xs]))
tot=arch; parts={}
for p in [2,3,5,7]:
    L=np.log(p); ms=np.arange(-int(400*L/(2*np.pi))-5,int(400*L/(2*np.pi))+6)
    lor=sum(1/(0.25+(xs-2*np.pi*m/L)**2) for m in ms)
    Q0=I(1/(0.25+xs**2)); parts[p]=dict(Q0=Q0,sum_m=I(lor))
    tot+=L*nF-I(lor)
out['Q0_vs_local']=[parts[2]['Q0'],float(np.trapezoid(Gp**2,u)+0.25*np.trapezoid(G**2,u))]
out['W_resolvent_decomp']=float(tot); out['W_spring']=float(Wd.form(F,F,0.0)); out['arch']=float(arch); out['normF2']=float(nF)
out['parts']=parts
print(json.dumps(out,indent=1)); json.dump(out,open('euler_resolvent.json','w'),indent=1)

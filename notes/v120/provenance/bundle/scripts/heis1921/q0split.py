# Q0(H)=∫∫H conjH e^{-|u-v|/2} = interior energy of G=-(1/4-d^2)^{-1}H on window + (1/2)e^{-A/2}(|ev+|^2+|ev-|^2)
import numpy as np, json
A=2.0; n=4001; u=np.linspace(-A/2,A/2,n); du=u[1]-u[0]; P=np.polynomial.polynomial
gp=P.polypow([1,0,-1],8); G0=P.polyval(u,gp); F=P.polyval(u,P.polyder(gp,2))-G0/4
res={}
for xi in [0.0,0.5,2.0,2*np.pi/np.log(2)]:
    H=np.exp(-1j*xi*u)*F
    K=np.exp(-np.abs(u[:,None]-u[None,:])/2)
    Q0=np.real(np.conj(H)@K@H)*du*du
    G=-(K@H)*du; Gp=np.gradient(G,u)
    interior=np.trapezoid(np.abs(Gp)**2+0.25*np.abs(G)**2,u)
    evp=np.trapezoid(H*np.exp(u/2),u); evm=np.trapezoid(H*np.exp(-u/2),u)
    bd=0.5*np.exp(-A/2)*(abs(evp)**2+abs(evm)**2)
    res[f'xi={xi:.4f}']=dict(Q0=Q0,interior=interior,boundary=bd,sum=interior+bd,ev_abs2_pred_factor=xi**4+xi**2)
    print(res[f'xi={xi:.4f}'])
json.dump(res,open('q0split.json','w'),indent=1)

# spring ledger W = H_A - M_A||F||^2 on the same E0 tests (P=0), vs symbol value from loc1970 output
import numpy as np, json
from scipy.integrate import quad
K0=-5.3721834192256654; k=lambda a: np.exp(-a/2)/(1-np.exp(-2*a))
res=json.load(open('orient1970.json'))
out=[]
for r in res[:5]:
    A=r['A']; uu=np.linspace(0,A,4001); du=uu[1]-uu[0]
    G={'sin8':np.sin(np.pi*uu/A)**8,'poly6':(uu*(A-uu))**6,'skew':uu**6*(A-uu)**8}[r['G']]
    F=np.gradient(np.gradient(G,du,edge_order=2),du,edge_order=2)-G/4; F/=np.sqrt(np.trapezoid(F*F,dx=du))
    rr=lambda s: np.trapezoid(F*np.interp(uu-s,uu,F,left=0,right=0),dx=du) if s<A else 0.0
    an={2:np.log(2)/np.sqrt(2)} if A>np.log(2) else {}
    Einf=quad(lambda a:k(a)*2*(1-rr(a)),0,A,limit=300)[0]+quad(lambda a:2*k(a),A,np.inf)[0]
    Hp=sum(c*2*(1-rr(np.log(n))) for n,c in an.items()); MA=-K0+2*sum(an.values())
    W=Einf+Hp-MA
    out.append(dict(A=A,G=r['G'],H_A=Einf+Hp,M_A=MA,W_spring=W,W_symbol=r['W_minus_P'],diff=W-r['W_minus_P']))
    print(out[-1])
json.dump(out,open('ledger1970.json','w'),indent=1)

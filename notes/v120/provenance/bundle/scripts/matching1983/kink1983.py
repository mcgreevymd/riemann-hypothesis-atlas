# Check exact prediction: for A=1, r2=(B h2) has derivative jump a_2*sinh(A/4)/2 at v0=±(log2-A/2) (prime-2 translate of window edge kink)
import numpy as np, json
from match1983 import resp
A=1.0; v0=np.log(2)-A/2; a2=np.log(2)/np.sqrt(2); out={}
for e in [1e-3,1e-4]:
    for s in [+1,-1]:
        x=s*v0; f=lambda t: resp(A,t,'h2')
        dl=(f(x)-f(x-e))/e; dr=(f(x+e)-f(x))/e
        out[f'v{s*v0:.4f}_eps{e}']=dict(jump=dr-dl,predicted_abs=a2*np.sinh(A/4)/2)
        print(out[f'v{s*v0:.4f}_eps{e}'])
json.dump(out,open('kink1983.json','w'),indent=1)

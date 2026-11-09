# Diagnostic (uses nothing but the ledger matrices): spectrum of FULL W on window A. Compare log-scale clustering with
# the Landau/Nyquist deficit heuristic D(T)=A T/pi - 2N(T) (max 2e^A at T=2*pi*e^A). [HEURISTIC; zeros enter only the prediction]
import numpy as np, json, runpy
ns=runpy.run_path('mom1975.py')
out={}
for A in [0.6,1.0,1.5]:
    ev,par=ns['basis_sine'](A,40); M=ns['matrices'](A,ev)
    B,G,cp,cm=M['B'],M['G'],M['cp'],M['cm']
    W=B+np.outer(cp,cm)+np.outer(cm,cp)
    w=ns['gen_eig'](W,G)[0]; we=ns['gen_eig'](W[np.ix_(par==1,par==1)],G[np.ix_(par==1,par==1)])[0]
    out[A]=dict(lowest=w[:10].tolist(),even_lowest=we[:5].tolist(),pred_2eA=2*np.exp(A))
    print(A,'2e^A=%.2f'%(2*np.exp(A)),np.array2string(w[:10],precision=2))
json.dump(out,open('nyq1989.json','w'),indent=1,default=float)

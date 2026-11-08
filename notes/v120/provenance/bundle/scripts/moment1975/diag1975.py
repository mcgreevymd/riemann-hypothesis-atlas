# (1) non-arithmetic controls at fixed constraints: moment weight alpha != 1/2; prime-2 spring scaled by lam; (2) single-moment criterion
import numpy as np, json
from mom1975 import *
out={}
J=48
for A in [0.6,1.0]:
    ev,par=basis_sine(A,J); M=matrices(A,ev); B,G=M['B'],M['G']
    uq,wq=gl(-A/2,A/2,240); Pq=ev(uq)
    for al in [0.3,0.4,0.45,0.5,0.55,0.6,0.8]:
        cp=(Pq*wq)@np.exp(al*uq); cm=(Pq*wq)@np.exp(-al*uq)
        e=sector(B,G,(cp+cm)/2,par,1); o=sector(B,G,(cp-cm)/2,par,-1)
        out[f'A{A}_alpha{al}']=dict(min_both=float(constrained_min(B,G,[cp,cm])),min_single=float(constrained_min(B,G,[cp])),
            q_even=e['q'],rho_even=e['rho'],align_even=e['align'],q_odd=o['q'],lam2_even=e['lam'][1])
        print(A,'alpha',al,out[f'A{A}_alpha{al}'],flush=True)
A=1.0; ev,par=basis_sine(A,J)
for lam in [0.0,0.5,0.9,1.0,1.1,1.5,2.0]:
    M=matrices(A,ev,lam2=lam); B,G,cp,cm=M['B'],M['G'],M['cp'],M['cm']
    e=sector(B,G,(cp+cm)/2,par,1); o=sector(B,G,(cp-cm)/2,par,-1)
    Pm=np.outer(cm,cp)+np.outer(cp,cm)
    out[f'lam2_{lam}']=dict(min_both=float(constrained_min(B,G,[cp,cm])),W_full_min=float(gen_eig(B+Pm,G)[0][0]),
        q_even=e['q'],q_odd=o['q'],nneg_even=e['nneg'],nneg_odd=o['nneg'],lam_even=e['lam'],lam_odd=o['lam'],rho_even=e['rho'])
    print('lam2',lam,out[f'lam2_{lam}'],flush=True)
json.dump(out,open('diag1975.json','w'),indent=1,default=float)

# Lefschetz local data: det Df = 1 for every area-preserving map, but the fixed-point index is sign det(I-Df) and the
# distributional (Atiyah-Bott/Guillemin) weight is 1/|det(I-Df)|. Harmonic oscillator: time-2pi map = identity (non-isolated).
import numpy as np, json
out={}
for name,Df in (('hyperbolic diag(2,1/2)',np.diag([2,.5])),('elliptic rot(pi/3)',np.array([[.5,-np.sqrt(3)/2],[np.sqrt(3)/2,.5]])),
                ('shear [[1,1],[0,1]] (parabolic)',np.array([[1.,1],[0,1]])),('osc time 2pi = I',np.eye(2))):
    d=np.linalg.det(np.eye(2)-Df)
    out[name]=dict(detDf=float(np.linalg.det(Df)),det_I_minus_Df=float(d),index=(int(np.sign(d)) if abs(d)>1e-12 else 'non-isolated/degenerate'),
                   AB_weight=(float(1/abs(d)) if abs(d)>1e-12 else 'undefined'))
# Connes/Weil p-adic normal weight: periodic orbit of length log p, multiplier u=p^m acting on the transverse Q_p direction:
# 1/|1-u|_p with the |u|^{1/2} normalisation gives log p * p^{-m/2} (Connes 1999 Thm 4 / Weil); real-analogue check of the normal factor:
rows=[]
for p in (2,3):
    for m in (1,2):
        u=p**m; rows.append(dict(p=p,m=m,abs_1_minus_u_p=1.0,abs_1_minus_uinv_p=float(p**m),
                                 Weil_weight=float(np.log(p)*p**(-m/2))))
out['p-adic |1-u|_p for u=p^m, p^-m (normal factor) and Weil weight log p p^{-m/2}']=rows
json.dump(out,open('lefschetz2002.json','w'),indent=1); print(json.dumps(out,indent=1))

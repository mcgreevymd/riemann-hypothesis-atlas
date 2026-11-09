# Pencil discriminant through e=h+v on the ACTUAL Galerkin window form (uses matching1989/mom1975.py, unchanged).
# For F (L2-normalized), x*=F+alpha*h+beta*v optimal; line x*+tau e meets {J=0} at tau_pm; separation = sqrt(2*disc/4)/1 ...
import numpy as np, json, runpy, os
os.chdir('../matching1989'); ns=runpy.run_path('mom1975.py')
out={}
for A in [0.6,1.0,1.5]:
    ev,par=ns['basis_sine'](A,40); Mx=ns['matrices'](A,ev)
    B,G,cp,cm=Mx['B'],Mx['G'],Mx['cp'],Mx['cm']
    Li=np.linalg.inv(np.linalg.cholesky(G)); Bt=Li@B@Li.T; Bt=(Bt+Bt.T)/2; ap=Li@cp; am=Li@cm
    W=Bt+np.outer(ap,am)+np.outer(am,ap); w,V=np.linalg.eigh(W)
    rows=[]
    for j in range(4):
        F=V[:,j]; c1=F@ap; c2=F@am; Bv=F@Bt@F
        # optimal U-part: alpha-beta = c_p - c_m (from sympy: d/du), alpha+beta free (flat) -> take alpha+beta=0
        u=c1-c2; al=u/2; be=-u/2
        Jex=c1+c2+al+be; Jxx=-Bv+2*al*c1+2*be*c2+2*al*be; disc4=Jex**2-2*Jxx
        sep=2*np.sqrt(max(disc4,0))/2      # tau_+ - tau_- = 2 sqrt(disc/4)/J(e,e)
        rows.append(dict(W=float(w[j]),disc_quarter=float(disc4),twoW=float(2*w[j]),null_point_separation=float(sep)))
    out[f'A={A}']=rows
json.dump(out,open('../parabolic1998/pencilW1998.json','w'),indent=1); print(json.dumps(out,indent=1))

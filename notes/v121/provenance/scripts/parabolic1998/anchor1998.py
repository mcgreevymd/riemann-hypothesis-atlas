# Dimension caveat: null pair (h,v), J(h,v)=1, e=h+v, nondegenerate J -- the parabolic/hyperbolic data do NOT fix n_+ beyond dim 3.
import numpy as np, json
def J(sgnD):  # V = D (dim 2) + U ; J|D = sgnD*I (i.e. -B = sgnD), no coupling
    M=np.zeros((4,4)); M[0,0]=M[1,1]=sgnD; M[2,3]=M[3,2]=1; return M
out={}
for sg,name in ((-1,'Lorentz (B>0 on D)'),(+1,'n_+=3 (B<0 on D)')):
    M=J(sg); ev=np.linalg.eigvalsh(M); e=np.array([0,0,1,1.])
    rng=np.random.default_rng(0); worst=1e9
    for _ in range(20000):
        x=rng.normal(size=4); d=(e@M@x)**2-(e@M@e)*(x@M@x); worst=min(worst,d/(x@x))
    out[name]=dict(inertia=[int((ev>0).sum()),int((ev<0).sum())],det=float(np.linalg.det(M)),J_ee=float(e@M@e),
                   min_pencil_disc_over_x2=float(worst),
                   verdict='every line through e meets {J=0} (hyperbola-type), contour empty' if worst>-1e-12 else 'ellipse-type lines through e exist (contour nonempty)')
json.dump(out,open('anchor1998.json','w'),indent=1); print(json.dumps(out,indent=1))

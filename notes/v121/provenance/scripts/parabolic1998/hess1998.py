# check Hess(-log(-Q)) = (2/|Q|)(M + 2 Mx xᵀM/|Q|) and det = -(2/|Q|)^N det M; signature tests
import numpy as np, json
rng=np.random.default_rng(1); out={}
for name,D in (('(2,1)',[1,1,-1]),('(3,1)',[1,1,1,-1]),('(1,3)',[1,-1,-1,-1])):
    D=np.array(D,float); N=len(D); R=np.linalg.qr(rng.normal(size=(N,N)))[0]; M=R@np.diag(D)@R.T
    # find x with Q(x)<0
    while True:
        x=rng.normal(size=N)
        if x@M@x<0: break
    q=-(x@M@x); f=lambda y: -np.log(-(y@M@y)); h=1e-4
    H=np.array([[ (f(x+h*(np.eye(N)[i]+np.eye(N)[j]))-f(x+h*(np.eye(N)[i]-np.eye(N)[j]))-f(x-h*(np.eye(N)[i]-np.eye(N)[j]))+f(x-h*(np.eye(N)[i]+np.eye(N)[j])))/(4*h*h) for j in range(N)] for i in range(N)])
    Hf=(2/q)*(M+2*np.outer(M@x,M@x)/q)
    out[name]=dict(formula_err=float(abs(H-Hf).max()), det=float(np.linalg.det(Hf)), det_pred=float(-(2/q)**N*np.linalg.det(M)),
                   hess_inertia=[int((np.linalg.eigvalsh(Hf)>0).sum()),int((np.linalg.eigvalsh(Hf)<0).sum())])
json.dump(out,open('hess1998.json','w'),indent=1); print(json.dumps(out,indent=1))

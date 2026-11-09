# Tolerance of the diagonal constant on E0: lowest eigenvalues of B|E0 (Galerkin, sine J=40) = max admissible error in M_A. [NUM]
import numpy as np, json, runpy
ns=runpy.run_path('mom1975.py'); out={}
for A in [0.6,1.0,1.5]:
    ev,par=ns['basis_sine'](A,40); M=ns['matrices'](A,ev)
    C=np.array([M['cp'],M['cm']]); Z=np.linalg.svd(C)[2][2:].T
    w=ns['gen_eig'](Z.T@M['B']@Z,Z.T@M['G']@Z)[0]; out[A]=w[:6].tolist(); print(A,np.array2string(w[:6],precision=3))
json.dump(out,open('e0tol1989.json','w'),indent=1)

import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from inertia2057 import *
rows=[]
for A in [.5,.694,1.,1.1,1.5,2.,2.5,3.]:
 for n in [1024,2048]:
  row=analyze(A,n);rows.append(row)
  print(A,n,row['Q_inertia'],row['W_inertia'],row['S_eigenvalues'],row['constrained_min'],flush=True)
scan=[]
for A in np.arange(.5,3.00001,.025):
 row=analyze(float(A),128);scan.append(row)
json.dump(dict(refined=rows,coarse_scan=scan,notice='NUM only; no detected failure is not a positivity theorem; cell eigenvalue bias remains substantial'),open(OUT/'scan2057.json','w'),indent=2)

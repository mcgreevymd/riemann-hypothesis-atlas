import os,sys
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'../inertia2057')
import numpy as np, inertia2057 as I, pathlib, time
C=pathlib.Path('cache');C.mkdir(exist_ok=True)
def get(A,n):
  f=C/f'Q_{A:.8f}_{n}.npz'
  if f.exists():
    d=np.load(f);return d['col'],d['gcol'],d['B']
  t=time.time()
  orig=I.atoms; I.atoms=lambda A:[]
  Qg,B=I.matrix(A,n); I.atoms=orig
  gcol=Qg[:,0].copy(); col=gcol.copy(); h=A/n
  for a,w,_ in I.atoms(A):
    col-=w*(np.maximum(0,1-abs(np.arange(n)*h-a)/h)+np.maximum(0,1-abs(np.arange(n)*h+a)/h))
  np.savez(f,col=col,gcol=gcol,B=B)
  print('built',A,n,time.time()-t,flush=True)
  return col,gcol,B
if __name__=='__main__':
  import math
  Al=[float(x) for x in sys.argv[2].split(',')]; n=int(sys.argv[1])
  for A in Al: get(A,n)

import os,sys
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np, scipy.linalg as la, json, time, build
L=np.log
WIN={'0.694':.694,'1.0':1.,'1.1':1.1,'log4-':L(4)-1e-5,'log4+':L(4)+1e-5,'1.5':1.5,'log5-':L(5)-1e-5,'log5+':L(5)+1e-5,'2.0':2.,'2.5':2.5,'3.0':3.}
def primecol(A,n,maxn=None):
  import inertia2057 as I
  h=A/n;c=np.zeros(n)
  for a,w,m in I.atoms(A):
    if maxn and m>maxn: continue
    c-=w*(np.maximum(0,1-abs(np.arange(n)*h-a)/h)+np.maximum(0,1-abs(np.arange(n)*h+a)/h))
  return c
def solve(col,B,k=6):
  Q=la.toeplitz(col);V=la.qr(B,mode='full')[0];Z=V[:,2:]
  M=Z.T@Q@Z; ev,U=la.eigh(M,subset_by_index=[0,k-1])
  return Q,Z,ev,Z@U
def diag(f,u,A,h):
  # f: function values on cells (L2 normalized: sum f^2 h=1)
  n=len(f); zc=int(np.sum(np.sign(f[1:])!=np.sign(f[:-1])))
  edge=float(np.sum(f[np.abs(u)>0.4*A]**2)*h)  # outer 10% each side = 20% of length
  pr=float((np.sum(f**2))**2/(n*np.sum(f**4)))
  rough=float(np.sum(np.diff(f)**2)*h/h**2)   # ~ int f'^2 if resolved
  rough_ratio=float(np.sum(np.diff(f)**2)/np.sum(f**2))
  fe=(f+f[::-1])/2; even=float(np.sum(fe**2)*h)
  F=np.abs(np.fft.rfft(f));fr=np.fft.rfftfreq(n,d=h)
  dom=float(fr[1+np.argmax(F[1:])]); 
  cen=float(np.sum(fr*F**2)/np.sum(F**2))
  hi=float(np.sum(F[fr>0.25/h]**2)/np.sum(F**2))  # power above half-Nyquist
  zeros=[float((u[i]+u[i+1])/2) for i in range(n-1) if np.sign(f[i])!=np.sign(f[i+1])]
  imax=int(np.argmax(np.abs(f)))
  return dict(zero_crossings=zc,zeros=zeros[:40],edge_mass_outer10pct_each_side=edge,participation_ratio=pr,
    diff_energy_over_h2=rough,diff_energy_ratio=rough_ratio,even_fraction=even,dom_freq=dom,spectral_centroid_freq=cen,
    power_above_half_nyquist=hi,argmax_u=float(u[imax]),max_abs=float(np.abs(f).max()))
def run(A,n,variants=('full','gamma','p23')):
  col,gcol,B=build.get(A,n);h=A/n;u=-A/2+(np.arange(n)+.5)*h
  out={}
  for var in variants:
    c={'full':col,'gamma':gcol,'p23':gcol+primecol(A,n,maxn=3)}[var]
    t=time.time();Q,Z,ev,Vs=solve(c,B)
    vs=[]
    for j in range(Vs.shape[1]):
      v=Vs[:,j]/np.sqrt(np.sum(Vs[:,j]**2)); f=v/np.sqrt(h)
      if f[n//2-1]+f[n//2]<0 or (abs(f[n//2])<1e-3*abs(f).max() and f[np.argmax(abs(f))]<0): f=-f
      vs.append(f)
    res=np.abs(B.T@(vs[0]*np.sqrt(h)))
    r=dict(A=A,n=n,variant=var,constrained_ev=ev.tolist(),gap_ratio=float(ev[1]/ev[0]),moment_residuals=res.tolist(),
           diag=diag(vs[0],u,A,h),diag2=diag(vs[1],u,A,h))
    # rayleigh split for full
    if var=='full':
      g=la.toeplitz(gcol); v=vs[0]*np.sqrt(h)
      r['rayleigh_gamma']=float(v@g@v); r['rayleigh_prime']=float(v@(la.toeplitz(col-gcol))@v)
      e,Uq=la.eigh(Q,subset_by_index=[0,0]); q=Uq[:,0]/np.sqrt(h)
      if q[n//2]<0:q=-q
      r['Q_negative_ev']=float(e[0])
      r['overlap_with_Qneg']=float(abs(np.sum(q*vs[0])*h))
      qp=Z@(Z.T@(q*np.sqrt(h)))/np.sqrt(h); qp/=np.sqrt(np.sum(qp**2)*h)
      r['overlap_with_projected_Qneg']=float(abs(np.sum(qp*vs[0])*h))
      out['qneg']=q
    out[var]=(r,np.array(vs))
    print(A,n,var,ev[:3],'%.1fs'%(time.time()-t),flush=True)
  return out
if __name__=='__main__':
  n=int(sys.argv[1]); keys=sys.argv[2].split(',') if len(sys.argv)>2 else list(WIN)
  os.makedirs('res',exist_ok=True)
  for k in keys:
    A=WIN[k]; o=run(A,n, ('full','gamma','p23') if n<=2048 else ('full',))
    np.savez(f'res/{k}_{n}.npz',**{v:o[v][1] for v in o if v!='qneg'},qneg=o['qneg'])
    json.dump({v:o[v][0] for v in o if v!='qneg'},open(f'res/{k}_{n}.json','w'))

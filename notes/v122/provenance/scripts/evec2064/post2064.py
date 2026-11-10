import numpy as np, json, os, glob
from scipy.optimize import brentq
from mpmath import zetazero
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from analyze2064 import WIN
G=[float(zetazero(k).imag) for k in range(1,16)]
def load(k,n,var='full',j=0):
  f=f'res/{k}_{n}.npz'
  if not os.path.exists(f): return None
  return np.load(f)[var][j]
def ft(f,A,t,odd=False):
  n=len(f);h=A/n;e=-A/2+np.arange(n+1)*h
  t=np.atleast_1d(t)[:,None]
  if odd: K=-(np.cos(t*e[1:])-np.cos(t*e[:-1]))/t   # int sin(tu)
  else: K=(np.sin(t*e[1:])-np.sin(t*e[:-1]))/t       # int cos(tu)
  return K@f
def zeros(f,A,odd=False,tmax=45):
  t=np.linspace(.3,tmax,9000);F=ft(f,A,t,odd)
  z=[brentq(lambda s:ft(f,A,s,odd)[0],t[i],t[i+1],xtol=1e-12) for i in range(len(t)-1) if np.sign(F[i])!=np.sign(F[i+1])]
  return z,float(np.abs(F).max())
def match(z):
  out=[]
  for g in G:
    if g>max(z+[0])+1: break
    d=min(z,key=lambda x:abs(x-g)) if z else np.nan
    out.append(dict(gamma=g,nearest=d,err=d-g))
  return out
NS=[512,1024,2048,4096,8192]
res={}
for k,A in WIN.items():
  for n in NS:
    f=load(k,n)
    if f is None: continue
    J=json.load(open(f'res/{k}_{n}.json'))
    z,mx=zeros(f,A); f2=load(k,n,j=1); z2,_=zeros(f2,A,odd=True)
    rel=[float(abs(ft(f,A,g)[0])/mx) for g in G[:6]]
    res[f'{k}|{n}']=dict(A=A,n=n,full=J['full'],ft_zeros_even=z,ft_zero_match_even=match(z),rel_absFhat_at_gamma=rel,
       ft_zeros_mode2_odd=z2,ft_zero_match_mode2=match(z2))
    if 'gamma' in J:
      for var in ['gamma','p23']:
        fv=load(k,n,var); zv,_=zeros(fv,A,odd=(J[var]['diag']['even_fraction']<.5))
        res[f'{k}|{n}'][var]=dict(constrained_ev=J[var]['constrained_ev'],ft_zeros=zv[:10],even=J[var]['diag']['even_fraction'])
# grid overlaps (exact, nested)
def ov(k,n1,n2):
  a=load(k,n1);b=load(k,n2)
  if a is None or b is None: return None
  a=np.repeat(a,n2//n1); return float(abs(np.sum(a*b))*(WIN[k]/n2))
gov={k:{f'{n1}-{n2}':ov(k,n1,n2) for n1,n2 in [(512,1024),(1024,2048),(512,2048),(2048,4096),(4096,8192)] if ov(k,n1,n2) is not None} for k in WIN}
# A overlaps in scaled coordinate x=2u/A
X=(np.arange(4000)+.5)/4000*2-1
def onx(k,n):
  f=load(k,n);m=len(f);idx=np.minimum((( X+1)/2*m).astype(int),m-1);g=f[idx];return g/np.sqrt(np.sum(g**2))
keys=list(WIN);aov={}
for i in range(len(keys)-1):
  aov[f'{keys[i]}->{keys[i+1]}']=float(abs(onx(keys[i],2048)@onx(keys[i+1],2048)))
aov['1.5->3.0']=float(abs(onx('1.5',2048)@onx('3.0',2048)));aov['1.1->3.0']=float(abs(onx('1.1',2048)@onx('3.0',2048)))
json.dump(dict(zeta_gammas=G,rows=res,grid_overlaps=gov,A_overlaps_scaled_n2048=aov),open('evec2064.json','w'),indent=1)
# downsampled vectors
ds={}
for k,A in WIN.items():
  f=load(k,2048); ds[k]=dict(A=A,u=(-A/2+(np.arange(2048)+.5)*A/2048)[::8].tolist(),v=f[::8].tolist(),v_mode2=load(k,2048,j=1)[::8].tolist())
json.dump(ds,open('vectors_n2048_every8.json','w'))
# FIGURES
fig,ax=plt.subplots(1,2,figsize=(12,4.5))
for k in ['0.694','1.0','1.1','1.5','2.0','2.5','3.0']:
  A=WIN[k];f=load(k,2048);u=-A/2+(np.arange(2048)+.5)*A/2048
  ax[0].plot(u,f,label=f'A={k}');ax[1].plot(2*u/A,f*np.sqrt(A/2),label=f'A={k}')
for p in [2,3,4,5,7,8,9,11,13,16,17,19]:
  if np.log(p)<1.5: ax[0].axvline(np.log(p),color='k',lw=.4,ls=':');ax[0].axvline(-np.log(p),color='k',lw=.4,ls=':')
ax[0].set_xlabel('u');ax[0].set_title('constrained min eigenvector of W|E0, n=2048 (L2: int v^2 du=1)\ndotted: ±log n, active prime powers');ax[0].legend(fontsize=7)
ax[1].set_xlabel('x=2u/A');ax[1].set_title('same, rescaled window');plt.tight_layout();plt.savefig('fig1_profiles_vs_A.png',dpi=130)
fig,ax=plt.subplots(1,3,figsize=(15,4.3))
for j,k in enumerate(['1.5','2.0','3.0']):
  A=WIN[k]
  for n in NS:
    f=load(k,n)
    if f is None: continue
    u=-A/2+(np.arange(n)+.5)*A/n;ax[j].plot(u,f,lw=1,label=f'n={n}')
  ax[j].set_title(f'A={k}: grid refinement');ax[j].legend(fontsize=7);ax[j].set_xlabel('u')
plt.tight_layout();plt.savefig('fig2_grid_refinement.png',dpi=130)
fig,ax=plt.subplots(2,1,figsize=(11,7.5));t=np.linspace(.3,45,4000)
for k in ['1.1','1.5','2.0','3.0']:
  A=WIN[k];n=4096 if load(k,4096) is not None else 2048;f=load(k,n);F=ft(f,A,t)
  ax[0].plot(t,np.log10(np.abs(F)+1e-16),lw=.8,label=f'A={k}, n={n}')
  f2=load(k,n,j=1);ax[1].plot(t,np.log10(np.abs(ft(f2,A,t,True))+1e-16),lw=.8,label=f'A={k}')
for a in ax:
  for g in G:
    if g<45:a.axvline(g,color='r',lw=.5,ls='--')
  a.set_ylim(-7,.5);a.legend(fontsize=7)
ax[0].set_title('log10|Fhat(t)| of constrained ground state (even, cos transform); red dashed = zeta zero ordinates')
ax[1].set_title('2nd constrained mode (odd, sine transform)');ax[1].set_xlabel('t')
plt.tight_layout();plt.savefig('fig3_fourier_zeta_zeros.png',dpi=130)
# eigenvalue vs h
fig,ax=plt.subplots(figsize=(6,4.5))
for k in ['1.0','1.1','1.5','2.0','2.5','3.0']:
  pts=[(WIN[k]/n,res[f'{k}|{n}']['full']['constrained_ev'][0]) for n in NS if f'{k}|{n}' in res]
  ax.loglog(*zip(*pts),'o-',label=f'A={k}')
ax.set_xlabel('h=A/n');ax.set_ylabel('constrained min (Ritz upper bound)');ax.legend(fontsize=7);ax.set_title('floor vs mesh: slope ~2 = discretization')
plt.tight_layout();plt.savefig('fig4_eigenvalue_vs_h.png',dpi=130)
print(json.dumps(gov,indent=0));print(aov)
for key in ['1.0|4096','1.1|4096','1.5|4096','2.0|4096','2.5|4096','3.0|4096','2.0|8192','3.0|8192','1.5|512','3.0|512']:
  if key in res:
    r=res[key];print(key,'ev',['%.3e'%x for x in r['full']['constrained_ev'][:3]])
    print('  even err',[ (round(m['gamma'],3),'%.1e'%m['err']) for m in r['ft_zero_match_even']][:8])
    print('  odd2 err',[ (round(m['gamma'],3),'%.1e'%m['err']) for m in r['ft_zero_match_mode2']][:8])
    print('  zeros',np.round(r['ft_zeros_even'][:12],4)); print('  rel',['%.1e'%x for x in r['rel_absFhat_at_gamma']])
for key in ['2.0|2048','3.0|2048']:
  for v in ['gamma','p23']: print(key,v,np.round(res[key][v]['ft_zeros'],3))

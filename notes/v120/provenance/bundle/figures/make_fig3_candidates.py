# Fig 3: two explicit independent representer candidates fail (matching1983). Uses scripts/matching1983/match1983.py resp().
# h1 edge log: EXACT mechanism, numbers NUM. h2 prime-2 kink at A=1: EXACT jump a2*sinh(A/4)/2=0.06191. RH is not proved.
import sys, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts', 'matching1983'))
from match1983 import resp
fig,ax=plt.subplots(1,2,figsize=(13,5))
A=0.6; d=np.geomspace(1e-5,0.3,40); v=A/2-d
phi=np.array([resp(A,x,'h1')/np.cosh(x/2) for x in v])
ax[0].semilogx(d,phi,'o-',ms=3,color='#d7191c',label=r'$r_{h_1}(v)/\cosh(v/2)$, A=0.6')
ax[0].semilogx(d,phi[-1]+0.5*np.log(d[-1]/d),'k--',lw=1,label=r'slope $\frac{1}{2}\log(1/d)$ (from $k(a)\sim 1/2a$)')
ax[0].set_xlabel('distance to window edge d'); ax[0].set_ylabel('response / cosh')
ax[0].set_title(r'(3a) $h_1=\cosh(u/2)1_{win}$: log edge divergence $\Rightarrow$ not $\kappa\cosh$',fontsize=11); ax[0].legend(fontsize=9)
A=1.0; v0=np.log(2)-A/2; vv=np.linspace(-A/2+0.02,A/2-0.02,121)
r=np.array([resp(A,x,'h2') for x in vv]); c=np.cosh(vv/2); kap=(r*c).sum()/(c*c).sum()
ax[1].plot(vv,r-kap*c,color='#2b83ba',label=r'$r_{h_2}-\kappa\cosh$ (least squares $\kappa$), A=1')
for s in (1,-1): ax[1].axvline(s*v0,color='#EE7733',ls=':')
ax[1].text(v0+0.01,ax[1].get_ylim()[0]*0.8 if ax[1].get_ylim()[0]<0 else 0,r'$\pm(\log 2-A/2)$: kink, jump $a_2\sinh(A/4)/2=0.0619$',fontsize=9,color='#EE7733')
ax[1].set_xlabel('v'); ax[1].set_title(r'(3b) Dirichlet $h_2$: prime-2 translate of edge kink [jump EXACT]',fontsize=11); ax[1].legend(fontsize=9,loc='upper center')
fig.text(0.01,0.01,'Shows only that these TWO candidates fail; not a no-go for all independent representers. Numbers double precision, uncertified.',fontsize=9)
fig.text(0.99,0.01,'The Riemann Hypothesis is not proved.',ha='right',color='#d7191c',fontsize=9)
fig.tight_layout(rect=(0,0.04,1,1)); fig.savefig('fig3_candidates.svg'); fig.savefig('fig3_candidates.png',dpi=140); print('ok')

# atlas1987 prototype figures (script-generated; values copied from cited scratch notes; NUM = uncertified double precision).
# RH is not proved.
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
FOOT='The Riemann Hypothesis is not proved.'
# ---------- Fig 1: exact ledger + one numerical instance ----------
fig,ax=plt.subplots(1,2,figsize=(13,5.2),gridspec_kw={'width_ratios':[1.15,1]})
ax[0].axis('off')
txt=[r'$W(F)=P(F)+B(F)$,  $P=2\,\mathrm{ev}_+\mathrm{ev}_-=2(C^2-S^2)$,  $\mathrm{ev}_\pm=\int F e^{\pm u/2}$',
     r'$B(F)=H_A(F)-M_A\|F\|^2=\frac{1}{2\pi}\int m_A(x)|\hat F(x)|^2dx$',
     r'$m_A(x)=\mathrm{Re}\,\psi(1/4+ix/2)-\log\pi-2\sum_{\log n<A}\frac{\Lambda(n)}{\sqrt{n}}\cos(x\log n)$',
     r'$M_A=-m_A(0)=-K_0+2\sum_{\log n<A}\Lambda(n)n^{-1/2}$,   $K_0=\psi(\frac{1}{4})-\log\pi=-5.37218$',
     r'$E_0=\{\mathrm{ev}_+=\mathrm{ev}_-=0\}$ kills $P$ only; $M_A\|F\|^2$ remains on $E_0$',
     r'Local ledger (covariance1956): $W_p=\log p\,(\|F\|^2-\langle F,P_pF\rangle)$, $P_p=\sum_k p^{-|k|/2}T_{k\log p}$',
     r'Sign mechanism: NOT supplied (covariances enter subtracted)']
for i,s in enumerate(txt): ax[0].text(0,0.95-0.13*i,s,fontsize=11.5,va='top')
ax[0].set_title('(1) Exact window ledger [identities]',loc='left',fontsize=13,weight='bold')
lab=['arch','p=2','p=3','p=5','total W']; val=[0.090,9.092,-9.001,-0.0016,0.1788]
cols=['#2b83ba','#1a9641','#d7191c','#d7191c','k']
ax[1].bar(lab,val,color=cols); ax[1].axhline(0,color='grey',lw=.8)
for i,v in enumerate(val): ax[1].text(i,v+(0.3 if v>=0 else -0.6),f'{v:+.4g}',ha='center',fontsize=10)
ax[1].set_title('Per-place contributions, A=2, F=LG, G=sin$^8$ [NUM, uncertified]',fontsize=11)
ax[1].set_ylabel('contribution to W(F)')
fig.text(0.99,0.01,FOOT,ha='right',color='#d7191c',fontsize=9); fig.tight_layout(rect=(0,0.03,1,1))
fig.savefig('fig1_ledger.svg'); fig.savefig('fig1_ledger.png',dpi=140); plt.close(fig)
# ---------- Fig 2: one form B: projective polarity + H1 skew -> H2 symmetric ----------
fig,ax=plt.subplots(1,2,figsize=(13,5.4))
t=np.linspace(-4,4,400); a=ax[0]; a.plot(t,t**2/4,'k',lw=2,label=r'model discriminant conic $T^2-4QZ=0$ (null)')
a.fill_between(t,t**2/4,6,color='#1a9641',alpha=.12,label=r'interior $Q<0$ (here $G$ pos. def.)')
a.plot([0],[1],'o',color='#AA4499',ms=9); a.text(.15,1.1,r'$h=(0{:}1{:}1)$, $Q(h)=-4$ (focus)',color='#AA4499')
a.axhline(-1,color='#AA4499',ls='--'); a.text(-3.9,-1.6,r'polar $h^{\perp}$: $q=-1$ (directrix); $Q|_{h^\perp}=v_T^2+4v_Z^2>0$',color='#AA4499',fontsize=9)
a.axvline(0,color='#EE7733',lw=1); a.text(.1,4.6,r'axis span$(h,x_\infty)$: signature (1,1)',color='#EE7733',fontsize=9)
for p0 in [-1.5,-.75,.75,1.5]: a.plot(t,p0*t-p0**2,color='grey',lw=.6)
a.text(-3.9,5.5,r'$x_\infty=(0{:}1{:}0)$ null; polar $Z=0$ contains $x_\infty$ (degenerate complement)',fontsize=9)
a.set_ylim(-2,6); a.set_xlim(-4,4); a.set_xlabel('t'); a.set_ylabel('q'); a.legend(loc='center right',fontsize=8.5)
a.set_title('(2a) one symmetric form B, signature (2,1): tangency and sign',fontsize=11.5,loc='left')
b=ax[1]; b.axis('off')
rows=[r'Curve $C$: $E(u,v)=\int u\wedge v$ alternating; $H^{1,0},H^{0,1}$ isotropic; $i\int\alpha\wedge\bar\alpha>0$',
      r'Product $C\times C$ (Künneth): $I(a\otimes b,c\otimes d)=-E(a,c)E(b,d)$  (symmetric)',
      r'Elliptic, area 1, $E(dz,d\bar z)=-2i$:',
      r'  mixed real $(1,1)$ primitive: $\alpha=dz\otimes d\bar z+d\bar z\otimes dz$:  $I(\alpha,\alpha)=-8<0$',
      r'  $(2,0)+(0,2)$: $\beta=dz\otimes dz+d\bar z\otimes d\bar z$:  $I(\beta,\beta)=+8>0$',
      r'Not all of $H^1\otimes H^1$ is negative; mixed sector $\neq$ all of primitive $H^{1,1}$ in general',
      r'Model/calibration only: no arithmetic map $E_0\to$ primitive $(1,1)$ is constructed']
for i,s in enumerate(rows): b.text(0,0.95-0.13*i,s,fontsize=10.5,va='top')
b.set_title('(2b) weight-1 skew $\\to$ weight-2 symmetric (hand algebra)',fontsize=11.5,loc='left')
fig.text(0.99,0.01,FOOT,ha='right',color='#d7191c',fontsize=9); fig.tight_layout(rect=(0,0.03,1,1))
fig.savefig('fig2_polarity.svg'); fig.savefig('fig2_polarity.png',dpi=140); plt.close(fig)
# ---------- Fig 3: constrained spectrum (moment1975 table) ----------
fig,ax=plt.subplots(figsize=(9.5,5.2))
A=[0.6,1.0]; l1=[-1.114,-1.977]; l2=[0.732,0.0134]; e0lo=[0.6918,0.01182]; e0hi=[0.6920,0.01197]
ax.plot(A,[abs(x) for x in l1],'s-',color='#d7191c',label=r'$|\lambda_1(B_e)|$ (the one negative even mode)')
ax.plot(A,l2,'o-',color='#2b83ba',label=r'$\lambda_2(B_e)$ (caps the constrained margin)')
ax.errorbar(A,[(a+b)/2 for a,b in zip(e0lo,e0hi)],yerr=[[ (b-a)/2 for a,b in zip(e0lo,e0hi)]]*2,fmt='D',color='#1a9641',capsize=4,label=r'$\min B|_{E_0}$ estimate (not certified)')
ax.axvline(2.0,color='grey',ls=':'); ax.text(1.62,0.03,'A=2: near-null cluster ~1e-15\nsign UNRESOLVED',fontsize=9)
ax.set_yscale('log'); ax.set_xlim(0.4,2.3); ax.set_xlabel('window width A'); ax.set_ylabel('value (log scale)')
ax.set_title('(S) Two moments vs the dangerous direction: alignment 0.970/0.991 [NUM, uncertified;\nRitz values are upper bounds for minima, not a lower-bound proof]',fontsize=10.5)
ax.legend(fontsize=8.5,loc='upper right'); fig.text(0.99,0.01,FOOT,ha='right',color='#d7191c',fontsize=9)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('figS_moment_spectrum.svg'); fig.savefig('figS_moment_spectrum.png',dpi=140); plt.close(fig)
# ---------- Animation: interior h_s=(0,1,s) -> null x_inf ----------
fig,ax=plt.subplots(1,2,figsize=(11,4.8)); S=np.concatenate([np.linspace(1,0.05,40),np.full(8,0.05)])
def frame(i):
    s=S[i]
    for a in ax: a.cla()
    a=ax[0]; a.plot(t,t**2/4,'k',lw=2); a.fill_between(t,t**2/4,30,color='#1a9641',alpha=.1)
    for p0 in np.linspace(-2,2,9): a.plot(t,p0*t-p0**2,color='grey',lw=.5)
    yh=1/s; a.plot([0],[min(yh,9.6)],'o',color='#AA4499',ms=9); a.axhline(max(-yh,-9.6),color='#AA4499',ls='--')
    a.set_ylim(-10,10); a.set_xlim(-4,4)
    a.set_title(f'$h_s=(0,1,s)$, s={s:.2f}: $Q(h_s)=-4s$ (homogeneous); affine rep. $(0,1/s,1)$: $Q=-4/s$\npoint q=1/s, polar q=-1/s',fontsize=9)
    a.set_xlabel('t'); a.set_ylabel('q')
    b=ax[1]; th=np.linspace(0,2*np.pi,300); b.plot(np.cos(th),np.sin(th)/(2*np.sqrt(s)),color='#AA4499')
    b.set_xlim(-1.5,1.5); b.set_ylim(-12,12); b.set_xlabel('$v_T$'); b.set_ylabel('$v_Q$')
    b.set_title(r'complement $v_Z=-s\,v_Q$: unit set of $Q=v_T^2+4s\,v_Q^2$'+'\n(degenerates as $s\\to0$: interior $\\to$ null boundary)',fontsize=10)
fig.text(0.99,0.01,FOOT+' Schematic algebra, not a physical recording.',ha='right',color='#d7191c',fontsize=8)
anim=FuncAnimation(fig,frame,frames=len(S)); anim.save('anim_polarity.gif',writer=PillowWriter(fps=8),dpi=80); plt.close(fig)
print('ok')

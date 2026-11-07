import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(15,4.2))
for ax,A in zip(axs,['3_2','2','3']):
    d=json.load(open(f'controls_{A}_12.json')); c=np.array(d['rho_curve'])
    ax.plot(c[:,0],c[:,1],'k-',lw=1.5,label=r'$\rho_f(b)=\langle f,T_bf\rangle/\|f\|^2$ (lowest mode)')
    ax.axhline(0,color='gray',lw=.6)
    for p in d['primes']:
        col='tab:green' if p['contrib']>0 else 'tab:red'
        ax.vlines(p['logn'],0,p['contrib'],color=col,lw=4,alpha=.8)
        if abs(p['contrib'])>2e-3: ax.annotate(str(p['n']),(p['logn'],p['contrib']),textcoords='offset points',xytext=(3,3),fontsize=8)
    ax.set_title(f"window A={A.replace('_','/')}: μmin={d['mu'][0]:.1e}, M_A={d['M']:.1f}\narch springs {d['decomp']['arch_springs']:.3f} vs K(0)={d['decomp']['K0']:.3f}",fontsize=9)
    ax.set_xlabel('lag b (log scale)'); ax.set_ylim(-1.05,1.05)
axs[0].set_ylabel(r'$\rho_f(b)$;  bars: contribution $-2a_n\rho_f(\log n)$')
axs[0].legend(fontsize=7,loc='lower left')
fig.suptitle('Spring domination is a signed balance: green = prime lag helps (anti-correlated), red = hurts.  Galerkin K=12, exact ker P, 50 digits (scratch)',fontsize=10)
plt.tight_layout(); plt.savefig('fig_mode_autocorr.png',dpi=130)
for A in ['3_2','2','3']:
    d=json.load(open(f'controls_{A}_12.json')); c=np.array(d['rho_curve']); z=c[1:,0][np.sign(c[1:,1])!=np.sign(c[:-1,1])]
    print(A,'zero crossings of rho:',np.round(z,3),' sum prime contrib',sum(p['contrib'] for p in d['primes']))

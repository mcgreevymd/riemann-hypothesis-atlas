"""Reproducible figures for night1916 (data-driven; no generated illustration).
Inputs: ../../spring1891/controls_{1,3_2,2,3}_12.json, ../../spring1891/spring1891_conv.json,
        values printed by ../../compat1907/checks1907.py (log: ../src/checks1907_rerun.log), ../tests/test1_result.json.
Outputs: fig1_springs.{svg,png}, fig2_boundary.{svg,png}, fig3_mechanisms.{svg,png}."""
import json, re, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
plt.rcParams.update({'font.size':9,'svg.fonttype':'none'})   # editable text in SVG
S='../../spring1891/'
def save(fig,name):
    fig.savefig(name+'.svg'); fig.savefig(name+'.png',dpi=140); plt.close(fig)
# ---------------- Fig 1: zeros-blind spring network ----------------
fig=plt.figure(figsize=(14,4.6)); gs=fig.add_gridspec(1,3,width_ratios=[1.1,1.3,1.0])
ax=fig.add_subplot(gs[0]); A=3.0
kinf=lambda a: np.exp(-a/2)/(1-np.exp(-2*a))
d=json.load(open(S+'controls_3_12.json'))
ax.set_title('W on a window = springs (zeros-blind input)\nW(f)=K(0)‖f‖²+∫k∞(a)‖f−T_af‖²da−2Σaₙ⟨f,T_{log n}f⟩',fontsize=9)
xs=np.linspace(0,A,13); ax.plot(xs,0*xs,'ko',ms=3)
for p in d['primes']:
    L=p['logn']; col='tab:green' if p['contrib']>0 else 'tab:red'
    for x0 in xs:
        if x0+L<=A+1e-9:
            t=np.linspace(0,np.pi,30); r=L/2; ax.plot(x0+r-r*np.cos(t),0.12*np.sqrt(p['a'])*L*np.sin(t)+0*t,color=col,lw=0.6,alpha=.6)
    ax.text(L,-0.08,'log %d'%p['n'],fontsize=7,ha='center',rotation=90,va='top')
aa=np.linspace(0.02,A,200); ax.fill_between(aa,-0.55,-0.55+0.08*kinf(aa)/kinf(0.02)*6,color='tab:blue',alpha=.35)
ax.text(1.5,-0.62,r'archimedean Lévy spring density $k_\infty(a)=e^{-a/2}/(1-e^{-2a})$ (always restoring)',fontsize=7,ha='center')
ax.text(0.02,0.42,r'arcs: prime-power couplings $a_n=\Lambda(n)n^{-1/2}$ at lag $\log n$'+'\n(green/red = sign of the contribution for the lowest mode, A=3)',fontsize=7)
ax.set_ylim(-0.75,0.55); ax.set_xlim(-0.1,A+0.1); ax.axis('off')
ax=fig.add_subplot(gs[1]); c=np.array(d['rho_curve'])
ax.plot(c[:,0],c[:,1],'k-',lw=1.4,label='ρ_f(b)=⟨f,T_bf⟩/‖f‖² (lowest Galerkin mode)')
ax.axhline(0,color='gray',lw=.5)
for p in d['primes']:
    col='tab:green' if p['contrib']>0 else 'tab:red'; ax.vlines(p['logn'],0,p['contrib'],color=col,lw=5,alpha=.85)
    if abs(p['contrib'])>5e-3: ax.annotate('n=%d: %+.3f'%(p['n'],p['contrib']),(p['logn'],p['contrib']),xytext=(4,4 if p['contrib']>0 else -12),textcoords='offset points',fontsize=7)
ax.set_xlabel('lag b'); ax.set_ylabel('ρ_f(b);  bars: −2aₙρ_f(log n)')
ax.set_title('Signed autocorrelation decides: window A=3, μ_min≈%.1e\n(arch springs %.3f vs −K(0)=%.3f; Galerkin K=12, exact E0 basis)'%(d['mu'][0],d['decomp']['arch_springs'],-d['decomp']['K0']),fontsize=9)
ax.legend(fontsize=7,loc='lower right'); ax.set_ylim(-0.9,1.05)
ax=fig.add_subplot(gs[2]); conv=json.load(open(S+'spring1891_conv.json'))
As=[0.6,1.0,1.5,2.0,3.0]; mu=[conv['A=%.1f'%x]['14']['mu_L2'] for x in As]; M=[conv['A=%.1f'%x]['14']['M'] for x in As]
ax.semilogy(As,M,'s-',color='tab:orange',label=r'"mass" $M_A=-K(0)+2\sum_{n\leq e^A}a_n$ (grows)')
ax.semilogy(As,mu,'o-',color='k',label='Galerkin min eigenvalue of W|E0, K=14\n(upper bound; A=3 value at precision limit)')
ax.set_xlabel('window length A'); ax.legend(fontsize=7); ax.grid(alpha=.3,which='both')
ax.set_title('Near-cancellation, not domination:\npositive Galerkin value is NOT a certificate',fontsize=9)
fig.suptitle('Fig. 1  Zeros-blind spring network for the Weil form on a window (scratch numerics; RH not proved)',fontsize=10)
fig.tight_layout(); save(fig,'fig1_springs')
# ---------------- Fig 2: Fourier-scale-Poisson boundary ----------------
log=open('../src/checks1907_rerun.log').read()
dens=[float(v) for v in re.findall(r'‖ψ-φ‖₂=([0-9.]+)',log)]; win=[float(v) for v in re.findall(r'dist\(Φ,E0_L\)=([0-9.]+)',log)]
t1=json.load(open('../tests/test1_result.json'))
fig,axs=plt.subplots(1,3,figsize=(16,5.2),gridspec_kw={'width_ratios':[1.45,1,1]})
ax=axs[0]; ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,10)
def box(x,y,w,h,t,fc):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',fc=fc,ec='k',lw=.8)); ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=7)
def arr(x0,y0,x1,y1,t=''):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle='->',mutation_scale=10,lw=.8)); ax.text((x0+x1)/2+.1,(y0+y1)/2,t,fontsize=7)
box(0.2,8,4,1.4,'f ∈ S(A_Q)\n(Schwartz–Bruhat)','#eef')
box(5.6,8,4.2,1.4,'b(f)=(f(0), ∫f dx) ∈ C²\n(Tate/Poisson boundary data)','#ffe')
arr(4.3,8.7,5.5,8.7,'b')
box(0.2,5.2,4,1.8,'Fourier F:  b(Ff)=σ b(f)\nU_a=|a|^{-1/2}R_a:  b(U_af)=D_a b(f)\nD_a=diag(|a|^{-1/2},|a|^{1/2}),  FU_a=U_{a⁻¹}F','#efe')
box(5.6,5.2,4.2,1.8,'smearing Θ_F=∫F(t)U_{e^t}dt:\nb(Θ_Ff)=diag(ev₀F, ev₁F) b(f)\nΘ_F S(A)⊂S(A)₀ ⇔ F∈E0','#efe')
box(0.2,2.2,4,2.0,'only invariant Hermitian form\non C² under all D_a and σ:\nH=z[[0,1],[1,0]]  sig (1,1)\n⇒ boundary cannot supply sign','#fee')
box(5.6,2.2,4.2,2.0,'E0={ev₀=ev₁=0} (ideal; Fourier\nreflects F(−u), adjoint gives F♯)\nS₀, E0: algebraic codim 2 but\nL²-dense; window: closed codim 2','#fee')
box(2.2,0.1,5.6,1.4,'sign must come from the bulk (W on E0):\nmissing independent positive map — not constructed','#ddd')
arr(2.2,7.9,2.2,7.1); arr(7.7,7.9,7.7,7.1); arr(2.2,5.1,2.2,4.3); arr(7.7,5.1,7.7,4.3); arr(5,2.1,5,1.6)
ax.set_title('(a) exact transformation laws (compat1907; Connes 1999 eqs (6),(10),(11))',fontsize=9)
ax=axs[1]; u=np.linspace(-2.5,2.5,401); X,Y=np.meshgrid(u,u); ax.contour(X,Y,2*X*Y,levels=np.linspace(-6,6,13),cmap='coolwarm',linewidths=.7)
for qq,mk in [(2,'o'),(3,'s'),(5,'^')]:
    nn=np.arange(-2,3); ax.plot(qq**(-nn/2),qq**(nn/2),mk,ms=5,label='F_q analogue: (D·v, D·h) of q^(-n/2)·Graph(Frobⁿ), q=%d'%qq)
ax.plot(u,u,'k:',lw=.7); ax.text(1.7,1.95,'σ (Fourier) axis',fontsize=7,rotation=45)
ax.set_xlim(-2.5,2.5); ax.set_ylim(-2.5,2.5); ax.set_aspect('equal'); ax.set_xlabel('b₀ = f(0)  ↔  D·v'); ax.set_ylabel('b₁ = ∫f  ↔  D·h')
ax.legend(fontsize=6.5,loc='lower left'); ax.axhline(0,color='gray',lw=.4); ax.axvline(0,color='gray',lw=.4)
ax.set_title('(b) boundary form 2b₀b₁ (hyperbolic, indefinite); D_a moves along\nhyperbolas. F_q model (Test 1): D²=2b₀b₁+D_⊥² (same diagonal law;\ndiscrete Frobenius samples, not the continuous moments)',fontsize=9)
ax=axs[2]; dl=[0.1,0.01,0.001,0.0001]; ax.loglog(dl,dens,'o-k',label='‖ψ−φ‖₂ with ψ∈S₀ (shrinking+broad bump), ψ(0)=∫ψ=0')
ax.loglog(dl,0.5159*np.sqrt(np.array(dl)/0.1),'k:',lw=.7,label='∝ δ^{1/2} (proof bound rate)')
ax2=ax.twiny(); Ls=[2,4,8]; ax2.plot(Ls,win,'s-',color='tab:purple'); ax2.set_xlabel('log-line window half-width L (purple): dist(Φ,E0_L)>0, closed codim 2',color='tab:purple',fontsize=8)
ax.set_xlabel('δ = 1/R'); ax.set_ylabel('L² distance'); ax.legend(fontsize=7,loc='lower right'); ax.invert_xaxis()
ax.set_title('(c) topology: dense globally, closed on a fixed window\n⇒ "P" = moment map b, not a global orthogonal projection',fontsize=9)
fig.suptitle('Fig. 2  Additive Fourier × multiplicative scaling × the two Poisson boundary functionals (exact, checked numerically on R)',fontsize=10)
fig.tight_layout(); save(fig,'fig2_boundary')
# ---------------- Fig 3: positive-square mechanisms ----------------
rows=[('Robertson–Schrödinger','w=V+iħσ/2 ≥0 (state)','σ (commutator) antisym.','positive state φ','no φ built from primes/Γ'),
('Bogomolny / instanton','‖F^∓‖² (Hodge star of a metric)','top. charge k (orientation)','Riemannian metric','no arithmetic Hodge star'),
('Hodge index (F_q: C×C)','primitive (1,1) = ASD ⇒ D²=−‖α‖²','2b₀b₁ boundary (h,v)','ample class / Kähler ω','surface Spec Z×Spec Z absent'),
('No-ghost (GT 1972)','transverse Fock norms','II₁,₁ light cone, c=26','positive transverse factor','H₊ not constructed (v1.15)'),
('SUSY {Q,Q†}','‖Qψ‖²+‖Q†ψ‖² ⇒ H≥|Z|','central charge Z','Hilbert space + Q','no arithmetic Q'),
('Connes 1999 Thm 5','Tr(S_Λ V(f∗f*)) = 2(f∗f*)(1)·log′Λ','subtraction Q′_{Λ,0}','order Q′_{Λ,0}≤S_Λ','proved char p only; ⇔ RH'),
('CC21 Sonin (∞)','Tr(ϑ(g)Sϑ(g)*) ≥0','vanishing at ±i/2, 0','compression to Sonin space','archimedean, small support')]
fig,ax=plt.subplots(figsize=(14,4.3)); ax.axis('off')
cols=['mechanism','positive square (source of ≥0)','indefinite / topological term','independent positive input','status for ζ']
cc=['#ffffff','#dff0d8','#fde2e2','#d9edf7','#eeeeee']
tb=ax.table(cellText=[list(r) for r in rows],colLabels=cols,loc='upper center',cellLoc='left',colWidths=[.15,.25,.19,.2,.21])
tb.auto_set_font_size(False); tb.set_fontsize(8); tb.scale(1,1.65)
for (i,j),cell in tb.get_celld().items():
    cell.set_facecolor('#cccccc' if i==0 else cc[j]); cell.set_edgecolor('#888')
ax.text(0.5,0.02,'Common pattern (each row is a standard result in its own setting): Q = ‖Φ·‖² + (indefinite boundary/charge term), with ‖·‖ from an INDEPENDENT positive structure.\n'
        'Arithmetic target (OPEN, not constructed): Φ: E0 → H₊ built from Euler factors + Γ data, scaling-equivariant, window-consistent,\n'
        'with ‖Φg‖² = W(g∗g♯) exactly and failing for Davenport–Heilbronn. Any such exact Φ is equivalent to RH.',ha='center',fontsize=9,transform=ax.transAxes,
        bbox=dict(boxstyle='round',fc='#fff8dc',ec='k'))
ax.set_title('Fig. 3  Positive-square mechanisms converge on one missing independent map (schematic of checked statements; nothing here is constructed for ζ)',fontsize=10)
save(fig,'fig3_mechanisms'); print('ok')

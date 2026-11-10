"""Figures for v1.22 (night2105). Reads the json outputs in this directory. Numerical/exact status as labelled on each panel."""
import json, math, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
H=Path(__file__).resolve().parent; O=H
_D=H.parents[1]/'notes'/'v122'/'provenance'/'data'
def J(name):
    return json.load(open(_D/('night2105_'+name)))
plt.rcParams.update({'font.size':9.5,'axes.titlesize':10.5,'svg.fonttype':'none'})
fig,ax=plt.subplots(2,2,figsize=(12.5,8.6))
# (a) determinant wall
a=ax[0,0]
for p,col in [(2,'C0'),(3,'C1'),(5,'C2')]:
    k=np.arange(1,8); a.semilogy(k,p**k-1.0,'o-',color=col,label=f'chart |det(1−dψ)| = {p}ᵏ − 1')
    a.semilogy(k,np.full(len(k),math.log(p)),'--',color=col,lw=1.2,label=f'needed atom log {p}')
a.set_xlabel('k  (μ = pᵏ)'); a.set_title('(a) Determinant wall = product formula  [Exact]')
a.text(0.03,0.97,'log(pᵏ − 1) = Σ over ℓ | pᵏ−1 of v_ℓ · log ℓ, with ℓ ≠ p;  |1 − pᵏ|ₚ = 1.\nThe graph of μ = pᵏ meets Δ over the other primes ℓ, never over p.\nChart counts: pᵏ − 1 = #G_m(F_pᵏ) (affine), pᵏ + 1 = #P¹(F_pᵏ) (compact).\nHalf-density: 2 sinh(u/2) = h_asym, 2 cosh(u/2) = h_sym (t2073 pair).',transform=a.transAxes,va='top',fontsize=8,bbox=dict(fc='white',ec='0.7'))
a.legend(fontsize=7,loc='lower right',ncol=2)
# (b) Shioda-Tate split under prime-scale sweep
b=ax[0,1]; R=J('n2c_scale_sweep.json')['rows']
for A,m in [(1.1,'o'),(1.5,'s'),(2.0,'^')]:
    rr=[r for r in R if r['A']==A]; s=[r['s'] for r in rr]
    b.step(s,[r['nQ'] for r in rr],where='mid',marker=m,ms=3,label=f'A={A}: n₋(Q)')
    b.step(s,[r['nS']+0.06 for r in rr],where='mid',ls=':',color='k',lw=1)
b.axvline(1.0,color='crimson',lw=1); b.text(1.004,6.3,'ζ\n(s = 1)',color='crimson',fontsize=8)
b.plot([],[],'k:',label='n₋(S), trivial lattice (all A)')
b.set_xlabel('common prime-weight scale s  (control only; s ≠ 1 is not Euler data)'); b.set_ylabel('count')
b.set_title('(b) Shioda–Tate split  n₋(W|E0) = n₋(Q) − n₋(S)\n[identity Exact; counts Numerical, n = 256]')
b.text(0.30,0.97,'n₋(Q) = # eigenvalues of H_A below M_A\n("Hodge index" = exactly one).\nOnly s = 1 keeps n₋(Q) = n₋(S) at A ≥ 1.5;\nthe trivial lattice stays at 1, the bound-state count moves.',transform=b.transAxes,va='top',fontsize=7.5,bbox=dict(fc='white',ec='0.7'))
b.legend(fontsize=7,loc='center left')
# (c) Riesz lifts as fibre classes
c=ax[1,0]; F=J('n2b_fibres.json')['rows']
for n,col in [(256,'C0'),(512,'C1'),(1024,'C2')]:
    rr=[r for r in F if r['n']==n]; A=[r['A'] for r in rr]
    c.semilogy(A,[r['I_HpHp'] for r in rr],'o-',color=col,label=f'I(H₊,H₊)   n={n}')
    c.semilogy(A,[1-r['I_HpHm'] for r in rr],'s--',color=col,label=f'1 − I(H₊,H₋)   n={n}',alpha=.7)
c.set_xlabel('window width A'); c.set_title('(c) Riesz lifts of C± look like fibres f₁, f₂ (Gram → J)\n[Numerical, mesh-dependent]')
c.text(0.42,0.97,'template C×C: f₁² = f₂² = 0, f₁·f₂ = 1\nhere I = −Q, H± = Q⁻¹r±, Gram = −S',transform=c.transAxes,va='top',fontsize=8,bbox=dict(fc='white',ec='0.7'))
c.legend(fontsize=6.5,ncol=2,loc='lower left')
# (d) FF Cayley-Hamilton kernel
d=ax[1,1]; FF=J('n4_cayley_hamilton.json')['rows']
for curve,col in [('genus1 y^2=x^3+x+1/F5','C0'),('genus2 y^2=x^5+2x+1/F3','C3')]:
    rr=[r for r in FF if r['curve']==curve]
    d.plot([r['window'] for r in rr],[r['rank'] for r in rr],'o-',color=col,label=f'{curve}: rank W_ff')
    d.plot([r['window'] for r in rr],[r['kernel_dim'] for r in rr],'s--',color=col,label='  kernel = multiples of L̃(x) (Cayley–Hamilton)')
d.set_xlabel('window length K+1 (Frobenius powers 0..K)'); d.set_ylabel('dimension')
d.set_title('(d) Near-null = numerically trivial (function field)\n[Exact over F_q; Analogy for ζ]')
d.text(0.03,0.62,'Over F_q: rank = 2g; kernel = classes Σ c_k q^(−k/2) Γ_k ≡ 0 in NS_num.\nFor ζ the near-null eigenvector has f̂(γ_k) ≈ 0 (t2064):\nthe analogue of an approximate Cayley–Hamilton relation.\n[Analogy for ζ; no Φ constructed]',transform=d.transAxes,va='top',fontsize=8,bbox=dict(fc='white',ec='0.7'))
d.legend(fontsize=6.5,loc='upper left')
fig.suptitle('RH Atlas v1.22 — two walls, one missing H¹: what a class map Φ must cross.   RH is not proved; Φ is not constructed; no Hodge sign.',fontsize=11)
fig.tight_layout(rect=(0,0,1,0.96))
for ext in ['png','svg']: fig.savefig(O/f'fig1_two_walls_shioda_tate.{ext}',dpi=150)
# Fig 2: Krein / boundary-condition picture
W=J('n3_weyl.json')['rows']
fig2,ax2=plt.subplots(1,2,figsize=(12,4.4))
x=np.linspace(-1.6,1.6,400)

th=[('Θ = 0  →  Q = H_A − M_A (one negative direction)',0),('Θ = J  →  W = Q + P (pole plane)',1),('Θ → ∞  →  W|E0 (Dirichlet: C± = 0)',2)]
for i,(t,_) in enumerate(th): ax2[0].text(0.03,0.85-0.17*i,t,transform=ax2[0].transAxes,fontsize=9)
ax2[0].text(0.03,0.28,'Krein formula (exact, finite dim.):\ndet(Q_Θ − λ) / det(Q − λ) = det(I + Θ M(λ)),   M(λ) = Bᵀ(Q − λ)⁻¹B\nspec W|E0 = zeros of det M(λ);   M′(λ) = Bᵀ(Q − λ)⁻²B ≥ 0 (Herglotz)\nPenalty threshold: Q + c(|C₊|²+|C₋|²) ≥ 0  ⇔  c ≥ c* = 1/|λ_min M(0)|  (when n₋(Q) = 1)',transform=ax2[0].transAxes,fontsize=8.5,bbox=dict(fc='white',ec='0.7'))
ax2[0].axis('off'); ax2[0].set_title('The pole plane is one boundary condition among a 2×2 family  [Exact]')
labs=[f"A={r['A']} {r['case']}" for r in W]; cs=[r['c_star'] for r in W]
ok=[r['case']=='full' for r in W]
ax2[1].bar(range(len(W)),[r['M0_eig'][0] for r in W],color=['C0' if o else 'C7' for o in ok],label='λ_min M(0)')
ax2[1].bar(range(len(W)),[r['M0_eig'][1] for r in W],color=['C1' if o else 'C7' for o in ok],alpha=.7,label='λ_max M(0)')
ax2[1].axhline(-1,color='k',ls=':',lw=.8); ax2[1].axhline(1,color='k',ls=':',lw=.8)
ax2[1].set_xticks(range(len(W))); ax2[1].set_xticklabels(labs,rotation=20,fontsize=7.5)
ax2[1].set_title('M(0) = S: ζ windows sit at ≈ −J (eigs ±1); controls drift  [Numerical, n = 512]')
ax2[1].legend(fontsize=8)
fig2.tight_layout()
for ext in ['png','svg']: fig2.savefig(O/f'fig2_boundary_condition_krein.{ext}',dpi=150)
print('ok')

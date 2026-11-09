#!/usr/bin/env python3
"""atlas2060 figures. Reads only archived JSON in ../data. Run: cd figures && python3 make_figures.py"""
import json, math, pathlib
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
D = pathlib.Path(__file__).resolve().parent.parent / 'data'; O = pathlib.Path(__file__).resolve().parent
FOOT = 'The Riemann Hypothesis is not proved. No all-window positivity is claimed.'
plt.rcParams.update({'font.size': 10, 'font.family': 'DejaVu Sans'})
scan = json.load(open(D / 'inertia2057_scan2057.json'))
coarse = sorted(scan['coarse_scan'], key=lambda r: r['A'])
ref = [r for r in scan['refined'] if r['n'] == 2048]
def lam(n): return math.log(n)
PP = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19]
def T(a): t = math.exp(-a/2); return math.atanh(t) + math.atan(t)
def box(ax, x, y, w, h, txt, fc, ec='#333', fs=9, weight='normal'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012', fc=fc, ec=ec, lw=1.1))
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=fs, weight=weight, wrap=True)
def arrow(ax, p, q, col='#333', ls='-'):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=12, color=col, lw=1.2, linestyle=ls))
# ---------------- Fig 1 (front): proved frontier + signature mechanism ----------------
fig = plt.figure(figsize=(17, 7.4)); gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1], wspace=0.05)
ax = fig.add_subplot(gs[0])
A = [r['A'] for r in coarse]; m = [r['constrained_min'] for r in coarse]
ax.semilogy(A, m, '-', color='#9aa6b2', lw=1.2, label='finite-model E0 minimum, 128 cells [Numerical, upper est.]')
ax.semilogy([r['A'] for r in ref], [r['constrained_min'] for r in ref], 'o', ms=4.5, color='#4b5d6e', label='same, 2048 cells [Numerical, upper est.]')
cert = [(0.1, 0.19656595, '#1b7837', 'A ≤ 0.1 (no prime): ≥ 0.1966  [Exact, analytic]'),
        (0.694, 0.0045, '#5aae61', 'A ≤ 0.694 (n=2): ≥ 0.0045  [Interval certificate]'),
        (1.0, 0.004, '#2166ac', 'A ≤ 1 (n=2): ≥ 0.004  [Computer-assisted]'),
        (1.1, 0.0005, '#762a83', 'A ≤ 1.1 (n=2,3): ≥ 0.0005  [Computer-assisted]')]
for x1, c, col, lab in cert:
    ax.hlines(c, 0.02, x1, colors=col, lw=3.2, label=lab); ax.plot([x1], [c], marker='|', ms=14, color=col, mew=3)
for n in PP:
    if lam(n) <= 3: ax.axvline(lam(n), color='#d6604d', lw=0.6, alpha=0.55)
ax.text(lam(2) - 0.045, 0.02, 'log 2', color='#b2182b', fontsize=8.5, rotation=90); ax.text(lam(3) - 0.045, 0.02, 'log 3', color='#b2182b', fontsize=8.5, rotation=90)
ax.text(1.15, 6e-5, 'red lines: prime-power lags log n', color='#b2182b', fontsize=8)
ax.axvspan(1.1, 3.0, color='#fde0dd', alpha=0.35, lw=0)
ax.text(2.05, 3.0e-4, 'A > 1.1: numerical evidence only\n128- vs 2048-cell values differ ~100×\n(grid bias ≈ size of the gap)', ha='center', fontsize=9, color='#67001f')
ax.text(0.06, 1.5e-6, 'Ghost control at A = 2: deleting only n = 2 gives W/‖F‖² ≈ −0.639 on an explicit E0 test\n(true coefficients: +0.0023) [Numerical]  →  any proof must see the prime coefficients', fontsize=8.6, color='#b2182b')
ax.set_xlim(0, 3.0); ax.set_ylim(8e-7, 4); ax.set_xlabel('window width A (log-scale variable u ∈ [−A/2, A/2])')
ax.set_ylabel('lower bound / estimate of  W(F)/‖F‖²  on E0 = ker C₊ ∩ ker C₋')
ax.set_title('W ≥ c‖F‖² on E0: proved (bars) vs. only computed (dots)', fontsize=12, weight='bold')
ax.legend(loc='upper right', fontsize=8.4, framealpha=0.95); ax.grid(alpha=0.25, which='major')
# right: mechanism
bx = fig.add_subplot(gs[1]); bx.set_xlim(0, 1); bx.set_ylim(0, 1); bx.axis('off')
bx.set_title('Signature mechanism and the missing piece', fontsize=12, weight='bold')
box(bx, 0.02, 0.83, 0.96, 0.12, 'W = P + H_A − M_A‖F‖²,   P = 2Re C₊C̄₋ (pole, vanishes on E0)\nH_A = Gamma + prime jump ("kinetic") energy ≥ 0,   M_A = −K₀ + 2Σ_{log n<A} Λ(n)/√n', '#f7f7f7', fs=9)
box(bx, 0.02, 0.58, 0.46, 0.2, 'Q = W − P (full window):\nexactly ONE negative direction;\nrest of spectrum ≥ 0.004 (A=1),\n≥ 0.0005 (A=1.1)  [Computer-assisted]', '#d1e5f0', fs=8.8)
box(bx, 0.52, 0.58, 0.46, 0.2, 'Two moments C± ⇒ 2×2 matrix S,\nsignature (1,1):\nn₋(Q|E0) = n₋(Q) + n₊(S) − 2 = 0\n[Exact identity + certificate]', '#d1e5f0', fs=8.8)
arrow(bx, (0.48, 0.68), (0.52, 0.68))
box(bx, 0.02, 0.29, 0.96, 0.23, 'Formal boundary model [Exact but tautological]\nU = span{h,v}: J(h,v)=1, J(h,h)=J(v,v)=0 — signature (1,1); FE swaps h ↔ v\ne = h+v, J(e,e) = 2 (residues −1, +1 of the completed ζ at 0, 1)\nπF = F − C₋(F)h − C₊(F)v  ⇒  J(πF, πG) = −W(F,G)\n(J on tests is defined from W itself: no sign theorem)', '#fee8c8', fs=8.6)
box(bx, 0.02, 0.02, 0.96, 0.22, 'MISSING [Open]: arithmetic class map Φ built from geometry first,\ne.g. Φ(F) = ∫F(u)[Γ_u]du (graphs of scaling), with a pairing COMPUTED, not defined:\nprimes = fixed points with weight Λ(n)/√n,  Gamma = archimedean Green term,\nM_A = diagonal self-intersection,  + a Hodge-index sign theorem that applies', '#fddbc7', ec='#b2182b', fs=8.6, weight='bold')
arrow(bx, (0.5, 0.58), (0.5, 0.52), ls='--'); arrow(bx, (0.5, 0.29), (0.5, 0.24), col='#b2182b', ls='--')
fig.text(0.5, 0.012, FOOT + '  Certificates: interval/IEEE-754 error model, not formal proofs.  RH Atlas v1.21 front figure.', ha='center', fontsize=8.5, color='#444')
fig.savefig(O / 'fig1_frontier.png', dpi=170, bbox_inches='tight'); fig.savefig(O / 'fig1_frontier.svg', bbox_inches='tight'); plt.close(fig)
# ---------------- Fig 2: realization / storage block in the prime gap ----------------
def a(n):
    for p in [2, 3, 5, 7]:
        k = round(math.log(n) / math.log(p))
        if p**k == n: return math.log(p) / math.sqrt(n)
    return 0.0
B = 2.0; atoms = [n for n in range(2, 8) if a(n) > 0]
s = np.linspace(0.02, 2.4, 2000)
g = np.array([T(x) - 2*math.exp(-x/2) for x in s])
pB = np.array([sum(a(n) for n in atoms if x <= math.log(n) < B) for x in s])
pBd = np.array([sum(a(n) for n in atoms if n != 2 and x <= math.log(n) < B) for x in s])
dB = np.where(s < B, 2*(math.exp(B/2) - np.exp(s/2)), 0.0)
fig, ax = plt.subplots(1, 2, figsize=(13, 4.8), gridspec_kw=dict(width_ratios=[1.3, 1]))
ax[0].plot(s, g + pB - dB, color='#2166ac', lw=2, label='w_B = g + p_B − d_B (true coefficients)')
ax[0].plot(s, g + pBd - dB, color='#d6604d', lw=1.4, ls='--', label='same with n = 2 deleted (ghost)')
ax[0].axhline(0, color='k', lw=0.7)
for n in atoms: ax[0].axvline(math.log(n), color='#999', lw=0.6, ls=':')
neg = (g + pB - dB) < 0
for i0 in range(len(s)):
    if neg[i0]: ax[0].axvspan(s[i0] - 0.0006, s[i0] + 0.0006, color='#fddbc7', alpha=0.5, lw=0)
ax[0].annotate('w_B < 0 (shaded) just after log 2, log 3, log 5, log 7 [Numerical];\nat s = 1.96 proved analytically: exact-match block\n[[a_B, −d_B], [−d_B, d_B]] not PSD, det ≈ −0.01126 [Obstruction]', xy=(1.96, -0.105), xytext=(0.45, -1.15), fontsize=8.3, arrowprops=dict(arrowstyle='->'))
ax[0].set_xlabel('history lag s'); ax[0].set_ylabel('signed storage weight'); ax[0].set_title('Pole-cancelled history storage at cutoff B = 2', weight='bold', fontsize=10.5)
ax[0].legend(fontsize=8, loc='upper right'); ax[0].set_ylim(-1.6, 3.2); ax[0].grid(alpha=0.25)
ax[1].axis('off'); ax[1].set_xlim(0, 1); ax[1].set_ylim(0, 1)
ax[1].set_title('Response / passivity reading of the complete W', weight='bold', fontsize=10.5)
txt = [('Exact identity', 'B_W(F_z, F_w) = (q(z)+q̄(w))/(z+w̄),  q = ξ′/ξ(½+z),  F_z = e^{−zu}·1_{u≥0},\nRe z, Re w > ½  — pole, Gamma, K₀ and every prime term matched', '#d9f0d3'),
       ('Cited theorem', 'RH ⇔ q positive-real on Re z > 0 (Lagarias 1999; Hinkkanen)', '#f7f7f7'),
       ('Exact (signed)', '2Re(ū y_B) = d/dt(S_∂ + S_jump) + D_jump − M_B|u|²\nboundary storage S_∂ = 2Re(x₊x̄₋) is indefinite', '#d1e5f0'),
       ('Obstructions', 'finite prime cutoff leaves a pole at z = ½; independent prime-line storage\ndiverges; fixed-diagonal PSD coupling leaves ≥ (√P_B − √G)² → ∞', '#fddbc7'),
       ('Positive substrate', 'Bost–Connes KMS at β = ½: ‖√Λ(n) μ_n* Ω‖² = Λ(n)/√n exactly —\nbut its kernel −ζ′/ζ(½+z+w̄) is not K_q (no Gamma, pole, mass)', '#e7d4e8'),
       ('Open', 'independently positive COUPLED storage reproducing K_q exactly', '#fee8c8')]
y = 0.93
for tag, t, col in txt:
    box(ax[1], 0.0, y - 0.13, 1.0, 0.12, f'[{tag}]  ' + t, col, fs=7.0); y -= 0.155
fig.text(0.5, -0.01, FOOT + '  Ghost = coefficient-sensitivity control, not admissible Euler data.', ha='center', fontsize=8.3, color='#444')
fig.savefig(O / 'fig2_response_storage.png', dpi=160, bbox_inches='tight'); fig.savefig(O / 'fig2_response_storage.svg', bbox_inches='tight'); plt.close(fig)
# ---------------- Fig 3: finite inertia scan ----------------
fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.4))
ax[0].plot(A, [r['S_eigenvalues'][0] for r in coarse], color='#b2182b', label='S_Q eigenvalue (−)')
ax[0].plot(A, [r['S_eigenvalues'][1] for r in coarse], color='#2166ac', label='S_Q eigenvalue (+)')
ax[0].plot(A, [r['Q_inertia'][0] for r in coarse], 'k:', label='n₋(Q) (finite model)')
ax[0].plot(A, [r['constrained_inertia'][0] for r in coarse], color='#1b7837', ls='--', label='n₋(Q|E0)')
ax[0].set_xlabel('A'); ax[0].set_title('Finite inertia, 128-cell exact-form models [Numerical]', weight='bold', fontsize=10.5)
ax[0].legend(fontsize=8); ax[0].grid(alpha=0.25)
ax[1].plot(A, [r['negative_mode_moment_overlap_squared'][0] for r in coarse], color='#762a83')
ax[1].set_xlabel('A'); ax[1].set_ylabel('squared overlap'); ax[1].set_ylim(0.95, 1.0)
ax[1].set_title('Negative Q-mode vs span{e^{u/2}, e^{−u/2}} [Numerical]', weight='bold', fontsize=10.5); ax[1].grid(alpha=0.25)
ax[1].text(0.6, 0.955, 'close to, but not inside, the moment span:\nthe constraints remove the index, not an eigenvector', fontsize=8.3)
fig.text(0.5, -0.02, FOOT + '  Index n₋(Q)=1 is certified only at A = 1 and A = 1.1.', ha='center', fontsize=8.3, color='#444')
fig.savefig(O / 'fig3_inertia_scan.png', dpi=160, bbox_inches='tight'); fig.savefig(O / 'fig3_inertia_scan.svg', bbox_inches='tight'); plt.close(fig)
print('ok')

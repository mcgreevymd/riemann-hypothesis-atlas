"""t2083 first-variation (dipole) probe on X = P^1 x P^1, product FS baseline (scratch).
Conventions as t2078: dd^c=(i/2pi) d dbar; g_u = -log|w-e^u z|^2 + log(1+|z|^2) + log(1+|w|^2);
T(u,v) = int (g_u*g_v)^omega = int_{Gamma_v} g_u omega + int_X g_v omega^2.
V_u := d/du [Gamma_u]  (dipole, exact (1,1)-current of order 1), Green function h_u = d/du g_u.
<V_u,Gamma_v,omega> = d_u T ;  <V_u,V_v,omega> = d_u d_v T  (omega^2 term drops: [V_u]=0 in H^{1,1})."""
import json, numpy as np, sympy as sp
from scipy import integrate
out = {}
u, v = sp.symbols('u v', real=True)
a, t = sp.symbols('a t', positive=True)
q = sp.exp(-a)
kinf = sp.exp(-a/2)/(1-sp.exp(-2*a))
def on_upgtv(expr):           # substitute u = v + a  (u>v)
    return sp.simplify(sp.expand(sp.simplify(expr.subs(u, v+a))))
T = {+1: 6 - 4*sp.log(sp.exp(u)-sp.exp(v)), -1: 6 - 4*sp.log(sp.exp(u)+sp.exp(v))}   # raw, u>v
Tb = {e: T[e] + 2*u + 2*v for e in T}                                                  # balanced
Ttr = 3 - 4*sp.log(2*sp.sinh((u-v)/2)) + (u-v)*sp.coth(u-v) + u*sp.coth(u) + v*sp.coth(v)   # comoving, u>v
res = {}
def rec(name, expr):
    e = on_upgtv(expr); res[name] = e
    out.setdefault('closed_forms_u_gt_v', {})[name] = str(e)
    return e
for e, tag in [(1, '+'), (-1, '-')]:
    rec(f'T{tag}_raw', T[e]); rec(f'T{tag}_bal', Tb[e])
    rec(f'A{tag}_raw = d_u T', sp.diff(T[e], u)); rec(f'A{tag}_bal = d_u T', sp.diff(Tb[e], u))
    rec(f'A{tag}_raw (u<v)', sp.diff(T[e], u).subs(u, v-a)+0*u)  # see note: evaluated at u=v-a
    rec(f'B{tag} = d_u d_v T', sp.diff(T[e], u, v))
    # half-densitized Ghat_u = e^{-u/2}Gamma_u ; bilinear => That = e^{-(u+v)/2} T ; dual-weighted e^{-(u-v)/2} T
    Th = sp.exp(-(u+v)/2)*Tb[e]; Td = sp.exp(-(u-v)/2)*Tb[e]
    rec(f'C{tag}_A_hat (both e^-/2, bal)', sp.diff(Th, u)); rec(f'C{tag}_B_hat (both e^-/2, bal)', sp.diff(Th, u, v))
    rec(f'C{tag}_A_dual (e^-(u-v)/2, bal)', sp.diff(Td, u)); rec(f'C{tag}_B_dual (e^-(u-v)/2, bal)', sp.diff(Td, u, v))
rec('F_A_tr = d_u T_tr', sp.diff(Ttr, u)); rec('F_B_tr = d_u d_v T_tr', sp.diff(Ttr, u, v))
# fix the u<v raw entries properly
for e, tag in [(1, '+'), (-1, '-')]:
    expr = sp.diff(-4*sp.log(sp.Abs(sp.exp(u)-e*sp.exp(v))), u).subs(u, v-a)
    e2 = sp.simplify(sp.expand(sp.simplify(expr.rewrite(sp.exp)))); res[f'A{tag}_raw (u<v)'] = e2
    out['closed_forms_u_gt_v'][f'A{tag}_raw (u<v), a=v-u'] = str(e2); out['closed_forms_u_gt_v'].pop(f'A{tag}_raw (u<v)')
# D: sign averages
D = {}
D['avg A_raw'] = sp.simplify((res['A+_raw = d_u T']+res['A-_raw = d_u T'])/2)
D['avg A_bal'] = sp.simplify((res['A+_bal = d_u T']+res['A-_bal = d_u T'])/2)
D['avg B'] = sp.simplify((res['B+ = d_u d_v T']+res['B- = d_u d_v T'])/2)
D['avg A_dual'] = sp.simplify((res['C+_A_dual (e^-(u-v)/2, bal)']+res['C-_A_dual (e^-(u-v)/2, bal)'])/2)
out['D_sign_averages'] = {k: str(val) for k, val in D.items()}
chk = lambda e: sp.simplify(sp.expand((e).rewrite(sp.exp)))
ids = {}
ids['cooked t2078: k - (-1/4)e^{-a/2} avg A_raw'] = chk(kinf + sp.Rational(1,4)*sp.exp(-a/2)*D['avg A_raw'])
ids['-1/4 A+_raw - 1/(1-q)  [AB index on O at (0,0)]'] = chk(-res['A+_raw = d_u T']/4 - 1/(1-q))
ids['-1/4 A+_raw(u<v) - (-q/(1-1/q)^{-1}...) : -1/4A(u<v) + q/(1-q)'] = chk(-res['A+_raw (u<v)']/4 + q/(1-q))
ids['-1/4 avg A_raw - 1/(1-q^2)  [doubling]'] = chk(-D['avg A_raw']/4 - 1/(1-q**2))
ids['-1/4 A+_bal - (1/2)coth(a/2)'] = chk(-res['A+_bal = d_u T']/4 - sp.coth(a/2)/2)
ids['B+ + 1/sinh^2(a/2)'] = chk(res['B+ = d_u d_v T'] + 1/sp.sinh(a/2)**2)
ids['B- - 1/cosh^2(a/2)'] = chk(res['B- = d_u d_v T'] - 1/sp.cosh(a/2)**2)
ids['-B+/4 - q/(1-q)^2  [=1/|det(1-diag(e^a,e^-a))|]'] = chk(-res['B+ = d_u d_v T']/4 - q/(1-q)**2)
ids['avg B + 2/sinh^2 a'] = chk(D['avg B'] + 2/sp.sinh(a)**2)
ids['sqrt identity: k - (sqrt(-B+/4)+sqrt(B-/4))/2'] = chk(kinf - (sp.sqrt(-res['B+ = d_u d_v T']/4)+sp.sqrt(res['B- = d_u d_v T']/4))/2)
ids['factorization: k - (-A+_raw/4)*(1/(2cosh(a/2)))'] = chk(kinf - (-res['A+_raw = d_u T']/4)/(2*sp.cosh(a/2)))
# half-density remainder: <d_u Ghat_u, Ghat_v^dual> (raw) = e^{-a/2}(A_raw - T_raw/2)
Td_raw = {e: sp.exp(-(u-v)/2)*T[e] for e in T}
avgCd_raw = on_upgtv((sp.diff(Td_raw[1], u)+sp.diff(Td_raw[-1], u))/2)
avgT_raw = on_upgtv((T[1]+T[-1])/2)
ids['k - [(-1/4)avg<dGhat,Ghat^v>_raw - (1/8)e^{-a/2} avgT_raw]'] = chk(kinf - (-avgCd_raw/4 - sp.exp(-a/2)*avgT_raw/8))
out['avgT_raw (u>v)'] = str(avgT_raw)
out['identities_residuals (0 = exact)'] = {k: str(val) for k, val in ids.items()}
print(json.dumps(out['identities_residuals (0 = exact)'], indent=1))
# E: asymptotics (a-only quantities)
asym = {}
cands = {'k_inf': kinf, '-1/8 A+_raw': -res['A+_raw = d_u T']/8, '-1/8 A+_bal': -res['A+_bal = d_u T']/8,
         '-1/8 avg A_raw': -D['avg A_raw']/8, 'B+': res['B+ = d_u d_v T'], 'B-': res['B- = d_u d_v T'], 'avg B': D['avg B'],
         'C+_A_dual': res['C+_A_dual (e^-(u-v)/2, bal)'], 'C+_B_dual': res['C+_B_dual (e^-(u-v)/2, bal)'],
         'avg C_A_dual': D['avg A_dual'], 'F_B_tr': res['F_B_tr = d_u d_v T_tr']}
for k, e in cands.items():
    small = sp.series(e, a, 0, 2).removeO()
    big = sp.limit(e*sp.exp(a/2), a, sp.oo)
    asym[k] = {'a->0': str(sp.simplify(small)), 'lim e^{a/2}*f (a->oo)': str(big),
               'lim f (a->oo)': str(sp.limit(e, a, sp.oo))}
    print(k, asym[k])
out['asymptotics'] = asym
out['u_dependent (non-invariant) pieces'] = {
  'C+_A_hat (both e^{-u/2},e^{-v/2})': str(res['C+_A_hat (both e^-/2, bal)']),
  'F_A_tr': str(res['F_A_tr = d_u T_tr'])}
# Fourier symbols (t != 0): FT f(x) = int e^{-ixt} f dx
out['fourier_symbols'] = {'T_bal-6 = -4log(2sinh(|x|/2))': '4 pi coth(pi t)/t',
  'A_bal = -2coth(x/2) (odd, PV)': '4 pi i coth(pi t)', 'B = -1/sinh^2(x/2) (Hadamard FP)': '4 pi t coth(pi t)  (>0)',
  'k_inf(|x|)': '~ -log|t| growth (FP 1/(2|x|) singularity); digamma-type'}
# ---------- numerical checks ----------
def g(uu, z, w): return -np.log(abs(w-np.exp(uu)*z)**2) + np.log(1+abs(z)**2) + np.log(1+abs(w)**2)
def S(uu, vv):   # int_{Gamma_v} g_u omega  (u-dependent part of T), deterministic 2D quadrature
    tt = np.exp(vv); tot = 0
    for sc in (1.0, tt):
        f = lambda th, xx: g(uu, np.sqrt(xx/(1-xx))*np.exp(1j*th)/sc, tt*np.sqrt(xx/(1-xx))*np.exp(1j*th)/sc)/(2*np.pi)
        tot += integrate.dblquad(f, 0, 1, 0, 2*np.pi, epsabs=1e-11, epsrel=1e-11)[0]
    return tot
def dip(uu, vv):   # <V_v, h_u omega> via Cartan: int_{Gamma_v} xi(h_u) omega, xi = 2Re(w d_w), h_u = 2Re(e^u z/(w-e^u z))
    tt = np.exp(vv); tot = 0
    for sc in (1.0, tt):
        def f(th, xx):
            z = np.sqrt(xx/(1-xx))*np.exp(1j*th)/sc; w = tt*z; L = np.exp(uu)
            return 2*np.real(-w*L*z/(w-L*z)**2)/(2*np.pi)
        tot += integrate.dblquad(f, 0, 1, 0, 2*np.pi, epsabs=1e-11)[0]
    return tot
rows = []; h = 1e-3
for uu, vv in [(0.7, 0.0), (1.3, 0.4), (-0.5, 1.5), (2.0, -1.0)]:
    Anum = (S(uu+h, vv)-S(uu-h, vv))/(2*h)
    Bnum = (S(uu+h, vv+h)-S(uu+h, vv-h)-S(uu-h, vv+h)+S(uu-h, vv-h))/(4*h*h)
    Aex = -4*np.exp(uu)/(np.exp(uu)-np.exp(vv)); Bex = -1/np.sinh((uu-vv)/2)**2
    rows.append(dict(u=uu, v=vv, A_fd=Anum, A_exact=Aex, B_fd=Bnum, B_cartan=dip(uu, vv), B_exact=Bex)); print(rows[-1])
out['numeric_checks_raw'] = rows
# Fourier/positivity check of B as Gram kernel: Q = int int phi'(u)phi'(v) T_bal(u-v) vs (1/2pi) int |phihat|^2 4pi t coth(pi t)
s0 = 0.8
xs = np.linspace(-12, 12, 2401); dx = xs[1]-xs[0]
phi = np.exp(-xs**2/(2*s0**2)); dphi = -xs/s0**2*phi
X = xs[:, None]-xs[None, :]; Tb_ = 6-4*np.log(2*np.sinh(np.abs(X)/2)+1e-300); np.fill_diagonal(Tb_, 0)
# diagonal log singularity: correct by local integral of -4log|x| over cell
cell = 6-4*(np.log(dx/2)-1)-0  # avg of 6-4log|x| on [-dx/2,dx/2] ~ 6-4(log(dx/2)-1)
np.fill_diagonal(Tb_, cell)
Qx = dphi @ Tb_ @ dphi * dx*dx
ts = np.linspace(1e-6, 40, 400001); phat2 = 2*np.pi*s0**2*np.exp(-s0**2*ts**2)
Qt = 2*np.trapezoid(phat2*4*np.pi*ts/np.tanh(np.pi*ts), ts)/(2*np.pi)
out['positivity_check_B'] = {'Q_direct': Qx, 'Q_fourier': Qt}; print('Q', Qx, Qt)
json.dump(out, open('vary2083.json', 'w'), indent=1, default=str)

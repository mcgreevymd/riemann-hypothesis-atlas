"""t2078 Route 2 current test on X = P^1 x P^1 (scratch).
Conventions: dd^c = (i/2pi) d dbar, so dd^c log|z|^2 = delta_0 and
omega_FS = dd^c log(1+|z|^2) has mass 1.  On C in r=|z|^2 the FS measure is dr/(1+r)^2.
g_u(z,w) = -log|w - e^u z|^2 + log(1+|z|^2) + log(1+|w|^2)    (Gillet-Soule Green current of Gamma_u)
Pairing used:  T(u,v) = int_X (g_u * g_v) ^ omega = int_{Gamma_v} g_u omega + int_X g_v omega^2.
"""
import json, numpy as np, sympy as sp
from scipy import integrate
out = {}
# ---------- exact radial integrals (sympy) ----------
x, c, s = sp.symbols('x c s', positive=True)
I_logx = sp.integrate(sp.log(x)/(1+x)**2, (x, 0, sp.oo))
I_log1px = sp.integrate(sp.log(1+x)/(1+x)**2, (x, 0, sp.oo))
f_c = sp.simplify(sp.integrate(sp.log(1+c*x)/(1+x)**2, (x, 0, sp.oo)))
out['exact'] = {'int log x dx/(1+x)^2': str(I_logx), 'int log(1+x) dx/(1+x)^2': str(I_log1px),
                'f(c)=int log(1+cx) dx/(1+x)^2': str(f_c)}
u, v = sp.symbols('u v', real=True)
t = sp.exp(v)
f = lambda cc: cc*sp.log(cc)/(cc-1)
# restriction of g_u to Gamma_v (w = t z):  -log|e^u-e^v|^2 + G_v(z),  G_v = -log r + log(1+r) + log(1+t^2 r)
# mu_1: dr/(1+r)^2 ; mu_t: t^2 dr/(1+t^2 r)^2  (pullback of FS on w)
G_mu1 = 0 + 1 + f(t**2)
G_mut = 2*v + f(1/t**2) + 1
term1 = -2*2*sp.log(sp.Abs(sp.exp(u)-sp.exp(v))) + G_mu1 + G_mut
term2 = 2*(-f(t**2) + 1 + 1)       # omega^2 = 2 pr1*w ^ pr2*w ; int log|w-a|^2 dmu(w) = log(1+|a|^2)
T = sp.simplify(term1 + term2)
out['T(u,v) exact'] = str(T)
print('T =', T)
# ---------- numerical check of T(u,v) from unsimplified formulas ----------
def g(uu, z, w):
    return -np.log(abs(w-np.exp(uu)*z)**2) + np.log(1+abs(z)**2) + np.log(1+abs(w)**2)
def T_num(uu, vv, eps=1.0, N=4_000_000, seed=1):
    tt = np.exp(vv)
    # term1: int over z in C of g_u(z, eps e^v z) against mu_1 + mu_t  (2D, polar, rho in (0,inf) via r = x/(1-x))
    def integrand(xx, th, which):
        r = xx/(1-xx); jac = 1/(1-xx)**2       # r=|z|^2 for mu_1
        if which == 't': r = r/tt**2; dens = 1.0  # mu_t is pushforward under z -> z/t of mu_1
        z = np.sqrt(r)*np.exp(1j*th)
        return g(uu, z, eps*tt*z)*(1/(1+xx/(1-xx))**2)*jac/(2*np.pi)
    t1 = sum(integrate.dblquad(lambda th, xx: integrand(xx, th, w_), 0, 1, 0, 2*np.pi, epsabs=1e-9)[0] for w_ in ('1', 't'))
    # term2: 2 * E[g_v(z,w)] with z,w independent FS-distributed (Monte Carlo)
    rng = np.random.default_rng(seed)
    def samp(n):
        xx = rng.random(n); return np.sqrt(xx/(1-xx))*np.exp(2j*np.pi*rng.random(n))
    zz, ww = samp(N), samp(N)
    gv = -np.log(abs(ww-eps*tt*zz)**2) + np.log(1+abs(zz)**2) + np.log(1+abs(ww)**2)
    t2 = 2*gv.mean(); se = 2*gv.std()/np.sqrt(N)
    return t1, t2, se
rows = []
for (uu, vv) in [(0.7, 0.0), (1.3, 0.4), (-0.5, 1.5), (2.0, -1.0)]:
    t1, t2, se = T_num(uu, vv)
    ex = float(T.subs({u: uu, v: vv}))
    rows.append({'u': uu, 'v': vv, 'num': t1+t2, 'mc_se': se, 'exact': ex})
    print(rows[-1])
out['check_T'] = rows
# sign-twisted graph Gamma_v^- = {w = -e^v z}: prediction -2log|e^u+e^v|^2 + 6
rows = []
for (uu, vv) in [(0.7, 0.0), (1.3, 0.4)]:
    t1, t2, se = T_num(uu, vv, eps=-1.0)
    rows.append({'u': uu, 'v': vv, 'num': t1+t2, 'mc_se': se, 'pred': -4*np.log(np.exp(uu)+np.exp(vv))+6})
    print('twisted', rows[-1])
out['check_T_twisted'] = rows
# ---------- k_inf comparisons ----------
a = sp.symbols('a', positive=True)
kinf = sp.exp(-a/2)/(1-sp.exp(-2*a))
Lplus = -4*sp.log(2*sp.sinh(a/2))      # a-part of T with balanced section (T' = T + 2u + 2v)
Lminus = -4*sp.log(2*sp.cosh(a/2))
lef = sp.exp(-a/2)/2*(1/(1-sp.exp(-a)) + 1/(1+sp.exp(-a)))
# identity: k_inf = -(1/4) e^{-a/2} * avg_eps d/du T_eps(u,v)  (raw sections, u>v, a=u-v)
Tp = -4*sp.log(sp.exp(u)-sp.exp(v)) + 6
Tm = -4*sp.log(sp.exp(u)+sp.exp(v)) + 6
cand = -sp.Rational(1,4)*sp.exp(-(u-v)/2)*(sp.diff(Tp, u)+sp.diff(Tm, u))/2
out['identities'] = {
  'lefschetz_even_avg - kinf': str(sp.simplify(lef - kinf)),
  'derivative identity residual (u>v)': str(sp.simplify((cand - kinf.subs(a, u-v)).rewrite(sp.exp))),
  'kinf - L+(a) is not zero (sample a=1)': float((kinf - Lplus).subs(a, 1)),
  'Lplus series a->0': str(sp.series(Lplus, a, 0, 2)),
  'kinf series a->0': str(sp.series(kinf, a, 0, 2)),
  'Lplus large a': '-2a + O(e^{-a})', 'kinf large a': 'e^{-a/2} + O(e^{-5a/2})',
  # Atiyah-Bott local index of z->q z on germs of K^{1/2} at 0: sum q^{n+1/2}
  'AB local K^1/2, q=e^-a': str(sp.simplify(sp.summation(sp.exp(-a*(sp.Symbol('n',integer=True,nonnegative=True)+sp.Rational(1,2))), (sp.Symbol('n',integer=True,nonnegative=True),0,sp.oo)))),
}
# ---------- blow-up: exceptional E0 = P^1 with slope m=w/z; Gamma_u~ meets E0 at m=e^u ----------
G_E = sp.simplify(-sp.log((sp.exp(u)-sp.exp(v))**2/((1+sp.exp(2*u))*(1+sp.exp(2*v)))))
out['FS Green on E0 at slopes e^u,e^v'] = str(G_E)
out['  = -2log|sinh(a/2)| + log cosh u + log cosh v (check, u=1.1,v=0.3)'] = float(G_E.subs({u:1.1,v:0.3}) - (-2*sp.log(sp.sinh(0.4)) + sp.log(sp.cosh(1.1)) + sp.log(sp.cosh(0.3))))
# ---------- toric (sup-norm) metric on O(1,1): omega = Haar on unit circles ----------
# restriction to Gamma_v: -log|e^u-e^v|^2 - log r + log max(1,r) + log max(1,t^2 r); measure = circle |z|=1 + circle |z|=1/t
Ttor1 = lambda uu, vv: -4*np.log(abs(np.exp(uu)-np.exp(vv))) + (0+0+max(0,2*vv)) + (2*vv + max(0,-2*vv) + 0)
out['toric metric term1 example (u=1,v=0.5)'] = Ttor1(1.0, 0.5)
json.dump(out, open('pair2078.json', 'w'), indent=1, default=str)
print(json.dumps(out['identities'], indent=1))

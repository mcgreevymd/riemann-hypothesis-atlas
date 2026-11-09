#!/usr/bin/env python3
"""atlas2060 independent audit checks (re-derivations by a different route than the source scripts).
All numerics are mpmath double/multi-precision, NOT interval-certified unless stated. Output: audit2060.json"""
import json, time, itertools
import mpmath as mp, numpy as np
mp.mp.dps = 30
t0 = time.time(); R = {}; ok = {}
def chk(name, cond, val=None):
    ok[name] = bool(cond); R[name] = val if val is not None else bool(cond)
    print(f'{time.time()-t0:7.1f}s {name}: {ok[name]}', flush=True)
g = mp.euler; pi = mp.pi; L2 = mp.log(2)
K0 = mp.digamma(mp.mpf(1)/4) - mp.log(pi)
chk('K0_closed_form', abs(K0 - (-g - pi/2 - 3*L2 - mp.log(pi))) < 1e-25, str(K0))
# FP_H int_0^inf k = pi/2 + 2 log 2 with k(a)=e^{a/2}/sinh a (counterterm1995 'K'); check -psi(1/4)-gamma-log2
chk('FP_identity', abs((-mp.digamma(0.25) - g - L2) - (pi/2 + 2*L2)) < 1e-25, str(pi/2 + 2*L2))
chk('minusK0_split', abs(-K0 - (g + mp.log(8*pi) + pi/2)) < 1e-25)
k = lambda a: mp.e**(-a/2)/(1 - mp.e**(-2*a))
T = lambda a: mp.atanh(mp.e**(-a/2)) + mp.atan(mp.e**(-a/2))
chk('T_closed_form', abs(mp.quad(k, [0.7, 3, mp.inf]) - T(0.7)) < 1e-20)
cstar = mp.log(5*mp.sqrt(2)/pi) - g - mp.mpf(3)/80
chk('small_window_cstar', cstar > mp.mpf(7)/240 and abs(cstar - mp.mpf('0.19656595196')) < 1e-9, str(cstar))
# two-scale bound actually exceeds -K0 at A=1/10 (the theorem's content)
A = mp.mpf(1)/10
chk('small_window_two_scale', T(A) + T(A/2) + K0 > cstar - 1e-12, str(T(A) + T(A/2) + K0))
a = lambda n, p: mp.log(p)/mp.sqrt(n)
a2, a3 = a(2, 2), a(3, 3)
M1 = -K0 + 2*a2; M11 = -K0 + 2*a2 + 2*a3
R['a2'], R['a3'], R['M_1'], R['M_1.1'] = str(a2), str(a3), str(M1), str(M11)
chk('M1_value', abs(M1 - mp.mpf('6.3524415626')) < 1e-9)
sstar = (a3 + mp.sqrt(a3**2 + 4*a2**2))/2
chk('two_prime_path_norm', abs(sstar - mp.mpf('0.9009276163')) < 1e-9, str(sstar))
# brute check of the 4-vertex path norm
Mp = np.array([[0, float(a2), 0, 0], [float(a2), 0, float(a3), 0], [0, float(a3), 0, float(a2)], [0, 0, float(a2), 0]])
chk('two_prime_path_norm_matrix', abs(max(abs(np.linalg.eigvalsh(Mp))) - float(sstar)) < 1e-12)
# --- complete-W exponential probe identity B_W(F_z,F_w)=K_q(z,w), Gamma part by direct quadrature in a ---
def xi(s): return mp.mpf(1)/2*s*(s-1)*pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def q(z): s = mp.mpf(1)/2 + z; return mp.diff(xi, s)/xi(s)
def BW(z, w):
    d = z + mp.conj(w)
    P = 1/((z+0.5)*(mp.conj(w)-0.5)) + 1/((z-0.5)*(mp.conj(w)+0.5))  # C-(F)conj C+(G)+C+(F)conj C-(G)
    gam = (K0 + mp.quad(lambda t: k(t)*(2 - mp.e**(-z*t) - mp.e**(-mp.conj(w)*t)), [0, 1, 10, mp.inf]))/d
    s1, s2 = mp.mpf(1)/2 + z, mp.mpf(1)/2 + mp.conj(w)
    prime = (mp.zeta(s1, derivative=1)/mp.zeta(s1) + mp.zeta(s2, derivative=1)/mp.zeta(s2))/d  # = -sum a_n(e^{-z b}+e^{-wbar b})/d
    return P + gam + prime
rows = []
for z, w in [(1, 2), (mp.mpc(0.8, 3), mp.mpc(1.5, -2)), (mp.mpc(0.6, 10), mp.mpc(0.6, 10))]:
    z, w = mp.mpmathify(z), mp.mpmathify(w)
    lhs = BW(z, w); rhs = (q(z) + mp.conj(q(w)))/(z + mp.conj(w))
    rows.append([str(z), str(w), mp.nstr(lhs, 15), mp.nstr(rhs, 15), float(abs(lhs - rhs))])
R['probe_identity_rows'] = rows
chk('probe_identity', max(r[4] for r in rows) < 1e-12)
chk('Kq_1_2_matches_kms2040', abs(mp.re(BW(mp.mpf(1), mp.mpf(2))) - mp.mpf('0.04599006651870111731')) < 1e-15)
chk('KMS_prime_kernel_1_2', abs(-mp.zeta(3.5, derivative=1)/mp.zeta(3.5) - mp.mpf('0.1003956416766439')) < 1e-14)
# q'(0)=xi''/xi(1/2) and positivity of Phi
qp0 = mp.diff(xi, 0.5, 2)/xi(0.5)
chk('qprime0', abs(qp0 - mp.mpf('0.0462099862308379')) < 1e-12, str(qp0))
Phi = lambda u: 4*sum((2*pi**2*n**4*mp.e**(4.5*u) - 3*pi*n**2*mp.e**(2.5*u))*mp.e**(-pi*n**2*mp.e**(2*u)) for n in range(1, 9))  # n<=8: tail < e^{-200} for u>=0
chk('Phi_moment_ratio', abs(mp.quad(lambda u: u**2*Phi(u), [0, 1, 2, 4])/mp.quad(Phi, [0, 1, 2, 4]) - qp0) < 1e-12)
chk('Phi_positive_samples', all(Phi(u) > 0 for u in [0, 0.1, 0.5, 1, 2]))
# --- n=2 ghost via Fourier-side Gamma energy (different route from physical-space quadrature) ---
mp.mp.dps = 20
import sympy as sp
u = sp.symbols('u'); G = (1 - u**2)**4; Fs = sp.expand(sp.diff(G, u, 2) - G/4)
Fl = sp.lambdify(u, Fs, 'mpmath')
Cp = sp.integrate(Fs*sp.exp(u/2), (u, -1, 1)); Cm = sp.integrate(Fs*sp.exp(-u/2), (u, -1, 1))
chk('ghost_moments_zero', sp.simplify(Cp) == 0 and sp.simplify(Cm) == 0)
N = float(sp.integrate(Fs**2, (u, -1, 1)))
def corr(b):
    b = sp.nsimplify(b) if isinstance(b, int) else b
    return float(sp.Integral(Fs*Fs.subs(u, u - b), (u, -1 + b, 1)).evalf(25)) if b < 2 else 0.0
# Fhat(t) = int F e^{-itu}: F even -> 2 int_0^1 F cos(tu)
Fc = sp.lambdify(u, Fs, 'mpmath')
def Fhat(t): return 2*mp.quad(lambda x: Fc(x)*mp.cos(t*x), [0, 1])
# closed form via sympy for speed
t = sp.symbols('t', positive=True)
Fh = sp.lambdify(t, sp.simplify(2*sp.integrate(Fs*sp.cos(t*u), (u, 0, 1))), 'mpmath')
Kg = lambda tt: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tt/2)) - mp.log(pi)
# the sympy closed form of Fhat cancels catastrophically near t=0, so use it only for t >= 8 and direct quadrature below
def Fhh(tt): return Fhat(tt) if tt < 8 else Fh(mp.mpf(tt))
gam = mp.quad(lambda tt: Kg(tt)*Fhh(tt)**2, [0, 2, 4, 8, 20, 80, 400])/pi  # (1/2pi)*2*int_0^inf; tail beyond 400 is O(400^-5)
primes = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]
prime = sum(-2*float(a(n, p))*float(sp.Integral(Fs*Fs.subs(u, u - sp.log(n)), (u, -1 + sp.log(n), 1)).evalf(20)) for n, p in primes)
W = float(gam) + prime
Wd = W + 2*float(a2)*float(sp.Integral(Fs*Fs.subs(u, u - sp.log(2)), (u, -1 + sp.log(2), 1)).evalf(20))
R['ghost_fourier_route'] = dict(norm2=N, W_over_N=W/N, W_drop2_over_N=Wd/N)
chk('ghost_W_matches', abs(W/N - 0.0023337532023) < 2e-6)
chk('ghost_drop2_matches', abs(Wd/N - (-0.6392279387151)) < 2e-6)
mp.mp.dps = 30
# --- blocks2038 negative prime-gap point ---
s0 = mp.mpf(49)/25
gs0 = T(s0) - 2*mp.e**(-s0/2); ds0 = 2*(mp.e - mp.e**(s0/2))
chk('block_gap_no_prime', 7 < mp.e**s0 < 8)
chk('block_negative', gs0 - ds0 < -mp.mpf(3)/100, dict(g=str(gs0), d=str(ds0), w=str(gs0 - ds0), det=str(ds0*(gs0 - ds0))))
chk('block_det_value', abs(ds0*(gs0 - ds0) - mp.mpf('-0.01126453789309')) < 1e-12)
# --- inertia identity n-(Q|E0)=n-(Q)+n+(S)-2 on random nonsingular symmetric matrices ---
rng = np.random.default_rng(2060); bad = 0
for trial in range(300):
    n = rng.integers(4, 12); Q = rng.standard_normal((n, n)); Q = Q + Q.T
    B = rng.standard_normal((n, 2)); S = B.T @ np.linalg.solve(Q, B)
    Z = np.linalg.svd(B.T)[2][2:].T
    lhs = int((np.linalg.eigvalsh(Z.T @ Q @ Z) < 0).sum())
    rhs = int((np.linalg.eigvalsh(Q) < 0).sum()) + int((np.linalg.eigvalsh(S) > 0).sum()) - 2
    bad += lhs != rhs
chk('two_constraint_inertia_identity_random', bad == 0, f'{bad} mismatches /300')
# --- pencil identity min_{alpha,beta} Delta_e(F+alpha h+beta v) = 2W(F)  (parabolic1998) ---
Bf, Cp_, Cm_, al, be = sp.symbols('B Cp Cm alpha beta')
J = lambda x, y: None
# x = F + al h + be v; J(x,x) = -B + 2 al Cp + 2 be Cm + 2 al be ; J(e,x) = Cp + Cm + al + be ; J(e,e) = 2
Jxx = -Bf + 2*al*Cp_ + 2*be*Cm_ + 2*al*be; Jex = Cp_ + Cm_ + al + be
Delta = sp.expand(Jex**2 - 2*Jxx)
sol = sp.solve([sp.diff(Delta, al), sp.diff(Delta, be)], [al, be], dict=True)
# Delta depends only on al+be up to the al*be term: check min over the line al=be+c numerically symbolic
Dsub = sp.simplify(Delta.subs(be, sp.Symbol('s') - al))
crit = sp.solve(sp.diff(Dsub, al), al)
mn = sp.simplify(Dsub.subs(al, crit[0]))
chk('pencil_min_flat_in_sum', sp.simplify(sp.diff(mn, sp.Symbol('s'))) == 0, str(mn))
chk('pencil_min_equals_2W', sp.simplify(mn - 2*(Bf + 2*Cp_*Cm_)) == 0)
# --- Serre: a1(f_10)=38016/691 ---
Bn = sp.bernoulli
k_ = 10; a1 = 2*k_ + sp.Rational(k_*(k_-12), 6)/Bn(k_) - sp.Rational(k_*(k_+2), 6)/Bn(k_+2)
chk('serre_E10_cusp_coefficient', sp.nsimplify(a1) == sp.Rational(38016, 691), str(a1))
# --- counterterm1995: K0 - K0^(1) = -pi/2 - log 2 ---
K01 = mp.digamma(0.5) - mp.log(pi)
chk('K0_minus_K0sigma1', abs((K0 - K01) - (-pi/2 - L2)) < 1e-25)
# --- diagonal2003 table: -K0 - (2-4a) for canonical a ---
tab = {'a=0': 2, 'a=1/2': 0, 'a=-log(pi)/2': 2 + 2*mp.log(pi), 'a=-log(2pi)/2': 2 + 2*mp.log(2*pi)}
R['arakelov_minus_K0_gaps'] = {kk: mp.nstr(-K0 - v, 6) for kk, v in tab.items()}
chk('arakelov_gaps', abs(-K0 - (2 + 2*mp.log(2*pi)) - mp.mpf('-0.3036')) < 1e-3)
# --- eisenstein1990: S_reg=-zeta'/zeta(1/2)=K0/2 ---
chk('Sreg_equals_K0_over_2', abs(-mp.zeta(0.5, derivative=1)/mp.zeta(0.5) - K0/2) < 1e-20)
# --- sos2010 identity constant K5(0)=K0+4 ---
chk('K5_equals_K0_plus_4', abs(mp.digamma(1.25) - mp.log(pi) - (K0 + 4)) < 1e-25)
# --- Gamma Planck ladder k = sum e^{-(2m+1/2)a} ---
chk('gamma_planck_ladder', abs(mp.nsum(lambda m: mp.e**(-(2*m + 0.5)*0.3), [0, mp.inf]) - k(mp.mpf(0.3))) < 1e-25)
# --- residues of the completed zeta Z(s)=pi^{-s/2}Gamma(s/2)zeta(s) at 0 and 1 (xi itself is entire) ---
Z = lambda s: pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
eps = mp.mpf('1e-12')
chk('completed_zeta_residues', abs(eps*Z(eps) + 1) < 1e-9 and abs(eps*Z(1 + eps) - 1) < 1e-9)
chk('xi_entire_at_0_1', abs(xi(mp.mpf('1e-15')) - mp.mpf(1)/2) < 1e-10 and abs(xi(1 + mp.mpf('1e-15')) - mp.mpf(1)/2) < 1e-10)
R['all_ok'] = all(ok.values()); R['failed'] = [k_ for k_, v in ok.items() if not v]; R['seconds'] = round(time.time() - t0, 1)
json.dump(R, open(__file__.replace('.py', '.json'), 'w'), indent=1, default=str)
print(json.dumps({'all_ok': R['all_ok'], 'failed': R['failed'], 'seconds': R['seconds']}))

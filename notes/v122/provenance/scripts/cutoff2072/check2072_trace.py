# t2072: the u->0 regularized pairing <Phi(F),Phi(G)> on X = A_Q/Q^x vs the project's W = P + H_A - M_A<F,G>.
# Conventions (t2068): theta_u xi(x)=e^{-u/2} xi(lambda_u^{-1}x); theta(g)=U(h) with h(x)=|x|^{-1/2} g(log|x|) (Zhat^x-invariant),
# Connes' Haar on K_v^* normalized by int_{1<=|u|<=Lam} d*u ~ log Lam  (on R^*: d*u = du/(2|u|)).
# Connes 1999 Thm 3/4: Tr(R_Lam U(h)) = 2 h(1) log Lam + sum_v int'_v h(u^{-1})/|1-u| d*u + o(1).
# g := F * G~,  G~(x) = conj G(-x),  so g(b) = <F, T_b G>,  g(0) = <F,G>.
import mpmath as mp, json
mp.mp.dps = 20
E, L2P = mp.euler, mp.log(2*mp.pi)
K0 = mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi)
k = lambda a: mp.exp(-abs(a)/2)/(-mp.expm1(-2*abs(a)))
out = {}

def connes_inf_xvar(g, lo=-0.95, hi=40):
    # int'_{R^*} h(u^{-1})/|1-u| d*u  with u=1-x, d*u=du/(2|u|): distribution T=Pf_1(1/|x|)+2(gamma+log2pi)delta in x
    h = lambda y: abs(y)**mp.mpf(-0.5)*g(mp.log(abs(y)))
    phi = lambda x: h(1/(1-x))/(2*abs(1-x))
    f = lambda x: (phi(x)+phi(-x)-2*phi(0))/x
    pf = mp.quad(f, [0, mp.mpf('0.5'), 1]) + mp.quad(lambda x: (phi(x)+phi(-x))/x, [1, mp.mpf('0.99999')*0+1, 2, 10, 100, 1e4, 1e6])
    return pf + 2*(E+L2P)*phi(0)

def connes_inf_logvar(g):
    # same distribution written in a = log scale: Pf_a int k(|a|) g(a) da + (gamma+log2pi) g(0)  (Hadamard at scale 1 in a)
    f = lambda a: k(a)*(g(a)+g(-a)) - g(0)/a
    pf = mp.quad(f, [0, 1]) + mp.quad(lambda a: k(a)*(g(a)+g(-a)), [1, 5, 20, mp.inf])
    return pf + (E+L2P)*g(0)

def W_inf_fourier(gh):
    # (1/2pi) int ghat(t) (Re psi(1/4+it/2) - log pi) dt  (Weil archimedean term, ghat(t)=int g e^{itu})
    return mp.quad(lambda t: gh(t)*(mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2)) - mp.log(mp.pi)), [-mp.inf, -20, 0, 20, mp.inf])/(2*mp.pi)

def W_inf_degree(g):
    # project degree (Laplacian) form: K0 g(0) + int_0^inf K(a)(g(0)-(g(a)+g(-a))/2) da, K=2k
    return K0*g(0) + mp.quad(lambda a: k(a)*(2*g(0)-g(a)-g(-a)), [0, 1, 5, 20, mp.inf])

# --- A. archimedean: Connes int' == -W_inf, three independent forms; non-even g included
A = {}
for name, s, c in (('gauss_s0.5_even', mp.mpf('0.5'), 0), ('gauss_s0.3_shift0.2', mp.mpf('0.3'), mp.mpf('0.2'))):
    g = lambda a, s=s, c=c: mp.exp(-(a-c)**2/(2*s**2))
    gh = lambda t, s=s, c=c: s*mp.sqrt(2*mp.pi)*mp.exp(-s**2*t**2/2)*mp.exp(1j*t*c)
    cx, ca, wf, wd = connes_inf_xvar(g), connes_inf_logvar(g), W_inf_fourier(lambda t: mp.re(gh(t))), W_inf_degree(g)
    A[name] = dict(connes_xvar=mp.nstr(cx, 15), connes_logvar=mp.nstr(ca, 15), minus_Winf_fourier=mp.nstr(-wf, 15),
                   minus_Winf_degree=mp.nstr(-wd, 15), x_minus_log=mp.nstr(cx-ca, 3), x_plus_Wf=mp.nstr(cx+wf, 3), deg_minus_fourier=mp.nstr(wd-wf, 3),
                   omit_const_miss=mp.nstr(cx-(E+L2P)*g(0)+wf, 8))
out['A_archimedean'] = A

# --- B. full window ledger, A=1.1 (contains log2, log3), F != G, non-even
Aw = mp.mpf('1.1')
bump = lambda u: mp.exp(-1/(1-(2*u/Aw)**2)) if abs(u) < Aw/2 else mp.mpf(0)
F = lambda u: bump(u)*(1+mp.mpf('0.6')*u)
G = lambda u: bump(u)*(mp.mpf('0.4')+u**2 - mp.mpf('0.3')*u)
ip = lambda f1, f2: mp.quad(lambda u: f1(u)*f2(u), [-Aw/2, 0, Aw/2])
cache = {}
def g(b):
    b = mp.mpf(b)
    if abs(b) >= Aw: return mp.mpf(0)
    key = mp.nstr(b, 18)
    if key not in cache:
        lo, hi = max(-Aw/2, b-Aw/2), min(Aw/2, b+Aw/2)
        cache[key] = mp.quad(lambda u: F(u)*G(u-b), [lo, (lo+hi)/2, hi])   # <F, T_b G>
    return cache[key]
mp.mp.dps = 15
an = {2: mp.log(2)/mp.sqrt(2), 3: mp.log(3)/mp.sqrt(3)}
assert mp.log(4) > Aw
# trace side (geometric, zeros-blind): archimedean int' + p-adic orbit atoms (p-adic unit diagonal = 0, unramified character)
def connes_window(g):
    f = lambda a: k(a)*(g(a)+g(-a)) - g(0)/a
    pf = mp.quad(f, [0, mp.mpf('0.25'), mp.mpf('0.5'), 1]) + mp.quad(lambda a: k(a)*(g(a)+g(-a)), [1, Aw])
    return pf + (E+L2P)*g(0)
arch_tr = connes_window(g)
prime_tr = sum(an[n]*(g(mp.log(n))+g(-mp.log(n))) for n in an)
trace_fin = arch_tr + prime_tr
# project side, computed DIRECTLY from F,G (jump form), not through g:
FG = ip(F, G)
def jump(b):  # <(I-T_b)F,(I-T_b)G> with zero extension
    Tb = lambda f: (lambda u: f(u-b) if abs(u-b) < Aw/2 else mp.mpf(0))
    d1 = lambda u: F(u)*(1 if abs(u) < Aw/2 else 0) - Tb(F)(u)
    d2 = lambda u: G(u)*(1 if abs(u) < Aw/2 else 0) - Tb(G)(u)
    pts = sorted(set([-Aw/2, Aw/2, b-Aw/2, b+Aw/2, (b)/2]))
    return mp.quad(lambda u: d1(u)*d2(u), pts)
J_inf = mp.quad(lambda b: k(b)*jump(b), [0, mp.mpf('0.25'), mp.mpf('0.5'), 1, Aw]) + 2*FG*mp.quad(k, [Aw, mp.inf])
J_pr = sum(an[n]*jump(mp.log(n)) for n in an)
H_A = J_inf + J_pr
M_A = -K0 + 2*sum(an.values())
B = H_A - M_A*FG                       # = W - P
Cp = lambda f: mp.quad(lambda u: f(u)*mp.exp(u/2), [-Aw/2, Aw/2]); Cm = lambda f: mp.quad(lambda u: f(u)*mp.exp(-u/2), [-Aw/2, Aw/2])
P = Cp(F)*Cm(G) + Cm(F)*Cp(G)
out['B_window_A1.1'] = dict(FG=mp.nstr(FG, 12), arch_trace=mp.nstr(arch_tr, 12), prime_trace=mp.nstr(prime_tr, 12), trace_fin=mp.nstr(trace_fin, 12),
    H_A=mp.nstr(H_A, 12), M_A=mp.nstr(M_A, 12), B_eq_W_minus_P=mp.nstr(B, 12), P=mp.nstr(P, 12),
    trace_fin_plus_B=mp.nstr(trace_fin + B, 3),
    trace_fin_minus_B=mp.nstr(trace_fin - B, 8),
    note='trace_fin = -(W-P) = M_A<F,G> - H_A(F,G); divergent part 2 log(Lam) <F,G> removed')
print(json.dumps(out, indent=1)); json.dump(out, open('check2072_trace.json', 'w'), indent=1)

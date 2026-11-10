# t2072 B (exact version): polynomial-bump F,G on I_A, A=11/10 (contains log2, log3); g=F*G~ exact piecewise polynomial (sympy);
# jump-form identity <(I-T_b)F,(I-T_b)G> = 2<F,G> - g(b) - g(-b) verified symbolically; trace vs ledger compared in mpmath (dps 40).
import sympy as sp, mpmath as mp, json
mp.mp.dps = 40
u, b = sp.symbols('u b', real=True)
A = sp.Rational(11, 10); h = A/2
bump = (1-(u/h)**2)**4
F = bump*(1+sp.Rational(3, 5)*u)
G = bump*(sp.Rational(2, 5)+u**2-sp.Rational(3, 10)*u)
FG = sp.integrate(F*G, (u, -h, h))
# g(b) = <F, T_b G> = int F(u) G(u-b) du, for 0<=b<=A: u in [b-h, h];  for -A<=b<=0: u in [-h, b+h]
gp = sp.expand(sp.integrate(F*G.subs(u, u-b), (u, b-h, h)))
gm = sp.expand(sp.integrate(F*G.subs(u, u-b), (u, -h, b+h)))
# direct jump form for 0<=b<=A (zero extension): <F-T_bF, G-T_bG> = <F,G> + <T_bF,T_bG> - <F,T_bG> - <T_bF,G>
FtG = sp.integrate(F*G.subs(u, u-b), (u, b-h, h))            # <F,T_bG>
tFG = sp.integrate(F.subs(u, u-b)*G, (u, b-h, h))            # <T_bF,G>
jump = 2*FG - FtG - tFG
gneg_at = sp.expand(gm.subs(b, -b))                          # g(-b) for b>=0
id_resid = sp.simplify(sp.expand(jump - (2*FG - gp - gneg_at)))
out = {'jump_identity_residual(symbolic)': str(id_resid)}
def exactpoly(expr):
    cs = [sp.Rational(c) for c in sp.Poly(expr, b).all_coeffs()]
    cm = [mp.mpf(c.p)/c.q for c in cs]
    return lambda x: mp.polyval(cm, x)
gpos = exactpoly(gp); gneg = exactpoly(gneg_at)
FGm = mp.mpf(sp.Rational(FG).p)/sp.Rational(FG).q
Am = mp.mpf(11)/10
k = lambda a: mp.exp(-a/2)/(-mp.expm1(-2*a))
E, L2P = mp.euler, mp.log(2*mp.pi)
K0 = mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi)
an = {2: mp.log(2)/mp.sqrt(2), 3: mp.log(3)/mp.sqrt(3)}
geven = lambda a: gpos(a) + gneg(a)            # g(a)+g(-a), a>=0
# trace side (Connes int' in log variable; verified = x-variable form in check2072_trace.py A)
arch_tr = mp.quad(lambda a: k(a)*geven(a) - FGm/a, [0, Am/4, Am/2, 1]) + mp.quad(lambda a: k(a)*geven(a), [1, Am]) + (E+L2P)*FGm
prime_tr = sum(an[n]*geven(mp.log(n)) for n in an)
trace_fin = arch_tr + prime_tr
# ledger side (jump form, exact jump polynomial; beyond b=A supports are disjoint so jump = 2<F,G>)
jl = exactpoly(sp.expand(jump))
J_inf = mp.quad(lambda a: k(a)*jl(a), [0, Am/4, Am/2, 1, Am]) + 2*FGm*mp.quad(k, [Am, mp.inf])
J_pr = sum(an[n]*jl(mp.log(n)) for n in an)
H_A = J_inf + J_pr; M_A = -K0 + 2*sum(an.values())
B = H_A - M_A*FGm
Cp = lambda f: sp.integrate(f*sp.exp(u/2), (u, -h, h)); Cm = lambda f: sp.integrate(f*sp.exp(-u/2), (u, -h, h))
P = sp.N(Cp(F)*Cm(G) + Cm(F)*Cp(G), 40)
# degree-form diagonal coefficient of the trace (everything that multiplies <F,G>):
out.update(FG=str(FG), FG_num=mp.nstr(FGm, 20), arch_trace=mp.nstr(arch_tr, 20), prime_trace=mp.nstr(prime_tr, 20),
           trace_fin=mp.nstr(trace_fin, 20), H_A=mp.nstr(H_A, 20), M_A=mp.nstr(M_A, 20), W_minus_P=mp.nstr(B, 20), P=str(P),
           trace_fin_plus_W_minus_P=mp.nstr(trace_fin + B, 5), W=mp.nstr(B + mp.mpf(str(P)), 20),
           trace_fin_vs_minus_W=mp.nstr(trace_fin + B + mp.mpf(str(P)), 20),
           arch_trace_via_FP_route=mp.nstr(mp.quad(lambda a: k(a)*(geven(a)-2*FGm), [0, Am/4, Am/2, 1, Am]) - 2*FGm*mp.quad(k,[Am,mp.inf]) + (mp.pi/2+2*mp.log(2))*FGm + (E+L2P)*FGm, 20))
print(json.dumps(out, indent=1)); json.dump(out, open('check2072_window_exact.json', 'w'), indent=1)

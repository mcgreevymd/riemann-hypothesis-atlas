# t2072: exact/high-precision checks of the constants in the u->0 regularization (zeros-blind).
import sympy as sp, mpmath as mp, json
mp.mp.dps = 30
out = {}
a = sp.symbols('a', positive=True)
k = sp.exp(-a/2)/(1-sp.exp(-2*a))
ser = sp.series(k, a, 0, 3).removeO()
out['k_inf_series'] = str(sp.expand(ser))            # expect 1/(2a) + 1/4 - a/48 + ...
out['K=2k_series'] = str(sp.expand(sp.series(2*k, a, 0, 3).removeO()))
# Even-average identity (t2068) re-checked
out['even_avg_minus_k'] = str(sp.simplify(sp.exp(-a/2)*(1/(1-sp.exp(-a))+1/(1+sp.exp(-a)))/2 - k))
# K0 closed form
K0 = mp.digamma(0.25) - mp.log(mp.pi)
out['K0'] = mp.nstr(K0, 20)
out['K0_minus_closed(-g-pi/2-3log2-logpi)'] = mp.nstr(K0 - (-mp.euler - mp.pi/2 - 3*mp.log(2) - mp.log(mp.pi)), 5)
# Hadamard finite part of int_0^inf K, K = 2k:   FP = int_0^1 (K - 1/a) + int_1^inf K
K = lambda x: 2*mp.exp(-x/2)/(-mp.expm1(-2*x))
FP = mp.quad(lambda x: K(x) - 1/x, [0, 1]) + mp.quad(K, [1, mp.inf])
out['FP_H_int0inf_K'] = mp.nstr(FP, 20)
out['FP_minus(pi/2+2log2)'] = mp.nstr(FP - (mp.pi/2 + 2*mp.log(2)), 5)
# -K0 = (gamma+log 2pi) + FP
out['-K0-(gamma+log2pi)-FP'] = mp.nstr(-K0 - (mp.euler + mp.log(2*mp.pi)) - FP, 5)
# Fourier transform of Pf_1(1/|x|) (Hadamard at scale 1) with character e^{-2 pi i x y}:  = -2gamma - 2log(2pi) - 2log|y|
# test on phi_s(x)=exp(-pi x^2/s^2), phihat_s(y)= s exp(-pi s^2 y^2), for two s (pins both the log and the delta coefficient)
res = {}
for s in (mp.mpf(1), mp.mpf(2), mp.mpf('0.7')):
    phi = lambda x: mp.exp(-mp.pi*x**2/s**2)
    lhs = 2*(mp.quad(lambda x: (phi(x)-1)/x, [0, 1]) + mp.quad(lambda x: phi(x)/x, [1, mp.inf]))
    rhs = mp.quad(lambda y: (-2*mp.euler - 2*mp.log(2*mp.pi) - 2*mp.log(abs(y)))*s*mp.exp(-mp.pi*s**2*y**2), [-mp.inf, 0, mp.inf])
    res[str(s)] = mp.nstr(lhs - rhs, 5)
out['FT_Pf_check_lhs_minus_rhs'] = res
# => Connes' extension int' (FT vanishing at y=1) = Pf_1(1/|x|) + 2(gamma+log 2pi) delta_0.
# Gamma expansion: Re psi(1/4+it/2) - psi(1/4) = sum_j 2t^2/(c_j(c_j^2+t^2)), c_j = 2j+1/2
res = {}
for t in (mp.mpf('0.3'), mp.mpf(3), mp.mpf(17)):
    lhs = mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2)) - mp.digamma(mp.mpf(1)/4)
    rhs = mp.nsum(lambda j: 2*t**2/((2*j+mp.mpf(1)/2)*((2*j+mp.mpf(1)/2)**2 + t**2)), [0, mp.inf])
    res[str(t)] = mp.nstr(lhs - rhs, 5)
out['gamma_expansion_residual'] = res
print(json.dumps(out, indent=1)); json.dump(out, open('check2072_sym.json', 'w'), indent=1)

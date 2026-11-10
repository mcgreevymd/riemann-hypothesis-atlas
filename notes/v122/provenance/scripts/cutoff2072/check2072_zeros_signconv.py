# t2072 C: CONVENTION CHECK ONLY (zeros used to read off the sign convention of W, never in the construction).
# Gaussian g(a)=exp(-a^2/(2 s^2)), s=0.1: ledger W(g) = P + W_inf - sum a_n (g(log n)+g(-log n))  vs  sum_rho ghat(gamma_rho).
import mpmath as mp, json
mp.mp.dps = 25
s = mp.mpf('0.1')
g = lambda a: mp.exp(-a**2/(2*s**2)); gh = lambda t: s*mp.sqrt(2*mp.pi)*mp.exp(-s**2*t**2/2)
K0 = mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi)
k = lambda a: mp.exp(-a/2)/(-mp.expm1(-2*a))
Winf = K0*g(0) + mp.quad(lambda a: k(a)*(2*g(0)-2*g(a)), [0, 1, mp.inf])
P = gh(1j/2) + gh(-1j/2)
primes = mp.mpf(0)
import sympy as sp
for n in range(2, 400):
    fac = sp.factorint(n)
    if len(fac) == 1:
        p = list(fac)[0]; primes += mp.log(p)/mp.sqrt(n)*2*g(mp.log(n))
W_ledger = mp.re(P) + Winf - primes
Z = 0
for j in range(1, 120):
    Z += 2*gh(mp.im(mp.zetazero(j)))
trace_fin = -(W_ledger - mp.re(P))
out = dict(P=mp.nstr(mp.re(P), 15), Winf=mp.nstr(Winf, 15), primes=mp.nstr(primes, 15), W_ledger=mp.nstr(W_ledger, 15),
           sum_rho_ghat=mp.nstr(Z, 15), diff=mp.nstr(W_ledger - Z, 3), trace_fin=mp.nstr(trace_fin, 15),
           )
out['trace_fin_minus_(P_minus_sum_rho)'] = mp.nstr(trace_fin - (mp.re(P) - Z), 3)
print(json.dumps({kk: v for kk, v in out.items() if v is not None}, indent=1))
json.dump({kk: v for kk, v in out.items() if v is not None}, open('check2072_zeros_signconv.json', 'w'), indent=1)

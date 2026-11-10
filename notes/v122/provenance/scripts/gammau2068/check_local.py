# Zeros-blind check: Lefschetz/fixed-point local indices of the scaling x -> lam*x
# (half-density normalised, |lam|^{1/2}) on R and on Q_p reproduce k_inf and Lambda(n)/sqrt(n).
import sympy as sp, mpmath as mp
a=sp.symbols('a',positive=True)
# archimedean: fixed point x=0 of x->u x on R, u in R^*, |u|=e^{-a}; index 1/|1-u|; even part: u=+-e^{-a}
idx = sp.exp(-a/2)*(1/(1-sp.exp(-a)) + 1/(1+sp.exp(-a)))/2
print("arch even-averaged index - k_inf :", sp.simplify(idx - sp.exp(-a/2)/(1-sp.exp(-2*a))))
# |u|>1 side (u=+-e^{a}) gives the same kernel (symmetry a->-a of k(|a|))
idx2 = sp.exp(a/2)*(1/sp.Abs(1-sp.exp(a)) + 1/(1+sp.exp(a)))/2
print("arch |u|>1 side - k_inf          :", sp.simplify(sp.simplify(idx2.rewrite(sp.exp)).subs(sp.Abs(1-sp.exp(a)),sp.exp(a)-1) - sp.exp(-a/2)/(1-sp.exp(-2*a))))
# p-adic: fixed point x=0 of x->u x on Q_p, |u|_p = p^{-k}; index 1/|1-u|_p = 1 (k>0); half density p^{-k/2};
# shell volume in log-scale measure: d*u on Q_p^* restricted to |u|=p^{-k} has mass vol(Z_p^*)=1 at displacement k log p;
# converting to Lebesgue du on R (u = k log p) the atom weight is log p (Haar normalisation of Q_p^*/Z_p^* ~ log p Z).
for p,k in [(2,1),(2,3),(3,2),(5,1)]:
    n=p**k
    w = mp.log(p)*p**(-k/2)
    print(f"n={n}: local atom weight {w}  vs Lambda(n)/sqrt(n) = {mp.log(p)/mp.sqrt(n)}")

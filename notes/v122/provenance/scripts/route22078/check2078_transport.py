"""Check: comoving (scaling-transported) FS metrics. h_u = transport of FS metric of Gamma_0 by sigma_u(z,w)=(z,e^u w).
g_u^tr(z,w) = -log|e^{-u}w - z|^2 + log(1+|z|^2) + log(1+e^{-2u}|w|^2),  omega_u = mu(z) + mu^{(u)}(w)  (w = e^u * FS sample).
Prediction: T_tr = 3 - 4 log(2 sinh(a/2)) + a coth a + u coth u + v coth v.
T = int_{Gamma_v} g_u omega + int_X omega_u g_v omega   (third class omega = FS, fixed)."""
import numpy as np, json
from scipy import integrate
def gtr(uu, z, w): return -np.log(abs(np.exp(-uu)*w - z)**2) + np.log(1+abs(z)**2) + np.log(1+np.exp(-2*uu)*abs(w)**2)
def T_num(uu, vv, N=4_000_000, seed=2):
    tt = np.exp(vv)
    def integ(xx, th, scale):
        r = xx/(1-xx); z = np.sqrt(r)*np.exp(1j*th)/scale
        return gtr(uu, z, tt*z)/(2*np.pi)          # FS-distributed z/scale, density in xx is uniform
    t1 = sum(integrate.dblquad(lambda th, xx: integ(xx, th, sc), 0, 1, 0, 2*np.pi, epsabs=1e-9)[0] for sc in (1.0, tt))
    rng = np.random.default_rng(seed)
    def samp(n): x = rng.random(n); return np.sqrt(x/(1-x))*np.exp(2j*np.pi*rng.random(n))
    z, w, w2 = samp(N), samp(N), np.exp(uu)*samp(N)
    A = gtr(vv, z, w); B = gtr(vv, z, w2)
    return t1 + A.mean() + B.mean(), np.hypot(A.std(), B.std())/np.sqrt(N)
cth = lambda x: x/np.tanh(x) if x != 0 else 1.0
rows = []
for uu, vv in [(0.7, 0.0), (1.3, 0.4), (-0.5, 1.5)]:
    a = abs(uu-vv); pred = 3 - 4*np.log(2*np.sinh(a/2)) + cth(a) + cth(uu) + cth(vv)
    num, se = T_num(uu, vv); rows.append(dict(u=uu, v=vv, num=num, se=se, pred=pred)); print(rows[-1])
json.dump(rows, open('check2078_transport.json', 'w'), indent=1)

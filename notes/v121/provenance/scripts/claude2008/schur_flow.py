"""W-bridge review (Claude, Nov 2026). Private research artifact; RH NOT proved.
Object: the Schur/Verblunsky flow of the prime-side Weil kernel on a uniform window grid.
On boxes of width h, W = arch jumps + prime springs - M + pole is a symmetric TOEPLITZ matrix (pole term too:
C+_i C-_j ~ e^{(a_i - a_j)/2}).  Levinson-Durbin gives reflection coefficients kappa_n and prediction errors s_n
(s_n = det T_{n+1}/det T_n).  Exact: W >= 0 on every grid window [0, nh] (n <= N)  <=>  |kappa_j| < 1 for j < N.
Also: S = C^T Q^{-1} C (Q = W - P) on orthonormal boxes, versus -J2 (Woodbury limit).
Controls: synthetic ghost (exact rank-6 zero move), Davenport-Heilbronn, Beurling move of p = 2, shuffled chi_4.
"""
import json, math, random, sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import r33_onemode as r3

def levinson(t):
    """t = first column of a symmetric Toeplitz matrix; returns kappa (len n-1), s (prediction errors), first exit index."""
    n = len(t); a = np.zeros(n); a[0] = 1.0; s = [t[0]]; kap = []
    for m in range(1, n):
        acc = t[m] + np.dot(a[1:m], t[m - 1:0:-1])
        k = -acc / s[-1]; kap.append(k)
        a_new = a.copy(); a_new[1:m] = a[1:m] + k * a[m - 1:0:-1]; a_new[m] = k; a = a_new
        s.append(s[-1] * (1 - k * k))
        if abs(k) >= 1 or s[-1] <= 0:
            return np.array(kap), np.array(s), m
    return np.array(kap), np.array(s), None

def box_ft(z, a, b):
    return (np.exp(1j * z * b) - np.exp(1j * z * a)) / (1j * z * np.sqrt(b - a))

def ghost_col(a, b, t, beta):
    """first column of the exact zero move Delta (quadruple +-t +- i beta in, on-line pair +-t out); Toeplitz."""
    f0 = lambda z: box_ft(z, a[:1], b[:1])[0]
    col = np.zeros(len(a), dtype=complex)
    for s in (t - 1j * beta, t + 1j * beta, -t - 1j * beta, -t + 1j * beta):
        col += box_ft(s, a, b) * np.conj(f0(np.conj(s)))
    for g in (t, -t):
        col -= box_ft(g, a, b) * np.conj(f0(g))
    return col.real

class Moved(r3.Sector):
    def __init__(self, p, d):
        super().__init__("zeta"); self.p, self.d = p, d
    def atoms(self, xmax):
        L, W = r3.Sector("zeta").atoms(xmax + 1.0); L, W = L.copy(), W.copy(); lq = math.log(self.p) + self.d
        for i in range(len(L)):
            k = round(L[i] / math.log(self.p))
            if k >= 1 and abs(math.exp(L[i]) - self.p ** k) < 0.5:
                L[i] = k * lq; W[i] = lq * math.exp(-k * lq / 2)
        o = np.argsort(L); keep = L[o] < xmax
        return L[o][keep], W[o][keep]

class Chi4Shuffled(r3.Sector):
    def __init__(self, table):
        super().__init__("chi_4"); self.chi = lambda p: table.get(p, 0)

def dh_lambda(nmax, kap=(math.sqrt(10 - 2 * math.sqrt(5)) - 2) / (math.sqrt(5) - 1)):
    A = [0.0, 1.0, kap, -kap, -1.0]; a = np.array([A[n % 5] for n in range(nmax + 1)]); lam = np.zeros(nmax + 1)
    for n in range(2, nmax + 1):
        s = a[n] * math.log(n)
        for d in range(2, int(math.isqrt(n)) + 1):
            if n % d == 0:
                s -= lam[d] * a[n // d]
                if d != n // d: s -= lam[n // d] * a[d]
        lam[n] = s
    return lam

class DH(r3.Sector):
    def __init__(self, nmax):
        super().__init__("chi_5"); self.a, self.kappa, self.pole = 1, 1.5, False; self.lam = dh_lambda(nmax)
    def atoms(self, xmax):
        n = np.arange(2, min(int(math.exp(xmax)) + 2, len(self.lam))); w = self.lam[n] / np.sqrt(n); k = w != 0
        return np.log(n[k].astype(float)), w[k]

def wcol(ell, h, S, pole=True):
    Z, kp, km = r3.grid_Z(ell, h, S)
    W = Z + (np.outer(kp, km) + np.outer(km, kp) if pole else 0)
    return W[:, 0].copy(), W, Z, kp, km

def main():
    out = {}
    h, ell = 0.01, 6.0
    col, W, Z, kp, km = wcol(ell, h, r3.Sector("zeta"))
    kap, s, ex = levinson(col)
    out["zeta"] = {"h": h, "ell": ell, "exit": ex, "max|kappa|": float(np.abs(kap).max()),
                   "min(1-|kappa|) on n>=100": float((1 - np.abs(kap[99:])).min()),
                   "s_n at ell=1,2,3,4,5,6": [float(s[int(round(l / h)) - 1]) for l in (1, 2, 3, 4, 5, 6)],
                   "lambda_min(W) at ell=2,4,6": [float(np.linalg.eigvalsh(W[:m, :m])[0]) for m in (200, 400, 600)]}
    # Woodbury: S = C^T Q^{-1} C on orthonormal boxes, Q = Z
    Sd = {}
    for l in (2.0, 4.0, 6.0):
        m = int(round(l / h)); C = np.column_stack([kp[:m], km[:m]]); S = C.T @ np.linalg.solve(Z[:m, :m], C)
        Sd[str(l)] = {"S": S.round(8).tolist(), "eig": np.linalg.eigvalsh(S).round(8).tolist(),
                      "S + J2": (S + np.array([[0, 1.0], [1.0, 0]])).tolist()}
    out["S_orthonormal"] = Sd
    # controls
    a = h * np.arange(len(col)); b = a + h
    import mpmath as mp
    g = [float(mp.im(mp.zetazero(n))) for n in range(1, 6)]
    ctrl = {}
    for name, t, beta in (("ghost gamma1 b=0.3", g[0], 0.3), ("ghost gamma5 b=0.3", g[4], 0.3), ("ghost gamma1 b=0.05", g[0], 0.05)):
        _, _, e = levinson(col + ghost_col(a, b, t, beta)); ctrl[name] = None if e is None else round(e * h, 2)
    Sdh = DH(int(math.exp(ell)) + 10); c2, *_ = wcol(ell, h, Sdh, pole=False); _, _, e = levinson(c2)
    ctrl["Davenport-Heilbronn (no pole)"] = None if e is None else round(e * h, 2)
    for d in (-6e-5, +3e-4, -3e-5):
        c3, *_ = wcol(4.0, h, Moved(2, d)); _, _, e = levinson(c3)
        ctrl["Beurling: log 2 -> log 2 %+.0e" % d] = None if e is None else round(e * h, 2)
    odd = r3.primes_upto(int(math.exp(ell)) + 2)[1:]; true = {p: r3.kronecker(-4, p) for p in odd}
    ex = []
    for seed in range(10):
        vals = [true[p] for p in odd]; random.Random(seed).shuffle(vals)
        Zc, kp2, km2 = r3.grid_Z(ell, h, r3.Sector("zeta")); Wc, _, _ = r3.grid_Z(ell, h, Chi4Shuffled(dict(zip(odd, vals))))
        _, _, e = levinson((Zc + Wc + np.outer(kp2, km2) + np.outer(km2, kp2))[:, 0]); ex.append(None if e is None else round(e * h, 2))
    Zc, kp2, km2 = r3.grid_Z(ell, h, r3.Sector("zeta")); Wc, _, _ = r3.grid_Z(ell, h, Chi4Shuffled(true))
    _, _, e = levinson((Zc + Wc + np.outer(kp2, km2) + np.outer(km2, kp2))[:, 0])
    ctrl["Dedekind Q(i), genuine chi_4"] = None if e is None else round(e * h, 2)
    ctrl["Dedekind with shuffled chi_4 (10 seeds)"] = ex
    out["exits (ell where the Schur flow leaves the disk)"] = ctrl
    # mechanism test: hyperbolic radius steps at prime-power arrivals vs elsewhere (zeta, ell <= 4)
    rho = np.arctanh(np.abs(kap[:400])); d = np.diff(rho)
    L, _ = r3.Sector("zeta").atoms(4.1)
    arr = set(int(x // h) for x in L) | set(int(x // h) + 1 for x in L)
    idx = np.arange(1, len(rho))
    at = np.array([d[i - 1] for i in idx if i in arr]); off = np.array([d[i - 1] for i in idx if i not in arr])
    out["mechanism: d(artanh|kappa|) per step (ell<=4)"] = {
        "at prime-power arrivals: n, mean, frac>0": [len(at), float(at.mean()), float((at > 0).mean())],
        "elsewhere: n, mean, frac>0": [len(off), float(off.mean()), float((off > 0).mean())]}
    json.dump(out, open(os.path.join(HERE, "schur_flow.json"), "w"), indent=1, default=float)
    print(json.dumps(out, indent=1, default=float))

if __name__ == "__main__":
    main()

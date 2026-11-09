"""Round 33: the one unstable (Perron) mode of the archimedean+prime part of Weil's form; the pole/Perron 2x2 block as a
second channel; Dirichlet sectors (no pole); a Maslov-type dequantization of the archimedean Gamma term.

Kernel (L2-normalised boxes of width h at log-scales; generalises round 32).  For a sector with conductor q, parity a,
character weights chi(n) and a deformation parameter hbar of the Gamma term (digamma psi(z) -> psi(z/hbar) + log hbar):
  arch(g)  = (log(q/pi) - gamma) g(0) + 2 int_0^oo [e^{-2 hbar x} g(0) - e^{-(1/2+a) x} g(x)] hbar/(1 - e^{-2 hbar x}) dx
  pole     = 2 K(1/2) K(-1/2) for zeta only (chi = 1)
  primes   = -2 sum_n chi(n) Lambda(n) n^{-1/2} g(log n)
hbar = 1 is the Weil form of L(s, chi); hbar -> 0 replaces log Gamma by its Stirling main term (kernel 1/(2x)).
Zeros are used only in part A (validation of the chi-sector archimedean term).

A  kernel checks: reproduces round 32 (zeta); chi-sector formula vs zeros of L(s, chi); hbar = 1 identity and hbar -> 0
B  one unstable mode: n_-(Z), Z = arch + primes, across bases (box grids on [0, log X], integer lattice m <= X, prime sites,
   prime-gap tiling, Legendre in Arb multiprecision) for X = 1e3, 1e4, 1e5; onset in ell; the unconditional lower bound
C  the pole/Perron 2x2 block: margin vs X, its split (Perron gain vs leakage); SOS and single-channel ladder fits with the
   pole/Perron pair as a second channel vs the round-31 plateau
D  Dirichlet sectors chi_4, chi_3, chi_5, chi_-163: J_pq(chi) closed form, archimedean symbol, n_- of arch / ferro part /
   full form on box grids
E  Maslov: h log B(a/h, b/h) limit; hbar-deformation of the Gamma term vs the 2x2 balance; width scaling = rescaling
F  onset of the Perron mode (single-box witness); positivity window in hbar; symbol inequality; chi(n) = -1 atoms as an
   effective pole
G  W restricted to span{v, phi}; the Perron mode's W-energy
H  sign of the SOS deficit W - fit on the pole/Perron span and on W's near-null space
I  Caratheodory-Fejer check: roots of the Perron vector (box grid, Toeplitz) lie on the unit circle
Runs used for r33_onemode.json: main (A B D E F G I) and, in parallel with --out=..., C, B:legendre and H, then merged.
"""
import gc, json, math, os, sys, time
import numpy as np
import mpmath as mp
import scipy.linalg as sla
from scipy.sparse.linalg import eigsh, LinearOperator

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r31_weil as rw

OUT = os.path.join(HERE, next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--out=")), "r33_onemode.json"))
out = {}
T0 = time.time()
EG = 0.57721566490153286061
LOGPI = math.log(math.pi)
GL = {n: np.polynomial.legendre.leggauss(n) for n in (6, 8, 16, 32)}
RHO = float(max(np.roots([1, 0, -1, -1]).real))


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def save():
    json.dump(out, open(OUT, "w"), indent=1, default=float)


def primes_upto(n):
    return [p for p, lam in rw.prime_powers(n) if abs(lam - math.log(p)) < 1e-12]


# ------------------------------------------------------------------------------------------------ sectors
def kronecker(d, p):
    """Kronecker symbol (d/p) for a prime p."""
    if p == 2:
        return 0 if d % 2 == 0 else (1 if d % 8 in (1, 7) else -1)
    r = pow(d % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)


SECTORS = {
    "zeta": (1, 0, lambda p: 1, True),
    "chi_4": (4, 1, lambda p: kronecker(-4, p), False),
    "chi_3": (3, 1, lambda p: kronecker(-3, p), False),
    "chi_5": (5, 0, lambda p: kronecker(5, p), False),
    "chi_-163": (163, 1, lambda p: kronecker(-163, p), False),
}


class Sector:
    def __init__(self, name="zeta", hbar=1.0):
        self.name = name
        self.q, self.a, self.chi, self.pole = SECTORS[name]
        self.hbar = float(hbar)
        self.kappa = 0.5 + self.a
        self.C0 = math.log(self.q / math.pi) - EG

    def bose(self, x):
        return self.hbar / (-np.expm1(-2 * self.hbar * x))

    def logterm(self, y):
        """log(hbar) - log(1 - e^{-2 hbar y}), stable as hbar -> 0."""
        return -np.log(-np.expm1(-2 * self.hbar * np.asarray(y, dtype=float)) / self.hbar)

    def atoms(self, xmax):
        """Sorted log n and weights chi(n) Lambda(n)/sqrt(n) over prime powers n <= e^xmax with chi(n) != 0."""
        L, Wt = [], []
        for n, lam in rw.prime_powers(int(math.exp(xmax)) + 2):
            p = int(round(math.exp(lam)))
            k = round(math.log(n) / lam)
            c = self.chi(p) ** k
            if c != 0:
                L.append(math.log(n)); Wt.append(c * lam / math.sqrt(n))
        L, Wt = np.array(L), np.array(Wt)
        o = np.argsort(L)
        return L[o], Wt[o]

    def symbol(self, r):
        """Fourier symbol of the archimedean term: log(q/pi) + Re psi_hbar((1/2 + a + i r)/2)."""
        z = mp.mpc(self.kappa / 2, r / 2)
        return float(math.log(self.q / math.pi) + mp.re(mp.digamma(z / self.hbar)) + math.log(self.hbar))


# ------------------------------------------------------------------------------------------------ box kernel
def self_energy(h, S):
    T, Wt = GL[32]
    x = h / 2 * (T + 1); w = h / 2 * Wt
    integ = (np.exp(-2 * S.hbar * x) - np.exp(-S.kappa * x) * (1 - x / h)) * S.bose(x)
    return float(S.C0 + S.logterm(h) + 2 * np.sum(w * integ))


def arch_overlap(uo, h, S):
    c0 = 1 - uo / h
    b1, b2, b3 = np.minimum(uo, h - uo), np.maximum(uo, h - uo), uo + h
    T, Wt = GL[32]
    tot = np.zeros_like(uo)
    for lo, hi in ((np.zeros_like(uo), b1), (b1, b2), (b2, b3)):
        x = lo[:, None] + (hi - lo)[:, None] / 2 * (T[None, :] + 1)
        w = (hi - lo)[:, None] / 2 * Wt[None, :]
        gs = 0.5 * (np.clip(1 - np.abs(x - uo[:, None]) / h, 0, None) + np.clip(1 - np.abs(x + uo[:, None]) / h, 0, None))
        tot += np.sum(w * (np.exp(-2 * S.hbar * x) * c0[:, None] - np.exp(-S.kappa * x) * gs) * S.bose(x), axis=1)
    return S.C0 * c0 + c0 * S.logterm(b3) + 2 * tot


def arch_far(u, h, S):
    """-int e^{-kappa x} tri_h(x - u) B(x) dx for u >= h; 32 nodes per half-panel when u < 20h, else 8."""
    res = np.empty_like(u)
    near = u < 20 * h
    for mask, n in ((near, 32), (~near, 8)):
        if not mask.any():
            continue
        uu = u[mask]
        T, Wt = GL[n]
        tot = np.zeros_like(uu)
        for rising in (True, False):
            a = uu - h if rising else uu
            x = a[:, None] + h / 2 * (T[None, :] + 1)
            w = h / 2 * Wt[None, :]
            f = (x - (uu[:, None] - h)) / h if rising else ((uu[:, None] + h) - x) / h
            tot += np.sum(w * np.exp(-S.kappa * x) * f * S.bose(x), axis=1)
        res[mask] = -tot
    return res


def arch_kernel(u, h, S):
    u = np.array(u, dtype=float)
    u[np.abs(u - h) < 1e-9 * h] = h
    u[u < 1e-9 * h] = 0.0
    out_ = np.empty_like(u)
    z = u == 0
    out_[z] = self_energy(h, S)
    ov = (u > 0) & (u < h)
    if ov.any():
        out_[ov] = arch_overlap(u[ov], h, S)
    far = u >= h
    if far.any():
        out_[far] = arch_far(u[far], h, S)
    return out_


def prime_kernel(u, h, L, Wt):
    """-sum_n w_n [tri_h(log n - u) + tri_h(log n + u)] (the second term vanishes for h < log 2)."""
    u = np.asarray(u, dtype=float)
    res = np.zeros_like(u)
    if len(L) == 0:
        return res
    for sgn in (1.0, -1.0):
        c = sgn * u
        lo = np.searchsorted(L, c - h, side="right")
        hi = np.searchsorted(L, c + h, side="left")
        kmax = int(np.max(hi - lo)) if u.size else 0
        for k in range(kmax):
            idx = lo + k
            ok = idx < hi
            j = np.where(ok, idx, 0)
            res -= np.where(ok, Wt[j] * np.clip(1 - np.abs(L[j] - c) / h, 0, None), 0.0)
    return res


def box_moments(a, b):
    h = b - a
    kp = 2 * (np.exp(b / 2) - np.exp(a / 2)) / np.sqrt(h)
    km = 2 * (np.exp(-a / 2) - np.exp(-b / 2)) / np.sqrt(h)
    return kp, km


# ------------------------------------------------------------------------------------------------ assemblies
def grid_Z(ell, h, S, primes=True, only_sign=None):
    """Uniform box grid on [0, ell]: Z = Toeplitz(arch + primes); pole moments (Kp, Km) (zeta only)."""
    N = int(round(ell / h))
    ell_eff = N * h
    lags = h * np.arange(N)
    K = arch_kernel(lags, h, S)
    if primes:
        L, Wt = S.atoms(ell_eff + h)
        if only_sign is not None:
            sel = np.sign(Wt) == only_sign
            L, Wt = L[sel], Wt[sel]
        for x, c in zip(L, Wt):
            if x >= ell_eff:
                continue
            k = int(x // h); fr = x / h - k
            if k < N:
                K[k] -= c * (1 - fr)
            if k + 1 < N:
                K[k + 1] -= c * fr
    i = np.arange(N)
    Z = K[np.abs(i[:, None] - i[None, :])]
    x0 = h * i
    kp, km = box_moments(x0, x0 + h)
    if not S.pole:
        kp, km = np.zeros(N), np.zeros(N)
    return Z, kp, km


def points_Z(xs, h, S, prime_pairs=None, chunk=150000):
    """Equal-width boxes [x_i, x_i + h] at arbitrary non-overlapping positions; arch dense, primes given as sparse
    (i, j, value) triples (prime_pairs) since for these site sets an atom couples m to n m exactly."""
    xs = np.asarray(xs, dtype=float)
    n = len(xs)
    Z = np.empty((n, n))
    se = self_energy(h, S)
    for i0 in range(0, n, max(1, chunk // n)):
        i1 = min(n, i0 + max(1, chunk // n))
        U = np.abs(xs[i0:i1, None] - xs[None, :])
        flat = U.ravel()
        vals = np.full(flat.shape, se)
        nz = flat > 0
        vals[nz] = arch_far(flat[nz], h, S) if np.all(flat[nz] >= h * (1 - 1e-9)) else arch_kernel(flat[nz], h, S)
        Z[i0:i1] = vals.reshape(U.shape)
    if prime_pairs is not None:
        for i, j, v in prime_pairs:
            Z[i, j] += v
            Z[j, i] += v
    kp, km = box_moments(xs, xs + h)
    if not S.pole:
        kp, km = np.zeros(n), np.zeros(n)
    return Z, kp, km


def interval_Z(a, b, S, chunk=120000):
    """General non-overlapping boxes [a_i, b_i] (sorted): trapezoid cross-correlations."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    n = len(a)
    hw = b - a
    L, Wt = S.atoms(b[-1] - a[0] + 1e-9)
    C0 = np.concatenate([[0.0], np.cumsum(Wt)])
    C1 = np.concatenate([[0.0], np.cumsum(Wt * L)])
    Z = np.zeros((n, n))
    for i in range(n):
        Z[i, i] = self_energy(hw[i], S) - 2 * np.sum(Wt[L < hw[i]] * np.clip(1 - L[L < hw[i]] / hw[i], 0, None))
    iu, ju = np.triu_indices(n, 1)
    for s in range(0, len(iu), chunk):
        I, J = iu[s:s + chunk], ju[s:s + chunk]
        hi_, hj = hw[I], hw[J]
        sc = np.sqrt(hi_ * hj)
        x1 = a[J] - b[I]; m = np.minimum(hi_, hj); M = np.maximum(hi_, hj)
        x2, x3, x4 = x1 + m, x1 + M, x1 + hi_ + hj
        val = np.zeros(len(I))
        near = x1 < 20 * M
        for mask, nn in ((near, 16), (~near, 6)):
            if not mask.any():
                continue
            T, Wg = GL[nn]
            for lo, hi2, kind in ((x1, x2, 0), (x2, x3, 1), (x3, x4, 2)):
                lo_m, hi_m = lo[mask], hi2[mask]
                wdt = hi_m - lo_m
                x = lo_m[:, None] + wdt[:, None] / 2 * (T[None, :] + 1)
                w = wdt[:, None] / 2 * Wg[None, :]
                if kind == 0:
                    f = (x - x1[mask][:, None]) / sc[mask][:, None]
                elif kind == 1:
                    f = np.broadcast_to((m[mask] / sc[mask])[:, None], x.shape)
                else:
                    f = (x4[mask][:, None] - x) / sc[mask][:, None]
                val[mask] -= np.sum(w * np.exp(-S.kappa * x) * f * S.bose(np.maximum(x, 1e-300)), axis=1)
        # prime atoms: piecewise-linear trapezoid against prefix sums
        for lo, hi2, A0, B0 in ((x1, x2, -x1 / sc, 1 / sc), (x2, x3, m / sc, 0 * sc), (x3, x4, x4 / sc, -1 / sc)):
            s0 = np.searchsorted(L, lo, side="left"); s1 = np.searchsorted(L, hi2, side="left")
            val -= A0 * (C0[s1] - C0[s0]) + B0 * (C1[s1] - C1[s0])
        Z[I, J] = val
        Z[J, I] = val
    kp, km = box_moments(a, b)
    if not S.pole:
        kp, km = np.zeros(n), np.zeros(n)
    return Z, kp, km


# ------------------------------------------------------------------------------------------------ analysis
def pole_vectors(kp, km):
    na, nb = np.linalg.norm(kp), np.linalg.norm(km)
    if na == 0:
        return None, None, 0.0, 0.0
    A, B = kp / na, km / nb
    ab = A @ B
    lp, lm = na * nb * (ab + 1), na * nb * (ab - 1)
    v = math.sqrt(lp) * (A + B) / np.linalg.norm(A + B)
    w = math.sqrt(-lm) * (A - B) / np.linalg.norm(A - B)
    return v, w, lp, lm


def analyse(Z, kp, km, box_basis=True, big=False, solve=True, tol_rel=1e-11):
    n = Z.shape[0]
    v, w, lp, lm = pole_vectors(kp, km)
    res = {"n": n}
    if not big:
        ez, Uz = np.linalg.eigh(Z)
        ew = np.linalg.eigvalsh(Z + np.outer(kp, km) + np.outer(km, kp)) if v is not None else ez
    else:
        # dense subset solver (Lanczos stalls on the near-zero cluster); Z is consumed (turned into W) at the end
        ez, Uz = sla.eigh(Z, subset_by_index=[0, 3], driver="evr", check_finite=False)
        ew = None
    scale = max(abs(ez[0]), abs(ez[-1]), 1.0)
    tol = tol_rel * scale
    phi = Uz[:, 0] * (1 if Uz[:, 0].sum() >= 0 else -1)
    res.update({"Z_lowest": [float(e) for e in ez[:4]],
                "Z_n_neg": int((ez < -tol).sum()) if (not big or ez[-1] >= -tol) else ">=4",
                "pole_eigs": [float(lp), float(lm)]})
    if box_basis:
        res["Perron_vector_positive"] = bool(np.all(phi > 0))
    Y = None
    if v is not None and solve:
        if ez[0] < 0:
            mu = -ez[0]
            res["Perron_share (v.phi)^2/mu"] = float((v @ phi) ** 2 / mu)
            res["(w.phi)^2/mu"] = float((w @ phi) ** 2 / mu)
        if big:
            lu = sla.lu_factor(Z.copy(), overwrite_a=True, check_finite=False)
            Y = sla.lu_solve(lu, np.column_stack([v, w]))
            del lu; gc.collect()
        else:
            Y = np.linalg.solve(Z, np.column_stack([v, w]))
    if big:
        if v is not None:
            Z += np.outer(kp, km); Z += np.outer(km, kp)
        ew = sla.eigh(Z, subset_by_index=[0, 2], eigvals_only=True, driver="evr", overwrite_a=True, check_finite=False)
    res.update({"W_lowest": [float(e) for e in ew[:3]], "W_n_neg": int((ew < -tol).sum())})
    if Y is not None:
        U = np.column_stack([v, w])
        S2 = np.diag([-1.0, 1.0]) - U.T @ Y
        es2 = np.linalg.eigvalsh(0.5 * (S2 + S2.T))
        eps = float(-1 - v @ Y[:, 0])
        res["secular"] = {"eps=-1-vZ^-1v": eps, "odd_margin=1-wZ^-1w": float(1 - w @ Y[:, 1]),
                          "vZ^-1w": float(v @ Y[:, 1]), "S2_eigs": [float(es2[0]), float(es2[1])],
                          "n_neg_W_predicted": int((ez < -tol).sum() + (es2 < 0).sum() - 1)
                          if (not big or ez[-1] >= -tol) else None}
        if ez[0] < 0:
            res["secular"]["perron_gain=(share-1)"] = res["Perron_share (v.phi)^2/mu"] - 1
            res["secular"]["leakage=perron_gain-eps"] = res["Perron_share (v.phi)^2/mu"] - 1 - eps
    return res


# ------------------------------------------------------------------------------------------------ A
def part_A():
    # (1) reproduce round 32 (zeta, hbar = 1)
    import r32_quotient as rq
    S = Sector("zeta")
    us = np.concatenate([[0.0], np.array([0.3, 0.5, 0.9]) * 0.01, 0.01 * np.arange(1, 400) * 1.0])
    a33 = arch_kernel(us, 0.01, S)
    a32, _, _ = rq.kernel(us, 0.01, np.array([]), np.array([]))
    chk = {"max|arch33 - arch32| (h=0.01, u in [0,4])": float(np.max(np.abs(a33 - a32)))}
    Zg, kp, km = grid_Z(3.0, 0.03, S)
    Wg = rw.grid_W(3.0, 0.03)
    chk["max|grid W33 - grid W31| (ell=3,h=0.03)"] = float(np.max(np.abs(Zg + np.outer(kp, km) + np.outer(km, kp) - Wg)))
    # general-interval assembly on a uniform grid must equal the Toeplitz assembly
    xs = 0.05 * np.arange(40)
    Zi, kpi, kmi = interval_Z(xs, xs + 0.05, S)
    Zt, kpt, kmt = grid_Z(2.0, 0.05, S)
    chk["max|interval_Z - grid_Z| (ell=2, h=0.05)"] = float(np.max(np.abs(Zi - Zt)))
    # unequal widths: a box of width 2h equals the normalised sum of two width-h boxes
    S1 = Sector("zeta")
    Za, _, _ = interval_Z(np.array([0.0, 0.2, 0.3]), np.array([0.1, 0.3, 0.5]), S1)
    Zb, _, _ = interval_Z(np.array([0.0, 0.2, 0.3, 0.4]), np.array([0.1, 0.3, 0.4, 0.5]), S1)
    Bm = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1 / math.sqrt(2), 1 / math.sqrt(2)]])
    chk["max|unequal-width trapezoid - subbox sum|"] = float(np.max(np.abs(Za - Bm @ Zb @ Bm.T)))
    # hbar: hbar = 1 identity, hbar -> 0 limit kernel 1/(2x)
    S0 = Sector("zeta", hbar=1e-9)
    u = np.array([0.05, 0.3, 1.0, 3.0])
    T, Wt = GL[32]
    lim = []
    for uu in u:
        tot = 0.0
        for lo, rising in ((uu - 0.01, True), (uu, False)):
            x = lo + 0.01 / 2 * (T + 1); w = 0.01 / 2 * Wt
            f = (x - (uu - 0.01)) / 0.01 if rising else ((uu + 0.01) - x) / 0.01
            tot += np.sum(w * np.exp(-x / 2) * f / (2 * x))
        lim.append(-tot)
    chk["hbar->0 kernel vs -int e^{-x/2} tri/(2x)"] = float(np.max(np.abs(arch_far(u, 0.01, S0) - np.array(lim))))
    chk["self_energy(h=0.01): hbar=1, 0.5, 1e-9"] = [self_energy(0.01, Sector("zeta", hb)) for hb in (1.0, 0.5, 1e-9)]
    out["A_checks"] = chk
    log("A checks:", chk)
    save()
    # (2) chi-sector archimedean term vs zeros of L(s, chi) (Gaussian test functions)
    mp.mp.dps = 20
    val = {}
    for name in ("chi_4", "chi_3", "chi_5"):
        S = Sector(name)
        q, a = S.q, S.a
        chi_list = [0] * q
        for k in range(1, q):
            if math.gcd(k, q) == 1:
                vv = 1
                kk = k
                while kk > 1:
                    p = rw.smallest_prime(kk)
                    vv *= S.chi(p); kk //= p
                chi_list[k] = vv
        theta = lambda t: t / 2 * mp.log(mp.mpf(q) / mp.pi) + mp.im(mp.loggamma((mp.mpf(0.5) + a + 1j * t) / 2))
        Zf = lambda t: mp.re(mp.exp(1j * theta(t)) * mp.dirichlet(mp.mpc(0.5, t), chi_list))
        ts = np.arange(0.02, 42.0, 0.04)
        zs = [float(Zf(t)) for t in ts]
        zeros = []
        for k in range(len(ts) - 1):
            if zs[k] == 0 or zs[k] * zs[k + 1] < 0:
                zeros.append(float(mp.findroot(Zf, (ts[k], ts[k + 1]), solver="anderson")))
        Tmax = ts[-1]
        nvm = Tmax / math.pi * math.log(q * Tmax / (2 * math.pi * math.e)) / 2
        rows = []
        for sig in (0.3, 0.45, 0.6):
            g = lambda x: math.exp(-x * x / (4 * sig * sig))
            ghat = lambda r: 2 * sig * math.sqrt(math.pi) * math.exp(-sig * sig * r * r)
            arch = (math.log(q / math.pi) - EG) + 2 * mp.quad(lambda x: (mp.exp(-2 * x) - mp.exp(-(0.5 + a) * x) * g(x)) / (1 - mp.exp(-2 * x)), [0, 0.5, 2, 8, 40])
            pr = 0.0
            for n, lam in rw.prime_powers(int(math.exp(10 * sig)) + 3):
                p = rw.smallest_prime(n); kk = round(math.log(n) / math.log(p))
                pr += 2 * (S.chi(p) ** kk) * lam / math.sqrt(n) * g(math.log(n))
            prime_side = float(arch) - pr
            zero_side = 2 * sum(ghat(gm) for gm in zeros)
            rows.append({"sigma": sig, "prime_side": prime_side, "zero_side(2*sum_{0<gamma<42})": zero_side,
                         "diff": prime_side - zero_side})
        val[name] = {"n_zeros_found(0,42)": len(zeros), "N(T)/2 main term": nvm, "first_zeros": zeros[:4], "checks": rows}
        log("A chi:", name, val[name])
    out["A_chi_validation"] = val
    save()


# ------------------------------------------------------------------------------------------------ B
def legendre_mp(ell, N, dps):
    """Z = W - pole on the orthonormal Legendre basis of [-ell/2, ell/2], in multiprecision."""
    Wa, kpa, kma = rw.assemble_hp_legendre(ell / 2, N, dps=dps)
    mp.mp.dps = dps
    W = rw.arb_to_mp(Wa, dps)
    kp = mp.matrix(rw.arbvec_to_mp(kpa, dps)); km = mp.matrix(rw.arbvec_to_mp(kma, dps))
    P = kp * km.T + km * kp.T
    Z = W - P
    ez, Q = mp.eigsy(Z)
    ez = [ez[i] for i in range(N)]
    o = sorted(range(N), key=lambda i: ez[i])
    ew = sorted(mp.eigsy(W, eigvals_only=True))
    na, nb = mp.norm(kp), mp.norm(km)
    A, B = kp / na, km / nb
    ab = (A.T * B)[0]
    lp, lm = na * nb * (ab + 1), na * nb * (ab - 1)
    v = mp.sqrt(lp) * (A + B) / mp.norm(A + B)
    w = mp.sqrt(-lm) * (A - B) / mp.norm(A - B)
    yv, yw = mp.lu_solve(Z, v), mp.lu_solve(Z, w)
    phi = mp.matrix([Q[i, o[0]] for i in range(N)])
    mu = -ez[o[0]]
    share = (v.T * phi)[0] ** 2 / mu if mu > 0 else None
    eps = -1 - (v.T * yv)[0]
    return {"ell": ell, "N": N, "dps": dps, "Z_lowest": [mp.nstr(ez[i], 8) for i in o[:4]],
            "Z_n_neg": sum(1 for e in ez if e < 0), "W_lowest": [mp.nstr(e, 8) for e in ew[:2]],
            "W_n_neg": sum(1 for e in ew if e < 0), "pole_eigs": [mp.nstr(lp, 8), mp.nstr(lm, 8)],
            "Perron_share": mp.nstr(share, 12) if share is not None else None,
            "eps=-1-vZ^-1v": mp.nstr(eps, 8), "odd_margin": mp.nstr(1 - (w.T * yw)[0], 8),
            "vZ^-1w": mp.nstr((v.T * yw)[0], 6)}


def part_B(which=("grid", "onset", "lattice", "primes", "gaps", "legendre")):
    S = Sector("zeta")
    res = out.setdefault("B_one_mode", {})
    if "grid" in which:
        rows = []
        for X in (10, 100, 1000, 10 ** 4, 10 ** 5):
            ell = math.log(X)
            for h in (0.02, 0.01, 0.005):
                if ell / h > 2400:
                    continue
                t0 = time.time()
                Z, kp, km = grid_Z(ell, h, S)
                r = analyse(Z, kp, km)
                r.update({"X": X, "ell": ell, "h": h, "secs": round(time.time() - t0, 1)})
                rows.append(r)
                log("B grid:", r)
                res["box_grid"] = rows
                save()
    if "onset" in which:
        rows = []
        for ell in (0.1, 0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, math.log(2), 0.8, 1.0, 1.5):
            for N in (100, 400):
                h = ell / N
                Z, kp, km = grid_Z(ell, h, S)
                Zn, kpn, kmn = grid_Z(ell, h, S, primes=False)
                ez = np.linalg.eigvalsh(Z); ezn = np.linalg.eigvalsh(Zn)
                Th = Zn + np.outer(kpn, kmn) + np.outer(kmn, kpn)
                rows.append({"ell": ell, "N": N, "Z_lowest": [float(ez[0]), float(ez[1])], "Z_n_neg": int((ez < 0).sum()),
                             "arch_only_n_neg": int((ezn < 0).sum()), "Theta_lambda_min": float(np.linalg.eigvalsh(Th)[0])})
                log("B onset:", rows[-1])
        res["onset"] = rows
        save()
    if "lattice" in which:
        rows = []
        for X in (1000, 10 ** 4):
            t0 = time.time()
            h = 0.45 / X
            ms = np.arange(1, X + 1)
            xs = np.log(ms.astype(float))
            pairs = []
            for n, lam in rw.prime_powers(X):
                c = -lam / math.sqrt(n)
                for m in range(1, X // n + 1):
                    pairs.append((m - 1, n * m - 1, c))
            Z, kp, km = points_Z(xs, h, S, prime_pairs=pairs)
            r = analyse(Z, kp, km, big=X > 3000)
            del Z; gc.collect()
            r.update({"X": X, "h": h, "n_prime_entries": len(pairs), "secs": round(time.time() - t0, 1)})
            rows.append(r)
            log("B lattice:", r)
            res["integer_lattice"] = rows
            save()
    if "primes" in which:
        rows = []
        for X, h in ((1000, 1e-4), (10 ** 4, 5e-5), (10 ** 5, 5e-6)):
            t0 = time.time()
            P = np.array(primes_upto(X), dtype=float)
            xs = np.log(P)
            assert h <= math.log1p(1.0 / X)
            Z, kp, km = points_Z(xs, h, S)
            r = analyse(Z, kp, km, big=len(P) > 3000)
            del Z; gc.collect()
            r.update({"X": X, "h": h, "n_sites": len(P), "D_h(0)": self_energy(h, S), "secs": round(time.time() - t0, 1)})
            rows.append(r)
            log("B prime sites:", r)
            res["prime_sites"] = rows
            save()
    if "gaps" in which:
        rows = []
        for X in (1000, 10 ** 4, 10 ** 5):
            t0 = time.time()
            P = primes_upto(X)
            br = np.log(np.array([1] + P, dtype=float))
            Z, kp, km = interval_Z(br[:-1], br[1:], S)
            r = analyse(Z, kp, km, big=len(br) > 3000)
            del Z; gc.collect()
            r.update({"X": X, "n_boxes": len(br) - 1, "tiling": "[0,log 2], [log p_k, log p_k+1]",
                      "secs": round(time.time() - t0, 1)})
            rows.append(r)
            log("B prime-gap tiling:", r)
            res["prime_gap_tiling"] = rows
            save()
    if "legendre" in which:
        rows = []
        for ell, N, dps in ((1.0, 24, 100), (2.0, 24, 100), (3.0, 24, 120), (4.0, 24, 120), (5.0, 24, 140),
                            (6.0, 24, 140), (math.log(1000), 24, 160), (3.0, 32, 160), (math.log(1000), 32, 200)):
            t0 = time.time()
            r = legendre_mp(ell, N, dps)
            r["secs"] = round(time.time() - t0, 1)
            rows.append(r)
            log("B legendre:", r)
            res["legendre_mp"] = rows
            save()


# ------------------------------------------------------------------------------------------------ C
def sos_fit_ext(fit, W, U, iters=6000, X0=None):
    """min ||W - A(X) - U C U^T||, X >= 0, C >= 0 (FISTA, two PSD blocks)."""
    from r31_sos import psd_proj
    Lx = fit.lipschitz()
    UtU = U.T @ U
    Lc = 2 * np.linalg.norm(UtU, 2) ** 2
    step = 1.0 / (Lx + Lc)
    r = U.shape[1]
    X = np.zeros((fit.m, fit.m)) if X0 is None else X0.copy()
    C = np.zeros((r, r))
    Yx, Yc, t = X.copy(), C.copy(), 1.0
    for _ in range(iters):
        R = fit.A(Yx) + U @ Yc @ U.T - W
        Gx = 2 * fit.At(R); Gx = 0.5 * (Gx + Gx.T)
        Gc = 2 * U.T @ R @ U; Gc = 0.5 * (Gc + Gc.T)
        Xn, Cn = psd_proj(Yx - step * Gx), psd_proj(Yc - step * Gc)
        tn = 0.5 * (1 + math.sqrt(1 + 4 * t * t))
        Yx = Xn + (t - 1) / tn * (Xn - X); Yc = Cn + (t - 1) / tn * (Cn - C)
        X, C, t = Xn, Cn, tn
    R = fit.A(X) + U @ C @ U.T - W
    return X, C, float(np.linalg.norm(R) / np.linalg.norm(W)), R


def ladder_ext(W, D_list, Ms, U, seeds=6, x0=None):
    """Q1 = sum alpha_k D_k + sum_n (a_n M_n + b_n M_n^T);  W ~ Q1^T Q1 + U L L^T U^T (L lower triangular)."""
    from scipy.optimize import least_squares
    N = W.shape[0]
    K, Sn, r = len(D_list), len(Ms), U.shape[1]
    Dl, Ml = np.array(D_list), np.array(Ms)
    MlT = np.transpose(Ml, (0, 2, 1))
    tri = np.tril_indices(r)

    def unpack(p):
        al, a, b = p[:K], p[K:K + Sn], p[K + Sn:K + 2 * Sn]
        Lm = np.zeros((r, r)); Lm[tri] = p[K + 2 * Sn:]
        return al, a, b, Lm

    def res(p):
        al, a, b, Lm = unpack(p)
        Q = np.tensordot(al, Dl, 1) + np.tensordot(a, Ml, 1) + np.tensordot(b, MlT, 1)
        UL = U @ Lm
        return (Q.T @ Q + UL @ UL.T - W).ravel()
    npar = K + 2 * Sn + len(tri[0])
    g = np.random.default_rng(0)
    starts = ([x0] if x0 is not None else []) + [g.standard_normal(npar) * 0.5 for _ in range(seeds)]
    best = None
    for s in starts:
        rr = least_squares(res, s, method="lm", max_nfev=8000)
        rel = float(np.linalg.norm(rr.fun) / np.linalg.norm(W))
        if best is None or rel < best[0]:
            best = (rel, rr.x)
    return best


def part_C():
    import r31_sos as rs
    rows = []
    for ell in (1.5, 3.0, 4.0):
        for N in (24, 32):
            t0 = time.time()
            R, Bs, ns, (wT, VT) = rs.setup(ell, N)
            W = R["W"]
            Z = W - R["pole"]
            ez, Uz = np.linalg.eigh(Z)
            phi = Uz[:, 0]
            v, w, lp, lm = pole_vectors(R["kp"], R["km"])
            ew, Uw = np.linalg.eigh(W)
            nv = lambda x: x / np.linalg.norm(x)
            chans = {"pole_pair(v,w)": np.column_stack([nv(v), nv(w)]),
                     "pole+Perron(v,phi)": np.column_stack([nv(v), nv(phi)]),
                     "pole+Perron(v,w,phi)": np.column_stack([nv(v), nv(w), nv(phi)]),
                     "control_random3": np.linalg.qr(np.random.default_rng(1).standard_normal((N, 3)))[0],
                     "control_W_low3": Uw[:, :3], "control_W_top3": Uw[:, -3:]}
            fit = rs.SOSFit(Bs)
            X0, r0 = fit.fit(W, iters=6000)
            R0 = fit.A(X0) - W
            row = {"ell": ell, "N": N, "sos_baseline": r0}
            for name, U in chans.items():
                P = U @ np.linalg.pinv(U)
                row["sos_baseline_residual_fraction_in_span(" + name + ")"] = float(np.linalg.norm(P @ R0 @ P) / np.linalg.norm(R0))
                _, C, rr, _ = sos_fit_ext(fit, W, U, iters=6000, X0=X0)
                row["sos+" + name] = rr
                row["sos+" + name + "_C_trace"] = float(np.trace(C))
            # single-channel ladder (round 31 'arch_D_ladder') and with the pole/Perron second channel
            Ms = [R["M"][n] for n in ns]
            base = rs.fit_ladder(W, Bs[:3], Ms, seeds=6)
            row["ladder_baseline(arch D + ladder)"] = base[0]
            for name in ("pole_pair(v,w)", "pole+Perron(v,phi)", "pole+Perron(v,w,phi)", "control_random3", "control_W_low3"):
                U = chans[name]
                x0 = np.concatenate([base[1], np.zeros(len(np.tril_indices(U.shape[1])[0]))])
                row["ladder+" + name] = ladder_ext(W, Bs[:3], Ms, U, seeds=3, x0=x0)[0]
            # the secular 2x2 data in this basis (double precision)
            low = ew < 1e-3 * ew[-1]
            row.update({"W_lambda_min(double)": float(ew[0]), "n_low_W(<1e-3 lmax)": int(low.sum()),
                        "phi_in_low_W_space": float(np.linalg.norm(Uw[:, low].T @ phi)),
                        "v_in_low_W_space/|v|": float(np.linalg.norm(Uw[:, low].T @ v) / np.linalg.norm(v)),
                        "phi^T W phi": float(phi @ W @ phi), "Z_n_neg": int((ez < -1e-9).sum()),
                        "secs": round(time.time() - t0, 1)})
            rows.append(row)
            log("C:", row)
            out["C_second_channel"] = rows
            save()


# ------------------------------------------------------------------------------------------------ D
def part_D():
    res = {}
    for name in ("zeta", "chi_4", "chi_3", "chi_5", "chi_-163"):
        S = Sector(name)
        sym0 = S.symbol(0.0)
        r0 = None
        if sym0 < 0:
            lo, hi = 0.0, 1.0
            while S.symbol(hi) < 0:
                hi *= 2
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if S.symbol(mid) < 0 else (lo, mid)
            r0 = 0.5 * (lo + hi)
        q_threshold = math.pi * math.exp(-float(mp.digamma((0.5 + S.a) / 2)))
        entry = {"q": S.q, "a": S.a, "symbol_at_0=log(q/pi)+psi((1/2+a)/2)": sym0, "symbol_root_r0": r0,
                 "arch_PSD_iff_q>=pi*exp(-psi((1/2+a)/2))": q_threshold,
                 "self_energy(h=1e-3)": self_energy(1e-3, S),
                 "chi(p) for p<=41": {p: S.chi(p) for p in primes_upto(41)}}
        # J_pq(chi) on prime sites: closed form r^{3/2-a}/(r^2-1)
        if name != "zeta":
            P = np.array(primes_upto(1000), dtype=float)
            h = 1e-4
            xs = np.log(P)
            iu = np.triu_indices(len(P), 1)
            U = xs[iu[1]] - xs[iu[0]]
            J = -arch_far(U, h, S)
            rr = np.exp(U)
            lim = h * rr ** (1.5 - S.a) / (rr ** 2 - 1)
            entry["prime_sites_X1000"] = {"frac_ferro": float(np.mean(J > 0)), "max_rel_dev_from_closed_form":
                                          float(np.max(np.abs(J - lim) / np.abs(lim))), "J_23/h": float(J[0] / h),
                                          "closed_form_23": float(1.5 ** (1.5 - S.a) / (1.5 ** 2 - 1))}
        grids = []
        for ell in (1.0, 2.0, 3.0, 4.0, 6.0):
            h = 0.01 if ell <= 4 else 0.02
            Zf, kp, km = grid_Z(ell, h, S)
            Za, _, _ = grid_Z(ell, h, S, primes=False)
            Zp, _, _ = grid_Z(ell, h, S, only_sign=1.0)
            Am = Zf - Zp
            g = {"ell": ell, "h": h, "arch_n_neg": int((np.linalg.eigvalsh(Za) < 0).sum()),
                 "ferro(arch+chi=+1 atoms)_n_neg": int((np.linalg.eigvalsh(Zp) < 0).sum()),
                 "antiferro_atoms(chi=-1)_n_pos": int((np.linalg.eigvalsh(Am) > 1e-12).sum()) if name != "zeta" else None,
                 "ferro_offdiag_max(<=0)": float(np.max(Zp - np.diag(np.diag(Zp)))),
                 "full_Z_n_neg": int((np.linalg.eigvalsh(Zf) < 0).sum())}
            if name == "zeta":
                Wf = Zf + np.outer(kp, km) + np.outer(km, kp)
                ew = np.linalg.eigvalsh(Wf)
            else:
                ew = np.linalg.eigvalsh(Zf)
            g["W_lambda_min"] = float(ew[0]); g["W_n_neg"] = int((ew < -1e-11 * abs(ew[-1])).sum())
            grids.append(g)
            log("D:", name, g)
        entry["grids"] = grids
        res[name] = entry
        out["D_dirichlet"] = res
        save()


# ------------------------------------------------------------------------------------------------ E
def part_E():
    res = {}
    mp.mp.dps = 40
    beta = []
    for a, b in ((1.0, 1.0), (1.0, 2.0), (0.3, 1.7)):
        lim = a * math.log(a / (a + b)) + b * math.log(b / (a + b))
        for h in (0.1, 0.01, 0.001, 1e-4):
            val = float(h * (mp.loggamma(a / h) + mp.loggamma(b / h) - mp.loggamma((a + b) / h)))
            nxt = 0.5 * h * math.log(2 * math.pi * h * (a + b) / (a * b))
            beta.append({"a": a, "b": b, "h": h, "h*logB(a/h,b/h)": val, "limit": lim, "diff": val - lim,
                         "Stirling next term (h/2)log(2 pi h (a+b)/(ab))": nxt})
    res["beta_limit"] = beta
    log("E beta:", beta[-1])
    # symbol difference Omega_hbar - Omega_1 (zeta)
    sym = {}
    for hb in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99, 1.01, 1.1, 1.5, 2.0):
        Sh, S1 = Sector("zeta", max(hb, 1e-9)), Sector("zeta")
        sym[str(hb)] = {f"r={r}": Sh.symbol(r) - S1.symbol(r) for r in (0.0, 5.0, 14.13, 50.0, 300.0, 3000.0)}
    res["symbol_difference"] = sym
    log("E symbol diff:", sym)
    # hbar sweep on box grids
    sweep = []
    for ell, h in ((1.0, 0.01), (2.0, 0.01), (3.0, 0.01), (4.0, 0.01), (3.0, 0.005)):
        for hb in (1e-9, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0, 1.01, 1.05, 1.1, 1.5, 2.0):
            S = Sector("zeta", hbar=hb)
            Z, kp, km = grid_Z(ell, h, S)
            r = analyse(Z, kp, km)
            sweep.append({"ell": ell, "h": h, "hbar": hb, "W_lambda_min": r["W_lowest"][0], "W_n_neg": r["W_n_neg"],
                          "Z_n_neg": r["Z_n_neg"], "Z_lambda_min": r["Z_lowest"][0],
                          "eps": r["secular"]["eps=-1-vZ^-1v"], "Perron_share": r.get("Perron_share (v.phi)^2/mu")})
            log("E sweep:", sweep[-1])
        res["hbar_sweep"] = sweep
        out["E_maslov"] = res
        save()
    # the positivity window in hbar around 1 is computed in part F (2)
    res.pop("hbar_critical", None)
    # width scaling is a rescaling: W restricted to stretched test functions equals W on the longer support
    res["width_scaling_note"] = "k(x) -> lambda^{-1/2} k(x/lambda) maps L2[0,ell] onto L2[0,lambda ell]; the margin then follows the X-dependence of part B/C"
    out["E_maslov"] = res
    save()


# ------------------------------------------------------------------------------------------------ F
def part_F():
    from scipy.optimize import brentq
    res = {}
    S = Sector("zeta")
    # (1) single-box witness: arch(1_[0,l]/sqrt l) = self_energy(l) < 0 for l > l1; onset l0 of n_-(Z) on grids
    l1 = brentq(lambda l: self_energy(l, S), 0.05, 0.6, xtol=1e-14)
    on = {}
    for N in (200, 400, 800):
        lo_, hi_ = 0.1, 0.3
        f = lambda l: np.linalg.eigvalsh(grid_Z(l, l / N, S)[0])[0]
        for _ in range(45):
            mid = 0.5 * (lo_ + hi_)
            lo_, hi_ = (mid, hi_) if f(mid) > 0 else (lo_, mid)
        on[str(N)] = 0.5 * (lo_ + hi_)
    res["onset"] = {"l1(single box: self_energy(l1)=0)": l1, "self_energy(log 2)": self_energy(math.log(2), S),
                    "l0(lambda_min(Z_l)=0 on grid of N boxes)": on}
    log("F onset:", res["onset"])
    # (2) positivity window in hbar around 1
    win = []
    for ell, h in ((1.0, 0.01), (2.0, 0.01), (3.0, 0.01), (4.0, 0.01), (6.0, 0.01), (3.0, 0.005)):
        def lmin(hb):
            Z, kp, km = grid_Z(ell, h, Sector("zeta", hbar=hb))
            return np.linalg.eigvalsh(Z + np.outer(kp, km) + np.outer(km, kp))[0]
        l1v = lmin(1.0)
        up, dn = 1e-7, 1e-7
        while lmin(1 + up) > 0 and up < 1:
            up *= 2
        lo_, hi_ = 1 + up / 2 if up > 1e-7 else 1.0, 1 + up
        for _ in range(50):
            mid = 0.5 * (lo_ + hi_)
            lo_, hi_ = (mid, hi_) if lmin(mid) > 0 else (lo_, mid)
        hplus = 0.5 * (lo_ + hi_)
        scan = [(hb, float(lmin(hb))) for hb in np.round(np.arange(0.5, 1.0, 0.05), 3)]
        while lmin(1 - dn) > 0 and dn < 0.5:
            dn *= 2
        if dn >= 0.5 and lmin(1 - dn) > 0:
            hminus = None
        else:
            lo_, hi_ = 1 - dn, (1 - dn / 2 if dn > 1e-7 else 1.0)
            for _ in range(50):
                mid = 0.5 * (lo_ + hi_)
                lo_, hi_ = (lo_, mid) if lmin(mid) > 0 else (mid, hi_)
            hminus = 0.5 * (lo_ + hi_)
        win.append({"ell": ell, "h": h, "lambda_min(W_1)": float(l1v), "hbar_plus": hplus, "hbar_minus": hminus,
                    "lambda_min scan hbar in [0.5,1)": scan})
        log("F window:", win[-1])
    res["hbar_window"] = win
    # (3) symbol inequality Omega_hbar >= Omega_1 for hbar <= 1/2; exact hbar = 1/2 identity; Polya-type data
    rs = np.concatenate([[0.0], np.logspace(-3, 3.5, 300)])
    ineq = {}
    S1 = Sector("zeta")
    o1 = np.array([S1.symbol(r) for r in rs])
    for hb in (1e-9, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.75, 0.9):
        Sh = Sector("zeta", hb)
        d = np.array([Sh.symbol(r) for r in rs]) - o1
        ineq[str(hb)] = {"min_diff": float(d.min()), "argmin_r": float(rs[int(np.argmin(d))]),
                         "diff_at_r=1000*y^2(y=r/2)": float(d[np.argmin(np.abs(rs - 1000))] * (rs[np.argmin(np.abs(rs - 1000))] / 2) ** 2),
                         "predicted (1-hb)[1/8-(1+hb)/12]": (1 - hb) * (1 / 8 - (1 + hb) / 12)}
    half = max(abs(Sector("zeta", 0.5).symbol(r) - S1.symbol(r) - (math.pi / 2) / math.cosh(math.pi * r)) for r in rs if r < 30)
    om = lambda t: 1 / (-np.expm1(-t)) - 1 / t
    t = np.linspace(1e-3, 60, 60000)
    polya = {}
    for hb in (1e-9, 0.1, 0.25, 0.5, 0.75):
        F = (om(t) - hb * om(hb * t)) * np.exp(-t / 4)
        d1, d2 = np.gradient(F, t), np.gradient(np.gradient(F, t), t)
        polya[str(hb)] = {"F>=0": bool(F.min() >= 0), "F decreasing": bool(d1.max() <= 1e-12), "F convex": bool(d2[5:-5].min() >= -1e-9),
                          "max F'": float(d1.max()), "min F''": float(d2[5:-5].min())}
    res["symbol_inequality"] = {"min over r of Omega_hbar - Omega_1": ineq, "max|Omega_1/2 - Omega_1 - (pi/2)/cosh(pi r)| (r<30)": half,
                                "Polya data for F_hbar(t) = [w(t) - hbar w(hbar t)] e^{-t/4}, w(t) = 1/(1-e^-t) - 1/t": polya}
    log("F symbol:", res["symbol_inequality"])
    # (4) chi sectors: does the antiferromagnetic part act as an effective (rank-2) pole?
    eff = []
    for name in ("chi_4", "chi_3", "chi_5", "chi_-163"):
        Sx = Sector(name)
        for ell, h in ((3.0, 0.01), (4.0, 0.01), (6.0, 0.02)):
            Zf, _, _ = grid_Z(ell, h, Sx)
            Zp, _, _ = grid_Z(ell, h, Sx, only_sign=1.0)
            Am = Zf - Zp
            N = Zf.shape[0]
            x0 = h * np.arange(N)
            kp, km = box_moments(x0, x0 + h)
            Q, _ = np.linalg.qr(np.column_stack([kp, km]))
            Pi = Q @ Q.T
            A2 = Pi @ Am @ Pi
            ezp, Uzp = np.linalg.eigh(Zp)
            e_eff = np.linalg.eigvalsh(Zp + A2)
            M2 = Q.T @ Am @ Q
            pole_half = Q.T @ (0.5 * (np.outer(kp, km) + np.outer(km, kp))) @ Q
            phi = Uzp[:, 0]
            eff.append({"chi": name, "ell": ell, "h": h, "ferro_n_neg": int((ezp < 0).sum()), "ferro_lambda_min": float(ezp[0]),
                        "Z+ + Pi A- Pi: lambda_min": float(e_eff[0]), "Z+ + Pi A- Pi: n_neg": int((e_eff < 0).sum()),
                        "eig(A- in pole frame)": [float(x) for x in np.linalg.eigvalsh(M2)],
                        "eig(half zeta pole in same frame)": [float(x) for x in np.linalg.eigvalsh(pole_half)],
                        "phi^T A- phi / mu": float(phi @ Am @ phi / -ezp[0]) if ezp[0] < 0 else None,
                        "full W_chi lambda_min": float(np.linalg.eigvalsh(Zf)[0])})
            log("F chi:", eff[-1])
    res["chi_effective_pole"] = eff
    out["F_supplements"] = res
    save()


# ------------------------------------------------------------------------------------------------ G
def part_G():
    """The pole/Perron pair as a literal 2x2 block: W restricted to span{v, phi}; the Perron mode's W-energy."""
    S = Sector("zeta")
    rows = []
    for X in (10, 100, 1000, 10 ** 4, 10 ** 5):
        for h in (0.01, 0.005):
            Z, kp, km = grid_Z(math.log(X), h, S)
            v, w, lp, lm = pole_vectors(kp, km)
            W = Z + np.outer(kp, km) + np.outer(km, kp)
            ez, Uz = np.linalg.eigh(Z)
            phi = Uz[:, 0] * np.sign(Uz[:, 0].sum())
            mu = -ez[0]
            vh = v / np.linalg.norm(v)
            B = np.array([[vh @ W @ vh, vh @ W @ phi], [phi @ W @ vh, phi @ W @ phi]])
            G = np.array([[1, vh @ phi], [vh @ phi, 1]])
            eb = np.sort(np.real(sla.eigvals(B, G)))
            rows.append({"X": X, "h": h, "mu": float(mu), "cos(v,phi)": float(vh @ phi), "phi^T W phi": float(phi @ W @ phi),
                         "(v.phi)^2 - mu": float((v @ phi) ** 2 - mu), "(w.phi)^2": float((w @ phi) ** 2),
                         "v^T W v/|v|^2": float(vh @ W @ vh), "2x2 block eigs (generalised, span{v,phi})": [float(x) for x in eb],
                         "lambda_min(W)": float(np.linalg.eigvalsh(W)[0])})
            log("G:", rows[-1])
    out["G_pole_perron_block"] = rows
    save()


# ------------------------------------------------------------------------------------------------ H
def part_H():
    """Why a PSD second channel on span U cannot lower the SOS plateau: the sign of the deficit W - A(X0) on span U."""
    import r31_sos as rs
    rows = []
    for ell in (1.5, 3.0, 4.0):
        for N in (24, 32):
            R, Bs, ns, _ = rs.setup(ell, N)
            W = R["W"]
            ez, Uz = np.linalg.eigh(W - R["pole"])
            v, w, _, _ = pole_vectors(R["kp"], R["km"])
            nv = lambda x: x / np.linalg.norm(x)
            fit = rs.SOSFit(Bs)
            X0, r0 = fit.fit(W, iters=6000)
            D = W - fit.A(X0)
            ew, Uw = np.linalg.eigh(W)
            row = {"ell": ell, "N": N, "sos_rel_residual": r0, "|D|": float(np.linalg.norm(D))}
            for name, U in (("v,w", np.column_stack([nv(v), nv(w)])), ("v,phi", np.column_stack([nv(v), nv(Uz[:, 0])])),
                            ("v,w,phi", np.column_stack([nv(v), nv(w), nv(Uz[:, 0])]))):
                Q, _ = np.linalg.qr(U)
                M = Q.T @ D @ Q
                em = np.linalg.eigvalsh(M)
                row["eig(U^T (W - fit) U) on " + name] = [float(x) for x in em]
                row["PSD-correctable part |[.]_+| / |D| on " + name] = float(np.linalg.norm(np.clip(em, 0, None)) / np.linalg.norm(D))
            dlow = Uw[:, :5].T @ D @ Uw[:, :5]
            row["eig of deficit on W's 5 lowest eigvecs"] = [float(x) for x in np.linalg.eigvalsh(dlow)]
            row["|D on W's 10 lowest| / |D|"] = float(np.linalg.norm(Uw[:, :10].T @ D @ Uw[:, :10]) / np.linalg.norm(D))
            rows.append(row)
            log("H:", row)
    out["H_why_second_channel"] = rows
    save()


# ------------------------------------------------------------------------------------------------ I
def part_I():
    """Box-grid Z is a symmetric Toeplitz matrix; for its simple minimal eigenvalue (the Perron mode) the corollary of
    Caratheodory-Fejer quoted by Connes-van Suijlekom puts all zeros of sum_j phi_j z^j on the unit circle."""
    rows = []
    for ell, h in ((1.0, 0.02), (2.0, 0.02), (3.0, 0.03), (4.0, 0.04), (6.0, 0.06)):
        Z, _, _ = grid_Z(ell, h, Sector("zeta"))
        ez, Uz = np.linalg.eigh(Z)
        r = {"ell": ell, "h": h, "N": Z.shape[0], "lambda_1": float(ez[0]), "gap_lambda2-lambda1": float(ez[1] - ez[0])}
        for k, name in ((0, "Perron (lowest)"), (1, "second"), (2, "third")):
            z = np.roots(Uz[::-1, k])
            r[name + ": max||z|-1|"] = float(np.max(np.abs(np.abs(z) - 1)))
        rows.append(r)
        log("I:", r)
    out["I_caratheodory_fejer_check"] = rows
    save()


if __name__ == "__main__":
    args = [p for p in sys.argv[1:] if not p.startswith("--")]
    if os.path.exists(OUT):
        out.update(json.load(open(OUT)))
    for p in args or ["A", "B", "C", "D", "E"]:
        if p.startswith("B:"):
            part_B(tuple(p[2:].split(",")))
            continue
        log("=== part", p)
        globals()["part_" + p]()
    log("done")

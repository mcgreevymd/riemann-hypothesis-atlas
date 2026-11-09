"""Round 31: prime-side assembly of Weil's quadratic form on finite bases (no zeros are used anywhere here).

For real k supported in [-L, L] (log scale), g = k * k~ (its autocorrelation, an even function):
  W(k) = 2 K(1/2) K(-1/2)                                                            pole terms h(i/2) + h(-i/2)
       - (log pi + gamma) g(0) + 2 int_0^oo [e^{-2x} g(0) - e^{-x/2} g(x)] / (1 - e^{-2x}) dx      archimedean
       - 2 sum_n Lambda(n) n^{-1/2} g(log n)                                         primes, log n < 2L
with K(a) = int k(y) e^{a y} dy.  The archimedean line is the x-space form of (1/2pi) int ghat(r) 2 theta'(r) dr.
Under RH, W(k) = sum_gamma |khat(gamma)|^2 with khat(r) = int k(x) e^{irx} dx (the zero side; used only to validate).

Bases: orthonormal Legendre on [-L, L] (double precision and python-flint/Arb multiprecision), orthonormal Hermite
functions of width sigma (all primes contribute), and normalised box functions of mesh h on [0, ell] (Toeplitz + rank 2).
"""
import math
import numpy as np

EULER = 0.57721566490153286061
LOGPI = math.log(math.pi)


def prime_powers(xmax):
    """(n, Lambda(n)) for prime powers n <= xmax, sorted."""
    xmax = int(xmax)
    sieve = np.ones(xmax + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(xmax ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    out = []
    for p in np.flatnonzero(sieve):
        p = int(p)
        q = p
        while q <= xmax:
            out.append((q, math.log(p)))
            q *= p
    out.sort()
    return out


def smallest_prime(n):
    return next(q for q in range(2, n + 1) if n % q == 0)


# ----------------------------------------------------------------------------------------------- Legendre, double
def legendre_vals(t, N):
    t = np.asarray(t, dtype=float)
    P = np.zeros((N,) + t.shape)
    P[0] = 1.0
    if N > 1:
        P[1] = t
    for j in range(1, N - 1):
        P[j + 1] = ((2 * j + 1) * t * P[j] - j * P[j - 1]) / (j + 1)
    return P


class LegendreBasis:
    """Orthonormal e_j(x) = sqrt((2j+1)/(2L)) P_j(x/L) on [-L, L]."""

    def __init__(self, L, N):
        self.L, self.N = float(L), int(N)
        self.norm = np.sqrt((2 * np.arange(N) + 1) / (2 * L))

    def eval(self, x):
        x = np.asarray(x, dtype=float)
        inside = np.abs(x) <= self.L
        V = legendre_vals(np.clip(x / self.L, -1, 1), self.N) * self.norm.reshape((-1,) + (1,) * x.ndim)
        return V * inside

    def corr(self, xs):
        """g_ij(x) = int e_i(y) e_j(y - x) dy = <e_i, T_x e_j> for x in [0, 2L]; shape (len(xs), N, N)."""
        xs = np.atleast_1d(np.asarray(xs, dtype=float))
        t, w = np.polynomial.legendre.leggauss(self.N + 6)
        a = xs - self.L
        half = (self.L - a) / 2
        y = a[:, None] + half[:, None] * (t[None, :] + 1)
        wy = half[:, None] * w[None, :]
        return np.einsum('ibm,bm,jbm->bij', self.eval(y), wy, self.eval(y - xs[:, None]))

    def moments(self, a, nq=400):
        t, w = np.polynomial.legendre.leggauss(nq)
        x = self.L * t
        return (self.eval(x) * (np.exp(a * x) * w * self.L)[None, :]).sum(axis=1)


def assemble(L, N, nq_arch=320):
    """Weil form on LegendreBasis(L, N): dict with pole, arch, prime (W = pole + arch + prime) and the shift matrices M_n."""
    B = LegendreBasis(L, N)
    two_L = 2 * L
    kp, km = B.moments(0.5), B.moments(-0.5)
    pole = np.outer(kp, km) + np.outer(km, kp)
    t, w = np.polynomial.legendre.leggauss(nq_arch)
    xq = two_L / 2 * (t + 1)
    wq = two_L / 2 * w
    G = B.corr(xq)
    Ge = 0.5 * (G + np.transpose(G, (0, 2, 1)))
    I = np.eye(N)
    num = np.exp(-2 * xq)[:, None, None] * I[None] - np.exp(-xq / 2)[:, None, None] * Ge
    arch = -(LOGPI + EULER) * I + 2 * (wq[:, None, None] * num / (1 - np.exp(-2 * xq))[:, None, None]).sum(0) \
        - I * math.log(1 - math.exp(-2 * two_L))
    pps = [(n, lam) for n, lam in prime_powers(math.exp(two_L)) if math.log(n) < two_L]
    Ms, prime = {}, np.zeros((N, N))
    if pps:
        Gp = B.corr(np.array([math.log(n) for n, _ in pps]))
        for (n, lam), Mn in zip(pps, Gp):
            Ms[n] = Mn
            prime -= lam / math.sqrt(n) * (Mn + Mn.T)
    return {"pole": pole, "arch": arch, "prime": prime, "W": pole + arch + prime, "M": Ms, "kp": kp, "km": km, "basis": B}


# ----------------------------------------------------------------------------------------------- Legendre, multiprecision
def gl_nodes_hp(n, dps):
    import mpmath as mp
    from flint import arb
    t0, _ = np.polynomial.legendre.leggauss(n)
    ts, ws = [], []
    with mp.workdps(dps + 10):
        for x0 in t0:
            x = mp.mpf(x0)
            for it in range(9):
                p0, p1 = mp.mpf(1), x
                for k in range(1, n):
                    p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
                dp = n * (x * p1 - p0) / (x * x - 1)
                if it < 8:
                    x = x - p1 / dp
            ts.append(arb(mp.nstr(x, dps + 5)))
            ws.append(arb(mp.nstr(2 / ((1 - x * x) * dp * dp), dps + 5)))
    return ts, ws


def gh_nodes_hp(n, dps):
    """Gauss-Hermite (weight e^{-u^2}) nodes/weights via the normalised recurrence psi_k = c_k H_k."""
    import mpmath as mp
    from flint import arb
    u0, _ = np.polynomial.hermite.hermgauss(n)
    us, ws = [], []
    with mp.workdps(dps + 10):
        c0 = mp.pi ** (-mp.mpf(1) / 4)
        for x0 in u0:
            x = mp.mpf(x0)
            for it in range(10):
                p0, p1 = c0, mp.sqrt(2) * x * c0
                for k in range(1, n):
                    p0, p1 = p1, mp.sqrt(mp.mpf(2) / (k + 1)) * x * p1 - mp.sqrt(mp.mpf(k) / (k + 1)) * p0
                if it < 9:
                    x = x - p1 / (mp.sqrt(2 * n) * p0)
            us.append(arb(mp.nstr(x, dps + 5)))
            ws.append(arb(mp.nstr(1 / (n * p0 * p0), dps + 5)))
    return us, ws


def _arb(v, dps):
    import mpmath as mp
    from flint import arb
    return arb(mp.nstr(mp.mpf(v), dps + 5))


def _finish_hp(W, N, kp, km, corr_at, arch_nodes, xmax_arb, xmax_f, dps):
    """Add pole, archimedean and prime parts to the arb_mat W (zero on entry)."""
    from flint import arb
    for i in range(N):
        for j in range(N):
            W[i, j] = kp[i] * km[j] + km[i] * kp[j]
    logpi_gamma = arb.pi().log() + arb.const_euler()
    for x, wq in arch_nodes:
        G = corr_at(x)
        den = 1 - (-2 * x).exp()
        c0 = (-2 * x).exp() / den * wq * 2
        c1 = (-x / 2).exp() / den * wq * 2
        for i in range(N):
            for j in range(i, N):
                val = -c1 * (G[i, j] + G[j, i]) / 2 + (c0 if i == j else 0)
                W[i, j] += val
                if j != i:
                    W[j, i] += val
    tail = -(1 - (-2 * xmax_arb).exp()).log()
    for i in range(N):
        W[i, i] += -logpi_gamma + tail
    for n, lam in prime_powers(math.exp(xmax_f)):
        xn = arb(n).log()
        if not (xn < xmax_arb):
            continue
        G = corr_at(xn)
        cn = arb(smallest_prime(n)).log() / arb(n).sqrt()
        for i in range(N):
            for j in range(N):
                W[i, j] -= cn * (G[i, j] + G[j, i])
    return W


def assemble_hp_legendre(L, N, dps=120, nq_arch=200):
    """Multiprecision Weil form on the orthonormal Legendre basis of [-L, L]; returns (arb_mat W, kp, km)."""
    from flint import arb, arb_mat, ctx
    ctx.dps = dps
    La = _arb(L, dps)
    norm = [((2 * j + 1) / (2 * La)).sqrt() for j in range(N)]

    def vals(x):
        t = x / La
        P = [arb(1), t]
        for j in range(1, N - 1):
            P.append(((2 * j + 1) * t * P[j] - j * P[j - 1]) / (j + 1))
        return [P[j] * norm[j] for j in range(N)]

    tc, wc = gl_nodes_hp(N + 6, dps)

    def corr_at(x):
        lo, hi = x - La, La
        half = (hi - lo) / 2
        M = len(tc)
        E1, E2 = arb_mat(N, M), arb_mat(M, N)
        for m in range(M):
            y = lo + half * (tc[m] + 1)
            v1, v2 = vals(y), vals(y - x)
            wm = half * wc[m]
            for i in range(N):
                E1[i, m] = v1[i] * wm
                E2[m, i] = v2[i]
        return E1 * E2

    tm, wm_ = gl_nodes_hp(max(60, N + 20), dps)
    half = arb(1) / 2
    kp, km = [arb(0)] * N, [arb(0)] * N
    for m in range(len(tm)):
        x = La * tm[m]
        v = vals(x)
        fp, fm = (half * x).exp() * wm_[m] * La, (-half * x).exp() * wm_[m] * La
        kp = [kp[j] + v[j] * fp for j in range(N)]
        km = [km[j] + v[j] * fm for j in range(N)]
    twoL = 2 * La
    ta, wa = gl_nodes_hp(nq_arch, dps)
    arch_nodes = [(twoL / 2 * (ta[q] + 1), twoL / 2 * wa[q]) for q in range(len(ta))]
    W = _finish_hp(arb_mat(N, N), N, kp, km, corr_at, arch_nodes, twoL, 2 * float(L), dps)
    return W, kp, km


def assemble_hp_hermite(sigma, N, dps=60, panel_nodes=16):
    """Multiprecision Weil form on Hermite functions of width sigma: correlations and pole moments by Gauss-Hermite
    (exact for polynomial x Gaussian), archimedean integral by Gauss-Legendre panels of width sigma/2."""
    from flint import arb, arb_mat, ctx
    ctx.dps = dps
    sa = _arb(sigma, dps)
    K = N + 4
    gu, gw = gh_nodes_hp(K, dps)
    c0 = arb.pi() ** (arb(-1) / 4)
    s2 = arb(2).sqrt()

    def psi(z):
        P = [c0, s2 * z * c0]
        for n in range(1, N - 1):
            P.append((arb(2) / (n + 1)).sqrt() * z * P[n] - (arb(n) / (n + 1)).sqrt() * P[n - 1])
        return P[:N]

    def corr_at(x):
        s = x / sa
        E1, E2 = arb_mat(N, K), arb_mat(K, N)
        for k in range(K):
            a, b = psi(gu[k] + s / 2), psi(gu[k] - s / 2)
            for i in range(N):
                E1[i, k] = a[i] * gw[k]
                E2[k, i] = b[i]
        return (E1 * E2) * (-(s * s) / 4).exp()

    kp, km = [], []
    for sign in (1, -1):
        b = sign * sa / 2
        acc = [arb(0)] * N
        for k in range(K):
            P = psi(s2 * gu[k] + b)
            acc = [acc[j] + P[j] * gw[k] for j in range(N)]
        f = sa.sqrt() * s2 * (b * b / 2).exp()
        (kp if sign == 1 else km).extend([a * f for a in acc])
    smax = 2 * (math.sqrt(2 * N + 1) + math.sqrt((dps + 10) * math.log(10)))
    xmax_f = sigma * smax
    xmax = _arb(xmax_f, dps)
    tp, wp = gl_nodes_hp(panel_nodes, dps)
    npan = int(math.ceil(xmax_f / (sigma / 2)))
    arch_nodes = []
    for q in range(npan):
        a = xmax * q / npan
        hpan = xmax / npan / 2
        arch_nodes += [(a + hpan * (tp[m] + 1), hpan * wp[m]) for m in range(panel_nodes)]
    W = _finish_hp(arb_mat(N, N), N, kp, km, corr_at, arch_nodes, xmax, xmax_f, dps)
    return W, kp, km, xmax_f


def arb_to_mp(Wa, dps):
    import mpmath as mp
    mp.mp.dps = dps
    n = Wa.nrows()
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = mp.mpf(Wa[i, j].mid().str(dps + 5, radius=False))
    return M


def arbvec_to_mp(v, dps):
    import mpmath as mp
    mp.mp.dps = dps
    return [mp.mpf(x.mid().str(dps + 5, radius=False)) for x in v]


# ----------------------------------------------------------------------------------------------- Hermite, double
def herm_poly_norm(z, N):
    """psi_n(z) = c_n H_n(z), so that h_n(z) = psi_n(z) e^{-z^2/2}; shape (N,) + z.shape."""
    z = np.asarray(z, dtype=float)
    P = np.zeros((N,) + z.shape)
    P[0] = math.pi ** -0.25
    if N > 1:
        P[1] = math.sqrt(2) * z * P[0]
    for n in range(1, N - 1):
        P[n + 1] = math.sqrt(2 / (n + 1)) * z * P[n] - math.sqrt(n / (n + 1)) * P[n - 1]
    return P


class HermiteBasis:
    """e_j(x) = sigma^{-1/2} h_j(x / sigma)."""

    def __init__(self, sigma, N):
        self.s, self.N = float(sigma), int(N)
        self.u, self.wu = np.polynomial.hermite.hermgauss(N + 4)

    def corr(self, xs):
        s = np.atleast_1d(np.asarray(xs, dtype=float)) / self.s
        A = herm_poly_norm(self.u[None, :] + s[:, None] / 2, self.N)
        Bm = herm_poly_norm(self.u[None, :] - s[:, None] / 2, self.N)
        return np.einsum('ibk,k,jbk->bij', A, self.wu, Bm) * np.exp(-s ** 2 / 4)[:, None, None]

    def moments(self, a):
        b = a * self.s
        v, wv = np.polynomial.hermite.hermgauss(self.N + 40)
        t = math.sqrt(2) * v + b
        P = herm_poly_norm(t, self.N) * np.exp(-t ** 2 / 2 + b * t + v ** 2)[None, :]
        return math.sqrt(self.s) * math.sqrt(2) * (P * wv[None, :]).sum(axis=1)


def assemble_hermite(sigma, N, nq=600):
    B = HermiteBasis(sigma, N)
    xmax = 2 * sigma * (math.sqrt(2 * N + 1) + 9)
    kp, km = B.moments(0.5), B.moments(-0.5)
    pole = np.outer(kp, km) + np.outer(km, kp)
    t, w = np.polynomial.legendre.leggauss(nq)
    xq = xmax / 2 * (t + 1)
    wq = xmax / 2 * w
    G = B.corr(xq)
    Ge = 0.5 * (G + np.transpose(G, (0, 2, 1)))
    I = np.eye(N)
    num = np.exp(-2 * xq)[:, None, None] * I[None] - np.exp(-xq / 2)[:, None, None] * Ge
    arch = -(LOGPI + EULER) * I + 2 * (wq[:, None, None] * num / (1 - np.exp(-2 * xq))[:, None, None]).sum(0) \
        - I * math.log(1 - math.exp(-2 * xmax))
    pps = prime_powers(math.exp(xmax))
    prime = np.zeros((N, N))
    for i0 in range(0, len(pps), 4000):
        chunk = pps[i0:i0 + 4000]
        Gp = B.corr(np.array([math.log(n) for n, _ in chunk]))
        c = np.array([lam / math.sqrt(n) for n, lam in chunk])
        prime -= np.einsum('b,bij->ij', c, Gp + np.transpose(Gp, (0, 2, 1)))
    return {"W": pole + arch + prime, "pole": pole, "arch": arch, "prime": prime, "xmax": xmax, "n_pp": len(pps)}


# ----------------------------------------------------------------------------------------------- box grid on [0, ell]
def grid_W(ell, h, nodes=48):
    """Normalised boxes of mesh h on [0, ell]: W = Toeplitz(K) + kp km^T + km kp^T."""
    N = int(round(ell / h))
    t, w = np.polynomial.legendre.leggauss(nodes)
    K = np.zeros(N)
    x = h / 2 * (t + 1)
    wx = h / 2 * w
    K[0] = -(LOGPI + EULER) + 2 * np.sum(wx * (np.exp(-2 * x) - np.exp(-x / 2) * (1 - x / h)) / (1 - np.exp(-2 * x))) \
        - math.log(1 - math.exp(-2 * h))
    for m in range(1, N):
        tot = 0.0
        for a, b, rising in (((m - 1) * h, m * h, True), (m * h, (m + 1) * h, False)):
            x = a + (b - a) / 2 * (t + 1)
            wx = (b - a) / 2 * w
            f = (x - (m - 1) * h) / h if rising else ((m + 1) * h - x) / h
            tot += np.sum(wx * np.exp(-x / 2) * f / (1 - np.exp(-2 * x)))
        K[m] = -tot
    for n, lam in prime_powers(math.exp(ell)):
        a = math.log(n)
        if a >= ell:
            continue
        k = int(a // h)
        fr = a / h - k
        c = lam / math.sqrt(n)
        if k < N:
            K[k] -= c * (1 - fr)
        if k + 1 < N:
            K[k + 1] -= c * fr
    i = np.arange(N)
    T = K[np.abs(i[:, None] - i[None, :])]
    kp = 2 * (np.exp((i + 1) * h / 2) - np.exp(i * h / 2)) / math.sqrt(h)
    km = -2 * (np.exp(-(i + 1) * h / 2) - np.exp(-i * h / 2)) / math.sqrt(h)
    return T + np.outer(kp, km) + np.outer(km, kp)


def diag_mass(X, a, h, rows=None):
    """Sum of the means of the two diagonals straddling lag a (entries X[i, i+k]); for a kernel atom c delta(x-y-a)
    this tends to c as h -> 0, while integrable kernels give O(h)."""
    k = int(a // h)
    d1, d2 = np.diag(X, k), np.diag(X, k + 1)
    if rows is not None:
        d1, d2 = d1[rows[0]:rows[1]], d2[rows[0]:rows[1]]
    return float(np.mean(d1) + np.mean(d2))

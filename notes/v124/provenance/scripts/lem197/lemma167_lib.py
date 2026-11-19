"""Shared library for TAA Lemmas 167-169 (Weil-form spectrometers). RH is not proved.
L149 basis: cubic B-spline hats e_j(u) = B3(u/h - j), j = 0..N-1, span W = (N+1)h; Toeplitz rows from l149/rows_h{h}.npz
(read-only: d, G2 = hat Gram row, POLE, AZ = zeta arch (Gamma(s/2), -log pi), AD = DH arch (Gamma((s+1)/2), +log(5/pi)), PZ, PD = full prime rows).
Prime rows recomputed here: row(v) = -sum_n coef(n)/sqrt(n) * h B3((log n - v)/h)  (same as t781/c4)."""
import numpy as np, math, os
_D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'l149_small')
from scipy.linalg import eigh, toeplitz, null_space
C = np.load(''+_D+'/coef.npz'); LAM = C['Lam']; CDH = C['cDH']
def B3(x):
    x = np.abs(x); return np.where(x < 1, 2/3-x**2+x**3/2, np.where(x < 2, (2-x)**3/6, 0.0))
def rows(h):
    R = np.load(f''+_D+f'/rows_h{h}.npz'); return {k: R[k] for k in R.files}
def chi5(n):
    r = np.asarray(n) % 5; out = np.zeros(np.shape(n), complex)
    out[r == 1] = 1; out[r == 2] = 1j; out[r == 3] = -1j; out[r == 4] = -1; return out
def prow(coef, d, h, sel=None, nmax=None):
    """coef indexed by n (coef[0], coef[1] ignored); sel boolean mask over n (same length) or None = all."""
    nmax = nmax or len(coef)-1
    n = np.arange(2, nmax+1); c = coef[2:nmax+1]
    if sel is not None: c = np.where(sel[2:nmax+1], c, 0)
    keep = c != 0; n = n[keep]; c = c[keep]; ln = np.log(n); w = c/np.sqrt(n)
    PR = np.zeros(len(d), complex)
    for i, v in enumerate(d):
        lo, hi = np.searchsorted(ln, v-2*h), np.searchsorted(ln, v+2*h)
        if hi > lo: PR[i] -= np.sum(w[lo:hi]*h*B3((ln[lo:hi]-v)/h))
    return PR
def gen_eigs(rw, G2, N, real=False, kerP=False, h=None):
    M = toeplitz(rw[:N], np.conj(rw[:N])); B = toeplitz(G2[:N]).astype(float)
    if real or np.max(np.abs(np.imag(rw[:N]))) == 0: M = M.real
    if kerP:
        a = np.arange(N)*h; K = null_space(np.vstack([np.exp(a/2), np.exp(-a/2)]))
        M = K.T@M@K if np.isrealobj(M) else K.conj().T@M@K; B = K.T@B@K
    return eigh(M, B, eigvals_only=True)
def onset(rw, G2, h, Nmax, real=False, kerP=False, thr=-1e-9, Nlo=4):
    f = lambda N: gen_eigs(rw, G2, N, real, kerP, h)[0] < thr
    if not f(Nmax): return None
    lo, hi = Nlo, Nmax
    if f(lo): return round((lo+1)*h, 6)
    while hi-lo > 1:
        m = (lo+hi)//2
        if f(m): hi = m
        else: lo = m
    return round((hi+1)*h, 6)
def factor_sets(nmax):
    spf = np.zeros(nmax+1, dtype=np.int64)
    for p in range(2, nmax+1):
        if spf[p] == 0: spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    maxp = np.zeros(nmax+1, dtype=np.int64); npf = np.zeros(nmax+1, dtype=np.int64)
    for n in range(2, nmax+1):
        m = n; last = 0; k = 0; mx = 0
        while m > 1:
            p = spf[m]
            if p != last: k += 1; last = p
            mx = max(mx, p); m //= p
        maxp[n] = mx; npf[n] = k
    return maxp, npf   # largest prime factor; number of distinct prime factors (1 => prime power)
def log_deriv_coeffs(a, nmax):
    """c with c * a = a . log (Dirichlet), a[1] = 1: c(n) = a(n) log n - sum_{d|n, 1<d<n... } ; computed by forward sieve."""
    a = np.asarray(a, float); c = np.zeros(nmax+1); acc = np.zeros(nmax+1)
    nz = np.nonzero(a[2:nmax+1])[0]+2
    for n in range(2, nmax+1):
        c[n] = a[n]*math.log(n) - acc[n]
        if c[n] != 0.0:
            ks = nz[nz <= nmax//n]
            if len(ks): acc[n*ks] += c[n]*a[ks]
    return c
def epstein_coeffs(nmax, forms=((1, 0, 5),)):
    """r_Q(n)/2 for Q = A x^2 + B x y + C y^2 summed over forms; a[1] normalised by the caller."""
    r = np.zeros(nmax+1)
    for (A, Bq, Cq) in forms:
        X = int(math.sqrt(4*Cq*nmax/(4*A*Cq-Bq*Bq)))+2
        for x in range(-X, X+1):
            Y = X
            ys = np.arange(-Y, Y+1); v = A*x*x+Bq*x*ys+Cq*ys*ys
            v = v[(v >= 1) & (v <= nmax)]; np.add.at(r, v, 1)
    return r

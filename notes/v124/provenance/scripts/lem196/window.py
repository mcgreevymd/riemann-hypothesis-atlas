"""L196 step 3-4: (a) 4x4 Hodge-index lattice {f1,f2,Delta,Gamma_n} <=> Weil bound at n (exact check);
(b) F_q window forms on degrees 0..L in the Gamma_k basis (congruent to the normalized basis, Sylvester):
   Gram(Gamma)_{kl} = q^min(k,l) N_|k-l|, N_0 = 2-2g = -2  (intersection numbers on C x C)
   Q = -Gram(Gamma)  (analogue of CCM Q: Perron, kernel -q^{-m/2}N_m <= 0 iff N_m >= 0)
   C+ = sum x_k q^k (= .f2), C- = sum x_k (= .f1);  P = 2 C+ C-;  W = Q + P = -(primitive intersection) = Toeplitz(q^{-m/2} S_m)
   E0 = ker C+ cap ker C- (primitive), cosh^perp = ker(C+ + C-) (= (f1+f2)^perp).
 Inertia exactly by Jacobi sign rule on fraction-free (Bareiss) leading minors; zero minor -> mpmath fallback.
RH is not proved."""
import json, math, sys, numpy as np, mpmath as mp, sympy
from ladder import S_seq
mp.mp.dps = 80
LMAX = 30
def leading_minors(M):
    n = len(M); A = [row[:] for row in M]; prev = 1; out = []
    for k in range(n):
        piv = A[k][k]; out.append(piv)
        if piv == 0: return out, False
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*piv - A[i][k]*A[k][j])//prev
        prev = piv
    return out, True
def neg_counts(M):
    """n_- of each leading block (sizes 1..n) via Jacobi; None where undecidable."""
    D, ok = leading_minors(M); res = []; ch = 0; s_prev = 1
    for d in D:
        if d == 0: break
        s = 1 if d > 0 else -1
        ch += (s != s_prev); s_prev = s; res.append(ch)
    return res
def mp_negcount(M):
    A = mp.matrix(M); n = A.rows
    sc = [mp.sqrt(abs(A[i, i])) if A[i, i] != 0 else 1 for i in range(n)]
    B = mp.matrix(n, n)
    for i in range(n):
        for j in range(n): B[i, j] = A[i, j]/(sc[i]*sc[j])
    ev = mp.eigsy(B, eigvals_only=True)
    return sum(1 for e in ev if e < -mp.mpf(10)**-40)
def forms(a1, a2, q, L):
    S = S_seq(a1, a2, q, L); N = [-2]+[1+q**k-S[k] for k in range(1, L+1)]
    G = [[q**min(k, l)*N[abs(k-l)] for l in range(L+1)] for k in range(L+1)]  # Gram(Gamma)
    Qm = [[-x for x in row] for row in G]
    Wm = [[q**min(k, l)*S[abs(k-l)] for l in range(L+1)] for k in range(L+1)]
    return G, Qm, Wm, S, N
def restrict(M, B):
    # B: list of basis vectors (ints); returns B^T M B
    MB = [[sum(M[i][k]*b[k] for k in range(len(b))) for i in range(len(M))] for b in B]
    return [[sum(B[a][i]*MB[c][i] for i in range(len(M))) for c in range(len(B))] for a in range(len(B))]
def bases(q, L):
    E0 = []; CP = []
    for j in range(2, L+1):
        v = [0]*(L+1); v[0] = q**j - q; v[1] = -(q**j - 1); v[j] = q - 1; E0.append(v)
    for j in range(1, L+1):
        v = [0]*(L+1); v[0] = 1 + q**j; v[j] = -2; CP.append(v)
    return E0, CP
def onset(counts):
    for i, c in enumerate(counts):
        if c and c > 0: return i
    return None
def analyse_one(a1, a2, q, L=LMAX):
    G, Qm, Wm, S, N = forms(a1, a2, q, L)
    E0, CP = bases(q, L)
    WE = restrict(Wm, E0)  # = Q on E0
    QC = restrict(Qm, CP)
    nW = neg_counts(Wm); nE = neg_counts(WE); nC = neg_counts(QC); nQ = neg_counts(Qm)
    r = {'nW_by_size': nW, 'nQE0_by_size': nE, 'nQcosh_by_size': nC, 'nQ_by_size': nQ}
    # onset windows L* (window = degrees 0..L, size L+1; E0 size L-1 (L>=2); cosh^perp size L (L>=1))
    r['Lstar_W'] = onset(nW); r['Lstar_E0'] = (onset(nE)+2) if onset(nE) is not None else None
    r['Lstar_cosh'] = (onset(nC)+1) if onset(nC) is not None else None
    r['decided_sizes'] = [len(nW), len(nE), len(nC), len(nQ)]
    return r
if __name__ == '__main__':
    R = json.load(open('out/ladder_raw.json')); C = json.load(open('out/curves.json'))
    res = {}
    # (a) 4x4 Hodge-index check
    hi = {}
    for q, rows in R.items():
        qq = int(q); bad = 0; tot = 0
        for x in rows:
            if not x['iv']: continue
            S = S_seq(x['a1'], x['a2'], qq, 20)
            for n in range(1, 21):
                Nn = 1 + qq**n - S[n]
                Gm = sympy.Matrix([[0, 1, 1, 1], [1, 0, 1, qq**n], [1, 1, -2, Nn], [1, qq**n, Nn, -2*qq**n]])
                cp = Gm.charpoly().all_coeffs()  # real-rooted => Descartes exact
                nz = [c for c in cp if c != 0]
                npos = sum(1 for i in range(len(nz)-1) if (nz[i] > 0) != (nz[i+1] > 0))
                hodge = (npos == 1)
                weil = S[n]**2 <= 16*qq**n
                tot += 1; bad += (hodge != weil)
        hi[q] = {'pairs_checked': tot, 'HodgeIndex_vs_Weil_mismatch': bad}
        print('4x4', q, hi[q], flush=True)
    res['hodge4x4'] = hi
    json.dump(res, open('out/window.json', 'w'), default=str)

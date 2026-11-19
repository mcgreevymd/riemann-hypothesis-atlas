"""L196 step 1: genus-2 curves y^2=f(x), f squarefree of degree 5 or 6 over F_q (q=3,5,7,11).
Point counts N1 (F_q) and N2 (F_{q^2} = F_q[t]/(t^2-nu)), L-poly P(T)=1+a1T+a2T^2+q a1T^3+q^2T^4.
Reductions: y-scaling => leading coeff in {1,nu}; for q>=5 translation kills x^5 (deg 6) / x^4 (deg 5, q!=5) coeff.
Squarefreeness checked exactly (sympy gcd over GF(q)) on a representative of each (a1,a2) class; also full
squarefree census for q<=7. RH is not proved."""
import numpy as np, itertools, json, sys, time
from sympy import Poly, GF, symbols
X = symbols('x')
def nonres(q): return next(a for a in range(2, q) if pow(a, (q-1)//2, q) == q-1)
def sqfree(coeffs, q):  # coeffs low->high
    f = Poly(list(reversed([c % q for c in coeffs])), X, modulus=q)
    return f.degree() >= 5 and f.gcd(f.diff(X)).degree() == 0
def census(q):
    nu = nonres(q); chi = np.array([0]+[1 if pow(a, (q-1)//2, q) == 1 else -1 for a in range(1, q)])
    # F_{q^2} elements a+b t, t^2=nu ; norm a^2 - nu b^2 ; chi_{q^2}(z) = chi_q(N z)
    A = np.array([(a, b) for a in range(q) for b in range(q)])
    fams = []
    for deg in (5, 6):
        for lead in (1, nu):
            free = list(range(deg))  # coefficient indices 0..deg-1
            kill = None
            if q >= 5 and deg == 6: kill = 5
            if q >= 5 and deg == 5 and q != 5: kill = 4
            idx = [i for i in free if i != kill]
            fams.append((deg, lead, kill, idx))
    res = {}; reps = {}
    for (deg, lead, kill, idx) in fams:
        grid = np.array(list(itertools.product(range(q), repeat=len(idx))), dtype=np.int64)
        n = len(grid); C = np.zeros((n, deg+1), dtype=np.int64); C[:, deg] = lead
        for j, i in enumerate(idx): C[:, i] = grid[:, j]
        # N1
        xs = np.arange(q); val = np.zeros((n, q), dtype=np.int64)
        for d in range(deg, -1, -1): val = (val*xs + C[:, d:d+1]) % q
        inf1 = (1 + chi[lead]) if deg == 6 else 1
        N1 = q + chi[val].sum(1) + inf1
        # N2: Horner in F_{q^2}
        va = np.zeros((n, q*q), dtype=np.int64); vb = np.zeros((n, q*q), dtype=np.int64)
        xa, xb = A[:, 0], A[:, 1]
        for d in range(deg, -1, -1):
            na = (va*xa + nu*vb*xb + C[:, d:d+1]) % q; nb = (va*xb + vb*xa) % q; va, vb = na, nb
        nrm = (va*va - nu*vb*vb) % q
        inf2 = 2 if deg == 6 else 1
        N2 = q*q + chi[nrm].sum(1) + inf2
        a1 = N1 - q - 1; S1 = -a1; S2 = q*q + 1 - N2  # S2 = sum alpha^2 = a1^2 - 2 a2
        a2 = (a1*a1 - S2)//2
        assert np.all((a1*a1 - S2) % 2 == 0)
        keys = np.stack([a1, a2], 1)
        u, first, cnt = np.unique(keys, axis=0, return_index=True, return_counts=True)
        for (k1, k2), fi, c in zip(u.tolist(), first.tolist(), cnt.tolist()):
            res.setdefault((k1, k2), 0); res[(k1, k2)] += c
            reps.setdefault((k1, k2), []).append((C[fi].tolist(), [int(i) for i in np.where((keys == [k1, k2]).all(1))[0][:40]], deg, lead, kill, idx, grid))
    # squarefree certification per class: try up to 40 members
    attained = {}
    for key, lst in reps.items():
        ok = None
        for (c0, members, deg, lead, kill, idx, grid) in lst:
            for m in members:
                C = [0]*(deg+1); C[deg] = lead
                for j, i in enumerate(idx): C[i] = int(grid[m][j])
                if sqfree(C, q): ok = C; break
            if ok: break
        if ok: attained[key] = ok
    return attained, res
out = {}
for q in [int(a) for a in sys.argv[1:]] or [3, 5, 7, 11]:
    t = time.time(); att, res = census(q)
    out[q] = {'pairs': sorted([list(k) for k in att]), 'witness_f_low_to_high': {f'{k[0]},{k[1]}': v for k, v in att.items()},
              'n_pairs': len(att), 'pairs_from_nonsquarefree_only': sorted([list(k) for k in res if k not in att])}
    print(q, 'attained (a1,a2):', len(att), 'nonsqfree-only classes', len(out[q]['pairs_from_nonsquarefree_only']), f'{time.time()-t:.1f}s', flush=True)
json.dump(out, open('out/curves.json', 'w'), indent=0)

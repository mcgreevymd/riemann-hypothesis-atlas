"""L196 extras: (1) mp fallback for fakes with zero leading minors; (2) index vs type; (3) failure localization by degree d
(analogue of §351 place attribution) on Q|E0 at onset, with random-vector baseline; (4) one-place perturbations of real curves;
(5) Hodge-index slack s_n of real curves. RH is not proved."""
import json, math, random, collections, numpy as np, mpmath as mp
from window import forms, restrict, bases, mp_negcount, neg_counts, onset
from ladder import S_seq, closed_points
mp.mp.dps = 60
R = json.load(open('out/ladder_raw.json')); C = json.load(open('out/curves.json')); WR = json.load(open('out/window_runs.json'))
out = {}
# (1)+(2)
fb = {}; typ = collections.defaultdict(collections.Counter)
for q, rows in WR['fakes'].items():
    qq = int(q); lst = []
    for r in rows:
        full = (len(r['nW']) == 31)
        if not full:
            nW = []
            for L in range(0, 13):
                G, Qm, Wm, S, N = forms(r['a1'], r['a2'], qq, L); nW.append(mp_negcount(Wm))
            r['nW_mp'] = nW; r['Lstar_W'] = onset(nW); lst.append({'a1': r['a1'], 'a2': r['a2'], 'nW_mp_L0..12': nW})
        fin = r.get('nW_mp', r['nW'])[-1]
        typ[q][(r['type'] if r['vi'] else 'not_vi', fin)] += 1
    fb[q] = lst
json.dump({'fallback': fb, 'WR': WR}, open('out/fallback_cache.json', 'w'))
out['fallback'] = fb; out['index_by_type'] = {q: {f'{k[0]}|nW={k[1]}': v for k, v in c.items()} for q, c in typ.items()}
print('index by type', out['index_by_type'])
print('fallback Lstar', {q: collections.Counter(onset(x['nW_mp_L0..12']) for x in l) for q, l in fb.items()})
# (3) localization
def E0_onb(q, L):
    A = mp.matrix(2, L+1)
    for k in range(L+1): A[0, k] = mp.sqrt(q)**k; A[1, k] = mp.sqrt(q)**(-k)
    # orthonormal basis of null space via QR of A^T complement (Gram-Schmidt)
    basis = []
    rows = [[A[0, k] for k in range(L+1)], [A[1, k] for k in range(L+1)]]
    def gs(v, B):
        for b in B:
            c = sum(v[i]*b[i] for i in range(len(v))); v = [v[i]-c*b[i] for i in range(len(v))]
        n = mp.sqrt(sum(x*x for x in v)); return [x/n for x in v], n
    R2 = []
    for rw in rows:
        v, n = gs(rw, R2); R2.append(v)
    for k in range(L+1):
        e = [mp.mpf(0)]*(L+1); e[k] = mp.mpf(1)
        v, n = gs(e, R2 + basis)
        if n > mp.mpf(10)**-20: basis.append(v)
    return basis
def attribution(v, q, a, L):
    Rm = [sum(v[k]*v[k+m] for k in range(L+1-m))*(1 if m == 0 else 2) for m in range(L+1)]
    A = {d: d*a[d]*sum(mp.sqrt(q)**(-m)*Rm[m] for m in range(d, L+1, d)) for d in range(1, L+1)}
    return {d: float(x) for d, x in A.items()}, float(2*Rm[0])
loc = {}
for q in ['7', '11']:
    qq = int(q); rows = [r for r in WR['fakes'][q] if r['Lstar_E0']]
    random.seed(1); rows = random.sample(rows, min(300, len(rows)))
    top_neg = collections.Counter(); top_rand = collections.Counter(); share_neg = collections.defaultdict(list); share_rand = collections.defaultdict(list)
    for r in rows:
        L = r['Lstar_E0']; S = S_seq(r['a1'], r['a2'], qq, L); N = [-2]+[1+qq**k-S[k] for k in range(1, L+1)]
        a = closed_points(N, L)
        B = E0_onb(qq, L)
        u = [mp.mpf(S[m])/mp.sqrt(qq)**m for m in range(L+1)]
        M = mp.matrix(len(B), len(B))
        for i in range(len(B)):
            for j in range(len(B)):
                M[i, j] = sum(B[i][k]*B[j][l]*u[abs(k-l)] for k in range(L+1) for l in range(L+1))
        ev, V = mp.eigsy(M)
        i0 = min(range(len(B)), key=lambda i: ev[i])
        v = [sum(V[i, i0]*B[i][k] for i in range(len(B))) for k in range(L+1)]
        A, g0 = attribution(v, qq, a, L)
        assert abs(g0 - sum(A.values()) - float(ev[i0])) < 1e-8*max(1, abs(float(ev[i0])))
        pos = {d: x for d, x in A.items() if x > 0}; tot = sum(pos.values())
        top_neg[max(A, key=A.get)] += 1
        for d in (1, 2, 3): share_neg[d].append(pos.get(d, 0)/tot if tot else 0)
        for t in range(5):
            w = np.random.default_rng(abs(t+r['a1']*100000+r['a2']*7)+t).standard_normal(len(B))
            w = w/np.linalg.norm(w); vv = [sum(mp.mpf(w[i])*B[i][k] for i in range(len(B))) for k in range(L+1)]
            Ar, _ = attribution(vv, qq, a, L); posr = {d: x for d, x in Ar.items() if x > 0}; tr = sum(posr.values())
            top_rand[max(Ar, key=Ar.get)] += 1
            for d in (1, 2, 3): share_rand[d].append(posr.get(d, 0)/tr if tr else 0)
    loc[q] = {'n': len(rows), 'top_degree_neg': dict(top_neg), 'top_degree_random': dict(top_rand),
              'mean_share_neg': {d: float(np.mean(s)) for d, s in share_neg.items()},
              'mean_share_random': {d: float(np.mean(s)) for d, s in share_rand.items()}}
    print('loc', q, loc[q], flush=True)
out['localization'] = loc
# (4) one-place perturbations of real curves
pert = {}
for q in ['5', '7', '11']:
    qq = int(q); pairs = C[q]['pairs']; random.seed(4); pairs = pairs if len(pairs) <= 120 else random.sample(pairs, 120)
    res = collections.defaultdict(collections.Counter); HI = collections.Counter()
    for (a1, a2) in pairs:
        S = S_seq(a1, a2, qq, 20)
        for d in (1, 2, 3, 4):
            for s in (+1, -1):
                for conv in ('A', 'B'):
                    Sp = [S[m] - s*d*(m % d == 0 and m > 0) for m in range(21)]
                    Sp[0] = 4 - s*d if conv == 'A' else 4
                    on = None
                    for L in range(1, 13):
                        Wm = [[qq**min(k, l)*Sp[abs(k-l)] for l in range(L+1)] for k in range(L+1)]
                        if mp_negcount(Wm) > 0: on = L; break
                    res[f'd={d},{"+" if s>0 else "-"}1,conv{conv}'][on] += 1
                hv = [n for n in range(1, 21) if (S[n]-s*d*(n % d == 0))**2 > 16*qq**n]
                HI[f'd={d},{"+" if s>0 else "-"}1: 4x4 HI first fail n'] += 0
                HI[(d, s, hv[0] if hv else None)] += 1
    pert[q] = {'onset_W_by_case': {k: {str(kk): vv for kk, vv in c.items()} for k, c in res.items()},
               'HI4x4_first_fail': {f'd={k[0]},s={k[1]},n={k[2]}': v for k, v in HI.items() if isinstance(k, tuple)}}
    print('pert', q, json.dumps(pert[q]), flush=True)
out['perturbation'] = pert
# (5) slack
sl = {}
for q, d in C.items():
    qq = int(q); vals = []; zero = 0
    for (a1, a2) in d['pairs']:
        S = S_seq(a1, a2, qq, 50); s = [1-abs(S[n])/(4*qq**(n/2)) for n in range(1, 51)]
        vals.append(min(s)); zero += any(S[n]**2 == 16*qq**n for n in range(1, 51))
        s1 = 1-abs(S[1])/(4*qq**.5)
    sl[q] = {'min_slack_n<=50': min(vals), 'median_min_slack': float(np.median(vals)), 'curves_with_exact_zero_slack(some n<=50)': zero,
             'min_slack_n=1': min(1-abs(a1)/(4*qq**.5) for a1, a2 in d['pairs'])}
print('slack', sl)
out['slack_real'] = sl
json.dump(out, open('out/extras.json', 'w'), indent=1, default=str)

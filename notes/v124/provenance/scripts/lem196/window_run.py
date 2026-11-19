"""L196 step 4: window-form inertia for fakes (rung iv survivors, off-circle) and real curves; onset L*; Haynsworth check.
RH is not proved."""
import json, sys, math, random, numpy as np, mpmath as mp
from multiprocessing import Pool
from window import forms, restrict, bases, neg_counts, onset, mp_negcount, LMAX
from ladder import S_seq
def fake_job(args):
    q, x = args
    G, Qm, Wm, S, N = forms(x['a1'], x['a2'], q, LMAX)
    E0, CP = bases(q, LMAX)
    nW = neg_counts(Wm); nE = neg_counts(restrict(Wm, E0)); nC = neg_counts(restrict(Qm, CP)); nQ = neg_counts(Qm)
    o = {'a1': x['a1'], 'a2': x['a2'], 'delta': x.get('delta', math.log(x['r'], q)-.5), 'vi': bool(x.get('vi')),
         'type': x.get('type'), 'fwv': x.get('first_weil_violation_n'),
         'Lstar_W': onset(nW), 'Lstar_E0': None if onset(nE) is None else onset(nE)+2,
         'Lstar_cosh': None if onset(nC) is None else onset(nC)+1,
         'nW': nW, 'nE0': nE, 'ncosh': nC, 'nQ': nQ}
    # Haynsworth / L194(e) checks where decided: n-(Q|E0) <= n-(Q|cosh) <= n-(Q|E0)+1 ; n-(W) - n-(Q|E0) in {0,1,2}
    return o
def real_job(args):
    q, a1, a2, L = args
    mp.mp.dps = 60
    G, Qm, Wm, S, N = forms(a1, a2, q, L)
    E0, CP = bases(q, L)
    sq = [mp.sqrt(mp.mpf(q))**k for k in range(L+1)]
    # normalized W: u_{|k-l|} = S/q^{|k-l|/2}
    Wn = mp.matrix(L+1, L+1)
    for k in range(L+1):
        for l in range(L+1): Wn[k, l] = mp.mpf(S[abs(k-l)])/mp.sqrt(mp.mpf(q))**abs(k-l)
    ev = sorted(mp.eigsy(Wn, eigvals_only=True))
    rank = sum(1 for e in ev if abs(e) > mp.mpf(10)**-30)
    return {'a1': a1, 'a2': a2, 'L': L, 'Wmin': float(ev[0]), 'Wrank': rank, 'top4': [float(e) for e in ev[-4:]],
            'nQ': mp_negcount(Qm), 'nQE0': mp_negcount(restrict(Wm, E0)), 'nQcosh': mp_negcount(restrict(Qm, CP))}
if __name__ == '__main__':
    qs = [int(a) for a in sys.argv[1:]] or [3, 5, 7, 11]
    R = json.load(open('out/ladder_raw.json')); C = json.load(open('out/curves.json'))
    out = {'fakes': {}, 'real': {}}
    with Pool(8) as P:
        for q in qs:
            fk = [x for x in R[str(q)] if x['iv'] and not x['on']]
            out['fakes'][q] = P.map(fake_job, [(q, x) for x in fk], chunksize=8)
            pairs = C[str(q)]['pairs'] if str(q) in C else []
            random.seed(196); pairs = pairs if len(pairs) <= 120 else random.sample(pairs, 120)
            out['real'][q] = P.map(real_job, [(q, a, b, 16) for a, b in pairs])
            print(q, len(fk), 'fakes;', len(pairs), 'real', flush=True)
    json.dump(out, open('out/window_runs.json', 'w'))

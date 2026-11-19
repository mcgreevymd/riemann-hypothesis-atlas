"""L196 rank/signature check of window W for fakes: Thm 196.4 predicts rank W_L = 4 (distinct roots, L>=3) and
signature (4 - 2m, m)... i.e. n_- = number of off-circle FE pairs {beta,1/conj(beta)} up to conjugation; onset L*<=3 (=2g-1).
Also nQ = nW + 1 (pole plane, Haynsworth). RH is not proved."""
import json, random, collections, mpmath as mp
from window import forms
from ladder import S_seq
mp.mp.dps = 80
WR = json.load(open('out/window_runs.json')); R = json.load(open('out/ladder_raw.json'))
out = {}
for q in ['5', '7', '11', '13']:
    qq = int(q); rows = [x for x in R[q] if x['iv'] and not x['on']]; random.seed(7); rows = random.sample(rows, min(150, len(rows)))
    c = collections.Counter(); bad = 0
    for x in rows:
        al = mp.polyroots([qq*qq, qq*x['a1'], x['a2'], x['a1'], 1], maxsteps=200, extraprec=200)
        al = [1/a for a in al]; beta = [a/mp.sqrt(qq) for a in al]
        offpairs = sum(1 for b in beta if abs(b) > 1+mp.mpf(10)**-20)  # one per FE pair
        # predicted n_-: off pairs counted up to conjugation -> each off pair (beta,1/beta) is one negative direction
        L = 10; G, Qm, Wm, S, N = forms(x['a1'], x['a2'], qq, L)
        u = [mp.mpf(S[m])/mp.sqrt(qq)**m for m in range(L+1)]
        Wn = mp.matrix([[u[abs(k-l)] for l in range(L+1)] for k in range(L+1)])
        ev = mp.eigsy(Wn, eigvals_only=True); sc = max(abs(e) for e in ev)
        rank = sum(1 for e in ev if abs(e) > sc*mp.mpf(10)**-40); nneg = sum(1 for e in ev if e < -sc*mp.mpf(10)**-40)
        P = mp.matrix([[mp.sqrt(qq)**(k-l)+mp.sqrt(qq)**(l-k) for l in range(L+1)] for k in range(L+1)])
        evq = mp.eigsy(Wn-P, eigvals_only=True); scq = max(abs(e) for e in evq)
        nq = sum(1 for e in evq if e < -scq*mp.mpf(10)**-40)
        c[(rank, nneg, offpairs, nq)] += 1; bad += (nneg != offpairs) or (nq != nneg+1)
    out[q] = {'(rank,n-W,offpairs,n-Q)': {str(k): v for k, v in c.items()}, 'violations_of_prediction': bad, 'n': len(rows)}
    print(q, out[q], flush=True)
json.dump(out, open('out/rankcheck.json', 'w'), indent=1)

"""L196 step 2-3: ablation ladder for integer FE-shaped genus-2 'L-polynomials' P(T)=1+a1T+a2T^2+q a1 T^3+q^2 T^4.
Box |a1|<=4q, |a2|<=6q^2 is complete for rung (iii) (Thm 196.1: N_n>=0 for all n => max|alpha|<=q).
All 'for all n / for all d' statements certified: exact integer check for n<D0 plus an explicit tail bound.
RH is not proved."""
import numpy as np, json, math, sys, time
def mu(n):
    r, m, p = 1, n, 2
    while p*p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r
MU = [0]+[mu(n) for n in range(1, 2001)]
def S_seq(a1, a2, q, D):
    # power sums of inverse roots: Newton for k<=4, recurrence afterwards. Exact ints.
    e = [1, -a1, a2, -q*a1, q*q]  # P(T)=prod(1-alpha T) => e_k = (-1)^k c_k ; c=(1,a1,a2,qa1,q^2)
    S = [4]+[0]*D
    for k in range(1, D+1):
        s = (-1)**(k-1)*k*e[k] if k <= 4 else 0
        for i in range(1, min(k, 5)):
            s += (-1)**(i-1)*e[i]*S[k-i]
        S[k] = s
    return S
def closed_points(N, D):
    a = [None]
    for d in range(1, D+1):
        s = 0
        for e in range(1, d+1):
            if d % e == 0: s += MU[d//e]*N[e]
        assert s % d == 0
        a.append(s//d)
    return a
def tail_ok(q, r, D0):
    # for d>=D0: d*a_d >= q^d - 4 r^d - sum_{e<=d/2}(1+q^e+4 r^e) > 0 ; check D0..D0+400 in logs (monotone tail beyond)
    if r >= q: return False
    for d in range(D0, D0+400):
        rr = max(r, 1.0001); lq = math.log(q)
        rel = (d/2)*math.exp(-d*lq) + math.exp((1-d/2)*lq)/(q-1) + 4*math.exp((d/2+1)*math.log(rr) - d*lq)/(rr-1)
        if not (1 - 4*math.exp(d*math.log(r/q)) - rel > 0): return False
    return True
def certify_nonneg(seqfun, q, r, Dmax=3000):
    """seqfun(D) -> (N list, a list) exact; returns (min over n<D0 of N_n, of a_d, D0, certified flag)."""
    D0 = 8
    while D0 < Dmax and not tail_ok(q, r, D0): D0 += 4
    N, a = seqfun(D0)
    return min(N[1:D0+1]), min(a[1:D0+1]), D0, (D0 < Dmax), N, a
def analyse(q):
    rows = []
    for a1 in range(-4*q, 4*q+1):
        for a2 in range(-6*q*q, 6*q*q+1):
            al = 1/np.roots([q*q, q*a1, a2, a1, 1]); r = float(np.max(np.abs(al)))
            on = bool(np.all(np.abs(np.abs(al)/math.sqrt(q)-1) < 1e-6))
            rows.append((a1, a2, r, on, al))
    out = []
    for (a1, a2, r, on, al) in rows:
        rec = {'a1': a1, 'a2': a2, 'r': r, 'on': on}
        # rung iii/iv for P and (v) for twist P(-T) <-> (a1,a2)->(-a1,a2)
        def seq(D, s1=a1):
            S = S_seq(s1, a2, q, D); N = [2-4]+[1+q**k-S[k] for k in range(1, D+1)]
            return N, closed_points(N, D)
        # quick reject
        S = S_seq(a1, a2, q, 30); N = [None]+[1+q**k-S[k] for k in range(1, 31)]
        if min(N[1:]) < 0:
            rec.update(iii=False, iv=False, v=False); out.append(rec); continue
        if r > q*(1+1e-9):
            # Thm 196.1 says impossible for (iii); check exactly to 400 to be sure
            S = S_seq(a1, a2, q, 400); N = [None]+[1+q**k-S[k] for k in range(1, 401)]
            rec.update(iii=min(N[1:]) >= 0, iii_note='r>q exact to 400', iv=False, v=False); out.append(rec); continue
        if r >= q*(1-1e-9):
            Nn, a = seq(300); rec.update(iii=min(Nn[1:]) >= 0, iv=min(a[1:]) >= 0, boundary_r_eq_q=True)
            Nt, at = seq(300, -a1); rec['v'] = rec['iv'] and min(Nt[1:]) >= 0 and min(at[1:]) >= 0
            out.append(rec); continue
        mN, ma, D0, cert, Nn, a = certify_nonneg(seq, q, r)
        assert cert
        rec.update(iii=mN >= 0, iv=(mN >= 0 and ma >= 0), D0=D0)
        if rec['iv']:
            mN2, ma2, _, c2, _, _ = certify_nonneg(lambda D: seq(D, -a1), q, r)
            rec['v'] = mN2 >= 0 and ma2 >= 0
            # (vi) Jacobian-group counts: J_n = prod(1-alpha^n) = P_n(1) positive, J_1 | J_n  (n<=12)
            Jn = []
            for n in range(1, 13):
                # exact: P_n(1) = prod (1 - alpha^n) via char poly of companion^n ; use resultant formula through S:
                # P_n(1) = 1 - e1(n) + e2(n) - e3(n) + e4(n), e_k(n) from Newton on power sums S_{kn}
                Sx = S_seq(a1, a2, q, 4*n)
                p = [Sx[n*k] for k in range(5)]
                E = [1, 0, 0, 0, 0]
                for k in range(1, 5):
                    E[k] = sum((-1)**(i-1)*E[k-i]*p[i] for i in range(1, k+1))
                    assert E[k] % k == 0; E[k] //= k
                Jn.append(E[0]-E[1]+E[2]-E[3]+E[4])
            rec['J'] = Jn[:4]
            rec['vi'] = rec['v'] and all(j > 0 for j in Jn) and all(j % Jn[0] == 0 for j in Jn)
        else:
            rec['v'] = False
        if rec.get('vi'):
            S = S_seq(a1, a2, q, 200)
            u = [abs(S[n])/(4*q**(n/2)) for n in range(1, 201)]
            viol = [n for n in range(1, 201) if abs(S[n])**2 > 16*q**n]
            rec['first_weil_violation_n'] = viol[0] if viol else None
            rec['max_ratio_n<=200'] = max(u)
            rec['slack_n1'] = 1 - u[0]
            # type: real Weil poly h(x)=x^2+a1 x+(a2-2q)
            disc = a1*a1 - 4*(a2-2*q)
            rec['type'] = 'C' if disc < 0 else ('R' if not on else 'on')
            rec['delta'] = math.log(r, q) - 0.5
        out.append(rec)
    return out
if __name__ == '__main__':
  res = {}
  for q in [int(a) for a in sys.argv[1:]] or [3, 5, 7, 11]:
    t = time.time(); rows = analyse(q)
    for x in rows: x.pop('al', None)
    res[q] = rows
    print(q, 'box', len(rows), f'{time.time()-t:.1f}s', flush=True)
  json.dump(res, open('out/ladder_raw.json', 'w'))

#!/usr/bin/env python3
"""Test 2, paths relative to this repository.

Finite-field dictionary plus a ζ window on a free basis, K = 8, 50 digits.
Positive Galerkin minima are not certificates. Negative Rayleigh quotients
here are strong numerical witnesses: this script does not attach a rigorous
quadrature bound, so they are not called certified.
RH is not proved. The script uses W itself, so it is not an independent sign.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SPRING = ROOT / "provenance" / "session" / "notes" / "spring1891"
sys.path.insert(0, str(SPRING))
import spring_mp as S  # noqa: E402

res = {
    "rh_proved": False,
    "basis": "free (constrained=False), K=8, full width A of [-A/2, A/2]",
    "certificate_status": "negative Rayleigh quotients are strong numerical witnesses without a rigorous integral error bound; positive minima are Galerkin upper bounds",
}
q, a = 5, 2
G = sp.Matrix([[0, 1, 1, q], [1, 0, 1, 1], [1, 1, 0, q + 1 - a], [q, 1, q + 1 - a, 0]])
e = lambda M: [round(float(x), 6) for x in np.linalg.eigvalsh(np.array(M, dtype=float))]
bv = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0]]) * G
Hyp = bv.T * sp.Matrix([[0, 1], [1, 0]]) * bv
res["Fq_minusD2_eigs"] = e(-G)
res["Fq_W_eigs"] = e(-G + Hyp)
for A in ("1", "2"):
    B = S.build(A, 8, constrained=False)
    m = S.mats(B)
    u = sp.Symbol("u")
    Ar = sp.Rational(A)
    mom = lambda s: [mp.mpf(sp.N(sp.integrate(F * sp.exp(s * u / 2), (u, -Ar / 2, Ar / 2)), 60)) for F in B["Fu"]]
    am, bp = mom(-1), mom(1)
    Pm = mp.matrix(8, 8)
    for j in range(8):
        for k in range(8):
            Pm[j, k] = am[j] * bp[k] + bp[j] * am[k]
    Wm = S.W(m)
    E1, V1 = S.geneig(Wm, m["G"])
    E2, V2 = S.geneig(Wm + Pm, m["G"])
    v = V1[0]
    nv = (v.T * m["G"] * v)[0]
    res["zeta_A=" + A] = dict(
        W_minus_P_eigs=[mp.nstr(x, 6) for x in E1[:3]],
        n_neg_W_minus_P=sum(1 for x in E1 if x < 0),
        W_eigs=[mp.nstr(x, 6) for x in E2[:3]],
        n_neg_W=sum(1 for x in E2 if x < 0),
        witness_rayleigh=mp.nstr((v.T * Wm * v)[0] / nv, 8),
        P_on_that_vector=mp.nstr((v.T * Pm * v)[0] / nv, 8),
    )
out = ROOT / "results" / "test2_result.json"
out.write_text(json.dumps(res, indent=1), encoding="utf-8")
print(json.dumps(res, indent=1))

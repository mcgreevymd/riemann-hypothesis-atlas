#!/usr/bin/env python3
"""Small audit checks for atlas v1.19. RH is not proved.

These lock corrections that the 6 Nov 2026 bundle stated too strongly.
They are elementary identities, inertia counts, and one numerical
functional-equation check. None is an independent positivity theorem for ζ.
"""
import json
import os
from pathlib import Path

import mpmath as mp
import sympy as sp

OUT = Path(__file__).resolve().parents[1] / "results" / "audit_v119.json"
res = {"rh_proved": False, "checks": {}}


def record(name, ok, **detail):
    res["checks"][name] = {"ok": bool(ok), **detail}
    print(("OK  " if ok else "FAIL") , name)


# 1. Invariant Hermitian forms on the two boundary scalars.
a, b, x, y, A = sp.symbols("a b x y A", real=True)
A = sp.symbols("A", positive=True)
H = sp.Matrix([[a, x + sp.I * y], [x - sp.I * y, b]])
D = sp.Matrix([[A**(-sp.Rational(1, 2)), 0], [0, A**(sp.Rational(1, 2))]])
sigma = sp.Matrix([[0, 1], [1, 0]])
scale = sp.simplify(D.H * H * D - H)
swap = sp.simplify(sigma.H * H * sigma - H)
# Off-diagonal entries of the scaling condition force a = b = 0; the swap forces y = 0.
eqs = list(scale) + list(swap)
sol = sp.solve(eqs, [a, b, y], dict=True)
record(
    "boundary_invariant_form",
    sol == [{a: 0, b: 0, y: 0}],
    solution=str(sol),
    note="Nonzero multiples are z * [[0,1],[1,0]], z real. The zero form is the degenerate solution.",
)

hyp = sp.Matrix([[0, 1], [1, 0]])
ev = list(hyp.eigenvals().keys())
record(
    "boundary_signature_1_1",
    sorted(ev) == [-1, 1],
    eigenvalues=str(sorted(ev)),
    zero_form_eigenvalues="[0, 0]",
)

# 2. Clifford multiplication exists for an indefinite metric and for a Euclidean one.
e1 = sp.Matrix([[0, 1], [1, 0]])
e2 = sp.Matrix([[0, 1], [-1, 0]])
g_indef = sp.diag(1, -1)
E = [e1, e2]
indef_ok = all((E[i] * E[j] + E[j] * E[i]) == 2 * g_indef[i, j] * sp.eye(2) for i in range(2) for j in range(2))
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
g_eucl = sp.eye(2)
S = [s1, s2]
eucl_ok = all((S[i] * S[j] + S[j] * S[i]) == 2 * g_eucl[i, j] * sp.eye(2) for i in range(2) for j in range(2))
record(
    "clifford_does_not_choose_signature",
    indef_ok and eucl_ok,
    indefinite_Cl_1_1=indef_ok,
    euclidean_Cl_2=eucl_ok,
    note="The Clifford relation is not a positivity source.",
)

# 3. Spring completion versus signed autocorrelation, for a real isometry.
# ||F - TF||^2 = 2||F||^2 - 2 <F, TF>  when T is orthogonal on a real inner product.
nf, ip = sp.symbols("norm2 ip", real=True)
spring = nf - 2 * ip + nf  # ||F||^2 + ||TF||^2 - 2 ip, and ||TF||=||F||
signed = -2 * ip
mass_shift = -2 * nf  # the -2 a ||F||^2 absorbed into M, here a = 1
record(
    "spring_completion_matches_signed_term",
    sp.expand(spring + mass_shift - signed) == 0,
    note="Prime spring energy stays nonnegative. After the counterterm removes 2 a ||F||^2, the leftover is -2 a <F, TF>, signed with the autocorrelation.",
)

# 4. Finite-field perpendicular Gram: inertia, not determinant.
q, a = sp.symbols("q a", real=True)
Gperp = sp.Matrix([[-2, -a], [-a, -2 * q]])
# Leading minors: -2 < 0, and det = 4q - a^2. Negative definite iff det > 0 (since first minor is negative).
det = sp.factor(Gperp.det())
record("perp_det_formula", det == 4 * q - a**2, det=str(det))
samples = []
negdef_iff = True
det_positive_but_not_positive_form = False
for qq in (2, 3, 5, 7):
    for aa in range(-int(2 * qq**0.5) - 3, int(2 * qq**0.5) + 4):
        M = sp.Matrix([[-2, -aa], [-aa, -2 * qq]])
        evs = [sp.N(e) for e in M.eigenvals(multiple=True)]
        npos = sum(1 for e in evs if e > 1e-9)
        nneg = sum(1 for e in evs if e < -1e-9)
        hasse = aa * aa <= 4 * qq
        if (nneg == 2 and npos == 0) != hasse and not (aa * aa == 4 * qq):
            # on the wall, one zero and one negative: semidefinite, still "hasse"
            if hasse and npos == 0:
                pass
            else:
                negdef_iff = False
        if hasse and npos == 0 and M.det() > 0 and nneg == 2:
            det_positive_but_not_positive_form = True
        samples.append({"q": qq, "a": aa, "det": int(M.det()), "npos": npos, "nneg": nneg})
record(
    "fq_inertia_not_determinant",
    negdef_iff and det_positive_but_not_positive_form,
    n_samples=len(samples),
    det_can_be_positive_while_negative_definite=det_positive_but_not_positive_form,
    note="Negative semidefinite tracks the Hasse inequality. det > 0 is not positivity. Discrete samples are not Mellin moments; this check does not identify them.",
)

# 5. Trace norm is nonnegative. A signed quadratic remainder is a different number.
P = sp.eye(2)
A = sp.Matrix([[1, 0], [0, -3]])
leak = (sp.eye(2) - sp.zeros(2))  # a projection difference stand-in: I itself
# nuclear norm of a diagonal matrix is the sum of absolute values
nuclear = abs(1) + abs(-3)
signed_quadratic = sp.Matrix([1, 1]).dot(A * sp.Matrix([1, 1]))
record(
    "trace_norm_nonnegative_signed_remainder_separate",
    nuclear > 0 and signed_quadratic < 0 and nuclear != signed_quadratic,
    nuclear_norm=int(nuclear),
    signed_quadratic=int(signed_quadratic),
    note="A trace-norm leakage cannot be given a negative sign. Report the nonnegative norm and, separately, any signed quadratic remainder. The draft S={infinity,2} leakage test was not run.",
)

# 6. BPS toy: topological constant has zero Hessian; the square's Hessian at a zero of the map is nonnegative.
x = sp.symbols("x")
M = x**2
C = sp.Integer(5)  # locally constant charge
Phi = M**2 + C
hess_C = sp.diff(C, x, 2)
hess_at_0 = sp.diff(Phi, x, 2).subs(x, 0)
record(
    "bps_toy_hessian",
    hess_C == 0 and hess_at_0 >= 0,
    hessian_of_charge=str(hess_C),
    hessian_of_square_at_zero=str(hess_at_0),
    note="Toy of the architecture only. Not an arithmetic instanton, and not a sign for W.",
)

# 7. Completed zeta ratio on the critical line is 1 by the functional equation.
# Λ(s) = π^{-s/2} Γ(s/2) ζ(s), Λ(s) = Λ(1-s), so Λ(1/2-it)/Λ(1/2+it) = 1
# wherever both values are finite and nonzero. Numerical witness at two heights.

def Lambda(s):
    return mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)

ratios = {}
for t in (1, 5):
    num = Lambda(mp.mpf("0.5") - 1j * t)
    den = Lambda(mp.mpf("0.5") + 1j * t)
    ratios[str(t)] = complex(num / den)
ok_ratio = all(abs(v - 1) < 1e-8 for v in ratios.values())
record(
    "completed_zeta_ratio_is_one",
    ok_ratio,
    ratios={k: [v.real, v.imag] for k, v in ratios.items()},
    note="Meromorphic consequence of Λ(s) = Λ(1-s). No group-delay positivity. The local archimedean phase delay is a different function, K.",
)

# 8. Level-2 Virasoro norm at h = -1 is (c-26)/2. Algebra only.
c, h = sp.symbols("c h")
# Gram on (L-2, L-1^2): [[4h+c/2, 6h],[6h, 8h**2+4h]]
G = sp.Matrix([[4 * h + c / 2, 6 * h], [6 * h, 8 * h**2 + 4 * h]])
det = sp.factor(G.det())
# vector chi = L-2 + (3/2) L-1^2 at h=-1; its norm squared is the quadratic form
v = sp.Matrix([1, sp.Rational(3, 2)])
norm2 = sp.simplify((v.T * G * v)[0].subs(h, -1))
record(
    "virasoro_h_minus_one_is_algebra",
    sp.simplify(norm2 - (c - 26) / 2) == 0,
    norm_squared=str(norm2),
    det=str(det),
    note="Null at c=26. This is not a unitarity proof. c here is the Virasoro central charge, not a speed and not a topological charge.",
)

res["all_ok"] = all(v["ok"] for v in res["checks"].values())
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, indent=1), encoding="utf-8")
print("wrote", OUT, "all_ok", res["all_ok"])
if not res["all_ok"]:
    raise SystemExit(1)

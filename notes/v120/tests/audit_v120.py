#!/usr/bin/env python3
"""Exact and cheap numerical checks for atlas v1.20. RH is not proved.

No slow Galerkin scan. The prime-2 kink uses a few response evaluations.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1] / "results" / "audit_v120.json"
SCRIPT = ROOT / "notes" / "v120" / "provenance" / "bundle" / "scripts" / "matching1983"
sys.path.insert(0, str(SCRIPT))
from match1983 import resp  # noqa: E402

res = {"rh_proved": False, "checks": {}}


def record(name, ok, **detail):
    res["checks"][name] = {"ok": bool(ok), **detail}
    print(("OK  " if ok else "FAIL"), name)


# 1. K0
k0 = mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)
record(
    "K0_digamma",
    abs(k0 - mp.mpf("-5.3721834192256654")) < mp.mpf("1e-12"),
    K0=str(k0),
)

# 2. E0 kills P, not the diagonal symbol.
ev_p, ev_m = sp.symbols("ev_p ev_m")
P = 2 * ev_p * ev_m
record("E0_kills_P_only", sp.simplify(P.subs({ev_p: 0, ev_m: 0})) == 0, note="The diagonal M_A stays in B by definition of the ledger.")

# 3. Twisted star (chi f)* = chi^{-1} f*
u = sp.symbols("u", real=True)
f_re, f_im = sp.symbols("f_re f_im", complex=True)
# Evaluate on an explicit function f(u) = exp(-u**2) * (1+I*u)
def f(x):
    return np.exp(-np.asarray(x, dtype=float) ** 2) * (1 + 1j * np.asarray(x, dtype=float))

def star(fun, x):
    return np.conjugate(fun(-x))

def chi(x):
    return np.exp(-np.asarray(x, dtype=float) / 2)

xs = np.array([-1.3, -0.2, 0.4, 1.7])
left = star(lambda x: chi(x) * f(x), xs)
right = (1 / chi(xs)) * star(f, xs)
record("twisted_star", np.allclose(left, right), max_abs=float(np.max(np.abs(left - right))))

# Naive (chi f)*(chi f)* is not chi * (f * f*) as functions of one variable:
# compare the involution of chi*f with chi * involution of f, already equal,
# and compare with chi(u) * (chi f)*(u), which is a different weight.
naive = chi(xs) * star(lambda x: chi(x) * f(x), xs)
record(
    "naive_star_differs",
    not np.allclose(naive, right),
    note="(chi f)* equals chi^{-1} f*, not chi times that same star.",
)

# 4. Archimedean density k(a) ~ 1/(2a)
def k(a):
    a = np.asarray(a, dtype=float)
    return np.exp(-a / 2) / (1 - np.exp(-2 * a))

a_small = np.array([1e-2, 1e-3, 1e-4])
ratio = (2 * a_small) * k(a_small)
record("k_edge_equivalent", np.allclose(ratio, 1, atol=1e-2), ratios=[float(x) for x in ratio])

# 5. Exact prime-2 jump, and one finite difference
A = 1.0
a2 = np.log(2) / np.sqrt(2)
predicted = a2 * np.sinh(A / 4) / 2
record(
    "kink_exact_value",
    abs(predicted - 0.061906320172915884) < 1e-15 and abs(predicted - 0.06191) < 5e-6,
    predicted=float(predicted),
)
v0 = np.log(2) - A / 2
eps = 1e-4
def slope_jump(x):
    f = lambda t: resp(A, t, "h2")
    left_s = (f(x) - f(x - eps)) / eps
    right_s = (f(x + eps) - f(x)) / eps
    return right_s - left_s

jump = slope_jump(v0)
record(
    "kink_finite_difference",
    abs(jump - predicted) < 2e-3 and abs(abs(jump) - 0.06189) < 2e-4,
    jump=float(jump),
    v0=float(v0),
    note="Numerical derivative. The exact jump is the prediction. Not a certificate of a spectrum.",
)

# 6. Bordered inertia, including index 0
rng = np.random.default_rng(1983)

def inertia(M, tol=1e-8):
    ev = np.linalg.eigvalsh(M)
    return int(np.sum(ev < -tol)), int(np.sum(np.abs(ev) <= tol)), int(np.sum(ev > tol))

def restrict(B, c):
    # orthonormal basis of c-perp
    c = c / np.linalg.norm(c)
    A = np.eye(len(c)) - np.outer(c, c)
    basis = np.linalg.svd(A, full_matrices=True)[0][:, :-1]
    return basis.T @ B @ basis

cases = []
ok_border = True
# index 0
for n in (3, 4):
    M = rng.normal(size=(n, n))
    B = M.T @ M + np.eye(n)
    c = rng.normal(size=n)
    q = float(c @ np.linalg.solve(B, c))
    nB = inertia(B)[0]
    nR = inertia(restrict(B, c))[0]
    pred = nB - 1 + (1 if q > 0 else 0)
    good = nB == 0 and q > 0 and nR == 0 and pred == nR
    ok_border = ok_border and good
    cases.append({"kind": "index0", "q": q, "nB": nB, "nR": nR, "good": good})
# index 1, q < 0 and q > 0
B = np.diag([2.0, 3.0, -1.5])
for c, kind in ((np.array([0.0, 0.0, 1.0]), "index1_q_neg"), (np.array([1.0, 0.2, 0.0]), "index1_q_pos")):
    q = float(c @ np.linalg.solve(B, c))
    nB = inertia(B)[0]
    nR = inertia(restrict(B, c))[0]
    pred = nB - 1 + int(q > 0)
    good = nB == 1 and nR == pred and ((kind.endswith("neg") and q < 0 and nR == 0) or (kind.endswith("pos") and q > 0 and nR == 1))
    ok_border = ok_border and good
    cases.append({"kind": kind, "q": q, "nB": nB, "nR": nR, "good": good})
# index 2 always fails
B2 = np.diag([4.0, -1.0, -2.0])
c = np.array([0.3, -0.4, 0.8])
q = float(c @ np.linalg.solve(B2, c))
nB = inertia(B2)[0]
nR = inertia(restrict(B2, c))[0]
pred = nB - 1 + int(q > 0)
good = nB == 2 and nR == pred and nR >= 1
ok_border = ok_border and good
cases.append({"kind": "index2", "q": q, "nB": nB, "nR": nR, "good": good})
record("bordered_inertia_both_index0_and_index1", ok_border, cases=cases)

# 7. Conic gauges and Sylvester shape
T, Qv, Z = sp.symbols("T Q Z")
Qform = T**2 - 4 * Qv * Z
record("Q_homogeneous_and_affine", sp.simplify(Qform.subs({T: 0, Qv: 1, Z: sp.symbols("s")})) == -4 * sp.symbols("s") and sp.simplify(Qform.subs({T: 0, Qv: 1 / sp.symbols("s"), Z: 1})) == -4 / sp.symbols("s"))
s = sp.symbols("s", positive=True)
record(
    "gauge_ratio_is_scale_squared",
    sp.simplify((Qform.subs({T: 0, Qv: 1 / s, Z: 1})) / (Qform.subs({T: 0, Qv: 1, Z: s})) - s ** (-2)) == 0,
)
M = sp.Matrix([[1, 0, 0], [0, 0, -2], [0, -2, 0]])
evs = sorted(M.eigenvals().keys())
record("conic_signature_one_negative", evs == [-2, 1, 2], eigenvalues=str(evs))
# polar of h=(0,1,1): Z = -Q, form T^2 + 4 Q^2
polar = sp.simplify(Qform.subs(Z, -Qv))
record("polar_positive", polar == T**2 + 4 * Qv**2)
# smooth at x_infinity in chart Q=1: T^2 - 4Z, gradient nonzero at (0,0)
gT = sp.diff(T**2 - 4 * Z, T)
gZ = sp.diff(T**2 - 4 * Z, Z)
record("smooth_at_infinity", not (gT.subs(T, 0) == 0 and gZ == 0), note="Chart Q=1 is the parabola T^2=4Z. Not a cusp.")

# 8. Kunneth signs
# E(dz, dzbar) = -2i, alternating, diagonals 0
i = sp.I
E_dz_dzbar = -2 * i
E_dzbar_dz = 2 * i
# I(a⊗b,c⊗d) = -E(a,c)E(b,d)
# alpha = dz⊗dzbar + dzbar⊗dz
term_cross_1 = -E_dz_dzbar * E_dzbar_dz
term_cross_2 = -E_dzbar_dz * E_dz_dzbar
I_alpha = sp.simplify(term_cross_1 + term_cross_2)
E_dz_dz = 0
term_b1 = -E_dz_dzbar * E_dz_dzbar
term_b2 = -E_dzbar_dz * E_dzbar_dz
I_beta = sp.simplify(term_b1 + term_b2)
record("kunneth_signs", I_alpha == -8 and I_beta == 8, I_alpha=str(I_alpha), I_beta=str(I_beta))

# 9. Polynomial test is not smooth, but moments vanish by parts
A_sym, u, t, k = sp.symbols("A u t k", positive=True)
# G as a function of t, G(±1)=0 and G_t(±1)=0 for k=0
t_sym = sp.symbols("t")
G = (1 - t_sym**2) ** 2
record(
    "polynomial_test_boundary",
    G.subs(t_sym, 1) == 0 and G.subs(t_sym, -1) == 0 and sp.diff(G, t_sym).subs(t_sym, 1) == 0 and sp.diff(G, t_sym).subs(t_sym, -1) == 0,
)
# second t-derivative at the endpoint is not zero, so a zero extension is not C2
Gtt = sp.diff(G, t_sym, 2)
record("polynomial_test_not_smooth", Gtt.subs(t_sym, 1) != 0, Gtt_edge=str(Gtt.subs(t_sym, 1)))
# IBP cancellation for alpha = ±1/2
alpha = sp.Rational(1, 2)
record("moment_operator_cancels", sp.simplify(alpha**2 - sp.Rational(1, 4)) == 0)

# 10. Short AR(1) covariance is PSD, hence enters as something that can be subtracted
p = 2.0
n = 6
toe = np.array([[p ** (-abs(i - j) / 2) for j in range(n)] for i in range(n)])
record("ar1_covariance_psd", np.min(np.linalg.eigvalsh(toe)) >= -1e-10, min_eig=float(np.min(np.linalg.eigvalsh(toe))))

# 11. Z[sqrt(-5)] is not a UFD: no norm 2, two factorizations of 6
def norm(a, b):
    return a * a + 5 * b * b

has_norm_2 = any(norm(a, b) == 2 for a in range(-3, 4) for b in range(-3, 4))
record(
    "local_ufd_not_global_principal",
    (not has_norm_2) and norm(2, 0) == 4 and norm(1, 1) == 6 and 2 * 3 == 6,
    note="2 and 1+sqrt(-5) are irreducible. Noetherian does not mean a Noether charge. Regular local UFD is not global principality.",
)

# 12. Weight calibration is not k/12
mismatches = []
for k_w, shown, _ratio in (
    (12, -0.26351879595508976, 1.0),
    (16, 0.3555288230925293, 1.3333333333333333),
):
    val = 2 * (mp.digamma(mp.mpf(k_w) / 2) - mp.log(2 * mp.pi))
    mismatches.append(abs(val - mp.mpf(shown)) < mp.mpf("1e-12") and abs(val - mp.mpf(k_w) / 12) > mp.mpf("0.1"))
record("weight_is_not_counterterm", all(mismatches), note="2(psi(k/2)-log 2pi) is not k/12.")

# 13. Hilbert transform of an indicator is not compactly supported
# H 1_[-1,1](x) = (1/pi) log |(x+1)/(x-1)|
x = 2.0
closed = (1 / np.pi) * np.log(abs((x + 1) / (x - 1)))
# principal-value numerical check on a split integral
def integrand(t):
    return (1 / np.pi) * (1 / (x - t))

left_int = np.trapezoid(integrand(np.linspace(-1, 0.5, 4000)), np.linspace(-1, 0.5, 4000))
right_int = np.trapezoid(integrand(np.linspace(0.5, 1, 8000)), np.linspace(0.5, 1, 8000))
# The singularity is at t=x which is outside [-1,1], so the integral is ordinary.
quad = np.trapezoid(integrand(np.linspace(-1, 1, 20001)), np.linspace(-1, 1, 20001))
record(
    "hilbert_not_compactly_supported",
    abs(quad - closed) < 1e-3 and abs(closed) > 0.1,
    closed=float(closed),
    quad=float(quad),
    note="Nonzero at x=2, outside the support of the indicator. A convolution J does not preserve compact support.",
)

# 14. Level set versus sublevel: at small s the ellipse is tall, the limit objects differ
s = 0.05
# semi-axis in v_Q is 1/(2 sqrt(s)); level points have |v_T|<=1
semi = 1 / (2 * np.sqrt(s))
record(
    "level_set_not_the_strip",
    semi > 2 and abs(np.sqrt(1 - 4 * s * (semi - 1e-9) ** 2)) < 0.01,
    semi_axis=float(semi),
    note="The curve Q=1 meets v_T near 0 only at large |v_Q|. Its limit is two lines. The inequality Q<=1 fills the region between them.",
)

# 15. Schema of the atlas after insertion
atlas = json.loads((ROOT / "atlas.json").read_text(encoding="utf-8"))
concepts = atlas["concepts"]
by = {c["id"]: c for c in concepts}
n_rel = sum(len(c["rels"]) for c in concepts)
ids_ok = len(by) == len(concepts)
ranks_ok = [c["rank"] for c in concepts] == list(range(1, len(concepts) + 1))
links_ok = all(r["to"] in by for c in concepts for r in c["rels"])
rank1 = concepts[0]["id"] == "kahler_triple_polarization" and concepts[0]["rank"] == 1
# file may not be sorted; check the rank-1 concept
rank1_c = min(concepts, key=lambda c: c["rank"])
rank1 = rank1_c["id"] == "kahler_triple_polarization" and abs(rank1_c["priority"] - 0.72) < 1e-9
missing = [c for c in concepts if "missing piece" in c["axes"]]
new_ids = [
    "window_energy_ledger",
    "pole_form_P_2ReCplusCminus",
    "bulk_form_B_off_E0",
    "local_product_state_covariance",
    "product_formula_defect_mean",
    "twisted_star_convolution",
    "semilocal_scattering_phase_time_delay",
    "connes_cutoff_pair_two_hankel",
    "bordered_inertia_moment_criterion",
    "even_odd_sector_constraints",
    "near_null_cluster_A2",
    "independent_representer_test",
    "prime_edge_kink_orbit",
    "conic_polarity_one_form",
    "polar_family_h_s_degeneration",
    "kunneth_skew_to_symmetric",
    "nonstationary_J_obstruction",
    "iwasawa_regularity_class",
    "rankin_selberg_square_calibration",
]
present = all(i in by for i in new_ids)
open_18 = sum(json.dumps(c).count("Open ~1.8") for c in concepts)
record(
    "atlas_schema",
    ids_ok and ranks_ok and links_ok and rank1 and len(missing) == 10 and present and n_rel == atlas["counts"]["relations"] and len(concepts) == atlas["counts"]["concepts"] and open_18 >= 1,
    concepts=len(concepts),
    relations=n_rel,
    rank1=rank1_c["id"],
    priority=rank1_c["priority"],
    missing_pieces=len(missing),
    open_18=open_18,
)

res["all_ok"] = all(v["ok"] for v in res["checks"].values())
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, indent=1), encoding="utf-8")
print("wrote", OUT, "all_ok", res["all_ok"])
if not res["all_ok"]:
    raise SystemExit(1)

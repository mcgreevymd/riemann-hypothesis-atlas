#!/usr/bin/env python3
"""Apply the aligned-bundle and manuscript-audit wording to existing v1.20 nodes.

Does not recompute priorities, ranks, or the set of concepts.
"""
import json
from pathlib import Path

ATLAS = Path(__file__).resolve().parents[2] / "atlas.json"
data = json.loads(ATLAS.read_text(encoding="utf-8"))
by = {c["id"]: c for c in data["concepts"]}
before = {c["id"]: (c["priority"], c["rank"]) for c in data["concepts"]}


def set_fields(cid, **fields):
    c = by[cid]
    for k, v in fields.items():
        c[k] = v


set_fields(
    "product_formula_defect_mean",
    name="The counterterm adds local mean statistics; it is not a global idele coupling",
    aliases=["local means of log modulus", "capped prime-power mean"],
    plain="M_A is a sum of separate local means, one place at a time. There is no coupling on principal ideles in this identity, so it is not a proved product-formula defect. If the prime sum runs over all prime powers inside the cutoff, the capped mean is a sum over those primes, not a one-prime expression.",
    core="Each place contributes its own truncated expectation of log |x|_v. The archimedean mean is K0 = psi(1/4) - log pi. For the primes, a_n = Lambda(n) n^(-1/2) already sums prime powers. Written as a Gibbs capped mean over every prime power with k log p < A, the diagonal is 2 times the sum over p < exp(A) of the local mean of log p times min(N_p, K_p(A)). A formula that shows only one p on the right-hand side does not match a sum over all such prime powers. The classical product formula, product over places of |x|_v = 1, is a different statement. It is not a coupling that has been constructed on principal ideles, and it is not the source of the sign.",
    formula="M_A = -K0 + 2 sum_{log n < A} a_n = -2 sum_v (local mean_v); prime part sums over p",
    pitfalls=[
        "Do not call this a proved product-formula defect.",
        "No global idele coupling is claimed.",
        "A single-prime right-hand side is the wrong way to write the sum over all prime powers.",
    ],
)

set_fields(
    "bulk_form_B_off_E0",
    core="B(F) = H_A(F) - M_A ||F||^2 = (1/2 pi) integral m_A(x) |Fourier F(x)|^2 dx, with m_A the archimedean symbol minus the cosine sum over log n < A. Do not infer infinite rank from unboundedness alone: a finite-rank form made of unbounded linear functionals can be unbounded. The corrected reason uses high frequency. Re psi(1/4 + i x/2) tends to +infinity, while the prime cosine sum is bounded by 2 sum a_n, so some X has m_A(x) at least 1 for |x| at least X. Then B(F) is at least ||F||^2 minus (1+M_A) times the form of the compact time-band-limiting operator K_X, the window compression of the Fourier cutoff |frequency| < X. On the closed finite-codimension subspace where K_X is smaller than 1/(2(1+M_A)), B is at least half the norm squared. That subspace meets smooth E0 on the window in an infinite-dimensional set. So on E0, where W equals B, the form is positive definite on an infinite-dimensional subspace. A map into a finite-dimensional V whose pulled-back pairing equals W would vanish on a kernel of codimension at most dim V, and that kernel would meet the positive subspace. A fixed finite H^{1,1} cannot carry W. The same estimate says B has only finitely many negative directions on one window. That is an analytic description of one window. It is not Weil positivity, and it is not a claim that the form is close to being positive. The geometric target of the right size is not constructed.",
    pitfalls=[
        "Do not write unbounded, therefore not finite rank.",
        "Finitely many negative directions on one window is not a sign theorem.",
        "B inverse applied to the constraint is not an independent constructor, and the infinite-dimensional domain is unproved.",
    ],
)
for rel in by["bulk_form_B_off_E0"]["rels"]:
    if rel["to"] == "mp_d8":
        rel["note"] = "a fixed finite H^{1,1} cannot carry W, by the high-frequency band-limit; unboundedness alone is not the reason; nothing here constructs a replacement"

set_fields(
    "even_odd_sector_constraints",
    plain="On a reflection-invariant finite Galerkin space whose even and odd blocks are invertible, B is positive semidefinite on E0 exactly when each sector passes the bordered test: negative index 0, or negative index 1 with q at most 0. The even test alone is not E0. The odd index seen in two runs is numerical.",
    core="For an R-invariant finite Galerkin space with invertible sector blocks, B is at least 0 on E0(I) if and only if [n-(B_even) = 0, or n-(B_even) = 1 and q_even <= 0] and [n-(B_odd) = 0, or n-(B_odd) = 1 and q_odd <= 0]. This is the parent audit's Lemma 2. The reflection RF(u) = F(-u) commutes with B, because the symbol is even, and it commutes with P. Cosh is the even constraint and sinh is the odd constraint. In the A = 0.6 and A = 1 runs the odd block had negative index 0. That is numerical, not a general fact. Full-window W is a different question: if the even block has index 1 and is invertible, W_even is positive semidefinite if and only if q_even <= -1/2. If the odd block is positive definite, W_odd is positive semidefinite if and only if q_odd <= 1/2.",
    formula="B >= 0 on E0 iff both sectors pass: index 0, or index 1 and q <= 0",
)

nums = by["bordered_inertia_moment_criterion"]["numbers"]
by["bordered_inertia_moment_criterion"]["numbers"] = [
    "Session |cosine| between cosh and a computed even mode, not a squared overlap: about 0.970 at A = 0.6, 0.991 at A = 1, and 0.997 at A = 2. The width-2 figure sits in the unresolved cluster and is not an eigenvalue.",
    "E0 minima are estimates, not certified brackets. Ritz upper estimates about 0.697 at A = 0.6 and 0.01315 at A = 1. Lower-bound-inspired values about 0.6919 and 0.0119. No interval is certified.",
    "A = 2 is unresolved. Do not quote a second eigenvalue as certified.",
]
by["bordered_inertia_moment_criterion"]["pitfalls"] = [
    p for p in by["bordered_inertia_moment_criterion"]["pitfalls"]
    if "0.6918" not in p
] + [
    "Do not draw the Ritz value and the lower-bound-inspired value as the ends of a certified bracket.",
]

by["near_null_cluster_A2"]["numbers"] = [
    "Do not quote either cluster as spec(B).",
    "|cosine| 0.970, 0.991, and 0.997, and the E0 estimates at A = 0.6 and A = 1, are uncertified. They are not squared overlaps and not brackets.",
]
by["near_null_cluster_A2"]["core"] = by["near_null_cluster_A2"]["core"].replace(
    "Finite positive Galerkin values remain upper bounds on minima when they come from a Rayleigh-Ritz projection. They are not analytic positivity.",
    "Finite positive Galerkin values remain upper bounds on minima when they come from a Rayleigh-Ritz projection. They are not analytic positivity. Calling a Ritz value and a tail estimate a bracket overstates what was proved.",
)

core = by["independent_representer_test"]["core"]
old = "h1 = cosh(u/2) times the window indicator fails at A = 0.6 and at A = 1 because the response over cosh blows up at the edge like (1/2) log(1/d). That mechanism is exact."
new = "h1 = cosh(u/2) times the window indicator fails at A = 0.6 and at A = 1. The proof splits the archimedean integral at a fixed small a0. The untruncated comparison with the smooth continuation cosh(u/2) diverges, because the Gamma integrand tends to -cosh(v/2) at infinity and cosh sits at the Gamma pole. From a0 to infinity the integrand stays bounded, since h1 is bounded and compactly supported. On the short interval the smooth piece is integrable and the missing translate produces (cosh(L/2)/2) log(1/d) plus a bounded term. The coefficient 1/2 is the one in that expansion. A refinement records a rise of about 0.689 to 0.691 per factor of four in d, against (1/2) log 4 = 0.693. The Jc/Js decomposition in the parent audit is the same split."
if old not in core:
    raise SystemExit("h1 sentence not found")
by["independent_representer_test"]["core"] = core.replace(old, new)
by["independent_representer_test"]["pitfalls"] = [
    "Only these two candidates are excluded. There is no universal Gamma-only no-go.",
    "Do not prove the h1 edge by an untruncated integral against the smooth continuation of cosh. That integral diverges. Split at a fixed small a0.",
    "Polynomial tests are piecewise and not smooth. A density argument from smooth E0 tests is not proved.",
    "B inverse c is not an independent constructor.",
    "Infinite-dimensional invertibility is unproved.",
    "The Riemann Hypothesis is not proved.",
]

by["conic_polarity_one_form"]["proved"] = (
    "The three-by-three algebra and Sylvester's law on that matrix. Nothing about zeta. "
    "The Hodge index, as a cited sign pattern and not as a constructor, is Hartshorne, Algebraic Geometry, GTM 52, Chapter V, Theorem 1.9. "
    "The harmonic-form sign is the Hodge-Riemann bilinear relations; a chapter-level pointer is Huybrechts, Complex Geometry, or Griffiths and Harris, Principles of Algebraic Geometry, Chapter 0. Those pages were not re-opened here. Wikipedia is not the source."
)
by["conic_polarity_one_form"]["plain"] = by["conic_polarity_one_form"]["plain"].replace(
    "That curve is a discriminant boundary of the model.",
    "That curve is the model discriminant conic.",
)

obs = " Observation, not a theorem: the OU rate 2j + 1/2 is the distance from 1/2 to the pole s = -2j of the archimedean Gamma factor. For j at least 1 those poles are cancelled in xi by the trivial zeros. The j = 0 pole at s = 0 survives in Lambda and is the moment removed by E0."
if "Observation, not a theorem" not in by["local_product_state_covariance"]["core"]:
    by["local_product_state_covariance"]["core"] += obs

for c in data["concepts"]:
    if before[c["id"]] != (c["priority"], c["rank"]):
        raise SystemExit("rank or priority moved for " + c["id"])
    blob = json.dumps(c, ensure_ascii=False)
    if "\\" in blob and c["id"] in {
        "product_formula_defect_mean",
        "bulk_form_B_off_E0",
        "even_odd_sector_constraints",
        "bordered_inertia_moment_criterion",
        "near_null_cluster_A2",
        "independent_representer_test",
        "conic_polarity_one_form",
        "local_product_state_covariance",
    }:
        raise SystemExit("backslash in " + c["id"])

text = json.dumps(data, indent=1, ensure_ascii=False)
if not text.endswith("\n"):
    text += "\n"
ATLAS.write_text(text, encoding="utf-8")
print("updated wording; counts", data["counts"])

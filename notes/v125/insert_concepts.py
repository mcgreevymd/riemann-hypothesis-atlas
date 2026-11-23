#!/usr/bin/env python3
"""Insert the two v1.25 concepts into atlas.json and append the approved
Einstein/Hagedorn sentence to the existing Bost–Connes / Hagedorn entries.

Baseline: 1113 concepts, 2266 relations, rank 1 kahler_triple_polarization,
Open ~1.8 present. Priorities and ranking blocks are copied from templates.
Rank is assigned here: existing relative order is unchanged, and new concepts
follow the existing block of the same priority (alphabetical by id inside
that new block).

No backslashes are allowed (build_public_md.py rejects them).
"""
import json
from collections import defaultdict
from pathlib import Path


def _has_backslash(obj):
    if isinstance(obj, str):
        return "\\" in obj
    if isinstance(obj, dict):
        return any(_has_backslash(v) for v in obj.values())
    if isinstance(obj, list):
        return any(_has_backslash(v) for v in obj)
    return False


ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "atlas.json"

# Approved sentence, used on existing Bost–Connes / Hagedorn entries.
EINSTEIN = (
    "Einstein's 1917 derivation of B₁₂ = B₂₁ (hence Planck's law from A/B "
    "coefficients plus Boltzmann statistics) uses the high-temperature limit "
    "ρ → ∞. The primon gas's thermal description ends at the Hagedorn point "
    "β_H = 1 (the pole of ζ), and the Weil form lives beyond it, on Re β = ½ "
    "(complex β). So the step that forces detailed balance in physics is "
    "unavailable for ζ; continuation past β = 1 runs through the functional "
    "equation, which Davenport–Heilbronn and Epstein zetas (e.g. Z_{x²+5y²}) share."
)

ADDING = [
    {
        "id": "einstein_hagedorn_bc",
        "name": (
            "Einstein's 1917 B₁₂ = B₂₁ step uses ρ → ∞, unavailable past the "
            "Hagedorn point β_H = 1; continuation to the Weil form at Re β = ½ "
            "runs through the functional equation, shared by Davenport–Heilbronn "
            "and Epstein zetas"
        ),
        "aliases": [],
        "plain": EINSTEIN + " [Exact]",
        "label": "Theorem",
        "core": EINSTEIN + " Sources: TAA research notes, 20–22 Nov 2026.",
        "formula": "",
        "numbers": [],
        "axes": ["structure/frame (Ax1)"],
        "uncertain": "",
        "proved": "",
        "tests": "",
        "pitfalls": [
            "The high-temperature step is a fact about Einstein 1917 and the Hagedorn point of ζ; it supplies no sign.",
            "RH is not proved.",
        ],
        "lemmas": [],
        "rels": [
            {"type": "related", "to": "hagedorn_bc", "note": "Hagedorn β_H = 1; Weil at β = ½"},
            {"type": "related", "to": "kms_bost_connes", "note": "Bost–Connes / primon-gas partition function"},
            {"type": "related", "to": "kms_half_kernel_not_response", "note": "KMS/primon entry at β = ½"},
            {"type": "related", "to": "davenport_heilbronn", "note": "functional equation shared past β = 1"},
            {"type": "related", "to": "epstein", "note": "functional equation shared past β = 1, e.g. Z_{x²+5y²}"},
        ],
        "priority": 0.325,
        "_template": "hagedorn_bc",
    },
    {
        "id": "constraint_dirac_framing_route",
        "name": (
            "Constraint/Dirac framing of Q is sign-neutral: the only "
            "multiplicativity-using constraint is the Euler-product filter and "
            "supplies no sign; anything beyond that is the missing square"
        ),
        "aliases": [],
        "plain": (
            "In the Lagrange/Dirac-constraint picture of Q (norm constraint ‖f‖² = 1, "
            "pole constraints f̂(0) = f̂(1) = 0 or ⟨f, cosh⟩ = 0, the pencil Q − λ·norm, "
            "Poisson brackets such as {xy, x²+y²} = 2(y²−x²)), every element is built "
            "from Q alone and is sign-neutral: Davenport–Heilbronn and Epstein zetas "
            "share it. Relative to Q the pole plane is already nondegenerate (1,1), "
            "i.e. a second-class pair, with no Euler product used; Q-orthogonal "
            "reduction of that plane gives index 1 only, not Q ≥ 0 on E0 (L194). The "
            "Hamiltonian J (rotation of the (x, y) plane) is not TARGET's J (a complex "
            "structure on ℋ compatible with ω); brackets with respect to TARGET's ω "
            "are undefined until piece (B) exists. The only multiplicativity-using "
            "constraint expressible here is simultaneous eigen-constraints for the "
            "commuting Hecke / scaling-by-p family; it rejects Z_{x²+5y²} = ½(ζ_K + "
            "L(s,χ)), K = ℚ(√−5), only because it is a sum of two Euler products, so "
            "it is the Euler-product filter (#884: selects pure modes) and supplies no "
            "sign (cf. L196: 𝔽_q fakes with Euler products fail Hodge index). Any "
            "sign-giving, prime-dependent constraint beyond this would have to encode "
            "finite-place intersection data, i.e. the missing square Spec ℤ × Spec ℤ."
        ),
        "label": "Restatement",
        "core": (
            "Every constraint built from Q is sign-neutral. The pole plane is already "
            "a nondegenerate (1,1) pair relative to Q, with no Euler product used. "
            "Q-orthogonal reduction gives index 1, not Q ≥ 0 on E0 (L194). The only "
            "multiplicativity-using constraint expressible here is the Hecke / "
            "scaling-by-p eigen-filter (#884), which selects pure modes and supplies "
            "no sign (L196). A sign-giving prime-dependent constraint would be the "
            "missing square. Sources: TAA research notes, 20–22 Nov 2026."
        ),
        "formula": "{xy, x²+y²} = 2(y²−x²)",
        "numbers": [],
        "axes": ["no-go / refuted", "physics analogue", "ghost-blind"],
        "uncertain": "",
        "proved": "",
        "tests": "",
        "pitfalls": [
            "The Hamiltonian J of the (x, y) plane is not TARGET's J on ℋ.",
            "Brackets with respect to TARGET's ω are undefined until piece (B) exists.",
            "Framing items are labelled as such; none supplies the sign.",
            "RH is not proved; Φ is not constructed; there is no Hodge-type sign.",
        ],
        "lemmas": ["L194", "L196"],
        "rels": [
            {"type": "related", "to": "closed_routes_t2271_2284", "note": "a further closed route"},
            {"type": "related", "to": "prime_torus_nonresonance", "note": "Euler-product filter #884; selects pure modes, no sign"},
            {"type": "related", "to": "missing_square_spec_z", "note": "a sign-giving prime-dependent constraint would be the square"},
            {"type": "related", "to": "cosh_ample_direction_weil_equivalence", "note": "Q-orthogonal reduction gives index 1, not Q ≥ 0 on E0 (L194)"},
            {"type": "related", "to": "haynsworth_pole_plane_split_windows", "note": "pole plane already nondegenerate (1,1) relative to Q"},
            {"type": "related", "to": "multiplicativity_filter_sort_2271", "note": "Euler-using steps supply no sign"},
            {"type": "related", "to": "euler_fe_split_not_sign_carrier", "note": "L196: F_q fakes with Euler products fail Hodge index"},
        ],
        "priority": 0.24,
        "_template": "closed_routes_t2271_2284",
    },
]


def main():
    data = json.loads(ATLAS.read_text(encoding="utf-8"))
    concepts = data["concepts"]
    by = {c["id"]: c for c in concepts}
    if len(by) != 1113 or data["counts"]["concepts"] != 1113 or data["counts"]["relations"] != 2266:
        raise SystemExit(f"baseline counts differ from 1113/2266: {len(by)} {data['counts']}")
    if sum(len(c["rels"]) for c in concepts) != 2266:
        raise SystemExit("relation sum differs from counts.relations")
    rank1 = min(concepts, key=lambda c: c["rank"])
    if rank1["id"] != "kahler_triple_polarization" or rank1["rank"] != 1:
        raise SystemExit("rank 1 is not kahler_triple_polarization")
    old_open = sum(json.dumps(c, ensure_ascii=False).count("Open ~1.8") for c in concepts)
    if old_open < 1:
        raise SystemExit("Open ~1.8 missing from the live atlas")
    old_order = [c["id"] for c in sorted(concepts, key=lambda c: c["rank"])]
    old_priority = {c["id"]: c["priority"] for c in concepts}
    old_missing = sum(1 for c in concepts if "missing piece" in c["axes"])

    # Annotate existing Bost–Connes / Hagedorn catalog entries with the approved sentence.
    marker = "Einstein's 1917 derivation of B₁₂ = B₂₁"
    h = by["hagedorn_bc"]
    if marker not in h["plain"]:
        h["plain"] = h["plain"].rstrip() + " " + EINSTEIN + " [Exact]"
    if marker not in h["core"]:
        h["core"] = h["core"].rstrip() + " " + EINSTEIN
    k = by["kms_bost_connes"]
    if marker not in k["plain"]:
        k["plain"] = k["plain"].rstrip() + " " + EINSTEIN + " [Exact]"

    types = {r["type"] for c in concepts for r in c["rels"]}
    labels = {c["label"] for c in concepts}
    axes = {a for c in concepts for a in c["axes"]}
    ids = [c["id"] for c in ADDING]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate ids inside the delta")
    collisions = [i for i in ids if i in by]
    if collisions:
        raise SystemExit("id collision: " + " ".join(collisions))
    all_ids = set(by) | set(ids)
    nrel = 0
    built = []
    for spec in ADDING:
        if spec["label"] not in labels:
            raise SystemExit("new label " + spec["label"])
        for a in spec["axes"]:
            if a not in axes:
                raise SystemExit(f"new axis on {spec['id']}: {a}")
        tmpl = spec["_template"]
        if tmpl not in by:
            raise SystemExit("missing template " + tmpl)
        if spec["priority"] != by[tmpl]["priority"]:
            raise SystemExit("priority drifted from template " + spec["id"])
        for r in spec["rels"]:
            if r["type"] not in types:
                raise SystemExit(f"new relation type {r['type']} on {spec['id']}")
            if r["to"] not in all_ids:
                raise SystemExit(f"missing target {spec['id']} -> {r['to']}")
            nrel += 1
        c = {
            "id": spec["id"],
            "name": spec["name"],
            "aliases": spec["aliases"],
            "plain": spec["plain"],
            "label": spec["label"],
            "core": spec["core"],
            "formula": spec["formula"],
            "numbers": spec["numbers"],
            "axes": spec["axes"],
            "uncertain": spec["uncertain"],
            "proved": spec["proved"],
            "tests": spec["tests"],
            "pitfalls": spec["pitfalls"],
            "lemmas": spec["lemmas"],
            "rels": spec["rels"],
            "priority": spec["priority"],
            "ranking": by[tmpl]["ranking"],
            "rank": 10**9,
        }
        if _has_backslash(c):
            raise SystemExit("backslash remains in " + c["id"])
        if _has_backslash(h) or _has_backslash(k):
            raise SystemExit("backslash in annotated existing entry")
        built.append(c)
        concepts.append(c)
    if nrel != 12:
        raise SystemExit(f"expected 12 relations, found {nrel}")

    existing = [c for c in concepts if c["id"] in old_priority]
    existing.sort(key=lambda c: c["rank"])
    ex_b = defaultdict(list)
    nu_b = defaultdict(list)
    for c in existing:
        ex_b[c["priority"]].append(c)
    for c in built:
        nu_b[c["priority"]].append(c)
    order = []
    for p in sorted(set(ex_b) | set(nu_b), reverse=True):
        order.extend(ex_b.get(p, []))
        order.extend(sorted(nu_b.get(p, []), key=lambda c: c["id"]))
    for i, c in enumerate(order, 1):
        c["rank"] = i
    if order[0]["id"] != "kahler_triple_polarization":
        raise SystemExit("rank 1 moved: " + order[0]["id"])
    if [c["id"] for c in order if c["id"] in old_priority] != old_order:
        raise SystemExit("relative order of existing concepts changed")
    for c in order:
        if c["id"] in old_priority and c["priority"] != old_priority[c["id"]]:
            raise SystemExit("priority changed for " + c["id"])
    new_open = sum(json.dumps(c, ensure_ascii=False).count("Open ~1.8") for c in order)
    if new_open != old_open:
        raise SystemExit(f"Open ~1.8 count changed {old_open} -> {new_open}")
    ranks = [c["rank"] for c in order]
    if ranks != list(range(1, len(order) + 1)):
        raise SystemExit("ranks are not 1..N")
    if len({c["id"] for c in order}) != len(order):
        raise SystemExit("duplicate ids after merge")
    new_missing = sum(1 for c in order if "missing piece" in c["axes"])
    if new_missing != old_missing:
        raise SystemExit(f"missing-piece axis count changed {old_missing} -> {new_missing}")

    data["concepts"] = order
    data["counts"] = {
        "concepts": len(order),
        "relations": sum(len(c["rels"]) for c in order),
    }
    if data["counts"] != {"concepts": 1115, "relations": 2278}:
        raise SystemExit("unexpected totals " + str(data["counts"]))
    if _has_backslash(data):
        raise SystemExit("backslash in atlas.json after merge")
    text = json.dumps(data, indent=1, ensure_ascii=False)
    if not text.endswith("\n"):
        text += "\n"
    ATLAS.write_text(text, encoding="utf-8")
    print("counts", data["counts"])
    print("rank1", order[0]["id"], order[0]["priority"])
    print("open_1.8", new_open, "unchanged")
    print("missing_piece_axis", new_missing, "(unchanged)")
    print("added", len(built), "relations_added", nrel)
    for c in built:
        print(" ", c["id"], "rank", c["rank"], "prio", c["priority"])


if __name__ == "__main__":
    main()

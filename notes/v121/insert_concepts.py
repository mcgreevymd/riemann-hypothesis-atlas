#!/usr/bin/env python3
"""Insert the v1.21 concepts into atlas.json.

Baseline checked on the live repo before insertion: 1044 concepts, 2051 relations,
rank 1 kahler_triple_polarization, Open ~1.8 present. Priorities and ranking
blocks are the template copies in delta/atlas_delta_v121.json. Rank is assigned
here: existing relative order is unchanged, and new concepts follow the existing
block of the same priority (alphabetical by id inside that new block).

The formula backslash in probe_response_identity (LaTeX \\bar) is written as q̄.
The public atlas rejects backslashes in build_public_md.py.
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
DELTA = Path(__file__).resolve().parent / "provenance" / "delta" / "atlas_delta_v121.json"


def main():
    data = json.loads(ATLAS.read_text(encoding="utf-8"))
    concepts = data["concepts"]
    by = {c["id"]: c for c in concepts}
    if len(by) != 1044 or data["counts"]["concepts"] != 1044 or data["counts"]["relations"] != 2051:
        raise SystemExit(f"baseline counts differ from 1044/2051: {len(by)} {data['counts']}")
    if sum(len(c["rels"]) for c in concepts) != 2051:
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
    if old_missing != 10:
        raise SystemExit(f"expected 10 missing-piece-axis concepts, found {old_missing}")

    delta = json.loads(DELTA.read_text(encoding="utf-8"))
    if delta["base"]["concepts"] != 1044 or delta["base"]["relations"] != 2051:
        raise SystemExit("delta base is not the verified 1044/2051 baseline; recompute before merging")
    adding = delta["concepts"]
    if len(adding) != 22:
        raise SystemExit(f"expected 22 concepts, found {len(adding)}")
    ids = [c["id"] for c in adding]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate ids inside the delta")
    collisions = [i for i in ids if i in by]
    if collisions:
        raise SystemExit("id collision: " + " ".join(collisions))

    types = {r["type"] for c in concepts for r in c["rels"]}
    labels = {c["label"] for c in concepts}
    axes = {a for c in concepts for a in c["axes"]}
    all_ids = set(by) | set(ids)
    nrel = 0
    built = []
    for spec in adding:
        if spec["label"] not in labels:
            raise SystemExit("new label " + spec["label"])
        for a in spec["axes"]:
            if a not in axes:
                raise SystemExit(f"new axis on {spec['id']}: {a}")
        tmpl = spec["_template"]
        if tmpl not in by:
            raise SystemExit("missing template " + tmpl)
        if spec["priority"] != by[tmpl]["priority"] or spec["ranking"] != by[tmpl]["ranking"]:
            raise SystemExit("priority/ranking drifted from template " + spec["id"])
        if spec["rank"] is not None:
            raise SystemExit("delta rank must be null for " + spec["id"])
        for r in spec["rels"]:
            if r["type"] not in types:
                raise SystemExit(f"new relation type {r['type']} on {spec['id']}")
            if r["to"] not in all_ids:
                raise SystemExit(f"missing target {spec['id']} -> {r['to']}")
            nrel += 1
        formula = spec["formula"].replace("\\bar q", "q\u0304").replace("\\bar w", "w\u0304")
        c = {
            "id": spec["id"],
            "name": spec["name"],
            "aliases": spec["aliases"],
            "plain": spec["plain"],
            "label": spec["label"],
            "core": spec["core"],
            "formula": formula,
            "numbers": spec["numbers"],
            "axes": spec["axes"],
            "uncertain": spec["uncertain"],
            "proved": spec["proved"],
            "tests": spec["tests"],
            "pitfalls": spec["pitfalls"],
            "lemmas": spec["lemmas"],
            "rels": spec["rels"],
            "priority": spec["priority"],
            "ranking": spec["ranking"],
            "rank": 10**9,
        }
        if _has_backslash(c):
            raise SystemExit("backslash remains in " + c["id"])
        built.append(c)
        concepts.append(c)
    if nrel != 57:
        raise SystemExit(f"expected 57 relations, found {nrel}")

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

    data["concepts"] = order
    data["counts"] = {
        "concepts": len(order),
        "relations": sum(len(c["rels"]) for c in order),
    }
    if data["counts"] != {"concepts": 1066, "relations": 2108}:
        raise SystemExit("unexpected totals " + str(data["counts"]))
    text = json.dumps(data, indent=1, ensure_ascii=False)
    if not text.endswith("\n"):
        text += "\n"
    ATLAS.write_text(text, encoding="utf-8")
    print("counts", data["counts"])
    print("rank1", order[0]["id"], order[0]["priority"])
    print("open_1.8", new_open, "unchanged")
    print("missing_piece_axis", sum(1 for c in order if "missing piece" in c["axes"]), "(was 10; formal_projection_restates_w and arithmetic_class_map_requirements carry the axis at template priority)")
    print("added", len(built), "relations_added", nrel)


if __name__ == "__main__":
    main()

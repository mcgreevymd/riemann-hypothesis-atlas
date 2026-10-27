# The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity

**J. W. McGreevy; formalization by Grok Bot**

Version 1.0 · 26 Oct 2026

> ## ⚠ The Riemann Hypothesis is NOT proved here.
> This repository is a map, not a proof. It classifies known theorems, criteria, analogies and open problems by how they bear on RH, and it states precisely which pieces are still missing.

## What this is

The RH Atlas is a structured catalogue of 131 concepts from number theory, algebraic geometry, spectral theory and physics that have been proposed as routes to, restatements of, or analogies for the Riemann Hypothesis. There are 279 typed relations between them (same mechanism as, special case of, analogue of, implies, equivalent to RH, corrects, lives in, fails for). It grew out of the research programme *Thermodynamics of Arithmetic Action* (TAA). References of the form “TAA Lemma N” point to that lemma series; The published volumes listed below collect the earlier lemmas; later lemmas (beyond Lemma 118) are not yet published.

Every entry says in plain words what the concept is, gives its precise core statement, carries a label for how well established it is, and records corrections and cautions where a tempting claim turns out to be false.

## The organizing split

Most beautiful structure around ζ turns out not to decide RH. The atlas sorts structures by one question: **would this still hold if ζ had a zero off the critical line?**

- **Phase / unitarity is ghost-blind.** Functional equations, unit-modulus scattering phases |φ| = 1, cocycles, Hecke operators and cusp-form positivity hold just as well for functions that *do* have zeros off the line, such as the Davenport–Heilbronn function. A “ghost” here means a hypothetical off-line zero, which shows up as a negative-norm direction of the Weil form.
- **The sign of a spectral weight is ghost-sensitive.** Whether a certain quadratic form is positive (the Weil form, the Rosati form, Re ξ′/ξ to the right of the line) does change when an off-line zero is present. For ζ, that sign *is* RH.

So the useful question about any idea is whether it touches the sign, or only the phase.

## How entries are ordered

Every list in the atlas runs in **descending priority**, with `#rank · priority` shown in each header. Priority comes from a scoring layer that is labelled **Heuristic**: the scores are judgment calls, shown component by component so you can disagree with any of them. For each concept:

- **Gap significance:** how closely it bears on one of the ten missing pieces (1.0 if it *is* one, then 0.8, 0.5, 0.2 by distance in the relation graph). The nearest gap is named.
- **Sensitivity:** does it hold for ζ (is it necessary for, or implied by, RH)?
- **Specificity:** does it *fail* for the fakes (the Davenport–Heilbronn function and ghost-zero models)? Ghost-blind structure scores near 0.
- **Tractability:** the chance that working on it gives provable progress.
- **Evidence:** the weight of its label (shown, not in the composite).

  **priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability**

A concept ranks high only if it is both true for ζ and false for the fakes. The full rules and tie-breaks are in [scores.md](scores.md).

## Label legend

| Label | Meaning |
|---|---|
| Theorem | Proved (in the literature or in a TAA lemma). |
| Restatement | Equivalent to RH or to a known result; a reformulation, not progress. |
| Analogy | A structural parallel, not a mathematical identity. |
| Conjecture | Believed but unproved. |
| Open | An unsolved problem or a missing object. |
| Numerical | Computed evidence (some computer-certified), not a proof. |
| Heuristic | A plausible reading or judgment call. |
| Cited | Taken from the literature. Citations marked “to verify” have not yet been checked against the source. |

## Top 15 concepts by rank

| # | priority | concept | label | quadrant |
|---|---|---|---|---|
| 1 | 0.720 | [Weil positivity criterion](ATLAS.md#weil-positivity) | Cited | RH-sharp |
| 2 | 0.720 | [Davenport–Heilbronn function](ATLAS.md#davenport-heilbronn) | Theorem | RH-sharp |
| 3 | 0.720 | [ψ(x) − x (explicit formula, deviation from the pole)](ATLAS.md#psi-minus-x) | Cited | RH-sharp |
| 4 | 0.720 | [Primitive part V₀ = U^⊥](ATLAS.md#primitive-part) | Theorem | RH-sharp |
| 5 | 0.720 | [Lagarias/Hinkkanen criterion](ATLAS.md#lagarias) | Cited | RH-sharp |
| 6 | 0.700 | [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](ATLAS.md#mp-castelnuovo) | Open | RH-sharp |
| 7 | 0.700 | [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](ATLAS.md#mp-d8) | Open | RH-sharp |
| 8 | 0.700 | [Missing: flow-relative H¹ for Spec ℤ](ATLAS.md#mp-flow-h1) | Open | RH-sharp |
| 9 | 0.700 | [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](ATLAS.md#mp-quadratic-rr) | Open | RH-sharp |
| 10 | 0.700 | [Missing: an inequality consequence of automorphy (SC-E / HS-1)](ATLAS.md#mp-automorphy-ineq) | Open | RH-sharp |
| 11 | 0.700 | [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](ATLAS.md#mp-brst) | Open | RH-sharp |
| 12 | 0.700 | [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](ATLAS.md#mp-h1-square) | Open | RH-sharp |
| 13 | 0.700 | [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](ATLAS.md#mp-ns-psi) | Open | RH-sharp |
| 14 | 0.700 | [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](ATLAS.md#mp-passivity-margin) | Open | RH-sharp |
| 15 | 0.700 | [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](ATLAS.md#mp-rg5) | Open | RH-sharp |

Ties at the same priority are broken by gap significance, then by number of relations, then alphabetically by id.

## The ten missing pieces

These are the objects that would have to exist for a positivity proof of RH along the lines of the function-field case (all labelled Open):

1. arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)
2. surface + ample class + Riemann–Roch for Spec ℤ (D8)
3. flow-relative H¹ for Spec ℤ
4. quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square
5. an inequality consequence of automorphy (SC-E / HS-1)
6. a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)
7. H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)
8. a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ
9. passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)
10. RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)

Each is stated precisely in [ATLAS.md](ATLAS.md#missing-pieces), with what is proved around it and the tests (against the Davenport–Heilbronn function and ghost models) it must pass.

## Published volumes (Thermodynamics of Arithmetic Action)

- Arithmetic Unitarity I (v2): https://ai.vixra.org/abs/2610.0045
- Arithmetic Unitarity II: https://ai.vixra.org/abs/2610.0054
- Arithmetic Unitarity III: https://ai.vixra.org/abs/2610.0052
- Arithmetic Unitarity IVa: https://ai.vixra.org/abs/2610.0056
- Arithmetic Unitarity IVb: https://ai.vixra.org/abs/2610.0055
- Arithmetic Unitarity V: https://ai.vixra.org/abs/2610.0059

## How to cite

J. W. McGreevy, *The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity*, version 1.0 (26 Oct 2026), https://github.com/mcgreevymd/riemann-hypothesis-atlas

## Files

| File | What it is |
|---|---|
| `README.md` | This overview. |
| `ATLAS.md` | The full atlas in readable form: missing pieces, diagnostic quadrants, every concept by primary axis (all in priority order), and an index by rank. |
| `atlas.json` | The machine-readable atlas (source of truth for this repository). |
| `scores.md` | The scoring method behind the ordering. |
| `CHANGELOG.md` | Version history. |
| `build_public_md.py` | Regenerates `ATLAS.md` from `atlas.json`: `python3 build_public_md.py`. |
| `q.py` | Command-line query tool: `python3 q.py rosati`, `python3 q.py --axis ghost-blind`, `python3 q.py --list`, `python3 q.py --quadrant RH-sharp`, `python3 q.py --missing`. Python 3, standard library only. |

No license has been chosen yet; all rights are reserved by the author until one is added.

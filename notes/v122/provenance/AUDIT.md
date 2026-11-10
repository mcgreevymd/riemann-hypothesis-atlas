# AUDIT for v1.22 (binding; overrides SYNTHESIS.md and every archived note)

Prepared 10 Nov 2026, about 12:30 AM CST. **RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity. Open ~1.8 is unchanged. Rank 1 is unchanged.**

## A. Claim discipline
1. The certified E0 gaps are still the v1.21 ones (A ≤ 1.1). Nothing tonight is a certificate. All n₋ counts outside A = 1 and 1.1 are numerical.
2. Exact-identity claims are finite-dimensional linear algebra or elementary arithmetic:
   - the Shioda–Tate split, the Krein formula, the penalty threshold, the product formula, and the Cayley–Hamilton kernel.
   - Continuum versions need Q invertible on a stated domain, and a boundary triple. **Neither is verified.**
3. Prime-weight scaling (s ≠ 1) and atom deletions are sensitivity controls. They are not Euler data and not counterexamples.
4. "Genus ∞ on every window" (N4) uses RH only to write W(F) = Σ|F̂(γ)|². Completeness of {e^{iγu}} uses only the zero density (Beurling–Malliavin / Levinson). Without RH the statement is about the indefinite form and is not claimed.
5. The Fréchet/L² ↔ homological/numerical reading is **[Analogy]**.

## B. Cooked or withdrawn
- k∞ from first variations (t2083): **cooked**. The half-density, the sign average and the orientation are inserted.
- Dreamer Construction A (t2092–t2101): **cooked**. Construction B is the Guillemin–Sternberg flow trace, a trace shape and not an intersection.
- The dreamer's explicit chart in the t2101 "part 2B": **cooked**. The obstruction it uncovered is real and is recorded as `real_pl_chart_r2_r3_nogo`.
- "1/(2 sinh(a/2)) is close to k∞" (t2097 side remark): **cooked**. The q → q² gap is inserted.
- The dreamer's fibre-class map into H¹ (t2103): **undefined**. Its n² is W inserted by hand.

## C. Corrections
1. k∞ comes from the x∞ = 0 fixed locus, not from the diagonal self-intersection (t2068).
2. In t2072 the divergence 2 log Λ is subtracted, not cancelled. The ε-pole has the same sign.
3. "W(H_lift) < 0" is the wrong ample-type test. The lock is dropped (t2084; framing2073 §6).
4. "Positivity + (1) + (2)" is Weil's criterion, not a no-go. The dreamer's Bochner step overreaches: it forces off-line classes to have norm zero but does not exclude them (t2104).
5. As defined, Sonine/prolate spaces are archimedean-only. They do not model the primes (t2103).
6. The 1e−5 plateau above A = 1.1 is a mesh floor (t2064). The eigenvector's Fourier zeros at γ_k are a known consequence of the explicit formula (Connes–Consani ζ-cycles; atlas #374), not evidence for RH.
7. S ≈ −J and the "fibre-class" Gram of the Riesz lifts are mesh-dependent (night2105 n2b). Only the sign pattern is robust.
8. Telegrapher (t2085) and graded shadow (t2091) are recorded from the conversation summary only. Telegrapher is recorded by title. Neither is expanded beyond what the conversation states.

## D. Re-derivations run for this bundle (night2105)

| check | result |
|---|---|
| n₋(W\|E0) = n₋(Q) − n₋(S) | 84/84 runs (6 windows × 2 grids × 7 cases) |
| Krein: M(λ) singular at W\|E0 eigenvalues | relative σ_min 1e−6 to 1e−15, against 0.02–1 at midpoints |
| Krein root scan versus compression eigenvalues | matches to ≤ 1e−14 where found; the scan misses eigenvalues below its resolution (stated) |
| Penalty threshold c* | Q + c BBᵀ has λ_min < 0 at 0.99c* and > 0 at 1.01c* for ζ windows |
| Product formula | p^k ≤ 10⁶, p < 60: error 1.8e−15 |
| Half-density P¹/G_m counts | sympy identity |
| Function-field Cayley–Hamilton | rank = min(K+1, 2g); kernel residual ≤ 3.2e−14; G − P + T ≤ 1e−12; point counts match the prime2087 brute force |

## E. Hygiene
- Absolute scratch paths in notes and scripts are rewritten to sibling-relative `../<dir>/`. `inertia2057.py` is copied, so `common2105.py` and the t2064/t2073 scripts resolve.
- arXiv PDFs and text extracts are **not** included (ccrr2098 cc1603/cc2205). Cite arXiv 1603.03191 and 2205.01391 instead.
- evec2064 `cache/`, `res/` and the vector dump are not included (size). Their summary JSON is included.
- No credentials or chat text. Conversation-only items are paraphrased with their turn ids.

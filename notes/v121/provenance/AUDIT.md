# atlas2060: independent audit (binding over SYNTHESIS.md and notes/)

Audited 8 Nov 2026, about 9:15–10:05 PM CST (America/Chicago).

**Outcome: PASS with corrections.** No claim in the bundle asserts RH or all-window positivity. Each item below is either re-derived by a separate route, checked against archived JSON, or corrected. **The Riemann Hypothesis is not proved.**

## A. Reproducibility

- `rerun_all.py` re-executes 47 source scripts under single-thread BLAS. It rebuilds each source directory in a scratch tree from the bundle's own `scripts/` and `data/`, with machine paths made relative. Details are in `checks/RERUN_REPORT.md` and `checks/rerun_results.json`.
- All 47 exit 0 and every output was regenerated. Every regenerated JSON matches the archive exactly, with three exceptions:
  - wall-clock `elapsed_seconds`;
  - a 2.7e−14 rounding difference in `osc2006`;
  - `eisenstein1990/ma_explicit1990.json` (see A2).
- **A1. Certificates.** All internal assertions pass:
  - certify2044: interval certificate, A ≤ 0.694;
  - certify2047: A ≤ 1, 5.9 s;
  - certify_two2047: A ≤ 1.1, 89.3 s;
  - certify_inertia2057: index certificates at A = 1 and 1.1, 102.7 s;
  - check2057: 117 scan rows, 6.9 s.
  The certified numbers are bit-identical to the archived ones: 1553 numeric fields and 264 interval/string fields were compared across all runs.
- **A2. Provenance mismatch.** The archived `ma_explicit1990.json` was produced with 3000 zeros. The archived script uses 400 zeros, and so does the note. Zero-free fields match. The table is diagnostic only and is never used for a sign.
- **A3. Not re-run.** The long 2048-cell scans `inertia2057.py` and `scan2057.py` were not re-run. check2057 re-verifies their rows, and the archived JSON is used for the figures.

## B. Independent re-derivations

`checks/audit2060.py` writes `checks/audit2060.json`. It runs 32 checks, all pass, in 6.4 s. The checks are mpmath multi-precision and are not interval-certified unless stated.

| Claim | Method | Result |
|---|---|---|
| K₀ = ψ(1/4) − log π = −γ − π/2 − 3log2 − log π; −K₀ = γ + log 8π + π/2; FP∫k = π/2 + 2log2 | 30-digit closed forms | pass |
| c* = log(5√2/π) − γ − 3/80 ≈ 0.196566 > 7/240; two-scale bound at A = 1/10 exceeds c* | direct | pass |
| M₁ = 6.3524415627, s* = 0.9009276163 | formula + 4×4 path-matrix eigenvalue | pass |
| B_W(F_z,F_w) = K_q(z,w) | Gamma part by quadrature in a, primes via ζ′/ζ, ξ′/ξ by numerical differentiation; 3 pairs including z = w = 0.6 + 10i | agreement ≤ 7e−14 |
| K_q(1,2) = 0.0459901; KMS kernel −ζ′/ζ(3.5) = 0.1003956 | direct | pass |
| q′(0) = ξ″/ξ(½) = 0.04620999 equals the second moment of positive Φ | quadrature of the theta series | pass |
| Ghost: W/N = 0.00233375, drop-2 W/N = −0.639228 | **Fourier-side** Gamma energy (the source used physical space) | pass |
| Block at s₀ = 49/25: g, d, w, det | closed forms | pass (det = −0.0112645379) |
| n−(Q\|E0) = n−(Q) + n+(S) − 2 | 300 random nonsingular symmetric matrices | 0 mismatches |
| W(F) = ½ min Δ_e (pencil) | sympy | pass |
| a₁(f₁₀) = 38016/691 | Bernoulli numbers | pass |
| K₀ − K₀^{(1)} = −π/2 − log2; S_reg = −ζ′/ζ(½) = K₀/2; K₅(0) = K₀ + 4 | direct | pass |
| −K₀ − (2 − 4a) = 3.37218, 5.37218, 1.08272, −0.303571 | direct | pass |
| k∞(a) = Σ e^{−(2m+½)a} | series | pass |
| Completed ζ has residues −1 (s=0) and +1 (s=1); ξ(0) = ξ(1) = ½ (entire) | direct | pass |
| M̃_A = M_A − 4e^{A/2}: −0.24244, 0.35152, 0.46108 (A = 1, 2, 3) | all prime powers recomputed | matches sos2010 note (−0.242, 0.352, 0.461) |
| **New:** at B = 2, w_B < 0 on (0.693, 0.766), (1.099, 1.183), (1.609, 1.707), (1.946, 2) | dense grid, 2·10⁵ points [Numerical] | the source proved only s₀ = 1.96; fig2 shades all four intervals |

## C. Number cross-check

`checks/numbers_crosscheck.py` writes `checks/numbers_crosscheck.json`.
- 62 numbers cited in SYNTHESIS, the delta and the audit were searched in all archived JSON and in audit2060.json. **58 were matched** to their stated digits.
- The 4 unmatched are explained:
  - "K(9) > 0.358" and "Schur margin > 0.000314" are stated lower bounds; the enclosures are [0.35883, …] and [0.0003145, …].
  - M̃₁ = −0.2424 and M̃₃ = 0.4611 come from a .txt table; they were recomputed in §B.
- One rounding slip was found and fixed during the audit: M₁ = 6.3524415626 → 6.3524415627.

## D. Overclaims found and their fixes (applied in SYNTHESIS, the delta and the figures)

1. "Residues of ξ" → residues of the **completed zeta** Λ(s) at s = 0, 1. ξ is entire.
2. "e^⊥ = E0" is wrong. e^⊥ = R(h − v) ⊕ π(A) contains the negative line h − v, with J = −2.
3. "The negative Q-mode *is* the hyperbolic plane" → Analogy. The squared overlap is 0.969–0.999, not 1.
4. "Two negative directions" (earlier sketch) → **one** (certified at A = 1, 1.1).
5. The signature of S at A = 1, 1.1 is derived *using* the constrained certificate. It is not independent evidence.
6. Statements for A > 1.1 are numerical only. 128- and 2048-cell models differ by about 100×, which is the size of the gap.
7. The ghost is a quadrature sensitivity control. It is not admissible Euler data and not a counterexample.
8. `−J(πF, πG) = W` is tautological, because J on tests is defined from W. It is not evidence for a Hodge index theorem.
9. Certificates use mpmath intervals plus an IEEE-754 rounding model for the matrix layer. They are **not formally verified proofs**.
10. dispersion2030 "PSD on one vertical line ⇒ W ≥ 0 on compact tests" is a sketched proof.
11. q′(0) > 0 is not passivity (z + z³ is a falsifier).
12. The KMS β = ½ weights are positive, but the KMS kernel is not K_q.
13. Source-note claims superseded later and not to be quoted without correction:
    - hodge1991 "X¹⁰ − 1 is the Eisenstein class": it is the boundary class δ(1) in H¹_c (boundary1994).
    - matching1989 "RG family": K₀ is fixed by the character class (counterterm1995).
    - effectivity2001 items corrected by intersection2002.
    - counterterm1995 h(0)/2 bookkeeping.
    - sos2010 "Lemma A": a Ritz value, not a bound.
    - geometry2006 S ≈ ±400: a basis artifact.
    - eisenstein1990 items it marks unaudited, and its zero-based table: diagnostic only.
14. hodge1991 "T₂ nilpotent mod 691" is imprecise. 2049 ≡ −24 mod 691, so N = T₂ + 24 is the nilpotent element.
15. The interval bound failing at 0.695 is inconclusive. It is not a counterexample.
16. The "kinetic vs potential", Planck/primon and Heaviside readings are Analogy. They have no sign mechanism.

## E. Delta validation

`delta/build_delta.py`:
- Proposes 22 concepts and 57 relations, taking v1.20's 1044 / 2051 to **1066 / 2108**.
- No id collisions. Every relation target exists.
- Relation types, labels and axes all come from the v1.20 vocabulary. `rank` is left for the build.
- Rank 1 (`kahler_triple_polarization`) and Open ~1.8 are untouched.

## F. Residual risks

- The baseline counts come from the local copy `ref/atlas.json` (v1.20). The cloud agent must re-read them from the live repo.
- Certificates depend on the floating-point model. A formal (e.g. Arb/flint or Lean) re-verification has not been done.
- Chat-only conclusions (§3.4–§4 of SYNTHESIS) are paraphrased. No chat text is quoted.

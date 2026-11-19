# Lemma 195 (draft): onset law and matched entire control

Scratch draft (t2273). Not in STATE.md, TARGET.md or the atlas, and nothing pushed. **RH is not proved.**
Tags: [T] theorem or exact algebra, [N] numerical, [C] cited from the ledger, [H] heuristic.
Conventions: the window is [0, r] (equivalently [−r/2, r/2] by translation covariance, L194(a)). W is the full Weil form. E₀ = ker C₊ ∩ ker C₋. cosh^⊥ = {∫F cosh((u − r/2)/2) = 0}, tested for Q = W − P (L194(e)). ρ = ½ + σ′ + iγ. The onset r* is the first r with n₋ ≥ 1 (τ = 1e−9).

## Statement

**(a) [N] The proposed law σ′·r* = c is false.** The data cover 45 real or synthetic quartets (15 certified DH quartets, each in three backgrounds) plus a fixed-γ σ′-scan (40 runs).
- r* depends on σ′ only logarithmically: dr*/d ln σ′ is between −0.06 and −0.21.
- Across the scan, σ′r* runs from 0.03 to 1.9.
- Over the 15 DH quartets, σ′r* has a coefficient of variation of 0.47, and its regression on log γ gives R² = 0.02.

**(b) [N] r* is set by the analytic conductor.** It tracks ℓ = log(qγ/2π), with a weak σ′ term and a background ("hole") term:

  r* ≈ A·ℓ + B + κ ln σ′

| fit | A | κ | R² | rms |
|---|---|---|---|---|
| DH | 0.82 | −0.29 | 0.90 | 0.19 |
| ζ | 0.99 | −0.11 | 0.98 | 0.09 |
| L5 | 0.90 | −0.15 | 0.91 | 0.18 |

The same quartet placed in the ζ background and in the L5 (q = 5) background has onsets that differ by about 1.5–1.6 ≈ log 5. This reproduces the ledger's 107-onset law (§226–§227 [C]: L* = A·ℓ/(1 + s/s₀) − κ_δ ln(δ/0.15), A ≈ 1.18, universal for ζ, L5 and DH). The DH onsets come from per-quartet runs, so the first DH onset (3.58) is attributable to the 85.7 quartet: every other quartet's single-quartet onset is ≥ 3.97.

**(c) [T]+[H] Mechanism.**
- [T, r20 symbolic] The quartet's representer block has its negative part set by sinh(σ′r)/σ′ − r ≈ σ′²r³/6 for σ′r ≲ 1.
- [H] Onset is the point where this signal beats the positive on-line margin at frequency γ. That margin collapses once the window resolves height γ, i.e. e^{r} ≳ qγ/2π, because the near-null count is ≈ 2e^{r} (§226).
- So r* ≈ ℓ − O(1) − (const)·ln σ′. A constant σ′r* would need a fixed O(1) floor, and none exists.
- [H] Reading: the window half-length r/2 reaches log √(qγ/2π), the approximate-functional-equation length at height γ.

**(d) [N] Pole-having d = −20 ghosts.**
- Z₁ = x²+5y², first ghost 0.9329696975+15.6682495313i [C Krawczyk §184], σ′ = 0.43297. Onsets r* = 3.0 (W), 3.175 (E₀) and 3.175 (cosh^⊥) at h = .025; at h = .05 they are 3.05, 3.2 and 3.2. The eigenvector peaks at 14.3, so the onset is attributable to γ = 15.67. σ′r* is 1.30–1.37, but r* − ℓ = −0.7 to −0.9, the same as DH's mean of −0.78.
- Z₂ = 2x²+2xy+3y², first ghost 2.0794141048 + 7.6288675878i (mpmath refine). It lies **outside the critical strip**, with σ′ = 1.579. Onsets r* = 0.85 (W, a frequency-0 mode), 1.35 (E₀) and 1.15 (cosh^⊥), the same at h = .05 and .025. σ′r* is 2.13 on E₀ and 1.82 on cosh^⊥. This is a different regime (|σ′| > ½), not evidence for a law.
- ζ_K (control) has no onset on W, E₀ or cosh^⊥ up to r = 6.

**(e) [N] Matched entire control (T3).** Both functions below have Γ_R(s+1) and q = 5:
- L(s, χ), χ mod 5 odd with χ(2) = i, in the Hermitian Weil form: **no negative eigenvalue** on W, E₀ or cosh^⊥ up to r = 8 (h = .025 and .05). The smallest λ_min stays positive (down to 2e−10).
- ½L(χ)L(χ̄): same result.
- DH: onset 3.85 (h = .025) or 5.7 (h = .05). The fine values are 3.579–3.580 (§230 [C]) and 3.575 (zero side, h = .003125).
- [C] CC25 Table 1: χ₅ full λ_max < 0 up to L = 16.

**(f) [T]/[N] What T3 separates.**
- **DH:** signed and non-prime-power. Λ_DH(49)/log 7 = −2.0807009 = −(2+κ²) (κ = 0.284079). Of 1361 nonzero c(n) with n ≤ e⁸, 677 are negative and 900 are at non-prime-powers; the first composites are 6, 12, 14, 18, 21, 24, …
- **L(χ):** 461 nonzero, all at prime powers. 232 are non-real and 116 are real negative.
- Both have signed or complex coefficients, so the coefficient sign does not separate them; the prime-power support (Euler product) together with the FE does. The real-coefficient version of this separation already existed: L(χ₋₄) and the genus L-function pass with signed Λ (L194(e), §4283), while Z₁ and Z₂ fail with positive a_n. T3 adds the matched, same-Γ, same-q, entire pair.
- It does **not** show that multiplicativity alone suffices: L166, §304 and the E1 conjunction (§3786) already rule that out [C].

## Tests

1. **Fixed-γ σ′-scan.** `dscan.py` → `dscan_h0.00625.json`: σ′ ∈ {.01, …, .49}, γ = 85.70 (DH, ζ and L5 backgrounds) and 176.70 (DH).
   - Pass condition for the law: r*σ′ constant. Observed r* goes 3.99 → 3.22 (DH 85.7), 4.57 → 3.67 (DH 176.7), 2.96 → 2.71 (ζ) and 4.54 → 3.96 (L5), so σ′r* runs 0.04 → 1.6 (DH 85.7).
   - **FAIL.** W and E₀ onsets are identical except for one 0.006 difference.
2. **Cross-quartet fit.** `fit_t1.py` → `fit_t1.json`, using the r19 data (h = .003125, m = 8, density tail).
   - σ′r* versus log γ: R² = 0.02 / 0.05 / 0.02 (DH / ζ / L5).
   - r* = c/σ′: R² is between −20 and −57.
   - r* = Aℓ + B + κ ln σ′: R² = 0.90 / 0.98 / 0.91.
3. **Basis (N) dependence.**
   - r19 onsets at h = .003125 and .00625 differ by ≤ 0.04 (≤ 0.12 for γ > 520, flagged truncation-sensitive).
   - Prime-side L149 basis: DH 3.85 at h = .025 versus 5.7 at h = .05, against the fine value 3.58. Z₁ and Z₂ change by ≤ 0.05 between h = .05 and .025.
   - Onsets in nested bases are upper bounds (a finer basis gives an earlier onset), so the Z₁ value may sit up to about 0.3 lower in a fine basis. That would lower σ′r* by about 0.1 and leave the verdict unchanged.
4. **Validation.**
   - The generalized-frequency log-derivative code reproduces `lemma167_lib.log_deriv_coeffs` on Z₁ to 7e−15.
   - Z₁ onsets equal L169's 3.0 and 3.175 exactly.
   - ζ_K shows no onset (Euler control).
   - Z₂ ghost: |Z₂| < 3e−26 at the refined root.
5. **Z₂ explicit formula [T].** Λ_{Z₂} = 20^{s/2}Γ_R(s)Γ_R(s+1)·2^{−s}G(s) = 5^{s/2}Γ_RΓ_R G(s). So the archimedean row is AZ + AD (conductor 5), and the prime side sits at the generalized frequencies log(n/2^k) of −G′/G. The pole row is unchanged.
6. **T3.** `t3.py` → `t3_h0.05.json` and `t3_h0.025.json`, with profiles in steps of 0.25 up to r = 8.

## Not done

- No Krawczyk certification of the Z₁ ghosts beyond the first, or of the Z₂ ghosts. These are mpmath roots, all at |Z| < 1e−25.
- No per-ghost onsets for Z₁ or Z₂: only the first onset is attributed. That would need single-ghost zero-side runs over certified on-line zeros.
- The lem194 high-precision basis was not rerun near r = 4.0 for the 114.2 quartet. The lem194 brackets for 114.2 are limited by reach (Nπ/r ≈ 113 at N = 144).

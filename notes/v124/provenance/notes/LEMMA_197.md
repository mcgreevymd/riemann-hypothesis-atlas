# Lemma 197 — Euler × FE ablation with failure localization (STATE §351 design; t2285 overnight run)

Scratch, `lem197/`. **RH is not proved. Φ is not constructed. No sign is found. Nothing here touches TARGET (D).** STATE.md, TARGET.md and the atlas were not edited by this run.
Labels: [P] proved, [N] numerical (Galerkin; not a certificate), [F] framing, [C] closed route / restatement of ledger content.

## Setting
L149/L167 cubic B-spline basis, spacing h = 0.025 (cross-check h = 0.05), window length r = (N+1)h ≤ 8 (N ≤ 319, the §351 "M = 320, L ≤ 8"). Rows from `num/l149/rows_h*.npz` (POLE, AZ = Γ(s/2) arch, AD = Γ((s+1)/2) + log(5/π) arch). Prime side: −Σ_λ c_λ e^{−λ/2} g(λ) with c_λ the coefficients of −L′/L (generalized frequencies λ = log(n/2^k) for Z₂, as in t2273/epstein12.py). Three restrictions per member: W on the full window, W|E₀ (E₀ = ker C₊ ∩ ker C₋), and Q = W − P on cosh(u/2)^⊥ (the L194(e) 6′ inertia count; for entire members Q = W). Onset r* = first r with a generalized eigenvalue < −10⁻⁹ (bisection in N; monotone by L194(a)(ii)).

Matched families (40 members + 40 ε-scan members + 9 truncations + 3 prime-free "flat" forms):
- **(a) Euler + FE:** ζ; ζ_K (K = ℚ(√−20)), L(χ₋₄)L(χ₅) (same Γ_ℝ(s)Γ_ℝ(s+1), q = 20); L(χ mod 5, χ(2) = i) (Hermitian form, q = 5, entire).
- **(b) FE kept, Euler broken:** F_λ = (ζ_K + λ·L(χ₋₄)L(χ₅))/(1+λ), λ ∈ {0.02, 0.1, 0.3, 1 (= Z₁), 3, −0.3, −0.7, −1 (= Z₂)}; DH (same Γ, q = 5 as L(χ)).
- **(c) Euler kept, FE lost:** one-prime local factor ×(1 − ε p₀^{−s})^{−1} (ζ, ζ_K, L(χ); p₀ ∈ {2,3,5,7}; ε = ±0.2, 0.05, and a scan 10⁻⁴…0.2); prime deleted (p₀ = 2, 3); Beurling primes (log p jittered by U(±0.02), all powers kept); χ(2) rotated off the character (|a_p| = 1 kept); ζ_K with the q = 5 arch (wrong conductor).

## Lemma 197
**(i) [N] Separation.** On every window r ≤ 8, all four (a) members have W ≥ 0, W|E₀ ≥ 0 and Q|cosh^⊥ ≥ 0 (Galerkin minima > 0, decaying to 10⁻⁸–10⁻¹⁰ by r = 8: positivity is marginal, not robust). All 36 ablated members fail: (b) at r* = 0.85–5.7, (c) at r* = 0.78–4.6 (full form). Neither ingredient alone keeps the sign in windows ≤ 8. §351's falsifier ("a control stays positive to L = 8") is not triggered.

**(ii) [P] The §351 p₀-share criterion is tautological for (c).** Write Q_pert = Q_base + Δ, with Δ supported on the perturbed frequencies {k log p₀}. If v is the negative vector of Q_pert and Q_base(v) ≥ 0, then Δ(v) ≤ Q_pert(v) < 0, so 100% of the defect sits on p₀ by construction. (Q_base(v) > 0 was computed directly for every reported v.) The criterion "p₀ share > 2× random baseline" therefore cannot fail and carries no evidence. This corrects the §351 design. The informative quantity is the **detection lag** r* − log p₀.

**(iii) [N] Detection lag grows with the analytic conductor and slowly with 1/|ε|.**
| base | p₀ | ε = 0.2 | 0.05 | 0.01 | 10⁻³ | 10⁻⁴ | −10⁻⁴ | −0.01 | −0.2 | (full / E₀) |
|---|---|---|---|---|---|---|---|---|---|---|
| ζ (deg 1, q = 1) | 2 | .775/.95 | .825/1.025 | .875/1.10 | .95/1.20 | 1.075/1.40 | 1.125/1.475 | .95/1.35 | .825/1.225 | log 2 = .693 |
| ζ | 3 | 1.175/1.175 | 1.20/1.20 | 1.225/1.225 | 1.275/1.325 | 1.425/1.50 | 1.425/1.725 | 1.25/1.30 | 1.15/1.20 | log 3 = 1.099 |
| ζ_K (deg 2, q = 20) | 2 | 2.525/4.625 | 2.775/4.65 | 2.975/4.65 | 3.20/4.75 | 3.35/4.95 | 4.125/4.125 | 3.775/3.775 | 3.475/3.60 | |
| ζ_K | 3 | 2.525/3.60 | 2.775/3.70 | 2.975/3.80 | 3.175/3.95 | 3.325/4.225 | 4.475/4.50 | 4.175/4.175 | 4.025/4.025 | |
For ζ the lag is 0.08–0.43 (full) and grows about 0.03–0.06 per e-fold of 1/|ε|. For ζ_K it is 1.8–3.8. Negative eigenvalues at onset (|ε| = 10⁻⁴) are −10⁻⁶–−10⁻⁵, i.e. 10²–10³ above the threshold and the true-member floor. Truncations of ζ at P = 2…13 fail at log(next prime power) + 0.027–0.051 [C: restates §304, "L*(P) − log p_next ∈ [.014, .176]"].

**(iv) [N] The prime-free ("flat") background is positive only on short windows, and how short depends on the class.** Arch + pole with no primes: ζ class r* = 0.775 (full), 1.225 (E₀), 0.775 (cosh^⊥); q = 5 odd entire class 1.725 / 5.775 / 4.3; ζ_K class (q = 20) 2.5 / 4.675 / 3.3. "ζ minus p = 2" fails at exactly the flat onset 0.775. So for ζ, the free flat region ends at r ≈ 0.78, about 0.08 after log 2, and Λ(2) with its exact weight is load-bearing from there on. This corrects the t2284 equivalence-principle framing ("short windows see only the universal background and everything passes"): it holds only for r ≤ 0.78 in the ζ class, and the slack grows with log of the analytic conductor (three points, roughly 0.78 + 0.6 log q in the full form).

**(v) [N] Localization for (b).** Here Δ = Q_fake − Q_Euler, taken against the matched Euler member with the same arch, so Δ_arch = 0 exactly.
- Share of the negative defect carried by composite (non-prime-power) n:
  - DH: 74% (top carriers n = 14, 21, 6, 34).
  - F_λ: 87% at λ = .02, 77% at .1, 69% at .3, 47% at Z₁ (top n = 6, 21, 3, 9), 25% at λ = 3, 65–76% at −.3, and 0% at −.7, where the carriers are the prime powers 3 and 2.
  - Z₂: 61–89% sits on the non-integer frequencies log(9/4), log(27/8), log(7/2) of its 2^{−s}G(s) form. These are frequencies of the generalized expansion, not of an integer Dirichlet series: compare the t2284 note.
- So composite support is the typical carrier, but it is not universal. Far from the Euler point, Euler-breaking shows up in the prime-power coefficients themselves.
- First carrier frequency: log 2 for most F_λ, log 4 for DH, log 3 for λ = −0.3.
- Zero responsible: the peak of |F̂| of the negative vector matches the lowest off-line zero for DH (84.5 vs 85.70) and Z₁ (14.3 vs 15.67). It does not match for Z₂ (3.7–4.7 vs 7.63; its first ghost has Re ρ > 1) or for the F_λ interior members, whose ghosts were not computed.
- Onsets on the d = −20 pencil (E₀): λ = .02 → 5.675, .1 → 4.675, .3 → 3.675, 1 → 3.175, 3 → 3.40; λ = −.3 → 2.0, −.7 → 1.15, −1 → 1.35. The λ > 0 branch restates §197/L173. **The λ < 0 branch (toward Z₂) is new and fails early.** The cause is presumably zeros leaving the strip, as for Z₂; that has not been verified.

**(vi) [N] Robustness.** h = 0.05 reproduces every onset to ±0.05, except two cases:
- DH: 5.7 at h = .05, against 3.85 at h = .025 and 3.58 fine (t2273).
- F_λ=.02: 6.8, against 5.675.

Low-amplitude ghosts are basis-sensitive. Onsets are upper bounds that decrease under refinement, since the B-spline spaces are nested.

**(vii) [P] + [N] ζ-side analogue of L196.6 (convention A): Euler kept, FE lost, and the form stays positive.**
- Deleting the local factor at p₀ removes −log p₀·Σ_{k≥1} p₀^{−k/2}[g(k log p₀) + g(−k log p₀)].
- Adding back the diagonal log p₀·g(0) = log p₀·‖F‖² completes this to log p₀·Σ_{k∈ℤ} p₀^{−|k|/2} g(k log p₀) = log p₀ ∫|F̂(t)|²·P_{p₀}(t) dt/2π. Here P_{p₀} is the Poisson kernel with r = p₀^{−1/2} at angle t log p₀, which is > 0.
- So the result is W_ζ + (a PSD form) [P]. It is positive whenever W_ζ is: unconditionally on the certified windows (E₀, A ≤ 1.1), and on every window under RH.
- [N] Results:
  - ζ minus p₀ ∈ {2, 3, 5} with the diagonal +log p₀: no onset to r = 8 in any mode.
  - The same holds for ζ_K at p₀ = 2 and 5 (ramified). At p₀ = 3 (split, two degree-1 primes) the compensation needed is 2 log 3: with log 3 it fails at 4.25; with 2 log 3 there is no onset.
  - Adding a copy of the factor instead (diagonal −log p₀) fails at once: r* = 0.125–0.175 for ζ, 1.2–1.5 for ζ_K (full).
- This is the exact counterpart of L196.6 (convention A: removing a point keeps W > 0, adding one fails). The (c) results in (iii) correspond to L196's convention B (diagonal kept), where both signs fail.
- Conclusion: an Euler product **without** the FE can be window-positive, so the (c) failures in (i) depend on the bookkeeping convention, and FE-loss by itself is not what makes positivity fail. As in L196.6, positivity without the FE does not imply purity: the deleted object ζ·(1 − p₀^{−s}) has extra zeros at s = 2πik/log p₀, on Re s = 0, which is off the line.

## Reconciliation with Lemma 196 (§351 [H 3.30])
L196 (C) says the ζ/DH separation by Euler × FE is **not** evidence that those ingredients carry the sign, because over F_q thousands of off-circle fakes have a genuine Euler product with nonnegative integer counts and the FE (rungs iii–vi), and they still fail. Only Hodge index on C×C, from effectivity of Γ_{F^n}, kills them. Lemma 197 agrees and adds the ζ side:
1. (i) shows that, in windows ≤ 8, removing either ingredient breaks positivity. That makes Euler × FE **necessary-looking**, not sufficient. L196 shows that it is not sufficient over F_q. On the ℚ side, sufficiency was never tested here: no Euler + FE fake exists in the matched d = −20 or q = 5 families, and Beurling/random Euler products with an FE are the ledger's L166, §304, §3786 controls.
2. (vii) shows that "Euler kept, FE lost" can stay positive (convention A). So even the necessity reading of FE is convention-dependent. What fails is purity, not positivity, which matches L196.6.
3. (ii) and L196.5 agree that failure has no robust place localization. Over F_q it is one root (finite rank ≤ 2g). On ℚ, the (c) "localization" is tautological and the (b) carriers spread over composites and prime powers.
4. Both lemmas see rigid, marginal positivity in the true cases: over F_q, W is singular off 2g directions; on ℚ, λ_min falls to 10⁻⁸–10⁻¹⁰ by r = 8. So ablation measures fragility, not the source of the sign.

Net verdict: §351 [H 3.30] stands as a **diagnostic pattern** (in the tested families, every separator of ζ from DH runs through Euler × FE). It should **not** be read as "Euler × FE carries the sign". The F_q answer (L196 B) is effectivity + Riemann–Roch + an ample class (T-D2), which is not a property of the coefficients.

## Proof status
(ii) and the PSD identity in (vii) are proved (a few lines each). Everything else is numerical, in a Galerkin basis with h = 0.025, cross-checked at 0.05:
- A negative Galerkin value certifies a negative direction, assuming the stored rows are exact.
- A positive Galerkin minimum certifies nothing (L194(a)(iii)).

## Verdict
**Mostly restatement, plus one method correction, a convention-A positivity identity on the ζ side, and two small new data points.** See also the reconciliation with L196 above.
- Restated ledger content:
  - The separation in (i) is the standing control: §351 [H 3.30], L64 §73, L60 §69, L164, and t2273 T3.
  - The truncation lags restate §304.
  - The λ > 0 pencil restates L173.
- New:
  - (ii), the p₀-share criterion of §351 is vacuous.
  - (iii)/(iv), the detection lag scales with the analytic conductor, and ζ's prime-free region ends at r ≈ 0.78.
  - The λ < 0 pencil onsets.
- The test cannot tell "the step uses Euler and FE jointly" apart from "the true forms sit at a marginal positive minimum (10⁻⁸–10⁻¹⁰ by r = 8), so any change to the explicit formula is eventually detected."
- Ablation therefore localizes failure. It does not locate the source of the sign.
- Nothing here touches (D).

## Tests (reproduce)
- `python3 l197.py 0.025` (about 2 s on 8 cores), producing `l197_h0.025.json`; also `l197.py 0.05`.
- `python3 extra197.py`: ε-scan, flat forms, truncations, Δ-attribution, true profiles (`extra197.json`).
- `python3 chk.py`: magnitudes at onset.
- `python3 conv196.py`: convention-A deletion and addition (vii).
- Validation against earlier runs: DH 3.85 (t2273 T3, h = .025), Z₁ 3.0 / 3.175 / 3.175, Z₂ 0.85 / 1.35 / 1.15 (t2273 epstein12, h = .025); ζ, ζ_K, L(χ) positive to r = 8 (t2273, L173).

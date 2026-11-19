# REPORT — Lemma 197 (Euler × FE ablation), overnight t2285

Scratch only (`lem197/`): STATE.md, TARGET.md and the atlas were not touched by this run; nothing was pushed. **RH is not proved.** Full statement: LEMMA_197.md.

Files: l197.py, extra197.py, chk.py, l197_h0.025.json, l197_h0.05.json, extra197.json, run_h0.025.log, run_h0.05.log, extra197.log. Compute: about 1 min in total.

Key numbers:
- (a) members positive to r = 8 (ζ, ζ_K, LL, L(χ mod 5)); Galerkin minima fall to 10⁻⁸–10⁻¹⁰.
- 36/36 ablated members fail: (b) FE-only at r* 0.85–5.7; (c) Euler-only at 0.78–4.6.
- One-prime perturbation of ζ at p₀ = 2: r* = 0.775–1.125 (full) for |ε| from 0.2 down to 10⁻⁴; at p₀ = 3: 1.15–1.425. For ζ_K: 2.5–4.5.
- Flat (prime-free) forms: ζ class 0.775, q = 5 entire 1.725, ζ_K class 2.5 (full).
- (b) defect carried on composites: DH 74%, Z₁ 47%, F_λ 0–87% depending on λ; Z₂ 61–89% on non-integer frequencies.
- Zero match: DH 84.5 vs 85.70, Z₁ 14.3 vs 15.67.

- Convention A (vii): ζ or ζ_K with a deleted local factor plus the diagonal compensation stays positive to 8. This is exact (PSD Poisson completion) and is the ζ-side twin of L196.6. Euler without FE can be positive, but it is then not pure.
- Reconciled with L196: Euler × FE is a diagnostic pattern, not the carrier of the sign.

Verdict:
- Restatement of the standing multiplicativity control.
- Method correction: §351's p₀-share criterion is tautological.
- New small items:
  - ζ's flat region ends at 0.78, so Claude's t2284 "all pass small windows" holds only to there.
  - Detection lag grows with the analytic conductor.
  - The λ < 0 pencil fails early.
- It does not touch (D).

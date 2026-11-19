# RH Atlas v1.24: the ample direction, the anatomy of the sign over F_q, and an Euler × FE ablation (TAA Lemmas 194–197)

1113 concepts (+12) and 2266 typed relations (+49), from v1.23 at `b035a04` (1101 concepts, 2217 relations). Covers 17–18 Nov 2026 (America/Chicago).

**What is new.**
- TAA Lemmas 194–197:
  - **L194 [Proved; Restatement]:** over all windows, RH ⇔ Q ≥ 0 on cosh(u/2)^⊥ ⇔ Q ≥ 0 on E0. Index 1 (λ₁(Q) ≥ 0) is only implied by RH. Translation acts as a boost and carries E0 to E0. The ample class f₁ + f₂ corresponds to cosh.
  - **L195 draft [Numerical]:** σ′·r* = const fails (σ′r* ranges over 0.09–1.58, with R² = 0.02). The conductor law stands. Z₂'s early onset comes from its Re ρ = 2.079 zero. L(χ mod 5) is positive to r = 8 while DH fails at 3.58. The separator is prime-power support + FE, not sign Λ.
  - **L196 [Proved + exact Numerical], genus 2 over F_q:**
    - No count rung kills the fakes; off-circle survivors number 12 to 4322 for q = 3–13. The Hodge index at a single n ⇔ the Weil bound at n, and the depth N*(q) grows with q.
    - Thm 196.1: N_n ≥ 0 ⇒ |α| ≤ q.
    - Thm 196.4: the form has finite rank ≤ 2g, the pole plane is an off-circle FE pair, and n−(Q) = n−(W) + 1.
    - 196.6: the FE is needed for positivity ⇒ purity.
  - **L197 [Numerical + Proved]:**
    - All 36 single-ingredient fakes fail by r = 5.7. The §351 "p₀ share" test is tautological. The detection lag grows with the analytic conductor. ζ's prime-free region ends at r ≈ 0.78.
    - Deleting a place and restoring its diagonal adds a positive Poisson form, so Euler without the FE can be positive (the twin of L196.6).
    - Reconciled with L196: the Euler × FE split is a diagnostic pattern and does not carry the sign.
- Filter sort: ledger lemmas binned by use of multiplicativity. None of the Euler-using steps produces the sign.
- Closed routes and framings, t2271–t2286: Maass–Selberg/Witten (the ½ offset); Ruppeiner/Lee–Yang/Fisher; Hodge star (a Riemannian metric, not the arithmetic sign); f∗f̃; gravity/rest energy; degree and conductor; the equivalence principle; Kepler/KS perpendicularity.
- Corrections to earlier chat checks:
  - Z₂'s first frequency is log(3/2).
  - 0.2812 is the Markov threshold, not a positivity threshold.
  - ∫F∧*F = ‖F‖² ≥ 0 on a Riemannian 4-manifold, and *² = +1 there.

**Not claimed.** RH is not proved. Φ is not constructed. There is no Hodge-type sign and no all-window positivity. Nothing touches (D). The certificates are unchanged (A ≤ 1.1).

**Ordering.** Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. Rank 1 remains `kahler_triple_polarization`. Open ~1.8 is unchanged. No new figures.

**Front matter.** `notes/v124/` (FRONT, SYNTHESIS, LIMITATIONS, insert script). Provenance (lemmas, checks, filter sort, scripts, small data, AUDIT, smoke test) is in `notes/v124/provenance/`.

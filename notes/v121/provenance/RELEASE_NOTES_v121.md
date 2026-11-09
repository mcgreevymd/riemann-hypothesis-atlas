# Draft changelog entry: v1.21

## v1.21: 8–9 Nov 2026 (UTC)

**Counts.** 1066 concepts (+22) and 2108 typed relations (+57), up from v1.20 (1044 concepts, 2051 relations). Covers 8 Nov 2026 (America/Chicago).

**What is new.**
- The window Weil form is the form of one closed, semibounded, signed self-adjoint operator.
- E0 = (∂² − 1/4)H²₀. The Hardy and cusp constant 1/4 is shared, but the operators are not identified.
- M_A is a regularized prime sum, and K₀ is fixed by the character class.
- Certified E0 gaps:
  - 0.1966 for A ≤ 1/10 (analytic);
  - 0.0045 for A ≤ 0.694 (interval);
  - 0.004 for A ≤ 1 and 0.0005 for A ≤ 1.1 (computer-assisted, IEEE-754 model, not formal proofs).
- Exactly one negative direction off E0 is certified at A = 1 and 1.1.
- The boundary plane has signature (1,1), with an FE-fixed class e = h + v and J(e,e) = 2.
- The formal projection −J(πF, πG) = W is recorded as a restatement.
- Requirements on the missing arithmetic class map Φ.
- The probe identity B_W(F_z, F_w) = K_q.
- Obstructions: signed KYP storage, prime-gap blocks, the KMS β = ½ kernel, and K₀ as an Arakelov degree on P¹_Z.
- Calibrations: the Serre-derivative closure at k = 4, 6, 8, 12, and the boundary class δ(1) with Eisenstein denominator 691.

**Not claimed.**
- The Riemann Hypothesis is not proved, and there is no all-window positivity.
- Statements for A > 1.1 are numerical. There, 128- and 2048-cell models differ by about 100×, and the gap and the grid error are the same size.
- Deleting n = 2 alone gives W/‖F‖² = −0.639 on an explicit E0 test. This is a sensitivity control, not Euler data.

**Corrections.**
- Residues belong to the completed zeta, not ξ.
- e^⊥ ≠ E0.
- One negative direction, not two.
- The S signature depends on the E0 certificate.
- X¹⁰ − 1 is a boundary class, not the Eisenstein class.
- K₀ has no RG freedom.
- "Lemma A" is a Ritz value.
- The vertical-line step of the probe argument is a sketch.
- q′(0) > 0 is not passivity.

**Ordering.** Existing priorities and the relative order of existing concepts are unchanged. New concepts follow the existing block of the same priority. Rank 1 remains `kahler_triple_polarization`. Open ~1.8 is unchanged.

**Front matter.**
- Notes and figures go under `notes/v121/` and `figures/v121/`: one front figure and two supporting figures.
- Raw notes, scripts, data and the independent audit go under `notes/v121/provenance/`.
- Reproducibility: 47 scripts re-run with single-thread BLAS, all certificate assertions pass, and 32 independent re-derivations pass.

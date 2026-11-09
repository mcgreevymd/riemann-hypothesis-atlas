# Figures for v1.21 (proposed path `figures/v121/`)

The figures are regenerated with `python3 figures/make_figures.py`. The script reads only `data/`. Each figure is saved as PNG and SVG, and every one carries the footer "The Riemann Hypothesis is not proved. No all-window positivity is claimed."

## Fig 1 (front figure): `fig1_frontier`: "What is proved, what is only computed, and what is missing"

**Left panel.** Log-scale lower bounds on W/‖F‖² over E0 against the window width A, with red lines at the prime-power lags log n.

- Certified bars:
  - A ≤ 0.1, 0.1966 [Exact];
  - A ≤ 0.694, 0.0045 [Interval certificate];
  - A ≤ 1, 0.004 [Computer-assisted];
  - A ≤ 1.1, 0.0005 [Computer-assisted].
- Grey curve: the 128-cell finite-model minima. Dots: the 2048-cell minima [Numerical, upper estimates].
- The region A > 1.1 is shaded with the note "numerical evidence only; 128- vs 2048-cell values differ ~100×".
- Ghost note: deleting only n = 2 gives −0.639 at A = 2, against +0.0023 with the true coefficients.

**Right panel.** The mechanism as a stack of boxes:

1. The ledger W = P + H_A − M_A‖F‖².
2. Q = W − P has exactly one negative direction [Certificate]. With S of signature (1,1), the count n−(Q|E0) = n−(Q) + n+(S) − 2 = 0.
3. The formal boundary model, which is exact but tautological.
4. The red box: **MISSING** class map Φ, built from geometry with the pairing computed.

Caption: Certified window positivity stops at A = 1.1. Beyond it the computed gap (~1e−5) is the same size as the discretization error. The sign pattern (one negative direction, absorbed by two moments) is the Hodge-index pattern. The object that would make it a theorem, an arithmetic class map with a computed intersection pairing, is missing.

## Fig 2: `fig2_response_storage`: "The response reading of W, and where storage fails"

- **Left.** The signed storage weight w_B(s) at cutoff B = 2, true coefficients against n = 2 deleted. It is negative just after log 2, 3, 5 and 7 (shaded) [Numerical]. At s = 1.96 the failure is proved: det = −0.01126 [Obstruction].
- **Right.** Status-tagged boxes:
  - the probe identity B_W = K_q [Exact];
  - Lagarias/Hinkkanen [Cited];
  - signed KYP [Exact];
  - obstructions;
  - the KMS β = ½ substrate;
  - [Open] coupled positive storage.

## Fig 3: `fig3_inertia_scan`: "Finite inertia scan"

- **Left.** The eigenvalues of S_Q and the counts n−(Q) = 1 and n−(Q|E0) = 0 on the 128-cell models, A = 0.5 to 3.
- **Right.** The squared overlap of the negative Q-mode with span{e^{±u/2}} (0.969 to 0.999): close to the moment span, but not inside it.

All of fig 3 is [Numerical]. Only A = 1 and A = 1.1 are certified.

**Alt text** is given in the captions above. Do not crop the footer.

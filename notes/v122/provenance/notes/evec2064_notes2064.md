# t2064: the eigenvector under the ~1e-5 constrained floor (scratch only)

Status: **NUMERICAL** throughout. There is no continuum certificate above A=1.1, Phi is not constructed, RH is unproved, and there is no all-window positivity. Nothing was pushed or sent.

## Method
- The operator is reused unchanged from `../inertia2057/inertia2057.py`: complete Gamma cell integrals (`matrix(A,n)`), prime-power atoms Λ(n)/√n for log n < A, and exact moment columns B. `build.py` computes Q and caches it in `cache/`. It also keeps the Gamma-only column and checks that it reproduces `matrix()` exactly (max diff 0).
- E0 = ker Bᵀ, with Z = full-QR(B)[:,2:]. The six smallest eigenpairs of ZᵀQZ are lifted as v = Z·U. On E0, W equals Q.
- Normalization: f = v/√h (cell values of the function), so ∫f² du = 1. Sign: f(0) > 0. Moment residuals |Bᵀv| ≤ 6e-16 for every run (in E0 to machine precision).
- Grids: n = 512, 1024, 2048 at all 11 windows (0.694, 1, 1.1, log4±1e-5, 1.5, log5±1e-5, 2, 2.5, 3). n = 4096 at 1, 1.1, 1.5, 2, 2.5, 3. n = 8192 at 2 and 3.
- Variants at n ≤ 2048: full, Gamma-only, and Gamma + n∈{2,3}.
- Fourier transform: f̂(t) = ∫ f(u) e^{itu} du, computed exactly over cells (cosine transform for even modes, sine for odd). Real zeros on t ∈ (0.3, 45] are found with brentq and compared with the ordinates γ_k of the zeta zeros (mpmath).
- Scripts: `analyze2064.py`, `post2064.py`. Data: `res/*.npz|json`, `evec2064.json` (all diagnostics), `vectors_n2048_every8.json` (downsampled vectors).

## 1. Eigenvalue: the "plateau" is a mesh floor, not a continuum level
Constrained min (Ritz upper bound), with the 2nd and 3rd values in parentheses:

| A | 512 | 1024 | 2048 | 4096 | 8192 |
|---|---|---|---|---|---|
| 1.0 | 1.202e-2 | 1.191e-2 | 1.187e-2 | 1.186e-2 | – |
| 1.1 | 1.092e-3 | 9.660e-4 | 9.319e-4 | 9.220e-4 | – |
| 1.5 | 1.884e-4 | 5.563e-5 | 1.721e-5 | 5.062e-6 (7.33e-6, 4.44e-5) | – |
| 2.0 | 1.527e-4 | 4.861e-5 | 1.278e-5 | 3.493e-6 | 1.032e-6 (1.65e-6, 3.16e-6) |
| 2.5 | 1.782e-4 | 4.709e-5 | 1.305e-5 | 3.266e-6 | – |
| 3.0 | 1.193e-4 | 4.316e-5 | 1.279e-5 | 3.248e-6 | 9.070e-7 (1.46e-6, 2.36e-6) |

- At A ≤ 1.1 the value converges, so it is a resolved continuum level.
- For A ≥ 1.5 it falls by a factor of 3.2–3.9 at each doubling, roughly h^1.7–1.9, down to about 1e-6 at n=8192. At fixed n it is nearly independent of A. The "1e-5 plateau" is therefore the best-approximation error of the piecewise-constant cell basis, not a property of W. The second and third constrained eigenvalues fall at the same rate. This is a cluster of near-null directions, not one isolated null vector: the gap ratio λ2/λ1 is about 1.4–2.1.
- An h² Richardson extrapolation gives about 2e-7 at A=2 and 7e-8 at A=3. That is NUM only and cannot fix the sign. Connes–Consani report astronomically small minima for the comparable truncated Weil form (for example 2.4e-48 at λ²=11, i.e. log-length ≈ 2.4). Their space and normalization are not ours, so this is cited as context, not checked equivalence.

## 2. Eigenvector: smooth, even, grid-stable — not grid noise
Values at n=2048 unless stated; the pattern is the same on all grids.

| A | zero crossings | even fraction | edge mass (outer 10% each side) | PR | ∫f'² (Σ(Δf)²/h) | power > half-Nyquist | ⟨v,Q_neg⟩ |
|---|---|---|---|---|---|---|---|
| 0.694 | 2 | 1.000 | 0.201 | 0.649 | 154 | 5e-7 | 0.139 |
| 1.0 | 2 | 1.000 | 0.126 | 0.659 | 77 | 6e-8 | 0.004 |
| 1.1 | 2 | 1.000 | 0.061 | 0.579 | 66 | 1e-8 | 0.000 |
| 1.5 | 2 | 1.000 | 0.012 | 0.397 | 44 | 8e-11 | 0.000 |
| 2.0 | 2 | 1.000 | 0.041 | 0.514 | 21 | 9e-11 | 0.000 |
| 2.5 | 2 | 1.000 | 0.057 | 0.508 | 13 | 7e-11 | 0.000 |
| 3.0 | 2 | 1.000 | 0.084 | 0.561 | 9 | 2e-10 | 0.000 |

- The difference energy saturates under refinement. At A=3 it is 8.8, 8.9, 9.0 for n = 512, 1024, 2048, rather than scaling like 1/h². There is no checkerboard, no Nyquist content, and no edge ringing.
- The two nodes sit at u ≈ ±0.21A (±0.373 at A=2, ±0.628 at A=3). They are not at ±log p, and there are no kinks at ±log n.
- The 2nd constrained mode is odd, with 3 crossings, and also smooth.
- Grid overlaps |⟨f_n, f_2n⟩| (exact, nested cells): ≥ 0.9999 at A ≤ 1.1; 0.9993–0.9999 at log4± and log5±; 0.9986–0.9998 at A=2.5 and 3 (4096→8192 at A=3: 0.9979); A=2 0.9936–0.9996.
- A=1.5 is the weakest (1024→2048 0.9906, 2048→4096 0.9911, 512→2048 0.975). Its flank lobes move under refinement (fig2). The likely cause is mixing with the next even soft mode (λ3 is also small).
- Continuity in A (scaled coordinate x = 2u/A, n=2048): neighbours 0.98–0.996; 1.1→log4⁻ 0.918; 1.5→3.0 0.912; 1.1→3.0 0.993.
- Prime crossings: log4⁻ vs log4⁺ overlap 0.9999999997; log5± 0.99998. Eigenvalues agree to 3–4 digits. There is no jump when an atom enters, as expected from the vanishing-overlap onset.
- The plateau mode continues the A ≤ 1.1 constrained ground state. It is orthogonal (≤ 1e-3) to the unconstrained negative eigenvector of Q, even after that vector is projected into E0. So it is a different shape from the boundary-absorbed negative direction.
- Rayleigh split (A ≥ 1.5): the Gamma part is negative and the prime part positive, cancelling to about 5–6 digits (A=3: −0.9195 vs +0.9195; A=2: −0.4239 vs +0.4239).

## 3. The recognizable structure lives in Fourier space: zeros at the zeta ordinates
f̂(t) of the constrained ground state has real zeros at the ordinates γ_k of the zeta zeros. Error z−γ_k:

| A, n | γ1=14.1347 | γ2=21.0220 | γ3=25.0109 | γ4=30.4249 | γ5=32.9351 | γ6=37.5862 | γ7=40.9187 | γ8=43.3271 |
|---|---|---|---|---|---|---|---|---|
| 1.0, 4096 | 1.2e-1 | 6.9e-1 | 2.0 | (no match) | … | | | |
| 1.1, 4096 | 1.2e-2 | 1.3e-1 | 4.2e-1 | 1.1 | … | | | |
| 1.5, 4096 | −3e-5 | 9e-3 | 5e-3 | 4e-2 | 9e-2 | 0.19 | 0.7 | |
| 2.0, 4096 | 2e-5 | 3e-5 | 3e-5 | −3e-4 | −5e-4 | −4e-3 | 3e-2 | 2e-2 |
| 2.0, 8192 | 7e-6 | 1.5e-5 | 8e-6 | −7e-5 | −9e-5 | −3e-4 | −2e-3 | −4e-3 |
| 3.0, 4096 | −9e-6 | −1.5e-4 | −1.2e-4 | 2e-5 | −3e-5 | −1.2e-4 | 6e-5 | −8e-7 |
| 3.0, 8192 | −3e-6 | −3.5e-5 | −3e-5 | 7e-6 | −6e-6 | −2.6e-5 | 2.4e-5 | 3e-6 |

- |f̂(γ_k)| / max|f̂| ≈ 1e-7 (A=3, n=8192) for k ≤ 6.
- The odd second mode (sine transform) does the same: errors ≤ 1e-4 for γ1..γ7 at A=3, n=8192.
- The agreement sharpens with A (more zeros captured) and with n (errors fall about 2–4× per doubling). That is the opposite of noise.
- Not every zero is a zeta zero. f̂ also has extra zeros below γ1 and between zeta zeros (A=2: 8.39, 12.03, 18.57 at n=4096 → 8.46, 12.40, 18.92 at n=8192). These move under refinement and are not stable.
- Controls:
  - Gamma-only constrained form: not positive (min −0.535 at A=2). Its ground state's zeros are equally spaced, spacing 2π/A (A=2: 6.81, 9.91, 13.02, …; A=3: 4.48, 6.57, 8.65, …). These are window/sinc zeros with no arithmetic.
  - Gamma + {2,3} only: still negative at A ≥ 1.5. Zeros are unrelated to γ_k (A=2: 3.56, 8.48, 13.37, 14.91, …).
  - So the zeta-zero structure requires the full set of prime powers below e^A. It is not present with Gamma alone or with partial primes.

Exact identity behind this (not new): by the Weil explicit formula, the window form is the zero-side sum over nontrivial zeros ρ of terms in F̂ at ρ, with the poles removed by E0's conditions F̂(±i/2)=0. A vector with very small W must make F̂ nearly vanish at the low γ's. That is consistent only with zeros on the line, so it is an expected consequence of the trace formula, not evidence for RH. The phenomenon is the one Connes–Consani found ("Spectral triples and ζ-cycles", arXiv 2106.01715) and Connes–Consani–Moscovici developed ("Zeta zeros and prolate wave operators", arXiv 2310.18423; "Zeta spectral triples", arXiv 2511.22755). There, the Fourier transform of the even ground state of the truncated Weil form has real zeros reproducing the low zeta zeros, and it is the regularized determinant of a rank-one perturbation of the scaling operator on a circle of length L = log λ². Our finding is an independent reproduction inside the TAA complete-W cell model, plus the mesh diagnosis of the floor.

## Verdict: (iii) mixed, sharply split
- **Stable, recognizable (NUM):** the near-null eigenvector is a smooth, even, two-node, prolate-like bump continuing the A ≤ 1.1 ground state. It is grid-convergent (overlaps ≥ 0.99, saturating ∫f'², no Nyquist content), and its Fourier transform vanishes at γ1…γ8 to 1e-5–1e-6. That is a genuine arithmetic structure, but a spectral (zeros-side) one: no feature in u-space sits at ±log p.
- **Mesh-limited:** the eigenvalue, i.e. the "1e-5 plateau" itself, which is a cell-basis approximation floor (≈ h^1.8, now 1e-6 at n=8192). Also the extra non-zeta Fourier zeros, the A=1.5 flank lobes, and the choice of vector within the near-null cluster (λ1, λ2, λ3 all fall together).
- So the vector is a reliable object, but the number 1e-5 is not. No continuum sign above A=1.1 follows.

## Cautious analogy for Phi (analogy only; Phi not constructed; no cycle claimed)
- The near-null direction is characterized by duality with the zeros (f̂(γ_k) ≈ 0), not by local prime geometry. In the function-field picture this is like a class nearly orthogonal to the low Frobenius eigen-components, not a class supported near the graphs of individual correspondences.
- The u-space profile is global and unkinked. Each prime enters only through the global cancellation Gamma ≈ −primes, to 6 digits. So Phi(F) = ∫F(u)[Γ_u]du would need to send this vector to something whose pairing with the whole correspondence family nearly cancels, not to a local cycle.
- The Connes–Consani construction suggests a concrete operator-theoretic target to compare with: the rank-one-perturbed scaling operator whose determinant is f̂.
- Identifying this vector as a ζ-cycle in their sense is a statement about a spectral realization, not about a geometric cycle in a Hodge-index setting. The matching W = −(intersection) remains entirely open.

## Figures
- fig1_profiles_vs_A.png: profiles A = 0.694…3, raw and rescaled.
- fig2_grid_refinement.png: n = 512…8192 overlays at A = 1.5, 2, 3.
- fig3_fourier_zeta_zeros.png: log|f̂| with the zeta ordinates, for the even ground state and the odd second mode.
- fig4_eigenvalue_vs_h.png: the floor versus h.

# t2064 report: what the near-null eigenvector looks like

**Status:** NUMERICAL only. There is no continuum certificate above A=1.1, Phi is not constructed, and RH is unproved. Everything here is scratch work in ../evec2064/.

## Verdict: mixed, and the split is sharp
The eigenvalue and the eigenvector behave in opposite ways.

**1. The "1e-5 plateau" is a mesh floor.**
- The value is an artifact of the grid (cell basis), not a level of W.
- For A ≥ 1.5 the constrained minimum keeps falling as the grid is refined, roughly like h^1.8:
  - A=2: 1.5e-4, 4.9e-5, 1.28e-5, 3.5e-6, 1.03e-6 for n = 512, 1024, 2048, 4096, 8192.
  - A=3: 1.2e-4, 4.3e-5, 1.28e-5, 3.2e-6, 9.1e-7 over the same grids.
- At fixed n the value is almost the same for every A. That is why it looked like a plateau.
- The 2nd and 3rd constrained eigenvalues fall at the same rate. So there is a cluster of near-null directions, not one isolated null vector.
- At A ≤ 1.1 the value converges (A=1: 0.01186; A=1.1: 9.2e-4), so it is a real continuum level there.
- Context, not a checked equivalence: Connes–Consani report minima of order 1e-48 for the comparable truncated Weil form at a similar width.

**2. The eigenvector is a reliable, smooth object, not grid noise.**
- **Shape:** even, with exactly two nodes at u ≈ ±0.21A. It is a single prolate-like bump with negative flanks.
- **No grid-scale content:**
  - power above half-Nyquist ≤ 1e-9;
  - no checkerboard pattern;
  - the derivative energy ∫f'² saturates under refinement (A=3: 8.8, 8.9, 9.0).
- **Grid overlaps** n→2n are 0.998–0.9999. The weakest is A=1.5 at about 0.99, where the flank lobes still shift.
- **Continuous in A:** it continues the A ≤ 1.1 constrained ground state.
- **No jump at prime-power crossings:** the overlap across log4 ± 1e-5 is 0.9999999997.
- **Different from the negative direction:** it is orthogonal (≤ 1e-3) to the unconstrained negative eigenvector of Q.
- **No local prime features:** nothing in u-space sits at ±log p.

**3. The recognizable structure is arithmetic, and it lives in Fourier space.**
- The transform f̂(t) = ∫f(u)e^{itu}du of the ground state vanishes at the zeta-zero ordinates.
- At A=3, n=8192, the errors for γ1…γ8 (14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271) are −3e-6, −3.5e-5, −3e-5, 7e-6, −6e-6, −2.6e-5, 2.4e-5, 3e-6.
- |f̂(γ_k)| / max|f̂| ≈ 1e-7.
- The odd second mode does the same through its sine transform.
- The match improves both with A (more zeros captured) and with n.
- **Controls:**
  - With Gamma only, the constrained form is not positive, and the ground state's zeros are just equally spaced window zeros (spacing 2π/A).
  - With Gamma plus primes 2 and 3 only, the zeros have nothing to do with the γ_k.
  - So the structure needs the full set of prime powers below e^A.
- The transform also has extra, non-zeta zeros (e.g. 8.4, 12.0–12.4, 18.6–18.9 at A=2). These move under refinement and are not stable.

## How to say it to J.W.
The eigenvector under the floor is not discretization noise. It is a smooth, even, two-node profile that holds its shape across grids and across windows, and its Fourier transform vanishes, to about six digits, at the first eight zeta ordinates. That is a genuinely arithmetic signature, though not a new one. It is the "ζ-cycle" phenomenon of Connes and Consani (arXiv 2106.01715), developed further with Moscovici (arXiv 2310.18423, 2511.22755), here reproduced independently inside the complete-W cell model.

It is also exactly what the explicit formula predicts. W on E0 is a sum over zeros of terms in F̂ there, so any direction that makes W tiny has to nearly kill F̂ at the low γ's. That makes it a consequence of the trace formula, not evidence for RH.

What the grid does not resolve is the eigenvalue. The 1e-5 "plateau" is the cell basis's approximation floor. It shrinks like h² toward 1e-6 at n=8192, so it tells us nothing about the sign of the continuum form above A=1.1.

For Phi the hint is analogical, and it cuts against a local picture:
- The near-null direction is defined by duality with the zeros, not by features at ±log p.
- Its smallness comes from a global, six-digit cancellation between the Gamma part and the prime part.
- So the image of this vector would have to be a class nearly orthogonal to the low "Frobenius-eigen" components, rather than something localized on individual correspondences.
- The rank-one-perturbed scaling operator whose determinant is f̂ is a concrete spectral object to compare Phi against.

The vector is not claimed to be a geometric cycle. Constructing Phi, and matching W to minus the intersection pairing, remain open.

## Best figures
- ../evec2064/fig3_fourier_zeta_zeros.png (lead: log|f̂| dips at the zeta ordinates)
- ../evec2064/fig2_grid_refinement.png (profiles for n = 512…8192 at A = 1.5, 2, 3)
- ../evec2064/fig4_eigenvalue_vs_h.png (the floor scales with h)
- Also: fig1_profiles_vs_A.png, notes2064.md (full tables), evec2064.json, vectors_n2048_every8.json

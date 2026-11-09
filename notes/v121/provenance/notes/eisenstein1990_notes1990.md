# eisenstein1990: all-weight Eisenstein, the quasimodular anomaly, and irregular primes versus the Weil ledger

Run t1990 (pt1990u), 8 Nov 2026 CST. This is unpublished scratch: no repo or manuscript edits were made. **The Riemann Hypothesis is not proved.**

Labels:
- [V] machine-verified this run (exact rationals, or mpmath at 20–30 digits);
- [H] derived by hand, not separately machine-checked;
- [C] cited.

Files: `eis1990.py`/`eis1990.json` (exact q-series, Hecke, congruences), `analytic1990.py`/`analytic1990.json` (E2*, Kronecker, M_A, scattering), `ma_explicit1990.py`/`ma_explicit1990.json` (explicit-formula split of M_A), and `zeros400.json`.

## 0. The analogy first

The Serre-derivative correction and the Weil-ledger counterterm have the same anatomy:

- a derivative is made covariant by subtracting a logarithmic derivative of a "partition function" (Δ, or the completed L-function Λ_A);
- that subtraction has a scalar "vacuum" part and a convolution "spring" part;
- the non-holomorphic or pole anomaly is a residue term.

The modular case closes because SL₂(ℤ)-covariance forces the correction uniquely, and the remainder lands in a finite-dimensional space with Petersson positivity. The window case has only the ℤ/2 functional equation. That symmetry fixes only the scalar.

## 1. Level 1 facts [V and C]

- −I ∈ SL₂(ℤ) forces M_k = 0 for odd k. Odd weights are absent at level 1, and that is not a gap.
- M₂ = 0. E₂ = 1 − 24 Σσ₁(n)qⁿ is quasimodular: E₂(γz) = (cz+d)²E₂(z) + (6c/πi)(cz+d). [V] The S-transform residual is 3e−32 at z = 0.1+0.9i.
- E₂* = E₂ − 3/(πy) is modular of weight 2. [V] Residual 2e−31.
- E₂* = (12/πi) ∂_z log(√y |η|²). [H] This uses ∂_z log η = (πi/12)E₂ and ∂_z log √y = −i/(4y).
- Kronecker limit formula, with E(z,s) = Σ_{Γ∞\Γ} Im(γz)^s:
  E(z,s) = 3/(π(s−1)) + (6/π)[γ − log 2 − ζ′(2)/ζ(2) − log(√y |η(z)|²)] + O(s−1).
  [V] Checked to about 1e−9 at three points. The extra constant is −ζ′/ζ(2) = 0.5699609931.
  - The residue is 3/π = (1/2)/ξ(2), with ξ(2) = π/6 = vol(SL₂ℤ\H)/2.
  - The E₂ anomaly therefore comes from the pole of ξ at 1 (the residue of the constant-term factor φ(s) = ξ(2s−1)/ξ(2s)).
- Derivatives:
  - D = q d/dq.
  - Serre derivative: ϑ_k = D − (k/12)E₂ = Δ^{k/12} ∘ D ∘ Δ^{−k/12}, because DΔ = E₂Δ.
  - Maass derivative: δ_k = D − k/(4πy) = ϑ_k + (k/12)E₂*.
- The scalar k/12 has three equal readings:
  - −k ζ(−1);
  - k·vol/(4π), the valence/Gauss–Bonnet degree of the weight-k bundle;
  - k B₂/2.

## 2. General-weight correction formula [V for k ≤ 60, proof H]

**Theorem.** For even k ≥ 4,

  D E_k = (k/12)(E₂E_k − E_{k+2}) + f_k,  with f_k ∈ S_{k+2},
  a₁(f_k) = 2k + k(k−12)/(6B_k) − k(k+2)/(6B_{k+2}).

**Consequence.** f_k = 0 if and only if S_{k+2} = 0, that is, k ∈ {4, 6, 8, 12}. Only E₄, E₆, E₈ and E₁₂ "close". Every other weight has a cusp correction.

**Proof.**
1. ϑ_kE_k ∈ M_{k+2}, with constant term −k/12, so adding (k/12)E_{k+2} gives a cusp form.
2. The formula for a₁ follows by expanding the q¹ coefficient.
3. a₁ ≠ 0 at k = 10, where a₁ = 38016/691.
4. For k ≥ 14, a₁ ≠ 0 because |k(k−12)/(6B_k)| + |k(k+2)/(6B_{k+2})| < 2k. This was checked with exact Bernoulli numbers for 14 ≤ k ≤ 398 [V]. For larger k it follows from |B_k| > 2k!/(2π)^k.
5. For k = 4, 6, 8, 12 the space S_{k+2} is zero, so a₁ = 0. This gives the Bernoulli identities that the formula predicts.

Examples:
- D E₁₀ = (5/6)(E₂E₁₀ − E₁₂) + (38016/691)Δ.
- k = 2 is Ramanujan's quasimodular case: D E₂ = (E₂² − E₄)/12 [V].

Maass form of the same statement:

  δ_kE_k = (k/12)E₂*E_k − (k/12)E_{k+2} + f_k.

The constant term of the right side is −k/(4πy).

**Spectral content of f_k.**
- [V] Under T₂, the Krylov rank of f_k equals dim S_{k+2} for every k+2 ≤ 62. So every Hecke-eigen component of f_k is nonzero in that range.
- [H/C] Rankin unfolding (Zagier 1977, §1 Rankin identity) gives ⟨f_k, g⟩ = −(k/12)⟨E₂*E_k, g⟩ ∝ L(g,k+1)·L(g,k). Here δ_kE_k ⊥ cusp forms, and E_{k+2} ⊥ S.
- Both arguments lie in the region of absolute convergence (k > (k+3)/2). Each Euler factor is at least (1 − p^{(K−1)/2−s})² > 0, by Deligne's bound. So these values are positive trivially and carry no information about zeros.

## 3. Bernoulli primes [V and C]

- **Denominators of the cusp correction.** For k ≤ 60, the primes in the denominator of a₁(f_k) are exactly the primes of num(B_k/k) together with those of num(B_{k+2}/(k+2)).
- **Eisenstein–cusp congruences, checked for n ≤ 60:**
  - Dimension-1 weights, normalized form congruent to σ_{K−1}: K = 12 (691), 16 (3617), 18 (43867), 20 (283, 617), 22 (131, 593), 26 (657931).
  - Dimension ≥ 2 weights, where the T₂ characteristic polynomial has the root 1 + 2^{K−1} mod p:
    - K = 24 (103, 2294797);
    - K = 28 (9349, 362903);
    - K = 30 (1721, 1001259881);
    - K = 32 (37, 683, 305065927);
    - K = 34 (151628697551);
    - K = 38 (154210205991661).
  - Irregular pairs: (37, 32) checked; 59 at 44 and 67 at 58 appear in the denominators, but their congruences were not run.
  - Irregular primes reference: OEIS A000928.
  - Herbrand–Ribet: Ribet, Invent. Math. 34 (1976) 151–162.
- **Denominator primes (von Staudt–Clausen) are a different phenomenon.** E_{p−1} ≡ 1 mod p, the Hasse-invariant lift, holds for p = 5 through 23 [V].
- **Sign versus valuation.** ζ(1−K) = −B_K/K is positive for K ≡ 0 mod 4 and negative for K ≡ 2 mod 4. That is real (archimedean) data. A congruence is p-adic closeness between an Eisenstein series and a cusp form. It is not an inequality and cannot sign W.

## 4. The Weil side: exact identities [V]

- **The bulk symbol is a log-derivative.**
  m_A(x) = Re ψ(1/4 + ix/2) − log π − 2Σ_{log n<A} a_n cos(x log n) = 2 Re (Λ_A′/Λ_A)(1/2 + ix),
  where Λ_A uses the truncated −ζ′/ζ series.
- **The counterterm is the zero-frequency value.**
  M_A = −m_A(0) = 2(S_A − S_reg),
  with S_A = Σ_{log n<A} Λ(n)n^{−1/2} and
  S_reg = −ζ′/ζ(1/2) = Γ_R′/Γ_R(1/2) = K₀/2 = −2.686091709612833.
  The middle equality is the functional equation: (Λ′/Λ)(1/2) = 0.
  [V] Identical to 20+ digits for A = 0.6, 1, 2, 3. For example M₁ = 6.352441562694 and M₂ = 11.224651783578.
  So M_A is "partial sum minus regularized sum". This is the exact analog of Serre's scalar −k/12 = kζ(−1).
- **Explicit-formula split of the counterterm.** With x = e^A not a prime power and the zero sum taken symmetrically:
  M_A = 4e^{A/2} − 2Σ_ρ e^{A(ρ−1/2)}/(ρ−1/2) + 2Σ_{k≥1} e^{−(2k+1/2)A}/(2k+1/2).
  - The first term is the pole at s = 1.
  - The middle term is the zeros. For zeros on the line it equals −4Σ_{γ>0} sin(γA)/γ.
  - The last term is the trivial zeros. Its rates 2k+1/2 are the archimedean Ornstein–Uhlenbeck (OU) rates.
  - E0 kills the pole's rank-2 part P. The pole's diagonal footprint 4e^{A/2} stays in M_A.

  [V] Numerical check, with 400 zeros (truncation error about 1e−2, so not certified):

  | A | M_A | 4e^{A/2} | Γ tail | zero part needed | 400-zero sum |
  |---|-----|----------|--------|------------------|--------------|
  | 0.6 | 5.37218 | 5.39944 | 0.21651 | −0.24376 | −0.23144 |
  | 1.0 | 6.35244 | 6.59489 | 0.07112 | −0.31357 | −0.31799 |
  | 1.5 | 8.31416 | 8.46800 | 0.01935 | −0.17320 | −0.17068 |
  | 2.0 | 11.22465 | 10.87313 | 0.00545 | +0.34608 | +0.33727 |
  | 3.0 | 18.38784 | 17.92676 | 0.00044 | +0.46064 | +0.44428 |

  The zero-dependent part of the counterterm, in the minimal-cutoff gauge, oscillates with size 0.07–0.46. At A = 1 it far exceeds the uncertified E0 margin of about 0.012. So no zero-free scalar can replace M_A in this gauge without changing the sign question.
- **Eisenstein scattering versus the Weil symbol.** [V] To full precision at t = 0.7, 3.1, 14.13, 20:
  −φ′/φ(1/2 + it) = 4 Re (Λ′/Λ)(1 + 2it).
  - The modular-surface time delay is the Weil symbol moved to the edge line σ = 1, at doubled frequency.
  - Maass–Selberg positivity of truncated Eisenstein norms therefore yields ζ(1+it) ≠ 0 (Jacquet–Shalika 1976/77; Sarnak 2004). It does not reach the critical line.
  - The Weil constant S_reg = −ζ′/ζ(1/2) corresponds to the Eisenstein parameter s = 1/4, which is non-unitary.
  - This is consistent with Zagier's 1981 renormalized Rankin–Selberg transform, whose possible poles include ρ/2, and with the atlas node eisenstein_resonances_rho_half.
- **Gauge freedom.** On window-A tests, adding to m_A any g whose Fourier transform is supported in |u| ≥ A leaves W unchanged. Going from cutoff A to A′ > A moves M_A to M_{A′}, and the new springs compensate exactly.
  - So the scalar counterterm is a gauge choice; the minimal cutoff gives M_A.
  - [C, H] Positivity on all window tests is equivalent to a positive-definite extension of the Weil distribution from (−A, A) (Krein 1940). The E0 variant, with two moment constraints, was not worked out here.
  - Serre's correction is unique, because SL₂(ℤ) acts and M_{k+2} is finite-dimensional. The window correction is not unique: it is an infinite-dimensional family of gauges.

## 5. Answer and obstacle

**Dictionary.**

| Modular side | Weil side |
|---|---|
| scalar k/12 | M_A = −m_A(0) = 2(S_A − S_reg) |
| (k/12)(E₂ − 1) convolution | springs |
| 3/(πy) residue anomaly | P (killed by E0) |
| −(k/12)E_{k+2} boundary | the E0 moments |
| cusp remainder f_k | no independent analog; the zero part of M_A is the "spectral" piece |

**Verdict.** Every Eisenstein, quasimodular or irregular-prime "correction" is structural calibration only. None is the missing subtraction:
- k/12 and 3/π are finite constants. They cannot reproduce M_A(A) = 4e^{A/2} + (zero sawtooth) + (Γ tail).
- f_k is controlled by absolutely convergent L-values.
- Bernoulli primes are p-adic.

No universal no-go is claimed.

**Precise obstacle.** An independent object would be an explicit positive extension, or a covariance group stronger than ℤ/2, that fixes the out-of-window gauge from Gamma and prime data alone. Under RH, the zero measure is such an extension, which is circular. Eisenstein constructions see Λ only on σ = 1 (the 2s doubling) or at s = 1/4, where unitarity fails.

**Tests any proposed modular correction must pass.**
1. Reproduce M_A exactly, including its A-dependence and the zero part −0.3136 at A = 1 and +0.3461 at A = 2.
2. Be gauge-covariant under A → A′.
3. Give a sign on E0, not just on the even sector.

**Weight-12 audit, reconciled.** 2(ψ(K/2) − log 2π) = 2(log Γ_C)′(K/2) is the correct weight-K analog of K₀ = 2(log Γ_R)′(1/2). By the functional equation it equals −2L′/L(g, K/2) when L(g, K/2) ≠ 0 [H]. k/12 is the global Serre/valence constant. Their mismatch is expected: local central Gamma versus global degree.

## Sources
- Zagier, "Elliptic modular forms and their applications" (1-2-3 of Modular Forms): https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-74119-0_1/fulltext.pdf
- Zagier 1977, LNM 627, pp. 105–169: https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BFb0065299/ModFormsZetaValues.pdf (doi 10.1007/BFb0065299)
- Zagier 1981/82, J. Fac. Sci. Univ. Tokyo 28, 415–437: https://people.mpim-bonn.mpg.de/zagier/files/rankin-selberg/fulltext.pdf (doi 10.15083/00039589)
- Ribet 1976, Invent. Math. 34, 151–162 (bibliographic record: https://www.mathstat.dal.ca/~dilcher/bernr.html)
- Sarnak 2004, "Nonvanishing of L-functions on ℜ(s)=1": https://publications.ias.edu/taxonomy/term/39?page=2, which cites Jacquet–Shalika, Invent. Math. 38 (1976/77)
- Krein 1940, C. R. (Doklady) Acad. Sci. URSS 26, 17–22 (MR0004333)
- OEIS A000928: https://oeis.org/A000928

The Riemann Hypothesis is not proved.

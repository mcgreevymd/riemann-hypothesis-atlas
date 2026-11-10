# t2072 report: the u → 0 cutoff, matched against W

**Short version.** The cutoff already built into the t2068 pairing reproduces H_A − M_A‖F‖² exactly. The divergence is removed by subtracting it; nothing cancels it. The result has the opposite sign: the renormalized pairing equals −(W − P). On E0 that is exactly −W. Off E0 the pole term P is missing, because no fixed point produces it. None of this gives a sign. Positivity on E0 is still Weil's criterion, i.e. the Riemann hypothesis.

## What was compared
- W = P + H_A − M_A‖F‖² (counterterm1995/notes1995.md l.7; multiprime2047/notes2047.md §A; inertia2057/notes2057.md §1).
- H_A = ∫_0^∞ k∞(a)‖F − T_aF‖² da + Σ_{log n<A} a_n‖F − T_{log n}F‖², a nonnegative jump energy.
- M_A = −K0 + 2Σ_{log n<A} a_n, with K0 = ψ(1/4) − log π = −5.37218.
- P = 2 Re C₊ conj C₋.
- Sign convention: W = +Σ_ρ ĝ(γ_ρ). The zeros were used only to check this convention (residual 7e-26).

## Regularization
Connes 1999 (Thm 3 local, Thm 4 semilocal): Tr(R_Λ U(h)) = 2h(1) log Λ + Σ_v ∫'_v. Here h(x) = |x|^{−1/2} g(log|x|) and g = F ∗ G̃. The Haar measure is normalized by ∫_{1≤|u|≤Λ} d*u ~ log Λ. That normalization is the t2068 factor of ½ over the two signs, and it is also where the log p in Λ(n) comes from.

At ∞, in the log variable: ∫'_R = Pf₁∫k∞(|a|)g(a)da + (γ + log 2π)g(0).

## Results
⟨Φ(F),Φ(G)⟩_ren = lim[Tr − 2⟨F,G⟩ log Λ]
= (γ + log 2π + π/2 + 2 log 2 + 2Σ_{log n<A} a_n)⟨F,G⟩ − H_A(F,G)
= M_A⟨F,G⟩ − H_A(F,G) = −(W − P)(F,G).

The middle step uses −K0 = γ + log 8π + π/2 and FP_H∫_0^∞ 2k∞ = π/2 + 2 log 2.

1. **Divergence: MISMATCH with the checklist.** The only divergence is +2⟨F,G⟩ log Λ, and it is subtracted. With an ε cutoff instead, the pole is g(0) log(1/ε) over both sides, or ½ per side. It has the same sign as the log Λ term, so the two never cancel. In the Λ scheme the ε pole does not appear at all.
2. **Diagonal: H_A MATCH and M_A MATCH**, exactly, in degree form. The literal δ₀ coefficient of the trace is γ + log 2π. The rest of M_A, namely π/2 + 2 log 2 + 2Σa_n, comes from rewriting the transverse kernel and the prime atoms in degree form. The checklist got this wrong: the digamma constant belongs to M_A, and H_A is jump energy.
3. **Relative signs: MATCH.** The Archimedean, prime, and diagonal sectors each enter with a factor of −1. The prime sum is +Σa_n in the trace and −Σa_n in W.
4. **Overall sign: −W on E0 (MATCH).** Off E0 the pairing is −W + P (PARTIAL), because P is not produced. So B_W(F,G) = −⟨Φ(F),Φ(G)⟩_ren holds on E0.

## Checks
- Exact window check: A = 1.1, F ≠ G, both non-even, with log 2 and log 3 active. The residual is 1.3e-40, and trace − (−W) equals P.
- Independent rerun by nested quadrature: residual 1.4e-16.
- Constants: FT of Pf 1/|x|, FP_H, K0 and the Gamma expansion all agree to about 1e-30.

## What is left
- No sign, and no (1,1) home (Open ~1.8).
- This is a semilocal theorem. The global operator-trace statement on X is Connes' formula, which is equivalent to RH.
- This repeats counterterm1995 §1 and §8 in the t2068 convention, extended to F ≠ G.

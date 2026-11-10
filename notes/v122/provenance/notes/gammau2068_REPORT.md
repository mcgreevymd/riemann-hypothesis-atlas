# t2068 report — [Γ_u] for real u

**Short version.** I wrote the family for every real u. I also wrote Φ, but only as a distribution-valued integral. Its pairing is defined without the zeros. The prime and Gamma parts of that pairing come from a fixed-point calculation, and they match Λ(n)/√n and k_∞. What is still missing is a geometric home with a real intersection product, plus a sign theorem. Φ has not been built as a map into a sign-controlled primitive (1,1) sector, and the Riemann hypothesis is not proved.

## Written
- **Ambient:** the adèle class space X = A_Q/Q^×, with Bruhat–Schwartz test functions. Let λ_u = (e^u, 1, 1, …) be the scaling idèle.
- **[Γ_u], for every real u:** the graph of scaling with a half-density weight, ⟨[Γ_u], K⟩ = e^{−u/2} ∫_A K(λ_u x, x) dx. This is the Schwartz kernel of the unitary scaling θ_u. It uses no zeros, no ξ'/ξ and no explicit formula.
- **Φ(F) = ∫ F(u)[Γ_u] du:** a well-defined distribution kernel, namely the kernel of θ(F), in the weak-* topology.
- **Pairing:** Φ(F)·Φ(G) := the distributional fixed-point trace of θ(F∗G̃). This reduces to a single distribution τ(a) = [Γ_a]·Δ.
- **Fixed-point computation** (the local terms in Connes 1999, rechecked in check_local.py):
  - The locus x_∞ = 0 is present for every u. Its index, averaged over the sign ±1 in R^×, is e^{−a/2}/(1−e^{−2a}) = k_∞(a). So the hyperbolic denominator is the fixed-point index of scaling on the real line.
  - The locus x_p = 0 is present only when u ∈ Z·log p. It gives atoms log p·p^{−k/2} = Λ(n)/√n at ±log n.
  - Prime powers therefore enter as fixed loci of the graph meeting the diagonal, not as special graphs.

## Matching conditions (open)
- u → 0: Γ_0 = Δ, and the self-intersection diverges. It needs a cutoff Λ, which gives a 2 log Λ term plus principal values. I have not checked that this reproduces H_A − M_A‖F‖², and I have not fixed the overall sign against −W.
- My guess is that E0 = ker C+ ∩ ker C− corresponds to Connes's codimension-2 space {f(0) = 0, f̂(0) = 0}. That would realize the rank-two boundary plane. This is a guess and still needs checking.

## Analogy only
- A Deninger foliation or flow for Spec Z is conjectural.
- The isotropic and Frobenius orthogonality picture from t2064–65 remains an analogy.

## Missing
1. **An ambient with an intersection product.** The graphs need to live as cycles or currents with a real cup product and a primitive decomposition. X has none, so this is a trace pairing, not an intersection of (1,1)-currents. The best candidate is the square of the Connes–Consani arithmetic site. There, Frobenius correspondences Ψ(λ) are already built for all real λ > 0, with Ψ(λ)∘Ψ(λ') = Ψ(λλ') except for a tangential correction when λλ' is rational. The missing pieces are intersection theory on that square and a proof that Ψ(e^u)·Ψ(e^v) = τ(u−v).
2. **A sign theorem.** We need a Hodge-index or Castelnuovo–Severi type theorem on the completed primitive part, proved geometrically. On X, positivity of this pairing on E0 is exactly Weil's criterion, which is RH, so X gives no independent sign.
3. **A next step we can check now.** Work out the diagonal regularization and the rank-two plane against H_A, M_A and C±.

## Candidates that failed
- **Graphs of x ↦ x^n on G_m or P^1 over Z:** only discrete n, and the global numbers never produce Λ(n).
- **Interpolating Frobenius:** there is no flow over Spec Z.
- **Extending from the atoms at log n:** these points have no accumulation point, so continuity fixes nothing. Pinning the values in between by k_∞ would define Γ_u from W, which runs backwards.

## A refinement of t2065
That turn called the Connes-style route circular. That holds for the spectral realization, the quotient whose spectrum is the zeros. The geometric side (graphs and fixed points) is zeros-blind, and it does compute the prime and Gamma pieces independently of W. What it lacks is a geometric ambient and a sign theorem.

## Overclaims to avoid
- "Φ is constructed."
- "k_∞ comes from the diagonal self-intersection." It comes from the locus x_∞ = 0, which is present for every u.
- "This is an intersection pairing of (1,1)-currents."
- "This gives positivity."
- Any statement that the Riemann hypothesis follows.

# t2068 — an independent definition of [Γ_u] for real u (scratch notes)

Scope: J.W. authorized (pt2068u) writing a zeros-blind geometric definition of [Γ_u] for real u, or else
a precise list of what is still missing. Scratch only; nothing pushed. RH is NOT proved. Φ is NOT claimed
constructed as a map into a sign-controlled primitive (1,1) sector.

Labels used throughout: **[WRITTEN]** = an actual definition/computation (ours or in the literature, cited);
**[MATCH]** = a matching condition against W that is checked or still to be checked; **[ANALOGY]** = structural
analogy only; **[MISSING]** = a concrete ingredient nobody has supplied.

Formal W (for matching only, never for defining Γ_u): W = P + H_A − M_A‖F‖² on E0 = ker C+ ∩ ker C−,
k_∞(a) = e^{−a/2}/(1−e^{−2a}), prime atoms Λ(n)/√n at ±log n, rank-2 boundary plane from exponential moments.

---------------------------------------------------------------------------------------------------
## 1. Survey of candidates for a real-u family

### 1a. Graph of x ↦ x^n (or multiplication) on G_m / P^1 over Z — fails to give real u, fails the weights
- Over Z the only endomorphisms of G_m are x ↦ x^n, n ∈ Z. "Multiplication by e^u" is not algebraic; it exists
  only on the archimedean fiber G_m(R) = R^×. So no real-u family on the integral model. **[WRITTEN: obstruction]**
- Even at discrete n: the graph of x^n on P^1_Z × P^1_Z is a genuine divisor (bidegree (n,1)), but its global
  intersection numbers are polynomial in n (degree data), and its arithmetic heights involve roots of unity
  (Mahler measure 0). Λ(n) only appears after localizing at the fiber over p, where x^p ≡ Frobenius.
  So the weight Λ(n)/√n is not produced globally. Dead end for Φ. **[WRITTEN: obstruction]**

### 1b. Continuous interpolation of Frobenius graphs — not available
- Over F_q, Frobenius is one map and its powers are discrete (u ∈ Z log q). Over Spec Z there is no geometric
  Frobenius at all, let alone a flow. Nothing in the literature constructs one on a scheme. One must not pretend
  the discrete Γ_{p^k} already define Γ_u for generic u. **[WRITTEN: obstruction]**

### 1c. Distribution/current extension from the atoms u = log n — underdetermined
- {log n} has no accumulation point in R (gaps ≥ log(1+1/n) > 0). Weak continuity in u therefore imposes
  NO constraint between atoms: any family agreeing at the atoms is an "extension". The extension is maximally
  non-unique. **[WRITTEN]**
- The only way to pin it is to impose a kernel between the atoms. Imposing that Γ_u·Γ_v reproduce k_∞(u−v) is
  defining Γ_u from W — backwards, forbidden. **[WRITTEN: rejected]**

### 1d. Deninger foliated dynamical system — conjectural for Spec Z
- Deninger conjectures a foliated space with an R-action (flow φ^t) whose closed orbits have lengths log p,
  with a leafwise cohomology H^1 carrying an R-action whose infinitesimal generator has the zeros as spectrum,
  plus a Hodge ⋆ giving positivity. Toy foliated/laminated systems with analogous dynamical trace formulas exist
  (Deninger; Kopei; Leichtnam), but NO such space is constructed for Spec Z. Treating it as written would be an
  overclaim. **[ANALOGY / MISSING]**

### 1e. Scaling action on the adèle class space X = A_Q/Q^× — written, zeros-blind; this is the pick
- The idèle class group C_Q, in particular R_+^× embedded at the archimedean place, acts on X by scaling.
  This action is defined with no reference to zeros. Its graph for λ = e^u is a well-defined subset of X × X
  for EVERY real u (not just log n), and it can be made a distribution (Schwartz kernel). See §2. **[WRITTEN]**
- Caveat: X is a noncommutative (bad) quotient, not a scheme or complex manifold; "(1,1)-current" is not
  literally defined there. The graph is a distribution kernel, not a (1,1)-current. **[WRITTEN: limitation]**

### 1f. Connes–Consani arithmetic site and its square — written for real λ, no intersection theory yet
- Connes–Consani (C. R. 2014; Adv. Math. 2016 "Geometry of the arithmetic site") build the arithmetic site
  (topos N^×^ with the tropical semiring structure sheaf), its square (structure sheaf Z_min ⊗_B Z_min), and
  **Frobenius correspondences Ψ(λ) for every λ ∈ R_+^×**, as congruences on Newton polygons (half-planes of slope λ;
  irrational λ via best rational approximations). Composition: Ψ(λ)∘Ψ(λ') = Ψ(λλ') when λλ' ∉ Q, and when λ, λ'
  are rational; for λ, λ' irrational with λλ' ∈ Q one gets Id_ε∘Ψ(λλ'), Id_ε the tangential deformation of the
  identity. The points over R_max^+ are tied to (a quotient of) the adèle class space. **[WRITTEN, literature]**
- This is the only place in the literature where a real-parameter family of *correspondences* (not just an
  operator) is constructed in a geometric setting. What is not there: an intersection pairing on the square
  with a primitive decomposition and a Hodge-index-type sign. **[MISSING]**

Pick: write [Γ_u] concretely on X (§2), because its pairing can actually be computed locally; record 1f as the
geometric home that would have to be upgraded.

---------------------------------------------------------------------------------------------------
## 2. The definition **[WRITTEN]**

Ambient. A = A_Q, Haar measure dx; S(A) Bruhat–Schwartz functions; X = A/Q^×. For u ∈ R put
λ_u := (e^u, 1, 1, …) ∈ A^× (archimedean component e^u, all finite components 1); |λ_u| = e^u.
Unitary scaling: (θ_u ξ)(x) = e^{−u/2} ξ(λ_u^{−1} x), so θ_u θ_v = θ_{u+v}, θ_u^* = θ_{−u}.

Graph. For every real u, [Γ_u] is the distribution on A × A (test space S(A × A)) given by

  ⟨[Γ_u], K⟩ := e^{−u/2} ∫_A K(λ_u x, x) dx ,

i.e. integration over the graph {(λ_u x, x)} of scaling, with half-density weight. It is the Schwartz kernel of θ_u.
On X × X one descends by the Q^×-action (the diagonal Q^× acts on both factors; graphs are Q^×-invariant because
scaling commutes with Q^×). No zeros, no ξ'/ξ, no explicit formula used.

Family integral. For F ∈ C_c^∞(I_A),

  Φ(F) := ∫ F(u) [Γ_u] du ∈ S'(A × A),  ⟨Φ(F), K⟩ = ∫ F(u) ⟨[Γ_u], K⟩ du,

well defined because u ↦ ⟨[Γ_u], K⟩ is smooth for Schwartz K. Φ(F) is the Schwartz kernel of θ(F) = ∫ F(u) θ_u du.
Topology: weak-* on S'(A × A) (equivalently strong operator topology on θ(F)). Φ is linear and continuous
from C_c^∞(I_A) into these kernels. **This writes the integrand family and Φ as a distribution-kernel-valued
integral. It does not land in a space of real (1,1)-currents, because X has none.**

Specialization at u = log n. Γ_{log n} is NOT a Frobenius graph on its own: scaling by n at ∞ equals scaling by
1/n at the finite places modulo Q^× (n ∈ Q^×). What is special about u = k log p is the fixed-point set:
Γ_u ∩ Δ contains the locus X_p = {x : x_p = 0} exactly when e^u ∈ |Q_p^×| = p^Z, i.e. u ∈ Z log p
(isotropy Q_p^×, orbit period log p). So prime powers appear as **non-transverse fixed loci of the graph with the
diagonal**, not as special graphs. **[WRITTEN]**

u → 0. Γ_0 = Δ. The self-intersection Δ·Δ is totally non-transverse and divergent; in Connes' treatment it requires
a cutoff Λ and produces a term 2 h(1) log Λ, plus principal values (Weil's Pf) at u = 0 from the archimedean and
unit (|u|_p = 1) parts. That is the "regularization of the diagonal". We did NOT compute that it equals
H_A − M_A‖F‖². **[WRITTEN: structure; MATCH: open]**

---------------------------------------------------------------------------------------------------
## 3. The pairing

### 3a. Definition (independent of W) **[WRITTEN, with caveats]**
Use group composition: Γ_u ∘ Γ_v^T = Γ_{u−v}. Define

  Φ(F) · Φ(G) := ⟨Φ(F) ∘ Φ(G)^T, Δ⟩ = Tr_distr θ(F ∗ G̃),  G̃(u) = conj G(−u),

the distributional (Atiyah–Bott / Guillemin–Sternberg) trace, computed by fixed points of the flow.
So everything reduces to the one distribution τ(a) := "[Γ_a] · Δ", and Φ(F)·Φ(G) = ∫∫ F(u) conj G(v) τ(u−v).
Translation invariance makes Γ_u·Γ_v depend only on u − v; u = ±v gives τ(0) (diagonal, divergent) and τ(±2u).

### 3b. Computation of τ by fixed points (zeros-blind; Connes, Selecta 1999, local terms) **[WRITTEN, literature + our check]**
- Locus x_∞ = 0, present for every u. Transversal direction is the line R with x ↦ ±e^{−a} x; Lefschetz index
  1/|1 − λ|. Averaging the two signs (even sector) with half-density e^{−a/2}:
    e^{−a/2}·½(1/(1−e^{−a}) + 1/(1+e^{−a})) = e^{−a/2}/(1 − e^{−2a}) = k_∞(a),
  and the |λ| > 1 side gives the same function of |a|. Checked symbolically/numerically (check_local.py,
  check_local.out). **So the hyperbolic denominator 1 − e^{−2a} is literally the fixed-point index of scaling on
  the real line, summed over the sign ±1 ∈ R^×.** This answers the t2067 "origin of k_∞" question at the level of
  the fixed-point formula, without using W. **[WRITTEN]**
- Locus x_p = 0, present for u = k log p. Index 1/|1 − λ|_p = 1 for |λ|_p < 1 (and |λ|_p^{−1} on the other side),
  half-density p^{−k/2}, orbit period log p: atom weight log p · p^{−k/2} = Λ(p^k)/√(p^k) at ±k log p. Checked. **[WRITTEN]**
- u = 0: divergent, cutoff 2 log Λ and Pf's (see §2). **[MATCH open]**

### 3c. Comparison to −W (schematic)
Prime atoms: match. Archimedean kernel: matches k_∞. Subtraction/boundary terms H_A, M_A and the rank-2 plane:
not matched. Structural guess: E0 = ker C+ ∩ ker C− ↔ Connes' codimension-2 subspace S(A)_0 = {f(0) = 0, f^(0) = 0}
(the two "trivial" classes H^0, H^2 / poles at s = 0, 1, i.e. the hyperbolic framing). **[ANALOGY, to be checked]**
Overall sign convention (pairing = −W vs +W) must be fixed by this matching. **[MATCH open]**

### 3d. What this pairing is NOT
- It is a trace on a noncommutative space, not a cup product on H^{1,1} of a geometric object. There is no
  primitive decomposition and no Hodge index theorem attached.
- Global rigor: the semilocal version (finitely many places S) is a theorem (Connes). The global version needs
  the cutoff; Connes showed the global trace formula (in his Hilbert-space setting) is equivalent to RH; Meyer
  (2005) gives an unconditional version in a non-Hilbert (Schwartz-type) setting, without positivity.
- Positivity of this pairing on the E0-analogue IS Weil's criterion, i.e. RH. So it supplies NO independent sign.
- Line held from t2065: we used only the geometric side (graphs, fixed points). The spectral realization
  (cokernel of S(A)_0 → S(C_Q), spectrum = zeros) was not used; using it would be circular.
  Refinement of t2065: the geometric side of Connes' setup IS zeros-blind and DOES compute the prime and Gamma
  pieces independently of W; what it lacks is a geometric ambient with a sign theorem.

---------------------------------------------------------------------------------------------------
## 4. Honesty ledger

- Family [Γ_u] for all real u: **written** (graph of scaling on X = A_Q/Q^×, as a distribution kernel).
- Φ(F) = ∫ F(u)[Γ_u] du: **written as a distribution-kernel-valued integral**, NOT as a map into a completed
  real (1,1)-current space or a primitive sector.
- Pairing: **defined** as distributional fixed-point trace; **local prime and archimedean terms computed and match**
  Λ(n)/√n and k_∞; subtraction/boundary terms **not matched**; global version needs a cutoff.
- Sign: **none**. Positivity of this pairing on E0 is equivalent to RH.

### Missing ingredients (concrete)
M1. A geometric ambient where these graphs are cycles/currents with a genuine intersection (cup) product, Künneth
    and a primitive decomposition w.r.t. an ample class. Best literature candidate: the square of the Connes–Consani
    arithmetic/scaling site, where Ψ(λ), λ ∈ R_+^×, already exist — what is missing is an intersection theory on the
    square, and a proof that Ψ(e^u)·Ψ(e^v) equals the fixed-point τ(u − v) above.
M2. A Hodge-index-type sign theorem on the completed primitive part of that ambient, proved by geometry and not via
    zeros (Castelnuovo–Severi analogue). Any such theorem implies RH; nothing supplies it now.
M3 (checkable now). The canonical regularization of Δ·Δ: relate Connes' cutoff log Λ and Pf's to our window A, and
    check whether they reproduce H_A − M_A‖F‖², and whether E0 ↔ S(A)_0 realizes the rank-2 boundary plane.

### Overclaims to avoid
- Not "Φ is constructed": only the integrand family and a kernel-valued Φ.
- Not "k_∞ comes from the diagonal self-intersection": it comes from the transversal fixed locus x_∞ = 0, present
  for every u; the diagonal (u = 0) gives only the divergent/subtraction part.
- Not "the pairing is an intersection pairing of (1,1)-currents": it is a Lefschetz trace on a noncommutative space.
- Not "the geometric side gives positivity": its positivity is RH.
- Do not say Deninger's flow or an arithmetic Frobenius flow exists for Spec Z.
- Do not define the in-between values of Γ_u so that intersections equal k_∞ (backwards).

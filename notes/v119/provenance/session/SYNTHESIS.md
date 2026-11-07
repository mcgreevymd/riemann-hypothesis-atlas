# Where could the sign of the Weil pairing come from? — synthesis of the 6 Nov 2026 session (TAA, J. W. McGreevy)

> **Status.** The Riemann Hypothesis is **not** proved here, and nothing below claims progress toward a proof.
> This is a curated research record. Labels: **[EXACT]** proved here (elementary) or a cited theorem; **[NUM]** finite numerics
> (Galerkin values are upper bounds, never certificates of positivity; a negative value with an explicit vector *is* a certificate);
> **[ANALOGY]**; **[TARGET]** a precisely stated open requirement; **[PRIOR]** already in the literature or the atlas.
> Work by Grok Bot (AI-assisted) for J. W. McGreevy. Times are America/Chicago (CST).

## 0. One-paragraph overview
Weil's criterion says RH ⇔ a certain Hermitian form W (the Weil pairing: pole term + archimedean term − prime-power term) is ≥ 0 on test
functions. Tonight's thread asked whether physics-style "positivity from squares" (harmonic/anharmonic oscillators, uncertainty
relations, Tate's Fourier/Poisson structure, spinors, instantons, Virasoro/no-ghost, supersymmetry) can supply that sign
*independently of the zeros*. The answer, made precise in several exact computations, is a single pattern: **in every mechanism the
form splits as ‖Φ·‖² + (an indefinite boundary/charge term), and the square ‖Φ·‖² comes from an independent positive structure
(a metric, a polarization, a positive representation).** The boundary data of Tate's thesis carry exactly such an indefinite
(hyperbolic, signature (1,1)) term, so they cannot be the sign source; the sign must come from the bulk W on the constrained space
E0. Over a finite field the bulk sign is the Hodge index theorem, and tonight's control tests reproduce that split exactly. For ζ the
independent map Φ is **missing**; any exact version of it is equivalent to RH.

## 1. Objects and conventions [EXACT]
- Log line: F(u) = e^{u/2} f(e^u) (unitary L²(R₊, dx) → L²(R, du)); ev_s(F) = ∫ F(u) e^{(s−½)u} du (Mellin at s); F^♯(u) = conj F(−u).
- **E0** = {ev₀ = ev₁ = 0}: the two pole constraints. Since ev_s(F∗G) = ev_s(F)ev_s(G), E0 is a convolution ideal, ♯-stable.
- L = ∂² − ¼: ev_s(LF) = s(s−1) ev_s(F); L: C_c^∞ → E0 ∩ C_c^∞ is a bijection preserving support hulls.
  **[PRIOR]** Connes–Consani 2021, Lemma 3.3 (ii)–(iv) (operator −(ρ∂_ρ)² + ¼); Prop. 3.5: positivity on C_c^∞(I) ∩ J ⇔ positivity of φ∘Q on C_c^∞(I).
- On a fixed window [−A/2, A/2] and F ∈ E0 (real), with K(r) = Re ψ(¼ + ir/2) − log π and a_n = Λ(n) n^{−1/2}:
  W(F) = ⟨F, K(D)F⟩ − Σ_n a_n 2Re⟨F, T_{log n}F⟩ (pole term P = 2ab vanishes on E0; prime sum finite on the window).
  W is a **quadratic form on window spaces** (K(D) ~ log|D| is unbounded), not a bounded multiplication operator on all of L².

## 2. Findings (curated)
**F1 — A zeros-blind spring network represents W; its sign is a signed balance, not a domination. [EXACT + NUM]**
Exact (cutoff-free on a window; atlas r341/r423 prior for the Lévy–Khintchine part):
W(f)/‖f‖² = K(0) + ∫₀^∞ k_∞(a)(2 − 2ρ_f(a)) da − 2 Σ_n a_n ρ_f(log n), with ρ_f(b) = ⟨f, T_b f⟩/‖f‖², k_∞(a) = e^{−a/2}/(1 − e^{−2a}).
The archimedean springs are restoring; prime springs help or hurt according to the sign of the autocorrelation at lag log n.
μ_min is concave in the weights, so the positivity region is convex in (K(0), k_∞, a_n). Numerics (exact rational overlaps, 50 digits,
exact-E0 basis): μ_min drops from 0.73 (A=0.6) to ~1e−14 (A=3) while the "mass" M_A = −K(0) + 2Σ_{n≤e^A} a_n grows; dropping any single
prime n ≤ 13 at A=3 creates a negative direction (certificate). **Fig. 1.** These positive minima are Galerkin upper bounds, not proofs.

**F2 — Tate's boundary data are exactly compatible with Fourier and scaling, and carry an indefinite form. [EXACT]** (compat1907)
b(f) = (f(0), ∫f dx). Fourier: b(Ff) = σ b(f) (swap). Unitary scaling U_a = |a|^{−1/2} R_a: b(U_a f) = diag(|a|^{−1/2}, |a|^{1/2}) b(f); F U_a = U_{a⁻¹} F.
Smearing Θ_F = ∫F(t) U_{e^t} dt: b(Θ_F f) = diag(ev₀F, ev₁F) b(f), so Θ_F maps S(A) into S(A)₀ ⇔ F ∈ E0 (cf. Connes 1999 §III eqs (6),(10),(11)).
Orientation: F Θ_F F⁻¹ = Θ_{F(−·)} (linear); Θ_F* = Θ_{F^♯} (antilinear). **Lemma:** the only Hermitian forms on C² invariant under all D_a
and σ are z·[[0,1],[1,0]], z ∈ R — signature (1,1). Hence the boundary cannot supply positivity. Topology: S₀ and E0 are algebraically
codimension 2 but **dense in L²** (explicit shrinking-bump + broad-bump construction, error ≤ |c₀|δ^{1/2}‖η‖ + |c₁′|R^{−1/2}‖κ‖); on a fixed
window the two functionals are bounded, so the window kernel is closed of codimension 2. The "projection removing the poles" is the moment
map b (or a window-dependent projection), not a global orthogonal projection. **Fig. 2.**

**F3 — Every positive-square mechanism examined needs an independent positive structure. [EXACT in each setting; ANALOGY as bridge]**
- *Robertson–Schrödinger:* w = V + (iħ/2)σ ≥ 0 for a positive state; reading W as a covariance needs a state φ built from primes/Γ with φ(Φ(F)*Φ(G)) = W(F,G). A commutative positive functional *can* be independent (Bochner–Schwartz: a positive tempered measure); non-commutativity is needed only for a nonzero commutator. W is unbounded, so the right object is a positive functional/weight on the test-function *-algebra, not a normalized state on bounded translations.
- *Heisenberg 1925 ground state:* the termination condition fixes a constant because amplitudes are norms (|a(n,n−1)|² = n + c ≥ 0) in a Hilbert space; the positivity source is the Hilbert norm, not the ladder.
- *Witten positive energy:* the spinor supplies the square ‖∇ψ‖²; the sign comes from the dominant energy condition (a bulk hypothesis) together with existence of the Witten spinor (elliptic theory) and asymptotics. The semilocal Sonin inequality is **one** candidate analogue of the energy condition (OPEN).
- *Bogomolny/instanton:* |F|² ∓ F∧F/vol = 2|F^∓|² ≥ 0 (checked). The charge k (orientation-signed) labels a sector; its Hessian is zero; the positivity is the kinetic term from the Hodge star of a metric. At a BPS point the Hessian of ‖M‖² + C_top is 2 dM*dM ≥ 0 because of the square; non-BPS saddles in the same sector can be unstable.
- *Hodge index as an instanton:* on a Kähler surface, primitive real (1,1) forms are anti-self-dual, so α∧α = −|α|² vol (checked) and D² = −‖α‖² for a primitive class with harmonic curvature α = iF/2π. Sign source: the polarization ω, not the Chern class. Integrality alone does not give ampleness (Bl_pt P², D = 2H + E: D² = 3, D·E = −1).
- *Virasoro / no-ghost / SUSY:* Virasoro unitarity is Gram-matrix positivity (level-2 Kac determinant 2h(16h² + 2(c−5)h + c) checked; the vector (L₋₂ + 3/2 L₋₁²)|h=−1⟩ is null exactly at c = 26 — algebra only, not a positivity proof). Goddard–Thorn transports positivity from a positive transverse space; SUSY gives ‖Qψ‖² + ‖Q†ψ‖² ⇒ H ≥ |Z|. Each needs its positive space.
- *Connes 1999 / CC21 (the arithmetic proofs that do exist):* Tr(S_Λ V(f∗f*)) = 2(f∗f*)(1) log′Λ is positive but divergent; Weil arises as the limit of the subtraction Δ_Λ = Tr((S_Λ − Q′_{Λ,0})V(f)), positive in characteristic p because of the projection order Q′_{Λ,0} ≤ S_Λ (Thm 5; the global number-field statement is equivalent to RH). CC21 Thm 1 proves W_∞(g∗g*) ≥ Tr(ϑ(g) S ϑ(g)*) at the archimedean place for small support and vanishing conditions. **Fig. 3.**
These are not the only possible sign sources ("only Hodge produces sign" is false); they are the ones checked.

**F4 — Finite-field control: the split is exact there. [EXACT, Test 1]** On E×E/F_q with b(D) = (D·v, D·h):
D² = 2 b₀ b₁ + D_⊥² exactly, the normalized Frobenius graphs q^{−n/2}Γ_{Fⁿ} have b = (q^{−n/2}, q^{n/2}) (the same diagonal law as U_a on
Tate's data — discrete samples, *not* the continuous moments), and the Gram on ⟨h,v⟩^⊥ is [[−2, −a], [−a, −2q]], negative semidefinite
⇔ a² ≤ 4q (151 trace values scanned). det = 4q − a² > 0 holds while the form is negative definite: determinants/discriminants detect
degeneracy, inertia decides sign.

## 3. The missing law (a target, not a discovery) [TARGET]
Find a Hilbert space H₊ that is positive for reasons independent of the zeros, and a map Φ: E0 ∩ C_c^∞(window) → H₊ such that
1. ‖Φg‖² = W(g ∗ g^♯) **exactly** (not up to an uncontrolled remainder), with the divergent counterterm handled as in Connes' cutoff;
2. Φ intertwines scaling and is consistent under window restriction;
3. Φ is built from Euler factors and Γ data only (not a sum of place-local squares, since each local term is indefinite);
4. the construction fails for Davenport–Heilbronn-type functions (functional equation without Euler product).
Equivalently (atlas v1.15 wording): a no-ghost theorem for the scaling reduction, with the pole pair as the indefinite part and H₊ as the
positive transverse factor. Existence of such Φ is equivalent to RH (GNS/Kolmogorov), so all content is in an independent **construction**.
Do not conflate: covariance (a state's two-point function), stiffness (a Hamiltonian's quadratic form), poles (the boundary pair b), and zeros (spectral data) play different roles.

## 4. Tests run tonight (limitations stated)
- **Test 1 (new cross-check, exact):** the finite-field split above. It *reproduces* the Hodge-index sign (Weil/Mattuck–Tate); it detects no sign for ζ.
- **Test 2 (dictionary, numerical):** in F_q, W_q := −D² + 2b₀b₁ = −D_⊥² ≥ 0 while W_q − (hyperbolic term) = −D² has exactly one negative direction.
  On ζ windows (free basis, K = 8, 50 digits): W − P has exactly one negative eigenvalue (A=1: −1.524; A=2: −3.280; explicit vectors = certificates; prior: atlas r329), and W itself has no negative Galerkin eigenvalue (min 1.4e−4, 4.4e−12: not certificates). On the negative vector the pole term (1.587; 3.311) barely exceeds |W − P|. The signature pattern matches the F_q dictionary; this uses W itself, so it is a consistency check, **not** an independent sign.
- **Reproduction:** spring Galerkin A=1, A=2 at K=8 re-run: 0.06734, 1.65e−8 — between the stored K=6 and K=10 values, decreasing with K, as upper bounds should.
- **Audit outcome:** no new independent-sign candidate survived audit tonight. The best next test (not launched) is the S = {∞, 2} leakage/projection-order test of §5.

## 5. Next test (proposed, not launched)
At S = {∞, 2}: with prolate approximants B_Λ and the semilocal map E_S, measure the trace-norm leakage of the projection order
‖(1 − S_Λ) E_S Q_{B_Λ}‖₁ against Λ and the sign of Δ_{Λ,S} on E0 windows of length ≤ log 4; control S = {∞} against CC21 Thm 1.
It differs from the naive semilocal-Sonin difference that already failed (atlas R26, λ_min = −log2/√2). Falsified if leakage stays O(1) with negative sign.

## Appendix A — "Common quadratic geometry" bridge (t1917) [ANALOGY with exact pieces]
- Clifford: c(v)c(w) + c(w)c(v) = 2g(v,w) exists for indefinite g (Cl(1,1) by real 2×2 matrices, checked) — so Clifford structure alone is not a positivity source. For Riemannian g, the Dirac square D² = ∇*∇ + R/4 (Lichnerowicz) and on forms (d + d†)² = Δ; positivity comes from the Riemannian metric.
- Hodge (primitive ⇒ ASD) and the spinorial square can live on one geometry (a Kähler surface), but a list of squares does not produce an arithmetic surface. A candidate surface would have to explain multiplication (convolution), cohomological grading, duality (Fourier/FE) and intersection — not just an abstract Hilbert space.
- Discriminants: det of a finite Gram detects degeneracy only; det > 0 is not positivity (det(−I₂) = det(I₂)); use inertia or all leading principal minors, and control infinitely many windows.
- A positive compatible complex structure J and spinor chirality are different structures and not interchangeable. Do not identify a quadric zero locus with the needed arithmetic surface. Hypothesis (OPEN): one quadratic geometry underlies the Hodge-index sign, the Dirac square and the no-ghost transverse norm; the independent construction for ζ is the gap. No universal discriminant is proved.

## Appendix B — background threads, briefly
- Anharmonic oscillator/interactions (t1890): an explicit functional Φ_N with Hess Φ_N(0) = W exactly (quartic spring potentials); Hess at F₀ ≠ 0 is ≥ W. A Hessian identity restates W; it does not sign it.
- Position–momentum/energy–time pairs (t1904): (Q₀ = LQL⁻¹, D) on (E0, G₀) is the Schrödinger representation relabelled; prime isometries S_p give number–phase pairs; Lefschetz sl₂ with Hodge–Riemann is the only sign-carrying pair among those checked.
- Quartet/Planck units (t1906): Planck relations ℓ_P/t_P = c etc. are definitions; doubling the canonical pair adds no positivity. The archimedean stiffness K equals the group delay of the local gamma-factor phase (prior: atlas archimedean_weyl_kernel); the full completed-ζ ratio on the line is ≡ 1 by the functional equation, so no delay-positivity inference is drawn from it.
- Torsion (t1908 context): skew-torsion Lichnerowicz terms enter with the wrong sign for positivity; no claim that any geometry forces torsion to vanish.
- Deninger's program (t1897): a positive Hodge ⋆ on leafwise cohomology commuting with the flow (up to the conformal factor) would force Re = ½; the existence of that ⋆ is the conjecture.

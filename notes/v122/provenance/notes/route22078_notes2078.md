# t2078 — Route 2 current test on X = P¹(C) × P¹(C)  (scratch; nothing pushed)

Scope: archimedean Green pairing of two continuous Möbius graphs Γ_u = {w = e^u z}. No primes, no zeros,
no trace formula used as input. Does not construct Φ, does not give a Hodge sign, does not touch RH.
Scripts: `pair2078.py` (exact sympy + numerical check, output `pair2078.json`),
`check2078_transport.py` (comoving-metric family, output `check2078_transport.json`).

## 0. Conventions
- d^c = (∂ − ∂̄)/(4πi), so dd^c = (i/2π)∂∂̄ and dd^c log|z|² = δ_0 (Gillet–Soulé). With the i/π convention every
  Green function below is halved; nothing structural changes.
- ω_FS = dd^c log(1+|z|²), mass 1. On C, in r = |z|², the FS measure is dr/(1+r)².
- ω = pr₁*ω_FS + pr₂*ω_FS = c₁(O(1,1), FS). ω² = 2 pr₁*ω_FS ∧ pr₂*ω_FS, ∫_X ω² = 2.

## 1. Q1 — the Green current (exact)
Section of O(1,1): s_u = w₁z₀ − e^u w₀z₁ (affine: w − e^u z). FS metric ‖s‖² = |s|²/((|z₀|²+|z₁|²)(|w₀|²+|w₁|²)).
  g_u = −log‖s_u‖²_FS
      = −log|w₁z₀ − e^u w₀z₁|² + log(|z₀|²+|z₁|²) + log(|w₀|²+|w₁|²)      (homogeneous)
      = −log|w − e^u z|² + log(1+|z|²) + log(1+|w|²)                        (affine)
Poincaré–Lelong (exact): dd^c g_u + δ_{Γ_u} = ω_u, with ω_u = ω for every u (the FS class does not move).
g_u is a function (a (0,0)-current; "Green current of type (0,0) for a codim-1 cycle"), smooth off Γ_u, with
log singularity along Γ_u. Additive constant: rescaling s_u ↦ s_u/λ_u adds log|λ_u|². Natural choices:
raw (λ=1) and balanced s_u = e^{−u/2}w₁z₀ − e^{u/2}w₀z₁ (λ_u = e^{u/2}, adds +u).
Bidegree: Γ_u ∈ |O(1,1)|, smooth rational curve, Γ_u² = 2. For u ≠ v, Γ_u ∩ Γ_v = {(0,0),(∞,∞)}, both transversal,
Γ_u·Γ_v = 2.

## 2. Q2 — the pairing
On a complex surface g_u * g_v = g_u δ_{Γ_v} + ω_u g_v is a (1,1)-current; to get a number one pairs with a
third class. I used the polarization itself:
  T(u,v) := ∫_X (g_u * g_v) ∧ ω = ∫_{Γ_v} g_u ω + ∫_X g_v ω².
This is the archimedean part of the arithmetic triple product Γ̂_u·Γ̂_v·Ô(1,1)_FS, less the FS height of the
0-cycle (0,0)+(∞,∞), which is 0 on the standard model. (Γ_u is not defined over Z for generic u, so only the
archimedean piece is meaningful.)
Regularization: none needed. The collisions at (0,0),(∞,∞) give log|z|² singularities of g_u|_{Γ_v}, which are
integrable against the smooth form ω. The "exclude small FS balls" scheme has the same limit, because the
excised contribution is O(ε² log ε).

Key exact fact. On Γ_v (coordinate z, w = e^v z), s_u|_{Γ_v} = (e^v − e^u) z₀z₁. So
  g_u|_{Γ_v} = −log|e^u − e^v|² + G_v(z),   G_v(z) = −log|z|² + log(1+|z|²) + log(1+e^{2v}|z|²),
where G_v is the Green function of the fixed divisor 0+∞ on Γ_v and does not depend on u.
Radial integrals (exact, sympy): ∫₀^∞ log x dx/(1+x)² = 0; ∫ log(1+x) dx/(1+x)² = 1;
f(c) := ∫ log(1+cx) dx/(1+x)² = c log c/(c−1); ∫ log|w−α|² dμ_FS(w) = log(1+|α|²).
Hence ∫_{Γ_v} g_u ω = −2 log|e^u−e^v|² + 2 + 2v + 2v coth v and ∫_X g_v ω² = 4 − 2v(1+coth v). Total:

  **T(u,v) = 6 − 4 log|e^u − e^v|**   (exact, raw sections; numerical check to MC error ~1e-3 at 4 points)
  balanced sections: T' = T + 2u + 2v = **6 − 4 log(2 sinh(a/2))**,  a = |u−v|.

Split:
 (i) a-dependent interaction: −4 log(2 sinh(a/2)) = −2·Γ_u·Γ_v · log|2 sinh(a/2)|. The factor 2 is ∫_{Γ_v} ω = deg.
 (ii) u-only / v-only: −2(u+v) for raw sections, 0 for balanced. This is a pure section-normalization term.
     Constant 6: the FS self-energy of the configuration (2 from ∫_{Γ_v} G_v ω after the v-terms cancel, 4 from ∫ g_v ω²).
 (iii) algebraic part: Γ_u·Γ_v = 2 enters only as the coefficient of the log. Its finite part (the height of
     (0,0)+(∞,∞)) is 0.
Sign-twisted graph Γ_v^− = {w = −e^v z} (the sign character of R^×): T_− = 6 − 4 log(e^u + e^v), and the balanced
form is 6 − 4 log(2 cosh(a/2)) (exact; checked numerically).

Comparison to k_∞(a) = e^{−a/2}/(1−e^{−2a}) = (e^{−a/2}/2)(1/(1−e^{−a}) + 1/(1+e^{−a})) (the second identity is exact):
 - a→0: T' ~ −4 log a (log singularity), while k_∞ ~ 1/(2a) + 1/4 − a/48 (simple pole).
 - a→∞: T' ~ −2a (linear growth), while k_∞ ~ e^{−a/2} (decay).
 - There is no e^{−a/2} half-density factor and no 1/(1−e^{−2a}) denominator. The only a-function is log sinh(a/2)
   (and log cosh(a/2) for the twisted graph). **No match: FS gives a logarithmic height only.** Note that
   log cosh(a/2) is NOT the untwisted answer; it appears only for the sign-twisted pair.
 - I inserted no Haar factor du/(2|u|) and no half-density. Nothing in the Green pairing asks for one.

Rigidity (exact, any fixed metric). Let h be any continuous/smooth Hermitian metric on O(1,1) not depending on u,
with c₁ = ω_h. Then s_u|_{Γ_v} = (e^v−e^u)z₀z₁ gives ∫_{Γ_v} g_u ω_h = −2 log|e^u−e^v|² + β(v), and ∫ g_v ω_h² = γ(v).
Symmetry of the star product (mod im∂+im∂̄, paired with a closed form) forces β+γ to be constant. So
  T_h(u,v) = −4 log|e^u − e^v| + C_h   for EVERY fixed metric,
and section rescalings add only α(u)+α(v). The a-dependence −4 log|2 sinh(a/2)| is therefore universal: no choice
of a fixed metric (FS, toric/sup-norm, Poincaré-type with finite mass) can change it. This follows because
Γ_u ∩ Γ_v = 0+∞ is the same divisor on Γ_v for every u; the only thing that knows u is the leading coefficient
e^v − e^u.

## 3. Q3 — metric dependence vs blow-up
(a) Metric change. A fixed metric change adds only constants, by the rigidity result above. A u-dependent family
h_u = h e^{−φ_u}, g_u ↦ g_u + φ_u, adds (exact expansion)
   ∫φ_u ω² + ∫φ_v ω² + E(u,v),   E(u,v) = ∫_X φ_u dd^cφ_v ∧ ω = −∫ dφ_u ∧ d^cφ_v ∧ ω.
The only genuinely two-variable term is E, a negative-semidefinite Dirichlet-energy Gram kernel of the potentials.
 - The canonical C^×-adapted family is the comoving FS metric: transport the FS-metrized Γ̂_0 by σ_u(z,w) = (z, e^u w).
   Here φ_u = 2u + log((1+e^{−2u}|w|²)/(1+|w|²)), and the result (exact, checked numerically at 3 points) is
     T_tr = 3 − 4 log(2 sinh(a/2)) + a coth a + u coth u + v coth v.
   The denominator 1−e^{−2a} does appear naturally here, in a coth a = a(1+e^{−2a})/(1−e^{−2a}) = a + 2a Σ_{k≥1} e^{−2ka}.
   It comes from f(c) = c log c/(c−1) with c = e^{2a}, the FS energy between two rescaled FS metrics. It carries a
   factor a, though, has no pole at a=0 (a coth a = 1 + a²/3 + …), has no e^{−a/2}, and leaves non-invariant
   u coth u + v coth v terms. Still not k_∞.
 - Producing k_∞ exactly means choosing φ_u with Gram kernel E(u,v) = k_∞(u−v) (plus a compensating −log term).
   That is possible only by reverse-engineering: it is a Kolmogorov/Gram realization in which the kernel is
   chosen first. The sign of E is then fixed by construction, not derived. A strictly C^×-invariant metric
   (Haar d²z/|z|²) has infinite mass and is not a metric on O(1,1). Cutting it off at |log|z|| ≤ R makes the
   interaction coefficient grow like R, which only rescales the log.
(b) Blow-up of (0,0),(∞,∞). Γ̃_u = π*Γ_u − E₀ − E_∞, Γ̃_u·Γ̃_v = 2−1−1 = 0, disjoint. Γ̃_u meets E₀ ≅ P¹ (slope
m = w/z) at m = e^u, and E_∞ at slope e^{−u}. g̃_u = π*g_u − g_{E₀} − g_{E_∞}. On Γ̃_v the quotient section
equals (e^v−e^u)×(a nowhere-vanishing section), so ∫_{Γ̃_v} g̃_u ω̃ = −log|e^u−e^v|²·deg_{ω̃}Γ̃_v + (v-only).
This is again a pure log, now smooth because disjoint. The exceptional curves contribute the FS Green function on E₀
at the slopes: −log(|e^u−e^v|²/((1+e^{2u})(1+e^{2v}))) = −2 log|sinh(a/2)| + log cosh u + log cosh v (exact),
plus constants from E² = −1. No 1−e^{−2a}.
(c) Diagnosis. In this geometry k_∞ appears naturally at exactly one place, the local holomorphic Lefschetz
(Atiyah–Bott) index at the collision point. Near (0,0) the composite correspondence is z ↦ q z with q = e^{−a}.
On germs of half-forms K^{1/2} (monomials z^n dz^{1/2}) the local trace is Σ_{n≥0} q^{n+1/2} = e^{−a/2}/(1−e^{−a})
(Bose), and with the sign twist (−1)^n it is e^{−a/2}/(1+e^{−a}) (Fermi). Their even average is exactly k_∞.
That is an infinite tower (the whole Taylor tower of the local ring), i.e. a trace. The intersection multiplicity
at the same point is 1. Globally, the contributions at 0 and ∞ cancel: index of O(−1) = 0.
So **a single Green pairing of two compact graphs is the wrong shape of invariant**. It sees the collision only
through log of the leading coefficient, once, while k_∞ is a geometric series over the tower at the fixed point.
The holomorphic Atiyah–Bott version is the t2068 real Lefschetz index in holomorphic form. It is a trace, so it is
not an independent intersection-theoretic source.

Exact structural identity (analogy, not geometrization). For any fixed metric and raw sections, with u>v and a=u−v:
   k_∞(a) = −¼ e^{−a/2} · ½ Σ_{ε=±} ∂_u ⟨Γ̂_u, Γ̂_v^ε⟩_∞
(sympy residual 0). The Bose and Fermi factors are the u-derivatives of the Green interactions −4 log|e^u ∓ e^v|,
i.e. the derivative of a log height. This is the usual digamma = d log Γ relation. Three ingredients are added by
hand: the derivative (a variation/dipole current ∂_u g_u = 2Re(e^u z/(w−e^u z)), Cauchy-type, not a Green
current), the sign average, and the half-density e^{−a/2}. The identity also depends on the raw normalization:
balanced sections shift ∂_u T by +2. Recorded as analogy only.

Pointer, not verified here: the Arakelov mechanism that does produce tower/Lerch-type terms is equivariant
analytic torsion (Köhler–Roessler arithmetic Lefschetz). It needs isometric automorphisms (rotations), not the
non-isometric real scaling. It is spectral (the Laplacian on P¹), and it is a trace-type invariant.

## 4. What this says
- Route 2 as literally posed (Green current of Γ_u on P¹×P¹, pairing ⟨Γ̂_u, Γ̂_v⟩_∞) fails to produce k_∞. The answer
  is a logarithmic height −4 log(2 sinh(a/2)) + const, rigid under any fixed metric and unchanged by the blow-up.
- k_∞ is reachable only (1) by reverse-engineering a u-dependent metric family, or (2) as a local Atiyah–Bott
  trace, or (3) as the derivative of the Green interaction with half-density and sign average inserted. None of
  these is an independent, sign-controlled intersection.
- The surviving structural analogy is "k_∞ = half-density, even-averaged d/du of the archimedean Green
  interaction". It suggests that, if Route 2 is to continue, the object to pair is a first variation
  (tangent/dipole current of the family Γ_u) rather than the cycles themselves. That is a proposal, not a result.
- Open ~1.8 stays open. Φ is not constructed. No Hodge sign. Nothing here bears on RH.

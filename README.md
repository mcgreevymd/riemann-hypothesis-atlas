# The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity

**J. W. McGreevy; formalization by Grok Bot**

Version 1.8 · 30 Oct 2026

## Latest results (v1.8)

> The Riemann Hypothesis is not proved. Figures from the research notes folded into v1.8; labels and route scores (0.6·significance + 0.4·probability, 0–10) as in the entries.

<table>
<tr><td width="50%" valign="top"><a href="figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png"><img src="figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png" width="420" alt="Central-charge positivity is the Weil form"></a><br><sub>Central-charge positivity is the Weil form: from the prime side ζ stays ≥ 0 up to L = 8, while Davenport–Heilbronn turns negative near L = 4, with no zeros used. <b>[Restatement + Numerical · route score 4.7 (as a route to RH 2.8)]</b></sub></td><td width="50%" valign="top"><a href="figures/heat_flow_energy/zero_free_signed_energy_trace.png"><img src="figures/heat_flow_energy/zero_free_signed_energy_trace.png" width="420" alt="Zero-free signed energy of the heat-flowed Ξ"></a><br><sub>Zero-free signed energy of the heat-flowed Ξ: every ghost goes negative before it lands, ζ windows stay positive, and the Hermite form counts off-line pairs exactly. <b>[Theorem + Numerical · 4.4 (as a route to RH 3.3)]</b></sub></td></tr>
<tr><td width="50%" valign="top"><a href="figures/nc_torus_fv/gap_widths_and_nonnormal_residue.png"><img src="figures/nc_torus_fv/gap_widths_and_nonnormal_residue.png" width="420" alt="Hofstadter gap widths are log-linear in |n| and close like (distance to the wall)^½ on the lobe side"></a><br><sub>Hofstadter gap widths are log-linear in |n| and close like (distance to the wall)^½ on the lobe side; ‖P − P&#42;‖ is a gauge quantity that spikes at every collision, not a ghost test. <b>[Numerical + Theorem · 3.6 / 3.4 / 4.4 (as a ghost detector 1.6)]</b></sub></td><td width="50%" valign="top"><a href="figures/nc_torus_fv/nc_torus_gap_labels_ghost_blind.png"><img src="figures/nc_torus_fv/nc_torus_gap_labels_ghost_blind.png" width="420" alt="F/V on the noncommutative torus"></a><br><sub>F/V on the noncommutative torus: Manin’s lobe / wall / wedge, and gap labels that hold for every zero set, so the K-theory order is ghost-blind. <b>[Theorem + Numerical · 4.7 (as a route to ζ positivity 2.8)]</b></sub></td></tr>
<tr><td width="50%" valign="top"><a href="figures/heat_flow_energy/rodgers_tao_sundman_clock.png"><img src="figures/heat_flow_energy/rodgers_tao_sundman_clock.png" width="420" alt="The Rodgers–Tao energy is an exact Sundman clock with speed limit 4, but monotone for every real configuration"></a><br><sub>The Rodgers–Tao energy is an exact Sundman clock with speed limit 4, but monotone for every real configuration; the near-collision law separates Davenport–Heilbronn from ζ. <b>[Theorem + Numerical · 4.4]</b></sub></td><td width="50%" valign="top"><a href="figures/hardy_constant/hardy_constant_primes.png"><img src="figures/hardy_constant/hardy_constant_primes.png" width="420" alt="A Hardy constant for the primes is window positivity restated"></a><br><sub>A Hardy constant for the primes is window positivity restated: ζ’s margin closes (critical), Davenport–Heilbronn crosses 1 near ℓ = 4–5, and local constants do not glue. <b>[Theorem + Numerical · 3.9]</b></sub></td></tr>
<tr><td width="50%" valign="top"><a href="figures/sundman_clock/sundman_levi_civita_clock.png"><img src="figures/sundman_clock/sundman_levi_civita_clock.png" width="420" alt="Sundman/Levi-Civita clock"></a><br><sub>Sundman/Levi-Civita clock: the F/V collision becomes a turning point and real τ bounces; positivity is the clock staying real, i.e. RH restated. <b>[Theorem · 4.7 (circular as a proof route, Restatement 4.4)]</b></sub></td><td width="50%" valign="top"><a href="figures/sundman_clock/two_kepler_degenerations.png"><img src="figures/sundman_clock/two_kepler_degenerations.png" width="420" alt="Two Kepler degenerations"></a><br><sub>Two Kepler degenerations: F = V is the circular orbit (e = 0), not the Levi-Civita centre collision (e = 1); both share the square-root map. <b>[Theorem · 4.4]</b></sub></td></tr>
</table>

> **New in v1.8** (see [CHANGELOG.md](CHANGELOG.md)): five sets of research notes are folded in (a Hardy-inequality reading of the window Weil form; the Rodgers–Tao log-gas energy in a Sundman clock; the F/V family on the noncommutative-torus side; a zero-free signed-energy trace of the heat-flowed Ξ; a Polishchuk–Schwarz central charge on the F/V family, with central-charge positivity tested on ζ and Davenport–Heilbronn): 472 concepts and 1177 typed relations. Several of the constructions were suggested in external review; each is recorded only at the label its test supports. **Every new positivity reformulation is Weil positivity again [Restatement]:** a Hardy/KLMN constant for the primes, the linear K-theory order on exponential-type tests (Akhiezer), and central-charge positivity with a Rosati partner. Their value is computational: from the prime side alone ζ stays ≥ 0 up to support L = 8, while Davenport–Heilbronn turns negative near L = 4, with no zeros used [Numerical]. **Zero-free ghost detection [Theorem + Numerical]:** the signed energy Σ(z_j − z_k)⁻² of the heat-flowed zeros can be computed from contour integrals alone; every ghost drives it negative before it lands, but its sign at a single time is not a reality test. The Hermite form built from the same contour moments counts off-line pairs exactly and caught every Davenport–Heilbronn and planted ghost tested. For ζ, positivity at every small t > 0 is Λ ≤ 0, i.e. RH restated; the non-circular use is as a barrier certificate for upper bounds on Λ [Open]. **Ghost-blind [Theorem]:** the monotone Rodgers–Tao energy (monotone for every real configuration), the K-theory gap labels, and the non-normality ‖P − P*‖ of spectral projections (a gauge quantity that diverges at every collision). **Noncommutative torus [Theorem]:** in Manin’s dictionary the Hasse lobe is a CM elliptic curve and the wedge a noncommutative torus with real multiplication; the Sundman gap² clock is hyperbolic arc length; Z_F(r, d) = −d + F·r is a Bridgeland central charge whose Rosati partner is complex conjugation on the lobe and Galois conjugation on the wedge, and the Polishchuk–Schwarz tilt is at slope −1/θ. Hofstadter gap widths decay exponentially in the label |n|, and on the lobe side they close like the square root of the distance to the wall [Numerical]. **Rank 1 is a manual pin:** the narrowed missing piece is listed first by the author’s choice, not by its score (Heuristic priority 0.380, unchanged); every other entry follows the scored order. **The Riemann Hypothesis is not proved.**

<p align="center"><img src="figures/animation_labelled/fv_sweep.gif" alt="F and V as the roots of x² − a·x + q while the trace a sweeps: ellipse, double line, hyperbolic window" width="820"></p>

*Animated: Frobenius F (●) and Verschiebung V (■) as the roots of x² − a·x + q (q = 5) and the norm conic deg(m − nF) = m² − a·mn + q·n² as the trace a sweeps. After J. W. McGreevy's animation “Flat Potential Oscillations” (Aug 2025, [x.com/McGreevyMD/status/1951474097990279331](https://x.com/McGreevyMD/status/1951474097990279331)); re-rendered by Grok Bot from the analysed geometry, not from the original code.*

[![Overview: the original frames, the five stages, the F ↔ V sweep and the legend](figures/animation_labelled/overview.png)](figures/animation_labelled/overview.png)

## Two equivalent figure sets

The repository carries two sets of labelled figures. **They are equivalent:** the same five stages of the same animation, drawn from the same geometry, with the same mathematics and the same status tags. They differ only in emphasis. Each set is meant to illuminate or highlight specific aspects:

- **Concept-colour set** (`figures/animation_labelled/`). One colour per concept, the same in every frame, the overview and the GIF. Each frame has at most two callouts, plus small insets (the roots F and V, the LC energy curve, the resonance line shapes). The background is muted. This set brings out **which concept sits where**, and how the same concept comes back from stage to stage.
- **Detailed-annotation set** (`figures/animation_detailed/`). The norm conic is drawn as a full-strength colour map of deg. In the hyperbolic window it is a sign map: orange where deg > 0, purple where deg < 0. Every element has a full-text callout giving its formula, its numbers and its TAA lemma reference. The legend explains the status tags. This set brings out **the values and the sign of the form**, the closed lobe against the hyperbolic window, and the exact statement behind each label.

| Concept-colour set (`figures/animation_labelled/`) | Detailed-annotation set (`figures/animation_detailed/`) |
|---|---|
| <a href="figures/animation_labelled/overview.png"><img src="figures/animation_labelled/overview.png" alt="Overview: original frames, five stages, sweep, legend" width="420"></a><br>**Overview: original frames, five stages, sweep, legend** | <a href="figures/animation_detailed/overview.png"><img src="figures/animation_detailed/overview.png" alt="Overview: original frames, five stages, sweep, legend" width="420"></a><br>**Overview: original frames, five stages, sweep, legend** |
| <a href="figures/animation_labelled/stage1_closed_lobes.png"><img src="figures/animation_labelled/stage1_closed_lobes.png" alt="1 · Closed lobe: definite form, Hasse" width="420"></a><br>**1 · Closed lobe: definite form, Hasse** | <a href="figures/animation_detailed/stage1_closed_lobes.png"><img src="figures/animation_detailed/stage1_closed_lobes.png" alt="1 · Closed lobe: definite form, Hasse" width="420"></a><br>**1 · Closed lobe: definite form, Hasse** |
| <a href="figures/animation_labelled/stage2_approach.png"><img src="figures/animation_labelled/stage2_approach.png" alt="2 · Approach: the lobe stretches" width="420"></a><br>**2 · Approach: the lobe stretches** | <a href="figures/animation_detailed/stage2_approach.png"><img src="figures/animation_detailed/stage2_approach.png" alt="2 · Approach: the lobe stretches" width="420"></a><br>**2 · Approach: the lobe stretches** |
| <a href="figures/animation_labelled/stage3_pure_wedge.png"><img src="figures/animation_labelled/stage3_pure_wedge.png" alt="3 · Pure wedge: a² = 4q, doubled line" width="420"></a><br>**3 · Pure wedge: a² = 4q, doubled line** | <a href="figures/animation_detailed/stage3_pure_wedge.png"><img src="figures/animation_detailed/stage3_pure_wedge.png" alt="3 · Pure wedge: a² = 4q, doubled line" width="420"></a><br>**3 · Pure wedge: a² = 4q, doubled line** |
| <a href="figures/animation_labelled/stage4_hyperbolic_window.png"><img src="figures/animation_labelled/stage4_hyperbolic_window.png" alt="4 · Hyperbolic window: a ghost" width="420"></a><br>**4 · Hyperbolic window: a ghost** | <a href="figures/animation_detailed/stage4_hyperbolic_window.png"><img src="figures/animation_detailed/stage4_hyperbolic_window.png" alt="4 · Hyperbolic window: a ghost" width="420"></a><br>**4 · Hyperbolic window: a ghost** |
| <a href="figures/animation_labelled/stage5_half_turn.png"><img src="figures/animation_labelled/stage5_half_turn.png" alt="5 · Half turn: S² = −I, F ↔ V" width="420"></a><br>**5 · Half turn: S² = −I, F ↔ V** | <a href="figures/animation_detailed/stage5_half_turn.png"><img src="figures/animation_detailed/stage5_half_turn.png" alt="5 · Half turn: S² = −I, F ↔ V" width="420"></a><br>**5 · Half turn: S² = −I, F ↔ V** |
| <a href="figures/animation_labelled/fv_sweep.png"><img src="figures/animation_labelled/fv_sweep.png" alt="F ↔ V sweep (static)" width="420"></a><br>**F ↔ V sweep (static)** | <a href="figures/animation_detailed/fv_sweep.png"><img src="figures/animation_detailed/fv_sweep.png" alt="F ↔ V sweep (static)" width="420"></a><br>**F ↔ V sweep (static)** |
| <a href="figures/animation_labelled/legend.png"><img src="figures/animation_labelled/legend.png" alt="Legend" width="420"></a><br>**Legend** | <a href="figures/animation_detailed/legend.png"><img src="figures/animation_detailed/legend.png" alt="Legend" width="420"></a><br>**Legend** |
| <a href="figures/animation_labelled/fv_sweep.gif"><img src="figures/animation_labelled/fv_sweep.gif" alt="F ↔ V sweep, animated" width="420"></a><br>**F ↔ V sweep, animated** | <a href="figures/animation_detailed/fv_sweep.gif"><img src="figures/animation_detailed/fv_sweep.gif" alt="F ↔ V sweep, animated" width="420"></a><br>**F ↔ V sweep, animated** |

**How to read the figures.** In the concept-colour set, each colour is one concept: the drawn element and the box that names it share that colour, and the grey badge is the status. In the detailed set, the status tag closes each callout. In both sets, matching a picture element to a piece of mathematics is an Analogy; the mathematics on each label carries its own tag.

### Absorption vs gain: the Kramers–Kronig pair of a zero

[![Kramers–Kronig pair of a zero: absorption line vs gain line, and Γ as the full width at half maximum](figures/kk/kk_absorption_vs_gain.png)](figures/kk/kk_absorption_vs_gain.png)

- **[Theorem]** (Hadamard; TAA Lemma 154) On Re s = σ, each zero ρ = β + iγ contributes a Lorentzian line to Re ξ′/ξ. The line has area +π when σ > β (absorption) and −π when σ < β (gain). The dispersive partner is Im F = −sgn(σ−β)·H[Re F].
- **[Theorem given certificates]** (TAA Lemmas 154, 156) The width Γ = 2|β − ½| is the limit of the full width at half maximum as σ → ½, approached from below for a ghost. For the first Davenport–Heilbronn ghost, the certified value is Γ₁ = 0.617034364913274771106 ± 9·10⁻²².
- **[Numerical]** The bottom panels evaluate ζ and Davenport–Heilbronn directly at σ = 0.55. The ζ panel shows absorption lines only. The Davenport–Heilbronn panel shows a gain line at its first ghost.

## Figures

[![Eigenvalue plane vs the upper half-plane](figures/fixed_point/eigenvalue_plane_vs_upper_half_plane.gif)](figures/fixed_point/eigenvalue_plane_vs_upper_half_plane.gif)

Eigenvalue plane vs the upper half-plane. Left: Frobenius F and Verschiebung V as roots of x² − a·x + q (q = 5), normalized by √q. Right: the fixed point τ of g_t = [[t, −1], [1, 0]] (t = a/√q) in the Poincaré disk, which equals F/√q and is the complex structure J the element preserves. Invariant circles (elliptic, harmonic oscillator) become horocycles at the F/V meeting point (parabolic, free particle) and an axis with hypercycles past it (hyperbolic, inverted oscillator); at trace √p + 1/√p the translation length is log p. Theorem-level geometry; archimedean and ghost-blind on its own. RH is not proved.

[![Smoothness through the meeting point](figures/fixed_point/smoothness_through_the_meeting_point.png)](figures/fixed_point/smoothness_through_the_meeting_point.png)

Smoothness through the meeting point: F’s speed |dF/da| blows up like |a − 2√q|^(−½), while the generator X and the trace as a function of θ² are real-analytic straight through it.

[![The 45° flip of the F/V ring](figures/flip45/flip45.gif)](figures/flip45/flip45.png)

The 45° flip of the F/V ring (q = 5): the reflection R(z) = i·z̄ across y = x sends the collision √q to i√q and the real split axis to the imaginary axis, where the F ↔ V swap is the Fricke involution τ ↦ −q/τ, fixed at i√q (Theorem; static version: [flip45.png](figures/flip45/flip45.png)).

### New in v1.8

[![Central-charge positivity for ζ and Davenport–Heilbronn](figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png)](figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png)

**Central-charge positivity is the Weil form, and it separates ζ from Davenport–Heilbronn without zeros** (`figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png`, research notes). On the F/V family, Z_F(r, d) = −d + F·r is a Bridgeland central charge; at the wall every line-bundle phase collapses to 0 or 1, the Polishchuk–Schwarz tilt [Theorem]. Summed over zeros with the Rosati partner 1 − ρ̄, central-charge positivity is exactly Weil’s quadratic form [Restatement]. Computed from the prime side, ζ stays ≥ 0 up to support L = 8; computed from its Dirichlet coefficients, Davenport–Heilbronn turns negative near L = 4, from its off-line quadruple at height 85.70, and its negative index is 2 [Numerical].

| File | Caption | Label |
|---|---|---|
| `figures/nc_torus_fv/central_charge_positivity_zeta_vs_dh.png` | Bridgeland phases of line bundles on the F/V family and their collapse at the wall; support constant and Hecke minimal mass; minimum eigenvalue of the Weil (central-charge) form against support L for ζ, Davenport–Heilbronn and planted ghosts; negative index | Theorem + Numerical |
| `figures/nc_torus_fv/gap_widths_and_nonnormal_residue.png` | Hofstadter gap widths against the label &#124;n&#124; (log-linear) and toward the wall (exponent ½ on the lobe side); ‖P − P*‖ of Riesz projections for ζ, Davenport–Heilbronn and planted ghosts in companion, balanced and normal models; its divergence at every collision, including ζ’s backward collision | Numerical + Theorem |
| `figures/nc_torus_fv/nc_torus_gap_labels_ghost_blind.png` | Hofstadter butterfly with the F/V fluxes; gap labelling checked on zero-built operators; lobe, wall and wedge as CM point, boundary point and closed geodesic; the K-theory labels are ghost-blind | Theorem + Numerical |
| `figures/heat_flow_energy/zero_free_signed_energy_trace.png` | Signed energy of the heat-flowed Ξ from contour integrals (no zeros located): Davenport–Heilbronn ghosts under the true heat flow, planted ghosts, ζ windows positive and decreasing, contour against direct sums, early-warning fraction against ghost height | Theorem + Numerical |
| `figures/heat_flow_energy/rodgers_tao_sundman_clock.png` | Rodgers–Tao energy as a Sundman clock (speed limit 4); backward collision times for ζ, Davenport–Heilbronn and controls; Lehmer pairs against the pair law; ghost local energy; root-free companion trace; near-collision law at t → 0 | Theorem + Numerical |
| `figures/hardy_constant/hardy_constant_primes.png` | Hardy/KLMN constant of the window Weil form for ζ, Davenport–Heilbronn, a ghost and controls; S-lemma constant for the indefinite cushion; jump-form levels below the mass; the p = 2 Vladimirov symbol and its α-derivative (the prime term); products of local constants diverge | Theorem + Numerical |
| `figures/sundman_clock/sundman_levi_civita_clock.png` | Sundman/Levi-Civita regularization (v1.7 research notes): F, V against a and in Sundman time (a turning point); the square-root factorization of the discriminant; a heat-flow ghost pair and the Calogero pair in Sundman time; iterated Turán rungs are ghost-blind | Theorem + Numerical |
| `figures/sundman_clock/two_kepler_degenerations.png` | Two Kepler degenerations on the F/V gap axis (circular orbit e = 0 is F = V; centre collision e = 1 is different) and the shared square-root map | Theorem |

### New in v1.7

[![Prime-by-prime build of the window Weil form](figures/narrowed_missing_piece/prime_by_prime_build.png)](figures/narrowed_missing_piece/prime_by_prime_build.png)

**Positivity appears only when every lag is present** (`figures/narrowed_missing_piece/prime_by_prime_build.png`, research notes). Adding primes in increasing order, the partial window forms stay indefinite; the negative count peaks near log P ≈ ℓ/2, where ζ is more indefinite than sign-flipped controls, and the form enters the positive cone only for the last primes (log p ≈ ℓ) [Numerical]. Sharing the positive cushion among primes needs hundreds of times the cushion that exists [Numerical], and the sign of each prime step follows the sign of the gap excess g_p − log p, which changes infinitely often [Theorem]. The missing piece is a reason for this global cancellation [Open].

| File | Caption | Label |
|---|---|---|
| `figures/narrowed_missing_piece/prime_by_prime_build.png` | Prime-by-prime build: inertia and margin of partial sums, per-prime margin steps, onset of partial sums, per-prime allocation lower bound, step sign against the prime-gap excess | Numerical + Theorem |
| `figures/narrowed_missing_piece/levinson_light_cone.png` | Verblunsky coefficients &#124;k(ℓ)&#124; (&#124;k&#124; = 1 is the light cone) for genuine ζ, L(Δ), 11a1, sign flips and Davenport–Heilbronn; the innovation margin E/r₀ = Π(1 − k²) | Theorem + Numerical |
| `figures/narrowed_missing_piece/levinson_update_not_contracting.png` | The Levinson update is expanding for ζ, not contracting; loss of contraction warns no earlier than &#124;k&#124;; onset is non-perturbative (flat until about 2% from the critical ghost size); controls coincide with ζ until log p of the first flipped prime | Numerical |
| `figures/narrowed_missing_piece/gaussian_smoothing_ghost_blind.png` | Exact window positivity against the Gaussian (imaginary-shift, Husimi) filtered form: the filter stays positive for all ghosts and Davenport–Heilbronn; detection returns only when the hard window edge cuts the Gaussian | Numerical |
| `figures/lemma185/l185r3_stability.png` | Window thermodynamics (TAA Lemma 185 rev. 3): isotherms and mechanical instability; onsets in δ; the earlier height-79.34 warning re-examined on a longer window (an artefact) | Numerical |
| `figures/lemma185/l185r3_baro.png` | Barotropy test: the baroclinic measure for genuine ζ and a near-wall ghost; genuine ζ is baroclinic, close to an ideal gas | Numerical |
| `figures/lemma185/l185r2_dose.png` | Gluing curvature under a ghost (TAA Lemma 185 rev. 2): it responds only once positivity is lost, and the most negative K then equals λ_min(W); the Fisher curvature operator is ghost-blind except at the crossing | Numerical |

### New in v1.6.1

[![Flat gluing connections, curvature in the metric](figures/lemma184/l184r2_flat_gluing.png)](figures/lemma184/l184r2_flat_gluing.png)

**Where curvature can live** (`figures/lemma184/l184r2_flat_gluing.png`, TAA Lemma 184 rev. 2). Each Euler factor is a unitary local frame [Theorem]; the connections that glue the primes, a Galois representation (Frobenius as holonomy) and ω = W⁻¹dW for the window family, are flat [Theorem]; so curvature with a sign has to come from the metric they preserve (Petersson, Weil). The window form is positive only after all primes are glued [Numerical]. That metric over Spec ℤ is the missing piece [Open].

| File | Caption | Label |
|---|---|---|
| `figures/lemma184/l184r2_flat_gluing.png` | Flat gluing connections; curvature with a sign must live in the metric | Theorem + Numerical + Open |
| `figures/lemma184/l184r2_gluing_curvature.png` | Gluing curvature K_g(p,q) on 105 prime pairs (window ℓ = 5, p ≤ 47): genuine ζ, L(Δ), 11a1 nonnegative on 91–100% of pairs, sign-flipped and permuted variants about half negative; the log-det Hessian curvature is negative for every positive-definite form (control); the symmetric/antisymmetric split of the connection moves alike under sign flips (null) | Numerical |
| `figures/lemma184/l184_quaternionic_star.png` | Same formula Cκ, opposite squares: the 45° flip is a real structure (square +1), Deninger’s ⋆ on H¹ is quaternionic (square −1); a compatible quaternionic ⋆ on a finite form is a parity condition | Theorem + Numerical |

### New in v1.6

[![Brainstorm map: the new idea, the missing piece and what surrounds them](figures/new_idea_map/brainstorm_map.png)](figures/new_idea_map/brainstorm_map_hires.png)

**The shape of the new idea and the missing piece** (`figures/new_idea_map/brainstorm_map.png`; 300 dpi: [brainstorm_map_hires.png](figures/new_idea_map/brainstorm_map_hires.png)). The proved surround, the no-go boundary and recurring concepts around the new idea (positive space) and the missing piece (negative space), joined by density × density on the diagonal and its log n translates. Line style is the label: solid Theorem, dashed Restatement, dotted Analogy, red ✗ no-go. A map, not a proof [labels as marked; centre Open].

[![What abuts the new idea and the missing piece, in seven beats](figures/new_idea_map/abut.gif)](figures/new_idea_map/abut.mp4)

**What abuts the missing piece, in seven beats** (`abut.gif`; H.264: [abut.mp4](figures/new_idea_map/abut.mp4)). λ₂ along the window for ζ, Davenport–Heilbronn, ζ with one prime dropped and ½L(χ)L(χ̄) [Numerical]; the pole light cone and its boost [Theorem]; the 45° F/V axis swap [Restatement]; the deficit cone under the flow [Theorem]; buoyancy [Theorem locally, Analogy globally]; density × density [Restatement + Numerical]; the shape of the missing piece [Open].

[![Allowed locally, aligned globally: Δ and 11a1 under genuine, shuffled, Sato–Tate and adversarial angles](figures/allowed_vs_aligned/fig3_allowed_vs_aligned.png)](figures/allowed_vs_aligned/fig3_allowed_vs_aligned.png)

**Allowed locally ≠ aligned globally** (`figures/allowed_vs_aligned/fig3_allowed_vs_aligned.png`). Unstable-mode counts of the window form for Δ (left) and 11a1 (right): only the genuine Frobenius angles keep n₋ = 0; permuted, i.i.d. Sato–Tate and adversarial-but-allowed angles fail [Numerical; consistent with GRH, not evidence for it].

[![The angles arrive prime by prime; positivity pins each one](figures/allowed_vs_aligned/theta.gif)](figures/allowed_vs_aligned/theta.mp4)

**θ_p at an allowed angle, in seven beats** (`theta.gif`; H.264: [theta.mp4](figures/allowed_vs_aligned/theta.mp4)). Angles arrive prime by prime (Deligne, Sato–Tate) [Theorem]; same angles, different assignment; phases add up coherently or drift [Numerical]; positivity pins each angle [Numerical]; no tachyon for Δ [Numerical]; η²⁴ and the 1/24 [Theorem identities; Numerical no-go]; the missing piece is the alignment [Open].

| File | Caption | Label |
|---|---|---|
| `figures/allowed_vs_aligned/fig1_newton_angles.png` | 11a1 at p = 2, 3, 5, 7, 19: Newton polygon of 1 − a_pX + pX² (ordinary vs supersingular) and α/√p on the unit circle; the polygon fixes \|α\| = √p, not θ_p | Theorem + Numerical |
| `figures/allowed_vs_aligned/fig2_sato_tate.png` | The marginal is satisfied: 11a1 angles for p ≤ 3000 against the Sato–Tate density (KS distance 0.024) | Cited + Numerical |
| `figures/allowed_vs_aligned/fig3_allowed_vs_aligned.png` | Genuine vs permuted / Sato–Tate / adversarial angles for Δ and 11a1: only the genuine set keeps W ⪰ 0 | Numerical |
| `figures/allowed_vs_aligned/fig3b_pinning.png` | The pinning: the admissible width of one angle (others genuine) shrinks from 180° to about 0.03° by ℓ = 6; widths are model-dependent | Numerical |
| `figures/allowed_vs_aligned/fig4_slot_in.png` | The slot-in shape: allowed marginals plus an unknown joint law; candidates scored 0.6·sig + 0.4·prob | Open + Heuristic scores |
| `figures/allowed_vs_aligned/fig5_eta24.png` | η²⁴ = Δ and the 1/24; the one-sided weight edge is generic (11a1 has it too), not a fingerprint of 1/24 | Theorem (identities) + Numerical (no-go) |
| `figures/new_idea_map/brainstorm_map.png`, `brainstorm_map_hires.png` | Brainstorm map of the new idea and the missing piece | labels as marked |
| `figures/new_idea_map/abut.gif`, `abut.mp4` | Seven captioned beats abutting the missing piece | labels per beat |
| `figures/allowed_vs_aligned/theta.gif`, `theta.mp4` | Seven captioned beats on θ_p at an allowed angle | labels per beat |
| `figures/lemma181/l181_Q.png` | The ℚ side: a ghost drives the primitive margin negative while the pole channels stay put; E×E primitive minimum; genus by resolution; (d) a two-class diagnostic that uses the zeros | Numerical |
| `figures/lemma181/l181_genus2.png` | Genus 2 over F_q: genuine defect Grams are PSD, fakes have one negative eigenvalue; which channel fails as graphs are added | Theorem + Numerical |
| `figures/lemma181/l181_ghostQ.png` | Over ℚ, planted off-line quartets on finite sections (box, sine, bump, Legendre bases): which channel goes negative first | Numerical (diagnostic) |
| `figures/lemma182/l182_ghostcount.png` | The ghost count: lowest eigenvalues of Z_ℓ with and without a synthetic off-line pair; the Perron mode stays the pole, ghost modes oscillate at the ghost frequency | Numerical |
| `figures/lemma182/l182_poleplane.png` | The pole plane: P = 2K₊K₋ hyperbolic, null lines forced by dilation; the coupling to the primitive part stays O(1), only its ratio decays | Theorem + Numerical |
| `figures/lemma182/l182_crossings.png` | Synthetic-ghost crossing windows against log(t/2π)(0.85 + 0.14/β); Davenport–Heilbronn gains unstable modes in pairs | Numerical |
| `figures/lemma182/l182_691.png` | Irregular primes leave no signature in the ℚ window form; τ(n) ≡ σ₁₁(n) mod 691 for n ≤ 1000 | Numerical |

(J. W. McGreevy; formalization by Grok Bot.)

## Where RH is likely to live

> **⚠ RH is not proved.** The pictures locate the question; they do not answer it.

- **[Heuristic]** The pictures carry two kinds of layer: ones a hypothetical off-line zero (a “ghost”) cannot see, and ones it changes.
- **[Theorem]** Ghost-blind: the symmetry and the phase (the functional equation, the critical line, |φ| = 1 at the cusp, the circle and the π in zero counts, F and V as a dual pair with FV = q) hold just as well for the Davenport–Heilbronn function, which has off-line zeros.
- **[Theorem]** Ghost-sensitive: positivity (the closed lobe of a definite form, unequal resonance widths, gain lines, the hyperbolic window) changes sign when a ghost is present; Davenport–Heilbronn shows it numerically **[Numerical]**.
- **[Numerical, rigorous]** The ghost-sensitive layer can be seen from the prime side. Davenport–Heilbronn's ghosts are detected from its coefficients, Γ-factor and functional equation, with no zero list (TAA Lemma 155). Its zero list for 2 < t < 135 is certified complete: 79 zeros, 75 on the line plus 4 off it (TAA Lemma 156).
- **[Restatement]** “V = F† for a positive form” is the RH-type statement for curves (Hasse); for ζ it is a restatement, not a proof.
- **[Theorem]** For ζ, RH is equivalent to Weil positivity (Weil's criterion).
- **[Open]** The one positivity input with no known construction for ζ is the arithmetic Hodge-index / Rosati sign, labelled MP4 in TAA Lemma 151.
- **[Heuristic]** So RH is likely to live in the ghost-sensitive layer: in supplying that positivity, not in more symmetry or phase.

| File (in both figure folders) | Stage |
|---|---|
| `overview.png` | Original frames (credited), the five stages, the F ↔ V sweep and the legend |
| `stage1_closed_lobes.png` | Closed lobe: definite form, a² < 4q, V = F̄, Hasse; Legendre tangents; LC ellipse; equal resonance widths |
| `stage2_approach.png` | Approach to degeneracy |
| `stage3_pure_wedge.png` | Pure wedge: double line a² = 4q (at atan(1/√5) ≈ 24°, not 45°) |
| `stage4_hyperbolic_window.png` | Hyperbolic window: an indefinite block (a ghost); Davenport–Heilbronn; split resonance widths; LC hyperbola |
| `stage5_half_turn.png` | The 180° half turn: S² = −I, Hardy Z sign flip, F ↔ V swap |
| `fv_sweep.png`, `fv_sweep.gif` | F and V on the circle of radius √q as the trace a sweeps |
| `legend.png` | Concept-colour set: one row per concept (colour, line style, meaning, math, status, references). Detailed set: the status tags and how to read them |

Most PNGs have a PDF twin. The detailed overview is PNG only. The Kramers–Kronig figure is in `figures/kk/`. All figures are ordinary files in the repository (no Git LFS).

> ## ⚠ The Riemann Hypothesis is NOT proved here.
> This repository is a map, not a proof. It classifies known theorems, criteria, analogies and open problems by how they bear on RH, and it states precisely which pieces are still missing.

## What this is

The RH Atlas is a structured catalogue of 472 concepts from number theory, algebraic geometry, spectral theory and physics that have been proposed as routes to, restatements of, or analogies for the Riemann Hypothesis. There are 1177 typed relations between them (same mechanism as, special case of, analogue of, implies, equivalent to RH, corrects, lives in, fails for). It grew out of the research programme *Thermodynamics of Arithmetic Action* (TAA). References of the form “TAA Lemma N” point to that lemma series; The published volumes listed below collect the earlier lemmas; later lemmas (beyond Lemma 118) are not yet published.

Every entry says in plain words what the concept is, gives its precise core statement, carries a label for how well established it is, and records corrections and cautions where a tempting claim turns out to be false.

## The organizing split

Most beautiful structure around ζ turns out not to decide RH. The atlas sorts structures by one question: **would this still hold if ζ had a zero off the critical line?**

- **Phase / unitarity is ghost-blind.** Functional equations, unit-modulus scattering phases |φ| = 1, cocycles, Hecke operators and cusp-form positivity hold just as well for functions that *do* have zeros off the line, such as the Davenport–Heilbronn function. A “ghost” here means a hypothetical off-line zero, which shows up as a negative-norm direction of the Weil form.
- **The sign of a spectral weight is ghost-sensitive.** Whether a certain quadratic form is positive (the Weil form, the Rosati form, Re ξ′/ξ to the right of the line) does change when an off-line zero is present. For ζ, that sign *is* RH.

So the useful question about any idea is whether it touches the sign, or only the phase.

## How entries are ordered

Every list in the atlas runs in **descending priority**, with `#rank · priority` shown in each header. Priority comes from a scoring layer that is labelled **Heuristic**: the scores are judgment calls, shown component by component so you can disagree with any of them. For each concept:

- **Gap significance:** how closely it bears on one of the ten missing pieces (1.0 if it *is* one, then 0.8, 0.5, 0.2 by distance in the relation graph). The nearest gap is named.
- **Sensitivity:** does it hold for ζ (is it necessary for, or implied by, RH)?
- **Specificity:** does it *fail* for the fakes (the Davenport–Heilbronn function and ghost-zero models)? Ghost-blind structure scores near 0.
- **Tractability:** the chance that working on it gives provable progress.
- **Evidence:** the weight of its label (shown, not in the composite).

  **priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability**

A concept ranks high only if it is both true for ζ and false for the fakes. The full rules and tie-breaks are in [scores.md](scores.md).

**One manual exception.** Rank 1 is a pin, not a score: the missing piece [Open], narrowed in v1.7 to a structural reason for the global cancellation in the prime-to-sequence map (a per-prime ferromagnetic sign is refuted in the tested families), is listed first by an editorial decision of the author, kept since v1.5. Its own Heuristic priority is 0.380. Every other entry sits where the priority puts it.

## Label legend

| Label | Meaning |
|---|---|
| Theorem | Proved (in the literature or in a TAA lemma). |
| Restatement | Equivalent to RH or to a known result; a reformulation, not progress. |
| Analogy | A structural parallel, not a mathematical identity. |
| Conjecture | Believed but unproved. |
| Open | An unsolved problem or a missing object. |
| Numerical | Computed evidence (some computer-certified), not a proof. |
| Heuristic | A plausible reading or judgment call. |
| Cited | Taken from the literature. Citations marked “to verify” have not yet been checked against the source. |

## Top 15 concepts by rank

| # | priority | concept | label | quadrant |
|---|---|---|---|---|
| 1 | 0.380 | [Narrowed missing piece (Open): a structural reason for the global cancellation in the prime-to-sequence map (the explicit formula’s balance); a per-prime ferromagnetic sign is refuted in the tested families](ATLAS.md#ferromagnetic-phi-missing-piece) | Open | RH-sharp |
| 2 | 0.720 | [Weil positivity criterion](ATLAS.md#weil-positivity) | Cited | RH-sharp |
| 3 | 0.720 | [Davenport–Heilbronn function](ATLAS.md#davenport-heilbronn) | Theorem | RH-sharp |
| 4 | 0.720 | [ψ(x) − x (explicit formula, deviation from the pole)](ATLAS.md#psi-minus-x) | Cited | RH-sharp |
| 5 | 0.720 | [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](ATLAS.md#two-verschiebungs-dual-vs-adjoint) | Theorem | RH-sharp |
| 6 | 0.720 | [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](ATLAS.md#frobenius-graph-lattice) | Theorem | RH-sharp |
| 7 | 0.720 | [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](ATLAS.md#kahler-triple-polarization) | Theorem | RH-sharp |
| 8 | 0.720 | [Lagarias/Hinkkanen criterion](ATLAS.md#lagarias) | Cited | RH-sharp |
| 9 | 0.720 | [Connes trace formula](ATLAS.md#connes-trace) | Cited | RH-sharp |
| 10 | 0.720 | [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](ATLAS.md#kahler-identities-foliated) | Theorem | RH-sharp |
| 11 | 0.720 | [Primitive part V₀ = U^⊥](ATLAS.md#primitive-part) | Theorem | RH-sharp |
| 12 | 0.720 | [Definite cup square / Krein one-liner](ATLAS.md#definite-cup-square) | Theorem | RH-sharp |
| 13 | 0.700 | [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](ATLAS.md#mp-flow-h1) | Open | RH-sharp |
| 14 | 0.700 | [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a &#124;·&#124;²)](ATLAS.md#mp-castelnuovo) | Open | RH-sharp |
| 15 | 0.700 | [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](ATLAS.md#mp-h1-square) | Open | RH-sharp |

Ties at the same priority are broken by gap significance, then by number of relations (counted in this public edition), then alphabetically by id.

## The ten missing pieces

These are the objects that would have to exist for a positivity proof of RH along the lines of the function-field case (all labelled Open):

1. arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)
2. surface + ample class + Riemann–Roch for Spec ℤ (D8)
3. flow-relative H¹ for Spec ℤ
4. quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square
5. an inequality consequence of automorphy (SC-E / HS-1)
6. a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)
7. H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)
8. a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ
9. passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)
10. RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)

Each is stated precisely in [ATLAS.md](ATLAS.md#missing-pieces), with what is proved around it and the tests (against the Davenport–Heilbronn function and ghost models) it must pass.

## Published volumes (Thermodynamics of Arithmetic Action)

- Arithmetic Unitarity I (v2): https://ai.vixra.org/abs/2610.0045
- Arithmetic Unitarity IVa: https://ai.vixra.org/abs/2610.0056
- Arithmetic Unitarity IVb: https://ai.vixra.org/abs/2610.0055
- Arithmetic Unitarity V: https://ai.vixra.org/abs/2610.0059

## Lemmas

- [Lemma 159: The arithmetic equation of state](lemmas/lemma159_arithmetic_equation_of_state.pdf) (J. W. McGreevy; formalization by Grok Bot). RH is not proved.

## How to cite

J. W. McGreevy, *The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity*, version 1.8 (30 Oct 2026), https://github.com/mcgreevymd/riemann-hypothesis-atlas

## Files

| File | What it is |
|---|---|
| `README.md` | This overview. |
| `ATLAS.md` | The full atlas in readable form: missing pieces, diagnostic quadrants, every concept by primary axis (all in priority order), and an index by rank. |
| `atlas.json` | The machine-readable atlas (source of truth for this repository). |
| `scores.md` | The scoring method behind the ordering. |
| `CHANGELOG.md` | Version history. |
| `build_public_md.py` | Regenerates `ATLAS.md` from `atlas.json`: `python3 build_public_md.py`. |
| `figures/` | `animation_labelled/` (concept-colour set), `animation_detailed/` (detailed-annotation set), `kk/` (Kramers–Kronig figure), `fixed_point/` (eigenvalue plane vs upper half-plane), `flip45/` (the 45° flip), `new_idea_map/` (brainstorm map and the abut animation), `allowed_vs_aligned/` (Frobenius-angle figures and the θ animation), `lemma181/`, `lemma182/`, `lemma184/`, `lemma185/` (figures from TAA Lemmas 181, 182, 184 and 185), `narrowed_missing_piece/` (research-note figures for the v1.7 narrowing), `heat_flow_energy/`, `nc_torus_fv/`, `hardy_constant/` and `sundman_clock/` (research-note figures for v1.8, shown in the “Latest results (v1.8)” gallery at the top). |
| `LICENSE` | Creative Commons Attribution 4.0 International (CC BY 4.0), full legal text. |
| `q.py` | Command-line query tool: `python3 q.py rosati`, `python3 q.py --axis ghost-blind`, `python3 q.py --list`, `python3 q.py --quadrant RH-sharp`, `python3 q.py --missing`. Python 3, standard library only. |

## License

© 2026 J. W. McGreevy. Formalization by Grok Bot.

The RH Atlas (text, data and figures) is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see [LICENSE](LICENSE). You may share and adapt it for any purpose if you give appropriate credit, link to the license, and indicate if changes were made. Suggested credit: “J. W. McGreevy, The RH Atlas, v1.8, CC BY 4.0”.

# The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity

**J. W. McGreevy; formalization by Grok Bot**

Version 1.6.1 · 29 Oct 2026

> **New in v1.6.1** (see [CHANGELOG.md](CHANGELOG.md)): corrections from an external review, a literature review (1976–2026), TAA Lemma 183 and TAA Lemma 184 (rev. 1 and rev. 2) are folded in: 388 concepts and 1040 typed relations. **Correction, the two circles [Theorem]:** v1.6 said no map between Li’s circle and the Lee–Yang circle is known. In Li’s variable z = 1 − 1/s, ξ becomes a series F(z) with F(1/z) = F(z), positive coefficients and a₁/a₀ = λ₁, the shape of a Lee–Yang partition function; RH is then the Lee–Yang property of F [Restatement]. **Nonnegative couplings plus a pole are not enough [Numerical]:** with random signs in place of χ₄, ζ·L(χ₄) keeps nonnegative coefficients and its pole but fails the window test in 20 of 20 cases. **Davenport–Heilbronn, corrected:** a functional equation alone is not sufficient [Theorem], but the Euler product is not necessary either: Weng zeta functions satisfy RH without one [Theorem, Cited]. A ladder exponent of −0.19 is withdrawn as noise. **Lemma 184 [Theorem + Numerical]:** a quaternionic ⋆ on a finite form is a parity condition; the 45° flip is a real structure (square +1), not a rotation; the gluing connections (Galois representations, ω = W⁻¹dW) are flat, so curvature with a sign has to live in the metric; a gluing curvature on prime pairs is nonnegative on 91–100% of pairs for ζ, L(Δ) and 11a1 and about half negative for shuffled forms, a tendency, not a law; a torsion/contorsion split is a null result. **Rank 1 is a manual pin:** the ferromagnetic missing piece is listed first by the author’s choice, not by its score (Heuristic priority 0.200); every other entry follows the scored order. **The Riemann Hypothesis is not proved.**

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

The RH Atlas is a structured catalogue of 388 concepts from number theory, algebraic geometry, spectral theory and physics that have been proposed as routes to, restatements of, or analogies for the Riemann Hypothesis. There are 1040 typed relations between them (same mechanism as, special case of, analogue of, implies, equivalent to RH, corrects, lives in, fails for). It grew out of the research programme *Thermodynamics of Arithmetic Action* (TAA). References of the form “TAA Lemma N” point to that lemma series; The published volumes listed below collect the earlier lemmas; later lemmas (beyond Lemma 118) are not yet published.

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

**One manual exception.** Rank 1 is a pin, not a score: the refined missing piece (a ferromagnetic coupling of the primes that produces Φ) [Open] is listed first by an editorial decision of the author, kept since v1.5. Its own Heuristic priority is 0.200. Every other entry sits where the priority puts it.

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
| 1 | 0.200 | [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](ATLAS.md#ferromagnetic-phi-missing-piece) | Open | RH-sharp |
| 2 | 0.720 | [Davenport–Heilbronn function](ATLAS.md#davenport-heilbronn) | Theorem | RH-sharp |
| 3 | 0.720 | [Weil positivity criterion](ATLAS.md#weil-positivity) | Cited | RH-sharp |
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

J. W. McGreevy, *The RH Atlas: A Systematic Accounting of the Structures in Mathematics and Physics That Touch the Riemann Hypothesis, Classified by Positivity, Sign and Unitarity*, version 1.6.1 (29 Oct 2026), https://github.com/mcgreevymd/riemann-hypothesis-atlas

## Files

| File | What it is |
|---|---|
| `README.md` | This overview. |
| `ATLAS.md` | The full atlas in readable form: missing pieces, diagnostic quadrants, every concept by primary axis (all in priority order), and an index by rank. |
| `atlas.json` | The machine-readable atlas (source of truth for this repository). |
| `scores.md` | The scoring method behind the ordering. |
| `CHANGELOG.md` | Version history. |
| `build_public_md.py` | Regenerates `ATLAS.md` from `atlas.json`: `python3 build_public_md.py`. |
| `figures/` | `animation_labelled/` (concept-colour set), `animation_detailed/` (detailed-annotation set), `kk/` (Kramers–Kronig figure), `fixed_point/` (eigenvalue plane vs upper half-plane), `flip45/` (the 45° flip), `new_idea_map/` (brainstorm map and the abut animation), `allowed_vs_aligned/` (Frobenius-angle figures and the θ animation), `lemma181/`, `lemma182/`, `lemma184/` (figures from TAA Lemmas 181, 182 and 184). |
| `LICENSE` | Creative Commons Attribution 4.0 International (CC BY 4.0), full legal text. |
| `q.py` | Command-line query tool: `python3 q.py rosati`, `python3 q.py --axis ghost-blind`, `python3 q.py --list`, `python3 q.py --quadrant RH-sharp`, `python3 q.py --missing`. Python 3, standard library only. |

## License

© 2026 J. W. McGreevy. Formalization by Grok Bot.

The RH Atlas (text, data and figures) is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see [LICENSE](LICENSE). You may share and adapt it for any purpose if you give appropriate credit, link to the license, and indicate if changes were made. Suggested credit: “J. W. McGreevy, The RH Atlas, v1.6.1, CC BY 4.0”.

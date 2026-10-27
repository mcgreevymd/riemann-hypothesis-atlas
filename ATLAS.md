# The RH Atlas — full public edition

Version 1.0 · 26 Oct 2026 · J. W. McGreevy; formalization by Grok Bot

> **The Riemann Hypothesis is NOT proved here.** This atlas is a classification of known structures, criteria and open problems, not a proof.

131 concepts · 279 typed relations · 10 missing pieces. Generated from `atlas.json` by `build_public_md.py`.

**Order.** Every section lists its entries in descending priority. Headers read `#rank · priority · name`. Priority comes from the Heuristic scoring layer described in [scores.md](scores.md): priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability. The scores are judgment calls, shown component by component so any reader can disagree with them.

**Organizing split.** Phase/unitarity structure (functional equations, |φ| = 1, cocycles, Hecke operators, cusp positivity) is *ghost-blind*: it holds equally for functions with zeros off the critical line, such as the Davenport–Heilbronn function. The *sign* of a spectral weight is *ghost-sensitive*, and for ζ that sign is RH.

**Labels.** Theorem · Restatement (equivalent to RH or to a known result) · Analogy · Conjecture · Open · Numerical · Heuristic · Cited (taken from the literature). References of the form “TAA Lemma N” point to the lemma series of the Thermodynamics of Arithmetic Action programme (see README.md for the published volumes). Citations marked “to verify” have not yet been checked against the source.

## Contents

- [Missing pieces](#missing-pieces)
- [Diagnostic quadrants](#diagnostic-quadrants)
- [Concepts by primary axis](#concepts-by-primary-axis)
  - [sign/positivity (Ax2)](#axis-sign-positivity-ax2) (23)
  - [no-go / refuted](#axis-no-go-refuted) (4)
  - [reference/pole/cusp](#axis-reference-pole-cusp) (18)
  - [physics analogue](#axis-physics-analogue) (16)
  - [Spec ℤ gap](#axis-spec-gap) (21)
  - [phase/unitarity (Ax3)](#axis-phase-unitarity-ax3) (17)
  - [ghost-sensitive](#axis-ghost-sensitive) (6)
  - [geometry over F_q](#axis-geometry-over-f-q) (8)
  - [numerics/certificate](#axis-numerics-certificate) (5)
  - [structure/frame (Ax1)](#axis-structure-frame-ax1) (1)
  - [open target](#axis-open-target) (1)
  - [ghost-blind](#axis-ghost-blind) (1)
- [Index by rank](#index-by-rank)

## Missing pieces

These are the objects that, as far as this atlas can tell, would have to exist for a positivity proof of RH along the lines of the function-field case. Each is labelled Open. Listed in priority order.

### #6 · 0.700 · Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²) <a id="mp-castelnuovo"></a>

**Label:** Open · **id:** `mp_castelnuovo` · **quadrant:** RH-sharp

*In plain words:* A space with an infinite H¹, a positive involution † and a flow u_t with u_t u_t† = eᵗ, on which the explicit-formula (Weil) distribution becomes a squared norm, with that positivity proved without using the zeros.

**Core.** Arithmetic Castelnuovo object = (C1) infinite H¹, (C2) positive involution, (C3) u_t u_t† = eᵗ, (C4) positivity proved without zeros (TAA Lemma 136); equivalently a positive involution plus a Frobenius-type flow with positivity proved without zeros (TAA Lemma 136 synthesis). Hilbert–Pólya form: a positive V ≅ H¹ (TAA Lemma 115); “all that is missing is an appropriate inner product” (Lax–Phillips, TAA Lemma 105/TAA Lemma 141).

**What is proved around it.** Over F_q: Ax2 ∧ Ax3 ⇔ |α| = √q (TAA Lemma 137, theorem). Over ℚ: isometry of the flow is unconditional (TAA Lemma 1); the Čech 2-class supplies C2–C3 structure but not the sign (TAA Lemma 138); Ax2 alone holds for fakes, Ax3 alone is tautological (TAA Lemma 137).

**Tests it must pass.** Must separate ghosts: Ax2 and Ax3 jointly, never one alone (TAA Lemma 137). Must not define the inner product by Weil’s form (circular, TAA Lemma 138 R2; TAA Lemma 106).

**Also known as:** C1–C4; positive involution; Hilbert–Pólya object

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2), open target

**TAA lemmas:** 105, 106, 115, 136, 137, 138

**Scores (Heuristic):** gap significance 1.0 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object)
- same mechanism as → [Hilbert–Pólya](#hilbert-polya)
- special case of → [Ax1–Ax3 axioms (Yoneda specification)](#ax123) — Ax2 + Ax3 jointly

**Relations (incoming):** [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (special case of)

### #7 · 0.700 · Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8) <a id="mp-d8"></a>

**Label:** Open · **id:** `mp_d8` · **quadrant:** RH-sharp

*In plain words:* The top substantive direction: a surface S over Spec ℤ with an ample class and a Riemann–Roch whose χ(nD) is quadratic, so that Hodge index follows as it does for curves.

**Core.** D8: surface + ample + RR for Spec ℤ — find S with χ(nD) quadratic and a Hodge index; obstacle: the collapse ℤ ⊗ ℤ = ℤ; sign = Weil form (TAA Lemma 140, TAA Lemma 141). Acceptance test (TAA Lemma 141): reconstruct the relative space and its form from independent constraints — (a) the hyperbolic plane U = ⟨𝟙, 𝕃⟩, (b) the scaling flow acting on it as diag(1, eᵗ), (c) ampleness at ∞, (d) RR/GRR with quadratic growth — then prove negativity on U^⊥. Any proof that uses the zeros, or defines the form by its negativity, fails.

**What is proved around it.** Over F_q: surface + ample + RR ⇒ Hodge index (Segre 1937, Grothendieck 1958) (TAA Lemma 140). Spec ℤ ×_ℤ Spec ℤ = Spec ℤ (TAA Lemma 65). Arithmetic surfaces (curve × Spec O_K) satisfy V1–V3, but the relative part is Néron–Tate, not ζ (TAA Lemma 145).

**Tests it must pass.** Must pass the tautology test (no zeros, no definition by negativity, TAA Lemma 141) and the must-fail-for-DH test (TAA Lemma 147).

**Also known as:** D8; arithmetic surface with Hodge index

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 65, 140, 141, 145, 147

**Scores (Heuristic):** gap significance 1.0 (nearest gap: surface + ample class + Riemann–Roch for Spec ℤ (D8)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.4 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)
- same mechanism as → [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr)
- special case of → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo)

**Relations (incoming):** [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as)

### #8 · 0.700 · Missing: flow-relative H¹ for Spec ℤ <a id="mp-flow-h1"></a>

**Label:** Open · **id:** `mp_flow_h1` · **quadrant:** RH-sharp

*In plain words:* For ℚ both cohomologies we can compute vanish (étale H¹ = 0, Arakelov Pic⁰ = a point), yet ψ(x) − x ≠ 0. The zeros need a cohomology relative to the scaling flow.

**Core.** TAA Lemma 141 H¹ table: Spec ℤ has étale H¹ = 0, Arakelov Pic⁰ = point (r = 0, h = 1), relative count ψ(x) − x = −Σ_ρ x^ρ/ρ + …, infinitely many zeros, flow H¹ = Deninger H¹_flow (Open). “For ℚ both H¹’s that we can compute vanish, yet ψ − x ≠ 0, so the zeros need a cohomology relative to the flow” (TAA Lemma 141, restatement).

**Formula.** N_n − (1 + qⁿ) = −Tr(Fⁿ | H¹) ↔ ψ(x) − x = −Σ_ρ x^ρ/ρ + …

**What is proved around it.** π₁ét(Spec ℤ) = 1 ⇒ H¹ét = 0 (TAA Lemma 140); curve row: N_n − (qⁿ + 1) = −Tr(Fⁿ | H¹) with relative Gram NSD (TAA Lemma 141 §1); Tr ↔ −(ψ − x) up to the s = 0 term and ARCH (TAA Lemma 142 corrections).

**Tests it must pass.** Must carry a positive structure (Ax2), not only the trace formula: the explicit formula alone is ghost-blind in data (TAA Lemma 143: ghost defect ≤ 1.9e−5, 0.08× noise).

**Also known as:** H¹_flow; Deninger H¹

**Axes:** missing piece, Spec ℤ gap, reference/pole/cusp

**TAA lemmas:** 140, 141, 142

**Scores (Heuristic):** gap significance 1.0 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [No étale H¹ for Spec ℤ](#no-etale-h1)
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)
- same mechanism as → [Deninger’s foliated program](#deninger)

**Relations (incoming):** [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as)

### #9 · 0.700 · Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square <a id="mp-quadratic-rr"></a>

**Label:** Open · **id:** `mp_quadratic_rr` · **quadrant:** RH-sharp

*In plain words:* A Riemann–Roch on Spec ℤ × Spec ℤ whose Euler characteristic is quadratic in D, together with the step “ample ⇒ has sections ⇒ effective”. This is exactly the part of the curve proof that Spec ℤ lacks.

**Core.** Classical chain: S1 quadratic RR, S2 Serre duality, S3 h¹ ≥ 0 / Minkowski, S4 sections ⇒ effective, S5 ample·effective > 0. Missing Spec ℤ step = quadratic S1 + S4 (“ampleness ⇒ effectivity” via a 2-dim h⁰) (TAA Lemma 145 V3, verdict VF-E). Parity: quadratic χ is even in D, linear χ odd ⇒ fixed rank proves only degree c(D) = 0, never sees D².

**Formula.** χ(D) = ½D·(D − K) + χ(𝒪) (needed shape)

**What is proved around it.** Every proved Connes–Consani RR is 1-dimensional, χ = deg + const (TAA Lemma 147); fixed-rank products are linear, h⁰/n = 2.000 at n = 400 (TAA Lemma 145 Thm linear); on ℙ¹_ℤ χ̂ is quadratic and realizes the U-form (TAA Lemma 145). Hodge index also needs S2, S3, S5 (TAA Lemma 145 corrections).

**Tests it must pass.** Must fail for Davenport–Heilbronn, hence must use the Euler product (TAA Lemma 147, necessary condition). Must see D², i.e. be quadratic. V3 on the square ⇔ Weil ⇔ RH, so it must be proved, not assumed (TAA Lemma 145).

**Also known as:** S1q + S4; quadratic RR; VF-E

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 145, 147

**Scores (Heuristic):** gap significance 1.0 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.4 → priority 0.700

> ❓ **Not verified / open.** The displayed “needed shape” is the classical surface RR, quoted as the target form.

**Relations (outgoing):**

- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)
- fails for → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) — linear χ
- same mechanism as → [Parity argument: linear χ cannot see D²](#parity-linear-chi)

**Relations (incoming):** [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (same mechanism as)

### #10 · 0.700 · Missing: an inequality consequence of automorphy (SC-E / HS-1) <a id="mp-automorphy-ineq"></a>

**Label:** Open · **id:** `mp_automorphy_ineq` · **quadrant:** RH-sharp

*In plain words:* Automorphy (invariance under the full modular group) decides where the zeros are but does not derive it; what is missing is an inequality that automorphy forces on δ_ρ.

**Core.** SC-E (structural P: Hecke/Euler product) = Selberg-class RH, the open non-circular version of trapped-set rigidity (TAA Lemma 143); sharpened to “an inequality consequence of automorphy” (→ Weil positivity, TAA Lemma 142) (TAA Lemma 144). HS-1: an automorphy-defect functional 𝒟(Λ_X) ≥ 0 with 𝒟 = 0 ⇔ Λ_X = ξ; it needs an inequality that the defect forces on δ_ρ, which we do not have (TAA Lemma 144).

**Formula.** 𝒟(Λ_X) ≥ 0, 𝒟(Λ_X) = 0 ⇔ Λ_X = ξ

**What is proved around it.** Thm 3.3 (TAA Lemma 144): automorphy picks a = 1/ξ(2s), c = φ uniquely, exact defect formula; Hecke alone puts no constraint on φ (Prop 3.2). SC-A ⇔ RH (restatement); SC-B false (DH); SC-C false (all cofinite Γ); HS-B (Hecke + unitarity ⇒ δ = 0) false (fakes).

**Tests it must pass.** Fakes pass Hecke/FE/Δ/unitarity to 1e−25 but fail S-invariance: DH by 1.4–3.2%, the degree-0 ghost by 4.5e−6–1.6e−4 (TAA Lemma 144). The inequality must be violated by both.

**Also known as:** SC-E; HS-1; automorphy-defect functional

**Axes:** missing piece, Spec ℤ gap, ghost-sensitive, phase/unitarity (Ax3)

**TAA lemmas:** 142, 143, 144

**Scores (Heuristic):** gap significance 1.0 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Automorphy defect (TAA Lemma 144)](#automorphy-defect)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH breaks automorphy
- implies → [Weil positivity criterion](#weil-positivity) — target

### #11 · 0.700 · Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3) <a id="mp-brst"></a>

**Label:** Open · **id:** `mp_brst` · **quadrant:** RH-sharp

*In plain words:* A nilpotent operator on the test functions whose cohomology is exactly the relative space U^⊥, so that “remove the pole plane, then the rest is positive” becomes a cohomology statement, as in Gupta–Bleuler/BRST.

**Core.** PM-3: Gupta–Bleuler/BRST complex Q on TAA Lemma 142’s test functions with H(Q) = U^⊥ (TAA Lemma 146). Thm gb (linear algebra, proved): for V = U ⊕ U^⊥, U = ⟨F₁, F₂⟩, F_i² = 0, F₁F₂ = 1, the quotient F₁^⊥/⟨F₁⟩ is isometric to U^⊥; a nilpotent Q with cohomology U^⊥ would package it as a flow-relative cohomology (Open).

**Formula.** F₁^⊥/⟨F₁⟩ ≅ U^⊥ (isometric)

**What is proved around it.** TAA Lemma 115: BRST structure exact over F_q and ℚ; “no ghosts” ⇔ RH (restatement); missing positive V ≅ H¹ (Hilbert–Pólya). TAA Lemma 146: the BRST quartet decouples, but a ghost quartet survives.

**Tests it must pass.** A ghost quartet is exactly a quartet that fails to decouple (TAA Lemma 146); the complex must not decouple it. Positivity of the quotient is an input in QED and is RH for ζ.

**Also known as:** PM-3; flow-relative cohomology (BRST)

**Axes:** missing piece, physics analogue, structure/frame (Ax1)

**TAA lemmas:** 115, 146

**Scores (Heuristic):** gap significance 1.0 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst)
- same mechanism as → [Primitive part V₀ = U^⊥](#primitive-part) — H(Q) = U^⊥
- same mechanism as → [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1)

### #12 · 0.700 · Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0) <a id="mp-h1-square"></a>

**Label:** Open · **id:** `mp_h1_square` · **quadrant:** RH-sharp

*In plain words:* A first cohomology on the square of Connes–Consani’s scaling site; with it, an RR theorem would give D(f)•D(f) ≤ 0, which is RH.

**Core.** CC18: RH ⇔ s(f,f) ≤ 0, s(f,f) = D•D with D = ∫fΨ_λ; five steps, only step 1 (complex lift) built; H¹ on the square of the scaling site, and hence RR there, is open (TAA Lemma 147, correction 2). ½D(f)•D(f) = ½s(f,f) is the Weil form (TAA Lemma 142).

**Formula.** RH ⇔ s(f,f) = D(f)•D(f) ≤ 0

**What is proved around it.** No RR for C_ℚ × C_ℚ exists (TAA Lemma 147, correction 2). The square exists as a site with Ψ_λ (TAA Lemma 30) but carries no H¹, RR or Hodge index (TAA Lemma 65).

**Tests it must pass.** All H⁰-side objects built from ℤ ⊂ 𝔸_ℚ are ghost-blind; the topological side s(f,f) is ghost-sensitive (DH-location ghost positive from L* = 3.45, actual DH from 4.70) (TAA Lemma 142, TAA Lemma 147).

**Also known as:** H¹ on C_ℚ × C_ℚ; CC18 key step

**Axes:** missing piece, Spec ℤ gap

**TAA lemmas:** 30, 65, 142, 145, 147

**Scores (Heuristic):** gap significance 1.0 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — s(f,f) ≤ 0
- same mechanism as → [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff)

### #13 · 0.700 · Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ <a id="mp-ns-psi"></a>

**Label:** Open · **id:** `mp_ns_psi` · **quadrant:** RH-sharp

*In plain words:* An intersection theory on the square in which the Connes–Consani correspondences Ψ_λ are genuine classes outside the pole plane U, with enough sections that their growth sees s(f,f).

**Core.** Need NS ⊋ U with Ψ_λ, and #H⁰(±nD(f)) ≥ 2^{n² s(f,f)/2} (TAA Lemma 147). Decisive missing objects: H¹ on the square, an intersection theory putting Ψ_λ into an NS larger than U, and quadratic RR (TAA Lemma 147 (iv)).

**Formula.** #H⁰(±nD(f)) ≥ 2^{n² s(f,f)/2}

**What is proved around it.** Laurent piece of HZ ∧_𝕊 HZ: box count 2n² + 4n exact, but the quadratic coefficient 2αβ is the U-form ⇒ vacuous on degree-0 D(f) (TAA Lemma 147 Thm vac).

**Tests it must pass.** Quadratic growth must come from V₀ = U^⊥, not from U (Thm vac). Ghost-sensitive side is s(f,f), which must be negative for ζ and fail for DH (TAA Lemma 142, TAA Lemma 147).

**Also known as:** NS ⊋ U; Ψ_λ classes

**Axes:** missing piece, Spec ℤ gap, structure/frame (Ax1)

**TAA lemmas:** 147, 142

**Scores (Heuristic):** gap significance 1.0 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square)
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — must leave U
- same mechanism as → [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff)

### #14 · 0.700 · Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin) <a id="mp-passivity-margin"></a>

**Label:** Open · **id:** `mp_passivity_margin` · **quadrant:** RH-sharp

*In plain words:* RH is equivalent to ξ′/ξ being a passive (positive-real) response to the right of the line. What is missing is a proof of a passivity margin that uses only primes, the pole and the archimedean place.

**Core.** Lagarias (1.5), attributed to Hinkkanen: RH ⇔ Re ξ′/ξ(s) > 0 on Re s > ½ (TAA Lemma 146, opened). PM-1: a Lagarias margin h(σ) for ξ vs DH/ghost — a provable, ghost-sensitive passivity margin? (TAA Lemma 146).

**Formula.** RH ⇔ Re ξ′/ξ(s) > 0 for Re s > ½

**What is proved around it.** Re ξ′/ξ = Σ(σ−β)/((σ−β)² + (t−γ)²): each zero an absorption line, an off-line zero a gain line (TAA Lemma 146). Passivity ⇒ causality, not conversely (TAA Lemma 146 corrections). Free positivity (Λ(n) ≥ 0, KMS, Bagchi recurrence) is ghost-blind (TAA Lemma 136, TAA Lemma 118).

**Tests it must pass.** Grid σ ∈ [.505, 1.1], t ∈ [80, 92]: ξ min +0.00467; DH −66.84 at (0.794, 85.70), 1.89% negative; ghost −66.97, 1.94% (TAA Lemma 146). The margin must stay positive for ξ and go negative for both.

**Also known as:** PM-1; Lagarias margin

**Axes:** missing piece, sign/positivity (Ax2), ghost-sensitive, physics analogue

**TAA lemmas:** 17, 146

**Scores (Heuristic):** gap significance 1.0 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Passivity (positive real part)](#passivity)
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias)
- fails for → [Gain lines (active media)](#gain-line)

### #15 · 0.700 · Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”) <a id="mp-rg5"></a>

**Label:** Open · **id:** `mp_rg5` · **quadrant:** RH-sharp

*In plain words:* In the relative Gram dictionary every entry has an analogue except the one that proves the sign: a Riemann–Roch or Grothendieck–Riemann–Roch theorem on an arithmetic square.

**Core.** RG-5: RR/GRR on an arithmetic “Spec ℤ × Spec ℤ” producing the sign — the missing row of the TAA Lemma 142 dictionary (TAA Lemma 142). D9: arithmetic GRR test on the scaling-site square (TAA Lemma 140/TAA Lemma 141 candidate).

**Formula.** G_rel ≤ 0 on all spans ⇔ RH

**What is proved around it.** TAA Lemma 142 Thm 1.1: Weil Gram on translates is Toeplitz (flow), POLE = rank-2 signature (1,1) = the curve U-part exactly; every entry zero-free (flow, U/Tate poles, Γ_ℝ, Λ(n)); G_rel ≤ 0 on all spans ⇔ RH (Weil, restatement). Unconditional sign only on windows ≤ log 3 (TAA Lemma 10) and arch-only a* (TAA Lemma 127), both ghost-blind.

**Tests it must pass.** Ghost ⇒ n₊(G_rel) = 2 (TAA Lemma 142); DH-location ghost positive from L* = 3.45. The theorem must produce G_rel ≤ 0 for ζ on every span without using zeros.

**Also known as:** RG-5; D9; missing row

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2), restatement ⇔ RH

**TAA lemmas:** 10, 127, 140, 141, 142

**Scores (Heuristic):** gap significance 1.0 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Relative Gram matrix G_rel](#relative-gram)
- same mechanism as → [Tautology boundary (zero side vs prime side)](#tautology-boundary)
- same mechanism as → [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8)

## Diagnostic quadrants

Sensitivity asks whether a statement holds for ζ (is necessary for, or implied by, RH). Specificity asks whether it fails for the fakes (the Davenport–Heilbronn function and the ghost zero models). A concept can only detect RH if it scores high on both.

| | specificity ≥ 0.8 (fails for the fakes) | specificity < 0.8 (ghost-blind or untested) |
|---|---|---|
| **sensitivity ≥ 0.8** (true for ζ) | RH-sharp: 43 | true but ghost-blind/untested: 71 |
| **sensitivity < 0.8** (interpretive) | sharp but interpretive: 5 | background: 12 |

### RH-sharp: true for ζ and fails for the fakes (43)

- #1 · 0.720 · [Weil positivity criterion](#weil-positivity) [Cited]
- #2 · 0.720 · [Davenport–Heilbronn function](#davenport-heilbronn) [Theorem]
- #3 · 0.720 · [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) [Cited]
- #4 · 0.720 · [Primitive part V₀ = U^⊥](#primitive-part) [Theorem]
- #5 · 0.720 · [Lagarias/Hinkkanen criterion](#lagarias) [Cited]
- #6 · 0.700 · [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) [Open]
- #7 · 0.700 · [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) [Open]
- #8 · 0.700 · [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1) [Open]
- #9 · 0.700 · [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) [Open]
- #10 · 0.700 · [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) [Open]
- #11 · 0.700 · [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) [Open]
- #12 · 0.700 · [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) [Open]
- #13 · 0.700 · [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) [Open]
- #14 · 0.700 · [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) [Open]
- #15 · 0.700 · [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) [Open]
- #16 · 0.600 · [Passivity (positive real part)](#passivity) [Restatement]
- #17 · 0.600 · [Relative Gram matrix G_rel](#relative-gram) [Restatement]
- #18 · 0.600 · [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) [Restatement]
- #27 · 0.540 · [Rosati positivity](#rosati) [Theorem]
- #28 · 0.540 · [Castelnuovo–Severi inequality](#castelnuovo-severi) [Theorem]
- #29 · 0.540 · [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) [Theorem]
- #30 · 0.540 · [RH for curves over F_q (Weil)](#fq-curves) [Cited]
- #31 · 0.540 · [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) [Theorem]
- #32 · 0.540 · [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) [Cited]
- #33 · 0.540 · [Decay rate ¼](#decay-quarter) [Theorem]
- #34 · 0.540 · [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) [Theorem]
- #35 · 0.540 · [Compatible complex structure J commuting with Frobenius](#compatible-j) [Theorem]
- #36 · 0.540 · [Connes trace formula](#connes-trace) [Cited]
- #37 · 0.540 · [de Branges spaces](#de-branges) [Cited]
- #38 · 0.540 · [Epstein zeta no-go](#epstein) [Theorem]
- #39 · 0.540 · [Hasse bound as a positive degree form](#hasse-pythagoras) [Theorem]
- #40 · 0.540 · [Li criterion](#li-criterion) [Cited]
- #41 · 0.540 · [Suzuki’s de Branges line from the prime side](#suzuki-line) [Cited]
- #42 · 0.540 · [Bagchi recurrence](#bagchi) [Cited]
- #43 · 0.540 · [de Bruijn–Newman constant Λ](#debruijn-newman) [Cited]
- #44 · 0.540 · [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) [Theorem]
- #57 · 0.420 · [Two-point form g + iω ≥ 0](#two-point) [Restatement]
- #62 · 0.400 · [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) [Numerical]
- #65 · 0.380 · [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) [Open]
- #67 · 0.360 · [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) [Theorem]
- #68 · 0.360 · [Krein collisions (how ghosts are born)](#krein-collision) [Theorem]
- #69 · 0.360 · [Two partners of a zero (duality vs conjugation)](#two-partners) [Theorem]
- #70 · 0.360 · [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) [Theorem]

### True for ζ but ghost-blind or untested against the fakes (71)

- #19 · 0.579 · [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) [Theorem]
- #20 · 0.579 · [Ax1–Ax3 axioms (Yoneda specification)](#ax123) [Theorem]
- #21 · 0.579 · [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) [Theorem]
- #22 · 0.579 · [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) [Theorem]
- #23 · 0.579 · [Parity argument: linear χ cannot see D²](#parity-linear-chi) [Theorem]
- #24 · 0.579 · [Tautology boundary (zero side vs prime side)](#tautology-boundary) [Theorem]
- #25 · 0.579 · [Deninger’s foliated program](#deninger) [Cited]
- #26 · 0.579 · [No étale H¹ for Spec ℤ](#no-etale-h1) [Theorem]
- #46 · 0.492 · [Integer dimension over 𝕊 (minimal generators)](#dim-s) [Numerical]
- #47 · 0.452 · [Hodge index theorem](#hodge-index) [Theorem]
- #48 · 0.452 · [Lax–Phillips scattering](#lax-phillips) [Cited]
- #49 · 0.452 · [Cartan involution / compact unitary group](#cartan-involution) [Theorem]
- #50 · 0.452 · [Connes–Consani sites](#connes-consani) [Cited]
- #51 · 0.452 · [Pole plane / Tate poles at s = 0, 1](#pole-plane) [Theorem]
- #52 · 0.452 · [Products grow linearly (2n), not quadratically](#products-linear) [Theorem]
- #53 · 0.452 · [Yoneda specification](#yoneda) [Theorem]
- #58 · 0.419 · [Riemann hypothesis (target node)](#rh) [Open]
- #59 · 0.419 · [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) [Open]
- #60 · 0.419 · [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) [Open]
- #61 · 0.419 · [Hilbert–Pólya](#hilbert-polya) [Open]
- #71 · 0.347 · [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) [Cited]
- #72 · 0.347 · [Automorphy defect (TAA Lemma 144)](#automorphy-defect) [Theorem]
- #73 · 0.347 · [Certified positivity windows](#certified-windows) [Numerical]
- #74 · 0.325 · [Hodge–Riemann bilinear relations](#hodge-riemann) [Theorem]
- #75 · 0.325 · [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) [Theorem]
- #76 · 0.325 · [√2 family](#sqrt2-family) [Theorem]
- #77 · 0.325 · [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) [Cited]
- #78 · 0.325 · [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) [Theorem]
- #79 · 0.325 · [Closed geodesics on the modular surface](#closed-geodesics) [Theorem]
- #80 · 0.325 · [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) [Theorem]
- #81 · 0.325 · [Selberg resonances](#selberg-resonances) [Theorem]
- #82 · 0.325 · [Arakelov geometry](#arakelov) [Cited]
- #83 · 0.325 · [Cusp ≠ archimedean place](#cusp-vs-infinity) [Theorem]
- #84 · 0.325 · [Density / volume reading](#density-volume) [Theorem]
- #85 · 0.325 · [F₁ base](#f1-base) [Cited]
- #86 · 0.325 · [Principalization](#principalization) [Theorem]
- #87 · 0.325 · [Spec ℤ is terminal](#spec-z-terminal) [Theorem]
- #88 · 0.325 · [Spinor/Clifford route](#spinor-route) [Theorem]
- #89 · 0.325 · [Weil Rosetta stone](#weil-rosetta) [Cited]
- #90 · 0.325 · [Cohesion (arena)](#cohesion) [Theorem]
- #91 · 0.325 · [Local-to-global failure](#local-global) [Theorem]
- #94 · 0.307 · [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) [Theorem]
- #95 · 0.307 · [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) [Theorem]
- #96 · 0.307 · [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) [Theorem]
- #97 · 0.307 · [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) [Theorem]
- #98 · 0.307 · [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) [Cited]
- #99 · 0.307 · [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) [Cited]
- #100 · 0.307 · [Archimedean place and Γ_ℝ factor](#archimedean-place) [Theorem]
- #101 · 0.307 · [Cusp forms & Petersson positivity](#cusp-forms-petersson) [Theorem]
- #102 · 0.307 · [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) [Cited]
- #103 · 0.307 · [Tate count / Picard number (ghost-blind)](#tate-count) [Theorem]
- #104 · 0.307 · [Hecke operators](#hecke) [Theorem]
- #105 · 0.307 · [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) [Numerical]
- #106 · 0.307 · [Archimedean thresholds a*](#arch-threshold) [Numerical]
- #107 · 0.307 · [Maass–Selberg relations](#maass-selberg) [Numerical]
- #108 · 0.267 · [Metaplectic / Kubota cocycle](#metaplectic) [Theorem]
- #109 · 0.267 · [The prime 2 as the wild place](#prime-two-wild) [Theorem]
- #110 · 0.267 · [Scattering unitarity |φ| = 1](#scattering-phi) [Theorem]
- #111 · 0.267 · [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) [Theorem]
- #112 · 0.267 · [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) [Theorem]
- #113 · 0.267 · [Half-density normalization |x|^{½}](#half-density) [Theorem]
- #114 · 0.267 · [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) [Cited]
- #115 · 0.267 · [Counts vs quadratic positivity](#count-positivity) [Theorem]
- #116 · 0.267 · [w₂ / Čech class (TAA Lemma 138)](#w2-cech) [Theorem]
- #117 · 0.267 · [Weight ladder (modular weights)](#weight-ladder) [Theorem]
- #118 · 0.267 · [Yoshida window positivity](#yoshida) [Cited]
- #119 · 0.267 · [Cup product / Poincaré duality pairing](#cup-product) [Theorem]
- #120 · 0.267 · [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) [Theorem]
- #121 · 0.267 · [Bost–Connes KMS states](#kms-bost-connes) [Cited]
- #122 · 0.267 · [Spin structure & theta characteristic](#spin-theta) [Theorem]
- #131 · 0.165 · [Standard conjectures (Hodge type)](#standard-conj) [Open]

### Separates ζ from the fakes, but the claim itself is interpretive (Analogy/Heuristic) (5)

- #45 · 0.532 · [Gain lines (active media)](#gain-line) [Analogy]
- #54 · 0.451 · [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) [Heuristic]
- #55 · 0.451 · [Must-fail-for-DH acceptance test](#dh-acceptance) [Heuristic]
- #63 · 0.392 · [Källén–Lehmann spectral positivity](#kallen-lehmann) [Analogy]
- #64 · 0.392 · [Time delay (Wigner)](#time-delay) [Analogy]

### Background: interpretive and not separating (12)

- #56 · 0.423 · [BRST / Gupta–Bleuler physical quotient](#brst) [Analogy]
- #66 · 0.377 · [Displaced reference (subtracting the pole)](#displaced-reference) [Heuristic]
- #92 · 0.324 · [Kramers–Kronig relations](#kramers-kronig) [Analogy]
- #93 · 0.324 · [Gribov ambiguity](#gribov) [Analogy]
- #123 · 0.256 · ["Cocycles give structure, not sign"](#cocycle-principle) [Heuristic]
- #124 · 0.226 · [Buoyancy / Archimedes principle](#archimedes) [Analogy]
- #125 · 0.226 · [Heaviside RLGC line](#heaviside) [Analogy]
- #126 · 0.226 · [Mass-density positivity](#mass-density) [Analogy]
- #127 · 0.226 · [Distortionless line R/L = G/C](#distortionless) [Analogy]
- #128 · 0.212 · [Anomalous dispersion](#anomalous-dispersion) [Analogy]
- #129 · 0.181 · [Lamb cutoff](#lamb-cutoff) [Analogy]
- #130 · 0.181 · [Two different χ’s: Euler characteristic vs class-group character](#two-chis) [Analogy]

## Concepts by primary axis

Sections are ordered by their highest-ranked entry; entries within each section by descending priority. Missing pieces are listed above and not repeated.

## Axis: sign/positivity (Ax2) <a id="axis-sign-positivity-ax2"></a>

### #1 · 0.720 · Weil positivity criterion <a id="weil-positivity"></a>

**Label:** Cited · **id:** `weil_positivity` · **quadrant:** RH-sharp

*In plain words:* A quadratic form built from primes, the archimedean place and the pole. RH holds exactly when it is never negative.

**Core.** Weil 1952: RH ⇔ W(f∗f̃*) ≥ 0 for all test f; equivalently the Hermitian form 𝒬 is positive, ⇔ a unitary Hilbert realization of the scaling flow (TAA Lemma 1 Thm 2.1 (iv)).

**Formula.** RH ⇔ W(f ∗ f̃*) ≥ 0 ∀f

**Numbers.** κ(𝒬) = N₊ (TAA Lemma 1)

**Also known as:** Weil criterion; W(f∗f̃*) ≥ 0; Weil form 𝒬; arithmetic action S[F]

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH, Spec ℤ gap

**TAA lemmas:** 1, 17, 98, 103, 142

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** The zero-side check is tautological (TAA Lemma 142); only the prime side with no zeros is a test.

> ⚠ **Correction / caution.** "Q = LP + positive" is false (TAA Lemma 8).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Weil 1952
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — TAA Lemma 142: Weil form = relative intersection matrix on translates
- same mechanism as → [Hodge index theorem](#hodge-index) — Spec ℤ analogue of Hodge index on V₀ (TAA Lemma 91)
- same mechanism as → [Two-point form g + iω ≥ 0](#two-point) — TAA Lemma 103: g + iω ≥ 0 ⇔ Weil

**Relations (incoming):** [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (implies); [Relative Gram matrix G_rel](#relative-gram) (same mechanism as); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (same mechanism as); [Tautology boundary (zero side vs prime side)](#tautology-boundary) (same mechanism as); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (same mechanism as); [Connes trace formula](#connes-trace) (same mechanism as); [Li criterion](#li-criterion) (same mechanism as); [Two-point form g + iω ≥ 0](#two-point) (same mechanism as); [Källén–Lehmann spectral positivity](#kallen-lehmann) (same mechanism as); [Archimedean place and Γ_ℝ factor](#archimedean-place) (lives in)

### #5 · 0.720 · Lagarias/Hinkkanen criterion <a id="lagarias"></a>

**Label:** Cited · **id:** `lagarias` · **quadrant:** RH-sharp

*In plain words:* RH ⇔ the log-derivative of ξ has positive real part to the right of the line.

**Core.** Lagarias 1999 (1.5), credited to Hinkkanen: RH ⇔ Re ξ′/ξ(s) > 0 on Re s > ½ (TAA Lemmas 17, 146).

**Formula.** RH ⇔ Re ξ′/ξ(s) > 0 (Re s > ½)

**Numbers.** DH: Re ξ′/ξ = −66.8

**Also known as:** Re ξ′/ξ > 0; Hinkkanen

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 17, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Passivity (positive real part)](#passivity)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH violates it

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (same mechanism as); [Passivity (positive real part)](#passivity) (same mechanism as)

### #17 · 0.600 · Relative Gram matrix G_rel <a id="relative-gram"></a>

**Label:** Restatement · **id:** `relative_gram` · **quadrant:** RH-sharp

*In plain words:* Take a test function, translate it, and form the matrix of pairings after removing the pole plane. RH ⇔ this matrix is positive (semi)definite for all choices.

**Core.** TAA Lemma 142: G_rel(f; t_i) with zero-free entries (flow, U/Tate poles, Γ_ℝ, Λ(n)); G_rel ⪰ 0 ∀ ⇔ Weil ⇔ RH. Unconditional only on windows ≤ log 3 (TAA Lemma 10) and arch a* (TAA Lemma 127).

**Formula.** G_rel ⪰ 0 ∀ f, t_i ⇔ RH

**Also known as:** relative intersection matrix; Gram on translates; Weil Gram

**Axes:** sign/positivity (Ax2), ghost-sensitive, reference/pole/cusp, restatement ⇔ RH, Spec ℤ gap

**TAA lemmas:** 142, 10, 127

**Scores (Heuristic):** gap significance 0.8 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Using the zero side to "check" it is tautological.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — TAA Lemma 142
- same mechanism as → [Weil positivity criterion](#weil-positivity)
- analogue of → [Primitive part V₀ = U^⊥](#primitive-part) — Gram on U^⊥

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as); [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (same mechanism as); [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as)

### #18 · 0.600 · Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0 <a id="rr-strategy-sff"></a>

**Label:** Restatement · **id:** `rr_strategy_sff` · **quadrant:** RH-sharp

*In plain words:* Connes–Consani’s plan: build divisors D(f) on the square from test functions; RH is equivalent to their self-intersection being ≤ 0, and an RR theorem there would prove it.

**Core.** CC18: RH ⇔ s(f,f) ≤ 0 (12), s(f,f) = D•D with D = ∫fΨ_λ (14); five steps, only step 1 (complex lift) built; H¹ on the square open. ½D(f)•D(f) = ½s(f,f) is the Weil form (TAA Lemma 147 §4, TAA Lemma 142).

**Formula.** RH ⇔ s(f,f) = D(f)•D(f) ≤ 0

**Also known as:** CC18; s(f,f) = D•D; five steps; D = ∫fΨ_λ

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH, Spec ℤ gap

**TAA lemmas:** 147, 142

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** The H⁰ side is ghost-blind; only the topological side s(f,f) is ghost-sensitive (TAA Lemma 147 §4).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — CC18 (12)
- same mechanism as → [Weil positivity criterion](#weil-positivity) — ½ s(f,f) = Weil form
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — TAA Lemma 142 computes it
- lives in → [Connes–Consani sites](#connes-consani) — scaling site square

**Relations (incoming):** [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (same mechanism as); [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (same mechanism as)

### #20 · 0.579 · Ax1–Ax3 axioms (Yoneda specification) <a id="ax123"></a>

**Label:** Theorem · **id:** `ax123` · **quadrant:** true but ghost-blind/untested

*In plain words:* The three ingredients that together force RH for curves: Hodge index on Frobenius graphs (Ax1), a positive involution † (Ax2), and ππ† = q for that same † (Ax3).

**Core.** TAA Lemma 137: on T_W, |α| = √q ⇔ Ax2 ∧ Ax3 ⇔ Ax1 ∀N. Each axiom alone is ghost-blind (Ax3 alone tautological; Ax2 alone holds for fakes); only the joint requirement separates. All qualifying items are over F_q; no Spec ℤ item qualifies.

**Formula.** |α| = √q ⇔ Ax2 ∧ Ax3 ⇔ Ax1 ∀N

**Numbers.** 7 of 135 items in the programme’s positivity inventory pass (TAA Lemma 137) · n₊(Ax1) = 1 + n₋(Ax2) observed

**Also known as:** Ax1; Ax2; Ax3; T_W

**Axes:** sign/positivity (Ax2), phase/unitarity (Ax3), structure/frame (Ax1), geometry over F_q

**TAA lemmas:** 137, 138, 141

**Scores (Heuristic):** gap significance 0.8 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** Ax3 (unitarity, ππ† = q) is satisfied by ghosts too; never present it as positivity.

**Relations (outgoing):**

- special case of → [Rosati positivity](#rosati) — Ax2 ∧ Ax3 = Rosati
- same mechanism as → [Hodge index theorem](#hodge-index) — Ax1
- lives in → [RH for curves over F_q (Weil)](#fq-curves) — proved only over F_q

**Relations (incoming):** [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) (special case of); [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) (fails for); [Yoneda specification](#yoneda) (same mechanism as); [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) (same mechanism as)

### #27 · 0.540 · Rosati positivity <a id="rosati"></a>

**Label:** Theorem · **id:** `rosati` · **quadrant:** RH-sharp

*In plain words:* An involution † on endomorphisms with Tr(φφ†) > 0 — like a squared length that is never negative. With ππ† = q it forces |α| = √q.

**Core.** Tr(φφ†) > 0 on End⁰(J); ππ† = q ⇒ |α| = √q (Milne AV 14.3). On R[F]: Rosati PD ⇔ RH-model ⇔ ∃ compatible J with [J,F] = 0; n₋ = #real pairs + 2#quartets (TAA Lemma 106). Over ℚ: Rosati = Weil form is a restatement.

**Formula.** Tr(φφ†) > 0; ππ† = q

**Numbers.** E^n over F₅: Tr = 2ΣN(φ_ij) > 0, 3000/3000 (TAA Lemma 136) · signatures true (2,0),(4,0),(8,0); ghost (1,1); quartet (2,2)

**Also known as:** Rosati involution †; Tr(φφ†) > 0; positive involution; Ax2∧Ax3

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 84, 99, 106, 133, 136

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** |φ| = 1 on Re s = ½ is only the adjoint half ππ† = q (Ax3), ghost-blind.

> ⚠ **Correction / caution.** Positivity over F_q is geometric, from intersection numbers, not arithmetic (TAA Lemma 106, correction 1).

**Relations (outgoing):**

- same mechanism as → [Castelnuovo–Severi inequality](#castelnuovo-severi) — TAA Lemma 133
- special case of → [Cartan involution / compact unitary group](#cartan-involution) — Rosati = Cartan θ_J on commutant (TAA Lemma 99)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — over ℚ
- analogue of → [Mass-density positivity](#mass-density) — mass-like single positivity
- lives in → [RH for curves over F_q (Weil)](#fq-curves) — proved setting

**Relations (incoming):** [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (special case of); [Castelnuovo–Severi inequality](#castelnuovo-severi) (same mechanism as); [Hasse bound as a positive degree form](#hasse-pythagoras) (special case of); [Cartan involution / compact unitary group](#cartan-involution) (same mechanism as); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of); [Mass-density positivity](#mass-density) (analogue of)

### #28 · 0.540 · Castelnuovo–Severi inequality <a id="castelnuovo-severi"></a>

**Label:** Theorem · **id:** `castelnuovo_severi` · **quadrant:** RH-sharp

*In plain words:* On the surface C×C a class cannot be "too timelike" relative to the two fibre directions; applied to Frobenius graphs it gives RH for curves.

**Core.** D² ≤ 2(D·f₁)(D·f₂); def(D) = 2d₁d₂ − D² = −(D°)² = Tr_{H¹}(α_D α_D†) (C–S = Rosati, TAA Lemma 133). Weil mF + n: −(2gqm² + 2amn + 2gn²) ≤ 0 ⇔ a² ≤ 4g²q (TAA Lemma 125).

**Formula.** D² ≤ 2(D·f₁)(D·f₂)

**Numbers.** primitive Gram det 4p − a² > 0 (29 primes, TAA Lemma 133)

**Also known as:** C–S; reverse Cauchy–Schwarz; def(D)

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 14, 114, 125, 133

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** A “−2Tr” formula holds only on the primitive part with the g-dimensional trace.

**Relations (outgoing):**

- same mechanism as → [Rosati positivity](#rosati) — TAA Lemma 133: C–S = Rosati
- special case of → [Hodge index theorem](#hodge-index) — C–S ⇔ Hodge index on ⟨f₁,f₂,D⟩
- analogue of → [Buoyancy / Archimedes principle](#archimedes) — buoyancy reading
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — relative to the null rays

**Relations (incoming):** [Rosati positivity](#rosati) (same mechanism as); [RH for curves over F_q (Weil)](#fq-curves) (implies); [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) (analogue of); [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (fails for); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (fails for); [Buoyancy / Archimedes principle](#archimedes) (analogue of)

### #30 · 0.540 · RH for curves over F_q (Weil) <a id="fq-curves"></a>

**Label:** Cited · **id:** `fq_curves` · **quadrant:** RH-sharp

*In plain words:* For a curve over a finite field the Frobenius eigenvalues all have size √q. This is the one setting where TAA’s positivity is a theorem.

**Core.** Weil 1948: Castelnuovo–Severi / Hodge index on C×C ⇒ |α_i| = √q. Proved without the zeros: surface + ample class + Riemann–Roch ⇒ Hodge index ⇒ sign.

**Formula.** |α_i| = √q; |N − q − 1| ≤ 2g√q

**Also known as:** Hasse–Weil; |α| = √q; column 2

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 3, 14, 98, 133, 140

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Weil already did column 2 (1940 note, 1948 books); the open step is column 3.

**Relations (outgoing):**

- implies → [Castelnuovo–Severi inequality](#castelnuovo-severi) — proof route
- analogue of → [Riemann hypothesis (target node)](#rh) — column 2 ↔ column 3 (Rosetta)
- lives in → [Weil Rosetta stone](#weil-rosetta) — column 2

**Relations (incoming):** [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (lives in); [Rosati positivity](#rosati) (lives in); [Weil Rosetta stone](#weil-rosetta) (analogue of)

### #35 · 0.540 · Compatible complex structure J commuting with Frobenius <a id="compatible-j"></a>

**Label:** Theorem · **id:** `compatible_J` · **quadrant:** RH-sharp

*In plain words:* A quarter-turn that commutes with Frobenius and makes the form positive; it exists exactly when the curve satisfies RH.

**Core.** J = (2F − a)/√(4q − a²) (TAA Lemma 101) exists only if a² < 4q; 2^g sign choices, exactly one positive. Finite: compatible J with [J,F] = 0 ⇔ F unitary semisimple (TAA Lemma 104). For ζ: J exists ⇔ RH (restatement, TAA Lemma 104 dichotomy).

**Formula.** J = (2F − a)/√(4q − a²)

**Numbers.** g = 1, q = 101: J = J_F exact; ghosts give Cl(1,1)

**Also known as:** J = (2F − a)/√(4q − a²); h(i); polarizing J

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 99, 100, 101, 104, 110

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** A quartet J is symplectic but never compatible (sig (2,2)) (TAA Lemma 110).

> ⚠ **Correction / caution.** With a W-independent form J is unconditional but ghost-blind (TAA Lemma 104).

**Relations (outgoing):**

- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — for ζ
- same mechanism as → [Spinor/Clifford route](#spinor-route) — Clifford pair version

**Relations (incoming):** [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (same mechanism as); [Spinor/Clifford route](#spinor-route) (same mechanism as)

### #37 · 0.540 · de Branges spaces <a id="de-branges"></a>

**Label:** Cited · **id:** `de_branges` · **quadrant:** RH-sharp

*In plain words:* Hilbert spaces of entire functions built from a Hermite–Biehler function E; RH becomes "E_h is Hermite–Biehler", but de Branges’ stronger positivity conditions are known to fail for ζ.

**Core.** TAA Lemma 36 Thm 3.1: for h ∈ (0,½], all β ≤ ½ + h ⇔ PR on σ > ½ + h ⇔ E_{h′} HB ∀h′ > h; h = ½ free, h → 0 = RH. Conrey–Li 2000 (opened, TAA Lemma 78): de Branges positivity fails for ζ and χ₄. TAA Lemma 118: Ψ_c passive ⇔ E_c = ξ(·+c) Hermite–Biehler. TAA Lemma 34: Suzuki’s de Branges line from the prime side.

**Also known as:** Hermite–Biehler

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 34, 36, 78, 118

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Conrey–Li: de Branges’ stronger conditions fail — beware "positivity ⇒ RH" shortcuts.

**Relations (outgoing):**

- same mechanism as → [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky)
- same mechanism as → [Passivity (positive real part)](#passivity) — HB ⇔ passive (TAA Lemma 118)

**Relations (incoming):** [Suzuki’s de Branges line from the prime side](#suzuki-line) (same mechanism as)

### #39 · 0.540 · Hasse bound as a positive degree form <a id="hasse-pythagoras"></a>

**Label:** Theorem · **id:** `hasse_pythagoras` · **quadrant:** RH-sharp

*In plain words:* For an elliptic curve the degree of an endomorphism is a positive quadratic form; Hasse’s bound is that this form is positive (Cauchy–Schwarz / Pythagoras).

**Core.** deg(m + nπ) = m² + amn + qn² is PD ⇔ a² < 4q; Hasse = Cauchy–Schwarz. Ghost a = 25, q = 101: deg(10 − π) = −49 (TAA Lemma 106).

**Formula.** m² + a mn + q n² > 0 ⇔ a² < 4q

**Numbers.** ghost deg(10 − π) = −49

**Also known as:** deg form; Q_p = x² + a_p xy + p y²; Pythagoras

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 19, 64, 106, 114

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- special case of → [Rosati positivity](#rosati) — genus 1
- analogue of → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — definite forms = hyperboloid sheet (TAA Lemma 14)

**Relations (incoming):** [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (analogue of)

### #40 · 0.540 · Li criterion <a id="li-criterion"></a>

**Label:** Cited · **id:** `li_criterion` · **quadrant:** RH-sharp

*In plain words:* RH ⇔ the Li coefficients are non-negative.

**Core.** Li 1997 / Bombieri–Lagarias 1999: RH ⇔ λ_n ≥ 0 for all n — the Weil positivity in another basis. TAA Lemma 112 reads the Weil form as a Toeplitz–Carathéodory problem; TAA Lemma 131: no route supplies the positivity.

**Formula.** λ_n ≥ 0 ∀n

**Also known as:** λ_n ≥ 0

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 112, 131

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Weil positivity criterion](#weil-positivity) — same positivity, other basis
- same mechanism as → [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) — TAA Lemma 112

### #41 · 0.540 · Suzuki’s de Branges line from the prime side <a id="suzuki-line"></a>

**Label:** Cited · **id:** `suzuki_line` · **quadrant:** RH-sharp

*In plain words:* A de Branges / transmission-line object built from prime data whose passivity along the whole line is equivalent to RH.

**Core.** Su21 (Suzuki JFA 281 (2021) 109116): E^{ω,ν} = ξ(½ + ω − iz)^ν, νω > 1, Hankel kernel from prime-side data (TAA Lemma 34). TAA Lemma 37: headline exponential line Θ_c = exp(−2c ξ′/ξ); ‖𝒦[t]‖ < 1 ∀t ⇔ sup ≤ 1; weak form sup_t ≤ 1 ⇔ RH; "sup < 1" is false in the passive case; strict pointwise bound open (M11).

**Formula.** Θ_c = exp(−2c ξ′/ξ)

**Also known as:** Suzuki JFA 2021; E^{ω,ν}; exponential line Θ_c; G5 line

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 34, 37

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** "sup < 1" is false in the passive case; the correct form is sup ≤ 1 (TAA Lemma 37).

**Relations (outgoing):**

- same mechanism as → [de Branges spaces](#de-branges)
- same mechanism as → [Passivity (positive real part)](#passivity) — G5 as passive line
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — weak form (TAA Lemma 37)

### #47 · 0.452 · Hodge index theorem <a id="hodge-index"></a>

**Label:** Theorem · **id:** `hodge_index` · **quadrant:** true but ghost-blind/untested

*In plain words:* On a surface the intersection form has exactly one positive direction (the ample class); everything orthogonal to it is negative. This sign is what proves RH for curves.

**Core.** NS(C×C) ⊗ ℝ has signature (1, ρ−1); U = ⟨f₁,f₂⟩ is the (1,1) part and its complement is negative definite. Over ℚ, Hodge-index form on V₀ ⇔ RH (TAA Lemma 91, restatement). Surface + ample + RR ⇒ Hodge index (D8).

**Formula.** sig NS = (1, ρ − 1); D·D ≤ 0 on h^⊥

**Numbers.** true E×E (1,3), fakes (2,2) (TAA Lemma 88)

**Also known as:** NS signature (1, ρ−1); Lorentzian Néron–Severi; Ax1

**Axes:** sign/positivity (Ax2), geometry over F_q, structure/frame (Ax1)

**TAA lemmas:** 14, 88, 91, 98, 140, 145

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Effectivity and Hodge index are independent on both sides (TAA Lemma 94).

> ⚠ **Correction / caution.** Hodge index needs S2, S3, S5 too (TAA Lemma 145).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — D·D ≤ 0 on V₀ over ℚ (TAA Lemma 91)
- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst) — U^⊥ = physical quotient (TAA Lemma 115, TAA Lemma 146)
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — complement of U

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as); [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) (lives in); [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (same mechanism as); [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) (implies); [Parity argument: linear χ cannot see D²](#parity-linear-chi) (fails for); [Castelnuovo–Severi inequality](#castelnuovo-severi) (special case of); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Standard conjectures (Hodge type)](#standard-conj) (special case of)

### #49 · 0.452 · Cartan involution / compact unitary group <a id="cartan-involution"></a>

**Label:** Theorem · **id:** `cartan_involution` · **quadrant:** true but ghost-blind/untested

*In plain words:* A positive involution is the same thing as a compact (rotation-type) symmetry group; Albert lists the possible kinds.

**Core.** Positive involution ⇔ compact unitary group (TAA Lemma 99, Milne Prop 1.20); Rosati = Cartan θ_J on commutant of J; Weil numbers generate CM or totally real fields (TAA Lemma 136); Albert types I–IV.

**Also known as:** positive involution ⇔ compact form; Albert classification

**Axes:** sign/positivity (Ax2), structure/frame (Ax1)

**TAA lemmas:** 84, 99, 136

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Abelian scaling has only an outer Cartan U(1); zeros-as-angles = RH (circular, TAA Lemma 99).

**Relations (outgoing):**

- same mechanism as → [Rosati positivity](#rosati) — Rosati = Cartan θ_J (TAA Lemma 99)
- fails for → [Riemann hypothesis (target node)](#rh) — no compact Hodge circle for ℚ (TAA Lemma 100)

**Relations (incoming):** [Rosati positivity](#rosati) (special case of)

### #54 · 0.451 · Organizing split: ghost-blind = phase, ghost-sensitive = sign <a id="split-blind-sensitive"></a>

**Label:** Heuristic · **id:** `split_blind_sensitive` · **quadrant:** sharp but interpretive

*In plain words:* Every test that ghosts pass is about phase/unitarity; every test that catches a ghost is about the sign of a spectral weight, and for ζ that sign is RH.

**Core.** TAA Lemma 146 synthesis: functional equation, |φ| = 1, cocycles, Hecke, cusp positivity are ghost-blind (Ax3); Lagarias sign, Weil sign, Rosati sign are ghost-sensitive (Ax2) and ⇔ RH for ζ. Every ghost-sensitive global quadratic statement for Spec ℤ found so far is a restatement.

**Formula.** ghost-blind ↔ Ax3 (phase); ghost-sensitive ↔ Ax2 (sign) ⇔ RH

**Numbers.** DH: FE to 5×10⁻¹⁵ yet Re ξ′/ξ = −66.8

**Also known as:** TAA Lemma 146 split; two bins; phase vs sign

**Axes:** sign/positivity (Ax2), phase/unitarity (Ax3), ghost-blind, ghost-sensitive

**TAA lemmas:** 146, 137, 141

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 0.7 · specificity 1.0 · tractability 0.5 · evidence 0.6 → priority 0.451

> ⚠ **Correction / caution.** An organizing observation, not a theorem: "sign" items for curves are theorems, for ζ restatements.

**Relations (outgoing):**

- same mechanism as → [Kramers–Kronig relations](#kramers-kronig) — absorption (sign) vs dispersion (phase) split
- same mechanism as → [Ax1–Ax3 axioms (Yoneda specification)](#ax123) — Ax2 vs Ax3

**Relations (incoming):** [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Kramers–Kronig relations](#kramers-kronig) (same mechanism as); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); ["Cocycles give structure, not sign"](#cocycle-principle) (same mechanism as)

### #57 · 0.420 · Two-point form g + iω ≥ 0 <a id="two-point"></a>

**Label:** Restatement · **id:** `two_point` · **quadrant:** RH-sharp

*In plain words:* Combine a metric g and symplectic ω into one Hermitian form; positivity ⇔ Weil.

**Core.** TAA Lemma 103: g + iω ≥ 0 ⇔ Weil ⇔ RH.

**Formula.** g + iω ≥ 0

**Also known as:** Kähler two-point

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 103

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Weil positivity criterion](#weil-positivity)

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as)

### #67 · 0.360 · Negative index κ(𝒬) = N₊ (ghost count) <a id="kappa-index"></a>

**Label:** Theorem · **id:** `kappa_index` · **quadrant:** RH-sharp

*In plain words:* Counts how many negative directions the Weil form has; each off-line zero quartet contributes exactly 2.

**Core.** Unconditional: κ(𝒬) = N₊ (TAA Lemma 1 Thm 2.1); each ghost quartet gives 2 negative eigenvalues (TAA Lemma 103, Bombieri). Finite form: n₋ = k_r + 2k_c = ½ rk E² (TAA Lemma 110 Thm 2.3); Rosati n₋ = k = τ + ½Z_off = n₊(NS) − 1 (TAA Lemma 88 Thm B).

**Formula.** n₋ = k_r + 2k_c

**Numbers.** 2 negative eigenvalues per quartet

**Also known as:** κ; negative index; Bombieri count; n₋ = #real pairs + 2#quartets

**Axes:** sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 1, 88, 93, 103, 110

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

> ⚠ **Correction / caution.** Count convention: TAA Lemma 91 n₊ = 2k vs TAA Lemma 88 k = ½Z_off — see TAA Lemma 92 C5 notation clash.

**Relations (outgoing):**

- same mechanism as → [Rosati positivity](#rosati) — Rosati index on R[F] = Weil index (TAA Lemma 106)
- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — one quartet ↦ two negatives

**Relations (incoming):** [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) (same mechanism as)

### #74 · 0.325 · Hodge–Riemann bilinear relations <a id="hodge-riemann"></a>

**Label:** Theorem · **id:** `hodge_riemann` · **quadrant:** true but ghost-blind/untested

*In plain words:* Pairing a holomorphic form with its own complex conjugate gives a positive number: a genuine |amplitude|².

**Core.** HR holds on every compact Riemann surface; HR form = 2 × Petersson (TAA Lemma 134). Positivity = complex structure inserted (Weil operator C = i^{p−q}). Hecke self-adjointness gives a_p ∈ ℝ, not |a_p| ≤ 2√p.

**Formula.** i ∫ α ∧ ᾱ = 2∫|f|² > 0

**Also known as:** HR form; i∫α∧ᾱ > 0; Riemann form; Petersson positivity

**Axes:** sign/positivity (Ax2), geometry over F_q

**TAA lemmas:** 40, 102, 134, 139, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Column 2 (F_q) never fully inherited the HR sign; Castelnuovo replaces it algebraically (TAA Lemma 140).

**Relations (outgoing):**

- special case of → [Cup product / Poincaré duality pairing](#cup-product) — cup with the conjugate through the Hodge structure
- same mechanism as → [Rosati positivity](#rosati) — Rosati = H-adjoint (TAA Lemma 134)
- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) — positivity needs C = i^{p−q}

**Relations (incoming):** [Cusp forms & Petersson positivity](#cusp-forms-petersson) (same mechanism as); [Hecke operators](#hecke) (same mechanism as)

### #75 · 0.325 · Weil operator C = i^{p−q} = Wick rotation <a id="weil-operator"></a>

**Label:** Theorem · **id:** `weil_operator` · **quadrant:** true but ghost-blind/untested

*In plain words:* Turning an indefinite pairing into a positive one by inserting a quarter turn — the same move as Wick rotation in physics.

**Core.** TAA Lemma 139: Q indefinite → Q(C·, ·̄) PD (Rosati); Abel–Jacobi = principalization. A complex structure is a μ₄ action (J² = −1). Obstruction: Pic^(Spec ℤ̄) ≅ ℝ has no complex structure.

**Formula.** C = i^{p−q}; Q(x, C ȳ) > 0

**Numbers.** y² = x³ − x: π/√p primitive 4th root of unity for p ≡ 3 mod 4 (TAA Lemma 140)

**Also known as:** Wick rotation; J² = −1; μ₄ action; complex structure

**Axes:** sign/positivity (Ax2), Spec ℤ gap, physics analogue

**TAA lemmas:** 139, 140, 102

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** The Fourier transform is the swap, not the Weil operator (TAA Lemma 140).

> ⚠ **Correction / caution.** Over F_q the sign is algebraic (Castelnuovo); the Hodge model is only an analogy there (TAA Lemma 139 caveat).

**Relations (outgoing):**

- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j) — J = h(i)
- analogue of → [Principalization](#principalization) — Abel–Jacobi = principalization
- fails for → [Arakelov geometry](#arakelov) — no complex structure on Pic^ ≅ ℝ

**Relations (incoming):** [Compatible complex structure J commuting with Frobenius](#compatible-j) (same mechanism as); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Arakelov geometry](#arakelov) (fails for); [Principalization](#principalization) (analogue of)

### #78 · 0.325 · Toeplitz / Verblunsky coefficients <a id="toeplitz-verblunsky"></a>

**Label:** Theorem · **id:** `toeplitz_verblunsky` · **quadrant:** true but ghost-blind/untested

*In plain words:* Positivity of Toeplitz matrices ⇔ |α_n| < 1; each step a boost of rapidity artanh|α|.

**Core.** TAA Lemma 112 [C Simon]: Carathéodory–Toeplitz–Herglotz; T_{n+1} ≻ 0 ⇔ |α_j| < 1 ∀j < n; n₋(T_N) = #{E_n < 0}, sign flips at each |α_j| > 1. Levinson: PD ⇔ |κ_j| < 1, each step a boost of rapidity artanh κ (true |κ| < 1 for 60 orders; ghost κ₈ = −1.0009). TAA Lemma 117: U(1,1) boost of velocity |α|; |α| > 1 = Krein swap ∘ boost. TAA Lemma 37/TAA Lemma 118: Schur/Verblunsky layer stripping = restatement (circular).

**Formula.** |α_n| < 1

**Numbers.** closest true κ₈ = −0.986 · ghost 14.13 ± 0.1i: κ₈ = −1.0009

**Also known as:** Szegő; Levinson

**Axes:** sign/positivity (Ax2)

**TAA lemmas:** 37, 98, 112, 117, 118

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- analogue of → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost)

**Relations (incoming):** [de Branges spaces](#de-branges) (same mechanism as); [Li criterion](#li-criterion) (same mechanism as); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (analogue of)

### #88 · 0.325 · Spinor/Clifford route <a id="spinor-route"></a>

**Label:** Theorem · **id:** `spinor_route` · **quadrant:** true but ghost-blind/untested

*In plain words:* Encode J and F as a Clifford pair; ghosts give the indefinite Cl(1,1).

**Core.** TAA Lemma 101/TAA Lemma 110: ghosts give Cl(1,1); true case Cl(2,0).

**Also known as:** Clifford pair; Cl(1,1)

**Axes:** sign/positivity (Ax2), geometry over F_q

**TAA lemmas:** 101, 110

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j)

**Relations (incoming):** [Compatible complex structure J commuting with Frobenius](#compatible-j) (same mechanism as)

### #101 · 0.307 · Cusp forms & Petersson positivity <a id="cusp-forms-petersson"></a>

**Label:** Theorem · **id:** `cusp_forms_petersson` · **quadrant:** true but ghost-blind/untested

*In plain words:* Cusp forms have positive Petersson norm — a real positivity, but it does not see ζ’s zeros.

**Core.** ⟨f,f⟩ = ∫|f|²y^k dμ > 0; HR = 2 × Petersson (TAA Lemma 134). Ghost-blind for ζ (TAA Lemma 146).

**Formula.** ⟨f,f⟩ = ∫ |f|² y^k dμ > 0

**Also known as:** Petersson norm; ⟨f,f⟩ > 0

**Axes:** sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 134, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Positive but about cusp forms, not ζ’s spectral weights.

**Relations (outgoing):**

- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann)
- fails for → [Riemann hypothesis (target node)](#rh) — ghost-blind

**Relations (incoming):** [Weight ladder (modular weights)](#weight-ladder) (same mechanism as)

## Axis: no-go / refuted <a id="axis-no-go-refuted"></a>

### #2 · 0.720 · Davenport–Heilbronn function <a id="davenport-heilbronn"></a>

**Label:** Theorem · **id:** `davenport_heilbronn` · **quadrant:** RH-sharp

*In plain words:* Has a functional equation but no Euler product, and zeros off the line.

**Core.** DH is a location test only (no Euler product, TAA Lemma 103). Tail 0.7398 (TAA Lemma 78) vs 0.7376 (TAA Lemma 136).

**Numbers.** 0.7398 (TAA Lemma 78) · 0.7376 (TAA Lemma 136) · 5×10⁻¹⁵ · −66.8

**Also known as:** DH

**Axes:** no-go / refuted, ghost-sensitive

**TAA lemmas:** 78, 103, 136, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** Tail number conflict.

**Relations (outgoing):**

- fails for → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (fails for); [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (fails for); [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) (analogue of); [Epstein zeta no-go](#epstein) (same mechanism as); [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) (fails for); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (fails for)

### #38 · 0.540 · Epstein zeta no-go <a id="epstein"></a>

**Label:** Theorem · **id:** `epstein` · **quadrant:** RH-sharp

*In plain words:* Epstein zeta functions of binary quadratic forms have a functional equation but no Euler product, and they have zeros off the line — the classic counterexample class next to DH.

**Core.** TAA Lemma 83: Epstein x² + 5y² = ζL(χ₋₂₀) + L(χ₋₄)L(χ₅); N(200) = 253 zeros, 183 on the line (70 off-line); first off-line 0.93297 + 15.66825i. TAA Lemma 135: 46 zeros with ½ < σ < 1 for t ≤ 250; control x² + y² (= 4ζL(χ₋₄), has Euler product): 0. TAA Lemma 138 R4: theta inversion and FE hold, unitarity ⇒ FE only, ghost-blind (Thm).

**Numbers.** 0.93297 + 15.66825i · N(200) = 253, 183 on line · 46 off-line zeros t ≤ 250

**Also known as:** Epstein

**Axes:** no-go / refuted, ghost-sensitive, numerics/certificate

**TAA lemmas:** 83, 135, 138

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- same mechanism as → [Davenport–Heilbronn function](#davenport-heilbronn)
- fails for → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — FE without RH
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — TAA Lemma 135 counts vs quadratic positivity

### #91 · 0.325 · Local-to-global failure <a id="local-global"></a>

**Label:** Theorem · **id:** `local_global` · **quadrant:** true but ghost-blind/untested

*In plain words:* Local positivity at each prime does not imply global.

**Core.** TAA Lemma 25 Rem 6.2: naive local positivity fails (K < 0 for |r| < 6.28984); CC21 Thm 1 local archimedean positivity only for supp ⊂ [2^{−½}, 2^{½}] with vanishing. TAA Lemma 64/TAA Lemma 65: local Hasse (Q_p > 0 at every p, proved) vs global RH for L(E,s) (open) — the collective split. TAA Lemma 66: local positivity via Deligne weights is ghost-blind residual data.

**Numbers.** |r| < 6.28984

**Also known as:** local positivity

**Axes:** no-go / refuted

**TAA lemmas:** 25, 64, 65, 66, 91

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

### #115 · 0.267 · Counts vs quadratic positivity <a id="count-positivity"></a>

**Label:** Theorem · **id:** `count_positivity` · **quadrant:** true but ghost-blind/untested

*In plain words:* Point counts being positive does not force RH; only quadratic forms can.

**Core.** TAA Lemma 109: 2935 count-positive ghosts (g = 2, q = 11).

**Numbers.** 2935

**Also known as:** N_n ≥ 0

**Axes:** no-go / refuted, ghost-blind

**TAA lemmas:** 109

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly)

**Relations (incoming):** [Epstein zeta no-go](#epstein) (same mechanism as); [Tate count / Picard number (ghost-blind)](#tate-count) (same mechanism as)

## Axis: reference/pole/cusp <a id="axis-reference-pole-cusp"></a>

### #3 · 0.720 · ψ(x) − x (explicit formula, deviation from the pole) <a id="psi-minus-x"></a>

**Label:** Cited · **id:** `psi_minus_x` · **quadrant:** RH-sharp

*In plain words:* Count prime powers with weight log p and subtract the pole’s prediction x; what remains is a sum over zeros. RH ⇔ the remainder is O(√x log²x).

**Core.** Explicit formula ψ(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½log(1 − x⁻²); RH ⇔ ψ(x) − x = O(x^{½+ε}). In TAA the x term is the pole/𝕃 reference; ψ − x ≠ 0 measures the flow-relative H¹.

**Formula.** ψ(x) − x = −Σ_ρ x^ρ/ρ + …

**Also known as:** Chebyshev ψ; prime counting error; ψ − x ≠ 0

**Axes:** reference/pole/cusp, ghost-sensitive, Spec ℤ gap

**TAA lemmas:** 142, 144

**Scores (Heuristic):** gap significance 0.8 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 0.8 → priority 0.720

> ⚠ **Correction / caution.** ψ(x) − x ≠ 0 is not a failure: it is the zero contribution relative to the pole reference.

> ❓ **Not verified / open.** The explicit-formula wording is standard (cited), not from a specific lemma section.

**Relations (outgoing):**

- same mechanism as → [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) — both compare a prime product/sum to a pole reference
- same mechanism as → [Displaced reference (subtracting the pole)](#displaced-reference) — subtract the pole
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — size O(x^{½+ε}) ⇔ RH
- analogue of → [Tate count / Picard number (ghost-blind)](#tate-count) — N_n − (1 + qⁿ) = −Tr(Fⁿ|H¹) over F_q

**Relations (incoming):** [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1) (same mechanism as); [No étale H¹ for Spec ℤ](#no-etale-h1) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (same mechanism as); [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (same mechanism as); [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as)

### #4 · 0.720 · Primitive part V₀ = U^⊥ <a id="primitive-part"></a>

**Label:** Theorem · **id:** `primitive_part` · **quadrant:** RH-sharp

*In plain words:* What is left after removing the reference plane; on it the form should be negative (curves: theorem; ℚ: RH).

**Core.** D° = D − d₁f₂ − d₂f₁; (D°)² = −Tr_{H¹}(α_Dα_D†) (TAA Lemma 133). Over ℚ V₀ = U^⊥ and D·D ≤ 0 on V₀ ⇔ RH (TAA Lemma 91).

**Formula.** (D°)² = −def(D) ≤ 0

**Also known as:** V₀; primitive classes; D°

**Axes:** reference/pole/cusp, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 91, 125, 133, 142

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** A “−2Tr” formula holds only on the primitive part.

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — complement
- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst) — physical quotient

**Relations (incoming):** [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Relative Gram matrix G_rel](#relative-gram) (analogue of); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (fails for); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (same mechanism as)

### #19 · 0.579 · Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays) <a id="light-cone-u"></a>

**Label:** Theorem · **id:** `light_cone_U` · **quadrant:** true but ghost-blind/untested

*In plain words:* The two special directions (the trivial class 𝟙 and the Lefschetz/pole class 𝕃) span a plane with one positive and one negative direction; positivity is always measured relative to it.

**Core.** Over F_q: U = ⟨f₁, f₂⟩ ⊂ NS(C×C), signature (1,1), f₁, f₂ null; ample class lies in U; complement negative definite. Over ℚ: the pole/Tate plane spanned by 𝟙 and 𝕃 (poles at s = 0, 1), U^⊥ = V₀ (TAA Lemma 142).

**Formula.** U = ⟨𝟙, 𝕃⟩, sig U = (1,1), 𝟙² = 𝕃² = 0

**Also known as:** U; null rays; hyperbolic plane; light cone

**Axes:** reference/pole/cusp, structure/frame (Ax1), geometry over F_q

**TAA lemmas:** 14, 98, 115, 140, 142

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** "Light cone" includes its interior.

> ⚠ **Correction / caution.** The ample class lives in U; the surface is read relative to the points.

**Relations (outgoing):**

- same mechanism as → [Pole plane / Tate poles at s = 0, 1](#pole-plane) — same plane over ℚ
- lives in → [Hodge index theorem](#hodge-index) — the (1,1) part

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (lives in); [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (lives in); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (lives in); [Castelnuovo–Severi inequality](#castelnuovo-severi) (lives in); [Hasse bound as a positive degree form](#hasse-pythagoras) (analogue of); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (lives in); [Hodge index theorem](#hodge-index) (lives in); [Pole plane / Tate poles at s = 0, 1](#pole-plane) (same mechanism as)

### #32 · 0.540 · Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order) <a id="goldfeld-bsd"></a>

**Label:** Cited · **id:** `goldfeld_bsd` · **quadrant:** RH-sharp

*In plain words:* If the partial Euler product of L(E,s) at the centre behaves like C/(log x)^r, then L(E,s) satisfies RH and r is the analytic order of vanishing — with a surprising √2 in the constant.

**Core.** If ∏_{p≤x} L_p(E,1) ∼ C/(log x)^r then L(E,s) satisfies RH, r = ord_{s=1}L(E,s), C = L^{(r)}(E,1)/(r! √2 e^{rγ}) (Goldfeld 1982, cited via Conrad 2005; TAA Lemma 140).

**Formula.** ∏_{p≤x} L_p(E,1) ∼ C/(log x)^r, C = L^{(r)}(E,1)/(r!√2 e^{rγ})

**Numbers.** √2 factor

**Also known as:** Goldfeld 1982; Nagao–Mestre product; ∏ L_p(E,1)

**Axes:** reference/pole/cusp, ghost-sensitive

**TAA lemmas:** 140

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** It gives the analytic order, not the rank (rank = order is BSD).

> ⚠ **Correction / caution.** a_p are not BSD generators.

> ⚠ **Correction / caution.** Note the √2 factor (Conrad).

**Relations (outgoing):**

- implies → [Riemann hypothesis (target node)](#rh) — for L(E,s)
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — prime data vs the reference at s = 1
- analogue of → [Displaced reference (subtracting the pole)](#displaced-reference)

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (same mechanism as); [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (same mechanism as); [√2 family](#sqrt2-family) (corrects)

### #51 · 0.452 · Pole plane / Tate poles at s = 0, 1 <a id="pole-plane"></a>

**Label:** Theorem · **id:** `pole_plane` · **quadrant:** true but ghost-blind/untested

*In plain words:* The two poles of ξ(s) at s = 0 and 1 give the reference plane; subtracting them is what makes a form "relative".

**Core.** TAA Lemma 142: the relative Gram on translates uses the pole terms f̂(0), f̂(1) (zero-free entries). Pole of ζ at s = 1 is the 𝕃-ray; the functional equation pairs it with s = 0.

**Formula.** ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)

**Also known as:** Tate plane; 𝟙, 𝕃; pole terms

**Axes:** reference/pole/cusp

**TAA lemmas:** 142, 143, 144

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u)
- same mechanism as → [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1)

**Relations (incoming):** [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) (same mechanism as); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as)

### #66 · 0.377 · Displaced reference (subtracting the pole) <a id="displaced-reference"></a>

**Label:** Heuristic · **id:** `displaced_reference` · **quadrant:** background

*In plain words:* Arithmetic quantities are measured relative to a reference fixed by the pole; the "error" is the displacement from that reference.

**Core.** ψ − x, E₂* = E₂ − 3/(πy) and the relative Gram all subtract a pole/reference term. TAA Lemma 146 records this as an organizing analogy.

**Also known as:** reference subtraction

**Axes:** reference/pole/cusp, physics analogue

**TAA lemmas:** 146, 142

**Scores (Heuristic):** gap significance 0.5 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.377

> ⚠ **Correction / caution.** Analogy, not theorem.

**Relations (outgoing):**

- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)
- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly)
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram)
- analogue of → [Buoyancy / Archimedes principle](#archimedes) — buoyancy: weight relative to displaced fluid

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (analogue of); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as); [Buoyancy / Archimedes principle](#archimedes) (analogue of)

### #76 · 0.325 · √2 family <a id="sqrt2-family"></a>

**Label:** Theorem · **id:** `sqrt2_family` · **quadrant:** true but ghost-blind/untested

*In plain words:* Geodesic from 1 + √2; it is not singled out.

**Core.** TAA Lemma 146 §1: traces t_k = 6, 34, 198, 1154, 6726 (Pell), lengths kℓ₀, ℓ₀ = 4 log(1+√2) = 3.5255; length-ordered series is periodic (period 2πi/ℓ₀ = 1.7822i) ⇒ cannot carry ζ zeros; conductor-ordered = h⁺R(8)ζ(s−1)/L(s,χ₈). TAA Lemma 146, correction 2: √2 is not the first norm −1 unit (φ is smaller).

**Numbers.** traces 6, 34, 198, 1154, 6726 · ℓ₀ = 3.5255

**Also known as:** √2 geodesic; t = 6

**Axes:** reference/pole/cusp

**TAA lemmas:** 141, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** √2 is not the first norm −1 unit; the golden ratio is smaller (TAA Lemma 146).

**Relations (outgoing):**

- special case of → [Closed geodesics on the modular surface](#closed-geodesics)
- corrects → [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) — √2 in Goldfeld is unrelated

**Relations (incoming):** [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as)

### #77 · 0.325 · Pole of ζ at s = 1 (residue / 3/π) <a id="pole-s1"></a>

**Label:** Cited · **id:** `pole_s1` · **quadrant:** true but ghost-blind/untested

*In plain words:* ζ has a pole at s = 1; the Eisenstein series E(z,s) has its pole there with residue 3/π, the reciprocal of the area of the modular surface.

**Core.** Res_{s=1} E(z,s) = 3/π = 1/vol(SL₂(ℤ)∖ℍ); E₂* = E₂ − 3/(πy) is the non-holomorphic correction (TAA Lemma 144/TAA Lemma 145 context).

**Formula.** Res_{s=1}E(z,s) = 3/π

**Numbers.** 3/π

**Also known as:** s = 1 pole; residue 3/π; Eisenstein pole

**Axes:** reference/pole/cusp

**TAA lemmas:** 144, 145

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** The point 1 is not ∞.

**Relations (outgoing):**

- same mechanism as → [Displaced reference (subtracting the pole)](#displaced-reference)
- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) — 3/(πy) correction
- same mechanism as → [Pole plane / Tate poles at s = 0, 1](#pole-plane) — 𝕃-ray

**Relations (incoming):** [Pole plane / Tate poles at s = 0, 1](#pole-plane) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as)

### #79 · 0.325 · Closed geodesics on the modular surface <a id="closed-geodesics"></a>

**Label:** Theorem · **id:** `closed_geodesics` · **quadrant:** true but ghost-blind/untested

*In plain words:* Lengths 2 log ε_t from traces t; Selberg trace formula pairs them with resonances.

**Core.** Length 2 log ε_t with h⁺ classes (TAA Lemma 143); trace-6 has 3 primitive oriented classes (TAA Lemma 141); counts t = 3..11: 1,2,2,3,3,4,2,6,3. √2 geodesic ℓ = 3.5254943481, sinh(ℓ/2) = 2√2; golden geodesic 1.9248 is shortest. S(t) = Σ h⁺ log ε⁺², 36 discriminants 0 mismatches (TAA Lemma 143).

**Formula.** ℓ = 2 log ε_t

**Numbers.** 1.9248 (golden) · 3.5254943481 (√2) · counts 1,2,2,3,3,4,2,6,3

**Also known as:** primitive hyperbolic classes

**Axes:** reference/pole/cusp

**TAA lemmas:** 141, 143, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Selberg resonances](#selberg-resonances)

**Relations (incoming):** [√2 family](#sqrt2-family) (special case of)

### #81 · 0.325 · Selberg resonances <a id="selberg-resonances"></a>

**Label:** Theorem · **id:** `selberg_resonances` · **quadrant:** true but ghost-blind/untested

*In plain words:* Poles of φ(s) relate to ζ zeros at s = ρ/2.

**Core.** φ = Λ(2s−1)/Λ(2s) has poles in Re s < ½ exactly at ρ/2, φ(½) = −1 (TAA Lemma 143). ΣΛ(P)N^{−s} = Z′/Z(s) − Z′/Z(s+1). TAA Lemma 143: ρ/2 seen in the length spectrum from class numbers (projection on the predicted ζ term 1.003). Selberg zeros ρ/2: infinitely many off the line (TAA Lemma 141).

**Also known as:** scattering poles

**Axes:** reference/pole/cusp, phase/unitarity (Ax3)

**TAA lemmas:** 141, 143, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct)

**Relations (incoming):** [Closed geodesics on the modular surface](#closed-geodesics) (same mechanism as)

### #83 · 0.325 · Cusp ≠ archimedean place <a id="cusp-vs-infinity"></a>

**Label:** Theorem · **id:** `cusp_vs_infinity` · **quadrant:** true but ghost-blind/untested

*In plain words:* The cusp of the modular curve and the archimedean place of ℚ are different objects, though both get written ∞.

**Core.** The cusp is a point of the modular curve; the archimedean place is a valuation of ℚ. Neither is the frame bundle, and ∞-toposes are unrelated to the infinite place.

**Also known as:** cusp i∞; place ∞

**Axes:** reference/pole/cusp

**TAA lemmas:** 144, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Do not identify cusp, place ∞, frame bundle, ∞-topos.

**Relations (outgoing):**

- corrects → [Archimedean place and Γ_ℝ factor](#archimedean-place)

### #84 · 0.325 · Density / volume reading <a id="density-volume"></a>

**Label:** Theorem · **id:** `density_volume` · **quadrant:** true but ghost-blind/untested

*In plain words:* The modular surface’s volume form and the half-density: area π/3 gives degree 1/12, and the half-density y^½ is the Heaviside ½ — structure, not sign.

**Core.** TAA Lemma 141 §7: c₁(ω, Pet) = dxdy/(4πy²); area π/3 ⇒ deg ω = 1/12 = −ζ(−1); χ_orb = −1/6; half-density y^½ unitary L²(dr) → L²(dy/y²) = Heaviside ½. TAA Lemma 145: the U-form is indefinite, not a volume (TAA Lemma 145 corrections); volume formula for h⁰ is heuristic.

**Formula.** deg ω = 1/12 = −ζ(−1)

**Numbers.** area π/3 · χ_orb = −1/6

**Also known as:** volume form

**Axes:** reference/pole/cusp, physics analogue

**TAA lemmas:** 141, 145

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Volume form ≠ Levi-Civita connection (TAA Lemma 141 list).

**Relations (outgoing):**

- same mechanism as → [Mass-density positivity](#mass-density)

### #96 · 0.307 · E₂ anomaly (E₂* = E₂ − 3/(πy)) <a id="e2-anomaly"></a>

**Label:** Theorem · **id:** `e2_anomaly` · **quadrant:** true but ghost-blind/untested

*In plain words:* E₂ fails to be modular; fixing it costs a non-holomorphic term 3/(πy) tied to the pole. One reading treats the failure as a 2-class.

**Core.** E₂(−1/z) = z²E₂(z) + 12z/(2πi)… corrected by E₂* = E₂ − 3/(πy), modular of weight 2. Ghost-blind (phase/automorphy data).

**Formula.** E₂* = E₂ − 3/(πy)

**Numbers.** 3/π

**Also known as:** quasimodular E₂; 2-class; modular anomaly

**Axes:** reference/pole/cusp, ghost-blind, phase/unitarity (Ax3)

**TAA lemmas:** 144, 145, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 0.8 → priority 0.307

> ❓ **Not verified / open.** Exact transformation constant quoted from standard theory; the 2-class reading is conjectural.

**Relations (outgoing):**

- same mechanism as → [Displaced reference (subtracting the pole)](#displaced-reference)
- same mechanism as → [Automorphy defect (TAA Lemma 144)](#automorphy-defect) — defect of a cocycle
- same mechanism as → [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1)

**Relations (incoming):** [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as); [Automorphy defect (TAA Lemma 144)](#automorphy-defect) (same mechanism as); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as); [Weight ladder (modular weights)](#weight-ladder) (same mechanism as)

### #98 · 0.307 · Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k <a id="herbrand-ribet"></a>

**Label:** Cited · **id:** `herbrand_ribet` · **quadrant:** true but ghost-blind/untested

*In plain words:* The p-part of the class group of ℚ(μ_p) splits into pieces labelled by powers of the Teichmüller character ω. The piece ω¹⁻ᵏ is nonzero exactly when p divides the Bernoulli number B_k; for p = 691, k = 12 this is the ω⁻¹¹ piece.

**Core.** For odd p and even k, 2 ≤ k ≤ p−3: A(ω¹⁻ᵏ) ≠ 0 ⇔ p | B_k (Herbrand 1932 ⇒, Ribet 1976 ⇐). p = 691, k = 12: B₁₂ = −691/2730, class in ω⁻¹¹ = ωᵖ⁻¹² (same character, since ω has order p − 1); odd character ⇒ minus part. TAA Lemma 66: 691 has two irregular indices (12, 200), so Cl/691 is 2-dim (ω⁻¹¹, ω⁻¹⁹⁹); ρ_{Δ,691} ss = 1 ⊕ ω¹¹, the non-split extension gives the ω⁻¹¹ class via CFT (Greenberg–Monsky lattices).

**Formula.** A(ω¹⁻ᵏ) ≠ 0 ⇔ p | B_k

**Numbers.** B₁₂ = −691/2730 · irregular indices of 691: 12, 200 · v₆₉₁(h⁻) = 2

**Also known as:** Teichmüller eigenspace; ω⁻¹¹ class; χ¹¹-minus class; 691 class; Kummer criterion refined

**Axes:** reference/pole/cusp, ghost-blind

**TAA lemmas:** 60, 66

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Notation: det ρ_Δ = χ_cyc¹¹ (cyclotomic character), whose reduction mod 691 is ω¹¹; the class itself sits in ω⁻¹¹ (TAA Lemma 66).

> ⚠ **Correction / caution.** Ribet 1976 used weight-2 forms on Γ₁(p), not Δ.

> ⚠ **Correction / caution.** Some authors write ωᵖ⁻¹²; it is the same eigenspace.

**Relations (outgoing):**

- implies → [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) — via Ribet’s Eisenstein congruence
- special case of → [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) — size statement implied by the main conjecture
- fails for → [Riemann hypothesis (target node)](#rh) — sizes, not signs: ghost-blind residual data (TAA Lemma 66)

**Relations (incoming):** [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (special case of); [Two different χ’s: Euler characteristic vs class-group character](#two-chis) (analogue of)

### #99 · 0.307 · Mazur–Wiles main conjecture ("Euler characteristic = L-value") <a id="mazur-wiles"></a>

**Label:** Cited · **id:** `mazur_wiles` · **quadrant:** true but ghost-blind/untested

*In plain words:* The size of each Teichmüller piece of the class group (and of the Iwasawa module up the cyclotomic tower) equals the p-part of an L-value; slogan: an algebraic Euler characteristic equals an analytic L-value.

**Core.** Mazur–Wiles 1984: characteristic ideal of the χ-part of the Iwasawa module = ideal of the Kubota–Leopoldt p-adic L-function. Finite-level consequence: #A(ω¹⁻ᵏ) = p-part of L(0, ωᵏ⁻¹) (Ribet, Berkeley slides). TAA Lemma 66: main conjecture = Hilbert–Pólya-type with free p-adic unitarity (γ eigenvalues are 1-units); μ = 0 is not a positivity; no positivity found on the Iwasawa side (OPEN).

**Formula.** char(X_∞^χ) = (L_p(χ))

**Also known as:** Iwasawa main conjecture; char ideal = p-adic L-function; Kubota–Leopoldt

**Axes:** reference/pole/cusp, ghost-blind, physics analogue

**TAA lemmas:** 4, 66

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Iwasawa theory measures sizes (orders, characteristic ideals), never the sign of D²; it cannot by itself give Weil positivity.

> ⚠ **Correction / caution.** "Euler characteristic = L-value" is a slogan (Heuristic wording), the theorem is the equality of ideals.

**Relations (outgoing):**

- analogue of → [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) — "χ = value" shape only
- analogue of → [Hilbert–Pólya](#hilbert-polya) — TAA Lemma 66: Hilbert–Pólya-type, p-adic

**Relations (incoming):** [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) (analogue of); [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (special case of); [Two different χ’s: Euler characteristic vs class-group character](#two-chis) (analogue of)

### #100 · 0.307 · Archimedean place and Γ_ℝ factor <a id="archimedean-place"></a>

**Label:** Theorem · **id:** `archimedean_place` · **quadrant:** true but ghost-blind/untested

*In plain words:* The "prime at infinity": its Gamma factor contributes a term to the Weil form that can be positive or negative depending on the window.

**Core.** Γ_ℝ contributes the arch functional to W; arch-only positivity holds on thresholds a* (TAA Lemma 127), ghost-blind.

**Formula.** Γ_ℝ(s) = π^{−s/2}Γ(s/2)

**Also known as:** Γ_ℝ(s) = π^{−s/2}Γ(s/2); place ∞; arch term

**Axes:** reference/pole/cusp, ghost-blind

**TAA lemmas:** 98, 121, 127

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** ∞ is not the frame bundle.

**Relations (outgoing):**

- same mechanism as → [Archimedean thresholds a*](#arch-threshold)
- lives in → [Weil positivity criterion](#weil-positivity)

**Relations (incoming):** [Cusp ≠ archimedean place](#cusp-vs-infinity) (corrects); [Archimedean thresholds a*](#arch-threshold) (special case of)

### #102 · 0.307 · Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂) <a id="ramanujan-691"></a>

**Label:** Cited · **id:** `ramanujan_691` · **quadrant:** true but ghost-blind/untested

*In plain words:* The cusp form Δ agrees with the Eisenstein series E₁₂ modulo 691, because 691 divides the numerator of ζ(−11). It is the meeting point of the Eisenstein (reference) and cusp-form (primitive) parts of the Hecke algebra.

**Core.** τ(n) ≡ σ₁₁(n) mod 691; ζ(−11) = −B₁₂/12 = 691/32760 (constant term of E₁₂ ∝ ζ(−11)/2 = 691/65520, TAA Lemma 70). TAA Lemma 66: τ(p) ≡ 1 + p¹¹ mod 691 for all 9592 p < 10⁵; Hecke congruence moduli N_k = |num(B_k/2k)| = 691, 3617, 43867, … (k = 12, 16, 18, …); bridge = closed point where Eisenstein and cuspidal components of Spec 𝕋 meet. TAA Lemma 70 (Mazur77 at source): Eisenstein ideal 𝕋/𝔍 ≅ ℤ/n, modulus = numerator of an Euler-depleted ζ(1−k); cusp encodes it as a negative zeta value; positivity invisible (timelike f ≡ spacelike E).

**Formula.** τ(n) ≡ σ₁₁(n) mod 691, ζ(−11) = 691/32760

**Numbers.** 9592 primes checked (TAA Lemma 66) · 691/65520 = ζ(−11)/2

**Also known as:** 691 congruence; Δ ≡ E₁₂ mod 691; ζ(−11) = 691/32760; Eisenstein ideal at level 1

**Axes:** reference/pole/cusp, ghost-blind

**TAA lemmas:** 66, 70

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** The congruence is mod 691 data: it says nothing about the sign of the Weil form (TAA Lemma 66: bridge = where positivity is lost).

> ⚠ **Correction / caution.** E₁₂ has all its zeros off Re s = 6 (unconditional, TAA Lemma 66) — an "all ghost" Euler product.

**Relations (outgoing):**

- lives in → [Weight ladder (modular weights)](#weight-ladder) — weight-12 rung: E₁₂ reference vs Δ primitive
- same mechanism as → [Primitive part V₀ = U^⊥](#primitive-part) — Eisenstein = reference, cusp form = primitive split
- special case of → [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) — the k = 12, p = 691 case

**Relations (incoming):** [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (implies)

### #117 · 0.267 · Weight ladder (modular weights) <a id="weight-ladder"></a>

**Label:** Theorem · **id:** `weight_ladder` · **quadrant:** true but ghost-blind/untested

*In plain words:* Modular forms come in weights; at each rung the Eisenstein series E_k is the reference. A “stratification” of modular structures is this ladder.

**Core.** TAA Lemma 146 corrections: stratification = weight ladder, with E_k the reference per rung; cusp positivity on each rung is ghost-blind. TAA Lemma 139 weight-1 search: weight-1 modular = motivic weight 0 (η(z)η(23z), |α| = 1); motivic weight 1 = weight-2 cusp forms (11a, Rosati PD); ζ appears only in Eisenstein lines (ζ_K weight 1, ζ(s)ζ(s−1) weight 2), not in L².

**Also known as:** weight k ladder

**Axes:** reference/pole/cusp, ghost-blind

**TAA lemmas:** 146, 139

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly)
- same mechanism as → [Cusp forms & Petersson positivity](#cusp-forms-petersson) — cusp positivity per rung is ghost-blind

**Relations (incoming):** [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (lives in)

## Axis: physics analogue <a id="axis-physics-analogue"></a>

### #16 · 0.600 · Passivity (positive real part) <a id="passivity"></a>

**Label:** Restatement · **id:** `passivity` · **quadrant:** RH-sharp

*In plain words:* A system that never produces energy; its impedance has non-negative real part. For ξ′/ξ this is Lagarias’ criterion.

**Core.** Passivity ⇔ Re ξ′/ξ > 0 on Re s > ½ ⇔ RH (Lagarias/Hinkkanen). Passivity ⇒ causality (TAA Lemma 146, correction 3).

**Formula.** Re ξ′/ξ(s) > 0 for Re s > ½

**Also known as:** Re Z ≥ 0; positive-real function

**Axes:** physics analogue, sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 17, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Not independent of causality.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias)
- implies → [Kramers–Kronig relations](#kramers-kronig) — causal

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (same mechanism as); [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (same mechanism as); [de Branges spaces](#de-branges) (same mechanism as); [Suzuki’s de Branges line from the prime side](#suzuki-line) (same mechanism as); [Bagchi recurrence](#bagchi) (analogue of); [Gain lines (active media)](#gain-line) (fails for); [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Kramers–Kronig relations](#kramers-kronig) (same mechanism as)

### #33 · 0.540 · Decay rate ¼ <a id="decay-quarter"></a>

**Label:** Theorem · **id:** `decay_quarter` · **quadrant:** RH-sharp

*In plain words:* Every scattering resonance of the modular surface decays at rate ¼ exactly when its ζ-zero is on the line; an off-line zero decays at (1−β)/2 instead.

**Core.** TAA Lemma 118 Thm 3.1: ‖Z″‖ ≤ 1 unconditionally, poles at ρ/2 symmetric about ¼, rate (1−β)/2; RH ⇔ all rates ¼ [R]. TAA Lemma 120: spectral rate ¼, not uniform. TAA Lemma 143 SC-A (L + unitarity ⇒ κ ≡ ¼) ⇔ RH; ringing rate 0.24996 vs predicted ¼. TAA Lemma 144: μ = ¼ for every ρ (FE), ghost and DH ring at 0.0957414 = (1−β)/2.

**Formula.** rate = (1 − β)/2; RH ⇔ all rates = ¼

**Numbers.** 0.24996 (pred ¼) · 0.0957414 ghost/DH

**Also known as:** spectral gap ¼

**Axes:** physics analogue, reference/pole/cusp, ghost-sensitive

**TAA lemmas:** 118, 120, 141, 143, 144

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** The circular line for the modular surface is Re s = ¼, not ½ (TAA Lemma 143 corrections); rate = (1−β)/2, not Re ρ/2 (TAA Lemma 143 corrections).

> ⚠ **Correction / caution.** No essential spectral gap for the modular surface (Bourgain–Dyatlov 1612.09040).

**Relations (outgoing):**

- special case of → [Lax–Phillips scattering](#lax-phillips)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — RH ⇔ all rates ¼ (TAA Lemma 118)
- same mechanism as → [Heaviside RLGC line](#heaviside) — critically damped modes (TAA Lemma 144)

**Relations (incoming):** [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #45 · 0.532 · Gain lines (active media) <a id="gain-line"></a>

**Label:** Analogy · **id:** `gain_line` · **quadrant:** sharp but interpretive

*In plain words:* A ghost acts like a gain line: negative absorption.

**Core.** TAA Lemma 146 §2: Re ξ′/ξ = Σ(σ−β)/((σ−β)² + (t−γ)²) — each zero is an absorption line to its right; an off-line zero gives a gain line. Grid σ ∈ [.505,1.1], t ∈ [80,92]: ξ min +0.00467; DH −66.84 at (0.794, 85.70), 1.89% negative; TAA Lemma 144 ghost −66.97 (1.94%). Lorentz model: dRe χ/dω −6 (absorber) / +6 (gain).

**Numbers.** ξ min +0.00467 · DH −66.84 (1.89% negative) · ghost −66.97 (1.94%)

**Also known as:** negative absorption

**Axes:** physics analogue, ghost-sensitive

**TAA lemmas:** 36, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.532

**Relations (outgoing):**

- analogue of → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)
- fails for → [Passivity (positive real part)](#passivity)

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (fails for); [Time delay (Wigner)](#time-delay) (same mechanism as); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #48 · 0.452 · Lax–Phillips scattering <a id="lax-phillips"></a>

**Label:** Cited · **id:** `lax_phillips` · **quadrant:** true but ghost-blind/untested

*In plain words:* Scattering theory for waves on the modular surface; resonances relate to zeros.

**Core.** LP80 (read at source, TAA Lemma 118/TAA Lemma 141): s(z) = Λ(2s−1)/Λ(2s), Res_{s=1} = 3/π, poles at zeros of ζ(1+2iz), RH ⇒ Im z = ¼; Pavlov–Faddeev "RH iff Z″ decays exponentially"; spectrum of B″ = {(κ−1)/2}; "all that is missing is an appropriate inner product". TAA Lemma 118 Thm 3.1: ‖Z″‖ ≤ 1 unconditionally.

**Numbers.** Res = 3/π · Im z = ¼

**Also known as:** LP scattering

**Axes:** physics analogue, phase/unitarity (Ax3)

**TAA lemmas:** 118, 141, 143

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** LP (6.19) rate sign ambiguous in OCR (TAA Lemma 118, correction 7).

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi)
- same mechanism as → [Decay rate ¼](#decay-quarter)
- same mechanism as → [Passivity (positive real part)](#passivity) — passive arrow (TAA Lemma 118)

**Relations (incoming):** [Decay rate ¼](#decay-quarter) (special case of); [Hilbert–Pólya](#hilbert-polya) (same mechanism as); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of)

### #56 · 0.423 · BRST / Gupta–Bleuler physical quotient <a id="brst"></a>

**Label:** Analogy · **id:** `brst` · **quadrant:** background

*In plain words:* Remove null and negative-norm states to get a positive physical space — as U^⊥ in Hodge index.

**Core.** TAA Lemma 115: BRST structure exact over F_q and ℚ [T]; "no ghosts" ⇔ RH [R]; missing positive V ≅ H¹ (Hilbert–Pólya) ⇒ restatement. TAA Lemma 146 §3: Gupta–Bleuler F₁^⊥/F₁ ≅ U^⊥; the BRST quartet decouples but the ghost quartet survives. PM-3 (BRST complex with H(Q) = U^⊥) open.

**Also known as:** ghost subtraction; PM-3

**Axes:** physics analogue, reference/pole/cusp

**TAA lemmas:** 115, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.4 → priority 0.423

> ⚠ **Correction / caution.** PM-3 is open.

> ❓ **Not verified / open.** PM-3 open.

**Relations (outgoing):**

- same mechanism as → [Hodge index theorem](#hodge-index)
- same mechanism as → [Primitive part V₀ = U^⊥](#primitive-part)

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (same mechanism as); [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Hodge index theorem](#hodge-index) (same mechanism as); [Gribov ambiguity](#gribov) (analogue of)

### #63 · 0.392 · Källén–Lehmann spectral positivity <a id="kallen-lehmann"></a>

**Label:** Analogy · **id:** `kallen_lehmann` · **quadrant:** sharp but interpretive

*In plain words:* Physical theories have non-negative spectral weight; ζ analogue is the sign of zero weights.

**Core.** TAA Lemma 146 §3: Källén–Lehmann / R(s) positivity is an Ax2 statement (spectral weight ≥ 0; CMT05, WP20 6931(40)e−11). TAA Lemma 146 corrections: KL positivity needs a positive metric — exactly what is missing for ζ.

**Formula.** ρ(μ²) ≥ 0

**Also known as:** spectral density ρ ≥ 0

**Axes:** physics analogue, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.392

> ⚠ **Correction / caution.** KL needs a positive metric (TAA Lemma 146 corrections).

**Relations (outgoing):**

- same mechanism as → [Weil positivity criterion](#weil-positivity)

**Relations (incoming):** [Gribov ambiguity](#gribov) (fails for)

### #64 · 0.392 · Time delay (Wigner) <a id="time-delay"></a>

**Label:** Analogy · **id:** `time_delay` · **quadrant:** sharp but interpretive

*In plain words:* How long a wave packet lingers in the cusp; unlike the winding of the phase, the time-delay peak does see ghosts.

**Core.** TAA Lemma 143: winding ½ per zero for all β (ghost-blind), but time-delay peak at r = 42.85 is 3.09 (ζ), 27.22 (ζ + TAA Lemma 103 ghost), 27.42 (DH): ghost-sensitive. ζ time delay is negative for r ≲ 2.9 (min −3.87), so "positive delay" fails for ζ. TAA Lemma 120: dwell time ∂_x log|Φ| = −θ′(ω). TAA Lemma 118: Connes harmonic measure of an off-line zero = (1/2π) × TAA Lemma 117 excess group delay.

**Numbers.** 3.09 / 27.22 / 27.42 at r = 42.85 · min −3.87

**Also known as:** phase derivative

**Axes:** physics analogue, ghost-sensitive, numerics/certificate

**TAA lemmas:** 117, 118, 120, 143

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.392

> ⚠ **Correction / caution.** Positive time delay fails for ζ (TAA Lemma 143 corrections).

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi)
- same mechanism as → [Gain lines (active media)](#gain-line) — ghost = extra delay

### #92 · 0.324 · Kramers–Kronig relations <a id="kramers-kronig"></a>

**Label:** Analogy · **id:** `kramers_kronig` · **quadrant:** background

*In plain words:* Causal response: real (dispersive) and imaginary (absorptive) parts determine each other. Absorption’s sign is the passivity condition.

**Core.** TAA Lemma 146: dispersion = phase (ghost-blind), absorption sign = passivity ⇔ Lagarias ⇔ RH.

**Also known as:** KK; dispersion relation

**Axes:** physics analogue, phase/unitarity (Ax3), sign/positivity (Ax2)

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.324

> ⚠ **Correction / caution.** Passivity implies causality, not conversely (TAA Lemma 146).

**Relations (outgoing):**

- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive)
- same mechanism as → [Passivity (positive real part)](#passivity)

**Relations (incoming):** [Passivity (positive real part)](#passivity) (implies); [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) (same mechanism as); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #93 · 0.324 · Gribov ambiguity <a id="gribov"></a>

**Label:** Analogy · **id:** `gribov` · **quadrant:** background

*In plain words:* In QCD the gluon propagator violates positivity (it changes sign in Euclidean time) — the physics example of a "spectral weight" that is not positive.

**Core.** TAA Lemma 146 §3: Gribov C(t) re-derived to 1e−16, first sign change t* = π/(2√2 M) = 1.1107 (in units of M). Interpretation as positivity violation is interpretive (TAA Lemma 146 corrections).

**Formula.** t* = π/(2√2 M)

**Numbers.** t* = 1.1107 · re-derived to 1e−16

**Also known as:** gauge-fixing failure

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.324

> ⚠ **Correction / caution.** Gluon positivity violation as confinement evidence is interpretive (TAA Lemma 146 corrections).

**Relations (outgoing):**

- analogue of → [BRST / Gupta–Bleuler physical quotient](#brst)
- fails for → [Källén–Lehmann spectral positivity](#kallen-lehmann) — spectral positivity violated

### #121 · 0.267 · Bost–Connes KMS states <a id="kms-bost-connes"></a>

**Label:** Cited · **id:** `kms_bost_connes` · **quadrant:** true but ghost-blind/untested

*In plain words:* A quantum statistical system whose partition function is ζ(β); its positive KMS states and phase transition at β = 1 see ζ only at real β > 1, never the zeros.

**Core.** BC95 (Thm 5; CM08 3.32): Q-structure, Gal(Q^cycl/Q) symmetry, positive KMS states, ζ(β) real for β > 1; no trace equal to the Weil distribution found (TAA Lemma 30). TAA Lemma 38: strongest rigorous bridge; BC time is dual to rapidity, (β,t) = (Re s, −Im s); BC ordered phase ⇔ ω > ½. TAA Lemma 39: BC = tensor product over primes twisted by Galois. TAA Lemma 54/TAA Lemma 118: KMS/passivity uses ζ at real β > 1 ⇒ ghost-blind.

**Also known as:** BC system

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 30, 38, 39, 54, 118

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** BC95 Thm 5(a) states β < 1 (β ≤ 1 from CM08 3.32) (TAA Lemma 38 flag).

**Relations (outgoing):**

- analogue of → [Connes trace formula](#connes-trace)

### #124 · 0.226 · Buoyancy / Archimedes principle <a id="archimedes"></a>

**Label:** Analogy · **id:** `archimedes` · **quadrant:** background

*In plain words:* Weight is measured relative to the fluid displaced; Castelnuovo–Severi and the pole subtraction can be read the same way.

**Core.** TAA Lemma 146 §7: C–S as D² = 2ab + D′² — Archimedes relative to U; the sign is an input (fluids), proved (curves), ⇔ RH (ζ). Buoyancy sign as input: TAA Lemma 146 corrections.

**Also known as:** buoyancy; displaced fluid

**Axes:** physics analogue, reference/pole/cusp

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

> ⚠ **Correction / caution.** Analogy, not a mechanism.

**Relations (outgoing):**

- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- analogue of → [Displaced reference (subtracting the pole)](#displaced-reference)

**Relations (incoming):** [Castelnuovo–Severi inequality](#castelnuovo-severi) (analogue of); [Displaced reference (subtracting the pole)](#displaced-reference) (analogue of); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #125 · 0.226 · Heaviside RLGC line <a id="heaviside"></a>

**Label:** Analogy · **id:** `heaviside` · **quadrant:** background

*In plain words:* Transmission line with resistance, inductance, conductance, capacitance; used as a model for β.

**Core.** TAA Lemma 25: {R/L, G/C} = {β, 1 − β} in τ, orientation conventional (Prop 3.3); TAA Lemma 143 R/2L ↔ β/2; TAA Lemma 144 unordered {(1−β)/2, β/2} in u.

**Also known as:** telegrapher; RLGC

**Axes:** physics analogue

**TAA lemmas:** 25, 143, 144

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.4 → priority 0.226

> ⚠ **Correction / caution.** The R/L, G/C ordering is a convention and differs between TAA Lemmas 25, 143 and 144.

> ❓ **Not verified / open.** R/L vs G/C ordering conventional.

**Relations (outgoing):**

- same mechanism as → [Distortionless line R/L = G/C](#distortionless)

**Relations (incoming):** [Decay rate ¼](#decay-quarter) (same mechanism as); [Distortionless line R/L = G/C](#distortionless) (special case of)

### #126 · 0.226 · Mass-density positivity <a id="mass-density"></a>

**Label:** Analogy · **id:** `mass_density` · **quadrant:** background

*In plain words:* Single positive quantity (like mass) as model for Rosati.

**Core.** TAA Lemma 146 §7: N² = −(g/ρ)ρ′ (buoyancy frequency); the sign of the density gradient is an input for fluids, proved for curves, ⇔ RH for ζ.

**Also known as:** positive mass

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.4 → priority 0.226

> ❓ **Not verified / open.** Analogy only.

**Relations (outgoing):**

- analogue of → [Rosati positivity](#rosati)

**Relations (incoming):** [Rosati positivity](#rosati) (analogue of); [Density / volume reading](#density-volume) (same mechanism as)

### #127 · 0.226 · Distortionless line R/L = G/C <a id="distortionless"></a>

**Label:** Analogy · **id:** `distortionless` · **quadrant:** background

*In plain words:* Line that transmits without distortion; corresponds to β = ½.

**Core.** TAA Lemma 25/TAA Lemma 143: distortionless ⇔ β = ½.

**Formula.** R/L = G/C

**Also known as:** Heaviside condition

**Axes:** physics analogue, phase/unitarity (Ax3)

**TAA lemmas:** 25, 143

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- special case of → [Heaviside RLGC line](#heaviside)

**Relations (incoming):** [Heaviside RLGC line](#heaviside) (same mechanism as)

### #128 · 0.212 · Anomalous dispersion <a id="anomalous-dispersion"></a>

**Label:** Analogy · **id:** `anomalous_dispersion` · **quadrant:** background

*In plain words:* Phase behavior near a line; ghost-blind.

**Core.** TAA Lemma 36: anomalous dispersion = analogy — gain lines are where absorption and phase disagree; THM 4.3 absorption–phase sum rule ∫₀ᵀ Re ξ′/ξ(σ₀+it)dt = π[N(T) − 2N(σ₀,T)] + …, deficit 2πN(σ₀,T) ≥ 0 (leads to zero density, not a proof). TAA Lemma 78: causality versus linewidth, Kramers–Kronig for the modular scattering matrix. TAA Lemma 146: dRe χ/dω at centre −6 (absorber) vs +6 (gain).

**Also known as:** dispersion near resonance

**Axes:** physics analogue, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 36, 78, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

**Relations (outgoing):**

- same mechanism as → [Kramers–Kronig relations](#kramers-kronig)
- same mechanism as → [Gain lines (active media)](#gain-line)

### #129 · 0.181 · Lamb cutoff <a id="lamb-cutoff"></a>

**Label:** Analogy · **id:** `lamb_cutoff` · **quadrant:** background

*In plain words:* In a stratified fluid, waves below the Lamb cutoff frequency c/2H cannot propagate; on the modular surface the cusp’s −¼ is exactly this cutoff with scale height H = 1.

**Core.** TAA Lemma 146 §7: with dy/y² = e^{−r}dr, the cusp −¼ equals the Lamb cutoff c/2H with H = 1 (exact operator identity); TAA Lemma 141 §6: the cusp is a Webster horn A = e^{−r}, Liouville factor e^{r/2}, and +¼ cancels the horn cutoff. Same −¼ as y²∂²(y^½W) = y^½(W″ − W/4) (TAA Lemma 145).

**Formula.** y²∂²(y^½W) = y^½(W″ − W/4)

**Also known as:** Lamb

**Axes:** physics analogue, reference/pole/cusp, ghost-blind

**TAA lemmas:** 141, 145, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.181

> ⚠ **Correction / caution.** Lamb’s original source not opened (TAA Lemma 146 refs); the identity is checked as an operator identity.

**Relations (outgoing):**

- same mechanism as → [Half-density normalization |x|^{½}](#half-density)
- same mechanism as → [Buoyancy / Archimedes principle](#archimedes) — same stratified-fluid picture
- same mechanism as → [Decay rate ¼](#decay-quarter) — the same ¼

**Relations (incoming):** [Half-density normalization |x|^{½}](#half-density) (same mechanism as)

## Axis: Spec ℤ gap <a id="axis-spec-gap"></a>

### #21 · 0.579 · Surface + ample + RR ⇒ Hodge index (D8) <a id="surface-ample-rr"></a>

**Label:** Theorem · **id:** `surface_ample_rr` · **quadrant:** true but ghost-blind/untested

*In plain words:* The curve proof needs a surface, an ample class and Riemann–Roch.

**Core.** D8 (TAA Lemma 140): surface + ample + RR ⇒ Hodge index. TAA Lemma 145 V3: classical S1 quadratic RR, S2 Serre, S3 h¹ ≥ 0, S4 sections ⇒ effective, S5 ample·eff > 0; the missing Spec ℤ step is quadratic S1 + S4. TAA Lemma 147: CC18 calls exactly this "the key missing step".

**Also known as:** D8

**Axes:** Spec ℤ gap, geometry over F_q

**TAA lemmas:** 140, 145, 147

**Scores (Heuristic):** gap significance 0.8 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** Needs S2, S3, S5 too (TAA Lemma 145).

**Relations (outgoing):**

- implies → [Hodge index theorem](#hodge-index)

**Relations (incoming):** [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (same mechanism as); [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) (same mechanism as); [Products grow linearly (2n), not quadratically](#products-linear) (fails for); [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) (same mechanism as); [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) (analogue of)

### #22 · 0.579 · Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U) <a id="laurent-square"></a>

**Label:** Theorem · **id:** `laurent_square` · **quadrant:** true but ghost-blind/untested

*In plain words:* The tensor square of ℤ over the sphere spectrum is bigger than ℤ and has a Laurent-polynomial piece; its sections grow quadratically, but the quadratic term is only the U-form, so it is vacuous on the degree-0 divisors that matter for RH.

**Core.** CC16 Prop 7.4: HZ ∧ HZ ≇ HZ, assembly onto ℤ[t^±]^{⊗k}/ℤ. TAA Lemma 147 Laurent model (t-degree ≤ nβ, coefficient ≤ 2^{nα}): box count 2n² + 4n exact; ℓ² ball counts = volume to 4.8e−6 (n = 10), log₂ # = 2n² − n log₂ n + O(n); coefficient 2αβ is the U-form ⇒ vacuous on degree-0 D(f) (Thm vac). Needed: NS ⊋ U containing Ψ_λ with #H⁰(±nD(f)) ≥ 2^{n² s(f,f)/2}.

**Formula.** log₂ # = 2n² − n log₂ n + O(n); quadratic coefficient 2αβ = U-form

**Numbers.** box 2n² + 4n · 4.8e−6 at n = 10

**Also known as:** HZ∧HZ; Laurent assembly ℤ[t^±]/ℤ; Thm vac; CC-1/CC-3 object

**Axes:** Spec ℤ gap, reference/pole/cusp, open target

**TAA lemmas:** 147

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** Quadratic growth here comes only from U, so it says nothing about the primitive part V₀ (Thm vac).

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — quadratic term = U-form only
- fails for → [Primitive part V₀ = U^⊥](#primitive-part) — vacuous on degree 0
- special case of → [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) — candidate H⁰ of the square

**Relations (incoming):** [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (same mechanism as)

### #23 · 0.579 · Parity argument: linear χ cannot see D² <a id="parity-linear-chi"></a>

**Label:** Theorem · **id:** `parity_linear_chi` · **quadrant:** true but ghost-blind/untested

*In plain words:* A Riemann–Roch whose Euler characteristic is linear (odd) in D can prove "positive degree ⇒ sections" but never contains D²; a quadratic (even) χ is needed for Hodge index.

**Core.** TAA Lemma 145: quadratic χ is even in D, linear χ odd ⇒ fixed rank only proves degree c(D) = 0, never sees D². TAA Lemma 147: for CC23, χ(D) + χ(−D) = 2 for deg₂D ∉ ℤ (even part constant 2χ(𝒪), odd part ⌈deg₂D⌉′); χ(D) + χ(K−D) = 0 except −1 on deg₂ ∈ (−2,0) (observation).

**Formula.** χ(D) + χ(−D) = 2

**Also known as:** TAA Lemma 145 parity; even/odd χ; χ(D)+χ(−D) = 2

**Axes:** Spec ℤ gap, structure/frame (Ax1)

**TAA lemmas:** 145, 147

**Scores (Heuristic):** gap significance 0.8 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** χ-symmetry is an observation, not a CC claim (TAA Lemma 147 s2).

**Relations (outgoing):**

- fails for → [Hodge index theorem](#hodge-index) — cannot reach the D² step
- same mechanism as → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch)

**Relations (incoming):** [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) (same mechanism as); [Products grow linearly (2n), not quadratically](#products-linear) (same mechanism as); [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) (same mechanism as)

### #24 · 0.579 · Tautology boundary (zero side vs prime side) <a id="tautology-boundary"></a>

**Label:** Theorem · **id:** `tautology_boundary` · **quadrant:** true but ghost-blind/untested

*In plain words:* Checking positivity using the zeros themselves is circular; a real test must use only primes, the pole and the archimedean place.

**Core.** TAA Lemma 142: all entries of the relative Gram are zero-free (flow, U/Tate poles, Γ_ℝ, Λ(n)); sign = RH (Weil); the zero-side check is the tautology. Unconditional sign only on windows ≤ log 3 (TAA Lemma 10) and arch-only a* (TAA Lemma 127), both ghost-blind.

**Also known as:** circularity; zero-free entries

**Axes:** Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 142, 106, 109, 137

**Scores (Heuristic):** gap significance 0.8 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** "Without zero locations" is vacuous in finite models (Newton identities, TAA Lemma 109).

**Relations (outgoing):**

- same mechanism as → [Weil positivity criterion](#weil-positivity) — zero side = restatement
- fails for → [Certified positivity windows](#certified-windows) — certificates are below ghost thresholds

**Relations (incoming):** [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as)

### #25 · 0.579 · Deninger’s foliated program <a id="deninger"></a>

**Label:** Cited · **id:** `deninger` · **quadrant:** true but ghost-blind/untested

*In plain words:* Deninger’s program: a foliated dynamical space whose leafwise cohomology carries the zeros; a positive Hodge star plus the flow would force Θ = ½ + (skew part).

**Core.** TAA Lemma 4: foliation-like (Deninger) structure carries the explicit formula with its signs; contact-like (Reeb) gives only the analytic shadow; on closed M, Reeb flows and Deninger systems are mutually exclusive. TAA Lemma 28: zeros = leafwise zero modes [analogy/conjectural]. TAA Lemma 50 Prop 7.1 (Den98): positive J commuting with Θ ⇒ Θ − ½ skew [RESTATEMENT]. TAA Lemma 93: Deninger D1–D5 stated exactly. TAA Lemma 141 §2: level S3 of the "surface" target.

**Formula.** Θ = ½ + A, A skew

**Also known as:** foliation

**Axes:** Spec ℤ gap, open target, physics analogue

**TAA lemmas:** 4, 28, 50, 93, 141

**Scores (Heuristic):** gap significance 0.8 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)

**Relations (incoming):** [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1) (same mechanism as)

### #26 · 0.579 · No étale H¹ for Spec ℤ <a id="no-etale-h1"></a>

**Label:** Theorem · **id:** `no_etale_h1` · **quadrant:** true but ghost-blind/untested

*In plain words:* Spec ℤ is simply connected; the "H¹" must be relative to the flow (ψ − x ≠ 0).

**Core.** TAA Lemma 140: π₁ét(Spec ℤ) = 1 ⇒ H¹ét = 0. TAA Lemma 141 §4: H¹ table with a flow-H¹ column; Q(√2) circle length √2·log(1+√2) = 1.24645 (Schoof). The H¹ that carries zeros is flow-relative (ψ − x).

**Also known as:** flow-relative H¹

**Axes:** Spec ℤ gap

**TAA lemmas:** 140, 141

**Scores (Heuristic):** gap significance 0.8 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)

**Relations (incoming):** [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1) (same mechanism as)

### #36 · 0.540 · Connes trace formula <a id="connes-trace"></a>

**Label:** Cited · **id:** `connes_trace` · **quadrant:** RH-sharp

*In plain words:* Connes’ trace formula on the adele class space: zeros appear as an absorption spectrum, and the global trace formula holding is equivalent to RH.

**Core.** Connes 1999 (read at source, TAA Lemma 30/TAA Lemma 71): global trace formula ≡ RH; Thm 1 sees only critical zeros (δ > 1); Thm 5 char p; zeros = absorption spectrum (TAA Lemma 71). TAA Lemma 82: cutoff, non-critical zeros as resonances. TAA Lemma 118: Connes reduces RH for Hecke L to the trace formula ⇒ Weil positivity; absorption spectrum ghost-blind. TAA Lemma 138 R2: Hilbert–Pólya positivity is circular if the inner product is Weil’s form.

**Also known as:** adelic class space

**Axes:** Spec ℤ gap, restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 30, 71, 82, 118, 138

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Weil positivity criterion](#weil-positivity) — reduces to Weil positivity (TAA Lemma 118)

**Relations (incoming):** [Bost–Connes KMS states](#kms-bost-connes) (analogue of)

### #50 · 0.452 · Connes–Consani sites <a id="connes-consani"></a>

**Label:** Cited · **id:** `connes_consani` · **quadrant:** true but ghost-blind/untested

*In plain words:* Topos-theoretic candidate for Spec ℤ × Spec ℤ.

**Core.** Arithmetic site and scaling site (CC14, CC16): a square exists, with Ψ_λ and s(f,f) = D•D (TAA Lemma 30), but no H¹, RR or Hodge index on it (TAA Lemma 65). TAA Lemma 147: their proved RRs are 1-dimensional; RR on the square is open (CC18).

**Also known as:** arithmetic site; scaling site

**Axes:** Spec ℤ gap

**TAA lemmas:** 30, 131, 140, 147

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object)

**Relations (incoming):** [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (lives in)

### #52 · 0.452 · Products grow linearly (2n), not quadratically <a id="products-linear"></a>

**Label:** Theorem · **id:** `products_linear` · **quadrant:** true but ghost-blind/untested

*In plain words:* Sections on naive products of Spec ℤ̄ grow only linearly in n (slope 2); a genuine surface needs quadratic growth, which forces the rank to grow with n.

**Core.** TAA Lemma 147 [T/N]: product sandwich ⌈log₂ #⌉ ≤ dim_𝕊(box) ≤ Σ dims, exact = additive bound in 6/6 boxes; fixed rank ⇒ linear: Spec ℤ̄² fits 1.99993n + 2.0009 (vs 2n + 4); quadratic growth ⇒ rank ≳ n. Same as TAA Lemma 145 Thm linear (fixed-rank lattice ⇒ h⁰ linear, h⁰/n = 2.000 at n = 400).

**Formula.** dim_𝕊 H⁰(nD) ≈ 2n + O(1)

**Numbers.** 1.99993n + 2.0009 · 6/6 boxes exact

**Also known as:** product sandwich; fixed rank ⇒ linear; Spec ℤ̄² growth 2n

**Axes:** Spec ℤ gap, numerics/certificate

**TAA lemmas:** 147, 145

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- fails for → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) — no quadratic S1
- same mechanism as → [Parity argument: linear χ cannot see D²](#parity-linear-chi) — linear χ sees only degree

### #58 · 0.419 · Riemann hypothesis (target node) <a id="rh"></a>

**Label:** Open · **id:** `rh` · **quadrant:** true but ghost-blind/untested

*In plain words:* All nontrivial zeros of ζ have real part ½. In TAA every ghost-sensitive global sign statement for Spec ℤ turns out to be RH restated.

**Core.** RH is not proved in TAA. The positivity inventory of the programme finds that every ghost-sensitive global quadratic statement for Spec ℤ is a restatement of RH.

**Formula.** ρ = β + iγ, β = ½ for all ρ

**Also known as:** RH; Θ = ½

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 1, 107

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

> ⚠ **Correction / caution.** Every lemma PDF carries "RH NOT proved".

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (equivalent to RH); [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (equivalent to RH); [Lagarias/Hinkkanen criterion](#lagarias) (equivalent to RH); [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (equivalent to RH); [Passivity (positive real part)](#passivity) (equivalent to RH); [Relative Gram matrix G_rel](#relative-gram) (equivalent to RH); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (equivalent to RH); [Rosati positivity](#rosati) (equivalent to RH); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (equivalent to RH); [RH for curves over F_q (Weil)](#fq-curves) (analogue of); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (implies); [Decay rate ¼](#decay-quarter) (equivalent to RH); [Compatible complex structure J commuting with Frobenius](#compatible-j) (equivalent to RH); [Connes trace formula](#connes-trace) (equivalent to RH); [Li criterion](#li-criterion) (equivalent to RH); [Suzuki’s de Branges line from the prime side](#suzuki-line) (equivalent to RH); [Bagchi recurrence](#bagchi) (equivalent to RH); [de Bruijn–Newman constant Λ](#debruijn-newman) (equivalent to RH); [Hodge index theorem](#hodge-index) (equivalent to RH); [Cartan involution / compact unitary group](#cartan-involution) (fails for); [Two-point form g + iω ≥ 0](#two-point) (equivalent to RH); [Hilbert–Pólya](#hilbert-polya) (implies); [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (fails for); [Cusp forms & Petersson positivity](#cusp-forms-petersson) (fails for); [Hecke operators](#hecke) (fails for)

### #59 · 0.419 · Arithmetic Castelnuovo object (C1–C4) <a id="castelnuovo-object"></a>

**Label:** Open · **id:** `castelnuovo_object` · **quadrant:** true but ghost-blind/untested

*In plain words:* Requirements an arithmetic surface would need to reproduce the curve proof.

**Core.** TAA Lemma 136: an arithmetic Castelnuovo object needs (C1) infinite H¹, (C2) positive involution, (C3) u_t u_t† = e^t, (C4) positivity proved without zeros; circularity flagged (TAA Lemma 106). TAA Lemma 138: the Čech 2-class supplies C2–C3 structure but not the sign. TAA Lemma 147: the decisive missing objects are H¹ on the square, an NS ⊋ U containing Ψ_λ, and quadratic RR.

**Also known as:** C1–C4

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 136, 138, 145, 147

**Scores (Heuristic):** gap significance 0.8 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

**Relations (outgoing):**

- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)

**Relations (incoming):** [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) (same mechanism as); [Connes–Consani sites](#connes-consani) (same mechanism as); [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) (special case of)

### #60 · 0.419 · No Riemann–Roch for C_ℚ × C_ℚ (the square is open) <a id="cc-square-open"></a>

**Label:** Open · **id:** `cc_square_open` · **quadrant:** true but ghost-blind/untested

*In plain words:* There is no Riemann–Roch theorem for the square of the scaling site; Connes–Consani themselves list H¹ on the square, and hence RR there, as open.

**Core.** TAA Lemma 147, correction 2: "their RR for the square / C_ℚ × C_ℚ, if it exists" — it does not exist; CC18 states H¹ on the square of the scaling site, and hence RR there, is open. TAA Lemma 147 (iv): decisive missing objects = H¹ on the square, an intersection theory putting Ψ_λ into an NS larger than U, and quadratic RR.

**Also known as:** RR on the square; H¹ on the square; TAA Lemma 147, correction 2

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 147

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

> ⚠ **Correction / caution.** Do not cite a CC Riemann–Roch on the square: none exists (TAA Lemma 147, correction 2).

**Relations (outgoing):**

- special case of → [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) — the missing arithmetic surface
- corrects → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) — proved RRs are only 1-dimensional

**Relations (incoming):** [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (same mechanism as); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (special case of)

### #71 · 0.347 · Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional) <a id="cc-riemann-roch"></a>

**Label:** Cited · **id:** `cc_riemann_roch` · **quadrant:** true but ghost-blind/untested

*In plain words:* Connes and Consani proved Riemann–Roch for the compactified Spec ℤ, counting sections by integer numbers of generators; it is a one-dimensional "χ = degree + constant" law and cannot see D².

**Core.** CC23 Thm 1.1/5.1 over 𝕊: dim H⁰ − dim H¹ = ⌈deg₂D⌉′ + 1 (genus 0, base 2, no exceptional set); CC22 over 𝕊[±1]: ⌈(deg D + log 2)/log 3⌉′ − 1_L, duality H⁰(K−D) ≅ Hom(H¹(D), U(1)_{1/4}), K = −2{2}; scaling site Thm 5.17 Dim_ℝ H⁰(D) − Dim_ℝ H⁰(−D) = deg D. Verdict (TAA Lemma 147): all proved RRs are 1-dimensional, χ = deg + const ⇒ blind to D² by TAA Lemma 145 parity.

**Formula.** dim H⁰(D) − dim H¹(D) = ⌈deg₂D⌉′ + 1

**Numbers.** RR grid 320 points, error 0 · χ(D) + χ(−D) = 2

**Also known as:** VF-1; CC22; CC23; RR over 𝕊

**Axes:** Spec ℤ gap, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 147, 145

**Scores (Heuristic):** gap significance 0.8 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.347

> ⚠ **Correction / caution.** RR is for the Arakelov compactification Spec ℤ̄, not Spec ℤ; two versions, the 𝕊 one supersedes 𝕊[±1] (TAA Lemma 147, correction 3).

> ⚠ **Correction / caution.** Dim_ℝ is a Lebesgue covering dimension on C_p, not a theta count (TAA Lemma 147, correction 1).

**Relations (outgoing):**

- analogue of → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)

**Relations (incoming):** [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) (fails for); [Parity argument: linear χ cannot see D²](#parity-linear-chi) (same mechanism as); [Integer dimension over 𝕊 (minimal generators)](#dim-s) (special case of); [Must-fail-for-DH acceptance test](#dh-acceptance) (fails for); [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) (corrects); [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) (same mechanism as)

### #82 · 0.325 · Arakelov geometry <a id="arakelov"></a>

**Label:** Cited · **id:** `arakelov` · **quadrant:** true but ghost-blind/untested

*In plain words:* Compactified arithmetic surfaces.

**Core.** TAA Lemma 74: Ô(1)² = ½ for FS metrics; pole-plane Gram [[½,1],[1,0]] signature (1,1); Hodge index vacuous in genus 0. TAA Lemma 139: Pic^(Spec ℤ̄) ≅ ℝ has rank 1 and no complex structure. TAA Lemma 65/TAA Lemma 145: Faltings–Hriljac = Hodge index on arithmetic surfaces (curve × Spec O_K), relative part = Néron–Tate, not ζ. TAA Lemma 138 R5: Néron–Tate PD (37a1 ĥ = 0.051114).

**Also known as:** Pic^

**Axes:** Spec ℤ gap

**TAA lemmas:** 65, 74, 138, 139, 145

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- fails for → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)

**Relations (incoming):** [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (fails for)

### #85 · 0.325 · F₁ base <a id="f1-base"></a>

**Label:** Cited · **id:** `f1_base` · **quadrant:** true but ghost-blind/untested

*In plain words:* The hoped-for "field with one element" under Spec ℤ. Over F₁ the single Frobenius trace becomes a sum over all zeros, and Connes–Consani take the sphere spectrum 𝕊 as F₁.

**Core.** TAA Lemma 65: a_p is the right model, but over F₁ the single trace becomes Σ_ρ u^ρ (one eigenvalue per zero, infinite genus, N(1) = −∞); for curves the CC dictionary is literal (u = qⁿ, α_i = q^{ρ_i}). CC10 N(u) positive on (1,∞) is prime-side and shared by Beurling systems ⇒ cannot force RH alone. TAA Lemma 147, correction 4: "On the metaphysics of F₁" proves no new RR; it restates CC23 and discusses 𝕊 as F₁.

**Formula.** N(u) = u − d/du(Σ_ρ order(ρ) u^{ρ+1}/(ρ+1)) + 1

**Also known as:** field with one element

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 65, 147

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** CC N(u) is only formal (TAA Lemma 65 C1).

**Relations (outgoing):**

- same mechanism as → [Spec ℤ is terminal](#spec-z-terminal)

**Relations (incoming):** [Spec ℤ is terminal](#spec-z-terminal) (same mechanism as)

### #86 · 0.325 · Principalization <a id="principalization"></a>

**Label:** Theorem · **id:** `principalization` · **quadrant:** true but ghost-blind/untested

*In plain words:* Making divisors principal; Abel–Jacobi = principalization (TAA Lemma 139).

**Core.** TAA Lemma 60: "principalization as hamiltonization"; clutching = principalization (analogy). TAA Lemma 71: curve version theorem — #Pic⁰(F_{pⁿ}) = |1 − πⁿ|²; on Spec ℤ only the ℝ>0 boost (blind to θ_p). TAA Lemma 73: class group = obstruction to integral spinor square roots of light rays. TAA Lemma 139: Abel–Jacobi = principalization.

**Also known as:** Abel–Jacobi

**Axes:** Spec ℤ gap

**TAA lemmas:** 60, 71, 73, 139

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- analogue of → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)

**Relations (incoming):** [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (analogue of)

### #87 · 0.325 · Spec ℤ is terminal <a id="spec-z-terminal"></a>

**Label:** Theorem · **id:** `spec_z_terminal` · **quadrant:** true but ghost-blind/untested

*In plain words:* Spec ℤ has no base to fiber over, unlike a curve over F_q.

**Core.** Spec ℤ ×_ℤ Spec ℤ = Spec ℤ (TAA Lemma 65 THM), so the "square" must be built elsewhere (arithmetic site, Borger). TAA Lemma 137: Spec ℤ is terminal ⇒ Yoneda gives uniqueness only. TAA Lemma 140: π₁ét(Spec ℤ) = 1.

**Also known as:** no base

**Axes:** Spec ℤ gap

**TAA lemmas:** 65, 90, 137, 140

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [F₁ base](#f1-base)

**Relations (incoming):** [F₁ base](#f1-base) (same mechanism as)

### #89 · 0.325 · Weil Rosetta stone <a id="weil-rosetta"></a>

**Label:** Cited · **id:** `weil_rosetta` · **quadrant:** true but ghost-blind/untested

*In plain words:* Weil’s analogy number fields / function fields / Riemann surfaces.

**Core.** TAA Lemma 140: Rosetta table (loop, H¹, 1 ⊕ 𝕃, counts, involution, sign); the Spec ℤ sign cell is missing (Weil positivity ⇔ RH). Column 2’s sign is the dim-2 algebraic shadow of Hodge–Riemann (surface + ample + RR ⇒ Hodge index). Weil’s 1940 letter quotes read at source (Krieger, Notices 52(3)).

**Also known as:** three columns

**Axes:** Spec ℤ gap, geometry over F_q

**TAA lemmas:** 140

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- analogue of → [RH for curves over F_q (Weil)](#fq-curves)

**Relations (incoming):** [RH for curves over F_q (Weil)](#fq-curves) (lives in)

### #90 · 0.325 · Cohesion (arena) <a id="cohesion"></a>

**Label:** Theorem · **id:** `cohesion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Cohesion is the arena, not the surface.

**Core.** TAA Lemma 141 §3: cohesion is the arena, not the surface; the étale ∞-topos of Spec ℤ is not cohesive (pro-shape, Hoyois); new Thm: [ℕ^×, Set] is not cohesive (Γ has no right adjoint). D10 (relative cohesion). TAA Lemma 146 §5: the cohesion quadruple Π ⊣ Disc ⊣ Γ ⊣ coDisc is a line without sign; RLGC is a 2×2 grid with mirror/KK/sign — numerology only.

**Also known as:** cohesive topos

**Axes:** Spec ℤ gap

**TAA lemmas:** 96, 141, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Heaviside ≠ cohesion one-to-one.

### #97 · 0.307 · Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR) <a id="euler-char-chi"></a>

**Label:** Theorem · **id:** `euler_char_chi` · **quadrant:** true but ghost-blind/untested

*In plain words:* The χ in the Connes–Consani Riemann–Roch is an Euler characteristic: sections minus obstructions of a divisor D. It is a number attached to D, not a character of a Galois group.

**Core.** CC23 over 𝕊: χ(D) = dim H⁰(D) − dim H¹(D) = ⌈deg₂D⌉′ + 1 (TAA Lemma 147). TAA Lemma 145 parity: a linear χ is odd in D and never contains D²; the Hodge-index step needs a quadratic χ (D²/2 term). TAA Lemma 147: χ(D) + χ(−D) = 2 (deg₂D ∉ ℤ).

**Formula.** χ(D) = dim H⁰(D) − dim H¹(D)

**Numbers.** χ(D) + χ(−D) = 2

**Also known as:** χ(D); Euler characteristic; RR χ

**Axes:** Spec ℤ gap, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 145, 147

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Notation clash: this χ is an Euler characteristic, not the character χ (or ω) of the 691 class-group eigenspace.

**Relations (outgoing):**

- same mechanism as → [Parity argument: linear χ cannot see D²](#parity-linear-chi)
- same mechanism as → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch)
- analogue of → [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) — both "χ = L-value"-type identities; analogy only

**Relations (incoming):** [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) (analogue of); [Two different χ’s: Euler characteristic vs class-group character](#two-chis) (analogue of)

### #130 · 0.181 · Two different χ’s: Euler characteristic vs class-group character <a id="two-chis"></a>

**Label:** Analogy · **id:** `two_chis` · **quadrant:** background

*In plain words:* The χ of the Connes–Consani Riemann–Roch on the square is an Euler characteristic of a divisor; the χ¹¹ / ω⁻¹¹ of the 691 story is a Galois character labelling an eigenspace. Different objects; any link is an analogy.

**Core.** Euler characteristic χ(D) = dim H⁰ − dim H¹ (TAA Lemma 145/TAA Lemma 147, a number for each divisor) vs Teichmüller / cyclotomic character ω, χ_cyc (TAA Lemma 66, labels of eigenspaces of Cl(ℚ(μ₆₉₁)) and of ρ_Δ mod 691). Shared shape only: Mazur–Wiles equates an algebraic size with an L-value, as RR equates χ with degree + constant. Neither sees the sign of D² (Iwasawa: sizes; CC RR: linear χ).

**Also known as:** which chi; χ notation clash

**Axes:** Spec ℤ gap, ghost-blind

**TAA lemmas:** 66, 145, 147

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.4 → priority 0.181

> ⚠ **Correction / caution.** Do not identify them: notation clash only.

> ⚠ **Correction / caution.** Iwasawa measures sizes, never the sign of D².

> ❓ **Not verified / open.** The analogy itself is interpretive; no TAA lemma relates the two.

**Relations (outgoing):**

- analogue of → [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi)
- analogue of → [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet)
- analogue of → [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles)

## Axis: phase/unitarity (Ax3) <a id="axis-phase-unitarity-ax3"></a>

### #29 · 0.540 · Arithmetic unitarity ("RH = unitarity") <a id="arith-unitarity"></a>

**Label:** Theorem · **id:** `arith_unitarity` · **quadrant:** RH-sharp

*In plain words:* TAA’s founding claim made precise: the scaling flow is always an isometry of the Weil form; RH is the statement that this form is positive, so the flow is genuinely unitary.

**Core.** TAA Lemma 1 Thm 2.1: (ii) T_t is a 𝒬-isometry unconditionally; (iii) growth exponent = Θ − ½; (iv) RH ⇔ 𝒬 ≥ 0 ⇔ unitary Hilbert realization ⇔ bounded matrix coefficients.

**Formula.** (T_tF)(u) = F(u − t); RH ⇔ 𝒬 ≥ 0

**Also known as:** TAA central thesis; unitary realization; T_t isometry

**Axes:** phase/unitarity (Ax3), sign/positivity (Ax2), restatement ⇔ RH

**TAA lemmas:** 1, 7

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Isometry is free (Ax3-like); positivity of the form is the content (Ax2).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — TAA Lemma 1 (iv)
- same mechanism as → [Weil positivity criterion](#weil-positivity) — same form

**Relations (incoming):** [Deninger’s foliated program](#deninger) (analogue of); [Hilbert–Pólya](#hilbert-polya) (same mechanism as); [Half-density normalization |x|^{½}](#half-density) (same mechanism as)

### #69 · 0.360 · Two partners of a zero (duality vs conjugation) <a id="two-partners"></a>

**Label:** Theorem · **id:** `two_partners` · **quadrant:** RH-sharp

*In plain words:* Every zero has a duality partner (from the functional equation) and a conjugate partner; RH says the two coincide.

**Core.** TAA Lemma 93 Thm 1.1: duality partner (Poincaré duality/cup product, ghosts too) and conjugation partner; RH ⇔ partners coincide. Rosati Tr(p(F)p(F)†) and the Weil zero side have the same "zero × duality partner" shape.

**Formula.** RH ⇔ 1 − ρ = ρ̄

**Also known as:** ρ ↔ 1 − ρ; ρ ↔ ρ̄; α ↔ q/α vs ᾱ

**Axes:** phase/unitarity (Ax3), ghost-sensitive

**TAA lemmas:** 93, 30

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- same mechanism as → [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) — mirror ρ ↦ 1 − ρ̄ fixes ρ ⇔ β = ½
- same mechanism as → [Cup product / Poincaré duality pairing](#cup-product) — duality pairing = cup product

**Relations (incoming):** [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) (same mechanism as); [Cup product / Poincaré duality pairing](#cup-product) (same mechanism as)

### #72 · 0.347 · Automorphy defect (TAA Lemma 144) <a id="automorphy-defect"></a>

**Label:** Theorem · **id:** `automorphy_defect` · **quadrant:** true but ghost-blind/untested

*In plain words:* How far a function fails to be modular, packaged as a cocycle; it is phase data.

**Core.** TAA Lemma 144: defect is a cocycle; ghost-blind. "Cocycles give structure, not sign."

**Also known as:** defect cocycle

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 144

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.347

**Relations (outgoing):**

- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle)
- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly)

**Relations (incoming):** [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as)

### #80 · 0.325 · S-mirror ρ ↦ 1 − ρ̄ <a id="s-mirror"></a>

**Label:** Theorem · **id:** `s_mirror` · **quadrant:** true but ghost-blind/untested

*In plain words:* Reflecting across the critical line; a zero is fixed exactly when it is on the line.

**Core.** ρ fixed by ρ ↦ 1 − ρ̄ ⇔ β = ½.

**Formula.** 1 − ρ̄ = ρ ⇔ β = ½

**Also known as:** mirror symmetry; critical-line reflection

**Axes:** phase/unitarity (Ax3)

**TAA lemmas:** 93, 144

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Two partners of a zero (duality vs conjugation)](#two-partners)

**Relations (incoming):** [Two partners of a zero (duality vs conjugation)](#two-partners) (same mechanism as); [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) (same mechanism as)

### #94 · 0.307 · Functional equation ξ(s) = ξ(1 − s) <a id="functional-equation"></a>

**Label:** Theorem · **id:** `functional_equation` · **quadrant:** true but ghost-blind/untested

*In plain words:* ζ’s completed version is symmetric under s ↦ 1 − s. Ghosts satisfy it too, so it cannot prove RH.

**Core.** ξ(s) = ξ(1 − s); DH satisfies FE to 5×10⁻¹⁵ yet Re ξ′/ξ = −66.8 off the line (TAA Lemma 146). Ghost-blind.

**Formula.** ξ(s) = ξ(1 − s)

**Numbers.** 5×10⁻¹⁵ · −66.8

**Also known as:** FE; completed zeta

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 103, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Symmetry is phase data, never sign.

**Relations (outgoing):**

- same mechanism as → [S-mirror ρ ↦ 1 − ρ̄](#s-mirror)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH satisfies FE without RH

**Relations (incoming):** [Davenport–Heilbronn function](#davenport-heilbronn) (fails for); [Epstein zeta no-go](#epstein) (fails for); [Scattering unitarity |φ| = 1](#scattering-phi) (special case of); [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (implies)

### #104 · 0.307 · Hecke operators <a id="hecke"></a>

**Label:** Theorem · **id:** `hecke` · **quadrant:** true but ghost-blind/untested

*In plain words:* Averaging operators on modular forms; self-adjointness gives real eigenvalues but not the Ramanujan bound.

**Core.** Hecke self-adjoint ⇒ a_p ∈ ℝ, not |a_p| ≤ 2√p (TAA Lemma 134). Ghost-blind (TAA Lemma 146).

**Also known as:** T_p; Hecke self-adjointness

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 134, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** a_p are not BSD generators.

**Relations (outgoing):**

- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann)
- fails for → [Riemann hypothesis (target node)](#rh) — ghost-blind

### #107 · 0.307 · Maass–Selberg relations <a id="maass-selberg"></a>

**Label:** Numerical · **id:** `maass_selberg` · **quadrant:** true but ghost-blind/untested

*In plain words:* Norm of truncated Eisenstein series expressed via φ and φ′; positivity there is automatic.

**Core.** TAA Lemma 146 §8.1: Maass–Selberg ‖Λ^T E‖² minimum 0.611 (ζ) vs 1.383 (DH) over 540 points ⇒ ghost-blind; it only constrains ζ(w) ≠ 0 for Re w > 1 (already known).

**Numbers.** 0.611 (ζ) · 1.383 (DH)

**Also known as:** truncated Eisenstein norm

**Axes:** phase/unitarity (Ax3), ghost-blind, reference/pole/cusp

**TAA lemmas:** 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.8 → priority 0.307

**Relations (outgoing):**

- same mechanism as → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct)

### #108 · 0.267 · Metaplectic / Kubota cocycle <a id="metaplectic"></a>

**Label:** Theorem · **id:** `metaplectic` · **quadrant:** true but ghost-blind/untested

*In plain words:* A 2-valued cocycle on SL₂ behind half-integer weight; structure without sign.

**Core.** TAA Lemma 146 §4: Kubota cocycle is a phase (Ax3); Hilbert product formula 300/300, quadratic reciprocity; θ weight ½ is metaplectic (a fourth root, TAA Lemma 141 §7) — mod 2 data, ghost-blind.

**Also known as:** Kubota; double cover

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 141, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle)
- same mechanism as → [w₂ / Čech class (TAA Lemma 138)](#w2-cech)

**Relations (incoming):** [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as)

### #110 · 0.267 · Scattering unitarity |φ| = 1 <a id="scattering-phi"></a>

**Label:** Theorem · **id:** `scattering_phi` · **quadrant:** true but ghost-blind/untested

*In plain words:* The cusp scattering coefficient has modulus one on the critical line — true with or without RH.

**Core.** |φ(½ + it)| = 1 follows from the functional equation; it is Ax3 (adjoint) only and ghost-blind.

**Formula.** |φ(½ + it)| = 1

**Also known as:** |φ| = 1; unitary scattering matrix

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 144, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Not Rosati: only the ππ† = q half.

**Relations (outgoing):**

- special case of → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)
- analogue of → [Rosati positivity](#rosati) — Ax3 half only
- analogue of → [Lax–Phillips scattering](#lax-phillips) — unitary scattering

**Relations (incoming):** [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) (same mechanism as)

### #111 · 0.267 · Eisenstein constant term & scattering φ(s) <a id="eisenstein-ct"></a>

**Label:** Theorem · **id:** `eisenstein_ct` · **quadrant:** true but ghost-blind/untested

*In plain words:* The Eisenstein series’ constant term has two pieces linked by φ(s); on Re s = ½ |φ| = 1 for any zeros — a phase statement.

**Core.** φ(s) = ξ(2s−1)/ξ(2s); |φ(½+it)| = 1 unconditionally (unitarity of scattering). Ghost-blind.

**Formula.** φ(s) = ξ(2s − 1)/ξ(2s)

**Also known as:** constant term y^s + φ(s)y^{1−s}; φ(s) = ξ(2s−1)/ξ(2s)

**Axes:** phase/unitarity (Ax3), ghost-blind, reference/pole/cusp

**TAA lemmas:** 144, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** |φ| = 1 is only Ax3.

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi)
- same mechanism as → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)

**Relations (incoming):** [Selberg resonances](#selberg-resonances) (same mechanism as); [Maass–Selberg relations](#maass-selberg) (same mechanism as)

### #113 · 0.267 · Half-density normalization |x|^{½} <a id="half-density"></a>

**Label:** Theorem · **id:** `half_density` · **quadrant:** true but ghost-blind/untested

*In plain words:* Multiplying by |x|^{½} makes scaling unitary on L²; this is why the critical line is at ½.

**Core.** TAA Lemma 145 Thm twist: |x|^½ = (dx/d*x)^½ is unitary L²(dx) → L²(d*x); U_λ unitary with generator −(x∂_x + ½); Mellin is unitary only on Re s = ½ (Plancherel 0.35355339 both sides; at Re 0.4 a weighted norm 0.53173). Cusp gauge y²∂²(y^½W) = y^½(W″ − W/4).

**Formula.** f ↦ |x|^{½} f

**Also known as:** ½ shift; unitary normalization

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 1, 141, 145

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** There are two ½’s (TAA Lemma 145 corrections): the unitary twist and the critical line.

**Relations (outgoing):**

- same mechanism as → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- same mechanism as → [Lamb cutoff](#lamb-cutoff)

**Relations (incoming):** [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (analogue of); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #114 · 0.267 · Hilbert reciprocity at 2: the odd halves become sign bits <a id="hilbert-reciprocity-at-2"></a>

**Label:** Cited · **id:** `hilbert_reciprocity_at_2` · **quadrant:** true but ghost-blind/untested

*In plain words:* At odd primes the halves (p − 1)/2 count squares; at 2 the corresponding quantities ε(u) = (u − 1)/2 and ω(u) = (u² − 1)/8 are sign bits. Hilbert reciprocity says the sign at 2 is fixed by the odd places and ∞. This is phase information, not positivity.

**Core.** (−1/p) = (−1)^{ε(p)}, (2/p) = (−1)^{ω(p)}. 2-adic Hilbert symbol: for a = 2^α u, b = 2^β v with u, v odd units, (a,b)₂ = (−1)^{ε(u)ε(v) + αω(v) + βω(u)} (Serre, A Course in Arithmetic, Ch. III, Thm 1). Product formula ∏ᵥ (a,b)ᵥ = 1 over all places including ∞ ⇒ the 2-adic sign is determined by the odd places and ∞; it is a restatement of quadratic reciprocity with both supplementary laws. ℚ₂^×/squares has order 8; ℤ₂^×/squares = {±1, ±5} has order 4: two sign bits, ε (sign of −1) and ω (the √2 / χ₈ bit). Checked: product formula holds for 3000 random pairs |a|, |b| ≤ 5000; ε, ω for u = 1, 3, 5, 7: (0,0), (1,1), (0,1), (1,0). Phase data (Ax3), ghost-blind: Davenport–Heilbronn shares the same reciprocity.

**Formula.** ∏ᵥ (a,b)ᵥ = 1, (a,b)₂ = (−1)^{ε(u)ε(v) + αω(v) + βω(u)}

**Numbers.** ℚ₂^×/(ℚ₂^×)² order 8 · ℤ₂^×/squares = {±1, ±5} · 3000/3000 product-formula checks

**Also known as:** ε(u) = (u−1)/2; ω(u) = (u²−1)/8; 2-adic Hilbert symbol; sign of the prime 2; product formula

**Axes:** phase/unitarity (Ax3), ghost-blind, reference/pole/cusp

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 0.8 → priority 0.267

> ⚠ **Correction / caution.** The sign at 2 is a reciprocity sign (phase), not the positivity sign of RH; reading it as the half-density counterpart is an analogy.

> ⚠ **Correction / caution.** Equivalent to quadratic reciprocity, not to RH.

> ❓ **Not verified / open.** to verify: Serre, A Course in Arithmetic, Ch. III Thm 1 not opened here; formula re-checked numerically via the product formula only.

**Relations (outgoing):**

- same mechanism as → [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) — odd halves (p ± 1)/2 ↔ sign bits ε, ω at 2
- same mechanism as → [The prime 2 as the wild place](#prime-two-wild) — 2 as the wild place
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Hilbert symbol = the cocycle behind the metaplectic cover
- same mechanism as → [√2 family](#sqrt2-family) — ω is the χ₈ = (2/·) bit

### #116 · 0.267 · w₂ / Čech class (TAA Lemma 138) <a id="w2-cech"></a>

**Label:** Theorem · **id:** `w2_cech` · **quadrant:** true but ghost-blind/untested

*In plain words:* Obstruction class to a spin structure, tested as a candidate arithmetic object (TAA Lemma 138).

**Core.** TAA Lemma 138: the Čech 2-class (polarization, c₁) supplies the pairing, † and Ax3 (π*L ≅ L^q) for free; spin supplies mod-2 refinements only; the sign is always ampleness. TAA Lemma 141 §7: w₂ = c₁ mod 2; half-densities are canonical (no w₂); w₂ governs half-forms (K^{1/2} = ω weight 1).

**Also known as:** Stiefel–Whitney; spin obstruction

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 141

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** w₂ is not for densities (TAA Lemma 141 list).

**Relations (outgoing):**

- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle)

**Relations (incoming):** [Metaplectic / Kubota cocycle](#metaplectic) (same mechanism as); [Spin structure & theta characteristic](#spin-theta) (same mechanism as)

### #119 · 0.267 · Cup product / Poincaré duality pairing <a id="cup-product"></a>

**Label:** Theorem · **id:** `cup_product` · **quadrant:** true but ghost-blind/untested

*In plain words:* The pairing of cohomology classes; it gives the duality partner of a zero, ghosts included.

**Core.** Duality partner via cup product (TAA Lemma 93); positivity needs conjugate + Hodge structure (HR).

**Also known as:** ∪; duality pairing

**Axes:** phase/unitarity (Ax3), ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 93, 134, 138

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → [Two partners of a zero (duality vs conjugation)](#two-partners)

**Relations (incoming):** [Two partners of a zero (duality vs conjugation)](#two-partners) (same mechanism as); [Hodge–Riemann bilinear relations](#hodge-riemann) (special case of)

### #120 · 0.267 · Theta inversion θ(1/t) = √t θ(t) <a id="theta-inversion"></a>

**Label:** Theorem · **id:** `theta_inversion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Poisson summation gives the functional equation; phase data.

**Core.** θ(1/x) = √x θ(x) gives Riemann’s FE and the boundary terms f(0), f̂(0) of 1/(s(s−1)) (TAA Lemma 36 §6). TAA Lemma 138 R4: theta inversion for x² + 5y² to 3e−30; Weil representation unitary, (ST)³ = Gauss sum · I; unitarity ⇒ FE only, ghost-blind (Thm). TAA Lemma 145: θ FE error 6.3e−26; TAA Lemma 146: θ S-error ≤ 2.5e−16, Fresnel = half-density × Weil index.

**Formula.** θ(1/t) = √t θ(t)

**Also known as:** Jacobi theta; Poisson summation

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 36, 138, 145, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- implies → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Weil index

### #122 · 0.267 · Spin structure & theta characteristic <a id="spin-theta"></a>

**Label:** Theorem · **id:** `spin_theta` · **quadrant:** true but ghost-blind/untested

*In plain words:* Theta characteristics = spin structures = square roots of the canonical bundle; they refine the Weil pairing mod 2 and are shared by fakes and true curves alike.

**Core.** TAA Lemma 136: theta chars = spin structures = quadratic refinements of the Weil pairing; Arf counts 3/1, 10/6, 36/28, 136/120, 528/496 (g ≤ 5); K^{1/2} = fixed points of D ↦ K − D = self-dual centre s = ½ [R]. TAA Lemma 138 R3 (exhaustive g ≤ 2): #Frobenius-fixed theta chars = #J[2](F_q); fakes share mod-2 data with true curves ⇒ ghost-blind (Thm). TAA Lemma 141 §7: w₂ governs half-forms (K^{1/2}), not half-densities.

**Numbers.** Arf 3/1, 10/6, 36/28, 136/120, 528/496

**Also known as:** theta characteristic; spin

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 50, 136, 138, 141

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** "Spec ℤ not spin": the real place obstructs a half twist — analogy only (TAA Lemma 50 Rem 7.3).

**Relations (outgoing):**

- same mechanism as → [w₂ / Čech class (TAA Lemma 138)](#w2-cech)

### #123 · 0.256 · "Cocycles give structure, not sign" <a id="cocycle-principle"></a>

**Label:** Heuristic · **id:** `cocycle_principle` · **quadrant:** background

*In plain words:* Any cocycle/class (metaplectic, w₂, defect) fixes structure but cannot decide a positivity sign.

**Core.** TAA Lemma 138/TAA Lemma 144/TAA Lemma 146 summary principle.

**Also known as:** cocycle principle

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 144, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 0.7 · specificity 0.05 · tractability 0.5 · evidence 0.6 → priority 0.256

**Relations (outgoing):**

- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive)

**Relations (incoming):** [Automorphy defect (TAA Lemma 144)](#automorphy-defect) (same mechanism as); [Metaplectic / Kubota cocycle](#metaplectic) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [w₂ / Čech class (TAA Lemma 138)](#w2-cech) (same mechanism as)

## Axis: ghost-sensitive <a id="axis-ghost-sensitive"></a>

### #31 · 0.540 · Ghost quartet ½ ± δ ± iγ <a id="ghost-quartet"></a>

**Label:** Theorem · **id:** `ghost_quartet` · **quadrant:** RH-sharp

*In plain words:* A fake set of four zeros off the line, replacing a pair ½ ± iγ, used to test whether a criterion can detect RH failure.

**Core.** TAA Lemma 103 convention: replace ½ ± iγ by ½ ± δ ± iγ; each quartet gives 2 negative Weil eigenvalues; onsets L* listed.

**Formula.** ½ ± δ ± iγ

**Numbers.** onsets 0.90, 1.15, 1.70, 3.45

**Also known as:** ghost; off-line quartet; synthetic ghost

**Axes:** ghost-sensitive, numerics/certificate

**TAA lemmas:** 103, 110, 144

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** δ convention conflict: δ = β − ½ (TAA Lemma 25/TAA Lemma 103/TAA Lemma 143) vs δ_ρ = 2β − 1 (TAA Lemma 144).

**Relations (outgoing):**

- same mechanism as → [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index)
- same mechanism as → [Ghost conventions (δ, heat-flow healing)](#ghost-conventions)

**Relations (incoming):** [Gain lines (active media)](#gain-line) (analogue of); [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) (same mechanism as); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as); [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) (same mechanism as)

### #42 · 0.540 · Bagchi recurrence <a id="bagchi"></a>

**Label:** Cited · **id:** `bagchi` · **quadrant:** RH-sharp

*In plain words:* RH ⇔ ζ approximates itself in the strip (strong recurrence).

**Core.** Bagchi (via Nakamura Thm B): RH ⇔ strong recurrence of ζ for all K, ε ("infinite prime bath still recurs", TAA Lemma 118). TAA Lemma 123 local form [T given Voronin + Carlson]: ζ strongly recurrent on a disc K ⇔ no zero on K; ghosts show up as a local Rouché defect. Finite prime baths recur but are ghost-blind.

**Also known as:** universality

**Axes:** ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 118, 123

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- analogue of → [Passivity (positive real part)](#passivity) — prime-bath / arrow-of-time reading (TAA Lemma 118)

### #43 · 0.540 · de Bruijn–Newman constant Λ <a id="debruijn-newman"></a>

**Label:** Cited · **id:** `debruijn_newman` · **quadrant:** RH-sharp

*In plain words:* Heat flow on ξ; Λ ≥ 0 (Rodgers–Tao), RH ⇔ Λ = 0.

**Core.** Λ ≥ 0 ⇒ ζ not heat-flow stable (TAA Lemma 111). Healing times TAA Lemma 124/TAA Lemma 136 conflict.

**Also known as:** heat flow; Λ ≥ 0

**Axes:** ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 111, 124, 136

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** t* = 2δ² vs δ²/2.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Λ = 0
- analogue of → [Krein collisions (how ghosts are born)](#krein-collision)

**Relations (incoming):** [Krein collisions (how ghosts are born)](#krein-collision) (analogue of)

### #55 · 0.451 · Must-fail-for-DH acceptance test <a id="dh-acceptance"></a>

**Label:** Heuristic · **id:** `dh_acceptance` · **quadrant:** sharp but interpretive

*In plain words:* Any future Riemann–Roch on the square must be false for Davenport–Heilbronn; otherwise it cannot prove RH. So it has to use the Euler product.

**Core.** All H⁰-side objects are built from ℤ ⊂ 𝔸_ℚ and are ghost-blind; the topological side s(f,f) is ghost-sensitive (TAA Lemma 142: DH-location ghost positive from L* = 3.45, actual DH from 4.70). Hence an RR theorem on the square must FAIL for DH ⇒ must use the Euler product / ring structure (necessary condition, proposed acceptance test, TAA Lemma 147).

**Numbers.** L* = 3.45 (DH-location ghost) · 4.70 (actual DH, uncertified list)

**Also known as:** ghost criterion; Euler-product necessity; CC-4 test; TAA Lemma 147

**Axes:** ghost-sensitive, no-go / refuted, Spec ℤ gap

**TAA lemmas:** 147, 142

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 0.7 · specificity 1.0 · tractability 0.5 · evidence 0.48 → priority 0.451

> ⚠ **Correction / caution.** A necessary condition only.

> ❓ **Not verified / open.** Proposed acceptance test.

**Relations (outgoing):**

- same mechanism as → [Davenport–Heilbronn function](#davenport-heilbronn) — DH as test object
- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) — H⁰ blind, s(f,f) sensitive
- fails for → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) — proved RRs pass DH, so cannot decide RH

### #65 · 0.380 · Chebyshev bias for elliptic curves (averaged sign of a_p) <a id="elliptic-chebyshev-bias"></a>

**Label:** Open · **id:** `elliptic_chebyshev_bias` · **quadrant:** RH-sharp

*In plain words:* Individual signs of a_p are phase data, but their running average is biased, and the bias is governed by the zeros of L(E, s) and the analytic rank, in the same way ψ(x) − x is governed by the zeros of ζ. An off-line zero would make the averaged sign blow up like a power of x.

**Core.** Proposed comparison (TAA Lemma 150 plan): averaged sign of a_p for 11a, 37a, 389a and 32a (y² = x³ − x) against ψ − x; ties to Goldfeld’s product ∏ L_p(E,1) ∼ C/(log x)^r. Under RH the bias is a log-scale effect; an off-line zero gives power-law growth. The literature citation for an elliptic-curve Chebyshev bias is to verify and is not given.

**Also known as:** average sign of a_p; prime race for a_p

**Axes:** ghost-sensitive, reference/pole/cusp, open target

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.4 → priority 0.380

> ⚠ **Correction / caution.** Literature citation to verify: none is given until opened at source.

> ❓ **Not verified / open.** to verify: the Chebyshev-bias citation for elliptic curves is unverified (not opened); no reference given.

**Relations (outgoing):**

- same mechanism as → [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) — Goldfeld product (log x)^r
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — averaged error term governed by zeros
- analogue of → [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) — individual sign (phase) vs averaged sign (zeros)

### #70 · 0.360 · Ghost conventions (δ, heat-flow healing) <a id="ghost-conventions"></a>

**Label:** Theorem · **id:** `ghost_conventions` · **quadrant:** RH-sharp

*In plain words:* Bookkeeping for ghost parameters across lemmas; several conventions disagree.

**Core.** δ = β − ½ (TAA Lemmas 25, 103, 143) vs δ_ρ = 2β − 1 (TAA Lemma 144). Heat-flow healing time t* = 2δ² (TAA Lemma 124) vs δ²/2 (TAA Lemma 136).

**Numbers.** t* = 2δ² (TAA Lemma 124) · t* = δ²/2 (TAA Lemma 136)

**Also known as:** TAA Lemma 103 convention; δ_ρ

**Axes:** ghost-sensitive

**TAA lemmas:** 25, 103, 106, 124, 136, 143, 144

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 0.8 → priority 0.360

> ⚠ **Correction / caution.** Always state which δ is used.

> ❓ **Not verified / open.** Conflicts unresolved.

**Relations (outgoing):**

- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)

**Relations (incoming):** [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) (same mechanism as)

## Axis: geometry over F_q <a id="axis-geometry-over-f-q"></a>

### #34 · 0.540 · Fake Weil polynomials (finite ghosts) <a id="fake-weil-poly"></a>

**Label:** Theorem · **id:** `fake_weil_poly` · **quadrant:** RH-sharp

*In plain words:* Polynomials that look like curve zeta numerators (functional equation, integer counts) but have roots off the circle. They are the F_q test ghosts.

**Core.** Fakes pass FE, count positivity, mod-2 data and the Hecke lattice (1,2); they fail Hodge index on ⟨H,V,Δ,Γ_{Fⁿ}⟩ (n₊ ≥ 2) and Rosati. Mixed fake (T² − 6T + 7)(T² + 7) passes N ≤ 2, fails from N = 4 (TAA Lemma 137, TAA Lemma 141).

**Numbers.** T² − 5T + 5: |α| = 3.618 > √5 · g = 2, q = 11: 2935 count-positive ghosts (TAA Lemma 109)

**Also known as:** fakes; T² − 5T + 5; ghost a=25 q=101; quartet q=11

**Axes:** geometry over F_q, ghost-sensitive, numerics/certificate

**TAA lemmas:** 88, 94, 109, 137, 138, 141

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Degenerate fakes (|α| ∈ {1, q}) cause pole-degenerate exceptions (TAA Lemma 92 C9).

**Relations (outgoing):**

- fails for → [Ax1–Ax3 axioms (Yoneda specification)](#ax123) — no positive † with ππ† = q
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — F_q analogue of DH

**Relations (incoming):** [Tate count / Picard number (ghost-blind)](#tate-count) (fails for); [Counts vs quadratic positivity](#count-positivity) (fails for)

### #44 · 0.540 · Frobenius as a boost (rapidity ½ log q) <a id="frobenius-boost"></a>

**Label:** Theorem · **id:** `frobenius_boost` · **quadrant:** RH-sharp

*In plain words:* On the light-cone plane Frobenius acts like a Lorentz boost of rapidity ½ log q; a true curve needs one boost, a fake needs two.

**Core.** Hodge index + one boost of rapidity ½ log q on the H–V plane ⇒ Hasse; fakes need two (TAA Lemma 98 thm:fqboost). Over ℚ: translation is an isometry, pole boost rapidity ½ log λ; Lorentzian = Weil positivity (restatement).

**Formula.** B_{½ log q}(H + V) = Γ/√q (hyperbolic part)

**Numbers.** q = 101: translation length 2.3076 = ½ log 101

**Also known as:** one boost; hyperbolic orthogonal; Levinson boosts

**Axes:** geometry over F_q, structure/frame (Ax1), ghost-sensitive

**TAA lemmas:** 14, 98, 99, 107, 114, 117

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Dividing by √q does not undo the boost (TAA Lemma 114, correction 14).

> ⚠ **Correction / caution.** Two boosts are never a pure rotation unless inverse (TAA Lemma 107).

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — acts on U
- analogue of → [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) — Levinson/Szegő step = boost of rapidity artanh|α| (TAA Lemma 98, TAA Lemma 117)

**Relations (incoming):** [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) (analogue of)

### #68 · 0.360 · Krein collisions (how ghosts are born) <a id="krein-collision"></a>

**Label:** Theorem · **id:** `krein_collision` · **quadrant:** RH-sharp

*In plain words:* Zeros on the line carry a sign; two can only leave the line together if they meet with opposite signs.

**Core.** TAA Lemma 111: semisimple unit-spectrum F strongly stable ⇔ Krein form definite on each eigenspace; ghosts born only at opposite-sign collisions (710/710 births). For ζ the graphical Krein sign alternates ⇒ no protection; Λ ≥ 0 ⇒ ζ not heat-flow stable.

**Numbers.** 300 paths: 710 births, all opposite-sign

**Also known as:** Krein sign; opposite-sign collision; strong stability

**Axes:** geometry over F_q, ghost-sensitive

**TAA lemmas:** 27, 41, 111, 120

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

> ⚠ **Correction / caution.** Krein = stability, not positivity; presupposes unit spectrum (TAA Lemma 111 circularity).

**Relations (outgoing):**

- analogue of → [de Bruijn–Newman constant Λ](#debruijn-newman) — heat-flow collisions
- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — pair leaves as (γ ± iδ)²

**Relations (incoming):** [de Bruijn–Newman constant Λ](#debruijn-newman) (analogue of)

### #95 · 0.307 · Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity) <a id="gauss-sum-unitarity"></a>

**Label:** Theorem · **id:** `gauss_sum_unitarity` · **quadrant:** true but ghost-blind/untested

*In plain words:* A quadratic Gauss sum has absolute value exactly √p: this is the statement that the finite Fourier transform is unitary. For the CM curve y² = x³ − x and p ≡ 1 mod 4, the Frobenius eigenvalue is a Gaussian integer π with ππ̄ = p, so RH for this curve is the same kind of unitarity identity.

**Core.** |g|² = p (checked numerically for all odd p ≤ 691) = Plancherel for the finite Fourier transform, the same |x|^{½} twist as TAA Lemma 145. For p ≡ 1 mod 4, π ∈ ℤ[i], ππ̄ = p, a_p = 2 Re π, so |α| = √p is automatic. Over ℚ the analogue |ε| = 1 of a root number holds for Davenport–Heilbronn too: necessary, not sufficient. Open: a ζ-analogue in which the eigenvalue itself is a Gauss sum.

**Formula.** |g|² = p, ππ̄ = p, a_p = 2 Re π

**Numbers.** |g|² at p = 691: 691 (float)

**Also known as:** |g|² = p; finite Fourier transform unitary; CM Frobenius in ℤ[i]

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Unitarity identities of this kind are Ax3 (phase); over ℚ they are satisfied by DH too and cannot replace the sign.

**Relations (outgoing):**

- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — Plancherel / unitary |x|^{½} twist
- analogue of → [Hasse bound as a positive degree form](#hasse-pythagoras) — CM case: |π|² = p as a norm identity
- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) — phase side
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — |ε| = 1 holds for DH as well

**Relations (incoming):** [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (same mechanism as)

### #103 · 0.307 · Tate count / Picard number (ghost-blind) <a id="tate-count"></a>

**Label:** Theorem · **id:** `tate_count` · **quadrant:** true but ghost-blind/untested

*In plain words:* Counting algebraic classes on C×C does not see whether eigenvalues are on the circle.

**Core.** ρ(C×C) = 2 + Σ m(λ)m(q/λ) (Tate 1966, S–S §14.6); = 2g for squarefree, fakes too (TAA Lemma 93 Prop 2.3).

**Formula.** ρ = 2 + Σ m(λ) m(q/λ)

**Numbers.** 2923/2923 family checks (TAA Lemma 93)

**Also known as:** ρ = 2 + Σm(λ)m(q/λ); Tate classes

**Axes:** geometry over F_q, ghost-blind

**TAA lemmas:** 88, 93

**Scores (Heuristic):** gap significance 0.5 (nearest gap: flow-relative H¹ for Spec ℤ) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — fakes have the same count
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — counts are blind

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (analogue of)

### #105 · 0.307 · Primary sign rule for a_p of y² = x³ − x <a id="primary-sign-rule"></a>

**Label:** Numerical · **id:** `primary_sign_rule` · **quadrant:** true but ghost-blind/untested

*In plain words:* For p ≡ 1 mod 4 write p = a² + b² with b even; the sign of a in a_p = 2a is fixed by a 2-adic normalisation (a + b ≡ 1 mod 4). The individual sign is phase data; RH is about the size |a_p| ≤ 2√p, not the sign.

**Core.** p = a² + b², b even, a_p = 2a with a + b ≡ 1 mod 4 (π primary mod (1 + i)³); checked for all 14 primes p ≡ 1 mod 4 below 120 (p = 5, 13, 17: a_p = −2, 6, 2). The individual sign is a 2-adic phase (ghost-blind); RH = |a_p| ≤ 2√p is a size statement. The distribution of the signs (Sato–Tate for CM curves) is a separate question; no citation given here.

**Formula.** a_p = 2a, p = a² + b², a + b ≡ 1 mod 4

**Numbers.** 14/14 primes p ≡ 1 mod 4, p < 120

**Also known as:** a_p = 2a; primary mod (1+i)³; sign of a_p

**Axes:** geometry over F_q, ghost-blind, numerics/certificate

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.307

> ⚠ **Correction / caution.** The minus sign in a₅ = −2 is not the positivity sign of RH: it is a phase (choice of primary generator), and RH bounds the size.

> ❓ **Not verified / open.** Sato–Tate/Hecke–Deuring citation for CM sign distribution not verified; none given.

**Relations (outgoing):**

- same mechanism as → [The prime 2 as the wild place](#prime-two-wild) — the normalisation is 2-adic
- same mechanism as → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) — a_p = 2 Re π
- fails for → [Castelnuovo–Severi inequality](#castelnuovo-severi) — the sign of a_p is not the Castelnuovo sign

**Relations (incoming):** [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (analogue of)

### #112 · 0.267 · Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula <a id="gauss-half"></a>

**Label:** Theorem · **id:** `gauss_half` · **quadrant:** true but ghost-blind/untested

*In plain words:* Every odd prime p splits the nonzero residues into (p − 1)/2 squares and (p − 1)/2 non-squares; the quadratic character (x/p) records which. For an elliptic curve y² = f(x), a_p is minus the sum of these characters, and its value mod p is a Gauss-half power.

**Core.** a_p = −Σ_x (f(x)/p) for y² = f(x); Hasse: a_p ≡ coefficient of x^{p−1} in f^{(p−1)/2} mod p. For p ≡ 3 mod 4, (p + 1)/4 is an integer and √a = a^{(p+1)/4} mod p (691 → 173). y² = x³ − x: a_p = −2, 6, 2 for p = 5, 13, 17; a_p = 0 for p ≡ 3 mod 4, so N₆₉₁ = 692. The Gauss halves see only the coherent H¹(E, 𝒪), i.e. a_p mod p; the bound |a_p| ≤ 2√p needs positivity (Castelnuovo/Hodge index).

**Formula.** a_p = −Σ_x (f(x)/p), a_p ≡ [x^{p−1}] f^{(p−1)/2} mod p

**Numbers.** (691 + 1)/4 = 173 · N₆₉₁(y² = x³ − x) = 692

**Also known as:** Gauss 1/2 system; (p+1)/2 split; p/4 measure; 691 → 173; Hasse invariant

**Axes:** geometry over F_q, ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** a_p mod p is phase-type information; it does not give the size bound |a_p| ≤ 2√p.

> ⚠ **Correction / caution.** The ½ of (p ± 1)/2 is a counting half; relating it to the half-density ½ is an analogy.

**Relations (outgoing):**

- analogue of → [Half-density normalization |x|^{½}](#half-density) — the ½ in (p ± 1)/2 vs the unitary |x|^{½} twist; analogy
- fails for → [Castelnuovo–Severi inequality](#castelnuovo-severi) — mod-p data cannot give the size bound; that needs Castelnuovo–Severi
- same mechanism as → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity)

**Relations (incoming):** [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as)

### #131 · 0.165 · Standard conjectures (Hodge type) <a id="standard-conj"></a>

**Label:** Open · **id:** `standard_conj` · **quadrant:** true but ghost-blind/untested

*In plain words:* The higher-dimensional version of Hodge index in characteristic p; known for surfaces, open in general.

**Core.** Hodge standard conjecture: known in char 0 and for surfaces, abelian fourfolds (Ancona 2021), K3² (IIK 2022); open in general char p, dim ≥ 3. Common root of Hodge, BSD and RH over F_q; analogy over ℚ (TAA Lemma 88).

**Also known as:** Hodge standard conjecture; Grothendieck

**Axes:** geometry over F_q, open target

**TAA lemmas:** 88, 94, 134

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.165

> ⚠ **Correction / caution.** TAA Lemma 89, correction 4: unrefereed preprint claim (CM Hodge ⇒ standard conjecture) flagged, not applied.

**Relations (outgoing):**

- special case of → [Hodge index theorem](#hodge-index) — generalization

## Axis: numerics/certificate <a id="axis-numerics-certificate"></a>

### #46 · 0.492 · Integer dimension over 𝕊 (minimal generators) <a id="dim-s"></a>

**Label:** Numerical · **id:** `dim_S` · **quadrant:** true but ghost-blind/untested

*In plain words:* On Spec ℤ̄ Connes–Consani’s dimension is an integer: the least number of generators over the sphere spectrum. The log-theta dimension of van der Geer–Schoof is a different, "virtual" count that agrees up to a bounded error.

**Core.** TAA Lemma 147 [N]: brute force dim_𝕊(HZ)_[−m,m] = n + 1 for all m ≤ 16; dim_𝕊[±1] = ⌈log₃(2n+1)⌉ for all n ≤ 40; dim_𝕊 − vdGS h⁰/log 2 ∈ [1.016, 1.983]. TAA Lemma 147, correction 1: Dim_ℝ on C_p is a covering dimension, not a theta count.

**Numbers.** n + 1 (m ≤ 16) · ⌈log₃(2n+1)⌉ (n ≤ 40) · [1.016, 1.983]

**Also known as:** dim_𝕊; dim_𝕊[±1]; vdGS virtual dimension

**Axes:** numerics/certificate, Spec ℤ gap

**TAA lemmas:** 147

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.492

> ⚠ **Correction / caution.** Do not identify CC dimension with theta/lattice counts (TAA Lemma 147, correction 1).

**Relations (outgoing):**

- special case of → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch)

### #62 · 0.400 · Ghost onset L* ≈ log(γ/2π) <a id="ghost-onset"></a>

**Label:** Numerical · **id:** `ghost_onset` · **quadrant:** RH-sharp

*In plain words:* The smallest window at which a ghost quartet can be detected; it grows like the log of the ghost’s height.

**Core.** TAA Lemma 103: onsets L* = 0.90, 1.15, 1.70, 3.45 for the test ghosts; L* ≈ log(γ/2π).

**Formula.** L* ≈ log(γ/2π)

**Numbers.** 0.90 · 1.15 · 1.70 · 3.45

**Also known as:** onset length; detection scale

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 103, 142

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)

**Relations (incoming):** [Certified positivity windows](#certified-windows) (fails for); [Yoshida window positivity](#yoshida) (fails for)

### #73 · 0.347 · Certified positivity windows <a id="certified-windows"></a>

**Label:** Numerical · **id:** `certified_windows` · **quadrant:** true but ghost-blind/untested

*In plain words:* Computer-certified intervals on which the Weil form is positive.

**Core.** Certified windows: progress log reaches e² and hybrid e^2.4; one text says "stop at 1.6". All below ghost onsets, ghost-blind (TAA Lemma 142).

**Numbers.** e² · e^2.4 (hybrid) · 1.6

**Also known as:** interval-arithmetic certificates; windows to e², e^2.4

**Axes:** numerics/certificate, ghost-blind

**TAA lemmas:** 121, 127, 142

**Scores (Heuristic):** gap significance 0.5 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.347

> ⚠ **Correction / caution.** Source conflict: "stop at 1.6" vs progress log to e², e^2.4.

> ❓ **Not verified / open.** Which extent is current needs a check of the progress log.

**Relations (outgoing):**

- fails for → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset)
- special case of → [Yoshida window positivity](#yoshida)

**Relations (incoming):** [Tautology boundary (zero side vs prime side)](#tautology-boundary) (fails for); [Yoshida window positivity](#yoshida) (same mechanism as)

### #106 · 0.307 · Archimedean thresholds a* <a id="arch-threshold"></a>

**Label:** Numerical · **id:** `arch_threshold` · **quadrant:** true but ghost-blind/untested

*In plain words:* Largest window size where the archimedean part alone is positive.

**Core.** TAA Lemma 127: a*_S2 < 0.5976773 (supersedes TAA Lemma 121’s 0.602); TAA Lemma 98 states a ≤ 1 in another normalization. Ghost-blind.

**Numbers.** a*_S2 < 0.5976773 · 0.602 (TAA Lemma 121, superseded) · a ≤ 1 (TAA Lemma 98)

**Also known as:** a*_S2 < 0.5976773; a ≤ 1

**Axes:** numerics/certificate, ghost-blind, reference/pole/cusp

**TAA lemmas:** 98, 121, 127

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.307

> ⚠ **Correction / caution.** Source conflict: TAA Lemma 98 "a ≤ 1" vs TAA Lemma 127 a* < 0.5976773 (different setups/normalizations to check).

> ❓ **Not verified / open.** Normalization between TAA Lemma 98 and TAA Lemma 127 not reconciled here.

**Relations (outgoing):**

- special case of → [Archimedean place and Γ_ℝ factor](#archimedean-place)
- same mechanism as → [Yoshida window positivity](#yoshida) — window positivity

**Relations (incoming):** [Archimedean place and Γ_ℝ factor](#archimedean-place) (same mechanism as)

### #118 · 0.267 · Yoshida window positivity <a id="yoshida"></a>

**Label:** Cited · **id:** `yoshida` · **quadrant:** true but ghost-blind/untested

*In plain words:* For test functions supported in a small enough window, Weil positivity holds unconditionally.

**Core.** Yoshida: W ≥ 0 for supp f ⊂ small window; TAA Lemma 10 window ≤ log 3. Below ghost onsets, so ghost-blind.

**Numbers.** log 3 (TAA Lemma 10)

**Also known as:** Yoshida 1992; small-support positivity

**Axes:** numerics/certificate, ghost-blind

**TAA lemmas:** 10, 142

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Unconditional windows never reach ghost onset.

**Relations (outgoing):**

- same mechanism as → [Certified positivity windows](#certified-windows)
- fails for → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) — windows smaller than onset

**Relations (incoming):** [Certified positivity windows](#certified-windows) (special case of); [Archimedean thresholds a*](#arch-threshold) (same mechanism as)

## Axis: structure/frame (Ax1) <a id="axis-structure-frame-ax1"></a>

### #53 · 0.452 · Yoneda specification <a id="yoneda"></a>

**Label:** Theorem · **id:** `yoneda` · **quadrant:** true but ghost-blind/untested

*In plain words:* Specify the object by its properties (Ax1–Ax3).

**Core.** TAA Lemma 90: bare Hom sets do not determine an object (ℚ vs ℚ^(N)); naturality needed; representability ⇒ uniqueness/functoriality, presupposes positivity if it is an axiom. TAA Lemma 98 Prop 6.1: representable ⇒ unique; 𝔉(pt) ≠ ∅ ⇒ RH; "representability is the whole battle" (TAA Lemma 98, correction 19). TAA Lemma 137: T_W with Ax1–Ax3; existence open.

**Also known as:** T_W

**Axes:** structure/frame (Ax1)

**TAA lemmas:** 89, 90, 98, 137

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Ax1–Ax3 axioms (Yoneda specification)](#ax123)

## Axis: open target <a id="axis-open-target"></a>

### #61 · 0.419 · Hilbert–Pólya <a id="hilbert-polya"></a>

**Label:** Open · **id:** `hilbert_polya` · **quadrant:** true but ghost-blind/untested

*In plain words:* Find a self-adjoint operator with spectrum the γ’s.

**Core.** Standard program: a self-adjoint/unitary realization with spectrum the γ’s would give RH. TAA verdicts: spinor route = Hilbert–Pólya in Clifford dress (TAA Lemma 104); 2B″ + ½ needs an inner product (TAA Lemma 105, LP80 "all that is missing is an appropriate inner product"); missing positive V ≅ H¹ (TAA Lemma 115); circular if the inner product is Weil’s form (TAA Lemma 138 R2); lossless Heaviside realization = Hilbert–Pólya [O] (TAA Lemma 144 HS-F).

**Also known as:** self-adjoint operator

**Axes:** open target, phase/unitarity (Ax3)

**TAA lemmas:** 104, 105, 115, 138, 144

**Scores (Heuristic):** gap significance 0.8 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

**Relations (outgoing):**

- implies → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- same mechanism as → [Lax–Phillips scattering](#lax-phillips) — missing inner product

**Relations (incoming):** [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) (same mechanism as); [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) (analogue of)

## Axis: ghost-blind <a id="axis-ghost-blind"></a>

### #109 · 0.267 · The prime 2 as the wild place <a id="prime-two-wild"></a>

**Label:** Theorem · **id:** `prime_two_wild` · **quadrant:** true but ghost-blind/untested

*In plain words:* The only even prime is 2 (not √2). At 2 the Gauss halves break: (p − 1)/2 is not an integer, every model y² = f(x) has bad reduction, and the Hilbert symbol / metaplectic cocycle is wild. √2 enters through (2/p), which depends on p mod 8.

**Core.** Supplementary law: (2/p) = +1 ⇔ p ≡ ±1 mod 8; √2 ∈ ℚ(ζ₈), so (2/p) is the character χ₈ (the √2 family). At p = 2, (p − 1)/2 is not an integer and every Weierstrass model y² = f(x) is bad at 2; the Hilbert symbol and the metaplectic (Kubota) cocycle are wild at 2. All of this is phase data, hence ghost-blind.

**Formula.** (2/p) = (−1)^{(p²−1)/8}

**Also known as:** even prime; √2 and (2/p); supplementary law; bad reduction at 2

**Axes:** ghost-blind, phase/unitarity (Ax3), reference/pole/cusp

**TAA lemmas:** 150 (planned)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The even prime is 2, not √2; √2 appears only through the character (2/p) = χ₈(p).

**Relations (outgoing):**

- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — wild at 2: Hilbert symbol / Kubota cocycle
- same mechanism as → [√2 family](#sqrt2-family) — χ₈ = (2/·), √2 ∈ ℚ(ζ₈)
- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle) — structure, not sign

**Relations (incoming):** [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as)

## Index by rank

| # | priority | concept | label | quadrant |
|---|---|---|---|---|
| 1 | 0.720 | [Weil positivity criterion](#weil-positivity) | Cited | RH-sharp |
| 2 | 0.720 | [Davenport–Heilbronn function](#davenport-heilbronn) | Theorem | RH-sharp |
| 3 | 0.720 | [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) | Cited | RH-sharp |
| 4 | 0.720 | [Primitive part V₀ = U^⊥](#primitive-part) | Theorem | RH-sharp |
| 5 | 0.720 | [Lagarias/Hinkkanen criterion](#lagarias) | Cited | RH-sharp |
| 6 | 0.700 | [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) | Open | RH-sharp |
| 7 | 0.700 | [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) | Open | RH-sharp |
| 8 | 0.700 | [Missing: flow-relative H¹ for Spec ℤ](#mp-flow-h1) | Open | RH-sharp |
| 9 | 0.700 | [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) | Open | RH-sharp |
| 10 | 0.700 | [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) | Open | RH-sharp |
| 11 | 0.700 | [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) | Open | RH-sharp |
| 12 | 0.700 | [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) | Open | RH-sharp |
| 13 | 0.700 | [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) | Open | RH-sharp |
| 14 | 0.700 | [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) | Open | RH-sharp |
| 15 | 0.700 | [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) | Open | RH-sharp |
| 16 | 0.600 | [Passivity (positive real part)](#passivity) | Restatement | RH-sharp |
| 17 | 0.600 | [Relative Gram matrix G_rel](#relative-gram) | Restatement | RH-sharp |
| 18 | 0.600 | [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) | Restatement | RH-sharp |
| 19 | 0.579 | [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) | Theorem | true but ghost-blind/untested |
| 20 | 0.579 | [Ax1–Ax3 axioms (Yoneda specification)](#ax123) | Theorem | true but ghost-blind/untested |
| 21 | 0.579 | [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) | Theorem | true but ghost-blind/untested |
| 22 | 0.579 | [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) | Theorem | true but ghost-blind/untested |
| 23 | 0.579 | [Parity argument: linear χ cannot see D²](#parity-linear-chi) | Theorem | true but ghost-blind/untested |
| 24 | 0.579 | [Tautology boundary (zero side vs prime side)](#tautology-boundary) | Theorem | true but ghost-blind/untested |
| 25 | 0.579 | [Deninger’s foliated program](#deninger) | Cited | true but ghost-blind/untested |
| 26 | 0.579 | [No étale H¹ for Spec ℤ](#no-etale-h1) | Theorem | true but ghost-blind/untested |
| 27 | 0.540 | [Rosati positivity](#rosati) | Theorem | RH-sharp |
| 28 | 0.540 | [Castelnuovo–Severi inequality](#castelnuovo-severi) | Theorem | RH-sharp |
| 29 | 0.540 | [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) | Theorem | RH-sharp |
| 30 | 0.540 | [RH for curves over F_q (Weil)](#fq-curves) | Cited | RH-sharp |
| 31 | 0.540 | [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) | Theorem | RH-sharp |
| 32 | 0.540 | [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) | Cited | RH-sharp |
| 33 | 0.540 | [Decay rate ¼](#decay-quarter) | Theorem | RH-sharp |
| 34 | 0.540 | [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) | Theorem | RH-sharp |
| 35 | 0.540 | [Compatible complex structure J commuting with Frobenius](#compatible-j) | Theorem | RH-sharp |
| 36 | 0.540 | [Connes trace formula](#connes-trace) | Cited | RH-sharp |
| 37 | 0.540 | [de Branges spaces](#de-branges) | Cited | RH-sharp |
| 38 | 0.540 | [Epstein zeta no-go](#epstein) | Theorem | RH-sharp |
| 39 | 0.540 | [Hasse bound as a positive degree form](#hasse-pythagoras) | Theorem | RH-sharp |
| 40 | 0.540 | [Li criterion](#li-criterion) | Cited | RH-sharp |
| 41 | 0.540 | [Suzuki’s de Branges line from the prime side](#suzuki-line) | Cited | RH-sharp |
| 42 | 0.540 | [Bagchi recurrence](#bagchi) | Cited | RH-sharp |
| 43 | 0.540 | [de Bruijn–Newman constant Λ](#debruijn-newman) | Cited | RH-sharp |
| 44 | 0.540 | [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) | Theorem | RH-sharp |
| 45 | 0.532 | [Gain lines (active media)](#gain-line) | Analogy | sharp but interpretive |
| 46 | 0.492 | [Integer dimension over 𝕊 (minimal generators)](#dim-s) | Numerical | true but ghost-blind/untested |
| 47 | 0.452 | [Hodge index theorem](#hodge-index) | Theorem | true but ghost-blind/untested |
| 48 | 0.452 | [Lax–Phillips scattering](#lax-phillips) | Cited | true but ghost-blind/untested |
| 49 | 0.452 | [Cartan involution / compact unitary group](#cartan-involution) | Theorem | true but ghost-blind/untested |
| 50 | 0.452 | [Connes–Consani sites](#connes-consani) | Cited | true but ghost-blind/untested |
| 51 | 0.452 | [Pole plane / Tate poles at s = 0, 1](#pole-plane) | Theorem | true but ghost-blind/untested |
| 52 | 0.452 | [Products grow linearly (2n), not quadratically](#products-linear) | Theorem | true but ghost-blind/untested |
| 53 | 0.452 | [Yoneda specification](#yoneda) | Theorem | true but ghost-blind/untested |
| 54 | 0.451 | [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) | Heuristic | sharp but interpretive |
| 55 | 0.451 | [Must-fail-for-DH acceptance test](#dh-acceptance) | Heuristic | sharp but interpretive |
| 56 | 0.423 | [BRST / Gupta–Bleuler physical quotient](#brst) | Analogy | background |
| 57 | 0.420 | [Two-point form g + iω ≥ 0](#two-point) | Restatement | RH-sharp |
| 58 | 0.419 | [Riemann hypothesis (target node)](#rh) | Open | true but ghost-blind/untested |
| 59 | 0.419 | [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) | Open | true but ghost-blind/untested |
| 60 | 0.419 | [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) | Open | true but ghost-blind/untested |
| 61 | 0.419 | [Hilbert–Pólya](#hilbert-polya) | Open | true but ghost-blind/untested |
| 62 | 0.400 | [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) | Numerical | RH-sharp |
| 63 | 0.392 | [Källén–Lehmann spectral positivity](#kallen-lehmann) | Analogy | sharp but interpretive |
| 64 | 0.392 | [Time delay (Wigner)](#time-delay) | Analogy | sharp but interpretive |
| 65 | 0.380 | [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) | Open | RH-sharp |
| 66 | 0.377 | [Displaced reference (subtracting the pole)](#displaced-reference) | Heuristic | background |
| 67 | 0.360 | [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) | Theorem | RH-sharp |
| 68 | 0.360 | [Krein collisions (how ghosts are born)](#krein-collision) | Theorem | RH-sharp |
| 69 | 0.360 | [Two partners of a zero (duality vs conjugation)](#two-partners) | Theorem | RH-sharp |
| 70 | 0.360 | [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) | Theorem | RH-sharp |
| 71 | 0.347 | [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) | Cited | true but ghost-blind/untested |
| 72 | 0.347 | [Automorphy defect (TAA Lemma 144)](#automorphy-defect) | Theorem | true but ghost-blind/untested |
| 73 | 0.347 | [Certified positivity windows](#certified-windows) | Numerical | true but ghost-blind/untested |
| 74 | 0.325 | [Hodge–Riemann bilinear relations](#hodge-riemann) | Theorem | true but ghost-blind/untested |
| 75 | 0.325 | [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) | Theorem | true but ghost-blind/untested |
| 76 | 0.325 | [√2 family](#sqrt2-family) | Theorem | true but ghost-blind/untested |
| 77 | 0.325 | [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) | Cited | true but ghost-blind/untested |
| 78 | 0.325 | [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) | Theorem | true but ghost-blind/untested |
| 79 | 0.325 | [Closed geodesics on the modular surface](#closed-geodesics) | Theorem | true but ghost-blind/untested |
| 80 | 0.325 | [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) | Theorem | true but ghost-blind/untested |
| 81 | 0.325 | [Selberg resonances](#selberg-resonances) | Theorem | true but ghost-blind/untested |
| 82 | 0.325 | [Arakelov geometry](#arakelov) | Cited | true but ghost-blind/untested |
| 83 | 0.325 | [Cusp ≠ archimedean place](#cusp-vs-infinity) | Theorem | true but ghost-blind/untested |
| 84 | 0.325 | [Density / volume reading](#density-volume) | Theorem | true but ghost-blind/untested |
| 85 | 0.325 | [F₁ base](#f1-base) | Cited | true but ghost-blind/untested |
| 86 | 0.325 | [Principalization](#principalization) | Theorem | true but ghost-blind/untested |
| 87 | 0.325 | [Spec ℤ is terminal](#spec-z-terminal) | Theorem | true but ghost-blind/untested |
| 88 | 0.325 | [Spinor/Clifford route](#spinor-route) | Theorem | true but ghost-blind/untested |
| 89 | 0.325 | [Weil Rosetta stone](#weil-rosetta) | Cited | true but ghost-blind/untested |
| 90 | 0.325 | [Cohesion (arena)](#cohesion) | Theorem | true but ghost-blind/untested |
| 91 | 0.325 | [Local-to-global failure](#local-global) | Theorem | true but ghost-blind/untested |
| 92 | 0.324 | [Kramers–Kronig relations](#kramers-kronig) | Analogy | background |
| 93 | 0.324 | [Gribov ambiguity](#gribov) | Analogy | background |
| 94 | 0.307 | [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) | Theorem | true but ghost-blind/untested |
| 95 | 0.307 | [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) | Theorem | true but ghost-blind/untested |
| 96 | 0.307 | [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) | Theorem | true but ghost-blind/untested |
| 97 | 0.307 | [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) | Theorem | true but ghost-blind/untested |
| 98 | 0.307 | [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) | Cited | true but ghost-blind/untested |
| 99 | 0.307 | [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) | Cited | true but ghost-blind/untested |
| 100 | 0.307 | [Archimedean place and Γ_ℝ factor](#archimedean-place) | Theorem | true but ghost-blind/untested |
| 101 | 0.307 | [Cusp forms & Petersson positivity](#cusp-forms-petersson) | Theorem | true but ghost-blind/untested |
| 102 | 0.307 | [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) | Cited | true but ghost-blind/untested |
| 103 | 0.307 | [Tate count / Picard number (ghost-blind)](#tate-count) | Theorem | true but ghost-blind/untested |
| 104 | 0.307 | [Hecke operators](#hecke) | Theorem | true but ghost-blind/untested |
| 105 | 0.307 | [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) | Numerical | true but ghost-blind/untested |
| 106 | 0.307 | [Archimedean thresholds a*](#arch-threshold) | Numerical | true but ghost-blind/untested |
| 107 | 0.307 | [Maass–Selberg relations](#maass-selberg) | Numerical | true but ghost-blind/untested |
| 108 | 0.267 | [Metaplectic / Kubota cocycle](#metaplectic) | Theorem | true but ghost-blind/untested |
| 109 | 0.267 | [The prime 2 as the wild place](#prime-two-wild) | Theorem | true but ghost-blind/untested |
| 110 | 0.267 | [Scattering unitarity |φ| = 1](#scattering-phi) | Theorem | true but ghost-blind/untested |
| 111 | 0.267 | [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) | Theorem | true but ghost-blind/untested |
| 112 | 0.267 | [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) | Theorem | true but ghost-blind/untested |
| 113 | 0.267 | [Half-density normalization |x|^{½}](#half-density) | Theorem | true but ghost-blind/untested |
| 114 | 0.267 | [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) | Cited | true but ghost-blind/untested |
| 115 | 0.267 | [Counts vs quadratic positivity](#count-positivity) | Theorem | true but ghost-blind/untested |
| 116 | 0.267 | [w₂ / Čech class (TAA Lemma 138)](#w2-cech) | Theorem | true but ghost-blind/untested |
| 117 | 0.267 | [Weight ladder (modular weights)](#weight-ladder) | Theorem | true but ghost-blind/untested |
| 118 | 0.267 | [Yoshida window positivity](#yoshida) | Cited | true but ghost-blind/untested |
| 119 | 0.267 | [Cup product / Poincaré duality pairing](#cup-product) | Theorem | true but ghost-blind/untested |
| 120 | 0.267 | [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) | Theorem | true but ghost-blind/untested |
| 121 | 0.267 | [Bost–Connes KMS states](#kms-bost-connes) | Cited | true but ghost-blind/untested |
| 122 | 0.267 | [Spin structure & theta characteristic](#spin-theta) | Theorem | true but ghost-blind/untested |
| 123 | 0.256 | ["Cocycles give structure, not sign"](#cocycle-principle) | Heuristic | background |
| 124 | 0.226 | [Buoyancy / Archimedes principle](#archimedes) | Analogy | background |
| 125 | 0.226 | [Heaviside RLGC line](#heaviside) | Analogy | background |
| 126 | 0.226 | [Mass-density positivity](#mass-density) | Analogy | background |
| 127 | 0.226 | [Distortionless line R/L = G/C](#distortionless) | Analogy | background |
| 128 | 0.212 | [Anomalous dispersion](#anomalous-dispersion) | Analogy | background |
| 129 | 0.181 | [Lamb cutoff](#lamb-cutoff) | Analogy | background |
| 130 | 0.181 | [Two different χ’s: Euler characteristic vs class-group character](#two-chis) | Analogy | background |
| 131 | 0.165 | [Standard conjectures (Hodge type)](#standard-conj) | Open | true but ghost-blind/untested |

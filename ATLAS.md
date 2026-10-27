# The RH Atlas — full public edition

Version 1.1 · 27 Oct 2026 · J. W. McGreevy; formalization by Grok Bot

> **The Riemann Hypothesis is NOT proved here.** This atlas is a classification of known structures, criteria and open problems, not a proof.

183 concepts · 529 typed relations · 10 missing pieces. Generated from `atlas.json` by `build_public_md.py`.

**Order.** Every section lists its entries in descending priority. Headers read `#rank · priority · name`. Priority comes from the Heuristic scoring layer described in [scores.md](scores.md): priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability. The scores are judgment calls, shown component by component so any reader can disagree with them.

**Organizing split.** Phase/unitarity structure (functional equations, |φ| = 1, cocycles, Hecke operators, cusp positivity) is *ghost-blind*: it holds equally for functions with zeros off the critical line, such as the Davenport–Heilbronn function. The *sign* of a spectral weight is *ghost-sensitive*, and for ζ that sign is RH.

**Labels.** Theorem · Restatement (equivalent to RH or to a known result) · Analogy · Conjecture · Open · Numerical · Heuristic · Cited (taken from the literature). References of the form “TAA Lemma N” point to the lemma series of the Thermodynamics of Arithmetic Action programme (see README.md for the published volumes). Citations marked “to verify” have not yet been checked against the source.

## Contents

- [Missing pieces](#missing-pieces)
- [Diagnostic quadrants](#diagnostic-quadrants)
- [Concepts by primary axis](#concepts-by-primary-axis)
  - [sign/positivity (Ax2)](#axis-sign-positivity-ax2) (32)
  - [no-go / refuted](#axis-no-go-refuted) (5)
  - [reference/pole/cusp](#axis-reference-pole-cusp) (18)
  - [Spec ℤ gap](#axis-spec-gap) (22)
  - [geometry over F_q](#axis-geometry-over-f-q) (12)
  - [physics analogue](#axis-physics-analogue) (22)
  - [numerics/certificate](#axis-numerics-certificate) (13)
  - [ghost-sensitive](#axis-ghost-sensitive) (11)
  - [structure/frame (Ax1)](#axis-structure-frame-ax1) (10)
  - [phase/unitarity (Ax3)](#axis-phase-unitarity-ax3) (25)
  - [restatement ⇔ RH](#axis-restatement-rh) (1)
  - [open target](#axis-open-target) (1)
  - [ghost-blind](#axis-ghost-blind) (1)
- [Index by rank](#index-by-rank)

## Missing pieces

These are the objects that, as far as this atlas can tell, would have to exist for a positivity proof of RH along the lines of the function-field case. Each is labelled Open. Listed in priority order.

### #9 · 0.700 · Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name) <a id="mp-flow-h1"></a>

**Label:** Open · **id:** `mp_flow_h1` · **quadrant:** RH-sharp

*In plain words:* For ℚ both cohomologies we can compute vanish (étale H¹ = 0, Arakelov Pic⁰ = a point), yet ψ(x) − x ≠ 0. The zeros need a cohomology relative to the scaling flow.

**Core.** Construct the middle term of Tate's split at |x| = 1 as an H¹ for Spec ℤ carrying (a) a Frobenius-type flow whose spectrum is the zeros (MP1–MP2; needs the Euler product, absent for DH) and (b) a cup product H¹ × H¹ → H² ≅ ℝ(−1) (MP3; absent for DH), and prove the cup square definite on the primitive part (MP4 = Hodge index/Rosati sign; the only positivity input). MP0: H⁰/H² = Tate boundary terms f(0), f̂(0) (DH: none). Deninger's axioms, TAA refinements MP0/MP4 (TAA Lemma 151 Conj 4.1). TAA Lemma 153: Connes's cokernel (TAA Lemma 153, correction 18) — its Hilbert space is automatically positive and sees only critical zeros; RH ⇔ nothing missing ⇔ global trace formula. Recorded as a precision of MP4, no new missing piece (MPU153).

**Formula.** N_n − (1 + qⁿ) = −Tr(Fⁿ | H¹) ↔ ψ(x) − x = −Σ_ρ x^ρ/ρ + …

**What is proved around it.** π₁ét(Spec ℤ) = 1 ⇒ H¹ét = 0 (TAA Lemma 140); curve row: N_n − (qⁿ + 1) = −Tr(Fⁿ | H¹) with relative Gram NSD (TAA Lemma 141 §1); Tr ↔ −(ψ − x) up to the s = 0 term and ARCH (TAA Lemma 142 corrections).

**Tests it must pass.** Must carry a positive structure (Ax2), not only the trace formula: the explicit formula alone is ghost-blind in data (TAA Lemma 143: ghost defect ≤ 1.9e−5, 0.08× noise).

**Also known as:** H¹_flow; Deninger H¹

**Axes:** missing piece, Spec ℤ gap, reference/pole/cusp

**TAA lemmas:** 140, 141, 142, 151, 153

**Scores (Heuristic):** gap significance 1.0 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [No étale H¹ for Spec ℤ](#no-etale-h1)
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)
- same mechanism as → [Deninger’s foliated program](#deninger)
- same mechanism as → [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) — subsumed as MP4 (TAA Lemma 151)
- same mechanism as → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) — sign half = MP4 (TAA Lemma 151)
- same mechanism as → [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) — contained as a test (TAA Lemma 151)

**Relations (incoming):** [Connes trace formula](#connes-trace) (same mechanism as); [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (analogue of); [Deninger’s foliated program](#deninger) (same mechanism as); [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) (same mechanism as); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (same mechanism as)

### #10 · 0.700 · Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ <a id="mp-ns-psi"></a>

**Label:** Open · **id:** `mp_ns_psi` · **quadrant:** RH-sharp

*In plain words:* An intersection theory on the square in which the Connes–Consani correspondences Ψ_λ are genuine classes outside the pole plane U, with enough sections that their growth sees s(f,f).

**Core.** Need NS ⊋ U with Ψ_λ, and #H⁰(±nD(f)) ≥ 2^{n² s(f,f)/2} (TAA Lemma 147). Decisive missing objects: H¹ on the square, an intersection theory putting Ψ_λ into an NS larger than U, and quadratic RR (TAA Lemma 147 (iv)).

**Formula.** #H⁰(±nD(f)) ≥ 2^{n² s(f,f)/2}

**What is proved around it.** Laurent piece of HZ ∧_𝕊 HZ: box count 2n² + 4n exact, but the quadratic coefficient 2αβ is the U-form ⇒ vacuous on degree-0 D(f) (TAA Lemma 147 Thm vac).

**Tests it must pass.** Quadratic growth must come from V₀ = U^⊥, not from U (Thm vac). Ghost-sensitive side is s(f,f), which must be negative for ζ and fail for DH (TAA Lemma 142, TAA Lemma 147).

**Also known as:** NS ⊋ U; Ψ_λ classes

**Axes:** missing piece, Spec ℤ gap, structure/frame (Ax1)

**TAA lemmas:** 147, 142, 150

**Scores (Heuristic):** gap significance 1.0 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

> ⚠ **Correction / caution.** TAA Lemma 150 Prop 2.3: classes at log n (n ≤ 90, disjoint hats) are ghost-blind — ζ, DH and inserted ghosts all give λ_max < 0; NS ⊋ U must use continuous translates or all ratios λ ∈ ℚ₊ (PSI-2).

**Relations (outgoing):**

- same mechanism as → [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square)
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — must leave U
- same mechanism as → [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff)

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (analogue of); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) (fails for)

### #11 · 0.700 · Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²) <a id="mp-castelnuovo"></a>

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

**Relations (incoming):** [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (special case of)

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

**Relations (incoming):** [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as)

### #13 · 0.700 · Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8) <a id="mp-d8"></a>

**Label:** Open · **id:** `mp_d8` · **quadrant:** RH-sharp

*In plain words:* The top substantive direction: a surface S over Spec ℤ with an ample class and a Riemann–Roch whose χ(nD) is quadratic, so that Hodge index follows as it does for curves.

**Core.** D8: surface + ample + RR for Spec ℤ — find S with χ(nD) quadratic and a Hodge index; obstacle: the collapse ℤ ⊗ ℤ = ℤ; sign = Weil form (TAA Lemma 140, TAA Lemma 141). Acceptance test (TAA Lemma 141): reconstruct the relative space and its form from independent constraints — (a) the hyperbolic plane U = ⟨𝟙, 𝕃⟩, (b) the scaling flow acting on it as diag(1, eᵗ), (c) ampleness at ∞, (d) RR/GRR with quadratic growth — then prove negativity on U^⊥. Any proof that uses the zeros, or defines the form by its negativity, fails. TAA Lemma 152: phrased as a 'degree' — a count (≥ 0) on arithmetic correspondences whose polarization is Weil's form; in Cayley–Klein terms the absolute of the arithmetic pairing must be imaginary (= MP4).

**What is proved around it.** Over F_q: surface + ample + RR ⇒ Hodge index (Segre 1937, Grothendieck 1958) (TAA Lemma 140). Spec ℤ ×_ℤ Spec ℤ = Spec ℤ (TAA Lemma 65). Arithmetic surfaces (curve × Spec O_K) satisfy V1–V3, but the relative part is Néron–Tate, not ζ (TAA Lemma 145).

**Tests it must pass.** Must pass the tautology test (no zeros, no definition by negativity, TAA Lemma 141) and the must-fail-for-DH test (TAA Lemma 147).

**Also known as:** D8; arithmetic surface with Hodge index

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 65, 140, 141, 145, 147, 152

**Scores (Heuristic):** gap significance 1.0 (nearest gap: surface + ample class + Riemann–Roch for Spec ℤ (D8)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.4 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)
- same mechanism as → [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr)
- special case of → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo)

**Relations (incoming):** [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as)

### #14 · 0.700 · Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square <a id="mp-quadratic-rr"></a>

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

### #15 · 0.700 · Missing: an inequality consequence of automorphy (SC-E / HS-1) <a id="mp-automorphy-ineq"></a>

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

### #16 · 0.700 · Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3) <a id="mp-brst"></a>

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
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1)

### #17 · 0.700 · Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin) <a id="mp-passivity-margin"></a>

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

### #18 · 0.700 · Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”) <a id="mp-rg5"></a>

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
| **sensitivity ≥ 0.8** (true for ζ) | RH-sharp: 61 | true but ghost-blind/untested: 98 |
| **sensitivity < 0.8** (interpretive) | sharp but interpretive: 7 | background: 17 |

### RH-sharp: true for ζ and fails for the fakes (61)

- #1 · 0.720 · [Weil positivity criterion](#weil-positivity) [Cited]
- #2 · 0.720 · [Davenport–Heilbronn function](#davenport-heilbronn) [Theorem]
- #3 · 0.720 · [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) [Cited]
- #4 · 0.720 · [Connes trace formula](#connes-trace) [Cited]
- #5 · 0.720 · [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) [Theorem]
- #6 · 0.720 · [Definite cup square / Krein one-liner](#definite-cup-square) [Theorem]
- #7 · 0.720 · [Lagarias/Hinkkanen criterion](#lagarias) [Cited]
- #8 · 0.720 · [Primitive part V₀ = U^⊥](#primitive-part) [Theorem]
- #9 · 0.700 · [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) [Open]
- #10 · 0.700 · [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) [Open]
- #11 · 0.700 · [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) [Open]
- #12 · 0.700 · [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) [Open]
- #13 · 0.700 · [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) [Open]
- #14 · 0.700 · [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) [Open]
- #15 · 0.700 · [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) [Open]
- #16 · 0.700 · [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) [Open]
- #17 · 0.700 · [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) [Open]
- #18 · 0.700 · [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) [Open]
- #19 · 0.600 · [Relative Gram matrix G_rel](#relative-gram) [Restatement]
- #20 · 0.600 · [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) [Restatement]
- #21 · 0.600 · [Passivity (positive real part)](#passivity) [Restatement]
- #22 · 0.600 · [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) [Restatement]
- #23 · 0.600 · [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) [Restatement]
- #24 · 0.580 · [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) [Numerical]
- #25 · 0.580 · [DH prime-side Gram test](#dh-prime-side-gram) [Numerical]
- #26 · 0.580 · [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) [Numerical]
- #27 · 0.580 · [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) [Numerical]
- #38 · 0.540 · [Rosati positivity](#rosati) [Theorem]
- #39 · 0.540 · [Castelnuovo–Severi inequality](#castelnuovo-severi) [Theorem]
- #40 · 0.540 · [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) [Theorem]
- #41 · 0.540 · [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) [Theorem]
- #42 · 0.540 · [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) [Theorem]
- #43 · 0.540 · [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) [Theorem]
- #44 · 0.540 · [Krein collisions (how ghosts are born)](#krein-collision) [Theorem]
- #45 · 0.540 · [RH for curves over F_q (Weil)](#fq-curves) [Cited]
- #46 · 0.540 · [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) [Theorem]
- #47 · 0.540 · [Decay rate ¼](#decay-quarter) [Theorem]
- #48 · 0.540 · [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) [Theorem]
- #49 · 0.540 · [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) [Theorem]
- #50 · 0.540 · [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) [Theorem]
- #51 · 0.540 · [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) [Theorem]
- #52 · 0.540 · [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) [Theorem]
- #53 · 0.540 · [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) [Cited]
- #54 · 0.540 · [Epstein zeta no-go](#epstein) [Theorem]
- #55 · 0.540 · [Compatible complex structure J commuting with Frobenius](#compatible-j) [Theorem]
- #56 · 0.540 · [de Branges spaces](#de-branges) [Cited]
- #57 · 0.540 · [de Bruijn–Newman constant Λ](#debruijn-newman) [Cited]
- #58 · 0.540 · [Hasse bound as a positive degree form](#hasse-pythagoras) [Theorem]
- #59 · 0.540 · [Li criterion](#li-criterion) [Cited]
- #60 · 0.540 · [Suzuki’s de Branges line from the prime side](#suzuki-line) [Cited]
- #61 · 0.540 · [Bagchi recurrence](#bagchi) [Cited]
- #83 · 0.420 · [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) [Restatement]
- #84 · 0.420 · [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) [Restatement]
- #85 · 0.420 · [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) [Restatement]
- #86 · 0.420 · [Two-point form g + iω ≥ 0](#two-point) [Restatement]
- #91 · 0.400 · [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) [Numerical]
- #103 · 0.360 · [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) [Theorem]
- #104 · 0.360 · [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) [Theorem]
- #105 · 0.360 · [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) [Theorem]
- #106 · 0.360 · [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) [Theorem]
- #107 · 0.360 · [Two partners of a zero (duality vs conjugation)](#two-partners) [Theorem]

### True for ζ but ghost-blind or untested against the fakes (98)

- #28 · 0.579 · [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) [Theorem]
- #29 · 0.579 · [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) [Theorem]
- #30 · 0.579 · [Ax1–Ax3 axioms (Yoneda specification)](#ax123) [Theorem]
- #31 · 0.579 · [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) [Cited]
- #32 · 0.579 · [Deninger’s foliated program](#deninger) [Cited]
- #33 · 0.579 · [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) [Theorem]
- #34 · 0.579 · [Parity argument: linear χ cannot see D²](#parity-linear-chi) [Theorem]
- #35 · 0.579 · [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) [Cited]
- #36 · 0.579 · [Tautology boundary (zero side vs prime side)](#tautology-boundary) [Theorem]
- #37 · 0.579 · [No étale H¹ for Spec ℤ](#no-etale-h1) [Theorem]
- #63 · 0.492 · [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) [Numerical]
- #64 · 0.492 · [Integer dimension over 𝕊 (minimal generators)](#dim-s) [Numerical]
- #65 · 0.452 · [Hodge index theorem](#hodge-index) [Theorem]
- #66 · 0.452 · [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) [Cited]
- #67 · 0.452 · [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) [Theorem]
- #68 · 0.452 · [Hodge–Riemann bilinear relations](#hodge-riemann) [Theorem]
- #69 · 0.452 · [Lax–Phillips scattering](#lax-phillips) [Cited]
- #70 · 0.452 · [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) [Theorem]
- #71 · 0.452 · [Connes–Consani sites](#connes-consani) [Cited]
- #72 · 0.452 · [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) [Cited]
- #73 · 0.452 · [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) [Cited]
- #74 · 0.452 · [Cartan involution / compact unitary group](#cartan-involution) [Theorem]
- #75 · 0.452 · [Maxwell construction / convex effective potential](#maxwell-effective-potential) [Theorem]
- #76 · 0.452 · [Pole plane / Tate poles at s = 0, 1](#pole-plane) [Theorem]
- #77 · 0.452 · [Products grow linearly (2n), not quadratically](#products-linear) [Theorem]
- #78 · 0.452 · [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) [Cited]
- #79 · 0.452 · [Yoneda specification](#yoneda) [Theorem]
- #87 · 0.419 · [Riemann hypothesis (target node)](#rh) [Open]
- #88 · 0.419 · [Hilbert–Pólya](#hilbert-polya) [Open]
- #89 · 0.419 · [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) [Open]
- #90 · 0.419 · [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) [Open]
- #95 · 0.387 · [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) [Numerical]
- #99 · 0.365 · [Cutoff saturation (class-number x is not the lever)](#cutoff-saturation) [Numerical]
- #100 · 0.365 · [LMFDB level-1 Maass list complete to T = 100](#lmfdb-maass-complete) [Numerical]
- #101 · 0.365 · [Null-calibrated GLS matched filter](#null-calibrated-gls) [Numerical]
- #102 · 0.365 · [Ghost onset depends on kernel width](#onset-kernel-dependence) [Numerical]
- #108 · 0.347 · [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) [Cited]
- #109 · 0.347 · [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) [Theorem]
- #110 · 0.347 · [Automorphy defect (TAA Lemma 144)](#automorphy-defect) [Theorem]
- #111 · 0.347 · [Certified positivity windows](#certified-windows) [Numerical]
- #112 · 0.325 · [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) [Theorem]
- #113 · 0.325 · [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) [Theorem]
- #114 · 0.325 · [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) [Theorem]
- #115 · 0.325 · [√2 family](#sqrt2-family) [Theorem]
- #116 · 0.325 · [Closed geodesics on the modular surface](#closed-geodesics) [Theorem]
- #117 · 0.325 · [Cusp ≠ archimedean place](#cusp-vs-infinity) [Theorem]
- #118 · 0.325 · [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) [Cited]
- #119 · 0.325 · [Selberg resonances](#selberg-resonances) [Theorem]
- #120 · 0.325 · [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) [Theorem]
- #121 · 0.325 · [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) [Theorem]
- #122 · 0.325 · [Arakelov geometry](#arakelov) [Cited]
- #123 · 0.325 · [Density / volume reading](#density-volume) [Theorem]
- #124 · 0.325 · [F₁ base](#f1-base) [Cited]
- #125 · 0.325 · [Principalization](#principalization) [Theorem]
- #126 · 0.325 · [Spec ℤ is terminal](#spec-z-terminal) [Theorem]
- #127 · 0.325 · [Spinor/Clifford route](#spinor-route) [Theorem]
- #128 · 0.325 · [Weil Rosetta stone](#weil-rosetta) [Cited]
- #129 · 0.325 · [Cohesion (arena)](#cohesion) [Theorem]
- #130 · 0.325 · [Local-to-global failure](#local-global) [Theorem]
- #133 · 0.307 · [Half Tate twist ℚ(½)](#half-tate-twist) [Theorem]
- #134 · 0.307 · [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) [Theorem]
- #135 · 0.307 · [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) [Theorem]
- #136 · 0.307 · [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) [Cited]
- #137 · 0.307 · [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) [Theorem]
- #138 · 0.307 · [Archimedean place and Γ_ℝ factor](#archimedean-place) [Theorem]
- #139 · 0.307 · [Cup product / Poincaré duality pairing](#cup-product) [Theorem]
- #140 · 0.307 · [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) [Cited]
- #141 · 0.307 · [Cusp forms & Petersson positivity](#cusp-forms-petersson) [Theorem]
- #142 · 0.307 · [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) [Theorem]
- #143 · 0.307 · [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) [Theorem]
- #144 · 0.307 · [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) [Cited]
- #145 · 0.307 · [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) [Cited]
- #146 · 0.307 · [Tate count / Picard number (ghost-blind)](#tate-count) [Theorem]
- #147 · 0.307 · [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) [Cited]
- #148 · 0.307 · [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) [Cited]
- #149 · 0.307 · [Hecke operators](#hecke) [Theorem]
- #150 · 0.307 · [Bost–Connes KMS states](#kms-bost-connes) [Cited]
- #151 · 0.307 · [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) [Numerical]
- #152 · 0.307 · [Maass–Selberg relations](#maass-selberg) [Numerical]
- #153 · 0.307 · [Archimedean thresholds a*](#arch-threshold) [Numerical]
- #154 · 0.267 · [Metaplectic / Kubota cocycle](#metaplectic) [Theorem]
- #155 · 0.267 · [Half-density normalization |x|^{½}](#half-density) [Theorem]
- #156 · 0.267 · [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) [Theorem]
- #157 · 0.267 · [The prime 2 as the wild place](#prime-two-wild) [Theorem]
- #158 · 0.267 · [Scattering unitarity |φ| = 1](#scattering-phi) [Theorem]
- #159 · 0.267 · [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) [Theorem]
- #160 · 0.267 · [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) [Cited]
- #161 · 0.267 · [Counts vs quadratic positivity](#count-positivity) [Theorem]
- #162 · 0.267 · [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) [Theorem]
- #163 · 0.267 · [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) [Theorem]
- #164 · 0.267 · [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) [Theorem]
- #165 · 0.267 · [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) [Theorem]
- #166 · 0.267 · [Weight ladder (modular weights)](#weight-ladder) [Theorem]
- #167 · 0.267 · [Yoshida window positivity](#yoshida) [Cited]
- #168 · 0.267 · [w₂ / Čech class (TAA Lemma 138)](#w2-cech) [Theorem]
- #169 · 0.267 · [Sector map w = e^{iπs/2}](#sector-map-w) [Theorem]
- #170 · 0.267 · [Spin structure & theta characteristic](#spin-theta) [Theorem]
- #183 · 0.165 · [Standard conjectures (Hodge type)](#standard-conj) [Open]

### Separates ζ from the fakes, but the claim itself is interpretive (Analogy/Heuristic) (7)

- #62 · 0.532 · [Gain lines (active media)](#gain-line) [Analogy]
- #80 · 0.451 · [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) [Heuristic]
- #81 · 0.451 · [Must-fail-for-DH acceptance test](#dh-acceptance) [Heuristic]
- #92 · 0.392 · [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) [Analogy]
- #93 · 0.392 · [Time delay (Wigner)](#time-delay) [Analogy]
- #94 · 0.392 · [Källén–Lehmann spectral positivity](#kallen-lehmann) [Analogy]
- #173 · 0.253 · [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) [Analogy]

### Background: interpretive and not separating (17)

- #82 · 0.423 · [BRST / Gupta–Bleuler physical quotient](#brst) [Analogy]
- #96 · 0.377 · [Displaced reference (subtracting the pole)](#displaced-reference) [Heuristic]
- #97 · 0.377 · [Band criterion γ < 2T_M](#band-criterion) [Heuristic]
- #98 · 0.377 · [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) [Heuristic]
- #131 · 0.324 · [Kramers–Kronig relations](#kramers-kronig) [Analogy]
- #132 · 0.324 · [Gribov ambiguity](#gribov) [Analogy]
- #171 · 0.256 · ["Cocycles give structure, not sign"](#cocycle-principle) [Heuristic]
- #172 · 0.256 · [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) [Heuristic]
- #174 · 0.226 · [Buoyancy / Archimedes principle](#archimedes) [Analogy]
- #175 · 0.226 · [Distortionless line R/L = G/C](#distortionless) [Analogy]
- #176 · 0.226 · [Heaviside RLGC line](#heaviside) [Analogy]
- #177 · 0.226 · [Mass-density positivity](#mass-density) [Analogy]
- #178 · 0.212 · [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) [Analogy]
- #179 · 0.212 · [Klein–Gordon indefinite charge](#klein-gordon-charge) [Analogy]
- #180 · 0.212 · [Anomalous dispersion](#anomalous-dispersion) [Analogy]
- #181 · 0.181 · [Lamb cutoff](#lamb-cutoff) [Analogy]
- #182 · 0.181 · [Two different χ’s: Euler characteristic vs class-group character](#two-chis) [Analogy]

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

**TAA lemmas:** 1, 17, 98, 103, 142, 152

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** The zero-side check is tautological (TAA Lemma 142); only the prime side with no zeros is a test.

> ⚠ **Correction / caution.** "Q = LP + positive" is false (TAA Lemma 8).

> ⚠ **Correction / caution.** Definition, not source (TAA Lemma 152 §3): Weil's criterion ⇔ RH, so it cannot by itself supply the positivity.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Weil 1952
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — TAA Lemma 142: Weil form = relative intersection matrix on translates
- same mechanism as → [Hodge index theorem](#hodge-index) — Spec ℤ analogue of Hodge index on V₀ (TAA Lemma 91)
- same mechanism as → [Two-point form g + iω ≥ 0](#two-point) — TAA Lemma 103: g + iω ≥ 0 ⇔ Weil

**Relations (incoming):** [Connes trace formula](#connes-trace) (same mechanism as); [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (implies); [Relative Gram matrix G_rel](#relative-gram) (same mechanism as); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (lives in); [Tautology boundary (zero side vs prime side)](#tautology-boundary) (same mechanism as); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (same mechanism as); [Li criterion](#li-criterion) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (lives in); [Maxwell construction / convex effective potential](#maxwell-effective-potential) (analogue of); [Two-point form g + iω ≥ 0](#two-point) (same mechanism as); [Källén–Lehmann spectral positivity](#kallen-lehmann) (same mechanism as); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (same mechanism as); [Archimedean place and Γ_ℝ factor](#archimedean-place) (lives in)

### #6 · 0.720 · Definite cup square / Krein one-liner <a id="definite-cup-square"></a>

**Label:** Theorem · **id:** `definite_cup_square` · **quadrant:** RH-sharp

*In plain words:* Positivity is put in by a definite Hermitian square: a flow that scales it forces every eigenvalue onto the line, and only null vectors (ghosts) can escape.

**Core.** If ⟨φᵗx, φᵗy⟩ = eᵗ⟨x,y⟩ for a Hermitian form, an eigenvector with eigenvalue e^{tρ} has Re ρ = ½ or is null; ρ pairs only with 1 − ρ̄ (Krein-neutral (1,1) block); definite ⇒ all on the line (TAA Lemma 152 Prop 2.1; NUM 2.3e−16). A bilinear cup pairing only pairs ρ with 1 − ρ (= functional equation, ghost-blind; Cor 2.2): Hermitian needs conjugation + Weil operator/polarization. Over F_q: the definite form is the Rosati trace form on End⁰(J)⊗ℝ (ππ′ = q ⇒ |σ(π)|² = q), equivalently Hodge index on NS(C×C) — not a Hermitian form on H¹_ét (TAA Lemma 152, correction 1). For ζ: MP4 (TAA Lemma 151), the only positivity input. On E×E the projection D_n = Γ_n − qⁿe₁ − e₂ gives D_m·D_n = −Σ αᵢⁿ βᵢᵐ, β = q/α: Hermitian iff |α| = √q (TAA Lemma 152 Prop 4.3).

**Formula.** e^{t(ρ+σ̄)} h(v,w) = eᵗ h(v,w)

**Also known as:** Krein one-liner; Hermitian vs bilinear

**Axes:** sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** Over F_q there is no positive Hermitian form on H¹_ét (TAA Lemma 152, correction 1).

> ⚠ **Correction / caution.** A bilinear (cup) pairing gives only the FE (TAA Lemma 152, correction 2).

**Relations (outgoing):**

- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision) — Krein-neutral pair = ghost
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP4
- same mechanism as → [Rosati positivity](#rosati) — F_q form
- lives in → [Cup product / Poincaré duality pairing](#cup-product) — needs conjugation + polarization
- same mechanism as → [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square)

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as)

### #7 · 0.720 · Lagarias/Hinkkanen criterion <a id="lagarias"></a>

**Label:** Cited · **id:** `lagarias` · **quadrant:** RH-sharp

*In plain words:* RH ⇔ the log-derivative of ξ has positive real part to the right of the line.

**Core.** Lagarias 1999 (1.5), credited to Hinkkanen: RH ⇔ Re ξ′/ξ(s) > 0 on Re s > ½ (TAA Lemmas 17, 146).

**Formula.** RH ⇔ Re ξ′/ξ(s) > 0 (Re s > ½)

**Numbers.** DH: Re ξ′/ξ = −66.8

**Also known as:** Re ξ′/ξ > 0; Hinkkanen

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 17, 146, 154

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Passivity (positive real part)](#passivity)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH violates it
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero)

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (same mechanism as); [Passivity (positive real part)](#passivity) (same mechanism as); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as)

### #19 · 0.600 · Relative Gram matrix G_rel <a id="relative-gram"></a>

**Label:** Restatement · **id:** `relative_gram` · **quadrant:** RH-sharp

*In plain words:* Take a test function, translate it, and form the matrix of pairings after removing the pole plane. RH ⇔ this matrix is positive (semi)definite for all choices.

**Core.** TAA Lemma 149: prime side to x = e^16, exact u-space ARCH; hats h = 0.025, all 316 spans 0.25–16: ζ λ_max(G_rel) < 0 everywhere (−2.31e−6, −5.13e−9, −4.90e−11, −2.78e−11, −6.45e−12 at L = 1, 4, 8, 12, 16), n₊(C) = 1; roundoff floor 5e−15 (not a certificate).

**Formula.** G_rel ⪰ 0 ∀ f, t_i ⇔ RH

**Numbers.** λ_max(16) = −6.45e−12 (h=0.025), −2.69e−11 at 15.95 (h=0.05) · floor ≤ 4.9e−15 · plateau ≈ −2.8e−11 on L ∈ [11,14]

**Also known as:** relative intersection matrix; Gram on translates; Weil Gram

**Axes:** sign/positivity (Ax2), ghost-sensitive, reference/pole/cusp, restatement ⇔ RH, Spec ℤ gap

**TAA lemmas:** 142, 10, 127, 149

**Scores (Heuristic):** gap significance 0.8 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Using the zero side to "check" it is tautological.

> ⚠ **Correction / caution.** Negative sign is predicted both by RH and by any ghost with δ below the detection threshold (δ ≈ 0.01 at γ 85.7 by L = 16).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — TAA Lemma 142
- same mechanism as → [Weil positivity criterion](#weil-positivity)
- analogue of → [Primitive part V₀ = U^⊥](#primitive-part) — Gram on U^⊥
- lives in → [Davenport–Heilbronn function](#davenport-heilbronn) — [tested-by] DH prime side positive from L = 3.85 (TAA Lemma 149)

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as); [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (analogue of); [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (same mechanism as); [DH prime-side Gram test](#dh-prime-side-gram) (special case of); [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) (same mechanism as); [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) (lives in); [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) (same mechanism as); [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as)

### #20 · 0.600 · Verschiebung as the positive adjoint of Frobenius (F† = V) <a id="verschiebung-positive-adjoint"></a>

**Label:** Restatement · **id:** `verschiebung_positive_adjoint` · **quadrant:** RH-sharp

*In plain words:* Frobenius has a partner map going the other way, Verschiebung, with F·V = q; the true statement behind RH is that V is the mirror image (adjoint) of F for a positive inner product, and J. W. McGreevy’s animation runs this pairing continuously.

**Core.** [T] On an elliptic curve over F_q: FV = VF = q and F + V = a (trace); deg(m − nF) = (m − nF)(m − nV) = m² − a·mn + q·n² (the norm conic); a² < 4q ⇒ ellipse and V = F̄ (complex conjugate eigenvalues), so |α|² = αᾱ = FV = q: Hasse; a² = 4q double line; a² > 4q hyperbola, F, V two different real numbers (a fake). Dieudonné modules W(k){F,V}/(FV − p); Rosati: π∘π† = q ⇒ π† = qπ⁻¹ = V (TAA Lemma 115 §6.1, Milne AV Lemma 1.2 as cited there). [R] The ghost-sensitive statement is V = F† for a POSITIVE form (Rosati trace form): ⟨Fx,Fy⟩ = q⟨x,y⟩ (Krein one-liner, definite_cup_square); for a finite model RH ⇔ there is a positive involution with F† = V (TAA Lemma 115 §6.3, via TAA Lemma 113 Thm 2.1). Flow form: adjoint = inverse up to eᵗ ⇔ Re ρ = ½. On the Eisenstein constant term Ve = Fr̄ on y^s iff Re s = ½ (TAA Lemma 115; a Ramanujan statement for E(·,s), not RH for ζ). [Ghost-blind] FV = q alone is pure algebra: any fake with char. poly x² − ax + q has V = a − F with FV = q (TAA Lemma 113 Thm 5.1 via TAA Lemma 115). TAA Lemma 117 §4: with the pairing ρ ↔ 1 − ρ̄, Ve = Fr† always; an on-line zero is self-paired (definite square), an off-line pair spans a hyperbolic plane where p^{−½}Fr is a boost of rapidity δ log p. TAA Lemma 121: Π_p′ (transpose of Frobenius) is Verschiebung, Π_pΠ_p′ = p; mod p, Φ_p = 0 is graph of j ↦ j^p ∪ its transpose (Kronecker congruence). [A] J. W. McGreevy’s animation as the dynamic F ↔ V sweep: the half turn swaps F and V; running a through a² < 4q, = 4q, > 4q is lobe → wedge → hyperbola.

**Formula.** FV = VF = q; deg(m − nF) = (m − nF)(m − nV); F† = V ⇔ |α| = √q

**Numbers.** TAA Lemma 115: s = ½ + 7.3i, p = 3: Fr = −0.28601 + 1.70827i, Ve = conj(Fr), Fr·Ve = 3 · TAA Lemma 115: T_pE = (p^{s−½} + p^{½−s})E checked to 1e−30

**Also known as:** F ↔ V swap; Rosati adjoint of Frobenius; FV = VF = q

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 115, 117, 121, 152, 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 0.8 → priority 0.600

> ⚠ **Correction / caution.** FV = q is ghost-blind (fakes have it); only “V is the adjoint for a POSITIVE form” is ghost-sensitive.

> ⚠ **Correction / caution.** TAA Lemma 115 TAA Lemma 115, correction 12: “Verschiebung drives the birth” holds only as a parameter flow (V_N: y ↦ Ny is not Γ-invariant), not as a symmetry of the zero set.

> ⚠ **Correction / caution.** TAA Lemma 115: on the Eisenstein side “Ve = Fr†” restates Ramanujan/temperedness for E(·,s), not RH for ζ.

> ⚠ **Correction / caution.** The animation reading is an Analogy; its code is lost and per-frame autoscaling could fake a flip (TAA Lemma 152, correction 11).

> ❓ **Not verified / open.** No new lemma build: assembled from TAA Lemma 115/TAA Lemma 117/TAA Lemma 121/TAA Lemma 152/TAA Lemma 153; Milne AV Lemma 1.2 as cited in TAA Lemma 115.

**Relations (outgoing):**

- same mechanism as → [Rosati positivity](#rosati) — π† = V
- same mechanism as → [Definite cup square / Krein one-liner](#definite-cup-square) — ⟨Fx,Fy⟩ = q⟨x,y⟩
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — deg(m − nF) = (m − nF)(m − nV)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — finite model: RH ⇔ positive involution with F† = V (TAA Lemma 115 §6.3); for ζ a Restatement of MP4
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — adjoint = inverse up to eᵗ
- same mechanism as → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — off-line pair: p^{−½}Fr is a boost (TAA Lemma 117)
- same mechanism as → [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) — half turn = F ↔ V swap
- analogue of → [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) — dynamic F ↔ V sweep
- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — fakes keep FV = q but V ≠ F†
- same mechanism as → [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) — Frob/√q elliptic ⇔ V = F̄

**Relations (incoming):** [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #22 · 0.600 · Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts) <a id="cayley-klein-absolute"></a>

**Label:** Restatement · **id:** `cayley_klein_absolute` · **quadrant:** RH-sharp

*In plain words:* A geometry is definite exactly when its absolute (the conic at infinity) has no real points; real points give boosts and null directions, i.e. ghosts.

**Core.** Every projective metric = cross-ratio with a fixed conic, the absolute (Cayley 1859, Klein 1871). Imaginary absolute ⇔ definite form ⇔ rotations, eigenvalues e^{±iθ} on the unit circle, no real null vectors. Real absolute (null rays at ±45°) ⇔ indefinite ⇔ boosts, eigenvalues e^{±η}, rapidity η = ½ log CR(ℓ₁,ℓ₂; N₊,N₋) (TAA Lemma 152 NUM 4.4e−16), real null vectors = Krein-neutral pairs = ghosts. Gap restated: is the absolute of the arithmetic pairing imaginary? Over F_q yes (Hodge index); for ζ this is MP4 ⇔ RH. J. W. McGreevy's withdrawn 45° null rays are the picture of the failure mode.

**Numbers.** rapidity identity 4.4e−16

**Also known as:** Cayley–Klein metric; imaginary vs real absolute; rotations vs boosts

**Axes:** sign/positivity (Ax2), restatement ⇔ RH, structure/frame (Ax1)

**TAA lemmas:** 152, 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Cayley 1859 and Klein 1871: bibliographic data verified via Crossref only.

> ⚠ **Correction / caution.** Restatement: it re-expresses Weil positivity; it supplies no positivity.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — imaginary absolute of the arithmetic pairing = MP4 ⇔ RH (Weil)
- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision) — real null vectors = Krein-neutral pairs
- same mechanism as → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — RH = exclude boosts (TAA Lemma 42/TAA Lemma 58/TAA Lemma 98)
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP4 = imaginary absolute
- same mechanism as → [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) — Klein model; trace classification

**Relations (incoming):** [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (same mechanism as); [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) (special case of)

### #23 · 0.600 · Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0 <a id="rr-strategy-sff"></a>

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

**Relations (incoming):** [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (same mechanism as); [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (same mechanism as)

### #30 · 0.579 · Ax1–Ax3 axioms (Yoneda specification) <a id="ax123"></a>

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

### #38 · 0.540 · Rosati positivity <a id="rosati"></a>

**Label:** Theorem · **id:** `rosati` · **quadrant:** RH-sharp

*In plain words:* An involution † on endomorphisms with Tr(φφ†) > 0 — like a squared length that is never negative. With ππ† = q it forces |α| = √q.

**Core.** Tr(φφ†) > 0 on End⁰(J); ππ† = q ⇒ |α| = √q (Milne AV 14.3). On R[F]: Rosati PD ⇔ RH-model ⇔ ∃ compatible J with [J,F] = 0; n₋ = #real pairs + 2#quartets (TAA Lemma 106). Over ℚ: Rosati = Weil form is a restatement.

**Formula.** Tr(φφ†) > 0; ππ† = q

**Numbers.** E^n over F₅: Tr = 2ΣN(φ_ij) > 0, 3000/3000 (TAA Lemma 136) · signatures true (2,0),(4,0),(8,0); ghost (1,1); quartet (2,2)

**Also known as:** Rosati involution †; Tr(φφ†) > 0; positive involution; Ax2∧Ax3

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 84, 99, 106, 133, 136, 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** |φ| = 1 on Re s = ½ is only the adjoint half ππ† = q (Ax3), ghost-blind.

> ⚠ **Correction / caution.** Positivity over F_q is geometric, from intersection numbers, not arithmetic (TAA Lemma 106, correction 1).

**Relations (outgoing):**

- same mechanism as → [Castelnuovo–Severi inequality](#castelnuovo-severi) — TAA Lemma 133
- special case of → [Cartan involution / compact unitary group](#cartan-involution) — Rosati = Cartan θ_J on commutant (TAA Lemma 99)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — over ℚ
- analogue of → [Mass-density positivity](#mass-density) — mass-like single positivity
- lives in → [RH for curves over F_q (Weil)](#fq-curves) — proved setting
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — OS shape; positivity from polarization

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (same mechanism as); [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (special case of); [Castelnuovo–Severi inequality](#castelnuovo-severi) (same mechanism as); [Hasse bound as a positive degree form](#hasse-pythagoras) (special case of); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Cartan involution / compact unitary group](#cartan-involution) (same mechanism as); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of); [Mass-density positivity](#mass-density) (analogue of)

### #39 · 0.540 · Castelnuovo–Severi inequality <a id="castelnuovo-severi"></a>

**Label:** Theorem · **id:** `castelnuovo_severi` · **quadrant:** RH-sharp

*In plain words:* On the surface C×C a class cannot be "too timelike" relative to the two fibre directions; applied to Frobenius graphs it gives RH for curves.

**Core.** D² ≤ 2(D·f₁)(D·f₂); def(D) = 2d₁d₂ − D² = −(D°)² = Tr_{H¹}(α_D α_D†) (C–S = Rosati, TAA Lemma 133). Weil mF + n: −(2gqm² + 2amn + 2gn²) ≤ 0 ⇔ a² ≤ 4g²q (TAA Lemma 125). TAA Lemma 152 §3: the proved source of positivity over F_q (Weil 1948, BIB): surface → ample → RR → Hodge index; Weil's criterion is the definition, not the source.

**Formula.** D² ≤ 2(D·f₁)(D·f₂)

**Numbers.** primitive Gram det 4p − a² > 0 (29 primes, TAA Lemma 133)

**Also known as:** C–S; reverse Cauchy–Schwarz; def(D)

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 14, 114, 125, 133, 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** A “−2Tr” formula holds only on the primitive part with the g-dimensional trace.

**Relations (outgoing):**

- same mechanism as → [Rosati positivity](#rosati) — TAA Lemma 133: C–S = Rosati
- special case of → [Hodge index theorem](#hodge-index) — C–S ⇔ Hodge index on ⟨f₁,f₂,D⟩
- analogue of → [Buoyancy / Archimedes principle](#archimedes) — buoyancy reading
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — relative to the null rays
- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) — the source chain

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (same mechanism as); [Rosati positivity](#rosati) (same mechanism as); [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (special case of); [RH for curves over F_q (Weil)](#fq-curves) (implies); [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) (analogue of); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (fails for); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (fails for); [Buoyancy / Archimedes principle](#archimedes) (analogue of)

### #45 · 0.540 · RH for curves over F_q (Weil) <a id="fq-curves"></a>

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

**Relations (incoming):** [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (lives in); [Rosati positivity](#rosati) (lives in); [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) (analogue of); [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) (analogue of); [Weil Rosetta stone](#weil-rosetta) (analogue of)

### #55 · 0.540 · Compatible complex structure J commuting with Frobenius <a id="compatible-j"></a>

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

### #56 · 0.540 · de Branges spaces <a id="de-branges"></a>

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

### #58 · 0.540 · Hasse bound as a positive degree form <a id="hasse-pythagoras"></a>

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

### #59 · 0.540 · Li criterion <a id="li-criterion"></a>

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

### #60 · 0.540 · Suzuki’s de Branges line from the prime side <a id="suzuki-line"></a>

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

### #65 · 0.452 · Hodge index theorem <a id="hodge-index"></a>

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

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as); [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (special case of); [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) (lives in); [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) (implies); [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (same mechanism as); [Parity argument: linear χ cannot see D²](#parity-linear-chi) (fails for); [Castelnuovo–Severi inequality](#castelnuovo-severi) (special case of); [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) (analogue of); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Standard conjectures (Hodge type)](#standard-conj) (special case of)

### #66 · 0.452 · Osterwalder–Schrader reflection positivity <a id="os-reflection-positivity"></a>

**Label:** Cited · **id:** `os_reflection_positivity` · **quadrant:** true but ghost-blind/untested

*In plain words:* 

**Core.** TAA Lemma 25 Prop 6.3: OS-RP for Weil with θu = −u FAILS (atom δ_{log2}: RP ≍ −1/ε, −2.50, −11.08, −35.58, −121.35 at ε = 0.1…0.003); OS gives H ≥ 0 semigroup, Weil a unitary group. TAA Lemma 32: RH ⇔ |OS_a| ≤ Q on E₊(a) (domination form); OS-RP false unconditionally. TAA Lemma 42 Thm 2.1/2.2/4.4 (Hankel ≠ Toeplitz; orthogonality pincer). TAA Lemma 47: reflection ⇒ FE, positivity needs polarization. Closest literature: Neeb–Ólafsson RP ↔ Lax–Phillips. TAA Lemma 151: failure at log 2 = smallest prime, not wildness; half density = the reflection (unitary) half of OS. TAA Lemma 153 (claim 6): for Gaussian data RP ⇔ the reflected form B(f,g) = ⟨θf,g⟩ is PSD on the positive-time space ⇔ every 2-plane restriction is an ellipse or degenerate (trivially, since 1-dim restrictions suffice); NOT ⇔ 'the blocks of one chosen decomposition are ellipses' unless they are B-orthogonal (TAA Lemma 153, correction 6). TAA Lemma 153's R-symmetric tilt blocks are reflection pairs (f₊, f₋ = Rf₊).

**Also known as:** OS reflection positivity

**Axes:** sign/positivity (Ax2), no-go / refuted, physics analogue

**TAA lemmas:** 25, 32, 42, 47, 151, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** As stated (OS_a ≥ 0) it is false for ζ; only the domination |OS_a| ≤ Q is RH-equivalent.

**Relations (outgoing):**

- same mechanism as → [Weil positivity criterion](#weil-positivity) — degenerate OS form (TAA Lemma 32)
- analogue of → [Rosati positivity](#rosati) — θ ↔ Rosati, positivity from polarization
- analogue of → [BRST / Gupta–Bleuler physical quotient](#brst) — OS reconstruction ↔ Gupta–Bleuler quotient
- same mechanism as → [Lax–Phillips scattering](#lax-phillips) — Neeb–Ólafsson
- analogue of → [Klein–Gordon indefinite charge](#klein-gordon-charge)
- analogue of → [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) — regularity failure (H)
- analogue of → [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square)
- analogue of → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) — RP kernel with H² spectrum z would force z ≥ 0
- analogue of → [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic)

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (analogue of); [Rosati positivity](#rosati) (analogue of); [Half Tate twist ℚ(½)](#half-tate-twist) (analogue of); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (analogue of); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of)

### #67 · 0.452 · Legendre strata: support function / Fenchel–Moreau as a definiteness detector <a id="legendre-support-function"></a>

**Label:** Theorem · **id:** `legendre_support_function` · **quadrant:** true but ghost-blind/untested

*In plain words:* All the information about a convex curve sits in the intercepts of its tangent lines; the Legendre transform returns the curve exactly when it is convex, so it is a definiteness test.

**Core.** Tangent lines carry a convex curve: the support function h(θ) = sup_{x∈K}⟨x,u_θ⟩ determines a closed convex K (Minkowski; BIB). For f = ½xᵀAx the Legendre transform is ½pᵀA⁻¹p, finite everywhere iff A ≻ 0; if A has a negative eigenvalue f* ≡ +∞ (on a box |x| ≤ R it grows with R: TAA Lemma 153 NUM). Fenchel–Moreau: f** = f iff f is convex lsc (BIB). Support-function window of a conic region: 2π for an ellipse; for one convex hyperbola branch exactly 2·atan√(|λ₋|/λ₊) < π (NUM 64.8° vs 64.62° predicted for λ = 1, −0.4); for both branches (or the region xᵀAx ≤ 1 with A indefinite) empty; jump 2π → 0 at det = 0. J. W. McGreevy's 'Legendre type concept' is this.

**Formula.** h_K(u) = sup⟨x,u⟩; (½xᵀAx)* = ½pᵀA⁻¹p iff A ≻ 0

**Numbers.** hyperbola-branch window 2 atan√(|λ₋|/λ₊): 64.8° (grid) vs 64.62°

**Also known as:** support function; Fenchel–Moreau; y-intercepts of tangents

**Axes:** sign/positivity (Ax2), structure/frame (Ax1)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) — ellipse ⇔ imaginary absolute ⇔ full window
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — window = conic type
- lives in → [Weil positivity criterion](#weil-positivity) — applied blockwise

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [Maxwell construction / convex effective potential](#maxwell-effective-potential) (same mechanism as); [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) (special case of); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as)

### #68 · 0.452 · Hodge–Riemann bilinear relations <a id="hodge-riemann"></a>

**Label:** Theorem · **id:** `hodge_riemann` · **quadrant:** true but ghost-blind/untested

*In plain words:* Pairing a holomorphic form with its own complex conjugate gives a positive number: a genuine |amplitude|².

**Core.** HR holds on every compact Riemann surface; HR form = 2 × Petersson (TAA Lemma 134). Positivity = complex structure inserted (Weil operator C = i^{p−q}). Hecke self-adjointness gives a_p ∈ ℝ, not |a_p| ≤ 2√p.

**Formula.** i ∫ α ∧ ᾱ = 2∫|f|² > 0

**Also known as:** HR form; i∫α∧ᾱ > 0; Riemann form; Petersson positivity

**Axes:** sign/positivity (Ax2), geometry over F_q

**TAA lemmas:** 40, 102, 134, 139, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Column 2 (F_q) never fully inherited the HR sign; Castelnuovo replaces it algebraically (TAA Lemma 140).

**Relations (outgoing):**

- special case of → [Cup product / Poincaré duality pairing](#cup-product) — cup with the conjugate through the Hodge structure
- same mechanism as → [Rosati positivity](#rosati) — Rosati = H-adjoint (TAA Lemma 134)
- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) — positivity needs C = i^{p−q}

**Relations (incoming):** [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (same mechanism as); [Cusp forms & Petersson positivity](#cusp-forms-petersson) (same mechanism as); [Hecke operators](#hecke) (same mechanism as)

### #73 · 0.452 · Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r² <a id="selberg-eigenvalue-mass-shell"></a>

**Label:** Cited · **id:** `selberg_eigenvalue_mass_shell` · **quadrant:** true but ghost-blind/untested

*In plain words:* The Laplacian on the modular surface is positive, which forces its eigenvalues onto a line; whether the first eigenvalue is at least ¼ for all congruence groups is still open.

**Core.** Δ ≥ 0 on L²(Γ∖ℍ), λ = s(1−s) real ⇒ s ∈ [0,1] or Re s = ½; for SL₂(ℤ) λ₁ = ¼ + 9.53369…² ≈ 91.14 > ¼, so the spectral zeros of Selberg's zeta (cusp forms) lie on Re s = ½. Selberg's conjecture λ₁ ≥ ¼ for congruence subgroups: open; Selberg 3/16 (1965), Kim–Sarnak 975/4096 = ¼ − (7/64)² ≈ 0.2380 (appendix to Kim, JAMS 16 (2003) 139–183; bib data Crossref, bound via secondary sources). Shape analogy: ρ(1−ρ) = ¼ + γ² ≥ ¼ real ⇔ ρ on the line (or real) (Analogy).

**Also known as:** λ₁ ≥ ¼; 975/4096; interior positivity

**Axes:** sign/positivity (Ax2), structure/frame (Ax1)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- analogue of → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) — ¼ + γ²
- analogue of → [Riemann hypothesis (target node)](#rh) — ρ(1−ρ) ≥ ¼
- lives in → [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) — interior positivity

### #74 · 0.452 · Cartan involution / compact unitary group <a id="cartan-involution"></a>

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

### #80 · 0.451 · Organizing split: ghost-blind = phase, ghost-sensitive = sign <a id="split-blind-sensitive"></a>

**Label:** Heuristic · **id:** `split_blind_sensitive` · **quadrant:** sharp but interpretive

*In plain words:* Every test that ghosts pass is about phase/unitarity; every test that catches a ghost is about the sign of a spectral weight, and for ζ that sign is RH.

**Core.** TAA Lemma 146 synthesis: functional equation, |φ| = 1, cocycles, Hecke, cusp positivity are ghost-blind (Ax3); Lagarias sign, Weil sign, Rosati sign are ghost-sensitive (Ax2) and ⇔ RH for ζ. Every ghost-sensitive global quadratic statement for Spec ℤ found so far is a restatement.

**Formula.** ghost-blind ↔ Ax3 (phase); ghost-sensitive ↔ Ax2 (sign) ⇔ RH

**Numbers.** DH: FE to 5×10⁻¹⁵ yet Re ξ′/ξ = −66.8

**Also known as:** TAA Lemma 146 split; two bins; phase vs sign

**Axes:** sign/positivity (Ax2), phase/unitarity (Ax3), ghost-blind, ghost-sensitive

**TAA lemmas:** 146, 137, 141, 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 0.7 · specificity 1.0 · tractability 0.5 · evidence 0.6 → priority 0.451

> ⚠ **Correction / caution.** An organizing observation, not a theorem: "sign" items for curves are theorems, for ζ restatements.

**Relations (outgoing):**

- same mechanism as → [Kramers–Kronig relations](#kramers-kronig) — absorption (sign) vs dispersion (phase) split
- same mechanism as → [Ax1–Ax3 axioms (Yoneda specification)](#ax123) — Ax2 vs Ax3
- analogue of → [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager)

**Relations (incoming):** [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Kramers–Kronig relations](#kramers-kronig) (same mechanism as); [Half Tate twist ℚ(½)](#half-tate-twist) (lives in); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); ["Cocycles give structure, not sign"](#cocycle-principle) (same mechanism as)

### #86 · 0.420 · Two-point form g + iω ≥ 0 <a id="two-point"></a>

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

### #92 · 0.392 · Curvature as cup square: convexity ↔ Rosati positivity <a id="curvature-cup-square"></a>

**Label:** Analogy · **id:** `curvature_cup_square` · **quadrant:** sharp but interpretive

*In plain words:* 

**Core.** K θ₁∧θ₂ = ω₁₃∧ω₂₃ (convention-independent; dω₁₂ = ±ω₁₃∧ω₂₃): Gauss curvature is a wedge square of second-fundamental-form 1-forms; Theorema Egregium; Gauss–Bonnet. Convex (II definite) ⇒ K > 0 ⇒ Cohn-Vossen rigidity (Herglotz). Dictionary: II ↔ H¹/cup product; convexity ↔ Rosati Tr(φφ′) > 0 ↔ |α| = √q; 'what is the arithmetic C²?' (FR-1).

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.392

**Relations (outgoing):**

- analogue of → [Rosati positivity](#rosati) — convexity ↔ positive involution
- analogue of → [Hodge index theorem](#hodge-index)
- analogue of → [Cup product / Poincaré duality pairing](#cup-product) — K is a cup square
- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- analogue of → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — deg(m+nF) as the cup square
- analogue of → [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) — rigid vs flexible

**Relations (incoming):** [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Cup product / Poincaré duality pairing](#cup-product) (analogue of)

### #105 · 0.360 · Negative index κ(𝒬) = N₊ (ghost count) <a id="kappa-index"></a>

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

### #109 · 0.347 · Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ <a id="zero-count-two-form"></a>

**Label:** Theorem · **id:** `zero_count_two_form` · **quadrant:** true but ghost-blind/untested

*In plain words:* A zero’s line always has area π however wide it is; stacking these areas over the strip gives the 2-form that counts zeros, and RH would need that count to come from a positive pairing.

**Core.** [T] Re ξ′/ξ(σ+it) = ∂_σ log|ξ|; each line has area π·sgn(σ−β) independent of its width (width × height = 1); crossing σ = β the area jumps by 2π = flux of ∇log|ξ| around ρ; Poincaré–Lelong/Jensen: (1/2π)Δ log|ξ| dσ∧dt = Σ_ρ δ_ρ (BIB). [N] TAA Lemma 154 fitted amplitudes = 1 to ≤ 3.4e−5 (area π); DH ghost-1 near amplitude −1 at d = 0.30, +1 at d = 0.35. [R] Pairing the 2-form with test functions = zero side of Weil's explicit formula; making it positive = MP4. Local areas are ghost-blind in total; their sign seen from σ > ½ is ghost-sensitive.

**Also known as:** Poincaré–Lelong; Jensen

**Axes:** sign/positivity (Ax2), ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 154

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.347

**Relations (outgoing):**

- same mechanism as → [Weil positivity criterion](#weil-positivity) — global pairing of the 2-form
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — positivity = MP4
- special case of → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — area of a line
- same mechanism as → [Cup product / Poincaré duality pairing](#cup-product) — volume form

**Relations (incoming):** [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (same mechanism as)

### #112 · 0.325 · Weil operator C = i^{p−q} = Wick rotation <a id="weil-operator"></a>

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

**Relations (incoming):** [Compatible complex structure J commuting with Frobenius](#compatible-j) (same mechanism as); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (analogue of); [Arakelov geometry](#arakelov) (fails for); [Principalization](#principalization) (analogue of)

### #120 · 0.325 · Toeplitz / Verblunsky coefficients <a id="toeplitz-verblunsky"></a>

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

**Relations (incoming):** [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (analogue of); [de Branges spaces](#de-branges) (same mechanism as); [Li criterion](#li-criterion) (same mechanism as)

### #127 · 0.325 · Spinor/Clifford route <a id="spinor-route"></a>

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

### #140 · 0.307 · Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}]) <a id="cc21-archimedean-positivity"></a>

**Label:** Cited · **id:** `cc21_archimedean_positivity` · **quadrant:** true but ghost-blind/untested

*In plain words:* Connes and Consani explain why Weil’s form is positive for test functions too narrow to see the prime 2: it dominates a trace on Sonin space.

**Core.** Selecta Math. (N.S.) 27 (2021) no. 4, art. 77 (arXiv 2006.13771, opened). Weil's inequality: f smooth positive definite, supp f ⊂ (1/2, 2), f̂(±i/2) = 0 ⇒ W∞(f) ≥ 0 (proved by Yoshida 1992 by explicit computation); ⇔ QW(g) = W∞(g∗g*) ≥ 0 for supp g ⊂ [2^{−1/2}, 2^{1/2}], ĝ(i/2) = 0. Support (1/2,2) chosen so that no rational prime enters. Thm 1: if also ĝ(0) = 0, W∞(g∗g*) ≥ Tr(ϑ(g) S ϑ(g)*), S = projection on Sonin space; Thm 6.11: without ĝ(0) = 0, ≥ Tr(...) − c|ĝ(0)|², 13 < c < 17. Their abstract method alone reaches I = [u⁻¹,u], u = 1.10246 (Cor 8) / 1.15077 (Rem 9); [1/2,2] needs Sonin/prolate and numerics (§6). In log scale: f supported in |u| < log 2 = the first prime atom; TAA Lemma 25's OS-RP fails exactly when the atom log 2 enters. Ghost-blind (archimedean only).

**Numbers.** 13 < c < 17 · u = 1.10246 / 1.15077 abstract range

**Also known as:** CC21; Sonin space; log 2 window

**Axes:** sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- special case of → [Yoshida window positivity](#yoshida) — conceptual strengthening
- lives in → [Archimedean place and Γ_ℝ factor](#archimedean-place)
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — both thresholds at log 2
- analogue of → [Connes trace formula](#connes-trace) — Sonin trace

**Relations (incoming):** [Yoshida window positivity](#yoshida) (analogue of)

### #141 · 0.307 · Cusp forms & Petersson positivity <a id="cusp-forms-petersson"></a>

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

**Relations (incoming):** [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (same mechanism as); [Weight ladder (modular weights)](#weight-ladder) (same mechanism as)

## Axis: no-go / refuted <a id="axis-no-go-refuted"></a>

### #2 · 0.720 · Davenport–Heilbronn function <a id="davenport-heilbronn"></a>

**Label:** Theorem · **id:** `davenport_heilbronn` · **quadrant:** RH-sharp

*In plain words:* Has a functional equation but no Euler product, and zeros off the line.

**Core.** TAA Lemma 149: DH Gram matrix from its own prime side (c_DH from c*a = a·log, Γ((s+1)/2), conductor 5, no pole; no zero list): λ_max > 0 for all L ≥ 3.85 (hats h = 0.025), 0.224 at 4, 192 at 16; two positive from 3.90; h = 0.05 onset 5.75. TAA Lemma 153: archimedean factor = that of the odd character mod 5 with χ(2) = i (χ(−1) = χ(4) = i² = −1), so any archimedean-only object is DH-blind.

**Numbers.** 0.7398 (TAA Lemma 78) · 0.7376 (TAA Lemma 136) · 5×10⁻¹⁵ · −66.8 · Ξ_DH even to 4.5e−33, real on ℝ to 1e−31 · z₀ = τ₀² = 7344.2831 − 52.8794i · Z_DH: 62 sign changes vs N = 66 on [10,120]; deficits 2 in [80,90] and [110,120] (TAA Lemma 152) · TAA Lemma 153: prime-side tilt blocks (w = 1.5, τ = 0.3) hyperbolic on [84.36,84.77] (flank), [85.48,85.91] and [114.04,114.29]; nowhere else on [10,120]; every window within 1.4 of an off-line height (85.699, 114.163); first significant at X = e^12 (111,273 nonzero DH coefficients) · TAA Lemma 153: λ₋ = −1.884 at γ = 85.70 and −0.367 at 114.16 (τ = 0.3) · TAA Lemma 154: ρ₁ = 0.8085171824566 + 85.6993484853776i, ρ₂ = 0.6508300806097 + 114.1633427307570i (|f| ≤ 4e−30); Γ = 0.61703, 0.30166 · TAA Lemma 154: 75 on-line zeros γ < 135 refined; TAA Lemma 141 list ≤ 0.0144 off · Standard DH zero list (TAA Lemma 154: 75 on-line zeros γ < 135 refined to 1e−12, plus the two off-line pairs); supersedes the TAA Lemma 141 list (max deviation 0.0144); adopted as standard · [N] TAA Lemma 155: off-line zeros detected from coefficients + FE (ghost map): β̂ = 0.80852, 0.65083 at log X = 16; SNR ≥ 10 from log X = 4 · [N] TAA Lemma 155: exact comb from AFE with N = 12 / 13 terms (σ = 0.55) · [N, rigorous] TAA Lemma 156: standard list certified complete and accurate to 1e−12 for 2 < t < 135 (79 zeros) · [N, rigorous] TAA Lemma 156: further off-line pairs ρ₃ = 0.574356 + 166.479306i, ρ₄ = 0.724258 + 176.702461i (Krawczyk); 135 < t < 200 complete (51)

**Also known as:** DH

**Axes:** no-go / refuted, ghost-sensitive

**TAA lemmas:** 78, 103, 136, 146, 148, 149, 150, 152, 153, 154, 155, 156

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** Tail number conflict.

> ⚠ **Correction / caution.** Injected DH locations only; not the DH function itself (no Euler product, no class-number data).

> ⚠ **Correction / caution.** Truncated zero side is finite-rank in fine bases (spurious λ ≈ +1e−15 from L = 2.85) — use prime side (TAA Lemma 149, correction 4).

> ⚠ **Correction / caution.** TAA Lemma 141 list leaves a cos(31.63v) residual 4.7e−8 vs prime side (TAA Lemma 149, correction 7, unexplained).

> ⚠ **Correction / caution.** Integer Ψ_n lattice does not detect DH (TAA Lemma 150, correction 6).

> ⚠ **Correction / caution.** Window edge 85.91 (TAA Lemma 153 §2 table) vs 85.92 (TAA Lemma 153 summary, s2 text and delta 1): rounding of the same scan; the table value is used here.

> ⚠ **Correction / caution.** Use for DH zeros; the TAA Lemma 141 list is off by up to 0.0144 (TAA Lemma 154, correction 14).

> ⚠ **Correction / caution.** “DH’s ghosts” needs a height range: the standard list (2 < t < 135) has two off-line pairs; TAA Lemma 156 certifies two more pairs at t ≈ 166.48 and 176.70 (ρ₃, ρ₄), recorded separately, not in the standard list (TAA Lemma 156, correction 4).

**Relations (outgoing):**

- fails for → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (fails for); [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (fails for); [Relative Gram matrix G_rel](#relative-gram) (lives in); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (special case of); [DH prime-side Gram test](#dh-prime-side-gram) (analogue of); [DH prime-side Gram test](#dh-prime-side-gram) (corrects); [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) (analogue of); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (lives in); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (lives in); [Epstein zeta no-go](#epstein) (same mechanism as); [Epstein zeta no-go](#epstein) (analogue of); [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (lives in); [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) (fails for); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (fails for); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of)

### #54 · 0.540 · Epstein zeta no-go <a id="epstein"></a>

**Label:** Theorem · **id:** `epstein` · **quadrant:** RH-sharp

*In plain words:* Epstein zeta functions of binary quadratic forms have a functional equation but no Euler product, and they have zeros off the line — the classic counterexample class next to DH.

**Core.** TAA Lemma 83: Epstein x² + 5y² = ζL(χ₋₂₀) + L(χ₋₄)L(χ₅); N(200) = 253 zeros, 183 on the line (70 off-line); first off-line 0.93297 + 15.66825i. TAA Lemma 135: 46 zeros with ½ < σ < 1 for t ≤ 250; control x² + y² (= 4ζL(χ₋₄), has Euler product): 0. TAA Lemma 138 R4: theta inversion and FE hold, unitarity ⇒ FE only, ghost-blind (Thm). TAA Lemma 153 (G, CM points): Σ′(m²+n²)^{−s} = 4ζ(s)L(s,χ₋₄) (NUM s = 3: 4.6589136156); Σ′(m²+mn+n²)^{−s} = 6ζ(s)L(s,χ₋₃) (6.3758815528); x²+5y²: ζ_K + L(χ₋₄)L(χ₅), 2x²+2xy+3y²: ζ_K − L(χ₋₄)L(χ₅), sum over the class group = 2ζ_K (Euler product restored, Hecke; NUM to 1e−12). Off-line zero refined: 0.9329696975 + 15.6682495313i (|Z| = 3e−21; ζ_K there 0.933). CM points are where one restricts (toric periods), not a quotient (TAA Lemma 153, correction 22).

**Numbers.** 0.93297 + 15.66825i · N(200) = 253, 183 on line · 46 off-line zeros t ≤ 250

**Also known as:** Epstein

**Axes:** no-go / refuted, ghost-sensitive, numerics/certificate

**TAA lemmas:** 83, 135, 138, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- same mechanism as → [Davenport–Heilbronn function](#davenport-heilbronn)
- fails for → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — FE without RH
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — TAA Lemma 135 counts vs quadratic positivity
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — class number 2 ⇒ no Euler product ⇒ off-line zeros (DH 1936)
- lives in → [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) — CM points i, ρ

### #97 · 0.377 · Band criterion γ < 2T_M <a id="band-criterion"></a>

**Label:** Heuristic · **id:** `band_criterion` · **quadrant:** background

*In plain words:* A ζ zero (or ghost) at height γ is visible in the class-number data only if every Maass form with t_j < γ/2 is known and subtracted; the zero’s frequency γ/2 must lie below the unknown-Maass band.

**Core.** TAA Lemma 148 Prop. band [H, N support]: with T_M = 100 the DH-location ghost (85.699, δ =.3085) has count-matched SNR 238 (x = 1e8) / 270 (x = 1e10); with T_M = 35.4 it is 0.15. γ = 143.1, δ =.1: SNR 4.6 (T_M = 100) vs 0.010 (T_M = 35.4). Reaching height γ needs ≈ γ²/48 Maass forms and the zero list below γ ⇒ the readout only re-derives listed zeros.

**Formula.** detectable ⇔ γ/2 < T_M (Maass list complete to T_M)

**Numbers.** SNR 270 vs 0.15 (DH-location) · 2T_M = 200

**Also known as:** spectral separation; Maass completeness threshold

**Axes:** no-go / refuted, numerics/certificate

**TAA lemmas:** 148

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.377

> ⚠ **Correction / caution.** Not a theorem; the noise model treats unknown t_j as random.

**Relations (outgoing):**

- fails for → [Riemann hypothesis (target node)](#rh) — circular: needs the zero list it would test

**Relations (incoming):** [LMFDB level-1 Maass list complete to T = 100](#lmfdb-maass-complete) (implies); [Null-calibrated GLS matched filter](#null-calibrated-gls) (same mechanism as)

### #130 · 0.325 · Local-to-global failure <a id="local-global"></a>

**Label:** Theorem · **id:** `local_global` · **quadrant:** true but ghost-blind/untested

*In plain words:* Local positivity at each prime does not imply global.

**Core.** TAA Lemma 25 Rem 6.2: naive local positivity fails (K < 0 for |r| < 6.28984); CC21 Thm 1 local archimedean positivity only for supp ⊂ [2^{−½}, 2^{½}] with vanishing. TAA Lemma 64/TAA Lemma 65: local Hasse (Q_p > 0 at every p, proved) vs global RH for L(E,s) (open) — the collective split. TAA Lemma 66: local positivity via Deligne weights is ghost-blind residual data.

**Numbers.** |r| < 6.28984

**Also known as:** local positivity

**Axes:** no-go / refuted

**TAA lemmas:** 25, 64, 65, 66, 91

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

### #161 · 0.267 · Counts vs quadratic positivity <a id="count-positivity"></a>

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

**Relations (incoming):** [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (same mechanism as); [Epstein zeta no-go](#epstein) (same mechanism as); [Tate count / Picard number (ghost-blind)](#tate-count) (same mechanism as)

## Axis: reference/pole/cusp <a id="axis-reference-pole-cusp"></a>

### #3 · 0.720 · ψ(x) − x (explicit formula, deviation from the pole) <a id="psi-minus-x"></a>

**Label:** Cited · **id:** `psi_minus_x` · **quadrant:** RH-sharp

*In plain words:* Count prime powers with weight log p and subtract the pole’s prediction x; what remains is a sum over zeros. RH ⇔ the remainder is O(√x log²x).

**Core.** Explicit formula ψ(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½log(1 − x⁻²); RH ⇔ ψ(x) − x = O(x^{½+ε}). In TAA the x term is the pole/𝕃 reference; ψ − x ≠ 0 measures the flow-relative H¹.

**Formula.** ψ(x) − x = −Σ_ρ x^ρ/ρ + …

**Numbers.** max|ψ−x|/√x ≤ 0.778 on log x ∈ [1,16] · DH max|ψ_DH|/√x: 0.878, 1.411, 3.199, 8.444 on [1,4), [4,8), [8,12), [12,16) · (θ(x)−x)/√x log-mean −1.123 on [1e3,1e7]

**Also known as:** Chebyshev ψ; prime counting error; ψ − x ≠ 0

**Axes:** reference/pole/cusp, ghost-sensitive, Spec ℤ gap

**TAA lemmas:** 142, 144, 149, 150

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 0.8 → priority 0.720

> ⚠ **Correction / caution.** ψ(x) − x ≠ 0 is not a failure: it is the zero contribution relative to the pole reference.

> ❓ **Not verified / open.** The explicit-formula wording is standard (cited), not from a specific lemma section.

**Relations (outgoing):**

- same mechanism as → [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) — both compare a prime product/sum to a pole reference
- same mechanism as → [Displaced reference (subtracting the pole)](#displaced-reference) — subtract the pole
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — size O(x^{½+ε}) ⇔ RH
- analogue of → [Tate count / Picard number (ghost-blind)](#tate-count) — N_n − (1 + qⁿ) = −Tr(Fⁿ|H¹) over F_q
- analogue of → [Relative Gram matrix G_rel](#relative-gram) — [less-sensitive-than] Gram separates DH at span 3.85; ψ separation needs log x ≳ 8 (TAA Lemma 149)

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (analogue of); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (same mechanism as); [No étale H¹ for Spec ℤ](#no-etale-h1) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (same mechanism as); [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of)

### #8 · 0.720 · Primitive part V₀ = U^⊥ <a id="primitive-part"></a>

**Label:** Theorem · **id:** `primitive_part` · **quadrant:** RH-sharp

*In plain words:* What is left after removing the reference plane; on it the form should be negative (curves: theorem; ℚ: RH).

**Core.** D° = D − d₁f₂ − d₂f₁; (D°)² = −Tr_{H¹}(α_Dα_D†) (TAA Lemma 133). Over ℚ V₀ = U^⊥ and D·D ≤ 0 on V₀ ⇔ RH (TAA Lemma 91).

**Formula.** (D°)² = −def(D) ≤ 0

**Numbers.** λ_max on ker P / λ_max = 1.19–6361 over spans ≤ 16; 1.2–4.4 for L ≥ 12

**Also known as:** V₀; primitive classes; D°

**Axes:** reference/pole/cusp, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 91, 125, 133, 142, 149

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** A “−2Tr” formula holds only on the primitive part.

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — complement
- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst) — physical quotient

**Relations (incoming):** [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Relative Gram matrix G_rel](#relative-gram) (analogue of); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (fails for); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (same mechanism as)

### #28 · 0.579 · Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays) <a id="light-cone-u"></a>

**Label:** Theorem · **id:** `light_cone_U` · **quadrant:** true but ghost-blind/untested

*In plain words:* The two special directions (the trivial class 𝟙 and the Lefschetz/pole class 𝕃) span a plane with one positive and one negative direction; positivity is always measured relative to it.

**Core.** Over F_q: U = ⟨f₁, f₂⟩ ⊂ NS(C×C), signature (1,1), f₁, f₂ null; ample class lies in U; complement negative definite. Over ℚ: the pole/Tate plane spanned by 𝟙 and 𝕃 (poles at s = 0, 1), U^⊥ = V₀ (TAA Lemma 142).

**Formula.** U = ⟨𝟙, 𝕃⟩, sig U = (1,1), 𝟙² = 𝕃² = 0

**Numbers.** U-fraction of ζ's near-null vector 0.63, 0.65, 0.56, 0.27, 0.11, 0.18, 0.20 at L = 1, 2, 4, 8, 12, 14, 16 · λ₂(C) = λ_max|ker P to < 1e−3 for L ≥ 1.1 (POLE rank 2, ker P its kernel)

**Also known as:** U; null rays; hyperbolic plane; light cone

**Axes:** reference/pole/cusp, structure/frame (Ax1), geometry over F_q

**TAA lemmas:** 14, 98, 115, 140, 142, 149

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** "Light cone" includes its interior.

> ⚠ **Correction / caution.** The ample class lives in U; the surface is read relative to the points.

**Relations (outgoing):**

- same mechanism as → [Pole plane / Tate poles at s = 0, 1](#pole-plane) — same plane over ℚ
- lives in → [Hodge index theorem](#hodge-index) — the (1,1) part

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (lives in); [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (lives in); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (lives in); [Castelnuovo–Severi inequality](#castelnuovo-severi) (lives in); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (lives in); [Hasse bound as a positive degree form](#hasse-pythagoras) (analogue of); [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) (analogue of); [Hodge index theorem](#hodge-index) (lives in); [Pole plane / Tate poles at s = 0, 1](#pole-plane) (same mechanism as); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #53 · 0.540 · Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order) <a id="goldfeld-bsd"></a>

**Label:** Cited · **id:** `goldfeld_bsd` · **quadrant:** RH-sharp

*In plain words:* If the partial Euler product of L(E,s) at the centre behaves like C/(log x)^r, then L(E,s) satisfies RH and r is the analytic order of vanishing — with a surprising √2 in the constant.

**Core.** If ∏_{p≤x} L_p(E,1) ∼ C/(log x)^r then L(E,s) satisfies RH, r = ord_{s=1}L(E,s), C = L^{(r)}(E,1)/(r! √2 e^{rγ}) (Goldfeld 1982, cited via Conrad 2005; TAA Lemma 140).

**Formula.** ∏_{p≤x} L_p(E,1) ∼ C/(log x)^r, C = L^{(r)}(E,1)/(r!√2 e^{rγ})

**Numbers.** √2 factor · K_E = 5.5712, 8.2314, 5.9082, 2.1574 (11a1, 37a1, 389a1, 32a) · ∏N_p/p/(log x)^r at 1e7: 5.52, 7.95, 6.02, 2.37

**Also known as:** Goldfeld 1982; Nagao–Mestre product; ∏ L_p(E,1)

**Axes:** reference/pole/cusp, ghost-sensitive

**TAA lemmas:** 140, 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** It gives the analytic order, not the rank (rank = order is BSD).

> ⚠ **Correction / caution.** a_p are not BSD generators.

> ⚠ **Correction / caution.** Note the √2 factor (Conrad).

> ⚠ **Correction / caution.** Finite products (±10% oscillation to 1e7) are not evidence for RH (TAA Lemma 150, correction 10).

**Relations (outgoing):**

- implies → [Riemann hypothesis (target node)](#rh) — for L(E,s)
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — prime data vs the reference at s = 1
- analogue of → [Displaced reference (subtracting the pole)](#displaced-reference)

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (same mechanism as); [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (same mechanism as); [√2 family](#sqrt2-family) (corrects)

### #76 · 0.452 · Pole plane / Tate poles at s = 0, 1 <a id="pole-plane"></a>

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

### #96 · 0.377 · Displaced reference (subtracting the pole) <a id="displaced-reference"></a>

**Label:** Heuristic · **id:** `displaced_reference` · **quadrant:** background

*In plain words:* Arithmetic quantities are measured relative to a reference fixed by the pole; the "error" is the displacement from that reference.

**Core.** ψ − x, E₂* = E₂ − 3/(πy) and the relative Gram all subtract a pole/reference term. TAA Lemma 146 records this as an organizing analogy.

**Also known as:** reference subtraction

**Axes:** reference/pole/cusp, physics analogue

**TAA lemmas:** 146, 142

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.377

> ⚠ **Correction / caution.** Analogy, not theorem.

**Relations (outgoing):**

- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)
- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly)
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram)
- analogue of → [Buoyancy / Archimedes principle](#archimedes) — buoyancy: weight relative to displaced fluid

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (analogue of); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as); [Buoyancy / Archimedes principle](#archimedes) (analogue of)

### #115 · 0.325 · √2 family <a id="sqrt2-family"></a>

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

### #116 · 0.325 · Closed geodesics on the modular surface <a id="closed-geodesics"></a>

**Label:** Theorem · **id:** `closed_geodesics` · **quadrant:** true but ghost-blind/untested

*In plain words:* Lengths 2 log ε_t from traces t; Selberg trace formula pairs them with resonances.

**Core.** Length 2 log ε_t with h⁺ classes (TAA Lemma 143); trace-6 has 3 primitive oriented classes (TAA Lemma 141); counts t = 3..11: 1,2,2,3,3,4,2,6,3. √2 geodesic ℓ = 3.5254943481, sinh(ℓ/2) = 2√2; golden geodesic 1.9248 is shortest. S(t) = Σ h⁺ log ε⁺², 36 discriminants 0 mismatches (TAA Lemma 143). TAA Lemma 148: S(t) extended to t ≤ 1e5 via quadclassunit, validated = qfbclassno on 8000 traces (2.3e−16); hR = √d L(1,χ)/2 checked to 2.2e−16.

**Formula.** ℓ = 2 log ε_t

**Numbers.** 1.9248 (golden) · 3.5254943481 (√2) · counts 1,2,2,3,3,4,2,6,3 · 99 998 traces to t = 1e5 (x = 1e10), TAA Lemma 148

**Also known as:** primitive hyperbolic classes

**Axes:** reference/pole/cusp

**TAA lemmas:** 141, 143, 146, 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Selberg resonances](#selberg-resonances)

**Relations (incoming):** [√2 family](#sqrt2-family) (special case of)

### #117 · 0.325 · Cusp ≠ archimedean place <a id="cusp-vs-infinity"></a>

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

**Relations (incoming):** [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (corrects); [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) (same mechanism as)

### #118 · 0.325 · Pole of ζ at s = 1 (residue / 3/π) <a id="pole-s1"></a>

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

### #119 · 0.325 · Selberg resonances <a id="selberg-resonances"></a>

**Label:** Theorem · **id:** `selberg_resonances` · **quadrant:** true but ghost-blind/untested

*In plain words:* Poles of φ(s) relate to ζ zeros at s = ρ/2.

**Core.** φ = Λ(2s−1)/Λ(2s) has poles in Re s < ½ exactly at ρ/2, φ(½) = −1 (TAA Lemma 143). ΣΛ(P)N^{−s} = Z′/Z(s) − Z′/Z(s+1). TAA Lemma 143: ρ/2 seen in the length spectrum from class numbers (projection on the predicted ζ term 1.003). Selberg zeros ρ/2: infinitely many off the line (TAA Lemma 141). TAA Lemma 148: per-resonance decay rates read for 79 ρ/2 (γ < 200), all consistent with ¼ (calibration).

**Also known as:** scattering poles

**Axes:** reference/pole/cusp, phase/unitarity (Ax3)

**TAA lemmas:** 141, 143, 146, 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- same mechanism as → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct)

**Relations (incoming):** [Closed geodesics on the modular surface](#closed-geodesics) (same mechanism as)

### #123 · 0.325 · Density / volume reading <a id="density-volume"></a>

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

### #138 · 0.307 · Archimedean place and Γ_ℝ factor <a id="archimedean-place"></a>

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

**Relations (incoming):** [Cusp ≠ archimedean place](#cusp-vs-infinity) (corrects); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (lives in); [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) (lives in); [Archimedean thresholds a*](#arch-threshold) (special case of)

### #142 · 0.307 · E₂ anomaly (E₂* = E₂ − 3/(πy)) <a id="e2-anomaly"></a>

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

### #144 · 0.307 · Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k <a id="herbrand-ribet"></a>

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

### #145 · 0.307 · Mazur–Wiles main conjecture ("Euler characteristic = L-value") <a id="mazur-wiles"></a>

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

### #148 · 0.307 · Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂) <a id="ramanujan-691"></a>

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

### #166 · 0.267 · Weight ladder (modular weights) <a id="weight-ladder"></a>

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

**Relations (incoming):** [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (lives in); [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of)

## Axis: Spec ℤ gap <a id="axis-spec-gap"></a>

### #4 · 0.720 · Connes trace formula <a id="connes-trace"></a>

**Label:** Cited · **id:** `connes_trace` · **quadrant:** RH-sharp

*In plain words:* Connes’ trace formula on the adele class space: zeros appear as an absorption spectrum, and the global trace formula holding is equivalent to RH.

**Core.** Connes 1999 (read at source, TAA Lemma 30/TAA Lemma 71): global trace formula ≡ RH; Thm 1 sees only critical zeros (δ > 1); Thm 5 char p; zeros = absorption spectrum (TAA Lemma 71). TAA Lemma 82: cutoff, non-critical zeros as resonances. TAA Lemma 118: Connes reduces RH for Hecke L to the trace formula ⇒ Weil positivity; absorption spectrum ghost-blind. TAA Lemma 138 R2: Hilbert–Pólya positivity is circular if the inner product is Weil’s form. TAA Lemma 151: Connes's cokernel L²(C_k)/Im E (absorption spectrum) is the MP1 candidate; E carries |g|^{½} (canonical real half twist); C ⊕ C(1) boundary = H⁰/H². Missing on both sides: MP4. TAA Lemma 153 (E, corrected per H): Selecta Math. (N.S.) 5 (1999) 29–106, doi 10.1007/s000290050042 (Crossref; abstract re-read). Connes cokernel: the positive (Hilbert) space sees only the critical zeros — spectral realization of the critical zeros as an absorption spectrum (δ > 1 version, Thm 1 as read at source in TAA Lemma 30/TAA Lemma 71), noncritical zeros only as resonances; semi-local trace formula proved; RH ⇔ validity of the global trace formula (⇔ Weil positivity). A quotient of a Hilbert space is automatically positive, so 'positivity of the inherited form ⇔ RH' was wrong (TAA Lemma 153, correction 18): RH ⇔ nothing is missing from the positive space. The two quotients: (1) by ℚ^× acting on ideles → C_ℚ = 𝔸^×/ℚ^× (modular analogue Γ∖ℍ); (2) the cokernel of the summation map E (modular analogue: the constant term at the cusp; cusp forms = its kernel). CM points are not the quotient.

**Also known as:** adelic class space; Connes cokernel: positive space sees only critical zeros; RH ⇔ global trace formula

**Axes:** Spec ℤ gap, restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 30, 71, 82, 118, 138, 151, 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Weil positivity criterion](#weil-positivity) — reduces to Weil positivity (TAA Lemma 118)
- analogue of → [Half Tate twist ℚ(½)](#half-tate-twist) — |g|^{½}
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — RH ⇔ nothing missing from the positive space

**Relations (incoming):** [Deninger’s foliated program](#deninger) (analogue of); [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) (analogue of); [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (same mechanism as); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (analogue of); [Bost–Connes KMS states](#kms-bost-connes) (analogue of)

### #29 · 0.579 · Surface + ample + RR ⇒ Hodge index (D8) <a id="surface-ample-rr"></a>

**Label:** Theorem · **id:** `surface_ample_rr` · **quadrant:** true but ghost-blind/untested

*In plain words:* The curve proof needs a surface, an ample class and Riemann–Roch.

**Core.** D8 (TAA Lemma 140): surface + ample + RR ⇒ Hodge index. TAA Lemma 145 V3: classical S1 quadratic RR, S2 Serre, S3 h¹ ≥ 0, S4 sections ⇒ effective, S5 ample·eff > 0; the missing Spec ℤ step is quadratic S1 + S4. TAA Lemma 147: CC18 calls exactly this "the key missing step". TAA Lemma 152 Table 1: the chain exists for F_q curves and arithmetic surfaces; for Spec ℤ the space is partial, the ample class missing (Pic^ ≅ ℝ), RR 1-dimensional (CC22/23), Hodge index ⇔ RH (TAA Lemma 91). Deligne's route avoids Hodge index but not positivity (deligne_tensor_power).

**Also known as:** D8; ample → RR → Hodge index chain

**Axes:** Spec ℤ gap, geometry over F_q

**TAA lemmas:** 140, 145, 147, 152

**Scores (Heuristic):** gap significance 0.8 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** Needs S2, S3, S5 too (TAA Lemma 145).

**Relations (outgoing):**

- implies → [Hodge index theorem](#hodge-index)
- analogue of → [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) — the other proved route

**Relations (incoming):** [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (same mechanism as); [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) (same mechanism as); [Castelnuovo–Severi inequality](#castelnuovo-severi) (same mechanism as); [Products grow linearly (2n), not quadratically](#products-linear) (fails for); [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) (same mechanism as); [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (implies); [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) (analogue of)

### #32 · 0.579 · Deninger’s foliated program <a id="deninger"></a>

**Label:** Cited · **id:** `deninger` · **quadrant:** true but ghost-blind/untested

*In plain words:* Deninger’s program: a foliated dynamical space whose leafwise cohomology carries the zeros; a positive Hodge star plus the flow would force Θ = ½ + (skew part).

**Core.** TAA Lemma 4: foliation-like (Deninger) structure carries the explicit formula with its signs; contact-like (Reeb) gives only the analytic shadow; on closed M, Reeb flows and Deninger systems are mutually exclusive. TAA Lemma 28: zeros = leafwise zero modes [analogy/conjectural]. TAA Lemma 50 Prop 7.1 (Den98): positive J commuting with Θ ⇒ Θ − ½ skew [RESTATEMENT]. TAA Lemma 93: Deninger D1–D5 stated exactly. TAA Lemma 141 §2: level S3 of the "surface" target. TAA Lemma 151 Conj 4.1 (OPEN): Deninger's conjectured cohomology stated as axioms MP0–MP4 (H⁰/H² = Tate boundary terms; H¹ with flow, spectrum = zeros; trace formula; cup product to ℝ(−1); definite cup square on primitive part = the sign). Naming rule: no coined name until constructed. Deninger 2007 (opened): 'the conjectured cohomology has not been constructed'.

**Formula.** Θ = ½ + A, A skew

**Also known as:** foliation

**Axes:** Spec ℤ gap, open target, physics analogue

**TAA lemmas:** 4, 28, 50, 93, 141, 151, 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- analogue of → [Connes trace formula](#connes-trace) — foliation vs leaf space; J. W. McGreevy conjectures an isomorphism (Hodge–Lefschetz style)
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP0–MP4
- analogue of → [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) — archimedean Γ-factor proved (Consani 1998)

**Relations (incoming):** [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Half Tate twist ℚ(½)](#half-tate-twist) (analogue of); [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) (special case of)

### #33 · 0.579 · Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U) <a id="laurent-square"></a>

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

### #34 · 0.579 · Parity argument: linear χ cannot see D² <a id="parity-linear-chi"></a>

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

### #36 · 0.579 · Tautology boundary (zero side vs prime side) <a id="tautology-boundary"></a>

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

### #37 · 0.579 · No étale H¹ for Spec ℤ <a id="no-etale-h1"></a>

**Label:** Theorem · **id:** `no_etale_h1` · **quadrant:** true but ghost-blind/untested

*In plain words:* Spec ℤ is simply connected; the "H¹" must be relative to the flow (ψ − x ≠ 0).

**Core.** TAA Lemma 140: π₁ét(Spec ℤ) = 1 ⇒ H¹ét = 0. TAA Lemma 141 §4: H¹ table with a flow-H¹ column; Q(√2) circle length √2·log(1+√2) = 1.24645 (Schoof). The H¹ that carries zeros is flow-relative (ψ − x).

**Also known as:** flow-relative H¹

**Axes:** Spec ℤ gap

**TAA lemmas:** 140, 141

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)

**Relations (incoming):** [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as)

### #71 · 0.452 · Connes–Consani sites <a id="connes-consani"></a>

**Label:** Cited · **id:** `connes_consani` · **quadrant:** true but ghost-blind/untested

*In plain words:* Topos-theoretic candidate for Spec ℤ × Spec ℤ.

**Core.** Arithmetic site and scaling site (CC14, CC16): a square exists, with Ψ_λ and s(f,f) = D•D (TAA Lemma 30), but no H¹, RR or Hodge index on it (TAA Lemma 65). TAA Lemma 147: their proved RRs are 1-dimensional; RR on the square is open (CC18).

**Also known as:** arithmetic site; scaling site

**Axes:** Spec ℤ gap

**TAA lemmas:** 30, 131, 140, 147

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object)

**Relations (incoming):** [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (lives in); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of)

### #77 · 0.452 · Products grow linearly (2n), not quadratically <a id="products-linear"></a>

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

### #87 · 0.419 · Riemann hypothesis (target node) <a id="rh"></a>

**Label:** Open · **id:** `rh` · **quadrant:** true but ghost-blind/untested

*In plain words:* All nontrivial zeros of ζ have real part ½. In TAA every ghost-sensitive global sign statement for Spec ℤ turns out to be RH restated.

**Core.** RH is not proved in TAA. The positivity inventory of the programme finds that every ghost-sensitive global quadratic statement for Spec ℤ is a restatement of RH.

**Formula.** ρ = β + iγ, β = ½ for all ρ

**Also known as:** RH; Θ = ½

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 1, 107

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

> ⚠ **Correction / caution.** Every lemma PDF carries "RH NOT proved".

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (equivalent to RH); [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (equivalent to RH); [Connes trace formula](#connes-trace) (equivalent to RH); [Lagarias/Hinkkanen criterion](#lagarias) (equivalent to RH); [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (equivalent to RH); [Relative Gram matrix G_rel](#relative-gram) (equivalent to RH); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (equivalent to RH); [Passivity (positive real part)](#passivity) (equivalent to RH); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (equivalent to RH); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (equivalent to RH); [Rosati positivity](#rosati) (equivalent to RH); [RH for curves over F_q (Weil)](#fq-curves) (analogue of); [Decay rate ¼](#decay-quarter) (equivalent to RH); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (equivalent to RH); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (implies); [Compatible complex structure J commuting with Frobenius](#compatible-j) (equivalent to RH); [de Bruijn–Newman constant Λ](#debruijn-newman) (equivalent to RH); [Li criterion](#li-criterion) (equivalent to RH); [Suzuki’s de Branges line from the prime side](#suzuki-line) (equivalent to RH); [Bagchi recurrence](#bagchi) (equivalent to RH); [Hodge index theorem](#hodge-index) (equivalent to RH); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (analogue of); [Cartan involution / compact unitary group](#cartan-involution) (fails for); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (equivalent to RH); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (equivalent to RH); [Two-point form g + iω ≥ 0](#two-point) (equivalent to RH); [Hilbert–Pólya](#hilbert-polya) (implies); [Band criterion γ < 2T_M](#band-criterion) (fails for); [Cusp forms & Petersson positivity](#cusp-forms-petersson) (fails for); [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (fails for); [Hecke operators](#hecke) (fails for)

### #89 · 0.419 · Arithmetic Castelnuovo object (C1–C4) <a id="castelnuovo-object"></a>

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

### #90 · 0.419 · No Riemann–Roch for C_ℚ × C_ℚ (the square is open) <a id="cc-square-open"></a>

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

### #98 · 0.377 · Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing) <a id="formal-vs-geometric-lattice"></a>

**Label:** Heuristic · **id:** `formal_vs_geometric_lattice` · **quadrant:** background

*In plain words:* Numbers arranged as an intersection lattice prove nothing by themselves; on a real surface the Hodge index theorem makes them proof-bearing.

**Core.** A formal lattice of intersection numbers (TAA Lemma 150 Ψ_n lattice = Weil's form as a lattice) satisfies whatever identities are built in and was ghost-blind (λ_max −0.416 ζ vs −2.226 DH at K = 90; TAA Lemma 150 Prop 2.3). On C×C the same numbers are proof-bearing because the Hodge index is a theorem about the surface (ample class + RR), proved before the αᵢ are known. The composition law can be imposed consistently on any FE data (fakes, DH): only definiteness separates (TAA Lemma 149 DH prime-side onset 3.85; fakes (2,2)) (TAA Lemma 152, correction 5). What carries the numbers: classes Γ_t with a composition law from a flow, an ample class, RR strong enough for Hodge index.

**Also known as:** formal lattice; consistent vs definite

**Axes:** Spec ℤ gap, structure/frame (Ax1)

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.377

**Relations (outgoing):**

- same mechanism as → [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) — formal
- same mechanism as → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — geometric
- implies → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) — what makes numbers proof-bearing
- analogue of → [DH prime-side Gram test](#dh-prime-side-gram) — consistent but indefinite

### #108 · 0.347 · Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional) <a id="cc-riemann-roch"></a>

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

### #122 · 0.325 · Arakelov geometry <a id="arakelov"></a>

**Label:** Cited · **id:** `arakelov` · **quadrant:** true but ghost-blind/untested

*In plain words:* Compactified arithmetic surfaces.

**Core.** TAA Lemma 74: Ô(1)² = ½ for FS metrics; pole-plane Gram [[½,1],[1,0]] signature (1,1); Hodge index vacuous in genus 0. TAA Lemma 139: Pic^(Spec ℤ̄) ≅ ℝ has rank 1 and no complex structure. TAA Lemma 65/TAA Lemma 145: Faltings–Hriljac = Hodge index on arithmetic surfaces (curve × Spec O_K), relative part = Néron–Tate, not ζ. TAA Lemma 138 R5: Néron–Tate PD (37a1 ĥ = 0.051114). TAA Lemma 152: Faltings 1984 (Ann. Math. 119, 387–424), Hriljac 1985 (Amer. J. Math. 107, 23–38), bibliographic data verified: Hodge index on arithmetic surfaces ⇒ Néron–Tate positive definite; not RH for any L-function (TAA Lemma 152, correction 12).

**Also known as:** Pic^; Faltings–Hriljac arithmetic Hodge index; Faltings–Hriljac (arithmetic Hodge index)

**Axes:** Spec ℤ gap

**TAA lemmas:** 65, 74, 138, 139, 145, 152

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Faltings–Hriljac gives height positivity, not RH (TAA Lemma 152, correction 12).

**Relations (outgoing):**

- fails for → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)

**Relations (incoming):** [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (fails for)

### #124 · 0.325 · F₁ base <a id="f1-base"></a>

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

### #125 · 0.325 · Principalization <a id="principalization"></a>

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

### #126 · 0.325 · Spec ℤ is terminal <a id="spec-z-terminal"></a>

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

### #128 · 0.325 · Weil Rosetta stone <a id="weil-rosetta"></a>

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

### #129 · 0.325 · Cohesion (arena) <a id="cohesion"></a>

**Label:** Theorem · **id:** `cohesion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Cohesion is the arena, not the surface.

**Core.** TAA Lemma 141 §3: cohesion is the arena, not the surface; the étale ∞-topos of Spec ℤ is not cohesive (pro-shape, Hoyois); new Thm: [ℕ^×, Set] is not cohesive (Γ has no right adjoint). D10 (relative cohesion). TAA Lemma 146 §5: the cohesion quadruple Π ⊣ Disc ⊣ Γ ⊣ coDisc is a line without sign; RLGC is a 2×2 grid with mirror/KK/sign — numerology only.

**Also known as:** cohesive topos

**Axes:** Spec ℤ gap

**TAA lemmas:** 96, 141, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Heaviside ≠ cohesion one-to-one.

### #143 · 0.307 · Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR) <a id="euler-char-chi"></a>

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

### #182 · 0.181 · Two different χ’s: Euler characteristic vs class-group character <a id="two-chis"></a>

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

## Axis: geometry over F_q <a id="axis-geometry-over-f-q"></a>

### #5 · 0.720 · Frobenius-graph lattice on E×E (relative counts = intersections with Δ) <a id="frobenius-graph-lattice"></a>

**Label:** Theorem · **id:** `frobenius_graph_lattice` · **quadrant:** RH-sharp

*In plain words:* On the square of an elliptic curve, the graph of Frobenius meets the diagonal in the point count; the sign pattern of these intersections is exactly the Riemann hypothesis for the curve.

**Core.** e₁, e₂, Δ, Γ_{F^n} on E×E/F_q: Γ_n·e₁ = 1, Γ_n·e₂ = q^n, Δ·Γ_n = N_n, Γ_m·Γ_n = q^{min}N_{|m−n|}; complement Gram −[[2,a],[a,2q]] = −2 deg(m+nF); det = −(4q − a²); Hodge index ⇔ signature (1,3) ⇔ Hasse. NUM 11a1, 15 primes: (1,3,0), with Γ₂ (1,3,1); fake a > 2√p → (2,2). TAA Lemma 152 Prop 4.1 (NUM, zeta-free): 11a1, brute-force counts over F_{p^k} (p^k ≤ 729; p = 2,3,5,7,13,17,19) satisfy Γ_m·Γ_n = q^m N_{n−m} (incl. m = n, N₀ = 2 − 2g); Gram of ⟨e₁,e₂,Γ₀..Γ_K⟩ rank 4, inertia (1,3) exactly; fakes (5,5),(7,6),(13,8),(2,3) give (2,2). Prop 4.3: D_m·D_n = −Σ αᵢⁿβᵢᵐ.

**Formula.** det Gram⟨e₁,e₂,Δ,Γ_F⟩ = −(4q − a²)

**Numbers.** det₄ = −11 (p=3), −211 (p=59) · N_k(11a1, p = 2) = 5, 5, 5, 25, 25, 65, 145, 225, 545 (k ≤ 9) · inertia (1,3) for all 7 primes; fakes (2,2)

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 150, 152

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

**Relations (outgoing):**

- special case of → [Hodge index theorem](#hodge-index) — E×E
- same mechanism as → [Rosati positivity](#rosati) — Rosati form = intersection form on the Frobenius plane
- same mechanism as → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- analogue of → [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) — ℚ target: Ψ_λ classes
- analogue of → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — relative counts = intersections with Δ

**Relations (incoming):** [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (same mechanism as); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) (analogue of); [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (same mechanism as)

### #41 · 0.540 · Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse <a id="conic-type-at-infinity"></a>

**Label:** Theorem · **id:** `conic_type_at_infinity` · **quadrant:** RH-sharp

*In plain words:* Whether the quadratic form deg is an ellipse or a hyperbola is decided at infinity; deg ≥ 0 because it counts points, so it is an ellipse, which is the Hasse bound.

**Core.** A conic is an ellipse/parabola/hyperbola as it has 0/1/2 real points at infinity (discriminant of Q = 0); a plane through the cone's vertex gives a line pair (J. W. McGreevy's wedge). For E/F_q: deg(m − nF) = m² − a·mn + q·n² ≥ 0 (it counts a kernel) ⇒ a² − 4q ≤ 0 ⇔ Hasse (Silverman AEC Thm V.1.1): the norm conic is an ellipse; a² = 4q gives a double line (TAA Lemma 152, correction 10). Same as TAA Lemma 150's det −(4q − a²), signature (1,3); fakes (a² > 4q) give a hyperbola and (2,2). For ζ: Weil's form in blocks, on-line zero elliptic, off-line pair hyperbolic (1,1). Missing ingredient as a 'degree': a count (≥ 0) whose polarization is Weil's form (Open).

**Formula.** deg(m − nF) = m² − a mn + q n² ≥ 0 ⇒ a² ≤ 4q

**Numbers.** 11a1 at p = 2,3,5,7: ellipses; fake p = 5, a = 5: hyperbola

**Also known as:** norm conic; ellipse = Hasse

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- same mechanism as → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — det −(4q−a²); (1,3) vs (2,2)
- special case of → [Castelnuovo–Severi inequality](#castelnuovo-severi) — genus 1, norm form
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — deg counts a kernel
- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — fakes give a hyperbola

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (same mechanism as); [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) (same mechanism as); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (same mechanism as)

### #42 · 0.540 · Frobenius as a boost (rapidity ½ log q) <a id="frobenius-boost"></a>

**Label:** Theorem · **id:** `frobenius_boost` · **quadrant:** RH-sharp

*In plain words:* On the light-cone plane Frobenius acts like a Lorentz boost of rapidity ½ log q; a true curve needs one boost, a fake needs two.

**Core.** Hodge index + one boost of rapidity ½ log q on the H–V plane ⇒ Hasse; fakes need two (TAA Lemma 98 thm:fqboost). Over ℚ: translation is an isometry, pole boost rapidity ½ log λ; Lorentzian = Weil positivity (restatement). TAA Lemma 150 §4.5: Doppler red/blue shift = boost; on-line motion = rotation (a_p = 2√p cos θ_p), off-line displacement σ − ½ = rapidity; a shift √p e^{±η} is forbidden for curves by Castelnuovo/Hodge index; TAA Lemma 58 'RH = exclude boosts'. Ghost-sensitive (it is δ itself).

**Formula.** B_{½ log q}(H + V) = Γ/√q (hyperbolic part)

**Numbers.** q = 101: translation length 2.3076 = ½ log 101

**Also known as:** one boost; hyperbolic orthogonal; Levinson boosts; Doppler = boost = off-line displacement

**Axes:** geometry over F_q, structure/frame (Ax1), ghost-sensitive

**TAA lemmas:** 14, 98, 99, 107, 114, 117, 150, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Dividing by √q does not undo the boost (TAA Lemma 114, correction 14).

> ⚠ **Correction / caution.** Two boosts are never a pure rotation unless inverse (TAA Lemma 107).

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — acts on U
- analogue of → [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) — Levinson/Szegő step = boost of rapidity artanh|α| (TAA Lemma 98, TAA Lemma 117)
- analogue of → [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) — Doppler reading is ghost-sensitive, Higgs reading is not
- same mechanism as → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) — boost ⇔ complex z
- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision)
- same mechanism as → [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) — |tr| > 2

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) (analogue of); [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) (analogue of); [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) (same mechanism as)

### #44 · 0.540 · Krein collisions (how ghosts are born) <a id="krein-collision"></a>

**Label:** Theorem · **id:** `krein_collision` · **quadrant:** RH-sharp

*In plain words:* Zeros on the line carry a sign; two can only leave the line together if they meet with opposite signs.

**Core.** TAA Lemma 111: semisimple unit-spectrum F strongly stable ⇔ Krein form definite on each eigenspace; ghosts born only at opposite-sign collisions (710/710 births). For ζ the graphical Krein sign alternates ⇒ no protection; Λ ≥ 0 ⇒ ζ not heat-flow stable.

**Numbers.** 300 paths: 710 births, all opposite-sign

**Also known as:** Krein sign; opposite-sign collision; strong stability

**Axes:** geometry over F_q, ghost-sensitive

**TAA lemmas:** 27, 41, 111, 120, 152, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Krein = stability, not positivity; presupposes unit spectrum (TAA Lemma 111 circularity).

**Relations (outgoing):**

- analogue of → [de Bruijn–Newman constant Λ](#debruijn-newman) — heat-flow collisions
- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — pair leaves as (γ ± iδ)²
- same mechanism as → [Definite cup square / Krein one-liner](#definite-cup-square) — Krein one-liner (TAA Lemma 152 Prop 2.1)
- same mechanism as → [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) — hyperbolic block = off-line pair (claim 7, Restatement)

**Relations (incoming):** [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (same mechanism as); [de Bruijn–Newman constant Λ](#debruijn-newman) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (analogue of); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of)

### #49 · 0.540 · Fake Weil polynomials (finite ghosts) <a id="fake-weil-poly"></a>

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

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (fails for); [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (fails for); [Tate count / Picard number (ghost-blind)](#tate-count) (fails for); [Counts vs quadratic positivity](#count-positivity) (fails for)

### #72 · 0.452 · Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick <a id="deligne-tensor-power"></a>

**Label:** Cited · **id:** `deligne_tensor_power` · **quadrant:** true but ghost-blind/untested

*In plain words:* Deligne proved the Weil conjectures without the Hodge index theorem, but still with a positivity: Rankin’s positivity of coefficients of tensor powers.

**Core.** Deligne, Weil I (Publ. IHÉS 43, 1974, 273–307): RH over F_q without a Hodge index theorem — Lefschetz pencils and monodromy (SGA 7) reduce to a local system on a curve; Rankin's trick (Rankin 1939) bounds weights through L-functions of tensor powers. It still uses positivity: of the coefficients of those L-functions (TAA Lemma 152, correction 4). For ζ no tensor-power analogue is known to give more than zero-free regions (Heuristic, BR-4).

**Also known as:** Weil I; Rankin trick; tensor-power trick

**Axes:** geometry over F_q, sign/positivity (Ax2)

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 0.8 → priority 0.452

> ⚠ **Correction / caution.** 'No positivity' is wrong: Rankin's coefficient positivity is used; what is avoided is a Hodge index theorem (TAA Lemma 152, correction 4).

> ❓ **Not verified / open.** Numdam record and reference list opened; the argument itself is standard knowledge (BIB), not re-read.

**Relations (outgoing):**

- analogue of → [RH for curves over F_q (Weil)](#fq-curves) — a second proof of RH over F_q
- analogue of → [Hodge index theorem](#hodge-index) — replaces Hodge index by coefficient positivity

**Relations (incoming):** [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) (analogue of)

### #78 · 0.452 · Weight–monodromy conjecture (Deligne): status <a id="weight-monodromy"></a>

**Label:** Cited · **id:** `weight_monodromy` · **quadrant:** true but ghost-blind/untested

*In plain words:* Deligne conjectured that the monodromy filtration and Frobenius weights match; it is proved in characteristic p and in many but not all mixed-characteristic cases.

**Core.** For X proper smooth over a local field, Frobenius weights on gr_j^N H^i are i + j. Proved: equal characteristic (Deligne, Weil II 1980, over a curve; general char p via Terasoma, Ito); dim ≤ 2 in mixed characteristic (Rapoport–Zink + de Jong); p-adically uniformized varieties (Ito; Dat); cases of Shimura varieties; set-theoretic complete intersections in projective smooth toric varieties (Scholze, Publ. IHÉS 116, 2012, Thm 1.14). Open in general in mixed characteristic. (Curves and abelian varieties: curves are in dim ≤ 2; abelian varieties BIB, not opened.)

**Also known as:** WMC; monodromy filtration

**Axes:** geometry over F_q, structure/frame (Ax1)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- analogue of → [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) — ℓ-adic analogue of W(N)
- analogue of → [RH for curves over F_q (Weil)](#fq-curves) — weights

### #135 · 0.307 · Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity) <a id="gauss-sum-unitarity"></a>

**Label:** Theorem · **id:** `gauss_sum_unitarity` · **quadrant:** true but ghost-blind/untested

*In plain words:* A quadratic Gauss sum has absolute value exactly √p: this is the statement that the finite Fourier transform is unitary. For the CM curve y² = x³ − x and p ≡ 1 mod 4, the Frobenius eigenvalue is a Gaussian integer π with ππ̄ = p, so RH for this curve is the same kind of unitarity identity.

**Core.** |g|² = p (checked numerically for all odd p ≤ 691) = Plancherel for the finite Fourier transform, the same |x|^{½} twist as TAA Lemma 145. For p ≡ 1 mod 4, π ∈ ℤ[i], ππ̄ = p, a_p = 2 Re π, so |α| = √p is automatic. Over ℚ the analogue |ε| = 1 of a root number holds for Davenport–Heilbronn too: necessary, not sufficient. Open: a ζ-analogue in which the eigenvalue itself is a Gauss sum.

**Formula.** |g|² = p, ππ̄ = p, a_p = 2 Re π

**Numbers.** |g|² at p = 691: 691 (float) · max ||g|²−p| = 3.75e−12 (p ≤ 691) · g² = (−1/p)p to 3.7e−48 (p < 200, 50 digits)

**Also known as:** |g|² = p; finite Fourier transform unitary; CM Frobenius in ℤ[i]

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Unitarity identities of this kind are Ax3 (phase); over ℚ they are satisfied by DH too and cannot replace the sign.

**Relations (outgoing):**

- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — Plancherel / unitary |x|^{½} twist
- analogue of → [Hasse bound as a positive degree form](#hasse-pythagoras) — CM case: |π|² = p as a norm identity
- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) — phase side
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — |ε| = 1 holds for DH as well
- same mechanism as → [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) — Gauss sum = Weil index phase of the reflection (TAA Lemma 151)

**Relations (incoming):** [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (lives in); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (same mechanism as)

### #146 · 0.307 · Tate count / Picard number (ghost-blind) <a id="tate-count"></a>

**Label:** Theorem · **id:** `tate_count` · **quadrant:** true but ghost-blind/untested

*In plain words:* Counting algebraic classes on C×C does not see whether eigenvalues are on the circle.

**Core.** ρ(C×C) = 2 + Σ m(λ)m(q/λ) (Tate 1966, S–S §14.6); = 2g for squarefree, fakes too (TAA Lemma 93 Prop 2.3).

**Formula.** ρ = 2 + Σ m(λ) m(q/λ)

**Numbers.** 2923/2923 family checks (TAA Lemma 93)

**Also known as:** ρ = 2 + Σm(λ)m(q/λ); Tate classes

**Axes:** geometry over F_q, ghost-blind

**TAA lemmas:** 88, 93

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — fakes have the same count
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — counts are blind

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (analogue of); [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) (analogue of)

### #151 · 0.307 · Primary sign rule for a_p of y² = x³ − x <a id="primary-sign-rule"></a>

**Label:** Numerical · **id:** `primary_sign_rule` · **quadrant:** true but ghost-blind/untested

*In plain words:* For p ≡ 1 mod 4 write p = a² + b² with b even; the sign of a in a_p = 2a is fixed by a 2-adic normalisation (a + b ≡ 1 mod 4). The individual sign is phase data; RH is about the size |a_p| ≤ 2√p, not the sign.

**Core.** p = a² + b², b even, a_p = 2a with a + b ≡ 1 mod 4 (π primary mod (1 + i)³); checked for all 14 primes p ≡ 1 mod 4 below 120 (p = 5, 13, 17: a_p = −2, 6, 2). The individual sign is a 2-adic phase (ghost-blind); RH = |a_p| ≤ 2√p is a size statement. The distribution of the signs (Sato–Tate for CM curves) is a separate question; no citation given here. TAA Lemma 150 Prop 3.3: checked on all 147 primes ≡ 1 mod 4 below 2000. Individual sign = 2-adic phase (ghost-blind); the averaged sign is the Sarnak bias 1 − 2r (TAA Lemma 150 §2.1). CM angles: χ² = 0.34 on 10 bins (n = 39,175, p < 1e6), 50.07% positive; Hecke/Deuring equidistribution [BIB, not opened].

**Formula.** a_p = 2a, p = a² + b², a + b ≡ 1 mod 4

**Numbers.** 14/14 primes p ≡ 1 mod 4, p < 120 · 147/147 primes · χ² = 0.34 (10 bins)

**Also known as:** a_p = 2a; primary mod (1+i)³; sign of a_p

**Axes:** geometry over F_q, ghost-blind, numerics/certificate

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.307

> ⚠ **Correction / caution.** The minus sign in a₅ = −2 is not the positivity sign of RH: it is a phase (choice of primary generator), and RH bounds the size.

> ❓ **Not verified / open.** Sato–Tate/Hecke–Deuring citation for CM sign distribution not verified; none given.

**Relations (outgoing):**

- same mechanism as → [The prime 2 as the wild place](#prime-two-wild) — the normalisation is 2-adic
- same mechanism as → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) — a_p = 2 Re π
- fails for → [Castelnuovo–Severi inequality](#castelnuovo-severi) — the sign of a_p is not the Castelnuovo sign
- analogue of → [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) — individual (phase) vs averaged (positivity) sign

**Relations (incoming):** [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (analogue of)

### #163 · 0.267 · Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula <a id="gauss-half"></a>

**Label:** Theorem · **id:** `gauss_half` · **quadrant:** true but ghost-blind/untested

*In plain words:* Every odd prime p splits the nonzero residues into (p − 1)/2 squares and (p − 1)/2 non-squares; the quadratic character (x/p) records which. For an elliptic curve y² = f(x), a_p is minus the sum of these characters, and its value mod p is a Gauss-half power.

**Core.** a_p = −Σ_x (f(x)/p) for y² = f(x); Hasse: a_p ≡ coefficient of x^{p−1} in f^{(p−1)/2} mod p. For p ≡ 3 mod 4, (p + 1)/4 is an integer and √a = a^{(p+1)/4} mod p (691 → 173). y² = x³ − x: a_p = −2, 6, 2 for p = 5, 13, 17; a_p = 0 for p ≡ 3 mod 4, so N₆₉₁ = 692. The Gauss halves see only the coherent H¹(E, 𝒪), i.e. a_p mod p; the bound |a_p| ≤ 2√p needs positivity (Castelnuovo/Hodge index). TAA Lemma 150 Prop 3.1 (THM+NUM): verified for p = 3,5,7,11,13,17,29,37,41,691; 70,563 square roots a^{(p+1)/4} and a_p = 0 for p ≡ 3 mod 4, p < 2000. The half records a_p mod p (Hasse invariant = Frobenius on coherent H¹); the bound needs positivity (TAA Lemma 150 Thm 2.2).

**Formula.** a_p = −Σ_x (f(x)/p), a_p ≡ [x^{p−1}] f^{(p−1)/2} mod p

**Numbers.** (691 + 1)/4 = 173 · N₆₉₁(y² = x³ − x) = 692 · 691 → 173, N₆₉₁ = 692 · 70,563 residues checked

**Also known as:** Gauss 1/2 system; (p+1)/2 split; p/4 measure; 691 → 173; Hasse invariant

**Axes:** geometry over F_q, ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** a_p mod p is phase-type information; it does not give the size bound |a_p| ≤ 2√p.

> ⚠ **Correction / caution.** The ½ of (p ± 1)/2 is a counting half; relating it to the half-density ½ is an analogy.

**Relations (outgoing):**

- analogue of → [Half-density normalization |x|^{½}](#half-density) — the ½ in (p ± 1)/2 vs the unitary |x|^{½} twist; analogy
- fails for → [Castelnuovo–Severi inequality](#castelnuovo-severi) — mod-p data cannot give the size bound; that needs Castelnuovo–Severi
- same mechanism as → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity)
- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — the square root sits here; the inequality does not (TAA Lemma 150)
- lives in → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) — TAA Lemma 150 §3.2

**Relations (incoming):** [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as)

### #183 · 0.165 · Standard conjectures (Hodge type) <a id="standard-conj"></a>

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

**Relations (incoming):** [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of)

## Axis: physics analogue <a id="axis-physics-analogue"></a>

### #21 · 0.600 · Passivity (positive real part) <a id="passivity"></a>

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

### #47 · 0.540 · Decay rate ¼ <a id="decay-quarter"></a>

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

**Relations (incoming):** [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Cutoff saturation (class-number x is not the lever)](#cutoff-saturation) (same mechanism as); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #62 · 0.532 · Gain lines (active media) <a id="gain-line"></a>

**Label:** Analogy · **id:** `gain_line` · **quadrant:** sharp but interpretive

*In plain words:* A ghost acts like a gain line: negative absorption.

**Core.** TAA Lemma 146 §2: Re ξ′/ξ = Σ(σ−β)/((σ−β)² + (t−γ)²) — each zero is an absorption line to its right; an off-line zero gives a gain line. Grid σ ∈ [.505,1.1], t ∈ [80,92]: ξ min +0.00467; DH −66.84 at (0.794, 85.70), 1.89% negative; TAA Lemma 144 ghost −66.97 (1.94%). Lorentz model: dRe χ/dω −6 (absorber) / +6 (gain). TAA Lemma 154: measured widths — the near line of a DH ghost on σ = ½+d has FWHM 2|d − (β−½)| (match ≤ 3e−6, 13 d), inverted for d < β−½; as d → 0 its FWHM → Γ = 2(β−½) from below; the visible feature (near − mirror) keeps width ≈ ½(β−½) while its depth fades as 2d/(β−½)². KK sign invariant κ = Re F·∂_tIm F = −1/a³ flips at a gain line. [N] TAA Lemma 155: DH's gain lines reconstructed from ≈ 10 nonzero coefficients via the theta AFE (N = 13), and detected as ghost-map bumps from damped Dirichlet sums with X ≈ 55.

**Numbers.** ξ min +0.00467 · DH −66.84 (1.89% negative) · ghost −66.97 (1.94%)

**Also known as:** negative absorption

**Axes:** physics analogue, ghost-sensitive

**TAA lemmas:** 36, 146, 154, 155

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.532

**Relations (outgoing):**

- analogue of → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)
- fails for → [Passivity (positive real part)](#passivity)
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — gain line = negative width

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (fails for); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #69 · 0.452 · Lax–Phillips scattering <a id="lax-phillips"></a>

**Label:** Cited · **id:** `lax_phillips` · **quadrant:** true but ghost-blind/untested

*In plain words:* Scattering theory for waves on the modular surface; resonances relate to zeros.

**Core.** LP80 (read at source, TAA Lemma 118/TAA Lemma 141): s(z) = Λ(2s−1)/Λ(2s), Res_{s=1} = 3/π, poles at zeros of ζ(1+2iz), RH ⇒ Im z = ¼; Pavlov–Faddeev "RH iff Z″ decays exponentially"; spectrum of B″ = {(κ−1)/2}; "all that is missing is an appropriate inner product". TAA Lemma 118 Thm 3.1: ‖Z″‖ ≤ 1 unconditionally. TAA Lemma 153: bib verified by Crossref: Lax–Phillips, Scattering Theory for Automorphic Functions, Ann. Math. Stud. 87 (Princeton 1976; De Gruyter record dated 1977), doi 10.1515/9781400881567; Bull. AMS 2 (1980) 261–295 (Crossref pages; TAA Lemma 141 cited 261–296, TAA Lemma 153, correction 31); Pavlov–Faddeev, J. Soviet Math. 3 (1975) 522–548, doi 10.1007/BF01084688 (Zap. LOMI 27 (1972)). Poles of φ at ρ/2 = eigenvalues of the generator of the contraction semigroup Z(t) (LP80, read in TAA Lemma 141); contraction ⇒ Re s ≤ ½ (Re ρ ≤ 1) only; purity Re s = ¼ ⇔ RH: Restatement of MP4 ('all that is missing is an appropriate inner product').

**Numbers.** Res = 3/π · Im z = ¼

**Also known as:** LP scattering

**Axes:** physics analogue, phase/unitarity (Ax3)

**TAA lemmas:** 118, 141, 143, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** LP (6.19) rate sign ambiguous in OCR (TAA Lemma 118, correction 7).

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi)
- same mechanism as → [Decay rate ¼](#decay-quarter)
- same mechanism as → [Passivity (positive real part)](#passivity) — passive arrow (TAA Lemma 118)
- same mechanism as → [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift)

**Relations (incoming):** [Decay rate ¼](#decay-quarter) (special case of); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (same mechanism as); [Hilbert–Pólya](#hilbert-polya) (same mechanism as); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of)

### #75 · 0.452 · Maxwell construction / convex effective potential <a id="maxwell-effective-potential"></a>

**Label:** Theorem · **id:** `maxwell_effective_potential` · **quadrant:** true but ghost-blind/untested

*In plain words:* Doing the Legendre transform twice fills in a double well with a flat floor; this convexity comes for free only from a positive measure.

**Core.** The effective potential Γ = (log Z)* is convex automatically (a Legendre transform); for a double well the biconjugate V** is the convex envelope, flat between the two minima (Maxwell's common tangent; TAA Lemma 153 figure). log ∫e^{Jφ}dμ is convex in J by Hölder when μ ≥ 0; for a signed μ it can fail (TAA Lemma 153 example μ = ½δ₋₁ − 0.6δ₀ + ½δ₁). Physics citation left uncited (none opened).

**Also known as:** convex hull of a double well; Hölder convexity of log Z; Flat Potential (J. W. McGreevy animation)

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** No physics source opened; Hölder argument proved inline (TAA Lemma 153 §2).

**Relations (outgoing):**

- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — biconjugate = convex envelope
- analogue of → [Weil positivity criterion](#weil-positivity) — convexity needs a positive measure: Weil’s form has signed prime terms

### #82 · 0.423 · BRST / Gupta–Bleuler physical quotient <a id="brst"></a>

**Label:** Analogy · **id:** `brst` · **quadrant:** background

*In plain words:* Remove null and negative-norm states to get a positive physical space — as U^⊥ in Hodge index.

**Core.** TAA Lemma 115: BRST structure exact over F_q and ℚ [T]; "no ghosts" ⇔ RH [R]; missing positive V ≅ H¹ (Hilbert–Pólya) ⇒ restatement. TAA Lemma 146 §3: Gupta–Bleuler F₁^⊥/F₁ ≅ U^⊥; the BRST quartet decouples but the ghost quartet survives. PM-3 (BRST complex with H(Q) = U^⊥) open. Kugo–Ojima (TAA Lemma 146 §1, Analogy): BRST quartets are the closest physics analogue of ζ’s zero quartets, but a BRST quartet DECOUPLES (its ker Q part is null and is quotiented out), while a ghost quartet SURVIVES in the relative quotient with two positive directions (TAA Lemma 142). Higgs/ghost cancellation: which modes are physical vs null = the ghost question; Analogy only.

**Also known as:** ghost subtraction; PM-3; Kugo–Ojima quartet mechanism; Higgs/BRST ghost cancellation

**Axes:** physics analogue, reference/pole/cusp

**TAA lemmas:** 115, 146

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.4 → priority 0.423

> ⚠ **Correction / caution.** PM-3 is open.

> ❓ **Not verified / open.** PM-3 open.

**Relations (outgoing):**

- same mechanism as → [Hodge index theorem](#hodge-index)
- same mechanism as → [Primitive part V₀ = U^⊥](#primitive-part)
- analogue of → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — Kugo–Ojima quartet decouples; ghost quartet survives

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (same mechanism as); [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Hodge index theorem](#hodge-index) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Gribov ambiguity](#gribov) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #93 · 0.392 · Time delay (Wigner) <a id="time-delay"></a>

**Label:** Analogy · **id:** `time_delay` · **quadrant:** sharp but interpretive

*In plain words:* How long a wave packet lingers in the cusp; unlike the winding of the phase, the time-delay peak does see ghosts.

**Core.** TAA Lemma 143: winding ½ per zero for all β (ghost-blind), but time-delay peak at r = 42.85 is 3.09 (ζ), 27.22 (ζ + TAA Lemma 103 ghost), 27.42 (DH): ghost-sensitive. ζ time delay is negative for r ≲ 2.9 (min −3.87), so "positive delay" fails for ζ. TAA Lemma 120: dwell time ∂_x log|Φ| = −θ′(ω). TAA Lemma 118: Connes harmonic measure of an off-line zero = (1/2π) × TAA Lemma 117 excess group delay. TAA Lemma 153: Wigner time delay = −φ′/φ(½+it) = 2π dξ/dt (Birman–Krein); Wigner 1955 (Phys. Rev. 98, 145–147, doi 10.1103/PhysRev.98.145; Crossref) gives a causality lower bound, not positivity; ζ's delay negative only through −1/(¼+t²) (t ≤ 2.8); DH's positive everywhere, ghost = peak 27.27 at 42.84. TAA Lemma 154: the Wigner delay −φ′/φ is a sum of positive Breit–Wigner lines (two per zero, HWHM β/2, (1−β)/2); the group delay of ξ along σ (Re ξ′/ξ) is a sum of signed ones; negative group delay in Re s > ½ is a ghost (TAA Lemma 154, correction 12: optics 'superluminal is harmless' does not transfer).

**Numbers.** 3.09 / 27.22 / 27.42 at r = 42.85 · min −3.87

**Also known as:** phase derivative

**Axes:** physics analogue, ghost-sensitive, numerics/certificate

**TAA lemmas:** 117, 118, 120, 143, 153, 154

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.392

> ⚠ **Correction / caution.** Positive time delay fails for ζ (TAA Lemma 143 corrections).

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi)
- same mechanism as → [Gain lines (active media)](#gain-line) — ghost = extra delay
- same mechanism as → [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift)

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) (same mechanism as)

### #94 · 0.392 · Källén–Lehmann spectral positivity <a id="kallen-lehmann"></a>

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

### #131 · 0.324 · Kramers–Kronig relations <a id="kramers-kronig"></a>

**Label:** Analogy · **id:** `kramers_kronig` · **quadrant:** background

*In plain words:* Causal response: real (dispersive) and imaginary (absorptive) parts determine each other. Absorption’s sign is the passivity condition.

**Core.** TAA Lemma 146: dispersion = phase (ghost-blind), absorption sign = passivity ⇔ Lagarias ⇔ RH. TAA Lemma 154: for ξ′/ξ on a line σ: Im = −H[Re] + Σ_{β>σ} −2(t−γ)/((σ−β)²+(t−γ)²) [T]; FFT check on DH/ζ models (zeros |γ−100| < 40, t ∈ [−1900, 2100]): residual ≤ 1e−4 when no zero is right of σ; DH ghost term recovered to ≤ 9.5e−5. KK alone is an identity either way (TAA Lemma 146, correction 3); the sign of Re carries RH.

**Also known as:** KK; dispersion relation

**Axes:** physics analogue, phase/unitarity (Ax3), sign/positivity (Ax2)

**TAA lemmas:** 146, 154

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.324

> ⚠ **Correction / caution.** Passivity implies causality, not conversely (TAA Lemma 146).

**Relations (outgoing):**

- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive)
- same mechanism as → [Passivity (positive real part)](#passivity)

**Relations (incoming):** [Passivity (positive real part)](#passivity) (implies); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) (same mechanism as); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #132 · 0.324 · Gribov ambiguity <a id="gribov"></a>

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

### #136 · 0.307 · Nash–Kuiper flexibility / Onsager threshold <a id="nash-kuiper-onsager"></a>

**Label:** Cited · **id:** `nash_kuiper_onsager` · **quadrant:** true but ghost-blind/untested

*In plain words:* 

**Core.** No 'Nash–Kuiper transform': Nash 1954 / Kuiper 1955 C¹ isometric embeddings (flat torus in ℝ³, crumpled sphere); rigidity of convex surfaces for C^{1,α}, α > 2/3 (Borisov; Cohn-Vossen, Herglotz, Pogorelov for C²); h-principle α < 1/(1+n+n²) (CDS), 1/5 for 2D disks (DIS); threshold open in [1/5, 2/3] (½ suggested). Onsager 1/3 settled (CET 1994; Isett; BDLSV 2019). Cao–Hirsch–Inauen 1/3⁻ is Monge–Ampère, not isometric. ANALOGY: DH = the Nash–Kuiper surface (FE + phases, no Frobenius/H¹/cup ⇒ zeros unpinned).

**Axes:** physics analogue, ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — DH = Nash–Kuiper surface
- analogue of → [Rosati positivity](#rosati) — rigidity ↔ |α| = √q
- analogue of → [Hodge index theorem](#hodge-index)
- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- analogue of → [Connes–Consani sites](#connes-consani) — TAA Lemma 147 H¹/cup target

**Relations (incoming):** [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) (analogue of); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of)

### #150 · 0.307 · Bost–Connes KMS states <a id="kms-bost-connes"></a>

**Label:** Cited · **id:** `kms_bost_connes` · **quadrant:** true but ghost-blind/untested

*In plain words:* A quantum statistical system whose partition function is ζ(β); its positive KMS states and phase transition at β = 1 see ζ only at real β > 1, never the zeros.

**Core.** BC95 (Thm 5; CM08 3.32): Q-structure, Gal(Q^cycl/Q) symmetry, positive KMS states, ζ(β) real for β > 1; no trace equal to the Weil distribution found (TAA Lemma 30). TAA Lemma 38: strongest rigorous bridge; BC time is dual to rapidity, (β,t) = (Re s, −Im s); BC ordered phase ⇔ ω > ½. TAA Lemma 39: BC = tensor product over primes twisted by Galois. TAA Lemma 54/TAA Lemma 118: KMS/passivity uses ζ at real β > 1 ⇒ ghost-blind.

**Also known as:** BC system

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 30, 38, 39, 54, 118

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** BC95 Thm 5(a) states β < 1 (β ≤ 1 from CM08 3.32) (TAA Lemma 38 flag).

**Relations (outgoing):**

- analogue of → [Connes trace formula](#connes-trace)

### #172 · 0.256 · J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge <a id="wedge-flip-animation"></a>

**Label:** Heuristic · **id:** `wedge_flip_animation` · **quadrant:** background

*In plain words:* J. W. McGreevy’s animation shows a field turning, passing through a pure wedge and coming back with opposite sign; it is a picture of the sign at each zero.

**Core.** J. W. McGreevy's Aug 2025 GRQFT animation (panel 'Flat Potential Oscillations', 15 stills): the bright region moves clockwise; polarity flips when the pattern passes the 180° side (frames 5→6, 10→11), frame 10 is a pure wedge (constant on rays), a full cycle restores. Read as the sign layer (half_turn_sign_flip), not the missing surface (TAA Lemma 152, correction 8). Caveat: per-frame colour autoscaling could fake a flip; code lost (TAA Lemma 152, correction 11). Atlas v1.1: labelled still frames (Grok Bot re-renders, faithful to the analysed geometry, not J. W. McGreevy’s original code) in the atlas figure set animation_labelled. Reading: the animation as the dynamic F ↔ V (Frobenius/Verschiebung) sweep.

**Also known as:** GRQFT animation; pure wedge stage; polarity inversion

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 152, 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.7 · specificity 0.05 · tractability 0.5 · evidence 0.48 → priority 0.256

> ❓ **Not verified / open.** Reading from stills only; autoscaling not excluded.

**Relations (outgoing):**

- analogue of → [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) — polarity flip = sign of Z at a zero
- analogue of → [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) — dynamic F ↔ V sweep
- analogue of → [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) — lobes / wedge

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (analogue of); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (analogue of); [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) (corrects)

### #173 · 0.253 · Purity as distortionless transmission: weight strata = attenuation classes <a id="purity-distortionless"></a>

**Label:** Analogy · **id:** `purity_distortionless` · **quadrant:** sharp but interpretive

*In plain words:* On a perfect cable every frequency fades at the same rate; RH-type purity says every Frobenius eigenvalue has the same size, and rescaling by √q makes the fading disappear altogether.

**Core.** Lossless = unitary (|φ| = 1 on the line; after the half-density gauge no attenuation) [T]. Distortionless = every mode shares one attenuation rate [T for the line]. Frobenius eigenvalues |α| = q^{w/2}: α^n decays/grows at rate (w/2) log q, so the weight strata (rings |z| = q^{−σ}) are attenuation classes; purity (one ring) = distortionless [Restatement for Frobenius]; dividing by q^{1/2} (half Tate twist, the e^{−αx} factor) turns distortionless into lossless [T]. For ζ (no Frobenius) this is an Analogy. DH off-line zeros = modes with another attenuation = distortion [R, TAA Lemma 144 overdamped ghost]. Hyperbolic side: characteristics x ± ct are the null lines of dx² − c²dt²; Wick rotation t → iτ makes it dx² + c²dτ² (OS link) — a different sign flip from C → −C in the LC energy (TAA Lemma 153, correction 30). Elliptical conic sections, not elliptic curves. TAA Lemma 154: on the cusp purity = every zero has HWHM pair (¼, ¼), i.e. one lifetime [R]; DH ghost 1 measured (0.0957, 0.4042). On observer lines the FE pairs widths ±Γ (PT gain/loss shape, Analogy).

**Also known as:** lossless vs distortionless; attenuation classes

**Axes:** physics analogue, restatement ⇔ RH, structure/frame (Ax1)

**TAA lemmas:** 153, 154

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.253

**Relations (outgoing):**

- analogue of → [Distortionless line R/L = G/C](#distortionless)
- analogue of → [Half Tate twist ℚ(½)](#half-tate-twist) — ÷ q^{1/2}
- analogue of → [Weight ladder (modular weights)](#weight-ladder) — strata = attenuation classes
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — Wick rotation

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (analogue of); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as); [Distortionless line R/L = G/C](#distortionless) (analogue of)

### #174 · 0.226 · Buoyancy / Archimedes principle <a id="archimedes"></a>

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

### #175 · 0.226 · Distortionless line R/L = G/C <a id="distortionless"></a>

**Label:** Analogy · **id:** `distortionless` · **quadrant:** background

*In plain words:* Line that transmits without distortion; corresponds to β = ½.

**Core.** TAA Lemma 25/TAA Lemma 143: distortionless ⇔ β = ½. TAA Lemma 153 (sympy): telegrapher V_xx = LC V_tt + (RC+GL)V_t + RG V; gauge V = e^{−μt}w, μ = (R/L+G/C)/2, leaves w_xx − LC w_tt + [(CR−GL)²/(4CL)]w, zero iff R/L = G/C; then V = e^{−αx}F(t − x√(LC)), α = √(RG) (residual 0). Substituting e^{−αx} in the PDE alone does not remove the loss terms (first-order terms remain; TAA Lemma 153, correction 26). Cusp: u = log y, y²∂_y² = ∂_u² − ∂_u, a = e^{u/2}w ⇒ ∂_u² − ¼ (sympy), w = e^{itu} + φe^{−itu} at λ = ¼ + t²: distortionless (k = t, group velocity 1) w.r.t. λ − ¼ (Lax–Phillips shift), Klein–Gordon dispersive w.r.t. λ (v_g = k/√(k²+¼)).

**Formula.** R/L = G/C

**Also known as:** Heaviside condition; Heaviside condition at the cusp; half-density gauge

**Axes:** physics analogue, phase/unitarity (Ax3)

**TAA lemmas:** 25, 143, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- special case of → [Heaviside RLGC line](#heaviside)
- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — e^{u/2} = Heaviside gauge
- analogue of → [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless)

**Relations (incoming):** [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of); [Heaviside RLGC line](#heaviside) (same mechanism as)

### #176 · 0.226 · Heaviside RLGC line <a id="heaviside"></a>

**Label:** Analogy · **id:** `heaviside` · **quadrant:** background

*In plain words:* Transmission line with resistance, inductance, conductance, capacitance; used as a model for β.

**Core.** TAA Lemma 25: {R/L, G/C} = {β, 1 − β} in τ, orientation conventional (Prop 3.3); TAA Lemma 143 R/2L ↔ β/2; TAA Lemma 144 unordered {(1−β)/2, β/2} in u. TAA Lemma 153: gauge residual (CR−GL)²/(4CL) recomputed (sympy); the cusp is a distortionless line after the half-density gauge (see distortionless). LC energy ½LI² + ½CV² is an ellipse in (V,I) iff L, C > 0 (Hessian det LC): physical positivity = the input MP4 lacks (Analogy); C < 0 gives the hyperbola, C = 0 the double line.

**Also known as:** telegrapher; RLGC

**Axes:** physics analogue

**TAA lemmas:** 25, 143, 144, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.4 → priority 0.226

> ⚠ **Correction / caution.** The R/L, G/C ordering is a convention and differs between TAA Lemmas 25, 143 and 144.

> ❓ **Not verified / open.** R/L vs G/C ordering conventional.

**Relations (outgoing):**

- same mechanism as → [Distortionless line R/L = G/C](#distortionless)
- analogue of → [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) — ellipse / double line / hyperbola pencil

**Relations (incoming):** [Decay rate ¼](#decay-quarter) (same mechanism as); [Distortionless line R/L = G/C](#distortionless) (special case of)

### #177 · 0.226 · Mass-density positivity <a id="mass-density"></a>

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

### #178 · 0.212 · Higgs mechanism: negative mass² at the symmetric point <a id="higgs-negative-mass2"></a>

**Label:** Analogy · **id:** `higgs_negative_mass2` · **quadrant:** background

*In plain words:* 

**Core.** V = −μ²|φ|² + λ|φ|⁴: mass² = −μ² < 0 at φ = 0 (tachyonic); vacuum |φ|² = μ²/2λ, ⟨φ⟩ = v/√2, v = μ/√λ ≈ 246 GeV; m_H² = 2μ² > 0; Yukawa m_f = y v/√2 (√2 a convention). Positivity by CHOICE of vacuum — RH cannot choose (zeros are given). Mass is not friction (no dissipation, Lorentz invariant; TAA Lemma 150, correction 14). Honest link to GRR/relative counts: main term + oscillation ↔ vev + fluctuation only.

**Axes:** physics analogue, sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 150, 154

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

> ⚠ **Correction / caution.** The cusp two-Lorentzian “doublet” (TAA Lemma 153 Thm 7.7, TAA Lemma 154) is a parity doublet, not the Higgs complex doublet: no continuous group, no vev, no eaten modes (TAA Lemma 154, correction 13).

**Relations (outgoing):**

- analogue of → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) — tachyonic point vs off-line complex mass²
- analogue of → [Krein collisions (how ghosts are born)](#krein-collision) — instability ↔ complex eigenvalue pair
- analogue of → [Standard conjectures (Hodge type)](#standard-conj) — positivity input not derivable from structure
- analogue of → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — main term + oscillation ↔ vev + fluctuation

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (analogue of); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (analogue of)

### #179 · 0.212 · Klein–Gordon indefinite charge <a id="klein-gordon-charge"></a>

**Label:** Analogy · **id:** `klein_gordon_charge` · **quadrant:** background

*In plain words:* 

**Core.** KG charge i∫(φ̄∂_tφ − φ∂_tφ̄) is indefinite: ± frequency pairs = hyperbolic planes ↔ Krein form on the zero space (TAA Lemma 25 Thm 1.2) and TAA Lemma 142's U-part; positivity restored on a physical quotient ↔ Gupta–Bleuler/BRST (PM-3); Dirac square root ↔ Hilbert–Pólya self-adjointness (imposed in physics, to be proved for ζ: circular as input). Evenness/'two symmetric roots', spin/metaplectic covers and Feynman–Stueckelberg are ghost-blind.

**Axes:** physics analogue, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

**Relations (outgoing):**

- analogue of → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — hyperbolic plane
- analogue of → [BRST / Gupta–Bleuler physical quotient](#brst) — Gupta–Bleuler quotient
- analogue of → [Hilbert–Pólya](#hilbert-polya) — Dirac square root
- analogue of → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi)
- analogue of → [Metaplectic / Kubota cocycle](#metaplectic) — spin vs metaplectic double cover, both at 2

**Relations (incoming):** [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of)

### #180 · 0.212 · Anomalous dispersion <a id="anomalous-dispersion"></a>

**Label:** Analogy · **id:** `anomalous_dispersion` · **quadrant:** background

*In plain words:* Phase behavior near a line; ghost-blind.

**Core.** TAA Lemma 36: anomalous dispersion = analogy — gain lines are where absorption and phase disagree; THM 4.3 absorption–phase sum rule ∫₀ᵀ Re ξ′/ξ(σ₀+it)dt = π[N(T) − 2N(σ₀,T)] + …, deficit 2πN(σ₀,T) ≥ 0 (leads to zero density, not a proof). TAA Lemma 78: causality versus linewidth, Kramers–Kronig for the modular scattering matrix. TAA Lemma 146: dRe χ/dω at centre −6 (absorber) vs +6 (gain). TAA Lemma 154: precise form — per line Im F = −sgn(σ−β) H[Re F]; KK holds on σ iff no zero lies right of σ; a ghost flips the pairing locally (DH residual 9–20 at d = 0.25…0.05, = predicted term to 1e−4; ζ ≤ 1e−4). Re F = group delay d arg ξ/dt, Im F = −d log|ξ|/dt. Convention-free content: relative sign κ = −1/a³ (absorber < 0, gain > 0). J. W. McGreevy's strip prototype (TAA Lemma 36) = this object [R]; 'anomalous' in the optical sense [A].

**Also known as:** dispersion near resonance

**Axes:** physics analogue, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 36, 78, 146, 154

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

**Relations (outgoing):**

- same mechanism as → [Kramers–Kronig relations](#kramers-kronig)
- same mechanism as → [Gain lines (active media)](#gain-line)
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero)

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as)

### #181 · 0.181 · Lamb cutoff <a id="lamb-cutoff"></a>

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

## Axis: numerics/certificate <a id="axis-numerics-certificate"></a>

### #24 · 0.580 · Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side <a id="blockwise-weil-diagnostic"></a>

**Label:** Numerical · **id:** `blockwise_weil_diagnostic` · **quadrant:** RH-sharp

*In plain words:* Testing Weil’s form on pairs of tilted wave packets finds Davenport–Heilbronn’s two off-line zero pairs from the primes alone, while ζ stays positive on the same tests.

**Core.** 2×2 blocks of Weil's form at height γ on f± = e^{−u²/2w²}cos(γu)e^{±τu}; R: u ↦ −u swaps f±, so A = [[a,b],[b,a]], eigenvectors cosh/sinh tilts, hyperbolic iff |b| > a. Prime side (Dirichlet coefficients only) + arch (+ pole for ζ), X ≤ e^16; zero side = check. w = 1.5: prime side converged to ≤ 1e−7 (X-cut differences); ζ: no significant negative eigenvalue anywhere on γ ∈ [10,120] (all τ); DH (τ = 0.15, 0.3): hyperbolic on [85.48,85.92] and [114.04,114.29] plus a flank [84.36,84.77], nowhere else (λ₋ = −1.884 and −0.367 at τ = 0.3), first significant at X = e^12 (111,273 nonzero DH coefficients; ζ: 15,040 prime powers), matching the zero side; τ = 0 (1-dim) blind at w = 1.5. Planted ghost on ζ's zero side detected at [85.57,85.87]. The brief's cos/sin block is conformal (∝ I) and never hyperbolic (TAA Lemma 153, correction 8). Not a proof: prime side = zero side exactly (explicit formula); detection is finite-X resolution.

**Numbers.** DH w=1.5 τ=0.3: λ₋ = −1.884 at 85.70, −0.367 at 114.16 · first significant at log X = 12 · ζ: no significant negativity (w=1.5) · w=2.5: prime side not converged at X=e^16 (false negatives for ζ)

**Also known as:** BR-2; tilt block; boost block; prime-side block scan

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Circular as a proof: the prime side equals the zero side.

> ⚠ **Correction / caution.** w = 2.5 needs X > e^16.

> ⚠ **Correction / caution.** Zero list (TAA Lemma 141) differs from the converged prime side by up to 0.17 at γ ≈ 50, 100.

**Relations (outgoing):**

- lives in → [Weil positivity criterion](#weil-positivity)
- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision) — off-line pair = (1,1) block
- special case of → [Davenport–Heilbronn function](#davenport-heilbronn) — DH detection
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — R-symmetric block = reflection pair
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — block conic type
- analogue of → [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula)
- analogue of → [DH prime-side Gram test](#dh-prime-side-gram) — TAA Lemma 149 Gram, now blockwise
- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — window narrows to 0

**Relations (incoming):** [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (lives in)

### #25 · 0.580 · DH prime-side Gram test <a id="dh-prime-side-gram"></a>

**Label:** Numerical · **id:** `dh_prime_side_gram` · **quadrant:** RH-sharp

*In plain words:* Build the Weil-form Gram matrix of Davenport–Heilbronn from its Dirichlet coefficients alone; it turns indefinite at span 3.85.

**Core.** c_DH(n), n ≤ e^{3.85} ≈ 47, plus Γ-factor suffice; λ_max jumps −8e−9 → 3e−2 between L = 3.80 and 3.90.

**Also known as:** DH from primes

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 149

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

**Relations (outgoing):**

- special case of → [Relative Gram matrix G_rel](#relative-gram) — [instance-of]
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — [control-for] replaces TAA Lemma 141's uncertified zero list
- corrects → [Davenport–Heilbronn function](#davenport-heilbronn) — [replaces] zero-list control → prime side (TAA Lemma 149, correction 1, TAA Lemma 149, correction 4)

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (analogue of); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (analogue of)

### #63 · 0.492 · Near-null direction of ζ's relative Gram matrix <a id="near-null-anatomy"></a>

**Label:** Numerical · **id:** `near_null_anatomy` · **quadrant:** true but ghost-blind/untested

*In plain words:* The direction where ζ's relative Gram matrix is closest to zero is a function whose Fourier transform lives almost entirely below the first zero γ₁.

**Core.** Spectral mass below γ₁ = 14.13: 1−1.3e−4 (L=1), 1−7.5e−7 (4), 1−8.1e−9 (8), 1−6.9e−9 (16); U-fraction falls 0.63 → 0.20.

**Also known as:** RG-3/RG-4 anatomy

**Axes:** numerics/certificate

**TAA lemmas:** 149

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.492

**Relations (outgoing):**

- lives in → [Relative Gram matrix G_rel](#relative-gram) — [part-of]
- analogue of → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — [relates-to] U-component of the near-null vector
- implies → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) — [explains] small-δ onsets jump where ζ's λ plateaus (L ∈ [8,14])

### #64 · 0.492 · Integer dimension over 𝕊 (minimal generators) <a id="dim-s"></a>

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

### #91 · 0.400 · Ghost onset L* ≈ log(γ/2π) <a id="ghost-onset"></a>

**Label:** Numerical · **id:** `ghost_onset` · **quadrant:** RH-sharp

*In plain words:* The smallest window at which a ghost quartet can be detected; it grows like the log of the ghost’s height.

**Core.** TAA Lemma 103: onsets L* = 0.90, 1.15, 1.70, 3.45 for the test ghosts; L* ≈ log(γ/2π).

**Formula.** L* ≈ log(γ/2π)

**Numbers.** 0.90 · 1.15 · 1.70 · 3.45 · A at 85.699: δ.3085/.2/.1/.05/.02/.01 → L* 3.45/4.0/4.6/5.4/8.5/>16 (h=0.025) · γ₁: δ.2/.1/.05/.02/.01 → 1.0/1.05/1.25/1.4/1.8 · C at DH location 2.85; γ₄ δ.2 1.7; γ₅₀ δ.3/.1 4.9/6.35

**Also known as:** onset length; detection scale

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 103, 142, 149

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

> ⚠ **Correction / caution.** L* depends on kernel width h, not only span (TAA Lemma 149, correction 3): 3.45 vs 5.15 for h = 0.025 vs 0.05.

**Relations (outgoing):**

- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)

**Relations (incoming):** [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) (implies); [Ghost onset depends on kernel width](#onset-kernel-dependence) (corrects); [Certified positivity windows](#certified-windows) (fails for); [Yoshida window positivity](#yoshida) (fails for)

### #95 · 0.387 · Integer Ψ_n lattice test (negative result) <a id="psi-n-lattice"></a>

**Label:** Numerical · **id:** `psi_n_lattice` · **quadrant:** true but ghost-blind/untested

*In plain words:* Placing test functions only at logarithms of integers turns out too coarse to tell ζ from its fake.

**Core.** Classes K_h(·−log n), n ≤ K ≤ 90, h = 0.9/(4K): ζ λ_max(G_rel)/g₀ = −0.370…−0.416, n₊(C) = 1 (Hodge-index shape); DH λ_max ≈ −2.2, n₊ = 0; ghosts inserted into ζ stay negative (−0.4220 at DH location). Ghost-blind: diagonal-dominated, samples W only at log(j/k).

**Numbers.** K = 90: ζ −0.416, DH −2.226

**Axes:** numerics/certificate, ghost-blind, no-go / refuted

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.8 → priority 0.387

**Relations (outgoing):**

- fails for → [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) — integer lattice cannot test NS ⊋ U
- analogue of → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — ℚ mimic of Γ_{F^n}
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — TAA Lemma 149 continuous translates do separate

**Relations (incoming):** [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (same mechanism as)

### #99 · 0.365 · Cutoff saturation (class-number x is not the lever) <a id="cutoff-saturation"></a>

**Label:** Numerical · **id:** `cutoff_saturation` · **quadrant:** true but ghost-blind/untested

*In plain words:* On-line ζ terms decay like e^{−u/4} while unknown Maass terms do not, so going to larger class-number cutoffs adds almost nothing; the Maass list is the lever.

**Core.** TAA Lemma 148 Prop. sat: E1 sd flat for U = log x ∈ [14, 23] (zero 1: 0.86e−3–1.17e−3 at T_M = 35.4; 3.7e−5–4.5e−5 at T_M = 100). Residual rms 1.775e−4 → 2.47e−5 (7.2×) for 50 → 617 Maass forms; x = 1e8 → 1e10 changes it by < 1%. Noise rms ∝ T_M^{−2} predicts 8.0×.

**Formula.** info about β_k on [U, U+dU] ∝ e^{−U/2} dU

**Numbers.** 7.2× (measured) vs 8.0× (T_M^{−2}) · 1.775e−4 → 2.47e−5

**Also known as:** x-saturation; e^{−u/4} vs constant noise

**Axes:** numerics/certificate

**TAA lemmas:** 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

> ⚠ **Correction / caution.** TAA Lemma 148, correction 6: TAA Lemma 146/TAA Lemma 143 said reading β_k for k ≫ 1 needs smaller noise relative to x^{−1/4}; the cutoff is not the lever.

**Relations (outgoing):**

- same mechanism as → [Decay rate ¼](#decay-quarter) — e^{−u/4} envelope

### #100 · 0.365 · LMFDB level-1 Maass list complete to T = 100 <a id="lmfdb-maass-complete"></a>

**Label:** Numerical · **id:** `lmfdb_maass_complete` · **quadrant:** true but ghost-blind/untested

*In plain words:* The LMFDB rigorous list for PSL₂(ℤ) has 2202 forms to t = 184.9 but matches Weyl’s law only to T = 100 (617 forms); about 40–80 are missing above.

**Core.** TAA Lemma 148: 1092 even + 1110 odd; count − two-term Weyl ∈ [−2.9, 2.7] on [10, 100]; −39.7 at 105, −80.1 at 110, −82.0 at 120. First 50 agree with TAA Lemma 143’s list to 1e−7.

**Formula.** N(T) = T²/12 − (2T/π) log(T/(e√(π/2))) − 131/144 + o(T) [B, not opened]

**Numbers.** 617 at T = 100 (Weyl 617.3) · 2202 total

**Also known as:** maass_rigor level 1; 617 forms

**Axes:** numerics/certificate

**TAA lemmas:** 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.64 → priority 0.365

> ⚠ **Correction / caution.** Weyl constant term not opened in TAA Lemma 148.

> ❓ **Not verified / open.** Weyl law source not opened.

**Relations (outgoing):**

- implies → [Band criterion γ < 2T_M](#band-criterion) — sets T_M = 100, band edge 200

### #101 · 0.365 · Null-calibrated GLS matched filter <a id="null-calibrated-gls"></a>

**Label:** Numerical · **id:** `null_calibrated_gls` · **quadrant:** true but ghost-blind/untested

*In plain words:* Generalized least squares with the Maass-tail covariance plus a white floor chosen so that templates at random heights on the real, uninjected data give z-statistics with sd 1.

**Core.** TAA Lemma 148: tail-only covariance over-confident (null sd(z) 4.5–7.7); w* = 1.68e−6 (base), 7.17e−7 (T_M = 100, x = 1e10); A-templates still sd(z) 1.55–2.06 at w* (deflate). TAA Lemma 148, correction 1: subsampling every 4th point (Nyquist 157 < 600) aliased the tail — use the full grid.

**Formula.** C = C_tail + w*² I, C_tail(Δu) = ∫_{T_M}^{600} (t/6) 2|c(½+it)|² cos(tΔu) dt

**Numbers.** w* = 7.17e−7 · null sd(z) 7.7 at w = 1e−7

**Also known as:** white-floor calibration; w*

**Axes:** numerics/certificate

**TAA lemmas:** 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

> ⚠ **Correction / caution.** TAA Lemma 148, correction 1 aliasing

> ⚠ **Correction / caution.** TAA Lemma 148, correction 2 over-confidence

**Relations (outgoing):**

- same mechanism as → [Band criterion γ < 2T_M](#band-criterion) — exploits γ/2 < T_M

### #102 · 0.365 · Ghost onset depends on kernel width <a id="onset-kernel-dependence"></a>

**Label:** Numerical · **id:** `onset_kernel_dependence` · **quadrant:** true but ghost-blind/untested

*In plain words:* The span at which a fake off-line zero becomes visible depends on the test-function width h, not only on the span.

**Core.** Hats: DH-location ghost 3.45 (h=0.025) vs 5.15 (h=0.05); DH 3.85 vs 5.75; γ₁ δ=0.01 1.8 vs 3.85.

**Axes:** numerics/certificate

**TAA lemmas:** 149

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- corrects → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) — TAA Lemma 149, correction 3 (TAA Lemma 142 'invariant is the span')

### #111 · 0.347 · Certified positivity windows <a id="certified-windows"></a>

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

### #153 · 0.307 · Archimedean thresholds a* <a id="arch-threshold"></a>

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

### #167 · 0.267 · Yoshida window positivity <a id="yoshida"></a>

**Label:** Cited · **id:** `yoshida` · **quadrant:** true but ghost-blind/untested

*In plain words:* For test functions supported in a small enough window, Weil positivity holds unconditionally.

**Core.** Yoshida: W ≥ 0 for supp f ⊂ small window; TAA Lemma 10 window ≤ log 3. Below ghost onsets, so ghost-blind. TAA Lemma 153: CC21 credit Yoshida (ASPM 21, 1992, 281–325) with W∞(f) ≥ 0 for supp f ⊂ (1/2,2), f̂(±i/2) = 0, i.e. |log x| < log 2 (before the prime 2).

**Numbers.** log 3 (TAA Lemma 10)

**Also known as:** Yoshida 1992; small-support positivity

**Axes:** numerics/certificate, ghost-blind

**TAA lemmas:** 10, 142, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Unconditional windows never reach ghost onset.

> ⚠ **Correction / caution.** Atlas window ≤ log 3 (TAA Lemma 10) vs CC21/Yoshida (1/2, 2) ↔ log 2: different statements/normalizations, not reconciled here.

**Relations (outgoing):**

- same mechanism as → [Certified positivity windows](#certified-windows)
- fails for → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) — windows smaller than onset
- analogue of → [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity)

**Relations (incoming):** [Certified positivity windows](#certified-windows) (special case of); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (special case of); [Archimedean thresholds a*](#arch-threshold) (same mechanism as)

## Axis: ghost-sensitive <a id="axis-ghost-sensitive"></a>

### #26 · 0.580 · Chebyshev bias for elliptic curves (averaged sign of a_p) <a id="elliptic-chebyshev-bias"></a>

**Label:** Numerical · **id:** `elliptic_chebyshev_bias` · **quadrant:** RH-sharp

*In plain words:* Individual signs of a_p are phase data, but their running average is biased, and the bias is governed by the zeros of L(E, s) and the analytic rank, in the same way ψ(x) − x is governed by the zeros of ζ. An off-line zero would make the averaged sign blow up like a power of x.

**Core.** Sarnak, letter to Mazur (2007, opened): S_{1,E}(x) = (log x/√x) Σ_{p≤x} a_E(p)/√p has mean −2r + 1 under GRH + independence. TAA Lemma 150 NUM (p ≤ 1e7): log-mean of θ_E/√x = 0.942, −1.101, −3.189, 0.949 for 11a1, 37a1, 389a1, 32a (1 − 2r = 1, −1, −3, 1); ζ: (θ(x) − x)/√x log-mean −1.123. An off-line zero gives power-law growth x^{β−½}.

**Numbers.** 0.942 / −1.101 / −3.189 / 0.949 · log-density θ_E<0: 0.030, 0.972, 0.99996, 0.094

**Also known as:** average sign of a_p; prime race for a_p

**Axes:** ghost-sensitive, reference/pole/cusp, open target

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.64 → priority 0.580

> ⚠ **Correction / caution.** Literature citation to verify: none is given until opened at source.

> ⚠ **Correction / caution.** Counting version (signs of a_p) differs for CM vs non-CM curves (Sarnak); TAA Lemma 150 uses only the weighted sum.

> ❓ **Not verified / open.** to verify: the Chebyshev-bias citation for elliptic curves is unverified (not opened); no reference given.

**Relations (outgoing):**

- same mechanism as → [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) — Goldfeld product (log x)^r
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — averaged error term governed by zeros
- analogue of → [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) — individual sign (phase) vs averaged sign (zeros)

**Relations (incoming):** [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (analogue of)

### #27 · 0.580 · Ghost conventions A / B / C for spectral tests <a id="ghost-conv-abc"></a>

**Label:** Numerical · **id:** `ghost_conv_abc` · **quadrant:** RH-sharp

*In plain words:* A (TAA Lemma 103) replaces one on-line zero by a pair and so adds a zero (tests multiplicity); B compares the pair with an on-line double zero (pure β, O(δ²)); C replaces two neighbours by the pair (count preserved).

**Core.** Gram side: B's ghost world = A's (Prop AB); any on-line multiset gives M ⪰ 0, so positive λ comes only from δ; TAA Lemma 148, correction 5 multiplicity caveat applies to fitted readouts only (TAA Lemma 149, correction 5).

**Formula.** B: defect = term(½+δ) + term(½−δ) − 2 term(½)

**Numbers.** A 7171 / B 69 / C 10 100

**Also known as:** count-matched ghost; collision ghost; TAA Lemma 103 replace

**Axes:** ghost-sensitive

**TAA lemmas:** 103, 143, 148, 149

**Scores (Heuristic):** gap significance 0.5 (nearest gap: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.64 → priority 0.580

> ⚠ **Correction / caution.** Quote spectral ghost sensitivities in B.

> ❓ **Not verified / open.** Convention B is a proposal, not adopted.

**Relations (outgoing):**

- corrects → [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) — adds the multiplicity caveat for TAA Lemma 103
- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — pair ½ ± δ
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — [coincide-on] A = B as worlds (Prop AB)

**Relations (incoming):** [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) (same mechanism as)

### #46 · 0.540 · Ghost quartet ½ ± δ ± iγ <a id="ghost-quartet"></a>

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

**Relations (incoming):** [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) (same mechanism as); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as); [Gain lines (active media)](#gain-line) (analogue of); [BRST / Gupta–Bleuler physical quotient](#brst) (analogue of); [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) (same mechanism as); [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) (same mechanism as); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as)

### #50 · 0.540 · Ghost map Δ_w: zeros right of σ from damped Dirichlet sums <a id="ghost-map"></a>

**Label:** Theorem · **id:** `ghost_map` · **quadrant:** RH-sharp

*In plain words:* Subtract the smoothed comb from a damped prime sum: whatever is left is a bump at each zero that lies right of the observation line, and its phase tells how far right.

**Core.** [T] D_w(s) = Σ c(n) n^{−s} e^{−w² log² n/2} (entire), A_w = Gaussian-smoothed archimedean part, k_w*F_σ = smoothed comb on Re s = σ. Then A_w − D_w = Σ_ρ J_w(s−ρ) and Δ_w := A_w − D_w − k_w*F_σ = Σ_{β>σ} (√2π/w) exp((s−ρ)²/2w²): one Gaussian bump (width w) per zero right of σ, peak (√2π/w)e^{(β−σ)²/2w²}, phase slope (σ−β)/w² ⇒ γ̂, β̂, Γ̂ = 2(β̂−½). Identity holds whatever the zeros do (no RH content). Inputs: coefficients + Γ-factor + FE (F_σ by theta-function AFE); no zero list (TAA Lemma 155, correction 1). [N] DH: SNR (vs ζ control) ≥ 10 at X ≈ e^4 ≈ 55 (w = 0.4–0.5), β to 0.01 at X ≈ e^5 (w = 0.5, σ = 0.55), β̂ = 0.80852 / 0.65083 to ≤ 4e−9 at X = e^16 (SNR 6e6); ζ: no bump, floor ≤ 1e−6.

**Numbers.** [N] AFE comb = TAA Lemma 154 direct to 6.5e−13 (DH, σ = 0.55), N = 13 terms suffice · [N] ghost map SNR ≥ 10 at log X = 4 (w ≥ 0.4) · [N] β̂ = 0.80852, 0.65083 (|err| ≤ 4e−9) at log X = 16

**Also known as:** prime-side comb; coefficient-only ghost detector

**Axes:** ghost-sensitive, numerics/certificate

**TAA lemmas:** 155

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Not coefficients alone: needs Γ-factor and FE inside the strip (TAA Lemma 155, correction 1).

> ⚠ **Correction / caution.** Threshold measured only at t ≈ 86–114 (TAA Lemma 155, correction 7).

> ⚠ **Correction / caution.** ζ null result proves nothing about RH.

**Relations (outgoing):**

- lives in → [Davenport–Heilbronn function](#davenport-heilbronn) — detects both ghosts
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — Γ̂ from coefficients
- same mechanism as → [DH prime-side Gram test](#dh-prime-side-gram) — comparable coefficient threshold (Heuristic)
- same mechanism as → [Gain lines (active media)](#gain-line) — gain lines reconstructed
- special case of → [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) — AFE uses θ(1/x) = x^{3/2}θ(x) for DH
- same mechanism as → [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) — ghosts the map detects are certified by Krawczyk boxes (TAA Lemma 156)

### #52 · 0.540 · Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150 <a id="certified-zero-lists"></a>

**Label:** Theorem · **id:** `certified_zero_lists` · **quadrant:** RH-sharp

*In plain words:* Rigorous computer arithmetic proves that the zero lists used for the width measurements are complete and accurate, so the widths and flips are theorems, not fits.

**Core.** [N, rigorous] Arb ball arithmetic: argument principle on [−1,2]×[t_a,t_b] (segment enclosures excluding 0 in a sector < π), sign changes of the real completed function at γ ± 1e−12, Krawczyk boxes for off-line zeros; count = sign intervals + boxes ⇒ list complete, simple, on-line ones on the line. DH 2 < t < 135: 79 = 75 + 4 (standard list correct to 1e−12); ρ₁ = 0.808517182456637385553 + 85.699348485377592171929i, ρ₂ = 0.650830080609737082404 + 114.163342730756980904164i (± 6e−22). DH 135 < t < 200: 51 = 47 + 4; new pairs ρ₃ = 0.57435605045080599072 + 166.47930591316815587648i, ρ₄ = 0.724257694626809780211 + 176.702461242855825054474i. ζ 2 < t < 150: 52, all simple on the line. [T] ⇒ TAA Lemma 154 widths 2d, flips at d* = β−½ ∈ (0.30,0.35), (0.15,0.20), Γ₁ = 0.617034364913274771106, Γ₂ = 0.30166016121947416481 (± 3e−21), ghost FWHM → Γ from below.

**Numbers.** [N, rigorous] DH t < 135: 79 zeros = 75 on-line + 4 off-line (certified complete) · [N, rigorous] DH 135 < t < 200: 51 = 47 + 4 (new ghosts 166.479, 176.702) · [N, rigorous] ζ t < 150: 52 on-line · [N] first-order fit bounds ≤ 1.6e−5 rel (ghost 2: 6.3e−5 with tail subtracted)

**Also known as:** TAA Lemma 156 certificate; Krawczyk; argument principle count

**Axes:** ghost-sensitive, numerics/certificate

**TAA lemmas:** 156

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Fit outputs certified to first order only; nonlinear remainder measured (≤ 2.9e−10).

> ⚠ **Correction / caution.** Nothing certified above t = 200.

**Relations (outgoing):**

- lives in → [Davenport–Heilbronn function](#davenport-heilbronn) — certified ghosts
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — certified Γ
- same mechanism as → [Gain lines (active media)](#gain-line) — certified flips
- same mechanism as → [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) — TAA Lemma 156, correction 1: corrected cusp ghost-2 widths

**Relations (incoming):** [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as)

### #57 · 0.540 · de Bruijn–Newman constant Λ <a id="debruijn-newman"></a>

**Label:** Cited · **id:** `debruijn_newman` · **quadrant:** RH-sharp

*In plain words:* Heat flow on ξ; Λ ≥ 0 (Rodgers–Tao), RH ⇔ Λ = 0.

**Core.** Λ ≥ 0 ⇒ ζ not heat-flow stable (TAA Lemma 111). Healing times TAA Lemma 124/TAA Lemma 136 conflict. TAA Lemma 150 (opened): Rodgers–Tao Λ ≥ 0 (Forum Math Pi 2020), Polymath 15 Λ ≤ 0.22; H_0(z) = Ξ(z/2)/8, so t_RT = 4·t_Ξ (TAA Lemma 150, correction 8). DH heuristic (truncated list): pair at 85.70 closes at t_RT ≈ 0.177 (isolated 2δ² = 0.190); does not separate DH from ζ's known range.

**Numbers.** Λ ∈ [0, 0.22] · DH t*_RT ≈ 0.177 (H)

**Also known as:** heat flow; Λ ≥ 0

**Axes:** ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 111, 124, 136, 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** t* = 2δ² vs δ²/2.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Λ = 0
- analogue of → [Krein collisions (how ghosts are born)](#krein-collision)

**Relations (incoming):** [Krein collisions (how ghosts are born)](#krein-collision) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as)

### #61 · 0.540 · Bagchi recurrence <a id="bagchi"></a>

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

### #81 · 0.451 · Must-fail-for-DH acceptance test <a id="dh-acceptance"></a>

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

### #83 · 0.420 · Γ, the width of a zero: FWHM of its Breit–Wigner line <a id="gamma-fwhm-of-a-zero"></a>

**Label:** Restatement · **id:** `gamma_fwhm_of_a_zero` · **quadrant:** RH-sharp

*In plain words:* Each zero shows up as a bell-shaped line; its width at the critical line is twice its distance from the line. RH says every width is zero: every line becomes a spike.

**Core.** [T] On Re s = σ each zero ρ = β+iγ contributes to Re ξ′/ξ the signed line (σ−β)/((σ−β)²+(t−γ)²): FWHM 2|σ−β|, height 1/(σ−β), area π·sgn(σ−β) (Hadamard; TAA Lemma 146). [R] Γ_ρ := 2|β−½| = lim_{σ→½} FWHM (signed Γ± = 2(β−½); FE mirror has −Γ±); s = ½+iE puts ρ at E = γ − iΓ±/2. RH ⇔ all Γ_ρ = 0 ⇔ every line sharpens to πδ_γ as σ↓½. Γ is a limit, not observable on σ = ½ itself (Re ξ′/ξ ≡ 0 there by the FE; TAA Lemma 154, correction 6). 'Stable vs decaying' is convention-dependent; invariant: unitary state vs non-unitary ±Γ pair (in u = log x the ghost grows like e^{Γu/2}; TAA Lemma 154, correction 3). [N] TAA Lemma 154: ζ (5 zeros) and DH on-line: measured FWHM = 2d to 3.3e−7 rel over 13 lines d ∈ [0.01, 0.5], area π to 6e−7; DH ghosts: near line FWHM 2|d − (β−½)| (≤ 3e−6), flips to a gain line for d < β−½, → Γ = 0.617 / 0.302 from below (0.5970 / 0.2816 at d = 0.01; TAA Lemma 154, correction 2: not 'at least Γ'); visible feature width ≈ ½(β−½) constant, depth ≈ 2d/(β−½)² → 0; planted ghost (0.8, 40) identical. [N] TAA Lemma 155: Γ recovered without a zero list — Γ̂ = 2(β̂−½) = 0.61703, 0.30166 from the ghost map's phase slope (coefficients + Γ-factor + FE); exact comb from the theta AFE agrees with TAA Lemma 154 to 1e−12. Recorded in TAA Lemma 155 §0; certification in TAA Lemma 156. TAA Lemma 156 [N, rigorous]: certified (Arb) Γ₁ = 0.617034364913274771106 ± 9e−22, Γ₂ = 0.30166016121947416481 ± 3e−21; [T given certificates] flips at d* = β−½ in (0.30,0.35), (0.15,0.20); ζ targets simple on the line ⇒ FWHM 2d exact; ghost FWHM → Γ from below; [N] TAA Lemma 154 fits certified to first order (rel ≤ 1.6e−5; ghost 2 ≤ 6.3e−5 after tail subtraction).

**Numbers.** ζ: FWHM = 2d, rel err ≤ 3.3e−7 (13 d, 5 zeros) · DH ghost 1: Γ = 0.61703, FWHM 0.5970 at d = 0.01 · DH ghost 2: Γ = 0.30166, FWHM 0.2816 at d = 0.01 · feature depth −0.216 vs −2d/(β−½)² = −0.210 (d = 0.01)

**Also known as:** width of a zero; resonance width; Γ = 2|β−½|

**Axes:** ghost-sensitive, restatement ⇔ RH, numerics/certificate

**TAA lemmas:** 154, 155, 156

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** The ghost FWHM tends to Γ from below; it sharpens only on σ = β (TAA Lemma 154, correction 2).

> ⚠ **Correction / caution.** Decaying vs growing depends on the sign convention; the FE pairs ±Γ (TAA Lemma 154, correction 3).

> ⚠ **Correction / caution.** Hilbert–Pólya in widths is content-free without a natural operator (TAA Lemma 154, correction 5).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — all widths vanish
- same mechanism as → [Gain lines (active media)](#gain-line) — σ < β ⇒ inverted line
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias) — positivity of the comb on σ > ½
- analogue of → [Hilbert–Pólya](#hilbert-polya) — Γ = 0 ⇔ real energy
- same mechanism as → [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) — one width for every zero
- lives in → [Davenport–Heilbronn function](#davenport-heilbronn) — measured ghosts

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (same mechanism as); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (special case of); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (same mechanism as); [Gain lines (active media)](#gain-line) (same mechanism as); [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (corrects); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (special case of); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #104 · 0.360 · Ghost conventions (δ, heat-flow healing) <a id="ghost-conventions"></a>

**Label:** Theorem · **id:** `ghost_conventions` · **quadrant:** RH-sharp

*In plain words:* Bookkeeping for ghost parameters across lemmas; several conventions disagree.

**Core.** δ = β − ½ (TAA Lemmas 25, 103, 143) vs δ_ρ = 2β − 1 (TAA Lemma 144). Heat-flow healing time t* = 2δ² (TAA Lemma 124) vs δ²/2 (TAA Lemma 136).

**Numbers.** t* = 2δ² (TAA Lemma 124) · t* = δ²/2 (TAA Lemma 136)

**Also known as:** TAA Lemma 103 convention; δ_ρ

**Axes:** ghost-sensitive

**TAA lemmas:** 25, 103, 106, 124, 136, 143, 144, 148

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 0.8 → priority 0.360

> ⚠ **Correction / caution.** Always state which δ is used.

> ⚠ **Correction / caution.** TAA Lemma 148, correction 5: TAA Lemma 103 convention adds a zero (multiplicity); use count-matched B for β-sensitivity.

> ❓ **Not verified / open.** Conflicts unresolved.

**Relations (outgoing):**

- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)
- same mechanism as → [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc)

**Relations (incoming):** [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) (corrects); [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) (same mechanism as)

### #106 · 0.360 · S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T) <a id="s-of-t-remainder"></a>

**Label:** Theorem · **id:** `s_of_t_remainder` · **quadrant:** RH-sharp

*In plain words:* The zero count is a smooth main term plus a wiggly remainder S(T); a fake zero off the line only shows up when the count is compared with the sign changes on the line.

**Core.** N(T) = θ(T)/π + 1 + S(T) (ζ); the smooth part is the phase winding of χ, S(T) the remainder. Ghost status (TAA Lemma 153, correction 28): S(T) and N(T) count ALL zeros in the strip (argument principle), so S(T) alone is ghost-blind; the ghost shows only against the on-line count N₀(T) (Hardy-Z sign changes): DH 62 sign changes vs N = 66 on [10,120], deficits exactly 2 in [80,90] and [110,120] (TAA Lemma 152). The cusp phase φ smooths S out: its zero information arrives as Lorentzians of width ≥ min(β,1−β)/2.

**Also known as:** S(T); arg ζ(½+iT); Turing-type deficit

**Axes:** ghost-sensitive, numerics/certificate, restatement ⇔ RH

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- same mechanism as → [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) — smooth vs fluctuating part
- analogue of → [Tate count / Picard number (ghost-blind)](#tate-count)

## Axis: structure/frame (Ax1) <a id="axis-structure-frame-ax1"></a>

### #31 · 0.579 · Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS) <a id="lmhs-nilpotent-orbit"></a>

**Label:** Cited · **id:** `lmhs_nilpotent_orbit` · **quadrant:** true but ghost-blind/untested

*In plain words:* When a family of Hodge structures degenerates, the limit remembers a filtration with a definite form on each layer; this is the formal object behind the rings.

**Core.** A polarized VHS over a punctured disc has quasi-unipotent monodromy T; with N = log of its unipotent part, Schmid's nilpotent orbit theorem (Invent. 22, 1973, Thm 4.9) and SL₂-orbit theorem (Thm 5.13) give a limiting MHS: weight filtration W(N) centred at w, N^k: Gr_{w+k} ≅ Gr_{w−k}, the form Q(·, N^k C ·) positive on primitive pieces (CKS, Ann. 123, 1986). J. W. McGreevy's picture mapped: definite family = polarized VHS; origin = degeneration; rings = W(N); duality across strata = N^k. Correction: a half-turn (T = −1, finite order) has N = 0 and gives no weight filtration; the rings need unipotent monodromy such as τ ↦ τ + 1 (TAA Lemma 153, correction 11).

**Also known as:** LMHS; nilpotent orbit; SL₂-orbit; weight filtration W(N)

**Axes:** structure/frame (Ax1), sign/positivity (Ax2)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- analogue of → [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) — finite-order part only
- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann) — polarization on primitive pieces
- analogue of → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — local model of a degenerate H¹

**Relations (incoming):** [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (special case of); [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) (analogue of); [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) (analogue of)

### #35 · 0.579 · Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸) <a id="adelic-gluing-bruhat-tits"></a>

**Label:** Cited · **id:** `adelic_gluing_bruhat_tits` · **quadrant:** true but ghost-blind/untested

*In plain words:* The global object glues the hyperbolic disk at infinity to a tree at each prime; local RH holds at each prime for holomorphic forms, but the global RH does not follow.

**Core.** GL₂(ℚ)∖GL₂(𝔸)/K glues the upper half-plane (∞) with the (p+1)-regular Bruhat–Tits tree at each p (BIB, Serre 'Trees', unopened). Local RH at p = temperedness: Hecke eigenvalue in the ℓ²-spectrum [−2√p, 2√p] of the tree (Ramanujan–Petersson; proved for holomorphic weight ≥ 2 by Deligne 1974; open for Maass forms). GRH for these L-functions remains open. GL₁ version: Connes's adele class space 𝔸_ℚ/ℚ^× (Connes 1999). This is the 'global picture' J. W. McGreevy asked for: the gluing exists; the missing input is global positivity (MP4).

**Also known as:** Bruhat–Tits tree; adelic quotient; Ramanujan graph

**Axes:** structure/frame (Ax1), Spec ℤ gap

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 0.8 → priority 0.579

> ❓ **Not verified / open.** Serre Trees and the tree spectrum statement: BIB, not opened.

**Relations (outgoing):**

- lives in → [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) — ∞-component
- analogue of → [Connes trace formula](#connes-trace) — GL₁ adele class space
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — global positivity missing

### #43 · 0.540 · Poincaré disk: period domain, cusp degeneration and the trace classification <a id="poincare-disk-period-domain"></a>

**Label:** Theorem · **id:** `poincare_disk_period_domain` · **quadrant:** RH-sharp

*In plain words:* In the hyperbolic disk every motion is a rotation, a slide toward the boundary, or a boost between two boundary points; Frobenius of an elliptic curve is always a rotation, a ghost would be a boost.

**Core.** ℍ ≅ D = SL₂(ℝ)/SO(2) is the period domain of weight-1 rank-2 polarized Hodge structures; degeneration at a cusp with unipotent T: τ ↦ τ+1, N = log T, W(N) weights 0, 2. The Klein (projective) model is the Cayley–Klein geometry with a real absolute conic; the boundary = null rays of ℝ^{2,1}; SO⁺(2,1) ≅ PSL₂(ℝ). Trace classification: |tr| < 2 elliptic (rotation), |tr| = 2 parabolic (unipotent; horocycles to a cusp), |tr| > 2 hyperbolic (boost along a geodesic, two real fixed boundary points). Frob/√q has trace a/√q: elliptic ⇔ |a| < 2√q (Hasse; for a² = 4q Frobenius is ±√q·I, not unipotent). TAA Lemma 153 NUM: 11a1, 302 primes < 2000, max |a_p|/√p = 1.947 (all elliptic); fake trace 2cosh 0.3 = 2.091 hyperbolic. Ghost = boost (TAA Lemma 42 Def 6.12 'every arithmetic Frobenius Euclidean'; TAA Lemma 58 'RH = exclude boosts'). Not global: the cusp ≠ archimedean place (TAA Lemma 146); Maass–Selberg/Petersson positivity reaches only Re s = 1 and is ghost-blind (TAA Lemma 69, TAA Lemma 146).

**Numbers.** 11a1: max|a_p|/√p = 1.947 over 302 primes < 2000 · fake: tr = 2.091

**Also known as:** period domain; elliptic/parabolic/hyperbolic; SO(2,1) ≅ PSL₂(ℝ)

**Axes:** structure/frame (Ax1), geometry over F_q, ghost-sensitive

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- same mechanism as → [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) — real absolute = boundary
- same mechanism as → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — ghost = hyperbolic element
- analogue of → [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) — distance = ½ log CR
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — trace ⇔ conic type
- special case of → [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) — cusp LMHS
- corrects → [Cusp ≠ archimedean place](#cusp-vs-infinity) — disk boundary is not the archimedean place

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) (lives in); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (same mechanism as); [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) (special case of)

### #70 · 0.452 · Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points <a id="laguerre-formula"></a>

**Label:** Theorem · **id:** `laguerre_formula` · **quadrant:** true but ghost-blind/untested

*In plain words:* The angle between two lines is read off at infinity, from how the lines sit relative to two imaginary points; the metric lives at infinity.

**Core.** θ(ℓ₁,ℓ₂) = (1/2i) log CR(ℓ₁,ℓ₂; I, J), I, J = (1 : ±i : 0), isotropic lines y = ±ix; CR = (m₁−i)(m₂+i)/((m₁+i)(m₂−i)) = e^{2i(θ₁−θ₂)} (TAA Lemma 152 NUM 7.1e−16, 2000 pairs). The ½: θ is defined mod π (ℝP¹). The Euclidean metric is the pair {I, J} at infinity (the absolute). Resolves J. W. McGreevy's paradox: lines through 0 are not parallel at infinity (Riemann sphere: they meet again at ∞ with the same angle, opposite orientation; ℝP²: distinct points at infinity); the angle at 0 becomes a separation at infinity.

**Formula.** θ = (1/2i) log CR(ℓ₁,ℓ₂; I,J)

**Numbers.** max error 7.1e−16 (2000 random pairs)

**Also known as:** circular points I, J; the absolute; metric at infinity; Laguerre 1853

**Axes:** structure/frame (Ax1), sign/positivity (Ax2)

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Sign/orientation conventions: with CR as written Laguerre gives θ₁ − θ₂ mod π; only |θ| mod π is canonical (TAA Lemma 152, correction 9).

> ⚠ **Correction / caution.** Laguerre 1853 (Nouv. Ann. 12, 57–66): Numdam record and first page opened; the formula’s place in the paper not seen.

**Relations (outgoing):**

- special case of → [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) — imaginary absolute
- analogue of → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — rapidity ½ log CR vs ½ log q

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (analogue of); [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (analogue of); [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) (analogue of)

### #79 · 0.452 · Yoneda specification <a id="yoneda"></a>

**Label:** Theorem · **id:** `yoneda` · **quadrant:** true but ghost-blind/untested

*In plain words:* Specify the object by its properties (Ax1–Ax3).

**Core.** TAA Lemma 90: bare Hom sets do not determine an object (ℚ vs ℚ^(N)); naturality needed; representability ⇒ uniqueness/functoriality, presupposes positivity if it is an axiom. TAA Lemma 98 Prop 6.1: representable ⇒ unique; 𝔉(pt) ≠ ∅ ⇒ RH; "representability is the whole battle" (TAA Lemma 98, correction 19). TAA Lemma 137: T_W with Ax1–Ax3; existence open.

**Also known as:** T_W

**Axes:** structure/frame (Ax1)

**TAA lemmas:** 89, 90, 98, 137

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Ax1–Ax3 axioms (Yoneda specification)](#ax123)

### #113 · 0.325 · Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point <a id="dual-conic"></a>

**Label:** Theorem · **id:** `dual_conic` · **quadrant:** true but ghost-blind/untested

*In plain words:* The family of tangent lines of a conic is itself a conic; for a pair of crossing lines it collapses to the crossing point, counted twice.

**Core.** The tangent lines of a nondegenerate conic xᵀMx = 0 (3×3) form the dual conic uᵀM⁻¹u = 0 (equivalently adj M). For the affine block xᵀAx = 1: dual yᵀA⁻¹y = 1 (same type). A line pair (rank 2 in P²; J. W. McGreevy's pure wedge) has rank-1 adjugate: the dual is the vertex counted twice (claim 4 correct, for the 3×3 projective matrix). Fixes the 'unique absolute definition' of each stratum up to scale.

**Also known as:** adjugate; tangential conic; wedge dual

**Axes:** structure/frame (Ax1)

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- special case of → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — tangent data
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity)
- analogue of → [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) — metric read at infinity

**Relations (incoming):** [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (same mechanism as); [Heaviside RLGC line](#heaviside) (analogue of)

### #114 · 0.325 · Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1) <a id="morse-lobes-wedges-windows"></a>

**Label:** Theorem · **id:** `morse_lobes_wedges_windows` · **quadrant:** true but ghost-blind/untested

*In plain words:* Near a non-degenerate critical point a function looks like a quadratic form: a minimum gives closed elliptical loops (lobes), a saddle gives hyperbolas, and the level through the saddle is a pair of crossing lines (the wedge).

**Core.** [T] Morse lemma: near a non-degenerate critical point f = f(p) ± x² ± y² in suitable coordinates. Index 0 or 2: level sets are closed ellipse-like loops (J. W. McGreevy’s lobes). Index 1: level sets are hyperbolas and the critical level is a crossing line pair (the pure wedge, the dual conic of which is a double point: dual_conic). det Hess = 0 is the degenerate parabolic case (a² = 4q, double line). This is the local version of conic_type_at_infinity, and the block test of blockwise_weil_diagnostic: an off-line pair gives an index-1 (hyperbolic) 2×2 block, a ‘hyperbolic window’ (DH: [84.36,84.77], [85.48,85.91], [114.04,114.29], TAA Lemma 153). [A] Identification with the animation frames.

**Also known as:** lobes vs wedges vs hyperbolic windows; Morse lemma; saddle crossing

**Axes:** structure/frame (Ax1), sign/positivity (Ax2)

**TAA lemmas:** 152, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 0.8 → priority 0.325

> ⚠ **Correction / caution.** Standard Morse lemma; no source opened in a lemma. The reading of the animation frames is an Analogy (code lost, TAA Lemma 152, correction 11).

> ❓ **Not verified / open.** Chat-level concept; not a lemma result. Morse lemma not opened at source.

**Relations (outgoing):**

- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — local quadratic form
- same mechanism as → [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) — wedge ↔ double point
- lives in → [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) — hyperbolic window = index-1 block
- analogue of → [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) — lobes / wedge
- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — support window jumps at det = 0

**Relations (incoming):** [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #147 · 0.307 · Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial <a id="consani-archimedean-cohomology"></a>

**Label:** Cited · **id:** `consani_archimedean_cohomology` · **quadrant:** true but ghost-blind/untested

*In plain words:* At the infinite place there is a proved cohomology whose Frobenius has the Gamma factor as characteristic polynomial; it is purely local.

**Core.** Consani, Compositio 111 (1998) 323–358 (abstract read): a double complex with a monodromy-type operator N at the archimedean fibre, viewed as 'maximally degenerate' (analogue of LMHS); proves Deninger's conjecture that the archimedean Γ-factor is the (regularized) characteristic polynomial of an archimedean Frobenius on the N-invariants of the hypercohomology. Local only: says nothing about zeros (ghost-blind: DH has the Γ-factor of an odd character mod 5).

**Also known as:** Consani 1998; archimedean Frobenius; Deninger Γ-factor conjecture

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- special case of → [Deninger’s foliated program](#deninger) — archimedean Γ-factor proved
- analogue of → [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) — fibre at ∞ maximally degenerate
- lives in → [Archimedean place and Γ_ℝ factor](#archimedean-place)

**Relations (incoming):** [Deninger’s foliated program](#deninger) (analogue of)

### #159 · 0.267 · Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics) <a id="fundamental-domain-three-phases"></a>

**Label:** Theorem · **id:** `fundamental_domain_three_phases` · **quadrant:** true but ghost-blind/untested

*In plain words:* The modular surface has two cone points, one cusp and many closed geodesics: the three kinds of motion seen on the quotient.

**Core.** Elliptic points i (stabilizer ⟨S⟩) and ρ = e^{2πi/3} (⟨ST⟩) = CM points of discriminant −4, −3; one cusp (0 = S·∞ ~ i∞ for SL₂(ℤ); for Γ₀(N) the cusps 0 and ∞ are distinct, swapped by the Fricke involution); hyperbolic classes ↔ closed geodesics of length 2 log ε (Selberg's primes). Interior: Δ ≥ 0 (selberg_eigenvalue_mass_shell); cusp: unitary scattering φ (eisenstein_resonances_rho_half); CM points: Epstein/Hecke (epstein). The cusp ties them: its constant term carries ζ.

**Also known as:** three phases on Γ∖ℍ; CM points i, ρ; cusp 0 ~ i∞

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- special case of → [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) — quotient Γ∖ℍ
- same mechanism as → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — hyperbolic = boost
- same mechanism as → [Cusp ≠ archimedean place](#cusp-vs-infinity) — cusp is a point, not the place ∞

**Relations (incoming):** [Epstein zeta no-go](#epstein) (lives in); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (lives in)

### #169 · 0.267 · Sector map w = e^{iπs/2} <a id="sector-map-w"></a>

**Label:** Theorem · **id:** `sector_map_w` · **quadrant:** true but ghost-blind/untested

*In plain words:* Mapping the critical strip to a 90° sector puts the critical line on the 45° ray; the functional equation becomes w ↦ i/w.

**Core.** arg w = πσ/2: strip edges σ = 0, 1 → rays 90° apart, critical line → the 45° ray. s ↦ 1 − s is w ↦ i/w (reflection in the 45° ray composed with |w| ↦ 1/|w|; fixed points ±e^{iπ/4}), not a reflection (TAA Lemma 152, correction 6); the reflection in the 45° ray is s ↦ 1 − s̄, w ↦ i w̄ (NUM 4.5e−28, 4.0e−28). In this picture the 45° ray is the critical line, not a null ray.

**Also known as:** w = e^{iπs/2}; 45° ray

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — w ↦ i/w
- analogue of → [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip)

## Axis: phase/unitarity (Ax3) <a id="axis-phase-unitarity-ax3"></a>

### #40 · 0.540 · Zeros as Breit–Wigner resonances (line shapes, cusp doublets) <a id="breit-wigner-resonances"></a>

**Label:** Theorem · **id:** `breit_wigner_resonances` · **quadrant:** RH-sharp

*In plain words:* In scattering language every zero is a resonance peak; at the cusp it is a pair of peaks whose widths are equal exactly when the zero is on the line.

**Core.** [T] Breit–Wigner line (Γ/2)/((E−E₀)² + (Γ/2)²): FWHM Γ, area π, lifetime 1/Γ (Fourier image of e^{iE₀u−Γu/2}); BW 1936 Phys. Rev. 49, 519–531 (Crossref record only). Zero lines of ξ′/ξ on Re s = σ are signed BW lines (gamma_fwhm_of_a_zero). Cusp (TAA Lemma 153 Thm 7.7): −φ′/φ(½+it) = −1/(¼+t²) + Σ_ρ two positive BW lines at γ/2, HWHM β/2 (from ξ(2s−1)) and (1−β)/2 (from ξ(2s)); sum ½; no inverted lines on the cusp. [N] DH ghost 1 cusp widths 0.09574 / 0.40415 vs 0.09574 / 0.40426, amplitudes 2.000/2.000; ghost 2 0.1737/0.3219 vs 0.1746/0.3254 (far-tail limited). [R] parity-doublet splitting = unequal widths; [A] Higgs complex doublet (loose: no continuous group, vev, eaten modes); [A] ±Γ pair ↔ PT-symmetric gain/loss.

**Numbers.** cusp ghost 1: 0.09574/0.40415 (pred 0.09574/0.40426) · cusp ghost 2: 0.1737/0.3219 (pred 0.1746/0.3254) · TAA Lemma 117: min τ_d on [10,30], true ξ 0.00105 (d = 0.01); ghost (γ₁, 0.3) −0.22, −2.49 at d = 0.01, 0.1; excess delay 4π per quartet · TAA Lemma 146: min Re ξ′/ξ on σ ∈ [.505,1.1], t ∈ [80,92]: ξ +0.00467; DH −66.84 at (0.794, 85.70) · [N] TAA Lemma 156, correction 1: cusp ghost 2 widths 0.17458489/0.32541474 vs 0.17458496/0.32541504 after subtracting certified zeros < 200 (quadratic bg); TAA Lemma 154 0.1737/0.3219 superseded

**Also known as:** zeros_as_resonances; Lorentzian; Zeros as Breit–Wigner resonances; ghosts as gain lines; resonance doublet

**Axes:** phase/unitarity (Ax3), ghost-sensitive, physics analogue

**TAA lemmas:** 154, 117, 146, 156

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Higgs doublet comparison is a loose Analogy (TAA Lemma 154, correction 13).

> ⚠ **Correction / caution.** BW 1936 not opened; facts proved directly.

> ⚠ **Correction / caution.** A ghost’s width on σ = ½ + d tends to Γ = 2(β−½) from below as d → 0; it never stays “at least Γ” (TAA Lemma 154, correction 2).

> ⚠ **Correction / caution.** Optics’ “negative group delay is harmless” does not transfer: for ξ, RH ⇔ positive group delay on every line σ > ½ (TAA Lemma 154, correction 12; TAA Lemma 117).

> ⚠ **Correction / caution.** Lagarias 1999 (Hinkkanen) criterion: opened in TAA Lemma 146 and re-opened in TAA Lemma 154; TAA Lemma 117 proves τ_d > 0 ∀d ⇔ RH inline and cites only Lagarias–Suzuki.

> ⚠ **Correction / caution.** The TAA Lemma 154 cusp widths for DH ghost 2 (0.1737/0.3219) are superseded by 0.17458489/0.32541474 (predicted 0.17458496/0.32541504) once certified zeros below t = 200 are subtracted (TAA Lemma 156, correction 1).

**Relations (outgoing):**

- same mechanism as → [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) — poles at ρ/2
- same mechanism as → [Time delay (Wigner)](#time-delay) — Wigner delay = sum of BW lines
- same mechanism as → [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) — spectral density
- special case of → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — line shapes
- analogue of → [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) — widths (¼, ¼)
- same mechanism as → [Gain lines (active media)](#gain-line) — inverted Lorentzian = gain line
- same mechanism as → [Anomalous dispersion](#anomalous-dispersion) — J. W. McGreevy: direct touch point
- same mechanism as → [Kramers–Kronig relations](#kramers-kronig) — Im part = dispersive partner
- analogue of → [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) — loose: doublet only (TAA Lemma 154, correction 13)
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias) — no gain lines right of ½

**Relations (incoming):** [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (same mechanism as)

### #48 · 0.540 · Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼ <a id="eisenstein-resonances-rho-half"></a>

**Label:** Theorem · **id:** `eisenstein_resonances_rho_half` · **quadrant:** RH-sharp

*In plain words:* At the cusp the Eisenstein series scatters with a phase of modulus one; its poles sit at half the zeta zeros, all on one line exactly when RH holds.

**Core.** φ(s) = ξ(2s−1)/ξ(2s) for SL₂(ℤ): |φ(½+it)| = 1 (NUM 2e−31), φ(s)φ(1−s) = 1 (FE, ghost-blind; NUM 8e−32). Zeros ρ of ζ give poles of φ at s = ρ/2 (simple: |φ|·ε → 0.5146 at ρ₁/2): under RH all on Re s = ¼ (one stratum); an off-line zero β + iγ would sit at Re s = β/2 (DH-type fake: 0.404, 0.0957, 0.325, 0.175 vs 0.25). Constant term a₀(y) = y^s + φ(s)y^{1−s} on s = ½+it: half-density lobes y^{½}e^{±it log y}. Where Selberg's zeta picks these up (Hejhal, Venkov): BIB, unopened.

**Numbers.** |φ(½+it)| − 1 ≤ 2e−31 · residue scale 0.5146 at ρ₁/2

**Also known as:** scattering matrix φ; resonances ρ/2; cusp as tying section

**Axes:** phase/unitarity (Ax3), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- same mechanism as → [Cusp forms & Petersson positivity](#cusp-forms-petersson) — cusp = kernel of constant term
- analogue of → [Half-density normalization |x|^{½}](#half-density) — y^{½} lobes
- same mechanism as → [Connes trace formula](#connes-trace) — constant term ↔ cokernel of E
- same mechanism as → [Maass–Selberg relations](#maass-selberg)

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) (same mechanism as)

### #51 · 0.540 · Arithmetic unitarity ("RH = unitarity") <a id="arith-unitarity"></a>

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

### #85 · 0.420 · Why the area is π: the circle in every zero count (Basel as common origin) <a id="circle-pi-in-zero-counts"></a>

**Label:** Restatement · **id:** `circle_pi_in_zero_counts` · **quadrant:** RH-sharp

*In plain words:* The π in each zero’s area is the circle’s π, coming from the geometry of complex numbers; the same circle gives Euler’s π²/6, but the zeros do not explain π.

**Core.** [T] ∫ a/(a²+x²)dx = π sgn a = angle subtended by ℝ at ia = half of ∮dz/z = 2πi; P_a = (1/π)a/(a²+x²) is harmonic measure, Cayley-equivalent to the disk Poisson kernel (mass 1, NUM 40 digits); 2π = circumference/radius. [R] Area is a dimensionless invariant of the complex structure (scale- and coordinate-free yes), as C/d is of a round metric. Direction: the circle puts π into every zero count; the zeros do not derive π (TAA Lemma 154, correction 9). [T] Euler: ζ(2) = π²/6, ζ(2k) = rational·π^{2k} (sin product / π cot πz; NUM sanity ζ(2) − π²/6 = 2e−41). [R] Basel and the ±π area share an origin (the circle); NOT (±π)²/6 from residue areas: ζ(2k) is archimedean (Γ-factor, trivial zeros; ζ(1−2k) = −B_{2k}/2k) (TAA Lemma 154, correction 10). [C/O] ζ(3) irrational (Apéry, BIB); rationality of ζ(3)/π³ OPEN (TAA Lemma 154, correction 11); even/odd ↔ ghost-blind/sensitive is Heuristic at most. The locked ratio is the complex structure J, which also defines the Weil operator C = i^{p−q} (OS/Wick reading Analogy, TAA Lemma 153, correction 10).

**Also known as:** harmonic measure; Cayley transform

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 154

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** Not a derivation of π from zeros or RH (TAA Lemma 154, correction 9).

> ⚠ **Correction / caution.** ζ(2) is not a product of resonance areas (TAA Lemma 154, correction 10).

> ⚠ **Correction / caution.** ζ(3)/π³ irrational is unproved (TAA Lemma 154, correction 11).

**Relations (outgoing):**

- same mechanism as → [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) — π per line
- same mechanism as → [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) — circle / Fourier
- analogue of → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) — complex structure J
- corrects → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — zeros do not explain π

### #103 · 0.360 · Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept <a id="birman-krein-spectral-shift"></a>

**Label:** Theorem · **id:** `birman_krein_spectral_shift` · **quadrant:** RH-sharp

*In plain words:* The scattering phase at the cusp counts states; its derivative is a sum of positive bumps, one pair per zeta zero, whose widths tell where the zero sits.

**Core.** Birman–Krein (Dokl. 144 (1962) 475–478): det S(λ) = e^{−2πiξ(λ)} [Cs]. Cusp of SL₂(ℤ): S = φ (one cusp), φ(½+it) = Λ(2it)/Λ(1+2it), |φ| = 1 (NUM 3.9e−31, t ≤ 60), so dξ/dt = (1/2π)(−φ′/φ)(½+it) (sign convention). THEOREM (Hadamard; NUM ≤ 3.9e−6 with 1517 zeros + tail): −φ′/φ(½+it) = −1/(¼+t²) + Σ_ρ [a/(a²+(t−γ/2)²) + b/(b²+(t−γ/2)²)], a = (1−β)/2, b = β/2: each zero gives two Lorentzians of mass π (winding ghost-blind), widths ghost-sensitive. The only negative term is the ζ pole term −1/(¼+t²) (negativity t ≤ 2.8; TAA Lemma 153, correction 23 refined). DH (Λ entire): −φ′/φ > 0 everywhere (min 0.41 on [0.5,60]) even with its ghost, so density positivity is ghost-blind (TAA Lemma 153, correction 29); ghost = narrow Lorentzians (peak 27.27 at t = 42.84; predicted ghost part 25.84). The ratio across the y-axis = φ; for ζ the analogous ratio is χ(s) = ζ(s)/ζ(1−s), χ(½+it) = e^{−2iθ(t)} gives the smooth part θ/π of N(T).

**Numbers.** Lorentzian decomposition err ≤ 3.9e−6 (t ≤ 60) · DH peak 27.27 at t = 42.84 · ζ negativity only t ≤ 2.8

**Also known as:** spectral shift function; det S = e^{−2πiξ}

**Axes:** phase/unitarity (Ax3), ghost-sensitive, numerics/certificate, physics analogue

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- same mechanism as → [Scattering unitarity |φ| = 1](#scattering-phi) — phase of det S
- same mechanism as → [Time delay (Wigner)](#time-delay) — dξ/dt
- same mechanism as → [Maass–Selberg relations](#maass-selberg) — intercept
- same mechanism as → [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) — Lorentzians at γ/2

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) (same mechanism as)

### #107 · 0.360 · Two partners of a zero (duality vs conjugation) <a id="two-partners"></a>

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

### #110 · 0.347 · Automorphy defect (TAA Lemma 144) <a id="automorphy-defect"></a>

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

### #121 · 0.325 · S-mirror ρ ↦ 1 − ρ̄ <a id="s-mirror"></a>

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

### #133 · 0.307 · Half Tate twist ℚ(½) <a id="half-tate-twist"></a>

**Label:** Theorem · **id:** `half_tate_twist` · **quadrant:** true but ghost-blind/untested

*In plain words:* 

**Core.** ℚ(1) cyclotomic, H² = ℚ(−1); ℚ(½) not canonical: ℓ-adic F(½) needs a chosen √p (Katz–Rojas-León, opened); g_p² = (−1/p)p gives canonical √(p*) ∈ ℚ(ζ_p); √p for p ≡ 3 mod 4 costs √−1 (disc ℚ(√p) = 4p: ramified at 2; p* < 0: sign at ∞). Over ℝ canonical: Connes's E(f)(g) = |g|^{½} Σ f(qg) and C(1) = (j,λ) ↦ |j|λ. Two product formulas: ∏|x|_v = 1 (size: norm map, scaling flow, √ = critical line) vs ∏(a,b)_v = 1 (phase, obstruction at 2). HEURISTIC nexus: Deninger's cohomology contains an honest ℚ(½), MP4 stated on H¹(½); all twist data ghost-blind.

**Also known as:** ℚ(½); half twist

**Axes:** phase/unitarity (Ax3), ghost-blind, Spec ℤ gap

**TAA lemmas:** 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — real realization |·|^{½}
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — ±1 obstruction at 2, ∞
- same mechanism as → [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2)
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — half density = unitary reflection
- lives in → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) — phase side
- analogue of → [Deninger’s foliated program](#deninger) — placement of MP4
- same mechanism as → [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) — t^{¼}θ(t) invariant

**Relations (incoming):** [Connes trace formula](#connes-trace) (analogue of); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (lives in); [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of)

### #134 · 0.307 · Functional equation ξ(s) = ξ(1 − s) <a id="functional-equation"></a>

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

**Relations (incoming):** [Davenport–Heilbronn function](#davenport-heilbronn) (fails for); [Epstein zeta no-go](#epstein) (fails for); [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (implies); [Scattering unitarity |φ| = 1](#scattering-phi) (special case of); [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) (same mechanism as); [Sector map w = e^{iπs/2}](#sector-map-w) (same mechanism as)

### #137 · 0.307 · Half turn = sign flip (S² = −I, root number, Hardy Z sign changes) <a id="half-turn-sign-flip"></a>

**Label:** Theorem · **id:** `half_turn_sign_flip` · **quadrant:** true but ghost-blind/untested

*In plain words:* Turning by 180° is a sign: it flips modular forms of odd weight, gives the root number, and is the sign change of Hardy’s Z at each zero on the line.

**Core.** S² = −I in SL₂(ℤ) acts by (−1)^k on weight k (odd weights vanish; weight ½ needs the metaplectic cover). s ↦ 1 − s is the 180° rotation about ½; its sign is the root number (+1 for ζ, −1 for 37a1, forcing L(E,1) = 0). Hardy Z(t) = e^{iϑ(t)} ζ(½ + it) is real; it changes sign at each on-line zero of odd order. An off-line pair adds 2 to N(T) and no sign change. TAA Lemma 152 NUM (t ∈ [10,120], step 0.01): ζ 38 sign changes / 38 zeros; DH 62 / 66, the two deficits of 2 exactly in [80,90] and [110,120] (off-line pairs 85.699, 114.163). ℝP¹ = directions mod 180°; tautological bundle = Möbius band (the sign).

**Numbers.** ζ: 38/38 on [10,120] · DH: 62 sign changes vs N = 66; 5 vs 7 on [80,90] and [110,120] · |Im Λ_DH|/|Λ_DH| ≤ 7.1e−12 on the line

**Also known as:** wedge; S² = −I; root number; Hardy Z sign changes; Möbius band

**Axes:** phase/unitarity (Ax3), ghost-blind, numerics/certificate

**TAA lemmas:** 152

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Ghost-blind at on-line zeros (DH flips like ζ); off-line zeros appear only as missing flips against a global count N(T) (argument principle, Turing-type): detection, not positivity (TAA Lemma 152, correction 8).

**Relations (outgoing):**

- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — S² = −I; weight ½
- same mechanism as → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — s ↦ 1 − s half turn; root number
- corrects → [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) — the wedge is the sign layer, not the missing surface (TAA Lemma 152, correction 8)

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (analogue of); [Sector map w = e^{iπs/2}](#sector-map-w) (analogue of); [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #139 · 0.307 · Cup product / Poincaré duality pairing <a id="cup-product"></a>

**Label:** Theorem · **id:** `cup_product` · **quadrant:** true but ghost-blind/untested

*In plain words:* The pairing of cohomology classes; it gives the duality partner of a zero, ghosts included.

**Core.** Duality partner via cup product (TAA Lemma 93); positivity needs conjugate + Hodge structure (HR).

**Also known as:** ∪; duality pairing

**Axes:** phase/unitarity (Ax3), ghost-blind, structure/frame (Ax1)

**TAA lemmas:** 93, 134, 138, 151

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- same mechanism as → [Two partners of a zero (duality vs conjugation)](#two-partners)
- analogue of → [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) — K = ω₁₃∧ω₂₃

**Relations (incoming):** [Definite cup square / Krein one-liner](#definite-cup-square) (lives in); [Hodge–Riemann bilinear relations](#hodge-riemann) (special case of); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Two partners of a zero (duality vs conjugation)](#two-partners) (same mechanism as); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (same mechanism as)

### #149 · 0.307 · Hecke operators <a id="hecke"></a>

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

### #152 · 0.307 · Maass–Selberg relations <a id="maass-selberg"></a>

**Label:** Numerical · **id:** `maass_selberg` · **quadrant:** true but ghost-blind/untested

*In plain words:* Norm of truncated Eisenstein series expressed via φ and φ′; positivity there is automatic.

**Core.** TAA Lemma 146 §8.1: Maass–Selberg ‖Λ^T E‖² minimum 0.611 (ζ) vs 1.383 (DH) over 540 points ⇒ ghost-blind; it only constrains ζ(w) ≠ 0 for Re w > 1 (already known). TAA Lemma 153 (G): on s = ½+it, ‖Λ^T E‖² = 2 log T − (φ′/φ)(½+it) + (φ̄T^{2it} − φT^{−2it})/(2it) (form as in TAA Lemma 69, checked there to ≤ 1.9e−15 by quadrature against Sarnak's (25)); a line in log T with slope 2 and intercept −φ′/φ(½+it) (J. W. McGreevy's y-intercepts). The intercept is not a positive density: −φ′/φ(½+it) = −1.907 at t = 0.5, −0.135 at t = 2, +0.005 at t = 3 (TAA Lemma 153, correction 23). Positivity reaches only the edge Re s = 1 (TAA Lemma 69).

**Numbers.** 0.611 (ζ) · 1.383 (DH) · intercept −φ′/φ(½+3i) = 0.00508 · MS at T = 1,2,4,8,16 (t=3): 0.200, 1.059, 2.932, 4.334, 5.217

**Also known as:** truncated Eisenstein norm; Maass–Selberg intercept

**Axes:** phase/unitarity (Ax3), ghost-blind, reference/pole/cusp

**TAA lemmas:** 146, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.8 → priority 0.307

**Relations (outgoing):**

- same mechanism as → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct)

**Relations (incoming):** [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (same mechanism as); [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) (same mechanism as)

### #154 · 0.267 · Metaplectic / Kubota cocycle <a id="metaplectic"></a>

**Label:** Theorem · **id:** `metaplectic` · **quadrant:** true but ghost-blind/untested

*In plain words:* A 2-valued cocycle on SL₂ behind half-integer weight; structure without sign.

**Core.** TAA Lemma 146 §4: Kubota cocycle is a phase (Ax3); Hilbert product formula 300/300, quadratic reciprocity; θ weight ½ is metaplectic (a fourth root, TAA Lemma 141 §7) — mod 2 data, ghost-blind. TAA Lemma 151: θ multiplier eighth roots = Weil index; local covers split over SL₂(ℤ_p), p odd [BIB]; obstruction at 2 and ∞ = half-twist ±1.

**Also known as:** Kubota; double cover

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 141, 146, 151

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle)
- same mechanism as → [w₂ / Čech class (TAA Lemma 138)](#w2-cech)

**Relations (incoming):** [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #155 · 0.267 · Half-density normalization |x|^{½} <a id="half-density"></a>

**Label:** Theorem · **id:** `half_density` · **quadrant:** true but ghost-blind/untested

*In plain words:* Multiplying by |x|^{½} makes scaling unitary on L²; this is why the critical line is at ½.

**Core.** TAA Lemma 145 Thm twist: |x|^½ = (dx/d*x)^½ is unitary L²(dx) → L²(d*x); U_λ unitary with generator −(x∂_x + ½); Mellin is unitary only on Re s = ½ (Plancherel 0.35355339 both sides; at Re 0.4 a weighted norm 0.53173). Cusp gauge y²∂²(y^½W) = y^½(W″ − W/4). TAA Lemma 153 (E): (U_λ f)(x) = λ^{½}f(λx) on L²(ℝ₊,dx): U_λ x^{−s} = λ^{½−s} x^{−s} (NUM ≤ 2.2e−16), |λ^{½−s}| = 1 for all λ iff Re s = ½ (x^{−s} is a generalized eigenfunction, not in L²). Critical line = unitary spectrum of scaling; this is unitarity (Ax3), not positivity.

**Formula.** f ↦ |x|^{½} f

**Also known as:** ½ shift; unitary normalization; critical line = spectrum of unitary scaling

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 1, 141, 145, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** There are two ½’s (TAA Lemma 145 corrections): the unitary twist and the critical line.

**Relations (outgoing):**

- same mechanism as → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- same mechanism as → [Lamb cutoff](#lamb-cutoff)
- same mechanism as → [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) — half-density amplitude

**Relations (incoming):** [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (analogue of); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as); [Distortionless line R/L = G/C](#distortionless) (same mechanism as); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #156 · 0.267 · Theta inversion θ(1/t) = √t θ(t) <a id="theta-inversion"></a>

**Label:** Theorem · **id:** `theta_inversion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Poisson summation gives the functional equation; phase data.

**Core.** θ(1/x) = √x θ(x) gives Riemann’s FE and the boundary terms f(0), f̂(0) of 1/(s(s−1)) (TAA Lemma 36 §6). TAA Lemma 138 R4: theta inversion for x² + 5y² to 3e−30; Weil representation unitary, (ST)³ = Gauss sum · I; unitarity ⇒ FE only, ghost-blind (Thm). TAA Lemma 145: θ FE error 6.3e−26; TAA Lemma 146: θ S-error ≤ 2.5e−16, Fresnel = half-density × Weil index. TAA Lemma 151 centrepiece: θ(1/t) = √t θ(t) and ϑ(−1/τ) = √(τ/i) ϑ(τ) to ≤1.5e−51; √(1/i) = (1 − i)/√2 primitive 8th root (√2 in the phase); t^{¼}θ(t) inversion-invariant; unitary inversion on L²(ℝ₊,dx) is x^{−1}f(1/x) (TAA Lemma 151, correction 6). TAA Lemma 153: √(1/i) = e^{−iπ/4} is the Maslov factor of a negative-definite Hessian (stationary phase).

**Formula.** θ(1/t) = √t θ(t)

**Numbers.** rel err ≤ 1.5e−51 (t), 1.1e−51 (τ)

**Also known as:** Jacobi theta; Poisson summation; Jacobi θ reflection (θ(1/t) = √t θ(t))

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 36, 138, 145, 146, 151, 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- implies → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Weil index
- same mechanism as → [Half Tate twist ℚ(½)](#half-tate-twist)
- same mechanism as → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — reflection half

**Relations (incoming):** [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (special case of); [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (same mechanism as); [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as)

### #158 · 0.267 · Scattering unitarity |φ| = 1 <a id="scattering-phi"></a>

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

**Relations (incoming):** [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) (same mechanism as); [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) (same mechanism as)

### #160 · 0.267 · Hilbert reciprocity at 2: the odd halves become sign bits <a id="hilbert-reciprocity-at-2"></a>

**Label:** Cited · **id:** `hilbert_reciprocity_at_2` · **quadrant:** true but ghost-blind/untested

*In plain words:* At odd primes the halves (p − 1)/2 count squares; at 2 the corresponding quantities ε(u) = (u − 1)/2 and ω(u) = (u² − 1)/8 are sign bits. Hilbert reciprocity says the sign at 2 is fixed by the odd places and ∞. This is phase information, not positivity.

**Core.** (−1/p) = (−1)^{ε(p)}, (2/p) = (−1)^{ω(p)}. 2-adic Hilbert symbol: for a = 2^α u, b = 2^β v with u, v odd units, (a,b)₂ = (−1)^{ε(u)ε(v) + αω(v) + βω(u)} (Serre, A Course in Arithmetic, Ch. III, Thm 1). Product formula ∏ᵥ (a,b)ᵥ = 1 over all places including ∞ ⇒ the 2-adic sign is determined by the odd places and ∞; it is a restatement of quadratic reciprocity with both supplementary laws. ℚ₂^×/squares has order 8; ℤ₂^×/squares = {±1, ±5} has order 4: two sign bits, ε (sign of −1) and ω (the √2 / χ₈ bit). Checked: product formula holds for 3000 random pairs |a|, |b| ≤ 5000; ε, ω for u = 1, 3, 5, 7: (0,0), (1,1), (0,1), (1,0). Phase data (Ax3), ghost-blind: Davenport–Heilbronn shares the same reciprocity.

**Formula.** ∏ᵥ (a,b)ᵥ = 1, (a,b)₂ = (−1)^{ε(u)ε(v) + αω(v) + βω(u)}

**Numbers.** ℚ₂^×/(ℚ₂^×)² order 8 · ℤ₂^×/squares = {±1, ±5} · 3000/3000 product-formula checks · Serre III Thm 1 formula vs PARI hilbert: 3000/3000 · product formula 2000/2000 · ε/ω table u mod 16

**Also known as:** ε(u) = (u−1)/2; ω(u) = (u²−1)/8; 2-adic Hilbert symbol; sign of the prime 2; product formula

**Axes:** phase/unitarity (Ax3), ghost-blind, reference/pole/cusp

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 0.8 → priority 0.267

> ⚠ **Correction / caution.** The sign at 2 is a reciprocity sign (phase), not the positivity sign of RH; reading it as the half-density counterpart is an analogy.

> ⚠ **Correction / caution.** Equivalent to quadratic reciprocity, not to RH.

> ⚠ **Correction / caution.** Phase data: DH obeys the same reciprocity (TAA Lemma 150, correction 2).

> ❓ **Not verified / open.** to verify: Serre, A Course in Arithmetic, Ch. III Thm 1 not opened here; formula re-checked numerically via the product formula only.

**Relations (outgoing):**

- same mechanism as → [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) — odd halves (p ± 1)/2 ↔ sign bits ε, ω at 2
- same mechanism as → [The prime 2 as the wild place](#prime-two-wild) — 2 as the wild place
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Hilbert symbol = the cocycle behind the metaplectic cover
- same mechanism as → [√2 family](#sqrt2-family) — ω is the χ₈ = (2/·) bit

**Relations (incoming):** [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as)

### #162 · 0.267 · Eisenstein constant term & scattering φ(s) <a id="eisenstein-ct"></a>

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

### #164 · 0.267 · Gauss sum as canonical √(±p) <a id="gauss-sum-canonical-root"></a>

**Label:** Theorem · **id:** `gauss_sum_canonical_root` · **quadrant:** true but ghost-blind/untested

*In plain words:* 

**Core.** g_p = Σ (x/p) e^{2πix/p}: g_p² = (−1/p)p (NUM to 3.7e−48 for p < 200); g_p = √p (p ≡ 1) or i√p (p ≡ 3 mod 4) (Gauss's sign); so √(p*) is canonical in ℚ(ζ_p) given ψ; Katz–Rojas-León/Katz–Tiep use the Gauss sum as the half-twist constant.

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 151

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- same mechanism as → [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) — |g| = √p
- lives in → [Half Tate twist ℚ(½)](#half-tate-twist) — canonical √(±p)
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Weil index
- same mechanism as → [The prime 2 as the wild place](#prime-two-wild) — √−1 costs ramification at 2

### #165 · 0.267 · Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase <a id="maslov-legendre-fourier"></a>

**Label:** Theorem · **id:** `maslov_legendre_fourier` · **quadrant:** true but ghost-blind/untested

*In plain words:* The Fourier transform of a wave is, to leading order, its Legendre transform in the phase, a half-density in the amplitude, and a quarter-turn sign for each concave direction.

**Core.** ∫e^{i(S(x)−px)}dx ≈ √(2π)|S″(x_p)|^{−½} e^{−iS*(p)} e^{iπ sgn S″/4}, S′(x_p) = p, S*(p) = p x_p − S(x_p) (critical-value Legendre transform); exact for quadratic S (Fresnel). Tangent of slope p meets the y-axis at S − xS′ = −S*(p): the intercepts give the phase; the half-density |dx|^{½} → |dp|^{½} gives the amplitude |S″|^{−½}; the Maslov factor records the Hessian signature and jumps at caustics (S″ = 0), where stationary phase fails (Airy; TAA Lemma 153 NUM). TAA Lemma 153 NUM: rel. err 0.012 (λ=20), 0.003 (λ=80), both signs. e^{−iπ/4} = √(1/i) is the factor in ϑ(−1/τ) = √(τ/i)ϑ(τ) (TAA Lemma 151; 9e−17). Riemann–Siegel θ(t) = (t/2)log(t/2π) − t/2 − π/8 + 1/(48t) + … (NUM); −π/8 as a Maslov-type phase is Heuristic.

**Numbers.** rel. err 1.2e−2 (λ=20), 3.1e−3 (λ=80) · θ inversion 9.2e−17 · RS residual × 48t → 1.0000001 (t=1000)

**Also known as:** stationary phase; Maslov index

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 153

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Intercepts give the phase, not the half-density; the amplitude comes from the curvature S″ (TAA Lemma 153, correction 15).

> ⚠ **Correction / caution.** Hörmander / Guillemin–Sternberg: bibliographic data only (unopened).

**Relations (outgoing):**

- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — amplitude
- same mechanism as → [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) — √(1/i)
- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — Maslov index / Weil index
- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — phase = Legendre

**Relations (incoming):** [Half-density normalization |x|^{½}](#half-density) (same mechanism as)

### #168 · 0.267 · w₂ / Čech class (TAA Lemma 138) <a id="w2-cech"></a>

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

### #170 · 0.267 · Spin structure & theta characteristic <a id="spin-theta"></a>

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

### #171 · 0.256 · "Cocycles give structure, not sign" <a id="cocycle-principle"></a>

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

## Axis: restatement ⇔ RH <a id="axis-restatement-rh"></a>

### #84 · 0.420 · Mass shell / even Ξ: s(1−s) = ¼ + t² <a id="mass-shell-even-xi"></a>

**Label:** Restatement · **id:** `mass_shell_even_xi` · **quadrant:** RH-sharp

*In plain words:* Rewrite the zeros as 'masses squared': RH says every one of them is a real number at least ¼, like a stable particle.

**Core.** Ξ(t) = ξ(½+it) even and real ⇒ Ξ(t) = F(t²); RH ⇔ every root z = t² of F is real and positive ⇔ every nontrivial ρ(1−ρ) = σ(1−σ) + t² + it(1−2σ) is real and ≥ ¼ (then ρ(1−ρ) = ¼ + z). Dictionary: mass² = ¼ = ρ² (half density), momentum t; off-line pair = complex mass² (DH: z₀ = 7344.283 − 52.879i); real zero in (0,1) = tachyon. Connes 1999: 'positivity properties of Δ = D(1−D)', Selberg Laplacian λ = s(1−s) ≥ ¼.

**Formula.** RH ⇔ ρ(1−ρ) ∈ [¼, ∞) ∀ρ

**Numbers.** ζ: ρ(1−ρ) = 200.0405, 442.1762, … · DH: ρ₀(1−ρ₀) = 7344.5331 − 52.8794i

**Also known as:** s(1−s) = ¼ + t² mass shell; ζ mass shell; ρ(1−ρ) ≥ ¼

**Axes:** restatement ⇔ RH, sign/positivity (Ax2), physics analogue

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — restatement
- same mechanism as → [de Bruijn–Newman constant Λ](#debruijn-newman) — heat flow pushes complex z to the real shell
- same mechanism as → [Hilbert–Pólya](#hilbert-polya) — H² ≥ 0 with spectrum z
- same mechanism as → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — U-part = hyperbolic plane
- analogue of → [Krein collisions (how ghosts are born)](#krein-collision) — pair born as (γ ± iδ)²
- same mechanism as → [Half-density normalization |x|^{½}](#half-density) — mass ½

**Relations (incoming):** [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (analogue of); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

## Axis: open target <a id="axis-open-target"></a>

### #88 · 0.419 · Hilbert–Pólya <a id="hilbert-polya"></a>

**Label:** Open · **id:** `hilbert_polya` · **quadrant:** true but ghost-blind/untested

*In plain words:* Find a self-adjoint operator with spectrum the γ’s.

**Core.** Standard program: a self-adjoint/unitary realization with spectrum the γ’s would give RH. TAA verdicts: spinor route = Hilbert–Pólya in Clifford dress (TAA Lemma 104); 2B″ + ½ needs an inner product (TAA Lemma 105, LP80 "all that is missing is an appropriate inner product"); missing positive V ≅ H¹ (TAA Lemma 115); circular if the inner product is Weil’s form (TAA Lemma 138 R2); lossless Heaviside realization = Hilbert–Pólya [O] (TAA Lemma 144 HS-F). TAA Lemma 154: 'all widths Γ_ρ vanish' ⇔ RH ⇔ the γ's are the spectrum of some self-adjoint operator — content-free without a natural operator (TAA Lemma 154, correction 5).

**Also known as:** self-adjoint operator

**Axes:** open target, phase/unitarity (Ax3)

**TAA lemmas:** 104, 105, 115, 138, 144, 154

**Scores (Heuristic):** gap significance 0.8 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

**Relations (outgoing):**

- implies → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- same mechanism as → [Lax–Phillips scattering](#lax-phillips) — missing inner product

**Relations (incoming):** [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

## Axis: ghost-blind <a id="axis-ghost-blind"></a>

### #157 · 0.267 · The prime 2 as the wild place <a id="prime-two-wild"></a>

**Label:** Theorem · **id:** `prime_two_wild` · **quadrant:** true but ghost-blind/untested

*In plain words:* The only even prime is 2 (not √2). At 2 the Gauss halves break: (p − 1)/2 is not an integer, every model y² = f(x) has bad reduction, and the Hilbert symbol / metaplectic cocycle is wild. √2 enters through (2/p), which depends on p mod 8.

**Core.** Supplementary law: (2/p) = +1 ⇔ p ≡ ±1 mod 8; √2 ∈ ℚ(ζ₈), so (2/p) is the character χ₈ (the √2 family). At p = 2, (p − 1)/2 is not an integer and every Weierstrass model y² = f(x) is bad at 2; the Hilbert symbol and the metaplectic (Kubota) cocycle are wild at 2. All of this is phase data, hence ghost-blind.

**Formula.** (2/p) = (−1)^{(p²−1)/8}

**Also known as:** even prime; √2 and (2/p); supplementary law; bad reduction at 2

**Axes:** ghost-blind, phase/unitarity (Ax3), reference/pole/cusp

**TAA lemmas:** 150

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The even prime is 2, not √2; √2 appears only through the character (2/p) = χ₈(p).

> ⚠ **Correction / caution.** √2 is not a prime (TAA Lemma 150, correction 1); √2 enters via χ₈ and, separately, via Goldfeld's √2 (prime squares).

**Relations (outgoing):**

- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — wild at 2: Hilbert symbol / Kubota cocycle
- same mechanism as → [√2 family](#sqrt2-family) — χ₈ = (2/·), √2 ∈ ℚ(ζ₈)
- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle) — structure, not sign
- same mechanism as → [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) — sign bits ε, ω at 2

**Relations (incoming):** [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (same mechanism as)

## Index by rank

| # | priority | concept | label | quadrant |
|---|---|---|---|---|
| 1 | 0.720 | [Weil positivity criterion](#weil-positivity) | Cited | RH-sharp |
| 2 | 0.720 | [Davenport–Heilbronn function](#davenport-heilbronn) | Theorem | RH-sharp |
| 3 | 0.720 | [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) | Cited | RH-sharp |
| 4 | 0.720 | [Connes trace formula](#connes-trace) | Cited | RH-sharp |
| 5 | 0.720 | [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) | Theorem | RH-sharp |
| 6 | 0.720 | [Definite cup square / Krein one-liner](#definite-cup-square) | Theorem | RH-sharp |
| 7 | 0.720 | [Lagarias/Hinkkanen criterion](#lagarias) | Cited | RH-sharp |
| 8 | 0.720 | [Primitive part V₀ = U^⊥](#primitive-part) | Theorem | RH-sharp |
| 9 | 0.700 | [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) | Open | RH-sharp |
| 10 | 0.700 | [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) | Open | RH-sharp |
| 11 | 0.700 | [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) | Open | RH-sharp |
| 12 | 0.700 | [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) | Open | RH-sharp |
| 13 | 0.700 | [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) | Open | RH-sharp |
| 14 | 0.700 | [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) | Open | RH-sharp |
| 15 | 0.700 | [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) | Open | RH-sharp |
| 16 | 0.700 | [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) | Open | RH-sharp |
| 17 | 0.700 | [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) | Open | RH-sharp |
| 18 | 0.700 | [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) | Open | RH-sharp |
| 19 | 0.600 | [Relative Gram matrix G_rel](#relative-gram) | Restatement | RH-sharp |
| 20 | 0.600 | [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) | Restatement | RH-sharp |
| 21 | 0.600 | [Passivity (positive real part)](#passivity) | Restatement | RH-sharp |
| 22 | 0.600 | [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) | Restatement | RH-sharp |
| 23 | 0.600 | [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) | Restatement | RH-sharp |
| 24 | 0.580 | [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) | Numerical | RH-sharp |
| 25 | 0.580 | [DH prime-side Gram test](#dh-prime-side-gram) | Numerical | RH-sharp |
| 26 | 0.580 | [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) | Numerical | RH-sharp |
| 27 | 0.580 | [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) | Numerical | RH-sharp |
| 28 | 0.579 | [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) | Theorem | true but ghost-blind/untested |
| 29 | 0.579 | [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) | Theorem | true but ghost-blind/untested |
| 30 | 0.579 | [Ax1–Ax3 axioms (Yoneda specification)](#ax123) | Theorem | true but ghost-blind/untested |
| 31 | 0.579 | [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) | Cited | true but ghost-blind/untested |
| 32 | 0.579 | [Deninger’s foliated program](#deninger) | Cited | true but ghost-blind/untested |
| 33 | 0.579 | [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) | Theorem | true but ghost-blind/untested |
| 34 | 0.579 | [Parity argument: linear χ cannot see D²](#parity-linear-chi) | Theorem | true but ghost-blind/untested |
| 35 | 0.579 | [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) | Cited | true but ghost-blind/untested |
| 36 | 0.579 | [Tautology boundary (zero side vs prime side)](#tautology-boundary) | Theorem | true but ghost-blind/untested |
| 37 | 0.579 | [No étale H¹ for Spec ℤ](#no-etale-h1) | Theorem | true but ghost-blind/untested |
| 38 | 0.540 | [Rosati positivity](#rosati) | Theorem | RH-sharp |
| 39 | 0.540 | [Castelnuovo–Severi inequality](#castelnuovo-severi) | Theorem | RH-sharp |
| 40 | 0.540 | [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) | Theorem | RH-sharp |
| 41 | 0.540 | [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) | Theorem | RH-sharp |
| 42 | 0.540 | [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) | Theorem | RH-sharp |
| 43 | 0.540 | [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) | Theorem | RH-sharp |
| 44 | 0.540 | [Krein collisions (how ghosts are born)](#krein-collision) | Theorem | RH-sharp |
| 45 | 0.540 | [RH for curves over F_q (Weil)](#fq-curves) | Cited | RH-sharp |
| 46 | 0.540 | [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) | Theorem | RH-sharp |
| 47 | 0.540 | [Decay rate ¼](#decay-quarter) | Theorem | RH-sharp |
| 48 | 0.540 | [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) | Theorem | RH-sharp |
| 49 | 0.540 | [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) | Theorem | RH-sharp |
| 50 | 0.540 | [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) | Theorem | RH-sharp |
| 51 | 0.540 | [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) | Theorem | RH-sharp |
| 52 | 0.540 | [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) | Theorem | RH-sharp |
| 53 | 0.540 | [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) | Cited | RH-sharp |
| 54 | 0.540 | [Epstein zeta no-go](#epstein) | Theorem | RH-sharp |
| 55 | 0.540 | [Compatible complex structure J commuting with Frobenius](#compatible-j) | Theorem | RH-sharp |
| 56 | 0.540 | [de Branges spaces](#de-branges) | Cited | RH-sharp |
| 57 | 0.540 | [de Bruijn–Newman constant Λ](#debruijn-newman) | Cited | RH-sharp |
| 58 | 0.540 | [Hasse bound as a positive degree form](#hasse-pythagoras) | Theorem | RH-sharp |
| 59 | 0.540 | [Li criterion](#li-criterion) | Cited | RH-sharp |
| 60 | 0.540 | [Suzuki’s de Branges line from the prime side](#suzuki-line) | Cited | RH-sharp |
| 61 | 0.540 | [Bagchi recurrence](#bagchi) | Cited | RH-sharp |
| 62 | 0.532 | [Gain lines (active media)](#gain-line) | Analogy | sharp but interpretive |
| 63 | 0.492 | [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) | Numerical | true but ghost-blind/untested |
| 64 | 0.492 | [Integer dimension over 𝕊 (minimal generators)](#dim-s) | Numerical | true but ghost-blind/untested |
| 65 | 0.452 | [Hodge index theorem](#hodge-index) | Theorem | true but ghost-blind/untested |
| 66 | 0.452 | [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) | Cited | true but ghost-blind/untested |
| 67 | 0.452 | [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) | Theorem | true but ghost-blind/untested |
| 68 | 0.452 | [Hodge–Riemann bilinear relations](#hodge-riemann) | Theorem | true but ghost-blind/untested |
| 69 | 0.452 | [Lax–Phillips scattering](#lax-phillips) | Cited | true but ghost-blind/untested |
| 70 | 0.452 | [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) | Theorem | true but ghost-blind/untested |
| 71 | 0.452 | [Connes–Consani sites](#connes-consani) | Cited | true but ghost-blind/untested |
| 72 | 0.452 | [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) | Cited | true but ghost-blind/untested |
| 73 | 0.452 | [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) | Cited | true but ghost-blind/untested |
| 74 | 0.452 | [Cartan involution / compact unitary group](#cartan-involution) | Theorem | true but ghost-blind/untested |
| 75 | 0.452 | [Maxwell construction / convex effective potential](#maxwell-effective-potential) | Theorem | true but ghost-blind/untested |
| 76 | 0.452 | [Pole plane / Tate poles at s = 0, 1](#pole-plane) | Theorem | true but ghost-blind/untested |
| 77 | 0.452 | [Products grow linearly (2n), not quadratically](#products-linear) | Theorem | true but ghost-blind/untested |
| 78 | 0.452 | [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) | Cited | true but ghost-blind/untested |
| 79 | 0.452 | [Yoneda specification](#yoneda) | Theorem | true but ghost-blind/untested |
| 80 | 0.451 | [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) | Heuristic | sharp but interpretive |
| 81 | 0.451 | [Must-fail-for-DH acceptance test](#dh-acceptance) | Heuristic | sharp but interpretive |
| 82 | 0.423 | [BRST / Gupta–Bleuler physical quotient](#brst) | Analogy | background |
| 83 | 0.420 | [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) | Restatement | RH-sharp |
| 84 | 0.420 | [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) | Restatement | RH-sharp |
| 85 | 0.420 | [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) | Restatement | RH-sharp |
| 86 | 0.420 | [Two-point form g + iω ≥ 0](#two-point) | Restatement | RH-sharp |
| 87 | 0.419 | [Riemann hypothesis (target node)](#rh) | Open | true but ghost-blind/untested |
| 88 | 0.419 | [Hilbert–Pólya](#hilbert-polya) | Open | true but ghost-blind/untested |
| 89 | 0.419 | [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) | Open | true but ghost-blind/untested |
| 90 | 0.419 | [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) | Open | true but ghost-blind/untested |
| 91 | 0.400 | [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) | Numerical | RH-sharp |
| 92 | 0.392 | [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) | Analogy | sharp but interpretive |
| 93 | 0.392 | [Time delay (Wigner)](#time-delay) | Analogy | sharp but interpretive |
| 94 | 0.392 | [Källén–Lehmann spectral positivity](#kallen-lehmann) | Analogy | sharp but interpretive |
| 95 | 0.387 | [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) | Numerical | true but ghost-blind/untested |
| 96 | 0.377 | [Displaced reference (subtracting the pole)](#displaced-reference) | Heuristic | background |
| 97 | 0.377 | [Band criterion γ < 2T_M](#band-criterion) | Heuristic | background |
| 98 | 0.377 | [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) | Heuristic | background |
| 99 | 0.365 | [Cutoff saturation (class-number x is not the lever)](#cutoff-saturation) | Numerical | true but ghost-blind/untested |
| 100 | 0.365 | [LMFDB level-1 Maass list complete to T = 100](#lmfdb-maass-complete) | Numerical | true but ghost-blind/untested |
| 101 | 0.365 | [Null-calibrated GLS matched filter](#null-calibrated-gls) | Numerical | true but ghost-blind/untested |
| 102 | 0.365 | [Ghost onset depends on kernel width](#onset-kernel-dependence) | Numerical | true but ghost-blind/untested |
| 103 | 0.360 | [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) | Theorem | RH-sharp |
| 104 | 0.360 | [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) | Theorem | RH-sharp |
| 105 | 0.360 | [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) | Theorem | RH-sharp |
| 106 | 0.360 | [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) | Theorem | RH-sharp |
| 107 | 0.360 | [Two partners of a zero (duality vs conjugation)](#two-partners) | Theorem | RH-sharp |
| 108 | 0.347 | [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) | Cited | true but ghost-blind/untested |
| 109 | 0.347 | [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) | Theorem | true but ghost-blind/untested |
| 110 | 0.347 | [Automorphy defect (TAA Lemma 144)](#automorphy-defect) | Theorem | true but ghost-blind/untested |
| 111 | 0.347 | [Certified positivity windows](#certified-windows) | Numerical | true but ghost-blind/untested |
| 112 | 0.325 | [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) | Theorem | true but ghost-blind/untested |
| 113 | 0.325 | [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) | Theorem | true but ghost-blind/untested |
| 114 | 0.325 | [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) | Theorem | true but ghost-blind/untested |
| 115 | 0.325 | [√2 family](#sqrt2-family) | Theorem | true but ghost-blind/untested |
| 116 | 0.325 | [Closed geodesics on the modular surface](#closed-geodesics) | Theorem | true but ghost-blind/untested |
| 117 | 0.325 | [Cusp ≠ archimedean place](#cusp-vs-infinity) | Theorem | true but ghost-blind/untested |
| 118 | 0.325 | [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) | Cited | true but ghost-blind/untested |
| 119 | 0.325 | [Selberg resonances](#selberg-resonances) | Theorem | true but ghost-blind/untested |
| 120 | 0.325 | [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) | Theorem | true but ghost-blind/untested |
| 121 | 0.325 | [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) | Theorem | true but ghost-blind/untested |
| 122 | 0.325 | [Arakelov geometry](#arakelov) | Cited | true but ghost-blind/untested |
| 123 | 0.325 | [Density / volume reading](#density-volume) | Theorem | true but ghost-blind/untested |
| 124 | 0.325 | [F₁ base](#f1-base) | Cited | true but ghost-blind/untested |
| 125 | 0.325 | [Principalization](#principalization) | Theorem | true but ghost-blind/untested |
| 126 | 0.325 | [Spec ℤ is terminal](#spec-z-terminal) | Theorem | true but ghost-blind/untested |
| 127 | 0.325 | [Spinor/Clifford route](#spinor-route) | Theorem | true but ghost-blind/untested |
| 128 | 0.325 | [Weil Rosetta stone](#weil-rosetta) | Cited | true but ghost-blind/untested |
| 129 | 0.325 | [Cohesion (arena)](#cohesion) | Theorem | true but ghost-blind/untested |
| 130 | 0.325 | [Local-to-global failure](#local-global) | Theorem | true but ghost-blind/untested |
| 131 | 0.324 | [Kramers–Kronig relations](#kramers-kronig) | Analogy | background |
| 132 | 0.324 | [Gribov ambiguity](#gribov) | Analogy | background |
| 133 | 0.307 | [Half Tate twist ℚ(½)](#half-tate-twist) | Theorem | true but ghost-blind/untested |
| 134 | 0.307 | [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) | Theorem | true but ghost-blind/untested |
| 135 | 0.307 | [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) | Theorem | true but ghost-blind/untested |
| 136 | 0.307 | [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) | Cited | true but ghost-blind/untested |
| 137 | 0.307 | [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) | Theorem | true but ghost-blind/untested |
| 138 | 0.307 | [Archimedean place and Γ_ℝ factor](#archimedean-place) | Theorem | true but ghost-blind/untested |
| 139 | 0.307 | [Cup product / Poincaré duality pairing](#cup-product) | Theorem | true but ghost-blind/untested |
| 140 | 0.307 | [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) | Cited | true but ghost-blind/untested |
| 141 | 0.307 | [Cusp forms & Petersson positivity](#cusp-forms-petersson) | Theorem | true but ghost-blind/untested |
| 142 | 0.307 | [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) | Theorem | true but ghost-blind/untested |
| 143 | 0.307 | [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) | Theorem | true but ghost-blind/untested |
| 144 | 0.307 | [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) | Cited | true but ghost-blind/untested |
| 145 | 0.307 | [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) | Cited | true but ghost-blind/untested |
| 146 | 0.307 | [Tate count / Picard number (ghost-blind)](#tate-count) | Theorem | true but ghost-blind/untested |
| 147 | 0.307 | [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) | Cited | true but ghost-blind/untested |
| 148 | 0.307 | [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) | Cited | true but ghost-blind/untested |
| 149 | 0.307 | [Hecke operators](#hecke) | Theorem | true but ghost-blind/untested |
| 150 | 0.307 | [Bost–Connes KMS states](#kms-bost-connes) | Cited | true but ghost-blind/untested |
| 151 | 0.307 | [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) | Numerical | true but ghost-blind/untested |
| 152 | 0.307 | [Maass–Selberg relations](#maass-selberg) | Numerical | true but ghost-blind/untested |
| 153 | 0.307 | [Archimedean thresholds a*](#arch-threshold) | Numerical | true but ghost-blind/untested |
| 154 | 0.267 | [Metaplectic / Kubota cocycle](#metaplectic) | Theorem | true but ghost-blind/untested |
| 155 | 0.267 | [Half-density normalization |x|^{½}](#half-density) | Theorem | true but ghost-blind/untested |
| 156 | 0.267 | [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) | Theorem | true but ghost-blind/untested |
| 157 | 0.267 | [The prime 2 as the wild place](#prime-two-wild) | Theorem | true but ghost-blind/untested |
| 158 | 0.267 | [Scattering unitarity |φ| = 1](#scattering-phi) | Theorem | true but ghost-blind/untested |
| 159 | 0.267 | [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) | Theorem | true but ghost-blind/untested |
| 160 | 0.267 | [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) | Cited | true but ghost-blind/untested |
| 161 | 0.267 | [Counts vs quadratic positivity](#count-positivity) | Theorem | true but ghost-blind/untested |
| 162 | 0.267 | [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) | Theorem | true but ghost-blind/untested |
| 163 | 0.267 | [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) | Theorem | true but ghost-blind/untested |
| 164 | 0.267 | [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) | Theorem | true but ghost-blind/untested |
| 165 | 0.267 | [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) | Theorem | true but ghost-blind/untested |
| 166 | 0.267 | [Weight ladder (modular weights)](#weight-ladder) | Theorem | true but ghost-blind/untested |
| 167 | 0.267 | [Yoshida window positivity](#yoshida) | Cited | true but ghost-blind/untested |
| 168 | 0.267 | [w₂ / Čech class (TAA Lemma 138)](#w2-cech) | Theorem | true but ghost-blind/untested |
| 169 | 0.267 | [Sector map w = e^{iπs/2}](#sector-map-w) | Theorem | true but ghost-blind/untested |
| 170 | 0.267 | [Spin structure & theta characteristic](#spin-theta) | Theorem | true but ghost-blind/untested |
| 171 | 0.256 | ["Cocycles give structure, not sign"](#cocycle-principle) | Heuristic | background |
| 172 | 0.256 | [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) | Heuristic | background |
| 173 | 0.253 | [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) | Analogy | sharp but interpretive |
| 174 | 0.226 | [Buoyancy / Archimedes principle](#archimedes) | Analogy | background |
| 175 | 0.226 | [Distortionless line R/L = G/C](#distortionless) | Analogy | background |
| 176 | 0.226 | [Heaviside RLGC line](#heaviside) | Analogy | background |
| 177 | 0.226 | [Mass-density positivity](#mass-density) | Analogy | background |
| 178 | 0.212 | [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) | Analogy | background |
| 179 | 0.212 | [Klein–Gordon indefinite charge](#klein-gordon-charge) | Analogy | background |
| 180 | 0.212 | [Anomalous dispersion](#anomalous-dispersion) | Analogy | background |
| 181 | 0.181 | [Lamb cutoff](#lamb-cutoff) | Analogy | background |
| 182 | 0.181 | [Two different χ’s: Euler characteristic vs class-group character](#two-chis) | Analogy | background |
| 183 | 0.165 | [Standard conjectures (Hodge type)](#standard-conj) | Open | true but ghost-blind/untested |

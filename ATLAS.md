# The RH Atlas — full public edition

Version 1.6 · 29 Oct 2026 · J. W. McGreevy; formalization by Grok Bot

> **The Riemann Hypothesis is NOT proved here.** This atlas is a classification of known structures, criteria and open problems, not a proof.

346 concepts · 989 typed relations · 10 missing pieces. Generated from `atlas.json` by `build_public_md.py`.

**Order.** Every section lists its entries in descending priority. Headers read `#rank · priority · name`. Priority comes from the Heuristic scoring layer described in [scores.md](scores.md): priority = 0.6 · (gap significance × √(sensitivity · specificity)) + 0.4 · tractability. The scores are judgment calls, shown component by component so any reader can disagree with them.

**Organizing split.** Phase/unitarity structure (functional equations, |φ| = 1, cocycles, Hecke operators, cusp positivity) is *ghost-blind*: it holds equally for functions with zeros off the critical line, such as the Davenport–Heilbronn function. The *sign* of a spectral weight is *ghost-sensitive*, and for ζ that sign is RH.

**Labels.** Theorem · Restatement (equivalent to RH or to a known result) · Analogy · Conjecture · Open · Numerical · Heuristic · Cited (taken from the literature). References of the form “TAA Lemma N” point to the lemma series of the Thermodynamics of Arithmetic Action programme (see README.md for the published volumes). Citations marked “to verify” have not yet been checked against the source.

## Contents

- [Missing pieces](#missing-pieces)
- [Diagnostic quadrants](#diagnostic-quadrants)
- [Concepts by primary axis](#concepts-by-primary-axis)
  - [open target](#axis-open-target) (15)
  - [no-go / refuted](#axis-no-go-refuted) (10)
  - [sign/positivity (Ax2)](#axis-sign-positivity-ax2) (53)
  - [reference/pole/cusp](#axis-reference-pole-cusp) (24)
  - [geometry over F_q](#axis-geometry-over-f-q) (24)
  - [Spec ℤ gap](#axis-spec-gap) (26)
  - [physics analogue](#axis-physics-analogue) (37)
  - [restatement ⇔ RH](#axis-restatement-rh) (10)
  - [numerics/certificate](#axis-numerics-certificate) (43)
  - [ghost-sensitive](#axis-ghost-sensitive) (13)
  - [structure/frame (Ax1)](#axis-structure-frame-ax1) (43)
  - [phase/unitarity (Ax3)](#axis-phase-unitarity-ax3) (33)
  - [ghost-blind](#axis-ghost-blind) (5)
- [Index by rank](#index-by-rank)

## Missing pieces

These are the objects that, as far as this atlas can tell, would have to exist for a positivity proof of RH along the lines of the function-field case. Each is labelled Open. Listed in priority order.

### #13 · 0.700 · Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name) <a id="mp-flow-h1"></a>

**Label:** Open · **id:** `mp_flow_h1` · **quadrant:** RH-sharp

*In plain words:* For ℚ both cohomologies we can compute vanish (étale H¹ = 0, Arakelov Pic⁰ = a point), yet ψ(x) − x ≠ 0. The zeros need a cohomology relative to the scaling flow.

**Core.** Construct the middle term of Tate's split at |x| = 1 as an H¹ for Spec ℤ carrying (a) a Frobenius-type flow whose spectrum is the zeros (MP1–MP2; needs the Euler product, absent for DH) and (b) a cup product H¹ × H¹ → H² ≅ ℝ(−1) (MP3; absent for DH), and prove the cup square definite on the primitive part (MP4 = Hodge index/Rosati sign; the only positivity input). MP0: H⁰/H² = Tate boundary terms f(0), f̂(0) (DH: none). Deninger's axioms, TAA refinements MP0/MP4 (TAA Lemma 151 Conj 4.1). TAA Lemma 153: Connes's cokernel (TAA Lemma 153, correction 18) — its Hilbert space is automatically positive and sees only critical zeros; RH ⇔ nothing missing ⇔ global trace formula. Recorded as a precision of MP4, no new missing piece (MPU153). TAA Lemma 157 sharpening of MP4: Deninger's conjectured cohomology carries a positive g = tr(· ∪ ∗·) with ∗ commuting with Θ, i.e. the Poincaré dual of the flow equals its Hilbert adjoint (Θ^∨ = Θ†); equivalently the arithmetic J (from the Euler product) makes the flow a rotation. Den98 §3 p.169 (opened) gives ⇒ RH. TAA Lemma 158: degree-1 form of MP4 for surface leaves: positivity tr(h∪∗h) is automatic (Den05 (15)); ∗ = −J on H̄¹; MP4 ⇔ the flow preserves a leafwise Hodge splitting ([J,Θ] = 0), cf. Deninger–Singhof Prop 4.6. Missing Piece v5 (headline adopted by J. W. McGreevy): MP4 is headed by the one-line Conjecture "the Euler product induces the Hodge splitting of the square, with its sign" (entry: Euler product induces the Hodge splitting), with the v4 sharp form underneath: a complex structure J on H¹ with (1) [J,Θ] = 0, (2) g = ω(·,J·) positive definite on the primitive part (a Θ-invariant fundamental decomposition of the Krein form; σ: ρ ↦ 1 − ρ̄ fixes every eigenvalue), (3) the positivity derived, not verified, from a structural input built from the whole Euler product that is prime-crossing and uses all primes in each window at once (R8′). Requirements R1–R8′ unchanged; no-go list 32 items. Headline reworded geometrically: "the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign".

**Formula.** N_n − (1 + qⁿ) = −Tr(Fⁿ | H¹) ↔ ψ(x) − x = −Σ_ρ x^ρ/ρ + …

**What is proved around it.** π₁ét(Spec ℤ) = 1 ⇒ H¹ét = 0 (TAA Lemma 140); curve row: N_n − (qⁿ + 1) = −Tr(Fⁿ | H¹) with relative Gram NSD (TAA Lemma 141 §1); Tr ↔ −(ψ − x) up to the s = 0 term and ARCH (TAA Lemma 142 corrections).

**Tests it must pass.** Must carry a positive structure (Ax2), not only the trace formula: the explicit formula alone is ghost-blind in data (TAA Lemma 143: ghost defect ≤ 1.9e−5, 0.08× noise).

**Also known as:** H¹_flow; Deninger H¹

**Axes:** missing piece, Spec ℤ gap, reference/pole/cusp

**TAA lemmas:** 140, 141, 142, 151, 153, 157, 158

**Scores (Heuristic):** gap significance 1.0 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.5 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [No étale H¹ for Spec ℤ](#no-etale-h1)
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x)
- same mechanism as → [Deninger’s foliated program](#deninger)
- same mechanism as → [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) — subsumed as MP4 (TAA Lemma 151)
- same mechanism as → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) — sign half = MP4 (TAA Lemma 151)
- same mechanism as → [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) — contained as a test (TAA Lemma 151)
- same mechanism as → [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) — headline of MP4 (Missing Piece v5)

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (lives in); [Connes trace formula](#connes-trace) (same mechanism as); [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (lives in); [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) (lives in); [Deninger’s foliated program](#deninger) (same mechanism as); [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (analogue of); [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) (lives in); [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) (same mechanism as); [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (special case of); [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (constrains); [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) (lives in); [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (lives in); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (same mechanism as); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (lives in)

### #14 · 0.700 · Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²) <a id="mp-castelnuovo"></a>

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

**Relations (incoming):** [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (lives in); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) (special case of); [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (constrains)

### #15 · 0.700 · Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0) <a id="mp-h1-square"></a>

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

**Relations (incoming):** [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) (same mechanism as)

### #16 · 0.700 · Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ <a id="mp-ns-psi"></a>

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

### #17 · 0.700 · Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8) <a id="mp-d8"></a>

**Label:** Open · **id:** `mp_d8` · **quadrant:** RH-sharp

*In plain words:* The top substantive direction: a surface S over Spec ℤ with an ample class and a Riemann–Roch whose χ(nD) is quadratic, so that Hodge index follows as it does for curves.

**Core.** D8: surface + ample + RR for Spec ℤ — find S with χ(nD) quadratic and a Hodge index; obstacle: the collapse ℤ ⊗ ℤ = ℤ; sign = Weil form (TAA Lemma 140, TAA Lemma 141). Acceptance test (TAA Lemma 141): reconstruct the relative space and its form from independent constraints — (a) the hyperbolic plane U = ⟨𝟙, 𝕃⟩, (b) the scaling flow acting on it as diag(1, eᵗ), (c) ampleness at ∞, (d) RR/GRR with quadratic growth — then prove negativity on U^⊥. Any proof that uses the zeros, or defines the form by its negativity, fails. TAA Lemma 152: phrased as a 'degree' — a count (≥ 0) on arithmetic correspondences whose polarization is Weil's form; in Cayley–Klein terms the absolute of the arithmetic pairing must be imaginary (= MP4). TAA Lemma 158: the collapse as an object: requirements R1–R5 on a defect invariant (missing_square_spec_z); collapse alone is ghost-blind.

**What is proved around it.** Over F_q: surface + ample + RR ⇒ Hodge index (Segre 1937, Grothendieck 1958) (TAA Lemma 140). Spec ℤ ×_ℤ Spec ℤ = Spec ℤ (TAA Lemma 65). Arithmetic surfaces (curve × Spec O_K) satisfy V1–V3, but the relative part is Néron–Tate, not ζ (TAA Lemma 145).

**Tests it must pass.** Must pass the tautology test (no zeros, no definition by negativity, TAA Lemma 141) and the must-fail-for-DH test (TAA Lemma 147).

**Also known as:** D8; arithmetic surface with Hodge index

**Axes:** missing piece, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 65, 140, 141, 145, 147, 152, 158

**Scores (Heuristic):** gap significance 1.0 (nearest gap: surface + ample class + Riemann–Roch for Spec ℤ (D8)) · sensitivity 1.0 · specificity 1.0 · tractability 0.25 · evidence 0.4 → priority 0.700

**Relations (outgoing):**

- same mechanism as → [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr)
- same mechanism as → [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr)
- special case of → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo)

**Relations (incoming):** [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) (same mechanism as); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (same mechanism as)

### #18 · 0.700 · Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3) <a id="mp-brst"></a>

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

**Relations (incoming):** [Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24](#central-term-24-algebra-conjecture) (refines)

### #19 · 0.700 · Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin) <a id="mp-passivity-margin"></a>

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

**Relations (incoming):** [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) (analogue of)

### #20 · 0.700 · Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square <a id="mp-quadratic-rr"></a>

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

### #21 · 0.700 · Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”) <a id="mp-rg5"></a>

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

**Relations (incoming):** [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (same mechanism as)

### #22 · 0.700 · Missing: an inequality consequence of automorphy (SC-E / HS-1) <a id="mp-automorphy-ineq"></a>

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

## Diagnostic quadrants

Sensitivity asks whether a statement holds for ζ (is necessary for, or implied by, RH). Specificity asks whether it fails for the fakes (the Davenport–Heilbronn function and the ghost zero models). A concept can only detect RH if it scores high on both.

| | specificity ≥ 0.8 (fails for the fakes) | specificity < 0.8 (ghost-blind or untested) |
|---|---|---|
| **sensitivity ≥ 0.8** (true for ζ) | RH-sharp: 125 | true but ghost-blind/untested: 177 |
| **sensitivity < 0.8** (interpretive) | sharp but interpretive: 11 | background: 33 |

### RH-sharp: true for ζ and fails for the fakes (125)

- #1 · 0.200 · [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) [Open]
- #2 · 0.720 · [Davenport–Heilbronn function](#davenport-heilbronn) [Theorem]
- #3 · 0.720 · [Weil positivity criterion](#weil-positivity) [Cited]
- #4 · 0.720 · [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) [Cited]
- #5 · 0.720 · [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) [Theorem]
- #6 · 0.720 · [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) [Theorem]
- #7 · 0.720 · [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) [Theorem]
- #8 · 0.720 · [Lagarias/Hinkkanen criterion](#lagarias) [Cited]
- #9 · 0.720 · [Connes trace formula](#connes-trace) [Cited]
- #10 · 0.720 · [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) [Theorem]
- #11 · 0.720 · [Primitive part V₀ = U^⊥](#primitive-part) [Theorem]
- #12 · 0.720 · [Definite cup square / Krein one-liner](#definite-cup-square) [Theorem]
- #13 · 0.700 · [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) [Open]
- #14 · 0.700 · [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) [Open]
- #15 · 0.700 · [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) [Open]
- #16 · 0.700 · [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) [Open]
- #17 · 0.700 · [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) [Open]
- #18 · 0.700 · [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) [Open]
- #19 · 0.700 · [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) [Open]
- #20 · 0.700 · [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) [Open]
- #21 · 0.700 · [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) [Open]
- #22 · 0.700 · [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) [Open]
- #23 · 0.600 · [Passivity (positive real part)](#passivity) [Restatement]
- #24 · 0.600 · [Relative Gram matrix G_rel](#relative-gram) [Restatement]
- #25 · 0.600 · [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) [Restatement]
- #26 · 0.600 · [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) [Restatement]
- #27 · 0.600 · [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) [Restatement]
- #28 · 0.600 · [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) [Restatement]
- #29 · 0.580 · [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) [Numerical]
- #30 · 0.580 · [DH prime-side Gram test](#dh-prime-side-gram) [Numerical]
- #31 · 0.580 · [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) [Numerical]
- #32 · 0.580 · [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime) [Numerical]
- #33 · 0.580 · [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) [Numerical]
- #34 · 0.580 · [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) [Numerical]
- #35 · 0.580 · [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix) [Numerical]
- #36 · 0.580 · [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) [Numerical]
- #37 · 0.580 · [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) [Numerical]
- #38 · 0.580 · [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) [Numerical]
- #50 · 0.560 · [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) [Conjecture]
- #51 · 0.560 · [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) [Open]
- #52 · 0.540 · [Rosati positivity](#rosati) [Theorem]
- #53 · 0.540 · [Krein collisions (how ghosts are born)](#krein-collision) [Theorem]
- #54 · 0.540 · [Castelnuovo–Severi inequality](#castelnuovo-severi) [Theorem]
- #55 · 0.540 · [de Bruijn–Newman constant Λ](#debruijn-newman) [Cited]
- #56 · 0.540 · [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) [Theorem]
- #57 · 0.540 · [Epstein zeta no-go](#epstein) [Theorem]
- #58 · 0.540 · [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) [Theorem]
- #59 · 0.540 · [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) [Theorem]
- #60 · 0.540 · [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) [Theorem]
- #61 · 0.540 · [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) [Theorem]
- #62 · 0.540 · [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) [Theorem]
- #63 · 0.540 · [Compatible complex structure J commuting with Frobenius](#compatible-j) [Theorem]
- #64 · 0.540 · [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) [Theorem]
- #65 · 0.540 · [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) [Theorem]
- #66 · 0.540 · [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) [Theorem]
- #67 · 0.540 · [RH for curves over F_q (Weil)](#fq-curves) [Cited]
- #68 · 0.540 · [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) [Theorem]
- #69 · 0.540 · [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) [Theorem]
- #70 · 0.540 · [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) [Theorem]
- #71 · 0.540 · [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold) [Theorem]
- #72 · 0.540 · [Decay rate ¼](#decay-quarter) [Theorem]
- #73 · 0.540 · [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) [Theorem]
- #74 · 0.540 · [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) [Theorem]
- #75 · 0.540 · [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) [Cited]
- #76 · 0.540 · [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) [Theorem]
- #77 · 0.540 · [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity) [Theorem]
- #78 · 0.540 · [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) [Theorem]
- #79 · 0.540 · [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) [Theorem]
- #80 · 0.540 · [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh) [Cited]
- #81 · 0.540 · [Li criterion](#li-criterion) [Cited]
- #82 · 0.540 · [Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q](#burgers-local-toeplitz) [Theorem]
- #83 · 0.540 · [de Branges spaces](#de-branges) [Cited]
- #84 · 0.540 · [Hasse bound as a positive degree form](#hasse-pythagoras) [Theorem]
- #85 · 0.540 · [Suzuki’s de Branges line from the prime side](#suzuki-line) [Cited]
- #86 · 0.540 · [Bagchi recurrence](#bagchi) [Cited]
- #87 · 0.540 · [Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k)](#coupled-coil-hasse) [Theorem]
- #117 · 0.420 · [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) [Restatement]
- #118 · 0.420 · [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) [Restatement]
- #119 · 0.420 · [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece) [Restatement]
- #120 · 0.420 · [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) [Restatement]
- #121 · 0.420 · [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) [Restatement]
- #122 · 0.420 · [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) [Restatement]
- #123 · 0.420 · [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) [Restatement]
- #124 · 0.420 · [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin) [Restatement]
- #125 · 0.420 · [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) [Restatement]
- #126 · 0.420 · [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts) [Restatement]
- #127 · 0.420 · [Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing](#passive-network-positive-real) [Restatement]
- #128 · 0.420 · [Two-point form g + iω ≥ 0](#two-point) [Restatement]
- #134 · 0.400 · [One Perron mode against the pole](#pole-perron-one-mode) [Numerical]
- #135 · 0.400 · [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) [Numerical]
- #136 · 0.400 · [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) [Numerical]
- #137 · 0.400 · [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix) [Numerical]
- #138 · 0.400 · [Davenport-Heilbronn window jumps](#davenport-heilbronn-window-jumps) [Numerical]
- #139 · 0.400 · [Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t))](#dilution-law-dh-to-product) [Numerical]
- #140 · 0.400 · [Which channel detects a fake depends on the span](#channel-depends-on-span) [Numerical]
- #141 · 0.400 · [Certified window for one off-line pair](#explicit-ghost-window) [Numerical]
- #142 · 0.400 · [Which channel an off-line zero breaks first over the rationals](#ghost-channel-order-over-q) [Numerical]
- #143 · 0.400 · [Crossing scale of a ghost](#ghost-crossing-scale) [Numerical]
- #144 · 0.400 · [Duursma zeta functions of codes as a finite RH laboratory: Golay satisfies RH; the [32,16,4] code G₂₄ ⊕ e₈ fails](#duursma-code-toy) [Numerical]
- #145 · 0.400 · [The Laguerre inequality Ξ′² − ΞΞ″ > 0 holds for ζ on [0,60] and fails exactly around the off-line zero of the Davenport–Heilbronn function](#laguerre-detects-offline-zero) [Numerical]
- #151 · 0.380 · [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece) [Conjecture]
- #152 · 0.380 · [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open) [Open]
- #169 · 0.360 · [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) [Theorem]
- #170 · 0.360 · [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant) [Cited]
- #171 · 0.360 · [Ghost count of the arithmetic side](#ghost-count-theorem) [Theorem]
- #172 · 0.360 · [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) [Theorem]
- #173 · 0.360 · [Two partners of a zero (duality vs conjugation)](#two-partners) [Theorem]
- #174 · 0.360 · [Frobenius-graph Toeplitz form and its pole/count split](#frobenius-graph-toeplitz-split) [Theorem]
- #175 · 0.360 · [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) [Theorem]
- #176 · 0.360 · [Castelnuovo-Severi and Weil's bound](#castelnuovo-severi-lemma) [Cited]
- #177 · 0.360 · [Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology)](#deninger-derivation-positivity) [Cited]
- #178 · 0.360 · [d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1)](#dolbeault-kahler-sign) [Theorem]
- #179 · 0.360 · [Castelnuovo-Severi defect as a Toeplitz block](#fq-cs-block-identity) [Theorem]
- #180 · 0.360 · [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) [Theorem]
- #181 · 0.360 · [Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians)](#shear-push-density) [Theorem]
- #182 · 0.360 · [Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear](#trace-shear-budget) [Theorem]
- #315 · 0.240 · [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton) [Restatement]
- #316 · 0.240 · [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation) [Restatement]
- #317 · 0.240 · [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece) [Restatement]
- #318 · 0.240 · [RH as a negative-square count (restatement)](#ghost-count-rh-restatement) [Restatement]
- #319 · 0.240 · [Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel](#anisotropic-part-weil) [Restatement]
- #320 · 0.240 · [Hodge index in push/shear language: D² = (D·ω)²/ω² + D°², Hodge index ⇔ D°² ≤ 0 (shear can only subtract); D°² = D₀² − ½(D·h − D·v)²](#hodge-index-shear-subtracts) [Restatement]
- #321 · 0.240 · [Invariant maximal non-positive subspaces: exactly two](#pontryagin-exactly-two) [Restatement]
- #322 · 0.240 · [Riemann-Roch sorts the two conditions](#riemann-roch-sorting) [Restatement]
- #323 · 0.240 · [⟨g|h⟩_W=Σ_ρ ĝ(ρ)conj ĥ(1−ρ̄); Hermitian and scaling-isometric unconditionally; RH ⇔ positive semidefinite](#weil-braket-pairing) [Restatement]

### True for ζ but ghost-blind or untested against the fakes (177)

- #39 · 0.579 · [Deninger’s foliated program](#deninger) [Cited]
- #40 · 0.579 · [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) [Theorem]
- #41 · 0.579 · [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) [Theorem]
- #42 · 0.579 · [Ax1–Ax3 axioms (Yoneda specification)](#ax123) [Theorem]
- #43 · 0.579 · [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) [Cited]
- #44 · 0.579 · [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) [Theorem]
- #46 · 0.579 · [Parity argument: linear χ cannot see D²](#parity-linear-chi) [Theorem]
- #47 · 0.579 · [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) [Cited]
- #48 · 0.579 · [Tautology boundary (zero side vs prime side)](#tautology-boundary) [Theorem]
- #49 · 0.579 · [No étale H¹ for Spec ℤ](#no-etale-h1) [Theorem]
- #89 · 0.492 · [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) [Numerical]
- #90 · 0.492 · [The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation](#single-box-axis-criterion) [Numerical]
- #91 · 0.492 · [Integer dimension over 𝕊 (minimal generators)](#dim-s) [Numerical]
- #92 · 0.452 · [Hodge index theorem](#hodge-index) [Theorem]
- #93 · 0.452 · [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) [Cited]
- #94 · 0.452 · [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) [Theorem]
- #95 · 0.452 · [Lax–Phillips scattering](#lax-phillips) [Cited]
- #96 · 0.452 · [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) [Theorem]
- #97 · 0.452 · [Hodge–Riemann bilinear relations](#hodge-riemann) [Theorem]
- #98 · 0.452 · [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) [Theorem]
- #99 · 0.452 · [Connes–Consani sites](#connes-consani) [Cited]
- #100 · 0.452 · [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) [Theorem]
- #101 · 0.452 · [Pole plane / Tate poles at s = 0, 1](#pole-plane) [Theorem]
- #102 · 0.452 · [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric) [Theorem]
- #103 · 0.452 · [Cartan involution / compact unitary group](#cartan-involution) [Theorem]
- #104 · 0.452 · [On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example)](#conformal-flow-needs-solenoid) [Theorem]
- #105 · 0.452 · [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) [Cited]
- #106 · 0.452 · [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) [Cited]
- #107 · 0.452 · [Maxwell construction / convex effective potential](#maxwell-effective-potential) [Theorem]
- #108 · 0.452 · [Products grow linearly (2n), not quadratically](#products-linear) [Theorem]
- #109 · 0.452 · [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) [Cited]
- #110 · 0.452 · [Yoneda specification](#yoneda) [Theorem]
- #129 · 0.419 · [Riemann hypothesis (target node)](#rh) [Open]
- #130 · 0.419 · [Hilbert–Pólya](#hilbert-polya) [Open]
- #131 · 0.419 · [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) [Open]
- #132 · 0.419 · [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) [Open]
- #133 · 0.419 · [Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24](#central-term-24-algebra-conjecture) [Conjecture]
- #150 · 0.387 · [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) [Numerical]
- #157 · 0.365 · [Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector](#dedekind-qi-one-mode) [Numerical]
- #158 · 0.365 · [Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻](#talenti-template-test) [Numerical]
- #159 · 0.365 · [No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes](#ferromagnetic-sign-not-count) [Numerical]
- #160 · 0.365 · [The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions](#prime-weight-anisotropy) [Numerical]
- #161 · 0.365 · [Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder](#structured-gram-factor-search) [Numerical]
- #162 · 0.365 · [How much the primes fill the archimedean deficit of the Weil form, by support](#archimedean-rectifier-fill) [Numerical]
- #163 · 0.365 · [Cutoff saturation (class-number x is not the lever)](#cutoff-saturation) [Numerical]
- #164 · 0.365 · [Genus seen at resolution sigma](#genus-at-resolution) [Numerical]
- #165 · 0.365 · [LMFDB level-1 Maass list complete to T = 100](#lmfdb-maass-complete) [Numerical]
- #166 · 0.365 · [Null-calibrated GLS matched filter](#null-calibrated-gls) [Numerical]
- #167 · 0.365 · [Ghost onset depends on kernel width](#onset-kernel-dependence) [Numerical]
- #168 · 0.365 · [Model kernel e^{−bu²−u⁶}: first zero collision at b_c ≈ 3.1955](#sextic-kernel-collision) [Numerical]
- #183 · 0.347 · [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) [Theorem]
- #184 · 0.347 · [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) [Cited]
- #185 · 0.347 · [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) [Cited]
- #186 · 0.347 · [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) [Theorem]
- #187 · 0.347 · [Automorphy defect (TAA Lemma 144)](#automorphy-defect) [Theorem]
- #188 · 0.347 · [Certified positivity windows](#certified-windows) [Numerical]
- #189 · 0.347 · [Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x](#beurling-counting-test-bstar) [Numerical]
- #190 · 0.325 · [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) [Theorem]
- #191 · 0.325 · [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) [Theorem]
- #192 · 0.325 · [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) [Theorem]
- #193 · 0.325 · [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) [Cited]
- #194 · 0.325 · [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) [Theorem]
- #195 · 0.325 · [√2 family](#sqrt2-family) [Theorem]
- #196 · 0.325 · [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) [Theorem]
- #197 · 0.325 · [Cusp ≠ archimedean place](#cusp-vs-infinity) [Theorem]
- #198 · 0.325 · [F₁ base](#f1-base) [Cited]
- #199 · 0.325 · [Null-line quotient (Gupta-Bleuler form)](#null-line-quotient) [Theorem]
- #200 · 0.325 · [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) [Theorem]
- #201 · 0.325 · [Arakelov geometry](#arakelov) [Cited]
- #202 · 0.325 · [Closed geodesics on the modular surface](#closed-geodesics) [Theorem]
- #203 · 0.325 · [Density / volume reading](#density-volume) [Theorem]
- #204 · 0.325 · [Multi-channel first-order factors are bounded by the SOS fit](#gram-factor-channel-bound) [Theorem]
- #205 · 0.325 · [Principalization](#principalization) [Theorem]
- #206 · 0.325 · [Selberg resonances](#selberg-resonances) [Theorem]
- #207 · 0.325 · [Spec ℤ is terminal](#spec-z-terminal) [Theorem]
- #208 · 0.325 · [Spinor/Clifford route](#spinor-route) [Theorem]
- #209 · 0.325 · [Weil Rosetta stone](#weil-rosetta) [Cited]
- #210 · 0.325 · [Local-to-global failure](#local-global) [Theorem]
- #211 · 0.325 · [Cohesion (arena)](#cohesion) [Theorem]
- #216 · 0.307 · [Metaplectic / Kubota cocycle](#metaplectic) [Theorem]
- #217 · 0.307 · [Half Tate twist ℚ(½)](#half-tate-twist) [Theorem]
- #218 · 0.307 · [Bost–Connes KMS states](#kms-bost-connes) [Cited]
- #219 · 0.307 · [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) [Theorem]
- #220 · 0.307 · [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) [Theorem]
- #221 · 0.307 · [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) [Theorem]
- #222 · 0.307 · [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) [Theorem]
- #223 · 0.307 · [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) [Theorem]
- #224 · 0.307 · [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) [Theorem]
- #225 · 0.307 · [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) [Cited]
- #226 · 0.307 · [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) [Theorem]
- #227 · 0.307 · [Cup product / Poincaré duality pairing](#cup-product) [Theorem]
- #228 · 0.307 · [Hecke operators](#hecke) [Theorem]
- #229 · 0.307 · [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) [Theorem]
- #230 · 0.307 · [Archimedean place and Γ_ℝ factor](#archimedean-place) [Theorem]
- #231 · 0.307 · [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) [Theorem]
- #232 · 0.307 · [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) [Cited]
- #233 · 0.307 · [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) [Cited]
- #234 · 0.307 · [Cusp forms & Petersson positivity](#cusp-forms-petersson) [Theorem]
- #235 · 0.307 · [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) [Cited]
- #236 · 0.307 · [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) [Cited]
- #237 · 0.307 · [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) [Theorem]
- #238 · 0.307 · [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) [Cited]
- #239 · 0.307 · [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) [Theorem]
- #240 · 0.307 · [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) [Theorem]
- #241 · 0.307 · [Tate count / Picard number (ghost-blind)](#tate-count) [Theorem]
- #242 · 0.307 · [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) [Cited]
- #243 · 0.307 · [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) [Theorem]
- #244 · 0.307 · [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) [Theorem]
- #245 · 0.307 · [λ₂ is monotone under nested windows (Cauchy interlacing)](#lambda2-monotone-nested-windows) [Theorem]
- #246 · 0.307 · [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) [Numerical]
- #247 · 0.307 · [Archimedean thresholds a*](#arch-threshold) [Numerical]
- #248 · 0.307 · [Maass–Selberg relations](#maass-selberg) [Numerical]
- #249 · 0.307 · [Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity](#arithmetic-topology-linking-matrix) [Numerical]
- #250 · 0.307 · [Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z²](#slack-ledger-cf) [Numerical]
- #251 · 0.307 · [Monotone quantities along the de Bruijn–Newman flow: kernel-side entropies are smooth through t = 0; zero-side energy relaxes](#dbn-monotone-functionals) [Numerical]
- #252 · 0.292 · [Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow](#hopf-fibration-spec-z) [Conjecture]
- #253 · 0.292 · [Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy](#perelman-template-dbn) [Open]
- #257 · 0.267 · [Half-density normalization |x|^{½}](#half-density) [Theorem]
- #258 · 0.267 · [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) [Theorem]
- #259 · 0.267 · [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) [Theorem]
- #260 · 0.267 · [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) [Theorem]
- #261 · 0.267 · [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) [Theorem]
- #262 · 0.267 · [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) [Cited]
- #263 · 0.267 · [The prime 2 as the wild place](#prime-two-wild) [Theorem]
- #264 · 0.267 · [Scattering unitarity |φ| = 1](#scattering-phi) [Theorem]
- #265 · 0.267 · [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep) [Theorem]
- #266 · 0.267 · [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) [Theorem]
- #267 · 0.267 · [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) [Theorem]
- #268 · 0.267 · [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) [Theorem]
- #269 · 0.267 · [Yoshida window positivity](#yoshida) [Cited]
- #270 · 0.267 · [Counts vs quadratic positivity](#count-positivity) [Theorem]
- #271 · 0.267 · [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero) [Theorem]
- #272 · 0.267 · [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift) [Theorem]
- #273 · 0.267 · [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) [Theorem]
- #274 · 0.267 · [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings) [Theorem]
- #275 · 0.267 · [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance) [Theorem]
- #276 · 0.267 · [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4) [Theorem]
- #277 · 0.267 · [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality) [Theorem]
- #278 · 0.267 · [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp) [Theorem]
- #279 · 0.267 · [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term) [Theorem]
- #280 · 0.267 · [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) [Theorem]
- #281 · 0.267 · [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge) [Cited]
- #282 · 0.267 · [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids) [Theorem]
- #283 · 0.267 · [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities) [Theorem]
- #284 · 0.267 · [Weight ladder (modular weights)](#weight-ladder) [Theorem]
- #285 · 0.267 · [CM case: the Hasse triangle is Fermat's two-squares triangle](#cm-gaussian-hasse-triangle) [Theorem]
- #286 · 0.267 · [Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward](#dbn-bohlin-decay) [Theorem]
- #287 · 0.267 · [η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential](#eta-chain) [Theorem]
- #288 · 0.267 · [(τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²](#exactness-monge-ampere) [Theorem]
- #289 · 0.267 · [The critical-line wave: Hardy Z and the Riemann–Siegel phase](#hardy-z-critical-line-wave) [Theorem]
- #290 · 0.267 · [E₂* as the derivative of the Kronecker limit (cusp-scattering footprint)](#kronecker-limit-e2star) [Theorem]
- #291 · 0.267 · [Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)](#local-dbn-slack) [Theorem]
- #292 · 0.267 · [w₂ / Čech class (TAA Lemma 138)](#w2-cech) [Theorem]
- #293 · 0.267 · [W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ](#archimedean-weyl-kernel) [Theorem]
- #294 · 0.267 · [Beta integral, Maslov dequantization and entropy](#beta-dequantization-entropy) [Theorem]
- #295 · 0.267 · [The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄)](#chi-minus-one-half-pole) [Theorem]
- #296 · 0.267 · [On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH](#chirality-star-gamma5-hodge-index) [Theorem]
- #297 · 0.267 · [Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1)](#hecke-toy-contraction) [Theorem]
- #298 · 0.267 · [One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction](#prime-clocks) [Theorem]
- #299 · 0.267 · [Sector map w = e^{iπs/2}](#sector-map-w) [Theorem]
- #300 · 0.267 · [Elliptic/parabolic/hyperbolic as |tr M| = 2r < = > 2 for normalised Frobenius; only SO(2) compact; in RP² the parabola is tangent to the line at infinity (zero-margin edge as tangency); r = 1 forces scalar Frobenius for elliptic curves](#conic-compactness) [Theorem]
- #301 · 0.267 · [Saddles of Euler products: curvature is additive and the cross-prime term at a saddle is always non-positive](#euler-product-saddle-additivity) [Theorem]
- #302 · 0.267 · [The factorial of one half and the Fourier quarter-turn](#fourier-quarter-turn) [Theorem]
- #303 · 0.267 · [Fourth roots: a_p = 0 (supersingular) gives r = 0 over 𝔽_p and the cusp r = 1 over 𝔽_{p²} (a_{p²} = −2p)](#fourth-roots-supersingular) [Theorem]
- #304 · 0.267 · [Kepler: LRL vector closes so(4) = su(2) ⊕ su(2) for E < 0, so(3,1) for E > 0, e(3) at E = 0](#kepler-so4-contraction) [Theorem]
- #305 · 0.267 · [Φ is not in Newman's class 𝒫 (unconditional), so b₀ < ∞; the Lee–Yang property of Φ is RH](#newman-class-p-fails-for-phi) [Cited]
- #306 · 0.267 · [Platonic-point deficits 2π(1 − 1/k) are orbifold cone deficits of S²/G, not Descartes vertex defects; orbifold Gauss–Bonnet: cone deficits + area = 720° (icosahedral 708° + 12°, χ_orb = 1/30)](#orbifold-vs-descartes-deficits) [Theorem]
- #307 · 0.267 · [Ruled quadric through a saddle: null lines, signature (1,1)](#ruled-quadric-null-lines) [Theorem]
- #308 · 0.267 · [so(4)=su(2)⊕su(2): Λ± are commuting rotation subalgebras; D·D=‖D⁺‖²−‖D⁻‖²](#so4-chirality-split) [Theorem]
- #309 · 0.267 · [Spin structure & theta characteristic](#spin-theta) [Theorem]
- #310 · 0.267 · [Three lenses on one Euler factor (analytic factor, det(1 − Frob X), oscillator 2cos(z log p)) carry the same dBN flow; they separate only for products](#three-lenses-one-flow) [Theorem]
- #311 · 0.267 · [Forced functionals of the finite dBN zero gas: dL/dt = 2E, dE/dt ≤ 0; W = L − (n(n−1)/4) log S₂ nondecreasing, constant on Hermite configurations; Y = ΣIm² nonincreasing; de Bruijn envelope y_max(t)² ≤ max(y₀² − 2(t − t₀), 0)](#zero-gas-forced-functionals) [Theorem]
- #338 · 0.187 · [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) [Open]
- #343 · 0.165 · [Candidate formulations of Castelnuovo-Severi over the integers](#cs-for-spec-z-formulations) [Open]
- #344 · 0.165 · [Standard conjectures (Hodge type)](#standard-conj) [Open]
- #345 · 0.165 · [Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance](#thermodynamic-j-direction) [Open]
- #346 · 0.165 · [One operator that is a sum of squares (net ≥ 0 as an identity) and generates dBN (∂_tH = +Δ_z H, backward heat on the real line); stronger than Hilbert–Pólya](#both-at-once) [Open]

### Separates ζ from the fakes, but the claim itself is interpretive (Analogy/Heuristic) (11)

- #45 · 0.579 · [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) [Theorem]
- #88 · 0.532 · [Gain lines (active media)](#gain-line) [Analogy]
- #111 · 0.451 · [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) [Heuristic]
- #112 · 0.451 · [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) [Heuristic]
- #113 · 0.451 · [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) [Heuristic]
- #114 · 0.451 · [Must-fail-for-DH acceptance test](#dh-acceptance) [Heuristic]
- #146 · 0.392 · [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) [Analogy]
- #147 · 0.392 · [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) [Analogy]
- #148 · 0.392 · [Time delay (Wigner)](#time-delay) [Analogy]
- #149 · 0.392 · [Källén–Lehmann spectral positivity](#kallen-lehmann) [Analogy]
- #314 · 0.253 · [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) [Analogy]

### Background: interpretive and not separating (33)

- #115 · 0.423 · [BRST / Gupta–Bleuler physical quotient](#brst) [Analogy]
- #116 · 0.423 · [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) [Analogy]
- #153 · 0.377 · [Displaced reference (subtracting the pole)](#displaced-reference) [Heuristic]
- #154 · 0.377 · [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) [Heuristic]
- #155 · 0.377 · [Band criterion γ < 2T_M](#band-criterion) [Heuristic]
- #156 · 0.377 · [Preserved-leaf contribution χ(L)/|e^{κt} − 1| (Álvarez López–Kordyukov–Leichtnam Thm 1.3.10) has the shape of the archimedean term](#deninger-preserved-leaf-term) [Heuristic]
- #212 · 0.324 · [Kramers–Kronig relations](#kramers-kronig) [Analogy]
- #213 · 0.324 · [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy) [Analogy]
- #214 · 0.324 · [Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity)](#ep-gap-across-collision) [Analogy]
- #215 · 0.324 · [Gribov ambiguity](#gribov) [Analogy]
- #254 · 0.271 · [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate) [Heuristic]
- #255 · 0.271 · [The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)](#edge-boundary-cycle) [Heuristic]
- #256 · 0.271 · [RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin](#kahler-package-one-liner) [Heuristic]
- #312 · 0.256 · ["Cocycles give structure, not sign"](#cocycle-principle) [Heuristic]
- #313 · 0.256 · [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) [Heuristic]
- #324 · 0.226 · [Buoyancy / Archimedes principle](#archimedes) [Analogy]
- #325 · 0.226 · [Distortionless line R/L = G/C](#distortionless) [Analogy]
- #326 · 0.226 · [Heaviside RLGC line](#heaviside) [Analogy]
- #327 · 0.226 · [One log-gas and its frozen limit](#log-gas-frozen-limit) [Analogy]
- #328 · 0.226 · [Mass-density positivity](#mass-density) [Analogy]
- #329 · 0.226 · [Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned](#serre-derivative-analogy) [Analogy]
- #330 · 0.226 · [Einstein–Cartan: spin enters as torsion](#einstein-cartan-torsion-spin) [Analogy]
- #331 · 0.226 · [Einstein–de Haas lesson: the molecular-current model gave g ≈ 1, the true carrier was spin (g = 2); the missing piece may be a spin-like degree of freedom, not an orbit](#einstein-de-haas-lesson) [Analogy]
- #332 · 0.226 · [Viscosity multiplies trace-free strain; dissipation 2μ|S°|² ≥ 0 is the analogue of the missing sign; baroclinic wedge ↔ Gram tilt cos θ = r, net = p sin²θ](#viscosity-baroclinic) [Analogy]
- #333 · 0.212 · [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) [Analogy]
- #334 · 0.212 · [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) [Analogy]
- #335 · 0.212 · [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) [Analogy]
- #336 · 0.212 · [Klein–Gordon indefinite charge](#klein-gordon-charge) [Analogy]
- #337 · 0.212 · [Anomalous dispersion](#anomalous-dispersion) [Analogy]
- #339 · 0.181 · [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading) [Analogy]
- #340 · 0.181 · [Lamb cutoff](#lamb-cutoff) [Analogy]
- #341 · 0.181 · [Two different χ’s: Euler characteristic vs class-group character](#two-chis) [Analogy]
- #342 · 0.181 · [Ramanujan's 691 as a degeneration of the pole line](#ramanujan-691-degeneration) [Analogy]

## Concepts by primary axis

Sections are ordered by their highest-ranked entry; entries within each section by descending priority. Missing pieces are listed above and not repeated.

## Axis: open target <a id="axis-open-target"></a>

### #1 · 0.200 · Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement <a id="ferromagnetic-phi-missing-piece"></a>

**Label:** Open · **id:** `ferromagnetic_phi_missing_piece` · **quadrant:** RH-sharp

*In plain words:* Newman's results turn RH into a statement in statistical mechanics: RH holds exactly when the kernel Φ behaves like the spin distribution of a ferromagnet, so that every ferromagnetic system built from copies of it has its field zeros on the imaginary axis. That equivalence is a restatement, not progress. The conjectured missing piece is a mechanism: a ferromagnetic system whose sites are the primes (and the archimedean place) and whose block-spin law is Φ. Such a system would give the Lee–Yang property, and hence RH, as a structural consequence. Two pictures point the same way. Li's criterion moves the zeros onto a unit circle, and RH says exactly that they all lie on it; Lee and Yang proved that ferromagnetic coupling puts zeros on a unit circle. And only the genuine prime angles keep the window form positive, as if the primes were coupled ferromagnetically, while shuffled angles behave like a frustrated spin glass. Both links are analogies, not proofs. The Riemann Hypothesis is not proved.

**Core.** Open. The equivalence RH ⇔ Φ Lee–Yang is a cited Restatement (Newman 1974/1976, Lieb–Sokal 1981); only a ferromagnetic construction from the primes would be new. RH is not proved. A Gram factor of the Weil form always exists under RH and is, up to rotation, indexed by the zeros, so reading couplings off the Weil form is circular; a construction must define J_pq from primes and ∞ and prove J_pq ≥ 0 independently. Link (29 Oct 2026): two unit circles. Li's map w = 1 − 1/ρ sends the critical line to |w| = 1, and under RH λₙ = Σ_ρ 2sin²(nθ_ρ/2) [Theorem]; Lee–Yang: ferromagnetic coupling puts the partition-function zeros on |z| = 1 [Theorem]. The two circles live in different variables (zeros of ξ versus fugacity) and no map between them is known, so the link is an Analogy; Li's λₙ ≥ 0 for all n is itself a restatement of RH. The genuine-versus-shuffled angle result reads as ferromagnetic versus frustrated, spin-glass-like coupling [Analogy]. RH is not proved.

**Formula.** RH ⇔ Φ(u)du has the Lee–Yang property (Newman 1974, as stated by Lieb–Sokal 1981) ⇔ b₀ ≥ 0 (Newman 1976, Λ = −4b₀, since Newman's variable is t = 2u; ∫Φ(u)e^{hu}du = ¼ξ(½+h/2)) ⇔ Λ ≤ 0; with Λ ≥ 0 (Rodgers–Tao) the margin is zero. Refined form: Φ(u)du = lim_N law of (Σ_{i∈B_N} c_{N,i}σ_i), with σ_i = ±1 Ising spins with ferromagnetic couplings J_ij ≥ 0 indexed by primes and ∞

**Numbers.** Φ even to 2.9e−12 and positive on [0,1.5]; Φ(0) = 0.44670 · one-site Lee–Yang to height 100: 29 sign changes of Ξ = N(100) = 29 · Newman class 𝒫 fails unconditionally: V/u⁴ = 253, 160, 247, 584 at u = 0.5, 1, 1.5, 2 (double-exponential decay) · Turán gaps positive for the flowed kernel at every b tested (1 → 3000), so these tests cannot locate b₀ · normalisation check: ∫Φ(u)e^{hu}du = ¼ξ(½+h/2) to relative error ≤ 1.5e−21 at h = 0, 0.6, 0.5+3i, 10i; zeros of ∫Φ(u)e^{izu}du sit at z = 2γ · lattice-factor no-go: if Φ = φ∗ψ with φ a measure on a lattice LZ (L > 0.111, e.g. L = log 2) and ψ̂ entire, then φ̂ has no zeros (finitely supported ⇒ a pure shift; otherwise Euler-factor-like, with poles but no zeros) [Theorem] · mean-field no-go: Φ = e^{λu²}ν with λ > 0 and ν Lee–Yang would give Λ ≤ −λ < 0, contradicting Λ ≥ 0 (Rodgers–Tao); the dBN tilt is exactly a Curie–Weiss self-coupling [Theorem, given de Bruijn and Rodgers–Tao] · one prime as a spin-1 site: 2e^{t log²p}cos(z log p) − a/√p is the transform of a (signed, if a > 0) spin-1 measure; its one-site Lee–Yang threshold is t = Λ_p [Theorem] · excluded ferromagnets: free Euler-factor systems (J = 0 between primes) and finite mean-field couplings; open: pair-dependent couplings J_pq ≥ 0 defined from primes and ∞ alone · Li's criterion: w = 1 − 1/ρ maps the critical line Re s = ½ onto the unit circle |w| = 1; under RH each w_ρ = e^{iθ_ρ} and λₙ = Σ_ρ [1 − (1 − 1/ρ)ⁿ] = Σ_ρ 2sin²(nθ_ρ/2) ≥ 0 (zeros paired with their conjugates) [Theorem; Li 1997, Bombieri–Lagarias 1999] · Lee–Yang circle theorem: ferromagnetic pair couplings (J_ij ≥ 0) put every zero of the Ising partition function in the fugacity z = e^{−2h} on the unit circle |z| = 1 [Theorem; Lee–Yang 1952] · the window angle test read physically: the genuine Frobenius angles of Δ and 11a1 keep window positivity, while permuted, i.i.d. Sato–Tate and adversarial-but-allowed angles break it; read as ferromagnetic (aligned) versus frustrated, spin-glass-like coupling [Analogy; the test itself is Numerical]

**Axes:** open target, physics analogue, sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.5 → priority 0.200

> ⚠ **Correction / caution.** Λ = −4b₀ (not −b₀) in Newman's 1976 normalisation; Ξ-type transform of Φ is ¼ξ(½+iz/2), not ξ(½+iz)

> ⚠ **Correction / caution.** Li's unit circle (w = 1 − 1/ρ) and the Lee–Yang unit circle (fugacity z) are different variables; no map between them is known, so the Li ↔ Lee–Yang link is an Analogy, not a Theorem

**Relations (outgoing):**

- refines → [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh)
- restates → [de Bruijn–Newman constant Λ](#debruijn-newman)
- candidate setting for → [Bost–Connes KMS states](#kms-bost-connes)
- tested by → [Duursma zeta functions of codes as a finite RH laboratory: Golay satisfies RH; the [32,16,4] code G₂₄ ⊕ e₈ fails](#duursma-code-toy)
- related to → [Li criterion](#li-criterion) — Li's w = 1 − 1/ρ puts the zeros on a unit circle under RH, as Lee–Yang does for ferromagnets [each a Theorem; the link is an Analogy]
- analogous to → [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) — genuine versus shuffled angles read as ferromagnetic versus frustrated, spin-glass-like coupling [Analogy]

**Relations (incoming):** [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix) (tests); [Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing](#passive-network-positive-real) (contrasts with); [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece) (analogy of); [Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder](#structured-gram-factor-search) (constrains); [Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow](#hopf-fibration-spec-z) (analogy of); [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge) (analogy of); [Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1)](#hecke-toy-contraction) (obstructs); [Saddles of Euler products: curvature is additive and the cross-prime term at a saddle is always non-positive](#euler-product-saddle-additivity) (constrains); [Φ is not in Newman's class 𝒫 (unconditional), so b₀ < ∞; the Lee–Yang property of Φ is RH](#newman-class-p-fails-for-phi) (constrains); [Einstein–de Haas lesson: the molecular-current model gave g ≈ 1, the true carrier was spin (g = 2); the missing piece may be a spin-like degree of freedom, not an orbit](#einstein-de-haas-lesson) (heuristically points to)

### #50 · 0.560 · MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign <a id="mp4-euler-induces-hodge"></a>

**Label:** Conjecture · **id:** `mp4_euler_induces_hodge` · **quadrant:** RH-sharp

*In plain words:* Unique factorization splits ζ across the primes but carries no sign; on a surface the Hodge index splits the square and supplies the sign. Over finite fields Weil needed both. The conjecture: over the integers the first produces the second.

**Core.** Two splittings. (a) Euler product: a splitting across primes, no sign [Theorem]: −ζ′/ζ supported on prime powers ⇔ Euler product (TAA Lemma 165); for eigenforms one SU(2) class per prime, Flath restricted tensor product; every Dirichlet L has it and GRH for them is open. (b) Hodge index on the square: an ample class splits NS ⊗ ℝ = ℝH ⊕ H^⊥ with H^⊥ negative definite, which on Frobenius graphs is Weil/Castelnuovo positivity. (c) Over F_q both are needed (Riemann–Roch on C×C plus an ample class for the sign; the Frobenius correspondence for the arithmetic); fake polynomials share the counting input and fail the sign (TAA Lemma 137, TAA Lemma 141). Conjecture: in Deninger's conjectured cohomology splitting (a) produces a Θ-invariant splitting of the square whose primitive part is definite, i.e. MP4(1)–(2), with the sign derived (R7) and all primes in each window used at once (R8′). Not the claim (a) = (b): the two tensors (across primes vs L ⊗ R) are distinct and identifying them is an Analogy. Undefined for DH (composite leakage): exclusion, not a sign. Provisional reading of "couple all places" (adopted until a better definition is found): a signed product formula on the square (Open). TAA Lemma 166 (function-field test): counts + FE + positive integer closed-point counts do not induce the sign (675/2935/4961 count-positive off-circle fakes, g = 2, q = 7/11/13); the conjecture survives only in a geometric reading (the Euler product of an object whose square has Hodge index). Headline reworded (approved by J. W. McGreevy after TAA Lemma 166): "the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign". Reason: over F_q, counting data, the functional equation and non-negative closed-point counts do not induce the sign (TAA Lemma 166: 675/2935/4961 count-positive off-circle fakes); the sign comes from the Frobenius correspondence on C×C with an ample class (Hodge index). The v4 sharp form stays underneath. Standard controls for any proposed mechanism: DH and Epstein x² + 5y².

**Formula.** Euler product as Frobenius correspondence on the square (+ ample class) ⟹? Hodge splitting with sign

**Also known as:** MP4(3) one line; lead conjecture v5; two splittings; Euler product induces the Hodge splitting (v5 wording); geometric MP4 headline

**Axes:** open target, sign/positivity (Ax2), Spec ℤ gap, ghost-sensitive

**TAA lemmas:** 166

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.5 → priority 0.560

> ⚠ **Correction / caution.** Do not identify the Euler-product tensor (across primes) with the L ⊗ R tensor of the surface: Analogy only.

**Relations (outgoing):**

- special case of → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP4 headline (Missing Piece v5)
- lives in → [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) — splitting (a) = zero composite leakage (TAA Lemma 165)
- analogue of → [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) — TAA Lemma 163: the zero-side compact form is RH restated; the conjecture asks for the sign to be produced
- analogue of → [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) — TAA Lemma 164: coefficient positivity is not the sign
- analogue of → [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) — TAA Lemma 165: leaving the Euler product creates ghosts
- same mechanism as → [Hodge index theorem](#hodge-index) — splitting (b)
- lives in → [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) — standing assignment
- lives in → [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) — all places already present; coupling missing
- lives in → [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign)

**Relations (incoming):** [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) (lives in); [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) (lives in); [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (fails for)

### #51 · 0.560 · The shape of the missing piece: ten necessary properties (P1–P10) <a id="missing-piece-shape-list"></a>

**Label:** Open · **id:** `missing_piece_shape_list` · **quadrant:** RH-sharp

*In plain words:* Collecting what is proved around the window form and every no-go result gives a list of properties that any source of the missing sign must have. Four are proved necessary, the others are numerical or heuristic, as marked. The list constrains the object; it does not construct it.

**Core.** The shape of the missing piece: ten necessary properties (P1–P10). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Numbers.** P1 sees all primes jointly (fails when one prime is dropped) — proved necessary for this criterion [Theorem mechanism + Numerical] · P2 uses the Euler product and the functional equation together — Euler product necessary [Theorem, Davenport–Heilbronn]; functional equation necessary [Numerical only] · P3 invariant under the reflection s ↦ 1 − s (centrosymmetry of the window) [Restatement] · P4 gives a sign on the primitive part, not on the pole plane, which is indefinite (1,1) — proved necessary [Theorem, Haynsworth inertia] · P5 reduces to Castelnuovo–Severi / Hodge index over F_q [Heuristic: desirable, not forced] · P6 works with zero margin, as an identity rather than a bound — proved necessary [Theorem: no uniform margin; sup r = 1] · P7 controls the infimum of λ₂ over windows (monotone, continuous at log p), not jump events [Theorem + Numerical] · P8 is not ghost-blind: it must change when an off-line zero is planted — proved necessary [Theorem, logic] · P9 carries a metric, not only a measure: a positive pairing of half-densities [Heuristic/Restatement] · P10 is additive under gluing of windows: gluing defect 0 for ζ, at least 2 for Davenport–Heilbronn [Numerical; testable]

**Axes:** open target, Spec ℤ gap, sign/positivity (Ax2), ghost-sensitive

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.5 → priority 0.560

> ⚠ **Correction / caution.** Every criterion on this list that is equivalent to RH is circular as an input.

> ⚠ **Correction / caution.** The missing structure is referred to as Deninger’s conjectured cohomology; no new name is coined.

**Relations (outgoing):**

- constrains → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1)
- constrains → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo)
- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)
- uses → [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime)
- uses → [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction)
- uses → [λ₂ is monotone under nested windows (Cauchy interlacing)](#lambda2-monotone-nested-windows)
- uses → [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric)

### #130 · 0.419 · Hilbert–Pólya <a id="hilbert-polya"></a>

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

**Relations (incoming):** [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) (analogue of); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #133 · 0.419 · Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24 <a id="central-term-24-algebra-conjecture"></a>

**Label:** Conjecture · **id:** `central_term_24_algebra_conjecture` · **quadrant:** true but ghost-blind/untested

*In plain words:* What survives of the 1/24 idea is a conjecture: an operator algebra acting on the window space, with a central term fixed by 24 (an analogue of the Virasoro central charge), whose constraints force the window form to have exactly one negative square for ζ (the pole as the single "tachyon") and none for Δ. Nothing known constructs such an algebra. A cheap test of the "tachyon = pole" reading: E₁₂ against Δ in the window model.

**Core.** Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** Prediction to test: n₋ = 1 for ζ, n₋ = 0 for Δ, and two pole-type modes for E₁₂ (poles at s = ½ ± 11/2)

**Axes:** open target, physics analogue, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

> ⚠ **Correction / caution.** The 1/24 in the window model acts only through the weight, and its edge is generic, so the conjecture has no numerical support yet.

> ⚠ **Correction / caution.** If stated as "the quotient is positive" it is equivalent to RH; the content would be the algebra, not the sign.

**Relations (outgoing):**

- refines → [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy)
- refines → [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst)

### #151 · 0.380 · Global complex structure J on arithmetic H¹ (sharpened missing piece) <a id="global-j-missing-piece"></a>

**Label:** Conjecture · **id:** `global_J_missing_piece` · **quadrant:** RH-sharp

*In plain words:* RH would follow from a real structure J (J² = −1, antisymmetric) on the conjectural arithmetic H¹, commuting with the flow and making tr(f ∪ Jf) positive, restricting to the Frobenius rotation α_p/√p at each prime and to multiplication by i on the critical line at infinity. A Z/4 action with J² = −1 is the same assumption as i. i ∈ Q_p iff p ≡ 1 mod 4. Local pieces are theorems (Hasse, Deligne); the CM case shows local coherence is insufficient.

**Core.** Global complex structure J on arithmetic H¹ (sharpened missing piece)

**Axes:** open target, Spec ℤ gap, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.5 → priority 0.380

> ⚠ **Correction / caution.** fourth roots of unity do not avoid assuming i; they are i

> ⚠ **Correction / caution.** C is the completion of Q(i), not of Q

> ⚠ **Correction / caution.** forcing |α_p| = √p is the local RH, already a theorem

**Relations (outgoing):**

- refines → [Deninger’s foliated program](#deninger)
- refines → [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open)
- analogy of → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

**Relations (incoming):** [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece) (refines); [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) (refines); [One Perron mode against the pole](#pole-perron-one-mode) (refines); [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix) (counterexample to sufficiency of); [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings) (refines); [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality) (analogy of); [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids) (refines); [CM case: the Hasse triangle is Fermat's two-squares triangle](#cm-gaussian-hasse-triangle) (counterexample to sufficiency of); [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton) (analogy of); [One log-gas and its frozen limit](#log-gas-frozen-limit) (analogy of)

### #152 · 0.380 · Hodge energy on arithmetic cohomology, and a torsion term with forced sign <a id="deninger-hodge-energy-torsion-open"></a>

**Label:** Open · **id:** `deninger_hodge_energy_torsion_open` · **quadrant:** RH-sharp

*In plain words:* Deninger's heuristic: if H¹ of compactified Spec Z had a Hodge star making tr(f ∪ ⋆f′) positive definite and commuting with the flow, the generator would be ½ plus a skew operator, giving RH. This is a Maxwell-energy shape (∫F∧⋆F). Open: no arithmetic field strength exists, and it is unknown whether the conjectural cohomology or its foliated models carry a torsion term with a forced sign.

**Core.** Hodge energy on arithmetic cohomology, and a torsion term with forced sign Deninger, Doc. Math. Extra Vol. ICM 1998 I, 163–186, pp. 169, 172, 180.

**Formula.** ⟨f,f′⟩ = tr(f ∪ ⋆f′) > 0, [Θ,⋆] = 0, Θ a derivation ⇒ Θ = ½ + A, Aᵀ = −A ⇒ zeros on Re s = ½

**Axes:** open target, Spec ℤ gap, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.2 · evidence 0.5 → priority 0.380

> ⚠ **Correction / caution.** positivity here is a hypothesis on ⋆; the content is a ⋆ compatible with the flow

> ⚠ **Correction / caution.** arXiv:0709.2801 has the leafwise Hodge decomposition but no separate positivity statement; the proposal is in the ICM 1998 paper

**Relations (outgoing):**

- refines → [Deninger’s foliated program](#deninger)
- analogy of → [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear)
- analogy of → [Einstein–Cartan: spin enters as torsion](#einstein-cartan-torsion-spin)

**Relations (incoming):** [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric) (constrains); [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece) (refines)

### #252 · 0.292 · Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow <a id="hopf-fibration-spec-z"></a>

**Label:** Conjecture · **id:** `hopf_fibration_spec_z` · **quadrant:** true but ghost-blind/untested

*In plain words:* The KS map that turns Kepler into an oscillator is the Hopf fibration of S³. In the knots–primes dictionary, its arithmetic analogue would be a three-dimensional foliated system with a compact flow whose closed orbits are the primes; RH would say the net form is a sum of squares in that coordinate. A literal circle action is impossible because the periods log p are incommensurable; the compact object would be the Bohr torus. RH is not proved.

**Core.** Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow

**Axes:** open target, Spec ℤ gap, physics analogue

**TAA lemmas:** 180, 13, 19

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.292

**Relations (outgoing):**

- refines → [Deninger’s foliated program](#deninger)
- analogy of → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

**Relations (incoming):** [Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity](#arithmetic-topology-linking-matrix) (constrains)

### #253 · 0.292 · Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy <a id="perelman-template-dbn"></a>

**Label:** Open · **id:** `perelman_template_dbn` · **quadrant:** true but ghost-blind/untested

*In plain words:* Perelman found a quantity that the Ricci flow forces to increase. At one prime the dBN flow has such quantities. No such quantity is known for the whole product, and the link to Galois deformations is only an analogy.

**Core.** Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy

**Formula.** Ṡ = 2Σ_k(∂_k S)² ≥ 0 (finite real-rooted polynomials)

**Numbers.** degree 8: Ṡ = 53.110 both ways

**Axes:** open target, physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.292

**Relations (outgoing):**

- contrasts with → [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction)
- analogy of → [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles)

**Relations (incoming):** [Forced functionals of the finite dBN zero gas: dL/dt = 2E, dE/dt ≤ 0; W = L − (n(n−1)/4) log S₂ nondecreasing, constant on Hermite configurations; Y = ΣIm² nonincreasing; de Bruijn envelope y_max(t)² ≤ max(y₀² − 2(t − t₀), 0)](#zero-gas-forced-functionals) (refines)

### #254 · 0.271 · Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack <a id="identity-not-estimate"></a>

**Label:** Heuristic · **id:** `identity_not_estimate` · **quadrant:** background

*In plain words:* With local room but no global room, a proof has to show the sign exactly rather than bound it.

**Core.** Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack

**Formula.** Λ_p<0 locally; Λ=0 globally

**Axes:** open target, sign/positivity (Ax2), Spec ℤ gap

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.271

> ⚠ **Correction / caution.** The slack is in the de Bruijn–Newman direction only; it is not a null vector of Weil's form.

**Relations (outgoing):**

- refines → [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin)

**Relations (incoming):** [The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation](#single-box-axis-criterion) (refines); [The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions](#prime-weight-anisotropy) (refines); [Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance](#thermodynamic-j-direction) (feeds)

### #255 · 0.271 · The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger) <a id="edge-boundary-cycle"></a>

**Label:** Heuristic · **id:** `edge_boundary_cycle` · **quadrant:** background

*In plain words:* ∂∂ = 0 carries no sign; the positivity must come from extra structure.

**Core.** The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)

**Axes:** open target, Spec ℤ gap

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.271

**Relations (outgoing):**

- explains → [(τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²](#exactness-monge-ampere)
- heuristically points to → [Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology)](#deninger-derivation-positivity)

**Relations (incoming):** [d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1)](#dolbeault-kahler-sign) (supplies the sign for)

### #256 · 0.271 · RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin <a id="kahler-package-one-liner"></a>

**Label:** Heuristic · **id:** `kahler_package_one_liner` · **quadrant:** background

*In plain words:* The pole push has signature (1,1) and K is unsigned.

**Core.** RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin

**Axes:** open target, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.271

**Relations (outgoing):**

- sharpens → [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece)
- uses → [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation)

**Relations (incoming):** [One operator that is a sum of squares (net ≥ 0 as an identity) and generates dBN (∂_tH = +Δ_z H, backward heat on the real line); stronger than Hilbert–Pólya](#both-at-once) (strengthens)

### #317 · 0.240 · RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole <a id="sharpened-missing-piece"></a>

**Label:** Restatement · **id:** `sharpened_missing_piece` · **quadrant:** RH-sharp

*In plain words:* A programme, not a theorem; boundary term cannot be W_R itself.

**Core.** RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole

**Axes:** open target, restatement ⇔ RH, sign/positivity (Ax2), Spec ℤ gap, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (incoming):** [Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻](#talenti-template-test) (constrains); [Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology)](#deninger-derivation-positivity) (candidate setting for); [RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin](#kahler-package-one-liner) (sharpens); [(τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²](#exactness-monge-ampere) (explains)

### #343 · 0.165 · Candidate formulations of Castelnuovo-Severi over the integers <a id="cs-for-spec-z-formulations"></a>

**Label:** Open · **id:** `cs_for_spec_z_formulations` · **quadrant:** true but ghost-blind/untested

*In plain words:* Ranked candidates: Hodge index on the span of translates (a restatement of RH), a fibre-null completion of the pole channel, a quadratic Riemann-Roch on the square of the scaling site with the scaling correspondences as graphs, a positive involution on a first cohomology, and a q -> 1 finite-genus approximation. Obstructions: the product of Spec Z with itself collapses, fixed rank forces linear growth, counts do not induce the sign, and the functional equation is blind to off-line zeros.

**Core.** Candidate formulations of Castelnuovo-Severi over the integers

**Axes:** open target, Spec ℤ gap, sign/positivity (Ax2)

**TAA lemmas:** 181

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.165

**Relations (outgoing):**

- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

**Relations (incoming):** [Castelnuovo-Severi and Weil's bound](#castelnuovo-severi-lemma) (analogy of)

### #346 · 0.165 · One operator that is a sum of squares (net ≥ 0 as an identity) and generates dBN (∂_tH = +Δ_z H, backward heat on the real line); stronger than Hilbert–Pólya <a id="both-at-once"></a>

**Label:** Open · **id:** `both_at_once` · **quadrant:** true but ghost-blind/untested

*In plain words:* Hodge flow is e^{−tΔ}; dBN is e^{+tΔ_z} on the spectral variable.

**Core.** One operator that is a sum of squares (net ≥ 0 as an identity) and generates dBN (∂_tH = +Δ_z H, backward heat on the real line); stronger than Hilbert–Pólya

**Axes:** open target, sign/positivity (Ax2), Spec ℤ gap

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.165

**Relations (outgoing):**

- strengthens → [RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin](#kahler-package-one-liner)

## Axis: no-go / refuted <a id="axis-no-go-refuted"></a>

### #2 · 0.720 · Davenport–Heilbronn function <a id="davenport-heilbronn"></a>

**Label:** Theorem · **id:** `davenport_heilbronn` · **quadrant:** RH-sharp

*In plain words:* Has a functional equation but no Euler product, and zeros off the line.

**Core.** TAA Lemma 149: DH Gram matrix from its own prime side (c_DH from c*a = a·log, Γ((s+1)/2), conductor 5, no pole; no zero list): λ_max > 0 for all L ≥ 3.85 (hats h = 0.025), 0.224 at 4, 192 at 16; two positive from 3.90; h = 0.05 onset 5.75. TAA Lemma 153: archimedean factor = that of the odd character mod 5 with χ(2) = i (χ(−1) = χ(4) = i² = −1), so any archimedean-only object is DH-blind.

**Numbers.** 0.7398 (TAA Lemma 78) · 0.7376 (TAA Lemma 136) · 5×10⁻¹⁵ · −66.8 · Ξ_DH even to 4.5e−33, real on ℝ to 1e−31 · z₀ = τ₀² = 7344.2831 − 52.8794i · Z_DH: 62 sign changes vs N = 66 on [10,120]; deficits 2 in [80,90] and [110,120] (TAA Lemma 152) · TAA Lemma 153: prime-side tilt blocks (w = 1.5, τ = 0.3) hyperbolic on [84.36,84.77] (flank), [85.48,85.91] and [114.04,114.29]; nowhere else on [10,120]; every window within 1.4 of an off-line height (85.699, 114.163); first significant at X = e^12 (111,273 nonzero DH coefficients) · TAA Lemma 153: λ₋ = −1.884 at γ = 85.70 and −0.367 at 114.16 (τ = 0.3) · TAA Lemma 154: ρ₁ = 0.8085171824566 + 85.6993484853776i, ρ₂ = 0.6508300806097 + 114.1633427307570i (|f| ≤ 4e−30); Γ = 0.61703, 0.30166 · TAA Lemma 154: 75 on-line zeros γ < 135 refined; TAA Lemma 141 list ≤ 0.0144 off · Standard DH zero list (TAA Lemma 154: 75 on-line zeros γ < 135 refined to 1e−12, plus the two off-line pairs); supersedes the TAA Lemma 141 list (max deviation 0.0144); adopted as standard · [N] TAA Lemma 155: off-line zeros detected from coefficients + FE (ghost map): β̂ = 0.80852, 0.65083 at log X = 16; SNR ≥ 10 from log X = 4 · [N] TAA Lemma 155: exact comb from AFE with N = 12 / 13 terms (σ = 0.55) · [N, rigorous] TAA Lemma 156: standard list certified complete and accurate to 1e−12 for 2 < t < 135 (79 zeros) · [N, rigorous] TAA Lemma 156: further off-line pairs ρ₃ = 0.574356 + 166.479306i, ρ₄ = 0.724258 + 176.702461i (Krawczyk); 135 < t < 200 complete (51) · TAA Lemma 157: dual−adjoint gaps ρ₁ 0.617034364913, ρ₂ 0.301660161219, ρ₃ 0.148712100902, ρ₄ 0.448515389254 (DH has the dual, ρ ↔ 1−ρ, but no agreeing positive form) · TAA Lemma 158: DH = ½(1−iκ)L(s,χ) + ½(1+iκ)L(s,χ̄), χ mod 5, κ = 0.284079: two ℤ̂*-sectors (residual 0); a(2)a(3) = −0.0807 ≠ a(6) = 1 · TAA Lemma 159: coefficients (1, κ, −κ, −1, 0) mod 5; KMS Toeplitz min eig −7.78 (β = 2); 466/1999 negative Lévy coefficients; (log DH)″ < 0 on (1, 4.23183) (negative heat capacity); passivity min −15.08 at (0.75, 85.7) · TAA Lemma 160: N(135) = 79 vs main term 79.0002, N(200) = 130 vs 129.548 (χ-type count matches); on-line 75 / 122 (h-type deficit 4 / 8) · TAA Lemma 161 (reusing overnight cycle 3): 15 certified off-line quartets for 2 < γ ≤ 600, Γ from 0.032 (γ = 520.94) to 0.739 (γ = 240.40) · TAA Lemma 162: c(2)c(3) = −κ² ≠ c(6) = 1 ⇒ no Hecke eigen-system on S³; FE holds in span{Λ(χ),Λ(χ̄)} only at c = κ · TAA Lemma 163: Weil-Gram real form O(n−q, q), q ≤ 24; on-line spacings KS vs GUE.121 (464 zeros, 5% crit.063) · TAA Lemma 165: ghosts born from L(χ) along the σ-pencil at λ* ∈ [.033,.499], t ≤ 600; composite −L′/L terms from n = 6 · TAA Lemma 164: Toeplitz/Bochner test at β = 1.6 fails (DH not a partition function); companion positive ghost Z_Q (x²+5y²) · TAA Lemma 167: Weil index on kerP = full index (24 at h = 0.025, W = 15.95); onset 3.875 · TAA Lemma 174: Σa(n) bounded (θ = 0) yet no Euler product; composite share of |c(n)| 0.878 (458,230 atoms ≤ 2·10⁶)

**Also known as:** DH

**Axes:** no-go / refuted, ghost-sensitive

**TAA lemmas:** 78, 103, 136, 146, 148, 149, 150, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 164, 167, 174

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

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (fails for); [Lagarias/Hinkkanen criterion](#lagarias) (fails for); [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (fails for); [Relative Gram matrix G_rel](#relative-gram) (lives in); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (special case of); [DH prime-side Gram test](#dh-prime-side-gram) (analogue of); [DH prime-side Gram test](#dh-prime-side-gram) (corrects); [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) (tests); [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) (fails for); [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) (analogue of); [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) (fails for); [Epstein zeta no-go](#epstein) (same mechanism as); [Epstein zeta no-go](#epstein) (analogue of); [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) (fails for); [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) (analogue of); [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) (fails for); [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) (fails for); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (lives in); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (lives in); [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) (fails for); [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) (fails for); [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) (fails for); [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (fails for); [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) (fails for); [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (lives in); [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) (fails for); [Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x](#beurling-counting-test-bstar) (fails for); [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) (fails for); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (fails for); [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) (fails for); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) (fails for); [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) (fails for); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (fails for)

### #57 · 0.540 · Epstein zeta no-go <a id="epstein"></a>

**Label:** Theorem · **id:** `epstein` · **quadrant:** RH-sharp

*In plain words:* Epstein zeta functions of binary quadratic forms have a functional equation but no Euler product, and they have zeros off the line — the classic counterexample class next to DH.

**Core.** TAA Lemma 83: Epstein x² + 5y² = ζL(χ₋₂₀) + L(χ₋₄)L(χ₅); N(200) = 253 zeros, 183 on the line (70 off-line); first off-line 0.93297 + 15.66825i. TAA Lemma 135: 46 zeros with ½ < σ < 1 for t ≤ 250; control x² + y² (= 4ζL(χ₋₄), has Euler product): 0. TAA Lemma 138 R4: theta inversion and FE hold, unitarity ⇒ FE only, ghost-blind (Thm). TAA Lemma 153 (G, CM points): Σ′(m²+n²)^{−s} = 4ζ(s)L(s,χ₋₄) (NUM s = 3: 4.6589136156); Σ′(m²+mn+n²)^{−s} = 6ζ(s)L(s,χ₋₃) (6.3758815528); x²+5y²: ζ_K + L(χ₋₄)L(χ₅), 2x²+2xy+3y²: ζ_K − L(χ₋₄)L(χ₅), sum over the class group = 2ζ_K (Euler product restored, Hecke; NUM to 1e−12). Off-line zero refined: 0.9329696975 + 15.6682495313i (|Z| = 3e−21; ζ_K there 0.933). CM points are where one restricts (toric periods), not a quotient (TAA Lemma 153, correction 22). TAA Lemma 164 (merged here; the delta proposed a separate positive-ghost entry): Z_Q = ζL(χ₋₂₀) + L(χ₋₄)L(χ₅) (genus theory, checked n ≤ 300) has non-negative integer multiplicities (a Gibbs/KMS system with H = log Q(m,n)), the functional equation and Bochner positivity, yet zeros with ½ < Re ρ < 1, so KMS/thermal/partition-function positivity does not force RH; r_Q(2)r_Q(3) = 0 ≠ r_Q(6) = 4 (a sum of two Euler products, like DH). Davenport–Heilbronn 1936: infinitely many zeros in σ > 1 (cited). TAA Lemma 164 Krawczyk-certified 52 zeros with Re ρ ≥ 0.52, t < 400 (max Re 0.9549; mpmath |Z_Q(ρ₁)| = 2.8e−15). Correction (Missing Piece v5, I16): the 52 is a lower bound, not a census, because TAA Lemma 164's scan grid starts at σ = 0.52 (TAA Lemma 135 already found 46 zeros with ½ < σ < 1 for t ≤ 250, against 38 in TAA Lemma 164's list there); and the ghost is not new: it is this entry (TAA Lemma 83, TAA Lemma 135, TAA Lemma 138, TAA Lemma 153, TAA Lemma 159). TAA Lemma 164 adds the KMS/Bochner reading and the certification.

**Numbers.** 0.93297 + 15.66825i · N(200) = 253, 183 on line · 46 off-line zeros t ≤ 250 · TAA Lemma 164: ≥ 52 certified zeros with Re ρ ≥ 0.52, t < 400 (lower bound: grid starts at σ = 0.52) · r_Q(6) = 4, r_Q(2) = r_Q(3) = 0 · TAA Lemma 169: truncated Weil test h = 0.025: onset 3.0 (kerP 3.175, no pole 1.05); index 32 at W = 7.9; ζ_K control passes to W = 8 · TAA Lemma 174: counting θ̂ ≈ 0.32; composite share of |c(n)| 0.921; ψ slope 0.92 (max Re 0.955)

**Also known as:** Epstein; Epstein ghost; positive ghost; Z_Q, Q = x² + 5y²

**Axes:** no-go / refuted, ghost-sensitive, numerics/certificate

**TAA lemmas:** 83, 135, 138, 153, 159, 164, 169, 174

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** TAA Lemma 159: Epstein x² + 5y² is a genuine positive-weight gas (Bochner, convexity) with FE and an off-line zero: gas positivity is not RH-forcing; its log is not infinitely divisible (40 negative Lévy coefficients, n ≤ 2000).

> ⚠ **Correction / caution.** TAA Lemma 164 presented this ghost as new; it was already this entry (correction I16 of Missing Piece v5). Its count 52 is a lower bound, not a census.

**Relations (outgoing):**

- same mechanism as → [Davenport–Heilbronn function](#davenport-heilbronn)
- fails for → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — FE without RH
- same mechanism as → [Counts vs quadratic positivity](#count-positivity) — TAA Lemma 135 counts vs quadratic positivity
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — class number 2 ⇒ no Euler product ⇒ off-line zeros (DH 1936)
- lives in → [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) — CM points i, ρ
- fails for → [Bost–Connes KMS states](#kms-bost-connes) — passes KMS tests, has off-line zeros (TAA Lemma 164)
- lives in → [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) — TAA Lemma 164
- lives in → [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation)

**Relations (incoming):** [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) (fails for); [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) (fails for); [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (lives in); [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) (analogue of); [Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x](#beurling-counting-test-bstar) (fails for)

### #155 · 0.377 · Band criterion γ < 2T_M <a id="band-criterion"></a>

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

### #183 · 0.347 · No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n! <a id="nogo-v5-per-prime-and-places"></a>

**Label:** Theorem · **id:** `nogo_v5_per_prime_and_places` · **quadrant:** true but ghost-blind/untested

*In plain words:* Six more ingredients that cannot supply the missing sign: each works one prime (or one place) at a time, or matches data between primes, or restates RH.

**Core.** 27 per-prime SU(2)/Satake data (a_{p^k}/p^{k/2} = U_k(cos θ_p); 11a1: √12·U₂(−1/√2)·U₁(−1/(2√3)) = −2 = a₁₂; Flath; per-prime Rankin–Selberg ½ ⊗ ½ = Sym² ⊕ ζ). 28 per-prime norm identities (a_p² + |α−ᾱ|² = 4p; (p+1)² − (p−1)² = 4p, m = 2√p, v = (p−1)/(p+1); Kepler |A|² + 2m|E|L² = (mk)²): algebraic, true for every Satake pair. 29 correspondence alone: Jacquet–Langlands via the Shimizu theta lift, Langlands functoriality (Ramanujan via Symⁿ, not RH; Lafforgue used Deligne's RH as input) (not opened). 30 KMS/coefficient (Bochner) positivity (TAA Lemma 164): the Epstein ghost passes. 31 a compact real form on the zero side used as input (TAA Lemma 163): circular. 32 single-place data of n! (Γ, v_p, Γ_p, Gauss sums; the product formula as an identity). Each is ghost-blind or circular; requirements R1–R8′ unchanged.

**Numbers.** no-go list 26 → 32

**Also known as:** no-go 27–32; per-prime results are ghost-blind

**Axes:** no-go / refuted, ghost-blind

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.347

**Relations (outgoing):**

- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — inputs excluded from MP4(3)
- same mechanism as → [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) — item 30
- same mechanism as → [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) — item 31
- same mechanism as → [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) — item 32
- analogue of → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) — item 28
- analogue of → [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) — items 27, 29
- fails for → [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) — cannot supply the sign

**Relations (incoming):** [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime) (refines); [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) (lives in)

### #189 · 0.347 · Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x <a id="beurling-counting-test-bstar"></a>

**Label:** Numerical · **id:** `beurling_counting_test_bstar` · **quadrant:** true but ghost-blind/untested

*In plain words:* To separate the genuine integers from imitations, count how many 'integers' lie below x and compare with the expected straight line. For ℤ the error never exceeds 1. Imitation number systems built with random or slightly shifted primes wobble by about √x, which first suggested a conjecture (B*): a system with unique factorization whose wobble stays well below √x must satisfy RH. That now looks false. Choosing the imitation primes deterministically, so that they track a smooth system with a planted zero off the line, keeps unique factorization and keeps the planted zero exactly, yet the wobble grows only like x^0.29 as far as it was computed (x = 5·10⁷). So counting regularity alone does not force RH. This is numerical evidence, not a proof: nobody has shown the exponent stays below ½ forever.

**Core.** [N] B* (Euler product + N(x) = ρx + O(x^θ), θ < ½ ⇒ RH) appears false: a deterministic discretization of the continuous Beurling system below (g-primes chosen greedily so that the prime-counting discrepancy, prime powers included, stays ≤ 1) keeps an exact zero at 0.75 ± 10i, because ζ_P = ζ_T·e^H with H holomorphic on Re s > 0 [T, given the continuous system], while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (max|N − ρx| ≈ 4.3·x^0.3; ratio to √x falls from 0.61 to 0.116). Asymptotic θ < ½ is not proved, so this is a numerical refutation, not a theorem. Compare Diamond–Montgomery–Vorhauer (2006) and Broucke–Vindas (arXiv 2102.08478); prior examples were not exhaustively searched. Consequence: integer-counting regularity is a no-go as a route to RH on its own. [N] Earlier controls to X = 10⁷: random (Poisson) discretizations and integer-supported random multiplicities fluctuate at order √x; that √x noise came from the prime-counting discrepancy, not from discreteness [H]. [T] continuous system ζ_C = (s − ρ₀)(s − ρ̄₀)(s + 10)/(s²(s − 1)), N_C = ρx + O(log² x), positivity min f/t = 0.193 (computer-assisted). [C] DMV 2006 (θ > ½, RH fails), Zhang (RH with regular N), BDV 2020 (RH with large N oscillation), Hilberdink 2005 (the integer and prime exponents cannot both be < ½; not contradicted here, since the prime count is far from li x).

**Numbers.** deterministic discretization: θ̂ ≈ 0.28–0.29 up to x = 5·10⁷ (2,994,465 g-primes); max|N − ρx| ≈ 4.3·x^0.3; ratio to √x 0.61 → 0.116 · ψ regression coefficient on the planted term 0.9999993 · random controls, ratio to √x: PERT 0.19–0.28; CRAMER 0.6–1.4; ZERO 1.6–2.0; RANDMULT 3.1–4.4 · θ̂: Epstein 0.32, ζ_Q(i) 0.32

**Also known as:** B*; B* no-go; Beurling controls; integer-counting regularity

**Axes:** no-go / refuted, numerics/certificate, ghost-blind, Spec ℤ gap

**TAA lemmas:** 174

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.347

> ⚠ **Correction / caution.** θ̂ are finite-range slopes (x ≤ 5·10⁷); θ < ½ asymptotically is not proved.

> ⚠ **Correction / caution.** B* was earlier listed as a live conjecture; it is withdrawn on this numerical evidence.

> ⚠ **Correction / caution.** Euler product + counting data still excludes Davenport–Heilbronn and Epstein, but only through the Euler product.

> ❓ **Not verified / open.** Numerical refutation: θ < ½ for the discretized system is not proved asymptotically; prior examples in the literature were not exhaustively searched.

**Relations (outgoing):**

- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — no Euler product (4,062 defects ≤ 200)
- fails for → [Epstein zeta no-go](#epstein) — no Euler product (1,566 defects)
- lives in → [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) — (B) as the additive shadow of stable directions [H]

### #210 · 0.325 · Local-to-global failure <a id="local-global"></a>

**Label:** Theorem · **id:** `local_global` · **quadrant:** true but ghost-blind/untested

*In plain words:* Local positivity at each prime does not imply global.

**Core.** TAA Lemma 25 Rem 6.2: naive local positivity fails (K < 0 for |r| < 6.28984); CC21 Thm 1 local archimedean positivity only for supp ⊂ [2^{−½}, 2^{½}] with vanishing. TAA Lemma 64/TAA Lemma 65: local Hasse (Q_p > 0 at every p, proved) vs global RH for L(E,s) (open) — the collective split. TAA Lemma 66: local positivity via Deligne weights is ghost-blind residual data.

**Numbers.** |r| < 6.28984

**Also known as:** local positivity

**Axes:** no-go / refuted

**TAA lemmas:** 25, 64, 65, 66, 91

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (incoming):** [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime) (refines)

### #270 · 0.267 · Counts vs quadratic positivity <a id="count-positivity"></a>

**Label:** Theorem · **id:** `count_positivity` · **quadrant:** true but ghost-blind/untested

*In plain words:* Point counts being positive does not force RH; only quadratic forms can.

**Core.** TAA Lemma 109: 2935 count-positive ghosts (g = 2, q = 11).

**Numbers.** 2935 · TAA Lemma 166: exact census (|a| ≤ 6q, |b| ≤ 20q, d ≤ 40): 675 (q = 7), 2935 (q = 11, reproduces TAA Lemma 109), 4961 (q = 13); on-circle 205/401/513

**Also known as:** N_n ≥ 0

**Axes:** no-go / refuted, ghost-blind

**TAA lemmas:** 109, 166

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly)

**Relations (incoming):** [Epstein zeta no-go](#epstein) (same mechanism as); [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (same mechanism as); [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) (analogue of); [Tate count / Picard number (ghost-blind)](#tate-count) (same mechanism as)

### #297 · 0.267 · Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1) <a id="hecke-toy-contraction"></a>

**Label:** Theorem · **id:** `hecke_toy_contraction` · **quadrant:** true but ghost-blind/untested

*In plain words:* The simplest prime-indexed ladder operators fail to close into a spin algebra; they contract.

**Core.** Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1)

**Axes:** no-go / refuted, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- illustrates → [Hecke operators](#hecke)
- obstructs → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #301 · 0.267 · Saddles of Euler products: curvature is additive and the cross-prime term at a saddle is always non-positive <a id="euler-product-saddle-additivity"></a>

**Label:** Theorem · **id:** `euler_product_saddle_additivity` · **quadrant:** true but ghost-blind/untested

*In plain words:* For a product of local factors, minus the second log-derivative is a sum over primes. At a saddle the cross terms combine to minus a sum of squares, so they always oppose; the matrix of pairwise saddle margins is entrywise positive but indefinite. Saddle geometry carries no positive cross-prime coupling.

**Core.** Saddles of Euler products: curvature is additive and the cross-prime term at a saddle is always non-positive

**Formula.** F″/F = Σ f_p″/f_p + 2Σ_{p<q}(f_p′/f_p)(f_q′/f_q) and, at a saddle, the cross term = −Σ (f_p′/f_p)²

**Numbers.** 11a1, 2–20 factors: 22–809 saddles, all longitudinal; identity to 8e−16 · pairwise matrix: 1, 2, 3, 6, 11, 21, 30 negative eigenvalues for N = 2, 3, 5, 10, 20, 40, 60

**Axes:** no-go / refuted, sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 180, 55, 56

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- constrains → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #311 · 0.267 · Forced functionals of the finite dBN zero gas: dL/dt = 2E, dE/dt ≤ 0; W = L − (n(n−1)/4) log S₂ nondecreasing, constant on Hermite configurations; Y = ΣIm² nonincreasing; de Bruijn envelope y_max(t)² ≤ max(y₀² − 2(t − t₀), 0) <a id="zero-gas-forced-functionals"></a>

**Label:** Theorem · **id:** `zero_gas_forced_functionals` · **quadrant:** true but ghost-blind/untested

*In plain words:* For finitely many zeros the flow forces several quantities to move in one direction, Perelman-style. None of them decides anything at time zero, for heuristic reasons.

**Core.** Forced functionals of the finite dBN zero gas: dL/dt = 2E, dE/dt ≤ 0; W = L − (n(n−1)/4) log S₂ nondecreasing, constant on Hermite configurations; Y = ΣIm² nonincreasing; de Bruijn envelope y_max(t)² ≤ max(y₀² − 2(t − t₀), 0)

**Numbers.** n = 10: W_Hermite = −50.2043

**Axes:** no-go / refuted, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** None of these functionals decides the sign at time zero (Heuristic). The claim that y_max² + 2t is nonincreasing is false as stated.

**Relations (outgoing):**

- refines → [Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy](#perelman-template-dbn)

## Axis: sign/positivity (Ax2) <a id="axis-sign-positivity-ax2"></a>

### #3 · 0.720 · Weil positivity criterion <a id="weil-positivity"></a>

**Label:** Cited · **id:** `weil_positivity` · **quadrant:** RH-sharp

*In plain words:* A quadratic form built from primes, the archimedean place and the pole. RH holds exactly when it is never negative.

**Core.** Weil 1952: RH ⇔ W(f∗f̃*) ≥ 0 for all test f; equivalently the Hermitian form 𝒬 is positive, ⇔ a unitary Hilbert realization of the scaling flow (TAA Lemma 1 Thm 2.1 (iv)). TAA Lemma 161: positivity read as definite (apsidal/Kepler) stability vs gyroscopic (TAA Lemma 4) stability: the FE is a work-free J that DH also has; only a definite form excludes Krein collisions (Heuristic).

**Formula.** RH ⇔ W(f ∗ f̃*) ≥ 0 ∀f

**Numbers.** κ(𝒬) = N₊ (TAA Lemma 1)

**Also known as:** Weil criterion; W(f∗f̃*) ≥ 0; Weil form 𝒬; arithmetic action S[F]

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH, Spec ℤ gap

**TAA lemmas:** 1, 17, 98, 103, 142, 152, 161

**Scores (Heuristic):** gap significance 0.8 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** The zero-side check is tautological (TAA Lemma 142); only the prime side with no zeros is a test.

> ⚠ **Correction / caution.** "Q = LP + positive" is false (TAA Lemma 8).

> ⚠ **Correction / caution.** Definition, not source (TAA Lemma 152 §3): Weil's criterion ⇔ RH, so it cannot by itself supply the positivity.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Weil 1952
- same mechanism as → [Relative Gram matrix G_rel](#relative-gram) — TAA Lemma 142: Weil form = relative intersection matrix on translates
- same mechanism as → [Hodge index theorem](#hodge-index) — Spec ℤ analogue of Hodge index on V₀ (TAA Lemma 91)
- same mechanism as → [Two-point form g + iω ≥ 0](#two-point) — TAA Lemma 103: g + iω ≥ 0 ⇔ Weil
- analogue of → [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability)

**Relations (incoming):** [Connes trace formula](#connes-trace) (same mechanism as); [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) (implies); [Relative Gram matrix G_rel](#relative-gram) (same mechanism as); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (lives in); [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) (tests); [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) (special case of); [Tautology boundary (zero side vs prime side)](#tautology-boundary) (same mechanism as); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (same mechanism as); [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity) (refines); [Li criterion](#li-criterion) (same mechanism as); [Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q](#burgers-local-toeplitz) (refines); [The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation](#single-box-axis-criterion) (restates); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (lives in); [Maxwell construction / convex effective potential](#maxwell-effective-potential) (analogue of); [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) (analogue of); [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) (restates); [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin) (restates); [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts) (restates); [Two-point form g + iω ≥ 0](#two-point) (same mechanism as); [Källén–Lehmann spectral positivity](#kallen-lehmann) (same mechanism as); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (same mechanism as); [Archimedean place and Γ_ℝ factor](#archimedean-place) (lives in)

### #5 · 0.720 · Two Verschiebungs: pairing dual V^∨ vs positive adjoint V† <a id="two-verschiebungs-dual-vs-adjoint"></a>

**Label:** Theorem · **id:** `two_verschiebungs_dual_vs_adjoint` · **quadrant:** RH-sharp

*In plain words:* The Verschiebung can be defined by a pairing (always available, blind to fake zeros) or by a positive inner product (the hard part). RH says the two definitions agree.

**Core.** [T] For a flow generator Θ on a real space with a nondegenerate pairing B for which Θ is a derivation into a twist-1 top class (B(Θx,y)+B(x,Θy) = B(x,y), Deninger's cup product), the B-dual is Θ^∨ = 1 − Θ (ρ ↦ 1−ρ: the functional equation, ghost-blind; DH has it). For a positive form g(x,y) = B(x,∗y) the g-adjoint is Θ† = ∗⁻¹ Θ^∨ ∗. Hence Θ† = Θ^∨ ⇔ [∗,Θ] = 0, and then Θ = ½ + A with A skew (Deninger ICM98 §3, p.169, opened). Group form: for F with ω(Fx,Fy) = q·ω(x,y), V := F^∨ = qF⁻¹ always; F† = qF⁻¹ ⇔ F/√q ∈ Sp ∩ O = U(n). Polar F = UP: F^∨ = P⁻¹U⁻¹, F† = PU⁻¹, gap ‖F^∨ − F†‖ = ‖P − P⁻¹‖ (= 2 sinh r in 2D). Lie algebra: Θ^∨ − Θ† = −2S, S = symmetric (squeeze) part of Θ − ½. TAA Lemma 161: in 2D the gap form is the radial speed r·v; apsides are its zeros; circle ⇔ dual = adjoint; e_K = tanh d_H(i, τ).

**Numbers.** polar identities: 60 random Sp(2n), n ≤ 3, residuals ≤ 3.2e−10 · 2D gap = 2 sinh r: 0.6090405869 at r = 0.3

**Also known as:** V^∨ vs V†; dual vs adjoint; Θ† = ∗⁻¹Θ^∨∗

**Axes:** sign/positivity (Ax2), structure/frame (Ax1), ghost-sensitive

**TAA lemmas:** 157, 161

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** RH ⇒ dual = adjoint needs Θ normal for g (semisimple + orthogonal eigenlines); the converse needs nothing.

> ⚠ **Correction / caution.** Building the positive g from the Euler product is open (= MP4).

**Relations (outgoing):**

- same mechanism as → [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) — refines: dual vs adjoint
- same mechanism as → [Definite cup square / Krein one-liner](#definite-cup-square) — bilinear pairs ρ↔1−ρ; Hermitian pairs ρ↔ρ̄
- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j) — adjoint = J-conjugate of dual
- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP4 sharpened: Poincaré dual = Hilbert adjoint
- analogue of → [Deninger’s foliated program](#deninger) — Den98 p.169 argument
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — dual exists, no positive form agrees
- analogue of → [Rosati positivity](#rosati) — Rosati: π† = qπ⁻¹ = V
- same mechanism as → [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form)

**Relations (incoming):** [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (same mechanism as); [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (same mechanism as); [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) (lives in); [Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity)](#ep-gap-across-collision) (analogue of); [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) (same mechanism as)

### #7 · 0.720 · Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved <a id="kahler-triple-polarization"></a>

**Label:** Theorem · **id:** `kahler_triple_polarization` · **quadrant:** RH-sharp

*In plain words:* A positive form on phase space needs a choice of complex structure on top of the symplectic pairing; over finite fields the polarization provides it, for ζ it is missing.

**Core.** [T] ω antisymmetric (pairing side; Sp preserves it; ω-dual of symplectic F is F⁻¹). Positivity is extra data: compatible J, g = ω(·,J·) > 0 (Riemann form E with E(ix,x) > 0 for abelian varieties: polarization ⇒ Rosati positive). sp = u(n) ⊕ {squeezes}: rotations commute with J, squeezes anticommute. SL₂: for M ≠ ±1 the invariant symmetric forms form a line, spanned by a definite / indefinite / degenerate form as |tr M| <, >, = 2. 𝔽_q: M = Frobenius/√q on ℤ[π] preserves the norm form m² + amn + qn², positive ⇔ a² < 4q ⇔ TAA Lemma 150 lattice U ⊕ (−2N) has signature (1,3); fakes (2,2), det −(4q − a²) (q = 101: a = −3, 0, 12, 20 → (1,3); 21, 25, 40 → (2,2)). Hyperbolic Γ_q = 2 arccosh(|a|/2√q)/log q. TAA Lemma 161: S_t = |x − τp|² with τ = F/√q: the preserved complex structure; eccentricity measures d_H(i, τ) (e_K = tanh d).

**Numbers.** q = 101 trichotomy: 7/7 traces match (1,3)/(2,2) · a = 21: Γ_q = 0.1292230686

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive, structure/frame (Ax1)

**TAA lemmas:** 157, 161

**Scores (Heuristic):** gap significance 0.8 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** The J preserved by an elliptic M is forced by M (unique up to scale); the arithmetic content is that the polarization supplies the same g for all Frobenius powers.

**Relations (outgoing):**

- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j)
- same mechanism as → [Rosati positivity](#rosati)
- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann)
- lives in → [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) — missing arithmetic J
- same mechanism as → [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint)
- analogue of → [Metaplectic / Kubota cocycle](#metaplectic) — metaplectic preserves ω only

**Relations (incoming):** [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (same mechanism as); [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (same mechanism as); [Metaplectic / Kubota cocycle](#metaplectic) (same mechanism as); [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) (same mechanism as); [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) (analogue of); [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) (analogue of)

### #8 · 0.720 · Lagarias/Hinkkanen criterion <a id="lagarias"></a>

**Label:** Cited · **id:** `lagarias` · **quadrant:** RH-sharp

*In plain words:* RH ⇔ the log-derivative of ξ has positive real part to the right of the line.

**Core.** Lagarias 1999 (1.5), credited to Hinkkanen: RH ⇔ Re ξ′/ξ(s) > 0 on Re s > ½ (TAA Lemmas 17, 146).

**Formula.** RH ⇔ Re ξ′/ξ(s) > 0 (Re s > ½)

**Numbers.** DH: Re ξ′/ξ = −66.8

**Also known as:** Re ξ′/ξ > 0; Hinkkanen

**Axes:** sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 17, 146, 154, 157

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Passivity (positive real part)](#passivity)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH violates it
- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero)

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (same mechanism as); [Passivity (positive real part)](#passivity) (same mechanism as); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) (equivalent to RH); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as); [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) (refines); [Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing](#passive-network-positive-real) (restates); [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) (analogue of)

### #10 · 0.720 · Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting <a id="kahler-identities-foliated"></a>

**Label:** Theorem · **id:** `kahler_identities_foliated` · **quadrant:** RH-sharp

*In plain words:* Kähler identities make the Hodge star expressible through the complex structure and the Kähler class; then any flow that respects both is a rotation up to scale, which is RH. For Deninger's space positivity is free; the missing piece is a complex structure the flow respects.

**Core.** [C,N] Kähler identities [Λ,∂̄] = −i∂*, [Λ,∂] = i∂̄*, [L,Δ] = 0 (Wikipedia/Huybrechts §3.1; sign verified symbolically on ℂ² with ω = (i/2)Σdz∧dz̄: residual 0, opposite sign fails). sl₂ (L,Λ,Π) ⇒ hard Lefschetz, Hodge–Riemann on primitive classes. [C] Deninger–Singhof 2002 (opened): Kähler–Riemann foliations: H̄ⁿ_F = ⊕H^{pq} (depends only on J, Prop 4.2), hard Lefschetz (4.3), polarization (4.4), Prop 4.6 (Serre 1960 analogue): f leafwise holomorphic, f*[ω_F] = q[ω_F] ⇒ f* = q^{n/2}·unitary. [T] infinitesimal: Θ derivation, Θ[ω] = α[ω], [Θ,J] = 0 ⇒ Θ = nα/2 + skew on H̄ⁿ; finite model N: 60 trials, commuting part Re = ½ to 6e−16, generic sp part off-line in 88%. [T] Surface leaves (Deninger's 3-dim picture): ∗ = −J on 1-forms (∗dz = −i dz), positivity tr(h∪∗h) is automatic for every Riemannian foliation (Den05 (15)); so MP4 in degree 1 ⇔ [J,Θ] = 0 on H̄¹ (Restatement). Den05: 'one will need the Kähler identities on cohomology' (for (11)). El Kacimi 1990 (opened): basic (transverse) Hodge/Lefschetz — the other flavour, not Deninger's leafwise H̄.

**Numbers.** Kähler identity residual 0 (16 forms, ℂ²); opposite sign 14.55 · finite Serre model: Re − ½ ≤ 5.6e−16 when [J,Θ] = 0

**Also known as:** Serre Kählerian Weil analogue; Deninger–Singhof Prop. 4.6; leafwise Hodge splitting

**Axes:** sign/positivity (Ax2), structure/frame (Ax1), ghost-sensitive

**TAA lemmas:** 158

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** El Kacimi treats basic (transverse) cohomology; Deninger needs leafwise reduced cohomology (Deninger–Singhof).

> ⚠ **Correction / caution.** Leafwise holomorphic is a pointwise (forms) condition; Deninger doubts it for number fields. The cohomological condition [J,Θ] = 0 suffices but is equally open.

**Relations (outgoing):**

- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann)
- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j) — [J,Θ] = 0
- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) — ∗ = −J on H¹ of surfaces
- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP4 degree-1 form
- analogue of → [Deninger’s foliated program](#deninger) — Den05 Thm 4.1 toy model
- same mechanism as → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — arithmetic J
- same mechanism as → [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) — dual = adjoint ⇔ [∗,Θ] = 0

**Relations (incoming):** [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) (same mechanism as); [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) (analogy of); [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) (analogue of)

### #12 · 0.720 · Definite cup square / Krein one-liner <a id="definite-cup-square"></a>

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

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (same mechanism as); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as)

### #24 · 0.600 · Relative Gram matrix G_rel <a id="relative-gram"></a>

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

### #25 · 0.600 · Verschiebung as the positive adjoint of Frobenius (F† = V) <a id="verschiebung-positive-adjoint"></a>

**Label:** Restatement · **id:** `verschiebung_positive_adjoint` · **quadrant:** RH-sharp

*In plain words:* Frobenius has a partner map going the other way, Verschiebung, with F·V = q; the true statement behind RH is that V is the mirror image (adjoint) of F for a positive inner product, and J. W. McGreevy’s animation runs this pairing continuously.

**Core.** [T] On an elliptic curve over F_q: FV = VF = q and F + V = a (trace); deg(m − nF) = (m − nF)(m − nV) = m² − a·mn + q·n² (the norm conic); a² < 4q ⇒ ellipse and V = F̄ (complex conjugate eigenvalues), so |α|² = αᾱ = FV = q: Hasse; a² = 4q double line; a² > 4q hyperbola, F, V two different real numbers (a fake). Dieudonné modules W(k){F,V}/(FV − p); Rosati: π∘π† = q ⇒ π† = qπ⁻¹ = V (TAA Lemma 115 §6.1, Milne AV Lemma 1.2 as cited there). [R] The ghost-sensitive statement is V = F† for a POSITIVE form (Rosati trace form): ⟨Fx,Fy⟩ = q⟨x,y⟩ (Krein one-liner, definite_cup_square); for a finite model RH ⇔ there is a positive involution with F† = V (TAA Lemma 115 §6.3, via TAA Lemma 113 Thm 2.1). Flow form: adjoint = inverse up to eᵗ ⇔ Re ρ = ½. On the Eisenstein constant term Ve = Fr̄ on y^s iff Re s = ½ (TAA Lemma 115; a Ramanujan statement for E(·,s), not RH for ζ). [Ghost-blind] FV = q alone is pure algebra: any fake with char. poly x² − ax + q has V = a − F with FV = q (TAA Lemma 113 Thm 5.1 via TAA Lemma 115). TAA Lemma 117 §4: with the pairing ρ ↔ 1 − ρ̄, Ve = Fr† always; an on-line zero is self-paired (definite square), an off-line pair spans a hyperbolic plane where p^{−½}Fr is a boost of rapidity δ log p. TAA Lemma 121: Π_p′ (transpose of Frobenius) is Verschiebung, Π_pΠ_p′ = p; mod p, Φ_p = 0 is graph of j ↦ j^p ∪ its transpose (Kronecker congruence). [A] J. W. McGreevy’s animation as the dynamic F ↔ V sweep: the half turn swaps F and V; running a through a² < 4q, = 4q, > 4q is lobe → wedge → hyperbola. TAA Lemma 157: V^∨ (pairing dual, = qF⁻¹, ghost-blind) vs V† (positive adjoint); F† = J⁻¹F^∨J; agree ⇔ F/√q ∈ U(n); per-eigenline gap |q/α − ᾱ| (exponent form Γ = |1−2β|).

**Formula.** FV = VF = q; deg(m − nF) = (m − nF)(m − nV); F† = V ⇔ |α| = √q

**Numbers.** TAA Lemma 115: s = ½ + 7.3i, p = 3: Fr = −0.28601 + 1.70827i, Ve = conj(Fr), Fr·Ve = 3 · TAA Lemma 115: T_pE = (p^{s−½} + p^{½−s})E checked to 1e−30

**Also known as:** F ↔ V swap; Rosati adjoint of Frobenius; FV = VF = q

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 115, 117, 121, 152, 153, 157

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

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (same mechanism as); [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) (analogue of); [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #26 · 0.600 · Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts) <a id="cayley-klein-absolute"></a>

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

**Relations (incoming):** [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (same mechanism as); [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) (special case of); [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) (same mechanism as)

### #27 · 0.600 · Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0 <a id="rr-strategy-sff"></a>

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

### #42 · 0.579 · Ax1–Ax3 axioms (Yoneda specification) <a id="ax123"></a>

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

### #52 · 0.540 · Rosati positivity <a id="rosati"></a>

**Label:** Theorem · **id:** `rosati` · **quadrant:** RH-sharp

*In plain words:* An involution † on endomorphisms with Tr(φφ†) > 0 — like a squared length that is never negative. With ππ† = q it forces |α| = √q.

**Core.** Tr(φφ†) > 0 on End⁰(J); ππ† = q ⇒ |α| = √q (Milne AV 14.3). On R[F]: Rosati PD ⇔ RH-model ⇔ ∃ compatible J with [J,F] = 0; n₋ = #real pairs + 2#quartets (TAA Lemma 106). Over ℚ: Rosati = Weil form is a restatement.

**Formula.** Tr(φφ†) > 0; ππ† = q

**Numbers.** E^n over F₅: Tr = 2ΣN(φ_ij) > 0, 3000/3000 (TAA Lemma 136) · signatures true (2,0),(4,0),(8,0); ghost (1,1); quartet (2,2) · TAA Lemma 157: Rosati positivity = the g of the Kähler triple attached to the polarization (Riemann form E(ix,x) > 0); dual = adjoint ⇔ |α| = √q

**Also known as:** Rosati involution †; Tr(φφ†) > 0; positive involution; Ax2∧Ax3

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 84, 99, 106, 133, 136, 151, 157

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

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (analogue of); [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (same mechanism as); [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (same mechanism as); [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) (analogue of); [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (special case of); [Castelnuovo–Severi inequality](#castelnuovo-severi) (same mechanism as); [Hasse bound as a positive degree form](#hasse-pythagoras) (special case of); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Cartan involution / compact unitary group](#cartan-involution) (same mechanism as); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of); [Mass-density positivity](#mass-density) (analogue of)

### #54 · 0.540 · Castelnuovo–Severi inequality <a id="castelnuovo-severi"></a>

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

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (same mechanism as); [Rosati positivity](#rosati) (same mechanism as); [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (special case of); [RH for curves over F_q (Weil)](#fq-curves) (implies); [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity) (restates); [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) (analogue of); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) (fails for); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (fails for); [Buoyancy / Archimedes principle](#archimedes) (analogue of); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (analogue of)

### #62 · 0.540 · F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern) <a id="fv-merge-trichotomy"></a>

**Label:** Theorem · **id:** `fv_merge_trichotomy` · **quadrant:** RH-sharp

*In plain words:* As Frobenius and Verschiebung slide together on the unit circle, the invariant conic goes from a circle to ever thinner ellipses; when they meet it degenerates, and past that it becomes a hyperbola with positive and negative wedges, which only fake zeta functions reach.

**Core.** [T] M_t = [[0,−1],[1,t]] (Frobenius/√q on ℤ[π], t = a/√q) preserves Q_t = m² + tmn + n² (residual 0); disc t² − 4: |t| < 2 definite (closed ellipses; circle iff t = 0), |t| = 2 degenerate, |t| > 2 indefinite (1,1): + in two opposite wedges, − in the other two. Eigenvalues α, ᾱ = (t ± i√(4−t²))/2 start at ±i (t = 0), meet at 1 (t = 2), split on ℝ. Fixed point τ(t) = (−t + i√(4−t²))/2 of z ↦ −1/(z+t): τ = i at t = 0 (the round START), → ∂ℍ as |t| → 2. [N] t = 0 occurs for every supersingular E/𝔽_p, p ≥ 5 (y² = x³ − x, p ≡ 3 mod 4: 8/8; y² = x³ + 1, p ≡ 2 mod 3: 9/9): not specific to CM by ℤ[i]. |t| = 2 on actual curves: y² = x³ − x over 𝔽_{p²} (p = 3, 7, 11): a = −2p, π = −p scalar (every form invariant, TAA Lemma 157, correction 4), not a Jordan block. [T] Mirror α ↔ ᾱ and half turn Q(−x) = Q(x) persist in every stage: ghost-blind; the signal is sign(t² − 4) (signature), coordinate-free. [A] The merge is the 𝔽_q picture of the de Bruijn–Newman collision. TAA Lemma 160: the merge never happens in a single Euler factor at a good prime (|a_p| < 2√p); at the level of zeros it is the dBN double zero (zeros_as_frames_trichotomy); one-frame Wick rotation in euler_factor_wick_rotation. TAA Lemma 161: F = V is the parabolic escape of the invariant conic (Kepler e_K = t/2 = 1 after Bohlin); hyperbolic F, V span the asymptotes, mirror images in the 45° apsidal axis.

**Numbers.** trace 0: 17/17 supersingular examples · scalar Frobenius over F_{p²}: a = −2p for p = 3, 7, 11

**Also known as:** tilt

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive, structure/frame (Ax1)

**TAA lemmas:** 158, 160, 161

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** τ = i is the start (t = 0), not the meeting point (TAA Lemma 158, correction 13).

> ⚠ **Correction / caution.** At |t| = 2 actual curves have scalar Frobenius; the parallel-line picture is the non-semisimple model (TAA Lemma 158, correction 14).

> ⚠ **Correction / caution.** The 'tilt' of an axis is coordinate-dependent; use the discriminant/signature (TAA Lemma 158, correction 17).

**Relations (outgoing):**

- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity)
- same mechanism as → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — SL₂ trichotomy
- same mechanism as → [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) — half turn ghost-blind
- analogue of → [de Bruijn–Newman constant Λ](#debruijn-newman) — collision ↔ merge
- same mechanism as → [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) — lobes vs wedges
- fails for → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — hyperbolic stage

**Relations (incoming):** [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (same mechanism as); [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) (same mechanism as); [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) (same mechanism as); [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep) (refines)

### #63 · 0.540 · Compatible complex structure J commuting with Frobenius <a id="compatible-j"></a>

**Label:** Theorem · **id:** `compatible_J` · **quadrant:** RH-sharp

*In plain words:* A quarter-turn that commutes with Frobenius and makes the form positive; it exists exactly when the curve satisfies RH.

**Core.** J = (2F − a)/√(4q − a²) (TAA Lemma 101) exists only if a² < 4q; 2^g sign choices, exactly one positive. Finite: compatible J with [J,F] = 0 ⇔ F unitary semisimple (TAA Lemma 104). For ζ: J exists ⇔ RH (restatement, TAA Lemma 104 dichotomy).

**Formula.** J = (2F − a)/√(4q − a²)

**Numbers.** g = 1, q = 101: J = J_F exact; ghosts give Cl(1,1)

**Also known as:** J = (2F − a)/√(4q − a²); h(i); polarizing J

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 99, 100, 101, 104, 110

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** A quartet J is symplectic but never compatible (sig (2,2)) (TAA Lemma 110).

> ⚠ **Correction / caution.** With a W-independent form J is unconditional but ghost-blind (TAA Lemma 104).

**Relations (outgoing):**

- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — for ζ
- same mechanism as → [Spinor/Clifford route](#spinor-route) — Clifford pair version

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (same mechanism as); [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (same mechanism as); [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (same mechanism as); [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (same mechanism as); [Spinor/Clifford route](#spinor-route) (same mechanism as); [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) (lives in)

### #67 · 0.540 · RH for curves over F_q (Weil) <a id="fq-curves"></a>

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

### #77 · 0.540 · Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q) <a id="trace-polarization-primitive-positivity"></a>

**Label:** Theorem · **id:** `trace_polarization_primitive_positivity` · **quadrant:** RH-sharp

*In plain words:* Split each class into the part along the two fibre directions and the rest. The first part is the polarization. Positivity means the rest is definite, and that only makes sense relative to the polarization. The two together are the Hodge index theorem, which is Weil's proof of RH for curves.

**Core.** Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)

**Formula.** π(D) = (D·v)h + (D·h)v; D² = 2(D·h)(D·v) + D₀²

**Numbers.** fake (5,5): signature (2,2); real: (1,3) · h − v complement indefinite even for real curves

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** The trace-free part alone is not positivity. The flowed primitive form is definite iff t > Λ_p (formal).

**Relations (outgoing):**

- restates → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- refines → [Weil positivity criterion](#weil-positivity)
- feeds → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)

**Relations (incoming):** [Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear](#trace-shear-budget) (refines); [On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH](#chirality-star-gamma5-hodge-index) (refines); [Hodge index in push/shear language: D² = (D·ω)²/ω² + D°², Hodge index ⇔ D°² ≤ 0 (shear can only subtract); D°² = D₀² − ½(D·h − D·v)²](#hodge-index-shear-subtracts) (restates)

### #78 · 0.540 · Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH <a id="free-gas-positivity-ladder"></a>

**Label:** Theorem · **id:** `free_gas_positivity_ladder` · **quadrant:** RH-sharp

*In plain words:* A genuine gas needs positive weights, and a free gas needs an Euler product. Davenport–Heilbronn fails both tests and even has negative heat capacity, but Epstein zeta functions and ζ(s)ζ(s+a) pass them and still have zeros off their lines, so gas positivity alone cannot give RH.

**Core.** [T] For a Dirichlet series with a(n) ≥ 0 and β in the half-plane of absolute convergence: φ_β(t) = f(β+it)/f(β) is a characteristic function (positive definite, Bochner) and log f is convex in β (Cauchy–Schwarz), i.e. heat capacity ≥ 0. With an Euler product, log f = Σ b(n)n^{−s}, b(n) = Λ(n)/log n ≥ 0 for ζ: compound Poisson, infinitely divisible (a free gas of independent modes). [N] β = 2, Toeplitz [φ(t_i − t_j)], h = 0.25, N = 120: ζ min eigenvalue 1.3e−10 (PSD), DH −7.78 (10 negative). Lévy coefficients b(n), n ≤ 2000: ζ 0 negative; DH 466 negative, 615 nonzero off prime powers ('interacting'); ζ(s)ζ(s+½) 0 negative; Epstein x²+5y² (a(n) = r(n)/2 ≥ 0) 40 negative. Real-axis stability: (log DH)″ < 0 for 1 < β < 4.23183 (negative heat capacity), > 0 beyond. [T] DH coefficients periodic mod 5: (1, κ, −κ, −1, 0), κ = 0.284079 (two-sector mix, TAA Lemma 158). Ghost test: every rung separates DH (DH-sensitive) but none forces RH: Epstein x²+5y² has positive weights and FE s ↔ 1−s and an off-line zero 0.93297 + 15.66825i (TAA Lemma 83/TAA Lemma 153); ζ(s)ζ(s+a) has an Euler product and is infinitely divisible, with zeros on Re s = ½ and ½ − a, off its own FE line Re s = (1−a)/2 [T]. Hurwitz ζ(s,a) (a ≠ ½, 1; positive weights) has zeros in 1 < σ < 1+ε (Davenport–Heilbronn 1936 / Cassels, via Wikipedia).

**Numbers.** ζ PSD (min eig 1.3e−10) vs DH −7.78 · Lévy negatives: ζ 0, DH 466, ζ(s)ζ(s+½) 0, Epstein 40 (n ≤ 2000) · (log DH)″ < 0 on (1, 4.23183)

**Also known as:** Bochner positivity of the KMS state; infinite divisibility of the zeta distribution; free gas = Euler product

**Axes:** sign/positivity (Ax2), ghost-sensitive, physics analogue, numerics/certificate

**TAA lemmas:** 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** DH-sensitive is not ghost-sensitive in general: Epstein (positive weights) and ζ(s)ζ(s+a) (Euler product) carry ghosts relative to their FE lines.

> ⚠ **Correction / caution.** All of this lives at Re s > 1; the zeros are at Re s ≤ 1.

**Relations (outgoing):**

- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — signed weights, not ID, negative C for β < 4.23
- fails for → [Epstein zeta no-go](#epstein) — positive weights but off-line zeros
- same mechanism as → [Bost–Connes KMS states](#kms-bost-connes) — KMS characteristic function
- analogue of → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) — DH-sensitive yet not RH-forcing
- lives in → [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state)

### #81 · 0.540 · Li criterion <a id="li-criterion"></a>

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

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (related to)

### #82 · 0.540 · Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q <a id="burgers-local-toeplitz"></a>

**Label:** Theorem · **id:** `burgers_local_toeplitz` · **quadrant:** RH-sharp

*In plain words:* The log-derivative side of the flow is a Burgers equation. At one prime its time-t positivity switches on exactly at the local Newman time. For products the primes couple at first order through a product of their log-derivatives.

**Core.** Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q

**Formula.** c_k(t) = (α_t^k + β_t^k)/p^{k/2} = 2T_k(λ_p e^{−t log²p}/2)

**Numbers.** (5,3): min eig −9.9e8, −1.9e3, −34 at Λ_p − 0.05, −0.005, −0.0005

**Axes:** sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- restates → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)
- refines → [Weil positivity criterion](#weil-positivity)
- feeds → [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term)

### #83 · 0.540 · de Branges spaces <a id="de-branges"></a>

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

### #84 · 0.540 · Hasse bound as a positive degree form <a id="hasse-pythagoras"></a>

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

### #85 · 0.540 · Suzuki’s de Branges line from the prime side <a id="suzuki-line"></a>

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

### #92 · 0.452 · Hodge index theorem <a id="hodge-index"></a>

**Label:** Theorem · **id:** `hodge_index` · **quadrant:** true but ghost-blind/untested

*In plain words:* On a surface the intersection form has exactly one positive direction (the ample class); everything orthogonal to it is negative. This sign is what proves RH for curves.

**Core.** NS(C×C) ⊗ ℝ has signature (1, ρ−1); U = ⟨f₁,f₂⟩ is the (1,1) part and its complement is negative definite. Over ℚ, Hodge-index form on V₀ ⇔ RH (TAA Lemma 91, restatement). Surface + ample + RR ⇒ Hodge index (D8). TAA Lemma 162: E×E Gram of {pt×E, E×pt, Δ, Γ_F}: det = a² − 4p; one positive eigenvalue ⇔ |a| ≤ 2√p; compact-group analogue: Haar positivity (Peter–Weyl).

**Formula.** sig NS = (1, ρ − 1); D·D ≤ 0 on h^⊥

**Numbers.** true E×E (1,3), fakes (2,2) (TAA Lemma 88)

**Also known as:** NS signature (1, ρ−1); Lorentzian Néron–Severi; Ax1

**Axes:** sign/positivity (Ax2), geometry over F_q, structure/frame (Ax1)

**TAA lemmas:** 14, 88, 91, 98, 140, 145, 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Effectivity and Hodge index are independent on both sides (TAA Lemma 94).

> ⚠ **Correction / caution.** Hodge index needs S2, S3, S5 too (TAA Lemma 145).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — D·D ≤ 0 on V₀ over ℚ (TAA Lemma 91)
- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst) — U^⊥ = physical quotient (TAA Lemma 115, TAA Lemma 146)
- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — complement of U
- analogue of → [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface)

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (same mechanism as); [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (special case of); [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) (lives in); [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) (implies); [Ax1–Ax3 axioms (Yoneda specification)](#ax123) (same mechanism as); [Parity argument: linear χ cannot see D²](#parity-linear-chi) (fails for); [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (same mechanism as); [Castelnuovo–Severi inequality](#castelnuovo-severi) (special case of); [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) (special case of); [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) (analogue of); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes](#ferromagnetic-sign-not-count) (fails for); [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) (analogue of); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) (refines); [Ruled quadric through a saddle: null lines, signature (1,1)](#ruled-quadric-null-lines) (instance of); [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) (analogue of); [Standard conjectures (Hodge type)](#standard-conj) (special case of)

### #93 · 0.452 · Osterwalder–Schrader reflection positivity <a id="os-reflection-positivity"></a>

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

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (analogue of); [Rosati positivity](#rosati) (analogue of); [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (analogue of); [Half Tate twist ℚ(½)](#half-tate-twist) (analogue of); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (analogue of); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of)

### #94 · 0.452 · Legendre strata: support function / Fenchel–Moreau as a definiteness detector <a id="legendre-support-function"></a>

**Label:** Theorem · **id:** `legendre_support_function` · **quadrant:** true but ghost-blind/untested

*In plain words:* All the information about a convex curve sits in the intercepts of its tangent lines; the Legendre transform returns the curve exactly when it is convex, so it is a definiteness test.

**Core.** Tangent lines carry a convex curve: the support function h(θ) = sup_{x∈K}⟨x,u_θ⟩ determines a closed convex K (Minkowski; BIB). For f = ½xᵀAx the Legendre transform is ½pᵀA⁻¹p, finite everywhere iff A ≻ 0; if A has a negative eigenvalue f* ≡ +∞ (on a box |x| ≤ R it grows with R: TAA Lemma 153 NUM). Fenchel–Moreau: f** = f iff f is convex lsc (BIB). Support-function window of a conic region: 2π for an ellipse; for one convex hyperbola branch exactly 2·atan√(|λ₋|/λ₊) < π (NUM 64.8° vs 64.62° predicted for λ = 1, −0.4); for both branches (or the region xᵀAx ≤ 1 with A indefinite) empty; jump 2π → 0 at det = 0. J. W. McGreevy's 'Legendre type concept' is this. TAA Lemma 159: thermodynamic potentials U, F, H, G are Legendre transforms of one generating function on one Legendrian surface; stability (convexity) is what makes the dictionary invertible.

**Formula.** h_K(u) = sup⟨x,u⟩; (½xᵀAx)* = ½pᵀA⁻¹p iff A ≻ 0

**Numbers.** hyperbola-branch window 2 atan√(|λ₋|/λ₊): 64.8° (grid) vs 64.62°

**Also known as:** support function; Fenchel–Moreau; y-intercepts of tangents

**Axes:** sign/positivity (Ax2), structure/frame (Ax1)

**TAA lemmas:** 153, 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) — ellipse ⇔ imaginary absolute ⇔ full window
- same mechanism as → [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) — window = conic type
- lives in → [Weil positivity criterion](#weil-positivity) — applied blockwise

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [Maxwell construction / convex effective potential](#maxwell-effective-potential) (same mechanism as); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (same mechanism as); [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) (special case of); [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) (same mechanism as); [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as)

### #96 · 0.452 · Weil operator C = i^{p−q} = Wick rotation <a id="weil-operator"></a>

**Label:** Theorem · **id:** `weil_operator` · **quadrant:** true but ghost-blind/untested

*In plain words:* Turning an indefinite pairing into a positive one by inserting a quarter turn — the same move as Wick rotation in physics.

**Core.** TAA Lemma 139: Q indefinite → Q(C·, ·̄) PD (Rosati); Abel–Jacobi = principalization. A complex structure is a μ₄ action (J² = −1). Obstruction: Pic^(Spec ℤ̄) ≅ ℝ has no complex structure.

**Formula.** C = i^{p−q}; Q(x, C ȳ) > 0

**Numbers.** y² = x³ − x: π/√p primitive 4th root of unity for p ≡ 3 mod 4 (TAA Lemma 140)

**Also known as:** Wick rotation; J² = −1; μ₄ action; complex structure

**Axes:** sign/positivity (Ax2), Spec ℤ gap, physics analogue

**TAA lemmas:** 139, 140, 102

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** The Fourier transform is the swap, not the Weil operator (TAA Lemma 140).

> ⚠ **Correction / caution.** Over F_q the sign is algebraic (Castelnuovo); the Hodge model is only an analogy there (TAA Lemma 139 caveat).

**Relations (outgoing):**

- same mechanism as → [Compatible complex structure J commuting with Frobenius](#compatible-j) — J = h(i)
- analogue of → [Principalization](#principalization) — Abel–Jacobi = principalization
- fails for → [Arakelov geometry](#arakelov) — no complex structure on Pic^ ≅ ℝ

**Relations (incoming):** [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (same mechanism as); [Compatible complex structure J commuting with Frobenius](#compatible-j) (same mechanism as); [Hodge–Riemann bilinear relations](#hodge-riemann) (same mechanism as); [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (analogue of); [Arakelov geometry](#arakelov) (fails for); [Principalization](#principalization) (analogue of)

### #97 · 0.452 · Hodge–Riemann bilinear relations <a id="hodge-riemann"></a>

**Label:** Theorem · **id:** `hodge_riemann` · **quadrant:** true but ghost-blind/untested

*In plain words:* Pairing a holomorphic form with its own complex conjugate gives a positive number: a genuine |amplitude|².

**Core.** HR holds on every compact Riemann surface; HR form = 2 × Petersson (TAA Lemma 134). Positivity = complex structure inserted (Weil operator C = i^{p−q}). Hecke self-adjointness gives a_p ∈ ℝ, not |a_p| ≤ 2√p.

**Formula.** i ∫ α ∧ ᾱ = 2∫|f|² > 0

**Also known as:** HR form; i∫α∧ᾱ > 0; Riemann form; Petersson positivity

**Axes:** sign/positivity (Ax2), geometry over F_q

**TAA lemmas:** 40, 102, 134, 139, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Column 2 (F_q) never fully inherited the HR sign; Castelnuovo replaces it algebraically (TAA Lemma 140).

**Relations (outgoing):**

- special case of → [Cup product / Poincaré duality pairing](#cup-product) — cup with the conjugate through the Hodge structure
- same mechanism as → [Rosati positivity](#rosati) — Rosati = H-adjoint (TAA Lemma 134)
- same mechanism as → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) — positivity needs C = i^{p−q}

**Relations (incoming):** [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (same mechanism as); [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (same mechanism as); [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (same mechanism as); [Hecke operators](#hecke) (same mechanism as); [Cusp forms & Petersson positivity](#cusp-forms-petersson) (same mechanism as)

### #103 · 0.452 · Cartan involution / compact unitary group <a id="cartan-involution"></a>

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

### #106 · 0.452 · Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r² <a id="selberg-eigenvalue-mass-shell"></a>

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

### #112 · 0.451 · Organizing split: ghost-blind = phase, ghost-sensitive = sign <a id="split-blind-sensitive"></a>

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

**Relations (incoming):** [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) (analogue of); [Must-fail-for-DH acceptance test](#dh-acceptance) (same mechanism as); [Kramers–Kronig relations](#kramers-kronig) (same mechanism as); [Half Tate twist ℚ(½)](#half-tate-twist) (lives in); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); ["Cocycles give structure, not sign"](#cocycle-principle) (same mechanism as)

### #113 · 0.451 · Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh <a id="gyroscopic-vs-definite-stability"></a>

**Label:** Heuristic · **id:** `gyroscopic_vs_definite_stability` · **quadrant:** sharp but interpretive

*In plain words:* A planet near periapsis is stable because its energy is a positive bowl. A Trojan at TAA Lemma 4 sits on a hilltop and is kept there only by the sideways Coriolis force, which does no work. That kind of stability breaks when two modes of opposite sign collide or when any friction is added. Weil's criterion says ζ's zeros would need the first, positive kind.

**Core.** [T] TAA Lemma 4 linearization λ⁴ + λ² + (27/4)μ(1−μ) = 0 (residual 9e−8); μ_R = (1 − √(23/27))/2 = 0.0385208965; μ = 0.04: ±0.0675 ± 0.7103i. Ω-Hessian positive definite (TAA Lemma 4 = max of −Ω); quadratic energy signature (2,2); Krein signs of the slow/fast modes −/+ (μ =,.038). Coriolis −2ω × v ⊥ v (zero power; skew block, no contribution to the gap form or energy). Linear damping −γv: max Re λ =.0018 (γ =.001),.018 (.01),.086 (.05) at μ =. Linearized motion epicyclic: long period √(27μ/4) libration + short ≈ 1 epicycle; tadpole/horseshoe are large-amplitude nonlinear (horseshoe encloses TAA Lemma 3, TAA Lemma 4, TAA Lemma 5; Dermott–Murray 1981). Kepler: a periapsis perturbation gives a nearby conic (orbital, not Lyapunov, stability: separation 0.012 → 0.150 over t ≤ 200; linear oscillator bounded). [C] Gascheau 1843 (via Sicardy 2010), Routh 1875 PLMS 6, 86–97; BKMR 1994 AIHP 11, 37–90. [R] Weil: RH ⇔ positivity → definite type; [A/H] FE/quartet symmetry = work-free J (ghost-blind, DH has it); DH ghosts ↔ quadruples past Routh; cycle 3: Weil Gram index 2 per resolved quartet.

**Numbers.** μ_R = 0.0385208965 · μ = 0.04: ±0.0675 ± 0.7103i · damped growth.018 at γ =

**Also known as:** Gascheau–Routh; Coriolis = J; dissipation-induced instability

**Axes:** sign/positivity (Ax2), physics analogue, ghost-sensitive

**TAA lemmas:** 161

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 0.7 · specificity 1.0 · tractability 0.5 · evidence 0.6 → priority 0.451

> ⚠ **Correction / caution.** Kepler apsides are not equilibria (TAA Lemma 161, correction 13).

> ⚠ **Correction / caution.** Tadpole/horseshoe are nonlinear; linear motion is epicyclic (TAA Lemma 161, correction 14).

> ⚠ **Correction / caution.** DH ↔ TAA Lemma 4 is Analogy; 27/4 has no arithmetic meaning claimed.

**Relations (outgoing):**

- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision) — Gascheau–Routh = Krein collision
- analogue of → [Weil positivity criterion](#weil-positivity) — definite energy
- analogue of → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — Hamiltonian–Hopf quadruple
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — J (FE) without definiteness
- lives in → [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form)

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (analogue of); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as); [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) (analogue of)

### #119 · 0.420 · Two conditions: primitive positivity and pole channel <a id="two-channel-missing-piece"></a>

**Label:** Restatement · **id:** `two_channel_missing_piece` · **quadrant:** RH-sharp

*In plain words:* On each finite section, Weil positivity splits into (a) positivity on the primitive part (functions whose Mellin transform vanishes at the two pole points), which is Castelnuovo-Severi / Hodge index on the primitive part and is where off-line zeros and finite-field fakes show up, and (b) positivity of the even and odd pole margins, which are exactly zero in the finite-field template, tend to zero generically, and are blind to off-line zeros. (a) and (b) on all sections is equivalent to RH. What is missing is a source for (a). In the finite-field model the pole channel is zero only once the graphs span the fibre classes; with an incomplete span a fake fails first in the pole channel, so the pole condition is not pure normalisation on finite sections.

**Core.** Two conditions: primitive positivity and pole channel

**Formula.** (a) W ⪰ 0 on ker P;  (b) ε = -1 - vᵀZ⁻¹v > 0, η = 1 - wᵀZ⁻¹w > 0;  1 - sup r = ε/(1+ε)

**Numbers.** eps_ell123 · eta_ell123 · ghost_beta_0p2_primitive · ghost_eps

**Axes:** sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 180, 181

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

**Relations (outgoing):**

- refines → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)
- refines → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (refines); [Davenport-Heilbronn window jumps](#davenport-heilbronn-window-jumps) (refines); [Which channel detects a fake depends on the span](#channel-depends-on-span) (refines); [Which channel an off-line zero breaks first over the rationals](#ghost-channel-order-over-q) (refines); [Genus seen at resolution sigma](#genus-at-resolution) (refines); [Castelnuovo-Severi defect as a Toeplitz block](#fq-cs-block-identity) (refines); [Null-line quotient (Gupta-Bleuler form)](#null-line-quotient) (refines); [Riemann-Roch sorts the two conditions](#riemann-roch-sorting) (refines); [Candidate formulations of Castelnuovo-Severi over the integers](#cs-for-spec-z-formulations) (refines)

### #128 · 0.420 · Two-point form g + iω ≥ 0 <a id="two-point"></a>

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

### #146 · 0.392 · Curvature as cup square: convexity ↔ Rosati positivity <a id="curvature-cup-square"></a>

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

### #147 · 0.392 · Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line <a id="clausius-gamma-reversibility"></a>

**Label:** Analogy · **id:** `clausius_gamma_reversibility` · **quadrant:** sharp but interpretive

*In plain words:* Reading the width Γ as entropy production gives nothing, because widths are never negative anyway; RH says every width is zero, i.e. the system is reversible. The positivity that does work is passivity: ζ absorbs everywhere to the right of the line, while a ghost shows up as gain.

**Core.** [C] Clausius ∮δQ/T_res ≤ 0, equality iff reversible; entropy production ≥ 0 (Wikipedia 'Clausius theorem', opened). [N] Carnot T_h = 2, T_c = 1: Σ Q/T = 0, efficiency 0.5; conduction Q = 1 from 2 to 1: entropy production 0.5. [A] Γ_ρ = 2|β − ½| ↔ entropy production: Γ ≥ 0 holds by definition, so this 'second law' is empty; RH is the EQUALITY Γ ≡ 0 ('every mode reversible'), matching TAA Lemma 118 (RH = undoubled system lossless). [N] TAA Lemma 156 certified: ζ 52 zeros t < 150 all Γ = 0; DH Γ = 0.617034, 0.301660, 0.148712, 0.448515 (t < 200), sum 1.516. [R] The precise positivity law is passivity (Lagarias/Hinkkanen): RH ⇔ Re ξ′/ξ > 0 on Re s > ½; each zero gives a Lorentzian of sign sgn(σ − β), so a ghost is GAIN (negative absorption) for ½ < σ < β — the opposite sign to 'ghost = dissipation'. [N] t ∈ [80,120], σ ∈ {.55}: ζ min 0.0467 > 0; DH min −15.08 at (0.75, 85.7), negative on [85.5,85.9] and [114.1,114.3] at σ =. [T] On the line ξ′/ξ(½+it) = −iΞ′/Ξ is purely reactive (lossless); Foster's monotone reactance dX/dt > 0 is the Laguerre inequality Ξ′² − ΞΞ″ > 0 (⇐ RH; ⇏ RH, TAA Lemma 116 locally invisible ghosts). [C] de Bruijn–Newman: the forward (dissipative) heat flow creates off-line pairs (TAA Lemma 158, correction 16) — here 'ghost = dissipation' is right. [O] An entropy-production functional built without zeros (R5) whose zero set is Γ ≡ 0: none known.

**Numbers.** ζ passivity min 0.0467; DH min −15.08 · DH Γ sum 1.516 (four pairs, t < 200) · Carnot Clausius sum 0; conduction σ = 0.5

**Also known as:** Clausius inequality; RH = reversible on every mode; Foster reactance

**Axes:** sign/positivity (Ax2), ghost-sensitive, physics analogue

**TAA lemmas:** 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 0.6 · specificity 1.0 · tractability 0.4 · evidence 0.5 → priority 0.392

> ⚠ **Correction / caution.** Γ ≥ 0 is automatic: no content (TAA Lemma 159, correction 12).

> ⚠ **Correction / caution.** In the passivity picture a ghost is gain, not dissipation; in the de Bruijn–Newman picture dissipation creates ghosts: say which (TAA Lemma 159, correction 12).

**Relations (outgoing):**

- same mechanism as → [Passivity (positive real part)](#passivity) — the working positivity law
- analogue of → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — Γ ↔ entropy production
- same mechanism as → [Gain lines (active media)](#gain-line) — ghost = gain
- analogue of → [de Bruijn–Newman constant Λ](#debruijn-newman) — forward heat creates ghosts
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — via passivity (Lagarias/Hinkkanen)

### #171 · 0.360 · Ghost count of the arithmetic side <a id="ghost-count-theorem"></a>

**Label:** Theorem · **id:** `ghost_count_theorem` · **quadrant:** RH-sharp

*In plain words:* Write Weil's form as W = Z + P, with P the rank-2 pole term of signature (1,1) and Z the archimedean-plus-primes side, and restrict to test functions supported in a window of length l. The number of negative squares of Z on the window is at most 1 + N+, where N+ is the number of distinct zeros off the critical line to the right, and for every finite N <= N+ it is at least 1 + N once the window is long enough. So the count increases to 1 + N+. In the combined ledger the pole pair at +-i/2 enters exactly like an off-line zero pair with multiplicity -1; its negative direction is the even (cosh) pole vector, i.e. the Perron mode.

**Core.** Ghost count of the arithmetic side

**Formula.** n_-(Z_l) <= n_-(W_l) + 1 <= 1 + N+;  n_-(Z_l) increases to 1 + N+ as l -> infinity

**Axes:** sign/positivity (Ax2), reference/pole/cusp, ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- refines → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [Davenport-Heilbronn window jumps](#davenport-heilbronn-window-jumps) (instance of); [Certified window for one off-line pair](#explicit-ghost-window) (refines); [Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector](#dedekind-qi-one-mode) (tests); [RH as a negative-square count (restatement)](#ghost-count-rh-restatement) (instance of)

### #175 · 0.360 · Negative index κ(𝒬) = N₊ (ghost count) <a id="kappa-index"></a>

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

### #178 · 0.360 · d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1) <a id="dolbeault-kahler-sign"></a>

**Label:** Theorem · **id:** `dolbeault_kahler_sign` · **quadrant:** RH-sharp

*In plain words:* The sign is minus a sum of squares, as an identity.

**Core.** d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1)

**Axes:** sign/positivity (Ax2), structure/frame (Ax1), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- supplies the sign for → [The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)](#edge-boundary-cycle)
- worked example of → [η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential](#eta-chain)

### #181 · 0.360 · Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians) <a id="shear-push-density"></a>

**Label:** Theorem · **id:** `shear_push_density` · **quadrant:** RH-sharp

*In plain words:* Zero margin is a theorem in density form; approach from below is RH. Margin has density 0 against dBN slack.

**Core.** Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians)

**Axes:** sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- quantifies → [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation)
- density form of → [Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel](#anisotropic-part-weil)

### #182 · 0.360 · Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear <a id="trace-shear-budget"></a>

**Label:** Theorem · **id:** `trace_shear_budget` · **quadrant:** RH-sharp

*In plain words:* Positivity means the isotropic part outweighs the shear; Hasse is that inequality for one Frobenius.

**Core.** Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear

**Formula.** λ = τ/2 ± √(((h11−h22)/2)² + h12²)

**Numbers.** 0/20000 mismatches

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

> ⚠ **Correction / caution.** The Hodge-index analogue holds up to a sign on the complement.

**Relations (outgoing):**

- refines → [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity)

**Relations (incoming):** [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance) (refines)

### #185 · 0.347 · Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind) <a id="oscillator-semigroup-contraction"></a>

**Label:** Cited · **id:** `oscillator_semigroup_contraction` · **quadrant:** true but ghost-blind/untested

*In plain words:* Positive Gaussian operators exist exactly on the stable (rotation) side; this is real but archimedean, so it cannot tell ζ from a fake.

**Core.** [C] Dereziński–Karczmarczyk arXiv:1701.07297 Prop. 10: a·Op(e^{−A}) (A ∈ Sym++(ℂ^{2d})) is Hermitian iff a ∈ ℝ, A real; positive iff a > 0 and A ∈ Sym_p(ℝ^{2d}) (σ(Aθ) ⊂ [−1,1]); following Howe. [T,N] d = 1: Op(e^{−λ(x²+p²)}) = r^N/(1+λ), r = (1−λ)/(1+λ): positive iff λ ≤ 1; normalized elements are contractions with generator −N (harmonic oscillator, the rotation side). The IHO quadratic x² − p² is indefinite, so its Gaussians are not in the positive cone. [T] dissipative A ⇒ Re⟨(λ−A)⁻¹x,x⟩ > 0 for Re λ > 0 (Carathéodory). [R] A contraction semigroup whose generator realizes {ρ − ½} would give Lagarias's Re ξ′/ξ > 0 and, with the functional equation, RH. [A] the oscillator semigroup itself has spectrum {−n}, unrelated to zeros: 'contraction ⇒ no gain lines' is an analogy for it.

**Numbers.** Mehler/Laguerre check ≤ 1e−31 (6 cases) · Carathéodory: min Re m = 0.0308 > 0 over 200 random dissipative 6×6

**Axes:** sign/positivity (Ax2), ghost-blind, physics analogue

**TAA lemmas:** 157

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.347

> ⚠ **Correction / caution.** Re A > 0 gives bounded operators, not positive ones (positive needs A real, Prop. 10).

> ⚠ **Correction / caution.** Contraction alone + FE would already force β = ½ if the zeros were its spectrum: the content is the realization, not the sign.

**Relations (outgoing):**

- analogue of → [Lagarias/Hinkkanen criterion](#lagarias) — Carathéodory ⇔ Herglotz
- analogue of → [Lax–Phillips scattering](#lax-phillips) — contraction semigroup
- lives in → [Metaplectic / Kubota cocycle](#metaplectic)
- analogue of → [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) — needs a zero-free realization

**Relations (incoming):** [Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy](#perelman-template-dbn) (contrasts with)

### #186 · 0.347 · Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ <a id="zero-count-two-form"></a>

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

### #196 · 0.325 · Toeplitz / Verblunsky coefficients <a id="toeplitz-verblunsky"></a>

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

**Relations (incoming):** [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (analogue of); [Li criterion](#li-criterion) (same mechanism as); [de Branges spaces](#de-branges) (same mechanism as)

### #208 · 0.325 · Spinor/Clifford route <a id="spinor-route"></a>

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

### #223 · 0.307 · Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree <a id="lps-hecke-on-s3"></a>

**Label:** Theorem · **id:** `lps_hecke_on_s3` · **quadrant:** true but ghost-blind/untested

*In plain words:* Multiplying by the p+1 quaternions of norm p is an averaging operator on the 3-sphere. The constant function is its one 'big' eigenvector, which is the ζ-type piece. Every other eigenvalue is at most 2√p, which is the Ramanujan bound and the compact, rotation-type piece.

**Core.** [N] X^{5,13} (2184, PGL bipartite) max nontrivial |λ| 4.2497 ≤ 4.4721; X^{13,17} (2448) 7.0902 ≤ 7.2111; X^{17,13} (1092) 7.8509 ≤ 8.2462; X^{5,17} (4896) 4.3089 ≤ 4.4721. Hecke T_p on SO(3) harmonics ℓ ≤ 15: max |λ| 4.2841 (p = 5), 7.0075 (p = 13). Primitive norm-p^k counts (p+1)p^{k−1} (k ≤ 3). [C] LPS Combinatorica 8 (1988) 261–277; CPAM 39 (1986) S149–S186 (bibliographic + reference list). [T] trivial rep ↔ Eisenstein/ζ (hyperbolic, poles side); cusp part ↔ compact, Ramanujan. DH has no Hecke eigen-system here (c(2)c(3) = −κ² ≠ c(6) = 1).

**Numbers.** X^{5,13}: 4.2497 ≤ 4.4721 · X^{13,17}: 7.0902 ≤ 7.2111 · S²: 4.2841 ≤ 4.4721 (p = 5)

**Also known as:** LPS Ramanujan graphs; Brandt/Hecke on the sphere; trivial vs Ramanujan spectrum

**Axes:** sign/positivity (Ax2), structure/frame (Ax1), numerics/certificate, ghost-blind

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** The 2√p bound uses Deligne (Weil conjectures) — it is input, not output.

> ⚠ **Correction / caution.** The trivial eigenvalue p+1 is ζ's frame; ζ's zeros are not eigenvalues here.

**Relations (outgoing):**

- lives in → [Hecke operators](#hecke)
- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) — compact quotient ⇒ unitary Hecke
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — not multiplicative
- lives in → [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift)

**Relations (incoming):** [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (analogue of); [Hecke operators](#hecke) (lives in); [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) (lives in); [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) (lives in)

### #233 · 0.307 · Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}]) <a id="cc21-archimedean-positivity"></a>

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

### #234 · 0.307 · Cusp forms & Petersson positivity <a id="cusp-forms-petersson"></a>

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

**Relations (incoming):** [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (same mechanism as); [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) (analogue of); [Weight ladder (modular weights)](#weight-ladder) (same mechanism as)

### #244 · 0.307 · Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has <a id="thermo-geometry-ruppeiner-contact"></a>

**Label:** Theorem · **id:** `thermo_geometry_ruppeiner_contact` · **quadrant:** true but ghost-blind/untested

*In plain words:* Thermodynamic stability gives a positive metric on the space of states, and the first law gives a contact structure. On a two-dimensional state space a compatible complex structure always exists, so the hard part of MP4, a J commuting with a flow, has no thermodynamic counterpart yet.

**Core.** [C] Ruppeiner g_R = −Hess S (positive by stability), Weinhold g_W = Hess U, ds_R² = ds_W²/T; flat for non-interacting systems; Lorentzian signature for negative heat capacity (Reissner–Nordström) (Wikipedia, opened). Mrugała 2000 (opened): thermodynamic phase space = (2n+1)-dim contact manifold, Legendre submanifolds = equilibrium states; contact ↔ first law, metric ↔ second law; his G = dp dx + θ⊗θ has signature (n+1, n) (TAA Lemma 116, correction 1). [T] On a 2-dim oriented state surface with metric g and area form ω = f·vol_g (f > 0), J := rotation by 90° in g satisfies J² = −1, g(J·,J·) = g, ω(·, J·) = f g: the triple always exists, so it carries no content here; MP4's content is commutation with a flow (TAA Lemma 157/TAA Lemma 158), and equilibrium thermodynamics has no flow. [N] ideal gas at (U,V) = (3,2): g_R = diag(1/6, 1/4), ω = 1/3 dU∧dV, J² + 1 = 1e−16, Ruppeiner curvature 0; ω = √(2/3)·vol_W identically (sympy); vdW (1, 0.2): curvature 0.2244 (interaction), J² + 1 = 2e−16. TAA Lemma 116: Euler (multiplicative) field ⇒ flat; χ₄ field curved: curvature measures non-multiplicativity, not zeros. Stability = convexity ⇔ Legendre transform finite/involutive (TAA Lemma 153 window; Fenchel–Moreau); non-convex ⇒ convex hull (Maxwell construction, BIB).

**Numbers.** ideal: K = 0, ω/vol_W = √(2/3) · vdW: K = 0.2244

**Also known as:** Ruppeiner metric; Weinhold metric; Gibbs–Hermann–Mrugała contact geometry; missing J

**Axes:** sign/positivity (Ax2), structure/frame (Ax1), ghost-blind, physics analogue

**TAA lemmas:** 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** In 2D the compatible J is free; do not count it as a missing piece (TAA Lemma 159, correction 13).

> ⚠ **Correction / caution.** Gibbs, Hermann, Weinhold and Ruppeiner primary papers not opened.

**Relations (outgoing):**

- analogue of → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — (ω, J, g) automatic in 2D
- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — stability ⇔ Legendre finite
- analogue of → [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) — positivity free, commutation is the content
- lives in → [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state)

### #305 · 0.267 · Φ is not in Newman's class 𝒫 (unconditional), so b₀ < ∞; the Lee–Yang property of Φ is RH <a id="newman-class-p-fails-for-phi"></a>

**Label:** Cited · **id:** `newman_class_P_fails_for_phi` · **quadrant:** true but ghost-blind/untested

*In plain words:* Newman's sufficient condition (an even potential growing like a polynomial) fails for Φ because Φ decays doubly exponentially. Lee–Yang for Φ is therefore not available from that theorem.

**Core.** Φ is not in Newman's class 𝒫 (unconditional), so b₀ < ∞; the Lee–Yang property of Φ is RH

**Numbers.** V/u⁴ = 253, 160, 247, 584 at u = 0.5, 1, 1.5, 2

**Axes:** sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- constrains → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #318 · 0.240 · RH as a negative-square count (restatement) <a id="ghost-count-rh-restatement"></a>

**Label:** Restatement · **id:** `ghost_count_rh_restatement` · **quadrant:** RH-sharp

*In plain words:* RH holds if and only if the arithmetic side has exactly one negative square on all long windows, equivalently its second min-max value is non-negative for every window. If RH fails anywhere, the count is at least two on all long windows. This is equivalent to RH and is circular as a route to it.

**Core.** RH as a negative-square count (restatement)

**Formula.** RH <=> n_-(Z_l) = 1 for all large l <=> lambda_2(Z_l) >= 0 for all l

**Axes:** sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- instance of → [Ghost count of the arithmetic side](#ghost-count-theorem)

**Relations (incoming):** [λ₂ is monotone under nested windows (Cauchy interlacing)](#lambda2-monotone-nested-windows) (refines); [Invariant maximal non-positive subspaces: exactly two](#pontryagin-exactly-two) (refines)

### #320 · 0.240 · Hodge index in push/shear language: D² = (D·ω)²/ω² + D°², Hodge index ⇔ D°² ≤ 0 (shear can only subtract); D°² = D₀² − ½(D·h − D·v)² <a id="hodge-index-shear-subtracts"></a>

**Label:** Restatement · **id:** `hodge_index_shear_subtracts` · **quadrant:** RH-sharp

*In plain words:* The ample direction pushes, everything orthogonal to it can only lower the self-intersection.

**Core.** Hodge index in push/shear language: D² = (D·ω)²/ω² + D°², Hodge index ⇔ D°² ≤ 0 (shear can only subtract); D°² = D₀² − ½(D·h − D·v)²

**Formula.** D² ≤ (D·ω)²/ω²

**Numbers.** fakes (5,5): max D°²/|D|² = 0.18 > 0

**Axes:** sign/positivity (Ax2), geometry over F_q, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

> ⚠ **Correction / caution.** ω = h + v; h alone has h² = 0.

**Relations (outgoing):**

- restates → [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity)

### #321 · 0.240 · Invariant maximal non-positive subspaces: exactly two <a id="pontryagin-exactly-two"></a>

**Label:** Restatement · **id:** `pontryagin_exactly_two` · **quadrant:** RH-sharp

*In plain words:* If the number of off-line zeros N+ is finite, the dilation group has exactly 2^(1+N+) invariant maximal non-positive subspaces in the spectral completion (one null line chosen in each hyperbolic plane). Under RH there are exactly two, the light-cone lines of the pole plane. RH is equivalent to there being exactly two; this restates RH and is circular as a route. Pontryagin-type theorems give existence only.

**Core.** Invariant maximal non-positive subspaces: exactly two

**Formula.** #invariant MNPS = 2^(1 + N+);  RH <=> exactly two

**Axes:** sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- refines → [RH as a negative-square count (restatement)](#ghost-count-rh-restatement)

## Axis: reference/pole/cusp <a id="axis-reference-pole-cusp"></a>

### #4 · 0.720 · ψ(x) − x (explicit formula, deviation from the pole) <a id="psi-minus-x"></a>

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

**Relations (incoming):** [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) (analogue of); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) (same mechanism as); [No étale H¹ for Spec ℤ](#no-etale-h1) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (same mechanism as); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (same mechanism as); [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of)

### #11 · 0.720 · Primitive part V₀ = U^⊥ <a id="primitive-part"></a>

**Label:** Theorem · **id:** `primitive_part` · **quadrant:** RH-sharp

*In plain words:* What is left after removing the reference plane; on it the form should be negative (curves: theorem; ℚ: RH).

**Core.** D° = D − d₁f₂ − d₂f₁; (D°)² = −Tr_{H¹}(α_Dα_D†) (TAA Lemma 133). Over ℚ V₀ = U^⊥ and D·D ≤ 0 on V₀ ⇔ RH (TAA Lemma 91). TAA Lemma 167: Weil-form analogue numerically: kerP (pole/cusp functionals) removes exactly ζ's one pole direction; DH index on kerP = full index (primitive failure).

**Formula.** (D°)² = −def(D) ≤ 0

**Numbers.** λ_max on ker P / λ_max = 1.19–6361 over spans ≤ 16; 1.2–4.4 for L ≥ 12

**Also known as:** V₀; primitive classes; D°

**Axes:** reference/pole/cusp, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 91, 125, 133, 142, 149, 167

**Scores (Heuristic):** gap significance 0.8 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.720

> ⚠ **Correction / caution.** A “−2Tr” formula holds only on the primitive part.

**Relations (outgoing):**

- lives in → [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) — complement
- same mechanism as → [BRST / Gupta–Bleuler physical quotient](#brst) — physical quotient
- lives in → [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer)

**Relations (incoming):** [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Relative Gram matrix G_rel](#relative-gram) (analogue of); [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) (lives in); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (fails for); [BRST / Gupta–Bleuler physical quotient](#brst) (same mechanism as); [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) (analogue of); [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) (same mechanism as)

### #40 · 0.579 · Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays) <a id="light-cone-u"></a>

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

### #75 · 0.540 · Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order) <a id="goldfeld-bsd"></a>

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

### #101 · 0.452 · Pole plane / Tate poles at s = 0, 1 <a id="pole-plane"></a>

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

**Relations (incoming):** [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) (same mechanism as); [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) (same mechanism as); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as)

### #153 · 0.377 · Displaced reference (subtracting the pole) <a id="displaced-reference"></a>

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

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (same mechanism as); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (analogue of); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (same mechanism as); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as); [Buoyancy / Archimedes principle](#archimedes) (analogue of)

### #193 · 0.325 · Pole of ζ at s = 1 (residue / 3/π) <a id="pole-s1"></a>

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

**Relations (incoming):** [Pole plane / Tate poles at s = 0, 1](#pole-plane) (same mechanism as); [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) (same mechanism as); [The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄)](#chi-minus-one-half-pole) (refines)

### #195 · 0.325 · √2 family <a id="sqrt2-family"></a>

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

**Relations (incoming):** [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as)

### #197 · 0.325 · Cusp ≠ archimedean place <a id="cusp-vs-infinity"></a>

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

### #202 · 0.325 · Closed geodesics on the modular surface <a id="closed-geodesics"></a>

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

### #203 · 0.325 · Density / volume reading <a id="density-volume"></a>

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

**Relations (incoming):** [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (analogue of)

### #206 · 0.325 · Selberg resonances <a id="selberg-resonances"></a>

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

### #221 · 0.307 · E₂ anomaly (E₂* = E₂ − 3/(πy)) <a id="e2-anomaly"></a>

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

**Relations (incoming):** [Displaced reference (subtracting the pole)](#displaced-reference) (same mechanism as); [Automorphy defect (TAA Lemma 144)](#automorphy-defect) (same mechanism as); [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) (same mechanism as); [Weight ladder (modular weights)](#weight-ladder) (same mechanism as); [E₂* as the derivative of the Kronecker limit (cusp-scattering footprint)](#kronecker-limit-e2star) (same mechanism as)

### #230 · 0.307 · Archimedean place and Γ_ℝ factor <a id="archimedean-place"></a>

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

### #232 · 0.307 · Mazur–Wiles main conjecture ("Euler characteristic = L-value") <a id="mazur-wiles"></a>

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

**Relations (incoming):** [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) (analogue of); [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (special case of); [Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy](#perelman-template-dbn) (analogy of); [Two different χ’s: Euler characteristic vs class-group character](#two-chis) (analogue of)

### #236 · 0.307 · Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k <a id="herbrand-ribet"></a>

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

### #238 · 0.307 · Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂) <a id="ramanujan-691"></a>

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

**Relations (incoming):** [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (implies); [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities) (refines)

### #274 · 0.267 · One cusp, three readings: orbifold, Tate curve, archimedean monodromy <a id="one-cusp-three-readings"></a>

**Label:** Theorem · **id:** `one_cusp_three_readings` · **quadrant:** true but ghost-blind/untested

*In plain words:* Closing the cone angle 2π/m of the triangle orbifolds S²(2,3,m) runs from the Platonic solids (m = 3,4,5, Euler characteristic 2/|G|) through the flat case m = 6 to the modular orbifold at m = ∞, whose cusp is a pseudosphere horn of area 2π with unipotent holonomy T = 1+N, N² = 0. Arithmetically the cusp of X(1) is the Tate-curve degeneration (multiplicative reduction, nonzero N). At good primes Frobenius is semisimple and elliptic of trace a_p/√p; the inert value a_p = 0 is the order-2 point i, and the Hasse edge is a scalar, not a unipotent element. At the archimedean place an operator N playing the role of the logarithm of monodromy exists for local factors (Consani). On the modular surface the Riemann zeros appear as scattering resonances at Re s = 1/4, outside self-adjoint control. A polarized (N, log-Frobenius) package on a global cohomology would give Weil positivity; this is conjectural and RH is not proved.

**Core.** One cusp, three readings: orbifold, Tate curve, archimedean monodromy

**Formula.** χ_orb(S²(2,3,m)) = 1/m − 1/6; tr = 2cos(π/m) → 2; T = [[1,1],[0,1]] = 1+N; φ(s)=Λ(2s−1)/Λ(2s), poles at s = ρ/2

**Numbers.** area of SL2(Z)⧵H = π/3 · horn area 2π = area of {y ≥ 1}/(z ↦ z+2π) · |φ(1/2+ir)| = 1 to 2e−21 · 32a1 over F_9: a = −6, Frobenius² scalar −3 · 11a1 at 11: split multiplicative, Kodaira I_5

**Axes:** reference/pole/cusp, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality)
- refines → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)
- refines → [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton)

**Relations (incoming):** [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids) (refines); [The critical-line wave: Hardy Z and the Riemann–Siegel phase](#hardy-z-critical-line-wave) (analogy of)

### #283 · 0.267 · The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight <a id="one-twentyfourth-identities"></a>

**Label:** Theorem · **id:** `one_twentyfourth_identities` · **quadrant:** true but ghost-blind/untested

*In plain words:* The 1/24 is real and global: 1/24 = −ζ(−1)/2, the exponent of q in η, and η²⁴ = Δ, of weight 12 = 24·½. It is ζ(2), an absolutely convergent Euler product, carried to s = −1 by the functional equation. But in the window model of Weil’s form the 1/24 enters only through the Γ-factor (the weight). Lowering the weight below 12 breaks positivity almost at once (a one-sided edge), but that edge is generic: 11a1, with weight 2 and no 1/24 in this sense, sits on the same kind of edge, even tighter. For ζ the 1/12 = B₂/2 enters only through Stirling’s 1/(12z) term, which is the same for every Γ-factor and identical for Davenport–Heilbronn, so it cannot tell a true zero from a planted ghost. Verdict: the 1/24 does not supply the positive metric on the primitive part.

**Core.** The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** 1/24 = −ζ(−1)/2, ζ(−1) = −B₂/2 = −1/12; η(τ) = q^(1/24)∏(1 − qⁿ), η²⁴ = Δ; Θ_Leech = E₁₂ − (65520/691)Δ = 1 + 196560q² + 16773120q³ + 398034000q⁴ + …; 24 = 2³·3 (von Staudt–Clausen primes of B₂)

**Numbers.** τ(1…6) = 1, −24, 252, −1472, 4830, −6048 (checked) · Θ_Leech coefficients checked exactly; the 0 at q¹ (no roots) fixes the coefficient of Δ · Δ, weight k = 12 + 2ε with angles fixed: raising k never broke positivity (to Δk ≈ 2.6); lowering breaks at Δk = −5.0e−3, −2.0e−3, −1.1e−3, −3.9e−4 for ℓ = 2, 3, 4, 6 · 11a1: same one-sided edge, Δk = −2.3e−3, −2.5e−4, −7.4e−5 at ℓ = 2, 4, 6; ζ’s λ₂ has an edge in the opposite direction (+ε fails at 0.065 / 0.0043 / 0.0022) · for ζ the archimedean term log π + Re ψ(¼ + ir/2) has constants γ, log π, log 2 only; ζ(−1) does not appear · Riemann–Siegel θ(T): the 1/(48T) term splits as B₂ part −1/(6T) plus +3/(16T) (checked at T = 10³…10⁵)

**Axes:** reference/pole/cusp, physics analogue, ghost-blind

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The weight edge is the zero margin seen along the archimedean axis (like the prime-weight slab along the prime axis); it is not a fingerprint of 1/24 [Numerical no-go].

> ⚠ **Correction / caution.** "1/24 supplies the positive metric on the primitive part" is not supported in the window model.

**Relations (outgoing):**

- refines → [η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential](#eta-chain)
- refines → [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691)
- tests → [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally)

**Relations (incoming):** [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy) (uses)

### #284 · 0.267 · Weight ladder (modular weights) <a id="weight-ladder"></a>

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

### #287 · 0.267 · η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential <a id="eta-chain"></a>

**Label:** Theorem · **id:** `eta_chain` · **quadrant:** true but ghost-blind/untested

*In plain words:* The arithmetic η for the Weil form is open.

**Core.** η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the TAA Lemma 179 equipotential

**Axes:** reference/pole/cusp, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- extends → [Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned](#serre-derivative-analogy)

**Relations (incoming):** [d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1)](#dolbeault-kahler-sign) (worked example of); [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities) (refines)

### #293 · 0.267 · W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ <a id="archimedean-weyl-kernel"></a>

**Label:** Theorem · **id:** `archimedean_weyl_kernel` · **quadrant:** true but ghost-blind/untested

*In plain words:* The archimedean 'curvature' is monotone but unsigned.

**Core.** W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ

**Axes:** reference/pole/cusp, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- feeds → [Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻](#talenti-template-test)
- analogous to → [Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned](#serre-derivative-analogy)

### #295 · 0.267 · The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄) <a id="chi-minus-one-half-pole"></a>

**Label:** Theorem · **id:** `chi_minus_one_half_pole` · **quadrant:** true but ghost-blind/untested

*In plain words:* Split the prime atoms by the character χ₄. The atoms with χ₄ = −1 equal one half of (odd-n ζ prime part − χ₄ prime part), an exact identity. They carry half of ψ(x)’s main term, i.e. half the pole, while the χ₄ part has no main term. On windows the cancellation is only approximate, because it comes from a main term (the prime number theorem in progressions), not from a symmetry.

**Core.** The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** atoms(χ₄ = −1) = ½(odd-n ζ prime part − χ₄ prime part) [Theorem, identity]; weights (1 + χ₄)Λ ≥ 0

**Numbers.** ratio of the χ = −1 atoms to ½P on the pole frame (v-direction, w-direction): ℓ = 2: 0.286, 2.908; ℓ = 3: 0.465, 1.897; ℓ = 4: 0.613, 1.520; ℓ = 6: 0.816, 1.178 — both tend to 1

**Axes:** reference/pole/cusp, structure/frame (Ax1), ghost-blind

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** An explanation, not a route: it carries no RH information.

**Relations (outgoing):**

- explains → [Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector](#dedekind-qi-one-mode)
- refines → [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1)

### #342 · 0.181 · Ramanujan's 691 as a degeneration of the pole line <a id="ramanujan-691-degeneration"></a>

**Label:** Analogy · **id:** `ramanujan_691_degeneration` · **quadrant:** background

*In plain words:* tau(n) = sigma_11(n) mod 691 follows from Ramanujan's identity 691 + 65520 sum sigma_11(n) x^n = 441 Q^3 + 250 R^2, since 691 divides the numerator of B_12 and zeta(-11) = 691/32760. Over the complex numbers the Eisenstein (pole) line is orthogonal to the cusp forms; mod 691 its constant term, half of zeta(-11), vanishes and the Eisenstein line collides with the cuspidal line (Mazur's Eisenstein line meeting Spec T). So 691 is where the null-line quotient breaks down integrally, not an instance of it. An exploratory test found no irregular-prime signature in the real Weil-form model, as expected: primes enter only through smooth weights log p / p^(k/2). In the p-adic Stickelberger form on (Z/p)^x the pole is the unique eigenvalue of valuation -1, and the radical mod p sits exactly at the k with p | B_k (checked for 182 primes 5..1097, 66 irregular). At 691 the k = 12 radical line is the weight-12 Eisenstein constant term up to a unit; a second line sits at k = 200. What degenerates is a weight-k Eisenstein line in the p-adic family, not the pole of zeta; positivity has no p-adic analogue, only non-degeneracy.

**Core.** Ramanujan's 691 as a degeneration of the pole line

**Formula.** G_12 = zeta(-11)/2 + sum sigma_11(n) q^n;  zeta(-11) = 691/32760;  tau = sigma_11 mod 691

**Numbers.** tau_sigma11_checked_n · irregular_test_p · radical_k_691

**Axes:** reference/pole/cusp, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.181

**Relations (outgoing):**

- analogy of → [Null-line quotient (Gupta-Bleuler form)](#null-line-quotient)

## Axis: geometry over F_q <a id="axis-geometry-over-f-q"></a>

### #6 · 0.720 · Frobenius-graph lattice on E×E (relative counts = intersections with Δ) <a id="frobenius-graph-lattice"></a>

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

**Relations (incoming):** [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (same mechanism as); [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) (lives in); [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) (analogue of); [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) (analogue of); [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (same mechanism as); [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) (lives in); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (analogue of)

### #53 · 0.540 · Krein collisions (how ghosts are born) <a id="krein-collision"></a>

**Label:** Theorem · **id:** `krein_collision` · **quadrant:** RH-sharp

*In plain words:* Zeros on the line carry a sign; two can only leave the line together if they meet with opposite signs.

**Core.** TAA Lemma 111: semisimple unit-spectrum F strongly stable ⇔ Krein form definite on each eigenspace; ghosts born only at opposite-sign collisions (710/710 births). For ζ the graphical Krein sign alternates ⇒ no protection; Λ ≥ 0 ⇒ ζ not heat-flow stable. TAA Lemma 160: KGL rule re-sourced (Gelfand–Lidskii MR0091390 record); 4×4 toy (ε = 0.2): opposite signs exit for |ω₁ − ω₂| < 0.2, same sign never; H_t collision (4,5) re-checked t* = −3.954792524 (diff 2.2e−9 from TAA Lemma 111); box count conserved, real count 2 → 0. TAA Lemma 161: Gascheau–Routh TAA Lemma 4 as the classical model: slow mode Krein −, fast +; collision at μ_R = 0.0385209; μ = 0.04 quadruple ±0.0675 ± 0.7103i; damping makes the pre-collision regime unstable too (BKMR 1994). TAA Lemma 163: sp(4,ℝ) normal form: equal-frequency oscillators coupled by ε leave the axis iff Krein signatures are opposite (band ≈ 2ε). TAA Lemma 165: realized arithmetically: every DH ghost with t ≤ 600 is born from a collision of two opposite-sign on-line crossings of the σ-pencil (signs 200/294 → 185/279).

**Numbers.** 300 paths: 710 births, all opposite-sign

**Also known as:** Krein sign; opposite-sign collision; strong stability

**Axes:** geometry over F_q, ghost-sensitive

**TAA lemmas:** 27, 41, 111, 120, 152, 153, 160, 161, 163, 165

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Krein = stability, not positivity; presupposes unit spectrum (TAA Lemma 111 circularity).

**Relations (outgoing):**

- analogue of → [de Bruijn–Newman constant Λ](#debruijn-newman) — heat-flow collisions
- same mechanism as → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) — pair leaves as (γ ± iδ)²
- same mechanism as → [Definite cup square / Krein one-liner](#definite-cup-square) — Krein one-liner (TAA Lemma 152 Prop 2.1)
- same mechanism as → [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) — hyperbolic block = off-line pair (claim 7, Restatement)
- lives in → [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy)
- same mechanism as → [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability)
- lives in → [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4)
- lives in → [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy)

**Relations (incoming):** [Definite cup square / Krein one-liner](#definite-cup-square) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [de Bruijn–Newman constant Λ](#debruijn-newman) (analogue of); [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (same mechanism as); [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) (same mechanism as); [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) (same mechanism as); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (analogue of); [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) (same mechanism as); [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4) (lives in); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of)

### #56 · 0.540 · Frobenius as a boost (rapidity ½ log q) <a id="frobenius-boost"></a>

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

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (same mechanism as); [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) (analogue of); [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) (analogue of); [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) (analogue of); [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) (same mechanism as); [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) (same mechanism as)

### #59 · 0.540 · Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse <a id="conic-type-at-infinity"></a>

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

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (same mechanism as); [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) (same mechanism as); [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (same mechanism as); [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) (same mechanism as); [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) (same mechanism as); [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) (same mechanism as)

### #66 · 0.540 · Fake Weil polynomials (finite ghosts) <a id="fake-weil-poly"></a>

**Label:** Theorem · **id:** `fake_weil_poly` · **quadrant:** RH-sharp

*In plain words:* Polynomials that look like curve zeta numerators (functional equation, integer counts) but have roots off the circle. They are the F_q test ghosts.

**Core.** Fakes pass FE, count positivity, mod-2 data and the Hecke lattice (1,2); they fail Hodge index on ⟨H,V,Δ,Γ_{Fⁿ}⟩ (n₊ ≥ 2) and Rosati. Mixed fake (T² − 6T + 7)(T² + 7) passes N ≤ 2, fails from N = 4 (TAA Lemma 137, TAA Lemma 141). TAA Lemma 166: on the primitive Gram, #positive eigenvalues = #σ-2-cycles of off-circle roots (real pair 1, quartet 2), checked on all stored fakes.

**Numbers.** T² − 5T + 5: |α| = 3.618 > √5 · g = 2, q = 11: 2935 count-positive ghosts (TAA Lemma 109)

**Also known as:** fakes; T² − 5T + 5; ghost a=25 q=101; quartet q=11

**Axes:** geometry over F_q, ghost-sensitive, numerics/certificate

**TAA lemmas:** 88, 94, 109, 137, 138, 141, 166

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Degenerate fakes (|α| ∈ {1, q}) cause pole-degenerate exceptions (TAA Lemma 92 C9).

**Relations (outgoing):**

- fails for → [Ax1–Ax3 axioms (Yoneda specification)](#ax123) — no positive † with ππ† = q
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — F_q analogue of DH

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (fails for); [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) (fails for); [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (fails for); [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) (same mechanism as); [Tate count / Picard number (ghost-blind)](#tate-count) (fails for); [Counts vs quadratic positivity](#count-positivity) (fails for)

### #87 · 0.540 · Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k) <a id="coupled-coil-hasse"></a>

**Label:** Theorem · **id:** `coupled_coil_hasse` · **quadrant:** RH-sharp

*In plain words:* The quadratic form m² − a mn + p n² is the energy of two coupled inductors. It is never negative exactly when the coupling coefficient is at most one, which is the Hasse bound. A perfect transformer (k = 1) is the cusp; k > 1 would need an active element.

**Core.** Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k)

**Formula.** k_p = |a_p|/(2√p) = |cos θ_p|; Λ_p = log k_p / log²p; min_u (f′² − f f″) = 4 log²p (1 − k_p) for f = 2cos(u log p) − a/√p

**Numbers.** 11a1, 37a1, p < 2000: all k < 1; max k 0.9737 (p = 1367) and 0.9880 (p = 953) · Laguerre identity checked to 7e−15

**Axes:** geometry over F_q, sign/positivity (Ax2), physics analogue, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- refines → [Passivity (positive real part)](#passivity)
- restates → [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep)

### #98 · 0.452 · Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts <a id="ff-counts-do-not-induce-sign"></a>

**Label:** Theorem · **id:** `ff_counts_do_not_induce_sign` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over a finite field, you can write down fake zeta functions whose point counts look perfectly healthy (all positive, with the right symmetry) but whose zeros are off the circle. So the counts alone do not force the sign; what does is the geometry of the surface C×C.

**Core.** [T] Gram of ⟨H, V, Γ₀..Γ_M⟩ from counts only (Γ_m·Γ_n = q^min N_|m−n|, N₀ = 2−2g; Hallouin–Perret arXiv 1409.2357 Lemma 3); primitive Gram −q^min Σα^|m−n| is −Toeplitz(Σ u^k), so #positive eigenvalues = #σ-2-cycles (real pair 1, quartet 2). [N] 15 point-counted curves (q, g) = (7,2), (11,2), (13,2), (7,3), (11,3): full inertia (1, 2g+1), primitive part NSD rank 2g (max eig ≤ 1e−13). Exact census g = 2, |a| ≤ 6q, |b| ≤ 20q (no hits on the border), a_d exact for d ≤ 40: off-circle FE integer polynomials with all a_d ≥ 0: 675 (q = 7), 2935 (q = 11; = TAA Lemma 109), 4961 (q = 13); on-circle 205/401/513. DH-like pencil (1−λ)P₁ + λP₂ of two genus-3 curves over F₁₁: off-circle for λ ∈ [0.233, 0.9725] (4 roots, 2 positive primitive eigenvalues); genus-2 pencils and (7,3) stay on the circle (sign kept although a_d non-integral). Consequence for MP4: 'Euler product' read as counting data is insufficient; the conjecture can only hold in a geometric reading (an object whose square carries Hodge index).

**Numbers.** count-positive off-circle (g = 2, d ≤ 40): 675 / 2935 / 4961 at q = 7 / 11 / 13 · (11,3) pencil off-circle on λ ∈ [0.233, 0.9725] · genuine curves: inertia (1, 2g+1), 15/15

**Also known as:** v5 direction 1; F_q test of the lead conjecture; count-positive fakes vs Hodge sign

**Axes:** geometry over F_q, sign/positivity (Ax2), numerics/certificate

**TAA lemmas:** 166

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** a_d ≥ 0 checked for d ≤ 40 only (exact integers).

> ⚠ **Correction / caution.** Not a refutation of the conjecture in Deninger’s conjectured cohomology: it rules out the reading “numerical Euler-product data ⇒ sign”.

> ⚠ **Correction / caution.** Framework (Gram of Frobenius graphs, geometric vs arithmetic facet) is Hallouin–Perret’s; TAA Lemma 109/TAA Lemma 137/TAA Lemma 141/TAA Lemma 152 had the count-positive ghosts.

**Relations (outgoing):**

- lives in → [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) — tests reading (c) over F_q
- same mechanism as → [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) — count-positive fakes fail the sign
- lives in → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice)
- special case of → [Hodge index theorem](#hodge-index) — sign = Hodge index on C×C
- analogue of → [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) — F_q pencil of two L-polynomials

**Relations (incoming):** [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) (analogue of); [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (lives in)

### #105 · 0.452 · Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick <a id="deligne-tensor-power"></a>

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

### #109 · 0.452 · Weight–monodromy conjecture (Deligne): status <a id="weight-monodromy"></a>

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

### #170 · 0.360 · Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞ <a id="acm-local-newman-constant"></a>

**Label:** Cited · **id:** `acm_local_newman_constant` · **quadrant:** RH-sharp

*In plain words:* Each prime has its own threshold time after which its two zeros are real. It is negative exactly when the Hasse bound holds. This is already known from work on function fields.

**Core.** Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞

**Formula.** Λ_p = log(|a|/2√p)/log²p; Rodgers–Tao units ×4; ACM units ×log²p

**Numbers.** (5,3) −0.1541 · (7,−4) −0.0739 · (11,6) −0.0174 · (5,5) fake +0.0431 · (11,7) fake +0.0094 · ζ local pair (a = p+1): log cosh(½ log p)/log²p, p = 2: 0.1226

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- feeds → [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep)
- restates → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset)

**Relations (incoming):** [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity) (feeds); [Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q](#burgers-local-toeplitz) (restates); [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp) (restates); [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term) (obstructs); [Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)](#local-dbn-slack) (restates); [One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction](#prime-clocks) (restates)

### #174 · 0.360 · Frobenius-graph Toeplitz form and its pole/count split <a id="frobenius-graph-toeplitz-split"></a>

**Label:** Theorem · **id:** `frobenius_graph_toeplitz_split` · **quadrant:** RH-sharp

*In plain words:* For the graphs of Frobenius powers, the defect between the m-th and n-th graph is q^min(m,n) times the trace t_|m-n|. After rescaling by q^(-n/2) the defect Gram matrix is Toeplitz (Hallouin-Perret 2019). It splits as a rank-2 pole term of signature (1,1) (the fibre classes) plus minus the Toeplitz matrix of normalised point counts, which is the finite-field shadow of Weil's form split as pole plus archimedean-and-primes. Checked by brute-force counts for an elliptic curve at three primes and for three genus-2 curves.

**Core.** Frobenius-graph Toeplitz form and its pole/count split

**Formula.** def(Γ_m,Γ_n) = q^{min(m,n)} t_{|m-n|};  W_q = Toeplitz(t_k q^{-k/2}) = P_q + Z_q,  Z_q = -Toeplitz(q^{-k/2} N_k)

**Numbers.** genus2_primitive_min · genus2_inertia_W · genus2_inertia_Z

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 181

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- instance of → [Castelnuovo-Severi and Weil's bound](#castelnuovo-severi-lemma)
- analogy of → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) (analogy of)

### #176 · 0.360 · Castelnuovo-Severi and Weil's bound <a id="castelnuovo-severi-lemma"></a>

**Label:** Cited · **id:** `castelnuovo_severi_lemma` · **quadrant:** RH-sharp

*In plain words:* On a product of two curves, the defect 2 d1 d2 - D^2 is non-negative for every divisor D (Castelnuovo-Severi). It follows from the Hodge index theorem applied to the primitive part of D, and Hodge index itself follows from Riemann-Roch on the surface plus the existence of an effective multiple. Applied to the diagonal and the graph of Frobenius it gives Weil's bound. Weil's own 1948 proof used Riemann-Roch on the curve only; Mattuck-Tate (1958) used Riemann-Roch on the product; Grothendieck (1958) reduced it to Hodge index.

**Core.** Castelnuovo-Severi and Weil's bound

**Formula.** def(D) = 2 d1 d2 - D^2 >= 0;  |N - q - 1| <= 2 g sqrt(q)

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 181

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- analogy of → [Candidate formulations of Castelnuovo-Severi over the integers](#cs-for-spec-z-formulations)

**Relations (incoming):** [Frobenius-graph Toeplitz form and its pole/count split](#frobenius-graph-toeplitz-split) (instance of)

### #179 · 0.360 · Castelnuovo-Severi defect as a Toeplitz block <a id="fq-cs-block-identity"></a>

**Label:** Theorem · **id:** `fq_cs_block_identity` · **quadrant:** RH-sharp

*In plain words:* For the graphs of Frobenius powers on a product of two copies of a curve over a finite field, the Castelnuovo-Severi defect between the n-th and m-th graph is q^min(m,n) times the trace t_|m-n|. After rescaling by q^(-n/2) the defect matrix is Toeplitz in t_k q^(-k/2); the term 2 d1 d2 becomes a rank-2 form of signature (1,1); and the remainder is minus the Toeplitz matrix of normalised point counts. So the counts being non-negative is exactly the off-diagonal sign pattern, and Hodge index is exactly one negative mode.

**Core.** Castelnuovo-Severi defect as a Toeplitz block

**Formula.** def(Γ_m,Γ_n) = q^{min(m,n)} t_{|m-n|};  W_q = Toeplitz(t_k q^{-k/2}) = P_q + Z_q,  P_q = x y^T + y x^T (x_n = q^{n/2}, y_n = q^{-n/2}),  Z_q = -Toeplitz(q^{-k/2} N_k), N_0 = 2-2g

**Numbers.** cases · genuine_inertia_W · genuine_inertia_Z · primitive_min · fake_primitive_min · pole_channel

**Axes:** geometry over F_q, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- analogy of → [One Perron mode against the pole](#pole-perron-one-mode)
- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

### #220 · 0.307 · Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity) <a id="gauss-sum-unitarity"></a>

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

### #241 · 0.307 · Tate count / Picard number (ghost-blind) <a id="tate-count"></a>

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

**Relations (incoming):** [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (analogue of); [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) (same mechanism as); [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) (analogue of)

### #246 · 0.307 · Primary sign rule for a_p of y² = x³ − x <a id="primary-sign-rule"></a>

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

### #261 · 0.267 · Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula <a id="gauss-half"></a>

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

**Relations (incoming):** [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) (same mechanism as)

### #268 · 0.267 · Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites <a id="sl2fp-half-representations"></a>

**Label:** Theorem · **id:** `sl2fp_half_representations` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over the field with p elements, SL(2) has exactly two pairs of 'half-size' representations, of dimensions (p+1)/2 and (p−1)/2, and their characters carry the square-root Gauss sum. This needs p to be prime. For hydrogen, (n ± 1)/2 appears for every n, so it does not single out primes.

**Core.** [N] p = 3, 5, 7, 11, 13: Σ dim² = p(p²−1); the unipotent class sum on Ind_B^G(Legendre) has eigenvalues giving χ(u) = (1 ± √(εp))/2 with multiplicity (p+1)/2 each; second orthogonality Σ|χ(u)|² = 2p. [C] Fulton–Harris §5.2 (table via Braun–Nebe, from Dornhoff Thm 38.1: ξ₁,₂(c) = ½(1 ± √(εq)), η₁,₂(c) = ½(−1 ± √(εq))). For composite n, SL(2,ℤ/n) = Π SL(2,ℤ/p^k) (CRT): reps are tensor products, no new n-halves. [T] Hydrogen (j,j), j = (n−1)/2, Casimir ((n−1)/2)((n+1)/2) for every n; odd n ⇔ integer j (parity, cf. hilbert_reciprocity_at_2). L is not 'the prime', A′ not ±1 (vectors, |j₊| = |j₋|). [H] per-prime, phase data ⇒ ghost-blind (DH shares the local quadratic characters).

**Formula.** χ(u) = (1 ± √(εp))/2, (−1 ± √(εp))/2; ε = (−1/p)

**Numbers.** Σ dim² = p(p²−1), p ≤ 13 · Σ|χ(u)|² = 2p

**Also known as:** half principal / half discrete series; Legendre-character split

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The (p+1)/2 reps are halves of a principal series, not cuspidal; the (p−1)/2 are halves of the discrete series.

> ⚠ **Correction / caution.** Ghost-blind: local quadratic data.

**Relations (outgoing):**

- same mechanism as → [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) — √(εp) Gauss sum
- analogue of → [Half-density normalization |x|^{½}](#half-density) — (p ± 1)/2
- lives in → [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) — PSL(2,F_q) quotients
- analogue of → [Half Tate twist ℚ(½)](#half-tate-twist)
- analogue of → [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) — integer vs half-integer j

**Relations (incoming):** [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) (analogue of)

### #271 · 0.267 · Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class) <a id="incommensurable-lehmer-zero"></a>

**Label:** Theorem · **id:** `incommensurable_lehmer_zero` · **quadrant:** true but ghost-blind/untested

*In plain words:* Zeros from different primes come arbitrarily close because the logarithms of primes are rationally independent, which is unique factorisation. Running the flow backward makes every such pair collide, so the product sits exactly at threshold 0, whatever the a_p are. This is a statement on the local unitarity line, not GRH.

**Core.** Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)

**Formula.** collision t_c ≈ −d²/8; F_{−s} = F + sF″ + O(s²)

**Numbers.** record pair d = 1.98792e−6 at z = 430949.266: t_c = −4.93978673e−13 = −d²/8 (ratio 1 + 7e−13) · (5,3)×(11,6) min gap 1.6e−3 (z < 100), 1.1e−4 (z < 10⁴), 3.7e−6 (z < 10⁵)

**Axes:** geometry over F_q, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 0.8 → priority 0.267

> ❓ **Not verified / open.** No exact reference found; the method is close to Csordas–Smith–Varga and Dobner (possibly folklore). Hasse-level, not GRH.

**Relations (outgoing):**

- mirror of → [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold)
- refines → [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term)

**Relations (incoming):** [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin) (feeds); [Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z²](#slack-ledger-cf) (refines); [Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)](#local-dbn-slack) (feeds)

### #277 · 0.267 · Split/inert duality for a CM curve (32a1) <a id="cm-split-inert-duality"></a>

**Label:** Theorem · **id:** `cm_split_inert_duality` · **quadrant:** true but ghost-blind/untested

*In plain words:* For y² = x³ − x one character, χ₄(p), decides both properties. Split primes have i ∈ Q_p, are ordinary, and have the angle of a Gaussian prime, equidistributed for the uniform measure (Hecke), not Sato–Tate. Inert primes have i ∉ Q_p, are supersingular (Deuring), and have a_p = 0 and angle exactly 90°; there Frobenius satisfies π² = −p and anticommutes with complex multiplication, so π/√p is a 90° rotation. The two classes are the fibres of the Galois character of Q(i), a duality rather than an isomorphism. The same holds for every CM curve, and RH for their L-functions is open.

**Core.** Split/inert duality for a CM curve (32a1)

**Formula.** χ₄(p)=+1: a_p = 2a, a²+b² = p, θ_p = arg(a+bi); χ₄(p)=−1: a_p = 0, π² = −p, π∘[i] = [−i]∘π; CM angle law ½δ_{π/2} + (1/2π)dθ

**Numbers.** p < 2·10⁴: 1125 split, 1136 inert; a_p = 0 exactly on the inert primes · split angles vs uniform: KS p = 0.96; vs Sato–Tate: KS p = 3e−30 · #E(F_{p²}) = (p+1)² for p = 3, 7, 11, 19, 23, 31, 43; anticommutation on all F_{p²}-points for p = 3, 7, 11 · π(x;4,3) ≥ π(x;4,1) for all p < 2·10⁴ (Chebyshev's bias); density ½ each is asymptotic

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** not an exact 50/50 split at finite height

> ⚠ **Correction / caution.** CM angles are uniform, not Sato–Tate

**Relations (outgoing):**

- refines → [CM case: the Hasse triangle is Fermat's two-squares triangle](#cm-gaussian-hasse-triangle)
- analogy of → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) (analogy of); [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings) (refines)

### #285 · 0.267 · CM case: the Hasse triangle is Fermat's two-squares triangle <a id="cm-gaussian-hasse-triangle"></a>

**Label:** Theorem · **id:** `cm_gaussian_hasse_triangle` · **quadrant:** true but ghost-blind/untested

*In plain words:* For y² = x³ − x (CM by Z[i]) the Hasse triangle at p ≡ 1 mod 4 has integer legs 2a, 2b with a² + b² = p, and its angle is the argument of a Gaussian prime; at p ≡ 3 mod 4, a_p = 0 and α_p/√p = ±i. All Frobenius elements lie in one field Q(i), so a coherent family of local i's exists, yet RH for this L-function is open: local coherence is not the missing piece.

**Core.** CM case: the Hasse triangle is Fermat's two-squares triangle

**Numbers.** checked for all p < 2·10⁴ (1136 primes ≡ 3 mod 4 with a_p = 0)

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- counterexample to sufficiency of → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality) (refines); [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton) (refines)

### #303 · 0.267 · Fourth roots: a_p = 0 (supersingular) gives r = 0 over 𝔽_p and the cusp r = 1 over 𝔽_{p²} (a_{p²} = −2p) <a id="fourth-roots-supersingular"></a>

**Label:** Theorem · **id:** `fourth_roots_supersingular` · **quadrant:** true but ghost-blind/untested

*In plain words:* At ±i the Frobenius pair has maximal slack; squaring moves it to the cusp.

**Core.** Fourth roots: a_p = 0 (supersingular) gives r = 0 over 𝔽_p and the cusp r = 1 over 𝔽_{p²} (a_{p²} = −2p)

**Axes:** geometry over F_q, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- illustrates → [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep)

### #315 · 0.240 · Hasse triangle and Newton's dT/dθ = L² <a id="hasse-triangle-newton"></a>

**Label:** Restatement · **id:** `hasse_triangle_newton` · **quadrant:** RH-sharp

*In plain words:* Write a_p = 2√p cos θ_p. The triangle with legs a_p and √(4p − a_p²) and hypotenuse 2√p exists exactly when the Hasse bound holds. In Newton's geometric calculus (T = tan θ) the derivative is dT/dθ = L² = 4p/a_p². This restates the bound; it does not determine θ_p, which is Sato–Tate distributed for non-CM curves. The blow-up at a_p = 0 is a chart singularity of tan, but the locus a_p = 0 (α_p = i√p, supersingular) is arithmetic.

**Core.** Hasse triangle and Newton's dT/dθ = L² Needham, Visual Complex Analysis (OUP 1997), Preface p. ix.

**Formula.** 2α_p = a_p + i√(4p − a_p²); T = √(4p−a_p²)/a_p, L = 2√p/|a_p|, dT/dθ = 1+T² = L² = 4p/a_p²; (2/π)sin²θ dθ = (2/π)T²(1+T²)^{-2} dT

**Numbers.** identity checked to 4e−16 for 11a1, 37a1, 32a1, p < 2·10⁴ · a_p = 0 below 2·10⁴: 23 primes (11a1), 13 (37a1) · Sato–Tate KS p-values 0.93 (11a1), 0.82 (37a1), 0.38 (τ, p < 3000) · τ(p) ≠ 0 for p < 3000; closest to a right angle at p = 2927 (|cos θ| = 4.9e−4)

**Axes:** geometry over F_q, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- refines → [CM case: the Hasse triangle is Fermat's two-squares triangle](#cm-gaussian-hasse-triangle)
- analogy of → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) (refines); [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings) (refines)

### #344 · 0.165 · Standard conjectures (Hodge type) <a id="standard-conj"></a>

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

## Axis: Spec ℤ gap <a id="axis-spec-gap"></a>

### #9 · 0.720 · Connes trace formula <a id="connes-trace"></a>

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

**Relations (incoming):** [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix) (restates); [Deninger’s foliated program](#deninger) (analogue of); [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) (analogue of); [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (same mechanism as); [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) (analogue of); [Bost–Connes KMS states](#kms-bost-connes) (analogue of); [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) (analogue of)

### #39 · 0.579 · Deninger’s foliated program <a id="deninger"></a>

**Label:** Cited · **id:** `deninger` · **quadrant:** true but ghost-blind/untested

*In plain words:* Deninger’s program: a foliated dynamical space whose leafwise cohomology carries the zeros; a positive Hodge star plus the flow would force Θ = ½ + (skew part).

**Core.** TAA Lemma 4: foliation-like (Deninger) structure carries the explicit formula with its signs; contact-like (Reeb) gives only the analytic shadow; on closed M, Reeb flows and Deninger systems are mutually exclusive. TAA Lemma 28: zeros = leafwise zero modes [analogy/conjectural]. TAA Lemma 50 Prop 7.1 (Den98): positive J commuting with Θ ⇒ Θ − ½ skew [RESTATEMENT]. TAA Lemma 93: Deninger D1–D5 stated exactly. TAA Lemma 141 §2: level S3 of the "surface" target. TAA Lemma 151 Conj 4.1 (OPEN): Deninger's conjectured cohomology stated as axioms MP0–MP4 (H⁰/H² = Tate boundary terms; H¹ with flow, spectrum = zeros; trace formula; cup product to ℝ(−1); definite cup square on primitive part = the sign). Naming rule: no coined name until constructed. Deninger 2007 (opened): 'the conjectured cohomology has not been constructed'. TAA Lemma 174: Livšic route audit — conformal ⇒ α = 0 on compact manifolds (Thm V; Deninger Rem. 2); explicit formula fixes only ε = +1 and |det A_p| = p (Thm I). Reference note: ICM 1998 paper: page range 163–186 (Documenta Extra Volume; 23–46 is a database numbering).

**Formula.** Θ = ½ + A, A skew

**Numbers.** TAA Lemma 157: Den98 p.169 re-opened: Hodge ∗ with tr(f ∪ ∗f′) positive definite, ∗Θ = Θ∗ ⇒ Θ = ½ + A, A skew ⇒ RH; in TAA Lemma 157 terms Θ† = ∗⁻¹Θ^∨∗ · TAA Lemma 158: Den05 p.18–19 (opened): foliated Hodge–Kähler theory (18)–(19), polarizable primitive H̄; 'I do not think that such a metric will exist … one will need the Kähler identities on cohomology' (for (11) Θ∗ = ∗(d−i+Θ))

**Also known as:** foliation

**Axes:** Spec ℤ gap, open target, physics analogue

**TAA lemmas:** 4, 28, 50, 93, 141, 151, 153, 157, 158, 174, 180

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.579

**Relations (outgoing):**

- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- analogue of → [Connes trace formula](#connes-trace) — foliation vs leaf space; J. W. McGreevy conjectures an isomorphism (Hodge–Lefschetz style)
- same mechanism as → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP0–MP4
- analogue of → [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) — archimedean Γ-factor proved (Consani 1998)
- lives in → [On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example)](#conformal-flow-needs-solenoid)

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (analogue of); [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) (analogue of); [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) (same mechanism as); [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) (analogue of); [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) (analogue of); [On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example)](#conformal-flow-needs-solenoid) (lives in); [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece) (refines); [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open) (refines); [Preserved-leaf contribution χ(L)/|e^{κt} − 1| (Álvarez López–Kordyukov–Leichtnam Thm 1.3.10) has the shape of the archimedean term](#deninger-preserved-leaf-term) (extends); [Half Tate twist ℚ(½)](#half-tate-twist) (analogue of); [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) (special case of); [Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow](#hopf-fibration-spec-z) (refines)

### #41 · 0.579 · Surface + ample + RR ⇒ Hodge index (D8) <a id="surface-ample-rr"></a>

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

### #44 · 0.579 · Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U) <a id="laurent-square"></a>

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

**Relations (incoming):** [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) (same mechanism as); [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) (same mechanism as)

### #46 · 0.579 · Parity argument: linear χ cannot see D² <a id="parity-linear-chi"></a>

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

### #48 · 0.579 · Tautology boundary (zero side vs prime side) <a id="tautology-boundary"></a>

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

### #49 · 0.579 · No étale H¹ for Spec ℤ <a id="no-etale-h1"></a>

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

### #99 · 0.452 · Connes–Consani sites <a id="connes-consani"></a>

**Label:** Cited · **id:** `connes_consani` · **quadrant:** true but ghost-blind/untested

*In plain words:* Topos-theoretic candidate for Spec ℤ × Spec ℤ.

**Core.** Arithmetic site and scaling site (CC14, CC16): a square exists, with Ψ_λ and s(f,f) = D•D (TAA Lemma 30), but no H¹, RR or Hodge index on it (TAA Lemma 65). TAA Lemma 147: their proved RRs are 1-dimensional; RR on the square is open (CC18).

**Numbers.** TAA Lemma 158: CC16 §6 (opened): ℤ_min ⊗_B ℤ_min, reduced square with Newton polygons, points over ℝ_max⁺ = product of points (Prop 6.11), Ψ(λ) congruences

**Also known as:** arithmetic site; scaling site

**Axes:** Spec ℤ gap

**TAA lemmas:** 30, 131, 140, 147, 158

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object)

**Relations (incoming):** [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (lives in); [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) (lives in); [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) (analogue of); [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) (same mechanism as); [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) (analogue of)

### #108 · 0.452 · Products grow linearly (2n), not quadratically <a id="products-linear"></a>

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

### #129 · 0.419 · Riemann hypothesis (target node) <a id="rh"></a>

**Label:** Open · **id:** `rh` · **quadrant:** true but ghost-blind/untested

*In plain words:* All nontrivial zeros of ζ have real part ½. In TAA every ghost-sensitive global sign statement for Spec ℤ turns out to be RH restated.

**Core.** RH is not proved in TAA. The positivity inventory of the programme finds that every ghost-sensitive global quadratic statement for Spec ℤ is a restatement of RH.

**Formula.** ρ = β + iγ, β = ½ for all ρ

**Also known as:** RH; Θ = ½

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 1, 107

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.419

> ⚠ **Correction / caution.** Every lemma PDF carries "RH NOT proved".

**Relations (incoming):** [Weil positivity criterion](#weil-positivity) (equivalent to RH); [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) (equivalent to RH); [Lagarias/Hinkkanen criterion](#lagarias) (equivalent to RH); [Connes trace formula](#connes-trace) (equivalent to RH); [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (equivalent to RH); [Passivity (positive real part)](#passivity) (equivalent to RH); [Relative Gram matrix G_rel](#relative-gram) (equivalent to RH); [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (equivalent to RH); [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) (equivalent to RH); [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) (equivalent to RH); [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) (equivalent to RH); [Rosati positivity](#rosati) (equivalent to RH); [de Bruijn–Newman constant Λ](#debruijn-newman) (equivalent to RH); [Compatible complex structure J commuting with Frobenius](#compatible-j) (equivalent to RH); [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) (equivalent to RH); [RH for curves over F_q (Weil)](#fq-curves) (analogue of); [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold) (equivalent to RH); [Decay rate ¼](#decay-quarter) (equivalent to RH); [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) (implies); [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh) (equivalent to RH); [Li criterion](#li-criterion) (equivalent to RH); [Suzuki’s de Branges line from the prime side](#suzuki-line) (equivalent to RH); [Bagchi recurrence](#bagchi) (equivalent to RH); [Hodge index theorem](#hodge-index) (equivalent to RH); [Cartan involution / compact unitary group](#cartan-involution) (fails for); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (analogue of); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (equivalent to RH); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (equivalent to RH); [Two-point form g + iω ≥ 0](#two-point) (equivalent to RH); [Hilbert–Pólya](#hilbert-polya) (implies); [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) (equivalent to RH); [Band criterion γ < 2T_M](#band-criterion) (fails for); [Hecke operators](#hecke) (fails for); [Cusp forms & Petersson positivity](#cusp-forms-petersson) (fails for); [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) (fails for)

### #131 · 0.419 · Arithmetic Castelnuovo object (C1–C4) <a id="castelnuovo-object"></a>

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

### #132 · 0.419 · No Riemann–Roch for C_ℚ × C_ℚ (the square is open) <a id="cc-square-open"></a>

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

**Relations (incoming):** [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) (same mechanism as); [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) (special case of); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (same mechanism as)

### #154 · 0.377 · Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing) <a id="formal-vs-geometric-lattice"></a>

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

### #156 · 0.377 · Preserved-leaf contribution χ(L)/|e^{κt} − 1| (Álvarez López–Kordyukov–Leichtnam Thm 1.3.10) has the shape of the archimedean term <a id="deninger-preserved-leaf-term"></a>

**Label:** Heuristic · **id:** `deninger_preserved_leaf_term` · **quadrant:** background

*In plain words:* In foliated Lefschetz formulas, a leaf preserved by the flow contributes a term that looks like the archimedean factor. Matching it with the pole push is an open test.

**Core.** Preserved-leaf contribution χ(L)/|e^{κt} − 1| (Álvarez López–Kordyukov–Leichtnam Thm 1.3.10) has the shape of the archimedean term

**Axes:** Spec ℤ gap, physics analogue, open target

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.7 · specificity 0.5 · tractability 0.5 · evidence 0.6 → priority 0.377

> ⚠ **Correction / caution.** Deninger Theorem 5: a conformal factor gives Re ρ = α/2 in the fixed-point-free model. Defining the flow by e^{tρ} is circular.

**Relations (outgoing):**

- extends → [Deninger’s foliated program](#deninger)

### #177 · 0.360 · Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology) <a id="deninger-derivation-positivity"></a>

**Label:** Cited · **id:** `deninger_derivation_positivity` · **quadrant:** RH-sharp

*In plain words:* The closest existing 'Leibniz plus a positive star' mechanism.

**Core.** Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology)

**Axes:** Spec ℤ gap, sign/positivity (Ax2), ghost-sensitive, open target

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.360

**Relations (outgoing):**

- candidate setting for → [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece)

**Relations (incoming):** [The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)](#edge-boundary-cycle) (heuristically points to)

### #184 · 0.347 · Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional) <a id="cc-riemann-roch"></a>

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

### #198 · 0.325 · F₁ base <a id="f1-base"></a>

**Label:** Cited · **id:** `f1_base` · **quadrant:** true but ghost-blind/untested

*In plain words:* The hoped-for "field with one element" under Spec ℤ. Over F₁ the single Frobenius trace becomes a sum over all zeros, and Connes–Consani take the sphere spectrum 𝕊 as F₁.

**Core.** TAA Lemma 65: a_p is the right model, but over F₁ the single trace becomes Σ_ρ u^ρ (one eigenvalue per zero, infinite genus, N(1) = −∞); for curves the CC dictionary is literal (u = qⁿ, α_i = q^{ρ_i}). CC10 N(u) positive on (1,∞) is prime-side and shared by Beurling systems ⇒ cannot force RH alone. TAA Lemma 147, correction 4: "On the metaphysics of F₁" proves no new RR; it restates CC23 and discusses 𝕊 as F₁.

**Formula.** N(u) = u − d/du(Σ_ρ order(ρ) u^{ρ+1}/(ρ+1)) + 1

**Also known as:** field with one element

**Axes:** Spec ℤ gap, open target

**TAA lemmas:** 65, 147, 158

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** CC N(u) is only formal (TAA Lemma 65 C1).

> ⚠ **Correction / caution.** TAA Lemma 158: Borger's square is the Witt space W*(Spec ℤ), not Spec ℤ (the collapse is Durov's).

**Relations (outgoing):**

- same mechanism as → [Spec ℤ is terminal](#spec-z-terminal)

**Relations (incoming):** [Spec ℤ is terminal](#spec-z-terminal) (same mechanism as); [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) (analogue of)

### #201 · 0.325 · Arakelov geometry <a id="arakelov"></a>

**Label:** Cited · **id:** `arakelov` · **quadrant:** true but ghost-blind/untested

*In plain words:* Compactified arithmetic surfaces.

**Core.** TAA Lemma 74: Ô(1)² = ½ for FS metrics; pole-plane Gram [[½,1],[1,0]] signature (1,1); Hodge index vacuous in genus 0. TAA Lemma 139: Pic^(Spec ℤ̄) ≅ ℝ has rank 1 and no complex structure. TAA Lemma 65/TAA Lemma 145: Faltings–Hriljac = Hodge index on arithmetic surfaces (curve × Spec O_K), relative part = Néron–Tate, not ζ. TAA Lemma 138 R5: Néron–Tate PD (37a1 ĥ = 0.051114). TAA Lemma 152: Faltings 1984 (Ann. Math. 119, 387–424), Hriljac 1985 (Amer. J. Math. 107, 23–38), bibliographic data verified: Hodge index on arithmetic surfaces ⇒ Néron–Tate positive definite; not RH for any L-function (TAA Lemma 152, correction 12).

**Numbers.** TAA Lemma 158: Moriwaki (opened) Thm B, d = 1 case = Faltings–Hriljac: deg(x·ĉ₁(H)^{d−1})-form ≤ 0 on classes with z(x)·H^{d−1} = 0, equality iff nx = f*(y); hypothesis d = dim f ≥ 1 excludes Spec ℤ itself (d = 0, CĤ¹ ≅ ℝ)

**Also known as:** Pic^; Faltings–Hriljac arithmetic Hodge index; Faltings–Hriljac (arithmetic Hodge index)

**Axes:** Spec ℤ gap

**TAA lemmas:** 65, 74, 138, 139, 145, 152, 158

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Faltings–Hriljac gives height positivity, not RH (TAA Lemma 152, correction 12).

**Relations (outgoing):**

- fails for → [Weil operator C = i^{p−q} = Wick rotation](#weil-operator)

**Relations (incoming):** [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) (fails for)

### #205 · 0.325 · Principalization <a id="principalization"></a>

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

### #207 · 0.325 · Spec ℤ is terminal <a id="spec-z-terminal"></a>

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

### #209 · 0.325 · Weil Rosetta stone <a id="weil-rosetta"></a>

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

### #211 · 0.325 · Cohesion (arena) <a id="cohesion"></a>

**Label:** Theorem · **id:** `cohesion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Cohesion is the arena, not the surface.

**Core.** TAA Lemma 141 §3: cohesion is the arena, not the surface; the étale ∞-topos of Spec ℤ is not cohesive (pro-shape, Hoyois); new Thm: [ℕ^×, Set] is not cohesive (Γ has no right adjoint). D10 (relative cohesion). TAA Lemma 146 §5: the cohesion quadruple Π ⊣ Disc ⊣ Γ ⊣ coDisc is a line without sign; RLGC is a 2×2 grid with mirror/KK/sign — numerology only.

**Also known as:** cohesive topos

**Axes:** Spec ℤ gap

**TAA lemmas:** 96, 141, 146

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Heaviside ≠ cohesion one-to-one.

### #231 · 0.307 · Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR) <a id="euler-char-chi"></a>

**Label:** Theorem · **id:** `euler_char_chi` · **quadrant:** true but ghost-blind/untested

*In plain words:* The χ in the Connes–Consani Riemann–Roch is an Euler characteristic: sections minus obstructions of a divisor D. It is a number attached to D, not a character of a Galois group.

**Core.** CC23 over 𝕊: χ(D) = dim H⁰(D) − dim H¹(D) = ⌈deg₂D⌉′ + 1 (TAA Lemma 147). TAA Lemma 145 parity: a linear χ is odd in D and never contains D²; the Hodge-index step needs a quadratic χ (D²/2 term). TAA Lemma 147: χ(D) + χ(−D) = 2 (deg₂D ∉ ℤ). TAA Lemma 160: χ-type vs h-type counts (invariant_vs_refined_count): χ conserved, h^i semicontinuous; for zeros, total count conserved, on-line count changes only at collisions.

**Formula.** χ(D) = dim H⁰(D) − dim H¹(D)

**Numbers.** χ(D) + χ(−D) = 2

**Also known as:** χ(D); Euler characteristic; RR χ

**Axes:** Spec ℤ gap, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 145, 147, 160

**Scores (Heuristic):** gap significance 0.5 (nearest gap: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Notation clash: this χ is an Euler characteristic, not the character χ (or ω) of the 691 class-group eigenspace.

**Relations (outgoing):**

- same mechanism as → [Parity argument: linear χ cannot see D²](#parity-linear-chi)
- same mechanism as → [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch)
- analogue of → [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) — both "χ = L-value"-type identities; analogy only

**Relations (incoming):** [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) (same mechanism as); [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) (analogue of); [Two different χ’s: Euler characteristic vs class-group character](#two-chis) (analogue of)

### #235 · 0.307 · What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ <a id="f1-square-constructions"></a>

**Label:** Cited · **id:** `f1_square_constructions` · **quadrant:** true but ghost-blind/untested

*In plain words:* Each 𝔽₁ theory either collapses the square back to Spec ℤ (Durov), replaces it by something huge (Borger's Witt space, Connes–Consani's tropical square), or skips it (Deninger). None yet carries a proved sign.

**Core.** [C, opened] Manin/Soulé: ask for Spec ℤ ×_{Spec 𝔽₁} Spec ℤ, motivated by C × C in Weil's proof (Soulé 2004 §1.2). Durov: forces Spec ℤ ×_{𝔽₁} Spec ℤ ≅ Spec ℤ, 'unsuitable to pursue Deninger's program' (López Peña–Lorscheid). Borger (Λ-rings): 𝔽₁-structure on flat X = commuting Frobenius lifts ψ_p; 'Spec Z ×_{Spec F1} Spec Z must be defined to be the Witt space W*(Spec Z)'; 'says nothing about the archimedean place'. Haran (abstract only): F-rings with an arithmetical surface Spec O_K × Spec O_K. Connes–Consani: square of the arithmetic site = topos N̂^{×2} with ℤ_min ⊗_B ℤ_min (reduced: Newton polygons), points over ℝ_max⁺ = product of points, Frobenius correspondences Ψ(λ) as congruences (CC16); H¹/RR on the square open (CC19); ℤ ⊗_𝕊 ℤ non-trivial over 𝕊-algebras (Connes essay). Deninger: no square; H¹ with flow. [T,N] Witt link: big Witt W_12(ℤ): F_nV_n = n (ghost), V_nF_n = V_n(1)·, projection formula V_n(x·F_n y) = V_n(x)·y, F₂F₃ = F₆, integrality — the pairing side (sign-free) of TAA Lemma 157's two Verschiebungs (Analogy).

**Numbers.** Witt checks: F_nV_n = n, projection formula, F₂F₃ = F₆, integrality (N = 12)

**Also known as:** Borger square = W*(Spec ℤ); arithmetic-site square; Durov collapse

**Axes:** Spec ℤ gap, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 158

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Witt 'ghost components' are unrelated to TAA ghosts (off-line zeros).

> ⚠ **Correction / caution.** Haran: abstract only, not opened.

> ⚠ **Correction / caution.** Earlier TAA record (lit/lemma30/verified_refs.md) called 'ℤ⊗_{𝔽₁}ℤ = ℤ' for Borger a deduction; Borger's own definition gives W*(Spec ℤ) (TAA Lemma 158, correction 8).

**Relations (outgoing):**

- analogue of → [F₁ base](#f1-base)
- same mechanism as → [Connes–Consani sites](#connes-consani) — arithmetic-site square
- same mechanism as → [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) — 𝕊-algebra square
- lives in → [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z)
- analogue of → [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) — Witt F/V: pairing side only

### #338 · 0.187 · The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5) <a id="missing-square-spec-z"></a>

**Label:** Open · **id:** `missing_square_spec_z` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over ℤ the product of Spec ℤ with itself collapses onto its diagonal, so the surface Weil used does not exist. Treating that absence as the object needs a defect invariant with a sign, built from the primes, that fails for fake zeta functions.

**Core.** [T] ℤ⊗_ℤℤ = ℤ, so Spec ℤ ×_{Spec ℤ} Spec ℤ = Spec ℤ and the diagonal is an isomorphism: no off-diagonal room for a Frobenius graph, no NS(C×C), no Castelnuovo sign. Over 𝔽_q: C ×_{𝔽_q} C is a surface, Γ_F·Δ = #C(𝔽_q), Hodge index ⇒ |α| = √q (Weil). ℤ is initial among rings, so any deeper base must leave rings (Borger, opened). [T] Any invariant that depends only on the collapse is an invariant of ℤ alone, hence the same for ζ, L(s,χ) and DH: ghost-blind. [O] J. W. McGreevy's reading made mathematics: a defect invariant δ with (R1) built from Euler-product data (primes/multiplicativity), (R2) ghost-sensitive (fails or changes sign for DH), (R3) a sign whose validity ⇒ RH, (R4) reducing over 𝔽_q to the Castelnuovo defect def(D) = 2d₁d₂ − D² ≥ 0, (R5) not defined through the zeros. 'Topological barrier' = Analogy until δ exists. Deninger's conjectured cohomology (MP0–MP4) is the hole stated on H¹ (Restatement). TAA Lemma 162: SU(2)×SU(2) on S³ and Moser's S²×S² are compact product models with automatic definiteness, but they carry elliptic-curve (rotation) frames; ζ's frames are boosts (Analogy; Open).

**Also known as:** Spec ℤ × Spec ℤ

**Axes:** Spec ℤ gap, sign/positivity (Ax2), structure/frame (Ax1), ghost-blind

**TAA lemmas:** 158, 162

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.2 · evidence 0.5 → priority 0.187

> ⚠ **Correction / caution.** The collapse is a property of ℤ only: it cannot by itself tell ζ from DH.

> ⚠ **Correction / caution.** 'Topological barrier' has no invariant yet: Analogy, not Theorem.

**Relations (outgoing):**

- same mechanism as → [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) — obstacle: collapse ℤ⊗ℤ = ℤ
- same mechanism as → [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) — the missing row
- same mechanism as → [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open)
- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi) — R4: defect over F_q
- analogue of → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — off-diagonal room over F_q
- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — Deninger moves the hole to H¹
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — collapse alone is ghost-blind
- analogue of → [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2)

**Relations (incoming):** [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) (analogue of); [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) (lives in); [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) (analogue of)

### #341 · 0.181 · Two different χ’s: Euler characteristic vs class-group character <a id="two-chis"></a>

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

## Axis: physics analogue <a id="axis-physics-analogue"></a>

### #23 · 0.600 · Passivity (positive real part) <a id="passivity"></a>

**Label:** Restatement · **id:** `passivity` · **quadrant:** RH-sharp

*In plain words:* A system that never produces energy; its impedance has non-negative real part. For ξ′/ξ this is Lagarias’ criterion.

**Core.** Passivity ⇔ Re ξ′/ξ > 0 on Re s > ½ ⇔ RH (Lagarias/Hinkkanen). Passivity ⇒ causality (TAA Lemma 146, correction 3). TAA Lemma 159: the working 'second law': each zero contributes a Lorentzian of sign sgn(σ−β), ghosts are gain for ½ < σ < β; [N] ζ min 0.0467 vs DH −15.08 on t ∈ [80,120]; on the line ξ′/ξ = −iΞ′/Ξ is purely reactive and Foster monotonicity = Laguerre inequality (⇐ RH, ⇏ RH).

**Formula.** Re ξ′/ξ(s) > 0 for Re s > ½

**Also known as:** Re Z ≥ 0; positive-real function

**Axes:** physics analogue, sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 17, 146, 159

**Scores (Heuristic):** gap significance 0.8 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Not independent of causality.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias)
- implies → [Kramers–Kronig relations](#kramers-kronig) — causal

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (same mechanism as); [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (same mechanism as); [de Branges spaces](#de-branges) (same mechanism as); [Suzuki’s de Branges line from the prime side](#suzuki-line) (same mechanism as); [Bagchi recurrence](#bagchi) (analogue of); [Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k)](#coupled-coil-hasse) (refines); [Gain lines (active media)](#gain-line) (fails for); [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) (instance of); [Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing](#passive-network-positive-real) (refines); [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) (same mechanism as); [Kramers–Kronig relations](#kramers-kronig) (same mechanism as); [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) (analogy of)

### #72 · 0.540 · Decay rate ¼ <a id="decay-quarter"></a>

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

### #80 · 0.540 · Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0 <a id="lee-yang-fisher-rh"></a>

**Label:** Cited · **id:** `lee_yang_fisher_rh` · **quadrant:** RH-sharp

*In plain words:* Lee and Yang proved that ferromagnets have their partition-function zeros on a circle. ζ's zeros are zeros in temperature (Fisher zeros), not in field; the exact Lee–Yang-type statement for ζ is the de Bruijn–Newman one, which is RH itself.

**Core.** [C] Lee–Yang (1952): ferromagnetic Ising, zeros in the fugacity z = e^{−2βh} on |z| = 1; Newman 1974 extension (Newman–Wu 2019 Thm 11, opened); Lee–Yang zeros (field) vs Fisher zeros (temperature) (Wikipedia 'Lee–Yang theory', opened). [N] 3-spin toy: ferromagnet J = 0.4 zeros |z| = 1, 1, 1; antiferromagnet J = −0.4: 13.79, 1.00, 0.0725. [T] Truncated Euler products have no zeros in any prime fugacity: ζ zeros are Fisher zeros of the Bost–Connes continuation, not Lee–Yang zeros (TAA Lemma 124). [C/R] Precise Lee–Yang form: Newman–Wu Thm 9 (de Bruijn 1950, Newman 1976): H_λ has only real zeros iff λ ≥ Λ; RH ⇔ Λ ≤ 0; Rodgers–Tao Λ ≥ 0; Polymath Λ ≤ 0.22. NW19: the 1976 result's 'original motivation was provided more by statistical physics and Euclidean field theory … than by analytic number theory'. e^{λt²} weighting = Gaussian (ferromagnetic-type) tilt; increasing λ = backward heat (TAA Lemma 158, correction 16). TAA Lemma 180: Newman 1976 (opened) proves the classification of the class 𝒫 and Φ ∉ 𝒫 unconditionally (so b₀ < ∞), and states RH as b₀ ≥ 0. It does not state 'RH ⇔ Φ Lee–Yang'; that follows from Newman 1974 via Lieb–Sokal 1981 (first pages opened). ζ zeros are Fisher-type (temperature) zeros of the Bost–Connes continuation at Re β = ½, beyond the transition at β = 1; finite truncations have zeros off the line.

**Numbers.** toy ferromagnet |z| = 1 (3/3); antiferromagnet 13.79, 1.00, 0.0725

**Also known as:** Lee–Yang theorem; Fisher zeros; Lee–Yang property of Φ

**Axes:** physics analogue, restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 159, 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** ζ zeros are Fisher, not Lee–Yang, zeros (TAA Lemma 159, correction 5).

> ⚠ **Correction / caution.** Lee–Yang 1952 originals not opened (via Newman–Wu, Wikipedia).

**Relations (outgoing):**

- same mechanism as → [de Bruijn–Newman constant Λ](#debruijn-newman)
- analogue of → [Bost–Connes KMS states](#kms-bost-connes) — Fisher zeros of the continuation
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Λ ≤ 0

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (refines); [The Laguerre inequality Ξ′² − ΞΞ″ > 0 holds for ζ on [0,60] and fails exactly around the off-line zero of the Davenport–Heilbronn function](#laguerre-detects-offline-zero) (tests)

### #88 · 0.532 · Gain lines (active media) <a id="gain-line"></a>

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

**Relations (incoming):** [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) (fails for); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (same mechanism as); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as); [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #95 · 0.452 · Lax–Phillips scattering <a id="lax-phillips"></a>

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

**Relations (incoming):** [Decay rate ¼](#decay-quarter) (special case of); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (same mechanism as); [Hilbert–Pólya](#hilbert-polya) (same mechanism as); [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) (analogue of); [Scattering unitarity |φ| = 1](#scattering-phi) (analogue of)

### #107 · 0.452 · Maxwell construction / convex effective potential <a id="maxwell-effective-potential"></a>

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

### #115 · 0.423 · BRST / Gupta–Bleuler physical quotient <a id="brst"></a>

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

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (same mechanism as); [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) (same mechanism as); [Hodge index theorem](#hodge-index) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy) (analogy of); [Gribov ambiguity](#gribov) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #120 · 0.420 · The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β)) <a id="arithmetic-equation-of-state"></a>

**Label:** Restatement · **id:** `arithmetic_equation_of_state` · **quadrant:** RH-sharp

*In plain words:* ζ is the partition function of a free gas of primes. Temperature, energy, entropy and heat capacity are exact; volume and pressure are not built in. With a cutoff at X the 'pressure' is a prime count whose smooth part comes from the pole and whose wiggles are the zeros.

**Core.** [T] Primon gas (Julia 1990, Spector 1990; Wikipedia 'Primon gas', opened): Fock basis |n⟩, H|n⟩ = log n|n⟩, Z(β) = Tr e^{−βH} = ζ(β), β > 1; Hagedorn divergence at β = 1 (density of states e^E). Bost–Connes (BC95 Thm 5, opened): unique KMS_β for 0 < β < 1 (type III₁), for β > 1 extreme KMS_β indexed by embeddings of ℚ^cycl (type I∞), normalization 1/ζ(β), T_c = 1, Gal(ℚ^cycl/ℚ) broken for β > 1. Sums over all occupation numbers at fugacity 1 = grand canonical, μ = 0: Ω = −T log ζ(β) = Σ_p T log(1 − p^{−β}) (independent modes). U = −ζ′/ζ(β), S = ∂(T log Z)/∂T = log ζ + βU, C = β²(log ζ)″ = β² Var(log n). [N] β = 2: log Z 0.497700, U 0.569961, S 1.637622, C 3.537927 (residual of S ≤ 2e−30); C(1.01) = 10200.8. [T/N] No volume: with mode cutoff p ≤ X, log Z_X(2) → log ζ(2) = 0.49770 (per mode 7.5e−7 at X = 10⁷: not extensive); log Z_X(1) = γ + log log X + o(1) (Mertens; 3.35717 vs 3.35716 at 10⁷). So 'Ω = −PV' is a name, not an identity. Time (KMS strip, BC95 §1): σ_t(μ_n) = n^{it}μ_n, Tr(e^{−βH}e^{itH}) = ζ(β − it); critical line = β = ½, inside the Hagedorn-divergent region where ζ is a continuation, not a trace. [Def + T] Energy-cutoff 'pressure' P_X(β) := Σ_{n≤X} Λ(n)n^{−β}/log n; smooth part Li_β(X) = ∫₂^X u^{−β}du/log u comes from the pole (displaced reference, TAA Lemma 146 buoyancy); fluctuation P_X − Li_β is the explicit-formula sum over zeros; RH ⇔ fluctuation O(X^{½−β+ε}) (von Koch type, Restatement). [N] β = ½: fluctuation 0.268, 0.292, 0.290, 0.246, 0.247 at X = 10³…10⁷. Earlier material: density = Hagedorn density of states; half density = β = ½ weights n^{−½} (TAA Lemma 145); mass shell β(1−β) = ¼ at β = ½ (TAA Lemma 150); buoyancy = pole subtraction (TAA Lemma 146) [Analogy for the names].

**Numbers.** β = 2: S = 1.637622, C = 3.537927 · log Z_X(1) − log log X → γ (3.35717 at 10⁷) · P_X(½) − Li_½(X) ≈ 0.25 (X = 10⁶, 10⁷)

**Also known as:** primon gas; Riemann gas

**Axes:** physics analogue, structure/frame (Ax1), restatement ⇔ RH

**TAA lemmas:** 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** 'Pressure × volume' is only the name of −Ω: the primon gas has no volume and is not extensive (TAA Lemma 159, correction 2).

> ⚠ **Correction / caution.** The critical line β = ½ is in the Hagedorn-divergent region; there Z is a continuation (TAA Lemma 159, correction 4).

> ⚠ **Correction / caution.** Every T,P,V,S object is a Legendre transform of one generating function: a dictionary is a change of variables unless a positivity law does work (TAA Lemma 159, correction 8).

**Relations (outgoing):**

- same mechanism as → [Bost–Connes KMS states](#kms-bost-connes)
- same mechanism as → [Displaced reference (subtracting the pole)](#displaced-reference) — Li_β(X) = pole part
- analogue of → [Buoyancy / Archimedes principle](#archimedes) — buoyancy = pole subtraction
- analogue of → [Half-density normalization |x|^{½}](#half-density) — β = ½
- analogue of → [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) — β(1−β) = ¼
- same mechanism as → [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) — fluctuation of P_X
- analogue of → [Density / volume reading](#density-volume) — volume options

**Relations (incoming):** [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) (lives in); [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) (lives in); [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) (lives in)

### #148 · 0.392 · Time delay (Wigner) <a id="time-delay"></a>

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

### #149 · 0.392 · Källén–Lehmann spectral positivity <a id="kallen-lehmann"></a>

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

### #212 · 0.324 · Kramers–Kronig relations <a id="kramers-kronig"></a>

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

**Relations (incoming):** [Passivity (positive real part)](#passivity) (implies); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) (same mechanism as); [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) (counterexample to sufficiency of); [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) (analogy of); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #213 · 0.324 · No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy) <a id="no-ghost-gupta-bleuler-analogy"></a>

**Label:** Analogy · **id:** `no_ghost_gupta_bleuler_analogy` · **quadrant:** background

*In plain words:* In string theory 24 transverse oscillators each contribute ½ζ(−1) = −1/24 to the vacuum energy, giving intercept a = 1; null spurious states decouple and the physical quotient has no negative-norm states (no ghosts), with one tachyon at level 0. On the arithmetic side, Weil’s window form has one negative square (the pole), the pole’s null line is quotiented out (Gupta–Bleuler), and the quotient is positive exactly when RH holds. The dictionary is good at the level of "a null line quotiented out of an index-1 space". It breaks at what forces the critical point: in the string an algebra (Virasoro, central charge 24) forces it; on our side nothing does.

**Core.** No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma). Goddard–Thorn 1972 and Brower 1972 are cited by name (not opened); the string-side statements are standard textbook content.

**Numbers.** indefinite Fock space ↔ Weil form Z_ℓ with one negative square [Analogy, good] · null spurious states decoupled ↔ pole null line e, quotient e^⊥/e [Analogy, good] · no ghosts ⇔ positive physical quotient ↔ W ≥ 0 on the primitive part ⇔ RH [Analogy; circular as a criterion] · one tachyon ↔ one Perron/pole mode for ζ; none for Δ (no pole); the Eisenstein part E₁₂ (L = ζ(s)ζ(s−11)) has poles [Analogy] · intercept a = 1 from 24·(1/24) ↔ the pole of ζ at s = 1: a coincidence [Heuristic] — the pole comes from the divergence of Σn^(−s) (Haar measure), not from a zero-point sum · critical dimension fixed by the central charge ↔ no analogue found [Open]

**Axes:** physics analogue, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.324

> ⚠ **Correction / caution.** The no-ghost theorem gives a ghost-free spectrum for a = 1 and D ≤ 26; it is not "unitary iff D = 26". D = 26 is the critical point where an extra family of null states decouples and light-cone Lorentz invariance closes.

**Relations (outgoing):**

- analogy of → [BRST / Gupta–Bleuler physical quotient](#brst)
- analogy of → [Null-line quotient (Gupta-Bleuler form)](#null-line-quotient)
- uses → [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities)

**Relations (incoming):** [Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24](#central-term-24-algebra-conjecture) (refines)

### #214 · 0.324 · Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity) <a id="ep-gap-across-collision"></a>

**Label:** Analogy · **id:** `ep_gap_across_collision` · **quadrant:** background

*In plain words:* TAA Lemma 157's gap between the two Verschiebungs is zero while a zero sits on the line and opens once a pair splits off. If you call that gap the difference between inertial and gravitational mass, RH says ζ obeys the equivalence principle, but only just.

**Core.** [T, TAA Lemma 157] ⟨(Θ^∨ − Θ†)v, v⟩ = 1 − 2β for an eigenvector with eigenvalue β + iγ. Along a dBN collision: 0 before (both real), 0 at the double zero, ±(1 − 2β) after, growing like (t* − t)^{1/2} by the fold law. [N] DH certified gaps 0.617034364913, 0.301660161219, 0.148712100902, 0.448515389254 (TAA Lemma 156/TAA Lemma 157). [A] 'inertial = gravitational' ↔ dual = adjoint. Flags: the EP is postulated in physics (renaming, not mechanism); the gap is computed from zeros (circular unless Θ† comes from an Euler-product metric, MP4 sharp).

**Numbers.** DH gaps 0.617, 0.302, 0.149, 0.449

**Also known as:** EP gap

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 160

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.324

> ⚠ **Correction / caution.** Postulated in physics: reading RH as the EP is a restatement (TAA Lemma 160, correction 8).

> ⚠ **Correction / caution.** No Lagrangian with these two masses exists.

**Relations (outgoing):**

- same mechanism as → [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap)
- analogue of → [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint)
- lives in → [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy)

### #215 · 0.324 · Gribov ambiguity <a id="gribov"></a>

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

### #218 · 0.307 · Bost–Connes KMS states <a id="kms-bost-connes"></a>

**Label:** Cited · **id:** `kms_bost_connes` · **quadrant:** true but ghost-blind/untested

*In plain words:* A quantum statistical system whose partition function is ζ(β); its positive KMS states and phase transition at β = 1 see ζ only at real β > 1, never the zeros.

**Core.** BC95 (Thm 5; CM08 3.32): Q-structure, Gal(Q^cycl/Q) symmetry, positive KMS states, ζ(β) real for β > 1; no trace equal to the Weil distribution found (TAA Lemma 30). TAA Lemma 38: strongest rigorous bridge; BC time is dual to rapidity, (β,t) = (Re s, −Im s); BC ordered phase ⇔ ω > ½. TAA Lemma 39: BC = tensor product over primes twisted by Galois. TAA Lemma 54/TAA Lemma 118: KMS/passivity uses ζ at real β > 1 ⇒ ghost-blind. TAA Lemma 162: the precise form of 'local boosts become global rotations' is KMS periodicity in imaginary time (Bisognano–Wichmann/Unruh); p^{−it} is the Bost–Connes time evolution; DH has no primon gas. TAA Lemma 164: B2 negative: KMS/Bochner positivity = non-negative multiplicities; Epstein Z_Q passes and has off-line zeros; BC's arithmetic = multiplicativity (Hecke algebra, Galois), i.e. the Euler product.

**Numbers.** TAA Lemma 159: BC95 Thm 5 re-read (lit/lemma31/bc95.txt): 0 < β < 1 unique KMS (III₁); β > 1 simplex over embeddings of ℚ^cycl (I∞), normalization 1/ζ(β), T_c = 1; §1 KMS strip F(t + iβ) and log Tr e^{−βH} = sup(S − βφ(H)) · TAA Lemma 159: φ_β(t) = ζ(β+it)/ζ(β) positive definite (Toeplitz min eig 1.3e−10 at β = 2); DH −7.78

**Also known as:** BC system

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 30, 38, 39, 54, 118, 159, 162, 164

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** BC95 Thm 5(a) states β < 1 (β ≤ 1 from CM08 3.32) (TAA Lemma 38 flag).

**Relations (outgoing):**

- analogue of → [Connes trace formula](#connes-trace)
- same mechanism as → [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms)
- lives in → [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity)

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (candidate setting for); [Epstein zeta no-go](#epstein) (fails for); [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) (lives in); [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) (same mechanism as); [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) (same mechanism as); [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh) (analogue of); [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (lives in); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (same mechanism as)

### #224 · 0.307 · Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect <a id="moser-orbit-space-s2xs2"></a>

**Label:** Theorem · **id:** `moser_orbit_space_s2xs2` · **quadrant:** true but ghost-blind/untested

*In plain words:* Each bound Kepler orbit of a given energy is labelled by two points, one on each of two spheres, so the space of orbits is a product of two spheres. Its intersection pattern has one positive and one negative direction, the same shape Weil used. A small push to a closed orbit only makes it precess slowly; an open orbit is just deflected once.

**Core.** [T] (1e−15, 200 random bound states) L·A′ = 0 ⇒ |j₊| = |j₋|; [C] Moser CPAM 23 (1970) 609–636 (regularization: Kepler flow at E < 0 ↔ geodesic flow on S³; oriented great circles of S³ = S²×S²). Exact Kepler: A conserved at every energy (no precession, no snapping back, TAA Lemma 162 correction to); E = 0 changes only the rescaling A′ = A/√(∓2E): so(4) vs so(3,1). [A] product surface with one positive and one negative direction, cf. Weil's C×C; Euler product ↔ hidden symmetry, DH κ-mix ↔ symmetry-breaking perturbation: precession (zeros move on the line) vs escape (Krein collision). [T] FE rigidity: in span{Λ(χ), Λ(χ̄)} the FE holds only for c = κ (one complex line), so an A4 test family must leave the span. Hydrogen level n = (j,j), j = (n−1)/2, Casimir (n²−1)/4: every n, no prime distinction.

**Numbers.** |j±| identity 1.3e−15 · FE residual: c = 0: 0.32, c = κ: 3e−17

**Also known as:** Moser regularization; Souriau; LRL precession vs scattering

**Axes:** physics analogue, sign/positivity (Ax2), structure/frame (Ax1), ghost-blind

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** In exact Kepler A does not precess at any energy.

> ⚠ **Correction / caution.** S²×S² ↔ Spec ℤ × Spec ℤ is Analogy.

**Relations (outgoing):**

- special case of → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) — orbit space of the SO(4) picture
- analogue of → [Hodge index theorem](#hodge-index) — signature (1,1)
- analogue of → [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) — product surface
- lives in → [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface)
- analogue of → [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) — precession vs escape

**Relations (incoming):** [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) (analogue of); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (lives in); [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) (analogue of)

### #225 · 0.307 · Nash–Kuiper flexibility / Onsager threshold <a id="nash-kuiper-onsager"></a>

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

### #281 · 0.267 · Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian <a id="johnson-lippmann-supercharge"></a>

**Label:** Cited · **id:** `johnson_lippmann_supercharge` · **quadrant:** true but ghost-blind/untested

*In plain words:* For the relativistic hydrogen atom there is a first-order operator, built from spin and the Coulomb direction, that commutes with the energy and anticommutes with Dirac's K. It plays the role of a supercharge: the hidden symmetry made one level more fundamental. Analogy only for RH.

**Core.** Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian Johnson–Lippmann, Phys. Rev. 78 (1950) 329(A); Khachidze–Khelashvili, arXiv:hep-th/0602181; Am. J. Phys. 74 (2006) 628.

**Formula.** A = Σ·r̂ − (i/(ma))K(Σ·p) + (i/(mr))Kγ⁵ = γ⁵α·r̂ − (i/(ma))Kγ⁵(H − βm); [A,H] = 0, {A,K} = 0

**Numbers.** checked symbolically on test spinors: |[A,H]ψ| ≤ 6e−15, |{A,K}ψ| ≤ 4e−15 · a Lorentz-scalar potential breaks it (residual 7.1) · a literal reading of a typeset variant with γ⁵ outside the bracket fails (residual 13.7) · hydrogen radial factorisation H_ℓ = A_ℓ†A_ℓ − 1/(2(ℓ+1)²) exact for ℓ = 0..3

**Axes:** physics analogue, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy)
- analogy of → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

**Relations (incoming):** [Multi-channel first-order factors are bounded by the SOS fit](#gram-factor-channel-bound) (analogy of); [Einstein–Cartan: spin enters as torsion](#einstein-cartan-torsion-spin) (analogy of)

### #294 · 0.267 · Beta integral, Maslov dequantization and entropy <a id="beta-dequantization-entropy"></a>

**Label:** Theorem · **id:** `beta_dequantization_entropy` · **quadrant:** true but ghost-blind/untested

*In plain words:* As hbar -> 0, hbar log B(a/hbar, b/hbar) tends to -(a+b) times the Shannon entropy of the split a:b, with an O(hbar log hbar) correction from Stirling. The integral collapses onto the saddle x* = a/(a+b) of a log x + b log(1-x), a max-plus problem, and the Beta(a/hbar, b/hbar) law satisfies a large-deviation principle with rate (a+b) KL(x*||x). With four points fixed, the Koba-Nielsen integral is the Beta function (Veneziano), and its high-energy fixed-angle limit is the same saddle. The Sato-Tate law is Beta(3/2,3/2), with constant pi/8 = Gamma(3/2)^2/Gamma(3). The CM split-prime law is Beta(1/2,1/2), with constant pi. This concerns the Gamma factors and the a_p distributions, not the zeros.

**Core.** Beta integral, Maslov dequantization and entropy

**Formula.** hbar log B(a/hbar, b/hbar) = a log(a/(a+b)) + b log(b/(a+b)) + (hbar/2) log hbar + hbar(log(2pi)/2 - log(ab/(a+b))/2) + O(hbar^2)

**Numbers.** a = 1, b = 2: limit -1.9095425 = -3 H(1/3) · residual after the Stirling terms 0.0972 hbar^2 · KS, p < 1e5: 11a1 vs Beta(3/2,3/2) 0.0050; 32a1 split vs Beta(1/2,1/2) 0.0078

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- instance of → [One log-gas and its frozen limit](#log-gas-frozen-limit)
- analogy of → [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids)

### #304 · 0.267 · Kepler: LRL vector closes so(4) = su(2) ⊕ su(2) for E < 0, so(3,1) for E > 0, e(3) at E = 0 <a id="kepler-so4-contraction"></a>

**Label:** Theorem · **id:** `kepler_so4_contraction` · **quadrant:** true but ghost-blind/untested

*In plain words:* The hidden symmetry of the hydrogen atom switches type with the sign of the energy, as the conic does.

**Core.** Kepler: LRL vector closes so(4) = su(2) ⊕ su(2) for E < 0, so(3,1) for E > 0, e(3) at E = 0

**Axes:** physics analogue, structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- illustrates → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy)

### #313 · 0.256 · J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge <a id="wedge-flip-animation"></a>

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

### #314 · 0.253 · Purity as distortionless transmission: weight strata = attenuation classes <a id="purity-distortionless"></a>

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

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (analogue of); [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) (same mechanism as); [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (analogue of); [Distortionless line R/L = G/C](#distortionless) (analogue of)

### #324 · 0.226 · Buoyancy / Archimedes principle <a id="archimedes"></a>

**Label:** Analogy · **id:** `archimedes` · **quadrant:** background

*In plain words:* Weight is measured relative to the fluid displaced; Castelnuovo–Severi and the pole subtraction can be read the same way.

**Core.** TAA Lemma 146 §7: C–S as D² = 2ab + D′² — Archimedes relative to U; the sign is an input (fluids), proved (curves), ⇔ RH (ζ). Buoyancy sign as input: TAA Lemma 146 corrections. TAA Lemma 159: in the arithmetic equation of state the pole part Li_β(X) of P_X(β) is the displaced reference; the fluctuation is the buoyancy-corrected part, governed by the zeros (Analogy).

**Also known as:** buoyancy; displaced fluid

**Axes:** physics analogue, reference/pole/cusp

**TAA lemmas:** 146, 159

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

> ⚠ **Correction / caution.** Analogy, not a mechanism.

**Relations (outgoing):**

- analogue of → [Castelnuovo–Severi inequality](#castelnuovo-severi)
- analogue of → [Displaced reference (subtracting the pole)](#displaced-reference)

**Relations (incoming):** [Castelnuovo–Severi inequality](#castelnuovo-severi) (analogue of); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (analogue of); [Displaced reference (subtracting the pole)](#displaced-reference) (analogue of); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #325 · 0.226 · Distortionless line R/L = G/C <a id="distortionless"></a>

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

### #326 · 0.226 · Heaviside RLGC line <a id="heaviside"></a>

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

### #327 · 0.226 · One log-gas and its frozen limit <a id="log-gas-frozen-limit"></a>

**Label:** Analogy · **id:** `log_gas_frozen_limit` · **quadrant:** background

*In plain words:* Under the de Bruijn-Newman backward heat flow, the zeros of H_t move by dz_k/dt = 2 sum_{j != k} 1/(z_k - z_j), the gradient flow of a logarithmic (Coulomb) energy. An off-line pair collides onto the real axis in finite time. RH is equivalent to Lambda = 0, i.e. every charge already on the axis at t = 0. The Hopf-Cole transform turns the heat equation into Hamilton-Jacobi in the hbar -> 0 limit, with a min-plus (Hopf-Lax) solution. Koba-Nielsen weights are 2D Coulomb-gas Boltzmann weights, and the Stieltjes equilibrium of charges in a Gaussian field sits at Hermite zeros, which the beta-Hermite ensemble freezes onto as beta grows. GUE pair correlation of zeros (conjectural) is the beta = 2 log-gas. The picture explains symmetry and statistics; it gives no positivity.

**Core.** One log-gas and its frozen limit

**Formula.** dz_k/dt = H''/H' = 2 sum_{j != k} 1/(z_k - z_j); S_t + S_x^2 = hbar S_xx -> S(x,t) = min_y [S_0(y) + (x-y)^2/(4t)]

**Numbers.** ODE vs exact roots 8e-11 · Hopf-Lax error 0.0027 at hbar = 1e-3 · Stieltjes n = 8 vs H_8 zeros 8e-8 · beta-Hermite rms ~ beta^-0.49

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- analogy of → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Beta integral, Maslov dequantization and entropy](#beta-dequantization-entropy) (instance of); [The factorial of one half and the Fourier quarter-turn](#fourier-quarter-turn) (instance of)

### #328 · 0.226 · Mass-density positivity <a id="mass-density"></a>

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

### #329 · 0.226 · Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned <a id="serre-derivative-analogy"></a>

**Label:** Analogy · **id:** `serre_derivative_analogy` · **quadrant:** background

*In plain words:* The open part is a signed curvature, the analogue of −E₄/12.

**Core.** Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned

**Axes:** physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- analogous to → [(τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²](#exactness-monge-ampere)

**Relations (incoming):** [η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential](#eta-chain) (extends); [W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ](#archimedean-weyl-kernel) (analogous to)

### #330 · 0.226 · Einstein–Cartan: spin enters as torsion <a id="einstein-cartan-torsion-spin"></a>

**Label:** Analogy · **id:** `einstein_cartan_torsion_spin` · **quadrant:** background

*In plain words:* In Einstein–Cartan theory the spin of matter couples to the torsion of a metric-compatible connection; torsion is algebraic (fixed pointwise by spin) and gives only a weak contact interaction. In the Lichnerowicz formula for a Dirac operator with skew torsion H the torsion enters as s·dH − 2s²‖H‖², which works against positivity. So 'a first-order operator whose square is the push, with spin entering through torsion' has no forced helpful sign for the torsion part.

**Core.** Einstein–Cartan: spin enters as torsion Hehl–von der Heyde–Kerlick–Nester, Rev. Mod. Phys. 48 (1976) 393; Cartan, C. R. Acad. Sci. Paris 174 (1922) 593–595; Kibble, J. Math. Phys. 2 (1961) 212–221; Sciama, Recent Developments in General Relativity (1962) 415–439; Bismut, Math. Ann. 284 (1989) 681–699; Ferreira, Proc. Edinburgh Math. Soc. 56 (2013) 501–508, Thm. 2.1.

**Formula.** (D^{s/3})² = Δ^s + F^W + κ/4 + s dH − 2s²‖H‖², ∇^s = ∇^g + 2sH; H = 0 gives D² = ∇*∇ + κ/4

**Axes:** physics analogue, sign/positivity (Ax2)

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- analogy of → [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge)

**Relations (incoming):** [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open) (analogy of)

### #331 · 0.226 · Einstein–de Haas lesson: the molecular-current model gave g ≈ 1, the true carrier was spin (g = 2); the missing piece may be a spin-like degree of freedom, not an orbit <a id="einstein-de-haas-lesson"></a>

**Label:** Analogy · **id:** `einstein_de_haas_lesson` · **quadrant:** background

*In plain words:* The first explanation of magnetism used circulating currents; the right one needed spin.

**Core.** Einstein–de Haas lesson: the molecular-current model gave g ≈ 1, the true carrier was spin (g = 2); the missing piece may be a spin-like degree of freedom, not an orbit

**Axes:** physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

> ⚠ **Correction / caution.** Original 1915 papers not opened.

**Relations (outgoing):**

- heuristically points to → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #332 · 0.226 · Viscosity multiplies trace-free strain; dissipation 2μ|S°|² ≥ 0 is the analogue of the missing sign; baroclinic wedge ↔ Gram tilt cos θ = r, net = p sin²θ <a id="viscosity-baroclinic"></a>

**Label:** Analogy · **id:** `viscosity_baroclinic` · **quadrant:** background

*In plain words:* Hasse makes the tilt a real angle.

**Core.** Viscosity multiplies trace-free strain; dissipation 2μ|S°|² ≥ 0 is the analogue of the missing sign; baroclinic wedge ↔ Gram tilt cos θ = r, net = p sin²θ

**Axes:** physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.226

**Relations (outgoing):**

- illustrates → [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation)

### #335 · 0.212 · Higgs mechanism: negative mass² at the symmetric point <a id="higgs-negative-mass2"></a>

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

**Relations (incoming):** [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (analogue of); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (analogue of)

### #336 · 0.212 · Klein–Gordon indefinite charge <a id="klein-gordon-charge"></a>

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

### #337 · 0.212 · Anomalous dispersion <a id="anomalous-dispersion"></a>

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

### #339 · 0.181 · Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks <a id="buoyancy-reading"></a>

**Label:** Analogy · **id:** `buoyancy_reading` · **quadrant:** background

*In plain words:* A picture, not a proof: the cusp is neutral buoyancy, not half submerged.

**Core.** Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks

**Axes:** physics analogue, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.181

**Relations (outgoing):**

- illustrates → [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance)

**Relations (incoming):** [Elliptic/parabolic/hyperbolic as |tr M| = 2r < = > 2 for normalised Frobenius; only SO(2) compact; in RP² the parabola is tangent to the line at infinity (zero-margin edge as tangency); r = 1 forces scalar Frobenius for elliptic curves](#conic-compactness) (refines); [so(4)=su(2)⊕su(2): Λ± are commuting rotation subalgebras; D·D=‖D⁺‖²−‖D⁻‖²](#so4-chirality-split) (corrects); [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation) (extends)

### #340 · 0.181 · Lamb cutoff <a id="lamb-cutoff"></a>

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

### #345 · 0.165 · Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance <a id="thermodynamic-j-direction"></a>

**Label:** Open · **id:** `thermodynamic_J_direction` · **quadrant:** true but ghost-blind/untested

*In plain words:* Thermodynamics supplies the antisymmetric half (area) for free; the positive half needs extra structure that the free prime gas does not have.

**Core.** Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance

**Formula.** dT∧dS = dP∧dV; J(dP)=dT ⇔ U_SS+U_VV=0; (log ζ)″ = Σ_p log²p p^{−β}/(1−p^{−β})²

**Numbers.** Var(log n)|β=2 = 0.884481834

**Axes:** physics analogue, open target, Spec ℤ gap

**TAA lemmas:** 180, 102

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.2 · evidence 0.5 → priority 0.165

> ⚠ **Correction / caution.** Ruppeiner, Rev. Mod. Phys. 67 (1995), abstract opened; a one-parameter primon gas has no Ruppeiner curvature.

**Relations (outgoing):**

- feeds → [On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH](#chirality-star-gamma5-hodge-index)
- feeds → [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate)

## Axis: restatement ⇔ RH <a id="axis-restatement-rh"></a>

### #28 · 0.600 · Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows <a id="zero-side-real-form-krein"></a>

**Label:** Restatement · **id:** `zero_side_real_form_krein` · **quadrant:** RH-sharp

*In plain words:* On the side of the zeros, asking whether ζ's hidden symmetry is the compact (rotation) form is the same as asking whether all zeros are on the line. DH visibly fails it; ζ passes every tested window, but that is a readout, not a proof.

**Core.** [T given MP0–MP3] Krein lemma ⇒ on-line lines h-definite, σ-2-cycles hyperbolic planes (1,1); flow unbounded on off-line pairs. [N] finite explicit formulas: inertia (6+2m, 2m), m = 0..3 (60 digits). [C] Katz–Sarnak Bull. AMS 36 (1999) 1–26: over F_q normalized Frobenius in USp(2g) (Weil). [N] spacing statistics: ζ GUE-consistent (KS.024, 20000 zeros), DH on-line rejected at 5% (KS.121 >.063): readouts of the zeros (fail R5). Answer to B1: compact real form for ζ = RH restated.

**Numbers.** inertia (6+2m, 2m), m ≤ 3 · DH q ≤ 24 (h =.025) · KS GUE: ζ.024 (20000), DH.121 (464)

**Also known as:** which real form is ζ's G×G (B1); U(p,q) of the Krein form

**Axes:** restatement ⇔ RH, ghost-sensitive, sign/positivity (Ax2)

**TAA lemmas:** 163

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.600

> ⚠ **Correction / caution.** Circular: compactness on the zero side is RH.

> ⚠ **Correction / caution.** GUE statistics are computed from the zeros (fail R5).

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh)
- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision)
- analogue of → [Rosati positivity](#rosati) — USp(2g) over F_q
- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1)

**Relations (incoming):** [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (analogue of); [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (same mechanism as)

### #71 · 0.540 · Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set <a id="dbn-parabolic-threshold"></a>

**Label:** Theorem · **id:** `dbn_parabolic_threshold` · **quadrant:** RH-sharp

*In plain words:* Under RH the heat-flow family sits exactly at the point where lowering the time would push zeros off the line. Since ζ's known zeros are all simple, the first collisions would happen farther and farther up, so ζ is at the edge only at infinity.

**Core.** [C] Newman 1976: −∞ < Λ ≤ ½, zeros of H_t all real ⇔ t ≥ Λ; de Bruijn 1950: real for t ≥ ½; Rodgers–Tao (Forum Math. Pi 8 (2020) e6) Thm 1: Λ ≥ 0; Polymath 15 Thm 1.1: Λ ≤ 0.22; CSV 1994 Cor. 1: for t > Λ zeros real and simple. [R] RH ⇔ Λ = 0. Direction: ∂_t H_t = −∂_zz H_t (RT: backwards heat); increasing t makes zeros real; collisions come from LOWERING t (TAA Lemma 158, correction 16, TAA Lemma 160, correction 6). [T] Prop: under RH, if H_0 has simple zeros near a compact K, then for −δ < t ≤ 0 all zeros of H_t in K are real; since H_t has non-real zeros for every t < 0, these leave every compact set as t → 0⁻: the threshold is at infinity. Simplicity verified for the first 1,500,000,001 zeros (γ < 545,439,823.215; van de Lune–te Riele–Winter 1986). Newman's 'barely true' (RT §1; CSV 'quantitative version of the dictum'); Lehmer pairs are finite-height witnesses (CSV Thm 1). [N] first low collision at t ≈ −3.95 (zeros 4, 5), far from 0.

**Numbers.** Λ ≥ 0 (RT), Λ ≤ 0.22 (Polymath) · 1,500,000,001 simple zeros (vdL–tR–W 1986)

**Also known as:** RH barely true; threshold at infinity

**Axes:** restatement ⇔ RH, phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 160

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** ζ does not have a double zero at any computed height; the family, not ζ, is at threshold (TAA Lemma 160, correction 5).

> ⚠ **Correction / caution.** H_t has no Euler product for t ≠ 0 (TAA Lemma 160, correction 9).

**Relations (outgoing):**

- same mechanism as → [de Bruijn–Newman constant Λ](#debruijn-newman)
- lives in → [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy)
- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Λ = 0 given Rodgers–Tao

**Relations (incoming):** [de Bruijn–Newman constant Λ](#debruijn-newman) (same mechanism as); [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin) (feeds); [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero) (mirror of)

### #118 · 0.420 · Mass shell / even Ξ: s(1−s) = ¼ + t² <a id="mass-shell-even-xi"></a>

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

**Relations (incoming):** [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) (same mechanism as); [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) (analogue of); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (analogue of); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (analogue of); [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) (analogue of); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #121 · 0.420 · Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6) <a id="composite-leakage"></a>

**Label:** Restatement · **id:** `composite_leakage` · **quadrant:** RH-sharp

*In plain words:* A true L-function's log-derivative only has terms at prime powers; that is unique factorization in coefficient form. DH has extra terms at composites, starting at 6 = 2·3, and these extra terms are exactly what turn on as you slide away from the true L-function, at the same time as zeros start leaving the line.

**Core.** [T] elementary: log F = Σ c_n/log n · n^{−s}. [C] Saias–Weingartner Acta Arith. 140 (2009): periodic-coefficient series not P·L_χ have ≫T zeros in 1/2 < σ1 < σ < σ2 ≤ 1+η; pencil not P·L_ψ by a_p² ≠ a_{p²} at p ≡ 2 mod 5 (4λ(1−λ)W ≠ 0). [N] n ≤ 3000, 201 λ: leakage.049 (λ=.005),.233 (.033),.696 (1/2); symmetric λ ↔ 1−λ. Weil truncation table. As an RH test: 'has an Euler product' restated (L(χ) pass; GRH open).

**Numbers.** c₆ = 1.9364, c₁₂ = −.7629, c₁₄ = −2.852 · DH onset 1.90 for P = 5, 7, 11, 13 · |c₆| ≈ 7.14λ · TAA Lemma 168: DH smooth truncations lock at 3.85 for P ≥ 43; prime-power-only at 1.90 for P ≥ 3 (428 primes ≤ e⁸)

**Also known as:** unique factorization diagnostic; support on prime powers

**Axes:** restatement ⇔ RH, ghost-sensitive, numerics/certificate

**TAA lemmas:** 165, 168

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

**Relations (outgoing):**

- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — first at n = 6
- lives in → [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy)
- analogue of → [Epstein zeta no-go](#epstein) — same exclusion (restored after the TAA Lemma 164 merge)
- lives in → [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate)

**Relations (incoming):** [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) (lives in); [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) (lives in); [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (lives in); [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) (lives in)

### #124 · 0.420 · Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector <a id="rh-hodge-index-zero-margin"></a>

**Label:** Restatement · **id:** `rh_hodge_index_zero_margin` · **quadrant:** RH-sharp

*In plain words:* Weil turned RH into a positivity statement, and Bombieri asked whether some index theorem proves it. The de Bruijn–Newman constant says that positivity holds with no room to spare.

**Core.** Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector

**Formula.** RH ⇔ Weil form ≥ 0 (pole terms = polarization); Λ ≥ 0 (Rodgers–Tao) ⇒ RH ⇔ Λ = 0

**Axes:** restatement ⇔ RH, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** Building the pole term as a genuine ⋆-polarization is Open (Deninger).

**Relations (outgoing):**

- restates → [Weil positivity criterion](#weil-positivity)
- feeds → [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero)
- feeds → [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold)

**Relations (incoming):** [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts) (refines); [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate) (refines)

### #126 · 0.420 · Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0 <a id="weil-shear-subtracts"></a>

**Label:** Restatement · **id:** `weil_shear_subtracts` · **quadrant:** RH-sharp

*In plain words:* Restated this way, RH says the zeros can only subtract once the pole terms are removed; the restatement proves nothing.

**Core.** Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0

**Formula.** f̂(s) = ĝ(s)·conj ĝ(1−s̄); f̂(0)+f̂(1) = 2Re ĝ(0)conj ĝ(1)

**Axes:** restatement ⇔ RH, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** The inequality is still RH (Open).

**Relations (outgoing):**

- restates → [Weil positivity criterion](#weil-positivity)
- refines → [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin)

**Relations (incoming):** [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance) (feeds); [⟨g|h⟩_W=Σ_ρ ĝ(ρ)conj ĥ(1−ρ̄); Hermitian and scaling-isometric unconditionally; RH ⇔ positive semidefinite](#weil-braket-pairing) (restates)

### #127 · 0.420 · Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing <a id="passive-network-positive-real"></a>

**Label:** Restatement · **id:** `passive_network_positive_real` · **quadrant:** RH-sharp

*In plain words:* A circuit that never produces energy has a positive-real impedance. For ξ′/ξ this property is equivalent to RH. Building the circuit from the primes would make positivity structural.

**Core.** Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing

**Numbers.** min Re Z > 0 on the tested half-plane grid; |Re Z| < 1e−20 on the axis; Foster interlacing holds on the tested range

**Axes:** restatement ⇔ RH, physics analogue, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** Completely passive ⇔ KMS is Pusz–Woronowicz (not opened).

**Relations (outgoing):**

- restates → [Lagarias/Hinkkanen criterion](#lagarias)
- refines → [Passivity (positive real part)](#passivity)
- contrasts with → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #316 · 0.240 · Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down <a id="net-force-orientation"></a>

**Label:** Restatement · **id:** `net_force_orientation` · **quadrant:** RH-sharp

*In plain words:* Locally net = det of the Frobenius Gram matrix, p − a²/4.

**Core.** Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down

**Axes:** restatement ⇔ RH, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- extends → [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading)

**Relations (incoming):** [Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians)](#shear-push-density) (quantifies); [RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin](#kahler-package-one-liner) (uses); [Viscosity multiplies trace-free strain; dissipation 2μ|S°|² ≥ 0 is the analogue of the missing sign; baroclinic wedge ↔ Gram tilt cos θ = r, net = p sin²θ](#viscosity-baroclinic) (illustrates)

### #319 · 0.240 · Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel <a id="anisotropic-part-weil"></a>

**Label:** Restatement · **id:** `anisotropic_part_weil` · **quadrant:** RH-sharp

*In plain words:* On finite bases the top eigenvalue tends to 0 from below; the near-null mode is an archimedean/p=2 cancellation.

**Core.** Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel

**Axes:** restatement ⇔ RH, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- refines → [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance)

**Relations (incoming):** [Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians)](#shear-push-density) (density form of)

### #323 · 0.240 · ⟨g|h⟩_W=Σ_ρ ĝ(ρ)conj ĥ(1−ρ̄); Hermitian and scaling-isometric unconditionally; RH ⇔ positive semidefinite <a id="weil-braket-pairing"></a>

**Label:** Restatement · **id:** `weil_braket_pairing` · **quadrant:** RH-sharp

*In plain words:* RH adds positivity, not unitarity.

**Core.** ⟨g|h⟩_W=Σ_ρ ĝ(ρ)conj ĥ(1−ρ̄); Hermitian and scaling-isometric unconditionally; RH ⇔ positive semidefinite

**Axes:** restatement ⇔ RH, phase/unitarity (Ax3), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- restates → [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts)

## Axis: numerics/certificate <a id="axis-numerics-certificate"></a>

### #29 · 0.580 · Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side <a id="blockwise-weil-diagnostic"></a>

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

### #30 · 0.580 · DH prime-side Gram test <a id="dh-prime-side-gram"></a>

**Label:** Numerical · **id:** `dh_prime_side_gram` · **quadrant:** RH-sharp

*In plain words:* Build the Weil-form Gram matrix of Davenport–Heilbronn from its Dirichlet coefficients alone; it turns indefinite at span 3.85.

**Core.** c_DH(n), n ≤ e^{3.85} ≈ 47, plus Γ-factor suffice; λ_max jumps −8e−9 → 3e−2 between L = 3.80 and 3.90. TAA Lemma 168: reproduced at h = 0.025 by P-smooth truncations: DH onset 3.85 reached at P = 43 and fixed for all 428 primes ≤ e⁸.

**Also known as:** DH from primes

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 149, 168

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

**Relations (outgoing):**

- special case of → [Relative Gram matrix G_rel](#relative-gram) — [instance-of]
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — [control-for] replaces TAA Lemma 141's uncertified zero list
- corrects → [Davenport–Heilbronn function](#davenport-heilbronn) — [replaces] zero-list control → prime side (TAA Lemma 149, correction 1, TAA Lemma 149, correction 4)

**Relations (incoming):** [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) (analogue of); [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) (same mechanism as); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) (analogue of)

### #31 · 0.580 · Euler product and functional equation work only together: the window positivity test <a id="euler-fe-conjunction"></a>

**Label:** Numerical · **id:** `euler_fe_conjunction` · **quadrant:** RH-sharp

*In plain words:* Take Weil-type window forms with the same archimedean term (an odd character of conductor 5) and compare four functions. The genuine product ½L(χ)L(χ̄), which has both an Euler product and a functional equation, stays positive on every window up to length 12. The Davenport–Heilbronn function (functional equation, no Euler product) loses positivity at window length 4.8. Random completely multiplicative Euler products (Euler product, no functional equation) lose it at 1.7–2.5, and the same Euler product with every atom sign flipped at 1.6. So neither property alone carries the sign: a proof step has to use both at once. This is a diagnostic on finite windows, not evidence for RH.

**Core.** Euler product and functional equation work only together: the window positivity test. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** Z_ℓ = arch(odd, q = 5) − Σ Λ_f(n) n^(−½) · (box kernel at log n), box grid h = 0.02; first window ℓ with n₋(Z_ℓ) ≥ 1

**Numbers.** ½L(χ)L(χ̄), χ the odd quartic character mod 5: n₋ = 0 to ℓ = 12 (λ_min = 4.0e−5 at ℓ = 8, 1.7e−5 at ℓ = 12) · Davenport–Heilbronn: first crossing 0 → 2 at ℓ = 4.80; n₋ = 2 at ℓ = 8 · random unimodular completely multiplicative coefficients (6 seeds): first crossing ℓ = 1.68–2.48; n₋ = 27–44 at ℓ = 8 · same Euler product with all atom signs flipped: first crossing ℓ = 1.60

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Window positivity of the genuine form up to ℓ = 12 is consistent with GRH for χ mod 5; it is not evidence for it.

> ⚠ **Correction / caution.** The functional equation is shown necessary only numerically here; the Euler product is necessary by the Davenport–Heilbronn example (Theorem).

**Relations (outgoing):**

- refines → [Davenport-Heilbronn window jumps](#davenport-heilbronn-window-jumps)
- tests → [Davenport–Heilbronn function](#davenport-heilbronn)
- counterexample to sufficiency of → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation)
- tests → [Weil positivity criterion](#weil-positivity)

**Relations (incoming):** [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (uses); [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) (refines); [Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t))](#dilution-law-dh-to-product) (refines)

### #32 · 0.580 · Completeness rigidity: one missing prime creates many unstable modes <a id="completeness-rigidity-one-prime"></a>

**Label:** Numerical · **id:** `completeness_rigidity_one_prime` · **quadrant:** RH-sharp

*In plain words:* The count "exactly one unstable mode" of the arithmetic side of Weil’s form is reached only when every prime power up to the window scale e^ℓ is present. Dropping a single prime from ζ’s Euler product creates many negative modes on every window tested (1 → 7 at ℓ = 2 without p = 2; 1 → 53 at ℓ = 6). Truncated products give counts that go up and down as primes are added, so there is no monotone prime-by-prime filtration. The count is a global cancellation, not a product of local counts. Mechanism [Theorem]: dropping p multiplies ζ by (1 − p^(−s)), whose zeros lie on Re s = 0, at distance ½ from the critical line.

**Core.** Completeness rigidity: one missing prime creates many unstable modes. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** n₋(Z_ℓ) is subadditive: n₋(A + B) ≤ n₋(A) + n₋(B) [Theorem]; (n₋(Z), n₋(W)) on box grids h = 0.02

**Numbers.** ℓ = 2: no primes (4, 3); p ≤ 5 (2, 1); p ≤ 7 (1, 0); all but 2 (7, 6); all but 7 (2, 1) · ℓ = 4: (1, 0) once all p ≤ 55 are present; all but 2 (27, 26); all but 7 (20, 20) · ℓ = 6: (1, 0) once all p ≤ 404 are present; all but 2 (53, 52); all but 7 (44, 44) · non-monotone count at ℓ = 4 as primes are added: 8, 11, 15, 20, 19, 23, 18, 8, 1

**Axes:** numerics/certificate, sign/positivity (Ax2), no-go / refuted, ghost-sensitive

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** "Each local Euler factor has exactly two invariant lines and the product keeps the count" fails as stated: each local factor 1/(1 − p^(−s)) has a whole lattice of poles on Re s = 0 [Heuristic reading].

> ⚠ **Correction / caution.** The qualitative observation that positivity breaks after the first omitted prime is earlier work in the programme; the counts and the drop-one-prime test are new.

**Relations (outgoing):**

- refines → [Local-to-global failure](#local-global)
- refines → [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places)
- tests → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (uses); [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) (explains); [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) (analogy of)

### #33 · 0.580 · Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP <a id="primitive-part-weil-spectrometer"></a>

**Label:** Numerical · **id:** `primitive_part_weil_spectrometer` · **quadrant:** RH-sharp

*In plain words:* Split the Weil test into the part tied to the pole of ζ and the rest. The pole part accounts for exactly one negative direction and nothing else; ζ and a genuine L-function are fine on the rest, while DH fails on the rest exactly as before. So DH's failure is in the 'primitive' part, where the missing positivity has to come from.

**Core.** [N] TAA Lemma 149 cubic-B-spline hats, h = 0.05 (N = 4..319) and h = 0.025 (N = 4..637 step 3); generalized eigenproblem vs hat Gram; thresholds −1e−9 and −1e−12 agree. ζ full λ_min ≥ 6.6e−12 (floor), ζ without pole row: 1 negative from W = 0.25/0.275, none on kerP. χ₅ (χ(2) = i): 0 on both. DH index 1 → 24 (h = 0.025) and 1 → 14 (h = 0.05) by W ≈ 16; kerP differs by ≤ 1 at a few W. [C] Bombieri 2000 (Rend. Lincei 11): if RH failed with finitely many off-line zeros, for large truncations #negative eigenvalues = ½ #off-line zeros; read here for DH by analogy only. The primitive part is where the MP4 sign lives; it is not supplied by the projection.

**Numbers.** DH index 24 (h = 0.025, W = 15.95), 14 (h = 0.05, W = 16) · ζ no-pole index 1 from W = 0.25 · ζ λ_min floor ≈ 7e−12

**Also known as:** v5 direction 2; kerP spectrometer

**Axes:** numerics/certificate, ghost-sensitive, sign/positivity (Ax2)

**TAA lemmas:** 167

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Index not converged in h (24 vs 14): finite-resolution count, not a zero count.

> ⚠ **Correction / caution.** ζ passing to W = 16 is a check consistent with the known zeros, not evidence for RH beyond them.

**Relations (outgoing):**

- lives in → [Primitive part V₀ = U^⊥](#primitive-part)
- special case of → [Weil positivity criterion](#weil-positivity)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — primitive index up to 24
- lives in → [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) — primitive part definite
- same mechanism as → [Pole plane / Tate poles at s = 0, 1](#pole-plane) — kerP removes exactly the pole direction

**Relations (incoming):** [Primitive part V₀ = U^⊥](#primitive-part) (lives in)

### #34 · 0.580 · Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8 <a id="two-standing-ghosts-truncation"></a>

**Label:** Numerical · **id:** `two_standing_ghosts_truncation` · **quadrant:** RH-sharp

*In plain words:* The Epstein zeta function of x² + 5y² has positive coefficients and the right symmetry but no Euler product. In the same prime-truncation test it fails early (at 3.0) and stays failed, like DH; its Euler-product partner ζ_K, with the same symmetry, passes.

**Core.** [N] h = 0.025, n ≤ e^8.1; coefficients exact (r_Q(n)/2; genus check ζ_K = Σ_{d|n} χ₋₂₀(d) max error 0; ζ_K composite c(n) ≤ 6e−14). Epstein composite c(n) ≠ 0 from n = 6 (c₆ = 2 log 6 = 3.584), then 14, 21, 36, 46, …; |c| leakage share 0.55/0.70/0.78 at n ≤ 40/400/3296 (DH 0.48/0.60/0.70; ζ_K ≤ 6e−16). ζ_K truncations: onset W > log q with larger slack than ζ for small P (degree-2 archimedean term). [C] Davenport–Heilbronn 1936 / Lamzouri 2021 (arXiv 1907.06387): Epstein with h(D) ≥ 2 has infinitely many zeros in Re s > 1 and ≫ T zeros in σ₁ < Re s < σ₂. Positive coefficients + FE + pole do not give positivity; the separating input is multiplicativity (cf. TAA Lemma 164, TAA Lemma 166).

**Numbers.** Epstein onset 3.0 (kerP 3.175, no pole 1.05) · locks: smooth 3.0 (P ≥ 7), prime powers 3.35 (P ≥ 3) · index 32 at W = 7.9 (DH 6) · ζ_K: no onset to W = 8

**Also known as:** v5 direction 4; Epstein second ghost

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 169

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Normalization F = Z_Q/2 so a₁ = 1; the Weil form of a non-Euler series is a formal analogue (its explicit formula still holds via −F′/F).

> ⚠ **Correction / caution.** Index counts at finite h, not zero counts.

**Relations (outgoing):**

- fails for → [Epstein zeta no-go](#epstein) — onset 3.0, locks for P ≥ 7
- analogue of → [Davenport–Heilbronn function](#davenport-heilbronn) — second standing ghost
- lives in → [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) — Epstein leakage 0.78 at n ≤ 3296
- same mechanism as → [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) — positive coefficients pass Bochner, fail Weil
- analogue of → [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) — positive counts insufficient over ℚ too

**Relations (incoming):** [Epstein zeta no-go](#epstein) (lives in)

### #35 · 0.580 · Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only <a id="weil-gram-coupling-matrix"></a>

**Label:** Numerical · **id:** `weil_gram_coupling_matrix` · **quadrant:** RH-sharp

*In plain words:* Put a narrow bump at each log p and evaluate the Weil quadratic form on pairs, using only the primes and the archimedean term. The matrix agrees with the zero-side sum to 1e−12 and is positive semidefinite to rounding; its smallest eigenvalue goes to 0⁺ and its rank saturates at the number of zeros the bumps can see. Replacing the exponent ½ in the prime weights by 0.4 or 0.6 destroys positivity.

**Core.** Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only

**Numbers.** s = 0.05, 300 primes: λ_min 1.08, 0.226, 8.5e−3, 1.3e−6 at N = 2, 5, 10, 20; then rounding level; rank 28 · s = 0.02: λ_min 23.2 → 3.6e−10 at N = 100, then rounding · without the pole term: λ_min = −5.4e5 at N = 300 · σ = 0.4 and 0.6: negative eigenvalues (−1.05e5 and −88.9 at N = 100); σ = ½: PSD

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Positivity here is equivalent to the visible zeros being on the line (Restatement); not evidence for RH.

**Relations (outgoing):**

- tests → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)
- restates → [Connes trace formula](#connes-trace)

**Relations (incoming):** [Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder](#structured-gram-factor-search) (extends); [How much the primes fill the archimedean deficit of the Weil form, by support](#archimedean-rectifier-fill) (related to); [Multi-channel first-order factors are bounded by the SOS fit](#gram-factor-channel-bound) (refines); [Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity](#arithmetic-topology-linking-matrix) (compared with)

### #36 · 0.580 · Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3 <a id="growing-s-truncation-rate"></a>

**Label:** Numerical · **id:** `growing_s_truncation_rate` · **quadrant:** RH-sharp

*In plain words:* Keep only the primes up to P and test positivity. For true Euler products the test fails exactly when the first missing prime comes into view, every time, for all 428 primes tried. DH behaves the same while its composite terms are kept, until it hits its own failure point at 3.85, where it stays.

**Core.** [N] onset = first span with λ_min < −1e−9 (bisection, exact to h). ζ_P = pole + arch + prime powers p ≤ P; DHs_P = arch + all P-smooth n; DHp_P = arch + prime powers only. Per-prime offset bounded by about half the hat support (2h = 0.05; χ₅ up to 0.063), no trend with log q: no finite S is positive beyond log of the next prime (per-prime data cannot certify positivity; v5 no-go 27/28). DH lock at 3.85 reproduces TAA Lemma 149 dh_prime_side_gram (n ≤ e^3.85 ≈ 47 suffices); DHp lock at 1.90 reproduces TAA Lemma 165 (c₆ at log 6). DH-sensitivity appears only through composites; the per-prime offset itself is not DH-sensitive (DHs offsets match ζ’s until P = 41).

**Numbers.** ζ offsets 0.009–0.052 · DH smooth lock 3.85 (P ≥ 43) · DH prime-power lock 1.90 (P ≥ 3) · ζ margin 1.8e−6 → 5e−11

**Also known as:** v5 direction 3; smooth-DH truncation

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 168

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.580

> ⚠ **Correction / caution.** Margins below ~1e−10 are at the conditioning floor of the hat basis (full ζ λ_min ≈ 7e−12 at W = 16).

> ⚠ **Correction / caution.** Rate = offset in span; no claim about the size of positivity added per prime beyond the margin column.

**Relations (outgoing):**

- lives in → [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — locks at 3.85 (smooth) / 1.90 (prime powers)
- same mechanism as → [DH prime-side Gram test](#dh-prime-side-gram) — n ≤ 46 suffice
- lives in → [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) — no finite S suffices

**Relations (incoming):** [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) (lives in)

### #89 · 0.492 · Near-null direction of ζ's relative Gram matrix <a id="near-null-anatomy"></a>

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

### #90 · 0.492 · The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation <a id="single-box-axis-criterion"></a>

**Label:** Numerical · **id:** `single_box_axis_criterion` · **quadrant:** true but ghost-blind/untested

*In plain words:* Instead of growing the number of test functions at a fixed window, take one box of length ℓ. The resulting function F(ℓ) is an explicit prime sum minus the pole plus the archimedean term. On the zero side it is a sum of squares under RH, and an off-line zero would add a term growing like e^(βℓ) with oscillating sign, so "F(ℓ) ≥ 0 for all ℓ" is (heuristically, Landau-type) equivalent to RH. Numerically F stays between 0.060 and 0.134 on [1, 10], but the pole and the primes cancel to one part in about 9400 at ℓ = 10. The obstruction is moved, not removed.

**Core.** The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** F(ℓ) = ℓ·W(1_[0,ℓ]/√ℓ) = W(1_[0,ℓ]) = Σ_{γ>0} 8 sin²(γℓ/2)/γ² (under RH)

**Numbers.** prime side = zero side (5000 zeros plus tail) to 2.1e−4 relative on ℓ ∈ [0.1, 10] · min F = 0.0601 on [1, 10]; mean value 4Σ1/γ² = 0.0933 · pole part / F = 9433 at ℓ = 10

**Axes:** numerics/certificate, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.64 → priority 0.492

> ⚠ **Correction / caution.** As a route this is RH again (circular).

> ⚠ **Correction / caution.** If the ordinates γ are linearly independent over ℚ, Kronecker’s theorem makes inf F = 0 over all ℓ, so the margin is uniform only on finite ranges [Heuristic].

> ❓ **Not verified / open.** The equivalence with RH is a Heuristic, Landau-type sketch; criteria of this shape are probably classical (not checked against the literature); no novelty is claimed.

**Relations (outgoing):**

- restates → [Weil positivity criterion](#weil-positivity)
- refines → [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate)

### #91 · 0.492 · Integer dimension over 𝕊 (minimal generators) <a id="dim-s"></a>

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

### #134 · 0.400 · One Perron mode against the pole <a id="pole-perron-one-mode"></a>

**Label:** Numerical · **id:** `pole_perron_one_mode` · **quadrant:** RH-sharp

*In plain words:* Split Weil's form on a grid of narrow boxes as W = Z + P, where Z (archimedean plus primes) has non-positive off-diagonal entries and P is the rank-2 pole term. On every grid tested, Z has exactly one negative eigenvalue, with an entrywise-positive (Perron) eigenvector. The pole's positive eigenvalue cancels it with a margin of 1e-3 to 1e-6. Without the primes, Z has about ell*6.29/pi - 1 negative modes; the primes collapse them into one. Positivity of W implies at most one negative mode of Z (theorem); an unconditional proof that there is exactly one, together with a positive 2x2 margin on all grids, is open and would imply RH. In the finite-field template the single negative mode is the ample (timelike) class of Hodge index and the pole is 2 d1 d2; fakes have two negative modes. The entrywise-positive Perron vector is automatic from the sign pattern and also occurs for fakes.

**Core.** One Perron mode against the pole

**Formula.** J_pq = h j(q/p), j(r) = r^{3/2}/(r^2-1) - (sqrt r + 1/sqrt r) = -(r^3-r-1)/(sqrt r (r^2-1)); ferromagnetic iff q/p < rho (plastic number 1.3247); eps = -1 - v^T Z^{-1} v; n_-(W) = n_-(Z) + n_-(S_2) - 1

**Numbers.** fraction of prime pairs <= 1e4 with q/p < rho: 163185/754606 = 0.21625 (heuristic limit 1 - 1/rho = 0.2451) · lambda_min(Z) = -1.987, -4.305, -7.230, -11.231 at ell = 1, 2, 3, 4 · margin eps = 4.4e-4, 3.4e-5, 5.7e-5, 2.7e-6; lambda_min(W) = 6.0e-4, 1.2e-4, 3.1e-4, 2.2e-5 · negative modes of Z without primes: 2, 4, 6, 8 · archimedean deformation psi(z/hbar) + log hbar: sign change at hbar* = 1.0004 (ell = 2) and 1.0003 (ell = 3)

**Axes:** numerics/certificate, sign/positivity (Ax2), reference/pole/cusp, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- refines → [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix)
- refines → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime) (tests); [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece) (refines); [Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector](#dedekind-qi-one-mode) (refines); [No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes](#ferromagnetic-sign-not-count) (corrects); [The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions](#prime-weight-anisotropy) (refines); [Ghost count of the arithmetic side](#ghost-count-theorem) (refines); [Frobenius-graph Toeplitz form and its pole/count split](#frobenius-graph-toeplitz-split) (analogy of); [Castelnuovo-Severi defect as a Toeplitz block](#fq-cs-block-identity) (analogy of); [λ₂ is monotone under nested windows (Cauchy interlacing)](#lambda2-monotone-nested-windows) (refines)

### #135 · 0.400 · Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1) <a id="allowed-locally-not-aligned-globally"></a>

**Label:** Numerical · **id:** `allowed_locally_not_aligned_globally` · **quadrant:** RH-sharp

*In plain words:* For a degree-2 L-function each prime has an angle θ_p (α_p/√p = e^(±iθ_p)). Hasse (11a1) and Deligne (Ramanujan’s Δ) make every angle real, and Sato–Tate says how they are distributed. Both are proved; GRH is open. In the window model the genuine angles keep the form positive for every window up to ℓ = 7, while the same angles permuted among the primes, i.i.d. Sato–Tate angles, aligned rearrangements, or one wrong local factor all fail quickly. Global positivity pins each angle to a fraction of a degree although 180° is allowed. So the missing piece is the joint law of the angles across all primes, together with the archimedean place and the conductor — not any single angle.

**Core.** Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma). Cited: Deligne, Publ. Math. IHÉS 43 (1974) Thm 8.2; Barnet-Lamb–Geraghty–Harris–Taylor 2011 (Sato–Tate).

**Formula.** atom weights 2cos(kθ_p) log p / p^(k/2); Δ: Γ_R(s+11/2)Γ_R(s+13/2), q = 1; 11a1: Γ_R(s+½)Γ_R(s+3/2), q = √11 each; box grid h = 0.02, ℓ ≤ 7

**Numbers.** genuine angles: n₋ = 0 for every ℓ = 1…7 (Δ: λ_min = 7.2e−3 at ℓ = 1 … 5.8e−5 at ℓ = 7; 11a1: 6.0e−5 at ℓ = 7) · genuine angles permuted, 20 seeds: 20/20 fail by ℓ ≤ 2 (Δ: n₋ = 27–44 at ℓ = 7; 11a1: 13–20); only primes > 50 permuted: 20/20 fail at ℓ = 4–5 · i.i.d. Sato–Tate angles, 20 seeds: 20/20 fail by ℓ ≤ 2 (Δ: n₋ = 26–43 at ℓ = 7; 11a1: 12–20) · adversarial but allowed: same multiset aligned with cos(t₀ log p), t₀ = 1.5/3/6: Δ n₋ = 18/25/23, 11a1 6/7/10 at ℓ = 7; every θ_p = π/2: 13 / 8; every θ_p = 0.05: n₋ = 1, λ_min = −73 · 11a1 with the bad-prime factor mis-normalised: n₋ = 2…13 for ℓ = 3…7 · pinning (one angle varied, others genuine): Δ, p = 2: 0.32° (ℓ = 2) → 0.062° (ℓ = 6); p = 3: 0.25° → 0.027°; p = 7: 0.024° at ℓ = 6; 11a1, p = 2: 11.1° → 0.13°; p = 7: 0.028° at ℓ = 6 · Δ, worst genuine test vector at ℓ = 7: archimedean −0.2567, primes +0.2568, net 5.8e−5 (one part in about 4400) · checks: a_p of 11a1 by point counting = q-expansion of η(z)²η(11z)² for p ≤ 3000 (0 mismatches); Sato–Tate KS distance 0.024, mean cos²θ = 0.243 (theory 0.25), n = 429

**Axes:** numerics/certificate, sign/positivity (Ax2), phase/unitarity (Ax3), ghost-sensitive

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

> ⚠ **Correction / caution.** ζ has no angle per prime: its Euler factor 1 − p^(−s) has degree 1; for ζ the "angle" is only the phase γ log p of a zero against a prime.

> ⚠ **Correction / caution.** Window positivity for ℓ ≤ 7 is a finite section of a criterion equivalent to GRH: consistent with GRH, not evidence for it.

> ⚠ **Correction / caution.** Finite-window margins go to 0 as ℓ grows, so the pinning widths are model-dependent: read the trend, not the values.

> ⚠ **Correction / caution.** The Hecke relations (a_mn = a_m a_n, a_p² relation) hold for any assignment of angles, including the shuffled ones; what is joint is the existence of the modular form, i.e. the functional equation.

**Relations (outgoing):**

- refines → [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton)
- tests → [Hecke operators](#hecke)
- refines → [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction)
- analogy of → [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime)

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (analogous to); [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities) (tests)

### #136 · 0.400 · Ghost onset L* ≈ log(γ/2π) <a id="ghost-onset"></a>

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

**Relations (incoming):** [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) (implies); [Ghost onset depends on kernel width](#onset-kernel-dependence) (corrects); [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant) (restates); [Certified positivity windows](#certified-windows) (fails for); [Yoshida window positivity](#yoshida) (fails for)

### #137 · 0.400 · The induction matrix on the Q-quotient (Weil form on S-unit lattices) <a id="q-quotient-induction-matrix"></a>

**Label:** Numerical · **id:** `q_quotient_induction_matrix` · **quadrant:** RH-sharp

*In plain words:* Place one Gaussian test function at log m for each S-smooth m ≤ N and take M_mn = W(η_m, η_n), Weil's quadratic form built from primes and the archimedean place. Translation invariance makes M_mn a function of the rational m/n alone. The couplings take both signs about equally (their pattern follows cos(γ₁ log(m/n))), so the matrix is pair-dependent but not ferromagnetic. Its smallest eigenvalue is positive and collapses super-exponentially as the lattice fills (σ = 0.1: 2.4e−5 → 8.7e−26 for N = 30). Restricting the prime sum to S makes it strongly negative, because the indefinite rank-2 pole term is no longer cancelled by the prime density. Including all primes up to the window scale restores positivity. The matrix is the Weil form rewritten: positivity for all such lattices is a restatement of RH.

**Core.** The induction matrix on the Q-quotient (Weil form on S-unit lattices)

**Formula.** M_mn = w(log(m/n)), w(d) = Σ_{γ>0} 4πσ² e^{−σ²γ²} cos(γd) = pole + archimedean − 2Σ Λ(n)n^{−1/2} g_d(log n)

**Numbers.** zero-side agreement ≤ 5e−37 · λ_min full, σ=0.1, N=100, X=2,3,5,7: 8.0e−8, 3.4e−14, 7.4e−25, 4.8e−36 · λ_min truncated, N=100: −0.77, −2.00, −2.96, −3.47, −3.73 for X = 2..11 · restoration: primes ≤ 3N suffice at σ = 0.1

**Axes:** numerics/certificate, sign/positivity (Ax2), restatement ⇔ RH, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- analogy of → [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1)
- counterexample to sufficiency of → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)
- instance of → [The critical-line wave: Hardy Z and the Riemann–Siegel phase](#hardy-z-critical-line-wave)

**Relations (incoming):** [One Perron mode against the pole](#pole-perron-one-mode) (refines)

### #138 · 0.400 · Davenport-Heilbronn window jumps <a id="davenport-heilbronn-window-jumps"></a>

**Label:** Numerical · **id:** `davenport_heilbronn_window_jumps` · **quadrant:** RH-sharp

*In plain words:* The Davenport-Heilbronn function has the functional equation and archimedean factor of an odd character mod 5 but no Euler product, and has off-line zeros near 0.8085+85.699i and 0.6508+114.163i. Its window form has no negative squares for short windows and gains them in pairs, one quadruple at a time, at window length about 3.9 and 5.67. So the archimedean place and the functional equation cannot force the second mode to stay non-degenerate: any proof must use the Euler product. This matches the constant-signature mechanism of Adiprasito-Huh-Katz Prop. 7.16, where non-degeneracy is proved independently.

**Core.** Davenport-Heilbronn window jumps

**Formula.** n_-(W_DH,l): 0 -> 2 at l ~ 3.9, 2 -> 4 at l ~ 5.67 (h = 0.01)

**Numbers.** jumps · offline_zeros

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- instance of → [Ghost count of the arithmetic side](#ghost-count-theorem)
- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

**Relations (incoming):** [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) (refines)

### #139 · 0.400 · Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t)) <a id="dilution-law-dh-to-product"></a>

**Label:** Numerical · **id:** `dilution_law_dh_to_product` · **quadrant:** RH-sharp

*In plain words:* Mix the two forms: (1−t)·(Davenport–Heilbronn) + t·(½L(χ)L(χ̄)). On the zero side this carries the Davenport–Heilbronn zeros with weight 1−t, so for every t < 1 the off-line zeros are still there and some window eventually sees them. The window at which they are first seen recedes only logarithmically as t → 1. In plain words: any fixed amount of non-multiplicativity is caught by a long enough window. This calibrates "a proof must use the Euler product"; it says nothing about whether RH is true.

**Core.** Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t)). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** ℓ*(t) ≈ 5.14 + 2.51·log(1/(1−t)) (fit); the first Davenport–Heilbronn ghost has 1/β′ = 3.24

**Numbers.** ℓ*(t) = 4.80, 5.28, 5.78, 6.30, 6.74, 7.14, 7.50, 7.76, 8.02, 8.38, 8.86, 9.64, 11.36 at t = 0, 0.1, …, 0.9 (and two intermediate points); no crossing up to ℓ = 12 at t = 0.95 and t = 1 · the fit predicts 12.7 at t = 0.95, consistent with no crossing up to 12

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.64 → priority 0.400

> ⚠ **Correction / caution.** For 0 < t < 1 the mixture is not an L-function; it is a weighted ledger with fractional multiplicities.

> ❓ **Not verified / open.** Theorem-level sketch only: it assumes GRH for χ mod 5 (to place χ’s zeros on the line) and the computed Davenport–Heilbronn zeros; constants are not certified.

**Relations (outgoing):**

- refines → [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction)
- analogy of → [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy)
- refines → [Crossing scale of a ghost](#ghost-crossing-scale)

### #140 · 0.400 · Which channel detects a fake depends on the span <a id="channel-depends-on-span"></a>

**Label:** Numerical · **id:** `channel_depends_on_span` · **quadrant:** RH-sharp

*In plain words:* For fake Frobenius data (functional equation kept, one root pair off the circle), when the chosen graphs span the fibre classes the pole channel is exactly zero and the failure is on the primitive part. With fewer graphs, the failure appears first in the odd pole channel while the primitive part is still positive. Over the rationals no finite section spans the fibre classes, so the model does not rule out an off-line zero showing first in the pole channel.

**Core.** Which channel detects a fake depends on the span

**Formula.** N = r+2: ε = η = 0, λ_min(W|kerP) < 0;  N < r+2: η < 0, λ_min(W|kerP) > 0

**Numbers.** fakes_tested · first_negative_N

**Axes:** numerics/certificate, geometry over F_q, ghost-sensitive

**TAA lemmas:** 181

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

**Relations (incoming):** [Which channel an off-line zero breaks first over the rationals](#ghost-channel-order-over-q) (refines)

### #141 · 0.400 · Certified window for one off-line pair <a id="explicit-ghost-window"></a>

**Label:** Numerical · **id:** `explicit_ghost_window` · **quadrant:** RH-sharp

*In plain words:* For a synthetic off-line quadruple at the height of the first zero, Paley-Wiener interpolants at the pole pair and the four off-line points, a written-out mollification step, and a tail bound (Poisson-kernel envelope of the kernels plus the Hadamard identity sum of Poisson kernels = (1/pi) Re xi'/xi) certify three negative squares for every window length at least 5.55, 3.60, 2.90, 2.20 at displacement 0.1, 0.2, 0.3, 0.45. The certificate is floating point, not interval arithmetic. A closed form scales like displacement^(-2/3) at low height and like (1/displacement) log(8 displacement log(height/2pi)) at large height. The explicit length needs every off-line zero to be known.

**Core.** Certified window for one off-line pair

**Formula.** lambda_{1+N+}(H+R) + 2u + u^2 < 0  =>  n_-(Z_l) = 1 + N+ for all larger l;  |e_w(x)|^2 <= coth(sigma beta) P_beta(x - t)

**Numbers.** ell_certified · ell_closed_form

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- refines → [Ghost count of the arithmetic side](#ghost-count-theorem)

**Relations (incoming):** [Crossing scale of a ghost](#ghost-crossing-scale) (refines)

### #142 · 0.400 · Which channel an off-line zero breaks first over the rationals <a id="ghost-channel-order-over-q"></a>

**Label:** Numerical · **id:** `ghost_channel_order_over_Q` · **quadrant:** RH-sharp

*In plain words:* Diagnostic, not evidence: off-line zero quartets were planted by hand on finite sections of Weil's form (box, sine, Legendre and bump bases; supports 1 to 5). In 225 of 226 failing runs the form first goes negative through the pole channel (even or odd, about equally). The primitive part fails just after, exactly when the planted zero gives the arch-plus-primes part a second unstable mode, and the gap between the two onsets shrinks as the section is refined. The finite-field rule 'incomplete span means the pole channel fails first' carries over; its 'odd channel' refinement does not, and the TAA Lemma 2 distance of the fibre functionals from the section does not predict the channel.

**Core.** Which channel an off-line zero breaks first over the rationals

**Formula.** beta_W <= beta_kerP = beta(n_-(Z)=2);  gap (beta_kerP - beta_W)/beta_W: 0.22 (N=4) -> 2e-4 (N=840), support 5

**Numbers.** runs · failing · pole_first · eps_first · eta_first · primitive_first · smallest_onset_beta

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 181

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- refines → [Which channel detects a fake depends on the span](#channel-depends-on-span)
- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

### #143 · 0.400 · Crossing scale of a ghost <a id="ghost-crossing-scale"></a>

**Label:** Numerical · **id:** `ghost_crossing_scale` · **quadrant:** RH-sharp

*In plain words:* For synthetic off-line pairs the second eigenvalue of the arithmetic side first goes negative at a window length roughly log(t/2pi)(0.85 + 0.14/beta) on h = 0.01 grids: both the displacement and the height matter. The level drops as the grid is refined; the shape is stable.

**Core.** Crossing scale of a ghost

**Formula.** l* ~ log(t/2pi) (0.85 + 0.14/beta)

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- refines → [Certified window for one off-line pair](#explicit-ghost-window)

**Relations (incoming):** [Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t))](#dilution-law-dh-to-product) (refines)

### #144 · 0.400 · Duursma zeta functions of codes as a finite RH laboratory: Golay satisfies RH; the [32,16,4] code G₂₄ ⊕ e₈ fails <a id="duursma-code-toy"></a>

**Label:** Numerical · **id:** `duursma_code_toy` · **quadrant:** RH-sharp

*In plain words:* Linear codes have zeta functions with a Riemann hypothesis that can hold or fail, so the positivity tests can be calibrated on them.

**Core.** Duursma zeta functions of codes as a finite RH laboratory: Golay satisfies RH; the [32,16,4] code G₂₄ ⊕ e₈ fails Duursma, arXiv:math/0302172.

**Axes:** numerics/certificate, ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (tested by)

### #145 · 0.400 · The Laguerre inequality Ξ′² − ΞΞ″ > 0 holds for ζ on [0,60] and fails exactly around the off-line zero of the Davenport–Heilbronn function <a id="laguerre-detects-offline-zero"></a>

**Label:** Numerical · **id:** `laguerre_detects_offline_zero` · **quadrant:** RH-sharp

*In plain words:* A one-site positivity test that does see an off-line zero: for the Davenport–Heilbronn function the Laguerre quantity turns negative on 85.42 ≤ t ≤ 85.98, bracketing its zero at 0.8085 + 85.6993i.

**Core.** The Laguerre inequality Ξ′² − ΞΞ″ > 0 holds for ζ on [0,60] and fails exactly around the off-line zero of the Davenport–Heilbronn function

**Numbers.** ζ: normalised minimum 0.0337 on [0,60] · DH: negative on t ∈ [85.42, 85.98]; off-line zero 0.808517 + 85.699348 i

**Axes:** numerics/certificate, sign/positivity (Ax2), ghost-sensitive

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.7 · evidence 0.8 → priority 0.400

**Relations (outgoing):**

- tests → [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh)

### #150 · 0.387 · Integer Ψ_n lattice test (negative result) <a id="psi-n-lattice"></a>

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

### #157 · 0.365 · Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector <a id="dedekind-qi-one-mode"></a>

**Label:** Numerical · **id:** `dedekind_qi_one_mode` · **quadrant:** true but ghost-blind/untested

*In plain words:* For ζ_ℚ(i) = ζ·L(χ₄) the arithmetic side of the window form is ζ’s plus a pole-free part. As predicted, it has exactly one unstable mode on every window tested, aligned with the pole vector and entrywise positive, and the full form W has no negative squares. Its margins are about three times ζ’s, which is automatic because W_K = W_ζ + W_χ.

**Core.** Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Numbers.** ℓ = 2, 3, 4, 6: n₋(Z_K) = 1; cos(φ, v) = 0.99598, 0.99864, 0.99879, 0.99953; n₋(W_K) = 0 · L(χ₄) alone has n₋ = 0 on these windows · alignment bound 0 ≤ ‖v‖² − μ ≤ E holds in every case

**Axes:** numerics/certificate, sign/positivity (Ax2), reference/pole/cusp

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

> ⚠ **Correction / caution.** The larger margins are trivial (W_K ≥ W_ζ when W_χ ≥ 0) [Restatement]; positivity of W_χ is only checked numerically.

**Relations (outgoing):**

- tests → [Ghost count of the arithmetic side](#ghost-count-theorem)
- refines → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄)](#chi-minus-one-half-pole) (explains)

### #158 · 0.365 · Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻ <a id="talenti-template-test"></a>

**Label:** Numerical · **id:** `talenti_template_test` · **quadrant:** true but ghost-blind/untested

*In plain words:* The template gives a sign only where no primes enter.

**Core.** Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻

**Axes:** numerics/certificate, sign/positivity (Ax2)

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- constrains → [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece)

**Relations (incoming):** [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance) (tested by); [W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ](#archimedean-weyl-kernel) (feeds)

### #159 · 0.365 · No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes <a id="ferromagnetic-sign-not-count"></a>

**Label:** Numerical · **id:** `ferromagnetic_sign_not_count` · **quadrant:** true but ghost-blind/untested

*In plain words:* The arithmetic side of the window form has non-positive off-diagonal entries, so its lowest mode is entrywise positive (Perron–Frobenius). That sign pattern does not force the count. In a deformed-archimedean test the matrix stays ferromagnetic yet has two to three unstable modes. So a Hodge-index proof shape "ample class plus an effective cone" cannot get its cone from this sign alone. Likewise Λ(n) ≥ 0, the sign behind the 3 + 4cos θ + cos 2θ trick, only excludes off-line zeros near the edge of the strip.

**Core.** No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Numbers.** deformed archimedean scale ħ = 0.75: the matrix stays ferromagnetic and has 2–3 unstable modes · Davenport–Heilbronn coefficients: Λ(2) = 0.197, Λ(3) = −0.312, Λ(4) = −1.442 (mixed signs); 66% of its non-zero atoms with n ≤ e⁸ sit at non-prime-powers

**Axes:** numerics/certificate, no-go / refuted, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

> ⚠ **Correction / caution.** The deformed archimedean term satisfies no explicit formula; it is used only as a counterexample, not as evidence.

> ⚠ **Correction / caution.** This concerns the sign pattern of the window matrix, not the Lee–Yang ferromagnet of the refined missing piece.

**Relations (outgoing):**

- corrects → [One Perron mode against the pole](#pole-perron-one-mode)
- fails for → [Hodge index theorem](#hodge-index)

### #160 · 0.365 · The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions <a id="prime-weight-anisotropy"></a>

**Label:** Numerical · **id:** `prime_weight_anisotropy` · **quadrant:** true but ghost-blind/untested

*In plain words:* Scale the p = 2 atoms by (1 + d cos θ) and the p = 3 atoms by (1 + d sin θ) and ask how large d can be before the window form loses positivity. The allowed region is narrowest near 30–37° (close to the total-mass, i.e. pole, direction) and widest near 127° (roughly mass-neutral). The aspect ratio is about 30, and both widths shrink at about e^(−0.8ℓ). Rotating by 45° separates a pole direction from a primitive direction but does not escape the shrinking.

**Core.** The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** u = d₂ + d₃ (total mass, cancelled by the pole), v = d₂ − d₃ (primitive); global-scaling tolerance ≈ λ_min(W)/‖v‖² [Restatement]

**Numbers.** ℓ = 4: narrowest half-width 4.6e−5 at 37.5°, widest 1.5e−3 at 127.5° (aspect 32) · ℓ = 6: narrowest 9.7e−6 at 30°, widest 2.7e−4 at 127.5° (aspect 28) · global scaling of all primes, upper tolerance: 2.4e−2, 3.4e−4, 6.3e−5, 1.7e−5, 3.8e−6, 1.9e−6 at ℓ = 1, …, 6

**Axes:** numerics/certificate, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

> ⚠ **Correction / caution.** The primitive (mass-neutral) direction is fine-tuned too; only a constant factor of about 30 is gained.

**Relations (outgoing):**

- refines → [One Perron mode against the pole](#pole-perron-one-mode)
- refines → [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate)

### #161 · 0.365 · Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder <a id="structured-gram-factor-search"></a>

**Label:** Numerical · **id:** `structured_gram_factor_search` · **quadrant:** true but ghost-blind/untested

*In plain words:* An SDP search asks whether the Weil form on a finite test space is the square of a sparse first-order operator linking n to pn. It is not: the best such factor leaves at least half of the form unexplained, with a certified lower bound. The prime pattern does fit somewhat better than additive or random patterns, and better on the true form than on a control built from jittered zeros: a weak arithmetic signal. Any exact factor is, up to rotation, indexed by the zeros (circular).

**Core.** Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder

**Numbers.** relative residual, s = 0.05: 0.50, 0.67, 0.75, 0.79 (SDP lower bounds, N = 10, 20, 30, 40); additive 0.71–0.90; random 0.63–0.88 · fitted ladder coefficient exponent ≈ −0.19 (not −½) · Cholesky mass on prime-ratio pairs 28% true vs 18% jittered-zero control (N = 40)

**Axes:** numerics/certificate, sign/positivity (Ax2), no-go / refuted

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- extends → [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix)
- constrains → [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece)

### #162 · 0.365 · How much the primes fill the archimedean deficit of the Weil form, by support <a id="archimedean-rectifier-fill"></a>

**Label:** Numerical · **id:** `archimedean_rectifier_fill` · **quadrant:** true but ghost-blind/untested

*In plain words:* Below support log 4 the archimedean term alone is favourable (Yoshida's regime). From log 4 on it has unfavourable directions, which the primes fill with a ratio tending to 1 from above, while the margin falls from 3e−3 to below quadrature noise by support 2.5. Primes 2 and 3 alone fill the first dip but not beyond support 2.

**Core.** How much the primes fill the archimedean deficit of the Weil form, by support The archimedean kernel is monotone with one sign change at t₀ = 6.29; it does not oscillate.

**Numbers.** margin 3.19e−3 (log 3), 1.45e−6 (log 4), 7.5e−9 (1.6), 1.1e−10 (2.0) · min fill ratio 1.351, 1.121, 1.037, 1.0001, 1.00002 at supports log 4, 1.6, 2, 2.5, 3 · 2 and 3 only: total +0.31 at support 2, +0.62 at 2.5

**Axes:** numerics/certificate, sign/positivity (Ax2), reference/pole/cusp

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- related to → [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix)

### #163 · 0.365 · Cutoff saturation (class-number x is not the lever) <a id="cutoff-saturation"></a>

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

### #164 · 0.365 · Genus seen at resolution sigma <a id="genus-at-resolution"></a>

**Label:** Numerical · **id:** `genus_at_resolution` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over a finite field the ratio of the defect of a graph to 2 d1 d2 is the genus, the same for every graph. Over the rationals the analogous ratio for a Gaussian test function of log-width sigma runs from very large (fine functions) to essentially zero (coarse functions). Coarse test functions see no first cohomology, which is why the pole margin tends to zero.

**Core.** Genus seen at resolution sigma

**Formula.** g_eff(σ) = e^{-σ²/4} Σ_γ e^{-σ²γ²}

**Numbers.** sigma · g_eff

**Axes:** numerics/certificate, geometry over F_q

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

### #165 · 0.365 · LMFDB level-1 Maass list complete to T = 100 <a id="lmfdb-maass-complete"></a>

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

### #166 · 0.365 · Null-calibrated GLS matched filter <a id="null-calibrated-gls"></a>

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

### #167 · 0.365 · Ghost onset depends on kernel width <a id="onset-kernel-dependence"></a>

**Label:** Numerical · **id:** `onset_kernel_dependence` · **quadrant:** true but ghost-blind/untested

*In plain words:* The span at which a fake off-line zero becomes visible depends on the test-function width h, not only on the span.

**Core.** Hats: DH-location ghost 3.45 (h=0.025) vs 5.15 (h=0.05); DH 3.85 vs 5.75; γ₁ δ=0.01 1.8 vs 3.85.

**Axes:** numerics/certificate

**TAA lemmas:** 149

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- corrects → [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) — TAA Lemma 149, correction 3 (TAA Lemma 142 'invariant is the span')

### #168 · 0.365 · Model kernel e^{−bu²−u⁶}: first zero collision at b_c ≈ 3.1955 <a id="sextic-kernel-collision"></a>

**Label:** Numerical · **id:** `sextic_kernel_collision` · **quadrant:** true but ghost-blind/untested

*In plain words:* For the model kernel, increasing b merges the first two real zeros of its Fourier transform at z ≈ 8.25 when b ≈ 3.1955; beyond that the pair is complex.

**Core.** Model kernel e^{−bu²−u⁶}: first zero collision at b_c ≈ 3.1955

**Numbers.** real zeros on (0,40]: 13 at b = 3.1955, 11 at b = 3.1956; collision at z ≈ 8.25

**Axes:** numerics/certificate, physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.7 · evidence 0.8 → priority 0.365

**Relations (outgoing):**

- illustrates → [de Bruijn–Newman constant Λ](#debruijn-newman)

### #188 · 0.347 · Certified positivity windows <a id="certified-windows"></a>

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

### #204 · 0.325 · Multi-channel first-order factors are bounded by the SOS fit <a id="gram-factor-channel-bound"></a>

**Label:** Theorem · **id:** `gram_factor_channel_bound` · **quadrant:** true but ghost-blind/untested

*In plain words:* If every channel of Q lies in a fixed operator dictionary, Σ_k Q_kᵀQ_k = Σ X_ab B_aᵀB_b with X ⪰ 0, so no number of channels beats the sum-of-squares fit in that dictionary. For Weil's form on short-support Legendre bases with the dictionary {I, functions of the archimedean part, prime shifts}, two channels reach 5.8–7.1% residual, matching the SOS bound (5.8–6.8%); one archimedean plus one shift channel is far worse (27–60%).

**Core.** Multi-channel first-order factors are bounded by the SOS fit

**Numbers.** support 1.5 and 3.0, N = 16–32, double precision · independent recheck: λ_min = 9.44716e−7 (support 1, N 24), 2.05904e−16 (support 2, N 24), 1.62356e−20 (support 2, N 32); archimedean-plus-pole positivity up to support 0.7432

**Axes:** numerics/certificate, sign/positivity (Ax2), no-go / refuted

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** λ_min at fixed support keeps falling with N; quote N with every value

**Relations (outgoing):**

- refines → [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix)
- analogy of → [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge)

### #247 · 0.307 · Archimedean thresholds a* <a id="arch-threshold"></a>

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

### #249 · 0.307 · Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity <a id="arithmetic-topology-linking-matrix"></a>

**Label:** Numerical · **id:** `arithmetic_topology_linking_matrix` · **quadrant:** true but ghost-blind/untested

*In plain words:* In arithmetic topology primes behave like knots and the Legendre symbol like a linking number. The symmetric matrix of Legendre symbols among primes ≡ 1 mod 4 looks like a random sign matrix: about half its eigenvalues are negative, and its signs are uncorrelated with the Weil Gram coupling matrix. Quadratic linking does not see positivity.

**Core.** Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity Morishita, Knots and Primes (Springer 2012); Deninger, arXiv:0709.2801 (3-dimensional foliated dynamical systems, closed orbits as knots).

**Numbers.** N = 300: eigenvalues −31.8 … +32.3 (≈ ±0.92·2√N), 149 negative · sign agreement with the Weil Gram matrix 0.495, correlation −0.008 (z = −1.6)

**Axes:** numerics/certificate, no-go / refuted, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.8 → priority 0.307

**Relations (outgoing):**

- compared with → [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix)
- constrains → [Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow](#hopf-fibration-spec-z)

### #250 · 0.307 · Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z² <a id="slack-ledger-cf"></a>

**Label:** Numerical · **id:** `slack_ledger_cf` · **quadrant:** true but ghost-blind/untested

*In plain words:* How fast the local slack is used up is governed by how well log q/log p is approximated by fractions.

**Core.** Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z²

**Formula.** |t_first(Z)| = d_min(Z)²/8 ≈ C²/(8Z²)

**Numbers.** Z≤1e9 · envelope slopes −1.01,−0.85,−0.89,−0.90 · record α 1.04,1.11,1.08,1.16 · 22/22 same-branch jumps = q_n · |t_c/(−d²/8)−1| ≤ 5e−15 on 24 records

**Axes:** numerics/certificate, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.8 → priority 0.307

> ⚠ **Correction / caution.** Z·d_min stays in [0.11, 5.4]; partial quotients drive the excursions.

**Relations (outgoing):**

- refines → [Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)](#local-dbn-slack)
- refines → [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero)

### #251 · 0.307 · Monotone quantities along the de Bruijn–Newman flow: kernel-side entropies are smooth through t = 0; zero-side energy relaxes <a id="dbn-monotone-functionals"></a>

**Label:** Numerical · **id:** `dbn_monotone_functionals` · **quadrant:** true but ghost-blind/untested

*In plain words:* Along the heat flow, the entropy, Fisher information and a one-dimensional Perelman-type functional of the tilted kernel e^{tu²}Φ change smoothly and monotonically, with nothing special at t = 0, so they cannot see the de Bruijn–Newman constant. The zeros' pair energy decreases and their spacing becomes more regular (the Rodgers–Tao gradient-flow picture), but any such zero-side quantity is circular as a route to RH.

**Core.** Monotone quantities along the de Bruijn–Newman flow: kernel-side entropies are smooth through t = 0; zero-side energy relaxes Perelman, arXiv:math/0211159; Rodgers–Tao, arXiv:1801.05914.

**Formula.** W_min(p) = S − ½ log(2πe/I) ≥ 0; ∂_t x_k = 2Σ_{j≠k} 1/(x_k − x_j), ∂_t 𝓗 = −4E (formal, full system)

**Numbers.** t ∈ [−0.2, 0.5]: S −0.8147 → −0.8075, I 87.76 → 86.54, W_min 0.00373 → 0.00393 · first ten zeros: energy 1.265 → 1.147, gap coefficient of variation 0.399 → 0.369; truncated Hamiltonian increases (cross terms)

**Axes:** numerics/certificate, no-go / refuted, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.7 · evidence 0.64 → priority 0.307

> ❓ **Not verified / open.** Open: a functional whose monotonicity is a sum of squares and fails exactly at off-line zeros.

**Relations (outgoing):**

- tests → [de Bruijn–Newman constant Λ](#debruijn-newman)

### #269 · 0.267 · Yoshida window positivity <a id="yoshida"></a>

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

### #37 · 0.580 · Chebyshev bias for elliptic curves (averaged sign of a_p) <a id="elliptic-chebyshev-bias"></a>

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

### #38 · 0.580 · Ghost conventions A / B / C for spectral tests <a id="ghost-conv-abc"></a>

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

### #55 · 0.540 · de Bruijn–Newman constant Λ <a id="debruijn-newman"></a>

**Label:** Cited · **id:** `debruijn_newman` · **quadrant:** RH-sharp

*In plain words:* Heat flow on ξ; Λ ≥ 0 (Rodgers–Tao), RH ⇔ Λ = 0.

**Core.** Λ ≥ 0 ⇒ ζ not heat-flow stable (TAA Lemma 111). Healing times TAA Lemma 124/TAA Lemma 136 conflict. TAA Lemma 150 (opened): Rodgers–Tao Λ ≥ 0 (Forum Math Pi 2020), Polymath 15 Λ ≤ 0.22; H_0(z) = Ξ(z/2)/8, so t_RT = 4·t_Ξ (TAA Lemma 150, correction 8). DH heuristic (truncated list): pair at 85.70 closes at t_RT ≈ 0.177 (isolated 2δ² = 0.190); does not separate DH from ζ's known range. TAA Lemma 158: H_t = ∫e^{tu²}Φ(u)cos(zu)du solves the BACKWARD heat equation ∂_tH = −∂_zzH (Rodgers–Tao, Polymath, opened); increasing t (= exp(−tD²), anti-dissipative) makes zeros real (Pólya); the dissipative (forward-heat) direction t ↓ creates collisions and complex pairs. RH ⇔ Λ ≤ 0; Λ ≥ 0 (Rodgers–Tao, Forum Math Pi 2020); Λ ≤ ½ (de Bruijn 1950); −∞ < Λ (Newman 1976); Λ ≤ 0.22 (Polymath). Toy exp(−tD²)(z²−1)(z²−1.6²): Λ_toy = −0.0463. F/V merge = 𝔽_q picture of the collision (Analogy, fv_merge_trichotomy). TAA Lemma 159: Newman–Wu 2019 (opened): the 1976 theorem's motivation came 'more by statistical physics and Euclidean field theory … than by analytic number theory'; Lee–Yang property of Φ is the precise Lee–Yang form of RH (lee_yang_fisher_rh). TAA Lemma 160: direction stated explicitly (RT convention ∂_t H = −∂_zz H; increasing t makes zeros real; collisions come from lowering t); RH ⇔ Λ = 0; under RH with simple zeros the forced collisions escape every compact set as t → 0⁻ (dbn_parabolic_threshold). Newman 1976 is Proc. AMS 61, 245–251 (AMS DOI record; TAA Lemma 158 had 246). TAA Lemma 180: local flow = F/V sweep; Λ_p = ACM Lemma 3.18 (t_ACM = t log²p, t_RT = 4t); product cross-term explicit; Λ_global = 0 for incommensurable Hasse products (Heuristic/Numerical).

**Numbers.** Λ ∈ [0, 0.22] · DH t*_RT ≈ 0.177 (H)

**Also known as:** heat flow; Λ ≥ 0

**Axes:** ghost-sensitive, restatement ⇔ RH

**TAA lemmas:** 111, 124, 136, 150, 158, 159, 160, 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** t* = 2δ² vs δ²/2.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — Λ = 0
- analogue of → [Krein collisions (how ghosts are born)](#krein-collision)
- same mechanism as → [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold)

**Relations (incoming):** [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) (restates); [Krein collisions (how ghosts are born)](#krein-collision) (analogue of); [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (analogue of); [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold) (same mechanism as); [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh) (same mechanism as); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) (analogue of); [Model kernel e^{−bu²−u⁶}: first zero collision at b_c ≈ 3.1955](#sextic-kernel-collision) (illustrates); [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) (lives in); [Monotone quantities along the de Bruijn–Newman flow: kernel-side entropies are smooth through t = 0; zero-side energy relaxes](#dbn-monotone-functionals) (tests); [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep) (localises)

### #60 · 0.540 · Ghost quartet ½ ± δ ± iγ <a id="ghost-quartet"></a>

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

**Relations (incoming):** [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) (same mechanism as); [Krein collisions (how ghosts are born)](#krein-collision) (same mechanism as); [Gain lines (active media)](#gain-line) (analogue of); [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) (analogue of); [BRST / Gupta–Bleuler physical quotient](#brst) (analogue of); [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) (same mechanism as); [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) (same mechanism as); [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) (same mechanism as); [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4) (analogue of)

### #65 · 0.540 · Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census <a id="euler-to-dh-pencil-genealogy"></a>

**Label:** Theorem · **id:** `euler_to_dh_pencil_genealogy` · **quadrant:** RH-sharp

*In plain words:* Slide continuously from a genuine L-function to DH and watch: zeros move along the line, and every time two of them with opposite orientation collide, a pair jumps off. Doing this up to height 600 recreates exactly DH's 15 known bad zeros and records when and where each was born.

**Core.** [N] 154875-point Arb grid t ≤ 620; 242 certified folds; escapes (t_c, λ*) from (85.90,.3054) … (531.73,.0330); every endpoint Krawczyk-certified as a DH zero, equal to TAA Lemma 156/cycle-3 census to double precision (2 in uncensused 135–200); Krawczyk both sides of each fold; exponents.496–.500; on-line 494 → 464, signs 200/294 → 185/279 (one of each per collision). Captures at λ =.4445 (t 286.2),.4148 (t 475.8). LRL/precession comparison: Analogy only.

**Numbers.** 17 escapes, 2 captures, net 15 · min λ* =.0330 (t_c 531.7) · exponent.496–.500

**Also known as:** B3 / redesigned A4 test; DH genealogy; σ-pencil

**Axes:** ghost-sensitive, numerics/certificate, structure/frame (Ax1)

**TAA lemmas:** 165

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — reproduces its census by deformation
- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision)
- lives in → [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4)

**Relations (incoming):** [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (analogue of); [Krein collisions (how ghosts are born)](#krein-collision) (lives in); [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) (analogue of); [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) (lives in); [Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t))](#dilution-law-dh-to-product) (analogy of)

### #68 · 0.540 · Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β <a id="gamma-as-dual-adjoint-gap"></a>

**Label:** Theorem · **id:** `gamma_as_dual_adjoint_gap` · **quadrant:** RH-sharp

*In plain words:* The width Γ of a zero equals how far the pairing-dual and the positive adjoint disagree on that zero.

**Core.** [T] For any eigenvector v (|v| = 1) of Θ with eigenvalue ρ = β+iγ: Θ^∨v = (1−ρ)v and ⟨Θ†v,v⟩ = ρ̄, so ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β and Γ_ρ = |1−2β| = |(1−ρ) − ρ̄| ≤ ‖Θ^∨ − Θ†‖ = 2‖S‖ (no normality needed). 𝔽_q: |q/α − ᾱ| = |q − |α|²|/|α|; in exponents (α = q^s) |(1−s) − s̄| = |1−2β|. [N, certified inputs TAA Lemma 156] DH: ρ₁ gap 0.617034364913274771106, ρ₂ 0.301660161219474164808, ρ₃ 0.14871210090161198144, ρ₄ 0.448515389253619560422 (mirrors equal); ζ (52 zeros, t < 150) and DH on-line (122, t < 200): gap 0.

**Numbers.** ρ₁ 0.617034364913, ρ₂ 0.301660161219, ρ₃ 0.148712100902, ρ₄ 0.448515389254 · ζ: 0 on 52 certified zeros

**Axes:** ghost-sensitive, restatement ⇔ RH, numerics/certificate

**TAA lemmas:** 157

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** Γ ≤ ‖Θ^∨ − Θ†‖ is an inequality per eigenline; equality of operators needs normality.

**Relations (outgoing):**

- same mechanism as → [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) — Γ = FWHM limit = dual−adjoint gap
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — ghost gaps 0.617, 0.302, 0.149, 0.449
- equivalent to RH → [Lagarias/Hinkkanen criterion](#lagarias) — all gaps 0 ⇔ no gain lines
- lives in → [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint)
- same mechanism as → [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) — certified β

**Relations (incoming):** [Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity)](#ep-gap-across-collision) (same mechanism as); [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) (analogue of)

### #70 · 0.540 · Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150 <a id="certified-zero-lists"></a>

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

**Relations (incoming):** [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) (same mechanism as); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as)

### #74 · 0.540 · Ghost map Δ_w: zeros right of σ from damped Dirichlet sums <a id="ghost-map"></a>

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

### #86 · 0.540 · Bagchi recurrence <a id="bagchi"></a>

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

### #114 · 0.451 · Must-fail-for-DH acceptance test <a id="dh-acceptance"></a>

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

### #117 · 0.420 · Γ, the width of a zero: FWHM of its Breit–Wigner line <a id="gamma-fwhm-of-a-zero"></a>

**Label:** Restatement · **id:** `gamma_fwhm_of_a_zero` · **quadrant:** RH-sharp

*In plain words:* Each zero shows up as a bell-shaped line; its width at the critical line is twice its distance from the line. RH says every width is zero: every line becomes a spike.

**Core.** [T] On Re s = σ each zero ρ = β+iγ contributes to Re ξ′/ξ the signed line (σ−β)/((σ−β)²+(t−γ)²): FWHM 2|σ−β|, height 1/(σ−β), area π·sgn(σ−β) (Hadamard; TAA Lemma 146). [R] Γ_ρ := 2|β−½| = lim_{σ→½} FWHM (signed Γ± = 2(β−½); FE mirror has −Γ±); s = ½+iE puts ρ at E = γ − iΓ±/2. RH ⇔ all Γ_ρ = 0 ⇔ every line sharpens to πδ_γ as σ↓½. Γ is a limit, not observable on σ = ½ itself (Re ξ′/ξ ≡ 0 there by the FE; TAA Lemma 154, correction 6). 'Stable vs decaying' is convention-dependent; invariant: unitary state vs non-unitary ±Γ pair (in u = log x the ghost grows like e^{Γu/2}; TAA Lemma 154, correction 3). [N] TAA Lemma 154: ζ (5 zeros) and DH on-line: measured FWHM = 2d to 3.3e−7 rel over 13 lines d ∈ [0.01, 0.5], area π to 6e−7; DH ghosts: near line FWHM 2|d − (β−½)| (≤ 3e−6), flips to a gain line for d < β−½, → Γ = 0.617 / 0.302 from below (0.5970 / 0.2816 at d = 0.01; TAA Lemma 154, correction 2: not 'at least Γ'); visible feature width ≈ ½(β−½) constant, depth ≈ 2d/(β−½)² → 0; planted ghost (0.8, 40) identical. [N] TAA Lemma 155: Γ recovered without a zero list — Γ̂ = 2(β̂−½) = 0.61703, 0.30166 from the ghost map's phase slope (coefficients + Γ-factor + FE); exact comb from the theta AFE agrees with TAA Lemma 154 to 1e−12. Recorded in TAA Lemma 155 §0; certification in TAA Lemma 156. TAA Lemma 156 [N, rigorous]: certified (Arb) Γ₁ = 0.617034364913274771106 ± 9e−22, Γ₂ = 0.30166016121947416481 ± 3e−21; [T given certificates] flips at d* = β−½ in (0.30,0.35), (0.15,0.20); ζ targets simple on the line ⇒ FWHM 2d exact; ghost FWHM → Γ from below; [N] TAA Lemma 154 fits certified to first order (rel ≤ 1.6e−5; ghost 2 ≤ 6.3e−5 after tail subtraction). TAA Lemma 157: Γ_ρ = |⟨(Θ^∨ − Θ†)v,v⟩| = |(1−ρ) − ρ̄|, the dual−adjoint gap (Thm); DH ρ₃ 0.148712100902, ρ₄ 0.448515389254 (from TAA Lemma 156 enclosures).

**Numbers.** ζ: FWHM = 2d, rel err ≤ 3.3e−7 (13 d, 5 zeros) · DH ghost 1: Γ = 0.61703, FWHM 0.5970 at d = 0.01 · DH ghost 2: Γ = 0.30166, FWHM 0.2816 at d = 0.01 · feature depth −0.216 vs −2d/(β−½)² = −0.210 (d = 0.01)

**Also known as:** width of a zero; resonance width; Γ = 2|β−½|

**Axes:** ghost-sensitive, restatement ⇔ RH, numerics/certificate

**TAA lemmas:** 154, 155, 156, 157, 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** The ghost FWHM tends to Γ from below; it sharpens only on σ = β (TAA Lemma 154, correction 2).

> ⚠ **Correction / caution.** Decaying vs growing depends on the sign convention; the FE pairs ±Γ (TAA Lemma 154, correction 3).

> ⚠ **Correction / caution.** Hilbert–Pólya in widths is content-free without a natural operator (TAA Lemma 154, correction 5).

> ⚠ **Correction / caution.** TAA Lemma 159: reading Γ as entropy production gives an empty second law (Γ ≥ 0 by definition); RH = Γ ≡ 0 is a reversibility (equality) statement.

**Relations (outgoing):**

- equivalent to RH → [Riemann hypothesis (target node)](#rh) — all widths vanish
- same mechanism as → [Gain lines (active media)](#gain-line) — σ < β ⇒ inverted line
- same mechanism as → [Lagarias/Hinkkanen criterion](#lagarias) — positivity of the comb on σ > ½
- analogue of → [Hilbert–Pólya](#hilbert-polya) — Γ = 0 ⇔ real energy
- same mechanism as → [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) — one width for every zero
- lives in → [Davenport–Heilbronn function](#davenport-heilbronn) — measured ghosts

**Relations (incoming):** [Lagarias/Hinkkanen criterion](#lagarias) (same mechanism as); [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (special case of); [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) (same mechanism as); [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) (same mechanism as); [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) (same mechanism as); [Gain lines (active media)](#gain-line) (same mechanism as); [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) (corrects); [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) (analogue of); [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) (special case of); [Anomalous dispersion](#anomalous-dispersion) (same mechanism as)

### #172 · 0.360 · Ghost conventions (δ, heat-flow healing) <a id="ghost-conventions"></a>

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

### #180 · 0.360 · S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T) <a id="s-of-t-remainder"></a>

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

### #43 · 0.579 · Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS) <a id="lmhs-nilpotent-orbit"></a>

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

### #45 · 0.579 · Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not <a id="livsic-route-split"></a>

**Label:** Theorem · **id:** `livsic_route_split` · **quadrant:** sharp but interpretive

*In plain words:* If every closed orbit of Deninger's hoped-for flow stretched its two transverse directions equally, a theorem of Kalinin and Sadovskaya type would make the whole flow conformal, and Deninger's theorem would put the zeros on the line. The explicit formula, though, only tells us each orbit's sign and its area scaling p. It cannot tell a rotation from a mild squeeze, so the key local input has to come from somewhere else. Worse, equal stretching on every orbit is more than RH needs: a slightly bent version of Deninger's own example keeps RH, yet stretches unequally at one fixed point. So the missing input has to be global, a positivity on the square, as in Connes and Consani's programme.

**Core.** [T] Thm I (invisibility) and Prop S (abelian half) of TAA Lemma 174; conditional on (A1) a solenoidal version of KS 2010 Thm 1.3 (Open). [C] Kalinin, Ann. Math. 173 (2011): Livšic for GL(m,R) cocycles over transitive homeomorphisms of compact metric spaces with the closing property; Kalinin–Sadovskaya, JMD 4 (2010) Thm 1.3: 2-dim fibres, return maps diagonalizable over C with equal-modulus eigenvalues ⇒ conformal (base: transitive C² Anosov diffeo of a compact manifold). [Open] (A1) solenoidal KS; [Open] (A2) fixed points (infinitely generated orbit lengths); [Open] (A3) the local input, invisible to the explicit formula. RH is not proved. [T] Conformal (SO(2)) periodic data on the prime orbits is invisible to the explicit formula (Thm I) and strictly stronger than RH: a nonlinear perturbation of Deninger's CM elliptic-curve solenoid over F₅ keeps H¹, hence RH, but has a node fixed point (agreed in partner review; the perturbation is not reproduced in TAA Lemma 174). So a per-orbit route needs a rigidity axiom that arithmetic does not supply, and (B) must be global: an intersection pairing Γ_F·Δ on the square with Rosati/Hodge-index positivity [R: this restates Connes–Consani]. Model: Deninger's elliptic-curve solenoid satisfies all links (return maps π^ν, C-linear; Hasse ⇔ |π| = √q).

**Numbers.** allowed band 2 < |tr M_p| < √p + 1/√p (p = 2: 2.1213) · |det A_p| = p from the k ≤ −1 coefficients Np^k

**Also known as:** Livšic route; (A) split into A1–A3; invisibility theorem

**Axes:** structure/frame (Ax1), Spec ℤ gap, ghost-sensitive

**TAA lemmas:** 174

**Scores (Heuristic):** gap significance 0.8 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 0.5 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.579

> ⚠ **Correction / caution.** Kalinin–Sadovskaya 2010 is for C² Anosov diffeomorphisms of compact manifolds only.

> ⚠ **Correction / caution.** The earlier reading “each prime orbit’s transversal is a rotation” holds only when |det| = 1 (TAA Lemma 174, correction 1).

**Relations (outgoing):**

- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — reduces H4 to periodic orbits, given (A1)
- analogue of → [Deninger’s foliated program](#deninger) — periodic-data route to Thm 4.1
- same mechanism as → [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) — invariant leafwise J = holomorphic flow
- lives in → [Connes–Consani sites](#connes-consani) — the global form of (B): Γ_F·Δ on the square with Rosati/Hodge-index positivity [Restatement]

**Relations (incoming):** [Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x](#beurling-counting-test-bstar) (lives in)

### #47 · 0.579 · Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸) <a id="adelic-gluing-bruhat-tits"></a>

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

**Relations (incoming):** [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) (lives in)

### #61 · 0.540 · Poincaré disk: period domain, cusp degeneration and the trace classification <a id="poincare-disk-period-domain"></a>

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

### #76 · 0.540 · ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂* <a id="profinite-integers-adelic-solenoid"></a>

**Label:** Theorem · **id:** `profinite_integers_adelic_solenoid` · **quadrant:** RH-sharp

*In plain words:* The profinite integers are where all the finite primes live in the adelic picture. They are not the analogue of Frobenius over ℚ (that is the real scaling flow); they give the totally disconnected direction and the Dirichlet-character sectors, and DH sits in no single sector.

**Core.** [C] Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂ (Frobenius generates the dense ℤ); ℤ̂ = ∏ℤ_p, dual ℚ/ℤ; 𝔸_ℚ ≅ ℝ × (ℤ̂⊗ℚ) (Wikipedia, opened). [T] ℚ + (ℝ × ℤ̂) = 𝔸_ℚ and ℚ ∩ (ℝ × ℤ̂) = ℤ ⇒ ℚ⧵𝔸_ℚ ≅ (ℝ × ℤ̂)/ℤ, the adelic solenoid (leaves ℝ, transversal ℤ̂; Den05's S¹_p = ℝ ×_ℤ ℤ_p is the one-prime case, opened). [T] class number 1 + ℤ^× = {±1}: C_ℚ = ℚ^×⧵𝔸^× ≅ ℝ₊* × ℤ̂*. [C] Connes 1999 (20)–(21): C_k ≅ K × N, N = ℝ₊* (number fields) vs q^ℤ (function fields); H = ⊕_χ H_χ over characters of K. Dictionary: over ℚ the Frobenius role goes to ℝ₊* (the flow), not to ℤ̂; ℤ̂ carries the finite primes (transversal), ℤ̂* the Dirichlet-character sectors. [T,N] DH = ½(1−iκ)L(s,χ) + ½(1+iκ)L(s,χ̄), χ mod 5 (residual 0): a sum of two sectors, in no single one; a(2)a(3) = −0.0807 ≠ a(6) = 1. Wikipedia's line 𝔸^×/ℚ^× ≅ (ℝ×ℤ̂)/ℤ conflates the additive quotient: not used.

**Numbers.** DH decomposition residual 0; a(2)a(3) = −0.0807, a(6) = 1

**Also known as:** adelic solenoid; idele class group

**Axes:** structure/frame (Ax1), ghost-sensitive, geometry over F_q

**TAA lemmas:** 158

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** ℤ̂ ≠ the Frobenius group over ℚ: Connes N = ℝ₊*.

> ⚠ **Correction / caution.** Sector exclusion of DH is structural, not a sign: GRH per sector remains open.

**Relations (outgoing):**

- lives in → [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits)
- analogue of → [Connes trace formula](#connes-trace) — C_ℚ = ℝ₊* × ℤ̂*
- same mechanism as → [Bost–Connes KMS states](#kms-bost-connes) — ℤ̂* symmetry
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — DH = two ℤ̂*-sectors
- analogue of → [Deninger’s foliated program](#deninger) — solenoids

**Relations (incoming):** [On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example)](#conformal-flow-needs-solenoid) (analogue of)

### #100 · 0.452 · Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points <a id="laguerre-formula"></a>

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

### #102 · 0.452 · Measure versus metric: the product formula gives an invariant measure, not an invariant metric <a id="haar-measure-not-metric"></a>

**Label:** Theorem · **id:** `haar_measure_not_metric` · **quadrant:** true but ghost-blind/untested

*In plain words:* By the product formula, multiplication by nonzero rationals preserves Haar measure on the idele classes, and the closed orbits have lengths log p. What it does not give is an invariant metric, i.e. a Hermitian structure: Spec ℤ comes with a density, and that is exactly why it is not yet Kähler. The lift the shape list asks for would turn that Haar measure into a Hermitian metric for which the pole line is self-dual and the graphs of multiplication by n are anti-self-dual. A positive Hodge star commuting with the flow would give RH (Deninger, ICM 1998, p. 169), so such a lift stated as positivity is equivalent to RH.

**Core.** Measure versus metric: the product formula gives an invariant measure, not an invariant metric. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma). Cited: Connes, Selecta Math. 5 (1999) 29–106; Deninger, Doc. Math. Extra Vol. ICM 1998 I, 163–186.

**Formula.** |x|_∞ ∏_p |x|_p = 1 ⇒ ℚ^× preserves Haar measure on 𝔸^×; C_ℚ ≅ ℝ_{>0} × Ẑ^×; no ℚ^×-invariant metric is supplied

**Axes:** structure/frame (Ax1), Spec ℤ gap, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 0.8 → priority 0.452

> ⚠ **Correction / caution.** Random Euler products have no pole, so they are not Haar at s = 1; Davenport–Heilbronn has no Euler product, hence no adelic density [Heuristic / Theorem].

> ❓ **Not verified / open.** The lift itself is Open (Conjecture-level); it would need Deninger’s conjectured cohomology, which has not been constructed.

**Relations (outgoing):**

- refines → [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids)
- refines → [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal)
- constrains → [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open)

**Relations (incoming):** [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (uses)

### #104 · 0.452 · On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example) <a id="conformal-flow-needs-solenoid"></a>

**Label:** Theorem · **id:** `conformal_flow_needs_solenoid` · **quadrant:** true but ghost-blind/untested

*In plain words:* A flow on a closed, finite manifold cannot stretch everything sideways forever, because the total volume has to stay the same. The Riemann zeta function needs exactly such stretching. So Deninger's space has to be a solenoid, in which the stretching along the leaves is paid for by shrinking in a dust-like p-adic direction.

**Core.** [T] one-line proof (TAA Lemma 174 Thm V). [C] Deninger 2005 Cor. 5.5 Rem. 2 and arXiv 0709.2801 state that the conditions force α = 0; Rem. 3: finitely generated orbit-length group, infinitely generated needs fixed points; §7: solenoid (C ×_Γ T_πΓ) ×_{p^Z} R*_+ with metric e^t Re ξη̄ has α = 1. [H] multiplication by π scales leaf area by q and has index q on T_πΓ.

**Numbers.** α = 0 forced (compact manifold)

**Also known as:** Theorem V; α = 0 on manifolds

**Axes:** structure/frame (Ax1), Spec ℤ gap

**TAA lemmas:** 174

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

> ⚠ **Correction / caution.** Volume balance on solenoids is shown only for Deninger’s elliptic-curve example (Heuristic in general).

**Relations (outgoing):**

- lives in → [Deninger’s foliated program](#deninger) — why α = 1 needs solenoids
- analogue of → [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) — non-archimedean transversal

**Relations (incoming):** [Deninger’s foliated program](#deninger) (lives in)

### #110 · 0.452 · Yoneda specification <a id="yoneda"></a>

**Label:** Theorem · **id:** `yoneda` · **quadrant:** true but ghost-blind/untested

*In plain words:* Specify the object by its properties (Ax1–Ax3).

**Core.** TAA Lemma 90: bare Hom sets do not determine an object (ℚ vs ℚ^(N)); naturality needed; representability ⇒ uniqueness/functoriality, presupposes positivity if it is an axiom. TAA Lemma 98 Prop 6.1: representable ⇒ unique; 𝔉(pt) ≠ ∅ ⇒ RH; "representability is the whole battle" (TAA Lemma 98, correction 19). TAA Lemma 137: T_W with Ax1–Ax3; existence open.

**Also known as:** T_W

**Axes:** structure/frame (Ax1)

**TAA lemmas:** 89, 90, 98, 137

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.452

**Relations (outgoing):**

- same mechanism as → [Ax1–Ax3 axioms (Yoneda specification)](#ax123)

### #116 · 0.423 · Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off <a id="weil-template-factor-product"></a>

**Label:** Analogy · **id:** `weil_template_factor_product` · **quadrant:** background

*In plain words:* In Weil's proof a curve is one factor, the surface C×C is the product, and the ample class splits the product. Over the integers Deninger's foliation plays the factor, the Connes–Consani square the product, and the splitting is what is missing.

**Core.** Over F_q [Theorem]: factor C (H¹), product C×C, ample-class splitting ℝH ⊕ H^⊥; on S² × S², L_{X×Y} = L_X ⊗ 1 + 1 ⊗ L_Y gives ½ ⊗ ½ = 1 ⊕ 0, triplet = H⁰, ample class, H⁴, singlet = primitive H² class, negative (signature (1,1)). Over ℤ [Analogy, adopted as standing]: Deninger's foliation / H¹ of Deninger's conjectured cohomology = the factor; the Connes–Consani square of the arithmetic site = the product; 1 ⊕ 0 = a splitting of the product (not a separate space), which is the missing piece. Cusp reading (exact in parts): the split-off part pt × C, C × pt = MP0 boundary terms = poles of ζ at 0, 1 = the Eisenstein/cusp constant term (the ζ factor of L(Δ×Δ,s) = ζ(s−11)L(Sym²Δ,s), whose pole comes from the cusp constant term); MP4(2) is definiteness on the primitive part orthogonal to exactly these. Kepler/KS: r = u†u is the singlet; the collision r = 0 is Moser's point at infinity (Analogy).

**Formula.** ½ ⊗ ½ = 1 ⊕ 0

**Also known as:** Weil template; factor / product / splitting; seeing the square from the cusp

**Axes:** structure/frame (Ax1), reference/pole/cusp, geometry over F_q, Spec ℤ gap

**Scores (Heuristic):** gap significance 0.8 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 0.6 · specificity 0.5 · tractability 0.4 · evidence 0.5 → priority 0.423

> ⚠ **Correction / caution.** Roles were first stated reversed (CC square as ½ ⊗ ½ and the foliation as 1 ⊕ 0); the foliation is the factor, 1 ⊕ 0 a splitting.

**Relations (outgoing):**

- lives in → [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) — MP0 boundary terms = split-off part
- same mechanism as → [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) — the product
- analogue of → [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface)
- analogue of → [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) — S² × S², singlet ↔ point at infinity
- analogue of → [Primitive part V₀ = U^⊥](#primitive-part) — definiteness on the complement of the split-off part

**Relations (incoming):** [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (lives in)

### #123 · 0.420 · Density × density: Weil’s form read off the diagonal and its log n translates <a id="density-times-density-diagonal"></a>

**Label:** Restatement · **id:** `density_times_density_diagonal` · **quadrant:** RH-sharp

*In plain words:* The prime side of ζ is a density on the log-scale line, dΛ = Σ Λ(n) δ(x − log n). Weil’s form pairs two half-densities g(x), g(y) against a distribution that depends only on x − y. That distribution is not supported on the diagonal alone: it lives on the diagonal (the archimedean term and the pole, which is a smooth Haar part) and on its translates x − y = ±log n, with weights Λ(n)/√n. Those translates are the graphs of multiplication by n, the analogue of the graphs of Frobenius powers on C × C, whose Gram matrix over F_q is Toeplitz (Hallouin–Perret). The two pole functionals are pairings with the Haar half-densities x^(±½), so quotienting by the pole line (Gupta–Bleuler) is quotienting by "pure Haar". Positivity of the pairing is Weil’s criterion, i.e. RH.

**Core.** Density × density: Weil’s form read off the diagonal and its log n translates. From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma). Cited: Hallouin–Perret, Trans. AMS 372 (2019) 5409–5451.

**Formula.** ⟨g|g⟩_W = ∫∫ g(x) ḡ(y) dΔ(x − y), dΔ supported on {x = y} ∪ {x − y = ±log n}, weight Λ(n)/√n on the translates

**Numbers.** ζ, Perron mode of Z_ℓ, box grid h = 0.02: net/pole E/P = 7.9e−3, 1.7e−3, 1.1e−3 at ℓ = 2, 4, 6, with n₋(W) = 0 · one prime dropped (2, 3, 5 or 7): E/P = 1.3e−2 to 2.0e−1 (1.7–80 times worse) and n₋(W) = 1–52; the failure shows up in the primitive part, not as a sign flip of the pole channel · dropping p multiplies ζ by (1 − p^(−s)), which has zeros on Re s = 0 [Theorem]

**Axes:** structure/frame (Ax1), restatement ⇔ RH, sign/positivity (Ax2)

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

> ⚠ **Correction / caution.** "Read off the diagonal" should be "read off the diagonal and its log n translates".

> ⚠ **Correction / caution.** That the four lifts (F_q → ℚ, local → global, Spec ℤ → Spec ℤ × Spec ℤ, quotient → whole space) are one move is an Analogy; only the finite-field statement (graphs against the diagonal) is a Theorem.

**Relations (outgoing):**

- restates → [Weil positivity criterion](#weil-positivity)
- analogy of → [Frobenius-graph Toeplitz form and its pole/count split](#frobenius-graph-toeplitz-split)
- refines → [Half-density normalization |x|^{½}](#half-density)
- explains → [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime)

**Relations (incoming):** [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric) (refines)

### #191 · 0.325 · Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1) <a id="morse-lobes-wedges-windows"></a>

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

**Relations (incoming):** [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (same mechanism as); [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) (lives in); [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #192 · 0.325 · Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity <a id="zeros-as-frames-trichotomy"></a>

**Label:** Theorem · **id:** `zeros_as_frames_trichotomy` · **quadrant:** true but ghost-blind/untested

*In plain words:* Think of each zero on the line as a frame that is still elliptic. Two zeros can leave the line only by first merging into a double zero, the parabolic moment, and then splitting into a mirror pair off the line. The only other route is for off-line zeros to come in from infinity.

**Core.** [T] For a continuous family F_t of real entire functions (e.g. de Bruijn–Newman H_t, Rodgers–Tao convention H_t(z) = ∫₀^∞ e^{tu²}Φ(u)cos(zu)du, H_0(z) = ξ(½ + iz/2)/8): (a) a simple real zero stays simple and real for nearby t (Hurwitz + conjugation symmetry); (b) non-real zeros come in pairs z, z̄ (quartets ±z, ±z̄ for even F_t = TAA Lemma 103 ghost quartet); (c) a real zero becomes non-real inside a bounded region only through a real zero of multiplicity ≥ 2 at the transition; otherwise non-real zeros arrive from infinity. [A] Spectral reading: separated F ≠ V on the circle / F = V merge / hyperbolic split (TAA Lemma 158 §H). [N] independent quadrature: zeros 4, 5 of H_t collide at t* = −3.954792524, x* = 66.1974676 (TAA Lemma 111 −3.954792522, diff 2.2e−9), ∂²H ≠ 0 (double); box |Re z − x*| ≤ 4, |Im z| ≤ 1.5: argument principle 2.000000 at t* + 0.05, t* − 0.05, t* − 0.3, real zeros 2, 0, 0; pair 66.4147 ± 0.7812i at t* − 0.3; fold law |Im| ∝ (t* − t)^{1/2} (Polymath §3; TAA Lemma 111 fit 0.51). [T, KGL] only opposite Krein signs exit (4×4 toy, ε = 0.2: window |ω₁ − ω₂| < 0.2, max Re λ 0.0995; same sign ≤ 2.2e−16); graphical Krein sign of H_t alternates (−,+,… on zeros 1–8), so every adjacent pair is a possible exit.

**Numbers.** t* = −3.954792524, x* = 66.1974676 (zeros 4, 5) · box count 2.000000 across collision; real count 2 → 0 · Krein toy window |δ| < 0.2

**Also known as:** Krein collision of zeros

**Axes:** structure/frame (Ax1), phase/unitarity (Ax3), numerics/certificate

**TAA lemmas:** 160

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Global zeros are not frame mergers: no Euler factor vanishes (TAA Lemma 160, correction 1, TAA Lemma 160, correction 4).

> ⚠ **Correction / caution.** Zeros can also arrive from infinity; Hurwitz is local (TAA Lemma 160, correction 11).

**Relations (outgoing):**

- same mechanism as → [Krein collisions (how ghosts are born)](#krein-collision) — double zero = opposite-sign collision
- same mechanism as → [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) — zero-level version of the F/V merge
- lives in → [de Bruijn–Newman constant Λ](#debruijn-newman)
- analogue of → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — hyperbolic split = boost

**Relations (incoming):** [Krein collisions (how ghosts are born)](#krein-collision) (lives in); [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold) (lives in); [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) (lives in); [Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity)](#ep-gap-across-collision) (lives in)

### #194 · 0.325 · Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point <a id="dual-conic"></a>

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

### #199 · 0.325 · Null-line quotient (Gupta-Bleuler form) <a id="null-line-quotient"></a>

**Label:** Theorem · **id:** `null_line_quotient` · **quadrant:** true but ghost-blind/untested

*In plain words:* In a non-degenerate space with exactly one negative square, the orthogonal complement of any neutral vector is non-negative and its quotient by that vector is positive definite; a dilation that fixes the neutral line descends to a unitary operator. On finite windows the scale-character representers are negative but tend to neutral, so the quotient is reached only in the limit. On each window the quotient is positive exactly when the arithmetic side has one negative square; there is no version with a margin uniform in the window length, since the margin is squeezed between the smallest eigenvalue of W and the second eigenvalue of Z, both tending to 0. The representer value q(K+-) is about 5 to 40 times lambda_min(W)/kappa^2 (Woodbury), so it tracks the smallest eigenvalue of W.

**Core.** Null-line quotient (Gupta-Bleuler form)

**Formula.** n_- = 1, Z(e) = 0  =>  Z >= 0 on e^perp,  e^perp / e positive definite

**Numbers.** q_K_legendre · q_over_lambda_min_ratio

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), physics analogue

**TAA lemmas:** 182

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

**Relations (outgoing):**

- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

**Relations (incoming):** [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy) (analogy of); [Ramanujan's 691 as a degeneration of the pole line](#ramanujan-691-degeneration) (analogy of)

### #226 · 0.307 · Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i) <a id="apsides-gap-form"></a>

**Label:** Theorem · **id:** `apsides_gap_form` · **quadrant:** true but ghost-blind/untested

*In plain words:* In a two-dimensional orbit the radial speed is exactly TAA Lemma 157's dual-minus-adjoint gap. It vanishes at the apsides, where position and velocity are perpendicular, and it vanishes everywhere only for a circle, which is the case where the dual and the adjoint agree.

**Core.** [T] ω-dual X^∨ = −X (Hamiltonian), Euclidean adjoint Xᵀ; r·v = vᵀXv = ½⟨(Xᵀ − X^∨)v, v⟩ = vᵀ Sym(X) v (TAA Lemma 157 gap form, reference metric). Apsides (r ⊥ v) = null directions of Sym(X) (the 𝔭/squeeze part of the polar decomposition). For the preserved metric g_τ (S_t) X is skew, so the S-adjoint of X equals X^∨: the gap is identically 0 — the apsidal gap measures reference (i) vs preserved (τ) complex structure. Invariant form: e_K = tanh d_H(i, τ), e_H² = 1 − e^{−2d_H(i,τ)} (any SL₂-conjugate; 200 random, 6e−8). [N] 200 random X: 1e−12; orbit t = 1: 4 zeros of r·v per period at the 45°/135° axes. Ghost-blind (archimedean, one frame).

**Numbers.** gap identity residual 1e−12 (200 random X) · e_K = tanh d_H(i,τ): 6e−8

**Also known as:** r ⊥ v at apsides; radial speed = gap form

**Axes:** structure/frame (Ax1), physics analogue, ghost-blind

**TAA lemmas:** 161

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** The gap uses the Euclidean (reference) adjoint; for the preserved metric g_τ it is identically zero.

> ⚠ **Correction / caution.** Eccentricity is gauge-dependent: a squeeze conjugation changes e but not F, V (TAA Lemma 161, correction 4).

**Relations (outgoing):**

- same mechanism as → [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) — gap form = radial speed
- same mechanism as → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — circle ⇔ J preserved
- analogue of → [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) — per-zero gap |1 − 2β|
- lives in → [Compatible complex structure J commuting with Frobenius](#compatible-j)

**Relations (incoming):** [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) (same mechanism as); [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) (lives in); [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) (lives in)

### #239 · 0.307 · Self-dual / anti-self-dual split as push / shear <a id="self-duality-push-shear"></a>

**Label:** Theorem · **id:** `self_duality_push_shear` · **quadrant:** true but ghost-blind/untested

*In plain words:* In four Euclidean dimensions the Hodge star splits a field strength into self-dual and anti-self-dual parts. The energy is the sum of their squares and the topological density is the difference. On a Kähler surface the self-dual (1,1) part is the Kähler direction (push) and the anti-self-dual part is the primitive part (shear), so push minus shear is the Hodge-index form pointwise. Saturating the instanton (Bogomolny) bound means zero shear, which is stronger than Hodge index.

**Core.** Self-dual / anti-self-dual split as push / shear Belavin–Polyakov–Schwarz–Tyupkin, Phys. Lett. B 59 (1975) 85–87.

**Formula.** ⋆²=1 on Λ²(R⁴); F^± = (F±⋆F)/2; |F|² = |F⁺|²+|F⁻|²; F∧F = (|F⁺|²−|F⁻|²) vol; |F|² ≥ |⟨F,⋆F⟩| with equality iff F = ±⋆F; for F = aω+P (P primitive (1,1)): F∧F = (2a²−|P|²) vol

**Numbers.** identities checked on 1000 random 2-forms, error ≤ 5e−15 · real (1,1)-forms on C² form R·ω ⊕ Λ⁻ (dim 4); ω self-dual, primitive forms anti-self-dual (error 2e−16) · Lorentzian signature: ⋆² = −1 on 2-forms (exact), so the split is complex there

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), physics analogue, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** the real split needs Euclidean signature

> ⚠ **Correction / caution.** ½(E²+B²) is T⁰⁰, not a Lorentz invariant; B²−E² and E·B are indefinite (502/498 signs in 1000 samples); what is positive is u ≥ |E×B| (dominant energy)

> ⚠ **Correction / caution.** energy positivity alone carries no information: it holds for every field

**Relations (outgoing):**

- refines → [Hodge index theorem](#hodge-index)
- analogy of → [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated)
- analogy of → [Kramers–Kronig relations](#kramers-kronig)
- analogy of → [Passivity (positive real part)](#passivity)

**Relations (incoming):** [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open) (analogy of)

### #240 · 0.307 · Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal) <a id="standing-frame-so22-ads3"></a>

**Label:** Theorem · **id:** `standing_frame_so22_ads3` · **quadrant:** true but ghost-blind/untested

*In plain words:* Of seven candidate symmetry groups for the per-prime frame picture, only SO(2,2) acting on SL(2,R) does everything the animation shows; its compact twin is SO(4) on the 3-sphere. That settles the figures' standing frame, not the RH question.

**Core.** [T] Candidates evaluated: SO(4) fails K1/K6 (no boosts, ζ frames absent); SO(3,1) ≅ PSL₂ℂ fails K2/K3/K4/K7 (complex traces, loxodromics, no real G×G); SL₂ℝ alone and SU(1,1) (= SL₂ℝ by Cayley) fail K3 (conjugation orbits dim 2) and K5; GL₂ℝ² fails K5/K7; Sp(4,ℝ) ≅ Spin(3,2) not a form of so(4,ℂ), contains so(2,2) as a vector stabilizer. Minimality: the anti-diagonal is an irreducible module of the diagonal sl₂. Satake: ζ's frame (p+1)/√p = endpoint of the spherical unitary dual (trivial rep.); tempered ⇔ |t| ≤ 2 (SU(2) classes). DH: no frames (undefined). Scope: frame side only; ζ's zero-side real form is RH-equivalent.

**Numbers.** SO(2,2): 7/7; SO(4) 5/7; SO(3,1) 3/7; Sp(4,ℝ) 4/7 · orbit dims: two-sided 3, conjugation 2

**Also known as:** TAA Lemma 162 decision; AdS₃ / S³ standing frame; criteria K1–K7

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 163

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Frame side only: it does not say which real form ζ's hidden symmetry on H¹ has (that is RH).

> ⚠ **Correction / caution.** SU(1,1) and SL(2,ℂ) are not new candidates: Cayley transform; SL₂ℂ = so(3,1).

**Relations (outgoing):**

- special case of → [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) — decides TAA Lemma 162
- lives in → [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) — compact dual
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — no frames

**Relations (incoming):** [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) (lives in); [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4) (lives in)

### #242 · 0.307 · Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial <a id="consani-archimedean-cohomology"></a>

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

### #243 · 0.307 · PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form <a id="pv-ts-symplectomorphism"></a>

**Label:** Theorem · **id:** `pv_ts_symplectomorphism` · **quadrant:** true but ghost-blind/untested

*In plain words:* The first law makes the pressure–volume picture and the temperature–entropy picture two maps of the same area form: every cycle encloses the same area in both, which is why work equals heat. Work is an area (a flux), not a cohomology class.

**Core.** [T] dU = T dS − P dV ⇒ 0 = d(dU) = dT∧dS − dP∧dV, so ω := dT∧dS = dP∧dV on the (fixed-N, 2-dim) state surface: (P,V) and (T,S) are two Darboux charts of one area form, ∂(T,S)/∂(P,V) = 1, and the four Maxwell relations are this identity in the charts (P,S), (T,V), (P,T), (S,V) (Wikipedia 'Maxwell relations' §Jacobians, opened; Ritchie AJP 36 (1968) 760 not opened). Equal area holds for every region, not only cycles; orientation preserved (engine cycles clockwise in (V,P) and in (S,T)). [N] ideal and vdW (a = 1, b = 0.2) gases: Jacobian 1 ± 2e−9 at 200 random points; ellipse cycle W = ∮PdV = 1.272345 = Q = ∮TdS = π·0.9·0.45; Maxwell (∂T/∂P)_S = (∂V/∂S)_P = 0.8 (ideal), 0.9 (vdW). [T] Cochains vs cohomology: P dV and T dS are not closed; both are primitives of ω (d(PdV) = d(TdS) = ω) and differ by dU (first law). State space is contractible, so H¹ = 0: work over a cycle is the flux of ω through the enclosed region (Stokes), not a cohomology class. The honest cohomology in the arithmetic picture: d log ξ is closed on ℂ∖{zeros} (the Fisher zeros are the holes); periods 2πi·multiplicity [N: ζ box at 14.13 → 1.0; DH box around ρ₁ → 1.0; box around ρ₁ and 1−ρ̄₁ → 2.0]: counts, ghost-blind.

**Formula.** dT∧dS = dP∧dV; ∮P dV = ∮T dS

**Numbers.** Jacobian 1 ± 2e−9 (ideal, vdW) · W = Q = 1.272345 (ellipse cycle) · periods of d log Λ: 1.0, 1.0, 2.0

**Also known as:** Maxwell relations as a Jacobian

**Axes:** structure/frame (Ax1), ghost-blind, physics analogue

**TAA lemmas:** 159

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** It is one 2-form in two charts, valid where (P,V) and (T,S) are both coordinates (fails on coexistence lines).

> ⚠ **Correction / caution.** Work is not a cohomology class on a contractible state space; first law = [δQ − δW] = 0.

**Relations (outgoing):**

- analogue of → ["Cocycles give structure, not sign"](#cocycle-principle) — cocycles give structure, not sign
- same mechanism as → [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) — Legendre charts of one surface
- analogue of → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — ω on the state surface; g = Ruppeiner
- lives in → [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state)

### #245 · 0.307 · λ₂ is monotone under nested windows (Cauchy interlacing) <a id="lambda2-monotone-nested-windows"></a>

**Label:** Theorem · **id:** `lambda2_monotone_nested_windows` · **quadrant:** true but ghost-blind/untested

*In plain words:* On a fixed grid, the window spaces are nested: the test functions for a window of length ℓ are among those for any longer window. By Cauchy interlacing every eigenvalue of the arithmetic side Z_ℓ, in particular the second one λ₂, is non-increasing in ℓ. So "λ₂ never reaches 0 as the window passes each log p" is the same as "the infimum of λ₂ over all windows is ≥ 0": the decisive statement is a limit, not a sequence of events at the points log p. The theorem holds for every form, including Davenport–Heilbronn, so it locates where RH is decided rather than deciding it.

**Core.** λ₂ is monotone under nested windows (Cauchy interlacing). From the TAA research notes of 29 Oct 2026 (window model of TAA Lemma 182; not yet in a lemma).

**Formula.** V_ℓ ⊂ V_ℓ′ (ℓ < ℓ′) ⇒ λ_k(Z_ℓ′) ≤ λ_k(Z_ℓ) for every k; RH ⇔ inf_ℓ λ₂(Z_ℓ) ≥ 0 (by the ghost count; circular as a route)

**Numbers.** ζ, box grid h = 0.02: the largest step-to-step increase of λ₂ on ℓ ∈ [0.3, 6] is −3.6e−6 < 0 · h = 0.005: the step in λ₂ across log 7, log 11, log 13 and log 16 is at most 1.6 times the median step (no jump at log p) · base case: λ₂ > 0 for ℓ ∈ (0.2295, log 2] (TAA Lemma 182)

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), ghost-blind

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Monotonicity needs nested sections (a fixed grid); on families with a fixed number of boxes the sections are not nested.

**Relations (outgoing):**

- refines → [RH as a negative-square count (restatement)](#ghost-count-rh-restatement)
- refines → [One Perron mode against the pole](#pole-perron-one-mode)

**Relations (incoming):** [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) (uses)

### #265 · 0.267 · De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p} <a id="dbn-local-flow-fv-sweep"></a>

**Label:** Theorem · **id:** `dbn_local_flow_fv_sweep` · **quadrant:** true but ghost-blind/untested

*In plain words:* Running the heat flow on a single Euler factor changes only its trace, which shrinks or grows exponentially, while the product of the two Frobenius roots stays p. So the flow slides the pair along the F/V sweep.

**Core.** De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}

**Formula.** P_p(½+iz) = e^{−iz log p}(2cos(z log p) − a/√p); H_t = 2e^{t log²p}cos(z log p) − a/√p

**Numbers.** forward: z → π/(2 log p), F,V → ±i√p (k = 2 point) · inversion: flowed 1/P_p diverges for t > 0 (weight 2·10^275 at k = 70, t = 0.05)

**Axes:** structure/frame (Ax1), phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy)
- localises → [de Bruijn–Newman constant Λ](#debruijn-newman)

**Relations (incoming):** [Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k)](#coupled-coil-hasse) (restates); [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant) (feeds); [Fourth roots: a_p = 0 (supersingular) gives r = 0 over 𝔽_p and the cusp r = 1 over 𝔽_{p²} (a_{p²} = −2p)](#fourth-roots-supersingular) (illustrates); [Three lenses on one Euler factor (analytic factor, det(1 − Frob X), oscillator 2cos(z log p)) carry the same dBN flow; they separate only for products](#three-lenses-one-flow) (restates)

### #266 · 0.267 · Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁) <a id="four-squares-eisenstein-lift"></a>

**Label:** Theorem · **id:** `four_squares_eisenstein_lift` · **quadrant:** true but ghost-blind/untested

*In plain words:* Counting the ways to write n as four squares gives exactly ζ(s)ζ(s−1), so ζ's per-prime frames are the 'trivial' part of the quaternion picture. Genuine wave-like (cusp) pieces only show up for other quaternion lattices, for example one tied to the curve 11a1.

**Core.** [T] Jacobi r₄(n) = 8Σ_{d|n,4∤d} d (n ≤ 3000 exact); Dirichlet identity coefficientwise (n ≤ 3000) and numerically at s = 4, 5, 6.5 (1e−11). θ⁴ ∈ M₂(Γ₀(4)), all Eisenstein. Hurwitz order: #norm n = 24σ(n), n odd. B = (−1,−11)_ℚ (ramified at 11, ∞), maximal order O = ℤ⟨1, i, (1+j)/2, i(1+j)/2⟩, norm form Q ⊕ Q with Q = x² + xy + 3y²; θ_O = 1 + (12/5)Σ(σ(n) − 11σ(n/11))qⁿ + (8/5) η(z)²η(11z)² (n ≤ 300, exact). [C] Eichler 1954 Arch. Math. 5 355–366 (Brandt/basis problem; bibliographic). [A] 'definite energy' (TAA Lemma 161) ↔ definite quaternion algebra (compact quotient).

**Formula.** Σ r₄(n) n^{−s} = 8(1−4^{1−s}) ζ(s) ζ(s−1); θ_O = E + (8/5) f₁₁ₐ₁

**Numbers.** B3 rel. err 1.2e−11 · θ_O − E = (8/5) f₁₁ₐ₁ to n = 300

**Also known as:** Jacobi four-square theorem; r₄(n); Eisenstein vs cusp in theta series

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), ghost-blind, numerics/certificate

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Four squares has NO cusp part (dim S₂(Γ₀(4)) = 0).

> ⚠ **Correction / caution.** ζ sits on the Eisenstein (non-compact, boost) side; the quaternion lift does not place ζ's zeros in a compact setting.

**Relations (outgoing):**

- same mechanism as → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) — ζ(s)ζ(s−1) frames at φ = ½ log p
- lives in → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct)
- analogue of → [Cusp forms & Petersson positivity](#cusp-forms-petersson) — cusp part of θ_O
- lives in → [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift)

**Relations (incoming):** [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (same mechanism as); [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) (lives in)

### #267 · 0.267 · Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics) <a id="fundamental-domain-three-phases"></a>

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

**Relations (incoming):** [Epstein zeta no-go](#epstein) (lives in); [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) (lives in); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (same mechanism as)

### #272 · 0.267 · Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4) <a id="ks-quaternion-lift"></a>

**Label:** Theorem · **id:** `ks_quaternion_lift` · **quadrant:** true but ghost-blind/untested

*In plain words:* Squaring a quaternion turns the Kepler problem in 3D into a perfectly round oscillator in 4D. Bound orbits become ordinary oscillations and unbound ones become an upside-down oscillator, which is the same switch as a Wick rotation.

**Core.** [T] KS (J. reine angew. Math. 218 (1965) 204–219): x = q i q̄, fibre q ↦ q e^{iα}; dx kills the fibre, and on the horizontal space (⟨q i, q′⟩ = 0) dx = 2|q| × isometry (5e−10). With ds = dt/r: q″ = −ω²q, ω² = −E/2, |q′|² + ω²|q|² = μ/2 (coupling-constant metamorphosis; ΔE 1e−10, Kepler ẍ = −μx/r³ to 4e−7). E > 0: inverted oscillator → hyperbola (2e−6). 2D case = Levi-Civita/Bohlin z ↦ z² (TAA Lemma 161): e_K = e_H²/(2 − e_H²). u(4) (16 generators) ∩ commutant of the constraint = 8-dim u(2)⊕u(2), derived algebra 6 = su(2)⊕su(2) ≅ so(4) (bound Kepler); the two u(1) = constraint and oscillator H. [A] J. W. McGreevy. Ghost-blind (archimedean).

**Formula.** x = q i q̄; |x| = |q|²; q″ = (E/2) q; ω² = −E/2

**Numbers.** ΔE 1.3e−10 (E = −0.5) · commutant dim 8, derived 6

**Also known as:** Hopf map; Levi-Civita/Bohlin in 4D; coupling-constant metamorphosis

**Axes:** structure/frame (Ax1), physics analogue, ghost-blind

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The 4D oscillator symmetry is U(4); only the su(2)⊕su(2) commuting with the constraint descends to Kepler.

> ⚠ **Correction / caution.** Spelling: Kustaanheimo–Stiefel.

**Relations (outgoing):**

- same mechanism as → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) — ω → iω is cos θ → cosh φ
- special case of → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) — SO(4) made manifest
- lives in → [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) — Bohlin z² = 2D KS

**Relations (incoming):** [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) (lives in); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (same mechanism as)

### #275 · 0.267 · Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner) <a id="push-shear-balance"></a>

**Label:** Theorem · **id:** `push_shear_balance` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over a whole surface the isotropic and shear parts of a Hessian balance exactly; any surplus is a boundary or curvature term.

**Core.** Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)

**Formula.** ∫(τ/2)²−∫|H°|² = ½∮[κ|∇u|² − 2u_s∂_s u_n] ; = ½∫K|∇u|² (closed)

**Numbers.** disk x³+xy²: B=4π · disk x²y+y⁴−x: B=−2π · S² Y₂⁰: 48π/5

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The sign is controlled only with Dirichlet or Neumann data on convex domains (Miranda–Talenti).

**Relations (outgoing):**

- refines → [Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear](#trace-shear-budget)
- feeds → [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts)
- tested by → [Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻](#talenti-template-test)

**Relations (incoming):** [Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel](#anisotropic-part-weil) (refines); [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading) (illustrates)

### #276 · 0.267 · Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts <a id="quartet-capacity-sp4"></a>

**Label:** Theorem · **id:** `quartet_capacity_sp4` · **quadrant:** true but ghost-blind/untested

*In plain words:* An off-line zero shows up as a group of four eigenvalues. Whether a symmetry group can produce such quartets depends on the representation, not on whether the group is compact; inside the 4D symplectic group they appear exactly when two oscillations of opposite energy sign collide.

**Core.** [N] random generators: quartet fractions 0, 0,.394,.354, 1.0; boost 0.3 ⊗ rotation 2 gives ±0.3 ± 2i exactly. Krein (sp(4,ℝ)): equal frequencies, coupling.05: opposite signs max|Re|.025, same 4e−17; instability band ω₂ ∈ [.951, 1.050]. so(2,2) = stabilizer of a vector in so(3,2) (dim 6, Killing (4,2)). Correction TAA Lemma 163, correction 4: 'split frame group ⇒ no ghosts' is false.

**Numbers.** quartet fractions 0/0/.394/.354/1.0 · band [.951, 1.050]

**Also known as:** Sp(4,ℝ) quartet group; Krein signature

**Axes:** structure/frame (Ax1), ghost-blind, sign/positivity (Ax2)

**TAA lemmas:** 163

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- lives in → [Krein collisions (how ghosts are born)](#krein-collision)
- analogue of → [Ghost quartet ½ ± δ ± iγ](#ghost-quartet)
- lives in → [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) — so(2,2) ⊂ sp(4,ℝ)

**Relations (incoming):** [Krein collisions (how ghosts are born)](#krein-collision) (lives in); [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) (lives in)

### #278 · 0.267 · Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V) <a id="dbn-deficit-time-to-cusp"></a>

**Label:** Theorem · **id:** `dbn_deficit_time_to_cusp` · **quadrant:** true but ghost-blind/untested

*In plain words:* Each prime's Frobenius is a rotation of the sphere, so it has a cone angle. The flow sharpens the cone backward until it becomes a cusp, exactly at the local Newman time. Forward it relaxes toward a half-turn. Past the cusp the rotation becomes a boost.

**Core.** Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)

**Formula.** SO(3) angle 2θ̄, θ̄ = arccos(|a|/2√p); t_k = log(cos θ̄₀/cos(π/k))/log²p; 2η = 2 arccosh(|tr|/2) = log(F/V)

**Numbers.** δ(0): (5,3) 264.3°, (7,−4) 278.2°, (11,6) 309.5° · fake (5,5): 2η = 0.962 · ζ paired factor: boost length log p

**Axes:** structure/frame (Ax1), reference/pole/cusp, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The time-to-cusp restates Andrade–Chang–Miller Lemma 3.18; the deficit reading was not found there or in Chang et al.

**Relations (outgoing):**

- restates → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)
- refines → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation)
- mirror of → [Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward](#dbn-bohlin-decay)

**Relations (incoming):** [Platonic-point deficits 2π(1 − 1/k) are orbifold cone deficits of S²/G, not Descartes vertex defects; orbifold Gauss–Bonnet: cone deficits + area = 720° (icosahedral 708° + 12°, χ_orb = 1/30)](#orbifold-vs-descartes-deficits) (feeds)

### #279 · 0.267 · Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p <a id="dbn-product-cross-term"></a>

**Label:** Theorem · **id:** `dbn_product_cross_term` · **quadrant:** true but ghost-blind/untested

*In plain words:* The flow of a product is not the product of the flows. The extra terms are explicit, and they decide the product's threshold, which the local thresholds do not determine.

**Core.** Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p

**Formula.** cross-weights e^{±2t log p log q}, as in Dobner's ζ_t

**Numbers.** Hasse factors at distinct primes: Λ_global = 0 (numerical, ±5·10⁻⁴) vs max Λ_p −0.0174 … −0.119 · fake (5,5)×(11,6): 0.0356 < 0.0431 · same p (5,3)×(5,1): −0.0132 vs −0.1541 · 11a1 truncations (2–6 primes): Λ = 0

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- obstructs → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)

**Relations (incoming):** [Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q](#burgers-local-toeplitz) (feeds); [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero) (refines); [One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction](#prime-clocks) (feeds)

### #282 · 0.267 · Kaluza–Klein circles, the infinite torus, and adelic solenoids <a id="kk-circle-and-adelic-solenoids"></a>

**Label:** Theorem · **id:** `kk_circle_and_adelic_solenoids` · **quadrant:** true but ghost-blind/untested

*In plain words:* A Kaluza–Klein circle gives a complex structure on its charged modes only. The pseudosphere is a warped circle of radius e^{−u}, and only the neutral (constant-term) mode reaches the cusp, where the scattering coefficient Λ(2s−1)/Λ(2s) carries ζ. The per-prime phases p^{−it} fill the infinite torus ∏S¹, the dual of the multiplicative group of positive rationals. That torus differs from the solenoid 𝔸/ℚ, which is the dual of the additive rationals; the p-adic solenoid is the inverse limit of S¹ under z ↦ z^p. The product formula makes ℚ^× preserve Haar measure, so the compatible structure is an invariant measure, not an invariant metric. The expected dynamical system for Spec ℤ (three-dimensional, orbits of length log p) has not been constructed.

**Core.** Kaluza–Klein circles, the infinite torus, and adelic solenoids

**Formula.** Σ_p = (ℝ×ℤ_p)/ℤ = lim←(S¹, z↦z^p); 𝔸_ℚ/ℚ = (ℝ×Ẑ)/ℤ = ℚ^∨; ∏_p S¹ = (ℚ^×_{>0})^∨; C_ℚ = ℝ_{>0}×Ẑ^×

**Numbers.** warped circle R = e^{−u}: K = −1 · Kronecker on T³ (2,3,5): bins within 0.9% · periods 2π/log p: 9.06, 5.72, 3.90, 3.23

**Axes:** structure/frame (Ax1), physics analogue, ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings)
- refines → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric) (refines); [Beta integral, Maslov dequantization and entropy](#beta-dequantization-entropy) (analogy of)

### #286 · 0.267 · Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward <a id="dbn-bohlin-decay"></a>

**Label:** Theorem · **id:** `dbn_bohlin_decay` · **quadrant:** true but ghost-blind/untested

*In plain words:* Under the forward flow every orbit becomes more circular at an exact exponential rate. The ghost onset is the moment it becomes parabolic. The picture in the root dictionary is different (see TAA Lemma 179).

**Core.** Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward

**Formula.** e_K(t) = |a_eff(t)|/2√p

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity)
- mirror of → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation)

**Relations (incoming):** [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp) (mirror of)

### #288 · 0.267 · (τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|² <a id="exactness-monge-ampere"></a>

**Label:** Theorem · **id:** `exactness_monge_ampere` · **quadrant:** true but ghost-blind/untested

*In plain words:* Push−shear is exact in flat space; curvature is the non-exact leftover.

**Core.** (τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- explains → [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece)

**Relations (incoming):** [The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)](#edge-boundary-cycle) (explains); [Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned](#serre-derivative-analogy) (analogous to)

### #291 · 0.267 · Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min) <a id="local-dbn-slack"></a>

**Label:** Theorem · **id:** `local_dbn_slack` · **quadrant:** true but ghost-blind/untested

*In plain words:* One prime survives a definite amount of backward heat flow; a product of two primes survives none, because near-coincident zeros collide.

**Core.** Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)

**Formula.** s_p = log(2√p/|a|)/log²p; s(product) = 0; t_c = −d²/8

**Numbers.** s_5(3)=0.15413 · s_7(-4)=0.07389 · s_11(6)=0.01745

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** A correction term changes the function; a non-circular form is an exact ledger (Open).

**Relations (outgoing):**

- restates → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)
- feeds → [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero)

**Relations (incoming):** [Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z²](#slack-ledger-cf) (refines)

### #296 · 0.267 · On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH <a id="chirality-star-gamma5-hodge-index"></a>

**Label:** Theorem · **id:** `chirality_star_gamma5_hodge_index` · **quadrant:** true but ghost-blind/untested

*In plain words:* Over the complex numbers, the polarization is the self-dual (right-handed) direction and the primitive classes are anti-self-dual. Curvature produces the topological signature through its Weyl part, but that signature is zero for every such surface and does not see Frobenius.

**Core.** On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH The signature is constant (LeBrun, arXiv:2203.02528, eq. (2)).

**Formula.** b⁺ = 2h^{2,0} + 1 = 3, b⁻ = h^{1,1} − 1 = 3

**Numbers.** ρ = 3 (non-CM), 4 (CM); over F̄_q supersingular ρ = 6 > h^{1,1}

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity)

**Relations (incoming):** [Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance](#thermodynamic-j-direction) (feeds)

### #298 · 0.267 · One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction <a id="prime-clocks"></a>

**Label:** Theorem · **id:** `prime_clocks` · **quadrant:** true but ghost-blind/untested

*In plain words:* The heat flow advances each frequency at a rate set by its square. On its own clock, every prime with the same angle reaches the cusp at the same moment. When two primes combine, their clocks interact, which is why products behave differently.

**Core.** One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction

**Formula.** e^{iωz} ↦ e^{ω²t}; Wick t = −is: iH_s = −H_zz, ω = k², v_g = 2k

**Numbers.** θ̄₀ = π/5: Λ_p = −0.0818, −0.0369, −0.0100, −0.0025 at p = 5, 11, 101, 10007

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** “Proper time” is an Analogy only.

**Relations (outgoing):**

- feeds → [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term)
- restates → [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant)

### #299 · 0.267 · Sector map w = e^{iπs/2} <a id="sector-map-w"></a>

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

### #300 · 0.267 · Elliptic/parabolic/hyperbolic as |tr M| = 2r < = > 2 for normalised Frobenius; only SO(2) compact; in RP² the parabola is tangent to the line at infinity (zero-margin edge as tangency); r = 1 forces scalar Frobenius for elliptic curves <a id="conic-compactness"></a>

**Label:** Theorem · **id:** `conic_compactness` · **quadrant:** true but ghost-blind/untested

*In plain words:* The parabola is not compact.

**Core.** Elliptic/parabolic/hyperbolic as |tr M| = 2r < = > 2 for normalised Frobenius; only SO(2) compact; in RP² the parabola is tangent to the line at infinity (zero-margin edge as tangency); r = 1 forces scalar Frobenius for elliptic curves

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- refines → [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading)

### #306 · 0.267 · Platonic-point deficits 2π(1 − 1/k) are orbifold cone deficits of S²/G, not Descartes vertex defects; orbifold Gauss–Bonnet: cone deficits + area = 720° (icosahedral 708° + 12°, χ_orb = 1/30) <a id="orbifold-vs-descartes-deficits"></a>

**Label:** Theorem · **id:** `orbifold_vs_descartes_deficits` · **quadrant:** true but ghost-blind/untested

*In plain words:* There are two different 'deficit angles of the Platonic solids'. The ones on the F/V sweep belong to the quotient of the sphere by the symmetry group. The corners of the solids themselves have smaller defects. Both add up to 720° once the smooth curvature is counted.

**Core.** Platonic-point deficits 2π(1 − 1/k) are orbifold cone deficits of S²/G, not Descartes vertex defects; orbifold Gauss–Bonnet: cone deficits + area = 720° (icosahedral 708° + 12°, χ_orb = 1/30)

**Formula.** Σ 2π(1−1/k_i) + 4π/|G| = 4π; Descartes: Σ vertex defects = 4π

**Numbers.** Descartes defects: 180°, 90°, 120°, 36°, 60°

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- feeds → [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp)

### #307 · 0.267 · Ruled quadric through a saddle: null lines, signature (1,1) <a id="ruled-quadric-null-lines"></a>

**Label:** Theorem · **id:** `ruled_quadric_null_lines` · **quadrant:** true but ghost-blind/untested

*In plain words:* x²+y²−t² = c has two rulings for c > 0, collapsing to the cone at c = 0; the quadric is P¹×P¹ with intersection form of signature (1,1), the C×C of Weil's proof for C = P¹. Its lines are null (zero proper time); proper time lives on the two-sheet hyperboloid. The mutual moment of two lines is symmetric, of constant sign within a ruling and zero across rulings, so no assignment of primes to lines reproduces Legendre symbols, which are antisymmetric on primes ≡ 3 mod 4.

**Core.** Ruled quadric through a saddle: null lines, signature (1,1)

**Formula.** moment(ℓ_φ1^ε, ℓ_φ2^ε) = 2ε(1 − cos(φ1 − φ2)); moment across rulings = 0

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** a 2D Morse saddle has a separatrix of two lines, not a cone; the cone needs an added Lorentzian coordinate

> ⚠ **Correction / caution.** x² − t² = (x−t)(x+t) is indefinite, not a Gram form

**Relations (outgoing):**

- instance of → [Hodge index theorem](#hodge-index)

### #308 · 0.267 · so(4)=su(2)⊕su(2): Λ± are commuting rotation subalgebras; D·D=‖D⁺‖²−‖D⁻‖² <a id="so4-chirality-split"></a>

**Label:** Theorem · **id:** `so4_chirality_split` · **quadrant:** true but ghost-blind/untested

*In plain words:* Both chiral halves generate rotations; ⋆ referees the sign.

**Core.** so(4)=su(2)⊕su(2): Λ± are commuting rotation subalgebras; D·D=‖D⁺‖²−‖D⁻‖²

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- corrects → [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading)

### #310 · 0.267 · Three lenses on one Euler factor (analytic factor, det(1 − Frob X), oscillator 2cos(z log p)) carry the same dBN flow; they separate only for products <a id="three-lenses-one-flow"></a>

**Label:** Theorem · **id:** `three_lenses_one_flow` · **quadrant:** true but ghost-blind/untested

*In plain words:* At a single prime the analytic factor, the Frobenius polynomial and the oscillator are the same equation, and the flow acts on all three in the same way.

**Core.** Three lenses on one Euler factor (analytic factor, det(1 − Frob X), oscillator 2cos(z log p)) carry the same dBN flow; they separate only for products

**Formula.** H(z) = 0 ⇔ e^{iz log p} ∈ spec(Frob/√p)

**Axes:** structure/frame (Ax1), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- restates → [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep)

### #322 · 0.240 · Riemann-Roch sorts the two conditions <a id="riemann-roch-sorting"></a>

**Label:** Restatement · **id:** `riemann_roch_sorting` · **quadrant:** RH-sharp

*In plain words:* Riemann-Roch on the curve (and its arithmetic version via theta sums and Poisson summation) controls the poles and the functional equation: the pole channel. It is blind to off-line zeros. Positivity on the primitive part needs Riemann-Roch on the surface (equality plus effectivity gives Hodge index), and the needed surface over the integers collapses. Arithmetic GRR has an archimedean correction (the R-genus, built from zeta'(-m)) that parallels the archimedean term only by analogy.

**Core.** Riemann-Roch sorts the two conditions

**Formula.** h⁰(D) - h⁰(κ-D) = deg D - ½ log|Δ|

**Axes:** structure/frame (Ax1), Spec ℤ gap

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.240

**Relations (outgoing):**

- refines → [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece)

### #334 · 0.212 · SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G) <a id="su2xsu2-peter-weyl-surface"></a>

**Label:** Analogy · **id:** `su2xsu2_peter_weyl_surface` · **quadrant:** background

*In plain words:* The four-dimensional rotation group is two copies of SU(2), one acting from the left and one from the right, so the 3-sphere behaves like a 'product' with a diagonal. That mirrors the curve-times-curve surface Weil used, and on a compact group the positivity Weil needed comes for free. The catch is that ζ's own frames are boosts, not rotations.

**Core.** [T] (g,h) ↦ L_g R_{h⁻¹} ∈ SO(4), kernel ±(1,1), so(4) = su(2)_L ⊕ su(2)_R; diagonal conjugation preserves Re x = cos θ (latitude = Sato–Tate class). Peter–Weyl: characters U_n orthonormal for Sato–Tate (6e−15); matrix coefficients (MC 1.4e−3). Weil side: Gram of {pt×E, E×pt, Δ, Γ_F} on E×E (11a1) has one positive eigenvalue, det = a² − 4p (Hodge index ⇔ |a| ≤ 2√p ⇔ m² − a mn + p n² ≥ 0, the TAA Lemma 152 norm conic); fake a = 8 at p = 13 gives two positive eigenvalues. #E(F_p) = p + 1 − a_p (Lefschetz). [A] 'SU2 x SU2 … surface on SpecZ x SpecZ': compactness gives definiteness for free, but SU(2) is the group of an elliptic curve's frames; ζ's frames are boosts. [O] a compact G×G whose diagonal sees ζ's zeros. [C] Connes–Consani, The Arithmetic Site (C. R. 352 (2014) 971–975): Frobenius correspondences realized in the square of the arithmetic site.

**Numbers.** Sato–Tate Gram = I to 6e−15 · det Gram = a² − 4p · fake a = 8 > 2√13: n₊ = 2

**Also known as:** Peter–Weyl as Künneth; compact product surface

**Axes:** structure/frame (Ax1), sign/positivity (Ax2), Spec ℤ gap, ghost-blind

**TAA lemmas:** 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

> ⚠ **Correction / caution.** Analogy only: no compact G×G is known whose diagonal sees ζ's zeros (Open).

> ⚠ **Correction / caution.** Never name the missing cohomology: it is Deninger's conjectured cohomology (MP0–MP4).

**Relations (outgoing):**

- analogue of → [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) — compact model of the square
- analogue of → [Hodge index theorem](#hodge-index) — Haar positivity ↔ Hodge index
- lives in → [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) — Γ_F ↔ translated diagonal
- analogue of → [Connes–Consani sites](#connes-consani) — square of the arithmetic site
- lives in → [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3)

**Relations (incoming):** [Hodge index theorem](#hodge-index) (analogue of); [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) (analogue of); [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) (lives in); [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) (lives in); [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) (lives in)

## Axis: phase/unitarity (Ax3) <a id="axis-phase-unitarity-ax3"></a>

### #58 · 0.540 · Zeros as Breit–Wigner resonances (line shapes, cusp doublets) <a id="breit-wigner-resonances"></a>

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

### #64 · 0.540 · Arithmetic unitarity ("RH = unitarity") <a id="arith-unitarity"></a>

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

**Relations (incoming):** [Deninger’s foliated program](#deninger) (analogue of); [Hilbert–Pólya](#hilbert-polya) (same mechanism as); [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (analogue of); [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) (analogue of); [Half-density normalization |x|^{½}](#half-density) (same mechanism as); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (analogue of)

### #73 · 0.540 · Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼ <a id="eisenstein-resonances-rho-half"></a>

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

### #111 · 0.451 · Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution <a id="boost-rotation-modular-kms"></a>

**Label:** Heuristic · **id:** `boost_rotation_modular_kms` · **quadrant:** sharp but interpretive

*In plain words:* A boost never becomes a rotation by moving it around space. It becomes one when time is made imaginary, and then the required 2π period is exactly thermal equilibrium at temperature a/2π. ζ is the partition function of a gas of primes, so the closest precise version of the idea is thermal.

**Core.** [T] Thomas–Wigner: boosts 0.9 (x) and 0.7 (y) compose to boost × rotation by 16.1546° = 2 arctan(tanh(η₁/2) tanh(η₂/2)). Rindler (t,x) = ρ(sinh η, cosh η) → ρ(sin τ, cos τ), period 2π. [C] Bisognano–Wichmann J. Math. Phys. 16 (1975) 985–1007, 17 (1976) 303–321; Unruh Phys. Rev. D 14 (1976) 870–892; Bost–Connes Selecta 1 (1995) 411–457 (abstract: partition function ζ, phase transition at β = 1); Julia 1990; Spector CMP 127 (1990) 239–252. Corrections: a boost subgroup is non-compact on any manifold (dS₃ isometry group SO(3,1) non-compact); K → iK is a change of real form, not a transport; holonomy on Riemannian S³ lies in SO(3) because the metric is definite. [H] 'boosts made global rotations' = thermal (KMS) periodicity, not topology. [O] does a KMS/modular structure give Krein definiteness for ζ? DH: no Euler product ⇒ no primon gas (ghost-sensitive point). TAA Lemma 164: the compact pieces are J (ℤ/2) and the KMS imaginary-time circle; the real-time modular group is ℝ (BC: n^{it}, not periodic).

**Numbers.** Wigner angle 16.1546° · Euler product vs ζ(2): 4.6e−6 (p < 2·10⁴)

**Also known as:** Thomas–Wigner rotation; Unruh/KMS; modular flow; primon gas

**Axes:** phase/unitarity (Ax3), physics analogue, ghost-sensitive

**TAA lemmas:** 162, 164

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 0.7 · specificity 1.0 · tractability 0.5 · evidence 0.6 → priority 0.451

> ⚠ **Correction / caution.** Compactness of a one-parameter subgroup is intrinsic.

> ⚠ **Correction / caution.** KMS periodicity is a property of the state, not of the group.

**Relations (outgoing):**

- lives in → [Bost–Connes KMS states](#kms-bost-connes)
- same mechanism as → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) — p^{−s} = boost × rotation
- analogue of → [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) — Euclidean periodicity
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — no Euler product ⇒ no primon gas
- lives in → [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost)
- lives in → [Epstein zeta no-go](#epstein) — (Epstein ghost)

**Relations (incoming):** [Epstein zeta no-go](#epstein) (lives in); [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) (special case of); [Bost–Connes KMS states](#kms-bost-connes) (same mechanism as)

### #122 · 0.420 · Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function) <a id="arithmetic-response-passivity-32a1"></a>

**Label:** Restatement · **id:** `arithmetic_response_passivity_32a1` · **quadrant:** RH-sharp

*In plain words:* For the CM curve y² = x³ − x (conductor 32, root number +1) take Z = Λ′/Λ of the completed L-function, critical line Re s = 1. On the line Z is purely imaginary (lossless, phase ±90° everywhere), by the functional equation and real coefficients. Lagarias's theorem on admissible zero sets gives: GRH for this L-function holds iff Re Z > 0 on Re s > 1, i.e. the response is passive. Under GRH, Z(1+w) = Σ 2w/(w²+γ²) over zeros γ > 0, one lossless resonator per zero; off the line each has damping 2(σ−1), and an off-line zero would be a gain resonator. The absorption peaks near the line sit at the zeros, not at primes. Inert primes enter only at second order, with their own poles on Re s = 1/2. No finite Euler product is passive near the line. Kramers–Kronig and the 90° crossing hold for gain media too, so they do not supply the sign. This restates GRH; it does not prove it.

**Core.** Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)

**Formula.** Z(s)=Λ′/Λ(s), Λ(s)=32^{s/2}(2π)^{−s}Γ(s)L(E,s); Z(1+it) ∈ iR; GRH ⟺ Re Z>0 on Re s>1; Z(1+w)=Σ_{γ>0} 2w/(w²+γ²); inert factor log-derivative 2 log p·p^{1−2s}/(1+p^{1−2s})

**Numbers.** min_t≤40 Re Z(σ+it) ≈ 0.468(σ−1) for 1.005 ≤ σ ≤ 2, attained at t = 0, slope 2Σγ^{−2} = 0.4682 · |Re Z| on the line ≤ 1.3e−47 for t ≤ 40 · 33 absorption peaks at σ = 1.02 match the 33 zeros in [0.5, 39.5] within 0.0019 · Foster sum over 439 zeros below 300 plus tail matches Z to relative error ≤ 8e−5 · finite Euler product X = 10⁴: gain on 34% of the t-grid at σ = 1.005, none for σ ≥ 1.3 · synthetic zero moved to β = 1.15: gain exactly in 1 < σ < 1.15

**Axes:** phase/unitarity (Ax3), restatement ⇔ RH, physics analogue

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.5 (nearest gap: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)) · sensitivity 1.0 · specificity 1.0 · tractability 0.3 · evidence 1 → priority 0.420

**Relations (outgoing):**

- instance of → [Passivity (positive real part)](#passivity)
- refines → [Lagarias/Hinkkanen criterion](#lagarias)
- counterexample to sufficiency of → [Kramers–Kronig relations](#kramers-kronig)
- analogy of → [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality)
- refines → [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece)

**Relations (incoming):** [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix) (analogy of); [The critical-line wave: Hardy Z and the Riemann–Siegel phase](#hardy-z-critical-line-wave) (analogy of)

### #125 · 0.420 · Why the area is π: the circle in every zero count (Basel as common origin) <a id="circle-pi-in-zero-counts"></a>

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

### #169 · 0.360 · Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept <a id="birman-krein-spectral-shift"></a>

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

**Relations (incoming):** [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) (same mechanism as); [Lax–Phillips scattering](#lax-phillips) (same mechanism as); [Time delay (Wigner)](#time-delay) (same mechanism as); [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) (same mechanism as); [E₂* as the derivative of the Kronecker limit (cusp-scattering footprint)](#kronecker-limit-e2star) (analogue of)

### #173 · 0.360 · Two partners of a zero (duality vs conjugation) <a id="two-partners"></a>

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

### #187 · 0.347 · Automorphy defect (TAA Lemma 144) <a id="automorphy-defect"></a>

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

### #190 · 0.325 · Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein) <a id="euler-factor-wick-rotation"></a>

**Label:** Theorem · **id:** `euler_factor_wick_rotation` · **quadrant:** true but ghost-blind/untested

*In plain words:* Each prime's Euler factor is one frame. Changing cos θ to cos(iφ) = cosh φ slides it from bounded oscillation, through the meeting point, to exponential growth. The far end of the slide is exactly the Euler factor of ζ(s)ζ(s−1). An Euler factor never vanishes, so this moves poles, not zeros.

**Core.** [T] 1/(1 − tu + u²) = Σ U_k(t/2)u^k, u = p^{½−s} (arithmetic s, weight 2) = p^{−s'} (analytic). Elliptic t = 2cos θ: c_k = sin((k+1)θ)/sin θ, poles e^{±iθ}; parabolic t = 2: c_k = k + 1, double pole u = 1; hyperbolic θ = iφ: c_k = sinh((k+1)φ)/sinh φ, poles e^{±φ}, Re s = ½ ∓ φ/log p. φ = ½ log p: t = √p + 1/√p, factor = 1/((1 − p^{−s})(1 − p^{1−s})), Hecke eigenvalue 1 + p (weight-2 Eisenstein). sl₂: tr exp X = 2cos √det X (det X = θ², 0, −k²). [T] No Euler factor vanishes; a convergent product of non-zero factors is non-zero (zeros only after continuation). [N] errors ≤ 5e−30; ζ(s)ζ(s−1) identity 3.4e−31; sl₂ 6.3e−14 (300 X). |u| = 1 is local unitarity (tempered), NOT the critical line (Re s = 1 arithmetic) (TAA Lemma 160, correction 3). Cusp forms elliptic (Eichler–Shimura + Weil; Deligne); Maass: Ramanujan open, Kim–Sarnak 7/64 bounds the hyperbolic excursion. [A] physics Wick rotation rotates time, here the angle/frequency is rotated (TAA Lemma 160, correction 7). TAA Lemma 162: ζ frames are exactly the four-squares/Eisenstein frames r₄(p)/8 = p + 1; KS coupling-constant metamorphosis ω² = −E/2 is the oscillator version of cos θ → cosh φ.

**Formula.** cosh φ = cos(iφ); 1/(1 − 2cosh φ·u + u²) = Σ sinh((k+1)φ)/sinh φ · u^k

**Numbers.** p = 5, φ = ½ log 5: poles 1/√5, √5 (Re s = 1, 0) · Chebyshev errors ≤ 5e−30

**Also known as:** Chebyshev frame; Eisenstein endpoint

**Axes:** phase/unitarity (Ax3), structure/frame (Ax1), physics analogue

**TAA lemmas:** 160, 162

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.5 · tractability 0.6 · evidence 1 → priority 0.325

> ⚠ **Correction / caution.** Local poles never lie on the critical line of a cusp form (TAA Lemma 160, correction 3).

**Relations (outgoing):**

- same mechanism as → [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) — one frame through the cusp
- same mechanism as → [Hecke operators](#hecke) — a_{p^k} = p^{k/2}U_k(t_p/2)
- analogue of → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) — Eisenstein endpoint at the cusp
- analogue of → [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) — |u| = 1 = one ring
- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) — per-prime unitarity ≠ global
- same mechanism as → [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift)

**Relations (incoming):** [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (same mechanism as); [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) (same mechanism as); [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) (same mechanism as); [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift) (same mechanism as); [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp) (refines); [Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward](#dbn-bohlin-decay) (mirror of)

### #200 · 0.325 · S-mirror ρ ↦ 1 − ρ̄ <a id="s-mirror"></a>

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

### #216 · 0.307 · Metaplectic / Kubota cocycle <a id="metaplectic"></a>

**Label:** Theorem · **id:** `metaplectic` · **quadrant:** true but ghost-blind/untested

*In plain words:* A 2-valued cocycle on SL₂ behind half-integer weight; structure without sign.

**Core.** TAA Lemma 146 §4: Kubota cocycle is a phase (Ax3); Hilbert product formula 300/300, quadratic reciprocity; θ weight ½ is metaplectic (a fourth root, TAA Lemma 141 §7) — mod 2 data, ghost-blind. TAA Lemma 151: θ multiplier eighth roots = Weil index; local covers split over SL₂(ℤ_p), p odd [BIB]; obstruction at 2 and ∞ = half-twist ±1.

**Also known as:** Kubota; double cover

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 141, 146, 151, 157

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- same mechanism as → ["Cocycles give structure, not sign"](#cocycle-principle)
- same mechanism as → [w₂ / Čech class (TAA Lemma 138)](#w2-cech)
- same mechanism as → [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) — preserves ω (dual side) only

**Relations (incoming):** [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) (analogue of); [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) (lives in); [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (same mechanism as); [Klein–Gordon indefinite charge](#klein-gordon-charge) (analogue of)

### #217 · 0.307 · Half Tate twist ℚ(½) <a id="half-tate-twist"></a>

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

**Relations (incoming):** [Connes trace formula](#connes-trace) (analogue of); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (same mechanism as); [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) (analogue of); [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) (lives in); [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) (analogue of)

### #219 · 0.307 · Functional equation ξ(s) = ξ(1 − s) <a id="functional-equation"></a>

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

**Relations (incoming):** [Davenport–Heilbronn function](#davenport-heilbronn) (fails for); [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) (counterexample to sufficiency of); [Epstein zeta no-go](#epstein) (fails for); [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) (same mechanism as); [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) (implies); [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) (same mechanism as); [Scattering unitarity |φ| = 1](#scattering-phi) (special case of); [Sector map w = e^{iπs/2}](#sector-map-w) (same mechanism as)

### #222 · 0.307 · Half turn = sign flip (S² = −I, root number, Hardy Z sign changes) <a id="half-turn-sign-flip"></a>

**Label:** Theorem · **id:** `half_turn_sign_flip` · **quadrant:** true but ghost-blind/untested

*In plain words:* Turning by 180° is a sign: it flips modular forms of odd weight, gives the root number, and is the sign change of Hardy’s Z at each zero on the line.

**Core.** S² = −I in SL₂(ℤ) acts by (−1)^k on weight k (odd weights vanish; weight ½ needs the metaplectic cover). s ↦ 1 − s is the 180° rotation about ½; its sign is the root number (+1 for ζ, −1 for 37a1, forcing L(E,1) = 0). Hardy Z(t) = e^{iϑ(t)} ζ(½ + it) is real; it changes sign at each on-line zero of odd order. An off-line pair adds 2 to N(T) and no sign change. TAA Lemma 152 NUM (t ∈ [10,120], step 0.01): ζ 38 sign changes / 38 zeros; DH 62 / 66, the two deficits of 2 exactly in [80,90] and [110,120] (off-line pairs 85.699, 114.163). ℝP¹ = directions mod 180°; tautological bundle = Möbius band (the sign).

**Numbers.** ζ: 38/38 on [10,120] · DH: 62 sign changes vs N = 66; 5 vs 7 on [80,90] and [110,120] · |Im Λ_DH|/|Λ_DH| ≤ 7.1e−12 on the line

**Also known as:** wedge; S² = −I; root number; Hardy Z sign changes; Möbius band

**Axes:** phase/unitarity (Ax3), ghost-blind, numerics/certificate

**TAA lemmas:** 152, 158

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** Ghost-blind at on-line zeros (DH flips like ζ); off-line zeros appear only as missing flips against a global count N(T) (argument principle, Turing-type): detection, not positivity (TAA Lemma 152, correction 8).

> ⚠ **Correction / caution.** TAA Lemma 158: every quadratic form has Q(−x) = Q(x): the half turn persists through the F/V merge; ghost-blind. The signal is the sign pattern (definite → indefinite).

**Relations (outgoing):**

- same mechanism as → [Metaplectic / Kubota cocycle](#metaplectic) — S² = −I; weight ½
- same mechanism as → [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) — s ↦ 1 − s half turn; root number
- corrects → [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) — the wedge is the sign layer, not the missing surface (TAA Lemma 152, correction 8)

**Relations (incoming):** [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) (same mechanism as); [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) (analogue of); [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) (same mechanism as); [Sector map w = e^{iπs/2}](#sector-map-w) (analogue of); [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) (analogue of)

### #227 · 0.307 · Cup product / Poincaré duality pairing <a id="cup-product"></a>

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

### #228 · 0.307 · Hecke operators <a id="hecke"></a>

**Label:** Theorem · **id:** `hecke` · **quadrant:** true but ghost-blind/untested

*In plain words:* Averaging operators on modular forms; self-adjointness gives real eigenvalues but not the Ramanujan bound.

**Core.** Hecke self-adjoint ⇒ a_p ∈ ℝ, not |a_p| ≤ 2√p (TAA Lemma 134). Ghost-blind (TAA Lemma 146). TAA Lemma 160: a_{p^k} = p^{k/2}U_k(t_p/2) — each Hecke eigenvalue is one frame; multiplicativity = product of frames; per-frame ellipticity (Ramanujan) is not known to imply GRH (Open). TAA Lemma 162: LPS Hecke on S³/±1 and PSL/PGL(2,F_q) graphs: trivial p+1 vs |λ| ≤ 2√p (4 graphs, ≤ 4896 vertices; S² harmonics ℓ ≤ 15).

**Also known as:** T_p; Hecke self-adjointness

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 134, 146, 160, 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** a_p are not BSD generators.

**Relations (outgoing):**

- same mechanism as → [Hodge–Riemann bilinear relations](#hodge-riemann)
- fails for → [Riemann hypothesis (target node)](#rh) — ghost-blind
- lives in → [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3)

**Relations (incoming):** [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) (tests); [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (same mechanism as); [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) (lives in); [Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1)](#hecke-toy-contraction) (illustrates)

### #229 · 0.307 · Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic <a id="real-forms-compact-vs-boost"></a>

**Label:** Theorem · **id:** `real_forms_compact_vs_boost` · **quadrant:** true but ghost-blind/untested

*In plain words:* The same complex symmetry has three real versions: all rotations (compact, the 3-sphere), the Lorentz group (rotations plus boosts), and two copies of SL(2,ℝ) acting on anti-de Sitter space, which is the group the F/V animation already uses. Only the all-rotation version has bounded orbits and finite unitary pictures. ζ's prime frames are boosts.

**Core.** [T] Killing signatures computed: so(4) (0,6), so(3,1) (3,3), so(2,2) (4,2). SL₂ℝ×SL₂ℝ preserves det (signature (2,2)) on M₂(ℝ); diagonal = conjugation preserves tr = (F+V)/√q (2e−12). Lorentz: [K_i,K_j] = −ε J_k (convention), N± = (J ± iK)/2 commute only after complexification; K → iK gives so(4) (Killing (0,6)) — Weyl's unitary trick. Compact ⇔ bounded orbits, unit-circle eigenvalues, every finite-dim/unitary rep unitarizable; SO(3,1): non-trivial irreducible unitary reps infinite-dimensional. e^{iθJ} = cos θ + iJ sin θ needs J² = 1 (fails for spin-1 J_z: 0.235). Pauli: L² + A′² = −1/(2E) (E < 0, A′ = A/√(−2E)), A′² − L² = 1/(2E) (E > 0); L·A = 0; E_n = −1/2n² (1e−13). [A] definite energy = sign of the Casimir = compact real form (Theorem for Kepler; Analogy for ζ). [O] which real form is ζ's G×G. TAA Lemma 163: objective scoring K1–K7: SO(2,2) on AdS₃ unique 7/7 for the frame side ( adopted, scoped); SU(1,1) = SL₂ℝ, SL₂ℂ = so(3,1); sp(4,ℝ) not a form of so(4,ℂ).

**Numbers.** Killing: (0,6), (3,3), (4,2) · spin-1 exp-formula error 0.235

**Also known as:** rotations vs boosts; SO(2,2) on AdS₃; Weyl unitary trick; Pauli Casimir

**Axes:** phase/unitarity (Ax3), sign/positivity (Ax2), structure/frame (Ax1), ghost-blind

**TAA lemmas:** 162, 163

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

> ⚠ **Correction / caution.** N± split is complex; real boosts mix the two factors.

> ⚠ **Correction / caution.** Sign of [K,K] is convention; the relative flip vs [J,J] is what matters.

> ⚠ **Correction / caution.** "Purely imaginary generators" is the Hermitian physics convention.

**Relations (outgoing):**

- same mechanism as → [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) — rotations vs boosts
- same mechanism as → [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) — ζ frame = boost ½ log p
- lives in → [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface)
- special case of → [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) — Pauli Casimir sign
- lives in → [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3)

**Relations (incoming):** [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) (lives in); [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) (special case of)

### #248 · 0.307 · Maass–Selberg relations <a id="maass-selberg"></a>

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

### #257 · 0.267 · Half-density normalization |x|^{½} <a id="half-density"></a>

**Label:** Theorem · **id:** `half_density` · **quadrant:** true but ghost-blind/untested

*In plain words:* Multiplying by |x|^{½} makes scaling unitary on L²; this is why the critical line is at ½.

**Core.** TAA Lemma 145 Thm twist: |x|^½ = (dx/d*x)^½ is unitary L²(dx) → L²(d*x); U_λ unitary with generator −(x∂_x + ½); Mellin is unitary only on Re s = ½ (Plancherel 0.35355339 both sides; at Re 0.4 a weighted norm 0.53173). Cusp gauge y²∂²(y^½W) = y^½(W″ − W/4). TAA Lemma 153 (E): (U_λ f)(x) = λ^{½}f(λx) on L²(ℝ₊,dx): U_λ x^{−s} = λ^{½−s} x^{−s} (NUM ≤ 2.2e−16), |λ^{½−s}| = 1 for all λ iff Re s = ½ (x^{−s} is a generalized eigenfunction, not in L²). Critical line = unitary spectrum of scaling; this is unitarity (Ax3), not positivity. TAA Lemma 159: β = ½ (the critical line) is inverse temperature ½, i.e. half-density weights n^{−½}, inside the Hagedorn-divergent region (Analogy for the identification).

**Formula.** f ↦ |x|^{½} f

**Also known as:** ½ shift; unitary normalization; critical line = spectrum of unitary scaling

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 1, 141, 145, 153, 159

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** There are two ½’s (TAA Lemma 145 corrections): the unitary twist and the critical line.

**Relations (outgoing):**

- same mechanism as → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity)
- same mechanism as → [Lamb cutoff](#lamb-cutoff)
- same mechanism as → [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) — half-density amplitude

**Relations (incoming):** [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) (analogue of); [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) (same mechanism as); [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) (analogue of); [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) (refines); [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) (same mechanism as); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (analogue of); [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) (same mechanism as); [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) (analogue of); [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) (same mechanism as); [Distortionless line R/L = G/C](#distortionless) (same mechanism as); [Lamb cutoff](#lamb-cutoff) (same mechanism as)

### #258 · 0.267 · Theta inversion θ(1/t) = √t θ(t) <a id="theta-inversion"></a>

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

### #259 · 0.267 · The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K <a id="apsidal-sweep-eccentricity"></a>

**Label:** Theorem · **id:** `apsidal_sweep_eccentricity` · **quadrant:** true but ghost-blind/untested

*In plain words:* As t grows from 0 to 2 the invariant ellipse of the frame stretches along a fixed 45° line, like a planet given ever-larger kicks at periapsis. At t = 2, where F and V meet, the orbit becomes a parabola and escapes; beyond that it is a hyperbola. After squaring (Bohlin's map) the eccentricity is exactly t/2.

**Core.** [T] gᵀS_tg = S_t; eigenvectors (1,1),(1,−1) ∀t > 0 (t = 0: S = I). Hooke eccentricity of S_t = 1 (t < 2) and S_t = −1 (t > 2, transverse axis on (1,1)): e_H² = 2c/(1+c), c = t/2 = cos θ | cosh φ; Wick form 1 − tan²(θ/2) → 1 + tanh²(φ/2); other family 1/e² + 1/e′² = 1. Table: t = 1.8165, 1.9.9871, 2.5 1.0541, 4 1.1547; e_H → √2. Bohlin (z ↦ z², Bull. Astr. 28 (1911) 113–119): focal conic with e_K = t/2 exactly (fit residual 1e−9), apsidal line 45° → 90°; F/√q = e_K + i b_K/a_K (elliptic), e^{±φ} = e_K ± b_K/a_K (hyperbolic); r_a/r_p = (1+e_K)/(1−e_K) = −((1+u)/(1−u))², u = F/√q (Cayley). Margin: S_t on (1,1)/√2 = 1 − t/2 = λ_min(S_t) = 1 − e_K = −2E r_p/μ (Kepler binding at fixed periapsis). Periapsis kick from a circle, v = k v_c: e = k² − 1, apsidal line and r_p fixed, escape k = √2 (⇔ t = 2). [N] 38 checks PASS. [A] 45° tilt = the fixed apsidal axis of the animation's normalized norm conic (q-normalized coordinates).

**Formula.** e_H² = 2t/(t+2); e_K = t/2; F/√q = e_K + i·b/a; margin = 1 − t/2

**Numbers.** e_H:.8165 (t=1),.9871 (1.9), 1.0541 (2.5), 1.1547 (4) · kick: e = k² − 1, escape k = √2 · r_a/r_p = cot²(θ/2)

**Also known as:** Kepler sequence of a frame; binding margin

**Axes:** phase/unitarity (Ax3), structure/frame (Ax1), physics analogue, ghost-blind, numerics/certificate

**TAA lemmas:** 161

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** The F/V real line is in the eigenvalue plane, the apsidal line in phase space (TAA Lemma 161, correction 5).

> ⚠ **Correction / caution.** r_a/r_p ≠ F/V; e ≠ tanh φ (TAA Lemma 161, correction 6).

> ⚠ **Correction / caution.** Definite energy is eroded by the kick, not produced by it (TAA Lemma 161, correction 9).

**Relations (outgoing):**

- same mechanism as → [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) — F = V ⇔ parabolic escape
- same mechanism as → [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) — cos θ ↔ cosh φ
- lives in → [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) — lobe/wedge/window = ellipse/parabola/hyperbola
- lives in → [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form)

**Relations (incoming):** [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift) (lives in); [Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward](#dbn-bohlin-decay) (refines); [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) (lives in)

### #260 · 0.267 · Eisenstein constant term & scattering φ(s) <a id="eisenstein-ct"></a>

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

**Relations (incoming):** [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) (analogue of); [Selberg resonances](#selberg-resonances) (same mechanism as); [Maass–Selberg relations](#maass-selberg) (same mechanism as); [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) (lives in); [E₂* as the derivative of the Kronecker limit (cusp-scattering footprint)](#kronecker-limit-e2star) (same mechanism as)

### #262 · 0.267 · Hilbert reciprocity at 2: the odd halves become sign bits <a id="hilbert-reciprocity-at-2"></a>

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

**Relations (incoming):** [Half Tate twist ℚ(½)](#half-tate-twist) (same mechanism as); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) (analogue of)

### #264 · 0.267 · Scattering unitarity |φ| = 1 <a id="scattering-phi"></a>

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

### #273 · 0.267 · Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase <a id="maslov-legendre-fourier"></a>

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

### #280 · 0.267 · Gauss sum as canonical √(±p) <a id="gauss-sum-canonical-root"></a>

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

### #289 · 0.267 · The critical-line wave: Hardy Z and the Riemann–Siegel phase <a id="hardy-z-critical-line-wave"></a>

**Label:** Theorem · **id:** `hardy_z_critical_line_wave` · **quadrant:** true but ghost-blind/untested

*In plain words:* On the critical line ζ(1/2+it) = Z(t)e^{−iθ(t)} with Z real, so the real and imaginary parts are one real wave seen through a rotating phase. Each simple zero is a sign change of Z, so the phase of ζ jumps by π. The mean of Re ζ on the line is 1; Gram's law is the separate statement (−1)^n Z(g_n) > 0 at Gram points, and it fails first at n = 126. Sign changes equal N(T) for all T iff RH holds and all zeros are simple. Under RH, (Z′/Z)′ = −Σ(t−γ)^{−2} − (log G)″, which forbids wrong-sign extrema wherever the sum dominates (checked for 5.7 ≤ t ≤ 400).

**Core.** The critical-line wave: Hardy Z and the Riemann–Siegel phase

**Formula.** ζ(1/2+it)=Z(t)e^{−iθ(t)}; Z=−2π^{1/4}Ξ/G, G=(t²+1/4)|Γ(1/4+it/2)|; (Z′/Z)′=−Σ_γ[(t−γ)^{−2}+(t+γ)^{−2}]−(log G)″

**Numbers.** mean Re ζ on [0,500] = 0.997 · Gram's law 98.5% for −1 ≤ n ≤ 199, first failure n = 126 · sign changes = N(T) = 29, 79, 269 at T = 100, 200, 500 · 271 extrema on (0,500], one wrong-sign at t = 2.48 (inside t < 5.7)

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- analogy of → [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1)
- analogy of → [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings)

**Relations (incoming):** [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix) (instance of)

### #292 · 0.267 · w₂ / Čech class (TAA Lemma 138) <a id="w2-cech"></a>

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

### #302 · 0.267 · The factorial of one half and the Fourier quarter-turn <a id="fourier-quarter-turn"></a>

**Label:** Theorem · **id:** `fourier_quarter_turn` · **quadrant:** true but ghost-blind/untested

*In plain words:* Gamma(1/2) = sqrt(pi) and (1/2)! = sqrt(pi)/2. The Gaussian e^{-pi x^2} is fixed by the Fourier transform, F^4 = 1, and the Hermite functions are its eigenfunctions with eigenvalues 1, -i, -1, i. Poisson summation for the Gaussian gives the theta inversion, and its Mellin transform gives xi(s) = xi(1-s). This explains the symmetry s <-> 1-s, not the critical line. The archimedean term alone is positive only for support below 0.2143; with the pole (or on the pole-free space) the threshold is 0.7432.

**Core.** The factorial of one half and the Fourier quarter-turn

**Formula.** int_R |x|^{s-1} e^{-pi x^2} dx = pi^{-s/2} Gamma(s/2); F h_n = (-i)^n h_n, h_n = H_n(sqrt(2 pi) x) e^{-pi x^2}

**Numbers.** theta inversion error 2e-32 · xi(s) - xi(1-s) error 8e-32 at s = 0.3 + 7i · arch alone positive for ell < 0.2143; arch + pole for ell < 0.7432

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 180

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

**Relations (outgoing):**

- instance of → [One log-gas and its frozen limit](#log-gas-frozen-limit)

### #309 · 0.267 · Spin structure & theta characteristic <a id="spin-theta"></a>

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

### #312 · 0.256 · "Cocycles give structure, not sign" <a id="cocycle-principle"></a>

**Label:** Heuristic · **id:** `cocycle_principle` · **quadrant:** background

*In plain words:* Any cocycle/class (metaplectic, w₂, defect) fixes structure but cannot decide a positivity sign.

**Core.** TAA Lemma 138/TAA Lemma 144/TAA Lemma 146 summary principle.

**Also known as:** cocycle principle

**Axes:** phase/unitarity (Ax3), ghost-blind

**TAA lemmas:** 138, 144, 146

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 0.7 · specificity 0.05 · tractability 0.5 · evidence 0.6 → priority 0.256

**Relations (outgoing):**

- same mechanism as → [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive)

**Relations (incoming):** [Automorphy defect (TAA Lemma 144)](#automorphy-defect) (same mechanism as); [Metaplectic / Kubota cocycle](#metaplectic) (same mechanism as); [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) (analogue of); [The prime 2 as the wild place](#prime-two-wild) (same mechanism as); [w₂ / Čech class (TAA Lemma 138)](#w2-cech) (same mechanism as)

### #333 · 0.212 · Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind) <a id="lrl-hidden-symmetry-trichotomy"></a>

**Label:** Analogy · **id:** `lrl_hidden_symmetry_trichotomy` · **quadrant:** background

*In plain words:* The Runge–Lenz vector points from the Sun to the periapsis and its length is the eccentricity. Bound orbits have it shorter than its maximum, and that is when the hidden symmetry is the compact rotation group of a four-dimensional sphere. A push along the orbit lengthens it; a push along it only turns it, which is precession.

**Core.** [T] A = p × L − mk r̂ points focus → periapsis, |A|² = m²k² + 2mE|L|²; at periapsis gravity is anti-parallel to A, v ⊥ A. dA/dt = f × L + p × (r × f) for an extra force f (checked 6e−10). m = k = 1, r = (1,0), p = (0,1.2): A = (0.44,0), |A|² = 0.1936; Δp = 0.01 tangential: ΔA = (0.0241, 0) (stretch); radial: ΔA = (0, −0.012) (rotation; |A| changes at 2nd order). Linear model: rotation-conjugation of g_t = precession (trace, F, V, e unchanged); squeeze-conjugation changes e, not F, V; changing t = kick (changes the spectrum). [C] Pauli 1926 (Z. Phys. 36, 336–363), Fock 1935 (Z. Phys. 98, 145–154; momentum space → S³), Bargmann 1936 (Z. Phys. 99, 576–582); Bander–Itzykson 1966 (RMP 38, 330; 346): O(4) bound, O(1,3) scattering, E(3) at E = 0 (preprint). [A] definite ⇔ compact symmetry ⇔ unitary finite-dim reps ⇔ discrete spectrum ↔ TAA thesis 'RH is unitarity'; spherical/flat/hyperbolic matches the (2,3,n) split. [O] what compact group plays SO(4) for ζ (Katz–Sarnak 1999 symmetry types are statistical, not this). TAA Lemma 162: KS makes SO(4) manifest (commutant su(2)⊕su(2) of the U(1) constraint in u(4)); Pauli Casimir sign = real form; Moser orbit space S²×S²; in exact Kepler A never precesses (correction).

**Numbers.** A = (0.44, 0), |A|² = 0.1936 · ΔA tangential (0.0241, 0); radial (0, −0.012)

**Also known as:** Runge–Lenz; SO(4) of hydrogen; LRL precession

**Axes:** phase/unitarity (Ax3), physics analogue, ghost-blind

**TAA lemmas:** 161, 162

**Scores (Heuristic):** gap significance 0.5 (nearest gap: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)) · sensitivity 0.6 · specificity 0.05 · tractability 0.4 · evidence 0.5 → priority 0.212

> ⚠ **Correction / caution.** At periapsis the force is radial, not tangential (TAA Lemma 161, correction 11).

> ⚠ **Correction / caution.** SO(4) ↔ RH is Analogy only.

**Relations (outgoing):**

- analogue of → [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) — compact hidden symmetry ↔ unitarity
- lives in → [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity)
- analogue of → [Hilbert–Pólya](#hilbert-polya) — discrete spectrum from a compact symmetry
- same mechanism as → [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) — sphere / plane / hyperbolic
- same mechanism as → [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift)
- lives in → [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2)

**Relations (incoming):** [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (analogue of); [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) (special case of); [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) (special case of); [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift) (special case of); [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge) (refines); [Kepler: LRL vector closes so(4) = su(2) ⊕ su(2) for E < 0, so(3,1) for E > 0, e(3) at E = 0](#kepler-so4-contraction) (illustrates)

## Axis: ghost-blind <a id="axis-ghost-blind"></a>

### #69 · 0.540 · KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n) <a id="kms-bochner-coefficient-positivity"></a>

**Label:** Theorem · **id:** `kms_bochner_coefficient_positivity` · **quadrant:** RH-sharp

*In plain words:* The thermal (KMS) route makes imaginary time a circle and gives a positivity, but that positivity is only about the coefficients being counts. It rules out DH for the wrong reason and lets other bad functions through.

**Core.** [T] Bochner; Tomita–Takesaki S = JΔ^{1/2} (checked 2e−16); thermal time = Hamiltonian time (Connes–Rovelli); BW: wedge boost, e^{2πiK} = 1. [N] BC: Tr e^{−βH} = ζ(β); Galois-averaged KMS value (p^{1−β}−1)/(p−1) (2e−31); symmetry breaking φ(e(1/5)) =.04+.606i. Toeplitz test β = 1.6: ζ, Z_Q PSD, DH min −3.96 (relative). DH excluded by coefficients (not a sign on zeros); Z_Q passes ⇒ B2 negative (TAA Lemma 164 Cor. 4.3).

**Numbers.** 17/17 checks · K5 min 0.0027 on [1, 1e4]

**Also known as:** B2 verdict; modular route to compact J

**Axes:** ghost-blind, physics analogue, restatement ⇔ RH

**TAA lemmas:** 164

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

**Relations (outgoing):**

- special case of → [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms)
- lives in → [Bost–Connes KMS states](#kms-bost-connes)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — negative coefficients

**Relations (incoming):** [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) (same mechanism as); [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (analogue of); [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (same mechanism as); [Bost–Connes KMS states](#kms-bost-connes) (lives in)

### #79 · 0.540 · Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant <a id="invariant-vs-refined-count"></a>

**Label:** Theorem · **id:** `invariant_vs_refined_count` · **quadrant:** RH-sharp

*In plain words:* Some counts can't change under deformation, like the total number of zeros or a Lefschetz number. Others can, like the number of zeros on the line. RH says the second count equals the first. Davenport–Heilbronn has the same total count as a true L-function but fewer zeros on the line, so the protected counts can't tell ghosts apart.

**Core.** [T/B] Lefschetz number homotopy-invariant (fixed points collide/annihilate in pairs); in flat proper families χ = Σ(−1)^i h^i is constant while h^i are upper semicontinuous (Hartshorne III.12.8, not opened); TAA Lemma 140: #C(F_{qⁿ}) − (1 + qⁿ) = −Tr(Fⁿ|H¹): H⁰/H² terms rigid, H¹ frames movable. [N] all 10,100 smooth y² = x³ + Ax + B over F_101: invariant part 102, a_p in [−20, 20] (41 values), all elliptic. [T] H_t: box count (argument principle) conserved across a collision (2.000000), real count 2 → 0. [R] N₀(T) = N(T) ∀T ⇔ RH. [H/N] DH: Riemann–von Mangoldt main term (T/2π)log(5T/2πe) by the FE argument (no source opened for DH): N(135) = 79 vs 79.0002, N(200) = 130 vs 129.548 (TAA Lemma 156 certified); on-line 75 and 122 (ghost deficits 4, 8 at 85.70, 114.16, 166.48, 176.70). ζ: N(150) = 52 vs 52.75. No-go: invariance of counts cannot exclude ghosts.

**Numbers.** DH N(135) = 79 vs 79.0; N₀ = 75 · DH N(200) = 130 vs 129.5; N₀ = 122 · F_101 family: 1 + p = 102 fixed, 41 values of a_p

**Also known as:** χ-type vs h-type; refined = invariant

**Axes:** ghost-blind, geometry over F_q, restatement ⇔ RH, numerics/certificate

**TAA lemmas:** 160

**Scores (Heuristic):** gap significance 0.5 (nearest gap: an inequality consequence of automorphy (SC-E / HS-1)) · sensitivity 1.0 · specificity 1.0 · tractability 0.6 · evidence 1 → priority 0.540

> ⚠ **Correction / caution.** For ζ there is no family and no h¹ (Deninger’s conjectured cohomology, MP0–MP4): Analogy.

> ⚠ **Correction / caution.** DH main term is Heuristic (no source opened) + Numerical (TAA Lemma 160, correction 14).

**Relations (outgoing):**

- same mechanism as → [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) — χ protected, h^i jump
- same mechanism as → [Tate count / Picard number (ghost-blind)](#tate-count) — counts ghost-blind
- analogue of → [Counts vs quadratic positivity](#count-positivity)
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — same N(T), deficient N₀(T)
- lives in → [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy)

### #237 · 0.307 · The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once <a id="n-factorial-bridge-all-places"></a>

**Label:** Theorem · **id:** `n_factorial_bridge_all_places` · **quadrant:** true but ghost-blind/untested

*In plain words:* The factorial already contains the archimedean data (the Gamma function) and the p-adic data (how often each prime divides it). Each piece alone cannot tell ζ from a fake; what is missing is something that ties all of them together with a sign.

**Core.** [Theorem] Chebyshev: log n! = Σ_{d≤n} Λ(d)⌊n/d⌋ (log = Λ ∗ 1; exact for n = 10, 100, 1000). Legendre: v_p(n!) = (n − s_p(n))/(p − 1) (100!, p = 2, 3, 5, 7). Stirling/Γ: n! = Γ(n+1), Γ the archimedean factor (error 2.7e−12 at n = 1000). Product formula |n!|_∞ Π_p |n!|_p = 1 (exact for n = 20). F₁ limit |GL_n(F_q)|/(q−1)^n → n! (2, 6, 24); the F₁ reading is a Heuristic (Tits/Soulé, not opened). [Cited] Morita 1975 p-adic Γ_p (values in ℤ_p^×); Gross–Koblitz 1979: Gauss sums = π-power × products of Γ_p values. Link to the SL(2,F_p) half representations: character values (±1 ± √(εp))/2 with √(εp) the quadratic Gauss sum, g_p² = εp; consistency mod p ((p−1)/2)!² ≡ (−1)^{(p+1)/2} for p < 1000. Ghost check: DH shares Γ; its c ∗ a = a·log needs composite c (6, 12, 14, …), so the bridge separates DH only through the support of Λ (the Euler product). Verdict: no new non-archimedean element is needed; what is missing is a positivity coupling all places at once (R8′). The product formula is the only known all-places coupling and is an identity with no sign; provisional definition: a signed product formula on the square (Open).

**Formula.** log n! = Σ_{d≤n} Λ(d)⌊n/d⌋; |n!|_∞ Π_p |n!|_p = 1

**Numbers.** 20! = 2¹⁸3⁸5⁴7²·11·13·17·19 · g_p² = εp to 2.3e−13 (p < 200)

**Also known as:** n! bridge; Chebyshev identity; non-archimedean element

**Axes:** ghost-blind, Spec ℤ gap, numerics/certificate

**Scores (Heuristic):** gap significance 0.5 (nearest gap: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.307

**Relations (outgoing):**

- analogue of → [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) — quadratic Gauss sum = Γ_p(½) case of Gross–Koblitz
- lives in → [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) — separates DH only through the support of Λ
- fails for → [Davenport–Heilbronn function](#davenport-heilbronn) — each place ghost-blind

**Relations (incoming):** [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) (lives in); [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) (same mechanism as)

### #263 · 0.267 · The prime 2 as the wild place <a id="prime-two-wild"></a>

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

### #290 · 0.267 · E₂* as the derivative of the Kronecker limit (cusp-scattering footprint) <a id="kronecker-limit-e2star"></a>

**Label:** Theorem · **id:** `kronecker_limit_E2star` · **quadrant:** true but ghost-blind/untested

*In plain words:* E₂'s modular anomaly is the derivative of the √y piece of the Eisenstein series' constant term, i.e. a trace of the cusp's continuous spectrum.

**Core.** [T] ∂_z log(√y|η(z)|²) = (πi/12)·E₂*(z), E₂* = E₂ − 3/(πy) (from (1/2πi) d log Δ = E₂, Zagier Prop. 7, and ∂_z ½ log y = −i/(4y)). Kronecker's first limit formula: E(z,s) = Σ′ y^s/|mz+n|^{2s} = π/(s−1) + 2π(γ − log 2 − log(√y|η|²)) + O(s−1). Constant term 2ζ(2s)[y^s + φ(s)y^{1−s}], φ = ξ(2s−1)/ξ(2s) (TAA Lemma 153 Birman–Krein). Ghost-blind (symmetry layer). [N] identity to 2e−62 (3 points); limit formula 3.9e−21 at ε = 1e−20; φ identity 1.1e−61. The other LLM's IHO ↔ E₂-anomaly 'inverse-area' bridge: no support (arXiv 2012.09875, 2412.09274 opened: no modular forms).

**Numbers.** ∂_z identity |diff| ≤ 2e−62 · Kronecker limit |diff| 3.9e−21

**Axes:** ghost-blind, phase/unitarity (Ax3)

**TAA lemmas:** 157

**Scores (Heuristic):** gap significance 0.2 (no gap within distance 2) · sensitivity 1.0 · specificity 0.05 · tractability 0.6 · evidence 1 → priority 0.267

> ⚠ **Correction / caution.** Ghost-blind: says nothing about MP4.

> ⚠ **Correction / caution.** No IHO/E₂ bridge in the cited physics papers.

**Relations (outgoing):**

- same mechanism as → [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) — E₂* = ∂ of Kronecker limit
- same mechanism as → [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) — φ in the constant term
- analogue of → [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) — cusp scattering

## Index by rank

| # | priority | concept | label | quadrant |
|---|---|---|---|---|
| 1 | 0.200 | [Refined missing piece (Open): a ferromagnetic coupling between the primes (and the archimedean place) that produces the Riemann kernel Φ; the underlying equivalence RH ⇔ Φ is a Lee–Yang single-spin measure (Λ = 0 margin) is a known restatement](#ferromagnetic-phi-missing-piece) | Open | RH-sharp |
| 2 | 0.720 | [Davenport–Heilbronn function](#davenport-heilbronn) | Theorem | RH-sharp |
| 3 | 0.720 | [Weil positivity criterion](#weil-positivity) | Cited | RH-sharp |
| 4 | 0.720 | [ψ(x) − x (explicit formula, deviation from the pole)](#psi-minus-x) | Cited | RH-sharp |
| 5 | 0.720 | [Two Verschiebungs: pairing dual V^∨ vs positive adjoint V†](#two-verschiebungs-dual-vs-adjoint) | Theorem | RH-sharp |
| 6 | 0.720 | [Frobenius-graph lattice on E×E (relative counts = intersections with Δ)](#frobenius-graph-lattice) | Theorem | RH-sharp |
| 7 | 0.720 | [Kähler triple (ω, J, g) = polarization; elliptic ⇔ positive form preserved](#kahler-triple-polarization) | Theorem | RH-sharp |
| 8 | 0.720 | [Lagarias/Hinkkanen criterion](#lagarias) | Cited | RH-sharp |
| 9 | 0.720 | [Connes trace formula](#connes-trace) | Cited | RH-sharp |
| 10 | 0.720 | [Kähler identities → Serre/Deninger–Singhof unitarity → MP4 in degree 1 ⇔ the flow preserves a leafwise Hodge splitting](#kahler-identities-foliated) | Theorem | RH-sharp |
| 11 | 0.720 | [Primitive part V₀ = U^⊥](#primitive-part) | Theorem | RH-sharp |
| 12 | 0.720 | [Definite cup square / Krein one-liner](#definite-cup-square) | Theorem | RH-sharp |
| 13 | 0.700 | [Missing: Deninger's conjectured cohomology for Spec ℤ, stated as axioms MP0–MP4 (no coined name)](#mp-flow-h1) | Open | RH-sharp |
| 14 | 0.700 | [Missing: arithmetic Castelnuovo object (positive involution on a space where the Weil distribution is a |·|²)](#mp-castelnuovo) | Open | RH-sharp |
| 15 | 0.700 | [Missing: H¹ on the square of the scaling site (Connes–Consani s(f,f) ≤ 0)](#mp-h1-square) | Open | RH-sharp |
| 16 | 0.700 | [Missing: a Néron–Severi strictly larger than U containing the Frobenius classes Ψ_λ](#mp-ns-psi) | Open | RH-sharp |
| 17 | 0.700 | [Missing: surface + ample class + Riemann–Roch for Spec ℤ (D8)](#mp-d8) | Open | RH-sharp |
| 18 | 0.700 | [Missing: a BRST-type complex Q with H(Q) = U^⊥ positive (PM-3)](#mp-brst) | Open | RH-sharp |
| 19 | 0.700 | [Missing: passivity of ξ′/ξ from a zero-free mechanism (Lagarias margin)](#mp-passivity-margin) | Open | RH-sharp |
| 20 | 0.700 | [Missing: quadratic Riemann–Roch + “ampleness ⇒ effectivity” on the square](#mp-quadratic-rr) | Open | RH-sharp |
| 21 | 0.700 | [Missing: RR/GRR on an arithmetic Spec ℤ × Spec ℤ producing the sign (RG-5, “the missing row”)](#mp-rg5) | Open | RH-sharp |
| 22 | 0.700 | [Missing: an inequality consequence of automorphy (SC-E / HS-1)](#mp-automorphy-ineq) | Open | RH-sharp |
| 23 | 0.600 | [Passivity (positive real part)](#passivity) | Restatement | RH-sharp |
| 24 | 0.600 | [Relative Gram matrix G_rel](#relative-gram) | Restatement | RH-sharp |
| 25 | 0.600 | [Verschiebung as the positive adjoint of Frobenius (F† = V)](#verschiebung-positive-adjoint) | Restatement | RH-sharp |
| 26 | 0.600 | [Cayley–Klein absolute: definite ⇔ no real null rays (rotations vs boosts)](#cayley-klein-absolute) | Restatement | RH-sharp |
| 27 | 0.600 | [Riemann–Roch strategy: RH ⇔ s(f,f) ≤ 0](#rr-strategy-sff) | Restatement | RH-sharp |
| 28 | 0.600 | [Zero-side real form = RH: under MP0–MP3 a finite Θ-stable σ-stable block with m off-line orbits has Krein isometry group U(n₀+m, m); the normalized flow is in a compact group on every block ⇔ RH; DH's Weil Gram reads O(n−q, q), q up to 24 (h =.025, L = 15.95), ζ compact on all TAA Lemma 149 windows](#zero-side-real-form-krein) | Restatement | RH-sharp |
| 29 | 0.580 | [Block-wise Weil-form diagnostic (BR-2): R-symmetric tilt blocks detect DH’s off-line pairs from the prime side](#blockwise-weil-diagnostic) | Numerical | RH-sharp |
| 30 | 0.580 | [DH prime-side Gram test](#dh-prime-side-gram) | Numerical | RH-sharp |
| 31 | 0.580 | [Euler product and functional equation work only together: the window positivity test](#euler-fe-conjunction) | Numerical | RH-sharp |
| 32 | 0.580 | [Completeness rigidity: one missing prime creates many unstable modes](#completeness-rigidity-one-prime) | Numerical | RH-sharp |
| 33 | 0.580 | [Primitive-part Weil spectrometer: the TAA Lemma 149 Weil Gram restricted to kerP = {∫f e^{±u/2} = 0} (pole/cusp functionals): ζ’s only negative direction without the pole row is the pole direction (index 1, removed by kerP); ζ, L(χ₅) PSD on full and kerP to W = 16; DH’s failure is primitive: same onset (3.875 at h = 0.025, 5.7 at h = 0.05) and essentially the same index (24 / 14 at W ≈ 16) on kerP](#primitive-part-weil-spectrometer) | Numerical | RH-sharp |
| 34 | 0.580 | [Two standing ghosts in the truncated Weil test: the Epstein zeta Z_Q/2, Q = x² + 5y² (non-negative coefficients, FE, pole, Γ_R(s)Γ_R(s+1), conductor 20, no Euler product) fails at W = 3.0 (kerP 3.175; no pole row 1.05) and locks there for all P ≥ 7 (all P-smooth n); prime powers only lock at 3.35; ζ_K = ζL(χ₋₂₀) (same Γ factor, Euler product) passes to W = 8 and its truncations track log q; Epstein index 32 at W = 7.9 vs DH 6 at W = 8](#two-standing-ghosts-truncation) | Numerical | RH-sharp |
| 35 | 0.580 | [Weil Gram matrix of prime-localised bumps (mutual-inductance matrix), computed from primes and ∞ only](#weil-gram-coupling-matrix) | Numerical | RH-sharp |
| 36 | 0.580 | [Growing-S rate test (h = 0.025, all 428 primes P ≤ e⁸): Euler-product truncations (ζ, L(χ₅)) fail just after log q of the first omitted prime (offsets 0.009–0.051 for ζ, all P; 0.017–0.063 for χ₅, P ≥ 7; small-P slack of χ₅ since χ₅(5) = 0) with pre-onset margin 1.8e−6 → 5e−11 (numerical floor); DH with all P-smooth composites tracks log q until P = 41 and locks at its global onset 3.85 for all P ≥ 43; DH prime powers only locks at 1.90 for all P ≥ 3](#growing-s-truncation-rate) | Numerical | RH-sharp |
| 37 | 0.580 | [Chebyshev bias for elliptic curves (averaged sign of a_p)](#elliptic-chebyshev-bias) | Numerical | RH-sharp |
| 38 | 0.580 | [Ghost conventions A / B / C for spectral tests](#ghost-conv-abc) | Numerical | RH-sharp |
| 39 | 0.579 | [Deninger’s foliated program](#deninger) | Cited | true but ghost-blind/untested |
| 40 | 0.579 | [Light cone U = ⟨𝟙, 𝕃⟩ (pole plane, null rays)](#light-cone-u) | Theorem | true but ghost-blind/untested |
| 41 | 0.579 | [Surface + ample + RR ⇒ Hodge index (D8)](#surface-ample-rr) | Theorem | true but ghost-blind/untested |
| 42 | 0.579 | [Ax1–Ax3 axioms (Yoneda specification)](#ax123) | Theorem | true but ghost-blind/untested |
| 43 | 0.579 | [Limiting mixed Hodge structure / nilpotent and SL₂-orbit theorems (Schmid; CKS)](#lmhs-nilpotent-orbit) | Cited | true but ghost-blind/untested |
| 44 | 0.579 | [Tensor square HZ ∧_𝕊 HZ and its Laurent piece (quadratic only in U)](#laurent-square) | Theorem | true but ghost-blind/untested |
| 45 | 0.579 | [Livšic route to conformality, split: under Deninger’s working hypothesis 7.5 ζ’s explicit formula fixes only ε_γp(k) = +1 and |det A_p| = p for the return map of the log p orbit; tr M_p (M_p = A_p/√p) is constrained only by |tr M_p| < √p + 1/√p, while Kalinin–Sadovskaya’s periodic-data conformality theorem needs |tr M_p| < 2; the scalar factor e^t is supplied by abelian Livšic, the conformal structure (≡ invariant leafwise J, i.e. H4 at the prime orbits) is not](#livsic-route-split) | Theorem | sharp but interpretive |
| 46 | 0.579 | [Parity argument: linear χ cannot see D²](#parity-linear-chi) | Theorem | true but ghost-blind/untested |
| 47 | 0.579 | [Adelic gluing: ℍ at ∞ and Bruhat–Tits trees at p in GL₂(ℚ)∖GL₂(𝔸)](#adelic-gluing-bruhat-tits) | Cited | true but ghost-blind/untested |
| 48 | 0.579 | [Tautology boundary (zero side vs prime side)](#tautology-boundary) | Theorem | true but ghost-blind/untested |
| 49 | 0.579 | [No étale H¹ for Spec ℤ](#no-etale-h1) | Theorem | true but ghost-blind/untested |
| 50 | 0.560 | [MP4 headline: the Euler product, taken as geometry (the Frobenius correspondence: graph classes on the square with an ample class), not as counting data, induces the Hodge splitting of the square, with its sign](#mp4-euler-induces-hodge) | Conjecture | RH-sharp |
| 51 | 0.560 | [The shape of the missing piece: ten necessary properties (P1–P10)](#missing-piece-shape-list) | Open | RH-sharp |
| 52 | 0.540 | [Rosati positivity](#rosati) | Theorem | RH-sharp |
| 53 | 0.540 | [Krein collisions (how ghosts are born)](#krein-collision) | Theorem | RH-sharp |
| 54 | 0.540 | [Castelnuovo–Severi inequality](#castelnuovo-severi) | Theorem | RH-sharp |
| 55 | 0.540 | [de Bruijn–Newman constant Λ](#debruijn-newman) | Cited | RH-sharp |
| 56 | 0.540 | [Frobenius as a boost (rapidity ½ log q)](#frobenius-boost) | Theorem | RH-sharp |
| 57 | 0.540 | [Epstein zeta no-go](#epstein) | Theorem | RH-sharp |
| 58 | 0.540 | [Zeros as Breit–Wigner resonances (line shapes, cusp doublets)](#breit-wigner-resonances) | Theorem | RH-sharp |
| 59 | 0.540 | [Conic type decided at infinity: degree positivity ⇒ ellipse ⇒ Hasse](#conic-type-at-infinity) | Theorem | RH-sharp |
| 60 | 0.540 | [Ghost quartet ½ ± δ ± iγ](#ghost-quartet) | Theorem | RH-sharp |
| 61 | 0.540 | [Poincaré disk: period domain, cusp degeneration and the trace classification](#poincare-disk-period-domain) | Theorem | RH-sharp |
| 62 | 0.540 | [F/V merge: circle → ellipse → parabolic → hyperbola (t = a/√q; τ(t); sign pattern)](#fv-merge-trichotomy) | Theorem | RH-sharp |
| 63 | 0.540 | [Compatible complex structure J commuting with Frobenius](#compatible-j) | Theorem | RH-sharp |
| 64 | 0.540 | [Arithmetic unitarity ("RH = unitarity")](#arith-unitarity) | Theorem | RH-sharp |
| 65 | 0.540 | [Genealogy of DH ghosts: the σ-pencil f_λ = (1−λ)Λ(χ) + λWΛ(χ̄) (χ mod 5) keeps a functional equation for all real λ, runs from the Euler product L(χ) to DH (λ = 1/2); on-line zeros = crossings of one phase θ(t) with the level tan θ = −(1−λ)/λ; off-line pairs are born at folds (Krein collisions of opposite-sign crossings) with the square-root law; t ≤ 600: 17 escapes, 2 captures, net 15 = DH census](#euler-to-dh-pencil-genealogy) | Theorem | RH-sharp |
| 66 | 0.540 | [Fake Weil polynomials (finite ghosts)](#fake-weil-poly) | Theorem | RH-sharp |
| 67 | 0.540 | [RH for curves over F_q (Weil)](#fq-curves) | Cited | RH-sharp |
| 68 | 0.540 | [Γ is the dual−adjoint gap: ⟨(Θ^∨ − Θ†)v,v⟩ = 1 − 2β](#gamma-as-dual-adjoint-gap) | Theorem | RH-sharp |
| 69 | 0.540 | [KMS/modular positivity is coefficient positivity: a KMS system with partition function F = Σ a_n n^{−β} exists ⇔ a_n ∈ ℤ≥0; then t ↦ F(β+it) is positive definite (|F(β+it)| ≤ F(β)). Compact pieces of the modular route: Tomita J (ℤ/2) and the imaginary-time circle; the BC modular group n^{it} is unitary but not periodic and acts on the prime side (log n)](#kms-bochner-coefficient-positivity) | Theorem | RH-sharp |
| 70 | 0.540 | [Certified zero lists (Arb): DH complete for t < 200, ζ for t < 150](#certified-zero-lists) | Theorem | RH-sharp |
| 71 | 0.540 | [Λ = 0 (⇔ RH, given Rodgers–Tao) puts ζ at the parabolic threshold of the de Bruijn–Newman family — at infinity: with simple zeros, forced collisions for t < 0 escape every compact set](#dbn-parabolic-threshold) | Theorem | RH-sharp |
| 72 | 0.540 | [Decay rate ¼](#decay-quarter) | Theorem | RH-sharp |
| 73 | 0.540 | [Eisenstein scattering resonances at s = ρ/2: purity at Re s = ¼](#eisenstein-resonances-rho-half) | Theorem | RH-sharp |
| 74 | 0.540 | [Ghost map Δ_w: zeros right of σ from damped Dirichlet sums](#ghost-map) | Theorem | RH-sharp |
| 75 | 0.540 | [Goldfeld’s theorem (Euler product at s = 1 ⇒ RH, analytic order)](#goldfeld-bsd) | Cited | RH-sharp |
| 76 | 0.540 | [ℤ̂ in the dictionary: Gal(𝔽̄_q/𝔽_q) ≅ ℤ̂; ℚ⧵𝔸 ≅ (ℝ × ℤ̂)/ℤ; C_ℚ ≅ ℝ₊* × ℤ̂*](#profinite-integers-adelic-solenoid) | Theorem | RH-sharp |
| 77 | 0.540 | [Trace part = polarization (projection onto span{h,v}, ample ω = h + v, ω² = 2), positivity = definiteness of the primitive part relative to it; together = Hodge index on E×E (primitive Gram [[−2,−a],[−a,−2q]] definite ⇔ a² < 4q)](#trace-polarization-primitive-positivity) | Theorem | RH-sharp |
| 78 | 0.540 | [Gas positivities: positive weights ⇒ positive-definite KMS characteristic function and convex log Z; Euler product ⇒ infinitely divisible (free gas). DH fails all; Epstein and ζ(s)ζ(s+a) show none forces RH](#free-gas-positivity-ladder) | Theorem | RH-sharp |
| 79 | 0.540 | [Invariant (χ-type) vs refined (h-type) counts: Lefschetz/GRR totals, N(T), box counts are FE-determined and ghost-blind; the on-line count changes only at collisions; RH ⇔ refined = invariant](#invariant-vs-refined-count) | Theorem | RH-sharp |
| 80 | 0.540 | [Lee–Yang vs Fisher zeros; Newman's Lee–Yang property of Φ ⇔ RH ⇔ Λ ≤ 0](#lee-yang-fisher-rh) | Cited | RH-sharp |
| 81 | 0.540 | [Li criterion](#li-criterion) | Cited | RH-sharp |
| 82 | 0.540 | [Cole–Hopf: Ψ = H′/H obeys backward Burgers ∂_tΨ = −Ψ″ − 2ΨΨ′; at one prime the Toeplitz sequence 2T_k(x_t) is positive-definite iff t ≥ Λ_p; product cross-term −2tΨ_pΨ_q](#burgers-local-toeplitz) | Theorem | RH-sharp |
| 83 | 0.540 | [de Branges spaces](#de-branges) | Cited | RH-sharp |
| 84 | 0.540 | [Hasse bound as a positive degree form](#hasse-pythagoras) | Theorem | RH-sharp |
| 85 | 0.540 | [Suzuki’s de Branges line from the prime side](#suzuki-line) | Cited | RH-sharp |
| 86 | 0.540 | [Bagchi recurrence](#bagchi) | Cited | RH-sharp |
| 87 | 0.540 | [Coupled coils: the Frobenius norm form is a two-coil energy with coupling k = |a_p|/2√p; Hasse ⇔ k ≤ 1; one-factor Laguerre margin 4 log²p (1 − k)](#coupled-coil-hasse) | Theorem | RH-sharp |
| 88 | 0.532 | [Gain lines (active media)](#gain-line) | Analogy | sharp but interpretive |
| 89 | 0.492 | [Near-null direction of ζ's relative Gram matrix](#near-null-anatomy) | Numerical | true but ghost-blind/untested |
| 90 | 0.492 | [The one-box axis: F(ℓ) = W(1_[0,ℓ]) has a uniform rescaled margin on [1, 10], but only by a 1-in-9400 cancellation](#single-box-axis-criterion) | Numerical | true but ghost-blind/untested |
| 91 | 0.492 | [Integer dimension over 𝕊 (minimal generators)](#dim-s) | Numerical | true but ghost-blind/untested |
| 92 | 0.452 | [Hodge index theorem](#hodge-index) | Theorem | true but ghost-blind/untested |
| 93 | 0.452 | [Osterwalder–Schrader reflection positivity](#os-reflection-positivity) | Cited | true but ghost-blind/untested |
| 94 | 0.452 | [Legendre strata: support function / Fenchel–Moreau as a definiteness detector](#legendre-support-function) | Theorem | true but ghost-blind/untested |
| 95 | 0.452 | [Lax–Phillips scattering](#lax-phillips) | Cited | true but ghost-blind/untested |
| 96 | 0.452 | [Weil operator C = i^{p−q} = Wick rotation](#weil-operator) | Theorem | true but ghost-blind/untested |
| 97 | 0.452 | [Hodge–Riemann bilinear relations](#hodge-riemann) | Theorem | true but ghost-blind/untested |
| 98 | 0.452 | [Function-field test of the MP4 headline: over F_q, point counts + functional equation + non-negative integer closed-point counts (an Euler product with positive multiplicities, which implies Ihara’s constraints) do NOT induce the Hodge sign; the sign on the Frobenius-graph Gram comes from the surface C×C (Hodge index), not from the counts](#ff-counts-do-not-induce-sign) | Theorem | true but ghost-blind/untested |
| 99 | 0.452 | [Connes–Consani sites](#connes-consani) | Cited | true but ghost-blind/untested |
| 100 | 0.452 | [Laguerre's formula: angle = (1/2i) log cross-ratio with the circular points](#laguerre-formula) | Theorem | true but ghost-blind/untested |
| 101 | 0.452 | [Pole plane / Tate poles at s = 0, 1](#pole-plane) | Theorem | true but ghost-blind/untested |
| 102 | 0.452 | [Measure versus metric: the product formula gives an invariant measure, not an invariant metric](#haar-measure-not-metric) | Theorem | true but ghost-blind/untested |
| 103 | 0.452 | [Cartan involution / compact unitary group](#cartan-involution) | Theorem | true but ghost-blind/untested |
| 104 | 0.452 | [On a compact manifold a flow conformal on TF with factor e^{αt} has α = 0 (Jacobian e^{αt}, volume conserved); ζ needs α = 1, so the phase space must be solenoidal, with leaf expansion balanced by contraction of a totally disconnected transversal (product formula as volume balance, in Deninger’s elliptic-curve example)](#conformal-flow-needs-solenoid) | Theorem | true but ghost-blind/untested |
| 105 | 0.452 | [Deligne's route: Lefschetz pencils, monodromy and Rankin's tensor-power trick](#deligne-tensor-power) | Cited | true but ghost-blind/untested |
| 106 | 0.452 | [Selberg eigenvalue conjecture ↔ mass shell λ = ¼ + r²](#selberg-eigenvalue-mass-shell) | Cited | true but ghost-blind/untested |
| 107 | 0.452 | [Maxwell construction / convex effective potential](#maxwell-effective-potential) | Theorem | true but ghost-blind/untested |
| 108 | 0.452 | [Products grow linearly (2n), not quadratically](#products-linear) | Theorem | true but ghost-blind/untested |
| 109 | 0.452 | [Weight–monodromy conjecture (Deligne): status](#weight-monodromy) | Cited | true but ghost-blind/untested |
| 110 | 0.452 | [Yoneda specification](#yoneda) | Theorem | true but ghost-blind/untested |
| 111 | 0.451 | [Boosts close into rotations only in imaginary time: Thomas–Wigner (boost commutators are rotations), Cartan duality H³ = SO(3,1)/SO(3) ↔ S³ = SO(4)/SO(3) (p ↦ ip), and Bisognano–Wichmann/Unruh: the Rindler boost is the modular flow of the wedge algebra; its Wick rotation is a Euclidean rotation whose 2π period is the KMS condition (T = a/2π) — arithmetic counterpart: ζ(β) as the primon-gas / Bost–Connes partition function, p^{−it} the time evolution](#boost-rotation-modular-kms) | Heuristic | sharp but interpretive |
| 112 | 0.451 | [Organizing split: ghost-blind = phase, ghost-sensitive = sign](#split-blind-sensitive) | Heuristic | sharp but interpretive |
| 113 | 0.451 | [Definite (Kepler/apsidal) vs gyroscopic (TAA Lemma 4) stability: TAA Lemma 4 has indefinite energy held by the work-free Coriolis J; opposite Krein signs collide at Gascheau–Routh μ = 0.0385209 (Hamiltonian–Hopf quadruple); any dissipation destroys it (Kelvin–Tait–Chetaev); Weil positivity says ζ-type stability must be definite — DH ≈ TAA Lemma 4 past Routh](#gyroscopic-vs-definite-stability) | Heuristic | sharp but interpretive |
| 114 | 0.451 | [Must-fail-for-DH acceptance test](#dh-acceptance) | Heuristic | sharp but interpretive |
| 115 | 0.423 | [BRST / Gupta–Bleuler physical quotient](#brst) | Analogy | background |
| 116 | 0.423 | [Weil template, standing assignment (Missing Piece v5): Deninger's foliation = one factor (½), the Connes–Consani square = the product (½ ⊗ ½), 1 ⊕ 0 = the splitting of the product by the ample class, cusp part split off](#weil-template-factor-product) | Analogy | background |
| 117 | 0.420 | [Γ, the width of a zero: FWHM of its Breit–Wigner line](#gamma-fwhm-of-a-zero) | Restatement | RH-sharp |
| 118 | 0.420 | [Mass shell / even Ξ: s(1−s) = ¼ + t²](#mass-shell-even-xi) | Restatement | RH-sharp |
| 119 | 0.420 | [Two conditions: primitive positivity and pole channel](#two-channel-missing-piece) | Restatement | RH-sharp |
| 120 | 0.420 | [The arithmetic equation of state: primon gas / Bost–Connes dictionary (T, U, S, C, Ω; KMS time; volume options; P_X(β))](#arithmetic-equation-of-state) | Restatement | RH-sharp |
| 121 | 0.420 | [Composite leakage: −F′/F supported on prime powers ⇔ Euler product (unique factorization); DH leaks first at n = 6 (c₆ = 1.9364; also 12, 14, 18, 21, …); along the pencil leakage is 0 exactly at λ = 0, 1 and |c₆| ≈ 7.1λ; Saias–Weingartner ⇒ every 0 < λ < 1 has infinitely many off-line zeros, so ghost births start at λ = 0⁺ as T → ∞; truncated Weil forms (primes ≤ P = 5…13): ζ, χ₅ fail just after log of the next prime, DH at 1.90 for all P (c₆ at log 6)](#composite-leakage) | Restatement | RH-sharp |
| 122 | 0.420 | [Passive arithmetic response of 32a1 (Λ′/Λ as a Foster function)](#arithmetic-response-passivity-32a1) | Restatement | RH-sharp |
| 123 | 0.420 | [Density × density: Weil’s form read off the diagonal and its log n translates](#density-times-density-diagonal) | Restatement | RH-sharp |
| 124 | 0.420 | [Compressed slogan: RH is the Hodge index theorem for Spec ℤ × Spec ℤ, holding with zero margin (Λ = 0); restates Bombieri's 'general index theorem' question; zero margin = dBN time, not a null vector](#rh-hodge-index-zero-margin) | Restatement | RH-sharp |
| 125 | 0.420 | [Why the area is π: the circle in every zero count (Basel as common origin)](#circle-pi-in-zero-counts) | Restatement | RH-sharp |
| 126 | 0.420 | [Weil criterion in push/shear language: pole terms = (hyperbolic) push, −Σ_ρ f̂(ρ) = shear, primes + archimedean = total; degree-0 test functions remove the push; RH ⇔ shear ≤ 0](#weil-shear-subtracts) | Restatement | RH-sharp |
| 127 | 0.420 | [Passive-network reading: RH ⇔ ξ′/ξ(½+w) is positive real on Re w > 0 (Lagarias); lossless on the line; Foster interlacing](#passive-network-positive-real) | Restatement | RH-sharp |
| 128 | 0.420 | [Two-point form g + iω ≥ 0](#two-point) | Restatement | RH-sharp |
| 129 | 0.419 | [Riemann hypothesis (target node)](#rh) | Open | true but ghost-blind/untested |
| 130 | 0.419 | [Hilbert–Pólya](#hilbert-polya) | Open | true but ghost-blind/untested |
| 131 | 0.419 | [Arithmetic Castelnuovo object (C1–C4)](#castelnuovo-object) | Open | true but ghost-blind/untested |
| 132 | 0.419 | [No Riemann–Roch for C_ℚ × C_ℚ (the square is open)](#cc-square-open) | Open | true but ghost-blind/untested |
| 133 | 0.419 | [Conjecture: a no-ghost-type polarisation forced by an algebra with central term 24](#central-term-24-algebra-conjecture) | Conjecture | true but ghost-blind/untested |
| 134 | 0.400 | [One Perron mode against the pole](#pole-perron-one-mode) | Numerical | RH-sharp |
| 135 | 0.400 | [Allowed locally ≠ aligned globally: every Frobenius angle is allowed, but only the genuine assignment keeps the window form positive (Δ and 11a1)](#allowed-locally-not-aligned-globally) | Numerical | RH-sharp |
| 136 | 0.400 | [Ghost onset L* ≈ log(γ/2π)](#ghost-onset) | Numerical | RH-sharp |
| 137 | 0.400 | [The induction matrix on the Q-quotient (Weil form on S-unit lattices)](#q-quotient-induction-matrix) | Numerical | RH-sharp |
| 138 | 0.400 | [Davenport-Heilbronn window jumps](#davenport-heilbronn-window-jumps) | Numerical | RH-sharp |
| 139 | 0.400 | [Dilution law on the path from Davenport–Heilbronn to an Euler product: ℓ*(t) ≈ 5.1 + 2.5 log(1/(1−t))](#dilution-law-dh-to-product) | Numerical | RH-sharp |
| 140 | 0.400 | [Which channel detects a fake depends on the span](#channel-depends-on-span) | Numerical | RH-sharp |
| 141 | 0.400 | [Certified window for one off-line pair](#explicit-ghost-window) | Numerical | RH-sharp |
| 142 | 0.400 | [Which channel an off-line zero breaks first over the rationals](#ghost-channel-order-over-q) | Numerical | RH-sharp |
| 143 | 0.400 | [Crossing scale of a ghost](#ghost-crossing-scale) | Numerical | RH-sharp |
| 144 | 0.400 | [Duursma zeta functions of codes as a finite RH laboratory: Golay satisfies RH; the [32,16,4] code G₂₄ ⊕ e₈ fails](#duursma-code-toy) | Numerical | RH-sharp |
| 145 | 0.400 | [The Laguerre inequality Ξ′² − ΞΞ″ > 0 holds for ζ on [0,60] and fails exactly around the off-line zero of the Davenport–Heilbronn function](#laguerre-detects-offline-zero) | Numerical | RH-sharp |
| 146 | 0.392 | [Curvature as cup square: convexity ↔ Rosati positivity](#curvature-cup-square) | Analogy | sharp but interpretive |
| 147 | 0.392 | [Clausius as candidate positivity: Γ ≥ 0 is automatic, RH = Γ ≡ 0 (reversible / lossless); the working positivity is passivity (ghosts = gain), with Foster ⇔ Laguerre on the line](#clausius-gamma-reversibility) | Analogy | sharp but interpretive |
| 148 | 0.392 | [Time delay (Wigner)](#time-delay) | Analogy | sharp but interpretive |
| 149 | 0.392 | [Källén–Lehmann spectral positivity](#kallen-lehmann) | Analogy | sharp but interpretive |
| 150 | 0.387 | [Integer Ψ_n lattice test (negative result)](#psi-n-lattice) | Numerical | true but ghost-blind/untested |
| 151 | 0.380 | [Global complex structure J on arithmetic H¹ (sharpened missing piece)](#global-j-missing-piece) | Conjecture | RH-sharp |
| 152 | 0.380 | [Hodge energy on arithmetic cohomology, and a torsion term with forced sign](#deninger-hodge-energy-torsion-open) | Open | RH-sharp |
| 153 | 0.377 | [Displaced reference (subtracting the pole)](#displaced-reference) | Heuristic | background |
| 154 | 0.377 | [Formal intersection lattice vs geometric surface (ghost-blind vs proof-bearing)](#formal-vs-geometric-lattice) | Heuristic | background |
| 155 | 0.377 | [Band criterion γ < 2T_M](#band-criterion) | Heuristic | background |
| 156 | 0.377 | [Preserved-leaf contribution χ(L)/|e^{κt} − 1| (Álvarez López–Kordyukov–Leichtnam Thm 1.3.10) has the shape of the archimedean term](#deninger-preserved-leaf-term) | Heuristic | background |
| 157 | 0.365 | [Dedekind zeta of ℚ(i): one pole, exactly one unstable mode, aligned with the pole vector](#dedekind-qi-one-mode) | Numerical | true but ghost-blind/untested |
| 158 | 0.365 | [Talenti template transcribed to Weil: bulk=boundary works on Yoshida's short-support class (ĝ(±i/2)=0 as the boundary condition); W_R alone indefinite by support log 4; total top eigenvalue → 0⁻](#talenti-template-test) | Numerical | true but ghost-blind/untested |
| 159 | 0.365 | [No-go: a ferromagnetic sign pattern fixes the shape of the unstable mode, not the number of unstable modes](#ferromagnetic-sign-not-count) | Numerical | true but ghost-blind/untested |
| 160 | 0.365 | [The admissible prime weights form a thin slab: narrow along total mass, about 30 times wider along mass-neutral directions](#prime-weight-anisotropy) | Numerical | true but ghost-blind/untested |
| 161 | 0.365 | [Search for a structured square root Q (QᵀQ = Weil form) supported on a prime ladder](#structured-gram-factor-search) | Numerical | true but ghost-blind/untested |
| 162 | 0.365 | [How much the primes fill the archimedean deficit of the Weil form, by support](#archimedean-rectifier-fill) | Numerical | true but ghost-blind/untested |
| 163 | 0.365 | [Cutoff saturation (class-number x is not the lever)](#cutoff-saturation) | Numerical | true but ghost-blind/untested |
| 164 | 0.365 | [Genus seen at resolution sigma](#genus-at-resolution) | Numerical | true but ghost-blind/untested |
| 165 | 0.365 | [LMFDB level-1 Maass list complete to T = 100](#lmfdb-maass-complete) | Numerical | true but ghost-blind/untested |
| 166 | 0.365 | [Null-calibrated GLS matched filter](#null-calibrated-gls) | Numerical | true but ghost-blind/untested |
| 167 | 0.365 | [Ghost onset depends on kernel width](#onset-kernel-dependence) | Numerical | true but ghost-blind/untested |
| 168 | 0.365 | [Model kernel e^{−bu²−u⁶}: first zero collision at b_c ≈ 3.1955](#sextic-kernel-collision) | Numerical | true but ghost-blind/untested |
| 169 | 0.360 | [Birman–Krein bridge: scattering phase = spectral shift; −φ′/φ = spectral density = Wigner delay = Maass–Selberg intercept](#birman-krein-spectral-shift) | Theorem | RH-sharp |
| 170 | 0.360 | [Local Newman constant Λ_p = log(|a|/2√p)/log²p (Andrade–Chang–Miller 2014, Lemma 3.18, in time t_ACM = t log²p); Λ_p ≤ 0 ⇔ Hasse; a = 0 ⇒ −∞](#acm-local-newman-constant) | Cited | RH-sharp |
| 171 | 0.360 | [Ghost count of the arithmetic side](#ghost-count-theorem) | Theorem | RH-sharp |
| 172 | 0.360 | [Ghost conventions (δ, heat-flow healing)](#ghost-conventions) | Theorem | RH-sharp |
| 173 | 0.360 | [Two partners of a zero (duality vs conjugation)](#two-partners) | Theorem | RH-sharp |
| 174 | 0.360 | [Frobenius-graph Toeplitz form and its pole/count split](#frobenius-graph-toeplitz-split) | Theorem | RH-sharp |
| 175 | 0.360 | [Negative index κ(𝒬) = N₊ (ghost count)](#kappa-index) | Theorem | RH-sharp |
| 176 | 0.360 | [Castelnuovo-Severi and Weil's bound](#castelnuovo-severi-lemma) | Cited | RH-sharp |
| 177 | 0.360 | [Deninger: Θ a derivation of cup product + positive Hodge ⋆ ⇒ Θ=½+A, A skew ⇒ RH (conjectural cohomology)](#deninger-derivation-positivity) | Cited | RH-sharp |
| 178 | 0.360 | [d* = −⋆d⋆ (dim 4), ∂̄* = −⋆∂⋆, Δ = 2□, [Λ,∂̄] = −i∂*; Hodge-index sign D°² = −‖α_harm‖² from ⋆ = −1 on primitive (1,1)](#dolbeault-kahler-sign) | Theorem | RH-sharp |
| 179 | 0.360 | [Castelnuovo-Severi defect as a Toeplitz block](#fq-cs-block-identity) | Theorem | RH-sharp |
| 180 | 0.360 | [S(T) = (1/π) arg ζ(½+iT): the fluctuating remainder of N(T)](#s-of-t-remainder) | Theorem | RH-sharp |
| 181 | 0.360 | [Shear-to-push density r = T/(2ℓ₊ℓ₋): RH iff r ≤ 1 for push > 0; sup r = 1 unconditionally (log-Gaussians)](#shear-push-density) | Theorem | RH-sharp |
| 182 | 0.360 | [Budget lemma: a 2×2 symmetric H = (τ/2)I + H° is PD iff τ/2 > |H°|; for [[1,a/2],[a/2,p]] this is a² < 4p (Hasse); dBN shrinks only the off-diagonal shear](#trace-shear-budget) | Theorem | RH-sharp |
| 183 | 0.347 | [No-go items 27–32 (Missing Piece v5): per-prime SU(2)/Satake data; per-prime norm identities (a_p² + |α−ᾱ|² = 4p, the ζ mass shell, Kepler's |A|² + 2m|E|L² = (mk)²); correspondence alone (Jacquet–Langlands via Shimizu, functoriality); KMS/coefficient positivity; a compact real form on the zero side as input; single-place data of n!](#nogo-v5-per-prime-and-places) | Theorem | true but ghost-blind/untested |
| 184 | 0.347 | [Connes–Consani Riemann–Roch on Spec ℤ̄ (1-dimensional)](#cc-riemann-roch) | Cited | true but ghost-blind/untested |
| 185 | 0.347 | [Oscillator semigroup: positive ⇔ real A with symplectic eigenvalues ≤ 1 (archimedean, ghost-blind)](#oscillator-semigroup-contraction) | Cited | true but ghost-blind/untested |
| 186 | 0.347 | [Width → area → 2-form: (1/2π)Δ log|ξ| dσ∧dt = Σ δ_ρ](#zero-count-two-form) | Theorem | true but ghost-blind/untested |
| 187 | 0.347 | [Automorphy defect (TAA Lemma 144)](#automorphy-defect) | Theorem | true but ghost-blind/untested |
| 188 | 0.347 | [Certified positivity windows](#certified-windows) | Numerical | true but ghost-blind/untested |
| 189 | 0.347 | [Base-regularity test (B) and the B* no-go: B* (Euler product + counting error O(x^θ), θ < ½ ⇒ RH) appears false — a deterministic discretization of a continuous Beurling system keeps an exact zero at 0.75 ± 10i while the measured counting exponent is θ̂ ≈ 0.29 up to x = 5·10⁷ (Numerical refutation; asymptotic θ < ½ not proved); integer-counting error over 9 systems: ℤ bounded (≤ 1), Davenport–Heilbronn bounded, Epstein and ζ_Q(i) θ̂ ≈ 0.32, random discretizations at order √x](#beurling-counting-test-bstar) | Numerical | true but ghost-blind/untested |
| 190 | 0.325 | [Wick rotation of one Euler frame: t = 2cos θ → 2cos(iφ) = 2cosh φ; elliptic (bounded U_k, poles on |u| = 1 = local unitarity) → parabolic (k + 1, double pole) → hyperbolic (sinh growth); endpoint φ = ½ log p is ζ(s)ζ(s−1) (Eisenstein)](#euler-factor-wick-rotation) | Theorem | true but ghost-blind/untested |
| 191 | 0.325 | [Morse picture of the strata: lobes (extrema), wedge (saddle level), hyperbolic windows (index 1)](#morse-lobes-wedges-windows) | Theorem | true but ghost-blind/untested |
| 192 | 0.325 | [Zeros as frames: simple real zero = elliptic, double zero = parabolic (collision), conjugate pair/quartet = hyperbolic; real zeros leave the line only by collision or from infinity](#zeros-as-frames-trichotomy) | Theorem | true but ghost-blind/untested |
| 193 | 0.325 | [Pole of ζ at s = 1 (residue / 3/π)](#pole-s1) | Cited | true but ghost-blind/untested |
| 194 | 0.325 | [Dual conic (adjugate): ellipse ↔ ellipse, hyperbola ↔ hyperbola, line pair ↔ double point](#dual-conic) | Theorem | true but ghost-blind/untested |
| 195 | 0.325 | [√2 family](#sqrt2-family) | Theorem | true but ghost-blind/untested |
| 196 | 0.325 | [Toeplitz / Verblunsky coefficients](#toeplitz-verblunsky) | Theorem | true but ghost-blind/untested |
| 197 | 0.325 | [Cusp ≠ archimedean place](#cusp-vs-infinity) | Theorem | true but ghost-blind/untested |
| 198 | 0.325 | [F₁ base](#f1-base) | Cited | true but ghost-blind/untested |
| 199 | 0.325 | [Null-line quotient (Gupta-Bleuler form)](#null-line-quotient) | Theorem | true but ghost-blind/untested |
| 200 | 0.325 | [S-mirror ρ ↦ 1 − ρ̄](#s-mirror) | Theorem | true but ghost-blind/untested |
| 201 | 0.325 | [Arakelov geometry](#arakelov) | Cited | true but ghost-blind/untested |
| 202 | 0.325 | [Closed geodesics on the modular surface](#closed-geodesics) | Theorem | true but ghost-blind/untested |
| 203 | 0.325 | [Density / volume reading](#density-volume) | Theorem | true but ghost-blind/untested |
| 204 | 0.325 | [Multi-channel first-order factors are bounded by the SOS fit](#gram-factor-channel-bound) | Theorem | true but ghost-blind/untested |
| 205 | 0.325 | [Principalization](#principalization) | Theorem | true but ghost-blind/untested |
| 206 | 0.325 | [Selberg resonances](#selberg-resonances) | Theorem | true but ghost-blind/untested |
| 207 | 0.325 | [Spec ℤ is terminal](#spec-z-terminal) | Theorem | true but ghost-blind/untested |
| 208 | 0.325 | [Spinor/Clifford route](#spinor-route) | Theorem | true but ghost-blind/untested |
| 209 | 0.325 | [Weil Rosetta stone](#weil-rosetta) | Cited | true but ghost-blind/untested |
| 210 | 0.325 | [Local-to-global failure](#local-global) | Theorem | true but ghost-blind/untested |
| 211 | 0.325 | [Cohesion (arena)](#cohesion) | Theorem | true but ghost-blind/untested |
| 212 | 0.324 | [Kramers–Kronig relations](#kramers-kronig) | Analogy | background |
| 213 | 0.324 | [No-ghost theorem ↔ Gupta–Bleuler quotient of the window form (Analogy)](#no-ghost-gupta-bleuler-analogy) | Analogy | background |
| 214 | 0.324 | [Equivalence-principle gap across a collision: TAA Lemma 157 gap 1 − 2β is 0 before and at the merge and opens ∝ (t* − t)^{1/2} after; RH read as ζ on the EP side, at its edge (at infinity)](#ep-gap-across-collision) | Analogy | background |
| 215 | 0.324 | [Gribov ambiguity](#gribov) | Analogy | background |
| 216 | 0.307 | [Metaplectic / Kubota cocycle](#metaplectic) | Theorem | true but ghost-blind/untested |
| 217 | 0.307 | [Half Tate twist ℚ(½)](#half-tate-twist) | Theorem | true but ghost-blind/untested |
| 218 | 0.307 | [Bost–Connes KMS states](#kms-bost-connes) | Cited | true but ghost-blind/untested |
| 219 | 0.307 | [Functional equation ξ(s) = ξ(1 − s)](#functional-equation) | Theorem | true but ghost-blind/untested |
| 220 | 0.307 | [Gauss-sum unitarity |g| = √p (RH for a CM curve as a unitarity identity)](#gauss-sum-unitarity) | Theorem | true but ghost-blind/untested |
| 221 | 0.307 | [E₂ anomaly (E₂* = E₂ − 3/(πy))](#e2-anomaly) | Theorem | true but ghost-blind/untested |
| 222 | 0.307 | [Half turn = sign flip (S² = −I, root number, Hardy Z sign changes)](#half-turn-sign-flip) | Theorem | true but ghost-blind/untested |
| 223 | 0.307 | [Hecke on S³ (Lubotzky–Phillips–Sarnak): for p ≡ 1 mod 4 the p+1 norm-p quaternions act on S³/±1 and on PSL/PGL(2,F_q) Cayley graphs; constant function eigenvalue p+1 (= ζ frame √p + 1/√p after normalizing), all other eigenvalues |λ| ≤ 2√p (Ramanujan via Deligne/Eichler) = elliptic frames; unique factorization ⇒ (p+1)-regular tree](#lps-hecke-on-s3) | Theorem | true but ghost-blind/untested |
| 224 | 0.307 | [Moser/Souriau: bound Kepler orbits at fixed E < 0 form S²×S² with coordinates j± = (L ± A′)/2, |j₊| = |j₋| = 1/(2√(−2E)); H²(S²×S²) intersection form [[0,1],[1,0]] (signature (1,1): diagonal +2, anti-diagonal −2 — Hodge-index shape); perturbations of a compact orbit average to slow precession of A at fixed |A|, unbound orbits only deflect](#moser-orbit-space-s2xs2) | Theorem | true but ghost-blind/untested |
| 225 | 0.307 | [Nash–Kuiper flexibility / Onsager threshold](#nash-kuiper-onsager) | Cited | true but ghost-blind/untested |
| 226 | 0.307 | [Apsides = zeros of the dual-minus-adjoint gap form: for v′ = Xv, X ∈ sl₂(ℝ), r·v = ½⟨(Xᵀ − X^∨)v, v⟩; apsides are the null lines of the squeeze part; circle ⇔ gap ≡ 0 ⇔ dual = Euclidean adjoint (τ = i)](#apsides-gap-form) | Theorem | true but ghost-blind/untested |
| 227 | 0.307 | [Cup product / Poincaré duality pairing](#cup-product) | Theorem | true but ghost-blind/untested |
| 228 | 0.307 | [Hecke operators](#hecke) | Theorem | true but ghost-blind/untested |
| 229 | 0.307 | [Compact vs non-compact real forms of so(4,ℂ) = sl₂ℂ ⊕ sl₂ℂ: so(4) = su(2)⊕su(2) (Killing (0,6), S³), so(3,1) = sl(2,ℂ)_ℝ ((3,3), H³/Lorentz), so(2,2) = sl(2,ℝ)⊕sl(2,ℝ) ((4,2)); SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ by x ↦ g x h⁻¹ is the F/V animation's own G×G, the non-compact twin of SO(4) on S³; rotation = elliptic, boost = hyperbolic (ζ: φ = ½ log p), null rotation = parabolic](#real-forms-compact-vs-boost) | Theorem | true but ghost-blind/untested |
| 230 | 0.307 | [Archimedean place and Γ_ℝ factor](#archimedean-place) | Theorem | true but ghost-blind/untested |
| 231 | 0.307 | [Euler characteristic χ(D) = dim H⁰ − dim H¹ (Connes–Consani RR)](#euler-char-chi) | Theorem | true but ghost-blind/untested |
| 232 | 0.307 | [Mazur–Wiles main conjecture ("Euler characteristic = L-value")](#mazur-wiles) | Cited | true but ghost-blind/untested |
| 233 | 0.307 | [Connes–Consani 2021: Weil positivity at the archimedean place (support [2^{−1/2}, 2^{1/2}])](#cc21-archimedean-positivity) | Cited | true but ghost-blind/untested |
| 234 | 0.307 | [Cusp forms & Petersson positivity](#cusp-forms-petersson) | Theorem | true but ghost-blind/untested |
| 235 | 0.307 | [What each 𝔽₁ approach builds in place of Spec ℤ × Spec ℤ](#f1-square-constructions) | Cited | true but ghost-blind/untested |
| 236 | 0.307 | [Herbrand–Ribet: ω¹⁻ᵏ eigenspace of Cl(ℚ(μ_p)) and p | B_k](#herbrand-ribet) | Cited | true but ghost-blind/untested |
| 237 | 0.307 | [The n! bridge: n! carries every place (Γ/Stirling at ∞; v_p(n!), Morita's Γ_p and Gauss sums at p), tied by the product formula; each place is ghost-blind, so what is missing is a positivity coupling all places at once](#n-factorial-bridge-all-places) | Theorem | true but ghost-blind/untested |
| 238 | 0.307 | [Ramanujan congruence τ(n) ≡ σ₁₁(n) mod 691 (Δ ≡ E₁₂)](#ramanujan-691) | Cited | true but ghost-blind/untested |
| 239 | 0.307 | [Self-dual / anti-self-dual split as push / shear](#self-duality-push-shear) | Theorem | true but ghost-blind/untested |
| 240 | 0.307 | [Standing frame of the F/V frame geometry: SO(2,2)₀ = (SL₂ℝ×SL₂ℝ)/±1 on AdS₃ = SL₂ℝ (x ↦ g x h⁻¹), compact dual SO(4) on S³ — the unique candidate meeting seven criteria read off the animation (all frame types; trace-preserving conjugation; transitive sweep through t = ±2; real traces only; real form of so(4,ℂ); all Satake frames of ζ and cusp forms; minimal)](#standing-frame-so22-ads3) | Theorem | true but ghost-blind/untested |
| 241 | 0.307 | [Tate count / Picard number (ghost-blind)](#tate-count) | Theorem | true but ghost-blind/untested |
| 242 | 0.307 | [Consani: archimedean cohomology, N at infinity, Γ-factor as a characteristic polynomial](#consani-archimedean-cohomology) | Cited | true but ghost-blind/untested |
| 243 | 0.307 | [PV ↔ TS: dT∧dS = dP∧dV (Maxwell as one area identity); work = heat = enclosed area; PdV, TdS two primitives of one exact 2-form](#pv-ts-symplectomorphism) | Theorem | true but ghost-blind/untested |
| 244 | 0.307 | [Thermodynamic geometry: Ruppeiner/Weinhold metrics, contact structure (Mrugała), and the compatible J that a 2-dim state surface always has](#thermo-geometry-ruppeiner-contact) | Theorem | true but ghost-blind/untested |
| 245 | 0.307 | [λ₂ is monotone under nested windows (Cauchy interlacing)](#lambda2-monotone-nested-windows) | Theorem | true but ghost-blind/untested |
| 246 | 0.307 | [Primary sign rule for a_p of y² = x³ − x](#primary-sign-rule) | Numerical | true but ghost-blind/untested |
| 247 | 0.307 | [Archimedean thresholds a*](#arch-threshold) | Numerical | true but ghost-blind/untested |
| 248 | 0.307 | [Maass–Selberg relations](#maass-selberg) | Numerical | true but ghost-blind/untested |
| 249 | 0.307 | [Legendre-symbol linking matrix of primes ≡ 1 mod 4: spectrally random, indefinite, uncorrelated with Weil positivity](#arithmetic-topology-linking-matrix) | Numerical | true but ghost-blind/untested |
| 250 | 0.307 | [Slack ledger: record close pairs follow z ~ C/d (exponent 1.0±0.15, C ~ π²/(2 log p log q), no sharp constant); same-branch record jumps are exactly continued-fraction convergent denominators of log q/log p; slack left in [0,Z] is d_min(Z)²/8 ≈ C²/8Z²](#slack-ledger-cf) | Numerical | true but ghost-blind/untested |
| 251 | 0.307 | [Monotone quantities along the de Bruijn–Newman flow: kernel-side entropies are smooth through t = 0; zero-side energy relaxes](#dbn-monotone-functionals) | Numerical | true but ghost-blind/untested |
| 252 | 0.292 | [Conjecture-level target: a Hopf-type fibration of Spec ℤ (a global Kustaanheimo–Stiefel map) as a Deninger triple with a compact circle/Bohr-torus flow](#hopf-fibration-spec-z) | Conjecture | true but ghost-blind/untested |
| 253 | 0.292 | [Perelman template: forced monotones of the local flow (|a_eff|, zero log-energy S with Ṡ = 2Σ(∂S)²); a monotone functional for the full product is Open; Galois/curvature link is Analogy](#perelman-template-dbn) | Open | true but ghost-blind/untested |
| 254 | 0.271 | [Zero-margin heuristic: Hodge-index positivity for Spec Z × Spec Z must come from an identity (Weil form = ‖Qg‖², or ⋆ with ⋆²=+1), not an estimate with slack](#identity-not-estimate) | Heuristic | background |
| 255 | 0.271 | [The edge r = 1 as a boundary; ∂∂ = 0 ⇔ d² = 0 as the root of exactness; what survives at the edge as a cycle, i.e. a cohomology class (Deninger)](#edge-boundary-cycle) | Heuristic | background |
| 256 | 0.271 | [RH needs a Kähler package (L, ∂̄, ⋆) for Spec Z × Spec Z under which the trace-free part is a sum-of-squares deficit against the trace push, balanced at zero margin](#kahler-package-one-liner) | Heuristic | background |
| 257 | 0.267 | [Half-density normalization |x|^{½}](#half-density) | Theorem | true but ghost-blind/untested |
| 258 | 0.267 | [Theta inversion θ(1/t) = √t θ(t)](#theta-inversion) | Theorem | true but ghost-blind/untested |
| 259 | 0.267 | [The F/V sweep as an orbit sequence: invariant conics S_t = [[1,−t/2],[−t/2,1]] of g_t keep their apsidal axes at 45°/135° for all t; e_H² = 2t/(t+2); after Bohlin z², Kepler e_K = t/2 = (F+V)/2√q, F/√q = e_K + i b/a; circle → ellipse → parabola (t = 2, F = V, escape) → hyperbola; binding margin 1 − t/2 = 1 − e_K](#apsidal-sweep-eccentricity) | Theorem | true but ghost-blind/untested |
| 260 | 0.267 | [Eisenstein constant term & scattering φ(s)](#eisenstein-ct) | Theorem | true but ghost-blind/untested |
| 261 | 0.267 | [Gauss half: quadratic character, (p ± 1)/2 and the (p + 1)/4 square-root formula](#gauss-half) | Theorem | true but ghost-blind/untested |
| 262 | 0.267 | [Hilbert reciprocity at 2: the odd halves become sign bits](#hilbert-reciprocity-at-2) | Cited | true but ghost-blind/untested |
| 263 | 0.267 | [The prime 2 as the wild place](#prime-two-wild) | Theorem | true but ghost-blind/untested |
| 264 | 0.267 | [Scattering unitarity |φ| = 1](#scattering-phi) | Theorem | true but ghost-blind/untested |
| 265 | 0.267 | [De Bruijn–Newman flow at one prime = the F/V sweep at fixed determinant: a_eff(t) = a e^{−t log²p}](#dbn-local-flow-fv-sweep) | Theorem | true but ghost-blind/untested |
| 266 | 0.267 | [Four squares as the quaternion lift of ζ: Σ r₄(n) n^{−s} = 8(1 − 4^{1−s}) ζ(s) ζ(s−1); r₄(p)/8 = p + 1 ⇒ normalized t = (p+1)/√p = 2cosh(½ log p) — ζ's hyperbolic (boost) frames are the trivial/Eisenstein part; cusp parts appear only for other definite quaternion lattices (B ramified at 11, ∞: θ_O = E + (8/5) f₁₁ₐ₁)](#four-squares-eisenstein-lift) | Theorem | true but ghost-blind/untested |
| 267 | 0.267 | [Fundamental domain of SL₂(ℤ): elliptic (CM points), parabolic (cusp), hyperbolic (closed geodesics)](#fundamental-domain-three-phases) | Theorem | true but ghost-blind/untested |
| 268 | 0.267 | [Half representations of SL(2,F_p): p+4 irreps of dims 1, p, p+1 ((p−3)/2 of them), p−1 ((p−1)/2), and two each of dims (p+1)/2 and (p−1)/2 — the induced rep from the quadratic (Legendre) character splits in half, with unipotent character values (1 ± √(εp))/2 and (−1 ± √(εp))/2, ε = (−1/p) (quadratic Gauss sum); needs F_p a field — the precise place where (p ± 1)/2 separates primes from odd composites](#sl2fp-half-representations) | Theorem | true but ghost-blind/untested |
| 269 | 0.267 | [Yoshida window positivity](#yoshida) | Cited | true but ghost-blind/untested |
| 270 | 0.267 | [Counts vs quadratic positivity](#count-positivity) | Theorem | true but ghost-blind/untested |
| 271 | 0.267 | [Λ = 0 exactly for every finite product of ≥ 2 strictly Hasse degree-2 factors at distinct primes; (a) infinitely many non-real zeros for all t < 0 (Kronecker close pairs + local Rouché on F + sF″; Bohr + Hurwitz), (b) real-rooted for t ≥ 0 (Pólya 1927, Laguerre–Pólya class)](#incommensurable-lehmer-zero) | Theorem | true but ghost-blind/untested |
| 272 | 0.267 | [Kustaanheimo–Stiefel quaternion lift: x = q i q̄ (Hopf map S³ → S², |x| = |q|²) with the bilinear U(1) constraint turns 3D Kepler at energy E into the 4D isotropic oscillator with ω² = −E/2; E < 0 real ω (rotation), E > 0 inverted oscillator (boost) — the Wick rotation; the commutant of the constraint in u(4) is u(2)⊕u(2) ⊃ su(2)⊕su(2) = so(4)](#ks-quaternion-lift) | Theorem | true but ghost-blind/untested |
| 273 | 0.267 | [Legendre ↔ Fourier: stationary phase, half-density amplitude, Maslov phase](#maslov-legendre-fourier) | Theorem | true but ghost-blind/untested |
| 274 | 0.267 | [One cusp, three readings: orbifold, Tate curve, archimedean monodromy](#one-cusp-three-readings) | Theorem | true but ghost-blind/untested |
| 275 | 0.267 | [Push–shear balance: ∫(τ/2)² − ∫|H°|² = ½B with B = ∫(Δu)² − ∫|Hess u|² = ∮[κ(u_n²+u_s²) − 2u_s∂_s u_n] (corner terms on polygons); 0 on ℝ², ½∫K|∇u|² on closed surfaces (Bochner)](#push-shear-balance) | Theorem | true but ghost-blind/untested |
| 276 | 0.267 | [Quartet capacity: which real Lie algebras carry an off-line quartet {±δ ± iγ}: none in so(4) or in sl₂⊕sl₂ on ℝ²⊕ℝ²; yes in so(2,2) on ℝ²⊗ℝ² (a_i + b_j), sp(4,ℝ) ≅ so(3,2) and sl₂ℂ on ℂ²; Krein collision in sp(4,ℝ): only opposite signatures leave the axis — the real form of the frame group does not decide ghosts](#quartet-capacity-sp4) | Theorem | true but ghost-blind/untested |
| 277 | 0.267 | [Split/inert duality for a CM curve (32a1)](#cm-split-inert-duality) | Theorem | true but ghost-blind/untested |
| 278 | 0.267 | [Cone deficit along the local dBN flow: δ(t) = 2π − 2arccos(|a|e^{−t log²p}/2√p) falls to 180° forward and reaches the cusp (2π) at t = Λ_p; past the cusp it is a boost of length log(F/V)](#dbn-deficit-time-to-cusp) | Theorem | true but ghost-blind/untested |
| 279 | 0.267 | [Product obstruction: flow(H₁H₂) − flow(H₁)flow(H₂) = 2e^{t(L₁²+L₂²)}[(e^{2tL₁L₂}−1)cos(L₁+L₂)z + (e^{−2tL₁L₂}−1)cos(L₁−L₂)z]; Λ_global ≠ max Λ_p](#dbn-product-cross-term) | Theorem | true but ghost-blind/untested |
| 280 | 0.267 | [Gauss sum as canonical √(±p)](#gauss-sum-canonical-root) | Theorem | true but ghost-blind/untested |
| 281 | 0.267 | [Johnson–Lippmann operator: a spin-dependent Laplace–Runge–Lenz operator commuting with the Dirac–Coulomb Hamiltonian](#johnson-lippmann-supercharge) | Cited | true but ghost-blind/untested |
| 282 | 0.267 | [Kaluza–Klein circles, the infinite torus, and adelic solenoids](#kk-circle-and-adelic-solenoids) | Theorem | true but ghost-blind/untested |
| 283 | 0.267 | [The 1/24 identities (1/24 = −ζ(−1)/2, η²⁴ = Δ, Θ_Leech) and the verdict: in Weil’s form the 1/24 acts only through the weight](#one-twentyfourth-identities) | Theorem | true but ghost-blind/untested |
| 284 | 0.267 | [Weight ladder (modular weights)](#weight-ladder) | Theorem | true but ghost-blind/untested |
| 285 | 0.267 | [CM case: the Hasse triangle is Fermat's two-squares triangle](#cm-gaussian-hasse-triangle) | Theorem | true but ghost-blind/untested |
| 286 | 0.267 | [Bohlin eccentricity under the local flow: e_K(t) = e^{−(t−Λ_p) log²p}; elliptic → parabolic (t = Λ_p) → hyperbolic, read backward](#dbn-bohlin-decay) | Theorem | true but ghost-blind/untested |
| 287 | 0.267 | [η chain: weight-½ half-density, D log η = E₂/24, E₂* curvature = c₁(ω) (half-volume); half-mass fits only as the L179 equipotential](#eta-chain) | Theorem | true but ghost-blind/untested |
| 288 | 0.267 | [(τ/2)²−|H°|²=det H=½div(Δu∇u−H∇u), det H dx∧dy=d(u_x du_y); on S² the non-exact remainder is ½∫K|∇u|²](#exactness-monge-ampere) | Theorem | true but ghost-blind/untested |
| 289 | 0.267 | [The critical-line wave: Hardy Z and the Riemann–Siegel phase](#hardy-z-critical-line-wave) | Theorem | true but ghost-blind/untested |
| 290 | 0.267 | [E₂* as the derivative of the Kronecker limit (cusp-scattering footprint)](#kronecker-limit-e2star) | Theorem | true but ghost-blind/untested |
| 291 | 0.267 | [Local slack s_p = -Lambda_p = log(2 sqrt p/|a|)/log^2 p; products of Hasse frames at distinct primes have slack 0 (not additive, not min)](#local-dbn-slack) | Theorem | true but ghost-blind/untested |
| 292 | 0.267 | [w₂ / Čech class (TAA Lemma 138)](#w2-cech) | Theorem | true but ghost-blind/untested |
| 293 | 0.267 | [W_R=(1/2π)∫|Φ̂|²K, K=log π−Re ψ(1/4+it/2)=−2θ′ (smooth zero density); K(t₀)=0 at t₀=6.2898=argmin θ](#archimedean-weyl-kernel) | Theorem | true but ghost-blind/untested |
| 294 | 0.267 | [Beta integral, Maslov dequantization and entropy](#beta-dequantization-entropy) | Theorem | true but ghost-blind/untested |
| 295 | 0.267 | [The χ = −1 "effective pole" is half of ζ’s pole, entering through ζ_ℚ(i) = ζ·L(χ₄)](#chi-minus-one-half-pole) | Theorem | true but ghost-blind/untested |
| 296 | 0.267 | [On E×E over ℂ: ⋆² = 1, ⋆ = γ₅ on spinors (up to sign), Λ⁺ = ℝω ⊕ Re Λ^{2,0}, primitive (1,1) = ASD; Hodge index = only SD (1,1) class is ω; τ = (1/12π²)∫(|W⁺|² − |W⁻|²) = 0, blind to RH](#chirality-star-gamma5-hodge-index) | Theorem | true but ghost-blind/untested |
| 297 | 0.267 | [Hecke ladder toy: U_p on ℓ²(ℕ) with J₃ = log n raises J₃ by log p, but [U_p, U_p*] is a projection (Toeplitz/Bost–Connes): a contraction, neither su(2) nor su(1,1)](#hecke-toy-contraction) | Theorem | true but ghost-blind/untested |
| 298 | 0.267 | [One clock per prime: τ_p = t log²p (ACM time); time to the cusp on its own clock is log cos θ̄₀, independent of p; cross-tones run at (log p + log q)², and the 2 log p log q term is the product interaction](#prime-clocks) | Theorem | true but ghost-blind/untested |
| 299 | 0.267 | [Sector map w = e^{iπs/2}](#sector-map-w) | Theorem | true but ghost-blind/untested |
| 300 | 0.267 | [Elliptic/parabolic/hyperbolic as |tr M| = 2r < = > 2 for normalised Frobenius; only SO(2) compact; in RP² the parabola is tangent to the line at infinity (zero-margin edge as tangency); r = 1 forces scalar Frobenius for elliptic curves](#conic-compactness) | Theorem | true but ghost-blind/untested |
| 301 | 0.267 | [Saddles of Euler products: curvature is additive and the cross-prime term at a saddle is always non-positive](#euler-product-saddle-additivity) | Theorem | true but ghost-blind/untested |
| 302 | 0.267 | [The factorial of one half and the Fourier quarter-turn](#fourier-quarter-turn) | Theorem | true but ghost-blind/untested |
| 303 | 0.267 | [Fourth roots: a_p = 0 (supersingular) gives r = 0 over 𝔽_p and the cusp r = 1 over 𝔽_{p²} (a_{p²} = −2p)](#fourth-roots-supersingular) | Theorem | true but ghost-blind/untested |
| 304 | 0.267 | [Kepler: LRL vector closes so(4) = su(2) ⊕ su(2) for E < 0, so(3,1) for E > 0, e(3) at E = 0](#kepler-so4-contraction) | Theorem | true but ghost-blind/untested |
| 305 | 0.267 | [Φ is not in Newman's class 𝒫 (unconditional), so b₀ < ∞; the Lee–Yang property of Φ is RH](#newman-class-p-fails-for-phi) | Cited | true but ghost-blind/untested |
| 306 | 0.267 | [Platonic-point deficits 2π(1 − 1/k) are orbifold cone deficits of S²/G, not Descartes vertex defects; orbifold Gauss–Bonnet: cone deficits + area = 720° (icosahedral 708° + 12°, χ_orb = 1/30)](#orbifold-vs-descartes-deficits) | Theorem | true but ghost-blind/untested |
| 307 | 0.267 | [Ruled quadric through a saddle: null lines, signature (1,1)](#ruled-quadric-null-lines) | Theorem | true but ghost-blind/untested |
| 308 | 0.267 | [so(4)=su(2)⊕su(2): Λ± are commuting rotation subalgebras; D·D=‖D⁺‖²−‖D⁻‖²](#so4-chirality-split) | Theorem | true but ghost-blind/untested |
| 309 | 0.267 | [Spin structure & theta characteristic](#spin-theta) | Theorem | true but ghost-blind/untested |
| 310 | 0.267 | [Three lenses on one Euler factor (analytic factor, det(1 − Frob X), oscillator 2cos(z log p)) carry the same dBN flow; they separate only for products](#three-lenses-one-flow) | Theorem | true but ghost-blind/untested |
| 311 | 0.267 | [Forced functionals of the finite dBN zero gas: dL/dt = 2E, dE/dt ≤ 0; W = L − (n(n−1)/4) log S₂ nondecreasing, constant on Hermite configurations; Y = ΣIm² nonincreasing; de Bruijn envelope y_max(t)² ≤ max(y₀² − 2(t − t₀), 0)](#zero-gas-forced-functionals) | Theorem | true but ghost-blind/untested |
| 312 | 0.256 | ["Cocycles give structure, not sign"](#cocycle-principle) | Heuristic | background |
| 313 | 0.256 | [J. W. McGreevy's flat-potential animation: half-turn polarity flip through a pure wedge](#wedge-flip-animation) | Heuristic | background |
| 314 | 0.253 | [Purity as distortionless transmission: weight strata = attenuation classes](#purity-distortionless) | Analogy | sharp but interpretive |
| 315 | 0.240 | [Hasse triangle and Newton's dT/dθ = L²](#hasse-triangle-newton) | Restatement | RH-sharp |
| 316 | 0.240 | [Net force = push − shear = ⟨g|g⟩_W with shear = prime side (Hodge: net = −D°²); RH iff the net force never points down](#net-force-orientation) | Restatement | RH-sharp |
| 317 | 0.240 | [RH = Hodge index for Spec Z×Spec Z with zero margin; missing piece = identity (balance law) whose leftover is a signed boundary term at ∞ and the pole](#sharpened-missing-piece) | Restatement | RH-sharp |
| 318 | 0.240 | [RH as a negative-square count (restatement)](#ghost-count-rh-restatement) | Restatement | RH-sharp |
| 319 | 0.240 | [Anisotropic part: E×E primitive Gram negative definite iff Hasse (det = 2(a²−4p)); over Spec Z, Q = 1−P removes the pole functionals and Weil’s criterion is T ≤ 0 on the kernel](#anisotropic-part-weil) | Restatement | RH-sharp |
| 320 | 0.240 | [Hodge index in push/shear language: D² = (D·ω)²/ω² + D°², Hodge index ⇔ D°² ≤ 0 (shear can only subtract); D°² = D₀² − ½(D·h − D·v)²](#hodge-index-shear-subtracts) | Restatement | RH-sharp |
| 321 | 0.240 | [Invariant maximal non-positive subspaces: exactly two](#pontryagin-exactly-two) | Restatement | RH-sharp |
| 322 | 0.240 | [Riemann-Roch sorts the two conditions](#riemann-roch-sorting) | Restatement | RH-sharp |
| 323 | 0.240 | [⟨g|h⟩_W=Σ_ρ ĝ(ρ)conj ĥ(1−ρ̄); Hermitian and scaling-isometric unconditionally; RH ⇔ positive semidefinite](#weil-braket-pairing) | Restatement | RH-sharp |
| 324 | 0.226 | [Buoyancy / Archimedes principle](#archimedes) | Analogy | background |
| 325 | 0.226 | [Distortionless line R/L = G/C](#distortionless) | Analogy | background |
| 326 | 0.226 | [Heaviside RLGC line](#heaviside) | Analogy | background |
| 327 | 0.226 | [One log-gas and its frozen limit](#log-gas-frozen-limit) | Analogy | background |
| 328 | 0.226 | [Mass-density positivity](#mass-density) | Analogy | background |
| 329 | 0.226 | [Quasimodular anomaly: E₂(γτ)=j²E₂+(6/πi)cj, E₂=D log Δ connection, ϑ_k=D−(k/12)E₂, curvature −E₄/12; Weil analogue: Γ-factor log-derivative K already present and unsigned](#serre-derivative-analogy) | Analogy | background |
| 330 | 0.226 | [Einstein–Cartan: spin enters as torsion](#einstein-cartan-torsion-spin) | Analogy | background |
| 331 | 0.226 | [Einstein–de Haas lesson: the molecular-current model gave g ≈ 1, the true carrier was spin (g = 2); the missing piece may be a spin-like degree of freedom, not an orbit](#einstein-de-haas-lesson) | Analogy | background |
| 332 | 0.226 | [Viscosity multiplies trace-free strain; dissipation 2μ|S°|² ≥ 0 is the analogue of the missing sign; baroclinic wedge ↔ Gram tilt cos θ = r, net = p sin²θ](#viscosity-baroclinic) | Analogy | background |
| 333 | 0.212 | [Laplace–Runge–Lenz vector: |A| = mk·e, so bound (definite, E < 0) ⇔ |A| < mk; hidden symmetry SO(4) (E < 0, compact, discrete spectrum) / E(3) (E = 0) / SO(1,3) (E > 0) = elliptic / parabolic / hyperbolic; tangential periapsis impulse stretches A (changes the margin), radial impulse rotates A (precession, spectrum-blind)](#lrl-hidden-symmetry-trichotomy) | Analogy | background |
| 334 | 0.212 | [SU(2)×SU(2) as a compact 'product surface': SO(4) = (SU(2)×SU(2))/±1 acts on S³ = SU(2) by x ↦ g x h⁻¹, stabilizer of 1 = diagonal (conjugation, preserves trace = F+V); Peter–Weyl L²(G) = ⊕ V_π ⊗ V_π* is the compact analogue of Künneth; dictionary to Weil's C×C (Δ ↔ diagonal, Γ_F ↔ translate, Lefschetz ↔ trace, Hodge index ↔ Haar positivity, automatic for compact G)](#su2xsu2-peter-weyl-surface) | Analogy | background |
| 335 | 0.212 | [Higgs mechanism: negative mass² at the symmetric point](#higgs-negative-mass2) | Analogy | background |
| 336 | 0.212 | [Klein–Gordon indefinite charge](#klein-gordon-charge) | Analogy | background |
| 337 | 0.212 | [Anomalous dispersion](#anomalous-dispersion) | Analogy | background |
| 338 | 0.187 | [The missing square Spec ℤ × Spec ℤ as the object (collapse ℤ⊗ℤ = ℤ; defect requirements R1–R5)](#missing-square-spec-z) | Open | true but ghost-blind/untested |
| 339 | 0.181 | [Buoyancy reading of the F/V sweep: r=|a|/2√p = shear/push (rescaled frame); elliptic floats (margin s_p=log(1/r)/log²p), cusp neutral, hyperbolic sinks](#buoyancy-reading) | Analogy | background |
| 340 | 0.181 | [Lamb cutoff](#lamb-cutoff) | Analogy | background |
| 341 | 0.181 | [Two different χ’s: Euler characteristic vs class-group character](#two-chis) | Analogy | background |
| 342 | 0.181 | [Ramanujan's 691 as a degeneration of the pole line](#ramanujan-691-degeneration) | Analogy | background |
| 343 | 0.165 | [Candidate formulations of Castelnuovo-Severi over the integers](#cs-for-spec-z-formulations) | Open | true but ghost-blind/untested |
| 344 | 0.165 | [Standard conjectures (Hodge type)](#standard-conj) | Open | true but ghost-blind/untested |
| 345 | 0.165 | [Thermodynamic J direction: Maxwell = symmetry (no sign), Clausius = inequality, ω(x,x)=0; positivity needs a compatible J or a stability Hessian; a rigid work↔heat J is Cauchy–Riemann (harmonic U, indefinite) or forces quadratic U; free primon gas has zero cross-prime covariance, (log ζ)″ is a trivial variance](#thermodynamic-j-direction) | Open | true but ghost-blind/untested |
| 346 | 0.165 | [One operator that is a sum of squares (net ≥ 0 as an identity) and generates dBN (∂_tH = +Δ_z H, backward heat on the real line); stronger than Hilbert–Pólya](#both-at-once) | Open | true but ghost-blind/untested |

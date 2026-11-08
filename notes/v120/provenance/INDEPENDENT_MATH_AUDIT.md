# INDEPENDENT MATH / CITATION / CLAIM-SCOPE AUDIT — Arithmetic Unification VI (32 pp. draft, build of Nov 7 2026 ~10:31 PM CST)
Auditor: atlas1987 bundle executor (not the manuscript writer). Date: Nov 7 2026, ~10:41 PM CST. Scope: full read of abstract, overview,
Chs. 1–10, App. A–B (LaTeX `sections/*.tex` and `pdftotext` of the PDF), the three figures, and `references.bib`. Compared against audited
sources: `/workspace/taa/atlas1987/{AUDIT.md,SYNTHESIS.md}`, `matching1983/PUBLICATION_AUDIT.md`, corrected `moment1975/notes1975.md`,
`localization1970/orient1970.json`, `moment1975/{mom1975,lower1975,diag1975}.json`, and the primary-source texts in `/workspace/taa/lit/`
(Connes math/9811068; Connes–Consani 2006.13771; Connes–Consani–Moscovici 2310.18423; Zagier `lemma49/zagier123.txt`; Deninger `lemma49/den98.txt`).
No writer files were modified. No new research; only hand re-derivations and source look-ups. **RH is not proved, and the manuscript says so consistently.**

## Verdict
**No BLOCKING mathematical errors found.** Every display I re-derived checks, with the conventions the manuscript fixes (F̂(x)=∫F e^{−ixu}, Plancherel 1/2π,
total width A, cutoff log n < A, sesquilinear form linear in the first slot). The claim scope is disciplined: RH, the floor, the matching Target and the
thermodynamic/RH–unitarity completion are all labelled open. TAA's ultimate aim recurs in the abstract, overview, Ch. 1, Ch. 4, the L1–L4 ladder in Ch. 10 and the conclusion, so it is not a token paragraph.
There are **5 IMPORTANT** items. Fix them before freeze; each is a wording or citation fix, not a change to any result. There are also 12 MINOR items.
The Atlas v1.19 citation is treated as temporary staging, per the parent's instruction, and does not block.

## Re-derivations performed (all PASS)
| Anchor (PDF page) | Item checked | Result |
|---|---|---|
| p.7 (2.1)–(2.4) | F̂, L_F(s)=F̂(i(s−1/2)), C_+=L_F(1), C_−=L_F(0); L_{r_{F,G}}(s)=L_F(s)·conj L_G(1−s̄) | PASS |
| p.8 (2.5)–(2.7) | P=2Re(C_+ conj C_−) Hermitian; W=Σ_ρ L_F(ρ)conj L_F(1−ρ̄) equals |F̂(−γ)|² under RH; explicit formula (2.7) equals Guinand–Weil with h=|F̂|², g=r_F, g(0)=‖F‖²=(1/2π)∫|F̂|²; pole terms h(±i/2) give 2Re(C_+conj C_−) | PASS |
| p.8 Thm 2.2 | constrained criterion: CC2021 Intro eq. (2) and App. C, Prop. C.1 (F ⊇ {0,1}) checked in local source | PASS (citation correct) |
| p.8 Prop 2.3 | global density by e^{±R/2} bump corrections, O(e^{−R/2}); window E0 closed codim 2 | PASS |
| p.8 Prop 2.4 | (1/4−∂²)^{−1} kernel e^{−|u−v|/2} (Green's function 1/(2k)·e^{−k|x|}, k=1/2); RF = e^{−u/2}C_+ to the right, e^{u/2}C_− to the left | PASS (see MINOR m1 on the locator) |
| p.9 (3.1)–(3.3), Prop 3.1 | ψ(1/4)=−γ−π/2−3log2 ⇒ K0=−5.37218; DLMF 5.9.16 difference ⇒ Reψ(1/4+ix/2)−ψ(1/4)=∫k_∞(a)(2−2cos xa)da with t=2a; (1/2π)∫(2−2cos xa)|F̂|²=‖F−T_aF‖² | PASS |
| p.9 Thm 3.2 (3.6) | B_A=H_A−M_A‖F‖² off E0; diagonal 2Σa_n cancels; window-enlargement invariance | PASS |
| p.10 (3.8) | m_A(x) ≥ m_A(0) = K0−2Σa_n = −M_A | PASS |
| p.10 (3.9)–(3.10) | k_∞=Σ_j e^{−λ_j a}, λ_j=2j+1/2; ∫e^{−λa}(2−2cos xa)=2x²/(λ(λ²+x²)) ⇒ c_j=2/λ_j=1/(j+1/4), d_j=λ_j²; min_z{x²|f−z|²+d|z|²}=dx²|f|²/(x²+d), minimizer w=F−d(d−∂²)^{−1}F | PASS |
| p.11 (4.1)–(4.6) | Gibbs Z_P, geometric laws, −∂_β log Z=E H, ∂²_β log Z=Var, S=log Z+βE H; a_{p^k}=log p·P_{1/2}(N_p ≥ k); tail-sum capped mean | PASS (see m3) |
| p.12 (4.7)–(4.8) | Z_∞(s)=∫e^{−πx²}|x|^s d*x=π^{−s/2}Γ(s/2); Var=(1/4)ψ'(s/2); 2E_{1/2}log|x|=ψ(1/4)−log π=K0 | PASS |
| p.12 (4.9)–(4.11) | Poisson symbol (1−ρ²)/(1−2ρcos+ρ²)>0; log p(‖F‖²−⟨F,P_pF⟩)=−2Σ_k log p·p^{−k/2}Re r_F(k log p); the covariance enters with a minus sign | PASS |
| p.12 (4.12) | OU series: Re 1/(j+1/4+ix/2)=2λ_j/(λ_j²+x²), matching the O_λ multiplier; digamma series ψ(z)=−γ+Σ(1/(j+1)−1/(j+z)) | PASS |
| p.13 (4.13)–(4.14) | 2∂_σ log|Λ_S| at σ=1/2 equals m_S; ∂_σ‖U_σF‖² at 1/2 equals B_A (all prime powers allowed, as r_F vanishes beyond A) | PASS |
| p.13 (4.16) | Gaussian Z, U=d/(2β), S=(d/2)(1+log(2π/β))−(1/2)log det K | PASS |
| p.14 (5.1), Model | X_H=(H_p,−H_q)=−J∇H for ω(U,V)=g(JU,V)=dq∧dp; H=(2q²−p²)/2 gives Hamiltonian eigenvalues ±√2 and gradient eigenvalues −2, 1 | PASS |
| p.14–15 (5.3)–(5.6) | real/imaginary-time velocities; dE/dτ=−(2/ħ)Var; ∂_z∂_z̄ log N=(1/4)∂²_τ log N=Var/ħ² for z=t−iτ | PASS |
| p.15 Prop (unitarity) | W(T_aF,T_aG)=W(F,G), since e^{a(ρ−1/2)}·conj e^{a(1/2−ρ̄)}=1; conditional on W ≥ 0 | PASS (scope correctly conditional) |
| p.15 (5.7) | uniform law on [−1,1]: overlap sin t/t; generator spectrum is the interval | PASS |
| p.16 (6.1)–(6.4) | Ramanujan system; E L_0=1−E_2; Var L_0=24Σn²q^n/(1−q^n)²=(E_4−E_2²)/12 using d/dβ=−θ; Δ^{−1}=e^βZ_24 | PASS |
| p.16–17 (6.5)–(6.8) | Φ(1/y)=Φ(y); Φ'=2πE_2*; Φ''=(π²/3)(E_4−E_2²)+6/y²; half-trace 3/y²; Hess=diag(−V, V+6/y²); weight k gives k/(4y²) | PASS |
| p.17 (6.9)–(6.10) | Petersson norm finite positive; E_12 coefficient 65520/691; B_10=5/66, B_12=−691/2730; Rankin–Selberg Γ(s+11)(4π)^{−(s+11)}Σ|τ(n)|²n^{−(s+11)} with Γ_∞ ∋ ±1 | PASS |
| p.18 (7.1)–(7.4), Prop 7.1 | τ_S statement = Connes 1999 §VII Thm 4 (local source l.1444); I_S=P−W=−B_A; (χf)^*=χ^{−1}f^*; χ(f*f^*)=g*g^#, g^#(u)=e^{−u}conj g(−u) | PASS |
| p.19 | −i∂_x log c_S = −m_S for c_S(x)=Λ_S(1/2−ix)/Λ_S(1/2+ix) (gives −2Re Λ'/Λ(1/2+ix)); finite S only; no global c≡1 | PASS |
| p.19 | Sonin: CC2021 Thm 1 (support in [2^{−1/2},2^{1/2}], vanishing at i/2 and 0) and CCM Thm 4.6 (hilbertian isomorphism of Sonin spaces) are described correctly and not extended | PASS |
| p.20 (8.1) | real primitive (1,1) is anti-self-dual ⇒ −∫α∧α=‖α‖²; ϑ_h reflection gives g_h(v,v)=a²I(h,h)−I(w,w)>0 | PASS |
| p.20 (8.3) | I(a⊗b,c⊗d)=−E(a,c)E(b,d); all of H¹⊗H¹ is primitive for ω=ω_1+ω_2, because H³(C)=0; mixed real (1,1) negative, (2,0)+(0,2) positive; h−v is primitive with square −2 | PASS |
| p.21 (8.4) | Γ_n² = q^n(2−2g), since the normal bundle ≅ (Frob^n)^*T_C | PASS |
| p.21 Target 8.1, (8.6) | conditional Sylvester lemma, with negative index ≤1 and B(h,h)<0 forcing index exactly 1 | PASS |
| p.21–22 (8.7)–(8.8) | ∇F=(−2t,4) never vanishes; tangents q=pt−p², p²−tp+q=0; M gives T²−4QZ; Q(0,1,1)=−4; polar Q+Z=0 (q=−1); complement T²+4Z²>0; T=0 plane has signature (1,1); [0:1:0] is a smooth point with tangent Z=0 | PASS |
| p.23 (9.2), Prop 9.1 | P=2(|C|²−|S|²) for complex F; congruence proof of the index-one compression criterion (q ≤ 0); index-0 and index-≥2 remarks | PASS — consistent with PUBLICATION_AUDIT Lemma 1 |
| p.24 Table 9.1 + text | −1.11/0.24, −1.98/0.020, −4.28/near 0; Ritz 0.6971/0.01315 (mom1975.json 0.69705, 0.013149); 0.6919/0.0119 (lower1975 0.69185; mom1975 0.01197/diag 0.01183); "not brackets" | PASS |
| p.24 compression table | 0.87903/0.69761/−0.18142 etc. = orient1970.json (correct orientation P̂=M_c H M_c̄) | PASS |
| p.25 (9.6)–(9.8) | weak response includes −M_A h and the paired Gamma integrand; h_2 kink at ±(log2−1/2); jump (a_2/2)sinh(A/4)=0.06191; only n=2 enters at A=1 (log 3 > 1) | PASS (see I3 on the h_1 wording) |
| p.28 App. A Galerkin | H=2∫k(G−R(a))+2Σa_n(G−R(log n)); E_∞ tail 2‖F‖²∫_A^∞k; prime powers below e² are 2,3,4,5,7 | PASS |

## BLOCKING
None.

## IMPORTANT (fix before freeze)
**I1. Finite-H^{1,1} obstruction is asserted, not proved (p.27 §10.3; also p.21 after Target 8.1).**
The text says "a single fixed finite-dimensional H^{1,1} cannot faithfully reproduce an infinite-rank analytic pairing" but never shows that the pairing has infinite rank.
Do not argue "unbounded ⇒ not finite rank": a finite-rank form built from *unbounded* linear functionals can be unbounded. Suggested qualified replacement (unconditional, elementary):
> *Lemma.* Fix a window I. Since Re ψ(1/4+ix/2) → +∞ while the prime cosine sum is bounded by 2Σa_n, there is X with m_A(x) ≥ 1 for |x| ≥ X. Hence m_A ≥ 1 − (1+M_A)·1_{|x|<X}
> and B_A(F) ≥ ‖F‖² − (1+M_A)⟨F, K_X F⟩, where K_X = P_I 𝓕^{−1}1_{[−X,X]}𝓕 P_I is the compact (Hilbert–Schmidt, prolate) time–band-limiting operator on L²(I).
> On the closed finite-codimension spectral subspace of K_X where K_X < 1/(2(1+M_A)), B_A ≥ ½‖F‖². This subspace meets the dense smooth E0(I) in an infinite-dimensional space.
> So B_A = W is positive definite on an infinite-dimensional subspace of E0(I). If Φ: E0(I) → V with −I(ΦF,ΦG) = W(F,G), then W would vanish on ker Φ, which has codimension ≤ dim V. A positive-definite infinite-dimensional subspace meets every finite-codimension subspace nontrivially, so dim V = ∞.
This also gives, for free, that B_A has only finitely many negative directions on a window. That is an honest analytic statement, not a sign result.
Keep the conclusion as is: the target must be an infinite-dimensional, ind-limit or cohomological space with its domain specified.

**I2. Hodge-index citation is secondary only (p.20 §8.1, bib `HodgeSecondary`; App. A "Reference verification policy", p.29).**
A theorem used as an established sign mechanism should cite primary or textbook sources, not only Wikipedia. Add R. Hartshorne, *Algebraic Geometry*, GTM 52, Springer 1977, Ch. V, Thm 1.9 (Hodge index). For the harmonic-form sign (8.1), the Hodge–Riemann bilinear relations, add D. Huybrechts, *Complex Geometry*, Springer 2005, Prop. 1.2.30 / Cor. 3.3.17, or Griffiths–Harris (1978), Ch. 0 §7. The writer should check those locators against the copies before freeze; if they cannot, cite at chapter level. Keep the Wikipedia link only as a secondary pointer.

**I3. h_1 edge-divergence wording (p.25, display after (9.7)).**
"Relative to the smooth continuation cosh(u/2) … relative to the smooth interior expression" is ill-defined as written. For the *untruncated* continuation, k_∞(a)·[2cosh(v/2)−cosh((v+a)/2)−cosh((v−a)/2)] → −cosh(v/2) as a → ∞, so the comparison integral diverges linearly: cosh(u/2) sits at the Gamma pole s=0/1.
Fix: split the integral at a fixed small a_0 < L. The part ∫_{a_0}^∞ is bounded because h_1 is bounded and compactly supported. On [0,a_0] write the integrand as the smooth-continuation integrand, which is O(a) and integrable, plus the missing-translate term ∫_d^{a_0} k_∞(a)cosh((v+a)/2)da = (cosh(L/2)/2)log(1/d)+O(1).
Or quote PUBLICATION_AUDIT Prop. 4 directly (the J_c/J_s decomposition). The conclusion and coefficient ½ for r/cosh are correct: refinement records show 0.689–0.691 per factor of 4 in d, against ½ln4 = 0.693.

**I4. State the combined parity criterion explicitly (p.23–25, §9.1–9.2).**
Prop 9.1 is per-constraint. The final remark on p.25 says the odd sector must be proved separately, but no statement gives full E0(I) positivity. Add, as a corollary for R-invariant finite Galerkin spaces with *invertible* sector blocks:
B ≥ 0 on E0(I) ⇔ [n−(B_e)=0, or n−(B_e)=1 with q_e ≤ 0] **and** [n−(B_o)=0, or n−(B_o)=1 with q_o ≤ 0].
This is PUBLICATION_AUDIT Lemma 2, with its stated hypotheses. Note that n−(B_o)=0 at A=0.6 and A=1 is numerical only, not a general fact.

**I5. Earlier archive items with proof claims (Ch. 1 §1.2, p.6; bib `authorpage`).**
The cited author listing contains earlier deposits titled as RH proofs: ai.viXra 2606.0029 "A Rigorous Analytic Proof of the Riemann Hypothesis…" and 2607.0006 "The Riemann Hypothesis as a Direct Theorem…". The bib note says "no earlier proof claims are adopted", but the main text should say it too.
Add one sentence in §1.2: "Earlier archive items by the author that announced proofs of RH are not relied on; nothing in this manuscript depends on or endorses those claims."
Optionally also list 2610.0046 (TAA Lemma 1: Arithmetic Unitarity…, verified on the public listing tonight) for completeness of the series. The listed IDs and titles for I–V match the public author page (fetched Nov 7 2026 ~10:38 PM CST).

## MINOR
- **m1 (p.8, after Prop 2.4).** "[CC2021, Section 3, Lemma 3]" should be **Lemma 3.3 (ii)–(iii)**: the operator Q(g)=(−(ρ∂_ρ)²+1/4)g, with support-preserving preimage g=Y^**Y^*f (local source l.1131). Sign remark ("opposite sign") correct.
- **m2 (p.9, Prop 3.1).** DLMF locator (5.9.16) agrees with the formula used; keep it. Optionally mention that the paired subtraction is at z=1/4 *before* integrating, which the text already stresses.
- **m3 (p.11, (4.6)).** The left side sums over all p and k with k log p < A, but the right side is written for one p. Write 2Σ_{p<e^A} E_{1/2}[log p·min(N_p,K_p(A))].
- **m4 (p.12, after (4.8)).** Good correction. "Product-formula defect" is rightly not asserted, because no coupling on principal ideles exists. The atlas1987 bundle has been aligned to this wording.
- **m5 (p.24, §9.3).** "overlaps the cosh representer at roughly 97%–99.7%": the sources record |cos∠(c,v_1)| = 0.970/0.991/0.997, including A=2. Say "|cosine| 0.970–0.997 (A=0.6, 1, 2)" so it is not read as squared overlap.
- **m6 (p.28, App. A, "Sine bases …").** The justification "endpoint linear vanishing" fits sine modes but **not** F=(∂²−1/4)G. That F has jumps at ±A/2, since G'' ≠ 0 at the edges (PUBLICATION_AUDIT, domain section).
  Replace with: bounded functions with finitely many jumps lie in Q(I); a smooth interior cutoff χ_ε changes the log-energy by O(ε log(1/ε)), with moments re-imposed by a small smooth correction. That density step is plausible but not proved here, so leave it labelled as such. The text's own disclaimer (p.24) already avoids relying on it.
- **m7 (p.22, Fig. "conic_calibration").** The shaded region is labelled "G positive definite", which is correct since det G = q−t²/4. Add to the caption that this is the region where the projective form M is *negative* (Q(v)=T²−4QZ<0), matching "h has square −4". Use the neutral name **"model discriminant conic"** for the wall, not "Hasse". The atlas1987 bundle figures and storyboard now use this label.
- **m8 (Ch. 8 / any h_s mention; bundle animation).** If the polar family h_s=(0,1,s) is described, state the gauge. In homogeneous coordinates Q(h_s)=−4s. The affine-normalized representative (0,1/s,1) of the same projective point has Q=−4/s. The sign is gauge-independent, the magnitude is not. The bundle animation title now states both.
- **m9 (p.22, §8.5).** "factorial valuations and the Dirichlet inverse Möbius function" is cryptic. Suggest: "Legendre's formula v_p(n!)=Σ_k⌊n/p^k⌋ and the Möbius function μ (Dirichlet inverse of 1, Σμ(n)n^{−s}=1/ζ(s) for Re s>1) encode different operations and imply no sign theorem."
  If the earlier square-free discussion is wanted, state it correctly: Σμ²(n)n^{−s}=ζ(s)/ζ(2s); the fermionic finite-prime ensemble has Z=Π_p(1+p^{−β}), and for all primes with β>1 this equals ζ(β)/ζ(2β). Optional, no new claim.
- **m10 (optional, p.10 (3.9) or p.12 (4.12)).** A one-line remark ties the TAA thread together and is correct: λ_j=2j+1/2 is the distance from 1/2 to the poles s=−2j of Γ_R. For j≥1 these poles are cancelled in ξ by the trivial zeros of ζ. The j=0 pole at s=0 survives in Λ(s), dual to s=1, and is exactly the moment C_− = L_F(0) removed by E0. This is consistent with Prop. 2.4, where rate 1/2 gives support preservation iff both moments vanish. Label it as an observation.
- **m11 (bib).** `CCM2023`: the title "Zeta zeros and prolate wave operators: semilocal adelic operators" (arXiv:2310.18423, v2 4 May 2024) matches the local source. Check whether a journal version exists before freeze; the arXiv citation is acceptable otherwise.
  The other entries agree with what I know of the publications: Connes, Selecta Math. 5 (1999) 29–106; Connes–Consani, Selecta Math. 27 (2021) Paper 77; Deninger, Doc. Math. Extra Vol. ICM 1998 I, 163–186; Zagier, *The 1-2-3 of Modular Forms* (2008) 1–103. I did not re-open the journal pages for those.
  Zagier locators §2.2 (Eisenstein Fourier expansions), §2.4 (discriminant), §5.1 Prop. 15 (Ramanujan) verified in the local copy. Deninger §3 ("conjectural cohomological formalism") verified. Consider adding Auslander–Buchsbaum (1959) for "regular local ⇒ UFD" (p.22) and Iwasawa (1959) for μ, λ, ν.
- **m12 (Fig. "taa_architecture", p.6).** The solid arrow points from "Local ensembles" up to "Arithmetic data". Reverse it, or label it "reproduces", so it does not suggest ensembles generate the arithmetic data.

## Claim-scope checklist requested by parent
| Requirement | Status |
|---|---|
| 2π / Fourier / width A / cutoff log n<A / prime powers | PASS (p.7–9, p.28) |
| E0 moments and P = 2Re(C_+conj C_−); E0 kills P, not M_A | PASS (p.8–10, overview) |
| Positive covariances enter with a minus sign; no divergent unpairing | PASS (p.12) |
| Semilocal trace conventions, twisted star, finite S only, no c≡1 | PASS (p.18–19) |
| Finite inertia with invertibility and exactly one negative eigenvalue; index-0 caveat; both parities; domains | PASS with I4 (combined statement) and m6 |
| Candidate failures: h_1 exact mechanism, h_2 exact at A=1 under hypotheses, A=0.6 numerical only; no universal no-go; singular edge orbits not claimed | PASS with I3 (wording) |
| Projective geometry and Künneth signs | PASS (p.20–22); m7 |
| Surface Hodge metric not an arbitrary positive Kähler metric on W | PASS (p.14 Model, p.20–21) |
| Infinite-dimensional geometric target; no fixed finite H^{1,1} | Conclusion correct; proof missing → I1 |
| Main arithmetic map and sign theorem open; finite calibrations are not constructors | PASS (Target 8.1, Ch. 10) |
| Prior closed routes not reopened (formal graph cycles, naive star, single-compression mismatch, weight-12 selector, σ-convexity, Rosati wrong-space) | PASS (p.19, 22, 24; App. B) |
| Thermodynamics: specified ensembles only, k_B=1, no physical universality claimed; β ≠ A; no ζ ensemble at β=1/2 | PASS (p.11–13) |
| TAA thermodynamic / RH–unitarity aim central and clearly conjectural | PASS (abstract, overview, Ch. 1, 10) |
| Citations real, theorem usage matches sources | PASS with I2, I5, m1, m11 |
| Atlas v1.19 citation | Temporary staging (not blocking); update to the new release URL at freeze |

## Unresolved contradictions found
None between the manuscript and the audited sources. Two places in the atlas1987 bundle were looser than the manuscript, and I have aligned them:
- **E0 minima:** the bundle called them "brackets"; it now says estimates, not certified brackets.
- **M_A reading:** the bundle called it a "product-formula defect"; it now calls it a sum of local mean statistics.

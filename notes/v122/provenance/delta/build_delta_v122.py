#!/usr/bin/env python3
"""Build delta/atlas_delta_v122.json (v1.22 concepts) against the live v1.21 atlas.json.
Priority and ranking are copied from a template concept (never set by hand). rank is null; the insert script assigns it."""
import json, sys, copy
from pathlib import Path
ATLAS=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[2]/'repo'/'atlas.json'
D=json.loads(ATLAS.read_text(encoding='utf-8')); by={c['id']:c for c in D['concepts']}
NOTRH='RH is not proved; Φ is not constructed; there is no Hodge-type sign.'
def R(t,to,note=''): return dict(type=t,to=to,note=note)
C=[]
def add(id,tmpl,label,name,plain,core,axes,rels,numbers=(),pitfalls=(),uncertain='',proved='',tests='',aliases=(),formula=''):
    C.append(dict(id=id,_template=tmpl,label=label,name=name,aliases=list(aliases),plain=plain,core=core,formula=formula,numbers=list(numbers),
                  axes=axes,uncertain=uncertain,proved=proved,tests=tests,pitfalls=list(pitfalls)+([NOTRH] if label in ('Open','Analogy','Restatement') else []),lemmas=[],rels=rels))
# ---------- tonight, organized ----------
add('scaling_graph_family_gamma_u','probe_response_identity','Theorem',
 'Graphs of scaling [Γ_u] for every real u: k∞ from the x∞ = 0 locus, Λ(n)/√n from x_p = 0',
 'On the adèle class space the graph of scaling by e^u, with a half-density weight, is the kernel of the unitary scaling θ_u. Its fixed-point loci give the archimedean kernel and the prime atoms, without using zeros. It is a trace pairing, not an intersection of (1,1)-currents.',
 '⟨[Γ_u],K⟩ = e^{−u/2}∫ K(λ_u x, x) dx; Φ(F) = ∫F(u)[Γ_u]du = kernel of θ(F). Locus x∞ = 0 (all u): index averaged over ±1 = k∞(a) = e^{−a/2}/(1−e^{−2a}). Locus x_p = 0 (u ∈ ℤ log p): atoms log p · p^{−k/2}. Local terms as in Connes 1999, rechecked (gammau2068).',
 ['structure/frame (Ax1)','Spec ℤ gap','ghost-blind'],
 [R('refines','connes_trace','zeros-blind fixed-point side'),R('feeds','arithmetic_class_map_requirements','candidate Φ(F), no ambient'),R('uses','half_density','e^{−u/2} weight')],
 pitfalls=['Not an intersection of (1,1)-currents: the adèle class space has no intersection product.','k∞ comes from the x∞ = 0 locus, not from the diagonal self-intersection.'])
add('renormalized_trace_equals_minus_w_minus_p','probe_response_identity','Theorem',
 'Renormalized fixed-point pairing = −(W − P); on E0 it is −W; the divergence is subtracted, not cancelled',
 'Subtracting the 2 log Λ divergence from the fixed-point trace of θ(F∗G̃) leaves exactly M_A − H_A, which is minus the Weil form without its pole term. On E0 this is −W. No fixed point produces P, and nothing about the sign follows.',
 '⟨Φ(F),Φ(G)⟩_ren = lim[Tr − 2⟨F,G⟩ log Λ] = M_A⟨F,G⟩ − H_A(F,G) = −(W − P)(F,G); −K₀ = γ + log 8π + π/2. Exact window check A = 1.1 (log 2, log 3 active), residual 1.3e−40; nested quadrature 1.4e−16 (cutoff2072).',
 ['sign/positivity (Ax2)','structure/frame (Ax1)','ghost-blind'],
 [R('restates','formal_projection_restates_w','same ledger, t2068 convention'),R('refines','renormalized_pairing_is_semilocal','') if 'renormalized_pairing_is_semilocal' in by else R('related','connes_trace','semilocal, not the global trace'),R('uses','scaling_graph_family_gamma_u','')],
 numbers=['residual 1.3e−40 (A = 1.1, F ≠ G)'],pitfalls=['The ε-pole and the log Λ term have the same sign and never cancel.','Positivity of this pairing on E0 is Weil positivity, i.e. RH.'])
add('sym_asym_boundary_frame','fe_fixed_boundary_class','Theorem',
 'The (h_sym, h_asym) = (2cosh(u/2), 2sinh(u/2)) frame: I-signature (1,1), negative Q-mode aligned with h_sym',
 'The two half-density boundary modes are orthogonal for the trace pairing I = −Q by parity, one positive and one negative. The unique negative direction of Q is even and almost parallel to 2cosh(u/2). Their Riesz lifts carry the same signs.',
 'C±(h_sym) = 2sinh(A/2) + A; C₊(h_asym) = −C₋(h_asym) = 2sinh(A/2) − A. Q(h_sym) < 0 < Q(h_asym) at A = 0.5–3; cos(negative Q-mode, h_sym) = 0.9949 (A = 1), 0.9937 (A = 1.1), 0.9996 (A = 3). Riesz lifts: I(H_sym) ≈ +2.00002, I(H_asym) ≈ −1.98 (A = 1). E0 is not I-orthogonal to h_sym (max |I(F, ĥ_sym)| = 0.378 at A = 1) (framing2073).',
 ['sign/positivity (Ax2)','reference/pole/cusp','numerics/certificate'],
 [R('refines','fe_fixed_boundary_class',''),R('refines','one_negative_direction_certificate','placement of the negative mode'),R('related','pole_block_hyperbolic_plane','')],
 pitfalls=['Alignment and lift values are numerical; only the index count is certified (A = 1, 1.1).','h_sym is not a Q-eigenvector (relative residual 0.19 at A = 1).'])
add('w_of_lift_negative_wrong_test','n2_deletion_ghost_control','Theorem',
 'Correction: "W(H_lift) < 0" is the wrong ample-type test (lock dropped)',
 'Finite W has no negative directions, and under RH W ≥ 0 on the whole window, so asking for W < 0 on a lifted boundary class can never succeed. The coherent tests are Q(h) < 0 for functions and −⟨v, Q⁻¹v⟩ > 0 for Riesz lifts, and both reduce to the certified inertia.',
 'n₋(W) = 0 in every finite model; W(H_sym) = 1.5e−5 (A = 1, n = 1024). The Riesz sign is equivalent, by Haynsworth, to the v1.21 inertia plus the parity placement (framing2073 §6).',
 ['sign/positivity (Ax2)','no-go / refuted'],
 [R('corrects','arithmetic_class_map_requirements','drops the W(H) < 0 lock'),R('uses','bordered_inertia_moment_criterion','')])
add('ff_frobenius_template_forces_half_density','frobenius_graph_toeplitz_split','Theorem',
 'Function-field template: Φ_ff = Σ c_k q^{−k/2} Γ_{Frob^k}; bidegree = (C₋, C₊); Toeplitz forces the half-density; primitive pairing = −W_ff',
 'On C×C over F_q, the Frobenius graphs weighted by q^{−k/2} reproduce the window ledger exactly: the two degrees are the moments C±, the trivial lattice gives P, and the primitive part is −W. The half-density is forced by translation invariance, not inserted.',
 'Γ_k·Γ_l = q^{min(k,l)} N_{|k−l|}; w_k w_l q^{min(k,l)} = f(k − l) forces w_k ∝ q^{−k/2}. Full = P_ff − W_ff; primitive = −W_ff; prime block Γ_k·Δ = N_k gives Λ_ff(n)/√n in du = log q dk. Hodge index ⇒ W_ff ≥ 0. Genus 1 (y² = x³ + x + 1 / F₅) and genus 2 (y² = x⁵ + 2x + 1 / F₃): Toeplitz residual < 3e−15 (prime2087).',
 ['geometry over F_q','sign/positivity (Ax2)','structure/frame (Ax1)'],
 [R('refines','frobenius_graph_toeplitz_split',''),R('refines','ff_weil_form_is_h1_gram',''),R('explains','half_density','forced by Toeplitz invariance'),R('feeds','arithmetic_class_map_requirements','R1–R4 template')])
add('phi_requirements_r1_r4','arithmetic_class_map_requirements','Open',
 'Requirements R1–R4 (and R5) on the class map Φ',
 'From the function-field template: Φ must send u to classes of bidegree (1, e^u), satisfy the min-composition law that forces the half-density, contain a log p fibre component over p that rational equivalence does not kill, and carry ζ (not cusp forms) in its primitive part. Tonight adds R5: Φ must be numerically injective on every window.',
 'R1: bidegree(Γ_u) = (1, e^u), so C± are the degrees and E0 = primitive. R2: Γ_λ·Γ_μ = min(λ,μ)(Γ_{λ/μ}·Δ). R3: Γ_{p^k}·Δ ⊃ a multiplicity-1 component of Arakelov degree log p over p, not rationally trivial (NS of infinite rank). R4: primitive sector carries ζ. R5 (night2105): no window kernel (genus ∞ on every window). Ruled out: P¹_Z×P¹_Z, modular-curve squares, power-map graphs, one real PL chart, CC Riemann–Roch on the square. Candidate only: the Connes–Consani square with Ψ(λ).',
 ['open target','Spec ℤ gap','missing piece'],
 [R('refines','arithmetic_class_map_requirements',''),R('lives-in','mp_ns_psi','R3 = infinite-rank NS'),R('lives-in','mp_h1_square',''),R('uses','ff_frobenius_template_forces_half_density','')])
add('green_current_route2_fails','k0_not_arakelov_degree','Theorem',
 'Route 2 fails: Green currents of scaling graphs on P¹×P¹ give 6 − 4 log|e^u − e^v|, a log height, not k∞',
 'Arakelov-style Green currents for the graphs w = e^u z on P¹×P¹ give an exact closed-form pairing, but it is a logarithmic height with a log singularity, not the archimedean kernel with its pole and e^{−a/2} decay.',
 'dd^c g_u + δ_{Γ_u} = ω; T = ∫(g_u ∗ g_v)∧ω = 6 − 4 log|e^u − e^v| (any fixed metric: universal −4 log|e^u − e^v|). Balanced 6 − 4 log(2 sinh(a/2)); twisted 6 − 4 log(2 cosh(a/2)). Blow-up and comoving metrics add only log cosh and a coth a terms (route22078).',
 ['no-go / refuted','Spec ℤ gap'],
 [R('fails-for','arithmetic_class_map_requirements','no k∞'),R('related','arakelov','')])
add('first_variation_cooked','k0_not_arakelov_degree','Theorem',
 'First variations of [Γ_u] give weight-0 and weight-1 local traces; k∞ needs weight ½ plus a ±1 projection (cooked)',
 'Differentiating the graph family produces Atiyah–Bott-type local traces like 1/(1−q) and −1/sinh²(a/2). The archimedean kernel appears only after inserting a half-density, a sign average and an orientation constant by hand.',
 '−¼∂_u T_raw = 1/(1−q) (q = e^{−a}); ∂_u∂_v T = −1/sinh²(a/2) (metric-independent; FT 4πt coth πt > 0). Cooked identity k∞ = −¼ e^{−a/2} avg A_raw (u > v only) (vary2083).',
 ['no-go / refuted','physics analogue'],
 [R('fails-for','arithmetic_class_map_requirements','cooked k∞'),R('related','green_current_route2_fails','')],
 pitfalls=['The k∞ match is cooked: half-density, sign average and orientation are inserted.'])
add('hecke_square_wrong_target','k0_not_arakelov_degree','Theorem',
 'Hecke correspondences on X₀(N)²: the primitive sector carries L(f,s), not ζ',
 'Frobenius-type Hecke combinations on a modular-curve square have the right bidegree shape, but their primitive intersection numbers give the prime block of weight-2 newforms. ζ appears only in the rank-2 trivial lattice and at the cusp.',
 'T_n·Δ = 2σ₁(n) − Tr(T_n | H¹) (Hurwitz; Eichler–Selberg); Φ_{p^k} = T_{p^k} − pT_{p^{k−2}} has bidegree 1 + p^k and cusp count 2 for all k (p = 2, 3, 5, 7; k ≤ 5). Kronecker–Hurwitz checked for n < 60 (prime2087 §2).',
 ['no-go / refuted','reference/pole/cusp'],
 [R('fails-for','arithmetic_class_map_requirements','R4 wrong target'),R('related','eisenstein_ct','') if 'eisenstein_ct' in by else R('related','arakelov','')])
add('arakelov_p1z_power_graphs_principal','k0_not_arakelov_degree','Theorem',
 'Arakelov P¹_Z × P¹_Z: Γ̂_n = Δ̂ + div̂(f_n), so all intersections are independent of n; no log p',
 'On the arithmetic surface P¹_Z×P¹_Z the graphs of w = nz differ from the diagonal by a principal arithmetic divisor, so every arithmetic intersection number is the same for all n. The finite and archimedean log(n − 1) terms cancel by the product formula, and CH¹_R is only 3-dimensional.',
 'f_n = (w₁z₀ − n w₀z₁)/(w₁z₀ − w₀z₁); finite part 2 log(n−1) over ℓ | n − 1, archimedean −2 log(n−1); total 0 (n < 40, residual 9e−16). Power map w = z^p: fixed points 0, ∞, μ_{p−1}; no log p (prime2087 §3).',
 ['no-go / refuted','Spec ℤ gap'],
 [R('fails-for','arithmetic_class_map_requirements','R3'),R('refines','k0_not_arakelov_degree',''),R('related','arakelov','')])
add('tropical_cartier_r2_genus0','pole_block_hyperbolic_plane','Theorem',
 'Real-weight tropical Cartier model: R2 is a theorem, but the model is genus 0 and reproduces only P (kernel 2cosh(a/2))',
 'With Ψ(μ) = div max(Y − μX, 0) on tropical P¹×P¹, pullback gives μΔ and the composition law R2 holds. But Ψ(e^a)·Δ = e^a + 1, so after the half-density only the pole kernel 2cosh(a/2) appears; there are no prime atoms and no k∞. The min-kernel is positive definite: an ample-type sign on the trivial part only.',
 'G_μ*Ψ(μ) = μΔ; Ψ(λ)·Ψ(μ) = λ + μ; affine |λ − μ|; mixed Monge–Ampère to 1e−9. Pullback conventions: density μ⁻¹Δ, current 1·Δ, Cartier μΔ (only the last satisfies R1). On C_p the degree-μ operator is the semilinear Fr^a_μ (CC Lemma 5.7), a translation on points (r2trop2097).',
 ['structure/frame (Ax1)','reference/pole/cusp','no-go / refuted'],
 [R('special-case-of','phi_requirements_r1_r4','R1 + R2 only'),R('related','tropical_psd_fq_weil_bound',''),R('related','pole_block_hyperbolic_plane','P kernel')],
 pitfalls=['Real slopes and the (1,1)-Cartier calculus are model choices.','"Close to k∞" observations for 1/(2 sinh(a/2)) are cooked (q → q² inserted).'])
add('cc_riemann_roch_no_n2','k0_not_arakelov_degree','Theorem',
 'Connes–Consani Riemann–Roch on the square gives no n² term; the classical n² is the Jacobian with Rosati',
 'Connes–Consani dimensions are log₃-cardinality counts and are additive under products, so χ(nD) is linear in n. On a periodic orbit C_p, Pic⁰ is the finite group ℤ/(p−1), so there is no continuous Jacobian to supply n². On C×C the n² comes from deg(nψ) on the Jacobian, and its sign is Rosati positivity, a closed route.',
 'CC23 (arXiv 2205.01391): box dims 2, 4, 4, 4 = 1-D sums; χ(n(F₁+F₂)) = 4, 6, 10, 16, 32, 60 (linear). CC17 (arXiv 1603.03191): Pic⁰(C_p) = ℤ/(p−1)ℤ; Ψ(μ) Cartier only for μ ∈ ℚ. Classical: χ(nD) = ½D²n² + (1−g)², D² = −W_ff (genus 1: −810, −18630, −89910) (ccrr2098).',
 ['no-go / refuted','Spec ℤ gap','sign/positivity (Ax2)'],
 [R('fails-for','mp_quadratic_rr','no quadratic term'),R('contrasts-with','rosati','classical n² source'),R('lives-in','mp_h1_square','')])
add('real_pl_chart_r2_r3_nogo','k0_not_arakelov_degree','Theorem',
 'No-go: R2 and R3 cannot both hold in one real piecewise-linear chart',
 'In any real PL chart where scaling is Y = μX (required by R1/R2), the intersection with the diagonal at μ = p^k is p^k − 1, and a change of chart only multiplies by a fixed Jacobian. Matching log p for every k would need a k-dependent chart Jacobian (p^k − 1)/log p, which one fixed space cannot have.',
 '|det(n_{p^k}, n₁)| = p^k − 1; chart change: × |det J|⁻¹ fixed; needed |det J| = (p^k − 1)/log p: 1.443, 4.328, 10.10, 21.64, 44.72 for p = 2, k = 1..5. A p-adic determinant |1 − p^k|_p = 1 gives multiplicity 1, not log p; mixing |·|_∞ and |·|_p place by place is the adelic trace route (conversation t2099–t2101; night2105 n1).',
 ['no-go / refuted','Spec ℤ gap'],
 [R('fails-for','phi_requirements_r1_r4','R2 + R3 in one chart'),R('refines','tropical_cartier_r2_genus0','')])
add('determinant_wall_n2_wall','formal_projection_restates_w','Restatement',
 'Two walls: determinant (intersection gives |det(1−dψ)|, the explicit formula needs its inverse × a length) and n² (no continuous fibre Picard object); both crossed classically by the Jacobian / H¹',
 'Every model tried lands on one side of a wall: intersection numbers are determinants, while the explicit formula has the trace shape (length × inverse determinant); and the sign needs a quadratic n² term from a continuous Picard object. In Weil\'s proof the Jacobian crosses both: Lefschetz turns det(1 − Frob | H¹) into fixed-point counts, and the same H¹ gives the n² term.',
 '#Fix(Frob^k) = 1 − Tr(Frob^k | H¹) + q^k. Determinant side: p^k − 1, e^a ± 1. Trace side: log p, k∞. n² side: χ(nD) = ½D²n² + … (conversation t2101–t2102).',
 ['Spec ℤ gap','structure/frame (Ax1)','open target'],
 [R('explains','real_pl_chart_r2_r3_nogo',''),R('explains','cc_riemann_roch_no_n2',''),R('lives-in','mp_h1_square','target: H¹-type object on the scaling site')])
add('connes_cokernel_h1_frechet_l2','cc21_archimedean_positivity','Cited',
 "Connes' cokernel H¹: trace (a) holds after a cutoff, no polarization; Fréchet (trace, no inner product) versus L² (positivity, sees only on-line zeros)",
 "Connes' quotient of L² on the idele class group by the closed range of the summation map is defined without zeros and reproduces the explicit formula as a trace after a cutoff. It lacks a polarization: on the Fréchet version the only natural pairing is W, and on the L² version positivity is automatic but the trace equals the prime side only if RH holds.",
 'H¹ = L²(C_ℚ)/closure(ℰ(𝒮₀)), ℰf(x) = |x|^{1/2} Σ_{q∈ℚ^×} f(qx), f(0) = f̂(0) = 0. Positivity + scaling-isometry + convergence to W on E0 is Weil\'s criterion (not a no-go). A positive scaling-invariant limit forces off-line eigenclasses to have norm zero; it does not decide whether they exist (conversation t2102–t2104).',
 ['Spec ℤ gap','restatement ⇔ RH','sign/positivity (Ax2)'],
 [R('refines','connes_trace',''),R('lives-in','mp_castelnuovo','missing polarization') if 'mp_castelnuovo' in by else R('related','rosati',''),R('restates','weil_positivity','positivity + (1) + (2)')],
 pitfalls=["The dreamer's fibre-class map x ↦ [Σ c_i ψ_{μ_i}(x)] ∈ H¹ is undefined; its n² is W inserted by hand.",'Sonine/prolate spaces as defined are archimedean-only.','The Bochner step overreaches.'])
add('semilocal_prolate_boundary_lead','arithmetic_class_map_requirements','Open',
 'Open lead: the semilocal prolate boundary condition as a zeros-free sign source',
 'In Connes–Consani\'s semilocal prolate framework the self-adjoint extension is fixed by a boundary condition at |x| = λ rather than by the zeros. Whether a sign-definite boundary quantity built only from it controls hypothetical off-line classes is open. The finite-window Krein calculus (pole plane as a boundary condition) gives it a checkable form.',
 'Target: a zeros-free Θ_A in the cone {Θ > 0 : det(Θ⁻¹ + M_A(0)) < 0}, M_A(0) = Bᵀ Q_A⁻¹ B (night2105 N3).',
 ['open target','Spec ℤ gap'],
 [R('uses','pole_plane_krein_boundary_condition',''),R('related','cc21_archimedean_positivity','')])
add('near_null_floor_is_mesh_floor','e0_minima_grid_bias','Numerical',
 'The 1e−5 E0 "plateau" above A = 1.1 is a mesh floor (≈ h^1.8); the eigenvector is smooth and its Fourier transform vanishes at γ₁…γ₈',
 'Refining the cell grid drives the constrained minimum down steadily for A ≥ 1.5, so the plateau is not a level of W. The eigenvector itself is stable: even, two nodes, and its transform vanishes at the first eight zero ordinates to about six digits, the known ζ-cycle phenomenon, which the explicit formula predicts.',
 'A = 2: 1.5e−4, 4.9e−5, 1.28e−5, 3.5e−6, 1.03e−6 for n = 512…8192; A = 1: 0.01186 (converged). Overlaps n → 2n: 0.998–0.9999. f̂(γ_k) errors ≤ 3.5e−5 (A = 3, n = 8192). Gamma-only and two-prime controls lose the γ match (evec2064).',
 ['numerics/certificate','ghost-blind'],
 [R('refines','e0_minima_grid_bias',''),R('reconfirms','infrared_minimiser_nodes','')],
 pitfalls=['Not evidence for RH: a consequence of the explicit formula.','The floor says nothing about the continuum sign above A = 1.1.'])
# ---------- night2105 new connections ----------
add('determinant_wall_product_formula','k0_not_arakelov_degree','Theorem',
 'The determinant wall is the product formula: the graph of ×p^k meets Δ over the primes ℓ | p^k − 1, never over p',
 'A real chart counts p^k − 1 fixed points for scaling by p^k: the points of the torus G_m over F_{p^k}, a genus-0, weight-0-and-2 count. By the product formula, log(p^k − 1) is a sum of log ℓ over primes ℓ ≠ p dividing p^k − 1, and the p-adic size of 1 − p^k is 1. So the determinant is owned by other primes; a log p atom at p must be a vertical fibre degree.',
 'p^k − 1 = #G_m(F_{p^k}), p^k + 1 = #P¹(F_{p^k}); half-density: e^{−u/2}(e^u ∓ 1) = 2 sinh(u/2), 2 cosh(u/2) = h_asym, h_sym. log(p^k − 1) = Σ_{ℓ | p^k−1} v_ℓ log ℓ; |1 − p^k|_p = 1. Checked for all p^k ≤ 10⁶, p < 60: error 1.8e−15 (night2105 n1).',
 ['Spec ℤ gap','structure/frame (Ax1)','no-go / refuted'],
 [R('explains','real_pl_chart_r2_r3_nogo',''),R('explains','arakelov_p1z_power_graphs_principal','same cancellation'),R('explains','tropical_cartier_r2_genus0','genus 0 = Tate part only'),R('refines','determinant_wall_n2_wall','')],
 tests='Any Φ candidate: does Ψ(p^k) ∩ Δ have a vertical component over p?')
add('window_shioda_tate_split','one_negative_direction_certificate','Theorem',
 'Finite-window Shioda–Tate split: n₋(W|E0) = n₋(Q) − n₋(S); Hodge index for I = −Q is one bound state of H_A below M_A',
 'Take the Riesz lifts of the two moments as a "trivial lattice". E0 is exactly its orthogonal complement for the zeros-blind pairing I = −Q, so the signature splits as (trivial lattice) ⊕ (E0). E0-positivity is the statement that the two negative counts agree; "exactly one positive direction of I" is H_A having one eigenvalue below M_A.',
 'Triv = span{Q⁻¹r±}; I|Triv = −S, I|E0 = −W, E0 = Triv^{⊥_I}; In(I) = In(−S) ⊕ In(−W|E0). ζ: n₋(Q) = n₋(S) = 1 at A = 0.694–2.5 (n = 256, 512); identity holds in 84/84 runs. Controls (prime weights × s, not Euler data): at A = 1.5 and 2 only s = 1 is E0-positive at resolution 0.01; failures raise n₋(Q) (to 2–10) with n₋(S) = 1; deleting n = 2 at A ≤ 1.1 gives n₋(Q) = n₋(S) = 2 (absorbed) (night2105 n2, n2c).',
 ['sign/positivity (Ax2)','structure/frame (Ax1)','ghost-sensitive','numerics/certificate'],
 [R('refines','bordered_inertia_moment_criterion','orthogonal-sum form'),R('analogue-of','faltings_hriljac_statement','trivial lattice ⊕ height lattice'),R('analogue-of','hodge_index',''),R('refines','weil_hodge_index_one','')],
 numbers=['84/84 identity checks','only s = 1 positive at A = 1.5, 2 (step 0.01)'],
 pitfalls=['Counts are numerical; n₋(Q) = 1 is certified only at A = 1, 1.1 (v1.21).','The continuum identity needs Q invertible on a stated domain (not verified).','s ≠ 1 and deletions are sensitivity controls, not Euler data.'])
add('riesz_lifts_as_fibre_classes','e0_minima_grid_bias','Numerical',
 'The Riesz lifts of C± behave like the fibre classes f₁, f₂: Gram −S → J (isotropic, mutual pairing 1)',
 'In the function field the trivial lattice is spanned by two isotropic fibres meeting once. The Riesz lifts of the window moments have almost exactly that Gram for A ≥ 1: self-pairings near 0 and mutual pairing near 1, improving under refinement.',
 'A = 1.1, n = 1024: I(H₊,H₊) = 9.6e−4, I(H₊,H₋) = 0.99905; A = 3, n = 1024: 1.4e−5, 0.99999. A = 0.5: 0.514, 0.525 (not U-like). The defect tracks the W mesh floor via Woodbury S = −(I − JR⁻¹)⁻¹J, R = BᵀW⁻¹B (night2105 n2b).',
 ['numerics/certificate','reference/pole/cusp','structure/frame (Ax1)'],
 [R('illustrates','window_shioda_tate_split',''),R('analogue-of','light_cone_U','U = ⟨f₁, f₂⟩'),R('related','near_null_floor_is_mesh_floor','mesh-dependent defect')],
 pitfalls=['Mesh-dependent: no continuum claim that the Gram equals J.'])
add('pole_plane_krein_boundary_condition','bordered_inertia_moment_criterion','Theorem',
 'The pole plane is a boundary condition: Q_Θ = Q + BΘBᵀ (Θ = 0: Q; Θ = J: W; Θ → ∞: W|E0), Krein formula with a 2×2 Herglotz Weyl function',
 'The pole term is one member of a two-parameter family of boundary perturbations. Krein\'s formula reads the spectrum of each member off a 2×2 Weyl function M(λ); the E0 spectrum is where det M vanishes. With one negative direction of Q, E0-positivity is det M(0) < 0, equivalently some positive boundary penalty makes the whole-window form positive.',
 'det(Q_Θ − λ)/det(Q − λ) = det(I + ΘM(λ)), M(λ) = Bᵀ(Q−λ)⁻¹B, M′ ≥ 0. Penalty Θ = cI: c* = 1/|λ_min M(0)|; |C₊|² + |C₋|² − P = |C₊ − C₋|² ≥ 0, so W ≥ 0 on the window ⇒ c* ≤ 1. Numbers: c* = 0.99997 (A = 1.1), 0.99999 (A = 1.5, 2); relative σ_min of M at W|E0 eigenvalues 1e−6–1e−15 vs 0.02–1 at midpoints (night2105 n3, n3b).',
 ['sign/positivity (Ax2)','structure/frame (Ax1)','reference/pole/cusp'],
 [R('refines','bordered_inertia_moment_criterion','resolvent form'),R('related','lax_phillips','boundary/scattering reading'),R('feeds','semilocal_prolate_boundary_lead','admissible cone for Θ_A'),R('uses','window_shioda_tate_split','')],
 pitfalls=['A reformulation, not a sign source.','Continuum version needs a boundary triple on a stated domain (not built).'])
add('near_null_cayley_hamilton_genus_infinity','frobenius_graph_toeplitz_split','Theorem',
 'Near-null = numerically trivial (Cayley–Hamilton) over F_q; for ζ no window has an exact kernel ("genus ∞")',
 'Over a finite field the Weil Toeplitz form on any window has rank 2g, and its kernel is exactly the relations among Frobenius graphs given by the characteristic polynomial of Frobenius. For ζ, completeness of the zero exponentials on every interval means W has no exact kernel on any window: the near-null cluster is a shadow of infinite genus, not a finite relation.',
 'W_ff Toeplitz on k = 0..K: rank min(K+1, 2g); kernel = multiples of L̃(x) = ∏(x − β_i); G − P = −W_ff. Genus 1 (F₅) and genus 2 (F₃): residuals ≤ 1e−12. ζ (under RH): W(F) = Σ|F̂(γ)|²; N(T) ~ (T/2π) log T gives infinite density, so {e^{iγu}} is complete on every I_A (Beurling–Malliavin / Levinson) (night2105 n4).',
 ['geometry over F_q','structure/frame (Ax1)','Spec ℤ gap'],
 [R('refines','frobenius_graph_toeplitz_split',''),R('explains','near_null_floor_is_mesh_floor','genus-∞ shadow'),R('constrains','phi_requirements_r1_r4','R5'),R('analogue-of','standard_conj','hom vs num')],
 pitfalls=['Fréchet/L² ↔ homological/numerical equivalence is an analogy only.','The ζ statement uses RH only to write W as a sum of squares.'])
out=dict(base=dict(version='v1.21',concepts=len(by),relations=sum(len(c['rels']) for c in D['concepts'])),proposed='v1.22',
         added_concepts=len(C),added_relations=sum(len(c['rels']) for c in C),concepts=[])
ids={c['id'] for c in C}
for c in C:
    t=by[c['_template']]
    c2=dict(c); c2['priority']=t['priority']; c2['ranking']=copy.deepcopy(t['ranking']); c2['rank']=None
    for r in c['rels']:
        assert r['to'] in by or r['to'] in ids, (c['id'],r['to'])
    assert c['id'] not in by, c['id']
    out['concepts'].append(c2)
p=Path(__file__).resolve().parent/'atlas_delta_v122.json'
p.write_text(json.dumps(out,indent=1,ensure_ascii=False)+'\n',encoding='utf-8')
print(out['base'],out['added_concepts'],out['added_relations'])

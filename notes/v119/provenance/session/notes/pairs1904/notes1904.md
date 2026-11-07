# pairs1904 — non-commuting pairs: position/momentum & energy/time analogues in pure math (t1904; RH not proved)
checks1904.py verified: prime isometries ([H,S_p]=log p S_p, S_p*S_p=I, S_pS_p*=P_p, S_p*S_q=S_qS_p* p≠q, [X_p,Y_p]=−(i/2)(I−P_p), [H,X_p]=i log p Y_p, Gibbs φ_β(P_p)=p^{−β});
affine [D,e^u]=−i e^u; Lefschetz sl2 on H*(P¹×P¹): [H,L]=2L,[L,Λ]=H; ample² = 2 > 0, primitive (h1−h2)² = −2 (Hodge index sign).

## Corrections to obs1902
C1 Commutative positive states CAN be independent: on the convolution *-algebra C_c^∞(R) (product *, involution ♯), a positive functional = positive-definite distribution = (Bochner–Schwartz) Fourier transform of a positive tempered measure; an independent construction of that measure would suffice. Non-commutativity is needed only for a NONZERO RS commutator, not for positivity. "Bochner trap" overstated.
C2 W is unbounded (K(D) ~ log|ξ|): it is not a normalized state on the C*-algebra of bounded translations (those give bounded positive-definite functions). Proper object: positive functional/weight on the test-function *-algebra (Wightman/distributional), or semifinite weight/trace.
C3 Theta inversion ⇒ FE (Riemann) is a one-way implication; do NOT read FE ⇔ modularity (Hamburger characterizes ζ by FE + Dirichlet-series conditions; converse theorems are separate).
C4 σ_∂ exclusion stands only as a direct consequence of RS for that σ under the Hermitian complex extension: RS ⇔ W(F) ≥ (ħ/2)⟨F,DF⟩ ∀ complex F∈E0⊗C (real F give ⟨F,DF⟩=0, so modulation is essential). It rules out a normalization; it is not stronger than RS and gives no sign information.

## Ranked pairs
1 (Q0,D) on (E0∩C_c^∞, G0): [Q0,D]=i, [Q0,T_a]=aT_a, window-preserving; G0 reference geometry, W=h(D) stiffness, [Q,h(D)]=i h'(D) on core for smooth K; prime part finite only as form on a fixed window. τ=spec D = Mellin frequency (s=½+iτ): u↔τ is THIS pair, not a second energy-time pair. Re s−½ = exponential weight e^{(σ−½)u} (non-unitary continuation), not conjugate to u; zero ordinates = hoped spectrum of something, here only support of W's spectral symbol (explicit formula).
2 Affine (D, X=e^u) and additive characters ⋊ scaling: [D,X]=−iX, X>0 (semibounded like Pauli), T_aM_ξT_a^{−1}=M_{e^{−a}ξ}. Arithmetic enters via Q ⊂ A_Q discrete cocompact, self-dual Fourier/Poisson (Tate) ⇒ FE, not W positivity. CC21 Sonin space lives here.
3 Prime number–phase pair (S_p,H) on ℓ²(N)=⊗_p ℓ²(N_0): S_p = unilateral shift of v_p (Toeplitz isometry, not boson a†), H=Σ log p N_p. Number–phase analogue (Susskind–Glogower: no self-adjoint phase; boundary projection I−P_p). Positive KMS state β>1 independent but sees ζ(β); spec H = {log n}, no W match. BC partial isometries μ_n = this prototype (source-level).
4 Energy–time: time a parameter; Pauli: semibounded H ⇒ no s.a. T with Weyl relation (domain-level exceptions exist); Mandelstam–Tamm ΔH ΔA ≥ (ħ/2)|d⟨A⟩/dt|; modular flow Δ^{it} = intrinsic time of a state (Tomita), prime gas: σ_t(S_p)=p^{it}S_p; bandwidth–duration (Fourier) is pair 1 again.
5 Lefschetz sl2 (L=∪ω, Λ, H=deg−n): exact, and Hodge–Riemann positivity on primitive classes is a SIGN source (ample + sl2), unlike pairs 1–4. Absent over Q (analogy). Deformation/response (β,⟨H⟩) are Legendre (Fenchel) conjugates, convexity not commutator.
Pure Gaussian minimal uncertainty ⇒ compatible positive J; does not explain the arithmetic metric.

## Next test (not launched)
Prime-isometry boundary sums: regularized Tr(e^{−βH}(I−P_p)) = ζ(β)(1−p^{−β}); test whether the pole term P=2ab (ev_0, ev_1) arises exactly as residue/defect (β→1) of boundary contributions of an admissible map F ↦ A_F built from S_n, i.e. an arithmetic admissibility law vs pole constraint. No positivity claimed.

# obs1902 — arithmetic observables & adjoints; modularity recall (t1902; continues rs1901; RH not proved)
Recall: SearchTranscripts returned "no record" for this session; recovered via RecallMemory (paraphrased profile facts, NOT verbatim) + STATE.md:
- 2026-10-29: "whether modular invariance of observables is why the genuine Frobenius-angle assignment knows the zeta zeros" (answer then: modularity ⇒ FE + continuation, separates genuine from shuffled Hecke-consistent angles; Cardy/bootstrap analogy).
- 2026-10-31: SL2(Z) on binary quadratic forms as "the same form seen by different observers" (j-invariant, D=0 cusp).
- Lemma 31 (STATE §40): Tomita–Takesaki/KMS — ξ(1+it) is a KMS_1 two-point fn ⇔ FE, unconditional ⇒ not the positivity source. BC95 KMS: ζ(β), real β, zeros-blind.
- L103: two-point THM (J=i restatement), scaling-invariant state ⇔ RH (circular), real test fns: ω from odd part ≡ 0. L104: (σ,σH) Euclidean pair, J=Hilbert transform commutes with scaling, ghost-blind.

## Conventions
H=L²(R,du) log line, F(u)=e^{u/2}f(e^u) (unitary from L²(R+,dx)). T_a h(u)=h(u−a), T_a*=T_{−a}; D=−i∂ (T_a=e^{−iaD}); Q=u.
checks1902.py (sympy): [Q,T_a]=aT_a, [D,T_a]=0, [Q,D]=i, e^{isQ}T_a=e^{isa}T_a e^{isQ}, T_a M_ξ T_a^{-1}=M_{e^{-a}ξ} (M_ξ=e^{iξe^u}), ev_s(T_aF)=e^{(s−½)a}ev_s(F), ev_s(DF)=i(s−½)ev_s(F).

## Ledger (operator | adjoint | preserves E0? window? | status)
T_a | T_{−a} (L² and G0) | yes / shifts window by a | EXACT
O(F)=∫F(a)T_a da = F* | O(F^♯), F^♯(a)=conj F(−a); s.a. iff F=F^♯ (real F: iff even) | yes (ideal) / support grows by supp F | EXACT
X(F)=O(F_+), Y(F)=O(F_−) with F_+=(F+F^♯)/2, F_−=(F−F^♯)/(2i) | self-adjoint | yes | EXACT; all commute: abelian => σ=0 (matches L103 'odd part ≡ 0')
C_n=T_{log n}+T_{−log n}=2cos(D log n) | s.a., mutually commuting | yes / shifts | EXACT
W|E0 = ⟨F,[K(D) − Σ a_n C_n]F⟩ (P=0 on E0) | function of D: stiffness/Hamiltonian, not a measured oscillator | — | EXACT (prime sum finite on window)
D | s.a. in L² and G0 (commutes with L) | yes / yes | EXACT
Q | s.a. L² | NO (moments) | EXACT
Q0=L Q L^{-1} | G0-symmetric: G0(Q0F,G)=⟨QL^{-1}F,L^{-1}G⟩ | yes / yes (L^{-1}F supported in hull of supp F) | EXACT; prior art CC21 Lemma 3
[Q0,D]=i, [Q0,T_a]=aT_a on (E0,G0) | — | — | EXACT but = Schrödinger rep transported by L (zeros-blind, arithmetic-free)
M_ξ (additive char on x=e^u) | M_{−ξ} | no (changes moments) | EXACT; affine/ax+b enlargement, adelic version = adele class crossed product (Connes) — SOURCE-level, state OPEN

## Key points
- Bochner trap: a state on the abelian translation algebra with φ(O(F)*O(F))=W(F) is exactly a positive-definite distribution = GNS of W (premise). Independence must come from a noncommutative extension whose positivity is structural (vector/density state, CC21 compression), with W as restriction.
- RS normalization test: with local σ_∂(F,G)=∫F G' (real E0), RS "W + iħσ/2 ≥ 0" needs W(F) ≥ (ħ/2)⟨F,|D|F⟩; on a fixed window W(F) ≤ (log(2+|ξ|)+C)‖F‖² for modulated bumps ⇒ inf ratio = 0 ⇒ fails for every ħ>0. Excludes "W = covariance w.r.t. σ_∂" (normalization exclusion, not sign info). Bounded σ (Hilbert-type) remains admissible -> threshold ħ*=2·inf W/‖F‖²-type, tied to near-null μ_min.
- Modularity meanings: (A) SL2(Z)/theta inversion ⇒ FE ⇔ Hermiticity (adjoint law), not positivity; (B) Tomita–Takesaki ⇒ modular group of a GIVEN faithful state, KMS ⇔ FE (L31), unconditional; (C) scaling modulus |λ| = Haar module (geometry1897 conformal e^t); (D) Galois modularity/Hecke: Petersson-positive, T_p self-adjoint, commutative ⇒ real eigenvalues, not Ramanujan, no σ.
## Target (not launched)
φ on C*(additive ⋊ scaling) / adele class crossed product, positive by construction, computed from primes/Γ/poles, with φ(O(F)*O(G)) = W(F,G) on E0∩C_c^∞([−L,L]); must be undefined/non-positive on DH data.

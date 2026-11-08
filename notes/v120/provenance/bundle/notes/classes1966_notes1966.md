# classes1966 (t1966; Nov 7 2026 ~8:45 PM CST; RH NOT proved). Scratch only. tau1966.py/json.
Sources read this turn (local copies): Connes 1999 math/9811068 (lit/lemma30/math_9811068.txt): §VII Thm 4 (p.31), (VII.1-13),
 §VIII Cor 2, eq (16), Thm 5 + proof eqs (17)-(26) (pp.41-43); Connes-Consani arXiv:2006.13771 (lit/2006.13771.txt): Thm 1, Thm 3 (4.7), intro.
Supersedes map1965 wording: the Q "graph integral" there was FORMAL; pairing there was defined from bulk. Here the functional is defined first.

## 1. Candidate objects (all independently defined; none uses W, sqrt W, or a sign)
 S finite set of places of Q, S ⊇ {∞} ∪ {p < e^A}.  C_S = J_S/O_S^* ≅ R_+^* × Π_{p∈S} Z_p^*.  X_S = A_S/O_S^*.
 "Correspondences": A_S^ur = unramified C_c^∞(C_S) ≅ C_c^∞(R_+^*), convolution, involution f^*(λ)=conj f(λ^{-1}); act by
   U(h)=∫h(λ)U(λ)d*λ on L^2(X_S) (Connes (VII.5) inner product Σ_{q∈O_S^*}|f(qx)|^2|x|d*x; U(λ)ξ(x)=ξ(λ^{-1}x)).
 Measures: d*λ on C_S with ∫_{|λ|∈[1,Λ]} ~ log Λ (VII.4); local k_v^* embedded => d*u = du/(2|u|) on R^*, mass log p per shell on Q_p^*.
 Cutoffs: P_Λ (|x|≤Λ), P̂_Λ = F P_Λ F^{-1} (F depends on α=Πα_v), R_Λ = P̂_Λ P_Λ (not positive).
 Trace functional (paired finite part, ONE counterterm whose coefficient h(1) is intrinsic):
   τ_S(h) := lim_{Λ→∞} [ Tr(R_Λ U(h)) − 2 h(1) log'Λ ],   2 log'Λ = ∫_{|λ|∈[Λ^{-1},Λ]} d*λ  (= Tr(S_Λ V(f)) / f(1), Connes VIII).
 Pairing: I_S(h1,h2) := τ_S(h1 * h2^*)   (sesquilinear; Hermitian since the geometric side is real for real-symmetric data).
 Dictionary to our window: h(e^s) = e^{-s/2} r(s), r = F ⋆ F~ (autocorrelation); ĥ(z)=∫h|u|^z d*u, ĥ(0)=ev−, ĥ(1)=ev+ products: ĥ(0)+ĥ(1)=P.

## 2. Ledger (status per equality)
 (L1) τ_S(h) exists and = Σ_{v∈S} ∫'_{k_v^*} h(u^{-1})/|1−u| d*u, ∫' fixed by α_v (FT of the extension vanishes at 1).
      [THEOREM, Connes Thm VII.4, statement read from source; hypotheses: S finite, h ∈ S(C_S) compact support; semilocal only.]
 (L2) p-adic local term (unramified h, p∈S) = Σ_{k≥1} log p · p^{-k/2}·2 r(k log p) = 2 Σ_{p^k} Λ(n)n^{-1/2} r(log n).
      [EXACT: shells |u|=p^{∓k}, |1−u|_p = 1 or p^k; unit shell contributes 0 (consistent with Connes App.2 (26), log|d^{-1}|=0 for Q).]
 (L3) archimedean term = FP∫_R k(|t|) r(t) dt + (γ + log 2π) r(0), FP = unit-cutoff finite part; transverse weight
      Σ_± e^{t/2}/|1∓e^t| = 2k(|t|), halved by d*u normalisation. Constant: α_∞-condition FT[T0(·−1)+cδ_1](1)=0 ⇒ c=2(γ+log2π).
      [EXACT derivation; matches K0 = −(log2π+γ+FP∫_0^∞2k) of map1965.]
 (L4) Window lemma: if supp r ⊂ [−A,A] and S ⊇ {p<e^A}, Σ_{v∈S} = Σ_{all v}; hence I_S(F,F) = Σ_v ∫'(h_F) = P(F) − W(F)
      (Weil explicit formula ĥ(0)+ĥ(1)−Σ_ρ ĥ(ρ) = Σ_v ∫', Connes App.2 / (26)). So  −I_S(F,F) = W(F) − P(F); on E0: −I_S = W.
      [EXACT given L1-L3 + explicit formula.]
 (L5) Numerical, independent evaluation of the α-normalised principal value vs Fourier symbol (A=2, ||F||=1):
      non-E0 poly: τ=2.2556245 vs −(W−P)=2.2556273 (Δ 2.9e−6); non-E0 skew: 2.3368602 vs 2.3368629 (Δ 2.8e−6);
      E0 sin8 (P=0): τ=−0.0014306 vs −W=−0.0014006 (Δ 3e−5, quadrature of rough F). [NUMERICAL, uncertified]
 What (L1-L5) are: a TRACE IDENTITY + formal Hermitian form on a convolution algebra. NOT: cycles/divisor classes, Num, a Hodge
 structure, a positive sector, or an effective cone. Connes himself frames the h(1) term as "lack of transversality" (§VII).

## 3. Sign mechanism: the one that exists (char p) and the exact obstruction (char 0)
 Char p (Connes Thm 5 proof): E: L^2(X)_0 → L^2(C_k) isometry; B_{Λ,0} = span{f∈S(A)_0 : f, f̂ vanish for |x|>Λ}; E(B_{Λ,0}) ⊂ S_Λ
   (support in |g|∈[Λ^{-1},Λ]) ⇒ Q'_{Λ,0} ≤ S_Λ ⇒ Δ_Λ(f) = Tr((S_Λ − Q'_{Λ,0})V(f)) is of positive type for EVERY Λ.
   Here S_Λ supplies exactly the counterterm 2f(1)log'Λ and Q' the compressed "colored" trace: covariance1956's
   "white minus colored", now with an actual positive operator S_Λ − Q' ≥ 0. Sign comes from the INCLUSION Q' ≤ S_Λ.
 NEW LEMMA (char 0; elementary proof, believed folklore — CC replace B_Λ by prolate/Sonin constructions):
   For k = Q and any finite S ∋ ∞, any Λ: B_Λ^S = {f ∈ S(A_S): f(x)=0 and f̂(x)=0 whenever |x|>Λ} = {0}.
   Proof. Finite part locally constant, compact support: f = Σ_i a_i ⊗ 1_{B_i}, B_i disjoint balls, a_i ∈ S(R). Pick y ∈ B_i with all
   coordinates ≠ 0 (exists in every ball): f(x,y) = a_i(x) = 0 for |x|_∞ > Λ/|y| ⇒ a_i compactly supported. Likewise
   f̂ = Σ_j b_j ⊗ 1_{B'_j} with b_j compactly supported. Since the 1̂_{B_i} are linearly independent, choose points η_l with
   (1̂_{B_i}(η_l)) invertible: each â_i(ξ) is a finite combination of f̂(ξ,η_l) = Σ_j b_j(ξ)1_{B'_j}(η_l) ⇒ â_i compactly
   supported. a_i and â_i both compactly supported ⇒ a_i = 0 (Paley–Wiener). ∎
   Hence Q_Λ = Q_{Λ,0} = 0 and Δ_Λ(f) = 2f(1)log'Λ: the char-p positivity mechanism has NO nonzero char-0 instance.
   This is an uncertainty principle (simultaneous x/x̂ localisation at ∞), not a missing estimate.
 Connes uses R_Λ = P̂P in char 0: trace formula holds (L1) but positivity is lost (R_Λ not ≤ S_Λ, not positive).
 CC 2020 replace with Sonin space S (complement of P_1 ∨ P̂_1, nonzero): Tr(ϑ(f)S) = W_∞(f) + ∫f ε (Thm 3), W_∞(g*g*) ≥ Tr(ϑ S ϑ*)
   for supp g ⊂ [2^{-1/2},2^{1/2}], ĝ(i/2)=ĝ(0)=0 (Thm 1) — archimedean, window log 2 only (no prime lag inside).

## 4. First axiom not established
 (A1) [positive cutoff] There is a closed subspace B ⊂ L^2(C_Q) with B ⊂ range S_Λ (⇒ positivity automatic) whose trace satisfies
   Tr(Q_B V(g)V(g)^*) = 2 log'Λ ||g||^2 + I_S(g,g) + o(1)   for g ∈ E0 ∩ window.
 Positivity would then give W ≥ 0 on E0∩window. The canonical char-p choice B=E(B_{Λ,0}) is {0} in char 0 (Lemma). Any B ⊂ S_Λ
 trivially has Tr(Q_B VV*) ≤ 2log'Λ||g||^2; A1 asks the deficit to be exactly W(g) (+o(1)). Not circular as a test: B must be
 specified without W; its deficit is computable.
## 5. Next sharply testable requirement (not started)
 Semilocal S={∞,2}, window length ≤ log 3 (prime 2 lag inside, 3 outside). Candidate B: image under E_S of the Halmos "angle ≈ 0"
 part of (P_Λ, P̂_Λ) (prolate eigenvectors with λ_n ≈ 1), compressed into S_Λ. Compute deficit δ_Λ(g) = 2log'Λ||g||^2 −
 Tr(Q_B V V^*) − W_S(g) for explicit E0 windows; A1 passes only if δ_Λ → 0 (or ≤ 0 uniformly). R26/R27 (naive Π_S, λ_min −log2/√2)
 is the known failure of a different (Sonin lower-bound) variant; not this test.
## FF calibration audit (map1965): used n ≥ 0 graphs only (no transposes needed); γ_n^2 = q^{-n}Γ_n^2 = 2−2g correct;
 graph-span rank 4 equals Num(E×E) rank only because E/F_5 is ordinary (End rank 2); not universal.

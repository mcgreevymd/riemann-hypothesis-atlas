# Lemma 196: anatomy of the sign over F_q (genus 2). Which ingredient carries Weil positivity?

Scratch only, in lem196/. Authorized by J.W. at t2283 ("Yes run it here"), ledger direction G1 (STATE ~l.1767, score .80).
**RH is not proved. Nothing is claimed about ζ.** STATE.md, TARGET.md and the atlas were not touched, and nothing was pushed.
Tags: [T] theorem (proved here or elementary), [C] cited, [N] numerical (exact integer arithmetic unless noted), [R] restatement, [A] analogy/framing.

## Setting and conventions
C/F_q has genus 2, with q odd prime, and X = C×C. P(T) = 1 + a1T + a2T² + q a1T³ + q²T⁴ = ∏(1−α_jT), β_j = α_j/√q.
S_m = Σα_j^m, N_m = 1 + q^m − S_m, and N_0 := 2 − 2g = −2. The number of closed points of degree d is a_d = (1/d)Σ_{e|d}μ(d/e)N_e.
Classes: f1 = pt×C, f2 = C×pt, Δ, Γ_k = Γ_{F^k}. Then f_i² = 0, f1·f2 = 1, Γ_k·f1 = 1, Γ_k·f2 = q^k, Δ = Γ_0, Γ_k·Γ_l = q^{min(k,l)}N_{|k−l|} (Γ_k² = q^k(2−2g)).
The window on degrees 0..L uses Γ-coordinates x, or the normalized coordinates c_k = q^{k/2}x_k (these are congruent by Sylvester's law).
- Q := −Gram(Γ) is the analogue of CCM's Q. Its kernel is −q^{−|k−l|/2}N_{|k−l|}, and 2g−2 sits on the diagonal.
- C₊ = Σc_k q^{k/2} = (·f2), C₋ = Σc_k q^{−k/2} = (·f1), P = 2C₊C₋, W = Q + P.
- E₀ = ker C₊ ∩ ker C₋ is the primitive part. cosh^⊥ = ker(C₊+C₋) = (f1+f2)^⊥.

## Statements

**196.0 (dictionary is exact) [T].** In normalized coordinates, W(c) = Σ_{k,l}c_kc_l q^{−|k−l|/2}S_{|k−l|} = tr(Φ(c)Φ(c)^∨) (TARGET §2 Prop. 1). Also W = −(intersection form on the primitive projection), P = (intersection form on ⟨f1,f2⟩), and Q = −Gram(Γ). This makes L194(d) exact: ample f1+f2 ↔ cosh, E₀ ↔ primitive part.
Moreover, with ĉ(z) = Σc_kz^k, the FE (β ↦ 1/β) gives u_m = Σ_jβ_j^m for all m ∈ ℤ, hence
W(c) = Σ_j ĉ(β_j)ĉ(1/β_j) and P(c) = 2ĉ(√q)ĉ(1/√q).
So the pole plane H⁰⊕H² is exactly a real "off-circle FE pair" β = q^{±1/2} entering with multiplicity −1.
*Note on naming:* TARGET Prop. 1 calls this trace form "Q_ff". In L194 conventions it is W, and it equals Q only on E₀ (TARGET's "on primitive c").
*Test:* window.py builds Q, W and P from counts; rankcheck.py confirms n−(Q) = n−(W)+1 on 600/600 fakes.

**196.1 (box completeness) [T].** If N_n ≥ 0 for all n, then max|α_j| ≤ q, hence |a1| ≤ 4q and |a2| ≤ 6q².
*Proof.* Suppose r = max|α| > q. By Dirichlet simultaneous approximation, infinitely many n make every z_j^n = (α_j/r)^n with |α_j| = r close to 1. For those n, S_n ≥ ½r^n ≫ q^n, so N_n < 0. ∎
So the box enumerated below contains every candidate on rung (iii) and beyond. No candidate with r = q occurred (boundary count 0).

**196.2 (count rungs never kill the fakes) [N], certified for all n and all d.**
Every "∀n" and "∀d" check is done in exact integer arithmetic for d < D0, plus an explicit tail bound d·a_d ≥ q^d − 4r^d − Σ_{e≤d/2}(1+q^e+4r^e) > 0 for d ≥ D0 (ladder.py: tail_ok, certify_nonneg). Integrality of a_d is automatic from (ii) [T]: the S_d are traces of an integer matrix, so the necklace congruences hold.
The rungs:
- (iii) N_n ≥ 0 for all n.
- (iv) a_d ≥ 0 for all d, i.e. a genuine Euler product with nonnegative integer counts.
- (v) the hyperelliptic twist P(−T) also satisfies (iv). This is equivalent to N_n ≤ 2(q^n+1) together with the twist's Euler product: a geometric constraint (gonality 2) that does not use RH.
- (vi) Jacobian group orders J_n = ∏(1−α_j^n) > 0 and J_1 | J_n (n ≤ 12). Divisibility is automatic [T].

Census (each cell is total / off-circle):

| q | box | (iii) | (iv) | (v) twist | (vi) J_n | HI n≤1 | HI n≤2 | HI n≤3 | HI n≤4 | HI n≤6 | HI n≤8 | HI n≤12 | HI ∀n | real curves |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 2725 | 88/28 | 74/17 | 68/12 | 68/12 | 68/12 | 66/10 | 60/4 | 56/0 | 56/0 | 56/0 | 56/0 | 56/0 | 50 |
| 5 | 12341 | 364/237 | 326/199 | 297/172 | 297/172 | 297/172 | 237/112 | 145/20 | 133/8 | 125/0 | 125/0 | 125/0 | 125/0 | 115 |
| 7 | 33573 | 946/741 | 880/675 | 789/586 | 789/586 | 789/586 | 477/274 | 249/46 | 225/22 | 205/2 | 203/0 | 203/0 | 203/0 | 192 |
| 11 | 129317 | 3508/3107 | 3336/2935 | 2956/2555 | 2956/2555 | 2956/2555 | 1113/712 | 515/114 | 447/46 | 411/10 | 403/2 | 401/0 | 401/0 | 383 |
| 13 | 213045 | 5712/5199 | 5474/4961 | 4835/4322 | 4835/4322 | 4835/4322 | 1523/1010 | 673/160 | 577/64 | 525/12 | 517/4 | 513/0 | 513/0 | (not enumerated) |

Notes on the table:
- (iv) off-circle = 675/2935/4961 at q = 7/11/13, and (iv) on-circle = 205/401/513. Both reproduce L166 exactly, now certified for all d (L166 checked d ≤ 40).
- Every attained (a1,a2) passes every rung (`attained_not_in_vi = []`).
- Count-positive on-circle survivors that are not genus-2 Jacobians: 6/10/11/18 for q = 3/5/7/11. Honda–Tate/Rück abelian-surface membership was **not done**.
- Fake types at (vi): R (real Weil polynomial with real roots outside ±2√q) / C (complex): 8/4, 80/92, 269/317, 1143/1412, 1916/2406.

**196.3 (the first killing rung is Hodge index on C×C) [T]+[N].**
(a) [T] On the lattice ⟨f1,f2,Δ,Γ_n⟩, Hodge index (exactly one positive eigenvalue) ⇔ 16q^n − S_n² ≥ 0, the Weil bound at n. The primitive 2×2 Gram is [[−4, −S_n],[−S_n, −4q^n]].
[N] Checked by exact Descartes counting on real-rooted charpolys: 0 mismatches over 201,800 (curve, n ≤ 20) pairs, q = 3..13.
(b) [T] Hodge index for all n ⇔ every |β_j| = 1. Use the same Dirichlet argument as 196.1, with r > √q.
(c) [N] The minimal depth that kills every fake is N*(q) = 4, 5, 7, 9, 12 for q = 3, 5, 7, 11, 13, so it grows with q. The deepest fakes are the nearest to the circle, for example q = 13: (a1,a2) = (±1,−19), type R, δ = 0.0257. Min δ among fakes is 0.215, 0.101, 0.034, 0.026, 0.016.
So **no count-level rung kills the fakes. The first rung that does is the numerical Hodge index on C×C, which is count-determined but RH(C)-equivalent once taken for all n.** Its non-circular content is existence: the classes Γ_{F^n} are effective curves on a projective surface, so Riemann–Roch plus an ample class forces Hodge index (Grothendieck; Weil via Castelnuovo–Severi) [C]. That is T-D2: "F is a morphism defined over F_q" ⇒ Γ_F is effective ⇒ Hodge index/Rosati [R of TARGET §2].

**196.4 (window form: finite rank, signature, onset) [T]+[N].**
By 196.0, W is a Hermitian form of rank ≤ 2g = 4 on every window, and it has exactly rank 4 for L ≥ 3 when the roots are distinct.
- Each on-circle conjugate pair gives (2,0).
- Each real off-circle FE pair {β, 1/β} gives (1,1).
- Each complex quadruple gives (2,2).
Hence n−(W_L) is the number of |β_j| > 1 once L ≥ 3, n−(Q) = n−(W)+1 (the pole pair, κ = 1), and the onset satisfies L*_W ≤ 2g−1 = 3 and L*_{E₀} ≤ 2g+1 = 5, **independent of the deviation δ**.
[N] Data:
- rankcheck: 600/600 sampled fakes (q = 5, 7, 11, 13) have rank 4, n−(W) = number of |β| > 1 ∈ {1, 2}, and n−(Q) = n−(W)+1.
- Real curves: n−(Q) = 1, n−(Q|E₀) = n−(Q|cosh^⊥) = 0, W ≥ 0 with rank 4 (rank 2 for 4–9 per q with repeated roots); min eigenvalue ≥ −1e−59 at 60 digits, L = 16, 405 curves.
- Fakes, L*_W:
  - q = 3: 2:8, 3:9
  - q = 5: 2:113, 3:86
  - q = 7: 1:12, 2:471, 3:192
  - q = 11: 1:184, 2:2359, 3:392
- Fakes, L*_{E₀} ∈ {2..5}.
- corr(L*, 1/(δ log q)) = −0.03…0.30, so there is no onset law in δ.
Real curves have zero slack: W_L is singular in all but 2g directions for every L. Positivity is rigid, not robust.

**196.5 (no degree localization) [N].** At the E₀ onset, the negative eigenvector is decomposed as W(v) = 2‖v‖² − Σ_dA_d(v), with A_d = d·a_d·Σ_{j≥1}q^{−jd/2}R_{jd}(v) (300 fakes, q = 7 and 11).
- The degree-2 share is 0.46 / 0.44, against 0.23 / 0.25 for random E₀ vectors. That is ×2.04 at q = 7 and ×1.76 at q = 11, which sits at §351's 2× falsification threshold.
- The top degree is spread over d = 2–5.
- By 196.4 the failure is global: it is one root, not one place.
Verdict: no robust localization in the §351 sense.

**196.6 (one-place perturbation; FE is needed for positivity ⇔ RH) [T]+[N].** Take a real curve and change a_d by ±1. Then Z ↦ Z·(1−T^d)^{∓1}, which breaks the FE. Convention A is the consistent one, S'_0 = 4 ∓ d.
- **Adding a point** (+1) adds −Σ_{ζ^d=1}(ζ/√q)^{|m|}, the negative of a Poisson (positive-definite) Toeplitz matrix. W fails at L = 1–4 in every case: 120/120 per (d, q), d = 1..4, q = 5, 7, 11.
- **Removing a point** (−1) adds a positive-definite Toeplitz matrix, so W > 0 on every window [T]: 0 failures to L = 12.
- Under convention B (keeping Δ² = −2), both signs fail at L = 2–10.
- The 4×4 Hodge index (single n) almost never notices: ≤ 7/120 cases per (d, s).
So without the FE, window positivity does not imply purity: the one-point-removed object has roots of modulus 1 ≠ √q and still W > 0. The FE is what turns an inside root into an outside partner that the form can see.

**196.7 (slack of real curves) [N].**
- Min Hodge-index slack at n = 1, s₁ = 1 − |a1|/(4√q): 0.423 / 0.329 / 0.244 / 0.095 for q = 3/5/7/11.
- Median over curves of min_{n≤50} s_n: 0.009–0.018.
- 4/7/4/5 curves have exact zero slack at some n ≤ 50. For these, Γ_{F^n} is numerically in ⟨Δ, f1, f2⟩, i.e. F^n = ±q^{n/2} on H¹ (supersingular type) [T, from Hodge index with equality].

## Answers
- **(A)** No count rung kills all fakes, for any q. Rungs (iii)–(vi) leave 12/172/586/2555/4322 off-circle fakes at q = 3/5/7/11/13. The first rung that kills all is Hodge index on C×C, needed up to n = N*(q) = 4/5/7/9/12. For all n it is equivalent to RH(C).
- **(B)** [R] The sign is carried by T-D2: Frobenius is a morphism over F_q, so Γ_{F^n} is an effective class on a real surface with an ample class f1+f2, and Riemann–Roch gives Hodge index, i.e. Rosati. Counts, the Euler product, the FE, the twist and group orders never suffice. **Nothing new about the mechanism appears.** What is new is quantitative and exact:
  - the box-completeness theorem (196.1),
  - all-d certification of the L166 census,
  - N*(q) grows with q,
  - finite-rank rigidity, with onset ≤ 2g−1 independent of δ,
  - the FE is necessary for positivity ⇒ purity (196.6),
  - the pole plane is literally an off-circle FE pair with multiplicity −1 (196.0, matching the ledger's "pole pair = II₁,₁").
- **(C)** [A] On ζ/DH, onset is resolution-dependent (Conj 194c: the window must beat the on-line zero density). Over F_q, finite genus makes onset immediate (L* ≤ 2g−1) for every fake. A fake's failure is global (one root), with no robust degree localization (196.5).
  DH fails through its non-Euler support, while F_q fakes have genuine Euler products and the FE. So the ζ/DH separation by Euler × FE (§351 [H 3.30]) is **not** evidence that Euler × FE carries the sign: over F_q the same pair separates nothing.
- **(D)** [A, framing] The ℚ side must supply an object on which F ∗ F̃ is realized as an intersection of *effective* classes (images of morphisms) against an ample class, with Riemann–Roch forcing Hodge index. No condition on prime counts (Λ ≥ 0, Euler product, FE, positivity of a twist) can be enough, because over F_q every such condition is met by thousands of off-circle fakes.

## Tests (reproduce)
`python3 census_curves.py; python3 ladder.py 3 5 7 11 13; python3 summarize.py; python3 window.py; python3 window_run.py 3 5 7 11; python3 extras.py; python3 rankcheck.py`

The runs take about 10 minutes in total. Outputs are in out/: curves.json, ladder_raw.json, ladder_table.json, window.json, window_runs.json, extras.json, rankcheck.json, fallback_cache.json.
- census_curves.py cross-checks N3 by brute force over F_{q³} for 24 witnesses (q = 3, 5), with 0 mismatches. All 740 attained pairs have |β| = 1 to 3e−8 (the residual is double-root conditioning).

## Not done
- Honda–Tate/Rück classification of the non-Jacobian on-circle survivors.
- The q = 13 curve census.
- An exact-integer inertia path for rank-deficient windows (they fall back to mpmath at 60–80 digits).
- Genus ≥ 3.
- Rosati on End⁰(Jac) computed directly. The anatomy here is via NS(C×C), which is equivalent by TARGET §2 [C].

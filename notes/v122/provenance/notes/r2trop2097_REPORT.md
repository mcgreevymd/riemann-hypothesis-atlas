# REPORT t2097: is R2 a theorem or a definition? (scratch only, nothing pushed)

**Verdict.** (a) holds in the tropical model, but the model is the wrong one for R3.
- In the real-weight tropical Cartier model on R^2 / tropical P^1 x P^1 (log coordinates, psi_mu: X -> mu X), R2 is a theorem.
  Psi(mu) = div max(Y - mu X, 0), and G_mu^* Psi(mu) = div(mu max(Y-X,0)) = mu Delta. Given the projection formula, R2 <=> R1.
  R1, bidegree (1,mu), is forced by the normalization Psi(mu) = (id,psi_mu)_*[source].
- The model is genus 0: Psi(e^a).Delta = e^a + 1. It reproduces only P (kernel 2cosh(a/2)), with no log p atoms and no k_inf.
- On the periodic orbits C_p (Connes-Consani), the only degree-mu operator is the R_max-semilinear arithmetic Frobenius (CC Lemma 5.7).
  Its point map is a translation, so cycles on C_p x C_p cannot carry bidegree (1,mu). There R2 is vacuous or fails, and log p appears only as an excess length.
- R2 and R3 currently live in different models. Building one model containing both is the open problem.

**Numbers** (Cartier model; affine = R^2 part, total = P^1 x P^1)
| lam | mu | affine |lam-mu| | mu*(Psi(lam/mu).Delta)_aff | total lam+mu | min*(max/min+1) | density model 1/|lam-mu| |
|---|---|---|---|---|---|---|
| 3 | 2 | 1 | 1 | 5 | 5 | 1 |
| 4 | 2 | 2 | 2 | 6 | 6 | 0.5 |
| 2.5 | 0.7 | 1.8 | 1.8 | 3.2 | 3.2 | 0.5556 |
| e^1.3 | e^0.4 | 2.17747 | 2.17747 | 5.16112 | 5.16112 | 0.45925 |
| pi | sqrt2 | 1.72738 | 1.72738 | 4.55581 | 4.55581 | - |
| 0.3 | 0.9 | 0.6 | 0.6 | 1.2 | 1.2 | - |
The smoothed mixed Monge-Ampere integrals reproduce the affine column to about 1e-9. They also give G_2^*Psi(2).F1 = 2 and Psi(pi).F2 = pi.
The corners carry min(lam,mu) each, matching the function-field picture for P^1/F_q (checked with sympy).

**Pullback under the three conventions:** density gives mu^{-1} Delta, integration current gives 1*Delta, Cartier/Lagerberg (1,1) gives mu*Delta.
Only the last satisfies R1.

**Half-density:** min(lam,mu) forces the weight e^{-u/2} via Toeplitz invariance. The weighted kernel is 2cosh(a/2) = P, and w = 1 fails.
The required prime atom in Psi(e^a).Delta is Lambda(n) delta(a - log n) with no p^{-k/2}, consistent with Formulation B.

**Cooked / chosen:**
1. The choice of (1,1)-Cartier calculus over currents. This is the content behind "deg psi_mu = mu"; it is legitimate, but it is a model choice.
2. Extension to real weights, i.e. irrational slopes. There is no lattice, so the weights are fixed by graph normalization.
3. Any claim that this model sees primes or k_inf: it does not.
4. The side observation that the trace-type density kernel 1/(2sinh(a/2)) is "close to" k_inf. The q -> q^2 gap is still hand-inserted.

Files: notes2097.md, r2trop2097.py, r2trop2097.json.

**Question for the dreamer (paste-ready):**
Setup. Use log/tropical coordinates. psi_mu is X -> mu X. A real-weight tropical Cartier divisor is the corner locus of a PL function with real slopes, with weight given by the gradient-jump covector n. Intersections are |det(n1,n2)| (mixed real Monge-Ampere). Psi(mu) := div max(Y - mu X, 0), which has bidegree (1,mu) against the fibres. Delta = Psi(1).
In R^2 / tropical P^1 x P^1 this gives G_mu^* Psi(mu) = mu Delta and Psi(lam).Psi(mu) = lam + mu, with Psi(e^a).Delta = e^a + 1 and no atoms.
On Connes-Consani's periodic orbit C_p = R*_+/p^Z, the degree-mu operator is the arithmetic Frobenius Fr^a_mu f(l) = mu f(l/mu) (CC Lemma 5.7). Its point map is a translation, so cycles supported on its graph in C_p x C_p have fibre-bidegree (c,c), not (1,mu).
Question. Construct one 2-dimensional tropical space T (with a structure sheaf of PL functions) such that:
(i) T contains the slope-scaling square above, so that Psi(mu) = div(F_mu) for an explicit PL function F_mu on T. G_mu^* F_mu = mu*(defining function of Delta) must hold up to a function with no corners.
(ii) Near C_p x C_p, the same F_{p^k} restricts so that Psi(p^k).Delta acquires a component supported over C_p of size exactly log p. This must be computed as a |det|-type stable intersection number, not as an integral of dt or a pushforward over a parameter.
What counts as an answer: explicit coordinates on T near C_p x C_p, explicit F_mu, and the computation in (ii). Also say whether the mu in (i) comes from slope scaling (linear) or from the value-direction twist (CC's semilinear Fr^a). Mark the least certain step.
A failure mode to address: log p arising as a length is a trace or measure, not a |det|.

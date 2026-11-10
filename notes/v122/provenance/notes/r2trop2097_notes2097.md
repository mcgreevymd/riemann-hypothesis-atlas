# t2097: R2 tropical test. Scratch notes (local only, not pushed)

## Conventions
- Log/tropical coordinates (X,Y) on the square. psi_mu: X -> mu X (char-1 Frobenius x -> x^mu on R_max).
- Psi(mu) := (id, psi_mu)_*[R_X] (graph = pushforward of the source fundamental class, tangent weight (1,mu)).
- A real-weight 1-cycle in R^2 is recorded by its gradient-jump covector n (Cartier datum).
  Psi(mu) = div f_mu, f_mu(X,Y) = max(Y - mu X, 0), so n_mu = (-mu, 1) = J(1,mu).
- Stable intersection: D1.D2 = |det(n1,n2)| = total mixed real Monge-Ampere of the PL potentials
  (Bernstein normalization: integral of det(H1+H2) - det H1 - det H2). Equivalently, Lagerberg (1,1) supercurrents
  dd^# f, which are homogeneous of degree 1 in f.
- Pullback: n -> G^T n (div(f o G) = G^* div f). Pushforward for invertible G: n -> |det G| G^{-T} n (= cofactor on tangents).
  The projection formula |det(G_* n1, n2)| = |det(n1, G^T n2)| holds identically.
- Fibers: F1 = {X=c} = pt x S (n=(1,0)), F2 = {Y=c} = S x pt (n=(0,1)).

## Model (a): R^2 and tropical P^1 x P^1
- R1: Psi(mu).F1 = 1, Psi(mu).F2 = mu, so the bidegree is (1,mu). The normalization is pinned by "graph has degree 1 over the source"; it was not chosen.
  (A different potential, e.g. max(Y/mu, X), rescales n and gives (1/mu, 1). The real-weight theory has no primitive vectors, so the weight is fixed by the graph-pushforward normalization.)
- G_mu = id x psi_mu = diag(1,mu). G_mu^* f_mu = max(mu Y - mu X, 0) = mu max(Y - X, 0), so **G_mu^* Psi(mu) = mu Delta**.
  This is literally div(c f) = c div(f), the counterpart of (y-x)^{q^l}. For integer mu it is the lattice (Allermann-Rau) statement.
- (G_mu)_* Psi(lam/mu) = Psi(lam), checked via the covector rule and via the projection formula against F1 and F2.
- Affine (R^2) part: Psi(lam).Psi(mu) = |lam - mu| = mu (Psi(lam/mu).Delta)_aff = min(lam,mu)|max/min - 1|.
- Compact tropical P^1 x P^1: total = bidegree pairing (1,lam).(1,mu) = lam + mu = min(lam,mu)(max/min + 1).
  The difference 2 min(lam,mu) sits at the two corners (0,0)/(inf,inf). The local order of x^lam - x^mu is min(lam,mu) at each corner.
- Function-field match (P^1/F_q, lam=q^k, mu=q^l): fixed points of Frob^{k-l} are 0, inf, and F*_{q^{k-l}}, each with multiplicity q^l.
  So the corners carry q^l each and the q^{k-l}-1 torus points total q^k - q^l = |lam-mu|; the latter tropicalize to the origin.
  The Frobenius binomial identity was verified with sympy for (q,k,l) = (2,3,1), (3,2,1), (5,2,1).
- **Model (a) is exactly genus 0: Psi(e^a).Delta = e^a + 1, a continuous function of a with no atoms.**

## Contrast: current models (task 3)
| model | Psi(mu) as | G^*Psi(mu) | bidegree | Psi(lam).Psi(mu) |
|---|---|---|---|---|
| density | delta(Y-mu X) | mu^{-1} Delta | (1, 1/mu) | 1/|lam-mu| |
| integration current | delta(g)dg | 1 * Delta | (1,1) | +-1 |
| tropical Cartier / Lagerberg | delta(g) dg ^ d''g | mu Delta | (1, mu) | |lam-mu| |
Each model satisfies the projection formula internally. Only the Cartier model satisfies R1. So, given the projection formula, **R2 <=> R1**.
The numbers were verified numerically with Gaussian/softplus smoothing on a grid (agreement to ~1e-9).

## Half-density (task 4)
- With the Cartier numbers, e^{-(u+v)/2} Psi(e^u).Psi(e^v) = 2cosh(a/2), a = |u-v|, which is exactly the TAA P kernel (C+ conj C- + C- conj C+).
  The affine part alone gives 2 sinh(a/2). Weight w = 1 is not Toeplitz (3.718 vs 10.107 at a=1).
  So R2's min(lam,mu) forces e^{-u/2}, and it does not give min/something or lam*mu.
- Under this normalization, the TAA requirement (I = P - W, primes +) reads, for a>0:
  Psi(e^a).Delta = e^a + 1 + sum_n Lambda(n) delta(a - log n) + e^{a/2}*(archimedean term).
  The required prime atom is log p with no p^{-k/2}. That is exactly Formulation B's count, so the R2 normalization and B are mutually compatible.
- Model (a) supplies only e^a + 1: no atoms and no k_inf.
- Side observation (not a result): the density model with weight e^{+u/2} gives 1/(2 sinh(a/2)) = e^{-a/2}/(1-e^{-a}),
  an inverse-determinant (trace-type) kernel. The given k_inf(a) = e^{-a/2}/(1-e^{-2a}) differs from it by q -> q^2, the same hand-inserted +-1 average flagged in t2083.
  Intersection (Cartier) gives |det(1-dpsi)|; trace gives |det(1-dpsi)|^{-1}.

## Model (b): periodic orbit C_p = R*_+/p^Z (task 2). Read from the CC paper, Sec 5.2
- CC degree: deg D = sum h_j (orders = derivative jumps scaled by lambda, i.e. log-coordinate slope jumps).
- Relative Frobenius Fr^r_h f(l) = f(hl) (R_max-linear, h in H_p^+): translates points, **preserves deg** (Lemma 5.8).
- Arithmetic Frobenius Fr^a_mu f(l) = mu f(l/mu), **all mu in R*_+**: translates points, **multiplies deg by mu** (Lemma 5.7). It is R_max-semilinear.
- Absolute Fr_h f = h f: fixes points, deg x h; Fr_h = Fr^a_h o Fr^r_h. For mu = p^k, Fr^a_{p^k} = Fr_{p^k} fixes every point of C_p.
- So a mu-multiplicity does exist on C_p (correcting my prior expectation), but only through the semilinear (value-direction) Frobenius.
  The point map is always a translation of the circle.
- Obstruction: a real-weight cycle supported on a translation graph in C_p x C_p has tangent direction (1,1), so its fibre-bidegree is (c,c), never (1,mu).
  Translation graphs are disjoint from Delta unless mu in p^Z, and coincide with it (excess along C_p) when mu = p^k. Topologically Psi.Delta = 0 on the torus.
  Integer coverings t -> nt (which descend only for n in Z) give |n-1| fixed points, independent of L = log p. There is no log p in either case.
- Hence on C_p x C_p the factor mu lives in the value (R_max-coefficient) direction, which is not a direction of the square.
  R1/R2 as fibre-intersection statements fail there, or are vacuous (0 = mu*0).

## Verdict
(a) R2 is a theorem in the real-weight tropical Cartier model on R^2 / tropical P^1 x P^1 (model (a), CC's [0,inf) with lambda -> mu lambda).
    Given the projection formula, it is equivalent to R1, and R1 is forced by Psi(mu) = (id,psi_mu)_*[source].
    Not cooked inside the model. The one standing choice is the model itself: (1,1)-Cartier/Lagerberg currents rather than integration or density currents.
    That choice is what makes deg psi_mu = mu (slope scaling) rather than 1 (topological degree of a homeomorphism).
But that model is genus 0 (Psi(e^a).Delta = e^a+1, producing only P), with no log p and no k_inf. Condition 3 (same model gives R3) FAILS.
On C_p x C_p, R3's log p lives at the excess locus where Fr^a_{p^k} = absolute Frobenius, and there R1/R2 cannot hold as fibre-bidegree statements.
Net: R2 = theorem in a model where R3 is absent; R3 lives where R2 is vacuous. The joint model is the roadblock.

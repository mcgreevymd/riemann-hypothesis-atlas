# t1928 — "rest frame" / ample class as frame picker (Nov 7 2026 CST). Scratch only. RH NOT proved. Files: observer1928.py/json.
Source opened: https://en.wikipedia.org/wiki/Hodge_index_theorem (signature (1,ρ−1); H-perp negative definite; Hartshorne V.1).
GR/QFT statements below are standard textbook facts stated from knowledge (not re-sourced this turn).

## Physics, precise
- Observer at a point = unit future timelike u (g(u,u)=−1, signature −+++); rest space u⊥ with positive metric h = g + u♭⊗u♭.
  Riemann normal coordinates at P give g=η, ∂g=0 at P for ANY chosen orthonormal tetrad; second derivatives (Riemann, tides)
  cannot be removed. The equivalence principle supplies a family of local inertial frames, not a preferred u.
- What selects u: (i) a state/matter: total 4-momentum P timelike ⇒ u = P/√(−P·P) (centre-of-momentum frame); null P has no rest
  frame; (ii) a symmetry: a timelike Killing field (static observers in a stationary spacetime) — global frame field, not a global
  Minkowski chart; (iii) cosmology: comoving/CMB frame = (i) for the matter content. The Poincaré vacuum selects nothing;
  accelerated observers see it differently (Unruh), so "vacuum rest frame" is not defined.
- Quantum: ⟨P⟩=0 defines a rest frame of a state; a sharp momentum eigenstate is non-normalizable; localization vs momentum spread
  (uncertainty) — "rest" is a property of the expectation, not of a sharp state.

## Exact analogy (computed): ample class = observer, Cartan involution = rest-space metric
 I on NS_R of a projective surface: signature (1,ρ−1) (Hodge index). For A with I(A,A)>0:
  θ_A(y) = 2 I(y,A)A/I(A,A) − y (reflection: +1 on A, −1 on A⊥), θ_A² = 1, θ_A ∈ O(I);
  g_A(x,y) = I(x,θ_A y) = 2 I(x,A)I(y,A)/I(A,A) − I(x,y) is positive definite (x=αA+w ⇒ g_A = α²I(A,A) − I(w,w)).
 Same algebra as h_E = g + 2u♭⊗u♭ (Euclideanized metric of an observer, sign conventions aside).
 Checks (I = U ⊕ −I₃): g_A eigenvalues all 1 at A=f1+f2; boosted A=(e^t,e^{−t}) at t=0.7 gives 0.2466, 1,1,1, 4.0552 (=e^{∓1.4}):
 different ample classes = different observers related by boosts; signature (Sylvester) is invariant, the positive metric is not.
 Product of curves: U=span(f1,f2), A=f1+f2 ample, the factor swap fixes A and is the Cartan involution of U; Weil-type
 conditions ↔ orthogonality to f1,f2 (prior L114/L134 note, Bombieri Clay §V [C+A]).
 Boundary of our window space: pole form P(a,b) = 2Re(a b̄) on (ev0,ev1) is exactly U (signature (1,1)); the functional-equation
 swap σ fixes the timelike line a=b and P(x,σx) = |a|²+|b|² (checked). So FE + pole form already fix the boundary "rest frame".
 Hodge–Riemann generalization (with qualifiers): for a Kähler class ω, primitive (p,q)-forms get a definite sign — again a CHOSEN ω.

## What E0 still lacks (the real gap)
 E0 = boundary-orthogonal ("primitive") part. G0 > 0 there is an observer-type positive metric, but it is a choice, not an
 intersection form; it says nothing about the sign of W (Sylvester: no coordinate change alters inertia).
 An arithmetic analogue of the ample class must supply, independently of W: (1) a space V with a form I of PROVEN signature
 (1,n) or (2,n) (a Hodge-index theorem), (2) a timelike/boundary plane identified with (ev0,ev1, P, σ), and (3) a map Φ from E0
 into the orthogonal complement with −I(Φf,Φf) = W(f) (or ≤ W) given by an intersection theorem, not by defining I from W.
 Existing structure (pole form, FE swap, Tate boundary laws) fixes only (2).

## Refined research question
 Sign bookkeeping: in the surface case I is negative definite on A⊥; the analogue of "W ≥ 0 on E0" is "I < 0 on the
 primitive part", i.e. the target form must restrict to P on the boundary plane and to −W on E0. That form must come from an
 independent intersection theory (not be defined as P ⊕ −W, which would be circular).
 Question: is there a first-principles selection rule — state-type (u = P/|P|), symmetry-type (an involution commuting with
 scaling and the FE swap σ), or cone-type (ample/Kähler) — yielding an independently defined form I of proven signature (1,·) or
 (2,·) on a space containing the window functions, whose timelike data restrict to the pole form and σ, and whose restriction to
 E0 is −W? Then g_I = I(·,θ·) > 0 would make W ≥ 0 on E0 a Hodge-index theorem. Unanswered; no candidate constructed here.

# parabolic1998 — the user's parabolic tangent structure, the three discriminants, and the one that controls the sign
Nov 8 2026 ~10:15–10:50 AM CST. Scratch only; no repo/manuscript edits. RH NOT proved. Labels [EXACT] sympy/proof here, [THM] cited,
[NUM] Galerkin double precision (uncertified), [ANALOGY], [OPEN]. counterterm1995 scheme claims NOT used.
Scripts: conic1998.py/.json (sympy), pencilW1998.py/.json (actual window W via matching1989/mom1975.py, unchanged), anchor1998.py/.json, hess1998.py/.json (Hessian formula err ≤7e−6 finite-diff; det identity exact to 1e−12; (1,3): det>0 yet Hessian (2,2)).

## 1. The user's geometry, exactly [EXACT]
y=x² ⇔ Q=X²−YZ. Tangent at t = polar of (t,t²,1): tX − Y/2 − t²Z/2, affine y = 2tx − t², intercept −t² → −∞;
projectively (÷t²) → (0,0,−1/2): the LINE AT INFINITY Z=0 = tangent at x∞=(0,1,0) (the parabola's only point at infinity).
Unified pencil (one smooth conic, moving chart): x² − y + k y² = 0, M_k=[[1,0,0],[0,k,−½],[0,−½,0]].
 det M_k = −1/4 for ALL k, inertia (2,1) for all k: the ternary conic never degenerates; ellipse/parabola/hyperbola is NOT a rank change.
 Q|ℓ∞ = X² + kY², binary disc = −4k; dual form Q*(ℓ∞) = k; pole of ℓ∞ = center (0,1/(2k)), Q(center) = −4k.
 k>0 ellipse: no real points at ∞; far-vertex tangent y=1/k and vertical tangents x=±1/(2√k) (at y=1/(2k)) all run off to ∞; far tangent → ℓ∞ as k→0+.
 k=0 parabola: tangents along the branch → ℓ∞ itself (the user's intercept → −∞).
 k=−m² hyperbola: tangents along a branch → asymptotes (m,−m²,−½), i.e. y=(±mx−½)/m² — FINITE lines; both → ℓ∞ as m→0.
 So "tangent line at infinity" is the k→0 merger of the two asymptotes (hyperbola) = escape of the far vertex (ellipse).
h_s gauge (1980, here in the user's coordinates): h_s=(0,1,s), Q(h_s)=−s (homogeneous gauge; affine rep (0,1/s,1) has −1/s, same sign).
 polar of h_s = horizontal line y = −1/s (pole–polar reflection through the vertex): as s→0+, h_s climbs the axis to x∞ and its polar descends to
 intercept −∞ → ℓ∞. Gram of Q on h_s^⊥ = diag(1, s): s>0 definite (ellipse-type), s=0 null (parabola: tangent line, h ∈ h^⊥), s<0 (1,1) (hyperbola-type).
 Same limit two ways: boundary path (t,t²)→x∞ with tangents → ℓ∞; interior path h_s→x∞ with definite complements → degenerate.

## 2. Three discriminants — which can control the sign [EXACT]
 D1 ternary det M (pairing degeneracy / singular conic): controls RANK only; constant along the whole family. Cannot give sign.
 D3 binary restriction to a line ℓ (0/1/2 real points: ellipse/parabola/hyperbola type): identity (verified symbolically)
     det(PᵀMP) = (p1×p2)ᵀ adj(M)(p1×p2)  ⇒  disc(Q|ℓ) = −4 ℓᵀadj(M)ℓ = −4 det(M)·Q(pole ℓ).
     With inertia additivity In(M) = In(Q|c^⊥) + In(Q(c)) (c = pole): Q(c)<0 ⇔ Q|ℓ definite; this IS the sign-controlled complement.
 D2 envelope/caustic of the tangent family y−2tx+t²: disc_t = 4(x²−y) = the conic itself; sign at a point = number of real tangents
     (0 inside, 2 outside). D2 at h ≡ D3 at its polar (pole–polar duality). Projection Jacobian ∂y/∂t = 2(x−t) only labels the two sheets
     (fold orientation), not the complement sign (incidence1964/duality1967 distinction kept).
 So: the sign of the complement is controlled by D2/D3 (pole–polar), CONDITIONAL on the inertia anchor In(M)=(2,1) (D1≠0 + connected family + one point).
 Hasse wall |t|=2√q (duality1967) = D2 evaluated at the Frobenius point (t,q) — a consequence/location, not the sign source.
 Optical caustic/no-conjugate-points (Morse index of a generating family) is a different mechanism (index of a family Hessian), not D2/D3; not merged.

## 3. Transfer to the actual pairing: the pencil discriminant through e = h+v [EXACT + NUM]
Extended form J on V = D(I)⊕U (matching1989 §3): J(h,h)=J(v,v)=0, J(h,v)=1, J(h,F)=C+(F), J(v,F)=C−(F), J(F,F)=−B(F); e=h+v, J(e,e)=2.
 For x ∈ V, the line x+τe meets the quadric {J=0} in τ± with ¼disc_τ = Δ_e(x) = J(e,x)² − J(e,e)J(x,x).
 Identity (sympy): for x = F+αh+βv, Δ_e is flat in α+β and  min_{α,β} Δ_e(F+αh+βv) = 2(B(F) + 2C+(F)C−(F)) = 2W(F).
 ⇒ W(F) = ½ min (pencil discriminant)  and  W ≥ 0 on D(I) ⇔ every line through e is hyperbola-type ⇔ the apparent contour of {J=0}
   seen from e (branch locus of projection from e) is empty ⇔ n+(J)=1 (= matching1989 (a), now as the user's discriminant geometry).
 Zero locus W(F)=0 = lines through e TANGENT to the null quadric = parabolic degeneration (two null points merging, like asymptotes → ℓ∞).
 NUM on the actual window (sine basis J=40): ¼disc = 2W to 1e−15 (A=0.6,1.0); separation of the two null points τ+−τ− on the optimal line:
   A=0.6: 0.128; A=1.0: 1.46e−3; A=1.5: 1.6e−7 (W=1.3e−14, machine floor). The window lines through e become near-parabolic
   super-exponentially (the prolate ladder of matching1989 §4, seen as asymptotes merging). An RH-window failure = an ellipse-type line through e.
 Both moments: U=span(h,v) is hyperbola-type (two null points h,v = "two points at infinity"); one moment (single cusp, boundary1994: one
   independent boundary moment, P = −2|p10|² rank 1) is a degenerate/parabola-type border and cannot anchor; Γ0(N)/Fricke would give two [ANALOGY].
 Dimension caveat (anchor1998): in R⁴ with the same null pair, same det (−1), same J(e,e)=2, one has n+=1 (contour empty) or n+=3
   (ellipse-type lines through e exist). In dim 3 (a conic) nondegeneracy + a real point fixes the inertia up to global sign; for dim ≥ 4 the
   parabolic data never fix it. Full W: infinite rank even on one window, so no dimension-3 shortcut.

## 4. What WOULD supply the sign: the classical mechanism behind "no ellipse-type line through an ample point" [THM + EXACT]
Hodge index on a surface (Hartshorne V.1.9) is exactly: no ellipse-type plane span(H,D). Proof uses two inputs:
 (A) ampleness: H·Y > 0 for every nonzero effective Y;  (E) Riemann–Roch growth: D² > 0 ⇒ nD or −nD effective for n≫0.
 If span(e,x) were ellipse-type it contains D ⊥ e with D²>0 ⇒ ±D effective (E) ⇒ e·D ≠ 0 (A): contradiction.
Transfer test for J with the natural "effective" cone 𝒦₊ = {F ≥ 0 pointwise} ⊕ {α,β ≥ 0}:
 (A) holds EXACTLY: J(e, F+αh+βv) = ∫F(u)(e^{u/2}+e^{−u/2})du + α + β > 0 (C± are the Laplace moments at ±½). So e is "ample" for 𝒦₊.
 (E) FAILS for 𝒦₊ even if RH holds: x = e + εF with F sign-changing has J(x,x) ≈ 2 > 0 but x ∉ ±𝒦₊. Pointwise positivity is too small a cone;
   (E) needs an effectivity defined by SECTION COUNTS (h⁰>0 with RR growth), not by pointwise sign.
Conditional theorem (exact logic): if a cone 𝒦 ⊂ V, defined independently of J's sign, satisfies (A) J(e,·)>0 on 𝒦∖0 and
 (E) {x: J(x,x)>0} ⊂ 𝒦 ∪ −𝒦, then every line through e is hyperbola-type, hence W ≥ 0 on the window. Converse with 𝒦 = closed positive
 cone is tautological, so the content is entirely in an independent (E).
Missing ingredient (precise): a quadratic Riemann–Roch on the square: h⁰ for classes x ∈ V with h⁰(nx)+h⁰(K−nx) ≥ ½n²J(x,x) + O(n),
 whose effective classes include the positive functions (so (A) is inherited). Connes–Consani's RR for Spec Z̄ (arXiv:2205.01391, Bull. Sci. Math.
 187 (2023)) is the one-dimensional case (curve, not square); no square version exists [OPEN]. This is the existing W7 gap (STATE), now
 isolated as exactly the (E) half; the (A) half is proved here for the moment pair.

## 5. Gradient/Jacobian, placed precisely (brief, as the steering asks)
 dQ_x = 2B(x,·) is the polar map; the steepest-ascent vector needs a metric (polarity1980) — the metric-free object is the polar/pole.
 Hess(−log(−Q)) = (2/|Q|)[λ²|Q| + B(v⊥,v⊥)] (v = λx + v⊥): positive iff Q(x)<0 and Q|x^⊥>0 — i.e. it is D3 again (sign of the polar complement);
 det Hess = −(2/|Q|)^N det M (Monge–Ampère), whose sign cannot distinguish (3,1) from (1,3): full rank + det sign insufficient [EXACT].
 Curvature/period-map positivity (Griffiths) presupposes Hodge–Riemann on the target; for J it would be circular.

## 6. Added beyond polarity1980/hodge1981/incidence1964/duality1967
 (i) one smooth conic, MOVING chart: ellipse/parabola/hyperbola = sign of Q*(ℓ∞) = −4k with det fixed — the user's tangent-at-infinity is the
     wall between, with the explicit limits (far vertex, vertical tangents, asymptotes); (ii) disc(Q|ℓ) = −4det(M)Q(pole) identity (verified) tying
     D2 and D3 and separating D1; (iii) W(F) = ½ min pencil-discriminant through e (new identity, verified symbolically and on the actual window);
     (iv) near-parabolic collapse of the window pencils (numbers above); (v) dim-4 counterexample showing parabolic data never anchor inertia;
     (vi) ampleness half (A) proved for the moment pair on positive functions; failure of (E) for that cone, isolating quadratic RR.
Sources: Hartshorne, Algebraic Geometry, V Thm 1.9 & Ex 1.9–1.10; Connes–Consani https://arxiv.org/abs/2205.01391; Connes 1999 https://arxiv.org/abs/math/9811068;
 matching1989/notes1989.md §3–4; boundary1994/notes1994.md; polarity1980, hodge1981, incidence1964, duality1967 notes.

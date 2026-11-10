# t2083 — first-variation (dipole) probe on X = P¹(C)×P¹(C), product FS baseline (scratch; nothing pushed)

Scope: archimedean only. Does NOT construct Φ, gives NO Hodge-type sign for W, says nothing about RH.
Script: `vary2083.py` → `vary2083.json` (exact sympy residuals, asymptotics, numerical checks).
Conventions exactly as t2078: dd^c=(i/2π)∂∂̄, ω=pr₁*ω_FS+pr₂*ω_FS, g_u=−log|w−e^u z|²+log(1+|z|²)+log(1+|w|²),
dd^c g_u+δ_{Γ_u}=ω, T(u,v)=∫(g_u*g_v)∧ω=∫_{Γ_v}g_uω+∫g_vω². q:=e^{−a}, a=|u−v|. Below "u>v" unless noted.

## 1. The currents (definitions)
**V_u := ∂_u[Γ_u]** = lim_{ε→0}([Γ_{u+ε}]−[Γ_u])/ε. Let ξ = 2Re(w∂_w) (real part of the holomorphic field w∂_w; its flow
σ_t(z,w)=(z,e^t w) maps Γ_u→Γ_{u+t}). For a smooth 2-form φ on X: V_u(φ)=∫_{Γ_u}L_ξφ=∫_{Γ_u}ι_ξdφ, i.e. V_u=±d(ξ∧[Γ_u]).
 - V_u is a real 2-current of bidegree (1,1) (σ_t holomorphic), ORDER 1 (dipole: sees one normal derivative of the test
   form), supported on Γ_u, d-closed and d-exact, so [V_u]=0 in H^{1,1}. It pairs with smooth 2-forms (of type (1,1)).
 - ξ vanishes on {w=0}∪{w=∞}, so the dipole strength vanishes exactly at the collision points (0,0),(∞,∞).
 - Green function: h_u := ∂_u g_u = 2Re(e^u z/(w−e^u z)) (raw sections). dd^c h_u + V_u = ∂_uω = 0. h_u is a (0,0)-current
   with Cauchy-type 1/dist singularity along Γ_u (L¹_loc in real codim 2). It is unique up to an additive constant
   (compact X); raw vs balanced sections shift it by exactly 1 (h'_u=h_u+1).
 - Pairings on a surface still need a third class: star product h_u*g_v = h_u δ_{Γ_v} + (class of V_u=0)·g_v, so
   ⟨V_u,Γ_v,ω⟩ := ∫_{Γ_v}h_u ω = ∂_u T(u,v)      (the ω² term drops because [V_u]=0)
   ⟨V_u,V_v,ω⟩ := V_v(h_u ω) = ∂_v∂_u T(u,v)      (additive constant in h_u drops: V_v(cω)=c ∂_v∫_{Γ_v}ω=0).
   These ARE differentiated triple pairings; labelled as such. The second is checked independently via the Cartan form
   ∫_{Γ_v} ξ(h_u) ω by 2D quadrature (matches to 1e-8 at 4 points); first variation checked by finite differences of a
   direct quadrature of ∫_{Γ_v}g_uω (1e-6).
**Ĝ_u := e^{−u/2}[Γ_u]** (t2068 half-density). Green current e^{−u/2}g_u, class e^{−u/2}ω (moves with u!).
 ∂_uĜ_u = e^{−u/2}(V_u − ½[Γ_u]) — NOT null-homologous: class −½e^{−u/2}ω. Triple pairing is bilinear, so
 ⟨Ĝ_u,Ĝ_v,ω⟩ = e^{−(u+v)/2}T (not translation-invariant). A translation-invariant weight needs the contragredient on the
 second slot, Ĝ_v^∨ := e^{+v/2}[Γ_v] (unitary-adjoint convention U_u U_v^*=U_{u−v}): ⟨Ĝ_u,Ĝ_v^∨,ω⟩=e^{−(u−v)/2}T. That
 dual choice is itself a convention.
**Twisted family** Γ_u^ε={w=εe^u z}, ε=±1. Jensen-type fact: avg_ε(−4log|e^u−εe^v|) = −2log|e^{2u}−e^{2v}|, i.e. the
 sign average IS the pairing of the doubled family Γ_{2u} (quotient by z↦−z, w↦−w; coordinate z²). Hence q→q².

## 2. Closed forms (exact; sympy residual 0)
Graph pairings (t2078, re-confirmed): T_raw^± = 6−4log|e^u ∓ e^v|; T_bal^+ = 6−4log(2sinh(a/2)); T_bal^− = 6−4log(2cosh(a/2)).
A. first variation ⟨V_u,Γ_v^ε,ω⟩:
   A⁺_raw = −4e^u/(e^u−e^v) = −4/(1−q)            (u>v);   = +4q/(1−q) for u<v
   A⁻_raw = −4/(1+q)  (u>v);   = −4q/(1+q) (u<v)
   A⁺_bal = −2 coth(a/2)·sgn(u−v)   (odd, PV);   A⁻_bal = −2 tanh(a/2)·sgn(u−v)
   −¼A⁺_raw = 1/(1−q) = Σ_{n≥0}qⁿ  = holomorphic Atiyah–Bott index of z↦qz on O (K⁰) at the attracting point (0,0).
   For u<v the raw value is −4·AB_∞, AB_∞ = −q/(1−q). Balanced: −¼A⁺_bal = ½coth(a/2) = ½(AB_0 − AB_∞);
   raw − balanced = ½(AB_0+AB_∞) = ½χ(O) = ½. So the section normalization (the free constant in h_u) is exactly the
   split of χ(O)=1 between the two fixed points. (This is NOT the explicit-formula pole P; P is not addressed here.)
B. second variation ⟨V_u,V_v^ε,ω⟩ (canonical: independent of section normalization, of the constant in h_u, and — by
   t2078 rigidity T_h = −4log|e^u−e^v|+C_h+α(u)+α(v) — of ANY fixed metric):
   B⁺ = −1/sinh²(a/2) = −4q/(1−q)² = −4Σ_{n≥1} n qⁿ    (even, translation-invariant; Hadamard FP at a=0)
   B⁻ = +1/cosh²(a/2) = 4q/(1+q)²
   −¼B⁺ = q/(1−q)² = 1/|det(1−diag(e^a,e^{−a}))|  (full-density real Lefschetz/Guillemin denominator).
   Fourier symbol (t≠0): FT[B⁺](t) = 4π t coth(πt) > 0; checked on a Gaussian (13.825 direct vs 13.832 spectral).
   This positivity is just conditional positive-definiteness of −log (log-energy of a degree-0 smeared cycle
   ∫φV_u = −∫φ'Γ_u); it is not a sign theorem for W and is the wrong kernel.
C. half-densitized (balanced sections; x=u−v):
   ⟨∂_uĜ_u,Ĝ_v,ω⟩ = e^{−(u+v)/2}(∂_uT' − ½T')  — depends on u+v (not invariant).
   dual-weighted:  C_A := ∂_u[e^{−x/2}T'] = e^{−a/2}(−2coth(a/2) − 3 + 2log(2sinh(a/2)))
                   C_B := ∂_u∂_v[e^{−x/2}T'] = −e^{−a/2}(1/sinh²(a/2) + 2coth(a/2) + 3/2 − log(2sinh(a/2)))
   (twisted versions and both-e^{−/2} forms in vary2083.json). The derivative hits the density and drags in −½T,
   a log-height remainder. Exact: k_∞ = −¼·avg_ε⟨∂_uĜ_u,Ĝ_v^{ε∨},ω⟩_raw − ⅛e^{−a/2}·avg_εT_raw^ε, with
   avg_εT_raw^ε = 6−2log|e^{2u}−e^{2v}|. So Ĝ does not absorb the half-density; it produces k_∞ plus a log remainder.
D. sign averages:
   avg A_raw = −4/(1−q²);  avg A_bal = −(coth(a/2)+tanh(a/2)) = −2coth a;  avg B = −2/sinh²a = −8q²/(1−q²)² = 2B⁺(2a).
   Cooked t2078 identity CONFIRMED (residual 0, u>v only): k_∞ = −¼ e^{−a/2}·avg_ε A^ε_raw = q^{1/2}·1/(1−q²).
   With balanced sections it fails: −¼e^{−a/2}avg A_bal = ½e^{−a/2}coth a = k_∞·(1+q²)/2.
   For u<v the raw identity also fails (avg gives 4q²/(1−q²)). Other exact rewritings found:
     k_∞ = (−¼A⁺_raw)·1/(2cosh(a/2))         (AB_0 on O × Fermi factor)
     k_∞ = ½(√(−¼B⁺) + √(¼B⁻)) = ½(1/(2sinh(a/2)) + 1/(2cosh(a/2)))   (numerically exact)
   The last is the only one with no explicit e^{−a/2} and no orientation: the half-density comes out as the SQUARE ROOT
   of the full density that the second variation produces (Szegő ≈ √Bergman; |det(1−P)|^{−1/2} vs |det(1−P)|^{−1}).
   But a square root of a pairing is not a pairing; it is a nonlinear hand insertion.
F. comoving FS (t2078 T_tr): ∂_u∂_vT_tr = −1/sinh²(a/2) + 2(1−a coth a)/sinh²a  (a coth a extra; ~ −2/3 at 0, ~ −8a e^{−2a} at ∞).
   ∂_uT_tr = −2coth(a/2) + coth a − a/sinh²a + coth u − u/sinh²u  (non-invariant u-only term). Same coth extras only;
   no qualitative change.

## 3. Asymptotics vs k_∞ (k_∞ = 1/(2a) + 1/4 − a/48 + …;  k_∞ ~ e^{−a/2})
| object | a→0 | a→∞ |
|---|---|---|
| k_∞ | 1/(2a)+1/4−a/48 | e^{−a/2} |
| T'_bal (graph pairing) | −4 log a + 6 | −2a + 6 |
| −⅛A⁺_raw = ½/(1−q) | 1/(2a)+1/4+a/24 | → 1/2 (constant) |
| −⅛A⁺_bal = ¼coth(a/2) | 1/(2a)+a/24 | → 1/4 |
| −⅛avg A_raw = ½/(1−q²) | 1/(4a)+1/4+a/12 | → 1/2 |
| −¼e^{−a/2}avg A_raw (cooked) | = k_∞ exactly | = k_∞ |
| B⁺ | −4/a² + 1/3 | −4e^{−a} |
| B⁻ | 1 − a²/4… | 4e^{−a} |
| avg B | −2/a² + 2/3 | −8e^{−2a} |
| C_A (dual Ĝ, bal) | −4/a + 2log a − 1 + … | ~ a e^{−a/2} |
| C_B (dual Ĝ, bal) | −4/a² − 2/a + log a + … | ~ +(a/2) e^{−a/2} |
| ∂u∂vT_tr | −4/a² − 1/3 | −4e^{−a} |
Spectral orders (FT in x=u−v, t≠0): T' ~ 4πcoth(πt)/t; A ~ 4πi coth(πt) (bounded, odd); B ~ 4πt coth(πt) (~|t|);
k_∞: FP 1/(2|x|) singularity ⇒ ~ −log|t| (digamma-type). k_∞ sits between A and B: it is the EVEN (|·|) version of A's
PV 1/x pole, i.e. sgn(u−v)·A, which is a Hilbert-transform-type insertion.

Reading: the first variation gets the POLE right (residue matches after ×(−⅛); with raw sections even the constant 1/4)
but not the decay; the second variation gets an exponential decay but with full density e^{−a} and a double pole;
the half-densitized family gets e^{−a/2} but carries a log/linear-in-a remainder.

## 4. Insertions: intrinsic vs by hand
- Derivative: now intrinsic (it is the definition of V_u). ✔
- Normalization ¼: conventional, = 1/(2·deg_ωΓ_v) (2 from |s|² in dd^c log|s|², 2 from ∫_{Γ_v}ω for ω=O(1,1); with third
  class pr₁*ω_FS it becomes ½). Fixed by conventions, not by the current. ~neutral.
- Orientation u>v / choice of puncture: still by hand for A (A is odd; k_∞ is even). B removes it. ✔ for B only.
- Additive constant (raw vs balanced): A depends on it; the cooked identity needs RAW. B removes it.
- Half-density e^{−a/2}: NOT produced. Ĝ_u puts it on the current but the derivative then generates −½T (log height);
  the cooked identity needs e^{−a/2} as an external multiplier AFTER differentiating. In B-language it is a square root.
- Sign average: NOT produced by the current. Geometrically = passing to the ±1 quotient (q→q²); it can be motivated by
  R^×={±1}×R_+ at the real place (even test functions), but that is outside the P¹×P¹ intersection theory.

## 5. Verdict
Still cooked. The intrinsically defined variational currents remove exactly one insertion (the derivative) and, at second
order, also the orientation and section-constant dependence; what they canonically produce are full-density objects:
−¼⟨V_u,Γ_v,ω⟩_raw = 1/(1−q) (the Atiyah–Bott index on functions at the attracting fixed point, again a local trace in
disguise, the digamma = d log Γ relation) and −¼⟨V_u,V_v,ω⟩ = q/(1−q)² = 1/|det(1−P)| (Bergman/Guillemin-type, metric-
independent). k_∞ = q^{1/2}/(1−q²) needs the half-density q^{1/2} (K^{1/2} instead of K⁰, or √ of the second variation)
and the ±1 projection (q→q²), neither of which any variational current on P¹×P¹ supplies; the half-densitized family Ĝ_u
just trades the multiplier for a log-height remainder. It is better than Route 2's graph pairing — the pole shape and
the geometric-series structure now appear without hand insertion — but it does not fail "like Route 2" either: it lands
one level off (density weight 0 or 1 instead of ½), and closing that gap is precisely the cooked step. Open ~1.8 is
unchanged; Φ is not constructed; no Hodge-type sign; nothing here bears on RH.

## 6. Analytic caveats
- A and B are distributions in (u,v): A has a PV 1/(u−v) pole, B a Hadamard FP 1/(u−v)² (from ∂²log|u−v|; no extra δ
  terms since log|x| is L¹_loc). All "small-a" lines are for a≠0.
- ⟨V_u,V_v,ω⟩ was defined via the star product with [V_u]=0; I did not prove a general Gillet–Soulé star-product theory
  for order-1 dipole currents, only that the formula is the u,v-derivative of the t2078 pairing and that the Cartan form
  gives the same number. The intersection of V_u and V_v at (0,0),(∞,∞) is benign because ξ vanishes there.
- k_∞'s ~ −log|t| spectral growth is stated from its 1/(2|x|) singularity (standard), not separately computed here.
- The √ identity and the B-positivity are exact but interpretive; the Szegő/Bergman and |det(1−P)|^{∓1/2,∓1} readings
  are analogies, not theorems about Φ.

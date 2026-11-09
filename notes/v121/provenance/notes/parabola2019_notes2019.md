# t2019 — parabola boundary, differentiation, and the missing complete pairing
Scratch only. No Page/repository/manuscript/cloud/web actions. Read parabolic1998/notes1998.md and sos2010/notes2010.md. No new numerical claims.
Labels: [EXACT] direct computations below; [THM] standard theorem with hypotheses; [ANALOGY] constructive interpretation; [OPEN] missing construction. Work over R for forms unless specified.

## Proposed chat answer (~650 words)

Your parabola intuition identifies something useful: **a divergent affine expression can become a regular boundary expression, while differentiation records precisely how it meets that boundary.** That gives us a constructive model for the map we need—not yet the positivity theorem.

**1. Your tangent-at-infinity picture is exact. [EXACT]**
The projective parabola is \(YZ=X^2\). Its tangent at \((t,t^2)\) is
\[
2tX-Y-t^2Z=0.
\]
The affine intercept is \(-t^2\to-\infty\), but the projective line coefficients converge to \([0:0:1]\): the line \(Z=0\).
In the chart \(Y=1\), put \(r=X/Y\), \(z=Z/Y\). Then
\[
z=r^2,\qquad r=1/x,\qquad z=1/y.
\]
Infinity is now \((0,0)\), with \(dz/dr=0\). The line at infinity restricts to \(r^2=0\), so its intersection has multiplicity two. This is a genuine second-order boundary contact on a smooth curve.

**2. Roots of unity describe branches of a projection. [EXACT/ANALOGY]**
For \(y=x^2\), the curve is already smooth; \(x\) is its parameter. The inverse \(x=\sqrt y\) branches because the projection to \(y\) ramifies. The symmetry \(x\mapsto-x\) exchanges its sheets. More generally, for the local cyclic model \(y=T^n\), the roots of unity act by \(T\mapsto\zeta T\). This is a useful model for organizing sheets—not an operation that itself supplies positivity.
At a modular cusp, after moving it to infinity, \(q=e^{2\pi i z/w}\), with cusp width \(w\), supplies a regular boundary parameter. Roots of unity can record choices of roots of \(q\). The common idea is **choose the right local parameter and retain its symmetry**.

**3. We already have an exact arithmetic differentiation map. [EXACT]**
On a finite interval \(I=[a,b]\), define
\[
\mathcal D G=G''-\tfrac14G,\qquad G\in H^2_0(I).
\]
Here both \(G\) and \(G'\) vanish at the endpoints. Integration by parts gives
\[
\int_I e^{\pm u/2}\mathcal DG\,du
=\left[e^{\pm u/2}(G'\mp G/2)\right]_a^b=0.
\]
Conversely every \(F\in E_0\) has this representation. Thus the two moment conditions become explicit boundary conditions. This is the strongest direct connection between your differentiation intuition and our actual energy.

**4. What an independently constructed class map would add. [OPEN]**
The map above lands in functions. A geometric class map would instead assign \(F\mapsto c(F)\) in an independently defined geometric space, and prove
\[
B_W(F,H)=-I(c(F),c(H)),
\]
with the classes in the subspace where an established sign theorem applies. Here \(B_W\) is the polarization of the complete energy. The prime terms, Gamma term, diagonal subtraction, and boundary contributions must all match—not just their asymptotic shapes.

The operator alternative is equally concrete: construct a Hilbert space and a linear map \(\mathcal A\), independently of the desired sign, and prove
\[
B_W(\mathcal DG,\mathcal DH)
=\langle\mathcal AG,\mathcal AH\rangle.
\]
That would supply positivity. Defining \(\mathcal A\) as the square root of the target would assume what we seek.

**5. Where the analogy becomes a research direction. [EXACT/OPEN]**
Differentiation commutes with every prime translation, so it transports the complete energy without discarding the subtraction. Our exact Gamma/pole cancellation likewise regularizes the formula, but leaves a signed Chebyshev-error pairing. A chart change alone cannot erase that sign problem.

The Lefschetz piece \(\mathbb L\) records cohomological degree two; it is not the coordinate operation \(r\mapsto r^2\). Its constructive role would be through an actual ample class and its pairing theorem. **The promising bridge is therefore boundary conditions → an explicit map → a complete pairing identity → a sign theorem**, rather than quadratic inversion alone.

## Detailed checks for parent

### A. Smooth compactification and dual differentiation [EXACT]
Parametrization: [u:v] -> [uv:u^2:v^2]. On v!=0, x=u/v, y=x^2. Infinity is v=0, [0:1:0]. On u!=0, r=v/u and z=r^2. The gradient of YZ-X^2 at infinity is (0,0,1), so the point is smooth and the tangent is Z=0. The local intersection ring with Z=0 is k[r]/(r^2), length two. This is a nonreduced intersection, not a singular curve.

For homogeneous Q=YZ-X^2, dQ gives tangent [-2t:1:t^2], equivalent to [2t:-1:-t^2]. The dual conic in line coordinates [alpha:beta:gamma] is alpha^2=4 beta gamma. At infinity normalize gamma=1: [-2r:r^2:1]. This is smooth at r=0; its tangent beta=0 corresponds, by duality, to the original point [0:1:0]. Conormal/polar duality therefore really records tangency and differentiation; no metric or positive inner product occurs in these equations.

The real affine parabola has two ends meeting at its one projective point at infinity. That point is not a reflecting boundary condition imposed on a differential equation. Projective compactification does not by itself supply energy conservation or a metric.
Euclidean curvature is kappa(x)=2/(1+4x^2)^(3/2), tending to zero, although y''=2 is constant. Acceleration of the parametrized trajectory (t,t^2) and intrinsic curvature are not identical. The two derivatives dy/dx=2x and dz/dr=2r belong to different coordinate functions and are compatible; infinity did not contain a nonsmooth point to be repaired.

### B. Roots, ramification, cusps [EXACT; standard local models]
Over C, the map T->T^n is ramified at zero. On its punctured target, monodromy cycles sheets by zeta_n, and mu_n is the deck group. The total source is smooth already. For the parabola projection use T=x; the two branches of the inverse are not two distinct germs of the parabola at the origin.
This tame cyclic model is useful but not a universal description of arbitrary singularities or arbitrary degree-n charts; the degree of a global plane equation does not dictate every local parameter's power. No characteristic-p assertions are made.

For a modular cusp choose a Mobius coordinate z with that cusp at infinity and stabilizer generated by z->z+w (up to any elliptic/stack qualifications). Then q=exp(2 pi i z/w) is invariant under that translation, gives a punctured-disk coordinate, and extends by q=0. For a cover q=T^n, T has mu_n ambiguity. The existence of a cusp need not originate in fractional translations at rational points, nor does q eliminate arithmetic errors by itself.

### C. Differential map, inverse and domain [EXACT]
Let I=[a,b], E0(I)={F in L2(I): int e^(u/2)F=int e^(-u/2)F=0}; zero-extend F.
For smooth compact G, Dcal=(d/du-1/2)(d/du+1/2); extend to H^2_0 by Sobolev traces. The boundary formula in the proposed answer follows by two integrations by parts.
For F in E0, define on R
G(u)=2 int_{-infty}^u sinh((u-s)/2)F(s) ds.
Distributionally Dcal G=F; G=0 below a and for u>b,
G(u)=e^(u/2) C_-(F)-e^(-u/2) C_+(F)=0.
Thus G is H^2, compactly supported in I, with G=G'=0 at both endpoints. Uniqueness follows because a compactly supported solution of Dcal G=0 must vanish. This proves Dcal:H^2_0(I)->E0(I) is a bijection. No compact inverse/resolvent for the energy operator is inferred.
For rough L2 data, this parametrization is valid independently of energy finiteness: identities involving W are initially stated on smooth compact tests, then only extended to a verified form domain. H^2_0 alone does not automatically guarantee the logarithmic Gamma form is finite after applying Dcal.

With Fourier convention Fhat(t)=int e^(-itu)F(u)du,
Fhat(t)=-(t^2+1/4)Ghat(t).
Every translated norm is transported, not abolished:
||Dcal G||^2=||G''||^2+(1/2)||G'||^2+(1/16)||G||^2,
||Dcal G-T_b Dcal G||^2=||Dcal(G-T_bG)||^2
using zero extensions. Without clamped traces the zero extension of G'' can acquire boundary delta terms. They are not silently dropped.

### D. Exact pulled-back target and surviving remainder [EXACT]
Let F=Dcal G, J5(F)=int_0^infty k5(a)||F-T_aF||^2 da,
Jp(F)=sum_(log n<A) Lambda(n)n^(-1/2)||F-T_(log n)F||^2,
M_A=-K0+2 sum_(log n<A) Lambda(n)n^(-1/2).
Then the identity established in sos2010 is
W(Dcal G)=J5(Dcal G)+Jp(Dcal G)
 -(M_A-4)[||G''||^2+||G'||^2/2+||G||^2/16]
 -||G'||^2-||G||^2/4.
In particular the negative local remainder has not become positive by differentiation.
Equivalently, with E(x)=psi_Cheb(x)-x, k5(a)=e^(-5a/2)/(1-e^(-2a)), K5(0)=psi_digamma(5/4)-log pi,
W(F)=K5(0)||F||^2+J5(F)-2 int_[1,e^A] x^(-1/2)<F,T_(log x)F> dE(x).
K5(0) is negative, not refitted. For real F, correlation is real; in the complex version use real parts and polarized Hermitian forms. An endpoint prime at log n=A contributes zero correlation for supported tests, so strict cutoff is harmless in this correlation formula; retain the original strict convention in the jump/mass formula.
The last identity holds beyond E0 (as already checked in sos2010); it does not prove the E remainder nonnegative. "Prime acceleration" is at most an analogy, not the definition of E, its derivative, or a coordinate singularity.

### E. What is required of the proposed representations [THM + OPEN]
Geometric template: real divisor classes on an actual smooth projective surface, intersection I, and ample class H. Hodge index says I is nonpositive on H-perp. If a linear c:E0->H-perp is independently constructed and -I(cF,cH)=B_W(F,H) is proved, the target sign follows. This is a template, not an assertion that those classes exist for our W. Other geometric settings need their own established sign theorem and exact hypotheses, including any archimedean or regularized terms; a formal finite-dimensional conic does not accommodate the infinite-rank window form by itself.

Operator template: H independently Hilbert-positive, A linear on a specified dense test domain, and the mixed identity B_W(Dcal G,Dcal H)=<AG,AH>_H. A pointwise identity for all G would imply the mixed one by polarization, but testing selected eigenvectors or omitting cross terms would not. If one claims a positive self-adjoint operator rather than a test-domain norm representation, one additionally owes density, closability/closedness and the relevant representation theorem hypotheses. No square root of W or zero-based RH positivity is an input.
Positive-state template: independently positive functional omega on a *-algebra, with B_W(F,H)=omega(a(F)^*a(H)) and linear a, likewise matches all terms. Choosing omega solely to encode W's desired positivity is not independent.

An invertible real change of variables preserves a finite quadratic form's inertia by congruence; more generally a bijective domain reparametrization preserves whether negative directions exist. A restriction can change signs, which is why E0 and the boundary conditions must be explicitly specified and cannot be changed to remove unwanted directions.

### F. Lefschetz, constructively but accurately [THM/ANALOGY]
The standard decomposition h(P1)=1 direct-sum L has the Lefschetz/Tate summand realized in cohomological degree two. Degree two here is not the exponent of a coordinate. The same abstract P1 has degree-one, conic and higher Veronese embeddings, all with that same motive. Therefore the decomposition alone selects neither the parabola nor quadratic inversion nor any prime/Gamma pairing.
An ample class can implement a Lefschetz operator (cup product) and participate in Hodge-Riemann sign theorems once the geometric/cohomological setting exists. This is the useful destination of the analogy: construct the classes, identify their boundary/moment restrictions, and prove the complete pairing identity. No claim that the coordinate chart removes E(x) or proves RH follows.

## Scope / parent cautions
No new theorem about RH, no numerics, no source fetches, no changes outside this file. Mathematical local-model checks are explicit above. No unaudited scheme claims used; no return to closed Jacobian/Rosati routes. Existing sos2010 numerical positivity is not cited as certified. Do not repeat its loose "Lemma A holds near A=1" language as a proof: positive Ritz upper bounds certify no lower bound. Existing exponential Doob claims require their convergence strip; they are not needed here.

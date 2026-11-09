# t2023 — actual weak operator, closed-form realization, and Yoneda-inspired probes
Scratch only. Labels: [EXACT] direct identities/proofs; [THM] standard closed-form representation theorem; [CONSTRUCTED] object specified without spectral zeros or a sign assumption; [ANALOGY] comparison; [OPEN] missing independent positive factorization. No new numerics.
Context: polarity2021/notes2021.md; sos2010/notes2010.md; parabola2019/notes2019.md. Complete W definitions were already sent by parent. No Page/repo/manuscript/cloud/contact actions.

## Proposed chat answer (<700 words)

**W is the complete arithmetic energy:** boundary-pole contribution plus prime/Gamma jump energy minus the exact diagonal subtraction. It is a quadratic form on test functions; its mixed pairing records all cross terms.

Your Yoneda idea suggests a useful shift: **identify an operator by everything it does to probes, rather than guessing its appearance.** In fact, there is a concrete operator already determined by our arithmetic inputs. What remains unknown is its independently explained positive structure.

### 1. We can construct the signed operator now. [CONSTRUCTED/EXACT]
Zero-extend a function F from its interval I. The jump operator is
\[
\mathscr L_A F=1_I\left[\int_0^\infty k_\infty(a)(2F-T_aF-T_{-a}F)\,da
+\sum_{\log n<A}a_n(2F-T_{\log n}F-T_{-\log n}F)\right].
\]
The integral is first understood weakly, retaining its cancellation at zero. Then
\[
\mathscr K_A=\mathscr L_A-M_A I+\mathscr P_A,
\qquad \mathscr P_AF=C_-(F)e^{u/2}+C_+(F)e^{-u/2},
\]
with exponentials restricted to I. Its pairing is exactly
\[
\langle\mathscr K_AF,H\rangle=B_W(F,H).
\]
This is not just a finite matrix: the nonnegative jump form is closed on its zero-extension energy domain. Adding the bounded mass and rank-two pole terms gives a semibounded self-adjoint realization by the standard closed-form theorem. This construction needs no RH assumption.

On E₀ the pole term vanishes. Restricting the closed form gives the corresponding self-adjoint constrained operator. **Self-adjoint and bounded below do not mean nonnegative:** the remaining question is whether the prescribed mass is controlled on this particular constrained sector.

### 2. Its closest analogue is a nonlocal Schrödinger operator. [EXACT/ANALOGY]
The positive jump part is a nonlocal Laplacian; subtracting M_A is a negative constant potential; the pole term is a finite-rank boundary correction. Its Gamma multiplier grows logarithmically at high frequency, rather than quadratically like an ordinary Laplacian.

A d’Alembertian is not the closest model. Its hyperbolicity concerns propagation and principal-symbol signature. Our boundary plane’s hyperbolic pairing is a different meaning of “hyperbolic”; it does not turn this nonlocal operator into a wave operator.

### 3. What the Yoneda viewpoint adds. [EXACT/ANALOGY]
Knowing every mixed value B_W(F,H) determines the weak operator uniquely: each F is identified through its responses to all probes H. Polarization recovers these mixed values from exact diagonal outputs.

We can demand compatibility with interval enlargement, reflection, and the arithmetic convolution/local-place structure. There is already an exact consistency check: enlarging a window adds prime jumps, but their diagonal masses cancel on functions supported in the smaller window. Thus the complete pairing—not its pieces separately—is compatible across windows.

That resembles Yoneda’s “understand an object through all its maps,” but a literal Yoneda argument still requires a specified category, functors and natural transformation. Complete probe data identify an operator; they do not independently prove its sign.

### 4. What we should now search for. [OPEN]
Not another operator whose quadratic form is W—we have one. The constructive target is an arithmetic map into an independently positive Hilbert space satisfying
\[
B_W(\mathcal DG,\mathcal DH)=\langle\mathcal AG,\mathcal AH\rangle,
\qquad\mathcal D=D^2-\tfrac14,
\]
for every admissible pair G,H, with compatible domains and window enlargements. The known jump-gradient map supplies the positive energy, but not the subtraction. Explaining that subtraction within a complete positive identity is the substantive missing step. Taking a square root after assuming nonnegativity would not supply that explanation.

## Detailed proofs and operator domains

### A. Conventions and exact weak expression
I=[-A/2,A/2], A>0. Hilbert inner product <F,H>=int F conj(H), linear in the first argument. E:L2(I)->L2(R) is zero extension. T_a f(u)=f(u-a). Set r_±=exp(±u/2)|I, C_±(F)=<F,r_±>, k(a)=exp(-a/2)/(1-exp(-2a)), a_n=Lambda(n)/sqrt(n).

For smooth compact F,H in I define
q_inf(F,H)=int_0^infty k(a)<EF-T_aEF,EH-T_aEH>_(R) da,
q_p(F,H)=sum_(log n<A)a_n<EF-T_(log n)EF,EH-T_(log n)EH>_(R),
p(F,H)=C_-(F)conj(C_+(H))+C_+(F)conj(C_-(H)),
q_W=q_inf+q_p-M_A<F,H>+p,
M_A=-K0+2sum_(log n<A)a_n, K0=digamma(1/4)-log pi.
Translation adjunction immediately gives
<F-T_aF,H-T_aH>=<2F-T_aF-T_-aF,H>.
Consequently the distributional operator is exactly the expression in the proposed answer. Do not integrate the separate divergent terms 2F, -T_aF and -T_-aF at a=0: only their sum is integrable. For compact smooth F that sum is O(a^2) in suitable test norms.

The pole operator P_AF=C_-(F)r_++C_+(F)r_- is complex linear and bounded self-adjoint. In particular <P_AF,H>=p(F,H), with no conjugation of C_± in the operator formula. Its operator norm is at most 2||r_+||||r_-||. No endpoint derivative, reflection law or local Neumann condition has been imposed: zero extension defines the killed/nonlocal boundary convention. The a>A tail in q_inf is retained; for both supported tests its value is 2<F,H>int_A^infty k(a)da.

### B. Closedness, density and self-adjoint realization [proof + THM]
Define the whole-line nonnegative extended quadratic energy
E_inf(f)=int_0^infty k(a)||f-T_af||_2^2 da,
V_R={f in L2(R): E_inf(f)<infty}.
Fourier Plancherel, with fhat(t)=int exp(-itu)f(u)du, gives
E_inf(f)=(1/(2pi))int j(t)|fhat(t)|^2dt,
j(t)=2int_0^infty k(a)(1-cos(at))da >=0.
Here j(t) is finite for each t because int_0^1 a^2 k(a)da<infty and int_1^infty k(a)da<infty. This weighted Fourier-space norm proves V_R complete in ||f||_2^2+E_inf(f).
Let V_I={F in L2(I):EF in V_R}. The subspace of whole-line L2 functions supported in closed I is closed; therefore V_I is complete in the same energy norm. It is dense in L2(I) because it contains C_c^infty(I). No assertion that an arbitrary L2 function has finite energy is made.
Each prime jump form is bounded: ||f-T_bf||_2^2<=4||f||_2^2, so q_p is bounded with norm at most 4sum a_n. Mass and P_A are bounded self-adjoint perturbations too. Hence q_W is a densely defined closed symmetric semibounded form on V_I, with lower bound at least -(M_A+||P_A||)||F||_2^2. The standard first representation theorem for closed semibounded forms [THM] supplies a unique self-adjoint operator K_A with
D(K_A)={F in V_I: there exists h in L2(I) such that q_W(F,H)=<h,H> for every H in V_I}, K_AF=h.
This is an actual continuum construction, not an inference from finite Perron–Frobenius or a guessed domain. The integral expression in §A equals K_A only on vectors for which that weak distribution is represented by an L2 function with the required form identity. We have not identified all of D(K_A) with a classical Sobolev space.
No compact resolvent, spectral gap, ground-state simplicity, positive spectrum or RH is inferred here. The nonnegative operator L_A is separately supplied by the analogous nonnegative jump form.

### C. Constrained sector E0 and compression
E0={F in L2(I):C_+=C_-=0} is closed of codimension two. On a nonempty interval the functions r_+,r_- are linearly independent. Their Gram matrix in the centered window is
G=[[2sinh(A/2), A],[A,2sinh(A/2)]],
with eigenvalues 2sinh(A/2)±A>0.
Thus the independent L2 orthogonal projector is
Pi F=F-sum_(i,j in {+,-}) r_i(G^-1)_(ij)C_j(F).

V_I cap E0 is dense in E0: choose two compact smooth correction functions eta_1,eta_2 with invertible moment matrix (possible because the two moment functionals are independent on C_c^infty(I)). Approximate F in E0 by compact smooth f_n and subtract a linear combination of these eta_i that kills the residual moments. The coefficients tend to zero, so corrected approximants converge in L2.
The restricted form is closed: E0 is L2-closed, hence its intersection with V_I is closed in the energy/form norm. It is semibounded and dense in E0. The same representation theorem supplies a self-adjoint constrained operator K_A,0 on E0, without a positivity assumption.
Its symbolic form compression is Pi K_A Pi, with P_A killed because Pi P_A Pi=0. One must not assert equality with the raw product on an unstated operator domain; form compression is the rigorous definition here. In particular r_± are generally not compact smooth functions, so naively commuting Pi through an unbounded operator is not a domain argument.
On E0, q_W=q_inf+q_p-M_A||F||^2. A positive square root of K_A,0 would be available by spectral calculus IF K_A,0>=0 had already been proved; it is not an independent factorization or proof of that fact.

### D. Fourier symbol and differential comparison
The digamma identity established in sos2010 gives
j(t)=Re digamma(1/4+it/2)-digamma(1/4).
Writing K_Gamma(t)=Re digamma(1/4+it/2)-log pi,
the translation-invariant operator whose compression gives the nonpole part on I has multiplier
m_A(t)=K_Gamma(t)-2sum_(log n<A)a_n cos(t log n).
Thus K_A=E^*m_A(D)E+P_A as a weak/form identity, not a claim that unrestricted m_A(D) preserves interval support. An individual m_A corresponds to the chosen finite cutoff A; there is no convergent unregularized all-prime cosine sum asserted here.
Stirling/digamma asymptotics [THM] give K_Gamma(t)=log|t|-log(2pi)+O(|t|^-2). For fixed A the cosine part is bounded, so the high-frequency growth is logarithmic. This operator is consequently not a second-order Laplacian with symbol t^2; “nonlocal Schrödinger” describes its structure, not equality with a conventional differential Hamiltonian. A wave/d'Alembert operator's indefinite principal symbol and propagation theory are not supplied by the boundary hyperbolic plane.

### E. Probe determination and precise window compatibility
The map F->q_W(F,.) is a distribution-valued weak operator on compact smooth tests. If two weak operators give the same q(F,H) for all probes H, their outputs agree as distributions. If two closed form realizations have identical forms including domains, their associated self-adjoint operators agree. Agreement merely on chosen matrix entries or an unspecified dense set without a core/domain argument is weaker.
For a Hermitian q, knowing q(F,F) for all complex F recovers mixed values by polarization. With the present linear-first convention,
q(F,H)=(1/4)[q(F+H)-q(F-H)+i q(F+iH)-i q(F-iH)].
For real tests the simpler difference formula suffices.

Let I subset J be intervals and i:L2(I)->L2(J) be zero extension. For F,H supported in I and a new prime jump b=log n>=width(I), both shifted correlations vanish. Its additional contribution to the larger-window jump form is 2a_n<F,H>; its additional contribution to -M<F,H> is exactly -2a_n<F,H>. Gamma and moment terms are unchanged. Therefore
q_W,J(iF,iH)=q_W,I(F,H).
This is an exact complete-pairing identity, valid at the form level. It implies weak compression compatibility, not K_J i=i K_I: on the larger interval the operator can generate values outside I, and its domain/boundary action changes. The positive jump form L_A alone does NOT obey the same uncorrected compatibility because its mass has changed.
Reflection u->-u about the centered interval preserves the form and exchanges C_±. Whole-line translation invariance of a fixed-cutoff symbol does not imply translation symmetry within a fixed killed window. Comparisons of displaced intervals use the corresponding displacement/zero-extension maps.

Yoneda [THM, conceptual]: a category must be specified, and natural transformations between its representable Hom functors identify morphisms. No such category with an independently positive representing object has been constructed here. Probe uniqueness and the exact compression identity are rigorous, useful inputs to a future functorial formulation; they are not themselves a positivity theorem.

### F. Known gradient versus unknown complete positive representation
The known positive jump form has an explicit edge-gradient map:
J_A F = (sqrt(k(a))(EF-T_aEF), (sqrt(a_n)(EF-T_(log n)EF))_n)
into L2((0,infty),da;L2(R)) direct-sum a finite collection of L2(R) spaces. Its norm squared is q_inf(F)+q_p(F). Thus on E0,
W(F)=||J_A F||^2-M_A||F||^2.
This is an independently positive ambient Hilbert representation of the jump part, not of W. The exact missing bound is ||J_A F||^2>=M_A||F||^2 on E0. Calling this a constrained Poincare inequality is structurally accurate, but writing the inequality does not establish it. The negative mass cannot be dropped or absorbed by naming another metric.
A successful arithmetic construction could instead define a different linear A on a verified domain of clamped G, with
B_W(Dcal G,Dcal H)=<AG,AH>, Dcal=partial_u^2-1/4,
and a compatibility rule under interval inclusions. Neither A=sqrt(W) nor a GNS construction beginning with the assumed positive W is independent. The existing polarity2021 drop-n=2 ghost shares much of the probe/symmetry setup but fails the sign; it remains a concrete test of whether a proposed additional arithmetic structure has genuine coefficient sensitivity.

## Scope and completed work
Constructed the full signed weak operator and justified its semibounded self-adjoint realization, plus its constrained version. This establishes baseline operator existence, not positive factorization or a continuum ground-state/index theorem. No numerical, web or external-source claims were added. Standard closed-form and asymptotic inputs are explicitly labeled THM, rather than attributed to an unchecked citation. No additional research launched.

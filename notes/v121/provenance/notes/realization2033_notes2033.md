# t2033 — explicit arithmetic delay evolution, signed KYP identity, and tested reactive hypothesis
Scratch only. [EXACT] algebra/proofs; [CONSTRUCTED] independently specified arithmetic evolution; [SIGNED] valid identity without positivity; [THM] explicitly stated standard input; [NUM] uncertified evaluation; [OPEN] missing independently positive coupled storage. No RH claim.
Context: dispersion2030/notes2030.md, operator2023/notes2023.md, sos2010/notes2010.md. No change to the prior complete-W probe identity is needed. No Page/repository/manuscript/cloud/external-message actions. No extra research launched.

## Proposed chat answer (under 750 words)

**We can build an actual arithmetic state evolution and derive its energy balance. It gives a useful signed KYP realization—and exposes exactly where independent positivity must enter.**

Write \(b_n=\log n\), \(a_n=\Lambda(n)/\sqrt n\), and \(q(z)=\xi'/\xi(1/2+z)\). On Re z>1/2,
\[
q(z)=\frac1{z-1/2}+\frac1{z+1/2}+\frac{K_0}{2}
+\int_0^\infty k(a)(1-e^{-az})\,da
-\sum_n a_ne^{-b_nz}.
\]
Every coefficient is the original arithmetic one.

**1. Constructed driver and state. [EXACT]**
Feed a smooth causal input u(t) into a history line \(x(t,s)=u(t-s)\), satisfying \(x_t+x_s=0\), and two boundary channels
\[
\dot x_+=\tfrac12x_++u,\qquad
\dot x_-=-\tfrac12x_-+u.
\]
Read the output from their sum, the Gamma-weighted differences \(u-x(t,a)\), and the negative prime-delay samples. Its Laplace transfer is exactly q on the stated half-plane. At finite time only finitely many prime delays have been reached, so this is a concrete causal arithmetic evolution, not a state space defined from assumed zeros.

**2. Exact storage-and-supply calculation. [SIGNED]**
For a finite prime cutoff B, define positive delay-line storage
\[
S_{\rm jump}=\int k(a)\int_0^a|u(t-s)|^2ds\,da
+\sum_{b_n<B}a_n\int_0^{b_n}|u(t-s)|^2ds,
\]
and boundary storage \(S_{\partial}=2\operatorname{Re}(x_+\bar x_-)\). Then
\[
2\operatorname{Re}(\bar u y_B)
=\frac{d}{dt}(S_{\partial}+S_{\rm jump})
+D_{\rm jump}-M_B|u|^2.
\]
Here D_jump is the corresponding sum/integral of \(|u(t)-u(t-a)|^2\). Integrating recovers the complete W, including the pole term and exact subtraction. For two-moment-zero inputs, the terminal boundary state vanishes, but the mass does not disappear.

This is the desired type of calculation. However, boundary storage is indefinite, and the dissipation remainder contains the negative mass. Neither has been declared positive.

**3. Two concrete obstacles now isolated. [EXACT]**
First, every finite prime cutoff leaves an observable pole at z=1/2. Thus those truncated full-transfer systems cannot themselves be passive on the unshifted right half-plane. In the genuine transfer, the prime-density contribution cancels this pole; the Gamma shift cancels the other boundary pole. That cancellation must happen before a positive realization is inferred.

Second, summing the displayed positive prime-line storages over all primes gives infinity for any nonzero past input. Their divergent diagonal mass cancels in the output/energy formula, not in that naive positive storage. So simply assembling independent passive components does not solve the infinite system. A genuinely coupled storage construction is required.

**4. “Reactive mass” has a legitimate necessary test. [EXACT/NUM]**
The functional equation gives q(0)=0. A positive theta-integral calculation gives
\[
q'(0)=\xi''(1/2)/\xi(1/2)>0,
\]
approximately 0.0462099862. Thus the low-frequency response passes the natural inductive/reactive test. But q(z)=z+z³ also has zero constant term and positive slope, while having negative real part at z=1+2i. The test is insufficient. A minimum nonzero excitation amplitude is likewise not supplied by a linear homogeneous system: input and energy scale continuously.

**What we gained:** an explicit arithmetic evolution, an exact signed energy identity, and a precise failure of the naive positive-component assembly. The narrow next target is a finite, independently positive *coupled* storage on the pole-cancelled arithmetic history space whose dissipation is nonnegative and whose elimination preserves our exact kernel. We have not constructed that storage; neither the reactive coefficient nor generic KYP terminology proves it.

## A. Exact transfer and a classical core for the evolution
Use complex inputs u in C_c^infty((0,infty)), zero for t<0, and zero initial states. On the history core define
x(t,s)=u(t-s), s>=0, partial_t x+partial_s x=0, x(t,0)=u(t).
Set
x_+(t)=int_0^t e^((t-r)/2)u(r)dr,
x_-(t)=int_0^t e^(-(t-r)/2)u(r)dr.
These obey the two ODEs in the proposed answer. The exact arithmetic output is
y(t)=x_+(t)+x_-(t)+(K0/2)u(t)
 +int_0^infty k(a)[u(t)-u(t-a)]da
 -sum_(n=p^m)a_n u(t-b_n),
k(a)=e^-a/2/(1-e^-2a), b_n=log n, a_n=Lambda(n)/sqrt(n).
For each finite t, only n<=e^t can contribute to the prime sum. Near a=0, u(t)-u(t-a)=O(a) and k=O(1/a); at infinity k decays. Thus the output is well defined on this explicit smooth causal core. The history has unbounded trace readouts at discrete lags; we do NOT infer an everywhere bounded B,C system on a chosen Hilbert space from this core construction.

For Laplace parameter Re z>1/2 the prime sum is absolutely integrable against the input transform, because sum a_n e^-Re(z)b_n converges there. The boundary ODE transforms have the same abscissa, and the Gamma integral converges absolutely after its local cancellation. Fubini gives Y(z)=q(z)U(z), using
q(z)=r(z)+g(z)+ell(z),
r(z)=1/(z-1/2)+1/(z+1/2),
g(z)=K0/2+int k(a)(1-e^-az)da
 =(1/2)digamma(1/4+z/2)-(1/2)log pi,
ell(z)=-sum a_ne^-b_nz=zeta'(1/2+z)/zeta(1/2+z).
This equality uses only the absolutely convergent Euler log derivative in Re s>1, and the same digamma integral as dispersion2030. No evaluation of a divergent Euler series on Re z=0 is made. Beyond the initial half-plane q has its usual meromorphic continuation; that fact does not give an automatically bounded or passive realization of the history evolution on a larger domain.

## B. One-delay storage identity, with exact factors
For a single lag a>0, let y_a=u(t)-u(t-a), and
S_a(t)=int_0^a|u(t-s)|^2ds.
Then S_a'=|u(t)|^2-|u(t-a)|^2. Consequently
2Re(conj(u)y_a)=S_a'+|u(t)-u(t-a)|^2.
This is a genuine passive delay-line identity. Multiplying by k(a) or a_n and integrating/summing preserves it when the corresponding terms converge.
In spectral variables z,w with Re z,Re w>0, let d=z+conj w and E_a(z)=1-e^-az. The corresponding exact kernel identity is
[E_a(z)+conj E_a(w)]/d
 =int_0^a e^-zs e^-conj(w)s ds
  +E_a(z)conj E_a(w)/d.
The first term is the line-storage Gram kernel, the second is a positive dissipative kernel because 1/d=int_0^infty e^-zt e^-conj(w)t dt. check2033.py gives identically zero symbolic residual.
A negative prime transfer -a_n e^-b_nz alone is NOT passive: it is negative on the positive real axis. It may be rewritten as a_n(1-e^-b_nz)-a_n, but the second term is then a negative feedthrough that cannot be dropped.

## C. Boundary channels give exactly the old hyperbolic storage
Order the state vector x_boundary=(x_+,x_-), and put
A_boundary=diag(1/2,-1/2), B_boundary=(1,1)^T,
C_boundary=(1,1), P_boundary=[[0,1],[1,0]].
Directly A^*P+PA=0, PB=C^*. Thus
S_boundary=x_boundary^*P_boundary x_boundary=2Re(x_+ conj x_-),
S_boundary'=2Re(conj(u)(x_++x_-)).
It is lossless but indefinite. These matrix identities were checked symbolically in check2033.py. This is a real state-space occurrence of the boundary hyperbolic plane, not a proposed positive metric.
For v_boundary(z)=(1/(z-1/2),1/(z+1/2))^T,
[r(z)+conj r(w)]/d=v_boundary(w)^*P_boundary v_boundary(z).
This matches dispersion2030's pole kernel exactly.
If u is supported in [0,T],
x_+(T)=e^(T/2)C_-(u), x_-(T)=e^(-T/2)C_+(u),
so S_boundary(T)=2Re(C_-(u)conj C_+(u))=P(u).
For t>=T this cross storage remains constant, since the two autonomous exponents cancel. E0 inputs have both terminal states zero, not merely a zero cross-storage value.

## D. Finite-cutoff exact signed KYP identity
For B>0 retain all prime-power lags b_n<B, set M_B=-K0+2sum_(b_n<B)a_n, and define q_B and y_B by that finite sum. Rewriting the transfer gives
q_B=r+int k(a)(1-e^-az)da
 +sum_(b_n<B)a_n(1-e^-b_nz)-M_B/2.
This is the original operator's degree-minus-adjacency bookkeeping, not a modification of its weights.
Let
S_jump,B=int_0^infty k(a)S_a da+sum_(b_n<B)a_n S_b_n,
D_jump,B=int_0^infty k(a)|u(t)-u(t-a)|^2da
 +sum_(b_n<B)a_n|u(t)-u(t-b_n)|^2.
For smooth causal inputs these Gamma storage and dissipation integrals converge. In particular the Gamma storage is also the positive weighted history norm
S_Gamma=int_0^infty T(s)|u(t-s)|^2ds,
T(s)=int_s^infty k(a)da;
T(s) has a logarithmic singularity at zero and exponential decay at infinity, both integrable against these histories. Differentiation can be justified first with finite a limits and then dominated convergence. The exact identity is
2Re(conj(u)y_B)=(S_boundary+S_jump,B)' +D_jump,B-M_B|u|^2.

Elimination in spectral variables gives the complete kernel:
K_qB(z,w)=S_B(z,w)+[D_B^+(z,w)-M_B]/d,
S_B=v_boundary(w)^*P_boundary v_boundary(z)
 +int k(a)int_0^a e^-zs e^-conj(w)s ds da
 +sum_(b_n<B)a_n int_0^b_n e^-zs e^-conj(w)s ds,
D_B^+=int k(a)E_a(z)conj E_a(w)da
 +sum_(b_n<B)a_n E_b_n(z)conj E_b_n(w).
This is well-defined for Re z,Re w>1/2; in fact the delay terms need only positive real parts. S_B has an indefinite boundary block, and the dissipation numerator has a negative constant rank-one block. Therefore it is NOT a positive Gram representation even though its algebra is exact. The positive pieces and their obstructions are independently specified.

To recover W, integrate the supply over t>=0 for compact input. The jump storage tends to zero as t->infty (for the Gamma continuum this follows from the exponential kernel tail); initially it is zero. Boundary storage has limit P(u). Integrating each dissipation term gives the full zero-extension jump norm on R. Thus
int_0^infty 2Re(conj(u)y_B)dt
=P(u)+H_B(u)-M_B||u||^2.
For u supported on an interval of width A<=B, the correlations of every additional prime lag b>=A vanish. Such an added delay contributes 2a_n||u||^2 to H_B and the same amount to M_B||u||^2. Hence this integrated expression is exactly the fixed-window W_A, independent of increasing B beyond A. All zero-extension tail terms are retained. Polarization recovers the complete mixed pairing.
This proves consistency with operator2023's window compressions and dispersion2030's exponential-probe identity. The time-domain supply is not a new energy declared equal to W; the equality follows from the explicit response and line-storage algebra.

## E. What KYP positivity would require (not a finite-dimensional theorem applied to this system)
For reference, finite-dimensional state equations x'=Ax+Bu, y=Cx+Du and S=x^*Px give the purely algebraic identity
2Re(u^*y)-S'=[x;u]^*R_P[x;u],
R_P=[[-A^*P-PA, C^*-PB],[C-B^*P,D+D^*]].
If independently P>=0 and R_P>=0, the storage and supply are positive in the required sense. Factoring R_P=Z^*Z and writing v(z)=(zI-A)^-1B, one gets
[q(z)+conj q(w)]/d=v(w)^*P v(z)
 +[Z(v(w),1)]^*[Z(v(z),1)]/d.
This verifies the exact sign and factor of the dissipation term requested in the brief.
For our unbounded-input/output history system this is only a template: a Hilbert state domain, continuous/admissible input and observation maps, well-defined storage, compatible time evolution, and a valid limiting energy identity must be established. We have proved the concrete identity directly on a smooth classical core, not invoked a finite-dimensional KYP lemma to certify the infinite system. A storage obtained simply by encoding the unknown W or its Gram kernel is not an independent solution.

## F. Two substantive obstructions and the arithmetic pole cancellation
1. [EXACT] Every finite q_B has an uncancelled pole at z=1/2 with residue +1. Its Gamma term and finite delay sum are holomorphic there. Approaching that pole from its left inside Re z>0 makes the real part negative. Hence finite prime cutoffs cannot individually be unshifted positive-real/passive full-transfer systems. A passive approximation scheme cannot simply require each q_B to solve the unshifted problem. This is a concrete obstruction to that particular approach, not a claim that no other realization exists.

2. [EXACT] The displayed independent positive prime-line storage has no finite all-prime limit. If a causal history is nonzero, then for all lags b beyond the elapsed time, S_b(t)=int_0^t|u(r)|^2dr>0. Since sum a_n diverges, sum a_n S_b_n=+infty. The same large-lag diagonal divergence appears in D_jump and M_B|u|^2 and cancels only in their signed combination/output. Any renormalized finite storage obtained by subtracting it must have its sign proved separately. Infinite positive storage is not an acceptable KYP certificate for finite-energy excitations.
The divergence of sum a_n follows already from the elementary divergence of sum over primes 1/p, since log p/sqrt p>=1/p for large p; no RH estimate is used.

There is a useful independently derived transfer cancellation, paralleling sos2010:
Let E(x)=psi_Cheb(x)-x, s=1/2+z and k5(a)=e^-5a/2/(1-e^-2a).
The digamma recurrence gives g(z)=g5(z)-1/(z+1/2),
g5(z)=(1/2)digamma(5/4+z/2)-(1/2)log pi.
The smooth part of the prime measure contributes
-int_0^infty e^-(z-1/2)b db=-1/(z-1/2).
Therefore for Re z>1/2,
q(z)=g5(z)-int_[1,infty) x^-(z+1/2)dE(x).
This exactly cancels both rational boundary poles in the transfer expression. Equivalently
g5(z)=(K0+4)/2+int_0^infty k5(a)(1-e^-az)da.
The shifted constant is still negative and dE is signed. The cancellation isolates a much better target for a coupled realization but does not turn the remainder into a positive medium. Absolute convergence of the signed Stieltjes integral is guaranteed in the stated initial half-plane; extending a positive-state realization to Re z>0 is not supplied by the formal continuation of the formula.

## G. Shifted passive control versus the actual unshifted target
[THM, checked previously in Lagarias source] q has positive real part for Re z>1/2. Thus q_delta(z)=q(z+delta) is unconditionally positive-real for delta>=1/2 on Re z>0, and has an abstract Herglotz positive realization. Its kernel is
[q(z+delta)+conj q(w+delta)]/[z+conj w].
In original arguments zeta=z+delta, eta=w+delta this uses denominator zeta+conj eta-2delta, not the desired denominator zeta+conj eta. This is a legitimate discounted/shifted passive control, not the solution of full W.
In a hypothetical state realization the same shift replaces A by A-delta I. At fixed P the KYP residual gains +2delta P in its state-state block. Removing the shift loses that positive term. This explicitly explains why shifted passivity need not survive removing the discount. No claim that this particular unbounded realization already satisfies all such shift-domain hypotheses is made.

## H. Minimum-excitation and reactive-coefficient tests
A nonzero amplitude threshold is not forced by a linear homogeneous realization: u->epsilon u scales states and outputs linearly and every quadratic supply/storage by |epsilon|^2. A frequency threshold or a coercivity lower bound would be a separate quantitatively specified assertion, not implied by the phrase minimum excitation.
A genuine scalar reactive test is available at the analytic center. FE gives q(0)=0 and
q'(0)=xi''(1/2)/xi(1/2).
This coefficient is strictly positive WITHOUT RH. Here is an independent positive-integral proof, not a zero-location argument.

Let theta(t)=sum_(n in Z)e^-pi n^2t and A(u)=e^(u/2)[theta(e^(2u))-1] for u>=0. The Gaussian theta/Mellin formula and Poisson reflection (as already derived in polarity2021) give
xi(1/2+z)=1/2+(z^2-1/4)int_0^infty A(u)cosh(zu)du.
The theta functional equation gives A'(0)=-1/2. Twice integrating by parts, with its superexponential tail, yields
xi(1/2+z)=int_0^infty Phi(u)cosh(zu)du,
Phi=A''-A/4
=4sum_(n>=1)[2pi^2 n^4 e^(9u/2)-3pi n^2 e^(5u/2)]e^-pi n^2 e^(2u).
For u>=0 every summand is positive because 2pi n^2 e^(2u)>3. Thus
q'(0)=int u^2 Phi(u)du / int Phi(u)du>0.
The entire integral and differentiations converge locally uniformly in z. This constructs a positive moment ratio for the low-frequency slope; it does not construct a positive-real function on the whole right half-plane.
check2033.py evaluates xi''/xi at 60-digit working precision as
0.04620998623083794157786762086067802800676... [NUM].
The positivity proof is analytic, not numerical. Calling this an effective inductance/reactive coefficient is an analogy once the transfer convention is chosen. No physical mass or units have been identified, and it is not M_A, whose origin is the diagonal bookkeeping above.

[EXACT falsifier] q_test(z)=z+z^3 is real-symmetric, odd, entire, q_test(0)=0 and q_test'(0)=1>0. Yet q_test(1+2i)=-10, so it is not positive-real. This disproves sufficiency of the two low-frequency hypotheses, not any assertion about genuine Euler data.
The prior n=2 ghost gives a coefficient-sensitive stronger control: changing the prime-delay sample while leaving boundary/Gamma data unchanged yields negative full W on the fixed E0 trial function in polarity2021. A successful coupled-storage construction must detect this change, rather than proving passivity from only local slope or boundary parity. No new ghost numerics were needed.

## I. Completed result and next narrow target
Constructed an arithmetic transport-plus-boundary evolution whose transfer is exactly q in Re z>1/2; proved a signed storage/supply and mixed-kernel identity; recovered full W by elimination and window-compatible integration; isolated the uncancelled finite-cutoff pole and infinite independent-line storage as explicit obstructions; proved positivity of the genuine low-frequency reactive coefficient.
No independently positive full storage was obtained. The best next narrow test, if separately authorized, is to propose a finite positive cross-coupled storage for the pole-cancelled Gamma/Chebyshev-history representation in §F and verify its energy identity on the smooth causal core, including the n=2 delay coefficient. One must not merely set that storage equal to the unknown W Gram form. Work stops here.
Sources: all newly used energy identities are derived above; no infinite-dimensional KYP theorem is cited or applied. The checked Lagarias and passive-media sources from dispersion2030 remain background only. No additional external-source claims were introduced.

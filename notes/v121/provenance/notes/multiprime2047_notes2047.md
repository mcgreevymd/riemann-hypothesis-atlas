# t2047 — joint-shift finite-block/continuum-tail certificates at A=1 and A=1.1
Scratch only. [EXACT] analytical comparison and domain identities; [CERT] interval coefficients plus verified finite-matrix residual bounds and analytic complement; [NUM] unverified exploratory spectra or quadrature; [OPEN] extensions beyond the certified windows. No RH claim.
No Page/repo/manuscript/cloud/contact actions; no external-source facts needed beyond standard elementary interval Poincare/closed-form facts proved or specified below. No further research launched.

## Proposed chat answer (under 750 words)

**We reached both targets: width 1, and a window containing both prime shifts 2 and 3.** The proof uses a new finite-block/continuum-tail comparison, not an extrapolation of the earlier edge-strip estimate.

The certificates give, for the original energy on E₀,
\[
W(F)\ge0.004\|F\|^2\quad(A\le1),
\]
and
\[
\boxed{W(F)\ge0.0005\|F\|^2\quad(A\le1.1).}
\]
Since log3≈1.098612, the second result includes both exact coefficients log2/√2 and log3/√3. This does not claim positivity at A=2 or on all windows.

**1. A rigorous minorant of the logarithmic energy. [EXACT]**
Expand the Gamma symbol into its positive rational terms and retain finitely many. The omitted terms are nonnegative on the entire continuum. The retained operator is an identity minus an explicit sum of exponential integral kernels, together with the exact prime translations.

I add a fixed positive penalty for the two exponential moments. It vanishes identically on E₀, so the target there is unchanged. This allows both constraints to participate in a finite-block positivity test without pretending that a compressed trial eigenvalue is a lower bound.

**2. Preserve the prime translations exactly. [EXACT]**
The interval is partitioned into cells whose translations by log2—and, at width 1.1, log3—match other cells exactly. The cell-constant subspace and its orthogonal complement are therefore both invariant under the prime operator. No prime cross-coupling into an uncontrolled tail is discarded.

For two primes, the overlapping strips organize into explicit four-vertex chains with weights log2/√2, log3/√3, log2/√2, plus ordinary paired strips. This is where the actual arithmetic coefficients enter jointly.

**3. Control the infinite complement, not just the matrix. [EXACT/CERT]**
Mean-zero functions on each cell have a small antiderivative. Ordinary cell Poincare therefore bounds the *smoothing exponential kernels* on the complement; it is not incorrectly imposed on the logarithmic Gamma energy itself.

At width 1.1 a scalar tail estimate was still too weak. I replaced it by a matrix-valued bound involving the exact Gram matrix of derivatives of those smoothing kernels. This retains the coupling’s direction, rather than charging every low mode the worst possible tail cost.

A Schur-complement inequality then certifies the full infinite-dimensional form. At A=1.1 the verified effective finite-block lower bound exceeds 0.0006638; the continuum high block exceeds 3.2078. Together they establish the stated 0.0005 bound.

The numerical eigensolver is used only to produce a candidate diagonalization. Its residual and orthogonality errors are checked, kernel coefficients are interval-enclosed, and omitted continuum contributions have analytical bounds. Thus these are computer-assisted continuum lower certificates, not positive Ritz values. The rounding checks use the usual double-precision dot-product error model explicitly documented in the proof.

**Scope and control.** The exact diagonal K₀, both moments, zero extension and all active prime weights remain intact. Smaller windows inherit the bounds by complete-W compression consistency. The dropped-n=2 ghost still has the previously observed large negative trial energy at A=2; nothing here falsely certifies that window. Passing on our smaller windows would not establish universal non-blindness.

**What changed:** wider overlap and two interacting prime shifts are now handled by an explicit arithmetic graph plus a rigorously bounded continuum remainder. The next obstruction is no longer the failed one-strip estimate. Larger windows introduce additional shift graph structure and require new certificates; no global sign theorem has been assumed or obtained.

## A. The original form and a finite positive Gamma minorant
Use I_A=[-A/2,A/2], zero extension E, T_bF(u)=F(u-b), inner product linear in its first argument. Set
Q_A(F)=K0||F||^2+J_infty(F)-2sum_(log n<A)a_n Re<F,T_log nF>,
a_n=Lambda(n)/sqrt(n), K0=digamma(1/4)-log pi,
J_infty=int_0^infty k(a)||EF-T_aEF||^2da.
On E0, W=Q_A; in jump form W=H_A-M_A||F||^2, with the original M_A=-K0+2sum a_n. Nothing is refitted.
The exact Gamma expansion is
K(t)=K0+sum_(j>=0)2t^2/[c_j(c_j^2+t^2)], c_j=2j+1/2.
For N positive terms define the whole-line convolution operator
(C_N f)(x)=int_R sum_(j=0)^(N-1)e^-c_j|x-y| f(y)dy,
d_N=K0+sum_(j<N)2/c_j,
S_A=sum_(log n<A)a_n E^*(T_log n+T_-log n)E.
Because the Fourier multiplier of e^-c|x| is 2c/(c^2+t^2), monotone positivity of the omitted Gamma terms gives the form inequality
Q_A >= d_N I-E^*C_NE-S_A.
This holds on the full zero-extension energy domain. The right side is bounded; no approximation-error guess for the discarded positive terms is required.

Let R:R^2->L2(I_A) have columns r_+=e^(u/2), r_-=e^(-u/2), and define
A_N,kappa=d_N I-E^*C_NE-S_A+kappa RR^*, kappa>0.
For F in E0, R^*F=0, hence
W(F)>=<A_N,kappa F,F>.
The moment penalty is a proof device on the unconstrained space, not a change to W on its target domain. It uses both constraints simultaneously. We choose the fixed values kappa=2 at A=1 and kappa=4 at A=1.1, not a redefinition of the arithmetic energy.

## B. Exact prime-invariant partitions
Let P be orthogonal projection onto normalized cell indicators phi_i=1_Ii/sqrt(h_i), Q=I-P. If the active translated cells match exactly or leave I, S_A commutes with P. This is essential: an arbitrary uniform grid would not justify deleting PSQ.

### Width A=1, one prime
Let b=log2, delta=1-b and middle=2b-1. Divide the left strip [-1/2,-1/2+delta] into 250 equal cells, and its translated right strip into the same 250 cells. Divide the middle strip into 315 equal cells. Total dimension 815. T_b pairs each left/right indicator and vanishes elsewhere, so S has paired 2x2 blocks with off-diagonal a_2=log2/sqrt2. Thus ||S||=a_2 and PSQ=0 exactly.

### Width A=11/10, two primes
Use coordinate x in [0,A]. Let b=log2, c=log3, epsilon=A-c, d=c-b, L=A-b. Here 0<epsilon<d and L<b. The seven segments are
[0,epsilon], [epsilon,d], [d,L], [L,b],
[b,b+epsilon], [b+epsilon,c], [c,A].
Use cell counts [3,674,3,478,3,674,3], total 1838. Corresponding length-epsilon segments receive identical subdivisions, as do the two length-(d-epsilon) segments.
The b-shift links segments (0,4), (1,5), (2,6); the c-shift links (0,6), in zero-based indexing. All links match cells exactly. The nontrivial joint components on the small strips are four-vertex paths with edge weights a_2,a_3,a_2; the middle paired strips have weight a_2. Therefore
||S||=s_*=(a_3+sqrt(a_3^2+4a_2^2))/2,
a_3=log3/sqrt3.
This follows by diagonalizing the symmetric four-vertex weighted path (even/odd reflection sectors). s_*≈0.9009276163. No n=4 atom is active because A<log4. Neither coefficient has been replaced by a norm bound independent of the other.
Both QL2 and PL2 are invariant under S, including its action on mean-zero cell fluctuations, since each link is an exact measure-preserving translation with equal cell lengths.

## C. Analytic control of the infinite high block
Set h=max_i h_i, s_N=sum_(j<N)2/c_j, t_N=sum_(j<N)c_j, and r_A=||r_+||^2+||r_-||^2=4sinh(A/2).
The kernel C_N is positive, with whole-line norm <=s_N. For f in QL2, each cell mean vanishes. Its primitive G can be chosen zero at both ends of every cell, giving
||G||^2<=(h/pi)^2||f||^2, G'=Ef.
Since the Fourier multiplier of C_N is bounded by 2t_N/t^2 for t!=0,
<QE^*C_NEQ f,f><=epsilon_C||f||^2,
epsilon_C=2t_N(h/pi)^2.
This uses ordinary cell Dirichlet Poincare on a primitive, NOT an invalid bound of the logarithmic energy below by an ordinary derivative energy.
For the two moment vectors, cell Poincare gives
||QR||^2<=epsilon_R=(h/(2pi))^2 r_A.
The high block therefore satisfies
QA_N,kappa Q >= h_* Q,
h_*=d_N-||S||-epsilon_C,
because the moment penalty is nonnegative and can be omitted in this high lower bound.

A simple mixed-block bound is
||QA_N,kappa P||<=sqrt(s_N epsilon_C)+kappa sqrt(r_A epsilon_R)=B_*.
It follows from positivity of C_N (block Cauchy–Schwarz) and the rank-two moment operator. Thus a finite lower bound lambda_L for PA_N,kappa P gives the sufficient scalar Schur condition
lambda_L-c-B_*^2/(h_*-c)>=0, h_*>c.
At A=1 this already succeeds. At A=1.1 it does not, even though the better directional test below does succeed. This is the new-method comparison rather than a scan of the old edge estimate.

## D. Matrix-valued mixed-block control for two primes
For f in PL2, cell mean-zero projection applied to C_N Ef gives
||Q E^*C_N E f||^2<=(h/pi)^2||(C_N Ef)'||^2_R.
Define the finite PSD derivative Gram matrix
D_ij=<(C_N E phi_i)',(C_N E phi_j)'>_(R).
Then the mixed-block operator satisfies
(PA_N,kappa Q)(QA_N,kappa P)
<=2(h/pi)^2 D+2kappa^2 epsilon_R R_L R_L^*,
where R_L=P R is its cell-coordinate matrix. This follows from ||x+y||^2<=2||x||^2+2||y||^2 and the bound on QR. No finite Ritz interpretation is needed.
Consequently it suffices to verify
A_LL-alpha D-beta R_L R_L^*>=c I,
alpha>=2(h/pi)^2/(h_*-c),
beta>=2kappa^2 epsilon_R/(h_*-c), h_*>c.
Because D and R_LR_L^* are PSD, larger rational alpha,beta give a valid more conservative test. This retains the directional tail cost rather than charging every low vector ||C_N||.

## E. Exact finite matrices and derivative Gram formula
For disjoint cells i<j with endpoints l_i,r_i and widths h_i, put
q_i(c)=(1-e^-c h_i)/(c sqrt(h_i)).
The exact cell matrix for the exponential kernel C_c is
(C_c)_ij=q_i(c)q_j(c)e^(c r_i-c l_j),
(C_c)_ii=2/c-2(1-e^-c h_i)/(c^2 h_i).
The opposite triangle is its transpose. Moment columns are
(R_L)_i,sign=e^(sign l_i/2)(e^(sign h_i/2)-1)/[(sign/2)sqrt(h_i)].
All formulas in the code refer to exact logarithmic partition endpoints, interval-enclosed before comparison with their floating representations.

For D, the whole-line Fourier multiplier is
Dhat(t)=t^2[sum_(j<N)2c_j/(c_j^2+t^2)]^2>=0.
Partial fractions give the exact physical-space kernel
sum_j [alpha_j e^-c_j|x|-c_j^2|x|e^-c_j|x|],
alpha_j=c_j+4c_j^2 sum_(i!=j)c_i/(c_j^2-c_i^2).
Therefore the exact finite derivative Gram matrix is
D=sum_j[alpha_j C_cj+c_j^2 partial_c C_c|_(c=c_j)].
For i<j,
partial_c(C_c)_ij=(C_c)_ij[ell_i(c)+ell_j(c)+r_i-l_j],
ell_i(c)=h_i/(e^(c h_i)-1)-1/c.
For the diagonal,
partial_c(C_c)_ii=-2/c^2+4(1-e^-c h_i)/(c^3 h_i)-2e^-c h_i/c^2.
These signed formulas are only used to COMPUTE a matrix whose PSD meaning is established independently by the derivative Gram identity. Cancellation in their numerical construction is explicitly bounded below; no assumption of positivity of the rounded D is used.

## F. Verified finite-matrix calculations: what is, and is not, trusted
The scripts use mpmath.iv at 55 digits for scalar constants, endpoints, exponential factors, moment integrals, diagonal coefficients and derivative coefficients. K0 is enclosed by its exact formula
K0=-gamma-pi/2-3log2-log pi,
with gamma between H_1000-log1000-1/2000 and that expression plus 1/(12*1000^2).
The finite matrix itself is evaluated in double precision. Its eigenvectors/eigenvalues are NOT accepted as a theorem by themselves.

For an approximate eigendecomposition (Q,Lambda) of a real matrix M, compute
G=Q^T Q-I, R=M Q-Q Lambda.
Explicit double-precision dot-product error bounds produce upper bounds eta>=||G||_2 and rho>=||R||_2, using Frobenius norms as overestimates. Under eta<1 and positive numerator, the Rayleigh identity on x=Qv proves
lambda_min(M)>=[lambda_min(Lambda)-eta||Lambda||-sqrt(1+eta)rho]/(1+eta).
A separately proved operator-norm enclosure delta_M for matrix construction is then subtracted. This converts a numerical diagonalization into a checked LOWER bound for the EXACT finite matrix, rather than a trial-space upper bound for the continuum operator.

Rounding model: ordinary IEEE-754 double precision, no overflow/underflow, with the standard dot-product forward bound gamma_n=n u/(1-n u), u=2^-53; scalar coefficient validation does not assume NumPy exp is correctly rounded because its resulting factors are independently interval-compared. Frobenius evaluation allowances are inflated by 1+10^-7 (well above the accumulated dimension-squared roundoff here), with extra absolute slack. Residual multiplication and subtraction errors are explicitly included. This is a standard verified-numerical certificate under that arithmetic model, not a theorem-prover/machine-instruction formal verification. The proof and checks are reproducible; an independent audit should retain these stated assumptions.

### Construction enclosures
For C_c off-diagonal factors the code verifies relative error <10^-9 for each factor, implying relative entry error <3*10^-9 after multiplication and accumulation slack. Since the exact C_c matrices have nonnegative entries and norm <=2/c, an entrywise relative majorant bounds its operator error without multiplying by the matrix dimension. Diagonal errors are bounded separately by 10^-10 per Gamma term. Moment columns similarly have relative error <10^-9; their positive rank-two Gram errors are bounded using kappa r_A. Diagonal d_N is enclosed within 10^-7, shift weights within 10^-12, and final assembly roundoff is overestimated. The resulting analytic construction norm bound is below 10^-6; that coarser value is used.
For D the derivative log factors are enclosed within 10^-9 and diagonal derivative errors within 10^-8. The pointwise exact off-diagonal log derivative is bounded in absolute value by A+2/c. These bounds imply
err(C_c)<=3*10^-9*(2/c)+10^-10,
err(C'_c)<=[3*10^-9*(A+2/c)+5*10^-9]*(2/c)+10^-8.
The alpha_j coefficient errors are bounded by 10^-6. Summing the weighted norm bounds and a generous floating assembly allowance yields err(D)<0.097 in the two-prime run; the proof deliberately uses the much larger bound 100. Even this large allowance affects the effective matrix by only alpha*100=2.5*10^-6. This controls cancellations rather than declaring the derivative matrix accurate by inspection.

## G. Results and reproducible certificate outputs
### G1. Width one
N=48, kappa=2, 815 cells. certify2047.py verifies
exact finite A_LL eigenvalue >0.00699625 (use the weaker rational 0.0069),
h_*>2.2304423,
B_*<0.07587108.
For c=1/250=0.004, the exact interval scalar Schur margin is >0.00031452. Thus
A_N,kappa>=0.004 I on L2(I_1),
and W>=0.004||F||^2 on E0.
This already improves the old .694 certificate to A=1 without optimizing narrow overlap strips.

### G2. Width 11/10 with both primes
N=192, kappa=4, 1838 cells, h<0.000599522.
Choose rational Schur coefficients
alpha=1/40000000=2.5*10^-8,
beta=1/4000000=2.5*10^-7,
and c=1/2000=0.0005.
certify_two2047.py verifies
h_*>3.2078580,
needed alpha<2.270870*10^-8,
needed beta<2.100651*10^-7.
The approximate effective finite eigenvalue is 0.000667444379345; after construction error, orthogonality defect and eigen-residual allowances the EXACT effective matrix lower bound exceeds 0.0006638402. This is larger than c.
Therefore the full infinite-dimensional Schur comparison gives
W(F)>=0.0005||F||^2 for F in E0 supported in width 11/10.
No claim is based solely on the finite eigenvalue. The scalar mixed-tail bound at this same resolution was NEGATIVE (~-.0073); the derivative Gram directional correction is what makes the proof succeed.

Smaller centered intervals embed by zero extension preserving both moments and complete W: additional prime correlations outside their support vanish and their jump/diagonal additions cancel. Translated intervals have the same form by common translation (C_± scale reciprocally). Thus the results hold for every width A<=1 and A<=1.1 respectively. At A=1.1 the threshold remains M_A=-K0+2a_2+2a_3; the theorem proves H_A>=(M_A+0.0005)||F||^2, not that M_A is the sharp lowest energy.
No compact-resolvent/ground-state theorem for W was assumed or needed. The infinite complement is explicitly retained. Its high lower bound is a bound for a finite positive Gamma MINORANT plus bounded terms, not an assertion about a global all-prime essential spectrum.

## H. Arithmetic/fake sensitivity and scope
Both shifts and weights enter the invariant graph, S norm, finite matrix and high Schur constants. Deleting n=2 changes the graph and the exact low matrix; the certificate is not a phase-only or moment-only construction. Nevertheless finite-window positivity can hold for a fake too, so passing on these windows would not prove universal non-blindness.
ghost2047.py recomputes the explicit E0 control at A=2:
G=(1-u^2)^4, F=G''-G/4 on [-1,1]. The moments vanish exactly, and fixed-trial quadrature yields
W_original/N≈+0.0023337532023,
W_drop2/N≈-0.6392279387151.
These values are non-interval quadratures, not the lower certificates. The positive original trial value proves no continuum sign. The large negative ghost is a useful control outside the certified range, and nothing in our theorem extends falsely to it. No alternative ghost Euler/FE admissibility is asserted.

The approach is finite arithmetic-kernel comparison with a verified continuum remainder. It has not proved all-window positivity, full unconstrained W positivity, RH, a canonical geometric class map or a global positive response realization. The next larger windows require further prime-orbit structure and adequate finite/tail bounds; no untested endpoint or global extrapolation is claimed. Work stops here.

## Artifacts
- certify2047.py / certify2047.json: width-one certificate; all assertions passed after enlarging rounding allowances.
- certify_two2047.py / certify_two2047.json: two-prime certificate; all assertions passed, about 87 seconds on this box.
- experiment2047.py/.json: first scalar-tail tests.
- twoprime_experiment2047.py/.json: scalar-tail failure beyond log3.
- twoprime_derivative2047.py/.json: successful directional-tail exploratory comparison, superseded by the verified certificate.
- ghost2047.py/.json: explicit fixed-trial coefficient control.
Run verified scripts with OPENBLAS_NUM_THREADS=1 python3 <script>. The thread limit is for reproducibility/performance; the stated residual rounding model is included rather than assuming an eigensolver theorem.

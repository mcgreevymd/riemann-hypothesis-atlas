# t2024 — Poincare/Wirtinger at infinity: exact coordinate model and a proved small-window bound
Scratch only. [EXACT] identities and elementary proofs; [THM] standard facts explicitly stated; [NUM] uncertified evaluations; [ANALOGY] structural reading; [OPEN] missing all-window inequality. No RH claim, Page/repository/manuscript/cloud/contact actions. No web sources used.

## Proposed chat answer (under 650 words)

**Yes—this is a promising formulation, and we can prove a genuine piece of it.** There is not one uniquely specified theorem called “Poincare/Wirtinger at infinity,” but two precise interpretations fit your idea.

**1. Our target already is an arithmetic Poincare inequality. [EXACT]**
On the two-moment-zero sector E₀, the pole term vanishes, so
\[
W(F)=H_A(F)-M_A\|F\|^2.
\]
Thus the desired statement is that the least constrained jump-energy quotient is at least the exact arithmetic threshold M_A, for every window. The constraints replace ordinary “mean zero,” and H_A is a nonlocal arithmetic analogue of the Dirichlet energy. No positive uniform gap above zero for W is required.

**2. A concrete Poincare comparison actually works on small windows. [EXACT]**
Zero extension is important: sufficiently long jumps leave the interval and force energy. Define
\[
T(a)=\int_a^\infty k_\infty(b)\,db
=\operatorname{artanh}(e^{-a/2})+\arctan(e^{-a/2}).
\]
Jumps of length at least A contribute twice the squared norm. Jumps between A/2 and A form chains of at most two points and contribute at least the squared norm. Hence
\[
H_A(F)\ge [T(A)+T(A/2)]\|F\|^2.
\]
For \(0<A\le1/10\), no prime jump occurs and \(M_A=-K_0\). This proves
\[
W(F)\ge c_*\|F\|^2\quad(F\in E_0),
\qquad
c_*=\log\frac{5\sqrt2}{\pi}-\gamma-\frac3{80}>0.
\]
The constant is about 0.1966. This is an independent, analytic small-window certificate—not a positive Ritz value or an assumption of the desired sign.

**3. Your “infinity” coordinate has an exact weighted interpretation. [EXACT]**
Set \(r=e^{-u}\) and make the change unitary:
\[
f(r)=r^{-1/2}F(-\log r).
\]
Translations become unitary dilations,
\(f(r)\mapsto e^{a/2}f(e^ar)\), and the two constraints become
\[
\int f(r)\,dr=0,\qquad\int f(r)\frac{dr}{r}=0.
\]
So one familiar mean-zero condition really appears, accompanied by a second weighted one. The relevant jump energy remains a dilation energy, not the usual derivative energy on a circle.

There is another striking match: under this same transformation our differential parametrizer \(D^2-1/4\) becomes
\[
g\longmapsto (r^2g')'.
\]
Its Hardy inequality is \(\int r^2|g'|^2\ge\tfrac14\int|g|^2\). Thus the boundary coordinate, weighted differentiation and the constant 1/4 genuinely fit together. But this parametrizer is not itself the full prime/Gamma energy operator.

**4. What remains at larger windows. [OPEN]**
The small-window bound loses strength as A grows. Stronger arithmetic chain comparisons are available, but the elementary ones do not reach M_A on the tested larger windows. The two moment constraints and exact prime weights must supply more than boundary escape alone.

Ordinary Wirtinger cannot simply be substituted: our Gamma multiplier grows like log-frequency, not frequency squared. Nor does a coordinate compactification remove negative directions. The earlier drop-n=2 ghost retains the same boundary constraints but has negative energy, so a successful theorem must detect the actual arithmetic coefficients.

**The constructive direction is therefore a sharp, two-constraint, dilation/nonlocal Poincare inequality with the exact arithmetic threshold—not merely smoothness at infinity.** We have proved its small-window version; its all-window arithmetic mechanism remains to be constructed.

## Proofs and exact comparisons

### A. Form domain and precise target
Use the closed zero-extension form domain from operator2023/notes2023.md. I is an interval of width A, E is zero extension, T_bF(u)=F(u-b), and
H_A(F)=int_0^infty k(b)||EF-T_bEF||^2db
 +sum_(log n<A) a_n||EF-T_(log n)EF||^2,
k(b)=e^-b/2/(1-e^-2b), a_n=Lambda(n)/sqrt(n),
M_A=-K0+2sum_(log n<A)a_n, K0=digamma(1/4)-log pi.
On E0=ker C_+ cap ker C_-, W=H_A-M_A||F||^2.
The exact constrained constant is lambda_0(A)=inf_(F in V_I cap E0, ||F||=1)H_A(F). The target is lambda_0(A)>=M_A for every A. This formulation requires no attainment of the infimum and no compact-resolvent claim. A lower bound proved on all F is sufficient but may lose the essential moment improvement. Positive upper Ritz estimates do not establish this inequality.

### B. A finite-shift chain lemma [EXACT]
For b>0 and any zero-extended interval-supported L2 function, split R into residue classes u=s+jb, with s in a length-b fundamental interval. The squared translation difference decomposes as the integral over s of the discrete energy sum_j|f_j-f_(j-1)|^2. Almost every chain has at most N=ceil(A/b) consecutive potentially nonzero entries; the exterior entries are zero.
For a chain of length n, this energy is the Dirichlet tridiagonal form with diagonal 2 and off-diagonal -1. Its exact smallest eigenvalue is
lambda_n=2-2cos(pi/(n+1)).
Since lambda_n decreases with n,
||EF-T_bEF||^2>=lambda_ceil(A/b)||F||^2.
If A/b is an integer, exceptional endpoint chains have measure zero, so the same N is valid. In particular b>=A gives lambda_1=2, and A/2<=b<A gives lambda_2=1. These statements hold for complex functions too.
All positive prime jumps can be retained in the comparison:
H_A(F)>= [int_0^infty k(b)lambda_ceil(A/b)db
 +sum_(log n<A)a_n lambda_ceil(A/log n)]||F||^2.
This is an independent ordinary discrete-Poincare comparison integrated over jump lengths. It ignores C_±, so it need not be sharp on E0.

### C. Closed-form two-scale certificate [EXACT]
Using only b>=A/2 from the previous lemma gives
H_A(F)>= [int_(A/2)^A k(b)db+2int_A^infty k(b)db]||F||^2
 =[T(A/2)+T(A)]||F||^2.
No contributions from b<A/2 are subtracted; they are nonnegative and simply omitted. All prime energies are also nonnegative.
Substituting t=e^-b/2 gives
T(a)=2int_0^(e^-a/2)dt/(1-t^4)
=artanh(e^-a/2)+arctan(e^-a/2).
For a>0,
artanh(e^-a/2)=(1/2)log coth(a/4)>(1/2)log(4/a),
arctan(e^-a/2)=pi/4-arctan(tanh(a/4))>=pi/4-a/4.
Therefore
T(A)+T(A/2)>log(4sqrt(2)/A)+pi/2-3A/8.
For 0<A<=1/10 the tail sum is at least its value at 1/10 and there are no prime jumps because A<log2. Use the exact digamma value
-K0=gamma+pi/2+3log2+log pi.
Subtracting this from the displayed bound at A=1/10 yields
c_*=log(5sqrt(2)/pi)-gamma-3/80.
It is strictly positive without reliance on floating-point certification: 5sqrt(2)/pi>2, log2>2/3, gamma<3/5 imply
c_*>2/3-3/5-3/80=7/240>0.
Here gamma<3/5 is an elementary bound on Euler's constant, for example obtained from gamma<H_100-log100<3/5. The other elementary numerical inequalities can be replaced by their familiar rational bounds (sqrt2>7/5 and pi<22/7 already imply the first). Consequently the theorem W(F)>=c_*||F||^2 on E0 for all widths 0<A<=1/10 is rigorous. The decimal c_*≈0.19656595 is illustrative; the analytic positive lower bound proves the sign.
The result is genuinely local: this range contains no prime-power atom. It establishes the boundary/Gamma portion of the proposed mechanism, not new control of the arithmetic prime regime.

### D. Stronger chain bound and its numerical calibration [NUM, exact formulas]
Set lambda_n=2-2cos(pi/(n+1)). The complete Gamma chain coefficient is the positive convergent series
B_chain,Gamma(A)=2T(A)+sum_(n>=2)lambda_n[T(A/n)-T(A/(n-1))].
A finite sum through n=N is a rigorous symbolic lower expression; our decimal evaluations are not interval-certified. The omitted series can be bounded above by
(pi^2/2)exp(3A/(2N))[N^-3+(2N^2)^-1],
using k(b)<=exp(3b/2)/(2b), lambda_n<=pi^2/n^2, log(n/(n-1))<=1/(n-1), and sum_(m>=N)m^-3<=N^-3+1/(2N^2).
For N=1000 and A<=3 this is below about 2.49e-6. Numerical rows (Gamma plus actual prime chain constants versus exact threshold):
A=.1: chain coefficient 5.8447094; M=5.3721834.
A=.25: 4.8789576 versus 5.3721834.
A=1: 3.7528147 versus 6.3524416.
A=2: 5.0527673 versus 11.2246518.
A=3: 7.5102116 versus 18.3878374.
Thus this particular moment-blind chain comparison does not reach the desired threshold at those larger examples. This is not a counterexample to W>=0 or to stronger nonlocal/weighted Poincare methods. In fact dropping the two constraints can admit negative Q=H-M, so a general all-functions lower bound cannot simply be expected to solve the constrained problem.
The arithmetic prime list for these rows includes every p^m<e^A (through 19 at A=3). No weights were changed. check2024.py and check2024.json record the computations.

### E. Exact compactification/dilation map and Hardy constant [EXACT]
For the centered interval I_A, r=e^-u maps it onto J_A=[e^-A/2,e^A/2]. Define U:L2(R,du)->L2((0,infty),dr) by
(UF)(r)=r^-1/2 F(-log r).
Then ||UF||_(dr)=||F||_(du); F(u)=r^1/2 f(r). The zero extension outside I_A becomes zero extension outside J_A in (0,infty).
Translations become the unitary dilation group
V_b f(r)=e^(b/2)f(e^b r), U T_b U^-1=V_b.
All jump norms are exactly preserved:
||F-T_bF||^2=int_0^infty |f(r)-e^(b/2)f(e^b r)|^2dr.
The constraints are precisely
C_-(F)=int_(J_A) f(r)dr,
C_+(F)=int_(J_A) f(r)dr/r.
The mass remains M_A||f||^2; it is not rescaled away. The transformed moment vectors are 1 and 1/r on J_A. Thus ordinary mean zero is one of the two conditions, but the energy is a dilation jump form, not an unweighted circle or interval derivative form. As A grows, the two ends tend to r=0 and r=infty respectively; treating only one misses part of the problem.

For the separate parametrization operator Dcal=partial_u^2-1/4,
U partial_u U^-1=-r partial_r-1/2,
U Dcal U^-1=r^2 partial_r^2+2r partial_r=partial_r(r^2 partial_r).
The two transformed adjoint zero modes are 1 and 1/r; this agrees with the two moment conditions. If G and G' vanish at finite interval endpoints, the transformed g=UG has g=g'=0 at both endpoints, so no extension delta terms occur.
For compact smooth g in (0,infty),
int r^2|g'|^2dr-(1/4)int|g|^2dr
=int |rg'+g/2|^2dr>=0.
This is the exact Hardy/Mellin threshold 1/4, corresponding to ||G'||^2 on the u side. Its constant is sharp on the full half-line: broad u-space cutoffs make ||G'||^2/||G||^2 tend to zero. This observation concerns the differential parametrizer, not a factorization of W. Applying it does not eliminate either K0, the prime coefficients or the signed remainder in W.

### F. Why classical Wirtinger and 'at infinity' need additional matching
Classical circle Wirtinger bounds a derivative energy on mean-zero functions. Even though the unitary r-chart exposes one ordinary mean, it does not identify our dilation energy with that derivative energy or preserve it without weights.
For a fixed smooth compact bump chi inside I, modulated tests F_n=chi(u)e^(inu) have derivative quotient asymptotic to n^2, whereas their Gamma jump quotient is asymptotic to log n. The finitely many prime jumps have uniformly bounded quotient for fixed A. Correcting the two moments using fixed compact bumps has rapidly decaying coefficients, so the same high-frequency comparison persists within E0. Consequently there is no inequality q_Gamma>=c||F'||^2 with a fixed c>0 on all these tests. This rules out that particular route from ordinary derivative Wirtinger, not all uncertainty estimates, nonlocal Poincare inequalities or weighted Hardy comparisons.

An 'inequality at infinity' can also mean coercivity outside compact sets or a statement about essential spectrum. Such a theorem concerns a specified global operator. Our fixed-window operators and their weak compression compatibility are constructed; an all-prime whole-line semibounded closed realization is not supplied merely by the compact-test distribution. Do not invoke Persson or an essential-spectrum threshold without those hypotheses. Even for a known global operator, exterior positivity alone need not exclude negative eigenstates in a compact region.

The PNT benchmark M_A~4exp(A/2) follows from the ordinary PNT by partial summation [THM, not an RH input]; no PNT estimate is used in the small-window proof. Large mass is balanced by the actual jumps, so it cannot be discarded as a coordinate divergence. The exact identity from sos2010 remains
W(F)=(K0+4)||F||^2+J5(F)-2int_[1,e^A]x^-1/2 <F,T_logxF>d(psi_Cheb(x)-x).
The shifted constant K0+4 is negative and the remainder is signed. Infinity regularity alone changes neither fact.

### G. Falsifier and completed scope
Use polarity2021's checked ghost: G=(1-u^2)^4 on [-1,1], F=Dcal G. Both moments vanish exactly. Removing only the n=2 atom, preserving the same boundary and Gamma kernel, gives Wghost(F)/||F||^2≈-0.63922794 (uncertified quadrature with a large negative margin). This is not admissible alternative Euler data or a claim that the fake satisfies a global FE. It falsifies any proposed universal boundary-only positivity mechanism indifferent to those prime coefficients.
A genuine all-window mechanism must use actual arithmetic coefficients and the two constraints, or provide an independent positive representation matching them. The present proved advance is the elementary small-window certificate plus the exact dilation/Hardy identification. No all-window sign theorem was obtained, and no additional work has been launched.

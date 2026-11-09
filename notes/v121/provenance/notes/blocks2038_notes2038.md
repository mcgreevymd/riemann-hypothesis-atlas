# t2038 — actual arithmetic block-positivity tests
Scratch only. [EXACT] formulas/elementary proofs; [CONSTRUCTED] independently specified arithmetic blocks; [PSD] a proved static block property; [SIGNED] identity without sign; [NUM] uncertified scalar matrix evaluation; [OPEN] missing nonlocal coupled storage. No RH claim.
Context: realization2033/notes2033.md, dispersion2030/notes2030.md, polarity2021/notes2021.md. No Page/repository/manuscript/cloud/external contacts. No further work launched.

## Proposed chat answer (under 750 words)

**I constructed and tested explicit arithmetic blocks. The result is informative: one natural coupling is positive but changes the energy; the coupling that preserves the exact signed storage fails positivity in a specific prime gap.** This is covariance-style block algebra, not an appeal to quantum positivity.

Use history coordinate s≥0 and a prime cutoff B. Define three independently specified weights:
\[
g(s)=\int_s^\infty k_5(a)da,\quad
p_B(s)=\sum_{s\le\log n<B}\frac{\Lambda(n)}{\sqrt n},\quad
d_B(s)=\int_s^B e^{a/2}da
\]
(the last is zero for s≥B). These are respectively the Gamma₅, prime-tail and smooth-prime-density histories. They come directly from the pole-cancelled response, not from an assumed sign of W.

**Test 1: fixed Gamma block plus prime block. [EXACT]**
Take
\[
\begin{pmatrix}g&-\sqrt{gp_B}\\-\sqrt{gp_B}&p_B\end{pmatrix}.
\]
It passes: its quadratic form is \(|\sqrt g f-\sqrt{p_B}h|^2\). But both branches carry the same physical history, so their storage is \(\int(\sqrt g-\sqrt{p_B})^2|f|^2ds\). This diverges as all prime delays are included.

More strongly, **no positive cross block with these fixed diagonal energies can remove that divergence**. Block positivity bounds its cross term by \(\sqrt{G P_B}\), leaving storage at least \((\sqrt{P_B}-\sqrt G)^2\). Here G is finite and P_B diverges. This rules out that fixed-Gamma assembly, not every possible coupled arithmetic realization.

**Test 2: preserve the actual prime-density cancellation. [EXACT]**
Set \(a_B=g+p_B\) and use the fully specified block
\[
\mathcal B_B(s)=
\begin{pmatrix}a_B&-d_B\\-d_B&d_B\end{pmatrix}.
\]
On the shared history its storage is exactly \((a_B-d_B)|f|^2\), the signed storage derived from the complete pole-cancelled response. Schur’s test gives
\[
\mathcal B_B\ge0\quad\Longleftrightarrow\quad a_B\ge d_B
\]
where d_B>0.

It fails concretely. At B=2 and s=1.96, no prime-power lag remains between s and B. We obtain
\[
g\approx0.003012,\quad p_B=0,\quad d_B\approx0.107651.
\]
The determinant is about −0.011265. An elementary analytic bound proves the negative sign; it is not a questionable tiny eigenvalue. Continuity gives a whole interval of negative history directions.

Replacing the cross term by \(-\sqrt{a_Bd_B}\) makes the block positive, but changes the shared storage to \((\sqrt{a_B}-\sqrt{d_B})^2\). It no longer has the original energy identity unless an additional, separately checked dissipation correction is supplied. Thus positivity cannot be obtained merely by clipping the cross coupling.

**Coefficient sensitivity. [NUM]** At B=2,s=0.5, the exact-match block passes locally: a_B−d_B≈+0.204116. Deleting only the n=2 atom changes this to −0.286014. So this matching block detects actual prime coefficients; the automatically positive square block is blind as a positivity certificate. The existing full-W ghost test also remains negative on its explicit E₀ input.

**What this establishes:** the complete signed response identity is retained, including the diagonal subtraction and boundary-pole cancellation. But simple pointwise history covariance blocks do not provide the desired positive storage. The remaining candidate must use more structure—such as a genuinely nonlocal history coupling or different state variables—and must prove both storage positivity and the unchanged supply/dissipation identity. We have not ruled out that broader route or proved RH.

## A. Pole-cancelled arithmetic transfer and exact storage weights
Let b_n=log n, a_n=Lambda(n)/sqrt(n), E(x)=psi_Cheb(x)-x, and
k5(a)=e^-5a/2/(1-e^-2a), K5=digamma(5/4)-log pi=K0+4.
The previously derived exact transfer, initially Re z>1/2, is
q(z)=g5(z)-int_[1,infty)x^-(z+1/2)dE(x),
g5(z)=K5/2+int_0^infty k5(a)(1-e^-az)da.
Both rational pole channels have already been cancelled in this expression. Its finite signed-measure approximation is explicitly
q_EB(z)=g5(z)-sum_(b_n<B)a_n e^-b_nz
 +int_0^B e^(a/2)e^-az da.
Unlike the raw q_B from realization2033, q_EB has no pole at z=1/2. It is defined by convergent integrals throughout Re z>0 (indeed a larger half-plane for g5), so low-frequency checks are legitimate. q_EB->q locally uniformly on Re z>1/2, not automatically in any state-energy norm on a larger domain.

Put the signed jump measure
nu_B(da)=k5(a)da+sum_(b_n<B)a_n delta_b_n(da)-e^(a/2)1_(0<a<B)da,
and tilde M_B=M_B-4e^(B/2), M_B=-K0+2sum_(b_n<B)a_n.
Then exactly
q_EB(z)=-tilde M_B/2+int nu_B(da)(1-e^-az).
The divergent total Gamma measure is only used in its convergent difference form; the feedthrough shown is finite.
Its signed history tail is
w_B(s)=int_[s,infty)nu_B(da)=g(s)+p_B(s)-d_B(s),
g(s)=int_s^infty k5(a)da
 =artanh(e^-s/2)+arctan(e^-s/2)-2e^-s/2,
p_B(s)=sum_(s<=b_n<B)a_n,
d_B(s)=2(e^(B/2)-e^(s/2))1_(s<B).
Endpoint values at the finitely many b_n do not affect any history L2 form. All weights are independent arithmetic data. g>0 and is locally integrable with a logarithmic singularity at s=0; p_B,d_B are nonnegative bounded functions at each finite B.

For smooth causal u, with physical history f_t(s)=u(t-s), the exact signed KYP identity is
2Re(conj(u)y_EB)=d/dt int_0^infty w_B(s)|f_t(s)|^2ds
 +int nu_B(da)|u(t)-u(t-a)|^2-tilde M_B|u(t)|^2.
This follows by integrating the elementary one-delay identity from realization2033 against nu_B. Every term converges on that smooth causal core; the negative smooth density is finite-cutoff and the Gamma difference controls zero. No positive sign is inferred for w_B or the dissipation measure.
In spectral variables d=z+conj w and E_a(z)=1-e^-az,
K_qEB(z,w)=int_0^infty w_B(s)e^-zs e^-conj(w)s ds
 +[int nu_B(da)E_a(z)conj E_a(w)-tilde M_B]/d.
This is the complete mixed identity, not merely a storage guess. In particular the negative mass is NOT an unidentified Schur complement and is not inferred from a frequency derivative.
For a compact input of width A<=B, integrating supply gives
W_A(F)=J5(F)+sum_(b_n<B)a_n||F-T_b_nF||^2
 -int_0^B e^(a/2)||F-T_aF||^2da-tilde M_B||F||^2.
Terms beyond the input width cancel their diagonal masses, so this is exactly the earlier full-W identity, not just its E0 restriction. Boundary-pole contributions were cancelled algebraically with the smooth density and Gamma pole, not discarded. On E0 the same formula holds; the subtraction remains.

## B. Block test 1: explicitly positive fixed-Gamma/prime contraction
On two copies of L2((0,infty),ds), initially on compact smooth histories supported away from zero, specify
Q_Gamma=M_g, Q_prime,B=M_p_B,
X_B=-M_sqrt(g p_B).
The measurable multiplication block
C_B=[[Q_Gamma,X_B],[X_B^*,Q_prime,B]]
is PSD pointwise, hence on its natural multiplication-form domain, because
<C_B(f,h),(f,h)>=int|sqrt(g)f-sqrt(p_B)h|^2ds.
This is an actual independently specified block, not a fit to W or its spectral data. Its physical shared-input compression has weight
w_C,B=(sqrt(g)-sqrt(p_B))^2.
It describes a positive difference-of-amplitudes history storage. It does NOT match w_B=g+p_B-d_B, nor the earlier uncorrected sum g+p_B, in general. Maintaining the original readout while changing storage would also change the dissipation remainder. There is no reason that new remainder is positive.

### General fixed-diagonal obstruction [EXACT]
The following is stronger than checking this one cross term. Let a PSD block have fixed Gamma quadratic energy G(f)<infty and prime energy P_B(f), with ANY cross form X_B defined on the physical embeddings of the same history f. Positivity of the scalar 2x2 restriction implies
|X_B(f,f)|^2<=G(f)P_B(f).
Therefore its shared-history energy is bounded below by
G(f)+P_B(f)+2Re X_B(f,f)>=(sqrt(P_B(f))-sqrt(G(f)))^2.
For a nonzero compactly supported history f with finite G,
P_B(f)=int p_B(s)|f(s)|^2ds ->infty,
because p_B(s) increases to infinity for every fixed s. The divergence of sum a_n follows already from the divergence of the prime reciprocal sum; no RH bound is required. Monotone convergence then gives the assertion.
Consequently NO PSD cross form with these fixed diagonal energies and fixed physical embeddings can make the all-prime shared-history storage finite. This does not require an invertible Gamma operator or a bounded Schur inverse. Allowing the Gamma diagonal itself to grow with B, changing the input embeddings, taking a quotient, or introducing different state variables is outside the proved obstruction and would need a new matching/finiteness argument.

## C. Block test 2: exact signed-storage matching after density cancellation
Combine the two positive arithmetic pieces as a_B=g+p_B. Compare them with the positive smooth-density tail d_B. Define
Q_plus,B=M_a_B, Q_smooth,B=M_d_B, X_match,B=-M_d_B,
B_match,B=[[M_a_B,-M_d_B],[-M_d_B,M_d_B]].
These blocks are again independently specified from the same arithmetic kernel/density, not learned from W values. On (f,f), the quadratic form is exactly int(a_B-d_B)|f|^2=int w_B|f|^2, the signed storage in §A.
For s with d_B(s)>0, the Schur complement relative to d_B is a_B-d_B; equivalently the determinant is d_B(a_B-d_B). Thus this multiplication block is PSD iff w_B>=0 almost everywhere on (0,B). For s>=B, d_B=0 and the block is diag(g,0), already PSD. No infinite-dimensional inverse or unsupported matrix analogy is used: this is a pointwise multiplication-form criterion.
A compression to histories supported on any measurable region where a_B>=d_B really is PSD and retains the signed-storage weight there. Such a region need not be invariant under history transport, so this restricted static result is not a passive realization of the whole evolution.

### An exact arithmetic negative region, not merely a floating-point failure
Choose B=2 and s0=49/25=1.96. Elementary exponential bounds give 7<exp(s0)<exp(2)<8, so there is no prime-power lag in [s0,2); p_2(s0)=0.
The smooth density tail satisfies
d_2(s0)=2(e-e^(49/50))=2e^(49/50)(e^(1/50)-1)>1/25.
Meanwhile
0<g(s0)<=e^(-5s0/2)/[(5/2)(1-e^-2s0)]<1/100,
where e^(49/10)>100 and 1-e^(-98/25)>1/2 give even the rough upper estimate <1/125. Therefore g(s0)-d_2(s0)<-3/100. A neighborhood of s0 remains inside the same prime gap with strictly negative w_2. Taking any nonzero smooth history supported in that neighborhood yields a negative block direction (f,f). This proves failure in the actual infinite-dimensional multiplication form, not just in a sampled matrix.
The exponential inequalities above can be established by elementary rational Taylor bounds; their margins are large. Numerical values, offered only as calibration, are
g=0.00301192415024,
d=0.10765117305926,
w=-0.10463924890902,
det=-0.01126453789309,
pointwise eigenvalues approximately -0.0643602 and +0.1750233.
The analytical negativity does not rely on those decimals.

## D. Saturating the positive block is not an energy-preserving repair
For a_B,d_B>=0, consider the explicit contraction family
B_rho=[[a_B,-rho sqrt(a_B d_B)],[-rho sqrt(a_B d_B),d_B]],
with real |rho|<=1, interpreted as multiplication blocks. These are PSD. At rho=1 the shared-history weight is
w_sat=(sqrt(a_B)-sqrt(d_B))^2>=0.
To preserve the signed weight w_B=a_B-d_B, the physical diagonal calculation requires
rho_req=sqrt(d_B/a_B)
where d_B>0. This lies outside the PSD range whenever d_B>a_B. At the proven negative region it is about 5.97843, not a permissible contraction. Thus no member of this natural pointwise contraction family simultaneously preserves the exact signed storage and passes PSD there. This is a concrete ansatz obstruction, not a general theorem excluding nonlocal storages or alternate state realizations.

If one instead retains the same output q_EB while substituting positive storage S_sat, its exact residual kernel is
R_sat(z,w)=q_EB(z)+conj q_EB(w)
 -(z+conj w)int_0^infty w_sat(s)e^-zs e^-conj(w)s ds.
This formula preserves the transfer by definition, but positivity of R_sat is a SEPARATE test; block PSD alone proves nothing about it. At B=2 the finite pole-cancelled transfer has
q_E2(0)=-tilde M_2/2≈-0.17576223487.
Thus for sufficiently small positive real z, K_qE2(z,z)<0; no positive storage plus PSD residual can realize this entire finite-B transfer passively. This is an additional numerical/DC diagnostic with a large margin, not the proof needed for the already exact prime-gap block obstruction. Finite-B signed-density truncations need not themselves be passive even though their supply agrees with W on inputs supported in sufficiently short windows. They are not the final full arithmetic response.
Alternatively choosing a new readout so w_sat becomes the tail of its signed delay measure realizes a different transfer: replace nu_B by -dw_sat, adjust feedthrough as specified by that new system. The derivative/atoms generally differ from k5+prime-smooth, and the unchanged W identity has then been lost. A positive storage weight alone does not even ensure -dw_sat is positive, so that modification is not an automatic passivity proof either.

## E. All-prime behavior of the density-balanced positive block
In the second construction BOTH positive diagonals diverge as B grows: a_B and d_B. Their formal difference is finite at each B but is arithmetic-error sensitive. Let
P(t)=sum_(b_n<t)a_n,
R(t)=P(t)-2(e^(t/2)-1).
Away from atom endpoints,
w_B(s)=g(s)+R(B)-R(s),
w_sat,B(s)=w_B(s)^2/[sqrt(a_B(s))+sqrt(d_B(s))]^2.
By the ordinary PNT [THM], for fixed s the denominator is asymptotic to 8e^(B/2). The elementary block computation does not by itself bound R(B) sufficiently to prove a finite all-prime limit of w_sat. For illustration only, IF R(B)=o(e^(B/4)), the positive shared weight collapses to zero for each fixed s; such a limit would not reproduce a nonzero target storage automatically. No such rate or RH input is assumed here. Separately, the diagonal blocks have no finite naive limit on a nonzero fixed history. A valid limiting state space would need a justified renormalization/coupling/quotient and full supply matching, not subtraction of infinities with a declared positive sign.

## F. Coefficient-sensitive control, including the n=2 ghost
At B=2 the actual prime atoms are n=2,3,4,5,7, with exactly the original weights. At s=1/2,
g≈0.14639418242586,
p_B≈2.92623418217641,
d_B≈2.86851282354261.
Thus w_B≈+0.20411554105966 and the exact-match point block is PSD there (numerical local statement). Deleting only the n=2 atom reduces p_B(s) by a_2=(log2)/sqrt2 for every s<log2 and leaves g,d unchanged. Then at s=1/2,
w_ghost≈-0.28601353067461,
det B_match,ghost≈-0.82043348044682.
So the exact-matching block is coefficient-sensitive; its local behavior changes with a genuine arithmetic atom. It nevertheless fails elsewhere for the true coefficients too, so it is not a sign certificate. The always-square saturated PSD block remains PSD for either coefficient list and is therefore blind as a bare positivity test.

For the complete transfer the ghost modification is exactly
q_ghost(z)=q(z)+a_2 e^-b_2 z,
Delta K(z,w)=a_2[e^-b_2 z+e^-b_2 conj(w)]/[z+conj w].
For any compact test F,
Delta W(F)=2a_2 Re<F,T_log2F>.
The previous explicitly checked E0 input F=(D^2-1/4)(1-u^2)^4 on [-1,1] has
W(F)/||F||^2≈+0.0023337532,
W_ghost(F)/||F||^2≈-0.6392279387.
Those are prior non-interval quadratures with a large negative ghost margin, not new continuum eigenvalue certificates. They show why preserving the original kernel matters beyond passing a static PSD block. Note the ghost actually improves the finite-B DC test: q_E2,ghost(0)≈+0.31436683686; a single scalar low-frequency sign can miss the bad Gram direction.
No claim that the ghost is admissible complete Euler data, or has the genuine global FE, is made. It is a local coefficient-sensitivity falsifier only.

## G. Artifacts and scope
check2038.py/.json record all atoms, scalar weights, Schur determinants/eigenvalues, the contraction needed for exact matching, and the ghost difference. Arithmetic coefficients are computed directly; no W-sign fitting, optimization, spectral zeros or Ritz argument is used. The pointwise numerical matrices are checks of an exact multiplication-block criterion, not approximations to a continuum spectral minimum.
Proved: fixed finite Gamma diagonal plus diverging prime diagonal cannot be cured by ANY PSD cross form under fixed physical embeddings; the natural density-balanced exact-match multiplication block fails on an explicit actual prime gap; saturated positive alternatives do not retain the signed storage/readout automatically.
Not proved: impossibility of a nonlocal cross-history storage, a different arithmetic state module, or a positive realization of full q/W. Those remain open. The specific next requirement is a new independently specified storage with an actual domain and exact KYP residual calculation—not an assertion M=X^*Q^-1X. No further work was launched.

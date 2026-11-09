# t2057 — finite inertia, and a certified continuum index (scratch only)

No repo, Atlas, Page, manuscript, cloud or external-message changes. Everything here is scratch. No RH, Hodge-index, or all-window positivity claim.

## 1. Conventions and a substantive correction to the proposed pattern

Write **Q = W − P = H_A − M_A I** on the full window; W includes the pole form P = C+ conjugate(C−) + C− conjugate(C+). Let B have columns r±(u)=exp(±u/2), so E0=ker B*. Thus P=B J B*, J=[[0,1],[1,0]]. All inertias below are ordered (negative, zero, positive). Real matrices suffice: complexification has the same Hermitian inertia.

There are THREE different finite models, not interchangeable:

1. Exact-form Galerkin compressions Q_G, W_G on cell indicators. Their Gamma matrix is computed from exact integral formulas with numerical quadrature (no Gamma truncation). Their reported spectra are **NUMERICAL**, not interval certified.
2. The positive-Gamma **minorant** Q_J=d_J I−C_J−S_prime, and W_J=Q_J+P on the t2047 prime-invariant cells. The omitted Gamma form is positive, so Q≥Q_J and W≥W_J. These are not exact Galerkin matrices of Q and W.
3. The penalized proof matrix Q_J+κBB*, which is positive in t2047. It is not W off E0. Counting its negative directions would say nothing useful about those of the original unconstrained form.

The exact-form finite models tested here have **one**, not two, negative directions for Q, and **none** for W. The two constraints remove the one negative direction in the sense of index reduction, not by identifying E0 with an exact spectral orthocomplement. The minorant W_J instead has two negative directions; they disappear upon restricting to E0. The distinction matters.

## 2. Exact inertia identity and its hypotheses

For an n×n nonsingular Hermitian Q and an n×k full-rank B, set S=B*Q^{-1}B and K=[[Q,B],[B*,0]]. Eliminating Q yields

    inertia(K) = inertia(Q) + inertia(−S).

Choose a basis Z for ker B* and a complementary basis Y. Congruence reduction of the constraint/Y block yields

    inertia(K) = inertia(Z*QZ) + (k,0,k).

Consequently, for k=2,

    n−(Q|E0) = n−(Q) + n+(S) − 2,
    n0(Q|E0) = n0(S),
    n+(Q|E0) = n+(Q) + n−(S) − 2.

S need not be nonsingular for these bordered formulas. Q must be nonsingular and B full rank. If S is nonsingular, this is equivalently n−(Q|E0)=n−(Q)−n−(S). If Q is singular, use the bordered matrix directly, not an unqualified inverse or pseudoinverse. The same reasoning applies to the continuum closed form when the associated self-adjoint Q is boundedly invertible, has finite negative index, and B is bounded/full-rank; Q^{-1}B lies in its operator domain. Strict constrained coercivity then forces S nonsingular. An eigenvector annihilated by both moments survives in E0; nothing here discards such modes.

Interlacing only says n−(Q)≤2 is necessary for constrained nonnegativity. It does not say the unconstrained form must have two negative directions. At these windows it has one. For full W the same identity uses S_W=B*W^{-1}B, not S_Q.

## 3. Complete Gamma finite matrices (no Gamma truncation)

Use n equal cells, h=A/n, normalized indicators. Q is symmetric Toeplitz. With k(a)=exp(−a/2)/(1−exp(−2a)),

    Q_ii = K0 + (2/h)∫_0^h a k(a) da + 2∫_h^∞ k(a) da,
    Q_(i,i+m) = −(1/h)∫_(mh−h)^(mh+h) (h−|a−mh|)k(a)da, m≥1,

before prime terms. Each prime power n adds the exact translation-overlap Toeplitz coefficients with weight Λ(n)/sqrt(n). The diagonal prime-jump mass cancels against M_A; there is no forgotten diagonal jump at a prime crossing. Exact cell integrals give B, and P=BJB*. QR gives an orthonormal basis for E0; a direct constrained diagonalization is compared against the Schur identity. No inverse formula alone supplies the constrained spectrum.

Runs use n=128,256,512 over 16 windows including log2, log3±1e−5, log4±1e−5, log5±1e−5, and n=1024,2048 on eight representative windows. A coarse 101-window scan on [.5,3] uses n=128. Inertia tolerance is 1e−9; reported zero means within tolerance, not a proof of exact nullity. All these counts are NUM. The indicator spaces are nested at fixed A under doubling; constrained Ritz minima decrease and are upper bounds, not continuum lower bounds.

There is no detected A* through width 3 on the tested scan. Nor does n−(Q) exceed one anywhere tested. The windows above 1.1 have a severe near-zero-resolution obstruction: constrained minima fall roughly with the discretization bias, so positive finite values do not certify a continuum gap or exclude an unsampled failure. New prime terms turn on through a vanishing overlap at A=log n, not a finite rank-count jump forced by the coefficient. We tested crossings; no index transition was found.

## 4. Certified passage to the continuum: stronger than index ≤2

The old certificates already imply Q+κBB*≥cI on the full continuum, with c=.004 at A=1 and c=.0005 at A=1.1. Hence n−(Q)≤2, independently of any Ritz computation. Here we sharpen this to **n−(Q)=1 with a spectral gap** at BOTH endpoints.

Let L be the prime-invariant cell space and H its orthogonal complement, and use Q_J (no moment penalty). Its high block satisfies Q_J,HH≥h_*I, h_*>2.23044 at A=1 and h_*>3.20785 at A=1.1. Prime mixed blocks vanish exactly. Q−Q_J≥0 in the complete form domain.

### A=1: scalar mixed-block bound

For Q_J the mixed norm squared is at most s_J epsilon_C (no moment term). Rerunning the original interval checks plus a verified diagonalization of Q_J,LL gives a lower bound >.00704288 on its SECOND eigenvalue. Its first eigenvalue is negative. With c=.004,

    .00704288 − c − s_J epsilon_C/(h_*−c) > .00051260.

Restricting L to the orthogonal complement of its single low negative eigenvector and using the high-block Schur bound proves that Q_J−c has negative index at most one. This is a continuum complement bound, not an extrapolation from a finite positive eigenvalue. A normalized constant trial has rigorously enclosed exact Q value in [−1.954501,−1.954000], proving at least one negative direction. Therefore the continuum Q has exactly one negative eigenvalue and its remaining spectrum is ≥.004. In particular it is invertible and dist(0,spec Q)≥.004.

### A=1.1: directional Schur complement

Use the t2047 derivative Gram D with the exact prime-invariant 1838-cell partition. For the unpenalized Q_J,

    mixed*mixed* ≤ (h/pi)^2 D.

Thus Q_J−c has index at most that of the finite matrix

    E−cI, E=Q_J,LL−alpha D,

provided alpha≥(h/pi)^2/(h_*−c). We use alpha=1/40000000, the original conservative coefficient (now no factor 2 and no moment cross term is needed). Interval coefficient and derivative-Gram construction errors plus eigenvector residual/orthogonality bounds verify that E has at most one eigenvalue below c=.0005. An interval constant trial proves at least one negative direction of exact Q. Hence again n−(Q)=1, with the rest of its spectrum ≥.0005 and bounded invertibility.

The numerical diagonalization only supplies candidates. All finite error allowances use the same explicitly documented IEEE-754 dot-product forward-error model as t2047: interval coefficients, conservative construction norm errors, and residual/orthogonality estimates. Not theorem-prover verification; assumptions and runnable checks retained. This is a one-sided positive-Gamma minorant plus an exact-form negative trial, not an unproved two-sided operator approximation.

### Certified continuum Schur sign

The earlier constrained certificates give Q|E0≥cI. For x∈ker S, y=Q^{-1}Bx lies in E0 and q(y)=x*Sx=0. Coercivity forces y=0, hence x=0: S is invertible. The bounded form-orthogonal decomposition

    H = E0 direct-sum Q^{-1}ran B

then gives inertia(S)=(1,0,1), because Q has one negative direction and E0 none. This proves the sign of the actual continuum inverse-moment matrix without pretending that a finite inverse approximates it in norm. No numerical values for the continuum S are certified. Finite inverse values are not substituted into this argument.

We have NOT certified full W≥0 on the unconstrained continuum. Its exact-form finite compressions are positive in these computations, but the Gamma minorants W_J are not. The finite-minorant negative counts therefore cannot be transferred as lower negative counts of W: adding a positive omitted form can remove them. The Q trial/index sandwich is what makes our exact continuum conclusion valid.

## 5. Boundary interpretation

The formal boundary plane with Gram [[0,1],[1,0]] has exact signature (1,1); h+v has positive square 2. This is distinct from the compression of Q onto span{r+,r−}, though the latter also has signature (1,1) in these numerical tests. Negative Q eigenvectors are even and overlap strongly, but not perfectly, with the moment span. Quantitative squared projection norms are in the JSON. The two constraints are a codimension-two annihilator, not a license to delete arbitrary two negative eigenvalues. This remains an analytic signature mechanism, not the Hodge index theorem; no arithmetic class map or independent ample class has been constructed.

## 6. Artifacts and reproducibility

Run with `OPENBLAS_NUM_THREADS=1 python3 <script>`.

- inertia2057.py / inertia2057.json: complete-Gamma cell formulas, finite counts, direct constrained spectra, Schur values, overlaps, crossings.
- scan2057.py / scan2057.json: refined grids through 2048 and 101-window coarse scan.
- certify_inertia2057.py / certify_inertia2057.json / certify_two_inertia2057.json: reruns original interval checks, then continuum index and gap checks. Original source files are read/executed with output JSON redirected HERE; original files are not edited.
- base_certificate2057.json / base_two_certificate2057.json: the rerun original lower certificates.
- explore_minorant2057.py: initial parity diagnostic; superseded by the full verified index test.

Numerical tables and exact verified outputs follow in the generated results section.

## 7. Results (generated from JSON)

Complete-form cell compressions, **NUM**, n=2048. For EVERY row Q inertia=(1,0,2047), W inertia=(0,0,2048), constrained inertia=(0,0,2046), S_Q=(−,+), S_W=(+,+).

| A | S_Q eigenvalues | min constrained (1024 → 2048 cells) | negative Q eigenvector squared overlap with moment span |
|---|---|---|---|
| 0.5 | -1.03839034, 0.01122220 | 0.87491956 → 0.87488185 | 0.96913195 |
| 0.694 | -1.00118660, 0.14302224 | 0.54558138 → 0.54554575 | 0.96965288 |
| 1 | -1.00000262, 0.99038889 | 0.011906274 → 0.011872393 | 0.98988943 |
| 1.1 | -1.00000211, 0.99901107 | 0.00096604001 → 0.00093187288 | 0.98745388 |
| 1.5 | -1.00000096, 0.99988935 | 5.5632258e-05 → 1.7214655e-05 | 0.99570798 |
| 2 | -1.00000053, 0.99996491 | 4.8606821e-05 → 1.2779984e-05 | 0.99723964 |
| 2.5 | -1.00000035, 0.99998554 | 4.7092255e-05 → 1.304789e-05 | 0.99832196 |
| 3 | -1.00000028, 0.99999332 | 4.3161838e-05 → 1.2785888e-05 | 0.99910302 |

Certified-partition finite **minorant** summary (spectral figures/counts NUM; continuum claims CERT as detailed above):

| A | cells | inertia(Q_J) | inertia(W_J) | S_Q_J eigenvalues | constrained min |
|---|---|---|---|---|---|
| 1 | 815 | (1, 0, 814) | (2, 0, 813) | -0.99916496, 1.11589604 | 0.00702064641 |
| 1.1 | 1838 | (1, 0, 1837) | (2, 0, 1836) | -0.99995804, 1.00531059 | 0.00069090815 |

For W_J, S_W_J has two negative signs by the nonsingular finite inertia bookkeeping; for Q_J it has one sign of each type. On E0 the pole is zero, so their constrained matrices agree. The corresponding penalized proof matrices have no negative directions.

Verified continuum outputs:

- A=1: n−(Q)=1; remaining spectrum ≥0.004; S signature (1,0,1); exact Q constant-trial enclosure [-1.95450095781795573998552895784503955066406250911849223799627, -1.95400049970328649843979608755515555244758730191845925024041]; verified effective second lower 0.00704288131202; Schur margin 0.000512607028031.
- A=1.1: n−(Q)=1; remaining spectrum ≥0.0005; S signature (1,0,1); exact Q constant-trial enclosure [-2.13510295432079493712983338249701819793180676435718534790286, -2.13464798482261077814886410647591153288652627296321595393032]; verified effective second lower 0.000664078976317; Schur margin 0.000164078976317.

The continuum S-sign certification reuses the already certified constrained inequality; it is NOT a logically independent Schur-sign proof of that inequality. The new independent information is the exact unconstrained Q index and gap.

`check2057.py` reruns the width-one interval/continuum certificate, recomputes representative finite spectra, and checks all 117 refined/scan inertia identities; output in check2057.json.

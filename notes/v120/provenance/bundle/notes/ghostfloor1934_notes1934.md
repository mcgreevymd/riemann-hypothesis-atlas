# ghostfloor1934 — subtraction vs floor (t1934; Nov 7 2026 CST; RH not proved). floor1934.py/json.
## Split (exact)
On window length A, F real, N ≥ e^A:  W = P + H − M_A‖F‖²,  H = E_∞ + Σ_{log n<A} a_n‖F−T_{log n}F‖²,
 M_A = −K0 + 2Σ_{log n<A} a_n, K0 = ψ(¼)−log π = −5.37218 (interactions1890 THM; tails n ≥ e^A cancel exactly).
 (i) P = 2ab, a,b = ∫F e^{∓u/2}: hyperbolic (1,1) BOUNDARY form; E0 = {a=b=0} kills both null directions (positive and
     negative), not a projection onto a negative eigenvector. Closed codim-2 only on a fixed window (compat1907 §3).
 (ii) M_A: BULK, survives on E0. Prime part = exact diagonal self-energy 2a_n‖F‖² of each spring; arch part −K0 is the
     Γ-factor constant (FE-fixed), not a finite self-energy. Correction to voa1932: "normal-ordering counterterm" = only
     this diagonal subtraction; no state/current realizing it was shown.
 "Ghost" language: P's negative direction is a Krein-type label (lemma1: n_- = 1 + N_+ on finite V, Thm 15.2), not BRST.
## Achievement 1 (subtraction fixed algebraically): essentially already exact and cutoff-free (M_A above).
   Missing: an independent structure (state/current/Sonin trace) that PRODUCES M_A rather than reading it off.
## Achievement 2 (floor): kinetic floor κ_A := inf_{E0∩window} H/‖F‖²; W ≥ 0 on E0 ⇔ κ_A ≥ M_A (RH-equivalent over all A).
 Zero velocity = classical kinetic minimum 0, not a cushion; the cushion is a localization (zero-point-type) effect.
## New numbers (sine basis J=36, Ritz upper bounds on floors, quadrature error ~1e-3; joint−M slightly negative = error,
## known true margin ~1e-5 at A=2 [interactions1890]; NOT certified)
 A   M_A    Einf full→E0   Ep full→E0    sum sep(E0)  shortfall  joint(E0)
 1.0 6.352  3.664→5.559    0.490→0.490   6.049        0.304      6.367
 1.6 8.314  3.071→5.079    1.725→1.748   6.827        1.487      8.314
 2.0 11.225 2.775→4.846    4.022→4.298   9.143        2.081      11.224
 3.0 18.388 2.218→4.394    8.849→11.33   15.72        2.666      18.37
 Findings: (a) E0 lifts the archimedean floor by ≈ +1.9…2.2 (removing the e^{±u/2} near-threshold content) — the boundary
 condition is itself part of the cushion. (b) separate floors fall short of M_A by 0.30→2.67, growing with A: positivity needs
 an ALIGNMENT gain between arch and prime cushions (their near-minimizers must be far apart). (c) Slepian/Landau–Pollak bound
 E_∞ ≥ f(X)(1−λ0(AX/2)) is rigorous but weak (2.31 at A=1, 1.43 at A=2; grid X ≥ 0.5).
## Recovered candidates (exact ids)
 C1 semilocal Sonin inequality: atlas needed_semilocal_sonin_inequality [Open], t_iff_semilocal_sonin; spinor1908; CCM
    2310.18423 trace positivity; R26 (STATE §231): naive Π_S with p=2 fails, λ_min = −log2/√2.
 C2 coupled cushion: atlas kinetic_mass_metric, witten_constant_window (c = 1 − O(1e-10), circular variants),
    slemma_constant_indefinite_cushion, arch_levy_khintchine_sos; bridge1371 (STATE §292: no shift-free split, KLMN a→1).
 C3 nonlocal Weitzenböck/Dirac: spinor1908 (lichnerowicz_is_gamma_shift, weitzenbock_curvature_density FAILS pointwise),
    momentum1929 target. Only factorized/per-prime ansätze tested (no_single_prime_frame_positive, string1915); coupled
    constructors not ruled out.
 C4 ample/Hodge metric on E0: restframe1928; Lemma 99 (§110 Cartan/Wick), Lemma 113 (§124); no candidate on E0.
 Frame form H^{-1/2}BH^{-1/2} ≤ I ⇔ W ≥ 0 (Sylvester, §292 Thm 3.5): restatement; useful only for finite-window certificates.

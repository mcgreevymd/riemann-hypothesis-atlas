# hp2251 — high-precision spectra of Q and QW = Q + P (t2251)
Scratch only. Window u ∈ [-r/2, r/2]. Scripts:
- sine.py — spec basis sqrt(2/r) sin(nπ(u+r/2)/r), closed-form shifted overlaps, k=1/(2t)+h split (Si/Ci exact, composite Gauss–Legendre on h), mpmath.eigsy. Output: sout/*.json, sine_summary.txt (summ.py).
- hp.py — Legendre basis, Q from the existing Arb assembly (pont2106/res2115/cert3 → res2112/cert2, ball radii ≤1e-459), P added in mpmath. Output: out/*.json.
- scloc.py — locates ground-state sign changes. check_vs_lib.py — symbol-route check.
Checks: symbol route (1/π)∫σ_r|F̂|² = cᵀQc to ~1e-8 (r=1, 2.5; limited by ξ cutoff); low-index entries agree with lib.py; quadrature node doubling changes nothing in 15 digits; dps vs 2×dps identical in all printed digits for every adequately-precise run.
r= 1.0 N= 50 dps= 60 | QW e0=1.050010e-06 e1=2.0438e-02 o0=2.250394e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.973471 lam1=1.354390e-02(e) sc=0 t=4.2
r= 1.0 N=100 dps= 60 | QW e0=1.005509e-06 e1=1.9292e-02 o0=2.111613e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.980368 lam1=1.276258e-02(e) sc=0 t=17.4
r= 1.0 N=100 dps=120 | QW e0=1.005509e-06 e1=1.9292e-02 o0=2.111613e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.980368 lam1=1.276258e-02(e) sc=0 t=27.9
r= 1.0 N=150 dps= 60 | QW e0=9.844454e-07 e1=1.8878e-02 o0=2.059261e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.982729 lam1=1.248195e-02(e) sc=0 t=36.3
r= 1.0 N=200 dps= 60 | QW e0=9.731384e-07 e1=1.8672e-02 o0=2.030798e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.983891 lam1=1.234293e-02(e) sc=0 t=73.1
r= 1.0 N=200 dps=120 | QW e0=9.731384e-07 e1=1.8672e-02 o0=2.030798e-04 sc=0 n-=0 e<o=True | Q n-=1 q0=-1.983891 lam1=1.234293e-02(e) sc=0 t=98.4
r= 1.2 N= 50 dps= 60 | QW e0=1.814324e-09 e1=1.2104e-04 o0=6.950916e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.396140 lam1=7.789825e-05(e) sc=0 t=3.5
r= 1.2 N=100 dps= 60 | QW e0=1.767069e-09 e1=1.1387e-04 o0=6.603817e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.406333 lam1=7.324962e-05(e) sc=0 t=12.9
r= 1.2 N=100 dps=120 | QW e0=1.767069e-09 e1=1.1387e-04 o0=6.603817e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.406333 lam1=7.324962e-05(e) sc=0 t=19.4
r= 1.2 N=150 dps= 60 | QW e0=1.729889e-09 e1=1.1069e-04 o0=6.430450e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.409789 lam1=7.119585e-05(e) sc=0 t=32.7
r= 1.2 N=200 dps= 60 | QW e0=1.704734e-09 e1=1.0889e-04 o0=6.325728e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.411562 lam1=7.003429e-05(e) sc=0 t=69.0
r= 1.2 N=200 dps=120 | QW e0=1.704734e-09 e1=1.0889e-04 o0=6.325728e-07 sc=0 n-=0 e<o=True | Q n-=1 q0=-2.411562 lam1=7.003429e-05(e) sc=0 t=89.9
r= 1.5 N= 50 dps= 60 | QW e0=4.837927e-15 e1=1.3209e-09 o0=4.005096e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.076603 lam1=8.457458e-10(e) sc=0 t=3.6
r= 1.5 N=100 dps= 60 | QW e0=4.014790e-15 e1=1.2769e-09 o0=3.715168e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.088636 lam1=8.176808e-10(e) sc=0 t=12.2
r= 1.5 N=100 dps=120 | QW e0=4.014790e-15 e1=1.2769e-09 o0=3.715168e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.088636 lam1=8.176808e-10(e) sc=0 t=19.9
r= 1.5 N=150 dps= 60 | QW e0=3.986397e-15 e1=1.2591e-09 o0=3.679928e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.092692 lam1=8.062898e-10(e) sc=0 t=30.4
r= 1.5 N=200 dps= 60 | QW e0=3.954707e-15 e1=1.2434e-09 o0=3.639596e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.094728 lam1=7.961684e-10(e) sc=0 t=64.8
r= 1.5 N=200 dps=120 | QW e0=3.954707e-15 e1=1.2434e-09 o0=3.639596e-12 sc=0 n-=0 e<o=True | Q n-=1 q0=-3.094728 lam1=7.961684e-10(e) sc=0 t=94.8
r=   2 N= 50 dps= 60 | QW e0=2.110141e-29 e1=5.1328e-23 o0=5.086621e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.265326 lam1=3.283445e-23(e) sc=0 t=3.4
r=   2 N=100 dps= 60 | QW e0=7.662204e-30 e1=2.8202e-23 o0=1.880113e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.285486 lam1=1.803580e-23(e) sc=0 t=11.4
r=   2 N=100 dps=120 | QW e0=7.662204e-30 e1=2.8202e-23 o0=1.880113e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.285486 lam1=1.803580e-23(e) sc=0 t=19.6
r=   2 N=150 dps= 60 | QW e0=6.815481e-30 e1=2.5469e-23 o0=1.759500e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.292914 lam1=1.628759e-23(e) sc=0 t=29.4
r=   2 N=200 dps= 60 | QW e0=6.533542e-30 e1=2.3427e-23 o0=1.623039e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.295908 lam1=1.498102e-23(e) sc=0 t=63.2
r=   2 N=200 dps=120 | QW e0=6.533542e-30 e1=2.3427e-23 o0=1.623039e-26 sc=0 n-=0 e<o=True | Q n-=1 q0=-4.295908 lam1=1.498102e-23(e) sc=0 t=92.4
r= 2.5 N= 50 dps= 60 | QW e0=1.665655e-42 e1=3.2843e-36 o0=2.089474e-39 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.617647 lam1=2.108031e-36(e) sc=0 t=3.3
r= 2.5 N=100 dps= 60 | QW e0=7.939249e-54 e1=1.3937e-46 o0=3.331449e-50 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.642440 lam1=8.922973e-47(e) sc=0 t=11.2
r= 2.5 N=100 dps=120 | QW e0=7.939248e-54 e1=1.3937e-46 o0=3.331449e-50 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.642440 lam1=8.922973e-47(e) sc=0 t=18.5
r= 2.5 N=150 dps= 60 | QW e0=7.259927e-55 e1=2.3329e-47 o0=5.505196e-51 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.650961 lam1=1.493259e-47(e) sc=0 t=28.9
r= 2.5 N=200 dps= 60 | QW e0=6.014299e-55 e1=2.0363e-47 o0=4.567168e-51 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.655448 lam1=1.303443e-47(e) sc=0 t=60.0
r= 2.5 N=200 dps=120 | QW e0=6.014292e-55 e1=2.0363e-47 o0=4.567168e-51 sc=0 n-=0 e<o=True | Q n-=1 q0=-5.655448 lam1=1.303443e-47(e) sc=0 t=85.7
r=   3 N= 50 dps= 60 | QW e0=7.661404e-52 e1=1.2965e-45 o0=1.840245e-49 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.146246 lam1=8.347155e-46(e) sc=0 t=3.4
r=   3 N= 50 dps=150 | QW e0=7.661404e-52 e1=1.2965e-45 o0=1.840245e-49 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.146246 lam1=8.347155e-46(e) sc=0 t=8.3
r=   3 N=100 dps= 60 | QW e0=2.399595e-60 e1=2.6193e-60 o0=2.710905e-60 sc=2 n-=0 e<o=True | Q n-=1 q0=-7.192448 lam1=2.472037e-60(e) sc=0 t=10.8
r=   3 N=100 dps=120 | QW e0=1.239493e-75 e1=1.5109e-68 o0=2.178738e-72 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.192448 lam1=9.691915e-69(e) sc=0 t=17.5
r=   3 N=100 dps=150 | QW e0=1.239493e-75 e1=1.5109e-68 o0=2.178738e-72 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.192448 lam1=9.691915e-69(e) sc=0 t=20.5
r=   3 N=150 dps= 60 | QW e0=1.589374e-60 e1=1.6687e-60 o0=1.504804e-60 sc=2 n-=0 e<o=False | Q n-=1 q0=-7.204438 lam1=1.589857e-60(o) sc=0 t=27.0
r=   3 N=150 dps=150 | QW e0=7.874631e-89 e1=4.3008e-81 o0=2.955009e-85 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.204438 lam1=2.755813e-81(e) sc=0 t=48.2
r=   3 N=200 dps= 60 | QW e0=8.575644e-61 e1=1.1080e-60 o0=2.109960e-61 sc=2 n-=0 e<o=False | Q n-=1 q0=-7.211459 lam1=4.024728e-61(o) sc=0 t=56.4
r=   3 N=200 dps=120 | QW e0=2.199958e-95 e1=3.0581e-87 o0=2.378628e-91 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.211459 lam1=1.958916e-87(e) sc=0 t=83.6
r=   3 N=200 dps=150 | QW e0=2.199958e-95 e1=3.0581e-87 o0=2.378628e-91 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.211459 lam1=1.958916e-87(e) sc=0 t=90.5
r=   3 N=200 dps=300 | QW e0=2.199958e-95 e1=3.0581e-87 o0=2.378628e-91 sc=0 n-=0 e<o=True | Q n-=1 q0=-7.211459 lam1=1.958916e-87(e) sc=0 t=149.9
r=   4 N= 50 dps= 60 | QW e0=-1.815808e-60 e1=1.9847e-59 o0=-1.219784e-60 sc=0 n-=2 e<o=True | Q n-=1 q0=-11.082314 lam1=1.261176e-59(e) sc=0 t=3.5
r=   4 N= 50 dps=200 | QW e0=6.309442e-66 e1=2.0977e-59 o0=2.879069e-63 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.082314 lam1=1.353630e-59(e) sc=0 t=12.8
r=   4 N=100 dps= 60 | QW e0=2.684708e-61 e1=1.3319e-60 o0=-1.099044e-60 sc=18 n-=1 e<o=False | Q n-=2 q0=-11.156033 lam1=-9.878362e-61(o) sc=0 t=10.5
r=   4 N=100 dps=120 | QW e0=8.241598e-106 e1=1.2808e-98 o0=1.492281e-102 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.156033 lam1=8.241613e-99(e) sc=0 t=18.1
r=   4 N=100 dps=200 | QW e0=8.241598e-106 e1=1.2808e-98 o0=1.492281e-102 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.156033 lam1=8.241613e-99(e) sc=0 t=28.9
r=   4 N=150 dps= 60 | QW e0=-1.506687e-60 e1=6.5729e-61 o0=-2.207756e-60 sc=22 n-=3 e<o=False | Q n-=4 q0=-11.180859 lam1=-2.160084e-60(o) sc=0 t=24.1
r=   4 N=150 dps=200 | QW e0=3.173353e-136 e1=1.3028e-128 o0=6.716702e-133 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.180859 lam1=8.369557e-129(e) sc=0 t=54.7
r=   4 N=200 dps= 60 | QW e0=-8.597872e-60 e1=-4.6782e-60 o0=-5.656018e-60 sc=70 n-=12 e<o=True | Q n-=12 q0=-11.194247 lam1=-8.761909e-60(e) sc=0 t=48.6
r=   4 N=200 dps=120 | QW e0=1.831585e-120 e1=1.9094e-120 o0=3.029793e-120 sc=2 n-=0 e<o=True | Q n-=1 q0=-11.194247 lam1=1.905916e-120(e) sc=0 t=75.6
r=   4 N=200 dps=200 | QW e0=6.288551e-162 e1=5.2882e-154 o0=2.220788e-158 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.194247 lam1=3.394408e-154(e) sc=0 t=97.1
r=   4 N=200 dps=400 | QW e0=6.288551e-162 e1=5.2882e-154 o0=2.220788e-158 sc=0 n-=0 e<o=True | Q n-=1 q0=-11.194247 lam1=3.394408e-154(e) sc=0 t=191.2
r=   5 N= 50 dps=250 | QW e0=5.118920e-76 e1=1.2544e-69 o0=1.270656e-73 sc=0 n-=0 e<o=True | Q n-=1 q0=-16.792376 lam1=8.080544e-70(e) sc=0 t=17.9
r=   5 N=100 dps=250 | QW e0=9.760596e-127 e1=1.4357e-119 o0=8.772396e-124 sc=0 n-=0 e<o=True | Q n-=1 q0=-16.935416 lam1=9.256307e-120(e) sc=0 t=35.3
r=   5 N=150 dps=250 | QW e0=3.388344e-169 e1=1.4429e-161 o0=3.993403e-166 sc=0 n-=0 e<o=True | Q n-=1 q0=-16.980939 lam1=9.289017e-162(e) sc=0 t=63.2
r=   5 N=200 dps=250 | QW e0=5.545876e-207 e1=3.6060e-199 o0=6.936707e-204 sc=0 n-=0 e<o=True | Q n-=1 q0=-17.002554 lam1=2.319283e-199(e) sc=0 t=107.8
r=   5 N=200 dps=500 | QW e0=5.545876e-207 e1=3.6060e-199 o0=6.936707e-204 sc=0 n-=0 e<o=True | Q n-=1 q0=-17.002554 lam1=2.319283e-199(e) sc=0 t=263.6
r=   6 N= 50 dps=300 | QW e0=4.327403e-84 e1=2.1577e-77 o0=5.613280e-82 sc=0 n-=0 e<o=True | Q n-=1 q0=-25.468808 lam1=1.382148e-77(e) sc=0 t=26.6
r=   6 N=100 dps=300 | QW e0=1.977743e-143 e1=2.3741e-136 o0=8.982161e-141 sc=0 n-=0 e<o=True | Q n-=1 q0=-25.738978 lam1=1.530520e-136(e) sc=0 t=49.1
r=   6 N=150 dps=300 | QW e0=2.340589e-195 e1=1.2862e-187 o0=5.485019e-192 sc=0 n-=0 e<o=True | Q n-=1 q0=-25.826202 lam1=8.290346e-188(e) sc=0 t=83.6
r=   6 N=200 dps=300 | QW e0=6.864591e-242 e1=6.3527e-234 o0=1.087268e-238 sc=0 n-=0 e<o=True | Q n-=1 q0=-25.870182 lam1=4.091788e-234(e) sc=0 t=139.1
r=   6 N=200 dps=600 | QW e0=6.864591e-242 e1=6.3527e-234 o0=1.087268e-238 sc=0 n-=0 e<o=True | Q n-=1 q0=-25.870182 lam1=4.091788e-234(e) sc=0 t=386.3

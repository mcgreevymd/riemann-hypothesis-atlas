# t2003: metrized derived diagonal on arithmetic P^1_Z vs -K0. Conventions: c1hat(L)=(div s,-log||s||^2),
# deg(0,g) on arithmetic surface = 1/2 * int g c1 ; arithmetic degree of a point-pairing likewise (Gillet-Soule/BGS).
import mpmath as mp, json
mp.mp.dps=30
K0=mp.digamma(0.25)-mp.log(mp.pi); mK0=-K0
r={}
# (1) FS height: c1hat(O(1)_FS)^2 = 1/2 * int log(1+|z|^2) mu_FS  (sections x0,x1 disjoint over Z; g_{x0}(0)=0; int log|z|^2 mu=0)
I1=mp.quad(lambda u: mp.log(1+u)/(1+u)**2,[0,mp.inf])         # = int log(1+|z|^2) dmu
Ilog=mp.quad(lambda u: mp.log(u)/(1+u)**2,[0,1,mp.inf])         # = int log|z|^2 dmu
r['O1hat_sq']=float(0.5*(I1-Ilog))
# (2) Arakelov Green normalisation on P^1 with mu=FS: average of log chordal distance (sphere, diameter 1) = -1/2
avg=mp.quad(lambda t: 0.5*mp.log(t),[0,1]); r['avg_log_chordal']=float(avg)
# numerical double check by direct integral over w with z=0: chordal(0,w)=|w|/sqrt(1+|w|^2)
avg2=mp.quad(lambda u: 0.5*mp.log(u/(1+u))/(1+u)**2,[0,1,mp.inf]); r['avg_log_chordal_direct']=float(avg2)
c=-avg  # g_Ar = log chordal + c, int g mu = 0  -> c=1/2 ; residue metric ||dz||_Ar=(1+|z|^2)e^{-c}
# (3) omega-hat^2 as function of constant rescale ||.||=e^{-a}||.||_{FS^-2}: (-2 O1)^2 + 2a*deg(omega) = 2 - 4a
f=lambda a: 4*r['O1hat_sq']+2*a*(-2)
conv={'a=0 (FS^-2 on omega, Green -log chordal^2)':0,
      'Arakelov (int g mu=0, residue metric), a=1/2':float(c),
      'Kahler vol-1, omega=(i/2)h dz^dzbar: a=-1/2 log pi':float(-0.5*mp.log(mp.pi)),
      'Kahler vol-1, omega=i h dz^dzbar: a=-1/2 log 2pi':float(-0.5*mp.log(2*mp.pi))}
r['omega_hat_sq']={k:float(f(v)) for k,v in conv.items()}
r['anomaly_coeff_d_da']=-4.0   # = 2 deg omega = 2(2g-2)
r['minusK0']=float(mK0)
r['mismatch_minusK0_minus_value']={k:float(mK0-f(v)) for k,v in conv.items()}
astar=(4*r['O1hat_sq']-mK0)/4; r['a_needed_NOT_A_FIT']=float(astar); r['exp_minus_a_needed']=float(mp.e**(-astar))
r['compare_sqrtpi_sqrt2pi']=[float(mp.sqrt(mp.pi)),float(mp.sqrt(2*mp.pi))]
# (4) horizontal section P=0: (P,P)_Ar = -deg omegahat|_P = -( -2*hFS(0) + a ), hFS(0)=0
r['section_selfint_P0']={k:float(-v) for k,v in conv.items()}
# (5) Tate / dim-1 model: Spec Z -> Spec Z x_Z Spec Z iso, conormal 0 -> derived diag degree 0; self-dual dx <-> ||1||=1, deg=0
r['tate_derived_diag_degree']=0.0
# (6) K0 as Mellin/log-det derivative: GammaR(s)=pi^{-s/2}Gamma(s/2); K0 = 2 (log GammaR)'(1/2)
GR=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)
r['K0']=float(K0); r['2dlogGammaR_half']=float(2*mp.diff(lambda s: mp.log(GR(s)),0.5))
# scale behaviour: degree shifts by a under ||.||->e^{-a}||.||; d/ds log(C*GammaR) is C-invariant; lambda^s factor shifts by log lambda
r['dlog_invariant_under_const']=float(2*mp.diff(lambda s: mp.log(7.3*GR(s)),0.5)-2*mp.diff(lambda s: mp.log(GR(s)),0.5))
r['K0_decomp']={'psi(1/4)':float(mp.digamma(0.25)),'-log pi (from pi^{-s/2}, s-dependent scale)':float(-mp.log(mp.pi))}
json.dump(r,open('arak2003.json','w'),indent=1); print(json.dumps(r,indent=1))

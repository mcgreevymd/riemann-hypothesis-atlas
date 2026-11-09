"""Real interval certificate: no eigenvalues, no complex digamma, no numerical quadrature."""
import mpmath as m, json
iv=m.iv;iv.dps=60
q=lambda n,d=1:iv.mpf(n)/iv.mpf(d)
pi=iv.pi;A=q(347,500);theta=q(3,16)
# Euler's constant enclosure from elementary harmonic/log bounds.
Ng=1000
H=sum((q(1,n) for n in range(1,Ng+1)),q(0))
g0=H-iv.log(q(Ng))-q(1,2*Ng)
# Euler--Maclaurin alternating remainder: 0 < gamma-g0 < 1/(12 Ng^2).
gamma=iv.mpf([g0.a,(g0+q(1,12*Ng**2)).b])
K0=-gamma-pi/2-3*iv.log(q(2))-iv.log(pi)
# A rational finite positive digamma series gives a certified lower bound on K(9).
Nseries=2000; kap=q(9)
partial=sum((2*kap**2/((2*q(j)+q(1,2))*((2*q(j)+q(1,2))**2+kap**2)) for j in range(Nseries)),q(0))
K9partial=K0+partial
# This partial sum's interval encloses the partial sum, not all K(9); omitted terms are positive.
def T(a):
 t=iv.exp(-a/2)
 return iv.log((1+t)/(1-t))/2+iv.atan2(t,q(1))
base=K0+2*T(A/2)
delta=A-iv.log(q(2));Delta=T(delta)+T(A)-2*T(A/2)
a2=iv.log(q(2))/iv.sqrt(q(2))
k0=2*pi/A-A/(4*pi)
kl=2*pi/A-1/(4*k0)
edge_budget=theta*Delta-a2
Wlower=(1-theta)*K9partial+theta*base
# Comparisons of interval endpoints ensure strict inequalities.
assert kl.a>q(9).b
assert edge_budget.a>q(0).b
assert K9partial.a>q(358,1000).b
assert base.a>q(-1527,1000).b
assert Wlower.a>q(45,10000).b
out={'A':'347/500','theta':'3/16','gamma_enclosure':str(gamma),'K0_enclosure':str(K0),'elementary_k_lower':str(kl),'K9_positive_partial_sum_enclosure':str(K9partial),'potential_baseline':str(base),'overlap_width':str(delta),'edge_potential_gain':str(Delta),'prime_weight':str(a2),'edge_budget':str(edge_budget),'W_lower_expression_enclosure':str(Wlower),'claimed_uniform_bound':'W >= (9/2000)||F||^2 for A<=347/500 and F in E0','harmonic_N':Ng,'positive_series_N':Nseries,'all_assertions_passed':True}
print(json.dumps(out,indent=2));open('../logpoincare2044/certify2044.json','w').write(json.dumps(out,indent=2))

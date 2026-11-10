"""R2 test (t2097, scratch only). Tropical Cartier vs current models on the scaling square.
Conventions: log/tropical coords (X,Y). Psi(mu) = (id,psi_mu)_*[R_X], psi_mu: X -> mu X.
Cartier model: Psi(mu) = div f_mu, f_mu = max(Y - mu X, 0); a real-weight 1-cycle in R^2
is recorded by its gradient-jump covector n (n_mu = (-mu,1)); stable intersection
D1.D2 = |det(n1,n2)| (= mixed real Monge-Ampere of the PL potentials, Bernstein normalization).
Pullback of Cartier divisor: n -> G^T n.  Pushforward (G invertible): n -> |det G| G^{-T} n.
"""
import json, math
import numpy as np
import sympy as sp

def n_psi(mu): return np.array([-mu, 1.0])
N_F1 = np.array([1.0, 0.0])   # F1 = {X=c} = div max(X-c,0)  (pt x S)
N_F2 = np.array([0.0, 1.0])   # F2 = {Y=c} = div max(Y-c,0)  (S x pt)
def I(n1, n2): return abs(n1[0]*n2[1]-n1[1]*n2[0])
def G(mu): return np.diag([1.0, mu])
def pull(Gm, n): return Gm.T @ n
def push(Gm, n): return abs(np.linalg.det(Gm))*np.linalg.inv(Gm).T @ n

out = {}
pairs = [(3.0,2.0),(4.0,2.0),(2.5,0.7),(math.e**1.3, math.e**0.4),(math.pi, math.sqrt(2)),(0.3,0.9)]

# --- R1
out["R1_bidegree"] = {str(mu): [I(n_psi(mu),N_F1), I(n_psi(mu),N_F2)] for mu in [0.7,2.0,math.pi]}
# --- pullback G_mu^* Psi(mu) vs Delta
out["pullback"] = {}
for mu in [0.7,2.0,math.pi]:
    pn = pull(G(mu), n_psi(mu))           # = mu*(-1,1)
    out["pullback"][str(mu)] = {"G*Psi(mu) covector": pn.tolist(), "ratio_to_Delta": (pn/n_psi(1.0)).tolist()}
# --- pushforward and projection formula, affine (R^2) part
rows = []
for lam, mu in pairs:
    direct = I(n_psi(lam), n_psi(mu))
    pf = push(G(mu), n_psi(lam/mu))
    proj = I(n_psi(lam/mu), pull(G(mu), n_psi(mu)))
    R2 = mu*I(n_psi(lam/mu), n_psi(1.0))
    m, M = min(lam,mu), max(lam,mu)
    R2sym = m*I(n_psi(M/m), n_psi(1.0))
    # compact tropical P1xP1: bidegree pairing (a,b).(c,d)=ad+bc ; corners: local order of x^lam - x^mu = min
    total = 1*mu + lam*1
    corners = 2*min(lam,mu)
    rows.append(dict(lam=lam, mu=mu, affine_direct=direct, pushforward_equals_Psi_lam=bool(np.allclose(pf, n_psi(lam))),
                     projection_formula=proj, R2_mu_times_PsiDelta=R2, R2_min_form=R2sym,
                     P1xP1_total=total, corners_2min=corners, affine_plus_corners=direct+corners,
                     R2_total=m*(M/m+1)))
out["pairs_cartier"] = rows

# --- numerical check: smoothed mixed Monge-Ampere  int [det(H1+H2)-detH1-detH2]
def softplus_hess(g, gx, gy, eps):
    s = 1/(1+np.exp(-g/eps)); rho = s*(1-s)/eps
    return rho*gx*gx, rho*gx*gy, rho*gy*gy
def mixedMA(n1, n2, c2=(0.0,0.0), eps=0.04, L=2.5, h=0.004):
    x = np.arange(-L, L, h); X, Y = np.meshgrid(x, x, indexing="ij")
    g1 = n1[0]*X + n1[1]*Y
    g2 = n2[0]*(X-c2[0]) + n2[1]*(Y-c2[1])
    a = softplus_hess(g1, n1[0], n1[1], eps); b = softplus_hess(g2, n2[0], n2[1], eps)
    d = lambda A: A[0]*A[2]-A[1]**2
    S = (a[0]+b[0], a[1]+b[1], a[2]+b[2])
    return float(np.sum(d(S)-d(a)-d(b))*h*h)
num = []
for lam, mu in pairs[:4]:
    num.append(dict(lam=lam, mu=mu, MA=mixedMA(n_psi(lam), n_psi(mu)), exact=abs(lam-mu)))
mu = 2.0
fmu_pulled = lambda: None
# pulled-back potential f_mu(X, mu Y) = max(mu Y - mu X, 0): its covector is mu*(-1,1) -> intersect with fibre F1
num.append(dict(check="G2^*Psi(2) . F1 (Delta.F1=1)", MA=mixedMA(pull(G(mu), n_psi(mu)), N_F1, c2=(0.3,0)), exact=mu))
num.append(dict(check="Psi(pi).F2", MA=mixedMA(n_psi(math.pi), N_F2, c2=(0,0.3)), exact=math.pi))
out["numeric_MA"] = num

# --- current models (linear-in-tropical-coordinate Dirac currents)
def dens(n1, n2, eps=0.01, L=2.5, h=0.002):
    x = np.arange(-L, L, h); X, Y = np.meshgrid(x, x, indexing="ij")
    gs = lambda g: np.exp(-g**2/(2*eps**2))/(eps*math.sqrt(2*math.pi))
    return float(np.sum(gs(n1[0]*X+n1[1]*Y)*gs(n2[0]*X+n2[1]*Y))*h*h)
cur = []
for lam, mu in pairs[:4]:
    cur.append(dict(lam=lam, mu=mu, density_pairing=dens(n_psi(lam), n_psi(mu)), exact=1/abs(lam-mu),
                    form_pairing=1.0))
# pullback in density model: delta(mu Y - mu X) = mu^{-1} delta(Y-X); form model delta(g)dg invariant
cur_pull = {"density: G^*Psi(mu)/Delta": "1/mu", "form (delta(g)dg): G^*Psi(mu)/Delta": "1",
            "cartier/Lagerberg (delta(g) dg^d''g): G^*Psi(mu)/Delta": "mu",
            "bidegree density": "(1,1/mu)", "bidegree form": "(1,1)", "bidegree cartier": "(1,mu)"}
# numeric density bidegree
cur_bideg = {str(m): [dens(n_psi(m), N_F1), dens(n_psi(m), N_F2)] for m in [2.0, math.pi]}
out["current_models"] = dict(pairs=cur, pullback=cur_pull, density_bidegree=cur_bideg)

# --- function field sanity: P1/F_q, Gamma_k.Gamma_l = q^l (q^{k-l}+1); corners 0,inf mult q^l each
x = sp.symbols('x')
ff = []
for q,k,l in [(2,3,1),(3,2,1),(5,2,1)]:
    lhs = sp.Poly(x**(q**k) - x**(q**l), x, modulus=q)
    rhs = sp.Poly((x**(q**(k-l)) - x)**(q**l), x, modulus=q)
    ff.append(dict(q=q,k=k,l=l, frob_binomial_identity=lhs==rhs, ord_at_0=q**l,
                   total=q**k+q**l, interior_points_Fq_star=q**(k-l)-1, interior_mult_total=q**k-q**l))
out["function_field_P1"] = ff

# --- half-density / Toeplitz
def K_cartier(u,v): # weighted pairing e^{-(u+v)/2} Psi(e^u).Psi(e^v), compact total
    return math.exp(-(u+v)/2)*(math.exp(u)+math.exp(v))
tp = []
for (u,v) in [(0.2,1.5),(1.0,2.3),(-0.4,0.9),(2.0,0.7)]:
    a = abs(u-v)
    tp.append(dict(u=u,v=v,a=a, cartier_total=K_cartier(u,v), two_cosh=2*math.cosh(a/2),
                   cartier_affine=math.exp(-(u+v)/2)*abs(math.exp(u)-math.exp(v)), two_sinh=2*math.sinh(a/2),
                   density_weighted_plus=math.exp((u+v)/2)/abs(math.exp(u)-math.exp(v)), inv_two_sinh=1/(2*math.sinh(a/2)),
                   k_inf=math.exp(-a/2)/(1-math.exp(-2*a))))
out["toeplitz"] = tp
# weight forced: w(u)w(v)(e^u+e^v) Toeplitz => w = c e^{-u/2}; test w=1 fails
out["weight_test_w1"] = [ (1+math.exp(1.0)), (math.exp(1)+math.exp(2)) ]  # a=1 at (0,1) and (1,2): not equal

# --- model (b): torus (R/LZ)^2, L=log p
tor = []
for p in [2,3,5]:
    L = math.log(p)
    for mu in [1.5, math.pi, p**2]:
        s = math.log(mu)/L
        tor.append(dict(p=p, mu=mu, translation_class=(1,1), Psi_dot_Delta=0,
                        coincident_with_Delta=abs(s-round(s))<1e-12))
    # integer covering t -> n t ( only integer n descend): fixed points of t->n t on circle = |n-1|
    for n in [2,3,5]:
        tt = np.linspace(0, L, 200001)[:-1]
        f = ((n-1)*tt) % L
        cnt = int(np.sum(np.abs(np.diff(f)) > L/2)) + (1 if f[0]==0 else 0)
        tor.append(dict(p=p, covering_n=n, fixed_points=cnt, expected=abs(n-1)))
out["model_b_torus"] = tor
# CC slope lattice index [H_p : h H_p] for h in H_p^+ : prime-to-p part of numerator
def idx(h, p):
    h = sp.Rational(h); num = h.p
    while num % p == 0: num //= p
    return num
out["model_b_CC_index"] = [dict(p=p, h=str(h), index=idx(h,p), deg_CC_preserved=True)
                           for p,h in [(2,3),(2,sp.Rational(3,4)),(3,9),(3,2),(5,sp.Rational(7,25))]]
json.dump(out, open("r2trop2097.json","w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))

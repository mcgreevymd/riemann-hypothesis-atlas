# exact small examples: e_n = v_p |X/omega_n X|, omega_n=(1+T)^{p^n}-1 ; regularity of Lambda/(f)
import sympy as sp
p=3
def vp(x):
    x=sp.Integer(x); 
    if x==0: return sp.oo
    return sp.multiplicity(p,x)
def e_cyclic_root(a,n): # Lambda/(T-a): X/omega_n = Z_p/omega_n(a)
    return vp((1+a)**(p**n)-1)
rows=[]
for a in [p,-p,p**2,p+p**2]:
    rows.append((a,[e_cyclic_root(a,n) for n in range(6)]))
for a,e in rows: print("Lambda/(T-%s): e_n="%a,e,"  Delta e=",[e[i+1]-e[i] for i in range(5)])
# Lambda/(p): X/omega_n = F_p[T]/(T^{p^n}) -> e_n = p^n ; Delta = (p-1)p^n
print("Lambda/(p): e_n=",[p**n for n in range(6)])
# Lambda/(T^2-p) and Lambda/(T^2-p^3): X/omega_n = Z_p[x]/(x^2-c, omega_n(x)) ; size = |Res(x^2-c, omega_n)|_p^-1
x=sp.symbols('x')
for c in [p,p**3]:
    e=[vp(sp.resultant(x**2-c,(1+x)**(p**n)-1,x)) for n in range(5)]
    print("Lambda/(T^2-%d): e_n="%c,e," Delta=",[e[i+1]-e[i] for i in range(4)])
# pseudo-isomorphism: add finite Lambda/(p,T)=F_p -> nu+1
print("Lambda/(T-p) + F_p: e_n=",[e_cyclic_root(p,n)+1 for n in range(6)])
# regularity of support: class of f in m/m^2 (coeffs of p and T mod p)
def grad(f):  # f polynomial in T with Z coefficients, f in m assumed
    c0=sp.Poly(f,T).coeff_monomial(1); c1=sp.Poly(f,T).coeff_monomial(T)
    return (sp.Integer(c0)//p % p if c0%p==0 else 'unit', c1 % p)
T=sp.symbols('T')
for f in [T-p, T**2-p, T**2-p**3, p*T, T**2, p**2]:
    g=grad(f); print("f=",f," class in m/m^2 =",g, " Lambda/(f) regular:", g!=(0,0))

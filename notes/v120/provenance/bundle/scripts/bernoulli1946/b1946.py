import sympy as sp, mpmath as mp, json
from sympy import bernoulli, Rational, factorial, factorint, numer, denom
out={}
def dimS(k): 
    if k%2 or k<4: return 0
    d=k//12 + (0 if k%12==2 else 1); return d-1   # dim M_k - 1
rows=[]
for k in range(4,34,2):
    B=bernoulli(k); c=-B/(2*k)
    rows.append(dict(k=k,B=str(B),num_B=str(factorint(abs(numer(B)))),G_const=str(c),num_G_const=str(factorint(abs(numer(c)))),
                     dimS=dimS(k),cancels=str({p:e for p,e in factorint(abs(numer(B))).items() if numer(c)%p})))
out['table']=rows
out['B10/10 vs B2/2 mod 5 (Kummer, 10≡2 mod 4)']=[str(bernoulli(10)/10),str(bernoulli(2)/2),
    int((numer(bernoulli(10)/10)*pow(int(denom(bernoulli(10)/10)),-1,5))%5),int((numer(bernoulli(2)/2)*pow(int(denom(bernoulli(2)/2)),-1,5))%5)]
# Hirzebruch: x/tanh x = sum 2^{2j} B_{2j} x^{2j}/(2j)! ; coefficient of p_j in L_j: s_j = 2^{2j}(2^{2j-1}-1)|B_{2j}|/(2j)!
x=sp.symbols('x'); ser=sp.series(x/sp.tanh(x),x,0,12).removeO()
out['x/tanh x']=str(ser)
out['s_j']={j:str(2**(2*j)*(2**(2*j-1)-1)*abs(bernoulli(2*j))/factorial(2*j)) for j in range(1,7)}
# Kervaire–Milnor |bP_{4k}| = a_k 2^{2k-2}(2^{2k-1}-1) num(4B_{2k}/k), a_k=1 (k even), 2 (k odd)
out['bP_4k']={4*k:int((1 if k%2==0 else 2)*2**(2*k-2)*(2**(2*k-1)-1)*numer(4*abs(bernoulli(2*k))/k)) for k in range(2,7)}
# Binet: psi(z) = log z - 1/(2z) - 2∫ t/((t^2+z^2)(e^{2πt}-1)) dt, Re z>0 ; Stirling enveloping (real z)
for xv in [0,3,10]:
    z=mp.mpf(1)/4+1j*mp.mpf(xv)/2
    I=mp.quad(lambda t: t/((t**2+z**2)*(mp.e**(2*mp.pi*t)-1)),[0,1,mp.inf])
    out[f'Binet z=1/4+{xv}i/2']=[str(mp.nstr(mp.digamma(z),12)),str(mp.nstr(mp.log(z)-1/(2*z)-2*I,12))]
out['psi(1/4) = -gamma - pi/2 - 3log2']=[float(mp.digamma(0.25)),float(-mp.euler-mp.pi/2-3*mp.log(2))]
print(json.dumps(out,indent=1)); json.dump(out,open('b1946.json','w'),indent=1)

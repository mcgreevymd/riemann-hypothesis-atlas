# Exact check: archimedean spring symbol = complete-Bernstein (Stieltjes) sum = DtN of positive KK tower
import mpmath as mp, json
mp.mp.dps=30
k=lambda a: mp.e**(-a/2)/(1-mp.e**(-2*a))
spring=lambda x: mp.quad(lambda a:k(a)*(2-2*mp.cos(x*a)),[0,1,10,mp.inf])
digam=lambda x: mp.re(mp.digamma(mp.mpf(1)/4+1j*x/2))-mp.digamma(mp.mpf(1)/4)
stieltjes=lambda x: mp.nsum(lambda n: x**2/((n+mp.mpf(1)/4)*((2*n+mp.mpf(1)/2)**2+x**2)),[0,mp.inf])
out=[]
for x in [0.3,1,2.5,7,14.1347]:
    r=dict(x=x,spring=float(spring(x)),digamma=float(digam(x)),stieltjes=float(stieltjes(x))); out.append(r); print(r)
# tower minimization check for one mode: c*l/(l+d) = (c/d)*min_w (l|1-w|^2 + d|w|^2)
l,d,c=mp.mpf(3),mp.mpf(6.25),mp.mpf(0.8)
wopt=l/(l+d); out.append(dict(single_mode_lhs=float(c*l/(l+d)),rhs=float(c/d*(l*(1-wopt)**2+d*wopt**2))))
K0=mp.digamma(0.25)-mp.log(mp.pi); out.append(dict(K0=float(K0)))
print(out[-2:]); json.dump(out,open('kk_tower.json','w'),indent=1)

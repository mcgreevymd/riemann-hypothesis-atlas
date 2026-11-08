import mpmath as mp, sympy as sp, json, math
def lam(n):
    f=sp.factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
out={}
for A in [1.0,2.0,3.0]:
    ns=[n for n in range(2,int(math.exp(A))+1) if lam(n)>0 and math.log(n)<A]
    m=lambda x: float(mp.re(mp.digamma(0.25+0.5j*x))-mp.log(mp.pi))-2*sum(lam(n)/math.sqrt(n)*math.cos(x*math.log(n)) for n in ns)
    MA=-float(mp.digamma(0.25)-mp.log(mp.pi))+2*sum(lam(n)/math.sqrt(n) for n in ns)
    xs=[i*0.01 for i in range(0,6001)]; vals=[m(x) for x in xs]
    zeros=[round(xs[i],2) for i in range(len(xs)-1) if vals[i]*vals[i+1]<0]
    out[f'A={A}']=dict(M_A=MA,minus_m0=-m(0),first_zero_velocity_x=zeros[:6],min_m=min(vals))
print(json.dumps(out,indent=1)); json.dump(out,open('zv1941.json','w'),indent=1)

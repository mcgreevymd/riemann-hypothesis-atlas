from sympy import divisor_sigma as s
N=40
def mul(a,b): return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(N)]
def ser(c0,c,k): return [c0]+[c*int(s(n,k)) for n in range(1,N)]
P=ser(1,-24,1); Q=ser(1,240,3); R=ser(1,-504,5)
th=lambda f:[n*f[n] for n in range(N)]
D=[0]*N; D[1]=1
for n in range(1,N):
    for _ in range(24): D=[D[i]-(D[i-n] if i>=n else 0) for i in range(N)]
z=lambda f: all(abs(x)<1e-9 for x in f)
lin=lambda *terms: [sum(c*t[i] for c,t in terms) for i in range(N)]
print('thetaP',z(lin((12,th(P)),(-1,mul(P,P)),(1,Q))))
print('thetaQ',z(lin((3,th(Q)),(-1,mul(P,Q)),(1,R))))
print('thetaR',z(lin((2,th(R)),(-1,mul(P,R)),(1,mul(Q,Q)))))
print('Q3-R2=1728Delta',z(lin((1,mul(mul(Q,Q),Q)),(-1,mul(R,R)),(-1728,D))))
print('thetaDelta=P Delta',z(lin((1,th(D)),(-1,mul(P,D)))))
print('Serre D4Q=-R/3',z(lin((3,th(Q)),(-1,mul(P,Q)),(1,R))))
print('Serre D12 Delta=0',z(lin((12,th(D)),(-12,mul(P,D)))))

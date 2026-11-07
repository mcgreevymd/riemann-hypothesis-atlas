import numpy as np, sympy as sp
# (1) prime isometries on l2(N), truncated N; test on vectors supported on n<=N//p^2 to avoid edge
N=3000; p=3; q=5
def S(k,v):
    w=np.zeros(N+1,complex); idx=np.arange(1,N//k+1); w[idx*k]=v[idx]; return w
def Ss(k,v):
    w=np.zeros(N+1,complex); idx=np.arange(1,N//k+1); w[idx]=v[idx*k]; return w
logn=np.log(np.arange(N+1)+1e-300); logn[0]=0
H=lambda v: logn*v
rng=np.random.default_rng(0); v=np.zeros(N+1); m=N//(p*p*q*q); v[1:m+1]=rng.normal(size=m)
print('[H,S_p]-log p S_p :',np.abs(H(S(p,v))-S(p,H(v))-np.log(p)*S(p,v)).max())
print('S_p*S_p - I       :',np.abs(Ss(p,S(p,v))-v).max())
P=lambda k,w: np.where(np.arange(N+1)%k==0,w,0)
print('S_pS_p* - P_p     :',np.abs(S(p,Ss(p,v))-P(p,v)).max())
print('S_p*S_q - S_qS_p* :',np.abs(Ss(p,S(q,v))-S(q,Ss(p,v))).max())
X=lambda w:(S(p,w)+Ss(p,w))/2; Y=lambda w:(S(p,w)-Ss(p,w))/(2j)
print('[X,Y]+(i/2)(I-P_p):',np.abs(X(Y(v))-Y(X(v))+0.5j*(v-P(p,v))).max())
print('[H,X]-i log p Y   :',np.abs(H(X(v))-X(H(v))-1j*np.log(p)*Y(v)).max())
# Gibbs beta>1: <S_n S_n*>_beta = n^-beta
beta=2.0; n=np.arange(1,N+1); w=n**-beta; Z=w.sum()
print('phi_beta(P_p) vs p^-beta:',(w[n%p==0].sum()/Z), p**-beta)
# (2) affine pair on log line: [D, e^u] = -i e^u ; scaling generator vs x-position
u=sp.symbols('u',real=True); g=sp.Function('g')(u); D=lambda h:-sp.I*sp.diff(h,u)
print('[D,e^u]g + i e^u g =',sp.simplify(D(sp.exp(u)*g)-sp.exp(u)*D(g)+sp.I*sp.exp(u)*g))
# (3) sl2 Lefschetz on H*(P^1 x P^1) toy: L = cup with ample h1+h2 ; degrees 0..4 basis 1,h1,h2,h1h2
L=np.zeros((4,4)); L[1,0]=1;L[2,0]=1;L[3,1]=1;L[3,2]=1     # 1->h1+h2, h1->h1h2, h2->h1h2
Hd=np.diag([-2,0,0,2]); Lam=np.zeros((4,4)); Lam[0,1]=Lam[0,2]=1; Lam[1,3]=Lam[2,3]=1
print('[H,L]-2L',np.abs(Hd@L-L@Hd-2*L).max(),' [L,Lam]-H',np.abs(L@Lam-Lam@L-Hd).max())
# Hodge index on primitive H^2: Q(a,b)=intersection, primitive = ker L on H^1,1 -> h1-h2, (h1-h2)^2=-2<0 ; ample (h1+h2)^2=2>0
I=np.array([[0,1],[1,0]]); print('ample^2',np.array([1,1])@I@[1,1],' primitive^2',np.array([1,-1])@I@[1,-1])

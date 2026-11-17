"""t2251 spec (J.W./Claude): window u in [-r/2,r/2], basis phi_n = sqrt(2/r) sin(n pi (u+r/2)/r), n=1..N.
Q = K0 I + E_arch + sum_{n<e^r} a_n (-S(log n)),  a_n = Lambda(n)/sqrt(n)
E_arch_ij = int_0^inf k(t)[2 d_ij - S_ij(t)] dt  (= (1/2)∫∫(f(u)-f(v))^2 J(u-v) incl. killing, f extended by 0),
k(t)=J(t)=e^{-t/2}/(1-e^{-2t}),  S_ij(t)=<phi_i,tau_t phi_j>+<phi_j,tau_t phi_i> (closed form, zero for t>=r).
QW = Q + c+ c-^T + c- c+^T, c±_n = ∫phi_n e^{±u/2}.  Moments: k = 1/(2t) + h(t), 1/(2t) part via Si/Ci exactly,
h part by composite Gauss-Legendre.  usage: python sine.py r N dps [nodes_per_piece piece_len]"""
import sys, json, time, math
import mpmath as mp
def primes_atoms(r):
    out=[]
    for n in range(2,int(math.exp(r))+2):
        m=n;p=2;P=None
        while p*p<=m:
            if m%p==0:
                while m%p==0: m//=p
                P=p if m==1 else -1; break
            p+=1
        if P is None: P=n   # n prime
        if P>0 and mp.log(n)<r: out.append((mp.log(n),mp.log(P)/mp.sqrt(n),n))
    return out
ALPHA=None
def kfun(t): return mp.exp(-ALPHA*t)/(-mp.expm1(-2*t))
def hfun(t): return kfun(t)-1/(2*t)
def run(rs,N,dps,npc=None,plen=None,chi=None):
    global ALPHA
    t0=time.time(); mp.mp.dps=dps; r=mp.mpf(rs)
    if chi is None:
        ALPHA=mp.mpf(1)/2; K0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
    else:  # odd real character mod 4: Gamma_R(s+1), conductor 4
        ALPHA=mp.mpf(3)/2; K0=mp.digamma(mp.mpf(3)/4)+mp.log(4/mp.pi)
    ks=[n*mp.pi/r for n in range(1,N+1)]
    # composite Gauss-Legendre on [0,r]
    plen=mp.mpf(plen or '0.25'); npieces=int(mp.ceil(r/plen)); hl=r/npieces
    npc=npc or max(60, int(N*math.pi*float(hl)/float(r)/2)+int(dps*0.9)+20)
    # use mpmath gauss_quadrature for Legendre nodes
    xs,ws=mp.gauss_quadrature(npc,'legendre')
    T=[];Wq=[]
    for p in range(npieces):
        a=p*hl
        for x,w in zip(xs,ws): T.append(a+hl*(x+1)/2); Wq.append(w*hl/2)
    Is=[mp.mpf(0)]*N; Ic=[mp.mpf(0)]*N; Itc=[mp.mpf(0)]*N; H0=mp.mpf(0)
    th=mp.pi/r
    for t,w in zip(T,Wq):
        hw=hfun(t)*w; H0+=hw
        e1=mp.expjpi(t/r) ; e=e1
        for n in range(N):
            c,s=e.real,e.imag
            Is[n]+=hw*s; Ic[n]+=hw*c; Itc[n]+=hw*t*c
            e*=e1
    # full moments with 1/(2t) part exact
    def Isin(n):  # ∫_0^r k sin(a t)
        a=ks[n]; return mp.si(a*r)/2+Is[n]
    tail=mp.nsum(lambda m: mp.exp(-(2*m+ALPHA)*r)/(2*m+ALPHA),[0,mp.inf])
    IS=[Isin(n) for n in range(N)]
    Diag=[]
    for n in range(N):
        a=ks[n]; ar=a*r
        cin=mp.euler+mp.log(ar)-mp.ci(ar)
        one_minus_cos=cin/2+(H0-Ic[n])           # ∫k(1-cos at)
        tcos_minus=(mp.sin(ar)-mp.si(ar))/(2*a) + (Itc[n]-Is[n]/a)   # ∫k[t cos at - sin(at)/a]
        Diag.append(2*one_minus_cos+(2/r)*tcos_minus)
    def Smat_int_off(i,j):  # ∫_0^r k S_ij for i!=j same parity
        a,b=ks[i],ks[j]; return (2/r)*((IS[i]+IS[j])/(a+b)-(IS[i]-IS[j])/(a-b))
    def S_at(i,j,t):
        a,b=ks[i],ks[j]
        if i==j: return (2/r)*((r-t)*mp.cos(a*t)+mp.sin(a*t)/a)
        if (i-j)%2: return mp.mpf(0)
        return (2/r)*((mp.sin(a*t)+mp.sin(b*t))/(a+b)-(mp.sin(a*t)-mp.sin(b*t))/(a-b))
    atoms=primes_atoms(r)
    if chi is not None: atoms=[(L,an*chi(n),n) for L,an,n in atoms]
    SC=[([mp.sin(k*L) for k in ks],[mp.cos(k*L) for k in ks],L,an) for L,an,_ in atoms]
    def S_atom(i,j,sn,cs,L):
        a,b=ks[i],ks[j]
        if i==j: return (2/r)*((r-L)*cs[i]+sn[i]/a)
        return (2/r)*((sn[i]+sn[j])/(a+b)-(sn[i]-sn[j])/(a-b))
    Q=mp.matrix(N,N)
    for i in range(N):
        for j in range(i,N):
            if (i-j)%2: continue
            v=(K0+Diag[i]+2*tail) if i==j else -Smat_int_off(i,j)
            for sn,cs,L,an in SC: v-=an*S_atom(i,j,sn,cs,L)
            Q[i,j]=v; Q[j,i]=v
    cp=[];cm=[]
    for n in range(N):
        k=ks[n]; sg=(-1)**(n+1)
        for al,lst in ((mp.mpf(1)/2,cp),(-mp.mpf(1)/2,cm)):
            val=(mp.exp(al*r)*(-k*sg)+k)/(al**2+k**2)*mp.exp(-al*r/2)*mp.sqrt(2/r); lst.append(val)
    QW=Q.copy()
    for i in range(N):
        for j in range(N): QW[i,j]+=cp[i]*cm[j]+cm[i]*cp[j]
    return Q,QW,cp,cm,ks
if __name__=='__main__':
    a=sys.argv; res=run(a[1],int(a[2]),int(a[3]),int(a[4]) if len(a)>4 else None,a[5] if len(a)>5 else None)
    print(json.dumps(res),flush=True)

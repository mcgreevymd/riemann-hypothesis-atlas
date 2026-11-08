import numpy as np, json
out={}
# NS-type lattice form I = U ⊕ (-I_k): U=[[0,1],[1,0]] spanned by fibres f1,f2 (product of curves), k transverse
k=3; I=np.zeros((2+k,2+k)); I[0,1]=I[1,0]=1; I[2:,2:]=-np.eye(k)
out['sig_I']=[int((np.linalg.eigvalsh(I)>0).sum()),int((np.linalg.eigvalsh(I)<0).sum())]
def gA(A):
    IA=I@A; return 2*np.outer(IA,IA)/(A@I@A)-I
for t in [0.0,0.7]:
    A=np.zeros(2+k); A[0]=np.exp(t); A[1]=np.exp(-t)          # boosted 'observers' in the ample cone of U
    th=2*np.outer(A,A@I)/(A@I@A)-np.eye(2+k)                  # reflection fixing A, -1 on A-perp
    out[f't={t}']=dict(IAA=float(A@I@A),eig_gA=np.linalg.eigvalsh(gA(A)).round(6).tolist(),
        gA_eq_I_theta=float(np.abs(gA(A)-I@th).max()),theta_sq=float(np.abs(th@th-np.eye(2+k)).max()),theta_preserves_I=float(np.abs(th.T@I@th-I).max()))
# swap involution f1<->f2 fixes A=f1+f2 and is the Cartan involution of U at t=0
S=np.eye(2+k); S[[0,1]]=S[[1,0]]
out['swap_is_theta_t0']=float(np.abs(S[:2,:2]-(2*np.outer([1,1],np.array([1,1])@I[:2,:2])/2-np.eye(2))).max())
# boundary pole form P(a,b)=2Re(a conj b) on (ev0,ev1): same as U; FE swap sigma gives P(x,sigma x)=|a|^2+|b|^2
a,b=0.3+0.4j,-1.1+0.2j; P=lambda x,y: (x[0]*np.conj(y[1])+x[1]*np.conj(y[0])).real
out['P_x_sigmax']=[float(P((a,b),(b,a))),abs(a)**2+abs(b)**2]
print(json.dumps(out,indent=1)); json.dump(out,open('observer1928.json','w'),indent=1)

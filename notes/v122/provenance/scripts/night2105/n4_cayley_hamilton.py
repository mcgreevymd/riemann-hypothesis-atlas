"""N4: near-null directions = numerical-equivalence relations (Cayley-Hamilton for Frobenius), function-field template, exact.
C/F_q genus g. beta_i = alpha_i/sqrt q (|beta|=1). W_ff(m) = sum_i beta_i^m. Window k = 0..K: T_kl = W_ff(k-l) = (V V^*)_kl, V_ik = beta_i^k.
Claims checked: rank T = min(K+1, 2g); ker T = coefficient vectors of multiples of Ltilde(x) = prod (x - beta_i)  (Cayley-Hamilton);
and G - Pmat = -T for the normalized intersection Gram of Frobenius graphs (G_kl = q^{-|k-l|/2} N_|k-l|, N_0 = 2-2g; Pmat = trivial lattice),
so a Toeplitz-null c is exactly a numerically trivial primitive class sum c_k q^{-k/2} Gamma_k (Hodge index => definite => null = 0)."""
import json, numpy as np
def counts_from_L(q,Lc,M):
    al=np.roots(Lc[::-1])  # L(T)=sum Lc[j]T^j, roots are 1/alpha
    al=1/al
    return al,[int(round((q**m+1-np.sum(al**m)).real)) for m in range(1,M+1)]
cases=[]
# genus 1: y^2=x^3+x+1 / F5, N1=9 -> a=q+1-N1=-3, L=1+aT... careful: L(T)=1-(q+1-N1)T+qT^2
q=5; N1=9; L=[1,-(q+1-N1),q]
# genus 2: y^2=x^5+2x+1 / F3, N1=7,N2=15 (prime2087 brute force)
q2=3; n1,n2=7,15; a1=n1-q2-1; a2=(n2-q2**2-1+a1**2)//2; L2=[1,a1,a2,q2*a1,q2**2]
out=[]
for name,q,Lc,g,Nexp in [('genus1 y^2=x^3+x+1/F5',5,L,1,[9,27,108,675]),('genus2 y^2=x^5+2x+1/F3',3,L2,2,[7,15,19,83,232,795])]:
    al,N=counts_from_L(q,Lc,len(Nexp))
    beta=al/np.sqrt(q)
    Wff=lambda m: np.sum(beta**m).real
    for K in [2*g-1,2*g,2*g+3,12]:
        T=np.array([[Wff(k-l) for l in range(K+1)] for k in range(K+1)])
        ev=np.linalg.eigvalsh(T); rank=int(np.sum(ev>1e-9))
        Lt=np.poly(beta)  # coefficients of prod(x-beta), highest first
        Lt=Lt[::-1]       # lowest first
        res=0.
        for s in range(0,K+1-2*g):
            c=np.zeros(K+1,complex); c[s:s+2*g+1]=Lt; res=max(res,np.linalg.norm(T@c))
        # intersection Gram check
        Nn=lambda m: (2-2*g) if m==0 else int(round((q**m+1-np.sum(al**m)).real))
        G=np.array([[q**(-abs(k-l)/2)*Nn(abs(k-l)) for l in range(K+1)] for k in range(K+1)])
        P=np.array([[q**((k-l)/2)+q**((l-k)/2) for l in range(K+1)] for k in range(K+1)])
        out.append(dict(curve=name,K=K,window=K+1,rank=rank,expected=min(K+1,2*g),kernel_dim=K+1-rank,max_resid_Ltilde_shifts=float(res),
                        G_minus_P_plus_T=float(np.abs(G-P+T).max()),counts=N,counts_expected=Nexp,min_eig_T=float(ev[0])))
        print(out[-1])
json.dump(dict(note='exact identities checked in double precision',rows=out),open('n4_cayley_hamilton.json','w'),indent=1)

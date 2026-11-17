"""Lemma 189/191/192 tests (t2253). Sine basis from hp2251/sine.py (build.py = same assembly, returns Q,QW,c+,c-).
Everything via parity eigendecompositions of Q + secular equations (exact for rank-one / codim-one problems)."""
import sys, json, time
import mpmath as mp
import build
def bisect(f, lo, hi, it=None, incr=True):
    it = it or int(mp.mp.prec*1.1)+20
    for _ in range(it):
        mid=(lo+hi)/2; v=f(mid)
        if (v<0)==incr: lo=mid
        else: hi=mid
    return (lo+hi)/2
def eig(B):
    E,U=mp.eigsy(B); idx=sorted(range(len(E)),key=lambda q:E[q]); return [E[q] for q in idx],[[U[a,q] for a in range(len(E))] for q in idx]
def sub(M,idx):
    B=mp.matrix(len(idx),len(idx))
    for a,i in enumerate(idx):
        for b,j in enumerate(idx): B[a,b]=M[i,j]
    return B
def main(rs,N,dps,chi=None):
    t0=time.time()
    Q,QW,cp,cm,ks=build.run(rs,N,dps,chi=chi)
    ev=list(range(0,N,2)); od=list(range(1,N,2))  # index even <-> n odd <-> even function
    Le,Ue=eig(sub(Q,ev)); Lo,Uo=eig(sub(Q,od))
    c=[cp[i] for i in ev]; s=[cp[i] for i in od]
    chk=max([abs(cp[i]-cm[i]) for i in ev]+[abs(cp[i]+cm[i]) for i in od])
    ce=[mp.fdot(u,c)**2 for u in Ue]; so=[mp.fdot(u,s)**2 for u in Uo]
    out=dict(r=rs,N=N,dps=dps,chi=bool(chi),parity_check=mp.nstr(chk,3))
    allL=sorted([(x,'e') for x in Le]+[(x,'o') for x in Lo],key=lambda t:t[0])
    out['Q_low']=[mp.nstr(x,8)+p for x,p in allL[:3]]; out['Q_nneg']=sum(1 for x,_ in allL if x<0)
    if chi is None:
        # QW even ground state e0: 1+2 sum ce/(Le-mu)=0 on (Le0,Le1)
        g=lambda mu: 1+2*mp.fsum(w/(l-mu) for w,l in zip(ce,Le))
        e0=bisect(g,Le[0],Le[1])
        h=lambda mu: 1-2*mp.fsum(w/(l-mu) for w,l in zip(so,Lo))
        lo=Lo[0]-1
        while h(lo)<0: lo=2*lo-1
        o0=bisect(h,lo,Lo[0],incr=False)
        S=h(e0) if e0<Lo[0] else None
        out.update(QW_e0=mp.nstr(e0,8),QW_o0=mp.nstr(o0,8),even_lt_odd=bool(e0<o0),
                   S_scalar=(mp.nstr(S,10) if S is not None else 'e0>=minspec(Q_odd)'),
                   S_terms=dict(two_s_Rs=mp.nstr(1-S,10) if S is not None else None))
        # min of Q on ker C+ (= W there): sum v_k^2/(l_k-mu)=0 between lowest two overall eigenvalues
        pairs=[(l,w) for l,w in zip(Le,ce)]+[(l,w) for l,w in zip(Lo,so)]
        pairs.sort(key=lambda t:t[0])
        f=lambda mu: mp.fsum(w/(l-mu) for l,w in pairs)
        kp=bisect(f,pairs[0][0],pairs[1][0])
        # E0: even part min Q_e on ker c ; odd part min Q_o on ker s
        fe=lambda mu: mp.fsum(w/(l-mu) for l,w in zip(Le,ce)); E0e=bisect(fe,Le[0],Le[1])
        fo=lambda mu: mp.fsum(w/(l-mu) for l,w in zip(Lo,so)); E0o=bisect(fo,Lo[0],Lo[1])
        out.update(kerCplus_min=mp.nstr(kp,8),E0_min=mp.nstr(min(E0e,E0o),8),E0_min_par=('e' if E0e<E0o else 'o'),
                   ratio_kerC_over_o0=mp.nstr(kp/o0,8))
        # overlap of Q ground state (even) with cosh(u/2) direction (coefficients c = <phi,cosh>)
        nc=mp.sqrt(mp.fsum(x**2 for x in c)); ov=abs(mp.fdot(Ue[0],c))/nc
        rr=mp.mpf(rs); cosh_norm2=(mp.sinh(rr/2)+rr/2)  # ∫_{-r/2}^{r/2} cosh^2(u/2) du
        out.update(groundQ_cosh_overlap=mp.nstr(ov,10),cosh_coeff_capture=mp.nstr(nc**2/cosh_norm2,8),
                   cosh_weight_on_ground=mp.nstr(ce[0]/nc**2,10))
    else:
        out['Q_e_low']=[mp.nstr(x,8) for x in Le[:2]]; out['Q_o_low']=[mp.nstr(x,8) for x in Lo[:2]]
        # ground state sign changes
        u0=Ue[0] if Le[0]<Lo[0] else Uo[0]; idx=ev if Le[0]<Lo[0] else od
        r=mp.mpf(rs); us=[-r/2+r*mp.mpf(i)/1000 for i in range(1,1000)]
        vals=[mp.fsum(u0[a]*mp.sin(ks[i]*(u+r/2)) for a,i in enumerate(idx)) for u in us]
        sg=[v>0 for v in vals if v!=0]; out['ground_parity']='e' if Le[0]<Lo[0] else 'o'
        out['ground_sc']=sum(1 for x,y in zip(sg,sg[1:]) if x!=y)
    out['time']=round(time.time()-t0,1)
    return out
def chi4(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
if __name__=='__main__':
    a=sys.argv
    print(json.dumps(main(a[1],int(a[2]),int(a[3]),chi4 if len(a)>4 and a[4]=='chi4' else None)),flush=True)

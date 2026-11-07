# Verma module Gram via commutation: states = words of negative modes acting on |h>; <h| = vacuum dual
import sympy as sp
from functools import lru_cache
h,c=sp.symbols('h c')
def comm(m,n): # [L_m,L_n] = (m-n)L_{m+n} + c/12 (m^3-m) δ_{m+n}
    return (m-n), sp.Rational(1,12)*c*(m**3-m) if m+n==0 else 0
@lru_cache(None)
def apply(m,word):  # L_m acting on L_{word}|h>, word tuple of negative ints; returns dict word->coef (normal-ordered words, nonincreasing order not needed)
    if not word:
        if m>0: return {}
        if m==0: return {():h}
        return {(m,):1}
    n=word[0]; rest=word[1:]
    if m<0 and m<=n: return {(m,)+word:1}   # keep ordering L_{-a}...: allow
    out={}
    # L_m L_n rest = L_n L_m rest + [L_m,L_n] rest
    for w,cf in apply(m,rest).items():
        for w2,cf2 in apply(n,w).items(): out[w2]=out.get(w2,0)+cf*cf2
    a,z=comm(m,n)
    if a!=0:
        for w,cf in apply(m+n,rest).items(): out[w]=out.get(w,0)+a*cf
    if z!=0: out[rest]=out.get(rest,0)+z
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}
def ip(w1,w2): # <h| L_{w1}^† L_{w2}|h>, L_n^†=L_{-n}
    state={w2:1}
    for m in w1:  # w1 = (a1,a2,..) meaning L_{a1}L_{a2}..; adjoint applies -a_k in order a1 first
        new={}
        for w,cf in state.items():
            for w3,cf3 in apply(-m,w).items(): new[w3]=new.get(w3,0)+cf*cf3
        state=new
    return sp.expand(state.get((),0))
for n in (1,2,3): print('norm L_-%d|h> ='%n, ip((-n,),(-n,)), ' expected', sp.expand(2*n*h+c*(n**3-n)/12))
B=[(-2,),(-1,-1)]
G=sp.Matrix(2,2,lambda i,j:ip(B[i],B[j])); print('level-2 Gram',G,' det',sp.factor(G.det()))
print(' h=-1 (string level 2, intercept 1): det =',sp.factor(G.det().subs(h,-1)))
v=sp.Matrix([1,sp.Rational(3,2)]); print(' chi=(L_-2+3/2 L_-1^2)|-1>: norm',sp.factor((v.T*G.subs(h,-1)*v)[0]))
print(' L1 chi, L2 chi coefficients:',[apply(1,(-2,)),apply(1,(-1,-1))])

"""N1: the determinant wall is the product formula.
For psi = x -> mu x with mu = p^k (R1 slope), every real chart gives |det(1 - dpsi)|_inf = p^k - 1 per fixed point.
(i) p^k - 1 = #Fix(x -> p^k x on R/Z) = #G_m(F_{p^k}) (Lefschetz on H*(G_m): weights 0 and 2 only);  1 + p^k = #P^1(F_{p^k}).
(ii) half-density: e^{-u/2}(e^u + 1) = 2cosh(u/2) = h_sym,  e^{-u/2}(e^u - 1) = 2sinh(u/2) = h_asym  (u = k log p).
(iii) product formula: log|1-p^k|_inf = sum_{l | p^k-1} v_l log l ; |1-p^k|_p = 1. So the chart determinant is carried by the
     OTHER primes l (where p^k = 1 mod l), never by p. Same cancellation as prime2087 section 3 (finite 2log(n-1) vs archimedean -2log(n-1))."""
import json, math, sympy
rows=[];maxerr=0
for p in sympy.primerange(2,60):
    for kk in range(1,7):
        n=p**kk
        if n>10**6: break
        fac=sympy.factorint(n-1)
        lhs=math.log(n-1) if n>2 else 0.0
        rhs=sum(v*math.log(l) for l,v in fac.items())
        maxerr=max(maxerr,abs(lhs-rhs))
        fix=sum(1 for j in range(n-1) if (n*j-j)%(n-1)==0) if n<2000 else n-1   # fixed points j/(n-1) of x->n x on R/Z, counted on the grid j/(n-1)
        assert p not in fac
        rows.append(dict(n=n,p=p,k=kk,chart_det=n-1,primes_carrying=sorted(int(l) for l in fac),p_divides=False,fixed_points_RZ=fix,
                         log_p=math.log(p),ratio_chart_to_logp=(n-1)/math.log(p)))
# (ii) symbolic
u=sympy.symbols('u',real=True)
ok_sym=sympy.simplify(sympy.exp(-u/2)*(sympy.exp(u)+1)-2*sympy.cosh(u/2)).rewrite(sympy.exp).simplify()==0
ok_asym=sympy.simplify(sympy.exp(-u/2)*(sympy.exp(u)-1)-2*sympy.sinh(u/2)).rewrite(sympy.exp).simplify()==0
res=dict(max_abs_err_product_formula=maxerr,ok_halfdensity_P1_is_hsym=bool(ok_sym),ok_halfdensity_Gm_is_hasym=bool(ok_asym),
         p_never_divides_pk_minus_1=True,examples=[r for r in rows if r['n'] in (2,4,8,3,9,5,25,7,49,11,13,1024)],
         k_dependence_of_needed_chart_jacobian=[dict(p=2,k=k,needed=(2**k-1)/math.log(2)) for k in range(1,6)])
json.dump(res,open('n1_product_formula.json','w'),indent=1)
print(json.dumps({k:v for k,v in res.items() if k!='examples'},indent=1))
for r in res['examples']: print(r['n'],r['chart_det'],r['primes_carrying'],r['fixed_points_RZ'])

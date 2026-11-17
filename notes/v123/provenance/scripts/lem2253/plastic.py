"""Lemma 188: off-diagonal kernel of CCM's QW, K(w) = -J(w) + 2cosh(w/2), J(w)=e^{|w|/2}/(2 sinh|w|)."""
import mpmath as mp
mp.mp.dps=50
J=lambda w: mp.exp(abs(w)/2)/(2*mp.sinh(abs(w)))
K=lambda w: -J(w)+2*mp.cosh(w/2)
P=mp.findroot(lambda y:y**3-y-1,1.3)
w0=mp.log(P)
print("plastic P =",P)
print("w0 = log P =",w0, " sqrt(P) =",mp.sqrt(P)," w0/2 =",w0/2)
print("K(w0) =",mp.nstr(K(w0),5))
# closed form check: K = e^{w/2} - e^{-5w/2}/(1-e^{-2w})
cf=lambda w: mp.exp(w/2)-mp.exp(-5*w/2)/(1-mp.exp(-2*w))
print("max |K-cf| on grid:",mp.nstr(max(abs(K(mp.mpf(i)/100)-cf(mp.mpf(i)/100)) for i in range(1,300)),3))
# sign changes on (0,5]
g=[K(mp.mpf(i)/10000) for i in range(1,50001)]
sc=[i/10000 for i in range(1,50000) if (g[i-1]<0)!=(g[i]<0)]
print("sign changes of K on (0,5]:",sc)
# polynomial y^3-y-1: discriminant
print("disc(y^3-y-1) = -4(-1)^3-27(1)^2 =",-4*(-1)**3-27)
# J-trivial-zero expansion check: J = sum_{n>=0} e^{-(2n+1/2)w}
w=mp.mpf('0.7'); print("J series check:",mp.nstr(J(w)-mp.nsum(lambda n: mp.exp(-(2*n+mp.mpf(1)/2)*w),[0,mp.inf]),3))
# also the y^2=(y+1)^2(y-1) form with y=e^w? check at y=P
y=P; print("P^5-P^4-1 =",mp.nstr(P**5-P**4-1,3), "  (y+1)^2(y-1)-y^2 at y=P:",mp.nstr((y+1)**2*(y-1)-y**2,3))

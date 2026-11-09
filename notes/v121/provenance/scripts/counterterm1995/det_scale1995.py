# K0 as -2 d/ds log det_zeta((s-Theta)/c) at s=1/2, spectrum s+2n (n>=0) [Deninger-type archimedean det], scale cocycle in c.
import mpmath as mp, json
mp.mp.dps=30
def logdet(s,c):  # -zeta'_lambda(0) for lambda_n=(s+2n)/c ; zeta_lambda(z)=c^z 2^{-z} hurwitz(z,s/2)
    Z=lambda z: c**z*2**(-z)*mp.zeta(z,s/2)
    return -mp.diff(Z,0)
out={}
for c in (2*mp.pi, mp.mpf(1), mp.pi, 4*mp.pi):
    K=-2*mp.diff(lambda s: logdet(s,c), mp.mpf(1)/2)
    out[str(float(c))]=dict(minus2dlogdet=float(K), K0=float(mp.digamma(0.25)-mp.log(mp.pi)), diff=float(K-(mp.digamma(0.25)-mp.log(mp.pi))),
                           predicted_diff=float(mp.log(2*mp.pi)-mp.log(c)))
# Gamma_R identity check: det((s+2n)/2pi)^{-1} = 2^{-1/2} Gamma_R(s)
s=mp.mpf('0.37'); out['det^-1/Gamma_R at s=0.37']=float(mp.e**(-logdet(s,2*mp.pi))/(mp.pi**(-s/2)*mp.gamma(s/2)))
out['2^-1/2']=float(2**-0.5)
json.dump(out,open('det_scale1995.json','w'),indent=1);print(json.dumps(out,indent=1))

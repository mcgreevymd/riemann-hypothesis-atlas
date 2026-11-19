"""L197 add-on: zeta-side analogue of L196.6 convention A. Deleting p0 removes -log p0 * sum_{k>=1} p0^{-k/2}[g(k log p0)+g(-k log p0)];
adding back log p0 * g(0) (= log p0 * ||F||^2, row log p0 * G2) completes a Poisson sum log p0 * sum_{k in Z} p0^{-|k|/2} g(k log p0) >= 0 [T].
So W_del+comp = W + PSD: positive whenever W is. Adding a point (eps-type +): W - Poisson. Scratch. RH NOT proved."""
import sys; sys.argv=['x','0.025']
exec(open('l197.py').read().split("if __name__=='__main__':")[0])
def on(m): return {mo:onset(m,mo) for mo in ('full','E0','coshperp')}
for base,T,A in (('zeta',Tz,AZ),('zeta_K',TK,A20)):
    for p in (2,3,5):
        lp=math.log(p)
        m=member('del+comp',delete(T,p),A+lp*G2,True,''); print(base,p,'deleted + log p diag (conv A, remove)',on(m),flush=True)
        # add a full extra copy of the local factor (1-p^-s)^-1, with diag -log p (conv A, add)
        m=member('add-comp',perturb(T,p,1.0),A-lp*G2,True,''); print(base,p,'extra factor - log p diag (conv A, add)',on(m),flush=True)
m=member('x',delete(TK,3),A20+2*math.log(3)*G2,True,''); print('zeta_K 3 deleted + 2 log 3 diag (3 splits)',on(m))

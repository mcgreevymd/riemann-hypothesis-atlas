# Lower-bound scheme (complement to Ritz upper bounds): for |x|>X, m(x) >= m_lb(X); hence on window∩E0
#   B(F) >= m_lb ||F||^2 - <F, K_X F>,  K_X symbol (m_lb - m(x)) 1_{|x|<X}  (exact inequality)
# so inf_{E0_A} B/||F||^2 >= m_lb - lambda_max(P K_X P). lambda_max via Nystrom (numeric, uncertified).
import numpy as np, json
from scipy.special import psi
from mom1975 import gl, primes_win
def m(x,an): return np.real(psi(0.25+0.5j*x))-np.log(np.pi)-2*sum(c*np.cos(x*np.log(n)) for n,c in an.items())
out={}
for A,X,N in [(0.6,100,300),(0.6,400,700),(0.6,1500,1600),(1.0,100,300),(1.0,400,700),(1.0,1500,1600)]:
    an=primes_win(A)
    mlb=np.real(psi(0.25+0.5j*X))-np.log(np.pi)-2*sum(an.values())   # Re psi increasing in |x|
    xs,wx=gl(0,X,max(4000,int(6*X)))
    s=(mlb-m(xs,an))*wx/np.pi          # (1/2pi)∫_{-X}^{X} = (1/pi)∫_0^X for even symbol
    u,wu=gl(-A/2,A/2,N); sw=np.sqrt(wu)
    C=np.cos(np.outer(u,xs))*sw[:,None]; S=np.sin(np.outer(u,xs))*sw[:,None]
    K=(C*s)@C.T+(S*s)@S.T
    rows=np.array([np.exp(u/2)*sw,np.exp(-u/2)*sw]); Q,_=np.linalg.qr(rows.T); Pr=np.eye(N)-Q@Q.T
    for tag,PP in [('none',np.eye(N)),('E0',Pr)]:
        lmax=np.linalg.eigvalsh(PP@K@PP)[-1]
        out[f'A{A}_X{X}_{tag}']=dict(m_lb=float(mlb),lam_max=float(lmax),lower_bound=float(mlb-lmax))
        print(A,X,N,tag,out[f'A{A}_X{X}_{tag}'],flush=True)
json.dump(out,open('lower1975.json','w'),indent=1)

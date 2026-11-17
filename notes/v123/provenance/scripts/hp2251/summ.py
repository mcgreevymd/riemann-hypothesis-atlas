import json,glob
rows=[]
for f in glob.glob('sout/*.json'):
    try: rows.append(json.load(open(f)))
    except: pass
rows.sort(key=lambda d:(float(d['r']),d['N'],d['dps']))
F=lambda s:float(s)
for d in rows:
    e,o=d['QW_even'],d['QW_odd']; qe,qo=d['Q_even'],d['Q_odd']
    lam1=min(F(qe['low'][1]),F(qo['low'][0]))
    print(f"r={d['r']:>4} N={d['N']:3d} dps={d['dps']:3d} | QW e0={F(e['low'][0]):.6e} e1={F(e['low'][1]):.4e} o0={F(o['low'][0]):.6e} sc={e['sc0']} n-={e['nneg']+o['nneg']} e<o={F(e['low'][0])<F(o['low'][0])} | Q n-={qe['nneg']+qo['nneg']} q0={F(qe['low'][0]):.6f} lam1={lam1:.6e}({'e' if F(qe['low'][1])<F(qo['low'][0]) else 'o'}) sc={qe['sc0']} t={d['time']}")

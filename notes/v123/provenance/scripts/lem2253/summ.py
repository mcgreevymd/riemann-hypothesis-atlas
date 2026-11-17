import json,glob
def load(p):
    R=[]
    for f in glob.glob(p):
        s=open(f).read().strip()
        if s: R.append(json.loads(s))
    return sorted(R,key=lambda d:(float(d['r']),d['N'],d['dps']))
Z=load('out/z_*.json'); C=load('out/c_*.json')
L=['### Table Z: zeta, sine basis (hp2251 assembly), parity eigendecompositions + secular equations','',
'| r | N | dps | Q q0 | min Q on E0 (= Q q1 for r ≥ 1) | n-(Q) | QW e0 | QW o0 | o0/e0 | S(r) | min Q on ker C+ | ratio to o0 | cos(Q-ground, cosh) |','|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for d in Z:
    L.append(f"| {d['r']} | {d['N']} | {d['dps']} | {d['Q_low'][0][:-1]} | {d['E0_min']} | {d['Q_nneg']} | {d['QW_e0']} | {d['QW_o0']} | {float(d['QW_o0'])/float(d['QW_e0']):.3g} | {d['S_scalar']} | {d['kerCplus_min']} | {float(d['ratio_kerC_over_o0']):.5f} | {float(d['groundQ_cosh_overlap']):.6f} |")
L+=['','### Table C: L(s, chi_4) pole-free form (Gamma_R(s+1), conductor 4), sine basis','',
'| r | N | dps | lowest (parity) | 2nd | n- | ground sign changes |','|---|---|---|---|---|---|---|']
for d in C:
    L.append(f"| {d['r']} | {d['N']} | {d['dps']} | {d['Q_low'][0]} | {d['Q_low'][1]} | {d['Q_nneg']} | {d['ground_sc']} |")
open('TABLES.md','w').write('\n'.join(L)+'\n'); print('\n'.join(L))

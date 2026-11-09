"""Cross-check every number cited in SYNTHESIS.md / delta against archived JSON outputs (data/) and audit2060.json.
A cited value passes if some JSON number (or numeric string) agrees to the cited number of significant digits."""
import json, re, os, glob, math
H = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(H, '..')
vals = []
def walk(o, src, path=''):
    if isinstance(o, dict): [walk(v, src, path + '/' + str(k)) for k, v in o.items()]
    elif isinstance(o, list): [walk(v, src, path + f'[{i}]') for i, v in enumerate(o)]
    elif isinstance(o, (int, float)) and not isinstance(o, bool): vals.append((float(o), src, path))
    elif isinstance(o, str):
        for m in re.findall(r'-?\d+\.\d+(?:e-?\d+)?', o):
            try: vals.append((float(m), src, path))
            except ValueError: pass
for f in sorted(glob.glob(os.path.join(B, 'data', '*.json'))) + [os.path.join(H, 'audit2060.json')]:
    try: walk(json.load(open(f)), os.path.basename(f))
    except Exception as e: print('skip', f, e)
CITED = ['-5.372183', '0.19657', '3.7528', '6.3524', '0.005275', '9.0258', '0.358', '0.0069963', '2.2304', '0.07587', '0.000314', '0.00066384',
 '3.20786', '0.8749', '0.5455', '0.011872', '0.00093187', '1.72e-5', '1.278e-5', '1.30e-5', '1.2786e-5', '40.77466', '0.0951580', '0.0023338', '-0.63923',
 '-0.2424', '0.3515', '0.4611', '-0.50404', '-0.5000004', '-1.95450', '-1.95400', '-2.1351', '-2.1346', '0.000513', '0.000164', '0.969', '0.999',
 '0.128', '1.46e-3', '1.6e-7', '3.3722', '5.3722', '1.0827', '-0.3036', '0.045990', '0.0462099862', '0.003012', '0.107651', '-0.104639', '-0.0112645',
 '5.978', '0.20412', '-0.28601', '-0.17576', '0.63038', '0.100396', '1.0353620568e-6', '2.66247', '0.490129', '0.9009276163', '6.3524415627']
def sig(s): return len(re.sub(r'[^0-9]', '', s.split('e')[0]).lstrip('0'))
rows = []
for c in CITED:
    x = float(c); tol = 0.5 * 10 ** (math.floor(math.log10(abs(x))) - sig(c) + 1) * 1.0001
    hit = next(((v, s, p) for v, s, p in vals if abs(v - x) <= tol), None)
    rows.append(dict(cited=c, found=hit is not None, value=hit[0] if hit else None, source=f'{hit[1]}:{hit[2]}' if hit else None))
json.dump(rows, open(os.path.join(H, 'numbers_crosscheck.json'), 'w'), indent=1)
miss = [r['cited'] for r in rows if not r['found']]
print(len(rows), 'cited;', len(rows) - len(miss), 'found in JSON; not found:', miss)

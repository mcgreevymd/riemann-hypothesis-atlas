import json, collections
R = json.load(open('out/ladder_raw.json')); C = json.load(open('out/curves.json'))
tab = {}
for q, rows in R.items():
    qq = int(q); att = set(map(tuple, C[q]['pairs'])) if q in C else None
    def cnt(pred): return sum(1 for x in rows if pred(x))
    off = lambda x: not x['on']
    t = collections.OrderedDict()
    t['box_total'] = len(rows); t['box_off'] = cnt(off)
    t['iii_N>=0'] = (cnt(lambda x: x['iii']), cnt(lambda x: x['iii'] and off(x)))
    t['iv_a_d>=0'] = (cnt(lambda x: x['iv']), cnt(lambda x: x['iv'] and off(x)))
    t['v_twist'] = (cnt(lambda x: x.get('v')), cnt(lambda x: x.get('v') and off(x)))
    t['vi_Jgroup'] = (cnt(lambda x: x.get('vi')), cnt(lambda x: x.get('vi') and off(x)))
    for N in (1, 2, 3, 4, 6, 8, 12, 20):
        t[f'vii_HI_n<={N}'] = (cnt(lambda x: x.get('vi') and (x['first_weil_violation_n'] is None or x['first_weil_violation_n'] > N)),
                               cnt(lambda x: x.get('vi') and off(x) and (x['first_weil_violation_n'] is None or x['first_weil_violation_n'] > N)))
    t['vii_HI_all_n(=on circle)'] = (cnt(lambda x: x.get('vi') and x['on']), 0)
    t['boundary_r=q'] = cnt(lambda x: x.get('boundary_r_eq_q'))
    if att is not None:
        t['real_curves(attained)'] = len(att)
        t['attained_not_in_vi'] = [p for p in att if not any(x['a1'] == p[0] and x['a2'] == p[1] and x.get('vi') for x in rows)]
        t['on_circle_vi_not_attained'] = cnt(lambda x: x.get('vi') and x['on'] and (x['a1'], x['a2']) not in att)
    fk = [x for x in rows if x.get('vi') and off(x)]
    t['fakes_vi_by_type'] = dict(collections.Counter(x['type'] for x in fk))
    t['first_violation_n_hist'] = dict(sorted(collections.Counter(x['first_weil_violation_n'] for x in fk).items()))
    t['max_first_violation_n'] = max([x['first_weil_violation_n'] for x in fk], default=None)
    tab[q] = t
    print(q, json.dumps(t, default=str))
json.dump(tab, open('out/ladder_table.json', 'w'), indent=1, default=str)

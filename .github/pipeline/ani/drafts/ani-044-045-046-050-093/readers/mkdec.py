import json, os
D = []
def rd(s, r): return json.load(open('%s%s.json' % (r, s)))['words']
def dec(s, i, who, why, signs=None, q=None, approx=None, unsure=None):
    A, B = rd(s, 'A'), rd(s, 'B')
    a, b = A[i], B[i]
    src = a if who == 'A' else b
    d = {"stretch": int(s), 'word': i, 'page': a['page'], 'budge': src['budge'],
         'A': ' '.join(a['signs']) + ' | ' + (a.get('q') or ''), 'B': ' '.join(b['signs']) + ' | ' + (b.get('q') or ''),
         'decision': who, 'signs': signs or src['signs'], 'q': q if q is not None else src.get('q', ''),
         'approx': approx if approx is not None else [c for c in src.get('approx', []) if c in (signs or src['signs'])],
         'why': why}
    if unsure: d['unsure'] = unsure
    D.append(d)
exec(open('dec_rules.py').read())
json.dump({'decisions': D}, open('decisions.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter; print(len(D), Counter(d['decision'] for d in D))

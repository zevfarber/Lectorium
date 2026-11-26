import json
dec = json.load(open('decisions.json'))['decisions']
out = []
for st, (a, b) in enumerate([('A1', 'B1'), ('A2', 'B2')], 1):
    A = json.load(open(a + '.json'))['words']; B = json.load(open(b + '.json'))['words']
    assert len(A) == len(B)
    D = {d['word']: d for d in dec if d['stretch'] == st}
    for i, (x, y) in enumerate(zip(A, B)):
        w = {k: x[k] for k in ('page', 'plate', 'chapter', 'line', 'signs', 'q', 'budge', 'gloss', 'rubric', 'restored') if k in x}
        notes = []
        if x.get('unsure'): notes.append(x['unsure'])
        if y.get('unsure') and y['unsure'] != x.get('unsure'): notes.append('B: ' + y['unsure'])
        ap = [c for c in dict.fromkeys(x.get('approx', []) + y.get('approx', []))]
        if i in D:
            d = D[i]
            w['signs'] = d['signs']; w['budge'] = d['budge']
            if d.get('q'): w['q'] = d['q']
            else: w.pop('q', None)
            ap = d.get('approx', []) or [c for c in ap if c in d['signs']]
            notes.append('Decision (%s): %s' % (d['decision'], d.get('unsure') or d['why']))
        ap = [c for c in ap if c in w['signs']]
        if ap: w['approx'] = ap
        if notes: w['unsure'] = ' · '.join(notes)
        if x.get('restored') != y.get('restored'): print('restored differs', st, i)
        out.append(w)
json.dump(out, open('merged.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for w in out if w.get('rubric')), [ (w['page'], w['budge']) for w in out if w.get('restored')], sum(1 for w in out if w.get('approx')), sum(1 for w in out if w.get('unsure')))

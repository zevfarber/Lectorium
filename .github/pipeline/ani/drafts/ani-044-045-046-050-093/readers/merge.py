import json
dec = json.load(open('decisions.json'))['decisions']
KEYS = ('page', 'plate', 'chapter', 'line', 'signs', 'q', 'budge', 'gloss', 'rubric', 'restored')
out = []
def word(x, y, d):
    w = {k: x[k] for k in KEYS if k in x}
    notes = []
    if x.get('unsure'): notes.append(x['unsure'])
    if y is not None and y.get('unsure') and y['unsure'] != x.get('unsure'): notes.append('B: ' + y['unsure'])
    ap = list(dict.fromkeys(x.get('approx', []) + (y.get('approx', []) if y else [])))
    if d:
        w['signs'] = d['signs']; w['budge'] = d['budge']
        if d.get('q'): w['q'] = d['q']
        else: w.pop('q', None)
        ap = d.get('approx', []) or [c for c in ap if c in d['signs']]
        notes.append('Decision (%s): %s' % (d['decision'], d.get('unsure') or d['why']))
    ap = [c for c in ap if c in w['signs']]
    if ap: w['approx'] = ap
    if notes: w['unsure'] = ' · '.join(notes)
    return w
for st in (1, 2, 3):
    A = json.load(open('A%d.json' % st))['words']; B = json.load(open('B%d.json' % st))['words']
    D = {d['word']: d for d in dec if d['stretch'] == st and 'wordB' not in d}
    if st == 1:
        DB = {d['wordB']: d for d in dec if d['stretch'] == 1}
        for i, x in enumerate(A):
            if i == 27:   # split àu | χemu as Budge prints (decision B)
                for j in (27, 28):
                    w = word(B[j], None, None); w['unsure'] = (w.get('unsure', '') + ' · ' if w.get('unsure') else '') + 'Decision (B): ' + DB[j]['why']; out.append(w)
                continue
            j = i if i < 27 else i + 1
            out.append(word(x, B[j], DB.get(j)))
    else:
        assert len(A) == len(B)
        for i, (x, y) in enumerate(zip(A, B)):
            out.append(word(x, y, D.get(i)))
json.dump(out, open('merged.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for w in out if w.get('rubric')), [(w['page'], w['budge']) for w in out if w.get('restored')], sum(1 for w in out if w.get('approx')), sum(1 for w in out if w.get('unsure')))

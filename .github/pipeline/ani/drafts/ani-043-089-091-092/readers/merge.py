import json
dec = json.load(open('decisions.json'))['decisions']
KEYS = ('page', 'plate', 'chapter', 'line', 'signs', 'q', 'budge', 'gloss', 'rubric', 'restored')
def word(x, y, d):
    w = {k: x[k] for k in KEYS if k in x}
    notes = []
    if x.get('unsure'): notes.append(x['unsure'])
    if y is not None and y.get('unsure') and y['unsure'] != x.get('unsure'): notes.append('B: ' + y['unsure'])
    ap = list(dict.fromkeys(x.get('approx', []) + (y.get('approx', []) if y else [])))
    if d:
        w['signs'] = d['signs']
        if d.get('q'): w['q'] = d['q']
        else: w.pop('q', None)
        ap = d.get('approx') or [c for c in ap if c in d['signs']]
        notes.append('Decision (%s): %s' % (d['decision'], d['why']))
    ap = [c for c in ap if c in w['signs']]
    if ap: w['approx'] = ap
    if notes: w['unsure'] = ' · '.join(notes)
    return w
out = []
for st in (1, 2, 3):
    A = json.load(open('A%d.json' % st))['words']; B = json.load(open('B%d.json' % st))['words']
    D = {d['word']: d for d in dec if d['stretch'] == st}
    for i, x in enumerate(A):
        if st == 1 and i == 67:
            for j in (67, 68):
                w = word(B[j], None, None)
                w['unsure'] = (w.get('unsure', '') + ' · ' if w.get('unsure') else '') + "Decision (B): Budge spaces 'neter' and 'āa' as two transliteration words: two words (A had one)"
                out.append(w)
            continue
        j = i + 1 if (st == 1 and i > 67) else i
        assert x['budge'] == B[j]['budge'], (st, i, x['budge'], B[j]['budge'])
        out.append(word(x, B[j], D.get(i)))
json.dump(out, open('merged.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for w in out if w.get('rubric')), [(w['page'], w['budge']) for w in out if w.get('restored')], sum(1 for w in out if w.get('approx')), sum(1 for w in out if w.get('unsure')))

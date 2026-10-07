#!/usr/bin/env python3
"""Cut Greek t from the source lines 19.203-307 and attach English (l, i) and notes (n) from the data below."""
import json, os, re, ast
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
src = json.load(open(os.path.join(ROOT, 'source', 'odyssey-murray1919.json')))
L = [x for x in src['books']['19'] if 203 <= x['n'] <= 307]
assert len(L) == 105
lines = {x['n']: x['t'].split() for x in L}

# published whole-unit repeats, read from the packet
pk = open(os.path.join(HERE, 'packet.md'), encoding='utf-8').read()
PUB = {}
for m in re.finditer(r"- \*\*19\.(\d+)\*\* = .*?\n  - t: (.*?)\n  - l: (.*?)\n  - i: (.*?)\n", pk):
    PUB[int(m.group(1))] = tuple(ast.literal_eval(m.group(k)) for k in (2, 3, 4))

exec(open(os.path.join(HERE, 'units_data.py'), encoding='utf-8').read())  # defines UNITS, META

sents = []
cur = (203, 0)  # (line, word index)
for u in UNITS:
    endline, k = u['end']
    parts = []
    ln, wi = cur
    start_ln = ln
    while True:
        w = lines[ln]
        if ln == endline:
            stop = len(w) if k is None else k
            parts.append(' '.join(w[wi:stop]))
            cur = (ln + 1, 0) if stop == len(w) else (ln, stop)
            break
        parts.append(' '.join(w[wi:]))
        ln += 1; wi = 0
    t = '\n'.join(parts)
    if 'pub' in u:
        pt, pl, pi = PUB[u['pub']]
        assert pt == t, (u['pub'], pt, t)
        l, i = pl, pi
    else:
        l, i = u['l'], u['i']
    assert l.count('\n') == t.count('\n'), (start_ln, l, t)
    assert '\n' not in i
    s = {'t': t, 'l': l, 'i': i, 'n': u['n']}
    if u.get('p'): s['p'] = True
    s['v'] = True
    s['ln'] = start_ln
    if u.get('mark'): s['mark'] = u['mark']
    sents.append(s)
assert cur == (308, 0), cur

# quotation marks
def quote_open(s):
    if not s['l'].startswith('“'): s['l'] = '“' + s['l']
    if not s['i'].startswith('“'): s['i'] = '“' + s['i']
def quote_close(s):
    if not s['l'].endswith('”'): s['l'] += '”'
    if not s['i'].endswith('”'): s['i'] += '”'
for s, u in zip(sents, UNITS):
    if u.get('qo'): quote_open(s)
    if u.get('qc'): quote_close(s)

out = {'title': META['title'], 'titleEn': META['titleEn'], 'part': META['part'], 'about': META['about'], 'sentences': sents}
json.dump(out, open(os.path.join(HERE, 'units.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# checks: joined t reproduces the source
joined = '\n'.join(s['t'] for s in sents)
srcjoin = '\n'.join(x['t'] for x in L)
assert joined.replace('\n', ' ') == srcjoin.replace('\n', ' ')
assert joined == srcjoin or True
# stricter: unit boundaries mid-line become a space between pieces; whole-line boundaries a newline
flat = re.sub(r'\s+', ' ', joined)
assert flat == re.sub(r'\s+', ' ', srcjoin)
print('ok', len(sents), 'units')

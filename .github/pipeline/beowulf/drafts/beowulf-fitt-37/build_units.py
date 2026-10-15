# Cuts each unit's t from the packet's lines by (start line, start marker, end line, end marker).
# Marker None = start of line / end of line. Start marker: text from its first occurrence in the line.
# End marker: cut after its first occurrence in the line (searched from the start offset if same line).
import json, re, os
D = os.path.dirname(os.path.abspath(__file__))
pk = open(os.path.join(D, 'packet.md'), encoding='utf-8').read()
blk = pk.split('```')[1]
L = {}
for ln in blk.strip('\n').split('\n'):
    m = re.match(r'(\d+)  (.*)$', ln)
    if m: L[int(m.group(1))] = m.group(2)

from units_text import U   # list of (sl, sm, el, em, l, i, n, p)

def cut(sl, sm, el, em):
    s = 0 if sm is None else L[sl].index(sm)
    if sl == el:
        e = len(L[el]) if em is None else L[el].index(em, s) + len(em)
        return L[sl][s:e]
    parts = [L[sl][s:]]
    for k in range(sl + 1, el):
        parts.append(L[k])
    e = len(L[el]) if em is None else L[el].index(em) + len(em)
    parts.append(L[el][:e])
    return '\n'.join(parts)

out = []
for (sl, sm, el, em, l, i, n, p) in U:
    t = cut(sl, sm, el, em)
    assert t.count('\n') + 1 <= 8, sl
    o = {}
    if p: o['p'] = True
    o.update({'v': True, 'ln': sl, 't': t, 'l': l})
    if i: o['i'] = i
    o['n'] = n
    out.append(o)

# tiling check
flat = lambda s: re.sub(r'\s+', '', s)
allt = ''.join(L[k] for k in sorted(L))
assert flat(''.join(o['t'] for o in out)) == flat(allt), 'tiling mismatch'
json.dump({'sentences': out}, open(os.path.join(D, 'units.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'units; notes', sum(1 for o in out if o['n']))

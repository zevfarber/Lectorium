# One-off for the pilot: turn draft.py into units.json, cutting t from the edition.
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A, draft, gloss
P = A.part('aeneid-001'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
cuts = A.cut(P, [u[0] for u in draft.U])
sents = []; prev_end_line = None
for (t, ln), (_, l, i, n) in zip(cuts, draft.U):
    u = {'t': t, 'l': l, 'i': i, 'n': n}
    starts_line = prev_end_line != ln
    if starts_line and ln in paras: u['p'] = True
    u['v'] = True; u['ln'] = ln; sents.append(u)
    prev_end_line = ln + t.count('\n')
    if t.count('\n') != l.count('\n'): print('LINE COUNT', ln, repr(t[:30]))
A.jdump({'title': draft.TITLE, 'titleEn': draft.TITLE_EN, 'part': draft.PART, 'about': draft.ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
A.jdump(dict(sorted(gloss.G.items())), os.path.join(HERE, 'gloss.json'))
print(len(sents), 'units')

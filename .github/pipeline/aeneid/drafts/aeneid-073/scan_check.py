#!/usr/bin/env python3
"""Reviewer helper (aeneid-073): print the shared scanner's fit for every line of the part,
and the scan_story report, the way build_aeneid.py calls it; mark lines that scan-fixes.json overrides."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
P = A.part('aeneid-073'); L = A.lines_of(P)
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
D = A.jload(os.path.join(HERE, 'units.json'))
story = {'sentences': [{'t': u['t'], 'v': True, 'ln': u['ln']} for u in D['sentences']]}
n_ok, n_lines, rep = SL.scan_story(story)
for l in L:
    words, sc, best = SL.scan_line(l['t'])
    k = f"{P['book']}.{l.get('label', l['n'])}"
    tag = ' [FIX]' if k in fx else ''
    cost = '' if sc is None else '%.1f' % best[0]
    print(l['n'], cost, ' '.join(sc) if sc else 'UNRESOLVED', tag)
print('scan_story:', n_ok, 'units with sc of', len(story['sentences']), ';', n_lines, 'lines')
for r in rep: print('  ', r)

# ---- replica of build_aeneid.py's scansion step and validate_aeneid.py's metre check, with scan-fixes.json applied
units = [{'t': u['t'], 'v': True, 'ln': u['ln']} for u in D['sentences']]
n_ok, n_lines, rep = SL.scan_story({'sentences': units})
lt = [len(A.WORD_RE.findall(l['t'])) for l in L]
flat = [x for u in units for x in u.get('sc', [''] * len(A.WORD_RE.findall(u['t'])))]
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
applied = []
for i, l in enumerate(L):
    k = f"{P['book']}.{l.get('label', l['n'])}"
    if k in fx:
        a = sum(lt[:i]); new = fx[k]['sc']
        assert [strip(x) for x in new] == A.WORD_RE.findall(l['t']), k
        flat[a:a + lt[i]] = new; applied.append(k)
        rep = [r for r in rep if not (r.startswith(('COSTLY', 'UNRESOLVED')) and A.WORD_RE.findall(strip(r.split(': ', 1)[1])) == [strip(x) for x in A.WORD_RE.findall(l['t'])])]
pos = 0
for u in units:
    n = len(A.WORD_RE.findall(u['t'])); u['sc'] = flat[pos:pos + n]; pos += n
print('REPLICA applied', len(applied), applied)
print('REPLICA units with full sc:', sum(all(u['sc']) for u in units), 'of', len(units), '; report left:', rep)
bad = []
for i, l in enumerate(L):
    a = sum(lt[:i]); seg = ' '.join(flat[a:a + lt[i]])
    feet = re.findall(r'[1-6]', seg); syl = len(re.findall(r'[–⏑×]', seg))
    if str(fx.get(f"{P['book']}.{l.get('label', l['n'])}", {}).get('why', '')).startswith('Half-line'):
        if feet != list('123456'[:len(feet)]) or not feet or len(feet) >= 6 or seg.count('×') != 1: bad.append(l['n'])
        continue
    body = re.sub(r'[^0-9–⏑×]', '', seg); fp = re.findall(r'\d([–⏑×]+)', body)
    if feet != list('123456') or not 12 <= syl <= 17 or seg.count('×') != 1 or any(f not in ('–⏑⏑', '––') for f in fp[:5]) or fp[5] not in ('–×', '⏑×'): bad.append(l['n'])
print('REPLICA metre failures:', bad)
# per-unit: validator's 'sc does not line up with the words'
print('REPLICA units whose sc does not line up:', [j for j, u in enumerate(units) if [strip(x) for x in u['sc']] != A.WORD_RE.findall(u['t'])])

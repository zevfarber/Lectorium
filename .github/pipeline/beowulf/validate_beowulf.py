#!/usr/bin/env python3
"""Gate for a built Beowulf part.   usage: python3 validate_beowulf.py beowulf-fitt-NN     Must print PASS before anything is pushed.
`python3 validate_beowulf.py all` checks every published part (use it after touching the glossary)."""
import sys, os, re
import beowulf_lib as B

def check(pid):
    P = B.part(pid); L = B.lines_of(P); F = []; W = []
    fail = lambda *a: F.append(' '.join(str(x) for x in a)); warn = lambda *a: W.append(' '.join(str(x) for x in a))
    try:
        S = B.jload(os.path.join(B.ROOT, P['file'])); G = B.glossary()['glossary']; M = B.jload(os.path.join(B.ROOT, 'stories.json'))['stories']
    except Exception as e:
        return [f'a file does not parse: {e}'], []
    U = S['sentences']
    # 1 the text is Klaeber's, character for character, with line breaks exactly at his line ends
    src = '\n'.join(l['t'] for l in L); got = ''
    for u in U:
        got += u['t']
        if len(got) < len(src): got += src[len(got)] if src[len(got)] in ' \n' else '\x00'
    if got != src: fail('concat: the units do not reproduce the edition')
    if B.sha(L) != P['sha256']: fail('source sha differs from parts.json')
    for u in U:
        bad = B.charset_errors(u['t'])
        if bad: fail(f'line {u.get("ln")}: characters outside Klaeber\'s inventory: {bad}')
    # 2 every word has a glossary entry, and every entry is well formed
    miss = sorted({f for u in U for f in B.forms(u['t'])} - set(G))
    if miss: fail('coverage:', len(miss), 'forms without an entry:', miss[:20])
    for f, e in G.items():
        if not re.match(r'^\S.* — \S', e) or '`' in e: fail('glossary shape:', f, '=>', e[:60])
    # 3 layers
    starts = {}; pos = 0
    nums = [l['n'] for l in L]; li = 0
    for k, u in enumerate(U):
        w = f'unit {k} (line {u.get("ln")}):'
        if u.get('ln') != nums[min(li, len(nums) - 1)]: fail(w, f'ln should be {nums[min(li, len(nums)-1)]}')
        li += u['t'].count('\n')
        if pos + len(u['t']) < len(src) and src[pos + len(u['t'])] == '\n': li += 1
        pos += len(u['t']) + 1
        if not u.get('l'): fail(w, 'missing l')
        if not u.get('v'): fail(w, 'v must be true')
        TR = r'\b(Heaney|Tolkien|Chickering|Headley|Liuzza|Donaldson|Raffel|Crossley-Holland|Gummere)\b'
        if re.search(TR, u.get('i', '') + u.get('l', '')): fail(w, 'names a modern translator in the translation')
        if re.search(TR, u.get('n', '')): warn(w, 'note names a modern translator — fine for a cultural remark (Tolkien’s orcs), never as a source of wording')
        if '`' in u.get('n', ''): fail(w, 'backtick in note')
        n = len(u.get('n', '').split())
        if u.get('n') and (n < 12 or n > 150): warn(w, f'note is {n} words')
    dens = sum(1 for u in U if u.get('n')) / len(U)
    if dens < 0.75: fail(f'notes on {dens:.0%} of units (floor 75%; the published parts sit at 95–100%)')
    # 4 emendation transparency: a unit covering a bracketed, italic or low-confidence line carries a note
    flagged = {l['n'] for l in L if '[' in l['t'] or '(' in l['t'] or l.get('italics') or l.get('variant')}
    for k, u in enumerate(U):
        span = set(range(u['ln'], u['ln'] + u['t'].count('\n') + 1))
        if span & flagged and not u.get('n'): fail(f'unit {k} (line {u["ln"]}): covers an emended or doubtful line and has no note')
    # 5 metadata and manifest
    for k in ('title', 'titleEn', 'work', 'workEn', 'part', 'source', 'about', 'glossaryFile'):
        if not S.get(k): fail('story missing', k)
    if S.get('langCode') is not None: fail('langCode must be null for Old English')
    if S.get('part') != P['part']: fail('part label differs from parts.json')
    me = [e for e in M if e.get('id') == pid]
    if len(me) != 1 or me[0].get('file') != P['file'] or me[0].get('part') != S['part']: fail('manifest entry missing or disagrees with the story')
    ids = [p['id'] for p in B.parts()['parts']]
    order = [e['id'] for e in M if e.get('id') in ids]
    if order != sorted(order, key=ids.index): fail('manifest: Beowulf parts out of poem order')
    return F, W

targets = [p['id'] for p in B.parts()['parts'] if p['status'] == 'published'] if sys.argv[1] == 'all' else [sys.argv[1]]
bad = 0
for pid in targets:
    F, W = check(pid)
    for w in W: print('WARN', pid, w)
    for f in F: print('FAIL', pid, f)
    print(pid, 'PASS' if not F else f'{len(F)} failure(s)')
    bad += len(F)
sys.exit(1 if bad else 0)

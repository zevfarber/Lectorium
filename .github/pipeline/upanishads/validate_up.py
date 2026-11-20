#!/usr/bin/env python3
"""Gate a built part before it is pushed:  python3 validate_up.py <part> [path-to-json]
Exit status 0 = PASS. Every check is against the repository's own source files."""
import json, os, sys
import up_lib as U

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
# red-flag phrases from well-known modern renderings: a hit means REPHRASE (spot-check rule).
ECHOES = ['the self-existent pierced the openings outward', 'arise! awake!', 'arise, awake, and stop not',
          'two birds, inseparable companions', 'that is full, this is full', 'lead me from the unreal to the real',
          'the knife\'s edge', 'sharp as a razor\'s edge', 'like the edge of a razor']


def main(pid, path=None):
    P = U.part(pid)
    path = path or os.path.join(ROOT, P['file'])
    fails, warns = [], []
    try:
        st = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('FAIL json:', e); return 1
    if st.get('id') != P['id'] or st.get('script') != 'devanagari' or st.get('langCode') is not None:
        fails.append('metadata (id/script/langCode)')
    units = U.read_part(pid)
    S = st['sentences']
    if len(S) != len(units):
        fails.append(f'{len(S)} units built, the source has {len(units)}')
    for k, (u, s) in enumerate(zip(units, S), 1):
        if s.get('t') != '\n'.join(u['lines']):
            fails.append(f'unit {k}: t does not match the source lines')
        if s.get('ln') != u['n']:
            fails.append(f'unit {k}: ln {s.get("ln")} where the source has {u["n"]}')
        flat = [g['s'] for w in s['words'] for g in w['glyphs']]
        src = [t for l in u['lines'] for t, _ in U.line_tokens(l)]
        if flat != src:
            fails.append(f'unit {k}: words do not tile the source tokens')
        brk = [i for i, w in enumerate(s['words']) if w.get('br')]
        want, c = [], 0
        for wl in U.words_of(u)[:-1]:
            c += len(wl); want.append(c)
        if brk != want:
            fails.append(f'unit {k}: line breaks {brk}, expected {want}')
        for w in s['words']:
            dev = next(g['s'] for g in w['glyphs'] if g.get('role') != 'punct')
            if not w.get('reading'):
                fails.append(f'unit {k}: word {dev} has no reading')
            if not w.get('morph') or any(not m.get('lemma') or not m.get('gloss') for m in w['morph']):
                fails.append(f'unit {k}: word {dev} has an empty morph')
            if dev not in st.get('glossary', {}):
                fails.append(f'unit {k}: {dev} missing from the glossary')
        if not s.get('l'):
            fails.append(f'unit {k}: no literal')
        if s.get('i') and s['i'] == s.get('l'):
            warns.append(f'unit {k}: i equals l (drop i)')
        low = ' '.join([s.get('l', ''), s.get('i', '')]).lower()
        for e in ECHOES:
            if e in low:
                fails.append(f'unit {k} echoes a modern translation: {e!r} — rephrase')
    numbered = [u for u in units if u['n'] is not None]
    noted = sum(1 for u, s in zip(units, S) if u['n'] is not None and s.get('n'))
    if numbered and noted < 0.5 * len(numbered):
        warns.append(f'only {noted} of {len(numbered)} numbered units have notes')
    if not st.get('about'):
        warns.append('no about')
    for w in warns:
        print('WARN', w)
    for f in fails:
        print('FAIL', f)
    print('PASS' if not fails else 'FAILED', P['file'], '| units', len(S), '| glossary', len(st.get('glossary', {})), '| warnings', len(warns))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))

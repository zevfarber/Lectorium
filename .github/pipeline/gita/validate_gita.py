#!/usr/bin/env python3
"""Gate a built chapter before it is pushed:  python3 validate_gita.py NN [path-to-json]
Exit status 0 = PASS. Every check is against the repository's own source files, never memory."""
import json, os, re, sys, unicodedata
from indic_transliteration import sanscript
import gita_lib as g

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SPEAKERS = {'धृतराष्ट्र उवाच', 'सञ्जय उवाच', 'अर्जुन उवाच', 'श्रीभगवानुवाच'}
# red-flag phrases from well-known modern renderings of the famous verses: a hit means REPHRASE.
ECHOES = ['i am become death', 'destroyer of worlds', 'shatterer of worlds', 'the destroyer of the worlds',
          'whenever there is a decline of righteousness', 'to protect the good and destroy the wicked',
          'you have a right to your actions, but never to your actions\' fruits',
          'abandon all varieties of religion', 'abandoning all duties']

def main(ch, path=None):
    parts = json.load(open(os.path.join(HERE, 'parts.json'), encoding='utf-8'))
    part = next(p for p in parts['parts'] if p['chapter'] == ch)
    path = path or os.path.join(ROOT, part['file'])
    fails, warns = [], []
    try:
        st = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('FAIL json:', e); return 1
    if st.get('id') != part['id'] or st.get('script') != 'devanagari' or st.get('langCode') is not None:
        fails.append('metadata (id/script/langCode)')
    verses = g.read_wikisource(ch)
    corr = g.corrections()
    units = st['sentences']
    # 1. tiling: the Devanagari tokens of the verse units reproduce the corrected source line by line
    vi = 0; seen_ln = []
    for u in units:
        toks = [w['glyphs'][0]['s'] for w in u.get('words', [])]
        if 'ln' not in u:
            if u.get('t') not in SPEAKERS: fails.append('unit without ln that is not a speaker line: %r' % u.get('t'))
            elif u.get('t') != (verses[vi]['speaker'] if vi < len(verses) else None): fails.append('speaker line %s out of place before verse %d' % (u.get('t'), vi + 1))
            continue
        v = verses[vi] if vi < len(verses) else None
        if v is None or u['ln'] != v['n']:
            fails.append('verse order: unit ln %s where verse %s expected' % (u['ln'], v and v['n'])); vi += 1; continue
        seen_ln.append(u['ln'])
        src = ' '.join(v['lines']).split()
        if toks != src:
            fails.append('%d.%d tokens do not tile the source' % (ch, u['ln']))
        # line breaks
        br = [i for i, w in enumerate(u['words']) if w.get('br')]
        want = []; c = 0
        for line in v['lines'][:-1]:
            c += len(line.split()); want.append(c)
        if br != want: fails.append('%d.%d line breaks %s, expected %s' % (ch, u['ln'], br, want))
        if not u.get('v'): fails.append('%d.%d missing v:true' % (ch, u['ln']))
        if u.get('t', '').split('\n') != [l + (' ॥' if i == len(v['lines']) - 1 else ' ।') for i, l in enumerate(v['lines'])]:
            fails.append('%d.%d t does not match the source lines with daṇḍas' % (ch, u['ln']))
        # 2. words model
        for w in u['words']:
            if not w.get('reading'): fails.append('%d.%d word %s has no reading' % (ch, u['ln'], w['glyphs'][0]['s']))
            if not w.get('morph') or any(not m.get('lemma') or not m.get('gloss') for m in w['morph']):
                fails.append('%d.%d word %s has an empty morph' % (ch, u['ln'], w['glyphs'][0]['s']))
            dev = w['glyphs'][0]['s']
            if dev not in st.get('glossary', {}): fails.append('%d.%d token %s missing from glossary' % (ch, u['ln'], dev))
            # reading sanity: same opening letters as the surface
            a = g.letters_dev(dev); b = g.letters_iast(w.get('reading', ''))
            if a[:2] != b[:2] and not dev.startswith(('ऽ',)):
                warns.append('%d.%d reading %r does not open like %s (%s)' % (ch, u['ln'], w.get('reading'), dev, a[:6]))
        # 3. translations and notes
        if not u.get('l'): fails.append('%d.%d no literal' % (ch, u['ln']))
        if u.get('i') and u['i'] == u.get('l'): warns.append('%d.%d i equals l (drop i)' % (ch, u['ln']))
        key = '%d.%d' % (ch, u['ln']); note = u.get('n', '')
        if key in corr and not any(cc[1] in note or cc[0] in note for cc in corr[key]): fails.append('%s note must name the correction' % key)
        if key in part['variantsVsBORI'] and 'BORI' not in note: fails.append('%s note must give the BORI reading' % key)
        low = ' '.join([u.get('l', ''), u.get('i', '')]).lower()
        for e in ECHOES:
            if e in low: fails.append('%s echoes a modern translation: %r' % (key, e))
        vi += 1
    if seen_ln != [v['n'] for v in verses]: fails.append('verse coverage %s..%s of %d' % (seen_ln[:1], seen_ln[-1:], len(verses)))
    # 4. note density
    noted = sum(1 for u in units if u.get('n'))
    if noted < 0.5 * len(verses): warns.append('only %d of %d verses have notes' % (noted, len(verses)))
    for w in warns: print('WARN', w)
    for f in fails: print('FAIL', f)
    print('PASS' if not fails else 'FAILED', part['file'], '| verses', len(seen_ln), '| units', len(units), '| glossary', len(st.get('glossary', {})), '| warnings', len(warns))
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else None))

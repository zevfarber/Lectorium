#!/usr/bin/env python3
"""Gate for one Slovo part file. Usage: validate_slovo.py <story.json> [--stories stories.json]

Exit code 0 = every gate passed. Prints a PASS/FAIL line per gate.

Gates (all mechanical, all required):
  1. JSON parses; required fields present; langCode is null; trStyle == "line".
  2. The concatenated `t` of the sentences equals the part's source text exactly
     (whitespace-normalised), where the part's boundaries come from parts.json and the
     source from source-1800.txt in this folder.
  3. Every sentence has t, tr, l; `p` on at least the first sentence.
  4. Glossary coverage is 100 % under the reader's own tokenizer (WORD_RE from reader.html,
     reproduced below — keep it in sync if reader.html changes), and no glossary key is unused.
  5. If --stories is given: the manifest parses, contains exactly one entry with this id, and
     that entry's `file` names this file.
"""
import json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

WORD_CLASS = ('A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ̀-ͯḀ-ỿ'
              'Ά-ϿЀ-ӿἀ-῿ᠠ-ᡷ᠋-᠎'
              'ؠ-ٰٟ-ۓە-ۭ')
HAN_CLASS = '㐀-䶿一-鿿豈-﫿'
WORD_RE = re.compile('[' + HAN_CLASS + ']|[' + WORD_CLASS + r']+(?:[-\[\]()][' + WORD_CLASS + ']+)*')


def gkey(tok):
    return re.sub(r'[\[\]()]', '', tok).lower()


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    path = args[0]
    stories = args[args.index('--stories') + 1] if '--stories' in args else None
    ok = True

    def gate(name, cond, detail=''):
        nonlocal ok
        print(('PASS ' if cond else 'FAIL ') + name + (('  ' + detail) if detail else ''))
        ok = ok and cond

    try:
        story = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('FAIL parse', e); sys.exit(1)
    for f in ('id', 'title', 'titleEn', 'work', 'workEn', 'part', 'language', 'source', 'about', 'sentences', 'glossary'):
        gate('field ' + f, f in story)
    gate('langCode null', story.get('langCode') is None)
    gate('trStyle line', story.get('trStyle') == 'line')

    sents = story.get('sentences', [])
    gate('sentences non-empty', bool(sents))
    gate('every sentence has t/tr/l', all(all(k in s and isinstance(s[k], str) and s[k].strip() for k in ('t', 'tr', 'l')) for s in sents))

    # gate 2: concat against the source part
    parts = json.load(open(os.path.join(HERE, 'parts.json'), encoding='utf-8'))['parts']
    raw_source = open(os.path.join(HERE, 'source-1800.txt'), encoding='utf-8').read()
    src = norm(raw_source)
    m = re.search(r'slovo-part(\d+)$', story.get('id', ''))
    pn = int(m.group(1)) if m else (0 if story.get('id') == 'slovo-proem' else None)
    gate('id names a part', pn is not None, story.get('id', ''))
    if pn is not None:
        p = next(x for x in parts if x['part'] == pn)
        i = src.find(p['opens']); j = src.find(p['ends'], i) + len(p['ends'])
        seg = src[i:j]
        cat = norm(' '.join(s['t'] for s in sents))
        same = unicodedata.normalize('NFC', cat) == unicodedata.normalize('NFC', seg)
        detail = ''
        if not same:
            k = next((q for q in range(min(len(cat), len(seg))) if cat[q] != seg[q]), min(len(cat), len(seg)))
            detail = 'first difference at char %d: story %r vs source %r' % (k, cat[max(0, k-30):k+30], seg[max(0, k-30):k+30])
        gate('concat t == source part %d' % pn, same, detail)
        gate('word count matches parts.json', len(cat.split()) == p['words'], '%d vs %d' % (len(cat.split()), p['words']))

        # gate 3: p:true marks exactly the sentences that open a real source paragraph
        # (the 1800 edition has 7 paragraphs by blank line; several parts — a part is a
        # narrower cut than a paragraph — sit entirely inside one paragraph and correctly
        # carry no p:true at all, so "first sentence always starts a paragraph" is false
        # in general; only true source paragraph-start offsets get marked).
        raw_paras = re.split(r'\n\s*\n', raw_source.strip())
        para_starts, para_pos = set(), 0
        for rp in raw_paras:
            npara = norm(rp)
            idx = src.find(npara, para_pos)
            para_starts.add(idx)
            para_pos = idx + len(npara)
        cur, offs = i, []
        for s in sents:
            st = norm(s['t'])
            off = src.find(st, cur)
            offs.append(off)
            cur = off + len(st) if off != -1 else cur
        expected = [off in para_starts for off in offs]
        actual = [s.get('p') is True for s in sents]
        gate('p marks exactly the sentences that open a source paragraph', expected == actual,
             'expected %s vs actual %s' % (expected, actual))

    # gate 4: glossary coverage under the reader's tokenizer
    gl = story.get('glossary', {})
    toks = [gkey(t) for s in sents for t in WORD_RE.findall(s['t'])]
    missing = sorted({t for t in toks if t not in gl})
    unused = sorted(k for k in gl if k not in set(toks))
    gate('glossary coverage 100 %', not missing, ('missing: ' + ', '.join(missing[:20])) if missing else '%d tokens, %d keys' % (len(toks), len(gl)))
    gate('no unused glossary keys', not unused, ('unused: ' + ', '.join(unused[:20])) if unused else '')
    gate('glossary values are non-empty strings', all(isinstance(v, str) and v.strip() for v in gl.values()))

    if stories:
        st = json.load(open(stories, encoding='utf-8'))['stories']
        hits = [e for e in st if e.get('id') == story.get('id')]
        gate('manifest has exactly one entry', len(hits) == 1, str(len(hits)))
        if hits:
            gate('manifest file matches', hits[0].get('file') == os.path.basename(path), str(hits[0].get('file')))
            gate('manifest work matches', hits[0].get('work') == story.get('work'))

    print('RESULT', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Build the Mencius source archive and parts.json from the Kanripo transcription of Zhu Xi's 孟子集注
(KR1h0015 四書章句集註, Wenyuange Siku Quanshu copy, 1782, juan 10-16, kept verbatim in source/kanripo/).
Run once, in setup (2026-11-20), modelled on ../analects/archive_analects.py.

Zhu Xi's commentary is printed in parentheses after each stretch of text; those interruptions are the
unit boundaries, as in the Analects. A ○ standing outside the commentary begins a new chapter (章); a
stretch that holds the end of one chapter and the start of the next with no comment between is split at
the ○, so a lemma never straddles two chapters. Each of the fourteen 篇 is cut into parts of whole chapters,
about a thousand characters each. Standard library only."""
import hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'source', 'kanripo')
BOOKS = ['梁惠王', '公孫丑', '滕文公', '離婁', '萬章', '告子', '盡心']
EN = ['King Hui of Liang', 'Gongsun Chou', 'Duke Wen of Teng', 'Li Lou', 'Wan Zhang', 'Gaozi', 'Exhausting the Heart']
TARGET = 1000

def flat():
    out = ''
    for i in range(10, 17):
        t = open(os.path.join(SRC, 'KR1h0015_%03d.txt' % i), encoding='utf-8').read()
        t = re.sub(r'<pb:[^>]*>', '', t)
        t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
        out += t.replace('¶', '').replace('\n', '').replace('　', '')
    out = out.replace('欽定四庫全書', '')
    out = re.sub(r'孟子[卷巻][一二三四五六七]+宋朱子集註', '', out)
    return out

def pieces(body):
    """→ list of (text, new_chapter) stretches between commentary, split at ○ outside commentary."""
    out = []
    depth = 0; cur = ''
    segs = []
    for ch in body:
        if ch == '(':
            if depth == 0: segs.append(cur); cur = ''
            depth += 1
        elif ch == ')':
            depth -= 1
        elif depth == 0:
            cur += ch
    segs.append(cur)
    if depth != 0: sys.exit('unbalanced commentary')
    first = True
    for s in segs:
        if not s: continue
        parts = s.split('○')
        for k, p in enumerate(parts):
            if not p: continue
            out.append((p, first or k > 0)); first = False
    return out

def build():
    t = flat()
    depth = []; d = 0
    for c in t:
        if c == '(': d += 1
        depth.append(d)
        if c == ')': d -= 1
    heads = []
    for b in BOOKS:
        for half in '上下':
            h = b + '章句' + half
            k = heads[-1][1] + 1 if heads else 0
            while True:
                k = t.find(h, k)
                if k < 0: sys.exit('heading not found: ' + h)
                if depth[k] == 0: break
                k += 1
            full = h
            if t[k + len(h)] == '(':
                full = t[k:t.index(')', k) + 1]
            heads.append((h, k, full))
    pian = []
    for idx, (h, k, full) in enumerate(heads):
        end = heads[idx + 1][1] if idx + 1 < len(heads) else len(t)
        body = t[k + len(full):end]
        ps = pieces(body)
        chap = sum(1 for _, nc in ps if nc)
        declared = re.search(r'凡(\S+?)章', full)
        pian.append({'pian': h, 'declared': declared.group(1) if declared else None, 'lemmata': [p for p, _ in ps], 'newChapter': [nc for _, nc in ps], 'chapters': chap})
    return pian

# Chapter starts the ○ marks get wrong in this transcription (checked against the standard chapter count
# Zhu Xi gives at the head of each 篇): (篇, opening characters of the stretch, is it a new chapter?)
FIX = [('滕文公章句下', '萬章問曰宋小國也', True),     # 3B.5 begins without a ○
       ('萬章章句上', '湯三使徃聘之', False),          # inside 5A.7
       ('萬章章句下', '曰敢問招虞人', False),          # inside 5B.7
       ('告子章句下', '孟子居鄒', True),               # 6B.5 begins without a ○
       ('告子章句下', '我能為君約與國', False)]        # inside 6B.9
END = ('盡心章句下', '則亦無有乎爾')                   # the last words of the Mencius; 中庸 follows in juan 16

def fixed():
    pian = build()
    for name, start, val in FIX:
        p = next(x for x in pian if x['pian'] == name)
        k = [i for i, l in enumerate(p['lemmata']) if l.startswith(start)]
        if len(k) != 1:   # the stretch may begin mid-lemma: split it there
            k = [i for i, l in enumerate(p['lemmata']) if start in l]
            assert len(k) == 1, (name, start, k)
            i = k[0]; a, b = p['lemmata'][i].split(start, 1)
            p['lemmata'][i:i + 1] = [a, start + b]; p['newChapter'][i:i + 1] = [p['newChapter'][i], val]
        else:
            p['newChapter'][k[0]] = val
    p = next(x for x in pian if x['pian'] == END[0])
    i = next(k for k, l in enumerate(p['lemmata']) if END[1] in l)
    p['lemmata'][i] = p['lemmata'][i][:p['lemmata'][i].index(END[1]) + len(END[1])]
    p['lemmata'] = p['lemmata'][:i + 1]; p['newChapter'] = p['newChapter'][:i + 1]
    for p in pian:
        p['chapters'] = sum(p['newChapter'])
    return pian

CN = {'七': 7, '十六': 16, '九': 9, '十四': 14, '五': 5, '十': 10, '二十八': 28, '三十三': 33, '二十': 20, '四十六': 46, '三十八': 38}

STATEMENT = ("Mencius 孟子 (Mengzi, c. 372–289 BC) and his disciples, 孟子 (the Mencius), {CITE}, from 〈{PIAN}〉, in the received text "
             "as printed in Zhu Xi 朱熹, 孟子集注 (part of his 四書章句集注, completed c. 1190), from the Wenyuange 文淵閣 copy of the "
             "Siku Quanshu 四庫全書 (1782), as transcribed by the Kanseki Repository (Kanripo, KR1h0015). Collated character by character "
             "against Zhao Qi's 趙岐 孟子章句 (2nd century) in the Sibu Congkan 四部叢刊 photographic reprint of a Song edition (Kanripo "
             "KR1h0002). Readings that change the sense are noted in the notes; graphic variants are not. Chapter divisions and their "
             "numbering are Zhu Xi's, the standard ones; Zhu Xi's text is substantially the one James Legge printed in The Chinese "
             "Classics, vol. 2 (Hong Kong, 1861). All punctuation is editorial — the original has none. Characters are traditional, as "
             "the edition prints them. Translations are made fresh from the Chinese. Pronunciation convention: modern Mandarin, given "
             "in Hanyu Pinyin — an admitted anachronism, and the living convention for reading these texts. Any prepared audio is "
             "synthesized speech in that same modern Mandarin convention; the exact voice used is recorded in audio/<id>/voice.txt "
             "and is fixed for every Chinese text.")

def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()

if __name__ == '__main__':
    pian = fixed()
    out = {'witness': 'Kanripo KR1h0015 (四書章句集註, 文淵閣四庫全書 copy, 1782), juan 10-16',
           'note': "Bare text of the Mencius as Zhu Xi's 孟子集注 prints it; one item per stretch between commentary interruptions, "
                   'never straddling two chapters. No punctuation: the edition has none.', 'books': {}}
    parts = []; seq = 0
    for bi, p in enumerate(pian):
        b = bi // 2 + 1; half = '上下'[bi % 2]; code = f'{b}{"AB"[bi % 2]}'
        assert p['chapters'] == CN[p['declared']], (p['pian'], p['chapters'], p['declared'])
        # chapters as lemma ranges
        ch = [i for i, nc in enumerate(p['newChapter']) if nc] + [len(p['lemmata'])]
        chap = [(ch[k], ch[k + 1]) for k in range(len(ch) - 1)]
        size = [sum(len(x) for x in p['lemmata'][a:z]) for a, z in chap]
        n = max(1, round(sum(size) / TARGET))
        # cut at the chapter boundaries nearest to each k/n of the 篇; drop empty groups
        cum = [0]
        for sz in size: cum.append(cum[-1] + sz)
        cuts = sorted({min(range(1, len(size)), key=lambda j: abs(cum[j] - sum(size) * k / n)) for k in range(1, n)}) if len(size) > 1 else []
        bounds = [0] + cuts + [len(size)]
        groups = [list(range(bounds[k], bounds[k + 1])) for k in range(len(bounds) - 1) if bounds[k + 1] > bounds[k]]
        for gi, g in enumerate(groups):
            seq += 1; key = f'{code}-{gi + 1}'
            lem = [x for k in g for x in p['lemmata'][chap[k][0]:chap[k][1]]]
            nc = [x for k in g for x in p['newChapter'][chap[k][0]:chap[k][1]]]
            out['books'][key] = {'title': p['pian'], 'lemmata': lem, 'newChapter': nc}
            parts.append({'id': f'mencius-{seq:02d}', 'seq': seq, 'book': key, 'pian': p['pian'], 'bookNo': b, 'half': half,
                          'title': BOOKS[b - 1], 'titleEn': EN[b - 1], 'firstPassage': g[0] + 1, 'passages': len(g),
                          'cite': f'{code}.{g[0] + 1}' + (f'–{g[-1] + 1}' if len(g) > 1 else ''),
                          'lemmata': len(lem), 'chars': sum(len(x) for x in lem), 'file': f'mencius-{seq:02d}.json',
                          'sha256': sha(lem), 'status': 'todo'})
    json.dump(out, open(os.path.join(HERE, 'source', 'mencius-zhuxi-siku.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'work': 'Mencius', 'source': 'source/mencius-zhuxi-siku.json', 'sourceStatement': STATEMENT,
               'cutRule': "the fourteen 篇 (Books 1A–7B) cut into parts of whole chapters, ~1,000 characters; within a part, one unit per stretch between Zhu Xi's commentary interruptions; each chapter starts a card (ln = chapter number within the 篇, p: true)",
               'parts': parts}, open(os.path.join(HERE, 'parts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for q in parts: print(q['id'], q['cite'], q['chars'], q['lemmata'])
    print(len(parts), 'parts', sum(q['chars'] for q in parts), 'chars')

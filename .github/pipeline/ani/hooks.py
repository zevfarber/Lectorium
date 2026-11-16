"""Book of the Dead of Ani (Papyrus of Ani, BM EA 10470) — work hooks for .github/pipeline/run3/r3.py.

Egyptian words model, as in the published part ani-spell125-opening (the 42 declarations): every word is
an object with its glyphs (Gardiner code, role here, transcription chunk), its reading, its morphs and a
vocalised "say" form. The text is established part by part from Budge's 1895 interlinear edition
(source/raw/budge1895.pdf): printed hieroglyphic type with his transliteration and word-by-word English
under each word. Status todo -> established -> published.

Established file: source/established/<id>.json
  {"id": ..., "pages": [first, last],            Budge's printed pages actually used
   "start": {"page":, "plate":, "line":, "note":}, "end": {"page":, "plate":, "line":, "lastWord":, "note":},
   "skipped": ["p. 193-197 Appendix (Naville, Bl. 133)", ...],
   "words": [{"page": 189, "plate": "XXX", "line": 1,       line = Budge's papyrus-line number in force
              "signs": ["D21", "Z1"],                         Gardiner codes in reading order
              "q": "0:1",                                     layout as Budge prints it (optional; see conventions)
              "budge": "Re", "gloss": "Chapter",              his transliteration and his English, as printed
              "rubric": true, "approx": ["Z1"], "unsure": "…"}]}   optional flags
"""
import json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

EST = os.path.join(HERE, 'source', 'established')
SIGNS = os.path.join(R.ROOT, 'signs-egyptian.json')
PDF = 'source/raw/budge1895.pdf'
PDF_OFFSET = 164          # PDF page = Budge's printed page + 164 (interlinear text, pp. 1-242)
ROLES = ('phon', 'comp', 'det', 'log', 'suff', 'num')


def code_name(code):
    """Gardiner code -> Unicode character name: G43 -> EGYPTIAN HIEROGLYPH G043, Aa1 -> ... AA001, N35A -> ... N035A."""
    m = re.fullmatch(r'(Aa|NL|NU|[A-IK-Z])(\d{1,3})([A-Za-z]?)', code)
    if not m:
        return None
    return 'EGYPTIAN HIEROGLYPH %s%03d%s' % (m.group(1).upper(), int(m.group(2)), m.group(3).upper())


def glyph(code):
    n = code_name(code)
    if not n:
        return None
    try:
        return unicodedata.lookup(n)
    except KeyError:
        return None


def signs():
    return R.jload(SIGNS)['signs']


def est_path(p):
    return os.path.join(EST, p['id'] + '.json')


def est(p):
    return R.jload(est_path(p)) if os.path.exists(est_path(p)) else None


def slice_source(p):
    e = est(p)
    if e is None:
        return None
    return json.dumps(e['words'], ensure_ascii=False, sort_keys=True)


def prev_end(p):
    q = p.get('after')
    if not q:
        return None
    f = os.path.join(EST, q + '.json')
    return R.jload(f).get('end') if os.path.exists(f) else None


def establish_packet(p):
    a, b = p['pages']
    pe = prev_end(p)
    if p.get('startAt'):
        start = p['startAt']
    elif pe:
        start = (f"right after the last word established by {p['after']}: its end is p. {pe.get('page')}, Plate {pe.get('plate')}, "
                 f"line {pe.get('line')}, last word “{pe.get('lastWord')}” ({pe.get('note', '')}).")
    else:
        start = (f"right after the end of {p.get('after')} — but that part has no established file yet. Stop: release the claim and "
                 f"write this to QUESTIONS.md (parts must be established in book order).")
    return f"""# Establish — {p['id']}: {p['name']}

Budge 1895, interlinear text, printed pp. {a}–{b} (PDF pages {a + PDF_OFFSET}–{b + PDF_OFFSET} of {PDF}; PDF page = printed page + {PDF_OFFSET}).
Chapters expected here (from Budge's running heads and his Table of Chapters; first pass, confirm on the page): {p.get('chapters', '')}
Plates: {p.get('plates', '')}

Start: {start}
End: {p.get('endAt') or "at the end of the chapter or section if it ends on your last page or in the first third of the page after it; otherwise at the last sentence-end on your last page. Never stop inside a sentence. Read on to the next page as far as that needs."}
The page ranges in parts.json are a first pass from the running heads: the page itself decides. Record the pages you really used.

What belongs to the Papyrus of Ani, and what does not (conventions.md, "What is Ani's text"):
- IN: everything Budge prints as the papyrus's own text under a "PLATE n." heading, including chapter titles, rubrics and
  the words written beside the figures in the vignettes.
- OUT: every section headed "Appendix." (text supplied from Naville's Todtenbuch or other papyri) up to the next "PLATE"
  heading or the return to Ani's text; every footnote, including footnotes that print a "less corrupt" parallel text in
  hieroglyphs; words Budge sets in [square brackets] as his own restorations are kept, with "restored": true.
  List what you left out in "skipped" (pages and Budge's label).

Procedure — the printed page is the authority for every sign:
1. Render each page with PyMuPDF at zoom 2 (`python3 ../run3/page.py` or fitz directly), cropped to the text block; then read
   one printed row at a time at zoom 3–4. A row is three lines: hieroglyphs, Budge's transliteration, his English.
2. TWO independent readers (two subagents on the strongest model, neither sees the other's output) each write every word of
   every row: the signs as Gardiner codes in reading order, Budge's transliteration exactly as printed (his ā à χ θ ś t' etc.),
   his English, the page, the plate and the papyrus-line number in force (the small "1." "2." … numerals set inside the rows;
   a word before the first numeral of a plate belongs to line 1 unless the page says otherwise).
   Word division = Budge's own: one group over one transliteration group. A suffix he hyphenates (t'et - à) stays in its word.
3. Diff the two readings word by word (`python3 hooks.py diff A.json B.json`). For every difference a third reader looks at a
   tight crop of that word only and decides. Use Budge's transliteration as a check on every word: the phonetic signs must
   spell it (his system → signs: conventions.md, "Budge's transliteration"); a word whose signs cannot give his reading is
   re-read before it is accepted.
4. A sign with no Unicode character: take the nearest standard sign, list its code under "approx" for that word, and say what
   the type shows in "unsure". A sign you cannot identify at all: put "unsure" on the word with what you see; if more than
   3 words in the part are like that, block the smallest piece (rule 7 of ../README.md), not the part.
5. Layout: "q" records how Budge's type groups the signs of the word, by glyph index: "-" between groups set side by side,
   ":" between signs stacked top to bottom inside a group, "*" between signs side by side inside a stacked group
   (the layout notation of the published part). Omit "q" for a single sign or a plain left-to-right string.
6. Rubrics: Budge marks red-ink passages with a line over the signs. Set "rubric": true on those words.
7. Write source/established/{p['id']}.json in the layout given at the top of hooks.py, with "start", "end" (page, plate, line,
   lastWord = Budge's transliteration of the last word, note = the last few words of his English) and "skipped".
8. `python3 ../run3/r3.py pin ani {p['id']}` checks it and pins it. LOG.md: pages used, words, differences between the two
   readers and how many the third reader decided each way, signs marked approx/unsure, what was skipped.
"""


def check_established(p):
    e = est(p)
    if e is None:
        return [f'{os.path.relpath(est_path(p), R.ROOT)} does not exist']
    errs = []
    a, b = p['pages']
    for k in ('pages', 'start', 'end', 'words'):
        if k not in e:
            errs.append(f'missing "{k}"')
    if errs:
        return errs
    if not isinstance(e.get('skipped', []), list):
        errs.append('"skipped" must be a list')
    for k in ('page', 'plate', 'line', 'lastWord'):
        if not e['end'].get(k):
            errs.append(f'end.{k} missing — the next part starts from it')
    ws = e['words']
    if not ws:
        return errs + ['no words']
    lastpage = 0
    for i, w in enumerate(ws):
        tag = f'word {i} (p. {w.get("page")}, “{w.get("budge")}”)'
        if not isinstance(w.get('page'), int) or not (a - 1 <= w['page'] <= b + 1):
            errs.append(f'{tag}: page outside {a - 1}–{b + 1}')
        elif w['page'] < lastpage:
            errs.append(f'{tag}: pages go backwards')
        else:
            lastpage = w['page']
        if not w.get('plate') or not isinstance(w.get('line'), int):
            errs.append(f'{tag}: plate / line missing')
        if not w.get('signs'):
            errs.append(f'{tag}: no signs')
        for c in w.get('signs', []):
            if glyph(c) is None:
                errs.append(f'{tag}: {c!r} is not a Gardiner code with a Unicode character')
        for c in w.get('approx', []):
            if c not in w.get('signs', []):
                errs.append(f'{tag}: approx lists {c!r}, which is not among its signs')
        if not (w.get('budge') or '').strip():
            errs.append(f'{tag}: Budge\'s transliteration missing')
        if 'gloss' not in w:
            errs.append(f'{tag}: Budge\'s English missing (use "" where he prints none)')
        if w.get('q'):
            idx = [int(x) for x in re.findall(r'\d+', w['q'])]
            if sorted(idx) != list(range(len(w['signs']))) or not re.fullmatch(r'[\d:\-*]+', w['q']):
                errs.append(f'{tag}: q {w["q"]!r} does not cover its {len(w["signs"])} signs once each')
    pages = sorted({w['page'] for w in ws if isinstance(w.get('page'), int)})
    if pages and len(ws) < 12 * len(pages):
        errs.append(f'only {len(ws)} words for {len(pages)} pages — a page of Budge holds 40–70; rows were missed')
    return errs


def flat(e):
    return [c for w in e['words'] for c in w['signs']]


def packet(p):
    e = est(p)
    S = signs()
    G = R.merged_inline_glossary('ani')
    out = [f'# Packet — {p["id"]}: {p["name"]}', '',
           f'Established from Budge 1895, pp. {e["pages"][0]}–{e["pages"][1]}. Start: {json.dumps(e["start"], ensure_ascii=False)}. '
           f'End: {json.dumps(e["end"], ensure_ascii=False)}.',
           'Left out as not Ani\'s text: ' + ('; '.join(e.get('skipped', [])) or 'nothing') + '.', '',
           'One line per word of the established text, in order: index · page/plate/line · signs (code=character, * = not yet in '
           'the sign glossary: add it with signs.py before building) · layout · Budge\'s transliteration · Budge\'s English '
           '(his 1895 understanding: a check on sense, never wording) · flags.',
           'Your units must use these signs in exactly this order (the build compares the whole sequence); you may join or split '
           'Budge\'s word groups where the grammar requires (say so in the note when you do).', '']
    line = None
    for i, w in enumerate(e['words']):
        if (w['plate'], w['line']) != line:
            line = (w['plate'], w['line'])
            out.append(f'\n## Plate {w["plate"]}, line {w["line"]} (p. {w["page"]})')
        sg = ' '.join(f'{c}={glyph(c)}' + ('' if c in S else '*') for c in w['signs'])
        fl = [k for k in ('rubric', 'restored') if w.get(k)]
        if w.get('approx'):
            fl.append('approx ' + ','.join(w['approx']))
        if w.get('unsure'):
            fl.append('UNSURE: ' + w['unsure'])
        out.append(f'- w{i} · {sg} · q {w.get("q", "—")} · {w["budge"]} · “{w.get("gloss", "")}”' + (' · ' + '; '.join(fl) if fl else ''))
    new = sorted({c for c in flat(e) if c not in S})
    out += ['', f'Signs not yet in signs-egyptian.json ({len(new)}): ' + (', '.join(new) or 'none'),
            f'Lemmas already glossed in the published parts: {len(G)} (ani-spell125-opening.json and later parts; reuse their '
            f'lemma spellings and glosses — list in known-lemmas.json).']
    R.jdump(G, os.path.join(R.drafts('ani', p['id']), 'known-lemmas.json'))
    return '\n'.join(out) + '\n'


def assemble(p, units, gloss):
    cfg = R.work_cfg('ani')
    e = est(p)
    G = R.merged_inline_glossary('ani')
    G.update({k: v for k, v in gloss.items() if v and k != '__broaden__'})
    G.update(gloss.get('__broaden__', {}))
    sents, problems = [], []
    for k, u in enumerate(units['sentences']):
        words = []
        for j, w in enumerate(u.get('words', [])):
            gl = []
            for g in w.get('glyphs', []):
                ch = glyph(g.get('sign', ''))
                if ch is None:
                    problems.append(f'unit {k} word {j}: {g.get("sign")!r} is not a Gardiner code with a Unicode character')
                    continue
                ng = {'s': ch, 'sign': g['sign'], 'role': g.get('role'), 'tr': g.get('tr', '')}
                for f in ('approx', 'restored'):
                    if g.get(f):
                        ng[f] = True
                gl.append(ng)
            nw = {'reading': w.get('reading', ''), 'glyphs': gl,
                  'morph': [{'lemma': m.get('lemma', ''), 'gloss': m.get('gloss') or first_gloss(G.get(m.get('lemma', ''), '')),
                             'g': m.get('g')} for m in w.get('morph', [])],
                  'say': w.get('say', '')}
            if w.get('q'):
                nw['q'] = w['q']
            if w.get('rubric'):
                nw['rubric'] = True
            words.append(nw)
        s = {'ln': u.get('ln'), 't': ' '.join(''.join(g['s'] for g in w['glyphs']) for w in words), 'words': words, 'l': u.get('l', '')}
        if u.get('p'):
            s = dict([('ln', s['ln']), ('p', True)] + [(a, b) for a, b in s.items() if a != 'ln'])
        for f in ('i', 'n', 'pl', 'gap'):
            if u.get(f):
                s[f] = u[f]
        sents.append(s)
    cite = f'pp. {e["pages"][0]}–{e["pages"][1]}' if e['pages'][0] != e['pages'][1] else f'p. {e["pages"][0]}'
    plates = sorted({w['plate'] for w in e['words']}, key=roman)
    story = {'id': p['id'], 'title': cfg['title'], 'titleRead': cfg['titleRead'], 'titleEn': units.get('titleEn', ''),
             'part': units.get('part', '')}
    story.update(cfg['header'])
    story.update({'numbering': 'stanza', 'dir': 'ltr', 'provisional': True, 'draftNote': cfg['draftNote'],
                  'source': cfg['sourceStatement'].replace('{cite}', cite).replace('{plates}', 'Plate' + ('s ' if len(plates) > 1 else ' ') + ', '.join(plates)),
                  'about': units.get('about', ''), 'sentences': sents})
    used = [m['lemma'] for s in sents for w in s['words'] for m in w['morph']]
    story['glossary'] = {k: G[k] for k in dict.fromkeys(used) if k in G}
    story['_problems'] = problems
    return story, {}


def first_gloss(entry):
    return entry.split(' — ', 1)[1] if ' — ' in entry else entry


def roman(s):
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    t = 0
    for a, b in zip(s, s[1:] + ' '):
        t += -v.get(a, 0) if v.get(a, 0) < v.get(b, 0) else v.get(a, 0)
    return t


def validate(p, story):
    errs, warns = list(story.pop('_problems', [])), []
    S = signs()
    e = est(p)
    if e is None:
        return ['no established text'], []
    got = [g['sign'] for s in story['sentences'] for w in s.get('words', []) for g in w['glyphs']]
    want = flat(e)
    if got != want:
        i = next((k for k in range(min(len(got), len(want))) if got[k] != want[k]), min(len(got), len(want)))
        errs.append(f'the units\' signs differ from the established text at sign {i}: units {got[i:i + 6]} vs established {want[i:i + 6]} '
                    f'({len(got)} signs drafted, {len(want)} established) — every established sign must appear once, in order')
    for k, s in enumerate(story['sentences']):
        if not isinstance(s.get('ln'), int):
            errs.append(f'unit {k}: ln (the papyrus line the unit starts in) missing')
        for j, w in enumerate(s.get('words', [])):
            tag = f'unit {k} word {j} ({w.get("reading")})'
            if not w.get('reading') or not w.get('say'):
                errs.append(f'{tag}: reading / say missing')
            n = len(w['glyphs'])
            cover = sorted(x for m in w['morph'] for x in (m.get('g') or []))
            if cover != list(range(n)):
                errs.append(f'{tag}: morph g-lists must cover its {n} glyphs once each (got {cover})')
            for m in w['morph']:
                if not m.get('gloss'):
                    errs.append(f'{tag}: lemma {m.get("lemma")!r} has no gloss')
                if m.get('lemma') not in story['glossary']:
                    errs.append(f'{tag}: lemma {m.get("lemma")!r} has no glossary entry')
            for g in w['glyphs']:
                if g['role'] not in ROLES:
                    errs.append(f'{tag}: bad role {g["role"]!r}')
                if g['role'] == 'det' and g['tr']:
                    errs.append(f'{tag}: a determinative carries no transcription')
                if g['role'] in ('phon', 'log') and not g['tr']:
                    warns.append(f'{tag}: {g["sign"]} is {g["role"]} with an empty transcription')
                if g['s'] != glyph(g['sign']):
                    errs.append(f'{tag}: character does not match its code {g["sign"]}')
            if w.get('q'):
                idx = [int(x) for x in re.findall(r'\d+', w['q'])]
                if sorted(idx) != list(range(n)):
                    errs.append(f'{tag}: q {w["q"]!r} does not cover its {n} glyphs once each')
    e2, w2 = R.words_checks(story, S)
    return errs + e2, warns + w2


def diff(a, b):
    """python3 hooks.py diff A.json B.json — word-by-word differences between two readers' files."""
    A, B = R.jload(a)['words'], R.jload(b)['words']
    import difflib
    ka = [' '.join(w['signs']) + '|' + w.get('budge', '') for w in A]
    kb = [' '.join(w['signs']) + '|' + w.get('budge', '') for w in B]
    n = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ka, kb, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        n += 1
        pg = (A[i1] if i1 < len(A) else B[min(j1, len(B) - 1)]).get('page')
        print(f'[{op}] p. {pg} · A[{i1}:{i2}] {ka[i1:i2]} · B[{j1}:{j2}] {kb[j1:j2]}')
    print(f'{len(A)} / {len(B)} words; {n} place(s) differ')


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == 'diff':
        diff(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)

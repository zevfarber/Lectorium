"""Sumerian King List — work hooks for .github/pipeline/run3/r3.py.

Cuneiform words model, as in king-list-antediluvian (2026-07-14). The pinned source is Langdon's 1923
transliteration of the Weld-Blundell Prism (WB 444), Cols. I–VIII, transcribed line by line from the page
images on 2026-10-12 (source/langdon-translit.json); the signs are read from Langdon's plates
(source/pages/langdon1923_0042–0045.jpg = Plates I–IV). Units never cross a column; `ln` is the prism line."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R
import cun as C

SRC = os.path.join(HERE, 'source', 'langdon-translit.json')
COLS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']


def entries(p):
    T = R.jload(SRC)
    key = lambda e: (COLS.index(e['col']), e['ln'] if isinstance(e['ln'], int) else int(str(e['ln']).split('-')[0]))
    a = (COLS.index(p['start']['col']), p['start']['ln'])
    b = (COLS.index(p['end']['col']), p['end']['ln'])
    return [e for e in T if a <= key(e) <= b]


def slice_source(p):
    return '\n'.join(f'{e["col"]} {e["ln"]}\t{e["t"]}' for e in entries(p))


def packet(p):
    out = [f'# Packet — {p["id"]}: {p["titleEn"]} ({p["range"]})', '',
           'Langdon 1923, his transliteration as printed (accents kept; convert to modern subscript indices by SIGN, '
           'not by arithmetic — e.g. his dé is the NE sign, de₃). Langdon\'s [ ] = restored; marks/notes from the '
           'transcription are given per line. Read every sign on the plate.', '',
           '## Images (source/pages/)', '',
           f'- transliteration pages: {", ".join(f"langdon1923_{int(i[-4:]):04d}.jpg" for i in p["pageImages"])}',
           f'- plates: {", ".join(f"langdon1923_{int(i[-4:]):04d}.jpg" for i in p["plateImages"])} ({", ".join(p["plates"])})',
           '- the published part king-list-antediluvian.json is the model of shape, notation and register', '',
           '## Lines (col · line · Langdon · confidence · note)', '']
    for e in entries(p):
        out.append(f'{e["col"]} {e["ln"]}\t{e["t"]}\t{e["conf"]}' + (f'\t— {e["note"]}' if e.get('note') else '')
                   + (f'\t[{", ".join(e["marks"])}]' if e.get('marks') else ''))
    inv = R.jload(os.path.join(HERE, 'source', 'sign-inventory.json'))
    out += ['', '## Value → sign map prepared on 2026-10-12 (first pass, NOT plate-verified; conf low = check)', '',
            '```json', json.dumps(inv.get('valueMap', inv), ensure_ascii=False)[:20000], '```']
    return '\n'.join(out) + '\n'


def assemble(p, units, gloss):
    cfg = R.work_cfg('king-list')
    S = C.signs()
    G = R.merged_inline_glossary('king-list')
    G.update({k: v for k, v in gloss.items() if v and k != '__broaden__'})
    G.update(gloss.get('__broaden__', {}))
    sents, problems = [], []
    for k, u in enumerate(units['sentences']):
        words = C.fill_words(u, S, G, k, problems)
        s = {'ln': u['ln'], 't': C.build_t(words), 'l': u['l'], 'words': words, 'col': u.get('col'), 'line': u.get('line', u['ln'])}
        for f in ('i', 'n', 'p', 'lost'):
            if u.get(f):
                s[f] = u[f]
        sents.append(s)
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': units.get('title') or cfg['title'], 'titleRead': units.get('titleRead') or cfg['titleRead'],
                  'titleEn': units['titleEn'], 'part': units['part'], 'provisional': True,
                  'draftNote': cfg['draftNote'], 'source': cfg['sourceStatement'].replace('{cite}', p['range']),
                  'about': units.get('about', ''), 'numbering': 'line', 'sentences': sents})
    used = {m['lemma'] for s in sents for w in s['words'] for m in w['morph']}
    story['glossary'] = {k: G[k] for k in sorted(used) if k in G}
    story['_problems'] = problems
    return story, {}


def validate(p, story):
    errs, warns = list(story.pop('_problems', [])), []
    want = [(e['col'], e['ln']) for e in entries(p)]
    got = []
    for k, s in enumerate(story['sentences']):
        if s.get('col') is None:
            errs.append(f'unit {k}: needs col')
            continue
        if s.get('lost'):
            got.append(next((w for w in want if w[0] == s['col'] and str(w[1]).split('-')[0] == str(s['line'])), (s['col'], s['line'])))
            continue
        n = s['t'].count('\n') + 1
        got += [(s['col'], s['line'] + i) for i in range(n)]
    if got != want:
        i = next((k for k in range(min(len(got), len(want))) if got[k] != want[k]), min(len(got), len(want)))
        errs.append(f'units cover {len(got)} prism lines, the part has {len(want)}; first mismatch at {i}: '
                    f'units {got[i] if i < len(got) else None} vs Langdon {want[i] if i < len(want) else None}')
    else:
        report = []
        flat = []
        for s in story['sentences']:
            flat += ['(lost)'] if s.get('lost') else C.lines_tr(s)
        for (col, ln), ours, e in zip(want, flat, entries(p)):
            if ours == '(lost)':
                continue
            r = C.ratio(ours, e['t'])
            if r < 0.7:
                report.append(f'{col} {ln}: ours {ours!r} · Langdon {e["t"]!r} · {r:.2f}')
        open(os.path.join(R.drafts('king-list', p['id']), 'linecheck.md'), 'w', encoding='utf-8').write(
            f'# Line check — {p["id"]}\n\nLines whose sign values differ from Langdon\'s transliteration; confirm each on the plate.\n\n'
            + '\n'.join(f'- {x}' for x in report) + '\n')
        if report:
            warns.append(f'{len(report)} line(s) differ from Langdon — see drafts/{p["id"]}/linecheck.md')
    S = C.signs()
    e2, w2 = R.words_checks(story, S)
    e3, w3 = C.glyph_checks(story, S)
    return errs + e2 + e3, warns + w2 + w3

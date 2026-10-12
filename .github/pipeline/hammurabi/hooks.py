"""Laws of Hammurabi — work hooks for .github/pipeline/run3/r3.py.

Cuneiform words model, as in the five published parts (hammurabi-prologue … hammurabi-laws-26-41).
The drafter identifies every sign on Harper's autograph plates and writes words with glyph SIGN KEYS; the
build takes each glyph character from the shared sign glossary (signs-cuneiform.json — whose glyphs were
themselves taken from Unicode names), builds `t` with a line break at every stele line, and checks that
the units cover exactly the part's stele lines (stele parts) or established witness lines (gap parts).

Two kinds of part:
  stele  — Harper 1904's transliteration of the stele (source/hammurabi-harper1904-source.json), §42 → end.
  gap    — the section chiselled off the stele, from duplicate tablets; its text is established by the
           run itself from the public-domain witness editions (source/witnesses/) and pinned as
           source/established/<id>.json before it is drafted.
"""
import difflib, json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R
import cun as C

SRC = os.path.join(HERE, 'source', 'hammurabi-harper1904-source.json')
PLATES = os.path.join(HERE, 'source', 'harper-plates.json')
EST = os.path.join(HERE, 'source', 'established')
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
_c = {}


def roman(s):
    v = 0
    for a, b in zip(s, s[1:] + ' '):
        v += -ROMAN[a] if b != ' ' and ROMAN.get(b, 0) > ROMAN[a] else ROMAN[a]
    return v


def src():
    if 'src' not in _c:
        _c['src'] = R.jload(SRC)
    return _c['src']


def stele_lines(p):
    L = src()['lines']
    return L[p['from']:p['to'] + 1]


def est_path(p):
    return os.path.join(EST, p['id'] + '.json')


def slice_source(p):
    if p['kind'] == 'stele':
        return '\n'.join(f'{l["col"]} {l["ln"]}\t{l["t"]}' for l in stele_lines(p))
    if not os.path.exists(est_path(p)):
        return None
    return json.dumps(R.jload(est_path(p)), ensure_ascii=False, sort_keys=True)


# ------------------------------------------------------------------ establishment (gap parts)
def establish_packet(p):
    if p['kind'] != 'gap':
        R.die(p['id'], 'is a stele part: its text is already pinned (Harper); nothing to establish')
    w = os.path.join(HERE, 'source', 'witnesses')
    return f"""# Establish — {p['id']}: {p['name']}

You are establishing the text of part of the section that was chiselled off the stele (between §65 and
§100), from the ancient duplicate tablets, in public-domain editions only. Nothing is drafted in this run.
**Establishing hammurabi-gap-a establishes the whole erased section** — write BOTH
source/established/hammurabi-gap-a.json (the house-and-neighbour laws, Ungnad's §66 to about §78) and
source/established/hammurabi-gap-b.json (the merchant-and-loan laws before §100), then pin both
(`python3 ../run3/r3.py pin hammurabi hammurabi-gap-a` and `… hammurabi-gap-b`). If gap-a is already
established, gap-b needs nothing more than its pin.

Witness editions (all pre-1930, all in source/witnesses/):
- kpu-vol2_djvu.txt + kpu-vol2-ungnad1909.pdf — Kohler & Ungnad, Hammurabi's Gesetz II (1909), pp. 33–37
  (PDF: find the pages headed "XVII 2—XVIII 3", "XVIII 4—51", "XVIII 52—XXIII 7"): Ungnad's syllabic
  transliteration of the gap laws with, for each stretch, the tablet it comes from (Scheil's Susa
  Fragments I and II — Délégation en Perse X p. 81 ff.; Rm. 277; DT 81; K 8321). Roman type = preserved on
  the Old Babylonian duplicates; italic = restored from the Assyrian copies; [ ] = restored. Anhang
  pp. 180–182 lists every duplicate and what it covers.
- ungnad1909-keilschrifttexte-b.pdf — Ungnad, Keilschrifttexte der Gesetze Hammurapis (1909): his
  autographs of those fragments. The signs come from HERE (read the plate for each line), the readings
  from KPU II.
- poebel1914-pbs5.pdf — Poebel, Historical and Grammatical Texts (PBS V, 1914), no. 93, Plates XXXIX
  (obverse, PDF page 89) and XL (reverse, PDF page 91): the Nippur tablet of the Code (University Museum,
  Philadelphia), which preserves merchant-and-loan laws of the gap.
- cuq1918-nouveaux-fragments.pdf / cuq1918_djvu.txt — Cuq (1918): Scheil's reading of that tablet,
  transliterated (see djvu lines ~430–600 for the Akkadian). Use it as the reading aid for PBS V 93;
  the signs come from Poebel's plates.
- kpu-vol3_djvu.txt pp. 265–267 — Ungnad's translation of the new fragments (for sense only).

Rules (Zev's decision, 2026-10-11): fill the gap from the duplicates; mark every passage with the tablet
it comes from; show a loss that no surviving copy preserves as a gap, never reconstruct it. Restorations
in [ ] made by the 1909/1914/1918 editors from parallel copies are reported in the notes, not adopted
as signs — the signs are what the tablet shows. Where a gap law is known only from a tablet published
after 1930, the fallback is the Aqhat rule: its attested signs may be taken from any edition, never that
edition's restorations or translation — but no such edition is in this repository, so such a law is
shown as a gap and listed in QUESTIONS.md.

Write each established file as JSON:
{{"witnesses": {{"<siglum>": "<tablet, edition, page/plate>"}},
  "laws": [{{"law": 66, "approx": false, "units": [{{"w": "<siglum>", "ref": "<tablet col. line–line>",
            "lines": ["<transliteration of one tablet line, in KPU/Cuq notation>", ...],
            "lost": false}}]}}],
  "gaps": ["<what is lost, where>"]}}
"law" is Ungnad's number (his "§ cca. 71" → 71 with "approx": true). A wholly lost stretch is a unit with
"lost": true, "lines": [] and a ref saying how much is missing. Then run the pin command; it checks the file.
"""


def check_established(p):
    errs = []
    path = est_path(p)
    if not os.path.exists(path):
        return [f'{os.path.relpath(path, R.ROOT)} does not exist']
    d = R.jload(path)
    if not d.get('witnesses') or not d.get('laws'):
        errs.append('needs witnesses and laws')
    for law in d.get('laws', []):
        if not isinstance(law.get('law'), int):
            errs.append(f'law number must be an integer: {law.get("law")!r}')
        for u in law.get('units', []):
            if u.get('w') not in d.get('witnesses', {}):
                errs.append(f'law {law.get("law")}: unknown witness {u.get("w")!r}')
            if not u.get('lost') and not u.get('lines'):
                errs.append(f'law {law.get("law")}: a unit with no lines must be marked lost')
    return errs


# ------------------------------------------------------------------ packet
def packet(p):
    out = [f'# Packet — {p["id"]}: {p["name"]}', '']
    if p['kind'] == 'stele':
        PL = R.jload(PLATES)
        cols = []
        for l in stele_lines(p):
            if l['col'] not in cols:
                cols.append(l['col'])
        pages = [x for x in PL['plates'] if set(x['cols']) & set(cols)]
        out += [f'Stele {p["cite"]} — {p["lines"]} lines of Harper\'s transliteration (pp. {stele_lines(p)[0]["harper_page"]}–{stele_lines(p)[-1]["harper_page"]}).',
                '', '## Where the signs are',
                f'Harper\'s autograph plates in source/harper1904-cornell.pdf (render with pymupdf at 200–300 dpi and read them):',
                ''] + [f'- Plate {x["plate"]} = PDF page {x["page"]} (columns {", ".join(x["cols"])})' for x in pages] + [
                f'- Harper\'s List of Signs: PDF pages {PL["signList"][0]}–{PL["signList"][1]}', '',
                '## Harper\'s transliteration, line by line (col · line · text)',
                'Raised text in braces: {b}, {ilu} = the divine determinative (write it {d} with the AN sign, role det), '
                '{amêlu} = the LÚ determinative, {kam}. Harper writes many logograms as the Akkadian word '
                '(eḳlam for A.ŠÀ) — the plate decides the sign. ḳ = q.', '']
        sec = None
        for l in stele_lines(p):
            s = src()['sections'][l['sec']]['heading']
            if s != sec:
                sec = s
                out.append(f'\n### {s}\n')
            out.append(f'{l["col"]} {l["ln"]}\t{l["t"]}' + ('' if l.get('flag') is None else f'\t[flag: {l.get("flag")}]'))
        app = [a['note'] for a in src().get('apparatus', []) if any(f'{c} ' in a.get('note', '') or f'Col. {c}' in a.get('note', '') for c in cols)]
        if app:
            out += ['', '## Notes from the transcription (apparatus)', ''] + [f'- {a}' for a in app[:60]]
    else:
        d = R.jload(est_path(p))
        out += ['Established gap text (pinned):', '', '```json', json.dumps(d, ensure_ascii=False, indent=1), '```', '',
                'Signs: read them on the witness autographs named for each unit (source/witnesses/).']
    S = C.signs()
    out += ['', '## Signs already in the shared sign glossary (signs-cuneiform.json) — key: values', '']
    out += [f'- {k}: {", ".join(v.get("values", []) or [v.get("sound") or ""])[:120]}' for k, v in S.items()]
    return '\n'.join(out) + '\n'


# ------------------------------------------------------------------ assembly
def assemble(p, units, gloss):
    cfg = R.work_cfg('hammurabi')
    S = C.signs()
    G = R.merged_inline_glossary('hammurabi')
    G.update({k: v for k, v in gloss.items() if v and k != '__broaden__'})
    G.update(gloss.get('__broaden__', {}))
    sents, problems = [], []
    for k, u in enumerate(units['sentences']):
        words = C.fill_words(u, S, G, k, problems)
        s = {'t': C.build_t(words), 'l': u['l'], 'words': words}
        if 'ln' in u:                                  # the first unit of each law (or every epilogue unit)
            s['ln'] = u['ln']
        for f in ('i', 'n', 'p'):
            if u.get(f):
                s[f] = u[f]
        for f in ('col', 'line', 'w', 'ref'):         # kept in the story: the validator re-checks coverage from them
            if f in u:
                s[f] = u[f]
        sents.append(s)
    first = sents[0]['words'][:2] if sents and sents[0].get('words') else []
    story = dict(cfg['header'])
    story.update({'id': p['id'],
                  'title': units.get('title') or ' '.join(''.join(g['s'] for g in w['glyphs']) for w in first),
                  'titleRead': units.get('titleRead') or ' '.join(w['say'] for w in first),
                  'titleEn': units['titleEn'], 'part': units['part'], 'numbering': p.get('numbering', 'clause'),
                  'provisional': True, 'draftNote': units.get('draftNote') or cfg['draftNote'],
                  'source': units.get('source') or cfg['sourceStatement'], 'images': cfg['images'],
                  'about': units.get('about', ''), 'sentences': sents})
    used = {m['lemma'] for s in sents for w in s['words'] for m in w['morph']}
    story['glossary'] = {k: G[k] for k in sorted(used) if k in G}
    story['_problems'] = problems
    return story, {}


def validate(p, story):
    errs, warns = list(story.pop('_problems', [])), []
    sents = story['sentences']
    # line coverage: units take the part's stele lines in order; a unit may run on into the next column
    want = [(l['col'], l['ln']) for l in stele_lines(p)] if p['kind'] == 'stele' else []
    got, pos = [], 0
    for k, s in enumerate(sents):
        n = s['t'].count('\n') + 1 if s['t'] else 0
        if p['kind'] == 'stele':
            col, line = s.get('col'), s.get('line')
            if col is None or line is None:
                errs.append(f'unit {k}: needs col and line (its first stele line)')
                continue
            if pos < len(want) and (col, line) != want[pos]:
                errs.append(f'unit {k}: starts at {col} {line}, but the next stele line is {want[pos][0]} {want[pos][1]}')
            got += want[pos:pos + n]
            pos += n
        if p['kind'] == 'gap' and not (s.get('w') and s.get('ref')):
            errs.append(f'unit {k}: a gap unit must name its witness ("w") and its place on that tablet ("ref")')
        if p['kind'] == 'gap' and s.get('w') and s['w'] not in (s.get('n') or ''):
            errs.append(f'unit {k}: its note must contain the witness siglum exactly as written in "w" ({s["w"]})')
    if p['kind'] == 'stele':
        if pos != len(want):
            errs.append(f'units cover {pos} stele lines, the part has {len(want)}')
        else:
            report, bad = [], 0
            flat = [x for s in sents for x in C.lines_tr(s)]
            for (col, ln), ours, h in zip(want, flat, stele_lines(p)):
                r = C.ratio(ours, h['t'])
                if r < 0.75:
                    bad += 1
                    report.append(f'{col} {ln}: ours {ours!r} · Harper {h["t"]!r} · {r:.2f}')
            path = os.path.join(R.drafts('hammurabi', p['id']), 'linecheck.md')
            open(path, 'w', encoding='utf-8').write(
                f'# Line check — {p["id"]}\n\nStele lines whose sign values differ from Harper\'s transliteration '
                f'(ratio < 0.75 after stripping accents, indices, braces). Most are logograms Harper writes as the '
                f'Akkadian word; each must be confirmed on the plate.\n\n' + '\n'.join(f'- {x}' for x in report) + '\n')
            if bad:
                warns.append(f'{bad} stele line(s) differ from Harper\'s transliteration — see drafts/{p["id"]}/linecheck.md; '
                             f'the reviewer confirms every one on the plate')
    # glyph/role/sign checks
    S = C.signs()
    e2, w2 = R.words_checks(story, S)
    e3, w3 = C.glyph_checks(story, S)
    errs += e2 + e3
    warns += w2 + w3
    for k, s in enumerate(sents):
        for j, w in enumerate(s['words']):
            for g in w['glyphs']:
                if g['role'] == 'log' and g.get('tr', '') != g.get('tr', '').upper():
                    warns.append(f'unit {k} word {j}: logogram tr {g.get("tr")!r} should be the CAPS Sumerogram')
    if p['kind'] == 'gap' and os.path.exists(est_path(p)):
        d = R.jload(est_path(p))
        want = [u['ref'] for law in d['laws'] for u in law['units'] if not u.get('lost')]
        have = []
        for s in sents:
            if s.get('ref') not in have:
                have.append(s.get('ref'))
        missing = [r for r in want if r not in have]
        if missing:
            errs.append(f'established passages not drafted: {missing[:8]}')
        est = {u['ref']: u.get('lines', []) for law in d['laws'] for u in law['units'] if not u.get('lost')}
        drafted = {}
        for s in sents:
            if s.get('ref') in est:
                drafted.setdefault(s['ref'], []).extend(C.lines_tr(s))
        for ref, lines in drafted.items():
            if len(lines) != len(est[ref]):
                errs.append(f'{ref}: {len(lines)} written lines drafted, the established text has {len(est[ref])}')
                continue
            for ours, theirs in zip(lines, est[ref]):
                if C.ratio(ours, theirs) < 0.7:
                    warns.append(f'{ref}: ours {ours!r} vs established {theirs!r} — confirm on the autograph')
    return errs, warns

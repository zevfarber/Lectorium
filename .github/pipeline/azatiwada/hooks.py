"""Azatiwada (KARATEPE 1, Hieroglyphic Luwian) — work hooks for .github/pipeline/run3/r3.py.

Words model with per-glyph Laroche sign keys, as in the pilot azatiwada-luwian (§1–§21, 2026-07-12).
The pinned source (source/source.json) is the ACLT 2 corpus text of copy Hu. (docs/96), parsed word by word
with every sign's transliteration, its Laroche key (verified against the Unicode Anatolian Hieroglyphs
names list and sign lists, see source/sign-verification.json), register breaks and damage, plus ACLT's
clitic-level transcription and lemma glosses (facts, per the Luwian amendment of 2026-07-11).

The drafter writes one unit per clause (ln = the clause number) with words whose glyphs are
{"keys": ["A439", "A383"], "role": ..., "tr": "wa/i+ra/i"} — a ligature or compound is ONE glyph with
several keys, as in the pilot. The build takes every character from signs-anatolian.json."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

SRC = os.path.join(HERE, 'source', 'source.json')
SIGNS = os.path.join(R.ROOT, 'signs-anatolian.json')


def signs():
    return R.jload(SIGNS)['signs']


def clauses(p):
    ids = p['clause_ids']
    C = {c['clause']: c for c in R.jload(SRC)['clauses']}
    return [C[i] for i in ids]


def slice_source(p):
    return json.dumps(clauses(p), ensure_ascii=False, sort_keys=True)


def src_units(word):
    """The source word as a list of glyph-units, each a list of (key, tr)."""
    if not word.get('signs'):                      # an ACLT lacuna marker: lost word(s)
        return [[('DAMAGED', '[…]')]]
    us = {}
    for s in word['signs']:
        for k in (s.get('sign') or 'DAMAGED').split('+'):      # a sign keyed as a ligature (A110+A383) = its parts
            us.setdefault(s.get('unit', 0), []).append((k, s['tr']))
    return [us[k] for k in sorted(us)]


def packet(p):
    out = [f'# Packet — {p["id"]}: {p["name"]} ({p["clauses"]})', '',
           'Base copy Hu. (ACLT docs/96). One unit per clause, ln = clause number. For each written word below: '
           'the ACLT transliteration, its glyph-units (sign key · value; a unit of several signs joined by + or . '
           'is ONE glyph with several keys), the interpreted word, and ACLT\'s clitic-level lemmas and glosses '
           '(facts — use them for morph; the English translation is yours, from the grammar). "lb" = a register '
           'break before the word (word nl) or before a sign (glyph nl). Damage: show damaged signs as the corpus '
           'does, lost ones with the DAMAGED placeholder ▢; supplied <…> signs are editorial — say so in the note.', '']
    for c in clauses(p):
        out.append(f'\n## §{c["clause"]}' + (' — ABSENT in both copies' if c.get('absent') else f' ({c.get("copy")}, {c.get("damage_state", "")})'))
        if c.get('absent'):
            out.append(c.get('note', ''))
            continue
        out.append(f'transcription: {c["transcription_text"]}')
        out.append(f'transliteration: {c["transliteration_text"]}')
        for j, w in enumerate(c['words']):
            us = ' | '.join('+'.join(f'{k}·{tr}' for k, tr in u) for u in src_units(w))
            flags = ' [lb]' if w.get('lb_before') else ''
            src_flags = sorted({str(s.get('sign_source')) + (': ' + s['sign_note'] if s.get('sign_note') else '') for s in w.get('signs', []) if s.get('sign_source') not in ('pilot', 'laroche', 'verified')})
            dmg = sorted({s.get('damage') for s in w.get('signs', []) if s.get('damage')})
            tw = '; '.join(f'{x["text"]} = {x.get("lemma")} ({x.get("pos")}{", " + x["gr"] if x.get("gr") else ""}) “{x.get("gloss")}”'
                           for x in w.get('transcription_words', []) if x.get('kind') == 'word')
            out.append(f'- w{j}{flags}: {w["translit"]} → {w.get("transcription", "(lost)")} :: units {us}'
                       + (f' :: damage {dmg}' if dmg else '') + (f' :: sign keys to treat with care {src_flags}' if src_flags else '')
                       + f' :: {tw}')
        if c.get('parallel'):
            out.append(f'(Ho., reference only: {c["parallel"] if isinstance(c["parallel"], str) else json.dumps(c["parallel"], ensure_ascii=False)[:400]})')
    return '\n'.join(out) + '\n'


def assemble(p, units, gloss):
    cfg = R.work_cfg('azatiwada')
    S = signs()
    G = {}
    for f in sorted(os.listdir(R.ROOT)):
        if f.startswith('azatiwada-') and f.endswith('.json'):
            G.update(R.jload(os.path.join(R.ROOT, f)).get('glossary', {}))
    G.update({k: v for k, v in gloss.items() if v and k != '__broaden__'})
    G.update(gloss.get('__broaden__', {}))
    sents, problems = [], []
    for k, u in enumerate(units['sentences']):
        words = []
        for j, w in enumerate(u['words']):
            gl = []
            for g in w['glyphs']:
                keys = g.get('keys') or [g.get('sign')]
                miss = [x for x in keys if x not in S]
                if miss:
                    problems.append(f'unit {k} word {j}: sign(s) {miss} not in signs-anatolian.json — add with run3/signs.py')
                    continue
                ng = {'s': ''.join(S[x]['glyph'] for x in keys), 'role': g['role'], 'tr': g['tr'], 'sign': keys[0]}
                if len(keys) > 1:
                    ng['keys'] = keys
                for f in ('nl', 'damaged'):
                    if g.get(f):
                        ng[f] = g[f]
                gl.append(ng)
            nw = {'reading': w['reading'], 'say': w.get('say', w['reading']), 'glyphs': gl,
                  'morph': [{'lemma': m['lemma'], 'gloss': m.get('gloss') or G.get(m['lemma'], ''), 'g': m['g']} for m in w.get('morph', [])]}
            if w.get('nl'):
                nw['nl'] = True
            words.append(nw)
        s = {'t': ' '.join(''.join(g['s'] for g in w['glyphs']) for w in words), 'l': u['l'], 'ln': u['ln'], 'words': words}
        for f in ('i', 'n', 'p', 'absent'):
            if u.get(f):
                s[f] = u[f]
        sents.append(s)
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': cfg['title'], 'titleEn': units['titleEn'], 'part': units['part'],
                  'numbering': 'clause', 'provisional': True, 'draftNote': cfg['draftNote'],
                  'source': cfg['sourceStatement'].replace('{cite}', p['clauses']), 'images': cfg['images'],
                  'about': units.get('about', ''), 'sentences': sents})
    used = {m['lemma'] for s in sents for w in s['words'] for m in w['morph']}
    story['glossary'] = {k: G[k] for k in sorted(used) if k in G}
    story['_problems'] = problems
    return story, {}


def validate(p, story):
    errs, warns = list(story.pop('_problems', [])), []
    S = signs()
    cl = clauses(p)
    want = [int(re.match(r'\d+', c['clause']).group()) for c in cl]
    got = [s['ln'] for s in story['sentences']]
    if got != want:
        errs.append(f'units are clauses {got}; the part has {want}')
    for c, s in zip(cl, story['sentences']):
        if c.get('absent'):
            if not s.get('absent'):
                errs.append(f'§{c["clause"]}: absent in both copies — the unit must be a gap unit with "absent": true and a note saying so')
            continue
        srcw = [u for w in c['words'] for u in [src_units(w)]]
        if len(srcw) != len(s['words']):
            errs.append(f'§{c["clause"]}: {len(s["words"])} words drafted, the source has {len(srcw)}')
            continue
        for j, (sw, dw) in enumerate(zip(srcw, s['words'])):
            dk = [g.get('keys') or [g['sign']] for g in dw['glyphs']]
            sk = [[k for k, _ in u] for u in sw]
            if dk != sk:
                errs.append(f'§{c["clause"]} word {j}: glyph keys {dk} differ from the source {sk}')
    for k, s in enumerate(story['sentences']):
        for j, w in enumerate(s['words']):
            for g in w['glyphs']:
                keys = g.get('keys') or [g['sign']]
                if g['s'] != ''.join(S.get(x, {}).get('glyph', '?') for x in keys):
                    errs.append(f'unit {k} word {j}: glyph characters do not match the sign glossary')
            for m in w['morph']:
                if not m['gloss']:
                    errs.append(f'unit {k} word {j}: lemma {m["lemma"]!r} has no gloss')
    e2, w2 = R.words_checks(story, S)
    return errs + e2, warns + w2

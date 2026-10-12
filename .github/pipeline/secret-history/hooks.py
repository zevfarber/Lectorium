"""Secret History of the Mongols — work hooks for .github/pipeline/run3/r3.py.

Words model, one glyph per word (the Chinese-character transcription of the Mongol word), as in the pilot
secret-history-01-06 (2026-07-29). The source gives every word's Ming gloss, Han transcription and
Shiratori's romanization; the build makes glyphs, readings and t from it. The drafter supplies the sense-units
(t = the romanized words joined by single spaces, cut in order), l / i / n, and each word's morph list
(lemma = dictionary form, gloss with the Ming gloss in square brackets), plus glossary entries for new tokens."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

SRC = os.path.join(HERE, 'source', 'secret-history-shiratori.json')
GLOSS = os.path.join(R.ROOT, 'secret-history-glossary.json')
FVS = {'᠋', '᠌'}          # the edition's "draw small" markup — stripped at publication (pilot rule)
_cache = {}


def _src():
    if 'src' not in _cache:
        _cache['src'] = R.jload(SRC)
    return _cache['src']


def sec_words(n):
    out = []
    for line in _src()['sections'][str(n)]['lines']:
        for w in line['words']:
            out.append(dict(w, line=line['id'], sec=n))
    return out


def part_words(p):
    out = []
    for n in range(p['from'], p['to'] + 1):
        out += sec_words(n)
    return out


def slice_source(p):
    return '\n'.join(f'{w["sec"]}|{w["line"]}|{w["gloss"]}|{w["han"]}|{w["rom"]}' for w in part_words(p))


EDGE = '.,:;!?"\'“”‘’«»()[]'


def bare(rom):
    """The word without the punctuation Shiratori attaches to it (kept in t and in the glyph's tr, dropped from the word's reading — as in the pilot)."""
    return rom.strip(EDGE)


def strip_fvs(s):
    return ''.join(c for c in s if c not in FVS)


def glossary():
    return R.jload(GLOSS)['glossary']


def forms(p):
    g = glossary()
    novel, known = {}, {}
    for w in part_words(p):
        for tok in R.tokens(w['rom']):
            if tok in g:
                known[tok] = g[tok]
            elif tok not in novel:
                novel[tok] = f'[{w["gloss"]}]'
    return novel, known


def packet(p):
    out = [f'# Packet — {p["id"]} (§§{p["from"]}–{p["to"]})', '',
           'Every word of the part, in order: index · § · line · Ming gloss · Han transcription · romanized Mongol.',
           'A unit\'s `t` is the romanized words of a run of consecutive indices joined by single spaces — cut it by '
           'script from this list. Each unit must also carry `words`: one entry per word, in order, each '
           '`{"morph": [{"lemma": ..., "gloss": "... [Ming gloss]"}]}` (one morph per morpheme the reader sees, '
           'e.g. qaγan + -(n)u).', '']
    sec = None
    for i, w in enumerate(part_words(p)):
        if w['sec'] != sec:
            sec = w['sec']
            out.append(f'\n## §{sec}\n')
        out.append(f'{i} · §{w["sec"]} · {w["line"]} · {w["gloss"]} · {strip_fvs(w["han"])} · {w["rom"]}')
    return '\n'.join(out) + '\n'


def assemble(p, units, gloss):
    cfg = R.work_cfg('secret-history')
    words = part_words(p)
    G = R.jload(GLOSS)
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    new = {k: v for k, v in gloss.items() if v and k not in G['glossary']}
    G['glossary'].update(new)
    G['glossary'].update(broaden)
    sents, pos = [], 0
    for k, u in enumerate(units['sentences']):
        n = len(u.get('words', []))
        ws = words[pos:pos + n]
        built = []
        for src, du in zip(ws, u.get('words', [])):
            han = strip_fvs(src['han'])
            built.append({'reading': f'{han} {bare(src["rom"])}',
                          'glyphs': [{'s': han, 'tr': src['rom'], 'role': 'phon'}],
                          'morph': [{'lemma': m['lemma'], 'gloss': m['gloss'], 'g': [0]} for m in du.get('morph', [])]})
        s = {'t': ' '.join(w['rom'] for w in ws), 'words': built, 'l': u.get('l', ''), 'ln': ws[0]['sec'] if ws else None}
        for f in ('i', 'n'):
            if u.get(f):
                s[f] = u[f]
        if u.get('p') or (ws and (pos == 0 or words[pos - 1]['sec'] != ws[0]['sec'])):
            s['p'] = True
        if u.get('t') and u['t'] != s['t']:
            s['_t_mismatch'] = u['t']
        sents.append(s)
        pos += n
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': f'元朝秘史 §§{p["from"]}–{p["to"]}',
                  'titleRead': f'Mongγol-un niγuča tobčiyan §§{p["from"]}–{p["to"]}',
                  'titleEn': units['titleEn'], 'part': units['part'],
                  'glossaryFile': 'secret-history-glossary.json',
                  'source': cfg['sourceStatement'].replace('{cite}', f'§§{p["from"]}–{p["to"]}'),
                  'about': units.get('about', ''), 'provisional': True,
                  'draftNote': cfg.get('draftNote', ''), 'sentences': sents})
    for k in ('about', 'draftNote'):
        if not story[k]:
            del story[k]
    story['_consumed'] = pos
    return story, {GLOSS: G}


def validate(p, story):
    errs, warns = [], []
    words = part_words(p)
    consumed = story.pop('_consumed', None)
    flat = [w for s in story['sentences'] for w in s['words']]
    if len(flat) != len(words):
        errs.append(f'units hold {len(flat)} words; the source part has {len(words)}')
    for k, s in enumerate(story['sentences']):
        if '_t_mismatch' in s:
            errs.append(f'unit {k}: the drafter\'s t {s["_t_mismatch"]!r} is not the source words {s["t"]!r}')
        if any(c in FVS for c in json.dumps(s, ensure_ascii=False)):
            errs.append(f'unit {k}: FVS markup left in')
    for a, b in zip(flat, words):
        if a['glyphs'][0]['s'] != strip_fvs(b['han']) or a['glyphs'][0]['tr'] != b['rom']:
            errs.append(f'word {b["rom"]}: glyph does not reproduce the source')
            break
    G = R.jload(GLOSS)['glossary']
    for k, s in enumerate(story['sentences']):
        for tok in R.tokens(s['t']):
            if tok not in G:
                errs.append(f'unit {k}: token {tok!r} has no glossary entry')
        for j, w in enumerate(s['words']):
            if not w['morph']:
                errs.append(f'unit {k} word {j}: no morph')
            for m in w['morph']:
                if not m.get('gloss'):
                    errs.append(f'unit {k} word {j}: morph without gloss')
        if s.get('ln') is None:
            errs.append(f'unit {k}: no § number')
    secs = [s['ln'] for s in story['sentences']]
    if secs != sorted(secs):
        errs.append('§ numbers out of order')
    if words and (secs[0] != p['from'] or secs[-1] != p['to']):
        errs.append('units do not run from the first to the last § of the part')
    for v in G.values():
        if ' — ' not in v:
            warns.append(f'glossary entry without " — ": {v[:40]!r}')
            break
    e2, w2 = R.words_checks(story)
    return errs + e2, warns + w2

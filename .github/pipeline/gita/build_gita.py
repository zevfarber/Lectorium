#!/usr/bin/env python3
"""Build gita-chNN.json from the drafter's files for one chapter.

    python3 build_gita.py NN            → writes ../../../gita-chNN.json (the repository root)
    python3 build_gita.py NN --out PATH

Inputs, in drafts/chNN/:
  words.txt   one block per verse:  "#<verse>" then one line per Devanagari token
              "<token>|<sandhi-split IAST reading>|<lemma — gloss>;;<lemma — gloss>…", with a line
              "--" between the verse's lines (a 2-line śloka has one "--", a 4-line triṣṭubh has three).
  trans.txt   one block per verse:  "#<verse>" then "L: literal", "I: idiomatic", "N: note" lines
              (I may be omitted when it would equal L; N is optional).
The Devanagari tokens must tile the corrected source text exactly (gita_lib.read_wikisource);
the script refuses to build otherwise. Speaker lines are generated. Everything else — the story
metadata, the words model, the glossary — follows conventions.md."""
import json, os, re, sys, unicodedata
from indic_transliteration import sanscript
import gita_lib as g

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

SPEAKERS = {
    'धृतराष्ट्र उवाच': ('dhṛtarāṣṭra uvāca', 'Dhṛtarāṣṭra said', [
        ('धृतराष्ट्र', 'dhṛtarāṣṭraḥ', 'Dhṛtarāṣṭra', 'Dhṛtarāṣṭra, the blind king of the Kurus, father of the hundred Kauravas (nom. sg.; final -ḥ dropped before the vowel u-)')]),
    'सञ्जय उवाच': ('sañjaya uvāca', 'Sañjaya said', [
        ('सञ्जय', 'sañjayaḥ', 'Sañjaya', "Sañjaya, the king's minister and charioteer, who reports the battle to him (nom. sg.)")]),
    'अर्जुन उवाच': ('arjuna uvāca', 'Arjuna said', [
        ('अर्जुन', 'arjunaḥ', 'Arjuna', 'Arjuna, the third Pāṇḍava, the great archer (nom. sg.)')]),
    'श्रीभगवानुवाच': ('śrībhagavān uvāca', 'The Blessed Lord said', [
        ('श्रीभगवानुवाच', 'śrī-bhagavān uvāca', 'śrī', 'holy, glorious (honorific prefix)'),
        ('', '', 'bhagavat', "the Blessed One, the Lord — Kṛṣṇa's title as speaker (nom. sg. bhagavān; -n + u- written joined)"),
        ('', '', 'vac', "to speak (uvāca: perfect 3rd sg. 'said')")]),
}
UVACA = ('उवाच', 'uvāca', 'vac', "to speak (uvāca: perfect 3rd sg. 'said')")

def parse_words(path):
    words, cur = {}, None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if not line.strip():
            continue
        if line.startswith('#'):
            cur = int(line[1:]); words[cur] = [[]]; continue
        if line.strip() == '--':
            words[cur].append([]); continue
        dev, reading, morphs = line.split('|')
        ms = []
        for m in morphs.split(';;'):
            lemma, gloss = m.split(' — ', 1)
            ms.append({'lemma': lemma.strip(), 'gloss': gloss.strip()})
        words[cur][-1].append({'dev': dev.strip(), 'reading': reading.strip(), 'morph': ms})
    return words

def parse_trans(path):
    trans, cur = {}, None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if line.startswith('#'):
            cur = int(line[1:]); trans[cur] = {}; continue
        if line[:2] in ('L:', 'I:', 'N:'):
            trans[cur][line[0].lower()] = line[2:].strip()
    return trans

def speaker_unit(sp, glossary):
    tr, en, ws = SPEAKERS[sp]
    wl = []
    if sp == 'श्रीभगवानुवाच':
        morph = [{'lemma': l, 'gloss': gl, 'g': [0]} for _, _, l, gl in ws]
        wl.append({'reading': 'śrī-bhagavān uvāca', 'glyphs': [{'s': sp, 'tr': 'śrī-bhagavān uvāca'}], 'morph': morph})
        glossary.setdefault(sp, 'śrī-bhagavān uvāca — ' + '; '.join(l + ' — ' + gl for _, _, l, gl in ws))
    else:
        for dev, reading, lemma, gloss in ws + [UVACA]:
            wl.append({'reading': reading, 'glyphs': [{'s': dev, 'tr': reading}], 'morph': [{'lemma': lemma, 'gloss': gloss, 'g': [0]}]})
            glossary.setdefault(dev, reading + ' — ' + lemma + ' — ' + gloss)
    return {'p': True, 't': sp, 'tr': tr, 'l': en, 'words': wl}

def build(ch, out=None):
    parts = json.load(open(os.path.join(HERE, 'parts.json'), encoding='utf-8'))
    part = next(p for p in parts['parts'] if p['chapter'] == ch)
    d = os.path.join(HERE, 'drafts', f'ch{ch:02d}')
    words = parse_words(os.path.join(d, 'words.txt'))
    trans = parse_trans(os.path.join(d, 'trans.txt'))
    verses = g.read_wikisource(ch)
    n = len(verses)
    assert sorted(words) == list(range(1, n + 1)), ('words.txt covers', sorted(words)[:3], '…', 'expected 1..%d' % n)
    assert sorted(trans) == list(range(1, n + 1)), 'trans.txt does not cover every verse'
    errors = 0
    for v in verses:
        if len(words[v['n']]) != len(v['lines']):
            errors += 1; print('LINE COUNT', ch, v['n'], len(words[v['n']]), 'blocks vs', len(v['lines']), 'source lines')
            continue
        for li, line in enumerate(v['lines']):
            want, got = line.split(), [w['dev'] for w in words[v['n']][li]]
            if want != got:
                errors += 1; print('MISMATCH', ch, v['n'], li + 1, '\n  src:', ' '.join(want), '\n  got:', ' '.join(got))
        if not trans[v['n']].get('l'):
            errors += 1; print('NO LITERAL', ch, v['n'])
    if errors:
        sys.exit('build refused: %d problem(s)' % errors)

    sentences, glossary = [], {}
    corr = g.corrections()
    for v in verses:
        if v['speaker']:
            sentences.append(speaker_unit(v['speaker'], glossary))
        wl, t_lines, tr_lines = [], [], []
        nl = len(v['lines'])
        for li, line in enumerate(v['lines']):
            t_lines.append(line + (' ॥' if li == nl - 1 else ' ।'))
            tr_lines.append(' '.join(w['reading'] for w in words[v['n']][li]))
            for wi, w in enumerate(words[v['n']][li]):
                glyphs = [{'s': w['dev'], 'tr': w['reading']}]
                if wi == len(words[v['n']][li]) - 1:
                    glyphs.append({'s': '॥' if li == nl - 1 else '।', 'tr': ' ', 'role': 'punct'})
                e = {'reading': w['reading'], 'glyphs': glyphs,
                     'morph': [{'lemma': m['lemma'], 'gloss': m['gloss'], 'g': [0]} for m in w['morph']]}
                if li > 0 and wi == 0:
                    e['br'] = True
                wl.append(e)
                glossary.setdefault(w['dev'], w['reading'] + ' — ' + '; '.join(m['lemma'] + ' — ' + m['gloss'] for m in w['morph']))
        s = {'ln': v['n'], 'v': True, 't': '\n'.join(t_lines), 'tr': ' |\n'.join(tr_lines) + ' ||', 'words': wl, 'l': trans[v['n']]['l']}
        i = re.sub(r'^(Sañjaya|Arjuna|Dhṛtarāṣṭra|The Blessed Lord) said: ', '', trans[v['n']].get('i', ''))
        if i: s['i'] = i
        note = trans[v['n']].get('n', '')
        key = f'{ch}.{v["n"]}'
        if key in corr and not any(c[1] in note or c[0] in note for c in corr[key]):
            sys.exit(f'build refused: the note to {key} must mention the correction {corr[key]}')
        if key in part['variantsVsBORI'] and 'BORI' not in note:
            sys.exit(f'build refused: {key} differs from the BORI text; its note must give the BORI reading')
        if note: s['n'] = note
        sentences.append(s)

    story = {
        'id': part['id'],
        'title': 'श्रीमद्भगवद्गीता — ' + part['title'],
        'titleRead': 'Bhagavadgītā — ' + part['titleTr'],
        'titleEn': 'The Bhagavad Gītā — Chapter %d: %s' % (ch, part['titleEn']),
        'work': 'श्रीमद्भगवद्गीता', 'workEn': 'The Bhagavad Gītā',
        'part': '%d · %s (%s)' % (ch, part['titleEn'], part['titleTr']),
        'language': 'Sanskrit', 'langCode': None, 'script': 'devanagari', 'numbering': 'stanza',
        'provisional': True,
        'draftNote': 'Prepared by the Lectorium pipeline from the vulgate text, with a drafting pass, a reviewing pass and a mechanical gate; a printed-edition collation and audio are still to come. Use ⚑ correction on any verse to report a problem.',
        'source': ("Text: the received (vulgate) text of the Bhagavadgītā, Mahābhārata 6.23–40, as read by Śaṅkara's commentary. "
                   "Devanagari from Sanskrit Wikisource (भगवद्गीता/%s), collated verse by verse against the GRETIL romanized text based on the "
                   "BORI critical edition (input Tokunaga, rev. J. Smith); every verse where the two differ carries a note giving the BORI reading, "
                   "and every correction to the Wikisource text is named in its note. Collation against a pre-1930 printed edition is still to be done. "
                   "Transliteration: IAST. The reading under each word gives the words with sandhi undone and compound members hyphenated, in the "
                   "manner of the traditional pada-pāṭha. Pronunciation convention: classical Sanskrit as described in Whitney's Sanskrit Grammar (1889); "
                   "no audio yet. Translations made fresh from the Sanskrit with Monier-Williams (1899), Apte (1890) and Śaṅkara's commentary for the "
                   "traditional sense; no modern translation consulted.") % part['title'],
        'sentences': sentences, 'glossary': glossary,
    }
    about = os.path.join(d, 'about.txt')
    if os.path.exists(about):
        story['about'] = open(about, encoding='utf-8').read().strip()
    out = out or os.path.join(ROOT, part['file'])
    json.dump(story, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', out, '| units', len(sentences), '| words', sum(len(s['words']) for s in sentences), '| glossary', len(glossary))
    return out

if __name__ == '__main__':
    ch = int(sys.argv[1])
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    build(ch, out)

import json, re, sys, unicodedata
from indic_transliteration import sanscript

import os; D = os.path.dirname(os.path.abspath(__file__)) + '/'
src = json.load(open(D + 'wiki-parsed.json'))
verses = {int(k): v for k, v in src['verses'].items()}
speaker = {int(k): v for k, v in src['speaker'].items()}
# one editorial correction to the Wikisource text (misprint), recorded in the note to 1.22
verses[22][0] = verses[22][0].replace('निरिक्षे', 'निरीक्षे')
assert 'निरीक्षे' in verses[22][0]

# ---- parse the word files ----
words = {}
for fn in ['words-01-16.txt', 'words-17-32.txt', 'words-33-47.txt']:
    cur = None
    for raw in open(D + fn, encoding='utf-8'):
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
assert sorted(words) == list(range(1, 48)), sorted(words)

# ---- parse translations ----
trans = {}
cur = None
for raw in open(D + 'trans.txt', encoding='utf-8'):
    line = raw.rstrip('\n')
    if line.startswith('#'):
        cur = int(line[1:]); trans[cur] = {}; continue
    if line[:2] in ('L:', 'I:', 'N:'):
        trans[cur][line[0].lower()] = line[2:].strip()
assert sorted(trans) == list(range(1, 48))

# ---- verify words against the source, line by line ----
errors = 0
for n in range(1, 48):
    for li, line in enumerate(verses[n]):
        want = line.split()
        got = [w['dev'] for w in words[n][li]]
        if want != got:
            errors += 1
            print('MISMATCH', n, li, '\n  src:', ' '.join(want), '\n  got:', ' '.join(got))
    # the reading, with hyphens and spaces removed, must transliterate back to the Devanagari letters
    for li, line in enumerate(verses[n]):
        for w in words[n][li]:
            back = re.sub(r"[\s\-']", '', sanscript.transliterate(w['dev'].replace('ऽ', ''), sanscript.DEVANAGARI, sanscript.IAST))
            rd = re.sub(r"[\s\-']", '', w['reading'])
            # sandhi-resolved reading differs from the surface at the joins; compare only if it is meant to be identical
            # (single-morph words with no sandhi note): report as info, not error
            if unicodedata.normalize('NFC', back) != unicodedata.normalize('NFC', rd) and len(w['morph']) == 1 and ' ' not in w['reading']:
                print('info: surface/reading differ (sandhi?)', n, w['dev'], back, rd)
if errors:
    sys.exit('word/source mismatches: %d' % errors)

# ---- assemble ----
SPEAK = {'धृतराष्ट्र उवाच': ('dhṛtarāṣṭra uvāca', 'Dhṛtarāṣṭra said', [('धृतराष्ट्र', 'dhṛtarāṣṭraḥ', 'Dhṛtarāṣṭra', 'Dhṛtarāṣṭra, the blind king of the Kurus, father of the hundred Kauravas (nom. sg.; final -ḥ dropped before the vowel u-)'), ('उवाच', 'uvāca', 'vac', 'to speak (uvāca: perfect 3rd sg. \'said\')')]),
         'सञ्जय उवाच': ('sañjaya uvāca', 'Sañjaya said', [('सञ्जय', 'sañjayaḥ', 'Sañjaya', 'Sañjaya, the king\'s minister and charioteer, who reports the battle to him (nom. sg.)'), ('उवाच', 'uvāca', 'vac', 'to speak (uvāca: perfect 3rd sg. \'said\')')]),
         'अर्जुन उवाच': ('arjuna uvāca', 'Arjuna said', [('अर्जुन', 'arjunaḥ', 'Arjuna', 'Arjuna, the third Pāṇḍava, the great archer (nom. sg.)'), ('उवाच', 'uvāca', 'vac', 'to speak (uvāca: perfect 3rd sg. \'said\')')])}

sentences = []
glossary = {}
def gkey(dev):
    return dev
for n in range(1, 48):
    if n in speaker:
        sp = speaker[n]; tr, en, ws = SPEAK[sp]
        wl = []
        for dev, reading, lemma, gloss in ws:
            wl.append({'reading': reading, 'glyphs': [{'s': dev, 'tr': reading}], 'morph': [{'lemma': lemma, 'gloss': gloss, 'g': [0]}]})
            glossary.setdefault(dev, reading + ' — ' + lemma + ' — ' + gloss)
        sentences.append({'p': True, 't': sp, 'tr': tr, 'l': en, 'words': wl})
    t_lines = [verses[n][0] + ' ।', verses[n][1] + ' ॥']
    tr_lines = []
    wl = []
    for li in range(2):
        tr_lines.append(' '.join(w['reading'] for w in words[n][li]))
        for wi, w in enumerate(words[n][li]):
            glyphs = [{'s': w['dev'], 'tr': w['reading']}]
            if wi == len(words[n][li]) - 1:
                glyphs.append({'s': '।' if li == 0 else '॥', 'tr': ' ', 'role': 'punct'})
            entry = {'reading': w['reading'], 'glyphs': glyphs,
                     'morph': [{'lemma': m['lemma'], 'gloss': m['gloss'], 'g': [0]} for m in w['morph']]}
            if li == 1 and wi == 0:
                entry['br'] = True
            wl.append(entry)
            glossary.setdefault(w['dev'], w['reading'] + ' — ' + '; '.join(m['lemma'] + ' — ' + m['gloss'] for m in w['morph']))
    s = {'ln': n, 'v': True, 't': '\n'.join(t_lines), 'tr': ' |\n'.join(tr_lines) + ' ||',
         'words': wl, 'l': trans[n]['l']}
    i = trans[n].get('i', '')
    i = re.sub(r'^(Sañjaya|Arjuna|Dhṛtarāṣṭra) said: ', '', i)
    if i: s['i'] = i
    if trans[n].get('n'): s['n'] = trans[n]['n']
    sentences.append(s)

story = {
    'id': 'gita-ch01',
    'title': 'श्रीमद्भगवद्गीता — अर्जुनविषादयोगः',
    'titleRead': 'Bhagavadgītā — Arjunaviṣādayoga',
    'titleEn': "The Bhagavad Gītā — Chapter 1: Arjuna's Despair",
    'work': 'श्रीमद्भगवद्गीता',
    'workEn': 'The Bhagavad Gītā',
    'part': "1 · Arjuna's Despair (Arjunaviṣādayoga)",
    'language': 'Sanskrit',
    'langCode': None,
    'script': 'devanagari',
    'numbering': 'stanza',
    'provisional': True,
    'draftNote': 'Pilot chapter (2026-09-15): first Sanskrit text in Lectorium and first use of the words model for an alphabetic script, to prove the sandhi-split reading layer. Chapters 2–18 to follow by scheduled runs once the presentation is approved.',
    'source': "Text: the received (vulgate) text of the Bhagavadgītā, Mahābhārata 6.23–40, as read by Śaṅkara's commentary. Devanagari from Sanskrit Wikisource (भगवद्गीता/अर्जुनविषादयोगः), collated verse by verse against the GRETIL e-text of the Bhagavadgītā with Śaṅkara's commentary (input Gaudiya Grantha Mandira); the four discrepancies are adjudicated in the notes (1.8, 1.22, 1.44; 1.5 and 1.15 differ only in anusvāra vs. class nasal). Collation against a pre-1930 printed edition is still to be done and is noted as pending. Transliteration: IAST. The reading under each word gives the words with sandhi undone and compound members hyphenated, in the manner of the traditional pada-pāṭha. Pronunciation convention: classical Sanskrit as described in Whitney's Sanskrit Grammar (1889), the standard recitation pronunciation; no audio yet. Translations made fresh from the Sanskrit with Monier-Williams (1899) and Apte (1890); no modern translation consulted.",
    'about': "The Bhagavadgītā, 'the Song of the Lord', is a dialogue of seven hundred verses set into the Mahābhārata at the moment before the great battle of Kurukṣetra. Chapter 1 is the frame: the blind king Dhṛtarāṣṭra asks his minister Sañjaya what is happening on the field; Sañjaya reports Duryodhana's nervous survey of the two armies, the blowing of the war-conches, and Arjuna's request to be driven between the lines to see whom he must fight. Seeing teachers, uncles, cousins and friends on both sides, Arjuna is overcome, lays down his bow and refuses to fight. His despair is the question the rest of the poem answers. The chapter is nearly all names and kinship terms; its value for the reader is that it teaches the two things every Sanskrit page needs first — how words fuse at their edges (sandhi) and how compounds are read backwards from their last member — on the simplest possible content.",
    'sentences': sentences,
    'glossary': glossary,
}
json.dump(story, open(D + 'gita-ch01.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(sentences), 'words', sum(len(s['words']) for s in sentences), 'glossary', len(glossary))

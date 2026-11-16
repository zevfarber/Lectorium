import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from units import U
from glossary import G
from tib import word, PUNCT
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sents = []; used = {}; nwords = 0
for u in U:
    words = []; t = ''; br = False; lead = ''
    for tok in u['w'].split():
        if tok == '/': br = True; t = t.rstrip(' ') + '\n'; continue
        if all(c in PUNCT for c in tok): lead = tok + ' '; t += tok + ' '; continue
        key, glyphs, reading, say = word(tok)
        assert key in G, ('no glossary entry', key, reading)
        used[key] = reading
        if lead: glyphs.insert(0, {'s': lead.strip(), 'tr': ' ', 'role': 'punct'}); lead = ''
        w = {'reading': reading, 'say': say, 'glyphs': glyphs,
             'morph': [{'lemma': reading, 'gloss': G[key], 'g': [i for i, g in enumerate(glyphs) if g.get('role') != 'punct']}]}
        if br: w['br'] = True; br = False
        words.append(w); nwords += 1
        t += tok + (' ' if tok[-1] in PUNCT else '')
    d = {'t': t.strip(), 'words': words, 'l': u['l']}
    for k in ('i', 'n'):
        if u.get(k): d[k] = u[k]
    if u.get('p'): d['p'] = True
    if u.get('v'):
        d['v'] = True
        assert d['t'].count('\n') == u['l'].count('\n'), ('verse lines', d['t'])
    assert ''.join(g['s'] for w in words for g in w['glyphs']) == d['t'].replace(' ', '').replace('\n', ''), d['t']
    sents.append(d)
# the units must reproduce the archived reading of the print, letter for letter
src = '\n'.join(l for l in open(os.path.join(HERE, 'source', 'w23710-pp09-17.txt'), encoding='utf-8').read().split('\n')
                if not l.startswith('#') and not l.startswith('{'))
for x, y in (('༄༅༔ ༔', ''), ('[?]', ''), ('\n', ''), (' ', ''), ('པའཾ', 'པའམ'), ('ལཾ་', 'ལམ་'),
             ('དུས་ཅན', 'ལུས་ཅན'), ('འབྲིང་རྣམསབར', 'འབྲིང་རྣམས་བར')): src = src.replace(x, y)
mine = ''.join(d['t'] for d in sents).replace(' ', '').replace('\n', '')
assert src.startswith(mine), 'units differ from the archived source'
extra = [k for k in G if k not in used]
assert not extra, extra
gloss = {k: used[k] + ' — ' + G[k] for k in sorted(used)}
story = {
 'id': 'bardo-thodol-001',
 'title': 'བར་དོ་ཐོས་གྲོལ་ཆེན་མོ།',
 'titleRead': 'Bardo Thödröl Chenmo',
 'titleEn': 'The Tibetan Book of the Dead — The Opening: How the Book Is to Be Read',
 'work': 'བར་དོ་ཐོས་གྲོལ།', 'workEn': 'The Tibetan Book of the Dead (Bardo Thödröl)',
 'part': '1 · The opening: for whom, when and how the book is read',
 'language': 'Classical Tibetan', 'langCode': None, 'script': 'tibetan',
 'provisional': True,
 'draftNote': 'Read from one blockprint at the resolution of an online scan; three doubtful places are marked in the notes, and the text has not yet been collated with other prints.',
 'source': open(os.path.join(HERE, 'source.txt'), encoding='utf-8').read().strip(),
 'about': open(os.path.join(HERE, 'about.txt'), encoding='utf-8').read().strip(),
 'sentences': sents, 'glossary': gloss}
json.dump(story, open(os.path.join(ROOT, 'bardo-thodol-001.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# library entry
sp = os.path.join(ROOT, 'stories.json'); lib = json.load(open(sp, encoding='utf-8'))
entry = {k: story[k] for k in ('id', 'title', 'titleEn', 'language', 'work', 'workEn', 'part')}
entry['file'] = 'bardo-thodol-001.json'; entry['seq'] = 1
lib['stories'] = [x for x in lib['stories'] if x['id'] != entry['id']] + [entry]
raw = open(sp, encoding='utf-8').read()
json.dump(lib, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, **({'indent': 1} if raw.startswith('{\n') else {}))
print(len(sents), 'units,', nwords, 'words,', len(gloss), 'glossary forms; every word has an entry')

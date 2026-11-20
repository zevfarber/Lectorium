#!/usr/bin/env python3
"""Build upanishad-<part>.json from the drafter's files for one part.

    python3 build_up.py <part>            e.g. katha-1  → writes ../../../upanishad-katha-1.json
    python3 build_up.py <part> --out PATH

Inputs, in drafts/<part>/ (the Bhagavadgītā's formats, keyed by UNIT ORDER, not by verse number):
  words.txt   one block per unit: "#<k>" (k = 1, 2, … the unit's place in the part, numbered or not), then
              one line per Devanagari WORD token (daṇḍa tokens are never listed)
              "<token>|<sandhi-split IAST reading>|<lemma — gloss>;;<lemma — gloss>…",
              with a line "--" between the unit's source lines.
  trans.txt   one block per unit: "#<k>" then "L: literal", "I: idiomatic", "N: note"
              (I may be omitted when it would equal L; N is optional).
  about.txt   one paragraph for the "Background information" box.
The tokens must tile the source (up_lib.read_part) exactly; the script refuses to build otherwise."""
import json, os, re, sys
import up_lib as U

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


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
        if line[:2] in ('L:', 'I:', 'N:') and cur is not None:
            trans[cur][line[0].lower()] = line[2:].strip()
    return trans


def build(pid, out=None):
    P = U.part(pid)
    d = os.path.join(HERE, 'drafts', pid)
    words = parse_words(os.path.join(d, 'words.txt'))
    trans = parse_trans(os.path.join(d, 'trans.txt'))
    units = U.read_part(pid)
    n = len(units)
    errors = 0
    if sorted(words) != list(range(1, n + 1)):
        sys.exit(f'build refused: words.txt covers units {sorted(words)[:3]}…, expected 1..{n}')
    if sorted(trans) != list(range(1, n + 1)):
        sys.exit(f'build refused: trans.txt covers units {sorted(trans)[:3]}…, expected 1..{n}')
    for k, u in enumerate(units, 1):
        want = U.words_of(u)
        if len(words[k]) != len(want):
            errors += 1; print('LINE COUNT unit', k, len(words[k]), 'blocks vs', len(want), 'source lines'); continue
        for li, w in enumerate(want):
            got = [x['dev'] for x in words[k][li]]
            if got != w:
                errors += 1; print('MISMATCH unit', k, 'line', li + 1, '\n  src:', ' '.join(w), '\n  got:', ' '.join(got))
        if not trans[k].get('l'):
            errors += 1; print('NO LITERAL unit', k)
    if errors:
        sys.exit('build refused: %d problem(s)' % errors)

    corr = {c['unit']: c for c in P.get('notesRequired', [])}
    sentences, glossary = [], {}
    for k, u in enumerate(units, 1):
        wl, tr_lines = [], []
        for li, line in enumerate(u['lines']):
            toks = U.line_tokens(line)
            dw = iter(words[k][li])
            lead = None
            line_words = []
            for t, is_p in toks:
                if is_p:
                    if line_words:
                        line_words[-1]['glyphs'].append({'s': t, 'tr': ' ', 'role': 'punct'})
                    else:
                        lead = t
                    continue
                w = next(dw)
                glyphs = [{'s': w['dev'], 'tr': w['reading']}]
                if lead:
                    glyphs.insert(0, {'s': lead, 'tr': ' ', 'role': 'punct'}); lead = None
                e = {'reading': w['reading'], 'glyphs': glyphs,
                     'morph': [{'lemma': m['lemma'], 'gloss': m['gloss'], 'g': [len(glyphs) - 1]} for m in w['morph']]}
                if li > 0 and not line_words:
                    e['br'] = True
                line_words.append(e)
                glossary.setdefault(w['dev'], w['reading'] + ' — ' + '; '.join(m['lemma'] + ' — ' + m['gloss'] for m in w['morph']))
            wl.extend(line_words)
            tr_lines.append(' '.join(x['reading'] for x in line_words))
        s = {'v': True, 't': '\n'.join(u['lines']), 'tr': '\n'.join(tr_lines), 'words': wl, 'l': trans[k]['l']}
        if u['n'] is not None:
            s['ln'] = u['n']
        else:
            s['p'] = True
        if trans[k].get('i'):
            s['i'] = trans[k]['i']
        note = trans[k].get('n', '')
        if k in corr and corr[k]['mustMention'] not in note:
            sys.exit(f'build refused: the note to unit {k} must mention {corr[k]["mustMention"]!r} ({corr[k]["why"]})')
        if note:
            s['n'] = note
        sentences.append(s)

    W = U.parts()
    story = {
        'id': P['id'], 'title': P['title'], 'titleRead': P['titleTr'],
        'titleEn': 'The Upanishads — ' + P['titleEn'],
        'work': 'उपनिषदः', 'workEn': 'The Upanishads',
        'part': P['label'],
        'language': 'Sanskrit', 'langCode': None, 'script': 'devanagari', 'numbering': 'stanza',
        'source': W['sourceStatement'].replace('{page}', P['wikisource']).replace('{witness}', P.get('witnessStatement', W['noWitness'])),
        'sentences': sentences, 'glossary': glossary,
    }
    about = os.path.join(d, 'about.txt')
    if os.path.exists(about):
        story['about'] = open(about, encoding='utf-8').read().strip()
    out = out or os.path.join(ROOT, P['file'])
    json.dump(story, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', out, '| units', len(sentences), '| words', sum(len(s['words']) for s in sentences), '| glossary', len(glossary))
    return out


if __name__ == '__main__':
    pid = sys.argv[1]
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    build(pid, out)

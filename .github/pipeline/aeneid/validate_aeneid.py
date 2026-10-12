#!/usr/bin/env python3
"""Gate for a built Aeneid part.   usage: python3 validate_aeneid.py aeneid-NNN     Must print PASS before anything is pushed.
Coverage is checked twice: with wordre.py (the Python copy of the reader's splitter) and, when node is available, by running
the WORD_CLASS / WORD_RE / wordKey lines taken out of reader.html itself, as the Ovid tooling did."""
import sys, os, re, json, subprocess, shutil
import aeneid_lib as A
pid = sys.argv[1]; P = A.part(pid); L = A.lines_of(P); F = []; W = []
def fail(*a): F.append(' '.join(str(x) for x in a))
def warn(*a): W.append(' '.join(str(x) for x in a))
try:
    S = A.jload(os.path.join(A.ROOT, P['file'])); G = A.glossary()['glossary']; M = A.jload(os.path.join(A.ROOT, 'stories.json'))['stories']
except Exception as e:
    print('FAIL: a file does not parse:', e); sys.exit(1)
U = S['sentences']
# 1 the text is the edition's, character for character
src = '\n'.join(l['t'] for l in L); got = ''
for u in U:
    got += u['t']
    if len(got) < len(src): got += src[len(got)] if src[len(got)] in ' \n' else '\x00'
if got != src: fail('concat: the units do not reproduce the edition')
if [w for u in U for w in A.WORD_RE.findall(u['t'])] != A.WORD_RE.findall(src): fail('tokens: unit tokens differ from the edition')
if A.sha(L) != P['sha256']: fail('source sha differs from parts.json')
if re.search(r'[āēīōūȳĀĒĪŌŪ]', ''.join(u['t'] for u in U)): fail('macron in t (the edition prints none)')
# 2 every word has a glossary entry (Python copy of the reader's splitter), and every entry is well formed
miss = sorted({f for u in U for f in A.forms(u['t'])} - set(G))
if miss: fail('coverage:', len(miss), 'forms without an entry:', miss[:20])
for f, e in G.items():
    if not re.match(r'^\S.* — \S', e) or '`' in e: fail('glossary shape:', f, '=>', e[:60])
# 2b the reader's own regex, run in node from reader.html
node = shutil.which('node')
if node:
    html = open(os.path.join(A.ROOT, 'reader.html'), encoding='utf8').read()
    grab = lambda pat: re.search(pat, html, re.M).group(0)
    wc = re.search(r"^const WORD_CLASS = .*?;[ \t]*$", html, re.M | re.S).group(0)
    wc = re.sub(r"/\*.*?\*/", "", wc, flags=re.S)          # the statement spans comment lines
    js = '\n'.join([wc, grab(r"^const HAN_CLASS = .*$"), grab(r"^const WORD_RE = .*$"), grab(r"^function wordKey\(w\).*$")])
    js += '''
const fs=require('fs'); const s=JSON.parse(fs.readFileSync(process.argv[2],'utf8')); const g=JSON.parse(fs.readFileSync(process.argv[3],'utf8')).glossary;
const miss=new Set(); let n=0; for(const u of s.sentences){ for(const m of u.t.matchAll(WORD_RE)){ n++; const k=wordKey(m[0]); if(g[k]===undefined) miss.add(k);} }
console.log(JSON.stringify({tokens:n, missing:[...miss]}));'''
    tmp = os.path.join(A.HERE, 'drafts', pid, '_reader_regex.js'); open(tmp, 'w').write(js)
    try:
        r = json.loads(subprocess.run([node, tmp, os.path.join(A.ROOT, P['file']), A.glossary_path()], capture_output=True, text=True, check=True).stdout)
        if r['missing']: fail('reader regex coverage:', len(r['missing']), 'missing', r['missing'][:20])
        else: print(f"reader.html WORD_RE (node): {r['tokens']} tokens, 0 missing")
    except Exception as e: fail('could not run the reader regex in node:', e)
    finally: os.remove(tmp)
else: warn('node not found: reader-regex coverage not run (wordre.py coverage passed)' if not miss else 'node not found')
# 3 layers
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
for k, u in enumerate(U):
    w = f'unit {k} (line {u.get("ln")}):'
    for f in ('l', 'i', 'n', 'sc'):
        if not u.get(f): fail(w, 'missing', f)
    if u.get('l', '').count('\n') != u['t'].count('\n'): fail(w, 'l line count')
    if [strip(x) for x in u.get('sc', [])] != A.WORD_RE.findall(u['t']): fail(w, 'sc does not line up with the words')
    n = len(u.get('n', '').split())
    if n < 15 or n > 140: warn(w, f'note is {n} words')
    if re.search(r'\b(Fitzgerald|Mandelbaum|Fagles|Ruden|Bartsch|Dryden|Lombardo|Ahl|Humphries|Day Lewis|Ferry|Lattimore)\b', u.get('n', '') + u.get('i', '') + u.get('l', '')): fail(w, 'names a modern translator')
# 4 scansion: every line six feet, 12–17 syllables, one line-end mark
alltok = [x for u in U for x in u.get('sc', [])]
if len(alltok) == len(A.WORD_RE.findall(src)):
    i = 0
    for l in L:
        n = len(A.WORD_RE.findall(l['t'])); seg = ''.join(alltok[i:i + n]); i += n
        feet = re.findall(r'[1-6]', seg); syl = len(re.findall(r'[–⏑×]', seg))
        if feet != list('123456') or not 12 <= syl <= 17 or seg.count('×') != 1: fail(f'line {l["n"]}: scansion is not a hexameter ({"".join(feet)}, {syl} syllables)')
        # each foot: dactyl –⏑⏑ or spondee –– (sixth: –×)
        body = re.sub(r'[^0-9–⏑×]', '', seg); feetpat = re.findall(r'\d([–⏑×]+)', body)
        if any(fp not in ('–⏑⏑', '––') for fp in feetpat[:5]) or feetpat[5] not in ('–×', '⏑×'): fail(f'line {l["n"]}: bad foot pattern {feetpat}')
# 5 speech marks
for layer in ('t', 'l', 'i'):
    o = sum(u[layer].count('“') for u in U); c = sum(u[layer].count('”') for u in U)
    if o != c: warn(f'{layer}: {o} opening and {c} closing quotation marks')
# 6 manifest
E = [e for e in M if e.get('work') == 'Aeneid']
if [e['seq'] for e in E] != sorted({e['seq'] for e in E}): fail('manifest: Aeneid seq not unique and ascending')
me = [e for e in E if e['id'] == pid]
if len(me) != 1 or me[0]['file'] != P['file'] or me[0]['seq'] != P['seq'] or me[0]['part'] != S['part'] or me[0]['titleEn'] != S['titleEn'] or me[0]['language'] != 'Latin': fail('manifest entry missing or disagrees with the story')
for k in ('source', 'about', 'glossaryFile'):
    if not S.get(k): fail('story missing', k)
if S.get('langCode') is not None: fail('langCode must be null for Latin (audio is the prepared pinned reading)')
for w in W: print('WARN', w)
for f in F: print('FAIL', f)
print('PASS' if not F else f'{len(F)} failure(s)', f'— {pid}: {len(U)} units, {len(L)} lines, glossary {len(G)}')
sys.exit(1 if F else 0)

#!/usr/bin/env python3
"""Gate for a built Meditations part.   usage: python3 validate_meditations.py meditations-NNN   Must print PASS before anything is pushed."""
import sys,os,re
import med_lib as O
from translit_grc import translit
pid=sys.argv[1]; P=O.part(pid); C=O.chapters_of(P); F=[];W=[]
def fail(*a): F.append(' '.join(str(x) for x in a))
def warn(*a): W.append(' '.join(str(x) for x in a))
try:
    S=O.jload(os.path.join(O.ROOT,P['file'])); G=O.glossary()['glossary']; M=O.jload(os.path.join(O.ROOT,'stories.json'))['stories']
except Exception as e:
    print('FAIL: a file does not parse:',e); sys.exit(1)
U=S['sentences']
if O.sha(C)!=P['sha256']: fail('source sha differs from parts.json')
# 1 the text is the edition's, character for character: blocks tiled in order
src=[bl['t'] for ch in C for bl in ch['blocks']]; k=0
for T in src:
    got=''
    while len(got)<len(T) and k<len(U):
        got+=U[k]['t']; k+=1
        if len(got)<len(T): got+=T[len(got)] if T[len(got)] in ' \n' else '\x00'
    if got!=T: fail('concat: the units do not reproduce the block beginning',repr(T[:50])); break
if k!=len(U): fail('concat: units left over')
if any(c in u['t'] for u in U for c in "᾽᾿'`ʼʽ"): fail('koronis / ASCII apostrophe / modifier letter in t')
# 2 every word has a glossary entry, and every entry is well formed
miss=sorted({f for u in U for f in O.forms(u['t'])}-set(G))
if miss: fail('coverage:',len(miss),'forms without an entry:',miss[:20])
for f,e in G.items():
    if not re.match(r'^\S.* — \S',e) or '`' in e or "'" in e: fail('glossary shape:',f,'=>',e[:60])
# 3 layers
chap_starts=[f'{ch["b"]}.{ch["c"]}' for ch in C]
if [u['ln'] for u in U if u.get('ln')]!=chap_starts: fail('ln: chapter numbers missing or out of order')
for k,u in enumerate(U):
    w=f'unit {k} ({u.get("ln") or "…"}):'
    for f in ('l','i','n','tr'):
        if not u.get(f): fail(w,'missing',f)
    if u.get('tr')!=translit(u['t']): fail(w,'tr is not the program\'s romanization')
    if u.get('l','').count('\n')!=u['t'].count('\n'): fail(w,'l line count')
    if u.get('ln') and not u.get('p'): fail(w,'a chapter\'s first unit must start a paragraph')
    n=len(u.get('n','').split())
    if n<12 or n>130: warn(w,f'note is {n} words (band 15–110)')
    if re.search(r'\b(Hays|Hammond|Waterfield|Staniforth|Farquharson|Hicks|Robin Hard|Gregory Hays|Casaubon|Haines|George Long)\b',u.get('n','')+u.get('i','')+u.get('l','')): fail(w,'names a translator')
    if '`' in u.get('n',''): fail(w,'backtick in note')
for layer in ('l','i'):
    for a,b in (('“','”'),('‘','’')):
        o=sum(u[layer].count(a) for u in U); c=sum(u[layer].count(b) for u in U)
        if a=='“' and o!=c: warn(f'{layer}: {o} opening and {c} closing double quotation marks')
# 4 a unit whose Greek repeats an earlier published unit must repeat its English
seen={}
for st in O.published_stories():
    for u in st['sentences']:
        key=O.letters_only(u['t'])
        if len(key.split())<3: continue
        if st['id']==pid and key in seen and not seen[key][0].startswith(pid) and (seen[key][1]!=u['l'] or seen[key][2]!=u['i']):
            fail(f'{u.get("ln") or "unit"}: same Greek as {seen[key][0]} but different English. Use exactly: l={seen[key][1]!r} i={seen[key][2]!r}')
        if key not in seen: seen[key]=(st['id'],u['l'],u['i'])
# 5 manifest and story
E=[e for e in M if str(e.get('id','')).startswith('meditations-')]
if [e['seq'] for e in E]!=sorted({e['seq'] for e in E}): fail('manifest: meditations seq not unique and ascending')
me=[e for e in E if e['id']==pid]
if len(me)!=1 or me[0]['file']!=P['file'] or me[0]['seq']!=P['seq'] or me[0]['group']!=O.GROUP(P['book']) or me[0]['part']!=S['part'] or me[0]['titleEn']!=S['titleEn']: fail('manifest entry missing or disagrees with the story')
for k in ('source','about','glossaryFile','trStyle','script','numbering'):
    if not S.get(k): fail('story missing',k)
for w in W: print('WARN',w)
for f in F: print('FAIL',f)
print('PASS' if not F else f'{len(F)} failure(s)',f'— {pid}: {len(U)} units, {P["chapters"]} chapters, glossary {len(G)}')
sys.exit(1 if F else 0)

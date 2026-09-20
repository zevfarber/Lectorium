#!/usr/bin/env python3
"""Gate for a built Odyssey part.   usage: python3 validate_odyssey.py odyssey-NNN     Must print PASS before anything is pushed."""
import sys,os,re,json
import odyssey_lib as O
from translit_grc import translit
pid=sys.argv[1]; P=O.part(pid); L=O.lines_of(P); F=[];W=[]
def fail(*a): F.append(' '.join(str(x) for x in a))
def warn(*a): W.append(' '.join(str(x) for x in a))
try:
    S=O.jload(os.path.join(O.ROOT,P['file'])); G=O.glossary()['glossary']; M=O.jload(os.path.join(O.ROOT,'stories.json'))['stories']
except Exception as e:
    print('FAIL: a file does not parse:',e); sys.exit(1)
U=S['sentences']
# 1 the text is the edition's, character for character
src='\n'.join(l['t'] for l in L); got='';
for k,u in enumerate(U):
    got+=u['t']
    if len(got)<len(src): got+=src[len(got)] if src[len(got)] in ' \n' else '\x00'
if got!=src: fail('concat: the units do not reproduce the edition')
if O.sha(L)!=P['sha256']: fail('source sha differs from parts.json')
if any(c in u['t'] for u in U for c in "᾽᾿'`"): fail('koronis / ASCII apostrophe in t')
# 2 every word has a glossary entry, and every entry is well formed
miss=sorted({f for u in U for f in O.forms(u['t'])}-set(G))
if miss: fail('coverage:',len(miss),'forms without an entry:',miss[:20])
for f,e in G.items():
    if not re.match(r'^\S.* — \S',e) or '`' in e or "'" in e: fail('glossary shape:',f,'=>',e[:60])
# 3 layers
strip=lambda s: re.sub(r'[0-9–⏑×‖]','',s)
for k,u in enumerate(U):
    w=f'unit {k} (line {u.get("ln")}):'
    for f in ('l','i','n','tr','sc'):
        if not u.get(f): fail(w,'missing',f)
    if u.get('tr')!=translit(u['t']): fail(w,'tr is not the program\'s romanization')
    if u.get('l','').count('\n')!=u['t'].count('\n'): fail(w,'l line count')
    toks=O.WORD.findall(u['t'])
    if [strip(x) for x in u.get('sc',[])]!=toks: fail(w,'sc does not line up with the words')
    n=len(u.get('n','').split())
    if n<20 or n>130: warn(w,f'note is {n} words (band 25–110)')
    if re.search(r'\b(Lattimore|Fagles|Fitzgerald|Wilson|Lombardo|Rieu|Mendelsohn)\b',u.get('n','')+u.get('i','')): fail(w,'names a modern translator')
    if '`' in u.get('n',''): fail(w,'backtick in note')
# 4 scansion: every line is six feet, 12–17 syllables
alltok=[x for u in U for x in u.get('sc',[])]; words=[w for l in L for w in O.WORD.findall(l['t'])]
if len(alltok)==len(words):
    i=0
    for l in L:
        n=len(O.WORD.findall(l['t'])); seg=''.join(alltok[i:i+n]); i+=n
        feet=re.findall(r'[1-6]',seg); syl=len(re.findall(r'[–⏑×]',seg))
        if feet!=list('123456') or not 12<=syl<=17 or seg.count('×')!=1: fail(f'line {l["n"]}: scansion is not a hexameter ({"".join(feet)}, {syl} syllables)')
        if seg.count('‖')!=1: warn(f'line {l["n"]}: {seg.count(chr(0x2016))} caesura marks')
# 5 speech marks
for layer in ('l','i'):
    o=sum(u[layer].count('“') for u in U); c=sum(u[layer].count('”') for u in U)
    if o!=c: warn(f'{layer}: {o} opening and {c} closing quotation marks in the part (a speech may run on into the next part — say so in LOG.md if it does)')
# 6 a unit whose Greek repeats an earlier published unit must repeat its English
seen={}
for st in O.published_stories():
    for u in st['sentences']:
        key=O.letters_only(u['t'])
        if st['id']==pid:
            if key in seen and (seen[key][1]!=u['l'] or seen[key][2]!=u['i']):
                fail(f'line {u["ln"]}: same Greek as {seen[key][0]} but different English. Use exactly: l={seen[key][1]!r} i={seen[key][2]!r}')
        if key not in seen: seen[key]=(f'{st["id"]} line {u["ln"]}',u['l'],u['i'])
# 7 manifest
E=[e for e in M if e.get('work')==S['work']]
if [e['seq'] for e in E]!=sorted({e['seq'] for e in E}): fail('manifest: Odyssey seq not unique and ascending')
me=[e for e in E if e['id']==pid]
if len(me)!=1 or me[0]['file']!=P['file'] or me[0]['seq']!=P['seq'] or me[0]['group']!=f'Book {P["book"]}' or me[0]['part']!=S['part'] or me[0]['titleEn']!=S['titleEn']: fail('manifest entry missing or disagrees with the story')
for k in ('source','about','glossaryFile','trStyle','script'):
    if not S.get(k): fail('story missing',k)
for w in W: print('WARN',w)
for f in F: print('FAIL',f)
print('PASS' if not F else f'{len(F)} failure(s)',f'— {pid}: {len(U)} units, {len(L)} lines, glossary {len(G)}')
sys.exit(1 if F else 0)

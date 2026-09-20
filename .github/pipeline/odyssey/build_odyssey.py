#!/usr/bin/env python3
"""Assemble one Odyssey part from its draft.   usage: python3 build_odyssey.py odyssey-NNN

Reads   drafts/odyssey-NNN/units.json   {title, titleEn, part, about, sentences:[{t,l,i,n,ln,v,p?,mark?}]}
        drafts/odyssey-NNN/gloss.json   {form: "lemma — meaning; parse"} for every form not yet in odyssey-glossary.json
                                        optional key "__broaden__": {form: new entry} — new entry must CONTAIN the old one
Writes  <repo root>/odyssey-NNN.json, <repo root>/odyssey-glossary.json (new keys appended, sorted), and adds the
        manifest entry to <repo root>/stories.json after the previous part. Refuses, changing nothing, on any failure.
tr (romanization) and sc (scansion) are made here by program; a drafter never writes them."""
import sys,os,re,json
import odyssey_lib as O
from translit_grc import translit
from scan_hexameter import scan_line
pid=sys.argv[1]; P=O.part(pid); L=O.lines_of(P)
def die(*a): print('BUILD REFUSED:',*a); sys.exit(1)
if O.sha(L)!=P['sha256']: die('source text does not match parts.json sha256')
D=O.jload(os.path.join(O.HERE,'drafts',pid,'units.json'))
for k in ('title','titleEn','part','about'):
    if not D.get(k): die('units.json missing',k)
if P['cite'] not in D['part'] or P['cite'] not in D['titleEn']: die('part/titleEn must carry the citation',P['cite'])
# ---- tiling: the units' t, joined in order, must reproduce the edition character for character
S='\n'.join(l['t'] for l in L); nums=[l['n'] for l in L]; paras={l['n'] for l in L if l['p']}|{L[0]['n']}
pos=0;li=0;atStart=True;errs=[]
for k,u in enumerate(D['sentences']):
    t=u.get('t','')
    if not t or not S.startswith(t,pos): die(f'unit {k}: t does not match the edition at line {nums[li]}: expected {S[pos:pos+50]!r}')
    if u.get('ln')!=nums[li]: errs.append(f'unit {k}: ln={u.get("ln")} but it starts on line {nums[li]}')
    if bool(u.get('p'))!=(atStart and nums[li] in paras): errs.append(f'unit {k} (line {nums[li]}): p should be {atStart and nums[li] in paras}')
    if not u.get('v'): errs.append(f'unit {k}: v must be true')
    for f in ('l','i','n'):
        if not (u.get(f) or '').strip(): errs.append(f'unit {k} (line {nums[li]}): missing {f}')
    if (u.get('l') or '').count('\n')!=t.count('\n'): errs.append(f'unit {k} (line {nums[li]}): l must have the same number of lines as t')
    if '\n' in (u.get('i') or ''): errs.append(f'unit {k}: i must not contain line breaks')
    if t.count('\n')+1>5: errs.append(f'unit {k} (line {nums[li]}): spans more than five lines')
    if t[-1] not in O.TERMINAL+',': errs.append(f'unit {k} (line {nums[li]}): does not end at punctuation')
    pos+=len(t); li+=t.count('\n')
    if pos<len(S):
        if S[pos] not in ' \n': die(f'unit {k}: ends mid-word at line {nums[li]}')
        atStart=S[pos]=='\n'; li+=1 if atStart else 0; pos+=1
if pos!=len(S): die(f'edition not fully covered: stopped at line {nums[li]}')
if errs: die('\n  '+'\n  '.join(errs))
# ---- scansion and romanization
scans=[scan_line(l['t'],l['n']) for l in L]
nofit=[s['n'] for s in scans if not s['pattern']]
if nofit: die('lines that do not scan at all (report in QUESTIONS.md, do not publish):',nofit)
stream=[t for s in scans for t in s['tokens']]; strip=lambda s: re.sub(r'[0-9–⏑×‖]','',s)
i=0;units=[]
for u in D['sentences']:
    toks=O.WORD.findall(u['t']); sc=stream[i:i+len(toks)]; i+=len(toks)
    if [strip(x) for x in sc]!=toks: die('scansion tokens do not line up with the text at line',u['ln'])
    nu={'t':u['t'],'tr':translit(u['t']),'l':u['l'],'i':u['i'],'n':u['n']}
    if u.get('mark'): nu['mark']=u['mark']
    if u.get('p'): nu['p']=True
    nu['v']=True; nu['ln']=u['ln']; nu['sc']=sc; units.append(nu)
# ---- glossary: additions only; an existing entry may be broadened, never replaced
G=O.glossary(); g=G['glossary']
add=O.jload(os.path.join(O.HERE,'drafts',pid,'gloss.json')); broaden=add.pop('__broaden__',{})
need={f for u in units for f in O.forms(u['t'])}
for f,e in add.items():
    if f in g: die('gloss.json redefines an existing form (use __broaden__):',f)
    if f not in need: die('gloss.json has a form that is not in this part:',f)
    if not re.match(r'^\S.* — \S',e) or '`' in e or "'" in e or len(e)>230: die('bad glossary entry shape:',f,'=>',e)
for f,e in broaden.items():
    if f not in g or g[f] not in e: die('__broaden__ must keep the old entry whole inside the new one:',f)
missing=sorted(need-set(g)-set(add))
if missing: die(f'{len(missing)} forms have no glossary entry:',missing[:25])
for f in sorted(add): g[f]=add[f]
for f,e in broaden.items(): g[f]=e
# ---- story, manifest
first=O.published_stories()[0]
story={'id':pid,'sourceId':pid,'title':D['title'],'titleEn':D['titleEn'],'work':first['work'],'workEn':first['workEn'],'part':D['part'],
 'language':'Ancient Greek','langCode':None,'source':first['source'],'about':D['about'],'trStyle':'line','script':'greek',
 'glossaryFile':'odyssey-glossary.json','sentences':units}
M=O.jload(os.path.join(O.ROOT,'stories.json')); st=M['stories']
st[:]=[e for e in st if e.get('id')!=pid]
prev=max([k for k,e in enumerate(st) if e.get('work')==first['work'] and e.get('seq',0)<P['seq']],default=len(st)-1)
st.insert(prev+1,{'id':pid,'title':D['title'],'titleEn':D['titleEn'],'language':'Ancient Greek','work':first['work'],'workEn':first['workEn'],
 'part':D['part'],'group':f'Book {P["book"]}','file':P['file'],'seq':P['seq']})
O.jdump(story,os.path.join(O.ROOT,P['file'])); O.jdump(G,O.glossary_path()); O.jdump(M,os.path.join(O.ROOT,'stories.json'))
flag=[(s['n'],s['flags']) for s in scans if any('UNRESOLVED' in f or 'AMBIGUOUS' in f for f in s['flags'])]
print(f'BUILT {pid}: {len(units)} units, {len(L)} lines, {len(add)} new glossary forms ({len(g)} total), {len(broaden)} broadened')
print('scansion lines needing a person or the reviewer:',flag if flag else 'none')

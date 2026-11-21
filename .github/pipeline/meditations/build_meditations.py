#!/usr/bin/env python3
"""Assemble one Meditations part from its draft.   usage: python3 build_meditations.py meditations-NNN
(adapted from ../hesiod/build_hesiod.py, 2026-11-21: prose, so no scansion)

Reads   drafts/meditations-NNN/units.json   {title, titleEn, part, about, sentences:[{t, l, i, n}]}
        drafts/meditations-NNN/gloss.json   {form: "lemma — meaning; parse"} for every form not yet in meditations-glossary.json
                                             optional key "__broaden__": {form: new entry} — new entry must CONTAIN the old one
Writes  <repo root>/meditations-NNN.json, <repo root>/meditations-glossary.json (new keys added, sorted), and the manifest
        entry in <repo root>/stories.json after the previous part. Refuses, changing nothing, on any failure.
The build, never the drafter, sets tr (romanization), ln (book.chapter, on a chapter's first unit), p (a chapter's first
unit, and a book's closing subscription) and v (units inside a verse quotation)."""
import sys,os,re
import med_lib as O
from translit_grc import translit
pid=sys.argv[1]; P=O.part(pid); C=O.chapters_of(P)
def die(*a): print('BUILD REFUSED:',*a); sys.exit(1)
if O.sha(C)!=P['sha256']: die('source text does not match parts.json sha256')
D=O.jload(os.path.join(O.HERE,'drafts',pid,'units.json'))
for k in ('title','titleEn','part','about'):
    if not D.get(k): die('units.json missing',k)
if P['cite'] not in D['part'] or P['cite'] not in D['titleEn']: die('part/titleEn must carry the citation',P['cite'])
for k,u in enumerate(D['sentences']):
    extra=set(u)-{'t','l','i','n','mark'}
    if extra: die(f'unit {k}: fields the build sets or does not know: {sorted(extra)}')
# ---- tiling: units fill each block in order, never crossing a block, reproducing it character for character
blocks=[(ch,bi,bl) for ch in C for bi,bl in enumerate(ch['blocks'])]
U=D['sentences']; k=0; units=[]; errs=[]
for ch,bi,bl in blocks:
    T=bl['t']; pos=0; first=True
    while pos<len(T):
        if k>=len(U): die(f'ran out of units in {ch["b"]}.{ch["c"]} at {T[pos:pos+50]!r}')
        u=U[k]; t=u.get('t','')
        if not t or not T.startswith(t,pos): die(f'unit {k}: t does not match the edition in {ch["b"]}.{ch["c"]}: expected {T[pos:pos+60]!r}, got {t[:60]!r}')
        pos+=len(t)
        if pos<len(T):
            if T[pos] not in ' \n': die(f'unit {k}: ends mid-word in {ch["b"]}.{ch["c"]}')
            pos+=1
            if t.rstrip(']⟩’)†')[-1:] not in O.TERMINAL+'—': errs.append(f'unit {k} ({ch["b"]}.{ch["c"]}): does not end at punctuation')
        w=f'unit {k} ({ch["b"]}.{ch["c"]})'
        for f in ('l','i','n'):
            if not (u.get(f) or '').strip(): errs.append(f'{w}: missing {f}')
        if (u.get('l') or '').count('\n')!=t.count('\n'): errs.append(f'{w}: l must have the same number of lines as t')
        if '\n' in (u.get('i') or ''): errs.append(f'{w}: i must not contain line breaks')
        if not bl.get('v') and '\n' in (u.get('l') or ''): errs.append(f'{w}: prose l must not contain line breaks')
        nw=len(O.WORD.findall(t))
        if nw>70: errs.append(f'{w}: {nw} Greek words — cut it at a stop or colon (70 at most)')
        nu={'t':t,'tr':translit(t),'l':u['l'],'i':u['i'],'n':u['n']}
        if u.get('mark'): nu['mark']=u['mark']
        if first and (bi==0 or bl.get('sub')): nu['p']=True
        if first and bi==0: nu['ln']=f'{ch["b"]}.{ch["c"]}'
        if bl.get('v'): nu['v']=True
        units.append(nu); k+=1; first=False
if k!=len(U): die(f'{len(U)-k} units left over after the last chapter')
if errs: die('\n  '+'\n  '.join(errs))
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
for f in add: g[f]=add[f]
for f,e in broaden.items(): g[f]=e
G['glossary']=dict(sorted(g.items()))
# ---- story, manifest
story={'id':pid,'sourceId':pid,'title':D['title'],'titleEn':D['titleEn'],'work':O.WORK[0],'workEn':O.WORK[1],'part':D['part'],
 'language':'Ancient Greek','langCode':None,'source':O.source_statement(P),'about':D['about'],'trStyle':'line','script':'greek',
 'numbering':'stanza','glossaryFile':'meditations-glossary.json','sentences':units}
M=O.jload(os.path.join(O.ROOT,'stories.json')); st=M['stories']
st[:]=[e for e in st if e.get('id')!=pid]
mine=[j for j,e in enumerate(st) if str(e.get('id','')).startswith('meditations-')]
prev=max([j for j in mine if st[j].get('seq',0)<P['seq']],default=(min(mine)-1 if mine else max([j for j,e in enumerate(st) if e.get('language')=='Ancient Greek'],default=len(st)-1)))
st.insert(prev+1,{'id':pid,'title':D['title'],'titleEn':D['titleEn'],'language':'Ancient Greek','work':O.WORK[0],'workEn':O.WORK[1],
 'part':D['part'],'group':O.GROUP(P['book']),'file':P['file'],'seq':P['seq']})
O.jdump(story,os.path.join(O.ROOT,P['file'])); O.jdump(G,O.glossary_path()); O.jdump(M,os.path.join(O.ROOT,'stories.json'))
print(f'BUILT {pid}: {len(units)} units, {P["chapters"]} chapters, {len(add)} new glossary forms ({len(g)} total), {len(broaden)} broadened')

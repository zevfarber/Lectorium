#!/usr/bin/env python3
"""Build source/iliad-monro-allen1920.json and parts.json from the Perseus TEI of Monro & Allen's Oxford Iliad.
usage: archive_iliad.py path/to/tlg0012.tlg001.perseus-grc2.xml
Run once (2026-10-12), modelled on ../odyssey/archive_odyssey.py. Kept so the archive can be re-derived and checked.
Lines the edition prints in square brackets (Perseus <del>) keep their brackets; nothing is dropped."""
import re,json,sys,hashlib,unicodedata,os
TARGET,MAXLEN,MINLEN=100,135,55
PIN={1:[100]}   # the pilot is 1.1-100; never re-cut it
x=open(sys.argv[1],encoding='utf8').read()
teisha=hashlib.sha256(x.encode('utf8')).hexdigest()
body=x[x.find('<body'):]
chunks=re.split(r'<div[^>]*subtype="[Bb]ook"[^>]*>',body)[1:]
assert len(chunks)==24
books=[];oddities=[]
for bi,ch in enumerate(chunks,1):
    lines=[];pending=False
    for m in re.finditer(r'<milestone[^>]*unit="[Pp]ara"[^>]*/>|<note\b.*?</note>|<l\b([^>]*)>(.*?)</l>',ch,flags=re.S):
        g=m.group(0)
        if g.startswith('<milestone'): pending=True; continue
        if g.startswith('<note'): oddities.append(f'{bi}: editorial note {re.sub("<[^>]+>","",g)!r} (after line {lines[-1]["n"] if lines else 0})'); continue
        attrs,raw=m.group(1),m.group(2)
        nm=re.search(r'n="([^"]+)"',attrs); n=nm.group(1) if nm else None
        para=pending or re.search(r'unit="[Pp]ara"',raw) is not None; pending=False
        raw=re.sub(r'<note\b.*?</note>','',raw,flags=re.S)
        bracket='<del>' in raw
        extra=set(re.findall(r'<(\w+)',raw))-{'milestone','del'}
        t=re.sub(r'<[^>]+>','',raw); t=re.sub(r'\s+',' ',t).strip()
        t=unicodedata.normalize('NFC',t.replace('ʼ','’').replace('᾽','’').replace("'",'’'))
        if bracket: t='['+t+']'; oddities.append(f'{bi}.{n}: printed in square brackets (athetized)')
        if not (n and n.isdigit()): oddities.append(f'{bi}: non-numeric line id {n!r}'); continue
        if extra: oddities.append(f'{bi}.{n}: inline tags {sorted(extra)}')
        lines.append({'n':int(n),'t':t,'p':bool(para) or not lines})
    for a,b in zip(lines,lines[1:]):
        if b['n']!=a['n']+1: oddities.append(f'{bi}: numbering jumps {a["n"]} -> {b["n"]}')
    books.append(lines)
os.makedirs('source',exist_ok=True)
src={'edition':'D. B. Monro and T. W. Allen, Homeri Opera, tomi I–II: Iliad, 3rd ed. (Oxford: Clarendon Press, 1920), Greek text','tei':'PerseusDL/canonical-greekLit tlg0012.tlg001.perseus-grc2.xml','teiSha256':teisha,
     'normalised':'elision mark -> U+2019; NFC; tags and editorial notes stripped; lines the edition brackets (TEI <del>) kept inside [ ]; nothing else','books':{str(i+1):b for i,b in enumerate(books)}}
json.dump(src,open('source/iliad-monro-allen1920.json','w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
parts=[];pid=0
for bi,lines in enumerate(books,1):
    first,last=lines[0]['n'],lines[-1]['n']
    starts=[l['n'] for l in lines if l['p']]
    ends=sorted({s-1 for s in starts if s>first}|{last})
    pins=[e for e in PIN.get(bi,[])]
    for e in pins: assert e in ends,(bi,e)
    INF=1e18;best={first-1:(0,None)}
    for e in ends:
        cand=(INF,None)
        for s in sorted(best):
            if s>=e: continue
            if any(s<p<e for p in pins): continue
            L=e-s
            if L>MAXLEN and any(s<q<e for q in ends): pen=(L-TARGET)**2*50
            else: pen=(L-TARGET)**2*(4 if L<MINLEN else 1)
            c=best[s][0]+pen
            if c<cand[0]: cand=(c,s)
        best[e]=cand
    cuts=[];e=last
    while e is not None and e>=first: cuts.append(e); e=best[e][1]
    cuts=sorted(c for c in cuts if c>=first)
    s=first
    for e in cuts:
        pid+=1; seg=[l for l in lines if s<=l['n']<=e]
        parts.append({'id':f'iliad-{pid:03d}','seq':pid,'book':bi,'from':s,'to':e,'lines':len(seg),'cite':f'{bi}.{s}–{e}','file':f'iliad-{pid:03d}.json','sha256':sha(seg),'status':'todo'})
        s=e+1
json.dump({'work':'Iliad','source':'source/iliad-monro-allen1920.json','cutRule':"parts end only where Monro & Allen begin a paragraph; target ~100 lines; iliad-001 (1.1-100) pinned",'parts':parts},open('parts.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
import statistics as st
L=[p['lines'] for p in parts]
print('lines',sum(len(b) for b in books),'paragraphs',sum(l['p'] for b in books for l in b),'parts',len(parts),'min/median/max',min(L),st.median(L),max(L))
print('over',MAXLEN,[(p['cite'],p['lines']) for p in parts if p['lines']>MAXLEN]); print('under',MINLEN,[(p['cite'],p['lines']) for p in parts if p['lines']<MINLEN])
print('oddities',len(oddities)); [print('  ',o) for o in oddities]
print(parts[0]); print(parts[1])

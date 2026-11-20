"""Make the Upanishads' source files from Sanskrit Wikisource (fetched 2026-11-20) — run once, in setup.
Each part file: blocks separated by a blank line; a numbered block's last line ends '॥ <n> ॥' (Devanagari);
an unnumbered block (invocation, heading, colophon) has no number. Every change beyond mechanical
cleaning (wiki markup, ZWJ/ZWNJ, NFC, '|' -> '।', spacing) is listed in CHANGES."""
import norm, re, json, os
from indic_transliteration import sanscript
D=lambda n: sanscript.transliterate(str(n), sanscript.IAST, sanscript.DEVANAGARI)
OUT='out'; os.makedirs(OUT,exist_ok=True)
CHANGES=[]
def num(b):
    m=re.search(r'॥\s*([०-९.]+)\s*॥\s*$',b[-1]); 
    return norm.d2i(m.group(1).split('.')[-1]) if m else None
def renum(b,n):   # normalise the number to '॥ n ॥'
    b=list(b); b[-1]=re.sub(r'॥\s*[०-९.]+\s*॥\s*$', f'॥ {D(n)} ॥', b[-1]); return b
def write(pid, bl, page):
    out=[]; seq=[]
    for b in bl:
        n=num(b)
        if n: b=renum(b,n); seq.append(n)
        out.append('\n'.join(b))
    assert seq==list(range(1,len(seq)+1)), (pid,seq)
    open(f'{OUT}/{pid}.txt','w').write('\n\n'.join(out)+'\n')
    return {'id':pid,'page':page,'units':len(bl),'numbered':len(seq)}
M=[]
def drop(bl, pred, why, pid):
    keep=[]
    for b in bl:
        if pred(b): CHANGES.append(f'{pid}: dropped the page-title line {" / ".join(b)!r} ({why})')
        else: keep.append(b)
    return keep
# --- Isha
bl=norm.blocks(open('ws-ईशोपनिषत्.txt').read())
M.append(write('isha',bl,'ईशोपनिषत्'))
# --- Kena: split at colophons
bl=norm.blocks(open('ws2-केनोपनिषद्.txt').read())
cut=[i for i,b in enumerate(bl) if re.search(r'इति केनोपनिषदि .* खण्डः',b[-1])]
segs=[bl[:cut[0]+1]]+[bl[a+1:b+1] for a,b in zip(cut,cut[1:])]
segs[-1]+=bl[cut[-1]+1:]
for k,s in enumerate(segs,1): M.append(write(f'kena-{k}',s,'केनोपनिषद्'))
# --- Katha: one page per vallī
pages=[('प्रथमोध्यायः','प्रथमवल्ली'),('प्रथमोध्यायः','द्वितीयवल्ली'),('प्रथमोध्यायः','तृतीयवल्ली'),('द्वितीयोध्यायः','प्रथमवल्ली'),('द्वितीयोध्यायः','द्वितीयवल्ली'),('द्वितीयोध्यायः','तृतीयवल्ली')]
for k,(a,v) in enumerate(pages,1):
    bl=norm.blocks(open(f'katha-{a}-{v}.txt').read())
    if k==1:
        i=next(i for i,b in enumerate(bl) if b[0].startswith('ॐ उशन्'))
        bl[i]=bl[i][:-1]+[bl[i][-1]+' ॥ १ ॥']; CHANGES.append('katha-1 1.1: verse number १ supplied (Wikisource prints none)')
        i=next(i for i,b in enumerate(bl) if b[0].startswith('पीतोदका'))
        b=bl[i]; assert b[1].endswith('॥ ३'), b
        bl[i:i+1]=[[b[0],b[1]+' ॥'],b[2:]]; CHANGES.append('katha-1 1.3–4: one Wikisource block split into verses ३ and ४; the closing ॥ of ३ supplied')
    if k==6:
        i=next(i for i,b in enumerate(bl) if b[-1].endswith('॥ १९ ॥'))
        bl[i]=bl[i][:-1]+[bl[i][-1].replace(' ॥ १९ ॥',' ॥')]; CHANGES.append('katha-6: the closing peace invocation (सह नाववतु…) is unnumbered (Wikisource numbers it as verse १९)')
    M.append(write(f'katha-{k}',bl,f'कठोपनिषत्/{a}/{v}'))
# --- Mundaka: split at colophons
raw=open('ws2-मुण्डकोपनिषद्.txt').read().split('== अधिकाध्ययनाय ==')[0]
bl=norm.blocks(raw)
bl=drop(bl, lambda b: b in (['॥ मुण्डकोपनिषत् ॥'],['॥ श्रीः ॥']), 'Wikisource page heading', 'mundaka')
cut=[i for i,b in enumerate(bl) if re.search(r'इति मुण्डकोपनिषदि',b[-1])]
segs=[bl[:cut[0]+1]]+[bl[a+1:b+1] for a,b in zip(cut,cut[1:])]
segs[-1]+=bl[cut[-1]+1:]
names=['1-1','1-2','2-1','2-2','3-1','3-2']
for k,s in zip(names,segs):
    if k=='2-2':
        i=next(i for i,b in enumerate(s) if b[0].startswith('यः सर्वज्ञः'))
        s[i:i+2]=[s[i]+s[i+1]]; CHANGES.append('mundaka-2-2 2.2.7: the two Wikisource blocks of verse ७ (यः सर्वज्ञः… and मनोमयः…) joined into one unit, as the verse is numbered')
    M.append(write(f'mundaka-{k}',s,'मुण्डकोपनिषद्'))
# --- Mandukya
bl=norm.blocks(open('man.txt').read())
bl=drop(bl, lambda b: b==['माण्डूक्योपनिषत्'], 'Wikisource page heading', 'mandukya')
M.append(write('mandukya',bl,'माण्डुक्योपनिषत्'))
json.dump({'parts':M,'changes':CHANGES},open(f'{OUT}/manifest.json','w'),ensure_ascii=False,indent=1)
for m in M: print(m)
print(*CHANGES,sep='\n')

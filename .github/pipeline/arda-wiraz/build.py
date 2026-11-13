import json,re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from units import U
from glossary import G
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
# the reader's WORD_CLASS (Latin + combining marks + Latin Ext. Additional/D + Greek for γ)
WC=r"A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ̀-ͯḀ-ỿ꜠-ꟿΆ-Ͽ"
WORD=re.compile('['+WC+']+(?:[-\\[\\]()]['+WC+']+)*')
sents=[]; spell={}
for x in U:
    toks=WORD.findall(x["t"]); wr=x["w"].split()
    assert len(toks)==len(wr),(x["ln"],len(toks),len(wr))
    d={"t":x["t"],"wr":wr,"l":x["l"]}
    if x.get("ln"): d["ln"]=x["ln"]
    for k in ("i","n"):
        if x.get(k): d[k]=x[k]
    if x.get("p"): d["p"]=True
    sents.append(d)
    for a,b in zip(toks,wr):
        spell.setdefault(a.lower(),[])
        if b not in spell[a.lower()]: spell[a.lower()].append(b)
keys=sorted(spell)
missing=[k for k in keys if k not in G]; extra=[k for k in G if k not in spell]
assert not missing,missing
assert not extra,extra
def written(forms):
    out=[]
    for f in forms:
        if f.isdigit() or re.fullmatch(r'\d+',f): out.append('the figure '+f)
        elif any(c.isupper() for c in f): out.append(f+(' (Aramaic word-sign with Persian ending)' if any(c.islower() for c in f) else ' (Aramaic word-sign)'))
        else: out.append(f)
    return ' · Written '+', also '.join(out)+'.'
gloss={k:G[k]+written(spell[k]) for k in keys}
story={
 "id":"arda-wiraz-001",
 "title":"Ardā Wirāz Nāmag",
 "titleEn":"The Book of Arda Viraf — Chapter 1: The Choosing of Wirāz",
 "work":"Ardā Wirāz Nāmag","workEn":"The Book of Arda Viraf (Ardā Wirāz Nāmag)",
 "part":"Chapter 1 · The choosing of Wirāz",
 "language":"Middle Persian (Pahlavi)","langCode":None,
 "numbering":"clause",
 "provisional":True,
 "draftNote":"The \"As written\" letters were set down from Haug's printed Pahlavi with the help of his own Roman reading of each word; not every letter has yet been checked against the page.",
 "source":open(os.path.join(HERE,'source.txt'),encoding='utf-8').read().strip(),
 "about":open(os.path.join(HERE,'about.txt'),encoding='utf-8').read().strip(),
 "glossaryFile":"arda-wiraz-glossary.json",
 "sentences":sents}
json.dump(story,open(os.path.join(ROOT,'arda-wiraz-001.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(gloss,open(os.path.join(ROOT,'arda-wiraz-glossary.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(sents),'units',len(keys),'glossary forms',sum(len(s['wr']) for s in sents),'words; coverage 100%')

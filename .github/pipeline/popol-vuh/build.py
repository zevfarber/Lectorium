import json,re,sys
sys.path.insert(0,'.')
import importlib, units; importlib.reload(units)
from units import U
WC=r"A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ̀-ͯḀ-ỿ꜠-ꟿ"
WORD=re.compile('['+WC+']+(?:[-\\[\\]()]['+WC+']+)*')
sents=[]
for x in U:
    d={"t":x["t"],"mt":[w.replace('~',' ') for w in x["m"].split()],"l":x["l"],"i":x["i"]}
    if x.get("n"): d["n"]=x["n"]
    if x.get("p"): d["p"]=True
    assert len(d["mt"])==len(WORD.findall(d["t"]))
    sents.append(d)
story={
 "id":"popol-vuh-001","sourceId":"popol-vuh-001",
 "title":"Are v xe oher ꜩih",
 "titleEn":"Popol Vuh — Preamble and the Making of the Earth",
 "work":"Popol Vuh","workEn":"Popol Vuh (The Council Book of the K'iche' Maya)",
 "part":"Preamble and the Making of the Earth",
 "language":"Classical K'iche'","langCode":None,
 "source":open('source.txt',encoding='utf-8').read().strip(),
 "about":open('about.txt',encoding='utf-8').read().strip(),
 "glossaryFile":"popol-vuh-glossary.json",
 "sentences":sents}
json.dump(story,open('popol-vuh-001.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
keys=sorted({w.lower() for s in sents for w in WORD.findall(s['t'])})
json.dump(keys,open('keys.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(sents),'units',len(keys),'keys',sum(len(WORD.findall(s['t'])) for s in sents),'tokens')

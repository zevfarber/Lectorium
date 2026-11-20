import re, json, sys, unicodedata
from indic_transliteration import sanscript
def d2i(s): return int(sanscript.transliterate(s, sanscript.DEVANAGARI, sanscript.IAST))
def clean(raw):
    raw=re.sub(r'(?s)<ref>.*?</ref>','',raw)
    raw=re.sub(r'<[^>]+>','',raw)
    raw=re.sub(r'\{\{[^}]*\}\}','',raw)
    raw=re.sub(r'(?m)^\s*(==.*==|\[\[.*\]\]|\*.*)\s*$','',raw)
    raw=raw.replace('‍','').replace('‌','').replace('|','।')
    raw=unicodedata.normalize('NFC',raw)
    return raw
def blocks(raw):
    out=[];cur=[]
    for l in clean(raw).split('\n'):
        s=re.sub(r'\s+',' ',l).strip()
        if not s: 
            if cur: out.append(cur); cur=[]
            continue
        cur.append(s)
    if cur: out.append(cur)
    return out
def split_khandas(raw, pat):
    """split raw page at headings matching pat (==..==)"""
    parts=re.split(pat,raw)
    return parts
def summarize(name,bl):
    nums=[]
    for b in bl:
        m=re.search(r'॥\s*([०-९]+)\s*॥\s*$',b[-1])
        nums.append(d2i(m.group(1)) if m else None)
    print(name, nums)
if __name__=='__main__':
    for f in sys.argv[1:]:
        summarize(f, blocks(open(f).read()))

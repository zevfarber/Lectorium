import json, re, html, glob, sys, os
RAW = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])) if len(sys.argv)>1 else '.', '')
ORDER = []
for v in ["一","二","三","四","五","六","七","八","九","十"]:
    for k in (1,2,3): ORDER.append(f"音訳蒙文元朝秘史/巻{v}-{k}")
for v in ["一","二"]:
    for k in (1,2,3): ORDER.append(f"音訳蒙文元朝秘史/続集巻{v}-{k}")
def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\u200b', '')
    return s.strip()
SPAN = re.compile(r'<span class="r2"><span class="t">(.*?)</span><span>(.*?)</span><span class="b">(.*?)</span></span>', re.S)
def extract(rawdir):
    pages = {}
    for f in glob.glob(os.path.join(rawdir, '*.json')):
        d = json.load(open(f, encoding='utf-8'))['parse']; pages[d['title']] = d['text']
    secs = {}; cur = None; order = []
    for title in ORDER:
        h = pages[title]
        # tokens: § markers, line ids, r2 spans
        for m in re.finditer(r'<b>§(\d+)</b>|<td>(\d\d:\d\d:\d\d)</td>|<span class="r2"><span class="t">(.*?)</span><span>(.*?)</span><span class="b">(.*?)</span></span>', h, re.S):
            if m.group(1):
                cur = int(m.group(1)); secs.setdefault(cur, {"page": title, "lines": []}); order.append(cur); line = None
            elif m.group(2):
                if cur is None: continue
                line = {"id": m.group(2), "words": []}; secs[cur]["lines"].append(line)
            else:
                if cur is None or line is None: continue
                line["words"].append({"gloss": clean(m.group(3)), "han": clean(m.group(4)), "rom": clean(m.group(5))})
    return secs, order
if __name__ == "__main__":
    """Writes secret-history-shiratori.json next to this script from raw/*.json (MediaWiki parse output of the
    36 pages of 音訳蒙文元朝秘史 on ja.wikisource, fetched 2026-10-12 by the Run 3 fetcher). Lines with no words
    (the Chinese abridged-translation rows) are dropped. Characters are kept exactly, including the
    edition's FVS markup (U+180B/U+180C) — the build strips those at publication, as the pilot did."""
    here = os.path.dirname(os.path.abspath(__file__))
    secs, order = extract(os.path.join(here, 'raw'))
    print(len(secs), order[:5], order[-5:], sorted(set(range(1,283))-set(secs)))
    nw = {s: sum(len(l["words"]) for l in v["lines"]) for s, v in secs.items()}
    print(sum(nw.values()), min(nw.values()), max(nw.values()))
    for v in secs.values():
        v["lines"] = [l for l in v["lines"] if l["words"]]
    doc = {"work": "Mongγol-un niγuča tobčiyan (The Secret History of the Mongols)",
           "edition": "Shiratori Kurakichi 白鳥庫吉, 音訳蒙文元朝秘史 (Tokyo, 1943), after the Ye Dehui print of 1905/1908; Japanese Wikisource transcription",
           "fields": "per word: gloss = Ming interlinear gloss; han = Chinese-character phonetic transcription (FVS markup kept); rom = Shiratori's romanization",
           "sections": {str(k): secs[k] for k in sorted(secs)}}
    json.dump(doc, open(os.path.join(here, 'secret-history-shiratori.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

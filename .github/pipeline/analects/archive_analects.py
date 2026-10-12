#!/usr/bin/env python3
"""Stage 0: build the Analects source archive from the Kanripo transcription of Zhu Xi's 論語集注.

Witness A (drafted from): Kanripo KR1h0015 四書章句集註, the Wenyuange 文淵閣 Siku Quanshu copy
(completed 1782), juan files KR1h0015_001..009 archived verbatim under source/kanripo/.
Zhu Xi's commentary is printed in parentheses after each stretch of text; those interruptions are
the sense-unit boundaries, exactly as Wang Bi's lemmata are for the Daodejing.

Output: source/analects-zhuxi-siku.json = {"books": {"1": {"title": "學而", "lemmata": [...]}, ...}}
with the bare text (no punctuation — the edition has none). Standard library only.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "kanripo")
NUM = "一二三四五六七八九十"
TITLES = ["學而", "為政", "八佾", "里仁", "公冶長", "雍也", "述而", "泰伯", "子罕", "鄉黨",
          "先進", "顏淵", "子路", "憲問", "衛靈公", "季氏", "陽貨", "微子", "子張", "堯曰"]


def cn(n):
    if n <= 10:
        return NUM[n - 1] if n < 10 else "十"
    if n < 20:
        return "十" + NUM[n - 11]
    return "二十"


def flat():
    out = ""
    for i in range(1, 10):
        t = open(os.path.join(SRC, "KR1h0015_%03d.txt" % i), encoding="utf-8").read()
        t = re.sub(r"<pb:[^>]*>", "", t)
        t = "\n".join(l for l in t.split("\n") if not l.startswith("#"))
        t = t.replace("¶", "").replace("\n", "").replace("　", "")
        out += t
    return out


def build():
    t = flat()
    # remove running heads (欽定四庫全書, 論語卷N 宋 朱子 集註) — they sit outside commentary
    t = re.sub(r"欽定四庫全書", "", t)
    t = re.sub(r"論語[卷巻][一二三四五六七八九十]+宋朱子集註", "", t)
    books = {}
    starts = []
    for n, title in enumerate(TITLES, 1):
        h = title + "第" + cn(n)
        k = t.find(h, starts[-1][1] if starts else 0)
        if k < 0:
            sys.exit("heading not found: " + h)
        starts.append((n, k, h))
    for idx, (n, k, h) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else len(t)
        body = t[k + len(h):end]
        # cut back-matter after book 20 (孟子序說 begins the Mencius)
        if n == 20:
            m = body.find("孟子序說")
            if m >= 0:
                body = body[:m]
        pieces = re.split(r"\([^)]*\)", body)
        lem = [p.replace("○", "") for p in pieces]
        lem = [p for p in lem if p]
        bad = [p for p in lem if re.search(r"[()（）]", p)]
        if bad:
            sys.exit("unbalanced commentary in book %d: %r" % (n, bad[:2]))
        books[str(n)] = {"title": TITLES[n - 1], "lemmata": lem}
    return books


def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


if __name__ == "__main__":
    books = build()
    out = {"witness": "Kanripo KR1h0015 (四書章句集註, 文淵閣四庫全書 copy, 1782), juan 1-9",
           "note": "Bare text of the Analects as Zhu Xi's 論語集注 prints it; one list item per stretch "
                   "between commentary interruptions. No punctuation: the edition has none.",
           "books": books}
    p = os.path.join(HERE, "source", "analects-zhuxi-siku.json")
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for n, b in books.items():
        s = "".join(b["lemmata"])
        print(n, b["title"], len(b["lemmata"]), "lemmata", len(s), "chars", sha(b["lemmata"])[:12])
    allc = "".join("".join(b["lemmata"]) for b in books.values())
    print("total chars", len(allc), "distinct", len(set(allc)))

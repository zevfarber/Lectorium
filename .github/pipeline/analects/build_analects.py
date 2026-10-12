#!/usr/bin/env python3
"""Build and validate one Analects part (book) from its draft.

    python3 build_analects.py analects-01            # build + validate, write files
    python3 build_analects.py analects-01 --check    # validate only (no writes)

Reads  drafts/<id>/units.py (UNITS), glossary_seed.py (GLOSS, POLY), parts.json, source archive.
Writes <repo>/<id>.json and merges <repo>/analects-glossary.json (additions only; never shortens).
Gates (all must pass): text = source exactly (Han characters, in order, per lemma); glyphs rebuild t;
every Han glyph has pinyin; every polyphone states its reading; 100% glossary coverage (every
character + every bound-compound lemma) with no unused keys; NFC; JSON round-trips; every unit has
l, and v/p/ln as the house shape requires. Standard library only.
"""
import hashlib, json, os, re, sys, unicodedata, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
HAN = re.compile(r"[㐀-䶿一-鿿豈-﫿]")
TOK = re.compile(r"^(\^?)([㐀-鿿豈-﫿]+)([^=/㐀-鿿]*)(?:=([^/]+))?(?:/(.*))?$")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def first_reading(entry):
    head = entry.split(" — ", 1)[0]
    return head.split()


def first_sense(entry):
    body = entry.split(" — ", 1)[1]
    return re.split(r";|\. ", body, maxsplit=1)[0].strip()


def build(pid, check=False):
    parts = json.load(open(os.path.join(HERE, "parts.json"), encoding="utf-8"))
    part = next(p for p in parts["parts"] if p["id"] == pid)
    src = json.load(open(os.path.join(HERE, parts["source"]), encoding="utf-8"))
    lemmata = src["books"][str(part["book"])]["lemmata"]
    seed = load(os.path.join(HERE, "glossary_seed.py"), "seed")
    GLOSS, POLY = seed.GLOSS, seed.POLY
    units = load(os.path.join(HERE, "drafts", pid, "units.py"), "units").UNITS
    errs = []

    if len(units) != len(lemmata):
        errs.append("unit count %d != lemma count %d" % (len(units), len(lemmata)))

    sentences, used = [], set()
    pas_no = 0
    for ui, u in enumerate(units):
        words, t = [], ""
        for raw in [x.strip() for x in u["w"].split(" | ")]:
            m = TOK.match(raw)
            if not m:
                errs.append("unit %d: bad token %r" % (ui, raw)); continue
            br, chars, punct, py, gl = m.groups()
            glosses = (gl or "").split("//")
            if py:
                pys = py.split()
            else:
                if len(chars) > 1:
                    e = GLOSS.get(chars)
                    pys = first_reading(e) if e else []
                else:
                    pys = first_reading(GLOSS[chars]) if chars in GLOSS else []
                    if chars in POLY:
                        errs.append("unit %d: polyphone %s has no stated reading" % (ui, chars))
            if len(pys) != len(chars):
                errs.append("unit %d: %s pinyin %r does not match characters" % (ui, chars, pys)); pys = (pys + ["?"] * len(chars))[:len(chars)]
            glyphs = [{"s": c, "tr": p, "role": "phon"} for c, p in zip(chars, pys)]
            if punct:
                glyphs.append({"s": punct, "tr": " ", "role": "punct"})
            morph = []
            if len(chars) > 1:
                if chars not in GLOSS:
                    errs.append("unit %d: bound compound %s has no glossary entry" % (ui, chars))
                morph.append({"lemma": chars, "gloss": glosses[0] or (first_sense(GLOSS[chars]) if chars in GLOSS else ""),
                              "g": list(range(len(chars)))})
                used.add(chars)
                for k, c in enumerate(chars):
                    cg = glosses[k + 1] if len(glosses) > k + 1 and glosses[k + 1] else (first_sense(GLOSS[c]) if c in GLOSS else "")
                    morph.append({"lemma": c, "gloss": cg, "g": [k]})
            else:
                morph.append({"lemma": chars, "gloss": glosses[0] or (first_sense(GLOSS[chars]) if chars in GLOSS else ""), "g": [0]})
            for c in chars:
                used.add(c)
                if c not in GLOSS:
                    errs.append("unit %d: character %s has no glossary entry" % (ui, c))
            w = {"reading": chars + " " + " ".join(pys), "glyphs": glyphs, "morph": morph}
            if br and words:
                w["br"] = True
            words.append(w)
            if br and t:
                t = t.rstrip() + "\n"
            t += chars + punct
        # gate: text equals source lemma
        bare = "".join(HAN.findall(t))
        if ui < len(lemmata) and bare != lemmata[ui]:
            errs.append("unit %d: text %s != source %s" % (ui, bare, lemmata[ui]))
        # gate: glyphs rebuild t
        rebuilt = "".join(g["s"] for w in words for g in w["glyphs"])
        if rebuilt != t.replace("\n", ""):
            errs.append("unit %d: glyphs do not rebuild t" % ui)
        s = {"t": unicodedata.normalize("NFC", t), "words": words, "l": u["l"]}
        if u.get("i"):
            s["i"] = u["i"]
        if u.get("n"):
            s["n"] = u["n"]
        s["v"] = True
        if u.get("pas"):
            pas_no += 1
            s["ln"] = pas_no
            if ui == 0:
                s["p"] = True
            else:
                s["p"] = True
        if s["t"] != t:
            errs.append("unit %d: t not NFC" % ui)
        if not s["l"]:
            errs.append("unit %d: no literal" % ui)
        if s["t"].count("\n") != s["l"].count("\n") and s["l"].count("\n"):
            pass  # l keeps lines where English can; not a gate
        sentences.append(s)

    if pas_no != part["passages"]:
        errs.append("passage count %d != %d" % (pas_no, part["passages"]))

    # glossary: coverage + no unused (for this part's keys) — merged later against the shared file
    gpath = os.path.join(REPO, "analects-glossary.json")
    shared = json.load(open(gpath, encoding="utf-8")) if os.path.exists(gpath) else {}
    merged = dict(shared)
    for k in sorted(used):
        new = GLOSS[k] if k in GLOSS else None
        if new is None:
            continue
        old = merged.get(k)
        if old is None or (len(new) >= len(old) and new.startswith(old[: max(1, len(old) // 2)])):
            merged[k] = new
        elif old != new:
            errs.append("glossary entry %s would be shortened or rewritten; broaden by addition only" % k)
    # every key in the merged glossary must be used by some published Analects part
    corpus_used = set(used)
    for f in os.listdir(REPO):
        if f.startswith("analects-") and f.endswith(".json") and f not in ("analects-glossary.json", pid + ".json"):
            d = json.load(open(os.path.join(REPO, f), encoding="utf-8"))
            for s2 in d["sentences"]:
                for w in s2["words"]:
                    for mm in w["morph"]:
                        corpus_used.add(mm["lemma"])
    unused = sorted(set(merged) - corpus_used)
    if unused:
        errs.append("unused glossary keys: %s" % " ".join(unused))
    missing = sorted(corpus_used - set(merged))
    if missing:
        errs.append("missing glossary keys: %s" % " ".join(missing))

    # pinyin on every phon glyph
    for si, s in enumerate(sentences):
        for w in s["words"]:
            for g in w["glyphs"]:
                if g["role"] == "phon" and (not g["tr"] or g["tr"] == "?"):
                    errs.append("unit %d: %s lacks pinyin" % (si, g["s"]))

    story = {
        "id": pid,
        "title": "論語 %s第%s" % (part["title"], part["cn"]),
        "titleEn": "The Analects — Book %d" % part["book"],
        "language": "Classical Chinese",
        "langCode": "zh-CN",
        "script": "chinese",
        "dir": "ltr",
        "numbering": "stanza",
        "glossaryFile": "analects-glossary.json",
        # keep a shipped audio field: a rebuild must never un-ship clips that exist
        **({"audio": "audio/" + pid} if os.path.exists(os.path.join(REPO, "audio", pid, "align.json")) else {}),
        "source": parts["sourceStatement"].replace("{BOOK}", str(part["book"])).replace("{TITLE}", part["title"]),
        "about": part["about"],
        "sentences": sentences,
        "glossary": {},
    }
    js = json.dumps(story, ensure_ascii=False, indent=1)
    if json.loads(js) != story:
        errs.append("JSON does not round-trip")
    print("%s: %d units, %d passages, %d tap-units, %d Han characters, glossary %d entries (%d new)"
          % (pid, len(sentences), pas_no, sum(len(s["words"]) for s in sentences),
             sum(len(HAN.findall(s["t"])) for s in sentences), len(merged), len(set(merged) - set(shared))))
    if errs:
        print("FAIL")
        for e in errs:
            print("  -", e)
        return 1
    print("PASS")
    if not check:
        open(os.path.join(REPO, pid + ".json"), "w", encoding="utf-8").write(js + "\n")
        json.dump(dict(sorted(merged.items())), open(gpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        open(gpath, "a").write("\n")
        print("wrote", pid + ".json", "and analects-glossary.json")
    return 0


if __name__ == "__main__":
    sys.exit(build(sys.argv[1], "--check" in sys.argv))

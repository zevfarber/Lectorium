#!/usr/bin/env python3
"""assemble_perrault.py -- the scripted, model-free stages of a Perrault batch.

Written 2026-09-10 (Perrault infrastructure firing). Nothing here takes judgment: every
output is determined by the archived source, the drafts, the patches and the conventions.

    novel     --root R --ids a,b [--slices 2] --out novel.json
              the forms the texts use that perrault-glossary.json lacks, derived with the reader's
              own WORD_RE before any drafting; each with the ids using it and one context unit of
              source text; split into alphabetical slices for the glossers
    assemble  --root R --draft draft.json [--patch p.json ...] --out <id>.json
              draft {id, about, advisory?, units:[{t, l, i?, n?}]} -> story file: p/v recomputed
              from the source blocks, `say` built from the speech map, title from the source,
              titleEn/part/source from the conventions, inline overrides from the patches
    merge-glossary --base G --patch p.json ... --out G2     additive; first lander wins
    merge-map      --base M --patch p.json ... --out M2     additive; first lander wins
    merge-manifest --base stories.json --root R --add id,... [--reissue id] --out S2
              additive: new entries appended in seq order, old bytes a verbatim prefix; the one
              authorised non-additive change is --reissue petit-chaperon-rouge (seq, part and the
              printed title synced to its re-issued story file), proven entry by entry
    rebuild-say --root R --ids a,b     rebuild `say` in place after a speech-map fix
    digest    FILE ...                  sha256 per file and one digest-of-digests
    selftest

Patch format (one per glosser):
    {"entries": {form: "LEMMA -- meaning (info)"},
     "overrides": {story_id: {form: "LEMMA -- meaning for this text"}},
     "speech": {old_form: modern_form},
     "properNouns": [..]}
"""
import copy, hashlib, json, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tools_french as TF   # noqa: E402

AW = TF.AW


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")


def write_json(path, obj):
    open(path, "wb").write(dump(obj))


def load(path):
    return json.load(open(path, encoding="utf-8"))


def source_for(root, sid):
    seq = TF.BY_ID[sid][0]
    return load(os.path.join(root, "sources", "perrault-%02d-source.json" % seq))


# ----------------------------------------------------------------------------- novel forms
def cmd_novel(root, ids, slices, out):
    gpath = os.path.join(root, TF.GLOSSARY_FILE)
    have = set(load(gpath)["glossary"]) if os.path.exists(gpath) else set()
    forms = {}
    for sid in ids:
        src = source_for(root, sid)
        units = [{"t": b["text"]} for b in src["blocks"]]
        toks = TF.node_tokens(os.path.join(root, "reader.html"), units)
        for b, o in zip(src["blocks"], toks):
            for k in o["keys"]:
                if k in have:
                    continue
                f = forms.setdefault(k, {"ids": [], "context": b["text"][:400]})
                if sid not in f["ids"]:
                    f["ids"].append(sid)
    keys = sorted(forms)
    n = max(1, slices)
    size = (len(keys) + n - 1) // n if keys else 0
    result = {"total": len(keys), "slices": []}
    for i in range(n):
        part = keys[i * size:(i + 1) * size]
        result["slices"].append({"from": part[0] if part else None, "to": part[-1] if part else None,
                                 "forms": {k: forms[k] for k in part}})
    write_json(out, result)
    print("novel forms: %d across %d text(s), %d slice(s)" % (len(keys), len(ids), n))
    return result


# ----------------------------------------------------------------------------- assemble
def flags_from_source(src, units):
    """p/v for each unit, recomputed from the source's block structure (never taken from a draft)."""
    S, sws, snl, bstarts = TF.stream([b["text"] for b in src["blocks"]])
    U, uws, unl, ustarts = TF.stream([u["t"] for u in units])
    if S != U:
        raise SystemExit("assemble: the draft's t does not reproduce the source; fix the draft, not the gate")
    bset = set(bstarts)
    bounds = bstarts + [len(S)]
    flags = []
    bi = 0
    for pos in ustarts:
        while bi + 1 < len(bstarts) and bounds[bi + 1] <= pos:
            bi += 1
        blk = src["blocks"][bi]
        f = {}
        if blk.get("v"):
            f["v"] = True
        elif pos in bset:
            f["p"] = True
        flags.append(f)
    return flags


def build_story(root, draft, patches=()):
    sid = draft["id"]
    seq, title_en = TF.BY_ID[sid]
    src = source_for(root, sid)
    smap_doc = load(os.path.join(root, ".github", "tools", "perrault-speech-map.json"))
    smap = {k.lower(): v for k, v in (smap_doc.get("map") or {}).items()}
    symbols = smap_doc.get("symbols") or {}
    units = draft["units"]
    flags = flags_from_source(src, units)
    sents = []
    for u, f in zip(units, flags):
        s = dict(f)
        s["t"] = u["t"]
        say = TF.build_say(u["t"], bool(f.get("v")), smap, symbols, TF.WORD_PAT)
        if say:
            s["say"] = say
        s["l"] = u["l"]
        if u.get("i") and u["i"] != u["l"]:
            s["i"] = u["i"]
        if u.get("n"):
            s["n"] = u["n"]
        sents.append(s)
    source_str = TF.SOURCE_HEAD.format(title=src["title"])
    if src.get("sourceClause"):
        source_str += " " + src["sourceClause"].strip()
    source_str += " " + TF.SOURCE_TAIL
    story = {"id": sid, "title": src["title"], "titleEn": title_en, "language": "French", "langCode": "fr-FR",
             "work": TF.WORK, "workEn": TF.WORK_EN, "part": title_en, "source": source_str,
             "about": draft["about"]}
    if draft.get("advisory"):
        story["advisory"] = draft["advisory"]
    story["wordClips"] = True
    story["glossaryFile"] = TF.GLOSSARY_FILE
    overrides = {}
    for _, p in patches:
        overrides.update((p.get("overrides") or {}).get(sid, {}))
    if overrides:
        story["glossary"] = dict(sorted(overrides.items()))
    story["sentences"] = sents
    return story


# ----------------------------------------------------------------------------- merges
def merge_additive(base, patches, section):
    out = dict(base)
    added, conflicts = [], []
    for name, p in patches:
        for k, v in (p.get(section) or {}).items():
            if k in out:
                if out[k] != v:
                    conflicts.append((k, name))
                continue
            out[k] = v
            added.append(k)
    for k in base:
        assert out[k] == base[k]
    return out, added, conflicts


def cmd_merge_glossary(base_path, patch_paths, out):
    patches = [(os.path.basename(p), load(p)) for p in patch_paths]
    if base_path and os.path.exists(base_path):
        doc = load(base_path)
    else:
        doc = {"work": TF.WORK, "workEn": TF.WORK_EN, "language": "French",
               "note": "Shared glossary for Perrault's Histoires ou contes du temps pass\u00e9 (1697). Keys are the "
                       "lowercased printed forms; 1697 spellings name their modern form.",
               "glossary": {}}
    base = doc["glossary"]
    new, added, conflicts = merge_additive(base, patches, "entries")
    ordered = dict(base)
    for k in sorted(added):
        ordered[k] = new[k]
    doc = dict(doc, glossary=ordered)
    write_json(out, doc)
    print("glossary: %d -> %d (+%d), %d conflict(s) kept as first lander%s" % (
        len(base), len(ordered), len(added), len(conflicts),
        (": " + ", ".join("%s (%s)" % c for c in conflicts[:20])) if conflicts else ""))
    return len(base), len(ordered), conflicts


def cmd_merge_map(base_path, patch_paths, out):
    doc = load(base_path)
    patches = [(os.path.basename(p), load(p)) for p in patch_paths]
    base = doc.get("map") or {}
    new, added, conflicts = merge_additive(base, patches, "speech")
    ordered = dict(base)
    for k in sorted(added):
        ordered[k.lower()] = new[k]
    proper = list(doc.get("properNouns") or [])
    for _, p in patches:
        for w in p.get("properNouns") or []:
            if w not in proper:
                proper.append(w)
    doc = dict(doc, properNouns=proper, map=ordered)
    write_json(out, doc)
    print("speech map: %d -> %d (+%d), %d conflict(s)" % (len(base), len(ordered), len(added), len(conflicts)))
    return len(base), len(ordered), conflicts


def manifest_entry(story, seq):
    return {"id": story["id"], "title": story["title"], "titleEn": story["titleEn"], "language": "French",
            "work": TF.WORK, "workEn": TF.WORK_EN, "part": story["titleEn"], "file": story["id"] + ".json",
            "seq": seq}


def merge_manifest(base_bytes, root, add_ids, reissue=None):
    man = json.loads(base_bytes.decode("utf-8"))
    if dump(man) != base_bytes:
        raise SystemExit("manifest: base does not re-serialise byte-exact; refusing to write")
    entries = man["stories"]
    have = {e["id"] for e in entries}
    new_entries = []
    for sid in sorted(add_ids, key=lambda s: TF.BY_ID[s][0]):
        if sid in have:
            raise SystemExit("manifest: %s is already live" % sid)
        new_entries.append(manifest_entry(load(os.path.join(root, sid + ".json")), TF.BY_ID[sid][0]))
    out = copy.deepcopy(man)
    if reissue:
        st = load(os.path.join(root, reissue + ".json"))
        for e in out["stories"]:
            if e["id"] == reissue:
                e["title"] = st["title"]
                e["part"] = st["titleEn"]
                e["seq"] = TF.BY_ID[reissue][0]
    out["stories"].extend(new_entries)
    out_bytes = dump(out)
    # proofs
    old_e, new_e = man["stories"], out["stories"]
    assert new_e[:len(old_e)] and len(new_e) == len(old_e) + len(new_entries)
    for a, b in zip(old_e, new_e):
        if a["id"] == reissue:
            diff = {k for k in set(a) | set(b) if a.get(k) != b.get(k)}
            assert diff <= {"title", "part", "seq"}, diff
            assert [k for k in b if k != "seq"] == list(a.keys())
        else:
            assert a == b and list(a) == list(b)
    if not reissue:
        close = b"\n ]\n}"
        assert base_bytes.endswith(close)
        assert out_bytes.startswith(base_bytes[:-len(close)] + b",")
    return out_bytes


def cmd_digest(paths):
    rows = []
    for p in paths:
        rows.append((os.path.basename(p), hashlib.sha256(open(p, "rb").read()).hexdigest()))
    dod = hashlib.sha256("".join("%s  %s\n" % (h, n) for n, h in sorted(rows)).encode()).hexdigest()
    for n, h in sorted(rows):
        print("%s  %s" % (h, n))
    print("digest-of-digests %s over %d file(s)" % (dod, len(rows)))
    return dod


# ----------------------------------------------------------------------------- selftest
def selftest():
    reader = None
    for cand in (os.path.join(HERE, "..", "..", "reader.html"), "reader.html"):
        if os.path.exists(cand):
            reader = open(cand, encoding="utf-8").read(); break
    if reader is None:
        print("assemble selftest: FAIL \u2014 reader.html not found"); return 1
    tmp = tempfile.mkdtemp()
    ok = True
    try:
        TF._fixture_tree(tmp, reader)
        sid = "petit-chaperon-rouge"
        live = load(os.path.join(tmp, sid + ".json"))
        # pretend the story is not yet live: remove it, its manifest entry and the glossary
        draft = {"id": sid, "about": live["about"],
                 "units": [{k: u[k] for k in ("t", "l", "i", "n") if k in u} for u in live["sentences"]]}
        gl = load(os.path.join(tmp, TF.GLOSSARY_FILE))
        os.remove(os.path.join(tmp, TF.GLOSSARY_FILE))
        man = load(os.path.join(tmp, "stories.json")); man["stories"] = man["stories"][:1]
        open(os.path.join(tmp, "stories.json"), "wb").write(dump(man))
        nov = cmd_novel(tmp, [sid], 2, os.path.join(tmp, "novel.json"))
        forms = [k for s in nov["slices"] for k in s["forms"]]
        ok &= sorted(forms) == sorted(gl["glossary"])
        patch_a = {"entries": {k: gl["glossary"][k] for k in nov["slices"][0]["forms"]}, "speech": {}}
        patch_b = {"entries": {k: gl["glossary"][k] for k in nov["slices"][1]["forms"]}, "speech": {"icy": "ici"}}
        write_json(os.path.join(tmp, "pa.json"), patch_a); write_json(os.path.join(tmp, "pb.json"), patch_b)
        story = build_story(tmp, draft)
        ok &= dump(story) == dump(live)
        print("  assembled story reproduces the fixture byte-exact: %s" % (dump(story) == dump(live)))
        write_json(os.path.join(tmp, sid + ".json"), story)
        cmd_merge_glossary(None, [os.path.join(tmp, "pa.json"), os.path.join(tmp, "pb.json")], os.path.join(tmp, TF.GLOSSARY_FILE))
        mb = open(os.path.join(tmp, "stories.json"), "rb").read()
        open(os.path.join(tmp, "stories.json"), "wb").write(merge_manifest(mb, tmp, [sid]))
        rep, _ = TF.run_gates(tmp, [sid], baseline={}, patches=[("pa.json", patch_a), ("pb.json", patch_b)])
        print("  gates on the assembled tree: %s" % ("PASS" if not rep.fails() else "FAIL"))
        if rep.fails():
            print(rep.text())
        ok &= not rep.fails()
        # negative: a merge refusing to add an id twice, and first-lander-wins
        try:
            merge_manifest(open(os.path.join(tmp, "stories.json"), "rb").read(), tmp, [sid])
            ok = False; print("  duplicate add NOT refused")
        except SystemExit:
            print("  duplicate add refused: yes")
        _, _, conf = cmd_merge_glossary(os.path.join(tmp, TF.GLOSSARY_FILE),
                                        [os.path.join(tmp, "pa.json")], os.path.join(tmp, "g2.json"))
        write_json(os.path.join(tmp, "pc.json"), {"entries": {"moulin": "moulin \u2014 changed"}})
        _, _, conf = cmd_merge_glossary(os.path.join(tmp, TF.GLOSSARY_FILE),
                                        [os.path.join(tmp, "pc.json")], os.path.join(tmp, "g3.json"))
        kept = load(os.path.join(tmp, "g3.json"))["glossary"]["moulin"] == gl["glossary"]["moulin"]
        print("  first lander wins on conflict: %s" % kept)
        ok &= kept and bool(conf)
        # re-issue path: seq/part/title only
        man = load(os.path.join(tmp, "stories.json"))
        e = man["stories"][1]; del e["seq"]; e["title"] = "Le petit Chaperon rouge"
        open(os.path.join(tmp, "stories.json"), "wb").write(dump(man))
        out = merge_manifest(open(os.path.join(tmp, "stories.json"), "rb").read(), tmp, [], reissue=sid)
        e2 = json.loads(out)["stories"][1]
        good = e2.get("seq") == 3 and e2["title"] == story["title"] and list(e2)[-1] == "seq"
        print("  re-issue sets seq/part/title only: %s" % good)
        ok &= good
        # a drafted t that drops a word is refused before anything is written
        bad = copy.deepcopy(draft); bad["units"][1]["t"] = "Ils heureux."
        try:
            build_story(tmp, bad); ok = False; print("  broken draft NOT refused")
        except SystemExit:
            print("  broken draft refused: yes")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("assemble selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv):
    import argparse
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "selftest":
        return selftest()
    ap = argparse.ArgumentParser(prog="assemble_perrault.py " + cmd)
    if cmd == "novel":
        ap.add_argument("--root", required=True); ap.add_argument("--ids", required=True)
        ap.add_argument("--slices", type=int, default=2); ap.add_argument("--out", required=True)
        a = ap.parse_args(rest); cmd_novel(a.root, a.ids.split(","), a.slices, a.out); return 0
    if cmd == "assemble":
        ap.add_argument("--root", required=True); ap.add_argument("--draft", required=True)
        ap.add_argument("--patch", action="append", default=[]); ap.add_argument("--out", required=True)
        a = ap.parse_args(rest)
        story = build_story(a.root, load(a.draft), [(os.path.basename(p), load(p)) for p in a.patch])
        write_json(a.out, story); print("assembled %s: %d units" % (story["id"], len(story["sentences"]))); return 0
    if cmd == "merge-glossary":
        ap.add_argument("--base"); ap.add_argument("--patch", action="append", default=[]); ap.add_argument("--out", required=True)
        a = ap.parse_args(rest); cmd_merge_glossary(a.base, a.patch, a.out); return 0
    if cmd == "merge-map":
        ap.add_argument("--base", required=True); ap.add_argument("--patch", action="append", default=[]); ap.add_argument("--out", required=True)
        a = ap.parse_args(rest); cmd_merge_map(a.base, a.patch, a.out); return 0
    if cmd == "merge-manifest":
        ap.add_argument("--base", required=True); ap.add_argument("--root", required=True)
        ap.add_argument("--add", default=""); ap.add_argument("--reissue"); ap.add_argument("--out", required=True)
        a = ap.parse_args(rest)
        out = merge_manifest(open(a.base, "rb").read(), a.root, [x for x in a.add.split(",") if x], a.reissue)
        open(a.out, "wb").write(out); print("manifest merged; proofs passed"); return 0
    if cmd == "rebuild-say":
        ap.add_argument("--root", required=True); ap.add_argument("--ids", required=True)
        a = ap.parse_args(rest)
        smap_doc = load(os.path.join(a.root, ".github", "tools", "perrault-speech-map.json"))
        smap = {k.lower(): v for k, v in (smap_doc.get("map") or {}).items()}
        for sid in a.ids.split(","):
            p = os.path.join(a.root, sid + ".json"); st = load(p); changed = 0
            for u in st["sentences"]:
                say = TF.build_say(u["t"], bool(u.get("v")), smap, smap_doc.get("symbols") or {}, TF.WORD_PAT)
                if say != u.get("say"):
                    changed += 1
                    items = [(k, v) for k, v in u.items() if k != "say"]; u.clear()
                    for k, v in items:
                        u[k] = v
                        if k == "t" and say:
                            u["say"] = say
            write_json(p, st); print("%s: say rebuilt on %d unit(s)" % (sid, changed))
        return 0
    if cmd == "digest":
        cmd_digest(rest); return 0
    print("unknown command %r" % cmd); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

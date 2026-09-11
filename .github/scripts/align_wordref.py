#!/usr/bin/env python3
"""Karaoke word timings for stories with a spoken layer (`say`) and/or word clips.

Written 2026-09-10 for Perrault's 1697 text, as the sibling of align_dtw.py, which it
reuses and never changes. Two differences from align_dtw.py:

1. THE REFERENCE IS THE STORY'S OWN VOICE. Where audio/<id>/w/<n>.mp3 exists for a
   token's glossary key (words.json), that clip, in the same Chirp voice that read the
   sentence, is the DTW reference for the token. espeak-ng is the fallback per token.

2. THE CLIP SPEAKS `say`, THE PAGE SHOWS `t`. A string `say` has the same WORD_RE tokens
   as `t`, in order, each identical or modernised (estoit -> etait), except that a printed
   symbol which is spoken but is not a word (`&` -> "et") adds one spoken token. Those
   symbols are declared in the `symbols` section of .github/tools/*-speech-map.json. The
   aligner times the spoken sequence and then folds each symbol's time into the previous
   word (or into the next word when the symbol opens the sentence), so align.json carries
   exactly one [start, end] per WORD_RE token of `t`, which is what the reader highlights.

If a sentence's `say` does not line up with `t` that way (the gate tools_french.py
refuses such files, so this should never happen), the sentence is aligned against the
tokens of `t` with the espeak reference and the problem is logged.

Usage: python3 align_wordref.py <story-id> [audio_dir]
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Mirrors reader.html exactly (WORD_CLASS, HAN_CLASS, WORD_RE, wordKey). tools_french.py
# proves token-for-token parity with the deployed reader's regex, run in node, per text.
WORD_CLASS = ('A-Za-z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\\u0100-\\u024F\\u0300-\\u036F\\u1E00-\\u1EFF'
              '\u0386-\u03ff\u0400-\u04ff\\u1F00-\\u1FFF\\u1820-\\u1877\\u180B-\\u180E'
              '\\u0620-\\u065F\\u0670-\\u06D3\\u06D5-\\u06ED')
HAN_CLASS = '\\u3400-\\u4DBF\\u4E00-\\u9FFF\\uF900-\\uFAFF'
WORD_PAT = '[' + HAN_CLASS + ']|[' + WORD_CLASS + ']+(?:[-\\[\\]()][' + WORD_CLASS + ']+)*'
WORD_RE = re.compile(WORD_PAT)


def word_key(w):
    return re.sub('[\u180B-\u180E]', '', re.sub(r'[\[\]()]', '', w)).lower()


_TABLES = None


def speech_tables():
    """Merge the `symbols` and `wordClipReadings` sections of every tools/*-speech-map.json."""
    global _TABLES
    if _TABLES is None:
        t = {"symbols": {}, "wordClipReadings": {}}
        for f in sorted(glob.glob(os.path.join(HERE, "..", "tools", "*-speech-map.json"))):
            d = json.load(open(f, encoding="utf-8"))
            for sec in t:
                t[sec].update(d.get(sec) or {})
        _TABLES = t
    return _TABLES


def spoken_sequence(s):
    """[('w', token) | ('sym', char)] in the order they occur in `t`."""
    syms = speech_tables()["symbols"]
    if not syms:
        return [("w", m.group(0)) for m in WORD_RE.finditer(s["t"])]
    pat = re.compile(WORD_PAT + "|[" + "".join(re.escape(c) for c in syms) + "]")
    out = []
    for m in pat.finditer(s["t"]):
        g = m.group(0)
        out.append(("sym", g) if g in syms else ("w", g))
    return out


def spoken_tokens(s):
    say = s.get("say")
    src = say if isinstance(say, str) and say.strip() else s["t"]
    return WORD_RE.findall(src)


def lined_up(s):
    """(sequence, spoken tokens, ok): ok when the spoken tokens line up one-for-one."""
    seq = spoken_sequence(s)
    sp = spoken_tokens(s)
    if not (isinstance(s.get("say"), str) and s["say"].strip()):
        seq = [x for x in seq if x[0] == "w"]
    return seq, sp, len(seq) == len(sp)


def token_pairs(s):
    """(printed token, spoken token) for every WORD_RE token of `t`."""
    seq, sp, ok = lined_up(s)
    if not ok:
        return [(w, w) for w in WORD_RE.findall(s["t"])]
    return [(tok, spk) for (kind, tok), spk in zip(seq, sp) if kind == "w"]


def main():
    import numpy as np
    import librosa
    from collections import defaultdict
    sys.path.insert(0, HERE)
    import align_dtw as AD   # load, mfcc, espeak_word, SR, HOP; VOICE comes from ESPEAK_VOICE

    sid = sys.argv[1]
    adir = sys.argv[2] if len(sys.argv) > 2 else "audio/" + sid
    story = json.load(open(sid + ".json", encoding="utf-8"))
    words = {}
    if os.path.exists(adir + "/words.json"):
        words = json.load(open(adir + "/words.json", encoding="utf-8"))
    cache = {}

    def ref_for(printed, spoken_tok, kind):
        if kind == "w":
            n = words.get(word_key(printed))
            p = "%s/w/%s.mp3" % (adir, n)
            if n is not None and os.path.exists(p):
                if p not in cache:
                    y = AD.load(p)
                    yt, _ = librosa.effects.trim(y, top_db=35)
                    cache[p] = yt if len(yt) >= 160 else y
                return cache[p]
        return AD.espeak_word(spoken_tok)

    def align(mp3, items):
        """items: [(kind, printed, spoken)] -> [[start, end]] per item."""
        y = AD.load(mp3)
        D = len(y) / AD.SR
        if not items:
            return [], D
        parts, bounds, cur = [], [], 0
        gap = np.zeros(int(0.03 * AD.SR))
        for kind, printed, spk in items:
            wy = ref_for(printed, spk, kind)
            st = cur
            parts.append(wy); cur += len(wy); bounds.append((st, cur))
            parts.append(gap); cur += len(gap)
        Xr = AD.mfcc(np.concatenate(parts)); Xt = AD.mfcc(y)
        _, wp = librosa.sequence.dtw(X=Xr, Y=Xt, metric="cosine"); wp = wp[::-1]
        acc = defaultdict(list)
        for rf, tf in zip(wp[:, 0], wp[:, 1]):
            acc[rf].append(tf)
        mp = np.full(Xr.shape[1], -1.0); last = 0.0
        for rf in range(Xr.shape[1]):
            if acc[rf]:
                mp[rf] = np.mean(acc[rf])
        for k in range(len(mp)):
            if mp[k] < 0:
                mp[k] = last
            else:
                last = mp[k]

        def t(sm):
            f = min(max(int(round(sm / AD.HOP)), 0), Xr.shape[1] - 1)
            return mp[f] * AD.HOP / AD.SR
        out = [[round(min(t(a), t(b)), 3), round(max(t(a), t(b)), 3)] for (a, b) in bounds]
        for k in range(len(out)):
            if k > 0 and out[k][0] < out[k - 1][1] - 0.001:
                out[k][0] = out[k - 1][1]
            if out[k][1] < out[k][0]:
                out[k][1] = out[k][0]
            out[k] = [round(min(out[k][0], D), 3), round(min(out[k][1], D), 3)]
        return out, D

    out, bad = {}, []
    for i, s in enumerate(story["sentences"]):
        tt = WORD_RE.findall(s["t"])
        seq, sp, ok = lined_up(s)
        if ok:
            items = [(kind, tok, spk) for (kind, tok), spk in zip(seq, sp)]
        else:
            bad.append((i, "say does not line up with t (%d vs %d); aligned on t" % (len(seq), len(sp))))
            items = [("w", w, w) for w in tt]
        try:
            arr, _ = align("%s/%d.mp3" % (adir, i), items)
        except Exception as e:  # noqa: BLE001
            arr, items = [], []
            bad.append((i, str(e)))
        # fold symbol timings into the neighbouring word
        timings = []
        pending_start = None
        for (kind, _, _), span in zip(items, arr):
            if kind == "sym":
                if timings:
                    timings[-1][1] = max(timings[-1][1], span[1])
                else:
                    pending_start = span[0] if pending_start is None else pending_start
                continue
            span = list(span)
            if pending_start is not None:
                span[0] = min(span[0], pending_start)
                pending_start = None
            timings.append(span)
        if len(timings) != len(tt):
            bad.append((i, "len %d!=tok %d" % (len(timings), len(tt))))
        out[str(i)] = timings
        if i % 12 == 0:
            print("aligned", i, "/", len(story["sentences"])); sys.stdout.flush()
    json.dump(out, open("%s/align.json" % adir, "w", encoding="utf-8"), ensure_ascii=False)
    print("DONE", len(out), "sentences,", sum(len(v) for v in out.values()),
          "timings; reference: word clips where present; issues:", bad or "none")


if __name__ == "__main__":
    main()

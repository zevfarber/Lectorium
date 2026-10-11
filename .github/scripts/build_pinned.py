#!/usr/bin/env python3
"""Prepared audio for languages with no voice of their own: a carrier voice reads per-word IPA pins.

Written 2026-09-28 for Ancient Greek (reconstructed Attic, after Allen, Vox Graeca). The recipe is
the one proven on the Hávamál (claude/norse-audio-carrier-findings.md): de-DE-Neural2-D, SSML
<phoneme alphabet="ipa">, deterministic, so one listen approves a whole language.

Called by build_audio.py for a story whose `language` is in PINNED. Writes, like every other audio
story: audio/<id>/<n>.mp3 (one per sentence), texts.json (the SSML each clip speaks, so a changed
line or a changed pin re-synthesizes and nothing else does), w/<n>.mp3 + words.json (word clips
for the popup and as the aligner's reference), voice.txt, then runs align_wordref.py.

Usage: python3 build_pinned.py <story-id>     Env: GOOGLE_TTS_KEY
"""
import json, os, re, shutil, subprocess, sys, time, base64, urllib.request, urllib.error
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import align_wordref as AW

PINNED = {
    # Voice switched 2026-10-04 from de-DE-Neural2-D to de-DE-Wavenet-B: Zev compared them by ear and
    # could not tell them apart, and WaveNet's free allowance is 4M characters a month against 1M.
    # The pilot clips already built with Neural2 (aesop-001, odyssey-001) are kept.
    # 2026-10-04, later: Greek may also use de-DE-Neural2-D (Voice A of the comparison, which Zev could not
    # tell from Voice C). Its free allowance (1M a month) is a separate pool that only Greek can use, so
    # Greek takes it first and leaves the WaveNet pool to Latin and Russian. A story keeps the voice it
    # was begun in; each story is one voice throughout.
    "Ancient Greek": {"module": "greek_g2p", "voice": "de-DE-Wavenet-B", "lang": "de-DE",
                      "voices": ["de-DE-Neural2-D", "de-DE-Wavenet-B"],
                      "rate": 0.9, "espeak": "grc"},
    # Latin, added 2026-10-04: restored Classical, normal word stress, long vowels held, elision as in
    # verse; vowel lengths from the Scansion overlay (latin_verse.py). Voice and rate as in the pilot
    # Zev approved by ear (audio-pilot/latin.html, Voice A).
    "Latin": {"module": "latin_verse", "voice": "de-DE-Wavenet-B", "lang": "de-DE",
              "rate": 0.85, "espeak": "la"},
    # Old East Slavic (Igor's Campaign), added 2026-10-04: the proem's hand method made automatic —
    # ru-RU-Wavenet-A reads a modern-normalized carrier, every word overridden by an IPA pin through
    # Google's customPronunciations (slovo_g2p.py; stress lexicon .github/pipeline/slovo/audio-lexicon.json).
    "Old East Slavic": {"module": "slovo_g2p", "voice": "ru-RU-Wavenet-A", "lang": "ru-RU",
                        "rate": 0.92, "espeak": "ru", "custom": True},
    # Akkadian (Laws of Hammurabi), added 2026-10-11: conventional reconstructed Old Babylonian
    # (akkadian_g2p.py). Zev auditioned German, American English, French, Arabic and Hebrew carriers and
    # chose the German voice "for now" (Voice A, de-DE-Neural2-D, rate 0.85). Akkadian stories are
    # words-model: `t` is cuneiform and each words[i].say is the reading, so the module builds the SSML
    # from the words and align_wordref.py times one span per word.
    "Akkadian (Old Babylonian)": {"module": "akkadian_g2p", "voice": "de-DE-Neural2-D", "lang": "de-DE",
                                  "voices": ["de-DE-Neural2-D", "de-DE-Wavenet-B"],
                                  "rate": 0.85, "espeak": "de"},
}
TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
# customPronunciations (per-word IPA over plain text) is a v1beta1 field; the proem was made with it.
TTS_URL_BETA = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"

# MONTHLY BUDGET (2026-10-11; replaces the free-allowance guard of 2026-10-04). Zev's rule now:
# everything in the queue gets audio, and paying is fine, up to US$10 a month across all voices. Every
# character sent to Google (here and in build_audio.py) is counted in audio/_tts-usage.json, which is
# committed with the clips (the build-audio job runs one at a time, so the count is exact). Google's
# free tier is used first; past it, characters are priced below. A story whose voicing would take the
# month past the budget is skipped, not half-built, and recorded under "blocked"; the daily budget
# check (a scheduled task) tells Zev, who decides whether to raise the budget or pause. A skipped story
# has no align.json, so the daily "missing" sweep picks it up again once there is room.
USAGE_FILE = "audio/_tts-usage.json"
FAMILIES = ("Chirp", "Neural2", "Wavenet", "Standard")
FREE_CHARS = {"Chirp": 1000000, "Neural2": 1000000, "Wavenet": 4000000, "Standard": 4000000}
USD_PER_MILLION = {"Chirp": 30.0, "Neural2": 16.0, "Wavenet": 16.0, "Standard": 4.0}
MONTHLY_BUDGET_USD = 10.0


def _family(voice):
    return next((f for f in FAMILIES if f in voice), voice)


def _month():
    return time.strftime("%Y-%m", time.gmtime())


def _usage():
    try:
        return json.load(open(USAGE_FILE, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}


def _charge(voice, n):
    u = _usage(); m = time.strftime("%Y-%m", time.gmtime())
    fam = u.setdefault(_family(voice), {}); fam[m] = fam.get(m, 0) + n
    os.makedirs(os.path.dirname(USAGE_FILE), exist_ok=True)
    json.dump(u, open(USAGE_FILE, "w", encoding="utf-8"), indent=1, sort_keys=True)


def used_this_month(voice):
    return _usage().get(_family(voice), {}).get(_month(), 0)


def month_cost(extra_voice=None, extra=0):
    """US$ this month beyond Google's free tiers, optionally with `extra` characters in `extra_voice`."""
    u, m, total = _usage(), _month(), 0.0
    for f in FAMILIES:
        used = u.get(f, {}).get(m, 0) + (extra if extra_voice and _family(extra_voice) == f else 0)
        total += max(0, used - FREE_CHARS[f]) * USD_PER_MILLION[f] / 1e6
    return round(total, 2)


def block(sid, voice, need):
    """Record a story skipped for the budget, so the daily budget check can report it."""
    u, m = _usage(), _month()
    b = u.setdefault("blocked", {}).setdefault(m, {})
    b[sid] = {"voice": voice, "chars": need, "would_cost_usd": month_cost(voice, need)}
    os.makedirs(os.path.dirname(USAGE_FILE), exist_ok=True)
    json.dump(u, open(USAGE_FILE, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print("BUDGET: %s skipped; voicing it would bring this month to US$%.2f (budget US$%.2f)"
          % (sid, month_cost(voice, need), MONTHLY_BUDGET_USD))
THROTTLE_S = 0.25
ELISION = "’᾽'ʼ᾿"
# printed punctuation -> what the carrier voice sees (pauses only)
PUNCT = {".": ".", ",": ",", ";": "?", ";": "?", "·": ",", "·": ",", "!": "!", ":": ","}


def synth_ssml(ssml, cfg, key, attempts=6):
    return synth_input({"ssml": ssml}, cfg, key, attempts)


def input_cost(inp):
    """Characters charged against the monthly allowance (counted generously: pins included)."""
    if "ssml" in inp:
        return len(inp["ssml"])
    return len(inp["text"]) + sum(len(p["phrase"]) + len(p["pronunciation"])
                                  for p in inp.get("customPronunciations", {}).get("pronunciations", []))


def synth_input(inp, cfg, key, attempts=6):
    body = json.dumps({"input": inp,
                       "voice": {"languageCode": cfg["lang"], "name": cfg["voice"]},
                       "audioConfig": {"audioEncoding": "MP3", "speakingRate": cfg["rate"]}}).encode()
    url = TTS_URL_BETA if "customPronunciations" in inp else TTS_URL
    last = None
    for a in range(attempts):
        req = urllib.request.Request(url + "?key=" + key, data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                audio = base64.b64decode(json.load(r)["audioContent"])
            _charge(cfg["voice"], input_cost(inp))
            return audio
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429 or 500 <= e.code < 600:
                time.sleep(min(5 * 2 ** a, 60)); continue
            raise RuntimeError("TTS %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:500]))
        except Exception as e:  # noqa: BLE001
            last = e; time.sleep(2 * (a + 1))
    raise last


_ROMAN = str.maketrans({"ˈ": "", "ʰ": "h", "ŋ": "ng", "ɛ": "e", "ɔ": "o", "ʏ": "y", "ɪ": "i",
                        "ʊ": "u", "ː": "", "j": "i"})


def ph(ipa):
    # The inner text is what the voice reads if it rejects the IPA (it did so for every string with ʰ,
    # and read the old placeholder "x" as the letter — "ex"). A rough romanization is the safer fallback.
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(ipa, {'"': "&quot;"}),
                                                            escape(ipa.translate(_ROMAN)))


def sentence_ssml(t, G):
    """One <phoneme> per word; an elided word is spoken glued to the next one."""
    parts, pend = [], ""
    pos = 0
    toks = list(AW.WORD_RE.finditer(t))
    for k, m in enumerate(toks):
        gap = t[pos:m.start()]
        for ch in gap:
            if ch in PUNCT:
                parts.append(PUNCT[ch])
        pos = m.end()
        p = G.ipa(m.group(0))
        after = t[m.end():m.end() + 1]
        if after and after in ELISION and k + 1 < len(toks):
            pend += p.replace("ˈ", "")
            continue
        parts.append(ph(pend + p) if (pend + p) else "")
        pend = ""
    for ch in t[pos:]:
        if ch in PUNCT:
            parts.append(PUNCT[ch])
    body = ""
    for x in parts:
        body += (x if x in PUNCT.values() else (" " + x))
    return "<speak>" + body.strip() + "</speak>"


def _key(inp):
    """What texts.json records for a clip: the SSML itself (as before), or the full request as JSON."""
    return inp["ssml"] if set(inp) == {"ssml"} else json.dumps(inp, ensure_ascii=False, sort_keys=True)


def _custom_input(text, G):
    t, pins = G.request(text, AW.WORD_RE)
    return {"text": t, "customPronunciations": {"pronunciations": [
        {"phrase": ph_, "phoneticEncoding": "PHONETIC_ENCODING_IPA", "pronunciation": ip}
        for ph_, ip in pins]}}


def sentence_input(s, G, cfg):
    if cfg.get("custom"):
        return _custom_input(s["t"], G)
    if hasattr(G, "sentence_ssml"):                 # a module that reads the whole unit (Latin: scansion)
        return {"ssml": G.sentence_ssml(s)}
    return {"ssml": sentence_ssml(s["t"], G)}


def word_inputs(story, G, cfg):
    """{glossary key: (ipa, request)} for the word clips."""
    if hasattr(G, "word_ipa_map"):
        ipas = G.word_ipa_map(story, AW.word_key)
    else:
        keys = {}
        for s in story["sentences"]:
            for tok in AW.WORD_RE.findall(s["t"]):
                keys.setdefault(AW.word_key(tok), tok)
        ipas = {k: G.ipa(tok) for k, tok in keys.items()}
        if cfg.get("custom"):
            return {k: (ipas[k], _custom_input(keys[k], G)) for k in keys}
    # A word clip whose IPA holds a space (an Akkadian reading of two words, "adi ḫamšīšu") gets one
    # <phoneme> per word; for every single-word pin this is the same SSML as before.
    return {k: (ip, {"ssml": "<speak>" + " ".join(ph(x) for x in ip.split()) + "</speak>"})
            for k, ip in ipas.items()}


def shared_word_clips(voice):
    """Word clips already made in this voice anywhere in the library: {texts.json entry: mp3 path}.

    Added 2026-10-04 to stay inside the free allowance: the same word said by the same voice from the
    same pins is the same clip, so a word met in an earlier fable or book is copied, not paid for again.
    """
    out = {}
    if not os.path.isdir("audio"):
        return out
    for d in os.listdir("audio"):
        vf, wtf = "audio/%s/voice.txt" % d, "audio/%s/w/texts.json" % d
        try:
            if open(vf).read().strip() != voice:
                continue
            for n, t in json.load(open(wtf, encoding="utf-8")).items():
                p = "audio/%s/w/%s.mp3" % (d, n)
                if os.path.exists(p) and os.path.getsize(p) > 0:
                    out.setdefault(t, p)
        except Exception:  # noqa: BLE001
            continue
    return out


def estimate(story, G, cfg, adir):
    """Characters this story will actually send in cfg's voice: changed units, plus word clips that exist
    nowhere in the library in that voice yet."""
    tf = adir + "/texts.json"
    prev = json.load(open(tf, encoding="utf-8")) if os.path.exists(tf) else {}
    need = 0
    for i, s in enumerate(story["sentences"]):
        x = sentence_input(s, G, cfg)
        if prev.get(str(i)) != _key(x) or not os.path.exists("%s/%d.mp3" % (adir, i)):
            need += input_cost(x)
    shared, seen = shared_word_clips(cfg["voice"]), set()
    for k, (ip, x) in word_inputs(story, G, cfg).items():
        kx = _key(x)
        if kx in shared or kx in seen or not re.search("[aeiouyɛɔɪʏʊœɨ]", ip):
            continue
        seen.add(kx); need += input_cost(x)
    return need


def main():
    sid = sys.argv[1]
    story = json.load(open(sid + ".json", encoding="utf-8"))
    cfg = PINNED[story["language"]]
    G = __import__(cfg["module"])
    key = os.environ["GOOGLE_TTS_KEY"]
    adir = "audio/" + sid
    tf, wf, wtf = adir + "/texts.json", adir + "/words.json", adir + "/w/texts.json"

    # A reading made by hand before this builder existed (the Igor proem, July 2026: takes chosen by
    # ear) has clips and align.json but no texts.json. Record what it says now, as build_audio.py does
    # for its own old stories, and leave its clips and timings alone; a later text change still
    # re-synthesizes exactly the changed units.
    if os.path.exists(adir + "/align.json") and not os.path.exists(tf):
        json.dump({str(i): _key(sentence_input(s, G, cfg)) for i, s in enumerate(story["sentences"])},
                  open(tf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if os.path.exists(wf) and not os.path.exists(wtf):
            words = json.load(open(wf, encoding="utf-8"))
            wi = word_inputs(story, G, cfg)
            json.dump({str(n): _key(wi[k][1]) for k, n in words.items() if k in wi},
                      open(wtf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if not os.path.exists(adir + "/voice.txt"):
            open(adir + "/voice.txt", "w").write(cfg["voice"] + "\n")
        print("hand-made reading kept as it is; baseline recorded for %s" % sid)
        return

    # Voice: the one this story was begun in; else, of the language's voices, the one that costs least
    # this month (free tier first). Skipped if even that would pass the monthly budget.
    vf = adir + "/voice.txt"
    begun = open(vf).read().strip() if os.path.exists(vf) else ""
    choices = [begun] if begun else cfg.get("voices", [cfg["voice"]])
    cfg = dict(cfg)
    priced = []
    for v in choices:
        cfg["voice"] = v
        need = estimate(story, G, cfg, adir)
        priced.append((month_cost(v, need), choices.index(v), v, need))
    cost, _, v, need = min(priced)
    cfg["voice"] = v
    if need and cost > MONTHLY_BUDGET_USD:
        block(sid, v, need)
        return
    os.makedirs(adir + "/w", exist_ok=True)

    # Aspirates: keep [pʰ tʰ kʰ] only if the voice accepts ʰ; otherwise fall back to p t k.
    if hasattr(G, "ASP") and G.ASP:
        try:
            synth_ssml("<speak>" + ph("ˈpʰos") + "</speak>", cfg, key)
        except RuntimeError as e:
            print("voice refuses ʰ, aspirates fall back to plain stops:", e); G.ASP = ""
    open(vf, "w").write(cfg["voice"] + "\n")

    prev = json.load(open(tf, encoding="utf-8")) if os.path.exists(tf) else {}
    sins = [sentence_input(s, G, cfg) for s in story["sentences"]]
    words = json.load(open(wf, encoding="utf-8")) if os.path.exists(wf) else {}
    wtexts = json.load(open(wtf, encoding="utf-8")) if os.path.exists(wtf) else {}
    winp = word_inputs(story, G, cfg)
    shared = shared_word_clips(cfg["voice"])

    texts, made = {}, 0
    for i, x in enumerate(sins):
        texts[str(i)] = _key(x)
        p = "%s/%d.mp3" % (adir, i)
        if os.path.exists(p) and os.path.getsize(p) > 0 and prev.get(str(i)) == texts[str(i)]:
            continue
        open(p, "wb").write(synth_input(x, cfg, key)); made += 1; time.sleep(THROTTLE_S)
    json.dump(texts, open(tf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("sentence clips: %d written of %d for %s" % (made, len(story["sentences"]), sid))

    nxt = max([int(n) for n in words.values()] + [-1]) + 1
    wmade, copied, skipped = 0, 0, []
    for k in sorted(winp):
        ip, x = winp[k]
        if not re.search("[aeiouyɛɔɪʏʊœɨ]", ip):
            skipped.append(k); continue          # a bare elided consonant has nothing to say alone
        if k not in words:
            words[k] = nxt; nxt += 1
        n = str(words[k]); p = "%s/w/%s.mp3" % (adir, n); kx = _key(x)
        if os.path.exists(p) and os.path.getsize(p) > 0 and wtexts.get(n) == kx:
            continue
        if kx in shared and os.path.abspath(shared[kx]) != os.path.abspath(p):
            shutil.copyfile(shared[kx], p); copied += 1
        else:
            open(p, "wb").write(synth_input(x, cfg, key)); wmade += 1
            shared[kx] = p
            time.sleep(THROTTLE_S)
        wtexts[n] = kx
    json.dump(words, open(wf, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    json.dump(wtexts, open(wtf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("word clips: %d synthesized, %d copied from earlier texts, of %d keys; no clip for %s"
          % (wmade, copied, len(winp), skipped or "none"))

    env = dict(os.environ); env["ESPEAK_VOICE"] = cfg["espeak"]
    subprocess.run(["python3", os.path.join(HERE, "align_wordref.py"), sid], check=True, env=env)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Decide which story ids this run should build audio for.

Sources, in priority order:
  1. workflow_dispatch input `id` (a story id or <id>.json filename).
  2. Root-level *.json files changed in the push that are audio-bearing stories.

A file counts as an audio-bearing story when it is a root-level JSON with a
non-empty `sentences` array, an `id`, and a `langCode` we have a voice for.
Glossaries, stories.json, and non-Latin-TTS texts are skipped.

Writes `ids=<space separated>` to $GITHUB_OUTPUT.
"""
import json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wordre import sent_tokens

VOICE_LANGS = {"de-DE", "fr-FR", "zh-CN", "ar-XA", "he-IL"}   # keep in sync with build_audio.py VOICES
# Languages read by a carrier voice under IPA pins (build_pinned.py PINNED). A language goes in
# PINNED_AUTO once its pilot reading is approved; before that only an explicit dispatch builds it.
PINNED_AUTO = {"Ancient Greek",     # approved by ear 2026-10-04 (WaveNet voice)
               "Latin",             # approved by ear 2026-10-04 (audio-pilot/latin.html, Voice A)
               "Old East Slavic"}   # the proem's hand method (July 2026), automatic from 2026-10-04
_DISPATCH_OK = set()

# Order of the daily "missing" sweep (2026-10-04). Audio must stay inside Google's free monthly
# allowance, which holds only part of the backlog each month, so the sweep takes stories in the order
# Zev asked for them ("Odyssey first"); anything not listed comes after, alphabetically.
MISSING_PRIORITY = ["odyssey-", "slovo-", "aesop-", "ovid-met-", "pyramus-thisbe"]
# Works whose new parts are built the moment they are pushed, ahead of the sweep (Zev, 2026-10-04).
BUILD_ON_PUSH = ("odyssey-",)


def _priority(sid):
    return next((n for n, p in enumerate(MISSING_PRIORITY) if sid.startswith(p)), len(MISSING_PRIORITY))


def _pinned_new(path, sid):
    """A pinned-voice story with no audio yet: left to the daily sweep, so the monthly allowance is
    spent in priority order rather than on whatever was pushed first. Corrections to a story that
    already has audio are still rebuilt on push."""
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return False
    return (not d.get("langCode") and d.get("language") in PINNED_AUTO
            and not sid.startswith(BUILD_ON_PUSH)
            and not os.path.exists(os.path.join("audio", sid, "align.json")))


def story_id(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(d, dict):
        return None
    if not d.get("sentences"):
        return None
    if d.get("langCode") not in VOICE_LANGS:
        # Pinned-voice languages (build_pinned.py): picked on push, "missing" and the stale
        # check only once the language is in PINNED_AUTO; a dispatch by id always builds.
        if d.get("langCode") or d.get("language") not in (PINNED_AUTO | _DISPATCH_OK):
            return None
    return d.get("id") or None


def changed_root_jsons():
    before = os.environ.get("BEFORE_SHA", "").strip()
    if before and set(before) != {"0"}:
        range_args = [before, "HEAD"]
    else:
        # new branch / no usable before-sha: fall back to the last commit
        range_args = ["HEAD~1", "HEAD"]
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", *range_args],
            capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return []
    return [f for f in out.split() if "/" not in f and f.endswith(".json")]


# Backfilling a missing baseline re-runs alignment for the whole story, which is expensive.
# Every story in the library lacks one right now, so an uncapped sweep would try to re-align the
# entire corpus in a single job. Backfill a few per run instead: it converges over a handful of
# pushes and no run is ever large.
BASELINE_BACKFILL_PER_RUN = 4
MISSING_PER_RUN = 40   # stories per "missing" sweep (2026-10-04: the Greek backfill runs daily)
GREEK_ALONGSIDE = 10   # of those, kept for Greek stories further down the order (see main)


def stale_alignment():
    """Story ids whose shipped align.json no longer has one timing per words-model unit.

    Word counts change without any character changing — binding two characters into one
    tap-unit is invisible to every text-level check — so alignment has to be verified against
    the story itself, not inferred from a diff.
    """
    out, baseline = [], []
    for f in sorted(os.listdir(".")):
        if "/" in f or not f.endswith(".json"):
            continue
        sid = story_id(f)
        if not sid:
            continue
        adir = os.path.join("audio", sid)
        ap = os.path.join(adir, "align.json")
        if not os.path.exists(ap):
            continue
        # No texts.json means this story predates the text-cache and has no baseline. Establish
        # one NOW, while its clips and text are known to agree. If we wait until someone corrects
        # a line, the grandfathering in build_audio would record the NEW text against the OLD clip
        # and the correction would silently never be spoken.
        if not os.path.exists(os.path.join(adir, "texts.json")):
            baseline.append(sid)
            continue
        try:
            story = json.load(open(f, encoding="utf-8"))
            al = json.load(open(ap, encoding="utf-8"))
        except Exception:
            continue
        # Every story is checked, not only words-model ones: on 2026-09-20 the Arabic Nights
        # shipped with an empty timing list for every sentence, and a words-only check could
        # not see it. sent_tokens() is the reader's own splitter (wordre.py).
        for i, s in enumerate(story["sentences"]):
            want = len(sent_tokens(s))
            if len(al.get(str(i), [])) != want:
                print("stale alignment: %s sentence %d has %d timings for %d units"
                      % (sid, i, len(al.get(str(i), [])), want))
                out.append(sid)
                break

    # stale alignment is a live defect and always runs; baselines are housekeeping and are rationed
    take = baseline[:BASELINE_BACKFILL_PER_RUN]
    if baseline:
        print("audio text baseline missing for %d story/ies; backfilling %d this run: %s"
              % (len(baseline), len(take), " ".join(take)))
    return out + take


def missing_audio():
    """Every audio-bearing root story that has no clips at all.

    WHY THIS MODE EXISTS. The push trigger only ever sees the stories changed in
    one push, and `stale_alignment` only looks at stories that ALREADY have an
    align.json. A batch whose clips were built and then lost is therefore
    unreachable by both: the story files sit on main, unchanged, and nothing will
    pick them up again. That is exactly what happened on 17 Aug 2026 — run #89
    synthesized all 47 tales of the P5-P10 landing, 2h 3m of paid TTS, and lost
    the lot when its push was rejected non-fast-forward. Before this mode the only
    remedy was one workflow_dispatch per tale, forty-seven times.

    Dispatch with id = "missing" to rebuild everything that has no audio.
    """
    out = []
    for f in sorted(os.listdir(".")):
        if "/" in f or not f.endswith(".json"):
            continue
        sid = story_id(f)
        if not sid:
            continue
        if not os.path.exists(os.path.join("audio", sid, "align.json")):
            out.append(sid)
    return sorted(out, key=lambda x: (_priority(x), x))


def main():
    ids = []
    dispatch = os.environ.get("DISPATCH_ID", "").strip()
    if dispatch.lower() == "missing":
        ids.extend(missing_audio())
        print("dispatch 'missing': %d story/ies have no clips yet" % len(ids))
        # One job may run at most 6 hours. A daily scheduled sweep takes a slice; the rest wait.
        # Greek has a second free pool (Neural2) that Latin and Russian cannot use, so a few Greek
        # stories ride along every day even while the Latin backlog is ahead of them in the order.
        head = ids[:MISSING_PER_RUN - GREEK_ALONGSIDE]
        # (With the Odyssey first the head is Greek already; the rule matters once Latin leads.)
        greek = [x for x in ids[len(head):] if x.startswith(("aesop-", "odyssey-"))][:GREEK_ALONGSIDE]
        ids = head + greek
    elif dispatch:
        _DISPATCH_OK.update(PINNED_AUTO)
        name = dispatch[:-5] if dispatch.endswith(".json") else dispatch
        fn = name + ".json"
        if os.path.exists(fn):
            sid = story_id(fn)
            if sid:
                ids.append(sid)
    else:
        for f in changed_root_jsons():
            if os.path.exists(f):
                sid = story_id(f)
                if sid and _pinned_new(f, sid):
                    print("%s: new, left to the daily sweep (priority order)" % sid)
                elif sid:
                    ids.append(sid)
        ids.extend(stale_alignment())

    ids = sorted(set(ids), key=lambda x: (_priority(x), x))
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a") as g:
            g.write("ids=" + " ".join(ids) + "\n")
    print("audio targets:", " ".join(ids) if ids else "(none)")


if __name__ == "__main__":
    main()

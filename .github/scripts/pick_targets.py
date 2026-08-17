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
import json, os, subprocess

VOICE_LANGS = {"de-DE", "fr-FR", "zh-CN"}   # keep in sync with build_audio.py VOICES


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
        for i, s in enumerate(story["sentences"]):
            want = len(s["words"]) if s.get("words") else None
            if want is None:
                continue
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
    return out


def main():
    ids = []
    dispatch = os.environ.get("DISPATCH_ID", "").strip()
    if dispatch.lower() == "missing":
        ids.extend(missing_audio())
        print("dispatch 'missing': %d story/ies have no clips yet" % len(ids))
    elif dispatch:
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
                if sid:
                    ids.append(sid)
        ids.extend(stale_alignment())

    ids = sorted(set(ids))
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a") as g:
            g.write("ids=" + " ".join(ids) + "\n")
    print("audio targets:", " ".join(ids) if ids else "(none)")


if __name__ == "__main__":
    main()

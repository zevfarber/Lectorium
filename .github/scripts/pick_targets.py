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


def stale_alignment():
    """Story ids whose shipped align.json no longer has one timing per words-model unit.

    Word counts change without any character changing — binding two characters into one
    tap-unit is invisible to every text-level check — so alignment has to be verified against
    the story itself, not inferred from a diff.
    """
    out = []
    for f in os.listdir("."):
        if "/" in f or not f.endswith(".json"):
            continue
        sid = story_id(f)
        if not sid:
            continue
        ap = os.path.join("audio", sid, "align.json")
        if not os.path.exists(ap):
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
    return out


def main():
    ids = []
    dispatch = os.environ.get("DISPATCH_ID", "").strip()
    if dispatch:
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

#!/usr/bin/env python3
"""Run 3 source fetcher (runs on the GitHub runner, which has open internet; Claude sessions do not).

Reads .github/pipeline/run3/fetch-requests.json: a list of
  {"url": ..., "dest": "<repo-relative path>", "note": "..."}
and downloads every entry whose dest does not exist yet. Writes a log of what happened to
.github/pipeline/run3/fetch-log.json (url, dest, status, bytes, sha256, error). Never overwrites a
file that exists (delete it in a commit to re-fetch). Files over 95 MB are refused (GitHub limit).
"""
import hashlib, json, os, sys, time, urllib.request, urllib.error

REQ = ".github/pipeline/run3/fetch-requests.json"
LOG = ".github/pipeline/run3/fetch-log.json"
UA = "LectoriumArchiver/1.0 (https://zevfarber.github.io/Lectorium/; public-domain source archiving)"
MAX = 95 * 1024 * 1024


def get(url, tries=3):
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read(MAX + 1)
                return r.status, data
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (403, 404, 410):
                return e.code, b""
        except Exception as e:
            last = e
        time.sleep(5 * (k + 1))
    raise RuntimeError(str(last))


def main():
    reqs = json.load(open(REQ, encoding="utf-8"))
    log = json.load(open(LOG, encoding="utf-8")) if os.path.exists(LOG) else []
    done = 0
    for r in reqs:
        dest = r["dest"]
        if os.path.exists(dest):
            continue
        ent = {"url": r["url"], "dest": dest, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        try:
            st, data = get(r["url"])
            ent["status"] = st
            if st == 200 and data and len(data) <= MAX:
                os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
                open(dest, "wb").write(data)
                ent["bytes"] = len(data)
                ent["sha256"] = hashlib.sha256(data).hexdigest()
                done += 1
            elif len(data) > MAX:
                ent["error"] = "too large"
        except Exception as e:
            ent["error"] = str(e)[:300]
        print(json.dumps(ent, ensure_ascii=False))
        log.append(ent)
        time.sleep(1)
    json.dump(log, open(LOG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"fetched {done} file(s)")


if __name__ == "__main__":
    main()

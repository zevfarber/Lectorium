#!/usr/bin/env python3
"""Run 3 command line. Run from anywhere; paths are resolved from this file.

    python3 r3.py next                     which work and part this firing takes (reads queue-run3.txt)
    python3 r3.py claim   <work> <id> <phase>
    python3 r3.py release <work> <id>
    python3 r3.py establish-packet <work> <id>   scan-based parts: what to read, and the OCR draft
    python3 r3.py pin     <work> <id>      established text written -> check it, pin its sha256, status established
    python3 r3.py packet  <work> <id>      checks the pinned source against parts.json, writes drafts/<id>/packet.md
    python3 r3.py build   <work> <id>      drafts/<id>/units.json (+ gloss.json) -> the story file, glossary, manifest
    python3 r3.py validate <work> <id>     must print PASS
    python3 r3.py publish <work> <id>      status published, plan.md, claim released
    python3 r3.py block   <work> <id> "<reason>"   a part that cannot be done unattended: status blocked
                                           (skipped by `next`), reason in QUESTIONS.md, claim released
    python3 r3.py done    <work>           last part published -> DONE marker + LOG line
    python3 r3.py plan    <work>
Every command refuses, changing nothing, when something is wrong.
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r3lib as R

QUEUE = os.path.join(R.PIPE, 'queue-run3.txt')


def queue():
    out = []
    for line in open(QUEUE, encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if line:
            out.append(line)
    return out


def cmd_next():
    for w in queue():
        if os.path.exists(os.path.join(R.PIPE, w, 'DONE')):
            continue
        p, action = R.next_part(w)
        if p is None:
            parts = R.parts_doc(w)['parts']
            blocked = [q['id'] for q in parts if q.get('status') == 'blocked']
            claimed = [q['id'] for q in parts if q.get('status') not in ('published', 'blocked')]
            if claimed:
                print(f'WORK {w}\nBUSY every remaining part is under a live claim: {", ".join(claimed)} — stop')
                return
            if blocked:
                print(f'SKIP {w}: only blocked parts are left ({", ".join(blocked)}) — see its QUESTIONS.md; going on')
                continue
            print(f'WORK {w}\nCOMPLETE run: python3 ../run3/r3.py done {w}')
            return
        print(f'WORK {w}\nPART {p["id"]}\nACTION {action}\nNAME {p.get("name", "")}')
        return
    print('ALL DONE')


def cmd_claim(work, pid, phase):
    R.part(work, pid)
    if R.live_claim(work, pid):
        R.die(pid, 'is already claimed')
    with open(os.path.join(R.claims_dir(work), pid + '.md'), 'w', encoding='utf-8') as f:
        f.write(time.strftime('%Y-%m-%dT%H:%M', time.gmtime()) + f'Z · {phase}\n')
    print('CLAIMED', pid)


def cmd_release(work, pid):
    p = os.path.join(R.claims_dir(work), pid + '.md')
    if os.path.exists(p):
        os.remove(p)
    print('RELEASED', pid)


def cmd_establish_packet(work, pid):
    H = R.hooks(work)
    p = R.part(work, pid)
    if not hasattr(H, 'establish_packet'):
        R.die(work, 'has no establishment step')
    out = H.establish_packet(p)
    path = os.path.join(R.drafts(work, pid), 'establish.md')
    open(path, 'w', encoding='utf-8').write(out)
    print('WROTE', os.path.relpath(path, R.ROOT))


def cmd_pin(work, pid):
    H = R.hooks(work)
    doc = R.parts_doc(work)
    p = next(q for q in doc['parts'] if q['id'] == pid)
    errs = H.check_established(p) if hasattr(H, 'check_established') else []
    if errs:
        for e in errs:
            print('  ERROR', e)
        R.die('established text fails its checks')
    p['sha256'] = R.sha(H.slice_source(p))
    p['status'] = 'established'
    R.save_parts(work, doc)
    cmd_plan(work)
    print('PINNED', pid, p['sha256'][:12])


def cmd_packet(work, pid):
    H = R.hooks(work)
    p = R.part(work, pid)
    src = H.slice_source(p)
    if src is None:
        R.die(pid, 'has no established text yet')
    if p.get('sha256') and R.sha(src) != p['sha256']:
        R.die(pid, 'source does not match the sha256 pinned in parts.json — write it to QUESTIONS.md, release the claim, stop')
    out = H.packet(p)
    path = os.path.join(R.drafts(work, pid), 'packet.md')
    open(path, 'w', encoding='utf-8').write(out)
    print('WROTE', os.path.relpath(path, R.ROOT))
    if hasattr(H, 'forms'):
        novel, known = H.forms(p)
        R.jdump(novel, os.path.join(R.drafts(work, pid), 'novel-forms.json'))
        R.jdump(known, os.path.join(R.drafts(work, pid), 'known-forms.json'))
        print(f'forms: {len(novel)} novel, {len(known)} already in the glossary')


def cmd_build(work, pid):
    H = R.hooks(work)
    cfg = R.work_cfg(work)
    p = R.part(work, pid)
    src = H.slice_source(p)
    if src is None or (p.get('sha256') and R.sha(src) != p['sha256']):
        R.die('source does not match parts.json sha256')
    d = R.drafts(work, pid)
    units = R.jload(os.path.join(d, 'units.json'))
    gpath = os.path.join(d, 'gloss.json')
    gloss = R.jload(gpath) if os.path.exists(gpath) else {}
    story, writes = H.assemble(p, units, gloss)        # writes: {path: obj} besides the story
    errs, warns = R.common_checks(story, p, cfg)
    real = R.jload                                      # validate against the glossary as it WILL be written
    R.jload = lambda path: writes[path] if path in writes else real(path)
    try:
        e2, w2 = H.validate(p, story)
    finally:
        R.jload = real
    errs += e2
    warns += w2
    if errs:
        for e in errs[:80]:
            print('  ERROR', e)
        R.die(f'{len(errs)} error(s); nothing written')
    R.jdump(story, os.path.join(R.ROOT, p['file']))
    for path, obj in writes.items():
        R.jdump(obj, path)
    entry = {k: story[k] for k in ('id', 'title', 'titleEn', 'language', 'work', 'workEn', 'part') if k in story}
    for k in ('group', 'seq'):
        if k in p:
            entry[k] = p[k]
    entry['file'] = p['file']
    R.manifest_insert(work, pid, entry)
    for w in warns[:60]:
        print('  WARN', w)
    print(f'BUILT {pid}: {len(story["sentences"])} units → {p["file"]}')


def cmd_validate(work, pid):
    H = R.hooks(work)
    cfg = R.work_cfg(work)
    p = R.part(work, pid)
    sp = os.path.join(R.ROOT, p['file'])
    if not os.path.exists(sp):
        R.die('not built yet')
    story = R.jload(sp)
    errs, warns = R.common_checks(story, p, cfg)
    e2, w2 = H.validate(p, story)
    errs += e2
    warns += w2
    M = R.jload(os.path.join(R.ROOT, 'stories.json'))
    if not any(e.get('id') == pid for e in M['stories']):
        errs.append('no manifest entry in stories.json')
    for e in errs[:80]:
        print('  ERROR', e)
    for w in warns[:60]:
        print('  WARN', w)
    print('PASS' if not errs else f'FAIL ({len(errs)} errors)')
    sys.exit(0 if not errs else 1)


def cmd_block(work, pid, *reason):
    doc = R.parts_doc(work)
    p = next((q for q in doc['parts'] if q['id'] == pid), None)
    if p is None:
        R.die(pid, 'is not in parts.json')
    p['status'] = 'blocked'
    p['blocked'] = ' '.join(reason) or 'see QUESTIONS.md'
    R.save_parts(work, doc)
    with open(os.path.join(R.PIPE, work, 'QUESTIONS.md'), 'a', encoding='utf-8') as f:
        f.write(f'- {time.strftime("%Y-%m-%d")} · {pid} · BLOCKED: {p["blocked"]} · Decided meanwhile: the part is skipped '
                f'by later firings; the owner (or a session with him) resolves it and sets its status back to todo.\n')
    cmd_plan(work)
    cmd_release(work, pid)
    print('BLOCKED', pid)


def cmd_publish(work, pid):
    H = R.hooks(work)
    cfg = R.work_cfg(work)
    q = R.part(work, pid)
    sp = os.path.join(R.ROOT, q['file'])
    if not os.path.exists(sp):
        R.die('not built yet')
    story = R.jload(sp)
    errs, _ = R.common_checks(story, q, cfg)
    errs += H.validate(q, story)[0]
    if not any(e.get('id') == pid for e in R.jload(os.path.join(R.ROOT, 'stories.json'))['stories']):
        errs.append('no manifest entry')
    if errs:
        for e in errs[:20]:
            print('  ERROR', e)
        R.die('the part does not validate; not published')
    doc = R.parts_doc(work)
    p = next(q for q in doc['parts'] if q['id'] == pid)
    p['status'] = 'published'
    R.save_parts(work, doc)
    cmd_plan(work)
    cmd_release(work, pid)


def cmd_done(work):
    doc = R.parts_doc(work)
    left = [q['id'] for q in doc['parts'] if q.get('status') != 'published']
    if left:
        R.die('not finished:', ', '.join(left))
    open(os.path.join(R.PIPE, work, 'DONE'), 'w').close()
    with open(os.path.join(R.PIPE, work, 'LOG.md'), 'a', encoding='utf-8') as f:
        f.write(f'- {time.strftime("%Y-%m-%d")} · DONE · all {len(doc["parts"])} parts published; Run 3 moves to the next work in queue-run3.txt\n')
    print('DONE marker written for', work)


def cmd_plan(work):
    doc = R.parts_doc(work)
    cfg = R.work_cfg(work)
    ps = doc['parts']
    n = sum(1 for q in ps if q.get('status') == 'published')
    lines = [f'# {cfg["workEn"]} — plan', '',
             f'{n} of {len(ps)} parts published (Run 3). Generated by `python3 ../run3/r3.py plan {work}`.', '',
             '| part | name | range | status |', '|---|---|---|---|']
    for q in ps:
        lines.append(f'| {q["id"]} | {q.get("name", "")} | {q.get("cite", "")} | {q.get("status", "todo")} |')
    open(os.path.join(R.PIPE, work, 'plan.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(0)
    c = a[0].replace('-', '_')
    fn = globals().get('cmd_' + c)
    if not fn:
        R.die('unknown command', a[0])
    fn(*a[1:])

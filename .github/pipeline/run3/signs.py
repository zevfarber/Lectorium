#!/usr/bin/env python3
"""Add a sign to a shared sign glossary and keep the copy embedded in the reader identical.

The reader (index.html, and its master copy reader.html — the two files are identical) embeds each script's
sign glossary in SIGN_GLOSSARIES. A new sign must go into BOTH the JSON file and those embedded copies, or
the sign browser and the word popup will not know it. This tool is the only way a run changes those two
HTML files: it rewrites the one JSON object for the script and nothing else, and refuses if anything else
would change.

    python3 signs.py check                       embedded copies == the JSON files (exit 1 if not)
    python3 signs.py add cuneiform KEY 'CUNEIFORM SIGN NAME' '{"name":..., "type":..., "sound":..., "values":[...], "label":...}'
    python3 signs.py add anatolian A###  'ANATOLIAN HIEROGLYPH A###' '{"name":..., "type":..., "sound":..., "pron":null, "determines":null}'
The glyph is always taken from Python's unicodedata by the Unicode name you give — never typed by hand.
"""
import json, os, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
FILES = {'cuneiform': ('signs-cuneiform.json', 'cuneiform'), 'anatolian': ('signs-anatolian.json', 'Anatolian hieroglyphs')}
HTML = ['index.html', 'reader.html']


def block(h, key):
    tag = f'\n "{key}": '
    i = h.find(tag)
    if i < 0:
        raise SystemExit(f'no embedded block "{key}"')
    j = i + len(tag)
    depth, k, instr, esc = 0, j, False, False
    while True:
        c = h[k]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return j, k + 1
        k += 1


def fmt(script, signs):
    """The embedded block's own layout, so a one-sign addition is a one-line diff."""
    if script == 'anatolian':
        return '{\n' + ',\n'.join(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}'
                                    for k, v in signs.items()) + '\n }'
    return json.dumps(signs, ensure_ascii=False, indent=1)


def load(script):
    fn, key = FILES[script]
    d = json.load(open(os.path.join(ROOT, fn), encoding='utf-8'))
    return d, d.get('signs', d), key


def check():
    ok = True
    for script, (fn, key) in FILES.items():
        _, signs, _ = load(script)
        for hf in HTML:
            h = open(os.path.join(ROOT, hf), encoding='utf-8').read()
            a, b = block(h, key)
            try:
                emb = json.loads(h[a:b])
            except Exception:
                emb = None
            if emb is None:
                print(f'{hf}: {script}: embedded block is not plain JSON — this tool cannot maintain it; report it')
                ok = False
            elif emb != signs:
                print(f'{hf}: {script}: embedded copy differs from {fn}')
                ok = False
    print('signs: in sync' if ok else 'signs: OUT OF SYNC')
    return ok


def add(script, key, uname, fields):
    d, signs, emb_key = load(script)
    if key in signs:
        raise SystemExit(f'{key} is already in the {script} sign glossary')
    glyph = unicodedata.lookup(uname)
    entry = {'glyph': glyph}
    entry.update(json.loads(fields))
    signs[key] = entry
    fn = FILES[script][0]
    json.dump(d, open(os.path.join(ROOT, fn), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for hf in HTML:
        p = os.path.join(ROOT, hf)
        h = open(p, encoding='utf-8').read()
        a, b = block(h, emb_key)
        before = h[:a] + h[b:]
        new = fmt(script, signs)
        h2 = h[:a] + new + h[b:]
        a2, b2 = block(h2, emb_key)
        assert h2[:a2] + h2[b2:] == before, 'would change more than the sign block'
        open(p, 'w', encoding='utf-8').write(h2)
    print(f'ADDED {script} {key} = {glyph} ({uname}) to {fn}, index.html, reader.html')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'check':
        sys.exit(0 if check() else 1)
    if a[0] == 'add' and len(a) == 5:
        add(*a[1:])
    else:
        print(__doc__)
        sys.exit(2)

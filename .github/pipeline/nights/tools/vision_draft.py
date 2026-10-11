#!/usr/bin/env python3
"""
vision_draft.py — Google Cloud Vision drafts for the Nights scan (added 2026-10-11).

WHY
    The correction agents start from a machine draft of each line. Tesseract (even fine-tuned)
    gets about half the words right; Cloud Vision, measured on the ten verified pages
    printed pp. 3-12 (2026-10-11), gets about 88 % of words and 95 % of characters right.
    A better draft means less work per line for the two passes and the adjudicator. The
    passes, the adjudication and the gate are unchanged: Vision only replaces the DRAFT.

TWO HALVES
    --fetch   runs on the GitHub Actions runner (the routine's sandbox cannot reach Google).
              Renders each target page at 300 dpi, sends it to Vision (DOCUMENT_TEXT_DETECTION,
              language hint ar) and saves every word with its box to vision/p<ppp>.json.
              Targets: the next AHEAD pages after the last archived page, plus any page listed
              in vision/request.txt. Pages already saved are never re-sent. A monthly page cap
              (vision/_usage.json) keeps it inside Google's free 1,000 pages a month.
    lines_for(page_json, body, shape)
              used by nights_ocr.py --vision: assigns the saved words to the line crops that the
              line detector found, right to left, and applies the mechanical clean-ups below.

KNOWN VISION HABITS (measured) and what is done about them here
    - detaches the conjunction waw ("و اصفر")  -> re-attached (the print attaches it).
    - Persian kaf/ya (ک ی)                      -> ك, and ي (ى word-finally).
    - specks read as w / n / 3                  -> tokens with no Arabic letter are dropped.
    - drops or misreads a word now and then     -> nothing mechanical; that is what the
                                                   correction passes are for.
"""
import argparse, base64, datetime, glob, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
NIGHTS = os.path.dirname(HERE)
VDIR = os.path.join(NIGHTS, 'vision')
LAST_PDF_PAGE = 938          # vol. 1 (plan.md)
AHEAD = 120                  # pages fetched ahead of the transcription (~15 runs of 8)
MONTHLY_CAP = 900            # Google: first 1,000 pages a month free; keep a margin

ARABIC = re.compile(r'[؀-ۿ]')

def chunk_for(page):
    """source/calcutta2-vol1-p<A>-<B>.pdf holding absolute PDF page `page`, and A-1."""
    for f in sorted(glob.glob(os.path.join(NIGHTS, 'source', 'calcutta2-vol1-p*-*.pdf'))):
        a, b = (int(x) for x in re.search(r'p(\d+)-(\d+)\.pdf$', f).groups())
        if a <= page <= b:
            return f, a - 1
    raise SystemExit(f'no source chunk holds PDF page {page}')

def last_archived():
    y = 0
    for f in glob.glob(os.path.join(NIGHTS, 'archive', 'pp*.json')):
        pages = json.load(open(f, encoding='utf-8')).get('pages', '')
        m = re.search(r'PDF pages?\s*(\d+)\s*[-–]\s*(\d+)', pages)
        if m: y = max(y, int(m.group(2)))
    return y

def render_gray(pdf, page_in_pdf, dpi=300):
    import fitz
    pix = fitz.open(pdf)[page_in_pdf - 1].get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
    return pix

def vision(jpeg_bytes, key):
    body = json.dumps({'requests': [{'image': {'content': base64.b64encode(jpeg_bytes).decode()},
                                     'features': [{'type': 'DOCUMENT_TEXT_DETECTION'}],
                                     'imageContext': {'languageHints': ['ar']}}]}).encode()
    req = urllib.request.Request('https://vision.googleapis.com/v1/images:annotate?key=' + key,
                                 data=body, headers={'Content-Type': 'application/json'})
    r = json.load(urllib.request.urlopen(req, timeout=120))['responses'][0]
    if 'error' in r: raise RuntimeError(r['error'])
    return r

def words_of(resp):
    out = []
    fta = resp.get('fullTextAnnotation') or {}
    for p in fta.get('pages', []):
        for b in p['blocks']:
            for pa in b['paragraphs']:
                for w in pa['words']:
                    v = w['boundingBox']['vertices']
                    xs = [q.get('x', 0) for q in v]; ys = [q.get('y', 0) for q in v]
                    t = ''.join(s['text'] for s in w['symbols'])
                    out.append([t, min(xs), min(ys), max(xs), max(ys)])
    return out

def fetch(a):
    key = os.environ.get('GOOGLE_TTS_KEY') or os.environ.get('GOOGLE_VISION_KEY')
    if not key: raise SystemExit('no API key in GOOGLE_TTS_KEY')
    os.makedirs(VDIR, exist_ok=True)
    y = last_archived()
    want = list(range(y + 1, min(LAST_PDF_PAGE, y + AHEAD) + 1))
    req = os.path.join(VDIR, 'request.txt')
    if os.path.exists(req):
        for tok in re.findall(r'\d+(?:-\d+)?', re.sub(r'#.*', '', open(req).read())):
            lo, hi = (int(x) for x in tok.split('-')) if '-' in tok else (int(tok),) * 2
            want += list(range(lo, hi + 1))
    want = sorted({p for p in want if not os.path.exists(os.path.join(VDIR, f'p{p:03d}.json'))})
    usage_f = os.path.join(VDIR, '_usage.json')
    usage = json.load(open(usage_f)) if os.path.exists(usage_f) else {}
    month = datetime.datetime.utcnow().strftime('%Y-%m')
    room = MONTHLY_CAP - usage.get(month, 0)
    if a.limit: room = min(room, a.limit)
    print(f'last archived PDF page {y}; {len(want)} pages lack a Vision draft; room this month {room}')
    done = 0
    for p in want[:max(0, room)]:
        pdf, off = chunk_for(p)
        pix = render_gray(pdf, p - off)
        jpg = pix.tobytes('jpg', jpg_quality=85)
        try:
            r = vision(jpg, key)
        except Exception as e:
            print(f'page {p}: Vision error {e}'); break
        ws = words_of(r)
        json.dump({'page': p, 'w': pix.width, 'h': pix.height, 'dpi': 300,
                   'engine': 'Google Cloud Vision DOCUMENT_TEXT_DETECTION (ar)',
                   'date': datetime.date.today().isoformat(), 'words': ws},
                  open(os.path.join(VDIR, f'p{p:03d}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, separators=(',', ':'))
        done += 1
        print(f'page {p}: {len(ws)} words')
    usage[month] = usage.get(month, 0) + done
    json.dump(usage, open(usage_f, 'w'), indent=1, sort_keys=True)
    print(f'fetched {done} pages; {usage[month]} this month')

# ---- used by nights_ocr.py -------------------------------------------------------------------

def clean_token(t):
    t = t.replace('ک', 'ك')
    if t.endswith('ی'): t = t[:-1] + 'ى'           # Persian ya is dotless at word end
    return t.replace('ی', 'ي')

def tidy(tokens):
    toks = [clean_token(t) for t in tokens if ARABIC.search(t) or t in '()']
    out = []
    for t in toks:
        if out and out[-1] == 'و' and ARABIC.search(t):
            out[-1] = 'و' + t                      # the print attaches the conjunction
        else:
            out.append(t)
    return ' '.join(out)

def load_page(vdir, page):
    f = os.path.join(vdir, f'p{page:03d}.json')
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else None

def lines_for(pj, body, shape, pad=16):
    """Vision words -> one draft string per detected body line (y0, y1) of a page whose
    flattened render has `shape` (h, w). Words are given to the line containing their vertical
    centre (crop padded by `pad` px, as nights_ocr.py crops); a word between crops goes to the
    nearer one if it is within half a pitch, else is dropped (headers, catchwords, specks)."""
    sy = shape[0] / pj['h']; sx = shape[1] / pj['w']
    buckets = [[] for _ in body]
    pitch = (body[-1][0] - body[0][0]) / max(1, len(body) - 1) if len(body) > 1 else 100
    for t, x0, y0, x1, y1 in pj['words']:
        cy = (y0 + y1) / 2 * sy; cx = (x0 + x1) / 2 * sx
        best, dist = None, None
        for i, (a, b) in enumerate(body):
            d = 0 if a - pad <= cy <= b + pad else min(abs(cy - (a - pad)), abs(cy - (b + pad)))
            if dist is None or d < dist: best, dist = i, d
        if best is not None and dist <= pitch / 2:
            buckets[best].append((cx, t))
    return [tidy([t for _, t in sorted(bk, key=lambda z: -z[0])]) for bk in buckets]

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--fetch', action='store_true')
    ap.add_argument('--limit', type=int, default=0, help='at most this many pages this run')
    a = ap.parse_args()
    if a.fetch: fetch(a)
    else: ap.print_help()

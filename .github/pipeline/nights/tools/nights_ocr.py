#!/usr/bin/env python3
"""
nights_ocr.py — OCR draft + line crops for one page-run of Calcutta II (aliflailaorbooko01macn.pdf).

Usage:
    python3 nights_ocr.py --pdf aliflailaorbooko01macn.pdf --pages 19-21 --out run-p19-21 \
        [--tessdata td --model calc] [--expect-lines 23]

For every PDF page it:
  1. renders at 300 dpi and flattens the background (Gaussian-blur divide),
  2. finds the text lines by ink projection, drops the running header (any line that sits
     above the first body line by more than one line-pitch) and checks the inter-line pitch: a dropped
     line shows as a double-pitch gap (a count alone is not enough — verse and heading pages
     legitimately carry fewer than the 23 lines of a full prose page) — this is
     the page-continuity gate from nights-corpus-plan.md, Finding 1: a page that detects
     22 lines is flagged, never silently accepted,
  3. OCRs each body line with Tesseract in raw-line mode (--psm 13) using the fine-tuned
     model (calc.traineddata; falls back to arabest/ara if absent),
  4. writes <out>/pNN/lineLL.png (2x crops for the correction agent), <out>/pNN/draft.json
     ({"line": n, "ocr": "..."}), and <out>/gate.json with the per-page line counts.

The OCR output is a DRAFT (measured ~85–90 % characters, ~50–60 % words exact on the pilot
pages). The correction agent reads each line crop against its draft line and writes the
transcription; see nights-ocr-experiment.md for the prompt and the measured cost.

Requires: pdftoppm (poppler), tesseract 5 with ara/arabest/calc traineddata, opencv, numpy.
"""
import argparse, json, os, subprocess, sys
import numpy as np, cv2

def render(pdf, page, dpi=300):
    """300 dpi grayscale render of one PDF page (1-based). pdftoppm if present, else PyMuPDF."""
    try:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(page), '-l', str(page), '-png',
                        '-singlefile', pdf, f'_pg{page}'], check=True, capture_output=True)
        g = cv2.imread(f'_pg{page}.png', 0); os.remove(f'_pg{page}.png')
        return g
    except (FileNotFoundError, subprocess.CalledProcessError):
        import fitz                                   # pip install pymupdf
        pix = fitz.open(pdf)[page - 1].get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
        return np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width).copy()

def flatten(g):
    bg = cv2.GaussianBlur(g, (0, 0), 25)
    return cv2.normalize(cv2.divide(g, bg, scale=255), None, 0, 255, cv2.NORM_MINMAX)

def find_lines(flat):
    a = flat < 128                       # ink after flattening
    prof = np.convolve(a.sum(1), np.ones(5) / 5, mode='same')
    ink = prof > max(8, prof.max() * 0.04)
    runs, y = [], 0
    while y < len(ink):
        if ink[y]:
            y0 = y
            while y < len(ink) and ink[y]: y += 1
            runs.append([y0, y])            # keep every run; short dot-bands merge below
        else:
            y += 1
    merged = []
    for r in runs:                       # merge dots/diacritic bands into their line
        if merged and r[0] - merged[-1][1] < 18: merged[-1][1] = r[1]
        else: merged.append(r)
    return [tuple(r) for r in merged if r[1] - r[0] > 34]   # body lines are ~45–60 px at 300 dpi

def split_header(lines):
    """Calcutta II body lines sit on a regular pitch (~103 px at 300 dpi); the running
    header sits well above the first body line. Return (header_lines, body_lines)."""
    if len(lines) < 3: return [], lines
    pitches = [b[0] - a[0] for a, b in zip(lines, lines[1:])]
    pitch = float(np.median(pitches))
    k = 0
    while k < len(lines) - 1 and (lines[k + 1][0] - lines[k][0]) > pitch * 1.25: k += 1
    return lines[:k], lines[k:]

def ocr_line(png, tessdata, model):
    """Tesseract raw-line read; empty string if tesseract is not installed (the correction
    agent then transcribes from the crop alone — slower, still correct)."""
    try:
        r = subprocess.run(['tesseract', png, '-', '-l', model, '--psm', '13',
                            '--tessdata-dir', tessdata], capture_output=True, text=True)
        return r.stdout.strip()
    except FileNotFoundError:
        return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', required=True); ap.add_argument('--pages', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--tessdata', default='td')
    ap.add_argument('--model', default='calc'); ap.add_argument('--expect-lines', type=int, default=23)
    ap.add_argument('--keep-ocr-crops', action='store_true', help='also keep the 1x crops (ocrNN.png) for model retraining')
    ap.add_argument('--offset', type=int, default=0, help='absolute PDF page number of page 1 of --pdf, minus 1 (chunked scans)')
    a = ap.parse_args()
    p0, p1 = (int(x) for x in a.pages.split('-')) if '-' in a.pages else (int(a.pages),) * 2
    os.makedirs(a.out, exist_ok=True)
    gate = {}
    for page in range(p0, p1 + 1):
        flat = flatten(render(a.pdf, page))
        header, body = split_header(find_lines(flat))
        page = page + a.offset            # absolute page number from here on
        d = os.path.join(a.out, f'p{page:03d}'); os.makedirs(d, exist_ok=True)
        draft = []
        for i, (y0, y1) in enumerate(body, 1):
            c = flat[max(0, y0 - 16):min(flat.shape[0], y1 + 16), :]
            c = cv2.copyMakeBorder(c, 30, 30, 40, 40, cv2.BORDER_CONSTANT, value=255)
            one = os.path.join(d, f'_ocr{i:02d}.png'); cv2.imwrite(one, c)
            big = cv2.resize(c, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(os.path.join(d, f'line{i:02d}.png'), big)
            draft.append({'line': i, 'ocr': ocr_line(one, a.tessdata, a.model)})
            if a.keep_ocr_crops: os.rename(one, os.path.join(d, f'ocr{i:02d}.png'))
            else: os.remove(one)
        json.dump(draft, open(os.path.join(d, 'draft.json'), 'w'), ensure_ascii=False, indent=1)
        # Safety net for the correction agent: the whole text block in three overlapping bands
        # at 1.3x, so a line the detector merged or dropped (verse pages especially) is still
        # seen. The agent transcribes every printed line, crops or no crops.
        top = max(0, (header[-1][1] if header else body[0][0]) - 40) if body else 0
        bot = min(flat.shape[0], body[-1][1] + 40) if body else flat.shape[0]
        H = bot - top; step = H / 3
        for k in range(3):
            y0 = int(top + k * step - 60); y1 = int(top + (k + 1) * step + 60)
            band = flat[max(0, y0):min(flat.shape[0], y1), :]
            cv2.imwrite(os.path.join(d, f'band{k + 1}.png'),
                        cv2.resize(band, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_CUBIC))
        # Gate: a dropped line shows as an inter-line gap of ~2x the page's pitch. Pages with
        # verse or a section heading legitimately carry fewer than 23 lines (p. 6 has 16), so
        # the count is reported but only a double-pitch gap fails the page.
        starts = [y0 for y0, _ in body]
        gaps = [b - a_ for a_, b in zip(starts, starts[1:])]
        pitch = float(np.median(gaps)) if gaps else 0
        big = [i + 1 for i, g in enumerate(gaps) if pitch and g > pitch * 1.75]
        ok = not big and len(body) <= a.expect_lines
        gate[page] = {'header_lines': len(header), 'body_lines': len(body), 'pitch': pitch,
                      'suspect_gap_after_line': big, 'ok': ok}
        print(f'page {page}: header {len(header)}, body {len(body)}, pitch {pitch:.0f}',
              '' if ok else f'  <-- GATE: double-pitch gap after line(s) {big} — a line may be missing')
    json.dump(gate, open(os.path.join(a.out, 'gate.json'), 'w'), indent=1)
    if not all(v['ok'] for v in gate.values()): sys.exit(2)

if __name__ == '__main__':
    main()

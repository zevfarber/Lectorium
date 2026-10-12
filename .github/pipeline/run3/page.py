#!/usr/bin/env python3
"""Render one page (or a region of it) of a scanned PDF to a PNG you can look at.

    python3 page.py <pdf> <page> [--zoom Z] [--clip x0,y0,x1,y1] [--out file.png]

<page> is 1-based. --clip is in PDF points of the unzoomed page (print the page size with --info).
Needs PyMuPDF: `pip install pymupdf` (it installs from PyPI)."""
import argparse, os, sys
try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit('PyMuPDF is missing: run  pip install pymupdf  (add --break-system-packages if pip refuses)')

ap = argparse.ArgumentParser()
ap.add_argument('pdf')
ap.add_argument('page', type=int)
ap.add_argument('--zoom', type=float, default=2.0)
ap.add_argument('--clip')
ap.add_argument('--out')
ap.add_argument('--info', action='store_true')
a = ap.parse_args()
d = pymupdf.open(a.pdf)
p = d[a.page - 1]
if a.info:
    print(f'{d.page_count} pages; page {a.page} is {p.rect.width:.0f} × {p.rect.height:.0f} points')
    sys.exit(0)
clip = pymupdf.Rect(*map(float, a.clip.split(','))) if a.clip else None
pix = p.get_pixmap(matrix=pymupdf.Matrix(a.zoom, a.zoom), clip=clip)
out = a.out or f'/tmp/page-{os.path.basename(a.pdf).rsplit(".", 1)[0]}-{a.page}' + (f'-{a.clip.replace(",", "_")}' if a.clip else '') + '.png'
pix.save(out)
print(out)

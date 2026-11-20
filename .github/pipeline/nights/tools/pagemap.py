"""pagemap.py — the scan-to-printed page map for both volumes (added 2026-11-20, volume 2).

Printed page = absolute PDF page - 22 throughout. Volume 2's printed page n is archived as
page 910 + n (so vol. 2 p. 5 is P915), at absolute PDF page 932 + n. source/pagemap.json lists the
PDF pages that are never transcribed: the volume-2 title leaves, and placeholder pages standing
in for pages missing from the only scan."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
NIGHTS = os.path.dirname(HERE)
_PM = json.load(open(os.path.join(NIGHTS, 'source', 'pagemap.json'), encoding='utf-8'))
EXCLUDE = {int(k): v for k, v in _PM['exclude_pdf'].items()}
LAST_PDF = _PM['last_pdf']
PDF_TO_PRINTED = -22
VOL2_OFFSET = 910
VOL1_LAST_PDF = 932


def excluded(pdf_page):
    return pdf_page in EXCLUDE


def missing_printed():
    """Archive page numbers (910+n) of the volume-2 pages absent from the scan."""
    return {VOL2_OFFSET + n for n in _PM['missing_printed_vol2']}


def volume(pdf_page):
    return 1 if pdf_page <= VOL1_LAST_PDF else 2


def header_number(archive_page):
    """The page number the print itself shows at the top of this archived page."""
    return archive_page - VOL2_OFFSET if archive_page > VOL2_OFFSET else archive_page


def archive_key(name):
    """Sort key for archive/pp<A>-<B>.json in printed order (numeric: pp1001 after pp999)."""
    m = re.match(r'pp(\d+)', name)
    return (int(m.group(1)) if m else -1, name)

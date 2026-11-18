"""Haug & West 1872, the printed Pahlavi: find the lines and word shapes on a page image and cut word images.
numpy + Pillow only (pip install numpy pillow). Everything here is deterministic for a given page file, so
the (line, shape) numbers a firing reads off a sheet stay valid when the part is built later."""
import os, json
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(HERE, 'source', 'pages')
UP, DOWN = 74, 54            # rows kept above / below a line's baseline band


def page(leaf):
    return np.array(Image.open(os.path.join(PAGES, f'n{leaf}.jpg')).convert('L')).astype(float)


def _peaks(k, distance, height):
    idx = [i for i in range(1, len(k) - 1) if k[i] >= height and k[i] >= k[i - 1] and k[i] > k[i + 1]]
    idx.sort(key=lambda i: -k[i])
    keep = []
    for i in idx:
        if all(abs(i - j) >= distance for j in keep):
            keep.append(i)
    return sorted(keep)


def detect(leaf, a=None):
    """-> {'x0': int, 'lines': [{'base': y, 'blocks': [[xa, xb], ...]}]}; blocks are in READING order
    (right to left), x measured from x0. Every printed line on the page is returned — Pahlavi, the Roman
    reading under it, and the footnotes; the cut file says which lines are the Pahlavi of a part."""
    a = page(leaf) if a is None else a
    h, w = a.shape
    x0, x1 = int(.03 * w), int(.975 * w)
    ya, yb = int(.04 * h), int(.94 * h)
    ink = (a[ya:yb, x0:x1] < 120).sum(axis=1).astype(float)
    k = np.convolve(ink, np.ones(14), 'same')
    lines = []
    for p in _peaks(k, 80, 0.25 * k.max()):
        base = ya + int(p)
        s, e = base - UP, base + DOWN
        if s < 0 or e > h:
            continue
        cols = (a[s + 18:e - 14, x0:x1] < 120).sum(axis=0) >= 2
        blocks, st, gap, last = [], None, 0, 0
        for x, c in enumerate(cols):
            if c:
                if st is None:
                    st = x
                last, gap = x, 0
            else:
                gap += 1
                if st is not None and gap > 16:
                    blocks.append([st, last])
                    st = None
        if st is not None:
            blocks.append([st, last])
        blocks = [b for b in blocks if b[1] - b[0] > 6]
        lines.append({'base': base, 'blocks': list(reversed(blocks))})
    return {'x0': x0, 'lines': lines}


def sheets(leaf, outdir, per=9):
    """Numbered sheets for a firing to read: every line as a strip, its word shapes boxed and numbered from the
    right (0 = first in reading order), the line number at the left edge. Returns the files written."""
    a = page(leaf)
    d = detect(leaf, a)
    im = Image.fromarray(a.astype('uint8'))
    x0 = d['x0']
    x1 = int(.975 * a.shape[1])
    tiles = []
    for li, L in enumerate(d['lines']):
        s, e = L['base'] - UP, L['base'] + DOWN
        t = im.crop((x0, s, x1, e)).convert('RGB')
        dr = ImageDraw.Draw(t)
        for j, b in enumerate(L['blocks']):
            dr.rectangle((b[0] - 3, 1, b[1] + 3, e - s - 2), outline=(255, 0, 0))
            dr.text((b[0] + 1, 2), str(j), fill=(0, 0, 255))
        dr.text((2, 58), f'L{li}', fill=(0, 140, 0))
        tiles.append(t)
    os.makedirs(outdir, exist_ok=True)
    out = []
    for k in range(0, len(tiles), per):
        grp = tiles[k:k + per]
        H = sum(t.size[1] for t in grp)
        sh = Image.new('RGB', (grp[0].size[0], H), 'white')
        y = 0
        for t in grp:
            sh.paste(t, (0, y))
            y += t.size[1]
        sh = sh.resize((1500, int(H * 1500 / sh.size[0])))
        p = os.path.join(outdir, f'n{leaf}-{chr(97 + k // per)}.png')
        sh.save(p)
        out.append(p)
    return out, [len(L['blocks']) for L in d['lines']]


def _components(mask):
    """4-connected components of a small boolean array -> list of index arrays (ys, xs)."""
    H, W = mask.shape
    seen = np.zeros_like(mask, bool)
    out = []
    for y0 in range(H):
        for x0 in range(W):
            if mask[y0, x0] and not seen[y0, x0]:
                stack, ys, xs = [(y0, x0)], [], []
                seen[y0, x0] = True
                while stack:
                    y, x = stack.pop()
                    ys.append(y)
                    xs.append(x)
                    for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= yy < H and 0 <= xx < W and mask[yy, xx] and not seen[yy, xx]:
                            seen[yy, xx] = True
                            stack.append((yy, xx))
                out.append((np.array(ys), np.array(xs)))
    return out


def cut(a, x0, base, b):
    """One word shape -> RGBA image (dark ink on transparent), or None if nothing is left after cleaning."""
    top, bot = base - UP, base + DOWN
    c = a[top:bot, x0 + b[0] - 4:x0 + b[1] + 5]
    alpha = np.clip((165 - c) / 85, 0, 1)
    alpha[alpha < 0.25] = 0
    for ys, xs in _components(alpha > 0):
        if ((ys.min() == 0 or ys.max() == alpha.shape[0] - 1) and (ys.max() - ys.min()) < 34) or len(ys) < 6:
            alpha[ys, xs] = 0            # a stroke of the line above or below, or a speck
    if alpha.sum() < 20:
        return None
    rgba = np.zeros(c.shape + (4,), 'uint8')
    rgba[..., 3] = (alpha * 255).astype('uint8')
    rgba[..., :3] = 30
    img = Image.fromarray(rgba, 'RGBA')
    img = img.resize((max(1, img.size[0] * 2 // 3), img.size[1] * 2 // 3), Image.LANCZOS)
    arr = np.array(img)
    arr[..., 3] = (np.round(arr[..., 3] / 255 * 7) / 7 * 255).astype('uint8')
    arr[..., :3] = 30
    return Image.fromarray(arr, 'RGBA')

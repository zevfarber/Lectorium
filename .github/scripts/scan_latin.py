#!/usr/bin/env python3
"""Latin dactylic hexameter scanner for Lectorium (standard library only). Written 2026-10-04.

Fills each unit's `sc` (the reader's Scansion overlay, same format as the Odyssey's): one string
per reader word token; each syllable = optional foot digit, letters, mark (– long, ⏑ short,
× final); trailing ‖ = main caesura; an elided final syllable is left unmarked.

Method: every line is fitted to the hexameter by a cost-minimising dynamic programme, as in the
Greek scanner (.github/pipeline/odyssey/scan_hexameter.py). Latin spelling shows no vowel length,
so a vowel's length is either fixed by position (two consonants follow, across word boundaries;
x and z count double; an i between vowels is a double consonant), by being a diphthong (ae oe au)
or a vowel before a vowel (short), or left open and settled by the metre, with small costs from
common word endings (-ās -ōs -ēs long, final -e short, final -ī -ō long ...). Elision is the
default before a vowel or h; synizesis (deinde, Lāvīnia) is available at a cost. A line that
fits no hexameter is reported UNRESOLVED and its unit gets no `sc`.

usage: python3 scan_latin.py file.json [...] [--write] [--report out.txt]
"""
import sys, re, json, itertools, argparse, unicodedata as U, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wordre import WORD_RE

LONG, SHORT, ANC, CAES = '–', '⏑', '×', '‖'
VOW = set('aeiouy')
MUTA, LIQ = set('bcdgptf'), set('lr')
DIPH = {'ae', 'oe', 'au'}
SYNIZ_FREE = {'heu', 'eheu', 'neu', 'seu', 'ceu', 'huic', 'cui', 'dein', 'deinde', 'proinde', 'proin',
              'deinceps', 'ei', 'hei', 'deest', 'deerat', 'deesse', 'dehinc'}
SHORT_FINAL_I = {'mihi', 'tibi', 'sibi', 'ubi', 'ibi', 'nisi', 'quasi', 'ubique'}
SHORT_FINAL_O = {'ego', 'modo', 'cito', 'duo', 'homo', 'quomodo', 'nescio', 'immo', 'octo', 'ambo'}


def segment(word, force_j=(), split=(), vowel_i=()):
    """-> list of items. ('V', text, base, diph) or ('C', text, weight). weight: x/z/intervocalic i = 2,
    h = 0, qu/gu = 1. `text` slices concatenate back to the word exactly."""
    w = word
    lw = U.normalize('NFD', w.lower())
    # work on characters of the original word; diaeresis marks a separate vowel
    chars = list(w)
    base = [U.normalize('NFD', c.lower())[0] for c in chars]
    diaer = ['̈' in U.normalize('NFD', c) for c in chars]
    out, i, n = [], 0, len(chars)
    def isv(k): return 0 <= k < n and base[k] in VOW
    while i < n:
        b = base[i]
        if b == 'q' and i + 1 < n and base[i + 1] == 'u':
            out.append(('C', w[i:i + 2], 1)); i += 2; continue
        if b == 'g' and i + 1 < n and base[i + 1] == 'u' and i > 0 and base[i - 1] == 'n' and isv(i + 2):
            out.append(('C', w[i:i + 2], 1)); i += 2; continue
        if b in VOW:
            # consonantal i: word-initial before a vowel, or between two vowels
            if b == 'i' and not diaer[i] and isv(i + 1) and (i == 0 or isv(i - 1)) and i not in vowel_i:
                out.append(('C', w[i], 1 if i == 0 else 2)); i += 1; continue
            if i in force_j:                       # consonantal i after a consonant (Lāvīnja, ārjete)
                out.append(('C', w[i], 1)); i += 1; continue
            if i + 1 < n and (b + base[i + 1]) in DIPH and not diaer[i + 1] and i not in split:
                out.append(('V', w[i:i + 2], b + base[i + 1], True, False)); i += 2; continue
            # a Greek vowel before a vowel (aër, Pēnēia) may be long: free when this reading was chosen
            free = (i in split) or (i + 1 in vowel_i)
            out.append(('V', w[i], b, False, free)); i += 1; continue
        if b in 'ptcr' and i + 1 < n and base[i + 1] == 'h':      # ph th ch rh: one consonant
            out.append(('C', w[i:i + 2], 1)); i += 2; continue
        if b == 'h':
            out.append(('C', w[i], 0)); i += 1; continue
        if b in 'xz':
            out.append(('C', w[i], 2)); i += 1; continue
        if b.isalpha():
            out.append(('C', w[i], 1)); i += 1; continue
        out.append(('C', w[i], 0)); i += 1          # hyphen etc.: no weight
    return out


def final_costs(lw, nuc_is_last, cons_after_in_word):
    """(cost_long, cost_short) for a vowel from word-ending knowledge; open vowels elsewhere: (0, 0)."""
    if not nuc_is_last:
        return (0.0, 0.0)
    tail = cons_after_in_word
    v = lw[-1] if not tail else lw[-(len(tail) + 1)]
    if tail == '':
        if v == 'a': return (0.0, 0.0)
        if v == 'e': return (0.6, 0.0)
        if v == 'i': return (0.0, 0.8) if lw not in SHORT_FINAL_I else (0.6, 0.0)
        if v == 'o': return (0.0, 0.6) if lw not in SHORT_FINAL_O else (0.4, 0.0)
        if v == 'u': return (0.0, 0.8)
        return (0.0, 0.0)
    if tail == 's':
        if v in 'aoe': return (0.0, 1.0) if lw not in ('es', 'potes', 'ades') else (0.8, 0.0)
        if v == 'u': return (0.8, 0.0)
        return (0.0, 0.0)
    if tail == 'm':
        return (1.0, 0.0)
    return (0.3, 0.0)


def j_candidates(word):
    """positions of an i after a consonant and before a vowel, inside the word (may be read as j)"""
    b = [U.normalize('NFD', c.lower())[0] for c in word]
    return [i for i in range(1, len(b) - 1) if b[i] == 'i' and b[i - 1] not in VOW and b[i - 1].isalpha()
            and b[i + 1] in VOW and b[i - 1] not in 'qh']


def split_candidates(word):
    """diphthong positions that may be two vowels (aër, Danaë, Phaëthon, Peneïa)"""
    b = [U.normalize('NFD', c.lower())[0] for c in word]
    return [i for i in range(len(b) - 1) if (b[i] + b[i + 1]) in ('ae', 'oe')]


def vowel_i_candidates(word):
    """an i between vowels that may be a vowel (Greek names: Peneia, Achaia)"""
    b = [U.normalize('NFD', c.lower())[0] for c in word]
    return [i for i in range(1, len(b) - 1) if b[i] == 'i' and b[i - 1] in VOW and b[i + 1] in VOW]


def line_nuclei(words, force=None):
    """Flatten a line into nuclei with their options. Returns list of dicts."""
    force = force or {}
    segs = [segment(w, force.get(('j', wi), ()), force.get(('s', wi), ()), force.get(('v', wi), ()))
            for wi, w in enumerate(words)]
    nuc = []
    for wi, sg in enumerate(segs):
        vpos = [k for k, it in enumerate(sg) if it[0] == 'V']
        lw = U.normalize('NFD', words[wi].lower())
        lw = ''.join(c for c in lw if not U.combining(c))
        for j, k in enumerate(vpos):
            last = (j == len(vpos) - 1)
            tail_cons = ''.join(it[1] for it in sg[k + 1:] if it[0] == 'C').lower() if last else ''
            nuc.append({'w': wi, 'k': k, 'item': sg[k], 'last': last, 'first': j == 0,
                        'lw': lw, 'tail': tail_cons})
    # following consonants (to the next nucleus, across words) and elidability
    for idx, nu in enumerate(nuc):
        wi, k = nu['w'], nu['k']
        cons, w2, k2 = [], wi, k + 1
        while True:
            sg = segs[w2]
            while k2 < len(sg) and sg[k2][0] == 'C':
                cons.append((sg[k2], w2)); k2 += 1
            if k2 < len(sg) or w2 + 1 >= len(segs):
                break
            w2 += 1; k2 = 0
        weight = sum(c[0][2] for c in cons)
        real = [c for c in cons if c[0][2] > 0]
        mcl = (len(real) == 2 and real[0][1] == real[1][1]
               and real[0][0][1].lower()[0] in MUTA and real[1][0][1].lower() in LIQ and weight == 2)
        nu['weight'] = weight
        nu['mcl'] = mcl
        nu['mcl_next'] = mcl and real[0][1] != wi        # both consonants open the next word
        nu['next_vowel_same_word'] = (weight == 0 and not nu['last'])
        # elision: last nucleus of a word, word ends in vowel or vowel+m, next word starts with vowel/h
        nu['elidable'] = False
        if nu['last'] and wi + 1 < len(words):
            tail = nu['tail']
            nxt = segs[wi + 1]
            starts_v = nxt and (nxt[0][0] == 'V' or (nxt[0][1].lower() == 'h' and len(nxt) > 1 and nxt[1][0] == 'V'))
            if tail in ('', 'm') and starts_v:
                nu['elidable'] = True
        nu['line_final'] = (idx == len(nuc) - 1)
    for idx, nu in enumerate(nuc):
        it = nu['item']
        if it[3]:                                   # diphthong
            opts = {LONG: 0.0}
        elif nu['next_vowel_same_word'] and it[4]:   # Greek vowel before vowel (aër, Pēnēia)
            opts = {LONG: 0.0, SHORT: 0.5}
        elif nu['next_vowel_same_word']:             # vowel before vowel: short
            opts = {SHORT: 0.0, LONG: 2.0}
        elif nu['weight'] >= 2 and not nu['mcl']:     # long by position
            opts = {LONG: 0.0}
        else:
            cl, cs = final_costs(nu['lw'], nu['last'], nu['tail'])
            if nu['mcl']:
                cl = min(cl, 0.5 if nu['mcl_next'] else 0.2)
            opts = {LONG: cl, SHORT: cs}
        nu['opts'] = opts
        # synizesis with the next nucleus in the same word
        nu['syn'] = None
        if idx + 1 < len(nuc) and nuc[idx + 1]['w'] == nu['w'] and nu['next_vowel_same_word']:
            nu['syn'] = 0.0 if nu['lw'] in SYNIZ_FREE else 1.5
    return segs, nuc


def templates():
    for feet in itertools.product('DS', repeat=5):
        cost = 0.0 if feet[4] == 'D' else 2.0
        t = []
        for f in feet:
            t += [LONG, SHORT, SHORT] if f == 'D' else [LONG, LONG]
        t += [LONG, ANC]
        yield feet, t, cost


def fit(nuc):
    """Best (cost, feet, assignment) where assignment[i] = ('el',) | ('syl', mark, slot) | ('syn', mark, slot) | ('in',)"""
    best = None
    N = len(nuc)
    for feet, tpl, tcost in templates():
        T = len(tpl)
        INF = float('inf')
        dp = [[INF] * (T + 1) for _ in range(N + 1)]
        bp = [[None] * (T + 1) for _ in range(N + 1)]
        dp[0][0] = tcost
        for i in range(N):
            nu = nuc[i]
            for j in range(T + 1):
                c0 = dp[i][j]
                if c0 == INF:
                    continue
                if nu['elidable']:
                    if c0 < dp[i + 1][j]:
                        dp[i + 1][j] = c0; bp[i + 1][j] = (i, j, ('el',))
                    hiatus = 3.0
                else:
                    hiatus = 0.0
                if j < T:
                    want = tpl[j]
                    for mark, c in nu['opts'].items():
                        if want == ANC or want == mark:
                            cc = c0 + c + hiatus
                            m = ANC if want == ANC else mark
                            if cc < dp[i + 1][j + 1]:
                                dp[i + 1][j + 1] = cc; bp[i + 1][j + 1] = (i, j, ('syl', m, j))
                    if nu['syn'] is not None and i + 1 < N and want in (LONG, ANC):
                        cc = c0 + nu['syn'] + hiatus
                        if cc < dp[i + 2][j + 1]:
                            dp[i + 2][j + 1] = cc; bp[i + 2][j + 1] = (i, j, ('syn', ANC if want == ANC else LONG, j))
        if dp[N][T] < INF and (best is None or dp[N][T] < best[0] - 1e-9):
            assign = [None] * N; i, j = N, T
            while i > 0:
                pi, pj, act = bp[i][j]
                assign[pi] = act
                if act[0] == 'syn':
                    assign[pi + 1] = ('in',)
                i, j = pi, pj
            best = (dp[N][T], feet, assign, tpl)
    return best


def foot_starts(feet):
    s, out = 0, []
    for f in feet:
        out.append(s); s += 3 if f == 'D' else 2
    out.append(s)
    return out


def render(words, segs, nuc, best):
    cost, feet, assign, tpl = best
    starts = foot_starts(feet)
    slot_foot = {s: k + 1 for k, s in enumerate(starts)}
    # word -> list of (nucleus idx)
    by_word = {}
    for idx, nu in enumerate(nuc):
        by_word.setdefault(nu['w'], []).append(idx)
    # caesura: word whose last pronounced syllable occupies a given slot, with no elision at its end
    last_slot = {}
    for wi, idxs in by_word.items():
        a = assign[idxs[-1]]
        if a[0] in ('syl', 'syn'):
            last_slot[wi] = a[2]
    caes = None
    cand = [starts[2]]                                   # penthemimeral: after first syllable of foot 3
    cand2 = [starts[3]]                                  # hephthemimeral
    cand3 = [starts[2] + 1] if feet[2] == 'D' else []    # trochaic third
    for group in (cand, cand2, cand3):
        for wi, s in last_slot.items():
            fused = wi > 0 and len(by_word.get(wi, [])) == 1 and by_word.get(wi - 1) and \
                assign[by_word[wi - 1][-1]][0] == 'el'
            if s in group and wi + 1 < len(words) and not fused:
                caes = wi; break
        if caes is not None:
            break
    out = []
    for wi, word in enumerate(words):
        sg = segs[wi]
        vpos = [k for k, it in enumerate(sg) if it[0] == 'V']
        if not vpos:
            out.append(word); continue
        # syllable boundaries within the word: index in sg where each syllable starts
        bounds = [0]
        for a, b in zip(vpos, vpos[1:]):
            mid = [k for k in range(a + 1, b)]
            if not mid:
                bounds.append(b); continue
            cons = [sg[k] for k in mid]
            if len(mid) >= 2 and cons[-2][1].lower()[:1] in MUTA and cons[-1][1].lower() in LIQ:
                bounds.append(mid[-2])
            else:
                bounds.append(mid[-1])
        bounds.append(len(sg))
        idxs = by_word.get(wi, [])
        pieces = []
        for s_i in range(len(vpos)):
            text = ''.join(it[1] for it in sg[bounds[s_i]:bounds[s_i + 1]])
            a = assign[idxs[s_i]]
            if a[0] == 'el':
                pieces.append(text)
            elif a[0] == 'in':
                pieces[-1] = (pieces[-1][0], pieces[-1][1] + text, pieces[-1][2]) if isinstance(pieces[-1], tuple) else pieces[-1] + text
            else:
                pieces.append((str(slot_foot.get(a[2], '')), text, a[1]))
        s = ''
        for p in pieces:
            s += (p[0] + p[1] + p[2]) if isinstance(p, tuple) else p
        if wi == caes:
            s += CAES
        out.append(s)
    return out


J_COST = 1.5
VAR_COST = {'j': 1.5, 's': 1.2, 'v': 1.0}


def scan_line(line):
    words = WORD_RE.findall(line)
    cands = ([('j', wi, p) for wi, w in enumerate(words) for p in j_candidates(w)] +
             [('s', wi, p) for wi, w in enumerate(words) for p in split_candidates(w)] +
             [('v', wi, p) for wi, w in enumerate(words) for p in vowel_i_candidates(w)])
    variants = [()] + [(c,) for c in cands] + list(itertools.combinations(cands, 2))
    top = None
    for var in variants:
        force = {}
        for kind, wi, p in var:
            force.setdefault((kind, wi), set()).add(p)
        segs, nuc = line_nuclei(words, force)
        best = fit(nuc)
        if best:
            total = best[0] + sum(VAR_COST[k] for k, _, _ in var)
            if top is None or total < top[0] - 1e-9:
                top = (total, segs, nuc, best)
    if not top:
        return words, None, None
    total, segs, nuc, best = top
    best = (total,) + best[1:]
    return words, render(words, segs, nuc, best), best


def scan_story(story):
    """Rebuild verse lines across units (a unit may start mid-line), scan, assign sc back."""
    lines = []          # list of (text, [(unit_idx, ntokens)])
    prev_last = None
    for ui, s in enumerate(story['sentences']):
        segs_ = s['t'].split('\n')
        ln = s.get('ln')
        for k, seg in enumerate(segs_):
            cont = (k == 0 and ln is not None and prev_last is not None and ln == prev_last and lines)
            ntok = len(WORD_RE.findall(seg))
            if cont:
                lines[-1][0] += ' ' + seg; lines[-1][1].append((ui, ntok))
            else:
                lines.append([seg, [(ui, ntok)]])
        prev_last = (ln + len(segs_) - 1) if ln is not None else None
    per_unit = {ui: [] for ui in range(len(story['sentences']))}
    bad_units, report = set(), []
    for text, parts in lines:
        words, sc, best = scan_line(text)
        if sc is None:
            report.append('UNRESOLVED: ' + text)
            for ui, _ in parts: bad_units.add(ui)
            sc = [''] * len(words)
        elif best[0] >= 2.0:
            report.append('COSTLY %.1f: %s' % (best[0], ' '.join(sc)))
        pos = 0
        for ui, ntok in parts:
            per_unit[ui] += sc[pos:pos + ntok]; pos += ntok
    n_ok = 0
    for ui, s in enumerate(story['sentences']):
        if ui in bad_units or not s.get('v'):
            s.pop('sc', None); continue
        toks = WORD_RE.findall(s['t'])
        sc = per_unit[ui]
        if len(sc) != len(toks):
            s.pop('sc', None); report.append('MISMATCH unit %d' % ui); continue
        s['sc'] = sc; n_ok += 1
    return n_ok, len(lines), report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+'); ap.add_argument('--write', action='store_true')
    ap.add_argument('--report')
    a = ap.parse_args()
    tot_u = tot_ok = tot_l = 0; rep = []
    for f in a.files:
        raw = open(f, encoding='utf-8').read()
        story = json.loads(raw)
        if story.get('language') != 'Latin':
            continue
        ok, nl, r = scan_story(story)
        tot_ok += ok; tot_u += len(story['sentences']); tot_l += nl
        rep += ['## ' + f] + r
        if a.write:
            indent = 1 if raw.startswith('{\n ') and not raw.startswith('{\n  ') else 2
            open(f, 'w', encoding='utf-8').write(json.dumps(story, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else ''))
    unres = sum(1 for x in rep if x.startswith('UNRESOLVED'))
    costly = sum(1 for x in rep if x.startswith('COSTLY'))
    print('units with scansion: %d of %d; lines: %d; unresolved lines: %d; costly fits: %d' % (tot_ok, tot_u, tot_l, unres, costly))
    if a.report:
        open(a.report, 'w', encoding='utf-8').write('\n'.join(rep) + '\n')


if __name__ == '__main__':
    main()

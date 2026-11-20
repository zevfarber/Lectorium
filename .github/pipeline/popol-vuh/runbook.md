# Popol Vuh — what one firing does

The Popol Vuh sits on the shared text pipeline's queue (`../queue.txt`, from 2026-11-20) but is built on
the Run 3 machinery, because its text has to be read from manuscript images first. So:

**Follow `../run3/RUNBOOK.md` exactly, with one change: wherever it says `R3 next`, run
`python3 ../run3/r3.py next main`** (it reads `queue.txt`). Everything else — claims, the two actions,
the three roles and their models, build, validate, publish, "If something is wrong" — is as written there.
Run every command from this folder. Read `conventions.md` before anything else.

Every part takes two firings: ACTION establish (the text), then ACTION draft. A part begins exactly where
the previous part's established text ends, so parts go strictly in order.

## ACTION establish
`python3 ../run3/r3.py establish-packet popol-vuh <id>` writes `drafts/<id>/establish.md`: the start point,
the images (`source/pages/i<NNNN>.jpg`) and the procedure. The image decides every letter; Brasseur 1861
(`source/raw/brasseur1861_djvu.txt`) only chooses between letters where Ximénez's hand is ambiguous. Write
`source/established/<id>.txt` with its three header lines (`# name:`, `# title:`, `# fols:`) and pin it.
`pin` refuses a file with a missing header line, digits, an apostrophe or unbalanced quotes; it also copies
the name and folios into `parts.json`. A page or spot that cannot be read: README rule 7 (leave the smallest
gap, note it, carry on).

## ACTION draft
Packet: the established paragraphs and the establishment log; `novel-forms.json` / `known-forms.json`.

**Drafter** gets `conventions.md`, `packet.md`, `../../../popol-vuh-001.json` (the model: shape, register,
note density) and the published parts before this one for consistency of renderings. Writes
`drafts/<id>/units.json`:
`{"about": "<one paragraph, plain, on what happens in this part — as the pilot's about>",
  "sentences": [{"t": "<cut by script from the packet>", "mt": ["<modern ALMG spelling of word 1>", …],
  "l": "…", "i": "…", "n": "…"}]}`.
`mt` has exactly one entry per word of `t` as the reader splits it (`../../scripts/wordre.py` WORD_RE),
following "The modern-letters toggle" in conventions.md. The build sets `p`, title, titleEn, part and source.

**Reviewer** — two passes, as RUNBOOK.md says, plus: every `mt` against its manuscript word (letters
respelled, nothing restored unless certain), the house renderings table, couplets kept as couplets in `i`.

**Glosser** (Sonnet): every novel form, key = the lowercased manuscript form as the reader tokenizes it,
value `modern form — meaning; morphology` (the format of `popol-vuh-glossary.json`); `__broaden__` for
known forms used in a new sense.

Build: `python3 ../run3/r3.py build popol-vuh <id>`, then `validate`. No audio (no voice chosen yet).
Copy any new house rendering into conventions.md's table.

When the last part (popol-vuh-039, ending with the lords' genealogy on image 0124) is published, `R3 next
main` answers COMPLETE: run `python3 ../run3/r3.py done popol-vuh`, commit, push; the next firing moves on
to the next work in `queue.txt` by itself.

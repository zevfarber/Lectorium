# The Tibetan Book of the Dead — what one firing does

The Bardo Thödröl sits on the shared text pipeline's queue (`../queue.txt`, from 2026-11-20) but is built
on the Run 3 machinery, because its text has to be read from blockprint images first. So:

**Follow `../run3/RUNBOOK.md` exactly, with one change: wherever it says `R3 next`, run
`python3 ../run3/r3.py next main`** (it reads `queue.txt`). Everything else — claims, the two actions,
the three roles and their models, build, validate, publish, "If something is wrong" — is as written there.
Run every command from this folder. Read `conventions.md` before anything else.
**First, `pip install pyewts`** (`python3 -c "import pyewts"` to check): `tib.py` needs it for the letters
and the pronunciation line, and the build cannot run without it.

Every part takes two firings: ACTION establish (the print, line by line), then ACTION draft. A part begins
exactly where the previous part's established text ends, so parts go strictly in order. Two texts are on
this list: kha (pp. 18–80, the peaceful deities; the pilot was its pp. 9–17) and ga (pp. 81–121, the
wrathful deities, beginning with its title leaf).

## ACTION establish
`python3 ../run3/r3.py establish-packet bardo-thodol <id>` writes `drafts/<id>/establish.md`: the start
point, the page images (`source/pages/n<leaf>.jpg`, page p = leaf n(p+1)) and the procedure. The image
decides every letter. Write `source/established/<id>.txt` in the format of `source/w23710-pp09-17.txt`
(one print line per line, `{page}` markers, `[?]` on doubtful syllables) with the header lines `# name:`
and `# pages:` and any `# fix:` lines, and pin it.

## ACTION draft
Packet: the established print with its fixes, and the establishment log.

**Drafter** gets `conventions.md`, `packet.md`, `units.py` and `../../../bardo-thodol-001.json` (the pilot:
word division, register, note density, recurring-pattern flags) and the published parts before this one.
Writes `drafts/<id>/units.json`:
`{"about": "<one paragraph, plain, on what this part says — as the pilot's about>",
  "sentences": [{"w": "<the text divided into words, ' / ' between verse lines>", "l": "…", "i": "…",
  "n": "…", "p": 1, "v": 1}]}` (`p` and `v` only where they apply; the first unit of a part has `p`).
`w` is the established text after its fixes, letter for letter, with a space between words: the build
refuses otherwise. Division rules: conventions.md, "What the page shows". House renderings: conventions.md,
"Translation". Each `# fix:` that corrects a misprint is named in that unit's note (README rule 5b).

**Reviewer** — two passes, as RUNBOOK.md says, plus: the word division against the conventions, every
grammatical label in the notes (case endings, verb stems), the house renderings.

**Glosser** (Sonnet): run `python3 ../run3/r3.py packet bardo-thodol <id>` again after the drafter (it then
lists the drafted words not yet in `glossary.json` in `novel-forms.json`). One entry per new word key
(the word in Tibetan script without its final tsheg), meaning only, in the style of `glossary.json`
(meaning first, then the parts in brackets, e.g. "of the bardo (bar do + -'i 'of')"); `__broaden__` for a
known word used in a new sense. The build puts the Wylie letters in front.

Build: `python3 ../run3/r3.py build bardo-thodol <id>`, then `validate`. No audio (Google has no Tibetan voice).

When the last part (bardo-thodol-013, ending text ga on p. 121) is published, `R3 next main` answers
COMPLETE: run `python3 ../run3/r3.py done bardo-thodol`, commit, push; the next firing moves on by itself.

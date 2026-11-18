# Ardā Wirāz Nāmag — what a firing does for this work

Read `../run3/RUNBOOK.md` first (it governs), then `conventions.md`. This file says what is particular here.
Setup once per firing: `pip install numpy pillow` (the page tools need them; nothing else).
The model of shape, register and note style is the published **arda-wiraz-001** (chapter 1):
`drafts/arda-wiraz-001/units.json` is its draft, `source/established/arda-wiraz-001.*` its established text.

## ACTION establish
`R3 establish-packet arda-wiraz <id>` writes `drafts/<id>/establish.md` with the exact procedure. In short:
1. Find the part's pages (`source/pages/n<leaf>.jpg`, starting at the leaf the packet names; the running head
   and the "Chapter N." headings tell you where you are).
2. Write `source/established/<id>.txt`: Haug's Roman reading, one numbered sentence per line, read from the
   page images (strongest model: this is reading a scan with no second reader).
3. Write `source/established/<id>.cut.json`: which printed lines are this part's Pahlavi and where each small
   sentence number sits (`python3 tools/sheet.py <leaf> …` makes the numbered sheets you read them from).
4. `R3 pin arda-wiraz <id>`. It refuses unless the two files agree sentence for sentence and every sentence has
   a plausible number of word shapes. It also takes the part's library label from the `# label:` line.
Nothing is drafted in an establishing firing. LOG line: leaves, sentences, anything unsure.

## The cut file, in one example
    {"leaves": {"109": {"lines": [6, 7], "num": {"6,0": "2.1", "7,3": "2.2"}, "drop": []},
                "110": {"lines": [0,1,2,3,4,5,6,7,8], "num": {"0,6": "2.3", …}, "drop": ["2,4", "8,11"]}}}
Lines and shapes are the numbers on the sheets (line L0 at the top; shapes counted from the right, 0 first).
`lines` lists only the Pahlavi lines of this part, never the headings, the Roman lines or the footnotes.
`drop` lists rings and paragraph ornaments. Shapes follow their sentence number across line and page ends.

## ACTION draft — the three roles
`R3 packet arda-wiraz <id>` writes `drafts/<id>/packet.md`: the pinned Roman sentences, every spelling already
settled, Haug's 1872 English as a check on the sense, and the glossary forms already entered.

**Drafter** (strongest model) gets `packet.md`, `conventions.md`, `drafts/arda-wiraz-001/units.json`, and the page
images for looking at the Pahlavi type where a spelling is in doubt. Writes `drafts/<id>/units.json`:
    {"about": "<optional: two or three sentences on what these chapters hold>",
     "advisory": {"lede": "…", "more": "…"},            (only where conventions.md, "Hell", calls for one)
     "sentences": [{"sents": ["2.1", "2.2"], "p": true, "t": "…", "w": "…", "l": "…", "i": "…", "n": "…"}]}
- A unit is one or more WHOLE sentences of Haug's, in order; never part of one. Join short sentences that make
  one sense unit; aim at units of 8–30 words. `sents` lists them. `p` on the unit that opens one of Haug's
  paragraphs (he indents them) and on the first unit of every chapter.
- `t` = the words as read, by the transcription rules in conventions.md. `w` = the letters as written, one
  group per word of `t`, separated by spaces (a compound that is one word in `t` joins its letter groups with
  a hyphen). Use the settled spelling for any word in the packet's list.
- `l`, `i`, `n` as in chapter 1. The note for the first unit of a chapter says in a clause where Wirāz now is.
- Sentence references in notes are written §chapter.sentence (§2.14).

**Reviewer** (strongest model, two passes) — as RUNBOOK.md, plus: every `w` group against Haug's Roman word
(the right word-sign, the final stroke where Haug has -ŏ/-ô) and, for any word new to the work, against the
Pahlavi type on the page; every `t` against the transcription rules; Haug's superseded readings handled as
conventions.md says. The reviewer checks the sense against Haug's English and then makes sure no phrase of
his survives in `l` or `i`.

**Glosser** (Sonnet) gets `units.json` and the packet's list of forms already entered. Writes
`drafts/<id>/gloss.json`: `{form: "lemma — meaning (grammar)"}` for every form of `t` (lowercased, as the
reader splits words) that is not yet entered; a known entry that does not cover this part's use goes under
`"__broaden__"` (old entry whole + " · " + new reading). Entries do not say how the word is written: the build
adds that from `w`. The reviewer's second pass checks every entry.

## Build, gate, publish
`R3 build` cuts the print images into `img/arda-wiraz/<nnn>/`, writes the story, and regenerates
`arda-wiraz-glossary.json` from `glossary-base.json` + `spellings.json` (commit all of them, and the images).
`R3 validate` must print PASS. A WARN about print shapes against words on a unit means the unit's `sents` or
the cut's numbers are off by one: look at that page's sheet before publishing.
If a page is unreadable or the cut cannot be made to pass, set the smallest piece aside (pipeline README,
rule 7) and go on; a part never waits for the owner.

## Voice
None chosen (owner, 2026-11-18: he cannot judge a language he does not know; the voice should follow the words
as read). Parts publish without audio. The run never builds audio.

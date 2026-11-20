# Classical Tibetan, *Bar do thos grol chen mo* — conventions (pilot, 2026-11-16)

First Tibetan text in Lectorium. Zev asked for the pilot; the choices below were made in the pilot
session and are his to change.

## Text of record

**The blockprint reproduced as BDRC W23710** (*Zab chos zhi khro dgongs pa rang grol las thos grol
skor*, undated woodblock print, 549 pp. in the reproduction, image group I0874; BDRC rights
statement: public domain). The *Chos nyid bar do'i gsal 'debs thos grol chen mo* is text **kha**,
starting at leaf n10 of the scan. Page images, reachable from cloud sessions:
`https://archive.org/download/bdrc-W23710/page/nNN_w3000.jpg` (native size 2021×494; leaf nNN =
printed page NN−1). Read by model from the images; enlarge doubtful words (crop ×5) before deciding.

A traditional blockprint carries no modern editor's work, so the pre-1930 rule is met by the
blocks themselves. Evans-Wentz 1927 printed no Tibetan, and there is no pre-1930 Western edition
of the Tibetan text.

Control witnesses, never the text and never copied (both stored in `source/raw/` since 2026-11-20, because
unattended runs cannot reach either site):
- dzogchengonpa.org, a line-by-line transcription of this same print with its page numbers (many
  typing errors; good for finding one's place);
- the text at bo.wikipedia.org (ཆོས་ཉིད་བར་དོའི་གསལ་འདེབས་ཐོས་གྲོལ་ཆེན་མོ་), another recension,
  for seeing where prints differ.
Modern translations (Evans-Wentz, Fremantle–Trungpa, Thurman, Dorje–Coleman) are not opened.

`source/` holds the print line by line, with `[?]` on uncertain readings and the line-end
abbreviations as printed.

## What the page shows

- Words model, `script: "tibetan"`. Tibetan writes no spaces between words; **the word division is
  ours** (lexical compounds one word: ཐོས་གྲོལ་, བྱང་ཆུབ་སེམས་དཔའ་; free particles their own word:
  ལ, ནི, དང, ཀྱི; fused endings stay on the word: བར་དོའི, བར་དོར, བླ་མས, བྱའོ).
- Each word = its syllables as glyphs, the tsheg kept with the syllable; ༔ and ༈ are `punct` glyphs.
- Under the words, by the two-state switch (the reader's say-mode): **letters** = Wylie per
  syllable (`glyphs[].tr`; EWTS for Sanskrit, shown with macrons, no `+`), or **as said** = one
  reading per word (`say`), THL Simplified Phonetic Transcription made by rule in `tib.py`
  (overrides there for Sanskrit: པདྨ pema, ཀྱཻ kyé).
- Popup: the word in Tibetan, its letters, how it is said, the glossary line.
- `units.py` holds the divided text, both translations and notes; `glossary.py` one entry per
  word form; `build.py` checks that the units reproduce the archived source letter for letter
  and that every word has an entry, then writes the part and its library entry.
- Verse (the opening fifteen nine-syllable lines) is `v: true`, one line per print verse line.

## The print's readings

- Line-end abbreviations written out (པའཾ → པའམ, ལཾ → ལམ).
- Clear misprints corrected in the text with the print's reading in the note (rule 5b): so far
  དུས་ཅན → ལུས་ཅན.
- The print's own spelling habits stay (འཕྲོད་བ, ཞུས་བ, ཐེབ beside ཐེབས, གཅིག་གི for གིས).
- Where the other recension differs in a way that changes the sense, the note says so; the print
  is followed.

## Translation

Two layers. `l` keeps Tibetan order (verb last, particles after their words) with hyphens for
fused endings. House renderings: bar do → "the between" in `l`, "bardo" in `i`; ngo sprod →
"face-introduce" / "point out"; 'od gsal → "clear light"; chos nyid → "reality itself" / "reality";
chos sku → "body of truth"; rig pa → "knowing" / "awareness"; rigs kyi bu → "child of noble
family"; 'pho ba → "transference"; rlung → "wind"; rtsa → "channel". Titles of companion texts
translated in `i`, explained in the note the first time.
Recurring patterns flagged once: verb-final order, -'i / -r / -s endings, the sentence-ending -o,
ma … na, the clause chain (la, nas, shing, ste), 'debs / btab / gdab / thebs.

## Open

1. Zev's verdict on the presentation.
2. No voice. Google has no Tibetan voice; nothing sampled.
3. No second-reader pass on the translation and no overlap scan against the modern translations.
4. Three uncertain readings (marked in the notes): དུས/ལུས p. 11, the length marks of དྷཱུ་ཏཱི p. 16,
   ཕྱིར་མེད་པ p. 17. A better scan or a second print would settle them.
5. For a run: the Thos grol chen mo proper is pp. 9–122 of the reproduction (chos nyid bar do,
   with the wrathful deities as text ga), the srid pa bar do is text ja; roughly 25–30 parts of
   this size. The four prayers (nga, ca, cha, ta) could follow. A shared glossary file would be
   needed, and page-image reading with a second reader, as for the Nights.

# Establish — bardo-thodol-004 (pp. 36–44 of the reproduction)

Read `conventions.md` first ("Text of record", "What the page shows", "The print's readings").
`pip install pyewts` if `python3 -c "import pyewts"` fails (it is needed for the draft and the build).

Start: …ར་ཡིན་ནོ་སྐྱབས་སུ་མཆིའོ་སྙམ་པའི་མོས་བ་གྱིས་ལ་གསོལ་བ་ཐོབ་ཅིག༔ — the end of bardo-thodol-003; begin with what follows (if that is mid-line, start the file with that page's {N} and the rest of the line)
Pages: source/pages/n37.jpg, source/pages/n38.jpg, source/pages/n39.jpg, source/pages/n40.jpg, source/pages/n41.jpg, source/pages/n42.jpg, source/pages/n43.jpg, source/pages/n44.jpg, source/pages/n45.jpg, source/pages/n46.jpg (page p is leaf n(p+1); the last one only to finish a sentence that runs over the edge of
p. 44).

Procedure (the image decides every letter; the witness tells you what to look for):
1. The witnesses are stored here, so no network is needed:
   - `source/raw/dzogchengonpa-kha.txt` — a transcription of THIS print, text kha, ONE PRINT LINE PER LINE
     (a line beginning ༄༅༔ ༔ starts a leaf front). It is close to the print but has typing errors
     (e.g. མཐབ for མཐའ, ལོངས་སྤྲོད for ལོངས་སྤྱོད, བཞུངས for བཞུགས). For text kha it is your working copy.
   - `source/raw/bowiki-other-recension.txt` — another recension; it goes on through the wrathful deities
     (text ga). For ga it is the guide to what a line says, never to how this print spells it.
2. Find the start point in the witness. Then, page by page: each page has FIVE print lines (count them on the
   image; a page that begins a leaf front opens with ༄༅༔ ༔). Crop one line at a time from the image, enlarge
   ×3 (×5 for a doubtful syllable), and check the witness line against it syllable by syllable. Where they
   differ, the image decides; where the image is unclear and the witness is plausible, take the witness and
   put `[?]` after the syllable. For text ga, read the image line by line with the other recension open: it
   tells you which words to expect, so a smudged syllable is a choice between candidates, never a guess.
   Write each print line as one line of the file, under a {page} marker, exactly as printed: tsheg, ༔ and །
   where the print has them, the line-end abbreviations as printed (པའཾ, ལཾ), the opening ornament ༄༅༔ ༔ where
   a page begins with it.
3. Stop at the last ༔ or ། that closes a sentence on p. 44, or finish the sentence from the next page.
4. Add `# fix:` lines for what the text will give differently from the print: each line-end abbreviation
   written out (`# fix: པའཾ => པའམ`), a tsheg missing where two print lines join (`# fix: རྣམསབར => རྣམས་བར`),
   and a clear misprint (README rule 5b; the note must name it). Nothing else.
5. Log every place the image overruled the witness, every `[?]`, every misprint, every place the other
   recension differs in sense, in `drafts/bardo-thodol-004/establish-log.md`; the drafter turns them into notes.
   A page you still cannot read with the witness beside it is a README rule 7 gap: the smallest stretch
   possible, logged, and the part goes on — never block the whole work for it.
6. Write `source/established/bardo-thodol-004.txt` with the header lines `# name:` (a short English name for the
   library: what this stretch says, e.g. "The second bardo: when the clear light is not recognised") and
   `# pages: pp. 36–44` (adjusted if it ran over), the `# fix:` lines, then the page-marked lines. Pin it:
   `python3 ../run3/r3.py pin bardo-thodol bardo-thodol-004`.

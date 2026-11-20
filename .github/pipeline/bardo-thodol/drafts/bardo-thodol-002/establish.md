# Establish — bardo-thodol-002 (pp. 18–26 of the reproduction)

Read `conventions.md` first ("Text of record", "What the page shows", "The print's readings").
`pip install pyewts` if `python3 -c "import pyewts"` fails (it is needed for the draft and the build).

Start: …ཞེས་ཕྱི་དབུགས་མ་ཆད་པའི་གོང་ནས་རྣ་བར་ལན་མང་དུ་བཤད་ལ་ཡིད་ལ་འཇགས་སུ་བཅུག་གོ༔ — the pilot (bardo-thodol-001) ends there, on the last line of p. 17 (leaf n18). bardo-thodol-002 begins with the next words, དེ་ནས་ at the end of that line: start the established file with {17} and that line-end fragment, then {18}.
Pages: source/pages/n19.jpg, source/pages/n20.jpg, source/pages/n21.jpg, source/pages/n22.jpg, source/pages/n23.jpg, source/pages/n24.jpg, source/pages/n25.jpg, source/pages/n26.jpg, source/pages/n27.jpg, source/pages/n28.jpg (page p is leaf n(p+1); the last one only to finish a sentence that runs over the edge of
p. 26).

Procedure (the image decides every letter):
1. Read each page line by line, enlarging (crop one line at a time and scale ×3; ×5 for a doubtful syllable).
   Write each print line as one line of the file, under a {page} marker, exactly as printed: tsheg, ༔ and །
   where the print has them, the line-end abbreviations as printed (པའཾ, ལཾ), the opening ornament ༄༅༔ ༔ if
   a page begins with it. Put `[?]` after any syllable you are not sure of.
2. Check your reading against the dzogchengonpa.org transcription of this same print and the bo.wikipedia.org
   text of another print if this sandbox can reach them; they find your place and flag a misread syllable, but
   the image decides. If they cannot be reached, say so in the log and read with extra care.
3. Stop at the last ༔ or ། that closes a sentence on p. 26, or finish the sentence from the next page.
4. Add `# fix:` lines for what the text will give differently from the print: each line-end abbreviation
   written out (`# fix: པའཾ => པའམ`), a tsheg missing where two print lines join (`# fix: རྣམསབར => རྣམས་བར`),
   and a clear misprint (README rule 5b; the note must name it). Nothing else.
5. Log every doubtful reading, every misprint, every place the other print differs in sense, in
   `drafts/bardo-thodol-002/establish-log.md`; the drafter turns them into notes.
6. Write `source/established/bardo-thodol-002.txt` with the header lines `# name:` (a short English name for the
   library: what this stretch says, e.g. "The second bardo: when the clear light is not recognised") and
   `# pages: pp. 18–26` (adjusted if it ran over), the `# fix:` lines, then the page-marked lines. Pin it:
   `python3 ../run3/r3.py pin bardo-thodol bardo-thodol-002`.

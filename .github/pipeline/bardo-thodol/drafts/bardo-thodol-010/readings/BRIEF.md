# Reader brief — bardo-thodol-010 establish (Bardo Thödröl, blockprint BDRC W23710, text GA, pp. 90–98)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use `/usr/bin/python3` (it has PIL; the default python3 does not) for cropping; write crops to drafts/bardo-thodol-010/readings/crops_<X>/ and delete them afterwards.
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading of THIS text ga: drafts/bardo-thodol-009/readings/read_C.txt and read_C-log.md (format and rigour to match),
and drafts/bardo-thodol-009/establish-log.md (the editor's decisions: ornament written ༄༅༔ ༔, -གས ligature written གས, etc.).
Do NOT open or recall any modern translation. Do not use the network.

## What is different this time
Text kha had a transcription of THIS print. Text ga has NONE. You read the image yourself, line by line.
Your guide is `drafts/bardo-thodol-010/readings/witness_ga.txt`: ANOTHER RECENSION (from bo.wikipedia), running text with no
line breaks, beginning at this part's start point (འདི་དང་བཏགས་གྲོལ…). It tells you which words to
expect, so a smudged syllable is a choice between candidates, never a free guess — but it is NOT this print: spelling,
particles, word order and whole phrases differ. Never copy it over what the image shows. Where the image is genuinely
unreadable and the recension offers a plausible candidate that fits the visible traces, take it and mark `[?]` after the
syllable. If a stretch cannot be read even so, write `[…]` for it and log it (it becomes a gap) — keep this to the minimum.

## Pages
Page p is the image source/pages/n(p+1).jpg (2021×494). Kha pages had five print lines; ga's first pages may differ —
COUNT the lines on every image (in ga so far, pp. 82–83 had four, pp. 84–90 five).
A page beginning a leaf front opens with ༄༅༔ ༔ or a similar ornament — record what is actually printed.

Procedure: find the line bands (row profile), crop each line in overlapping segments, enlarge ×3 (×5–×10 for doubtful
syllables), read syllable by syllable. Write each print line exactly as printed: tsheg, ༔ and ། as printed, line-end
abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས forms), ornament where printed. Filler dots at line
ends left out. Note whether the last syllable of each line carries a tsheg (a missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-010/readings/read_<X>.txt — `{page}` marker lines, then that page's print lines, for each of your pages.
- drafts/bardo-thodol-010/readings/read_<X>-log.md — line counts per page; method; every [?] with the candidates and why;
  every place this print differs from the other recension in a way that changes the sense (or adds/omits words);
  proposed `# fix:` lines (contractions/abbreviations written out, line-join tshegs, mid-line missing tshegs; format
  `# fix: <as printed, enough context to be unique> => <written out>`; -གས ligature written གས); suspected misprints with
  certainty and proposed fix (only where the sense allows one reading; otherwise "kept, note only"); any […] gap.
Reply with a short summary (lines read, [?] count, fixes, misprints, gaps). Do not commit.

## Where this part starts, and who reads what
Part 009 ended on p. 90 (image n91) line 2 at …ངན་སོང་དུ་སོང་བ་མི་སྲིད་དོ༔ (x≈1690). This part begins with what follows on
90.2 (expected འདི་དང…). Start your file `{90}` then the REST of line 90.2 only (from the first syllable after that ༔), then 90.3 onward.
- Reader A: p. 90 (rest of l. 2 to l. 5), pp. 91, 92 (images n91–n93).
- Reader B: pp. 93, 94, 95 (n94–n96). Also read the last line of p. 92 to confirm the seam with A.
- Reader C: pp. 96, 97, 98 (n97–n99), and p. 99 (n100) ONLY as far as needed to finish a sentence that runs over the end of p. 98.
  Also read the last line of p. 95 to confirm the seam. C decides the END: the last ༔ or ། closing a sentence at or near the
  end of p. 98 (or finish the sentence on p. 99); say exactly where, and propose a `# name:` (a short English name for what pp. 90–98 say).
Readers write only their own pages in read_<X>.txt (the seam lines go in the log, not the file).

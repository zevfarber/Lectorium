# Reader brief — bardo-thodol-011 establish (Bardo Thödröl, blockprint BDRC W23710, text GA, pp. 98–107)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use `/usr/bin/python3` (it has PIL; the default python3 does not) for cropping; write crops to drafts/bardo-thodol-011/readings/crops_<X>/ and delete them afterwards.
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading of THIS text ga: drafts/bardo-thodol-010/readings/read_C.txt and read_C-log.md (format and rigour to match),
and drafts/bardo-thodol-009/establish-log.md and drafts/bardo-thodol-010/establish-log.md (the editor's decisions: ornament written ༄༅༔ ༔, -གས ligature written གས, etc.).
Do NOT open or recall any modern translation. Do not use the network.

## What is different this time
Text kha had a transcription of THIS print. Text ga has NONE. You read the image yourself, line by line.
Your guide is `drafts/bardo-thodol-011/readings/witness_ga.txt`: ANOTHER RECENSION (from bo.wikipedia), running text with no
line breaks, beginning at this part's start point (ཡང་དེ་ལྟར་ངོ་སྤྲད་ཀྱང…). It tells you which words to
expect, so a smudged syllable is a choice between candidates, never a free guess — but it is NOT this print: spelling,
particles, word order and whole phrases differ. Never copy it over what the image shows. Where the image is genuinely
unreadable and the recension offers a plausible candidate that fits the visible traces, take it and mark `[?]` after the
syllable. If a stretch cannot be read even so, write `[…]` for it and log it (it becomes a gap) — keep this to the minimum.

## Pages
Page p is the image source/pages/n(p+1).jpg (2021×494). Kha pages had five print lines; ga's first pages may differ —
COUNT the lines on every image (in ga so far, pp. 82–83 had four, pp. 84–98 five).
A page beginning a leaf front opens with ༄༅༔ ༔ or a similar ornament — record what is actually printed.

Procedure: find the line bands (row profile), crop each line in overlapping segments, enlarge ×3 (×5–×10 for doubtful
syllables), read syllable by syllable. Write each print line exactly as printed: tsheg, ༔ and ། as printed, line-end
abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས forms), ornament where printed. Filler dots at line
ends left out. Note whether the last syllable of each line carries a tsheg (a missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-011/readings/read_<X>.txt — `{page}` marker lines, then that page's print lines, for each of your pages.
- drafts/bardo-thodol-011/readings/read_<X>-log.md — line counts per page; method; every [?] with the candidates and why;
  every place this print differs from the other recension in a way that changes the sense (or adds/omits words);
  proposed `# fix:` lines (contractions/abbreviations written out, line-join tshegs, mid-line missing tshegs; format
  `# fix: <as printed, enough context to be unique> => <written out>`; -གས ligature written གས); suspected misprints with
  certainty and proposed fix (only where the sense allows one reading; otherwise "kept, note only"); any […] gap.
Reply with a short summary (lines read, [?] count, fixes, misprints, gaps). Do not commit.

## Where this part starts, and who reads what
Part 010 ended on p. 98 (image n99) line 3 at …གཉིས་སུ་མེད་པར་ཐིམ་ནས / སངས་རྒྱས་པར་འགྱུར་རོ༔ (98.3 begins with སངས་རྒྱས་པར་འགྱུར་རོ༔).
This part begins with what follows on 98.3 (expected ཡང་དེ་ལྟར་ངོ་སྤྲད་ཀྱང…). Start your file `{98}` then the REST of line 98.3 only
(from the first syllable after that ༔), then 98.4 onward. Some images are skewed (n98, n99 were): straighten a copy if needed.
- Reader A: p. 98 (rest of l. 3 to l. 5), pp. 99, 100, 101 (images n99–n102).
- Reader B: pp. 102, 103, 104 (n103–n105). Also read the last line of p. 101 to confirm the seam with A.
- Reader C: pp. 105, 106, 107 (n106–n108), and p. 108 (n109) ONLY as far as needed to finish a sentence that runs over the end of p. 107.
  Also read the last line of p. 104 to confirm the seam. C decides the END: the last ༔ or ། closing a sentence at or near the
  end of p. 107 (or finish the sentence on p. 108); prefer a break at a natural division of the text (e.g. the close of a day or section)
  if one falls on p. 107; say exactly where, and propose a `# name:` (a short English name for what pp. 98–107 say).
Readers write only their own pages in read_<X>.txt (the seam lines go in the log, not the file).

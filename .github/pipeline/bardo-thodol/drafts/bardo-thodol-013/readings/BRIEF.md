# Reader brief — bardo-thodol-013 establish (Bardo Thödröl, blockprint BDRC W23710, text GA, pp. 115–121: THE LAST PART)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use python3 (it has PIL) for cropping; write crops to drafts/bardo-thodol-013/readings/crops_<X>/ and delete them afterwards.
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading of THIS text ga: drafts/bardo-thodol-012/readings/read_C.txt and read_C-log.md (format and rigour to match),
and drafts/bardo-thodol-012/establish-log.md (the editor's decisions: ornament written ༄༅༔ ༔, -གས ligature written གས, ཀྱཻ with two e-signs, etc.).
Do NOT open or recall any modern translation. Do not use the network.

## Method
Text ga has NO transcription of this print. You read the image yourself, line by line.
Your guide is `drafts/bardo-thodol-013/readings/witness_ga.txt`: ANOTHER RECENSION (from bo.wikipedia), running text with no
line breaks, beginning at this part's start point (ཁྱོད་རང་གི་བླ་མའི་མཚན…) and running to the end of text ga, colophon included.
It tells you which words to expect, so a smudged syllable is a choice between candidates, never a free guess — but it is NOT
this print: spelling, particles, word order and whole phrases differ (the colophon in particular may differ entirely). Never copy
it over what the image shows. Where the image is genuinely unreadable and the recension offers a plausible candidate that fits the
visible traces, take it and mark `[?]` after the syllable. If a stretch cannot be read even so, write `[…]` for it and log it
(it becomes a gap) — keep this to the minimum.

## Pages
Page p is the image source/pages/n(p+1).jpg (2021×494). COUNT the lines on every image (pp. 84–115 had five).
A page beginning a leaf front (odd pages: 117, 119, 121) opens with ༄༅༔ ༔ or a similar ornament — record what is printed.
Earlier images were skewed 1–2°: straighten a copy before cropping.

Procedure: find the line bands (row profile), crop each line in overlapping segments, enlarge ×3 (×5–×10 for doubtful
syllables), read syllable by syllable. Write each print line exactly as printed: tsheg, ༔ and ། as printed, line-end
abbreviations and contractions as printed (པའཾ, ལཾ, subscript-ས forms), ornament where printed. Filler dots at line
ends left out. Note whether the last syllable of each line carries a tsheg (a missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-013/readings/read_<X>.txt — `{page}` marker lines, then that page's print lines, for each of your pages.
- drafts/bardo-thodol-013/readings/read_<X>-log.md — line counts per page; method; every [?] with the candidates and why;
  every place this print differs from the other recension in a way that changes the sense (or adds/omits words);
  proposed `# fix:` lines (contractions/abbreviations written out, line-join tshegs, mid-line missing tshegs; format
  `# fix: <as printed, enough context to be unique> => <written out>`); suspected misprints with certainty and proposed fix
  (only where the sense allows one reading; otherwise "kept, note only"); any […] gap.
Reply with a short summary (lines read, [?] count, fixes, misprints, gaps). Do not commit.

## Where this part starts, and who reads what
Part 012 ended mid-line on p. 115 (image n116) line 5: …ཐུགས་རྗེས་བཟུང་ཞིག༔ ཡི་དམ་རིན་པོ་ཆེ་ཞེས་བོས་ལ་གསོལ་བ་ཐོབ་ཅིག༔
This part begins right after, on 115.5, with ཁྱོད་རང་གི་བླ་མའི་… . The established 115.5 line is the last line of
source/established/bardo-thodol-012.txt.
- Reader A: the rest of 115.5 (start the file `{115}` with only the part of line 5 after …གསོལ་བ་ཐོབ་ཅིག༔ — check the image that
  nothing else sits between), then pp. 116, 117 (images n116 (line 5 only), n117, n118).
- Reader B: pp. 118, 119 (n119, n120). Also read the last line of p. 117 to confirm the seam with A.
- Reader C: pp. 120, 121 (n121, n122). Also read the last line of p. 119 to confirm the seam. Text ga ENDS on p. 121
  (prayer of the bardo / benefits / colophon). Say exactly where the text ends on the page (what follows it, if anything: a
  new title, blank, ornament), and whether anything on p. 121 after the end of ga belongs to another text (leave that out).
  If text ga's last sentence runs onto the next page, say so (the image n123 is NOT stored; report it). Propose a `# name:`
  (a short English name for what pp. 115–121 say).
Readers write only their own pages in read_<X>.txt (the seam lines go in the log, not the file).

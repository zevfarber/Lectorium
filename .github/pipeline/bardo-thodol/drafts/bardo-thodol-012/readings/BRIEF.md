# Reader brief — bardo-thodol-012 establish (Bardo Thödröl, blockprint BDRC W23710, text GA, pp. 107–115)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use python3 (it has PIL) for cropping; write crops to drafts/bardo-thodol-012/readings/crops_<X>/ and delete them afterwards.
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading of THIS text ga: drafts/bardo-thodol-011/readings/read_C.txt and read_C-log.md (format and rigour to match),
and drafts/bardo-thodol-010/establish-log.md and drafts/bardo-thodol-011/establish-log.md (the editor's decisions: ornament written ༄༅༔ ༔, -གས ligature written གས, etc.).
Do NOT open or recall any modern translation. Do not use the network.

## What is different this time
Text kha had a transcription of THIS print. Text ga has NONE. You read the image yourself, line by line.
Your guide is `drafts/bardo-thodol-012/readings/witness_ga.txt`: ANOTHER RECENSION (from bo.wikipedia), running text with no
line breaks, beginning at this part's start point (ཀྱེ་རིགས་ཀྱི་བུ་ལྷོ་ནས…) and running on to the end of text ga. It tells you which words to
expect, so a smudged syllable is a choice between candidates, never a free guess — but it is NOT this print: spelling,
particles, word order and whole phrases differ. Never copy it over what the image shows. Where the image is genuinely
unreadable and the recension offers a plausible candidate that fits the visible traces, take it and mark `[?]` after the
syllable. If a stretch cannot be read even so, write `[…]` for it and log it (it becomes a gap) — keep this to the minimum.

## Pages
Page p is the image source/pages/n(p+1).jpg (2021×494). Kha pages had five print lines; ga's first pages may differ —
COUNT the lines on every image (in ga so far, pp. 82–83 had four, pp. 84–107 five).
A page beginning a leaf front opens with ༄༅༔ ༔ or a similar ornament — record what is actually printed.

Procedure: find the line bands (row profile), crop each line in overlapping segments, enlarge ×3 (×5–×10 for doubtful
syllables), read syllable by syllable. Write each print line exactly as printed: tsheg, ༔ and ། as printed, line-end
abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས forms), ornament where printed. Filler dots at line
ends left out. Note whether the last syllable of each line carries a tsheg (a missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-012/readings/read_<X>.txt — `{page}` marker lines, then that page's print lines, for each of your pages.
- drafts/bardo-thodol-012/readings/read_<X>-log.md — line counts per page; method; every [?] with the candidates and why;
  every place this print differs from the other recension in a way that changes the sense (or adds/omits words);
  proposed `# fix:` lines (contractions/abbreviations written out, line-join tshegs, mid-line missing tshegs; format
  `# fix: <as printed, enough context to be unique> => <written out>`; -གས ligature written གས); suspected misprints with
  certainty and proposed fix (only where the sense allows one reading; otherwise "kept, note only"); any […] gap.
Reply with a short summary (lines read, [?] count, fixes, misprints, gaps). Do not commit.

## Where this part starts, and who reads what
Part 011 ended at the end of p. 107 (image n108) line 2: …ཤར་གྱི་རྣལ་འབྱོར་མ་དྲུག་རང་གི་ཀླད་པའི་ནང་ནས་ཐོན་ནས་རང་ལ་འཆར་དུ་འོང་ངོ༔ དེ་ལ་མ་འཇིགས་ཤིག༔
This part begins with 107.3 (expected ཀྱཻ་རིགས་ཀྱི་བུ༔ ལྷོ་ནས…). Start your file `{107}` then lines 107.3, 107.4, 107.5.
A first reading of 107.3–5 by part 011's reader C is in drafts/bardo-thodol-011/readings/read_C.txt (last three lines): it has a
gap at 107.3 དགའ་བ་སེར་མོ་[…]་མགོ (an animal head of two syllables, the second ending in ད; the other recension has རྡོ་རྗེ་སེར་མོ་ཕག་མགོ་མ,
whose ཕག did not fit the traces) and a [?] at 107.5 སྤྲའི. Treat it as a check, not as the text: re-read those lines from the image,
and work hard on the gap (×5–×10, straightened copy; think which animal names fit the traces).
Images from n99 to n109 were skewed 1.4–2.0°: straighten a copy before cropping.
- Reader A: p. 107 (ll. 3–5), pp. 108, 109 (images n108–n110).
- Reader B: pp. 110, 111, 112 (n111–n113). Also read the last line of p. 109 to confirm the seam with A.
- Reader C: pp. 113, 114, 115 (n114–n116), and p. 116 (n117) ONLY as far as needed to finish a sentence that runs over the end of p. 115.
  Also read the last line of p. 112 to confirm the seam. C decides the END: the last ༔ or ། closing a sentence at or near the
  end of p. 115 (or finish the sentence on p. 116); prefer a break at a natural division of the text if one falls on p. 115 (the last
  part, 013, covers pp. 116–121 to the end of text ga); say exactly where, and propose a `# name:` (a short English name for what
  pp. 107–115 say).
Readers write only their own pages in read_<X>.txt (the seam lines go in the log, not the file).

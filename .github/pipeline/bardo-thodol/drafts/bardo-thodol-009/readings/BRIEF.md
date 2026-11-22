# Reader brief — bardo-thodol-009 establish (Bardo Thödröl, blockprint BDRC W23710, text GA)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use `/usr/bin/python3` (it has PIL) for cropping; write crops to drafts/bardo-thodol-009/readings/crops_<X>/ and delete them afterwards.
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading: drafts/bardo-thodol-008/readings/read_A.txt and read_A-log.md (format and rigour to match).
Do NOT open or recall any modern translation. Do not use the network.

## What is different this time
Text kha had a transcription of THIS print. Text ga has NONE. You read the image yourself, line by line.
Your guide is `drafts/bardo-thodol-009/readings/witness_ga.txt`: ANOTHER RECENSION (from bo.wikipedia), running text with no
line breaks, beginning at the start of the wrathful-deities bardo (ད་ནི་ཁྲོ་བོའི་བར་དོར་འཆར་ཚུལ…). It tells you which words to
expect, so a smudged syllable is a choice between candidates, never a free guess — but it is NOT this print: spelling,
particles, word order and whole phrases differ. Never copy it over what the image shows. Where the image is genuinely
unreadable and the recension offers a plausible candidate that fits the visible traces, take it and mark `[?]` after the
syllable. If a stretch cannot be read even so, write `[…]` for it and log it (it becomes a gap) — keep this to the minimum.

## Pages
Page p is the image source/pages/n(p+1).jpg (2021×494). Kha pages had five print lines; ga's first pages may differ —
COUNT the lines on every image (n83, p. 82, has only four). p. 81 (n82) is the title leaf of text ga: one line in a frame
(read it exactly, ornament included; also the letter in the top margin, ག, and the margin label at the left).
A page beginning a leaf front opens with ༄༅༔ ༔ or a similar ornament — record what is actually printed.

Procedure: find the line bands (row profile), crop each line in overlapping segments, enlarge ×3 (×5–×10 for doubtful
syllables), read syllable by syllable. Write each print line exactly as printed: tsheg, ༔ and ། as printed, line-end
abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས forms), ornament where printed. Filler dots at line
ends left out. Note whether the last syllable of each line carries a tsheg (a missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-009/readings/read_<X>.txt — `{page}` marker lines, then that page's print lines, for each of your pages.
- drafts/bardo-thodol-009/readings/read_<X>-log.md — line counts per page; method; every [?] with the candidates and why;
  every place this print differs from the other recension in a way that changes the sense (or adds/omits words);
  proposed `# fix:` lines (contractions/abbreviations written out, line-join tshegs, mid-line missing tshegs; format
  `# fix: <as printed, enough context to be unique> => <written out>`; -གས ligature written གས); suspected misprints with
  certainty and proposed fix (only where the sense allows one reading; otherwise "kept, note only"); any […] gap.
Reply with a short summary (lines read, [?] count, fixes, misprints, gaps). Do not commit.

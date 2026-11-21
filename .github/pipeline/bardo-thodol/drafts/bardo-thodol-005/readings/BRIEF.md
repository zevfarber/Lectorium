# Reader brief — bardo-thodol-005 establish (Bardo Thödröl, blockprint BDRC W23710, text kha)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use `/usr/bin/python3` (it has PIL) for cropping; write crops to your own scratch dir under /tmp/claude-0/.../scratchpad or drafts/bardo-thodol-005/readings/crops_<X>/ (delete crops afterwards).
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading: drafts/bardo-thodol-004/readings/read_C.txt and read_C-log.md (format and level of rigour to match).
Do NOT open or recall any modern translation. Do not use the network.

Your pages: page p is the image source/pages/n(p+1).jpg (2021×494, five print lines per page; a page that begins
a leaf front — odd pages here — opens with ༄༅༔ ༔). Your witness slice: drafts/bardo-thodol-005/readings/witness_<X>.txt —
a transcription of THIS print, one print line per line, in order (5 lines per page), with typing errors.
The other recension (source/raw/bowiki-other-recension.txt) may be consulted to see what a line says.

Procedure: for each print line, crop it out of the image (find the five line bands), enlarge ×3 (×5–×10 for a doubtful
syllable), and check the witness line against it syllable by syllable. Where they differ the image decides; where the
image is unclear and the witness is plausible, take the witness and put [?] after the syllable. Write each print line
exactly as printed: tsheg, ༔ and ། as printed, line-end abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས
forms like དངངྶ), the opening ornament ༄༅༔ ༔ where a page has it. Filler dots at line ends are left out. Note whether the last
syllable of each line has a tsheg (missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-005/readings/read_<X>.txt — `{page}` marker lines, then the five print lines of that page, for each of your pages.
- drafts/bardo-thodol-005/readings/read_<X>-log.md — line counts; table of every place the image overruled the witness
  (page.line | witness → print | why); every [?]; witness readings checked and confirmed though odd; proposed `# fix:` lines
  (contractions/abbreviations written out, line-join tshegs; format `# fix: <as printed, enough context to be unique> => <written out>`;
  conventions: line-end/mid-line contractions written out, -གས ligature written གས); suspected misprints with certainty and the
  proposed fix (only where the sense allows one reading; otherwise "kept, note only"); places the other recension differs in sense.
Reply with a short summary (counts of corrections, [?], fixes, misprints). Do not commit.

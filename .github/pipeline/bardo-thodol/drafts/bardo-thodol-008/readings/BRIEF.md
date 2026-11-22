# Reader brief — bardo-thodol-008 establish (Bardo Thödröl, blockprint BDRC W23710, text kha)

Work folder: /home/user/Lectorium/.github/pipeline/bardo-thodol (run commands from here).
Use `/usr/bin/python3` (it has PIL) for cropping; write crops to your own scratch dir under /tmp/claude-0/.../scratchpad or drafts/bardo-thodol-008/readings/crops_<X>/ (delete crops afterwards).
Read first: conventions.md ("Text of record", "What the page shows", "The print's readings"), and as the model of a
finished reading: drafts/bardo-thodol-006/readings/read_C.txt and read_C-log.md (format and level of rigour to match).
Do NOT open or recall any modern translation. Do not use the network.

Your pages: page p is the image source/pages/n(p+1).jpg (2021×494, five print lines per page; a page that begins
a leaf front — odd pages here — opens with ༄༅༔ ༔). Your witness slice: drafts/bardo-thodol-008/readings/witness_<X>.txt —
a transcription of THIS print, one print line per line, in order (5 lines per page), with typing errors.
The other recension (source/raw/bowiki-other-recension.txt) may be consulted to see what a line says.

Procedure: for each print line, crop it out of the image (find the five line bands), enlarge ×3 (×5–×10 for a doubtful
syllable), and check the witness line against it syllable by syllable. Where they differ the image decides; where the
image is unclear and the witness is plausible, take the witness and put [?] after the syllable. Write each print line
exactly as printed: tsheg, ༔ and ། as printed, line-end abbreviations and contractions as printed (པའཾ, ལཾ, ནམཁའ, subscript-ས
forms like དངངྶ), the opening ornament ༄༅༔ ༔ where a page has it. Filler dots at line ends are left out. Note whether the last
syllable of each line has a tsheg (missing tsheg at a line join needs a # fix line).

Write:
- drafts/bardo-thodol-008/readings/read_<X>.txt — `{page}` marker lines, then the five print lines of that page, for each of your pages.
- drafts/bardo-thodol-008/readings/read_<X>-log.md — line counts; table of every place the image overruled the witness
  (page.line | witness → print | why); every [?]; witness readings checked and confirmed though odd; proposed `# fix:` lines
  (contractions/abbreviations written out, line-join tshegs; format `# fix: <as printed, enough context to be unique> => <written out>`;
  conventions: line-end/mid-line contractions written out, -གས ligature written གས); suspected misprints with certainty and the
  proposed fix (only where the sense allows one reading; otherwise "kept, note only"); places the other recension differs in sense.
Reply with a short summary (counts of corrections, [?], fixes, misprints). Do not commit.

## This part (bardo-thodol-008, pp. 72–79)
Reader A: pp. 72–74 (images n73–n75). Reader B: pp. 75–77 (n76–n78). Reader C: pp. 78–79 (n79–n80).
Odd pages (73, 75, 77, 79) begin leaf fronts with ༄༅༔ ༔ — check this on the image.
Part seam: part 007 ended mid-line on 72.2 at …ཕྱག་རྒྱ་ནམ་མཁའ་ལ་མཛད་པ་ཅིག་འཆར་དུ་འོང་ངོ༔ (source/established/bardo-thodol-007.txt
already holds 72.1 and the start of 72.2). Reader A: transcribe ALL five lines of p. 72 (the assembler cuts at the seam) and
say exactly where on 72.2 the seam falls; part 008 begins with དཀྱིལ་འཁོར་དེའི་ཤར་ནས…
Reader C: p. 79 is the LAST page of text kha and has only THREE print lines (witness_C.txt: 5 lines of p. 78, then 3 of p. 79);
it closes with the colophon-like end (…ཐོས་གྲོལ་ཆེན་མོ་ཐལ་ལོ༔ then a mantric syllable and རྒྱ་རྒྱ་རྒྱ༔). Read the mantric syllable
(witness ཨྛྀི, likely wrong) with special care at ×5–×10 and say what stack the print really has; report anything in the
margin. The part ends at the end of p. 79. Reader C also proposes a short English `# name:` for the part (what pp. 72–79 say:
the seventh day's knowledge-holders, the ḍākinīs and their music, the animal light, the prayer, and the close of the
peaceful-deities bardo).
Report the tsheg status of your own first and last lines.

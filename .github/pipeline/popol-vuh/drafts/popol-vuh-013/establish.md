# Establish — popol-vuh-013 (images 0043–0047)

Read `conventions.md` first ("What the text looks like", the Parra letters, word division).

Start: …vabanel. Quehe cut xe chacatah vi rahaual Xibalba ri rumal capoh; xe moyvachixic conohel.  (the end of popol-vuh-012; begin with the words that follow these)
Images: source/pages/i0043.jpg, source/pages/i0044.jpg, source/pages/i0045.jpg, source/pages/i0046.jpg, source/pages/i0047.jpg, source/pages/i0048.jpg (the last one only to finish a sentence that runs over the edge of image 0047).
Each image is the K'iche' (left) column of one manuscript page, background flattened. Ximénez's Spanish is in
the right-hand column of the original and is not in these crops.

Procedure (the image decides every letter):
1. Brasseur de Bourbourg's 1861 edition is a transcription of THIS manuscript, stored here as OCR
   (`source/raw/brasseur1861_djvu.txt`; K'iche' paragraphs with his French translation and notes mixed in).
   Find the start point in it (search for a distinctive word or name); his text tells you what each line of
   the image should say. Then read the column in strips (crop about six lines at a time and enlarge 2–3×, e.g.
   with PIL), top to bottom, image by image, and write what Ximénez wrote, checking every word against
   Brasseur. The differences you must expect and always resolve in favour of the image: Brasseur prints q for
   ꜭ, g for ꜫ, tz for ꜩ, separates prefixes with hyphens (x-qui nohih) and apostrophes (r'utzinic), and
   normalises spelling; the OCR adds its own errors. Write the letters as Ximénez wrote them: c/qu, v, z, h,
   b, doubled vowels, and the colonial letters ꜩ ꜯ ꜭ ꜭh ꜫ (capitals Ꜩ Ꜯ Ꜭ Ꜫ). Where the image is unclear,
   take the letter Brasseur's reading implies and log it. Brasseur is never the text: his word order,
   additions or omissions against the image are logged and the image followed. A line still unreadable with
   Brasseur beside it is a README rule 7 gap — the smallest stretch possible, logged; never block the work.
2. Words Ximénez runs together across a line break are divided; particles he joins to a word are divided as
   the conventions say. A word he adds above the line is printed in place (note it in the log).
3. Punctuation, capitals and quotation marks are ours (“ ” around direct speech). Capitals: sentence start,
   names, the divine titles.
4. Paragraphs: Ximénez's own paragraphs and headings; a heading in capitals is its own paragraph, in
   capitals as he writes it.
5. Log every letter decided against Brasseur, every doubtful reading and every supralinear word in
   `drafts/popol-vuh-013/establish-log.md`; the drafter turns these into notes.
6. Write `source/established/popol-vuh-013.txt` in this format:
       # name: <short English name for the library, what happens in this stretch: "The animals are made">
       # title: <the first four to six words of the part, in the manuscript spelling>
       # fols: <folios, as Ximénez numbers them at the top right of each recto, e.g. "fols. 2v–4r">
       <paragraph>

       <paragraph>
   then pin it: `python3 ../run3/r3.py pin popol-vuh popol-vuh-013`.

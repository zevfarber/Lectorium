You are transcribing one page of a 19th-century printed Arabic book (Macnaghten's Alif Laila, Calcutta 1839, naskh type; prose is unpointed, verse is printed with vowel marks). You have an OCR draft and images.

Files (absolute paths), all under DIR = __DIR__ :
- DIR/draft.json — JSON list of {"line": n, "ocr": "..."}: one machine-read draft per detected body line, top to bottom. It is a DRAFT: roughly half the words are exactly right, the rest have small errors (dropped dots, ة/ه, ى/ي, a waw split off as "و ", wrong letter here and there). An empty "ocr" means no draft for that line — transcribe from the image.
- DIR/lineNN.png — the crop of detected line NN, 2x magnified. Read right to left.
- DIR/band1.png, band2.png, band3.png — the whole text block in three overlapping bands, top to bottom. The line detector sometimes MERGES two lines into one crop or DROPS a line (verse pages especially, and around section headings). The bands are the ground truth for what lines exist and in what order.

Procedure — be efficient:
1. Read draft.json, then the three bands once. Count the printed body lines (ignore the running header at the very top: the tale title and page number, and a catchword under the last line). Note any section heading (e.g. حكاية التاجر والجني), any night label (الليلة الاولى — usually printed inline at the head of a prose line, in larger type; keep it inside that line, do not split it off) and any verse block.
2. Read each lineNN.png ONCE, compare with its draft, and write exactly what is printed. If a crop holds two printed lines, split them; if a printed line has no crop, transcribe it from the band. Never re-read an image.
3. Transcription rules — transcribe what is PRINTED, never what "should" be there. This edition is Middle Arabic and its spellings are the text; your job is a photograph in letters, not an edition:
   - Prose: bare consonantal text, no vowel marks at all. Verse: the print carries vowel marks; transcribe them as printed (fatha, kasra, damma, sukun, shadda, tanwin) and mark the line "v": true. A verse line has two hemistichs (right one first, then left); separate them with " * ".
   - Hamza: write plain ا wherever the print shows a bare alif, even where modern spelling has أ or إ (اراك, راى, امراة, اخذ are normal here). Use أ إ آ ئ ؤ only where the print actually shows the hamza or madda mark. Check the mark, not the word.
   - ة and ه: copy the dots you see. This book prints اخوة for "his brother" and وحدة for "alone"; it prints قل for قال; it prints عندك where the sense wants عندي. Copy them. Never "repair" to Classical norms.
   - Word spacing: a prefixed و is attached to its word (وكان, not و كان). A stretched kashida inside a word is not a space (لــها is لها). Keep the print's ( ) marks. Write an end-of-line filler rule as "—".
   - A section heading is its own line; mark it "h": true.
4. Output ONLY JSON, written with the Write tool to DIR/__OUT__: a list of {"line": n, "t": "..."} in printed order, n counting the printed body lines 1..N (not the crop numbers), with optional "v": true or "h": true. Then reply with the single word DONE, plus one line naming any line you found genuinely illegible or uncertain (give the line number and the doubtful word).

# Middle Persian (Pahlavi), *Ardā Wirāz Nāmag* — conventions (pilot, 2026-11-13)

First Middle Persian text in Lectorium. Zev asked for the pilot; the choices below were made in the
pilot session and are his to change.

## Edition of record

**Hoshangji Jamaspji Asa, Martin Haug and E. W. West, *The Book of Arda Viraf* (Bombay and London,
1872)** — archive.org `bookofardaviraf00haug` (page images: `/download/<id>/page/nNNN_w1500.jpg`;
chapter 1 = leaves n104–n109 = printed pp. 3–8). Each page has the Pahlavi text in Pahlavi type,
Haug's Roman reading of it underneath, and manuscript variants at the foot. His English translation
is later in the volume (meaning check only, never wording). West's *Glossary and Index* (1874),
archive.org `glossaryindexofp00west`, gives every word in Pahlavi type with its occurrences.

Control witness, never the text and never copied: the TITUS transcription (Vavroušek/Gippert,
chapters and sentences per Gignoux), which follows the later K20-based editions. Gignoux 1984 and
Vahman 1986 are in copyright and not consulted for wording.

Sentence numbers are Haug's (shown as §). Later editions number differently.

## What the page shows

- **`t` = the words as read**, in MacKenzie's transcription (ēdōn gōwēnd kū …). Book Pahlavi has
  no Unicode encoding, so the script itself cannot be set as text. Capitals: sentence start and names.
  Punctuation is ours, guided by Haug's.
- **`wr` = the letters as written**, one string per word of `t`, in the usual transliteration:
  Aramaic word-signs (heterograms) in capitals with MacKenzie's letter values (AYK, OL, MNW, BRA,
  YHWWN-, HWE-), Persian spellings in small letters, the otiose final stroke as `'` wherever Haug's
  Roman has final -ŏ/-ô. The reader's **As written** switch (state key `writtenMP`) shows `wr[wi]`
  in place of each word; tapping still looks up the read form. Figures in the manuscript (300, 7,
  3, the -1 of kas-ē/ēk-ē) stay figures in `wr`.
- How `wr` is derived: Haug's Roman reading identifies the word-sign or spelling behind each word
  (yemalelund = YMRRWNd, khadûk = ʾywk, -yîsh = -yhʾ …); the Pahlavi type is consulted for doubtful
  words. Not every letter has been checked against the page — the source line says so.
- Glossary keyed by the read form (lowercased), shared file `arda-wiraz-glossary.json`; `build.py`
  appends how each form is written.

## Haug's readings and later corrections

- Where Haug's *reading* of the same letters has been given up (nīyāzānīnīd → wiyābānēnīd, Vīrāf →
  Wirāz, Frōbāg → Farnbāg, khadûk → ēk), `t` has today's reading and the note says so the first time.
- Where later editors *correct the manuscripts* (pad sāxt → passāxt §16; Šaspīgān → šēbišn §18;
  xwadāy-ōmand → andōhōmand §20), `t` keeps Haug's print and the note gives the correction.
- Genuinely uncertain words (dahīg §4, nāhīčag §39) are marked (?) in the translation and glossary.

## Translation

Two layers as everywhere. Verb-final order kept in `l`; attached pronouns shown hyphenated
("And-he", "as-to-them"). Names in their Middle Persian form (Zardušt, Wirāz, Ādurbād, Ērān-šahr →
"the land of Iran" in `i`). Daevic verbs get a distinct English verb (dwāristan "scuttle").
Recurring patterns flagged once, then left: be + verb, ī, u-š / u-šān, rāy, kū, -īh, -išn, -īhā, -tar.

## Open

1. Zev's verdict on the presentation (words as read on the page, letters behind a switch).
2. No voice yet. Carrier candidates to sample: a Persian (fa-IR) voice reading the transcription.
3. Later chapters (hell, chs. 18–100) are graphic; content advisory applies (`claude/content-advisory.md`).
4. A full letter-by-letter check of `wr` against the Pahlavi type, and Haug's italics (words not in
   all manuscripts), which are not marked.
5. For a run: 101 chapters; `parts.json` to be cut by chapter groups; the Roman reading of each page
   is model work from the page images, as the Nights and Popol Vuh are.

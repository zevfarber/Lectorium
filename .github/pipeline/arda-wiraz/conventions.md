# Middle Persian (Pahlavi), *Ardā Wirāz Nāmag* — conventions

First Middle Persian text in Lectorium. Pilot 2026-11-13 (chapter 1); the owner's rulings on the script
2026-11-18; queued on Run 4 the same day. Model part: **arda-wiraz-001**.

## Edition of record
**Hoshangji Jamaspji Asa, Martin Haug and E. W. West, *The Book of Arda Viraf* (Bombay and London, 1872)**,
archive.org `bookofardaviraf00haug`. Page images of the whole Pahlavi text are in `source/pages/` (leaves
n104–n239; leaf = printed page + 101; the text ends about n237). Each page: the Pahlavi in Pahlavi type,
Haug's Roman reading under it, manuscript variants at the foot.

Aids, none of them the text: the scan's OCR of the Roman lines (`source/raw/haug1872-text-ocr.txt`, words only)
and of Haug's English (`source/raw/haug1872-english-ocr.txt`, a check on the sense, never wording). No modern
edition or translation (Gignoux 1984, Vahman 1986, or any online transcription) is opened or recalled for
wording. The standard dictionary's system (MacKenzie, *A Concise Pahlavi Dictionary*, 1971) is the convention
followed for transcription and transliteration; it is a convention, used from knowledge, not a text to copy.

Sentence numbers are Haug's, cited §chapter.sentence. Later editions number differently.

## What the page shows (owner's ruling, 2026-11-18)
- **The script = images of Haug's print**, cut into words that wrap right to left above each unit (`img`).
  Sentence numbers, rings and ornaments are left out. Inscriptional and Psalter Pahlavi letters were tried
  and rejected; do not bring them back.
- **Under it the Latin line**, tappable: `t`, the words as read. The reader's button switches that line to
  `wr`, the letters as written.

## `t` — the words as read
MacKenzie's transcription: vowels a ā e ē i ī o ō u ū; consonants b č d f g γ h ǰ k l m n p r s š t w x y z ž.
Capitals for sentence starts and names only. Punctuation is ours, guided by Haug's. Attached pronouns and the
indefinite -ē are joined with a hyphen (u-š, u-šān, kū-mān, čiyōn-išān, kas-ē, ēk-ē); so are compounds Haug
hyphenates that are one notion (wad-baxt, ǰud-kēš, Ērān-šahr). The linking ī is its own word. Numbers written
as figures in the manuscript are read out (sēsad, haft).

## `w` — the letters as written
The usual transliteration, one group per word of `t`:
- Persian spellings in small letters: ʾ b g d h w z k l m n s p c š t y, and r where the word is spelled with
  the r-form. The standard dictionary spelling is the default (gēhān gyhʾn, kard krt, Ērān ʾylʾn).
- The final stroke is written `'` exactly where Haug's Roman ends in -ŏ or -ô (Aêtûnŏ → ʾytwn', dînô → dyn',
  shatrô → štr'), and not otherwise.
- Aramaic word-signs in capitals with MacKenzie's letter values (A aleph, E he, H heth, O ayin, C sadhe).
  Haug's Roman gives the word-sign by its traditional Parsi reading; the common ones:

  | Haug | written | read | | Haug | written | read |
  |---|---|---|---|---|---|---|
  | va | W | ud | | pavan | PWN | pad |
  | -i | Y | ī | | min | MN | az |
  | aîgh | AYK | kū | | val | OL | ō |
  | mûn | MNW | kē | | madam | MDM | abar |
  | amat | AMT | ka | | yîn | BYN | andar |
  | hat | HT | agar | | levatman | LWTE | abāg |
  | vad | OD | tā | | barâ | BRA | be |
  | lâ | LA | nē | | al | AL | ma |
  | zak | ZK | ān | | denman | ZNE | ēn |
  | valman | OLE | ōy | | valmanshân | OLEšʾn | awēšān |
  | li | L | man | | lanman | LNE | amā |
  | lekûm | LKWM | ašmā | | nafshman | NPŠE | xwēš |
  | benafshman | BNPŠE | xwad | | akhar | AHL | pas |
  | afash | APš | u-š | | afshân | APšʾn | u-šān |
  | adîn | ADYN | ēg | | kolâ | KRA | harw |
  | kabed | KBD | was | | zakâî | ZKʾy | any |
  | mandavam | MNDOM | tis | | shem | ŠM | nām |
  | anshûtâ | ANŠWTA | mardōm | | gabrâ | GBRA | mard |
  | nêshman | NYŠE | zan | | shapîr | ŠPYL | weh |
  | saryâ | SLYA | wad | | shanat | ŠNT | sāl |
  | mayâ | MYA | āb | | zahabâ | ZHBA | zarr |
  | babâ | BBA | dar | | tôrâ | TWRA | gāw |
  | yadman | YDE | dast | | ragelman | LGLE | pāy |
  | shêdâ | ŠDYA | dēw | | milayâ | MRYA | saxwan |
  | khadîh | AYŠ | kas | | aît | AYT | ast |
  | hômand | HWEnd | hēnd | | yehevûn- | YHWWN- | būdan, baw- |
  | yemalelûn- | YMRRWN- | guftan, gōw- | | vazlûn- | OZLWN- | šudan, šaw- |
  | yâtûn- | YATWN- | āmadan, āy- | | yâîtyûn- | YHYTYWN- | āwurdan, āwar- |
  | yâmtûn- | YHMTWN- | rasīdan, ras- | | yedrûn- | YBLWN- | burdan, bar- |
  | yehabûn- | YHBWN- | dādan, dah- | | khavîtûn- | YDOYTWN- | dānistan, dān- |
  | yekavîmûn- | YKOYMWN- | ēstādan, ēst- | | yetîbûn- | YTYBWN- | nišastan, nišīn- |
  | hankhetûn- | HNHTWN- | nihādan, nih- | | ramîtûn- | LMYTWN- | abgandan, abgan- |
  | zektelûn- | YKTLWN- | ōzadan, ōzan- | | neksûn- | NKSWN- | kuštan, kuš- |
  | bavîhûn- | BOYHWN- | xwāstan, xwāh- | | karîtûn- | KLYTWN- | xwandan, xwān- |
  | mekadlûn- | MKBLWN- | padīriftan, padīr- | | medammûn- | MDMEN- | sahistan, sah- |
  | zerkhûn- | YLYDWN- | zādan, zāy- | | tebrûn- | TBLWN- | škastan, škenn- |
  | khadûk | ʾywk | ēk | | khadû- | ʾyw- | ēw- |

  A verb's word-sign takes Persian endings in small letters: -t / -st past (YHWWNt būd, YTYBWNst nišast),
  -d 3 pl. (YMRRWNd gōwēnd), -yt 3 sg. and 2 pl. (OZLWNyt šawēd), -m 1 sg., -ym 1 pl., -ʾt (YKOYMWNʾt ēstād).
  Haug writes the past with ḍ and the 3 pl. with d. His -yîsh at a word's end is the adverb ending -īhā (-yhʾ).
- Figures in the manuscript stay figures (300, 7, 3; the -1 of AYŠ-1 kas-ē and ʾywk-1 ēk-ē).
- A word-sign not in this table: identify it from Haug's Roman, the Pahlavi type and the sense, write it by
  the same system, and add it to the table in the same commit. If it cannot be identified with confidence,
  write the group in small letters as the type shows it and say so in the unit's note.
- Two spellings in chapter 1 are a best reading of the type and are open: *did* (TNYD; Haug "tanid") and the
  second *sē* (TLTAk; Haug "telatâk"). Keep them as they are until someone settles them.

## Haug's readings and later corrections
- Where Haug's *reading* of the same letters has been given up, `t` has today's reading and the note says so
  the first time (Vîrâf → Wirāz; nîyâzânînîḍ → wiyābānēnīd; Frôbâg → Farnbāg; khadûk → ēk). His reading of a
  name never goes into `l` or `i`.
- Where later editors *correct the manuscripts*, `t` keeps Haug's print and the note gives the correction
  (ch. 1: pad sāxt → passāxt; Šaspīgān → šēbišn; xwadāy-ōmand → andōhōmand). Give such a correction only
  where you are sure of it; never look one up in a modern edition.
- Clear misprints follow the pipeline's rule 5b. Uncertain words are marked (?) in `l`, `i` and the glossary.

## Translation
Two layers as everywhere. Verb-final order kept in `l`; attached pronouns shown hyphenated ("And-he",
"as-to-them"). Names in their Middle Persian form (Zardušt, Wirāz, Ādurbād, Srōš, Ādur, Ohrmazd, Ahriman;
Ērān-šahr → "the land of Iran" in `i`). Verbs kept for evil beings get their own English verb (dwāristan
"scuttle"). Recurring patterns are flagged once per chapter at most, then left: be + verb, ī, u-š / u-šān,
rāy, kū, -īh, -išn, -īhā, -tar. Notes point out word-signs a reader of Hebrew or Aramaic will recognise,
once each across the work (already done: ŠM, PWN, MYA, ZHBA, TWRA, KLYTA, BBA, ANŠWTA, MNDOM, MRYA, AYŠ, ŠDYA,
GBRA, MNW, NPŠE, LKWM, ŠPYL, LGLE, YDE, AL, L).

House renderings: ahlaw "righteous"; druwand "wicked"; Gannāg Mēnōg "the Foul Spirit" (`i`: "the Evil
Spirit"); gizistag "accursed"; dēn "religion"; yazdān "the gods"; mēnōg "spirit, spirit world"; dušox "hell";
ruwān "soul"; dastwar "high priest"; māzdēsn "Mazda-worshipper"; humat, hūxt, huwaršt "good thought, good
word, good deed".

## Hell (chapters 17–100)
The punishments are graphic and many concern sexual conduct. Never bowdlerise: `l` and `i` say what the text
says, in plain words. A part whose content calls for it carries `advisory` in units.json (`lede`: one plain
sentence naming what the part shows; `more`: two or three sentences of context), by the project's
content-advisory rules. If there is a passage you will not translate, follow the pipeline README's rule 7:
leave out the smallest piece, mark the gap, publish the rest.

## Glossary
Keyed by the read form, lowercased, as the reader splits words. Entries: "lemma — meaning (grammar)"; verbs
under the infinitive with the present stem ("guftan, gōw- — to say (present, 'they say')"). How a form is
written is added by the build from `w` (`spellings.json`), so entries never state it.

## Open
1. No voice. 2. No letter-by-letter check of `w` against the type. 3. Word images are not linked to
glossary words. 4. Haug's italics (words not in all his manuscripts) are not marked.

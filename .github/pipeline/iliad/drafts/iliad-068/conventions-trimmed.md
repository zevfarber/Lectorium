# TRIMMED CONVENTIONS for iliad-068 (rules in full; house-rendering tables filtered to rows sharing a word with this part)

## ODYSSEY CONVENTIONS (rules)

# Homer, *Odyssey* — conventions (pilot, 2026-09-20; house renderings as revised at review)

The language-level Greek choices are those of `claude/greek-aesop-conventions.md` and are not
reopened here: pronunciation **reconstructed Attic after Allen, *Vox Graeca***; the `tr` scheme;
elision apostrophe **U+2019**; ano teleia **U+00B7**; `langCode: null`; `script: "greek"`;
`trStyle: "line"`. Everything below is what Homer adds.

## Edition of record

**A. T. Murray, *Homer: The Odyssey*, Loeb Classical Library (London: Heinemann; New York: Putnam,
1919)** — Greek text only. Pre-1930, public domain everywhere. Machine-readable copy: Perseus TEI
`PerseusDL/canonical-greekLit`, `tlg0012.tlg002.perseus-grc2.xml`. Murray's **English** translation
is printed in the same volume and is public domain; under the KJV rule it may be consulted silently
as a meaning-check on a hard passage, never for wording, and never shipped.

Text kept exactly as the archive prints it: no quotation marks round speeches (Murray prints none),
lower-case line openings, `ἐύ-` and `ἐυ-` without a printed diaeresis, the archive's accents. Only
two mechanical normalisations: U+02BC → U+2019 for the elision mark, and NFC.

## Sectioning

The 24 books are the authentic division and are the manifest `group` ("Book 1"). Inside a book the
parts are cut **only at paragraph breaks Murray prints** (1,162 in the poem), aiming at ~100 lines.
Part ids `odyssey-NNN` in poem order, `seq` on every manifest entry. `part` = our own English name
for the stretch plus the citation: `The Gods in Council (1.1–95)`. Arabic book numeral, Arabic lines.

## Verse and segmentation

- Verse stays verse: lines inside `t` joined by `\n`, `v: true`, `ln` = the line the unit starts on.
- **The tap-unit is the punctuated sense-unit**: it ends at a full stop, a Greek question mark `;`
  or an ano teleia `·`. Never at a comma, unless a period would otherwise run past **four lines** —
  then cut at the comma where the syntax pauses most.
- A unit may begin or end **mid-line** (1.19, 1.26, 1.57, 1.59, 1.60). The piece of the line that
  belongs to the unit goes in its `t`; the rest of the line opens the next unit. No character of the
  source is dropped, added or moved: the units' `t`, joined in order, must reproduce the archive.
- `p: true` on the first unit of each of Murray's paragraphs.
- **`mark`** (the quiet italic line above a unit) is used at the first unit of every speech, because
  Murray prints no quotation marks: `Zeus speaks`, `Athena answers`. English layers carry ordinary
  “ ” quotation marks round speech; the Greek does not, and `tr` follows the Greek.

## The two English layers

- `l` follows the Greek order as far as English can bear and keeps the **same line division as `t`**
  (one `\n` for each `\n` in `t`). Coherence wins ties. Hyphenate a compound where that shows how it
  is built (`many-turning`, `cloud-gatherer`), sparingly.
- `i` is real English prose, lightly elevated, never archaic for its own sake, never childish. No
  `\n` in `i`.
- **A repeated line gets the same English every time.** Homer's repetitions are the poem's method,
  and the reader should hear them. Lines 1.44 = 1.80 and 1.45 = 1.81 in this very part. In
  production this is enforced mechanically (first ratified rendering wins).
- Stock epithets are **translated every time, the same way every time**, even where they sit oddly
  with the context (*blameless* Aegisthus). The note says so once; the translation never quietly
  drops or varies them.
- Proper names in English take their familiar forms (Odysseus, Calypso, Aegisthus, Athena, Zeus,
  Poseidon, Orestes, Hermes, Polyphemus, Ithaca, Ogygia, Cronus, Penelope, Nestor, Menelaus, Ilus son
  of Mermerus, Ephyra, Dulichium, Same, Zacynthus, Pylos, Sparta, Patroclus, Antilochus, Priam,
  Diomedes, Idomeneus, Philoctetes; the Harpies — Murray prints ἅρπυιαι
  as a common noun, but the English capitalises it and the note explains it as "snatchers", the
  storm-winds). `tr` carries the Greek form.
- Never bowdlerize.

## Homeric Greek for a reader who knows some Attic (or none)

Flag on first occurrence in a part, then only nudge:

- **No augment**: `πάθεν`, `ἴδεν`, `φύγον`, `τέκε` are ordinary past tenses without the ἐ-.
- **The "article" is a pronoun**: `ὁ`, `τόν`, `τοῖσιν` mean *he, him, to them*; `τοί` can be relative.
- **Genitives** in `-οιο` (= -ου) and `-αο`/`-εω` (= -ου, 1st decl.); **datives** in `-ῃσι(ν)`,
  `-οισι(ν)`, `-εσσι(ν)`.
- **Uncontracted forms**: `ἡμέων`, `νέεσθαι`, `μνάασθαι`, `αἰτιόωνται` (diectasis).
- **Infinitives** in `-έμεν`, `-έμεναι`, `-μεναι` (`ἔμμεναι` = εἶναι, `ἐριδαινέμεν`).
- **Particles**: `κε(ν)` = ἄν; `ῥα`, `ἄρ`, `νυ`, `περ`, `τε` "epic τε" marking a general truth.
- **Possessive `ὅς, ἥ, ὅν`** = *his/her own* (`ὃν κατὰ θυμόν`, `ἣν γαῖαν`), easily mistaken for the relative.
- **Tmesis**: a preverb standing apart from its verb (`κατὰ … ἤσθιον`, 1.8–9).
- **`-δε`, `-θεν`, `-θι`, `-φι`** suffixes of direction and place (`οἶκόνδε`, `ἁμόθεν`, `Ἰθάκηνδε`).
- Ionic `η` for Attic long `ᾱ` (`Τροίης`, `αἴης`); `ἐς`/`εἰς`, `ἐνί`/`ἐν`, `αἰεί`/`ἀεί`.

The glossary names the **dictionary form as LSJ lemmatises it**, and where the Homeric form is far
from the Attic one says so: `ἔμμεναι` → `εἰμί — to be; pres. inf., epic (= Attic εἶναι)`.

## Sole-source rule and lexical aids

Draft from Murray's Greek plus, from your own knowledge, the public-domain aids: **LSJ 8th ed.
(1897)**, **Autenrieth, *Homeric Dictionary* (1891)**, **Cunliffe, *Lexicon of the Homeric Dialect*
(1924)**, **Monro, *Homeric Grammar* (2nd ed. 1891)**, **Smyth (1920)**. Nothing else open.

Modern translations are in copyright and distinctive — Lattimore, Fitzgerald, Fagles, Lombardo,
Mandelbaum, Rieu, Mitchell, Verity, Green, Wilson, Mendelsohn. Never consult them. If an English
phrase arrives fully formed, suspect it: rebuild the rendering from the case relations.

Words whose meaning is not actually known are **said to be unknown** in the note, not papered over:
`ἀργεϊφόντης`, `διάκτορος`, `ἀτρύγετος`, `ἀμύμων`, `ἠλίβατος`, `μέροπες` and their like.


## Odyssey house renderings — filtered rows

## House renderings — fixed before drafting

| Greek | `l` | `i` | avoided on purpose |
|---|---|---|---|
| αἰπὺς ὄλεθρος (1.11, 1.37) | "steep destruction" | "steep destruction" | "sheer destruction" |
| δῖος (of Odysseus) | "heavenly" | "heavenly" | "divine" (reserved for θεῖος), "goodly", "brilliant", "noble" |
| Ὀδυσσῆος φίλος υἱός | "Odysseus’ dear son" | "the dear son of Odysseus" | "Odysseus’ own son", "beloved son" |
| ἥρως (as title) | "the hero" | "the hero" | "lord", "warrior", "old soldier" |
| Γερήνιος ἱππότα Νέστωρ (Nestor's standing name-epithet, 3.68) | "the Gerenian horseman Nestor" | "the Gerenian horseman Nestor" (+ note: meaning of Γερήνιος disputed — Gerenia/Gerenon in Messenia, or γέρων / γέρας) | "old Nestor", "the aged Nestor", "honoured Nestor" (each silently picks one disputed etymology); "charioteer", "horse-driver", "knight", "lord of horses" for ἱππότα |
| ὦ Νέστορ Νηληϊάδη, μέγα κῦδος Ἀχαιῶν (whole-line vocative address, 3.79) | "O Nestor, son of Neleus, great glory of the Achaeans," | "Nestor, son of Neleus, great glory of the Achaeans," | "Neleides", "pride of the Achaeans", "great boast of the Achaeans" |
| ἀρήιος (3.109, 3.167) | "warlike" | "warlike" | "war-loving", "martial" (too Latinate) |
| φαίδιμος (3.189, "φαίδιμος υἱός") | "glorious" | "glorious" | "shining", "splendid" (reserved for ἀγλαός) |
| ὦ φίλος (nominative as vocative, 3.375; cf. ὦ φίλ’ shipped at 3.103, 3.211) | "O friend" | "Friend" | "My dear boy", "my friend" in `i` (kept to the shipped ὦ φίλ’ pattern); plain φίλος in καὶ σύ, φίλος stays "friend" / "my friend" as shipped at 1.301, 3.199 |
| δόρυ (6.167, of the palm's stem, ἐκ δόρυ γαίης) | "trunk" | "trunk" | "spear", "shaft" (both lose the tree), "timber" |
| δαίμων (6.172, ἐνθάδε κάββαλε δαίμων, an unnamed divine power) | "a power" | "some power" | "a god" (reserved for θεός), "spirit", "demon", "fortune", "fate" (reserved for μοῖρα / πότμος) |
| κρατερὴ ὑσμίνη (11.417) | "strong battle" | "strong battle" | "mighty" (reserved for ἴφθιμος), "fierce" (kept for ἄγριος), "hard" (reserved for tasks), "stern" |

χειρί τέ μιν κατέρεξεν ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν (4.610, fixed with a male subject) now also covers a female
subject (Calypso, 5.181): the English pronoun tracks the speaker's sex ("stroked him with her hand"), exactly as
the ὣς φάτο row already does.

ἅλα δῖαν (5.261, μοχλοῖσιν δ’ ἄρα τήν γε κατείρυσεν εἰς ἅλα δῖαν): from odyssey-024 on, δῖος applied to the sea
keeps "heavenly" in *both* `l` and `i`, per row 274 above. This is not a retroactive fix: 3.153 keeps its shipped
"heavenly brine" / "bright salt sea", and 4.577 keeps its shipped "bright sea" in `i` — both left as shipped, the
inconsistency already noted at row 274.
| ἄγρει δή (21.176) | "Come now," | "Come now," | follows the table’s ἀγρεῖθ’ "Come," with δή "now" added |

## Glossary entries

One shared file, `odyssey-glossary.json`; keys are lowercased word forms exactly as printed (an elided
form without its apostrophe: `δ`, `ἀλλ`, `ἔφαθ`). One entry per form, general to the form and never
pinned to a line: `<dictionary form as LSJ lemmatises it> — <terse meaning>; <parse>`.

    "θεοὶ": "θεός — god; nom. pl."
    "ἔμμεναι": "εἰμί — be; pres. inf., epic (= Attic εἶναι)"
    "πάθεν": "πάσχω — suffer, experience; aor. 3 sg., unaugmented (= ἔπαθεν)"
    "τὸν": "ὁ, ἡ, τό — he, she, it; that (in Homer a pronoun; later the article); masc. acc. sg. ’him’"
    "ὃν": "ὅς, ἥ, ὅν (possessive) — his own, her own; masc./neut. acc. sg. · also relative ὅς, ἥ, ὅν: whom, which (masc. acc. sg.)"
    "δ": "δέ (elided δ’) — and, but"

English inside an entry is quoted with the typographic ’ … ’, never an ASCII apostrophe or a backtick.
A word of unknown or disputed meaning says so. Additions only: the first entry to land stands, and a
later part may broaden it (old entry whole, then ` · ` and the new reading), never replace it.

## Notes (`n`)

What a tutor would point at: the Homeric form and its Attic equivalent, the construction, the
formula and what it is doing, the cultural fact. Quote Greek bare (no backticks), English glosses in
single quotes. A note asserts nothing about the rest of the poem that this part cannot show, and
makes no claim about where a word stands in its line without checking the line. Metre is mentioned
only where it explains a form (`πτολίεθρον`, `Ὀδυσσῆος` beside `Ὀδυσῆος`); the scansion display
carries the rest. Note density: most units carry one.

## Scansion

Every line is scanned by `scan_hexameter.py`; the result ships in the story as `sc` (one string per
word token: optional foot digit, syllable letters, then `–` long, `⏑` short, `×` the final
indifferent syllable; `‖` after the word that precedes the main caesura). A line the script cannot
fit without a flagged licence (metrical lengthening, a long scanned short) is settled by a person or
the reviewing agent and recorded. The reader shows it only when the Scansion toggle is on.
| ἐπ’ ἐσχατιῇ (9.182) | "at the edge" | "at its edge" | "at the far end", "on the outskirts" |
|---|---|---|---|
| πότνια μήτηρ (11.180) | "the lady mother" | "my lady mother" | "revered mother", "queen mother" (reserved for ἄνασσα); follows πότνια νύμφη "the lady nymph" |
| θεράπων of Pelias and Neleus (11.255) | "attendants" | "attendants" | "servants" (reserved for δμῶες), "squires", "henchmen"; follows the table's ὀτρηρὸς θεράπων "brisk attendant" |
| ἐπιμίξ (11.537; rare adverb) | "in confusion" | "in confusion" | "indiscriminately", "pell-mell", "in a mêlée" (all more specific than the root μίγνυμι "mix") |
| κεφαλή as a periphrasis for the person (11.549 τοίην γὰρ κεφαλήν; 11.557 Ἀχιλλῆος κεφαλῇ) | "head" | "such a man" (549) / "Achilles … himself" (557) | "life", "dear one" (add what the Greek does not say); same device as the table's ἱερὴ ἲς Τηλεμάχοιο, but `i` names the person because "head" alone reads as a body part in English |
| ἆ δείλ’ (cry of address, 11.618) | "oh, miserable one" | "oh, miserable man" | "ah" (reserved for ὢ πόποι), "alas", "poor wretch"; δειλός keeps the table's "miserable" |
| κῆρα μέλαιναν (15.275, with θάνατον) | "black death-fate" | "the black spirit of death" | "black doom", "dark fate" (reserved for μοῖρα / πότμος); follows the table's κὴρ θανάτοιο "death-spirit" and ἔκφυγε κῆρα "escaped death-fate" |
|---|---|---|---|
|---|---|---|---|
| ὦ φίλος (vocative, 17.17) | "O friend" | "Friend" | "O dear one", "my friend" in `i`, "dear sir", "good fellow"; follows the table row ὦ φίλος (nominative as vocative); ξεῖνε φίλε stays "Dear stranger" |
| ἐγγύθεν ἦλθεν (17.71) | "from close by came" | "came up from close by" | "from near", "came near", "approached"; follows the shipped "from close by" (odyssey-033, -035, -037) |
| δῖοι Ἀχαιοί (19.199) | "the heavenly Achaeans" | "the heavenly Achaeans" | "divine" (reserved for θεῖος), "noble", "brilliant", "goodly"; δῖος keeps the table's "heavenly" in the plural, as for places and for Odysseus |
| εὖχος (22.7, πόρῃ εὖχος) | "a boast" | "the triumph" | "glory" (reserved for κῦδος), "renown" (κλέος), "vaunt" |
| σάκος (22.101, 110, 122, 144, 184) | "shield" | "shield" | "buckler", "targe"; the plural σάκε’ is "shields" |


## ILIAD CONVENTIONS

# Homer, *Iliad* — conventions (pilot, 2026-10-12)

The Iliad is read exactly as the Odyssey is. **Everything in `../odyssey/conventions.md` applies here** —
language-level choices (reconstructed Attic after Allen, *Vox Graeca*; the `tr` scheme; U+2019 elision;
U+00B7 ano teleia; `langCode: null`; `script: "greek"`; `trStyle: "line"`), verse and segmentation,
the two English layers, the Homeric-Greek flags, the sole-source rule and lexical aids, the glossary-entry
format, notes, scansion — and **its house-renderings table is binding for the Iliad too**: a formula or
epithet the Odyssey has fixed keeps its English here. The scanner (`scan_hexameter.py`) and the
transliterator (`translit_grc.py`) are the Odyssey's own, imported, not copied. Below is only what the
Iliad changes or adds.

## Edition of record

**D. B. Monro and T. W. Allen, *Homeri Opera*, tomi I–II (Iliad), 3rd ed. (Oxford Classical Texts;
Oxford: Clarendon Press, 1920)** — Greek text only. Pre-1930, public domain everywhere. Machine-readable
copy: Perseus TEI `PerseusDL/canonical-greekLit`, `tlg0012.tlg001.perseus-grc2.xml` (TEI sha256
`ae8b617018c6e5af14cbab9ce6082438c0f103eafd0a4c67bdae4588cca5eaa4`), archived by `archive_iliad.py` into `source/iliad-monro-allen1920.json`.
There is no public-domain English printed with it; for a meaning-check on a hard passage, the old
public-domain translations (e.g. Murray's Loeb Iliad, 1924) may be consulted silently under the KJV rule,
never for wording, never shipped.

Text kept exactly as the archive prints it, with the Odyssey's two mechanical normalisations (U+02BC →
U+2019 for elision, NFC). The OCT prints the diaeresis (`ἐϋκνήμιδες`, `ἠΰκομος`, `ὀϊστοί`) and
prints `ἤτοι` as one word and `τοὶ γάρ` as two; keep all of these as printed. No quotation marks round
speeches, as in Murray.

Known features of this archive (from `archive_iliad.py`):
- 9.458–461 are not in the text (the edition gives them only in the apparatus); numbering jumps 457 → 462.
- Numbering also jumps at 11.542 → 544 and 14.268 → 270.
- 8.548 and 8.550–552 are printed in square brackets (athetized); the archive keeps them inside `[ ]`.
  The reader's word regex ignores the brackets. The note on the unit says what the brackets mean.

## Sectioning

The 24 books are the authentic division and the manifest `group` ("Book 1"). Inside a book the parts are
cut **only at paragraph breaks the edition prints** (1,055 in the poem), aiming at ~100 lines: 159 parts
(median 98 lines). Three parts fall outside the 55–135 band because the edition's paragraphs leave no
better cut: 9.430–605 (172 lines, Phoenix's speech), 11.655–803 (149, Nestor's tale) and 11.804–848 (45).
Part ids `iliad-NNN`, `seq` on every manifest entry; `part` = our English name + citation,
`The Wrath and the Plague (1.1–100)`.

## The three names of the army — a departure from the Odyssey

The Odyssey's `i` layer renders Δαναοί as "Greeks". **The Iliad does not**: Ἀχαιοί "Achaeans",
Δαναοί "Danaans", Ἀργεῖοι "Argives" in both layers, always, because the Iliad alternates the three
constantly and the reader should hear which one the poet chose. "Greeks" is used in neither layer.

## Sharing English with the Odyssey

`packet.py` lists every line of a part that already stands in a published Odyssey unit, with its English,
and `validate_iliad.py` warns (does not fail) when an Iliad unit has the same Greek as an Odyssey unit
but different English. Reuse the Odyssey's English unless the Iliad context forbids it; a departure is
recorded in the part's `new-renderings.md` with the reason. Inside the Iliad, the Odyssey's hard rule
holds: the same Greek gets the same English (enforced by the validator).

## House renderings — Iliad additions (fixed at the pilot, 2026-10-12)

The opening is our own. "Wrath" for μῆνις is the old, pre-modern rendering, chosen because the word is
specifically a lasting, god-sized anger (Calchas uses it of Apollo at 1.75), and because "rage" and
"anger" are the distinctive choices of the best-known modern versions.

| Greek | `l` | `i` | avoided on purpose |
|---|---|---|---|
| μεγάθυμοι Ἀχαιοί (1.123) | "great-hearted Achaeans" | "great-hearted Achaeans" | "high-spirited", "stout-hearted"; follows the Odyssey's μεγάθυμος "great-hearted" |
| ποθή (1.240, ποθὴ ἵξεται) | "a lack of Achilles" | "the lack of Achilles" | "longing", "yearning", "regret"; follows the table’s ξενίων ποθή "no lack of hospitality" |
| ἱπποδάμοιο (Ἀτρέος … ἱπποδάμοιο, 2.23) | "horse-taming" | "tamer of horses" | follows the table’s ἱππόδαμος Νέστωρ; δαΐφρονος keeps "wise-minded" / "wise-hearted" from the table’s δαΐφρων row |
|---|---|---|---|

| Τελαμώνιος Αἴας | "Telamonian Ajax" | "Telamonian Ajax" | "Ajax son of Telamon", "greater Ajax"; the adjective is kept to tell the two Ajaxes apart, with ταχὺς Αἴας Ὀϊλῆος "swift Ajax, son of Oileus" |
| μένεα πνείοντες (2.536) | "breathing might" | "breathing might" | "breathing strength" (the Odyssey’s 22.203; a departure, with the reason: the Iliad has μένος "might" at 2.387 and keeps "strength" for κράτος and σθένος), "breathing fury" (reserved for μένος of anger), "breathing courage" |
| αἶψα · αὐτίκα (2.662, 2.664) | "quickly" · "at once" | "quickly" · "at once" | the Odyssey table’s αἶψα "quickly" and αὐτίκα "at once", kept apart in two lines that stand next to each other |
| ἀρήϊος (Πρωτεσίλαος ἀρήϊος, 2.698, 2.708) | "warlike" | "warlike" | "martial", "valiant", "of Ares"; the Odyssey ships "warlike" (odyssey-010), and "steadfast in battle" is reserved for μενεπτόλεμος |
| κάρηνα (Τιτάνοιό τε λευκὰ κάρηνα, 2.735) | "peaks" | "peaks" | "heads" (kept for the Iliad's cities at 2.117 and the Odyssey's "heads" of the dead), "summits"; κάρηνα of mountains is "peaks", as in the Odyssey's ὀρέων … κάρηνα |
| πεζοί θ’ ἱππῆές τε (2.810) | "both on foot and horsemen" | "both on foot and mounted" | "infantry and cavalry", "foot-soldiers and charioteers"; the Odyssey’s wording (odyssey-115) |
|---|---|---|---|
| δῖος Ἀλέξανδρος (3.329, 3.352) | "heavenly Alexander" | "heavenly Alexander" | "godlike" (ἀντίθεος), "noble", "divine"; the table’s δῖος "heavenly" is kept even where it sits oddly, in the mouth of Menelaus, and the note says so once |
| ὁμίλου (ἑκάτερθεν ὁμίλου, 3.340) | "the throng" | "the throng" | "the crowd", "the company", "the press"; follows the shipped odyssey-082 "the great throng" |
| ἠρήρειστο (3.358) | "it was driven" | "was driven … as well" | "was fixed", "was lodged", "was thrust"; ἐρείδω "press, drive" |
| δίφρον (of a seat, 3.424) | "stool" | "stool" | "chair" (reserved for θρόνος), "seat" (reserved for κλισμός), "chariot" (the same word in 3.262 and 3.312; context tells them apart) |
| ἔασε (4.226) | "had left" | "had left" | "let be", "allowed" (the Odyssey’s ἔασε "allowed" with an infinitive), "abandoned"; with a plain object the verb is "left" |
| μάλα (τοὺς μάλα θαρσύνεσκε, τοὺς μάλα νεικείεσκε, 4.233, 4.241) | "greatly" | "heartily" (of cheering) · "sharply" (of reviling) | "very much", "loudly", "bitterly" (reserved for πικρός); μάλα is "greatly" in `l` and gets the adverb the verb needs in `i` |
| δαΐφρονα (Ἰδομενῆα, 4.252) | "wise-minded" | "wise-hearted" (+ note: "wise" or "fierce" disputed) | "warlike", "of the fierce mind", "sage"; follows the Odyssey table’s δαΐφρων (the note states the doubt) and iliad-008’s δαΐφρονος |
| ἀϋτή (4.328, 4.331) | "battle-cry" | "battle-cry" | "shout", "clamour"; kept apart from βοή "war-cry" (βοὴν ἀγαθός) |
| φαίδιμος Ἕκτωρ (4.505) | "glorious Hector" | "glorious Hector" | "shining", "splendid" (reserved for ἀγλαός); follows the Odyssey table’s φαίδιμος "glorious" |
| κῆρα μέλαιναν (5.22) | "the black death-fate" | "the black spirit of death" | follows the table (15.275) |
| ἀναχωρήσας (5.107) | "stepping back" | "stepping back" | "retreating", "withdrawing"; follows odyssey-086 "drawing back" |
| μώνυχας ἵππους (5.236; μώνυξ "with an undivided hoof") | "solid-hoofed horses" | "the solid-hoofed horses" | "single-hoofed" (reads as one hoof per animal), "whole-hoofed", "strong-hoofed"; the Odyssey table’s μώνυχες ἵπποι, unchanged |
| κῆδε (5.400, ἔκηδε 5.404) | "distressed" | "distressed" | "troubled" (the weaker word, and not the one the note gives for κήδω), "grieved" (kept for ἀχέω), "wounded"; one English verb for the imperfect of transitive κήδω at both lines, apart from κήδομαι "be troubled" |
| εὖχος … δώσειν (5.654) | "a boast … will give" | "will give me the triumph" | "glory" (reserved for κῦδος), "boast" in `i`; `l` follows the table's εὖχος ἔδωκας (5.285) and `i` the Odyssey's "the triumph" (22.7) |
| Ἄϊδι κλυτοπώλῳ (5.654; the reason for the epithet not known) | "Hades of the famous horses" | "Hades of the famous horses" | "of the famed steeds", "famed for horses"; κλυτός "famous" (δουρὶ κλυτός 2.645), πῶλος "foal, horse" |
| ἄντυγες (5.728) | "rails" | "rails" | "rims", "rings"; ἄντυξ keeps the "rail" of 5.262 |
|---|---|---|---|
| ἱπποδάμοιο (Ἀντήνορος, 6.299) | "horse-taming" | "tamer of horses" | follows the table’s ἱππόδαμος / ἱπποδάμοιο (2.23) |
| ἰῷ ἤματι (6.422) | "on one day" | "on a single day" | "in one day", "on the same day"; ἰῷ = ἑνί |
| ἀμφί + accusative (6.436–437) | "around" | "gathered around" | "led by", "with", "under"; ἀμφί "around", the leaders named with their followers understood |
| Greek | `l` | `i` | avoided on purpose |
| ὣς φίλον ἔπλετο θυμῷ (7.31) | "so it has been dear to the spirit" | "it has so pleased the spirit of" | "it is the will of" (the Odyssey table avoids "will"), "your hearts are set on" |
| φάλαγγας (7.141) | "battle-lines" | "battle-lines" | follows iliad-041 (7.54) |
| κοίρανε λαῶν (7.234, vocative) | "ruler of the people" | "ruler of the people" | "lord of the host", "leader of men", "commander" (ἄναξ ἀνδρῶν is "lord of men", ποιμὴν λαῶν "shepherd of the people"); keeps κοίρανος "ruler" |
| Αἶαν διογενὲς Τελαμώνιε (7.234) | "Ajax, Zeus-sprung, Telamonian" | "Zeus-born Ajax, Telamonian" | "Ajax son of Telamon", "scion of Zeus"; the table's διογενής pair "Zeus-sprung" / "Zeus-born" and Τελαμώνιος "Telamonian" |
| πάντοσ’ ἐΐσην (7.250) | "equal on every side" | "equal on every side" | the table's πάντοσε ἴσην, unchanged (ἐΐση is the longer form of the same word) |
| ἐγγύθεν ἦλθε (7.219) | "from close by came" | "came up from close by" | "came near", "approached", "came close"; the Odyssey table's ἐγγύθεν ἦλθεν (17.71), unchanged |
|---|---|---|---|

|---|---|---|---|
| κακὸν ἦμαρ (9.251) | "the evil day" | "the evil day" | "day of doom", "the day of ruin"; not the same as αἴσιμον ἦμαρ "fated day" |
| καλλίτριχας ἵππους (8.503) | "fair-maned horses" | "fair-maned horses" | follows the Odyssey’s καλλίτριχες ἵπποι (3.475) unchanged |
| ἐσχατιή (9.484) | "the edge" | "the edge" | "the border", "the far end"; follows the Odyssey’s ἐπ’ ἐσχατιῇ "at the edge" (9.182) |
| θυμὸν μέγαν (9.496) | "great spirit" | "great spirit" | "great heart" (θυμός is "heart" elsewhere, and the departure is made because ἦτορ "heart" follows in the next unit, as the Odyssey table does at 8.204), "proud heart", "mighty heart" |
| Ἄρηϊ (διαπραθέειν μεμαῶτες Ἄρηϊ, 9.532) | "in war" | "in war" | "with Ares", "to the god of war" (the name stands for war, and the note says so) |
| ἄρηι φίλος (9.550) | "dear to Ares" | "dear to Ares" | "beloved of war", "war-loving"; follows ἀρηΐφιλος "dear to Ares" (2.778) |

| μέρμερα (10.48, bare neuter plural; the table has μέρμερα ἔργα "baneful deeds", 8.453) | "baneful things" | "baneful things" | "grievous", "cruel", "dreadful"; follows the table's "baneful" |
| τέλος (Θρῃκῶν ἀνδρῶν τέλος, 10.470) | "company" | "company" | "end" (the table's τέλος θανάτοιο), "troop", "host", "band"; τέλος here is a body of men |
| ἐπεπωλεῖτο στίχας ἀνδρῶν (τῶν ἄλλων, 11.264) | "was going about the ranks of the other men" | "ranged along the ranks of the other men" | follows the table’s ἐπεπωλεῖτο στίχας ἀνδρῶν (4.231); τῶν ἄλλων "of the other men" added |

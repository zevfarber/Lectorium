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

## House renderings — fixed before drafting

| Greek | `l` | `i` | avoided on purpose |
|---|---|---|---|
| ἄνδρα μοι ἔννεπε, μοῦσα | "The man to me tell-of, Muse" | "Muse, tell me of the man" | "Sing to me of the man", "Tell me about a complicated man", "Sing in me" |
| πολύτροπος | "many-turning" | "of many shifts" | "of twists and turns", "of many ways", "of many turns", "complicated", "resourceful" |
| ἀτασθαλίαι (1.7, 1.34 — the echo is the point) | "wanton-follies" | "wanton folly" | "recklessness", "wild recklessness", "blind folly" |
| νόστιμον ἦμαρ | "the homecoming day" | "the day of their homecoming" | — (generic) |
| δῖα θεάων | "heavenly-one of goddesses" | "heavenly even among goddesses" | "bright among goddesses", "shining among divinities" |
| ἐν σπέσσι γλαφυροῖσι | "in hollow caves" | "in her hollow caves" / "in the hollow caves" | — (generic) |
| πατὴρ ἀνδρῶν τε θεῶν τε | "the father of men and of gods" | same | — (generic, unavoidable) |
| ἀμύμων | "blameless" | "blameless" (+ note at 1.29) | "stately", "handsome", "noble" |
| ὑπὲρ μόρον | "beyond portion" | "beyond what was allotted" | "beyond what is ordained", "beyond their proper share" |
| γλαυκῶπις Ἀθήνη | "gleaming-eyed Athena" | same | "gray-eyed", "bright-eyed", "flashing-eyed", "sparkling-eyed" |
| νεφεληγερέτα Ζεύς | "cloud-gatherer Zeus" | "Zeus who gathers the clouds" | — (generic) |
| ἕρκος ὀδόντων | "the fence of your teeth" | keep the image: "past the fence of your teeth" | "teeth's barrier", "slip through your teeth" |
| ὦ πάτερ ἡμέτερε Κρονίδη, ὕπατε κρειόντων | "O father ours, son-of-Cronus, highest of rulers" | "Father of us all, son of Cronus, highest of those who rule" | "our father Kronides, lord of lords" |
| τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα | "Him then answered" | "Then … answered him" | — |
| τὴν δ’ ἀπαμειβόμενος προσέφη | "Her answering addressed" | "In answer … said to her" | — |
| ἀργεϊφόντης | "Argeïphontes" | "the slayer of Argus" (+ note: meaning disputed) | — |
| διάκτορος | "the guide" | "the guide" (+ note: meaning unknown) | "the courier", "the giant-killer" |
| ἁλὸς ἀτρυγέτοιο | "of the unharvested salt-sea" | "of the sea that yields no harvest" (+ note) | "barren sea", "unresting sea" |
| γαιήοχος / ἐνοσίχθων | "earth-holder" / "earth-shaker" | same | — (generic) |
| ἀντίθεος | "godlike" | "godlike" | — |
| δαΐφρων · πολύφρων · ταλασίφρων (three different epithets of Odysseus in this part — keep them three) | "wise-minded" (δαῆναι reading in both layers; the note states the doubt) · "much-minded" · "enduring-minded" | "wise-hearted" · "of the many counsels" · "steadfast" | collapsing them into one word |
| κάρη κομόωντας Ἀχαιούς | "the long-haired-of-head Achaeans" | "the long-haired Achaeans" | "flowing-haired" |
| εἰλίποδας ἕλικας βοῦς | "rolling-gaited, crumple-horned cattle" | "the cattle of rolling gait and crumpled horn" | "shambling", "longhorn", "horn-curved" |
| μῆλ’ ἁδινά | "thronging sheep" | "his thronging sheep" | — |
| Πύλον ἠμαθόεντα | "sandy Pylos" | same | — (generic) |
| αἰπὺς ὄλεθρος (1.11, 1.37) | "steep destruction" | "steep destruction" | "sheer destruction" |
| ὢ πόποι | "Ah!" | "Ah," | "Oh for shame", "My word" |
| κλέος ἐσθλόν | "good fame" | "a good name" | "noble renown" |
| ἔπεα πτερόεντα προσηύδα | "winged words he spoke" | "spoke winged words" | "words winged and swift", "swift words", "feathered words", "words that fly", "words with wings on them" |
| τὸν δ’ αὖτε προσέειπε | "Him then in turn addressed" | "Then … spoke to him in turn" | "answered" (collapsing three separate reply-formulas into one) |
| ἀλλ’ ἄγε μοι τόδε εἰπὲ καὶ ἀτρεκέως κατάλεξον | "But come, tell me this, and recount it exactly" | "But come now, tell me this, and set it out for me exactly" | "tell me truly" (that is ἐτήτυμον), "tell me the whole truth" |
| χαῖρε, ξεῖνε | "Welcome, stranger" | "Welcome, stranger" | "Hail, stranger", "Greetings, stranger", "Joy to you", "Rejoice" |
| ξεῖνε φίλε | "Dear stranger" | "Dear stranger" | "friend" (drops ξεῖνος), "my dear guest" (drops the strangeness) |
| μνηστῆρες ἀγήνορες | "the lordly suitors" | "the lordly suitors" | "proud", "manly", "high-hearted" |
| πατρώιος ξεῖνος | "a guest-friend from my/our fathers’ time" | same | "hereditary guest", "family friend", "a friend of my father’s" |
| θεοειδής | "godlike-in-form" | "godlike in form" | "godlike" flat (reserved for ἀντίθεος), "of godlike form", "handsome as a god" |
| δῖος (of Odysseus) | "heavenly" | "heavenly" | "divine" (reserved for θεῖος), "goodly", "brilliant", "noble" |
| ὀβριμοπάτρη | "she of the mighty father" | "the daughter of a mighty father" | "mighty-fathered", "child of a mighty sire", "daughter of the Almighty" |
| Ταφίων ἡγήτωρ Μέντης | "Mentes, the Taphians’ leader" | "Mentes, the leader of the Taphians" | "chief", "lord", "prince of the Taphians" |
| φιλήρετμος | "oar-loving" | "oar-loving" | "that love the oar", "seafaring" |
| οἶνοψ πόντος | "the wine-faced open-sea" | "the sea that has the look of wine" | "wine-dark sea", "wine-blue", "the purple sea" |
| ἀλλόθροοι ἄνθρωποι | "men of other speech" | "men of another tongue" | "foreigners", "men of strange speech", "barbarians" |
| αἴθων σίδηρος | "fire-bright iron" | "fire-bright iron" | "gleaming" (reserved for γλαυκῶπις-type words), "flashing", "tawny", "ruddy" |
| πολυμήχανος | "many-devising" | "a man of many devices" | "resourceful", "of many wiles", "never at a loss", "ingenious" |
| φίλη πατρὶς αἶα | "his dear fatherland" | "his dear fatherland" | "his own dear native soil", "his beloved homeland" |
| κοίλῃς ἐνὶ νηυσίν | "in hollow ships" | "in their hollow ships" | "in their curved ships", "in the deep-hulled ships" |
| αἰδοίη ταμίη | "a revered housekeeper" | "a revered housekeeper" | "honoured", "grave", "modest", "the good housekeeper" |
| ὑλήεις | "wooded" | "wooded" | "leafy", "forested", "tree-clad" |
| τὴν/τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα (the fourth reply-formula) | "To her/him in turn prudent Telemachus spoke, face to face:" | "Then prudent Telemachus spoke to her/him in turn, face to face:" | "answered" (reserved for ἠμείβετο), "addressed" (reserved for προσέειπε / προσέφη) |
| πεπνυμένος (of Telemachus) | "prudent" | "prudent" | "thoughtful", "clear-headed", "poised", "sensible", anything in "-minded" (reserved for the -φρων epithets) |
| θεοὶ αἰὲν ἐόντες | "the gods who are forever" | "the gods who are forever" | "the immortal gods" (that is ἀθάνατοι), "the everlasting gods", "the gods who live for ever" |
| θεῶν ἐν γούνασι κεῖται | "lie(s) on the knees of the gods" | same | "rests in the lap of the gods", "is up to the gods", "is in the hands of the gods" |
| νηῦς θοή | "swift ship" | "swift ship" | "fast ship", "quick ship", "sharp ship" |
| κραναὴ Ἰθάκη | "rocky Ithaca" | "rocky Ithaca" | "rugged", "craggy", "rock-strewn" |
| ξανθὸς Μενέλαος | "fair-haired Menelaus" | "fair-haired Menelaus" | "red-haired", "tawny" (reserved for αἴθων), "golden-haired", "blond" |
| Ἀχαιοὶ χαλκοχίτωνες | "the bronze-shirted Achaeans" | same | "bronze-armoured", "bronze-clad", "bronze-mailed" |
| Αἴγισθος δολόμητις | "Aegisthus of guileful counsel" | same | "crafty", "treacherous", "wily" (too generic; none shows μῆτις); kept distinct from the table's ἀμύμων Αἴγισθος "blameless Aegisthus" |
| ἰσόθεος φώς | "a man equal to a god" | "a man the equal of a god" | "godlike" (reserved for ἀντίθεος), "godlike in form" (reserved for θεοειδής), "a man like a god" |
| κατὰ φρένα καὶ κατὰ θυμόν | "in mind and in heart" | "in your/his mind and heart" | "in heart and soul", "in his inmost heart" |
| εἰ δ’ ἄγε νῦν ξυνίει καὶ ἐμῶν ἐμπάζεο μύθων (whole line; second half recurs alone) | "Come now, then, attend, and take heed of my words" | "Come now, attend to me, and take heed of my words" | "mark my words", "listen well" |
| πάντες κ’ ὠκύμοροί τε γενοίατο πικρόγαμοί τε | "all of them would become swift-doomed and bitter-wedded" | "All of them would meet a swift doom and a bitter marriage" | "short-lived" (loses μόρος), "rue their wooing", "would all find …" |
| Παναχαιοί | "the Achaeans all together" | "all the Achaeans" | "the Panachaeans" (an English non-word) |
| ἀμφίαλος Ἰθάκη | "sea-girt Ithaca" | "sea-girt Ithaca" | "island-girt Ithaca", "encircled-by-sea Ithaca" (too free); literal sense is ἀμφί "around" + ἅλς "sea" |
| δῖα γυναικῶν (of Penelope) | "heavenly-one of women" | "heavenly among women" | "bright among women", "shining among women" — kept parallel to δῖα θεάων above rather than treated as a separate formula |
| θεῖος (of Phemius, θεῖον ἀοιδόν) | "divine" | "the divine minstrel" | "godlike" (reserved for ἀντίθεος/θεοειδής), "heavenly" (reserved for δῖος) |
| περίφρων Πηνελόπεια | "circumspect Penelope" | "circumspect Penelope" | "wise Penelope", "prudent Penelope" (reserved for πεπνυμένος), "thoughtful Penelope" |
| τὸν δ’ αὖτ’ Ἀντίνοος προσέφη, Εὐπείθεος υἱός (reply-formula: name + patronymic, no participle) | "Him then in turn addressed Antinous, Eupeithes’ son:" | "Then Antinous, son of Eupeithes, spoke to him in turn:" | "answered" (reserved for τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα) |
| τὸν δ’ αὖτ’ Εὐρύμαχος Πολύβου πάϊς ἀντίον ηὔδα (reply-formula: name + patronymic + ἀντίον ηὔδα) | "Him then in turn spoke Eurymachus, Polybus’ son, face to face:" | "Then Eurymachus, son of Polybus, spoke to him in turn, face to face:" | "answered" (reserved for τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα) |
| κεδνὰ ἰδυῖα (of Eurycleia) | "the one wise and trusty" | "trusty and wise" | "kindly", "careful" alone (loses ἰδυῖα "knowing, skilled") |
| αἰθομένας δαΐδας φέρε | "burning torches carried" | "carried burning torches" | "blazing torches", "flaming brands" |
| ἦμος δ’ ἠριγένεια φάνη ῥοδοδάκτυλος Ἠώς (whole line) | "When early-born appeared, rose-fingered Dawn," | "When early-born Dawn appeared, rose-fingered, …" | "rosy-fingered", "child of morning", "early-rising", "Dawn with her rose-red fingers" |
| Ὀδυσσῆος φίλος υἱός | "Odysseus’ dear son" | "the dear son of Odysseus" | "Odysseus’ own son", "beloved son" |
| βῆ δ’ / βῆ ῥ’ ἴμεν | "(he) set out to go" | "he set out for …" / "went" | "strode", "made his way" |
| θεῷ ἐναλίγκιος ἄντην | "like to a god to look upon" | "like a god to look upon" | "godlike" (reserved for ἀντίθεος), "godlike in form" (reserved for θεοειδής), "like a god in bearing" |
| κήρυκες λιγύφθογγοι | "the clear-voiced heralds" | "the clear-voiced heralds" | "loud-voiced", "shrill-voiced", "clear-toned" |
| κύνες ἀργοί | "swift dogs" | "swift dogs" (+ note: "swift" or "white", disputed) | "white dogs", "flashing dogs", "gleaming" (reserved for γλαυκῶπις) |
| θεσπεσίην … χάριν κατέχευεν | "wondrous … a grace poured-down" | "shed a wondrous grace upon him" | "divine grace" (reserved for θεῖος), "marvellous charm", "heavenly grace" (reserved for δῖος) |
| ἥρως (as title) | "the hero" | "the hero" | "lord", "warrior", "old soldier" |
| Ἴλιον εἰς ἐύπωλον | "to Ilios of-fine-foals" | "to Ilios of the fine foals" | "of the fine horses", "horse-rich", "famed for horses" (loses πῶλος "foal") |
| ἄγριος Κύκλωψ | "the savage Cyclops" | "the savage Cyclops" | "wild", "brutish", "fierce" |
| δάκρυ χέων | "a tear shedding" | "shedding tears" | "weeping" (drops χέω), "in tears" |
| ἀγορήσατο καὶ μετέειπε | "addressed-the-assembly and spoke among them" | "addressed the assembly and spoke among them" | "harangued", "made a speech"; μετέειπε alone = "spoke among (us/them)" |
| κέκλυτε δὴ νῦν μευ, Ἰθακήσιοι, ὅττι κεν εἴπω (whole line) | "Hear me now, men of Ithaca, whatever I may say;" | "Hear me now, men of Ithaca, and hear what I have to say." | "Listen to me", "Ithacans, hear me", "mark what I say" |
| ὣς φάτο | "So he spoke" | "So he spoke" | "Thus he spoke", "So he said" (keep one form throughout) |
| πεπνυμένα μήδεα εἰδώς | "prudent counsels knowing" | "a man versed in prudent counsels" | "wise in counsel", "shrewd" — "prudent" kept to match πεπνυμένος |
| καθαπτόμενος προσέειπεν | "accosting, he addressed him" | "addressing him directly" | "rebuked", "reproached" (the verb need not carry reproach) |
| ὦ γέρον | "Old man" | "Old man" | "Old sir", "Elder", "Grandfather" |
| πατὴρ δ’ ὣς ἤπιος ἦεν | "and like a father kind he was" | "and was as gentle as a father" | "fatherly", "kind as a father to his children" |
| αἶθοψ οἶνος (αἴθοπα οἶνον) | "the fire-faced wine" | "the wine that has the look of fire" | "sparkling", "gleaming", "fire-bright" (reserved for αἴθων), "bright wine"; built the same way as οἶνοψ πόντος |
| βοῦς ἱερεύοντες καὶ ὄις καὶ πίονας αἶγας (whole line) | "slaughtering oxen and sheep and fat goats," | "slaughtering oxen and sheep and fat goats" | "sacrificing" alone (hides that this is the meal), "fatted goats" |
| ἐυκνήμιδες Ἀχαιοί | "the well-greaved Achaeans" | "the well-greaved Achaeans" | "bronze-greaved", "armoured", "well-armed" |
| Ἀντίνοος δέ μιν οἶος ἀμειβόμενος προσέειπε (reply-formula) | "but Antinous, him, alone, answering addressed:" | "Antinous alone spoke to him in answer:" | "answered" as a finite verb (reserved for ἠμείβετο); kept parallel to ἀπαμειβόμενος προσέφη |
| Τηλέμαχ’ ὑψαγόρη, μένος ἄσχετε | "Telemachus, lofty-talker, unrestrained-in-fury" | "Telemachus, you lofty talker, unrestrained in your fury" | "braggart", "big-mouth", "high-flown", "ungovernable" |
| κέρδεα οἶδεν / εἰδώς | "knows cunning-ways" | "knows cunning ways" | "is full of tricks", "knows all the angles", "wily" |
| κοῦροι ἐμοὶ μνηστῆρες | "Young men, my suitors" | "Young men, my suitors" | "My young suitors", "Young lords", "Princes" |
| μοῖρ’ ὀλοή | "the deadly fate" | "the deadly fate" | "baneful doom", "cruel fate", "destructive destiny" |
| τανηλεγὴς θάνατος | "death that lays-at-length" | "death that lays men at length" (+ note: meaning unknown, the alternative "bringing long sorrow" is stated) | "woeful death", "grievous death", "long-sorrowing death" (silently choose the other ancient guess) |
| Ἀχαιϊάδες | "the Achaean women" | "the Achaean women" | "Achaean ladies", "Greek women" |
| ἐυπλοκαμῖδες (of the Achaean women of old) | "fair-tressed" | "fair-tressed" | "well-braided", "lovely-haired" — kept parallel to, but distinct from, ἐυπλόκαμος "fine-plaited" (Calypso's epithet, 1.86; not itself yet in this table), since ἐυπλοκαμῖδες is a separate nominal formation (women characterized by their locks), not the same word |
| ἐυστέφανος (of Mycene) | "fair-crowned" | "fair-crowned" | "well-garlanded", "crowned with flowers" |
| ἐυδείελος (of Ithaca) | "clear-seen" | "clear-seen" | "sunny", "far-seen", "visible from afar" — the ancient etymologies conflict (from δείελος "evening" or from δῆλος "visible"); kept literal and flagged as disputed in the note |
| εὐρύοπα Ζεύς | "far-thundering Zeus" | "Zeus who thunders from afar" | "wide-voiced Zeus", "far-seeing Zeus" — the second element (from ὄψ "voice" or "eye/face") is disputed; the traditional gloss "loud/far-thundering" is followed and the doubt is noted |
| πολύμητις (of Odysseus) | "many-wiled" | "of many wiles" | "resourceful" and "of many devices" (reserved for πολυμήχανος), "many-counselled"/"of many counsels" (reserved for πολύφρων, which already uses that wording); μῆτις is "cunning intelligence, craft", distinct from μηχανή "device" |
| υἷες Ἀχαιῶν (periphrasis for the young Achaean men / the suitors) | "sons of the Achaeans" | "the sons of the Achaeans" | "young Achaean men", "Achaean warriors" — a fixed periphrasis, not a plain stand-in for "the Achaeans" |
| μνηστὺς ἀργαλέη | "grievous wooing" | "grievous wooing" | "cruel courtship", "hard suit" |
| τὸν δ’ Εὐηνορίδης Λειώκριτος ἀντίον ηὔδα (reply-formula: name + patronymic + ἀντίον ηὔδα) | "Him then Leiocritus, son of Evenor, addressed, face to face:" | "Then Leiocritus, son of Evenor, spoke to him in turn, face to face:" | "answered" (reserved for τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα); kept on the same pattern already fixed for τὸν δ’ αὖτ’ Εὐρύμαχος Πολύβου πάϊς ἀντίον ηὔδα |
| ὣς φάτ’ Ἀθηναίη κούρη Διός (narrator's speech-closing formula, name + patronymic filled into ὣς φάτο) | "So spoke Athena, daughter of Zeus" | "So spoke Athena, daughter of Zeus" | "said" (reserved for a plain ἔφατο without a following name); "thus" for ὥς (reserved for the unelided adverb, see the ὣς φάτο row) |
| Ἀντίνοος δ’ ἰθὺς γελάσας κίε Τηλεμάχοιο, / ἔν τ’ ἄρα οἱ φῦ χειρί, ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε (two-line approach-and-address formula: a named figure comes straight up laughing, clasps the hand, and speaks) | "…, laughing outright, went straight for …,\nand clasped him by the hand, and spoke a word, and called him by name:" | "…, with a straight-out laugh, went right up to …, took his hand, and spoke, calling him by name:" | "smiling" (loses the mockery in γελάσας here), "grasped his hand" alone (drops the tmesis idiom ἔν … φῦ, 'grew into, took firm hold of') |
| μνηστῆρες/μνηστῆρας ἀγαυοί/ἀγαυούς | "the noble suitors" | "the noble suitors" | "lordly" (reserved for the separate house-fixed μνηστῆρες ἀγήνορες), "illustrious", "proud", "glorious" |
| πατρώιος ἑταῖρος / πατρώιοι ἑταῖροι ("a companion / companions from [someone's] father's day", of Mentor and Halitherses) | "a companion from his father's day" (sg.) / "his father's own companions" (pl.) | "a companion of his father's day" | "hereditary companion" (reserved for the already-fixed πατρώιος ξεῖνος), "family friend", "an old friend of his father's" |
| πολιὴ ἅλς (of the sea) | "the grey sea" | "the grey sea" | "hoary" (archaic-sounding), "silvery", "foam-flecked" (adds imagery not in the Greek) |
| ἐπ’ ἠεροειδέα πόντον | "over the misty-looking sea" | "over the misty-looking sea" | "murky", "dark", "hazy" (ἠεροειδής is built directly on ἀήρ 'mist, haze', and the literal 'looking like mist' is kept) |
| διογενής (of Odysseus) | "Zeus-sprung" | "Zeus-born" | "godlike" (reserved for ἀντίθεος), "heavenly" (reserved for δῖος), "divine" (reserved for θεῖος), "godlike in form" (reserved for θεοειδής) |
| ἱερὴ ἲς Τηλεμάχοιο (periphrasis) | "the sacred force of Telemachus" | "the strong, sacred figure of Telemachus" | naturalising it to a bare epithet-plus-name ("mighty Telemachus"), which would erase the periphrasis Homer uses in place of the bare name — the same device as βίη Ἡρακληείη for Heracles |
| ἀθανάτοισι θεοῖς αἰειγενέτῃσιν | "the immortal gods who are forever-born" | "the immortal, everlasting gods" | folding it into the already-fixed θεοὶ αἰὲν ἐόντες "the gods who are forever" — that formula is built on ἐόντες 'being', this one on γίγνομαι 'be born', and the two are kept as distinct literal renderings |
| ἔνθ’ αὖτ’ ἄλλ’ ἐνόησε θεά, γλαυκῶπις Ἀθήνη (whole-line formula) | "Then again another thing devised the goddess, gleaming-eyed Athena." | "Then, in her turn, the goddess, gleaming-eyed Athena, thought of something else." | "conceived a new plan" (loses the plain sense of ἄλλο "another thing," not specifically a "plan"), "had another idea" (too casual for the register) |
| τὸν προτέρη προσέειπε θεά, γλαυκῶπις Ἀθήνη (reply-formula variant: the speaker speaks first, 3.13) | "Him first addressed the goddess, gleaming-eyed Athena:" | "The goddess, gleaming-eyed Athena, was the first to speak to him:" | "answered" (no one has spoken yet; also reserved for ἠμείβετο); kept on the pattern of the fixed τὸν δ’ αὖτε προσέειπε "Him then in turn addressed", with προτέρη "first" in place of αὖτε "in turn" |
| Γερήνιος ἱππότα Νέστωρ (Nestor's standing name-epithet, 3.68) | "the Gerenian horseman Nestor" | "the Gerenian horseman Nestor" (+ note: meaning of Γερήνιος disputed — Gerenia/Gerenon in Messenia, or γέρων / γέρας) | "old Nestor", "the aged Nestor", "honoured Nestor" (each silently picks one disputed etymology); "charioteer", "horse-driver", "knight", "lord of horses" for ἱππότα |
| Νέστωρ ἱππόδαμος (3.17, genitive Νέστορος ἱπποδάμοιο) | "horse-taming Nestor" | "Nestor, tamer of horses" | "horse-breaker", "breaker of horses", "master of horses", "horseman" (reserved for ἱππότα) |
| ἐνοσίχθων κυανοχαίτης (3.6) | "the dark-haired earth-shaker" | "the dark-haired earth-shaker" | "blue-haired", "sable-haired", "dark-maned", "dark-browed"; ἐνοσίχθων keeps the table's "earth-shaker" |
| Παλλάδ’ Ἀθηναίην κούρην Διὸς αἰγιόχοιο (whole line, 3.42) | "Pallas Athena, the daughter of aegis-bearing Zeus" | "Pallas Athena, the daughter of aegis-bearing Zeus" (+ note: meaning of αἰγίοχος disputed) | "aegis-holding", "storm-bearing", "goat-riding"; "Pallas Athena" follows the form already shipped at 1.125, 1.327 and 2.405 |
| Ποσειδάωνι ἄνακτι (line-end phrase, 3.43 and 3.54) | "to Poseidon the lord" | "to lord Poseidon" | "king Poseidon", "master Poseidon", "Poseidon the king" |
| ἐυκτίμενον πτολίεθρον (3.4) | "well-built citadel" | "the well-built citadel" | "well-founded", "stately city", "fair-built town" |
| ζείδωρος ἄρουρα (3.3) | "the grain-giving plough-land" | "the grain-giving plough-land" (+ note: ancient alternative "life-giving") | "life-giving earth" (silently picks the minority etymology), "fruitful earth", "bountiful soil" |
| νηῦς ἐίση (3.10, genitive νηὸς ἐίσης) | "the well-balanced ship" | "the well-balanced ship" (+ note: sense uncertain) | "trim", "shapely", "evenly-built" |
| θοὴ νηῦς μέλαινα (3.61, θοῇ σὺν νηὶ μελαίνῃ) | "swift black ship" | "swift black ship" | "fast dark ship", "sable ship"; θοός keeps the table's νηῦς θοή "swift ship", and the pairing follows odyssey-008's shipped "the swift black ship" (2.430) |
| δέπας ἀμφικύπελλον (3.63; 3.63 also has καλόν, "the fair double cup") | "double cup" | "double cup" (+ note: "double cup" vs "two-handled", disputed) | "two-handled cup" (silently picks one side), "goblet" (reserved for ἄλεισον, 3.50/53) |
| ὑγρὰ κέλευθα (3.71) | "the watery ways" | "the watery ways" | "the sea-lanes", "the paths of the sea", "the wet ways" |
| μελιηδὴς οἶνος (3.46) | "honey-sweet wine" | "honey-sweet wine" | "mellow wine", "wine sweet as honey"; the plain ἡδὺς οἶνος (3.51) is "sweet wine" |
| ἐρικυδέα δαῖτα (3.66) | "a glorious feast" | "a glorious feast" | "splendid", "sumptuous", "rich feast" |
| ὦ Νέστορ Νηληϊάδη, μέγα κῦδος Ἀχαιῶν (whole-line vocative address, 3.79) | "O Nestor, son of Neleus, great glory of the Achaeans," | "Nestor, son of Neleus, great glory of the Achaeans," | "Neleides", "pride of the Achaeans", "great boast of the Achaeans" |
| ἀλλ’ εὖ μοι κατάλεξον ὅπως ἤντησας ὀπωπῆς (whole line, 3.97) | "but recount to me well how you came upon the sight." | "but tell me plainly how you came to see it." | "tell me truly" (that is ἐτήτυμον), "recount it exactly" (reserved for ἀτρεκέως κατάλεξον in the fixed ἀλλ’ ἄγε μοι τόδε εἰπέ line) |
| ἀρήιος (3.109, 3.167) | "warlike" | "warlike" | "war-loving", "martial" (too Latinate) |
| ἀτάσθαλα (3.207, adj./subst., distinct lemma from the already-fixed noun ἀτασθαλίαι) | "wanton deeds" / "wanton things" | "wanton deeds" | "reckless", "outrageous acts" — kept to echo the fixed ἀτασθαλίαι "wanton-follies" |
| λυγρός (3.132 λυγρὸν νόστον, 3.194 λυγρὸν ὄλεθρον) | "grievous" | "grievous" | "baneful", "woeful", "miserable" |
| θεσπέσιος of a sound (3.150 ἠχῇ θεσπεσίῃ; cf. the already-fixed θεσπεσίην … χάριν) | "wondrous" | "wondrous" | "divine", "prodigious", "supernatural" |
| Ἀτρεΐδῃ Ἀγαμέμνονι (3.156, 3.164; cf. Ἀτρεΐδῃσι 3.136, Ἀτρεΐδην alone 3.193) | "Atreus' son Agamemnon" | "Agamemnon, son of Atreus" | "the son of Atreus" alone when the name Agamemnon is also given |
| Ἀτρεΐδης / Ἀτρεΐδην used alone as a name-substitute (3.193) | "the son of Atreus" | "the son of Atreus" | naming him "Agamemnon" outright where the Greek withholds the name |
| Τυδέος υἱός / Τυδεΐδης (periphrasis and patronymic for Diomedes) | "the son of Tydeus" | "the son of Tydeus" | naming him "Diomedes" where the Greek uses the periphrasis alone |
| ἱππόδαμος applied to a figure other than Nestor (3.181, of Diomedes) | "horse-taming" | "tamer of horses" | keeps the wording already fixed for Νέστωρ ἱππόδαμος, now reused for its plain adjectival sense |
| μεγάθυμος (3.189, of Achilles) | "great-hearted" | "great-hearted" | "great-souled", "high-spirited" |
| φαίδιμος (3.189, "φαίδιμος υἱός") | "glorious" | "glorious" | "shining", "splendid" (reserved for ἀγλαός) |
| ἀγλαός (3.190, "Ποιάντιον ἀγλαὸν υἱόν") | "splendid" | "splendid" | "glorious" (reserved for φαίδιμος), "radiant" |
| ποιμένι λαῶν ("shepherd of the people", 3.156) | "shepherd of the people" | "shepherd of the people" | "shepherd of hosts", "leader of men" |
| βοὴν ἀγαθός (of Menelaus, 3.311) | "good at the war-cry" | "good at the war-cry" | "loud in the war-cry", "valiant", "brave" (loses the specific βοή 'battle-shout' image) |
| πολύχρυσος (of Mycenae, 3.305) | "rich in gold" | "rich in gold" | "golden", "gold-rich", "wealthy" |
| κυανόπρῳρος / κυανοπρῳρείους (of ships, 3.299) | "dark-prowed" | "dark-prowed" | "blue-prowed", "black-prowed", "dark-blue-prowed" |
| τοῖσι δὲ καὶ μετέειπε θεά, γλαυκῶπις Ἀθήνη (whole-line speech introduction, 3.330) | "And among them spoke also the goddess, gleaming-eyed Athena:" | "And among them the goddess, gleaming-eyed Athena, spoke up as well:" | "addressed" (reserved for προσέειπε/προσέφη), "answered" (reserved for ἠμείβετο); μετέειπε keeps the table's "spoke among" (see the ἀγορήσατο καὶ μετέειπε row); the opening τοῖσι δὲ καὶ μετέειπε follows the English shipped at 2.157 (odyssey-006, of Halitherses) |
| ἦ ῥα (speech-closing, ἦ from ἠμί; 3.337) | "He/She spoke" | "So he/she said" | "Thus he spoke" / "So he spoke" (reserved for ὣς φάτο / ὣς ἔφατο); follows the wording shipped at 2.321 |
| Διὸς θυγάτηρ (of Athena, 3.337, 3.378) | "the daughter of Zeus" | "the daughter of Zeus" | "Zeus' girl", "child of Zeus"; the same English as the table's κούρη Διός, since both nouns mean 'daughter' here |
| Παλλὰς Ἀθήνη (line-end name, 3.385) | "Pallas Athena" | "Pallas Athena" (+ note once: meaning of Παλλάς disputed) | "Athena Pallas", "the maiden Athena"; the form shipped at 1.125, 2.405, 3.29 |
| κυδίστη Τριτογένεια (3.378) | "most glorious Tritogeneia" | "most glorious Tritogeneia" (+ note: meaning of Τριτογένεια unknown — lake/river Triton, 'head', 'third-born') | "Triton-born", "third-born", "the Trito-born" (each silently picks one ancient guess); "glorious" follows the κῦδος root and is kept distinct from φαίδιμος only by the superlative |
| ὣς ἔφατ’ εὐχόμενος (prayer-closing, 3.385; shipped at 2.267) | "So he spoke, praying," | "So he prayed," | "So he said in prayer" |
| τοῦ δ’ ἔκλυε Παλλὰς Ἀθήνη (second half of the prayer-closing line, 3.385) | "and Pallas Athena heard him." | "and Pallas Athena heard him." | "heeded", "granted his prayer" (say more than κλύω) |
| ὣς ἄρα φωνήσασ’ (3.371; shipped at 2.405, 3.29) | "So then having spoken," | "So she spoke, and" | "Having said this", "With these words" |
| αὐτὰρ ἐπεὶ σπεῖσάν τ’ ἔπιον θ’, ὅσον ἤθελε θυμός (whole line, 3.342 = 3.395) | "But when they had poured libations and drunk, as much as their heart wished," | "But when they had poured libations and drunk as much as their hearts wished," | "to their hearts' content", "as much as they liked" (lose θυμός) |
| νώμησαν δ’ ἄρα πᾶσιν ἐπαρξάμενοι δεπάεσσι (whole line, 3.340) | "and they dealt it out to all, having first poured drops into the cups;" | "and served it out to all, first pouring a few drops into each cup" | "having poured the first-fruits", "having begun with the cups" (obscure), "distributed the cups" |
| ἠέλιος δ’ ἄρ’ ἔδυ καὶ ἐπὶ κνέφας ἦλθε (3.329, after ὣς ἔφατ’) | "and the sun then set, and darkness came on." | "and the sun set, and darkness came on." | "night fell", "dusk came down", "the sun went down" (keep δύω 'sink/set' and κνέφας 'darkness') |
| κατέρυκε καθαπτόμενος ἐπέεσσιν (3.345; variant of the table's καθαπτόμενος προσέειπεν) | "held (them) back, accosting (them) with words:" | "held (them) back, addressing (them) directly with these words:" | "rebuked", "reproached" — as in the καθαπτόμενος row |
| κατὰ μοῖραν (3.331; shipped at 2.251 as "according to what is fitting") | "according to what is fitting" | "as is fitting" | "rightly", "in due order", "properly" |
| γέρον φίλε (3.357) | "dear old man" | "dear old man" | "my good old friend", "dear sir"; builds on the table's ὦ γέρον "Old man" |
| ὦ φίλος (nominative as vocative, 3.375; cf. ὦ φίλ’ shipped at 3.103, 3.211) | "O friend" | "Friend" | "My dear boy", "my friend" in `i` (kept to the shipped ὦ φίλ’ pattern); plain φίλος in καὶ σύ, φίλος stays "friend" / "my friend" as shipped at 1.301, 3.199 |
| κοίλη νηῦς μέλαινα (3.365, κοίλῃ παρὰ νηὶ μελαίνῃ) | "the hollow black ship" | "the hollow black ship" | "dark hollow ship"; κοῖλος keeps the table's "hollow", μέλας the "black" of θοὴ νηῦς μέλαινα |
| Ὀλύμπια δώματ’ ἔχοντες (periphrasis for the gods, 3.377) | "those who hold the Olympian halls" | "those who hold the halls of Olympus" | "the Olympians", "those who dwell on Olympus" (drops ἔχω 'hold') |
| οἶνος ἡδύποτος (3.391) | "sweet-to-drink wine" | "wine sweet to drink" | "sweet wine" (reserved for ἡδὺς οἶνος), "honey-sweet" (reserved for μελιηδής), "mellow", "delicious" |
| ἀγακλυτός (of halls, 3.388) | "renowned" | "renowned" | "far-famed" (shipped for τηλεκλυτός at 1.30), "glorious" (reserved for φαίδιμος), "famous" (keep for κλυτός) |
| ὁ γέρων / ὁ γεραιός (narrator's name for Nestor, 3.373, 3.390, 3.393) | "the old man" | "the old man" | "the old king", "the aged one", "the elder"; γεραίτερος (comparative) is "older" |
| ὑπ’ αἰθούσῃ ἐριδούπῳ (3.399) | "beneath the loud-echoing portico" | "under the loud-echoing portico" | "loud-thundering", "resounding colonnade", "the porch" (αἴθουσα is the roofed portico) |
| τρητοῖς ἐν λεχέεσσιν (3.399; cf. παρὰ τρητοῖσι λέχεσσι, 1.440) | "on a bored bedstead" | "on a corded bedstead" (+ note: frame bored for the cords) — both layers follow the wording already shipped at 1.440 (odyssey-004) | "carved bed", "inlaid bed", "fretted bed" (τρητός is 'bored, pierced') |
| ἐυμμελίης (of Peisistratus, 3.400) | "of the good ash-spear" | "of the good ash-spear" | "good spearman", "skilled with the spear", "of the ashen spear" (drop ἐυ-) |
| ὄρχαμος ἀνδρῶν (3.400) | "chief of men" | "chief of men" | "leader of men" (kept apart from ἡγήτωρ 'leader' and ποιμὴν λαῶν), "lord of men" (ἄναξ ἀνδρῶν will need "lord") |
| δόμου ὑψηλοῖο (3.402; shipped at 1.126 as "the high house") | "the high house" | "the high house" | "lofty palace", "tall house" |
| ἄλοχος δέσποινα (3.403) | "his wife, the lady" | "his wife, the lady of the house" | "queen" (reserved for ἄνασσα), "mistress" alone, "noble wife" |
| ἄνασσα (vocative ἄνασσ’ to a goddess, 3.380) | "queen" | "queen" | "lady" (keep for δέσποινα / πότνια), "mistress" |
| εὐρυμέτωπος (of cattle, 3.382) | "broad-browed" | "broad-browed" / "broad of brow" | "wide-faced", "broad-fronted" |
| φήνη (bird, 3.372) | "a sea-eagle" | "a sea-eagle" (+ note: species unknown — sea-eagle, osprey, lammergeier proposed) | "vulture", "osprey" as if certain |
| Λακεδαίμων δῖα (3.326) | "heavenly Lacedaemon" | "heavenly Lacedaemon" | "bright", "divine" (reserved for θεῖος), "glorious"; δῖος keeps the table's "heavenly" for places too; note the live inconsistency that odyssey-010 shipped ἅλα δῖαν (3.153) as "heavenly brine" in `l` but "bright salt sea" in `i` — left as shipped, flagged at review |
| κακκείοντες ἔβαν οἶκόνδε ἕκαστος (half-line, 3.396; shipped at 1.424) | "to lie down going, each one went to his own house" | "each went off home to bed" | "went to rest", "retired to their homes"; wording follows 1.424 (odyssey-004) |
| θέσφατόν ἐστι (4.561) | "it is god-declared" | "it is decreed" | "it is fated" (blurs it with the separate μοῖρα/πότμος word-family already used elsewhere in this part), "it is ordained" (loses the θεός root) |
| Ἠλύσιον πεδίον καὶ πείρατα γαίης (4.563) | "the Elysian plain and the ends of the earth" | "the Elysian plain, at the ends of the earth" | "Elysium" alone (drops πεδίον "plain"), "the edges of the world" (πείρατα is properly "limits, bounds", kept literal) |
| θυμὸς ἀγήνωρ (4.548) | "manly spirit" | "proud spirit" | "manly heart" (in this specific epithet "spirit" is kept, reserving "heart" for ἦτορ/κραδίη in this phrase), "overbearing spirit" (too negative a reading of ἀγήνωρ here) — NB (added odyssey-023, 2026-09-27): θυμός itself is NOT kept "spirit" everywhere in the poem, despite what an earlier version of this row claimed; the pilot (1.4, ὃν κατὰ θυμόν "in his own heart"), the fixed κατὰ φρένα καὶ κατὰ θυμόν ("in mind and in heart"), and the shipped 5.83/5.157 ("racking his heart with tears and groans and pains") all render plain θυμός as "heart". Only this one fixed epithet, θυμὸς ἀγήνωρ, keeps "spirit" |
| τεληέσσας ἑκατόμβας (4.582) | "complete hecatombs" | "complete hecatombs" | "perfect", "unblemished" (both true to τέλος but drift from the literal "brought to completion"), "full hecatombs" (risks confusion with a literal headcount) |
| ἄσβεστον κλέος (4.584) | "fame unquenchable" | "fame that would never go out" | "undying fame" (that register is reserved for ἄφθιτον-type words, not used in this part), "imperishable renown" (too Latinate), "everlasting fame" (loses the fire-image in ἀ- + σβέννυμι) |
| ἤματα πάντα (4.592) | "all your days" | "for all your days" | "forever" (loses the concrete "days"), "all your life long" (too free) |
| δίφρον ἐύξοον (4.590) | "a well-polished car" | "a well-polished chariot" | "a well-planed chariot-board" (too technical), "a smooth car" (loses the craftsmanship sense of ξέω "plane, polish") |
| κρητῆρα τετυγμένον (4.615) / τετυγμένος generally | "a wrought mixing-bowl" | "a well-wrought mixing-bowl" | "a fashioned bowl" (flat), "a finely made bowl" (loses the link to τεύχω, the verb behind Homeric craftsmanship-formulas generally) |
| ἔργον Ἡφαίστοιο (4.617) | "the work of Hephaestus" | "the work of Hephaestus" | "Hephaestus's handiwork", "made by Hephaestus" (both lose the fixed formulaic shape of the phrase, a standing mark of the finest divine craftsmanship) |
| χειρί τέ μιν κατέρεξεν ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν (4.610, gesture-and-address formula) | "and stroked him with his hand, and spoke a word, and called him by name:" | "and stroked him with his hand, and spoke, calling him by name:" | "patted", "caressed" alone for κατέρεξεν (kept as "stroked" to distinguish from the firmer hand-clasp of the already-fixed ἔν τ’ ἄρα οἱ φῦ χειρί formula); the tail ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε(ν) keeps the wording already fixed for that formula's own closing words |
| Πύλῳ ἠγαθέῃ (4.599) | "holy Pylos" | "holy Pylos" | "very holy" (over-translates the intensive), "sacred Pylos" (risks confusion with the distinct, already-fixed "sandy Pylos" for a different epithet of the same city) |
| εὐρύχορον (4.635, of Elis) | "of wide dancing-grounds" | "spacious" | "of wide streets" (χορός is a dancing-place, not a street), "broad-lands" |
| ταλαεργοὶ ἡμίονοι (4.636) | "labour-enduring mules" | "labour-enduring... mules" | "hard-working" (loses the τλῆναι root, already used for "enduring-minded" ταλασίφρων), "toiling mules" |
| τοῖσι δὲ μύθων ἦρχε Γερήνιος ἱππότα Νέστωρ (whole-line speech introduction, 3.417 = 3.474; cf. τοῖς ἄρα … 3.68, and τοῖσι δὲ μύθων ἦρχε πατὴρ ἀνδρῶν τε θεῶν τε 1.28) | "And among them of speeches made-beginning the Gerenian horseman Nestor:" | "The Gerenian horseman Nestor was the first to speak among them:" | "addressed" (reserved for προσέειπε / προσέφη), "answered" (reserved for ἠμείβετο), "began to speak" (loses μῦθοι 'speeches'); `l` follows 1.28 and 3.68, and `i` follows the shipped 3.68 |
| αὐτὰρ ἐπεὶ πόσιος καὶ ἐδητύος ἐξ ἔρον ἕντο (whole line, 1.150 = 3.67 = 3.473; shipped) | "But when of drink and of food they had put away desire," | "But when they had put from them the desire for drink and food," | "had eaten and drunk their fill", "had satisfied their hunger and thirst" (lose ἔρος 'desire' and ἐξίημι 'send out') |
| δύσετό τ’ ἠέλιος σκιόωντό τε πᾶσαι ἀγυιαί (whole line, 2.388 = 3.487 = 3.497; shipped) | "And the sun set, and all the streets grew shadowy," | "The sun set, and all the streets grew dark," | "night fell", "the ways grew dim"; kept apart from ἠέλιος δ’ ἄρ’ ἔδυ καὶ ἐπὶ κνέφας ἦλθε ("and the sun set, and darkness came on"). At 3.497 it ends with a full stop, and a period replaces the comma in both layers |
| μάστιξεν δ’ ἐλάαν, τὼ δ’ οὐκ ἀέκοντε πετέσθην (whole line, 3.484 = 3.494) | "and he whipped them to drive on, and the two, not unwilling, flew" | "he whipped them to drive them on, and the pair flew not unwilling" | "nothing loath", "eagerly" / "gladly" (flattens the litotes), "sped" / "raced" (lose πέτομαι 'fly'), "lashed" (keep "whipped" for μαστίζω) |
| ὣς ἔφαθ’, οἱ δ’ ἄρα τοῦ μάλα μὲν κλύον ἠδ’ ἐπίθοντο (whole line, 3.477) | "So he spoke, and they then readily heard him and obeyed," | "So he spoke, and they listened to him readily and obeyed," | "heeded", "hearkened" (archaic), "did as he said" (loses κλύω 'hear'); opens with the table's ὣς φάτο "So he spoke" |
| ὁ γέρων (bare, of Proteus, 4.450, 455, 460) | "the old man" | "the old man" | inventing a new epithet; kept to the same plain rendering already established for Nestor's bare γέρων/γεραιός (row above), since both are simply "the old man" once the fuller epithet has introduced the figure |
| τετληότι θυμῷ (4.447, 459 — the same phrase repeated verbatim) | "with enduring heart" | "with enduring hearts" | varying the wording between the two occurrences; kept identical both times, though the referent (the four disguised men) is plural and the Greek dative is grammatically singular, distributive |
| δολίης/δολίην ... τέχνης/τέχνην (4.455, of Proteus's shape-shifting; 529, of Aegisthus's murder-plot) | "guileful device" | "guileful device" ("his guileful device" / "a guileful device of his own") | keeping them apart as two unrelated phrases; the identical English is kept for both so the reader can hear the deliberate parallel Proteus's own narrative draws between his own guile and Aegisthus's |
| Γυρῇσιν / Γυραίην (πέτρην) (4.500, 507) | "the Gyraean rocks" / "the Gyraean rock" | same | resolving the place to a modern identification (e.g. "the rocks of Tenos"); the location of Γυραί was disputed already in antiquity and remains unidentified, so the name is kept as a transliterated proper name and flagged as disputed in the note |
| μέγ’ ἀάσθη (4.503, 509 — the same words repeated verbatim, of Ajax's fatal boast) | "greatly blinded" | "a great blindness of mind" | "was greatly deluded", "was struck mad", "acted with great folly" (all lose the specific ἀάομαι root, the same one behind the goddess Ἄτη); kept identical in both occurrences |
| δολιχηρέτμοισι (of the ships bearing Ajax's fleet, 4.499) | "long-oared" | "long-oared" | "long-benched" (confuses ἐρετμόν "oar" with a rowing-bench), "well-oared" |
| ἁλιοτρεφέων (4.442, of the seals) | "sea-bred" | "sea-bred" | flagging as unknown; the compound (ἅλς + τρέφω) is transparent even though otherwise unattested |
| ζατρεφέας (4.451, of the seals) | "sleek" | "well-fed" | flagging as unknown; ζα- is the familiar intensive prefix (= δια-) on τρέφω "nourish" |
| ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμειβόμενος προσέειπεν· (a new reply-formula, first at 4.471, recurring verbatim at 491) | "So I spoke, and he then at once, answering me, addressed me:" | "So I said, and he answered me at once:" | using the gender-neutral formula already fixed at 4.464 ("So she spoke, and I then, answering her, addressed her:"); ὁ here is explicitly masculine, and a distinct formula is fixed for it, to be kept identical at every future recurrence |
| γέρων ἱππηλάτα Νέστωρ (3.436, 3.444) | "the old man, horse-driver Nestor" | "Nestor, the old horse-driver" | "horseman" (reserved for ἱππότα), "horse-taming" (reserved for ἱππόδαμος), "charioteer" (ἡνίοχος); the table already turned down "horse-driver" for ἱππότα, which leaves it free for ἱππηλάτα (ἵππος + ἐλαύνω) |
| οὖρος Ἀχαιῶν (of Nestor, 3.411) | "warden of the Achaeans" | "the warden of the Achaeans" | "bulwark" (that is ἕρκος), "guardian" (keep for φύλαξ), "wind of the Achaeans" (a confusion with οὖρος 'fair wind') |
| θεοείκελος (of Telemachus, 3.416) | "god-resembling" | "who was like a god" | "godlike" (reserved for ἀντίθεος), "godlike in form" (reserved for θεοειδής), "like to a god to look upon" (reserved for θεῷ ἐναλίγκιος ἄντην), "equal to a god" (reserved for ἰσόθεος) |
| μεγαλήτωρ (of Telemachus, 3.432; also of Odysseus, 5.81 "Ὀδυσσῆα μεγαλήτορα") | "great-spirited" | "great-spirited" | "great-hearted" (reserved for μεγάθυμος, which comes nine lines earlier, at 3.423), "great-souled", "high-spirited" (reserved for ὑπέρθυμος) |
| μενεπτόλεμος (of Thrasymedes, 3.442) | "steadfast-in-battle" | "steadfast in battle" | "warlike" (reserved for ἀρήιος), "staunch in fight", "stubborn in war" |
| ὑπέρθυμος (of Thrasymedes, 3.448) | "high-spirited" | "high-spirited" | "great-hearted" (reserved for μεγάθυμος), "overweening" / "arrogant" (the word is not a reproach here) |
| χθὼν εὐρυόδεια (3.453) | "the wide-wayed earth" | "the wide-wayed earth" | "broad earth" (keep for εὐρεῖα χθών), "the earth with its wide roads" |
| δαὶς θάλεια (3.420, δαῖτα θάλειαν) | "abundant feast" | "abundant feast" | "glorious feast" (reserved for ἐρικυδέα δαῖτα), "rich", "bounteous", "flourishing" |
| διοτρεφέες βασιλῆες (3.480) | "Zeus-nurtured kings" | "Zeus-nurtured kings" | "Zeus-born" (reserved for διογενής), "kings fostered by Zeus", "god-nurtured" |
| καλλίτριχες ἵπποι (3.475) | "fair-maned horses" | "fair-maned horses" | "sleek-coated", "long-maned", "beautiful-haired" |
| ὠκέες ἵπποι (3.478, 3.496) | "the swift horses" | "the swift horses" | "fleet", "quick", "fast"; ὠκύς keeps the "swift" of the shipped ὠκύμοροι 'swift-doomed' (1.266), so "swift" now does for both θοός and ὠκύς |
| ἀγλαὸν ὕδωρ (3.429) | "splendid water" | "splendid water" | "bright", "clear", "sparkling water"; the table's ἀγλαός "splendid" is kept even where it sits oddly, and the note explains it once |
| πρέσβα (of Eurydice, 3.452, πρέσβα Κλυμένοιο θυγατρῶν) | "eldest" | "the eldest" (+ note: also a title of honour, 'august', so 'first in rank' is possible) | "august" / "honoured" as if certain; "eldest" follows the partitive genitive |
| πρήσσῃσιν ὁδοῖο (3.476) | "make headway on his road" | "make headway on his road" | "speed on his way", "accomplish his journey" (loses the partitive genitive, 'some of the road') |
| αὐτὰρ ἐπεὶ κατὰ μῆρ’ ἐκάη καὶ σπλάγχνα πάσαντο, / μίστυλλόν τ’ ἄρα τἆλλα καὶ ἀμφ’ ὀβελοῖσιν ἔπειραν (sacrifice-meal lines, 3.461–462) | "But when the thigh-pieces were burned up and they had tasted the entrails,\nthey cut up the rest then into pieces and pierced them around spits," | "But when the thigh-pieces were burned up and they had tasted the entrails, they cut up the rest into small pieces, pierced them on spits," | "thigh-bones" (the shipped word is "thigh-pieces", 3.9), "innards", "skewers", "chopped"; σπλάγχνα πάσαντο keeps the shipped "tasted the entrails" (3.9) |
| ἀμφὶ δέ μιν φᾶρος καλὸν βάλεν ἠδὲ χιτῶνα, / ἔκ ῥ’ ἀσαμίνθου βῆ δέμας ἀθανάτοισιν ὁμοῖος (bath-and-dress lines, 3.467–468) | "and about him a fine cloak had thrown and a tunic,\nout of the bath he stepped, in body like the immortals;" | "and thrown a fine cloak and a tunic about him, he stepped out of the bath, in body like the immortals;" | "robe" (shipped for Penelope's φᾶρος at 2.97, but a man's φᾶρος is his cloak), "mantle", "godlike" (reserved for ἀντίθεος), "like a god in form" (reserved for θεοειδής); δέμας keeps the shipped "in body" (2.268) |
| ἵππους τε ζεύγνυντ’ ἀνά θ’ ἅρματα ποικίλ’ ἔβαινον (3.492) | "both the horses they yoked, and up onto the inlaid chariot they stepped;" | "they yoked the horses and mounted the inlaid chariot;" | "many-coloured", "painted", "decorated"; ποικίλος keeps "inlaid", as shipped for the seat at 1.132 |
| ἐκ δ’ ἔλασαν προθύροιο καὶ αἰθούσης ἐριδούπου (3.493) | "and out they drove from the forecourt and the loud-echoing portico;" | "and drove out of the forecourt and the loud-echoing portico;" | "gateway", "porch", "vestibule"; πρόθυρον keeps "forecourt" (shipped in Book 1, odyssey-002), αἴθουσα ἐρίδουπος the table's "loud-echoing portico" |
| Μενελάου κυδαλίμοιο (4.2, 4.16, 4.23, 4.46, genitive) | "of Menelaus, glorious" | "of glorious Menelaus" | "renowned" (risks confusion with κλέος-root words), "illustrious", "far-famed" (reserved for τηλεκλυτός) |
| ὀτρηρὸς θεράπων / ὀτρηροὺς θεράποντας (4.23, sg., of Eteoneus; 4.38, pl.) | "brisk attendant" / "brisk attendants" | "brisk attendant" / "brisk attendants" | "busy squire", "ready servant", "nimble henchman" — ὀτρηρός is "quick, prompt, ready for service" |
| ὑψερεφές (of Menelaus's hall, 4.15 μέγα δῶμα, 4.46 δῶμα alone) | "high-roofed" | "high-roofed" | "lofty-roofed", "high-ceilinged", "towering" (too free — the compound is literally "roofed high") |
| ἐχέφρων Πηνελόπεια (4.111) | "sound-minded Penelope" | "sound-minded Penelope" | "prudent Penelope" (reserved for πεπνυμένος), "circumspect Penelope" (the already-fixed rendering of the distinct epithet περίφρων Πηνελόπεια — kept separate since Homer uses two different φρήν-compounds of her), "wise-hearted" (too close to the δαΐφρων reading already fixed for Odysseus) |
| χλαῖναν πορφυρέην ἄντ’ ὀφθαλμοῖιν ἀνασχών/ἀνασχὼν (whole-phrase gesture of hiding tears, 4.115 = 4.154) | "his purple cloak before his eyes having raised" | "raising his purple cloak before his eyes" | "mantle" (kept "cloak" for χλαῖνα throughout), "crimson"/"dark-red" for πορφύρεος (kept plainly "purple") |
| Ἀρτέμιδι χρυσηλακάτῳ ἐικυῖα (simile for a woman, 4.122) | "like to Artemis of the golden distaff" | "like Artemis of the golden distaff" | "golden-shafted" (ἠλακάτη is a spindle/distaff, not an arrow — kept apart from Artemis's bow), "golden-spindled" (less natural in English) |
| τὸν/τὴν δ’ αὖ [Name] [patronymic] ἀντίον ηὔδα (reply-formula: name + patronymic + ἀντίον ηὔδα, here Νεστορίδης Πεισίστρατος, 4.155) | "Him then in turn spoke [Name], [patronymic], face to face:" | "Then [Name], [patronymic], spoke to him in turn, face to face:" | "answered" (reserved for τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα); kept on the pattern already fixed for τὸν δ’ αὖτ’ Εὐρύμαχος Πολύβου πάϊς ἀντίον ηὔδα and τὸν δ’ Εὐηνορίδης Λειώκριτος ἀντίον ηὔδα |
| Ἀτρεΐδη Μενέλαε διοτρεφές, ὄρχαμε λαῶν (full vocative address line, 4.156) | "Atreus' son, Menelaus, Zeus-nurtured, chief of the people," | "Son of Atreus, Menelaus, Zeus-nurtured, chief of the people," | naming him "Menelaus" alone and dropping the patronymic or the titles; ὄρχαμε λαῶν kept distinct in wording from the already-fixed ὄρχαμος ἀνδρῶν ("chief of men") since λαός and ἀνήρ are different nouns |
| κυνῶπις (Helen's standing self-reproach, 4.145) | "dog-faced" | "shameless" | "bitch" (too coarse for the register and not what the compound says), "dog-eyed" (the table's usual "-ωπ- → -eyed" pattern fits γλαυκῶπις's eye-colour sense, but κυνῶπις's force is about shameless boldness, not eye colour, so "faced" is kept here), translating away the self-blame entirely |
| Ἀργείη Ἑλένη, Διὸς ἐκγεγαυῖα (whole phrase, 4.184) | "Argive Helen, sprung of Zeus," | "Argive Helen, the daughter sprung from Zeus," | "born of Zeus" (flattens the perfect participle's sense of 'having come to be'), "Zeus-born" (reserved for the distinct adjective διογενής), "child of Zeus" (reserved for the noun-phrase Διὸς θυγάτηρ, used of Athena; here Homer uses a participle, not θυγάτηρ, so the two are kept apart) |
| νηπενθές τ’ ἄχολόν τε (of Helen's drug, 4.221) | "grief-easing and anger-easing" | "that eased grief and eased anger" | "nepenthe" (bare transliteration, not a translation), "sorrow-quelling", "wrath-calming", "banishing pain and anger" (loses the privative-compound structure of both words) |
| Πολύδαμνα, Θῶνος παράκοιτις (4.228) | "Polydamna, Thon's consort" | "Polydamna, the wife of Thon" | "Thon's queen" (παράκοιτις is plain "bedfellow, wife", not a rank-title), embellishing either name as if their story were known |
| Παιήονός … γενέθλης ("of the race of Paieon", 4.232) | "of the race of Paieon" | "descended from Paieon" | "Paean" (confuses the god Paieon with the epithet/hymn-name Paean), "Apollo" (a distinct, though related, healing god in Homer), "the race of healers" (drops the proper name) |
| Ἄντικλος (proper name, 4.286) | "Antiklos" | "Antiklos" | Latinizing to "Antiklus"; the name is a hapax, occurring nowhere else in the poem, so it carries no epithet to fix and is rendered as a plain transliteration |
| τανύπεπλος (of Helen, 4.305) | "long-robed" | "long-robed" | "long-gowned", "trailing-robed" — a transparent compound (τανύ- "long, stretched" + πέπλος "robe"); fixed now as Helen's standing epithet since it is likely to recur with her elsewhere in the poem |
| γέρων ἅλιος νημερτής (Proteus's standing epithet, 349, 384, 401; cf. the plain back-references θείοιο γέροντος 395 and τοῖο γέροντος 410 once he has been introduced) | "the unerring old man of the sea" | "the unerring old man of the sea" | "the truthful old man of the brine" (over-poetic), "the never-lying old man of the sea", "unfailing" (loses the specific sense of ἀ- + ἁμαρτάνω, "not missing the mark, not erring") |
| ἀεικέα πότμον (339, 340 — the same two words repeated verbatim in successive lines, applying the lion-simile to the suitors) | "an unseemly doom" | "an unseemly doom" | "a shameful fate" (drifts from πότμος, "portion, doom"), "an unfitting death" (πότμος need not mean death specifically, though it does here), "a disgraceful end" |
| νόστον θ’, ὡς ἐπὶ πόντον ἐλεύσομαι/ἐλεύσεαι ἰχθυόεντα (381, 1st sg.; 390, 424, 2nd sg., once Eidothea addresses Menelaus in turn) | "and of my/your return, how I/you shall come upon the fish-teeming sea" | "and how I am/you are to make my/your way home across the fish-teeming sea" | "the fishy sea" (wrong connotation in English — "fishy" reads as "suspicious"), "the fish-filled main", "over the sea, teeming with fish" (too loose a paraphrase) |
| Πρωτέος ἰφθίμου θυγάτηρ ἁλίοιο γέροντος (365, introducing Eidothea) | "the daughter of mighty Proteus, the old man of the sea" | "the daughter of mighty Proteus, the old man of the sea" | collapsing this into the fuller formula γέρων ἅλιος νημερτής (νημερτής "unerring" is not present here, so the two phrases are kept distinct); "stalwart Proteus" for ἴφθιμος (reserved plain "mighty") |
| ἀθάνατος Πρωτεὺς Αἰγύπτιος (385) | "immortal Proteus the Egyptian" | "immortal Proteus of Egypt" | "the deathless Proteus" (ἀθάνατος is kept as "immortal" throughout, e.g. ἀθανάτοισι θεοῖς), "Proteus who cannot die" (paraphrase) |
| καλῆς ἁλοσύδνης (404, of the seals' mother, a byname for a sea-goddess usually identified with Amphitrite) | "fair Halosydne" | "fair Halosydne" (+ note: an epithet-name for a sea-goddess, meaning disputed) | translating it as a common noun ("the fair sea-nymph"), which would erase the fact that ἁλοσύδνη functions here as a proper name whose sense is itself uncertain |
| νέποδες (404, of the seals as Halosydne's "children") | "offspring" | "children" (+ note: meaning/formation disputed) | "brood" (too avian), "spawn" (misleadingly narrows to fish/frogs) |
| ἐύσσελμος (409, of ships) | "well-benched" | "well-benched" | "well-decked", "well-timbered", "well-built" (reserved for ἐυκτίμενος); kept apart from the already-fixed νηῦς ἐίση, θοὴ νηῦς μέλαινα and κοίλη νηῦς μέλαινα |
| ὀλοφώια (410, substantival, of Proteus's shape-shifting) | "baneful wiles" | "baneful tricks" | "harmful arts" (correct sense but the formation is disputed, so "baneful" is kept, echoing the guessed connection with ὄλλυμι "destroy"), "destructive tricks" |
| θεσπιδαὲς πῦρ (418, one of Proteus's transformations) | "wondrous-blazing fire" | "wondrous-blazing fire" | "divine fire" (loses the δαίω "burn" half of the compound), "prodigious flame" |
| εὐρύπορος (432, of the sea) | "wide-wayed" | "wide-wayed" | "wide-pathed", "broad-tracked" — kept parallel to the already-fixed χθὼν εὐρυόδεια, "the wide-wayed earth" |
| ἐπ’ εὐρέα νῶτα θαλάσσης (362, "the broad back of the sea"; νῶτα is grammatically plural but pictures one continuous surface) | "the broad back of the sea" | "the sea's broad back" | "the broad backs of the sea" (keeping the Greek plural literally reads oddly in English; the plural-for-singular idiom is kept singular, as already practised for ἦτορ ἑταίρων) |
| αἲ γάρ, Ζεῦ τε πάτερ καὶ Ἀθηναίη καὶ Ἄπολλον (341, whole-line wish-opening) | "Would that — Father Zeus, and Athena, and Apollo —" | "If only — Father Zeus, Athena, and Apollo —" | "O Father Zeus" (drops the αἲ γάρ wish-force entirely), naming the three gods without any wish-particle |
| τὸν δ’ υἱὸς Φρονίοιο Νοήμων ἀντίον ηὔδα (reply-formula, 4.648) | "Him then the son of Phronius, Noemon, addressed, face to face:" | "Then Noemon, son of Phronius, spoke to him in turn, face to face:" | "answered" (reserved for τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα); unlike the already-fixed τὸν δ’ αὖτ’ [Name] [patronymic] ἀντίον ηὔδα pattern, here the patronymic periphrasis stands before the name and αὖ is absent, so it is kept as its own distinct formula rather than folded into that one |
| ὣς ἄρα φωνήσας ἀπέβη (masc. closing formula, 4.657 = 4.715) | "So then having spoken, away he went" | "So he spoke, and went off" | folding it into the already-fixed feminine ὣς ἄρα φωνήσασ’ ("So then having spoken," / "So she spoke, and") — the two are kept as parallel but separate entries, one masculine and one feminine, exactly as the table already does for the ὣς ἐφάμην reply-formula (masc. vs. fem., 4.464/4.471) |
| τοῖσιν δ’ Ἀντίνοος μετέφη Εὐπείθεος υἱός (speech-introduction formula, 4.660) | "Among them then spoke Antinous, Eupeithes’ son," | "Among them Antinous, son of Eupeithes, spoke," | "addressed" (reserved for προσέειπε/προσέφη), "answered" (reserved for ἠμείβετο); built like the already-fixed τοῖσι δὲ μύθων ἦρχε / τοῖσι δὲ καὶ μετέειπε lines but on μετέφη, a third aorist of "speak among", filled with name and patronymic |
| τὸν δὲ κατ’ οὐδοῦ βάντα προσηύδα Πηνελόπεια (approach-and-address formula, 4.680) | "And him, as he stepped down upon the threshold, Penelope addressed:" | "And Penelope spoke to him as he stood there on the threshold:" | "answered" (reserved for ἠμείβετο); a new variant on the standing-at-the-threshold picture, kept apart from the plain reply-formulas since it specifies where the herald was standing when addressed |
| Μέδων πεπνυμένα εἰδώς (Medon's standing epithet, 4.696, 4.711) | "Medon, prudent counsels knowing" | "Medon, a man versed in prudent counsels" | inventing new wording; this reuses the table's already-fixed πεπνυμένα μήδεα εἰδώς ("prudent counsels knowing" / "a man versed in prudent counsels") with μήδεα left elliptical, the same sense, now fixed as Medon's own recurring epithet |
| ὀψὲ δὲ δή μιν ἔπεσσιν ἀμειβομένη προσέειπε ("at last" reply-formula, 4.706) | "But at last, answering him with words, she addressed him:" | "But at last she found her voice, and answered him:" | "answered" as the finite verb alone (reserved for ἠμείβετο); ὀψέ "late, at last" marks the delay just narrated (her seized voice, 4.704–705), so it is kept as its own formula rather than assimilated to the plain reply-formulas |
| τῇς δ’ ἁδινὸν γοόωσα μετηύδα Πηνελόπεια (speech-introduction formula, 4.721) | "And among them, sobbing heavily, spoke Penelope:" | "And Penelope, sobbing heavily, spoke among them:" | "addressed" (reserved for προσέειπε/προσέφη); μετηύδα keeps the "spoke among" sense already established for μετέφη/μετέειπε-type verbs; ἁδινόν "thick, close-packed" is kept as "heavily" rather than "bitterly" or "loudly", to preserve the image of a thick flood of tears |
| τοῦ κλέος εὐρὺ καθ’ Ἑλλάδα καὶ μέσον Ἄργος (whole phrase, of Odysseus's fame, 4.726) | "whose fame is wide throughout Hellas and mid-Argos" | "whose fame spread wide through Hellas and the middle of Argos" | "throughout Greece" (anachronistic — Ἑλλάς here is a district of Thessaly, not the later whole of Greece, and is kept as the transliterated name "Hellas"); this is Penelope's signature line about Odysseus and is likely to recur elsewhere in the poem, so it is fixed now |
| εἴδωλον (of the dream-phantom Athena creates, 4.796 and passim) | "phantom" | "phantom" | "image", "likeness" (both lose the standing supernatural sense the word will carry at its later recurrences, e.g. of the shades in the underworld), "ghost" (wrong register — this εἴδωλον is a living construct sent by a goddess, not a spirit of the dead), "wraith" |
| τὴν δ’ ἀπαμειβόμενον προσέφη εἴδωλον ἀμαυρόν (reply-formula, 4.824 = 4.835, verbatim) | "Her answering addressed the dim phantom:" | "In answer the dim phantom said to her:" | "the faint wraith" (loses the fixed noun "phantom" above), "shadowy" for ἀμαυρόν (its plain sense "dim, faint, indistinct" is kept literal, not itself disputed) |
| φίλη τροφὸς Εὐρύκλεια (Eurycleia's standing name-periphrasis, 4.742) | "the dear nurse Eurycleia" | "her dear nurse Eurycleia" | "old nurse" (drops φίλη's warmth), "nurse Eurycleia" alone (drops φίλη) |
| νύμφα φίλη (Eurycleia's affectionate address to Penelope, 4.743) | "Dear bride" | "Dear lady" | "my dear child" (over-interprets; νύμφη is literally "young wife, bride", kept literal in `l`), "my dear" alone (loses the address form), "dear daughter" (Penelope is not Eurycleia's daughter) |
| Ἀτρυτώνη (cult-title of Athena, 4.762) | "Atrytone" | "Atrytone" (+ note: traditionally "the Unwearied", ἀ- + τρύω, but the formation is irregular and the sense not fully certain) | "the Unwearied" or "the Untiring" as if certain (silently picks one guess); "tireless one" |
| ὀνειρείῃσι πύλῃσιν ("at the gates of dreams", 4.809) | "at the gates of dreams" | "at the gates of dreams" | "in a dream-gate" (loses the plural), "dreaming at the threshold" (too free); kept literal since Book 19 later elaborates the image into gates of horn and of ivory |
| ὣς φάτο (used of a female speaker; cf. the existing row for the masculine) | "So she spoke" | "So she spoke" | "So she said", "Thus she spoke" (keep one form throughout, exactly as fixed for the masculine — the pronoun alone tracks the actual speaker's sex, the wording after it does not vary) |
| Ἠὼς δ’ ἐκ λεχέων παρ’ ἀγαυοῦ Τιθωνοῖο / ὤρνυθ’, ἵν’ ἀθανάτοισι φόως φέροι ἠδὲ βροτοῖσιν· (whole two-line dawn-formula, 5.1–2) | "And Dawn from her bed, from beside noble Tithonus, / was rising, so that to the immortals she might bring light, and to mortals;" | "And Dawn rose from her bed beside noble Tithonus, to bring light to the immortals and to mortals alike;" | "rosy-fingered Dawn" (that is the separate, already-fixed ἠριγένεια ῥοδοδάκτυλος formula), naming Tithonus "her husband" outright (the Greek leaves the relationship implicit) |
| ὑψιβρεμέτης (epithet of Zeus, 5.4) | "high-thundering" | "who thunders on high" | "loud-thundering" (risks blurring with the already-fixed εὐρύοπα Ζεύς "far-thundering Zeus", a different compound), "high-roaring" |
| πατρίδα γαῖαν (recurring noun-phrase, 5.15, 26, 37, 42, with varying possessives ἥν/ἑήν/φίλην) | "fatherland" (with whatever possessive the line supplies: "his own fatherland", "his dear fatherland") | "fatherland" (same) | "native land", "home country" — kept parallel to, but distinct from, the already-fixed φίλη πατρὶς αἶα, a different formula built on the noun αἶα rather than γαῖα (5.15 itself is an exact repeat of an already-published line and keeps that line's own "native land", by the exact-repeat rule) |
| σχεδίη πολύδεσμος (5.33, "σχεδίης πολυδέσμου") | "raft of many bonds" | "raft of many lashings" | "makeshift raft", "patched raft" (both add a pejorative note absent from the Greek), "well-lashed raft" (πολυ- is "many", not "well") |
| Σχερίη ἐρίβωλος (5.34) | "rich-clodded Scheria" | "rich-soiled Scheria" | "fertile Scheria" (loses the concrete βῶλος "clod of earth" image), "rich Scheria" alone (loses the soil-image entirely) |
| Φαίηκες ἀγχίθεοι (5.35, "Φαιήκων ... οἳ ἀγχίθεοι γεγάασιν") | "close to the gods" | "close to the gods" | "god-like" (reserved for ἀντίθεος/θεοειδής), "near-divine", "akin to the gods" (overstates; ἀγχι- is "near, close by", not "kin to") |
| λάρῳ ὄρνιθι ἐοικώς (simile-formula, 5.51) | "like a gull, a bird," | "in the likeness of a gull" | "gull-like" (loses ἐοικώς's participial force), "as a seagull" (drops ὄρνιθι, the noun in apposition) |
| ἰοειδής (of the sea, 5.56 "πόντου ... ἰοειδέος") | "violet-dark" | "violet-dark" | "violet-coloured" (clumsy), collapsing it into any of the already-fixed sea-epithets (οἶνοψ "wine-faced", πολιή "grey", ἠεροειδής "misty-looking") — this is a fourth, distinct colour-word for the sea and is kept separate |
| δάκρυα λείβων (5.84; distinct from the already-fixed δάκρυ χέων) | "tears pouring" | "pouring out his/her tears" | "shedding tears" (reserved for the separate, already-fixed δάκρυ χέων, a different verb), "weeping" (drops λείβω's specific pouring image) |
| χρυσόρραπις (standing epithet of Hermes, 5.87 "Ἑρμεία χρυσόρραπι") | "of the golden wand" | "of the golden wand" | "gold-wanded" (awkward compound), "with the golden staff" (staff is reserved for σκῆπτρον-type words), "golden-rod" (misleading modern plant-name association) |
| αἰδοῖός τε φίλος τε (formula of welcome to a guest, 5.88) | "both honored and dear" | "honored and dear" (as a description of the arriving guest) | "revered and beloved" (too solemn for the register), "respected and loved" (flattens; αἰδώς is specifically the respect owed a guest, not general esteem) |
| τίπτε μοι, Ἑρμεία χρυσόρραπι, εἰλήλουθας / αἰδοῖός τε φίλος τε; (Calypso's whole opening address to Hermes, 5.87–88, combining the two rows above) | "Why, to me, Hermes of the golden wand, have you come, / both honored and dear?" | "Why have you come to me, Hermes of the golden wand — honored guest and dear?" | any wording that breaks up χρυσόρραπι or αἰδοῖός τε φίλος τε from their own fixed renderings above |
| μιν ἔπεσσιν ἀμειβόμενος/η προσέειπε(ν) (reply-formula built on two verbs, masculine at 5.96; a feminine counterpart is already fixed elsewhere with a different lead-in, ὀψὲ δὲ δή) | "with words, answering, he/she addressed him/her:" | "he/she answered him/her, and spoke:" | "answered" alone (loses προσέειπε's "addressed"), "replied" (too flat for a two-verb formula), collapsing the masculine into the already-fixed feminine ὀψὲ δὲ δή variant, whose lead-in differs |
| πολύτλας (standing epithet of Odysseus, first at 5.171) | "much-enduring" | "much-enduring" | "long-suffering" (drops πολυ- "much" and adds a meek, patient tone the word does not have), "much-suffering" ("suffering" belongs to the πάσχω family, as in ἄλγεα πάσχων; τλάω is "endure, bear up under"), "steadfast" (already the `i` of ταλασίφρων, and a claim about moral character where the Greek says literally what he has borne), "enduring-minded" (reserved for ταλασίφρων), "patient" |
| πολύτλας δῖος Ὀδυσσεύς (whole name-formula, line-end, 5.171) | "much-enduring, heavenly Odysseus" | "much-enduring, heavenly Odysseus" | dropping either epithet; "divine" for δῖος (reserved for θεῖος); reordering the epithets round the name |
| ὣς φάτο, ῥίγησεν δὲ [Name] (reaction-formula after a speech, 5.116 of Calypso, 5.171 of Odysseus) | "So he/she spoke, and shuddered, [Name]," | "So he/she spoke, and [Name] shuddered," | "was dismayed", "was troubled", "was alarmed" (each loses the bodily chill of ῥιγέω, from ῥῖγος "cold, frost"), "trembled" (keep for τρέω/τρομέω), "shivered" (sounds like cold weather); built on the shipped pattern of ὣς φάτο, μείδησεν δὲ [Name] |
| ἀγχοῦ δ’ ἱσταμένη/ἱστάμενος + verb of speaking (5.159 with προσεφώνεε; cf. the shipped ἀγχοῦ δ’ ἱστάμενος ἔπεα πτερόεντα προσηύδα, 4.25) | "And standing close by, …" | "came and stood close beside him/her, and …" | "approaching" (drops ἵστημι), "addressed" for προσεφώνεε (reserved for προσέειπε/προσέφη) |
| [ἀλλὰ μάλ’ / ἀλλ’ ἐπεὶ] οὔ πως ἔστι Διὸς νόον αἰγιόχοιο / οὔτε παρεξελθεῖν ἄλλον θεὸν οὔθ’ ἁλιῶσαι (two-line formula, 5.103–104 = 5.137–138 except for the opening words) | "[But there is no way at all / But since there is no way] that the mind of aegis-bearing Zeus / any other god should either slip past or bring to nothing" | "… for any other god to slip past the mind of aegis-bearing Zeus or bring it to nothing" | "thwart", "circumvent", "cross" (lose the literal παρ-εξ-ελθεῖν "go out past"), "make void"/"frustrate" alone (lose ἅλιος "fruitless, vain", kept as "bring to nothing"), "will"/"purpose" for νόος (the pilot's "mind") |
| ἔνθ’ ἄλλοι μὲν πάντες ἀπέφθιθεν ἐσθλοὶ ἑταῖροι, / τὸν δ’ ἄρα δεῦρ’ ἄνεμός τε φέρων καὶ κῦμα πέλασσε. (two whole lines, 5.110–111 = 5.133–134) | "There all the others perished, his good companions, / but him, then, the wind, bearing him, and the wave brought near to here." | "There all his other good companions perished, but the wind and the wave carried him and brought him here." | "noble companions" (ἐσθλός is kept "good"), "washed him ashore" (drops πελάζω "bring near") |
| μή τί μοι/τοι αὐτῷ πῆμα κακὸν βουλευσέμεν ἄλλο (whole line, 5.179 and 5.187 with μοι/τοι) | "that you/I will not plan some other evil woe against me/you myself/yourself" | "that you/I will not plan some other evil woe against me/you" | "harm"/"mischief" alone (πῆμα is kept "woe"), "plot" (keep for λοχάω/δόλος words) |
| ἴστω νῦν τόδε γαῖα καὶ οὐρανὸς εὐρὺς ὕπερθε / καὶ τὸ κατειβόμενον Στυγὸς ὕδωρ, ὅς τε μέγιστος / ὅρκος δεινότατός τε πέλει μακάρεσσι θεοῖσι (the gods' oath by the Styx, 5.184–186) | "Let now the earth know this, and the wide sky above, / and the down-flowing water of the Styx, which is the greatest / oath and the most dread for the blessed gods," | "Now let the earth know this, and the wide sky above, and the down-flowing water of the Styx, which is the greatest and most dread oath for the blessed gods," | "be my witness" (the verb is οἶδα, "know"), "the dread river Styx" (the Greek names its water, ὕδωρ), "falling water"/"cascading" for κατειβόμενον (kept "down-flowing") |
| χρυσόθρονος (of Artemis, 5.123) | "golden-throned" | "golden-throned" (+ note: an old alternative derives the second part from θρόνα "embroidered flowers") | "of the golden flowers" or "golden-robed" as if certain; "gold-enthroned" |
| Ἄρτεμις ἁγνή (5.123) | "Artemis the pure" | "Artemis the pure" | "holy" (reserved for ἠγάθεος), "sacred" (ἱερός), "chaste" (narrows ἁγνός to a sexual sense) |
| ἀργῆτι κεραυνῷ (5.128, 5.131) | "with the bright thunderbolt" | "with the bright thunderbolt" | "flashing" (reserved elsewhere), "shining" (keep for φαεινός), "white" (literal but misleading), "vivid"; kept distinct from the shipped κύνες ἀργοί "swift dogs" |
| θεοὶ ῥεῖα ζώοντες (5.122; shipped at 4.805) | "the gods who live at ease" | "the gods who live at ease" | "the easy-living gods", "the blessed gods" (that is μάκαρες) |
| [οἷς] ἀγανοῖς βελέεσσιν ἐποιχόμενος/ἐποιχομένη κατέπεφνε(ν) (5.124, fem., of Artemis; shipped masc. at 3.280, of Apollo) | "with his/her gentle shafts assailing, slew" | "came upon … with his/her gentle arrows and killed …" | "kindly arrows", "painless darts" (the note, not the translation, says the death is sudden and painless) |
| μίγη/μιγῆναι φιλότητι καὶ εὐνῇ (5.126) | "was mingled in love and in bed" | "lay in love with …" | "made love", "slept with" (flatten μίγνυμι "mix, mingle"), "was joined" |
| κάμμορε (vocative address, 5.160) | "Ill-fated one" | "Ill-fated man" | "wretch", "poor fool", "unlucky one", "unhappy man" (κάμμορος = κατάμορος, built on μόρος "portion"); shares its English with the already-fixed δύσμορος "ill-fated" (1.49, 2.351) — accepted as near-synonyms, both built on μόρος |
| νῆες ἐῖσαι ὠκύποροι (5.175–176) | "well-balanced ships, swift-faring" | "well-balanced, swift-faring ships" | "sea-going", "fast-sailing", "quick-passaged"; ὠκύς keeps the table's "swift", ἐῖσαι keeps the table's "well-balanced" (sense of ἐῖσαι itself uncertain, flagged since 3.10) |
| πρόφρων (of a willing helper, 5.143; shipped at 2.230 as "ready-minded"), with the epic feminine πρόφρασσα (5.161) | "ready-minded" | "with a ready mind" | "gladly", "eagerly", "kindly" (lose φρήν), "wholeheartedly" |
| διογενὲς Λαερτιάδη, πολυμήχαν’ Ὀδυσσεῦ (whole-line vocative address to Odysseus, 5.203) | "Zeus-sprung son of Laertes, many-devising Odysseus," | "Zeus-born son of Laertes, Odysseus, man of many devices," | "Laertiades" (a transliteration, not a translation), "resourceful" (turned down in the table's πολυμήχανος row), "godlike" (reserved for ἀντίθεος); each word keeps its own fixed table rendering (διογενής, πολυμήχανος), and only the patronymic is new |
| τὴν δ’ ἀπαμειβόμενος προσέφη πολύμητις Ὀδυσσεύς (whole-line reply-formula, 5.214) | "Her answering addressed many-wiled Odysseus:" | "In answer Odysseus of many wiles said to her:" | "answered" (reserved for ἠμείβετο), "resourceful" / "of many devices" (reserved for πολυμήχανος, which Calypso uses of him eleven lines earlier at 5.203; the two epithets are kept apart); built on the table's τὴν δ’ ἀπαμειβόμενος προσέφη and πολύμητις rows |
| πότνα θεά (vocative address to a goddess, 5.215) | "Lady goddess" | "Lady goddess" | "Queen" (reserved for ἄνασσα), "Mistress", "Honoured goddess", "Great goddess"; πότνα is the short vocative of πότνια, shipped as "lady" (πότνια νύμφη "the lady nymph", 1.14; πότνια Ἥρη "the lady Hera", 4.513) |
| κρείων ἐνοσίχθων (of Poseidon, 5.282) | "the lord earth-shaker" | "the lord earth-shaker" | "the mighty earth-shaker", "the ruling earth-shaker"; κρείων keeps the "lord" shipped for κρείων Ἐτεωνεύς (4.22), and ἐνοσίχθων keeps the table's "earth-shaker" |
| κινήσας δὲ κάρη προτὶ ὃν μυθήσατο θυμόν (whole-line introduction to a speech made to oneself, 5.285) | "and, shaking his head, he spoke to his own heart:" | "and shaking his head he spoke to his own heart:" | "said to himself" (drops θυμός), "tossing his head", "nodding" (κινέω is 'move, shake'), "spirit" for θυμός (θυμός is "heart", as in ὃν κατὰ θυμόν 1.4) |
| μέλας οἶνος (5.265, μέλανος οἴνοιο) | "dark wine" | "dark wine" | "black wine" (misleading in English, though μέλας is "black" of ships in θοὴ νηῦς μέλαινα), "red wine" (a modern category), "ruddy"; kept apart from the table's αἶθοψ οἶνος "the fire-faced wine" |
| ὄρεα σκιόεντα (5.279) | "the shadowy mountains" | "the shadowy mountains" | "shady mountains" (suggests shade-trees), "dim", "dark mountains" (loses σκιά 'shadow') |
| οὖρος ἀπήμων τε λιαρός τε (5.268, οὖρον … ἀπήμονά τε λιαρόν τε) | "a fair wind, harmless and warm" | "a fair wind, harmless and warm" | "gentle", "soft", "balmy" (λιαρός is 'warm, mild'), "safe" (drops πῆμα, which ἀπήμων shares with the oath-line μή τί μοι αὐτῷ πῆμα κακὸν βουλευσέμεν ἄλλο); οὖρος keeps the shipped "fair wind" |
| φορτὶς εὐρεῖα (5.250, νηὸς … φορτίδος εὐρείης) | "a broad freighter" | "a broad freighter" | "merchantman" (period-specific), "cargo-boat", "trading-vessel"; φορτίς is from φόρτος 'cargo' |
| καὶ τότ’ [Name] λύτο γούνατα καὶ φίλον ἦτορ (5.297; cf. the shipped τῆς δ’ αὐτοῦ λύτο γούνατα καὶ φίλον ἦτορ, 4.703) | "And then [Name]’s knees were loosed, and his/her dear heart," | "And then [Name]’s knees gave way, and his/her heart too," | "his strength failed", "his spirit sank", "his heart melted" (each drops the concrete knees, which are the image); "limbs" for γούνατα; `l` and `i` follow the wording shipped at 4.703 |
| ὀχθήσας δ’ ἄρα εἶπε πρὸς ὃν μεγαλήτορα θυμόν (whole-line introduction to a speech made to oneself, 5.298 = 5.355) | "and, vexed, he then spoke to his own great-spirited heart:" | "and, troubled, he spoke to his own great-spirited heart:" | "deeply moved", "in anguish", "groaning" (ὀχθέω is 'be vexed, troubled', shipped as "greatly vexed" / "greatly troubled" for μέγ’ ὀχθήσας at 4.30, 4.332); "said to himself" (drops θυμός); "great-hearted" (reserved for μεγάθυμος) — μεγαλήτωρ keeps "great-spirited"; kept apart from the fixed κινήσας δὲ κάρη προτὶ ὃν μυθήσατο θυμόν ("and, shaking his head, he spoke to his own heart:") |
| ὤ μοι ἐγὼ δειλός (5.299) / ὤ μοι ἐγώ (5.356) (cries of distress opening a speech) | "Oh me, I, miserable one," / "Oh me, I …" (ἐγώ is part of the cry; at 5.356 `l` joins it to the fear-clause: "Oh me, I fear …") | "Oh me, miserable that I am," / "Oh me," | "Ah" / "Ah me" (reserved for ὢ πόποι), "Alas" (archaic, and it would swallow several distinct cries), "Woe is me" (archaic), "Poor me" (childish); δειλός is "miserable", kept apart from δύστηνος ("wretched", 1.55) and from λευγαλέος ("pitiful", below) |
| ἀλλὰ μάλ’ ὧδ’ ἔρξω, δοκέει δέ μοι εἶναι ἄριστον (whole line, 5.360), with its second-person counterpart ἀλλὰ μάλ’ ὧδ’ ἔρξαι, δοκέεις δέ μοι οὐκ ἀπινύσσειν (5.342) | "But I will do just this, and it seems to me to be best:" / "But do just this, and you seem to me not to lack sense:" | "But this is what I will do, and it seems to me the best:" / "But do just this, for you seem to me a man not lacking in sense:" | "Here is my plan", "This is what I shall do" alone (drops μάλ’ ὧδ’ 'just thus'); "you look like a sensible man", "you seem no fool" in `l` (ἀπινύσσω 'lack understanding' kept literal, the litotes explained in the note) |
| τά οἱ πόρε δῖα Καλυψώ (second half-line, 5.321 = 5.372, of the clothes) | "which heavenly Calypso had given him" | "which heavenly Calypso had given him" | "bestowed", "provided", "furnished" (πόρε is plain 'gave'), "divine Calypso" (δῖος keeps "heavenly") |
| Εὖρος · Νότος · Ζέφυρος · Βορέης (the four winds as named figures, all four in 5.295–296) | "the East Wind" · "the South Wind" · "the West Wind" · "the North Wind" | same | "Eurus", "Notus", "Zephyr", "Boreas" (transliterations that hide the plain sense; "the South Wind" and "the West Wind" follow the shipped 3.295 and 2.421); "south-easter" for Εὖρος (the exact quarter is uncertain, and the note does not claim more) |
| Ζέφυρος δυσαής (5.295) | "the ill-blowing West Wind" | "the ill-blowing West Wind" | "stormy", "boisterous", "blustering", "wild" (lose δυσ- 'bad' + ἄημι 'blow'); "the harsh West Wind" |
| Βορέης αἰθρηγενέτης (5.296) | "the North Wind born of the clear air" | "the North Wind born of the clear air" (+ note: or active, 'bringing clear skies'; disputed) | "sky-clearing North Wind" (silently picks the active reading), "the bright-born North Wind", "born in the upper air" (αἴθρη is clear sky, not the gods' αἰθήρ) |
| ὀπωρινὸς Βορέης (5.328) | "the late-summer North Wind" | "the late-summer North Wind" | "autumn North Wind" (ὀπώρα is the season at the end of summer when fruit ripens, not autumn as an English season), "harvest wind" |
| κραιπνὸς Βορέης (5.385) | "the rushing North Wind" | "the rushing North Wind" | "swift" (already does for θοός and ὠκύς), "rapid", "fleet" |
| ἄνεμος ζαής (5.368) | "a hard-blowing wind" | "a hard-blowing wind" | "strong", "violent", "furious" (lose ἄημι 'blow'); ζα- is the intensive already met in ζατρεφέας "well-fed" |
| ἄελλα · θύελλα (5.292, 5.304; 5.317) | "blast" (ἄελλαι παντοίων ἀνέμων "the blasts of winds of every kind") · "storm-blast" | same | "gale", "tempest", "hurricane"; θύελλα keeps the "storm-blast" shipped at 4.515; ἄελλα, shipped as "storm-blasts" (3.283) and "storms" (3.320), is here plain "blast", the genitive ἀνέμων supplying the wind, so the two nouns stay apart |
| Κάδμου θυγάτηρ, καλλίσφυρος Ἰνώ, / Λευκοθέη (5.333–334) | "the daughter of Cadmus, fair-ankled Ino, / Leucothea" | "the daughter of Cadmus, fair-ankled Ino, Leucothea" | "slim-ankled", "lovely-ankled", "trim-ankled" (καλλι- is "fair"); "the White Goddess" in place of the name (the note glosses Λευκοθέη as 'White Goddess' once) |
| βροτὸς αὐδήεσσα (5.334) | "a mortal endowed with speech" | "a mortal, speaking with a human voice" (+ note: the ancient explanation; exact force of αὐδήεις debated) | "a mortal woman who could speak" (flat), "a mortal with a voice", "a mortal of sweet voice" (adds a quality not in the word), "a mortal of human speech" (the drafted wording, withdrawn at review as remembered English) |
| κρήδεμνον (Ino's gift, 5.346, 351, 373) | "head-veil" | "head-veil" | "veil" (shipped for καλύπτρη, 5.232; NB the shipped 1.334 already has "veil" for Penelope’s λιπαρὰ κρήδεμνα, and 4.623 "fair-veiled" for καλλικρήδεμνοι — "head-veil" stays compatible with both, and both stand as shipped), "wimple", "mantilla", "scarf", "sash", "girdle" (it is tied under the chest here, but the word names a head-covering, κάρη + δέω); "covering", shipped at 3.392 for the lid-cloth of a wine-jar, is kept for that sense only |
| ἄμβροτος (5.347, κρήδεμνον … ἄμβροτον) | "deathless" | "deathless" | "immortal" (reserved for ἀθάνατος), "ambrosial" (reserved for ἀμβρόσιος, shipped in "ambrosial night"), "divine" (reserved for θεῖος) |
| αἰθυίῃ ἐικυῖα (5.337, 5.353) | "like to a shearwater" | "like a shearwater" (+ note: the bird's kind is not known) | "gull" (reserved for λάρος, 5.51), "diver" (reads as a human diver), "cormorant", "sea-mew", "sea-bird" (too vague for a named species); ἐικυῖα keeps the table's "like to" in `l` and "like" in `i`, as in Ἀρτέμιδι χρυσηλακάτῳ ἐικυῖα |
| εἶπέ τε μῦθον (half-line speech introduction at line-end, 5.338) | "and uttered a speech:" | "and spoke:" | "and said these words" (that would be ἔπεα), "and spoke a word" (reserved for ἔπος τ’ ἔφατ’ in the fixed ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε), "addressed" (reserved for προσέειπε / προσέφη) |
| τρὶς μάκαρες … καὶ τετράκις (5.306) | "Three times blessed …, and four times" | "Three times blessed … and four times over" | "thrice blessed" (archaic), "happy" / "lucky" (μάκαρ is the word used of the gods, 'blessed'), "a thousand times happier" |
| χαλκήρεα δοῦρα (5.309) | "bronze-fitted spears" | "bronze-fitted spears" | "bronze-tipped", "bronze-headed", "bronze spears"; follows the shipped χαλκήρεας ἰούς "bronze-fitted arrows" (1.262) |
| Πηλεΐων (name-substitute for Achilles, 5.310) | "the son of Peleus" | "the son of Peleus" | naming him "Achilles" where the Greek uses the patronymic alone; built like the table's Ἀτρεΐδης / Τυδέος υἱός rows |
| λευγαλέος θάνατος (5.312) | "a pitiful death" | "a pitiful death" | "wretched" (reserved for δύστηνος), "miserable" (now δειλός), "grievous" (reserved for λυγρός / ἀργαλέος), "shameful", "ignoble"; λευγαλέος of persons was shipped at 2.61 as "feeble" — a different use of the word |
| τέλος θανάτου (5.326) | "the end of death" | "the end that death brings" | "the doom of death", "death's fulfilment", "certain death" (drops τέλος) |
| μέλαν κῦμα (5.353) | "the dark wave" | "the dark wave" | "black wave" (μέλας is "black" of ships, but "black wave" misleads in English), "dark-blue"; kept parallel to μέλας οἶνος "dark wine" |
| δόλον ὑφαίνειν (5.356, μή τίς μοι ὑφαίνῃσιν δόλον) | "weave a trick" | "weave a trick" | "plot", "scheme", "hatch a plan" (lose the weaving image); δόλος keeps the "trick" shipped at 2.93, 4.437, 4.452 |
| Φαίηκες φιλήρετμοι (5.386, Φαιήκεσσι φιληρέτμοισι) | "the oar-loving Phaeacians" | "the oar-loving Phaeacians" | "seafaring Phaeacians", "the Phaeacians who love the oar"; φιλήρετμος keeps the table's "oar-loving" (shipped of the Taphians) |
| ἄνθρωποι διοτρεφέες (5.378, of the Phaeacians) | "Zeus-nurtured men" | "Zeus-nurtured men" | "men nurtured by Zeus", "god-nurtured men", "Zeus-born" (reserved for διογενής); keeps the table's διοτρεφέες βασιλῆες "Zeus-nurtured kings" |
| αὐτὰρ Ἀθηναίη κούρη Διὸς ἄλλ’ ἐνόησεν (whole line, 5.382) | "But Athena, daughter of Zeus, devised another thing." | "But Athena, daughter of Zeus, thought of something else." | "had another plan", "had a new idea"; built from the fixed Ἀθηναίη κούρη Διός ("Athena, daughter of Zeus") and the fixed ἔνθ’ αὖτ’ ἄλλ’ ἐνόησε θεά, γλαυκῶπις Ἀθήνη ("devised another thing" / "thought of something else") |
| κλυτὰ δώματα (5.381) | "famous halls" | "famous halls" | "renowned" (reserved for ἀγακλυτός), "far-famed" (reserved for τηλεκλυτός), "glorious" (reserved for φαίδιμος), "palace"; applies the table's note that "famous" is kept for κλυτός |
| ἄλγε’ ἔχοντα (5.336) beside ἄλγεα πάσχων (5.362) | "having pains" · "suffering pains" | "beset by pains" · "suffering pains" | collapsing the two into one: ἔχω 'have, hold' and πάσχω 'suffer' are different verbs; ἄλγεα πάσχων keeps the shipped "suffering pains" (4.372), and ἄλγε’ ἔχουσιν was shipped as "pains have" (1.34) |
| ἱμάσσω (5.380, ἵμασεν καλλίτριχας ἵππους) | "lashed" | "lashed" | "whipped" (reserved for μαστίζω, table row μάστιξεν δ’ ἐλάαν), "urged on", "drove" (lose ἱμάς 'strap') |
| πέλαγος (5.330 ἂμ πέλαγος; 5.335 ἁλὸς ἐν πελάγεσσι) | "the open sea" (unhyphenated) / "the salt-sea’s open waters" | "the open sea" / "the open waters of the salt sea" | "the open-sea" with a hyphen (reserved in `l` for πόντος), "the main", "the deep"; follows the shipped "open sea" for πέλαγος (3.91, 3.174, 3.179) |
| κύματι πηγῷ (5.388) | "on the strong-packed wave" | "on the heavy wave" (+ note: πηγός is a rare, disputed epithet — ancient link to πήγνυμι "make fast, compact", giving "massed, solid"; "strong, mighty" also guessed; not certain) | "the toilsome wave" (imports a sense not clearly present), "the surging wave" (too free, silently resolves the dispute) |
| ἐυπλόκαμος Ἠώς (5.390) | "fine-plaited Dawn" | "fine-plaited Dawn" | "rosy-fingered" (that is the separate, already-fixed ῥοδοδάκτυλος formula); ἐυπλόκαμος itself keeps the rendering already fixed for the nymph Calypso ("fine-plaited"), now extended to a second bearer of the same adjective |
| ἠιόνας τε παραπλῆγας λιμένας τε θαλάσσης (5.418 = 5.440, whole-line/half-line formula) | "beaches struck-by-the-surf, and harbours of the sea" | "surf-beaten beaches and harbours of the sea" | "storm-lashed" (overstates παραπλήξ, "struck on the side"), "sheltered coves" (too free), "safe harbours" (adds a judgement not in the Greek) |
| πουλύποδος θαλάμης ἐξελκομένοιο / πρὸς κοτυληδονόφιν πυκιναὶ λάιγγες ἔχονται (5.432–433, octopus simile) | "of an octopus dragged from its lair, to its suckers close-packed pebbles cling" | "when an octopus is dragged from its lair, thick-clustered pebbles cling to its suckers" | "den" for θαλάμη (kept "lair", a wild creature's home, distinct from any human dwelling-word), "tentacles" for the image generally (the Greek names only the octopus and its suckers), "stones" for λάιγγες (kept the more specific "pebbles") |
| ἐπιφροσύνη (5.437, Athena's saving gift) | "presence of mind" | "presence of mind" | "quick wit" (too casual a register), "cunning" (imports μῆτις-family connotations not present), "prudence" / "good sense" (both risk blending with the already-fixed πεπνυμένος "prudent", a different, settled-character word; ἐπιφροσύνη is a sudden, timely thought at a moment of crisis) |
| κλυτὸς Ἀμφιτρίτη (5.422) | "famous Amphitrite" | "famous Amphitrite" | "renowned" (reserved for ἀγακλυτός), "glorious" (reserved for φαίδιμος); κλυτός keeps its house rendering "famous" (as for κλυτὰ δώματα), applied here to a new proper name |
| κλυτὸς ἐννοσίγαιος (5.423) | "the famous earth-shaker" | "the famous earth-shaker" | collapsing it into the already-fixed κρείων ἐνοσίχθων "the lord earth-shaker"; ἐννοσίγαιος is a distinct compound (built on γαῖα, not χθών) with a distinct fixed epithet (κλυτός "famous" in place of κρείων "lord"), kept as its own formula |
| κλῦθι, ἄναξ, ὅτις ἐσσί (5.445, prayer-opening formula) | "Hear me, lord, whoever you are" | "Hear me, lord, whoever you may be" | "whoever you may be, hear me" (reorders away from the imperative-first shape of a Greek prayer-opening), "Lord, hear me" (drops ὅτις ἐσσί, the address to an unnamed local god by function alone, a genuine feature of Greek river- and place-cult) |
| ἱκέτης δέ τοι εὔχομαι εἶναι (5.450, supplication-formula) | "your suppliant I declare myself to be" | "I declare myself your suppliant" | "I am your suppliant" (loses εὔχομαι's formal, performative force — this is a declaration that creates a status, not a simple statement of fact), "I beg you as a suppliant" (turns a self-identification into a request) |
| ὀλιγηπελέων (5.457) / ἐξ ὀλιγηπελίης (5.468, "near-collapse" vocabulary, the same root twice in one part) | "faint with little strength" / "faintness" | "faint" (adj.) / "faintness" (noun) | "exhausted" (loses the literal "little strength" image), "weak" alone (too generic; kept as "faint" throughout so the reader can hear the repetition) |
| κεκαφηότα θυμόν (5.468) | "spent-breath spirit" | "exhausted, gasping spirit" (+ note: derivation of κεκαφηώς disputed — perhaps from a lost verb "breathe out, gasp"; not fully understood) | "grief-worn heart" (invents a sense not supported), "fainting heart" (blurs it with the separate, already-fixed ὀλιγηπελέων row just above) |
| ᾤδεε δὲ χρόα πάντα (5.455) | "swollen was all his flesh" | "his whole body was swollen" | "his flesh was bloated" (wrong register — this is drowning-swelling, not overeating), "puffed up" (too colloquial) |
| δαλὸν σποδιῇ ἐνέκρυψε μελαίνῃ … σπέρμα πυρὸς σώζων (5.488, 490, fire-and-embers simile) | "a brand in black ashes has hidden … saving a seed of fire" | "buries a live brand in black ashes … to keep a seed of fire alive" | "banked the coals" (a modern hearth-idiom, not a translation), "kept the fire going" (loses σπέρμα, literally "seed", the image of fire as a thing that germinates anew) |
| Κύκλωπες ἄνδρες ὑπερηνορέοντες (6.5, ὑπερηνορεόντων) | "the Cyclopes, men over-bold" | "the overbearing Cyclopes" | "overweening", "arrogant", "haughty"; "manly" and "lordly" (reserved for ἀγήνωρ). Built on ὑπέρ + ἠνορέη "manliness"; a reproach here, unlike ὑπέρθυμος |
| ἀνδρῶν ἀλφηστάων (6.8) | "of gain-winning men" | "of men who earn their living" (+ note: meaning uncertain; ἀλφάνω "find, earn", or ancient "grain-eating") | "bread-eating", "corn-eating" (silently pick the minority guess), "toiling", "mortal" |
| θεῶν ἄπο μήδεα εἰδώς (6.12) | "from the gods counsels knowing" | "who knew counsels from the gods" | "wise as the gods", "divinely wise", "wise in counsel" (drops θεῶν ἄπο); μήδεα keeps "counsels" as in πεπνυμένα μήδεα εἰδώς |
| θάλαμον πολυδαίδαλον (6.15) | "the much-wrought chamber" | "the richly wrought bedchamber" | "intricate", "cunningly made", "well-adorned" |
| ἀθανάτῃσι φυὴν καὶ εἶδος ὁμοίη (6.16) | "to the immortal ones in stature and form like" | "like the goddesses in stature and form" | "godlike" (reserved for ἀντίθεος), "beautiful as a goddess", "in body and looks" (φυή is "stature, growth") |
| Χαρίτων ἄπο κάλλος ἔχουσαι (6.18) | "from the Graces beauty having" | "who had their beauty from the Graces" | "graceful", "with the beauty of the Graces" |
| θύραι ἐπέκειντο φαειναί (6.19) | "the shining doors were set to" | "the shining doors were shut" | "gleaming" (reserved for γλαυκῶπις), "polished", "bright"; φαεινός keeps "shining" |
| ἀνέμου ὡς πνοιή (6.20) | "like a blowing of wind" | "like a breath of wind" | "gust", "puff", "blast" (reserved for ἄελλα / θύελλα) |
| τῇ μιν ἐεισαμένη προσέφη γλαυκῶπις Ἀθήνη (6.24, speech introduction) | "Having made herself like to her, addressed gleaming-eyed Athena:" | "Gleaming-eyed Athena, making herself like her, spoke to her:" | "in the guise of", "taking the form of" (loses εἴδομαι "make oneself like"), "answered" (nothing has been said to her) |
| σιγαλόεις (6.26, 6.38, 6.81: clothes, rugs, reins) | "glossy" | "glossy" | "shining" (reserved for φαεινός), "gleaming" (reserved for γλαυκῶπις), "sleek", "silent" (the ancient link with σιγή) |
| κλειτός (6.22 ναυσικλειτοῖο, 6.54 κλειτοὺς βασιλῆας) | "famous" (ship-famous) | "famous" (famous for his ships) | "renowned" (ἀγακλυτός), "glorious" (φαίδιμος); κλειτός is κλυτός in another spelling and keeps the table's "famous" |
| ἀπήνη / ἄμαξα (6.37, 6.57, 6.69, 6.72–73 and passim: one mule-wagon under two names) | "wagon" | "wagon" | "cart" (a second word would suggest a second vehicle), "carriage", "chariot" (ἅρμα / δίφρος) |
| ὑψηλὴν ἐύκυκλον (ἀπήνην) (6.58 = 6.70) | "high, well-wheeled" | "high, well-wheeled" | "tall", "fine-wheeled", "high-built" |
| ἄμαξα ἐύτροχος ἡμιονείη (6.72) | "a wagon, well-rolling, mule-drawn" | "the well-rolling, mule-drawn wagon" | "smooth-running", "swift", "well-wheeled" (kept for ἐύκυκλος) |
| ὑπερτερίη ἀραρυῖαν (6.70) | "fitted with an upper frame" | "with an upper frame fitted to it" (+ note: meaning of ὑπερτερίη uncertain; "upper frame" is a guess) | "with a cover", "roofed", "with a canopy" (each silently picks one guess) |
| πάππα φίλ’ (6.57) | "Dear papa" | "Dear papa" | "Dear father", "Daddy", "Father dear" |
| ἡ δὲ μάλ’ ἄγχι στᾶσα φίλον πατέρα προσέειπε (6.56, approach-and-address line) | "and she, very near standing, her dear father addressed:" | "She stood very close to her dear father and addressed him:" | "answered" (reserved for ἠμείβετο), "went up to" |
| ὣς εἰπὼν δμώεσσιν ἐκέκλετο, τοὶ δ’ ἐπίθοντο (6.71) | "So having spoken, to the servants he called out, and they obeyed." | "So he spoke, and gave orders to the servants, and they obeyed." | "commanded", "summoned"; "So he spoke" (kept for ὣς φάτο / ὣς ἔφατο; here it is ὣς εἰπών, "so having spoken") |
| δμῶες / δμῳαί (6.69, 6.99) | "servants" / "maidservants" | "servants" / "maids" | "slaves", "thralls", "handmaidens" |
| ἀμφίπολοι (γυναῖκες) (6.18, 6.52, 6.80, 6.84, 6.109) | "attendants" / "attendant women" (ἀμφιπόλοισι γυναιξίν) | "attendants" / "attendant women" | "handmaidens", "servants", "maids" (kept for δμῳαί) |
| ἐύθρονος Ἠώς (6.48) | "Dawn, fair-throned" | "fair-throned Dawn" | "golden-throned" (χρυσόθρονος), "rosy-fingered" (the separate ῥοδοδάκτυλος formula), "well-seated"; ἐύ- is "fair" as in ἐυστέφανος, καλλίσφυρος |
| ἐύπεπλος (of Nausicaa, 6.49) | "fair-robed" | "fair-robed" | "fair-gowned", "well-robed", "long-robed" (reserved for τανύπεπλος) |
| θαλερὸς γάμος (6.66) | "a blooming marriage" | "her blooming marriage" | "lusty", "fruitful", "youthful" |
| ἁλιπόρφυρα (6.53) | "sea-purple" | "sea-purple" | "sea-dyed", "purple as the sea", "crimson"; πορφύρεος elsewhere stays plain "purple" |
| μενοεικέ’ ἐδωδήν (6.76) | "satisfying food" | "satisfying food" | "food to the heart's content" (imports "heart"), "abundant food" |
| ἐύξεστος ἀπήνη (6.75) | "the well-polished wagon" | "the well-polished wagon" | "well-planed", "smooth"; follows the table's δίφρον ἐύξοον "a well-polished car" |
| ἄμοτον τανύοντο (6.83) | "unceasingly stretched themselves" | "strained on without pause" (+ note: sense of ἄμοτον not known; "unceasingly" is the traditional guess) | "eagerly", "furiously", "insatiably" (each silently picks one guess) |
| περικαλλής (6.85, ῥόον περικαλλέ’) | "very fair" | "very fair" | "exceedingly lovely", "all-fair", "most beautiful" |
| ἐπηετανοί (πλυνοί) (6.86) | "never-failing" | "never-failing" (+ note: sense only approximately known) | "plentiful", "ever-flowing", "year-round" (each picks a guess) |
| μέλαν ὕδωρ (6.91) | "dark water" | "dark water" | "black water", "murky water"; kept parallel to the table's μέλας οἶνος "dark wine" and μέλαν κῦμα "the dark wave" |
| ἔριδα προφέρουσαι (6.92) | "rivalry putting forward" | "each trying to outdo the other" | "quarrelling", "in a struggle" (ἔρις here is friendly rivalry), "racing" |
| λοεσσάμεναι καὶ χρισάμεναι λίπ’ ἐλαίῳ (6.96) | "having bathed and having anointed themselves richly with oil" | "bathed and anointed themselves richly with oil" | "rubbed with olive oil" (loses χρίω "anoint"), "sleekly", "generously" for λίπα |
| αὐτὰρ ἐπεὶ σίτου τάρφθεν δμῳαί τε καὶ αὐτή (6.99) | "But when they had had their fill of food, the maidservants and she herself," | "When the maids and she herself had had their fill of food," | "were satisfied with food", "had eaten" (lose τέρπω "delight, satisfy"); kept apart from the fixed ἐπεὶ πόσιος καὶ ἐδητύος ἐξ ἔρον ἕντο |
| λευκώλενος (6.101) | "white-armed" | "white-armed" | "fair-armed", "ivory-armed", "of the white arms" |
| ἤρχετο μολπῆς (6.101) | "led off the song-and-dance" | "led the song and dance" | "began the singing" alone (drops the dancing), "led the play" |
| ἰοχέαιρα (of Artemis, 6.102) | "arrow-pourer" | "who showers her arrows" (+ note: second element disputed, χέω "pour" or χαίρω "delight in") | "archer", "huntress", "arrow-shooter" (each hides the dispute); "delighting in arrows" (silently picks the other derivation) |
| περιμήκετον (of Taygetus, 6.103) | "very long" | "very long" | "exceedingly long", "towering", "lofty" (loses μῆκος "length") |
| ἀγρονόμοι (of the nymphs, 6.106) | "field-ranging" | "who range the countryside" | "rustic", "pastoral", "wild", "of the woods" |
| ἀριγνώτη (6.108) | "easily recognisable" | "easily known" | "conspicuous", "distinguished", "unmistakable" |
| παρθένος ἀδμής (6.109) | "the unwed maiden" | "the unwed maiden" | "untamed", "unbroken" (the literal root, kept in the note), "chaste" |
| ἐυῶπις (6.113, 6.142, κούρην ἐυώπιδα) | "fair-eyed" | "fair-eyed" | "bright-eyed", "beautiful-eyed", "well-eyed"; ἐύ- is "fair" as in ἐυστέφανος, and the word is kept apart from γλαυκῶπις "gleaming-eyed" |
| τὸν δ’ αὖ Ναυσικάα λευκώλενος ἀντίον ηὔδα (6.186, reply-formula: name + epithet + ἀντίον ηὔδα; the same shape as the fixed τὴν/τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα) | "To him in turn white-armed Nausicaa spoke, face to face:" | "Then white-armed Nausicaa spoke to him in turn, face to face:" | "answered" (reserved for ἠμείβετο), "addressed" (reserved for προσέειπε / προσέφη) |
| δή ῥα τότ’ ἀμφιπόλοισι μετηύδα δῖος Ὀδυσσεύς (whole-line speech introduction, 6.217) | "Then indeed among the attendants spoke heavenly Odysseus:" | "Then heavenly Odysseus spoke among the attendants:" | "answered" (reserved for ἠμείβετο), "addressed" (reserved for προσέειπε / προσέφη); μετηύδα keeps "spoke among", as fixed for τῇς δ’ ἁδινὸν γοόωσα μετηύδα Πηνελόπεια |
| ὀρεσίτροφος (of a lion, 6.130) | "mountain-nurtured" | "mountain-nurtured" | "mountain-bred" (loses τρέφω "nourish"; keep for a different compound), "reared on the mountains", "mountain-fed" |
| μήδεα φωτός (6.129, "the genitals of the man"; a distinct lemma from μήδεα "counsels" in πεπνυμένα μήδεα εἰδώς) | "the genitals of the man" | "his genitals" | "his nakedness", "his private parts" (bowdlerizing or euphemistic), "counsels" (that is the other word) |
| γουνοῦμαί σε, ἄνασσα (6.149, formal opening of a supplication) | "I beseech you at your knees, queen" | "I entreat you, queen" | "I clasp your knees" (Odysseus has decided not to touch them, 6.145–147; the note explains that the knee is only in the verb), "I implore you", "I kneel to you" |
| ἐέδνοισι βρίσας (6.159, "having outweighed with bridal gifts") | "having outweighed you with bridal gifts" | "outweighs his rivals with bridal gifts" | "loading you with gifts" (reverses who gives to whom), "buying you", "paying the bride-price" (the ἕεδνα are the suitor's gifts; the verb is βρίθω "be heavy") |
| δόρυ (6.167, of the palm's stem, ἐκ δόρυ γαίης) | "trunk" | "trunk" | "spear", "shaft" (both lose the tree), "timber" |
| δαίμων (6.172, ἐνθάδε κάββαλε δαίμων, an unnamed divine power) | "a power" | "some power" | "a god" (reserved for θεός), "spirit", "demon", "fortune", "fate" (reserved for μοῖρα / πότμος) |
| κακὰ κήδεα (6.165) | "evil sorrows" | "evil sorrows" | "evil cares", "grievous" (reserved for λυγρός / ἀργαλέος), "troubles" alone |
| διερὸς βροτός (6.201; meaning of διερός uncertain) | "a living mortal" | "no living mortal" (+ note: 'living' is the traditional guess; 'wet', 'lively' also proposed) | "an active mortal", "a quick mortal", "a wet mortal" (each silently picks one guess) |
| πολύκλυστος (of the sea, 6.204) | "much-washed" (of the open-sea) | "wave-washed" | "stormy", "surging", "tossing", "much-tossed" |
| πρὸς γὰρ Διός εἰσιν ἅπαντες / ξεῖνοί τε πτωχοί τε, δόσις δ’ ὀλίγη τε φίλη τε (two-line saying, 6.207–208) | "for from Zeus are all / strangers and beggars, and a gift is small and dear." | "for all strangers and beggars are from Zeus, and a small gift is welcome." | "under Zeus's protection" (turns πρός into an interpretation), "poor men" for πτωχοί (kept "beggars"), "a gift small but cherished" |
| ὣς ἔφαθ’, αἱ δ’ ἄρα τῆς μάλα μὲν κλύον ἠδ’ ἐπίθοντο (feminine speaker and hearers, 6.247; masc. line already fixed at 3.477) | "So she spoke, and they then readily heard her and obeyed," | "So she spoke, and they listened to her readily and obeyed," | "heeded", "hearkened", "did as she said"; ὣς ἔφαθ’ keeps the table's "So … spoke" |
| αὐτὰρ Ναυσικάα λευκώλενος ἄλλ’ ἐνόησεν (6.251) | "But white-armed Nausicaa devised another thing:" | "But white-armed Nausicaa thought of something else:" | "had another plan", "had a new idea"; built on the fixed αὐτὰρ Ἀθηναίη κούρη Διὸς ἄλλ’ ἐνόησεν |
| κρατερώνυχας (of mules, 6.253) | "strong-hoofed" | "strong-hoofed" | "strong-clawed", "stout-hoofed", "sturdy" |
| ἀμφιέλισσαι (of ships, 6.264) | "both-sides-curving" | "curved on both sides" (+ note: sense disputed, 'rowed on both sides' also guessed) | "curved at both ends" or "double-ended" (silently picks one guess), "rounded", "shapely" |
| ἐπίστιον (6.265) | "a slip" | "a slip of his own" (+ note: sense only approximately known) | "a home", "a hearth", "a berth" (each picks a guess) |
| Ποσιδήιον (neuter adj. as noun, 6.266) | "sanctuary of Poseidon" | "the sanctuary of Poseidon" | "temple" (no building is named), "shrine", "Poseidon's grove" |
| ὑπερφίαλος (6.274) | "overweening" | "overweening" | "arrogant", "insolent", "haughty"; kept apart from ὑπερηνορέοντες "overbearing" |
| ἱμάσθλη (6.320) | "lash" | "the lash" | "whip" (reserved for μάστιξ, 6.316), "goad", "scourge" |
| ἀεικέλιος (6.242) | "unseemly" | "unseemly" | "ugly", "shabby", "unsightly" (drop the sense of what is not fitting); follows ἀεικέα πότμον "an unseemly doom" |
| πολυάρητος (6.280) | "much-prayed-for" | "much prayed to" | "much-desired" (drops ἀρή "prayer"), "often invoked" |
| ἐπιζαφελῶς (6.330) | "furiously" | "furiously" | "unceasingly" (kept for the different word ἀσπερχές, 1.20), "greatly", "vehemently" |
| πατροκασίγνητος (6.330) | "father’s brother" | "her father’s brother" | "uncle" (loses the compound's plain sense), "Poseidon" (the Greek withholds the name) |
| στίλβων (6.237) | "glistening" | "glistening" | "gleaming" (reserved for γλαυκῶπις), "shining" (reserved for φαεινός), "sparkling" |
| μένος ἡμιόνοιιν (7.2, periphrasis for the pair of mules) | "the strength of the two mules" | "the strength of the two mules" | naturalising it to "the mules" (erases the periphrasis; same device as ἱερὴ ἲς Τηλεμάχοιο) |
| ἀθανάτοις ἐναλίγκιοι (7.5, of the brothers) | "like to the immortals" | "like the immortals" | "godlike" (reserved for ἀντίθεος); follows the shape of θεῷ ἐναλίγκιος ἄντην |
| θαλαμηπόλος (7.8) | "chamber-attendant" | "her chamber-attendant" | "housekeeper" (reserved for ταμίη), "handmaid", "bedchamber-servant" |
| γρῆυς Ἀπειραίη (7.8) | "an old woman of Apeire" | "an old woman from Apeire" (+ note: place not known) | "the Epirote", identifying Apeire with any known place |
| ξεῖνε πάτερ (7.28, 7.48, address to an older stranger) | "stranger, father" | "stranger, father" (+ note: respectful address, no kinship) | "father stranger", "good sir", "old sir" (reserved-out by the ὦ γέρον row), "dear stranger" (that is ξεῖνε φίλε) |
| ταλαπείριος (7.24; already shipped at 6.191) | "much-tried" | "much tried" | "wretched", "long-suffering" (reserved-out at πολύτλας), "enduring" |
| ἐραννός (7.18, πόλιν … ἐραννήν) | "delightful" | "delightful" | "lovely" (reserved for ἐρατεινός, shipped at 4.12 and used at 7.79), "charming", "fair" |
| ἐρατεινός (7.79, Σχερίην ἐρατεινήν) | "lovely" | "lovely" | "delightful" (reserved for ἐραννός), "desirable" |
| ἠήρ · ἀχλύς (7.15 ἠέρα; 7.41 ἀχλύν) | "mist" · "haze" | "a thick mist" · "a wondrous haze" | using one word for both; "darkness", "cloud" |
| δεινὴ θεός (7.41, of Athena) | "the dread goddess" | "the dread goddess" | "terrible", "awesome", "formidable"; follows "dread" as shipped for δεινή at 5.316 and δεινόν at 5.174 |
| φίλα φρονέουσ’ (7.15 alone; 7.42 with ἐνὶ θυμῷ) | "kindly thinking" (+ "in her heart") | "kindly disposed toward him" (+ "in her heart") | "with friendly thoughts", "well-meaning"; follows the shipped "thinks kindly toward you in her heart" (6.313) |
| Φαίηκες ναυσικλυτοί (7.39) | "the Phaeacians, ship-famous" | "the Phaeacians, famous for their ships" | "far-famed", "renowned" (reserved for ἀγακλυτός); κλυτός keeps "famous", as at 6.22 |
| ἐυπλόκαμος (7.41, of Athena) | "fine-plaited" | "fine-plaited" | "fair-haired" (reserved for ξανθός), "lovely-haired"; follows the table's ἐυπλόκαμος Ἠώς |
| ἡρώων ἀγοράς (7.44) | "the meeting-places of the heroes" | "the meeting-places of the heroes themselves" | "the market-places", "assemblies" (reserved for the assembly-vocabulary of Book 2) |
| σκολόπεσσιν ἀρηρότα (7.45, of walls) | "fitted with stakes" | "fitted with stakes" | "palisaded", "crowned with palisades" (each interprets the picture) |
| Ἀρήτη … ὄνομ’ ἐστὶν ἐπώνυμον (7.54) | "Arete is her name, name-bearing" | "Her name is Arete" | "her fitting name", "well-named" (both assert a meaning the Greek does not state) |
| ἀργυρότοξος Ἀπόλλων (7.64) | "silver-bowed Apollo" | "silver-bowed Apollo" | "of the silver bow", "the archer god", "silver-shafted" |
| ἄκουρος (7.64) | "having no son" | "who had no son" | "unmarried", "childless" (the next lines have him leave a daughter) |
| ἀτάσθαλος (7.60, adj.; cf. the table's ἀτάσθαλα) | "wanton" | "wanton" | "reckless", "outrageous" |
| ὑψόροφος (7.77, οἶκον ἐς ὑψόροφον; shipped at 5.42 and 5.115 as "high-roofed") | "high-roofed" | "high-roofed" | "high-ceilinged", "lofty"; the same English as ὑψερεφές (a different word, from ἐρέφω), by the shipped precedent |
| ἀτρύγετος (7.79, πόντον ἐπ’ ἀτρύγετον) | "over the unharvested open-sea" | "over the sea that yields no harvest" (+ note: meaning unknown) | "barren", "unresting"; the table's ἁλὸς ἀτρυγέτοιο with πόντος in place of ἅλς |
| εὐρυάγυια (of Athens, 7.80) | "wide-streeted" | "of the wide streets" | "broad-avenued", "spacious" (reserved for εὐρύχορος) |
| πυκινὸς δόμος (7.81, 7.88) | "the solid house" | "the solid house" | "close-built", "strong-built", "thick-walled" |
| ἐύδμητος (7.100, of pedestals) | "well-constructed" | "well-constructed" | "well-built" (reserved for ἐυκτίμενος), "well-framed" |
| βωμός (7.100) | "pedestal" | "pedestal" (+ note: usually 'altar') | "altar" (no sacrifice is in view) |
| κύανος (7.87) | "kyanos" | "kyanos" (+ note: material unknown) | "blue enamel", "lapis", "dark-blue glass" (each silently picks one guess) |
| κορώνη (7.90, of a door) | "handle" | "handle" (+ note: the word also means 'crow') | "knocker", "door-ring" |
| ἰδυῖα πραπίδες (7.92) | "knowing wits" | "his skilled wits" | "cunning hands", "craft-skilled mind" |
| μήλοψ καρπός (7.104) | "apple-coloured grain" | "the yellow grain" (+ note: meaning uncertain) | "golden", "tawny" (each silently picks one guess), "apple-faced" |
| καιρουσσέων ὀθονέων (7.107) | "close-woven cloths" | "the close-woven linen" (+ note: meaning uncertain, ancient explanation followed) | "glossy", "tightly-twisted"; flagged as uncertain |
| ἐπηετανός (7.99 as a noun, “a never-failing supply”, or an adverb; 7.128 adverbial; cf. the table's ἐπηετανοί, 6.86) | "never-failing" | "never-failing" / "never failing" | "plentiful", "unstinted", "all year round" (reserved for ἐπετήσιος) |
| ἐπετήσιος (7.118) | "year-long" | "lasting the whole year" | "yearly", "perennial" (drops ἔτος) |
| ὄρχατος (7.112) | "orchard" | "orchard" | "garden" (κῆπος, 7.129), "grove" (ἄλσος) |
| ἀλωή (7.122; 6.293 shipped it as "orchard") | "vineyard" | "vineyard" | "orchard": at 6.293 the same word is "orchard" as shipped, left as shipped; here the grapes, the pressing and the drying make it a vineyard, and the note says the word means a cultivated plot |
| τετράγυος (7.113) | "four-acre" | "four-acre" (+ note: size of γύης uncertain) | "four-plough-lands", "of four acres exactly" |
| τηλεθάων (7.114, 7.116) | "thriving" | "thriving" | "flourishing" (shipped for τεθαλυῖα at 6.293), "luxuriant", "blooming" |
| ἀγλαόκαρπος (7.115) | "with splendid fruit" | "with splendid fruit" / "bearing splendid fruit" | "bright-fruited", "fair-fruited" (ἀγλαός keeps "splendid") |
| ὄγχνη · ῥοιά · μηλέα · συκέα · ἐλαία (7.115–116) | "pear tree" · "pomegranate" · "apple tree" · "fig tree" · "olive" | same | "pear-tree", "quince" for μηλέα |
| γηράσκει (7.120, of fruit) | "grows old" | "grows old" | "ripens", "matures" (drops the age-image) |
| πολύκαρπος (7.122) | "many-fruited" | "richly fruited" | "fruitful", "abundant" |
| θειλόπεδον (7.123) | "sun-drying-ground" | "a warm drying-place" | "sun-terrace", "threshing-floor" |
| ὄμφακες (7.125) | "unripe grapes" | "unripe grapes" | "sour grapes", "green grapes" |
| ὑποπερκάζω (7.126) | "begin to darken" | "are just turning dark" | "ripen", "blush" |
| κοσμηταὶ πρασιαί (7.127) | "neatly-ordered beds" | "neatly ordered beds" | "trim borders", "well-arranged plots" |
| ἐπηετανὸν γανόωσαι (7.128) | "never-failing gleaming" | "gleaming fresh and never failing" | "shining all year", "bright" alone |
| ἐύσκοπος ἀργεϊφόντης (7.137, ἐυσκόπῳ ἀργεϊφόντῃ; shipped at 1.38, not yet in the table) | "keen-sighted Argeïphontes" | "the keen-sighted slayer of Argus" (+ note: meaning of ἀργεϊφόντης disputed) | "sharp-eyed", "far-seeing", "watchful" (ἐύσκοπος is σκοπός "watcher, one who looks out"); joins the table's ἀργεϊφόντης row |
| Φαιήκων ἡγήτορες ἠδὲ μέδοντες (7.136, 7.186) | "leaders and lords of the Phaeacians" | "the leaders and lords of the Phaeacians" | "rulers and counsellors", "chiefs and princes"; ἡγήτωρ keeps the shipped "leader" (Ταφίων ἡγήτωρ, 30.98), μέδων keeps the shipped "lord" (ἁλὸς ἀτρυγέτοιο μέδοντος, 1.72) |
| θέσφατος ἀήρ (7.143) | "the god-declared mist" | "the god-decreed mist" (+ note: sense of the compound of a mist uncertain) | "the marvellous mist", "the divine mist" (reserved for θεῖος), "the enchanted mist"; follows the table's θέσφατόν ἐστι "it is god-declared" / "it is decreed"; ἀήρ = ἠήρ "mist" |
| ἄνεῳ ἐγένοντο (7.144, of the company) | "they became speechless" | "they fell speechless" | "they fell silent" (keeps for ἀκὴν ἐγένοντο σιωπῇ, 7.154), "they were struck dumb" |
| ἀκὴν ἐγένοντο σιωπῇ (7.154) | "became still in silence" | "fell hushed and silent" | "were quite silent", "held their peace" |
| γέρων ἥρως Ἐχένηος (7.155) | "the old hero Echeneus" | "the old hero Echeneus" | "the aged warrior", "the old nobleman"; follows the shipped γέρων ἥρως Ἁλιθέρσης (2.157) and the table's ἥρως "the hero" |
| ἀργυρόηλος θρόνος (7.162, ἐπὶ θρόνου ἀργυροήλου) | "a silver-studded chair" | "a silver-studded chair" | "silver-nailed", "chair with silver nails", "throne" (θρόνος is "chair" as shipped at 2.144, 3.388) |
| Διὶ τερπικεραύνῳ (7.164, 7.180) | "bolt-delighting Zeus" | "Zeus, who delights in the thunderbolt" | "lord of thunder", "thunder-loving", "the thunderer" (drops τέρπω); from τέρπω "delight" + κεραυνός "thunderbolt" |
| ὅς θ’ ἱκέτῃσιν ἅμ’ αἰδοίοισιν ὀπηδεῖ (7.165 = 7.181, whole line) | "who keeps company with revered suppliants" | "who keeps company with revered suppliants" | "who watches over suppliants", "protector of suppliants" (states the doctrine the verb leaves implicit), "who attends respected suppliants" |
| ἱερὸν μένος Ἀλκινόοιο (7.167; 7.178 μένος Ἀλκινόοιο) | "the sacred strength of Alcinous" / "the strength of Alcinous" | same | "mighty Alcinous", "the sacred might of Alcinous", "the great Alcinous" (naturalising erases the periphrasis); μένος keeps the table's "strength" (μένος ἡμιόνοιιν) and ἱερόν the table's "sacred" (ἱερὴ ἲς Τηλεμάχοιο); "the strong, sacred figure" is reserved for ἲς |
| ποικιλομήτης (7.168, of Odysseus; shipped in odyssey-010, unit at line 162) | "of many-colored cunning" | "full of shifting cunning" | "of many wiles" (reserved for πολύμητις), "of many devices" (reserved for πολυμήχανος), "crafty", "wily"; joins the table's δαΐφρων row |
| ἀγαπήνωρ (7.170, of Laodamas) | "man-cherishing" | "who prized manliness" (+ note: exact sense unknown) | "manly", "beloved by men", "loving his people", "high-hearted"; ἀγαπάω + ἀνήρ kept in `l` |
| μελίφρων οἶνος (7.182, μελίφρονα οἶνον) | "honey-hearted wine" | "heart-sweetening wine" (+ note: sense uncertain) | "honey-sweet" (reserved for μελιηδής), "mellow", "honeyed", "honey-minded" (“-minded” is reserved for the -φρων epithets of persons) |
| ἀγακλειτὸς ἑκατόμβη (7.202, ἀγακλειτὰς ἑκατόμβας) | "renowned hecatombs" | "renowned hecatombs" | "glorious" (reserved for φαίδιμος), "famous" (reserved for κλυτός), "splendid"; ἀγακλειτός is ἀγακλυτός in another spelling (as κλειτός is κλυτός), so it takes the table's ἀγακλυτός row "renowned"; the shipped 3.59 "glorious hecatomb" (odyssey-009 line 57) is left as shipped, a discrepancy with that row of the same kind as the 3.153 note |
| θεοὶ … φαίνονται ἐναργεῖς (7.201) | "the gods appear manifest" | "the gods appear in manifest form" | "clearly", "openly", "in plain view"; ἐναργής is shipped "manifest form" (odyssey-013 line 418) |
| ἄγρια φῦλα Γιγάντων (7.206) | "the savage tribes of the Giants" | "the savage tribes of the Giants" | "wild", "fierce", "the wild races of the Giants"; ἄγριος keeps the table's "savage" |
| τὸν δ’ ἀπαμειβόμενος προσέφη πολύμητις Ὀδυσσεύς (7.207, whole-line reply-formula, masculine object) | "Him answering addressed many-wiled Odysseus:" | "In answer Odysseus of many wiles said to him:" | "answered" (reserved for ἠμείβετο), "resourceful"; the masculine of the shipped 5.214 line |
| κύντερον (7.216, στυγερῇ ἐπὶ γαστέρι κύντερον ἄλλο) | "more dog-like" | "more shameless" | "more brazen", "more wretched", "more importunate" (each drops the dog or picks the sense in `l`); κύων + comparative -τερον |
| κλῶθες (7.197) | "the Spinners" | "the Spinners" | "the Fates" (imports Moirai, and a later tradition), "the spinners" lower-case (loses the personification); κλώθω "spin" |
| πὰρ δέ οἱ … ἥσθην (7.231–232, dual) | "beside him … sat" | "beside him sat Arete and Alcinous" | naming the dual in English ("the two sat"), which would misplace the emphasis |
| τίς πόθεν εἰς ἀνδρῶν; | "Who among men are you, and from where?" | "Who among men are you, and where from?" | (already shipped in odyssey-002, unit at line 170; listed so the wording is table-fixed) "who are you and where do you come from?" |
| τὸν δ’ αὖτ’ Ἀλκίνοος ἀπαμείβετο φώνησέν τε (reply-formula, 7.298 = 7.308; name, no patronymic) | "Him then in turn answered Alcinous, and spoke:" | "Then Alcinous answered him in turn, and spoke:" | "addressed" (reserved for προσέειπε / προσέφη); "replied"; ἀπαμείβετο is the same verb as ἠμείβετο with ἀπό-, so "answered" is kept, and φώνησεν "spoke" carries the second verb |
| ὣς φάν (7.343, 3 pl. of φημί, unaugmented) | "So they spoke" | "So they spoke" | "So they said", "Thus they spoke"; plural counterpart of the table's ὣς φάτο |
| δολόεσσα Καλυψώ (7.245) | "guileful Calypso" | "guileful Calypso" | "crafty", "cunning", "wily"; δόλος is "trick", and "guileful" keeps the table's δολόμητις / δολίης τέχνης wording |
| Οὐρανίωνες (7.242, of the gods) | "the gods, the children-of-Heaven" | "the gods, the children of Heaven" (+ note: "descendants of Uranus" or "dwellers in heaven") | "the heavenly gods" (reserved for δῖος), "sons of Uranus" (silently picks one reading) |
| ἐφέστιος (7.248, ἐφέστιον ἤγαγε) | "to her hearth" | "to her hearth" | "as a suppliant", "to her home" |
| ἁλί (7.244, εἰν ἁλί; ἅλα 7.328) | "in the salt-sea" / "the salt-sea" | "in the sea" / "the salt sea" | "the brine"; keeps ἅλς distinct from πόντος "open-sea" and πολιὴ ἅλς "the grey sea" |
| νὺξ μέλαινα (7.253, νυκτὶ μελαίνῃ) | "black night" | "dark night" | "black night" in `i` (`i` keeps "dark" as for μέλας οἶνος, μέλαν κῦμα); "starless" |
| θυμηγερέων (7.283) | "spirit-gathering" | "gathering my spirits" | "catching my breath" (narrows the sense), "regaining courage" |
| διιπετής (of a river, 7.284) | "the Zeus-fallen river" | "the river fallen from Zeus" (+ note: meaning not certain, "fed by rain" is the ancient gloss) | "rain-fed", "heaven-fed" (silently pick the gloss) |
| ἀπείρων (7.286, ὕπνον … ἀπείρονα) | "boundless" | "boundless" | "endless", "deep", "immense" (reserved for ἀθέσφατος) |
| ἀθέσφατος (7.273, θάλασσαν ἀθέσφατον) | "immense" | "immense" | "boundless" (reserved for ἀπείρων), "vast", "measureless" |
| τετιημένος ἦτορ (7.287) | "grieved in my dear heart" | "grieving in my heart" | "sad", "downcast"; the accusative of respect keeps φίλον ἦτορ "dear heart" in `l`, dropped in `i`, as in the shipped renderings of φίλον ἦτορ |
| ἀμφιπόλους … παιζούσας (7.290–291) | "attendants … playing" | "attendants … playing" | "handmaidens" (see table: ἀμφίπολοι "attendants") |
| ἱκετεύω (7.292, τὴν ἱκέτευσ’) | "I supplicated" | "I made my plea to her as a suppliant" | "I begged", "I implored" |
| δύσζηλος (7.307, δύσζηλοι … φῦλ’ ἀνθρώπων) | "jealous" | "jealous" (+ note: quick to suspect and resent) | "envious" (a different word in English), "touchy", "suspicious" |
| φίλον κῆρ (7.309; κῆρ 'heart', distinct from ἦτορ and θυμός) | "dear heart" | "the heart in my breast" | "spirit" (reserved for θυμὸς ἀγήνωρ), "soul" |
| αἴσιμα · ἐναίσιμον (7.310 · 7.299) | "in due measure" · "of what is fitting" | "in due measure" · "what is fitting" | "right", "proper"; both are from αἶσα "portion" and the English keeps the family |
| πομπὴ (7.317) | "escort" | "escort" | "conveyance", "passage", "sending" |
| τεκμαίρομαι (7.317) | "I fix" | "I fix" | "I appoint", "I decree" (too formal) |
| γαλήνη (7.319) | "the calm" | "the calm water" | "the sea", "the waves" |
| πατρίδα σὴν καὶ δῶμα (7.320) | "your fatherland and house" | "your fatherland and house" | "your homeland", "your home" |
| ὄρσο κέων, ὦ ξεῖνε (7.342) | "Arise, to lie down, stranger" | "Up, stranger, and go to bed" | "Rise and lie down", "Get up to sleep" |
| ἀσπαστὸν ἐείσατο κοιμηθῆναι (7.343) | "welcome it seemed to sleep" | "it seemed welcome to go to sleep" | "was glad to sleep", "gladly" |
| κέκλετο (7.335, κέκλετο δ’ Ἀρήτη … ἀμφιπόλοισιν) | "ordered" / "gave orders to" | "gave orders to" | "called to", "summoned" |
| ἐγκονέουσαι (7.340) | "bustling about" | "working with speed" | "hurrying", "diligently" |
| πυκινὸν λέχος (7.340) | "the solid bed" | "the solid bed" | "well-made", "firm", "close-packed"; follows the table's πυκινὸς δόμος "the solid house" |
| εὐνή (7.342, 7.347) beside λέχος / δέμνια | "couch" | "couch" | "bed" (kept for λέχος), "bedding" |
| γυνὴ δέσποινα (7.347) | "the woman, the lady" | "his wife, the lady of the house" | "queen" (reserved for ἄνασσα / βασίλεια), "mistress" |
| ἄναξ ἀνδρῶν Ἀγαμέμνων (8.77) | "the lord of men, Agamemnon" | "Agamemnon, lord of men" | "king of men" (the table keeps "lord" for ἄναξ and "chief of men" for ὄρχαμος ἀνδρῶν) |
| κλέα ἀνδρῶν (8.73, the heroic songs) | "the glories of men" | "the glories of men" | "the famous deeds of men" (adds "deeds"), "the fames of men" |
| ἀργιόδοντας ὕας (8.60) | "white-toothed pigs" | "white-toothed pigs" | "white-tusked", "gleaming-toothed" (reserved for γλαυκῶπις-type words) |
| φόρμιγξ λίγεια (8.67) | "the clear-sounding lyre" | "the clear-sounding lyre" | "clear-voiced" and "clear-toned" (the table keeps "clear-voiced" for λιγύφθογγοι, and turns "clear-toned" down there) |
| σκηπτοῦχος βασιλεύς (8.41, 8.47; shipped in odyssey-007 as "sceptred king") | "sceptre-bearing kings" / "the sceptre-bearers" | "the sceptred kings" / "the sceptre-bearers" | "staff-holding", "sceptre-holders" |
| πρωτόπλοος (of a ship, 8.35) | "first-voyaging" | "one on her first voyage" | "new", "maiden" |
| ἐρίηρος ἀοιδός (8.62; shipped "trusty minstrel" at 1.346) | "the trusty minstrel" | "the trusty minstrel" | "faithful", "beloved" |
| βάν ῥ’ ἴμεν (8.56, plural of the table's βῆ ῥ’ ἴμεν) | "they set out to go" | "they set out for …" | "strode", "made their way" |
| ὅτε with optative ἄρχοιτο / λήξειεν (8.87–92, iterative clauses) | "whenever …" with "would" on the -σκε verbs (ἕλεσκε, σπείσασκε, γοάασκεν) | same | a past-simple rendering that loses the repetition |
| δεινός (of Odysseus, 8.22) | "dread" | "dread" | "awesome", "awe-inspiring", "formidable"; follows the table's "the dread goddess" |
| Δαναοί (8.82) | "Danaans" | "Greeks" | "Argives"; the two layers follow what is shipped in odyssey-020 and odyssey-021 |
| ἠοῖοι · ἑσπέριοι ἄνθρωποι (8.29) | "men of the dawn" · "men of the evening" | "men of the dawn" · "men of the evening" | "easterners", "westerners" |
| δαιτὸς ἐίσης (8.98) | "the equal feast" | "the equally shared feast" | "the fair feast", "the plentiful feast", "the well-balanced feast" (reserved for νηῦς ἐίση, whose sense is separately flagged as uncertain); ἐίσης of a feast is the adjective 'equal', each guest having an equal share |
| ἄεθλον / ἆθλον, ἀέθλια, ἄθλων, ἄεθλοι, ἀέθλους (8.100 and passim) | "contest(s)" | "contest(s)" | "game(s)", "prize(s)" (ἀέθλιον can mean the prize; here it is the contest), "trial(s)" (kept for the toils of Odysseus, as shipped in odyssey-001, odyssey-011, odyssey-015 and odyssey-016); the several spellings are one word; odyssey-033 (8.21) already ships "contests"; odyssey-020 (4.659) ships "games" for ἀέθλων, an older divergence not touched here |
| ἀθλητήρ (8.164) | "athlete" | "athlete" | "contestant", "sportsman", "wrestler" |
| βροτολοιγὸς Ἄρης (8.115, βροτολοιγῷ … Ἄρηϊ) | "mortal-ruining Ares" | "Ares, the ruin of mortals" | "man-slaying", "bane of men", "plague of mortals" (βροτός "mortal" and λοιγός "ruin" are both kept) |
| ἀγαθὸς πάϊς Ἀλκινόοιο (8.130, 8.143) | "the good son of Alcinous" | "the good son of Alcinous" | "brave", "noble", "worthy son"; ἀγαθός is "good" |
| τοῖς ἄρα Λαοδάμας μετέφη πάϊς Ἀλκινόοιο (8.132, whole-line speech introduction) | "among them then spoke Laodamas, Alcinous’ son:" | "Laodamas, son of Alcinous, spoke among them:" | "addressed" (reserved for προσέειπε / προσέφη), "answered" (reserved for ἠμείβετο); built on the fixed τοῖσιν δ’ Ἀντίνοος μετέφη Εὐπείθεος υἱός |
| τὸν δ’ αὖτ’ Εὐρύαλος ἀπαμείβετο νείκεσέ τ’ ἄντην (8.158, reply-formula with a second verb) | "Him then in turn answered Euryalus, and reviled him to his face:" | "Then Euryalus answered him in turn, and reviled him to his face:" | "taunted", "rebuked", "insulted" (νεικέω is "quarrel with, revile"), "openly" for ἄντην; built on the fixed τὸν δ’ αὖτ’ Ἀλκίνοος ἀπαμείβετο φώνησέν τε with νείκεσέ τ’ ἄντην in place of φώνησέν τε |
| τὸν δ’ ἄρ’ ὑπόδρα ἰδὼν προσέφη πολύμητις Ὀδυσσεύς (8.165, whole-line reply-formula) | "Him then with a scowl looking addressed many-wiled Odysseus:" | "Then Odysseus of many wiles, looking at him with a scowl, spoke to him:" | "glaring", "glowering", "looking darkly", "answered" (reserved for ἠμείβετο); the ancient explanation of ὑπόδρα is "from under the brows", and the derivation is not certain, so the note says so |
| ναυσίκλυτοι ἄνδρες (8.191, of the Phaeacians; with δολιχήρετμοι, which keeps the table's "long-oared") | "ship-famous men" | "men famous for their ships" | "famed sailors", "renowned shipmen", "glorious seafarers" (each drops ναῦς or κλυτός) |
| πολυκλήιδι νηί (8.161, ναῦς with many κληΐδες) | "a many-thwarted ship" | "a ship of many thwarts" | "many-benched" (too close to ἐύσσελμος "well-benched"), "many-oared", "with many benches"; κληΐς is "thwart, rowing-bench" |
| ἥβη (8.136, 8.181) | "youth" | "youthful vigour" / "youth" | "prime", "manhood" |
| Phaeacian youths named at 8.111–119 and their father | Acroneus, Ocyalus, Elatreus, Nauteus, Prymneus, Anchialus, Eretmeus, Ponteus, Proreus, Thoon, Anabesineus, Amphialus, Polyneus, Tecton, Euryalus, Naubolus, Laodamas, Halius, Clytoneus | same | "Acroneos", "Okyalos" and other transliterated endings; the familiar Latinised forms are used, as for the other names in the table; the sea-words that make up most of the names are explained once in the note at 8.111 |
| ἀγών (8.200, 8.238, 8.259, 8.260; ἐν ἀγῶνι, κατ’ ἀγῶνας, καλὸν … ἀγῶνα) | "the gathering" / "gathering-place" | "the gathering" / "the gathering-place" | "contest" (reserved for ἄεθλον), "games", "arena", "assembly" (reserved for the assembly-vocabulary of Book 2) |
| ἀρετή (8.237, 8.239, 8.244, of a man's or a people's prowess) | "excellence" | "excellence" | "virtue" (moral), "valour", "prowess", "merit" |
| φόρμιγξ γλαφυρή (8.257); φόρμιγξ λίγεια is already fixed | "the hollow lyre" | "the hollow lyre" | "curved lyre", "the polished lyre"; γλαφυρός keeps the "hollow" of ἐν σπέσσι γλαφυροῖσι |
| κίθαρις (8.248) | "the lyre" | "the lyre" (+ note: not claimed to differ from φόρμιγξ) | "harp", "cithara" (a transliteration) |
| δῆμος (8.211, 8.220; δήμῳ ἐν ἀλλοδαπῷ, δήμῳ ἔνι Τρώων) | "land" | "land" | "people" (that is λαός), "district", "community" |
| κραδίη θυμός τε (8.204) | "heart and spirit" | "heart and spirit" | "heart and heart"; θυμός is "heart" elsewhere, but is "spirit" here so that the two words that stand together are kept apart (compare the θυμὸς ἀγήνωρ row) |
| κραιπνῶς (8.247, adverb; the epithet κραιπνὸς Βορέης is already fixed) | "at a rush" | "at a rush" | "swiftly" (reserved for θοός and ὠκύς), "rapidly", "fleetly" |
| χρυσήνιος Ἄρης (8.285) | "golden-reined Ares" | "golden-reined Ares" | "gold-bridled", "golden-bridled", "of the golden harness" |
| κλυτοτέχνης (of Hephaestus, 8.286) | "famous in craft" | "famous in craft" | "renowned craftsman" (κλυτός keeps "famous"), "skilled", "cunning" |
| περικλυτός (of Hephaestus, 8.287) | "very-famous" | "very famous" | "far-famed" (reserved for τηλεκλυτός), "renowned" (reserved for ἀγακλυτός), "illustrious" |
| ἐρισθενής (of the son of Cronus, 8.289) | "of great strength" | "great in strength" | "mighty" (reserved for ἴφθιμος), "strong", "all-powerful" |
| ἀλαοσκοπιή (8.285) | "a blind man's watch" | "a blind man's watch" | "a careless watch" (states the meaning instead of the picture), "blind watch" |
| βητάρμονες (8.250) | "dancers" | "dancers" | "the nimblest", "measure-treaders" |
| αἰσυμνῆται (8.258) | "stewards" | "stewards" (+ note: 'presiding officers'; formation obscure) | "umpires", "judges", "magistrates" |
| Κυθέρεια (8.288) | "Cytherea" | "Cytherea" (+ note: name from the island of Cythera) | "the Cytherean", "Aphrodite" (the Greek gives the other name) |
| ἐνηής (of a companion, 8.200) | "kindly" | "kindly" | "gentle", "friendly", "good" |

χειρί τέ μιν κατέρεξεν ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν (4.610, fixed with a male subject) now also covers a female
subject (Calypso, 5.181): the English pronoun tracks the speaker's sex ("stroked him with her hand"), exactly as
the ὣς φάτο row already does.

ἅλα δῖαν (5.261, μοχλοῖσιν δ’ ἄρα τήν γε κατείρυσεν εἰς ἅλα δῖαν): from odyssey-024 on, δῖος applied to the sea
keeps "heavenly" in *both* `l` and `i`, per row 274 above. This is not a retroactive fix: 3.153 keeps its shipped
"heavenly brine" / "bright salt sea", and 4.577 keeps its shipped "bright sea" in `i` — both left as shipped, the
inconsistency already noted at row 274.

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

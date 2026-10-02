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
| ἀμφιγυήεις / περικλυτὸς ἀμφιγυήεις (Hephaestus, 8.300, 349, 357; meaning of ἀμφιγυήεις unknown) | "the both-limbed one" / "the very-famous both-limbed one" | "the both-limbed god" / "the very famous both-limbed god" (+ note: unknown; 'lame in both legs' or 'strong in both arms' guessed) | "lame", "the lame god", "crook-footed" (silently pick one guess); περικλυτός keeps the table's "very-famous" |
| τὸν δ’ αὖτε προσέειπε περικλυτὸς ἀμφιγυήεις / τὸν δ’ ἠμείβετ’ ἔπειτα περικλυτὸς ἀμφιγυήεις (8.349, 8.357) | "Him then in turn addressed the very-famous both-limbed one:" / "Him then answered the very-famous both-limbed one:" | "Then the very famous both-limbed god spoke to him in turn:" / "Then the very famous both-limbed god answered him:" | "answered" for προσέειπε; built on the table's two reply-formulas |
| τὸν δ’ ἠμείβετ’ ἔπειτα διάκτορος ἀργεϊφόντης (8.338) | "Him then answered the guide, Argeïphontes:" | "Then the guide, the slayer of Argus, answered him:" | "answered ... the giant-killer" (both epithets are already fixed in the table) |
| τὸν δ’ αὖτε προσέειπε Ποσειδάων ἐνοσίχθων (8.354) | "Him then in turn addressed Poseidon earth-shaker:" | "Then Poseidon earth-shaker spoke to him in turn:" | "the earth-shaking Poseidon", "answered" |
| Ἑρμῆν δὲ προσέειπεν ἄναξ Διὸς υἱὸς Ἀπόλλων (8.334) | "And Hermes was addressed by the lord, the son of Zeus, Apollo:" | "And lord Apollo, the son of Zeus, spoke to Hermes:" | "answered"; the l keeps the Greek object-first order by using the passive |
| ἑκάεργος (of Apollo, 8.323; disputed: 'far-working' or 'far-shooting') | "far-working" | "who works from afar" (+ note: meaning disputed) | "far-shooter", "the archer" (silently pick one guess; kept apart from ἑκατηβόλος) |
| ἑκατηβόλος (of Apollo, 8.339) | "far-shooting" | "who shoots from afar" | "far-working" (reserved for ἑκάεργος), "archer" |
| ἐριούνης (of Hermes, 8.322; meaning unknown) | "the helper" | "the helper" (+ note: unknown; 'helper' or 'luck-bringer' is the ancient guess) | "the luck-bringer", "the runner" (each silently picks one guess) |
| δωτῆρες ἑάων / δῶτορ ἑάων (8.325, 8.335) | "givers of good things" / "giver of good things" | same | "givers of blessings", "bounteous", "givers of all good" |
| φιλομμειδὴς Ἀφροδίτη (8.362) | "smile-loving Aphrodite" | "smile-loving Aphrodite" | "laughter-loving", "sweet-smiling", "of the sweet smile" (φιλο- + μειδάω 'smile') |
| χρυσέη Ἀφροδίτη (8.337, 8.342) | "golden Aphrodite" | "golden Aphrodite" | "gilded", "shining" (reserved for φαεινός) |
| κλυτοεργός (of Hephaestus, 8.345) | "famous in works" | "famous for his works" | "renowned craftsman", "of famous craft" (kept apart from κλυτοτέχνης "famous in craft") |
| ἀίδηλος (of Ares, 8.309; formation uncertain) | "destroying" | "destructive" (+ note: uncertain; 'making unseen' is the guessed origin) | "unseen", "baleful", "hateful" (each silently picks a different guess) |
| ἀρτίπος (8.310) | "sound-of-foot" | "sound of foot" | "fleet-footed", "sure-footed", "well-footed" |
| ἠπεδανός (8.311) | "infirm" | "infirm" | "feeble" (already used for λευγαλέος of persons), "crippled", "weakly" |
| ἀγριόφωνοι (of the Sintians, 8.294) | "savage-voiced" | "of savage speech" | "wild-voiced", "rough-tongued", "barbarous" |
| χαλκοβατὲς δῶ (8.321; floor or threshold, disputed) | "the bronze-floored house" | "the house with the bronze floor" (+ note: 'floor' or 'threshold' disputed) | "bronze-threshold", "the bronze-founded house" (silently picks one) |
| πουλυβότειρα (of the earth, 8.378) | "much-nourishing" | "that feeds so many" | "all-nourishing", "fertile", "giver of many" |
| ἀριδείκετος (8.382) | "most conspicuous" | "most distinguished" | "most glorious" (reserved for φαίδιμος), "renowned" (reserved for ἀγακλυτός), "far-famed" |
| κρείων (voc. κρεῖον, of Alcinous, 8.382) | "lord" | "my lord" | "king" (reserved for βασιλεύς), "ruler"; κρείων keeps the "lord" shipped for κρείων Ἐτεωνεύς (4.22) and the table's "lord" for ἄναξ — the two words are told apart by context, not by rendering |
| μοιχάγρια (8.332) | "the adultery-fine" | "the adulterer's fine" | "the penalty", "compensation" (drop the μοιχός element) |
| ἄσβεστος γέλως (8.326) | "unquenchable laughter" | "laughter that would never go out" | "uncontrollable laughter", "endless laughter" (lose the fire-image); i follows the table's ἄσβεστον κλέος "fame that would never go out" |
| ἐρίηρος ἑταῖροι (9.100, ἐρίηρας ἑταίρους) | "trusty companions" | "trusty companions" | "faithful", "dear" (kept for φίλος), "sturdy"; follows the shipped "trusty minstrel" (ἐρίηρος ἀοιδός); note says the sense of ἐρίηρος is not fully known |
| ἱερὸν ἦμαρ (9.56) | "the sacred day" | "the sacred day" | "holy day", "the day's strength", "bright day"; ἱερός keeps the table's "sacred" |
| λαῖλαψ (9.68, λαίλαπι θεσπεσίῃ) | "squall" (with θεσπέσιος "wondrous") | "squall" | "hurricane", "tempest", "gale" (ἄελλα, θύελλα, above); keeps "wondrous" as fixed for θεσπέσιος |
| ἄνθινον εἶδαρ (9.84) | "flowery food" | "a flowery food" | "blossom-food", "food of flowers"; εἶδαρ is a rare word for "food" |
| Λωτοφάγοι / λωτός (9.84, 9.91–102) | "the Lotus-eaters" / "lotus" | same | "Lotos-eaters", "Lotophagi" (transliteration); note says which plant λωτός names is not known |
| θάνατόν τε μόρον τε (9.61) | "both death and doom" | "death and doom" | "death and fate" (μοῖρα/πότμος words), "death and portion" (μόρος alone keeps "portion" in ὑπὲρ μόρον); note glosses μόρος as the allotted portion |
| ὀλοοὶ ἄνεμοι (9.82) | "deadly winds" | "deadly winds" | "baneful winds" ("baneful" is kept for ὀλοφώια; the table's μοῖρ’ ὀλοή is "the deadly fate"), "destructive winds", "cruel winds" |
| αἰνόμοροι (9.53, αἰνομόροισιν) | "dread-fated" | "so grimly fated" | "ill-fated" (reserved for δύσμορος / κάμμορος), "doomed" |
| ἀκαχήμενοι ἦτορ (9.62) | "grieved in heart" | "grieved at heart" | "sad at heart", "heavy-hearted"; follows the shipped τετιημένος ἦτορ "grieving in my heart" |
| ἄσμενος (9.63) | "glad" | "glad" | "delighted", "relieved", "welcome" (reserved for ἀσπαστός) |
| εἰνοσίφυλλος (9.22) | "leaf-shaking" | "leaf-shaking" | "quivering with leaves", "rustling", "covered with leaves"; built on ἔνοσις "shaking" + φύλλον |
| τρηχύς (9.27, τρηχεῖ’, of Ithaca) | "rough" | "rough" | "rugged", "rocky" (reserved for κραναή), "craggy" |
| κουροτρόφος (9.27) | "nurse-of-youths" | "nurse of young men" | "nurse of heroes", "rearer of boys" |
| διερῷ ποδί (9.43; meaning of διερός uncertain) | "on a nimble foot" | "on nimble feet" (+ note: 'living, lively' or 'wet' are the guesses) | "on a swift foot" (θοός/ὠκύς keep "swift"), "at a run" (silently picks one guess) |
| ἠέριος (9.52; meaning uncertain) | "early" | "early in the morning" (+ note: 'early' from ἠώς/ἦρι, or 'misty' from ἠήρ) | "in the mist", "at dawn" (each silently picks one guess) |
| ἐπικάρσιος (9.70; meaning uncertain) | "aslant" | "aslant" (+ note: uncertain; 'head first' from κάρ- is the guess) | "headlong", "slantwise", "prow-first" (each silently picks one guess) |
| βουλυτόνδε (9.58) | "toward the ox-unyoking time" | "toward the time for unyoking oxen" | "toward evening", "at nightfall" (drop the oxen) |
| ζυγά (of a ship, 9.99) vs κληῖσι (9.103, ἐπὶ κληῖσι καθῖζον) | "the benches" vs "the rowing-benches" | "the benches" vs "the oarlocks" | one word for both; "yokes" for ζυγά; "thwarts" for κληῖσι here (the formula is shipped at 8.418 and 19.576 as "upon the rowing-benches" / "sat down at the oarlocks"; "thwart" stays in πολυκλήιδι "many-thwarted") |
| ξεῖνος (of the bond between host and guest, 9.18) | "guest-friend" | "guest-friend" | "stranger" (kept for ξεῖνε in address), "guest", "friend"; agrees with the table's πατρώιος ξεῖνος "guest-friend from my fathers' time" |
| ἔνθεν δὲ προτέρω πλέομεν ἀκαχήμενοι ἦτορ. (10.77, whole line ending at a full stop; 9.62 and 10.133 carry on with a second line) | "From there farther we sailed, grieved in heart;" | "From there we sailed on, grieved at heart." | follows the shipped 9.62 wording for the line; only the punctuation differs |
| Λαιστρυγόνες · Λαιστρυγών · Λαιστρυγονίη (10.82, 106, 119) | "the Laestrygonians" · "a Laestrygonian" · "Laestrygonian" | same | "Lestrygonians", "Laestrygones"; the familiar Latinised form, as for the other names |
| Λάμου αἰπὺ πτολίεθρον · Τηλέπυλον Λαιστρυγονίην (10.81–82) | "Lamus’ steep citadel" · "Laestrygonian Telepylus" | "the steep citadel of Lamus" · "Laestrygonian Telepylus" | "sheer", "lofty" for αἰπύς (reserved for the table’s "steep"); Telepylus kept as a name, its sense (perhaps "far-gate") being uncertain |
| ἄργυφα μῆλα (10.85) | "silver-white flocks" | "the silver-white flocks" | "white sheep" (drops ἄργυ-, and ὄις is "sheep"), "gleaming", "shining" |
| ἀκταὶ προβλῆτες (10.89) | "headlands, thrust forward" | "headlands thrust forward" | "jutting shores", "promontories" (Latinate) |
| ἀραιὴ εἴσοδος (10.90) | "narrow is the entrance" | "the entrance is narrow" | "thin", "slight" |
| ἔνθα κ’ ἄυπνος ἀνὴρ δοιοὺς ἐξήρατο μισθούς (10.84) | "a sleepless man two wages might have earned" | "a sleepless man could have earned two wages" | "a man who needed no sleep" (explains the Greek), "double pay" |
| λευκὴ γαλήνη (10.94) | "white … a calm" | "a white calm" | "bright calm", "a glassy calm" (note says λευκή is also "bright") |
| σκοπιὴ παιπαλόεσσα (10.97 = 10.148) | "a rugged lookout" | "a rugged lookout" | "rocky", "craggy" (reserved for κραναή), "windy"; follows the shipped "rugged" of παιπαλόεσσα (Same, Chios) |
| ναύλοχος λιμήν (10.141; 4.846) | "a harbour fit for ships" | "a harbour where ships can lie" | follows the shipped 4.846 (odyssey-021) |
| ἀνδραχθέσι χερμαδίοισιν (10.121) | "man-burdening stones" | "stones as heavy as a man could carry" | "huge stones", "boulders", "stones a man could lift" |
| ἰφθίμη κούρη · ἴφθιμοι Λαιστρυγόνες (10.106, 10.119) | "a daughter, mighty" · "mighty Laestrygonians" | "a mighty daughter" · "mighty Laestrygonians" | "stout", "sturdy", "strong" — "mighty" as in the table’s ἴφθιμος |
| κακὸς κόναβος (10.122) | "an evil din" | "a terrible din" | "dreadful clatter", "ugly noise" |
| ἰχθῦς δ’ ὣς πείροντες ἀτερπέα δαῖτα φέροντο (10.124) | "and, like fish, piercing them, a joyless feast they carried off" | "and, piercing them like fish, they carried off a joyless feast" | "spearing", "gutting"; "joyless" follows the shipped ἀτερπής "joyless" (odyssey-032) |
| πολυβενθής (10.125, λιμένος πολυβενθέος) | "very deep" | "deep" | "of many depths", "bottomless", "deep-bottomed" |
| ξίφος ὀξύ · φάσγανον ὀξύ (10.126; 10.145) | "sharp sword" | "sharp sword" | "keen blade", "bright blade"; both nouns are "sword" (as ἔγχος and δόρυ are both "spear"), following the shipped 9.300 |
| ἐπηρεφέας πέτρας (10.131) | "the overhanging rocks" | "the overhanging rocks" | "roofing", "beetling", "jutting" (kept for προβλῆτες) |
| ἀσπασίως φύγε (10.131) | "gladly … fled" | "with joy … fled" | follows the table’s ἀσπασίως "gladly" / "with joy" |
| Αἰαίη νῆσος (10.135) | "the Aeaean island" | "the island of Aeaea" | "the Aeaean isle", "Aia"; follows the shipped Αἰαίη at 9.32 |
| Κίρκη ἐυπλόκαμος (10.136) | "Circe, fine-plaited" | "fine-plaited Circe" | "fair-haired", "fair-tressed" — the table’s ἐυπλόκαμος |
| δεινὴ θεὸς αὐδήεσσα (10.136; Circe’s standing phrase) | "a dread goddess endowed with speech" | "a dread goddess who speaks with a human voice" (+ note: ancient explanation; force of αὐδήεις debated) | "a goddess with a human voice" and "terrible goddess of human speech" (turn a word of uncertain force into a fact); built on the table’s δεινὴ θεός "dread goddess" and βροτὸς αὐδήεσσα |
| αὐτοκασιγνήτη (10.137) | "own-sister" | "own sister" | "full sister", "sister" alone |
| ὀλοόφρων Αἰήτης (10.137) | "baleful-minded Aeetes" | "baleful-minded Aeetes" | "deadly-minded", "wise Aeetes", "baneful-minded" (kept for ὀλοφώια); follows the shipped "baleful-minded Atlas" (ὀλοόφρονος Ἄτλαντος, 1.52, odyssey-001) — reviewer’s change, the drafter’s "deadly-minded" contradicted the shipped rendering of the same word |
| φαεσίμβροτος Ἠέλιος (10.138) | "the mortal-lighting Sun" | "the Sun, who gives light to mortals" | "bright", "mortal-brightening", "light of men" |
| Ὠκεανός · Πέρση (10.139) | "Oceanus" · "Perse" | same | "Okeanos", "Perses" |
| περιωπή (10.146) | "a vantage-point" | "a vantage-point" | "a lookout" (reserved for σκοπιή), "a peak", "a watch-place" |
| ἔργα βροτῶν · ἔργα βοῶν ἀνδρῶν (10.147; 10.98) | "works of mortals" · "works of oxen and of men" | "the works of mortals" · "work of oxen or of men" | "deeds of men", "farms", "tillage" (all interpret ἔργα) |
| ἐνοπή (10.147) | "a voice" | "a voice" | "a cry", "a sound", "a shout" |
| αἴθοπα καπνόν (10.152) | "the fire-faced smoke" | "the smoke that has the look of fire" | "glowing", "fiery smoke", "bright"; built the same way as the table’s αἶθοψ οἶνος |
| ὧδε δέ μοι φρονέοντι δοάσσατο κέρδιον εἶναι (10.153) | "And thus to me considering it seemed better to be," | "And this, as I thought it over, seemed to me the better course:" | follows the shipped δοάσσατο at 5.474 and 6.145 |
| νῆα θοὴν καὶ θῖνα θαλάσσης (10.154) | "the swift ship and the shore of the sea" | "the swift ship and the shore of the sea" | "the beach", "the sand"; νηῦς θοή keeps the table’s "swift ship" |
| ὑψίκερων ἔλαφον μέγαν (10.158) | "a high-horned stag, great" | "a great high-horned stag" | "antlered", "tall-antlered", "deer" |
| ἀπὸ δ’ ἔπτατο θυμός (10.163) | "and away flew his life" | "and his life flew away" | "his heart flew", "his spirit flew away" (θυμός is "heart" in the house, but what leaves the body at death is the life; the note says so once) |
| ἄκνηστις (10.161) | "the spine" | "the spine" | "the chine", "the backbone" |
| ῥῶπες · λύγοι (10.166) | "twigs" · "withies" | "twigs" · "withies" | "brushwood", "osiers", "saplings" |
| δεινὸν πέλωρ (10.168, δεινοῖο πελώρου) | "the dread monster" | "the dread monster" | "terrible monster", "huge beast"; "dread" as in the table’s δεινός |
| καταλοφάδεια (10.169) | "across-the-neck" | "slung across my neck" | "on my back", "over my shoulders" (ἐπ’ ὤμου "on the shoulder" is separate, 170) |
| ματίη (10.79) | "foolishness" | "foolishness" | "folly" (reserved for ἀφραδίη, "folly"/"follies"), "wanton folly" (ἀτασθαλίαι) |
| ἀλεγεινός (10.78, εἰρεσίης ἀλεγεινῆς) | "grievous" | "grievous" | follows the shipped "grievous" for ἀλεγεινός (odyssey-034) |
| ἁγνὴ Περσεφόνεια (11.386) | "pure Persephone" | "pure Persephone" | "noble" (ἀγαυή, shipped of her in odyssey-053), "holy" (reserved for ἠγάθεος), "chaste"; follows the table's Ἄρτεμις ἁγνή "the pure" |
| ἱεράων Ἀθηνάων (11.323, of the city) | "sacred Athens" | "sacred Athens" | "holy Athens" (reserved for ἠγάθεος; the shipped "holy citadel" is a one-off for ἱερὸν πτολίεθρον), "hallowed" |
| Δίῃ ἐν ἀμφιρύτῃ (11.325) | "in flowed-around Dia" | "in Dia, with the sea running all round it" | "washed on every side by the sea" (the draft; the same adjective is shipped in `i` as "with the sea running all round it" at 1.50 and 1.198), "sea-girt" (reserved for ἀμφίαλος), "wave-washed" (reserved for πολύκλυστος), "surrounded by the sea" |
| Διονύσου μαρτυρίῃσιν (11.325, plural noun) | "on Dionysus’ testimony" | "on the testimony of Dionysus" | "by the witness of", "as Dionysus bore witness" (the Greek does not say what he testified) |
| ἀπόνητο (11.324, ἦγε μέν, οὐδ’ ἀπόνητο) | "had no enjoyment of her" | "had no enjoyment of her" | "had no joy of her" (the draft; a stock phrase that may be remembered rather than built from ἀπονίναμαι "have profit or enjoyment of"), "had no profit of her", "got nothing from her" |
| χρυσὸν φίλου ἀνδρὸς ἐδέξατο τιμήεντα (11.327; genitive of price) | "gold for her dear husband accepted, precious" | "accepted precious gold as the price of her dear husband" | "gold from her husband" (reverses the sense of the genitive), "valuable gold" |
| στυγερός (11.326, στυγερὴν … Ἐριφύλην) | "hateful" | "hateful" | "odious", "loathsome", "hated"; follows the table’s στυγεροὶ ἐπέεσσιν "hateful words" |
| πρὶν γάρ κεν καὶ νὺξ φθῖτ’ ἄμβροτος (11.330) | "for sooner would even the night perish, deathless." | "for even the night, deathless though it is, would be spent before I finished." | "immortal night" (ἄμβροτος is "deathless", reserved against ἀθάνατος), "the night would end" |
| ἀκὴν ἐγένοντο σιωπῇ … κηληθμῷ δ’ ἔσχοντο (11.333–334; first half shipped) | "and were held by a spell" | "held in a spell" | "bewitched", "charmed into stillness", "held captive"; κηληθμός is "spell" |
| μέγαρα σκιόεντα (11.334) | "the shadowy halls" | "the shadowy halls" | "dim", "shady" (suggests shade-trees); follows the table’s ὄρεα σκιόεντα |
| φρένας ἔνδον ἐίσας (11.337) | "the wits within, well-balanced" | "the well-balanced mind within" | "equal", "fair", "even-tempered"; ἐίσας keeps the table’s "well-balanced" (sense uncertain, as flagged at 3.10) |
| ξεῖνος δ’ αὖτ’ ἐμός ἐστιν (11.338; ξεῖνος of the host–guest bond) | "And a guest-friend, moreover, mine he is" | "Moreover he is my guest-friend" | "my stranger" (the draft; the table gives "guest-friend" for ξεῖνος of the bond, and 1.417 ξεῖνος δ’ οὗτος ἐμός and 8.208 ξεῖνος γάρ μοι ὅδ’ ἐστί ship "guest-friend"), "my guest", "my friend" |
| ἕκαστος δ’ ἔμμορε τιμῆς (11.338) | "each has a share of honour" | "each of you has a share of honour" | "his due of honour", "honours him" |
| κολούετε (11.340) | "curtail" | "cut short" | "stint", "reduce", "withhold" |
| χρηίζοντι (11.340) | "to one so in need" | "for a man in such need" | "who asks for it", "wanting" |
| θεῶν ἰότητι (11.341) and κακῆς ἰότητι (11.384) | "by the gods’ will" / "through the evil will" | "by the will of the gods" / "through the evil will of a woman" | "by the favour of the gods", "by the gods’ grace", "wickedness" (ἰότης is will, one word throughout) |
| ἀπὸ σκοποῦ οὐδ’ ἀπὸ δόξης (11.344) | "wide of the mark nor away from opinion" | "wide of the mark, or at odds with what we think" (+ note: ἀπὸ δόξης could be "against expectation") | "off target", "contrary to reason" |
| βασίλεια περίφρων (11.345) | "the queen, circumspect" | "the circumspect queen" | "wise queen", "prudent queen" (reserved for πεπνυμένος); keeps the table’s περίφρων "circumspect" |
| ἔργον τε ἔπος τε (11.346) | "both deed and word" | "both action and word" | "word and deed" (reverses the Greek order), "act and speech" |
| τοῖσι δὲ καὶ μετέειπε γέρων ἥρως Ἐχένηος (11.342) | "And among them spoke also the old hero Echeneus," | "And among them the old hero Echeneus spoke up as well," | "addressed", "answered"; follows the table’s τοῖσι δὲ καὶ μετέειπε θεά … and the shipped γέρων ἥρως Ἐχένηος (7.155) |
| τοῦ γὰρ κράτος ἔστ’ ἐνὶ δήμῳ (11.353; τοῦ points back to the speaker; δῆμος as in the table, "land") | "for of him the power is in the land" | "for the power in the land is mine" | "among the people" (the draft; the table keeps "land" for δῆμος and "people" for λαός), "for it is I who hold power" (adds a cleft emphasis), "for he has power over the people" (loses the first person), "authority", "might" |
| δωτίνη (11.352, πᾶσαν δωτίνην) | "the whole gift" | "the whole gift" | "present", "bounty", "all his gifts" (δῶρα is the plural "gifts") |
| πομπὴ … μελήσει (11.332, 11.352; different lines, same verb) | "my escort will be a care to" (332) / "the escort will be a care to" (352) | "my escort will be the concern of" (332) / "his escort will be the care of" (352) | "the sending-off will be seen to", "the conveyance will be arranged"; follows the table’s πομπή "escort" |
| τλήτω · τλαίης · ἔτλη (11.350, 11.376, 11.425) | "let him endure" · "you were to bring yourself" · "she brought herself" | "let him bring himself" · "you could bring yourself" · "she did not bring herself" | "dare" (keep for θαρσέω), "have the heart to"; τλάω is "endure, bring oneself to" throughout, as in the table’s πολύτλας "much-enduring" |
| καί κεν πολὺ κέρδιον εἴη (11.358) | "much better it would be" | "far better" | "more profitable" (the note gives the sense), "much more to my advantage"; follows the table’s κέρδιον "better" |
| πλειοτέρῃ σὺν χειρί (11.359) | "with a fuller hand" | "with a fuller hand" | "with more in my hands", "richer"; the image is kept and the note explains it |
| αἰδοιότερος καὶ φίλτερος (11.360) | "more revered and dearer" | "the more revered, and dearer" | "more honoured and beloved" (αἰδοῖος is "revered" as in the table’s αἰδοίοισιν "revered suppliants"; "honored and dear" belongs to the welcome-formula αἰδοῖός τε φίλος τε) |
| ἠπεροπῆα … καὶ ἐπίκλοπον (11.364) | "a deceiver and a thievish one" | "a deceiver and a trickster" | "a cheat and a liar", "a liar and a thief" (ἐπίκλοπος is "thievish, sly"; ψεύδεα carries the lying) |
| γαῖα μέλαινα (11.365) | "the dark earth" | "the dark earth" | "black earth" (μέλας is "black" of ships and, in `l`, of night, but "dark" of wine, water and wave; the earth is kept with the latter), "the black soil" |
| πολυσπερέες ἄνθρωποι (11.365) | "men widely scattered" | "men scattered far and wide" | "teeming", "numerous" (loses σπείρω "scatter") |
| ψεύδεα … ἀρτύνοντας (11.366) | "fashioning lies" | "who fashion lies" | "inventing", "weaving", "plotting" (δόλον ὑφαίνειν is "weave a trick") |
| μορφὴ ἐπέων (11.367) | "a shape of words" | "your words have a shapely grace" | "beauty of speech", "eloquence" |
| φρένες ἐσθλαί (11.367) | "good wits" | "good sense" | "noble mind", "sound heart"; ἐσθλός is "good" throughout, as in ἐσθλὸς ἑταῖρος |
| ἐπισταμένως (11.368) | "skilfully" | "skilfully" | "knowingly", "expertly", "with knowledge" |
| ἀθέσφατος (11.373, of the night) | "immense" | "immense" (+ note: sense uncertain) | "endless", "boundless" (reserved for ἀπείρων), "vast"; same word, same rendering as the table’s ἀθέσφατος |
| θέσκελα ἔργα (11.374; meaning unknown) | "marvellous deeds" | "marvellous deeds" (+ note: meaning of θέσκελος not known) | "wondrous deeds" (reserved for θεσπέσιος), "god-wrought deeds", "godlike" (silently picks one guess) |
| ἐς ἠῶ δῖαν (11.375) | "to heavenly dawn" | "until heavenly dawn" | "bright dawn", "divine dawn" (reserved for θεῖος); δῖος keeps the table’s "heavenly" |
| ὥρη μὲν πολέων μύθων, ὥρη δὲ καὶ ὕπνου (11.379) | "a time for many tales, and a time too for sleep" | "there is a time for many tales, and a time also for sleep" | "an hour", "a season"; μῦθος is "tale" here, "talk" in μύθων ἤρχετο |
| φθονέοιμι (11.381) | "would begrudge" | "would not begrudge" | "refuse", "forbid", "envy"; shares its stem with the table’s ἐπιφθονέω "grudge / begrudge" |
| οἰκτρός (comparative 11.381, superlative 11.412, 11.421) | "more pitiable" · "most pitiable" | "more pitiable" · "most pitiable" | "piteous", "pitiful" (reserved for λευγαλέος), "wretched" (δύστηνος), "sad"; the table’s ἐλεεινός (8.530) is also "pitiable", the two words (ἔλεος "pity", οἶκτος "lament") told apart by context |
| στονόεσσα ἀυτή (11.383) | "groan-filled battle-cry" | "groan-filled battle-cry" | "groaning din", "tearful", "mournful"; στονόεις is built on στόνος "groan" |
| ἄλλυδις ἄλλῃ (11.385) | "this way and that" | "this way and that" | "hither and thither", "in all directions" |
| γυναικῶν θηλυτεράων (11.386, 11.434) | "of women, the female ones" | "of the women" (11.386) / "women" (11.434) | "of the weaker sex", "womanly"; θηλυτέρων is a comparative in form only |
| ψυχὴ Ἀγαμέμνονος Ἀτρεΐδαο (11.387) | "the soul of Agamemnon, Atreus’ son" | "the soul of Agamemnon, son of Atreus" | "the shade of", "the ghost of" (reserved for σκιαί and εἴδωλον); follows the table’s Ἀτρεΐδῃ Ἀγαμέμνονι |
| ἀχνυμένη (11.388) | "grieving" | "grieving" | "sorrowing", "mourning", "troubled" |
| ἀγηγέραθ’ (11.388) | "were gathered" | "were gathered" | "assembled", "crowded" |
| οἴκῳ ἐν Αἰγίσθοιο (11.389) | "in the house of Aegisthus" | "in the house of Aegisthus" | "Aegisthus’ hall", "his hall"; no epithet is given to Aegisthus here |
| λιγέως (of weeping, 11.391) | "clearly" | "in a clear voice" | "shrilly", "loudly", "bitterly"; follows the table’s λιγέως "clearly / in a clear voice" |
| κατὰ δάκρυον εἴβων (11.391) | "an abundant tear letting fall" | "letting abundant tears fall" | "shedding" (reserved for χέων), "pouring" (reserved for λείβων), "weeping"; θαλερὸν δάκρυον keeps the table’s "abundant" |
| πιτνὰς εἰς ἐμὲ χεῖρας (11.392) | "spreading his hands toward me" | "spreading out his hands toward me" | "stretching out", "holding out" (keep for ὀρέγομαι ὀρέξασθαι) |
| ὀρέξασθαι μενεαίνων (11.392) | "to reach, eager" | "straining to reach me" | "longing to embrace", "desperate to", "furious" |
| ἲς ἔμπεδος οὐδέ τι κῖκυς (11.393; κῖκυς a rare noun) | "firm force, nor any vigour" | "firm strength or vigour" | "steady strength", "power", "might" (reserved for κράτος); ἲς keeps "force" in `l` as in ἱερὴ ἲς |
| γναμπτοῖσι μέλεσσι (11.394) | "pliant limbs" | "supple limbs" | "bending", "curved", "strong"; γναμπτός is "bent, supple" |
| Ἀτρεΐδη κύδιστε, ἄναξ ἀνδρῶν Ἀγάμεμνον (11.397) | "Atreus’ son, most glorious, lord of men, Agamemnon," | "Son of Atreus, most glorious Agamemnon, lord of men," | "most famous", "noblest" for κύδιστε; keeps the table’s Ἀτρεΐδη … and ἄναξ ἀνδρῶν Ἀγαμέμνων "lord of men" |
| ἦε σέ γ’ ἐν νήεσσι Ποσειδάων ἐδάμασσεν (11.399; the sea-question) | "Was it that you in the ships Poseidon subdued," | "Was it Poseidon who overcame you among your ships," | "struck down", "killed", "destroyed"; ἐδάμασσεν keeps the shipped "subdued" / "overcame" of 11.398 |
| ἀμέγαρτον ἀυτμήν (11.400; meaning uncertain) | "the unenviable blast" | "a dreadful blast" (+ note: traditionally "not to be envied", so "dreadful"; sense uncertain) | "pitiless", "merciless", "unrelenting" (each picks one guess), "cruel breath" |
| ἀργαλέων ἀνέμων (11.400) | "of grievous winds" | "of grievous winds" | "harsh", "baneful", "fierce"; ἀργαλέος keeps the table’s "grievous" |
| ἀνάρσιοι ἄνδρες (11.401) | "hostile men" | "hostile men" | follows the table’s ἀνάρσιοι ἄνδρες (10.459) |
| ἐδηλήσαντ’ ἐπὶ χέρσου (11.401) | "harmed you on dry land" | "harmed you on dry land" | "hurt", "wounded", "injured"; χέρσος is "dry land" as the opposite of the sea |
| βοῦς περιταμνόμενον (11.402) | "cutting off cattle" | "driving off cattle" | "raiding", "rustling", "cutting out" |
| περὶ πτόλιος μαχεούμενον ἠδὲ γυναικῶν (11.403) | "fighting for a city and for women" | "fighting for a city and for women" | "defending", "for their wives"; περί with the genitive is "for, about" |
| οὔτ’ ἐμέ γ’ … οὔτε μ’ (11.406–408) | "neither me … nor …" | "Poseidon did not … nor did hostile men …" | "it was not … that", "neither … nor" in `i` (kept for the Greek order in `l` only) |
| θάνατόν τε μόρον τε (11.409) | "both death and doom" | "death and doom" | follows the table’s row for 9.61, the same two nouns; the draft’s "death and portion" / "death and an allotted end" clashed with it (the note glosses μόρος as the allotted portion) |
| ἔκτα σὺν οὐλομένῃ ἀλόχῳ (11.410) | "killed me, with (my) ruinous wife" | "killed me with my ruinous wife" | "accursed", "cursed" (the draft; the table’s φάρμακον οὐλόμενον is "the ruinous drug" and lists "accursed" as avoided), "baneful" (reserved for ὀλοφώια); οὐλόμενος is a curse-word, which the note says once |
| οἶκόνδε καλέσσας (11.410) | "having called me to his house" | "after calling me to his house" | "invited me home", "summoned" |
| δειπνίσσας (11.411; second half of the line shipped in odyssey-018) | "having feasted me" | "feasting me" | "given me dinner", "entertained"; the shipped wording of ὥς τίς τε κατέκτανε βοῦν ἐπὶ φάτνῃ is kept |
| ὣς θάνον οἰκτίστῳ θανάτῳ (11.412) | "So I died by a most pitiable death" | "So I died, by a most pitiable death" | "a most wretched death", "a sad end" |
| νωλεμέως κτείνοντο (11.413) | "unceasingly were being killed" | "were slaughtered without pause" | "relentlessly", "one after another", "were cut down" |
| ἀφνειοῦ ἀνδρὸς μέγα δυναμένοιο (11.414) | "of a rich man, greatly powerful" | "of a rich and powerful man" | "of a wealthy lord", "of a mighty man" (reserved for ἴφθιμος) |
| ἢ γάμῳ ἢ ἐράνῳ ἢ εἰλαπίνῃ τεθαλυίῃ (11.415) | "at a wedding, or a meal of shared contributions, or a flourishing banquet" | "at a wedding, or a meal where each man brings his share, or a flourishing banquet" | "contribution-feast", "club-feast", "picnic" for ἔρανος (the shipped 1.226 is "meal of shared contributions" / "meal where each man brings his share"); "abundant" for τεθαλυῖα (the draft; τεθαλυῖα is shipped "flourishing" at 6.293 and 11.192, and the table keeps "abundant" for θάλεια / θαλερός), "glorious", "rich" |
| κρατερὴ ὑσμίνη (11.417) | "strong battle" | "strong battle" | "mighty" (reserved for ἴφθιμος), "fierce" (kept for ἄγριος), "hard" (reserved for tasks), "stern" |
| μουνὰξ κτεινομένων (11.417) | "of men killed singly" | "men killed one by one" | "in single combat" (that is μονομαχία, a later word), "alone" |
| κρητῆρα … τραπέζας τε πληθούσας (11.419) | "the mixing-bowl and the tables, full" | "the mixing-bowl and the laden tables" | "overflowing", "crowded", "heaped"; κρητήρ keeps "mixing-bowl" as shipped |
| δάπεδον δ’ ἅπαν αἵματι θῦεν (11.420) | "the whole floor seethed with blood" | "the whole floor seethed with blood" | "ran with blood", "swam in blood", "was awash" (θύω is "rush, seethe") |
| Κασσάνδρης, τὴν κτεῖνε Κλυταιμνήστρη δολόμητις (11.422) | "Cassandra, whom killed Clytemnestra of guileful counsel" | "Cassandra, whom Clytemnestra of guileful counsel killed" | "crafty", "treacherous", "wily" for δολόμητις; built like the table’s Αἴγισθος δολόμητις "of guileful counsel"; Κλυταιμνήστρη keeps the shipped "Clytemnestra" |
| βάλλον ἀποθνήσκων περὶ φασγάνῳ (11.424) | "kept casting them, dying, around the sword" | "dying around the sword, lifted my hands and let them fall" | "pierced by the sword" (the Greek says only "around"), "on the sword"; the note leaves the picture open |
| κυνῶπις (11.424) | "dog-faced" | "the shameless one" | follows the table’s κυνῶπις "dog-faced" / "shameless" |
| χερσὶ κατ’ ὀφθαλμοὺς ἑλέειν σύν τε στόμ’ ἐρεῖσαι (11.426) | "to close my eyes and to press my mouth together" | "to close my eyes … or to press my mouth shut" | "to lay hands on", "to shut my lids and jaws"; the note gives κατὰ … ἑλέειν as "take down over" |
| αἰνότερον καὶ κύντερον (11.427) | "more fearsome and more dog-like" | "more fearsome or more shameless" | "more terrible", "more dreadful" (reserved for δεινός), "more bitch-like" (turned down at κυνῶπις); αἰνός keeps "fearsome" as the table’s αἰνὰ πέλωρα |
| ἔργον ἀεικές (11.429) | "an unseemly one" | "an unseemly deed" | "shameful", "disgraceful", "ugly"; follows the table’s ἀεικέα πότμον "an unseemly doom" |
| κουριδίῳ πόσει (11.430) | "to her wedded husband" | "her wedded husband" | "her lawful husband", "her young husband", "her husband of her youth" |
| τεύξασα φόνον (11.430; cf. τεύξας θάνατον, 11.409) | "contriving … slaughter" | "contriving the murder of" | "making", "bringing about", "plotting"; τεύχω is "contrive" in both lines |
| ἀσπάσιος παίδεσσιν ἰδὲ δμώεσσιν ἐμοῖσιν (11.431) | "welcome to my children and to my servants" | "a welcome sight to my children and my servants" | "gladly received by", "dear to"; follows the table’s ἀσπάσιος "a welcome sight" |
| ἔφην (11.430, ἦ τοι ἔφην γε) | "I said" | "I had supposed" | "I thought" in `l`, "I swore"; φημί is "say" in `l` throughout, and "suppose" is allowed in `i` where a thought is reported |
| ἔξοχα λυγρὰ ἰδυῖα (11.432) | "knowing outstandingly grievous things" | "who knew grievous things beyond all others" | "skilled in evil", "versed in cruelty", "knowing wicked things"; ἰδυῖα keeps "knowing", as in the table’s κεδνὰ ἰδυῖα |
| κατ’ αἶσχος ἔχευε (11.433) | "for herself shame poured down" | "poured shame down upon herself" | "heaped disgrace", "cast shame"; follows the table’s θεσπεσίην … χάριν κατέχευεν "poured-down" |
| ἐσσομένῃσιν ὀπίσσω θηλυτέρῃσι γυναιξί (11.433–434) | "those yet to be, hereafter, female women" | "women yet to come" | "future women", "women of times to come"; ἐσσόμενοι keeps the table’s "those yet to come" |
| ἥ κ’ ἐυεργὸς ἔῃσιν (11.434) | "whichever may be well-working" | "the one who does well" | "virtuous", "upright" (each fixes a moral sense the word may not carry), "good worker"; ἐυεργός is kept distinct from ἐυεργής "well-made" (9.202) |
| Names in 11.321–434 | Phaedra, Procris, Ariadne, Minos, Theseus, Crete, Athens, Artemis, Dia, Dionysus, Maera, Clymene, Eriphyle, Arete, Echeneus, Alcinous, Ilios, Persephone, Agamemnon, Atreus, Aegisthus, Poseidon, Laertes, Priam, Cassandra, Clytemnestra, Hades | same | "Phaidra", "Prokris", "Klytaimnestra", "Kassandra", "Eriphyle" as "Eriphyl" etc.; the familiar Latinised forms, as for the other names in the table |

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
| δὴ τότε / δή ῥα τότ’ … προσέφη (non-reply introduction of a speech: 8.423, 8.474, 8.486; e.g. δὴ τότε Δημόδοκον προσέφη πολύμητις Ὀδυσσεύς) | "Then indeed to X addressed Y:" | "Then Y said to X:" | "answered" (reserved for ἠμείβετο), "spoke to … in turn" (reserved for αὖτε); "addressed" kept for προσέφη in `l` as in the reply-formulas |
| πάτερ ὦ ξεῖνε (8.408, courteous address to an older stranger) | "father, O stranger" | "stranger, my father" | "father" alone (drops ξεῖνε), "old man" (reserved for ὦ γέρον), "honoured stranger" |
| γύναι (vocative, husband to wife, 8.424) | "wife" | "wife" | "woman" (curt), "lady" (reserved for πότνια / δέσποινα), "queen" (reserved for ἄνασσα) |
| κούρη (vocative, 8.468) | "maiden" | "maiden" | "girl", "daughter" (reserved for θύγατερ / κούρη Διός as a noun-phrase), "child" |
| ἀριπρεπής (8.390, 8.424) | "outstanding" | "outstanding" | "conspicuous" (reserved for ἀριδείκετος), "eminent", "splendid" (reserved for ἀγλαός) |
| περικαλλής (of gifts, chest, goblet: 8.420, 8.430, 8.438) | "very fair" | "very fair" | "very-beautiful", "very beautiful", "surpassingly fair", "most beautiful", "exceedingly lovely"; the περι- prefix is kept as "very"; follows the table row περικαλλής (6.85) |
| κάλλιμα δῶρα (8.439) | "fair gifts" | "fair gifts" | "lovely gifts" (reserved for ἐρατεινός / ἐραννός), "beautiful", "fine" (reserved for καλός); κάλλιμα is from κάλλος like περικαλλής, "very fair", and καλλι- is "fair" elsewhere |
| ξίφος ἀργυρόηλον (8.406, 8.416) | "the silver-studded sword" | "the silver-studded sword" | "silver-nailed", "silver-hilted" (the hilt is separately ἀργυρέη κώπη); follows the shipped "silver-studded chair" (8.65) |
| ἀργυρέη κώπη (8.403–404) | "a hilt of silver" | "a hilt of silver" | "silver handle", "silver-hilted" |
| ποικίλος δεσμός (8.448, of Circe's knot) | "intricate fastening" | "an intricate fastening" | "inlaid" (reserved for ποικίλος of wood and metal work), "many-coloured", "cunning knot" |
| πότνια Κίρκη (8.448) | "the lady Circe" | "the lady Circe" | "Queen", "mistress", "revered Circe"; follows πότνια νύμφη and πότνια Ἥρη |
| ἠύκομος Καλυψώ (8.452, ἠυκόμοιο) | "fine-haired Calypso" | "fine-haired Calypso" | "fair-haired" (reserved for ξανθός), "fair-tressed" (reserved for ἐυπλοκαμῖδες), "well-braided", "lovely-haired" |
| ἐρίγδουπος πόσις Ἥρης (8.465) | "loud-crashing husband of Hera" | "loud-crashing husband of Hera" | "far-thundering" (reserved for εὐρύοπα), "deep-thundering", "loud-thundering" (the compound is ἐρι- + δοῦπος 'a heavy crash'; thunder is the traditional reading only) |
| λοετροχόος τρίπους (8.435) | "the bath-water tripod" | "the bath-water tripod" | "bath-pouring tripod", "bath tripod", "cauldron" (the tripod is the stand-and-vessel; the word stays "tripod") |
| πῦρ κηλέον (8.435) | "the blazing fire" | "the blazing fire" (+ note: meaning uncertain, traditional gloss) | "burning", "flaming", "crackling" (silently picks one guess) |
| ἀσάμινθος (8.450, 8.456) | "bath" | "bath" | "bath-tub", "basin", "tub" alone; follows the table row ἔκ ῥ’ ἀσαμίνθου (3.468) "out of the bath"; the plural θερμὰ λοετρά stays "the warm baths" |
| θερμὰ λοετρά (8.451) | "the warm baths" | "the warm baths" | "hot baths", "warm water" |
| θαλερὴ ἀλοιφή (8.476) | "abundant fat" | "abundant" | "blooming" (reserved for θαλερὸς γάμος), "thick", "rich fat"; θαλερός keeps the root-sense of the shipped δαὶς θάλεια "abundant feast" |
| ἀργιόδων ὗς (8.476, ἀργιόδοντος ὑός) | "a white-toothed pig" | "a white-toothed pig" | "white-tusked", "gleaming-toothed"; follows the shipped ἀργιόδοντας ὕας (8.60) |
| ἀοιδός (generic, 8.479–481) | "minstrel(s)" | "minstrel(s)" | "singer(s)", "bard(s)", "poet(s)"; follows the shipped ἐρίηρος ἀοιδός "trusty minstrel" and θεῖος ἀοιδός "divine minstrel" |
| ἔμμορος (with genitive, 8.480) | "have a share of" | "have their share of" | "partake of", "are entitled to" |
| οἴμη (8.481) | "lays" (note: also 'paths of song') | "lays" | "songs" alone, "paths" (drops the song), "themes" |
| ὕμνος (of song, 8.429) | "strain" | "strain of song" | "hymn" (implies a god's praise), "lay" (reserved for οἴμη) |
| ἐπιχθόνιος ἄνθρωποι (8.479) | "men upon the earth" | "men who live on the earth" | "earthly men", "men on earth below", "mortals" (reserved for βροτοί) |
| ζωάγρια (8.462) | "life-price" | "the price of your life" | "reward for saving my life", "thank-offering", "life-debt" |
| ἐπιεικές (8.389, ὡς ἐπιεικές) | "as is fitting" | "as is fitting" | "as is proper", "as is right" (keeps the κατὰ μοῖραν rendering, since the sense is the same) |
| ξεινήιον (8.389) | "guest-gift" | "a guest-gift" | "hospitality gift", "parting present" |
| ἀρέσσασθαι / ἀρεσσάμενος (8.396, 8.402, 8.415) | "appease" / "having appeased" | "make amends to" / "when you made amends" | "please", "satisfy", "reconcile", "placate" |
| ἀγαυός (of heralds, 8.418) | "noble" | "the noble heralds" | "illustrious", "proud"; the same word as the shipped μνηστῆρες ἀγαυοί "noble suitors" |
| μοῖρα (plural, of meat, 8.470) | "portions" | "portions" | "shares", "fates" |
| αὐτόδιον (8.449) | "straightway" | "at once" | "on the spot", "right away" |
| ἀσπασίως (8.450) | "gladly" | "with joy" | "welcome", "willingly" |
| ὅττι τάχιστα (8.434) | "as quickly as possible" | "as quickly as possible" | "with all speed", "at once" |
| τόφρα (8.438 "meanwhile"; 8.453 "for that time") | "meanwhile" / "during that time" | "meanwhile" / "for that time" | "then", "so long" |
| ἦ ῥα καί (mid-narrative, 8.416, 8.469) | "He spoke, and" | "So he said, and" | keeps the table's ἦ ῥα rendering, extended to the ἦ ῥα καί form |
| τῆ δή, τοῦτο πόρε κρέας (8.477) | "here, this meat give" | "here, take this meat and give it" | "here you are", "there, take this" |
| ἄλεισον (8.430) | "goblet" | "goblet" | keeps the table's reservation (3.50/53) |
| ἥρως Δημόδοκος (8.483) | "the hero Demodocus" | "the hero Demodocus" | follows the table's ἥρως "the hero" |
| θέσπις ἀοιδή (8.498, θέσπιν ἀοιδήν) | "god-spoken song" | "inspired song" (+ note: formation of θέσπις usually explained as θεός + root of ἔπος, not certain) | "divine song" (reserved for θεῖος), "wondrous song" (reserved for θεσπέσιος), "sweet song" |
| ἀμφικαλύπτω (8.511 ἀμφικαλύψῃ, 8.569 ἀμφικαλύψειν) | "enfold" | "enfold" / "enfolded" | "cover", "shroud", "close over" (the echo between the horse in Troy and the mountain over the Phaeacian city is the point) |
| καλύπτω, perf. part. (8.503 κεκαλυμμένοι ἵππῳ, 8.562 κεκαλυμμέναι ἠέρι καὶ νεφέλῃ) | "hidden" | "hidden" | "covered", "wrapped", "veiled" |
| κατὰ κόσμον (8.489) / ἵππου κόσμον (8.492) | "in due order" / "the ordering of the horse" | "in very good order" / "the contriving of the wooden horse" | one English word for both (the two uses of κόσμος differ: proper sequence, then the fitting-out of the horse) |
| νηλεής (8.507 νηλέι χαλκῷ, 8.525 νηλεὲς ἦμαρ) | "pitiless" | "pitiless" | "ruthless", "cruel", "merciless" |
| ἐλεεινός (8.530 ἐλεεινοτάτῳ, 8.531 ἐλεεινόν) | "pitiable" | "pitiable" | "piteous", "pitiful" (reserved for λευγαλέος "pitiful") |
| γαῖα (8.555, in the list γαῖαν … δῆμον … πόλιν) | "country" | "country" | "earth", "soil" (the plain senses), "land" (reserved for δῆμος, per the table's 8.211 row) |
| ἠμὲν ὅσοι χαλεποί τε καὶ ἄγριοι οὐδὲ δίκαιοι, / οἵ τε φιλόξεινοι, καί σφιν νόος ἐστὶ θεουδής (8.575–576, two-line formula, said of the peoples a wanderer may meet) | "both those who are harsh and savage and not just,\nand those who are guest-loving, and to them a mind is god-fearing" | "both those who are harsh and savage and unjust, and those who are hospitable and whose minds are god-fearing" | "wild", "cruel", "lawless" (each drops one of the three words), "kindly to strangers" (drops the ξένος), "pious" for θεουδής (loses δέος "fear") |
| χαλεπός (8.575) | "harsh" | "harsh" | "grievous" (reserved for λυγρός / ἀργαλέος), "cruel", "hard" |
| φιλόξεινος (8.576) | "guest-loving" | "hospitable" | "friendly", "kind to strangers"; φίλος + ξένος kept visible in `l` |
| θεουδής (8.576) | "god-fearing" | "god-fearing" | "pious", "reverent" (both lose δέος) |
| πηός (8.581) | "kinsman-by-marriage" | "a relative by marriage" | "kinsman" alone (loses the marriage tie), "in-law" (gets the tie but hides the word as a class) |
| κήδιστος (8.582–583, κήδιστοι τελέθουσι) | "closest-tied" | "closest" | "dearest", "most beloved" (κῆδος is care and tie by marriage, not only affection) |
| ἀγάασθαι (8.565, ἀγάσασθαι ἡμῖν) | "be resentful of" | "resented" | "envy", "be angry with" (each fixes one shade of a word that spans both) |
| Κύκλωπες ὑπερφίαλοι ἀθέμιστοι (9.106, Κυκλώπων … ὑπερφιάλων ἀθεμίστων) | "the Cyclopes, overweening, lawless" | "the Cyclopes, an overweening and lawless people" | "arrogant", "wicked", "godless" (ἀθέμιστος is from θέμις, custom and right; ὑπερφίαλος keeps the table's "overweening" from 6.274) |
| ἀθέμιστος / ἀθεμίστια (9.106, 9.189) | "lawless" / "lawless things" | "lawless" / "lawless ways" | "unjust" (reserved for οὐ δίκαιος), "wicked", "criminal" |
| ἐριστάφυλος (9.111, οἶνον ἐριστάφυλον) | "wine of great clusters" | "wine from great clusters of grapes" | "rich-clustered", "thick-clustered" (ἐρι- is an intensive, kept as "great") |
| ἀγοραὶ βουληφόροι (9.112) | "assemblies that bear counsel" | "assemblies to deliberate in" | "counsel-bearing" as a hyphenated pair, "councils" |
| θέμιστες (9.112, 9.114 θεμιστεύει) | "rules of right" / "lays down the law" | "rules of right" / "lays down the law" | "laws" alone, "justice" |
| νῆσος λάχεια (9.116; meaning uncertain) | "an island, low-lying" | "a low-lying island" (+ note: sense uncertain) | "flat", "level", "wooded" (each silently picks one guess) |
| αἶγες ἄγριαι / ἀπειρέσιαι (9.118–119) | "goats past counting … wild" | "countless wild goats" | "innumerable", "feral" |
| μηκάδες αἶγες (9.124) | "bleating goats" | "the bleating goats" | "she-goats", "meck-goats" (μηκάομαι is 'bleat') |
| νέες μιλτοπάρῃοι (9.125) | "red-cheeked ships" | "red-cheeked ships" | "vermilion-prowed", "red-bowed", "red-painted ships" (παρῃά is 'cheek') |
| ἐυκτιμένην νῆσον (9.130) | "the island well-built" | "a well-settled place" (+ note: `l` keeps "well-built", `i` the sense "well-settled") | "well-founded" (turned down for the citadel), "well-cultivated" |
| ὥρια πάντα (9.131) | "all things in season" | "everything in its season" | "produce", "harvests" |
| ἄφθιτοι ἄμπελοι (9.133) | "unfailing vines" | "the vines would never fail" | "undying", "immortal" (reserved for ἀθάνατος), "imperishable" |
| λιμὴν ἐύορμος (9.136) | "a harbour good for mooring" | "a harbour good for mooring" | "well-anchored", "safe harbour", "sheltered" |
| εὐναί / πρυμνήσια (9.137) | "anchor-stones" / "stern-cables" | "anchor-stones" / "stern-cables" | "anchors" (they are stones), "hawsers", "moorings" |
| ὀρφναίη νύξ (9.143) | "the murky night" | "the murky night" | "dark night" (keep for μέλαινα), "black night", "gloomy" |
| ἀὴρ βαθεῖα (9.144) | "a mist, deep" | "a deep mist" | "air", "fog", "darkness" |
| ἐπὶ ῥηγμῖνι θαλάσσης (9.150, 9.169; the latter shipped at odyssey-017) | "on the surf-line of the sea" | "on the shore where the sea breaks" | "on the beach", "at the water's edge" — follows the wording shipped in odyssey-017 |
| ἀποβρίξαντες (9.151; rare verb) | "having slept" | "slept" (+ note: sense taken from context) | "having dozed", "having slumbered" |
| Ἠὼς δῖα (9.151, Ἠῶ δῖαν) | "heavenly Dawn" | "heavenly Dawn" | "bright Dawn", "divine Dawn" (reserved for θεῖος); keeps the table's δῖος "heavenly" for a goddess, as for the sea at 5.261 |
| νύμφαι, κοῦραι Διὸς αἰγιόχοιο (9.154) | "the nymphs, daughters of aegis-bearing Zeus" | "the nymphs, daughters of aegis-bearing Zeus" (+ note: meaning of αἰγίοχος disputed) | "child of Zeus" (reserved for the noun-phrase Διὸς θυγάτηρ), "goat-bearing", "storm-bearing" |
| αἶγες ὀρεσκῷοι (9.155) | "goats of the mountain-bed" | "mountain goats" (+ note: usual explanation 'lying on the mountains') | "wild goats" (ἄγριαι is already "wild"), "mountain-bred" |
| αἰγανέαι δολιχαύλοι (9.156) | "light spears, long-socketed" | "long-socketed javelins" (+ note: second element uncertain) | "long-shafted", "long-barbed" (silently pick one guess) |
| μενοεικὴς θήρη (9.158) | "a hunt to the heart's liking" | "a catch to our heart's liking" | "a rich hunt", "a hunt to their fill" (lose μένος 'spirit') |
| μέθυ ἡδύ (9.162) | "sweet wine" | "sweet wine" | "honey-sweet" (reserved for μελιηδής), "mellow"; the same word as the table's ἡδὺς οἶνος |
| ἄσπετα κρέα (9.162) | "boundless meat" | "boundless meat" | "unlimited", "endless" — literally 'not to be told' |
| οἶνος ἐρυθρός (9.163) | "red wine" | "red wine" | "dark wine" (μέλας), "ruddy wine", "wine-red" |
| ἀμφιφορεύς (9.164) | "amphora" | "jar" | "flagon", "wine-skin", "urn" |
| ἱερὸν πτολίεθρον (9.165) | "the holy citadel" | "their holy citadel" | "sacred citadel" (ἱερός is 'sacred' in ἱερὸν ἦμαρ; here it matches the shipped "holy citadel" of Troy at 1.2) |
| κνέφας (9.168) | "darkness" | "darkness" | "dusk", "gloom" — as in the table's ἠέλιος δ’ ἄρ’ ἔδυ καὶ ἐπὶ κνέφας ἦλθε |
| ἦμος δ’ ἠέλιος κατέδυ καὶ ἐπὶ κνέφας ἦλθε (whole line, 9.168) | "And when the sun set and darkness came on," | "And when the sun set and darkness came on," | "and the sun then set" (the separate row with ἠέλιος δ’ ἄρ’ ἔδυ) |
| ἀγορὴν θέμενος (9.171) | "an assembly having set" | "called an assembly" | "held an assembly", "made a speech" (reserved for ἀγορήσατο) |
| ὑβρισταί (9.175) | "violent" | "violent" | "insolent", "arrogant" (reserved for ὑπερφίαλος / ὑπερηνορέοντες); follows the wording shipped at 9.176 (odyssey-028) |
| ἄγριοι οὐδὲ δίκαιοι (9.175) | "savage and not just" | "savage and unjust" | "wild", "lawless" (reserved for ἀθέμιστος) |
| ἀνὰ νηὸς ἔβην (9.177) | "up onto the ship I went" | "I went up on board" | "I boarded", "I climbed the ship" |
| ἐπ’ ἐσχατιῇ (9.182) | "at the edge" | "at its edge" | "at the far end", "on the outskirts" |
| σπέος … δάφνῃσι κατηρεφές (9.182–183) | "a cave … roofed over with laurels" | "a cave … roofed over with laurels" | "shaded by laurels", "covered with bay" |
| ἰαύεσκον (9.184, of the flocks) / ἐνίαυε (9.187, of the man) | "used to sleep" | "used to sleep" | "slept" (drops the iterative -εσκον) |
| μῆλα (small livestock, 9.184 μῆλ’ ὄιές τε καὶ αἶγες, 9.187 τὰ μῆλα) | "flocks" | "flocks" | "sheep" (kept for ὄις, and for the fixed μῆλ’ ἁδινά "thronging sheep"; with ὄιές τε καὶ αἶγες in apposition, "sheep" would say the same word twice), "herds", "cattle" (βοῦς) |
| αὐλὴ ὑψηλὴ δέδμητο (9.184–185) | "a courtyard, high, had been built" | "a high yard had been built" | "fence", "enclosure", "pen"; ὑψηλός keeps the table's "high" |
| κατωρυχέεσσι λίθοισι (9.185) | "dug-in stones" | "stones sunk deep in the ground" | "quarried stones", "deep-set stones" (not what κατορύσσω says) |
| ὑψικόμοισι δρυσί (9.186) | "high-crowned oaks" | "high-crowned oaks" | "tall-leaved", "high-branched" |
| ἀνὴρ πελώριος (9.187) | "a man, monstrous" | "a monstrous man" | "giant", "huge", "prodigious" |
| σιτοφάγος (9.191) | "grain-eating" | "who eats grain" | "bread-eating" (σῖτος is grain, and covers bread), "corn-eating" |
| θαῦμα πελώριον (9.190) | "a marvel, monstrous" | "a monstrous marvel" | "prodigy", "wonder", "portent" |
| ῥίον ὑλῆεν (9.191, ῥίῳ ὑλήεντι) | "a wooded peak" | "a wooded peak" | "wooded headland", "forested crag"; keeps the table's ὑλήεις "wooded" |
| ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμείβετο νηλέι θυμῷ (whole-line reply-formula, 9.272; a first-person "So I spoke", with ἀμείβετο and no προσέειπεν) | "So I spoke, and he then at once answered me with pitiless heart:" | "So I spoke, and he answered me at once, with a pitiless heart:" | "addressed" (reserved for προσέειπε / προσέφη); folding it into the fixed ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμειβόμενος προσέειπεν ("So I said, and he answered me at once:"), which has a participle and a second verb; νηλεής keeps "pitiless" (as shipped at 8.507), θυμός plain "heart" |
| ἀλλὰ καὶ ὥς μιν ἔπεσσιν ἀμειβόμενος προσέειπον (9.258, first-person form of the table's μιν ἔπεσσιν ἀμειβόμενος/η προσέειπε(ν)) | "But even so, with words, answering him, I addressed him:" | "But even so I answered him, and spoke:" | "answered" alone (loses προσέειπον's "addressed"), "yet even then"; ἀλλὰ καὶ ὥς is "but even so", with ὥς the adverb |
| ποτιδόρπιον εἴη (9.234 ἵνα οἱ ποτιδόρπιον εἴη; 9.249 καί οἱ ποτιδόρπιον εἴη — the same two words twice; ποτί = πρός, δόρπον = the evening meal) | "so that for him it might be for supper" / "and for him for supper it might be" | "so that it would serve as his supper" / "and it would serve as his supper as well" | "dessert", "a relish", "his evening meal" in one place and "supper" in the other; kept identical both times |
| ἠλίβατος (of rock, 9.243 πέτρην ἠλίβατον; meaning unknown, 'steep, towering' the traditional guess) | "towering" | "towering" (+ note: meaning not known) | "sheer" (that would collide with the avoided "sheer destruction" for αἰπὺς ὄλεθρος and hides that the word is unknown), "steep" (reserved for αἰπύς), "high" (ὑψηλός), "immense" (reserved for ἀθέσφατος) |
| ὄβριμος (9.233 ὄβριμον ἄχθος, 9.241 θυρεὸν … ὄβριμον) | "mighty" | "mighty" | "huge", "heavy", "stout"; the same "mighty" that the table already has inside ὀβριμοπάτρη, and kept for both nouns so the reader hears the word twice |
| ἐυεργής (9.202 χρυσοῦ … ἐυεργέος; 9.279 ἐυεργέα νῆα) | "well-made" | "well-made" | "well-wrought" (kept for τετυγμένος, whose `i` is "well-wrought"), "well-worked", "finely made"; follows the shipped "well-made ship" at 8.567 (odyssey-038) |
| φέριστε (vocative address, 9.269) | "best of men" | "best of men" | "best one", "my good man", "noble sir" (reserved for ἀγαυός); follows the shipped "best of men" at 4.405 (odyssey-004) |
| ἐπιτιμήτωρ (9.270 Ζεὺς δ’ ἐπιτιμήτωρ ἱκετάων τε ξείνων τε; from ἐπιτιμάω 'assign a penalty, punish'; exact sense not certain) | "avenger" | "avenger" | "protector" (silently picks the other direction of the word), "punisher", "overseer", "guardian" (keep for φύλαξ) |
| ξείνιος Ζεύς (9.271) | "the guest-god" | "the god of guests" | "Zeus Xenios" (a transliteration), "Zeus of hospitality", "protector of strangers"; ξεῖνος itself stays "stranger" in the neighbouring genitives ξείνων, ξείνοισιν so that the repetition is heard |
| μεγάλην ἐπιειμένον ἀλκήν (9.214, ἐπιέννυμι perfect middle 'be clothed in', of the Cyclops) | "clothed in great might" | "clothed in great might" | "armed with great strength" (loses the garment image), "wearing great courage", "with great might"; ἀλκή is "might", kept apart from μένος "strength" (μένος ἡμιόνοιιν) and ἲς "force" |
| πρόγονοι · μέτασσαι · ἕρσαι (9.221–222, the three age-groups of the young animals in the pens; μέτασσαι is a rare word and ἕρσαι 'dews' is the ancient figure for the newest born) | "the earlier-born" · "the middle ones" · "the dews" | "the eldest" · "the middle ones" · "the youngest" (+ note: sense of the last two not certain) | "firstlings", "yearlings", "the lambs" (say more than the Greek does); "the dews" in `i` (keep the figure in `l` only) |
| θυρεός (9.240, ἐπέθηκε θυρεὸν μέγαν; the stone that closes the doorway; the same object is πέτρη at 9.243) | "door-stone" | "door-stone" | "shield" (the later sense of θυρεός), "boulder", "slab" (keep πέτρη "rock") |
| ἀκηράσιον (of wine, 9.205; 'unmixed', undiluted) | "unmixed" | "unmixed" | "pure", "unblended", "unwatered"; the word is a negative built on κεράννυμι 'mix', and the note ties it to the twenty measures of water at 9.209 |
| Οὖτις / Οὖτιν (9.366 ×2, 9.369; the false name, οὔ τις 'no one' written as a name) | "Nobody" | "Nobody" | "No-man", "Noman", "No one", "Nemo", "Outis" (a bare transliteration hides the pun; the note says it is οὔ τις) |
| δεῖπνον (9.311) · δόρπον (9.291, 9.344) · δειπνήσας (9.312) | "meal" · "supper" · "having eaten his meal" | "meal" · "supper" · "when he had eaten his meal" | "breakfast", "dinner" (each fixes a time of day the word does not itself give); δεῖπνον keeps "meal" and δόρπον the shipped "supper" (ποτιδόρπιον, 9.234), so that the two parallel lines 311 and 344 differ by exactly one word in English as in Greek |
| καλλίτριχα μῆλα (9.336) | "fair-coated flocks" | "fair-coated flocks" | "fair-haired" (reserved for ξανθός), "fair-fleeced" (the flocks are sheep and goats together), "well-haired"; built like the table's καλλίτριχες ἵπποι "fair-maned horses" |
| πίονα μῆλα (9.312, 9.315, 9.337) | "fat flocks" | "fat flocks" | "rich flocks", "fatted", "well-fed"; πίων is 'fat'; μῆλα keeps "flocks" from 9.184 |
| κλυτὰ μῆλα (9.308) | "famous flocks" | "famous flocks" | "renowned" (reserved for ἀγακλυτός), "glorious" (reserved for φαίδιμος); follows the table's κλυτός "famous" |
| μοχλός (9.332, and the stake throughout the blinding) | "stake" | "stake" | "bar", "lever", "club" (ῥόπαλον, the Cyclops' own club, 9.319, stays "club"), "spike", "pole"; the word is 'bar, lever', and "stake" is the sense its use as a sharpened post suggests; the same word is shipped as "levers" at 5.261 (μοχλοῖσιν, odyssey-024), where the bars launch a raft, and that stands as shipped — "lever" is avoided here only because this μοχλός is a sharpened post, not a bar used for prying |
| σχέτλιος (σχέτλια ἔργα 9.295; vocative σχέτλιε 9.351) | "cruel" (deeds) / "Cruel one" | "cruel deeds" / "Cruel one" | "dreadful", "terrible" (θεσπέσιος, δεινός and the like are taken), "wretch", "hard-hearted" |
| ἔπεσσι … μειλιχίοισι (9.363, with προσηύδων; a first-person speech introduction) | "with words … gentle ones" (προσηύδων "I spoke") | "with gentle words" (προσηύδων "I spoke to him") | "honeyed", "soothing", "soft", "mild words"; "addressed" (reserved for προσέειπε / προσέφη); προσαυδάω keeps "spoke", as in the table's ἔπεα πτερόεντα προσηύδα |
| ἀνδρόμεα κρέα (9.297, 9.347) | "human flesh" | "human flesh" | "man's flesh", "men's flesh", "the flesh of men" (ἀνδρόμεος is the adjective 'of a man, human'); kept identical at both occurrences |
| ἄκρητον γάλα (9.297) | "unmixed milk" | "unmixed milk" | "undiluted", "neat", "pure milk"; ἄκρητος is 'unmixed', the same English as the table's ἀκηράσιον |
| κισσύβιον (9.346) | "ivy-wood bowl" | "ivy-wood bowl" | "goblet" (reserved for ἄλεισον), "cup", "mixing-bowl" (κρητήρ); the note says the ivy origin is the traditional explanation |
| ῥόπαλον (9.319) | "club" | "club" | "staff", "cudgel", "bludgeon" |
| φρένες of the body (9.301, ὅθι φρένες ἧπαρ ἔχουσι) | "the midriff" | "the midriff" | "mind", "wits" (the sense φρένες has elsewhere, e.g. 9.362 and the table's κατὰ φρένα), "diaphragm", "lungs"; the note says the word is physical here |
| ὄργυια (9.325) | "a fathom" | "a fathom's length" | "six feet", "an arm-span" (the note gives the measure) |
| ἀνεκτῶς (9.350, οὐκέτ’ ἀνεκτῶς) | "no longer bearably" | "past all bearing" | "intolerably", "unbearably" (too flat), "beyond endurance" |
| κρατερὸς Πολύφημος (9.407, 9.446) | "strong Polyphemus" | "strong Polyphemus" | "mighty" (reserved for ὄβριμος), "stout", "powerful", "sturdy" |
| τοὺς δ’ αὖτ’ ἐξ ἄντρου προσέφη κρατερὸς Πολύφημος (9.407; reply-formula, name + epithet, with αὖτε) | "Them then in turn from the cave addressed strong Polyphemus:" | "Then strong Polyphemus spoke to them in turn from the cave:" | "answered" (reserved for ἠμείβετο); kept on the pattern of τὸν δ’ αὖτε προσέειπε |
| τὸν δ’ ἐπιμασσάμενος προσέφη κρατερὸς Πολύφημος (9.446; no αὖτε, since no one has spoken; ἐπιμασσάμενος is the aorist of ἐπιμαίομαι, the verb of ἐπεμαίετο 9.441) | "Him then, having felt over, addressed strong Polyphemus:" | "Then strong Polyphemus felt over him and spoke to him:" | "stroked", "patted" (ἐπιμαίομαι is 'feel over, touch' and is kept the same at 9.441 and 9.446), "answered" |
| οἱ δ’ ἀπαμειβόμενοι ἔπεα πτερόεντ’ ἀγόρευον (9.409; plural, with ἀγόρευον) | "And they, answering, winged words spoke:" | "And in answer they spoke winged words:" | "answered" as a finite verb (reserved for ἠμείβετο), "winged words … addressed" (προσέφη); ἀγόρευον is 'spoke', as προσηύδα in the table's ἔπεα πτερόεντα row |
| νήπιος (9.419 νήπιον, 9.442 νήπιος; literally 'not speaking', an infant, then 'foolish, blind to what is coming') | "foolish" | "foolish" (and "in his foolishness") | "childish" (the register rule), "simple", "naive", "infantile", "witless" |
| πέπον (vocative, 9.447 κριὲ πέπον; affectionate address; exact sense — 'ripe', 'soft', 'dear' — not known) | "good" (κριὲ πέπον "good ram") | "my good ram" (+ note: sense of πέπον not known) | "dear ram" (φίλος is "dear"), "gentle ram", "sweet ram" (each picks one guess) |
| ἄρσενες ὄιες (9.425) · ἀρνειός (9.432, 9.444) · κριός (9.447, 9.461) | "male sheep" · "ram" · "ram" | "male sheep" · "ram" · "ram" | "rams" for ἄρσενες ὄιες (keeps ἀρνειός and κριός apart from it), "wether", "tup"; ἀρνειός and κριός are the same animal and both are "ram" |
| ἰοδνεφές (9.426, εἶρος ἰοδνεφές; ἰον 'violet' + a second element, perhaps 'cloud' or 'dark', not certain) | "violet-dark" | "of a violet-dark colour" (+ note: second element uncertain) | "purple", "dark-violet wool" (changes the compound), "black" |
| λυγροῖς ἑτάροισι (9.454, of persons; the table's λυγρός "grievous" applied unchanged) | "grievous companions" | "grievous companions" | "wretched", "miserable", "baneful" (table); odd in English for people, kept so that λυγρός is heard the same in 3.132, 3.194 and here |
| ἀνὴρ κακός (9.453, of Odysseus, said by the Cyclops) | "a base man" | "a base man" | "worthless man" (kept for οὐτιδανός), "wicked man", "bad man", "evil man" (κακός is 'low, of no worth' here) |
| οὐτιδανός (9.460, οὐτιδανὸς … Οὖτις; 'worthless', a word that sounds like Οὖτις and may pun on it) | "worthless" | "worthless Nobody" | "good-for-nothing", "insignificant", "paltry" (οὐτιδανός is 'of no account', kept apart from the ἀνὴρ κακός "base man" above) |
| κερτομίοισι (9.474, with προσηύδων, the noun 'words' understood) | "with taunting ones" | "with taunts" | "with mocking words", "with cutting words", "with scornful words" (κερτόμιος is 'taunting, cutting') |
| ἀσπάσιος (9.466, ἀσπάσιοι … φάνημεν; adjective, 'welcome, glad'; the table's ἀσπασίως 'gladly' is the adverb) | "welcome" | "a welcome sight" | "gladly received", "a joy", "dear" (reserved for φίλος) |
| ἁλμυρὸν ὕδωρ (9.470) | "the salt water" | "the salt water" | "briny water", "the salty sea" (πολιὴ ἅλς is "the grey sea", a separate formula) |
| ἄναξ (9.440, 9.453 ἄνακτος; of Polyphemus as master of the flock) | "the lord" / "your lord's" | "the lord" / "your lord's" | "master", "king"; follows the table's ἄναξ "lord" (Ποσειδάωνι ἄνακτι) |
| ὥς τε περὶ ψυχῆς (9.423) | "as when it is for life" | "as one does when one's life is at stake" | "as for my soul" (ψυχή is 'life' here), "as if for their lives" |
| ταναύποδα (9.464, μῆλα ταναύποδα; 'stretched-foot', sense not certain) | "long-footed" | "long-legged" (+ note: sense not certain) | "slender-footed", "trim-footed", "long-shanked" (silently pick one guess) |
| πυριήκης (9.387, μοχλὸν πυριήκεα; πῦρ + ἀκή 'point', second half not fully certain) | "fire-pointed" | "fire-pointed" | "fire-hardened", "fire-tempered", "fire-sharpened" (would hide that ἀκ- is 'point') |
| ἀμύμων (9.414, μῆτις ἀμύμων; the table's "blameless" again, with the note that the real meaning is not known) | "blameless" | "blameless" | "flawless", "perfect", "matchless" |
| πτολιπόρθιος (of Odysseus; Ὀδυσσῆα πτολιπόρθιον 9.504, 9.530; the sack of Troy is ἔπερσεν "sacked", 1.2) | "Odysseus the city-sacking" | "Odysseus, sacker of cities" | "destroyer of cities", "city-waster", "city-sacker" (one word, hides the πτολι- 'city' + πέρθω 'sack' shape), "razer of towns" |
| Ζεὺς κελαινεφής (9.552, Ζηνὶ κελαινεφέι) | "Zeus dark-clouded" | "Zeus of the dark clouds" | "storm-cloud Zeus", "black-clouded", "Zeus of the thunderclouds"; kept apart from νεφεληγερέτα "cloud-gatherer" |
| ὣς ἐφάμην, ὁ δέ μ’ οἰμώξας ἠμείβετο μύθῳ· (whole line, 9.506; a third reply-formula built on ἠμείβετο) | "So I spoke, and he, groaning, answered me with a word:" | "So I spoke, and he groaned and answered me:" | "So I said" (the i of the προσέειπεν formula; the ἀμείβετο formula keeps "So I spoke", as the row for 9.272), "answered me with a groan", folding it into the already-fixed ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμειβόμενος προσέειπεν (that is ἀμειβόμενος προσέειπεν, not ἠμείβετο μύθῳ) |
| κλῦθι, Ποσείδαον γαιήοχε κυανοχαῖτα (whole line, 9.528) | "Hear, Poseidon earth-holder, dark-haired one," | "Hear me, Poseidon, earth-holder, dark-haired one;" | "Hear my prayer", "blue-maned", "dark-maned", "Poseidon, holder of the earth" (the house γαιήοχος "earth-holder", κυανοχαίτης "dark-haired") |
| ὣς ἔφατ’ εὐχόμενος, τοῦ δ’ ἔκλυε κυανοχαίτης (whole line, 9.536; first half is the table's "So he spoke, praying," / "So he prayed,") | "So he spoke, praying, and him heard the dark-haired one." | "So he prayed, and the dark-haired god heard him." | "the blue-haired god", "the dark-maned one" |
| ὣς φάσαν (9.500; plural of ὣς φάτο) | "So they spoke" | "So they spoke" | "Thus they said", "So they said" (keep one form, as for ὣς φάτο) |
| ἀνάλκις (9.475, ἀνάλκιδος ἀνδρός; ἄλκη 'defensive strength, might', 9.514 μεγάλην ἐπιειμένον ἀλκήν) | "without might" | "without might" | "cowardly" (an Aegisthus-word already shipped at 11.309), "weakling" (shipped at 17.333), "unwarlike"; ἄλκη keeps "might", ἄλκιμος stays "strong, valiant" as shipped |
| θέσφατα (9.507, παλαίφατα θέσφαθ’; plural noun) | "god-declared things" (with παλαίφατα "long-ago-spoken") | "prophecies" (+ "spoken long ago") | "oracles", "decrees", "fate"; follows the table's θέσφατόν ἐστι "it is god-declared / it is decreed" for the root |
| ἀπέλεθρος (9.538, ἶν’ ἀπέλεθρον) | "measureless" | "measureless" | "immense" (reserved for ἀθέσφατος), "boundless" (reserved for ἀπείρων), "vast"; the word may be built on πέλεθρον, a measure of length, but the formation is not certain |
| ἀρνειός (9.550) | "ram" | "a ram" | "male lamb", "wether" |
| ἐυκνήμιδες ἑταῖροι (9.550) | "well-greaved companions" | "well-greaved companions" | "well-armoured", "bronze-greaved"; extends the table's ἐυκνήμιδες Ἀχαιοί "well-greaved Achaeans" to the companions |
| ἐκλύσθη δὲ θάλασσα κατερχομένης ὑπὸ πέτρης· (whole line, 9.484 = 9.541) | "and the sea was washed up in a surge beneath the descending rock;" | "and the sea surged up beneath the falling rock;" | "the sea heaved", "the sea boiled up" |
| τυτθόν, ἐδεύησεν δ’ οἰήιον ἄκρον ἱκέσθαι (9.483 = 9.540) | "a little way, and it fell short of reaching the tip of the steering-oar" | "a little way … and it fell short of reaching the tip of the steering-oar" | "missed the rudder by a hair", "the end of the tiller" (οἰήιον is the handle of the steering-oar; it is not a 'rudder') |
| θέμωσε δὲ χέρσον ἱκέσθαι (9.486, 9.542; sense of θεμόω not known) | "and forced it to reach dry land" | "and forced it to reach dry land" (+ note: sense of θέμωσε not known; 'forced, drove' from context) | "and drove it to the shore", "and made it reach" (each silently picks a sense) |
| ἄκικυς (9.515; derivation not known) | "feeble" | "feeble" (+ note: derivation not known) | "weak" (reserved for ἠπεδανός / ἀνάλκις), "powerless" |
| ἐρίηρες ἑταῖροι (9.555) | "trusty companions" | "trusty companions" | already the table's row; no change |
| ἀλλ’ ὅτε δὴ δὶς τόσσον ἅλα πρήσσοντες ἀπῆμεν (9.491) | "But when twice so much of the salt-sea making-our-way we were away," | "But when we had gone twice as far over the sea," | "when we were twice as far out", "twice the distance" |
| Αἴολος Ἱπποτάδης / Ἱπποτάδαο (10.2, 10.36; patronymic) | "Aeolus, Hippotes' son" | "Aeolus, son of Hippotes" | built like Ἀτρεΐδῃ Ἀγαμέμνονι |
| ἀσκός (10.19, 10.47, 10.45) | "skin" | "skin" | follows the shipped "skin" (5.265, 9.196, 9.212); κώρυκος stays "leather bag" |
| βυκτάων ἀνέμων (10.20) | "the roaring winds" | "the roaring winds" | sense uncertain (note says so) |
| ταμίης ἀνέμων (10.21) | "steward of the winds" | "steward of the winds" | masculine ταμίης, distinct from αἰδοίη ταμίη "housekeeper" |
| πατρὶς ἄρουρα (10.29) | "the fatherland's soil" | "our native soil" | follows the shipped 4.407 for the whole phrase |
| γαίης ἄπο πατρίδος (10.49) | "away from their fatherland" | "away from their fatherland" | πατρίς + γαῖα = "fatherland" as at the πατρίδα γαῖαν row |
| ἀφραδίῃσιν (10.27) | "follies" | "folly" | follows 9.361 "folly"; echoes 1.7 ἀτασθαλίῃσιν |
| κεδνός (10.8, μητέρι κεδνῇ) | "trusty" | "trusty" | follows shipped κεδνῇ ἀλόχῳ "trusty wife" (4.432) |
| ἐνδυκέως (10.65) | "kindly" | "kindly" | follows shipped 7.255 (odyssey-032) |
| ἀχνύμενος κῆρ (10.67) | "grieving in heart" | "grieving in heart" | follows shipped ἀχνύμενος "grieving"; ἀκαχήμενος ἦτορ stays "grieved at heart" |
| ἄασαν (10.68) | "blinded me" | "blinded me" | follows the table's μέγ’ ἀάσθη "greatly blinded" |
| ὣς ἔφασαν (10.46) | "So they spoke" | "So they spoke" | plural of ὣς φάτο, as ὣς φάσαν (table) |
| ὣς ἐφάμην μαλακοῖσι καθαπτόμενος ἐπέεσσιν (10.70, whole-line formula, first-person) | "So I spoke, with soft words accosting them," | "So I spoke, addressing them directly with soft words," | built on the table's καθαπτόμενος row; μαλακός = "soft" |
| πατὴρ δ’ ἠμείβετο μύθῳ (10.71) | "but the father answered with a word:" | "but their father answered:" | μύθῳ as in the table's ὣς ἐφάμην … ἠμείβετο μύθῳ row ("with a word" in `l`) |
| ἔρρε / ἔρρ’ (10.72, 10.75; imperative) | "Begone" | "Begone" | same English both times |
| ἐλέγχιστε ζωόντων (10.72) | "most shameful of the living" | "you most shameful of the living" | |
| ἀποπέμπω (10.65 impf., 10.73 inf.) / κομιζέμεν (10.73) | "send off" / "care for" | "send off" / "care for" | κομίζω follows shipped "cared for" (5.451) |
| ἀπεχθάνομαι (10.74 ἀπέχθηται, 10.75 ἀπεχθόμενος) | "become hateful" / "being hateful" | "become hateful" / "hateful" | same word both times, to keep the echo |
| πυρπολέοντας (10.30) | "men tending fires" | "men tending fires" | |
| πόδα νηὸς ἐνώμων (10.32) | "the foot of the ship I was handling" | "the ship's sheet" | note says πούς = sail-rope |
| κνισῆεν δῶμα (10.10) | "the fat-scented house" | "the house, rich with the smell of cooking fat" | |
| ὀνείατα μυρία (10.9) | "dainties numberless" | "countless delicacies" | |
| ἐννεώροιο βοός (10.19) | "a nine-year-old ox" | "a nine-year-old ox" | |
| ὡς ὅδε πᾶσι φίλος καὶ τίμιός ἐστιν (10.38) | "dear to all, and honoured" | "dear and honoured" | τίμιος = "honoured" |
| κενεὰς σὺν χεῖρας ἔχοντες (10.42) | "empty hands along with us having" | "with empty hands" | |
| λιγέως / λίγ’ (10.201, 10.254; adverb of λιγύς, cf. the table's κήρυκες λιγύφθογγοι) | "clearly" | "with clear voices" / "in a clear voice" | "shrilly", "loudly" (turned down for the heralds), "clear-toned" |
| ἀπείριτος (10.195, πόντος ἀπείριτος) | "limitless" | "limitless" | "boundless" (already shipped for ἀπείρων (ἀπείρονα γαῖαν, 1.98; πόντον ἀπείρονα) and for ἄσπετα κρέα, 10.183–184; a third use would merge three Greek words), "immense" (ἀθέσφατος), "measureless" (ἀπέλεθρος) |
| καλλιπλόκαμος (10.220, θεᾶς καλλιπλοκάμοιο) | "fair-plaited" | "fair-plaited" | "fine-plaited" (reserved for ἐυπλόκαμος), "fair-tressed" (reserved for ἐυπλοκαμῖδες), "fair-haired" (ξανθός), "well-braided" |
| αἰνὰ πέλωρα (10.219) | "fearsome monsters" | "fearsome monsters" | "dread" (reserved for δεινός, as in δεινὸν πέλωρ), "terrible", "dreadful" |
| κρατερώνυχες (of wolves and lions, 10.216–218; the table has κρατερώνυχας "strong-hoofed" of mules, 6.253) | "strong-clawed" | "strong-clawed" | "strong-hoofed" (for mules only), "sharp-clawed"; same compound, ὄνυξ read as claw or hoof by the animal. Open: the existing row lists "strong-clawed" among its avoided renderings, so the two rows clash until the owner amends it |
| κλισμός (10.233, κατὰ κλισμούς τε θρόνους τε; the half-line is shipped at 1.145 and 3.389) | "seats" ("along the seats and the chairs") | "seats" ("along the seats and the chairs") | "easy-chairs", "easy chairs", "couches", "reclining-seats"; follows the shipped "seat(s)" (1.132 "inlaid seat", 1.145, 3.389); θρόνος keeps the table's "chair" (the lone κλισμῷ of 4.136 shipped as "chair") |
| χλωρὸν μέλι (10.234) | "yellow honey" | "yellow honey" | "green honey", "fresh honey", "pale honey" |
| Πραμνεῖος οἶνος (10.235) | "Pramnian wine" | "Pramnian wine" (+ note: origin of the name not known) | "wine of Pramnos", "red wine" |
| ἄκυλος (10.242; the ilex-acorn, LSJ) | "ilex-acorn" | "ilex-acorn" | "acorn" alone (βάλανος is "mast" in the same line) |
| ἀδευκής (10.245, ἀδευκέα πότμον; old, sense uncertain) | "bitter" | "bitter" (+ note: sense uncertain) | "grievous" (reserved for λυγρός), "pitiless" (νηλεής), "cruel" |
| περίσκεπτος (10.211 = 10.253, χώρῳ) | "with a view all round" | "with a view all around" (+ note: either 'seen from all sides' or 'commanding a view') | "conspicuous", "with a wide prospect" (picks one sense) |
| ἀγάομαι (10.249, ἀγασσάμεθ’; the table has ἀγάσασθαι "resented", 8.565) | "in wonder" | "were amazed at" | "resented" (the other shade, kept for 8.565 only), "admired" |
| διοτρεφές (vocative, 10.266; the table has διοτρεφέες βασιλῆες "Zeus-nurtured kings") | "Zeus-nurtured one" | "Zeus-nurtured one" | "Zeus-born" (reserved for διογενής), "king" |
| ὀπὶ καλῇ (10.220, ἀειδούσης ὀπὶ καλῇ) | "with a beautiful voice" | "in a beautiful voice" | "with a fine voice" (καλός is "fine" elsewhere, but the same words are shipped at 5.61 as "beautiful voice", and a repeated half-line keeps its English) |
| ὀρέστεροι (10.212) | "of the mountains" | "mountain" | "mountain-bred", "wild" |
| ὄπασσα (10.204) | "I gave" | "gave each group a leader" | "assigned", "appointed" |
| δρυμά (10.196, 10.251; shipped at 10.148, διὰ δρυμὰ πυκνὰ καὶ ὕλην) | "coppices" | "coppices" | "thickets", "copses", "undergrowth"; the half-line διὰ δρυμὰ πυκνὰ καὶ ὕλην keeps its shipped English "through thick coppices and woodland" |
| θᾶσσον (comparative adverb of ταχύς, in exhortations; 10.192, 10.228, 10.268) | "more quickly" | "quickly" | "faster", "quicker"; "sooner" / "the sooner" is shipped only where the sense is 'so that … sooner' (odyssey-007 line 306, odyssey-031 line 151, and the `i` of 10.31 in odyssey-045); for the imperative-type use the shipped practice is `l` "more quickly" and `i` "quickly" (10.44 and 10.72, odyssey-045) |
| πολυφάρμακος (of Circe, 10.276, Κίρκης πολυφαρμάκου) | "of many drugs" | "skilled in many drugs" | "of many potions", "of many spells", "the enchantress"; φάρμακον is "drug" throughout |
| φάρμακον (10.287, 10.302, 10.317, 10.326–327) | "drug" / "drugs" | "drug" / "drugs" | "potion", "charm", "herb", "poison"; follows the shipped "drugs" for the plural |
| ὑπηνήτης (10.279, πρῶτον ὑπηνήτῃ) | "first-bearded" | "with his first beard" | "downy-cheeked", "bearded youth" |
| χαριεστάτη ἥβη (10.279) | "the most graceful youth" | "the age when youth is most graceful" | "loveliest", "most charming"; ἥβη keeps the table's "youth" |
| ἄκρις (10.281, δι’ ἄκριας) | "hilltops" | "hilltops" | "peaks", "heights", "crags" |
| ἔρχαται (10.283, perfect passive of εἴργω) | "are penned" | "are shut up" | "are kept", "dwell", "are confined" |
| κευθμών (10.283, πυκινοὺς κευθμῶνας) | "solid hiding-places" | "their solid sties" | "lairs" (kept for θαλάμη, the octopus's lair, and for εὐνή of the lion), "close-built pens"; πυκινός keeps the table's "solid" |
| λύομαι (future middle part., 10.284) | "to release" | "to free" | "to ransom", "to rescue" (ἐρρύσατο "rescue"), "to loose" |
| ὀλοφώια δήνεα (10.289) | "baneful designs" | "baneful designs" | "baneful wiles" / "baneful tricks" (the table's substantival ὀλοφώια), "plots", "deadly arts"; δήνεα is "designs, counsels" |
| κυκεών (10.290, 10.316) | "stirred drink" | "mixed drink" | "potion", "brew", "kykeon" (transliteration), "mixture" alone (does not say it is drunk) |
| σῖτος (10.290, "βαλέει δ’ ἐν φάρμακα σίτῳ") | "food" | "food" | "bread" (shipped for σῖτον at 10.371), "grain", "meal" |
| ἐρύσας (of the plant, 10.303) | "having drawn" | "pulled" | "uprooted", "plucked"; same verb as ἐρυσσάμενος "drawing" of the sword, kept apart only by English tense |
| φύσις (10.303, φύσιν αὐτοῦ) | "its nature" | "its nature" (+ note: 'growth, kind') | "its properties", "how it grew" |
| μῶλυ (10.305) | "moly" | "moly" (+ note: meaning of the word not known; plant not identified) | "the herb", "an antidote", "milk-flower" |
| χαλεπὸν ὀρύσσειν (10.305; a task, not a person) | "hard" | "hard" | "harsh" (reserved for χαλεπός of persons and peoples, 8.575), "difficult", "grievous" |
| ἀνήνωρ / κακὸν καὶ ἀνήνορα (10.301, 10.341) | "base and unmanned" | "base and unmanned" | "cowardly" (ἀνάλκις), "weak", "a worthless unmanned wretch"; κακόν keeps the table's "base" (ἀνὴρ κακός), ἀπογυμνωθέντα / γυμνωθέντα is "stripped" |
| εὐνή (10.297, 10.334–335, 10.340–347; the intimate bed) | "bed" | "bed" | "couch" (kept for the guest-bed at 7.342, 7.347), "marriage-bed"; ἐπιβαίνω εὐνῆς is `l` "set foot upon … bed", `i` "mount … bed" |
| εὐνηθῆναι (10.296) | "to lie with her" | "to lie with her" | "to be put to bed", "to go to bed" |
| ἐπαῖξαι / ἐπήιξα (10.295, 10.322) | "rush at" / "rushed at" | "rush at" / "rushed at" | "leap upon", "charge" |
| ἄορ (10.321, 10.333) | "sword" | "sword" | the table's ξίφος ὀξύ "sharp sword" is kept for ξίφος; ἄορ is a second word for the same weapon |
| ἦ σύ γ’ Ὀδυσσεύς ἐσσι πολύτροπος (10.330) | "Truly you are Odysseus, the many-turning" | "Surely you are Odysseus of many shifts" | "Can you be Odysseus" (a question the Greek does not ask) |
| φάσκεν ἐλεύσεσθαι (10.331) | "kept saying would come" | "always told me would come" | "promised", "prophesied" |
| θαῦμά μ’ ἔχει (10.326) | "a wonder holds me" | "I am amazed" | "I marvel", "I wonder" alone |
| ἀκήλητος (10.329) | "not-to-be-charmed" | "cannot be charmed" | "unbewitched", "unyielding"; θέλγω is "enchant" |
| θέλγω / θέλξαι / ἐθέλχθης (10.291, 10.318, 10.326) | "enchant" / "enchanted" | "enchant" / "enchanted" | "charm", "bewitch", "spell" (keep "charm" for the ἀκήλητος root κηλέω) |
| ἀπώμνυεν (10.345) | "swore" | "swore" | "swore off", "forswore", "took the oath" |
| ὣς ἄρα φωνήσας πόρε (masc., 10.302) | "So then having spoken, gave" | "So he spoke, and … gave" | joins the table's ὣς ἄρα φωνήσας ἀπέβη row |
| ἔν τ’ ἄρα μοι φῦ χειρί, ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε (10.280; first-person object) | "and clasped me by the hand, and spoke a word, and called me by name:" | "took my hand, and spoke, calling me by name:" | "grasped my hand" alone (drops the tmesis); same shape as the Antinous row |
| ῥάβδῳ πεπληγυῖα ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν (10.319) | "striking … with her wand, she spoke a word and called me by name:" | "she struck me with her wand and spoke, calling me by name:" | "struck … with a wand" (house "wand" for ῥάβδος) |
| πέλω-root ἀμφίπολοι: τέσσαρες … δρήστειραι (10.349) | "serving-women" | "the women who do her work" | "maids" (δμῳαί), "handmaids" (kept as shipped in the identical 2.136 unit), "workers" |
| κρηνέων · ἀλσέων (10.350) | "springs" · "groves" | "springs" · "groves" | "fountains", "woods" |
| ῥήγεα πορφύρεα (10.352–353) | "fine blankets, purple" | "fine purple blankets" | "rugs" (blankets, as shipped in odyssey-016 and odyssey-032 for ῥήγεα), "carpets" (τάπητες) |
| λῖτα (10.353) | "linen cloth" | "a linen cloth" | "linens", "sheets" |
| κάνεια (10.355) | "baskets" | "baskets" | "trays", "platters" |
| κύπελλα (10.357) | "cups" | "cups" | "beakers", "goblets" (reserved for ἄλεισον) |
| ἡ μὲν … ἡ δ’ ἑτέρη … ἡ δὲ τρίτη … ἡ δὲ τετάρτη (10.352–358) | "of them one … and the second … and the third … and the fourth" | "one of them … the second … the third … the fourth" | "the other" for ἑτέρη (the Greek counts) |
| ἠνοπι χαλκῷ (10.360; ἤνοψ sense uncertain) | "bright bronze" | "bright bronze" (+ note: ἤνοψ not known for certain; 'gleaming, flashing' traditional) | "gleaming" (reserved for γλαυκῶπις), "flashing" (turned down for αἴθων), "shining" (φαεινός), "glittering" |
| θυμῆρες κεράσασα (10.362) | "mixing it to the heart’s pleasing" | "mixing it to suit my heart" | "to a pleasant warmth" (adds a quality), "comfortably" |
| θυμοφθόρος (10.363, κάματον θυμοφθόρον) | "heart-destroying" | "heart-destroying" | "heart-wasting", "life-sapping"; follows the "heart-destroying drugs" shipped in odyssey-008 |
| κάματος (10.363) | "weariness" | "weariness" | "toil", "fatigue" |
| ἐσθέμεναι ἐκέλευεν (10.373) | "to eat she bade" | "she urged me to eat" | "ordered", "commanded" |
| ἀλλοφρονέων (10.374) | "thinking elsewhere" | "with my thoughts elsewhere" | "absent-minded", "otherwise-minded" (“-minded” reserved for the -φρων epithets) |
| κακὰ ὄσσετο θυμός (10.374) | "evils my heart foresaw" | "my heart foresaw evils" | "boded", "had a presentiment of", "my spirit saw" (θυμός stays "heart") |
| κακὰ φρονέουσα ἐνὶ θυμῷ (10.317) | "evil thinking in her heart" | "meaning evil in her heart" | "plotting evil", "with evil thoughts"; keeps the pattern of φίλα φρονέουσ’ "kindly thinking" |
| ἔρχεο νῦν συφεόνδε (10.320) | "Go now to the pigsty" | "Go now to the pigsty" | "sty" alone; the shipped 047 "pigsties" for συφεοῖσι is plural |
| ἦ τοὺς λυσόμενος δεῦρ’ ἔρχεαι (10.284) | "Is it, them to release, that here you come?" | "Is it to free them that you have come here?" | "Have you come to ransom them?" |
|---|---|---|---|
| ἆ δειλοί (10.431, vocative) | "Oh, miserable ones," | "Oh, you miserable men," | "Ah" / "Ah me" (reserved for ὢ πόποι), "cowards" (δειλός is "miserable", as in the table's ὤ μοι ἐγὼ δειλός), "wretched" (reserved for δύστηνος) |
| δαιμόνιε (vocative, 10.472, δαιμόνι’) | "Strange man" | "Strange man" (+ note: force of the address uncertain; 'strange one, driven by something beyond himself') | "my good man", "my friend" (silently picks the gentle sense), "possessed one" (silently picks the literal sense) |
| θαλερὸν δάκρυ · θαλερὸν γόον (10.409, 10.457) | "an abundant tear" · "an abundant lament" | "abundant tears" · "your abundant lament" | "blooming" (reserved for θαλερὸς γάμος), "swollen", "bitter", "flowing"; θαλερός is kept "abundant" as in θαλερὴ ἀλοιφή |
| τανύηκες ἄορ (10.439) | "long-pointed sword" | "long-pointed sword" (+ note: ἀκ- 'point', as in πυριήκης) | "long-edged", "long-bladed", "far-reaching" |
| ἔκπαγλος ἐνιπή (10.448, ἐμὴν ἔκπαγλον ἐνιπήν) | "my terrifying rebuke" | "my terrifying rebuke" | "terrible" (taken by σχέτλιος, θεσπέσιος), "dread" (reserved for δεινός), "violent", "fearsome" (reserved for αἰνὰ πέλωρα); ἐνιπή is "rebuke" |
| φάρμακον οὐλόμενον (10.394) | "the ruinous drug" | "the ruinous drug" | "deadly" (reserved for ὀλοός), "baneful" (reserved for ὀλοφώια), "accursed", "destructive" |
| ἱμερόεις γόος (10.398) | "a lament full of longing" | "a lament full of longing" | "sweet lament", "desirable", "lovely" (ἱμερόεις is ἵμερος 'longing' + -όεις 'full of') |
| μέσσαυλον (10.435) | "mid-yard" | "farmyard" | "inner court", "yard in the midst", "stockyard" |
| ἄγραυλοι πόριες · βοῦς ἀγελαῖαι (10.410) | "field-dwelling calves" · "cows of the herd" | "calves that live in the fields" · "cows of the herd" | "heifers", "wild", "pasture-keeping", "herd-cattle" |
| ἀσκελέες καὶ ἄθυμοι (10.463) | "withered and without-heart" | "withered and disheartened" | "dried-up and spiritless" (spirit is reserved for θυμὸς ἀγήνωρ), "shrivelled", "lean"; ἄθυμος keeps θυμός "heart" |
| ἀνάρσιοι ἄνδρες (10.459) | "hostile men" | "hostile men" | "unfriendly", "enemy", "ill-fitting" |
| τελεσφόρον εἰς ἐνιαυτόν (10.467) | "for a completion-bearing year" | "for a full year" | "for a year of completion" (unidiomatic), "the whole year round", "a year that brought fruit" |
| σιάλοισιν ἐοικότας ἐννεώροισιν (10.390) | "like to fat hogs, nine-year-olds" | "looking like fat nine-year-old hogs" | "swine" (kept for σῦς, 10.433), "boars", "well-fed pigs"; σίαλος is a fattened hog |
| ἔν … ἔφυν χερσίν (10.397, plural; the singular idiom is the table's ἔν τ’ ἄρα οἱ φῦ χειρί) | "took-firm-hold in my hands" | "took firm hold of my hands" | "clasped", "embraced" (drop the tmesis idiom ἔν … φῦ, 'grew into') |
| δακρυόεντες ἔχυντο (10.415) | "tearful, poured themselves forth" | "came streaming forward in tears" | "embraced me weeping", "fell upon me" (the Greek does not say where they poured) |
| ἐναίσιμος (of a man, 10.383) | "one with a sense of what is fitting" | "with any sense of what is fitting" | "righteous", "decent", "reasonable"; keeps the αἶσα family of the table's αἴσιμα · ἐναίσιμον |
| θρασύς (of Odysseus, 10.436, ὁ θρασὺς Ὀδυσσεύς) | "the bold Odysseus" | "bold Odysseus" | "rash", "reckless", "audacious" (each picks the hostile sense the speaker intends) |
| χλαῖναι οὖλαι (10.451) | "thick cloaks" | "thick cloaks" | "woolly", "fleecy", "soft cloaks" |
| ἐσάντα (10.453) | "face to face" | "face to face" | "opposite", "in front of" |
| ὣς φάμενοι (10.446) | "So saying," | "So saying," | "So they spoke" (kept for ὣς φάν / ὣς ἔφαν) |
| ἀλλ’ ἄγετ’ ἐσθίετε βρώμην καὶ πίνετε οἶνον (10.460) | "But come, eat food and drink wine," | "But come, eat food and drink wine," | "feed", "partake of", "eat your fill" |
| ἐπηετανὸν γὰρ ἔχουσιν (10.427; table row ἐπηετανός) | "for never-failing they have it" | "for they have a never-failing supply" | "plenty", "abundantly" |
| μαλακοῖς ἐπέεσσι (10.422; 10.70 shipped) | "soft words" | "soft words" | "gentle words" (reserved for μειλιχίοις ἐπέεσσιν, 10.442), "kind words" |
| τῷ οἱ ἀποπλήξας κεφαλὴν οὖδάσδε πελάσσαι (10.440) | "with it his head, having struck it off, to bring to the ground" | "strike off his head with it and bring it down to the ground" | "cut off", "sever" (ἀποπλήσσω is 'strike off'); πελάσσαι keeps "bring near / bring" as in πελάσσατε (404) |
| πηῷ (10.441; follows the table's πηός) | "kinsman-by-marriage" | "a relative by marriage" | "kinsman" alone, "brother-in-law" (a guess the Greek does not give) |
| ψυχή (of the dead; 10.492, 530, 560, 565) | "soul" | "soul" | "ghost", "shade" (keep for σκιαί / εἴδωλον), "spirit" (reserved for θυμὸς ἀγήνωρ); at 10.560 the same word is the soul that goes down to Hades |
| σκιαί (10.495, of the dead other than Tiresias) | "shadows" | "shadows" | "shades" |
| ἐπαινή (of Persephone, 10.491, 534, 564; ἐπαινῆς / ἐπαινῇ Περσεφονείης) | "grim" | "grim" (+ note: traditionally "dread, awful"; exact sense not certain) | "dread" (reserved for δεινός, as in δεινὴ θεός and δεινὸν πέλωρ), "terrible", "awful", "fearsome" (reserved for αἰνὰ πέλωρα), "revered" |
| ἀμενηνὰ κάρηνα (10.521, 536; of the dead) | "the powerless heads" | "the powerless heads" | "feeble heads" (ἄκικυς is "feeble"), "weak", "strengthless" in `i` |
| εὐρώεις (of Hades' house, 10.512) | "mouldy" | "dank" | "dark", "gloomy", "broad" |
| ἀκτὴ λάχεια (10.509) | "a low-lying shore" | "a low-lying shore" (+ note: sense uncertain) | "flat", "level", "wooded"; follows the table's νῆσος λάχεια |
| ὠλεσίκαρπος (of willows, 10.510) | "that lose their fruit" | "that lose their fruit" | "fruit-destroying", "barren", "that shed unripe fruit" (adds a claim) |
| βαθυδίνης (of Oceanus, 10.511) | "deep-eddying" | "deep-eddying" | "deep-flowing", "deep-swirling" |
| ἐρίδουπος (of rivers, 10.515) | "loud-echoing" | "loud-echoing" | "loud-roaring", "thundering"; extends the table's ἐριδούπῳ "loud-echoing" (αἴθουσα) to a second noun |
| ἀπορρώξ (10.514, of Cocytus) | "offshoot" | "offshoot" | "tributary", "branch" |
| μελίκρητον (10.519) | "honey-mixture" | "a honeyed mixture" (+ note: traditionally honey with milk) | "mead", "honey-milk" as if certain |
| χοή (10.518) | "libation" | "libation" | "drink-offering", "offering" |
| ἄλφιτα λευκά (10.520) | "white barley-meal" | "white barley-meal" | "white flour", "groats" |
| πυγούσιον (10.517) | "a cubit's length" | "a cubit long" (+ note: πυγών, forearm) | "a foot", "a yard" |
| κλυτὰ ἔθνεα νεκρῶν (10.526) | "the famous tribes of the dead" | "the famous tribes of the dead" | "renowned", "glorious hosts" |
| ὄιν ἀρνειὸν … θῆλύν τε μέλαιναν (10.527, 572) | "a sheep, a ram, … and a female, black" | "a ram and a black ewe" | different English at 572 (kept identical at both occurrences) |
| χρυσόθρονος Ἠώς (10.541) | "golden-throned Dawn" | "golden-throned Dawn" (+ note: the old θρόνα "flowers" alternative) | "rosy-fingered" (the separate ἠριγένεια ῥοδοδάκτυλος formula); extends the table's χρυσόθρονος |
| ἀργύφεον φᾶρος (10.543) | "silver-white robe" | "silver-white robe" | follows the wording shipped in odyssey-024 (unit at line 230) |
| πνοιὴ Βορέαο (10.507) | "the breath of the North Wind" | "the breath of the North Wind" | "blast" (reserved for ἄελλα), "wind" alone |
| ἀωτεῖτε (10.548; rare verb, formation not certain) | "slumber" (with γλυκὺν ὕπνον "sweet sleep") | "slumbering in sweet sleep" (+ note: formation not certain) | "snore", "lie abed" |
| ἀρηρώς (φρεσὶν ᾗσιν ἀρηρώς, 10.553) | "sound" | "sound in his own wits" | "fitted", "settled", "steady" |
| οἰνοβαρείων (10.555) | "heavy with wine" | "heavy with wine" | "drunk", "sodden" (both overstate or flatten βαρύς "heavy") |
| ἀστράγαλοι (of the neck, 10.560) | "vertebrae" | "vertebrae" (+ note: also "knucklebone") | "joints", "neck-bones" |
| ἀπήμων (of persons, 10.551; cf. οὖρος ἀπήμων "harmless" of a wind) | "unharmed" | "unharmed" | "safe", "without loss" (drop πῆμα "woe") |
| ὣς ἐφάμην (plain, 10.550, 566; the two whole-line formulas ὣς ἐφάμην, ἡ δ’ αὐτίκ’ ἀμείβετο δῖα θεάων at 487 and 503 keep their shipped `i` "So I said") | "So I spoke" | "So I spoke" | "So I said" in a plain line (every shipped plain ὣς ἐφάμην, e.g. odyssey-044, -047, -049, has "So I spoke"; "So I said" belongs only to the fixed reply-formulas) |
| ὣς ἔφατ’, αὐτίκα δὲ χρυσόθρονος ἤλυθεν Ἠώς (whole line, 10.541) | "So she spoke, and at once golden-throned Dawn came." | "So she spoke, and golden-throned Dawn came at once." | "rose", "dawn broke" (keep ἔρχομαι 'come'), "rosy-fingered" (the separate ἠριγένεια ῥοδοδάκτυλος formula) |
| ἐρχομένοισι δὲ τοῖσιν ἐγὼ μετὰ μῦθον ἔειπον (whole-line first-person speech introduction, 10.561) | "And to them as they went, among them a speech I spoke:" | "And as they went on their way, I spoke among them:" | "addressed" (reserved for προσέειπε / προσέφη), "answered" (reserved for ἠμείβετο), "told them" (drops μετά 'among'); μετὰ … ἔειπον keeps the table's "spoke among" |
| ἴκμενον οὖρον … πλησίστιον (11.7) | "a favouring wind, sail-filling" | "a favouring wind that filled the sail" (+ note: sense of ἴκμενος uncertain, 'favouring' the traditional gloss) | "fair wind" (reserved for οὖρος ἀπήμων τε λιαρός τε, 'a fair wind, harmless and warm'), "following wind", "swelling" |
| ἐσθλὸς ἑταῖρος (of the wind, 11.7) | "a good companion" | "a good companion" | "a faithful friend", "trusty comrade" |
| φαέθων ἠέλιος (11.16) | "the shining sun" | "the shining sun" | "radiant", "blazing" (reserved for αἰθόμενος words), "bright" (reserved for φαεσίμβροτος 'who gives light to mortals'); follows the shipped "shining sun" for the same words (odyssey-026), even though the table keeps "shining" for φαεινός — the two are told apart by the noun |
| βαθύρροος Ὠκεανός (11.13) | "deep-flowing Oceanus" | "deep-flowing Oceanus" | "deep-streaming", "deep-running", "of the deep current"; follows the table's βαθυδίνης 'deep-eddying' in using 'deep' for βαθύς |
| ἀστερόεις οὐρανός (11.17) | "starry sky" | "the starry sky" | "star-spangled", "starlit sky", "starry heaven"; follows the shipped εἰς οὐρανὸν ἀστερόεντα "to the starry sky" (odyssey-044) |
| νὺξ ὀλοή (11.19) | "deadly night" | "deadly night" | "baneful", "ruinous", "destructive night"; follows the table's μοῖρ’ ὀλοή 'the deadly fate' and ὀλοοὶ ἄνεμοι 'deadly winds' |
| δειλοὶ βροτοί (11.19) | "miserable mortals" | "miserable mortals" | "wretched mortals" (reserved for δύστηνος), "poor mortals"; follows the table's δειλός 'miserable' |
| ἱερήια (11.23, neuter plural noun) | "victims" | "the victims" | "sacrificial animals", "offerings" |
| κελαινεφὲς αἷμα (11.36) | "dark-clouded blood" | "blood dark as a cloud" (+ note: κελαινεφής is Zeus's epithet in its home use; here it is applied to blood) | "blood black as a storm-cloud", "dark blood" (reserved for αἷμα κελαινόν, 11.98), "cloud-dark"; keeps the table's Ζεὺς κελαινεφής "dark-clouded" |
| αἷμα κελαινόν (11.98) | "dark blood" | "the dark blood" | "black blood", "murky blood" |
| ψυχὴ νεκύων κατατεθνηώτων / μητρὸς κατατεθνηυίης (11.37, 11.84) | "of the dead, of those who had died" / "of my mother, who had died" | "the souls of the dead, of those who had died" / "my mother, who had died" | "the dead and gone", "the departed", "my late mother" (each drops the doubled sense of κατα-τεθνηώς 'having died') |
| νύμφαι (of the dead, 11.38) | "brides" | "brides" | "nymphs", "young women"; follows the table's νύμφα φίλη 'Dear bride' (νύμφη is literally 'young wife, bride') |
| ἠίθεοι (11.38) | "unmarried young men" | "unmarried young men" | "youths", "bachelors", "young men" alone |
| πολύτλητοι γέροντες (11.38) | "much-enduring old men" | "much-enduring old men" | "long-suffering old men" (the table's πολύτλας row already avoids 'long-suffering'), "old men who had suffered much" |
| παρθενικαὶ ἀταλαί (11.39) | "tender maidens" | "tender maidens" | "delicate", "young girls" |
| νεοπενθέα θυμὸν ἔχουσαι (11.39) | "with a newly-grieved heart" | "with hearts newly grieved" | "fresh in sorrow", "with newly mourning spirits" (θυμός is 'heart' in this part; 'spirit' is reserved for θυμὸς ἀγήνωρ) |
| ἄνδρες ἀρηίφατοι (11.41) | "men Ares-slain" | "men slain in war" (+ note: derivation not certain) | "war-slain", "killed in battle", "Ares' victims" |
| βεβροτωμένα τεύχεα (11.41) | "gore-stained armour" | "armour stained with gore" | "bloodied", "blood-spattered", "bloody armour" |
| οὐτάμενοι χαλκήρεσιν ἐγχείῃσιν (11.40) | "wounded by bronze-fitted spears" | "wounded by bronze-fitted spears" | "bronze-tipped spears"; follows the table's χαλκήρεα δοῦρα 'bronze-fitted spears' |
| χλωρὸν δέος (11.43) | "pale fear" | "pale fear" | "green fear", "yellow fear" (the table keeps "yellow" for χλωρὸν μέλι), "livid fear", "ashen fear"; the note says χλωρός is also 'yellow, pale green' |
| ἄκλαυτον καὶ ἄθαπτον (11.54, 11.72) | "unwept and unburied" | "unwept and unburied" | "without tears or burial", "unmourned and uninterred" |
| ζόφος ἠερόεις (11.57, ὑπὸ ζόφον ἠερόεντα) | "the misty gloom" | "the misty gloom" | "murky darkness", "the shadowy dark"; ἠερόεις is built on ἀήρ 'mist', as the table's ἠεροειδής 'misty-looking' |
| δαίμονος αἶσα κακή (11.61) | "the evil portion of some power" | "an evil lot from some power" | "an evil fate", "a god's evil doom"; follows the table's δαίμων 'some power' and αἶσα 'portion' (αἴσιμα) |
| ἀθέσφατος οἶνος (11.61) | "immense wine" | "immense wine" | follows the table's ἀθέσφατος 'immense' (7.273); "boundless", "unspeakable", "measureless" |
| θεῶν μήνιμα (11.73) | "a cause of the gods' wrath" | "a cause of the gods' wrath" | "the gods' curse", "a thing of anger" |
| ἀνὴρ δύστηνος (11.76, 11.80, 11.93) | "a wretched man" / "wretched one" | "a wretched man" / "wretched one" | "ill-fated", "unlucky", "poor man"; "wretched" is reserved for δύστηνος, as the table notes at λευγαλέος θάνατος |
| στυγεροὶ ἐπέεσσιν (11.81) | "hateful words" | "hateful words" | "hated words", "loathsome", "grim words" |
| ἐσσόμενοι (11.76, dative ἐσσομένοισι) | "those to come" | "those yet to come" | "future generations", "posterity" |
| ἀναχάζομαι / ἀποχάζομαι (11.95, 11.97) | "draw back" | "draw back" | "retreat", "withdraw", "step aside" |
| νημερτέα εἰπεῖν (11.96) | "to speak unerring things" | "to tell you unerring things" | "tell you the truth", "speak without error"; follows the table's νημερτής 'unerring' |
| Ἀντίκλεια (11.85) | "Anticleia" | "Anticleia" | "Anticlea", "Antikleia" |
| μάντις ἀμύμων (11.99) | "the seer, blameless" | "the blameless seer" | "peerless seer", "noble seer", "faultless seer" (follows the table's ἀμύμων 'blameless' + note) |
| χρύσεον σκῆπτρον (11.91) | "a golden sceptre" | "a golden sceptre" | "a staff of gold", "gold staff" (reserved for ῥάβδος / χρυσόρραπις) |
| ἴφια μῆλα (11.108, of the Sun's flocks) | "stout flocks" | "stout flocks" | "fat" (reserved for πίονα μῆλα), "sturdy", "mighty" (reserved for ἴφθιμος) |
| ὃς πάντ’ ἐφορᾷ καὶ πάντ’ ἐπακούει (11.109, whole half-line, of the Sun) | "who oversees all things and listens to all things" | "who sees everything and hears everything" | "who watches and hears all", "all-seeing, all-hearing" (compounds the Greek does not make) |
| ἐυῆρες ἐρετμόν · ἐυήρε’ ἐρετμά (11.121, 11.129, 11.125) | "well-fitted oar(s)" | "well-fitted oar(s)" | "well-made" (reserved for ἐυεργής), "shapely", "fine" (reserved for καλός); ἐυήρης is from ἀραρίσκω "fit", as in χαλκήρεα "bronze-fitted" |
| φοινικοπάρῃος (11.124, of ships) | "crimson-cheeked" | "with crimson cheeks" | "red-cheeked" (kept for μιλτοπάρῃος), "purple-prowed"; παρῃά is "cheek", the side of the bow |
| ἀθηρηλοιγός (11.128) | "chaff-ruiner" | "winnowing-shovel" (+ note: first element disputed) | "winnowing-fan", "grain-shovel" as if the compound were clear |
| φαίδιμος ὦμος (11.128, with the table's φαίδιμος "glorious") | "glorious shoulder" | "glorious shoulder" | "splendid", "shining" (reserved for ἀγλαός / φαεινός); the table's epithet is kept even of a shoulder |
| ἱερὰ καλά (11.130) | "fine sacrifices" | "fine sacrifices" | "fair", "beautiful" (kept for κάλλιμα / καλλι- words), "holy offerings" |
| ἐπιβήτωρ κάπρος (11.131) | "boar, mounter of sows" | "a boar that mounts sows" | "breeding boar", "stud boar" (hide the verb) |
| ἀβληχρός (11.135, of Odysseus's death; meaning unknown) | "mild" | "mild" (+ note: meaning not known; 'gentle', 'feeble', 'slow' guessed) | "gentle" (reserved for ἀγανός), "feeble" (reserved for ἄκικυς / ἠπεδανός), "soft" (reserved for μαλακός) |
| ἐξ ἁλός (11.134) | "out of the salt-sea" | "from the sea" (+ note: 'away from the sea' also possible) | "away from the sea", "out at sea" (each silently picks one reading) |
| γῆρας λιπαρόν (11.136) | "sleek old age" | "a sleek old age" | "peaceful old age", "prosperous old age", "comfortable" (each interprets λιπαρός) |
| λαοὶ ὄλβιοι (11.136–137) | "the peoples … prosperous" | "the people will be prosperous" | "blessed" (reserved for μάκαρ), "happy", "fortunate" |
| κότος (11.102, κότον ἔνθετο θυμῷ) | "resentment" | "resentment" | "anger", "grudge" (kept for ἐπιφθονέω), "wrath" (kept for μήνιμα) |
| τεκμαίρομαι ὄλεθρον (11.112) | "I fix destruction" | "I fix destruction" | "I foretell", "I ordain"; follows the table's τεκμαίρομαι "I fix" |
| ἀποτίσεαι βίας (11.118) | "you will exact payment for … violent deeds" | "you will exact payment … for their violence" | "avenge", "punish" (hide the middle voice and the payment) |
| ἐπιφθονέω (11.149) | "grudge" | "begrudge" | "refuse", "forbid"; kept apart from κότος "resentment" |
| ἐάω (11.147, ἐᾷς … ἴμεν) | "allow" | "allow" | "let" alone, "permit" |
| ἀριφραδής (11.126) | "very plain" | "very plain" | "clear" alone (loses the intensive ἀρι-), "manifest" (reserved for ἐναργής) |
| ἐννοσίγαιος (bare, 11.102) | "the earth-shaker" | "the earth-shaker" | "Poseidon" (the Greek withholds the name); a bare form of the table's κλυτὸς ἐννοσίγαιος |
| ὣς φαμένη ψυχή (11.150, the soul of Tiresias, grammatically fem.) | "So saying, the soul" | "So speaking, the soul" | "she" for Tiresias (the feminine is the noun's gender); "With these words" (listed as avoided for ὣς ἄρα φωνήσασ’; kept apart so the two formulas stay distinct) |
| κατὰ θέσφατ’ ἔλεξεν (11.151, tmesis for κατέλεξεν) | "the prophecies he had recounted" | "he had recounted his prophecies" | "had spoken his oracles" (loses κατα- "recount in full") |
| ζωὸς ἐών (11.156) · τὸν ἐόντα (11.144) | "being alive" · "being the one I am" | "while still alive" · "for who I am" | "living" alone |
| κὴρ θανάτοιο (11.171) | "death-spirit" | "spirit of the death that lays men at length" | "fate" (reserved for μοῖρα), "doom" (reserved for πότμος), "death-fate"; κήρ is a power of death |
| νοῦσος (11.172, 11.200) | "sickness" | "sickness" | "disease", "illness", "plague" |
| ἐύσκοπος ἰοχέαιρα (of Artemis, 11.198) | "the keen-sighted arrow-pourer" | "the keen-sighted one who showers her arrows" | "far-seeing", "sharp-eyed" (kept for ἐύσκοπος as in the table's "keen-sighted Argeïphontes"), "huntress" |
| γέρας (11.175, 11.184) | "prize" | "prize of honour" | "honour" alone, "right", "estate" (reserved for τέμενος) |
| μνηστὴ ἄλοχος (11.177; shipped at 1.35 in odyssey-001) | "wedded wife" | "wedded wife" | "wooed wife" (the literal sense goes in the note), "betrothed", "bride" |
| ἔμπεδα φυλάσσει (11.178; shipped at 2.226 in odyssey-007) | "keeps all things steadfast" | "keeps everything secure" | "securely guards", "keeps … safe" (both vary the shipped wording), "firmly holds", "unshaken" |
| πότνια μήτηρ (11.180) | "the lady mother" | "my lady mother" | "revered mother", "queen mother" (reserved for ἄνασσα); follows πότνια νύμφη "the lady nymph" |
| ὣς ἐφάμην, ἡ δ’ αὐτίκ’ ἀμείβετο πότνια μήτηρ (11.180, whole line, feminine counterpart of the table's ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμειβόμενος προσέειπεν) | "So I spoke, and she then at once answered, the lady mother:" | "So I said, and my lady mother answered me at once:" | "addressed" (reserved for προσέειπε / προσέφη); `i` "So I said" follows the shipped reply-formulas |
| ὀιζυρός (11.182, of nights and days) | "sorrowful" | "sorrowful" | "wretched" (reserved for δύστηνος), "miserable" (reserved for δειλός), "woeful" |
| δικασπόλος (11.186) | "justice-tending" | "who dispenses justice" | "judge", "magistrate", "lawgiver" |
| τεμένεα νέμεται (11.185) | "enjoys the domains" | "enjoys your domains" | "manages the estates", "tends the lands" |
| χαλεπὸν γῆρας (11.196) | "harsh old age" | "harsh old age" | "grievous" (reserved for λυγρός / ἀργαλέος), "hard" (reserved for tasks), "heavy" |
| ἀλωῆς οἰνοπέδοιο (11.193; shipped at 2.191 in odyssey-002) | "the vineyard plot" | "the vineyard plot" | "wine-ground vineyard", "wine-bearing", "wine-land"; the note gives οἰνόπεδος as "wine-ground", as at 2.191, and κατὰ γουνόν as "on the rising ground", as shipped |
| ἀγανοφροσύνη (11.203) | "gentleness of mind" | "gentleness of mind" | "gentle-mindedness" (“-minded” is reserved for the -φρων epithets of persons), "kindliness" |
| τηκεδὼν στυγερή (11.201) | "hateful wasting" | "hateful wasting" | "wretched", "melting away" |
| θυμός of the life that leaves the body (11.201, 11.203) | "life" | "life" | "heart", "spirit"; follows the table's ἀπὸ δ’ ἔπτατο θυμός "his life flew away" |
| ἐφορμάομαι (11.206, ἐφωρμήθην) | "I rushed upon" | "I rushed toward" | "I lunged", "I sprang" |
| σκιῇ εἴκελον ἢ καὶ ὀνείρῳ (11.207) | "like a shadow or even a dream" | "like a shadow or a dream" | "a phantom" (reserved for εἴδωλον), "a shade" (kept for the dead as a class, cf. σκιαί "shadows") |
| ἄχος ὀξύ (11.208) | "sharp grief" | "sharp grief" | "bitter pain", "keen sorrow" (kept for ἄλγος "pain") |
| κρυερὸς γόος (11.212, κρυεροῖο … γόοιο) | "chilling lament" | "chilling lament" | "cold lament", "icy", "bitter wailing"; κρυερός is from κρύος "frost"; τεταρπώμεσθα keeps "take our fill of", as in the table's "had their fill of food" |
| ἔρχευ · ἴσχεο μηδ’ ὀνομήνῃς (11.251) | "go … and restrain yourself, and do not mention (it)" | "go … and restrain yourself, and do not mention it" | "hold your tongue", "say nothing", "do not name me" (the Greek gives no object, and ὀνομαίνω is "mention, name") |
| ἀιδρείῃσι νόοιο (11.272) | "in the ignorance of her mind" | "in the ignorance of her mind" | "folly", "blindness of mind" (the table's ἀάσθη is "blinded"), "through ignorance" alone |
| εὐπατέρεια (of Tyro, 11.235) | "well-fathered" | "the daughter of a good father" | "of noble birth", "of a noble father" (ἀγαυός is "noble"), "fair-fathered" |
| καλή of a person (καλὴν Ἐπικάστην, 11.271) | "fine" | "beautiful" | "fair" (reserved for καλλι- words), "lovely" (reserved for ἐρατεινός); the plain καλά of the streams (11.240) stays "fine" in both layers |
| κάλλιστος / καλλίστους (11.239, 11.310) | "the fairest" | "the most beautiful" | "handsomest", "loveliest"; πολύ keeps "by far" |
| θείοιο (of the river Enipeus, 11.238) | "divine" | "divine" | "godlike" (reserved for ἀντίθεος), "heavenly" (reserved for δῖος); keeps the table's θεῖος "divine" |
| γαιήοχος ἐννοσίγαιος (of Poseidon, no name given, 11.241) | "the earth-holder, the earth-shaker" | "the earth-holder, the earth-shaker" | naming him "Poseidon" where the Greek withholds the name; both epithets keep the table's "earth-holder" and "earth-shaker" |
| εἰσάμενος (11.241, τῷ … εἰσάμενος) | "like to him having made himself" | "took the likeness of …" | "disguised as", "in the guise of"; follows the table's ἐεισαμένη "making herself like" |
| παρελέξατο (11.242) | "lay beside her" | "lay with her" | "slept with", "took her" (flatten or intensify the verb) |
| φιλοτήσια ἔργα (11.246) | "the works of love" | "the works of love" | "the deeds of love", "the act of love", "lovemaking" |
| χαῖρε, γύναι, φιλότητι (11.248, χαῖρε with a dative, said by a god leaving) | "Be glad, woman, in love" | "Be glad of this love, woman" | "Rejoice", "Hail", "Welcome" (reserved for the greetings in the table's χαῖρε, ξεῖνε row); γύναι keeps "woman", the plain unmarked address, not "wife" (that is the husband's address, 8.424) or "lady" |
| ἀποφώλιοι εὐναί (11.249) | "not fruitless … the beds" | "the beds … are not fruitless" | "barren", "empty", "in vain" (each picks one side of a word whose origin is not known); the note says only the origin is unknown |
| ὑποκυσαμένη (11.254) | "having conceived" | "she conceived" | "being with child", "having become pregnant" |
| θεράπων of Pelias and Neleus (11.255) | "attendants" | "attendants" | "servants" (reserved for δμῶες), "squires", "henchmen"; follows the table's ὀτρηρὸς θεράπων "brisk attendant" |
| πολύρρηνος (of Pelias, 11.257) | "rich in sheep" | "rich in sheep" | "rich in flocks" (μῆλα is "flocks"), "of many lambs"; built like πολύχρυσος "rich in gold" |
| εὐρύχορος (of Iolcus 11.256, of Thebes 11.265) | "of wide dancing-grounds" | "spacious" | follows the table's εὐρύχορον (of Elis, 4.635) in both layers |
| βασίλεια γυναικῶν (of Tyro, 11.258) | "the queen of women" | "the queen of women" | "queenly", "royal lady" |
| ἱππιοχάρμης (11.259) | "chariot-fighter" | "the chariot-fighter" | "horse-fighter", "who fights from horseback" (riding is not meant); ἵππιος is "of horses" and χάρμη "battle" |
| εὔχετο … ἰαῦσαι (of Antiope, 11.261) | "declared that she had slept in the arms of Zeus" | "declared that she had slept in the arms of Zeus" | "boasted", "prayed" (both are senses of εὔχομαι); follows the table's εὔχομαι "declare" (ἱκέτης εὔχομαι εἶναι) |
| φάσκε … μιγῆναι (of Iphimedeia, 11.306) | "claimed to have mingled with" | "claimed to have lain with" | "said she had been joined to"; φάσκω is kept as "claimed", apart from φάτο / φῆ "said"; μίγνυμι follows the table's "lay in love with" |
| ἑπταπύλοιο (of Thebes, 11.263) | "the seven-gated" | "seven-gated" | "of the seven gates", "seven-portalled" |
| πύργωσαν · ἀπύργωτον (11.264) | "gave it towers" · "without towers" | "gave it towers" · "without towers" | "walled", "fortified", "unwalled" (πύργος is "tower", not "wall") |
| θρασυμέμνων (of Heracles, 11.267) | "bold-purposed" | "bold of purpose" (+ note: formation not certain) | "stout-hearted" (θυμός is "heart"), "of bold courage", "brave-minded" (“-minded” is reserved for the -φρων epithets); second element probably from μέμονα, not certain |
| θυμολέων (of Heracles, 11.267) | "lion-hearted" | "lion-hearted" | "lion-spirited" (θυμός is "heart", the θυμὸς ἀγήνωρ "spirit" is the single exception), "with a lion's heart" |
| Ἀμφιτρύωνος υἱός (periphrasis for Heracles, 11.270) | "the son of Amphitryon" | "the son of Amphitryon" | naming him "Heracles" where the Greek withholds the name; built like the table's Τυδέος υἱός |
| μένος αἰὲν ἀτειρής (11.270) | "in strength ever unwearied" | "ever unwearied in strength" | "unbreakable", "indomitable", "tireless" (ἀτειρής is ἀ- + τείρω "wear down"); μένος keeps "strength" |
| ὑπέρθυμος (of Creon, 11.269) | "high-spirited" | "high-spirited" | follows the table's ὑπέρθυμος |
| πολυήρατος (of Thebes, 11.275) | "much-loved" | "beloved" | "lovely" (reserved for ἐρατεινός), "much-desired" (turned down for πολυάρητος), "delightful" (reserved for ἐραννός) |
| θεῶν ὀλοὰς διὰ βουλάς (11.276) | "through the gods’ deadly plans" | "because of the deadly plans of the gods" | "baneful counsels" ("baneful" is kept for ὀλοφώια), "cruel designs"; βουλή keeps "plan" as at 11.230 |
| πυλάρτης (of Hades, 11.277, Ἀίδαο πυλάρταο κρατεροῖο) | "gate-fastener" | "the strong gate-fastener" (+ note: meaning not certain) | "gatekeeper", "who bars the gates" (each silently picks the traditional explanation), "the mighty one of the gates" |
| βρόχος αἰπύς (11.278) | "a steep noose" | "a steep noose" | "a high-hanging noose", "a deadly noose", "sheer" (the table's αἰπύς is "steep", "sheer" being turned down at αἰπὺς ὄλεθρος); the note says it hangs a long way down |
| μητρὸς Ἐρινύες (11.280) | "a mother’s Erinyes" | "a mother’s Erinyes" | "the Furies" (the Latin name), "avengers", "the mother’s curses"; the note explains them as avenging spirits |
| ὁπλοτάτην κούρην (11.283) | "the youngest daughter" | "the youngest daughter" | "the youngest girl", "the youngest maiden"; κούρη as a plain noun is "daughter" here, "maiden" being the vocative of 8.468 |
| μυρία ἕδνα (11.282) | "numberless bridal gifts" | "countless bridal gifts" | follows the table's ὀνείατα μυρία (l "numberless", i "countless") |
| ἶφι ἄνασσεν (11.284) | "ruled with force" | "ruled powerfully" | "ruled mightily" ("mighty" is reserved for ἴφθιμος and ὄβριμος), "ruled by force" (reads as tyranny), "ruled strongly"; ἶφι is the old instrumental of ἴς "force" |
| Μινύειος (of Orchomenus, 11.284) | "Minyan" | "Minyan" | "of the Minyans", "Minyeian" |
| ἀγέρωχος (11.286) | "lofty" | "lofty" (+ note: meaning unknown) | "proud", "lordly" (reserved for ἀγήνωρ), "honoured", "high-spirited" (reserved for ὑπέρθυμος) |
| περικτίται (11.288) | "the neighbours" | "the neighbours" | "those who dwell round about", "the surrounding peoples" |
| ἕλικας βόας εὐρυμετώπους (11.289) | "crumple-horned, broad-browed cattle" | "the cattle of crumpled horn and broad brow" | follows the table's εἰλίποδας ἕλικας βοῦς and εὐρυμέτωπος |
| βίη Ἰφικληείη (11.290, 11.296) | "the force of Iphicles" | "the strong figure of Iphicles" | naturalising to "mighty Iphicles" (erases the periphrasis); follows the table's ἱερὴ ἲς Τηλεμάχοιο (l "force", i "the strong … figure") |
| ἀργαλέας βόας (11.291; the same word of the bonds, 11.293 δεσμοί … ἀργαλέοι) | "grievous" | "grievous" | "hard-to-drive", "troublesome", "difficult"; ἀργαλέος keeps "grievous", as in the table's μνηστὺς ἀργαλέη; the note says that of the cattle it means hard to deal with |
| μάντις ἀμύμων (11.291) | "the seer, blameless" | "the blameless seer" | follows the table's μάντις ἀμύμων (11.99); the note says the meaning of ἀμύμων is unknown |
| κατὰ … πέδησε (11.292, tmesis, of fate) | "fettered (him) fast" | "fettered him" | "bound him down", "held him captive" |
| βουκόλοι ἀγροιῶται (11.293) | "cowherds, countrymen" | "cowherds from the countryside" | "rustic herdsmen", "peasant cowherds" |
| ἂψ περιτελλομένου ἔτεος (11.295) | "as the year went round again" | "as the year came round again" | "as the year turned", "at the year’s turning"; ἔτος is "year", as ἐνιαυτός in 11.248 |
| θέσφατα πάντ’ εἰπόντα (11.297) | "having told all the god-declared things" | "after he had told all the prophecies" | "oracles", "decrees"; follows the table’s θέσφατα (9.507) |
| Διὸς δ’ ἐτελείετο βουλή (11.297) | "and of Zeus the plan was being fulfilled" | "and the plan of Zeus was being fulfilled" | "the will of Zeus", "the counsel of Zeus"; βουλή keeps "plan" |
| κρατερόφρων (of the twins, 11.299, dual, agreeing with παῖδε) | "strong-minded" | "of strong mind" | "stout-hearted" (θυμός / κῆρ), "stout-minded", "wise" (δαΐφρων is "wise-minded"); “-minded” in `l` follows the -φρων epithets |
| πὺξ ἀγαθός (11.300) | "good with the fist" | "good with his fists" | "a good boxer", "skilled at boxing"; follows the table's βοὴν ἀγαθός "good at the war-cry" |
| φυσίζοος αἶα (11.301) | "the life-giving earth" | "the life-giving earth" | "the grain-giving earth" (reserved for ζείδωρος), "nourishing", "all-nourishing" (πουλυβότειρα is "much-nourishing") |
| ἑτερήμεροι (11.303) | "on alternate days" | "on alternate days" | "every other day", "day about", "in turn"; ἕτερος + ἡμέρα |
| τεθνᾶσιν (11.304, ἄλλοτε μὲν ζώουσ’ … ἄλλοτε δ’ αὖτε τεθνᾶσιν) | "are dead" | "they are dead" | "have died", "are lifeless"; ζώουσ’ keeps "live" |
| τιμὴν δὲ λελόγχασιν ἶσα θεοῖσι (11.304) | "honour they have received as their lot, equal to gods" | "they have received honour equal to that of gods" | "won", "obtained"; λαγχάνω is "receive as one’s share" |
| μινυνθάδιος (11.307) | "short-lived" | "short-lived" | "of brief life", "doomed to die young" |
| ἀντίθεος Ὦτος · τηλεκλειτὸς Ἐφιάλτης (11.308) | "godlike Otus" · "far-famed Ephialtes" | "the godlike Otus" · "far-famed Ephialtes" | κλειτός is κλυτός in another spelling, so τηλεκλειτός takes the table's τηλεκλυτός "far-famed" |
| μήκιστοι (11.309) | "the tallest" | "the tallest" | "the longest", "the biggest"; μῆκος keeps "length" (`l`) and "height" (`i`) in 11.312, as the body's length is its height |
| ἐννέωροι · ἐννεαπήχεες · ἐννεόργυιοι (11.311–312) | "nine years old" · "nine-cubited" · "nine-fathomed" | "nine years old" · "nine cubits across" · "nine fathoms in height" | "nine feet" (modern units); the note gives the measures once; follows the table's ἐννεώροιο βοός "nine-year-old" and ὄργυια "a fathom" |
| πολυάικος πολέμοιο φυλόπιδα στήσειν (11.314) | "to raise the battle-din of a war of many onrushes" | "that they would raise the din of a war of many onrushes" (+ note: meaning of πολυάικος not certain) | "furious", "swift" for πολυάικος (each silently picks one guess), "rouse the war-cry" (φύλοπις is "battle-din", not "cry") |
| ἵν’ οὐρανὸς ἀμβατὸς εἴη (11.316) | "that heaven might be climbable" | "so that heaven could be climbed" | "scalable", "a path to the sky"; οὐρανός keeps "heaven" |
| ἥβης μέτρον (11.317) | "the measure of youth" | "the measure of youth" | "full manhood", "the full measure of youth", "the age of strength" (the note says "full manhood"); ἥβη keeps the table's "youth" |
| ἰούλους · λάχνῃ ἐυανθέι (11.319–320) | "the down" · "fair-flowering beard" | "the down" · "a fair-flowering beard" | "the first beard", "bloom", "luxuriant"; λάχνη is properly "woolly hair" and is "beard" here (the note says so); ἐύ- is "fair", as in ἐυστέφανος |
| ὁ δ’ … ἐξεναρίξας · γῆμεν (11.273–274) | "his own father having killed … married (her)" | "he killed his own father and married her" | "slew and stripped", "wedded"; γῆμεν keeps "married" (as the table's Νηλεὺς γῆμεν, 11.282) |
| ἀνάπυστα θέσαν (11.274) | "made (it) known" | "made it known" | "revealed", "laid bare", "brought to light" (each fixes a nuance the Greek leaves open) |
| Ὄσσα · Οὔλυμπος · Πήλιον (11.315–316) | "Ossa" · "Olympus" · "Pelion" | same | "Mount Ossa" etc.; the Greek names the mountains bare; εἰνοσίφυλλον keeps "leaf-shaking" (as at 9.22) |
| Names in the catalogue (11.235–320) | Tyro, Salmoneus, Cretheus, Aeolus, Enipeus, Pelias, Neleus, Iolcus, Pylos, Aeson, Pheres, Amythaon, Antiope, Asopus, Amphion, Zethus, Thebes, Alcmene, Amphitryon, Heracles, Megara, Creon, Epicaste, Oedipus, Chloris, Iasus, Orchomenus, Nestor, Chromius, Periclymenus, Pero, Phylace, Iphicles, Leda, Tyndareus, Castor, Polydeuces, Iphimedeia, Aloeus, Otus, Ephialtes, Orion, Ossa, Olympus, Pelion, Apollo (unnamed), Leto | same | "Polydeukes", "Kastor", "Herakles", "Iphiclus"; the familiar Latinised forms, as for the other names in the table; Apollo is never named in these lines (11.318 gives only "the son of Zeus, whom fine-haired Leto bore") |
| Πηληϊάδης (11.467, Πηληϊάδεω Ἀχιλῆος) | "Achilles, Peleus’ son" | "Achilles, son of Peleus" | "Peleides", "Peleiades"; follows the table’s Πηλεΐων "the son of Peleus" for the same father |
| ἀφραδής (11.476, of the dead, νεκροὶ ἀφραδέες) | "senseless" | "senseless" | "foolish" and "witless" (both used elsewhere for νήπιος), "mindless", "thoughtless"; ἀ- + φράζομαι |
| πινυτός (11.445, πινυτή, of Penelope) | "discerning" | "discerning" | "prudent" (reserved for πεπνυμένος, to which the word is related), "sensible", "wise" (περίφρων is "circumspect"), "thoughtful" |
| φέρτατος (11.478, μέγα φέρτατ’ Ἀχαιῶν) | "by far the best" ("greatly best") | "by far the best of the Achaeans" | "mightiest", "bravest", "noblest" (each narrows the word) |
| Ἀργεῖοι (11.485, 11.500, 11.518, 11.524) | "Argives" | "Argives" | "Greeks" (reserved for Δαναοί in `i`), "Achaeans" (that is Ἀχαιοί) |
| εὐρύς of a place (Σπάρτῃ εὐρείῃ 11.460, Τροίῃ εὐρείῃ 11.499) | "broad" | "broad" | "wide" (kept for εὐρύοπα and the -όδεια, -πορος compounds), "spacious" (reserved for εὐρύχορος), "wide-streeted" (εὐρυάγυια) |
| νήπιος of a baby (11.449, νήπιος) | "an infant" | "an infant son" | "foolish" (the table’s rendering for the adult sense, 9.419), "childish" (the register rule), "witless" |
| ἀσκηθής (11.535) | "unscathed" | "unscathed" | "unharmed" (reserved for ἀπήμων of persons), "unhurt", "safe and sound" |
| χαλκοβαρές (11.532, δόρυ χαλκοβαρές) | "bronze-heavy" | "bronze-heavy" | "bronze-tipped" and "bronze-headed" (the table keeps "bronze-fitted" for χαλκήρης), "heavy-bronzed", "weighty" |
| δηιοτής (11.516, ἐν αἰνῇ δηιοτῆτι) | "fighting" | "fighting" | "slaughter" (reserved for φόνος), "carnage", "strife" (reserved for ἔρις); αἰνός keeps the table’s "fearsome" |
| ἀάπτους (11.502, χεῖρας ἀάπτους; meaning unknown) | "untouchable" | "irresistible" (+ note: meaning not known; both are traditional guesses) | "unconquerable", "invincible" (each picks one guess without saying so) |
| στύξαιμι (11.502, from στύζω, related to στυγέω) | "make hateful" | "make dreaded" | "make terrible", "make loathed"; the note gives the root and says the sense is taken from the context |
| ἐπάρουρος (11.489; exact force not certain) | "being on the ploughland" | "work on the land" (+ note: 'alive on the earth' or 'tied to the soil', not certain) | "above ground" or "living" (silently picks one guess) |
| ἄκληρος (11.490, ἀνδρὶ παρ’ ἀκλήρῳ) | "a man without allotment" | "a landless man" | "poor man", "needy"; ἀ- + κλῆρος "lot, plot of land" |
| ἐπιμίξ (11.537; rare adverb) | "in confusion" | "in confusion" | "indiscriminately", "pell-mell", "in a mêlée" (all more specific than the root μίγνυμι "mix") |
| Κήτειοι (11.521; a people, not otherwise known) | "Ceteians" | "Ceteian" | "Cetaeans", "Ketians"; the note says who they were is not known |
| παραυδάω (11.488, παραύδα) | "speak soothingly" | "talk soothingly" | "soothe" and "try to soothe" (the second adds a conative sense the present imperative does not carry), "console" (the note gives it as a sense), "persuade", "talk round" |
| τὸν μὲν ἐγὼν ἐπέεσσι προσηύδων μειλιχίοισιν (whole line, 11.552; no reply, so kept apart from the reply-formulas) | "Him, indeed, I with words addressed, soothing ones:" | "I addressed him with soothing words:" | "answered" (reserved for ἠμείβετο), "gentle", "honeyed" (μειλίχιος is 'soothing, gentle'; "honeyed" would suggest μελιηδής "honey-sweet") |
| κεφαλή as a periphrasis for the person (11.549 τοίην γὰρ κεφαλήν; 11.557 Ἀχιλλῆος κεφαλῇ) | "head" | "such a man" (549) / "Achilles … himself" (557) | "life", "dear one" (add what the Greek does not say); same device as the table's ἱερὴ ἲς Τηλεμάχοιο, but `i` names the person because "head" alone reads as a body part in English |
| πύργος (of Ajax as defender, 11.556) | "tower" | "tower" | "bulwark" (reserved for ἕρκος), "rampart", "wall" |
| κρατέρ’ ἄλγε’ ἔχοντα (11.582, 11.593; the same words twice, of Tantalus and Sisyphus) | "having strong pains" | "beset by harsh pains" | "mighty" (reserved for ἴφθιμος), "grievous" (reserved for λυγρός / ἀργαλέος), "hard" (reserved for tasks); ἄλγε’ ἔχοντα keeps the table's "beset by pains" in `i` and "having pains" in `l` |
| πελώριος (11.572 of Orion, 11.594 of the stone) | "huge" | "huge" | "monstrous" (that is πέλωρ "monster", already fixed in δεινὸν πέλωρ), "giant", "prodigious" |
| οἰοπόλος (of mountains, 11.574; usually glossed 'lonely', not certain) | "lonely" | "lonely" (+ note: sense not certain) | "sheep-haunted" (silently picks the other guess), "desolate" |
| παγχάλκεος · ἀαγής (11.575, of Orion's club) | "all of bronze" · "unbreakable" | "all of bronze" · "that could never be broken" | "wholly bronze", "bronze through and through" |
| καλλίχορος (of Panopeus, 11.581) | "of the fair dancing-grounds" | "with its fair dancing-grounds" | "of fair dances", "fair-dancing"; keeps the table's χορός "dancing-ground" (εὐρύχορος "of wide dancing-grounds") |
| ἀναιδής (λᾶας ἀναιδής, 11.598) | "shameless" | "ruthless" | "pitiless" alone, "unfeeling", "heartless"; `l` keeps the literal "shameless", as for κυνῶπις, and `i` the sense the line needs |
| βίη Ἡρακληείη (11.601; periphrasis for Heracles) | "the might of Heracles" | "the powerful figure of Heracles" | naturalising it to "mighty Heracles" (erases the periphrasis; same device as ἱερὴ ἲς Τηλεμάχοιο and μένος Ἀλκινόοιο); "mighty" is reserved for ἴφθιμος |
| χρυσοπέδιλος (of Hera, 11.604) | "golden-sandalled" | "of the golden sandals" | "gold-shod", "golden-slippered" (πέδιλον is 'sandal') |
| ἐρεμνὴ νύξ (11.606) | "dusky night" | "dusky night" | "black night" (the table's νὺξ μέλαινα in `l`), "dark night" (the table's `i` for μέλας), "murky night" |
| χαροποὶ λέοντες (11.611; meaning of χαροπός not certain) | "fierce-eyed lions" | "fierce-eyed lions" (+ note: 'fierce' and 'bright' both proposed) | "bright-eyed" (reserved against γλαυκῶπις), "glad-eyed" (silently picks one guess), "grey-eyed" |
| ἀέθλους (of Heracles' tasks, 11.622, 11.624 ἄεθλον) | "labours" | "labours" | "contests" (the table's ἄεθλον for games), "trials" (kept for the toils of Odysseus), "tasks"; a deliberate exception to the table's "contest(s)" row for ἄεθλος (that row says passim), because here the word names the labours imposed on Heracles |
| κρατερώτερον ἄεθλον (11.624) | "a stronger labour" | "a labour … harder" | "mightier" (reserved for ἴφθιμος), "more powerful"; κρατερός is "strong" in `l` and "harsh" / "hard" in `i` |
| ἆ δείλ’ (cry of address, 11.618) | "oh, miserable one" | "oh, miserable man" | "ah" (reserved for ὢ πόποι), "alas", "poor wretch"; δειλός keeps the table's "miserable" |
| ἔθνεα μυρία νεκρῶν (11.632) | "countless tribes of the dead" | "countless tribes of the dead" | "myriads", "ten thousand", "hosts" |
| χλωρὸν δέος (11.633; the line half is worded as in the shipped 11.43) | "pale fear" | "pale fear" | "green fear", "ashen fear", "sallow" |
| Γοργείη κεφαλή (11.634) | "the Gorgon head" | "the Gorgon head" | "the Gorgon's head" (genitive), "Gorgonian" |
| κάλλιμος οὖρος (11.640) | "a lovely fair wind" | "a lovely fair wind" | "beautiful", "fine" alone (drops οὖρος "fair wind", the table's rendering), "favourable" |
| ἐρικυδής, κυδρός (11.576 Γαίης ἐρικυδέος, 11.580 κυδρήν, 11.631 ἐρικυδέα) | "glorious" | "glorious" | "famous" (reserved for κλυτός); follows the shipped ἐρικυδέα δαῖτα "a glorious feast" and κυδίστη "most glorious" |
| ἡ δ’ ἐν μέσσῳ στᾶσα μετηύδα δῖα θεάων (whole-line speech introduction, 12.20) | "And she, in the midst having stood, spoke among them, heavenly-one of goddesses:" | "And she, heavenly even among goddesses, stood in the midst and spoke among them:" | "answered" (reserved for ἠμείβετο), "addressed" (reserved for προσέειπε / προσέφη); μετηύδα keeps "spoke among", δῖα θεάων the table's "heavenly-one of goddesses" / "heavenly even among goddesses" |
| καὶ τότε δή μ’ ἐπέεσσι προσηύδα πότνια Κίρκη (whole-line introduction to a speech made to Odysseus, 12.36) | "And then indeed me with words spoke the lady Circe:" | "And then the lady Circe spoke to me:" | "addressed" (reserved for προσέειπε / προσέφη), "answered"; προσηύδα keeps "spoke", πότνια the table's "lady" |
| σχέτλιοι (vocative plural, 12.21; the table has σχέτλιε "Cruel one") | "Cruel ones" | "Cruel ones" | "wretches", "reckless men", "rash fools"; follows the table; the note says the force is nearer dismay than cruelty |
| δισθανής (12.22, δισθανέες) | "twice-dying" | "men who die twice" | "twice-dead", "doubly dead" (the Greek is the present-stem δίς + θνῄσκω "die", not "be dead") |
| ἕκαστα (12.16 τὰ ἕκαστα; 12.25 ἠδὲ ἕκαστα; 12.34 ἐξερέεινεν ἕκαστα) | "each thing" | "every detail" / "everything" | "the particulars", "all the details" in `l`; ἕκαστα is "each thing" in `l` throughout, and `i` may vary between "every detail" and "everything" with the sentence |
| κυανῶπις (of Amphitrite, 12.60, κυανώπιδος Ἀμφιτρίτης) | "dark-eyed" | "dark-eyed" | "blue-eyed", "dark-faced", "blue-faced" (κυανο- is "dark", as in κυανοχαίτης "dark-haired" and κυανόπρῳρος "dark-prowed"); kept apart from γλαυκῶπις "gleaming-eyed" and ἐυῶπις "fair-eyed" |
| ἀγάστονος (of Amphitrite, 12.97, ἀγάστονος Ἀμφιτρίτη) | "loud-groaning" | "loud-groaning" | "much-sighing", "wailing", "roaring" (loses στένω "groan"); built on the intensive ἀγα- and στένω; kept apart from the table's κλυτὸς Ἀμφιτρίτη "famous Amphitrite" |
| Πλαγκταί (12.61, Πλαγκτὰς … καλέουσι) | "the Wandering Rocks" | "the Wandering Rocks" | "the Wanderers" alone (drops the πέτραι supplied from 12.59), "the Planktai" (a transliteration that hides the sense) |
| ποντοπόρος νηῦς (12.69) | "sea-crossing ship" | "sea-crossing ship" | "sea-faring" (kept clear of the table's avoided "seafaring" for φιλήρετμος), "sea-going", "ocean-crossing"; πόντος is "open sea" in the table and πόρος "passage", so "sea-crossing" |
| πᾶσι μέλουσα (of Argo, 12.70) | "a care to all" | "of concern to all" (+ note: the Greek says only "a care to all") | "famed among all men", "on everyone's lips" (state the sense the word leaves open); μέλω keeps "care", as in the table's πομπὴ … μελήσει |
| σκόπελος (12.73–95, of the two crags; μέσσῳ ἐν σκοπέλῳ) | "crag" | "crag" | "rock" (reserved for πέτρη / πέτρα), "cliff", "peak" (reserved for κορυφή); a σκόπελος is a rocky outlook |
| πέτρη · πέτρα (12.59 πέτραι, 12.64 λὶς πέτρη, 12.71 μεγάλας … πέτρας) | "rock" | "rock" | "crag" (reserved for σκόπελος), "cliff", "boulder" |
| λίς of rock (12.64 λὶς πέτρη; 12.79 πέτρη γὰρ λίς ἐστι) | "smooth" | "smooth" | "sheer" (turned down at αἰπὺς ὄλεθρος and ἠλίβατος), "bare", "slippery", "polished" (kept for περίξεστος "polished all round") |
| τρήρωνες (of doves, 12.63; τρήρων "timorous", from τρέω "tremble") | "timorous" | "timorous" | "shy", "fluttering", "swift-flying" (the last is a different word), "fearful" |
| ἐναρίθμιος (12.65, ἐναρίθμιον εἶναι) | "to be one of the number" | "to keep the number complete" | "to be counted in", "to make up the tally" |
| αἰζήιος ἀνήρ (12.83) | "a vigorous man" | "a vigorous man" | "strong young man" (adds "young" and "strong"), "stalwart", "lusty" |
| σμερδαλέος (12.91, σμερδαλέη κεφαλή) | "frightful" | "frightful" | "terrible", "dreadful" (both taken by σχέτλιος / θεσπέσιος / δεινός), "fearsome" (reserved for αἰνός), "grim" (reserved for ἐπαινή) |
| ἄωροι (12.89, πόδες … ἄωροι; meaning not known) | "dangling" | "dangling" (+ note: meaning not known; 'misshapen' and 'unseasonable' also proposed) | "misshapen", "uneven", "untimely" (each silently picks one guess) |
| μέλας θάνατος (12.92, μέλανος θανάτοιο) | "black death" | "black death" | "dark death", "gloomy death"; μέλας is "black" of ships and night, "dark" of wine, water, wave and earth, and death is placed with the first group |
| πλεῖοι (12.92, πλεῖοι μέλανος θανάτοιο) | "full" | "full" | "laden", "replete" |
| δελφῖνες · κύνες (12.96, δελφῖνάς τε κύνας τε; which sea creature κύνες names is not known) | "dolphins and dogs" | "dolphins and dogs" (+ note: which creature is meant is not known) | "dogfish", "seals", "sea-dogs" (each silently picks one guess) |
| κῆτος (12.97, μεῖζον … κῆτος) | "sea-beast" | "sea-monster" | "whale" (silently picks one animal), "sea-creature" |
| ἀκήριος (12.98, ναῦται ἀκήριοι; from ἀ- + κήρ, formation not fully clear) | "uninjured" | "uninjured" | "unscathed" (reserved for ἀσκηθής), "unharmed" (reserved for ἀπήμων of persons), "unhurt", "lifeless" |
| εὐχετόωνται (12.98, εὔχομαι with an infinitive of what is claimed) | "declare" | "declared" / "declare" | "boast", "claim", "pray" (the table's εὔχομαι is "declare") |
| κακορραφίῃ ἀλεγεινῇ (12.26; κακορραφίη a rare word, κακός + ῥάπτω "stitch") | "grievous ill-contriving" | "grievous bad planning" | "wicked plotting", "mischief"; ἀλεγεινός keeps the shipped "grievous" |
| Σειρῆνες · Σκύλλη · Ἀργώ · Ἰήσων · Αἰήτης · Ἀμφιτρίτη · Ἐλπήνωρ | the Sirens, Scylla, Argo, Jason, Aeetes, Amphitrite, Elpenor | same | "Seirenes", "Skylla", "Argos" for the ship; the familiar Latinised forms, as for the other names in the table |
| δῖα Χάρυβδις (12.104; stock epithet on a monster, kept though it sits oddly) | "heavenly Charybdis" | "heavenly Charybdis" | "divine Charybdis" (reserved for θεῖος), "bright", "dread" (reserved for δεινός); follows the table's δῖος "heavenly" |
| ἀναρροιβδέω / ῥοιβδέω (12.104, ἀναρροιβδεῖ; 12.105, ἀναροιβδεῖ; 12.106, ῥοιβδήσειεν) | "sucks down" / "gulps down" | "sucks down" / "gulps it down" | "swallows" (loses the roaring), "spews", "belches" (the verb is the down-draught, ἀνίησιν is the up-draught); ῥοῖβδος is the rushing noise of water |
| ἐρινεὸς μέγας, φύλλοισι τεθηλώς (12.103) | "a wild fig tree, great, flourishing with leaves" | "a great wild fig tree, flourishing with leaves" | "fig tree" alone (reserved for συκέα, 7.116), "caprifig" (a technical term); τεθηλώς keeps "flourishing", as shipped for τεθαλυῖα (6.293) |
| ἐπιποιμένες (12.131, θεαὶ δ’ ἐπιποιμένες εἰσίν) | "their shepherds" | "set over them as shepherds" | "herdswomen", "keepers", "guardians" (φύλαξ); ἐπιποιμήν is "one set over flocks", from ποιμήν "shepherd" |
| Κράταιις · Θρινακίη · Φαέθουσα · Λαμπετίη · Νέαιρα · Ὑπερίων (12.124, 127, 132–133) | Crataeis, Thrinacia, Phaethusa, Lampetie, Neaera, Hyperion | same | "Krataiis", "Thrinakia", "Phaethousa", "Lampetia", "Neaira"; the familiar Latinised forms, as for the other names in the table; Ἠελίῳ Ὑπερίονι is "the Sun Hyperion" (`l`) / "the Sun, Hyperion" (`i`), and Ὑπεριονίδης (12.176) is "Hyperion’s son" / "the son of Hyperion" |
| πολεμήια ἔργα (12.116) | "the works of war" | "deeds of war" | "warlike deeds" (reserved for ἀρήιος "warlike"), "feats of arms", "martial deeds" |
| ὦ φίλοι (12.154, plural address; cf. ὦ φίλος "O friend" / "Friend") | "O friends" | "Friends" | "My friends", "Dear friends" (reserved for φίλε in ξεῖνε φίλε), "Comrades" |
| δὴ τότ’ ἐγὼν ἑτάροισι μετηύδων ἀχνύμενος κῆρ (whole-line first-person speech introduction, 12.153) | "Then indeed I among my companions spoke, grieving in heart:" | "Then, grieving in heart, I spoke among my companions:" | "addressed" (reserved for προσέειπε / προσέφη), "answered" (reserved for ἠμείβετο), "said to my companions" (drops μετά "among"); μετηύδων keeps "spoke among", as in the table's δή ῥα τότ’ ἀμφιπόλοισι μετηύδα, and ἀχνύμενος κῆρ keeps the shipped "grieving in heart" |
| καρπαλίμως (12.166) | "speedily" | "speedily" | "swiftly" (reserved for θοός and ὠκύς), "quickly" (kept for αἶψα, ὦκα, θᾶσσον), "rapidly" (turned down at κραιπνῶς) |
| ῥίμφα (12.182, ῥίμφα διώκοντες) | "nimbly" | "nimbly" | "swiftly" (reserved for θοός / ὠκύς), "lightly", "briskly" |
| ὠκύαλος νηῦς (12.182; ὠκύς + ἅλς, "swift on the sea") | "the swift-sailing ship" | "the swift-sailing ship" | "sea-swift", "fast-sailing"; ὠκύς keeps the table's "swift", and the compound is kept apart from νηῦς θοή "swift ship" |
| πολύαιν’ Ὀδυσεῦ (12.184, πολύαινος, from πολύς + αἶνος "praise") | "much-praised Odysseus" | "much-praised Odysseus" | "much-renowned" (reserved for the κλυτός family), "famous" (reserved for κλυτός), "full of praise"; μέγα κῦδος Ἀχαιῶν keeps the table's "great glory of the Achaeans" |
| μελίγηρυς ὄψ (12.187, μελίγηρυν … ὄπ’; μέλι + γῆρυς "voice") | "a honey-toned voice" | "the honey-toned voice" | "honey-sweet" (reserved for μελιηδής), "honey-voiced voice" (says "voice" twice), "honeyed" |
| νωιτέρην ὄπα (12.185, dual possessive of the two Sirens) | "of us two the voice" | "the voice of the two of us" | "our voice" alone, which would lose the dual; follows the shipped "the voice of the two Sirens" (12.52) |
| δεσμῷ ἐν ἀργαλέῳ (12.160–161) | "a bond, a grievous one" | "a grievous bond" | "painful bond", "hard bond"; ἀργαλέος keeps the table's "grievous" |

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
  of Mermerus, Ephyra, Dulichium, Same, Zacynthus, Pylos, Sparta; the Harpies — Murray prints ἅρπυιαι
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

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
| μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος (1.1, house rendering of the opening) | "The wrath sing, goddess, of Peleus’-son Achilles" | "Goddess, sing the wrath of Peleus’ son Achilles" | "rage", "anger" (the famous modern choices), "Sing, goddess, the anger of…", "Rage — Goddess, sing the rage…", "Sing of the cataclysmic wrath"; "wrath" is the old, pre-modern rendering and the word μῆνις needs: a lasting, god-sized anger |
| μῆνις | "wrath" | "wrath" | "rage", "anger" (kept for χόλος), "fury"; χόλος stays "anger", κότος "resentment" (as in the Odyssey table) |
| οὐλομένην (of the wrath, 1.2) | "the ruinous one" | "the ruinous wrath" | "accursed", "murderous", "destructive", "cataclysmic"; keeps the Odyssey's οὐλόμενος "ruinous" |
| μυρί’ … ἄλγε’ ἔθηκε (1.2) | "countless pains laid" | "laid countless pains on" | "thousandfold", "immeasurable pain", "countless losses", "incalculable pain" |
| ἰφθίμους ψυχάς (1.3) | "mighty souls" | "mighty souls" | "strong souls"; ἴφθιμος keeps the Odyssey's "mighty" |
| Διὸς δ’ ἐτελείετο βουλή | "and of Zeus the plan was being fulfilled" | "and the plan of Zeus was being fulfilled" | Odyssey table, unchanged ("the will of Zeus" avoided) |
| ἄναξ ἀνδρῶν (Ἀγαμέμνων) | "lord of men" | "lord of men" | Odyssey table, unchanged |
| δῖος Ἀχιλλεύς | "heavenly Achilles" | "heavenly Achilles" | "brilliant", "godlike" (ἀντίθεος), "noble"; follows the Odyssey's δῖος "heavenly" |
| ἑκηβόλος (Ἀπόλλων) | "far-shooting" | "far-shooting" (+ note: usual explanation) | "far-darting" (kept for ἑκατηβελέτης), "the archer", "who strikes from afar" |
| ἑκατηβελέτης (1.75) | "far-darting" | "far-darting" | "far-shooting" (ἑκηβόλος), "deadly archer" |
| ἀργυρότοξος | "silver-bowed" | "silver-bowed" | Odyssey table, unchanged |
| Φοῖβος Ἀπόλλων | "Phoebus Apollo" | "Phoebus Apollo" | — |
| ἀρητήρ (1.11, 1.94) | "praying-priest" | "priest" / "his priest" | "the priest" in `l` (kept for ἱερεύς), "holy man" |
| ἱερεύς (1.23, 1.62) | "priest" | "priest" | — |
| ἄποινα · ἀπερείσια ἄποινα (1.13) | "ransom" · "unstinted ransom" | "ransom" · "an unstinted ransom" | "boundless", "measureless", "untold", "beyond number", "priceless" (ἀπερείσιος keeps the Odyssey's "unstinted" in `l`) |
| στέμματα / στέμμα (1.14, 1.28) | "fillets" / "fillet" | same | "wreaths", "garlands", "ribbons" |
| κοσμήτορε λαῶν (1.16) | "the two marshallers of the people" | "marshals of the people" | Odyssey table (κοσμήτωρ λαῶν), dual kept in `l` |
| ἐϋκνήμιδες Ἀχαιοί | "well-greaved Achaeans" | same | Odyssey table, unchanged |
| Ὀλύμπια δώματ’ ἔχοντες | "who hold the Olympian halls" | "who hold the halls of Olympus" | Odyssey table, unchanged |
| ἀγλαὰ … ἄποινα (1.23) | "the splendid ransom" | "the splendid ransom" | Odyssey ἀγλαός "splendid" |
| κρατερὸν δ’ ἐπὶ μῦθον ἔτελλε (1.25, 1.326 etc.) | "and a strong word enjoined on him" | "and laid a strong charge on him" | "harsh order", "stern command", "brutal" |
| πολυφλοίσβοιο θαλάσσης | "the much-roaring sea" | "the loud-roaring sea" | Odyssey table, unchanged |
| ἠΰκομος | "fine-haired" | "fine-haired" | Odyssey table (ἠύκομος), unchanged |
| κλῦθί μευ | "Hear me" | "Hear me" | as shipped in the Odyssey |
| ζάθεος (1.38) | "most holy" | "most holy" | "sacred" (ἱερός), "holy" (ἠγάθεος in the Odyssey table) |
| ἶφι ἀνάσσεις (1.38) | "are lord with force" | "powerfully rule" | Odyssey table (ἶφι ἄνασσεν "ruled with force / ruled powerfully") |
| Σμινθεύς | "Smintheus" | "Smintheus" (+ note: meaning uncertain) | "Mouse-god", "lord of mice" |
| κατὰ πίονα μηρί’ ἔκηα | "fat thigh-pieces I burned" | "burned the fat thigh-pieces" | as shipped in the Odyssey (21.762) |
| ὣς ἔφατ’ εὐχόμενος, τοῦ δ’ ἔκλυε Φοῖβος Ἀπόλλων | "So he spoke, praying, and him heard Phoebus Apollo," | "So he prayed, and Phoebus Apollo heard him," | Odyssey table pattern, unchanged |
| χωόμενος κῆρ | "incensed in heart" | "incensed at heart" | χώομαι keeps the Odyssey's "be incensed"; "angry at heart", "enraged" |
| νυκτὶ ἐοικώς (1.47) | "to night likened" | "like the night" | "like nightfall", "like the coming of night", "his descent was like" |
| κύνας ἀργούς | "swift dogs" | "swift dogs" (+ note: disputed) | Odyssey table, unchanged |
| ἐχεπευκής (1.51) | "sharp-pointed" | "sharp" (+ note: formation uncertain) | "piercing", "pine-sharp", "bitter" |
| κῆλα θεοῖο (1.53) | "the shafts of the god" | "the god’s shafts" | "arrows" (kept for ὀϊστοί, ἰός), "darts" |
| λευκώλενος Ἥρη | "white-armed Hera" | "white-armed Hera" | Odyssey λευκώλενος "white-armed" |
| πόδας ὠκὺς Ἀχιλλεύς | "swift-in-feet Achilles" | "Achilles, swift of foot" | Odyssey table πόδας ὠκύς ("swift in feet" / "swift of foot"); "swift-footed", "fleet-footed" reserved for ποδώκης, ποδάρκης |
| τὸν δ’ ἀπαμειβόμενος προσέφη πόδας ὠκὺς Ἀχιλλεύς | "Him answering addressed swift-in-feet Achilles:" | "In answer Achilles, swift of foot, said to him:" | follows the Odyssey's reply-formula row |
| ἤτοι ὅ γ’ ὣς εἰπὼν κατ’ ἄρ’ ἕζετο· τοῖσι δ’ ἀνέστη | "He then, having so spoken, sat down; and among them stood up" | "So he spoke, and sat down; and among them there stood up" | as shipped in the Odyssey (odyssey-007, 2.224) |
| οἰωνοπόλων ὄχ’ ἄριστος (1.69) | "of bird-diviners by far the best" | "far the best of those who read the birds" | "augurs", "prophets", "best of seers" (μάντις is "seer") |
| ὅ σφιν ἐὺ φρονέων ἀγορήσατο καὶ μετέειπεν | Odyssey wording | Odyssey wording | reused verbatim |
| Διῒ φίλος | "dear to Zeus" | "dear to Zeus" | "beloved of Zeus", "loved by Zeus" |
| ἐμεῦ ζῶντος καὶ ἐπὶ χθονὶ δερκομένοιο | "while I live and upon the earth am looking" | "while I live and look upon the earth" | follows the Odyssey (odyssey-081, 16.439) |
| μάντις ἀμύμων | "the seer, blameless" | "the blameless seer" | Odyssey table, unchanged |
| ἑλικῶπις (1.98) | "quick-eyed" | "quick-eyed" (+ note: sense disputed) | "bright-eyed", "glancing-eyed", "dark-eyed", "with sparkling eyes" |
| ἀπριάτην ἀνάποινον (1.99) | "unbought, unransomed" | "unbought and with no ransom" | "without price, without ransom"; ἀπρίατος keeps the Odyssey's "unbought" |
| Ἀχαιοί · Δαναοί · Ἀργεῖοι | "Achaeans" · "Danaans" · "Argives" | "Achaeans" · "Danaans" · "Argives" | **departs from the Odyssey**, whose `i` renders Δαναοί as "Greeks": in the Iliad the three names alternate constantly and the reader should hear which one the poet used; "Greeks" is avoided in both layers |
| εὐρὺ κρείων (Ἀγαμέμνων, 1.102; printed as two words) | "wide-ruling" | "wide-ruling" | "of wide dominion", "far-ruling", "mighty lord"; εὐρύ is the adverb "widely" and κρείων "ruling", and the Odyssey table's "lord" for κρείων is kept for κρείων alone |
| κρείων Ἀγαμέμνων (1.130, reply-formula) | "lord Agamemnon" | "lord Agamemnon" | "king Agamemnon", "ruler"; follows the Odyssey table's κρείων "lord"; ἄναξ ἀνδρῶν stays "lord of men" and the two are told apart by context |
| κάκ’ ὀσσόμενος (1.105) | "evils foreboding" | "foreboding evil" (+ note: look vs. forebode) | "with evil in his eyes", "darkly", "looking daggers" (each decides the open question); follows the Odyssey's κακὰ ὄσσετο "evils foresaw" |
| μάντι κακῶν (1.106) | "Seer of evils" | "Seer of evils" | "prophet of doom", "prophet of ill"; μάντις stays "seer" |
| τὸ κρήγυον (1.106) | "the welcome thing" | "anything welcome" | "good" (reserved for ἐσθλός, in the next line but one), "true", "favourable"; sense "good, useful" in LSJ, origin unknown |
| γέρας (1.118 and on) | "prize" | "prize of honour" | "honour" alone, "reward", "share"; follows the Odyssey table's γέρας "prize" / "prize of honour" (11.175) and is kept the same at every occurrence |
| ἀγέραστος (1.119) | "prizeless" | "without one" (+ the prize of honour just named, in the same sentence) | "unrewarded", "empty-handed", "dishonoured" (reserved for ἄτιμος) |
| ποδάρκης δῖος Ἀχιλλεύς (1.121) | "swift-footed, heavenly Achilles" | "swift-footed, heavenly Achilles" (+ note: formation uncertain, probably πούς + ἀρκέω) | "fleet-footed" (reserved for ποδώκης), "swift of foot" (πόδας ὠκύς), "strong-footed", "sure-footed", "of the swift feet" |
| Ἀτρεΐδη κύδιστε φιλοκτεανώτατε πάντων (1.122) | "Atreus’-son, most glorious, most possession-loving of all" | "Son of Atreus, most glorious, most covetous of all" | "greediest of all", "grasping", "most avaricious" (loses κτέανα "possessions"); κύδιστε keeps the Odyssey's "most glorious" (Ἀτρεΐδη κύδιστε, 11.397) |
| μεγάθυμοι Ἀχαιοί (1.123) | "great-hearted Achaeans" | "great-hearted Achaeans" | "high-spirited", "stout-hearted"; follows the Odyssey's μεγάθυμος "great-hearted" |
| ξυνήϊα (1.124) | "common goods" | "common goods" | "common property", "shared stores", "public goods" |
| ἐπιτηδές (ἐρέτας ἐπιτηδὲς ἀγείρομεν, 1.142) | "suitably" | "suitable" (oarsmen) | "purposely", "on purpose" (the Odyssey’s rendering at 15.28, in an ambush; here the word qualifies a levy of rowers, "as needed"), "as required" |
| τριπλῇ τετραπλῇ τ’ ἀποτείσομεν (1.128) | "threefold and fourfold will pay back" | "will repay you three times over and four" | "three and four times as much", "a threefold and fourfold ransom" |
| ἐξαλαπάξαι (1.129) | "plunder utterly" | "plunder" | "sack" (kept for ἐκπέρθω / ἐκπέρσαι, 1.19 and 1.125), "storm", "destroy"; a departure from the Odyssey, which ships "sacked" for ἐξαλαπάξαι (3.85) and "laid waste" for ἀλαπάζω, because ἐκπέρθω and ἐξαλαπάξαι stand within five lines of each other here and the Iliad has already fixed "sack" for the first |
| εὐτείχεος (πόλιν Τροίην εὐτείχεον, 1.129) | "well-walled" | "well-walled" | "strong-walled", "fine-walled", "fortified" |
| θεοείκελ’ Ἀχιλλεῦ (1.131) | "god-resembling Achilles" | "Achilles, you who are like a god" | "godlike" (ἀντίθεος), "godlike in form" (θεοειδής), "equal to a god"; follows the Odyssey's θεοείκελος "god-resembling" / "who was like a god" |
| κλέπτε νόῳ (1.132) | "steal in mind" | "try to cheat … in your mind" (+ note: the Greek gives no object) | "hide your thoughts", "play the thief", "steal a march"; the verb is κλέπτω "steal" and the note says the intent is not stated |
| ἀναιδείην ἐπιειμένε (1.149) | "in shamelessness clothed" | "you clothed in shamelessness" | "wearing shamelessness like a cloak", "shameless to the bone"; ἐπιέννυμι keeps the Odyssey's "clothed in" (ἐπιειμένον, 9.214); ἀναιδής keeps "shameless" |
| κερδαλεόφρων (1.149) | "gain-minded" | "with your mind on gain" | "shrewd" and "profit-seeking" (the Odyssey's rendering of κερδαλέος, which does not suit a charge of greed), "greedy", "cunning" (reserved for μῆτις) |
| ἶφι μάχεσθαι (1.151) | "with force to fight" | "to fight … powerfully" | "to fight with all their might" ("mighty" is reserved for ἴφθιμος), "by force"; follows the table’s ἶφι ἀνάσσεις "powerfully rule" |
| αἰχμητής (Τρώων … αἰχμητάων, 1.152) | "spearmen" | "spearmen" | "warriors", "spear-fighters", "lance-bearers" |
| ἐριβώλακι βωτιανείρῃ (Φθίῃ, 1.155) | "rich-soiled, man-nourishing" | "rich-soiled nurse of men" | "fertile", "grain-bearing", "feeding heroes"; ἐριβῶλαξ keeps the Odyssey's "rich-soiled" |
| σκιόεντα … ἠχήεσσα (οὔρεά τε σκιόεντα θάλασσά τε ἠχήεσσα, 1.157) | "the shadowy mountains … the resounding sea" | same | "echoing", "loud" (kept for πολυφλοίσβοιο "loud-roaring"); σκιόεις keeps the Odyssey’s "shadowy" |
| κυνῶπα (vocative, 1.159) | "dog-faced one" | "you dog-face" | "shameless" in `i` (the Odyssey’s `i` for κυνῶπις, but ἀναιδές "shameless" stands one clause before), "bitch", "dog-eyed"; a departure from the Odyssey table, which pairs "dog-faced" in `l` with "shameless" in `i` |
| μέγ’ ἀναιδές (1.158) | "greatly shameless" | "utterly shameless" | "great shameless one", "most brazen"; ἀναιδής of persons keeps "shameless" |
| τιμὴν ἀρνύμενοι (1.159) | "winning honour" | "winning honour" (+ note: τιμή here is satisfaction owed) | "earning", "seeking revenge", "exacting redress" (each resolves τιμή) |
| υἷες Ἀχαιῶν (1.162) | "the sons of the Achaeans" | "the sons of the Achaeans" | "the Achaean men", "the Achaeans’ sons", "the Achaean warriors" |
| πολυάϊκος πολέμοιο (1.165) | "much-rushing war" | "onrushing war" (+ note: sense uncertain) | "tumultuous", "furious", "grim war" (each picks one guess) |
| ὀλίγον τε φίλον τε (1.167) | "a small thing and a dear one" | "something small though dear to me" | "small but welcome", "little but my own" |
| ἄφενος καὶ πλοῦτον (1.171) | "wealth and riches" | "wealth and riches" | "gain", "treasure", "plenty"; both nouns are wealth words and the translation keeps two |
| ἀφύξειν (1.171, ἀφύσσω) | "draw up" | "go on piling up" | "scoop", "ladle", "gather in" |
| τὸν δ’ ἠμείβετ’ ἔπειτα ἄναξ ἀνδρῶν Ἀγαμέμνων (1.172, whole-line reply-formula) | "Him then answered the lord of men, Agamemnon:" | "Then Agamemnon, lord of men, answered him:" | "answered" is kept for ἠμείβετο; follows the table’s τὸν/τὴν δ’ ἠμείβετ’ ἔπειτα and ἄναξ ἀνδρῶν Ἀγαμέμνων |
| φεῦγε μάλ’ (1.173) | "Flee, by all means" | "Flee, then, by all means" | "Run away", "Be off", "Go on, run" |
| οὐδ’ ὄθομαι κοτέοντος (1.181) | "nor do I heed you bearing a grudge" | "I take no heed of your resentment" | "I do not mind your anger"; ὄθομαι "heed", κοτέω "bear a grudge" (the Odyssey’s κοτεσσάμενος), κότος "resentment" |
| Μυρμιδόνεσσιν ἄνασσε (1.180) | "rule over the Myrmidons" | "be lord over the Myrmidons" | "reign among", "command"; ἀνάσσω keeps "be lord" (ἄναξ "lord") |
| Βρισηΐδα καλλιπάρῃον (1.184) | "Briseis, fair-cheeked" | "Briseis, fair-cheeked" | "fair-faced", "lovely-cheeked"; follows the Odyssey’s καλλιπάρῃος "fair-cheeked" (also used of Chryseis, 1.143) |
| ἀντάξιον (1.136) | "of equal worth" | "of equal worth" | "a fair exchange", "equivalent" |
| ἐκπαγλότατ’ ἀνδρῶν (1.146) | "most terrifying of all men" | "most terrifying of all men" | "most overpowering", "most formidable", "mightiest"; keeps the Odyssey’s ἔκπαγλος "terrifying" (10.448, 17.215) and now applies it to a man |
| στήθεσσιν λασίοισι (1.189) | "in his shaggy chest" | "in his shaggy chest" | "hairy", "rough"; λάσιος "shaggy, hairy" (LSJ) |
| διάνδιχα μερμήριξεν (1.189) | "in two ways was in doubt" | "was in doubt between two courses" | "pondered" (reserved for ὁρμαίνω, 1.193), "debated" (a speech-word), "was torn", "wavered" |
| χόλον παύσειεν ἐρητύσειέ τε θυμόν (1.192) | "stop his anger and restrain his heart" | "stop his anger and restrain his heart" | "master his rage", "hold back his spirit"; χόλος keeps "anger", θυμός "heart" |
| ἄμφω ὁμῶς θυμῷ φιλέουσά τε κηδομένη τε (1.196) | "both alike in heart loving and caring for" | "loving and caring for them both alike in her heart" | "equally dear to her", "cherishing"; φιλέω "love", κήδομαι "care for" |
| ἕλε Πηλεΐωνα (1.197) | "took the son of Peleus" | "took the son of Peleus" | "seized Achilles", "grasped"; Πηλεΐων keeps the Odyssey’s "the son of Peleus" |
| ξανθῆς κόμης (1.197) | "by the fair hair" | "by his fair hair" | "golden", "yellow", "red-gold" (ξανθός keeps the Odyssey’s "fair-haired") |
| οἴῳ φαινομένη (1.198) | "appearing to him alone" | "appearing to him alone" | "visible to him only", "showing herself" |
| θάμβησεν (1.199) | "was struck with wonder" | "was struck with wonder" | "was amazed" and "amazement" (reserved for τάφος), "was astonished"; keeps "wonder" for θάμβος / θαῦμα |
| δεινὼ δέ οἱ ὄσσε φάανθεν (1.200) | "and dread her two eyes shone" | "and her eyes shone dread" (+ note: οἱ "her" or "to him") | "terrible", "fearsome" (αἰνός), "formidable"; δεινός keeps "dread" |
| καί μιν φωνήσας ἔπεα πτερόεντα προσηύδα (1.201) | "and, lifting his voice, to her winged words he spoke:" | "and lifting his voice he spoke winged words to her:" | reused verbatim from odyssey-002 (the packet’s row); μιν is Athena here as in the Odyssey, so "to her" fits both |
| τίπτ’ αὖτ’ … εἰλήλουθας; (1.202) | "Why again, child of aegis-bearing Zeus, have you come?" | "Why have you come now, child of aegis-bearing Zeus?" | "Why have you come again" in `i` (the poem has no earlier visit); αἰγίοχος keeps "aegis-bearing"; Διὸς τέκος "child of Zeus" as the Odyssey table’s τέκος "child" |
| ᾗς ὑπεροπλίῃσι (1.205) | "by his own acts of arrogance" | "through his own arrogance" | "insolence" (reserved for ὕβρις), "overbearing pride"; the noun is built like the table’s ὑπεροπλίζομαι (sense uncertain) |
| θυμὸν ὀλέσσῃ (1.205) | "may lose his life" | "may … lose his life" | "lose his heart", "lose his spirit"; θυμός of the life that leaves the body is "life", as in the Odyssey table |
| ἦ καί (1.219, closing a speech and starting the action) | "He spoke, and" | "So he said, and" | "So saying", "With that", "And he said"; ἦ is the old "he said", kept apart from ὣς φάτο "so he spoke"; `i` follows the Odyssey table’s ἦ ῥα καί (8.416, "So he said, and") and its ἦ καί units (odyssey-070, -105, -106) |
| ἀταρτηροῖς ἐπέεσσιν (1.223; ἀταρτηρός rare, origin not known, ancient gloss "harmful, mischievous") | "harsh words" | "harsh words" (+ note: meaning not known) | "bitter", "savage", "cruel" (each picks one sense), "harmful" (decides the guess); the Odyssey ships "reckless" for the vocative ἀταρτηρέ of a man (2.243, odyssey-007), a different use, so "reckless words" is not carried over |
| δαίμονας ἄλλους (1.222, the other gods of Olympus) | "the other divinities" | "the other divinities" | "the other powers" (the Odyssey table’s δαίμων "some power" is for one unnamed god acting on a man; a collective "powers" would read as forces here), "gods" (reserved for θεός), "spirits"; a departure from the Odyssey table, with the reason |
| οἰνοβαρές (1.225, vocative; the Odyssey’s οἰνοβαρείων, 21.304) | "Heavy with wine" | "You who are weighed down with wine" | "drunkard", "sot", "wine-bibber"; follows the table’s "heavy with wine" / "weighed down with wine" |
| κυνὸς ὄμματ’ ἔχων, κραδίην δ’ ἐλάφοιο (1.225) | "with a dog’s eyes in you, and a deer’s heart" | "with the eyes of a dog and the heart of a deer" | "shameless eyes", "a coward’s heart" (each explains the image); κραδίη and θυμός both "heart" when three lines apart |
| τέτληκας (+ infinitive, 1.228) | "have you dared" | "you have never dared" | "endured" (kept for τλάω without an infinitive, as the Odyssey’s τέτλαθι κραδίη), "had the heart", "brought yourself" |
| κὴρ εἴδεται εἶναι (1.228) | "seems to be a death-spirit" | "looks like a spirit of death" | "fate", "doom" (reserved for μοῖρα, πότμος); follows the table’s κὴρ θανάτοιο "death-spirit" |
| δημοβόρος βασιλεύς (1.231) | "a people-devouring king" | "you king who devour your people" | "people-eater", "tyrant", "king who eats up his land" (δῆμος "land" in the Odyssey table is for the place; here it is the people) |
| λωβήσαιο (1.232, λωβάομαι) | "you would do outrage" | "the last outrage you committed" | "insult" (kept for the Odyssey’s λώβη with θυμαλγής), "abuse", "wrong"; follows the table’s "outrage" for the plain noun λώβη |
| ναὶ μὰ τόδε σκῆπτρον (1.234) | "Yes, by this sceptre" | "Yes, by this sceptre" | "I swear by this sceptre" (supplies a verb the Greek leaves out), "By this staff"; σκῆπτρον "sceptre" as in χρύσεον σκῆπτρον |
| τομήν (1.235, "the stump, the cut") · ἀναθηλήσει (1.236) | "stump" · "flourish again" | "stump" · "flourish again" | "cutting", "trunk" · "grow green again", "put out leaves" (the verb before has φύλλα already); ἀναθάλλω keeps the table’s τεθηλώς / τεθαλυῖα "flourishing" |
| δικασπόλοι (1.238, plural) | "the justice-tending" | "who dispense justice" | "judges", "lawgivers"; follows the table’s δικασπόλος "justice-tending" / "who dispenses justice" |
| ποθή (1.240, ποθὴ ἵξεται) | "a lack of Achilles" | "the lack of Achilles" | "longing", "yearning", "regret"; follows the table’s ξενίων ποθή "no lack of hospitality" |
| ἀνδροφόνος Ἕκτωρ (1.242) | "man-slaying Hector" | "man-slaying Hector" | "man-killer", "slayer of men", "murderous"; ἀνδροφόνος is ἀνήρ + φόνος, and "slaying" keeps the φόνος |
| ἡδυεπὴς … λιγὺς Πυλίων ἀγορητής (1.248) | "sweet-of-speech … clear-voiced speaker of the Pylians" | "sweet of speech … the clear-voiced speaker of the Pylians" | "sweet-talking", "honey-tongued", "orator", "shrill" (loses the table’s λιγύς "clear" in κήρυκες λιγύφθογγοι); ἀγορητής is "speaker", kept apart from ἀγορή "assembly" |
| μέλιτος γλυκίων … αὐδή (1.249) | "sweeter than honey … the voice" | "the voice flowed sweeter than honey" | "speech", "words" (the word is αὐδή, "voice, speech"); γλυκύς keeps the table’s "sweet" |
| κάρτιστοι (1.266–267) | "strongest" | "the strongest" | "mightiest" (reserved for ἴφθιμος / ἴφθιμοι), "best" (reserved for ἄριστος), "bravest"; follows the table’s καρτερός "strong" |
| φηρσὶν ὀρεσκῴοισι (1.268; ὀρεσκῷος "lying on the mountains", the usual explanation) | "the mountain-bedded beasts" | "the beasts of the mountains" (+ note: the Greek does not name the Centaurs) | "Centaurs" (names what the Greek leaves unnamed), "mountain-dwelling", "wild beasts of the hills"; follows the table’s αἶγες ὀρεσκῷοι "mountain goats" |
| ἐκπάγλως (1.268) | "terribly" | "terribly" | "terrifyingly" (the adverb is "terribly" in both layers in the Odyssey, odyssey-025 and -055; ἔκπαγλος itself stays "terrifying"), "mightily", "fiercely", "utterly" |
| ἐξ ἀπίης γαίης (1.270; ἀπίη disputed, "far-off" by the ancient explanation, "Apian" = Peloponnese by another) | "from a distant land" | "from a distant land" (+ note: sense not certain) | "from the Apian land", "from the Peloponnese" (each picks the other reading) |
| μεθομίλεον (1.269) | "I kept company" | "I joined their company" | "I mingled with", "I consorted with"; ὁμιλέω (1.261) stays "kept company with" |
| ξύνιεν (1.273, συνίημι with genitive) | "understood" | "took in" | "heeded" (kept for ὄθομαι), "attended to" (the Odyssey’s ξυνίει "attend"), "listened to"; the object is "counsels", which the verb takes in |
| ἀντιβίην (1.278) · ἀντιβίοισι ἐπέεσσιν (1.304) | "in opposition" · "words of opposition" | "in open opposition" · "opposing words" | "face to face" (reserved for ἀντίον), "head-on", "to his face" · "hostile words" |
| ἕρκος … πολέμοιο κακοῖο (1.283–284) | "fence … against evil war" | "bulwark … against evil war" | "protection", "shield", "wall"; `l` keeps the table’s ἕρκος ὀδόντων "fence", `i` takes the sense a defence needs |
| ὑποβλήδην (1.292) | "cutting in" | "cutting in" | "interrupting" (a plain-English summary), "from beneath", "retorting"; the word is formed on ὑποβάλλω and means taking up the other speaker’s words |
| ὡς ἔσεταί περ (1.211) | "just as it will be" | "just as it shall be" (+ note: obscure, usually "however it turns out") | "however it turns out", "as you please" (each fixes the obscure sense); the wording is the Odyssey’s for the same words (odyssey-104, the unit at line 212) |
| ἐμήνιε (1.247, μηνίω) | "was wrathful" | "was wrathful" | "raged", "was angry", "bore a grudge"; the verb of μῆνις "wrath", so it keeps the table’s family |
| εἰ δ’ ἄγε μήν (1.302) | "But come now, indeed" | "But come" | "If you dare", "Go on then"; εἰ is part of the idiom, not "if" |
| ἐΐσας (νῆας ἐΐσας, 1.306) | "well-balanced" | "well-balanced" (+ note: sense not certain) | "even", "trim", "shapely", "swift" (each picks a sense); keeps the table’s φρένας ἔνδον ἐΐσας "well-balanced wits" |
| ἀρχός (1.311, ἐν δ’ ἀρχὸς ἔβη πολύμητις Ὀδυσσεύς) | "leader" | "commander" | "captain", "chief" (reserved for ὄρχαμος), "lord"; kept apart from ἡγήτωρ and ἡγεμών, which are "leader" |
| ἀπίθησε μύθῳ (1.220) | "nor disobeyed the word" | "did not disobey the word" | "ignored", "defied"; ἀπιθέω is the opposite of πείθομαι "obey" |
| ἔα … γέρας (1.276, ἐάω with an unstated object) | "allow it" | "let it stand" | "leave her", "let her be" (supplies a person as the object) |
| ἄριστον Ἀχαιῶν (1.244) | "the best of the Achaeans" | "the best of the Achaeans" | "the finest", "the bravest"; follows the table’s ἀριστήεσσιν Ἀχαιῶν "the best of the Achaeans" |
| ἀέκων (ἀέκοντε βάτην 1.327, ἀέκουσ’ 1.348) | "unwilling" | "unwilling" | "reluctant", "against their will" (kept for the Odyssey’s ἀέκουσαν ἀπῶσαι, 2.130, where it is a plain phrase); follows the table’s οὐκ ἀέκοντε "not unwilling" |
| ὑγρὰ κέλευθα (1.312; the whole line οἱ μὲν ἔπειτ’ ἀναβάντες ἐπέπλεον ὑγρὰ κέλευθα is Odyssey 15.474, and its second half is 4.842) | "the watery ways" (the line: "They then, having embarked, sailed over the watery ways") | "the watery ways" (the line: "Then they embarked and sailed over the watery ways") | Odyssey table, unchanged; the line follows 15.474, where ἐπέπλεον is "sailed" (4.842 has "were sailing") |
| λύματα (1.314) | "the filth" | "the filth" | "off-scourings" (archaic), "pollution", "defilement"; LSJ "that which is washed off, filth" |
| κνίση (1.317) | "the savour" | "the savour of it" | "the smell of fat" (the Odyssey table’s κνίση 17.270; here the word stands alone and "savour" is what iliad-001 shipped at 1.66, so the Iliad keeps it), "steam" |
| ἑλισσομένη περὶ καπνῷ (1.317) | "curling about in the smoke" | "curling about in the smoke" | "whirling", "wreathing", "rising in coils" |
| τὰ πένοντο (1.318) | "were busied with these things" | "busied themselves with these tasks" | "toiled at", "laboured", "were occupied", "were busy"; πένομαι keeps the Odyssey’s "were busied" / "busied themselves" (4.624, 24.412, περὶ δεῖπνον … πένοντο) |
| λῆγ’ ἔριδος τὴν πρῶτον ἐπηπείλησ’ (1.319) | "cease from the strife which at first he threatened" | "give up the strife with which he had first threatened" | "quarrel" (kept for νεῖκος), "wrath" (reserved for μῆνις); ἔρις keeps "strife" as at 1.210 |
| ἐπαίτιος (1.335) | "to blame" | "to blame" | "guilty", "responsible", "at fault" |
| χαίρετε κήρυκες (1.334) | "Welcome, heralds" | "Welcome, heralds" | "Hail", "Greetings", "Rejoice"; follows the table’s χαῖρε, ξεῖνε "Welcome, stranger" |
| Διὸς ἄγγελοι ἠδὲ καὶ ἀνδρῶν (1.334) | "messengers of Zeus and also of men" | "messengers of Zeus and of men as well" | "envoys", "ambassadors"; ἄγγελος is "messenger" |
| ἀπηνής (βασιλῆος ἀπηνέος, 1.340; origin not known, LSJ "harsh, rough, cruel") | "unkind" | "unkind" | "ungentle" (the first draft; the Odyssey fixes "unkind" for ἀπηνής at 18.381, 19.329, 23.97 and 23.230), "harsh" (kept for ἀταρτηροῖς ἐπέεσσιν, 1.223, and reserved for χαλεπός), "cruel", "pitiless", "stern" |
| ἀεικέα λοιγὸν ἀμῦναι (1.341, 1.398) | "to ward off unseemly ruin" | "to ward off unseemly ruin" | "shameful ruin", "ugly destruction", "plague" (λοιγός is "ruin"; the Odyssey’s βροτολοιγός "mortal-ruining"); ἀεικής keeps the table’s "unseemly", ἀμύνω "ward off" |
| ὀλοιῇσι φρεσὶ θύει (1.342) | "in baleful wits, rages" | "rages with a baleful mind" | "destructive", "murderous", "ruinous" (reserved for οὐλόμενος), "in a fatal frenzy"; ὀλοός keeps the "baleful" of the table’s ὀλοόφρων; θύω is "rush, seethe, rage" as in the table’s θῦεν "seethed" |
| ἅμα πρόσσω καὶ ὀπίσσω (1.343) | "at once forward and backward" | "what lies ahead and what lies behind" | follows the Odyssey (24.452, ὅρα πρόσσω καὶ ὀπίσσω "saw what lay ahead and what lay behind") |
| ὅππως … σόοι μαχέοιντο (1.344) | "how … the Achaeans may fight safe" | "how the Achaeans may fight safely" | "unharmed", "in safety" in `l`; "safe" keeps the Odyssey’s σόος |
| ὣς φάτο δάκρυ χέων, τοῦ δ’ ἔκλυε πότνια μήτηρ (1.357) | "So he spoke, a tear shedding, and him heard his lady mother" | "So he spoke, shedding tears, and his lady mother heard him" | "weeping" (drops χέων), "queenly mother"; table patterns ὣς ἔφατ’ εὐχόμενος, τοῦ δ’ ἔκλυε Φοῖβος, δάκρυ χέων, πότνια "lady" |
| καρπαλίμως δ’ ἀνέδυ πολιῆς ἁλὸς ἠΰτ’ ὀμίχλη (1.359) | "swiftly she rose up out of the grey sea like a mist" | same | "emerged", "came up"; ἠΰτε is "like" (the Odyssey’s ἠΰτε πέτρη, "like a rock"); πολιὴ ἅλς keeps "grey sea" |
| χειρί τέ μιν κατέρεξεν ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε (1.361, female subject) | "and stroked him with her hand, and spoke a word, and called him by name:" | "and stroked him with her hand, and spoke, calling him by name:" | Odyssey table (4.610), unchanged, with the female subject as shipped at Odyssey 5.181 |
| τέκνον τί κλαίεις; (1.362) | "Child, why do you weep?" | "Child, why are you weeping?" | "My son", "Why do you cry" (τέκνον is "child", not "son"); τέκνον keeps the table’s "child" |
| κεῦθε νόῳ (1.363) | "hide it in your mind" | "keep it hidden in your mind" | "conceal your thoughts", "hold it back"; νόος is "mind" |
| τὴν δὲ βαρὺ στενάχων προσέφη πόδας ὠκὺς Ἀχιλλεύς (1.364, whole-line reply-formula) | "Her, groaning heavily, addressed swift-in-feet Achilles:" | "Groaning heavily, Achilles, swift of foot, said to her:" | "sighing deeply", "with a heavy groan", "answered"; βαρὺ στενάχων keeps the Odyssey’s βαρέα στενάχοντα "groaning heavily"; πόδας ὠκύς and προσέφη as in the table |
| τί … ταῦτα ἰδυίῃ πάντ’ ἀγορεύω; (1.365) | "why indeed to you, knowing these things, do I tell it all?" | "Why should I tell it all to you, who know it already?" | "declare" (kept for ἀγορεύω in a public declaration, 1.385 and iliad-002), "recount"; τοι is read as σοι because ἰδυίῃ is dative |
| ἱερὴν πόλιν (1.366) | "the sacred city" | "the sacred city" | "holy" (reserved for ἠγάθεος / ζάθεος), "hallowed"; ἱερός keeps "sacred" |
| διεπράθομεν (1.367) | "we sacked" | "sacked" | "plundered", "destroyed"; "sack" is the Iliad’s word (ἐκπέρθω, 1.19), and the Odyssey has διεπράθετο "was sacked" |
| ἤγομεν ἐνθάδε πάντα (1.367) | "brought here everything" | "brought everything here" | "carried off", "plundered"; ἄγω of spoil is "bring" |
| εὖ δάσσαντο (1.368) | "divided well among themselves" | "divided the spoil well among themselves" | "shared out fairly", "apportioned"; δατέομαι is "divide", with the middle shown by "among themselves" |
| ἑκατηβόλου Ἀπόλλωνος (1.370) beside ἑκηβόλου Ἀπόλλωνος (1.373) | "far-shooting" · "far-shooting" | "who shoots from afar" · "far-shooting" | "far-darting" (reserved for ἑκατηβελέτης), "far-working" (ἑκάεργος); the Odyssey’s ἑκατηβόλος is kept, so the two epithets differ only in `i` |
| ἑκάτοιο (1.385; ἕκατος, a short form, probably the root of ἑκατηβόλος and ἑκατηβελέτης) | "of the far-darter" | "of the far-darter" (+ note: sense of ἕκατος alone not certain) | "of the far-shooter" (kept for ἑκηβόλος), "of the far-worker" (ἑκάεργος), "of Hecatus" |
| ἐπασσύτεροι (1.383) | "one close upon another" | "one close upon another" | "thick and fast", "in heaps", "in droves", "one after another"; the form looks like a comparative and the sense given is the traditional one |
| ἐπῴχετο κῆλα θεοῖο (1.383) | "the shafts of the god went about" | "the god’s shafts went about" | "ranged over" (decides the verb’s sense), "swept"; ἐποίχομαι is "go about, go among" as in the Odyssey’s κῆρυξ ἐπῴχετο "came round" |
| βέλος (ἧκε κακὸν βέλος, 1.382) | "an evil shaft" | "an evil shaft" | "missile" and "arrow" (the Odyssey ships both for βέλος, which iliad-001 did not carry over: it ships "shaft" at 1.51 for βέλος ἐχεπευκές, and this part follows iliad-001), "dart" |
| εὖ εἰδὼς ἀγόρευε θεοπροπίας (1.384–385) | "who knew well declared the prophecies" | "who knew well declared … the prophecies" | "spoke out", "uttered"; ἀγορεύω in a public pronouncement is "declare", as at 1.109 in iliad-002 |
| κελόμην … ἱλάσκεσθαι (1.386) | "urged to appease" | "was the first to urge that … be appeased" | "bade", "propitiate" (kept for ἱλάσσεαι in iliad-002), "placate"; κέλομαι keeps the Odyssey’s "bid / order" family, "urge" for advice |
| Ἀτρεΐωνα (1.387) | "Atreus’-son" | "the son of Atreus" | "Atreion", "Atreides"; the -ίων patronymic is the same man as Ἀτρεΐδης |
| ἠπείλησεν μῦθον (1.388) | "threatened a word" | "uttered a threat, a word" | "made a threat" alone (loses μῦθον); ἀπειλέω keeps "threaten" as at 1.319 |
| ὃ δὴ τετελεσμένος ἐστί (1.388) | "has indeed been fulfilled" | "has now been fulfilled" | "has come true", "has been accomplished"; τελέω keeps "fulfil" as in the table’s Διὸς δ’ ἐτελείετο βουλή |
| ἑλίκωπες Ἀχαιοί (1.389) | "the quick-eyed Achaeans" | "the quick-eyed Achaeans" (+ note: sense disputed) | "bright-eyed", "glancing-eyed", "dark-eyed", "with rolling eyes"; masculine form of the table’s ἑλικῶπις "quick-eyed" |
| κούρην Βρισῆος (1.392) | "the girl of Briseus" | "the girl, the daughter of Briseus" | "Briseus’ daughter" in `l` (decides how to read the genitive); κούρη is "girl", Βρισηΐς "daughter of Briseus" by its formation |
| περίσχεο παιδὸς ἑῆος (1.393) | "protect your own son" | "protect your own son" (+ note: ἑῆος also read as ἐΰς "good") | "shield", "cover", "stand over"; "your good son" (decides the open reading); ἑός is "own" as in the Odyssey’s possessive ὅς |
| λίσαι (λίσσομαι, 1.394) | "beg" | "beg" | "beseech", "entreat" (the Odyssey ships "begging" for λίσσετο and "entreated" for ἐλλίσσετο; iliad-001 has "begged" at 1.15), "supplicate" |
| ὤνησας κραδίην Διὸς … ἔπει … ἔργῳ (1.394–395) | "helped the heart of Zeus … by a word … by a deed" | "helped the heart of Zeus, whether by word or by deed" | "pleased", "gladdened" (each decides ὀνίνημι), "served"; κραδίη is "heart" |
| πολλάκι γάρ σεο … ἄκουσα εὐχομένης (1.396–397) | "many a time … I heard you boasting" | "I have often heard you … boasting" | "praying" (εὔχομαι is "pray" in iliad-001, but with ἔφησθα it is "claim, boast"), "vowing" |
| κελαινεφέϊ Κρονίωνι (1.397) | "the dark-clouded son of Cronus" | "the son of Cronus of the dark clouds" | Odyssey table’s κελαινεφής "dark-clouded" / "of the dark clouds", unchanged |
| ξυνδῆσαι (1.399) | "to bind together" | "to bind" | "to fetter", "to chain", "to bind fast"; δέω is "bind" |
| Βριάρεων · Αἰγαίων’ (1.403–404) | "Briareus" · "Aegaeon" | "Briareus" · "Aegaeon" | "Briareos", "Aigaion"; the Latinised forms, as for the other Greek names |
| ἑκατόγχειρον (1.402) | "the hundred-handed one" | "the hundred-handed one" | "hundred-armed", "of the hundred hands", "Hundred-Hander" |
| ὦχ’ (ὦκα, 1.402) | "quickly" | "quickly" | "swiftly" (reserved for καρπαλίμως and ὠκύς), "at once" (αὐτίκα) |
| μακρὸν Ὄλυμπον (1.402) | "tall Olympus" | "tall Olympus" | "long" (the Odyssey’s literal line once has "long Olympus" beside "tall Olympus" elsewhere; "tall" is the form it ships in both layers), "great", "high" |
| ὑπελύσαο δεσμῶν (1.401) | "set free from his bonds" | "set him free from his bonds" | "released", "loosed from under"; λύω keeps "release / set free" as in the table’s λύσαιτε |
| κύδεϊ γαίων (1.405) | "exulting in glory" | "exulting in his glory" | "rejoicing in his fame", "proud of his glory"; κῦδος is "glory" as in the table’s κύδιστε "most glorious" |
| τὸν καὶ ὑπέδεισαν μάκαρες θεοὶ οὐδ’ ἔτ’ ἔδησαν (1.406) | "him even the blessed gods feared, and no longer bound" | "even the blessed gods were afraid of him, and did not go on to bind Zeus" | "trembled before", "gave up", "dared not bind"; μάκαρες θεοί keeps "blessed gods" (+ note: the object, Zeus, is not in the Greek) |
| ἐπὶ Τρώεσσιν ἀρῆξαι (1.408) | "to help the Trojans" | "to help the Trojans" | "to aid", "to side with"; ἀρήγω is "help" |
| ἔλσαι … κτεινομένους (1.409–410) | "to hem in … being killed" | "to hem in … as they are killed" | "to drive back", "to press", "to pen"; εἴλω keeps "hem in" |
| ἵνα πάντες ἐπαύρωνται βασιλῆος (1.410) | "so that all may have the benefit of their king" | "so that all of them may have the benefit of their king" | "enjoy", "taste", "reap the reward" (ἐπαυρίσκομαι is neutral in sense and bitter in tone; the note says so), "suffer from" |
| ἣν ἄτην (1.412) | "his own bewilderment" | "his own bewilderment" | "blind folly" (turned down in the Odyssey table), "ruin", "madness", "delusion"; follows the Odyssey’s ἄτη "bewilderment" |
| ὅ τ’ ἄριστον Ἀχαιῶν οὐδὲν ἔτισεν (1.412) | "that the best of the Achaeans he honoured not at all" | "that he paid no honour at all to the best of the Achaeans" | reused from iliad-003 (1.244, ἔτισας), person changed |
| κατὰ δάκρυ χέουσα (1.413, feminine of the table’s δάκρυ χέων) | "down a tear shedding" | "shedding tears" | "weeping" (drops χέω), "pouring down tears"; κατά is tmesis for κατα-χέω, "pour down", and δάκρυ keeps the table’s "tear(s)" |
| αἰνὰ τεκοῦσα (1.414, αἰνά neuter plural as adverb) | "dreadfully having borne" | "when I had borne you in such dread" (+ note: whose dread is not said) | "to a dreadful fate", "in sorrow", "to misery" (each decides whose dread it is); αἰνός is "dread" |
| αἴθ’ ὄφελες + infinitive (1.415) | "Would that you ought … to sit" | "If only you were sitting" | "You should have stayed" (a rebuke the Greek does not make); ὄφελες is ὀφείλω "ought", kept apart from ὀφέλλω "increase" (1.510); follows the Odyssey’s ὡς ὄφελες "Would that / If only" |
| ἀδάκρυτος καὶ ἀπήμων (1.415) | "tearless and unharmed" | "without tears and unharmed" | "free of grief", "untroubled", "harmless" (the Odyssey table’s plural ἀπήμονες of escorts); ἀπήμων of a person keeps "unharmed" (10.551) |
| αἶσα (1.416, 1.418, κακῇ αἴσῃ) | "portion" · "an evil portion" | "lot" · "an evil lot" | "fate", "doom" (reserved for μοῖρα, πότμος, μόρος); follows the table’s δαίμονος αἶσα κακή "an evil lot from some power" |
| μίνυνθά περ οὔ τι μάλα δήν (1.416) | "for a little while, not very long at all" | "only a little while, not long at all" | "short though it be", "brief" alone; the `l` is the Odyssey’s (odyssey-110, "not very long at all"), but its `i` "though not for long at all" is not followed because there περ is read as a concession the Greek does not make |
| ὠκύμορος · ὠκυμορώτατος (1.417, 1.505, of Achilles) | "swift-doomed" · "most swift-doomed" | "swift to your doom" · "the swiftest of all to his doom" | "short-lived" (μινυνθάδιος), "doomed to die soon", "ill-fated" (ἄποτμος); the Odyssey’s plural ὠκύμοροι is "swift-doomed" in `l` and "meet a swift doom" in `i`, so the root keeps "swift … doom" |
| ὀϊζυρός (1.417, of a man) | "sorrowful" | "a man of sorrow" | "wretched" (reserved for δύστηνος), "miserable"; keeps the Odyssey’s "sorrowful" (20.140) |
| τερπικέραυνος (Ζεύς, 1.419) | "delighting-in-the-thunderbolt" | "who delights in the thunderbolt" | "thunder-loving", "who hurls the thunderbolt", "of the joyous lightning"; τέρπω "delight", κεραυνός "thunderbolt" (the Odyssey’s ἀργὴς κεραυνός "bright thunderbolt"); kept apart from εὐρύοπα "far-thundering" and ὑψιβρεμέτης "who thunders on high" |
| ἀγάννιφος (Ὄλυμπος, 1.420) | "very snowy" | "snowy" (+ note: formation not quite certain) | "snow-capped", "snow-clad", "deep in snow"; ἀγα- is the intensifier of the table’s ἀγακλυτός "renowned" |
| ὠκύπορος (νηυσὶ … ὠκυπόροισι, 1.421, 1.488) | "swift-faring" | "swift-faring" | "swift ships" (drops πόρος), "fast-sailing", "fleet"; keeps the Odyssey’s "swift-faring" (ὠκύποροι νῆες) |
| μήνιε (μηνίω, 1.422, 1.488) | "be wrathful" · "was wrathful" | "be wrathful" · "sat in wrath" | "rage", "be angry", "nurse your anger"; μηνίω is the verb of μῆνις "wrath" and keeps the family of ἐμήνιε "was wrathful" (1.247) |
| πάμπαν (1.422) | "altogether" | "altogether" | "entirely", "at all" (the Odyssey’s "not at all" is for negative contexts), "utterly" |
| ἀμύμονας Αἰθιοπῆας (1.423) | "the blameless Ethiopians" | "the blameless Ethiopians" | "noble", "peerless", "faultless"; ἀμύμων keeps "blameless" as in μάντις ἀμύμων |
| χθιζός (1.424) | "yesterday" | "yesterday" | "of yesterday", "only yesterday"; the adjective used as an adverb, as the Odyssey’s χθιζὸς θεὸς ἤλυθες "yesterday … came" |
| δωδεκάτῃ · δυωδεκάτη ἠώς (1.425, 1.493) | "on the twelfth" · "the twelfth dawn" | "on the twelfth day" · "the twelfth dawn" | "twelve days later", "after twelve days" (each loses the ordinal and what is counted from) |
| γουνάσομαι (1.427) | "I will entreat" | "entreat" | "I will clasp his knees" (the gesture is shown at 500), "I will supplicate", "beseech"; follows the table’s γουνάζομαι "I entreat" |
| ἐϋζώνοιο γυναικός (1.429) | "the well-girdled woman" | "the well-girdled woman" | "fair-girdled", "slim-waisted", "fair-belted", "deep-girdled"; ἐΰ- is "well" as in ἐϋκνήμιδες "well-greaved", and ζώνη "girdle" |
| ἀέκοντος ἀπηύρων (1.430) | "from him unwilling, they took away" | "taken from him by force, unwilling as he was" | "against his will" (kept for plain phrases, as in the table’s ἀέκων row), "robbed"; ἀπαυράω is "take away", as in the Odyssey (ἀπηύρα "took away") |
| ἱστοδόκη (1.434) | "the mast-holder" | "its holder" (+ note: the rest on which the lowered mast lies) | "mast-crutch", "mast-rest", "mast-box"; the word is ἱστός "mast" + δέχομαι "receive" |
| ὑφέντες (1.434, ὑφίημι) | "lowering" | "lowered" | "slackening", "letting down gently"; ἱστόν … προτόνοισιν is "the mast … with the forestays", the table’s πρότονοι "forestays" |
| ἐκ … βῆσαν (1.438, transitive aorist of βαίνω) | "made go" | "led … out" | "disembarked" (intransitive), "landed", "set ashore"; the note says the verb is transitive here |
| ἐΰδμητος (βωμόν, 1.448) | "well-built" | "well-built" | "well-made" (reserved for ἐυεργής), "fine-built", "well-fashioned"; ἐΰ- is "well", δέμω "build" |
| ἑξείης (1.448) | "in order" | "in order" | "in a row", "in rank", "one after another" (kept for ἐπασσύτεροι) |
| μεγάλ’ εὔχετο (1.450) | "loudly prayed" | "prayed loudly" | "greatly prayed", "prayed mightily", "boasted" (εὔχομαι is "pray" in iliad-001; the table’s "claim, boast" is for ἔφησθα with a past tense and does not apply here) |
| πολύστονα κήδεα (1.445) | "much-groaning sorrows" | "sorrows that bring many a groan" | "tearful", "woeful" (reserved for the table’s οἰζυρός family), "lamentable"; πολύστονος is πολύς + στόνος "groan"; κήδεα keeps the table’s "sorrows" |
| ἴψαο (ἴπτω, 1.454) | "greatly struck" | "struck … hard" (+ note: rare verb, traditional sense) | "smote", "afflicted", "oppressed", "plagued" (each names the plague the Greek does not name) |
| ἦ μὲν δή (1.453) | "Truly indeed" | "Truly" | "Surely", "Indeed, once"; ἦ μέν is the asseverative |
| ἠδ’ ἔτι καὶ νῦν (1.455) | "and still, even now" | "and further, even now" | "now once more", "and yet again"; ἔτι is "further, still" |
| ἤδη νῦν (1.456) | "even now" | "even now" | "now at last", "at once", "this very day" |
| αὐέρυσαν (1.459) | "drew back" | "drew the victims’ heads back" (+ note: the Greek has no object, the heads are supplied) | "lifted up the victims’ heads", "pulled back", "drew up"; the Odyssey does not have the line, and αὐερύω is "draw back" |
| κνίσῃ ἐκάλυψαν (1.460, dative of the covering) beside κνίση (1.317) | "covered them over with fat" | "covered them with fat" | "with the savour" (kept for κνίση, the smell rising to heaven, 1.317), "with caul-fat", "with the omentum"; reused from the Odyssey (odyssey-060) |
| μῆρε κάη (1.464, μῆρε looks like a dual) | "the thigh-pieces were burned up" | "the thigh-pieces were burned up" | "the two thigh-bones", "the pair of thighs"; the line differs from the Odyssey’s μῆρ’ ἐκάη only in the form μῆρε, and the English is the Odyssey’s (the note says the form looks like a dual) |
| πάσαντο (σπλάγχνα, 1.464) | "had tasted" | "had tasted" | "ate", "had eaten of", "devoured"; reused from the Odyssey |
| ἐΐσης (δαιτὸς ἐΐσης, 1.468) | "equal" | "equally shared" | "fair", "balanced" (reserved for ἐΐσας of ships), "well-apportioned"; reused from the Odyssey |
| μολπῇ · μέλποντες (1.472, 1.474) | "with song and dance" · "celebrating" | "with song and dance" · "celebrating" | "with singing", "with music", "dancing", "hymning"; μολπή keeps the table’s "song and dance" (6.101) and μέλπω shares its root |
| παιήων (1.473) | "paean" | "paean" | "hymn", "song of praise", "healing song"; the word is the name of the song and the note gives it as a song to Apollo |
| ἑκάεργον · ἑκάεργος (1.474, 1.479) | "the far-working one" · "far-working" | "the god who works from afar" · "who works from afar" (+ note: meaning disputed) | "far-shooting" (ἑκηβόλος), "far-darting" (ἑκατηβελέτης), "the archer"; follows the Odyssey table’s ἑκάεργος |
| ἠέλιος κατέδυ καὶ ἐπὶ κνέφας ἦλθε (1.475) | "the sun set and darkness came on" | "the sun set and darkness came on" | "night fell", "the sun went down"; reused from the Odyssey (odyssey-040) |
| κοιμήσαντο (1.476) | "lay down to sleep" | "lay down to sleep" | "went to sleep", "slept", "bedded down"; the aorist middle is "put themselves to sleep", as the Odyssey’s κοιμήθημεν "we lay down to sleep" |
| ἀνάγοντο (1.478) | "put out to sea" | "put out to sea" | "set sail", "were led up", "launched"; keeps the Odyssey’s "put out to sea" (ἀνάγοντο) |
| εὐρὺν στρατὸν Ἀχαιῶν (1.478, 1.484) | "the wide army of the Achaeans" | "the wide army of the Achaeans" | "broad host", "the vast army", "the Achaean host"; εὐρύς is "wide" as in εὐρὺ κρείων "wide-ruling", and στρατός is "army" |
| ἴκμενον οὖρον (1.479, without πλησίστιον) | "a favouring wind" | "a favouring wind" | "a fair wind" (reserved for οὖρος ἀπήμων τε λιαρός τε), "following wind"; the table’s ἴκμενον οὖρον … πλησίστιον adds "that filled the sail" in `i` for the word that is absent here |
| ἐν … πρῆσεν μέσον ἱστίον (1.481) | "filled the middle of the sail" | "filled the belly of the sail" | "swelled", "blew into", "bellied the sail"; follows the Odyssey (2.427) |
| πορφύρεον (κῦμα, 1.482) | "surging" | "surging" | "purple", "dark", "crimson"; keeps the Odyssey’s "surging" for the same line |
| διαπρήσσουσα κέλευθον (1.483) | "accomplishing the way" | "completing her way" | "making her way", "cutting through", "finishing her voyage"; follows the Odyssey’s διαπρήσσωσι κέλευθον "accomplish the way", with ὑγρά κέλευθα "ways" unchanged |
| ἕρματα (1.486, ὑπὸ δ’ ἕρματα μακρὰ τάνυσσαν) | "props" | "props" | "supports", "rollers", "ballast", "earrings" (the Odyssey’s ἕρματα at 18.297); ἕρμα is "what holds fast", and the note gives the sense used here |
| νέας (νῆας, 1.487) | "the ships" | "the ships" | "new" (the adjective νέος), "the new huts"; the form is the accusative plural of ναῦς |
| διογενής (1.489) | "Zeus-sprung" | "Zeus-born" | "god-born", "of divine birth", "born of Zeus"; the same pair as iliad-004 (Patroclus, 1.337) and the Odyssey’s "Zeus-sprung" |
| πωλέσκετο · φθινύθεσκε · ποθέεσκε (1.490–492, iterative -σκ-) | "did he go" · "kept wasting" · "kept longing" | "never went" · "kept wasting away" · "longed for" | "used to", "would", "was wasting"; the iterative suffix is shown by "kept" in `l`, and the note names it |
| ἀγορὴν κυδιάνειραν (1.490) | "the man-glorifying assembly" | "the assembly that brings men glory" | "glory-giving", "ennobling", "that raises men"; κυδιάνειρα is κῦδος + ἀνήρ, and the Iliad’s ἀγορή keeps "assembly" |
| φθινύθω φίλον κῆρ (1.491) | "wasting his dear heart" | "wasting away his dear heart" | "eating his heart out", "consuming his heart", "his own heart"; κῆρ is "heart" and φίλον "dear" as in the Odyssey’s φίλον ἦτορ |
| ἀϋτήν τε πτόλεμόν τε (1.492) | "the battle-cry and … war" | "the battle-cry and … war" | "the shout", "the clash", "the din of battle"; πτόλεμος is the epic πόλεμος "war" |
| θεοὶ αἰὲν ἐόντες (1.494) | "the gods who are forever" | "the gods who are forever" | Odyssey table, unchanged |
| ἐφετμέων (1.495) | "commands" | "commands" | "behests", "bidding", "orders"; keeps the Odyssey’s "commands" (ἐφετμέων, 17.353), and the note says they are Achilles’ requests |
| ἀνεδύσετο κῦμα θαλάσσης (1.496) | "rose up out of the wave of the sea" | "rose up out of the wave of the sea" | "emerged from", "dived up from", "rose from the swell"; ἀναδύομαι "rise up out of", as the Odyssey’s ἀνεδύσετο λίμνης "rose up from the water" |
| ἠερίη (1.497) | "morning-early" | "early in the morning" (+ note: sense not certain, "in the mist" another reading) | "misty", "through the mist", "at dawn" (each decides the open question) |
| εὐρύοπα Κρονίδην (1.498) | "far-thundering the son-of-Cronus" | "the son of Cronus, who thunders from afar" | "wide-voiced", "far-seeing"; the table’s εὐρύοπα Ζεύς "far-thundering" with the doubt noted, and Κρονίδης "son-of-Cronus" |
| πολυδειράς (Ὄλυμπος, 1.499) | "many-ridged" | "many-ridged" | "many-peaked", "long-ridged", "of many valleys", "ridge on ridge"; πολυ- "many", δειράς "ridge" |
| ἀκροτάτῃ κορυφῇ (1.499) | "on the topmost peak" | "on the topmost peak" | "highest", "uppermost", "the very summit"; ἄκρος "top" in the superlative, κορυφή "peak" |
| σκαιῇ · δεξιτερῇ … ὑπ’ ἀνθερεῶνος ἑλοῦσα (1.501) | "with her left hand" · "with her right, taking him under the chin" | "with her left hand" · "with her right hand under his chin" | "left-handed", "by the beard"; ἀνθερεών is "chin", and the Odyssey’s δεξιτερῇ "with his right hand" |
| λάβε γούνων (1.500) | "took hold of his knees" | "took hold of his knees" | "clasped his knees", "grasped"; follows iliad-004 (λαβὲ γούνων "take hold of his knees", 1.407) |
| Δία Κρονίωνα ἄνακτα (1.502) | "Zeus, the son of Cronus, the lord" | "lord Zeus, the son of Cronus" | "king Zeus", "ruler"; Κρονίων keeps "the son of Cronus" and ἄναξ "lord" |
| Ζεῦ πάτερ (1.503) | "Zeus father" | "Father Zeus" | "O Zeus, my father", "Zeus the father"; the vocative, as the Odyssey’s πάτερ ἡμέτερε "Father of us all" |
| ὄνησα · ἢ ἔπει ἢ ἔργῳ (1.503–504) | "I helped" · "either by a word or by a deed" | "I helped" · "whether by word or by deed" | "benefited", "served"; follows iliad-004 (ὤνησας "helped", ἔπει … ἔργῳ "by a word … by a deed", 1.394–395) |
| τίω · τῖσον · τίσωσιν (1.508, 1.510) | "honour" · "shall honour" | "honour" · "honour" | "avenge", "pay back", "repay", "reward"; the verb of ἔτισεν (1.412); "pay" would be τίνω and the note says the form could be read that way |
| ὀφέλλωσιν (1.510) | "shall increase" | "increase" | "exalt", "magnify", "help"; ὀφέλλω keeps the Odyssey’s "increase / grow" (ὀφέλλετο "grew") and is kept apart from ὀφείλω "ought" (1.415) |
| κράτος (ἐπὶ Τρώεσσι τίθει κράτος, 1.509) | "strength" | "strength" (+ note: may include the upper hand) | "victory", "the upper hand", "power", "might" (reserved for μένος / ἴς); the Odyssey ships "strength" for κράτος (1.70) |
| τόφρα δέ … ὄφρ’ ἂν (1.509) | "and meanwhile … until" | "and in the meantime … until" | "so long … as", "all the while until"; τόφρα is "for that time" and the pair makes the duration |
| τὴν δὲ μέγ’ ὀχθήσας προσέφη νεφεληγερέτα Ζεύς (1.517, whole-line speech introduction) | "Her, greatly vexed, addressed cloud-gatherer Zeus:" | "Greatly troubled, Zeus who gathers the clouds said to her:" | "angered", "much troubled", "grieved"; follows the Odyssey table’s νεφεληγερέτα Ζεύς and προσέφη "addressed / said to" |
| ὀχθέω (ὀχθήσας 1.517, ὄχθησαν 1.570) | "vexed" · "were vexed" | "troubled" · "were troubled" (the Odyssey’s) | "grieved", "indignant"; ὀχθέω is a mood of annoyance, so one English word serves Zeus and the gods |
| λοίγια ἔργα (1.518, 1.573; λοιγός "ruin", 1.341) | "ruin-bringing deeds" | "a disastrous business" | "ruinous" (reserved for οὐλόμενος), "baneful", "deadly deeds"; the same rendering at both places because Hephaestus repeats Zeus’ words |
| ἐχθοδοπῆσαι ἐφήσεις (1.518; ἐχθοδοπέω rare, "be at enmity") | "you will set me to be at enmity" | "you will set me at odds" | "make me quarrel", "pit me against", "make an enemy of me"; ἐφίημι "send upon, set to" as in the table’s χεῖρας ἐφήσεις "lay hands" |
| ἣ δὲ καὶ αὔτως (1.520) | "and she, even just so" | "even without cause" | "needlessly", "for nothing at all", "in vain"; αὔτως "just so, without ground" |
| νεικεῖ (1.521) | "rebukes" | "is … rebuking" | "scolds", "reviles", "taunts"; keeps the Odyssey’s νεικέω "rebuke" (νείκεσε "reviled" is reserved for the stronger verb with ἄντην) |
| κατανεύω · νεῦσε · κατανεύσομαι · κατάνευσον (1.514, 1.524, 1.527, 1.528, 1.558) | "nod assent" · "nodded" | "nod (one’s) assent" · "nodded" | "grant", "promise" (ὑπίσχομαι), "agree", "consent"; the verb is νεύω "nod" with κατά "down, in assent" |
| νημερτές (1.514, neuter adverb) | "unerringly" | "truly" | "without fail" (loses νημερτής "unerring" of the Odyssey), "frankly", "honestly" |
| ἀπόειπε (1.515, ἀπεῖπον) | "refuse" | "refuse" | "deny", "say no" (too colloquial), "renounce"; ἀπο- "away" + εἰπεῖν |
| ἀτιμοτάτη θεός (1.516) | "the most dishonoured goddess" | "the most dishonoured goddess" | "least honoured", "most slighted", "most unhonoured"; ἄτιμος "dishonoured", as ἀτιμάζω is "dishonour" |
| τέκμωρ (1.526) | "sign" | "sign" | "pledge" and "token" (each decides the sense), "end" (the Odyssey ships "end" for τέκμωρ at 4.373 and 4.466, where the word is the goal or way out of a predicament; here it is a sign given, so the Odyssey’s rendering is not carried over) |
| παλινάγρετον · ἀπατηλὸν · ἀτελεύτητον (1.526–527) | "can be taken back" · "deceptive" · "unfulfilled" | "taken back" · "prove false" · "go unfulfilled" | "revocable", "treacherous" (reserved for δολόεις), "unaccomplished" (reserved for τελέω "accomplish", 1.523) |
| ἦ καὶ κυανέῃσιν ἐπ’ ὀφρύσι νεῦσε Κρονίων (1.528) | "He spoke, and on his dark brows nodded the son of Cronus;" | "So he said, and the son of Cronus nodded with his dark brows;" | "black brows", "dark-blue brows", "frowning" (a nod is not a frown); ἦ καί as the table’s "He spoke, and" / "So he said, and"; κυάνεος "dark" |
| ἀμβρόσιαι χαῖται ἐπερρώσαντο (1.529) | "ambrosial locks streamed forward" | "the ambrosial locks … streamed forward" | "swayed" (turned down in the Odyssey table for ἐπερρώοντο), "rippled", "shook", "were stirred"; ἀμβρόσιος keeps "ambrosial" |
| ἐλέλιξεν (1.530) | "shook" | "shook" | "made tremble", "set quaking", "rocked"; ἐλελίζω "make quiver, shake" |
| τώ γ’ ὣς βουλεύσαντε διέτμαγεν (1.531, duals) | "The two, having so taken counsel, parted;" | "Having made their plan in this way, the two parted;" | "agreed", "plotted", "conspired"; βουλεύω "take counsel, plan", the dual kept as "the two" |
| ἠγνοίησεν ἰδοῦσ’ (1.536–537) | "did not fail to recognize" | "did not fail to know" | "was not ignorant", "was not unaware", "failed to notice" (reverses the sense of ἀγνοιέω), "did not miss"; follows odyssey-022 (5.77); double negative kept |
| συμφράσσατο βουλάς (1.537, 1.540) | "devised plans" | "had been devising plans" · "has been devising plans" | "plotted", "schemed"; συμφράζομαι "devise together"; βουλή "plan", but "will" avoided as in the table’s Διὸς βουλή |
| ἀργυρόπεζα Θέτις θυγάτηρ ἁλίοιο γέροντος (1.538, 1.556) | "silver-footed Thetis, daughter of the old man of the sea" | "silver-footed Thetis, the daughter of the old man of the sea" | "Nereus’ daughter" (names who the Greek does not name); Odyssey table’s ἀργυρόπεζα Θέτις "silver-footed Thetis" and ἁλίοιο γέροντος "the old man of the sea"; the same words at both places |
| κερτομίοισι … προσηύδα (1.539) | "with taunting ones she spoke to" | "she spoke … with taunts" | "mocking words" (the Odyssey table’s `l` for κερτομίοισι is "with taunting ones"), "sneers"; προσαυδάω "speak to" |
| δολομῆτα (1.540, vocative) | "you of guileful counsel" | "you of guileful counsel" | "schemer", "crafty one", "wily"; δολόμητις "of guileful counsel" is the Odyssey’s rendering of Aegisthus’ epithet |
| κρυπτάδια φρονέοντα δικαζέμεν (1.542) | "thinking secret things, to give judgement" | "to think your secret thoughts and pass judgement on them" | "to plot in secret" (loses δικάζω), "to decide alone", "to scheme"; δικάζω "give judgement" |
| ἐπιέλπεο … εἰδήσειν (1.545–546) | "do not hope … to know" | "do not hope to know" | "do not expect", "do not presume"; ἐλπίζω family is "hope" |
| πατὴρ ἀνδρῶν τε θεῶν τε (1.544, whole-line reply-formula) | "Her then answered the father of men and of gods:" | "Then the father of men and of gods answered her:" | follows the Odyssey table’s πατὴρ ἀνδρῶν τε θεῶν τε and the Iliad’s τὴν δ’ ἠμείβετ’ ἔπειτα |
| βοῶπις πότνια Ἥρη (1.551, 1.568; βοῶπις "ox-eyed") | "ox-eyed lady Hera" | "ox-eyed lady Hera" (+ note: usual explanation, large calm eyes) | "cow-eyed", "ox-faced", "large-eyed", "queenly Hera"; βοῶπις = βοῦς + ὤψ; πότνια "lady" as the Odyssey table’s πότνια νύμφη |
| τὸν δ’ ἠμείβετ’ ἔπειτα βοῶπις πότνια Ἥρη (1.551, whole-line reply-formula) | "Him then answered ox-eyed lady Hera:" | "Then ox-eyed lady Hera answered him:" | "white-armed" (λευκώλενος, a different epithet, 1.595), "queen Hera" |
| αἰνότατε (1.552) | "most dread" | "most dreadful" | "most terrible", "most fearsome", "most awful"; αἰνός "dread" as at 1.414; vocative, sharp rather than respectful |
| ποῖον τὸν μῦθον ἔειπες; (1.552) | "what sort of word is this you have spoken?" | "what kind of word is this that you have spoken?" | "what do you mean", "what is that you say"; ἔειπες "have spoken" (aorist) |
| καὶ λίην … πάρος γ’ (1.553) | "Truly, before now at least" | "Truly, until now" | "Indeed far too much" (reads λίην with the verb), "I have never"; καὶ λίην is an intensifier |
| εὔκηλος (1.554) | "at ease" | "quite at your ease" | "calmly", "untroubled", "quietly" (reserved for ἀκέων "in silence"); adjective as adverb |
| φράζεαι (1.554) | "plan" | "plan" | "ponder", "consider" (φράζομαι also means these, but the sense here is plan); "devise" reserved for συμφράσσατο |
| παρείπῃ (1.555) | "win you over" | "has talked you round" | "persuade" (reserved for πείθω), "beguile", "cajole"; παρεῖπον "win over with words", as the stem of παράφημι "advise" |
| ὀΐω · ὀΐεαι (1.558, 1.561) | "I suspect" · "you suspect" | "I suspect" · "you are always suspecting" | "I think", "I guess"; follows the Odyssey’s ὀϊόμεθα / ὀΐομαι "suspect" |
| ἐτήτυμον (1.558) | "in truth" | "in truth" | "truly" (reserved for ἦ μάλα / ἦ μέν), "really", "for certain" |
| ἀπὸ θυμοῦ … ἐμοὶ ἔσεαι (1.562–563) | "from my heart … you will be to me" | "will only be the farther from my heart" | "out of my favour", "dearer", "less dear"; θυμός "heart" |
| ἐμοὶ μέλλει φίλον εἶναι (1.564) | "it is sure to be dear to me" | "it must be what pleases me" | "so be it" (adds a phrase the Greek lacks), "it is bound to please me"; μέλλω + infinitive for what is bound to happen |
| ἐπιγνάμψασα φίλον κῆρ (1.569) | "having bent her dear heart" | "having forced her dear heart to yield" | "swallowed her anger", "curbed her spirit", "mastered her feelings"; ἐπιγνάμπτω "bend", κῆρ "heart" |
| Ἥφαιστος κλυτοτέχνης (1.571) | "Hephaestus, famous in craft" | "Hephaestus, famous in craft" | "renowned craftsman" (table’s own avoided), "the master smith"; keeps the Odyssey table’s κλυτοτέχνης "famous in craft" |
| τοῖσιν δ’ Ἥφαιστος κλυτοτέχνης ἦρχ’ ἀγορεύειν (1.571, whole-line speech introduction) | "and among them Hephaestus, famous in craft, began to speak," | "and Hephaestus, famous in craft, was the first to speak among them," | "addressed", "began to harangue"; follows the Odyssey table’s ἦρχ’ ἀγορεύειν "began to speak" / "was the first to speak" |
| ἐπίηρα φέρων · ἐπίηρα φέρειν (1.572, 1.578) | "bringing pleasing things" · "to bring pleasing things" | "trying to please" · "to please" | "bringing a kindness", "doing a favour", "offering comfort"; ἐπίηρος "pleasing", φέρω "bring" |
| οὐδ’ ἔτ’ ἀνεκτά (1.573) | "no longer bearable" | "no longer to be borne" | "intolerable", "unendurable"; follows the Odyssey table’s ἀνεκτός ("bearable" in `l`) |
| ἐριδαίνετον (1.574, dual) | "you two … quarrel" | "you two quarrel" | "contend", "wrangle", "fight"; ἐριδαίνω "quarrel" as the Odyssey table’s ἐριδαίνομεν |
| κολῳὸν ἐλαύνετον (1.575; κολῳός rare) | "an uproar you two drive on" | "keep an uproar going" | "brawl", "tumult" (each picks a degree), "stir up trouble"; ἐλαύνω "drive" |
| μητρὶ δ’ ἐγὼ παράφημι (1.577) | "I give counsel" | "I advise" | "I urge", "I tell", "I persuade"; παράφημι "advise, speak to persuade" |
| νεικείῃσι … σὺν … ταράξῃ (1.579) | "may rebuke, … confound" | "may not rebuke again and throw … into confusion" | "scold", "upset", "ruin the feast"; ταράσσω "stir up, confuse" |
| Ὀλύμπιος ἀστεροπητής (1.580, 1.609) | "the Olympian, the lightning-flasher" | "the Olympian who flashes lightning" | "lord of lightning", "the thunderer" (reserved for ὑψιβρεμέτης "high-thundering"), "lightning-hurler"; ἀστεροπητής from ἀστεροπή "lightning" |
| στυφελίξαι (1.581) | "thrust" | "drive" | "hurl", "strike", "knock"; στυφελίζω "strike hard, thrust out" |
| φέρτατος (1.581) | "by far the best" | "by far the best of us" (+ note: "of us" is supplied) | "the strongest" (κάρτιστοι), "the mightiest" (ἴφθιμοι); keeps the Odyssey’s πολὺ φέρτατος "by far the best"; the note says the sense is power |
| ἵλαος (1.583) | "gracious" | "gracious" | "kindly", "propitious", "merciful"; the adjective of ἱλάσκομαι "appease" |
| ὣς ἄρ’ ἔφη καὶ ἀναΐξας … καί μιν προσέειπε (1.584–585) | "So then he spoke, and having sprung up, … and addressed her:" | "So he spoke, and sprang up and … said to her:" | "leapt up" (kept for ἀναπηδάω); follows the Odyssey table’s ἀναΐξας "having sprung up" / "sprang up" |
| τέτλαθι · ἀνάσχεο (1.586) | "Endure" · "hold out" | "Endure it" · "bear up" | "be patient", "put up with it"; τέτλαθι keeps the Odyssey’s "Endure"; ἀνέχομαι "hold out" |
| κηδομένη περ (1.586) | "grieved though you are" | "worried as you are" | "though you care", "caring for him"; κήδομαι "care for" (1.196) is here "be distressed" |
| θεινομένην (1.588) | "being struck" | "being struck" | "beaten", "hit", "smitten"; θείνω "strike" |
| ἀργαλέος … ἀντιφέρεσθαι (1.589) | "hard … to oppose" | "hard to stand against" | "to resist" (reserved for ἀνθίστημι), "to fight"; ἀργαλέος "hard" (the Odyssey’s ἀργαλέος) |
| ἀλεξέμεναι μεμαῶτα (1.590) | "eager to defend" | "eager to defend you" (+ note: no object in the Greek) | "to help", "to ward off", "to protect"; ἀλέξω "ward off, defend" |
| ῥῖψε ποδὸς τεταγών (1.591) | "flung, seizing me by the foot" | "seized me by the foot and flung me" | "hurled", "threw", "grabbed", "caught"; ῥίπτω "fling" |
| βηλοῦ θεσπεσίοιο (1.591) | "the wondrous threshold" | "the wondrous threshold" | "the divine threshold" (θεῖος), "marvellous"; θεσπέσιος keeps the Odyssey’s "wondrous" |
| κάππεσον … ὀλίγος δ’ ἔτι θυμὸς ἐνῆεν (1.593) | "I fell … little life was still in me" | "I fell … little life still in me" | "a little breath", "little spirit"; θυμός of the life that leaves the body is "life" |
| κομίσαντο (1.594) | "took care of" | "took care of" | "took me in", "received", "tended"; κομίζω "take care of" |
| ὣς φάτο, μείδησεν δὲ θεὰ λευκώλενος Ἥρη (1.595) | "So he spoke, and smiled the goddess, white-armed Hera," | "So he spoke, and the goddess, white-armed Hera, smiled," | follows the Odyssey table’s ὣς φάτο, μείδησεν δὲ … pattern |
| παιδὸς … χειρὶ κύπελλον (1.596) | "from her son, with her hand, the cup" | "the cup from her son’s hand" | "goblet" (reserved for ἄλεισον), "chalice"; κύπελλον "cup", of the δέπας ἀμφικύπελλον "double cup" of 584 |
| ἐνδέξια (1.597) | "towards the right" | "going round to the right" | "from left to right" (reads the direction the other way), "in order"; as the Odyssey (17.365) |
| οἰνοχόει … νέκταρ (1.598) | "poured sweet nectar" | "poured sweet nectar for all the other gods" | "served as cupbearer", "ladled"; οἰνοχοέω "pour wine" |
| ἀφύσσων (1.598) | "drawing" | "drawing" | "scooping", "ladling"; ἀφύσσω "draw up" |
| ἄσβεστος … γέλως (1.599) | "unquenchable laughter" | "laughter that would never go out" | reused from the Odyssey (8.326), unchanged |
| ποιπνύοντα (1.600) | "bustling" | "bustling" | "hurrying", "scurrying", "limping" (adds the lameness the Greek leaves implicit); keeps the Odyssey’s "bustling" |
| ἐδεύετο (1.602) with the genitives of 603–604 | "did the heart lack" · "nor yet of the … lyre" | "went short of nothing" · "nor did they lack" | "was without", "wanted"; the first half is the published iliad-005 wording, the genitives carry the same verb |
| ἀμειβόμεναι ὀπὶ καλῇ (1.604) | "answering one another with a beautiful voice" | "answering one another in beautiful voice" | "singing in turns", "with sweet voices", "responding"; ἀμείβομαι "answer", ὄψ "voice" |
| λαμπρὸν φάος ἠελίοιο (1.605) | "the bright light of the sun" | "the bright light of the sun" | "the radiance", "the brilliant sun"; λαμπρός "bright" |
| οἳ μὲν κακκείοντες ἔβαν οἶκον δὲ ἕκαστος (1.606; οἶκον δέ printed as two words) | "they, to lie down going, went home, each one," | "they went off home to bed, each of them," | the Odyssey’s κακκείοντες ἔβαν οἶκόνδε ἕκαστος "to lie down going … each one went to his own house" / "went off home to bed", with οἶκον δέ "homewards" |
| ἧχι ἑκάστῳ δῶμα … ποίησεν (1.607–608) | "where for each a house … had made" | "to the place where … had made each a house" | "built" (reserved for δέμω), "fashioned"; ποιέω "make" |
| περικλυτὸς ἀμφιγυήεις Ἥφαιστος (1.607–608) | "the very-famous both-limbed one, Hephaestus" | "the very famous both-limbed god, Hephaestus" (+ note: meaning unknown) | Odyssey table, unchanged |
| ἰδυίῃσι πραπίδεσσι (1.608) | "with knowing wits" | "with his skilled wits" | Odyssey (7.92), unchanged; πραπίδες "wits" |
| Ζεὺς δὲ πρὸς ὃν λέχος ἤϊ’ (1.609) | "and Zeus to his own bed went" | "Zeus … went to his own bed" | "his own couch", "his chamber"; ὅς the possessive "his own" |
| ἔνθα καθεῦδ’ ἀναβάς (1.611) | "there he slept, having mounted" | "There he went up and slept" | "climbed into bed", "lay down"; ἀναβαίνω "go up"; καθεύδω "sleep" |
| χρυσόθρονος Ἥρη (1.611) | "golden-throned Hera" | "golden-throned Hera" (+ note: θρόνα alternative) | "golden-flowered" as if certain, "gold-enthroned"; extends the Odyssey table’s χρυσόθρονος |
| ἱπποκορυσταί (ἀνέρες ἱπποκορυσταί, 2.1) | "horse-arming" | "armed with horses" (+ note: whether chariot-fighters or horsehair-crested helmets is not known) | "charioteers", "horse-helmeted", "crested with horsehair" (each picks one guess); built on ἵππος + κορύσσω "arm, equip" |
| οὖλον ὄνειρον · οὖλε ὄνειρε (2.6, 2.8) | "a ruinous Dream" · "ruinous Dream" | "a ruinous Dream" · "ruinous Dream" | "baneful", "deadly", "evil" ; οὖλος keeps the "ruinous" of οὐλομένην (1.2); ὄνειρος is capitalised as a being sent and addressed; θεῖος ὄνειρος (2.22) is "the divine Dream", and "Dream" stays capitalised when Agamemnon speaks of it (2.56); "the dream" in lower case is the thing told, in Nestor’s speech (2.80) |
| καί μιν φωνήσας ἔπεα πτερόεντα προσηύδα (2.7; departure from 1.201) | "and, lifting his voice, to it winged words he spoke:" | "And lifting his voice he spoke winged words to the Dream:" | "to her" (the published English of 1.201, where μιν is Athena; here μιν is the masculine Dream); only the pronoun changes, and the unit is joined to the two lines before it so that the validator’s whole-unit rule does not force the wrong pronoun |
| βάσκ’ ἴθι (2.8) | "Go, set out" | "Be off with you" | "Run", "Hasten", "Away with you quickly" (adds speed the pair does not state); βάσκε + ἴθι are two imperatives |
| πανσυδίῃ (2.12, 2.29, 2.66) | "with-all-rush" | "with all speed" (+ note: "in full force" also possible) | "in full force", "in a body", "all together" (each picks one sense); πᾶς + σεύομαι "rush" |
| ἀμφὶς … φράζονται (οὐ γὰρ ἔτ’ ἀμφὶς Ὀλύμπια δώματ’ ἔχοντες ἀθάνατοι φράζονται, 2.13–14 = 2.30–31 = 2.67–68, whole line) | "for no longer apart, who hold the Olympian halls, the immortals plan;" | "for the immortals who hold the halls of Olympus no longer plan apart from one another;" | "in two minds", "in two camps", "divided" (each reads ἀμφίς as a faction); follows the table’s Ὀλύμπια δώματ’ ἔχοντες |
| ἐπέγναμψεν … λισσομένη (2.14, 2.31, 2.68) | "bent them all, Hera, entreating" | "Hera, entreating them, has swayed them all" | "talked them round", "won them over", "persuaded"; ἐπιγνάμπτω is "bend" |
| κήδε’ ἐφῆπται (2.15, 2.32, 2.69) | "sorrows are fastened" | "sorrows have been fastened upon" | "woes hang over", "cares are laid"; κήδεα keeps the table’s "sorrows" |
| θωρήσσω (θωρῆξαι 2.11, 2.28, 2.65, 2.72) | "to arm" | "arm" | "put on armour", "gather"; the verb is "arm" at every occurrence |
| κέλευε · κέλευσε (2.11, 2.28) | "bid" · "has bidden" | "bid" · "has bidden" | "tell", "order" (reserved for κέλευσε at 2.50, where "ordered" is used with the heralds as in the Odyssey’s same line) |
| ἀτρεκέως (2.10) | "very exactly" (πάντα μάλ’ ἀτρεκέως) | "very exactly" | follows the table’s ἀτρεκέως "exactly" |
| ἐπιτέλλω (ὡς ἐπιτέλλω, 2.10) | "as I enjoin" | "as I charge you" | "command", "bid" (reserved for κελεύω), "as I order"; ἐπιτέλλω keeps "enjoin / lay a charge" as in ἔτελλε (1.25) |
| ἱπποδάμοιο (Ἀτρέος … ἱπποδάμοιο, 2.23) | "horse-taming" | "tamer of horses" | follows the table’s ἱππόδαμος Νέστωρ; δαΐφρονος keeps "wise-minded" / "wise-hearted" from the table’s δαΐφρων row |
| βουληφόρον ἄνδρα (2.24) | "a man who bears counsel" | "a man who bears counsel" | "counsellor", "councillor" (as in the table’s Φαιήκων βουληφόροι, which names a group); here the phrase qualifies a single ἀνήρ and the two parts are kept visible |
| ξύνες ὦκα (2.26) | "give heed quickly" | "listen to me, and quickly" | "hear me" (reserved for κλῦθί μευ); συνίημι is "take in, give heed to" |
| Διὸς … ἄγγελός εἰμι (2.26) | "of Zeus … a messenger I am" | "I am a messenger of Zeus" | "envoy"; follows the table’s ἄγγελος "messenger" |
| μέγα κήδεται ἠδ’ ἐλεαίρει (2.27) | "greatly cares for and pities" | "cares greatly for … and pities" | "is concerned for … and has compassion on"; κήδεται keeps the "care" of κήδεα "sorrows" in the same family; ἐλεαίρω is "pity" |
| μελίφρων ὕπνος (2.34) | "honey-hearted sleep" | "heart-sweetening sleep" (+ note: sense uncertain) | "honey-sweet" (reserved for μελιηδής), "mellow"; extends the table’s μελίφρων οἶνος "honey-hearted wine" / "heart-sweetening wine" to ὕπνος |
| νήδυμος ὕπνος (2.2) | "sweet sleep" | "sweet sleep" (+ note: meaning not known) | follows the table’s νήδυμος ὕπνος; γλυκὺς ὕπνος (2.71) is also "sweet sleep" in English and the note keeps them apart |
| ἀμβρόσιος ὕπνος · ἀμβροσίη νύξ (2.19, 2.57) | "ambrosial sleep" · "the ambrosial night" | same | "divine sleep" (reserved for θεῖος), "heavenly" (δῖος); keeps "ambrosial" of ἀμβρόσιος (1.529) |
| κλισίη (2.9, 2.19) | "hut" | "hut" | "tent"; follows the Iliad’s earlier "hut" and the Odyssey’s κλισίη (14.194) |
| τὸν … τῖ’ Ἀγαμέμνων (τόν ῥα μάλιστα γερόντων τῖ’, 2.21) | "whom most of the elders Agamemnon honoured" | "the one of all the elders whom Agamemnon honoured most" | "esteemed", "respected"; τίω is "honour" |
| ὑπὲρ κεφαλῆς (στῆ δ’ ἄρ’ ὑπὲρ κεφαλῆς, 2.20, 2.59) | "stood above his head" | "stood above his head" | "at his head", "over his head" in the sense of "beyond" |
| ἐεισάμενος (τῷ μιν ἐεισάμενος, 2.22) | "having made himself like to him" | "making himself like" | "taking the form of", "disguising himself as", "assuming the shape"; εἴδομαι + ἐοικώς are kept as "like" |
| ἀπεβήσετο (ὣς ἄρα φωνήσας ἀπεβήσετο, 2.35) | "So then, having spoken, he went away" | "With these words he went away" | follows the table’s ὣς ἄρα φωνήσας ἀπέβη pattern ("So then having spoken …" / "So he spoke …"); not a stock speech-ending in the Odyssey table, so the English is chosen here |
| νήπιος (2.38, narrator’s comment) | "foolish" | "foolish as he was" | follows the table’s νήπιος "foolish" |
| θήσειν … ἄλγεά τε στοναχάς τε (2.39) | "lay both pains and groans" | "lay pains and groans" | "sufferings and lamentations"; ἄλγεα keeps "pains" |
| θείη ὀμφή (2.41) | "the divine voice" | "the divine voice" | "heavenly" (δῖος), "god-sent"; ὀμφή is a voice with a god behind it |
| νηγάτεος (χιτῶνα … νηγάτεον, 2.43; formation not known) | "new-made" | "newly made" (+ note: ancient gloss; formation not known) | "fresh-woven", "gleaming", "unworn" (each picks a sense) |
| ποσσὶ δ’ ὑπὸ λιπαροῖσιν ἐδήσατο καλὰ πέδιλα (2.44) | "and under his sleek feet he bound fine sandals" | "he bound fine sandals beneath his sleek feet" | reused from the Odyssey; the clause is not a whole unit here, so only the sentence frame differs |
| ξίφος ἀργυρόηλον (2.45) | "the silver-studded sword" | "the silver-studded sword" | "silver-nailed", "silver-hilted"; follows the Odyssey’s 8.406 |
| σκῆπτρον πατρώϊον ἄφθιτον αἰεί (2.46) | "the sceptre of his fathers, unfailing for ever" | "his fathers’ sceptre, which never fails" | "undying", "imperishable"; ἄφθιτος keeps the table’s "unfailing" (ἄφθιτοι ἄμπελοι) |
| ἠὼς … θεά (2.48) | "Dawn, the goddess" | "Dawn, the goddess" | "the dawn goddess"; Ἠώς is capitalised when she moves and speaks |
| φόως ἐρέουσα (2.49) | "light to announce" | "to announce the light" | "to bring light" (that is φόως φέροι, Od. 5.2), "to proclaim", "to speak"; ἐρέουσα is a future participle "about to say" and its sense is uncertain |
| κηρύκεσσι λιγυφθόγγοισι κέλευσε κηρύσσειν ἀγορὴν δὲ κάρη κομόωντας Ἀχαιούς (2.50–51) | "But he to the clear-voiced heralds gave-command to summon to assembly the long-haired-of-head Achaeans" | "But he ordered the clear-voiced heralds to summon the long-haired Achaeans to assembly" | the Odyssey’s αἶψα δὲ … form (2.6–7), with "At once" replaced by "But he" for αὐτὰρ ὃ |
| οἳ μὲν ἐκήρυσσον, τοὶ δ’ ἠγείροντο (2.52) | "They made-proclamation, and the others gathered very quickly;" | "The heralds made the proclamation, and the people gathered very quickly;" | "were roused", "mustered"; the Odyssey’s wording (2.8 = 2.52 here), kept unchanged |
| βουλὴν … ἷζε (2.53) | "a council … he seated" | "he seated a council" | "made sit", "convened"; ἷζε is transitive |
| Πυλοιγενής (2.54) | "Pylos-born" | "born at Pylos" | "Pylos-bred", "Pylian"; -γενής is "born" |
| πυκινὴν … βουλήν (2.55) | "close-packed plan" | "shrewd plan" | "thick counsel", "dense", "solid" (reserved for πυκινὸς δόμος); here πυκινή is read as "shrewd" and the note says so |
| ἀρτύνετο (2.55) | "arranged" | "set out" | "prepared", "contrived"; ἀρτύνω is "arrange, put in order" |
| κλῦτε φίλοι (2.56) | "Hear, friends" | "Hear me, friends" | "Listen" ; as shipped in odyssey-070; κλύω is "hear" |
| ἐνύπνιον (2.56) | "in sleep" | "in my sleep" | "in a vision", "as a dream" (that is ὄνειρος) |
| εἶδός τε μέγεθός τε φυήν τ’ ἄγχιστα ἐῴκει (2.58) | "in form and in size and in stature it most nearly resembled" | "most nearly in form, in size and in stature" | follows the Odyssey’s εἶδός τε μέγεθός τε φυήν τ’ ἄγχιστα ἐΐσκω ("in form and in size and in stature most nearly liken") |
| ὣς ὃ μὲν εἰπὼν ᾤχετ’ ἀποπτάμενος (2.70–71) | "So he, having spoken, went off flying away" | "With that he was gone, flying away" | "flew off", "vanished"; οἴχομαι is "be gone", ἀποπέτομαι "fly away" |
| ἀλλ’ ἄγετ’ αἴ κέν πως θωρήξομεν υἷας Ἀχαιῶν (2.72 = 2.83, whole line) | "But come, if in any way we might arm the sons of the Achaeans" | "But come, let us see if we can arm the sons of the Achaeans" | "perhaps we can"; αἴ κέν πως is "if somehow" and the English must hold both times (Agamemnon, then Nestor); υἷες Ἀχαιῶν keeps the table’s "the sons of the Achaeans" |
| ἔπεσιν πειρήσομαι, ἣ θέμις ἐστί (2.73) | "with words will make trial, as is the custom" | "make trial of them with words, as is the custom" | "test", "put to the test" (each sets the outcome), "as is lawful", "as is proper"; follows the table’s θέμις "custom"; πειράω is "make trial of" |
| πολυκλήϊσι (νηυσὶ πολυκλήϊσι, 2.74) | "many-thwarted" | "of many thwarts" | follows the shipped Odyssey wording (odyssey-102: "ships of many thwarts") |
| ἄλλοθεν ἄλλος ἐρητύειν ἐπέεσσιν (2.75) | "from different sides, each one, hold them back with words" | "each from a different quarter, must hold them back with words" | "one after another"; the infinitive stands for an imperative; ἐρητύω "hold back, restrain" as in the table’s ἐρητύσειε |
| Ἀργείων ἡγήτορες ἠδὲ μέδοντες (2.79) | "leaders and lords of the Argives" | "the leaders and lords of the Argives" | "rulers and counsellors", "chiefs and princes"; follows the table’s Φαιήκων ἡγήτορες ἠδὲ μέδοντες, with Ἀργείων named as the Iliad does |
| ψεῦδός κεν φαῖμεν καὶ νοσφιζοίμεθα μᾶλλον (2.81) | "a falsehood we should call it and turn away from it all the more" | "we should call it a falsehood and the rather turn away from it" | "lie", "reject outright", "shun"; ψεῦδος is "falsehood" and νοσφίζομαι "turn away from" |
| εὔχεται εἶναι (ὃς μέγ’ ἄριστος Ἀχαιῶν εὔχεται εἶναι, 2.82) | "by far the best of the Achaeans claims to be" | "claims to be by far the best of the Achaeans" | "boasts to be", "prides himself on being" (adds tone); "prays" (the other sense of εὔχομαι) |
| ὣς ἄρα φωνήσας βουλῆς ἐξῆρχε νέεσθαι (2.84) | "So then having spoken, he led the way from the council, to go," | "So he spoke, and led the way out of the council," | "led the council out", "rose to depart"; ὣς ἄρα φωνήσας keeps the Odyssey's "So then having spoken" |
| ἔθνεα (2.87 of bees; 2.91 of men) | "tribes" | "swarms" (both places) | "companies", "hosts"; the word is kept the same in `l` and echoed in `i`, as the simile needs |
| ἁδινάων (μελισσάων ἁδινάων, 2.87) | "thronging" | "thronging" | "murmuring", "swarming", "restless"; ἁδινός is "thick, crowded" (the Odyssey table's ἁδινόν "heavily" is the adverb of the same word) |
| ὄσσα … Διὸς ἄγγελος (2.93, lower-case in the edition) | "a rumour" … "a messenger of Zeus" | "a rumour" … "a messenger of Zeus" | "Rumour" with a capital (kept for the edition's capitalised Ὄσσα at 24.413), "voice", "report"; ἄγγελος keeps the table's "messenger" |
| σπουδῇ (ἕζετο λαός, 2.99) | "with difficulty" | "with difficulty" | "in haste", "eagerly"; the note says σπουδή can also mean haste |
| κρείων Ἀγαμέμνων (2.100) | "lord Agamemnon" | "lord Agamemnon" | follows the table's κρείων Ἀγαμέμνων row, unchanged |
| Ἥφαιστος … κάμε τεύχων (2.101) | "Hephaestus toiled making" | "Hephaestus had toiled to make" | "wrought", "fashioned with labour" (loses κάμνω "toil") |
| διάκτορος ἀργεϊφόντης (2.103, dative) | "the guide, Argeïphontes" | "the guide, the slayer of Argus" | follows the table's διάκτορος and ἀργεϊφόντης rows (8.338 pattern) |
| πληξίππος (Πέλοπι πληξίππῳ, 2.104) | "horse-lashing" | "the horse-lasher" | "charioteer", "horse-driving", "horse-taming" (reserved for ἱππόδαμος), "driver of horses" |
| πολύαρνι (Θυέστῃ, 2.106) | "rich in lambs" | "rich in lambs" | "rich in flocks", "lamb-rich"; ἀρήν is "lamb" |
| ἥρωες Δαναοὶ θεράποντες Ἄρηος (2.110) | "heroes, Danaans, attendants of Ares" | "Danaan heroes, attendants of Ares" | "servants of Ares" (reserved for δμῶες), "squires", "henchmen"; θεράπων keeps the table's "attendant" |
| ἄτῃ … βαρείῃ (2.111) | "in bewilderment … heavy" | "in heavy bewilderment" | "blind folly", "ruin", "delusion"; ἄτη keeps the table's "bewilderment" |
| σχέτλιος (nominative, of Zeus, 2.112) | "cruel one" | "cruel one" | "relentless", "stubborn", "pitiless"; follows the table's σχέτλιος "cruel" |
| δυσκλέα (2.115) | "inglorious" | "without glory" | "disgraced", "ill-famed", "shamed" |
| κάρηνα … κατέλυσε … λύσει (2.117–118) | "has undone the heads … will undo" | "has overthrown the heads … will overthrow more" | "razed the towers", "taken the citadels" (replaces κάρηνα "heads" with a guess); κατέλυσε / λύσει kept as one verb |
| κράτος … μέγιστον (2.118) | "the strength is greatest" | "his strength is greatest" | "power", "might"; follows the table's κράτος "strength" (1.509) |
| μὰψ οὕτω (2.120) | "in vain, so" | "to no purpose" | "idly", "for nothing"; the sense is that the war has had no result |
| ἄπρηκτον πόλεμον πολεμίζειν (2.121) | "a fruitless war to war" | "a fruitless war" | "unavailing", "useless"; the noun and the verb come from one root and `l` keeps both |
| ὅρκια πιστὰ ταμόντες (2.124) | "faithful oaths having cut" | "to swear faithful oaths" | follows the Odyssey's "faithful oaths having cut" / "faithful oaths sworn" |
| ἐφέστιοι (2.125) | "hearth-holders" | "all who have homes in the city" | "householders", "native", "resident"; the Greek is "at the hearth" |
| δεκάδες … οἰνοχόοιο (2.126–128) | "tens … a wine-pourer" | "tens … a cupbearer" | follows the table's οἰνοχόος "wine-pourer" / "cupbearer" |
| ἐγχέσπαλοι (2.131) | "spear-brandishing" | "spear-brandishing" (+ note: formation uncertain) | "spear-wielding", "famed for the spear", "spearmen" (reserved for αἰχμητής) |
| πλάζουσι (με μέγα πλάζουσι, 2.132) | "greatly drive me astray" | "drive me far off course" | "baffle", "hinder", "make me wander" (reserved for ἀλάομαι); follows the table's πλάζω "drive off course" |
| Διὸς μεγάλου ἐνιαυτοί (2.134) | "years of great Zeus" | "great Zeus's years" | "the great god's years", "Zeus's seasons"; ἐνιαυτός is "year" |
| δοῦρα νεῶν … σπάρτα (2.135) | "the timbers of the ships … the ropes" | same | "spars" (reserved for ἱστός), "cables"; δοῦρα here are ship's timbers, not spears |
| νήπια τέκνα (2.136) | "infant children" | "little children" | follows the table's νήπια τέκνα (14.264) |
| ἔργον … ἀκράαντον (2.137–138) | "the task just so unaccomplished" | "the work stands just as it was, unaccomplished" | "fruitless", "unfulfilled"; αὔτως keeps "just so" (Odyssey 14.151) |
| ἀλλ’ ἄγεθ’ ὡς ἂν ἐγὼ εἴπω πειθώμεθα πάντες (2.139) | Odyssey wording, unchanged | Odyssey wording, unchanged | reused verbatim (the edition leaves out the Odyssey's commas) |
| εὐρυάγυιαν (Τροίην εὐρυάγυιαν, 2.141) | "wide-streeted" | "of the wide streets" | keeps the table's εὐρυάγυια |
| φὴ κύματα μακρά (2.144) | "like the long waves" | "like the long waves" | "towering waves", "tall billows" |
| πόντου Ἰκαρίοιο (2.145) | "the Icarian open-sea" | "the Icarian open sea" | "Icarian sea" alone, "Icarian main"; πόντος keeps the table's "open-sea" |
| Εὖρός τε Νότος τε (2.145) | "the East Wind and the South Wind" | same | follows the table's four-winds row |
| Ζέφυρος … λάβρος ἐπαιγίζων (2.147–148) | "the West Wind … fierce, swooping on it" | "the West Wind … swooping fiercely on it" | "gale", "furious"; Ζέφυρος keeps the table's "West Wind" |
| ὑπένερθε κονίη ἵστατ’ ἀειρομένη (2.150–151) | "from beneath their feet the dust stood up, rising" | "the dust rose and stood in the air from beneath their feet" | "a cloud of dust" |
| οὐρούς (2.153) | "the channels" | "the channels" (+ note: sense taken from context) | "trenches", "dikes"; rare word |
| ἀϋτὴ δ’ οὐρανὸν ἷκεν (2.153) | "and the cry reached heaven" | "and the cry … reached heaven" | follows the table's οὐρανὸν ἵκει "reaches heaven" |
| ἕρματα νηῶν (2.154) | "the props of the ships" | "the props" | follows the shipped ἕρματα "props" (iliad-005) |
| ὑπέρμορα (2.155) | "beyond fate" | "contrary to fate" | "beyond what was fated", "against destiny", "before its time" |
| ὢ πόποι … Ἀτρυτώνη (2.157) | "Ah, child of aegis-bearing Zeus, Atrytone," | same | ὢ πόποι is the table's "Ah"; αἰγιόχοιο Διὸς τέκος Ἀτρυτώνη follows the Odyssey's wording |
| οὕτω δὴ οἶκον δὲ φίλην ἐς πατρίδα γαῖαν (statement 2.158; question 2.174) | "so then, home to their dear fatherland" / "is it so, then, that home to your dear fatherland" | statement / question | follows the Odyssey's wording for the question; Hera's statement is the same line with the question turned to a statement because the edition has no question mark |
| ἐπ’ εὐρέα νῶτα θαλάσσης (2.159) | "over the broad back of the sea" | "over the sea’s broad back" | follows the table's row (3.362) |
| εὐχωλήν (2.160, 2.176) | "a boast" | "as a boast" | "a vow" (εὐχωλή elsewhere), "a prayer", "a triumph"; here something to boast about, and the note says so |
| Ἀργείην Ἑλένην (2.161, 2.177) | "Argive Helen" | "Argive Helen" | follows the Odyssey's "Argive Helen" |
| φίλης ἀπὸ πατρίδος αἴης (2.162, 2.178) | "away from their dear fatherland" | "far from their dear fatherland" | "from their dear native soil"; follows the table's φίλη πατρὶς αἶα "dear fatherland" |
| σοῖς ἀγανοῖς ἐπέεσσιν ἐρήτυε φῶτα ἕκαστον (2.164, 2.180) | "with your gentle words restrain each man" | "restrain each man with your gentle words" | "soothing", "kindly" (ἀγανός keeps "gentle"); ἐρητύω keeps "restrain / hold back" |
| μηδὲ ἔα νῆας ἅλα δ’ ἑλκέμεν ἀμφιελίσσας (2.165, 2.181) | "and do not allow them to drag the both-sides-curving ships seaward" | "and do not let them drag the ships, curved on both sides, down to the sea" | follows the Odyssey's ἀμφιέλισσαι "both-sides-curving" / "curved on both sides" |
| ὣς ἔφατ’, οὐδ’ ἀπίθησε θεὰ γλαυκῶπις Ἀθήνη (2.166) | "So she spoke, and did not disobey, the goddess, gleaming-eyed Athena," | "So Hera spoke, and the goddess, gleaming-eyed Athena, did not disobey;" | follows the Odyssey's ὣς ἔφατ’, οὐδ’ ἀπίθησε "So he spoke, and did not disobey" |
| καρπαλίμως δ’ ἵκανε θοὰς ἐπὶ νῆας Ἀχαιῶν (2.168) | "Swiftly she reached the swift ships of the Achaeans." | "Swiftly she came to the swift ships of the Achaeans." | iliad-007 wording with the subject changed from the Dream ("he") to Athena ("she") |
| Διὶ μῆτιν ἀτάλαντον (2.169) | "the equal of Zeus in cunning" | "the equal of Zeus in cunning" | "wise as Zeus", "peer of Zeus in counsel" (μῆτις is "cunning" in the table); ἀτάλαντος is "equal in weight" |
| ἑσταότ’ (2.170) | "standing" | "standing there" | "rooted", "motionless" |
| νηὸς ἐϋσσέλμοιο μελαίνης (2.170) | "the well-benched black ship" | "his well-benched black ship" | follows the table's row |
| ἄχος κραδίην καὶ θυμὸν ἵκανεν (2.171) | "grief had reached his heart and spirit" | "grief had come upon his heart and spirit" | follows the Odyssey's "grief reaches my heart and spirit" |
| ἀγχοῦ δ’ ἱσταμένη προσέφη γλαυκῶπις Ἀθήνη (2.172) | Odyssey wording, unchanged | Odyssey wording, unchanged | reused verbatim |
| διογενὲς Λαερτιάδη, πολυμήχαν’ Ὀδυσσεῦ (2.173) | Odyssey wording, unchanged | Odyssey wording, unchanged | reused verbatim |
| ἐν νήεσσι πολυκλήϊσι πεσόντες (2.175) | "in your many-thwarted ships having fallen" | "throw yourselves into your ships of many thwarts" | "rush", "tumble"; πολυκλήϊσι keeps the table's "many-thwarted" / "of many thwarts"; πεσόντες is "having fallen" |
| μηδ’ ἔτ’ ἐρώει (2.179) | "and no longer hold back" | "and no longer hang back" | "linger", "delay", "keep your distance"; ἐρωέω "draw back, hang back" |
|---|---|---|---|
| ξυνέηκε (θεᾶς ὄπα, 2.182) | "understood" | "understood" | "heard", "took in" (kept for ξύνιεν), "brought together" (the 1.8 sense of the same aorist, a different meaning of συνίημι) |
| ἔξοχον ἄνδρα (2.188) | "man standing out" | "a man who stood out above the rest" | "outstanding" and "pre-eminent" (reserved, see the table's ἔξοχος Ἀχαιῶν), "man of mark" |
| κακὸν ὣς δειδίσσεσθαι (2.190) | "be frightened like a coward" | "to be frightened like a coward" | "to be afraid like a base man", "to scare others" (the active sense; the form is read as passive/middle) |
| ἀπτόλεμος (2.201) | "unwarlike" | "unwarlike" | "not a fighter", "cowardly" (kept for ἀνάλκις "without might"), "unfit for war" in the translation (the note says it) |
| ἐναρίθμιος (2.202) | "counted" (never once counted in war) | "of no account" | "one of the number" and "to keep the number complete" (the Odyssey's rendering at 12.65, a different context), "reckoned" |
| φέρτεροι (2.201) | "stronger" | "stronger" | "better" (kept for ἀμείνων, 2.239), "mightier"; keeps the Odyssey's φέρτερος "stronger" (22.289) |
| πολυκοιρανίη (2.204) | "many-rulership" | "rule by many" | "the rule of many lords", "multiple kings", "many-lordship"; κοίρανος keeps the Odyssey's "ruler" |
| κοιρανέων (2.207) | "acting as ruler" | "as its ruler" | "playing the lord" and "lording it" (the Odyssey's rendering at 13.377, where the verb is a swagger; here it is neutral, a departure with that reason) |
| ἀμετροεπής (2.212) | "of unmeasured words" | "a man with no measure in his speech" | "endless talker", "babbler", "loud-mouthed" (each adds a judgement) |
| ἐκολῴα (2.212) | "kept up his brawling" | "kept up his clamour" | "scolded", "shouted" (reserved for βοάω); same verb as the noun κολῳός "uproar" (1.575) |
| φολκός (2.217) | "bandy-legged" (+ note: meaning not known) | "bandy-legged" | "squint-eyed" (the other ancient guess), "crook-legged" |
| κυρτὼ … συνοχωκότε (2.218) | "hunched, drawn together" | "humped, drawn together" | "stooping", "contracted", "bent in" |
| φοξὸς … κεφαλήν (2.219) | "peaked in the head" | "his head came to a point" (+ note: usual explanation) | "conical", "pointed-headed", "egg-headed" |
| ψεδνὴ … λάχνη (2.219) | "sparse down" | "sparse down" | "thin wool", "scanty hair", "fuzz"; λάχνη is "down, wool" |
| ἔχθιστος (2.220) | "most hateful" | "most hateful" | "most hated", "most detested"; superlative of ἐχθρός with the dative of those who hate him |
| νεικείεσκε · νείκεε · νεικείων · νεικείειν (2.221, 2.224, 2.243, 2.277) | "used to rebuke" · "rebuked" · "rebuking" · "to rebuke" | same | "reviled" (kept for the aorist νείκεσσεν in the Odyssey table), "insulted", "abused"; the present system keeps "rebuke" as in the table's νεικεῖ |
| κεκλήγων ὀξέα (2.222) | "shrilly shrieking" | "shrilly screamed out reproaches" (ὀξέα read as an adverb in both layers, as the note says) | "crying", "bawling", "yelling"; κλάζω is "shriek, ring" (ἔκλαγξαν, 1.46) |
| κοτέοντο · νεμέσσηθεν (2.222–223) | "bore a grudge" · "felt resentment" | "bore him a grudge" · "felt resentment" | "were angry" (kept for χόλος), "were indignant"; κοτέω keeps "bear a grudge" (1.181), νεμεσσάω the Odyssey's "feel resentment" |
| ἐκπάγλως κοτέοντο (2.222–223) | "terribly bore a grudge" | "terribly bore him a grudge" | "bore a terrible grudge" (the adverb is kept as an adverb, as in the table's ἐκπάγλως row) |
| μακρὰ βοῶν (2.224) | "crying out loudly" | "shouting loudly" | "with a long shout", "at length"; μακρά is "long" used as an adverb of voice |
| ἐξαίρετοι (γυναῖκες, 2.227) | "picked out" | "picked out for you" | "chosen", "choice", "special"; ἐξαιρέω "take out" |
| πρωτίστῳ (2.228) | "first of all" | "to you first of all" | "to the foremost", "to the best man" |
| υἷος ἄποινα (2.230) | "as ransom for a son" | "as ransom for a son" | "the ransom of his son"; ἄποινα keeps "ransom" (1.13) |
| ἵνα μίσγεαι ἐν φιλότητι (2.232) | "that you may mingle with her in love" | "that you may lie with her in love" | "have union with", "make love to"; follows the Odyssey table's μίγη φιλότητι "was mingled in love" / "lay in love with" |
| ἀπονόσφι κατίσχεαι (2.233) | "will keep back apart" | "keep her apart for yourself" | "hold aside", "keep from the rest"; κατέχω "hold fast" |
| ἀρχὸν ἐόντα (2.234) | "one who is a commander" | "a commander" | "a leader" (reserved for ἡγήτωρ / ἡγεμών), "an author of ills"; follows the table's ἀρχός "commander" |
| ἐπιβασκέμεν κακῶν (2.234) | "to bring … into evils" | "to lead … into evils" | "to make walk upon", "to lead to ruin"; causative of ἐπιβαίνω, with the genitive of the place |
| ὦ πέπονες (2.235, plural) | "O good ones" | "My good fellows" (+ note: meaning not known; read as scornful) | "soft ones", "dear friends", "you sheep"; follows the Odyssey table's πέπον "good" / "my good fellow" |
| κάκ’ ἐλέγχε’ (2.235) | "base reproaches" | "base disgraces" | "wretched cowards", "shames"; follows the table's ἐλέγχεα "reproaches" / "a disgrace", with κακά "base" |
| Ἀχαιΐδες οὐκέτ’ Ἀχαιοί (2.235) | "Achaean women, no longer Achaeans" | "Achaean women and no longer Achaean men" | "Achaean girls", "Achaeans no more"; follows the table's Ἀχαιϊάδες "the Achaean women" |
| γέρα πεσσέμεν (2.237) | "digest his prizes" | "digest his prizes of honour" | "cook", "chew on", "enjoy"; πέσσω "cook, digest"; γέρας keeps "prize" / "prize of honour" |
| προσαμύνομεν (2.238) | "are of any help to him" | "are any help to him" | "ward off for him", "defend"; ἀμύνω "ward off" is for the simple verb |
| ἕο μέγ’ ἀμείνονα φῶτα (2.239) | "than himself much better a man" | "a man far better than himself" | "greater", "stronger" (reserved for φέρτερος); φώς "man" |
| ἀκριτόμυθε (2.246) | "of unsorted speech" | "you who speak without sorting your words" (+ note: sense not known) | "indiscriminate", "reckless", "of confused speech", "babbling" (the Odyssey table turns these down for ἀκριτόμυθοι of dreams); the Odyssey's "indistinct" does not fit a man |
| λιγύς … ἀγορητής (2.246) | "a clear-voiced speaker" | "clear-voiced speaker" | "shrill", "orator"; follows the table's λιγὺς Πυλίων ἀγορητής "clear-voiced speaker" |
| ἴσχεο (2.247) | "hold yourself back" | "hold yourself back" | "stop", "be still", "restrain yourself" (ἐρητύω "restrain" is for the transitive verb) |
| ἐριζέμεναι βασιλεῦσιν (2.214, 2.247) | "to quarrel with kings" | "to quarrel with kings" | "to rival", "to contend" (the Odyssey table's ἐρίζω "rival" is for skill; ἐρίσαντε at 1.6 is "having quarrelled") |
| χερειότερον (2.248) | "worse" | "worse" | "inferior", "meaner", "baser"; kept apart from ἀμείνων "better" (2.239) |
| τὼ οὐκ ἂν … ἀνὰ στόμ’ ἔχων (2.250) | "Therefore you should not, with kings in your mouth, declare" | "So you should not declaim with kings on your lips" | "so", "that is why"; τὼ = τῷ "therefore" |
| ἀγορεύοις · ἀγορεύεις (2.250, 2.256) | "declare" | "declaim" · "speak out" | "speak in the assembly" (adds the place); follows the table's ἀγορεύω "declare" in a public pronouncement |
| νόστον φυλάσσοις (2.251) | "keep watch for homecoming" | "keep watch for your homecoming" | "lie in wait for", "watch for the chance to sail home" (each decides the sneer) |
| ὅπως ἔσται τάδε ἔργα (2.252) | "how these deeds will be" | "how this business will turn out" | "how these things will end", "what will come of this"; ἔργα "deeds" |
| ὀνειδίζων (2.255) | "reproaching" | "reproaching" | "insulting", "mocking" (reserved for κερτομέω "taunt"); ὄνειδος "reproach", ὀνειδείοις ἐπέεσσιν "words of reproach" (2.277, the table's ὀνειδείοις ἐπέεσσιν) |
| ἀφραίνοντα (2.258) | "acting senselessly" | "acting senselessly" | "raving", "playing the fool", "being foolish"; ἄφρων "without wits" |
| κάρη ὤμοισιν ἐπείη (2.259) | "upon … shoulders may there be a head" | "may … have a head upon his shoulders" | "may his head stay on", "may his head not be cut off"; ἔπειμι "be upon" |
| Τηλεμάχοιο πατὴρ κεκλημένος εἴην (2.260) | "called the father of Telemachus may I be" | "may I … be called the father of Telemachus" | "may I no longer be a father to Telemachus"; καλέω "call", the perfect passive participle |
| φίλα εἵματα (2.261) | "your own clothes" | "your own clothes" | "dear clothes", "beloved garments"; φίλος as "own"; εἵματα "clothes" |
| ἀμφικαλύπτει αἰδῶ (2.262) | "enfold your shame" | "enfold your shame" | "cover your nakedness", "hide your privates" (the note says the meaning); ἀμφικαλύπτω keeps the Odyssey's "enfold" |
| ἀφήσω (2.263) | "send away" | "send you away" | "let go", "drive", "dismiss"; ἀφίημι "send off, let go" |
| πεπλήγων … ἀεικέσσι πληγῇσιν (2.264) | "beating … with unseemly blows" | "beating you out of the assembly with unseemly blows" | "with shameful blows", "ugly blows"; ἀεικής keeps "unseemly" |
| ἰδνώθη (2.266) | "doubled over" | "doubled over" | "bent", "writhed", "cringed"; ἰδνόομαι "bend, double up" (pain) |
| θαλερὸν δάκρυ (2.266) | "an abundant tear" | "an abundant tear" | "a big tear", "a swelling tear", "a warm tear"; keeps the Odyssey table's θαλερὸν δάκρυον "an abundant tear" |
| σμῶδιξ αἱματόεσσα (2.267) | "a bloody weal" | "a bloody weal" | "a welt", "a bruise", "a blood-red wound"; σμῶδιξ is the raised mark of a stroke |
| ἀχρεῖον ἰδών (2.269) | "idly looking" | "with a vacant look" | "uselessly", "helplessly" (each decides the look); follows the Odyssey table's ἀχρεῖον ἐγέλασσεν "an idle laugh" (the sense "to no purpose") |
| ἡδὺ γέλασσαν (2.270) | "sweetly laughed" | "laughed with relish" | "laughed heartily", "laughed pleasantly", "joyfully"; ἡδύς "sweet, pleasant" as an adverb |
| ἀχνύμενοί περ (2.270) | "even though grieving" | "though grieving" | "though troubled", "in spite of their sorrow"; follows the table's ἀχνύμενος "grieving" |
| ἐσθλά · ἀγαθάς (2.272–273) | "good things" · "good counsels" | "good things" · "good counsels" | "noble", "excellent" (each makes one word do more than the other); both are "good" in the table |
| βουλάς … ἐξάρχων (2.273) | "leading off good counsels" | "taking the lead in good counsels" | "initiating", "proposing"; ἐξάρχω "begin, lead off" |
| πόλεμον κορύσσων (2.273) | "arming war" | "arming for war" (+ note: bold phrase, "arming battle") | "setting war on foot", "raising", "marshalling battle" (each smooths the phrase); κορύσσω "arm" (cf. ἱπποκορυσταί, 2.1) |
| μέγ’ ἄριστον (2.274) | "by far the best" | "by far the best thing" | "the very best", "something supremely good"; keeps the Odyssey's μέγ’ ἄριστον reading (πολὺ φέρτατος "by far the best") |
| λωβητῆρα ἐπεσβόλον (2.275) | "the outrager, the word-flinger" | "this outrager, this word-flinger" | "reviler", "abuser" (reserved for νεικέω), "railer", "ribald"; λώβη keeps "outrage" (1.232), ἐπεσβόλος is ἔπος + βάλλω |
| ἔσχ’ ἀγοράων (2.275) | "held back from the assemblies" | "keeping … out of the assemblies" | "kept from speaking", "silenced"; ἔχω "hold, hold back" with the genitive of separation |
| οὔ θήν μιν (2.276) | "surely not … him" | "I am sure … will not" | "I think", "doubtless"; θήν is a particle of assertion, "surely, indeed" |
| ἀνήσει (2.276) | "will urge on" | "will urge … on" | "send forth", "impel", "incite"; ἀνίημι "send up", the sense "urge on" with an infinitive |
| μερόπεσσι βροτοῖσιν (2.285) | "speech-dividing mortals" | "mortals of articulate speech" (+ note: meaning of μέροποι not known) | "mortal men" (the Odyssey table turns it down: "mortal" is kept for βροτός), "all human beings"; the Odyssey row μερόπων ἀνθρώπων with βροτός added |
| ὑπόσχεσις · ὑπέσταν (2.286, 2.349) | "promise" · "undertook" | "promise" · "undertook" | "pledge", "vow"; ὑφίσταμαι is "undertake", and ὑπέσχετο (2.112, published in iliad-008) is "promised" |
| ἀνιηθέντα (ἀνιάω, 2.291) | "distressed" | "distressed" | "vexed" (kept for ὀχθέω), "grieved", "worn out" |
| πόνος (2.291) | "toil" | "a toil" | "hardship", "labour"; the Odyssey table’s "toil" |
| πολυζύγῳ (νηῒ πολυζύγῳ, 2.293; ζυγόν "cross-bench, thwart") | "many-yoked" | "many-benched" | "many-thwarted" (kept for πολυκλήϊσι), "many-oared"; ζυγόν is "yoke" in `l` and the rowers’ cross-bench in `i`, and "well-benched" (ἐϋσσέλμοιο) is a different word |
| ἄελλαι χειμέριαι (2.293–294) | "blasts wintry" | "wintry storms" | "gales", "winter storms" alone; ἄελλα bare is "blasts" in `l` and "storms" in `i`, as shipped at Odyssey 14.383 |
| εἰλέωσιν (εἴλω, 2.294) | "hem in" | "hem in" | "shut in", "pen in"; keeps the Iliad’s ἔλσαι "to hem in" (1.409) |
| ὀρινομένη θάλασσα (2.294) | "the sea stirred up" | "a stirred-up sea" | "a raging sea", "a troubled sea" |
| ἀσχαλάω (ἀσχαλάᾳ, ἀσχαλάαν, 2.293, 2.297) | "chafe" | "chafes" · "chafing" | "be distressed" (reserved for ἀνιάομαι), "pine", "grow restless" |
| εἴνατος … περιτροπέων ἐνιαυτός (2.295) | "ninth is the year, as it comes round" | "it is the ninth year as it comes round" | "as the seasons turn", "the revolving year", "the year turning" |
| νεμεσίζομαι (2.296) | "I do not feel resentment at" | "I feel no resentment at" | "blame", "reproach", "be indignant with"; follows the Odyssey’s νεμεσσάω "feel resentment" |
| κενεόν (2.298) | "empty" | "empty-handed" | "with nothing", "in vain"; follows odyssey-073 (ἂψ ἰέναι κενεόν "go back empty-handed") |
| τλῆτε (2.299) | "Endure" | "Endure" | "Hold out", "Bear up", "Be patient"; the aorist imperative of τλάω, as the Odyssey’s τέτλαθι "Endure" |
| δαῶμεν (δάω, 2.299) | "we learn" | "we learn" | "find out", "discover"; the aorist subjunctive of an epic verb |
| χθιζά τε καὶ πρωΐζ’ (2.303) | "yesterday and the day before" | "yesterday and the day before" (+ note: in effect "only the other day") | "only the other day", "just the other day", "recently" (each decides the idiom) |
| πλατάνιστος (2.307, 2.310) | "plane-tree" | "plane-tree" | "plane tree" (unhyphenated), "sycamore" (a different tree in English) |
| δαφοινός (ἐπὶ νῶτα δαφοινός, 2.308) | "blood-red" | "blood-red" (+ note: sense not certain) | "tawny", "spotted", "crimson", "gory" (each picks one guess) |
| φόως δέ (ἧκε φόως δέ, 2.309; φόως = φῶς, -δε of direction) | "sent to the light" | "sent forth into the light" | "sent light" (reads δέ as "and" or φόως as the object), "sent forth into the open"; the note says δέ is the suffix |
| Ὀλύμπιος (αὐτὸς Ὀλύμπιος, 2.309, Zeus unnamed) | "the Olympian himself" | "the Olympian himself" | "Olympian Zeus" (supplies the name the poet withholds until 2.324), "the god of Olympus" |
| στρουθός · νεοσσοί (2.311, 2.317, 2.326) | "sparrow" · "nestlings" | "sparrow" · "nestlings" | "bird" (loses the species), "ostrich" (later Greek), "chicks", "fledglings" |
| ὑποπεπτηῶτες (2.312) | "crouching" | "crouching" | "cowering", "huddled", "cringing"; ὑποπτήσσω is "crouch down" |
| τετριγῶτας (2.314) | "as they cheeped" | "as they cheeped" | "squealing", "chirping", "twittering"; τρίζω is the thin high cry of young birds |
| ἐλεεινά (adverb, 2.314) | "pitiably" | "pitiably" | "piteously", "wretchedly"; ἐλεεινός keeps the Odyssey’s "pitiable" |
| ἀμφεποτᾶτο · ὀδυρομένη (2.315) | "fluttered around" · "lamenting" | "fluttered about" · "lamenting" | "hovered", "wailing"; ὀδύρομαι is "lament" |
| ἐλελιξάμενος (2.316) | "having coiled himself" | "coiling himself" | "whirling", "twisting round" (each narrows the verb), "quivering"; ἐλελίζω "make quiver" is "shook" at 1.530 and the middle is read from the scene |
| ἀμφιαχυῖαν (2.316) | "shrieking around" | "shrieking about" (+ note: rare, sense taken from the formation) | "wailing", "screaming", "crying out" |
| ἀρίζηλος (ἀρίζηλον θῆκεν, 2.318) | "conspicuous" | "conspicuous" | "very clear", "plain to see", "famous"; ἀρι- is an intensifier |
| δεινὰ πέλωρα (2.321, neuter plural) | "the dread monsters" | "the dread monsters" | "dreadful portents", "fearful marvels"; follows the Odyssey’s δεινὸν πέλωρ "the dread monster", the plural kept |
| ὄψιμον ὀψιτέλεστον (2.325) | "late, late-fulfilled" | "a late one, late to be fulfilled" | "slow to come", "long delayed" (each drops one of the two ὀψ- words), "tardy"; τελέω is "fulfil" |
| πτολεμίξομεν (πτολεμίζω, 2.328) | "we shall fight" | "we shall fight" | "wage war" (reserved for the noun πόλεμος in a phrase), "do battle"; the epic form of πολεμίζω, read as a future |
| ἐπιφρασσαίατο (ἐπιφράζομαι, 2.282) | "take note of" | "take note of" | "ponder" (kept for φράζομαι in the sense "consider"), "mark", "heed"; ἐπιφράζομαι is "notice, take note of" |
| ἀγορᾶσθαι (ἀγοράασθε, 2.337) | "you speak in assembly" | "you hold forth in the assembly" | "you harangue", "you debate" (the Odyssey’s ἀγορήσατο is "addressed the assembly", of one speaker with a plan) |
| νηπίαχος (νηπιάχοις, 2.338) | "childish" | "childish" | "babyish", "infantile", "foolish" (reserved for νήπιος as an adjective of folly), "simple" |
| συνθεσίαι (2.339) | "covenants" | "covenants" | "agreements", "treaties", "pacts"; ὅρκια stays "oaths" |
| σπονδαὶ ἄκρητοι (2.341) | "libations unmixed" | "the unmixed libations" | "neat libations", "undiluted drink-offerings"; ἄκρητος is "unmixed" as in the Odyssey’s ἄκρητον γάλα |
| δεξιαί (2.341) | "right hands" | "right hands" | "pledges", "handclasps" (the note says what the right hand does); the Odyssey’s δεξιτερή is "right hand" |
| ᾗς ἐπέπιθμεν (2.341) | "in which we trusted" | "in which we trusted" | "on which we relied", "in which we had put our faith"; πείθομαι with the dative is "trust, rely on" |
| αὔτως (ἐπέεσσ’ ἐριδαίνομεν, 2.342) | "just so" | "to no purpose" | "idly" and "for no reason" (the Odyssey’s i-renderings of other contexts); keeps the Iliad’s "just so" in `l` and the Odyssey’s "to no purpose" (odyssey-060) in `i` |
| ἀστεμφής (ἀστεμφέα βουλήν, 2.344) | "unshaken" | "unshaken" (+ note: formation uncertain) | "firm", "steadfast" (kept for ἔμπεδος), "unmoving" |
| ἕνα καὶ δύο (2.346) | "one and two" | "one or two" | "a single one or two", "a few"; the idiom is kept as a number |
| νόσφιν (2.347) | "apart from" | "apart from" | "away from", "without" |
| ἄνυσις (2.347) | "accomplishment" | "accomplishment" | "success", "achievement", "progress" |
| ἐναίσιμα σήματα (2.353) | "fitting signs" | "fitting signs" (+ note: of omens, favourable) | "favourable signs", "propitious omens" (decide the sense); keeps the αἶσα family of the Odyssey’s ἐναίσιμος |
| ἐπιδέξια (2.353) | "on the right" | "on the right" (+ note: the lucky side) | "to the right-hand side", "from the right"; the adverb of the Odyssey’s ἐπιδέξια "to the right" |
| ὁρμήματα (2.356) | "strivings" | "strivings" (+ note: whose strivings, Helen’s own or the Achaeans’ for her, is not said) | "efforts", "struggles", "longing" (each decides whose they are) |
| κατακοιμηθῆναι (2.355) | "has lain down" | "has lain down beside" | "to have slept with", "to have bedded" (the note says what the euphemism means); κατακοιμάω is "put to sleep" |
| φῦλον · φρήτρη (2.362–363) | "tribe" · "clan" | "tribe" · "clan" | "race" (kept for γένος), "phratry", "brotherhood", "kin"; φῦλον keeps the Odyssey’s "tribe" (ἄγρια φῦλα Γιγάντων) |
| κρίνω (κρῖν’, 2.362) | "sort" | "sort" | "judge", "pick out" (the Odyssey’s sense of κρίνας … ἀρίστους, odyssey-020), "divide", "marshal" |
| ἀρήγω · ἀρήγῃ (2.363) | "help" | "help" | "aid", "defend"; follows the Iliad’s ἀρήγω "help" (ἐπὶ Τρώεσσιν ἀρῆξαι, 1.408) |
| κακός · ἐσθλός (of men in battle, 2.365–366) | "base" · "good" | "base" · "good" (+ note: in battle, cowardly and brave) | "bad" and "worthless" (κακός stays "base" of conduct), "cowardly" and "brave" (each decides the sense), "noble" |
| κακότης (ἀνδρῶν κακότητι, 2.368) | "baseness" | "baseness" | "wickedness", "misery" (the Odyssey’s renderings in odyssey-119 and odyssey-034, for other senses), "cowardice"; departure from the Odyssey, with the reason: κακός of men in war is "base" in this part, and the noun keeps the family |
| θεσπεσίῃ (dative without a noun, 2.367) | "wondrous (power)" | "some wondrous power" (+ note: usually a divine ordinance, set against men’s baseness) | "by divine will", "by a god’s decree" (supply the noun and decide the sense); θεσπέσιος keeps "wondrous" |
| ἀλαπάζω (οὐκ ἀλαπάξεις, 2.367) | "lay waste" | "lay waste" | "sack" (kept for ἐκπέρθω), "plunder" (ἐξαλαπάξαι at 1.129), "destroy"; keeps the Odyssey’s "laid waste" for the simple verb |
| συμφράδμονες (2.372, τοιοῦτοι δέκα μοι συμφράδμονες εἶεν Ἀχαιῶν) | "fellow-planners" | "advisers" | "counsellors" (the Iliad keeps "counsel" for βουλή and the Odyssey table reserves βουληφόρος "counsel-bearing"), "councillors", "planners" alone; σύν + φράζομαι "plan", as in the table’s συμφράσσατο "devised" |
| ἠμύσειε (πόλις … ἠμύσειε, 2.373; ἠμύω "bow down, sink forward", not ἀμύνω "ward off") | "would bow down" | "would fall" | "would stoop", "would collapse", "would be laid low"; the note names the root and keeps it apart from ἀμύνω |
| ἁλοῦσά τε περθομένη τε (2.374) | "taken and being sacked" | "taken and sacked" | "captured and ravaged", "stormed"; πέρθω keeps "sack" (the Iliad’s ἐκπέρθω "sack") |
| ἀπρήκτους ἔριδας καὶ νείκεα (2.376) | "fruitless strifes and quarrels" | "fruitless strifes and quarrels" | "futile", "endless" (ἄπρηκτος keeps "fruitless", as ἄπρηκτον πόλεμον at 2.121); ἔρις keeps "strife" and νεῖκος "quarrel" |
| νικᾷς … υἷας Ἀχαιῶν (2.370, νικάω with an accusative of persons) | "you surpass" | "you … surpass" | "you win over", "you defeat", "you beat" (each makes it a contest with a loser); νικάω "prevail over, surpass" |
| χαλεπαίνων (2.378) | "growing harsh" | "in my anger" | "being furious", "raging", "fiercely" (χόλος keeps "anger" and μῆνις "wrath"; the participle of χαλεπός "harsh" is read as a mood of anger, and the note says so) |
| ἀνάβλησις κακοῦ (2.380) · ἀμβαλλώμεθα (2.436, ἀναβάλλομαι) | "a putting-off of evil" · "let us put off" | "delay of evil" · "put off" | "postponement", "reprieve", "respite" (kept for παυσωλή); ἀναβάλλω "put off" in both |
| οὐδ’ ἠβαιόν (2.380, 2.386) | "not even a little" | "not the least bit" | "not even a little" in `i`, "not in the least", "not at all" (kept for οὐδέ τι); follows the Odyssey’s shipped οὐδ’ ἠβαιόν (odyssey-009, 3.14: `l` "not even a little", `i` "not the least bit"); ἠβαιός "little" |
| ξυνάγωμεν Ἄρηα (2.381) | "bring Ares together" | "join battle" | "bring on war", "clash"; Ἄρης stands for war and the idiom is Greek; follows the Odyssey table’s Ἄρηϊ "in battle" (20.50) |
| θηξάσθω · θέσθω · μεδέσθω (2.382–384, third-person imperatives) | "whet" · "put in order" · "be mindful of" | "whet" · "put in good order" · "be mindful of" | "sharpen" (θήγω is "whet"), "look to", "see to", "prepare"; μέδομαι "be mindful of" is kept apart from μέδων "lord" (Odyssey table μέδοντες) |
| κρινώμεθ’ Ἄρηϊ (2.385) | "be decided by … Ares" | "fight it out … in … war" | "be judged", "be parted", "be sorted" (κρίνω keeps "sort, decide" and διακρινέει "part", 2.387); the middle with Ares is "contend, fight" and the note says so |
| παυσωλή (2.386) | "respite" | "pause" | "cessation", "stop", "truce"; rare noun from παύω "stop" |
| μένος ἀνδρῶν (2.387, of fighting strength) | "the might of men" | "the might of men" | "the strength of men" (kept for σθένος and κράτος), "the fury" (the table’s μένος of anger, 1.207, 1.282 in iliad-003), "the courage"; "might" is the Iliad’s word reserved for μένος / ἴς |
| διακρινέει (2.387) | "shall part" | "parts" | "shall decide", "divide", "break up"; κρίνω + δια- "separate" |
| τελαμών (2.388) | "strap" | "shield-strap" | "baldric", "belt", "sling"; the strap that carried the shield on the chest |
| ἀσπίδος ἀμφιβρότης (2.389; the Odyssey does not have it) | "man-covering shield" | "man-covering shield" | "all-covering", "full-length shield", "round the man" (each decides the shape); ἀμφί "on both sides" + βροτός "mortal, man" |
| ἱδρώσει (2.388, 2.390) | "will sweat" | "will be wet with sweat" · "will sweat" | "will drip", "will stream", "will be drenched"; ἱδρόω "sweat" |
| ἐΰξοον (ἅρμα, 2.390; formation uncertain) | "well-polished" | "well-polished" | "well-planed", "smooth-running", "well-wheeled"; ἐΰ- "well" + the root of ξέω "scrape smooth", and the Odyssey table’s ἐΰξεστος "well-polished" is the same family |
| τιταίνων (of a horse, 2.390) | "straining at" | "strains at" | "pulling", "drawing", "stretching"; τιταίνω "stretch, strain" (the Odyssey table’s τόξα τιταίνοιτο "stretch bows") |
| ἄρκιον (2.393; usual sense "sufficient, sure") | "assured" | "no assurance" | "enough", "safe", "possible"; the adjective is "sufficient, certain" and the note says the sense is the usual one |
| μιμνάζειν (2.392) | "linger" | "linger" | "hang back", "stay put", "hold back"; the frequentative of μίμνω "stay" |
| ἀκτῇ ἐφ’ ὑψηλῇ … προβλῆτι σκοπέλῳ (2.395–396) | "on a high headland … on a jutting crag" | "on a high headland … on a jutting crag" | "shore", "cliff", "reef" (ἀκτή keeps the Odyssey’s "headland"); προβλής "thrust forward, jutting" as the Odyssey’s ἀκταὶ προβλῆτες "headlands, thrust forward"; σκόπελος "crag" |
| ὀρέοντο (2.398; epic form, root of ὄρνυμι) | "hurried off" | "hurried off" | "scattered" (kept for κεδασθέντες), "sprang up", "rushed"; the note says the root |
| κάπνισσαν (2.399) | "made smoke" | "set the smoke rising" | "lit fires", "kindled", "cooked" (each supplies what the Greek leaves implied); καπνίζω "make smoke" |
| αἰειγενέτης (θεῶν αἰειγενετάων, 2.400) | "of the gods, the forever-born" | "of the everlasting gods" | "ever-born" (the Odyssey table has "forever-born"), "immortal" (reserved for ἀθάνατος), "undying" (the Iliad’s ἀγήρως "ageless" stands at 447), "who are forever" (θεοὶ αἰὲν ἐόντες, the table’s other epithet); follows the table’s θεῶν αἰειγενετάων (24.373); αἰεί + γίγνομαι |
| μῶλον Ἄρηος (2.401) | "the toil of Ares" | "the toil of battle" | "the press of war", "the tumult", "the grind"; μῶλος "toil, struggle" and Ares as war, as in the Odyssey table’s Ἄρηϊ |
| ἄλλος δ’ ἄλλῳ ἔρεζε (2.400) | "one to one, and another to another, sacrificed" | "each man sacrificed to a different one" | "offered", "made offerings", "poured libations"; ῥέζω of sacrifice is "sacrifice" (ἱερὰ ῥέξας, "performed the sacrifices", 2.145) |
| πενταέτηρον (βοῦν … πίονα πενταέτηρον, 2.403) | "five-year-old" | "five-year-old" | "five years old", "of five winters", "full-grown"; πέντε + ἔτος; `l` keeps the Odyssey’s shipped "five-year-old" (odyssey-070, odyssey-096) |
| Παναχαιῶν (2.404) | "of the Achaeans all together" | "of all the Achaeans" | "Panachaeans" (an English non-word); follows the Odyssey table’s Παναχαιοί "the Achaeans all together" / "all the Achaeans" |
| γέροντας ἀριστῆας (2.404) | "the elders, the best men" | "the elders, the best men" | "the older champions", "the noble elders"; follows the Odyssey table’s ἀριστῆες "the best men" |
| Αἴαντε δύω (2.406, dual) | "the two Ajaxes" | "the two Ajaxes" | "the two Ajax", "both Ajaxes"; the dual is kept as "two" |
| αὐτόματος (2.408) | "of his own accord" | "unbidden" | "uninvited", "of himself", "spontaneously"; the adjective is "self-moved" |
| ἀδελφεόν (2.409) | "brother" | "brother" | "his own brother", "kinsman"; ἀδελφεός is the epic ἀδελφός |
| ὡς ἐπονεῖτο (2.409) | "how he was toiling" | "how hard … was toiling" | "how he was distressed" (πόνος keeps "toil"), "how he was busy"; πονέομαι "toil" |
| περιστήσαντο (βοῦν, 2.410) | "stood around" | "stood round" | "set the ox in place", "stationed the ox round the altar" (no altar is named); aorist middle with the ox as object |
| αἰθέρι ναίων (2.412) | "in the aether dwelling" | "who dwell in the bright upper air" | "in the upper air dwelling", "in the bright sky", "in the heavens" (reserved for οὐρανός); reused from the Odyssey’s shipped αἰθέρι ναίων (odyssey-076); αἰθήρ elsewhere is "the upper air" in `l` as in the Odyssey (2.458, δι’ αἰθέρος) |
| μὴ πρίν … δῦναι … ἐλθεῖν … πρίν … βαλέειν (2.413–414, a wish in infinitives) | "not before the sun go down … before I cast down" | "let the sun not go down … before I have thrown down" | "grant that" (supplies a verb the Greek leaves out), "may the sun not set until" (adds a conjunction); the note says the wish is carried by the infinitives |
| κατὰ πρηνὲς βαλέειν (2.414) · πρηνέες (2.418) | "cast down headlong" · "headlong" | "thrown down headlong" · "face down" | "forward", "prone", "straight down"; πρηνής "headlong, face-forward"; the adverb of the hall and the adjective of the men have one English in `l`, and `i` says "face down" for men |
| Πριάμοιο μέλαθρον (2.414) | "the roof of Priam" | "Priam’s palace" | "rafter" (the Odyssey table’s μέλαθρον at 22.239 is a single beam, "rafter"; here the roof stands for the house), "hall" (reserved for μέγαρον), "house"; a departure from the Odyssey, with the reason |
| αἰθαλόεν (2.415) | "soot-blackened" | "soot-blackened" | "smoky", "sooty" (the Odyssey table’s `l` for αἰθαλόεις 22.239 is "sooty"; the compound reads better with the roof, and `i` there is also "soot-blackened"); extends the Odyssey table’s αἰθαλόεις |
| πυρὸς δηΐοιο (2.415) | "hostile fire" | "hostile fire" | "enemy fire", "devouring fire", "raging fire", "consuming fire"; δήϊος "hostile" |
| θύρετρα (2.415) | "doors" | "doors" | "gates", "doorways"; keeps the Odyssey’s "doors" (22.137) |
| Ἑκτόρεον χιτῶνα (2.416) | "Hector’s tunic" | "Hector’s tunic" | "the tunic of Hector" is the same, "Hectorean tunic", "Hector’s shirt"; the adjective is turned to the genitive |
| δαΐξαι … ῥωγαλέον (2.416–417) | "to rend … torn to tatters" | "(have) torn … to rags" | "cleave", "slash", "pierce" (each says too little of the cloth); δαΐζω "rend, tear", ῥωγαλέος "torn, rent" |
| ὀδὰξ λαζοίατο γαῖαν (2.418) | "may take the earth with their teeth" | "bite the earth" | "lick the dust", "seize the ground", "kiss the earth" (each changes the gesture); ὀδάξ "with the teeth" |
| ἑταῖροι (2.417) | "companions" | "companions" | "comrades", "friends", "men"; keeps the Odyssey’s "companions" |
| ὣς ἔφατ’, οὐδ’ ἄρα πώ οἱ ἐπεκραίαινε Κρονίων (2.419) | "So he spoke, but not yet for him did the son of Cronus bring it to fulfilment" | "So he spoke, but the son of Cronus did not yet fulfil it for him" | "grant" (reserved for δίδωμι with a thing given), "answer"; ἐπικραιαίνω "bring to fulfilment" |
| ἀμέγαρτον πόνον (2.420) | "the unenviable toil" | "the dreadful toil" | "unwished-for", "grievous", "pitiless"; follows the Odyssey’s ἀμέγαρτον ἀυτμήν "unenviable" / "dreadful" |
| ἱρά (δέκτο μὲν ἱρά, 2.420) | "the sacrifices" | "the sacrifices" | "the offerings", "the rites"; ἱερά "sacrifices" as at 2.145 |
| ὄφελλεν (πόνον … ὄφελλεν, 2.420) | "increased" | "made … grow" | "heaped up", "swelled", "multiplied"; ὀφέλλω "increase", kept apart from ὀφείλω "ought" |
| σχίζῃσιν ἀφύλλοισιν (2.425) | "leafless split wood" | "leafless split wood" | "dry logs", "kindling", "billets", "stripped wood"; σχίζα "split piece of wood" |
| ὑπείρεχον Ἡφαίστοιο (2.426) | "held over Hephaestus" | "held … over the flame of Hephaestus" | "held over the fire" (loses the name), "held over Hephaestus" in `i` (opaque); the note says Hephaestus stands for fire |
| μηκέτι νῦν δήθ’ αὖθι λεγώμεθα (2.435; usual sense "talk idly", not certain) | "no longer now for long here let us talk" | "let us talk here no longer" | "lie about", "linger", "waste time" (each picks the other sense of λέγομαι), "gather" |
| ἔργον ὃ δὴ θεὸς ἐγγυαλίζει (2.436) | "the work which indeed a god is placing in our hands" | "the work that a god is now putting into our hands" | "Zeus" (supplies the name), "delivers", "offers"; ἐγγυαλίζω "put into the hand" |
| ἀθρόοι ὧδε (2.439) | "all together, thus" | "all together in this way" | "in a body", "massed"; ἀθρόος "all together, in a crowd" |
| ἀγειρόντων (2.438) · ἐγείρομεν (2.440) | "gather" · "rouse" | "gather" · "rouse" | "collect"/"muster" (kept for ἀγείρω in the Odyssey’s πολὺν βίοτον ἀγείρων "gathering"), "wake" (kept apart); ἀγείρω "gather" and ἐγείρω "rouse" differ by one vowel and the note says so |
| ὀξὺν Ἄρηα (2.440) | "sharp Ares" | "keen battle" | "fierce Ares" (ὀξύς is "sharp"), "swift war", "bitter fight"; Ares stands for war |
| οἳ δ’ ἀμφ’ Ἀτρεΐωνα διοτρεφέες βασιλῆες θῦνον κρίνοντες (2.445–446) | "rushed about, sorting them" | "hurried about … sorting them" | "choosing out", "marshalling", "picking out" (each decides what is sorted); θύνω "rush", κρίνω "sort"; the note says the Greek has no object |
| ἐρίτιμον (αἰγίδα, 2.447) | "much-honoured" | "much honoured" | "precious", "costly", "of great price" (the tassels are priced next line), "very valuable"; ἐρι- is an intensifier |
| ἀγήρων ἀθανάτην τε (2.447) | "ageless, and immortal" | "ageless and immortal" | "unaging", "deathless" (kept for ἀθάνατος in the Odyssey table); ἄγηρως "ageless" |
| θύσανοι παγχρύσεοι ἠερέθονται (2.448) | "tassels, all-golden, hang waving" | "tassels, all of gold, hang waving" | "tufts", "fringes" (θύσανος is a tassel), "swing", "flutter", "float"; πάγχρυσος follows the Odyssey table’s πάγχαλκος "all of bronze"; ἠερέθομαι is rare, "hang waving" |
| πάντες ἐϋπλεκέες (2.449) | "all well-plaited" | "every one finely plaited" | "well-woven", "braided"; πλέκω "plait", ἐΰ- "well" |
| ἑκατόμβοιος (2.449) | "worth a hundred oxen" | "worth a hundred oxen" | "a hundred-oxen's value", "worth a hecatomb" (a hecatomb is a sacrifice, not a price); ἑκατόν + βοῦς |
| παιφάσσουσα διέσσυτο (2.450; παιφάσσω rare) | "darting about … rushed through" | "darted about and rushed through" | "flashing", "gleaming" (each picks one guess), "sweeping"; διασεύω "rush through" |
| λαὸν Ἀχαιῶν (2.450) | "the people of the Achaeans" | "the army of the Achaeans" | "the host", "the men"; follows the shipped 2.163 (κατὰ λαὸν Ἀχαιῶν "through the people" / "through the army") |
| ὀτρύνουσ’ ἰέναι (2.451) | "urging them to go" | "urging them forward" | "bidding", "rousing" (kept for ὄρνυμι ἐν … ὦρσεν, 2.451); ὀτρύνω keeps "urge" (the Odyssey table sets it against ἄνωχθι "bid") |
| ἐν … ὦρσεν (2.451) | "roused in" | "roused in the heart of each man" | "stirred", "put into", "kindled"; ὄρνυμι "rouse", tmesis |
| ἄλληκτον (2.452) | "unceasing" | "unceasing" | "tireless", "unflagging", "relentless"; ἀ- + λήγω "stop" |
| πολεμίζειν ἠδὲ μάχεσθαι (2.452) | "to wage war and to fight" | "to wage war and to fight" | "to war and battle" (loses the verbs), "to fight on"; two infinitives kept |
| πόλεμος γλυκίων … ἠὲ νέεσθαι (2.453) | "war became sweeter than to go back" | "war became sweeter … than going home" | "more welcome", "more pleasant"; follows iliad-003’s γλυκίων "sweeter" (1.249) |
| πῦρ ἀΐδηλον (2.455; ἀΐδηλος either "destroying" or "unseen") | "destroying fire" | "destructive fire" (+ note: sense disputed) | "ruinous" (reserved for οὐλόμενος and the Odyssey’s 22.165 "that ruinous man"), "baleful", "unseen", "devouring"; follows the Odyssey table’s ἀίδηλον Ἄρηα "destroying Ares" / "destructive Ares" (8.309) |
| ἐπιφλέγει (2.455) | "blazes over" | "blazes over" | "burns", "sets alight", "devours"; ἐπιφλέγω "blaze upon" |
| ἄσπετον ὕλην (2.455) | "boundless forest" | "boundless forest" | "vast", "endless", "immeasurable" (kept for ἀμέτρητος); follows the Odyssey table’s ἄσπετα κρέα "boundless meat" |
| ἕκαθεν δέ τε φαίνεται αὐγή (2.456) | "from afar its glare is seen" | "its glare is seen from far off" | "its light", "its radiance" (kept for φάος / φαεινός), "its flame"; αὐγή "glare, bright light" |
| αἴγλη παμφανόωσα (2.458) | "the all-shining gleam" | "an all-shining gleam" | "dazzling", "blazing"; παμφανόων "all-shining" (the Odyssey table’s παμφανόων of the sun) |
| ἔθνεα πολλά (of birds, 2.459) · (of men, 2.464) | "the many tribes" · "the many tribes" | "the many swarms" · "their many swarms" | "flocks" (breaks the echo between the two similes and the table’s ἔθνεα (2.87, 2.91) "swarms" in both places), "companies", "hosts"; follows the table’s ἔθνεα "tribes" / "swarms" |
| ὀρνίθων πετεηνῶν (2.459) | "winged birds" | "winged birds" | "feathered", "flying"; πετεηνός "winged", as in the Odyssey table’s ἐλαφρότατος πετεηνῶν "lightest of winged things" |
| δουλιχοδείρων (κύκνων, 2.460; δολιχόδειρος) | "long-necked" | "long-necked" | "slender-necked", "of the long throat", "swan of the long necks"; δολιχός "long" + δειρή "neck" |
| Ἀσίῳ ἐν λειμῶνι Καϋστρίου ἀμφὶ ῥέεθρα (2.461) | "in the Asian meadow about the streams of the Cayster" | "in the Asian meadow around the streams of the Cayster" | "Asia’s meadow", "the Asian flats", "the Asius meadow" (a man’s name is another ancient reading); Κάϋστρος "the Cayster", the familiar form |
| ποτῶνται ἀγαλλόμενα πτερύγεσσι (2.462) | "fly about, exulting in their wings" | "fly about … exulting in their wings" | "flutter", "preening", "glorying in their wings", "rejoicing"; ποτάομαι "fly about", ἀγάλλομαι "exult" |
| κλαγγηδὸν προκαθιζόντων (2.463) | "settling down ahead with clamour" | "settling down ahead with clamour" | "alighting in front", "with a shrill cry" (loses the clamour’s root), "screaming"; προκαθίζω "sit down in front"; κλαγγή "clamour" as the Odyssey’s "boundless clamour" |
| σμαραγεῖ (2.463) | "resounds" | "resounds" | "roars", "echoes", "rings"; σμαραγέω "roar, resound" |
| προχέοντο (2.465) | "poured forth" | "poured out" | "streamed", "flowed", "swarmed"; προχέω "pour forth" middle |
| Σκαμάνδριον (πεδίον … λειμών, 2.465, 2.467) | "Scamandrian" | "Scamandrian" · "of the Scamander" | "of Scamander"; the adjective of Σκάμανδρος, the Latinised "Scamander" |
| κονάβιζε (2.466) | "rang" | "rang" | "resounded" (kept for σμαραγεῖ, three lines before), "thundered", "rumbled", "crashed"; κοναβίζω "resound, ring"; `l` "rang" as in iliad-010 (κονάβησαν) and odyssey-049 |
| ποδῶν αὐτῶν τε καὶ ἵππων (2.466) | "the feet of the men themselves and of horses" | "the feet of the men themselves and of the horses" | "the tramp", "the footfalls", "the hooves" (ἵππων has the horses), "of the men and horses alike" (αὐτῶν "themselves" is the men on foot as against the horses) |
| μυρίοι (2.468) | "countless" | "countless" | "ten thousand", "innumerable", "myriad"; follows μυρί’ ἄλγε’ "countless pains" (1.2) |
| φύλλα καὶ ἄνθεα … ὥρῃ (2.468) | "leaves and flowers … in their season" | "leaves and flowers … in their season" | "in spring", "in due time", "in the right hour"; ὥρη "season" in the dative of time |

| τῷ / τοῖς / τοῖσι δ’ ἅμα (ἅμ’) + number + μέλαιναι νῆες ἕποντο (2.524, 2.534, 2.545, 2.556, 2.568, whole-line closing formula of a Catalogue entry) | "And with them (him) forty black ships followed." | "And with them (him) forty black ships followed." | "ships followed them", "black ships went with them" (loses ἅμα), "dark ships"; μέλας "black" as in the Odyssey’s νηῦς μέλαινα; ἕπομαι "follow", kept apart from κίον "went" (2.509) and ἐστιχόωντο (2.516); `l` = `i` because the line is a counted formula and the number is what changes |
| τῶν αὖθ’ ἡγεμόνευ’ + name (2.540, 2.552, 2.563, whole-line leader formula) | "Of these again was leader X" | "Of these, in turn, X was the leader" | "led them again", "was their commander" (ἀρχός is "commander"), "of these X had command"; αὖθ’ = αὖθι, a by-form of αὖθις / αὖτε, "again, in turn", ἡγεμονεύω "be leader" (the Odyssey’s "led the way" is for a guide on a road) |
| ἦρχον (+ genitive of a people, 2.494, 2.512, 2.517) | "were leading" | "led" (or "were led by", when the people are the subject, 2.511) | "ruled", "were commanders" (reserved for ἀρχός), "commanded"; ἄρχω "lead" as in iliad-010 (ἄρχευ’ "lead") |
| ἡγεμονεύω / ἡγέομαι (2.527, 2.567) | "was leader" · "was leading" | "was leader" · "led" | "marched at the head", "was in command"; ἡγεμονεύω "be leader" and ἡγέομαι "lead" are kept apart |
| κοσμέω · διακοσμέω (κοσμῆσαι 2.554, διεκόσμεον 2.476) | "to set in order" · "set in order" | "to marshal" · "set in order" (the leaders) | "arrange", "array", "deck out" (the Odyssey’s κόσμος is "order" and "contriving"); `i` "marshal" in the skill (κοσμῆσαι), "set in order" for the act |
| ἐρίζω (of skill, Νέστωρ οἶος ἔριζεν, 2.555) | "rivalled" | "rivalled" | "quarrelled" (ἐρίζω of strife is "quarrel", 2.214 and 2.247), "vied with", "competed"; the Odyssey’s ἐρίζω "rival" for skill |
| ἱλάομαι (ἱλάονται, 2.550) | "appease" | "appease" | "propitiate", "placate", "worship"; the same verb as ἱλάσκομαι "appease" (1.386) |
| ἔσπετε νῦν μοι Μοῦσαι (2.484, whole-line invocation) | "Tell now to me, Muses," | "Tell me now, Muses," | "Sing", "Speak" (ἄειδε is "sing", 1.1), "Declare"; ἐνέπω "tell" as in the Odyssey’s ἔννεπε |
| Ὀλύμπια δώματ’ ἔχουσαι (2.484, feminine) · Ὀλυμπιάδες Μοῦσαι (2.491) | "who hold the Olympian halls" · "the Olympian Muses" | "you who hold the halls of Olympus" · "the Olympian Muses" | "Muses of Olympus" (for Ὀλυμπιάδες), "who dwell on Olympus"; the table’s Ὀλύμπια δώματ’ ἔχοντες in the feminine |
| κλέος οἶον ἀκούομεν (2.486) | "we hear a report alone" | "we hear only a report" | "fame", "rumour", "glory" (κλέος ἐσθλόν is "good fame"); κλέος "report" as in the Odyssey table’s κλέος "report" (16.461) |
| οὐκ ἂν … μυθήσομαι οὐδ’ ὀνομήνω (2.488) | "I could not tell, nor could I name it" | "I could not tell, nor name" | "I could not recount", "nor mention"; follows the Odyssey’s same words at 4.240 (also 11.328, 11.517) |
| δέκα μὲν γλῶσσαι, δέκα δὲ στόματ’ … φωνὴ ἄρρηκτος, χάλκεον … ἦτορ (2.489–490) | "ten tongues, and ten mouths … a voice unbreakable, and a heart of bronze for me were within" | "ten tongues were mine, and ten mouths, and an unbreakable voice, and a heart of bronze within me" | "unbroken voice", "iron voice", "tireless", "brazen heart"; ἄρρηκτος "unbreakable" (Odyssey), χάλκεος "of bronze", ἦτορ "heart" |
| μνησαίατο (μιμνήσκομαι, 2.492) | "call to mind" | "call to mind" | "remind me of", "remember" (no object "me" in the Greek), "tell"; μιμνήσκομαι "call to mind" |
| ἀρχοὺς … νηῶν (2.493) | "the commanders of the ships" | "the commanders of the ships" | "captains", "leaders" (reserved for ἡγεμών, ἡγήτωρ); follows the Iliad’s ἀρχός "commander" (1.311) |
| προπάσας (νῆάς τε προπάσας, 2.493) | "all of them" | "all" | "every single one", "all together" (reserved for συμπάντων / πάντων ἅμα) |
| ἔθνεα πολλά (of flies, 2.469) | "the many tribes" | "the many swarms" | follows the table’s ἔθνεα "tribes" / "swarms" (2.87, 2.91, 2.459, 2.464) |
| ἁδινάων μυιάων (2.469) | "thronging" | "thronging" | "buzzing", "restless" (kept for the table’s ἁδινάων "thronging", of the bees at 2.87) |
| μεταπρέπω (βόεσσι μεταπρέπει, 2.481) | "is conspicuous among" | "is conspicuous among" | "stands out among" (the Odyssey’s `i` for μεταπρέπει, 10.525 and 11.33; here it would repeat ἔξοχος "stands out" in the unit before), "excels among" |
| ἔξοχος (μέγ’ ἔξοχος ἔπλετο, 2.480; ἔξοχον ἡρώεσσιν, 2.483) | "greatly standing out" · "standing out" | "stands out far above" · "standing out" | "outstanding", "pre-eminent" (reserved, see the table’s ἔξοχος Ἀχαιῶν), "supreme"; follows the table’s ἔξοχος "stood out" |
| ἐκπρεπής (ἐκπρεπέ’ ἐν πολλοῖσι, 2.483) | "distinguished" | "distinguished" | "conspicuous" (reserved for ἀριδείκετος and μεταπρέπω), "eminent", "outstanding" (ἀριπρεπής), "splendid" (ἀγλαός) |
| ἀγέληφι (2.480) | "in the herd" | "in a herd" | "in the herd of cattle"; -φι is the old ending that serves as a dative |
| ἄγγεα (γλάγος ἄγγεα δεύει, 2.471) | "the vessels" | "the vessels" | "the pails" (the Odyssey’s `i` for γαυλοί, 9.222–223, where ἄγγεα stays "vessels"), "the jars", "the bowls" |
| ἠλάσκω (2.470) | "roam" | "roam" | "wander", "flit", "buzz"; ἠλάσκω "wander about" |
| ὑσμίνην ἰέναι (2.477) | "to go into battle" | "to go into battle" | "to enter the fray"; ὑσμίνη "battle" as in the Odyssey and iliad-007, iliad-010 |
| ὄζος Ἄρηος (Ἐλεφήνωρ, 2.540) | "scion of Ares" | "scion of Ares" | "offshoot", "branch", "descendant", "darling of Ares"; literally "branch", used of a descendant |
| ἀσπιδιώτης (ἀνέρας ἀσπιδιώτας, 2.554) | "shield-bearing" | "shield-bearing" | "shielded", "shield-men", "armed with shields" |
| λινοθώρηξ (2.529) | "linen-breastplated" | "wore a linen breastplate" | "linen-corsleted", "linen-armoured"; θώραξ is "breastplate" at every occurrence (2.544 θώρηκας "breastplates") |
| ἐκέκαστο (ἐγχείῃ ἐκέκαστο, 2.530) | "excelled" | "excelled" | "surpassed" (reserved for νικάω, 2.370), "outdid", "was better than"; follows the Odyssey’s ἐκέκαστο "excelled" (odyssey-006 and odyssey-044) |
| Πανέλληνες (2.530) | "the Hellenes all together" | "all the Hellenes" | "all Greeks" (Greeks is avoided in both layers), "the whole of Hellas"; follows the table’s Παναχαιῶν "of the Achaeans all together" / "of all the Achaeans" |
| μείων (2.528–529, in stature) | "smaller" | "smaller" | "lesser" (the rank), "lower", "shorter"; the comparative of μικρός / ὀλίγος |
| Τελαμώνιος Αἴας | "Telamonian Ajax" | "Telamonian Ajax" | "Ajax son of Telamon", "greater Ajax"; the adjective is kept to tell the two Ajaxes apart, with ταχὺς Αἴας Ὀϊλῆος "swift Ajax, son of Oileus" |
| μένεα πνείοντες (2.536) | "breathing might" | "breathing might" | "breathing strength" (the Odyssey’s 22.203; a departure, with the reason: the Iliad has μένος "might" at 2.387 and keeps "strength" for κράτος and σθένος), "breathing fury" (reserved for μένος of anger), "breathing courage" |
| ὄπιθεν κομόωντες (2.542) | "long-haired behind" | "who wore their hair long behind" | "long-haired at the back", "with hair grown long behind" (the same sense), "back-haired"; κομάω "wear the hair long", as in κάρη κομόωντες "long-haired-of-head" |
| ὀρεκτῇσι μελίῃσι (2.543) | "outstretched ash-spears" | "outstretched ash-spears" | "long ash-spears", "reaching spears", "levelled spears"; ὀρεκτός "stretched out", μελίη "ash-spear" (Odyssey) |
| δήϊοι (δηΐων, 2.544) | "of enemies" | "enemies’" | "of the foe", "hostile"; δήϊος "hostile", used as a noun |
| περιτελλομένων ἐνιαυτῶν (2.551) | "as the years come round" | "as the years come round" | "as the seasons turn", "as the years revolve" (the table’s εἴνατος περιτροπέων ἐνιαυτός "as it comes round"); the verb is "come round" in both |
| ἐσχατόωσα (Ἀνθηδών, 2.508) | "lying at the edge" | "lying at the edge" | "farthest", "remote", "far-off", "outermost"; ἐσχατάω "lie at the edge" |
| ποιήεις (Ἁλίαρτος, 2.503) | "grassy" | "grassy" | "meadowy", "grass-rich", "lush"; from ποίη "grass" |
| πολύκνημος (Ἐτεωνός, 2.497) | "many-spurred" | "many-spurred" | "many-ridged" (reserved for πολυδειράς, 1.499), "many-kneed", "hilly"; κνήμη "shin", used of a hill’s foot |
| πολυτρήρων (Θίσβη, 2.502) | "rich in doves" | "rich in doves" | "dove-haunted", "of many doves", "dove-covered", "timorous" (the Odyssey’s τρήρωνες, 12.63, is the adjective; here the word is taken as the noun "dove", the usual explanation); follows πολύαρνι "rich in lambs" |
| πολυστάφυλος (Ἄρνη, 2.507; Ἱστίαια, 2.537) | "rich in grapes" | "rich in grapes" | "grape-laden", "rich in clusters", "of many vines" (reserved for ἀμπελόεις); the same rendering at both places |
| ἀμπελόεις (Ἐπίδαυρος, 2.561) | "vine-clad" | "vine-clad" | "vine-covered", "rich in vines", "vineyarded" |
| τειχιόεις (Τίρυνς, 2.559) | "walled" | "walled" | "well-walled" (reserved for εὐτείχεος), "wall-girt", "fortified" |
| ἔφαλος (Κήρινθος, 2.538) | "by the sea" | "by the sea" | "sea-girt", "on the sea", "seaside" |
| πετρήεις · εὐρύχορος (2.496, 2.498, 2.519) | "rocky" · "of wide dancing-grounds" | "rocky" · "spacious" | Odyssey wording, unchanged (εὐρύχορος `l` "of wide dancing-grounds", `i` "spacious", 4.635, 11.256, 11.265) (πετρήεσσα "rocky", 4.844) |
| ζάθεος · ἐϋκτίμενον πτολίεθρον · ζείδωρος ἄρουρα · βοὴν ἀγαθός · ἰσόθεος φώς · αἰδοίη · ἐϋκνήμιδες · τερπικέραυνος | per the table | per the table | reused from the table and the Odyssey unchanged (2.508, 2.520: "most holy"; 2.501, 2.505, 2.546: "the well-built citadel"; 2.548: "the grain-giving plough-land"; 2.563, 2.567: "good at the war-cry"; 2.565: "a man the equal of a god"; 2.514: "revered"; 2.478: "delighting-in-the-thunderbolt") |
| ναίω · νέμομαι · ἔχω (of dwelling, 2.496–2.562) | "dwelt in" · "inhabited" · "held" | "dwelt in" · "inhabited" · "held" | "lived in", "occupied", "possessed"; ναίω / ναιετάω "dwell", νέμομαι "inhabit", ἔχω "hold" are kept apart through the Catalogue |
| στιχάομαι (ἐστιχόωντο, 2.516) · ἀμφιέπω (ἀμφιέποντες, 2.525) | "went in line" · "busying themselves about" | "went in line" · "busying themselves about" | "marched" (iliad-008 ships "were marching" for ἐστιχόωντο said of the tribes, 2.91; of ships the word would mislead, so the departure keeps στίχες "lines" in the verb), "sailed in order" · "attending to", "tending"; the first is the verb of στίχες "ranks" |
| κατέχω (βαθὺν κατὰ κόλπον ἐχούσας, 2.560; tmesis) | "hold" | "hold" | "lie along", "embrace", "command"; the κατά is read with ἐχούσας |
| τοῖς / τῷ δὲ τριήκοντα γλαφυραὶ νέες ἐστιχόωντο (2.516) | "and for them thirty hollow ships went in line." | "and thirty hollow ships went in line with them." | "ships were drawn up", "sailed in rank"; follows γλαφυρῇσι νηυσί "hollow ships" (2.454) |
| ἐΰκτιτον (Αἰπύ, 2.592) | "well-founded" | "well-founded" | "well-built" (reserved for ἐϋκτίμενος, 2.569–570), "well-settled", "stately"; ἐΰκτιτος is from κτίζω "found", the root of ἐϋκτίμενος too, but a different word, and the Odyssey table turns "well-founded" down for the citadel phrase, which leaves it free here; Αἰπύ is the neuter of αἰπύς used as a name, "Aepy" |
| κυδιόων (2.579) | "glorying" | "glorying" | "exulting in glory" (κύδεϊ γαίων, 1.405), "proud", "swaggering", "taking pride in it" (adds an object); from κῦδος "glory" |
| λαός · λαοί (of an army, 2.577–580, 2.675; of a band of followers, 2.664) | "people" | "troops" (army) · "people" (band, 2.664) | "peoples" (reads as nations), "men", "host"; the Iliad keeps "the army" for λαὸν Ἀχαιῶν (2.450); plural λαοί and the following band at 2.664, who are not yet an army, are told apart in `i` only |
| ἄγω (of a force, ἦγε 2.631, ἄγεν 2.654, ἄγε 2.580, 2.671) | "brought" · "brought" | "brought" | "led" (reserved for ἄρχω and ἡγέομαι), "took", "marched"; ἄγω "bring" is kept apart from ἄρχω "lead" and ἡγεμονεύω "be leader" through the Catalogue |
| προθυμίῃσι (ᾗσι προθυμίῃσι πεποιθώς, 2.588) | "his own eagerness" | "his own eagerness" | "his own eagernesses" (a plural in the Greek, but English wants the singular), "zeal", "courage"; the plural noun is read as one disposition |
| τίσασθαι (Ἑλένης ὁρμήματα τε στοναχάς τε, 2.589–590) · στοναχή | "to avenge" · "groans" | "to avenge" · "groans" | "to make pay for", "to punish" (each decides the object), "to take vengeance for"; τίνομαι is the middle of τίνω "make pay", kept apart from τίω "honour" (1.508), whose avoided "avenge" belongs to the other verb; στοναχή keeps the "groaning" of στενάχω (1.364); ὁρμήματα keeps the shipped "strivings" (2.356) |
| Θρύον Ἀλφειοῖο πόρον (2.592) | "Thryum, the ford of the Alpheus" | same | "Thryon", "the crossing of the Alpheus"; πόρος "ford" as the Odyssey’s πόρος "passage" in a river; neuter names in -ον take Latin -um as for Thronium and Dium |
| Κυπαρισσήεις (2.593) | "Cyparisseis" | "Cyparisseis" | "Cyparisseeis", "Cypress-grown" (a name is kept as a name, the note gives the sense) |
| πηρόν (θέσαν πηρόν, 2.599) | "made … maimed" | "maimed" | "blinded", "made lame" (each decides the maiming the Greek leaves open), "crippled" |
| ἐκλέλαθον · κιθαριστύς (2.600) | "made … forget" · "lyre-playing" | "made … forget" · "lyre-playing" | "cause to forget" (stiff), "robbed of memory"; "the art of the lyre", "harp-playing" (κιθάρα is "lyre"); ἐκλανθάνω in the causative reduplicated aorist |
| στεῦτο (2.597) | "he declared" | "he claimed" | "he stood" (the sense of the Odyssey’s στεῦτο at 11.584, which does not fit with εὐχόμενος), "he swore", "he vowed"; follows the Odyssey’s στεῦται "declares" / "claims" (odyssey-087) |
| κοῦραι Διὸς αἰγιόχοιο (2.598) | "the daughters of aegis-bearing Zeus" | same | "the girls of …" (κούρη is "girl" in the table, but with a divine father the Odyssey ships "daughters"), "maidens"; reused from the Odyssey’s κοῦραι Διὸς αἰγιόχοιο |
| ἀγχιμαχητής (ἀνέρες ἀγχιμαχηταί, 2.604) | "close-fighters" | "fighters at close quarters" | "hand-to-hand fighters", "spearmen" (reserved for αἰχμητής), "near fighters"; ἀγχί "near" + μάχομαι "fight" |
| πολύμηλος (Ὀρχομενόν, 2.605) | "rich in flocks" | "rich in flocks" | "rich in sheep", "rich in apples" (a wrong guess for μῆλον), "many-flocked"; follows πολύαρνι "rich in lambs" and πολυστάφυλος "rich in grapes", with the Odyssey’s μῆλα "flocks" |
| θαλάσσια ἔργα (2.614) | "the works of the sea" | "the work of the sea" | "sea-faring", "sailing", "nautical matters"; ἔργον "work, deed" as in the Odyssey’s ἔργα βροτῶν |
| ἀτάλαντος Ἄρηϊ · ἀτάλαντος Ἐνυαλίῳ (2.627, 2.651) | "the equal of Ares" · "the equal of Enyalius" | same | "equal to Ares", "a match for Ares" (the Odyssey’s "a counsellor to match the gods" is a different phrase), "the peer of …"; follows the table’s Διὶ μῆτιν ἀτάλαντος "the equal of Zeus in cunning" (2.169, 2.636) |
| ἀνδρειφόντης (Ἐνυαλίῳ ἀνδρειφόντῃ, 2.651) | "killer of men" | "killer of men" | "man-killer" and "man-slaying" (ἀνδροφόνος "man-slaying", 1.242), "slayer of men", "man-slayer"; from ἀνήρ "man" + the root of φόνος "killing" |
| Ἀκτορίωνε (2.621, dual) | "the two of Actor’s line" | "the pair of Actor’s line" | "the Actorions", "the Molionids", "the twin sons of Actor" (adds "twin"); a dual patronymic naming the fathers Cteatus and Eurytus |
| ἡγησάσθην (2.620, dual aorist) | "led" | "led" | "were leaders" (reserved for ἡγεμονεύω), "were leading"; the dual is shown by the pair of names |
| νήσων, αἳ ναίουσι (2.626, of islands) | "islands, which lie" | "islands that lie" | "which dwell" (a place does not dwell), "which are inhabited"; ναίω "dwell" read as "lie" of an island |
| τίκτω (ὃν τίκτε … Φυλεύς, 2.628, of a father) | "begot" | "begot" | "bore" (kept for a mother, ὃν τέκεν Ἀστυόχεια, 2.658), "fathered", "sired"; τίκτω of a father is "beget" |
| ἀπενάσσατο (2.629) | "removed himself" | "removed himself" | "emigrated", "settled away", "withdrew"; ἀπο- "away" + ναίω "dwell" |
| ἀγέρωχος (Ῥοδίων ἀγερώχων, 2.654) | "lofty" | "lofty" (+ note: meaning not known) | Odyssey table (11.286), unchanged |
| ἠΰς (Τληπόλεμος … ἠΰς τε μέγας τε, 2.653) | "good" | "good" | "noble", "brave", "fine" (each decides the sense), "goodly"; ἠΰς is the epic ἐΰς and the Odyssey ships "good" for ἐΰς of a man (odyssey-089); μέγας is "great" |
| ἀργινόεις (ἀργινόεντα Λύκαστον, 2.647; Κάμειρον, 2.656) | "bright-white" | "bright-white" (+ note: sense not certain) | "gleaming-white", "shining white" ("gleaming" is the Odyssey’s for γλαυκῶπις, "shining" for φαεινός), "chalk-white", "snowy" (ἀγάννιφος), "white" alone; built on ἀργός "bright, white", the root also of ἀργής "bright", so "bright" is kept in the compound |
| ἑκατόμπολις (Κρήτην ἑκατόμπολιν, 2.649) | "hundred-citied" | "hundred-citied" | "of a hundred cities", "with a hundred cities", "hundred-towned"; ἑκατόν + πόλις, as ἑκατόγχειρον is "hundred-handed" (1.402) |
| δουρὶ κλυτός (Ἰδομενεύς, 2.645, 2.650; Τληπόλεμος, 2.657) | "famous with the spear" | "famous with the spear" | "spear-famed", "renowned for the spear", "glorious with the spear"; κλυτός "famous", as in κλυτοτέχνης "famous in craft" (1.571) and the Odyssey’s κλυτὸς ἐννοσίγαιος "the famous earth-shaker" |
| ἀγχίαλος (Χαλκίδα ἀγχίαλον, 2.640) | "near the sea" | "near the sea" | "by the sea" (kept for ἔφαλος, 2.538, 2.584), "sea-girt" (the Odyssey’s ἀμφίαλος), "on the coast"; ἀγχί "near" + ἅλς "sea" |
| πόλις · ἄστυ (πόλεις εὖ ναιετοώσας, 2.648; ἄστεα πολλὰ, 2.660) | "cities" · "towns" | "cities" · "towns" | "towns" for πόλις and "cities" for ἄστυ (the two words stay apart); follows the Odyssey’s ἄστυ "town" (εὐρυχόροιο ἄστεος "the spacious town") and πόλις "city" |
| εὖ ναιετοώσας (2.648) | "well-inhabited" | "well-inhabited" | "well-built", "comfortable", "prosperous"; follows the Odyssey table’s δόμους εὖ ναιετάοντας "the well-inhabited house" |
| βίη Ἡρακληείη (2.658, 2.666) | "the might of Heracles" | "the might of Heracles" | "the powerful figure of Heracles" (the Odyssey’s `i` at 11.601, where the word stands beside εἴδωλον "phantom" and "figure" fits a shade; a departure, with the reason: here the phrase is the father and forebear of living men, and "figure" would read as a body), "Heraclean might", "mighty Heracles" (erases the periphrasis); the Odyssey’s `l` "the might of Heracles" is kept, the same words in the dative (2.658) and the genitive (2.666) |
| διὰ τρίχα · τριχθά (2.655, 2.668) | "in three parts" | "in three parts" | "in three divisions", "threefold", "by threes"; the same adverb at both places |
| καταφυλαδόν (2.668) | "tribe by tribe" | "tribe by tribe" | "by clans" (kept for φρήτρη), "in tribes", "each by itself"; from κατὰ φυλάς, φῦλον keeping "tribe" (2.362) |
| κατέχευε (πλοῦτον, 2.670) | "poured down" | "poured down" | "showered", "heaped"; καταχέω "pour down", κατά in tmesis as at 1.413 |
| πλοῦτος (θεσπέσιον πλοῦτον, 2.670) | "riches" | "riches" | "wealth" (kept for ἄφενος, 1.171), "treasure"; θεσπέσιος keeps "wondrous" |
| εὔπηκτος (μεγάρῳ εὐπήκτῳ, 2.661) | "well-framed" | "well-framed" | "well-built" (reserved for ἐϋκτίμενος), "well-fastened", "well-joined"; εὖ + πήγνυμι "fix, fit together", the verb of ἔπηξε (2.664) |
| μήτρως (πατρὸς ἑοῖο μήτρωα, 2.662) | "mother’s-brother" | "mother’s brother" | "maternal uncle", "uncle" alone (loses the mother); the note says whose mother |
| αἶψα · αὐτίκα (2.662, 2.664) | "quickly" · "at once" | "quickly" · "at once" | the Odyssey table’s αἶψα "quickly" and αὐτίκα "at once", kept apart in two lines that stand next to each other |
| ἀλαπαδνός (2.675) | "feeble" | "feeble" | "weakling", "frail", "unwarlike" (kept for ἀπτόλεμος, 2.201), "weak"; ἀλαπαδνός "feeble, easily drained" |
| παῦρος (παῦρος … λαός, 2.675) | "scanty" | "few" | "small", "slight", "meagre"; singular adjective on a collective noun, so `l` keeps "scanty" and `i` says "the troops … were few" |
| Νιρεύς … Νιρεύς … Νιρεύς (2.671–673) | "Nireus … Nireus … Nireus" | "Nireus … Nireus … Nireus" | one Nireus with the rest as relative clauses (hides the repeated opening, a rhetorical device of the poet’s); both layers keep the three names |
| ὅσσον … ἐντὸς ἐέργει (2.616–617; ἐφ’ construction unsettled) | "as much as … shut in within" | "all the land that … shut in" | "as far as … enclose" (reads ἐφ’ as a limit), "all that … lies between"; the note says the construction is compressed and the English reads the four places as the boundary |
| Σάμος (2.634) | "Samos" | "Samos" | "Same" (the Odyssey’s Σάμη; the identification is probable, not certain), "Samos of Ionia"; the note says it is probably the Odyssey’s Same |
| δυσηχής (πολέμοιο δυσηχέος, 2.686) | "ill-sounding" | "ill-sounding" | "dreadful" and "dread" (reserved for δεινός), "grim", "noisy", "clamorous"; δυσ- "ill" + ἦχος "sound", so both parts show |
| ἄναρχος · ἀρχός (οὐδ’ οἳ ἄναρχοι ἔσαν, πόθεόν γε μὲν ἀρχόν, 2.703, 2.726) | "without a commander" · "commander" | "not without a commander" · "commander" | "leaderless" (loses ἀρχός, and ἡγεμών is "leader"), "headless"; ἀ- + ἀρχός, with the repeated word kept in both layers |
| ποθέω (πόθεον 2.703, 2.709, ποθέοντες 2.778) | "longed for" · "longing for" | "missed" · "missing" | "yearned for", "regretted", "wanted" (reserved for δεύομαι "lack"); the Odyssey ships "missing" and "longing for" for ποθέοντες (odyssey-079, odyssey-109) |
| δεύομαι (δεύονθ’ ἡγεμόνος, 2.708) | "lack" | "lack" | "want", "be without"; keeps the "lack" of ἐδεύετο (1.602) |
| ἀρήϊος (Πρωτεσίλαος ἀρήϊος, 2.698, 2.708) | "warlike" | "warlike" | "martial", "valiant", "of Ares"; the Odyssey ships "warlike" (odyssey-010), and "steadfast in battle" is reserved for μενεπτόλεμος |
| ἀρείων (ὁ δ’ ἅμα πρότερος καὶ ἀρείων, 2.707) | "braver" | "braver" | "better" (kept for ἀμείνων, 2.239), "nobler", "stronger" (reserved for φέρτερος); the comparative is "better" in courage |
| πρότερος (2.707, of age) | "elder" | "elder" | "earlier", "former", "first-born"; the comparative of πρό "before", in the sense "born before" |
| κόσμησε (2.704, 2.727) | "set in order" | "marshalled" | "arranged", "drew up", "commanded"; follows κοσμῆσαι "to marshal" (2.554) in `i`, and διεκόσμεον "set in order" (2.476) in `l` |
| ὄζος Ἄρηος (Ποδάρκης, 2.704; Λεοντεύς, 2.745) | "scion of Ares" | "scion of Ares" | as in the table's Ἐλεφήνωρ row; the title is given to Podarces and to Leonteus alike |
| ποδάρκης (as a man's name, Ποδάρκης, 2.704) | "Podarces" | "Podarces" | "Swift-foot", "Podarkes"; the name is the same word as Achilles' epithet ποδάρκης (2.688, "swift-footed"), and the note says so |
| ἀμφιδρυφής (2.700) | "torn on both sides" | "with her cheeks torn in mourning" (+ note: the Greek says only "torn all round") | "scratched", "tearing her face", "in grief" alone (each decides what is torn); ἀμφί "on both sides" + δρύπτω "tear", and the usual explanation, from the lexicon, is that the wife has torn her cheeks in mourning |
| ἡμιτελής (δόμος, 2.701) | "half-finished" | "half-finished" | "half-built", "unfinished", "incomplete"; ἡμι- "half" + τελέω "finish", and "built" would decide what was left undone |
| λεχεποίης (Πτελεὸν λεχεποίην, 2.697) | "grass-bedded" | "with its beds of grass" (+ note: rare word, usual explanation) | "meadowy" and "grassy" (reserved for ποιήεις), "soft-bedded", "with grassy meadows"; λέχος "bed" + ποίη "grass" |
| μητέρα μήλων (Ἴτωνα, 2.696) | "mother of flocks" | "mother of flocks" | "nurse of flocks", "breeder of sheep", "mother of sheep"; μῆλα are "flocks" (πολύμηλος "rich in flocks"), and the image of "mother" is kept |
| τέμενος (Δήμητρος τέμενος, 2.696) | "precinct" | "precinct" | "sanctuary", "grove", "estate" (the Odyssey's `i` for τέμενος of ploughland, 17.299, which does not fit a god's ground); the `l` "precinct" is the Odyssey's (odyssey-029, odyssey-036) |
| ἀνθεμόεις (Πύρασον ἀνθεμόεντα, 2.695) | "flowery" | "flowery" | "blossoming", "flower-decked"; follows the Odyssey's ἀνθεμόεντα "flowery" (the meadow of the Sirens), not the "decorated with flowers" of the bowl, which is a pattern on metal |
| Ἑλλάδα καλλιγύναικα (2.683) | "Hellas of the fair women" | "Hellas of the fair women" | "with beautiful women", "land of lovely women"; follows the Odyssey's Σπάρτην … καλλιγύναικα "Sparta of the fair women" (13.412); the name stays "Hellas", a district, and Ἕλληνες is "Hellenes", not "Greeks" |
| Ἕλληνες (2.684) | "Hellenes" | "Hellenes" | "Greeks" (avoided in both layers by the conventions), "men of Hellas"; one of the three names of Achilles' people, with Μυρμιδόνες "Myrmidons" and Ἀχαιοί "Achaeans" |
| ἐγχεσίμωρος (ἐγχεσιμώρους, 2.692) | "spear-wielding" | "spear-wielding" | "spear-brandishing" (reserved for ἐγχέσπαλος, 2.131), "famed with the spear", "renowned spearman"; reused from the Odyssey (odyssey-010) |
| τόξων ἐῢ εἰδώς · τόξων εὖ εἰδότες (2.718, 2.720) | "well knowing the bow" | "who knew the bow well" · "who knew the bow well" | "skilled in archery", "master of the bow", "expert with bows" (each loses εἰδώς "knowing"); εὖ εἰδώς keeps the "knew well" of iliad-004 (1.384); τόξα is the bow, the plural being the usual Greek way of saying it |
| ἐρέται (2.719) | "oarsmen" | "oarsmen" | "rowers", "sailors"; keeps the Odyssey's "oarsmen" and the "oarsmen" of ἐρέτας ἐπιτηδές (1.142) |
| κρατέρ’ ἄλγεα πάσχων (2.721) | "suffering harsh pains" | "suffering harsh pains" | "strong pains", "severe pains" (the Odyssey ships all three in different places); follows odyssey-022, where the same half-line is said of Odysseus lying on Calypso's island |
| μοχθίζω (μοχθίζοντα, 2.723) | "toiling" | "suffering" | "labouring", "struggling", "in agony" (adds a degree); μοχθέω is "toil" and the sense here is the effect of the wound |
| ὕδρος (ὀλοόφρονος ὕδρου, 2.723) | "water-snake" | "water-snake" | "hydra" (a proper name of the monster), "serpent", "viper"; ὕδρος is ὕδωρ's snake, and ὀλοόφρων keeps the Odyssey's "baleful-minded" |
| ἔνθ’ ὅ γε κεῖτ’ ἀχέων (2.724) | "There he lay grieving" | "There he lay grieving" | "groaning", "in anguish"; follows the Odyssey (odyssey-052, "There he lies grieving"); ἀχέω "grieve" |
| νόθος (Ὀϊλῆος νόθος υἱός, 2.727) | "bastard" | "illegitimate" | "base-born", "natural son", "bastard" in `i` (loaded in modern English); the word is "born outside marriage" |
| πτολίπορθος (Ὀϊλῆϊ πτολιπόρθῳ, 2.728) | "city-sacking" | "sacker of cities" | "city-destroyer", "destroyer of cities"; follows the Odyssey's πτολιπόρθιος "city-sacking" / "sacker of cities" (odyssey-070), and πέρθω stays "sack" |
| κλωμακόεις (Ἰθώμην κλωμακόεσσαν, 2.729) | "stony" | "stony" (+ note: sense not certain, "terraced" another reading) | "rocky" (reserved for πετρήεις, 2.496), "craggy" (σκόπελος "crag"), "terraced" (decides the open sense); κλῶμαξ "heap of stones" |
| τρηχεῖαν (Ὀλιζῶνα τρηχεῖαν, 2.717) | "rough" | "rough" | "rugged" (the Odyssey's wording for a shore, odyssey-026), "harsh"; follows iliad-013's "rough Aegilips" (2.633) |
| ἰητῆρ’ ἀγαθώ (2.732, dual) | "two good healers" | "good healers both" | "doctors", "physicians", "skilled in medicine"; ἰητήρ keeps the Odyssey's "healer", and the dual is shown by "two" and "both" |
| κάρηνα (Τιτάνοιό τε λευκὰ κάρηνα, 2.735) | "peaks" | "peaks" | "heads" (kept for the Iliad's cities at 2.117 and the Odyssey's "heads" of the dead), "summits"; κάρηνα of mountains is "peaks", as in the Odyssey's ὀρέων … κάρηνα |
| λευκός (πόλιν Ὀλοοσσόνα λευκήν, 2.739; λευκὰ κάρηνα, 2.735) | "white" | "white" | "gleaming" (kept for the Odyssey's γλαυκῶπις), "bright" (kept for ἀργός), "chalky"; ἀργινόεις stays "bright-white" |
| Φῆρες · λαχνήεις (Φῆρας … λαχνήεντας, 2.743) | "the hairy beasts" | "the hairy beasts" | "Centaurs" (names what the Greek leaves unnamed, as at 1.268), "shaggy" (reserved for λάσιος, 1.189), "wild"; φήρ is "beast" and λαχνήεις "hairy" |
| ἐτίσατο (Φῆρας ἐτίσατο, 2.743) | "took vengeance on" | "took vengeance on" | "avenged himself on", "punished", "repaid"; the middle of τίνω, with the person as object; τίσασθαι "to avenge" (2.590) has a thing as object, and `l`/`i` there are the same verb |
| ὦσε … πέλασσεν (2.744) | "thrust … brought near" | "pushed … forced on to" | "drove" (reserved for ἐλαύνω and στυφελίζω), "banished"; ὠθέω "push", πελάζω "bring near" |
| οὐκ οἶος (2.745) | "not alone" | "did not lead alone" (the verb supplied from 740, as the note says) | "not by himself"; οἶος "alone" |
| δυσχείμερος (Δωδώνην δυσχείμερον, 2.750) | "harsh-wintered" | "of the harsh winters" | "wintry" (reserved for χειμέριος, the Odyssey's "wintry" storms), "stormy", "cold"; δυσ- "ill" + χεῖμα "winter" |
| οἰκί’ ἔθεντο (2.750) | "made their homes" | "made their homes" | "set up houses", "built their dwellings" (decides how); οἰκία "homes", τίθεμαι "make, set up" |
| ἔργα νέμοντο (Τιταρησσόν, 2.751) | "inhabited the farmlands" | "inhabited the farmlands" | "tilled the fields" (νέμομαι is "inhabit"), "had their farmlands" (that is ἔχω "hold", kept apart from νέμομαι through the Catalogue), "held the works"; ἔργα as the tilled land, and νέμομαι keeps "inhabit" |
| ἱμερτός (Τιταρησσόν, 2.751) | "lovely" | "lovely" | "desirable", "charming"; the Odyssey ships "lovely" for ἱμερτός / ἱμερόεις |
| καλλίρροος (ὕδωρ, 2.752) | "fair-flowing" | "fair-flowing" | "beautifully-flowing"; καλλι- "fair" + ῥόος "stream"; chosen here, no published Odyssey unit has the word |
| ἀργυροδίνης (Πηνειῷ ἀργυροδίνῃ, 2.753) | "silver-eddying" | "silver-eddying" | "silver-swirling", "silvery", "with silver whirlpools"; ἀργυρο- "silver" + δίνη "eddy", the stock epithet of a river |
| ἠΰτ’ ἔλαιον (2.754) | "like olive-oil" | "like olive oil" | "like oil" alone (loses the plant); ἠΰτε "like" (1.359) |
| ὅρκου δεινοῦ Στυγὸς ὕδατος … ἀπορρώξ (2.755) | "of the dread oath, the water of the Styx … an offshoot" | "an offshoot of the water of the Styx, the dread oath" | "branch", "tributary", "outlet" (the Odyssey ships "offshoot" for ἀπορρώξ of Cocytus, 10.514, and "the water of the Styx" for the same half-line Στυγὸς ὕδατός ἐστιν ἀπορρώξ); the three genitives are kept in apposition |
| ναίεσκον (2.758) | "kept dwelling" | "dwelt" | "used to dwell", "would dwell" (the iterative suffix is shown by "kept" in `l`); ναίω "dwell" kept apart from νέμομαι and ἔχω through the Catalogue |
| θοός (Πρόθοος θοός, 2.758) | "swift" | "swift" | "quick", "nimble", "fleet" (reserved for ποδώκης); θοός "swift", as of ships in the Odyssey |
| κοίρανοι (2.760) | "rulers" | "rulers" | "lords" (reserved for ἄναξ), "princes", "captains"; keeps the Odyssey's κοίρανος "ruler" |
| ὄχ’ ἄριστος (τίς τὰρ τῶν ὄχ’ ἄριστος ἔην, 2.761) | "by far the best" | "far the best" | "the very best", "the finest of them"; follows οἰωνοπόλων ὄχ’ ἄριστος (1.69) |
| ἔννεπε Μοῦσα (σύ μοι ἔννεπε Μοῦσα, 2.761) | "do you tell me, Muse" | "tell me, Muse" | "sing" (reserved for ἀείδω), "declare"; keeps the Odyssey's ἔννεπε "tell" and iliad-012's ἔσπετε "tell" |
| μέγ’ ἄρισται (ἵπποι, 2.763) | "by far the best" | "by far the best" | "the best of all", "far the finest"; μέγα as an adverb, "by far", while ὄχα is "far" |
| Φηρητιάδαο (2.763) | "Pheres’-son" | "the son of Pheres" (+ note: the man meant is usually taken to be Admetus) | "Pheres’ son" (the patronymic is hyphenated in `l` as at Ἀτρεΐδης "Atreus’-son"), "Pheretiades", "descendant of Pheres" (a patronymic does not always mean the son); the name is not given in the Greek |
| ὄτριχας οἰέτεας (2.765) | "alike in hair, of one age" | "alike in hair, of one age" (+ note: sense not certain) | "of one coat", "of equal years", "matched in colour"; ὄτριχας is perhaps ὁμο- + θρίξ, οἰέτεας probably οἶος "one" + ἔτος "year", and neither is certain |
| σταφύλῃ ἐπὶ νῶτον ἐΐσας (2.765) | "well-balanced along the back by the plumb-line" | "well-balanced along the back as if by the plumb-line" | "level", "even" (reserved against ἐΐσας "well-balanced"), "straight as a plumb-line"; ἐΐσας keeps the "well-balanced" of νῆας ἐΐσας (1.306), and σταφύλη is a plumb-line |
| ποδώκης (ποδώκεας, 2.764) | "fleet-footed" | "fleet-footed" | "swift-footed" (reserved for ποδάρκης), "swift of foot" (πόδας ὠκύς); πούς + ὠκύς |
| θρέψ’ (τρέφω, 2.766) | "reared" | "reared" | "nursed", "fed", "bred"; keeps the "reared" of Athena and Erechtheus (θρέψε, 2.548) |
| θηλείας (ἵππους, 2.767) | "female" | "mares" | "female horses", "she-horses"; ἵπποι is feminine here and the note says the pair are mares |
| φόβον Ἄρηος φορεούσας (2.767) | "carrying the terror of Ares" | "carrying the terror of battle" | "bearing the panic of Ares", "carrying flight", "fear of the war-god"; Ἄρηος as war (2.401, μῶλον Ἄρηος), φόβος "terror" |
| μήνιεν (ὄφρ’ Ἀχιλεὺς μήνιεν, 2.769) | "was wrathful" | "was wrathful" | "was angry", "nursed his wrath", "raged"; keeps ἐμήνιε "was wrathful" (1.247) |
| ἀπομηνίσας (κεῖτ’ ἀπομηνίσας, 2.772) | "withdrawn in wrath" | "withdrawn in wrath" (+ note: the force of ἀπο- is not certain) | "ceased from wrath", "having raged out his anger", "in full wrath" (each decides ἀπο-); μηνίω "be wrathful" + ἀπο- "away", with the dative of the one he is wrathful at |
| κορωνίς · ποντοπόρος (νήεσσι κορωνίσι ποντοπόροισι, 2.771) | "curved, sea-crossing" | "curved, sea-crossing" | "beaked", "sea-faring", "sea-going", "hollow" (reserved for γλαφυρός / κοῖλος); Odyssey table, unchanged |
| φέρτατος (πολὺ φέρτατος, 2.769) | "by far the best" | "by far the best" | "the strongest" (κάρτιστοι), "mightiest"; keeps the Odyssey's πολὺ φέρτατος "by far the best" |
| φορέεσκον (2.770) | "kept carrying" | "carried" | "used to carry", "were wont to carry"; φορέω "carry", the iterative shown by "kept" in `l` |
| τέρποντο … ἱέντες (δίσκοισιν … αἰγανέῃσιν … τόξοισιν, 2.774–775) | "were taking delight … throwing" | "were amusing themselves throwing the discus and the javelin, and shooting with bows" | "enjoyed", "took pleasure"; the line is the Odyssey's (4.626), reused for its own words, with ἱέντες "throwing" governing the bows of the next half-line as "shooting" |
| ῥηγμίν (παρὰ ῥηγμῖνι θαλάσσης, 2.773) | "the surf-line of the sea" | "the shore where the sea breaks" | "the beach", "the water's edge"; follows iliad-005 and the Odyssey |
| λωτός (2.776) | "lotus" | "lotus" (+ note: here a fodder plant) | "clover" (decides the plant; the Odyssey does ship "clover" for the λωτός of the plain of Sparta, 4.603, a pasture list, but the half-line λωτὸν ἐρεπτόμενοι is "feeding on lotus" there, 9.97, and the Iliad keeps the half-line), "water-lily", "trefoil"; the Odyssey ships "lotus" for λωτός of the Lotus-eaters and says which plant is not known |
| ἐλεόθρεπτος (σέλινον, 2.776) | "marsh-nurtured" | "marsh-nurtured" | "marsh-fed", "marsh-bred", "growing in the marsh" (drops θρέπτος); ἕλος "marsh" + τρέφω "nurture", as in the table's διοτρεφής "Zeus-nurtured" |
| σέλινον (2.776) | "celery" | "celery" (+ note: celery or a like plant) | "parsley", "wild celery", "marsh-parsley"; the plant is not told apart from its near relatives |
| ἐρέπτομαι (ἐρεπτόμενοι, 2.776) | "feeding on" | "feeding on" | "eating", "grazing", "browsing", "cropping"; keeps the Odyssey's λωτὸν ἐρεπτόμενοι "feeding on lotus" (odyssey-039; πυρὸν ἐρεπτομένους "eating wheat", odyssey-097, has another object) |
| ἕστασαν (2.777) | "stood" | "stood" | "had stood", "were standing" (it is the pluperfect of ἵστημι with a past sense) |
| πεπυκασμένα (ἅρματα δ’ εὖ πεπυκασμένα, 2.777) | "well covered" | "well covered" | "well wrapped", "closely covered", "well built" (the other sense of πυκάζω); πυκάζω "cover closely", kept apart from πυκινός "shrewd" |
| ἀρηΐφιλος (ἀρχὸν ἀρηΐφιλον, 2.778) | "Ares-loved" | "dear to Ares" | "war-loving", "beloved of Ares"; follows the Odyssey's ἀρηΐφιλος Μενέλαος "Ares-loved Menelaus" / "Menelaus, dear to Ares" (15.169) |
| φοιτάω (φοίτων, 2.779) | "went to and fro" | "went to and fro" | "roamed", "wandered", "kept coming and going"; keeps the Odyssey's "went to and fro" (odyssey-069) |
| οὐδὲ μάχοντο (2.779) | "and did not fight" | "and did not fight" | "nor fought" in `i`, "held back from battle"; μάχομαι "fight" |
| νέμοιτο (πυρὶ χθὼν πᾶσα νέμοιτο, 2.780, of fire) | "were being fed upon" | "were being consumed" | "grazed", "ranged over", "devoured" (kept for the fire of ἀΐδηλον, 2.455); νέμομαι is "inhabit" of men in the Catalogue (2.751, 2.835), and the note says it is a different sense here |
| ὑπεστενάχιζε (2.781) | "groaned beneath" | "groaned beneath" | "groaned under", "rumbled", "shuddered"; στεναχίζω keeps "groan" (1.364), with ὑπο- shown |
| Ἀρίμοις (εἰν Ἀρίμοις, 2.783) | "among the Arimi" | "among the Arimi" | "in Arima" (decides a place), "among the Arimians"; people or place not known, and the note says so |
| εὐνάς (Τυφωέος ἔμμεναι εὐνάς, 2.783) | "the beds of Typhoeus" | "Typhoeus has his bed" | "lair", "resting place" (each decides the sense), "couches"; the plural is one lair |
| διαπρήσσω + genitive (διέπρησσον πεδίοιο, 2.785) | "were crossing" | "were crossing" | "accomplishing" (the table keeps that for διαπρήσσουσα κέλευθον, which has its object), "making their way through"; the genitive is the ground covered |
| ποδήνεμος Ἶρις (2.786) | "wind-footed" | "wind-footed" | "wind-swift" (ἄνεμος + πούς, not ἀελλόπος), "storm-footed", "swift as the wind" (adds a comparison), "fleet-footed" (reserved for ποδώκης); ὠκέα Ἶρις alone is "swift Iris" |
| πόδας ὠκέα Ἶρις (2.790, 2.795) | "swift-in-feet Iris" | "Iris, swift of foot" | "swift-footed" (ποδάρκης), "fleet-footed" (ποδώκης); the feminine of the table’s πόδας ὠκὺς Ἀχιλλεύς |
| ἀγχοῦ δ’ ἱσταμένη προσέφη πόδας ὠκέα Ἶρις (2.790; departure from the Odyssey’s ἀγχοῦ δ’ ἱσταμένη προσέφη γλαυκῶπις Ἀθήνη, odyssey-071 and iliad-008) | "And standing close by, swift-in-feet Iris spoke;" | "Iris, swift of foot, came and stood close by, and spoke;" | "addressed him" / "said to him" (the shipped Odyssey and iliad-008 wording; in them a person is addressed at once, while here the Greek names no one until 795 and the speech starts only at 796), "addressed them" (supplies the assembly) |
| ἀγγελίη ἀλεγεινή (σὺν ἀγγελίῃ ἀλεγεινῇ, 2.787) | "grievous news" | "grievous news" | "message" (the Odyssey’s draft word, withdrawn), "tidings", "painful report"; follows the Odyssey’s ἀγγελίη "news" and ἀλεγεινός "grievous" |
| ἀγορὰς ἀγόρευον (2.788) | "were holding assemblies" | "were meeting in assembly" | "were declaring assemblies", "were making speeches" (the cognate noun is kept visible in `l`); ἀγορεύω is "declare" in a public pronouncement, and with its own noun it is "hold assembly" |
| ὁμηγερής (ὁμηγερέες, 2.789) | "gathered together" | "gathered together" | "assembled", "met together"; ὁμο- "same" + ἀγείρω "gather" |
| εἴσατο φθογγήν (2.791) | "made herself like in voice" | "made herself like … in voice" | "took the voice of" (loses εἴσατο), "imitated"; the aorist middle of εἴδομαι, kept as in ἐεισάμενος "making himself like" (2.22) |
| σκοπός (Τρώων σκοπός, 2.792) | "lookout" | "lookout" | "scout", "watchman", "spy"; σκοπέω "look" |
| ποδωκείη (ποδωκείῃσι πεποιθώς, 2.792) | "fleet-footedness" | "speed of foot" | "his legs", "swiftness" alone; the abstract noun of ποδώκης "fleet-footed", and πεποιθώς is "trusting in" |
| τύμβος (τύμβῳ ἐπ’ ἀκροτάτῳ, 2.793) | "on the topmost tomb" | "on the very top of the tomb" | "mound", "barrow" (the Odyssey’s "mound" at 3.239, but iliad-013 ships "tomb" for τύμβος in the Iliad), "highest"; ἀκρότατος keeps "topmost" as in ἀκροτάτῃ κορυφῇ "on the topmost peak" |
| δέγμενος ὁππότε … ἀφορμηθεῖεν (2.794) | "waiting for when … should set out" | "waiting for the moment when … should set out" | "watching for", "ready for"; the optative marks an expected event, and δέχομαι "receive" is "wait for" |
| ὦ γέρον (2.796) | "Old man" | "Old man" | "Father", "Sire", "Elder"; "old man" is reserved for ὦ γέρον in the Odyssey table (cf. πάτερ ὦ ξεῖνε) |
| μῦθοι φίλοι ἄκριτοί (2.796) | "words … dear, unsorted" | "endless talk … dear" | "indecisive", "confused" (the Odyssey’s "indistinct" for ἀκριτόμυθοι, a different word), "undecided"; ἄκριτος keeps the Iliad’s "unsorted" (ἀκριτόμυθε, 2.246), and `i` gives the sense, never reaching a decision |
| ἀλίαστος (πόλεμος ἀλίαστος, 2.797) | "relentless" | "relentless" | "unceasing" (kept for ἄλληκτον, 2.452), "unyielding", "unrelenting" (the note gives ἀ- + λιάζομαι as a possible origin) |
| εἰσήλυθον (μάχας εἰσήλυθον ἀνδρῶν, 2.798) | "I have gone into" | "I have gone into" | "I have entered", "I have been in"; the aorist of εἰσέρχομαι with a perfect sense |
| φύλλοισιν ἐοικότες ἢ ψαμάθοισιν (2.800) | "like leaves or sands" | "like leaves or sands" | "as numerous as" (the point of the comparison is their number, but the Greek does not say it), "grains of sand"; ψάμαθος is "sand" as in the shipped "sands" (iliad-005, odyssey-009, odyssey-017) |
| προτὶ ἄστυ (2.801) | "toward the town" | "toward the town" | "to the city" (πόλις is "city"); ἄστυ keeps the Odyssey’s "town" |
| ἐπιτέλλομαι (2.802, middle, with a person and an infinitive) | "I enjoin" | "I give this charge" | "I command", "I bid" (reserved for κελεύω); follows ἐπιτέλλω "enjoin / charge" (2.10) and ἐπιτέλλεο "lay these charges" (1.295) |
| πολυσπερέες (πολυσπερέων ἀνθρώπων, 2.804) | "widely scattered" | "widely scattered" | "far-sown", "of many seeds", "scattered far and wide"; πολύς + σπείρω |
| ἄλλη δ’ ἄλλων γλῶσσα (2.804) | "different of different men is the tongue" | "there is a different tongue for each" | "speech" for γλῶσσα in `l` (the Odyssey’s `i` in odyssey-093 has "a different speech for each people"); γλῶσσα keeps "tongue" in `l` |
| σημαινέτω (2.805) | "let him give orders" | "let him give orders" | "signal", "give the word", "mark out"; follows iliad-003’s σήμαιν’ "give orders" |
| ἐξηγείσθω … κοσμησάμενος πολιήτας (2.806) | "let him lead out, having marshalled the citizens" | "lead them out once he has marshalled his fellow-citizens" | "set in array", "draw up"; κοσμέω keeps "marshal" (2.554), and πολιήτης is "citizen" |
| ἔλυσ’ ἀγορήν (2.808) | "loosed the assembly" | "broke up the assembly" | "dissolved" (as a term), "dismissed", "released"; λύω is "loose / release", and `i` takes the sense of ending a meeting |
| τεύχεα (ἐπὶ τεύχεα, 2.808) | "armour" | "armour" | "arms", "gear", "weapons"; follows the Odyssey’s τεύχεα "armour" (12.228, 22.114) |
| ὠΐγνυντο πύλαι (2.809) | "were being opened" | "were opened" | "were thrown open", "flew open" (each adds force); ὀΐγνυμι is "open" |
| πεζοί θ’ ἱππῆές τε (2.810) | "both on foot and horsemen" | "both on foot and mounted" | "infantry and cavalry", "foot-soldiers and charioteers"; the Odyssey’s wording (odyssey-115) |
| ὀρυμαγδός · ὀρώρει (2.810) | "a great din had sprung up" | "a great din went up" | "tumult", "uproar", "had arisen"; follows the Odyssey’s πολὺς … ὀρώρει "a great din" (odyssey-036) and its "had sprung up" |
| κολώνη (αἰπεῖα κολώνη, 2.811) | "hill" | "hill" | "mound" (kept for τύμβος in the Odyssey’s 3.239), "knoll", "barrow"; with αἰπεῖα "steep" |
| περίδρομος (2.812) | "that can be run round" | "with room to run round it" | "encircled", "open on all sides", "with a path round it"; ἔνθα καὶ ἔνθα is "on this side and on that" |
| σῆμα (ἀθάνατοι δέ τε σῆμα … Μυρίνης, 2.814) | "tomb" | "tomb" | "sign" (kept for the Odyssey’s σῆμα ἄνακτι, 20.111), "monument", "mound"; a mark over a grave |
| πολυσκάρθμοιο (Μυρίνης, 2.814) | "much-leaping" | "much-leaping" | "swift-leaping", "bounding", "nimble"; πολύς + σκαρθμός "leap", and who Myrine was is not said |
| διέκριθεν (2.815) | "were parted" | "were parted" | "were sorted" (kept for κρίνω), "were divided", "were drawn up" (each decides the sense); the same verb as διακρινέει "parts" (2.387) |
| κορυθαίολος (Ἕκτωρ, 2.816) | "of the glancing helmet" | "of the glancing helmet" (+ note: κόρυς "helmet" + αἰόλος "quick-moving, glancing") | "flashing" (reserved for ἀστεροπητής), "shining" (φαεινός), "gleaming" (γλαυκῶπις), "shifting" (ποικιλομήτης), "tossing-plumed", "with the nodding helm" |
| Πριαμίδης (2.817) | "Priam’s-son" | "son of Priam" | "Priam’s son" unhyphenated in `l`; follows Ἀτρεΐδης "Atreus’-son" / "son of Atreus" |
| πολὺ πλεῖστοι καὶ ἄριστοι (2.817) | "by far the most numerous and the best" | "by far the most numerous and the best" | "the most and the best", "far the largest and the finest"; follows πολὺ φέρτατος "by far the best" |
| μεμαότες ἐγχείῃσι (2.818) | "eager with spears" | "eager with their spears" | "brandishing", "raging with the spear"; μέμονα "be eager", ἐγχείη "spear" |
| ἐῢς πάϊς Ἀγχίσαο (2.819) | "the good son of Anchises" | "the good son of Anchises" | "noble", "brave", "stalwart"; follows the Odyssey’s ἀγαθὸς πάϊς Ἀλκινόοιο "the good son of Alcinous" and ἠΰς "good" (2.653) |
| κνημός (Ἴδης ἐν κνημοῖσι, 2.821) | "in the spurs" | "in the spurs" | "glens", "folds", "slopes", "knees"; κνημός "mountain-spur", of the same word as πολύκνημος "many-spurred" (2.497) |
| εὐνηθεῖσα (θεὰ βροτῷ εὐνηθεῖσα, 2.821) | "having lain with" | "who had lain with" | "bedded", "been put to bed by", "made love to"; follows the Odyssey’s εὐνηθῆναι "to lie with her" (10.296) |
| μάχης εὖ εἰδότε πάσης (2.823) | "knowing all fighting well" | "who both knew all fighting well" | "skilled in every kind of battle", "masters of the fight"; εὖ εἰδώς keeps "knew … well" (2.718) |
| ὑπαὶ πόδα νείατον Ἴδης (2.824) | "beneath the lowest foot of Ida" | "beneath the lowest foot of Ida" | "at the foot of Ida" (loses νείατον), "the bottom of the mountain"; πούς of a mountain is "foot" |
| ἀφνειός (2.825) | "rich" | "rich" | "wealthy", "opulent"; the Odyssey’s "rich" |
| δῆμον Ἀπαισοῦ (2.828) | "the land of Apaesus" | "the land of Apaesus" | "the people of Apaesus", "the township"; δῆμος of a place is "land", as in the Odyssey table |
| ὄρος αἰπύ (Τηρείης ὄρος αἰπύ, 2.829) | "the steep mountain" | "the steep mountain" | "sheer", "lofty"; αἰπύς keeps "steep" (iliad-013, 2.603) |
| μαντοσύνας ᾔδεε (2.831–832) | "knew seercraft" | "knew the arts of prophecy" | "the prophetic art", "divination"; follows iliad-001’s μαντοσύνην "seercraft" / "gift of prophecy" and the Odyssey’s μαντοσύνη "seercraft" / "art of prophecy" |
| ἔασκε (οὐδὲ οὓς παῖδας ἔασκε στείχειν, 2.832) | "nor … did he keep allowing" | "would not allow" | "used not to let", "would not let"; the iterative suffix is shown by "kept" in `l`, as for ναίεσκον "kept dwelling" |
| φθισήνωρ (πόλεμον φθισήνορα, 2.833) | "man-wasting" | "that wastes men" | "man-destroying", "man-killing" (ἀνδροφόνος "man-slaying"), "destroyer of men"; φθίω "waste" + ἀνήρ "man" |
| κῆρες … μέλανος θανάτοιο (2.834) | "death-spirits of black death" | "spirits of black death" | "fates of dark death", "dark deaths"; follows iliad-010’s κῆρες θανάτοιο "death-spirits" / "spirits of death" and κῆρα μέλαιναν "black death-fate" (15.275), with μέλας "black" |
| ἀμφενέμοντο (2.835, 2.853) | "inhabited round about" | "inhabited the country round" | "dwelt around", "lived near" (ναίω "dwell"), "held" (ἔχω); ἀμφί + νέμομαι, kept apart from the other two verbs |
| αἴθων (ἵπποι αἴθωνες μεγάλοι, 2.838–839) | "fire-bright, big" | "fire-bright and big" | "tawny", "ruddy", "blazing" (each decides the colour); follows the Odyssey’s αἴθωνες, μεγάλοι of oxen (odyssey-091) and αἴθων σίδηρος "fire-bright iron" |
| ἀγάρροος (Ἑλλήσποντος ἀγάρροος, 2.845) | "strong-flowing" | "strong-flowing" | "swift-flowing", "strongly flowing", "mighty-flowing" (reserved for ἴφθιμος); ἀγα- the intensifier of ἀγακλυτός, ῥόος "stream" |
| ἀγκυλότοξος (Παίονας ἀγκυλοτόξους, 2.848) | "of the curved bows" | "with their curved bows" | "crooked-bowed", "bent-bow", "armed with bent bows"; follows the Odyssey’s ἀγκύλα τόξα "the curved bows" |
| εὐρὺ ῥέοντος (Ἀξιοῦ, 2.849) | "flowing wide" | "wide-flowing" | "broad-flowing", "flowing far"; εὐρύς is "wide" (1.478), and the adverb εὐρύ keeps it |
| κάλλιστον ὕδωρ ἐπικίδναται αἶαν (2.850) | "fairest water spreads over the earth" | "fairest water spreads over the land" | "most beautiful", "loveliest"; ἐπικίδναμαι "spread over", αἶα "land / earth" (the Odyssey’s αἶα "land") |
| λάσιον κῆρ (Πυλαιμένεος, 2.851) | "the shaggy heart" | "the shaggy heart" | "stout heart", "bold spirit", "hairy heart"; λάσιος "shaggy" (1.189), κῆρ "heart", and the phrase names the man by his heart |
| ἡμιόνων … ἀγροτεράων (2.852) | "wild mules" | "wild mules" | "mountain mules", "mules of the field" (that is ἀγρός); ἀγρότερος "wild", ἡμίονος "mule" |
| κλυτὰ δώματ’ ἔναιον (2.854) | "dwelt in famous halls" | "dwelt in famous halls" | "renowned dwellings", "fine houses"; follows the Odyssey’s κλυτὰ δώματα "famous halls" |
| γενέθλη (ἀργύρου γενέθλη, 2.857) | "the origin of silver" | "where silver has its origin" | "birthplace", "source", "stock" (the Odyssey’s "stock / race" is for a family); γίγνομαι "be born", γενέθλη "birth, origin" |
| οἰωνιστής (2.858) | "bird-diviner" | "reader of birds" | "augur", "seer" (μάντις); built on οἰωνός and kept with οἰωνοπόλων "of bird-diviners" / "those who read the birds" (1.69) |
| ἐρύσατο … κῆρα μέλαιναν (2.859) | "draw off the black death-fate" | "save himself from the black spirit of death" | "rescued" (the Odyssey’s `l` for ἐρύσατο, odyssey-068, which would make the death-fate the thing rescued), "ward off" (kept for ἀμύνω, ἐπαρκέω), "escape"; a departure from the Odyssey’s verb, with the reason; κῆρα μέλαιναν keeps "the black death-fate" / "the black spirit of death" (15.275) |
| ἐδάμη (2.860, 2.874) | "was subdued" | "was overcome" | "was killed", "was slain", "was tamed"; follows the Odyssey’s ἐδάμασσεν "subdued" / "overcame" (11.399) |
| ποδώκεος Αἰακίδαο (2.860, 2.874) | "the fleet-footed descendant of Aeacus" | "the fleet-footed descendant of Aeacus" | "swift-footed" (the Odyssey’s rendering of the same words, odyssey-055 and -056, but "swift-footed" is reserved here for ποδάρκης, 1.121, and the Iliad ships "fleet-footed" for ποδώκης at 2.764); a departure from the Odyssey, with the reason; "descendant of Aeacus" is the Odyssey’s |
| κεραΐζω (κεράϊζε, 2.861) | "was ravaging" | "was ravaging" | "was cutting down", "was slaying", "was plundering"; κεραΐζω "ravage, lay waste", and no published unit has it |
| θεοειδής (Ἀσκάνιος θεοειδής, 2.862) | "godlike in form" | "godlike in form" | "godlike" (ἀντίθεος), "like a god" (θεοείκελος "god-resembling"), "of divine form"; θεός + εἶδος "form" |
| ὑσμῖνι μάχεσθαι (2.863) | "in battle to fight" | "to fight in the battle" | "in the press", "in the fray"; ὑσμίνη "battle" (2.477) |
| βαρβαροφώνων (Καρῶν, 2.867) | "of barbarian speech" | "who spoke a foreign tongue" | "of barbarous speech" (misleads in English), "foreign-speaking", "barbarian-voiced"; βάρβαρος + φωνή "voice" |
| ἀκριτόφυλλον (ὄρος, 2.868) | "of unsorted leaves" | "thick with leaves" | "of countless leaves", "leafy" (loses ἄκριτος), "dense-leaved"; ἄκριτος keeps "unsorted" (2.246) and the note says the sense is taken from the formation |
| ῥοάς · κάρηνα (Μαιάνδρου ῥοάς, Μυκάλης αἰπεινὰ κάρηνα, 2.869) | "the streams" · "the steep peaks" | "the streams" · "the steep peaks" | "waters", "springs" · "heads", "summits"; κάρηνα of mountains is "peaks" (2.735), αἰπεινά "steep" |
| ἀγλαὰ τέκνα (Νομίονος, 2.871) | "the splendid children" | "Nomion’s splendid children" | "glorious sons", "bright children"; τέκνον is "child" and ἀγλαός "splendid" |
| χρυσὸν ἔχων (2.872) | "with gold on him" | "with gold on him" | "wearing gold", "carrying gold", "laden with gold" (each adds to the Greek); ἔχων "having" |
| ἠΰτε κούρη · νήπιος (2.872–873) | "like a girl" · "foolish" | "like a girl" · "foolish as he was" | "like a maiden", "childishly"; κούρη is "girl" (1.392), νήπιος "foolish" (2.38) |
| ἐπήρκεσε λυγρὸν ὄλεθρον (2.873) | "ward off grievous destruction" | "ward off grievous destruction" | "avert", "keep off", "prevent", "baneful"; follows the Odyssey’s ἐπαρκέω "ward off" (17.568), λυγρός "grievous" and ὄλεθρος "destruction" (3.194) |
| κομίζω (χρυσὸν … ἐκόμισσε, 2.875) | "carried off" | "carried off" | "took care of" (the shipped sense at 1.594), "brought home", "took", "gathered"; κομίζω is "carry" and, of spoil, "carry off" |
| δινήεις (Ξάνθου … δινήεντος, 2.877) | "eddying" | "eddying" | "swirling", "whirling", "deep-eddying" (ἀργυροδίνης is "silver-eddying"); δίνη "eddy" |
|---|---|---|---|
| Δύσπαρι (vocative, 3.39) | "Ill-Paris" | "Wretched Paris" (+ note: δυσ- "ill" put before Πάρις as an insult; same man as Alexander) | "Evil Paris", "Paris the accursed" ("accursed" is turned down for οὐλομένην), "Damned Paris", "Paris of ill omen"; Ἀλέξανδρος stays "Alexander" and the note says it is the same man |
| προμάχοισι (ἐν προμάχοισι, 3.31) · προμαχίζω (3.16) · πρόμον (3.44) | "front-fighters" · "was fighting in front" · "a foremost fighter" | "among the foremost fighters" · "was fighting in the front rank" · "a foremost fighter" | "champions" (kept for ἀριστῆες / ἀριστῆα "best man"), "vanguard", "leaders"; πρό "in front" + μάχομαι stays visible |
| τὸν δ’ ὡς οὖν ἐνόησεν + name (3.21, 3.30; whole-line opening, subject changes) | "Him then as he noticed, [Name]," | "And when [Name] noticed him" / "saw him" | "caught sight of", "spotted", "perceived"; ἐνόησεν "noticed" here (the Odyssey’s ἐνόησε "thought of / devised" is for ἄλλο ἐνόησε, an object of thought) |
| ὣς ἐχάρη Μενέλαος … ὀφθαλμοῖσιν ἰδών (3.27–28) · ἐχάρη | "so rejoiced Menelaus … with eyes having seen" | "So Menelaus rejoiced when he saw … with his eyes" | "was glad", "delighted"; χαίρω aorist is "rejoiced" here and at 3.76 (ἐχάρη μέγα) |
| φάτο γὰρ τίσεσθαι ἀλείτην (3.28) | "for he thought to take vengeance on the offender" | "for he thought he would take vengeance on the offender" | "said", "swore" (φάτο after γάρ gives his thought, not a spoken word), "punish" (the Odyssey table keeps "take vengeance on" for τίνυμαι, 12.378), "avenge himself on the sinner"; ἀλείτης "offender"; τίνυμαι kept apart from τίω "honour" |
| κατεπλήγη φίλον ἦτορ (3.31) | "he was struck in his dear heart" | "he was stricken at the heart" | "his heart sank", "his heart was shaken", "he was struck with terror" (each decides the force); φίλον ἦτορ "dear heart" in `l` and dropped in `i`, as in the table |
| κῆρ’ ἀλεείνων (3.32) | "death-fate avoiding" | "shunning death" | "the dark spirits"; κήρ "death-fate" (distinct from κῆρ "heart") as in the table’s κῆρα μέλαιναν |
| ἠέριαι (3.7; meaning disputed) | "early" | "early in the day" (+ note: "in the early morning" or "misty", disputed) | "in the morning mist", "at dawn" in `l` (each decides the dispute) |
| ὑπόψιον ἄλλων (3.42) | "one looked at askance by others" | "a man looked at askance by others" (+ note: ὑπό + ὄψ "sight") | "suspected", "despised", "a laughing-stock"; κέρδιον keeps the table’s "better" |
| κατ’ αἶσαν … ὑπὲρ αἶσαν (3.59) | "in due measure … beyond due measure" | "in due measure … beyond it" | "justly", "deservedly", "as I deserved"; follows the table’s αἴσιμα "in due measure" (αἶσα "portion") |
| δειδήμονες (3.56) | "timid" | "timid" | "cowardly", "fearful" (keep for δειλός and φοβέομαι), "faint-hearted"; the note says the formation is not clear |
| λάϊνον ἕσσο χιτῶνα (3.57) | "a stone tunic you would have put on" | "you would have put on a tunic of stone" (+ note: figure for stoning) | "you would have been stoned" (drops the image), "a coat of stones", "a shroud of stone" |
| ἀτάρβητος (νόος, 3.63) | "fearless" | "fearless" | "dauntless", "undaunted", "unshaken" (each is another word); ἀ- + ταρβέω |
| μή μοι δῶρ’ ἐρατὰ πρόφερε (3.64) | "do not bring forward to me the lovely gifts" | "do not bring up against me the lovely gifts" | "do not throw in my face", "do not taunt me with", "do not reproach me with" (each decides the sense of προφέρω); ἐρατός "lovely" |
| ἀπόβλητα … δῶρα (3.65) | "not to be thrown away" | "are not to be thrown away" | "not to be despised", "not to be scorned", "not to be refused"; ἀποβάλλω "throw away" |
| νεέσθων · ναίοιτε (3.74) | "let them go back" · "may you dwell" | "let them go back" · "may you live" | "return", "they must go home"; the optative of wish is kept as "may you" |
| Ἀχαιΐδα καλλιγύναικα (3.75) | "Achaea of the fair women" | "Achaea of the fair women" | "Achaean land" (loses the noun), "Achaea of the beautiful women"; follows Ἑλλάδα καλλιγύναικα "Hellas of the fair women" (2.683) |
| ὣς ἔφαθ’, Ἕκτωρ δ’ αὖτ’ ἐχάρη μέγα μῦθον ἀκούσας (3.76, speech-closing line with reaction) | "So he spoke, and Hector in turn rejoiced greatly, the speech having heard," | "So he spoke, and Hector rejoiced greatly to hear the speech," | "was very glad at the word", "was pleased"; ὣς ἔφαθ’ keeps "So he spoke" |
| ἀνέεργε φάλαγγας (3.77) | "held back the battle-lines" | "held back the Trojan battle-lines" | "pushed back", "restrained the ranks", "stopped the phalanxes" (φάλαγξ "battle-line"; "phalanx" is a later word) |
| τοὶ δ’ ἱδρύνθησαν ἅπαντες (3.78) | "and they were seated, all" | "and they all sat down" | "were settled", "took their seats at once"; the passive is kept in `l` |
| ἐπετοξάζοντο … τιτυσκόμενοι (3.79–80) | "were aiming-with-bows … taking aim" | "kept shooting at him … aiming" | "shot at", "fired at him"; the imperfect "kept" is the force of the tense |
| μακρὸν ἄϋσεν (3.81) | "shouted loudly" | "cried out loudly" | "gave a long cry", "bellowed"; μακρόν is an adverb "long", and ἀΰω "shout" |
| ἴσχεσθ’ Ἀργεῖοι, μὴ βάλλετε κοῦροι Ἀχαιῶν (3.82) | "Hold back, Argives, do not strike, youths of the Achaeans" | "Hold back, Argives; do not strike, young men of the Achaeans" | "Stop", "cease fire", "hold your arrows"; κοῦροι "young men / youths" (kept apart from υἷες "sons") |
| στεῦται γάρ τι ἔπος ἐρέειν (3.83) | "for … claims some word to say" | "for … claims that he will say something" | "swears he has something to say" (στεῦται is "claims", as at 2.597 and 17.525) |
| Πυγμαῖοι (3.6) | "Pygmy men" | "Pygmy men" | "dwarfs", "fist-men", "little people" |
| κλαγγῇ τ’ ἐνοπῇ τ’ (3.2) · ἐνοπή | "with clamour and shouting" | "with clamour and shouting" | "voice" (the table’s ἐνοπή at 10.147 is the Odyssey’s "voice"; here the word is a cry of many men, paired with κλαγγή "clamour"), "din", "cry"; κλαγγή keeps "clamour" |
| ὣς ἔφαθ’, οἳ δ’ ἔσχοντο μάχης ἄνεῴ τ’ ἐγένοντο ἐσσυμένως (3.84–85) | "So he spoke, and they held themselves back from the fighting and became speechless, hurriedly;" | "So he spoke, and in haste they held back from the fighting and fell speechless;" | "fell silent" (kept for ἀκὴν ἐγένοντο σιωπῇ, the Odyssey table), "stopped fighting" (drops ἔσχοντο μάχης "held back from"); ἄνεῳ ἐγένοντο keeps "speechless" / "fell speechless" (iliad-010, Odyssey table 7.144), ἐσσυμένως "hurriedly" / "in haste" (odyssey-039) |
| Ἕκτωρ δὲ μετ’ ἀμφοτέροισιν ἔειπε (3.85, speech introduction) | "and Hector among both spoke:" | "and Hector spoke among them both:" | "to both armies" (supplies a noun), "addressed" (reserved for προσέφη), "answered" |
| τοῖσι δὲ καὶ μετέειπε βοὴν ἀγαθὸς Μενέλαος (3.96, whole-line speech introduction) | "And among them spoke also Menelaus, good at the war-cry:" | "And Menelaus, good at the war-cry, also spoke among them:" | "Then Menelaus … rose to speak", "addressed them" (reserved for προσέφη), "good at the battle-cry"; βοὴν ἀγαθός keeps "good at the war-cry" (Iliad 2.563, 2.567) |
| ὣς ἔφαθ’, οἳ δ’ ἄρα πάντες ἀκὴν ἐγένοντο σιωπῇ (3.95) | "So he spoke, and they then all became still in silence;" | "So he spoke, and they all fell hushed and silent;" | "were silent" (the Odyssey’s ἀκὴν ἔσαν), "held their peace"; the phrase is the Odyssey table’s (7.154), unchanged, with ὣς ἔφαθ’ "So he spoke" |
| ὣς ἔφαθ’, οἳ δ’ ἐχάρησαν Ἀχαιοί τε Τρῶές τε ἐλπόμενοι παύσασθαι ὀϊζυροῦ πολέμοιο (3.111–112) | "So he spoke, and they rejoiced, Achaeans and Trojans both, hoping to cease from sorrowful war." | "So he spoke, and Achaeans and Trojans both were glad, hoping to cease from sorrowful war." | "hoping to be done with", "weary war", "grievous war", "wretched war"; ὀϊζυρός keeps "sorrowful" (iliad-005, odyssey-065) and παύω "cease" |
| κέκλυτέ μευ (3.86) · κέκλυτε … καὶ ἐμεῖο (3.97) | "Hear me" · "Hear now me, too" | "Hear me" · "Hear me, too, now" | "Listen to me"; follows κλῦθί μευ "Hear me" and the Odyssey’s κέκλυτε … μευ "Hear me now" |
| ἄρν’, ἕτερον λευκόν, ἑτέρην δὲ μέλαιναν (3.103; ἄρν’ the dual, 3.119 ἄρν’ the singular) | "two lambs, one white, and the other black" · "a lamb" | "two lambs, one white and the other black" · "a lamb" | "a ram … a ewe" (the Greek names no sex; the note says the endings show it), "sheep"; ἀρήν "lamb" as in πολύαρνι "rich in lambs" (2.106) |
| Γῇ τε καὶ Ἠελίῳ (3.104) | "for Earth and Sun" | "for Earth and the Sun" | "Gaia", "Helios", "the Sun-god"; follows the Odyssey’s Ἠέλιος "the Sun" (10.138) |
| Πριάμοιο βίην (3.105) | "the might of Priam" | "the might of Priam" | "Priam himself", "mighty Priam" (each erases the periphrasis); follows βίη Ἡρακληείη "the might of Heracles" (2.658) and the Odyssey table’s ἱερὴ ἲς Τηλεμάχοιο, a periphrasis kept |
| ὑπερφίαλοι καὶ ἄπιστοι (3.106) | "overweening and faithless" | "overweening and faithless" | "unbelieving" (the Odyssey’s ἄπιστος of a heart, odyssey-067 and -069, a different sense: here the sons are not to be trusted), "untrustworthy", "arrogant", "insolent"; ὑπερφίαλος keeps the Odyssey’s "overweening" (odyssey-029); a departure from the Odyssey for ἄπιστος, with the reason |
| ὑπερβασίῃ … δηλήσηται (3.107) | "through overstepping … harm" | "through overstepping do harm to" | "transgression", "violate", "break" (each decides what harm to an oath is); δηλέομαι keeps the Odyssey’s "harm" (11.401), ὑπερβασία is ὑπερβαίνω "step over" |
| ἠερέθονται (of wits, 3.108) | "are fluttering" | "are fluttering" | "hang waving" (the rendering of the same verb for the aegis’s tassels at 2.448, which does not fit the mind), "waver", "are unsteady", "flit"; a departure from the Iliad’s earlier "hang waving", with the reason: the verb is "hang waving, flutter" and the mind cannot hang |
| ἅμα πρόσσω καὶ ὀπίσσω λεύσσει (3.109–110) | "at once forward and backward he looks" | "he looks at what lies ahead and what lies behind" | follows the Iliad table’s ἅμα πρόσσω καὶ ὀπίσσω (1.343) and the Odyssey’s ὅρα πρόσσω καὶ ὀπίσσω |
| ὀϊζυρὸς πόλεμος (3.112) | "sorrowful war" | "sorrowful war" | see above |
| ἔρυξαν ἐπὶ στίχας (3.113) | "held back along the ranks" | "held back along the ranks" | "reined in" and "checked" (decide how), "in line"; ἐρύκω keeps the Odyssey’s "hold back" (odyssey-001, odyssey-019) |
| ὀλίγη δ’ ἦν ἀμφὶς ἄρουρα (3.115) | "small was the plough-land between" | "little plough-land lay between" | "a narrow field", "a strip of ground"; ἄρουρα keeps the Odyssey table’s "plough-land" (ζείδωρος ἄρουρα) |
| γαλόῳ … δάμαρτι (3.122) | "her husband’s sister … wife" | "her husband’s sister … wife" | "sister-in-law" (also covers the wife of a brother-in-law, which γάλως does not), "bride", "spouse"; γάλως is the husband’s sister, said to Helen of Alexander’s sister Laodice |
| εἶδος ἀρίστην (3.124) | "in form the best" | "the best in form" | "most beautiful", "fairest" (drops εἶδος); keeps "best in form" of 3.39 (εἶδος ἄριστε, iliad-016) and the Odyssey’s εἶδος "form" |
| ἱστόν (3.125; of the web on the loom) | "web" | "web" | "loom" (the frame, not the cloth), "tapestry", "mast" (kept for ἱστός in ships, 1.434); ἱστόν ὕφαινε "weave a web" |
| δίπλακα πορφυρέην (3.126) | "a double cloak, purple" | "a double cloak of purple" | "folded purple cloth", "double mantle"; follows the Odyssey table’s δίπλαξ "double cloak" and πορφυρέη "purple" |
| ἐνέπασσεν ἀέθλους (3.126) | "was working into it … struggles" | "working into it … struggles" | "contests" (the Odyssey table’s ἄεθλος, which is for games; here it is the fighting), "trials" (kept for the toils of Odysseus), "labours"; ἐμπάσσω "work in, embroider"; a departure from the Odyssey table’s "contest(s)", with the reason |
| Τρώων θ’ ἱπποδάμων καὶ Ἀχαιῶν χαλκοχιτώνων (3.127 = 3.131, whole line, repeated) | "of the horse-taming Trojans and the bronze-shirted Achaeans" | "of the Trojans, tamers of horses, and the bronze-shirted Achaeans" | "bronze-coated" (iliad-004 and iliad-007 ship "bronze-shirted"), "bronze-clad"; ἱππόδαμος keeps the Odyssey’s "horse-taming" / "tamer of horses" (Νέστωρ ἱππόδαμος), the plural placed after the noun in `i` |
| ὑπ’ Ἄρηος παλαμάων (3.128) | "at the hands of Ares" | "at the hands of Ares" | "at the hands of war" (loses the figure), "by the hand of Ares"; Ares stands for war, and the figure is kept in both layers |
| ἀγχοῦ δ’ ἱσταμένη προσέφη πόδας ὠκέα Ἶρις (3.129) | published (iliad-015, 2.790) | published | the unit takes the shipped English verbatim |
| δεῦρ’ ἴθι (3.130) | "Come here" | "Come here" | "Hither", "Come along", "Come now"; ἴθι is the imperative of εἶμι "go" |
| νύμφα φίλη (3.130) | "dear bride" | "dear lady" | "dear girl", "dear child", "my dear"; the Odyssey table’s νύμφα φίλη (4.743: "Dear bride" / "Dear lady"), unchanged |
| θέσκελα ἔργα (3.130) | "marvellous deeds" | "marvellous deeds" (+ note: meaning of θέσκελος not known) | "wondrous", "god-wrought"; the Odyssey table’s row, unchanged |
| πολύδακρυν Ἄρηα (3.132) · πόλεμον πολύδακρυν (3.165) | "tearful Ares" · "tearful war" | "tearful battle" · "tearful war" | "much-weeping", "of many tears" (keep the roots visible in `l` only if `l` is a compound), "lamentable"; πολύ- "much" + δάκρυ "tear", the adjective actively "full of tears" |
| Ἄρηα (3.132, of battle) | "Ares" | "battle" | "war" (kept for πόλεμος in the same sentence, 3.133), "fighting"; Ares stands for battle, as in the table’s μῶλον Ἄρηος "the toil of battle" |
| ὀλοοῖο … πολέμοιο (3.133) | "baneful war" | "baneful war" | "deadly", "ruinous" (reserved for οὐλόμενος), "destructive" (ἀΐδηλος); ὀλοός keeps "baleful / baneful"; the table’s ὀλοόφρων "baleful-minded", ὀλοιῇσι φρεσί "baleful" |
| λιλαιόμενοι (3.133) | "longing for" | "eager for" | "yearning" (the Odyssey’s l in odyssey-001), "desiring", "lusting for"; λιλαίομαι "long for" with the genitive |
| ἕαται (3.134) | "sit" | "sit" | "are seated", "are sitting"; the perfect of ἧμαι |
| πέπηγεν (ἔγχεα, 3.135) | "are fixed" | "planted" | "stuck", "set upright"; πήγνυμι "fix"; the ground is understood and `i` says "planted" |
| ἀρηΐφιλος Μενέλαος (3.90, 3.136) | "Ares-loved Menelaus" | "Menelaus, dear to Ares" | the Iliad’s row (2.778), unchanged |
| ἐγχείῃσι (3.137) | "spears" | "spears" | "lances"; ἔγχος and ἐγχείη both "spear" |
| κεκλήσῃ ἄκοιτις (3.138) | "you will be called … wife" | "you will be called … wife" | "spouse", "bedfellow" (an etymology), "consort"; ἄκοιτις is a plain word for wife |
| ἵμερος (3.139) | "longing" | "longing" | "desire" (reserved for ἐρατεινός / ἔρως), "yearning", "sweet pain"; ἵμερον … ἔμβαλε "put longing into" |
| ἀνδρός τε προτέρου καὶ ἄστεος ἠδὲ τοκήων (3.140) · πρότερόν τε πόσιν (3.163) | "her former husband, and city, and parents" · "your former husband" | "her former husband, her city and her parents" · "your former husband" | "first husband", "earlier husband", "husband of before"; πρότερος "former", the same word in both places |
| ἀργεννῇσι ὀθόνῃσιν (3.141) | "white linen" | "white linen" | "bright linen", "shining veil", "silvery cloth"; the Odyssey ships "white" for ἀργεννός |
| τέρεν κατὰ δάκρυ χέουσα (3.142) | "down a tender tear shedding" | "shedding tender tears" | "weeping" (drops χέω), "soft tears"; the table’s κατὰ δάκρυ χέουσα (1.413) with τέρεν "tender" |
| ἀμφίπολοι δύ’ (3.143, repeated Odyssey line) | "two handmaids" | "two handmaids" | "attendants" (the Odyssey table’s ἀμφίπολοι); the unit reuses the shipped English of the line (odyssey-004), which says "handmaids", and the shipped line wins over the table here |
| Σκαιαὶ πύλαι (3.145, 3.149) | "the Scaean Gates" | "the Scaean Gates" | "the left gates", "the Western Gates", "the Skaian Gates"; a name is kept as a name, the note gives the guess |
| δημογέροντες (3.149) | "elders of the people" | "elders of the people" | "old men of the town", "councillors", "elders of the land"; δῆμος "people" here (not the Odyssey’s "land"), γέρων "elder" |
| πεπνυμένω ἄμφω (3.148) | "the two prudent" | "both prudent men" | "wise", "both wise"; πεπνυμένος keeps the Odyssey’s "prudent" |
| ὄζον Ἄρηος (Ἱκετάονα, 3.147) | "scion of Ares" | "scion of Ares" | as at 2.540 (Ἐλεφήνωρ) and 2.704 |
| ἀγορηταὶ ἐσθλοί (3.150–151) | "speakers good" | "good speakers" | "orators", "fine speakers"; follows ἀγορητής "speaker" (1.248) and ἐσθλός "good" |
| τεττίγεσσιν (3.151) | "cicadas" | "cicadas" | "crickets", "grasshoppers", "tree-crickets" |
| ὄπα λειριόεσσαν (3.152) | "lily-like voice" | "lily-like voice" (+ note: sense not certain) | "delicate", "clear", "pure", "tender" (each decides the likeness), "lilied"; λείριον "lily" |
| ἧντο (3.153) | "were sitting" | "sat" | "sat" in `l`, "were seated"; the imperfect of ἧμαι, with ἥατο (3.149) |
| ἦκα … ἔπεα πτερόεντ’ ἀγόρευον (3.155) | "softly … winged words spoke" | "spoke winged words softly" | "gently" (the Odyssey’s ἦκα of slow movement and of a bent head), "in low tones", "said"; "declared" (ἀγορεύω in public, which this is not); ἔπεα πτερόεντα keeps "winged words" |
| οὐ νέμεσις (3.156) | "No resentment is it" | "It is no cause for resentment" | "No blame", "no wonder", "no indignation" (turned down at the Odyssey’s 20.330); νέμεσις keeps "resentment" as in νεμεσσάω |
| αἰνῶς … ἔοικεν (3.158) | "dreadfully … is like" | "is dreadfully like" | "terribly", "awfully", "wonderfully"; αἰνός is "dread" |
| πῆμα (3.160) | "woe" | "woe" | "bane", "plague", "ruin"; follows the Odyssey table’s πῆμα κακόν "evil woe" |
| ἐκαλέσσατο φωνῇ (3.161) | "called … to him with his voice" | "called … to him aloud" | "summoned", "invited"; καλέω "call", the middle "to himself" |
| ἵζευ ἐμεῖο (3.162) | "sit down by me" | "sit down by me" | "sit before me" (decides πάροιθε with ἐμεῖο), "sit near"; the note gives both readings |
| πηούς (3.163) | "kinsmen" | "kinsmen" | "in-laws", "relatives by marriage" (the note gives the sense) |
| αἰτίη · αἴτιοι (3.164) | "to blame" | "to blame" | "cause", "guilty", "responsible"; follows ἐπαίτιος "to blame" (1.335) |
| ἐφώρμησαν (3.165) | "stirred up against" | "stirred up against" | "launched upon", "sent against", "roused"; ἐφορμάω "set on" |
| ἐξονομήνῃς (3.166) | "you may name" | "tell me the name of" | "call by name", "point out", "declare" (reserved for ἀγορεύω in public); ὀνομαίνω "name" |
| πελώριον (ἄνδρα, 3.166) | "huge" | "huge" | "monstrous" (the Odyssey’s l for πελώριος of the Cyclops and of waves, a word of dread; here it is a word of wonder), "gigantic", "enormous"; a departure from the Odyssey’s "monstrous", with the reason |
| ἠΰς τε μέγας τε (3.167) | "both good and great" | "both good and great" | the shipped iliad-013 row (2.653), unchanged |
| καλὸν … γεραρόν (3.169–170, neuter, of a man) | "so fine … so stately" | "so fine … so stately" | "handsome" (reserved for the table’s other adjectives), "noble", "beautiful" (reserved for κάλλος); καλός keeps the table’s "fine"; γεραρός "stately, venerable", no published unit has it |
| βασιλῆϊ ἀνδρί (3.170) | "to a man, a king" | "a king" | "a kingly man", "a man of royal rank", "a royal man"; the dative of βασιλεύς with ἀνήρ in apposition |
| τὸν δ’ Ἑλένη μύθοισιν ἀμείβετο δῖα γυναικῶν (3.171, whole-line reply-formula) | "Him then Helen with words answered, heavenly-one of women:" | "Then Helen, heavenly among women, answered him with words:" | "replied", "addressed" (reserved for προσέφη); μύθοισιν kept as "with words"; follows the table's δῖα γυναικῶν "heavenly-one of women" / "heavenly among women" and the Iliad's ἠμείβετο rows |
| τὸν δ’ Ἑλένη τανύπεπλος ἀμείβετο δῖα γυναικῶν (3.228) | "Him then Helen, long-robed, answered, heavenly-one of women:" | "Then long-robed Helen, heavenly among women, answered him:" | "trailing-robed", "long-gowned"; τανύπεπλος "long-robed" as fixed at 4.305 |
| τὸν δ’ ἠμείβετ’ ἔπειθ’ Ἑλένη Διὸς ἐκγεγαυῖα (3.199) | "Him then answered thereupon Helen, sprung of Zeus:" | "Then Helen, the daughter sprung from Zeus, answered him:" | "born of Zeus", "child of Zeus", "Zeus-born"; Odyssey table's Ἀργείη Ἑλένη, Διὸς ἐκγεγαυῖα "sprung of Zeus" / "the daughter sprung from Zeus", with the Argive dropped because the Greek has no such word here |
| τὴν δ’ αὖτ’ Ἀντήνωρ πεπνυμένος ἀντίον ηὔδα (3.203, whole-line reply-formula) | "To her in turn prudent Antenor spoke, face to face:" | "Then prudent Antenor spoke to her in turn, face to face:" | "answered" (reserved for ἀμείβετο); follows the Odyssey's fourth reply-formula (Telemachus) unchanged |
| ὣς φάτο, τὸν δ’ ὁ γέρων ἠγάσσατο φώνησέν τε (3.181) | "So she spoke, and him the old man was in wonder at, and spoke:" · (i) "So she spoke, and the old man was amazed at him and spoke:" | as `l` | "admired", "marvelled" (decide how the wonder felt); ἀγάομαι "in wonder" / "were amazed at" as in the table (10.249), kept the same at 3.224 |
| δεύτερον αὖτ’ Ὀδυσῆα ἰδὼν ἐρέειν’ ὁ γεραιός (3.191) · τὸ τρίτον αὖτ’ Αἴαντα ἰδὼν ἐρέειν’ ὃ γεραιός (3.225) | "Second, in turn, seeing Odysseus, asked the old man:" · "Third, in turn, seeing Ajax, asked the old man:" | "Next, catching sight of Odysseus, the old man asked:" · "Third, catching sight of Ajax, the old man asked:" | "questioned" (ἐρέεινε is "asked"), "looking upon"; ὁ γεραιός keeps "the old man" (table: ὁ γέρων / ὁ γεραιός) |
| αἰδοῖός τέ μοί ἐσσι … δεινός τε (3.172) | "Revered to me you are, dear father-in-law, and dread;" | "To me you are revered, dear father-in-law, and dread;" | "awesome", "formidable" (the table's avoided words for δεινός); αἰδοῖος "revered" and δεινός "dread" both from the Odyssey table; ἑκυρός "father-in-law" (the husband's father) |
| παῖδά τε τηλυγέτην (3.175) | "my child, late-born" | "my late-born child" | "only", "cherished", "tender" (each decides an unknown); follows the Odyssey's τηλύγετος "late-born" (14.10), with the note that the word's origin is not known |
| γνωτούς (3.174) | "kinsfolk" | "kinsfolk" | "kinsmen" (shipped for πηοί at 3.163), "brothers", "family"; γνωτός is a blood relation |
| ὁμηλικίην ἐρατεινήν (3.175) | "the company of my own age, lovely" | "the lovely company of my own age" | "age-mates", "playmates", "girlhood friends"; ἐρατεινός "lovely" as in the Odyssey table |
| τὸ καὶ κλαίουσα τέτηκα (3.176) | "on that account, too, weeping, I have melted away" | "and that is why I waste away in tears" | "pine away", "dissolve"; τήκω "melt", the perfect intransitive |
| δαὴρ αὖτ’ ἐμὸς ἔσκε κυνώπιδος (3.180) | "husband’s-brother also he was, my own, of a dog-faced woman" | "and he was my husband’s brother, too, shameless creature that I am" | "brother-in-law" (also covers a sister's husband), "bitch"; κυνῶπις "dog-faced" in `l` and "shameless" in `i`, as in the Odyssey table (4.145); the vocative κυνῶπα (1.159) takes "you dog-face" only because ἀναιδές stood beside it |
| ὦ μάκαρ Ἀτρεΐδη μοιρηγενὲς ὀλβιόδαιμον (3.182) | "O blessed Atreus’-son, fate-born, prosperous in fortune," | "O blessed son of Atreus, born to your fate, prosperous in fortune," (+ note: μοιρηγενής, sense not known) | "fortunate", "happy", "lucky" (μάκαρ keeps "blessed", ὄλβιος "prosperous" per the Odyssey table); "child of destiny", "blessed by fate" (each decides the unknown sense of μοιρηγενής) |
| δεδμήατο κοῦροι Ἀχαιῶν (3.183) | "were subdued, the young men of the Achaeans" | "young men of the Achaeans were … made subject to you" | "were tamed", "fell under your sway", "followed you" (decide the sense); δάμνημι "subdue" (cf. "made subject" at Odyssey 56) |
| Φρυγίην … ἀμπελόεσσαν (3.184) | "Phrygia, vine-clad" | "vine-clad Phrygia" | "vine-rich", "vineyard-covered"; follows the shipped ἀμπελόεντα "vine-clad" (iliad-012) |
| Φρύγας ἀνέρας αἰολοπώλους (3.185) | "Phrygian men with gleaming colts" | "Phrygian men with their gleaming colts" (+ note: αἰόλος sense not known) | "swift-horsed", "with dappled horses", "of the flashing colts" (each decides the unknown sense of αἰόλος); πῶλος "colt" |
| Ἀμαζόνες ἀντιάνειραι (3.189) | "the Amazons, man-matching" | "the man-matching Amazons" (+ note: sense disputed) | "a match for men" (flat), "who fight like men", "man-fighting", "opposed to men" (each picks one reading) |
| ἐπίκουρος (3.188) | "ally" | "ally" | "helper", "auxiliary"; ἐπίκουρος is "ally" in the shipped parts (iliad-008, -015) |
| ἐλέχθην (3.188) | "was counted" | "was numbered" | "was called", "was reckoned"; the old sense "count" of λέγω |
| πουλυβοτείρῃ (3.195) | "much-nourishing" | "that feeds so many" | follows the shipped iliad-017 and odyssey-036 rendering |
| κτίλος ὥς (3.196) | "like a tame ram" | "like a tame ram" (+ note: sense of κτίλος not known) | "like a bell-wether", "like a gentle beast", "like a sheep" (each decides the unknown) |
| ἐπιπωλεῖται στίχας ἀνδρῶν (3.196) | "goes about the ranks of men" | "ranges along the ranks of men" | "patrols", "inspects", "marches along"; ἐπιπωλέομαι "go to and fro over" |
| ἀρνειῷ … πηγεσιμάλλῳ (3.197) | "a thick-fleeced ram" | "a thick-fleeced ram" | "heavy-fleeced", "woolly", "fat-fleeced"; πηγεσί- "firm, thick" with μαλλός "fleece" |
| ἀργεννάων (3.198) | "white" | "white" | "gleaming", "silver"; ἀργεννός is "white" |
| Λαερτιάδης πολύμητις Ὀδυσσεύς (3.200) | "Laertes’-son, many-wiled Odysseus" | "the son of Laertes, Odysseus of many wiles" | "resourceful", "many-devising" (reserved for πολυμήχανος); Λαερτιάδης "Laertes’-son" like Ἀτρεΐδης "Atreus’-son"; πολύμητις from the Odyssey table |
| Ἰθάκης κραναῆς περ ἐούσης (3.201) | "Ithaca, rugged though it is" | "Ithaca, rugged as it is" | "rocky", "craggy", "stony", "rough"; κραναός "rocky, rugged" read as "rugged" |
| δήμῳ (ἐν δήμῳ Ἰθάκης, 3.201) | "land" | "land" | "district", "community", "people"; the sense "country with its people" |
| μήδεα πυκνά (3.202, 3.208) | "solid counsels" | "solid counsels" | "thick counsels", "close counsels", "shrewd plans"; the Odyssey table's πυκινὰ μήδεα "solid counsels" (19.353), with πυκνά as the shorter form of the same word |
| ὦ γύναι (3.204) | "Woman" | "Woman" | "Lady" (reserved for πότνια / δέσποινα), "Madam"; the Odyssey table's γύναι "woman" for a non-wife, the note says it is courteous here |
| ἔπος νημερτές (3.204) | "word, unerring" | "a word … truly unerring" | "true", "infallible", "faithful"; νημερτής "unerring" as in the Odyssey table |
| ἀγγελίη (σεῦ ἕνεκ’ ἀγγελίης, 3.206) | "on an embassy" | "on an embassy" | "message", "errand", "news" (the house rendering, departed from here; the note says why); ἀγγελίη "news" in the Odyssey (odyssey-004, -005), "embassy" here because the word names the errand of envoys |
| ἐξείνισσα … φίλησα (3.207) | "I entertained as guests … befriended" | "I entertained them as my guests and treated them kindly" | "I received", "I lodged", "I loved"; ξεινίζω "entertain as a guest", as shipped at odyssey-093 and -117 |
| φυήν (3.208) | "stature" | "the stature" | "build", "growth", "nature"; shipped for φυή in odyssey-027 and -034 |
| ὑπείρεχεν εὐρέας ὤμους (3.210) | "rose above with his broad shoulders" | "rose above the other with his broad shoulders" | "was taller by", "stood over", "overtopped" (each is a fair rendering; "rose above" keeps the figure); ὑπερέχω "stand over" |
| γεραρώτερος (3.211) | "more stately" | "the more stately" | "more venerable", "nobler"; γεραρός "stately" as at 3.168 |
| ἐπιτροχάδην ἀγόρευε (3.213) | "spoke glibly" | "did speak glibly" | "fluently", "at a run", "rapidly"; ἐπιτροχάδην "glibly", as in the Odyssey table (18.26) |
| παῦρα … μάλα λιγέως (3.214) | "few things, but very clearly" | "a few things, but in a clear voice" | "shrilly", "loudly"; λιγέως "clearly" / "in a clear voice" as in the table |
| πολύμυθος (3.214) | "full of words" | "talkative" | "wordy", "garrulous"; follows odyssey-006 ("full of words", "talkative") |
| ἀφαμαρτοεπής (3.215) | "missing-the-mark in speech" | "one who missed his mark in speech" | "gabbling", "tongue-tied", "foolish in speech" (each decides the unknown ἀφ-); the compound of ἁμαρτάνω "miss" and ἔπος "word" |
| ὕστερος γένει (3.215) | "in birth the younger" | "the younger by birth" | "later-born", "junior"; follows iliad-014's "younger by birth" |
| ἀναΐξειεν … στάσκεν … ἴδεσκε … ἔχεσκεν (3.216–219; iterative past) | "whenever … sprang up, he would stand … look down … hold" | "whenever … sprang up, he would stand … look down … hold" | "used to", "always"; the -σκ- forms give "would" |
| ἀΐδρεϊ φωτί (3.219) | "a man who knew nothing" | "a man who knew nothing" | "ignorant" alone, "witless" (reserved for ἄφρων), "simple"; ἄϊδρις "without knowledge" |
| ζάκοτον (3.220) | "greatly resentful" | "full of resentment" | "sullen", "surly", "furious", "very angry" (χόλος is "anger", κότος "resentment"); ζα- "very" with κότος |
| ἄφρονα … αὔτως (3.220) | "senseless … simply" | "senseless … simply" | "foolish", "a fool" (reserved for νήπιος by the Odyssey table), "witless" (reserved for ἀνοήμων), "mindless"; ἄφρων "senseless" as in the Odyssey table (17.586) and odyssey-103 (the "foolish" of odyssey-028 and -100 is not followed; changed at review) |
| ὄπα … ἐκ στήθεος … ἔπεα νιφάδεσσιν ἐοικότα χειμερίῃσιν (3.221–222) | "the great voice from his chest … words like snowflakes, wintry" | "his great voice out from his chest, and words like wintry snowflakes" | "winter snow", "flakes of the storm"; νιφάς "snowflake", χειμέριος "wintry" |
| οὐκ ἂν … Ὀδυσῆΐ γ’ ἐρίσσειε βροτὸς ἄλλος (3.223) | "no other mortal would then rival Odysseus" | "no other mortal could rival Odysseus" | "compete with", "match"; ἐρίζω "rival" as shipped at odyssey-014 and -074 |
| ἀγασσάμεθ’ … εἶδος ἰδόντες (3.224) | "Not then so were we in wonder at Odysseus, having seen his form" | "we were not then so amazed at Odysseus when we saw his form" | "marvelled", "admired"; same verb and rendering as 3.181 (the table's ἀγάομαι) |
| ἔξοχος Ἀργείων κεφαλήν τε καὶ εὐρέας ὤμους (3.227) | "surpassing the Argives in head and broad shoulders" | "who stands out above the Argives in head and broad shoulders" | "taller than", "head and shoulders above"; ἔξοχος "standing out" |
| ἕρκος Ἀχαιῶν (3.229) | "the fence of the Achaeans" | "the bulwark of the Achaeans" | "wall", "rampart", "defence"; as shipped at iliad-003 (1.284) |
| ἀγοὶ ἠγερέθονται (3.231) | "the leaders … are gathered" | "the Cretan leaders are gathered around him" | "captains", "chiefs" (ὄρχαμος "chief"), "guides"; ἀγός "leader", from ἄγω |
| ξείνισσεν … ὁπότε Κρήτηθεν ἵκοιτο (3.232–233) | "entertained as a guest … whenever from Crete he came" | "often entertained him as a guest … whenever he came from Crete" | "received", "hosted"; ξεινίζω as at 3.207 |
| οὕς κεν ἐῢ γνοίην καί τ’ οὔνομα μυθησαίμην (3.235) | "whom I could well recognise and could tell the name of" | "whom I could recognise well and whose names I could tell" | "name by name", "speak the name"; οὔνομα "name" |
| δοιὼ … κοσμήτορε λαῶν (3.236) | "two … the two marshallers of the people" | "two … the two marshals of the people" | the Iliad table's κοσμήτορε λαῶν (1.16), unchanged |
| Κάστορά θ’ ἱππόδαμον καὶ πὺξ ἀγαθὸν Πολυδεύκεα (3.237, whole line, repeated) | "Castor, horse-taming, and Polydeuces, good with the fist," | "Castor, tamer of horses, and Polydeuces, good with his fists" | the packet's English from odyssey-053, unchanged |
| αὐτοκασιγνήτω (3.238) | "own brothers" | "my own brothers" | "full brothers", "brothers by the same blood"; shipped as "own brother" at iliad-014 and "own-sister" at odyssey-046 |
| τώ μοι μία γείνατο μήτηρ (3.238) | "the two whom one mother bore to me" | "whom one mother bore for me" | "my mother's sons", "born of the same mother"; γείνομαι "bear" |
| ἑσπέσθην … ἕποντο (3.239–240) | "they did not follow … they did follow" | "did not follow … followed" | "come with", "accompany"; ἕπομαι "follow" |
| νέεσσ’ ἔνι ποντοπόροισι (3.240) | "in sea-crossing ships" | "in their sea-crossing ships" | the Iliad table's ποντοπόρος "sea-crossing" (2.771) |
| μάχην καταδύμεναι ἀνδρῶν (3.241) | "to enter the fighting of men" | "enter the fighting of men" | "battle" (the table keeps μάχη "fighting", 2.823 and 3.84–85), "go down into", "join", "face"; καταδύω "go down into, enter" |
| αἴσχεα … ὀνείδεα (3.242) | "the shames and the many reproaches" | "the shames and the many reproaches" | "disgraces", "taunts", "insults" (the Iliad has "insults" at 1.291 where the speaker is hostile); αἴσχος "shame" as at odyssey-095, ὄνειδος "reproach" as at iliad-010 |
| φυσίζοος αἶα … φίλῃ ἐν πατρίδι γαίῃ (3.243–244) | "the life-giving earth … the dear land of their fathers" | "the life-giving earth … the dear land of their fathers" | "native soil", "home-earth"; φυσίζοος from the Odyssey table (11.301) |
| κήρυκες … φέρον ὅρκια πιστά (3.245) | "the faithful oaths of the gods" | "the faithful oaths of the gods" (+ note: the things that make the oath) | "oath-offerings", "sacrifices", "pledges" (each leaves the table's "faithful oaths"); ὅρκια πιστά as at 2.124, the note explains that the word here names the victims and the wine |
| οἶνον ἐΰφρονα καρπὸν ἀρούρης (3.246) | "wine, the heart-cheering fruit of the plough-land" | "heart-cheering wine, the fruit of the plough-land" | "kindly", "well-minded", "glad-making"; ἐΰφρων "well-minded" is "kindly" in the Odyssey (odyssey-081 ἐϋφρονέων); here active, "cheering" |
| ἀσκῷ ἐν αἰγείῳ (3.247) | "in a goatskin" | "in a goatskin" | "in a goat-hide bag"; as shipped at odyssey-027 |
| κρητῆρα φαεινόν (3.247) | "a mixing-bowl, shining" | "a shining mixing-bowl" | "bright", "gleaming"; κρητήρ keeps the Odyssey's "mixing-bowl" |
| χρύσεια κύπελλα (3.248) | "golden cups" | "golden cups" | "goblets", "beakers", "chalices"; κύπελλον "cup" as shipped at iliad-006 |
| ὄρσεο Λαομεδοντιάδη (3.250) | "Rise, son of Laomedon" | "Rise, son of Laomedon" | "Laomedon’s son", "Laomediades" (a transliteration); the patronymic as Ἀτρεΐδης "Atreus’-son" in `l`, "son of …" in `i` |
| Τρώων θ’ ἱπποδάμων καὶ Ἀχαιῶν χαλκοχιτώνων (3.251 = 3.127) | "of the horse-taming Trojans and the bronze-shirted Achaeans" | "of the Trojans, tamers of horses, and of the bronze-shirted Achaeans" | the packet's English from iliad-017, unchanged except that "of" is repeated before "the bronze-shirted" in `i` so that the sentence reads |
| ἵν’ ὅρκια πιστὰ τάμητε (3.252) | "that faithful oaths you may cut" | "so that you may swear faithful oaths" | "make", "ratify"; τάμνω "cut" in `l`, the table's ταμόντες |
| αὐτὰρ Ἀλέξανδρος καὶ ἀρηΐφιλος Μενέλαος μακρῇς ἐγχείῃσι μαχήσοντ’ ἀμφὶ γυναικί (3.253–254) | "but Alexander and Ares-loved Menelaus with long spears will fight about a woman" | "but Alexander and Menelaus, dear to Ares, will fight with their long spears for a woman" | "over a woman", "on account of"; the first line is 3.136 with the same English, the second differs in its Greek |
| τῷ δέ κε νικήσαντι γυνὴ καὶ κτήμαθ’ ἕποιτο (3.255) | "and with the one who wins, the woman and the possessions would go" | "and the woman and the possessions would follow whichever of them wins" | "to the victor the woman and the goods"; κτήματα "possessions" |
| οἳ δ’ ἄλλοι φιλότητα καὶ ὅρκια πιστὰ ταμόντες ναίοιμεν Τροίην ἐριβώλακα, τοὶ δὲ νέονται Ἄργος ἐς ἱππόβοτον καὶ Ἀχαιΐδα καλλιγύναικα (3.256–258) | "and we others, friendship and faithful oaths having cut, may we dwell in rich-soiled Troy, and they are going back to Argos horse-pasturing and Achaea of the fair women." | "and the rest of us, having made friendship and sworn faithful oaths, may we live in rich-soiled Troy, while they go back to horse-pasturing Argos and to Achaea of the fair women." | the iliad-016 unit (3.73–75) has different Greek (ναίοιτε, νεέσθων), so only its wording is reused, with "we" for "you" and "are going back" for "let them go back"; the table's ἐριβώλακα "rich-soiled", ἱππόβοτον "horse-pasturing", καλλιγύναικα "of the fair women" |
| ῥίγησεν δ’ ὃ γέρων (3.259) | "shuddered the old man" | "the old man shuddered" | "trembled", "was afraid"; ῥιγέω "shudder", as shipped at odyssey-023; the Greek gives no cause |
| ἵππους ζευγνύμεναι (3.260) | "yoke the horses" | "yoke the horses" | "harness"; ζεύγνυμι "yoke" |
| ὀτραλέως ἐπίθοντο (3.260) | "promptly obeyed" | "obeyed promptly" | "quickly", "briskly" ("briskly" is kept for ἐπιτροχάδην-type words); ὀτραλέως "promptly" as in odyssey-092 |
| ἂν δ’ ἄρ’ ἔβη Πρίαμος, κατὰ δ’ ἡνία τεῖνεν ὀπίσσω (3.261) | "And up went Priam, and the reins he drew tight backward" | "Priam mounted, and drew the reins back tight" | "pulled the reins taut", "tightened"; ἡνία "reins" as shipped at odyssey-013 and -027 |
| περικαλλέα … δίφρον (3.262) | "the very beautiful chariot" | "the very beautiful chariot" | "exceedingly beautiful", "very fair"; περι- "very" (as in περικαλλής); δίφρος "chariot" as shipped at odyssey-012 and -013 |
| διὰ Σκαιῶν πεδίον δ’ ἔχον ὠκέας ἵππους (3.263) | "through the Scaean gates to the plain held the swift horses" | "drove the swift horses through the Scaean Gates toward the plain" | "kept", "guided"; the Gates "Scaean Gates" as in iliad-017 (3.145) |

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

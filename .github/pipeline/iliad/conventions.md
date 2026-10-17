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

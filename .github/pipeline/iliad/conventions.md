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

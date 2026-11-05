# Review — iliad-158 (Iliad 24.596–706), pass 1 (units.json; gloss.json awaits pass 2)

Method: notes' labels, positions and cross-references checked against the line; Greek to `l` word by word; `l` against `i`; remembered English; quotation marks (previous part iliad-157 ends with its speech closed, so 599 opens a new speech); `p` flags and `t` cut re-checked against the packet by script (all 58 units: `t` identical to the edition lines, `p` true exactly at the nine ¶ lines, `l` line counts equal `t`, no ASCII quotes). Every epithet and key word grepped in `conventions.md` and `../odyssey/conventions.md`. `t` was not touched (verified identical before and after).

Counts: high 1, medium 6, low 9 (16 changes).

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 664 | l, i | high | Priam's speech opens at 660 (`mark`, “) and ends at 667 with εἴ περ ἀνάγκη; the last unit (664–667) had no closing ”, leaving the speech open into Achilles' reply formula at 668. | Added ” to the end of both `l` and `i`. |
| 608 | l | medium | "she said that the two had borne" read as if "the two" were the subject; in the Greek δοιώ is the object of τεκέειν and the subject (Leto) is understood. | `l` now "she said that [Leto] had borne two, but she herself had borne many;". Note already correct. |
| 704 | l | medium | "Hector, going," attached "going" to Hector; ἰόντες is nominative, agreeing with the Trojans. | `l` now "…Trojans and Trojan women, Hector, as you go,"; one clause added to the note saying ἰόντες agrees with the Trojans, not with Hector. |
| 690 | i | medium | `i` "through the camp" for κατὰ στρατόν while `l` has "army" and the house word is "army" (7.380 "throughout the army"; 23.285). | `i` now "drove swiftly through the army himself". |
| 605 | i | medium | `i` "angry at Niobe" for χωόμενος; the house table fixes χώομαι as "be incensed" (row χωόμενος κῆρ, which names "angry" as avoided; "anger" is kept for χόλος). | `i` now "incensed at Niobe". |
| 626 | n | medium | Note claimed "the word order puts the verb first and Achilles last"; in ἀτὰρ κρέα νεῖμεν Ἀχιλλεύς the verb is second (κρέα first). The "host's portion of the work" gloss was also vague. | Rewritten: "the meats first and Achilles last, set against Automedon, who deals out the bread." |
| about | about | medium | "grants twelve days of truce": Priam's plan (664–667) is nine days' mourning, burial on the tenth, the mound on the eleventh, fighting on the twelfth, i.e. eleven days of truce. | "grants the days of truce he asks for". |
| 602 (604) | n | low | Packet flag at 604 (UNRESOLVED, spondaic fifth). Hand scan: ἓξ μὲν | θῡγᾰ-τε | ρες ἓξ | δ᾽ υἱέ-ες | ἡ-βώ | οντες. Foot 2 needs θυ- lengthened, foot 3's longum -ρες is long by the digamma of ἕξ, and the fifth foot ἡ-βώ is a true spondee (η and ω both long, no correption). The note already gave the first two; the third was missing. | Added one sentence: "Its fifth foot is also a spondee (ἡ-βώ-), a rare ending in the hexameter." The packet shows the same line published in odyssey-045. |
| 631 | i | low | "Priam, the descendant of Dardanus"; the table's Δαρδανίδης Πρίαμος (3.303) is "a descendant of Dardanus" (and the same unit group at 628 already says "a"). | "a descendant of Dardanus". |
| 631 | l | low | "And in turn Achilles marvelled": αὐτὰρ ὅ is "but he" (cf. 21.367); "in turn" is not in the Greek (`i` may keep "in his turn" as idiom). | `l` now "But Achilles marvelled at Dardanus’ descendant Priam,". |
| 650 | n | low | Note glossed βουλὰς βουλεύουσι as "plan plans" while `l` says "counsels counsel" (and the table keeps "counsel"). | Note now "counsel counsels". |
| 668 | l (and new-renderings row) | low | `l` "And him in turn addressed…" departs from the table's τὸν δ’ αὖτε προσέειπε pattern ("Him then in turn addressed", rows 6.440, 9.114, 10.168, 24.217 …), though the new-renderings row claims to follow it. | `l` now "Him then in turn addressed swift-footed, heavenly Achilles:"; the same change made in the row in `new-renderings.md`. `i` already matched. |
| 669 | n | low | Note said καὶ ταῦτα "points at the twelve days"; it points at the plan Priam has just set out. | "points at the plan Priam has just set out (664–667)". |
| 679 | i | low | `i` "sleep did not hold Hermes" for οὐχ … ἔμαρπτεν; μάρπτω is "seize" (the note says so); "hold" is the sense of ἔχε at 2.2, a different verb. | "sleep did not take hold of Hermes". |
| 703 | n | low | "The colon announces her speech": the Greek mark is the ano teleia; every other note uses that name. | "The ano teleia announces her speech." |
| 614 | n | low | `l` "danced" (aorist ἐρρώσαντο) but `i` "dance", with no word in the note about the shift in tense. | Note now says the English gives the present "dance" because the nymphs are said still to dance there. |

## Checked and left alone (findings considered and refused)

- **Merged unit 679–682** (drafter kept "He stood over Priam’s head"). Accepted. A stand-alone 682 would have to repeat iliad-143's `l`/`i` exactly ("and it stood then above his head" / "It stood over his head and spoke to him"), and that English is about the ghost of Patroclus ("it"), wrong for Hermes. `validate_iliad.py` compares whole units only (the key is the unit's whole `t`), so a unit that contains the repeated line plus 679–681 raises neither a FAIL nor a WARN, and the build has no rule against two sentences in a unit (the note says so explicitly). "Priam’s" instead of "his" is right (the pronoun would be ambiguous after Hermes' subject). The `l` keeps the published "above his head". The cost is one longer unit; no change.
- **τύμβος "mound"** (664–667). The table is split ("tomb" at 2.793, 4.177, 16.457; "mound" at 7.337 `i` and, most recently, 23.245). The draft follows the latest (23.245). Left; the owner may want one word for τύμβος across the poem.
- **γέγωνε "called aloud"** (703). Row 4875 has `i` "called out"; here κώκυσε (the house "cried out") sits in the same clause, and "She cried out, and called out" would repeat. Left as "called aloud" in both layers; mention if a later pass wants to unify.
- **ἐν φόνῳ `l` "in slaughter" / `i` "in their blood"** (610). Departure is in the new-renderings row with a reason and the note says so. Left.
- **κατὰ κόσμον `i` "in good order"** (622): `l` "in due order" matches the table (5.759, 8.489); the Odyssey `i` for 8.489 is "in very good order", so "in good order" is within the house. Left.
- **694 `i` "Hermes then went off" vs the Odyssey's "Then Hermes went off"** (692): the warning is only for whole-unit repeats, and the "when …, then" frame needs the order given. Left.
- **σεῖο … ζωοῦ `i` "for your life"** (686): reads as the price for his being alive; closer than "for you alive" would be in flow. Left.
- **λαός `l` "people" / `i` "army"** (656, line 658): matches the Iliad house (2.450, 4.184, 10.364: "army" of the Achaean host in `i`); λαός of the Trojan people (664–667) is "people". Left.
- **ἦ ῥα / ἦ ῥ’ / ἦ καί `i` "So he spoke / So he said, and"**: matches table rows. Left.
- **649 `l` "And him, taunting, addressed…"**: the Odyssey row 22.194 has no "And", but 3.413 ("And her, enraged, addressed…") shows "And" is accepted for τὸν/τὴν δ’ + participle. Left.
- **ἠΰκομος Νιόβη, ἐριούνιος "the helper", Οὐρανίωνες "Uranians"/"gods of heaven", καλλιπάρῃος, ἰοχέαιρα, Κρονίων, αἴθοπα οἶνον, ἐγκονέουσαι, ποιμένι λαῶν, μήδεα πυκινά, ἱπποκορυσταί, πυλαωρός, Πέργαμος** all conform to the table. Repeated lines (604 Odyssey; 623–624, 626, 627, 628, 636, 644–646, 653, 656, 659, 674, 677, 678, 692–694) take the published English; units whose whole Greek is published (656, 659, 677/678 inside larger units) were compared and are word for word.
- **Remembered English**: nothing found that is a recalled phrase rather than a rebuilding of the grammar. 704–706 ("if ever you rejoiced … great joy to the city and to all the people") is close to common versions but is what the Greek says word for word; left.
- **Cross-references** (all true): 617 end of Niobe's tale; 601/602/613 μνήσατο; 611/612 θάπτω; 607 and 676 καλλιπάρῃος; 649 πόδας ὠκύς; 629/631; 617/637 πέσσω; 650–655/671; 672/689 δείδω; 688/690 γνώῃ/ἔγνω; 691/697 ἔγνω; 600/702 λεχέεσσι; 636 and 644–646 shared with odyssey-016; 674 with iliad-154; 677 with Iliad 2.1; 692–694 with iliad-090 and Odyssey.

## new-renderings.md (21 data rows; the brief said 22)

All 21 rows are sane and conform to their stated houses. One row corrected (668, see above). Checked: Pergamus consistent with the table (5.460); ἐκνοστήσαντι follows ἐκνοστήσαντε (5.157); ἐρρώσαντο row now matches the note; ἱεροὺς πυλαωρούς follows πυλαωρός (21.530) and ἱερός; the 634 row matches the published γέρων Πρίαμος θεοειδής English; 695 follows 8.1 (δέ for μέν).

## For pass 2

gloss.json is not yet read. Pass 2 should check each parse against the (now edited) units, especially ἰόντες (704, nominative plural), ἐρρώσαντο (aorist middle of ῥώομαι), λέξο (aorist imperative middle), ἕντο, δαινῦτο (optative of δαίνυμι, 665), μέμονας, ἐέλμεθα, πεπάσμην, ἀξέμεν, and the homographs βιοῖο/βίος.

---

# Pass 2 (units.json re-read after edits; gloss.json read in full)

Method: `units.json` re-read Greek → `l` → `i`, notes and quotation marks after pass-1 edits (all speech marks now balance: 599–620, 635–642, 650–658, 660–667, 669–670, 683–688, 704–706; nothing new found except the 695 note below). `gloss.json` checked by script against `iliad_lib` (every form of the part has an entry; no entry redefines an existing one; no ASCII quote or backtick; all new entries under 230 characters; all 20 `__broaden__` entries keep the old entry whole), then every parse against its line, then all 454 known forms read against their existing entries for uses they do not cover. The glosser's rewrites of the Odyssey-derived entries (34 in `odyssey-forms.json`) were compared one by one with the originals.

Counts, pass 2: high 0, medium 6, low 11 (17 changes).

| Entry / line | File | Severity | What was wrong | What was done |
|---|---|---|---|---|
| χαίρετ (706) | gloss | medium | Parsed "pres. imper. 2 pl. ’rejoice!’" (copied from the Odyssey entry); in εἴ ποτε … χαίρετ’ it is indicative, and the unit's note and `i` say "you rejoiced". | "impf. 2 pl., elided … unaugmented (= ἐχαίρετε), after εἴ ποτε: ’you rejoiced’". |
| ταρπώμεθα (635) | gloss | medium | Glosser changed the Odyssey's correct "’we may take our fill’" to "hortatory: ’let us …’"; after ὄφρα it is purpose. | "in a purpose clause after ὄφρα: ’that we may take our fill’". |
| ἐρύκω, μένω (broaden), τέως (658) | gloss | medium | ὄφρα τέως … μένω … ἐρύκω was parsed as a temporal clause ("for so long as I stay"); the unit's `l`, `i` and note read it as purpose ("so that for so long I may wait"), and the known ὄφρα entry lists purpose first. | All three entries now say purpose clause after ὄφρα, with the matching glosses. |
| γυναικῶν (698, broaden) | gloss | medium | New clause "after πρόσθε: ’before (all) women’" contradicts the unit note, which takes ἀνδρῶν … γυναικῶν as a partitive genitive after οὐδέ τις ἄλλος. | Clause now "partitive after οὐδέ τις ἄλλος: ’of … women’ …". |
| δοῖεν (686) | gloss | medium | Known entry covers only wish and protasis; here it is the potential with κε (σεῖο δέ κε … δοῖεν ἄποινα). | Broadened: "also aor. opt. 3 pl. with κε, potential: ’they would give’". |
| 695 (ἔλων) | units n | medium | Note called ἔλων "the participle ‘driving’", but the subject οἳ is plural and a participle would be ἐλόωντες/ἐλῶντες; it is a 3 pl. verb. The gloss already (rightly) treated it as a finite form. | Note: "ἔλων is ‘they were driving’, a rare epic form of ἐλαύνω (here a 3 pl. imperfect)". |
| ὅσσος (630) | gloss | low | "indirect exclamation"; the unit note says two indirect questions. | "indirect question". |
| γέγωνέ (703) | gloss | low | Gloss ’cried aloud’ collides with κώκυσε "cried out"; `l`/`i` say "called aloud". | ’called aloud’. |
| λεχέεσσ (702) | gloss | low | ’on a bier’; the house rendering is "bed" ("bier" avoided). | ’on a bed’. |
| νιόβῃ (606) | gloss | low | ’angry with Niobe’; house χώομαι is "incensed" (pass-1 fix to `i`). | ’incensed at Niobe’. |
| πέργαμον (700) | gloss | low | "Pergamos"; the Iliad glossary and table say "Pergamus". | "Pergamus". |
| ἐριούνιον (679) | gloss | low | "bringer of luck" asserted one guess among others; the house position is that the sense is unknown. | "helper … sense unknown, ’helper’ is one ancient guess". |
| ἄργυφον (621) | gloss | low | ’white’ drops ἀργ-; house is "silver-white" (Odyssey ἄργυφα μῆλα). | "silver-white". |
| ὕπο (636, broaden) | gloss | low | Known entry has no state/means use for ὕπνῳ ὕπο γλυκερῷ. | Added "+ dat. of the state one is in: ’in, under’". |
| ὑπὸ (638, broaden) | gloss | low | Known entry has the dative of agent only after a passive; ὑπὸ χερσίν goes with the active ὤλεσε. | Added "dative of the agent with an active verb: ’at the hands of’". |
| τοῖσιν (690, broaden) | gloss | low | Dative of advantage ("for them") not listed. | Added. |
| οἰμωγῇ (696, broaden) | gloss | low | Known entry pinned to εἴχοντο only. | Added the instrumental use with στοναχῇ. |

Checked and left: all the other 80 novel parses (including ἰόντες, ἐρρώσαντο, λέξο, λέξον, ἕντο, δαινῦτο, μέμονας, ἐέλμεθα, πεπάσμην, ἀξέμεν, βιοῖο/βίος, κέατ’ as imperfect, καθέηκα, γνώῃ, κλαίοισθα, γοάοιμεν, θάπτοιμεν, ποιήσαιμεν, πολεμίξομεν, ἐκπέμψειε) are true of the form in the line; the remaining 15 broaden entries (δοιὼ, εὐνάς, κάμε, κλισίης, κείμενον, Λητοῖ, νεκροῖο, σεῖο, σῇς, τηλόθι, τόσσον, τῇ, ὅπως, ἐόντ’, ἡμιόνων, φόνῳ, ἔπειτά, ὧδέ) are true of their lines. The glosser's other changes to the Odyssey-derived entries (κέατ’ as imperfect, κήρυκά … τε, ζωοῦ, δόρπου, etc.) are accurate for this part; the entry for εἰσενόησεν has the lemma εἰσνοέω, which I could not confirm in the sources and left. οἷός (630) and πρόσθ’ (698) in the known list are close enough to the existing entries to leave.

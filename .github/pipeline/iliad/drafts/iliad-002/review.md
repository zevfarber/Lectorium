# iliad-002 (Iliad 1.101–205): review

Reviewer pass 1 (labels, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, `p`, house tables, new-renderings rows) and pass 2 (the whole file re-read after the edits). Sources used: the Greek, the Iliad and Odyssey conventions and house tables, the published Odyssey units and `iliad-001.json` as English precedent. No modern translation consulted. `units.json` edited in place by script; `t` untouched (checked: every `t` identical to the pre-review file, and the units still concatenate to the packet's 105 lines). `gloss.json` does not exist yet, so the second-pass parse check against it was not possible.

Counts: 27 changes (5 high, 11 medium, 11 low), touching 37 unit fields; plus 6 edits to `new-renderings.md`.

Severity: high = identical Greek given different English from a published Odyssey unit, or a note that states something false about a form; medium = house-table or Iliad-internal inconsistency, or a wrong claim about where a word stands or what a cross-reference says; low = precision, particle force, polish.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 103 · l, i, n | high | The couplet μένεος δὲ μέγα φρένες ἀμφιμέλαιναι / πίμπλαντ’, ὄσσε δέ οἱ πυρὶ λαμπετόωντι ἐΐκτην is Odyssey 4.661–662 (odyssey-020, ln 661), already published ("and his heart, black all about, was greatly filled / with fury, and his two eyes were like blazing fire"; i "his heart, black through and through, swelled greatly with fury, and his eyes seemed like blazing fire"). The packet did not list it (it lists only whole-line matches), and the draft renders it afresh ("wits", "black-all-round", "were like"), with two rows in new-renderings that wrongly present it as new. | `l` and `i` replaced by the Odyssey's wording verbatim; note now says the couplet stands at Odyssey 4.661–662 and that φρένες is "heart" here (note kept to the 25–110 band). The two new-renderings rows (ἀμφιμέλαιναι, μένος) removed. |
| 113 · l, i, n | high | οὐ δέμας οὐδὲ φυήν is published twice in the Odyssey as "not in body nor in stature" / "in body or in stature" (odyssey-024, ln 211; odyssey-031, ln 208); the draft has "build". οὔτ’ ἂρ φρένας οὔτέ τι is published as "neither in mind nor at all in looks" (odyssey-016, ln 263; cf. odyssey-034, ln 167 "nor then mind"); the draft has "wits". | `l` "not in body nor in stature, nor then in mind nor in any works"; `i` "in body or stature, in mind or in any of her works"; note's gloss list changed to match. |
| 137 · n | high | Note says Αἴαντος, Ὀδυσῆος and τεὸν are "all genitives with γέρας". τεὸν is the neuter accusative agreeing with γέρας; only the two names are genitives. The note also asserted "the poem has two Ajaxes", which this part cannot show. | Note: τεὸν agrees with γέρας; the two names are genitives depending on it; "Which Ajax is meant, the text here does not say." |
| 140 · l, i, n | high | νῆα μέλαιναν ἐρύσσομεν εἰς ἅλα δῖαν is published (odyssey-033, ln 34) as "a black ship let us drag down into the heavenly brine" / "let us drag a black ship down into the heavenly brine"; the draft has "draw … to the heavenly salt-sea" / "haul … down to the heavenly sea". The Odyssey table fixes δῖος on the sea as "heavenly" in both layers and the shipped ἅλα as "brine". Note's "the plan he began with" also pointed at nothing in the speech. | `l` and `i` conformed ("drag", "into the heavenly brine"); note glosses changed; note now says the speech turns to "the business of sending the girl back". |
| 193 · l, i | high | ἧος ὁ ταῦθ’ ὥρμαινε κατὰ φρένα καὶ κατὰ θυμόν is published three times (odyssey-015 ln 120, odyssey-025 ln 365, odyssey-026 ln 424) as `l` "While he was pondering these things in mind and in heart," / `i` "While he was turning this over in his mind and heart". Draft `l` had the simple past "pondered" against its own note ("was pondering"), and `i` "was pondering this". | Both layers conformed to the published wording. The new-renderings row for 1.193 removed (no longer new). |
| 135 · i | medium | "give me a prize": γέρας is "prize of honour" in `i` at every occurrence (the draft's own row and the Odyssey table). | "give me a prize of honour". |
| 137 · i | medium | "take your prize" – same. | "take your prize of honour". |
| 166 · i | medium | "the far bigger prize is yours" – same. | "the far bigger prize of honour is yours". |
| 146 · l, i, n | medium | ἐκπαγλότατ’ ἀνδρῶν rendered "most overpowering" with no row; the Odyssey table fixes ἔκπαγλος as "terrifying" (10.448, 17.215), and "overpowering" is not recorded as a departure. | `l`, `i` "most terrifying of all men"; note glosses changed; a row added to new-renderings. |
| 154 · l, i, n | medium | ἐπεὶ ἦ μάλα πολλά: published as "since in truth very many things" / "truly" (odyssey-049, ln 463). The draft has "indeed" in `l` and drops ἦ in `i`; ἦ is "truly / in truth" throughout the Odyssey. | `l` "since in truth very many things lie between"; `i` "since truly a great deal lies between us"; note's gloss changed. |
| 169 · l, i | medium | ἐπεὶ ἦ πολὺ φέρτερόν ἐστιν: published (odyssey-058 ln 108, odyssey-103 ln 153) "truly much better" / "since truly it is far better". The draft has "indeed" in `l` and no force at all in `i`. | `l` "since truly it is much better"; `i` "since it is truly much better". |
| 204 · l | medium | ἀλλ’ ἔκ τοι ἐρέω is published (odyssey-006 ln 187, odyssey-093 ln 167) as `l` "But I will speak out plainly to you"; the draft has "But out to you I will speak". `i` already matched. | `l` "But I will speak out plainly to you, and this too, I think, will be fulfilled:". |
| 111 · n | medium | "ἔχειν … is the infinitive that waits for οἴκοι ‘at home’ in the next line": both οἴκοι and ἔχειν stand in line 113, οἴκοι first. | Note: "οἴκοι ἔχειν, ‘to keep at home’, opens the next line." |
| 127 (first unit) · n | medium | "answered by αὐτὰρ Ἀχαιοί in the next line": αὐτὰρ Ἀχαιοί is in line 127 itself, the same line as σὺ μὲν νῦν. | "in the next unit". |
| 106 · n | medium | "the whole speech is a charge against Calchas": 106–115 are the charge and the excuse, but 116–120 concede the girl and demand a prize from the whole assembly (the draft's own note at 118 says so). | "the first part of the speech is a charge against Calchas, before it turns to the prize he wants." |
| 176 · n | medium | "διοτρεφέων βασιλήων, a partitive genitive with the Homeric ending -ήων": the adjective ends in uncontracted -έων; only βασιλήων has -ήων. | Note states both endings correctly. |
| 105 · n | low | "Agamemnon turns on the seer before anyone else" – πρώτιστα does not say that, and he turns to the assembly at 118. | "turns on the seer first". |
| 113 · l | low | καὶ γάρ ῥα rendered "for in truth", which is the rendering of ἦ; the Odyssey renders ἄρα/ῥα "then" (and the same unit has οὔτ’ ἂρ "nor then"). | "for indeed, then,". |
| 144 · l | low | ἱλάσσεαι rendered "appease" in `l`; iliad-001 (1.100) and odyssey-013 (ln 418) have "propitiate" in `l`, "appease" in `i`. | `l` "propitiate"; `i` kept "appease"; note gives "propitiate, appease". |
| 176 · l | low | δέ dropped in `l` ("Most hateful to me are you"). | "And most hateful to me are you". |
| 179 · l | low | σέθεν δ’ … οὐκ ἀλεγίζω rendered "for you I do not care": "for" reads as γάρ or "on your behalf"; the Greek is the genitive object with δέ. | "but of you I do not care". |
| 182 · l | low | σὺν νηΐ τ’ ἐμῇ καὶ ἐμοῖς ἑτάροισι is published (odyssey-040 ln 173) as `l` "with my ship and with my companions". | `l` conformed. |
| 188 (second unit) · l | low | Πηλεΐωνι rendered "Peleus’ son"; Πηλεΐων is "the son of Peleus" in the Odyssey table and in this very unit's `i`, note and 1.197 row. | "to the son of Peleus". |
| 160 · n | low | "τῶν … refers back to the honour": τῶν is plural and could as well take in the whole business; the single-noun antecedent was asserted. | "is plural and takes in the whole business of winning honour from the Trojans." |
| 121 · n | low | "the same shape as the answer at 1.84": 1.84 is the ἀπαμειβόμενος formula, not this one. | "the formula at 1.84 is a different one, with ἀπαμειβόμενος." |
| 181 · n | low | Note 19 words (warn band is 25–110). | One true sentence added ("What he threatens comes in the next two units."). |
| 188 (first unit, ὣς φάτο) · n | low | Note 22 words. | Added that it closes Agamemnon's speech and that the sentence goes on with Achilles' reaction. |

### new-renderings.md
- Removed the rows for ἀμφιμέλαιναι, μένος (1.103) and ὃ ταῦθ’ ὥρμαινε … (1.193): they are now the Odyssey's published English, not new.
- εὐρὺ κρείων: added that the Odyssey ships the same wording (3.248).
- ἀγέραστος: `i` column now says "without one" (the prize of honour just named in the same sentence), which is what the unit has (the row had "without a prize of honour"; the unit's natural English was kept).
- ἐξαλαπάξαι: the row said only "sack" is kept for ἐκπέρθω; it did not mention that the Odyssey ships "sacked" for this very word (3.85) and "laid waste" for ἀλαπάζω. The row now records that departure and its reason.
- Added ἐπιτηδές (1.142; "suitably" against the Odyssey's "on purpose") and ἐκπαγλότατ’ ἀνδρῶν (1.146).
- Checked every other row against the units: all match.

## Checked and found correct (no change)
- `t`/packet identity; `p` on exactly the six ¶ lines (101, 121, 130, 148, 172, 188); `mark` on the first unit of each of the six speeches (106, 122, 131, 149, 173, 202), “ on each of those units and ” on the last (120, 129, 147, 171, 187, 205); no quotation marks elsewhere; iliad-001's last unit (1.100) ends with ”, so this part opens outside a speech.
- Scansion flags: none; nothing to add to a note.
- Both formula lines that the packet lists (101 = 1.68, 201 = odyssey-002) are exact; 130, 121/172 and 148 follow the Odyssey reply-formula rows; "Greeks" is absent from both layers; Achaeans/Danaans/Argives used consistently.
- Grammar labels in every other note checked against the line (including ἐπέσσυται, κεχολώσεται, ἀπαμειβόμενος/προσέφη, δώωσιν, ἐρύσσομεν, θείομεν, ἐΐκτην, φάανθεν, ὁρᾶτο, οἴῳ φαινομένη, the tmeses at 101, 142–143, 195, 199, and σ’ = σοί at 170); line-position claims (103, 108, 119, 123, 137, 161, 184, 190–192, 195, 104) and cross-references (1.7, 1.19, 1.23, 1.58, 1.65, 1.68, 1.96, 1.98, 1.121, 1.1) all true.

## Considered and refused
- **ἐξαλαπάξαι "plunder"** against the Odyssey's "sacked": kept. "Sack" is already fixed for ἐκπέρθω in this part and in iliad-001, and the Odyssey table itself has "laid waste" for ἀλαπάζω, so there is no single precedent to follow; the departure is now recorded with its reason.
- **θάμβησεν "was struck with wonder"** in both layers, where the Odyssey has "amazed" in `l` (3.322, 16.178) but "struck with wonder" in `i` (3.322), and its table reserves "wonder" for θάμβος: kept; consistent with the table row, and the Odyssey's own usage is mixed.
- **ἐπιτηδές "suitably"** against "on purpose" (15.28): kept (a levy of rowers, not an ambush); a row now records it.
- **φρεσί at 107 "wits"** against the Odyssey's "mind" at 19.347: kept; the table has φρένες ἐσθλαί "good wits" and the datives are not the same expression.
- **"to none of which you pay regard" (160)** for οὔ τι: kept as a reading of τι; the note's "not at all" is the same sense.
- **Capital or lower-case "But/and" after a semicolon** (125, 127, 137, 139): the published Odyssey uses both; no rule broken.
- **αὖτε at 202** ("again" in `l`, "now" in `i`): kept; the note and the row give the reason (no earlier visit in the text), and the Odyssey rows render αὖτε "in turn / again" only in reply formulas.
- **"shone dread" (200)**: kept; the house δεινός "dread" is applied and recorded, and the predicate use is a poetic but readable English.
- **"give me" (135), "grants us" (129), "my wedded wife" (113)**: pronouns supplied from the sense of the passage in `i` and one `l`; no Greek is contradicted.
- **ὡς = "since" (182)**: kept; ὡς "since, as" is in LSJ and the following clause fits.
- **δή dropped in `i` (110), γάρ dropped in `i` (123)**: force carried by word order and context; not a change in sense.
- **"Atreus’-son" (102, 122) beside "the son of Atreus" (191)**: kept; the Odyssey uses both for the nominative/vocative and accusative.

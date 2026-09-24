# Review: odyssey-010 (Odyssey 3.102–209)

I checked this part against `conventions.md`, `packet.md`, `new-renderings.md`, `LOG.md`, the source archive
(`source/odyssey-murray1919.json`, for the lines before and after the part) and the published `odyssey-001` to
`odyssey-009.json` at the repository root. Every repeated line and cross-reference was checked against those
shipped files, not against the packet's transcription. I did two passes over `units.json`, re-reading my own
first-pass edits at the end to catch anything introduced or missed. This is Pass 1 (translation) only; the
glossary has not been run yet and is out of scope here.

**57 units.** The concatenated `t` reproduces `packet.md` exactly (spot-checked at both ends and by length,
4,764 characters, unchanged before and after every edit — `t` was never touched). `p: true` falls on exactly
Murray's three ¶ lines for this part: 102, 184, 201, matching the packet. No `t`, `ln` or `p` field was touched.

**Speech-boundary structure (resolved).** Two speeches, both opening and closing wholly within this part:
- **Nestor's speech**, 3.103–199. The reply-formula at 3.102 (`mark: "Nestor answers"`) is narration and
  carries no quotation mark, matching the project's established pattern (e.g. odyssey-009's own reply-formulas);
  the speech itself opens with “ at 3.103 and closes with ” at 3.199, the last line before Telemachus's own
  reply-formula at 3.201 (¶).
- **Telemachus's speech**, 3.202–209. Again the reply-formula (3.201, `mark: "Telemachus answers"`) carries no
  mark; the speech opens with “ at 3.202 (reusing 3.79's wording, odyssey-009) and closes with ” at 3.209. I
  confirmed the close by reading the source archive's line 3.210, the first line of the *next* part: it is
  `τὸν δ’ ἠμείβετ’ ἔπειτα Γερήνιος ἱππότα Νέστωρ·`, a fresh ¶ and a fresh reply-formula — the very words that
  open this part's own Nestor's speech. Telemachus's speech does not run on as direct discourse into odyssey-011;
  a new speech begins there after a narrator's frame, exactly as odyssey-009 ended and odyssey-010 begins. This
  also settles the Drafter's own flagged uncertainty at 3.209 (below).

**As drafted, this part had almost no quotation marks at all** — a single “ at 3.202 and nothing else, in
either layer. Nestor's entire 97-line speech (3.103–199) had no opening or closing mark, and Telemachus's
speech had an opening mark but no closing one. This is the same class of part-wide omission recorded as a
major finding in odyssey-008's log. I fixed it as the leading item below.

**Findings fixed: 2 major (quotation-mark structure), 4 major (augment mislabels), 6 moderate, 4 minor.**
The four flagged items in `new-renderings.md` are ruled on explicitly below. Findings considered and refused
are listed at the end.

## Pass 1 — `units.json`

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 3.103–199 | `l`, `i` | **major** | Nestor's speech carried no quotation marks at all: no opening “ where the speech's actual words begin (3.103, after the non-quoted reply-formula at 3.102), and no closing ” at its last line (3.199). Only Telemachus's speech (from 3.202) had an opening mark. | Added “ to the start of `l` and `i` at 3.103, and ” to the end of `l` and `i` at 3.199. Marks now balance at 2 opening / 2 closing in both layers across the part. |
| 3.209 | `l`, `i`, `n` | **major** | The Drafter judged 3.209 grammatically complete but left the closing quotation mark off, on the guess that "the speech itself likely continues... in odyssey-011" (see the flagged item, below). The source archive shows this guess is wrong: 3.210 is a new ¶ opening with the reply-formula `τὸν δ’ ἠμείβετ’ ἔπειτα Γερήνιος ἱππότα Νέστωρ·` — the identical formula that opens this part's own Nestor's speech. Telemachus's speech ends at 3.209; it does not run into the next part as open discourse. | Added ” to the end of `l` and `i`. Note rewritten to state the verified fact (the next line's reply-formula) instead of the earlier guess. |
| 3.108 | `n` | **major** | κατέκταθεν was called "an unaugmented aorist passive". It is augmented: the preverb κατά elides its final vowel only because a vowel (the augment) follows it (κατ’ + ἔκταθεν); the unaugmented form is κτάθεν. This is the Drafter's known recurring error (LOG, odyssey-002 onward). | Note corrected to "augmented aorist passive... the unaugmented form is κτάθεν, found elsewhere in Homer," with the elision given as the reason. |
| 3.141 | `n` | **major** | ἑήνδανε was called "an unaugmented imperfect of ἁνδάνω". It is augmented: the verb's root once began with digamma (ϝανδάνω), so the augment ἐ- surfaces as ἑ-, the same family as the augmented ἥνδανε of Iliad 1.24 (also of Agamemnon's displeasure). The unaugmented form is ἄνδανε. | Note corrected to "augmented imperfect", with the digamma explanation and the Iliad parallel; unaugmented ἄνδανε given for contrast. |
| 3.173 | `n` | **major** | ᾐτέομεν was called "an unaugmented imperfect of αἰτέω". The ᾐ- spelling (eta with iota subscript, in place of the diphthong αι-) is itself the mark of the augment; only the ending is left uncontracted, epic-style. The unaugmented form would keep the diphthong, αἰτέομεν. | Note corrected to "augmented imperfect... with its ending left uncontracted", distinguishing the augment (on the stem) from the uncontraction (on the ending). |
| 3.182 | `n` | **major** | ἔσβη was called "an unaugmented aorist of σβέννυμι". It is an augmented root aorist: the root is consonant-initial (σβη-), so the augment shows plainly as the prefixed ἐ-. The unaugmented form is the bare σβη. | Note corrected to "augmented root aorist... the unaugmented form would be the bare σβη". |
| 3.120 | `n` | moderate | μῆτιν ὁμοιωθήμεναι after ἤθελ(ε) was called "an infinitive of purpose". ἐθέλω takes a complementary (object) infinitive, not a purpose infinitive. | Note corrected to "a complementary infinitive... not a purpose infinitive: ἐθέλω regularly takes its infinitive as a direct object." |
| 3.132 | `n` | moderate | The note said "λυγρὸν … νόστον... is a new phrase that recurs at 194", but 194 pairs λυγρός with a different noun (ὄλεθρον, not νόστον) — it is the adjective that recurs, not the phrase. The part's own later note at 3.193 gets this right ("the same word"), so the two notes contradicted each other. | Note corrected: "the adjective λυγρός recurs at 194, there describing Aegisthus's crime... rather than the same noun." |
| 3.196–198 | `n` | moderate | The note said πατροφονῆα (line 197) "reuse[s] the wording already fixed for this same line, 3.198" — but πατροφονῆα is on line 197, which is not itself a repeated line (odyssey-003's parallel line uses a different verb, ἔκτανε, not ἐτίσατο); only line 198 is the identical, already-published formula. | Note rewritten to keep the two apart: 197 is not a repeat (though it happens to share the one word), and 198 alone is identified as identical to 1.300 (odyssey-003), reusing its English. |
| 3.201 | `n` | moderate | The note read "This reply-formula is identical to 3.201, already published" — but this unit *is* 3.201; the cross-reference was self-referential and meaningless. | Corrected to cite the actual earlier occurrence: "identical to the line already published at 1.388 (odyssey-004)". |
| 3.202 | `n` | moderate | Same bug: "reuses the wording already fixed for 3.202" self-referenced this unit's own line number instead of the source it was copied from. | Corrected to "reuses the wording already fixed for the same line at 3.79 (odyssey-009)". |
| 3.208 | `n` | moderate | The note said ἐπέκλωσαν "is the same fate-spinning verb the table fixes at 1.17" — there is no house-table row for ἐπικλώθω/ἐπεκλώσαντο in `conventions.md`; the claim overstated what is actually fixed. | Reworded to describe the verb accurately without claiming a table entry that does not exist. |
| 3.115 | `n` | minor | "παραμίμνων… governs ἐξερέοις" reverses the grammatical relation: a circumstantial participle does not govern a finite verb. | Reworded: "a participle attached to the unexpressed subject of ἐξερέοις… inside the εἰ-clause." |
| 3.160 | `n` | minor | The note claimed σχέτλιος applied to Zeus is "elsewhere reserved for reckless men" — an assertion about the rest of the poem this part (and the published parts so far) cannot show; σχέτλιος does not occur in odyssey-001–009. | The unverifiable clause was cut; the note now just says the word is "a striking judgment for a god to receive." |
| 3.195 | `n` | minor | "recur through the rest of this speech" is imprecise: τίσασθαι/ἐτίσατο recur at 3.206, which is inside Telemachus's separate speech, not Nestor's. | Changed to "recur through the rest of this part, in both Nestor's and Telemachus's speeches." |
| new-renderings.md | table | minor | Six rows (Πάτροκλος, Ἀντίλοχος, Πρίαμος, Διομήδης, Ἰδομενεύς, Φιλοκτήτης) were plain proper names with no real `l`/`i` decision behind them ("avoided on purpose: — (plain proper name)"), out of step with how earlier parts logged proper names separately from the house-table formula list (e.g. odyssey-003's log: "14 new fixed renderings... plus 9 new proper names"). | Rows removed from the table. These six names still need adding to `conventions.md`'s prose proper-names list at publish time, alongside the ones already there. |

Every edited unit was checked again in the second pass. Quotation marks now balance at 2 opening / 2 closing
in both `l` and `i` (one speech-pair each for Nestor and Telemachus).

## The Drafter's 4 flagged items

1. **Comma-cuts at 3.103–108, 3.168–172 and 3.180–182.** Ruling: **keep 103–108 and 168–172; the 180–182 item
   is not actually a comma-cut.** 103–108 is one six-line sentence split 2+4 at the comma after Ἀχαιῶν (104),
   which is the boundary between the relative clause on ὀιζύος and the ἠμὲν…ἠδέ correlative that follows — the
   strongest pause available. 168–172 is one five-line sentence split 2+3 at the comma after ὁρμαίνοντας (169),
   the boundary before the embedded ἢ…ἦ alternative question — again the only strong pause. Both are good calls.
   180–182, however, is *not* a comma-cut at all: line 182 has its own ano teleia after ἵστασαν, so the material
   actually splits into two separate sentences (180–182a, ending ·, and 182b–183, ending .), each under the
   four-line cap on its own. No comma was needed there, and none was used — the unit boundaries in `units.json`
   are already correct; the Drafter's own description of this range was simply wrong. I also found one further,
   unflagged comma-cut at 3.130–131 (a five-line sentence, 130–134, split 2+3 at the comma after Ἀχαιούς, right
   at the boundary between the ἐπεί-clause and the ἐπεί… γάμος main clause that follows) — this is a good cut,
   correctly placed, just never mentioned in the Drafter's own list.
2. **3.135, 3.202: γλαυκώπιδος ὀβριμοπάτρης and κεῖνος left unnamed.** Ruling: **keep.** Both Athena (135) and
   Orestes (196, 202) are genuinely unnamed at every point they are mentioned in this part's Greek. Keeping the
   periphrasis/pronoun literal rather than silently inserting a name matches the table's established practice
   for ἱερὴ ἲς Τηλεμάχοιο and similar unnamed periphrases.
3. **3.199–200: packet's two transcriptions disagree on a comma.** Ruling: **not an error; no upstream fix
   needed.** I checked the source archive directly. Book 1 line 301 prints `καὶ σύ, φίλος,…` (comma, acute σύ);
   Book 3 line 199 prints `καὶ σὺ φίλος,…` (no comma, grave σὺ) — this is a real difference between the two
   printings of the formula in Murray's own edition, not a packet transcription slip: the packet's line-listing
   for 3.199 matches Book 3's own archive text exactly, and the packet's "already published" section is quoting
   Book 1's own archive text for 1.301, which likewise matches. Both are correctly reproduced verbatim in their
   own book's `t`, which is mechanically fixed and untouched. The accent/comma shift is the ordinary effect of a
   following pause on Greek accentuation, not a different reading, so this remains "the same line" in the sense
   the project's repeated-line rule cares about, and reusing the odyssey-003 English is correct. (Note reworded
   at 3.199 to record this reasoning rather than leaving the discrepancy as an open flag.)
4. **ἐπισμυγερῶς (195) absent from the house table.** Ruling: **keep, no addition.** It does not occur in
   odyssey-001–009, and a genuine Homeric rarity built on a low-frequency root (σμυγερός) is a reasonable
   candidate to leave unfixed unless and until it recurs.

## Repeated lines and cross-references: verified against the shipped files

| Line | Shipped source | Result |
|---|---|---|
| 3.198 (`Αἴγισθον δολόμητιν, ὅ οἱ πατέρα κλυτὸν ἔκτα.`) | odyssey-003 `ln` 298 (=1.300) | The formula's `l`/`i` match the published wording exactly (adjusted only for the different terminal punctuation of a statement vs. the published unit's question). |
| 3.199–200 (`καὶ σὺ φίλος…ἐὺ εἴπῃ.`) | odyssey-003 `ln` 301 (=1.301–302) | `l`/`i` are identical to the published couplet, aside from the closing ” now added. See the punctuation discrepancy ruling above. |
| 3.201 (`τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα·`) | odyssey-004 `ln` 388 | `t`, `l` and `i` are all identical. |
| 3.202 (`ὦ Νέστορ Νηληϊάδη, μέγα κῦδος Ἀχαιῶν,`) | odyssey-009 `ln` 79 | Only the first line of the two-part formula repeats here (the odyssey-009 unit continues with a different second line); that first line's `l`/`i`, including the opening “, are reused verbatim, as the "reuse the published wording... as far as your sentence allows" rule requires. |

I also checked all in-part cross-references named in the notes: ἀρήιος recurring 109→167 (verified: both lines
carry it); λυγρός recurring 132→194 (verified, corrected to name the right word, see above); Ἀτρεΐδῃσι/Ἀτρεΐδῃ
Ἀγαμέμνονι/Ἀτρεΐδην at 136, 156, 164, 193 (verified at each line); Τυδέος υἱός/Τυδεΐδεω for Diomedes at 167→181
(verified, both lines present); ἱπποδάμοιο extended from Nestor to Diomedes at 181 (verified against the house
table's Νέστωρ ἱππόδαμος row); θεσπεσίῃ (150) echoing the already-fixed θεσπεσίην … χάριν κατέχευεν row
(verified in `conventions.md`); ἱέμενος (159) "the same participle used of Odysseus in the poem's opening
lines" (verified in odyssey-001, `ln` 4 and elsewhere). All check out; no further fixes needed.

## House-table application

Spot-checked the recurring fixed renderings against `conventions.md` at every occurrence in this part: δῖος
(extended to δῖοι Ἀχαιοί and ἅλα δῖαν, consistent with the precedent of extending fixed epithets to new
referents, e.g. odyssey-008's ἐϋκνήμιδες/κάρη κομόωντας); ξανθὸς Μενέλαος; ἐυκνήμιδες Ἀχαιοί; νῆας ἐίσας;
Ποσειδάωνι (without ἄνακτι, correctly noted as such since the line omits the title); δαΐφρων; ἀμύμων; and the
reply-formula patterns. All are applied consistently and correctly. `new-renderings.md`'s remaining rows
(ἀρήιος, ἀτάσθαλα, λυγρός, θεσπέσιος of a sound, the Ἀτρεΐδης/Ἀτρεΐδην pair, Τυδέος υἱός/Τυδεΐδης, ἱππόδαμος of
Diomedes, μεγάθυμος, φαίδιμος, ἀγλαός, ποιμένι λαῶν) are all genuine, defensible translation choices with
avoid-lists in the house style; only the six plain-name rows were pruned (above).

## Considered and refused

- **ἀπηύρα (3.192), "an unaugmented aorist."** Looked wrong on first glance (the η resembles an augment), but
  LSJ specifically marks ἀπηύρα as never augmented: the η belongs to the verb's own long-grade stem, not to an
  augment prefix. This is a well-known exception, distinct from the four genuine augment errors above. Kept.
- **3.109, "Antilochus… died at Troy defending his father from a Trojan spear."** A background mythological
  fact not stated in this part's own text (it comes from the Aethiopis, not the Odyssey). Kept, on the same
  footing as this part's own similarly-scoped notes on Idomeneus and Philoctetes, and past parts' precedent for
  broad, uncontroversial thematic/background framing (odyssey-004's log).
- **3.167, "the patronymic Τυδεΐδης names him directly at 181."** Slightly loose phrasing (a patronymic is not
  the same as a real name), but line 181 does give both the patronymic Τυδεΐδεω and the real name Διομήδεος
  together, so the underlying claim is true. Not changed.
- **3.130–131, unflagged comma-cut.** Checked and found correctly placed (see the flagged-items ruling above);
  no change needed.
- **General smoothness check on `i`.** Read every `i` against its `l` for suspiciously idiomatic phrasing that
  might have been recalled rather than built from the Greek. Nothing stood out as drifting from a banned or
  copyrighted rendering; all avoid-lists in the house table are respected.

## Pass 2 — `gloss.json`

Checked after the Glosser's run. 271 top-level (non-broadening) entries, cross-checked by script against
`novel-forms.json`: the key sets match exactly, no missing forms, no extra forms, no line-pinned duplicates.
11 `__broaden__` entries, each checked against the actual shipped `/home/user/Lectorium/odyssey-glossary.json`
(read via its `glossary` key, not from memory). Entry shape (under 230 characters for every novel entry,
typographic ’ throughout, no backticks, `lemma — meaning; parse` format) verified by script; all pass.

**Findings fixed: 6 major (augment mislabels), 1 moderate.**

### Novel entries corrected

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| ἐνίκα (3.121) | major | Called "impf. 3 sg., unaugmented". νικάω's root νικ- is consonant-initial, so the visible ἐ- prefix on ἐνίκα can only be the augment; the unaugmented form would be bare νίκα. | Relabelled "augmented (ἐ- + νίκα; unaugmented would be νίκα)". |
| ἔθεμεν (3.179) | major | Called "aor. 1 pl., unaugmented". τίθημι's aorist stem θε- is consonant-initial (the aorist does not inherit the present's ι-reduplication), so ἔθεμεν's ἐ- is the augment; unaugmented is θέμεν. | Relabelled "augmented... unaugmented θέμεν". |
| ἔθηκε (3.136) | major | Same error as ἔθεμεν, and a plain contradiction of the shipped, correctly-labelled house example in `conventions.md` itself (ἔπαθεν given there as the *augmented* counterpart to unaugmented πάθεν — exactly the pattern ἔθηκε/θῆκε follows). | Relabelled "augmented... unaugmented θῆκε". |
| ἔκιχεν (3.169) | major | Called "unaugmented ἔκιχεν (= Attic ἔκιχε)". κιχάνω's root κιχ- is consonant-initial, so ἐ- is the augment; the note also conflated the movable -ν (an unrelated orthographic feature, kept in Attic too) with augment status. | Relabelled "augmented... unaugmented κίχεν", with the movable-ν point kept but separated from the augment claim. |
| ἔμελλεν (3.146) | major | Called "impf. 3 sg., unaugmented". μέλλω's root μελλ- is consonant-initial; ἔμελλεν is the ordinary, regularly augmented imperfect. | Relabelled "augmented... unaugmented μέλλε(ν)". |
| ἥνδανε (3.150) | major | Called "impf. 3 sg., unaugmented (beside the augmented ἑήνδανε...)". This is backwards: ἥνδανε (η-) is itself augmented, the contracted counterpart of the uncontracted ἑήνδανε (ἑ-) — both descend from the augment applied to the digamma-initial root (cf. Iliad 1.24's ἥνδανε, already identified as augmented in this part's Pass-1 review at 3.141/ἑήνδανε). The genuinely unaugmented form is ἄνδανε, not attested in this part. | Relabelled "augmented (η- from the root's original digamma, contracted...); unaugmented ἄνδανε". The parallel ἑήνδανε entry's own cross-reference to "unaugmented ἥνδανε" was fixed to match. |
| ἐγχεσιμώρους (3.188) | moderate | Gave only one etymology (ἔγχος + root of μέμονα) as if settled, for a word whose second element is genuinely disputed between μῶρος and μέμονα (one of the items the Glosser itself flagged as tricky). | Reworded to state the dispute explicitly: "second element disputed: linked to μῶρος 'eager, mad' or to μέμονα 'be eager'". |

Every other augment claim in the file was checked against its actual line in `units.json` and found correct:
βούλετο, βῆμεν, γίγνωσκον, δεῖξε, πάθομεν, πάθον, φεῦγε, φεῦγον, ἄγ’, ἀπηύρα (all genuinely unaugmented, no
visible prefix on their consonant-initial roots, or — for ἀπηύρα — the standard LSJ "never augmented"
exception already confirmed in Pass 1); κατέκταθεν and ᾐτέομεν (both correctly "augmented", carrying over
the Pass-1 fixes to the same two forms). ἐρητύοντο is correctly "unaugmented" on different grounds (its own
root is vowel-initial ἐρη-, and the form keeps the short ε rather than lengthening to η under augment, unlike
ἥνδανε/ἑήνδανε where the vowel comes from a lost digamma rather than the root itself).

### Disputed-meaning items checked (the Glosser's flagged list)

- **δαΐφρων** (δαΐφρονα, 3.109): states the root dispute (δαῆναι 'learn' vs δάϊς 'battle') — correct, matches
  `conventions.md`'s own house-table note on this epithet. Kept.
- **ἐγχεσιμώρους**: fixed, above.
- **ἐίσας** (νηῦς ἐίση, 3.180): "sense disputed, perhaps 'equal on both sides'" — correct, matches the house
  table's own "sense uncertain" flag on this word. Kept.
- **ἦρα** (3.164): hedges the gender ("neut./fem.") and notes it occurs only in the fixed idiom ἦρα φέρειν —
  a fair reflection of this word's genuinely unclear declension. Kept.
- **ὀβριμοπάτρης** (3.135): no dispute stated, and none is needed — this is a transparent compound (ὄβριμος +
  πατήρ), not a genuinely disputed word; nothing in `conventions.md`'s house-table row for it flags a dispute
  either. Kept as is.

### Broadenings: all 11 genuine and correctly formed

| Key | Old text preserved verbatim? | New reading needed and correct? |
|---|---|---|
| ὡς | Yes (checked byte-for-byte against the shipped glossary) | Yes — two new senses used in this part: a purpose clause (3.145, ὡς … ἐξακέσαιτο) and an exclamatory "how (good) …" (3.196, ὡς ἀγαθὸν … λιπέσθαι), neither covered by the shipped wish-only entry. |
| ὅτ’ | Yes | Yes — the shipped entry covers only ὅτε + subj. in a general clause; this part also uses ὅτ’ + indicative for a single definite past event (3.180). |
| θεὸς | Yes | Yes — the shipped entry covers only the predicate use ("as a god"); this part also uses it as a plain, unnamed subject (3.131, θεὸς δ’ ἐκέδασσεν Ἀχαιούς). |
| ἔπι | Yes | Yes — two new uses: postpositive + genitive of direction (3.171, νήσου ἔπι Ψυρίης) and bare adverbial intensifier (3.161, ἔπι δεύτερον αὖτις), beyond the shipped dative-with-anastrophe sense. |
| κατὰ | Yes | Yes — a "in quest of, after" + accusative sense (3.106, κατὰ ληίδα) not in the shipped entry. |
| μετ’ | Yes | Yes — a + dative "between, among" sense (3.136, μετ’ ἀμφοτέροισιν) not in the shipped entry (which covers only + accusative and tmesis). |
| περὶ | Yes | Yes — a + accusative "around" of place (3.107, περὶ ἄστυ) not in the shipped entry. |
| παρ’ | Yes | Yes — a + accusative "past, along" of motion (3.172, παρ’ Μίμαντα) not in the shipped entry (dative and genitive only). |
| ἀμφ’ | Yes | Yes — a + accusative "around, with" sense (3.163, ἀμφ’ Ὀδυσῆα) not in the shipped entry (dative only). |
| ὅπως | Yes | Yes — a + optative indirect-deliberative use in secondary sequence (3.129, ὅπως … γένοιτο) not in the shipped entry (subjunctive/future indicative only). |
| πρίν | Yes | Yes — an independent πρίν κε + optative potential clause (3.117, πρίν κεν … ἵκοιο) not in the shipped entry (infinitive and subjunctive temporal-clause uses only). |

All 11 check out: genuine new uses, correctly analysed, and none of them could have been folded into the
shipped entry's existing senses. None was found unnecessary or removed.

### Considered and refused

- **ἵστασαν (3.182), "impf. 3 pl., unaugmented."** Looked at closely because ἵστημι is a reduplicated -μι
  present (ι-στη-): its imperfect does not add a separately visible augment marker distinct from that
  reduplication vowel, the same kind of structural ambiguity as odyssey-009's note on ἷξον ("an augment would
  only lengthen an ι that is long already"). Calling it "unaugmented" is a defensible loose description (no
  extra prefix is shown either way) rather than a clear misstatement like the six fixed above, where the
  augment is plainly visible on a consonant-initial root. Left as is.
- **ἐλαύνομεν / ἕλκομεν / ῥάπτομεν, "pres.-stem form with past narrative force."** These are unaugmented
  imperfects that are orthographically identical to the present tense (a genuine Homeric ambiguity for
  thematic verbs in the 1st/2nd/3rd plural). The phrasing accurately describes this rather than overclaiming a
  tense the spelling cannot itself prove. Kept.
- **ἀπόλοντο (3.185), no augment comment.** The form is in fact unaugmented (ὀλ- is vowel-initial; augmented
  would lengthen to ἀπώλοντο), but the entry simply doesn't comment on it either way, which is allowed —
  `conventions.md` requires flagging Homeric features on first occurrence, not on every single form. No claim
  is made, so there is nothing to fix.

## Open items

None written to `QUESTIONS.md`. Everything found had a clear resolution from the source archive, LSJ, or the
project's own established conventions.

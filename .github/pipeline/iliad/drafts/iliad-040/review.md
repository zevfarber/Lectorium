# Review — iliad-040 (Iliad 6.440–529), reviewer passes 1 and 2 (units)

No modern translation was opened or recalled. `units.json` was edited in place by script; every `t` was asserted unchanged before writing. Original kept outside the repository. Same-Greek check run by script against all published Iliad units and all published Odyssey units (key `letters_only(t)`, as the validator does): 6.447 (iliad-022, odyssey-073), 6.448–449 (iliad-022) and 6.490–492a (odyssey-004) all match `l` and `i` exactly. No `gloss.json` exists yet, so no glossary parse was checked in this pass (the second pass of the glossed stage reads it).

Severity: high = sense wrong or reversed; medium = a note or layer states something false or misaligned; low = wording, consistency, tidiness.

## Changes (line · field · severity · what was wrong · what was done)

| line | field | sev | wrong | done |
|---|---|---|---|---|
| 450 (unit 6) and 454 (unit 7) | `i` | medium | `ὅσσον σεῦ` (the first words of unit 7) was rendered at the end of unit 6 as "as the thought of you does", an invented phrase, and unit 7's `i` began at "when", so its own Greek had no English | unit 6 `i` now ends "...beneath ill-disposed men,"; unit 7 `i` now begins "as it does for you, when one of the bronze-shirted Achaeans..." |
| 518 | `i` | high | "and have I not come as was fitting, as you bade me?" is a negative question that expects "you have", the opposite of `οὐδ’ ἦλθον ἐναίσιμον ὡς ἐκέλευες;` (Paris fears he did not come in good time) | "and did I fail to come as was fitting, as you bade me?" |
| 518 | `n` | low | "a guess from the other place it is used" named no place; nothing said that `οὐδ’ ἦλθον` is still inside the question | names Odyssey 14.147 (odyssey-067); adds one clause that `οὐδ’ ἦλθον` stays inside the question |
| 460 | `n` | medium | `Τρώων ἱπποδάμων` called "a genitive of the group he led": it is the partitive genitive after `ἀριστεύεσκε` ("best among"); nothing says Hector led them | corrected |
| 462 (second unit) | `n` | medium | "new because it adds to the sorrow of her father and brothers": a reason the lines do not give | "fresh grief for her because she will have no such husband to ward off slavery" |
| 466 | `n` | low | `οὗ` called "the genitive of the reflexive possessive"; it is the possessive `ὅς` in the genitive agreeing with `παιδός` (as the note itself says of `ὃν φίλον υἱόν` at 474) | corrected |
| 480 | `i` | low | "carry home" supplied "home", which the Greek lacks | "carry the bloody spoils" |
| 486 | `n` | low | "(the literal layer keeps 'strange woman')" is empty (both layers say it); the table row for `δαιμόνιε` requires the uncertainty of force to be stated | now says the force is uncertain (gentle or reproving) and "strange woman" keeps the word without choosing |
| 487 | `l` | low | "send-forth" with a hyphen, against the table's 5.190 row "send forth" | "will send forth" |
| 488 | `n` | low | `κακός` and `ἐσθλός` called "the words for men in battle" in a line about all men's birth | "'base' and 'good', the coward and the brave man" |
| 521 | `n` | low | `δαιμόνι’` given no mention of the uncertain force, unlike the table's `δαιμόνιε` rule | one clause added: force not certain, gentle here though it leads to a reproach |
| 523 (first, `μεθιεῖς`) | `n` | low | gloss "you give way" while `i` says "you slack off" | note now says "you slack off" |
| 526 (second) | `n` | low | the dative `θεοῖς` was not attached to any verb; the `l` order ("grant to the gods ... to set up") can mislead | note says `θεοῖς` is taken with `στήσασθαι` |

new-renderings.md edited (records, not units): `ἀμφίπολος` row (decision below); `ἀλυσκάζω` avoided-column corrected (it claimed "dodge" was turned down, but the Iliad table's 5.253 row ships "by dodging"; the row now says why "shun" is kept); `χυτὴ γαῖα` source corrected to Odyssey 3.258 (odyssey-011), the draft had "11.258"; `προϊάψει` `l` "send forth"; `ἱστόν` and `ἠλέκτωρ` and `ἠθεῖε` rows made explicit.

Counts: 1 high, 3 medium, 9 low in units.json (13 findings, 14 field edits); 4 low record corrections in new-renderings.md.

## Points the drafter handed over

- **ἀμφίπολος.** Published Iliad: "handmaid(s)" at 3.143 (iliad-017), 3.422 (iliad-020), 6.372 and 6.399 (iliad-039); the table's 3.143, 3.422 and 6.389 rows say so; the Odyssey ships "handmaid" for the singular (odyssey-002, -004, -015). Only the Odyssey's plural table row and iliad-038 (6.286, 6.323) say "attendants". House word for the Iliad: "handmaid(s)". Units 28 (forced by odyssey-004) and 32 (6.499) already use it; no unit change. iliad-038 is published and cannot be edited from here: flagged for the lead (a later cleanup or QUESTIONS.md entry), not changed.
- **ἠλέκτωρ** (6.513). Kept "like the sun". The word occurs nowhere else in published Iliad parts; the Odyssey's ἠλέκτρου / ἠλέκτροισιν are a different word ("amber"). The unit's note already says "the usual explanation, followed here, is 'the sun', but that is not certain", which meets the unknown-meaning rule.
- **ἠθεῖε** (6.518). Kept "Honoured one" (`l`) / "My honoured one" (`i`), identical to odyssey-067 (14.147) and the table row (sense not known); the note says so.
- **ἱστόν web/loom.** Kept both, because both are shipped: "web" for ἱστὸν ὑφαίνω (table 3.125, iliad-017), "loom" for ἱστόν as the thing tended (iliad-001, odyssey-004 whose English unit 28 must repeat). Unit 8's note says it is the web being woven; unit 28's note says loom.
- **Line 478** (hand scan, `ὧδε βίην τ’ ἀγαθόν, καὶ Ἰλίου ἶφι ἀνάσσειν`). 16 syllables: ὧ-δε-βί | ην τ’ ἀ-γα | θὸν καὶ Ἰ | λί-ου | ἶ-φι ἀ | νάσ-σειν; masculine caesura in the third foot after θόν. Both scansions the scanner finds differ only in the free quantity of the first ι of Ἰλίου; each is a complete hexameter. The licences are the ordinary ones (correption of καὶ before Ἰ; -ου kept long before ἶφι, which began with a digamma). I find no irregularity in the transmitted line, so no sentence was added to the note (runbook: only where the irregularity is real). Risk accepted: the first ι of βίην is scanned short, which the scanner treats as an open-syllable choice.
- **Same Greek, same English.** Unit 4 (447), unit 5 (448–449; ends in a comma in `l` and `i` though this part's Greek ends with a full stop, kept per the validator rule and said in the note), unit 28 (490–492a): all identical to the published English. Nothing to alter; the note of unit 5 states the comma/stop difference.

## Findings considered and refused

- Unit 2 `ἀλυσκάζω` "shun" vs the Iliad 5.253 "dodging": kept "shun" (the Odyssey table is binding; 17.581). Changing 5.253 is outside this part.
- Unit 2 note "frequentative of ἀλύσκω": same wording as the Odyssey table's 17.581 row; kept.
- Unit 2 `αἰδέομαι` "ashamed before": table rows 4.402/5.530 use "respect" and list "ashamed before" as the other sense; the context (Trojan women's opinion) is plainly shame and the note says so. Kept.
- Unit 24 `νοήσας` "as he looked at her" (`l` "having noticed"): near enough, the note gives "having noticed". Kept.
- Unit 13 `βοῆς` rendered "cries" (plural) against `l` "outcry": idiomatic, no sense change. Kept.
- Unit 33 `i` opens "So they lamented": the "So" is the drafter's smoothing of `αἳ μὲν`; harmless. Kept.
- Unit 48 `τὰ δ’ ὄπισθεν ἀρεσσόμεθ’` "what is amiss": the table's 4.362 row is "put right"; the object is a reasonable reading and the note says the reproaches are meant. Kept.
- Unit 12 `ἀμύνειν` "infinitive of purpose": defensible (dependent infinitive after `χήτεϊ`); kept.
- Unit 10 nested ‘ ’ and `mark` "The onlooker says": correct for a speech inside a speech; the count of “ and ” is 5 and 5 in both layers, each speech opening on the unit with a `mark` and closing on its last unit (lines 464, 480, 492, 518, 526).
- Speech continuity: iliad-039's last unit (6.438–439) closes Andromache's speech with ”; unit 0 (440) is narration and carries no mark; correct.
- Paragraph marks `p` fall on 440, 466, 482, 494, 503, 520, exactly the packet's ¶ lines.
- Unit 28 note "Odyssey 1.356–358" and unit 32 note "also stands at 6.370": checked against odyssey-004 (ln 356) and iliad-039 (ln 370); true.
- Greek words quoted in every note were checked by script against the unit's `t`; no misspelling or absent word found. Note lengths all within 25–110 words; quotation counts equal in `l` and `i`.

## Second sweep

Re-read every unit's Greek → `l` → `i` → note after the edits above; no further changes. The validator cannot run yet (part not built).

## Pass 2 (gloss)

No modern translation was opened or recalled. Every one of the 135 novel entries and the 28 `__broaden__` entries was checked against the line (case, number, tense, mood, voice, lemma, Attic equivalent, homographs); every known form in the part was checked against its existing entry for coverage; mechanical checks run by script: every novel entry under 230 characters, only the typographic ’, no backtick, no line number, no "here"; every `__broaden__` entry begins with the old entry whole. Words in the part: all covered by known or novel entries. `gloss.json` was edited in place by script; in `units.json` no `t` was touched (asserted).

### Changes to gloss.json (form · severity · what was wrong · what was done)

| form | sev | wrong | done |
|---|---|---|---|
| νέον (broaden, new) | medium | known entry gives only the adverbial "lately, just now"; 462 νέον … ἄλγος is the adjective, neut. nom. sg., "new" | added " · also neut. nom. sg., agreeing with ἄλγος: ’new’" |
| σ (broaden, new) | medium | known entry parses σ’ only as elided σε; at 490 τὰ σ’ αὐτῆς ἔργα, σ’ is σά, neut. acc. pl. of σός | added the σός reading |
| τινά (broaden, new) | low | known entry has only "a (man)"; 488 οὔ τινά is "no one" | added the negative reading |
| ἄλλοι (broaden, new) | low | known entry nom. only; 476 Ζεῦ ἄλλοι τε θεοί is vocative | added the vocative reading |
| ἄκρης (broaden) | medium | see "Flagged calls" below | adjective reading kept first (it is the reading of the note and of `i`, and of the published περγάμῳ entry); noun reading added in a closing clause |
| πατρός | medium | "’for (my) father’" is wrong for 445 πατρός τε μέγα κλέος (possessive genitive, "my father’s glory") | "’(my) father’s’ (πατρός τε μέγα κλέος …)" |
| ἀκούω | low | "and gen. of the person" is false of the line (αἴσχε’ is the acc., σέθεν hangs on ὑπέρ) | "+ acc. of what is heard" |
| ἀλυσκάζω | low | "+ gen." : πολέμοιο is governed by νόσφιν | removed |
| ἐϋρρεῖος | low | Attic equivalent given as "εὐρρέους" (not a form); Attic gen. is εὐρρεοῦς | corrected |
| ἠλέκτωρ | low | meaning stated flatly; the unit note itself says it is not certain (unknown-meaning rule) | "the sun (the usual explanation; meaning not certain, perhaps ’the beaming one’)" |
| ἠθεῖ | low | no statement of uncertainty, unlike the Odyssey entry ἠθεῖον and the unit note | "(exact sense not known)" |
| ἔφαντο | low | only "they supposed", while `l` says "did they say"; the Odyssey entry carries both | "’they said, they supposed (he would …)’" |
| προϊάψει | low | "’will fling’" against the house `l` "send forth" | "’will send forth (to Hades)’" |
| μάθον | low | no Attic equivalent for an unaugmented aorist | "unaugmented (= ἔμαθον)" |
| ἀγλαΐηφι | low | quote "’in his beauty’" against `i` "splendour" | "’in (his) splendour’" |

### Changes to units.json (no `t` touched)

| line | field | sev | wrong | done |
|---|---|---|---|---|
| 512 | `l` | low | `l` "down from the height of Pergamus" took ἄκρης as a noun while the note ("the high Pergamus") and `i` ("high Pergamus") take it as an adjective: one unit, two readings | `l` now "down from high Pergamus" |
| 521 | `n` | low | "ἀτιμήσειε is the aorist optative of ἀτιμάζω": the form is Homeric, from ἀτιμάω (as in the glossary and the Odyssey entries) | "of ἀτιμάω (Attic ἀτιμάζω)" |

### Flagged calls of the glosser

- **ἄκρης (512).** κατὰ Περγάμου ἄκρης admits two parses: adjective ἄκρος agreeing with the feminine Πέργαμος ("down from high Pergamos"), or noun ἄκρη "height" with Περγάμου dependent (the Odyssey glossary has the noun ἄκρη, "top, peak"). The published entry περγάμῳ already treats Πέργαμος as feminine "with ἱερῇ, ἄκρῃ" (adjective), the unit note and `i` say "high", so the adjective stays first; the noun is recorded as the alternative so the entry is true on either reading. Both are the same gen. sg. fem.
- **ἀτιμήσειε.** Lemma ἀτιμάω with "(Attic ἀτιμάζω)" is right: it agrees with the Odyssey entries ἀτιμῆσαι, ἀτιμήσουσι, ἀτιμήσασ’. Parse aor. opt. 3 sg. act. with οὐκ ἄν (potential) is right. Kept.

### Considered and refused

- ἀνάσσειν, ὑπ, ὑπὲρ, ὃ, τίς etc. in `__broaden__`: every new reading checked against its line and found true; kept.
- κατά (known): entry already covers tmesis, "in" with the accusative of respect (κατὰ θυμόν, so also κατὰ φρένα) and "+ acc./gen."; not broadened. Likewise κε, κέ, κέν, κεν, ἄν, ὥς, μή, εἴη, ἐϋζώνοιο, πάντα (has the nom. reading), κάρη, τι, τις: existing entries cover the use.
- γόον (broaden, γοάω impf.) and γόον noun at 497: both parses true, kept as homographs.
- ἐβεβήκει, δήθυνεν, κύσε, πῆλέ, ἔτετμεν, ἐνῶρσεν, θείῃ, θαλερὸν: checked, correct as written.
- ἐϋζώνοιο mentions γυναικός though here it goes with τιθήνης: the parse (fem. gen. sg.) is general and true; left.
- 484 ἐλέησε "pitied her" (object supplied): idiomatic, kept.

### Counts (pass 2)

gloss.json: 0 high, 4 medium (νέον, σ’, πατρός, ἄκρης), 11 low. units.json: 0 high, 0 medium, 2 low.

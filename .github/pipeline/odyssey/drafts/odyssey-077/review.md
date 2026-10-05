# odyssey-077 (16.1–111) — review, pass one (translation)

Reviewer pass one. Read: runbook §2, conventions.md (whole, house table to its last row), packet.md, new-renderings.md, units.json, drafts/odyssey-001/units.json, the last unit of odyssey-076 (ends 15.557 in the narrator's voice, no speech open, so 16.1 opens clean). No modern translation opened. `t` untouched (checked by comparing every unit's `t` before and after). `gloss.json` not read: pass two.

Checks run: every label in every note against the line; Greek to `l` word by word; `l` against `i`; remembered English; quotation marks; cross-references (every "line N" in every note); unit boundaries and "begins/ends in the middle of line N" claims; `p`/¶ (lines 1, 8, 11, 23, 36, 44, 46, 57, 60, 68 all correct); `ln`; `l` line counts; no `\n` in `i`; note length band; the validator's repeated-unit rule (step 6) emulated in a script against all 76 published parts (build_odyssey.py and validate_odyssey.py not run).

Scansion: the packet flags none. Hand check of all 110 lines with scan_hexameter: every line fits, no UNRESOLVED/AMBIGUOUS flag. Five lines (43, 53, 62, 63, 73) carry the scanner's remark "spondaic fifth", a regular licence, not an irregularity, so no note sentence was added.

Severity scale used: **error** = would fail the gate or misreads the Greek; **major** = a grammatical label or claim in a note that is false; **moderate** = departs from the house table, from shipped precedent, or is remembered English; **minor** = wording, clarity, small omission.

## Changes made (line · field · severity · what was wrong · what was done)

| # | Line | Field | Sev. | Wrong | Done |
|---|---|---|---|---|---|
| 1 | 16.37 | l, i, n | error | Same Greek as the published unit at 11.181 (odyssey-052); validator step 6 requires byte-identical English, and 052 carries ‘ (the words are a speech inside a speech there). The draft had “, so validate would FAIL. | l and i now read exactly as 052 (‘Yes, …). Note gets one sentence saying the English keeps its single mark and the speech closes with the matching mark at 39. (See "Decisions".) |
| 2 | 16.38–39 | l, i | minor | Closing ” would not pair with the ‘ forced on 16.37. | Closing mark changed to ’ so Eumaeus' speech is a matched pair. Quote count in the part is now 8 “ / 8 ” in both layers (no WARN). The unit's Greek differs from 052's by the diaeresis (see d), so nothing forces its English. |
| 3 | 16.58 | l | error | Same Greek as the published unit at 1.172 (odyssey-002, line 172); published l is "Who did they declare themselves to be?", draft had "Who to be did they declare themselves?". Validator step 6 would FAIL. | l set to the published wording (i was already identical). |
| 4 | 16.57 | n | major | "ἵκετο … without augment": line 57 scans ὅδ’ ἵ–κε⏑το⏑ with ι long, and the shipped notes (033, 068) state that this lengthening is the augment. | Note now says the metre needs ι long and that lengthening is the augment. |
| 5 | 16.11 | n | major | "Telemachus, who is not named until line 20": he is named in line 4. | "named in line 4 and not again until line 20". |
| 6 | 16.12 | n | major | ταφών "an old verb found only in the aorist": the perfect τέθηπα belongs to it. | "an old verb whose other main form is the perfect τέθηπα". |
| 7 | 16.23 | n | major | ἐφάμην "an aorist of φημί": it is the imperfect middle (shipped notes 017, 018 and the glossary entry say so). | "the imperfect middle of φημί". |
| 8 | 16.28 | n | major | ἐσορᾶν "the uncontracted infinitive": ἐσορᾶν is contracted; only the preverb has the epic ἐσ-. | "the infinitive of εἰσοράω … in its epic spelling with ἐσ-". |
| 9 | 16.31–32 | n | major | "short-vowel subjunctives ἴδω and ἀκούσω": both have the ordinary long vowel. | "the subjunctives ἴδω and ἀκούσω". |
| 10 | 16.43 | n | major | φώνησέν τε "enclitic τε, which moves the accent back": the enclitic adds a second accent on the last syllable of a proparoxytone. | Wording corrected (also names the movable ν). |
| 11 | 16.46–47 | n | major | "l and i carry a comma" after συβώτης: neither does. | "l and i run on without a stop". |
| 12 | 16.49 | n | major | τοῖσιν "the two guests": Telemachus is the master's son, not a guest. | "Odysseus and Telemachus, now seated". |
| 13 | 16.23–24 | i | moderate | "I never thought to see you again, once you had gone off by ship to Pylos" is too near a modern translation's sentence to trust as built from the case relations. | Rebuilt: "I did not think I should see you again, since you had gone off by ship to Pylos." (ἐπεί is "since" in l). |
| 14 | 16.17–19 | l, i, n | moderate | τηλύγετος was given "only, cherished", but 4.11 (odyssey-014) shipped "late-born" for the same word, with a note that the meaning is disputed, and the glossary entry is "late-born (or … darling)". New-renderings row therefore contradicts the first ratified rendering. | l "only, late-born"; i "his only, late-born child"; note rewritten (usual gloss "late-born", as at 4.11; other guesses stated). **new-renderings.md row for τηλύγετος should be dropped**, not copied into the table (014's own row records the choice). |
| 15 | 16.91 | l, n | moderate | ὦ φίλ’ rendered "My friend" in l; table row ὦ φίλε / ὦ φίλ’ (14.115, 14.149) is l "O friend", i "My friend". | l "O friend"; note reworded. i was already right. |
| 16 | 16.75 | l, n | moderate | l "the talk of the land" and i "the talk of the people" disagreed; the identical phrase δήμοιό τε φῆμιν is shipped at 15.468 (odyssey-076) as "the people's talk" / "the talk of the people". | l "the people’s talk"; note says "the community, the people of the land". |
| 17 | 16.1–3 | i, n | minor | "the swine they had gathered" makes the men the gatherers; ἀγρομένοισι is a middle participle, "gathered together". The word had no note. | i "the gathered swine"; note names the form (glossary already has it as aor. mid. part.). |
| 18 | 16.4 | n | minor | προσιόντα "agreeing with Τηλέμαχον understood": Telemachus is printed in the line; the unexpressed word is the object of ὕλαον. | Reworded. |
| 19 | 16.5–6 | i | minor | "and then came the sound of feet": "then" adds a sequence τε … τε does not give. | "and there came the sound of feet". |
| 20 | 16.44 | i, n | minor | i dropped καί of καὶ ἄλλοθι; note called δήομεν a plain "future" while the glossary entry (019) has it as a short-vowel form with future sense. | i "elsewhere too"; note "a form of the old verb δήω … with future sense". |
| 21 | 16.60 | n | minor | προσέφης "aorist": shipped notes 002/014 call the form the imperfect of πρόσφημι. | "imperfect (πρόσφημι)". |
| 22 | 16.78 | n | minor | ἀλλ’ ἦ τοι glossed "but still" while l reads "But truly". | Note now "but truly". |
| 23 | 16.105, 108 | n | minor | Units end at commas inside a seven-line sentence without saying why (the pattern in other parts). | One clause each. |

Counts: error 2, major 9, moderate 4, minor 8 (23 findings, 32 field edits).

## Decisions on the drafter's special points

**(a) Line 46, Murray's full stop after συβώτης.** Kept as drafted. The two halves are one sentence (τῷ δὲ συβώτης … χεῦεν), so cutting at the printed stop would leave a unit of a subject with no verb. Build/validate accept it (build checks only the last character of a unit; validate step 1 is a concat check). `t` keeps Murray's stop; the note says so. One false clause in that note was fixed (#11).

**(b) Lines 108–111, ῥυστάζοντας / ἔδοντας.** Reading confirmed. Both are accusative plural masculine active participles, so neither can agree with δμῳάς … γυναῖκας (fem.) or with διαφυσσόμενον (neut. passive); their subject, the suitors, is understood, and `l` supplies it in brackets, `i` plainly. στυφελιζομένους (middle/passive) agrees with ξείνους. The note is right.

**(c) Plural verbs in Odysseus' speech.** True, but they stand at **92 (καταδάπτετ’) and 93 (φατε)**, not 91 and 95: 91 has ἐστίν (sg.), 95 has εἰπέ and ὑποδάμνασαι (both sg.) and ἐχθαίρουσ’ is 3 pl. with the noun λαοί. The note's statement (second-person plural beside singular φίλ’ and σέθεν; Greek does not say whether Eumaeus is meant) is true and enough. No change.

**(d) ὀϊζυραὶ vs ὀιζυραὶ.** Does not matter. Murray prints ὀιζυραί at 11.182 and ὀϊζυραί at 16.38 (source file checked: U+03B9 vs U+03CA). validate step 6 keys on `letters_only(t)`, and WORD includes U+03CA as a letter, so the two units get different keys and the rule never fires on 16.38–39. There is no failure to avoid and no `t` to touch. The English was kept word-for-word with 052's anyway. (The glossary already has the key ὀϊζυραὶ; the glosser need only check that it covers the use.)

**(e) ‘ vs “ in the repeated 052 units.** Emulated step 6 against all published parts: two units of this part repeat a published unit and differ from it: 16.37 (quote mark) and 16.58 (word order; #3). 16.37 is the real conflict: the house rule says “ on a speech's first unit, but step 6 demands byte-identity with 052, which has ‘. The gate wins, as in the odyssey-014 run (LOG: repeated lines "corrected to the exact shipped wording, byte for byte, with notes added explaining the … quotation-mark mismatches"). Done as #1 and #2: the speech opens with ‘ at 37 and closes with ’ at 39, matched, with a note sentence. **If the lead prefers “ ” here, the one-line fix is to make validate step 6 compare after mapping ‘’ to “”**; I did not touch the validator.

## Findings considered and refused

- **Unit 16.46–47 split at Murray's stop** — refused, see (a).
- **16.91 "second-person plural" claim** — true; kept (c).
- **16.64 δαίμων "some power" in l** (table row 6.172 has l "a power") — kept: the table's own later rows (11.61, 12.295) use "some power" in `l`, and shipped 026 varies.
- **16.14 i "beautiful eyes" beside l "fine eyes"** — kept: rows 11.271 and 15.332 fix l "fine", i "beautiful" for καλός of a person; the eyes are the person's.
- **16.49 l "set beside the swineherd"** (reads as if the swineherd were beside something) — kept: `l` follows Greek order and the sentence is resolved in `i`.
- **16.86 note "ἀτασθαλίαι at the start of the poem"** — kept: a true cross-reference (1.7), not a claim the part cannot show.
- **16.8 note "ἢ καί ‘or even’" beside l "or else"** — kept; both reflect καί.
- **16.65 i "even if a great quarrel has arisen"** for the aorist subjunctive ὄρηται — acceptable English for the general condition.
- **16.65 ὑποδάμνασαι "second singular middle"** against 011's "present passive" — same form, same person; both labels true of a mediopassive.
- **16.65 (95–96) l without the comma after "Tell me"** that the published l has — Murray prints no comma at 16.95 (11.214 has one), so the English follows this Greek; the rule is "as far as your sentence allows".
- **16.65 "ἐστίν" etc.** no other label problems found.
- **16.57–58 and 16.59 ἄττα / τοι** — "father" row accepted; no kinship claimed; note says so.
- **16.2 ἄριστον "breakfast", 16.80 ξίφος ἄμφηκες, 16.69 ἔπος θυμαλγές, 16.102 ἀλλότριος φώς, 16.28 ἐπιδημεύω, 16.108–109 στυφελίζω / ῥυστάζω** — new-renderings accepted as drafted, with no conflict found in the shipped parts or the table. Only τηλύγετος was changed (#14).
- **16.47 i drops αὖ of νῦν αὖ** — a discourse particle; l keeps "again". Kept.
- **16.101** — Murray omits it; units 66 and 67 say so correctly (numbering 100 then 102).

## For the lead

1. Drop the τηλύγετος row from new-renderings.md before copying rows into the table (units now use the shipped "late-born").
2. 16.37 and 16.38–39 now carry single marks, see (e); the validator should print no quotation WARN (8/8).
3. Pass two (gloss.json) still to do. As of this review the published glossary has no entry for ἐσορᾶν, ταφὼν, ἐπιδημεύεις, κτύπος, τηλύγετον or ἄττα; ἀγρομένοισι, δήομεν, ἐφάμην and ὀϊζυραὶ are already there.

# Pass two (gloss.json, and a re-check of units.json)

Re-check of units.json after pass one: every unit's `t` unchanged, quotes 8/8 in both layers, repeated units identical to the published English (16.37, 16.58 included), `l` line counts and note bands fine. One further note edit: 16.25 τέρψομαι is "a future or a short-vowel subjunctive" (the old note called it a plain subjunctive; the gloss now says the same). new-renderings.md: τηλύγετος row removed, as advised.

gloss.json checked: all 112 new entries and 17 `__broaden__` entries against their lines; no missing forms, no redefinitions, no form outside the part, all under 230 characters, typographic ’ only. Every parse was right except the following.

| Form | Sev. | Wrong | Done |
|---|---|---|---|
| τηλύγετον | moderate | "only and dearly loved" disagreed with the units and with the existing τηλύγετος entry | "late-born, or on another view tenderly loved (meaning disputed)" |
| σαίνοντάς, ἔκπεμψάν | minor | "accent thrown back" (the enclitic adds a second accent) | reworded |
| παρενήνεεν | minor | lemma παρανέω is not the verb (reduplicated νηνέω) | lemma παρανηνέω, stem noted |
| τέρψομαι | minor | "fut." only; after ὄφρα it may be a short-vowel subjunctive | both stated |
| ἐνευναίων | minor | lemma given as certain | marked rare, sense from the formation |
| περί (broadened) | minor | "preverb in tmesis" stated as fact; the unit note says the force is uncertain | "adv. or preverb … exact force uncertain" |

Broadenings added (the known entry did not cover the use in this part): ἤματα (entry had only the accusative of time; here nominative subject), προτέρῃ (here with an understood ἡμέρῃ), κεῖται (of an object, not of the dead), ἕσσω (no preverb, double accusative). Checked and left: uncertain ἀΐδηλον ("destructive, baneful", debated; masc. acc. agreeing with ὅμιλον, correct), ἐνευναίων, παρενήνεεν, the ten other broadenings (γλυκερὸν, κακὸν, κάκ, νεῖκος, μή, μευ, οὐδόν, πόσιος, σταθμοῖσιν, τοὶ, χαλεπήνῃ, ἀεικέα, ἀτάσθαλον, ἄριστον, ἔπ, ὡς all verified; each keeps the old entry whole). Counts for pass two: moderate 1, minor 5, plus 4 added broadenings.

# iliad-058 (10.1–101) — reviewer's record

Two passes. Pass 1: `units.json` (notes, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, `mark`, `p`, cross-references, published-line reuse, house table). Pass 2: `gloss.json` against the lines, and `new-renderings.md` against what `units.json` ships. `t` was not touched; the units were checked against the packet (joined `t` equals the packet text up to line breaks). No scansion flags in the packet, so none scanned. Unit numbers below are 0-based positions in `sentences`; the first column is the line.

Totals: units and new-renderings — 1 high (unresolved, needs the caller), 5 medium, 7 low; gloss — 4 medium, 12 low, plus 12 new broadenings (low) and 1 refined.

## Unresolved, for the caller

| line · field | severity | what is wrong | what done |
|---|---|---|---|
| 10.85 · `t` of units 47 and 48 | **high** | The cut falls one word too early. Unit 47 `t` ends `…ἀκέων ἐπ’ ἔμ’` and unit 48 `t` begins `ἔρχεο· τίπτε δέ σε χρεώ;`. The ano teleia stands after ἔρχεο, so ἔρχεο belongs to unit 47, and `l`/`i`/`n` of both units already assume that (unit 47 `l` has “come at me”; unit 48 `l` has no “come”). As cut, unit 47 translates a word its `t` lacks and unit 48 has a word its `l` lacks. | Not fixed: `t` is off limits. The fix is to move `ἔρχεο·` from the start of unit 48 `t` to the end of unit 47 `t`, giving 47 `φθέγγεο, μηδ’ ἀκέων ἐπ’ ἔμ’ ἔρχεο·` and 48 `τίπτε δέ σε χρεώ;` (`ln` stays 85 for both). `l`, `i`, `n` need no change after that. |

## Pass 1 — changes to `units.json`

| line · field | severity | what was wrong | what done |
|---|---|---|---|
| 10.3 · unit 1 `n` | medium | Said “ὕπνος ἔχε γλυκερός puts the subject after the verb”. In the line ὕπνος stands before ἔχε; only γλυκερός follows. A false claim about where a word stands. | Rewritten: the object comes first, the subject ὕπνος after it, γλυκερός held to the end. |
| 10.17–20 · unit 7 `l`, `i`, `n` | medium | μῆτιν rendered “counsel”. The house table fixes μῆτις as “cunning” (2.169, 7.47, 7.447; Odyssey 19.326). | `l` “some blameless cunning”, `i` “some blameless cunning that would ward off evil…”, `n` “μῆτιν ‘cunning’ (cunning intelligence, here turned to framing a remedy)”. |
| 10.38 · unit 19 `l`, `i`, `n` | medium | αἰνῶς rendered “terribly”. The table has αἰνῶς “dreadfully” (3.158, 5.352, 8.397, 9.244, and 9.244’s own note that “terribly” is ἐκπάγλως). | `l` “very dreadfully”, `i` “dreadfully afraid”, `n` “very dreadfully”. |
| 10.93 · unit 52 `l`, `i`, `n` | medium | Same αἰνῶς “terribly”. | “dreadfully” in `l`, `i`, `n`. |
| 10.43–45 · unit 22 `l`, `i`, `n` | medium | βουλή is “counsel” here but “plan” at 10.17 in the same part; the table keeps βουλή “plan” (2.55 “shrewd plan”, 7.44, 11.230). | `l` “Need of a plan … a shrewd one, such as may protect and save”; `i` “need of a plan … a shrewd plan that may protect”; `n` “βουλῆς ‘of a plan’”. |
| 10.11 · unit 5 `n` | low | ὅμαδον printed without its accent (text has ὅμαδόν). | Accent restored. |
| 10.9–10 · unit 3 `n` | low | “κραδίης is the epic genitive of κραδίη” — κραδίη is the epic form of the word, the genitive is ordinary. | “the genitive of κραδίη, the epic form of καρδία ‘heart’”. |
| 10.41 · unit 20 `n` | low | “a future of necessity” is not a category; ἔσται is a plain future. | “a plain future: whoever goes will have to be very bold”. |
| 10.64 · unit 34 `n` | low | Claimed the edition prints a comma “because the speech opens with an infinitive” — a motive the note cannot know. | “the edition prints a comma, and the speech opens with an infinitive”. |
| 10.70–71 · unit 39 `n` | low | “hardship is the lot of kings from birth” — the Greek says ἄμμι “to us” and nothing about kings. | “hardship has been their lot since birth, so neither of them should hold back”. |
| 10.27 · unit 11 `n` | low | πουλύν called “the Ionic form of πολύν” and passed over: it is a masculine form beside the feminine ὑγρήν (noun unsaid), which the note did not admit. | “the epic form of πολύν; a masculine form beside the feminine ὑγρήν, and the construction is not quite clear”. |
| new-renderings.md · φρήν row | low | Row covered only 10.4 and 10.10, but the unit ships “mind” in both layers for singular φρήν at 10.45 and 10.46 (as 9.244). | Row extended to say so. |

## Pass 1 — checked and left alone

Reuse of published lines is exact: 10.22 (= 2.44, the unit’s `l`/`i` carry the published wording for that line), 10.42, 10.60, 10.64, 10.86 (whole-unit `l` and `i` identical to the published ones), 10.87 and 10.90 (published wording kept for those lines, including “for as long as breath stays in my chest and my knees can move”). Cross-references verified against the line: lines 3/73, 4/11/14, 6/8, 10/46/52, 26/92 (ἱζάνω), 43/85 (χρεώ), 51/92 (μέλω), 56/63 (ἐπιτείλω), 67/85 (φθέγγεο), 79/59 (ἐπιτρέπω), 22 = 2.44, 90 = 9.609–610. Quotation marks balanced: opening “ on units 17, 22, 32, 35, 46, 50; closing ” on 20, 30, 33, 39, 48, 55; `mark` on exactly those six speech openings; `p` on units 0, 9, 21, 31, 34, 40, 49 (¶ at 1, 25, 42, 60, 64, 72, 86). `l` has the `\n` count of `t` throughout; `i` has none; no ASCII apostrophes. Stock epithets in the table kept every time (βοὴν ἀγαθός ×2, ἄναξ ἀνδρῶν, κρείων, ποιμένα λαῶν ×2, διοτρεφές, φαίδιμος, παναίολος, φθισήνωρ, ἠΰκομος, Παναχαιῶν, ἀριστῆες).

## Pass 1 — findings refused

| finding | reason |
|---|---|
| `i` of unit 2 has “heavy rain” for πολὺν ὄμβρον where `l` has “much rain” | `i` is real English prose; πολύς of rain is naturally “heavy”; no table row for ὄμβρος. Sense unchanged. |
| ἐπετράπομέν note/gloss: the accent shift is said to come from γε | γε is treated as an enclitic in the accent rule; and the glossary key is the form as printed. Left. |
| unit 6 `n`: κῆρ called an accusative of respect | A defensible reading (the verb is intransitive-ish: groaned in the heart); the other, an internal accusative, comes to the same English. Left. |
| unit 24: αὔτως “as a mere man” in `i` / “just so” in `l` | Already a listed new rendering with reasons; consistent with 10.25 handled separately. Left. |
| unit 7 `i`: “first of all men” for πρῶτον … ἀνδρῶν | Stated in the note as “ahead of any other man”; correct. |
| unit 39 note: ἵει called “unaugmented” | ἵει is the same form with or without augment; the note only calls it an imperfect of ἵημι. Left. |
| scansion | No flags in the packet; nothing to scan. |

## Pass 2 — `gloss.json`

Every novel form parsed against the lines where it occurs. All 143 novel forms are present, none extra, no entry over 230 characters, only typographic ’. The 14 original broadenings all begin with the old entry whole.

| key · field | severity | what was wrong | what done |
|---|---|---|---|
| κοιμήσωνται | medium | “aor. subj. pass.” — κοιμήσωνται is the aorist subjunctive middle (the passive would be κοιμηθῶσι). | “aor. subj. mid. 3 pl.” |
| λάθωνται | medium | “short-vowel” subjunctive is wrong (-ωνται is the long-vowel form); “= Attic ἐπιλάθωνται” pinned to this line’s tmesis. | Removed both; “often with ἐπι- (ἐπιλανθάνομαι)”. |
| προθελύμνους | medium | “masc. acc. pl.” — in the line it agrees with feminine χαίτας (adjective of two endings). | “adj. of two endings, masc./fem. acc. pl.” |
| ἀλεξίκακος | medium | “masc. nom. sg.” — the line has it feminine (ἥ τις … γένοιτο, agreeing with βουλή); gloss “’a helper’” was invented. | “adj. of two endings, masc./fem. nom. sg.”; gloss dropped. |
| γιγνομένοισιν | low | Example “’for men as they live’” is not what the form says. | “’as they are born’”. |
| δαφοινὸν | low | Meaning “tawny, blood-red”; the draft keeps “tawny” for αἴθων and “deep-red” here. | “deep-red, blood-red”. |
| θρασυκάρδιος | low | Offered “stout-hearted”, which the draft reserves for the θυμός words. | “bold-hearted”. |
| κυδαίνων | low | Example “’heartening’” does not match the shipped “giving glory to”. | “’giving glory to’”. |
| μένω | low | Quoted “ἠὲ μένω … ἦ …”; the line has αὖθι μένω … ἦε θέω. | Quotation dropped. |
| πευκεδανοῖο | low | Meaning given as “bitter, piercing, harsh” — each decides a sense the draft says is unknown. | “sharp (a traditional guess; the meaning is not known)”. |
| ἀδηκότες | low | “be sated” first; the draft keeps “worn out” and says the sense is not quite certain. | Order changed; “(sense not quite certain)” added. |
| ἀσπάσιος | low | A second reading “agreeing with a land” has no support in this part. | “adj. of two endings, masc./fem. nom. sg.” |
| ἑκτορέοις | low | Lemma Ἑκτόρειος and “epic -οις” (the ending is the ordinary -οις). | “Ἑκτόρεος … masc./neut. dat. pl.” |
| ἠθεῖε | low | “dear, revered … ’dear friend’” makes the sense look known. | “honoured one (a form of address; the sense is not known)”. |
| ὀτρυνέεις | low | Example “’you will send’”. | “’you will urge’”. |
| ἀλαλύκτημαι | low | No hint that the formation is not certain (the note says so). | “formation uncertain” added. |

New or refined broadenings under `"__broaden__"` (each begins with the old entry whole; all low — the old entry did not cover the use in this part): αὔτως (ὣς δ’ αὔτως “in the same way”, 10.25), γήραϊ (dative after ἐπιτρέπω, 10.79), δοῦρε (nominative dual in apposition, 10.76), εὐρὺ (agreeing with μετάφρενον, 10.29), μῆτιν (object of τεκτήναιτο, 10.19), πουλὺν (beside fem. ὑγρήν, 10.27), σὲ (with χρεώ, 10.43), τέλος (after ἐς, a body of men, 10.56), τινά (fem., agreeing with μῆτιν, 10.19), ἠϋκόμοιο (agreeing with Ἥρης, 10.5), ἠέ (further alternative in a list, 10.8), πρὸ (after a locative in -θι, 10.12). Refined: ἔκλυον (the glosser’s “’I heard’” repeated what the old entry already held; now “aor. 1 sg. + gen. of the speaker”).

Pass 2 — refused: αἴθωνος “of a lion”, κερδαλέης “agreeing with βουλῆς”, θέω “deliberative”, and similar short contextual tags were left; they sit after the general parse and do not pin a line number or “here”. Known forms whose existing entries already cover this part (about 330) were checked by reading and left alone.

## `new-renderings.md` against `units.json`

All rows compared with the shipped `l` and `i` (after the edits above). Every row matches. One row extended (φρήν). Rows for μῆτις and βουλή are not needed: both now follow the table. αἰνῶς has no row because it follows the table.

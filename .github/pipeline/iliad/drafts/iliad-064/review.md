# iliad-064 (Iliad 11.1–121) — reviewer, pass 1 and pass 2

Method: runbook section 2, "Reviewer". Notes checked label by label against the form in its line; every
cross-reference looked up in the published parts (`iliad-NNN.json` in the repository root) and the packet;
Greek to `l` word by word; `l` against `i`; remembered English; house table (Odyssey and Iliad) row by row for
every stock word in the part; repeated lines against the published English; units, `ln`, `p` and the
concatenation of `t` against the pinned source (all valid; `t` is untouched, byte for byte). No translation
was opened or recalled. Pass 1 was the full read; pass 2 re-read every changed unit and re-walked the house
table for words pass 1 had passed (it found the μέλας row, change 34). `gloss.json` does not exist yet, so the
pass-2 check of its parses could not be made (see "For the glosser").

Counts: 34 changes — 1 high, 17 medium, 16 low. Scansion: 1 flag (line 37), real, sentence added.

Severity: high = would fail the gate or mistranslates; medium = a false label or cross-reference, a house
rendering not honoured, an unsupported claim; low = polish, tightened wording, a missing cross-reference.

## Changes

| # | line | field | sev | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 42 | l, i | high | The Greek (letters) equals the published unit at 3.337, so the validator demands the same English; the draft ended `nodded.` / `above.` where the published ends `nodded;` / `above;` (gate would fail: "same Greek as iliad-019 line 337 but different English"). | Final stop changed to `;` in both layers, text otherwise identical to 3.337. |
| 2 | 16 | n | med | "The same words stand at 13.578": Book 13 is not published (the repository ends at 10.579), so the reference points at nothing. The published line is 2.578 (iliad-013), `l` and `i` of which the draft already matches. | `13.578` to `2.578`. |
| 3 | 8 | n | med | εἴρυσαν called "the unaugmented aorist" (it is the augmented form, ει- for ἐ-; the glossary entry says so); ἤϋσε called the aorist "of ἀϋτέω" (the verb is ἀΰω, and ἤϋσε is augmented, as the glossary says). | "augmented aorist of ἐρύω … its augment written ει-"; "augmented aorist of ἀΰω ‘shout’". |
| 4 | 8 | n | low | The unit reuses the English of 8.225b–226 (published in iliad-048) but its note did not say so. | Sentence added: the relative clause stands at 8.225–226 and its English is kept. |
| 5 | 5 | n | low | The unit runs through 11.8a, so the reused lines are 8.222–225a, not "8.222–223". | "8.222–223 of Agamemnon" to "8.222–225a, where Agamemnon is the one who ‘stood’" (Agamemnon checked against iliad-048, 8.217–222). |
| 6 | 23 | n | med | οἱ in τοὔνεκά οἱ τὸν called an "article-pronoun"; οἱ is the enclitic personal pronoun (the glossary has it so); only τόν is the article. | Label corrected for each word. |
| 7 | 23 | l, i, n | med | χαριζόμενος rendered "doing a favour" / "as a favour". The table (5.71) and the published Iliad and Odyssey use "gratifying" in `l` and "to please" in `i`. | `l` "gratifying the king"; `i` "to please the king"; note reworded to match. |
| 8 | 90 | l, i, n | med | ἀρετῇ rendered "valour" in all three. The table fixes ἀρετή as "excellence" in both layers and lists "valour" among the renderings avoided (8.535, 9.498; iliad-051, iliad-056). | "by their own excellence" in `l`, `i` and the note. |
| 9 | 67 | l, i, n | med | ἄρουραν rendered "field". ἄρουρα is "plough-land" everywhere in the table and the published Iliad and Odyssey. | "plough-land" in `l`, `i` and the note. |
| 10 | 62 | l, i, n | med | οὔλιος rendered "fatal", and the note called "fatal" "the house word" (it is not in the table). οὔλιος is the longer form of οὖλος, which the Iliad table fixes as "ruinous" (οὖλος Ἄρης, 5.461, with οὖλον ὄνειρον and οὐλομένην); the drafter's `new-renderings.md` row missed that row. | "ruinous star" in `l` and `i`; note says οὔλιος is a longer form of οὖλος and "ruinous" is the house word; the `new-renderings.md` row rewritten to "ruinous" (the table must not receive "fatal"). |
| 11 | 62 | i | low | παμφαίνων rendered "shining all over" in `i`; the note says "all-shining", and iliad-040 (6.513) ships "all-shining" for the participle. | `i` "all-shining". |
| 12 | 80 | l, i, n | med | ἀλέγιζε rendered "took no heed" / "paid them no heed". Table row 8.477: ἀλεγίζω is "care for" (`l`) / "care about" (`i`); "heed" is kept for ἀλέγω. | `l` "did not care"; `i` "did not care about them"; note "care for". |
| 13 | 80–81 | l | med | ἀπάνευθε rendered "far off"; table row 10.425 fixes "apart" and lists "far off" as avoided. | `l` "apart sat down" (νόσφι λιασθείς stays "withdrawn apart" as in iliad-004; `i` "far apart" already agreed); note "apart from the others". |
| 14 | 83 | l | low | ὀλλύντας / ὀλλυμένους rendered "killing / being killed" in `l`; the three published instances (iliad-025, -046, -051) give "destroying / perishing" in `l`, "killing / being killed" in `i`. | `l` "those destroying and those perishing"; `i` unchanged. |
| 15 | 83 | n | med | ὀλλυμένους called "passive"; it is the middle participle (intransitive ‘perishing’). | "middle ὀλλυμένους ‘perishing’ (so ‘killing’ and ‘being killed’)". |
| 16 | 80–83 | n | low | "from καθέζετο to the end of the second line" is ambiguous in a four-line unit (the second line of the unit ends at γαίων, not Ἀχαιῶν). | "through Ἀχαιῶν at the end of 11.82". |
| 17 | 86 | n | med | Two claims about position wrong against the lines: τῆμος stands in 11.90, four lines after ἦμος (11.86), not "three"; and περ stands after δρυτόμος, so it cannot make ἦμος "just when". | "four lines later (11.90)"; "περ, after δρυτόμος, is an emphatic particle that the English leaves untranslated." |
| 18 | 36 | n | med | Scansion flag line 37 (see below). | One sentence added: line 37 is metrically irregular as transmitted, and where. |
| 19 | 117 | i | low | ἱκάνει rendered "takes hold of"; `l` has "comes" and the note "come upon". | `i` "comes upon her herself, from beneath". |
| 20 | 117 | n | med | "the trembling rises from the legs" is nothing the Greek says (ὑπό is only "from beneath"). | Parenthesis replaced by "the Greek does not say where the trembling starts". |
| 21 | 78 | l, n | med | Τρώεσσιν ἐβούλετο κῦδος ὀρέξαι is an Odyssey half-line (odyssey-016) and the Iliad table's κῦδος ὀρέξῃ rows give "grant glory"; `l` had "hold out glory". | `l` "grant glory" (`i` already "grant"); note says the half-line is the Odyssey's and its English kept. |
| 22 | 116 | l | low | χραισμεῖν without object is "avail" in `l` in iliad-003 and iliad-006 ("help" in `i`); draft `l` had "help". | `l` "to avail" (note: "to avail, to help"). |
| 23 | 91 | l | low | πλήξιππον in `l` rendered "the horse-lasher"; the table gives "horse-lashing" in `l` and "the horse-lasher" in `i` (4.327, 5.705, 2.104). | `l` "his companion Oileus, horse-lashing." |
| 24 | 91 | n | med | ὄρουσ’ called the aorist of ὄρνυμι; the aorist ὄρουσα is that of ὀρούω ‘spring, rush’ (LSJ). | Lemma corrected. |
| 25 | 38 (second unit) | n | med | ἐλέλικτο called the pluperfect passive of ἑλίσσω; it is the pluperfect of ἐλελίζω, the verb of ἐλέλιξε in iliad-048 (glossary: ἐλελίζω). | Lemma corrected: ἐλελίζω ‘whirl’, here ‘was coiled’. |
| 26 | 87 | l | low | `l` "his hands have had their fill" turned the accusative χεῖρας into a subject, against the note's own "literally ‘he has satisfied his hands’". | `l` "when he has sated his hands / of cutting tall trees,". |
| 27 | 69 | n | low | "a rule you will meet constantly" asserts something about the rest of the poem (Odyssey conventions, "Notes"). | Cut to the rule itself. |
| 28 | 21 | n | low | Κύπρον δέ is printed as two words in the edition; the note said "has the suffix -δε" without saying so. | "(printed as two words)" added; the reading itself kept (see refused 1). |
| 29 | 45 | n | low | Μυκήνης called "the Ionic genitive in -ης"; it is simply the genitive of Μυκήνη (Attic has the same form). | Label corrected. |
| 30 | 43 | n | low | κεκορυθμένα "said of the spear-heads"; the participle agrees with δοῦρε, and the Greek does not say which part is armed. | "agrees with δοῦρε and is ‘armed’, here ‘with bronze’". |
| 31 | 44 | l, i | low | οὐρανὸν εἴσω rendered "up into heaven" / "up to heaven"; "up" is not in the Greek. | "into heaven" in both. |
| 32 | 51 | n | low | φθὰν glossed "ἔφθασαν, the epic aorist"; it is the unaugmented athematic aorist 3 pl., Attic ἔφθασαν. | Label corrected. |
| 33 | 56 | n | low | The supplied verb is shown in parentheses in `l`, the note said "brackets". | "parentheses". |
| 34 | 24, 35 | l, i, n | med | μέλανος κυάνοιο rendered "dark kyanos". The table fixes μέλας as "black" (νηῒ μελαίνῃ, κῆρα μέλαιναν, μέλανα … λίθον); "dark" is kept for κυάνεος and κελαινός. (Found in pass 2.) | "black kyanos" in `l` and `i` of both units and in the note at 11.24; "dark serpents" (κυάνεοι) unchanged. |

### Line 37 (scansion), done by hand
δει-νὸν δερ-κο-μέ-νη, πε-ρὶ δὲ Δεῖ-μός τε Φό-βος τε: ––|–⏑⏑|–⏑⏑|––|–⏑⏑|–×. Feet 1–3 are regular (δεῖ-νὸν
spondee, with νόν long by position before δ; δερ-κο-μέ; νη-πε-ρὶ, main caesura after νη). Foot 4 is δὲ Δεῖ: δέ is
a short syllable with no consonant after it to make it long, so it stands as a long only by metrical lengthening
(the scanner's "longum of foot 4"), then μός τε Φό is a dactyl and βος τε closes. No other division fits (a short δέ cannot open a dactyl or a spondee here), so the irregularity is real. Added to the note of the unit at 11.36: "Line 37 is metrically irregular as transmitted: δέ in περὶ δὲ Δεῖμός
stands at the start of the fourth foot, where it is short but must count long."

## Considered and refused

1. **Isus as the νόθος (11.101–103, 107–108).** Checked, accepted. Ἄντιφος αὖ in 11.104 sets Antiphus against ὃ μὲν
   νόθος, so the bastard cannot be Antiphus and, with only two sons, is Isus; τὸν μέν / Ἄντιφον αὖ at 11.108–109 says
   the same. The inference rests on lines inside this part, the notes say that the sentence does not name him, and
   `i` does not name him.
2. **Speaker of ὅ γ’ at 11.94 = Oileus.** Checked, accepted. Agamemnon sprang in on foot (ὄρουσ’, 11.92); the one
   who leaps ἐξ ἵππων is the man last named, his companion Oileus; τὸν … νύξ’ then has Agamemnon as its subject and
   Oileus as object, and δάμασσε δέ μιν μεμαῶτα closes on the same man. The note's "Bianor is already dead" rests on
   ἕλε ‘took’ = ‘killed’ (which the note says) and on τοὺς μὲν λίπεν at 11.99; kept.
3. **Κύπρον δέ with πεύθετο (11.21).** Checked, accepted with the added "(printed as two words)". Κύπρον + -δε of
   direction as the goal of the report (κλέος) is the usual construction with a loose -δε; `l` "to Cyprus, a great report"
   keeps the ambiguity, `i` "the great report that came to Cyprus" resolves it the same way as the note, and
   the note admits ‘heard’ is not a verb of motion. No better parse exists (δέ cannot be the particle: no verb to
   attach a contrast to).
4. **"Gorgo" in `l`, "Gorgon" in `i` (11.36).** Γοργώ is the name; the table's "Gorgon" is for Γοργείη κεφαλή.
   Kept; `l` and `i` differ in the familiar-name way the conventions allow.
5. **ἔμβαλ’ "without augment" (11.11).** Both analyses (unaugmented ἔμβαλε, or augmented with the vowel lost) exist;
   the glossary entry does not choose; left.
6. **ἐγδούπησαν "from ἐκδουπέω" (11.45).** Could not confirm or refute from the aids named; the claim is
   harmless to the reader and the form is novel for the glosser, who may revise. Left.
7. **`i` "in good order" for εὖ κατὰ κόσμον (11.48).** Looked like a departure from the table's "in due order"
   (5.759), but the published iliad-062 (10.472, same words) ships "well in due order" / "in good order";
   the draft matches it. Left.
8. **ἀμφιβρότην note "big enough to cover the man" (11.32).** The table's avoided list rejects renderings that decide
   the shape; the draft's rendering is the table's "man-covering", and the note only glosses. Left.
9. **πάμφαινον `l` "all-bright" / `i` "shone all over" (11.30).** A finite verb, where "all-shone" would not
   read; note and `i` agree. Only the participle (11.63) was brought into line (change 11).
10. **δῄουν "cut down" (11.71)** against iliad-031's "hacked at": different construction (no object here), no table
    row; left.
11. **ὄρθι’ "high-pitched" in `l` (11.10–11).** The drafter's new rendering decides ὄρθια a little in `l`, but the
    new-renderings table and the note both say so, and "upright" would be nonsense for a voice. Left.
12. **ἦτορ "tender life" in `i` (11.115).** Table 5.250 (φίλον ἦτορ ὀλέσσῃς, "lose your life") licenses it, `l`
    keeps "heart", the note explains. Left.
13. **Κυδοιμός lower case (11.52).** Table 5.593 capitalises the personified Uproar with Enyo; here Zeus stirs up an
    "evil uproar", an adjective and no agent, and iliad-063 (10.523) is lower case. Left. (Ἔρις capital is right:
    a goddess who acts, table 4.440.)
14. **μεγακήτεϊ, ἐΐσας, νώροπα, κύανος, ἀμύμων, μερόπων, βλοσυρῶπις, φάλος.** Each checked against its table row (and
    each note says the sense is not known where the row does): conform.
15. **Quotation marks, `mark`, speeches.** None in 11.1–121; the last unit of iliad-063 ends a libation, not a
    speech. `p` is on exactly the six ¶ lines (1, 15, 47, 56, 67, 84).
16. **Missing stops in the source at 11.8–9.** The pinned source reads εἴρυσαν ἠνορέῃ … χειρῶν with no comma or stop,
    where the published 8.226 reads εἴρυσαν, … χειρῶν·. `t` is not the reviewer's to touch, the units still cut at commas
    that exist, and the build does not refuse; nothing done (runbook rule 5 applies only if the build refuses).
    The `l` of that unit ends `;` as in the published English.
17. **ὀλλύντάς (11.83).** The source prints an odd accent; `t` untouched.

## For the glosser (gloss.json absent at review)
- οὕνεκ’ is "because" in the existing entry but "that" at 11.21: broaden.
- ἐλέλικτο: ἐλελίζω, pluperfect passive. ὄρουσ’: ὀρούω. φθὰν: unaugmented aorist 3 pl. of φθάνω. ὀλλυμένους: middle.
- οἱ (11.23) is the enclitic pronoun; ὥ (11.104) the dual relative; ἀρετῇ "excellence"; ἄρουραν already "ploughland".
- ἤϋσε and εἴρυσαν already have augmented entries; the notes now agree with them.
- Κύπρον: accusative of the goal, with δέ printed apart; οὔλιος: longer form of οὖλος.

## Left for the caller
- `new-renderings.md`: the οὔλιος row was changed to "ruinous" (change 10) so that the wrong rendering is not copied into the table;
  no other row needed changing (the νόθος / γνήσιον row stands). Nothing else outside `units.json` and `review.md` was touched.
- Not run: build, validator, commit.

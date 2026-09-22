# odyssey-003 (1.213–324): reviewer's report, pass 1

I followed the pass-1 order in the runbook. I checked every grammatical label in every note by working out the form myself, and I did not rely on the drafter's label. I checked every claim about where a word stands against the packet's line. I checked every cross-reference into 1.1–212 against the text of `odyssey-001.json` and `odyssey-002.json`, and every "first time in the poem" claim by searching both files. I also checked each note against its own `l` and `i`, the Greek against `l` word by word, `l` against `i`, and the English for wording remembered from a modern translation. I re-derived the speech boundaries from the verbs of speaking. I compared the three fixed-English units character for character with the packet. I checked the house table and the drafter's own new renderings everywhere they recur in this part, and I re-ran the tiling check. The glossary does not exist yet and is out of scope.

## Mechanical checks that passed

- **`t` reproduces the packet exactly.** Joined in order (a space at a mid-line join, `\n` at each verse end), the 65 units' `t` rebuild all 112 packet lines character for character, and the result is NFC. I re-ran this after my edits and it still passes. I touched no `t`, `ln` or `p`.
- **`ln`** is correct on all 65 units. The two units starting in 225 and the two in 226 share their `ln` correctly.
- **`p: true`** stands on exactly 213, 221, 230, 252, 306, 314 and 319. These are Murray's seven paragraphs, no more and no fewer.
- **Line division**: `l` has the same number of `\n` as `t` in every unit, and there is no `\n` in any `i`.
- **The three fixed-English units match the ratified English exactly** (checked by string comparison):
  - 221 = odyssey-002's 178, "Him then in turn addressed the goddess, gleaming-eyed Athena:" / "Then the goddess, gleaming-eyed Athena, spoke to him in turn:"
  - 224 = 002's 169, "But come, tell me this, and recount it exactly;" / "But come now, tell me this, and set it out for me exactly:"
  - 314 = 001's 44, "Him then answered the goddess, gleaming-eyed Athena:" / "Then the goddess, gleaming-eyed Athena, answered him:"
- **The new reply formula (213 = 230 = 306)** has identical `l` and `i` in all three units.
- **Speech boundaries, re-derived from the Greek.** There are six speeches:
  - 214–220: Telemachus, after the formula at 213
  - 222–229: Athena, after 221
  - 231–251: Telemachus, after 230
  - 253–305: Athena, after 252 (τὸν δ’ ἐπαλαστήσασα προσηύδα)
  - 307–313: Telemachus, after 306
  - 315–318: Athena, after 314

  Each has `“` in both `l` and `i` of its first unit, `”` in both `l` and `i` of its last, and `mark` on its first unit. The six speech-introduction lines (213, 221, 230, 252, 306, 314) are narration, with no quotation mark and no `mark`. **Nothing runs in or out of this part.** odyssey-002's last unit (1.212) closes `l` and `i` with `”`. Athena's last speech closes at 318 (ἀμοιβῆς), and 319 ἡ μὲν ἄρ’ ὣς εἰποῦσ’ ἀπέβη resumes the narration, which runs to the end of the part at 324.
- **Augment labels: all correct.** This was last part's weak spot, so I derived every one by hand. The drafter labels 29 forms (30 labels, since δῶκεν is labelled twice), and all of them are right:
  - **Augmented, including inside compounds**: ηὔδα; ἀν-έ-γνω; ἔτετμε; ἐγείνατο; ἐβόλοντο; ἤρατ’; ἀν-ηρείψαντο; ἔτευξαν; προσ-ηύδα; ἐνόησα; ᾤχετο; ἔλλαβε; ἀπ-έ-βη; δι-έ-πτατο; ὑπ-έ-μνησεν; ἐπ-ῴχετο
  - **Unaugmented**: ὄφελον; γένετο; θῆκαν; μέλλεν; δάμη; τολύπευσεν; κάλλιπεν; δῶκεν (×2); νεμεσίζετο; φιλέεσκε (an iterative); θῆκε; θάμβησεν; ὀίσατο

  No present or future is called "unaugmented", the mirror-image error that turned up in the 002 glossary.
- **Other grammar, all checked and correct:**
  - **Genitives in -οιο and -αο**: μεγάροιο, ὁδοῖο, οἰχομένοιο, Μερμερίδαο.
  - **Datives in -ῃσι, -οισι and -εσσι**: πρώτῃσι θύρῃσι, ἐρέτῃσιν, τεοῖσι, οἷς ἑτάροισι, κτεάτεσσιν.
  - **Infinitives**: ἔμμεναι, and δόμεναι beside δοῦναι.
  - **Particles**: κε/κεν as ἄν, with the aorist indicative at 239–240 correctly called "would have"; ῥα; ἄρ’; νυ; concessive περ at 236, 288, 309 and 315; epic τε at 215.
  - **Possessive ὅς**: οἷς, ᾧ, ᾗσι, οἷσιν, ἑόν, ἑοῖς.
  - **Preposition after its noun, with accent (anastrophe)**: ἑοῖς ἔπι, τοῦ … ἔκ, Ἰθάκην κάτα.
  - **Suffixes**: -θεν in κεῖθεν, -δε in Σπάρτηνδε and οἶκόνδε.
  - **Other forms**: the dual δοῦρε; the article-form as a relative in ὅ κε (254) and ὅ οἱ (300); the demonstrative ὃς γάρ (286); the imperatives ἔστων, ἄνωχθι, ἴτω, ἔσσ’ and ἔρχεο; the subjunctives εἴπῃσι, πίθηαι and ἀνώγῃ; the optatives γενοίατο, ἀκαχοίμην and τλαίης.
- **Cross-references into odyssey-001 and 002: every one checks against the files.** They are:
  - 1.5 ἀρνύμενος; 1.6 ὣς; 1.8 νήπιοι; 1.26 δαιτί; 1.29 ἀμύμονος Αἰγίσθοιο; 1.39 μνάασθαι; 1.40 ἔσσεται; 1.43 ἀπέτισεν and ἀγαθὰ φρονέων; 1.55 κατερύκει; 1.60 φίλον ἦτορ; 1.66 περί with the genitive; 1.88 ἐγών; 1.89 μένος; 1.90 εἰς ἀγορὴν καλέσαντα; 1.94 πευσόμενον.
  - From 002: 1.99 ἄλκιμον; 1.106–112; 1.119 νεμεσσήθη; 1.124 σε χρή; 1.134 ὑπερφιάλοισι; 1.143 ἐπῴχετο; 1.159 μέλει; 1.163 ἰδοίατο; 1.169 and 1.206; 1.178; 1.179; 1.180 Anchialus; 1.182–186 the ship; 1.186 ὑλήεντι; 1.187 ξεῖνοι; 1.194 ἐπιδήμιον; 1.196 δῖος.
  - **"First in the poem" claims**: Penelope (223), Nestor and Menelaus (284) and ἰσόθεος (324) do not occur anywhere in 1.1–212.
  - **Longest speech**: "the longest speech in the poem so far" (305) is true. Athena's 253–305 runs 53 lines, against 34 for her 179–212 speech, the next longest.
- **House-table renderings are applied consistently**:
  - γλαυκῶπις Ἀθήνη (221, 314, 319); ὢ πόποι "Ah!"/"Ah," (253); ἀμύμων "blameless" (232); ὑλήεις "wooded" (246); δῖος "heavenly" (284, 298); φίλη πατρὶς γαῖα "dear fatherland" (290); ξεῖνοι "guest-friends" (313); Παλλὰς Ἀθήνη (252).
  - **The drafter's own new renderings recur the same way each time**: the reply formula (×3); "prudent" (×3); "the gods who are forever"; "the knees of the gods"; "swift ship" at 260 and 303; "take heed of my words" at 271 and 305; "in mind and in heart" at 294, with 322 keeping φρένες and θυμός apart as "mind" and "heart".
  - **Recurring words outside the table stay consistent**: ὀπίσσω is "hereafter" in `l` at 222 and 240, and "in time to come" in `i` at both. μένος is "force", as at 1.89. νεμεσσάομαι is "be indignant", as at 1.119.
- **Scansion**: the packet flags no line. As spot checks I scanned 213, 225 and 297 by hand. All three are regular:
  - **213**: πεπνῡμένος has a long υ, and with it the line scans cleanly.
  - **225**: ὅμῑλος has a long ι. δὲ ὅμιλος stands in hiatus with correption, and χρεώ is one syllable by synizesis, which is ordinary.
  - **297**: scans without licence.

## Changes made

**error** means a false statement, a missing or misplaced structural mark, or a note contradicting its own unit. **minor** means an inexact or over-reaching claim, an internal inconsistency, or wording suspiciously close to a published translation.

| line · field | sev | what was wrong | what I did |
|---|---|---|---|
| 230 · `n` | error | "In a line of this kind the name and epithet fill the **second half** of the verse." This is false of this line. The main caesura falls after Τηλέμαχος (penthemimeral: τὴν δ’ αὖ Τηλέμαχος ‖ πεπνυμένος ἀντίον ηὔδα), so the name is in the first half. The second half is the epithet plus ἀντίον ηὔδα. | "…fill the **middle** of the verse, between τὴν δ’ αὖ and ἀντίον ηὔδα, …" |
| 316 · `l` | error | The note says "φίλον ἦτορ is **'your own heart'**, as at 1.60", and 1.60's published `l` is indeed "your own heart". But this unit's own `l` read "whatever your **dear** heart bids you". The note contradicted its unit and broke the cross-reference it cites. | `l` → "whatever your **own** heart bids you give me," (`i` "your heart" is fine as prose.) |
| `about` | error | "…where Ilus son of Mermerus had refused him poison for his arrows and **her own father** had given it". Athena's own father is Zeus. The giver at 264 is πατήρ … ἐμός in the mouth of "Mentes", that is Anchialus, as the unit note at 262 correctly says. | "…and **the father she claims as Mentes** had given it". (`about` is not a locked field.) |
| 227 · `n` | minor | "ὥς τε is taken here as 'so, in such a way', **the accented adverb of 1.6** with epic τε". The acute here is thrown back onto proclitic ὡς by the enclitic τε. It is not evidence of the adverb ὥς 'thus' that stands at 1.6 (οὐδ’ ὣς). So the note presented as settled the very point it goes on to call open. The note also failed to connect its alternative with 308, where the draft itself glosses ὥς τε as the comparative 'just as'. | The reading and the alternative are kept, and the note now adds: "…the comparative sense ὥς τε has at 308. The accent does not decide between them: it is thrown onto ὡς by the enclitic τε, not the accent of the adverb ὥς 'thus' at 1.6." `l` and `i` are unchanged (see refusal 1). |
| 221 · `n` | minor | "τὸν δ’ αὖτε προσέειπε is one of **three** distinct reply-formulas". The poem already has four: τὴν δ’ ἀπαμειβόμενος προσέφη at 1.63, and the drafter's own new-renderings.md calls 213 "the fourth reply-formula". The note contradicted the drafter's own record. | "…is one of the reply-formulas kept distinct in the English: **in this part** it stands beside τὸν δ’ ἠμείβετ’ ἔπειτα, … and the new formula of 213, …" |
| 215 · `n` | minor | "οἶδ’ is οἶδα elided, held over to the head of 216". The head of 216 is οὐκ, and it is οὐκ οἶδ’ that is held over. | "οὐκ οἶδ’, with οἶδ’ for οἶδα elided, is held over to the head of 216, …" |
| 216 · `n` | minor | "ἑόν is from ἑός, a by-form of the possessive ὅς 'his own', **easily mistaken for a relative**." The warning in conventions.md applies to ὅς/ἥ/ὅν. ἑός has no relative homograph, so the warning was pasted in where it cannot apply. | Clause dropped. |
| 264 · `n` | minor | "265 takes up the broken wish of 255 with **the same** τοῖος ἐών". The earlier τοῖος ἐών stands at 257, not 255. | "…with the τοῖος ἐών **of 257**, 'being such a man'." |
| 252 · `l` | minor | `l` "Pallas Athena **addressed**" for προσηύδα. The drafter's own new-renderings.md rules out "addressed" because it is taken by προσέειπε and προσέφη. The house table and 002's 1.122 render προσηύδα "spoke" ("to her winged words he spoke"), and this unit's `i` already has "spoke to him". | `l` → "To him, in deep indignation, spoke Pallas Athena:" |
| 253 · `i` | minor | Remembered English: "you are **sorely in need** of Odysseus". This is the "sore need" of the familiar published wording of this line, and it goes beyond πολλὸν δεύῃ "you lack much". | Rebuilt from the Greek: "Ah, truly you are much in want of Odysseus, gone away as he is, …" This also restores ἦ δή 'truly', which `l` has and `i` had dropped. |
| 266 · `i` (+ new-renderings.md) | minor | Remembered English: "They would **all find** a swift doom and a bitter marriage". "All … would find swift X and bitter Y" is the frame of the familiar published versions of this line. It also matters more than a one-off, because the drafter has registered this line as a fixed rendering for its later recurrences. | `i` → "All of them would meet a swift doom and a bitter marriage." The new-renderings.md table entry is updated to match and records why. The compounds and `l` are unchanged. |

**Totals: 11 edits: 3 error, 8 minor.** 10 are in `units.json` (2 `l`, 2 `i`, 6 `n`) and 1 is in `about`, with the matching new-renderings.md update. After the edits I re-ran the tiling check and the three fixed-unit comparisons, and both still pass.

## Findings considered and refused

1. **227 · `l`/`i` taken as "so insolently … do they feast".** I considered switching to the comparative "like men who behave insolently" or the causal "since". I refused. The passage is disputed among the commentators, both main readings give the same sense of the scene, and the note now states the alternative honestly and says why the accent does not decide. Left as a stated choice.
2. **213 · πεπνυμένος "prudent" (judgement call).** I checked it for remembered English. The familiar modern renderings of this epithet are other words ("thoughtful", "poised", "clear-headed", "sensible"), and the drafter lists and avoids them. "Prudent" is the plain lexicon sense, and the note is honest that the link with πνέω is uncertain. **Accepted.**
3. **213 · ἀντίον ηὔδα "spoke, face to face" (judgement call).** ἀντίον can be 'facing' or simply 'in reply' (Cunliffe gives both). The note gives both senses, "face to face, in answer". "In answer" alone would crowd "answered", which is reserved for ἠμείβετο. **Accepted.** The rendering is literal to ἀντίος, and the note does not overclaim.
4. **320 · ἀνόπαια (judgement call; the brief says 318, but the word is in 320).** The meaning is genuinely unresolvable. The note lists every ancient reading ('upward', 'unseen', ἀν’ ὀπαῖα 'up through the smoke-vent', a bird's name) and says the Greek does not settle whether she changes shape. `l` and `i` commit to 'upward' because an English sentence has to say something, and the note owns that. **Accepted as honest.**
5. **277 · ἔεδνα and οἱ δέ (judgement call).** It is also unresolvable. The lexicon sense (a suitor's gifts for his bride) conflicts with the bride's family preparing them here. The note says exactly that and that "how the two fit together has long been discussed". "Wedding-gifts" is neutral between the two. The note states flatly that οἱ δέ are her father's people, not the suitors. That is the majority view, but some read the suitors here. I left it, because the note would otherwise need a second caveat in a unit that already carries one. **Flagged for the owner as the one place a reader might want "probably".**
6. **The forms left grammatically open**: ἀποτίσεται (268), future middle or short-vowel aorist subjunctive; ἀπώσεαι (270), the same; τοι (222), particle or dative; ἐπί as an adverb at 273 and 291. Each note states both readings, and the form genuinely does not decide. I left them as they are. They are honest, and pass 2 or the glosser should keep the same openness in the glossary entries.
7. **296 · `l` "there is no need for you" beside `i` "it is not right for you".** χρή covers both 'it is needful' and 'it is fitting/you ought'. `l` follows the note's gloss, and `i` gives the idiomatic force. They are within the word, so I refused.
8. **311 · `l` "rejoicing in your spirit" for ἐνὶ θυμῷ**, where θυμός is "heart" elsewhere in the part (294, 320, 323) and in 001/002. I refused because the same unit's first line already renders φίλον κῆρ "in your own heart", and two "hearts" for two Greek words in adjacent lines would blur them. θυμός is not on the house table, and `i` has "glad at heart".
9. **Possible Murray echoes**: 217 "whom old age overtook among his own possessions", 219 "most ill-fated of mortal men", 293 "by guile or openly", 297 "no longer of that age", 301 "fine and tall", 315 "eager as I am to be on my way". All of them fall straight out of the case relations, and Murray is the public-domain edition of record, not one of the banned translations. On the precedent of 002's review (refusal 10) I left them. The two I changed (253 and 266) are the ones where a distinctive non-literal word ("sore", "find") carried the echo.
10. **267 "lie on the knees of the gods".** This is also the familiar wording in English, but it is the literal image, and the drafter registered it deliberately with the note that the image's origin is disputed. The alternatives would lose the Greek. I refused.
11. **222 · `n` "ὄνυμα, an epic form of ὄνομα".** Strictly it is an Aeolic form, and in Homer it occurs only inside compounds like this one. "Epic" is how Autenrieth-level notes put it, and it is not false of the dialect of the poem, so I refused.
12. **235 · ἀκαχοίμην "reduplicated aorist optative".** I checked it against the possibility of a present optative middle. LSJ files ἀκαχοίμην (Od. 1.236) under the aorist 2 middle of ἀκαχίζω, so it stands.
13. **240 · ἤρατ’** is given no dictionary form, only "an aorist middle 'won for himself'". The form is the first aorist of ἄρνυμαι/αἴρω ("win"), whose lemma is disputed. Saying only "the sense is that of ἀρνύμενος at 1.5" is careful rather than wrong. I refused. The glosser will have to pick a lemma.
14. **264 · "ὁμιλήσειεν … still under εἰ γάρ".** 265 has no εἰ γάρ of its own. It is the resumption of the wish broken off at 259. That is the natural reading of the anacoluthon, so I refused.
15. **225 · τίπτε δέ σε χρεώ, the note's "σε is its object".** Loose, since σε is the accusative of the person with χρεώ (ἱκάνει being understood). The note immediately glosses it correctly ("what need is on you"). I refused.

## Verdict

**Pass 1 is complete, and I found nothing that would stop publication.** The structural marks were already correct. All six speeches open and close in the right units, with `mark` on each first unit. Nothing runs in from odyssey-002 or out to odyssey-004. The three repeated units carry the ratified English exactly. The drafter's known weak spot, the augment, is clean this time: all 30 augment labels are right, including the seven forms augmented inside a compound (ἀνέγνω, ἀνηρείψαντο, προσηύδα, ἀπέβη, διέπτατο, ὑπέμνησεν, ἐπῴχετο) and the unaugmented compound κάλλιπεν.

The three errors were a false claim about where words stand in the verse (230), a note contradicting its own `l` (316), and a factual slip in `about` that gave Athena's disguise-father as her own. The minor fixes are small: over-reach in 215, 216, 221, 227 and 264, one inconsistent `l` (252), and two `i` phrasings that echoed familiar published wording (253, 266).

**For the next stage** (pass 2 and the glosser):
- 277 οἱ δέ is stated as her father's people without a hedge (refusal 5).
- ἤρατ’ (240) needs a lemma decision in the glossary (refusal 13).
- The open parses at 268, 270 and 222 should stay open in the glossary entries.
- The 266 line is a registered fixed rendering whose `i` changed at review. Any later recurrence must use "All of them would meet a swift doom and a bitter marriage."

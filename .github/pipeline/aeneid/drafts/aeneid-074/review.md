# Review — aeneid-074 (Aeneid X.185–275), adversarial reviewer

**Severity counts: major 9, medium 2, low 21 (18 in pass 1, 3 in pass 2). Refused or upheld-without-change findings: 16. Scan-fixes entries added: 8 (all wrong full lines; no half-lines, no carriers).**

I reviewed this part in two passes.

**Pass 1** covered all 39 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked:
- the drafter's doubtful points (186 *Cinyre*, 188 *vestrum*, 199, 202–203, 214 *aera*, 253 *urbis*, 261 *cum deinde*, 266)
- the Latin Library variants, and the text for misprints (rule 5b)
- the speech marks
- the no-advisory decision
- `about`, the title and the part names

I read every `i` for echoes of the well-known English versions.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

I checked the in-poem cross-references against the pinned source. All are right except one, which was imprecise (L6):
- V.116 (*Pristim*), V.122 (*Centauro*), V.826 (*Cymodoceque*), V.867–868 (Aeneas steers after Palinurus is lost)
- VIII.414 and 710 (*Ignipotens*), VIII.620 (*flammasque vomentem*), VIII.680 (*stans celsa in puppi*, Augustus at Actium)
- IX.77–122 (the ships become nymphs), IX.80–92 (the pines of Ida), IX.82 and 117 (*genetrix*), IX.101–103 (the promise), IX.118 (*vincula*), IX.121 (= 10.223 word for word), IX.618 (*Dindyma*)
- X.147 (Aeneas at sea at midnight)
- XII.290 (Aulestes): he is named at 290 and killed at 294–296, so the note now cites XII.289–296 (L6)

**Pass 2** re-read every edited field in full, re-checked speech marks, line counts and note lengths, and made three more changes (P2-1 to P2-3).

**Scansion.** I hand-scanned all 91 lines. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story` (with each unit's `ln`), and compared its output with mine syllable by syllable. The helper is `drafts/aeneid-074/scan_check.py` (073's, with the part id changed).
- **The packet's flags.** 217 (COSTLY 2.2) is wrong: *Aeneas* has Ae- split (M2). 224 (COSTLY 2.6) is **right** and gets no entry: *chŏrēīs* (Greek χορεία) costs only because the scanner dislikes a long vowel before a vowel.
- **Seven more lines are wrong without a packet flag:** 189, 225, 228, 229, 253, 260, 263.
  - Greek *eu*: *Teucros* 260. Initial *Ae-*: *Aenea* 229 (and quantities).
  - Greek names with wrong quantities: *Phaethontis* 189 (ae read as a diphthong, as at 5.105), *Cymodocea* 225.
  - Consonantal *i* after a prefix: *biiugique* 253 (as 5.144, whose `why` already cites 10.253), with *frēna* and *leōnes* also wrong.
  - Wrong quantities with no special feature: 228 (*ignārum*, *adlŏquĭtur*, cost only 0.3), 263 (*Dardănĭdae*, *ē mūris*).
- **No carriers are needed:** every unit has `sc`.

Every new `scan-fixes.json` entry was checked by script (`drafts/aeneid-074/add_scan_fixes.py`, 073's with the entries replaced):
- against the build's word-match rule (`strip(sc) == WORD_RE.findall(line)` for the line as printed)
- against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×
- against its own `why`: each `why` gives a syllable count, and the script checked it.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 8 entries apply (keys `10.n`)
- **all 39 units get `sc`**
- every unit's `sc` lines up with its words
- all 91 lines pass the validator's metre check
- the scanner report has one entry left, COSTLY 2.6 at 224, which is right (see above; the build only prints COSTLY lines)

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by Python scripts: `review_edits.py` for pass 1 (25 field edits plus one in `about`) and `review_edits_pass2.py` for pass 2 (3 edits). Each old string was asserted to occur exactly once in its field. The file is written with `aeneid_lib.jdump`; a round-trip of the drafter's file through `jdump` was byte-identical before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` are as the drafter left them in all 39 units (checked by script against a copy taken before any edit). `title`, `titleEn` and `part` are unchanged; `about` changed only "Cinyras" to "Cinyrus" (Medium 1). No unit boundary was changed.
- **15 units changed:** 0, 1, 4, 7, 8, 9, 11, 13, 14, 16, 19, 23, 29, 33, 34.
- **Layout checks.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.** `t`, `l` and `i` each carry the marks on the same units: Cymodocea “ unit 14 (228) / ” unit 23 (245); Aeneas “ ” unit 29 (252–255).
- **Note lengths.** The notes run 37–120 words, under the validator's 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- **`scan-fixes.json`.** The diff only appends: 92 insertions, 0 deletions, trailing newline kept, formatting unchanged. The new keys follow 10.179, in line order.
- **Build and validator not run.** `build_aeneid.py` has no dry-run mode, so its scansion step and the validator's metre and `sc`-alignment checks were replicated instead.

## Changes — pass 1

### Major
- **M1. 10.189, *Phaethontis* (cost 0.0, unflagged).** The scanner read *Phae-* as a diphthong (14). Right, as 5.105 and as the drafter's own note says ("four syllables"): Nam-quĕ fĕ | rūnt lūc | tū Cyc | num Phă-ĕ | thon-tĭs ă | mā-ti (15).
- **M2. 10.217, *Aeneas* (flagged COSTLY 2.2).** The scanner split *Ae-* (15). Right: Ae-nē | ās nĕ-qu(e) ĕ | nim mem | bris dat | cū-ră quĭ | ē-tem (14).
- **M3. 10.225, *Cymodocea* (COSTLY 1.5, unflagged).** The scanner made *-si-* and *-ma* long, *Cy-* short, and *-cea* one syllable. Right, with the quantities of *Cymodoceque* at 5.826: quā-rum | quae fan | dī doc | tis-sĭ-mă | Cȳ-mŏ-dŏ | cē-a (14).
- **M4. 10.228 (cost 0.3, unflagged).** Right count, wrong quantities: the scanner made *ignārum* short in the a and *adlŏquĭ-* long-long. Right: tum sīc | ig-nā | r(um) ad-lŏ-quĭ | tur Vĭ-gĭ | lās-nĕ dĕ | um gens (15).
- **M5. 10.229, *Aenea* (unflagged).** Right count, wrong quantities: the scanner made *-nē-ā* short-short and *Vi-gi-* long-long. Right (as 3.41 *Quid miserum, Aenea, laceras*): Ae-nē | ā Vĭ-gĭ | l(a) et vē | līs im | mit-tĕ rŭ | den-tis (14).
- **M6. 10.253, *biiugique* (COSTLY 1.5, unflagged).** The scanner lengthened *bi-iu-*, shortened *frē-*, and made *leo-* one syllable. Right, as 5.144: tur-rĭ-gĕ | raequ(e) ur | bīs bĭ-jŭ | gīqu(e) ad | frē-nă lĕ | ō-nes (15).
- **M7. 10.260, *Teucros* (cost 0.0, unflagged).** The scanner split *eu* (15). Right: Iam-qu(e) in | cōn-spec | tū Teu | crōs hă-bĕt | ēt sŭ-ă | cas-tra (14).
- **M8. 10.263, *Dardanidae* (unflagged).** Right count, wrong quantities: the scanner made *Dar-da-ni-* all long and *ē mū-* short. Right: Dar-dă-nĭ | d(ae) ē mū | rīs spēs | ad-dĭ-tă | sus-cĭ-tăt | ī-ras (15).
- **M9. Unit 209–212, *caerula* (grammar, all three layers).** `l`, `i` and `n` took *caerula concha* together, "with his blue conch", as an ablative. The metre forbids it: the fifth foot is *caerŭlă*, with a short final -a (*concha* fills the sixth foot), so *caerula* cannot be ablative. It is neuter accusative plural with *freta*, object of *exterrens*: "terrifying the sea-blue straits with his conch". The scanner already had this right. Now:
  - `l`: "with his conch the sea-blue / straits terrifying"
  - `i`: "who terrifies the blue seas with his conch"
  - `n`: "'caerula… freta', 'the sea-blue straits', object of 'exterrens'; the metre makes the -a of 'caerula' short, so it cannot agree with the ablative 'concha', 'with his conch'."

### Medium
1. **Unit 185–188 and `about`, *Cinyre*.** The English used "Cinyras". A Latin vocative in *-e* comes from a nominative in *-us* (or a Greek *-es*). *Cinyras* would make the vocative *Cinyra*, and it is also the name of the Cyprian king, Adonis's father, which invites a false identification. `l`, `i` and `about` now read "Cinyrus". The note says "'Cinyre', vocative, pointing to a nominative 'Cinyrus'". The variant note (*Cunare*) is kept.
2. **Unit 189–193, *canentem*.** The note and `i` take *canentem* with *senectam* ("a white old age"), but `l` took it with Cycnus ("whitening, … drew on old age"). `l` now reads "in soft plumage drew on a whitening old age". The note now pairs *canentem… senectam* and adds that the metre makes *cā-* long, so the word is from *caneo*, not *cano*.

### Low
- **L1. Note 185–188, *vestrum*.** "Love and his fellow love-gods" is now "Love … together with his mother Venus, or with the other powers of love". Both are old explanations, and neither is certain.
- **L2. `i` 185–188.** "bravest in war of the Ligurian chiefs" made *Ligurum* partitive. It is the genitive with *ductor*: now "leader of the Ligurians and bravest in war".
- **L3. Note 185–188.** *olorinae… pennae* does not frame the line, because *cuius* comes first. It now reads "enclosing 'surgunt de vertice'".
- **L4. Note 198–201a, Manto.** "in Greek legend the daughter of … Tiresias" is now "commonly identified with the daughter of … Tiresias". Virgil's Manto may be a separate Italian seer.
- **L5. Note 198–201a, *dives avis*.** "ablative of respect" is now "ablative with an adjective of plenty" (A&G 409a).
- **L6. Note 207–208.** "Book XII (290)" is now "(289–296)". He is named at 290 and killed at 294–296 (checked in the edition).
- **L7. `i` 213–214.** "cutting the plains of salt with their bronze-clad prows" rendered the Latin Library's *aere*. It now renders the print's *aera* as subject, as `l` and `n` do: "and their bronze prows were cutting the plains of salt".
- **L8. Note 217–218.** Added "'Aeneas', 'Ae-' one syllable", to match M2.
- **L9. Note 224–228a.** Added "'Cymodocea' is five syllables, Cy-mo-do-ce-a", to match M3.
- **L10. Note 228b–229a, Servius.** "Servius says the words recall a ritual formula with which the Vestal Virgins roused the king of sacrifices" was an unchecked attribution from memory. It is softened to "Ancient commentators heard in the words a ritual call used to rouse a priest, 'vigilasne, rex? vigila'". Also added "'Aenea' is three syllables, the last long", to match M5.
- **L11. Note 230–231a.** *Idaeae… pinus* does not frame the line, because *Nos sumus* comes first. It now reads "enclosing 'sacro de vertice'".
- **L12. Note 236–237.** The elision list left out *atqu(e) horrentis*. Added.
- **L13. `l` 244–245.** "of huge Rutulian slaughter will look upon the heaps" took *ingentis* with *caedis* (genitive singular). The note and `i` take it with *acervos* (accusative plural). It now reads "will look upon huge heaps of Rutulian slaughter".
- **L14. `l` 252–255.** "Kindly mother of Ida, of the gods" treated *Idaea* as a genitive. It is now "Kindly Idaean mother of the gods".
- **L15. Note 252–255, *urbis*.** "nominative here, an old plural form" is now "must be nominative plural here, an old spelling of 'urbes' (which the Latin Library prints), not Greenough's usual accusative '-is'".
- **L16. Note 252–255.** Added "'biiugi' is bi-iu-gi, the second i a consonant", to match M6.
- **L17. `i` 260–262a.** "he has … in sight …, and then he raised" mixed tenses and lost the inverted *cum*. It was recast as a main clause followed by a "when" clause (tense settled in P2-1).
- **L18. Note 260–262a.** Added "'Teu-' in 'Teucros' one" syllable, to match M7.

## Changes — pass 2
- **P2-1. `i` 260–262a.** The pass-1 wording put *habet* into the past. It is now in Virgil's present, as `l` is: "And now, standing on the lofty stern, he has the Trojans and his own camp in sight, when he lifts the blazing shield high in his left hand."
- **P2-2. Note 224–228a.** Added "'ignarum' (long 'a', from 'gnarus')", to match M4.
- **P2-3. Note 262b–264a.** Added "(Dar-da-ni-dae, the middle syllables short)", to match M8.

## Scan-fixes entries added (8)
| key | reason | syllables |
|---|---|---|
| 10.189 | *Phaethontis* Pha-e-, not a diphthong (as 5.105) | 15 |
| 10.217 | *Aeneas*, initial Ae- (packet flag) | 14 |
| 10.225 | *Cymodocea* (quantities, no synizesis; *doctissimă*) | 14 |
| 10.228 | *ignārum*, *adlŏquĭtur* (quantities) | 15 |
| 10.229 | *Aenēā* vocative (quantities) | 14 |
| 10.253 | *biiugi* bĭ-jŭ- (as 5.144); *frēna*; *leōnes* three syllables | 15 |
| 10.260 | *Teucros*, Greek eu | 14 |
| 10.263 | *Dardănĭdae*, *ē mūris* (quantities) | 15 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **224 *choreis*** (flagged COSTLY 2.6): Ag-nōs | cunt lon | gē rē | gem lus | trant-quĕ chŏ | rē-īs (13). Right. The cost comes from the long *-ē-* before a vowel (Greek ει). The build only prints COSTLY lines, as for 143 in 073.
- **209 *Triton … caerula***: Trī-tōn (as 1.144), and *caerŭlă* has a short final -a. Right; see M9.
- **214 *Troiae et … aera***: *Troi(ae) et* is right, and *aeră*/*aerĕ* scan alike, so the metre does not decide the variant.
- **261 *deinde*** is two syllables, and **271 *aureus*** is three. Right.
- **273 *lugubre*** is *lū-gūb-re*, the *-gu-* lengthened before *br*, which is the only fit. Right.
- **227 *subremigat*** and **251 *adspectans***: the prefix syllable is long. Right.
- **264 *iaciunt*** and **248 *iaculo***: the initial *i* is consonantal. Right.
- **187 *cuius***: *cū-ius*. Right.
- **192 *canentem***: *cā-*, from *caneo*. Right; see Medium 2.
- **238 *Etrusco***: short *Ĕ-* (as 10.148). Right.

## Refused or upheld findings
1. **10.253 *urbis* (not a misprint; kept as printed).** It must be nominative plural, coordinate with *Dindyma*. A nominative plural in *-īs* is an attested old spelling of *-ēs* (Allen & Greenough's account of the third-declension plural; it is also found in old manuscripts of Virgil). It is therefore the source's own orthography, not a letter the sense allows only one way to read, and rule 5b does not apply. It is unusual for Greenough, who keeps *-is* for accusatives, so it goes to the owner. The metre cannot decide, because the two forms scan alike.
2. **10.214 *aera* (kept as printed).** It is construable as a nominative plural, "the bronzes", meaning the prows, as a second subject. The *aere* of the Latin Library is a variant, not a correction. Upheld; only `i` was aligned (L7).
3. **10.256 *rubebat* (kept as printed).** It is a known variant of *ruebat* and construable, and the note gives both. Upheld.
4. **No other misprints.** I checked the capitals after stops, the speech marks (both speeches close at line end) and Greenough's spellings (*adspectans*, *adlabi*, *adloquitur*, *adsurgens*, *inrita*, *certast*, *siquando*, *Cybebe*, *Mantus*, *pristim*, the *-is* accusatives *aequalis*, *praecipitis*, *horrentis*, *rudentis*, *ingentis*). Upheld.
5. **10.188 *vestrum*.** Upheld as plural possessive, softened (L1). The reading *crimen amor vestrum* (with *amor* nominative) is not Greenough's punctuation, so it is not added.
6. **10.261 *cum deinde… extulit*** as inverted *cum*. With Greenough's full stop after *ardentem*, the *cum*-clause carries the main event after *iamque… habet* (A&G 546a). Upheld; the `i` now shows it (L17, P2-1).
7. **10.199 *Tusci… amnis*** as the Tiber. This is the standard explanation. Upheld.
8. **10.202–203**, the races of Mantua left unnamed. Upheld.
9. **10.266 *clamore secundo*** as "glad clamour". Upheld.
10. **10.204 *in se… armat*** as "against himself". This is the usual explanation. Upheld.
11. **Note 189–193, Ovid Metamorphoses 2.367–380** (Cycnus, the Ligurian king). Upheld from memory.
12. **Note 224–228a, Iliad 18.39** (Cymodoce among the Nereids). Upheld from memory.
13. **Note 264–266, Iliad 3.3–7** (the cranes); **note 270–271, Iliad 5.4–7** (fire from Diomedes' helmet and shield); **note 272–275, Iliad 22.26–31** (Achilles like the dog-star). Upheld from memory.
14. **Echo check.** No `i` line echoes a distinctive phrase of a known English version. "mortalibus aegris" → "suffering mortals" is the stock rendering. Upheld.
15. **Speech marks** (Cymodocea “ 228 / ” 245; Aeneas “ 252 / ” 255). They agree in `t`, `l` and `i`. Upheld.
16. **Advisory: none (upheld).** This stretch is a catalogue and the preparation for battle, with no killing on stage.

## For the owner (QUESTIONS.md)
- **10.253 *urbis*.** Kept as printed as an old nominative plural, not corrected under 5b (see Refused 1). If the owner prefers to treat it as a misprint for *urbes*, the 5b sentence goes at the head of note 252–255. The scan-fix holds either way.
- **10.186 *Cinyre*: English "Cinyrus".** This is chosen on morphology (vocative *-e* ← *-us*). Many texts read *Cunare* (from *Cunarus*). I have not checked which editors print which, or what Greenough's school notes call the man.
- **Unchecked attributions from memory:**
  - Ovid Met. 2.367–380
  - Iliad 18.39, 3.3–7, 5.4–7, 22.26–31
  - the ritual call *vigilasne, rex? vigila* (softened to "ancient commentators"; the drafter's Servius/Vestals form is not verified)
  - Manto as the daughter of Tiresias (softened)
  - Mincius flowing from Benacus (Garda) past Mantua
  - Strymon cranes; Sirius and the dog days
- **Glossary stage (not this review's file).** Several `known-forms.json` entries do not fit this part. The glossary drafter should broaden them:
  - *canentem* is given only from *cano*; here it is from *caneo*
  - *urbis* is given only as genitive singular; here it is nominative plural
  - *vestrum* is given only as accusative; here it is nominative
  - *caerula* (neuter accusative plural) is already right
- **Advisory:** none taken.

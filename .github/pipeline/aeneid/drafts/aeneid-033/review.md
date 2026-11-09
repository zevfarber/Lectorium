# aeneid-033 (Aeneid V.201–285) — reviewer's record

Two passes. Pass 1: every note's grammar against the form and line, Latin to `l` word by word, `l`/`i` agreement, echoes in `i`, speech marks, paragraph flags. Pass 2: all 85 lines scanned by hand against the scanner's fits (not only the fit's syllable count but each open syllable's natural quantity, since the scanner prices open vowels at 0.0 and can pick a wrong-quantity fit), then every unit re-read as edited. `t`, `ln`, `v`, `p` untouched (asserted identical to the original after the edit script); title, titleEn, part and about untouched. `units.json` edited by script in `l`, `i`, `n` only. `scan-fixes.json` extended by script: 7 new keys appended after 5.193, existing entries untouched (diff is insertions only). Nothing built: the scan stage was reproduced with `scan_latin.scan_story` plus `scan-fixes.json` (the build's own code path), and the validator's foot, syllable-count and `×` checks were run on the result: 0 UNRESOLVED, 0 MISMATCH, 0 COSTLY, `sc` on all 37 units, all 85 lines six feet. Every note is 15–140 words; `l` has the same line count as `t` in every unit. `drafts/aeneid-033/draft.py` was not touched and no longer matches `units.json` (the brief limited edits to units.json, scan-fixes.json and this file).

Severity counts: **major 9, medium 11, low 13.** (Major = a false grammatical label, an `l` or `i` that gets the sense or the referent wrong, or a scansion with wrong syllable count or quantities. Of the 9, 4 are text and 5 are scansion.)

## Major

1. **5.232–234 `l`** read "if his palms… Cloanthus and poured out prayers… had called". `ni` is `nisi`, "unless": the Latin says the dead heat would have been the result unless Cloanthus had prayed. `l` now "unless his palms to the sea stretching both Cloanthus / had poured out prayers, and the gods into vows had called:". (`i` and note were right.)
2. **5.239–241 `i`** "pushed him on his way": `euntem` is the ship (the note says so, and `l` has "her going"). `i` now "pushed the ship forward as she went", and 5.242 `i` starts "She, swifter than…", so the ship is named once and picked up by `illa`.
3. **5.242 note** called `fugit` "a perfect". The scansion (`fŭgit`, short u, with the only fit) shows a present; the perfect would be `fūgit`. The note now calls it a historic present continued by the perfect `se condidit`.
4. **5.218 note** called `ipsa fuga` "an ablative of means, 'by her very flight'". The line scans only with short `-a` in `ipsa` (ipsă fŭgā sĕcăt), so `ipsa` is nominative with `Pristis`, and `fuga` is the ablative. Note, `l` ("so herself, in flight, cuts…") and `i` ("the Pristis herself, till now last, cuts the water in her flight") now agree.
5. **Scansion 5.216** `aere` ("air", Greek ἀήρ): the scanner read ae as a diphthong and made the final -re long before `lapsa` (cost 1.6), a wrong quantity. Now ā-ĕ-rĕ, three syllables, as the published `aera`/`aere` of earlier parts. `quieto` quĭ-ē-tō. Entered in `scan-fixes.json`.
6. **Scansion 5.231** `quia` was scanned as one long syllable (qu + consonantal i + a, cost 0.0): fourteen syllables where the word has two. Now quĭ-ă (as published aeneid-009 and -030). Entered.
7. **Scansion 5.263** `Phegeus` (Φηγεύς) split into Phĕ-gĕ-ŭs: the Greek ending -eus is one diphthong, as Orpheus and Mnestheus, and Phē is long. Now Phē-geus (fifteen syllables). Entered; the note says "one syllable (Phe-geus)".
8. **Scansion 5.268** *Iamque adeo donati omnes opibusque superbi*: the scanner (cost 0.0) found a second valid fit with four wrong quantities (dŏ-nă for dō-nā, ō-pī for ŏ-pĭ). Natural quantities fit too: Iam ă-dĕ | ō dō | nā om | nēs ŏ-pĭ | bus-quĕ sŭ | per-bi. Entered.
9. **Scansion 5.282** `Aeneas` split A-e-ne-as with short ne (cost 1.2). Now Ae-nē-ās, with -tum of `Sergestum` elided into it, as 2.2 and 5.129. Entered.

## Medium

1. **5.202 note**, `furens animi`: "a genitive of respect (an old locative sense)" mixed two labels. `animi` has the form of a genitive but is a locative ("in mind", as `aeger animi`, `pendere animi`); the note now says so and adds that grammars often class it as a genitive of respect. (Drafter's doubt, resolved.)
2. **5.202–203 note**: `subit` called "a present of vividness". It is the second verb of the `dum` clause (both `suburguet` and `subit` are the present of `dum`); the note says so.
3. **5.207–209 `i` and note**: `i` "hold up the race" contradicted the note ("the race goes on without them") and the sense; `morantur` is "they are delayed, lose time". `i` now "…with loud shouting and lose time there"; the note says "they are delayed, they lose time".
4. **5.213–217 note**: "A comparison of a ship with a bird is Homeric, and doves flying from rock hollows occur in the Iliad (XXI.493 ff.)" overclaimed (the Iliad passage is a dove darting *into* a hollow rock). Now "Compare the dove of Iliad XXI.493 ff., which darts into a hollow rock; here the bird shows the speed of a ship." Also added that `aere` is trisyllabic.
5. **5.229–230 note**, `ni teneant` (drafter's doubt, resolved): the note said the subjunctive "puts the fear into an indirect form, as in Greenough's note". Nothing here is fear, and the Greenough attribution cannot be checked. Reading kept (angry at the thought that they may not keep it; `ni` = `nisi`) and the label rewritten: the subjunctive makes the possible loss a case supposed inside their feeling, so `ni teneant` is "if they should fail to keep it". `l` ("if they should not hold") was already right.
6. **5.239–240 note**: `Nereidum` called "the old genitive plural in -um". It is the regular -um of a consonant stem (Greek `Nereis`), unlike the old -um of `superum`, `divom`. Rewritten. `Phorci chorus` (drafter's doubt): the reading "the company of the Nereids and of Phorcus" is right (`Phorci` genitive singular of Phorcus, both genitives with `chorus`), and `omnis` is nominative singular with `chorus`; kept, `Phorci` label made explicit.
7. **5.258 note** began "A new paragraph." Greenough does not begin a paragraph at 258 (packet shows ¶ at 201, 210, 220, 244, 268 only, and the unit has no `p`). Removed.
8. **5.264 note** ended "The line is flagged by the scanner for a reviewer's scansion": reader-facing text mentioning the build. Replaced by what the line shows: it scans only with long first syllable in `palantes` and short -as in `Troas` before the vowel of `agebat`.
9. **5.237–238 note**: garbled sentence ("the last two spelled for 'porriciam' from 'porricio'…"). Now: "'Constituam', 'porriciam' and 'fundam' are futures; 'porricio' is the ritual word for offering entrails, where the Latin Library prints 'proiciam', 'I will throw'."
10. **5.235–238 `l`/`i` echo**: "bound by my vow" for `voti reus` is the stock rendering of several known versions. `l` now "a debtor of the vow" (the note's "liable on a vow" kept), `i` "owing you the vow I make".
11. **5.242 `l`** "toward land fled" for the present `fugit` (see major 3). `l` now "flees", continuing "hid herself" for `se condidit`.

## Low

1. **5.201 `l`** "Brought of itself" suggested `sponte`; `ipse` agrees with `casus`. Now "Brought, itself, to the men…".
2. **5.205 note**: `concussae` has `sunt` understood; added.
3. **5.206 note**: "with her bows in the air" for `pependit` was unsupported; now "caught fast with her bows on the rock".
4. **5.212 `l`** "steep seas" for `prona maria`; now "sloping seas" (as note and `i`).
5. **5.213–217 `i`**: "glides down into calm air and skims her shining way" (direction not in `aere lapsa quieto`; `liquidum` is "clear") became "then, gliding in the still air, skims her clear path".
6. **5.218–219 note**: "the threefold 'sic' is Virgil's way of letting the ship pick up speed" and "impetus ipse… without help from the oars" were unsupported; softened.
7. **5.249 `i`**: "distinctions of their own" for `praecipuos… honores`; now "special honours" (as `l`).
8. **5.254–255 `l`**: stiffness (drafter's doubt): "whom the swift-winged from Ida / aloft snatched with feet" read as if `praepes` were the subject by itself; now "like to one panting, whom the swift-winged from Ida / aloft snatched up with feet, Jove's armour-bearer, hooked;". The hyperbaton is kept.
9. **5.258 `i`**: "linked of smooth rings and triple gold thread" is not English; now "its smooth rings interlinked and triple-threaded with gold".
10. **5.259–260 `l`** (drafter's doubt, stiffness): checked word by word ("with smooth hooks linked and with gold triple-threaded / a corselet, which from Demoleos had stripped himself"). Every word is accounted for and the hyperbaton (`levibus… hamis consertam auroque trilicem / loricam`) is the pilot's practice. Kept.
11. **5.263 note**: added "'Phegeus' has the Greek ending -eus, one syllable (Phe-geus)."
12. **5.282–283 note**: "perfect participles after 'ob'" corrected to "accusatives after 'ob' with perfect participles".
13. **Scansion entries that only confirm** the scanner's fit and clear the COSTLY flag: **5.240** (Nē-rĕ-ĭ | dum Phor | cī-quĕ chŏ | rūs Pă-nŏ | pē-ă-quĕ | vir-go; no hexameter exists with short -us of `chorus`, so it is lengthened in the arsis at the caesura; `Nereidum` four syllables) and **5.265** (Dē-mŏ-lĕ | ōs cūr | sū pā | lān-tēs | Trō-ăs ă | gē-bat, one anomaly: short -as of `Troas` before the vowel). The reasons are in `scan-fixes.json`.

## Scan-fixes added (7)

`5.216`, `5.231`, `5.240`, `5.263`, `5.265`, `5.268`, `5.282`, appended in that order after `5.193`, each with `sc` and `why`, in the existing format.

## Checked and kept (no change)

- **Speech marks**: Cloanthus's prayer (235–238) has “ at the head of `t`, `l`, `i` of its unit and ” at the end of all three. It is a single unit; no other speech in this part.
- **Paragraph flags**: `p: true` on 201, 210, 220, 244, 268 only, matching the packet; each of those notes opens "A new paragraph."
- **Misprint 5.215** `ana` for `arva`: `t` as printed, note opens "The print has…" (the precedent of 5.135/181). The scan `a–na⏑` has the same syllable count and quantities as `arva`.
- **5.231 `i`** "strength is theirs because they seem to have it": no echo of the famous renderings of *possunt, quia posse videntur* ("they can because they think they can" and its kin); it also keeps the seeming. Kept. All other `i` lines read for echoes; the two distinctive ones were 5.235–238 (above) and 5.241 ("pushed him on his way", changed for sense).
- **`Gyan`, `Simoënta`, `Chimaeram`, `Cloanthus`, `Mnestheus` (210, 218)**: Mnes-theus with eu one syllable, Clŏ-ān-thus, Si-mŏ-ën-ta, Gyan with long -an: scanner right. 5.223 `Gyan ipsamque`: right. 5.201 `casus honorem`, 5.233, 5.234 `divosque in vota` (-que elides, dī-vos), 5.252, 5.254 `Ida` (Ī-da, long I; `praepes` with short -es, cost 1.0 is correct): scanner right, no entries.
- **Scanner fits kept on the metre's say-so** (the only fit, each needing one lengthening or a quantity I could not confirm): 5.208 `trudes` (tru short), 5.217 `iter` (-ter long in the arsis), 5.239 `imis` (long i), 5.253 `veloces` (long vē), 5.256 `nequiquam` (nēquīquam), 5.233 `utrasque` (long u before tr), 5.280 `navis se` (-vis long in the arsis), 5.284 `datur` (-tur long at the caesura), 5.285 `genus Pholoë` (-nus long before Ph).

## Unresolved (for QUESTIONS.md)

1. **5.261** `victor apud rapidum Simoënta sub Ilio alto`. The scanner's fit (cost 0.3) is a valid hexameter with `sub` long, `I` short (Ĭ-lĭ(o)) and `-ta` of `Simoënta` long, while the published parts scan `Ilium` with long Ī everywhere. Fits with natural quantities exist, but each needs a hiatus before `alto` (Ī-lyō with synizesis, or Ī-lĭ-ŏ with the final -o shortened, five dactyls) which I cannot confirm from L&S or Conington without the commentary at hand. Not entered; left as the scanner has it. The owner may want one reading of `Ilio` across the poem.
2. **5.208 `trudes`**: only the short-u reading fits; L&S's quantity for `trudis` not confirmed.
3. **5.239 `imis`**: only the long-i reading fits; the quantity of `imus` (ĭmus/īmus) not confirmed.
4. **5.240 `Nereidum`**: published 3.74 scans the word Nē-rē-ī-dum (all long), which cannot fit here; 5.240 needs Nē-rĕ-ĭ-dum (or Nē-rēi-dum, three syllables, equally good). Not harmonised.
5. **The scanner's blind spots found in this part, for the scanner's notes**: it scans `quia` as one syllable at cost 0.0 whenever the line fits that way, picks wrong-quantity fits where open vowels are free (5.268), and does not know `aere` = aër.

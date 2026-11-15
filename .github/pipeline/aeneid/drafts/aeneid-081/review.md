# Review — aeneid-081 (Aeneid X.791–908), adversarial reviewer

**Severity counts: major 4, medium 6, low 24 (all in pass 1; pass 2 found nothing new). Refused or upheld without change: 12. Scan-fixes entries added: 14 (10 Ae- lines, 1 line with wrong quantities, 1 hypermetric line, 1 half-line, 1 carrier).**

All four majors are scansion findings. Three of them cover lines the packet did not flag.
- **M1: initial Ae- split.** The scanner (cost 1.2–1.5, not flagged) split *Ae-* in 10 lines: 798, 802, 809, 816, 826, 830, 863, 873, 874 and 896.
- **M2: wrong quantities with the right count at 891.** The scanner fit *bellatoris equi* at cost 0.0.
- **M3: 895 is hypermetric.** The scanner fit it wrongly at cost 0.6, reading *Troes* as one syllable and *Latī-* as short. The notes of 895 and 896 now say the line is hypermetric.
- **M4: half-line 876**, the packet's only flag. It is entered with 875 as a carrier, because a unit with an unresolved line gets no `sc` at all.

## How the review was done

**Pass 1** covered all 63 units word by word. I checked:
- `l`, `i` and `n` against the Latin
- every grammatical label, every "framing" claim and every elision list
- every cross-reference, and every attribution I could check
- the speech marks, the Latin Library variants, `about`, `title`, `part`, `titleEn`, the `p` flags and the bracketed line 872

**Sources.** The Latin, the pinned source, and memory of the public-domain references (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

**Elision lists.** I checked every line for a vowel or *-m* before a vowel or *h*. Two lists were wrong (D1, D2 below). All the others are right, including:
- *tanto (e)st* 792 and *ulla (e)st* 861, given as prodelision
- *nequ(e) adhuc* 855
- *Sci(o) acerba* 904
- *iuguloqu(e) haud* 907

The cross-line elision *Latiniqu(e) Advolat* (895–896) was missing and has been added.

**Speech marks.** `t`, `l` and `i` each have 8 “ and 8 ”, and a script asserts this. In `l`, `i` and `n`, each speech is closed in its own unit:

| speech | opens | closes (`l`, `i`) | `t` closing mark |
|---|---|---|---|
| Aeneas | 811 | 812 *tua.* (unit 811) | head of unit 812 (misprint) |
| Aeneas | 825 | 830 *cadis.* (unit 829) | head of unit 830 (misprint) |
| Mezentius | 846 | 856 *Sed linquam.* | head of unit 856b *Simul…* (misprint) |
| Mezentius | 861 | 866 | 866 |
| Aeneas | 875 | 876 | 876 |
| Mezentius | 878 (unit 878, mid-line) | 882 *prius.* (unit 881) | head of unit 882 (misprint) |
| Aeneas | 897 (unit 896) | 898 *animi?* (unit 896) | head of unit 898 (misprint) |
| Mezentius | 900 | 906 | 906 |

**About, title, part, titleEn and p.** All right.
- *Mors Lausi et Mezentii* uses the right genitives.
- `p` is set at 791 and 833, Greenough's only two paragraphs here, and both units start at the line start.
- 872 is printed in [ ] in `t`, `l` and `i`, and the note of unit 870b says it is spurious and repeats XII.668.

**Cross-references checked in the pinned source.** All are right:
- 785–786 (*imaque sedit / inguine*)
- IX.446–449 (*Fortunati ambo*)
- I.378 (*Sum pius Aeneas*)
- X.495–500 and X.505–506 (*impositum scuto referunt Pallanta*)
- XI.688–689 (*telo cecidisse Camillae*)
- VIII.481–495 and VIII.494–495 (*regem ad supplicium… reposcunt*)
- VII.648 (*contemptor divom Mezentius*)
- XII.666–668 (the same *aestuat ingens… virtus*)
- VIII.608–731 (the shield, from Venus's arrival to *fata nepotum*)
- 810 *increpitat*, as the note of 900 says

**Attributions to texts outside the source.** These come from my memory and agree with the drafter's: Iliad 16.856–857, 22.362–363, 18.23–24, 22.414, 17.426–440, 19.400–403, 8.185–197, 8.81–86 and 22.338–343; Lucretius 1.123. I softened one claim (L9). They are still unchecked against a text (see For the owner).

**Pass 2** re-read every field pass 1 edited, in full, and found nothing new. It re-checked the following by script:
- `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` against a copy taken before any edit: unchanged
- `l` has as many lines as `t` in every unit, and no `i` has a line break
- notes run 41–109 words
- the speech-mark layout and counts above
- no translator's name appears anywhere

**What was edited, and how.**
- **`units.json`** was edited only by `review_edits.py`: 48 string replacements, each old string asserted to occur exactly once in its field. The file is written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically before the edit.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to only by `add_scan_fixes.py`, which keeps the 963 earlier entries unchanged and in order (977 now).
- **`scan_check.py`** is 080's helper with the part id changed. With the fixes applied, a replica of the build's scansion step and the validator's metre check gives `sc` on all 63 units, no report left, no metre failures and no misaligned units.
- **Build and validator not run.** The build has no dry-run mode: it always writes `aeneid-081.json`, the glossary and `stories.json`. I called it once with no arguments by mistake, and it stopped at line 14 on the missing part id, before it reads or writes anything.

## Scansion

I hand-scanned all 118 lines and compared them syllable by syllable with the scanner.

**Packet flag:** 876 (UNRESOLVED) is a half-line, entered with 875 as a carrier (M4).

**Unflagged lines that are wrong (12):**
- **Initial Ae- split (cost 1.2):** 798 *Aeneae*, 802 *Aeneas*, 809 *Aeneas*, 816 *Aeneas*, 826 *Aeneas*, 830 *Aeneae*, 863 *Aeneae*, 874 *Aeneas*, 896 *Aeneas*.
- **Initial Ae- split (cost 1.5):** 873 *Aenean*.
- **Wrong quantities with the right count:** 891 *bel-lā-tō-rĭs ĕ-quī*. The scanner had *-la-* and *-to-* short and *-ris* and *e-* long.
- **Wrong scansion of a hypermetric line:** 895 *Troesque Latinique*.

**Lines hand-checked and right:**
- **Greek eu:** 866 *Teucros*, one syllable by synizesis (cost 1.5).
- **Consonantal i after a prefix:** 801 and 891 *conicio* (con- long), 858 *deiectus*, 894 *eiecto*.
- **Consonantal u:** 867 *consueta* (cost 1.5).
- **Other points:** 804 *diffūgit* (perfect); 886 *Troïus* (three syllables); 904 *Sci(o) acerba*. No hiatus and no *cui* in the part.

**Cosmetic syllable division only (no entry):** the scanner prints 860 *A–dlo*, 885 *ads–tan*, 905 *cums–ta* and 907 *ins–ci*. The quantities are right; 080 made no entries for this either.

| key | sc | reason (short) |
|---|---|---|
| 10.798 | 1Ae–ne–2ae– su⏑bi⏑3it–‖ mu–4cro–nem ip–5sum–que⏑ mo⏑6ran–do× | Ae- one syllable; *Aeneae* does not elide before *subiit*; 14 syllables |
| 10.802 | 1mis–si⏑li⏑2bus– Fu⏑rit⏑ 3Ae–ne–4as–‖ tec–5tus–que⏑ te⏑6net– se× | Ae-; 15 |
| 10.809 | 1Ae–ne–2as– nu–3bem–‖ bel–4li– dum– 5de–to⏑net⏑ 6om–nis× | Ae-; 13 |
| 10.816 | 1per– me⏑di⏑um 2Ae–ne–3as–‖ iu⏑ve⏑4nem– to–5tum–que⏑ re⏑6con–dit× | Ae-, *medi(um)* elided; 15 |
| 10.826 | 1quid– pi⏑us⏑ 2Ae–ne–3as–‖ tan–4ta– da⏑bit⏑ 5in–do⏑le⏑ 6dig–num× | Ae-; *tantā* ablative; 15 |
| 10.830 | 1Ae–ne–2ae– mag–3ni–‖ dex–4tra– ca⏑dis⏑ 5In–cre⏑pat⏑ 6ul–tro× | Ae-; 14 |
| 10.863 | 1et– ca⏑put⏑ 2Ae–ne–3ae–‖ re⏑fe⏑4res– Lau–5si–que⏑ do⏑6lo–rum× | Ae-; 15 |
| 10.873 | 1At–que hic– 2Ae–ne–3an–‖ mag–4na– ter– 5vo–ce⏑ vo⏑6ca–vit× | Ae- (Greek acc.); 13 |
| 10.874 | 1Ae–ne–2as– ag–3no–vit⏑ e⏑4nim–‖ lae–5tus–que⏑ pre⏑6ca–tur× | Ae-; 14 |
| 10.875 | scanner's own fit | carrier for the half-line 876; 16 |
| 10.876 | 1in–ci⏑pi⏑2as– con–3fer–re⏑ ma⏑4num× | Half-line; 9 syllables |
| 10.891 | 1bel–la–2to–ris⏑ e⏑3qui–‖ ca⏑va⏑ 4tem–po⏑ra⏑ 5co–ni⏑cit⏑ 6has–tam× | quantities of *bellatoris equi*; 16 |
| 10.895 | 1Cla–mo–re 2in–cen–3dunt–‖ cae–4lum– Tro–5es–que⏑ La⏑6ti–ni×que | hypermetric, *-que* elided into *Advolat*; 13 count |
| 10.896 | 1Ad–vo⏑lat⏑ 2Ae–ne–3as–‖ va–4gi–na–que 5e–ri⏑pit⏑ 6en–sem× | Ae-; 14 |

**Entry format.**
- Every `why` gives the scansion foot by foot. The script checks the syllable count it states against the `sc`.
- 876's `why` begins "Half-line", so the validator applies its half-line rule (feet 1–4, one ×).
- 895 follows the 781 pattern: the final *-que* is left unmarked after the ×.
- Every entry passes the build's word-match rule and the validator's metre rule; `add_scan_fixes.py` asserts both.

## Changes (pass 1)

**Major (scansion):** M1–M4 above. These changed `scan-fixes.json` and the notes of 895 and 896, and nothing else.

**Medium**
- **D1. Note 796–799, elision list.** It listed *Aenea(e) subiit*, but *s-* is a consonant, so there is no elision. Removed.
- **D2. Note 803–806, elision list.** It listed *arc(e) viator*, but *v-* is a consonant. The note now says that *arce viator* does not elide.
- **D3. Note 844–845.** It called *corpore* (in *corpore inhaeret*) a "dative with the compound". *corpore* is ablative; *inhaereo* takes the dative or the ablative.
- **D4. Note 815–816.** It said that "the word order sets 'Aeneas' at the head of the line". Line 816 begins *per medium*. The note now says that *Aeneas* sits inside *per medium… iuvenem*.
- **D5. Rule-5b placement at all five misprints (812, 830, 856, 882, 898).** This is now the same as 077, 078 and published 080 (`aeneid-080.json` 742/744 and 772/776):
  - The note of the unit where the speech closes (811, 829, 856a, 881, 896) now opens "The print has 'X', the closing speech mark joined to the next word, a misprint for 'Y', corrected here…".
  - The next unit, whose `t` begins with the stray ”, now opens "The closing speech mark printed at the head of this unit belongs to Aeneas's / Mezentius's speech (see the note before)."
  - The drafter had them the other way round, which is the placement 080's reviewer had already changed. `t` is untouched.
- **D6. Notes 895 and 896, hypermetric line.** The line is now described as hypermetric (as 781), and the cross-line elision *Latiniqu(e) Advolat* is listed.

**Low: labels, wording and attributions**
- **L1. Note 796.** "Aeneas rising on his toes" was invented. It now reads "rising up".
- **L2. Note 803.** Added that *diffugit* is perfect (the metre needs *fū*), of what always happens.
- **L3. Note 825.** "speaks to the dead boy" is now "the dying boy" (*morientis*, 821).
- **L4. Note 829.** *infelix* is now "nominative with the 'you' of 'solabere', where English would use a vocative", in place of "in effect a vocative".
- **L5. `i` 830.** *Increpat* was rendered "called on". It is now "rebuked… for hanging back", matching `l` "chides" and the note.
- **L6. Note 835.** *aerea… galea* is now "split across the line-end", not "spread across the line".
- **L7. Notes 844 and 867.** *ambas… palmas* is now "split across the line-end", not "framing the line-end". *iaculis… acutis* is now "enclosing the verb", not "framing the second half of the line".
- **L8. 839, *multumque remittit / qui revocent*.** The note now takes *multum* first as an adverb ("again and again"), with the antecedent of *qui* left out, which is the usual reading as I remember Conington. It gives *multos* as the alternative. `l` now reads "and often he sends / men who should call him back", and `i` reads "sent messengers time after time".
- **L9. Note 849–850.** "Many editors read *exilium*" is now "Some editors", since I can't check it.
- **L10. Note 888–891, Iliad 8.81–86.** Paris's arrow does not "bring Nestor's chariot down"; the wounded horse throws the team into confusion. Reworded.

**Low: echo recasts in `i`** (L11–L24, one each). I rebuilt each of these from the Latin, because the drafter's wording was close to the usual phrasing of the well-known versions:
- **811–812:** "Doomed boy, where are you rushing, attempting what is beyond your strength? Your devotion deceives you, and you are off your guard."
- **817–820:** "…slipped away through the air to the shades and forsook the body."
- **821–824:** "But when Anchises' son saw the dying boy's features…" (drafter: "the look on the dying boy's face")
- **825–826:** "Pitiable boy, what can Aeneas the dutiful offer you now for glory like yours?…"
- **827–828:** "The armour that was your delight, keep it; it is yours…"
- **855:** "And here I am, alive, not yet gone from mankind and the daylight."
- **856:** "But go I will."
- **861–862:** "Rhaebus, our life has been a long one, if any mortal thing can be said to last long."
- **879:** "There was one road only to my ruin, and you have taken it."
- **880:** "Death does not frighten me, and there is no god I spare."
- **901–902:** "Killing is no sin…"
- **903–904:** "I make one plea, by whatever grace a beaten enemy may still claim…"
- **904–906:** "…grant that I may lie with my son, his companion in the grave."
- **907–908:** "…knowing what he did, took the sword into his throat; his life went streaming out over the fields with the welling blood."

## Changes (pass 2)

None needed.

## Refused or upheld without change

1. **The drafter's rule-5b placement.** Not kept. 077, 078 and published 080 put the print's reading in the unit where the speech closes (D5). The owner was asked about this placement in 080's review; until he rules, consistency wins.
2. **829–830 `i`, "the hand that brings you down is the hand of great Aeneas".** Kept. It is not the usual phrasing.
3. **841–842 `i`, "a great figure, brought down by a great wound".** Kept. It is generic and follows the Latin's repetition.
4. **846–848 and 848–849 `i`.** Kept. Any close rendering of these questions has this shape, and neither borrows a distinctive phrase.
5. **900 `i`, "Bitter enemy, why do you taunt me and threaten me with death?"** Kept. It is literal, and nothing more distinctive is available.
6. **858 note, *decus illi* as a "dative of possession".** Kept. It is defensible with *erat*; reference would also do.
7. **875 note, *incipias* as "jussive".** Kept. The wish could be called optative, but the gloss "may you begin" is right either way.
8. **896 note, *super haec*.** Kept. It already gives both "over him" and "besides".
9. **850 *exitium*.** Kept as printed, with the note's mention of *exilium* softened (L9). It is a doubtful reading, not a misprint.
10. **857 *quamvis dolor… tardet*.** Kept, with the Latin Library's *quamquam vis… tardat* noted as the drafter had it.
11. **Cosmetic syllable divisions at 860, 885, 905 and 907.** No entries made (see Scansion).
12. **Advisory.** None added (see For the owner).

## For the owner

- **Rule-5b misprints.** There are five, each a closing mark joined to the next word: 10.812 `tua. ”Nec`, 10.830 `cadis. ”Increpat`, 10.856 `linquam. ”Simul`, 10.882 `prius. ”Dixit` and 10.898 `animi? ”Contra`. The publishing run should add the QUESTIONS.md entry that rule 5b asks for; the reviewer may not touch QUESTIONS.md. Note placement follows 077, 078 and 080 (D5); say if you prefer the other placement.
- **Doubtful readings.**
  - 850 *exitium* (some editors *exilium*; which editors could not be checked).
  - 857 *quamvis dolor… tardet* (Latin Library *quamquam vis… tardat*).
  - 908 *in arva* (Latin Library *in arma*).
  - 796 *prorupit* (Latin Library *proripuit*) and 801 *proturbant* (Latin Library *perturbant*).
  - 839 *multum* is now read as an adverb (L8), with *multos* given as the alternative.
- **Bracketed line.** 872 is kept in [ ]. The Latin Library omits it.
- **Half-line and hypermetric line.** 876 *incipias conferre manum* is a half-line, and 895 is hypermetric (*Latiniqu(e) Advolat*). 895 is in the usual list of Virgil's hypermetric lines as I remember it; I could not check that list.
- **Unchecked attributions from memory.**
  - Iliad 16.856–857, 22.362–363, 18.23–24, 22.414, 17.426–440, 19.400–403, 8.185–197, 8.81–86 and 22.338–343.
  - Lucretius 1.123 (*simulacra modis pallentia miris*).
  - The *multum* reading credited to Conington (L8).
  - The leftward circling at 885 explained as keeping the throwing arm toward Aeneas.
- **Advisory question.** At 907 Mezentius takes the sword in his throat willingly (*iuguloque haud inscius accipit ensem*). It is a death he consents to at an enemy's hand after asking for burial, not a suicide by his own hand, and it is told in two lines without lingering. Under "Book X–XII battle narrative: ordinary killing earns nothing", no advisory was added. Rule whether a consented-to death like this falls under the still-open question on Dido's suicide.
- **Build.** Not run (no dry-run mode). Build from `units.json` as it stands. `make_units.py` holds the pre-review strings.

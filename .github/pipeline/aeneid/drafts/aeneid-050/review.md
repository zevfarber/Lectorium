# Review — aeneid-050 (Aeneid VII.107–194), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 34 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference, and every historical or mythological claim. I also checked the speech marks and the rule-5b misprint notes (7.116, 7.120–121, 7.170), the Latin Library variant that changes the sense (7.129 *exiliis*/*exitiis*), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened. Every in-poem cross-reference was checked against the pinned source:
- 2.293 (Hector commends the Penates), 2.692–694 (thunder after Anchises's prayer)
- 3.94–96 and 3.167 (the ancient mother; *hinc Dardanus ortus*), 3.255–257 (Celaeno), 3.394 (Helenus)
- 1.724 (*crateras… statuunt et vina coronant*), 1.755 and 5.626 (the seventh summer), 5.545–603 (the Game of Troy)
- 7.10–24, 7.27, 7.37, 7.48, 8.128 (*vitta comptos… ramos*), 9.43 (the camp in Book IX)
- *mensa* through the whole poem: no prophecy of the tables is spoken by Anchises anywhere, as the notes say.

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 88 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×; the half-line 129 (its `why` begins "Half-line") against the validator's hemistich rule (feet 1..k, k < 6, one ×). Each `why` that gives a syllable count was checked against its entry by script. A replica of the build's scansion step with all fixes applied gives an empty scanner report (both COSTLY flags and both UNRESOLVED lines cleared), and every line passes the validator's check.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 34 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words (longest: unit 2, 138, unchanged; unit 27 is now 127).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 126 insertions, 0 deletions, trailing newline kept.

**Speech marks.** Iulus, 116: one unit, “ … ” in all three layers. Aeneas, 120–134: “ on the first unit (*Salve*), ” on the last (after *mensis.*); Anchises's words inside it (124–127) carry no inner marks, as Greenough prints none. `t` has 3 “ and 2 ”, because the print's “ before *vosque* (121) stands for a closing mark; `l` and `i` each have 3 “ and 3 ”, as at 6.46/6.52 (aeneid-040, published). The validator will warn (not fail) on `t`.

**Severity counts: major 5, medium 8, low 15 (14 in pass 1, 1 in pass 2). Refused findings: 22. Scan-fixes entries added: 11.**

## Changes — pass 1

### Major
1–5. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.124**: the scanner had *cum tĕ nă | tē fā*. *Tē* (pronoun) and *nāte* are long, *fămes* short. Hand scansion: cum tē | nā-tĕ fă | mēs ig | nō-t(a) ad | lī-tŏ-ră | vec-tum.
   - **7.174**: the scanner had *ō-mēn | ē-răt hŏc*. Hand scansion: rē-gĭ-bŭs | ō-mĕn ĕ | rāt hōc | il-līs | cū-rĭ-ă | tem-plum. The *-at* of *erat* is lengthened in the arsis at the main caesura and the sense pause (as *sēsē* at 1.314); the only fit (see the doubtful list).
   - **7.175**: the scanner had *dēs ē | pū-lĭs hĭc*. Hand scansion: hae sā | crīs sē | dēs ĕ-pŭ | līs hīc | ar-yĕ-tĕ | cae-sō.
   - **7.178**: the scanner made *antīqua* short in the middle, *Ītalus* long, and elided *cedro*. Hand scansion: an-tī | qu(a) ē cē | drō Ĭ-tă | lus-quĕ pă | ter-quĕ Să | bī-nus — hiatus after *cedro* at the pause; with the elision there is no fit. *Ĭtalus* as *Ĭtalis* 1.252.
   - **7.193 *Teucros***: the scanner split Teu- into Te-u. Hand scansion: sē-dĕ sĕ | dens Teu | crōs ad | sē-s(e) in | tec-tă vŏ | cā-vit.

### Medium
6–9. **Scansion: the packet's flags.**
   - **7.107** (COSTLY 3.2): the scanner split *Aeneas* into A-e-ne-as and read *Iulus* as two syllables. Hand scansion: Aē-nē | ās prī | mī-quĕ dŭ | cēs et | pul-chĕr Ĭ | ū-lus (Iulus trisyllabic, as the 1.556 and 5.570 entries).
   - **7.116** (COSTLY 3.5): *Iulus* again read as two syllables, with a spondaic fifth foot. Hand scansion: Heus ĕ-tĭ | am mēn | sās con | sū-mĭ-mŭs | in-quĭt Ĭ | ū-lus.
   - **7.129** (UNRESOLVED): half-line, ex-ĭ-lĭ | īs pŏ-sĭ | tū-ră mŏ | dum, entered as a hemistich like 5.574, 6.94 and 6.835. **7.128** is entered as a carrier line (the scanner's own fit), because the unit *haec nos… modum* runs on into 129 and the build gives no `sc` to a unit with an unresolved line.
   - **7.160** (UNRESOLVED): hypermetric, iam-qu(e) ĭ-tĕr | ē-men | sī tur | rīs ac | tec-tă Lă | tī-nō(rum), *-rum* elided into *ardua*, in the format of 1.332 and 1.448 (`La⏑6ti–no×rum`). **7.161** is entered as a carrier line (the scanner's own fit), for the same reason.
10. **Note 122–123, a wrong label**: "'Namque'… stands late in its clause as the fifth word". *Genitor mihi talia namque*: it is the fourth. Corrected.
11. **l 130–132, wrong agreement**: "with the first, glad, light of the sun" made *laeti* agree with *lumine*. It is nominative plural with the subject ("we"), as `i` ("let us gladly") has it. `l` now reads "Therefore come, and, glad, with the first light of the sun,"; the note adds "'laeti', 'glad', is nominative plural with the subject, 'we'."
12. **Note 166–168, a wrong cross-reference**: "'cum inversum' again (as at 28)". The *cum* is at 7.27 (*cum venti posuere*). Now "(as at 27)".
13. **l 189–191, participles misparsed**: "with her golden striking wand and changing with drugs" made *percussum* and *versum* active and agreeing with Circe. They are perfect passive and agree with *quem* (Picus). `l` now reads "with her golden wand struck, and changed by drugs," (see P2-1); the note adds "'percussum' and 'versum' agree with 'quem'".

### Low
14. **Note 107–111**: added that *Iulus* is three syllables (I-u-lus) and *Aeneas* three (Ae-ne-as), to go with the scan fixes at 107 and 116.
15. **Note 128, an unverifiable attribution**: "(Allen & Greenough's imperfect of a fact just realised)" cut; the note now reads "'this was, it turns out, that hunger', an imperfect of sudden recognition." The construction is right; the section reference could not be checked.
16. **Note 141–143**: "'clarus'… 'plain to hear', and thunder from a clear sky was taken as an unmistakable sign" joined a reading of *clarus* as sound to a claim about a clear sky that the line does not make (Jupiter in fact shows a cloud). Now "'clarus' agrees with 'pater' and is predicative, 'clear', 'plain to hear' (some take it as 'in brightness')."
17. **Note 150–151, Livy hedged**: "where, the story ran, Aeneas vanished from among men at the end of his life (Livy 1.2)" is now "by which, in the later story, Aeneas's life on earth ended; Livy (1.2) puts his resting-place beside it." Livy has him *situs… super Numicum flumen*; the vanishing is not Livy's.
18. **Note 150–151, label**: "'Thybrim' is the Greek accusative" — the *-im* is the Latin i-stem ending used for Greek names in *-is* (049, item 19, *Mephitim*). Now "the accusative, in '-im', of 'Thybris', the Greek-derived poetic name of the Tiber."
19. **Note 157–159**: "'Humili… fossa' frames the line" (it does not: *Ipse* stands first). Now "goes round 'designat moenia'".
20. **Note 160–161**: "'Tecta… ardua' frames the line-end" is now "is split across the line-end".
21. **l 162–165**: "or sharp ones they bend, bows" disagreed with the note ("'strong' bows") and `i` ("tough bows"). Now "or strong ones they bend, bows,".
22. **Note 173–176**: added "'ariete' is three syllables, 'ar-ye-te'. In 174 the '-at' of 'erat' is scanned long at the main pause, before 'hoc'."
23. **Note 177–179**: "'Veterum… avorum' frames the line" (*veterum* is the third word) is now "spans the line".
24. **Note 177–179**: added "'cedro' is not elided before 'Italusque' (hiatus, at the pause)", to go with the 7.178 fix.
25. **Note 180–182**: "'Martia… volnera'… frames the line" (*passi* follows) is now "spans the line".
26. **Note 183–186**: added that the first *-que*, in *spiculaque*, is scanned long before *cl-* (the scanner's fit is right here; see the doubtful list).
27. **Note 192–194**: "'Placido… ore'… frames the line" is now "goes round 'prior edidit'"; added "'Teucros' is two syllables, 'Teu-cros'", to go with the 7.193 fix.

## Changes — pass 2
- **P2-1 (low)**: in `l` 189–191, the pass-1 wording "with her golden wand struck and changed with drugs," read as if Circe did the striking with "changed" dangling; it now reads "with her golden wand struck, and changed by drugs," matching the note's "changed by drugs".

## Scan-fixes entries added (11)
Appended at the end of `scan-fixes.json`, each with its reason:
- 7.107, 7.116 (packet COSTLY flags)
- 7.124, 7.174, 7.175, 7.178, 7.193 (no flag, wrong quantities)
- 7.129 (half-line) with carrier 7.128
- 7.160 (hypermetric) with carrier 7.161

Each matches its line's words under `WORD_RE`. Each full line has six feet, five –⏑⏑/–– feet then –×, 14–15 syllables and one ×; 7.129 has feet 1–4 and one ×, its `why` beginning "Half-line" as the validator requires. In the replicated build all 11 apply, the scanner report is empty, and all 88 lines pass the validator's check.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: *aethere* (143) is right. *Aeneas* (107) is fixed.
- **Greek eu**: *Teucris* (155) is right, Teu- one syllable. *Teucros* (193) is fixed. *Heus* (116) is one syllable in the fix.
- **Consonantal i after a prefix**: *subiciunt* (110) is sub-jĭ-cĭ-unt, four syllables, – ⏑ ⏑ –; the scanner's division *su–bi⏑ci⏑unt–* is cosmetic, as *adiungi* in 049. *coniunx* (189) is con-iunx, two syllables, right. Also right: *Iuppiter* (110), *Troiae* (121), *Iovi* (133), *Iovem* (139), *Troiana* (144), *iubet* (154), *iuvenes* (161), *iuventus* (162), *Ianique* (180).
- **Synizesis**: *deinde* (135) two syllables, right, and the note says so.
- **Hiatus**: only 7.178 (fixed). Every other vowel meeting is an ordinary elision; *patria est* (122) is prodelision, handled right by the scanner.
- **Others checked and right**: *ădōrea* (109), *Cĕrĕāle* (111), *pēnūria*, *ădēgit* (113), *māla* (114), *Anchīsā* abl. (152), *ōrātōres* (153), *crātēras* (147), *Nŭmīci* (150), *dīditur* (144), *cŭpīdine* (189), *relĭgione* with long *rē-* (172), *ĕquum* (189), *ēdidit* (194).

## Doubtful quantities entered on the only fit
- **7.174 *erat***: final *-at* lengthened in the arsis at the main caesura before *hoc*. With natural quantities there is no fit (feet 1–3 have eight syllables, so the seventh must be long). UNCONFIRMED against an edition.
- **7.178 hiatus after *cedro***: the only fit; with elision there is none.
- **Scanner's fits, no entry**: *ā-* of *agrestibus* (111) before *gr*, *ā-* of *acris* (164) before *cr*, *sā-* of *sacris* (175, 183) before *cr*, *pā-* of *patres* (176) before *tr* — each long by position before stop and liquid, the only fit in each place. *spiculaque* (186): *-que* lengthened in the arsis before *cl-*; no other fit.

## Refused findings
- **R1 — Hesiod, *Theogony*, Earth after Chaos** (unit 135–138): kept. Theogony 116–117 (πρώτιστα Χάος γένετ', αὐτὰρ ἔπειτα Γαῖ'…); the note says "among the first beings after Chaos", which is exact.
- **R2 — Picus and Canens in Ovid, Met. 14** (unit 189–191): kept, as in 049 (R17). Circe loves Picus, is refused for Canens and turns him into a woodpecker.
- **R3 — "The discrepancy is usually counted among the places Virgil left unrevised"** (unit 116–117): kept; it is hedged, and the in-poem facts (Celaeno 3.255–257, Helenus 3.394, no Anchises) are verified.
- **R4 — 'pressit', "both readings are old"** (unit 117–119): kept; both are the ancient explanations (checked it / kept it close).
- **R5 — 'Haec' agreeing with 'patria'** (unit 122): kept; a demonstrative subject takes the gender of the predicate noun (A&G 296.a).
- **R6 — "seven years of wandering"** (unit 122): kept; 1.755 *septima… aestas*, 5.626 *Septuma… aestas*.
- **R7 — 3.94–96 and 3.167 for Italy as the ancestral land**: verified (*antiquam exquirite matrem*; *hinc Dardanus ortus*).
- **R8 — the misprints at 116, 120–121 and 170**: kept as rule-5b corrections, each note opening with the print's reading. 116 follows 7.68 (published 049); 121 follows 6.46/6.52 (aeneid-040, published); 170 *ingens. centum* splits subject from verb, so only one reading is possible.
- **R9 — any other misprint**: none found in 107–194. *Heus !* is part of the 116 note.
- **R10 — Latin Library variants**: only 7.129 *exitiis* changes the sense, and the note says so. *fascis*, *uulnera*, *diuum* are orthography or morphology.
- **R11 — *subiciunt* (110) and *coniunx* (189)**: the scanner's division is cosmetic; quantities and syllable counts are right. No entry.
- **R12 — i 122 "here is our home, this is our country"**: kept; the plain literal sense of five words, not a distinctive version.
- **R13 — i 116 "Look — we are even eating our tables!"**: kept; literal, not a known version's turn.
- **R14 — `l` "says" / `i` "said" for *inquit*, *ait* (116, 121)**: kept; both tenses are right for these verbs.
- **R15 — `l` 148 "her first torch" against the note's "its torch"**: kept; `l` follows the feminine *dies*, the note and `i` follow English.
- **R16 — 'crown the wine', two explanations** (unit 146–147): kept; both are the standard ones (Servius; Homer's κρητῆρας ἐπεστέψαντο).
- **R17 — hendiadys *radiis… lucis et auro*** (unit 141–143): kept.
- **R18 — 'currus' for the horses** (unit 162–165): kept; *domitant… currus* needs it.
- **R19 — olive boughs wound with wool** (unit 152–155): kept; 7.418 and 8.128 (*vitta comptos… ramos*) in the source.
- **R20 — the camp besieged in Book IX** (unit 157–159): verified, 9.43 *castra… aggere muros*.
- **R21 — 'quo… condant' as a relative of purpose** (unit 144–145): kept; the label is accurate enough for a reader, and the sense "the day on which they were to found" is right.
- **R22 — `title`, `titleEn`, `part`, `about`**: our own, borrowing no translation's heading; the summary is accurate. Unchanged.

## For the owner (QUESTIONS.md)
- **Misprints to record (no emend list for the Aeneid)**: 7.116 `“Heus ! etiam mensas consumimus, ”inquit` → `“Heus! etiam mensas consumimus,” inquit`; 7.121 `“vosque, ait, O fidi` → `vosque,” ait, “O fidi`; 7.170 `ingens. centum` → `ingens, centum`. In each case `t` is as printed, and `l`/`i` give the reading.
- **The “…ait pattern** (6.46, 6.52, now 7.121): each time the print sets “ at the head of the line where *ait* interrupts a speech. Three cases in the same shape suggest an encoding habit (a closing mark encoded as an opening one) rather than scattered misprints; the owner may want to rule once. Meanwhile it is treated as a misprint, following the published 6.46/6.52. `t` therefore has one more “ than ” in this part (validator warning only).
- **Doubtful quantities on the only fit**: 7.174 *erăt* lengthened at the caesura before *hoc*; 7.178 hiatus *cedro, Italusque*. Neither checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-050/make_units.py` still holds the drafter's strings; re-running it would discard this review.
- **From memory, worded as attributions**: Livy 1.2 (Aeneas by the Numicus), Hesiod *Theogony* 116–117, Ovid *Met.* 14 (Picus and Canens). None was checked against a text in this run.

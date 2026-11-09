# Aeneid — questions for the owner

Open:

1. **Approve the pilot?** aeneid-001 (I.1–101) is live. If approved, add `aeneid` to `.github/pipeline/queue.txt`
   (after `beowulf`, or wherever you want it) and the shared routine continues the poem from aeneid-002.
2. **Edition: Greenough (1881), not Hirtzel (1900).** Hirtzel could not be fetched (no reachable machine-readable
   copy). Greenough is the Perseus text and public domain. Meanwhile: proceeding on Greenough. Switching later means
   re-archiving and re-issuing published parts.
3. **Audio for the pilot.** Pushing a new Latin part does not build its audio; the daily sweep reaches the Aeneid only
   after the Odyssey, Igor, Aesop and all of Ovid (none of Ovid has audio yet either). A single *Build audio* dispatch
   with id `aeneid-001` would make it now (≈35k characters of SSML plus word clips; inside the $10/month budget).
   Meanwhile: left to the sweep.
4. **Library sub-grouping.** Aeneid entries carry `group: "Book I"` etc. (as the Odyssey does), so once there are
   several parts the text picker shows them under book headings. Ovid's entries have none. Meanwhile: kept.
5. **Dido's suicide (Book IV)** is not covered by any content-advisory trigger (the same gap noted for Ovid).
   Meanwhile: no advisory unless a trigger fires; to be decided before aeneid-030 (IV.607–705), where her death falls.

6. **I.203 set piece decided by the run.** The conventions asked for a dedicated pass before the batch reaching I.203; the unattended run built it from the Latin, rephrased away from known versions, and recorded it in the house-renderings table. Meanwhile: published as is; change it if you prefer another.
7. **Glossary `genitor`.** The broadened entry keeps the old "here Neptune" reading whole, per the broadening rule; the new reading (Jupiter, voc.) is appended.

8. **I.462 set piece decided by the run (aeneid-005).** As with I.203 (item 6): built from the Latin alone, rephrased away from known versions, added to the house-renderings table. The reviewer could only check against remembered versions. Meanwhile: published as is; change it if you prefer another.

9. **Half-lines.** Greenough prints ~58 half-lines (first: 1.534, 1.560). Meanwhile: each is hand-scanned in scan-fixes.json with a reason starting "Half-line", and validate_aeneid.py accepts such lines (fewer than six numbered feet, one × mark). Tell me if you want them treated differently.

10. **Doubtful quantities (aeneid-008).** 1.663 hand scansion needs Ergo not elided before his; 1.682 needs -us long before elided -ve; 1.703 intus, 1.733 huius, 1.693 amaracus each need a long syllable the references did not confirm. Meanwhile: kept the only parse that fits; revisit if you know otherwise.

11. **II.49 set piece decided by the run (aeneid-009).** Built from the Latin alone, rephrased away from known versions, added to the house-renderings table. Meanwhile: published as is; change it if you prefer another.

12. **Scansion not confirmed (aeneid-012).** 2.288 gemitus (scanner marks ge/mi long) and 2.325 Dardaniae/Troes (scanner splits ae and reads Troes as one syllable) are published on the scanner's fit; the reviewer could not settle them from public-domain sources. Audio quantities may be off there. Meanwhile: kept; revisit if you know otherwise. 2.339 Rhipeus rests on a long Rhi, also unconfirmed.

13. **Doubtful quantities (aeneid-013).** 2.433 long *si*, 2.419 long *i* in *imo*, 2.447 *iam*, 2.449 *imas*, 2.468 (half-line) long final -a of *interea* and lengthened *sat*, 2.417 short E- in *Eois* (cf. 1.489 long), and *Rhi-* long (as at 2.339) rest on the only fit found, unconfirmed. Meanwhile: kept; revisit if you know otherwise.

14. **Check merentis (aeneid-014, 2.585–586).** Read as acc. pl. of the participle merens agreeing with *poenas* ("deserved punishments"); the genitive-singular alternative is named in the note. Meanwhile: published as is.

15. **2.563 Iuli (aeneid-014).** The aeneid-015 review found Iulus/Iulum scan as three syllables (Ĭ-ū-lus) with a dactylic fifth foot (cf. 1.556, 1.690); aeneid-014 published 2.563 with a spondaic fifth foot and consonantal I. Meanwhile: left; a scan-fixes entry would apply on a rebuild of 014.

16. **Scansion not confirmed (aeneid-016).** 2.745 scans only with *deo* as one short syllable (synizesis); 2.787 is treated as a half-line (11 syllables; on the traditional list of Book II hemistichs, not sourced in the pipeline); long -bi of *tibi*/*ibi* (704, 784, 792), *Lydius* (781), *asylo* (761), *donec* (719), *e tanto* (718), *iuxta* (714), *gaza* (763) rest on the only fit found. Meanwhile: kept; revisit if you know otherwise.

17. **Scansion not confirmed (aeneid-017).** 3.74 (`Neptuno Aegaeo` unelided, long i of Nereidum) and 3.97 (`domus Aeneae` unelided, after 1.617) are hiatus fits, the only parse found; 3.41 `Quid miserum, Aenea, laceras?` has no hexameter under natural quantities (published on the scanner's fit); long -a of `iuxta` (22), `radicibus` (27), long -o of `meo` (18), short -es of `Thraces` (14) rest on the only fit found. Meanwhile: kept; revisit if you know otherwise.

18. **Scansion not confirmed (aeneid-018).** 3.108 `Rhoeteas` is hand-scanned Rhoe-tē-as (long te, Greek ει); 3.163 `Grai` (two long syllables) and 3.168 `Iasius` (long Ia- and si; Ī-ă-sĭ-us also fits) are on the scanner's COSTLY fits. Meanwhile: kept; revisit if you know otherwise.

19. **Scansion not confirmed; misprint (aeneid-019).** 3.209 final -dum of `Strophadum`, 3.211 `insulae Ionio` (scanner fit kept), 3.213 `liquere` long li-, 3.272 `Laërtia` with diaeresis, 3.277 `prora` before consonantal i, 3.295 long `Pri-` rest on the only fit found. 3.286 prints `clipeum.` where a comma is meant (rule 5b): the reading text has the comma, the note says so, `t` stays as printed because the checks require it. Meanwhile: published as is.

20. **Punctuation and speech marks (aeneid-020).** 3.315: Greenough prints a closing ” at 319 but no opening “ before Aeneas's reply; the reading text supplies it, `t` stays as printed (rule 5 would instead add the mark to the source and re-pin — tell me if you prefer that). 3.391 prints `iacebit.` where a comma is meant (rule 5b): reading text has the comma, `t` as printed. Meanwhile: published as is.

21. **Scansion not confirmed (aeneid-020).** 3.308 `deriguit` long -it in arsis; 3.311 `si` before `lux`; 3.316 initial `ne` long; 3.317 `te` long; 3.335 `Cha-` long and elided n'ā long; 3.354 `aulaï` final long; 3.365 `Harpyia` with long py- (consonantal i; 019 has four syllables Har-pў-ĭ-ae); 3.393 `requies`; 3.396 `Italique` short I vs long I at 3.364. 3.340 is a half-line deliberately not completed. Seven notes exceed 140 words (WARN). Meanwhile: kept; revisit if you know otherwise.

22. **Speech marks and scansion (aeneid-021).** 3.475–481: Greenough prints “ at 475, no closing mark at 479, and “ before *Vade* at 480; the reviewer and drafter read all of 475–481 as Helenus's speech, with *ait* a tag. `t` as printed; l and i supply the marks. Doubtful quantities (tibi 412, utraque 416, imo/ima 421/443, rursus 422, Pachyni 429, si 433/434/500, mittere 440 with lengthened -te, gravia 464, retro 496, casus 504) rest on the only fit found. Meanwhile: published as is.

23. **3.549 antemarum (aeneid-022).** Greenough prints `antemarum`; it scans only as `antemnarum` (dropped n, a misprint under rule 5b). Published as printed, note says so; t unchanged. Meanwhile: published as is; tell me if you want the reading text corrected.

24. **Scansion not confirmed (aeneid-023).** 3.642 `claudit` (dit lengthened in thesis), 3.617 `socii`, 3.671 `potis… fluctus`, 3.675 `e silvis`, 3.676 `portus`, 3.692 `Sicanio`, 3.693 `Plemyrium`, 3.701 `Geloi` (COSTLY 1.5 fit), 3.629 `oblitusve` rest on the only fit found; full list in `drafts/aeneid-023/review.md`. 3.640 `rumpite.` and 3.661 `solamenque mali.` are half-lines; 3.639 and 3.660 carry the scanner's own fit as carriers. Meanwhile: published as scanned; tell me if you know otherwise.

25. **IV.23 set piece decided by the run, and scansion not confirmed (aeneid-024).** IV.23 built from the Latin alone, rephrased away from known versions, added to the house-renderings table. Doubtful quantities left on the only fit found: 4.64 *pectoribus inhians* (long -bus), 4.69 long *-ta* of *coniecta*, 4.75 *Sidonias* short *do*, 4.8 long *sic*, 4.22 short *hic*; 4.52 *desaevit* read as present (a perfect reading exists). Meanwhile: published as is; change if you prefer another.

26. **Scansion not confirmed (aeneid-025).** 4.172 *praetexit* (long -it in thesis), 4.174 *velocius* (long ve-), *cōnūbium* long nū- (published 1.73 and 3.136 have short), *Iarbas* with vowel I at 4.196 (published 4.36 in aeneid-024 uses consonantal I and is probably wrong), *Sīdōnia* quantities differ among published parts, 4.132 Massyli, 4.136 stipante, 4.146 Cretesque Dryopesque, 4.166 pronuba rest on the only fit found. Published parts untouched. Meanwhile: published as scanned; revisit if you know otherwise.

27. **Scansion and readings not confirmed (aeneid-026).** 4.235 `spe inimica`: hand-scanned with hiatus after `spe` (scanner elided and made i-ni long); unconfirmed. 4.216 `mitra` long mī and 4.215 `semiviro` long sē are forced by the metre, unconfirmed. 4.274 `Iuli` read Ĭūlī (house practice; scanner preferred consonantal). Open readings stated in the notes: 244 `resignat`, 237 `nuntius`, 263 `quae`, 228 `Graium`/carried-over `non`, 303 `trieterica`. The unit-0 note's Iarbas "son of Jupiter Hammon" comes from IV.198–199, outside this part. Cuts: 276 closing ” stays at the head of the next unit's `t` (as 013); 296 `dolos—quis` has no space at the dash, so the stretch is one unit. 273 is Greenough's bracketed line, kept in [ ]. Meanwhile: published as is.

27. aeneid-027 review: published scan-fixes entry 4.36 (aeneid-024) scans Iarbas with consonantal I, but 4.196 and 4.326 need vowel I; probably re-enter 4.36 and rebuild aeneid-024. Left untouched meanwhile.

28. **Scansion, speech marks and advisory (aeneid-030).** 4.667 `femineo ululatu`: scanner fit (long mi-, synizesis in -neo) kept; a natural-quantity parse with hiatus also exists, unconfirmed. Lengthened syllables left as the scanner gives them: 615 `audacis`, 619 `tradiderit`, 645 `inrumpit`/`domus`, 670 `Tyros`, 672 `exanimis`, 686 `semianimem`. 4.659–660 and 4.685 print misplaced speech marks: `t` as printed, `l`/`i` mark the speeches by sense, notes say so (rule 5b), so the validator WARNs t has 6 opening / 7 closing marks. Dido's death (IV.642–705) carries no `advisory` (no trigger applies; see item 5); add one to this part if you want the suicide flagged. New house renderings: IV.653–654 and IV.660. Meanwhile: published as is.
- 2026-11-09 · aeneid-031 · V.1–103 · Doubtful quantities left as scanned: Aenea 5.17 (final -ā long here; published 017 has short), Criniso 5.38, muta-cum-liquida lengthenings (supra 10, tenebris 11, sacra 59, sacro 78, nigrantis 97, Thybrim 83), gaza/reduces 40, maturus 73, carchesia 77, Italos 82 (short I-), iam elided before a vowel 3 and 8. urbe Mycenae 5.52 taken as genitive singular (reviewer's judgement, not checked against a lexicon). No decision needed from the owner.

24. **Misprints and scansion (aeneid-032).** 5.135 `perfilsa` (perfusa), 5.166 `Pete` (pete), 5.181 `Ilium` (Illum) are published as printed, each note opening with the print's reading, as for #23; tell me if you want the reading text corrected. Open from review: (a) Ovid parts scan `Phae-` as one syllable, here `Phaethontis` is three (metre can't tell); (b) aeneid-019 (3.211 `insulae Ionio`) and aeneid-023 (3.671) treat the I of `Io-` as a consonant; 3.211's hiatus needs a vowel, so they probably need re-entering; (c) 5.186 `praeeunte` short `prae` rests on 7.524 `praeustis`, unconfirmed; (d) `ovid-met-026` has `biiu–3gum–`, likely the same bi-iu error fixed at 5.144. Meanwhile: nothing changed in published parts.

29. **Scansion and speech mark (aeneid-034).** Doubtful quantities left on the only fit found: 5.337 lengthened -lus of `Euryalus` before `et` at the pause (cf. 1.314), 5.311 long ā in `Amazoniam`, 5.334 long ŏb- in `oblitus`, 5.298 long Pā- in `Patron`, 5.343 short fa- in `favor`, 5.371 long ī in `idem`, 5.299 `Tegeaeae` as Te-ge-ae-ae. 5.294 and 5.322 are hemistichs. 5.385 prints the closing ” after `iube.` with no space before `Cuncti`: t as printed, l/i by sense. Meanwhile: published as is.

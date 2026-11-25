# Review — popol-vuh-008

## Pass 1

Reviewer pass 1, 2026-11-25. I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the text and the
establishment log), popol-vuh-001…007.json, popol-vuh-glossary.json, wordre.py, QUESTIONS.md, the 007 review and the draft
units.json (68 units). For meaning I used only Brasseur 1861 (OCR lines 20930–21370: K'iche', French and notes) and the
glossary. I opened no modern translation and recalled none. Every edit was made by script (json load/dump,
ensure_ascii=False, indent=1). No `t` was changed, and no unit was added, removed or moved. Unit numbers are 0-based, as
the draft's array.

I compared every mt with 001–007 by script (MS form → modern form, lowercased). There are seven differences, all the ones
the drafter made on purpose, and all hold. (1) `cab` → kab' 'second' (units 16, 18, 21; `v cab`). 003's `cab` is q'ab'
'hand', but 001's and 005's `vcab` 'its second' is ukab', and Brasseur's French has 'le second'. (2) `vcab` → uq'ab' 'his
hand' (units 60, 63; also `v cab` in 62). 001/005's `vcab` ukab' is 'second'. 'Hand' here follows 003's `cab` q'ab', and
Brasseur has u gab (g = ꜫ) and 'des pieds et des mains'. (3) `xquilo` → xqilo (unit 35). The boys are speaking, and
Brasseur has x-K'ilo (k = q) and 'nous avons vu'. 005/006's xkilo is 'they saw'. (4) `cumal` → qumal (unit 51). The boys
are speaking, with Brasseur's kumal and 'par nos soins'. (5) `vvb` → wub' (units 42, 45). After ca/qui the vv is respelled
wu, as 007's ivvbah gave iwub'aj. 005's lone `vvb` 'his blowgun' (uub') has u- 'his' as its first v. I corrected how the
note explains this (below). The forms with more than one published mt (ca ka/qa, chi chi/chik/chi', cu k'u/ku, vi
wi/wi', oc ok/oq, que ke/qe, quech, chique, cac, cam) each fit their sense here. I checked every new form against the
letter rule. The restorations are k'o for `co` (002's co → k'o), meb'a', nik'aj, uqul, muq/muqu (Brasseur muk, k = q),
q'aq' for `cac`, k'am for `cam`, k'utun (001's uk'utunisaxik), uti'o (003/004/007) and kaq- in kaqwakawoj. Each is a
certain word or follows a published precedent, and each note says so. I checked every grammatical label, `l` word by word
against the K'iche', `l` against `i`, the couplets, the house table, every cross-reference to an earlier part (by script)
and every Brasseur claim (against the OCR). Every establishment-log doubtful reading and letter decision is mentioned in
its unit's note.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 68 units, and the units' `t`, joined in order,
give back the packet's 26 paragraphs exactly, paragraph by paragraph.

Counts: **major 0 · minor 9 · style 4** (13 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 29, 33, 34, 37, 38 | i | minor | `at ꜭahol` was "young man" five times. 006 (6:43) and 007 (7:39, the same question `Apa cat be vi, at ꜭahol?`) give "boy". The note to 29 itself calls it "the address between young men of the last part". | "boy" in all five. |
| 5 | n | minor | "Brasseur takes hupunic and pacal as one stooping posture ('à plat ventre')". In this sentence his French renders only hupunic so. He gives `pacal curi tap xacanic` as 'l'écrevisse s'étant mise en marche en montant'. His 'à plat ventre de nouveau' belongs to the pacal of unit 10. | The note now says exactly that. |
| 18 | n | minor | "Brasseur thought of the earthquake" was said of the name. His note is about Cabracan's answer (unit 30), 'un symbole du tremblement de terre presque continuel', not about the name. | "Brasseur, in a note, takes his answer below as a figure of the almost constant earthquakes of the region". |
| 42 | n | minor | "the first v the w that joins ca 'our' to vb, as in iwub'aj": this gives a morphology that has no support. The w of iwub'aj is part of the 2pl prefix iw-, and nothing shows a w joining ca to a vowel. | The note now says what is written (vv after ca and qui, in vvb, vvbah, vvbanic), that the toggle respells it wu as 007 did, and that whether the v is a glide or part of the prefix is not clear. |
| 45 | n | minor | `cuxlabih` 'they breathe at' was labelled "with c- (ongoing)". Then nothing in the form says 'they', which `l` and `i` give. The form follows chi, and c- is the 3pl ergative before a vowel, as the drafter's own note on `calaxic` (unit 66) has it. | "its c- is taken as 'they', the form of qui before a vowel (as calaxic …), after chi; inferred". |
| 47 | n | minor | The fire drill ("a stick twirled on a board") was given as "a guess after Brasseur's 'battirent du feu'". Brasseur has 'struck fire', and the drill is not his. | The note gives Brasseur's sense and says that the drill reading is the drafter's guess. `l` keeps "drilled(?)". |
| 48 | l, i, n | minor | "(modern sajkab' 'lime')", and "lime" in `l` and `i`. The only witness, Brasseur, says zizate (Nahuatl tizatl), 'terre blanchâtre fort friable' used for polishing and cement. That this is a K'iche' word for lime is asserted without support. | `l` "white-earth(?)". `i` "One bird they smeared with chalky earth; they put white earth all over it." The note gives Brasseur's note in full and says that the toggle respells the letters. |
| 50 | n | minor | chacahoc is linked to xchacah 'it cooked', and the note did not say that Brasseur's letters set the two apart. He has ch'u kah-oc (k = q), as in kahoc 'downward', but x-chagah (g = ꜫ). | Added this; the line stays uncertain. |
| 62 | n | minor | "xim … im 'tie, bind' with x-". The root is xim (modern ximik 'tie'). The completive x- is not written apart, so the form is not im + x-. | "the root is xim 'tie, bind' (modern ximik), here passive, the x- of the completive not written apart (inferred …)". |
| 12, 53 | n | style | "Brasseur's print is illegible in the scan". What is illegible is the OCR text (х-Шор, бус); the print was not seen. | "Brasseur's word is garbled in the OCR (…)". |
| 36 | n | style | "icouic 'they passed' in the sixth part": the 'they' is xe (6:1, 6:36 `xe icouic`). | "xe icouic 'they passed'". |
| 39 | n | style | "iv- 'you (pl.)' (i- before a vowel)" reads as if i- were the form before a vowel (the 007 pass-2 fix). | "(the form of i- before a vowel)". |
| 57 | l | style | `Chi ya ta` "You(pl.)-give then": ta is not 'then'; the note calls it a particle. | "You(pl.)-give (ta)". |

### Refused / left

- **The drafter's deliberate mt changes (cab kab', vcab uq'ab', xqilo, qumal, wub'): all kept**, for the reasons in the
  method paragraph.
- **`chi cama ca be` kama (unit 41) beside `mi xca cam` k'am (unit 37), in one part.** Kept. Each follows a published
  precedent: cama → kama in 005/006, and cam/xquicam → k'am in 002/005/006. Brasseur has g in the first and q in the second.
  Both notes say so. This is QUESTIONS 007 (3), still open.
- **`racan` rakan beside the name Kab'raqan.** Kept, since published 001/006/007 give rakan, and 005 gives Kab'raqan.
  Raise it with QUESTIONS (the modern word is raqan).
- **Restorations kept:** co → k'o (002), cacvacavoh → kaqwakawoj (the note ties it to kaq with Brasseur's k, the 007 rule),
  nicah nik'aj, meba meb'a', vcul uqul, muc muq, cac q'aq', xcutun xk'utun, xutio xuti'o, huzu jusuk (002).
- **Letter for letter, kept:** vchec uchek (ch'ek 'knee' only inferred), chutinih chutinij (it may be chuti ch'uti', but
  that is not shown), zcaquin, cuz, cauahin, cabiquilahic, vcaxah, xuquiz (k'is, as published xquiz), vaih waij, iohol yojol.
- **`cu rraih` ku (unit 55)**: kept, as the 11 published ku. Brasseur has c'u raih.
- **`xrilih` 'it was watched' (unit 63) with an ergative r- and a passive sense**: left, because the note already says that
  the form is not clear.
- **Unit 35 `xa co quil caquiye` and unit 52 (`hun ꜩac, hun bit …`)**: the English follows Brasseur, as the notes say;
  nothing better can be built from the words.
- **The name counts in note 18 (Cabrracan ×7, Cabracan ×7)**: checked by script against `t`, and they are right. The
  establishment log's "8× … 6×" is wrong, because it counted the heading.
- **The about**: checked against the units; every event is there, in order. No change.
- **For the glosser / pass 2:** broaden `cab` (kab' 'second', in `v cab`), `vcab` (uq'ab' 'his hand'), `cumal` (qumal 'by
  us'), `xquilo` (xqilo 'we saw'), `vvb` (wub', after ca/qui). `xim` is the root xim. `zahcab` must not be glossed 'lime'
  as certain.

### For QUESTIONS.md

1. **`at ꜭahol`** is now "boy" here as in 006/007, though Brasseur has 'jeune homme'. Kept for consistency.
2. **`racan` rakan (001, 006, 007, 008) against the name Kab'raqan and the modern raqan 'leg'.** Decide together.
3. **The 'take' verb**, QUESTIONS 007 (3): it now splits inside one part (unit 37 k'am, unit 41 kama).
4. **vv after ca/qui** (ca vvb, qui vvbah) is respelled wu, after 007's iwub'aj; 005's vvb is uub'. Whether the v is a
   glide is for the owner.
5. **For the establisher:** the 008 log says Cabrracan ×8 / Cabracan ×6 (the text has 7/7) and "27 paragraphs" (the
   pinned text has 26).
6. No new house rendering in this part.

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

## Pass 2

Reviewer pass 2, 2026-11-25 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md (text and establishment log), popol-vuh-001…007.json, popol-vuh-glossary.json, wordre.py, the 007 review (its
pass 2), units.json as left by pass 1, pass 1's review, gloss.json, novel-forms.json and known-forms.json. For meaning I
used only Brasseur 1861 (OCR lines 20930–21370, K'iche', French and notes) and the glossary; no modern translation was
opened or recalled. Every edit was made by script (json load/dump, ensure_ascii=False, indent=1); no `t` was changed and
no unit was added, removed or moved. Unit numbers are 0-based, as in pass 1.

Units: I went through all 68 again (grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, the establishment-log items, the about) and re-checked every Brasseur claim in the notes
against the OCR, including pass 1's corrected ones (units 5, 18, 47, 48, 50, 12/53): all hold. Pass 1's fixes all stand.
I re-ran the MS-form → mt comparison against 001–007 by script (same five deliberate differences as pass 1), and then
compared the *roots* of 008's new forms with the published mt, which the form-for-form comparison cannot catch: the
climbing verb acan is aq'an in 004 (acan, acanic), 005 (chacan) and 006 (acanoc, "toggle aq'an, as in the earlier
parts", against Brasseur's k there too), but 008 had xakanik / kakanik.

Gloss: all 111 entries and every `__broaden__` value checked against the text and the final mt, by script (every
occurrence of each key) and by reading. Keys equal novel-forms.json exactly. Every head equalled the units' mt before
the acan change; xacanic and cacanic were changed with it. Every `__broaden__` value begins with the glossary entry
verbatim + " · ". `zahcab` is not glossed as lime (it says lime is not shown). I compared each known form's 008 uses with
its glossary entry: three broadenings were missing (bac, cat, xuxic) and one was not needed (bi).

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 68 units, the units' `t` give back the packet's
26 paragraphs exactly, paragraph by paragraph, every `t` equals pass 1's, gloss keys == novel-forms keys (+
`__broaden__`), every gloss head equals the units' mt for that form, and every `__broaden__` value starts with the current
glossary entry + " · ". Final gloss: 111 novel forms, 19 broadened.

Counts: **major 0 · minor 14 · style 16** (30 findings; units 3, gloss 27).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 5, 8, 36 | mt, n | minor | `xacanic` xakanik, `cacanic` kakanik ×2: the climbing verb acan is aq'an in every published part (004 acan/acanic, 005 chacan, 006 acanoc, each restored against Brasseur's k); the note itself calls it "acan 'climb'", a certain word. | mt xaq'anik, kaq'anik (×2); notes 5 and 8 say the toggle gives the root aq'an as in the earlier parts. |
| 59 | i | minor | "they set off again": xbe is 'he went', and the note says "singular then plural". | "he set off again, and they came there …". |
| 51 | i | style | "As the earth goes onto the bird's back": xchoc is 'it shall go' (l "it-shall-go-in"; Brasseur 'enveloppera'). | "As the earth shall go onto …". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| xeopon | value | minor | "also used with a singular subject (Zipacna) in the same sentence": wrong (the note: xbec singular for Zipacna, xeopon plural for all) and pinned to a line. | Dropped; the entry is the form's morphology. |
| xacanic | value | minor | Head xakanik, root "akan", against the glossary's acan aq'an and the corrected mt. | "xaq'anik … aq'an 'climb' …". |
| cacanic | value | minor | Head kakanik, the same. | "kaq'anik …". |
| xcutun | value | minor | "the verb of ukutunisaxik": the published form is uk'utunisaxik (glossary vcutunizaxic, cutun k'utun). | uk'utunisaxik. |
| xꜩolcopih | value | minor | "he turned back" stated plainly; the note says it is taken with Brasseur, the ending unknown. | "(inferred, after Brasseur 'il ne retourna plus')". |
| vulih | value | minor | Covered only `ca vulih` 'you'; in `xchin vulih` (unit 39) the v is 'I'. The head also described the preceding word ka as part of the form. | Both readings, the w described as what it is in each. |
| chacahoc | value | minor | "the line is uncertain" without the reason; note 50 (pass 1) gives Brasseur's ch'u kah-oc and 'his defeat'. | Says so. |
| tihic | value | minor | "eating" with no hedge; the establishment log and note call the reading doubtful (blot on the ligature). | "(doubtful reading: a blot sits on the ligature)". |
| xcul | value | minor | "kul 'smear'" plain; the notes mark the sense inferred (Brasseur 'frottèrent'). | "(inferred)". |
| __broaden__ bac | new | minor | Glossary 'bone; noun'; here a verb, xqui bac (qui cac) 'they made/struck (fire)', a guess after Brasseur. | Added "b'aq — (guess) make fire, strike fire …". |
| __broaden__ cat | new | minor | Glossary 'you (one) shall / ongoing'; in unit 51 `quehe cat` is taken as cut 'then' (Brasseur quehecut). | Added "kat — (inferred) then, so; taken as k'ut written cat …". |
| __broaden__ xuxic | new | minor | Glossary "they came to be"; here `abah cut xuxic ri Zipacna`, singular (no e-). | Added "xuxik — it became, he became …, no plural e-, so singular". |
| cumaꜩih | value | style | "their trick": 'their' is qui, not in the form; "(guess)" before the meaning. | "trick, contrivance (guess) …". |
| ahtah | value | style | "after ka r- … in kar ajtaj" pinned; head "wishing, want". | General, with the phrase as an example. |
| xcoc | value | style | "that it went in": 'that' is the context. | "it went in (inferred) …". |
| hupunic | value | style | "the jupulik of the last part": pinned to a part. | "jupulik 'face down' with n for l … (Brasseur 'à plat ventre')". |
| pacal | value | style | Brasseur's opposite reading not mentioned (the glossary's pacalic mentions it). | Adds "(Brasseur pagal, read as stooping)". |
| xtilob | value | style | "it came down … meaning unknown": self-contradictory order. | "(guess) meaning unknown, 'came down' guessed from qajoq …; doubtful reading (perhaps xhilob)". |
| hunchic | value | style | "said twice in a row": pinned. | Dropped. |
| xivilo | value | style | "(i- before a vowel)" reads as if i- were the prevocalic form (pass 1's fix in note 39; 007's pass 2). | "(the form of i- before a vowel)". |
| mabi | value | style | "not (yet)": 'yet' invented; the note says only a form of maui. | "not". |
| mucu | value | style | "they buried him": 'they' is xqui. | "bury (him) …". |
| __broaden__ xquilo | value | style | "(qa- before a vowel)": the same misreading of direction. | "(the form of qa- before a vowel)". |
| __broaden__ car | value | style | "not 'fish' here": pinned, and a negation rather than a meaning. | "kar — (inferred) k- 'ongoing' + r- 'he', run onto the verb aj …". |
| __broaden__ vi | value | style | Third reading not in the format. | "wi — part of wikiq'ab' 'right (hand)' (inferred), written apart …". |
| __broaden__ ba | value | style | "here perhaps pointing": pinned. | "b'a — (inferred) pointing, 'over there, look', after chila' 'there'". |
| __broaden__ bi | dropped | style | 'our name' after qa is the same sense as the entry's 'name' ('their name' after ki); not a new reading. | Removed. |

### Refused / left

- **Glosser's other broadenings kept** (cab, vcab, cumal, xquilo, vvb, pu 'in', car, xa 'you (did)', chu 'he', cha 'at
  your', vi, vaih 'hunger', cul 'coat', ꜩac, rico, ba): each is a sense the entry lacks and the units use.
- **No broadening for** `ꜭahol` 'boy' in address (007 pass 2 refused the same), `chi` joining a number to a noun (`e
  caib chi ꜭaholab`; the entry's 'with, of' is near enough and the l brackets it), `qui` in `qui paqueic` and `chu` in
  `xel chu vloc` (unexplained and unrendered in the units; a gloss would be a guess on a guess), `cabracan` "younger son"
  (= the second son, as the text says).
- **`cabrracan` gloss "younger son"** kept, to match the glossary's cabracan.
- **Brasseur's k (= q) in `u chek`, `bikitahie`, `chakou`, `chakatahic`**: left. vchec, biquitahic and xchacou are
  respelled letter for letter (uncertain words); chacatah- follows 004–007 (chakataj).
- **Unit 36 `qui couic` kowik** against 006's icouic ik'owik, though the note links them: kept, since the note calls the
  link inferred and Ximénez's plain c is respelled, as 007's ecouic ekowik.
- **Unit 41 note "Brasseur has Ch'y gama"**: the OCR has `дата`; the reading g is plain from the shape and agrees with
  his French; left.
- **Unit 15 l "Seven Macaw"** for Vvcub Caquix: as in 005–007 l.
- **The about**: re-checked against the units; no change.

### For QUESTIONS.md

1. Pass 1's six points stand.
2. **The climbing verb acan** is now aq'an in 008 as in 004–006, although Brasseur writes k (= q) here and in 005–006
   (x-akanic, c'akanic; ch'akan, akan-oc, as those notes say). The modern word is aq'an; the owner may want to confirm that the modern word,
   not Brasseur's letter, decides here (the same question as 007's rixk'aq).
3. No new house rendering in this part.

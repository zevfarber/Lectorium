# Sumerian King List — questions for the owner

- 2026-10-12 · published Col. I · Langdon prints Á-la(l)-gar (l. 5), Zimbar-šú without (ki) (l. 25), Zimbar-(ki) (l. 30), eri-ki-me-eš (l. 36), ĕ-dé (l. 41); the published part has a-la-gar, zimbir{ki}-šú, zimbir{ki}, eri{ki}, e₃; its restored [nam-] and [Eri]du are unmarked; its e₃ uses the E sign where the standard is UD.DU; some subscripts were not converted (šú, gín, úr, dúr, lù). Decided meanwhile: the published part is left as it is; new parts follow Langdon and the plate.
- 2026-10-12 · signs · signs-cuneiform.json has both ESH and ESZ keys for one sign. Decided meanwhile: new parts use ESH.
- 2026-10-12 · audio · No Sumerian voice chosen. Decided meanwhile: parts publish without audio.
- 2026-10-12 · published Col. I · Line 32 of king-list-antediluvian has an empty `t` (its transliteration is there, its cuneiform is not), so the reader shows a blank line. Decided meanwhile: left for the owner; not part of Run 3's parts.
- 2026-11-16 · king-list-kish-i · Langdon's fn 8 says the 19 preserved Kish I reigns sum to 12,491; the figures he prints (and the plate) sum to 15,751. Decided meanwhile: the II 42 note reports both and the scribe's 24,510, correcting none.
- 2026-11-16 · king-list-kish-i · II 9: the plate shows only two MU signs after KA-LU, so Langdon's "Ka-lu-mu-mu mu" is one MU short. Decided meanwhile: shipped ka-lu-mu + mu "years"; the note gives his reading and the Nippur -um forms.
- 2026-11-16 · king-list-kish-i · II 5–6: Langdon's restorations (Ba-[ba?-gul-?e?], Bu-ᵈ[En-zu]) carry his own question marks. Decided meanwhile: only the preserved signs + a LACUNA glyph are shipped; his guesses are in the notes.
- 2026-11-16 · published Col. I · the pilot glossary calls ib-ag "plural reign verb"; its -b- is not a plural marker (the reviewer flagged it). Decided meanwhile: published part left as is; new notes say the plural English follows the sense.
- 2026-11-16 · signs · Langdon's Tup- (KIŠIB) is drawn with Unicode's only character for it, CUNEIFORM SIGN MES, under a new key KISHIB. Decided meanwhile: kept; revisit if the owner prefers the MES key.
- 2026-11-16 · king-list-uruk-i · III 36: the twelve reigns as Langdon prints them sum to 2,311; the prism writes 2,310 and Langdon (fn 8) calls the addition correct. The difference may lie in the restored units of III 3 (325). Decided meanwhile: both figures reported in the note, nothing corrected.
- 2026-11-16 · signs · MES added as its own key (same Unicode character as KISHIB) for Mes-ki-aĝ₂-ga-še-ir and Gilgamesh; signs.py cannot add values to existing keys, so UL lacks 'utul' (III 24), TU lacks 'ku₄' (III 5), ḪAR lacks 'ḫur' (III 6). Decided meanwhile: the glyphs carry these values in `tr`; the sign entries are left for the owner.
- 2026-11-16 · king-list-uruk-i · III 17: ab-ba-ni lil₂-la₂ rendered with Langdon's 'his father was a fool (?)'; the modern understanding (a lillu, phantom/demon) is in the note. Decided meanwhile: Langdon as base per conventions.

## 2026-11-16 · king-list-ur-i-awan-kish-ii-hamazi
- **mes = DUB vs MES.** Langdon fn. 1 (III 40) says the sign written mes is DUP (REC 385), and the plate draws the same sign in III 40/42/43 and III 7. This part ships DUB (tr mes); the published king-list-uruk-i ships MES for the same drawn sign (III 7, and III 1 restored). Decided meanwhile: DUB here; uruk-i left untouched for the owner to reconcile.
- **Unread but visible sign (IV 30, Langdon '?' / fn. PISAN+RU?).** No sign key exists for "a sign present but unread"; shipped as the LACUNA glyph with tr "x", unbracketed, folded into the name's morph (x-nun-na), with the note explaining. Decided meanwhile: keep this; a dedicated key (label "x") via signs.py would be cleaner if the owner wants one.
- **New signs LAH4 (IV 20) and UMUSH (IV 29)** are identifications of uncertain copies (Langdon Laḫ(?), Umuš-e); both are flagged in the notes.

## 2026-11-16 · king-list-uruk-ii-to-kish-iii
- **Mari = ma-ri₂ (URU), not Langdon's Ma-er (IR).** In V 22 and V 33 the copy draws the sign after MA like the URU of III 15, not the IR of III 27. Decided meanwhile: shipped ma-ri₂{ki}; Langdon's reading is in the notes.
- **IV 48: 480 vs 420.** The prism's numeral is 8 geš = 480; Langdon's translation and introduction give 420 for the dynasty. Decided meanwhile: 480 shipped, both reported.
- **V 1–10** is one lost unit because Langdon's source has one entry for it (the build requires that); in Col. II the lost lines were one unit per line. Decided meanwhile: one unit, the note saying it stands for ten lines (Langdon: Ur II, 4 or 5 names).
- **V 43 Akšak**: two signs before KI, shipped as the conventional UD.KUŠU₂ though the copy does not confirm KUŠU₂ (new sign KUSHU2 added). The next part's drafter should compare V 44's first sign.
- **"tavern-keeper"** (V 37) is kept in `i`, against Langdon's "a female wine seller", since it is the part's name and the project's English for the word in Hammurabi. Decided meanwhile: kept.

## king-list-akshak-kish-iv-uruk-iii (2026-11-17)
- **Long-form "Gimil" (VI 9, VI 13; also VII 20, VII 45)**: the copy draws two touching parts where Langdon reads the one sign ŠU (Gimil). The drafter shipped an unidentified sign + ŠU; the reviewer refused that (the copy cannot settle it). Decided meanwhile: Langdon's šu-{d}suen, flagged uncertain in the note and glossary.
- **VI 17 Ašdar-muti**: the copy shows one sign the run could not identify; shipped as x-mu-ti with Langdon's Ašdar (Ištar) in the note.
- **Divine names read by sign** ({d}suen, {d}za-ba₄-ba₄, {d}šakkan₂) against Langdon's Sin, Ilbaba, Šaḫan, following the earlier {d}utu/{d}nanna decisions. Decided meanwhile: kept, Langdon's forms in notes.
- **conventions.md** listed VI 21 among totals that do not add up; it adds up (491). Corrected.

## king-list-akkad (2026-11-17)
- **Published VI 30 (king-list-akshak-kish-iv-uruk-iii)**: both drafter and reviewer of this part find that in VI 31, 34 and VII 13 the NE of A-ga-de₃ is the crossed box alone; in VI 30 the copy draws in addition a box of corner-wedges like ŠAR/SAR between NE and KI, which the published part merged into a 'wide two-part NE'. Decided meanwhile: the published part is left as it is, for the owner.
- **VI 33 sagi**: the first sign is drawn unlike both KA (II 9–10) and SAG (III 4). Decided meanwhile: Langdon's KA kept (KA.ŠU.DUG), read sagi, flagged uncertain.
- **signs-cuneiform.json DUG**: the entry added this firing says "in sagi (SAG.ŠU.DUG)"; after review the part ships KA.ŠU.DUG. signs.py cannot edit an existing entry. Decided meanwhile: left for the owner (one word to change, in the JSON and the two embedded copies).
- **VI 34**: the copy writes the second Agade A(sic!)-NE with no GA and no KI and puts a '?' inside the sign Langdon reads galu. Decided meanwhile: shipped a-de₃ and lu₂(?), Langdon's print in the note.
- **VII 9 Shu-Durul**: wholly restored; Langdon's Gimil-dur-ūl, KIB read ul after Scheil, shipped [šu-dur-ulₓ] with the new sign DUR (GU₂×KAK).

## king-list-uruk-iv-gutium (2026-11-17)
- **VII 31, VII 33: no MU on the plate.** Langdon prints 'mu 6 ni-ag' unbracketed in both; the copy goes straight from the name to the figure, while every other reign line draws MU. Decided meanwhile: the plate followed, `l` "6 (years)", Langdon's print in the notes.
- **Gutian total (VII 50–51).** The prism's surviving figures add to 91 years and 40 days; the 125 is Langdon's restoration from P. No. 2; his translation note says 'only 86' without showing how. Decided meanwhile: all three reported, nothing corrected.
- **VII 15 unug{ki}-še₃** at a dynasty's head (box drawn like the EŠ₂ of VIII 2, not GA): the third such -še₃ (V 23, V 44). Decided meanwhile: literal "to-Uruk (sic)", English "In Uruk", as before.
- **VII 26/27 gu-tu-x-um**: a sign Langdon does not read stands between TU and UM in both lines. Decided meanwhile: unread x (LACUNA glyph, tr "x"), lemma gu-tu-um.

## king-list-uruk-v-ur-iii-isin (2026-11-17)
- **VIII 4/6 "mu 7 šu-ši 7 u₄".** Langdon (fn. 7) takes šu-ši as 1/6: 7⅙ years and 7 days; elsewhere on the prism N šu-ši = N × 60, which would give 420. Decided meanwhile: Langdon's reading shipped, flagged, 420 given in the note.
- **VIII 31 Lipit-Ashdar.** Langdon restores ᵈLi-[bi-it-Ašdar] without "?", but gives no writing of Ašdar to ship (and in VI 17 his Ašdar is an unidentified sign); and the copy has no room for AN before LI. Decided meanwhile: li-[bi-it-…] with Ašdar as one LACUNA glyph; no {d}; both in the note.
- **Two-sign logograms with only the first sign surviving** are bracketed as Langdon does each time: urim₂[{ki}…] in VIII 8 but {d}su[en] in VIII 34 (split inside EN.ZU). A house rule is wanted.
- **Sign-glossary values** (signs.py cannot edit entries): ARAD lacks er₃, IB urta, ENGUR namma, KA pi₄, KAK du₃, DI ṭe, IG ĝal₂; UR2 has no values; NE and GAN have only bí, ḫé. Left for the owner.
- **AMAR vs BUR.** Langdon's one "Bur-Sin" is AMAR for the Ur III king (VIII 13, 15) and a closed box taken as BUR for the Isin king (VIII 34, 37). Decided meanwhile: {d}amar-{d}suen and {d}bur-{d}suen, the latter flagged.

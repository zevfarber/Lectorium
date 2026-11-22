# Review: cid-tiradas-104-104b (tirada 104, second part, vv. 2013–2067)

Checked against the pinned packet; Pidal 1923, PDF pp. 259–262 (printed 255–258: text and footnotes 2017, 2019,
2020, 2022, 2024, 2035, 2040, 2042, 2045, 2048, 2052, 2054, 2059), with 400 dpi crops of vv. 2027 (Levantados),
2035 (ên), 2040 (bócal), 2042 (Diaz) and 2063 (mando); PDF p. 27 (printed 23, the introduction's "Elemento
histórico", for the 2042 footnote's "p. 23"); the established texts of earlier parts for every verse
cross-reference (222, 264, 294, 789, 914, 975, 1029, 1222, 1226, 1241, 1345, 1388, 1396, 1516, 1836, 1842,
1960, 1998); the published and drafted parts (pilot, 15-17, 44-48, 75-77, 78-82, 83-83a, 83-83b, 102-102,
103-104a); `conventions.md`; and `cid-glossary.json`.
`t` integrity: all `t` joined by "\n" equal the 58 packet verses in order (2032b, 2036b, 2043b included), before
and after the edits. No `t` was touched, and every `l` has one line per verse. Title style ("tirada 104, second
part") matches 83-83b. Both files were edited by script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2033 (vv. 2033–35) · l + n · **error** · ên: the note said "we do not guess at its sense", and the `l` gave
   "in all my realm", dropping a word. Pidal's circumflex is the house's known contraction mark: lâ (v. 914), lês
   (v. 975), mê (v. 1029), âquel (v. 1222), all glossed so in cid-glossary.json. ên = e + en 'and in', and Pidal's
   footnote (dovos en todo mio reyno parte) joins the line to dovos, which fits. The circumflex is clear on the
   crop. Done: `l` "and-in all my realm part from today."; the note explains the contraction. The `i` ("and from
   this day a place in all my kingdom") already had the "and" and is kept.
2. 2030 (vv. 2030–32b) · n · **error** · "vuestra amor: amor is feminine here, masculine in mi amor, v. 2029": mi
   is invariable and shows no gender. Done: "amor is feminine here (mi, v. 2029, does not show the gender)".
3. 2030 · n · **weak** · "[todos] … restored for the sense and the metre" and "2032b … keeping the traditional
   count" gave Pidal motives he does not state (no footnote). Done: "the whole word Pidal's (in italics); he
   gives no note on it. The line is numbered 2032b in Pidal."
4. 2030 · n · **weak** · "fito, past participle of fincar": fito is the old participle from Latin fictus, which
   goes with fincar but is not formed from it. Done: "fito, 'fixed, planted' (Latin fictus), the old participle
   that goes with fincar 'to plant'".
5. 2052 (vv. 2052–54) · n · **weak** · "omillan is printed without an accent, as here" is meaningless (omillan
   takes no accent). Removed; the cross-reference now quotes v. 1396 (Omillom, doña Ximena), checked.
6. 2062 (vv. 2062–64) · n · **weak** · "mando … a slip for mandó" asserted a misprint. The crop confirms mando
   without an accent and with no footnote. Done: "mando is printed so, without an accent (checked on an enlarged
   crop of p. 258), and Pidal has no note; we read the preterite mandó, which the sense and the ó assonance
   require." `t` unchanged.
7. 2065 (vv. 2065–67) · n · **weak** · "compare se paga, v. 1959": v. 1959 is "Al rey ondrado delant le echaron las
   cartas"; se paga is at v. 1960. Done: "(compare de coraçón se paga, v. 1960)".
8. 2041 (vv. 2041–42) · n · **weak** · (a) "the co[m]de don Garcia of tirada 99" was not verifiable as given.
   Done: "of v. 1836" (checked in the established text). (b) "he refers to p. 23 of his introduction" was
   checked on PDF p. 27: there Pidal calls him Álvar Díaz, at court 1068–1111 and often governor of Oca, near
   Burgos. The note now says so, which also supports "Álvar Díaz" in the `i`. (c) **style** · "a final syllable
   disregarded" was changed to "the unstressed -ez disregarded".
9. 2014 (vv. 2014–15) · i + n · **weak** · onor: the drafter's reading is right, and the house rendering
   'estate' is refused here. Con tan grand onor is honour shown in a reception ('receive him with an estate' is
   nonsense). House 'estate / lands and lordship' belongs to onor held, given or taken (la onor, tollida la onor,
   102-102). The `i` had flattened tan grand: "with great honour". Done: `i` "with such great honour"; the note
   gives the reason and keeps onor distinct from ondra.
10. 2025 (vv. 2025–26) · i · **weak** · "and King Alfonso was greatly grieved" lost the tan of tan grand pesar
    ovo. Done: "so great was the grief King Alfonso felt:".
11. 2046 · l · **weak** · "if you it-should-please": vos is dative. Done: "if to-you it-should-please".
12. 2027 (vv. 2027–29) · n · **style** · "levantad + vos … (-d + os)" contradicted itself. Done: "levantad +
    (v)os … the v of vos lost after the -d". (Crop: Levantados, as pinned.)
13. 2052 · l · **style** · "in good[-hour]" put the unsaid ora in restoration brackets (only the a is Pidal's).
    Done: "in good (hour)", as in 103-104a (v. 1961).
14. 2021 (vv. 2021–24) · n · **style** · (a) the Cardeña cross-reference had no number. Done: "v. 264" (checked).
    (b) Pidal prints "ins Grans beissen". Done: "ins Gras beissen (printed Grans)".
15. 2036 · n · **style** · "[esta razón] … restored from the formula" inferred Pidal's source. Done: "both words
    Pidal's (in italics), no note: the formula … which the manuscript gives whole at v. 2043."

Drafter's points, judged:
- 2063 lo mando: the crop shows mando without an accent and with nothing after it. The note now says this
  (item 6); `t` unchanged.
- 2040 bócal: the crop shows the accent. Pidal's footnote ('levantóse en pie y le besó en la boca'; comp. 3030)
  is quoted accurately. The analysis boca + l(e), with the pronoun of saludó hung on the noun, is right. Kept.
- 2058–59 subject: the king, carried over from the line before (he cannot get his fill of his guest). Pidal's
  footnote to 2059 (the beard so grown that it amazed all who saw him) fits. Kept; the gloss for catándol is
  aligned (Pass 2).
- 2059 aínal = aína + le, 'so soon … on him', with Pidal 'tan pronto'. Kept.
- 2067: passado avie tres años, impersonal aver ('it had been three years'), + comieran, the -ra pluperfect.
  The `l`, `i` and note are right. Kept.
- 2035 ên: resolved (item 1).

Confirmed and unchanged: every Pidal footnote cited (2017 estar; 2019 a tierras firió, v. 1842; 2020 comidía;
2022 Hamilton, Romanic Review IV, 1913, pp. 226–227; 2024 omildança; 2035 comp. 1938, 2363; 2040 comp. 3030;
2042 p. 23; 2045 v. 222; 2048 comp. 2013, Cantar p. 293; 2052 comp. 1396; 2054 v. 1388; 2059 vv. 1241, 789,
2059–60, 3273–74, 1226, 2410); the italics pie[de]s (twice), [todos], [esta razón], [padre], F[o]ssedes, mi[o],
buen[a], R[o]y, f[o], creçi[ó]; Diaz unaccented at 2042 (crop); merced with plain c at 2036b; the ¡ without !
at 2031 and the ! without ¡ at 2053 and 2055; v. 2068 (mass next morning) for the forward reference. House
renderings: Infantes of Carrión, Garci Ordóñez, Ruy Díaz, amor → "favour" (2029, 2032, 2034), "my natural lord"
(as 44-48, 75-77), Alfonso / Alfons.

Refused / left as drafted:
- 2062 `i` "make ready a feast" for adobassen cozina: the next lines make it a feast. Left.
- 2052 `i` "bow before him" / "We salute you": this covers both omillarse 'humble oneself' and Pidal's
  'saludarle', and matches 83-83a "I bow before you". Left.
- 2054 `i` "we are working for your good": a fair rendering of andar en pro, and Pidal's 'somos vuestros buenos
  amigos' is in the note. Left.
- 2048 `l` "last-night" for anoch beside `i` "yesterday" (Pidal 'ayer'): `l` literal, sense in the note. Left.
- 2052 note "this is their first word to the Çid": nothing earlier contradicts it. Left.

Pass 1 counts: error 2 · weak 9 · style 4 (15 items).

## Pass 2: gloss.json

1. levantados · **error** · "past part. masc. pl., here with the force of an imperative" misnames the form. Done:
   imperative 2nd pl. levantad + enclitic (v)os; = levantaos.
2. ên · **error** · "= en … in" missed the contraction. Done: e + en 'and in', with the house parallels lâ, lês,
   mê, âquel.
3. valer · **error** · "valer me a Dios 'may God help me'" made the split future a wish, against the unit. Done:
   'will help me', = me valdrá.
4. omillámosnos · **weak** · "the s of -mos and nos run together in the spelling" is false: nothing is lost (the
   -s is kept, unlike modern -mo-nos). Done: corrected, and Pidal's sense 'greet' added.
5. omillan · **weak** · Pidal's omillarse a uno 'saludarle' added beside 'bow'.
6. catándol · **weak** · "the subject … probably the king; uncertain" and "gazing at him" did not match the unit
   (the king; le the owner of the beard). Done.
7. firió · **weak** · "sense inferred from the context, not certain" ignored Pidal's footnote. Done: Pidal 'echó
   pie a tierra'.
8. comidía · **weak** · "= comedir" as the modern form, with no Pidal. Done: Pidal 'como pensaba', 'como había
   dispuesto'; = pensaba.
9. __broaden__ parte · **weak** · "elliptical line, verb understood; could be read as a verb; uncertain": Pidal's
   footnote makes parte the object of dovos ('os doy acogida en mi reino'). Done: the new reading is "share,
   place, footing", citing Pidal.
10. __broaden__ tierras · **weak** · "sense inferred" ignored Pidal. Done: Pidal 'echó pie a tierra'.
11. __broaden__ don · **weak** · not needed: the glossary already has "also don — when, where (= donde, of time;
    Don llegan los otros …)". Removed.
12. __broaden__ ploguiere · **weak** · not needed: "(as long as) it may please … si vos ploguiere" already covers
    lo que ploguiere. Removed.
13. __broaden__ guisa · **weak** · not needed: "manner, fashion" with its phrases covers de tal / de aquesta guisa.
    Removed.
14. fossedes · **style** · "you be" changed to "(that) you were, would you were"; = fueseis.
15. viniemos · **style** · the example now says 'yesterday' (Pidal 'ayer'), as the unit does.
16. aínal, bócal, omildança · **style** · Pidal's glosses added ('tan pronto'; 'le besó en la boca';
    'acatamiento').
17. acuerdan · **style** · the modern form "= acuerdan" changed to "= concuerdan, se ponen de acuerdo".

Checked and kept: salen, yerbas, dientes, tomó, hinojos, fitos, dédesme, oyan, perdono, desde, levós, saludó,
huesped, ploguiesse, llegastes, otorgó, andamos, fartar, tántol, maravíllanse, claro, salie, adobassen, cozina,
comieran; __broaden__ querie, unos, sedie, sabe, demás, mando, avie, paga, feremos, razón, estar, si, quanto, a.
Every remaining __broaden__ is the glossary entry whole + " · " + the new reading (checked by script). The keys
equal novel-forms.json (39) plus __broaden__ (16). No entry is pinned to a line number, and no invented Pidal
attribution remains.

Pass 2 counts: error 3 · weak 10 · style 4 (17 items).

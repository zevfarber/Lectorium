# popol-vuh-021: drafter's notes

There are 47 units for 9 paragraphs (873 words). `cut.py` and `make_units.py` are unchanged from 020. `cut.json` has 70
pieces. `groups.py` merges consecutive pieces within a paragraph, and `units_src.py` holds mt / l / i / n. `make_units.py`
builds units.json and takes `t` only from cut.json, so no `t` was retyped. It prints:
`OK: 47 units, 9 paragraphs, 873 words, longest 45 (U4); paragraph starts at U1, 2, 15, 23, 24, 28, 35, 39, 46`.

The longest unit is U4 (one cut piece: the names of the seers and the first, long conditional of the boys' speech). It
cannot be split at a full stop. The heading couplet (U1) is kept whole. Each of the three question-and-answer pairs
(U8, U9+U10, U11–U14) keeps each question in the same unit as its answer, except where the cut pieces fall at a
semicolon.

## Checks run
- make_units.py OK (tiling, paragraph starts, one mt per WORD_RE token, the JSON loads).
- I compared every mt by script with the mt of the same manuscript form in published 001–020. Only one differs from a
  published spelling of that form: **xecah → xeqaj** 'they went down' (U26). The one published value is xekaj 'foot of
  the sky' (a different word), and the U26 note says so. Where a form has two published values, I chose by sense:
  ca qa 'we/our' or ka ongoing; cah qaj 'we want / go down' (U14, U40, U45); xcah xkaj 'they wanted' (U47); cab q'ab'
  'hand'; cam kam by the letters (U33 'die'; U44 'take (?)', where the word is uncertain); oc ok as the main verb
  'enter' (U41), oq after another verb (tix oc, cutun oc), as 001–020; cuꜭ kuk' 'with them' (U17, U37, U39), quk' 'with
  us' (U44, after Brasseur; 010 read the same phrase as kuk'); quetaam qetaam 'we know' (U21); quech kech; ꜭoh k'oj
  (U4); chi → chik before cut (U11, U23, U27, U30), and chi' 'mouth' in chu chi (U19).
- The forms that are new to the corpus are respelled letter by letter. I supplied an ejective only in eꜩanem →
  etz'anem 'game', aꜩiyac/aꜩiiac → atz'iyaq/atz'iiaq 'clothes', ꜭaztah/caztah → k'astaj (as published),
  cutunizah/xecutun → k'utunisaj/xek'utun (as published cutun), and ꜫihin → q'ijin (the letter is the tresillo, so
  nothing is restored). aꜩiiac keeps its ii in the toggle.
- README 5b: none (the establishment log has none).

## Proposed house renderings (not added to conventions.md)
- **Xulu, Pacam**: kept as names (mt Xulu, Pakam). The note gives Brasseur's notes (xulu 'divine'; Pacam from pac) as his.
- **chohim abah**: 'the heated stone' (as 018), also for the great oven here. **choh**: 'the oven (?)'. **chohibal**:
  'an oven (?)'.
- **vinac car**: 'fish-men' (Brasseur's 'hommes-poissons').
- **meba** (e caib meba, chi meba): 'poor men' (the two poor men). **xahol**: 'dancer(s)'. **xahoh**: 'dance' (the
  noun; xqui xaho 'they danced it').
- **The five dances**: kept as names. `i` uses Puhuy, Cux, Yboy, Xtzul, Chitzic, and mt uses Pujuy, Kux, Yb'oy, Xtzul,
  Chitzik. The note gives Brasseur's glosses as his (owl; weasel; armadillo; centipede; stilt-walker). Only Yboy
  'armadillo' is an ordinary word that I am sure of.
- **Xhunahpu** (U14): 'Hunahpu' in `i`. The note says that the manuscript has x- and gives Brasseur's diminutive.
- **ahaual ha**: 'the houses of lords'.

## Known forms used in a new sense (for the glosser's `__broaden__`)
cua 'spring (?)' (Brasseur quva), not 'once'; quih as qui ih 'their back (?)'; cul 'throat (?)' (in aꜩiiac cul qui cu);
chah 'say, answer (?)', not 'torch'; catoc 'we burn (?)' (coh catoc), not 'you enter'; hoc 'be ground (?)'; xac 'leaves,
branches'; quiy 'sweet (drink) (?)'; mich 'trick (?)'; tacal (of cries) '(?)'; cuz 'pleasing'; ꜭoh 'there is (?)' (Vve
ꜭoh ꜩonoxic); xecah 'they went down'; cam 'take part (?)' (U44); quixbic 'be ashamed (?)'; ia as part of quia 'many
(?)'; chih 'force (?)' (xe rah chih, xechihic).

## Doubtful readings from the establishment log, and where each is flagged
honel (U2); the blot after chicop / ꜭo (U2); the nicvachi-nel division (U3); caquinuc, the blotted mixoh, and ch-oc (U4);
the q-shaped ꜭux (U5); tacoh (U6); Vue, catoc against Brasseur's gat-oc, and the stroke in xchi|cuchah (U7); Ma vꜩ lo
missing in Brasseur, and ꜭaztah against caztah (U8, U33, U44); cahim (c against Brasseur's ꜭ) and cuchiqueic (U13);
cutunizah / cutun with c (U14, U27, U28, U29); achbilai que (U16); ca quiy (U20); queta-am and chivi / tana (U21); the
f-like t of taquic (U24); ꜫihin (U25); aꜩiyac / aꜩiiac, the marginal ?, and pu quih / cul qui cu (U29); Chiꜩic, with
Brasseur's Chitic (U30); the garbled Brasseur at libah chi … vinaquir (U31); v xenacahic, meaning uncertain (U34); the
q-shaped cuz (U36, U38); xqhao (U39); chi cah (U40); quiiꜩel (U41); gocam curaih naypu (U44); ca cah against Brasseur's
k'ah (U45); cax / cacrail with c (U46); xa chi mach cay (U47).

## Main uncertainties (all marked in the notes, most "(?)" in `i`)
1. **nabal (U1)**: 'remembrance (?)', after Brasseur's 'mémoire'.
2. **honel (U2)**: the word is doubtful and its meaning unknown. I gave 'attacking (?)' after Brasseur's 'attaques'.
3. **ma xa chicop choc chique (U4)**: I read 'we have not become mere beasts for them (?)'. Brasseur reads 'the brutes
   did not join them'. Both are guesses.
4. **que cumal (U5)**: que 'them' by the letters, but the sense needs 'us'. I followed Brasseur.
5. **ta coh catoc (U7)**: I took it as 'when we have been burned (?)'. Brasseur's gat-oc would give 'when we have been
   judged'.
6. **tix, xequeba, hoc / xhoc, queex, queic, cahim (U8–U13, U25)**: 'throw', 'hang', 'be ground' and 'meal' are all
   inferred from Brasseur and from the setting.
7. **ca quix ca chohih, qui la (U17); chopih, quiy, xicah (U20); coh i mich, chi vi tana (U21); culavachih, rip,
   hupuhuh (U22); yuyub, xulcab (U23)**: all read with Brasseur (inferred or guessed).
8. **Xchueca, pu quih, cul qui cu (U29)**: 'the next day' is inferred from chuvec. 'Backs (?)' and 'throats (?)' are
   guesses, and qui cu is left unrendered.
9. **hala (U30)**: I gave 'all kinds of (?)', from halahoh in 002. Brasseur has 'peu de chose'.
10. **Qui ia (U31)**: read as quia 'many (?)' with Brasseur. The toggle keeps the two words as written (Ki ya).
11. **pune (U33); v xenacahic (U34); xbochi (U38); ꜭo cam cu raih (U44); xelehebex, cacrail (U46); benam, quiamul,
    xechihic, mach cay (U47)**: all are guesses, mostly after Brasseur.
12. **Who speaks in U17 and U38**: these are messages that quote other speech. They are kept inside one pair of “ ” in
    `t`, as the log says. In `i` the quoted speech is set off with ‘ ’.

## Other decisions
- **Singular verbs with a group**: xcha (U36) with the lords and xuꜭhax (U38) with the messengers. I translated them
  as plural and said so in the notes.
- **The part ends at a Ximénez paragraph break (U47)**, as the log says. 022 opens with `Xe opon puch cuꜭ ahauab`.
- **Nothing was left untranslated.** The exception is the particles I marked as unrendered (qui in U15, qui la in U17,
  qui cu in U29, chi after Cate in U35).

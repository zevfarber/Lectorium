# popol-vuh-019 — review

## Pass 1

I checked all 50 units against conventions.md (the toggle rules and the house renderings table), runbook.md, ../run3/RUNBOOK.md
section 2, QUESTIONS.md (with the 019 establish entry), the packet and establishment log, the drafter's notes, units_src.py,
groups.py and make_units.py, the published parts 001–018 and the glossary. 018's review was the model for this one.

- **mt.** A script compared every token's mt with the mt of the same form in 001–018. Every new form's mt was read against its
  manuscript word under the toggle rules.
- **Grammar.** Every grammatical label in the notes was read against the form: person markers, ergative/absolutive,
  completive/ongoing, active/passive, plural.
- **`l` and `i`.** `l` was read against the K'iche' word by word, and `i` against `l`. I looked for remembered English and checked
  that couplets stay couplets.
- **Cross-references.** Every reference to an earlier part was looked up in that part.
- **Brasseur.** Every claim credited to him was checked in the OCR (lines 25590–25935: his K'iche' text, his French and his
  footnotes; line 8727 for 011's 'Maison des Lances d'Obsidienne').
- **Establishment log.** Every doubtful reading in the log was traced to its unit's note.
- **Images.** I looked at image 0061 for the two places the drafter or the OCR raised: U32 `ticon v ticon` and U22 `qui chacon`.

Edits were made in units_src.py by script, each one an exact-string replacement that had to match once. units.json was then
regenerated with make_units.py, which printed: `OK: 50 units, 10 paragraphs, 705 words, longest 34 (U22); paragraph starts at
U1, 6, 12, 17, 24, 28, 34, 37, 43, 48`. A script confirms that no `t` changed. groups.py is unchanged.

Counts: 0 major, 13 minor, 6 style.

### Changes

- U1 · n · minor · The note said "The part begins with the words that end 018 (are ta xahauax chiquech)". But 018 ends with
  `Xa coh bec,” xeꜭha ꜭaholab chique`, and `Are ta xahauax chiquech` is 018 U34, in the middle of the part. · The note now says
  the part opens with the words of 018 U34's Are ta xahauax chiquech.
- U6 · l · minor · `l` gave qui chacon as "their winning(?)", but `i` follows Brasseur with "the defeats (?)". The two layers
  disagreed in sense. · `l` now has "their beating(?)", which fits both readings, and the note already gives both.
- U8 · n · style · "(c- + aj 'want', as cah in 014)" did not say which c- this is. · Now "cah: c- 'we' + ah 'want', the verb of
  014's chi cah".
- U12 · i · minor · `ꜩaꜩ pu qui cha` 'many too (were) their plays (?)' was rendered "the boys played hard (?)". Nothing in the
  words says 'hard'; ꜩaꜩ is 'many, thick'. · Now "and many, too, were the boys' plays (?)".
- U12 · n · style · The note credited Brasseur with a note in ¶3 saying that cha plays on 'say', 'lance' and 'lancer'. That
  footnote is in fact attached to ¶4's chire cha ("Parlant alors aux lanciers (1)"). · The note now places the footnote there
  and quotes it ('le mot cha signifie alternativement le verbe dire ou parler, lance et lancier').
- U13 · l · style · `Que quicot` was glossed "They-rejoiced", although que is the ongoing c- + e, as the note says. · Now
  "They-rejoice".
- U15 · i · style · "they are ours, we have won them" added "they are ours", which is not in `ca chacom puch`. · Now "they are
  what we have won".
- U16 · n · minor · The establishment log lists acaba among its doubtful readings, but the note did not say so. · Added: "acaba
  is a doubtful reading in the manuscript".
- U22 · n · minor · The log lists chacab as doubtful, but the note did not say so. · Added: "a doubtful reading".
- U22 · n · minor · Brasseur prints `chi chacon ahauab` where the text has `qui chacon ahauab`. The note quoted his French but
  not this, and the log is silent. On image 0061 (line 3) the word is `qui` (q-shaped letter, then ui). · Added to the note,
  with the manuscript followed. Flagged for the record (below).
- U26 · i · minor · "what we have won from them" attached cumal 'by them' to the winning. In `l` it belongs with rilo 'see'
  ("he-sees-it our-won-thing by-them"). "else" also came from Brasseur's 'ailleurs', not from the K'iche'. · Now "From where
  could they come to see what we have won? Nowhere."
- U28 · n · minor · The note said "as nao 'feel' in 007, 009". 009 has no nao. · Now "as nao 'feel' in 004, 006, 007 and
  012", the published places (xca nao, xunao, xquinao, xqui nao).
- U29 · n · minor · The note said "009's racuh with vchi", but racuh … vchi occurs in 005–007, not in 009. · Now "the racuh …
  vchi of 005–007".
- U32 · n · minor · The note asked for the image to be rechecked at `ticon v ticon`. Rechecked on 0061: both words stand on one
  line, `chahal hcon vhcon huncame`. The second word carries v- 'its', and there is no line break between them. So this is not
  a clear dittography, and README rule 5b does not apply. The text reads as an apposition ('guardians of the garden, the garden
  of Huncame …'), which `l` and `i` already give. · The note now says this. It also says that Brasseur prints only one ticon
  (`chahal ticon Hun-Came`) and that the log is silent. `t` is unchanged.
- U33 · n · minor · The log lists elecai as doubtful, but the note did not say so. · Added: "a doubtful reading".
- U33 · n · style · "re is perhaps 'their teeth' (r- + e)": r- is the singular 'its'. · Now "(r- 'its' + e 'tooth', for the ants
  taken together)".
- U36 · l · minor · `xnoh` has no ergative and is intransitive: the note's own 'it was filled'. But `l` had "they-filled". · Now
  "it-filled".
- U43 · mt/l/i/n · minor · `ca vilo` was analysed as "ca 'we' + vilo, the v perhaps a glide", with mt qa wilo. In this hand,
  v- before a vowel is the 1st-person singular ergative. Published 017 has the same form twice (U19, U25), analysed there as "ca
  vilo 'I see it': v- 'I' + il 'see' + -o", with mt ka wilo. The 'glide' was special pleading. · mt ka wilo. `l` "I-see-it". `i`
  "These are our own flowers I see here". The note now gives the analysis as in 017, says that one lord speaks for the rest,
  and gives Brasseur's 'we' (kav'ilo, 'que nous voyons') as the other reading.
- about · style · "the blades are meant to cut them to pieces" overstated the text, which says 'be cut, quickly … die'. · Now
  "to cut them down".

### mt against the published parts

After the edits, two forms have an mt that differs from the published mt for the same letters. Each is a different word:
- `cana` q'ana 'yellow' (U10), against 010's kana 'left behind';
- `ꜭux` k'ux 'gnaw (?)' (U34, by the letters), against k'u'x 'heart'.

The forms with several published mt were each checked against person and sense:
- ca, chique, que, qui and cuꜭ go by person: narrative k-, and the speakers' own 'we/us' q-. ca is also ka where it is the
  ongoing (U3's first ca, U8, U33–35, U37 ca ꜭha, and now U43 ca vilo).
- cah is qaj 'go down' (U5, U21, U35, U48) and kaj 'four' (U8). U8's first cah is qaj 'we want' (q- + aj), the same letters
  as 'go down'. This is stated in the note.
- cab is kab' 'second' (U17, as 018) and q'ab' 'arm' (U29).
- chi is chi, chik (where it stands for chic) or chi' 'mouth'. he is je 'go' (U7) and je' 'tail' (U34, U44). xe is xe and xe'
  'root' (U46). oc is ok 'enter' (U17) and oq 'already' (U25, Mier oc).
- cu is k'u, but ku in U39's cu caam (c- + v-). caam is kaam, as 016 U39's cu caam. 001/002/015/016's caam k'a'm 'vine' is a
  different word.
- cam is kam 'die' (U1, U18) and k'am 'take, bring' (U37, U47), as published.
- Ha is ja 'house'.

All other known forms match the published mt.

### Rulings on the drafter's open points

1. **U25/U26, the lords' charge split at its question (46 words together).** Kept split. No rule forbids splitting a speech
   at a sentence boundary: the tap-unit is the sentence, and only couplets may not be split. The published parts have 136 units
   whose quotation marks open or close in another unit. The cut falls at `cumal?`, a full question, and neither half breaks a
   couplet. U25's note already says the charge runs on.
2. **U7 `“He na qui cut,” xa xeꜭha ꜭaholab.`** Kept with the boys. The establisher punctuated it by the house tag rule (a tag
   closes the speech before it), and QUESTIONS (019 establish) records this as decided meanwhile. The note gives Brasseur's
   one-speech reading with his French. Both his K'iche' (`He na qui cut xax e cha qaholab, xa-cucha ca kah cah tzel cotzih,
   x-e cha Xibalba`) and his French were checked. The exchange reads well as punctuated: the lords ask what they will win, the
   boys answer "go on, then", and the lords name the flowers. `i` "was all the boys said" for xa xeꜭha is a fair rendering of
   xa 'only, just'.
3. **`cana` → q'ana.** Accepted. The word is certain from its place in the colour list (caca 'red', zaqui 'white', cana, with
   carinimac), and Brasseur's g agrees. Plain c → q' is the same step as plain-c acab → aq'ab' (015/016) and 010's Ahalcana →
   Ajalq'ana.
4. **catacox → q'atakox, elecaxic/elecai → eleq'axik/eleq'ai, Chai → Chay.**
   - catacox: accepted for consistency with 011's xcat → xq'at (QUESTIONS 011 point 3), which rests on the same grounds
     (Brasseur's g and the sense). The word's identity here is only inferred, though, and the note says so. If the owner rules
     that an inferred word gets no supplied mark, 011 and 019 change together.
   - elecaxic, elecai: accepted. 'Steal' is certain from the context (the lords' charge, the guardians' punishment `chi
     elecaxic`), and Brasseur's g agrees.
   - Chai: Chay is a respelling only (final -ai → ay, as published nai → nay); no mark is supplied.

   Noted for the owner: this part also keeps -ai in choi and elecai, as published xkanai and pixab'ai. The published practice
   is already mixed.
5. **U32's second `v ticon`.** Image checked; not a clear dittography (see Changes). Kept, and the note now says why.

### Refused

- U21 `cah chi vi cha`: chi left as chi. 018's review made chi vi chik where it stood for chic 'again' (011/012 precedent). Here
  'again' does not fit (the blades had not gone down before), and the note marks chi as unclear. Same as 018's ca chi rox.
- U1 `chi cha` 'at the ball court (?)' and U12 `qui cha` 'their game (?)': kept. Both are marked as guesses, the alternatives
  (blade, Brasseur's 'lances') are in the notes, and the context of ¶1 and ¶3 is the game. In ¶4 cha is the blade, and the notes
  say so.
- U13 `nabe` "for once": kept. It is a natural English sense of 'first (time)', and the note gives 'the first time they have
  won' and Brasseur's 'tout d'abord'.
- U30 "uttering the same song over and over" for xavi xere chi qui ꜭhabeh ri qui bix: kept. xavi xere 'just so, only this'
  carries the repetition, and Brasseur's 'répétant le même chant' agrees.
- U33 "carrying the flowers off up the trees" for vloc 'hither': kept. "Hither" from the ants' point of view is awkward in
  English, and the direction is in `l`.
- U34 `ꜭux` mt k'ux: kept. The verb is respelled by the letters and nothing is restored. 'Gnaw' is inferred and marked.
- U44 `xcuyu` 'it was spared (?)': kept. It is marked, and the form (no ergative written) is left unanalysed in the note.
- U18 `catacox` analysis (ꜫat + -ac + -ox, a passive): the suffixes are not otherwise attested. The note marks the whole as
  inferred. Kept.
- acab with plain c (U15, U26, U16 acaba, U22 chacab, U41 acabil): printed as established. The aꜫab/acab difference with 018 is
  already in QUESTIONS (019 establish point 2), and U15's note says so.
- Establishment log: every doubtful reading is in its unit's note, as are the letter forms (t written like h in huticab, v
  tiohil, ticon ×4, tiquitoh, tique; mabu; cari; the g-shaped ꜭ and ꜭh; q-shaped ꜫuz), the blots (U12, U43), the X in the
  margin (U35), the struck `ri hun chi` and the caret (U1), and the speaker tags (U7, U49). Nothing else to change. One
  slip in the log itself: it says "as 015/018's ꜫuz", but ꜫuz is published in 015 and 017, not 018. The note (U39) correctly
  says 015 and 017.
- Brasseur: the other quotations and readings the notes credit to him are in the OCR, allowing for OCR noise. They include:
  'dans le jeu de paume', 'prenons maintenant la vôtre', 'ce qui mit aussitôt fin à la partie', 'ayant compté', 'leurs
  défaites', the chako footnote, the one-speech reading of He na qui cut, xa-cucha ca kah, 'un bouquet', huticab caka-muchih /
  zaki-muchih / gana-muchit / carinimak, the chipilin footnote, r'utzqui qux, 'tout d'abord', 'pris au piége', qama, agab,
  ch'y ya, 'nous sommes les gagnants maintenant', Agaba / 'Cette nuit également', 's'avisant mutuellement', Chàim-ha / 'la
  Maison des Lances', gatacox / 'tués par les lanciers', the cha/chai footnote, 'Par des promesses ils séduisent leurs
  gardiens', 'unanimement ils baissèrent leurs armes', ch'agab, the zanic/Chequen/zanpopo footnote, 'Fourmis tranchantes', pe-ne,
  oh y qama / 'allez chercher', qamol, 'jardin', 'D'avance', 'Quant à vous', elegaxic, 'Où donc', 'Veillez', xalog, rakuh,
  'criant de toutes leurs forces', gab, 'cheminant sur leurs jambes', chabeh, the night-watch footnote (x-pur pu-veh, 'est entré
  dans la nuit', pu huyu), ch'ogic and the og footnote, elegai / 'dérobant', 'ce qui était commis à leur garde', 'allant et
  revenant en troupes innombrables', 'coupant', 'les plates bandes de fleurs', tuguvic, ziqou / 'répandaient une douce odeur',
  cux / 'étant à scier', the 'allusion' footnote, 'c'était une moisson de fleurs', ca cu kah uloc, Libahchi, 'tout pleins',
  (akone!, qam, 'ce dont nous avons parlé', curi, c'u caam / 'ceux-ci prirent', guz / 'dont l'aspect faisait plaisir', 'Ils
  allèrent ensuite chercher', zakcah e / 'changèrent de couleur', 'leurs faces pâlirent', m'yx ya, x-e uchax chahal, 'On n'a
  même pas épargné nos queues', 'on leur fendit les lèvres', 'pour les châtier …', 'le commencement de leurs travaux', herebak,
  the Purpuek / Parpuak footnote, 'ils jouèrent de même tous ensemble', 'ayant achevé de jouer', 'en terminant'.
- House renderings: Vꜩ bala "Very well" (11×), ahau "the lord", Chaim Ha "the House of Blades (?)" (as 011, "(?)" at first
  mention), Vvcub Came → "Vucub Came", Huncame, Xibalba, Hunahpu, Xbalanque all as published. No remembered English found;
  "brought low" for chacatah is the published rendering (002, 010, 012, 014, 018).
- Couplets in `i`: U18 (chi qui ꜭux … chi qui ꜭux), U22 (quix petoc, quix oho), U33 (chuvi che … chuxe che), U34 (ca ꜭux qui
  he, ca ꜭux qui xic), U35 (re ca …, re ca …), U39 (ahau, ahauab) and U47 (qui chi herebac, qui chi Purpuec) are all kept
  as pairs.

### For QUESTIONS.md (publisher)

1. U32 `chahal ticon v ticon Huncame`: image 0061 rechecked. Both words are on one line, the second with v-, so this is not a
   clear dittography. Printed and rendered as written (apposition), and Brasseur's single ticon is in the note.
2. U22 `qui chacon ahauab`: Brasseur prints chi chacon. The manuscript (0061 line 3) has qui. The establishment log is silent;
   the note now says so.
3. U43 `ca vilo` is now 'I see it' (mt ka wilo), with published 017, against Brasseur's 'we'.
4. Marks supplied on Brasseur's g and the sense: q'ana (U10, colour certain), eleq'axik/eleq'ai (U25, U33, U43, U45; 'steal'
   certain), and q'atakox (U18). q'atakox is inferred and kept only for consistency with 011's xq'at (011 point 3). If inferred
   words are to get no supplied mark, 011 and 019 change together.
5. The -ai ending: Chai → Chay (as published nai → nay), while choi and elecai keep -ai (as published xkanai, pixab'ai). The
   published practice is mixed; a house rule is wanted.
6. U7 attribution: as decided meanwhile in the 019 establish entry. Nothing new.
7. The drafter's proposed house renderings (drafter-notes.md) are not added meanwhile: Chaim Ha; zanic 'the ants'; Chai /
   Chequen zanic kept as names; coꜩih 'flower(s)'; cah ꜩel coꜩih 'four bowls of flowers'; chahal / chahalib 'guardian(s)';
   ticon 'garden'; Puhuyu, Xpurpuvec, Purpuec kept; muchih / muchit / carinimac kept with colours translated; chacon / chacom
   'what (we) have won'.

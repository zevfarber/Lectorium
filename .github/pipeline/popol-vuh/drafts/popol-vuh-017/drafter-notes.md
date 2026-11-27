# popol-vuh-017 — drafter's notes

60 units for 19 paragraphs (966 words). The 122 cut pieces in cut.json are merged only within paragraphs, and only
consecutive pieces. Each speech is kept with its tag. The louse's message (¶17) runs over four units (U48–U51), split
at its semicolons and full stops. The long nested speech of ¶3 is split in two (U4–U5), with the tag on the second.
The longest unit has 28 words (U60, ¶19). Every `t` was built by script from cut.json, and the cut was made by
script from packet.md. The check passes: the units tile the 19 pinned paragraphs of packet.md exactly; each paragraph
starts a unit (U1, 2, 4, 6, 8, 11, 13, 16, 21, 26, 29, 32, 36, 39, 42, 45, 48, 54, 59); every `mt` has one entry per
WORD_RE token; the JSON loads.

## (a) Decisions a reviewer should know

1. **The README 5b corrections.** The note to U2 opens "The manuscript has mi xuhquiba, a misprint for mi xu
   tiquiba, corrected here". The note to U59 opens "The manuscript has hun nahpu, a misprint for Hunahpu,
   corrected here".
2. **catit / ca- by person**, as 014–016. In the narrative, `ruꜭ catit` (¶4, ¶17), `xꜭha ri catit` (¶6) and
   `chire catit` (¶17) are katit, and `cochoch` 'their house' is kochoch (¶4, ¶19). In the twins' speech (¶18), `ix
   catit` is qatit and `chu nicahal cochoch` is qochoch 'our house'. The lords' `pa ca vi` and `chi ca vach` (¶2) are
   qa, and so are the twins' `ca ꜩih`, `ca camic`, `ca chuch`, `xchi ca canah` and `xchi ca tic`. The ongoing ca (ca
   vilo, ca anic, ca ꜩihon, ca ziquinic, ca canahic, ca pe, ca nu taco/bico) is ka.
3. **Restorations and marks supplied where the word is certain:**
   - bico / xbic / xa bic 'swallow' → b'iq'o / xb'iq' / b'iq'. The MS has plain c; Brasseur has bigo/big (his g =
     ꜫ); the modern verb is b'iq'. The published `bic` (b'ik, 'going', a doubtful reading) is a different word, and
     the note to U42 says so.
   - xpec 'toad' → xpeq (Brasseur Xpek, his k = q; the modern word xpeq).
   - cazlic 'alive' → k'aslik (Brasseur qazlic; the word of ꜭazlem 'life').
   - quih in `qui quih` 'their day' → q'ij, as 016's `tiquil quih` (still open there).
   - chaquihic → chaqi'jik and nicahal → nik'ajal, following the published chaquih chaqi'j and nicah nik'aj.
   - caztah → k'astaj, the published form (Brasseur qaztah).
   - quitzih (written with plain t + z) → qitzij, as the published quiꜩih.
   - ꜩonoh → tz'onoj, as 016 (the supplied tz' on the plain ligature is still open).
   - quetzabal (plain t + z) → ketz'ab'al, the published mt of queꜩabal (009 point 1). etzanem and etzanic stay
     etzanem and etzanik by the letters, as 006's eꜩeyah (etzeyaj). So the 'play' root has tz' in one word and tz in
     the other. This follows the published forms, but the two should be decided together.
4. **mt differing from the published mt for the same letters** (script check; these are the only ones):
   - `camoc` k'amoq, against 007's kamoq 'let him die'. Here it is 'to take, fetch' (Brasseur qam-oc, 'pour
     prendre'), the 'take' verb given k'am in 015–016. The same applies to `xu cam` in U26 and U28.
   - `bic` b'iq', against the published b'ik (see 3).
   - `acan` akan ×2 (U43), against the published aq'an. The published form is the climbing word 'up' (acanoc in
     U13 keeps aq'an). Here it is 'leg, foot', the leg word of the published racan (rakan), without a possessor.
5. **Left by the letters, not restored.** These words are uncertain: echaahel, etzanem, quixbic, nicnot, hoc,
   tocol, chahic, xchoye, tzelavachixic, cayac, malmat, chavah, taconel, anaic/anic, vilo, xrictaxic, Zaquicaz
   (Saqikas, zaqui as saqi), oho, chan, ꜩuꜩil, xꜭhacachob, vacco/vac (wak), ꜩelet, xcachoh, vmucubal, taquiquil,
   caxꜩ, chaiic, ꜭaxtoy, xiic, vvarachac, rech/xrech, zucah (sukaj; Brasseur's tzukuh is the ꜩucuh 'seek' of 007,
   written here with plain z), nacal, chava re, ꜭhanic, chac, pixabai/pixabay, vtux, ah 'cane', xticou, loꜩ.
   - **The cry word** oꜫ is written with plain c in xoc, v oquibal, choquic, coquic and mix oquic. Its mt is ok- by
     the letters, as 015's choc 'cried' (open there); Brasseur's g and the modern oq' would give oq'.
   - **The plain-ch 'say' forms** (quecha, cacha) are kecha and kacha, as the published cacha. xuchax is xuch'ax, as
     the published xuchax.
6. **Names.** Hun Came is written as two words here (mt Jun Kame), where 009–012 had Huncame; `i` keeps the
   published "Huncame" and "Vucub Came", and so does "Vucub Hunahpu". Tamazul is kept as a name: Brasseur's
   footnote derives it from Nahuatl tamacolli 'toad', and the note gives that. Zaquicaz is kept untranslated. vac is
   "the falcon" in `i`, matching the part title. The note gives Brasseur's footnote, which ties it to 009's Voc and
   to xic 'the hawk' of the next sentence. `ri xic` (¶10) is the bird, rendered "the hawk", although published 009
   keeps Xic as a lord's name. The note says so.
7. **Person and voice.**
   - U2 `mi xu tiquiba` is singular, with the plural sense (the fixed xu-/xrah construction).
   - U4 `Xe taco vloc` is ambiguous: 'they (the lords) sent' or 'they (the boys) were sent for'. The note gives both.
   - U36 `xu binaah cumal` has the ergative written with 'by them', as 015's xu binaah.
   - U45 `xqui rech` / `xrech cumal` are read as the active and passive of one verb.
   - U59 `xticou` is read as the -ou agent-focus form 'it was Xbalanque who planted' (inferred, as 014's xe chacouic).
   - U60 has singular `xu tic` and plural `xqui tic` for the same act.
8. **Nested speech.** As the establish entry decided, the text prints the lords' words inside the messengers', and
   the grandmother's inside the louse's, within one pair of “ ”. `i` marks the inner level with single quotes: U4–U5,
   U15, U48–U51, U56–U57.
9. **Doubtful readings in the establishment log, each in its unit's note.** The t-as-h letter forms are in U8, U51,
   U53, U55, U28 and U42. The r-as-v forms are in U10, U12, U31 and U34. a/u: xu tic U59, xul U49, curi U29, chaahic
   U1. The other readings:

   | Reading | Unit |
   |---|---|
   | mi xuhquiba | U2 |
   | the ink blot in He cu itaca | U3 |
   | nima hoc, ca tocol | U6 |
   | que chahic | U7 |
   | qui quih | U9 |
   | ꜫuz (the g-shaped letter; the sense against 015) | U12 |
   | chimalmatib | U13 |
   | que bico v xpec | U26 |
   | que tio v cumatz | U28 |
   | xꜭhacachob | U29 |
   | xoc, oquibal | U30 |
   | chogquic / choquic | U31 |
   | Caꜭhau oc (MS caghauoc) | U39 |
   | xuchax | U41 |
   | chu caxꜩ with the supralinear x | U42 |
   | xrah chaiic, ꜭaxtoy, xiic vvarachac | U43 |
   | zucah against tzukuh | U45 |
   | chavare | U46 |
   | ꜭhanic; v chac against Brasseur's u bi | U47 |
   | caztah (MS catzatz / caztahz) | U50 |
   | coquic, cacha | U51 |
   | cazlic | U57 |
   | ix pu ca chuch (pu not in Brasseur), mix oquic | U58 |
   | hun nahpu, xticou | U59 |
10. **Brasseur.** Every French quotation in the notes was checked by script against the OCR (lines 24560–25065).
    All of them are there, allowing for OCR noise and the interleaved footnote columns. The quotations include:
    - the footnotes on Tamazul, ba, vac/voc/xic, Lotzquiq and the dropped n of xi;
    - 'At viy, toi neveu (ou petit-fils)';
    - 'il y a ce signe de notre parole qui est resté avec vous'.

    ꜫuz in U12 cites 015's 'plaisir' as that part's reading (from the published glossary entry), not this passage.

## (b) Proposed house renderings (not added to conventions)

| K'iche' (MS) | `l` | `i` |
|---|---|---|
| vꜭ | louse | the louse (mt uk') |
| xpec / Tamazul | toad / Tamazul | the toad, Tamazul (kept as a name; note: Nahuatl 'toad' after Brasseur) (mt xpeq) |
| cumatz / Zaquicaz | snake / Zaquicaz | the snake, Zaquicaz (kept as a name) |
| vac | falcon | the falcon (mt wak; its cry vacco) |
| xic (the bird) | hawk | the hawk (in 009, Xic, kept as a lord's name) |
| vvcubix | in-seven-days | in seven days |
| Ꜭo ba nu ꜩih chi nu pam | there-is (ba) my word in my belly | There is a word I carry in my belly |
| loꜩ quic | lotz rubber | lotz quic (kept; the remedy's name) |
| ꜭaxtoy | deceiver | cheat (cf. ꜭaxtoꜭ 'deceiver') |
| ah (planted) | cane | a cane |
| rax vleu / chaquih vleu | green earth / dry earth | green earth / dry earth |
| pixabai, pixabay | taking-leave | take their leave |
| taconel, tacol | messenger, summoner | the messenger, summoners |
| bico, bic | swallow | swallow (mt b'iq', restored) |

## (c) Open questions

1. bico / xbic / xa bic → b'iq' (restored), and xpec → xpeq, cazlic → k'aslik: confirm. These are the 007/010
   practice, where the word is certain and Brasseur's letter agrees.
2. The cry word oꜫ written with plain c (xoc, oquibal, choquic, coquic, mix oquic) is kept ok- by the letters, as
   015's choc. Should all of them, with 015, become oq'?
3. The 'play' root: quetzabal is ketz'ab'al (published queꜩabal), but etzanem / etzanic stay etz- (006's etzeyaj).
   Decide together (009 point 1).
4. U43 acan 'leg' is mt akan, after racan rakan; the modern word is raqan (008 point 5). Decide together.
5. U12 ꜫuz is read 'grieving (?)' here, after Brasseur's 'triste', against 015's 'delight (?)'. The glossary entry
   needs a broadening, or one of the two readings is wrong.
6. ri xic (U28) is 'the hawk', while 009 keeps the lord Xic as a name. Should 009's note mention the bird?
7. Glosser: broadenings are needed for:
   - quih (q'ij 'day', the second instance);
   - camoc (k'amoq 'to take', against 007's 'die');
   - bic (b'iq' 'swallow');
   - acan (akan 'leg');
   - xic (the bird);
   - quecha (kecha 'they say', the published entry being 'their food');
   - chac (u chak, perhaps 'prey');
   - rech (the 'open' verb);
   - ah (aj 'cane');
   - re (teeth?);
   - chi ('mouth', chi', in pu chi);
   - coh (koj 'put', U36);
   - oho;
   - tio ('eat' with u cumatz);
   - ꜫuz ('sorrowful', guess).
8. U14 / U19 `ca nu taco`, `ca nu bico` 'that I send / swallow you' have no written 'you'. The reading is inferred
   from the sense and from Brasseur ('aimerais-tu que je t'envoie', 'Veux-tu que je t'avale').
9. U2 `Apa china`: apa is 'where' elsewhere, and the pair is read as 'who' with Brasseur. Confirm.

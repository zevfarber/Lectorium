# popol-vuh-016 — drafter's notes

56 units for 19 paragraphs. The 94 cut pieces are merged only within paragraphs, and only consecutive pieces. Each
speech is kept with its tag. The long speech of ¶13 is split at its semicolons into three units (U34–U36), with the tag
on the last. The longest unit has 35 words (U5, ¶2: the speech with its two `ix catit` and the tag). Every `t` was built
by script from cut.json. The check passes: the units tile the 19 pinned paragraphs of packet.md exactly; each paragraph
starts a unit (U1, 5, 7, 9, 12, 13, 16, 18, 22, 26, 29, 32, 33, 37, 39, 43, 45, 49, 52); every `mt` has one entry per
WORD_RE token; the JSON loads.

## (a) Decisions a reviewer should know

1. **catit / cabix by person**, as 014–015. In speech, `ix catit` (¶2 ×2, ¶15) and the twins' `ri catit` (¶13 to the
   rat, ¶18) are qatit, and `ri cabix` (¶1, ¶2) is qab'ix. In the narrative, `chire catit`, `ruꜭ catit`, `re catit`,
   `xꜭha catit`, `chuvach catit` and `ca tahin curi catit` are katit. `chique` in the twins' speech (¶2) is chiqe 'to us'.
2. **cho 'rat' → ch'o (restored).** The modern word for rat and mouse is ch'o, and the word is certain. This is the
   only token whose mt differs from a published mt for the same letters: cho 'lake' in 001 is cho, a different word.
   If the owner wants the letters only, all 14 cho → cho.
3. **Other restorations and supplied marks where the word is certain** (the 007/010/015 practice):
   - catoh → q'atoj (as 015) and acab → aq'ab' (as 015).
   - quih → q'ij (U38 `tiquil quih` 'noon'). It has a plain qu, where the house word is ꜫih, and the glossary's quih
     is kij 'juice'. This needs a check.
   - quinac → kinaq' 'beans'.
   - iꜩocopih → itzoqopij: q for c, the modern tzoqopij 'let go'.
   - tz' supplied on the plain ligature for the 'close, stop up' family (ꜩapitah, ꜩapitahic, ꜩapih, ꜩapi →
     tz'apitaj / tz'apitajik / tz'apij / tz'api) and for ꜩonoh → tz'onoj 'ask'. This is the 015 tz'iloj precedent, and it
     is still an open question there.
   - avetaam → aweta'm (the double vowel as a glottal stop).
4. **Left by the letters, not restored.** These are uncertain words: varah waraj, baꜩonic b'atzonik, maꜩehe matzeje,
   mucumuxinac, cuchu, zep sep, tiꜭil tik'il, chauiheic chawijeik, iaclin yaklin, nebebic, yopih, xcupu, xzcatac,
   catat katat, xambe, ꜩoꜩotic tzotzotik, cateh katej, ze se, cul kul, yoteh, bio, bari, xequel xekel, quel kel,
   cuvvn kuwun, mezcutahinac, cuxu, vchah, quril kuril, nohinic, ca quil ka kil, cutu / xcut / cutum (kut-), ꜩahiꜩah
   tzajitzaj, quia, hizabah, cat kat, mahix majix, vah waj, quum kuum, canaic kanaik, and cacou kakow (the modern word is
   kakaw; a vowel, not a mark). In `cu caam` 'carrying' (U39) the mt is ku kaam, the letters, as 014's cucaam. The
   vine word caam is k'a'm.
5. **The 'take' verb** is k'am, as in 015 (open question 007/3 etc.). It occurs in xcam qui naoh 'they took counsel'
   (U3, U4, U37, as 006) and in xu cam (U15, U20). `xcam vi icahau` 'your father died' (U28) is xkam.
6. **chupan → chupam**, as published 011's chupan. The MS ending in n is noted.
7. **Water and house**: ha 'house' → ja (chi ha, chuvi ha, xiquin ha, pu tum ha, pa ha, pu vi ha); ha 'water' → ja'
   (ca ha pa quebal, yacal ha chel). ya and a 'river, water' are kept as in earlier parts. vvb → wub'.
8. **Renderings chosen.** The ball gear is rendered as in 009/010: bate 'rings', pachcab 'hand-guards', quic 'the rubber
   ball', queꜩabal 'gear for play'. quebal is 'jar', after Brasseur. The published keb'al 'household things' is a
   different sense and needs broadening. vbac vvach is 'its eyes' (house). xan is kept as the creature's name; the text
   glosses it as like vz 'gnat'. zaquil ic is 'white chile', not the house 'clear light'. tum is 'cords (?) of the roof'
   here, after Brasseur's note, not 015's 'brambles'.
9. **Doubtful senses, marked (?) in `i` and labelled in `n`:**
   - ¶1: Xa vi xuban chi rib 'done of itself' (inferred: the tools again; Brasseur has the twins); Ana vi 'perhaps';
     ca bano vlo; la quita; chi ca rileo 'catch'.
   - ¶2: coh michouic 'someone makes fools of us'; chi puch.
   - ¶3–¶5: xe baꜩonic 'armed'; xe chauiheic 'speaking'; Que nebebic 'thronging'.
   - ¶6: xa cuchu he 'tails bunched'; xcupu cab 'snapped off'; xzcatac 'short'.
   - ¶7–¶8: catat 'burning'; v xambe 'last'; ca ꜩoꜩotic 'hopping'; cateh, ze pa cul, yoteh, bio 'blocked, wrapped in a
     cloth, squeezed, choke'; biye 'pop out'.
   - ¶10–¶13: xequel 'hanging'; cuvvn / mezcutahinac 'stored / swept up'; vchah 'say'; quril 'she sees me'; coh nohinic
     'ready'; the first ca of `ca ca ya`; ca quil 'is seen'.
   - ¶14–¶19: hun acab 'through the night'; Qui cu tiquil quih 'noon'; yacalic 'openly'; cutu / xcut 'grind'; ꜩahiꜩah
     'pour out'; chi cama cu quia 'fetch a drink'; numic 'hungry' (Brasseur: thirst); hizabah 'choking'; coh vꜩin 'done
     for'; xu ca cat 'cut'; quum 'leather'; mahix 'seized'; que vah 'hid'; canaic 'was left'.
10. **Grammar points.** U9 has xe cuchu cu quib, with the absolutive xe where a reflexive would take xqui; the note
    says so. U22 Ma ta qui camic is read 'let me not die' with Brasseur, though no n is written. U13 xrah … qui chapo
    and U15 xu cam are singular verbs with the twins as the doers.
11. **The establishment log, traced unit by unit.** Every doubtful reading and every reading against Brasseur is in
    its unit's note:
    - Cate / catte U1; ruꜭ with comma U2; xcam with plain c U3; chi ca rileo U3; Naqui ri lo / vilo U5; qui bic / bie
      U8; tiꜭil U10; the missing `ta xe petic, xe chauiheic conohel` U10; xa cuchu he U14; xcupu cab / cub U14; yac
      / iac U16; aꜫ U16; catat U17; pa cul U19; ꜫaꜫ U20.
    - ꜭaholab q-shaped U21; Ma ta qui camic U22; ꜭo / go U22, U34; chabiyh with plain ch U23; queꜩabal / xequel
      (Brasseur's omission) U27; cuvvn U32; vve quril U33; co plain c U35; ca quil / k'il U36; quih with plain qu
      U38; yacalic / yaçalic and libah chi U40; ca ha / cu ha and the cu over ca U43; chupan / chupam U46; chel and chu
      tiho U48; xu ca cat / gat and quum / tzuum U50; vbeel / u heel U51.
    - One addition the log does not flag: at ¶13 end, Brasseur's text reads `xa pu ka ti ca kil vi` where the image
      (as established) has `xa pa cah ca quil vi`. The note to U36 says so.

## (b) Proposed house renderings (not added to conventions)

| K'iche' (MS) | `l` | `i` |
|---|---|---|
| cho | rat | the rat (mt ch'o, restored) |
| bate, pachcab, quic (ball gear) | ring, hand-guard, rubber | rings, hand-guards, the rubber ball (as 009/010) |
| quebal | jar | the jar (Brasseur 'cruche') |
| vvach quebal | its-face jar | the side of the jar |
| xiquin ha | corner house | the corner of the house |
| cutum ic | chile-sauce | chile sauce |
| tiquil quih / tiꜭil vꜭux acab | planted sun / planted its-heart night | noon / the very heart of the night |
| xan | xan | the xan (kept; 'like a gnat') |
| ꜩapih, ꜩapitah | close, be-closed | stop (the jar) (mt tz'apij, tz' supplied) |
| ixim, zaquil ic, quinac, pec, cacou | maize, white chile, bean, pek, cacao | maize, white chile, beans, pek, cacao |

## (c) Open questions

1. Should cho 'rat' get ch'o (restored, as drafted) or stay cho by the letters?
2. Should quih in `tiquil quih` get q'ij (as drafted)? The glossary's quih is kij 'juice'.
3. Should the tz' be supplied on the plain ligature for tz'apij and tz'onoj? This is the same question as 015's tz'iloj.
4. Glosser: quebal needs a broadening to 'jar'; tum needs 'cord, lashing (of a roof)'; ha 'house' / 'water' is
   already covered; xe 'beneath' as in 015 (no broadening).
5. U2 `Xa vi xuban chi rib vleuh` is read as the work again being done by itself, against Brasseur's 'ils en firent de
   même'. Either reading fits the letters.

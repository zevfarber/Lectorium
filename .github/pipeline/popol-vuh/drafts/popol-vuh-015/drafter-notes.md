# popol-vuh-015 — drafter's notes

49 units for 20 paragraphs. The 90 cut pieces are merged only within paragraphs; couplets and speech + tag are kept
together; the longest unit has 35 words (¶14, the axe sentence, kept whole so that `chu ban ri xa huna icah` stays
with its verb). Every `t` was built by script from cut.json. The check passes: the units tile the established text
exactly, each of the 20 paragraphs starts a unit, and every `mt` has one entry per WORD_RE token. (The brief said 22
paragraphs, but the pinned text and cut.json have 20.)

## (a) Decisions a reviewer should know

1. **catit / caꜩ by person**, as 014: `ix catit` and the twins' `ri catit` (¶16, to the dove) → qatit; narrative
   `ri catit cuꜭ`, `chire catit`, `rumal catit`, `chuvach catit` → katit; `ri caꜩ`, `qui ꜫexel caꜩ` (speech) → qatz.
   `ca chuch` (speech) qa chuch; `cabix` (narrative) kab'ix; `cochoch` (narrative) kochoch.
2. **coy** ×2 (`Hunahpu Coy`, `ri coy`, `e coy`) → k'oy / K'oy, as 014 (house ꜭoy).
3. **Restored marks where the word is certain and Brasseur's letter agrees** (the 007/010 practice):
   `cohom`, `cohomanic` → q'ojom, q'ojomanik (B. gohom; modern q'ojom); `xe coheic` → k'oje'ik (plain c here, 014's
   g-shaped ꜭoheic); `catoh` → q'atoj (plain c, B. gatoh; same word as ¶18's ꜫatoh); `acab` → aq'ab' (plain c, house
   aꜫab); `ꜩe`-family → tze', utze', itze', tze'b'al, utze'b'al, tze'j; `cheenel` → che'enel; `chu ꜩiloh` → tz'iloj
   (tz' supplied on the plain ligature, as 009's Junb'atz'); `quixic` → k'ixik (014's quix k'ix); `chu cab`, `pu cab` →
   q'ab' (014's chu cab tac che).
4. **The 'take' verb**: `vcamic` (¶1) → uk'amik and `xqui cam` (¶12) → xki k'am, with Brasseur's q and 006's
   xquicam. This is the only mt that differs from a published mt for the same form (published `vcamic` is ukamik
   'his death', another word). It is still open (QUESTIONS 007/3, 008/3, 009/4, 014/1).
5. **Left by the letters, not restored** (uncertain words): `yoc` yok (B. yog, perhaps yoq' 'abuse'), `xaloc` ×4 xalok
   (B. xalog), `choc` chok (B. ch'og; read as ch- + oc = oꜫ 'cry', inferred), `calabil` kalab'il (B. galabil), `cutam`
   kutam, `coꜩic` kotzik (modern kos?), `ꜫuz` q'us, `chi` 'any more' (¶2, ¶6) kept chi (no k added).
6. **cuꜭ / ꜭux / ꜭolic / ruꜭ** → kuk' / k'u'x / k'olik / ruk'. **iviy / viy** → iwiy / wiy (i- / v- + iy 'grandchild').
7. **Other mt choices**: `cahmul` kajmul, `roxmul` roxmul, `xahouic` / `xahauic` / `xahou` xajowik / xajawik / xajow
   (by the letters; modern xajoj); `vnicahal` unik'ajal (008/009 nik'aj); `vvaha` uwaja (va not understood);
   `iaol` / `iaoc` yaol / yaoq; `iacatahinac` yakatajinaq; `chutuquel` chutukel; `quicah`, `icah` kikaj, ikaj;
   `Xmucur` Xmukur; `ramaꜫelal` ramaq'elal (004's amaꜫel amaq'el 'always'); `queꜭha` kech'a, here 'they say' (the
   glossary entry for these letters says 'their food'); `chu caꜫih` chu kaq'ij; `coh` 'puma' koj (002); `vmul` umul,
   `iac` yak, `aꜫ` aq', `ziz` sis.
8. **Grammar read with the house analyses**: `que banou`, `xe banouic`, `coh michouic`: -ou-, the ending that names
   the doers (008's xchacou, 014's review), not a passive. `xque ca ziquih`, `xque ca pixabah`: future x- + que 'them'
   (object) + ca 'we' (the glossary's `xque` has 'they shall'; this use differs). `chu ziquih` (¶9) and `chu cuiu`
   (¶6): chu without the sense 'let'. `xꜩeenic` (¶2) is the plain completive 'she laughed', not 014's mi + ix.
9. **Difficult readings, rendered with (?) in `i` and marked in `n`**: Catiha china ('let us try again', a guess from
   ca + tih), Xavi cu ꜫuz / tacchih ('made such sport', 'stirred'), xiri, chitila, vchi qui ꜭux 'their chests',
   chu catanah ꜩac 'top of the house', caꜫruxruh, muꜩumac, quimal, macama, hoꜫih (the third approach); cua;
   xe ꜭobic ('they were known', a guess from its partner xe binahic); chilo ('we shall look on you as our mother',
   after Brasseur); xoquem 'digging sticks' (Brasseur's 'charrues' rejected); ticoh 'when the sun stands' = noon;
   toloc, lahahic, ꜫaꜫchacachoh, cupuh, tum, hec; tuyuba; piz la; bacala, puquih, vvebal; quiquih / yuc; michou;
   iac 'fox', ziz 'coati' (Brasseur Sarigue, Porc-Epic).
10. **¶13 `ma cu qui chi tahin ri mixquina chutuquel`** is rendered as a question that expects 'yes' ("was the hoe
    not at work all by itself?"). Brasseur's version is loose here. A reviewer may prefer a plain statement.
11. **¶10 `e ramaꜫelal co cochoch chic`** is rendered "Yet they had always lived at home (?)" after Brasseur
    ('ils étaient constamment dans leurs maisons'); the sense is inferred.
12. Every doubtful reading in the establishment log is in its unit's note: Eia catit (U6), Catiha china (U8), xchi
    ca bano (U13), Xavi cu ꜫuz and tacchih (U10), chitila (U11), macama (U15), yuc (U45), piz la (U41), quicah
    (U29), xaqui (U32), pa cabix (U46), co cochoch (U25), xe ꜭobic (U21), ꜫatoh (U42), iviy / viy (U20, U28, U31),
    tum / tun (U35, U47), caam and chuti as abbreviations (U34, U49), coh with plain c (U49), xa hun acab (U49).
    Against Brasseur: u qamic, xu cui / chu cuiu / cuyu, huiub, iaol / iaoc, iacatahinac, pu holom, quehe viri, que
    banou, chutuquel are noted where they occur.

## (b) Proposed house renderings (not added to conventions)

| K'iche' (MS) | `l` | `i` |
|---|---|---|
| cohom, cohomanic | drum, drumming | the drum, beat the drum (mt q'ojom) |
| bixan(ic) | sing | sing |
| xahou(ic) | dance | dance, dancing |
| abix / abixic / abixom | field / field-making / field-worker | the maize field / clearing a field / a field worker |
| icah, mixquina | axe, hoe | the axe, the hoe |
| xoquem | xoquem(?) | digging sticks (?) (not Brasseur's 'ploughs') |
| Xmucur | Xmucur | Xmucur (kept as a name; the note gives 'dove') |
| ꜩe, ꜩeen, ꜩeebal | laughter, laugh, laughable | laughter, laugh, a thing to laugh at |
| cahmul, oxmul, roxmul | four-times, three-times, its-third-time | four times, three times, the third time |
| che, caam | tree, vine | the trees and the vines |
| tum, quixic | bramble(?), thorn | brambles (?) and thorns |
| coh, balam, queh, vmul, iac, vtiu, aꜫ, ziz | puma … coati | the puma, the jaguar, the deer, the rabbit, the fox (?), the coyote, the peccary, the coati (?) |
| xaloc | for-nothing(?) | for nothing (?) |

## (c) Open questions

1. The 'take' verb (`vcamic`, `xqui cam`): k'am here, with 006 and Brasseur; still to be decided for all parts.
2. Should `choc` (¶17) be given choq' (ch- + oꜫ 'cry')? It is left by the letters, since the analysis is inferred.
3. `xque` as future + 'them' (object) here, against the glossary's 'they shall'; the glosser should broaden it.
4. `queꜭha` 'they say' (¶19): the published entry gives these letters as 'their food'. It should be broadened.
5. tz' supplied in `chu ꜩiloh` (tz'iloj) on the Junb'atz' precedent, but `coꜩic` left kotzik. If the owner wants
   only the letters (011's tzotz rule), tz'iloj → tziloj.
6. `chi` 'any more' (¶2, ¶6) is kept as chi; earlier parts sometimes gave chik. Decide whether to supply the k.
7. Paragraph count: the brief expected 22 paragraphs, but the pinned text has 20, and so does cut.json.

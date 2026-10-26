# Popol Vuh pilot — Ximénez MS (Newberry Ayer MS 1515), fols. 1r–2v, K'iche' column.
# Each unit: t (manuscript spelling, our word division/punctuation/capitals),
#            m (modern ALMG letters, one entry per token of t, in order),
#            l, i, n, p.
U = []
def u(t, m, l, i, n=None, p=False):
    d = {"t": t, "m": m, "l": l, "i": i}
    if n: d["n"] = n
    if p: d["p"] = True
    U.append(d)

u("Are v xe oher ꜩih varal Quiche vbi.",
  "Are u xe' ojer tzij waral K'iche' ub'i'",
  "This-is its root of-old word, here, Quiche its-name.",
  "This is the root of the ancient word of this place called K'iche'.",
  "The book's first line, written in capitals in the manuscript. Are 'this is' points forward to what follows. v xe 'its root': v- (modern u-) is the possessive 'his, her, its', the commonest prefix in the language — you'll see it constantly. oher ꜩih 'old word' means an ancient account, a history. Quiche vbi 'Quiche its-name' is how K'iche' says 'called K'iche'': the name first, then bi 'name' with the possessive. The letter ꜩ is the colonial letter for tz.",
  p=True)

u("Varal xchicaꜯibah vi, xchicatiquiba vi oher ꜩih, vticaribal, vxenabal puch ronohel xban pa tinamit Quiche, ramac Quiche vinac.",
  "Waral xchiqatz'ib'aj wi xchiqatikib'a' wi ojer tzij utikarib'al uxe'nab'al puch ronojel xb'an pa tinamit K'iche' ramaq' K'iche' winaq",
  "Here we-shall-write it, we-shall-plant it, the old word, its-planting-place, its-rooting-place also of-all that-was-done in the citadel of-Quiche, its-nation of-Quiche people.",
  "Here we shall write, here we shall plant the ancient word, the planting and the rooting of all that was done in the citadel of K'iche', among the K'iche' people.",
  "xchicaꜯibah breaks down as xchi- 'shall' (one future prefix, distinct from the x- of completed actions), ca- 'we', ꜯibah 'write' — ꜯ is the colonial letter for tz'. The same frame then comes back with tiquiba 'plant, begin': the first couplet. The book says almost everything twice in parallel lines, and the parallel pairs are its poetry. vi points back to 'here'. The ending -ibal / -abal makes a noun of place, means or origin: vticaribal 'its planting, its beginning', vxenabal 'its rooting'. A tinamit is a fortified hilltop town; ramac is r- 'its' (the form before a vowel) + amac 'nation, people of a town'. puch 'and also' tags the second item of a pair.",
  p=True)

u("Are cut xchicacam vi vcutunizaxic, vcalahobizaxic, vꜩihoxic puch euaxibal, zaquiribal rumal Ꜯacol, Bitol, Alom, Ꜭaholom, qui bi,",
  "Are k'ut xchiqak'am wi uk'utunisaxik uq'alajob'isaxik utzijoxik puch ewaxib'al saqirib'al rumal Tz'aqol B'itol Alom K'ajolom ki b'i'",
  "This then we-shall-take it, its-being-shown, its-being-made-clear, its-being-told also of-the-hiding-place, the-dawning-place, by Builder, Shaper, Child-Bearer, Son-Begetter, their name,",
  "And so we shall take up its showing, its revealing, the telling of what lay hidden and what came to light, by the Builder and the Shaper, the Mother of children and the Father of sons, as they are named,",
  "cut 'then, and so' is the narrative connective. The three nouns in -axic / -oxic are passives turned into nouns: 'its being shown', 'its being made clear', 'its being told'. euaxibal, zaquiribal 'place of hiding, place of dawning' — darkness and dawn, a pair the book returns to again and again. Ꜯacol and Bitol are agent nouns: ꜯac 'build (as a wall is built)', bit 'shape (as a potter shapes clay)'. Alom and Ꜭaholom are 'one who bears children' and 'one who begets sons': al is a woman's child, ꜭahol a man's son, and the creator is named as mother and father at once. Ꜭ is the colonial letter for k'. qui bi 'their name': qui- is 'their'.")

u("Hunahpu Vuch, Hunahpu Vtiu, Zaqui Nimac Ꜯyꜩ, Tepeu, Ꜫucumaꜩ, Vꜭux Cho, Vꜭux Palo, Ah Raxa Laꜫ, Ah Raxa Ꜩel, chuꜭhaxic;",
  "Junajpu Wuch' Junajpu Utiw Saqi Nimaq Tz'iis Tepew Q'ukumatz Uk'u'x Cho Uk'u'x Palow Aj Raxa Laq Aj Raxa Tzel chuch'axik",
  "Hunahpu Opossum, Hunahpu Coyote, White Great Coati, Sovereign, Quetzal-Serpent, Heart of-Lake, Heart of-Sea, He-of Green Plate, He-of Green Bowl, it-is-said;",
  "Hunahpu Opossum, Hunahpu Coyote, Great White Coati, Tepeu, Q'ucumatz, Heart of the Lake, Heart of the Sea, He of the Green Plate, He of the Green Bowl, as they are called;",
  "A litany of the creators' names. Hunahpu is a calendar date, hun 'one' + Ahpu, the name of a day; vuch is the opossum, vtiu the coyote. Zaqui Nimac Ꜯyꜩ is 'white great coati' as the manuscript spaces it. Most editors divide nimac into nim ac 'great peccary' and read two names, Great White Peccary and Coati; we follow the manuscript's spacing. Tepeu 'sovereign' is a loanword from Nahuatl. Ꜫucumaꜩ is ꜫuꜫ 'quetzal (feathers)' + cumatz 'serpent' — Ꜫ is the colonial letter for q'. Vꜭux 'its heart' (ꜭux 'heart, centre, spirit'). Ah 'he of, lord of'; raxa 'green-blue'; laꜫ a plate, ꜩel a gourd bowl. chuꜭhaxic 'it is said, as they are called' closes the list; ꜭh is the colonial spelling of ch'.")

u("rach bixic, rach ꜩihoxic ry Iyom, Mamom, Xpiyacoc, Xmucane vbi, Maꜩanel, Chuquenel, camul Iyom, camul Mamom chuꜭhaxic pa Quiche ꜩih.",
  "rach b'ixik rach tzijoxik ri Iyom Mamom Xpiyakok Xmukane ub'i' Matzanel Chuqenel kamul Iyom kamul Mamom chuch'axik pa K'iche' tzij",
  "together-with being-said, together-with being-told the Midwife, Grandfather, Xpiyacoc, Xmucane his-name, Keeper, Coverer, twice Midwife, twice Grandfather it-is-said in Quiche word.",
  "declared and told together with the Midwife and the Grandfather, whose names are Xpiyacoc and Xmucane, Keeper and Coverer, twice a midwife and twice a grandfather, as they are called in K'iche' speech.",
  "rach 'together with' (r- 'its' + ach 'companion'). bixic 'being said' and ꜩihoxic 'being told' are a pair of passives. The elder pair of creators: Iyom 'midwife' (from iy 'grandchild') and Mamom 'grandfather' (from mam). Xmucane is the grandmother, Xpiyacoc the grandfather; the names are old and their meaning is unclear. camul 'twice' (ca- 'two' + mul 'time'). Maꜩanel and Chuquenel are taken as 'one who holds, keeps' and 'one who covers, shelters'; both are uncertain.")

u("Ta xqui ꜩihoh ronohel, ruꜭ xqui ban chic chi zaquil ꜭolem, zaquil ꜩih.",
  "Ta xki tzijoj ronojel ruk' xki b'an chik chi saqil k'olem saqil tzij",
  "Then they told all, with-it they did also in white being, white word.",
  "They told all of it, and what they did besides, in the clear light of being, the clear light of the word.",
  "x- marks a completed action — 'did, has done' — and you will meet it on almost every verb. xqui ꜩihoh 'they told': x- + qui- 'they' + ꜩihoh 'tell' (from ꜩih 'word'). zaquil 'whiteness, light, clarity' from zac 'white'. ꜭolem 'existence, being'.",
  p=True)

u("Vae xchicaꜯibah chupan chic vꜭhabal Dios, pa christianoil chic;",
  "Wa'e xchiqatz'ib'aj chupam chik uch'ab'al Dios pa kristyanoil chik",
  "This we-shall-write within now its-speech of-God, in Christianity now;",
  "This we shall write now under the word of God, now in Christian times;",
  "chic 'now, by now, already' — at this later time. vꜭhabal Dios 'the speech of God': ꜭhabal 'speech, language' from ꜭha 'speak', and Dios is the Spanish loanword. christianoil 'Christianity' carries the K'iche' abstract ending -il. The authors are writing under Spanish rule.")

u("xchiquelezah, rumal mahabi chic ilbal re Popo Vuh, ilbal zac petenac chaca palo, vꜩihoxic camuhibal, ilbal zac ꜭazlem chuꜭhaxic.",
  "xchiqelesaj rumal majab'i chik ilb'al re Popo Wuj ilb'al saq petenaq ch'aqa' palow utzijoxik qamujib'al ilb'al saq k'aslem chuch'axik",
  "we-shall-bring-it-out, because there-is-not now seeing-instrument of Council Book, seeing-instrument clear having-come from-across sea, its-telling of-our-shade, seeing-instrument clear life, it-is-called.",
  "we shall bring it out, because the Popol Vuh can no longer be seen — the means of seeing clearly that came from across the sea, the account of our obscurity, the means of seeing life clearly, as it is called.",
  "The manuscript writes popo vuh: pop 'mat' (the woven mat on which a council sat, hence 'council') + vuh 'paper, book'. The usual modern title Popol Vuh comes from this line. ilbal 'instrument of seeing' (il 'see' + -bal): some take this to mean the old book was consulted for divination. petenac 'having come' is a perfect participle of pe 'come'. camuhibal 'our place of shade': ca- 'our' + muh 'shade'. Whether it is the book or the ancestors that came 'from across the sea' is disputed.")

u("Ꜭo nabe vuhil, oher ꜯibam puch; xa eual vvach ilol re, bizol re.",
  "K'o nab'e wujil ojer tz'ib'am puch xa ewal uwach ilol re b'isol re",
  "There-is first book, of-old written also; only hidden its-face to-the-seer of-it, to-the-ponderer of-it.",
  "There was the original book, written long ago; but its face is hidden from the one who would look into it, the one who would ponder it.",
  "ꜭo 'there is, there exists' — the commonest way to say that something exists. vuhil 'book' with -il. ꜯibam 'written' is a perfect participle of ꜯib 'write'. vvach 'its face': vach 'face, surface, eye, fruit' is one of the busiest words in K'iche'. ilol and bizol are agent nouns, 'one who sees', 'one who ponders'.",
  p=True)

u("Nim vpeoxic, vꜩihoxic puch, ta chiꜭiz ꜩuꜫ ronohel cah vleu,",
  "Nim upeoxik utzijoxik puch ta chik'is tzuq' ronojel kaj ulew",
  "Great its-coming, its-telling also, when finished the-completion of-all sky earth,",
  "Great was its presentation and its account of how all of sky and earth was completed:",
  "vpeoxic 'its coming forth' is usually connected with pe 'come'; the form is uncertain. chiꜭiz 'finished' from ꜭiz 'finish'. ꜩuꜫ is uncertain: 'completion', 'arranging' and 'sowing' have all been proposed. cah vleu 'sky-earth' is a pair-word for 'the world'.")

u("vcah ꜯucuxic, vcah xucutaxic, retaxic, vcah cheexic, vmeh camaxic, vyuc camaxic vpa cah, vpa vleu, cah ꜯuc, cah xucut chuꜭhaxic,",
  "ukaj tz'ukuxik ukaj xukutaxik retaxik ukaj che'xik umej k'a'maxik uyuq k'a'maxik upa kaj upa ulew kaj tz'uk kaj xukut chuch'axik",
  "its-four-cornering, its-four-siding, its-measuring, its-four-staking, its-doubling-the-cord, its-stretching-the-cord in-the-belly of-sky, in-the-belly of-earth, four corners, four sides, it-is-said,",
  "its four corners and four sides laid out, its measuring, its four stakes driven, the cord doubled and the cord stretched across the womb of the sky and the womb of the earth — four corners, four sides, as it is said —",
  "The world is laid out like a maize field: the corners staked, a measuring cord folded and stretched. cah here is 'four', which sounds exactly like cah 'sky', and the text probably plays on it. ꜯuc 'corner', xucut 'side', che 'stake, tree', camaxic 'cord-stretching'. vpa 'its belly, its inside': upa cah, upa vleu 'the womb of the sky, the womb of the earth'.")

u("rumal ri Ꜯacol, Bitol, vchuch, vcahau ꜭazlem, vinaquirem, abanel, ꜭuxlanel, alay rech, ꜭuxlaay rech zaquil amaquil, zaquil al, zaquil ꜭahol, ahbiz, ahnaoh chirech ronohel ato ꜭolvi cah vleu, cho palo.",
  "rumal ri Tz'aqol B'itol uchuch ukajaw k'aslem winaqirem ab'anel k'u'xlanel alay rech k'u'xla'y rech saqil amaq'il saqil al saqil k'ajol ajb'is ajna'oj chirech ronojel ato k'ol~wi kaj ulew cho palow",
  "by the Builder, Shaper, the-mother, the-father of-life, of-creation, the-breather(?), the-cherisher, the-bearer for the-white nations, the-white children, the-white sons, the-cherisher for them, the-ponderer, the-knower about all whatever there-is sky earth, lake sea.",
  "by the Builder and Shaper, mother and father of life and of all that is made, the one who breathes life and keeps all in heart, who bears and who cherishes the bright nations, the bright children, the bright sons; who ponders and knows all there is in sky and earth, in lake and sea.",
  "vchuch 'its mother', vcahau 'its father' — the creator is again both. Agent nouns: abanel is usually understood as 'breather, giver of breath', though the word is uncertain; ꜭuxlanel and ꜭuxlaay are built on ꜭuxla 'keep in mind, cherish' (from ꜭux 'heart'); alay 'one who bears'. rech 'of it, for it'. ah- makes 'one who': ahbiz 'one who ponders', ahnaoh 'one who knows'. cho palo 'lake, sea' pairs with cah vleu 'sky, earth' to make the whole world.")

u("Are v ꜩihoxic vae.",
  "Are u tzijoxik wa'e",
  "This-is its-telling this.",
  "This is the account.",
  "A heading, written in capitals in the manuscript: ARE V ꜨIHOXIC VAE.",
  p=True)

u("Caca ꜯinin oc, caca chamam oc, caꜯinonic; caca zilanic, caca lolinic, catolona puch vpacah.",
  "K'a~ka tz'inin oq k'a~ka chamam oq katz'inonik k'a~ka silanik k'a~ka lolinik katolona puch upa~kaj",
  "Still it-was quiet then, still it-was hushed then, it-was-silent; still it-was-unmoving, still it-was-calm, and-empty also the-belly-of-sky.",
  "All was at rest, all was hushed and silent; all lay unmoving and calm, and the womb of the sky was empty.",
  "caca is ca 'still, yet' + ca-, the marker of an ongoing action: 'it is still (doing)'. oc (modern -oq) marks a dependent, not-yet-settled state: 'while it was so'. The four verbs ꜯinin, chamam, zilan, lolin are near-synonyms for stillness, heaped up on purpose. vpacah 'the belly of the sky' is written as one word by Ximénez.",
  p=True)

u("Vae cute nabe ꜩih, nabe vchan.",
  "Wa'e k'ute nab'e tzij nab'e uch'an",
  "This then first word, first its-speech.",
  "This, then, is the first word, the first speech.",
  "cute is a longer form of cut 'then, so'. nabe 'first'.",
  p=True)

u("Mahabioc hun vinac, hun chicop, ꜯiquin, car, tap, che, abah, hul, ziuan, quim, quichelah;",
  "Majab'i~oq jun winaq jun chikop tz'ikin kar tap che' ab'aj jul siwan k'im k'iche'laj",
  "Not-yet-there-was one person, one animal, bird, fish, crab, tree, stone, hollow, canyon, grass, forest;",
  "There was not yet one person, not one animal, bird, fish, crab, tree, stone, hollow, canyon, meadow or forest;",
  "mahabioc: mahabi 'there is not' + oc, the same dependent ending, here 'yet'. hun 'one'. The list runs from people down through creatures to the land itself. quichelah 'forest' shares its root with the people's own name, which is usually explained as k'i 'many' + che 'tree'.")

u("xa vtuquel cah ꜭolic.",
  "xa utukel kaj k'olik",
  "only by-itself sky existing.",
  "the sky alone was there.",
  "xa 'only, just'. vtuquel 'alone, by itself'. ꜭolic 'being there, existing' — the same root as ꜭo.")

u("Mavi calah vvach vleu; xa vtuquel remanic palo, vpa cah ronohel.",
  "Mawi q'alaj uwach ulew xa utukel remanik palow upa kaj ronojel",
  "Not clear the-face of-earth; only by-itself pooled sea, the-belly of-sky all.",
  "The face of the earth had not yet appeared; there was only the sea lying still, and the whole womb of the sky.",
  "mavi 'not'. calah 'clear, visible' — Ximénez leaves its first sound, q', unmarked here; his marking of these sounds is not consistent. remanic 'lying pooled, still (of water)'.")

u("Mahabi naquila camolobic, cacoꜩobic; hunta cazilobic, camal cabantah, cacoꜩ cabantah pa cah.",
  "Majab'i naqila kamolob'ik kakotzob'ik junta kasilob'ik kamal kab'antaj kakotz kab'antaj pa kaj",
  "There-is-not anything gathering, piling-up; not-one moving, rustling being-done, sounding being-done in sky.",
  "Nothing was gathered together, nothing heaped up; nothing moved, nothing rustled, no sound was made in the sky.",
  "naquila 'anything'. Verbs in -obic seem to describe repeated or collective motion: gathering, piling up, stirring. hunta 'not one'. cabantah 'is being done'. The exact sense of mal and coꜩ is uncertain; 'rustle' and 'make a noise' are inferred from the context, and coꜩ appears to mean 'pile up' in cacoꜩobic and 'sound' two clauses later, which shows how unsure these readings are.")

u("Xma ꜭovi naquila ꜭolic, yacalic; xa remanic ha, xa lianic palo, xa vtuquel remanic; xma ꜭovi naquilalo ꜭolic.",
  "Xma k'o~wi naqila k'olik yakalik xa remanik ja' xa lianik palow xa utukel remanik xma k'o~wi naqilalo k'olik",
  "Not there-was anything existing, standing-up; only pooled water, only smooth sea, only by-itself pooled; not there-was anything-at-all existing.",
  "Nothing existed, nothing stood upright; there was only still water, only the calm sea, lying alone; nothing at all existed.",
  "yacalic 'standing, raised up' is a positional: K'iche' has a large family of words that say how a thing is placed — standing, lying, hanging, sitting. ha 'water'. lianic 'lying smooth, flat'. naquilalo 'anything at all': -lo 'perhaps' widens naquila.")

u("Xa cachamanic, caꜯininic chi queꜫum, chi aꜫab;",
  "Xa kachamanik katz'ininik chi q'equm chi aq'ab'",
  "Only it-was-hushed, it-was-silent in darkness, in night;",
  "There was only quiet, only hush, in the dark, in the night;",
  "queꜫum 'darkness', aꜫab 'night' — a standing pair. Ximénez writes queꜫum with the tresillo in the middle and plain qu at the start, where the modern word has q' first and q second.")

u("xa vtuquel ri Ꜯacol, Bitol, Tepeu, Ꜫucumaꜩ, e Alom, e Ꜭaholom ꜭo pa ha zactetoh.",
  "xa utukel ri Tz'aqol B'itol Tepew Q'ukumatz e Alom e K'ajolom k'o pa ja' saqtetoj",
  "only by-themselves the Builder, Shaper, Sovereign, Quetzal-Serpent, they Child-Bearers, they Son-Begetters are in water glittering.",
  "only the Builder and Shaper, Tepeu and Q'ucumatz, the Mothers of children and Fathers of sons, were there in the water, glittering.",
  "e 'they' stands before a noun to make it plural: e Alom 'the Child-Bearers'. zactetoh 'shining, glittering', from zac 'white'.")

u("E ꜭovi e mucutal pa cuc, pa raxon; are vbinaam vi ri Ꜫucumaꜩ.",
  "E k'o~wi e mukutal pa q'uq' pa raxon are ub'inam wi ri Q'ukumatz",
  "They are-there they hidden in quetzal-feathers, in cotinga-feathers; this-is why-named the Quetzal-Serpent.",
  "They were there, hidden beneath quetzal feathers and cotinga feathers; that is why they are called Q'ucumatz.",
  "mucutal 'covered, hidden' (a positional). cuc is the quetzal's long green feathers, raxon the blue feathers of the cotinga. The name Ꜫucumaꜩ, 'quetzal-serpent', is explained by these feathers. vbinaam 'named' is a perfect participle; vi here means 'by that, thereby'. Ximénez often doubles a vowel; it can mark a long vowel or a glottal stop.")

u("E nimac etamanel, e nimac ahnaoh chi qui ꜭoheic.",
  "E nimaq etamanel e nimaq ajna'oj chi ki k'oje'ik",
  "They great knowers, they great understanders in their being.",
  "Great in knowing, great in understanding is their very being.",
  "nimac 'great' with the plural ending -ac. etamanel 'one who knows' from etamah 'know'. chi qui ꜭoheic 'in their being'.")

u("Quehe cut xax ꜭovi ri cah, ꜭo nai puch Vꜭux Cah; are vbi ri Cabauil chuꜭhaxic.",
  "Keje' k'ut xax k'o~wi ri kaj k'o nay puch Uk'u'x Kaj are ub'i' ri K'ab'awil chuch'axik",
  "Thus then truly there-is the sky, there-is likewise also Heart of-Sky; this its-name of-the god it-is-called.",
  "So there was the sky, and there was also the Heart of Sky; that is the name of the god, as it is called.",
  "quehe 'thus, so'. xax 'truly, indeed'. Cabauil 'god, deity' — the K'iche' word that the missionaries replaced with Spanish Dios. Vꜭux Cah 'Heart of Sky' is named in what follows.")

u("Ta xpe cut vꜩih varal; xul cuꜭ ri Tepeu, Ꜫucumaꜩ varal chi queꜫumal, chi aꜫabal; xꜭhau ruꜭ ri Tepeu, Ꜫucumaꜩ.",
  "Ta xpe k'ut utzij waral xul kuk' ri Tepew Q'ukumatz waral chi q'equmal chi aq'ab'al xch'aw ruk' ri Tepew Q'ukumatz",
  "Then came then its-word here; it-arrived with-them the Sovereign, Quetzal-Serpent here in darkness, in night; it-spoke with-him the Sovereign, Quetzal-Serpent.",
  "Then his word came here; it came to Tepeu and Q'ucumatz, here in the darkness, in the night, and spoke with Tepeu and Q'ucumatz.",
  "vꜩih 'his word' — the word of the Heart of Sky. 'With' is a noun that takes the person prefix: cuꜭ 'with them', ruꜭ 'with him'. xꜭhau 'spoke'. Tepeu and Ꜫucumaꜩ, named side by side, may be one being addressed as a pair.",
  p=True)

u("Xeꜭha cut, ta xe naohinic, ta xe bizonic; xe rico quib, xqui cuch qui ꜩih, qui naoh.",
  "Xech'a k'ut ta xe na'ojinik ta xe b'isonik xe riqo kib' xki kuch ki tzij ki na'oj",
  "They-spoke then, then they pondered, then they worried; they found themselves, they joined their word, their thought.",
  "Then they spoke, they pondered, they worried; they came to agreement, and put their words and their thinking together.",
  "Watch the two ways of saying 'they': xe- with a verb that has no object (xe naohinic 'they pondered'), xqui- with one that does (xqui cuch 'they joined (it)'). K'iche' marks the subject differently according to whether the verb takes an object; you'll see this pattern constantly. rico quib 'find one another' = agree; it takes xe-, because with the reflexive quib 'themselves' the verb is treated as having no separate object. bizonic 'ponder anxiously, grieve'.")

u("Ta xcalah, ta xqui ꜭuxlaah quib xevi zac, ta xcalah puch vinac,",
  "Ta xq'alaj ta xki k'u'xla'aj kib' xe'~wi saq ta xq'alaj puch winaq",
  "Then it-came-clear, then they took-heart-counsel themselves at-the-root-of dawn, then came-clear also person,",
  "Then it came clear; they took counsel together at the foot of the dawn, and humankind came clear;",
  "xcalah 'it became clear, it was revealed'. ꜭuxlaah 'take to heart, ponder', from ꜭux 'heart'. Ximénez wrote xevi above the line with a caret, a correction in his own hand; it is xe 'root, base' + vi: 'at the foot of the dawn'. vinac 'person, people'.")

u("ta xqui naohih vꜩuquic, vvinaquiric che, caam, vꜩucuquic puch ꜭazlem, vinaquirem chi queꜫumal, chi aꜫabal, rumal ri Vꜭux Cah, Huracan vbi.",
  "ta xki na'ojij utzuqik uwinaqirik che' k'a'm utzukukik puch k'aslem winaqirem chi q'equmal chi aq'ab'al rumal ri Uk'u'x Kaj Juraqan ub'i'",
  "then they planned its-nurture, its-coming-into-being of-trees, vines, its-nurture also of-life, of-creation in darkness, in night, by the Heart of-Sky, Huracan his-name.",
  "and they planned how trees and vines would be nourished and come into being, how life would be nourished, and all that is made, in the darkness, in the night, through the Heart of Sky, whose name is Huracan.",
  "vinaquiric 'coming into being' is built on vinac 'person' + -ir 'become'; in use it simply means 'come into being'. che, caam 'tree, vine'. vꜩuquic and vꜩucuquic are taken from the root ꜩuc 'feed, sustain' (as in ꜩucul 'provider' below); the second form is uncertain. Huracan is often read as hun 'one' + racan 'his leg', which is also uncertain. Some compare it with the Taíno word behind Spanish huracán, English 'hurricane'; any connection is unproven.")

u("Caculha Huracan nabe; vcab cut Chipi Caculha; rox chic Raxa Caculha.",
  "Kaqulja Juraqan nab'e ukab' k'ut Ch'ipi Kaqulja rox chik Raxa Kaqulja",
  "Thunderbolt Huracan first; its-second then Youngest Thunderbolt; its-third now Green Thunderbolt.",
  "First is Thunderbolt Huracan; the second is Youngest Thunderbolt; the third is Green Thunderbolt.",
  "Caculha 'lightning, thunderbolt'. chipi 'youngest, last-born'. raxa 'green-blue', which also means fresh, new, sudden. vcab 'its second', rox 'its third', from cab 'two' and ox 'three'.",
  p=True)

u("Chi e cu oxib ry Vꜭux Cah.",
  "Chi e k'u oxib' ri Uk'u'x Kaj",
  "So they then three the Heart of-Sky.",
  "These three together are the Heart of Sky.",
  "oxib 'three' (the counting form).")

u("Ta xe ul cuꜭ ri Tepeu, Ꜫucumaꜩ; ta xnaohixic zac ꜭazlem;",
  "Ta xe ul kuk' ri Tepew Q'ukumatz ta xna'ojixik saq k'aslem",
  "Then they arrived with-them the Sovereign, Quetzal-Serpent; then was-planned light life;",
  "Then they came to Tepeu and Q'ucumatz, and the light of life was planned:",
  "xnaohixic 'it was planned' — the passive of naohih 'think out, plan'. zac ꜭazlem 'white life, light of life'.")

u("hupacha ta chauaxoc, ta zaquiro puch; apachinac ꜩucul, cool.",
  "jupacha ta chawaxoq ta saqiro puch apachinaq tzuqul k'o'l",
  "how then will-be-sown, then will-dawn also; who provider, sustainer.",
  "how there would be sowing, how there would be dawn; who would provide, who would sustain.",
  "chauaxoc 'it will be sown', zaquiro 'it will dawn', from zac 'white, light'. apachinac 'who'. ꜩucul, cool 'provider, sustainer': the creators want beings who will feed them with offerings and keep their names alive.")

u("\u201cTa chuxoc!",
  "Ta chuxoq",
  "\u201cLet it-be!",
  "\u201cLet it be so!",
  "The creators speak. ta with the future ch- gives a command or wish: 'let it be'.")

u("Quix nohin tah!",
  "Kix nojin taj",
  "You fill-up let!",
  "Be filled!",
  "quix is c- (an ongoing or commanded action) + ix 'you (all)'. nohin 'fill, be full'. tah is the Classical particle of wishing and command; in modern K'iche' taj has become a negative, so do not read it that way here. Who is addressed is disputed: the empty world, the water, or the creators to one another.")

u("Are ri ha chel tah, chi hama tah, chi vinaquir va vleu, vlaquel tacu rib;",
  "Are ri ja' chel taj chi jama taj chi winaqir wa ulew ulaqel taku rib'",
  "This the water let-it-go-out, let-it-open, let-it-come-into-being this earth, let-it-set itself;",
  "Let the water withdraw and open the way, so that the earth may come into being and settle in its place;",
  "chel 'let it go out' (el 'leave'), chi hama 'let it open'. chi with a verb makes a wish: 'let it…'. va 'this'. rib 'itself'. The meaning of vlaquel tacu is uncertain; 'set itself, level itself' fits.")

u("cha ta cut, ta chauaxoc, ta zaquiroc cah vleu;",
  "cha ta k'ut ta chawaxoq ta saqiroq kaj ulew",
  "say then, then will-be-sown, then will-dawn sky earth;",
  "then let there be sowing, let dawn break over sky and earth;",
  "The opening words cha ta cut are uncertain. They are read as 'then let it be', or as 'they said'.")

u("mata cut vꜫihilabal, vcalaibal ry caꜯac, cabit, ta vinaquiroc vinac ꜯac, vinac bit,\u201d xeꜭha cut.",
  "mata k'ut uq'ijilab'al uq'alaib'al ri qatz'aq qab'it ta winaqiroq winaq tz'aq winaq b'it xech'a k'ut",
  "not-will-be then its-glory, its-honour of our-built, our-shaped, until will-come-into-being person built, person shaped,” they-said then.",
  "for there will be no glory, no honour for what we have built and shaped until there is a human being, a person built, a person shaped,” they said.",
  "vꜫihilabal 'its glory' is built on ꜫih 'day, sun'; ꜫihila is to honour someone, to keep their day. caꜯac, cabit 'our built, our shaped' — ca- 'our' on the same roots as Ꜯacol and Bitol. The creators want people who will call on them by name.")

u("Ta xvinaquir cu ri vleu cumal.",
  "Ta xwinaqir k'u ri ulew kumal",
  "Then came-into-being then the earth by-them.",
  "Then the earth came into being through them.",
  "cumal 'by them' is rumal 'by him' with the plural prefix.",
  p=True)

u("Xa qui ꜩih xꜭohe vi vvinaquiric.",
  "Xa ki tzij xk'oje wi uwinaqirik",
  "Only their word was its-coming-into-being.",
  "Their word alone brought it into being.",
  "xꜭohe 'it was, it came to be', from ꜭohe 'be, exist'.")

u("Chi vinaquir vleu: “Vleuh,” xecha; libah chi xvinaquiric.",
  "Chi winaqir ulew Ulew xecha lib'aj chi xwinaqirik",
  "So-that came-into-being earth: “Earth,” they-said; instantly then it-came-into-being.",
  "For the earth to be made they said “Earth!” and at once it was made.",
  "xecha 'they said' — the usual verb introducing speech. libah 'instantly'. Ximénez writes vleu with and without a final h; it is the same word.")

u("Quehe ri xa ꜩuꜩ, xa mayui vvinaquiric chi cupa puheic, ta xtape pa ha ri huyub;",
  "Keje' ri xa tzutz xa mayuj uwinaqirik chi kupa pujeik ta xtape pa ja' ri juyub'",
  "Like it only cloud, only mist its-coming-into-being as it unfolded, when surfaced in water the mountains;",
  "Like a cloud, like a mist was its coming into being as it took shape, when the mountains rose from the water;",
  "ꜩuꜩ 'cloud' and mayui 'mist' are a pair. Two words here are poorly understood: cupa puheic, rendered 'as it unfolded', and xtape, which has been connected with tap 'crab', so that the mountains rose like crabs from the sea. Both renderings are guesses. huyub 'mountain'.")

u("huzuc nimac huyub xuxic.",
  "jusuk nimaq juyub' xuxik",
  "instantly great mountains came-to-be.",
  "and in an instant the great mountains were there.",
  "huzuc 'suddenly, at once'. xuxic 'came to be', from ux 'become'; a plural of things is often left unmarked on the verb.")

u("Xa qui naual, xa qui puz xbanatah vi vnaohixic huyub tacah;",
  "Xa ki nawal xa ki pus xb'anataj wi una'ojixik juyub' taq'aj",
  "Only their spirit-power, only their wonder-power was-done its-planning of-mountain plain;",
  "Only through their nawal power, only through their sacred power, was the plan for mountains and plains carried out;",
  "naual and puz are words for supernatural power. naual is shared with Nahuatl nahualli (Spanish nagual), a person's spirit-double; puz is often connected with sacrifice, but its exact sense is uncertain. huyub tacah 'mountain-plain' is another pair-word: the landscape.")

u("huzuc rach vinaquiric vquizizil, vpachahil vvach.",
  "jusuk rach winaqirik uk'isisil upachajil uwach",
  "instantly together-with its-coming-into-being its-cypress-grove, its-pine-grove its-face.",
  "and with them at once came the cypress and pine woods that cover their face.",
  "quiziz 'cypress' with -il for a grove or stand of them. The woods are the mountains' face (vvach).")

u("Quehe cut xquicot vi ri Ꜫucumaꜩ:",
  "Keje' k'ut xkikot wi ri Q'ukumatz",
  "Thus then rejoiced the Quetzal-Serpent:",
  "And so Q'ucumatz rejoiced:",
  "xquicot 'rejoiced', from quicot 'be glad'.",
  p=True)

u("“Vꜩ mixatulic, at Vꜭux Cah, at Huracan, at pu Chipi Caculha, Raxa Caculha!”",
  "Utz mixatulik at Uk'u'x Kaj at Juraqan at pu Ch'ipi Kaqulja Raxa Kaqulja",
  "“Good you-have-come, you Heart of-Sky, you Huracan, you also Youngest Thunderbolt, Green Thunderbolt!”",
  "“Welcome, Heart of Sky, Huracan, and you too, Youngest Thunderbolt, Green Thunderbolt!”",
  "vꜩ 'good'. mixatulic: mi- 'just now' + x- + at 'you' + ul 'arrive' + -ic — 'you have just come'. at 'you (one person)'. pu is a short form of puch 'also'.")

u("“Xchuꜩinic caꜯac, cabit,” xeꜭha cut.",
  "Xchutzinik qatz'aq qab'it xech'a k'ut",
  "“Will-be-completed our-built, our-shaped,” they-said then.",
  "“What we have built and shaped will be complete,” they said.",
  "xchuꜩinic 'it will be finished': xch- future + utzin 'complete' (from utz 'good') + -ic.")

u("Nabe cut xvinaquir vleuh, huyub, tacah;",
  "Nab'e k'ut xwinaqir ulew juyub' taq'aj",
  "First then came-into-being earth, mountain, plain;",
  "First the earth was made, the mountains and the plains;",
  None,
  p=True)

u("xchobochox vbe ha, xbiniheic colehe racan xol tac huyub;",
  "xchob'ochox ub'e ja' xb'inijeik kolej rakan xol taq juyub'",
  "was-divided its-road of-water, went-walking winding its-leg among plural mountain;",
  "the paths of the water were divided, and the streams went winding among the mountains;",
  "vbe 'its road'. racan 'its leg': the streams are the water's legs, and they walk (bin). tac makes a plural: xol tac huyub 'among the mountains'. colehe 'winding' is inferred from the context.")

u("xa chobol chic xeꜭohe vi ha, ta xcutuniheic nimac huyub.",
  "xa chob'ol chik xek'oje wi ja' ta xk'utunijeik nimaq juyub'",
  "only divided now were the waters, when were-revealed great mountains.",
  "the waters lay divided once the great mountains had shown themselves.",
  "chobol 'divided, separated'. xcutuniheic 'were revealed', the same root as vcutunizaxic 'its being shown' at the start of the book.")

u("Quehe cut vvinaquiric vleu ri, ta xvinaquiric cumal ri Vꜭux Cah, Vꜭux Vleu, que vchaxic,",
  "Keje' k'ut uwinaqirik ulew ri ta xwinaqirik kumal ri Uk'u'x Kaj Uk'u'x Ulew ke uchaxik",
  "Thus then its-coming-into-being of-earth this, when it-came-into-being by-them the Heart of-Sky, Heart of-Earth, as it-is-called,",
  "This, then, was how the earth was made, when it was made by Heart of Sky and Heart of Earth, as they are called,",
  "Vꜭux Vleu 'Heart of Earth' appears here for the first time, paired with Heart of Sky.",
  p=True)

u("ry cute nabe xqui nohih;",
  "ri k'ute nab'e xki nojij",
  "who then first they conceived-it;",
  "who were the first to conceive it.",
  "nohih 'think of, conceive'.")

u("xcolo vi ri cah, xcolo nai puch vleuh chupan ha.",
  "xkolo wi ri kaj xkolo nay puch ulew chupam ja'",
  "was-freed the sky, was-freed likewise also earth within water.",
  "The sky was freed, and the earth too was freed, there inside the water.",
  "colo 'be freed, loosed'. chupan 'inside, within'.")

u("Quehe cut vnohixic ri, ta xqui nohih, ta xqui bizoh ruꜩinic vbanatahic cumal.",
  "Keje' k'ut unojixik ri ta xki nojij ta xki b'isoj rutzinik ub'anatajik kumal",
  "Thus then its-being-conceived this, when they conceived-it, when they pondered its-completion its-being-done by-them.",
  "Such was its conception, as they thought it out and pondered how their work should be brought to completion.",
  "ruꜩinic 'its completion' (r- 'its' + utzin 'finish'). vbanatahic 'its being done'. The first section ends here; next come the animals.")

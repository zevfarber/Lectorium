# The Secret History of the Mongols — conventions (Run 3)

Distilled from the project's `middle-mongol-secret-history-conventions.md` (2026-07-29) and the published
pilot `secret-history-01-06.json` (§§1–6), the model of shape and register.

## What the text is (say it plainly to the reader)
The Mongolian original, in Mongolian script, is lost. What survives is a Ming teaching edition: the Mongolian
written phonetically in Chinese characters, a Chinese gloss over every word, and an abridged Chinese
translation. So (1) the characters are Chinese and mean nothing in Chinese; (2) the Mongol line is a
reconstruction — editors differ over vowels; (3) the glosses are the Ming glossators' own, carried in
square brackets.

## Source and the sole-source rule
- Text: Shiratori Kurakichi 白鳥庫吉, 音訳蒙文元朝秘史 (Tokyo 1943), after the Ye Dehui print of 1905/1908, from
  the Japanese Wikisource transcription — archived 2026-10-12 (all 36 pages, `source/raw/`), extracted to
  `source/secret-history-shiratori.json` (282 sections, 29,353 words; §§1–6 identical, word for word, to the
  pilot's verified archive). PD basis signed off by the owner 2026-07-29 (Shiratori d. 1942).
- While drafting: Shiratori's text and the Ming interlinear glosses only. Permitted meaning check: Naka
  Michiyo, 『成吉思汗実録』 (1907) — meaning only, never wording. Modern translations (de Rachewiltz, Cleaves,
  Onon, Atwood) are never opened.

## Data model (the build does the mechanics)
- One glyph per word: the Han transcription (the edition's FVS "small character" markup U+180B/U+180C is
  stripped at build — never by hand; U+FE00 stays as in the pilot). `glyph.tr` = the romanized word as
  printed (with its punctuation); `reading` = "<Han> <romanized word without punctuation>".
- `t` = the unit's romanized words joined by single spaces, exactly as printed. `ln` = the § number (§ chip);
  `p: true` on the first unit of every §.
- The drafter supplies each word's `morph`: one entry per morpheme the reader sees, `{"lemma": dictionary form
  (töre-, a-, deġü), "gloss": "… [Ming gloss]"}` — e.g. Qaγan-(n)u → qaγan + -(n)u.
- Glossary: shared `secret-history-glossary.json`, keyed by the reader's tokens of `t` (Qaγan-(n)u → `qaγan`
  and `nu`), value `"<dictionary form> — <meaning> (<grammar>) [<Ming gloss>]"`. 100 % coverage, no unused keys.

## Segmentation and translation
- Sense-unit = Shiratori's own punctuation where he has it (`.` closes a sentence), otherwise the natural
  clause. Genealogies stay whole. Long converb chains are broken into readable units and the note says so.
- `l`: possessor before its noun, converbs as "-ing", -tü as "wife-having", no copula supplied; stop before
  word-salad. `i`: plain, a little formal — a chronicle, never "verily".
- Grammar is the payload and the Ming glossators are the co-teacher (their 行 = dative-locative, 着 = converb,
  有的 = possessive). Recurring patterns flagged first, nudged after: converb chain; possessive -tü/-tu/-tai/-tei;
  reflexive-possessive -beġen/-deġen/-jüġen; vowel harmony in case endings; ese vs ülü.
- Notes admit uncertainty (börte čino is "blue-grey wolf" and a name; 訥 writes -nu and -nü).
- Proper names: Shiratori's form in `l`, a plain English spelling in `i` (Činggis → Chinggis, Temüžin → Temüjin).

## Characters
Three CJK Extension B characters occur in §§1–6 and more later; never substitute them — a box is honest.

## Pronunciation and audio
`langCode: null`. A Middle Mongol voice has not been chosen (it also waits for the Stele of Yisüngge); parts
publish without audio until the owner chooses. Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12)
- Parts: whole sections in order, grouped to about 300–520 words; a section longer than that is its own part
  (66 parts; see plan.md). New part ids use three-digit § numbers (secret-history-007-010).
- `p: true` on the first unit of every § (the conventions' rule; the pilot omitted it once, at §3).

## House renderings added by 109-114
- qād → "sovereigns"; qutuγ eġede → "door-frame of his fortune"; tedüi after a genitive → "no bigger than".
- Names in `i`: Barqujin, Yeke-Chiledü, Chilger-Bökö, Küchü, Buqura, Lady Üjin, Mother Etügen; Qaldun-Burqan (printed reversed once) → "Burqan Qaldun".

## House renderings added by 146-148
- Names in `i`: Qada'an, Qudu'udar, Qotun-Orchang, Tödöge, Jebe, Taichi'ud; title Qaγan in `l`, Qahan in `i`.

## House renderings added by 165-168
- Names in `i`: Jüchi, Cha'ur-Beki, Qojin-Beki, Högelün, Qarta'ad, Tödögen (Saiqan-Tödögen), Tayang, Jeje'er, Ber-Ke'eled, Sügegetei, Nilqa-Senggum, Father Münlig.
- maqa (Ming 莫) "perhaps (not)"; barija (拿咱) "let us seize"; the Ming alternates 俺/咱 for the inclusive bida- forms.

## House renderings added by 169
- Names in `i`: Alaqchid, Kishiliq, Narin-Kegen, Atan; horses Merkidai-Chaqa'an and Aman-Chaqa'an-Keger. deleme: Ming 泛濫 "overflowing, rash".

## House renderings added by 172-176
- Names in `i`: Boroqul, Bo'orchu, Qada'an-Daldurqan, Achiq-Shirun, Jürchedei, Quildar, Ögödei; peoples Kereid, Ongirad, Uruqud, Mongqud, Shilügeljid; Lake Büyür.
- Names in `i` (§§191–193): Qanghar-Qan, Sa'ari-Keger, Cherbi, Arqai-Qasar, Kerülen, Ornu'u.

## House renderings added by 178-181
- Names in `i`: Quchar, Altan, Oqda, Sübegei, Kököchü-Kirsa'an, Jegei-Qungtaqar, Charaqai-Linggu, Arqai-Qasar, Bilge-Beki; "Father Qan" for Qān ečige; qād "sovereigns".

## House renderings added by 182-185
- Names in `i`: Qali'udar, Chaqurqan, Qadaq-Ba'atur (printed Qdaγ-Baγ̇atur, read as a slip), Soqos-Chaqan, Arqal-Kögi, Je'üriyedei, Alaqush-Digit-Quri, Jekü, Jesünge, Jirgin, Jeje'er (Jeje'er Ündür in `i`); Kerülen. Lemmas buči-, eri- follow the glossary.

## House renderings added by 186-188
- Names in `i`: Taqai-Ba'atur, Jaqa Gambu, Ibaqa-Beki, Sorqaqtani-Beki, Tolui, Qori-Sübechi, Didig-Saqal, Negün-Usun, Chul, Abji'a-Ködegeri, Olon-Dongqaid, Tümen-Tübegen, Wang Qan, Ongjid Kereid, Jirgin, Naiman, Kököchü, Senggum. γ̇ → ' in names. beki = "a title of rank" (borne by men too).
- tusa-jin in-ü tula → "in return for the service of …"; žarliγ bolurun → "issued a decree:"; nögöġe kilgün bol → "Be a second shaft!"; aγtači → "groom".

## House renderings added by 189-190
- Names in `i`: Kürbesü, Kökse'ü-Sabraq, Inancha-Bilge, Torbi-Tashi, Juqunan, Ödchigin Noyan, Belgütei Noyan, Temegen-Keger, Tülkin-Che'üd, Önggüd. torluγ / torulmiši: no Ming gloss, left untranslated. bütügei (Ming 有者) "let them be". Quotes: double outer, single inner.

## House renderings added by 195
- Names in `i`: Sübegetei (not Sübegei, a different man), Uruqud, Angqu'a, Jamuqa, Tayang. Quotes: opening marks Shiratori omits are supplied in `i` and said so in the note.

## House renderings added by 196-197
- Names in `i`: Naya'a, Lady Qulan, Qo'as Merkid, Sa'ari-Keger, Toqto'a, Qaradal-Huja'ur, Chila'un, Dair-Usun, Ba'aridai (a people). bolγan stays "making" (Ming 審 unrendered); converb -žü is written so after back-vowel stems (jadažü).

## House renderings added by 198-199
- Names in `i`: Chimbai, Sorqan-Shira, Toqto'a-Beki, Küchülüg (Qan), Sübegetei, Gur-Qan, Qara-Kitad, Uduid, Erdis, Buqdurma, Mount Arai; "three Merkid"; alus "beyond(?)"; qulan (animal) "wild ass".

## House renderings added by 200
- Names in `i`: Jamuqa, Chinggis, Qahan, Wang Qan (Father Wang Qan), Mount Tanglu, Qalaqaljid-Eled. Lemmas bolulča-, duradγa-, adalidγa-, qān follow the glossary. Opening quote mark at Ken-ü idemü" supplied in `i` and said so in the note.

## House renderings added by 201
- Names in `i`: Sojidar-Mala, Taichar, Jeren, Dalan-Baljut, Qorqonaq-Jubur, Chinggis Qahan. anda → "sworn brother" (except where the word itself is the point); Qān → "Qan", Qaγan → "Qahan".

## House renderings added by 204-207
- Names in `i`: Bo'orchu, Muqali, Qorchi, Münlig, Ba'arin, Erdis, Qara'un-Jidun, Kügün-Go'a, Taqai, Ashiq, Guowang. -tuγai/-tügei = "optative (third person)"; eje (Ming 商量) = counsel/consult; köiten here "cold" (broadened).

## House renderings added by 208-210
- Names in `i`: Qalaqaljid-Eled (printed Qara-Qalžid-Eled), Qori-Shilemün and the Thousand Guards, Jaqa Gambu, Ibaqa-Beki, Ashiq-Temür, Alchiq, Bedüün, Qubilai, Jelme, Jebe, Sübegetei, Dodai, Doqolqu, Qunan (of the Genigedei; his people the Genigesid), Kökösös, Degei, Usun-Ebügen, Jüchi, Lake Baljuna, the Qalqa river.
- inže → "dowry attendant(s)"; soγ̇or → "clash"; noγai → "dogs"; erkid + noun → "leading …"; aman alda- → "gave his word"; sojurγažu žarliγ bolba → "showing favour, issued a decree"; uchuma (Ming 箭名) left as an arrow-name; ögbe after a converb tentatively "did for (me)". Curly quotes; opening marks Shiratori omits are supplied in `i` only and said in the note (U59, U71).

## House renderings added by 214-217
- Names in `i`: Shigi-Qutuqu, Boroqul, Küchü, Kököchü, Qargil-Shira (printed Qargil-/Γargil-), Tolui, Jetei, Jelme, Altani, Ögödei, Usun-Ebügen, Qunan, Kökösös, Degei, Quildar, Qalaqaljid-Eled, Kereid, Ba'arin. nögöġe kilγun "second shaft"; anda "sworn brother"; man- forms lemma ba (not bida); örežü "risking his own life".

## House renderings added by 218-223
- Names in `i`: Narin-To'oril (To'oril), Chagan-Go'a, Nekus (clan), Tarqutai-Kiriltuq, Sorqan-Shira, Chila'un, Chimbai, Qada'an (daughter), Badai, Kishiliq, Tödöge, Cheren, Selenge, Old Shirgötü, Alaq, Naya'a, Naya'a-Biljiur, Qutuqul-Nu'u, Guowang, Bo'orchu, Muqali, Jebe, Sübegetei, Degei, Küchügur, Mulqalqu, Jadaran (clan).
- ede / tümen follow the Ming ("these"; "ten thousand"); darqala- "be free"; qorčilaγulžu ötögleġülžü "having them bear the bow and offer the cup"; tus qān(i)-jan "one's own true lord"; medeġülbe "had (him) manage / put in charge"; lemmas naita-, darqan, dutaγ̇u, nököče- follow the glossary.

## House renderings added by 224-226
- Names in `i`: Jesün-Te'e, Bügidei, Qorqudaq, Lablaqa, Arqai-Qasar, Ögere, Buqa, Iluqai, Alchidai, Dodai, Doqolqu, Chanai, Aqutai, Yeke-Ne'ürin. čerbi → "cherbi" (meaning not known; not "chamberlain"); noyan → "officer"; aqalažu from aqa + -la- + -žu; ögtekün tentatively ög- + -te- + -kün.

## House renderings added by 227-229
- Names in `i`: Buqa, Alchidai, Dodai, Doqolqu, Eljigedei (Elžigedei), Chinggis Qahan (Qaγan in `l`). Dodai and Doqolqu are each "the cherbi" (čerbi → "cherbi", meaning unknown; not "chamberlain", as in 224-226).
- josutan böġesü after mököriġülkün / nišiγdaqun (Ming 理有的每) → "…, and rightly so" (not "in the right"); kešigtü → "man of the guard" / "guardsman" (kešig + -tü); kešigten → "guardsmen"; turγaγ (Ming 散班) → "day guard"; kebteġül → "night guard"; qorčin → "quiver-bearers"; baγ̇určin → "cooks"; aγta → "gelding"; kötöčin → "companion"; ger-ün in `i` "tent" (l "house").
- Lemmas: berkešije- (not berkeši + -jen), aqa + -la- (aqalažu, aqalaba), bügüdge-, taγ̇ul- (also printed daγ̇ul-), baγ̇u-, eki + -d, mürü + -s, ötögü (printed ötökü-), hoγara- (printed hoγ̇ara-/oγ̇ara-), niši-, mököri- + -ġül-; plain γ is written γ in lemmas the glossary spells so (doloγ̇an, qariγ̇u, sačaγ̇u, saγ̇urin, saγ̇uri, baγ̇urči).
- Reflexive (i) before -jen/-jan stays a separate morph: mör-tür(i)-jen → mör + -tür + -(i)jen. Opening quote mark that Shiratori omits (U20) is supplied in `i` only and said in the note.

## House renderings added by 230-236
- Names in `i`: Jesün-Te'e, Bügidei (printed Bugidai/Bukidai; Han as §225), Aqutai, Alchidai, Ögöle (the cherbi), Buqa, Dodai, Doqolqu, Chanai, Shigi-Qutuqu, Qubilai the noyan, Arslan Qan, Sübegetei-Ba'atur, Toqto'a, Qutu, Chila'un, the Chu; peoples Qarluq, Merkid.
- jekes turγaγ̇ud "great day guards"; ötöküs kebteġül "elder night guard"; nutuγ̇učin "camp-manager(s)"; eġüdečin "door-keepers"; qoničin/aduγ̇učin/temeġečin/hükečin herders; temür terege + -tü "of the iron cart"; tüsürge (Ming 酒局) "banquet", barin atuγai "stay to hold"; žebe (器械) "weapons" (common noun); hodun "star"; oγžad- + -γa- "to startle"; gerije + -s "keepsakes"; nendü qutuγ "good fortune and blessing"; X-i NAME keġegdün/keġedkün "call them NAME"; Kebteġül-eče before a verb of sharing "from the night guard"; uqažu atuγai "be mindful of". `l` mirrors Shiratori's quote marks (straight); `i` supplies omitted openings.

## House renderings added by 237-241
- Names in `i`: Idu'ut, Adkiraq, Darbai, Al-Altun, Sariq, Shiqshid, Quduqa Beki, Inalchi, Törelchi, Qoluiqan, Alaqa Beki, Chechegen, Boroqul, Daiduqul-Soqos, Botoqui-Tarqun, Dorbai-Doqshin of the Dörbetei, Qorchi, Bo'orchu, Muqali, Tögeles; peoples Oirat, Buriyat, Barqun, Ursut, Qabqanas, Qangqas, Tubas, Kirghiz, Shibir, Kesdiin, Baid, Tuqas, Tenlek, Tas, Bajigid, Önggüd, Tumad; the Forest People as the collective.

## House renderings added by 242-244
- Names in `i`: Jüchi, Ödchigin, Cha'adai, Ögödei, Tolui, Qasar, Alchidai, Belgütei, Da'aritai, Kereid, Jungsai, Qorqasun, Qunan, Müngkegür, Kete, Qarachar, Müngke, Iduqudai, Kökösös, Ilüge, Degei, Chedei, Bala, Jebke, Cha'urqai, Father Münlig, Qongqotadai, Qongqotan, Teb-Tenggeri (rule-built), Qachi'un, Barqujin, Jalairtai; Müṅke teṅgeri → "Eternal Heaven". jesün → "nine" though the Ming writes 九十. Participle + büleġe = past habitual ("used to").

## House renderings added by 245
- Names in `i`: Teb-Tenggeri, Soqor (man's name, not "blind"), Ödčigin, Temüge, Mother Etügen the Great Earth (dair "great" here); bökös → "wrestlers"; kölge- "to yoke"; temeče- + -ldü- + -d- + -kün; qanču + -d + -(i)jan.

## House renderings added by 246-248
- Names in `i`: Chabchiyal, Küiküneg (Shiratori's spelling), Juin, Fox Pass (Hünegen dabā), Zhongdu (Han 中都), Mozhou and Fuzhou; Teb-Tenggeri. lemmas else-, ič-, qoton + -d, daγa-, balaγad, bol- + -γa- follow the glossary.

## House renderings added by 249-252
- Names in `i`: Jubqan, Hexiwu, Shira-Keger, Önggür, Shigi-Qutuqu, Arqai-Qasar, Iluqu-Burqan, Hula'an-Degelen, Ile, Qada, Höbögetür, Chükü; "Liushou" kept as the Han title; Nangiṅ → "Nanjing"; Altan Qaγan → "Altan Qahan"; qa (Ming 係官) "state property" (tentative).

## House renderings added by 254
- Names in `i`: Uquna, Jesüi, Kökösös, Jüchi, Cha'adai, Sartaul (the Sartaγul); Merkidai Čulγul left as printed (people name uncertain). Quotes: openings Shiratori omits supplied in `i` only and said in the notes; the mother's thoughts in Kökösös's speech in single quotes in `i`.

## House renderings added by 255-256
- Names in `i`: Asha Gambu (after Jaqa Gambu), Mother Etügen; Altan = the Jin ruler (also where Ming 金 follows); Qān → Qan, Qaγan → Qahan. že-jin here "assent" (Ming 應許).

## House renderings added by 257-259
- Names in `i`: Sartaul (people), Arai, Jebe, Sübegetei, Toquchar, Qulan, Ödchigin, Sultan, Melig Qan, Udurar (Udirar/Udurar/Udarar one town). baγudqun (Ming 下營) "camp before"; baγ̇ulba "demoted" (Ming 削, tentative). Opening quote marks Shiratori omits are supplied in `i` only and said in the notes.

## House renderings added by 260-264
- Names in `i`: Jüchi, Cha'adai, Ögödei, Shigi-Qutuqu, Qongqai, Qongtaqar, Sormaqan, Qaliba, Ürüngechi, Dorbai-Doqshin, Jalawachi, Masqud, Bala, Jalaldin, Melig Qan, Zhongdu (Han 中都; the Ming here writes 大都), Erdis, Shin River; peoples Sartaul, Baqtad, Kibcha'ud, Bajigid, Majarad, Urijang (ž→j, γ→q/h, ṅ→ng as before).
- qorči/qorčin "quiver-bearer(s)"; daruγa "governor(s)"; serkes "wethers" (tentative); qarin (Ming 邦) "nation" (tentative); doroida- + -γ̇ul- (printed -γ̇ui-, read as slip, Han 兀勒); closing quote for the §263 decree supplied in `i` after talbižu.

# Review pass 1 — secret-history-140-143

Checked: 77 units, 431 words. `t` identical to packet words (script-verified), every word covered once, `ln` and `p` correct. Edited units.json in place by script; `t` untouched. Unit numbers are 0-based positions in `sentences`; word numbers are packet indices.

## Changes
| Unit | Field | Sev | Wrong | Done |
|---|---|---|---|---|
| 5 | i, n | moderate | "he had Belgütei and Büri-Bökö wrestle" invents an agent; the note itself says the maker is not named | passive: "were set to wrestle"; note says why |
| 7 | i | moderate | "got a shoulder under him" is an invention; mürüdežü is "taking on the shoulder" | "took him on his shoulder (?)", "pin" changed to "press" to match darun |
| 11 | i | moderate | "at the throat", "hauling back" not in Ming (交 扼着 扯着) | "crossing his two collars, throttling him and pulling" |
| 17 | i, n, morph w96 | moderate | note quoted Ming 折斷 but packet has 折折 (note and morph gloss); i dropped "pulled" | Ming quoted correctly; i = snapped / pulled and dragged / went off |
| 23 | l, i, n | moderate | l "lad" for köġün (Ming 兒子, "son" everywhere else); bolun (上頭) ignored, i had "(he being)"; the note's "here Büri-Bökö's to Chinggis's" is not derivable from the Ming | l son-from, "on-account"; i "Adjoining … and on that account"; claim removed; morph w125 "lad" removed |
| 27 | i | moderate | i dropped the first word Qadagin although l and note keep it | included |
| 41 | i | moderate | šiṅaγ̇a-jin (洲的) omitted; "to" for locative -da | "at the point of the sandbank where …" |
| 48 | i | moderate | ileġesü (conditional 呵) rendered as a finite verb; sentence runs on | "When … sent this word on to Wang Qan," |
| 60 | morph w326 | moderate | -tan labelled "front-vowel form"; -tan is the back-vowel variant on a front stem | label corrected |
| 60 | n | minor | "speaks from Chinggis's side" contradicts the inclusive 咱 (Sengüm is Wang Qan's) | rewritten |
| 74 | i | moderate | one clause rendered twice, with "broke" invented | "the storm came upon them." |
| 36 | n, i, w189 | minor | note said "Three leaders and then Aγ̇uču" (two); "their Taichi'ud" muddy; "Aghuchu" breaks house pattern (Chila'un, Bo'orchu, Qo'aqchin) | "Two"; "A'uchu-Ba'atur and company, the Taichi'ud"; also w365 (unit 65 i is untouched except gloss) |
| 65 | morph w365 | minor | "Aghuchu" | "A'uchu" |
| 38, 42, 43 | i | minor | qā rendered "qan"/"Gur-Qan"; house renders qā as Qahan (125-130) | Qahan / Gur-Qahan |
| 55 | i, w291 | minor | "Jaqa-Gambu" is a hyphen not in the one word Žaqaγambu | "Jaqagambu" |
| 45, 60 | morph w239, w331 | minor | -dür labelled "back-vowel form" | front-vowel |
| 75 | morph w422 | minor | -tur labelled "front-vowel form after s" | back-vowel |
| 2 | i | minor | "had seized … thrown": converbs carry no pluperfect | simple past |
| 46 | n | minor | Ming quoted as 送到着; packet has 到着 | fixed |
| 53 | i | minor | huruγ̇u "downstream" dropped | added |
| 58, 59 | i | minor | verb tabiγ̇ulba dropped, "one more/another" invented | "they had one post of scouts set" |
| 61, 62 | i | minor | finite "came" of unit 62 pulled into 61 | 61 ends "rushing and coming,"; 62 "came crying … and bringing the word" |
| 66 | n | minor | "same four peoples" miscounted (three peoples in the unit) | rewritten |
| 67 | i, n | minor | "have come" for jabužuγ̇ui ("go"); l says "are-gone" | "have marched" |
| 68 | i | minor | "until evening came": no "until" | "evening coming on," |
| 69 | i | minor | "joined the main camp" for γol-dur neilen ("at the main camp, joining") | "joined up at the main camp" |
| 70 | l, n | minor | l "at-Köiten" but Köiten has no case ending | l bare; note says "at" is the sense |
| 71 | i | minor | iquriγaldun (binding together) dropped | "linking up and putting themselves in order" |
| 72 | n | moderate | "worked with a stone" is outside knowledge, not from the Ming | removed |
| 72 | morph w408 | trivial | stem mede- vs printed modekün | gloss says printed with o |
| 75 | l, i | trivial | "ravines" vs gullies; "go forward" | gullies; "go on" |
| 68 | morph w380 | trivial | gloss text "頭哨每" but word's Ming is 頭哨 | fixed |

Counts: major 0, moderate 11, minor 21, trivial 3 (rows are grouped; some rows cover several edits).

## Refused
- U1 n "Earlier it meant 'against the Jurkin'": refers to the glossary entry from a previous part; true there.
- U6 i "gave way": uncertain reading, note flags it; left.
- U12 i "left him": note states the choice and uncertainty.
- U14 i "could not have beaten me": acceptable for ülü ilaγdaqu büleġe.
- U24 i opening "So": discourse connective only.
- U38 -je as hortative against Ming 着 (擡着): flagged in the note; left (doubt below).
- w390 gloss "elsewhere 澗": cites the known-form; bracket [大營] matches the word's Ming.
- U21 "After him": pronoun referent unclear in the Ming; note says so.
- Qutuqtu-Müngler spelling: ṅ → ng follows house (Münggür).

## Remaining doubts
- ergüje (U38): Ming 着 says converb; hortative reading is a guess.
- U6 who falls; U23 whole sentence; U15 sense; U63 "take word".
- ile- "went" (Ming 去了) vs glossary "send" (敎去了).
- γol as "main camp" overrides known-forms "stream".

# Review pass 2 — secret-history-140-143

Re-checked: all 77 units (`l` ↔ `i`, notes, every morph label and Ming bracket against the packet, `l` names against `t`), `ln`/`p` (first unit of each § carries `p`), and all 142 gloss entries plus the 16 `__broaden__` entries. Script checks: every token of every `t` (288 distinct) has an entry in gloss.json or the shared glossary, no unused keys, every gloss bracket equals the novel-forms bracket, every `__broaden__` value starts with the old entry whole + " · " (all 16 do), and each broadened reading is used in this part (büri u22, čaγaγ̇an u32, ken u41, dörben u28, žažiradai u38, maṅlai u54-55, bolun u15/23/73, γarču u7, odču u10, ilebe u12/16, γol-dur u69, jar/γari u2, jer u2, jan u15, nača u15). `t` untouched (script-verified); edits made in place by script.

## Units
| Unit | Field | Sev | Wrong | Done |
|---|---|---|---|---|
| 65 | i | moderate | "Aghuchu-Ba'atur": pass 1 fixed the morph gloss (w365) but left the English in `i`, breaking house A'uchu (unit 36) | "A'uchu-Ba'atur" |
| 18 | i, about | minor | "Qabul Qan" — house renders Qabul as Qahan (136-139 "Qabul Qahan", printed Qān there too) | "Qabul Qahan" in `i` and in `about` |
| 18 | l | minor | "Qabul Qan's": `l` keeps Shiratori's form (printed Qān) | "Qabul Qān's" |
| 18 | n | trivial | note silent on why the English is Qahan | one clause added |
| 32, 45 | i, n, morph w172, w234 | minor | "Gorolas": house has "Qorolas" (115-120 "from the Qorolas") | Qorolas in `i`, note (u45) and both morph glosses |
| 53 | i, n, morph w277 | minor | "Kelüren" in `i`: house is "Kerülen" (93-99, 136-139) | `i` Kerülen; note says Kelüren is the printed form of the Kerülen; morph gloss likewise |
| 1 | l | minor | "among-the-Jurkin": `l` keeps Shiratori's name form (Žürkin; 136-139 `l` has Žürukin-by) | "among-the-Žürkin" |
| 0, 5 | n, morph w7, w32 | minor | note says abal- is known "from nowhere else" — the shared glossary already has abaldurun (abal-, 'when grappling') | note and both stem glosses point to abaldurun, still "uncertain" |
| 9 | n, morph w51 | minor | -lüġe called unanalysable although the glossary has kürküi-lüġe / ireküi-lüġe ('as soon as') | cross-reference added; force still called uncertain |
| 65 | n | trivial | stray "(Tatar)" after "not the Tatar of the text" | removed |

Counts, units: major 0, moderate 1, minor 8, trivial 2 (rows group several edits).

## Gloss
| Key | Field | Sev | Wrong | Done |
|---|---|---|---|---|
| bökö | entry | minor | Ming is 勇士 at the end of §140 (word 134) but the entry only gives 力士 | said so in the entry; bracket unchanged (= novel-forms) |
| žada | entry | minor | Ming is 風雨 at words 412 and 417 (the storm), 能致風雨的事 only at 407 | said so |
| maṅlan | entry | minor | labelled "plural" on the strength of one 頭哨每; the other three uses (u65, 67, 68) are 頭哨 alone and the English reads "vanguard" | label softened ("plural or collective; uncertain") |
| ireġülüġed | entry | trivial | Ming (敎)來了 at word 266 not mentioned | added |
| belgütei-je | entry | minor | entry silent on the glossary's irekü-je with accusative -je, same shape | cross-reference and reason for the passive-agent reading added |
| abalduγ̇uluja, abalduγ̇ulba | entry | minor | "stem inferred" though abal- is in the glossary (abaldurun) | stem tied to abaldurun |
| ilaγdaqu | entry | trivial | no link to the glossary's ilaγ̇a- (ilaγču) | "compare ilaγ̇a-" |
| unaγ̇ažu | entry | minor | causative -γ̇a- asserted, but the Ming 倒着 is plain 'falling' | said the Ming does not mark it; read from 'threw down' |
| üžekü-lüġe | entry | minor | as unit 9 | cross-reference to kürküi-lüġe |
| uqa | entry | trivial | labelled plain noun | "noun, or the bare verb stem; uncertain" |
| γorolas-un | entry | minor | "the Gorolas" (house Qorolas) | fixed |
| __broaden__ nača | entry | trivial | new reading omitted that the Ming writes 行 (not 處) | added; old entry still whole |

Counts, gloss: major 0, moderate 0, minor 9, trivial 3. Every other entry: dictionary form, meaning, label and bracket checked against the packet and found acceptable (many stems are inferred from the Ming and are marked uncertain in the entry).

## Refused (pass 2)
- Unit 12 i "left him" (ilebe 去了): contradicts the dragging-off of unit 17 only if read as "abandoned"; note states the choice and its uncertainty; pass 1 also refused.
- Unit 6 who falls, unit 14 "could not have beaten me", unit 63 "go to meet": readings carried by the notes; left.
- Unit 57 "Enegen Küiletü" (two names or one): note says so.
- daruqu / darun lemma dara-: glossary already has darun → dara-; kept for house consistency (Written Mongol would suggest daru-; not changed).
- ireġülüġed -üġed vs "linking vowel + -ġed": the shared glossary's kürġeġülüġed uses -üġed; kept for consistency.
- Qutuγtu-Müṅler → "Müngler" (not Münggür): form printed differently from the house name; kept (pass 1).
- Žažiradai → "Jajirat" against house Jadaran/Jadaradai: a different spelling; I will not equate them from outside knowledge.
- qojar-tur 'against' with Ming 行: known entry reads 'among'; note flags the sense; no broaden needed.
- tatažu entry bracket [做妾着] (known) vs Ming 扯着 here: reading 'pull' fits; not broadened.

## Remaining doubts
- ergüje (u38) hortative vs converb; quγul-/quγura- stems (u13, 17, 24); who falls (u6); u23 as a whole; u15 sense; u63 "take word".
- ile- 'went' vs 'send' (u12, 16, 46); γol 'main camp' vs known 'stream'.
- Ungirat, Alchi, Qajiun-Beki, Chagan spellings are new (no house precedent).
- Nothing built or validated yet (`r3.py validate` refuses until a build).

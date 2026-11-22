# read_A: pp. 81–83 (leaves n82–n84), read from the images (text ga has no transcription of this print)

## Line counts

- **p. 81 (n82)** is the title leaf. It has one print line in a double frame. Line count checked: the row profile shows ink only at y 185–262 inside the frame.
- **p. 82 (n83)** has **four** lines. It opens with the ornament ࿐༔ ༔ (see below). After deskewing by −1.7°, the headlines are at y ≈ 167 / 227 / 287 / 347, the top frame is at 131–146 and the bottom frame at 401–410.
- **p. 83 (n84)** also has **four** lines, not five. It opens with the same ornament ࿐༔ ༔. After deskewing by +1.0°, the headlines are at y ≈ 140 / 203 / 266 / 323, the frame is at 107–119 and 380–392. Line spacing is about 62 px, against 55 px on the five-line kha pages.
- That makes 9 print lines in all: 1 + 4 + 4.

## Title leaf p. 81 (n82)

- **Line:** `࿐༔ ༔ཁྲོ་བོའི་བར་དོའཆར་ཚུལ་བསྟན་པ་བཞུགས་སོ༔` ("Here is the teaching of how the wrathful bardo appears").
- **Ornament:** at x 749–815 there is a horizontal swirl: a long tail at the left and two curls. It is not the stacked ༄༅ of the kha leaf fronts. I wrote it as **࿐** (U+0FD0, bka' shog gi mgo rgyan). If the project prefers to normalise all opening ornaments, ༄༅ is the alternative. Then come ༔ (x 816–833), a gap, and ༔ (x 844–862). The same three-part opening stands on p. 82.1 and p. 83.1.
- **Tshegs:** in the title most tshegs are fused into the headlines. Free blobs stand only after ཁྲོ (x 891–894), after ཆར (x 1094–1097) and after བསྟན (x 1255–1259). The others are written in the usual places.
- **བར་དོའཆར:** there is no tsheg between དོ and འ. The pixel dump shows a 3 px headline gap with no bump, and p. 82.1 has the same thing. It needs a fix (below).
- **ཚུལ / བསྟན:** read at ×6/×7. The ཚ has a tsa-phru and a zhabs-kyu tail. The stack is ས over ཏ with a leftward hook, so བསྟན and not བསྣན. This is the same wording as the running text's འཆར་ཚུལ་བསྟན་པར་བྱ་སྟེ.
- **Top margin:** **ག** (above the right half of the frame, x ≈ 1040, y ≈ 100–140), the volume/text letter.
- **Left margin:** a figure-8 lying on its side with a bar under it. Read sideways, this is Arabic **81**, the reproduction's page number, as on n79/n80. There is no Tibetan label.

## Method

1. I found line bands from the row profile. n83 and n84 slope by up to 40 px across the page, so I deskewed them first (rotation chosen to maximise the row-profile variance: n83 −1.7°, n84 +1.0°).
2. Each line was cropped in five overlapping segments at ×3 (LANCZOS). Doubtful syllables were re-cropped at ×5–×8.
3. I used pixel dumps (threshold 128) for tshegs, line ends and letter shapes, and connected-component listings for free tsheg blobs.

**How the tshegs show in this print.** This print rarely leaves a tsheg as a free dot. Most are a small triangle hanging under the right end of the headline. A clear example is ཡང་༔ on 82.3: a free-blob search finds only a handful of tshegs per line.
- I wrote a tsheg wherever that triangle or the usual headline gap shows.
- I wrote **no** tsheg where two syllables' letters touch or sit 1–3 px apart with no bump. Each such place has a `# fix` (below).
- Filler dots are left out (83.2 after བར་; 83.3 after the line-end བཅུ་).

## Line-end tsheg status

| line | ends | tsheg |
|---|---|---|
| 82.1 | བར་དོ་ལ་ | yes (visible dot before the frame) |
| 82.2 | གཅིག་ལ | **no** (pixel dump: ལ ends at x 1590, clean to 1617) → fix |
| 82.3 | སེམས་ཅན་ | yes (free blob x 1603–1613, y 280–286) |
| 82.4 | ཡུན་རིང ༔ མ་ | yes after མ |
| 83.1 | ཞིབ་ཏུ་ངོ་ | yes (dot before the frame) |
| 83.2 | རིག་འཛིན[?] | **no** (no room: the ན stem ends at x 1668, the frame starts at 1670) → fix |
| 83.3 | ལྔ་བཅུ་ | yes (tsheg, then two filler dots, which are left out) |
| 83.4 | འདིནི | **no** (the ན stem and gi-gu end at x 1665, clean to the frame) → fix at the join to p. 84 |

## Start of p. 82 against witness_ga.txt

- **The print:** `࿐༔ ༔ད་ནི་ཁྲོ་བོའི་བར་དོའཆར་ཚུལ་བསྟན་པར་བྱ་སྟེ༔ དེ་ཡང་གོང་དུ་ཞི་བའི་བར་དོ་ལ་འཕྲང་རིམ་པ་བདུན་ཡོད་དེ༔`.
- **The other recension:** `ད་ནི་ཁྲོ་བོའི་བར་དོར་འཆར་ཚུལ་བསྟན་པར་བྱ་སྟེ༔ དེ་ཡང་གོང་དུ་ཞི་བའི་བར་དོ་འཕྲང་རིམ་པ་བདུན་ཡོད་དེ༔`.
- **No extra title formula:** the running text begins directly with ད་ནི, after the ornament.
- **Differences:** the print has དོ (no ར) before འཆར, and it adds ལ after བར་དོ.

## [?] (5)

1. **82.2 ངོ[?]་སྤྲད** (x ≈ 1000–1030)
   - The ཡ-btags tail of 82.1 བྱ curves down right over the ང. A naro would sit in that same place, and it can't be told apart from the tail.
   - The sense needs ངོ་སྤྲད, and the recension has ངོ་སྤྲོད. Taken as ངོ.
   - སྤྲད itself is clear, with no naro (the space above it is clean).
2. **82.3 ཐོབ[?]** (x ≈ 570–595)
   - The bottom bar of 82.2's དུ loop (in བདུན) lies right on the ཐ's headline zone, so a naro would be hidden.
   - No naro tip is free to the right. Read ཐོབ (the sense and the recension). The alternative ཐབ is no word here.
3. **82.3 མང་དུ[?]་བྱུང** (x ≈ 1250–1310)
   - The pixel dump shows one zhabs-kyu loop under the ད–བྱ pair. It joins ད's long descender to the foot of བྱ, so I could not tell whether the u-vowel sits under ད (དུ་བྱང) or under བྱ (ད་བྱུང).
   - Taken as དུ་བྱུང (the sense). There is clearly **no འ** before བྱུང (no letter space), so the print has the past form བྱུང where the recension has འབྱུང.
4. **83.1 འཕྲི་བ་ལ[?]་མེད་པས**
   - After བ (a closed box, x 1222–1250) stands a letter at x 1248–1275: a closed bottom bar with the right stem descending, and no separate left stroke (so not this print's ཡ).
   - I read it as ལ. The recension has nothing here (ཟད་ཅིང་འཕྲི་བ་མེད་པས). Other candidates (ཡང, འང) are ruled out: there is no ང.
   - The sense is awkward ("[there is] no … to diminishing"), so I mark it and note it only.
5. **83.2 འཛིན[?]** (line end)
   - The last stack is 45 px wide (x 1622–1668), against about 28 px for one letter. It looks like ཛི with a ན squeezed against the frame (its right stem descends to y 244).
   - Taken as འཛིན (the sense; 83.3 begins མཁའ་འགྲོའི). The fallback reading is འཛི.

**Close calls not marked:**
- 82.1 / p. 81 **བར་དོའཆར:** no tsheg (see fixes).
- 82.2 ལམ: ལ and མ touch.
- 83.3 འདས: a check-shaped stroke above འ–ད belongs to the ya-btags tail of 83.2 འཁྱམས, not to a naro.
- 83.4 འོང: the naro is clear at ×7.
- 82.4 མང་༔ and 83.2 དང་༔: a fused tsheg bump shows between the letter and the ring.
- 82.4 **ཡུན་རིང ༔:** there is no bump at the head of ང, then a 35 px gap before ༔. Written without a tsheg, with a space as printed.
- 82.4 **སྟུག ༔:** ག, a gap, then ༔. Written with a space as printed. No tsheg after ག is normal.

## Where this print differs from the other recension (print followed)

- **82.1:** བར་དོ(ར)་འཆར. Print བར་དོ་ལ་འཕྲང་རིམ་པ ("in the peaceful bardo there are seven stages"); recension བར་དོ་འཕྲང. Same sense.
- **82.2:** print `དེ་ཡ་རིམ་པ་བཞིན་དུ་ངོ་སྤྲད་པས༔ ཅིག་ལ་མ་འཕྲོད་ཀྱང་གཅིག་ལ་འཕྲོད་དེ`; recension `དེ་རྣམས་ལ་རིམ་པ་བཞིན་དུ་ངོ་སྤྲོད་པ་གཅིག་ལ་ངོ་མ་འཕྲོད་ཀྱང་གཅིག་ལ་ངོ་འཕྲོད་དེ`.
  - The print drops ངོ twice, and has སྤྲད་པས༔ ("since [they] have been introduced").
  - Same sense ("not recognised at one, recognised at another").
- **82.3:** print `ཐོབ་པ་ནི་དཔག་ཏུ་མེད་པར་འབྱུང` (recension …མེད་པ་འབྱུང). Print **`གྲོལ་བ་མང་དུ་བྱུང་ཡང`** ("although many have been liberated", past) against recension `གྲོལ་བར་མང་དུ་འབྱུང་ཡང` ("although many come to liberation"). A small difference in tense.
- **82.4:** print ལྷུན་སྟུག; recension ལྷུན་འཐུག. Both mean "thick, heavy". Same sense.
- **83.1:** print `འཁྲུལ་འཁོར་འདི་ལ་ཟད་པ་མེད་ཅིང་འཕྲི་བ་ལ[?]་མེད་པས`; recension `ཟད་ཅིང་འཕྲི་བ་མེད་པས`. The print states the "no exhaustion" outright. Same sense.
- **83.1–2: print `ངོ་སྤྲད་ཀྱང་མ་གྲོལ་བར` ("even though introduced, not liberated"); recension `ངོ་སྤྲད་ཅིང་མ་གྲོལ་བར` ("introduced and not liberated").** The print is concessive.
- **83.2:** print `ཐུར་དུ་འཁྱམས་པ་ཡང་ཚན་ཆེ་སྟེ` adds ཡང ("those who wander downward are also very many").
- **83.3: print `རིག་འཛིན་མཁའ་འགྲོའི་ལྷ་ཚོགས་ཀྱི་བསུ་བ་འདས་པའི་འོག་ཏུ` ("after the welcome by the assembly of knowledge-holder and ḍākinī deities has passed"); recension `རིག་འཛིན་མཁའ་འགྲོའི་བསུན་མ་འདས་པའི་འོག་ཏུ༔`.** The print adds ལྷ་ཚོགས་ཀྱི, has བསུ་བ for བསུན་མ, and has no ༔ before ཁྲག.
- **83.4:** print `གནས་བསྒྱུར་དེ་འཆར` ("having changed their place/form, appear"; transitive བསྒྱུར, with དེ for ཏེ after ར); recension `གནས་འགྱུར་ནས་འཆར`. Same sense.
- **83.4: print `འཆར་དུ་འོང་བས་གོང་དང་མི་འདྲ་སྟེ༔ འདི་ནི…` ("they come to appear; therefore [it] is unlike before: this is …"); recension `འཆར་དུ་འོང་ངོ་༔ ད་ནི་གོང་དང་མི་འདྲ་སྟེ༔ འདིར་…` ("they appear. Now, unlike before, here …").**
  - The print joins the two sentences with བས, and it has no ད་ནི.
  - It has **འདི་ནི** ("this [is the wrathful bardo]") where the recension has འདིར ("here"). The rest of that sentence is on p. 84 (Reader B).

## Proposed `# fix:` lines

```
# fix: བར་དོའཆར་ཚུལ་བསྟན་པ་བཞུགས => བར་དོ་འཆར་ཚུལ་བསྟན་པ་བཞུགས
# fix: བར་དོའཆར་ཚུལ་བསྟན་པར => བར་དོ་འཆར་ཚུལ་བསྟན་པར
# fix: ཅིག་ལམ་འཕྲོད => ཅིག་ལ་མ་འཕྲོད
# fix: གཅིག་ལའཕྲོད་དེ => གཅིག་ལ་འཕྲོད་དེ
# fix: རིག་འཛིནམཁའ་འགྲོའི => རིག་འཛིན་མཁའ་འགྲོའི
# fix: ༔ འདིནི => ༔ འདི་ནི་
```

What each fix covers:
1. The title, p. 81: the missing tsheg. It is only needed if the title is part of the established text.
2. 82.1: the same missing tsheg.
3. 82.2: the mid-line tsheg between ལ and མ, whose letters touch.
4. The join 82.2→82.3.
5. The join 83.2→83.3.
6. 83.4: the internal tsheg between འདི and ནི, plus the line-end tsheg at the join to p. 84.

The last fix depends on what p. 84.1 opens with. If p. 84.1 is a leaf front opening with an ornament, the drafter should extend the fix across it (Reader B), for example `# fix: འདིནི࿐༔ ༔X => འདི་ནི་࿐༔ ༔X`.

Other joins:
- **82.4→83.1:** the line ends མ་ with a tsheg and 83.1 opens ࿐༔ ༔རིག. Read through the ornament, that gives མ་རིག. No fix is needed beyond however the build already handles a leaf-front ornament.
- **81→82:** the title is a separate leaf and does not join.

No line-end abbreviations (པའཾ, ལཾ, ནམཁའ, subscript-ས) occur on these pages.
I propose no fix for 82.4 `ཡུན་རིང ༔` (no tsheg before ༔ after ང). It is the print's spacing before ༔, like the ངོ༔ cases in 008. Note only. If the editor wants it: `# fix: ཡུན་རིང ༔ => ཡུན་རིང་༔`.

## Suspected misprints

1. **82.2 `དེ་ཡ་རིམ་པ་བཞིན་དུ`** for དེ་ལ་རིམ་པ་བཞིན་དུ ("to those, in order").
   - A side-by-side montage at ×6 shows the letter has this print's ཡ shape: a separate left stroke, then a two-legged body, the same as the ཡ of 82.1 ཡང. It is unlike the curled ལ of 82.3 གྲོལ.
   - Moderate certainty. The sense allows only ལ (the recension has དེ་རྣམས་ལ).
   - Proposed fix (rule 5b, print's reading in the note): `# fix: དེ་ཡ་རིམ་པ => དེ་ལ་རིམ་པ`.
2. **83.1 `འཕྲི་བ་ལ[?]་མེད་པས`:** the sense is unclear (see [?] 4). Kept, note only.
3. **82.3 `ཐོབ`, `མང་དུ་བྱུང`; 83.4 `བསྒྱུར་དེ`:** these are the print's own forms and readings, not misprints. `དེ` after ར (for ཏེ) is kept as the print's habit.

## Gaps

None. No `[…]`.

# Establish — hammurabi-gap-a: The erased columns I — houses and neighbours (from the duplicate tablets)

You are establishing the text of part of the section that was chiselled off the stele (between §65 and
§100), from the ancient duplicate tablets, in public-domain editions only. Nothing is drafted in this run.
**Establishing hammurabi-gap-a establishes the whole erased section** — write BOTH
source/established/hammurabi-gap-a.json (the house-and-neighbour laws, Ungnad's §66 to about §78) and
source/established/hammurabi-gap-b.json (the merchant-and-loan laws before §100), then pin both
(`python3 ../run3/r3.py pin hammurabi hammurabi-gap-a` and `… hammurabi-gap-b`). If gap-a is already
established, gap-b needs nothing more than its pin.

Witness editions (all pre-1930, all in source/witnesses/):
- kpu-vol2_djvu.txt + kpu-vol2-ungnad1909.pdf — Kohler & Ungnad, Hammurabi's Gesetz II (1909), pp. 33–37
  (PDF: find the pages headed "XVII 2—XVIII 3", "XVIII 4—51", "XVIII 52—XXIII 7"): Ungnad's syllabic
  transliteration of the gap laws with, for each stretch, the tablet it comes from (Scheil's Susa
  Fragments I and II — Délégation en Perse X p. 81 ff.; Rm. 277; DT 81; K 8321). Roman type = preserved on
  the Old Babylonian duplicates; italic = restored from the Assyrian copies; [ ] = restored. Anhang
  pp. 180–182 lists every duplicate and what it covers.
- ungnad1909-keilschrifttexte-b.pdf — Ungnad, Keilschrifttexte der Gesetze Hammurapis (1909): his
  autographs of those fragments. The signs come from HERE (read the plate for each line), the readings
  from KPU II.
- poebel1914-pbs5.pdf — Poebel, Historical and Grammatical Texts (PBS V, 1914), no. 93, Plates XXXIX
  (obverse, PDF page 89) and XL (reverse, PDF page 91): the Nippur tablet of the Code (University Museum,
  Philadelphia), which preserves merchant-and-loan laws of the gap.
- cuq1918-nouveaux-fragments.pdf / cuq1918_djvu.txt — Cuq (1918): Scheil's reading of that tablet,
  transliterated (see djvu lines ~430–600 for the Akkadian). Use it as the reading aid for PBS V 93;
  the signs come from Poebel's plates.
- kpu-vol3_djvu.txt pp. 265–267 — Ungnad's translation of the new fragments (for sense only).

Rules (Zev's decision, 2026-10-11): fill the gap from the duplicates; mark every passage with the tablet
it comes from; show a loss that no surviving copy preserves as a gap, never reconstruct it. Restorations
in [ ] made by the 1909/1914/1918 editors from parallel copies are reported in the notes, not adopted
as signs — the signs are what the tablet shows. Where a gap law is known only from a tablet published
after 1930, the fallback is the Aqhat rule: its attested signs may be taken from any edition, never that
edition's restorations or translation — but no such edition is in this repository, so such a law is
shown as a gap and listed in QUESTIONS.md.

Write each established file as JSON:
{"witnesses": {"<siglum>": "<tablet, edition, page/plate>"},
  "laws": [{"law": 66, "approx": false, "units": [{"w": "<siglum>", "ref": "<tablet col. line–line>",
            "lines": ["<transliteration of one tablet line, in KPU/Cuq notation>", ...],
            "lost": false}]}],
  "gaps": ["<what is lost, where>"]}
"law" is Ungnad's number (his "§ cca. 71" → 71 with "approx": true). A wholly lost stretch is a unit with
"lost": true, "lines": [] and a ref saying how much is missing. Then run the pin command; it checks the file.

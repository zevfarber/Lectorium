# Drafter notes — cid-tiradas-137-137b

29 units, 74 verses (3127–3198 incl. Pidal's 3179b, wholly italic, and 3197b, his own number), all tirada 137.
`t` cut by script from packet.md (scratchpad build_137b.py: units given as first/last verse id, `t` = packet
lines joined by "\n", numbers stripped). Asserted in the script: every packet verse used once, in order; 1–6
verses per unit; `l` line count = `t` line count. JSON parses. titleEn/part as in 137a, "second part" in `part`.
source/tiradas.json: tirada 137 runs 3060–3249, so it does NOT end here; the last note says it continues.

Rubric of 137 read on PDF 321 (printed 317); the clauses for this section folded into the first note: El rey
abre la sesión. Proclama la paz entre los litigantes.—El Cid expone su demanda. Reclama Colada y Tizón. Los de
Carrión entregan las espadas. El Cid las da a Pedro Vermúdez y Martín Antolínez.

Footnotes read on the scan (PDF 325–329) and quoted Spanish + English: 3130, 3135, 3137, 3138, 3139, 3145, 3158,
3163, 3164, 3167, 3173, 3178, 3196. None on PDF 329 up to 3198 (the next are 3204, 3205, 3211, 3213). Paragraph
indents seen at 3127, 3145, 3159, 3175 — said in the notes.

Note: page.py needs PyMuPDF, which was missing for python3.13 this time; installed with pip --target into the
scratchpad (not the repo) and run with PYTHONPATH.

## Readings for the reviewer to check
1. **3183 camear**: the m is broken on the scan (looks like "caınear" at zoom 4); read camear (= cambiar, as
   camearon v. 2093). Rendered "change (for others)" — no one could swap them; pueden has no stated subject.
2. **3186 nadi**: a broken mark under the n at zoom 1.4; read nadi, as at v. 2832.
3. **3134 "tuerto, le"**: the mark after tuerto is low, small and tight to the word (zoom 4) — possibly a stray
   mark, not a comma. Kept as in the packet; the note says so; ignored in `l`/`i` sense.
4. **3197 [o viniere sazón]**: the whole half-line Pidal's italic, no footnote; "or the time comes" is our reading.
5. **3179b**: wholly italic (Pidal's restoration), printed plain, flagged in its note; no footnote.
6. **3188 [don Pero]**: Pidal's restoration; "Don Pero" in `i` per conventions (house of 115-117), identified in
   the note as Per Vermudoz (Pidal's rubric 'Pedro Vermúdez'; sobrino at v. 2351). The brief said "= Per
   Vermudoz (house)"; if the owner prefers "Per Vermudoz" in `i`, change one word.
7. **3140 bolviere**: 'throw into disorder' is our reading of bolver here (no Pidal note, no vocabulary to hand).
8. **3141 quitar me a el reyno**: split future = me quitará el reino, rendered "shall leave my kingdom"
   (banishment), the me read as the king's dative; flagged as a reading.
9. **3132 por el amor de**: "out of favour to my Çid" (house 'favour' for a lord's amor); 3147 por mi amor and
   3157 perdieron mi amor ("lost my favour", the Çid as father-in-law) — check register.
10. **3163 ivan trayendo**: Pidal's gloss 'tratando' followed.
11. **3177 saca[n]**: the n italic (Pidal's); the present after the preterites kept.
12. **3190 mejora en señor**: "it is the better for its lord" — our reading of a compressed phrase.
13. **3194**: Pidal prints an opening “ at line start (instead of ”), a slip; repeated line-initial quotes are
    dropped by convention anyway; mentioned in the note.
14. **3195 Remont Verenguel** kept so in `i`, as in cid-tiradas-56-59 (Ramón Berenguer in the note);
    Barçilona "Barcelona" in `i` (as "count of Barcelona" in 49-55).
15. **3162 y el bando**: y for e as printed (packet); not further checked on the scan beyond zoom 1.4.

Two independent transcribers read the same pages of a 19th-century printed Arabic book (Macnaghten's Alif Laila, Calcutta 1839, naskh type; prose unpointed, verse pointed). They disagree at the spots listed in a file. Decide each one from the page images.

Files, all under RUN = __RUN__ :
- RUN/disputes.json — {"<p>": [[line_index_pass1, line_index_pass2, kind, pass1_text, pass2_text], ...]}, p = absolute PDF page number (folder RUN/p<ppp>/), indices are 0-based printed body lines, kind is "word" or "MISSING LINE".
- RUN/p<ppp>/pass1.json and pass2.json — the two full transcriptions (lists of {"line", "t", ...}).
- RUN/p<ppp>/band1.png, band2.png, band3.png — the page's text block in three overlapping bands at 1.3x, top to bottom. These are complete; use them to find each disputed line.
- RUN/p<ppp>/lineNN.png — 2x crops of detected lines; NN may not equal the printed line number (some pages have merged/dropped crops), so locate a line by its words, not its number.

For each dispute: find the printed line in a band (and the matching crop if you want more magnification), look at the actual letters and marks, and decide which reading matches the print — or give a third reading if neither does. Known facts about this edition that both transcribers tend to override with their own expectations: it usually prints قل for قال (accept قل when that is what is printed); it prints ة in اخوة "his brother"; it prints a bare alif where modern spelling has أ/إ and only sometimes a hamza or madda — record exactly what is printed, never what modern spelling requires; a stretched kashida inside a word is not a space; an end-of-line filler dash is written "—"; the night label الليلة الاولى (etc.) is printed inline at the head of a prose line and stays inside that line.

For "MISSING LINE" disputes: if the line exists in the print as its own line, give its text as the verdict; if it does not exist as a separate line (it is part of another line, or a header/catchword), give the verdict "" (empty) and say so in the note.

Also read every page join: the last words of each page and the first words of the next (the run will tell you the page range). If a join does not read as continuous text, say which join and what seems to be missing, in a final entry {"p": <first page of the join>, "join": true, "note": "..."}.

Write RUN/verdicts.json with the Write tool: a list of {"p": <p>, "i1": line_index_pass1, "i2": line_index_pass2, "pass1": "...", "pass2": "...", "verdict": "<the text as printed>", "confidence": "high|medium|low", "note": "<short reason>"} — one entry per dispute, in the order of disputes.json, then any join entries. Reply DONE.

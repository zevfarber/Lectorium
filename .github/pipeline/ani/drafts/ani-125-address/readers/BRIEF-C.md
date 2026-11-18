# Third reader brief — ani-125-address

Read BRIEF.md (same folder) first: its conventions and house rulings apply. Two independent readers (A and B) read the
same pages; `python3 ../../../hooks.py diff A.json B.json` lists where they differ (diffN.txt). Your job: for EVERY
place in the diff, look at a tight crop of exactly that word (render with run3/page.py at --zoom 4 or 5 with --clip
around the word only) and decide the signs, the order, q, Budge's transliteration and English as printed, and the flags
(rubric, restored, approx, unsure). Choose A, B, or your own reading; never "complete" a word from its
transliteration without seeing each sign. Use Budge's transliteration as a check: the phonetic signs must spell it.
Where the readers split or join words differently, the page decides (one sign group over one transliteration group).

Also check, for every word where A and B AGREE but either marked "unsure"/"approx", whether the agreed reading stands
(a quick look); fix it if it is clearly wrong and record that under "alsoFixed".

Write a script that builds the merged word list: every word where A and B agree is taken from A (merging the flags:
keep "unsure"/"approx" only if still true after your look, and say what the type shows), every differing place is
replaced by your decision. Output file (path in your task):
{"reader": "C", "pages": [..], "words": [...merged, in order...],
 "decisions": [{"page":, "line":, "budge":, "A": "...", "B": "...", "chose": "A|B|own", "signs": [...], "why": "..."}],
 "alsoFixed": [...], "classRulings": {"<sign class>": "ruling applied to every word with it"},
 "counts": {"A": n, "B": n, "own": n}}
Prefer class rulings for a recurring sign (decide it once from the clearest instance, apply it everywhere, list it).
Do not modify A*.json or B*.json, any other file in the repository, and do not run git.

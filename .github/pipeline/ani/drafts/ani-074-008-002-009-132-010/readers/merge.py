import json
# decisions: (stretch, A-index) -> dict(decision, signs, q, approx, budge, why)
D = {}
def d(st, i, dec, why, **kw): D[(st, i)] = dict(stretch=st, word=i, decision=dec, why=why, **kw)
# stretch 1
d(1,10,'A',"Ani's det on p. 118 is the kneeling man with arm raised, no flail visible at zoom 6: A1")
d(1,30,'A',"the det of ḥefṭ is a man seated as on a chair (no chair drawn), one arm raised: A50 approx", signs=['V28','I9','D46','A50','A1'], approx=['A50'])
d(1,36,'B',"pool on legs coded N37 + D54 (house ruling, Spell 147 gates)", signs=['N37','D54','G17','X1','D54','A1'], q='0:1-2-3:4-5', approx=['N37'])
d(1,40,'B',"Budge prints ā (macron), not à", budge='ābeḥ')
d(1,66,'B',"Budge prints the dots close against ṭep", budge='ṭep....')
d(1,98,'A',"moon-god figure (crescent and disc): seated god A40 approx (B2 independently the same in Spell II)", signs=['A40'], approx=['A40'])
# stretch 2
for i in (2,22): d(2,i,'B',"O1 over D21 over D54, X1 beside: reading order O1 D21 X1 D54", signs=['O1','D21','X1','D54'], q='0:1:3-2')
d(2,7,'B',"the flat sign has an upright tab at its right end: U15 (house: code what is printed; m expected)", signs=['U15','X1','N33'], q='0:1*2', approx=['N33'])
for i in (13,18): d(2,i,'A',"same flat sign with right-hand tab as in mit: U15 (Budge reads ā; code what is printed)", signs=['T21','Z1','U15'])
d(2,30,'A',"top-right flat bar has the upright tab: U15", signs=['K1','U15','Z7','U15'])
d(2,48,'A',"the mark before ta is in Budge's transliteration only (a broken '['?); no bracket in the sign line", unsure_add="Budge's transliteration prints a small broken mark like '[' before ta; the sign line has no bracket")
d(2,49,'B',"emmā's last sign the low flat ā D36 (house for mā)", signs=['G17','G17','D36'])
d(2,56,'B',"āba's first sign is the sceptre with crossbar and block on a stand: S42 approx (as both stretch-1 readers)", signs=['S42','D58','G29','G1','Y1a'], approx=['S42'])
d(2,57,'B',"Budge prints ḥ with the dot", budge='àmmeḥet')
d(2,64,'B',"the ram's head stands on a flat bar, which is coded: F7 N37 (approx) X1", signs=['F7','N37','X1'], q='0:1-2', approx=['N37'])
d(2,67,'A',"maa: eye with the sickle over it coded D4 U1 (house order)")
d(2,68,'B',"āba's first sign S42 approx", signs=['S42','D58','G29','Y1a','A1'], approx=['S42'])
for i in (71,79,89,101): d(2,i,'A',"the seated figures after àtef coded A1 (house ruling, Spell 17 part 2); the type shows a long-wigged figure close to A40")
d(2,75,'A',"first-person figure: A1 (house); hand near face but arm raised")
d(2,103,'A',"flat sign with right tab U15; the loop crossed by a band V38 approx (house)", signs=['O34','U15','V28','V38','Y1a','V31','G43','Z1'], approx=['V38'])
# stretch 3
d(3,12,'B',"àn's first sign is a reed M17 here, not the fish-like W25", signs=['M17','N35'])
d(3,20,'B',"Q3 over a long low flat sign, then a bar with hanging ends over D54: Q3 T9 N1 D54", signs=['Q3','T9','N1','D54'], approx=['T9','N1'])
d(3,24,'B',"after the cobra a flat roll with a tie is printed (Y1 shape), not the hand; Budge reads ṭ", signs=['O34','I10','Y1','I9','Z7','U15','N35','A1'])
d(3,30,'B',"rectangle with oblique strokes: N37 approx (house for ś)", signs=['O34','N37','Z9','D54','N35','A1'], approx=['N37','Z9'])
d(3,37,'B',"the sinuous sign is the sandbank N20 (wḏb)", signs=['V24','D58','N20','N21','Z2'], approx=['V24'])
d(3,54,'A',"first sign the crossed spindle shape: netting needle V26 (ꜥḏ) approx", signs=['V26','D46','T30','U15','N35','A1'], approx=['V26','T30'])
d(3,62,'B',"the tether stands on legs: V15", signs=['V15','X1','U15','N35','A1'], q='0-1:2-3:4')
d(3,77,'A',"ārt: D36 over D21, X1 over the jaw-like curl F19 approx", signs=['D36','D21','X1','F19','A1'], q='0:1-2:3-4', approx=['F19'])
d(3,92,'B',"the ⊥-shaped sign with pointed arms between χemt and em, with no transliteration under it, is the negation det D35 of ḫm; the hooked bar is U31 approx", signs=['Aa1','U31','X1','N35A','D35'], approx=['U31'])
json.dump({'decider':'run lead (routine model) from crops at zoom 2.5–6','decisions':list(D.values())}, open('decisions.json','w'), ensure_ascii=False, indent=1)
KEYS = ('page','plate','chapter','line','signs','q','budge','gloss','rubric','restored')
out = []
for st in (1,2,3):
    A = json.load(open('A%d.json'%st))['words']; B = json.load(open('B%d.json'%st))['words']
    # align B to A
    if st == 1: bmap = {i: (i if i < 75 else i+1) for i in range(len(A))}
    elif st == 3: bmap = {i: (i if i < 23 else (None if i == 23 else (i-1 if i < 93 else (None if i == 93 else i-2)))) for i in range(len(A))}
    else: bmap = {i: i for i in range(len(A))}
    for i, x in enumerate(A):
        y = B[bmap[i]] if bmap[i] is not None else None
        if st == 1 and i == 75:
            for j in (75, 76):
                w = {k: B[j][k] for k in KEYS if k in B[j]}
                if B[j].get('approx'): w['approx'] = B[j]['approx']
                w['unsure'] = (B[j].get('unsure','') + ' · ' if B[j].get('unsure') else '') + "Decision (B): the kneeling man stands alone over Budge's dots, apart from χakeru (A had it as χakeru's det)"
                out.append(w)
            continue
        if st == 1 and i == 76:
            w = {k: B[77][k] for k in KEYS if k in B[77]}; out.append(w); continue
        if st == 3 and i == 93: continue  # V12 '—' word: merged into χemt (decision 3/92)
        w = {k: x[k] for k in KEYS if k in x}
        if y is not None and st == 3 and y.get('rubric'): w['rubric'] = True
        notes = []
        if x.get('unsure'): notes.append(x['unsure'])
        if y is not None and y.get('unsure') and y['unsure'] != x.get('unsure'): notes.append('B: ' + y['unsure'])
        ap = list(dict.fromkeys(x.get('approx', []) + (y.get('approx', []) if y else [])))
        dd = D.get((st, i))
        if dd:
            if 'signs' in dd:
                w['signs'] = dd['signs']
                if dd.get('q'): w['q'] = dd['q']
                else: w.pop('q', None)
                ap = dd.get('approx', [])
            if 'budge' in dd: w['budge'] = dd['budge']
            if 'unsure_add' in dd: notes.append(dd['unsure_add'])
            notes.append('Decision (%s): %s' % (dd['decision'], dd['why']))
        if st == 3 and i == 23: notes.append("Decision (A): Budge prints àu twice (end of p. 121 row 8 and in row 9); B had only the first")
        if st == 3 and y is not None and y.get('rubric') and not x.get('rubric'): notes.append('Decision (B): the title runs under the ruled line that ends before Àusàr, as in the other titles of this part: rubric')
        ap = [c for c in ap if c in w['signs']]
        if ap: w['approx'] = ap
        else: w.pop('approx', None)
        if notes: w['unsure'] = ' · '.join(notes)
        out.append(w)
json.dump(out, open('merged.json','w'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for w in out if w.get('rubric')), [(w['page'],w['budge']) for w in out if w.get('restored')], sum(1 for w in out if w.get('approx')), sum(1 for w in out if w.get('unsure')))
for w in out:
  if w['budge'] in ('àu','satet - nà',"set'eṭefu - nà",'χemt','em','χāāu - f') and w['page'] in (121,122): print(w['page'],w['budge'],w['signs'])

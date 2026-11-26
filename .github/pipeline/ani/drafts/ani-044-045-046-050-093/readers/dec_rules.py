# Stretch 2 (pp. 108-109), decided by the run lead from crops at zoom 3-5
dec('2', 5, 'B', 'the sign is a domed block with a knife laid diagonally across it: knife-on-block T29, not the butcher knife alone')
for i in (11, 23, 35, 36, 56):
    dec('2', i, 'A', 'θes is printed as a horizontal cord with a knot and two loops (girdle knot S24, ṯs), not the tether V13')
dec('2', 22, 'A', 'tall thin staff with a curl at its foot; neither S38 nor S39 is exact; kept A (S38 approx)', unsure='tall thin staff with a small curl at its lower right, under the water line; S38 (crook) approx, S39 possible')
dec('2', 30, 'B', 'flat bar on a small foot carrying two knobbed uprights: offering-table shape R3 (approx) rather than a balance; no transliteration or English under it', unsure='printed with no transliteration and no English: a flat bar on a small foot with two knobbed uprights on it; R3 approx (U38 balance possible)')
dec('2', 33, 'B', 'a short stroke Z1 is printed under the lung-and-windpipe sign F36', approx=['F36'])
dec('2', 50, 'A', 'the vulture carries the sickle on its back as one ligature (house: U1 over the vulture as a ligature where so printed)', unsure='sickle-and-vulture ligature: the sickle rises from the vulture\'s back; coded U1 G1')
dec('2', 54, 'B', 'the marks after each flat land sign are two slanting serifed strokes (Z4), not bow-ties', approx=['N16'], unsure='each N16 followed by two slanting strokes with serifs, coded Z4; earlier parts coded a similar shape N21 approx')
dec('2', 55, 'A', 'S24 with the coil Z7 above, bolt O34 with U15 below: reading order top then bottom, group by group')
dec('2', 61, 'A', 'head D1 and stool Q3 side by side above the two strokes Z4')
dec('2', 67, 'A', 'straight flat sign with an upright tab and no upcurled end: the flat arm D36 (Budge reads a, not ā)', unsure='first sign a straight flat bar with an upright tab at the right, no upcurled end: D36 (U15 possible); Budge reads a')
dec('2', 83, 'A', 'determinative: a low flat base carrying a small sprawling shape; P1 approx, as in the same word on p. 110', unsure='determinative a low flat base carrying a small sprawling shape (boat P1 approx; duckling G47 or fire-drill U29 possible)')
dec('2', 94, 'B', 'the sign over the water line is a hoe with a cross-brace (U7 approx); the last sign is a phallus with no issue printed (D52)', approx=['U7'])
dec('2', 98, 'A', 'ennu\'s low tabbed sign U19 (house); the bracketed restoration is a long rounded bar over D54, Y1 approx', unsure='U19 approx (house); in [ ] a long rounded bar with tabbed ends (Y1 approx, V33 possible) over D54')
dec('2', 102, 'B', 'the bottom sign is a flat roll with a small tie on top (Y1), not a ticked branch')
dec('2', 107, 'A', 'Budge prints Bàbà (reed accents on both a\'s)')
BIRD = 'small bird with two human-like arms, one raised behind holding a stick, one held forward; the same shape in seχem (p. 108), useru and seχemu (p. 109): coded G24 approx (pinioned lapwing) throughout'
dec('2', 111, 'B', 'bird with arms: G24 approx, coded alike in all three words', approx=['G24'], unsure=BIRD)
dec('2', 115, 'B', 'bird with arms: G24 approx, coded alike in all three words', approx=['G24'], unsure=BIRD)
# Stretch 3 (pp. 110-111)
for i in (0, 75, 90):
    dec('3', i, 'B', 'determinative: a low flat base carrying a small sprawling shape, not a duckling; P1 approx', unsure='determinative a low flat base carrying a small sprawling shape (boat P1 approx; duckling G47 possible)')
dec('3', 2, 'A', 'àn is printed D35 alone; no water line under it')
for i in (12, 86):
    dec('3', i, 'A', 'the flat oval with a tab is the hand D46; the hatched slanting stem is the branch M3 (approx), with the knife T30 below', unsure='N37 hatched pool over the flat arm; flat hand D46; a slanting stem with side ticks (M3 approx; M44 possible); knife T30; dashed Z1')
dec('3', 41, 'B', 'tall stem with a crossbar at its foot and a horned knob on top: like an inverted nefer F35 (approx), not a papyrus stem', unsure='tall stem with a crossbar near its foot and a two-horned knob on top; F35 approx (inverted), M13 possible')
dec('3', 59, 'A', 'the long flat oval before the numeral 8. is the hand D46, then the leg-and-foot D58 and the two horns F16; numeral 8. printed inside the word')
dec('3', 61, 'A', 'transliteration as printed, "Rā - χeperà"')
dec('3', 71, 'B', 'the second sign is an upright with a foot turned left, the same shape as D58 in ṭeb - k; Budge reads no b here', approx=['D58', 'G27'], unsure='second sign an upright with a foot at its base, the shape of D58 in ṭeb - k, though Budge reads no b (Aa28 possible); numeral 9. printed inside the word')
dec('3', 103, 'A', 'the sickle U1 curves round a small flat bar Aa11, over the flat arm D36')
# Stretch 1 (pp. 105-108); B has one more word (àu | χemu), so B indices run one ahead from word 27
def dec1(ia, ib, who, why, **k):
    A, B = rd('1', 'A'), rd('1', 'B')
    D.append(dict(stretch=1, word=ia, wordB=ib, page=A[ia]['page'], budge=(A if who=='A' else B)[ia if who=='A' else ib]['budge'],
        A=' '.join(A[ia]['signs'])+' | '+(A[ia].get('q') or ''), B=' '.join(B[ib]['signs'])+' | '+(B[ib].get('q') or ''),
        decision=who, signs=k.get('signs') or (A[ia] if who=='A' else B[ib])['signs'],
        q=k.get('q', (A[ia] if who=='A' else B[ib]).get('q', '')),
        approx=k.get('approx', [c for c in (A[ia] if who=='A' else B[ib]).get('approx', []) if c in (k.get('signs') or (A[ia] if who=='A' else B[ib])['signs'])]),
        why=why, **({'unsure': k['unsure']} if 'unsure' in k else {})))
NEM = 'slender slanting rod (knife T34 approx, nm); F25 possible'
dec1(5, 5, 'B', 'the rod in nem is a slender slanting knife-like sign: T34 approx (nm)', approx=['T34'], unsure=NEM)
dec1(12, 12, 'B', 'the low rectangle is hatched: O31 (house: the hatched low rectangle O31)')
dec1(20, 20, 'B', 'a low flat sign with an upright at its end, over D21: U15 shape (approx), although Budge reads s', approx=['U15'], unsure='first sign a low flat sign with an upright at one end (U15 shape; T12 possible); Budge reads s')
dec1(25, 25, 'B', 'the determinative is a crouching man behind a wall: A5')
dec1(27, 27, 'B', 'Budge prints àu and χemu as two transliteration groups with a space: two words (word division = Budge)')
dec1(27, 28, 'B', '(second word of the split)')
dec1(30, 31, 'own', 'tall staff with a crossbar at the top (R15 approx; S40 possible); X1 over Z1; the small loop-and-tail curl is F51 (approx), the same curl as in āt on p. 107', signs=['R15','X1','Z1','F51'], approx=['R15','F51'], unsure='tall staff with a crossbar near the top (R15 approx, S40 possible); a small curl with a loop and a tail (F51 approx, Z7 possible); Budge prints (?) after àpt')
dec1(36, 37, 'B', 'hatched low rectangle O31 over U15, as in unu')
dec1(48, 49, 'B', 'the cobra I10 stands above, the bolt O34 and the viper I9 below: I10 O34 I9 (Budge t\'esef)')
dec1(69, 70, 'B', 'nem with the same slanting rod as in the title (T34 approx); the flat sign has no ā in Budge: U15 (house)', approx=['T34'], unsure=NEM)
for ia, ib in ((82, 83), (86, 87), (91, 92)):
    dec1(ia, ib, 'A', 'the determinative is a seated man hunched forward with hands at his knees, no stick: A7 (weary man)')
dec1(87, 88, 'A', 'the small loop-and-tail curl is F51 (approx), as in àpt(?)', approx=['F51'])
dec1(128, 129, 'own', 'the last sign is a bird with two arm-like projections, the same shape as in useru and seχemu: G24 approx', signs=['O34','S42','G17','Aa1','G24'], q='0-1-2-3-4', approx=['G24'], unsure=BIRD)
dec1(130, 131, 'B', 'O34 stands over the first looped cord and the flat hand D46 over the second: column order O34 V6 D46 V6, then I9', approx=['V6'])

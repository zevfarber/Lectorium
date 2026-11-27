import json,sys,difflib
A=json.load(open(sys.argv[1]))['words'];B=json.load(open(sys.argv[2]))['words']
ka=[w['budge'] for w in A];kb=[w['budge'] for w in B]
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,ka,kb,autojunk=False).get_opcodes():
  if op=='equal':
    for i,j in zip(range(i1,i2),range(j1,j2)):
      for k in ('page','plate','chapter','line','rubric','restored','q'):
        if A[i].get(k)!=B[j].get(k): print(i,j,A[i]['budge'],k,A[i].get(k),'|',B[j].get(k))
  else: print(op,ka[i1:i2],kb[j1:j2])

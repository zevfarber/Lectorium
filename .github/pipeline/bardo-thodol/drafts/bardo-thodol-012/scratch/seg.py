import json,glob,re,collections,sys
sys.path.insert(0,'.')
TS='་'
P='༔།'
def key(tok): return tok.rstrip(P).rstrip(TS)
V=collections.Counter()
for f in sorted(glob.glob('drafts/bardo-thodol-0*/units.json')):
    if '012' in f: continue
    for u in json.load(open(f))['sentences']:
        for t in u['w'].split():
            if t!='/': V[key(t)]+=1
G=json.load(open('glossary.json'))
s=open('drafts/bardo-thodol-012/scratch/fixed.txt').read()
# syllables: split after tsheg or after punctuation run
syl=re.findall(r'[^་༔།]+(?:་|[༔།]+)?|[༔།]+',s)
assert ''.join(syl)==s
# greedy longest match using V (frequency>=1) then glossary
out=[];i=0
while i<len(syl):
    best=1
    for n in range(6,1,-1):
        if i+n>len(syl): continue
        cand=''.join(syl[i:i+n])
        # don't swallow punctuation mid-token
        if any(re.search('[༔།]',x) for x in syl[i:i+n-1]): continue
        k=key(cand)
        if V[k]>=1:
            best=n;break
    out.append(''.join(syl[i:i+best])); i+=best
open('drafts/bardo-thodol-012/scratch/auto.txt','w').write(' '.join(out))
print(' '.join(out))
json.dump(V,open('drafts/bardo-thodol-012/scratch/vocab.json','w'),ensure_ascii=False)

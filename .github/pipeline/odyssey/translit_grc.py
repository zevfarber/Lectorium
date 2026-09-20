#!/usr/bin/env python3
"""Romanize polytonic Greek per claude/greek-aesop-conventions.md:
ē/ō; th/ph/ch; y for υ but u in diphthongs; h = rough breathing; rh initial ῥ, rr internal;
ēi/āi/ōi for iota subscript; nk/ng/nx/nch for γ before κ γ ξ χ; accents omitted; punctuation carried."""
import unicodedata as U,re
BASE={'α':'a','β':'b','γ':'g','δ':'d','ε':'e','ζ':'z','η':'ē','θ':'th','ι':'i','κ':'k','λ':'l','μ':'m','ν':'n','ξ':'x','ο':'o','π':'p','ρ':'r','σ':'s','ς':'s','τ':'t','υ':'y','φ':'ph','χ':'ch','ψ':'ps','ω':'ō'}
ROUGH='̔';SMOOTH='̓';IOTASUB='ͅ';DIAER='̈';ACC={'́','̀','͂'}
def word(w):
    # decompose into (base, marks)
    segs=[]
    for ch in U.normalize('NFD',w):
        if U.combining(ch): segs[-1][1].add(ch)
        else: segs.append([ch,set()])
    out=[];n=len(segs);i=0;rough=False
    res=[]
    for k,(b,m) in enumerate(segs):
        lb=b.lower();up=b!=lb
        if lb not in BASE: res.append(b);continue
        r=BASE[lb]
        prev=segs[k-1] if k else None
        nxt=segs[k+1] if k+1<n else None
        if lb=='υ':
            pv=prev[0].lower() if prev else ''
            # u in diphthongs: second element after α ε η ο ω (no diaeresis, and first vowel carries no breathing/accent) or first element of υι
            if pv in 'αεηοω' and pv and DIAER not in m and not (prev[1]&(ACC|{ROUGH,SMOOTH})): r='u'
            elif nxt and nxt[0].lower()=='ι' and DIAER not in nxt[1] and not (m&(ACC|{ROUGH,SMOOTH})): r='u'
        if lb=='ι' and DIAER in m: r='ï'
        if lb=='υ' and DIAER in m: r='ÿ'
        if lb=='γ' and nxt and nxt[0].lower() in 'κγξχ': r='n'
        if lb=='ρ' and ROUGH in m: r='rh'; m=m-{ROUGH}
        if lb in 'αηω' and IOTASUB in m: r={'α':'ā','η':'ē','ω':'ō'}[lb]+'i'
        if ROUGH in m:
            # breathing sits on 2nd vowel of a diphthong: h goes before the whole diphthong
            if prev and prev[0].lower() in 'αεηοωυ' and res and k==1: res.insert(len(res)-1,'H' if segs[0][0]!=segs[0][0].lower() else 'h'); 
            else: r=('H' if up else 'h')+ (r if not up else r); 
            if up and not (prev and k==1): r='H'+BASE[lb] if lb not in 'αηω' or IOTASUB not in m else 'H'+r[1:]
        elif up: r=r[0].upper()+r[1:]
        res.append(r)
    s=''.join(res)
    # fix capital diphthong with H inserted: 'HAi' -> 'Hai'
    if s.startswith('H') and len(s)>1 and s[1].isupper(): s='H'+s[1].lower()+s[2:]
    return s
W=re.compile(r"[Ͱ-ΆΈ-Ͽἀ-῿]+")
def translit(t): return W.sub(lambda m:word(m.group(0)),t)
if __name__=='__main__':
    import json,sys
    for f in sys.argv[1:]:
        d=json.load(open(f,encoding='utf8'));bad=0
        for u in d['sentences']:
            mine=translit(u['t'])
            if mine!=u['tr']:
                bad+=1
                a=mine.split();b=u['tr'].split()
                print(f,[ (x,y) for x,y in zip(a,b) if x!=y][:8])
        print(f,'units',len(d['sentences']),'mismatching',bad)

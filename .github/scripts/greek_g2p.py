#!/usr/bin/env python3
"""Polytonic Greek -> IPA pins for Lectorium's reconstructed-Attic reading (after Allen, Vox Graeca),
restricted to the phoneme set Google's de-DE Neural2 voice accepts (claude/norse-audio-carrier-findings.md §3).

Honest limits of the carrier, stated once in each text's `source`:
- pitch accent is rendered as stress on the accented syllable;
- vowel length survives only as quality contrast (ε e / η ɛ, ο o / ω ɔ, short ɪ ʏ a / long iː y aː);
  α ι υ count as long only where the text shows it (circumflex, iota subscript); unmarked they read short;
- ει merges with ε as [e], ου is [u];
- geminate consonants are read single;
- ASPIRATES: φ θ χ read [pʰ tʰ kʰ] if the voice accepts ʰ (ASP), else fall back to p t k.
"""
import unicodedata as U, re, sys, json
ROUGH='̔'; SMOOTH='̓'; ISUB='ͅ'; DIA='̈'
ACUTE='́'; GRAVE='̀'; CIRC='͂'; MAC='̄'; BREVE='̆'
ASP = 'ʰ'           # set to '' if the voice rejects it
VOW=set('αεηιουω')
def segs(w):
    out=[]
    for ch in U.normalize('NFD',w):
        if U.combining(ch):
            if out: out[-1][1].add(ch)
        else: out.append([ch.lower(),set()])
    return out
def ipa(word):
    s=segs(word); n=len(s)
    # 1. group into units: vowel nuclei (with diphthongs) and consonants
    units=[]; i=0
    while i<n:
        b,m=s[i]
        if b in VOW:
            nb,nm=(s[i+1] if i+1<n else (None,set()))
            if nb=='ι' and b in 'αεου' and DIA not in nm:
                units.append(('V',b+'ι',m|nm)); i+=2; continue
            if nb=='υ' and b in 'αεηο' and DIA not in nm:
                units.append(('V',b+'υ',m|nm)); i+=2; continue
            if b=='υ' and nb=='ι' and DIA not in nm:
                units.append(('V','υι',m|nm)); i+=2; continue
            units.append(('V',b,m)); i+=1
        else:
            units.append(('C',b,m)); i+=1
    out=[]; stressed=None
    for k,(t,b,m) in enumerate(units):
        acc = bool(m & {ACUTE,CIRC}) or (GRAVE in m)
        if t=='V':
            long_ = CIRC in m or ISUB in m or MAC in m
            if b=='α': v='aː' if long_ else 'a'
            elif b=='ε': v='e'
            elif b=='η': v='ɛ'
            elif b=='ι': v='iː' if long_ else 'ɪ'
            elif b=='ο': v='o'
            elif b=='ω': v='ɔ'
            elif b=='υ': v='y' if long_ else 'ʏ'
            elif b=='αι': v='aɪ'
            elif b=='ει': v='e'
            elif b=='οι': v='ɔʏ'
            elif b=='ου': v='u'
            elif b=='υι': v='ʏj'
            elif b=='αυ': v='aʊ'
            elif b=='ευ': v='eʊ'
            elif b=='ηυ': v='ɛʊ'
            elif b=='ου': v='u'
            else: v='o'
            if ISUB in m: v+='j'
            if ROUGH in m: out.append(('C','h'))
            out.append(('V',v))
            if acc and stressed is None: stressed=len(out)-1
        else:
            nxt=units[k+1][1] if k+1<len(units) else ''
            if b=='γ' and nxt in ('κ','γ','χ','ξ'): c='ŋ'
            elif b=='σ' or b=='ς': c='z' if nxt in ('β','γ','δ','μ') else 's'
            elif b=='ζ': c='zd'
            elif b=='ξ': c='ks'
            elif b=='ψ': c='ps'
            elif b=='φ': c='p'+ASP
            elif b=='θ': c='t'+ASP
            elif b=='χ': c='k'+ASP
            else: c={'β':'b','γ':'g','δ':'d','κ':'k','λ':'l','μ':'m','ν':'n','π':'p','ρ':'r','τ':'t'}.get(b,'')
            if not c: continue
            if out and out[-1][0]=='C' and out[-1][1]==c: continue   # geminate -> single
            out.append(('C',c))
    nv=sum(1 for t,_ in out if t=='V')
    if stressed is not None and nv>1:
        # put ˈ before the onset: back up over consonants, max two, (stop+liquid) or one
        j=stressed
        cons=[]
        while j-1>=0 and out[j-1][0]=='C': j-=1; cons.append(out[j][1])
        if len(cons)>=2:
            # keep a legal-ish onset: last consonant, or stop+liquid
            a=out[stressed-2][1] if stressed-2>=0 else ''; b=out[stressed-1][1]
            j = stressed-2 if (b in ('r','l') and a[:1] in 'pbtdkg') or a=='s' else stressed-1
        seq=[x for _,x in out]; seq.insert(j,'ˈ'); return ''.join(seq)
    return ''.join(x for _,x in out)
if __name__=='__main__':
    for w in sys.argv[1:]: print(w, ipa(w))

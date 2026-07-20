#!/usr/bin/env python3
# Model-free forced aligner for Lectorium prepared audio.
# Produces karaoke word-timings (align.json) from per-sentence TTS clips + the story text,
# using espeak-ng (reference) + librosa DTW. No ML-model download needed (works in the
# firewalled sandbox, unlike the vosk align.py).
#
# Deps:  apt-get install -y espeak-ng espeak libespeak-dev   ;   pip install librosa   (ffmpeg preinstalled)
# Usage: python3 align_dtw.py <story-id> [audio_dir]
#        reads <story-id>.json and <audio_dir>/<i>.mp3  (default audio_dir = audio/<story-id>)
#        writes <audio_dir>/align.json = {"<sentIdx>": [[start,end], ... one per WORD_RE token]}
import json, re, subprocess, sys, os
import numpy as np, librosa
from collections import defaultdict

SR=16000; HOP=160
WORD_CLASS='A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ'                    # matches reader.html WORD_RE (Latin)
WORD_RE=re.compile('['+WORD_CLASS+']+(?:[-\\[\\]()]['+WORD_CLASS+']+)*')
VOICE=os.environ.get("ESPEAK_VOICE","de")           # 'de' German, 'fr' French, etc.

def load(p): 
    y,_=librosa.load(p,sr=SR,mono=True); return y
def espeak_word(w):
    out="/tmp/w.wav"; clean=re.sub(r'[\[\]()]',' ',w)
    subprocess.run(["espeak-ng","-v",VOICE,"-s","160","-w",out,clean],
                   stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
    y,_=librosa.load(out,sr=SR,mono=True)
    yt,_=librosa.effects.trim(y,top_db=35)
    return yt if len(yt)>=160 else y
def mfcc(y):
    m=librosa.feature.mfcc(y=y,sr=SR,n_mfcc=13,hop_length=HOP,n_fft=400)
    return np.vstack([m,librosa.feature.delta(m)])

def align_sentence(mp3,text):
    toks=WORD_RE.findall(text); y=load(mp3); D=len(y)/SR
    if not toks: return [],D
    parts=[]; bounds=[]; cur=0; gap=np.zeros(int(0.03*SR))
    for w in toks:
        wy=espeak_word(w); s=cur; parts.append(wy); cur+=len(wy); bounds.append((s,cur)); parts.append(gap); cur+=len(gap)
    Xr=mfcc(np.concatenate(parts)); Xt=mfcc(y)
    _,wp=librosa.sequence.dtw(X=Xr,Y=Xt,metric='cosine'); wp=wp[::-1]
    acc=defaultdict(list)
    for rf,tf in zip(wp[:,0],wp[:,1]): acc[rf].append(tf)
    mp=np.full(Xr.shape[1],-1.0); last=0.0
    for rf in range(Xr.shape[1]):
        if acc[rf]: mp[rf]=np.mean(acc[rf])
    for k in range(len(mp)):
        if mp[k]<0: mp[k]=last
        else: last=mp[k]
    def t(s): f=min(max(int(round(s/HOP)),0),Xr.shape[1]-1); return mp[f]*HOP/SR
    out=[[round(min(t(s),t(e)),3),round(max(t(s),t(e)),3)] for (s,e) in bounds]
    for k in range(len(out)):
        if k>0 and out[k][0]<out[k-1][1]-0.001: out[k][0]=out[k-1][1]
        if out[k][1]<out[k][0]: out[k][1]=out[k][0]
        out[k]=[round(min(out[k][0],D),3),round(min(out[k][1],D),3)]
    return out,D

def main():
    sid=sys.argv[1]; adir=sys.argv[2] if len(sys.argv)>2 else "audio/"+sid
    story=json.load(open(sid+".json",encoding="utf-8"))
    out={}; bad=[]
    for i,s in enumerate(story["sentences"]):
        toks=WORD_RE.findall(s["t"])
        try: arr,_=align_sentence("%s/%d.mp3"%(adir,i),s["t"])
        except Exception as e: arr=[]; bad.append((i,str(e)))
        if len(arr)!=len(toks): bad.append((i,"len %d!=tok %d"%(len(arr),len(toks))))
        out[str(i)]=arr
        if i%12==0: print("aligned",i,"/",len(story["sentences"])); sys.stdout.flush()
    json.dump(out,open("%s/align.json"%adir,"w",encoding="utf-8"),ensure_ascii=False)
    print("DONE",len(out),"sentences,",sum(len(v) for v in out.values()),"timings; issues:",bad or "none")

if __name__=="__main__": main()

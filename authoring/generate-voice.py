"""Generate the portable Mandarin audio bank. Models are build tools, never runtime dependencies."""
from pathlib import Path
import json,hashlib,re,subprocess,time,sys,os
import numpy as np
import soundfile as sf
import onnxruntime as ort
from misaki import zh
from misaki.zh_frontend import ZH_MAP
from pypinyin.contrib.tone_convert import to_tone3
from pypinyin.style._utils import get_initials,get_finals
from kokoro_onnx import Kokoro
R=Path(sys.argv[1] if len(sys.argv)>1 else 'outputs/hanzi-reader/dist');M=Path(sys.argv[2] if len(sys.argv)>2 else 'work/hanzi-upgrade/models');A=R/'audio/kokoro';A.mkdir(parents=True,exist_ok=True)
s=(R/'practice-data.js').read_text();data=json.loads(s[s.index('{'):].rstrip(';\n'));book=json.loads((R/'dialogues.json').read_text());jobs={};mapping={}
g2p=zh.ZHG2P(version='1.1')
opts=ort.SessionOptions();opts.intra_op_num_threads=int(os.environ.get('HANZI_VOICE_THREADS','4'));opts.inter_op_num_threads=1
session=ort.InferenceSession(str(M/'kokoro-v1.1-zh.onnx'),sess_options=opts,providers=['CPUExecutionProvider'])
k=Kokoro.from_session(session,str(M/'voices-v1.1-zh.bin'),vocab_config=str(M/'config.json'))
def wordphones(pinyin):
 out=[]
 syllables=pinyin.replace('’',' ').replace("'",' ').split()
 tones=[to_tone3(x,neutral_tone_with_five=True).replace('v','ü') for x in syllables]
 for j,n in enumerate(tones):
  if syllables[j]=='r' and out:
   out[-1]=out[-1][:-1]+'R'+out[-1][-1];continue
  if n.endswith('3') and j+1<len(tones) and tones[j+1].endswith('3'):n=n[:-1]+'2'
  tone=n[-1] if n[-1:].isdigit() else '5';base=re.sub('[1-5]$','',n)
  initial=get_initials(base,strict=True);final=get_finals(base,strict=True).replace("ü","v")
  if final=='i' and initial in ['z','c','s']:final='ii'
  elif final=='i' and initial in ['zh','ch','sh','r']:final='iii'
  parts=[x for x in [initial,final,tone] if x];assert all(x in ZH_MAP for x in parts),(syllables[j],parts)
  out.append(''.join(ZH_MAP[x] for x in parts))
 return ''.join(out)
def add(text,phones=None):
 key=hashlib.sha256(('kokoro-v1.1-zh|zf_001|.92|'+text+'|'+str(phones)).encode()).hexdigest()[:16];rel='audio/kokoro/'+key+'.mp3';jobs[rel]=(text,phones);return rel
for w in data['words']:
 w['audio']=add(w['text'],wordphones(w['pinyin']));w['contextAudio']=add(w['context'])
for lesson in book['lessons']:
 for d in lesson['dialogues']:
  mapping[d['id']]=add(' '.join(d['lines']))
manifest={'engine':'Kokoro 1.1 Mandarin','voice':'zf_001','speed':.92,'source':'https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh','dialogues':mapping,'clips':[{ 'path':p,'text':t,'phonemes':ph}for p,(t,ph)in jobs.items()]}
manifest_path=R.parent/'authoring/voice-manifest.json';manifest_path.parent.mkdir(parents=True,exist_ok=True);manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
start=time.time();generated=0;limit=int(os.environ.get('HANZI_VOICE_BATCH','10000'))
for i,(rel,(text,phones)) in enumerate(jobs.items(),1):
 if i<int(os.environ.get('HANZI_VOICE_START','1')):continue
 dest=R/rel
 if not dest.exists() or dest.stat().st_size<500:
  phones=phones or g2p(text)[0];assert '❓' not in phones,(text,phones)
  samples,sr=k.create(phones,voice='zf_001',speed=.92,is_phonemes=True)
  assert len(samples)>sr*.15 and np.isfinite(samples).all() and np.max(np.abs(samples))>.001,text
  temp=Path('/tmp/hanzi-voice-render-'+str(os.getpid())+'.wav');sf.write(temp,samples,sr)
  generated+=1
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(temp),'-af','apad=pad_dur=0.25','-codec:a','libmp3lame','-b:a','64k',str(dest)],check=True)
 if i%25==0:print(f'{i}/{len(jobs)} clips; {time.time()-start:.0f}s',flush=True)
 if generated>=limit:break
if any(not (R/p).exists() or (R/p).stat().st_size<500 for p in jobs):
 print('BATCH SAVED; rerun to continue.',flush=True);raise SystemExit(0)
# Switch only when every recording is ready.
(R/'practice-data.js').write_text('window.PRACTICE_DATA='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
(R/'voice-data.js').write_text('window.HANZI_VOICE='+json.dumps({'name':'Kokoro Mandarin · zf_001','dialogues':mapping},ensure_ascii=False)+';\n')
print('DONE',len(jobs),'clips',sum((R/p).stat().st_size for p in jobs),'bytes',flush=True)

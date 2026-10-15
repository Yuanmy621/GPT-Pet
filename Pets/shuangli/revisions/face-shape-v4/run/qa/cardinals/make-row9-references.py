from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run')
# Reference-only collages from unmodified actual input pixels; no generated art.
canon=Image.open(R/'decoded/look-cardinals.png').convert('RGB')
slot=canon.width//4
out=Image.new('RGB',(1600,460),(240,242,248));d=ImageDraw.Draw(out)
for i,title in enumerate(['APPROVED UP','APPROVED RIGHT: BOTH EYES','APPROVED DOWN','APPROVED LEFT: BOTH EYES']):
    head=canon.crop((i*slot+95,5,i*slot+slot-90,300));head.thumbnail((390,405),Image.Resampling.LANCZOS)
    out.paste(head,(i*400+(400-head.width)//2,42));d.text((i*400+8,12),title,fill=(15,15,30))
out.save(R/'references/approved-cardinal-faces-highres.png')
body=Image.new('RGB',(1600,1250),'white');d=ImageDraw.Draw(body)
d.text((12,12),'BODY IDENTITY ONLY. Current atlas faces are defective: DO NOT COPY SIDE FACES.',fill=(25,25,25))
atlas=Image.open(R.parent/'inputs/current-spritesheet.png').convert('RGBA');atlas.thumbnail((760,1140),Image.Resampling.LANCZOS)
body.paste(atlas,(8,55),atlas)
d.text((790,12),'Original character identity board',fill=(25,25,25))
original=Image.open(R/'references/reference-02.png').convert('RGB');original.thumbnail((800,1140),Image.Resampling.LANCZOS)
body.paste(original,(790,55))
body.save(R/'references/row9-body-identity-board.png')
report={'operation':'Reference-only image crop/collage; no visual redraw or face alterations.','sources':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [R/'decoded/look-cardinals.png',R.parent/'inputs/current-spritesheet.png',R/'references/reference-02.png']],'outputs':['references/approved-cardinal-faces-highres.png','references/row9-body-identity-board.png']}
(R/'qa/cardinals/row9-reference-boards.json').write_text(json.dumps(report,indent=2)+'\n')

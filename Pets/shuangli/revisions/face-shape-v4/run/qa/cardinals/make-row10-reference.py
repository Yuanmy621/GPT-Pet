from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run');src=R/'decoded/look-cardinals.png';im=Image.open(src).convert('RGB');slot=im.width//4
out=Image.new('RGB',(1400,500),(238,240,245));d=ImageDraw.Draw(out)
for ix,col,title in [(3,0,'APPROVED LEFT - PRIMARY HEAD'),(2,1,'DOWN'),(0,2,'UP')]:
    p=im.crop((ix*slot+90,5,ix*slot+slot-85,310));p.thumbnail((450,410),Image.Resampling.LANCZOS);out.paste(p,(col*465+(465-p.width)//2,42));d.text((col*465+8,12),title,fill=(20,20,30))
out.save(R/'references/row10-left-down-up-faces.png')
guide=Image.new('RGB',(1900,828),(245,245,245));d=ImageDraw.Draw(guide)
for i in range(8):
    x=round((i+.5)*1900/8);d.rectangle((x-100,250,x+100,570),outline=(35,105,220),width=2);d.line((x,250,x,570),fill=(195,195,195))
guide.save(R/'references/layout-guides/look-row-10-spacious.png')
(R/'qa/cardinals/row10-reference-provenance.json').write_text(json.dumps({'face_board_source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'operation':'Unmodified head crops only; primary left with down/up anchors, excluding right head.','guide':{'size':[1900,828],'slot_centers':'(index+0.5)*1900/8','zone':[200,320],'common_baseline':570}},indent=2)+'\n')

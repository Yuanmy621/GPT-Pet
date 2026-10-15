from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run')
out=Image.new('RGB',(1600,950),'white');d=ImageDraw.Draw(out)
d.text((8,10),'Uploaded pet: FRONT IDLE identity only. No old side faces.',fill=(25,25,25))
atlas=Image.open(R.parent/'inputs/current-spritesheet.png').convert('RGBA')
front=atlas.crop((0,0,192,208));front.thumbnail((560,820),Image.Resampling.LANCZOS)
front=front.resize((560,607),Image.Resampling.LANCZOS);out.paste(front,(20,80),front)
d.text((620,10),'Original dragon-girl character identity',fill=(25,25,25))
original=Image.open(R/'references/reference-02.png').convert('RGB');original.thumbnail((970,840),Image.Resampling.LANCZOS);out.paste(original,(620,80))
out.save(R/'references/row9-front-only-identity-board.png')
guide=Image.new('RGB',(2172,724),(245,245,245));d=ImageDraw.Draw(guide)
for i in range(8):
    x=round((i+.5)*2172/8)
    d.rectangle((x-112,200,x+112,520),outline=(35,105,220),width=2)
    d.line((x,200,x,520),fill=(195,195,195),width=1)
guide.save(R/'references/layout-guides/look-row-9-spacious.png')
report={'description':'Reference-only body collage from exact uploaded atlas frontal idle cell and original reference board; invisible guide with 8 small safe zones, not visual art.','sources':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [R.parent/'inputs/current-spritesheet.png',R/'references/reference-02.png']],'body_atlas_crop':[0,0,192,208],'guide':{'size':[2172,724],'safe_zone_height':320,'safe_zone_width':224,'figure_scale':'shared across all 8'}}
(R/'qa/cardinals/row9-spacious-blueprint.json').write_text(json.dumps(report,indent=2)+'\n')

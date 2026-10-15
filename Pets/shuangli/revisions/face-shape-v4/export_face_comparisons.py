"""Render face-repair evidence from the exact before/after encoded atlases."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('pet_previews', ROOT.parents[1] / 'qa/render_final_previews.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
before_path = ROOT / 'inputs/current-spritesheet.png'
after_path = ROOT / 'run/final/spritesheet-extended.png'
before, after = [Image.open(p).convert('RGBA') for p in (before_path, after_path)]
out = ROOT / 'run/previews/comparisons'
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default(size=15)

def cell(atlas, row, column):
    return atlas.crop((column*192, row*208, (column+1)*192, (row+1)*208))

def compare(row, column, title, *, zoom=False):
    panel = Image.new('RGB', (400, 436 if zoom else 244), '#ececf5')
    draw = ImageDraw.Draw(panel)
    for x, atlas, label in [(4,before,'Before'),(204,after,'After')]:
        sprite = cell(atlas,row,column)
        panel.paste(sprite,(x,30),sprite)
        draw.text((x+8,8),label+' / '+title,font=font,fill='#38354e')
        if zoom:
            box = (72,0,168,88) if row==1 else (16,0,112,88) if row==2 else (48,0,144,88)
            head = sprite.crop(box).resize((192,176),Image.Resampling.NEAREST)
            panel.paste(head,(x,252),head)
    return panel

for row,name in [(1,'running-right'),(2,'running-left')]:
    helper.save_gif([compare(row,i,name) for i in range(8)],helper.ROW_DURATIONS[name],out/(name+'-before-after.gif'))
    helper.save_gif([compare(row,i,name,zoom=True) for i in range(8)],helper.ROW_DURATIONS[name],out/(name+'-faces.gif'))
helper.save_gif([compare(9+i//8,i%8,'look',zoom=True) for i in range(16)], [180]*16,out/'look-faces-before-after.gif')

proof = Image.new('RGB',(800,872),'#ececf5')
for i,(row,col,title) in enumerate([(9,4,'look right'),(10,4,'look left'),(1,0,'move right'),(2,0,'move left')]):
    proof.paste(compare(row,col,title,zoom=True),((i%2)*400,(i//2)*436))
proof.save(out/'face-shape-before-after.png')
(out/'provenance.json').write_text(json.dumps({
    'before_sha256':hashlib.sha256(before_path.read_bytes()).hexdigest(),
    'after_sha256':hashlib.sha256(after_path.read_bytes()).hexdigest(),
    'operation':'Encoded-cell crops and labeled comparison panels only. Enlarged head crops use nearest-neighbor pixels; no drawn or warped face.',
    'timings':'Existing Pets contract timings on both sides',
},indent=2)+'\n')
print(out)

"""Render before/after QA from encoded atlases, without changing artwork."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
RUN = ROOT / 'run'
spec = importlib.util.spec_from_file_location('preview_helper', ROOT.parents[1] / 'qa/render_final_previews.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
before_path = ROOT / 'inputs/current-spritesheet.png'
after_path = RUN / 'final/spritesheet-extended.png'
before = Image.open(before_path).convert('RGBA')
after = Image.open(after_path).convert('RGBA')
font = ImageFont.load_default(size=15)
out = RUN / 'previews/comparisons'
out.mkdir(parents=True, exist_ok=True)

def cell(atlas, row, column):
    return atlas.crop((column*192, row*208, (column+1)*192, (row+1)*208))

for state, row in [('idle', 0), ('running', 7), ('waiting', 6), ('review', 8)]:
    frames = []
    for column in range(len(helper.ROW_DURATIONS[state])):
        panel = Image.new('RGB', (400, 244), '#ececf5')
        draw = ImageDraw.Draw(panel)
        for x, atlas, title in [(4, before, 'Before'), (204, after, 'After')]:
            sprite = cell(atlas, row, column)
            panel.paste(sprite, (x, 32), sprite)
            draw.text((x+8, 9), title+' / '+state, font=font, fill='#38354e')
        frames.append(panel)
    helper.save_gif(frames, helper.ROW_DURATIONS[state], out / (state+'-before-after.gif'))

proof = Image.new('RGB', (768, 708))
draw = ImageDraw.Draw(proof)
for y, background in enumerate(['#ececf5', '#ffffff', '#292633']):
    draw.rectangle((0,y*236,768,(y+1)*236), fill=background)
    for x, (atlas, row, title) in enumerate([(before,0,'Before idle'),(after,0,'After idle'),(before,7,'Before work'),(after,7,'After work')]):
        sprite = cell(atlas, row, 0)
        proof.paste(sprite, (x*192, y*236+28), sprite)
        draw.text((x*192+8, y*236+6), title, font=font, fill='#ffffff' if y==2 else '#38354e')
proof.save(out / 'native-backgrounds.png')
proof.resize((576,531), Image.Resampling.LANCZOS).save(out / '75-percent-backgrounds.png')
(out / 'provenance.json').write_text(json.dumps({
    'before_sha256':hashlib.sha256(before_path.read_bytes()).hexdigest(),
    'after_sha256':hashlib.sha256(after_path.read_bytes()).hexdigest(),
    'source':'Exact encoded atlases; native cell crops, composited backgrounds and labels only',
    'animation_timing':'Same existing contract timings on both sides; no client FPS claim',
}, indent=2)+'\n')
print(out)

"""Run the bundled Pets assembly/validation tools on a fresh repair candidate.

Run with the Pillow-enabled Python runtime. Visual, blind, and MCP acceptance
remain separate gates; successful execution of this helper does not upload.
"""
from pathlib import Path
import hashlib
import json
import os
import statistics
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
RUN = ROOT / 'run'
SCRIPTS = Path.home() / '.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/scripts'
sys.path.insert(0, str(SCRIPTS))
import assemble_extended_atlas as bundled

def invoke(script, *args):
    result = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str,args)], capture_output=True, text=True)
    print(script, result.returncode, flush=True)
    if result.returncode:
        print(result.stdout[-3000:], result.stderr[-1500:])
        raise SystemExit(result.returncode)

metrics = {}
for row in (9,10):
    cells = bundled.extract_row_strip_cells(RUN / f'decoded/look-row-{row}.png', (0,255,0), 96)
    values = [{'height':c.height, 'width':c.width, 'area':sum(c.getchannel('A').histogram()[1:])} for c in cells]
    assert len(values)==8
    assert min(v['area'] for v in values) > .4 * max(v['area'] for v in values), 'Noise components selected instead of real pose groups'
    assert min(v['height'] for v in values) > .75 * max(v['height'] for v in values), 'Uneven or merged pose geometry'
    metrics[str(row)] = values
h9 = [v['height'] for v in metrics['9']]
h10 = [v['height'] for v in metrics['10']]
factor = min(statistics.median(h9)/statistics.median(h10), max(h9)/max(h10))
source10 = RUN / 'decoded/look-row-10.png'
im = Image.open(source10)
size = tuple(round(v*factor) for v in im.size)
im.resize(size, Image.Resampling.LANCZOS).save(RUN / 'decoded/look-row-10-density-normalized.png')
(RUN/'qa/source-density-normalization.json').write_text(json.dumps({
    'operation':'Uniform whole-source density adjustment before shared row9 look registration. No per-cell transforms or face edits.',
    'source_sha256':hashlib.sha256(source10.read_bytes()).hexdigest(),
    'selected_group_metrics':metrics, 'scale':factor,
    'source_size':im.size, 'normalized_size':size,
},indent=2)+'\n')

invoke('assemble_extended_atlas.py','--base-atlas',RUN/'final/spritesheet-standard.png',
       '--registered-row-9',RUN/'decoded/look-row-9-registered.png',
       '--row-9-registration',RUN/'qa/look-row-9-registration.json',
       '--look-row-10',RUN/'decoded/look-row-10-density-normalized.png',
       '--output',RUN/'final/spritesheet-extended-raw.png',
       '--manifest-output',RUN/'atlas-manifest.json','--chroma-key','#00FF00')
# Always start from the freshly assembled RAW candidate; never despill a cleaned sheet.
atlas = RUN/'final/spritesheet-extended.png'
invoke('despill_chroma_edges.py',RUN/'final/spritesheet-extended-raw.png',
       '--output',atlas,'--chroma-key','#00FF00','--json-out',RUN/'qa/chroma-despill-extended.json')
invoke('validate_atlas.py',atlas,'--require-v2','--json-out',RUN/'final/validation-extended.json')
invoke('make_contact_sheet.py',atlas,'--output',RUN/'qa/contact-sheet-final.png','--scale','1')
invoke('make_direction_qa_sheet.py',atlas,'--output',RUN/'qa/direction-sheet.png')
invoke('measure_direction_continuity.py',atlas,'--json-out',RUN/'qa/look-continuity.json')
invoke('make_direction_blind_qa_sheet.py',atlas,'--output',RUN/'qa/direction-blind.png',
       '--answer-key',RUN/'qa/direction-blind-answer-key.json')
preview = ROOT.parents[1]/'qa/render_final_previews.py'
subprocess.run([sys.executable,str(preview),str(atlas),'--output-dir',str(RUN/'previews')],
               env=dict(os.environ,PYTHONPATH=str(ROOT.parents[3]/'.pet-tools')),check=True,capture_output=True)
invoke('render_animation_previews.py','--frames-root',RUN/'previews/final-frames','--output-dir',RUN/'previews/bundled')
invoke('inspect_frames.py','--frames-root',RUN/'previews/final-frames','--json-out',RUN/'qa/final-frame-review.json')
blind = Image.open(RUN/'qa/direction-blind.png')
blind.crop((0,0,384,1652)).save(RUN/'qa/blind-horizontal.png')
blind.crop((0,1652,384,3304)).save(RUN/'qa/blind-vertical.png')

final = Image.open(atlas).convert('RGBA')
before = Image.open(ROOT/'inputs/current-spritesheet.png').convert('RGBA')
states = ['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
preserved = {states[i]:before.crop((0,i*208,1536,(i+1)*208)).tobytes()==final.crop((0,i*208,1536,(i+1)*208)).tobytes() for i in (0,3,4,5,6,7,8)}
assert all(preserved.values()), 'An unaffected state changed after encoding'
(RUN/'qa/preserved-states-final.json').write_text(json.dumps({'ok':True,'frames':41,'pixel_identical_rows':preserved},indent=2)+'\n')
proof = Image.new('RGB',(576,472),'#ececf5')
draw = ImageDraw.Draw(proof)
font = ImageFont.load_default(size=14)
for i,(row,col,label) in enumerate([(10,7,'337.5'),(9,0,'000 up'),(0,0,'neutral'),(9,7,'157.5'),(10,0,'180 down'),(0,0,'neutral')]):
    x,y = i%3*192,i//3*236
    c = final.crop((col*192,row*208,(col+1)*192,(row+1)*208))
    proof.paste(c,(x,y+28),c)
    draw.text((x+8,y+5),label,font=font,fill='#38354e')
proof.save(RUN/'qa/look-boundaries-native.png')
subprocess.run([sys.executable,str(ROOT/'export_face_comparisons.py')],check=True,capture_output=True)
print(json.dumps({'candidate_sha256':hashlib.sha256(atlas.read_bytes()).hexdigest(), 'bytes':atlas.stat().st_size,'preserved_frames':41}),flush=True)

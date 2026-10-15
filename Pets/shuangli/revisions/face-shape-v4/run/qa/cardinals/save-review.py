from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run')
ref=[R/'references/canonical-base.png',R.parent/'inputs/current-spritesheet.png',R/'references/reference-02.png',R/'references/layout-guides/look-cardinals.png']
canvas=Image.new('RGB',(768,236),(238,240,245));d=ImageDraw.Draw(canvas)
for i,lab in enumerate(['000 UP','090 SCREEN-RIGHT','180 DOWN','270 SCREEN-LEFT']):
    cell=Image.open(R/'decoded/cardinal-anchors'/f'{lab[:3]}.png').convert('RGBA')
    canvas.paste(cell,(192*i,28),cell);d.text((192*i+8,7),lab,fill=(30,30,40))
canvas.save(R/'qa/cardinal-native-panel.png')
faces=Image.new('RGB',(768,220),(238,240,245));d=ImageDraw.Draw(faces)
for i,lab in enumerate(['000 UP','090 SCREEN-RIGHT','180 DOWN','270 SCREEN-LEFT']):
    cell=Image.open(R/'decoded/cardinal-anchors'/f'{lab[:3]}.png').convert('RGBA')
    face=cell.crop((52,0,134,78)).resize((164,156),Image.Resampling.NEAREST)
    faces.paste(face,(i*192+14,32),face);d.text((i*192+8,7),lab,fill=(30,30,40))
faces.save(R/'qa/cardinal-face-proof.png')
report={
 'ok':True,'reviewer':'face_v4_cardinals visual worker','source':str(R/'decoded/look-cardinals.png'),
 'source_sha256':hashlib.sha256((R/'decoded/look-cardinals.png').read_bytes()).hexdigest(),
 'method':'Visual review of generated source plus exact official 192x208 anchors at native size',
 'observed':[
 {'direction':'000','verdict':'pass','evidence':'Broad frontal face, both eyes visibly lifted, chin raised and tiny nose angled upward; short compact rounded jaw remains under mouth.'},
 {'direction':'090','verdict':'pass','evidence':'Physical head yaw toward screen-right, shifted nose/mouth and rightmost face surface, both purple eyes visible with far eye foreshortened; compact curved cheek avoids previous full-profile flat jaw ledge. Rosette partly occluded on far side.'},
 {'direction':'180','verdict':'pass','evidence':'Head pitched downward, chin tucked toward chest, lower visible eye line and lowered eyelids; both eyes and rounded face remain visible.'},
 {'direction':'270','verdict':'pass','evidence':'Physical head yaw screen-left, both eyes readable and far eye narrowed, small nose and short curved cheek/chin; anatomical left temple rosette remains near/visible on screen-right head edge.'}],
 'identity':{'verdict':'pass','evidence':'White layered hair, two ivory horns, pointed ears, purple eyes, white/lavender full dress, waist-clasped hands, bat wings, attached fluffy tail, and left-temple rosette preserved; body remains frontal.'},
 'source_geometry':{'initial':'Official extraction failed on equal slot edge checks because isolated complete silhouettes straddled assumed boundaries. No source pose was clipped or touching a neighboring pose.','repair':'Official component groups deterministically recentered into evenly padded slots, no resize/redraw. Actual official extraction rerun reports ok true, all source edge pixels zero.'},
 'warnings':['Native anchors retain source green fringe pending the parent full-atlas single despill pass. Do not apply isolated repeated despill to these references.','Final look strips must preserve these three-quarter two-eye faces and must pass parent final direction/continuity review.'],
 'prompt':str(R/'prompts/look-cardinals-effective.md'),
 'generation_mode':'built-in image_gen',
 'generated_original':'/Users/ymy/.codex/generated_images/01a13fc0-4db7-7bd1-b5b5-38fb8eb88a5e/exec-2c8450c8-7228-4702-bc1e-60b53b7618c4.png',
 'references':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in ref],
 'parent_final_acceptance_pending':True}
(R/'qa/cardinal-visual-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':report['ok'],'source_sha256':report['source_sha256'],'review':str(R/'qa/cardinal-visual-review.json')},indent=2))

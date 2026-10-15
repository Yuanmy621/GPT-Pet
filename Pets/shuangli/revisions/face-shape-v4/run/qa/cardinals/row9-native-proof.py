from PIL import Image,ImageDraw
from pathlib import Path
import sys,json
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run')
S=Path('/Users/ymy/.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/scripts')
sys.path.insert(0,str(S));import extract_strip_frames as e
raw=Image.open(R/'decoded/look-row-9.png').convert('RGBA');clean=e.remove_chroma_background(raw,(0,255,0),96)
groups=e.component_frame_groups(clean,8);assert groups and len(groups)==8
components=e.connected_components(clean)
rep={'main_component_count':len([c for c in components if c['area']>=max(c['area'] for c in components)*.2]),'groups':[{'bbox':e.component_bounds(g),'components':len(g),'area':sum(c['area'] for c in g)} for g in groups]}
(R/'qa/look-row-9-source-components.json').write_text(json.dumps(rep,indent=2)+'\n')
im=Image.open(R/'decoded/look-row-9-registered.png').convert('RGBA')
out=Image.new('RGB',(1536,236),(238,240,245));d=ImageDraw.Draw(out)
faces=Image.new('RGB',(1536,220),(238,240,245));fd=ImageDraw.Draw(faces)
labels=['000 UP','022.5 UP-RIGHT','045 UP-RIGHT','067.5 UP-RIGHT','090 RIGHT','112.5 DOWN-RIGHT','135 DOWN-RIGHT','157.5 DOWN-RIGHT']
for i,label in enumerate(labels):
    cell=im.crop((i*192,0,(i+1)*192,208));out.paste(cell,(i*192,28),cell);d.text((i*192+8,7),label,fill=(20,20,30))
    face=cell.crop((52,0,134,78)).resize((164,156),Image.Resampling.NEAREST)
    faces.paste(face,(i*192+14,32),face);fd.text((i*192+8,7),label,fill=(20,20,30))
out.save(R/'qa/look-row-9-native.png');faces.save(R/'qa/look-row-9-faces.png')
print(json.dumps(rep,indent=2))

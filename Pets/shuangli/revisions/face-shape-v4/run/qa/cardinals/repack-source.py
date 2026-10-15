from pathlib import Path
import sys,json,hashlib
from PIL import Image
S=Path('/Users/ymy/.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/scripts')
sys.path.insert(0,str(S))
import extract_strip_frames as e
R=Path('/Users/ymy/Project/GPT-Pet/Pets/shuangli/revisions/face-shape-v4/run')
src=R/'decoded/candidates/look-cardinals/attempt-1.png'
im=Image.open(src).convert('RGBA')
clean=e.remove_chroma_background(im,(0,255,0),96.0)
groups=e.component_frame_groups(clean,4)
assert groups and len(groups)==4
boxes=[e.component_bounds(g) for g in groups]
assert all(len([c for c in g if c['area']>10000])==1 for g in groups)
slot=max(b[2]-b[0] for b in boxes)+64
out=Image.new('RGB',(slot*4,im.height),(0,255,0))
placements=[]
for i,(g,b) in enumerate(zip(groups,boxes)):
    crop=e.component_group_image(clean,g,padding=0)
    x=i*slot+(slot-crop.width)//2
    out.paste(crop,(x,b[1]),crop)
    placements.append({'source_bbox':b,'target_xy':[x,b[1]],'scale':1.0,'main_component_area':max(c['area'] for c in g)})
dest=R/'decoded/look-cardinals.png'
out.save(dest)
report={'operation':'recenter complete disjoint source components into safely padded slots; no resizing or redrawing','source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'output':str(dest),'output_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'source_size':im.size,'output_size':out.size,'slot_width':slot,'chroma_key':'#00FF00','placements':placements}
(R/'qa/cardinals/source-spacing-normalization.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

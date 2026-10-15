# Failed row visual review

Selected attempt 2 passes local source and native-size review. Exactly eight complete, separated poses portray a brief gentle disappointment: the gaze lowers, eyelids close softly with a small frown and subtle shoulder softness, then the eyes and posture recover to a calm forward gaze. The sequence stays upright with hands gently joined in front. First and last poses match the approved idle mood and the wrap panel has no visible pop.

Native 192×208 panels preserve the approved idle face/head size, formal dress and hair template, viewer-right temple silver rosette, attached wings and fluffy tail. Full horns, shoes, skirt, tail and wing tips stay unclipped; the feet/skirt baseline remains stable. No tears, smoke, symbols, shadows, new props or loose effects appear.

The first attempt was rejected because neighboring wing tips touched and component extraction merged two pose pairs. Attempt 2 visibly repairs that source geometry with wider green gutters. Its real bundled `extract_strip_frames.py --method components` and `inspect_frames.py --require-components` run passes with zero errors and zero warnings. Metrics are diagnostic; acceptance also used the selected source, native panel, idle comparison and enlarged wrap panel.

Only already-keyed background pixels were normalized to exact #00FF00. Original generated source is preserved as `source-attempt-2.png`; no character pixels were redrawn. A narrow chroma fringe remains for the parent workflow’s final single despill pass. No shared manifest, atlas, upload or active-pet record was changed.

# Waving row visual review

Selected source: `decoded/waving.png`. Generated with the built-in image generator from the canonical base, original identity board, previous atlas, four-slot layout guide, and approved current idle strip. The exact effective prompt is saved beside this note.

The source contains exactly four complete separated full-body poses on solid green. Their sequence is low hand lifting near chest, open palm beside the shoulder/lower cheek, a gentle wrist variation at the same height, and hand lowered toward the waist. Only her anatomical right hand on viewer left waves; the other hand stays low. Each hand remains attached through a visible arm. No extra limbs, new props, wave marks, sparkles, shadows, text, clipping, or copied guide marks are visible.

The bundled component extraction and `inspect_frames.py --require-components` both returned `ok: true`; inspection reported no errors or warnings. All four native bounds are [25, 5, 166, 203], with one shared transform and stable baseline. Horns, pointed ears, lavender wings, long skirt, shoes and attached tail remain complete. The silver temple knot remains on anatomical left/viewer right. Face, hair, dress and body template remain stable within this row.

The native contact and idle comparison were inspected at 192x208 per pose. The lavender eyes and small open palm remain readable, and the face remains in the canonical family. This row has a 141 px wide silhouette compared with the idle row's approximately 123 px width, mainly from broader wing/tail spread; both have a 198 px visible height and the same bottom edge. The difference is recorded for the parent's final cross-state review, without per-frame resizing.

Pre-final native previews show chroma edge spill. This is an extraction/edge-cleanup matter for the parent's one final despill pass after assembly; no deterministic pet pixels were redrawn. `native-loop.gif`, `native-contact.png`, `native-idle-comparison.png`, and `native-evidence.json` are diagnostic evidence, not upload artifacts. No shared manifest, final atlas, upload, or selection was changed.

Generation source: `/Users/ymy/.codex/generated_images/01a13e21-e8dc-7ef1-8290-17e9d88fe183/exec-829c29b8-7526-4d30-9947-bee0c21e1793.png`.

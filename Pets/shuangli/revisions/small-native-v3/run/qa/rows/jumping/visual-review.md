# Native jumping visual review

Selected generated source: `decoded/jumping.png` (2169×725). Exactly five generated whole poses, produced with the built-in image generator and approved canonical + idle + original identity board + current atlas + five-slot layout references. The effective prompt is `effective-prompt.md`.

The bundled component extractor succeeded using `--method components`; `inspect_frames.py --require-components` returned `ok: true`, no errors, and no warnings. Frames are original bundled extraction results; no pet pixels were invented, moved or resized after extraction.

Actual native-cell bounds are saved in `native-motion-metrics.json`. First and last bottoms are both203, matching the approved idle bottom203. The successive bottom lifts are0,15,39,13,0px. Visible heights are142,159,159,167,142px because the girl crouches then tucks her knees, not because the character is scaled between frames. Literal head and face size remains visually coherent with idle in the six-cell side-by-side `native-contact.png`. The parent inspected this contact and accepted39px peak lift as an intentional playful jump despite the original nominal20–30px target.

The contact shows chronological anticipation/rest crouch, lift, airborne delighted peak, descent and matching landing crouch. Both horns, viewer-right temple rosette, attached wings, connected fluffy tail, sleeves, skirt and shoes remain present and unclipped. Air is visible below the peak; first and fifth crouch depth and footprint agree. No shadows, dust, motion marks, labels, or detached effects are visible. Face, dress and lavender-white palette follow the new canonical design.

`native-loop.gif` and `idle-jump-idle-diagnostic.gif` are diagnostic previews from the actual extracted cells. Contact-sheet inspection was performed; final encoded-atlas playback and idle transition acceptance remain with the parent. Source antialiasing has pre-final green spill, so the parent must run the one mandatory final edge-despill pass after assembly. No atlas, manifest, Library lifecycle or pet upload was changed by this worker.

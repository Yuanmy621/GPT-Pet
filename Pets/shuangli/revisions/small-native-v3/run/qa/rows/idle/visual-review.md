# Native idle visual review

Selected source: `decoded/idle.png`, generated with the built-in image generator as an identity-preserving edit of candidate 01. This is generated artwork, not repeated or procedurally animated final cells. Six repeated canonical figures were used only as an image-generation reference layout.

The bundled component extractor found exactly six connected whole poses; `inspect_frames.py --require-components` passed with no errors or warnings. Shared scaling produces visible bounds 122–123 px wide, 197–198 px high, with all bottom edges at 203 (exclusive). Horns, wings, tail and skirt are complete, with no neighbor contact or guide marks.

Native ordered-cell inspection: the same face, horn pair, temple knot and waist-clasped hands remain consistent. Eyelids soften gently near the middle then return, with quiet shoulder/hair variation. No full closed-eye blinks, abrupt gestures, walking, props or strong reactions. First and last maintain the resting pose; feet and skirt stay planted. Stronger canonical contours and larger readable face are retained.

Pre-final edge pixels contain green spill, so the parent must apply the one mandatory final despill after assembly. The native contact and GIF are diagnostic previews before that pass, not upload artifacts. Interframe MAE is saved as a diagnostic only: stronger contours and antialiasing affect it, and it is not treated as a smoothness score or proof of a performance improvement. Final encoded-atlas motion and state transitions still require parent review.

Artifacts: `native-contact.png`, `native-loop.gif`, `native-motion-metrics.json`, `review.json`, `frames/frames-manifest.json`, and `frames/idle/00.png` through `05.png`. Rejected earlier source remains `decoded/idle-candidate-01.png` with its QA in `qa/rows/idle-candidate-01/`.

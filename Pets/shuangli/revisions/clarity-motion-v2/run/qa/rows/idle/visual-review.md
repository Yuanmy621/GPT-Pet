# Idle visual review — selected locked-cel edit

Reviewed all six extracted PNGs at exact native 192 × 208 size and compared with inputs/idle-00.png.

## Generation and provenance

- Generated with built-in imagegen, using all five manifest input references. Selected source: decoded/idle.png. Effective prompt: prompts/rows/idle-effective-locked-cel.md.
- Attempt 01 touched neighboring wing tips and failed extraction; preserved as decoded/idle-attempt-01.png.
- Attempt 02 separated poses and passed structure, but continuity metrics showed more repaint flicker than the original; preserved as decoded/idle-attempt-02.png and rejected.
- Strategy changed to imagegen editing a deterministic six-copy layout guide made only from approved canonical pixels. Original blank guide preserved at references/layout-guides/idle-original.png; copied-pixel reference at idle-locked-cel.png and idle.png. The final source remains imagegen output, not the deterministic reference.

## Selected visual assessment

- Bundled inspect_frames.py passes: six complete nonempty poses, shared-scale connected-component extraction, zero clipping, no warnings.
- Identity/proportions pass: same horns, silver hair, viewer-right rosette, purple eyes, lavender wings, attached fluffy tail and long white/lavender dress. The soft fine anime contour remains. The approved clearer canonical iris/lashes read at native size.
- Baseline and scale stable: every extracted bbox is exactly [27,5,165,203]. Hands stay clasped at waist. Head position, horn tips, body/dress folds, hair mass, wings and tail are essentially fixed with only small redraw variation.
- Blink reads open → partly closed → closed → partly open → open → open. It is calm with no gesture switching or whole head change.
- First/last are visibly close. Native whole RGB mean absolute difference across transitions is now 2.286–4.070 versus original 2.577–7.176. Wrap 5→0 is 3.332 versus original 7.059, roughly 53% smaller. Body-region wrap MAE is 5.145 versus 8.351, roughly 38% smaller. These are repaint/continuity metrics, not a measurement of application frame rate.
- Source reduced-size silhouette width is 138 px compared with original 123 px; both height 198 px. This follows the approved clearer canonical wing spread. Parent should check cross-state transitions after assembling preserved other rows.
- Remaining deterministic issue: visible green edge spill on extracted frames. Parent must perform the required one-time despill after final atlas assembly. These frames have deliberately not been despilled.
- Native preview: qa/rows/idle/native-loop.gif. Timing is preview-only, no runtime timing is changed by this source row.

## Artifacts

- decoded/idle.png
- qa/rows/idle/frames/idle/00.png through 05.png
- qa/rows/idle/frames/frames-manifest.json
- qa/rows/idle/review.json
- qa/rows/idle/continuity-metrics.json
- qa/rows/idle/native-loop.gif

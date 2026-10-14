# Review row visual QA

Selected source: `decoded/review.png`, generated with the built-in imagegen tool. First revision is preserved as `decoded/review-rejected-touching.png` because several neighboring wing tips touched and merged into one component.

Selected revision has six separate complete planted front-facing poses. Compared source and all six native extracted 192×208 frames against approved idle frame 00: silver-white hair, large chibi head and short torso, lavender eyes, ivory horns, viewer-right knot rosette, lilac membrane wings, attached curled fluffy tail, white/lilac dress and silver ornaments remain consistent. Baseline and scale are stable. Horns, wing tips and dress are unclipped. No new props or detached effects.

Review action is readable through narrowed inspecting eyes, a slight left scan, a right head tilt, careful blink/chin dip, pleased confirming nod, and attentive return. It is distinct from active thinking/work because hands remain low at the waist and the expression resolves into approval of inspected work.

Bundled `extract_strip_frames.py --states review --method auto` selected connected components and succeeded. Bundled `inspect_frames.py --states review --require-components` returned `ok: true`, no errors, no warnings.

Green edge fringe is visible before final atlas despill; leave the workflow's single prescribed final cleanup pass to the parent.

# Waiting row visual review, repaired revision

Previous source is preserved as decoded/waiting-v1.png; previous deterministic review is review-v1.json. Selected source is decoded/waiting.png. Built-in imagegen used idle.png as the primary exact proportions reference, canonical-base.png as secondary identity/style, identity-board.png for the original identity details, and layout-guides/waiting.png for invisible slot count.

All six complete extracted poses were inspected at native 192x208 beside idle frame 00. The larger chibi head and compact torso now match idle; the silhouette is 122 px wide rather than the previous 107 px, close to idle's 123 px. Every frame uses bbox [35,5,157,203] with stable foot/hem baseline. Horns, hair, wings, viewer-right rosette, lavender eyes, white/lilac dress and attached tail remain consistent and complete.

State is a patient needs-input request: hands clasp at upper chest, lift slightly under the chin, open into a compact palms-up gesture, eyes briefly close hopefully, then hands re-clasp. It differs from idle hands lowered at the waist, waving, and focused thinking. Feet stay planted; no new props or detached effects.

Bundled component extraction and frame inspection both passed with exactly six frames, zero edge pixels, no errors and no warnings. Small chroma fringes are reserved for the single required final atlas despill pass.

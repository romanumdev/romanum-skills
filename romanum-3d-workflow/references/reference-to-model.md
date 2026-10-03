# Coherent references and visual checks

Use this guide when an object's depth, unseen surfaces or multiple references could change the model. Keep simple, fully specified objects simple.

## Establish the reference set

Choose views for the unresolved shape rather than a fixed count of images. Front/back/side/three-quarter is a useful set for an asymmetric machine or character; a top view or opposite side may reveal a missing feature. A plain token with specified diameter, thickness and back needs no new four-view generation.

Keep a compact record alongside the working file:

| Record | Purpose |
| --- | --- |
| Reference file/version, view label and approval/source role | Identify which design governs the model |
| Dimensions or ratios, major landmarks and feature counts | Keep the same proportions and structure across views |
| Left/right orientation, confirmed symmetry and asymmetry | Avoid mirrored or invented features |
| Materials, colour regions and finish | Preserve the object's design when changing lighting/view |
| Unseen areas and unresolved conflicts | Make uncertainty explicit before it becomes geometry |

When another view is needed and generation is authorised, supply the selected object references and these invariants. Ask for a camera change, not a redesign. Label the output as a proposed view and inspect it before adding it to the approved set. An attractive new back view is not proof that the original has those details. If generation is unavailable, provide a reference-based brief and keep the missing coverage pending.

## Reconcile before detail

Compare corresponding landmarks at consistent scale. Account for perspective, pose and occlusion before deciding that differing apparent widths or feature counts indicate a design conflict. Record whether a side is the object's left or right; image-left is not a sufficient object orientation.

For a real conflict, use the approved reference or explicit design brief as the authority. Do not silently let the newest image overrule it. Correct the drifting view where authorised, or seek a decision if neither source settles a material feature. Work on unaffected geometry while that feature remains pending; do not combine one front with an unrelated back.

For an unseen back, distinguish observed detail, supported inference and an open design choice. Supported symmetry or a specified plain surface can resolve it. Otherwise omit arbitrary detail and use a reversible plain blockout, clearly labelled. If the user delegates original design, choose and record a coherent solution rather than repeatedly asking for every minor detail. That new design still needs consistent views and model checks.

## Compare blockout and final renders

At blockout, prioritise overall height/width/depth, silhouette and major landmarks. Resolve proportion errors before detailed bevels, ornaments or texture work make changes costly.

For each relevant view, retain the reference path, camera/view, actual render path, observed mismatches and any unresolved design areas. Match the reference's camera type/angle, pose, framing and scale as closely as practical; do not compare a perspective beauty shot with an orthographic silhouette as if they were equivalent.

Open the rendered images. Compare silhouette and proportions first, then feature placement/count, handedness and material regions/finish. Use simple lighting that exposes geometry and material boundaries; add the intended presentation view when composition is in scope. Do not hide a missing feature behind a favourable crop or dramatic lighting. Inspect the back and opposite side when those references carry design information.

Classify a discrepancy as a camera mismatch, a model/material error or a genuinely unresolved reference decision. Correct the responsible part and re-render the affected views. Before delivery, inspect the final set together to catch changes that fixed one view while breaking another. Record specific pending checks when render execution or image inspection is unavailable; a file list or render command's success is not a visual review.

# Concept to reusable assets

## 1. Generate and select the concept

Use imagegen to establish the full composition first. Supply the relevant style references and, when available, a current game screenshot. Specify the player's immediate task, required controls, target device, label hierarchy and gameplay area to preserve. A still concept describes visual states; it cannot prove animation, sound or interaction.

Include the concept and the requested extracted parts in one combined prompt, with at most eight output images total. One concept leaves room for seven assets; two concepts leave room for six. If the current model cannot generate images, explicitly ask the user to do so and supply [the combined generation prompt](imagegen-handoff.md). The concept-first sequence can happen within that one request to an image-generation assistant.

Review the render at its intended display size. Record the selected file and any approved changes. If a complete concept is already supplied and selected, use it directly. Do not begin unrelated visual exploration merely because the workflow contains a concept stage.

## 2. Extract with imagegen

Use the selected concept as the visual source for every extracted part, whether it was generated earlier in the same request or supplied as an attachment. Ask imagegen to isolate the listed components while preserving their design. If multiple input images are needed, label their roles explicitly.

Add a shared extraction instruction to the concept prompt, followed by a compact list of the required output files. For example:

> After creating the concept, use that actual image to extract each listed component as its own PNG. Preserve the shapes, colours, borders, highlights and shadows. Remove labels, changing values and surrounding UI; keep enough transparent padding for each component's shadow. Do not redesign the pieces or combine them into a sheet. Return the concept and all listed assets together.

List each needed icon, frame, pointer, texture or effect by filename and a short description; no separate prompt is needed per asset. Generate one useful piece per file. Use another imagegen pass if an extracted asset contains a baked label, missing border, opaque background, checkerboard pixels or unintended redesign. Do not replace this stage with a programmatic crop of the mockup. Filesystem tools may copy, inspect and package outputs; they do not fulfil visual extraction.

When more than eight images are needed, split the output list into batches of at most eight. The first batch includes the needed concepts; later batches attach the selected concept and generate remaining assets without regenerating it. Reference attachments do not consume output slots. A tool with a lower actual output limit may need smaller operations, but that does not change the default combined user-facing brief.

Typical boundaries:

| Extracted art | Kept live in the interface |
| --- | --- |
| Button base with border, lip and highlight | Label, price, interaction and state binding |
| Panel shell and optional separate tileable pattern | Layout, scrolling, item rows and content |
| Item/resource icon | Quantity, currency, damage or XP value |
| Progress-bar shell and fill art | Actual fill amount and progress label |
| Pointer, burst, shine or glow | Target position, timing, opacity and motion |

Use one coherent reference for a family of assets. When extracting a pressed variant, preserve dimensions and alignment so the hit target does not jump. A simple native press movement can also use the same base; do not generate another image for every possible numeric value or text state.

## 3. Inspect and record

View the actual outputs, including their alpha channel over both light and dark backgrounds. Compare border thickness, hue, highlights and shadow direction with the selected concept. Keep padding consistent. Check that no part of the control is cut off and that a supposedly seamless tile actually repeats cleanly. Imagegen extraction may drift; the comparison is necessary.

Keep a small asset manifest alongside the delivered files. Record:

- Selected concept path/version and source-reference roles.
- Stable asset key, local file, pixel dimensions and transparency status.
- Intended native component, state, anchor/parent and sizing behaviour.
- Measured safe inset or slice region, where applicable; do not guess coordinates.
- Live text/value binding separately from artwork.
- Upload status and real Roblox asset ID only after a successful authorised upload.

Use stable names such as `button-primary-base.png`, `panel-shop-shell.png`, `pattern-studs-tile.png` and `pointer-hand.png`. Retain the concept and originals so a future session can reopen them after compaction. Deliver the folder, not loose files with missing dependencies.

## 4. Assemble and verify

Use native Roblox controls and layout to make the art functional. Borders and corners can use [9-slice scaling](https://create.roblox.com/docs/ui/9-slice): set the image's ScaleType to Slice and determine SliceCenter from the actual source. Put a repeating pattern on a separate layer when stretching the centre would distort it. Do not nine-slice an entire HUD or a labelled button screenshot.

Keep text live for localisation and changing values. Allow for [ScreenGui screen insets](https://create.roblox.com/docs/reference/engine/classes/ScreenGui#ScreenInsets), touch controls and controller focus. A decorative ImageLabel cannot replace an accessible interactive control. Check z-order, modal input, target hit areas and longer labels in Studio.

Compare implementation captures with the concept at phone and desktop sizes: composition, legibility, texture scale, button depth and spacing should survive assembly. Also try presses, disabled states, rapid value changes and menu transitions. Report concept creation, asset extraction, upload, implementation and testing separately; completion of one stage does not prove the others.

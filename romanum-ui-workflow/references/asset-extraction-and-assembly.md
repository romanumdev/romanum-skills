# Concept to reusable assets

## 1. Generate and select the concept

Use imagegen to establish the full composition first. Supply the relevant style references and, when available, a current game screenshot. Specify the player's immediate task, required controls, target device, label hierarchy and gameplay area to preserve. A still concept describes visual states; it cannot prove animation, sound or interaction.

For a stud-style concept, supply the real texture and reserve its separate native layer. Do not ask imagegen to invent or redraw studs. If it cannot show the supplied texture faithfully, use a flat surface in the concept and inspect the actual texture during native assembly.

Include the concept and the requested extracted parts in one combined prompt, with at most eight output images total. One concept leaves room for seven assets; two concepts leave room for six. If the current model cannot generate images, explicitly ask the user to do so and supply [the combined generation prompt](imagegen-handoff.md). The concept-first sequence can happen within that one request to an image-generation assistant.

Review the render at its intended display size. Record the selected file and any approved changes. If a complete concept is already supplied and selected, use it directly. Do not begin unrelated visual exploration merely because the workflow contains a concept stage.

## 2. Extract with imagegen

Before choosing reusable files or output batches, break the selected concept into an asset map. Separate panel/button frames, backgrounds, icons, decorative effects and visually different pack/tier variants from editable text and values. For each part, record its concept location, defining appearance, intended display size and matching source or missing output. Similar style alone does not make an asset a match.

For an approved diamond shop showing a small cluster, a medium pile and a large heap, list the three pile compositions as separate asset keys. Preserve the visible amount, arrangement, outline and relative progression; one enlarged gem for every tier loses the design. A shared card frame and currency icon can still be reused where they match. If the concept deliberately repeats the same icon with different numeric labels, keep that reuse. Do not generate a new image for every price or quantity.

Inspect existing files against this map. Extract or generate missing distinct art only when authorised and necessary; include those variants in the output count and split batches as needed. If generation is unavailable or outside budget, identify the missing variants and supply the handoff instead of silently substituting unrelated art.

Use the selected concept as the visual source for every extracted part, whether it was generated earlier in the same request or supplied as an attachment. Ask imagegen to isolate the listed components while preserving their design. If multiple input images are needed, label their roles explicitly.

Add a shared extraction instruction to the concept prompt, followed by a compact list of the required output files. For example:

> After creating the concept, use that actual image to extract each listed component as its own PNG. Preserve the shapes, colours, borders, highlights and shadows. Remove labels, changing values and surrounding UI; keep enough transparent padding for each component's shadow. Leave panel/button artwork free of studs for the separate real texture layer. Do not invent a stud tile, redesign the pieces or combine them into a sheet. Return the concept and all listed assets together.

List each needed icon, frame, pointer, non-stud texture or effect by filename and a short description; no separate prompt is needed per asset. Generate one useful piece per file. Use another imagegen pass if an extracted asset contains baked labels or studs, a missing border, opaque background, checkerboard pixels or unintended redesign. Do not replace this stage with a programmatic crop of the mockup. Filesystem tools may copy, inspect and package outputs; they do not fulfil visual extraction. Reuse the actual stud tile unchanged; it does not consume a generated-output slot.

When more than eight images are needed, split the output list into batches of at most eight. The first batch includes the needed concepts; later batches attach the selected concept and generate remaining assets without regenerating it. Reference attachments do not consume output slots. A tool with a lower actual output limit may need smaller operations, but that does not change the default combined user-facing brief.

Typical boundaries:

| Extracted art | Kept live in the interface |
| --- | --- |
| Button base with border, lip and highlight | Label, price, interaction and state binding |
| Stud-free panel shell | Layout, scrolling, item rows, content and a separate sourced stud-texture layer |
| Item/resource icon | Quantity, currency, damage or XP value |
| Progress-bar shell and fill art | Actual fill amount and progress label |
| Pointer, burst, shine or glow | Target position, timing, opacity and motion |

Use one coherent reference for a family of assets. When extracting a pressed variant, preserve dimensions and alignment so the hit target does not jump. A simple native press movement can also use the same base; do not generate another image for every possible numeric value or text state.

## 3. Inspect and record

View the actual outputs, including their alpha channel over both light and dark backgrounds. Compare border thickness, hue, highlights and shadow direction with the selected concept. Keep padding consistent. Check that no part of the control is cut off and that a supposedly seamless tile actually repeats cleanly. Imagegen extraction may drift; the comparison is necessary.

Keep a small asset manifest alongside the delivered files. Record:

- Selected concept path/version and source-reference roles.
- Concept part/tier and defining appearance (including visible amount and silhouette), stable asset key, local file, pixel dimensions and transparency status; record why any shared source matches each use or mark the distinct asset pending.
- Intended native component, state, anchor/parent and sizing behaviour.
- Measured safe inset or slice region, where applicable; do not guess coordinates.
- Live text/value binding separately from artwork.
- Upload status and real Roblox asset ID only after a successful authorised upload.
- For stud layers, the source file/library identity or URL, author/terms and permission status, checksum, tile dimensions, `TileSize`, tint/transparency, parent, inset/mask and z-order. Keep an unuploaded asset ID unset.

Use stable names such as `button-primary-base.png`, `panel-shop-shell.png`, `pattern-studs-tile.png` and `pointer-hand.png`. Retain the concept and originals so a future session can reopen them after compaction. Deliver the folder, not loose files with missing dependencies.

## 4. Assemble and verify

Use native Roblox controls and layout to make the art functional. Borders and corners can use [9-slice scaling](https://create.roblox.com/docs/ui/9-slice): set the image's ScaleType to Slice and determine SliceCenter from the actual source. Put a repeating pattern on a separate layer when stretching the centre would distort it. Do not nine-slice an entire HUD or a labelled button screenshot.

### Stud texture layer

Use an actual user-provided stud texture or a verified licensed/owned library asset. Keep the original PNG unchanged and record its source and permissions. A screenshot, tutorial or Creator Store listing does not establish ownership or redistribution rights. Never invent a Roblox asset ID, assume a library upload exists, generate substitute studs or build stud geometry. If no authorised texture is available, leave the layer pending and request a source while continuing the other UI work.

The [packaged source](../assets/textures/user-provided-studs.png) is a 500 x 500 RGBA image with four studs across each side; [its notice and manifest](../assets/textures/NOTICE.md) record user-provided provenance and the local-inclusion permission. It has no recorded Roblox asset ID. This is a source tile, not a generated panel or a blanket licence for other projects.

Apply it as a decorative native `ImageLabel`, with `BackgroundTransparency = 1` and [`ScaleType = Enum.ScaleType.Tile`](https://create.roblox.com/docs/reference/engine/classes/ImageLabel#ScaleType). Set [`TileSize`](https://create.roblox.com/docs/reference/engine/classes/ImageLabel#TileSize) to the displayed size of the whole source tile, not one stud. For this square four-by-four tile, `UDim2.fromOffset(128, 128)` is a starting example: about 32 pixels between studs before any parent `UIScale`. Tune from actual phone/desktop captures and record the final size; preserve the tile's aspect ratio and avoid stretching or nine-slicing it with the panel.

Use `ImageColor3` to tint the texture and `ImageTransparency` to control its contrast over the panel's separate base colour. Keep the original alpha; never bake the tint or opacity into the source. The packaged PNG is already translucent (alpha ranges from 0 to 115 out of 255): start with white tint and `ImageTransparency = 0` to preserve it, then tint or increase transparency only as needed for readable small prices. Record the chosen settings rather than treating a preview as approval for every UI.

Place the tile inside the panel's content inset, above its base fill and below border/highlight artwork, item icons, live labels/prices and interactive controls. Record the parent, `ZIndex`, inset and clipping/mask treatment. The border artwork must leave the tiled interior visible; an opaque full-panel fill placed above it would hide the texture. Check rounded corners and shadow padding in the assembled result; do not assume a sibling's corner shape clips the tile. Keep the decorative layer non-interactive and verify it does not intercept input.

Before repeating this treatment across the UI, assemble one representative panel or button and compare a native capture with the reference/concept at desktop and actual mobile size. Inspect repeated tile seams, stud proportions/density, alpha fringes, tint/contrast behind small numbers, border/corner placement and content/shadow padding. Verify labels/prices can change and the native control still works. Fix that component before propagating its settings. If Studio access is unavailable, keep this fidelity check pending; a tiled preview or static export does not prove native QA.

The user supplied [Marvin's UI tutorial](https://x.com/marvin_x1/status/2104937885044461584) as an example of a Creator Store texture layer applied to native UI alongside generated decorative header/item art. That description is user-reported; the linked video was not independently inspected for this guide. It supplies neither a verified texture asset ID nor reuse terms.

### Native controls and verification

Keep text live for localisation and changing values. Allow for [ScreenGui screen insets](https://create.roblox.com/docs/reference/engine/classes/ScreenGui#ScreenInsets), touch controls and controller focus. A decorative ImageLabel cannot replace an accessible interactive control. Check z-order, modal input, target hit areas and longer labels in Studio.

Compare assembled implementation captures with the selected concept at actual phone and desktop display sizes, using the asset map to check frames, backgrounds, icons and every pack/tier. Check visible amount, arrangement, silhouette, relative scale and progression alongside composition, legibility, texture scale, button depth and spacing. Inspect variants together so a missing pile or collapsed progression is obvious; correct mismatches before marking the screen visually verified. Also try presses, disabled states, rapid value changes and menu transitions. Report concept creation, asset extraction, upload, implementation and testing separately; completion of one stage does not prove the others.

# Prop extraction

The props are images extracted from the approved concept, not redesigns. This follows [romanum-ui-workflow's](../../romanum-ui-workflow/SKILL.md) concept-then-extraction rule, with one change that made the worked example's cut-outs clean: image tools that can't output real transparency draw each piece on a flat key colour, and a script keys it out afterwards.

## The extraction brief

Attach the approved concept (and any separate product sheet, such as an egg design) to the image request. State that the panel, cards, buttons and text are native, so only the listed pieces are images. Then, for every piece:

- **Name, aspect and content:** `prop-ghost.png`, square: the peeking character from the left of the panel, whole body, leaning as it does in the concept.
- **What to leave out**, so moving parts can animate separately: no spiders or threads on the branch, no smoke on the saucer, no pedestal, name plate or wisps on the product.
- **No text** in any piece, except lettering that is part of the object's design. No studs drawn; the project's real stud texture is a separate layer.
- **Backgrounds.** Don't ask for transparency; tools often paint a checkerboard. Instead:
  - Outlined pieces go on a **perfectly flat, solid pure cyan (#00FFFF)** background filling the image: no gradient, shadow, floor, vignette, checkerboard or texture. Keep every glow inside the piece's dark outline. Choose another key (magenta) if the piece itself contains cyan.
  - Glow effects (lightning, smoke puffs, sparkles) go on **perfectly flat pure black (#000000)**.
- Save each output untouched in `raw/`; no resizing or background removal by the generator. Regenerate once if the background isn't flat, text appears, or the piece is cut off or redesigned.

Batch within the project's per-request image limit (romanum-ui-workflow uses eight). The worked example used three batches: eight outlined props and icons, three effects, then the second product.

A typical event-shop set: hero product(s), a peeking character, a corner prop (used twice, mirrored by position), a crashed or hovering object, an attachment (branch, chain, vine) and a dangler, the header icon (also used on the HUD button), a currency icon, and three effects: a lightning wisp, a smoke puff and a sparkle. Small regular patterns such as caution stripes can be drawn by script as a tiny tile.

## Keying

[`scripts/key_assets.py`](../scripts/key_assets.py) turns `raw/` into transparent, trimmed, downsized PNGs (Python with NumPy and Pillow). List the pieces in a JSON file, `{"prop-ghost.png": ["chroma", 768], "fx-smoke-puff.png": ["black", 384]}`, and run `python key_assets.py raw out pieces.json`.

- **Chroma pieces (cyan or magenta):** alpha comes from how far a pixel lifts the key's bright channels above its dark one (for cyan, how much greener and bluer than red it is), compared with the key sampled from the image border. Along a thick dark outline this gives the true mix of outline and key. Pixels far from the key stay solid, so the piece's own cool greys survive. The key colour is then unmixed from semi-transparent edge pixels, and cyan spill in a thin band along the edge is removed, so no fringe is left.
- **Black pieces:** alpha from brightness with the colour unpremultiplied, which keeps soft glows soft. A small floor drops the generator's noise.
- Each result is trimmed to its content with padding and scaled so its longer side fits a per-piece limit (1024 for heroes and big props, 768 for characters, 384 for small critters, 256 for icons and sparkles).

The script prints each piece's size and its opaque and clear share. Check the outputs on both a dark and a light background before uploading: look for fringes, holes in pale areas and clipped glows.

## Upload and manifest

Upload through the project's normal asset route and record each real ID; never invent IDs or report an upload that hasn't succeeded. Keep a manifest table:

| Piece | File | Size | Key | Code key | Where it's used | Roblox image |
| --- | --- | --- | --- | --- | --- | --- |
| Peeking ghost | `prop-ghost.png` | 550 × 768 | cyan | `Ghost` | Left edge: slides in, floats, ducks out and back | `rbxassetid://…` |

In code, keep the IDs in one `Art` table keyed by role, and let an empty ID leave that piece out, so the shop runs before every upload is done.

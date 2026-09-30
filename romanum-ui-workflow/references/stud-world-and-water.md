# Stud world and water references

Read this only when the interface must sit coherently within a toy-like world or when map art direction is requested. These images do not establish that this style performs better for all younger audiences.

## World shapes

Open the [islands](../assets/references/island-water.png), [harbour](../assets/references/harbour-water.png) and [arena](../assets/references/island-arena.png). Notice the broad block-built silhouettes, repeated studs, simple colour families and strong landmarks. Docks, paths, towers and clearings make the layout readable from above and at player height.

Use actual user-provided or verified licensed stud textures where they reinforce the building material: terrain plates, walls, roofs, rocks and selected props. Apply them through a suitable Roblox texture/material surface; never model artificial stud geometry or generate a fake stud texture. Record provenance and real Roblox asset IDs as in [the UI texture guidance](asset-extraction-and-assembly.md#stud-texture-layer). Keep spacing and scale coherent across adjoining surfaces. Use quieter surfaces where a dense pattern would obscure a path, text, target or important object. Studs are a preferred material treatment for this direction, not a requirement to cover every face at equal density.

The [shop example](../assets/references/world-shop.png) uses a sign, local lights, an NPC counter and a conspicuous interaction pad to identify its purpose. Extract the wayfinding principle; do not copy its watermark, branding or full arrangement.

## Water boundary

The island and harbour screenshots show a pale/white band near land and rock intersections, a lighter cyan transition, then stronger blue water with a broad cellular/wave-like surface pattern. The edge helps separate solid land from water. Preserve that layered, stylised feel and the varying contours around objects.

The exact shader, materials, animation and rendering method cannot be identified from these stills. Treat a narrow light contact band, softer cyan shallows and blue open water as the target appearance, not as a verified implementation recipe. The light band should follow water contact rather than outlining every edge of an object above water.

If asked to implement it, prototype an approach supported by the target Roblox setup, such as shaped shoreline strips with separate soft transition art or suitable textured geometry. Generate required water/shoreline decorative textures through imagegen from the selected concept; the actual-texture-only stud rule still applies. Inspect seams, transparency sorting, moving-camera shimmer and cost on the target device. Do not promise a custom depth shader or a native effect without checking that the chosen technique is supported.

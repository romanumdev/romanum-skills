# Blender mesh and texture production

Use this when an effect's primary silhouette needs authored geometry (a slash that wraps round the caster, a wave ring with a curling crest, a vortex, a crown splash) rather than camera-facing cards. It covers making the meshes and textures and wiring them in Roblox. Choreography, render review and cleanup stay in [SKILL.md](../SKILL.md), [roblox-recipes.md](roblox-recipes.md) and [render-review.md](render-review.md). Sources were checked on October 14, 2026; the community items are DevForum reports, not Roblox staff statements.

## Responsibility split

Meshes carry the main shape, white alpha textures carry edges and internal detail, and transforms on one timeline carry motion. Particles, Beams and Trails add fine detail. If particles carry the primary mass, the effect tends to read as a flat disc or sparkle cloud.

| Job | Starting option |
|---|---|
| Volumetric silhouette | Imported MeshPart with an alpha texture |
| Scrolling energy along a curve | Beam with TextureSpeed (the only documented, cheap texture scroll) |
| History of a moving tip | Trail |
| Shape that changes form | Mesh flipbook: several imported frames, visibility swapped by the timeline |
| Fine transient detail | ParticleEmitter burst via Emit(n) |
| Hand-drawn motion on a card | Particle flipbook (Grid2x2/4x4/8x8 or Custom) |

## Textures

Author white/grey shapes with real alpha; tint in Roblox through Color, ColorSequence or Color3. A minimal set: soft glow, strip that fades at both U ends (tileable in U if it scrolls), open ring with gaps, noise/erosion mask, an element-specific detail (foam lace, embers, cracks), and one flipbook if needed.

Preferred order of origin: verified CC0 packs (for example Kenney's Particle Pack; para's "Animated Particle Effects 1" 8x8 sheets on OpenGameArt), procedural scripts (PIL/numpy with supersampling, or Blender noise/ramp nodes baked to an image), image generation within the user's authorised tools, then flipbooks rendered from Blender with an orthographic camera and transparent film. CC-BY needs credits; reject non-commercial, share-alike and GPL licences for monetised games.

- 512 px for single shapes, 1024 px for flipbooks or large hero shapes; Roblox caps UV maps at 1024 px and streams lower mips first ([texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications)).
- Convert black-background generations to alpha before upload; a black card only disappears in additive layers.
- Pad shapes away from edges. In flipbooks leave transparent gutters between cells because mip filtering bleeds neighbours; frame rate caps at 30 fps ([particle emitters](https://create.roblox.com/docs/effects/particle-emitters)).
- Preserve holes and ragged edges. Record each texture's origin, licence or prompt, and the actual uploaded id; never guess an id.

## Meshes in Blender

Common kit: crescent arc, open ring band, wave-crest ring (curling profile swept round a circle), vortex ribbon, dome slices with gaps, spikes, crown splash (cylinder wall with an uneven pointed rim).

- **UVs:** unwrap strips so U runs 0–1 along the length and V 0–1 across. Rings take U around the circumference; crowns take V from base to tip. This lets one strip texture taper both ends and fade tips.
- Keep pieces low poly and smooth-shaded; put the pivot where the effect grows from; apply transforms; name pieces consistently.
- Thin shells are seen from both sides: duplicate faces with flipped normals or use the importer's double-sided option where available, then verify both sides in a render.
- Export mesh-flipbook frames as separate objects in one file.
- Render front, side, top and three-quarter views and inspect them before export (see the romanum-3d-workflow skill). Import with the project's established FBX scale and record the import settings.

## Assembly and motion in Roblox

Build one template per effect: anchored MeshParts with collision, touch, query and shadows off and Transparency 1 at rest; attachments holding emitters, Beams and Trails. Emit-group attributes such as EmitCount and EmitDelay are a common community convention ([Jad's Emit Plugin](https://devforum.roblox.com/t/dear-vfx-makers-i-present-to-you-jads-emit-plugin/1986838)), not an engine feature.

Animate Size from the pivot, CFrame spin, Transparency and Color on the single cast timeline. Impact frames jump close to full size and value; the remainder eases out.

MeshPart has no UV-offset property, and scripts cannot assign MeshId ([MeshPart](https://create.roblox.com/docs/reference/engine/classes/MeshPart)). Options to make a mesh appear to flow, most reliable first:

1. Spin a rotationally symmetric mesh carrying a noise texture.
2. Run a Beam along the same path for the scrolling layer.
3. Mesh flipbook: keep every frame in the template and show one at a time ([community thread](https://devforum.roblox.com/t/what-are-mesh-flipbooks/2656999)).
4. Test before relying on: Decal.UVOffset/UVScale ([Decal](https://create.roblox.com/docs/reference/engine/classes/Decal)) or Texture.OffsetStudsU/V on the mesh. Community reports disagree about whether these follow the mesh's own UVs ([thread](https://devforum.roblox.com/t/how-can-a-mesh-texture-be-animated/1707980)), and each additional decal re-renders the surface ([report](https://devforum.roblox.com/t/decal-uvoffset-uvscale-causes-significant-performance-impact/4802916)).
5. EditableMesh UV offsets per frame work but cost script time each frame ([request thread](https://devforum.roblox.com/t/scrollable-textures-for-meshparts/2820890)); reserve for a hero effect behind a quality tier.

ForceField material on a mesh gives a Fresnel-faded shimmer whose speed is not adjustable ([announcement](https://devforum.roblox.com/t/new-material-forcefield-v20/297785)); preview it against the intended look before choosing it.

## Mobile

Overlapping large transparent surfaces cost more than small particles. Particle Rate caps at 100/s per emitter on mobile, and flipbooks may be dropped under memory pressure, so give every flipbook layer a static fallback. A mesh-led effect should still read with all particles disabled; low tiers drop secondary layers, never the primary meshes or the phase peaks. Profile in the MicroProfiler and on target hardware before raising counts.

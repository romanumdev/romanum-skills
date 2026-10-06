# Roblox recipe: luminous rolling water

This is a proposed implementation recipe, not a reconstruction of lawral's private code. Verify current official APIs and inspect the existing place before editing. Documentation was checked October 6, 2026.

## 1. Select the smallest suitable path

### Terrain baseline

Use existing Terrain water when the game's swimming behavior, simple tuning, or broad coverage matters more than matching hero-scale relief. Documented knobs are WaterColor, WaterReflectance, WaterTransparency, WaterWaveSize, and WaterWaveSpeed. Color is global to Terrain water; do not promise separate per-pool Terrain palettes with these global properties. WaterWaveSize is constrained to 0–1 studs; WaterWaveSpeed is 0–100 up/down cycles per minute. These knobs support a baseline but do not alone establish the demonstrated large custom-wave silhouette or crest-specific white activity.

[Terrain API](https://create.roblox.com/docs/reference/engine/classes/Terrain)

### Existing skinned mesh

A pre-authored skinned grid can use Bone.Transform for cosmetic wave deformation. Reuse the project's working mesh/rig if available, keep its part transforms stable, and deform its bones instead of moving thousands of independent parts. Bone.Transform is not replicated: clients need shared wave parameters/time if consistency matters. Check real import/rigging support and do not assume bone deformation changes collision or swimming behavior.

[Bone API](https://create.roblox.com/docs/reference/engine/classes/Bone)

### EditableMesh

Use when changing positions, normals, UVs, or vertex colors is needed and the experience can support the API. It exposes SetPosition, SetNormal, SetUV, and SetColor; current APIs also include batching. Allocate topology/attribute IDs once, retain stable IDs, and update only necessary values. Prefer a fixed-size existing mesh when topology is static. Check creator verification, experience mesh/image API enablement, asset ownership/sharing, and client memory limits. Allocation can fail; provide a graceful lower-cost fallback. A Studio success alone does not establish published-client support.

Visual edits appear immediately, but collision/fluid geometry requires a separate rebuild. Do not rebuild collision on every visual-wave sample. Keep cosmetic mesh non-colliding when gameplay uses its own surface sampler/volume. Do not activate security/access settings without the required authorization.

[EditableMesh API](https://create.roblox.com/docs/reference/engine/classes/EditableMesh), [AssetService creation and failure behavior](https://create.roblox.com/docs/reference/engine/classes/AssetService/CreateEditableMesh)

## 2. Build a shared wave model

Start with a few smooth, differently directed components. One useful *proposed* model is:

height(x,z,t) = baseHeight + sum of A_i × sin(k_i × dot(direction_i, (x,z)) - omega_i × t + phase_i)

Use one dominant long component and lower-amplitude oblique secondary components. Sample height and derivatives from the same model for geometry, normal estimation, crest attachments, and required interaction probes. Evaluate in consistent world or water-local coordinates. Derive each frame from the original grid rather than repeatedly adding offsets to its previous deformed state; use elapsed time rather than a fixed per-frame phase increment.

A height field is the simplest controllable approximation. Optional Gerstner-style horizontal displacement can tighten crest shape but requires consistent displaced-position sampling for attachments and gameplay; do not introduce it just to imitate a familiar ocean tutorial. Bound steepness to avoid folds and verify the result at the player's camera. This recipe does not require real fluid simulation.

Tuning starting points, not measured source settings:

- Dominant swell wavelength about 8–20 avatar heights in open water; keep secondary amplitude around one-third of the dominant component, then judge the silhouette
- For a quiet cave, start amplitude around 0.05–0.25 avatar heights and longer/slower motion; increase only if the desired energy calls for it
- Space geometry densely enough to preserve the chosen silhouette at the near camera; use coarser samples for distant regions rather than a fixed grid density for the entire map

Use game-relative scale. Do not copy the creator's 50 × 50 count as a map dimension or a universal performance budget.

## 3. Color and material response

Keep the body's middle values blue, raised illuminated shoulders cyan/turquoise, and white reserved for selected peaks/glints/foam. Candidate art swatches: deep blue #075F91, body #138CB5, shoulder #24C6D2, accent #EAF8F8. These are proposed colors, not extracted Roblox property values. Tune under actual cave/day/night lighting; bright reference pixels are already lit and video-compressed.

SurfaceAppearance supports PBR maps on UV-mapped MeshParts, including color, normal, roughness, and metalness. Use a fine authored normal pattern to enrich a coarse rolling surface and a restrained roughness treatment for crisp highlights. Do not increase metalness merely as a universal gloss slider. The documentation warns that most SurfaceAppearance properties are not runtime-script-modifiable and rendering depends on graphics quality/device. Verify the exact property before proposing a runtime animation.

There is no documented SurfaceAppearance OffsetStudsU/V control. For repeating images on BasePart faces, Texture supplies StudsPerTileU/V and OffsetStudsU/V; TweenService can animate them. For a UV-mapped EditableMesh, SetUV is a different supported route, with CPU/update cost and all maps sharing that mesh UV flow. A scrolling flat Texture layer does not automatically conform to a displaced mesh. Avoid stacking large transparent planes just to obtain two counter-scrolling layers.

Do not prescribe arbitrary GLSL/HLSL, Unity Shader Graph, scene-depth sampling, or a custom Fresnel shader as if these were Roblox engine material APIs. View-dependent glints can arise from built-in lighting/material response; an authored color approximation is also valid when labeled honestly. True refraction or depth-driven transparency is optional and cannot be claimed from this source.

[SurfaceAppearance](https://create.roblox.com/docs/reference/engine/classes/SurfaceAppearance), [Textures and decals](https://create.roblox.com/docs/parts/textures-decals), [Texture API](https://create.roblox.com/docs/reference/engine/classes/Texture)

## 4. Keep white effects selective

Treat sharp glints and broad soft foam/spray as separate layers. First tune material lighting for glints. Add original soft, irregular foam/spray assets only where they add activity. Candidate triggers are crest height/slope, rising-wave activity, shore contact, or a gameplay event. Use thresholds with hysteresis, short fades, and a capped pool of emitters/patches so every sample does not spawn a new effect. Keep attachments on the sampled surface and validate that patches do not visibly float above or slice through troughs. Moving an attachment follows the wave at emission; it does not by itself keep already-emitted particles on the changing surface. Use brief spray lifetimes, deliberately tracked surface patches, or another explicit strategy for long-lived foam.

ParticleEmitter supports burst emission, lifetime, transparency, size, orientation, and flipbook controls. Beam supports textured ribbons, TextureSpeed, width, transparency, and endpoints; it can be useful for short wakes or localized foam, but a single two-endpoint ribbon will not conform to a complex rolling field without additional geometry/sampling. Neither is proof of the creator's method.

For shores, use authored boundary guides or cheap localized probes/known bathymetry appropriate to the project. Taper large swell near rock edges and put irregular fading foam at real contact zones. Do not require shader scene-depth access. Wading rings, entry bursts, boat wakes, and combat splashes are separate proposed features; implement only those requested and keep hit detection authoritative.

[ParticleEmitter](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter), [Beam](https://create.roblox.com/docs/reference/engine/classes/Beam), [Waterfall VFX layer example](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls)

## 5. Mobile and LOD strategy

Animate cosmetics locally from shared parameters rather than replicating every vertex/bone or particle each frame. Separate ocean coverage from near-camera detail. Reduce distant geometry update rate, fine detail, foam density, and shadow cost, with transitions that preserve phase and avoid seams. Shared edge sampling and world-consistent UV flow matter more than a particular LOD-ring algorithm. Do not assume RenderFidelity or streaming will automatically reduce a custom script's per-vertex update work.

Avoid excessive transparent overlap and particle overdraw. Pool reusable objects, reuse mesh/texture assets, avoid allocations inside hot loops, and release connections/buffers when water unloads. Update only visible/near regions when appropriate. Keep the cyan/blue silhouette readable in a low tier; lowering detail should not turn the intended look into flat opaque plastic.

Profile representative water views with combat/characters and the intended mobile device. Record water-on versus water-off CPU/GPU frame time, worst stutters, memory, active samples and effects; observe warm-device behavior where relevant. An empty-baseplate desktop FPS claim is not a map budget. Choose budgets from measured remaining frame time for the user's game.

[Performance guidance](https://create.roblox.com/docs/performance-optimization/improve), [MicroProfiler](https://create.roblox.com/docs/performance-optimization/microprofiler)

## 6. Minimum acceptance slice

For a small visual implementation, test a short capture from the low reference angle and the real third-person camera under the actual environment lighting. Show stills with water's silhouette and surface detail together. Check that:

- Waves change smoothly at varying frame rate, with no cumulative drift
- Large crest shape survives; fine patterns do not overwhelm the blue body
- Sharp glints remain occasional and white patches are selective rather than uniform stripes
- Geometry, foam attachments and any required gameplay sampler agree in coordinates/phase
- No cracks, z-fighting, abrupt foam/LOD popping or exposed test-plane edges in the playable slice
- Characters, combat telegraphs and traversable edges remain readable
- Target low graphics/mobile tier is measured and still recognizable
- Re-entering/unloading water does not leak connections, meshes or active effects

For a reference-analysis-only request, record these as future acceptance criteria rather than claiming they were executed. Expand the tests only as the implementation scope expands.

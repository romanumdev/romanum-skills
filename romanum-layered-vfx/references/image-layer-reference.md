# 85xvii image-led blackhole explosion

## Source and evidence boundary

- Creator: 85xvii, @85xvii_
- Original supplied URL: https://x.com/85xvii_/status/2107194537873748310?s=46
- Canonical source: https://x.com/85xvii_/status/2107194537873748310
- Reviewed October 6, 2026: actual full-screen source playback and paused samples across the clip
- Source media metadata: 1268 x 720, duration 11.583999 seconds
- X displayed October 5, 2026, 12:41 PM without a verified timezone; do not treat this display label as UTC

The caption describes a blackhole explosion and experimentation with a new style. The two visible source replies are audience reactions. The reviewed nearby posts/profile replies supplied no explanation of this effect's texture count, object types or construction. The user's suggestion that it is only a few images is a plausible reconstruction hypothesis, not a creator-confirmed count. Repeated cutout motifs are visible; source texture files, atlases, emitters, meshes, tools and easing are unknown. Audio was not inspected, so make no audio claims.

The clip starts with an effect already dispersing and shows repeated demonstrations with quiet intervals. Its entire 11.58-second duration is not one cast's required timeline. A cropped dark/cyan effect persists at the far left during quiet intervals; its relationship to the central showcase is not established. Do not add its dark debris, floor ring or behavior to the central effect's fingerprint.

No creator artwork, video or extracted frames are redistributed. Use the timestamp ledger below. This text-only package contains no media or runtime assets.

## Timestamp ledger: observed pixels

These are representative seek positions rounded to hundredths, not frame-accurate transition boundaries. Browser seeking can land on neighboring decoded frames.

| Sample | Observed central effect |
|---|---|
| 0.00 | Already dispersing: broad cyan/white ragged diagonal streak, thin crossing vertical streak, hollow gold/pink shapes and sparse flecks |
| 0.75 | Pink four-point/star-like cutout with forked tips and a bright outline; surrounding small marks |
| 1.55 | Almost quiet; a few faint colored fragments remain |
| 2.36 | Dense multicolored radial peak: white/cyan core, blue wavy boundary, long ragged strokes, gold/mint/pink hollow motifs |
| 3.17 | Central region nearly empty |
| 3.70 | Compact multicolored cluster with crossed tall/broad forms |
| 3.98 | Large body gone; recognizable smaller colored cutouts spread outward with broad gaps |
| 4.40–4.60 | Faint remnants, then almost empty center |
| 4.78–4.80 | Pink segmented outer arcs and nested center rings with open dark regions; a luminous oblique strip cuts across them |
| 5.00 | Much smaller pink four-point/star-like cutout at the center |
| 5.21 | Abrupt larger multicolored radial peak; tall narrow and broad diagonal cyan/white strokes intersect a bright pink-white core; wavy blue rim and gold/mint motifs |
| 5.41 | Primary glow mostly gone; larger crossing streaks and many repeated hollow/irregular colored fragments are farther apart |
| 5.59 | Sparse small cyan, pink, mint and gold fragments remain; most of the frame is empty |
| 6.40 / 7.20 | A later pink star sample, then near-quiet recovery |
| 8.01 / 9.63 / 11.24 | Later radial peak, dispersed repeated motifs, then faint residual fragments confirm repetition |

For a bounded reconstruction, the observed 4.60–5.59 sample interval supports: quiet → pink ring/diagonal motif → compact star → abrupt colored radial burst → separated cutout residue. Preserve that reading; do not invent a persistent black sphere, gravitational distortion, target damage or terrain destruction merely from the caption.

## What makes the image vocabulary work

**Observed:** jagged bright strokes contain dark holes; elongated gold and colored motifs have hollow interiors; ring arcs have large open gaps. Tall thin and broad diagonal forms overlap around the center, with fragments projecting in multiple directions. Cyan/white carries the hottest value; pink, mint and pale gold separate families. Their sizes, angles, spacing and brightness differ through the sequence. At the peak the core locally saturates; during dispersion, negative space and repeated cutout shapes are much easier to read.

**Inferred:** repeated shape families could share a small texture vocabulary, duplicated with different tints, rotations, aspect ratios and lifetimes. Crossed projected axes, overlap and outward spread create perceived volume. Pixels do not prove arbitrary world-oriented planes or billboarding: camera-facing images, velocity-relative particles, textured geometry and combinations can produce similar projections. Do not count visible copies as unique image files. No reliable avatar anchor is visible for the central effect, so avoid exact stud dimensions.

**Proposed authoring vocabulary:** create permitted original motifs for an open ring/arc, a forked star, a ragged hollow stroke, a small hollow loop/shard, and optional soft rim. Reuse the stroke or loop at smaller scale before adding another texture. This is a compact starting design, not the source's proven asset inventory. Preserve transparent holes and padded edges; no opaque rectangular card background. Use texture alpha for silhouettes, not black fill masquerading as holes. Review the original motifs against both dark and bright scenery.

## Roblox reconstruction choices

Official API support checked October 6, 2026. Recheck the relevant source when implementing. None of these mappings establishes the creator's implementation.

| Responsibility | Proposed option and limitation |
|---|---|
| One-shot 2D cutout layers | ParticleEmitter with Texture, Enabled=false and Emit(count); an Attachment establishes origin. Size/Transparency NumberSequences shape lifetime; Rotation and RotSpeed set initial degrees and degrees/second. They sample on emission, so changing initial rotation settings is not continuous control over already emitted layers |
| Frontal star/flare/rim | FacingCamera/FacingCameraWorldUp particles or BillboardGui plus ImageLabel. BillboardGui always faces the camera; depth can flatten when every major layer uses the same facing plane |
| Velocity-aligned streaks | ParticleEmitter VelocityParallel or VelocityPerpendicular. Test the actual motion/orientation; LockedToPart only makes active particles follow the emitter source, not arbitrary CFrame-oriented image planes |
| Exact crossed world planes | Transparent non-colliding supporting Parts with SurfaceGui/ImageLabel, rotating/moving the parts. Set BackgroundTransparency=1 and animate image scale/rotation/tint/ImageTransparency separately. SurfaceGui follows its selected part face; test front/back and edge-on views rather than assuming a two-sided card |
| Curved/stretched strip | Beam with Attachment endpoints, widths and cubic curvature; FaceCamera is deliberate. TextureMode/TextureLength and TextureSpeed control repeat/stretch/scroll, not an arbitrary image mask |
| Reused atlas | ImageLabel ImageRectOffset/ImageRectSize select a rectangular pixel crop. A zero dimension displays the full image. Keep transparent holes inside the crop and sufficient padding; these UI crop fields do not apply to ParticleEmitter, which has its own flipbook system |

Keep BillboardGui/SurfaceGui AlwaysOnTop=false when scene occlusion matters. AlwaysOnTop=true draws over 3D objects and can destroy the apparent depth/gameplay readability. GUI ImageTransparency and particle Transparency are opacity controls, not silhouette construction. Do not assume scale/rotation alone can turn a generic disk into the reference's ragged hollow shapes.

### Masking and transparency

Baked PNG alpha is the simplest reconstruction route for the observed holes and jagged edges. Ordinary ClipsDescendants is rectangular; rotation support has current setting-dependent restrictions, and it does not provide arbitrary silhouette masking. CanvasGroup can flatten children and apply UICorner/UIGradient group styling, at texture-memory cost; it can go blank at its memory cap. EditableImage can author RGBA pixels but has enablement/permission, size, memory and displayed-update limits. These are optional advanced routes, not prerequisites or evidence of the source's technique. Do not enable persistent access/settings just to avoid authoring alpha textures.

### Timing, motion and layer configuration

Start with one bounded burst, not the source's repeated test loop. Use the existing per-cast elapsed-time controller and seeded variants. Map the observed ring → compact star → radial pop → sparse fade into the ability's animation markers. The sampled ring-to-star-to-peak spacing is approximately 0.2 seconds per beat, a comparison anchor rather than exact source keyframes or a mandatory combat duration.

Give each layer a visual job, asset/pivot/aspect, origin offset, facing/plane choice, initial angle and angular change, scale envelope, outward path, tint, opacity envelope, start offset, lifetime and quality tier. Keep a brief bright core; let large ragged strokes disappear before the last small motifs. Stagger size/fade by family rather than shrinking every layer identically. Avoid a filled white sphere or uniform sparkle cloud. Pick world planes only if they improve side-camera fidelity; billboard the small detail when useful. Use small spatial offsets to avoid coincident-plane artifacts, then validate actual depth/occlusion.

## Image-layer fidelity gate

Review actual normal-speed runtime video and paused phases against the linked source. Record Pass / Needs adjustment / Not tested. Use the shared lifecycle/performance gate in [render-review.md](render-review.md).

1. Pink open rings and oblique strip resolve into a compact star before the abrupt multicolored peak
2. The radial peak has distinct tall/thin and broad/diagonal forms, hollow motifs and a readable blue boundary, rather than one flat solid disk
3. The authored holes and broad gaps survive without bloom, at small size and against light scenery
4. Reused fragments disperse with varied size/orientation/tint and clear to a quiet center; no permanent test-loop residue
5. Front, side, near and oblique cameras show acceptable depth; world cards do not unexpectedly vanish edge-on, and billboards do not visibly collapse the main shape
6. Occluders and gameplay subjects render correctly; no accidental AlwaysOnTop overlay, card rectangle, clipped atlas edge or coincident-plane flicker
7. Low tier keeps ring/star/peak/fade with fewer duplicate layers, smaller transparent coverage and optional rim disabled; cancellation/recast resets active particles/UI parts

A few images can still mean many overlapping instances and costly fill-rate. Track unique textures separately from active layers, and measure near-camera transparent area, frame time and intended concurrent casts on target hardware. Asset reuse saves authoring/memory, not proof of mobile performance. This skill addition is source analysis and reconstruction guidance; no Roblox runtime effect or device performance was tested.

## Official technical sources

- [ParticleEmitter API](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter) and [particle guide](https://create.roblox.com/docs/effects/particle-emitters)
- [BillboardGui / SurfaceGui containers](https://create.roblox.com/docs/ui/in-experience-containers)
- [ImageLabel alpha/crop fields](https://create.roblox.com/docs/reference/engine/classes/ImageLabel)
- [GuiObject clipping and transforms](https://create.roblox.com/docs/reference/engine/classes/GuiObject)
- [CanvasGroup](https://create.roblox.com/docs/reference/engine/classes/CanvasGroup)
- [EditableImage](https://create.roblox.com/docs/reference/engine/classes/EditableImage)
- [Beam](https://create.roblox.com/docs/reference/engine/classes/Beam)

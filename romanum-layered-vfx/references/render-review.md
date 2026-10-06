# Render review and completion checklist

## Scope the test

Use a disposable test place or the project's existing VFX harness. Do not install, publish, change the live map, or alter combat permissions merely to test an effect. Keep the source comparison and runtime claims separate. This package supplies design/implementation guidance; it does not contain a Studio-tested effect.

## Evidence to collect

- Normal-speed clip from the same relative camera/avatar staging as the reference
- Phase snapshots appropriate to the selected reference: for doranto, anticipation, travel, first impact, sustained body, contraction minimum, second peak, low release and late recovery; for the image-led burst, ring, compact star, radial peak, dispersion and quiet reset
- For supplementary lightning, capture John's charge/impact/ring/aftermath or icydxmon's sustained core/branches/base. Treat any new windup or recovery as proposed
- An oblique and near-camera view in representative gameplay lighting
- Particle/bloom-off blockout view and low/high quality view
- Device/performance readings and cleanup results, or a clear pending test list

## doranto fidelity gate

Rate each item Pass / Needs adjustment / Not tested and explain the evidence. Do not average away a failed structural beat.

1. **Intent:** The cue is visibly tied to caster/weapon, and paths establish where energy goes
2. **First impact:** A brief rapid rise in scale and value is distinct from the lead-in
3. **Primary silhouette:** The body is broad and ground-rooted; bands and negative space survive at small size
4. **Hierarchy:** Bright core, colored rims/strokes, dark debris, and tiny accents have different visual jobs
5. **Motion:** Major strokes have coherent paths and taper; rotating/sweeping layers do not resemble random scatter
6. **Contraction:** The body actually compresses dramatically before the next event
7. **Terminal release:** Second peak changes dominant direction/shape and opens into low crescents
8. **Recovery:** Energy resolves before debris; nothing persists accidentally
9. **Scale/contact:** Avatar reference, floor lighting/rim, and debris timing agree; effect does not float unintentionally
10. **Readability:** Caster/targets, telegraphs and UI remain usable in real gameplay; sustained overexposure is controlled

For the doranto example, failing contraction or the changed second release means the result misses the source fingerprint even if particles look attractive.

For 85xvii's image-led mode, use the distinct [image-layer fidelity gate](image-layer-reference.md#image-layer-fidelity-gate). Its repeated showcase is not evidence that a single cast needs several dome impacts, ground debris, or a permanent emitter loop.

For John and icydxmon, use the distinct [lightning reference checks](lightning-references.md#reference-specific-review). Neither needs doranto's contraction and second dome release.

## Robustness gate

- Natural completion returns instance/connection counts near baseline after all lifetimes
- Cancel during every phase; recast immediately; no late burst or pooled-state contamination
- Caster removal/death, missing permitted texture/mesh, nil ground raycast, and streaming gap handled
- Low frame rate/late event start does not reorder beats or emit every skipped accent together
- Multiple casts do not overwrite a shared camera/light state or clear each other's roots
- No gameplay hitboxes, damage, floor destruction, or server authority added by cosmetic implementation
- Reused trails/emitters are cleared; tweens/tasks cannot still modify returned leases

## Performance gate

- Measure one cast and intended concurrent/worst-case casts against an agreed baseline
- Check closest camera: a small world effect can still cover most of the screen
- Inspect overdraw/transparent area, GPU frame time, Lua work, instance count and memory trend
- Test low/high graphics settings; use actual representative hardware where available
- Mobile tier retains phases and major silhouette, dropping secondary accents first
- Shared textures and bounded light/debris count; no unbounded loops or permanent update bindings

A documented rate cap is not a whole-effect budget. A low particle count is not proof that several screen-sized transparent meshes are cheap. Passing static/code tests is not render verification.

## Focused revision order

Fix phase/shape mismatch, then scale and causal placement, then value/negative-space readability, then motion/taper, then fine detail. If the result is overbright, first reduce overlap and restore gaps; do not compensate by adding darker random particles. Keep each revision bounded and re-render the changed phases.

## Handoff summary

State what was built, reference/asset attribution, which render comparisons and tests actually ran, measured device results, known gaps, and what decision is needed. Include a direct rendered result and the phase/layer configuration. Do not call it source-faithful or mobile-ready when those checks are pending.

---
name: romanum-layered-vfx
description: Design, build, or review readable layered Roblox ability VFX from a visual reference, including timed volumetric shapes and reusable alpha-texture/card bursts. Use for Romanum VFX work and source-fidelity review; excludes general water rendering and unrelated app work.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Romanum layered VFX

Turn a visual reference into a readable, timed, maintainable Roblox effect. This skill covers doranto's cyan/pink choreography, 85xvii's image-led blackhole burst, and two supplementary lightning references. These clips do not prove a production method or asset count. Preserve the selected reference's sequence and shape hierarchy before adding detail.

## Load the relevant references

- For this source or a similar multi-stage ability, read [source-evidence.md](references/source-evidence.md). It distinguishes observed pixels, creator claims, and interpretation.
- For 85xvii's ring/star/radial burst or a small reusable image vocabulary, read [image-layer-reference.md](references/image-layer-reference.md). It contains observed samples, alpha-card reconstruction options, orientation/masking tradeoffs, and its own render gate. Do not impose doranto's dome/debris sequence on this mode.
- For John's staged electrical AoE or icydxmon's sustained column, read [lightning-references.md](references/lightning-references.md). Keep their distinct sequences; the sustained clip does not show windup or recovery.
- For implementation, read [roblox-recipes.md](references/roblox-recipes.md). It contains verified API choices, implementation tradeoffs, and a tunable timeline.
- Before declaring an effect ready, use [render-review.md](references/render-review.md).
- Use [effect-brief.md](references/effect-brief.md) to record a new effect's contract and handoff.

## 1. Establish the effect contract

Inspect the existing VFX architecture, camera, ability animation, gameplay timing, asset permissions, and device target. Reuse the project's lifecycle, quality tiers, pooling, and event interfaces. Do not replace combat logic or camera ownership to make a showcase work.

Decide the intended reading: who initiates, where energy travels, where impact happens, what radius is gameplay-relevant, and when control returns. Keep visual extent and gameplay hitbox distinct and documented. Cosmetic debris does not destroy the map or deal damage.

For a new reference, inspect the actual sequence rather than its caption or thumbnail. Record representative timestamps, visible forms, motion, scale relative to an avatar, and recovery. Mark each claim as Observed, Inferred, or Proposed. A bright glow does not prove BloomEffect; a curved streak does not prove Trail; a video does not reveal the generating model, prompt, mesh source, or plugin. Do not invent audio if it was not heard.

## 2. Lock the reference fingerprint

For the doranto example, the recognisable fingerprint is:

1. A small weapon/arm-led cue grows into several curved cyan/pink forward paths
2. A sudden oversized impact establishes a broad ground-rooted luminous dome
3. Rotating bands retain dark gaps, with long tapered ribbons and dark block debris breaking its edge
4. The dome contracts strongly into a compact core
5. A second, sharper release adds vertical/jagged accents and larger debris, then flattens into low crescents
6. Energy disappears before the last debris settles and clears

The contraction and second release are structural, not optional filler. Do not reduce this reference to an expanding neon sphere or an undifferentiated sparkle cloud. A different requested effect may use a different sequence; do not force every ability into this one.

Create a simple silhouette blockout and a phase chart first. Define what must survive at thumbnail size and with all secondary particles disabled. Set hue, value, scale, and timing after the shape reads. The source's approximate palette is near-white/cyan energy, pink-violet rim and accents, and dark neutral debris. These are roles, not mandatory colors for every Romanum ability.

## 3. Build by visual responsibility

Keep each layer independently toggleable:

- Intent: animation-synchronised weapon cue and directional paths
- Primary mass: broken dome bands or arc meshes with designed negative space
- Ground contact: low rim and expanding/flattening crescents
- Secondary motion: a few tapered flying ribbons and jagged accent paths
- Physical consequence: bounded cosmetic debris with deliberate size and trajectories
- Fine detail: small spark/shard bursts
- Response: controlled local light; optional restrained camera response only when requested or appropriate to the established project

Use a Trail for a history of moving attachments, a Beam for a presently defined curve, a mesh for a designed volumetric silhouette, and particles for fine transient detail. Avoid making every layer a particle emitter. Imported assets need verified ownership/permission; never guess asset IDs or extract and republish the creator's assets.

For an image-led effect, a few authored alpha motifs can carry the primary silhouette through reuse, tint, scale, rotation and staggered lifetimes. Choose camera-facing particles/BillboardGui or world-oriented SurfaceGui cards deliberately; they have different depth and edge-on behavior. Preserve transparent holes and negative space. A small texture count does not guarantee low overdraw. Use the image reference's API mapping and render checks rather than assuming the source used these objects.

Implement one cancellable elapsed-time timeline. Do not let independently delayed coroutines drift apart or create a frame loop per particle. Use deterministic seeds for repeatable reviews. Preserve the authored collapse/release timing at low frame rate; skip expired accents when entering late rather than replaying them all at once.

## 4. Match the render, then optimise

Run in a scoped test scene with a reference-size avatar and reproducible camera. Review the actual rendered clip at normal speed and paused at each phase boundary. Compare source and result for shape, value hierarchy, timing, causal direction, avatar scale, and residue. Code completion, object existence, and a static screenshot do not establish visual fidelity.

If rendering is unavailable, deliver the proposed design/code and identify runtime render review as pending. Do not claim visual verification. Obtain authorised environment access through the surrounding workflow; this skill does not grant it.

Then test in representative gameplay lighting, close/oblique cameras, low/high quality, and actual target hardware where available. Mobile fidelity means retaining the main silhouette and phase transitions while dropping small accents, large overlapping transparent coverage, excess debris, and optional post-processing. Profile before increasing counts.

## 5. Complete the lifecycle and handoff

Every cast owns its root, connections, tweens, timed tasks, transient lights, and any camera contribution. Cleanup must be safe on natural finish, cancellation, caster removal, missing assets, and errors. Pooled instances must be reset; Trail:Clear() and ParticleEmitter:Clear() remove old history. Cancel delayed callbacks or guard them with a cast token before reuse. Do not return a pooled object while a live tween/task can still modify it.

Deliver the brief, phase timeline, layer map, asset manifest, scoped code changes when requested, rendered comparison, device/performance measurements, cleanup tests, and known gaps. Distinguish observed source behavior from proposed implementation and actually tested behavior. Apply the user's current permissions before installation, publication, or deployment; a reusable skill is not approval for those actions.

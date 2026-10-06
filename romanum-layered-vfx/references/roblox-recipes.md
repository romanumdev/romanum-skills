# Roblox implementation recipes

These are proposed methods for reproducing doranto's visual responsibilities, not a reverse-engineered source project. For 85xvii's image-led burst, use [image-layer-reference.md](image-layer-reference.md) instead of forcing this dome/debris recipe. API availability checked against Roblox Creator Hub on October 6, 2026. Recheck relevant official documentation when implementing.

## Layer-to-primitive map

| Visual responsibility | Preferred starting option | Why / caution |
|---|---|---|
| Weapon-led stroke | Trail with two moving weapon attachments | Represents actual path history. Stationary attachments do not generate a designed curve. Tune attachment separation, Lifetime and WidthScale; review from side angles |
| Curved travelling lead-in | Animated path carriers with short Trails, or Beams joining animated attachments | Trails suit advancing tips; Beams suit curves that exist simultaneously. Pick based on motion, not the word “trail” |
| Broken dome bands | A few authored open shell/arc MeshPart templates, or layered curved ribbon meshes | Primary shape should survive without emitters. Clone vetted templates; do not assume normal scripts can assign MeshPart.MeshId at runtime |
| Ground rim / low release crescents | Flat/open arc meshes scaled and rotated around a surface-aligned root | Meshes preserve gaps and taper. Avoid many translucent full disks stacked on each other |
| Long tapered strokes | Beams with controlled endpoints/curves, or crescent/ribbon meshes | Beam widths, attachment orientations, CurveSize0/1 and Segments determine form. A curved Beam is not arbitrary multi-knot lightning |
| Jagged terminal accents | Several connected short Beam sections or designed jagged meshes | Keep branch count limited; do not introduce unobserved full-screen distortion |
| Blocks / ground fragments | Cosmetic Part/MeshPart clones with bounded scripted trajectories | Dark silhouettes add scale. Keep visual debris separate from damage, collision and terrain destruction |
| Fine flecks / short sparks | ParticleEmitter bursts | Use small supporting accents; do not fill negative space with random sparkles |
| Lit ground response | One controlled PointLight or project lighting response | A self-bright additive texture is not a scene light. Test graphics-tier differences |
| Halo | Existing project bloom or optional bounded BloomEffect | Intensity/Size/Threshold are tuning controls. Glow may erase the dark gaps; review with bloom disabled as well |

### Verified API behavior

- Beams render between two Workspace-descendant Attachments. Their cubic curve is determined by endpoint positions, attachment orientation, and CurveSize0/1. Width0/1 control endpoint widths; FaceCamera controls camera-facing rendering; Segments trades curve smoothness against complexity. [Beam](https://create.roblox.com/docs/reference/engine/classes/Beam)
- Trails record moving attachment history. Their plane can disappear from some directions unless a camera-facing mode is used; that choice can alter the intended silhouette. Clear() removes history. [Trail](https://create.roblox.com/docs/reference/engine/classes/Trail), [Trails guide](https://create.roblox.com/docs/effects/trails)
- For timed particle accents, keep Enabled=false and call Emit(count) once at the beat; Clear() removes active particles. Configure Size/Transparency sequences, Lifetime, Speed, Drag, Acceleration, and orientation intentionally. [ParticleEmitter](https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter)
- Roblox's guide warns about screen coverage/overdraw and device-dependent effect quality. The documented mobile rate ceiling is 100 particles/second per emitter, not a recommended total budget or proof that a burst is cheap. Flipbooks can be disabled under memory pressure. Reuse textures and give the effect a non-flipbook fallback. [Particle guide](https://create.roblox.com/docs/effects/particle-emitters)
- TweenService handles property interpolation and cancellation; use explicit finite durations, with a controller for phase changes. [TweenService](https://create.roblox.com/docs/reference/engine/classes/TweenService)
- Use a bounded update loop only for genuinely continuous motion; keep handles and disconnect them. Camera render-step bindings need unique names and UnbindFromRenderStep. [RunService](https://create.roblox.com/docs/reference/engine/classes/RunService)
- MeshPart's MeshId is not an ordinary runtime-writable asset field. Author/import a permitted template through supported tooling, then clone it. [MeshPart](https://create.roblox.com/docs/reference/engine/classes/MeshPart)
- RaycastResult supplies surface Position/Normal/Material; handle a nil hit and streamed-out geometry. Exclude the caster/effect root. [Raycasting](https://create.roblox.com/docs/workspace/raycasting)
- PointLight offers local illumination; BloomEffect is post-processing. Treat their tuning as distinct responsibilities. [PointLight](https://create.roblox.com/docs/reference/engine/classes/PointLight), [BloomEffect](https://create.roblox.com/docs/reference/engine/classes/BloomEffect)
- Debris:AddItem(instance, lifetime) schedules disposal. It is a fallback, not cancellation of your connections or safe return to a pool. [Debris](https://create.roblox.com/docs/reference/engine/classes/Debris)

## Asset-authoring gate and honest fallback

Before promising a recognisable runnable effect, check that the primary dome-band and crescent assets actually exist and are permitted. Record their IDs, source/owner, dimensions, open gaps, UV/transparency intent, and the supported import/template route. If authoring is needed, use an already available approved mesh workflow to make a small reusable set of open tapered arcs and band/shell pieces. Review front, side, and oblique silhouettes before adding detail. This package does not supply runtime mesh or texture assets.

For an asset-free **shape/timing blockout**, construct a few stacked open band arcs from paired cubic Beams and attachment carriers, with taper, offset planes and a low ground arc. Use permitted built-in/simple static textures and cosmetic box Parts. Animate the complete group through impact, contraction and release. This can establish timing, gaps and scale without imported meshes, but is an approximation: camera-facing ribbons cannot fully reproduce an authored volumetric shell. Label geometry fidelity pending rather than replacing the reference with a plain sphere and calling it complete. If no permitted static texture is available, keep the accent layer disabled and report the asset gap.

## Concept-fidelity blockout

1. Stage a dark neutral floor and reference-size avatar. Keep a forward target point separate from the caster.
2. Author only three groups: travelling thin curves, broken dome, and low terminal crescents. Include no fine particles, bloom, or camera shake yet.
3. Establish the two peaks and strong contraction. At every chosen key time, compare the body's width/height, visible gaps, location, and avatar relation to the source.
4. Add dark block silhouettes to make volume legible, then long tapered strokes, then sparse detail. Reduce layers if the primary mass stops reading.
5. Add lighting last. If brightness alone is doing the work, the shape is not solved.

## Proposed configurable showcase timeline

This is a tunable starting reconstruction, not measured source keyframes. Preserve the sequence; tune timings to the ability animation and gameplay requirements. Times are seconds from cast start.

| Phase | Suggested interval | Main responsibility |
|---|---|---|
| Anticipation | 0.00–0.60 | Pose/weapon cue; almost no large energy |
| Directed travel | 0.60–1.20 | Several curved bright tips/short histories ahead of caster |
| First impact | 1.20–1.55 | Rapid rise in silhouette and value; ground rim and bounded debris |
| Sustained body | 1.55–2.55 | Banded dome, rotating sweeps, gaps, supporting strokes |
| Contraction | 2.55–3.05 | Strong shrink in width/height and reduction of secondary strokes |
| Terminal release | 3.05–3.55 | Second bright/angular peak, then low crescents |
| Recovery | 3.55–5.20 | Energy ends first; debris/faint residue resolves |

Do not stretch anticipation just to meet these numbers. For a shorter combat ability, map the phase markers into an animation-authored timeline and preserve distinct beats.

### Tuning parameters to expose

- Core radius/height and target offset in avatar-relative units; separate visual radius and gameplay radius
- Per-phase durations and easing; contraction minimum scale; terminal peak scale
- Dome band gap/thickness, count, rotational offsets, and angular speed
- Stroke widths, taper, endpoint paths, curvature, and lifetimes
- Palette roles and maximum luminous coverage
- Debris count, size range, flight duration, radial/upward velocity, spin, shrink/fade
- Fine accent counts/lifetimes, local light contribution, optional camera-response strength
- Quality tiers, near-camera attenuation, simultaneous-cast cap, and distance cutoff

Suggested prototype budgets, **not engine limits or performance promises**: begin with 3–5 primary band/arc pieces, 2–4 lead-in curves, 4–8 major accent strokes, 6–12 debris pieces and 20–40 small accent particles across the full cast. A low tier can halve/remove secondary strokes and debris while retaining the banded body and both peaks. Profile actual screen coverage and concurrency before treating these as production budgets.

## Lifecycle architecture

Create one per-cast context containing root, seeded RNG, elapsed time, phase state, cancellation token, connections, tweens, and pooled leases. On each necessary update, derive the phase from elapsed time. An event fires only when its boundary is crossed; a late start does not replay expired bursts. Keep pure shape evaluation separate from asset creation so deterministic phase snapshots can be compared.

For cosmetic debris, a scripted anchored trajectory can use p(t)=p0+v0*t+0.5*g*t*t and a bounded angular transform. This is a proposal for repeatable visual motion, not source physics. Use a floor-raycast result to orient the root and sample matching ground color/material where appropriate. Do not imply terrain destruction by modifying actual floor parts.

Natural finish lets short particles/trails expire before releasing/resetting resources. Cancellation can clear them immediately. Cleanup is idempotent: mark token cancelled, disconnect updates, cancel tweens, disable emission/trails, clear history, restore/release owned camera/light contributions, return reset pool leases or destroy owned instances, and clear references. Delayed tasks check the token and lease identity before touching objects. Never restore global Lighting or camera state from an old snapshot after another effect has legitimately changed it; use the project's compositor/ownership mechanism.

## Mobile and concurrency

Cull distant/off-screen secondary work before creating it. Use stable quality tiers rather than rapid frame-to-frame flicker. Reduce large overlapping transparent coverage before simply reducing tiny particle count. Keep cosmetic Parts anchored when simulated physics is unnecessary and CanCollide/CanTouch/CanQuery false. Limit unnecessary per-frame work and ensure handles are cleaned. [Roblox performance guidance](https://create.roblox.com/docs/performance-optimization/improve)

Test one cast, normal concurrent use, and intended worst-case concurrency. Record actual target device, quality level, resolution, baseline/effect frame time, peak instance/particle counts, and cleanup trend. A Studio phone viewport alone does not validate phone GPU performance.


### Concrete low-tier starting configuration

Use this as a configurable prototype, not a measured device guarantee. Keep the same phase controller and cleanup across tiers.

| Responsibility | Low/mobile prototype | Missing resource behavior |
|---|---|---|
| Intent | 2 lead-in paths, short histories | Beam/attachment blockout if weapon Trail integration is unavailable |
| Primary body | 3 broken band pieces; preserve dark gaps and both peaks | Paired-Beam arc blockout; label authored geometry pending |
| Ground contact/release | 1 rim + up to 2 low crescent pieces | Open Beam arcs; do not substitute filled glowing disks |
| Secondary strokes | At most 4 major strokes; omit tiny branches | Disable unavailable accent assets |
| Debris | Up to 6 anchored cosmetic boxes; no cosmetic collisions | Simple Parts; preserve delayed fall/clear timing |
| Fine detail | Up to 20 short accent particles across cast; no required flipbook | Permitted static texture; disable detail if missing |
| Response | At most 1 owned local light; optional bloom and camera contribution off | Effect still reads through shape/value hierarchy |

Reduce close-camera translucent coverage as well as counts; distance/concurrency tiers may drop all secondary strokes and fine detail. Do not remove contraction or the distinct terminal release to save cost. On cancellation, low-tier trails, emitters, tasks, connections and leases follow exactly the same cleanup contract as high tier. Run the missing-mesh and missing-flipbook paths in the render harness and compare the resulting fallback explicitly.

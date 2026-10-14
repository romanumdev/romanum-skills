# Void singularity ultimate

A two-stage purple/white/black "ultimate" ability: a charge that wraps the caster, then a singularity formed at a point ahead of them that collapses into a whiteout and detonates across the ground. Use it as a target for any high-tier signature move in a combat or class-based game. Its sequence and value hierarchy are the reference; its colors are roles that can be re-tinted per class or element.

## Source and evidence boundary

- Supplied privately by a project member as an MP4 on October 14, 2026. Creator, original post and any caption are unknown. Do not guess an attribution, and do not redistribute the clip or frames.
- Media: 1370 x 740, 30 fps, 7.63 seconds. The audio track is silent (measured peak about -91 dB), so make no sound-design claims from it.
- Reviewed by full-clip contact sheets at 4 and 12 samples per second plus single full-size frames. Times below are sample positions, not frame-accurate boundaries.
- The clip holds two casts. It opens roughly 0.9 s into the first cast (mid wind-up flash), and the second cast starts from a quiet baseline at about 3.83 s. The ledger uses the second, complete cast, with times measured from 3.83 s.
- Staging: a light checker baseplate, bright sky, and a small blue avatar holding a short blade, low-left in frame. It is the only scale anchor. No targets, dummies, damage numbers or UI are visible, so nothing here establishes hit radius or gameplay effect.

## Timestamp ledger: observed pixels

| Cast time | Observed |
|---|---|
| 0.00 | Quiet baseline. Dark ground cracks and a faint dust haze remain from the previous cast |
| 0.12 | White crescent wind arcs whip round the caster on the ground; thin pink ink-like tendrils; one tall thin pink-violet vertical streak. The whole frame shifts toward a purple tint |
| 0.27 | Framing is much closer to the caster. Several short bright white vertical light pillars rise around them inside a swirling white/pink ground ring |
| 0.40–0.65 | Wider again. A ring of white crescent arcs, pink and violet ribbons and short black ink strokes spins round the caster; a dark ring sits on the ground under it |
| 0.85–0.95 | Two bright white flash bursts at and just ahead of the caster; black vertical bar marks cut through the first |
| 1.10 | A white cloud-like flash with a long tapered white streak and black glitch bars sits ahead of the caster; the caster's own ring is fading |
| 1.20–1.45 | At a point well ahead of the caster (several body lengths): a glowing violet orb with a white core and a thin ring outline. Black vertical bars and a tall black column cut through it at onset; pink tendrils whip out |
| 1.45–2.10 | Sustained singularity. Orb with a white-hot center and violet shell; a dark spiky crown behind its lower half; a stack of pink-white horizontal ring discs rising above it into a column; concentric white ripple rings on the ground; pink tendrils sweeping round it. The caster stays still, low-left |
| 2.12 | Whiteout impact frame: a pink-white dome fills most of the screen, with dense black vertical bars across it and a flat white disc at its base |
| 2.25–2.50 | Purple tint is gone; normal sky and floor colors return. A broad flat white shockwave disc spreads along the ground; a tan dust cloud rises at the center; thick pink ink splashes and loops fly outward; many small black flecks |
| 2.50–2.90 | Shockwave disc thins and opens; dust widens; tendrils and splashes thin out and fade |
| 2.90–3.80 | Only drifting dust and dark flecks remain, fading slowly. Dark ground cracks stay visible into the next cast |

The singularity's position relative to the caster and the slight horizon tilt in a few frames suggest camera movement or shake, but the clip cannot separate a scripted camera from the recorder moving.

## Reference fingerprint

1. **Self-charge:** energy wraps the caster first (crescent wind arcs, rising pillars, a spinning ground ring), with a purple scene tint that tells everyone a big move is coming
2. **Launch:** a white flash pushes the energy forward; the caster's ring dies as the forward point lights up
3. **Singularity hold:** a compact orb (white core, violet shell, ring outline) with a vertical structure stacked above it and ripples below. It is held, not instantly exploded, for roughly 0.6–0.9 s
4. **Impact frame:** one near-full-screen whiteout with black vertical bars
5. **Detonation:** the tint drops, and a flat ground shockwave, dust and flung ink splashes replace the orb. The release is low and wide, not a tall sphere
6. **Residue:** energy ends first, dust and flecks last, ground cracks last longest

The two locations (caster, then target point) and the hold before the whiteout are structural. Do not compress it into a single expanding sphere at the caster.

### Value and color roles

- Hottest: near-white (orb core, pillars, crescent arcs, shockwave disc, whiteout)
- Energy: saturated magenta-pink and violet (tendrils, ring discs, orb shell)
- Contrast: near-black ink (crown, glitch bars, ink strokes, flecks). The black is doing as much work as the glow; keep it
- Physical: tan dust and dark cracks, in the floor's own palette
- Scene: a purple ColorCorrection-style tint during the charge and hold, cleared on detonation

## Roblox reconstruction

Use the shared [layer-to-primitive map](roblox-recipes.md) and the project's Blender mesh plus white-alpha texture workflow. These are proposed methods; the clip does not reveal the creator's objects or assets.

| Layer | Proposed build |
|---|---|
| Crescent wind arcs | 3–5 open tapered crescent MeshParts (Blender), white alpha streak texture, spun and scaled round the caster; tint white with a pink edge |
| Rising light pillars | Thin vertical card meshes or Beams with a soft-glow strip texture, emitted with a short stagger; 4–6 |
| Caster ground ring | One flat open-ring mesh with an ink-stroke alpha texture, spinning; pink/black tint pair |
| Ink tendrils and splashes | Beams between animated attachments with a ragged ink-strip texture (tapers both ends), plus a few liquid-splash card meshes or a Codex-made splash flipbook for the detonation splashes |
| Launch flash | Short-lived soft-glow billboard plus one tapered streak card in the travel direction |
| Orb | Sphere mesh with a fresnel-style white-alpha texture for the violet shell, an inner smaller white core, and a thin ring-outline card facing the camera |
| Crown | One jagged crown mesh (Blender), near-black, sitting behind the orb's lower half |
| Ring-disc column | 4–6 flat torus or disc meshes stacked above the orb, each with an open-ring alpha texture, staggered rise and spin |
| Ground ripples | 2–3 thin ring meshes or decal rings expanding from the orb |
| Glitch bars | A strip texture of black vertical bars on a few camera-facing cards or a ScreenGui overlay; on screen for only a few frames at singularity onset and the whiteout |
| Whiteout | A ScreenGui frame or a ColorCorrection brightness spike, shaped by a large soft dome mesh around the target so it still reads in world space |
| Ground shockwave | One wide flat disc/ring mesh with a ragged-edge alpha texture, scaled out fast then faded |
| Dust | Particle flipbook smoke (CC0 or Blender-rendered), tinted to the floor, slow drift; plus black fleck particles |
| Cracks | Decal or flat mesh with a crack alpha texture on the raycast floor hit, faded over several seconds; cosmetic only |
| Scene tint | A cast-owned ColorCorrectionEffect TintColor tween in, then a cut back on detonation |

Implement it as one cancellable elapsed-time controller, per the shared lifecycle rules. The caster position and the target point are two inputs; the singularity layers are parented to the target root, never the caster.

### Proposed timeline

Tunable starting values derived from the ledger, in seconds from cast start.

| Phase | Interval | Main layers |
|---|---|---|
| Self-charge | 0.00–0.85 | Crescent arcs, pillars, caster ring, tendrils; tint in |
| Launch | 0.85–1.15 | Flash at caster, forward streak; caster ring out |
| Singularity onset | 1.15–1.45 | Orb grows from a point, glitch bars, ring outline |
| Hold | 1.45–2.10 | Ring-disc column rises, crown, ripples, sweeping tendrils |
| Impact frame | 2.10–2.20 | Whiteout plus glitch bars; orb removed underneath |
| Detonation | 2.20–2.90 | Tint cut, shockwave disc, dust burst, ink splashes, flecks |
| Residue | 2.90–4.00 | Dust and flecks fade; cracks keep fading after the controller releases energy layers |

### Gameplay contract (proposed, not observed)

- Keep visuals client-side. The server validates the cast, picks the target point, fixes the start time and seed, and replicates one event; every client runs the same timeline from that start.
- Damage belongs at the detonation beat only, in a radius set by game config. The visual shockwave may be larger than the hitbox; document both.
- The self-charge and the hold are the telegraph. Give opponents a readable ground marker at the target point from launch to detonation if the move is meant to be dodgeable.
- Lock or slow the caster only during self-charge if the design wants commitment; the clip shows a still caster but says nothing about control.
- Clean every owned instance, tween, connection and the tint on finish, cancel, caster death or the caster leaving.

### Readability, comfort and mobile

- The whiteout and black bars are a flash. Keep them to a few frames, scale them down for effects the local player did not cast, and honour any reduced-flash setting the game has.
- The purple tint affects the whole screen. Apply it only for the caster and nearby players, or soften it with distance, so a crowded server is not permanently purple.
- Low tier keeps the fingerprint: crescent arcs, orb, ring-disc column, whiteout (reduced), shockwave disc and a little dust. Drop pillars, extra tendrils, splash flipbooks, flecks and cracks first. Do not drop the hold or the second location.
- Measure near-camera transparent coverage; the whiteout dome and the dust cloud are the two biggest overdraw risks.

## Fidelity gate

Rate each Pass / Needs adjustment / Not tested, from a normal-speed runtime capture with a reference-size avatar low-left and a target point several body lengths ahead. Then run the shared checks in [render-review.md](render-review.md).

1. The charge visibly happens on the caster first, with crescent arcs and a spinning ring, and the scene tint starts with it
2. A launch flash links the caster to a separate target point
3. The orb reads as white core, violet shell and ring outline, with a dark crown and a ring-disc column above it, and holds long enough to register
4. The whiteout is brief, near full-screen, and carries black vertical bars
5. Detonation is low and wide: a ground shockwave, dust and flung ink, and the tint is gone
6. Energy clears before dust; cracks fade last; nothing persists into the next cast unless intended
7. Black ink elements survive bloom and the purple tint
8. Low tier still shows charge, launch, hold, whiteout and detonation

This entry is source analysis and reconstruction guidance only. No Roblox build of this effect, render comparison or device test has been run.

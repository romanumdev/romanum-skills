# Rewarding level-up moment

This is the owner's five-step recipe for making a level-up feel earned. Use the same beats for other big reward moments too, such as a rank up, a rebirth, a pass tier, a finished quest or a boss reward. Every beat answers a real state change. The animation shows the reward; it never grants it.

## The five beats

1. **Fill the bar.** XP orbs fly from where they were earned into the bar. Each arrival nudges the bar, which fills up smoothly with a small shake.
2. **Hold the full bar.** Pause on the full bar for a beat. It glows and spasms, as if it can't contain itself.
3. **Blast.** A pillar of light shoots up from the player and a shockwave rolls out along the ground.
4. **Slam the text.** Big LEVEL UP text slams onto the screen. Confetti everywhere is optional.
5. **Show the reward.** Reveal what the player got: pop the new stats in one by one and count the numbers up.

## Roblox notes

- **Easing, never linear.** Use TweenService with `Quad`, `Back` or `Exponential` easing. Pop-ins use `Back` `Out` to overshoot and settle. A slam scales from large to normal with `Back` or `Exponential` `Out`.
- **Orbs (beat 1).** Pool the orb ImageLabels. Fly each one along a slight curve (a bezier stepped on `RenderStepped`, or two tweens), staggered by a few hundredths of a second. Each arrival tweens the bar fill a step (`Quad` `Out`) and gives the bar a short scale or position kick. The fill follows the server's real XP; if the orbs are skipped, snap the bar to the true value.
- **Hold (beat 2).** About 0.3 to 0.5 s. Tween a `UIStroke` and a glow image's transparency up, and jitter the bar's position or rotation by a pixel or two each frame. Stop the jitter cleanly when the hold ends.
- **Pillar and shockwave (beat 3).** Build these as world VFX the way [the layered VFX skill](../../romanum-layered-vfx/SKILL.md) does: Blender meshes with white alpha textures tinted in Roblox, per [its mesh and texture pipeline](../../romanum-layered-vfx/references/mesh-texture-pipeline.md), with particles only for sparkle detail. Not a particle-only effect. A short camera shake sells the impact.
- **Slam (beat 4).** Start the text at about 2.5x scale and fully transparent, tween it to 1x and opaque in about 0.15 s, then hold and fade. A `UIStroke` and a drop shadow keep it readable over the world. Confetti is a pooled burst of small rotated frames or a ScreenGui particle setup; cap the count.
- **Reward (beat 5).** Each stat row pops in with `Back` `Out`, staggered. Count numbers up by tweening a NumberValue and writing its value to the label on `Changed`, rounded and formatted. Count to the server's actual value.
- **Sound.** Give each beat its own cue: soft ticks for the orbs, a rising tone through the hold, a boom for the blast, a hit for the slam, a chime per stat. Don't reuse another feature's signature sound.

## Keep it bounded

- Scale it to the moment. A routine level-up during fast progression gets beats 1, 2 and a small 4. Save the full five beats for meaningful levels and milestones.
- When several levels arrive at once, play one sequence that shows the final level and the combined reward. Don't queue five sequences.
- Let the player skip or tap through, and keep movement and the game visible. Under Reduced Motion, keep the bar, the text and the reward and drop the shake and flashing.
- Pool and clean up every orb, mesh, particle and sound when the sequence ends or is skipped.

See also [tutorials and feedback](tutorials-and-feedback.md#layer-the-feedback) for how this fits with smaller feedback.

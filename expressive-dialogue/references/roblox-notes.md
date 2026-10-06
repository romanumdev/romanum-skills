# Roblox implementation notes

These are adaptation choices supported by current Roblox APIs, not a claim about the source creator's code. Check the existing game's UI/animation architecture before selecting a route.

## Native reveal is a strong baseline

`TextLabel.MaxVisibleGraphemes` controls visible grapheme units while layout is computed for the complete text. Setting it to `-1` shows all text. This directly supports stable final line breaks and skip-to-complete behavior without substring growth. It does not supply independent glyph scale, position and opacity animations; those need an additional renderer/presentation layer when fidelity requires them.

Source: https://create.roblox.com/docs/reference/engine/classes/TextLabel

Use native reveal for the reduced-motion/instant mode and as a safe fallback for languages where separate-glyph rendering would break shaping. The source's soft glyph arrivals may justify a more capable renderer, but do not mistake plain native typewriter reveal for the entire demonstrated effect.

## Measurement and rich text

Measure with the real font, final rendered text, line spacing and bounded width. `TextBounds` reports rendered dimensions; `TextFits` can detect overflow. Keep the text viewport at its measured final size while the surrounding body retargets; do not bind wrapping width to the animated parent. Reserve enough height for all wrapped lines and extra clipping clearance for glyph rise/scale, since lines exceeding the label's vertical space can disappear. Avoid tying `TextScaled` to a body whose size is changing: that can scale the whole paragraph during the resize instead of resizing its cream container.

Source: https://create.roblox.com/docs/reference/engine/classes/TextLabel

Enable `RichText` for semantic color/underline. Roblox documentation notes that automatic localization removes rich-text formatting tags; reapply styling to localized strings. Store emphasis semantically or per localized message rather than assuming English byte positions. Escape dynamic names and literal text before inserting trusted styling tags. Use the final rendered text/semantic token stream for reveal counting and ranges, excluding tags and encoded-entity bytes.

Source: https://create.roblox.com/docs/ui/rich-text

## If animated graphemes are needed

A custom presentation layer must preserve line breaks, native glyph advances, kerning/shaping and decoration placement. A row of independently measured letters is not automatically equivalent to a natively rendered sentence. Test the chosen font and scripts. Prefer native shaping or a native fallback when exact glyph metrics cannot be preserved.

Keep per-glyph arrival transforms local to fixed final slots; do not let layout objects rearrange the row as glyphs become visible. Keep the bubble's dimensional tween separate from text size. Reuse existing project font/assets and inspect actual pixels before claiming a fidelity match.

## Body, tracking and modal effects

Use existing world-to-screen or billboard architecture to keep the bubble near its speaker, with explicit distance/visibility and viewport-clamp behavior. Animate body size/opacity and local glyph motion independently from anchor tracking. Head-look behavior should have intentionally bounded tracking and smooth recovery; the video establishes the outcome, not a particular rig method.

Roblox's UI tween guidance supports interpolated properties using TweenService and configurable easing. Use the reference's restrained ordinary resize and larger modal settle as two distinct motion modes, not one global spring setting.

Source: https://create.roblox.com/docs/ui/animation

A modal's dim/blur/texture layers must be explicitly owned and cleaned up. Keep gameplay/reward state authoritative; a click/reveal completion animation is presentation, not permission to award progress or accept a gameplay transition twice.

## Minimum runtime verification

Run the project's applicable checks and inspect the actual rendered client. Test font loading, phone-sized layouts, long/localized names, repeat input, cancel/replace while typing, tracking during camera movement and reduced-motion mode. Profile many simultaneous bubbles if the implementation creates one visual element per grapheme. State what was actually exercised; no runtime implementation or game tests are bundled in this design-only skill.

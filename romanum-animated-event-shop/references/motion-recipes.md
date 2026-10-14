# Motion recipes

These are the timings and formulas from the worked example, a Halloween shop built as native Roblox UI. Treat the numbers as tuned starting points at a 960 × 640 design size, not rules. Pixel amounts scale with the design size.

## The clock and the helpers

One function sets every animated property from two times: `since`, seconds since the shop opened, for entrances, and `t`, the current `os.clock()`, for idle loops.

```lua
local function ease(p) -- back-out: overshoots a little and settles; use for every pop-in
	p = math.clamp(p, 0, 1)
	local c = 1.7
	return 1 + (c + 1) * (p - 1) ^ 3 + c * (p - 1) ^ 2
end

local function smooth(p) -- smoothstep; use for fades and slides that shouldn't overshoot
	p = math.clamp(p, 0, 1)
	return p * p * (3 - 2 * p)
end

local function animate(now)
	local still = reducedMotion()
	local since = still and 99 or now - openedAt -- reduced motion: every entrance is already finished
	local t = now
	local idle = still and 0 or 1 -- multiply every idle term by this
	local function enter(delay, length)
		return math.clamp((since - delay) / (length or 0.4), 0, 1)
	end
	-- ... each prop below
end
```

Multiplying idle terms by `idle` (rather than branching) keeps every prop's resting pose identical with and without reduced motion.

## Entrance cascade

| Start (s) | Length (s) | Piece | Entrance |
| --- | --- | --- | --- |
| 0 | 0.32 | Panel | `UIScale` from 0.6 to 1 with `ease`; the dim behind fades to 0.55 transparency over 0.25 s |
| 0.12 | 0.38 | Header icon | Size from 0 with `ease`, rotation from −40° to its idle wobble |
| 0.22 | 0.5 | Peeking character (left edge) | Slides in 260 px from off-screen left with `ease`, fading in |
| 0.37, 0.44 | 0.45 | Corner props (bottom corners) | Size from 0 and rise 120 px from below with `ease`, one after the other |
| 0.38 | 0.5 | Crashed object (behind top-right corner) | Drops from 220 px above and 120 px right, spinning 90° into its tilt; fades in over 0.2 s |
| 0.45 | 0.45 | Attached growth (branch on the right edge) | Size from 0 at its anchor with `ease`, as if growing out from behind the panel |
| 0.6+ | 0.55 | Danglers (spiders) | Thread length from 0, so they drop down into place |
| 0.7 | 0.4 | Trailing smoke | Fades up once its source has landed |
| 0.6 + 0.7 n | — | Lightning | First flashes arrive in turn, then random timers |
| 0.26 + 0.045 k | 0.32 | Content tiles | `UIScale` from 0.4 to 1 with `ease`; a second card adds 0.12 s |

## Idle loops and surprise beats

Each prop stores a `Phase` so copies never move together.

**Peeking character.** Floats (`sin(t*2) * 10` px vertical, `sin(t*0.9) * 6` px horizontal), sways `sin(t*1.3) * 7`°, and breathes in transparency (0.06–0.16, as a ghost would). Every 7 s it ducks out and back:

```lua
local cycle = t % 7
local peek = 0
if cycle < 0.45 then peek = -70 * smooth(cycle / 0.45)          -- duck out
elseif cycle < 1.3 then peek = -70                              -- hide
elseif cycle < 1.75 then peek = -70 + 82 * ease((cycle - 1.3) / 0.45) -- pop back with overshoot
end
```

**Corner props.** Anchor at the bottom centre (`AnchorPoint = (0.5, 1)`) so they squash from the ground. Breathe with `sin(t*2.6 + phase)`: width −3 %, height +4.5 %. Hop 22 px for 0.5 s on their own period (`3.2 + i * 1.6` s). For a glowing face, flicker `ImageColor3` brightness by up to 16 % with two summed sines (`sin(t*13)` and `sin(t*7.3)`) so it reads as a candle, not a pulse.

**Crashed or hovering object.** Hovers `sin(t*1.8) * 8` px and rocks `sin(t*1.1) * 5`° around its crash tilt. Smoke: four puffs on a looping life `(t*0.42 + phase) % 1`; each drifts up and back from the source, grows from 40 to 120 px, rotates, and fades in fast and out slowly (`0.75 * (1 - life) * min(1, life * 6)`). Puffs follow the object's hover so they stay attached.

**Attached growth.** Sways `sin(t*0.8) * 2.5`°. Slow and small: it's the anchor for the danglers.

**Danglers.** A native 2 px `Frame` thread whose length drives the critter's position. Idle stretch `sin(t*1.5 + phase) * 9` px, side drift 3 px, swing `sin(t*2 + phase) * 10`°. Every `4 + i * 2.7` s each one drops 55 px in 0.25 s and climbs back over 1.95 s.

**Lightning behind the panel.** Each bolt keeps its own `Next` time. When `since` passes it, record `Flash = since` and set `Next = since + 1.6 + random() * 2.8`. A flash lasts 0.5 s with a double strike: near-opaque for 0–0.06 s and 0.12–0.18 s, then fading. Reset the timers on every open.

**Hero product (egg) on a pad.** Bob `sin(t*2) * 7` px and rock `sin(t*1.2) * 2.5`°. The shadow under it shrinks 10 % and lightens as the egg rises. The pad's glowing stroke pulses with `sin(t*2.6)`. Four sparkles twinkle with `max(0, sin(t*2.3 + phase))^2` as their size and spin slowly. Three fog puffs drift outwards from the feet on alternating sides and fade.

**Content tiles (specimen tanks).** Three to five bubbles per tile rise on `(t*0.42 + phase) % 1`, wobble sideways and fade as they rise. Bubbles stay inside the tile (`ClipsDescendants`).

**The rarest tile and progress bars.** Rotate a rainbow `UIGradient` on the `UIStroke` (90°/s on the rare tile, 60°/s on the pity bar). This shimmer is the only motion on content, and it is on the border, not the text.

**HUD button.** The button that opens the shop wiggles its icon for 0.6 s every 4 s (`sin` decaying to zero), so the entry point looks alive too.

## Close and notices

Close tweens the panel's `UIScale` to 0.82 and the dim to fully transparent over 0.16 s (`Quad`, `In`), then disables the `ScreenGui` if nothing reopened it meanwhile (compare a token). A notice pill pops in with a 0.25 s `Back` tween, holds 2.4 s and fades over 0.25 s; a newer notice cancels the old fade with a token.

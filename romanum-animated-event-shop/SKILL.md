---
name: romanum-animated-event-shop
description: Build a themed Roblox shop or event window that feels alive. A native panel pops in, then image props around its edges arrive one by one and keep moving (peeking characters, bouncing corner props, hovering wrecks, dangling critters, lightning), with extracted imagegen props, a single animation clock, reduced motion and a feature flag. Use for seasonal or event shops, gacha/egg windows and other decorated menus; pair with romanum-ui-workflow for the concept itself.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Animated event shop

A decorated shop reads as an event when its frame is part of the show: the panel arrives first, the decorations arrive after it in a short cascade, and nothing ever stands completely still. The [worked example](assets/example-halloween-shop.jpg) is a Halloween shop from a released Roblox game: a ghost peeks from the left edge, jack-o'-lanterns sit on the bottom corners, a crashed saucer smokes behind the top-right corner, spiders dangle from a branch, lightning flashes behind the panel, and each egg card's egg bobs over a glowing pad.

This skill covers the motion and assembly. Use [romanum-ui-workflow](../romanum-ui-workflow/SKILL.md) for the concept and its approval, and [romanum-game-economy](../romanum-game-economy/SKILL.md) for prices and odds. Paid random items follow Roblox's rules whatever the shop looks like.

## Workflow

**Layout reference -> imagegen concept with the props -> approval -> imagegen extraction of each prop -> key, trim and upload -> native panel -> prop choreography -> flagged test in Studio.**

1. **Start from a layout the owner wants.** A screenshot or clip of another game's shop is a layout reference: copy its structure (header bar, corner icon breaking out of the header, close button, where props sit) and redraw it in the project's own style, colours and theme. Never copy its art, fonts or text.
2. **Put the props in the concept.** Ask for the decorations around the panel's edges in the same image, each with a role and a spot, so their scale and overlap are approved together with the panel. Give each one a theme twist that ties it to the game (a bedsheet-ghost alien rather than a plain ghost).
3. **Decide what is an image.** The panel, header, cards, tiles, bars, buttons, text, prices and odds stay native and editable. Only the props, egg or product art, icons, effect sprites and small tiled patterns are images. Split anything that moves separately into its own piece: the branch without its spiders, the saucer without its smoke, the egg without its wisps or pedestal.
4. **Extract, key and upload** each piece as described in [prop extraction](references/prop-extraction.md). Record every piece in a manifest with its key colour, size, role and real asset ID.
5. **Build the native panel** and place props on two layers, behind and in front of it, as described in [Roblox assembly](references/roblox-assembly.md).
6. **Choreograph** the entrance cascade and the idle loops from [the motion recipes](references/motion-recipes.md). Every prop gets an entrance and at least one idle motion; a few get an occasional surprise beat (a duck, a hop, a drop).
7. **Gate and test.** Mount the shop only in Studio or behind a server-set flag until the event ships. Check it at desktop and phone sizes and with reduced motion on, and report created, installed, Play-tested and owner-reviewed states separately.

## Motion rules

- **Order matters.** The panel pops first (about 0.3 s, a small overshoot). The header icon follows at about 0.1 s, then props arrive at 0.05–0.1 s spacing, each with its own direction: slide in from the side it peeks from, bounce up from below, drop from above, grow from where it is attached. Content (tiles, cards) pops in on its own stagger. The whole cascade lands within about 0.7 s.
- **Idle never repeats in sync.** Give each prop its own phase and slightly different frequencies; give a second card or a mirrored prop an offset. Surprise beats run on separate periods (4 to 7 s) so they don't coincide.
- **Ambient, not distracting.** Idle motion is small: a few pixels of bob, a few degrees of sway, 3–5 % squash. Keep large motion for entrances and the rare surprise beats. Content the player reads (names, odds, prices) does not move after it lands.
- **Close fast.** About 0.16 s ease-in shrink and dim fade, then disable. Never replay the cascade backwards.
- **Reduced motion** shows every prop in its final pose with no idle loops, including the glows and shimmer.

## Build rules

- Drive all motion from one clock: the time since the shop opened for entrances and the current time for idle loops, evaluated each frame by one `RenderStepped` function that sets every property. This keeps the cascade deterministic, makes reopen restart it, and lets a test step it by calling the function directly when Studio isn't drawing frames. Use tweens only for one-off UI responses (close, notices).
- Stop the loop when the window closes, and disconnect it on error with a warning instead of erroring every frame.
- Design at a fixed size, fit with one `UIScale` that includes the props' reach past the panel, and rescale text-size limits with it.
- Purchases, prices, odds and balances come from the server. An animation never grants or implies anything; a preview build's buy buttons say it's a preview.

## Not covered

Uploading assets, publishing the place, turning on the live flag and any real-money product are separate, explicitly authorised steps. Generated images need the project's own image route; a written prompt is a handoff, not an asset.

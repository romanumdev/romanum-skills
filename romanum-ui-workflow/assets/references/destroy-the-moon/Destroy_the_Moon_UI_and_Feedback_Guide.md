# Destroy the Moon - UI, tutorial and feedback direction

Standalone advice for the owner's separately created UI-generation skill.
Status: reference review and proposed design guidance. Not a finished skill, generated UI, installed effect or playtest.
Updated: 29 September 2026.

## 1. The direction in one sentence

Bright, studded Roblox toy-world visuals with effortless actions, short typewritten instructions, obvious pointing arrows and frequent, readable rewards.

Keep the world visible and the action moving. Make each success noticeable without turning every success into a full-screen interruption. The intended experience is a colorful incremental simulator, not a restrained corporate dashboard or dark realistic space shooter.

## 2. What the supplied video actually demonstrates

Source: `20260929-0722-23.4835828.mp4`, approximately 80.67 seconds, 1916 x 1078 at 30 fps. These are recording timestamps, not timings for Destroy the Moon. The reference shows a lifting/breaking/collecting simulator, not shoulder-gun combat.

| Recording time | Observed reference | Useful adaptation |
| --- | --- | --- |
| 00:00-00:16 | Bright cyan surroundings, lime ground accents, large studded surfaces, an outlined yellow level bar and repeated stat gains. The visible character reaches several early levels in this excerpt. | Toy-like moon regions, conspicuous early progress and a level bar that responds to actual XP. Do not copy the reference's Strength stat by default. |
| 00:00.25-00:01.50 and 00:15-00:17.50 | Tutorial text appears progressively: a partial line becomes a short instruction. It sits over a dark translucent strip while the world remains visible. The instruction changes as the action changes. | Short typewriter instructions, one current action, and a restrained backing behind readable text. |
| Around 00:04 and 00:36 | Bright blue-white bursts, rings/particles around the character and level-reached messages accompany progress. | A short local level-up burst, bar response and readable level label. A proposal for precise timing is below. |
| Around 00:20-00:26 | World items have identities and values. A message says the full backpack teleported the player back to the roof. The player then reaches the Sell shop, and the Selling panel shows Sell All; a later message reports three items sold. | Separate collecting materials from earning Cash through selling. Your requested direct full-bag teleport to Sell is a new adaptation, not exactly what this clip proves. |
| Around 00:26-00:30 | A sequence of large white, dark-outlined arrows directs movement to the shop. The shop dims the world behind it. Item rows have large previews, stud textures, visible stats, Cash prices and Equipped states. | Clear wayfinding and a small gun shop where the next purchase is immediately understandable. |
| Around 00:41-00:43 | At Level 10 the scene dims and an arrow points at Rebirth. Its panel displays Level 10/10, a reset warning, and before/after multipliers. The visible level returns to 1, followed by a prominent multiplier animation and subsequent level gains. | Level-gated, deliberately confirmed rebirth with an explicit reset summary and a short, rewarding payoff. This does not establish the reference's complete save/reset rules or your final rebirth requirement. |
| Around 00:68-00:76 | Buying a visibly different weight is followed by different equipment and larger visible stat gains. | A gun purchase should change the shoulder equipment or firing pattern as well as its numbers. |

The clicky keyboard sound is part of the owner's requested direction. Exact audio samples, synchronization and the reference's camera-shake curve were not independently verified in this frame review. Do not tell another agent those assets or timings were extracted.

The owner also wants the satisfaction of item-collection GFX from Where's my Haul?. No exact Haul effect module was inspected for this document. Use the actual asset/module only when supplied; do not claim a faithful reuse from its name alone.

## 3. Art and UI language

### Bright color with clear roles

Use saturated, clean colors and broad, simple silhouettes. Give each moon zone a different dominant terrain/accent combination while keeping consistent shop and HUD components. Space can be stylized and bright; it does not need to be grey, dark or realistic.

A proposed role scheme is gold for XP/level emphasis, green for affordable Cash purchases, and a distinct accent for rebirth. These are suggestions, not selected final colors. Pair color with an icon, label and state so color alone never carries the instruction.

### Stud textures

Studs should look like a coherent toy-building material, not random noise. Repeat a clean raised pattern at a consistent scale on terrain, selected panel backgrounds, headers and buttons. Let it support the form rather than dominate it.

Keep the texture softer under small numbers and body text. Do not put equally strong studs, rays, gradients, sparkles and outlines behind every word. Avoid stretching circular/square studs into long shapes when a button resizes. Request a repeatable texture separately from the panel silhouette so the implementation can keep the scale consistent.

### Glowing and shiny, without washing everything out

Use local rim glows, soft halos, a short shine sweep or faint radial rays to emphasize important states. Reserve the brightest treatment for the current tutorial target, a new gun, a level-up or rebirth.

A purchased gun can have a stronger glow than its locked preview. An affordable button should be easy to distinguish from Equipped, Locked and Maxed without every button constantly pulsing. Keep terrain edges, button text and target silhouettes visible through effects.

### Type and panels

Use chunky readable lettering, clear light/dark contrast and a dark outline for floating numbers or instructions over the world. Ordinary shop content belongs on stable panel surfaces with enough breathing room for touch input.

The desired tutorial transparency mainly means an unobtrusive background and a graceful exit. It does NOT mean making the instruction itself permanently faint. Use clear letters over a transparent canvas or feathered translucent backing. Fade the completed line away; keep the current instruction readable.

Do not automatically copy the reference's number of side buttons, sale banners, offer badges, currencies or premium purchase buttons. Borrow its visual treatment, not its entire interface density.

## 4. Tutorial rule: point at the action, then acknowledge it

Teach through a visible object or button, a pointer, and a few words. One target at a time. No opening paragraphs explaining the economy.

### Typewriter behavior

- Reveal a brief line progressively instead of dumping a paragraph on screen. Use short phrases such as "Walk near rocks", "Upgrade your gun" and "Ready to rebirth".
- Let the arrow and actionable control appear immediately; do not require the player to wait for the typing to finish.
- Proposed starting feel: around 25-35 characters per second with a small pause at punctuation. This is a tuning suggestion, not a measured rate from the video.
- Use a quiet keyboard-like click with modest variation. Limit how many clicks overlap; a rapidly changing counter must not restart a typing loop.
- Tap/press to finish the current text instantly. Provide tutorial skip and sound/reduced-motion behavior without removing essential controls.
- Keep the label layout fixed while characters appear so the sentence does not jump around. Reveal user-visible characters cleanly and keep normal words readable.
- Once the real action completes, stop the old typing/sound, fade or replace the line, and move to the next relevant step. If the player acts ahead, skip already-completed instructions.

Do not slowly retype a whole instruction whenever its progress number changes. Separate an animated instruction from a live value such as 8/10.

### Dimming and arrows

For a first-time shop or rebirth action, darken/desaturate the unrelated scene and keep the intended control prominent. Use a live spotlight/cutout, not a painted screenshot of the target. A white arrow with a dark edge can point at the actual button; a gentle bob is enough.

Recalculate its placement as the interface resizes, the panel scrolls or the camera moves. The arrow should sit beside the actionable region, not hide the price or cover the touch target. Keep the tutorial text, close/skip control and any needed movement controls above the dimming layer.

For walking, point at the actual world destination or lay a short chain of arrows along the route. If the destination is offscreen, point towards it without pretending it is directly in front of the player. Do not dim the whole world throughout ordinary mining; that would hide the very action and effects the player is enjoying.

### Proposed opening sequence for this game

| Trigger/state | What gets emphasized | Minimal copy | Step completes when |
| --- | --- | --- | --- |
| Ready to play | Nearby mineable rock cluster | Walk near rocks | A real eligible shot hits |
| First material collected | Bag meter briefly | Rocks fill your bag | The actual inventory updates |
| Bag full | Sell indicator/teleport transition | Bag full. Selling... | The full-bag transition and sale actually complete |
| First useful gun upgrade is affordable | Shop, then the relevant upgrade button | Upgrade your gun | The server confirms the purchase |
| Gun equipped | New shoulder equipment | Stronger gun! | The display acknowledges the real equipped state |
| Rebirth level reached | Rebirth button, then honest summary | Ready to rebirth | The player chooses and the transaction succeeds |

This assumes the recommended auto-sell flow. Do not instruct "Press Sell" while automatically selling, or tell the player to buy something they cannot afford. Use the actual implementation's action.

Few words does not mean hidden consequences. Prices, bag limits, what is reset and what is kept must remain explicit. A brief rebirth reset/keep summary is necessary even if ordinary tutorial steps use only arrows.

## 5. Reward feedback: frequent, but layered

Give the player something to notice at each useful action, with a clear hierarchy:

| Event | Suggested visual feedback | What must remain true |
| --- | --- | --- |
| Accepted hit | Shoulder recoil, impact tick/flash, a small rock/salvage icon and +N | N is actual collected material, not invented damage or Cash |
| Material collection | A few fragments/icons curve toward player or bag; bag count responds | Visual travel does not control the inventory grant |
| Target destroyed | Bigger crack/pop, a bounded fragment burst, short stronger sound | No duplicate hit/kill reward unless the rules intentionally grant both |
| Bag full / sell | Compact full cue, short safe teleport, material count clears as actual Cash arrives | Sell once; no payout before a failed transaction or silent discarded overflow |
| Level-up | XP bar finishes, local ring/sparkle burst, brief "LEVEL N" and a restrained punch | The level is real; extra multipliers only appear when actually awarded |
| Gun purchase | Preview pops, Equipped state changes, new shoulder gear/firing appearance | Cost, stats and equipped gun agree with the server |
| Rebirth / BFG | Fuller dramatic sequence, then actual before/after benefits | Clear confirmation first; no other player's reset |

Examples such as +1 are a format, not a requirement to show +1 after every hit forever. When a gun earns 12 materials, show +12 or a truthful merged +24, not twelve unreadable labels. Distinguish materials gained, damage dealt and Cash earned with different icons/contexts.

### Proposed motion starting points

These are optional prototype ranges, not source measurements or final settings:

- Button press: quick compression and release, around 0.08-0.15 seconds each way.
- Routine pickup/gain: brief scale-in, small rise, fade over roughly 0.5-0.9 seconds total.
- Pickup attraction: a compact curved path, approximately 0.25-0.5 seconds for nearby effects.
- Level-up: local burst and short text, about 0.6-1.0 seconds without taking control away.
- Tutorial fade after completion: around 0.15-0.3 seconds.
- Major rebirth: a few seconds for the full optional presentation, with Skip and a quick accessibility alternative.

Favor a sharp start and a controlled settle over constant elastic wobbling. Faster weapons should produce a denser but still legible rhythm. Increase the sense of output using grouped bursts and a visibly improved firing pattern, not an unlimited number of effects.

Use recoil, icon punch and local object shake for routine hits. Keep global camera shake exceptional and bounded; ten impacts at once should not multiply it ten times. Reduced Motion should remove large flashes, shake and forced camera travel while retaining clear numbers and success states. Never make speed, resources or progress depend on watching the animation.

## 6. Gun shop and HUD

### Gun shop

Keep the useful structure from the reference: big weapon preview, short name, one meaningful stat comparison, Cash cost and a clearly distinct Equipped/Buy/Locked/Maxed state. A vertical list or small grid is enough. Show the next useful affordable purchase before a screenful of remote future items.

For Destroy the Moon, use the actual shoulder-gun/launcher artwork rather than the reference's weights. Purchase and equip should be one straightforward action when the item is strictly an upgrade. Avoid adding a separate weapon inventory, attachment builder or rarity roll just to fill a panel.

An optional capacity upgrade can support the growing material rate. It does not require a second shop, crafting system or extra currency. Keep new systems separate from visual styling decisions.

### HUD

Prioritize a clear Level/XP bar, compact bag count, Cash and a rebirth indicator. Gun stats can live in the shop/inspect surface rather than another large permanent meter. Do not add the reference's Strength system unless the game actually uses it.

During mining, favor world feedback and compact counters. During a guided purchase, make the relevant panel dominant. During a major celebration, temporarily coordinate other popups instead of drawing them all on top of one another.

The auto-sell trip should have an obvious transition, not appear to be a connection error or unexplained character jump. Recommended behavior is to return to the previous valid mining position after selling, unless the player deliberately opens the shop. This is a proposed flow choice, not an observed mechanic of the reference.

## 7. What to ask the separate UI-generation skill for

Do not write a skill or invent its tool capabilities from this document. Use this as its visual brief.

Useful deliverables are a desktop composition, a narrow-phone composition, and isolated reusable assets: stud tile, panel/background parts, soft radial burst, transparent glow/sparkle, material/gun/bag icons, pointer arrow and button states.

Separate decorative art from live content. Cash, XP, prices, names, bag totals, button labels, locks and tutorial text should remain editable runtime elements, not baked into a generated PNG. Generate typewriter text styling, but implement the actual typing, fading, spotlight and arrow tracking in game.

Ask for Idle, Pressed, Affordable, Unaffordable, Locked, Equipped and Maxed where relevant. Include safe transparent padding, clean silhouettes and backgrounds that can resize without stretching the stud pattern. A fake checkerboard is not real transparency.

Preview tutorial states on a real in-game screenshot when available. The source frame is a reference, not permission to duplicate its logos, characters, storefront offers or unrelated mechanics. Use explicit placeholders for unapproved stats and prices; do not invent finalized balance to make a mockup look complete.

## 8. Acceptance checklist

- With the tutorial text hidden, the highlighted object/arrow still makes the next action reasonably obvious; the short text removes remaining ambiguity.
- The typing is quick enough not to block acting. Audio stops on skip, line change and completion.
- The spotlight highlights the actual target at desktop and phone sizes; it never covers its label, cost or input area.
- Studs and glow preserve text contrast, especially under small prices and counters.
- Materials, Cash, XP and damage never masquerade as one another.
- Rapid gains merge correctly; no endless sound pile-up, offscreen flood or mandatory claim popups.
- Level-up and purchase effects reflect actual values; no fictitious multipliers for spectacle.
- No ordinary fullscreen dim/celebration obscures ongoing mining. Safe-zone pauses and menu state are deliberate.
- Full-bag teleport/sale/return is understandable, reversible on failure and does not strand the player or lose resources.
- Test rapid levels, multiple hits, shop/tutorial overlap, bag filling mid-volley, skip, death/reset, rejoin and Reduced Motion.
- Judge visual feel in actual motion on a phone as well as desktop. Still images do not prove animation timing, performance or gameplay responsiveness.

## Reference handoff

The companion reference pack contains this guide, the updated game direction, timestamped stills and a contact sheet. Stills preserve source imagery; captions are review notes. The 80-second source video is not duplicated into the pack. Supply the original uploaded video separately when another agent needs exact motion or audio review.

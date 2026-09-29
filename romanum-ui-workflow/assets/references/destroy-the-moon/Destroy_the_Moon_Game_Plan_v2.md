# Destroy the Moon - updated game direction

29 September 2026. Design update based on the owner's latest instructions and the uploaded simulator reference. Not implemented, installed, playtested or posted to Trello.

## The loop

Walk near rocks or aliens -> shoulder guns fire automatically -> every valid hit collects materials into a bag -> bag fills -> teleport to Sell -> exchange materials for Cash -> buy a stronger gun -> earn levels quickly -> rebirth for permanent improvement -> repeat across changing moon zones.

This supersedes the older plan's direct Cash-per-destruction and automatic Cash-to-Power purchases. A bag, Level/XP and a deliberate gun shop now have actual purposes. There is no need to add a separate Strength progression system.

## 1. Confirmed direction versus open choices

Owner-requested direction:
- Bright colors, stud textures, glow, frequent +N feedback and level-up effects.
- Proximity-based automatic shoulder-gun firing; simple manual interaction can supplement it.
- Material collection on hits, inventory capacity and a full-bag teleport to the Sell area.
- A shop for stronger guns/upgrades, not compulsory automatic Cash spending.
- Quick early levels, with reaching a required level as the proposed rebirth gate.
- Open, forward-connected moon zones with different rocks/aliens.
- A BFG-style moon-destruction moment remains part of the concept.
- Tutorial guidance should point at the next action with minimal, progressively typed text.

Still to settle:
- Whether selling and the return trip are both automatic. The recommended default below is yes.
- Exact reset/keep fields, multipliers and weapon progression across rebirths.
- Zone unlock requirements and how many zones ship initially.
- Whether the BFG is the rebirth ceremony or a separate ability. Combining them remains the recommendation, not a confirmed requirement.

## 2. Shooting and collecting

The player primarily chooses where to stand or walk. Shoulder pods acquire an eligible nearby target, fire, and smoothly move to the next valid target. Tapping can select a farther target or request a bounded faster firing rate, but ordinary auto-fire should already be satisfying.

A shot that misses, hits an invalid target or arrives after the target is resolved earns nothing. An accepted hit produces the real material gain and updates the bag. Use a finite material yield/health budget for each target so repeated small hits cannot create unlimited loot from one rock. Aliens can provide salvage under the same simple system.

Keep XP tied to a clear real action, such as collected materials or effective target work. An extra button press or client effect does not award XP. Early thresholds can be small enough for frequent level-ups; final values require playtesting.

Death effects, material icons and shoulder recoil make the action expressive. Materials enter inventory automatically; no walking over every fragment. Target destruction has a stronger visual payoff. A separate destruction bonus is optional, not implied by hit rewards.

No ammo, reload, manual pickup, crafting, equipment durability or complex alien combat is required for the first version.

## 3. Bag full -> sell -> resume

Recommended flow: when the bag reaches capacity, stop starting new attacks, give a compact full-bag cue, move to a safe Sell pad, sell the bag once, show Cash arriving, and return to the previous valid mining location.

Keep the sell trip short. Do not require three extra confirmations, make the player walk the whole route again, or charge a fee for returning. If the player deliberately opens the gun shop, do not auto-return through its menu; resume after that interaction ends.

The physical gun shop can sit beside Sell. It should also have an obvious optional access button, so buying an upgrade does not depend on catching a very brief teleport window. The opening tutorial can point at the first affordable upgrade without forcing a shop visit on every later sale.

Full-bag transitions need one active transaction, not one teleport request per arriving projectile. Handle in-flight gains without silently deleting the final materials. The bag removal and Cash payout must agree through retries, rejoin and sale failures. A failed sale preserves unsold inventory; it does not show a successful Cash burst.

Capacity must grow appropriately as guns improve. Otherwise a great gun could fill the bag every second and replace satisfying mining with constant teleporting. Check actual mining time versus time spent selling, rather than tuning damage alone.

## 4. Cash, levels, guns and rebirth

Cash comes from selling materials and buys gun upgrades. Show the real price, next benefit and Equipped state. Automatically equip a strictly better purchased upgrade, rather than requiring another inventory menu.

Level/XP is separate from Cash and principally indicates progress towards rebirth. Levels can be frequent without granting a new unexplained stat every time. Only display a multiplier reward when the game actually grants one.

A simple proposed way to preserve the earlier automatic-weapon idea:
- Within a cycle, Cash improves the current gun's output.
- Rebirth permanently unlocks and auto-equips a stronger shoulder-weapon family or rank.
- The next cycle visibly destroys familiar targets more efficiently.

This is a proposal to combine the shop and rebirth ideas, not a second compulsory weapon inventory. A simpler permanent-multiplier-only rebirth is also possible; choose one model before finalizing saves and prices.

Use one final calculation for gun damage, firing rate, material yield, sale value and any permanent bonus. Do not multiply the same benefit in several systems accidentally. Bigger numbers should buy noticeably stronger output rather than only bigger target health.

## 5. BFG and zones

Recommended BFG treatment: reaching the rebirth level makes the moon-destruction action available. Show a concise reset/keep summary and let the player choose. A short cinematic destroys a separate visual moon, celebrates the real permanent reward, then resumes the next cycle.

The old final-core requirement is NOT automatically retained on top of the new level requirement. Do not add an extra boss, fuel currency or long charge grind unless chosen. Other players' worlds and progress are not reset by someone's personal cinematic.

Rebirth reset rules remain unapproved. Define Level/XP, Cash, bag contents, Cash-bought gun tiers, permanent weapon unlocks and zone access separately. A full bag must be sold, retained or explicitly included in the warning; never quietly disappear. Cosmetics, settings and legitimate permanent purchase entitlements should remain protected.

Keep a wide open sky and broad zones connected in a clear forward direction. Studded rocks, low crater borders, crystals and terrain-color transitions can mark each region without high enclosing walls. Reuse a small target/weapon kit. Different moon regions should change silhouettes and visual rhythm, not introduce new control schemes.

A rebirth-gated zone ladder is one possible simple rule; exact gates are still a decision. Do not make Level both an undocumented zone gate and a rebirth requirement by accident.

## 6. What the reference adds, and what it does not prove

The supplied recording visibly shows rapidly advancing early levels, a collecting/selling loop, a shop purchase and a Level 10 rebirth prompt. Around 00:41-00:43 it displays before/after multipliers and a reset to Level 1. That is observed in this recording, not a validated normal-player pacing curve or a complete account of its save rules.

The reference's full bag returns the player to a roof, followed by a visit to Sell. Destroy the Moon's requested direct full-bag teleport to Sell is intentionally different.

The visual direction is documented separately in `Destroy_the_Moon_UI_and_Feedback_Guide.md`, including timestamped evidence, typewriter text, spotlight arrows, stud textures, glow, gain effects and shop states. No UI-generation skill is created here.

## 7. Small development sequence

1. One open field: shoulder auto-fire, a rock and a cartoon alien, hit-to-bag collection, compact +N effects.
2. One complete economy loop: full-bag transition, sale, Cash, one affordable gun upgrade and return to mining.
3. Level and rebirth: XP, short level-up effects, level requirement, exact reset/keep contract and one stronger next-cycle weapon/bonus.
4. Moon destruction plus a second open zone. Expand content only once that full cycle feels good.
5. Integrate the final visual kit, tutorials, saving/fault tests and real desktop/phone checks.

Begin authoritative state and save contracts alongside the features. Do not build the whole moon before the first bag-and-shop loop works. Keep monetization, extra currencies, pets, crafting, trading and elaborate alien combat outside this initial build.

## 8. Evidence and acceptance

Track: first shot, first material, first level-up, first full bag, successful sale, first gun purchase, return to mining, rebirth eligibility, completed rebirth and first improved cycle-two hit.

Watch active mining time versus selling/menu time; time without a valid target; bag-fill rate by gun; early levels per minute; and whether the first rebirth actually feels stronger. No claim of better retention without real cohort data.

Test duplicate hits, in-flight hits while full, full/sell loops, sale failure, replayed rewards, purchase affordability, fast successive levels, rebirth with unsold materials, safe return points, shop/auto-return overlap and reconnect. Verify tutorial completion from actions, not a timer. No animation is allowed to grant money, materials, XP or a second rebirth.

All sample numbers and timings are proposals unless explicitly attributed to the recording. Only real build/device tests establish implementation or playtest status.

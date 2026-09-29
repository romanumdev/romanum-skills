# Tutorials and reward feedback

The supplied design guide describes an incremental game and reports observations from a video. Its companion [contact sheet and six stills](reference-index.md#destroy-the-moon-study-pack) are now included. The video and audio are not included in this skill; timing ranges below are prototype suggestions, not extracted measurements. Its guns, bag, selling and rebirth flow are project-specific examples, not default systems for every game.

## Point, act, acknowledge

Use one obvious target and a few words: highlight the actual control or object, point beside it, and advance when the relevant action really completes. Avoid opening paragraphs. Tutorial progress should follow game state rather than a timer; skip already-completed steps when the player acts ahead.

For navigation, use a world pointer or a short route of arrows. For a first-time menu action, a temporary dimming layer and live target highlight can help. Track the target as the camera, viewport or scroll position changes. Do not paint a fake target into a screenshot or cover the real hit area, price or skip control with the arrow.

Open the [00:41 frame](../assets/references/destroy-the-moon/references/t_41.00.jpg) for the bright button/white arrow against a dim scene, and [00:41.60](../assets/references/destroy-the-moon/references/t_41.60.jpg) for the following panel's explicit reset warning and before/after values. Borrow that visual clarity without inheriting its reset rules or multipliers.

When typewriter text fits the brief, start its pointer immediately and let players act while the text appears. A starting pace around 25-35 visible characters per second can be tuned in playtests. Keep line layout stable; [MaxVisibleGraphemes](https://create.roblox.com/docs/reference/engine/classes/TextLabel#MaxVisibleGraphemes) is available for native text reveal. Progress such as `8/10` should update separately without retyping the sentence.

Allow instant text reveal and skip where appropriate. Quiet typing clicks should stop on completion, interruption or line change, and respect sound settings. Keep current instructions opaque enough to read; use a subtle backing and fade the completed instruction away. Reduced Motion should preserve the next action without requiring shake, flashing or a moving pointer.

## Layer the feedback

| Actual event | Useful treatment |
| --- | --- |
| Accepted action or hit | Compact icon/number, local impact and quick sound |
| Collection | A few fragments/icons travel toward the player or counter |
| Level-up | Bar response, local burst and brief level label |
| Purchase/equip | Item preview responds and the actual equipped state changes |
| Major milestone | A stronger, bounded celebration with a quick/skip alternative |

Keep materials, Cash, damage and XP visibly distinct. Show the amount actually awarded. Merge rapid gains truthfully rather than flooding the screen with one label per event. Reuse and cap visual effects and overlapping sounds; frame rate and comprehension should survive fast progression.

Visual travel must not grant inventory or determine transaction success. Respond to the real state change; do not fake a sale, equipped item or multiplier for spectacle. Normal feedback should preserve gameplay visibility and control. Reserve full-screen effects for deliberate transitions, not every click.

Possible starting durations: press/release about 0.08-0.15 seconds each way; gain feedback about 0.5-0.9 seconds total; a local level burst about 0.6-1.0 seconds. Tune them in motion on the target device. These values describe a starting feel, not universal rules.

## Review in motion

Try rapid gains, multiple levels, opening a shop during the tutorial, skip, death/reset and rejoin. Check that pointers stop targeting closed or missing controls, audio stops with its text, and repeated events do not duplicate rewards. Inspect actual phone input and controller navigation. An optional reviewer can compare screenshots to the concept, but screenshots alone cannot verify sound, timing or responsiveness.

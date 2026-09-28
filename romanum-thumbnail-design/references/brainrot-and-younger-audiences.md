# Brainrot and younger-audience thumbnails

Use this guide when the game's audience and visual language fit it. It is not the default art direction for every Roblox game. Familiar starter avatars, exaggerated reactions and progression contrasts are creative hypotheses here, not proof of higher CTR.

## Art direction

Prefer a polished Blender-style Roblox GFX render. Preserve blocky anatomy and recognisable hair while giving characters and props real volume, posed silhouettes and coherent perspective. Use a clear key light, soft bounced fill, contact shadows and restrained ambient occlusion to ground the scene. Rim light can separate the silhouette when useful. Give plastic, hair, cloth, metal and food appropriate roughness and highlights rather than making every surface equally glossy.

Keep the Roblox face graphic readable on the 3D head. Bright colours and exaggerated expressions do not require flat cartoon shading, illustrated contours or a 2D comic treatment. Reserve those styles for a matching brief or game art direction. Rainbow text and reward effects can sit over the rendered scene without changing its underlying style.

Use strong colour separation around the face and gameplay object. A bright sky and studded ground can work when they belong to the game; do not impose them on a different setting.

Keep one main moment. Usually one or two characters are enough. Simplify background geometry before adding glow, arrows, outlines or labels. Polished does not have to mean realistic skin, cinematic darkness or excessive depth of field. Do not humanise the avatars into teenagers, reshape their hands into realistic fingers, or turn a reference into a pasted sticker. A thin separation edge can help; thick comic borders should be a deliberate style choice.

The output should feel like a readable moment from this particular game. Do not add an obby, fight, conveyor, pet or money mechanic merely because another successful game uses it.

## Character and emotion

Read [the reference pack](characters.md) and attach the relevant originals to the image tool.

- **Bacon hair:** preserve the layered brown hair, black open jacket, blue shirt, dark trousers and white shoes. Change pose and emotion to match the action.
- **Acorn girl:** preserve the reddish-brown tied bun and fringe, blue jacket, light striped shirt and muted reddish trousers. "Acorn" names the avatar hairstyle; never generate an acorn-shaped head or costume.
- **Wicked grin:** use the separate close-up for the broad toothy smile, asymmetric brow and knowing eye contact. Its narrowed eyes should read as deliberate mischief, not drowsiness. A forward posture, engaged gaze and brow tension help. This reference controls expression, not the outfit or camera framing.

Relaxed, half-lidded eyes can be intentional in the supplied smug expressions. Do not automatically replace them with wide eyes; judge the whole face and pose against the requested emotion.

Choose emotion from the moment: smug anticipation while setting a trap; wide-eyed alarm as it activates; delight at a rare reveal; determination while recovering. A random open mouth is not a substitute for a clear intention. Keep the eyes and mouth visible and large enough to read on a phone.

Character rivalry can make the story legible. Either avatar may win, lose, prank or recover. Keep the conflict about the actual game action; do not make gender superiority, humiliation or pressure to "prove" one's gender the reason to play. A single character can work just as well when the action carries the story.

## Concept families

Choose based on the game's actual loop, not a fixed template:

| Concept | Visible story | Useful when |
| --- | --- | --- |
| Mischief / outplay | Character sets up a readable trick; another may be about to encounter it | Traps, stealing or deception are playable mechanics |
| Near miss | Pose, prop and destination make success or failure imminent | Balancing, escaping or transporting is central |
| Progression | Beginner and upgraded states differ in one instantly readable way | The pictured upgrade exists |
| Reveal | One reward or creature dominates; the character reacts | Discovery or collecting drives the loop |
| Clear action | One character performs the main verb in its setting | The game needs its premise explained quickly |

For a concept about a conveyor trap, the conveyor establishes the setting, a wicked grin establishes intent, and a hand placing a clearly recognisable toy trap establishes the action. Keep the trap and hand unobstructed. This is an example brief, not an assertion about a real game. Do not add unrelated weapons, cash values or rarity labels.

For a cake-delivery game, a doorstep, unstable cake and panicked carrier could deliver the same three reads. The transferable lesson is the structure, not the cake, town or winner's gender.

## Numbers as the gameplay hook

These treatments can explain an incremental or collecting loop quickly. Select one main hook; supporting reward pop-ups may reinforce it. They are options, not mandatory decorations or measured audience preferences.

| Pattern | What it communicates | How to compose it |
| --- | --- | --- |
| `+1 +1 +1` | Repeated gains from a tap, movement or another action | Put a few separate pop-ups beside the object or action producing the gain; vary their height or scale to suggest a sequence |
| `67T/s` or `67QT/s` | A spectacular production rate | Make one large rainbow rate label near the producer or in clear headroom, with the object and face still prominent |
| `DAY 1` / `DAY 999` | Beginner-to-advanced progression | Show the same loop or object at two clearly different stages: size, equipment, environment or reward changes; the labels support a visible transformation |
| `1 in 9,999,999` | A rare discovery or collectible | Pair one readable rarity label with one dominant reward and a reaction or reveal; use rolling/egg-opening imagery only when that mechanic belongs to the game |

Treat a floating `+1` as game feedback: it should visibly come from something. A rate badge without a producer, or rarity text without an identifiable prize, leaves the core action unclear. Repeated `+1M` can support an income scene, but do not scatter pop-ups evenly over every part of the image.

Use bold, rounded lettering, a clean dark outline and enough spacing to retain each digit at mobile size. Rainbow fills can move across the letters or digits while the outline holds them together. A small shadow, highlight or glow can separate text from the scene; keep those effects away from the eyes and the main interaction. Text outlines are useful here and are distinct from adding thick sticker borders to every character.

Write the requested notation exactly, including commas, plus signs and `/s`. `T` and `QT` are different strings; do not silently swap them. Use the game's supplied number formatting. Keep only one dominant numerical headline, or a paired headline for a before/after layout. Use a simple sign panel or open sky if the scene is too busy behind the text.

In concept work, requested example numbers can be used as illustrative labels; record that status in the brief rather than adding a disclaimer to the artwork. For a release asset, use the developer's confirmed rates and odds. `DAY 1` / `DAY 999` can be a stylised early/late-game comparison; it does not by itself establish a literal calendar or a time-to-reward claim. In-game currency effects should read as in-game rewards, not a promise of free Robux or cash.

Study the relevant [visual examples](visual-examples.md) before choosing a text treatment. They illustrate these choices; they do not replace the canonical character references or prove that a mechanic exists in the current game.

## Prompt scaffold

Fill only what matters; omit empty labels.

```text
Asset: 16:9 Roblox discovery thumbnail / square game icon.
Game truth: [actual setting and player action].
Moment: [one visible action and its immediate consequence].
Feeling: [what the player should expect to feel].
References: [image -> identity / outfit / expression / setting role].
Character: [canonical identity, pose, gaze and expression].
Composition: [main subject, action, supporting reaction, camera].
Render: polished Blender-style Roblox GFX, posed blocky avatars, dimensional materials, coherent lighting and contact shadows; adapt if the brief specifies another style.
Text: [exact strings, colour/outline, placement, hierarchy and any repeated pop-ups; or none].
Number meaning: [increment / production rate / progression / rarity; confirmed value or illustrative concept label].
Preserve: [identity and scene invariants for this generation/edit].
Avoid: [the few likely errors specific to this scene].
```

## Review and testing

Inspect the actual image at full and small size. Can a viewer describe where they are, how the character feels and what the character is doing without reading a caption? Does the hand touch the intended object? Are both faces recognisable, or has the supporting character become a distant speck? If the scene needs an explanation, simplify it or bring the action closer.

For numerical hooks, also read the text back: check every digit, comma, suffix and repeated label. The intended headline should read before decorative pop-ups, and neither should hide the emotion or gameplay object. On a square icon, reduce the number of labels rather than squeezing in the full thumbnail layout.

For broad concept exploration, change the moment, camera or focal subject. For measured variants, isolate the intended change: for example, the same scene with a grin versus alarm. Do not present an aesthetic judgement as predicted CTR. Compare real results within a comparable audience and placement when those results become available.

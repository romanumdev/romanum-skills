# Motion and interaction contract

## Tunable starting points, not recovered source constants

Use these values to build a first preview. Tune against the reference and the project's own approved treatment; no single setting is mandatory.

| Channel | Proposed starting range | Evidence relationship |
| --- | --- | --- |
| Old-copy clear | 80–140 ms opacity fade | Source clears old copy quickly, separately from the body |
| Ordinary body retarget | 220–340 ms eased width/height interpolation | Source changes fit over a few tenths of a second; large body wobble is not established |
| First reveal offset | 30–90 ms after copy is cleared; may overlap body settling | Source reveal follows a short clear interval |
| Glyph start interval | 25–40 ms | Close video samples suggest a few 60 fps frames per new glyph |
| Glyph arrival | 170–240 ms; opacity 0→1, small-to-final scale, upward settle | Source frontier is small/faint and rises into place before becoming calm |
| Glyph rise | About 0.20–0.35 of the cap height | Starting approximation from the observed small rise; scale responsively rather than hard-coding screenshot pixels |
| Glyph overshoot | Optional, restrained; 1.03–1.08 scale or slight vertical overshoot | Slight leading-glyph over-peak is visible; do not make every letter a large bounce |
| Authored emotional hold | 350–550 ms | The surprised name/exclamation has a pronounced visible beat |
| Modal entrance | 420–600 ms, one spring settle; about 1.08–1.10 peak scale | Source reward plate has approximately 9% overshoot and a small undershoot |
| Modal copy offset | Start after the dominant entrance motion, roughly 250–400 ms after entry begins | Copy begins after the plate is nearly settled |
| Hover/click response | 100–180 ms hover response; small 150–300 ms accent burst | Visible enlargement and short click marks; exact timing not recovered |
| Modal exit | 220–360 ms opacity + modest shrink | Source visibly fades/shrinks and restores the scene |

Ordinary bubble entrances/exits are less clearly demonstrated than copy swaps. If a flow needs them, start with a modest fade and restrained scale/translation. Do not claim that the clip establishes an entrance constant or require the modal's large overshoot everywhere.

## Separate models and clocks

Keep message content, presentation layout, animation and progression distinct:

- Content: speaker, localized text, semantic spans, explicit pauses, reaction cues and the event/choice that advances it
- Layout: completed line boxes, glyph/range positions, measured width/height, width limit, padding and speaker anchor
- Presentation: hidden/entering/revealing/holding/exiting, current visible count and current geometry
- Progression: gameplay state and user/event inputs; successful gameplay and rewards remain authoritative outside the animation layer

Use one active generation or cancellation identity per presentation. Replacement invalidates the previous identity before starting new scheduled work. Every delayed callback checks it. Cancelling must settle or dispose of all associated glyph arrivals, pauses, sounds, face/pose callbacks and completion work. Disposal and completion are idempotent.

## Transition recipe

1. Resolve localized copy and semantic spans; produce a native-shaped final layout at a bounded readable size
2. Stage the new layout in a separate hidden layer, or fade old copy before changing the active label. Commit new copy while hidden so cached text cannot flash on re-entry
3. For a line swap, retain the body/badge/connector while old copy clears; retarget body geometry from its current displayed size
4. Reveal into the fixed final line positions. Space and markup consume no spurious visual labels. Each arriving visible unit gets its local settle, then becomes still
5. Apply pause metadata at authored semantic boundaries. Do not enforce long pauses after every period, comma or exclamation by default
6. Hold the finished message until its approved user/event progression trigger occurs
7. On skip, finish current geometry/text/emphasis immediately, stop queued reveal sound and preserve the current message until the appropriate next input/event
8. On close/replace/destruction, invalidate all callbacks and release input ownership; restore any backdrop effects this presentation owns

The source demonstrates independent, short glyph animations. Implementation need not allocate a permanent object or coroutine for every character. Reuse/pool presentation resources where useful, but optimize only after preserving shaping and layout.

## Layout invariants

- One final line layout per localized message/viewport constraint, not per visible substring
- Full-body width/height measured from actual final rich text and padding; never count bytes as a pixel measure
- A fixed chosen anchor during retargeting; badge and connector reposition from current body geometry
- Keep the text viewport at its measured final size while the body retargets. Do not bind wrapping width or text scale to the tweening body. Preserve final positions relative to the chosen anchor, with clipping clearance for glyph rise/scale
- Per-glyph transforms cannot alter neighboring advances or wrap decisions
- Long text is paginated/reflowed at a readable size; do not silently shrink it into an unreadable stamp
- Resizing or font loading changes rebuild safely from the final content without duplicating progression
- Semantic emphasis survives line breaks and translated word order; do not save English byte offsets as localization-independent ranges
- Shaping-sensitive scripts retain native shaping. If independent glyph rendering breaks ligatures, bidirectional layout or emoji sequences, use a native reveal/fade fallback rather than splitting the string incorrectly

## Production checks

Compare both stills and real-time motion, including the reveal frontier and transitions. Verify:

- One-line → two-line, two-line → one-line and unequal-width swaps: no jump, clipping or whole-paragraph squeeze
- Reveal → immediate replace, close during a long pause and rapid repeated input: no stale text, delayed reappearance, doubled sounds or duplicate completion
- Skip near the final glyph: first input finishes current text; advancement follows the flow's deliberate next trigger
- Current speaker moves or exits camera: stable orientation, intentional visibility/distance rules and no reveal restart
- Combined accents, emoji sequences, long names, translations and right-to-left/connected scripts: valid shaping and predictable line breaks
- Touch/controller/keyboard and narrow viewport: reachable input, readable font and safe placement
- Reduced motion/instant text: equivalent information/progression without rise, bounce or forced waiting
- Modal opening/closing: focus is owned, covered gameplay cannot accidentally advance, backdrop restores correctly
- Optional audio: user-controlled volume, bounded/polyphony-safe delivery and complete cancellation on skip/close; audio is supplemental

Report runtime tests as passed, failed or not run. A valid skill package is not proof that the application renderer works.

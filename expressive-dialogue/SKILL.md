---
name: expressive-dialogue
description: Design or implement soft, expressive in-game dialogue with stable content-fit bubbles, animated text reveals, semantic emphasis and synchronized character reactions. Use for NPC dialogue or dialogue-like reward modals; not ordinary chat writing or generic UI animation.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Expressive Dialogue

Make dialogue feel spoken through coordinated layout, motion and character performance. The distinctive effect is a stable bubble whose copy softly clears, whose dimensions adjust to the next complete message, and whose new letters gently arrive. Preserve the project's approved art direction, font and assets. Reference motion is inspiration, not permission to replace Romanum's visual identity or copy another creator's assets.

## Choose the target

Inspect the current dialogue flow and supplied reference pixels before changing implementation. Establish the speaker anchor, approved bubble treatment, final text, semantic highlights, progression trigger and whether the user wants a world bubble, a screen panel or a reward modal. Infer ordinary details from the existing project; ask only for decisions that affect the outcome.

For this skill's source-grounded design, read [reference-teardown.md](references/reference-teardown.md). It distinguishes visible observations, approximate video measurements and proposed settings. When implementing, read [motion-contract.md](references/motion-contract.md); for Roblox, also use [roblox-notes.md](references/roblox-notes.md).

## Build the effect

- Resolve the final localized text and semantic spans before measuring. Measure the complete message with the actual font, line spacing, emphasis and width limit. Reserve its final line breaks and glyph positions before revealing anything; keep its layout viewport independent of the tweening body. Center completed lines within a content-fit body; growing visible prefixes must not recenter or rewrap settled letters
- Keep speaker badge, body and circular connector visually coherent during width/height changes. Preserve the chosen anchor while resizing. Separate speaker tracking from reveal animation so camera or character movement cannot restart the copy
- On a line change, fade old copy, smoothly retarget the body to the next measured size, then reveal new copy. Keep the container present across an ongoing exchange. Retarget an interrupted resize from its current visual state; do not stack competing tweens or flash cached text
- Reveal graphemes, not bytes. Give each arriving glyph a short opacity/scale/rise settle while previous glyphs become still. The visible frontier should be soft; persistent whole-paragraph waves are unnecessary unless requested
- Author brief pauses for important beats. A surprised name followed by a hold is more expressive than slowing every character. Keep color and underline attached to semantic spans through reveal, wrapping, skip and localization
- Synchronize face/pose changes with the event or speech beat. Give reactions a readable onset, hold and recovery. Do not infer gameplay success or award progress from an animation finishing
- Keep gameplay legible. Floating dialogue belongs near its speaker; instruction text and tool feedback can occupy separate calm regions. Use a dim/blur backdrop and larger entrance only for an approved modal. Distinguish camera motion, scene-edit fades and interface animation

## Interaction and delivery

During reveal, a deliberate advance first completes the current message; a subsequent input advances if that flow requires it. Keep event-driven dialogue event-driven. Support immediate/reduced-motion text, readable contrast and a text equivalent without requiring sound. Cancel scheduled glyphs, pauses, sounds, reactions and completion callbacks when replaced, closed, skipped or destroyed. Repeated completion must be harmless.

Test one-/two-/three-line swaps, rapid replacement, close during pause, skip at every stage, long/localized text, combined-character/emoji sequences, viewport changes and moving speakers. For shaping-sensitive scripts, retain native text shaping; a per-glyph renderer must prove correct output or fall back to native reveal.

Deliver the requested design or implementation with a brief visual check against the reference and approved project assets. Report measured facts separately from tuning proposals and state which runtime checks passed. This skill does not authorize publication, deployment, external communication or asset redistribution.

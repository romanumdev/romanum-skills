# Reference teardown: derpitect's cozy Roblox systems demo

## Source and evidence standard

- Creator: derp (@derpitect)
- Original post: https://x.com/derpitect/status/2107287986404475006/video/1?s=46
- Original context: a cozy Roblox game systems showcase covering NPC dialogue, archery and cutscenes
- Official X media metadata: https://cdn.syndication.twimg.com/tweet-result?id=2107287986404475006&lang=en&token=0
- Inspected rendition: official 1920 × 1080 MP4, nominal 60 fps; video metadata gives 78.483 seconds, container duration is 78.528 seconds

Actual source playback and downloaded frames were inspected. Close reveal samples use the original 60 fps frame sequence; wider sequences use 0.1- or 0.2-second samples. Timestamps are approximate, normally within one sampling interval. Compression, camera movement and fades limit pixel measurements. No source code was inspected: easing names, exact tween constants and renderer architecture are not known. Audio exists in the file, but its sound was not inspectable in this review; no typing-sound or music claims are made.

This portable package contains analysis and original instructions, not the original clip, fonts or textures. Use the creator's linked post as the visual source.

## The visual grammar that is actually visible

The NPC bubble is a compact, cream-white, heavily rounded rectangle above the speaker. Its interior has faint, regularly spaced round spots; these are low-contrast graphic marks rather than dense random noise. The edge reads softly luminous, without a hard dark border. A small coral-pink `NPC` badge overlaps the top-center edge. A separated white circular connector sits below the body toward the speaker, rather than a conventional sharp triangular speech tail. The badge and connector remain associated with the body as its geometry changes.

The body text is dark, thick, rounded and slightly irregular in feel. Two-line copy is centered by line, with deliberate padding and comfortable leading. The exact font and source asset are unidentified. A player's name is cyan-blue and underlined; important action/object words such as `bow`, `target`, `draw` and `loose` become green; `gift`/`gifts` become pink and underlined in the reward flow. These highlights are embedded in the sentence, not separate chips. The final punctuation retains its sentence role.

The background is a bright, open 3D scene with orange/pink/green trees and red, cyan and orange targets. The actual attraction is a coherent combination of playful letterforms, quiet cream surfaces, selective color and small movement. Copying only “rounded card plus typing” would miss most of that character. Romanum should keep its approved illustrated assets and thematic typography, adapting the interaction grammar instead of importing this game's art.

## Timeline: dialogue behavior

| Approximate time | Visible event | Interpretation and limit |
| --- | --- | --- |
| 0.00–0.10 s | An archery frame cuts to an NPC conversation already displaying a complete greeting | This is an edit boundary, not evidence of a bubble entrance |
| 0.10–1.23 s | Complete greeting holds; the player turns toward the NPC | Settled text is calm. The bubble tracks the speaker/world composition |
| 1.27–1.33 s | Old greeting fades almost completely while body, badge and connector stay | Copy replacement is separate from container lifecycle |
| 1.36–2.55 s | A new two-line instruction reveals from left to right within its final line positions | Character/grapheme progression, not whole-word replacement. The body smoothly narrows to the new content fit |
| 1.37–1.60 s, close-up | Leading glyphs are faint and small, rise/grow into place and settle; earlier glyphs become dark and still | This is animated glyph arrival, not merely toggling character visibility |
| 2.5–7.5 s | The finished instruction holds | No convincing evidence for a permanent sine-wave animation across completed copy |
| 7.53–7.67 s | Instruction clears and body retargets for a new sentence | Container persists; dimensions are determined by the next message rather than each visible prefix |
| 7.67–8.85 s | New two-line instruction reveals; `bow` is green | Semantic emphasis participates in the same reveal |
| 11.27–11.75 s | Brief near-black scene fade leads to another already-completed NPC line | Treat this as showcase editing; do not implement a blackout for every dialogue change |
| 14.10–15.45 s | New two-line bow instruction reveals during a third-person-to-first-person camera move | Text reveal and camera transition overlap without replacing the speaker bubble |
| 17.35–18.25 s | NPC changes to a distressed expression and defensive raised-arm pose; old text fades, then a short one-line protest reveals | Speech/body reaction share an event. The shorter bubble becomes shallower |
| 20.85–21.85 s | The protest clears; a narrower two-line instruction reveals while the smile/neutral posture recover | Width and height can change in opposite directions; do not uniformly scale the entire old paragraph |
| 24.55–26.05 s | Explosion begins; the NPC falls/recoils. Cyan-underlined name reveals first, holds, then the rest of the reaction continues | A deliberately separated emotional beat is visible |
| 24.70–25.45 s, close-up | Name and exclamation finish around 24.95–25.05 s; the next word starts around 25.43–25.50 s | Approximate 0.4–0.5-second hold after the exclamation. This does not establish a universal pause for every punctuation mark |
| 28.17–29.35 s | Follow-up sentence replaces the reaction and reveals over two lines | Same container-reuse and per-glyph grammar at a different speaker distance |

A small blue interaction/tool glyph appears separately near the character in several views. Its meaning is not proven by this clip; do not relabel it as a dialogue “next” button. No branching-choice interface or typing cursor is demonstrated.

## Text micro-motion and layout

At 1.3667 s the first new letter is barely present. By 1.4000 s the leading capital is visible and the following letter is faint. By 1.4667 s several letters have become dark while the next ones remain smaller/fainter. In this sample the leading capital reaches its high point around 1.50 s and has settled near its final baseline around 1.58–1.60 s. Its dark-pixel top moves approximately eight source pixels upward during arrival and returns approximately two pixels after the peak. Camera and container movement mean these are indicative, not a recovered animation curve.

Successive glyph starts appear a few video frames apart, roughly 25–40 ms in ordinary runs. Arrival takes longer than the start interval, so several arriving letters overlap in time. That overlapping frontier is what creates the soft rolling appearance. A single uniform opacity fade of the whole string would not reproduce it.

The text does not recenter around every freshly visible prefix. The first glyph already occupies the start of the final centered line, and the next line is reserved before its characters appear. The body moves toward a fit for the whole new message while text is being revealed. Once letters settle, reading position stays stable apart from speaker/camera tracking. Rebuilding layout from an ever-growing substring would introduce drift and late wrap jumps absent from the cleanest sections of the reference.

The body resize appears smoothly damped over a few tenths of a second. No large repeated spring wobble of the ordinary dialogue box is established. Keep the stronger overshoot for a more consequential transition such as the reward modal.

## Reward modal: the stronger motion mode

At roughly 51.90 s, the screen dims and blurs while a centered cream modal and small white flecks appear. Its silhouette is an asymmetrical, organic, lobed shape with shallow inward curves at top and bottom, not a generic pill or rectangle. It uses the same faint round-spot treatment as the bubble. The backdrop adds very quiet outlined tool motifs and a subtle patterned texture while the world remains visible behind it.

The modal grows rapidly, overshoots, undershoots slightly and settles before its body copy starts. In half-resolution frame measurements, the plate spans about 372 px at 52.05–52.10 s, about 328 px around 52.25–52.30 s and about 342 px around 52.45 s. That suggests roughly 9% scale overshoot and 4% undershoot. Thresholding/compression introduce small uncertainty. The meaningful rule is one readable spring settle, not those exact pixels.

Its orange confirmation button is visible early, while body text does not begin until around 52.23–52.28 s. The first message finishes around 53.35–53.45 s. This deliberate staging allows the shape's entrance to finish before reading begins. Pink-underlined reward emphasis uses the same character reveal language.

On hover, the orange button becomes larger; on the visible click near 55.20 s, small warm-colored marks burst briefly around it. The plate/copy then fade and shrink around 55.35–55.60 s. A new message plate enters, visibly overshoots around 55.80 s and settles near 56.00 s before its text fills. A second confirm near 58.00 s produces another small burst; the modal fades/shrinks away around 58.15–58.40 s and the world becomes clear again around 58.60–58.90 s.

The surrounding NPC dialogue continues to exist behind the modal. That is visible source behavior, not a recommendation to let players accidentally advance covered gameplay. A production modal needs explicit focus/input ownership.

## Character and hierarchy

The distressed expression, defensive arms and later fall make the character's reaction legible before all the words finish. Recovery has its own pose/face transition. The final demonstration, around 62–78 s, explicitly shows NPC head movement while the player/camera changes position: the head turns toward the player, and the floating dialogue remains upright/readable. The exact tracking limits, smoothing function and neck implementation cannot be determined from frames.

During first-person aiming, a vignette/dim treatment reduces background/HUD prominence. The bottom-center archery instruction occupies its own calm region, the selected arrow/tool UI remains near the aiming area, and the NPC's copy stays above the NPC. Menu/chat/hotbar/leaderboard regions remain around the edges. This is layered hierarchy, not one large all-purpose conversation panel.

## Evidence-to-design conclusion

Preserve five linked details when adapting the reference:

1. Stable, complete-message layout inside a softly retargeted bubble
2. Short overlapping glyph arrivals with a calm settled state
3. Semantic emphasis and explicitly authored emotional pauses
4. Event-timed face/body response and speaker tracking
5. A larger, staged spring entrance only for a meaningful modal

Do not infer exact easing constants, font identity, sound design or hidden progression logic from the clip. One re-entry around 50.72–50.80 s briefly shows old cached copy before the new reward sentence starts; treat that as a stale-content flash to prevent, rather than part of the desired style.

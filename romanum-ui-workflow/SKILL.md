---
name: romanum-ui-workflow
description: Design Roblox game UI through an imagegen concept, imagegen extraction of its individual assets, and editable native controls. Use for HUDs, menus, tutorial pointers, reward feedback and UI library reuse. Includes a stud-style simulator guide built around the Banana button reference.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Roblox UI workflow

Start with the player's task, device and reading needs. Carry the project's art direction and existing conventions through the work. Keep labels short and actions clear.

## Core workflow

**Imagegen concept -> visual review -> individual assets extracted with imagegen -> native Roblox UI -> in-game verification.**

For new visual UI, create the concept image before making its production art. Then give that actual concept to imagegen to isolate each needed piece. Written prompts are a valid handoff when generation is unavailable, but do not count as generated images. A contact sheet, programmatic crops of the mockup, or code-drawn approximations do not replace these two imagegen stages. Existing approved concepts and suitable reusable assets can satisfy work already done; preserve them rather than regenerating everything. A request to write a skill or review references alone does not authorise generation.

Request the concept and its individual assets in **one combined prompt** by default. Treat **eight output images per prompt** as this workflow's maximum, counting concepts and assets together: one concept plus seven assets, or two concepts plus six assets. Fewer is fine; do not add filler to reach eight. Include a compact output list and shared extraction instructions in the concept prompt, not a separate prompt for each asset. The receiving generator can create and inspect the concept, then extract the parts within the same request. Split sets larger than eight into batch prompts that reuse the selected concept. Eight is the project's batching rule, not a guarantee about every provider's capabilities; respect a lower actual tool limit.

For the bright stud-style direction, open [the Banana button](assets/references/banana-button.png) first and read [art direction](references/stud-ui-art-direction.md). Read [asset extraction and assembly](references/asset-extraction-and-assembly.md) when producing UI, and [tutorials and feedback](references/tutorials-and-feedback.md) for behaviour. [World style](references/stud-world-and-water.md) is optional context for maps and water; it is not a request to build a map. Use [the reference index](references/reference-index.md) to select other images without loading every file.

## When image generation is unavailable

Check the current session's actual tools, not just the model name. For Claude or any other model without usable built-in or connected image generation, explicitly ask the user to generate the UI images in an image generator. Provide one ready-to-paste prompt covering the concept and its individual assets, within the eight-image total; do not merely tell the user to find another tool. Follow [the prompt handoff](references/imagegen-handoff.md).

Ask for separate image files for the concept and each part. Do not require a user round trip between concept and assets when the receiving image-generation assistant can complete the combined request. If a material visual choice needs the user's input, return the concept for that choice. If a tool requires sequential operations, preserve the combined brief while adapting execution to its capabilities. Continue layout and behaviour planning while images are pending, and resume visual assembly when the actual files return.

## Reopen images after compaction

After every context compaction or handoff, reopen the reference images relevant to the current step, the selected concept, and any extracted assets being compared before continuing visual work. Do not reconstruct their appearance from a summary. Keep durable paths, reference roles, the selected concept version and the next unfinished step in the working handoff. If an image is unavailable, retrieve it or ask for it; do not silently substitute a remembered style.

## Find before generating

Search an available UI library for the screen or component, using its function and visual style. Inspect the actual layout, assets, supported devices, licence and attribution. Similar tags alone do not establish suitability. Reuse appropriate pieces and create only the missing ones.

If library access is unavailable, work from assets the developer supplied. Do not invent search results or claim a local folder is a connected marketplace. Permission to use a pack in a game does not necessarily allow sharing it or its edited images.

## Review a concept

Plan the necessary screen with a main action, information hierarchy and asset list. Use imagegen to render the complete concept against the intended gameplay background when available. Include a phone composition when mobile is in scope; do not just shrink a desktop screen. Use project-supplied copy and values, or clearly identified layout placeholders.

Review the actual image at the intended device size. Check labels, touch targets, hierarchy, gameplay visibility and whether the next action is obvious. Let the developer choose when a material visual choice remains open; when selection is already delegated, record the chosen render and continue. Stay within the authorised budget. If imagegen is unavailable, provide the prompt handoff above and clearly identify which images are still pending.

## Separate and assemble

Use the selected concept as an image input to imagegen for every extracted piece. Request one named asset per output, preserving its colour, shape, border, highlight and shadow. Independent pieces can be generated as a batch when the generator supports it. Extract button bases, panels, icons, pointers, non-stud textures and effects as separate files with real transparency where needed. Keep labels, prices, values and state changes editable in Roblox. Verify each asset against the concept; do not accept a freshly redesigned button as a faithful extraction.

For studs, use an actual user-provided texture or a verified licensed/owned library asset, as a separate native tiled `ImageLabel` layer. Never generate, redraw, bake in or model artificial studs, including on Roblox world assets. Imagegen panel/button artwork must omit studs and leave room for the real texture. The [supplied PNG and provenance](assets/textures/NOTICE.md) are available locally; inclusion does not establish public redistribution rights. Follow [the texture source, layer and fidelity checks](references/asset-extraction-and-assembly.md#stud-texture-layer) and record the source plus the real asset ID or pending upload status.

Make a manifest mapping stable keys to images and native components. Include dimensions, anchors, parent relationships and states. A library layout is structured data, not permission to execute uploaded scripts. Validate its hierarchy and reject unknown properties or executable content.

Use native `Frame`, `TextLabel`, `TextButton`, `ImageLabel` and `ImageButton` elements where appropriate. Supply real authorised Roblox asset IDs; do not invent IDs or report uploads before they succeed. A static Luau export is an artifact, not proof that Studio applied or tested it.

Use connected Studio tools only within granted permissions. Inspect the result on relevant screen sizes and check interaction, clipping, text fit and navigation. Publishing and destructive edits remain separate authorised actions. Distinguish what was created, applied and tested.

Independent subagent review is optional when the developer requests extra quality assurance or delegates that review. Give the reviewer the actual references, concept and implementation captures. It supplements visual and interaction checks; it is not a mandatory gate and cannot certify gameplay from a still image.

## Sharing

Private creation, analytics contributions and UI publication are separate choices. Never publish because someone enabled an unrelated data toggle. Show the selected licence and attribution, confirm rights for every source and derivative, and get explicit consent. Share only approved layouts and assets, not prompts, credentials, private statistics or source contracts.

Removing a listing stops new access through Romanum and may withdraw dependent listings. It does not undo licences already received or erase outside copies. Preserve attribution when reusing or exporting components.

## References

Roblox's [ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui) and [ImageLabel](https://create.roblox.com/docs/reference/engine/classes/ImageLabel) references define native objects. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) describes the optional community asset licence; it does not license Romanum's platform source or skill text. Verify the actual component's terms.

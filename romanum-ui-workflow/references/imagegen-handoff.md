# Handoff for models without image generation

Use this path when the current session has no usable image-generation tool, including Claude sessions without such a connection. Check actual tool availability rather than assuming capabilities from the model name.

Explicitly ask the user to make the UI images with an image generator and provide **one combined prompt** for the concept and extracted assets. For example:

> I don't have image generation available in this session. Please paste the prompt below into your image generator with the listed references. It requests the UI concept and its individual assets together. Return the resulting image files so I can check them and build the UI.

If a selected concept already exists, use it as the reference and request only the missing assets. A request to author this skill is not a request to generate a concept now.

## One prompt, up to eight output images

Treat eight as this workflow's maximum number of images requested in a single prompt. Count every concept, layout variant and asset image. For example:

| Requested set | Output count |
| --- | --- |
| One concept and seven assets | 8 |
| Two concepts and six assets | 8 |
| One concept and three assets | 4 |
| Existing concept supplied as a reference and eight new assets | 8 |

Use only the outputs the project needs. Eight is the developer's batching convention, not a verified universal platform limit. Respect a lower actual tool limit if encountered.

Write a finished, project-specific concept prompt, then include the asset-generation instructions directly in that same prompt. A short filename/description list is enough to identify the parts; do not write a standalone prompt for every item. Include:

- Game, screen, immediate player action, required controls and exact short labels.
- Target device, canvas/aspect ratio, composition and gameplay area to keep visible.
- The reference attachments and their roles, plus the intended typography, palette, border, depth and texture treatment.
- The total output count and a compact list of concepts and component files.
- Shared instructions to use the actual generated concept for extraction, preserve its design, keep text/values editable, and return separate images with real transparency where needed.

For stud-style UI, include the actual user-provided or verified licensed texture as a source reference and reserve a separate native texture layer. Do not request a generated stud tile or baked studs in any panel/button artwork. If the generator cannot preserve the supplied texture faithfully in the concept, use a flat surface and mark the texture preview pending native assembly. The sourced tile is reused, not a generated output slot. Read [the texture-layer rule](asset-extraction-and-assembly.md#stud-texture-layer).

Name the files the user should attach; a local path alone does not attach an image in another application. For the stud-style direction, identify the Banana reference as the button treatment and the gameplay screenshot as the layout context. Do not carry that palette into an unrelated project.

An illustrative combined prompt structure is:

> Create the complete UI concept described above using the attached references. Return eight separate images: one full concept, a primary button base, a secondary button base, a menu panel, a currency icon, a navigation icon, a progress-bar shell and its fill. Create and inspect the concept first, then use that actual image as the source for all seven components within this request. Preserve its shapes, colours, border weights, highlights and shadows. Component artwork must have no baked-in labels, prices or changing values. For stud-style UI, leave the panel/button faces stud-free for a separate native layer using the supplied real texture; do not invent, redraw or bake studs. Export each component as a separate PNG with true transparency where appropriate and padding for its shadow. Keep the concept as its own image; do not combine the outputs into a collage or sprite sheet. Return all eight images together, using the filenames listed below.

Replace the example inventory with the actual project's needs and include its complete visual brief and filenames before handing the prompt over. The example does not require every UI to have those seven assets. If two concepts differ, specify which one supplies the asset set so incompatible designs are not mixed.

Concept-first describes the order of work inside the request; it does not require two user submissions. Let a capable image-generation assistant complete the combined request. Ask for a concept decision only when a material choice remains with the user, not automatically between stages. A tool may execute multiple operations internally; one user-facing prompt does not imply one API call or simultaneous generation.

## When the set exceeds eight

Provide additional **batch prompts**, each requesting no more than eight output images. Put the concept and highest-priority assets in the first batch, then attach the selected concept to later batches for the remaining pieces. Do not waste later slots regenerating the concept or repeat the entire brief for every asset. For example, one concept plus ten assets can be requested as a first batch of one concept plus seven assets, then a second batch of three assets using that concept as a reference.

## Bring the files back

Ask the user to return the concept and extracted files together, preferably in a folder or ZIP with filenames preserved. Inspect the actual images, transparency and consistency before assembly. Supply a focused correction prompt only for missing or incorrect outputs; do not regenerate the whole set unnecessarily.

While the user generates the images, continue useful hierarchy, live-text, state and interaction planning. Mark production artwork as pending. Prompts and placeholders are not finished assets. Resume [native assembly and verification](asset-extraction-and-assembly.md) when the real files arrive, and reopen them after compaction.

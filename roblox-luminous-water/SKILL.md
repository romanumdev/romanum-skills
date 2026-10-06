---
name: roblox-luminous-water
description: Analyze a visual water reference or build luminous blue-cyan rolling water in Roblox, preserving the requested wave silhouette, surface detail, foam character, and gameplay readability. Use for stylized or stylized-realistic water art direction and implementation; not for generic fluid simulation or unrelated shader tutorials.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Roblox luminous water

Translate the reference's visible behavior into a feasible Roblox treatment. Preserve its art direction before optimizing. A vivid, gloss-rich, smooth swell is a different target from flat toon water, low-poly facets, or uniform white foam outlines.

## Establish the visual contract

Inspect the actual source pixels and motion when accessible. Use [references/lawral-reference.md](references/lawral-reference.md) for the original Tempest reference and its evidence limits. Separate:

- **Observed:** visible color families, large wave shapes, fine detail, glints, soft white patches, camera framing, and interactions actually shown
- **Creator-reported:** implementation or performance statements explicitly attributed to the creator
- **Inferred:** plausible explanation of a visible effect, with confidence and alternatives
- **Proposed:** the Roblox approach or new behavior being designed

Never convert cyan crests into proof of shallow depth, visible sparkle into proof of a specific shader, or a grid count into proof of EditableMesh versus bones. If the clip is unavailable, state that limit and request the clip/stills when they are necessary for a faithful match.

Determine the setting, gameplay camera, required swimming/boat/contact behavior, existing water implementation, and device target from supplied context or the project. Ask only for missing decisions that materially change the result. A reference preference does not authorize replacing an existing system.

## Preserve the important layers

Keep a compact art-direction contract with reference evidence:

1. Large, readable rolling silhouettes with secondary intersecting variation
2. Blue body/troughs and luminous cyan shoulders or crests
3. Fine surface detail clearly smaller than the swell
4. Sparse directional sharp glints, distinct from soft foam/spray
5. Foam activity motivated by selected crests or contacts, leaving blue negative space

For sheltered pools, adapt energy to the setting while keeping the palette and layered readability. Do not automatically flatten a hero swell or add ocean whitecaps to a quiet cave. Label the adaptation as a proposal.

## Choose supported Roblox mechanics

Read [references/roblox-recipe.md](references/roblox-recipe.md) when proposing or implementing the effect. Inspect the existing project before choosing among Terrain water, a skinned mesh, or EditableMesh. Reuse working art and architecture when they can satisfy the contract.

Use Roblox's documented material, texture, mesh, bone, particle, and beam features. Do not invent a user-authored GPU shader pipeline, depth-buffer sampling API, or a SurfaceAppearance UV-offset property. Validate current API availability and experience prerequisites before depending on dynamic mesh/image features.

Keep cosmetic deformation separate from authoritative water interactions. Use the same defined wave/height sampler for visible attachments and gameplay probes when they must agree; verify coordinates and displacement rather than trusting undeformed mesh collisions.

## Validate proportionately

For analysis, deliver a source-linked breakdown and feasible implementation choices; no engine tests are needed to claim analysis completion. For implementation, use a small representative slice before expanding across the map:

- Compare a low/grazing view and the real gameplay view in stills and a short motion capture
- Check silhouette, blue-cyan value separation, detail scale, glints versus foam, and character/attack readability
- Exercise only interactions in scope, such as shallow entry, swimming, a rock edge, or a boat
- On targeted mobile hardware and low graphics, compare water-on against water-off frame time, memory, and visual readability; test LOD transitions and repeated cleanup
- Diagnose the demonstrated failure; do not impose an unrelated production test suite on a small visual change

Record what passed, what is untested, and remaining art/performance tradeoffs. Return the full artifact or changed files with attribution. Keep the original source clip, frames, and textures out of the reusable skill package; link to the creator instead.

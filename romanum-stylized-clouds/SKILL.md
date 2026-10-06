---
name: romanum-stylized-clouds
description: Design, implement, or review a stylized Roblox sky with sweeping curled cloud silhouettes, soft volume, selective bright rims, clear sky gaps, and day-to-night palette changes. Use for cloud art direction and source-fidelity work; not general weather simulation or cloud hosting.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Stylized Roblox clouds

Preserve the cloud shapes before adding motion or technical complexity. This skill adapts Josh Audia's sky reference into original project work. It does not reproduce his private algorithm or supply cloud assets.

Read [cloud-reference.md](references/cloud-reference.md) for observed samples, creator statements, implementation choices, and their limits.

## Set the visual contract

Inspect the current sky, approved environment art, gameplay camera, day/night system, and target devices. Keep working systems when they can meet the requested result. A liked reference does not authorize replacing the sky or adding a day/night mechanic.

Record the features that matter:

- Broad sweeping cloud masses with curled tips and smaller wisps
- Soft internal volume with curved painterly shading
- Narrow bright rims on selected edges, rather than a uniform glowing outline
- Large overhead forms and smaller horizon bands with generous clear sky gaps
- A coherent palette for the requested times of day

Keep observed source behavior separate from creator-reported methods and proposed implementation. The demonstration accelerates its clock. Do not use its apparent motion as a measured gameplay wind speed.

## Choose a feasible treatment

Use the existing supported rendering path first. Native Roblox Clouds can provide a broad cloud-cover baseline; its standard controls do not guarantee the reference's authored curled silhouettes. If closer shape control is needed, propose original approved images or geometry and explain the camera, lighting, transparency, and asset tradeoffs.

Do not prescribe an undocumented custom GPU shader API or assume the creator used a skybox, mesh, billboard, or particular noise function. Follow the project's approved asset-authoring workflow. Record asset ownership and permitted destinations; the reference post is not an asset license.

Block out a few readable masses and sky gaps. Review horizon and upward views before adding wisps. Then tune soft body shading, selective rims, and palettes. Keep the horizon distinct from landmarks and preserve character and combat readability.

Use calmer gameplay drift unless the requested scene needs stronger motion. Separate cloud movement from clock speed. When a day/night system is in scope, interpolate the approved palettes smoothly through its existing state. Avoid synchronizing every cloud into identical motion or using dense transparent layers to hide weak shapes.

## Review and hand off

For analysis, return the visual contract and feasible choices. For implementation, inspect an actual normal-speed runtime capture and paused horizon/upward views. Check silhouette, sky gaps, rim restraint, palette transitions, smooth drift, camera seams, and foreground readability.

Measure a representative low-graphics/mobile tier against sky-off frame time and memory where the target hardware is available. Preserve the main masses and gaps while reducing wisps, transparent coverage, and update work. Check repeated loading, cancellation of transitions, and cleanup of owned instances and connections.

Deliver the requested design or changed files with source attribution. State which render and device checks passed and which are pending. A validated skill folder is not a tested sky implementation or permission to install, publish, or deploy.

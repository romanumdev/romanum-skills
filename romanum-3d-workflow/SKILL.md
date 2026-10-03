---
name: romanum-3d-workflow
description: Create or refine Roblox-ready 3D assets in Blender from coherent object references, blockouts and materials, then compare actual model renders with the selected design. Use for props, meshes and reference-based modelling; written briefs remain plans when modelling tools are unavailable.
license: "Romanum Source-Available License 1.0; see LICENSE or https://github.com/romanumdev/Romanum/blob/main/LICENSE. Commercial project outputs are permitted."
---

# Roblox 3D and Blender workflow

Start with the asset's role, approved design, target scale, visible views and project constraints. Inspect supplied references and any existing model before changing it. Preserve the project's art direction and editability; save a separate working version when revising existing work.

## Establish one coherent object

Choose enough views to resolve the shape. Front, back, side and three-quarter views are useful for complex or asymmetric objects; add the opposite side or top when needed. A simple symmetric prop with clear dimensions may need only one or two references. Reuse supplied views first; additional reference generation needs available tools and an authorised budget, not a mandatory four-image purchase.

Record reference paths/version, view labels, proportions, feature positions/counts and materials. Additional views must depict that same object, with only the camera changing. Generated unseen surfaces are proposed design, not evidence of the original. Before detailed geometry, reconcile conflicting proportions, handedness, features or materials against the approved source; correct a drifting view or seek a decision when the disagreement changes the design. Do not average incompatible views into a new object. Read [reference-to-model checks](references/reference-to-model.md) for ambiguous or multi-view work.

Mark unresolved surfaces explicitly. Use symmetry or plain continuation only when supported by the brief/references, and disclose the assumption. Keep disputed features pending with a reversible plain blockout; do not invent unseen vents, ornaments or mechanisms. Unresolved surfaces prevent a claim of complete faithful reproduction; a labelled partial model can still be delivered. When original design is delegated, record the chosen design and keep it consistent across views.

## Build, render and compare

Check a blockout's dimensions, landmarks and silhouette against the set before detail. Then refine geometry and materials while preserving the selected design. Use the project's actual mesh/texture budgets and export requirements rather than invented universal targets. Read [Blender delivery](references/blender-delivery.md) when editing or exporting a model.

Render from cameras corresponding to the references at comparable scale. Open and inspect the actual render files: compare silhouette, proportions, feature placement/count, handedness, material boundaries and finish across the relevant views. A pleasing three-quarter view alone does not verify the back. Correct mismatches and re-render affected views. A saved .blend, successful script or export does not prove visual fidelity. If rendering or inspection is unavailable, report that check as pending.

## Preserve quality when delegating

Keep any explicitly selected model. For quality-critical reference interpretation, geometry, composition and materials, inherit the parent model by default; do not silently switch these tasks to a cheaper or lower-capability model. Use a stronger model only when available and authorised; otherwise continue with the current model. This is a workflow preference, not a universal benchmark ranking, and model generation numbers alone do not establish task quality.

Mechanical extraction, file conversion or validation can be delegated separately when appropriate. Supply the actual sources and check the returned outputs against them. If conversion can change geometry, normals, UVs or materials, perform the corresponding geometry and render checks; conversion success alone is insufficient. The main agent remains responsible for the assembled model and final visual comparison.

## Tools, permissions and handoff

Inspect the session's actual Blender/modelling/rendering capabilities; this guide does not install or connect them. When tools are unavailable, deliver a precise plan or script and identify unexecuted steps. Paid generation, installations, uploads, live Studio changes and publishing need their applicable authorisation. Do not invent asset IDs or claim a model was applied or tested from a static export.

Deliver the editable source, authorised exports and actual render paths, with scale/orientation, reference version, design decisions, unresolved areas and completed/pending checks. Retain those files and reopen the relevant images after compaction or handoff.

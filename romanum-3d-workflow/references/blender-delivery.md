# Blender editing and delivery

Read this when actually editing or exporting. Use the available Blender version and tools; do not assume a connected Blender or Studio service merely because this guide is installed.

## Working model

Inspect the existing scene, object hierarchy, dimensions, modifiers, materials, UVs and external dependencies relevant to the requested asset. Save a separate working version and edit only the agreed object/collection. Keep source geometry and useful modifiers editable; destructive conversion should serve an actual export requirement.

Establish project scale and orientation early. Build a blockout, compare actual renders with the selected references, then refine. Use existing project polygon/texture constraints; if none are supplied, choose a modest, stated working assumption and confirm material constraints when they affect the design. Avoid hidden geometry or tiny details that add cost without affecting the intended views.

Check the asset's silhouette, shading/normals, intersections, material assignments and texture dependencies at its intended viewing distance. UVs and texture work must preserve the approved appearance. Do not replace a specified finish with a generic material merely because it is available.

## Export and handoff

Use the requested format and the project's actual Roblox import convention. Check dimensions, orientation, pivot/origin, texture paths and the visible result after export; inspect an offline reimport when practical. Apply transforms or modifiers only as needed for that export and preserve the editable source. Exporting is separate from uploading or applying the asset to a live place.

Deliver the .blend source, authorised exports and render files together with a small record of reference version, scale/orientation, materials/dependencies, remaining assumptions and verification status. When an importer or Studio session is unavailable, identify that limitation rather than claiming native verification. Reuse the reference and render comparison procedure in [reference-to-model checks](reference-to-model.md#compare-blockout-and-final-renders).

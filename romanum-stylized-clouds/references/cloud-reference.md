# Josh Audia stylized-cloud reference

## Source and review limits

- Creator: Josh Audia, @ThisIsTamely
- Original: https://x.com/thisistamely/status/2107268097422094746
- Reviewed: October 6, 2026
- Evidence: actual source frames at approximately 2.89, 11.89, 27.25, and 42.30 seconds, representing morning, day, evening, and night

The samples establish appearance and changing composition. They do not recover exact keyframes, cloud speed, normal gameplay timing, geometry, textures, or an algorithm. The reusable package contains no source clip, extracted frames, or creator assets.

## Observed appearance

- Broad sweeping masses have curled tips and smaller wisps. Curved painterly streaks carry internal shading
- Softly shaded bodies have selected bright narrow rims. The contours read as sculpted volume without sharp polygon edges
- Large forms occupy the overhead sky. Smaller bands sit lower, with broad clear gaps between forms. Visible layering does not prove separate geometry layers
- Day uses white and pale cyan clouds against saturated blue. Morning adds lavender and pink. Evening shifts toward gold and peach against magenta. Night uses blue and violet against a near-black sky
- Contours and positions change alongside the sun, moon, and palette. The clip shows an accelerated demonstration, not a measured normal-speed wind reference

## Creator-reported context

The post describes procedural clouds with a day/night cycle. In a [motion reply](https://x.com/ThisIsTamely/status/2107272084091273252), Audia says clock acceleration affects the demonstrated movement. A [technical reply](https://x.com/ThisIsTamely/status/2107283851001438657) describes 16 parallel CPU workers, work batches spread across frames, and interpolation between old and new positions.

These are attributed claims, not inspected source code or a tested Romanum implementation. The worker count is not a portable performance budget. A plugin release was conditional; the reviewed post did not supply a released asset or license.

## Proposed implementation choices

Choose from the current project and visual target. None of these choices establishes the creator's method.

1. Use an existing cloud system when its shapes and palette can satisfy the contract
2. Use native dynamic Clouds for a broad-cover baseline. Roblox documents Cover, Density, Color, and Enabled. Dynamic clouds render under Terrain, and global wind controls their motion. Lighting and Atmosphere also affect their appearance. These controls do not alone promise authored curled silhouettes. See [dynamic clouds](https://create.roblox.com/docs/environment/clouds) and [Clouds API](https://create.roblox.com/docs/reference/engine/classes/Clouds)
3. For stronger shape control, author a small original image or geometry vocabulary through the approved workflow. Review projected silhouettes, transparency, parallax, seams, lighting response, and overdraw before expanding it
4. Coordinate the sky with the existing atmosphere. Atmosphere affects distant visibility, haze, and color; use it to support the composition without obscuring landmarks. See [atmospheric effects](https://create.roblox.com/docs/environment/atmosphere)

Official technical sources were checked October 6, 2026. Recheck the relevant API when implementing. Do not assume custom shader access, arbitrary cloud topology controls, or the creator's exact noise algorithm.

## Future acceptance checks

Use actual normal-speed gameplay footage, with horizon and upward views. Compare sweeping/curling silhouettes, soft body volume, selective rims, and clear gaps. Review the requested time-of-day states and their transitions. Check gentle drift independently of clock speed, near/oblique views, foreground contrast, and a measured low-graphics or mobile tier. Inspect seams, excessive transparent coverage, update cost, and reload cleanup.

These are proposed checks. No sky was built or runtime/device-tested for this package.

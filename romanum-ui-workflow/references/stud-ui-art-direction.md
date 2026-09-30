# Stud-style simulator UI

Use this direction when the developer chooses a bright toy-like game for younger or mixed-age audiences. It is not a universal rule for Roblox interfaces. The primary reference is [the Banana button](../assets/references/banana-button.png); reopen it before visual decisions.

## Read the Banana button as layers

| Visible layer | Design lesson |
| --- | --- |
| Wide rounded rectangle with a strong black perimeter | A simple, instantly recognisable hit target and clean silhouette |
| Darker green lower edge beneath the bright face | A shallow raised-button feel, without a deep realistic extrusion |
| Lime face with brighter highlights and an inset edge | A restrained bevel gives the control volume and a clear edge |
| Faint geometric, stud-like and crosshatched pattern | Texture supplies character while staying quieter than the label |
| Large white, chunky uppercase lettering | One short word dominates; the screenshot does not establish the exact font |
| Black letter outline and a small downward dark shadow | Separation survives a colourful background and suggests tactile depth |

Preserve this hierarchy: label -> button silhouette -> highlight/depth -> decorative texture. The narrow highlight, bottom lip and subtle pattern matter as much as the green colour. Avoid turning it into a plain green rectangle with white text, or an over-rendered glass/chrome button. "BANANA" is reference copy, not the name of a production action. The white canvas around the screenshot is not part of the asset.

Generate a text-free, stud-free button base from the selected concept. Keep its outline, lip and highlight together; use the actual sourced stud texture as a separate native layer according to [assembly guidance](asset-extraction-and-assembly.md#stud-texture-layer). The screenshot's pattern is a visual observation, not a texture source or evidence of reuse rights. Rebuild the live label in Roblox with a suitable licensed/available chunky font, dark stroke and restrained shadow. Do not claim an exact font match without identifying it. Keep enough interior space for different labels and localised text.

## Apply the language consistently

- Use bold colour families with a purpose: the active action, progress and a special state should be distinguishable. The reference green is a style anchor, not a requirement for every control.
- Gradients, bevels, gloss and soft bursts are appropriate when they support this game style. Keep them subordinate to labels. Interface rules from an unrelated website do not decide a game's art direction.
- Use readable illustrated icons with consistent edges and shading. A game's UI icon need not use the realistic materials of a marketing thumbnail.
- Tile the real stud texture on selected backgrounds, panels and headers at consistent scale. Reduce texture contrast behind small numbers. Do not stretch it along with a resizable panel, generate substitutes or build stud geometry.
- Keep related buttons consistent in radius, outline weight, inner margin, label treatment and press depth. Reserve rainbow or strong shine for selected emphasis.

## HUD and screen hierarchy

Keep the main interaction area visible. Place compact counters and a few related navigation actions around it. Give the current tutorial target and immediate progress a stronger read than secondary menus. The gameplay screenshots are useful for icon/label treatment and feedback, not a mandate to copy every side button, sale badge and currency.

A shop card normally needs an item preview, short name, useful comparison, price and one clear action/state. Design only the states the game uses: available, unaffordable, locked, equipped or maxed, for example. Text and symbols must distinguish them as well as colour. Keep prices and reset consequences clear even when ordinary tutorial copy is brief.

The pack's [00:29 shop frame](../assets/references/destroy-the-moon/references/t_29.00.jpg) shows a large preview on the left, name/stat in the middle and price or Equipped on the right, with studs and radial rays behind the item. The [00:25 selling frame](../assets/references/destroy-the-moon/references/t_25.00.jpg) makes the bulk action prominent above repeated item rows. Use these as composition references; keep notifications and tutorial text from overlapping the content as they do in parts of the recording.

On phones, reorganise navigation and secondary actions before shrinking labels. Preserve movement/jump controls and system UI space. A readable desktop mockup alone does not establish mobile usability.

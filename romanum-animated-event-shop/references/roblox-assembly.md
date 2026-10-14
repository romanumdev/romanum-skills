# Roblox assembly

The structure below is from the worked example. Adapt names and helpers to the project's own UI kit (its panel, button and label helpers, stroke and gradient conventions).

## Hierarchy

```
ScreenGui  (ResetOnSpawn false, ZIndexBehavior Sibling, ScreenInsets None, Enabled false until opened)
├─ Dim            full-screen TextButton: dims the game and closes the shop when clicked
├─ MouseRelease   0×0 TextButton with Modal = true, frees the mouse in first person
└─ Stage          fixed design size (e.g. 960 × 640), centred
   ├─ UIScale "Fit"     fits the stage and the props' reach to the screen
   ├─ Back   (ZIndex 1) props behind the panel: lightning, the crashed object and its smoke, the branch, threads, danglers
   ├─ PanelHolder (ZIndex 2) with UIScale "Pop"  (only the panel pops; props have their own entrances)
   │  ├─ Panel (Active = true, so clicks on it don't reach Dim)
   │  │  ├─ Header: gradient, a shine sweep, title, red close button
   │  │  └─ ScrollingFrame of content cards
   │  └─ Notice pill
   └─ Front  (ZIndex 3) props in front: header icon, peeking character, corner props
```

`ZIndexBehavior.Sibling` makes the three sibling layers stack in order without every prop needing a global ZIndex. Props that overlap the panel's edge (the corner icon breaking out of the header, pumpkins sitting on the bottom corners) belong in `Front`; props that appear to be behind the window (a wreck behind the corner, a branch growing out from behind it) belong in `Back`.

Place each prop by its centre in stage coordinates with `AnchorPoint = (0.5, 0.5)`, `ScaleType = Fit`, `BackgroundTransparency = 1` and `Active = false`. Use a different anchor where the motion needs it (bottom centre for anything that squashes on the ground). Props placed relative to the panel's height use scale Y (`UDim2.new(0, x, 0.57, 0)`) so they follow a phone's shorter panel.

## Content cards

Each card is a native panel: a coloured header strip with a big name and a small italic tag, the product image large on the left overlapping the header, a row of tiles with the item name on top and its chance in the corner, a bigger highlighted tile for the rarest item, a progress (pity) bar and buy buttons along the bottom with a pack label above each. Buttons get more colourful for bigger packs, and the biggest gets a shine sweep. Theme the content to the event: in the example the tiles are glass specimen tanks (a rarity-coloured glow fading up from the bottom, a diagonal reflection gradient, rising bubbles) and the card has corner bolts and a tiled caution stripe, because the game is set in a lab.

Keep every name, chance, price and count a live `TextLabel` fed by data. Tiles are placed by their centre with their own `UIScale` so they can pop in from the middle.

## Fitting

```lua
local phone = UserInputService.TouchEnabled and math.min(view.X, view.Y) <= 500
local height = phone and PH_PHONE or PH_DESKTOP -- a shorter panel on phones keeps text big
stage.Size = UDim2.fromOffset(PW, height)
if phone then
	-- the panel gets the screen; props may run off its edges
	scale = math.min(view.X * 0.97 / PW, (view.Y - 24) * 0.95 / height)
else
	-- leave room for how far the props reach past the panel
	scale = math.min(view.X * 0.92 / (PW + 2 * REACH_X), (view.Y - 40) * 0.92 / (height + REACH_TOP + REACH_BOTTOM))
end
fit.Scale = math.clamp(scale, 0.3, 1.35)
```

`UITextSizeConstraint` limits count screen pixels and ignore `UIScale`, so record each constraint's design limits once and multiply them by `fit.Scale` on every refit. Refit on open and whenever the camera's `ViewportSize` or `workspace.CurrentCamera` changes.

## Open, close and the loop

- **Open:** reset the entrance clock (`openedAt = os.clock()`), the lightning timers, the scroll position and any notice; refit; enable the `ScreenGui`; run one animation step immediately so the first frame isn't the final pose; start the loop.
- **Loop:** one `RenderStepped` connection calls the animation function inside `pcall`. It disconnects itself when the gui is disabled or destroyed, and on an error it warns once and disconnects. Expose the step function (`Shop.Animate(now)`) so a test can drive the motion when Studio isn't rendering.
- **Close:** a short tween, then disable the gui guarded by a token so a quick reopen isn't closed by the old timer. Close from the X, the dim area and the gamepad's B button.
- **Reduced motion:** read `GuiService.ReducedMotionEnabled` inside `pcall`, plus the game's own setting if it has one.

## Feature flag

Hide an unfinished or seasonal shop in live servers without removing it:

```lua
local function enabled()
	return RunService:IsStudio() or ReplicatedStorage:GetAttribute("Game_EventShop") == true
end
if not enabled() then
	ReplicatedStorage:GetAttributeChangedSignal("Game_EventShop"):Wait()
end
-- mount the shop and attach its HUD button
```

The server sets the attribute, so it can be flipped on a live server or at a scheduled start without a new publish. A client flag hides the entry point only: every purchase must also be checked on the server, with the event's dates and the item's availability, because a client can always show itself a hidden window.

## HUD entry point

Attach the open button next to an existing HUD button and copy that button's `Size` and `Position` (offset below it), listening for changes so it follows the HUD's phone layout. Re-attach it whenever the HUD's `ScreenGui` is recreated (`PlayerGui.ChildAdded`). Use the header icon as the button's image so the button and the window read as one thing.

## Checks before handing over

- Desktop and phone landscape captures compared with the concept: every prop present, at the concept's scale, nothing covering names, chances or buttons.
- Entrance cascade watched in Play, plus a reopen mid-close and a rapid open/close.
- Reduced motion: all props in final pose, no loops.
- Flag off in a live test server: no button and nothing mounted; flipping the attribute on mounts it without a rejoin.
- Report what is a preview (for example, buy buttons that only show a notice).

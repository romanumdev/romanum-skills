# Rewards and shop screens (study pack)

These are ten third-party Roblox screenshots supplied on 22 Oct 2026 as references. They are unmodified. Study the layout and the pattern, not the art, and do not copy any of it. Quality varies a lot, so each screen has a verdict. Judged against our house style: chunky slab buttons, one thick dark outline, fat white stroked text, few words, few buttons.

## Quick verdicts

| Image | What it is | Verdict | One-line reason |
| --- | --- | --- | --- |
| [01](../assets/references/rewards-and-shop-screens/01-offline-free-reward.png) | "Free Reward" popup with huge rainbow banners | Mixed | Clear 3-tile reward and green Claim, but the banners shout louder than the panel. |
| [02](../assets/references/rewards-and-shop-screens/02-daily-rewards.png) | 7-day daily rewards grid | Mixed | Good day-by-day structure and a big Day 7 tile, but locks bury the rewards. |
| [03](../assets/references/rewards-and-shop-screens/03-playtime-rewards.png) | Timed playtime rewards grid | Avoid | Eight padlocks over dim art; the rewards are hard to read. |
| [04](../assets/references/rewards-and-shop-screens/04-hud-buttons.png) | Three HUD buttons: Trails, Plot, Sell | Reuse | Textbook slab buttons with one clearly dominant. |
| [05](../assets/references/rewards-and-shop-screens/05-collector-board.png) | In-world cash collector with COLLECT pad | Reuse | Big number, one big green action, small stats beside it. |
| [06](../assets/references/rewards-and-shop-screens/06-spin-wheel.png) | Prize wheel with odds and SPIN button | Mixed | Great shape and visible odds, but rotated text and a "SPIN (0)" dead end. |
| [07](../assets/references/rewards-and-shop-screens/07-minigames-menu.png) | Minigames picker with three art cards | Mixed | Clean three-card choice, but the glossy vector style does not match the studded UI. |
| [08](../assets/references/rewards-and-shop-screens/08-starter-pack.png) | Starter Pack offer gated by ads | Mixed | Reads in one second, but fake-urgency copy and an ad gate. |
| [09](../assets/references/rewards-and-shop-screens/09-high-striker-prompt.png) | In-world "E" proximity prompt | Reuse | Small, quiet, two lines, key cap on the left. |
| [10](../assets/references/rewards-and-shop-screens/10-fusion-pass.png) | Event pass with ticket tiers | Avoid | Too many timers, tiny text and two progress systems at once. |

## Per screen

### 01 Offline free reward

A "Free Reward" popup over a blurred world. The header is a rainbow gradient with a red X. Under it: red "Before you leave!", three tiles ($2500, Golden Lion marked "Free Gift!", x2 Speed 10m), the line "Thank you for playing the game!!" and a green Claim! button. Giant rainbow banners run across the top ("YOUR ANIMALS EARN OFFLINE") and bottom ("COME BACK LATER!"). The old tutorial text still shows behind it.

- **Works:** Three tiles in a row with the amount written on each. Claim is green on a dark brown panel, so it reads as the one action. The reward tiles have different colours so each is quick to tell apart.
- **Doesn't:** The banners are far bigger than the panel, so the eye goes to the slogan and not the reward. The popup is small for the screen. The rainbow header, rainbow banners and red subtitle fight each other. Claim is small compared with the empty space. Two copy lines ("Before you leave!", "Thank you...") add words without information. "Come back later" is a retention nudge. The tutorial prompt and "Sell!" label stay visible behind the blur, which is noisy.
- **Take from it:** Show rewards as a short row of labelled tiles with the amount on the tile. Put the Claim button in the one saturated colour on a dark panel. Keep one header colour, not a rainbow. If a banner is used, make it smaller than the panel. Dim or hide other prompts while a reward popup is open.

### 02 Daily rewards

A green-headed "Daily Rewards" panel with a countdown (23:59:58) and a red X. Days 1 to 6 are small square tiles in two rows of three. Day 1 shows CLAIMED and $1,000. Days 2 to 6 each have a yellow padlock over the reward art and a name (Bugman, Sabertooth, Gorilla, Spinosaurus, Kraken). Day 7 is a tall tile on the right with a large lock, "OP REWARD" and Dragon.

- **Works:** The seven-day shape is instantly understood. Day 7 is bigger, so the payoff at the end is obvious. Each tile has its own colour. "Day N" labels are large white text with stroke and readable. CLAIMED in green is a clear state.
- **Doesn't:** The padlocks sit on top of the art and names, so you cannot see what you are working toward. Reward names are dark and hard to read through the lock. There is no visible Claim button in this view, so it is unclear how to act. One timer in the header does not say what it is counting to. The reward amount for Day 1 is partly under the CLAIMED text.
- **Take from it:** A 6 plus 1 layout with a bigger final day is a good pattern. Put a small lock in a corner, not over the reward. Keep the reward art bright even when locked, and dim only the tile edge. Always show one obvious claim button for today's tile. Label the timer ("Next reward in").

### 03 Playtime rewards

A purple-headed "Playtime Rewards" panel. Eight tiles in two rows of four, each with a time at the top (1:44, 6:44, 11:44, 16:44, 21:44, 31:44, 36:44, 51:44) and a lock over the art. A wide ninth tile at the bottom shows 1:01:44 with a Brachiosaurus and cash. Some labels (cash amounts, Lion, Sabertooth, Tiger, T-Rex) are visible but dim; several amounts are cut off by the locks and are hard to read.

- **Works:** The time is at the top of every tile in the same place, so the schedule scans fast. The wide final tile marks the big reward. Consistent grid.
- **Doesn't:** Every tile is locked and dim, so the whole screen looks dead. Padlocks cover the rewards, the same flaw as screen 02 but worse. Times are small and the dark outline fights the dark art. It is unclear whether the numbers are elapsed time or time remaining. Eight identical grey states give no sense of progress. Nothing says what to do.
- **Take from it:** A reward schedule should show progress, for example a bar or a filled check on past tiles. Put the time in the same spot on each tile. Do not lock-cover the reward art. Make the next reward visibly brighter than the rest.

### 04 HUD buttons

Three wide slab buttons in a row: blue "Trails" with a sparkle icon, a larger yellow "Plot" with a house icon, and red "Sell" with a cash icon. Each has a studded surface texture, a thick dark outline and a darker lip. Small text "Ending in 12s" shows below.

- **Works:** Strong colour coding. One icon plus one word each. Fat white text with a dark stroke is readable at a glance. The middle button is bigger, so it reads as the main one. The lip gives a real pressable look. This is the closest match to our house style in the set.
- **Doesn't:** The red Sell button looks like a warning or a cancel on first read. Three same-height buttons in a row could be crowded on a phone. The small "Ending in 12s" text is tiny and unclear without context.
- **Take from it:** Use one icon and one word per HUD button. Make the most important button the largest. Keep the slab lip and the dark outline. Assign colours by meaning, and avoid red for a positive action.

### 05 Collector board

A 3D in-world station built from bricks. A gold sign shows "$53.1M". Below it: "Auto: ON" with a green ON switch, a "x21 Cash" chip and a "$177M/s" chip, then a large green COLLECT pad on the ground. A busy world and creatures glow behind it.

- **Works:** One huge number is the headline. COLLECT is the biggest, brightest object and sits at the front, so the action is obvious. The side stats are small and grouped. The brick frame fits the world, so it feels part of the game.
- **Doesn't:** The background is bright and busy, and glow effects make the small chips harder to read. The italic COLLECT text is tilted and less crisp than the rest. The chips are small for a phone. The relationship between "x21 Cash" and "$177M/s" is not explained.
- **Take from it:** Put a station's value in one big number and a single large action below it. Group secondary stats as small chips. Use a diagonal or slanted pad so it reads as a floor button. Keep the toggle (Auto) as a short label plus a coloured state.

### 06 Spin wheel

A rainbow prize wheel with eight wedges, a red pointer at the top, a red X, and a green "SPIN (0)" button below. Wedges: Lion %10, $10,000 %15, Llama %25, x2 Speed 15m 5%, $50,000 8%, Dragonfly %15, $2,000 %20, Mosasaurus %2. The percentages add up to 100. Each wedge has an icon and rotated text.

- **Works:** The wheel is exciting and instantly understood. Showing the odds on every wedge is honest and builds trust. Each wedge has a distinct colour and a clear icon. The SPIN button is large, green and centred below. Rare rewards sit at a small percentage, which tells the player what is special.
- **Doesn't:** Text is rotated, so half of it is upside down or sideways. The percent sign is placed inconsistently (%10 on some, 5% on others). "SPIN (0)" shows a zero count with no way to get more, which feels like a dead end or a nudge to buy. Small numbers on a bright rainbow have weak contrast. The X floats off the wheel by itself.
- **Take from it:** Show the odds, and keep the number format the same on every wedge. Put icon first and keep text short. Tell the player how to get spins when the count is zero. Keep the primary button below the wheel, large and green. Keep text upright where possible, for example a label under each icon.

### 07 Minigames menu

A rounded orange panel titled "MINIGAMES" with a joystick icon and a red X. Three tall cards in a row with illustrated art: Flappy Egg, Egg Merge (the centre card, slightly larger and raised) and Nest Strike. Each card has a name on a dark band at the bottom.

- **Works:** Three big cards are an easy choice. The centre card is raised, which suggests a featured pick. The illustrations are bright and show the game at a glance. Names sit on a dark band, so they stay readable.
- **Doesn't:** The smooth, glossy vector art looks like a different game next to the studded UI in the other screens. The thin outline and soft shadows do not match the thick-outline slab look. No play button, price or reward is shown, so it is not obvious what happens on tap. The card text is small on a phone.
- **Take from it:** A row of two to three big picture cards is a good picker. Use a dark label band at the bottom of each card. Keep all art in one style. Add a clear action cue, for example a play icon.

### 08 Starter pack

A cyan-headed "Starter Pack!" panel with a gift icon and a red X. The subtitle "Limited Time Deal!" is in rainbow gradient text. Three items joined by plus signs: Hacker Egg, $1M Cash and 2x Luck 15m, each with a glowing burst behind it. One yellow button reads "Watch 3 Ads" with a TV icon. The blurred game behind it shows through.

- **Works:** The "A + B + C" layout makes the bundle clear in one look. Big glossy blocky icons with a burst behind them are attractive and close to our house style, as is the faint studded texture in the header. Labels are short and readable. The yellow button stands out on the brown panel.
- **Doesn't:** "Limited Time Deal!" has no visible timer, so the urgency is fake. The price is "Watch 3 Ads", which is a chore, and it is not stated whether this is the only way to get it. The button is small compared with the big empty panel. Blurred UI bleeding through the panel adds noise. The rainbow text is a different style from the header.
- **Take from it:** Use a plus-joined row of big icons for bundles. Make the price or cost the most visible thing on the button. If something is limited, show a real timer. Keep the button wider than any single item.

### 09 High Striker prompt

A small dark rounded pill floating in the world. On the left is a bordered "E" key. On the right, "High Striker" in small grey text and "Hit for a prize!" in larger white text. It stands in front of a tall striker machine on a bright orange checkered floor.

- **Works:** The key cap makes the input obvious. Two lines give a name and a reason. The dark pill stands out on a bright floor. It is small and does not block the view.
- **Doesn't:** The text is small and the name line is thin grey, so it will be hard to read on a phone. It does not use the chunky outlined text of the other screens, so it feels like the default Roblox prompt. There is no touch cue. Little extra colour gives it nothing to grab attention.
- **Take from it:** A proximity prompt works with a key cap, a name and a one-line payoff. Keep it small and dark. For our version, add the thick text stroke and a tap target for touch. Make the name line bigger than this one.

### 10 Fusion pass

A wide red-to-magenta panel titled "Fusion Pass" with the subtitle "Fusion Event · Rewards scale with your progress!", a timer ("Next Fusion Portal in 02:41") and a red X. On the left: "Fusion Egg · SIZE x3", a DIVINE tag, egg art, a 1/25 progress bar, a grey Locked button and a "YOUR TICKETS" box (1 ticket, "Next reward at 2", "+1 every day you play · +1 every boss kill", "Next daily ticket in 14:52:55"). On the right: tiles for 1 TICKET (Common, +36.38k, "5 min Money", green Claimed), 2 TICKETS (Common, +100, "Speed +1%", Locked) and 3 TICKETS (Mythic, Snow Mythic Egg x1, Locked), with a scroll bar and part of a fourth tile at the edge.

- **Works:** Each tier tile has the same structure: ticket count, rarity, reward art, name, state button. The rarity label and colour (grey, red) are clear. Button states (Claimed in green, Locked in grey) are easy to read. Reward art sits on a black inset, so it pops.
- **Doesn't:** It is dense. There are three timers, two progress systems (the 1/25 bar and the ticket count) and several lines of small text. The tickets box has tiny type. "+100" next to "Speed +1%" is confusing. The Locked button under the main egg gives no clue how to unlock it. Rewards "scale with your progress" but nothing shows how. A sideways scroll hides later tiers, including the best one. Two currencies (tickets and egg progress) are hard to follow.
- **Take from it:** Use a fixed tile template for each tier. Show state with one button colour: green for claimed, grey for locked. Put a black inset behind reward art. Keep it to one progress bar and one timer. If there are tiers off-screen, show a clear arrow or a count.

## Patterns worth reusing

- One primary action per screen, in the largest and brightest button, in a saturated colour on a dark panel (screens 01, 05, 06).
- Rewards as a row of labelled tiles with the amount on the tile (01, 08).
- A 6 plus 1 grid with a bigger final tile for the big prize (02).
- The same timer position on every tile, so a schedule scans quickly (03, 10).
- Button states shown by colour: green for claim or claimed, grey for locked (02, 10).
- One icon and one word per HUD button, with the key button the largest (04).
- Show the odds when there is chance, with the same number format everywhere (06).
- A black inset behind reward art so it pops (10).
- A "A + B + C" row for bundles (08).
- A short in-world prompt: key cap, name, one-line payoff (09).

## Patterns to avoid

- Padlocks or dark overlays on top of reward art so you cannot see the prize (02, 03).
- Fake urgency, such as "Limited Time Deal!" with no timer (08).
- A price that is a chore ("Watch 3 Ads") with no alternative shown (08).
- Giant banners that outshout the panel (01).
- Several timers and two currencies on one screen (10).
- Mixed art styles in one menu, such as glossy vector cards next to studded slabs (07).
- Rainbow text and rainbow headers everywhere, which flattens the hierarchy (01, 08).
- A zero-count button with no way to get more, like "SPIN (0)" (06), and rotated or inconsistent text on a wheel (06).

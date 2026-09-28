# Early launch experiments

These practitioner notes were recorded in September 2026. Their original source, sample and campaign context have not been supplied; they are not attributed to Tizzy or Roblox. Preserve the distinction between a suggested experiment and a platform requirement.

## Advertising and discovery

| Reported recommendation | How to use it in a plan |
| --- | --- |
| 16 ad credits per day: 11 for visits, 5 for engagement, until 250 qualified users | A candidate starting budget and review milestone. Confirm the campaign objectives, current platform limits, qualification definition and total budget before recommending execution. These are advertising credits, not Romanum credits or USD. |
| It is usually safe to stop ads when home recommendations overtake advertising | A prompt to review dependence on paid traffic. Compare the same acquisition measure and time window across Home and ads; a brief crossover alone is insufficient to establish sustained organic acquisition. |
| It usually takes 7–14 days to reach recommendation traffic | A reported planning window, not an algorithm timer or a reason to keep spending despite poor results. Recommendation traffic may appear sooner, later or not at all. |

Do not claim that 250 qualified users unlocks discovery. Do not invent the meaning of "qualified users" or substitute visits, CCU or impressions for it. Before implementing a campaign, check current Roblox documentation and the developer's actual Ads Manager and analytics labels. Keep the original 11/5 split visible when discussing an alternative.

Define the budget cap, review date and outcome before starting. At the suggested constant rate, 7 days would use 112 ad credits and 14 days would use 224; those are arithmetic scenarios, not spending commitments or recommended automatic runtimes. Changing a campaign requires the developer's authorisation.

When Home traffic becomes stronger, consider reducing paid spend while checking whether comparable organic acquisition, first-session completion and return behaviour hold up. Report the effect without treating every change as caused by the ad reduction. Do not promise recommendation placement from a particular budget, retention figure or elapsed time.

## Funnels

Funnel analytics are strongly recommended here to measure where players drop off. Define a sequence such as join -> controls understood -> first action -> first reward -> next goal, with an observable event for each step. The sequence is an example: adapt it to the real loop. Report how many eligible players reach each step and the conversion and drop-off between steps. Separate failures to load from players who enter gameplay and leave later.

A drop-off identifies where to investigate, not why it happened. Compare device and acquisition cohorts where sample sizes permit, then inspect the largest loss through playtests or other authorised observations. The separate `romanum-player-onboarding` skill expands that workflow and visual tutorial design when available. Thumbnail production cadence and the suggested Ads Manager CTR target live in `romanum-thumbnail-design`; installing this skill does not install either of those skills automatically.

# Storyboard: Beyond the Total

Updated: 22 November 2026

Working title: Beyond the Total: Different Stories Behind Australia's Road Injuries.

This is our evidence-led storyboard after Stand Up 1. It describes planned design and behaviour, not completed D3 code. We will discuss the revised direction with the tutor in Week 11 and record the response before further substantial changes.

## Audience and purpose

We are designing for students and general readers interested in road safety who may assume a national decrease applies to every road user. Their task is to compare groups, inspect their composition and recognise the limits of hospitalisation counts. The website should guide those tasks rather than expose every variable as a global filter.

Our question is: what differences disappear when road injuries are reduced to one national total?

## Narrative sequence

| Frame | Reader's question | Evidence and planned visual | Transition |
| --- | --- | --- | --- |
| 1. Opening | Did every group decrease when the total fell? | Contrast the national -4.8% with cyclists +14.1% in 2019-2020. Keep a brief 2011-2021 national trend with 2012/2017 recording-break markers. | Invite comparison rather than assume a shared trend. |
| 2. Different trends | Which road users moved differently? | Dumbbell comparing 2019 and 2020 on one count scale, with signed change labels. Retain the small pick-up/van increase in the full data. | Focus on cyclists, while allowing other groups to be compared. |
| 3. Different event classifications | Does cyclist hospitalisation always involve another vehicle? | Two-column Road user / Counterparty Sankey for 2021, initially highlighting cyclists. Non-collision contributes 3,705/8,163; car/pick-up/van contributes 1,575/8,163. | Follow the selected group into its age profile. |
| 4. Different age profiles | Is the age mix the same across road users? | Heatmap initially showing within-road-user age percentages. Cyclists aged 40-64 account for 41.6%; the largest car-passenger age group is 17-25 at 26.8%. | Explain the denominator and the limits of this comparison. |
| 5. Takeaway and method | What can we responsibly conclude? | Summarise the three contrasts, expose exact values in a table and explain unknowns, unequal age bands and missing exposure denominators. | Leave three supported observations, not a ranking of dangerous transport modes. |

The 2021 profiles and 2019-2020 comparison answer different questions. Label each year or pair prominently. We will not imply that 2021 classifications caused the 2020 increase.

## Visual encoding and alternatives

| Candidate | Marks and channels | Purpose | Alternative and tradeoff |
| --- | --- | --- | --- |
| Dumbbell | Points on a shared quantitative x-axis; road-user rows; connecting segment; colour and shape distinguish years | Reveal direction and magnitude of the count differences | Grouped bars are familiar but take more space. A two-year comparison hides intermediate years, so keep trend context and exact values. |
| Sankey | Category nodes and links; width represents Hospitalisations; highlighting follows a selected group | Trace the composition of a road-user total | A count/row-normalised matrix may make pair comparison and mobile reading easier. Crossings and small links are a usability risk; test whether the Sankey is worth retaining. |
| Heatmap | Road-user rows and age columns; sequential colour encodes one labelled metric at a time | Compare age profiles across differently sized groups | Grouped bars are more precise for a single group but become crowded across all groups. Keep exact-value tooltips and a table because colour is less precise than position. |

These extend our existing line and bar views. The complete course materials still need checking before we claim a chart has not been taught. Technical novelty alone does not justify an unreadable chart. Sankey links represent categorical associations, not a patient journey, event sequence or assignment of fault.

## Interaction plan

| Trigger | Intended response | Reader's task |
| --- | --- | --- |
| Open story | Show the deliberate 2019-2020 comparison and national/cyclist contrast | Start with a question rather than an empty dashboard |
| Change year pair | Recalculate count and percentage change; flag comparisons crossing a recording break | Check whether the contrast generalises |
| Select road user | Highlight the group and pass selection to the profile views | Follow one group through the story |
| Change detail year, initially 2021 | Update Sankey, heatmap and detail table; keep the year-pair comparison separate and labelled | Distinguish a single-year profile from a two-year change |
| Hover or focus mark | Show years, count, percentage and denominator | Read exact values without a crowded chart |
| Activate Sankey category/link | Highlight associated categories and show count plus within-road-user share | Understand composition without inferring causation |
| Switch heatmap count / within-road-user % | Update scale, legend and table consistently | Distinguish size from composition; withhold bed-day mode until validated |
| Reset story | Restore the documented year pair, detail year and group defaults | Recover the starting point; specify scrolling separately |

Month, remoteness and sex do not automatically become extra global filters. The current website's Reset behaviour remains unchanged until a later implementation change is deliberately made and tested. Keyboard access, readable labels, contrast, a narrow layout and a table alternative must accompany new interactions.

## Data and coding handoff

| Data | Role | Before use in the website |
| --- | --- | --- |
| Existing annual and road-user exports | Context and selectable year comparison | Preserve source controls and served-copy reconciliation |
| `data/analysis/road_user_changes_2019_2020.csv` | Control example for the default contrast | Do not sum its All road users row with the category rows |
| `data/analysis/counterparty_by_road_user.csv` | Reference for a new KNIME export and Sankey | Preserve literal categories; conserve each selected road-user total |
| `data/analysis/age_by_road_user.csv` | Reference for the heatmap | Sum all source sex categories; include retained unknowns in the denominator |
| Monthly and remoteness summaries | Supporting EDA | Keep outside the main story unless further evidence justifies them |

The new summaries are Python-derived reference data, not completed KNIME exports. Extend the workflow before adopting them as final inputs. Any simplified display grouping needs a full documented mapping and table; do not remove unspecified categories to make the Sankey cleaner.

The existing `data.js`, `charts.js` and `app.js` split can support implementation. Specify the comparison year pair separately from the detail year, road-user selection and metric mode. Share number formatting, category ordering, colour meanings and recording-break constants.

## Evaluation tasks for Week 12

1. Find a group that increased while the national total decreased; distinguish absolute and percentage change.
2. Determine whether all cyclist hospitalisations involve another vehicle; identify non-collision and unspecified classifications correctly.
3. Compare two age profiles and explain what the heatmap percentage denominator means.
4. Reset the view and explain whether it identifies individual risk or crash locations.

Record success, time and misunderstandings. Test exact-value alternatives and keyboard/narrow-screen use. Passing data checks or displaying a static EDA figure does not demonstrate that the eventual interactions are usable.

## Next checkpoint

The [design preview](design/preview.html) now contains labelled desktop/narrow-screen wireframes, chart sketches and alternatives. The three [design sections](design_book/03_design_draft.md) and [coding plan](CODING_PLAN.md) are drafted. Use the [Stand Up 2 review guide](STANDUP_2_REVIEW.md) to inspect them, then prepare the slide deck and merged Design Book draft. New D3 code and KNIME extension remain pending. See [EDA_AND_STORY.md](EDA_AND_STORY.md) for calculations and limitations.

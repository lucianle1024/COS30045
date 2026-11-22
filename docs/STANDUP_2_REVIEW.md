# Stand Up 2: preparation and review guide

Updated: 22 November 2026. Team: Gr_01, Nguyen Huyen Minh Nhat and Le Tuan Huy.

Stand Up 2 explains our proposed design and coding plan. Stand Up 3 demonstrates the new chart code, interactions and validation. The talk must be under three minutes, with any web demonstration included. The extended time used for Stand Up 1 is not assumed for these presentations.

## What is ready, and where to inspect it

| Item | Where | What to inspect |
| --- | --- | --- |
| Verified findings and caveats | [EDA_AND_STORY.md](EDA_AND_STORY.md), `data/analysis` | Counts, percentage denominators, retained categories and limits |
| Question and reading sequence | [STORYBOARD.md](STORYBOARD.md) | Each chapter has a question, evidence and transition |
| Desktop/mobile wireframes | [Design preview](design/preview.html), `docs/design/wireframe_*.svg` | Headings, controls, charts, tables and narrow-screen alternatives |
| Labelled chart sketches and alternatives | Same preview, `docs/design/sketch_*.svg` | Marks, scales, year shapes, legends, exact values and tradeoffs |
| Design Book drafts | [03_design_draft.md](design_book/03_design_draft.md) | Sections 3.1 Website, 3.2 Visualisation and 3.3 Interaction; proposed status is explicit |
| Coding handoff | [CODING_PLAN.md](CODING_PLAN.md) | Actual CSV fields, KNIME changes, modules, shared state/constants and acceptance |
| Existing working website | `web/index.html`, served through HTTP | Earlier implementation for context; new sketches are not yet implemented there |

Open `docs/design/preview.html` directly for the design review. It embeds all figures and does not fetch CSVs or use a CDN. For both review page and current website, serve the repository root:

```bat
py -m http.server 8000
```

- Design review: http://localhost:8000/docs/design/preview.html
- Current website: http://localhost:8000/web/

This differs from the website-only README command using `--directory web`: that server cannot show `docs/design`.

## Presentation route: three slides, target 2:40

This is a speaking outline with pointer cues, not a completed slide deck. The eventual slides should use these exact sketches and verified figures.

| Time | What to say | Point to / show |
| --- | --- | --- |
| 0:00-0:40 / Slide 1 | "After the first stand-up, we explored differences hidden by the national total. In 2019-2020 the national count fell 4.8%, but cyclist hospitalisations rose 14.1%. Our revised story asks whether one total can represent every road-user group." | Point to the national figure first, then the cyclist figure. End on the revised question. |
| 0:40-1:15 / Slide 2 | "The dumbbell compares two years on the same count axis. Circle and diamond identify the years. The selected row gets an outline so colour keeps its meaning. We retain all 12 groups and exact values; small changes are harder to read on this scale." | Point to the year legend, the two cyclist endpoints and its change label. Briefly indicate the grouped-bar alternative. |
| 1:15-1:45 / Slide 2 | "For the 2021 profile, the event view separates non-collision from unspecified records. The age heatmap compares percentages within each road-user total. These are composition views, not risk estimates, and they do not explain the earlier increase." | Point to 3,705 / 8,163 on the Sankey, then the 41.6% cyclist/40-64 heatmap cell and legend. Show the 2021 label. |
| 1:45-2:10 / Slide 3 | "The layout separates comparison years from the profile year. Selecting a road user links the profiles, while count and percentage modes update the legend and table. Mobile uses selected-group bars with exact tables." | Point to the desktop detail-control band, then the mobile chart block. |
| 2:10-2:40 / Slide 3 | "Next we will reconcile the new KNIME counterparty export, build the comparison and age views, then test the event design. Our main design question is whether a Sankey helps more than a matrix. We will use task observations to choose and document changes for Week 12." | Point to the implementation sequence and the Sankey/matrix decision. Finish with the Week 12 evidence to collect. |

An optional 10-15 second opening of the design review page must replace equivalent slide time, not extend the talk. Keep screenshots ready in case switching windows fails. Rehearse with a timer and trim rather than speed up. The presenter must explain the choices in their own words.

## Q&A rehearsal

| Likely question | Evidence to use |
| --- | --- |
| What changed after the feedback? | A question-driven story, field audit, three new design candidates, simpler alternatives and explicit interaction specifications |
| Why those years? | 2019-2020 is the observed contrast and avoids the known 2012/2017 breaks; 2021 is the latest detail year in this release, not a cause of the earlier change |
| Why a dumbbell instead of bars? | Fewer marks and connected positions for two observations; bars are familiar and remain a mobile alternative |
| Is the Sankey justified? | It follows one total into classifications; the matrix is better for comparing groups. Reader evaluation will inform the choice |
| What does 41.6% mean? | 3,393 cyclist hospitalisations aged 40-64 divided by all 8,163 cyclist hospitalisations in 2021, including Unknown and all source sexes |
| Did only cyclists increase? | No. Pick-up/van occupants rose 260 -> 300; cyclists had a much larger absolute increase |
| Is this evidence of higher risk? | No exposure denominator is available in this analysis. Counts and composition do not establish risk or causation |
| Is the revised website finished? | No. The preview is design evidence. New D3 code, the KNIME extension and participant evaluation remain pending |

## Before the actual submission

- [ ] Agree which member presents Week 11, which presents Week 12 and the tutorial dates.
- [ ] Review the design in both members' own words and record actual individual contributions.
- [ ] Prepare the three-slide PPT using the reviewed sketches and a timed script.
- [ ] Merge the design drafts, updated story/purpose and EDA into the current Design Book PDF. The older PDF does not yet include this pack.
- [ ] Prepare and inspect the latest `Gr_01` KNIME export with bundled raw data and required outputs. Re-import it and check workflow-relative paths. The design pack does not itself update KNIME.
- [ ] Include the agreed repository link, following the tutor's confirmed submission arrangement; GitHub Classroom and Mercury are not required for this team.
- [ ] Submit PPT, draft Design Book and KNIME separately on the night before the actual presentation. Do not submit a ZIP.

## Checks for this checkpoint

Verification on 22 November 2026:

- The figure builder passed assertions for all 12 comparison groups, both national sums, every 2021 age row and the count-preserving cyclist event grouping (8,163).
- All six SVGs parsed and rendered to inspection PNGs. The two wireframes and four chart figures were visually reviewed for labels, clipping and layout.
- The embedded preview has six named figures, unique SVG IDs, valid local links and valid chapter anchors. New draft text uses ordinary hyphens.
- Core text colours against white and paper measure at least 5.56:1. Heatmap cell text is selected against its actual fill to reach at least 4.5:1. These checks do not establish complete accessibility conformance.
- Existing checks passed: 9 Python EDA tests, 6 JavaScript data tests and raw/processed/served-file reconciliation. The raw workbook and production website files were not changed.
- Chromium could not launch in this execution environment. Live browser reflow, navigation and keyboard behaviour have not been verified here. Inspect the review page on the presentation laptop before rehearsing.

New D3 interaction behaviour, live mobile layouts, KNIME re-execution and participant evaluation are outside this static design checkpoint.

AI use: AI assisted with this review guide and speaking outline. Presenter allocation, rehearsal duration and submission readiness must be confirmed from actual team work.

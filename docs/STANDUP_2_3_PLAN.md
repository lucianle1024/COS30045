# Stand Up 2 and 3 plan

Updated: 19/11/2026

Team: Nguyen Huyen Minh Nhat and Le Tuan Huy.

We have completed Stand Up 1. Our tutor's feedback was that the project needs deeper data exploration, stronger storytelling and more ambitious visualisation choices. This plan records how we will develop and demonstrate those changes over Weeks 11 and 12. It replaces the older Stand Up milestones in PROJECT_PLAN.md for these two presentations; it does not mark the planned work as completed.

## Assessment requirements

Source: Project Stand-up 2/3 (Week 11/12), supplied on 19/11/2026, pages 1-4.

- Each presentation must be less than three minutes, followed by Q&A.
- Both team members attend. One presents in Week 11 and the other in Week 12.
- Each responsible member prepares and delivers their presentation and answers questions about their own understanding. Both members need to understand the whole project.
- Submit the PowerPoint, current draft Design Book, latest KNIME workflow with data and team name, and the team GitHub Classroom link. Do not submit a ZIP.
- Submit on the night before the actual presentation. The PDF header displays 4 December at 23:59; we will confirm our tutorial dates and the Canvas submission arrangement rather than use that header as permission to submit after a presentation.
- This is an individual assessment. We will record actual contributions separately from the proposed speaking order.
- We will explain the revised direction to the tutor in Week 11 and discuss substantial later changes before the final submission.

Proposed speaking order: Nhat in Week 11; Huy in Week 12. We still need to agree this split and our exact presentation dates.

## Current baseline

- The existing website has a national trend, a road-user ranking and an age/sex view, with linked selection and a data table.
- The current KNIME pipeline filters Traffic and exports three hospitalisation datasets.
- Stand Up 1 and its draft Design Book are available. The student has confirmed that the presentation took place.
- The new chart designs, additional KNIME exports, revised story and user evaluation below are planned, not completed.

## Revised story to investigate

Working title: Beyond the Total: Different Stories Behind Australia's Road Injuries.

We will keep the September 2023 workbook covering 2011-2021 as our source version. We will not mix its figures with revised values on the live dashboard.

| Question | Evidence or investigation | Candidate chart |
| --- | --- | --- |
| Did all road users follow the national change in 2019-2020? | Initial EDA: the national count fell from 39,866 to 37,966, while cyclists rose from 7,302 to 8,332. Reproduce these controls in the new analysis. | Dumbbell chart comparing two selected years |
| Which counterparties and event categories appear within each road-user group? | Initial EDA: 3,705 of 8,163 cyclist hospitalisations in 2021 were classified as Non-collision transport accident. Check all category mappings and totals. | Two-column Sankey, with a matrix or table as an alternative |
| Does looking at age composition or bed-day burden change the picture? | Explore age by road user; audit bed-day definitions before introducing any ratio or burden claim. | Heatmap with clearly labelled count and within-group percentage modes; bed-day mode only if validated |

These are candidate questions. We will retain findings that survive the data audit and revise the chapter order to match the evidence.

Interpretation rules:

- Sum Hospitalisations; a raw row is an aggregated record, not one person or one crash.
- Counts and within-group percentages are not exposure-adjusted risk.
- Keep unknown categories and distinguish zero from missing values.
- Mark the 2012 and 2017 recording breaks. Do not attribute a change to COVID or another cause without appropriate evidence.
- Remoteness describes the patient's usual residence, not the crash location.
- Counterparty does not establish fault. Sankey links represent categorical associations, not a patient journey or a sequence of events.
- Bed-day ratios require aligned definitions and aggregation. Do not average row-level ratios or present hospital burden as a clinical severity score.
- Check candidate charts against the complete course materials and final rubric before claiming they extend beyond taught content.

## Stand Up 2 - Week 11: explain our design decisions

Required milestones: draft Visualisation Design, Interaction Design and Website Design sections; sketches or prototypes; a concrete coding plan.

| Order | Work before the presentation | Evidence to show |
| --- | --- | --- |
| 1 | Audit Month, Counterparty, Remoteness and bed-day fields. Reproduce the initial findings and list uncertainty. | An EDA table with source fields, calculation and checks for each proposed finding |
| 2 | Choose three questions and explain how they address the Stand Up 1 feedback. | A short storyboard with an opening, evidence and takeaway for each chapter |
| 3 | Sketch the dumbbell, heatmap and Sankey, and compare each with a simpler alternative. | Labelled sketches showing axes, marks, colour, legend and the question answered |
| 4 | Specify default selections, year comparison, highlighting, tooltips, Reset and a table fallback. | An interaction table with trigger, changed views and expected result |
| 5 | Draft the Website Design section around the reader's route through the three chapters. | Desktop and narrow-screen wireframes with headings, source notes and chart positions |
| 6 | Draft the Visualisation Design and Interaction Design sections, including tradeoffs. | Updated Design Book draft; no claim that the proposed chart code is already complete |
| 7 | Write the coding and data plan, then prepare and rehearse the presentation. | Data schemas, module responsibilities, shared constants and a presentation under three minutes |

Planned data and code:

- Reuse annual_totals.csv and road_user_by_year.csv for context and year comparison.
- Export counterparty_by_road_user.csv grouped by year, road user and counterparty, with summed Hospitalisations.
- Reuse the demographic export for the first heatmap. Calculate within-road-user percentages with an explicit denominator including retained unknowns.
- Add a separately specified bed-day export only after the measure audit. Record how deaths, transfers, missing values and zero denominators are handled.
- Keep one shared selection state and shared number formatting, age ordering, colour meanings and reporting-break constants.
- Give each chart a rendering function and a selection callback. Extend data validation and the accessible table for new views.
- Keep exports used by the website reconciled with the processed files and raw source.

Suggested Week 11 presentation, target 2 minutes 40 seconds:

| Slide | Time | Focus |
| --- | --- | --- |
| 1 | 40 seconds | Tutor feedback, the revised question and one verified surprising finding |
| 2 | 80 seconds | Show the sketches; explain the chart and interaction choices and one tradeoff |
| 3 | 40 seconds | Coding plan, unresolved issue and next steps for Week 12 |

Use sketches as the main evidence. If showing the existing website, include it within this time as a brief before/after reference. Do not reuse the longer Stand Up 1 demo.

Week 11 readiness:

- [ ] We have agreed the presenter and tutorial date.
- [ ] All three required design sections have drafts.
- [ ] The proposed charts have labelled sketches or prototypes.
- [ ] The data schemas, interactions and shared constants are specified.
- [ ] We can explain one chart alternative and why we did not choose it.
- [ ] The submission files are ready on the night before the presentation.

## Stand Up 3 - Week 12: demonstrate implementation and validation

Required milestones: draft Iteration and Validation section; updated earlier sections; a description of the planned design; actual code for charts and interactions.

| Order | Work between presentations | Evidence to show |
| --- | --- | --- |
| 1 | Record the Week 11 feedback and update the story, sketches and coding plan. | A decision log connecting each relevant comment to a change or reason for keeping the design |
| 2 | Extend KNIME and validate the new exports before connecting them to the web. | Latest executed workflow, bundled source data, exported CSVs and reconciliation results |
| 3 | Implement the dumbbell and its two-year selection first, then the heatmap, followed by the Sankey if its grouping is ready. | Actual working D3 charts and event handlers; remaining work labelled honestly |
| 4 | Check default views, filters, highlighting, tooltips, Reset, table totals and narrow layouts. | Technical validation results with tested scope and unresolved issues |
| 5 | Run a small usability evaluation, ideally with 3-5 people outside the team. | Actual participant/task records and findings; this is our target, not a stated assessment minimum |
| 6 | Make and document improvements based on the evaluation. | At least one evidenced before/after example if findings require a change |
| 7 | Draft Iteration and Validation and update the design, processing and implementation sections to match the actual work. | Current Design Book with completed, in-progress and pending work clearly separated |
| 8 | Prepare a short demo and rehearse the presentation plus questions. | A presentation under three minutes, with the demonstration included |

If user testing is not complete, document the test plan and mark results as pending. Do not describe planned participants, findings or improvements as completed. Aim to arrive with actual observations so the iteration section has useful evidence.

Suggested evaluation tasks:

1. Identify a road-user group that moved in the opposite direction to the national total in 2019-2020.
2. Find the non-collision count or share for cyclists in 2021 and explain what it means.
3. Compare two road-user age profiles and explain the difference between count and within-group percentage.
4. Reset the view and explain whether the charts establish individual risk.

Record task success, approximate time, misunderstandings and comments. Do not collect unnecessary personal information.

Suggested Week 12 presentation, target 2 minutes 45 seconds:

| Part | Time | Focus |
| --- | --- | --- |
| Slide 1 | 30 seconds | What changed since Week 11 and the responsible member's actual contribution |
| Live website | 65 seconds | Demonstrate a new chart, one meaningful selection and the resulting linked view or table |
| Slide 2 | 45 seconds | Validation evidence and one genuine usability finding with its improvement, or the remaining evaluation plan |
| Slide 3 | 25 seconds | Blockers, unfinished work and next steps for the final submission |

Week 12 readiness:

- [ ] The second team member has prepared and practised the presentation.
- [ ] Chart and interaction code can be demonstrated on the presentation laptop.
- [ ] The Design Book matches the implemented and still-planned design.
- [ ] Iteration and Validation has a draft with actual evidence or explicit pending status.
- [ ] The latest KNIME export includes data and the correct team name.
- [ ] The submission files are ready on the night before the presentation.

## Shared submission and Q&A checklist

For each week, submit the PowerPoint, draft Design Book and latest KNIME file separately, plus the team GitHub Classroom link. Our current repository is https://github.com/lucianle1024/COS30045; confirm the tutor accepts it or use the assigned Classroom repository. Do not assume that a normal repository is automatically a Classroom submission.

Use one team identifier consistently across the deck, Design Book, workflow filename and annotations. Earlier documents use Gr_01, while one uploaded KNIME filename used Gr02; confirm the official identifier before preparing the final submission set.

Both members should be able to explain:

- Why each chart answers its question, and the advantages and disadvantages of an alternative.
- Why a two-year comparison uses its chosen years and how recording breaks affect interpretation.
- What a raw row represents and how the CSVs and displayed totals are calculated.
- Which denominator is used in each percentage or bed-day ratio.
- What a click changes in the application state and how D3 updates the marks.
- How unknowns, missing values, zeros and small groups are handled.
- What has actually been tested and what remains uncertain.
- Their own work, supported by files, commits and decisions, without using presentation order as a substitute for contribution evidence.

We will explain the work in our own words, using the code or charts as evidence. We will not rely on reading code comments as our explanation.

## Next action

Progress on 21/11/2026:

- [x] Reproducible audit of all 13 fields, missingness and source controls.
- [x] Deeper EDA across year, month, counterparty, age and remoteness, with reference CSVs and two EDA figures.
- [x] Evidence-led [storyboard outline](STORYBOARD.md), design alternatives and intended interactions.
- [ ] Full design drafts, labelled wireframes/sketches and the Week 11 deck.
- [ ] New D3 chart/interaction code, KNIME extension and actual participant evaluation.

See [EDA_AND_STORY.md](EDA_AND_STORY.md) for findings and limits. Chapter 3 now uses age composition; bed-day ratios remain withheld until missing death fields and numerator scope are resolved. Multiple analysis CSVs still represent one national workbook.

Next: turn the storyboard into wireframes and chart sketches, then complete the three Week 11 design drafts and coding plan. These progress ticks do not mark the presentation or student acceptance as completed.

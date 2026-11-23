# Stand Up 2: preparation and review guide

Updated: 23 November 2026. Team: Gr_01, Nguyen Huyen Minh Nhat and Le Tuan Huy.

Stand Up 2 explains our proposed design and coding plan. Stand Up 3 demonstrates the new chart code, interactions and validation. On 22 November, the team confirmed the lecturer's clarification: both talks should run longer than three minutes. Our proposed rehearsal target is 4:45, generally 4-5 minutes before Q&A. This replaces the original PDF's shorter timing; it is not a new official maximum.

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

## Presentation route: Huy, 23 November, target 4:45

The [decision log](StandUp_02/DECISIONS_AFTER_STANDUP1.md) connects the feedback to our choices and their evidence. The [Markdown notes](StandUp_02/Gr_01_StandUp2_Huy_Notes.md) give Huy simple wording and pointer cues. The deck has six main slides and one Q&A audit backup.

| Slide | Time target | Focus |
| --- | --- | --- |
| 1 | 0:00-0:45 | Our decisions after Stand Up 1 |
| 2 | 0:45-1:30 | Our story questions and scope |
| 3 | 1:30-2:10 | Evidence behind our comparison |
| 4 | 2:10-3:05 | Chart choices for comparison and age composition |
| 5 | 3:05-3:45 | Event categories and an open design decision |
| 6 | 3:45-4:45 | Implementation decisions and the next checkpoint |
| 7 | Q&A only | Data exploration and checks |

The main script contains 441 English words. Present slides 1-6, then stop for Q&A. Slide 7 holds audit detail. The first two slides explain feedback, decisions and the selected story questions. Findings and chart sketches support those decisions. The notes contain short answers about why we kept some fields, deferred ratios and left Sankey/matrix open.

Rehearse with pointing and slide changes. An optional 20-second current-web example after slide 6 brings the target to about five minutes. Exact duration remains a laptop rehearsal check. The complete chart alternatives remain in the Design Book.

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

- [x] Huy presents Week 11 on 23 November. Confirm the Week 12 date for the other member.
- [ ] Review the design in both members' own words and record actual individual contributions.
- [x] Prepare six main slides, one audit backup, a 441-word Huy script and decision/Q&A notes in Markdown.
- [ ] Export/open the PPTX and measure the rehearsal on the presentation laptop.
- [x] Merge the story, processing/EDA and three design sections into a current Stand Up 2 Design Book source/PDF. The Stand Up 1 PDF remains as earlier evidence.
- [x] Prepare the team-labelled `Gr_01_StandUp2.knwf` copy and verify the bundled data, saved state, relative settings and unchanged node configuration.
- [ ] Re-import the renamed KNIME package on the presentation laptop and check execution there.
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

The 23 November revision puts the response to feedback first: decisions, selected questions and scope, research evidence, chart choices and implementation. All seven native slides are rendered and reviewed. Speaker notes match the Markdown script. The generator keeps notes in Markdown and counts only the six main-slide scripts.

The previous pack was committed and pushed as a608322 by Nhat. This revision will be copied and committed through the same CMD workflow. The unchanged Design Book PDF and KNIME package remain the assessment files from that commit.

New D3 interaction behaviour, live mobile layouts, KNIME re-execution and participant evaluation are outside this static design checkpoint. The renamed workflow passes archive/data checks; desktop import remains a presentation-laptop check. The revised PPTX needs a fresh native export before the next local commit.

AI use: AI assisted with this review guide and speaking outline. Presenter allocation, rehearsal duration and submission readiness must be confirmed from actual team work.

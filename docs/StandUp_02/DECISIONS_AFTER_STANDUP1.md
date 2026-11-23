# Decisions after Stand Up 1

Gr_01 - Nguyen Huyen Minh Nhat and Le Tuan Huy. Updated: 23 November 2026.

This records our response to the tutor's feedback as reported by the team. The feedback wording is a summary, not a quotation. The proposed design remains subject to the tutor's response and evaluation.

## Feedback, choice and evidence

| Feedback or issue | Our decision | Reason and evidence | Status |
| --- | --- | --- | --- |
| The project mainly applied the tutorials | Keep the working website and develop a question-led story around it | Existing national trend, ranking and demographics provide a foundation. The reader needs a guided comparison rather than more unrelated controls | Current story/design decision; revised D3 code pending |
| The data exploration needed more depth | Profile all 13 fields and reconcile findings before choosing examples | 187 source controls match: 11 annual, 132 road-user/year and 44 remoteness/year totals. Derived monthly, counterparty and age summaries also conserve the road-user totals | Existing analysis completed; new KNIME Counterparty branch pending |
| The story needed a clear focus | Use one main question with Compare, Events and Ages chapters | The national total can hide different group trends. Counterparty and age describe two different aspects of a group | Current storyboard decision |
| The chart choices needed more ambition | Prototype dumbbell and heatmap, each with an explicit simpler alternative. Compare Sankey with a matrix | Connected positions support two-year comparison. Within-group colour supports compact age profiles. Sankey follows one total; matrix supports between-group comparison | Design candidates specified; evaluation and new implementation pending |
| The scope could become too broad | Keep month/remoteness as supporting EDA, defer bed-day/death ratios, separate comparison and profile years | Missing death fields, transfer-related bed days and absent exposure denominators limit ratio/risk claims. Separate year controls prevent a profile change from altering the comparison silently | Scope/interaction decisions specified; new controls pending |

## Why we chose these questions

Main question: what differences disappear when road injuries become one national total?

| Chapter | Question | Why this question earns a place | Evidence |
| --- | --- | --- | --- |
| Compare | Did every road user follow the national change? | Challenges the assumption that a national decline applies to each group | 2019-2020 national 39,866 to 37,966 (-4.8%), cyclist 7,302 to 8,332 (+14.1%) |
| Events | Which event classifications appear within a road-user group? | Examines what the source records instead of assuming another vehicle is always involved | Cyclists, 2021: Non-collision 3,705/8,163 (45.4%). Unspecified stays separate |
| Ages | How does age composition vary between road users? | Within-group shares compare profiles when group totals differ | Cyclists, 2021: age 40-64 contributes 3,393/8,163 (41.6%). All source sexes and Unknown remain in the denominator |

We chose 2019-2020 for a clear observed contrast after the known 2012/2017 recording breaks. Cyclists provide a substantial absolute increase of 1,030. Pick-up/van occupants also increase, from 260 to 300. We do not claim cyclists were the only group to increase.

The initial profile year is 2021, the latest in this workbook. Its event and age profiles answer separate questions from the earlier change. They do not identify its cause. Counts and composition do not establish individual risk, a unique patient count or fault.

## Explored, retained and deferred

The [EDA report](../EDA_AND_STORY.md) records field checks, missingness and month/remoteness summaries. Those dimensions remain supporting analysis rather than extra global filters. Bed-day/death ratios need resolved definitions and missingness; a ratio cannot be treated as clinical severity without evidence. We retain Unknown and recorded zeros.

The [storyboard](../STORYBOARD.md), [design draft](../design_book/03_design_draft.md) and [coding plan](../CODING_PLAN.md) hold the detailed specifications and alternatives. These decisions extend the current line/bar implementation. The team still needs to check complete course coverage before claiming that a specific chart was never taught.

## What each checkpoint demonstrates

Stand Up 2 explains the response to feedback, the chosen questions, research evidence and design/coding decisions. Huy's confirmed personal contribution is the website/tutorial-based charts and practice running the basic KNIME workflow. Shared analysis/design is described as team work.

Stand Up 3 should show implemented charts, meaningful linked interaction, reconciled exports and actual validation/evaluation evidence. Final refinement follows that feedback. The data checks do not establish usability, and no participant findings or tutor approval are invented here.

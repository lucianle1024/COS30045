# Gr_01 - Stand Up 2 preparation

Huy presents on 23 November 2026. Both members attend. Revised after the team requested a clearer explanation of decisions following Stand Up 1.

Start with the [Markdown notes](Gr_01_StandUp2_Huy_Notes.md). The talk has six main slides and one Q&A audit backup. The 441-word English script has Vietnamese pointer cues and a rehearsal target of about 4:45 before Q&A. An optional 20-second current-web example brings it to about five minutes. Measure the duration aloud. The lecturer confirmed a format longer than three minutes; this rehearsal target is not an official maximum.

## Presentation route

| Slide | Timing | Purpose |
| --- | --- | --- |
| 1 | 0:00-0:45 | Feedback after Stand Up 1 and the decisions we made |
| 2 | 0:45-1:30 | Main question, three supporting questions and scope choices |
| 3 | 1:30-2:10 | Research supporting the year/group comparison |
| 4 | 2:10-3:05 | Why dumbbell and heatmap, with simpler alternatives |
| 5 | 3:05-3:45 | Event evidence and the open Sankey/matrix decision |
| 6 | 3:45-4:45 | Layout/interaction decisions and implementation checkpoint |
| 7 | Q&A only | Data audit and source-control checks |

The response is feedback, decision, evidence and next step. Findings support the choices rather than replace their explanation. The website story keeps Compare, Events and Ages as its reading order. Slide 4 places two encoding choices together to explain the charts efficiently.

## Materials

| Material | Location |
| --- | --- |
| Editable deck | [Open the presentation](https://chatgpt.com/space/page_ea183a7225cc8191ab4a21aee0030aea), export again as `Gr_01_StandUp2.pptx` |
| Script, pointer cues and Q&A | [Gr_01_StandUp2_Huy_Notes.md](Gr_01_StandUp2_Huy_Notes.md) |
| Decisions and reasons | [DECISIONS_AFTER_STANDUP1.md](DECISIONS_AFTER_STANDUP1.md) |
| Copy/commit steps | [Gr_01_StandUp2_Guide.md](Gr_01_StandUp2_Guide.md) |
| Existing assessment files | [Design Book PDF](../design_book/Gr_01_StandUp2_Design_Book.pdf), [KNIME workflow](../../knime/Gr_01_StandUp2.knwf) |

The native presentation is updated. The previously exported PPTX must be replaced with a fresh export. The Design Book and KNIME files from commit a608322 remain the same for this presentation revision.

New D3 chart code, the Counterparty KNIME extension and participant evaluation remain Week 12 work. The Sankey/matrix choice remains open. Huy should describe his personal contribution accurately and explain shared decisions as team work.

## Checks before presenting

- Open the newly exported PPTX and check seven slides, speaker notes and readable labels. Present slides 1-6, then Q&A.
- Rehearse with pointing and a timer. Use the four decision questions in the notes to prepare short answers. Keep the audit detail for Q&A.
- Import the existing KNIME package and check execution on the presentation laptop. Its archive, source data, relative paths and three CSV exports previously passed static checks.
- Submit the current PPTX, Design Book PDF and KNIME separately with the repository link under the tutor's arrangement. The ZIP is for transferring files.
- Both members attend. Huy presents Stand Up 2; confirm the Week 12 date for the other member.

## Optional tools

The generator `tools/build_standup2_pack.py` preserves Markdown notes and can regenerate the existing Design Book PDF and portable workflow. It requires Python, ReportLab, Pillow, Inkscape and the configured DejaVu font path. Rebuilding is unnecessary for this presentation-only revision.

Serve the repository root with `py -m http.server 8000` for the [current website](http://localhost:8000/web/) and [design review](http://localhost:8000/docs/design/preview.html). For a quick example, select 2020/Pedal cyclist, show 8,332 and the linked views, then Reset.

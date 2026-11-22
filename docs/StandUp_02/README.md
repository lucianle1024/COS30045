# Gr_01 - Stand Up 2 preparation

Presentation: 23 November 2026. Presenter: Le Tuan Huy. Both members attend.

Start with the [download and CMD guide](Gr_01_StandUp2_Guide.md), then rehearse the [Markdown speaking notes](Gr_01_StandUp2_Huy_Notes.md). The deck has five main slides and a 470-word English script with Vietnamese pointer cues. Our rehearsal target is 4:30, generally 4-5 minutes before Q&A. The lecturer's longer-than-three-minute clarification, confirmed by the team on 22 November, replaces the original PDF's shorter format. Our target is not an official maximum.

## Materials

| Material | Location | Use |
| --- | --- | --- |
| Editable five-slide deck | [Open presentation](https://chatgpt.com/space/page_ea183a7225cc8191ab4a21aee0030aea) | Export/download as `Gr_01_StandUp2.pptx`; open it on Huy's laptop |
| English script, Vietnamese pointer cues and Q&A | [Gr_01_StandUp2_Huy_Notes.md](Gr_01_StandUp2_Huy_Notes.md) | Prepare in Markdown; a notes PDF is no longer required |
| File list, copying and commit steps | [Gr_01_StandUp2_Guide.md](Gr_01_StandUp2_Guide.md) | Use actual files and Windows CMD |
| Design Book | [Source](../design_book/Gr_01_StandUp2_Draft.md), delivered `Gr_01_StandUp2_Design_Book.pdf` | Processing/EDA and Sections 3.1-3.3, wireframes, alternatives and interactions |
| KNIME package | Delivered `Gr_01_StandUp2.knwf` | Three current export branches, bundled workbook and saved execution data |

The native presentation link uses the current account's access. Export the PPTX to use it on Huy's laptop. The download ZIP is a file-transfer convenience; submit the PPTX, Design Book PDF and KNIME file separately, plus the repository link.

## Talk and progress

| Slide | Rehearsal timing | Evidence |
| --- | --- | --- |
| 1 | 0:00-0:45 | Huy's actual contribution, feedback and the national/cyclist contrast |
| 2 | 0:45-1:30 | Audit of all 13 fields and 187 matched published control totals |
| 3 | 1:30-2:45 | Dumbbell and heatmap, their questions, encodings and alternatives |
| 4 | 2:45-3:30 | Cyclist event classifications and the Sankey/matrix choice |
| 5 | 3:30-4:30 | Website layout, linked state, coding plan and Week 12 scope |

Compared with Stand Up 1, the work adds a verified question-driven story, deeper field checks and explicit design decisions. The new production D3 charts, Counterparty KNIME extension and participant evaluation remain Week 12 work. The current website remains the tutorial-based implementation.

An optional 20-30 second current-web example after slide 5 brings the talk to about five minutes: select 2020/Pedal cyclist, show 8,332 and the linked views, then Reset. Use the full design preview and detailed Q&A when asked rather than extending the main talk.

## Rebuild outputs if needed

The ready files are included in the download; rebuilding is optional. The existing generator requires Python, ReportLab, Pillow, Inkscape and the DejaVu fonts at its configured path. It was run in the Linux preparation environment; Windows dependency setup is not part of the CMD copying steps.

```text
python3 tools/build_standup2_pack.py --output ../standup2_submission
```

The command writes the Design Book PDF, Markdown notes, portable KNIME package and static check report. It does not export the native presentation. The [archived workflow diagram](current_workflow.svg) records the existing three-branch pipeline. The package changes the workflow root and team annotation; raw data, node settings, output CSVs and cached data are preserved.

## Checks and laptop preparation

- The deck uses editable marks, a native control-total table and a layout diagram. All five slides were visually reviewed; the reordered audit and event slides were rendered again for the longer format. The script matches the displayed counts and Huy's confirmed contribution.
- The KNIME archive passes integrity/XML checks. It contains `.savedWithData`, 10 nodes and saved EXECUTED state. The bundled workbook matches the source hash; its 11/132/1,683-row exports match the processed files byte for byte. Reader/writer settings retain workflow-relative paths.
- The 12-page Design Book PDF was rendered and reviewed. The notes stay in Markdown. Data and existing website checks remain separate from usability evidence for the proposed charts.
- On Huy's laptop: export/open all PPTX slides and speaker notes; re-import the renamed KNIME workflow and check reading/execution; rehearse aloud with pointing and a timer. Actual speaking duration and desktop KNIME execution remain local checks.
- Submit the three assessment files separately on 22 November, before the user-confirmed 23 November presentation, plus [the repository link](https://github.com/lucianle1024/COS30045). Both members attend. GitHub Classroom and Mercury are not required for this team.

For the current website and static design review, serve the repository root:

```bat
py -m http.server 8000
```

Current website: http://localhost:8000/web/

Design review: http://localhost:8000/docs/design/preview.html

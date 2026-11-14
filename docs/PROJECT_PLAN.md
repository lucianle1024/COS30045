# Individual project checkpoints

Updated: 13/11/2026

Scope: Australian hospitalised road injuries, 2011-2021. Three linked D3 visualisations answer questions about time trends, road users and demographics.

| Work | Implemented | Verified | Accepted by student |
| --- | --- | --- | --- |
| KNIME processing and three CSV exports | Yes | All 10 nodes executed in KNIME 5.12.0 LTS; independent raw-data reconciliation passed | Pending |
| D3 website | Yes | Default data, year selection, road-user selection, bar click, Enter toggle, Reset and data table checked in Chromium | Pending |
| Narrow layout | Yes | 340 CSS-pixel viewport checked using browser zoom; no page overflow or clipped SVG labels | Pending |
| Loading-error state | Yes | Missing CSV produced a visible error; recovery checked before packaging | Pending |
| Submission documents and hosting | Pending | Not yet verified | Pending |

## Completed data checks

- 117,919 meaningful raw records; 86,140 records retained after filtering Traffic.
- No duplicate Traffic keys across the eight source dimensions.
- All 11 annual totals match the source T1 table.
- All three CSVs reconcile with the raw data, including zeros and unknown categories.
- Counts for unknown age and the combined other/not-stated sex category are retained.

## Next work

1. Review the actual workflow and website in KNIME and a local browser.
2. Finalise the data story, wireframe and storyboard, recording the reasons for chart and interaction choices.
3. Prepare the draft Design Book and a Stand Up presentation of no more than five minutes.
4. Run a usability evaluation with real participants and record the resulting changes.
5. Complete the final PDF, KNIME export, required hosting and submission links.

## Submission checkpoints from the supplied PDFs

| Deliverable | Date shown in PDF | Required material |
| --- | --- | --- |
| Stand Up 1 | 22/11, 23:59 | PPTX, draft Design Book, KNIME with data and individual/team name, GitHub Classroom link in comments |
| Final project | 04/12, 23:59 | Design Book PDF, KNIME with all used data and exported files, Mercury and GitHub links in comments |

The Stand Up instructions also require submission two nights before the class presentation. Check the live class schedule and Canvas deadlines. ZIP files are not accepted for Stand Up 1.

This is an implementation checkpoint, not evidence of completed usability testing, lecturer acceptance or deployment. Mobile hardware, screen readers and the Mercury environment have not been tested.

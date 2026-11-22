# Hospitalised Road Injuries in Australia

Our COS30045 team project explores hospitalised road injuries in Australia from 2011 to 2021. The first website shows time trends, road users and demographics. We are developing a deeper story about differences hidden by the national total; the analysis and design decisions are documented below.

## Run the website

From this project folder in PowerShell:

```powershell
py -m http.server 8000 --directory web
```

Open http://localhost:8000/. If the Python launcher is unavailable, try `python` in place of `py`. VS Code Live Server can also serve `web/index.html`.

D3 is included locally, so the website does not need a CDN. Open the page through an HTTP server so the CSV files can load.

## Use the KNIME workflow

1. Import `knime/COS30045_Project.knwf` into KNIME Analytics Platform 5.12.0 LTS. For the next submission, export the refreshed workflow under a name containing Gr_01.
2. Open the workflow. The workbook, processed CSVs and executed node data are included.
3. To reproduce the processing, choose Reset all and Execute all. The CSV Writer nodes overwrite only their configured files inside the workflow's data folder.
4. Copy the three regenerated CSVs from the workflow's `data/processed` folder to this project's `data/processed` and `web/data` folders.

The workflow uses 10 nodes: Excel Reader, Row Filter, Column Filter and Column Renamer, followed by three GroupBy and CSV Writer branches.

| File | Grouping | Website use |
| --- | --- | --- |
| `annual_totals.csv` | Year | Line chart |
| `road_user_by_year.csv` | Year and road user | Road-user ranking and selected-group trend |
| `age_sex_by_road_user.csv` | Year, road user, age group and sex | Demographic chart and accessible table |

## Data and interpretation

- Original file: `data/raw/hospitalisation_injury_publication_sep2023.xlsx`, worksheet `raw`.
- Source: [BITRE Hospitalised Injury Data](https://www.bitre.gov.au/publications/ongoing/hospitalised-injury), September 2023 publication, using AIHW National Hospital Morbidity Database data.
- Filter: `Cause of injury = Traffic`. Measure: sum of `Hospitalisations`. Raw rows are aggregated records, not individual patients.
- The source workbook's Hospitalisations field subtracts the recorded died-in-care cases from Count of cases. The dictionary defines these deaths as occurring within 30 days of admission.
- Unknown age and the combined source sex category `intersex or indeterminate or missing` are retained. The website labels the latter Other / not stated.
- Counts are not population-adjusted risk. Age-group widths differ. The 2012 Victoria and 2017 NSW recording changes limit comparisons across the affected years.

The original dictionary and assessment files are in `docs/`.

## Checks

The KNIME exports were reconciled against the raw Traffic records and the published T1 annual totals. The check also compares the processed files with the copies loaded by the website.

```powershell
py tools/verify_data.py
npm test
```

The Python check uses only the standard library. The JavaScript tests use Node's built-in test runner; no npm dependencies need to be installed.

Current checks: 117,919 raw records, 86,140 Traffic records, 11 annual control totals matched, and CSV outputs with 11, 132 and 1,683 rows. The exact reconciliation result is in `data/processed/verification.json`.

## AI use and attribution

I used AI assistance to prepare and check the workflow configuration, build the D3 charts, and write the validation checks. Prompt summaries are included in the workflow annotations and source comments. The workflow configuration draws on the supplied Week 4 and Week 6 class examples and a bundled KNIME Excel Reader example.

The D3 bundle is version 7.9.2, downloaded from [D3's official site](https://d3js.org/getting-started). Its license is included in `web/vendor/D3-LICENSE`.

## Project status

The first data pipeline and website are available, and Stand Up 1 has taken place. The 21 November audit and EDA now support a Week 11 design pack added on 22 November: desktop/mobile wireframes, labelled chart alternatives, three Design Book section drafts and a coding handoff. New D3 charts, the KNIME extension and participant evaluation remain pending.

- [EDA findings, data-quality limits and reproduction commands](docs/EDA_AND_STORY.md)
- [Revised storyboard, chart alternatives and interaction plan](docs/STORYBOARD.md)
- [Stand Up 2 design preview](docs/design/preview.html) - open directly for the embedded sketches
- [What to prepare and where to review it](docs/STANDUP_2_REVIEW.md)
- [Design Book Sections 3.1-3.3](docs/design_book/03_design_draft.md)
- [Coding plan: inputs, shared state, modules and acceptance](docs/CODING_PLAN.md)
- [Week 11 and Week 12 stand-up plan and progress](docs/STANDUP_2_3_PLAN.md)

To view both the design preview and website through one server, run `py -m http.server 8000` from the repository root. Open http://localhost:8000/docs/design/preview.html for design evidence, or http://localhost:8000/web/ for the current website. The design figures are static and do not implement the proposed filters. Rebuild them with `py tools/build_design_pack.py` when Matplotlib and NumPy are available.

The older implementation checkpoint remains in `docs/PROJECT_PLAN.md`; use the dated documents above for the current analysis and stand-up milestones.

This development ZIP is for transferring the project files. For Stand Up 1, submit the required PPTX, draft Design Book and KNIME file separately, with the GitHub Classroom link in the submission comment. The supplied Stand Up instructions do not allow ZIP submissions.

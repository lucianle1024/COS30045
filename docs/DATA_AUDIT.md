# Data Audit - BITRE National Hospitalised Injury

Updated: 13 November 2026

## Sources and scope

- Dataset: `data/raw/hospitalisation_injury_publication_sep2023.xlsx`
- Dictionary: `docs/hospitalised-injury-data-dictionary-september-2023.pdf`
- Source: https://www.bitre.gov.au/publications/ongoing/hospitalised-injury
- Coverage: Australia, calendar years 2011-2021.
- Data origin: AIHW National Hospital Morbidity Database, published by BITRE.

The workbook contains 10 sheets: `Cover`, `Index`, `T1`, `T2`, `T2.1`, `T2.2`, `T3`, `T3.1`, `T4`, and `raw`. We should build KNIME analysis from `raw`, using published tables to validate aggregations.

## Verified structure

- 117,919 data records, excluding the header and 10 blank formatted rows.
- 13 columns; 86,140 records have `Cause of injury = Traffic`.
- Dimensions: `Calendar year`, `Month`, `ABS remoteness area`, `Cause of injury`, `Age group`, `Sex`, `Road user`, `Counterparty`.
- Measures: `Count of cases`, `Bed days`, `Died_cases`, `Died_bed_days`, `Hospitalisations`.
- No duplicate combinations of the eight dimension fields were found in the raw records.

## Validation

For `Traffic` records, the sum of `Hospitalisations` matches sheet `T1` for all 11 years.

| Year | Hospitalisations |
|---|---:|
| 2011 | 34,033 |
| 2019 | 39,866 |
| 2020 | 37,966 |
| 2021 | 39,505 |

`Count of cases` and `Hospitalisations` are not interchangeable. For 2011 traffic records, their sums are 34,294 and 34,033 respectively. The workbook contains blank `Died_cases` values for 2021: do not interpret this as evidence of zero deaths or publish death-trend conclusions without checking the source methodology.

## Data quality and interpretation

- Some `Count of cases` cells are empty while bed days are recorded; do not automatically delete these rows. The Data Dictionary describes transfers and episodes contributing bed days without an additional counted case.
- The raw sheet contains 12,440 records with `ABS remoteness area = Missing`, 177 with `Age group = Missing`, and 1,128 with `Sex = intersex or indeterminate or missing`. These are explicit category values.
- The Data Dictionary identifies a break in the time series in Victoria from 2012 and an admission-policy change in NSW from 2017. Interpret changes across those periods carefully.
- Counts are not population-adjusted risks. Raw count differences between groups do not establish higher individual risk.
- This September 2023 dataset is subject to revision; keep the Data Dictionary linked to the analysis.

## First KNIME workflow

1. Read Excel sheet `raw` with Excel Reader.
2. Filter `Cause of injury = Traffic`; retain 2011-2021.
3. Keep year, road-user group and `Hospitalisations` for the first pass.
4. Group by year, sum `Hospitalisations`, verify against `T1` for every year.
5. Group by year and road-user group, sum `Hospitalisations`, verify against `T2`.
6. Create EDA charts and export processed CSV only after those checks pass.

This is a read-only audit of the Excel workbook, not a completed KNIME workflow. KNIME evidence, interactive visualisations, actual usability feedback, and final interpretation remain pending.

# Coding plan for the revised road-injury story

Updated: 22 November 2026. Design handoff for Gr_01, not completed chart code.

We will extend the existing static D3 website rather than introduce a framework. `web/data.js` already loads and validates CSVs, `web/charts.js` renders charts and `web/app.js` coordinates selection. The [design draft](design_book/03_design_draft.md) defines the visual choices; [preview.html](design/preview.html) collects sketches.

## Data contract

| Input | Fields used | Source and status |
| --- | --- | --- |
| `annual_totals.csv` | `year`, `hospitalisations` | Existing KNIME output in `data/processed` and `web/data`; national context |
| `road_user_by_year.csv` | `year`, `road_user`, `hospitalisations` | Existing KNIME output; all 12 categories for two-year comparison |
| `age_sex_by_road_user.csv` | `year`, `road_user`, `age_group`, `sex`, `hospitalisations` | Existing KNIME output; sum all source sexes to reproduce the analysis age summary |
| Planned `counterparty_by_road_user.csv` | `year`, `road_user`, `counterparty`, `hospitalisations` | New KNIME GroupBy(year, road user, counterparty), sum Hospitalisations; analysis CSV is currently a reference only |

The two-year change CSV is a control fixture, not a second population to sum into the road-user data. The Python analysis files may include `within_road_user_pct`; production code computes percentages from reconciled counts to avoid using rounded values as inputs. No new monthly, remoteness or bed-day website input is required for this design.

Before connecting counterparty data, add a branch after the cleaned Traffic fields in KNIME and retain Counterparty in the shared Column Filter. Keep the existing branch keys and outputs unchanged. Save raw data and every used output inside the portable workflow, use workflow-relative paths, execute the new branch and export under a filename containing Gr_01. A named file is not proof that data is bundled: inspect the exported archive and test re-import/reset/execute in a separate KNIME location.

Compare the new KNIME output with `data/analysis/counterparty_by_road_user.csv` by its three dimension keys, ignoring the exploratory percentage column. Every year/road-user sum must match the existing road-user export. Compare age aggregation over all source sexes with `data/analysis/age_by_road_user.csv`. Copy only verified outputs into `data/processed` and `web/data`, then extend the existing reconciliation checks. The three transformed exports still represent one workbook, not independent data sources.

## Shared state and constants

Proposed state:

```js
const defaults = {
  comparisonYears: [2019, 2020],
  detailYear: 2021,
  roadUser: 'Pedal cyclist',
  ageMetric: 'share',
  counterpartyFocus: null,
};
```

Reset must create a new year-pair array rather than mutate the defaults. Keep the old application's single `year` separate while migrating to avoid accidentally coupling comparison and detail updates. One state update should compute validated views first, then render all affected charts, captions and tables together.

| Shared constant | Contract |
| --- | --- |
| Years | Available source years, 2011-2021; first comparison year must be earlier |
| Recording breaks | 2012 and 2017; show a comparison warning for any break where first year < break <= second year |
| Road-user order | All 12 groups, descending 2019 count with label tie-break; hold order across year selections |
| Age order | 0-7, 8-16, 17-25, 26-39, 40-64, 65-74, 75+, Missing; display Missing as Unknown |
| Year encodings | First year navy circle; second year rust diamond; selection uses outline/bold |
| Heatmap domains | Share 0-100; count 0 to maximum cell across the complete loaded age aggregation |
| Event grouping | Fixed exhaustive mapping in Design Book 3.2; unspecified never merged with non-collision |
| Formatting | Comma-separated integers; signed changes; one decimal percent; undefined share/change shown as not available |
| Narrow breakpoint | Below 740 px: selected-group bars with all categories accessible in tables |

Keep these in a small `web/constants.js` when implementation starts. Use the same labels, domains, defaults and mapping in the charts, controls and tables.

## Code responsibilities

| File | Planned responsibility |
| --- | --- |
| `web/data.js` | Parse counts, validate dimensions and totals; derive comparison, counterparty and age views without changing raw rows |
| `web/constants.js` | Defaults, category orders, year encodings, formatting helpers and fixed display grouping |
| `web/charts.js` | Keep the existing trend; add `drawComparison`, `drawAgeProfile` and `drawCounterparty` with view data and callbacks |
| `web/app.js` | Native controls, shared state, captions, exact tables, focus details, Reset and resize updates |
| `web/index.html`, `web/styles.css` | Story chapters, labelled controls, accessible names, focus styling and compact layouts |
| `tools/verify_data.py`, `tools/data.test.js` | Extend meaningful data-contract and derived-view checks for new inputs and edge cases |

Use stable join keys: road user for comparison rows, road user + age for heatmap cells, and display category for event nodes/links. D3's keyed data joins associate updates with the correct marks (Observable, n.d.). Check event handlers after updates so selections do not accumulate listeners. The existing local D3 bundle includes primitives needed for a one-source/two-column Sankey: cumulative counts determine ribbon boundaries and cubic paths connect matching boundaries. A general Sankey layout dependency is unnecessary for this restricted candidate; changing to a multi-group network would require revisiting that choice.

## Implementation order and acceptance

| Step | Work | Evidence before moving on |
| --- | --- | --- |
| 1 | Extend and execute KNIME; reconcile new Counterparty output and existing age aggregation | All 132 year/road-user sums agree; source/served files agree; Gr_01 workflow re-imports with bundled data |
| 2 | Derive state-independent comparison and profile views | Default 39,866 -> 37,966; cyclists 7,302 -> 8,332; zero baseline gives undefined percent; invalid pairs do not render |
| 3 | Build dumbbell, national context and chapter table | All 12 rows, fixed year shapes, selection outline, recording-break notes and usable narrow view |
| 4 | Build age heatmap and narrow bars | Default cyclist 40-64 = 3,393 / 8,163; full row sums agree; mode/year changes keep correct domains and table |
| 5 | Build one-group event candidate and alternative table | Default bins 3,705 + 1,854 + 1,575 + 1,029 = 8,163; full table has all 10 source labels; category focus does not filter age |
| 6 | Connect controls, focus details, Reset and error state | Comparison/detail years remain independent; Reset defaults agree everywhere and preserve scroll; keyboard/touch paths work |
| 7 | Review desktop/narrow layouts and run real evaluation | Record actual tasks, observations and any before/after refinements for Week 12; update Design Book to match implemented behaviour |

Data checks should reject blank, noninteger or negative Hospitalisations; duplicate keys; unknown dimension labels; mismatched coverage; nonconserving group mappings and inconsistent served copies. Only absent aggregate combinations become zero after reconciliation, not blank raw measures. A group with a zero total displays counts and an explicit unavailable percentage. Compare rounded display values with a tolerance only when testing rounded values; use integer counts for reconciliation.

Manual acceptance covers default load, a different year pair, a pair crossing 2017, group selection, detail-year change, age metric, category focus, keyboard activation, Escape, Reset, resize and a failed data load. Inspect at approximately 1440 px and 375 px and at browser zoom. These checks are still pending for the new implementation.

## Scope and review record

No second independent dataset, risk denominator or bed-day ratio is introduced in this step. A later source should answer a justified question and be checked for compatible definitions before integration. The full course chart coverage also needs checking before describing any design as outside the taught material.

The design assets can be rebuilt with `py tools/build_design_pack.py` when Matplotlib and NumPy are available. Those libraries generate review figures only; they are not runtime website dependencies. Review checks and current limitations are recorded in [STANDUP_2_REVIEW.md](STANDUP_2_REVIEW.md).

Observable. (n.d.). *Joining data*. D3. Retrieved November 22, 2026, from https://d3js.org/d3-selection/joining

AI use: AI assisted with this handoff and its consistency checks. The plan does not assign personal contributions or claim implementation, KNIME desktop execution or participant results.

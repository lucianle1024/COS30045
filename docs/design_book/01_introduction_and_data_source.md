# Road Crash Hospitalisations in Australia: Trends Across Road User Groups, 2011-2021

Design Book draft - Sections 1.1, 1.2 and 2.1  
Updated: 13 November 2026

## 1 Introduction

### 1.1 Background and Motivation

Road crashes are often discussed in terms of fatalities, but hospital admissions are another important part of their impact. A person can survive a crash and still require hospital treatment, which places pressure on patients, families and health services. Understanding how hospitalisation counts change over time, and which kinds of road users are represented, provides a useful perspective alongside fatality statistics.

The Australian Bureau of Infrastructure and Transport Research Economics (BITRE) publishes national hospitalised injury data covering 2011 to 2021. The national workbook includes information about calendar year, road user type, age group, sex and remoteness of residence. We intend to focus on road user groups and changes over time rather than trying to cover every possible breakdown in one dashboard.

Our primary audience is the general public and students interested in Australian road safety. Road safety communicators could also use the visualisations as a starting point for discussing broad patterns. We assume that visitors may not be familiar with hospitalisation data, so the website should be understandable without specialist knowledge.

Visitors should be able to:

- See how the national number of road-crash hospitalisations changed from 2011 to 2021.
- Compare the number of recorded hospitalisations across road user categories.
- Explore how the pattern for a selected road user group changed over time.
- Understand the main limitations before interpreting a difference as a change in risk.

### 1.2 Visualisation Purpose

The purpose of this project is to tell a focused, evidence-based story about the changing number and distribution of road-crash hospitalisations in Australia. We will use D3.js to build linked explanations and interactive charts based on data processed and validated in KNIME.

The project will address three research questions:

1. How did the national annual count of road-crash hospitalisations change between 2011 and 2021?
2. Which road user groups accounted for the most recorded hospitalisations, and how did their totals compare?
3. How did hospitalisation counts change over time for different road user groups?

A time-series chart can answer the first question; a comparison of road user categories can address the second; and a group-specific time series can help users explore the third. The final chart designs and story conclusions will depend on the KNIME exploration rather than assumptions about the results.

The expected benefit is clearer public understanding of patterns in recorded hospitalisations and the differences between road user categories. We are **not** using raw counts to rank the danger of road user types: the dataset does not provide exposure measures, such as kilometres travelled, and the counts are not adjusted for differences in group size. The visualisations are intended to support informed discussion, not causal or individual-risk claims.

## 2 Data

### 2.1 Data Source and Governance

The primary dataset is the national hospitalised injury workbook released by BITRE in September 2023. BITRE sources national hospital separation data from the Australian Institute of Health and Welfare (AIHW) National Hospital Morbidity Database. A hospital *separation* is an episode of admitted patient care rather than necessarily a unique injured person. BITRE applies inclusion and exclusion rules to estimate hospitalisation cases and limit double counting when care is transferred or split into multiple episodes (BITRE, 2023).

| Item | Description |
|---|---|
| Publisher | Bureau of Infrastructure and Transport Research Economics (BITRE) |
| Underlying source | AIHW National Hospital Morbidity Database |
| Release used | September 2023 |
| Coverage | Australia, calendar years 2011-2021 |
| File | `data/raw/hospitalisation_injury_publication_sep2023.xlsx` |
| Analytical sheet | `raw` (the workbook also provides published summary tables) |
| Data size | 117,919 aggregated raw records across all six cause categories; 86,140 records where `Cause of injury = Traffic` |
| Key dimensions | Calendar year, month, ABS remoteness area, cause of injury, age group, sex, road user, counterparty |
| Main measure | `Hospitalisations` |
| Companion source | `docs/hospitalised-injury-data-dictionary-september-2023.pdf` |

The worksheet includes six categories of cause of hospital admission. For our project we will select `Cause of injury = Traffic`, which is the category BITRE uses for road vehicle traffic accidents. We will sum `Hospitalisations`, **not** `Count of cases`, to reproduce the published hospitalisation totals. As an initial validation, the yearly totals derived from `Traffic` records match the published `T1` table across all 11 years, including 34,033 in 2011 and 39,505 in 2021. These are national counts, not rates.

**Collection and classification.** The source is administrative hospital data recorded using the Australian Modification of the International Classification of Diseases (ICD-10-AM). Road user categories are derived from the external-cause injury codes. Different ICD-10-AM editions were used over the reporting period; care is required when comparing values across years. The published workbook contains grouped counts and dimensions, not names or individual patient identifiers.

**Data quality.** The records are aggregated by combinations of dimensions. The initial file inspection found no duplicate combinations of those dimensions, but this does not remove the need to verify KNIME output. Missing or unknown values are sometimes explicit categories, and blank case values do not automatically mean that a row is invalid. We will retain the original file unchanged, document any exclusions and check processed totals against BITRE's own tables before using them in D3.

**Known limitations.** The Data Dictionary reports a break in comparability in Victoria from 2012 and a change in New South Wales admission policy from June 2017. Both may affect the national series, and their impacts may differ between road user groups. The 2023 release may also be revised. Raw hospitalisation counts are not standardised for road user population size or exposure, so they cannot by themselves establish relative crash risk. These caveats will be displayed in the website and considered when describing trends.

**Privacy and ethical use.** The dataset available for this project consists of grouped administrative counts without direct patient identifiers. We will not attempt to infer individual identities or treat small categories as evidence of individual behaviour. The website will identify the source and release date, avoid unsupported causal conclusions and make uncertainty or missing categories visible where relevant.

The data supports our research questions through the `Calendar year`, `Road user` and `Hospitalisations` fields. KNIME will prepare annual and annual-by-road-user summaries from the `raw` worksheet. This work belongs in Section 2.2 once the workflow has actually been built and checked.

## References - working entries

Bureau of Infrastructure and Transport Research Economics. (2023). *Hospitalised injuries from road crashes* [Data set]. Australian Government. https://www.bitre.gov.au/publications/ongoing/hospitalised-injury

Bureau of Infrastructure and Transport Research Economics. (2023). *Data dictionary: Hospitalised injuries from road crashes* (September 2023). Australian Government. https://www.bitre.gov.au/publications/ongoing/hospitalised-injury

> Draft status: Sections 1.1, 1.2 and 2.1 only. The team's name, members and tutorial details will go on the final title page. Sections 2.2-2.3, KNIME screenshots, actual findings and usability evidence remain pending. Check final source metadata and APA 7 formatting before submission.

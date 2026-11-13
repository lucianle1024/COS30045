# COS30045 Project Plan

Updated: 13 November 2026 (Phase 2.2 draft)

## Goal

Develop an evidence-based D3.js data story about hospitalised injuries from road crashes in Australia (2011-2021), using BITRE data, KNIME for processing and EDA, and a Design Book explaining the decisions. The project is not an unrestricted dashboard.

## Progress

- [x] Repo structure and original source files collected.
- [x] Initial raw-data inspection documented in `docs/DATA_AUDIT.md`.
- [x] Draft intended audience, research questions and Design Book Sections 1.1, 1.2 and 2.1 in `docs/design_book/01_introduction_and_data_source.md`.
- [ ] Team review of research scope and audience before KNIME EDA.
- [ ] Produce and validate KNIME workflow with all input and exported data.
- [ ] Complete Stand Up 1 presentation and Design Book draft.
- [ ] Create wireframe, storyboard and D3.js website.
- [ ] Conduct real usability testing, refine website and complete Design Book.
- [ ] Validate final submission against all official rubric criteria.

## Next step

Build and verify a KNIME workflow starting from the Excel `raw` sheet, filtering `Traffic` and grouping `Hospitalisations` by year and road user. Compare output with tables T1 and T2 before writing Data Processing and EDA results.

## Milestones

| Target | Deliverable | Acceptance evidence |
|---|---|---|
| 14 Nov | Data understanding and questions | Reviewed `DATA_AUDIT.md`, audience and focused questions |
| 17 Nov | KNIME / EDA | Working `.knwf`, source and output data, summary statistics and charts |
| 21 Nov | Stand Up 1 ready | 5-minute slides, Design Book draft and reproducible KNIME demo |
| 22 Nov | Stand Up 1 submission | Canvas files and links required by the course |
| 27 Nov | D3 prototype | Interactive charts backed by verified processed CSV |
| 30 Nov | Website / design evidence | Responsive website, storyboard, interactions and design rationale |
| 3 Dec | Testing / documentation | Real usability feedback, documented refinements, APA 7 and GenAI declaration |
| 4 Dec | Final submission | Design Book PDF, KNIME `.knwf`, hosted site and repository link |

## Provisional research direction

How have hospitalisations associated with road crashes changed among road-user groups in Australia from 2011 to 2021?

- What changed in the total national annual counts?
- Which road-user groups account for the largest counts?
- Which groups show distinct changes over time?

These are research questions, not pre-verified conclusions. Check the dataset's comparability notes and measure definitions before settling the narrative.

## Rubric quality checks

- Introduction: audience, motivation, tasks and questions.
- Data source and governance: provenance, structure, data quality, privacy and limitations.
- Processing and EDA: verified KNIME workflow with complete data and evidence of analytical decisions.
- Website and visuals: wireframe, storyboard, justified choices of charts, encodings and labels.
- Interaction: purposeful D3.js-driven interaction and appropriate technical complexity.
- Iteration and validation: genuine usability participants, notes, refinements and accessibility evidence.
- Coding: readable, appropriately commented source and AI-prompt summary.
- Storytelling, references and reflection: connected narrative, APA 7, honest GenAI declaration.

Both team members must contribute to and understand both design and programming. Assign responsibilities together; do not invent contribution records.

## Constraints and submission risks

- Keep the existing structure; use plain HTML, CSS, JavaScript, D3.js and KNIME unless a rubric requirement justifies another tool.
- Preserve the original workbook; do not invent missing values or results.
- Stand Up 1 is listed as due 22 November 2026 at 23:59; check the tutorial's earlier-submission requirement.
- The official materials specify GitHub Classroom and Mercury hosting. If the team intends alternatives, confirm acceptance with the tutor before submitting.

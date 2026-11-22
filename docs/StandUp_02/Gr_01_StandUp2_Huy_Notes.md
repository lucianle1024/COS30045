# Stand Up 2 - Huy's speaking notes

Gr_01 - 23 November 2026. Presenter: Le Tuan Huy. Both members attend.

## Thời lượng và cách dùng

Giảng viên đã thông báo Stand Up 2 và 3 cần/nên trình bày hơn 3 phút, theo xác nhận của nhóm ngày 22/11. Hướng dẫn mới này thay cho mốc dưới 3 phút trong PDF ban đầu. Mục tiêu đề xuất cho bài này là khoảng 4:30, trong khoảng 4-5 phút, chưa tính Q&A. Đây là thời lượng để tập, không phải một giới hạn mới do giảng viên ấn định.

Cả 5 slide đều thuộc bài nói chính. Nói phần tiếng Anh trong bảng. Cột bên phải là hướng dẫn thao tác bằng tiếng Việt. Nếu cần rút gọn, giữ finding, lý do chọn chart và bước tiếp theo. Chi tiết kiểm tra, công thức và code nằm ở phần Q&A sau script.

| Slide | Mốc tập | Ý chính |
| --- | --- | --- |
| 1 | 0:00-0:45 | Đóng góp của Huy, feedback và finding nổi bật |
| 2 | 0:45-1:30 | Nhóm đã đào sâu và kiểm tra dữ liệu như thế nào |
| 3 | 1:30-2:45 | Dumbbell và heatmap trả lời câu hỏi gì, vì sao chọn |
| 4 | 2:45-3:30 | Counterparty và quyết định Sankey/matrix |
| 5 | 3:30-4:30 | Layout, tương tác, coding plan và mốc Stand Up 3 |

## Slide 1 - Beyond the Total

Time: 0:00-0:45.

| Say in English | Point to / action |
| --- | --- |
| Hi, I am Huy. I helped build our website and charts using the course tutorials, and practised running the basic KNIME workflow. | Giới thiệu phần Huy trực tiếp tham gia. Không nói Huy làm toàn bộ audit hay tự dựng workflow mới. |
| After Stand Up 1, our team moved beyond describing totals and rankings. We explored whether the national trend represented every road user. | Chỉ hai dòng Stand Up 1 / Stand Up 2 phía trên. |
| Between 2019 and 2020, total hospitalisations fell by 4.8%, while cyclist hospitalisations rose by 14.1%. | Chỉ -4.8% bên trái rồi +14.1% bên phải. Chỉ hai cặp số đếm bên dưới để nhấn mạnh cùng giai đoạn. |
| That contrast gives our story a specific question: which differences disappear in a national total? Counts alone cannot establish individual risk. | Chỉ câu hỏi và dòng exposure data phía dưới. Chuyển sang bằng chứng kiểm tra ở slide 2. |

## Slide 2 - Data exploration and checks

Time: 0:45-1:30.

| Say in English | Point to / action |
| --- | --- |
| We expanded the exploration to all 13 source fields, including counterparty and bed-day measures. We checked categories, missing values and zero counts before choosing the story. | Chỉ số 13. Giải thích audit gồm kiểu dữ liệu, nhóm giá trị, giá trị trống và số 0. Không đọc tên cả 13 cột. |
| The analysis matches 187 published control totals: 11 annual totals, 132 road-user and year totals, and 44 remoteness and year totals. | Chỉ 187 rồi lần lượt ba hàng T1, T2, T4. Control total là tổng đối chiếu từ bảng do nguồn công bố. |
| The monthly, counterparty and age summaries also reconcile to the road-user totals. These checks support the finding, while the existing technical tests give further validation. | Chỉ hai dòng dưới bảng. Không đọc chi tiết từng test. |
| The revised charts still need browser checks and participant evaluation. | Chỉ dòng cuối. Đây là giới hạn của bằng chứng hiện tại. |

## Slide 3 - Chart choices for comparison and age composition

Time: 1:30-2:45.

| Say in English | Point to / action |
| --- | --- |
| The dumbbell connects two counts on one scale, making direction and magnitude easier to compare. Circles and diamonds identify the years. | Chỉ tiêu đề Dumbbell, hai ký hiệu 2019/2020 và một đường nối. |
| The cyclist row shows an increase of 1,030 hospitalisations. A selected row will receive an outline, keeping the year colours consistent. Grouped bars are familiar, but use more space. | Chỉ hàng Pedal cyclist, nhãn +1,030 và khung hàng. Dùng will vì đây là đặc tả tương tác, chưa phải chart D3 mới đã chạy. |
| The heatmap answers a different question: how does age composition vary across groups with different totals? In 2021, ages 40-64 account for 41.6% of cyclist hospitalisations. | Di chuyển sang heatmap. Chỉ nhãn 2021, hàng Pedal cyclist và ô 41.6 ở cột 40-64. |
| Each percentage uses the full road-user total, including Unknown and all source sex categories. A count mode will answer a different question about group size. | Chỉ dòng Within each road-user total (%) và Unk. ở cột cuối. |
| Bars give more precise comparisons for one group and suit mobile screens. Exact tables support both designs. These 2021 profiles do not explain the earlier increase. | Chỉ dòng alternative bên dưới. Nhắc lại nhãn 2021 trước khi chuyển slide. |

## Slide 4 - Recorded event classifications

Time: 2:45-3:30.

| Say in English | Point to / action |
| --- | --- |
| We also asked whether cyclist hospitalisations always record another vehicle. In 2021, 3,705 of 8,163 were classified as non-collision transport accidents, or 45.4%. | Chỉ tổng 8,163 bên trái, rồi nhóm Non-collision và nhãn 45.4% ở trên cùng bên phải. |
| We keep unspecified events separate instead of assigning them to collisions or non-collisions. | Chỉ Other and unspecified transport accidents, 1,854 / 8,163. |
| The Sankey is a design candidate for following one total into categories. A matrix may support comparisons across road users more clearly. We will evaluate that choice. | Chỉ các dải nối rồi dòng Alternative: a matrix phía dưới. Không mô tả Sankey như code D3 đã hoàn thành. |
| Link widths represent hospitalisations. The categories do not establish fault. | Chỉ độ dày dải nối và dòng giới hạn cuối slide. |

## Slide 5 - Website design and coding plan

Time: 3:30-4:30.

| Say in English | Point to / action |
| --- | --- |
| The layout guides readers from the opening contrast to comparison and then detail profiles. Comparison years stay separate from the detail year, while road-user selection links the profiles. | Chỉ bốn khối bên trái từ trên xuống. Dừng ở Detail year: 2021 để phân biệt với Compare years: 2019 and 2020. |
| Our design drafts and sketches are ready. Next, we will reconcile the new KNIME counterparty export, then build the dumbbell and age view in D3. | Chỉ bước 1 và 2 bên phải. Các CSV annual, road-user và age/sex hiện có sẽ được tái sử dụng. |
| We will keep the existing data, charts and app modules. Shared state, age ordering and colour meanings will keep the charts and their tables consistent. | Chỉ hai dòng Shared state / Shared constants. Đây là coding plan cụ thể để giải thích cách nối các view. |
| Our open decision is whether the Sankey helps readers more than a matrix. Stand Up 3 will demonstrate working charts, interactions and validation evidence. Final refinements will follow the evaluation. | Chỉ bước 3, Open decision và dòng Week 12. Kết thúc, chuyển sang Q&A. |

## Demo web ngắn nếu cần

Bài chính có thể dùng đủ 5 slide. Nếu giảng viên muốn xem web và thời gian cho phép, thêm khoảng 20-30 giây sau slide 5, đưa tổng bài nói về khoảng 4:50-5:00. Đây là ví dụ từ website hiện tại.

1. Mở `http://localhost:8000/web/` bằng server ở repo root.
2. Chọn năm 2020 và Pedal cyclist. Chỉ tổng 8,332 cùng trend và demographic view được cập nhật.
3. Bấm Reset để về 2021/all road users. Quay lại slide hoặc chờ câu hỏi.

Say: "This is the current website I helped build. Selecting 2020 and Pedal cyclist updates the linked views and shows 8,332 hospitalisations. The new comparison and composition designs are the next implementation step."

Nếu chuyển cửa sổ hoặc tải trang mất thời gian, dùng slide. Không mở thêm nhiều bộ lọc trong bài nói chính.

## What Huy should be ready to show

Huy contributed to the website and tutorial-based chart implementation and practised running the basic KNIME workflow. Use "our team" for the shared analysis and design work.

Before presenting, open the existing website and identify one chart or interaction Huy personally worked on. Huy should be able to explain that code without reading comments. Useful files to review are `web/charts.js`, `web/app.js` and `web/data.js`. These file suggestions are places to inspect, not a claim that Huy authored every line.

Q&A web route: open the existing website, choose year 2020 and Pedal cyclist, and locate 8,332 hospitalisations. Explain how that selection updates the group trend and demographic view. Reset restores 2021/all road users. This is the existing working website, while the proposed two-year dumbbell and heatmap remain sketches.

## Q&A - data and interpretation

### What does a raw row represent?

Short answer: "A row is an aggregated combination of dimensions. We filter Traffic and sum Hospitalisations, rather than counting rows."

Remember: the source has 117,919 raw records and 86,140 Traffic records. These are record counts, not hospitalisation totals. A hospitalisation also does not necessarily identify a unique person.

### Why compare 2019 and 2020?

Short answer: "That pair contains the contrast we found and avoids crossing the known 2012 and 2017 recording breaks. It still does not establish a cause."

National: 39,866 to 37,966, a decrease of 1,900. Cyclists: 7,302 to 8,332, an increase of 1,030. Percentage change divides the difference by the first year's count.

### Did only cyclists increase?

Short answer: "No. Pick-up or van occupants increased from 260 to 300, or 15.4%. We highlight cyclists because their absolute increase is much larger."

Do not say cyclists had the largest percentage increase or that COVID caused the change. The present analysis does not establish either claim.

### What exactly does 41.6% mean?

Short answer: "It is 3,393 cyclist hospitalisations aged 40-64 divided by all 8,163 cyclist hospitalisations in 2021. The denominator includes Unknown and every source sex category."

Slide 3 displays three selected road users. The full design has all 12. Unk. means Unknown. The age bands have unequal widths, so this is composition across categories rather than an age-specific risk measure.

### How did the team check the findings?

Short answer: "We reconcile the sums against the workbook's published controls and check the processed and website copies. The deeper age and counterparty summaries also match the road-user totals."

The analysis audit matches 11 annual controls, 132 road-user/year controls and 44 remoteness/year controls. The analysis records 9 Python checks and 6 existing JavaScript tests passing. Those results concern data and derived views. They do not establish usability of the proposed design.

### Why not add bed-day severity or risk rankings?

Short answer: "The source has missing death measures and transfer-related bed days, and we do not have compatible exposure denominators. We need to resolve those definitions before adding a ratio."

In 2021, both death fields are blank in all 7,811 Traffic records. Across Traffic data, 4,899 records have zero Hospitalisations and positive Bed days. Blank is not the same as observed zero. Age composition is our third chapter for the current design.

## Q&A - design and implementation

### Why a dumbbell instead of grouped bars?

Short answer: "Connected positions make a two-year difference clear with fewer marks. Bars are familiar, but take more space. Small differences still need exact values."

Both use a common quantitative scale. Year colour and shape identify the two observations. An outline identifies the selection. Do not recolour a year point to mean "selected".

### Why a heatmap instead of another bar chart?

Short answer: "It puts many age profiles in a compact grid. Within-group percentages let us compare composition when totals differ. Bars are more precise for one group."

Count mode and share mode answer different questions. Mode changes must update the legend, captions and table together. The percentage scale stays at 0-100 across years. Unknown stays in the denominator.

### Why is Sankey versus matrix still an open decision?

Short answer: "The Sankey follows a selected road-user total into recorded categories. A matrix makes comparison across groups easier. We plan to evaluate which supports the reader's task."

For cyclists in 2021, Non-collision transport accident is 3,705 of 8,163 (45.4%). Other and unspecified transport accidents is a separate 1,854 (22.7%). A Sankey link describes a classification, not a patient journey or fault. The full sketch and alternative are in Design Book 3.2.

### What changes when a reader selects something?

Short answer: "Comparison-year controls update the comparison. The detail-year control updates the profiles. Road-user selection links those profiles. Shared state keeps their captions and tables aligned."

Proposed defaults: comparison 2019/2020, detail year 2021, Pedal cyclist and age percentage mode. Reset restores those defaults and keeps scroll position. Focusing a counterparty highlights it but does not filter age data.

### How will the team organise the code and data?

Short answer: "We keep the existing data, charts and app modules. We reuse the annual, road-user and age/sex CSVs, and add the counterparty CSV after KNIME reconciliation. Shared constants hold ordering and colour meanings."

`data.js` validates inputs and derives views. `charts.js` renders the marks. `app.js` handles controls and shared selection. Planned `constants.js` holds defaults, age order and encoding meanings. D3's keyed data joins associate marks with the same category when views update.

### Can Huy explain the existing D3 implementation?

Short answer: "I worked on the website and tutorial-based chart implementation. The app updates selection state, builds the corresponding view and redraws the affected charts and table."

Prepare one example Huy actually worked on. In the current code, `app.js` handles the year/road-user controls, `buildView` derives the selected trend and demographics, and the drawing functions update the marks. `web/data.js` validates nonnegative integer counts and matching totals. The existing Reset restores 2021/all road users. The proposed new Reset will have different defaults and still needs implementation.

### What is implemented, and what will Week 12 add?

Short answer: "The existing website and basic pipeline work. The revised charts are currently sketches with a coding plan. Week 12 will demonstrate new chart code, interactions and validation evidence."

The new analysis CSVs are exploratory Python outputs, not yet final KNIME exports or production website inputs. Do not describe a static sketch as a working chart. Do not claim that every chart is outside the course material before checking the full teaching coverage.

## Tonight and tomorrow

- Export the five-slide deck as `Gr_01_StandUp2.pptx` and check all slides and notes on the presentation laptop.
- Import `Gr_01_StandUp2.knwf`. Confirm the bundled workbook, the three executed export branches and workflow-relative paths. Desktop re-import of this renamed package remains a local check.
- Rehearse the script aloud with pointing and a timer. Aim around 4:30, with the lecturer-confirmed longer format. If it runs long, shorten the wording before increasing speed.
- Have the design review and existing website ready for Q&A. The main talk uses all five slides. A short demonstration should keep the total around 5 minutes.
- Submit the PPTX, Design Book draft PDF and KNIME file separately, plus the agreed GitHub link, on 22 November, the night before the user-confirmed 23 November presentation. Do not submit a ZIP.
- Both Huy and Nhat attend. Huy presents Stand Up 2. Confirm the Week 12 date with the tutorial schedule.

AI use: AI assisted with these notes and the presentation. Huy should rehearse the reasoning and use his own words. The script reflects the personal work the user confirmed. It does not assign Huy the deeper audit or claim completed participant testing.

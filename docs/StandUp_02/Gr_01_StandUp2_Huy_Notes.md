# Stand Up 2 - Huy's speaking notes

Gr_01 - 23 November 2026. Presenter: Le Tuan Huy. Both members attend. Revised on 23 November to explain decisions after Stand Up 1.

## Thời lượng và cách dùng

Bài chính gồm 6 slide, khoảng 4:45 trước Q&A. Slide 7 là audit dự phòng, chỉ mở khi được hỏi. Script có 441 từ tiếng Anh để Huy có thời gian trỏ, dừng và chuyển slide. Đây là mục tiêu tập, không phải giới hạn mới của giảng viên. Giảng viên đã xác nhận Stand Up 2 và 3 cần/nên hơn 3 phút.

Mạch nói: nhận xét của thầy, quyết định của nhóm, câu hỏi được chọn, bằng chứng và phương án thiết kế, rồi bước tiếp theo. Mỗi slide chỉ nói phần Say in English. Không đọc hết bảng hoặc từng nhãn trên chart. Phần Q&A là tài liệu chuẩn bị, không đọc nối vào bài nói. Kết bài tại slide 6, không tự chuyển sang slide 7.

| Slide | Mốc tập | Vai trò trong bài nói |
| --- | --- | --- |
| 1 | 0:00-0:45 | Our decisions after Stand Up 1 |
| 2 | 0:45-1:30 | Our story questions and scope |
| 3 | 1:30-2:10 | Evidence behind our comparison |
| 4 | 2:10-3:05 | Chart choices for comparison and age composition |
| 5 | 3:05-3:45 | Event categories and an open design decision |
| 6 | 3:45-4:45 | Implementation decisions and the next checkpoint |
| 7 | Chỉ khi hỏi | Data exploration and checks |

## Slide 1 - Our decisions after Stand Up 1

Time: 0:00-0:45.

| Say in English | Point to / action |
| --- | --- |
| Hi, I am Huy. I helped build our website and tutorial-based charts, and practised running the basic KNIME workflow. | Chỉ dòng tên/đóng góp phía dưới. Nêu đúng phần Huy trực tiếp tham gia. |
| After Stand Up 1, the feedback was that we mainly applied what we had learned and needed deeper exploration and a stronger story. | Chỉ cột Feedback ở bên trái. Đây là nhóm tóm tắt nhận xét, không phải trích nguyên văn của thầy. |
| We decided to organise the website around questions, audit more of the dataset, and choose charts by the comparisons readers need to make. | Chỉ từng hàng Our decision bên phải. Nhấn decided để thể hiện phản hồi dẫn đến quyết định cụ thể. |
| The following slides show those choices and the evidence behind them. | Chuyển slide 2. Không đọc lại toàn bộ bảng. |

## Slide 2 - Our story questions and scope

Time: 0:45-1:30.

| Say in English | Point to / action |
| --- | --- |
| Our main question is: what differences disappear when road injuries become one national total? | Chỉ câu hỏi lớn phía trên bảng. |
| We chose three supporting questions: did every road user follow the national change, which event categories appear within a group, and how does age composition differ? | Chỉ ba hàng Compare, Events và Ages theo thứ tự. Chỉ nói câu hỏi, không đọc hết cột reason. |
| These move readers from a comparison into two group profiles. We explored month and remoteness too, but kept the main story focused. | Chỉ cột Why we kept it, rồi dòng Supporting exploration bên dưới. |
| We postponed bed-day and death ratios because definitions and missing values still need resolving. | Chỉ dòng Deferred. Giải thích đây là một quyết định sau audit, không phải quên xử lý dữ liệu. |

## Slide 3 - Evidence behind our comparison

Time: 1:30-2:10.

| Say in English | Point to / action |
| --- | --- |
| The national total fell by 4.8% between 2019 and 2020, while cyclist hospitalisations rose by 14.1%. | Chỉ -4.8%, +14.1%, rồi hai cặp số cùng giai đoạn. |
| We chose that pair because it shows the contrast and avoids the known 2012 and 2017 recording breaks. | Chỉ dòng Why 2019-2020 phía trên các con số. |
| We focus on cyclists because the increase is 1,030 hospitalisations. They are not the only group that increased. | Chỉ nhãn cyclist và hai số 7,302 / 8,332. Nếu bị hỏi nhóm khác, dùng Q&A pick-up/van 260 / 300. |
| Our audit matches 187 published control totals. This supports the counts, while the cause of the change remains unproven. | Chỉ dòng 187 controls phía dưới. Không giải thích toàn bộ T1/T2/T4 ở đây. |

## Slide 4 - Chart choices for comparison and age composition

Time: 2:10-3:05.

| Say in English | Point to / action |
| --- | --- |
| For the two-year question, we propose a dumbbell because connected positions show direction and size on one scale. Grouped bars are the simpler alternative. | Chỉ dumbbell, hai ký hiệu năm và hàng cyclist. Nói propose vì chart D3 mới chưa được triển khai. |
| For age composition, we propose a heatmap to compare several profiles in one grid. Within-group percentages help when totals differ. | Chỉ heatmap và nhãn Within each road-user total (%). |
| In 2021, ages 40-64 account for 41.6% of cyclist hospitalisations, including Unknown in the denominator. | Chỉ ô 41.6 hàng cyclist và cột Unk. ở cuối. Đây là profile năm 2021, không giải thích nguyên nhân thay đổi 2020. |
| We keep exact tables and selected-group bars for precise reading and mobile use. | Chỉ dòng alternative phía dưới. Giữ lời giải thích ngắn, không đọc từng ô. |

## Slide 5 - Event categories and an open design decision

Time: 3:05-3:45.

| Say in English | Point to / action |
| --- | --- |
| For the event question, 3,705 of 8,163 cyclist hospitalisations in 2021 were classified as non-collision, or 45.4%. | Chỉ tổng 8,163, dải Non-collision và 45.4%. |
| We keep unspecified events separate. The Sankey follows one total into categories, while a matrix supports comparison across groups. | Chỉ Other and unspecified, rồi dòng matrix alternative. |
| We will evaluate which view helps readers more before finalising that choice. These categories do not establish fault. | Chỉ dòng Open decision/alternative và giới hạn cuối slide. Không nói nhóm đã chốt Sankey hay đã test người dùng. |

## Slide 6 - Implementation decisions and the next checkpoint

Time: 3:45-4:45.

| Say in English | Point to / action |
| --- | --- |
| For the website, we decided on a guided reading order: comparison, events, then ages. Readers can follow one selected road user through the profiles. | Chỉ khối Reading order từ trên xuống. Đây là quyết định layout, không phải list thêm chart. |
| Comparison years and the detail year stay separate, so a profile change cannot silently change the earlier comparison. | Chỉ Compare years: 2019 and 2020, rồi Detail year: 2021. |
| Next, we will validate the new KNIME export and implement the comparison and age views in D3. We will evaluate the event view against its alternative. | Chỉ ba bước coding bên phải. Pipeline hiện tại vẫn có ba output; Counterparty export là bước tiếp theo. |
| Stand Up 2 presents these decisions and sketches. Stand Up 3 will show working interactions and validation evidence. Final refinements will follow the feedback. | Chỉ dòng cuối Week 12. Kết thúc hoặc chuyển demo hiện tại 20 giây nếu đã tập đủ thời gian. |

## Demo web ngắn nếu cần

Sau slide 6, thêm khoảng 20 giây nếu đã tập trước. Tổng bài sẽ khoảng 5 phút. Website vẫn là bản đang chạy trước khi triển khai các chart mới.

1. Mở `http://localhost:8000/web/` bằng server ở repo root.
2. Chọn 2020 và Pedal cyclist. Chỉ tổng 8,332 cùng các view liên kết.
3. Bấm Reset để về 2021/all road users. Kết thúc demo và chuyển Q&A.

Say: "This is our current website. Selecting 2020 and Pedal cyclist updates the linked views and shows 8,332 hospitalisations. The new designs are our next implementation step."

## Slide 7 - Q&A backup: Data exploration and checks

Chỉ mở khi thầy hỏi nhóm đã kiểm tra finding như thế nào. Chỉ 13 fields, rồi 187 controls và ba hàng 11 / 132 / 44. Không đưa phần này vào bài chính.

Say: "We checked all 13 source fields. Our sums match 187 published controls: 11 annual, 132 road-user/year and 44 remoteness/year totals. The new summaries also conserve the road-user totals. Reader evaluation for the revised charts is still pending."

## Q&A - decisions after the feedback

### What did the feedback change?

Short answer: "We kept the working website as a foundation, but changed the way we planned the story. We chose one main question, checked more fields, and specified charts and interactions for the reader's tasks."

Chỉ bảng slide 1. Đóng góp cá nhân của Huy vẫn là web/chart theo tutorial và thực hành workflow. Phần phân tích/thiết kế chung dùng "our team".

### Why these three questions?

Short answer: "The year comparison reveals a difference hidden by the total. Event categories describe what is recorded within a group. Age shares compare the composition of groups with different sizes. Each question has source fields, a checked calculation and a specific reader task."

Website giữ thứ tự Compare, Events, Ages. Slide 4 đặt dumbbell và heatmap cạnh nhau để giải thích hai lựa chọn encoding. Profile 2021 không giải thích nguyên nhân tăng năm 2020.

### Why leave other variables out of the main story?

Short answer: "We explored month and remoteness, but adding every field as a filter would make the story harder to follow. We kept them as supporting analysis. We postponed bed-day and death ratios until the definitions and missing values are resolved."

Đây là quyết định về phạm vi nội dung. Nhóm vẫn giữ dữ liệu/EDA để trả lời thêm. Không nói dữ liệu không có giá trị chỉ vì không đưa vào bài nói chính.

### Which decisions are settled, and which remain open?

Short answer: "The main question, three chapters and separate comparison/detail years are our current design decisions. Dumbbell and heatmap are proposed for implementation. Sankey versus matrix remains open until we evaluate the task. None of the revised interactions has been presented as completed code."

Xem [decision log](DECISIONS_AFTER_STANDUP1.md) để đối chiếu quyết định với evidence và trạng thái. Không nói thầy đã duyệt các quyết định mới nếu chưa nhận được phản hồi.

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

Slide 4 displays three selected road users. The full design has all 12. Unk. means Unknown. The age bands have unequal widths, so this is composition across categories rather than an age-specific risk measure.

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

## Before presenting

- Export the seven-slide deck (six main slides and one Q&A backup) as `Gr_01_StandUp2.pptx` and check all slides and notes on the presentation laptop.
- Import `Gr_01_StandUp2.knwf`. Confirm the bundled workbook, the three executed export branches and workflow-relative paths. Desktop re-import of this renamed package remains a local check.
- Rehearse the script aloud with pointing and a timer. Aim around 4:45, with the lecturer-confirmed longer format. If it runs long, shorten the wording before increasing speed.
- Have the design review and existing website ready for Q&A. The main talk uses slides 1-6. Slide 7 is Q&A only. A short demonstration should keep the total around 5 minutes.
- Use the revised PPTX and current Design Book/KNIME for the 23 November presentation. Submit files separately under the tutor's arrangement. The original night-before submission date was 22 November. The download ZIP is for transferring files.
- Both Huy and Nhat attend. Huy presents Stand Up 2. Confirm the Week 12 date with the tutorial schedule.

AI use: AI assisted with these notes and the presentation. Huy should rehearse the reasoning and use his own words. The script reflects the personal work the user confirmed. It does not assign Huy the deeper audit or claim completed participant testing.

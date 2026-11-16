# Gr_01 - Chuẩn bị Stand Up 1

Chuẩn bị: 16/11/2026. Buổi trình bày: ngày mai theo lịch Bro cung cấp.
Nhóm: Nguyen Huyen Minh Nhat và Le Tuan Huy.

## 1. Bộ nộp và những thứ cần mở sẵn

- `Gr_01_Stand_Up_1.pptx`: 5 slide, tối đa 5 phút.
- `Gr_01_Design_Book_Draft.pdf`: bản nháp Design Book, chưa phải báo cáo cuối.
- `Gr_01.knwf`: có tên nhóm, workbook, 3 CSV và dữ liệu node đã lưu.
- Link repo trong Submission Comment. PDF yêu cầu GitHub Classroom; repo GitHub thường cần tutor xác nhận chấp nhận. Chưa có bằng chứng nhóm đã vào Classroom.
- Mở sẵn website local và KNIME. Không nộp ZIP. PDF không cho resubmit, nên kiểm tra đúng file trước khi nộp.

PDF hiển thị 22/11 lúc 23:59, nhưng phần Due date yêu cầu hai tối trước Stand Up và nộp trước tutorial. Nếu Stand Up là ngày mai thì mốc hai tối đã qua: kiểm tra Canvas và nộp sớm nhất có thể, không đợi đến 22/11. Chưa có bằng chứng đã nộp Canvas.

## 2. Chia phần nói đề xuất - 4 phút 35 giây

| Slide | Người nói | Thời gian | Nội dung |
| --- | --- | --- | --- |
| 1 | Nhật | 40 giây | Problem, audience, purpose và câu hỏi |
| 2 | Huy | 55 giây | Source, governance và dictionary |
| 3 | Nhật | 65 giây | KNIME và kiểm tra dữ liệu |
| 4 | Huy | 75 giây | Findings và ví dụ prototype |
| 5 | Nhật | 40 giây | Tiến độ, khó khăn và next steps |

Hai người cần thống nhất cách chia này. Chia slide không đồng nghĩa với ghi nhận ai đã viết code tương ứng. Mỗi người chuẩn bị một ví dụ đóng góp thật của mình và xác nhận kênh liên lạc nhóm đang dùng. Cả hai phải hiểu toàn bộ project để trả lời Q&A.

## 3. Speaking cues bằng tiếng Anh

### Slide 1 - Nhat

Our project explores hospitalised road injuries in Australia from 2011 to 2021. We are Gr_01, Nguyen Huyen Minh Nhat and Le Tuan Huy. Our audience is the general public and students interested in road safety. We want users to explore the national trend, compare road user groups, and look at age and sex within a selected group. The prototype is already linked to processed data. Today we will show the pipeline, a few initial findings and what is still in progress.

### Slide 2 - Huy

We use the September 2023 workbook published by BITRE, based on AIHW hospital data. The original worksheet has 117,919 aggregated records. We keep the Traffic category, leaving 86,140 records, and sum Hospitalisations. Counting rows would be wrong because one row is a grouped record. Our main fields are year, road user, age, sex and the hospitalisation count. We retain unknown categories and zero values. The data has no direct patient identifiers. We also explain that the recording changes in 2012 and 2017 affect comparisons, and counts alone do not show individual risk.

### Slide 3 - Nhat

The KNIME workflow has ten nodes. It reads the Excel worksheet, filters Traffic, selects and renames fields, then creates three grouped exports. The annual file has eleven rows. The road user file has 132, and the demographic file has 1,683. We checked the outputs independently against the raw records and the published annual totals. All eleven annual totals match. The script also compares the processed CSVs with the copies loaded by D3. This matters because an old website copy could otherwise show different numbers. Six automated tests cover linked views and invalid data. The prepared team workflow keeps the original data and node settings.

### Slide 4 - Huy

The annual count increases from 34,033 in 2011 to 39,505 in 2021, an increase of 16.1 percent. Car drivers have the largest count in 2021, at 13,327. Pedal cyclist hospitalisations rise from 5,391 to 8,163, an increase of 51.4 percent. These are descriptive changes, not evidence that cycling became more dangerous. The prototype lets us select a year or road user and updates the related charts. For example, selecting Pedal cyclist in 2021 shows 8,163 and the matching age and sex distribution. Reset returns to all road users in 2021. A table provides the exact demographic values.

### Slide 5 - Nhat

The processing pipeline and linked prototype are implemented. Our Design Book is still a draft. A practical challenge is keeping the exports and website data aligned; the verification script now checks that boundary. We also need to finish the design explanation and test the website with real participants. Our next steps are to complete the evidence, run usability tasks and record the improvements. We have not completed user evaluation or final submission yet.

Dùng cues để tập nói bằng lời của mình; không đọc code comments. 4:35 là mục tiêu, chưa phải thời gian rehearsal đã đo. Nếu demo trực tiếp, thao tác trong lúc nói slide 4, không cộng thêm một phần demo dài.

## 4. Demo ngắn và kết quả cần thấy

1. Từ thư mục project, chạy `py -m http.server 8000 --directory web` trong PowerShell. Mở http://localhost:8000/.
2. Mặc định 2021 + All road users: **39,505**.
3. Chọn Pedal cyclist: **8,163**. Chọn 2011: **5,391**. Chỉ vào phần tuổi/giới tính cập nhật.
4. Bấm Reset: 2021 + All road users, **39,505**. Mở bảng dữ liệu nếu tutor hỏi số chính xác.
5. Mở `Gr_01.knwf` trong KNIME, chỉ đường đi Excel Reader -> Traffic filter -> GroupBy -> CSV Writer. Nếu demo lỗi, dùng hình trong slides và giải thích đúng lỗi gặp phải.

Trước khi nộp, import `Gr_01.knwf` trên máy của nhóm để kiểm tra dữ liệu và node. Cấu trúc archive, CSV và sự nguyên vẹn của cấu hình đã được kiểm tra. Chưa chạy lại KNIME desktop sau khi đổi tên nhóm. Kiểm tra dữ liệu và 6/6 Node tests PASS; chưa xác nhận lại giao diện bằng browser trong lượt này.

## 5. Q&A cả hai cần trả lời được

| Câu hỏi | Trả lời ngắn bằng tiếng Anh |
| --- | --- |
| Why this topic and audience? | Hospitalisation shows another part of the impact beyond fatalities. The site explains broad patterns for non-specialists. |
| BITRE or AIHW? | BITRE publishes the workbook; underlying hospital data comes from AIHW's National Hospital Morbidity Database. |
| What does one row represent? | An aggregated combination of source dimensions, not one patient. We sum Hospitalisations. |
| Why filter Traffic? | Our question concerns road vehicle traffic injuries. Other cause categories change the scope. |
| Why three CSVs? | Three aggregation levels from one workbook, not three independent sources. |
| Why keep unknowns and zeros? | Removing them would hide recorded categories or change totals. |
| How did you check correctness? | Reconcile raw Traffic records, all eleven T1 totals and the actual CSVs served by the website. |
| Why these charts? | A line shows change over time; sorted bars support category comparison; grouped bars compare demographic counts. |
| Which group has the highest risk? | We cannot determine that without suitable exposure denominators. Recording changes also affect comparisons. |
| Have you tested usability? | We have technical checks, but no completed study with independent participants yet. |
| How did you use AI? | AI helped with configuration, implementation, checks and draft preparation. The source records prompt summaries; we must explain and verify the work. |
| What did each person do? | State one real completed contribution each. Speaking order and repository ownership do not prove code authorship. |

## 6. Kiểm tra trước buổi trình bày - khoảng 15 phút

1. Cả hai mở PPTX và thống nhất phần nói, đóng góp thật và kênh liên lạc đang dùng.
2. Chạy demo và import KNIME trên máy mang đến lớp.
3. Tập một lượt có bấm giờ: mục tiêu 4:35, tối đa 5:00. Cả hai thử trả lời Q&A.
4. Kiểm tra đúng file và link trước khi Submit vì PDF không cho resubmit.
5. Cả hai có mặt và sẵn sàng show ví dụ. Stand Up 0 điểm; criterion là Progress Report, xét tiến độ và teamwork.

## 7. Cập nhật repository khi cần

GitHub trả 403 khi ghi; chưa có commit hoặc push mới từ lượt chuẩn bị này. File `Gr_01_Team_Update.patch` chỉ chứa thay đổi source và tài liệu. KNIME và PowerPoint/PDF được cung cấp riêng, không nằm trong patch.

Sau khi tải patch và KNIME về Downloads, mở PowerShell tại đúng repo `COS30045`:

```powershell
git status --short
git apply --check "$env:USERPROFILE\Downloads\Gr_01_Team_Update.patch"
git apply "$env:USERPROFILE\Downloads\Gr_01_Team_Update.patch"
Copy-Item "$env:USERPROFILE\Downloads\Gr_01.knwf" ".\knime\Gr_01.knwf"
git diff --stat
```

Nếu `git apply --check` báo lỗi thì dừng ở đó và gửi lỗi; không dùng force/reset. Nếu có thay đổi trùng file đang làm, giữ lại để đối chiếu trước. Chưa cần commit/push để tập trình bày bằng ba file đã tải.

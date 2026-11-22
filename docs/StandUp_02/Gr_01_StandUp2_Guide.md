# Gr_01 - Stand Up 2: file cần dùng và cách tự commit

Bắt đầu bằng việc tải `Gr_01_StandUp2_Files.zip`, giải nén và mở `Gr_01_StandUp2_Huy_Notes.md`. Bộ tải về chứa file thật theo cấu trúc repo. Bro tự copy, xem thay đổi và commit bằng CMD.

## 1. Stand Up 2 sẽ trình bày gì?

Huy trình bày ngày 23/11/2026. Cả hai thành viên tham dự. Giảng viên đã thông báo Stand Up 2 và 3 cần/nên hơn 3 phút, theo xác nhận của nhóm ngày 22/11. Thông báo mới thay cho mốc dưới 3 phút trong PDF cũ.

Bài này dùng 5 slide chính, script 470 từ tiếng Anh. Mục tiêu tập là 4:30, thường trong khoảng 4-5 phút trước Q&A. Đây là đề xuất để kiểm soát nhịp nói, không phải giới hạn mới của giảng viên.

| Slide | Mốc tập | Nội dung |
| --- | --- | --- |
| 1 | 0:00-0:45 | Huy đã làm gì, feedback sau Stand Up 1 và finding tổng giảm 4.8% nhưng cyclist tăng 14.1% trong 2019-2020 |
| 2 | 0:45-1:30 | Đào sâu 13 trường dữ liệu và đối chiếu 187 tổng do nguồn công bố |
| 3 | 1:30-2:45 | Dumbbell và heatmap: trả lời câu hỏi gì, cách đọc và phương án thay thế |
| 4 | 2:45-3:30 | Counterparty: 45.4% cyclist hospitalisations năm 2021 thuộc non-collision; cân nhắc Sankey/matrix |
| 5 | 3:30-4:30 | Website layout, tương tác, coding plan và công việc cho Stand Up 3 |

Nếu cần show web, thêm một demo 20-30 giây sau slide 5, đưa bài về khoảng 4:50-5:00. Chỉ chọn 2020/Pedal cyclist, chỉ 8,332 và các view liên kết, rồi Reset. Đây là website hiện tại; các chart mới vẫn là thiết kế.

## 2. Tải những file nào?

| File cần lấy | Cách dùng |
| --- | --- |
| `Gr_01_StandUp2_Files.zip` | Bộ file thật để copy vào repo. Có notes MD, hướng dẫn này, tài liệu nguồn, bản Design Book PDF và KNIME. Không cần áp dụng patch |
| `Gr_01_StandUp2_Huy_Notes.md` | Có trong ZIP và có thể tải riêng. Script tiếng Anh, chỉ dẫn trỏ bằng tiếng Việt, demo và Q&A |
| `Gr_01_StandUp2_Guide.md` | Hướng dẫn hiện tại, có ở gốc ZIP và trong thư mục repo |
| `Gr_01_StandUp2.pptx` | Mở [deck 5 slide](https://chatgpt.com/space/page_ea183a7225cc8191ab4a21aee0030aea), dùng Export/Download thành PowerPoint và lưu đúng tên này trong Downloads. PPTX chưa nằm trong ZIP |
| `Gr_01_StandUp2_Design_Book.pdf` và `Gr_01_StandUp2.knwf` | Đã có trong ZIP, ở các đường dẫn bên dưới. Dùng các file này cho submission |

Bên trong ZIP, `repo_files` giữ đúng cấu trúc cần copy:

| Nhóm | Đường dẫn trong repo |
| --- | --- |
| Hướng dẫn và notes | `docs/StandUp_02/README.md`, `docs/StandUp_02/Gr_01_StandUp2_Guide.md`, `docs/StandUp_02/Gr_01_StandUp2_Huy_Notes.md`, `docs/StandUp_02/current_workflow.svg` |
| Kế hoạch và review | `docs/STANDUP_2_3_PLAN.md`, `docs/STANDUP_2_REVIEW.md`, `README.md` |
| Design Book và preview | `docs/design_book/Gr_01_StandUp2_Draft.md`, `docs/design_book/Gr_01_StandUp2_Design_Book.pdf`, `docs/design/preview.html` |
| KNIME | `knime/Gr_01_StandUp2.knwf` |
| Script tạo tài liệu và quy tắc Git | `tools/build_standup2_pack.py`, `tools/build_design_pack.py`, `.gitattributes` |

PPTX sẽ được copy riêng vào `docs/StandUp_02/Gr_01_StandUp2.pptx`. Không cần chạy lại script tạo tài liệu để sử dụng bộ file đã tải. ZIP chỉ dùng để chuyển file; khi nộp bài, nộp PPTX, Design Book PDF và KNIME riêng, kèm link repo.

## 3. Copy file bằng Windows CMD

Chạy từng khối theo thứ tự trong Command Prompt. Các lệnh dưới đây dùng CMD, giống cửa sổ Bro đã gửi.

Giải nén ZIP bằng Extract All vào `%USERPROFILE%\Downloads\Gr_01_StandUp2_Files`. Kiểm tra bên trong thấy trực tiếp thư mục `repo_files`. Lưu PPTX đã export vào Downloads và giữ đúng tên file, không có hậu tố như (1).

Mở repo và kiểm tra trạng thái:

```bat
cd /d "D:\Swinburne\7th Sem\COS30045 - Data Visualization\COS30045"
git status --short
```

Nếu lệnh status không in gì thì tiếp tục. Nếu có thay đổi đang làm dở, giữ nguyên và xử lý trước khi copy đè các file cùng tên.

```bat
git switch main
git pull --ff-only
git config --local user.name "Nguyen Huyen Minh Nhat"
git config --local user.email "john.bibibi@gmail.com"
dir "%USERPROFILE%\Downloads\Gr_01_StandUp2_Files\repo_files"
dir "%USERPROFILE%\Downloads\Gr_01_StandUp2.pptx"
```

Chỉ copy khi cả thư mục và PPTX đều tìm thấy. Nếu `git pull` báo lỗi, dừng tại lỗi đó.

```bat
xcopy "%USERPROFILE%\Downloads\Gr_01_StandUp2_Files\repo_files\*" "." /E /I /Y
copy /Y "%USERPROFILE%\Downloads\Gr_01_StandUp2.pptx" "docs\StandUp_02\Gr_01_StandUp2.pptx"
git status --short
git diff --stat
```

Các file notes được giữ ở dạng MD. Bản notes PDF và các patch cũ không cần thêm vào commit này.

## 4. Kiểm tra rồi commit dưới tên Nhat

Chỉ stage những file thuộc bộ Stand Up 2:

```bat
git add -- .gitattributes README.md docs/STANDUP_2_3_PLAN.md docs/STANDUP_2_REVIEW.md docs/design/preview.html
git add -- docs/StandUp_02/README.md docs/StandUp_02/Gr_01_StandUp2_Guide.md docs/StandUp_02/Gr_01_StandUp2_Huy_Notes.md docs/StandUp_02/current_workflow.svg docs/StandUp_02/Gr_01_StandUp2.pptx
git add -- docs/design_book/Gr_01_StandUp2_Draft.md docs/design_book/Gr_01_StandUp2_Design_Book.pdf knime/Gr_01_StandUp2.knwf tools/build_standup2_pack.py tools/build_design_pack.py
git diff --cached --check
git diff --cached --stat
```

`--check` không in gì nghĩa là không phát hiện lỗi whitespace. Xem thay đổi phần notes và plan:

```bat
git diff --cached -- docs/StandUp_02/Gr_01_StandUp2_Huy_Notes.md docs/STANDUP_2_3_PLAN.md
```

Nếu Git mở trang cuộn, bấm q để thoát. Sau khi kiểm tra:

```bat
git commit -m "docs: finalize Huy's Stand Up 2 materials"
git log -1 --format=fuller
git push origin main
git status -sb
```

Author và Commit phải là Nguyen Huyen Minh Nhat với email đã đặt. Nếu lệnh nào báo lỗi, dừng và gửi output để xử lý. Tôi chưa commit/push bản cập nhật này; commit được tạo từ CLI của Bro.

## 5. Cải thiện gì và còn kiểm tra gì?

| Stand Up 1 | Stand Up 2 |
| --- | --- |
| Mô tả tổng, ranking và demographics | Câu hỏi có finding cụ thể: xu hướng tổng có che khuất khác biệt giữa road users không? |
| Pipeline cơ bản và ba CSV | Audit 13 trường, 187 tổng đối chiếu, kiểm tra missing/zero và các tổng phân nhóm |
| Chart theo tutorial | Đề xuất dumbbell, heatmap và Sankey/matrix; giải thích lựa chọn, encoding và tradeoff |
| Tương tác chọn năm/road user cơ bản | Đặc tả năm so sánh và năm detail riêng, shared state, bảng số liệu và phương án mobile |

Design Book PDF có 12 trang, gồm xử lý/EDA và ba phần thiết kế 3.1-3.3. KNIME có tên nhóm, workbook và dữ liệu thực thi đã lưu; archive và ba CSV đã qua kiểm tra tĩnh. Notes chỉ nhận đúng đóng góp Huy đã xác nhận: dựng web/chart theo tutorial và thực hành workflow cơ bản.

Trước buổi nói, còn 4 việc trên laptop:

1. Mở PPTX, xem đủ 5 slide và speaker notes; mở Design Book PDF.
2. Import `Gr_01_StandUp2.knwf`, kiểm tra Excel Reader dùng workbook bên trong và workflow chạy được.
3. Chạy `py -m http.server 8000` tại repo root. Kiểm tra `http://localhost:8000/web/` và `http://localhost:8000/docs/design/preview.html`.
4. Tập đủ bài với đồng hồ và thao tác trỏ. Giữ mỗi slide một ý chính; để công thức chi tiết, code và các câu hỏi phụ cho Q&A.

Stand Up 3 sẽ dành cho chart D3 chạy thật, Counterparty export mới, tương tác và kết quả đánh giá. Final demo dành cho phiên bản hoàn thiện sau feedback. Các phần đó chưa được coi là hoàn thành trong Stand Up 2.

Nộp các file riêng vào tối 22/11 theo lịch thuyết trình 23/11 nhóm đã xác nhận. Dùng [repo của nhóm](https://github.com/lucianle1024/COS30045); nhóm đã được xác nhận không cần Classroom/Mercury.

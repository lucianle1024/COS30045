# Gr_01 - Stand Up 2: cập nhật slide và quyết định sau feedback

Bản cập nhật ngày 23/11/2026, dựa trên commit a608322 mà Bro đã push. Bộ này tập trung sửa cách trình bày quyết định sau Stand Up 1. Notes giữ dạng Markdown.

## 1. Cần dùng bản nào?

Deck mới có 7 slide: 6 slide chính và slide 7 audit dự phòng. Script tiếng Anh có 441 từ, chỉ dẫn trỏ bằng tiếng Việt, mục tiêu tập khoảng 4:45 trước Q&A. Demo website hiện tại thêm khoảng 20 giây nếu cần, đưa tổng bài về khoảng 5 phút. Giảng viên đã xác nhận format hơn 3 phút; đây là mục tiêu tập của nhóm.

Mạch nói là feedback, quyết định, câu hỏi và phạm vi được chọn, bằng chứng, rồi bước tiếp theo. Xem `DECISIONS_AFTER_STANDUP1.md` nếu cần ôn lý do. Huy nói phần mình làm về web/chart theo tutorial và thực hành KNIME. Phân tích/thiết kế chung dùng "our team".

## 2. File tải về và vị trí copy

1. Tải `Gr_01_StandUp2_Story_Update.zip`, Extract All vào Downloads. Bên trong phải thấy thư mục `repo_files`.
2. Mở [deck đã cập nhật](https://chatgpt.com/space/page_ea183a7225cc8191ab4a21aee0030aea), export/download lại thành PowerPoint. Lưu `Gr_01_StandUp2.pptx` vào Downloads, thay bản cũ.
3. Notes MD và hướng dẫn này có trong ZIP; có thể tải riêng để đọc. Đảm bảo Windows không thêm (1) vào tên file.

| Nhóm | Vị trí trong repo |
| --- | --- |
| Notes và quyết định | `docs/StandUp_02/Gr_01_StandUp2_Huy_Notes.md`, `docs/StandUp_02/DECISIONS_AFTER_STANDUP1.md` |
| Hướng dẫn và mục lục | `docs/StandUp_02/Gr_01_StandUp2_Guide.md`, `docs/StandUp_02/README.md` |
| Plan, review và storyboard | `docs/STANDUP_2_3_PLAN.md`, `docs/STANDUP_2_REVIEW.md`, `docs/STORYBOARD.md` |
| Preview và script | `docs/design/preview.html`, `tools/build_design_pack.py`, `tools/build_standup2_pack.py` |
| PowerPoint export riêng | `docs/StandUp_02/Gr_01_StandUp2.pptx` |

Design Book PDF và KNIME của commit a608322 tiếp tục được dùng. Bộ cập nhật này không thay dữ liệu, workflow hoặc code production website.

## 3. Copy bằng CMD

Chạy từng khối tại Command Prompt. Nếu lệnh báo lỗi, dừng tại đó.

```bat
cd /d "D:\Swinburne\7th Sem\COS30045 - Data Visualization\COS30045"
git status --short
```

Nếu status không in gì, tiếp tục. Nếu đang có thay đổi, xử lý trước khi chép đè các file cùng tên.

```bat
git switch main
git pull --ff-only
git config --local user.name "Nguyen Huyen Minh Nhat"
git config --local user.email "john.bibibi@gmail.com"
dir "%USERPROFILE%\Downloads\Gr_01_StandUp2_Story_Update\repo_files"
dir "%USERPROFILE%\Downloads\Gr_01_StandUp2.pptx"
```

Khi cả thư mục và PPTX đều tìm thấy:

```bat
xcopy "%USERPROFILE%\Downloads\Gr_01_StandUp2_Story_Update\repo_files\*" "." /E /I /Y
copy /Y "%USERPROFILE%\Downloads\Gr_01_StandUp2.pptx" "docs\StandUp_02\Gr_01_StandUp2.pptx"
git status --short
start "" "docs\StandUp_02\Gr_01_StandUp2.pptx"
```

Kiểm tra đủ 7 slide và speaker notes. Bài nói dừng ở slide 6, slide 7 chỉ mở khi hỏi audit. Tập với đồng hồ; rút ngắn wording nếu quá giờ, không tăng tốc đọc hết bảng.

## 4. Check và commit dưới tên Bro

```bat
git add -- docs/StandUp_02 docs/STANDUP_2_3_PLAN.md docs/STANDUP_2_REVIEW.md docs/STORYBOARD.md docs/design/preview.html tools/build_design_pack.py tools/build_standup2_pack.py
git diff --cached --check
git diff --cached --stat
```

`--check` không in gì nghĩa là không phát hiện lỗi whitespace. Với base a608322 và PPTX đã export lại, dự kiến 11 file thay đổi. Không cần thêm ZIP hoặc patch vào repo.

```bat
git commit -m "docs: explain Stand Up 2 decisions after tutor feedback"
git log -1 --format=fuller
git push origin main
git status -sb
```

Author và Commit phải là Nguyen Huyen Minh Nhat. Kết quả cuối mong đợi là `## main...origin/main` và không có file thay đổi. Bộ này được chuẩn bị để Bro tự commit bằng CLI.

## 5. Những gì Huy cần nắm

| Khi thầy hỏi | Ý trả lời |
| --- | --- |
| Sau feedback, nhóm quyết định gì? | Giữ web đang chạy làm nền, đổi sang một story có câu hỏi, audit thêm fields và chọn chart theo task |
| Vì sao chọn ba câu hỏi? | Compare tìm khác biệt bị tổng che khuất; Events mô tả phân loại ghi nhận; Ages so sánh cơ cấu khi totals khác nhau |
| Vì sao không đưa mọi biến vào web? | Month/remoteness là nghiên cứu hỗ trợ; ratios còn vướng definitions/missingness; giữ story tập trung |
| Đã chốt chart chưa? | Dumbbell/heatmap là phương án thiết kế để implement. Sankey/matrix vẫn cần đánh giá |
| Stand Up 3 sẽ có gì? | Chart/interactions chạy thật, export mới đã đối chiếu, bằng chứng validation và evaluation |

Chỉ nộp PPTX, Design Book PDF và KNIME riêng cùng link repo theo hướng dẫn giảng viên. ZIP dùng để chuyển các file cập nhật.

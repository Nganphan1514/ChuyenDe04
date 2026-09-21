# SleepAlert AI Design Review & Ergonomic Assessment Report

> **Provenance**
> - **Source prompt:** [P4.4 — AI Design Review](../prompts/review-design.prompt.md)
> - **Artifact status:** `Accepted reviewed sample`
> - **Human action:** Evaluated critique findings, prioritized ergonomic fixes, and confirmed automotive safety standards.
> - **Reproduction note:** Structured heuristic review conducted prior to code implementation.

---

## 1. Phương pháp Đánh giá & Tiêu chuẩn So chiếu

Đội ngũ phát triển đã sử dụng các tiêu chuẩn quốc tế về công thái học buồng lái phương tiện giao thông để thực hiện phiên thẩm tra AI Design Review:
* **NHTSA Visual-Manual Driver Distraction Guidelines:** Quy định tài xế không được rời mắt khỏi mặt đường quá 2.0 giây cho một tác vụ, và mỗi lần liếc nhìn không quá 1.0 giây.
* **ISO 15008:** Yêu cầu về độ tương phản, kích thước ký tự và góc nhìn của màn hình hiển thị trong xe cơ giới ban ngày lẫn ban đêm.
* **WCAG 2.1 AAA:** Độ tương phản màu sắc cho các trạng thái nguy hiểm tối thiểu đạt tỷ lệ 7:1.

---

## 2. Bảng Thẩm định Chi tiết (Findings & Prioritized Actions)

```text
┌────┬──────────────┬──────────┬─────────────────────────────────────┬─────────────────────────────────────┬────────────────────────────────────┐
│ ID │ Lĩnh vực     │ Mức độ   │ Vấn đề nhận diện                    │ Cơ sở công thái học                 │ Hành động khắc phục đã áp dụng     │
├────┼──────────────┼──────────┼─────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────┤
│ F1 │ Glanceability│ CRITICAL │ Ban đầu biểu đồ PERCLOS hiển thị    │ Đọc biểu đồ đường tốn > 2.5 giây,   │ Chuyển thành thanh Bar màu lớn     │
│    │              │          │ dạng đồ thị sóng dao động phức tạp. │ gây xao nhãng nguy hiểm khi lái xe. │ kết hợp chữ số to đoản mạch.       │
├────┼──────────────┼──────────┼─────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────┤
│ F2 │ Night-Vision │ HIGH     │ Nền xám nhạt ở bản nháp đầu tiên    │ Ánh sáng nền làm co đồng tử mắt tài │ Đổi toàn bộ sang nền True Black    │
│    │              │          │ gây chói trong cabin tối đêm.       │ xế, giảm tầm nhìn bóng tối ngoài xe.│ (#0B0F19), giảm độ sáng màn hình.  │
├────┼──────────────┼──────────┼─────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────┤
│ F3 │ Audio Bias   │ HIGH     │ Chỉ dựa vào pop-up hình ảnh khi     │ Khi ngủ gật, mắt tài xế đang nhắm,  │ Kích hoạt còi hú tức thì (< 500ms),│
│    │              │          │ xảy ra vi giấc ngủ (microsleep).    │ không thể nhìn thấy bất kỳ modal nào│ hình ảnh chỉ đóng vai trò thứ cấp. │
├────┼──────────────┼──────────┼─────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────┤
│ F4 │ Cognitive    │ MEDIUM   │ Thông báo trạm dừng chân hiện chữ   │ Tài xế đang mệt mỏi không thể đọc   │ Dùng Text-to-Speech đọc to địa điểm│
│    │ Load         │          │ quá dài và địa chỉ nhiều dòng.      │ văn bản dài trên màn hình.          │ và chỉ hiện icon trạm + số km.     │
├────┼──────────────┼──────────┼─────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────┤
│ F5 │ Fleet Triage │ MEDIUM   │ Dashboard đội xe xếp theo thứ tự ID │ Điều hành viên khó phát hiện xe nào │ Tự động ghim các xe đang ở trạng   │
│    │              │          │ xe tĩnh, không ưu tiên xe nguy hiểm.│ đang có báo động đỏ trong 30 xe.    │ thái BÁO ĐỘNG ĐỎ lên đầu bảng.     │
└────┴──────────────┴──────────┴─────────────────────────────────────┴─────────────────────────────────────┴────────────────────────────────────┘
```

---

## 3. Kết luận của Phiên Review

1. **Phê duyệt Bản mẫu:** Giao diện buồng lái (HUD) và Bảng điều khiển Đội xe đã giải quyết triệt để các rủi ro gây mất tập trung, tuân thủ nghiêm ngặt quy tắc quan sát dưới 1 giây.
2. **Ủy quyền Triển khai:** Thiết kế này đã sẵn sàng để tích hợp vào bản mẫu tương tác thực tế (`prototype/index.html`) và chuẩn bị cho Chapter 5 (Thiết kế Kiến trúc Phần mềm).
